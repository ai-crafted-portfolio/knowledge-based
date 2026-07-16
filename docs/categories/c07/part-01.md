---
search:
  exclude: true
---

# Db2 for z/OS — 詳細 (1/3)

[← Db2 for z/OS の概要へ戻る](index.md)


## BIND/REBINDオプション > BIND PACKAGE / BIND PLAN


<section class="kb-item" id="c07-i0001"><h3>ACTION</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>ACTIONは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（5問）</summary><div class="kb-q"><p><strong>問題.</strong> 追加置換を導入設計で確認します。Db2の作業記録に追加と置換の扱いの根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. ACTION <span class="kb-ok">✅ 正解</span></li><li>B. RELEASE</li><li>C. CURRENTDATA</li><li>D. ENCODING</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答追加置換はAです。論点追加置換における指定名 ACTION の確認軸名は追加置換確認です。変更申請の置換可否と一致させますので、目的名は追加置換目的です。追加置換で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は追加置換説明です。Aが正解です。論点追加置換の指定名 ACTION が該当します。目的追加置換で読むパッケージカタログの根拠名は追加置換根拠です。誤答B追加置換は資源解放の時点の選択で、主題は追加置換です。除外B追加置換では資源解放の時点を外す理由も追加置換誤答です。誤答C追加置換はカーソル読み取りの現在性の選択で、主題は追加置換です。除外C追加置換ではカーソル読み取りの現在性を外す理由も追加置換誤答です。誤答D追加置換は文字データの符号化の選択で、主題は追加置換です。除外D追加置換では文字データの符号化を外す理由も追加置換誤答です。初出語追加置換として、指定名 ACTION はDb2の指定または確認表であり焦点は追加置換定義です。位置付け追加置換は追加と置換の扱い位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 追加置換を変更審査で確認します。Db2の作業記録に追加と置換の扱いの根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. SQLERROR</li><li>B. ACTION <span class="kb-ok">✅ 正解</span></li><li>C. CONCENTRATESTMT</li><li>D. QUALIFIER</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答追加置換はBです。論点追加置換における指定名 ACTION の確認軸名は追加置換確認です。変更申請の置換可否と一致させますので、目的名は追加置換目的です。追加置換で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は追加置換説明です。誤答A追加置換はSQLエラー時の成果物作成の選択で、主題は追加置換です。除外A追加置換ではSQLエラー時の成果物作成を外す理由も追加置換誤答です。Bが正解です。論点追加置換の指定名 ACTION が該当します。目的追加置換で読むパッケージカタログの根拠名は追加置換根拠です。誤答C追加置換は動的SQL文の集約の選択で、主題は追加置換です。除外C追加置換では動的SQL文の集約を外す理由も追加置換誤答です。誤答D追加置換は未修飾表名のスキーマの選択で、主題は追加置換です。除外D追加置換では未修飾表名のスキーマを外す理由も追加置換誤答です。初出語追加置換として、指定名 ACTION はDb2の指定または確認表であり焦点は追加置換定義です。位置付け追加置換は追加と置換の扱い位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 追加置換を性能調査で確認します。Db2の作業記録に追加と置換の扱いの根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. SWITCH(PREVIOUS)</li><li>C. ACTION <span class="kb-ok">✅ 正解</span></li><li>D. APPLCOMPAT</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答追加置換はCです。論点追加置換における指定名 ACTION の確認軸名は追加置換確認です。変更申請の置換可否と一致させますので、目的名は追加置換目的です。追加置換で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は追加置換説明です。誤答A追加置換はアクセスパス情報の出力の選択で、主題は追加置換です。除外A追加置換ではアクセスパス情報の出力を外す理由も追加置換誤答です。誤答B追加置換は前回コピーへの切り替えの選択で、主題は追加置換です。除外B追加置換では前回コピーへの切り替えを外す理由も追加置換誤答です。Cが正解です。論点追加置換の指定名 ACTION が該当します。目的追加置換で読むパッケージカタログの根拠名は追加置換根拠です。誤答D追加置換は互換性レベルの選択で、主題は追加置換です。除外D追加置換では互換性レベルを外す理由も追加置換誤答です。初出語追加置換として、指定名 ACTION はDb2の指定または確認表であり焦点は追加置換定義です。位置付け追加置換は追加と置換の扱い位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 追加置換を障害復旧で確認します。Db2の作業記録に追加と置換の扱いの根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. ISOLATION</li><li>C. QUERYACCELERATION</li><li>D. ACTION <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答追加置換はDです。論点追加置換における指定名 ACTION の確認軸名は追加置換確認です。変更申請の置換可否と一致させますので、目的名は追加置換目的です。追加置換で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は追加置換説明です。誤答A追加置換は準備済み動的SQL文の保持の選択で、主題は追加置換です。除外A追加置換では準備済み動的SQL文の保持を外す理由も追加置換誤答です。誤答B追加置換は分離レベルの選択で、主題は追加置換です。除外B追加置換では分離レベルを外す理由も追加置換誤答です。誤答C追加置換はアクセラレーター利用方針の選択で、主題は追加置換です。除外C追加置換ではアクセラレーター利用方針を外す理由も追加置換誤答です。Dが正解です。論点追加置換の指定名 ACTION が該当します。目的追加置換で読むパッケージカタログの根拠名は追加置換根拠です。初出語追加置換として、指定名 ACTION はDb2の指定または確認表であり焦点は追加置換定義です。位置付け追加置換は追加と置換の扱い位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 既存パッケージを残すのか、同名パッケージを置き換えるのかをバインド時に指定したい状況です。確認すべき BIND/REBIND オプションはどれですか。</p><ul class="kb-choices"><li>A. ACTION <span class="kb-ok">✅ 正解</span></li><li>B. ENCODING</li><li>C. CURRENTDATA</li><li>D. PATH</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 置換可否を見るなら A を選び、追加と置換の動作は ACTION で決まります。同名資産がある場合は上書きの有無を確認します。B: 文字データの符号化方式を扱います。C: カーソルで現行データを要求するかの指定です。D: ルーチン名などの探索順序を定めます；背景には追加方式を決める BIND/REBIND の ACTION は、新規追加か既存定義の置換かを明確にします、同名パッケージが既にある環境で置換を選ぶと、現行アプリケーションの実行資産が切り替わります、変更申請には対象名、置換可否、戻し方を分けて記録しますという関係があり、この区別で確認する名称は「ACTION」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ACTION</strong></p><p>検証目的: 復旧検査のDb2について、ACTION は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020078の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、復旧検査のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にACTIONを指定し、OSKB020078の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ACTION
CASE OSKB020078
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ACTION
CASE OSKB020078
SOURCE Db2 for z/OS
ACTIONとOSKB020078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020078を同じ出力で読み、復旧検査のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020078
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020078
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020078
DSNV401IとOSKB020078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ACTION と OSKB020078 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0002"><h3>APPLCOMPAT</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 上級</p><p>APPLCOMPATは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></section>


<section class="kb-item" id="c07-i0003"><h3>CURRENTDATA</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>CURRENTDATAは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 現在データ要求を導入設計で確認します。Db2の作業記録にカーソル読み取りの現在性の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. CURRENTDATA <span class="kb-ok">✅ 正解</span></li><li>C. RELEASE</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答現在データ要求はBです。論点現在データ要求における指定名 CURRENTDATA の確認軸名は現在データ要求確認です。並行更新時の読み取り要求を整理しますので、目的名は現在データ要求目的です。現在データ要求で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は現在データ要求説明です。誤答A現在データ要求は前回アクセスパスの再利用の選択で、主題は現在データ要求です。除外A現在データ要求では前回アクセスパスの再利用を外す理由も現在データ要求誤答です。Bが正解です。論点現在データ要求の指定名 CURRENTDATA が該当します。目的現在データ要求で読むパッケージカタログの根拠名は現在データ要求根拠です。誤答C現在データ要求は資源解放の時点の選択で、主題は現在データ要求です。除外C現在データ要求では資源解放の時点を外す理由も現在データ要求誤答です。誤答D現在データ要求は準備済み動的SQL文の保持の選択で、主題は現在データ要求です。除外D現在データ要求では準備済み動的SQL文の保持を外す理由も現在データ要求誤答です。初出語現在データ要求として、指定名 CURRENTDATA はDb2の指定または確認表であり焦点は現在データ要求定義です。位置付け現在データ要求はカーソル読み取りの現在性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 現在データ要求を変更審査で確認します。Db2の作業記録にカーソル読み取りの現在性の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. PLANMGMT</li><li>C. CURRENTDATA <span class="kb-ok">✅ 正解</span></li><li>D. APCOMPARE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答現在データ要求はCです。論点現在データ要求における指定名 CURRENTDATA の確認軸名は現在データ要求確認です。並行更新時の読み取り要求を整理しますので、目的名は現在データ要求目的です。現在データ要求で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は現在データ要求説明です。誤答A現在データ要求は前回コピーへの切り替えの選択で、主題は現在データ要求です。除外A現在データ要求では前回コピーへの切り替えを外す理由も現在データ要求誤答です。誤答B現在データ要求はパッケージコピーの保持の選択で、主題は現在データ要求です。除外B現在データ要求ではパッケージコピーの保持を外す理由も現在データ要求誤答です。Cが正解です。論点現在データ要求の指定名 CURRENTDATA が該当します。目的現在データ要求で読むパッケージカタログの根拠名は現在データ要求根拠です。誤答D現在データ要求はアクセスパス差分の比較の選択で、主題は現在データ要求です。除外D現在データ要求ではアクセスパス差分の比較を外す理由も現在データ要求誤答です。初出語現在データ要求として、指定名 CURRENTDATA はDb2の指定または確認表であり焦点は現在データ要求定義です。位置付け現在データ要求はカーソル読み取りの現在性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 現在データ要求を性能調査で確認します。Db2の作業記録にカーソル読み取りの現在性の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. QUERYACCELERATION</li><li>C. VALIDATE</li><li>D. CURRENTDATA <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答現在データ要求はDです。論点現在データ要求における指定名 CURRENTDATA の確認軸名は現在データ要求確認です。並行更新時の読み取り要求を整理しますので、目的名は現在データ要求目的です。現在データ要求で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は現在データ要求説明です。誤答A現在データ要求は成果物の所有者の選択で、主題は現在データ要求です。除外A現在データ要求では成果物の所有者を外す理由も現在データ要求誤答です。誤答B現在データ要求はアクセラレーター利用方針の選択で、主題は現在データ要求です。除外B現在データ要求ではアクセラレーター利用方針を外す理由も現在データ要求誤答です。誤答C現在データ要求は検査時期の選択で、主題は現在データ要求です。除外C現在データ要求では検査時期を外す理由も現在データ要求誤答です。Dが正解です。論点現在データ要求の指定名 CURRENTDATA が該当します。目的現在データ要求で読むパッケージカタログの根拠名は現在データ要求根拠です。初出語現在データ要求として、指定名 CURRENTDATA はDb2の指定または確認表であり焦点は現在データ要求定義です。位置付け現在データ要求はカーソル読み取りの現在性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 現在データ要求を障害復旧で確認します。Db2の作業記録にカーソル読み取りの現在性の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. CURRENTDATA <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. APCOMPARE</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答現在データ要求はAです。論点現在データ要求における指定名 CURRENTDATA の確認軸名は現在データ要求確認です。並行更新時の読み取り要求を整理しますので、目的名は現在データ要求目的です。現在データ要求で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は現在データ要求説明です。Aが正解です。論点現在データ要求の指定名 CURRENTDATA が該当します。目的現在データ要求で読むパッケージカタログの根拠名は現在データ要求根拠です。誤答B現在データ要求は分離レベルの選択で、主題は現在データ要求です。除外B現在データ要求では分離レベルを外す理由も現在データ要求誤答です。誤答C現在データ要求はアクセスパス差分の比較の選択で、主題は現在データ要求です。除外C現在データ要求ではアクセスパス差分の比較を外す理由も現在データ要求誤答です。誤答D現在データ要求はパッケージコピーの保持の選択で、主題は現在データ要求です。除外D現在データ要求ではパッケージコピーの保持を外す理由も現在データ要求誤答です。初出語現在データ要求として、指定名 CURRENTDATA はDb2の指定または確認表であり焦点は現在データ要求定義です。位置付け現在データ要求はカーソル読み取りの現在性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CURRENTDATA</strong></p><p>検証目的: 置換判定のDb2について、CURRENTDATA は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いがに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020084の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCURRENTDATAを指定し、OSKB020084の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CURRENTDATA
CASE OSKB020084
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CURRENTDATA
CASE OSKB020084
SOURCE Db2 for z/OS
CURRENTDATAとOSKB020084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020084を同じ出力で読み、置換判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020084
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020084
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020084
DSNV401IとOSKB020084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CURRENTDATA と OSKB020084 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0004"><h3>DEGREE</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>DEGREEは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 並列度を導入設計で確認します。Db2の作業記録に並列実行の許可の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. ENCODING</li><li>C. DEGREE <span class="kb-ok">✅ 正解</span></li><li>D. CURRENTDATA</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答並列度はCです。論点並列度における指定名 DEGREE の確認軸名は並列度確認です。中央処理装置余力と応答時間の両方を見ますので、目的名は並列度目的です。並列度で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は並列度説明です。誤答A並列度は前回コピーへの切り替えの選択で、主題は並列度です。除外A並列度では前回コピーへの切り替えを外す理由も並列度誤答です。誤答B並列度は文字データの符号化の選択で、主題は並列度です。除外B並列度では文字データの符号化を外す理由も並列度誤答です。Cが正解です。論点並列度の指定名 DEGREE が該当します。目的並列度で読むパッケージカタログの根拠名は並列度根拠です。誤答D並列度はカーソル読み取りの現在性の選択で、主題は並列度です。除外D並列度ではカーソル読み取りの現在性を外す理由も並列度誤答です。初出語並列度として、指定名 DEGREE はDb2の指定または確認表であり焦点は並列度定義です。位置付け並列度は並列実行の許可位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 並列度を変更審査で確認します。Db2の作業記録に並列実行の許可の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. PLAN_TABLE</li><li>C. APREUSE</li><li>D. DEGREE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答並列度はDです。論点並列度における指定名 DEGREE の確認軸名は並列度確認です。中央処理装置余力と応答時間の両方を見ますので、目的名は並列度目的です。並列度で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は並列度説明です。誤答A並列度は成果物の所有者の選択で、主題は並列度です。除外A並列度では成果物の所有者を外す理由も並列度誤答です。誤答B並列度はEXPLAIN基本表の選択で、主題は並列度です。除外B並列度ではEXPLAIN基本表を外す理由も並列度誤答です。誤答C並列度は前回アクセスパスの再利用の選択で、主題は並列度です。除外C並列度では前回アクセスパスの再利用を外す理由も並列度誤答です。Dが正解です。論点並列度の指定名 DEGREE が該当します。目的並列度で読むパッケージカタログの根拠名は並列度根拠です。初出語並列度として、指定名 DEGREE はDb2の指定または確認表であり焦点は並列度定義です。位置付け並列度は並列実行の許可位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 並列度を性能調査で確認します。Db2の作業記録に並列実行の許可の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. DEGREE <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. ISOLATION</li><li>D. QUALIFIER</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答並列度はAです。論点並列度における指定名 DEGREE の確認軸名は並列度確認です。中央処理装置余力と応答時間の両方を見ますので、目的名は並列度目的です。並列度で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は並列度説明です。Aが正解です。論点並列度の指定名 DEGREE が該当します。目的並列度で読むパッケージカタログの根拠名は並列度根拠です。誤答B並列度は分離レベルの選択で、主題は並列度です。除外B並列度では分離レベルを外す理由も並列度誤答です。誤答C並列度は分離レベルの選択で、主題は並列度です。除外C並列度では分離レベルを外す理由も並列度誤答です。誤答D並列度は未修飾表名のスキーマの選択で、主題は並列度です。除外D並列度では未修飾表名のスキーマを外す理由も並列度誤答です。初出語並列度として、指定名 DEGREE はDb2の指定または確認表であり焦点は並列度定義です。位置付け並列度は並列実行の許可位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 並列度を障害復旧で確認します。Db2の作業記録に並列実行の許可の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. SQLERROR</li><li>B. DEGREE <span class="kb-ok">✅ 正解</span></li><li>C. PLANMGMT</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答並列度はBです。論点並列度における指定名 DEGREE の確認軸名は並列度確認です。中央処理装置余力と応答時間の両方を見ますので、目的名は並列度目的です。並列度で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は並列度説明です。誤答A並列度はSQLエラー時の成果物作成の選択で、主題は並列度です。除外A並列度ではSQLエラー時の成果物作成を外す理由も並列度誤答です。Bが正解です。論点並列度の指定名 DEGREE が該当します。目的並列度で読むパッケージカタログの根拠名は並列度根拠です。誤答C並列度はパッケージコピーの保持の選択で、主題は並列度です。除外C並列度ではパッケージコピーの保持を外す理由も並列度誤答です。誤答D並列度はパッケージコピーの保持の選択で、主題は並列度です。除外D並列度ではパッケージコピーの保持を外す理由も並列度誤答です。初出語並列度として、指定名 DEGREE はDb2の指定または確認表であり焦点は並列度定義です。位置付け並列度は並列実行の許可位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEGREE</strong></p><p>検証目的: 終端判定のDb2について、DEGREE は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020085の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDEGREEを指定し、OSKB020085の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DEGREE
CASE OSKB020085
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DEGREE
CASE OSKB020085
SOURCE Db2 for z/OS
DEGREEとOSKB020085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020085を同じ出力で読み、終端判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020085
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020085
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020085
DSNV401IとOSKB020085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DEGREE と OSKB020085 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0005"><h3>DYNAMICRULES</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>DYNAMICRULESは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 動的文規則を導入設計で確認します。Db2の作業記録に動的エスキューエルの権限文脈の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. PLAN_TABLE</li><li>C. APREUSE</li><li>D. DYNAMICRULES <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文規則はDです。論点動的文規則における指定名 DYNAMICRULES の確認軸名は動的文規則確認です。アプリケーションの実行権限設計と照合しますので、目的名は動的文規則目的です。動的文規則で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文規則説明です。誤答A動的文規則は成果物の所有者の選択で、主題は動的文規則です。除外A動的文規則では成果物の所有者を外す理由も動的文規則誤答です。誤答B動的文規則はEXPLAIN基本表の選択で、主題は動的文規則です。除外B動的文規則ではEXPLAIN基本表を外す理由も動的文規則誤答です。誤答C動的文規則は前回アクセスパスの再利用の選択で、主題は動的文規則です。除外C動的文規則では前回アクセスパスの再利用を外す理由も動的文規則誤答です。Dが正解です。論点動的文規則の指定名 DYNAMICRULES が該当します。目的動的文規則で読むパッケージカタログの根拠名は動的文規則根拠です。初出語動的文規則として、指定名 DYNAMICRULES はDb2の指定または確認表であり焦点は動的文規則定義です。位置付け動的文規則は動的エスキューエルの権限文脈位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 動的文規則を変更審査で確認します。Db2の作業記録に動的エスキューエルの権限文脈の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. DYNAMICRULES <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. ISOLATION</li><li>D. QUALIFIER</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文規則はAです。論点動的文規則における指定名 DYNAMICRULES の確認軸名は動的文規則確認です。アプリケーションの実行権限設計と照合しますので、目的名は動的文規則目的です。動的文規則で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文規則説明です。Aが正解です。論点動的文規則の指定名 DYNAMICRULES が該当します。目的動的文規則で読むパッケージカタログの根拠名は動的文規則根拠です。誤答B動的文規則は分離レベルの選択で、主題は動的文規則です。除外B動的文規則では分離レベルを外す理由も動的文規則誤答です。誤答C動的文規則は分離レベルの選択で、主題は動的文規則です。除外C動的文規則では分離レベルを外す理由も動的文規則誤答です。誤答D動的文規則は未修飾表名のスキーマの選択で、主題は動的文規則です。除外D動的文規則では未修飾表名のスキーマを外す理由も動的文規則誤答です。初出語動的文規則として、指定名 DYNAMICRULES はDb2の指定または確認表であり焦点は動的文規則定義です。位置付け動的文規則は動的エスキューエルの権限文脈位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 動的文規則を性能調査で確認します。Db2の作業記録に動的エスキューエルの権限文脈の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. SQLERROR</li><li>B. DYNAMICRULES <span class="kb-ok">✅ 正解</span></li><li>C. PLANMGMT</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文規則はBです。論点動的文規則における指定名 DYNAMICRULES の確認軸名は動的文規則確認です。アプリケーションの実行権限設計と照合しますので、目的名は動的文規則目的です。動的文規則で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文規則説明です。誤答A動的文規則はSQLエラー時の成果物作成の選択で、主題は動的文規則です。除外A動的文規則ではSQLエラー時の成果物作成を外す理由も動的文規則誤答です。Bが正解です。論点動的文規則の指定名 DYNAMICRULES が該当します。目的動的文規則で読むパッケージカタログの根拠名は動的文規則根拠です。誤答C動的文規則はパッケージコピーの保持の選択で、主題は動的文規則です。除外C動的文規則ではパッケージコピーの保持を外す理由も動的文規則誤答です。誤答D動的文規則はパッケージコピーの保持の選択で、主題は動的文規則です。除外D動的文規則ではパッケージコピーの保持を外す理由も動的文規則誤答です。初出語動的文規則として、指定名 DYNAMICRULES はDb2の指定または確認表であり焦点は動的文規則定義です。位置付け動的文規則は動的エスキューエルの権限文脈位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 動的文規則を障害復旧で確認します。Db2の作業記録に動的エスキューエルの権限文脈の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. OPTHINT</li><li>C. DYNAMICRULES <span class="kb-ok">✅ 正解</span></li><li>D. PATH</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文規則はCです。論点動的文規則における指定名 DYNAMICRULES の確認軸名は動的文規則確認です。アプリケーションの実行権限設計と照合しますので、目的名は動的文規則目的です。動的文規則で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文規則説明です。誤答A動的文規則はアクセスパス情報の出力の選択で、主題は動的文規則です。除外A動的文規則ではアクセスパス情報の出力を外す理由も動的文規則誤答です。誤答B動的文規則は最適化ヒントの利用の選択で、主題は動的文規則です。除外B動的文規則では最適化ヒントの利用を外す理由も動的文規則誤答です。Cが正解です。論点動的文規則の指定名 DYNAMICRULES が該当します。目的動的文規則で読むパッケージカタログの根拠名は動的文規則根拠です。誤答D動的文規則はルーチン探索順序の選択で、主題は動的文規則です。除外D動的文規則ではルーチン探索順序を外す理由も動的文規則誤答です。初出語動的文規則として、指定名 DYNAMICRULES はDb2の指定または確認表であり焦点は動的文規則定義です。位置付け動的文規則は動的エスキューエルの権限文脈位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0006"><h3>ENCODING</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>ENCODINGは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（5問）</summary><div class="kb-q"><p><strong>問題.</strong> 符号化方式を導入設計で確認します。Db2の作業記録に文字データの符号化の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. CURRENTDATA</li><li>B. EXPLAIN</li><li>C. DYNAMICRULES</li><li>D. ENCODING <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答符号化方式はDです。論点符号化方式における指定名 ENCODING の確認軸名は符号化方式確認です。文字化けや比較規則への影響を確認しますので、目的名は符号化方式目的です。符号化方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は符号化方式説明です。誤答A符号化方式はカーソル読み取りの現在性の選択で、主題は符号化方式です。除外A符号化方式ではカーソル読み取りの現在性を外す理由も符号化方式誤答です。誤答B符号化方式はアクセスパス情報の出力の選択で、主題は符号化方式です。除外B符号化方式ではアクセスパス情報の出力を外す理由も符号化方式誤答です。誤答C符号化方式は動的SQLの権限文脈の選択で、主題は符号化方式です。除外C符号化方式では動的SQLの権限文脈を外す理由も符号化方式誤答です。Dが正解です。論点符号化方式の指定名 ENCODING が該当します。目的符号化方式で読むパッケージカタログの根拠名は符号化方式根拠です。初出語符号化方式として、指定名 ENCODING はDb2の指定または確認表であり焦点は符号化方式定義です。位置付け符号化方式は文字データの符号化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 符号化方式を変更審査で確認します。Db2の作業記録に文字データの符号化の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. ENCODING <span class="kb-ok">✅ 正解</span></li><li>B. QUERYACCELERATION</li><li>C. QUERYACCELERATION</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答符号化方式はAです。論点符号化方式における指定名 ENCODING の確認軸名は符号化方式確認です。文字化けや比較規則への影響を確認しますので、目的名は符号化方式目的です。符号化方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は符号化方式説明です。Aが正解です。論点符号化方式の指定名 ENCODING が該当します。目的符号化方式で読むパッケージカタログの根拠名は符号化方式根拠です。誤答B符号化方式はアクセラレーター利用方針の選択で、主題は符号化方式です。除外B符号化方式ではアクセラレーター利用方針を外す理由も符号化方式誤答です。誤答C符号化方式はアクセラレーター利用方針の選択で、主題は符号化方式です。除外C符号化方式ではアクセラレーター利用方針を外す理由も符号化方式誤答です。誤答D符号化方式は準備済み動的SQL文の保持の選択で、主題は符号化方式です。除外D符号化方式では準備済み動的SQL文の保持を外す理由も符号化方式誤答です。初出語符号化方式として、指定名 ENCODING はDb2の指定または確認表であり焦点は符号化方式定義です。位置付け符号化方式は文字データの符号化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 符号化方式を性能調査で確認します。Db2の作業記録に文字データの符号化の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. ENCODING <span class="kb-ok">✅ 正解</span></li><li>C. EXPLAIN(ONLY)</li><li>D. EXPLAIN(ONLY)</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答符号化方式はBです。論点符号化方式における指定名 ENCODING の確認軸名は符号化方式確認です。文字化けや比較規則への影響を確認しますので、目的名は符号化方式目的です。符号化方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は符号化方式説明です。誤答A符号化方式は前回アクセスパスの再利用の選択で、主題は符号化方式です。除外A符号化方式では前回アクセスパスの再利用を外す理由も符号化方式誤答です。Bが正解です。論点符号化方式の指定名 ENCODING が該当します。目的符号化方式で読むパッケージカタログの根拠名は符号化方式根拠です。誤答C符号化方式は候補アクセスパスの事前出力の選択で、主題は符号化方式です。除外C符号化方式では候補アクセスパスの事前出力を外す理由も符号化方式誤答です。誤答D符号化方式は候補アクセスパスの事前出力の選択で、主題は符号化方式です。除外D符号化方式では候補アクセスパスの事前出力を外す理由も符号化方式誤答です。初出語符号化方式として、指定名 ENCODING はDb2の指定または確認表であり焦点は符号化方式定義です。位置付け符号化方式は文字データの符号化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 符号化方式を障害復旧で確認します。Db2の作業記録に文字データの符号化の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. QUALIFIER</li><li>C. ENCODING <span class="kb-ok">✅ 正解</span></li><li>D. ISOLATION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答符号化方式はCです。論点符号化方式における指定名 ENCODING の確認軸名は符号化方式確認です。文字化けや比較規則への影響を確認しますので、目的名は符号化方式目的です。符号化方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は符号化方式説明です。誤答A符号化方式は前回コピーへの切り替えの選択で、主題は符号化方式です。除外A符号化方式では前回コピーへの切り替えを外す理由も符号化方式誤答です。誤答B符号化方式は未修飾表名のスキーマの選択で、主題は符号化方式です。除外B符号化方式では未修飾表名のスキーマを外す理由も符号化方式誤答です。Cが正解です。論点符号化方式の指定名 ENCODING が該当します。目的符号化方式で読むパッケージカタログの根拠名は符号化方式根拠です。誤答D符号化方式は分離レベルの選択で、主題は符号化方式です。除外D符号化方式では分離レベルを外す理由も符号化方式誤答です。初出語符号化方式として、指定名 ENCODING はDb2の指定または確認表であり焦点は符号化方式定義です。位置付け符号化方式は文字データの符号化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 外部クライアントとの連携で文字化けを避けるため、パッケージが扱う文字データの符号化方式を確認します。使うオプションはどれですか。</p><ul class="kb-choices"><li>A. ENCODING <span class="kb-ok">✅ 正解</span></li><li>B. ACTION</li><li>C. PLANMGMT</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 文字コードの扱いなら A が正解で、符号化方式は ENCODING で指定します。外部クライアントとの接続方式と整合させる必要があります。B: 追加か置換かの動作です。C: 旧パッケージコピーの保持です。D: 並列実行可否です；背景にはアプリケーションが扱う文字データの符号化方式は、ENCODING で指定します、Java や ODBC など外部クライアントと連携する場合、Db2 側とクライアント側の文字コード差が文字化けの原因になります、表定義とドライバー設定も国際化対応の確認対象ですという関係があり、この区別で確認する名称は「ENCODING」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ENCODING</strong></p><p>検証目的: 上書判定のDb2について、ENCODING は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わりに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020087の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にENCODINGを指定し、OSKB020087の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ENCODING
CASE OSKB020087
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ENCODING
CASE OSKB020087
SOURCE Db2 for z/OS
ENCODINGとOSKB020087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020087を同じ出力で読み、上書判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020087
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020087
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020087
DSNV401IとOSKB020087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ENCODING と OSKB020087 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0007"><h3>EXPLAIN</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>EXPLAINは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></section>


<section class="kb-item" id="c07-i0008"><h3>IMMEDWRITE</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>IMMEDWRITEは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Data Sharing で共有バッファプール依存ページを更新する処理について、変更ページの即時書き込みを制御したい状況です。使うオプションはどれですか。</p><ul class="kb-choices"><li>A. QUALIFIER</li><li>B. IMMEDWRITE <span class="kb-ok">✅ 正解</span></li><li>C. EXPLAIN</li><li>D. OWNER</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 共有バッファ関連の書き込みなら B が該当し、即時書き込みの制御は IMMEDWRITE で扱います。Data Sharing 構成のページ整合性と運用に関係します。A: 未修飾名のスキーマです。C: アクセスパス情報の出力です。D: 所有者の指定です；背景にはData Sharing の共有バッファプールに依存するページを即時書き込みするかは、IMMEDWRITE に関わります、対象は通常の単独 Db2 性能指定ではなく、グループバッファプール依存のページセットやパーティションです、可用性や整合性の設計と合わせて判断しますという関係があり、この区別で確認する名称は「IMMEDWRITE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMMEDWRITE</strong></p><p>検証目的: 区切判定のDb2について、IMMEDWRITE は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にIMMEDWRITEを指定し、OSKB020090の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND IMMEDWRITE
CASE OSKB020090
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM IMMEDWRITE
CASE OSKB020090
SOURCE Db2 for z/OS
IMMEDWRITEとOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020090を同じ出力で読み、区切判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020090
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020090
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020090
DSNV401IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の IMMEDWRITE と OSKB020090 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0009"><h3>ISOLATION</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>ISOLATIONは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 分離方式を導入設計で確認します。Db2の作業記録に分離レベルの根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. ISOLATION <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. APPLCOMPAT</li><li>D. SWITCH(PREVIOUS)</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答分離方式はAです。論点分離方式における指定名 ISOLATION の確認軸名は分離方式確認です。並行更新の待ちや読み取り精度を確認しますので、目的名は分離方式目的です。分離方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は分離方式説明です。Aが正解です。論点分離方式の指定名 ISOLATION が該当します。目的分離方式で読むパッケージカタログの根拠名は分離方式根拠です。誤答B分離方式はルーチン探索順序の選択で、主題は分離方式です。除外B分離方式ではルーチン探索順序を外す理由も分離方式誤答です。誤答C分離方式は互換性レベルの選択で、主題は分離方式です。除外C分離方式では互換性レベルを外す理由も分離方式誤答です。誤答D分離方式は前回コピーへの切り替えの選択で、主題は分離方式です。除外D分離方式では前回コピーへの切り替えを外す理由も分離方式誤答です。初出語分離方式として、指定名 ISOLATION はDb2の指定または確認表であり焦点は分離方式定義です。位置付け分離方式は分離レベル位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 分離方式を変更審査で確認します。Db2の作業記録に分離レベルの根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. ISOLATION <span class="kb-ok">✅ 正解</span></li><li>C. KEEPDYNAMIC</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答分離方式はBです。論点分離方式における指定名 ISOLATION の確認軸名は分離方式確認です。並行更新の待ちや読み取り精度を確認しますので、目的名は分離方式目的です。分離方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は分離方式説明です。誤答A分離方式は前回アクセスパスの再利用の選択で、主題は分離方式です。除外A分離方式では前回アクセスパスの再利用を外す理由も分離方式誤答です。Bが正解です。論点分離方式の指定名 ISOLATION が該当します。目的分離方式で読むパッケージカタログの根拠名は分離方式根拠です。誤答C分離方式は準備済み動的SQL文の保持の選択で、主題は分離方式です。除外C分離方式では準備済み動的SQL文の保持を外す理由も分離方式誤答です。誤答D分離方式は並列実行の許可の選択で、主題は分離方式です。除外D分離方式では並列実行の許可を外す理由も分離方式誤答です。初出語分離方式として、指定名 ISOLATION はDb2の指定または確認表であり焦点は分離方式定義です。位置付け分離方式は分離レベル位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 分離方式を性能調査で確認します。Db2の作業記録に分離レベルの根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. ENCODING</li><li>C. ISOLATION <span class="kb-ok">✅ 正解</span></li><li>D. CURRENTDATA</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答分離方式はCです。論点分離方式における指定名 ISOLATION の確認軸名は分離方式確認です。並行更新の待ちや読み取り精度を確認しますので、目的名は分離方式目的です。分離方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は分離方式説明です。誤答A分離方式は前回コピーへの切り替えの選択で、主題は分離方式です。除外A分離方式では前回コピーへの切り替えを外す理由も分離方式誤答です。誤答B分離方式は文字データの符号化の選択で、主題は分離方式です。除外B分離方式では文字データの符号化を外す理由も分離方式誤答です。Cが正解です。論点分離方式の指定名 ISOLATION が該当します。目的分離方式で読むパッケージカタログの根拠名は分離方式根拠です。誤答D分離方式はカーソル読み取りの現在性の選択で、主題は分離方式です。除外D分離方式ではカーソル読み取りの現在性を外す理由も分離方式誤答です。初出語分離方式として、指定名 ISOLATION はDb2の指定または確認表であり焦点は分離方式定義です。位置付け分離方式は分離レベル位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 分離方式を障害復旧で確認します。Db2の作業記録に分離レベルの根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. PLAN_TABLE</li><li>C. APREUSE</li><li>D. ISOLATION <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答分離方式はDです。論点分離方式における指定名 ISOLATION の確認軸名は分離方式確認です。並行更新の待ちや読み取り精度を確認しますので、目的名は分離方式目的です。分離方式で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は分離方式説明です。誤答A分離方式は成果物の所有者の選択で、主題は分離方式です。除外A分離方式では成果物の所有者を外す理由も分離方式誤答です。誤答B分離方式はEXPLAIN基本表の選択で、主題は分離方式です。除外B分離方式ではEXPLAIN基本表を外す理由も分離方式誤答です。誤答C分離方式は前回アクセスパスの再利用の選択で、主題は分離方式です。除外C分離方式では前回アクセスパスの再利用を外す理由も分離方式誤答です。Dが正解です。論点分離方式の指定名 ISOLATION が該当します。目的分離方式で読むパッケージカタログの根拠名は分離方式根拠です。初出語分離方式として、指定名 ISOLATION はDb2の指定または確認表であり焦点は分離方式定義です。位置付け分離方式は分離レベル位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISOLATION</strong></p><p>検証目的: 構文判定のDb2について、ISOLATION は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020081の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にISOLATIONを指定し、OSKB020081の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ISOLATION
CASE OSKB020081
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ISOLATION
CASE OSKB020081
SOURCE Db2 for z/OS
ISOLATIONとOSKB020081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020081を同じ出力で読み、構文判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020081
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020081
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020081
DSNV401IとOSKB020081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ISOLATION と OSKB020081 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0010"><h3>KEEPDYNAMIC</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>KEEPDYNAMICは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 動的文保持を導入設計で確認します。Db2の作業記録に動的エスキューエル文の保持の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. PLANMGMT</li><li>C. KEEPDYNAMIC <span class="kb-ok">✅ 正解</span></li><li>D. APCOMPARE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文保持はCです。論点動的文保持における指定名 KEEPDYNAMIC の確認軸名は動的文保持確認です。再準備コストと資源保持を比較しますので、目的名は動的文保持目的です。動的文保持で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文保持説明です。誤答A動的文保持は前回コピーへの切り替えの選択で、主題は動的文保持です。除外A動的文保持では前回コピーへの切り替えを外す理由も動的文保持誤答です。誤答B動的文保持はパッケージコピーの保持の選択で、主題は動的文保持です。除外B動的文保持ではパッケージコピーの保持を外す理由も動的文保持誤答です。Cが正解です。論点動的文保持の指定名 KEEPDYNAMIC が該当します。目的動的文保持で読むパッケージカタログの根拠名は動的文保持根拠です。誤答D動的文保持はアクセスパス差分の比較の選択で、主題は動的文保持です。除外D動的文保持ではアクセスパス差分の比較を外す理由も動的文保持誤答です。初出語動的文保持として、指定名 KEEPDYNAMIC はDb2の指定または確認表であり焦点は動的文保持定義です。位置付け動的文保持は動的エスキューエル文の保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 動的文保持を変更審査で確認します。Db2の作業記録に動的エスキューエル文の保持の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. QUERYACCELERATION</li><li>C. VALIDATE</li><li>D. KEEPDYNAMIC <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文保持はDです。論点動的文保持における指定名 KEEPDYNAMIC の確認軸名は動的文保持確認です。再準備コストと資源保持を比較しますので、目的名は動的文保持目的です。動的文保持で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文保持説明です。誤答A動的文保持は成果物の所有者の選択で、主題は動的文保持です。除外A動的文保持では成果物の所有者を外す理由も動的文保持誤答です。誤答B動的文保持はアクセラレーター利用方針の選択で、主題は動的文保持です。除外B動的文保持ではアクセラレーター利用方針を外す理由も動的文保持誤答です。誤答C動的文保持は検査時期の選択で、主題は動的文保持です。除外C動的文保持では検査時期を外す理由も動的文保持誤答です。Dが正解です。論点動的文保持の指定名 KEEPDYNAMIC が該当します。目的動的文保持で読むパッケージカタログの根拠名は動的文保持根拠です。初出語動的文保持として、指定名 KEEPDYNAMIC はDb2の指定または確認表であり焦点は動的文保持定義です。位置付け動的文保持は動的エスキューエル文の保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 動的文保持を性能調査で確認します。Db2の作業記録に動的エスキューエル文の保持の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. APCOMPARE</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文保持はAです。論点動的文保持における指定名 KEEPDYNAMIC の確認軸名は動的文保持確認です。再準備コストと資源保持を比較しますので、目的名は動的文保持目的です。動的文保持で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文保持説明です。Aが正解です。論点動的文保持の指定名 KEEPDYNAMIC が該当します。目的動的文保持で読むパッケージカタログの根拠名は動的文保持根拠です。誤答B動的文保持は分離レベルの選択で、主題は動的文保持です。除外B動的文保持では分離レベルを外す理由も動的文保持誤答です。誤答C動的文保持はアクセスパス差分の比較の選択で、主題は動的文保持です。除外C動的文保持ではアクセスパス差分の比較を外す理由も動的文保持誤答です。誤答D動的文保持はパッケージコピーの保持の選択で、主題は動的文保持です。除外D動的文保持ではパッケージコピーの保持を外す理由も動的文保持誤答です。初出語動的文保持として、指定名 KEEPDYNAMIC はDb2の指定または確認表であり焦点は動的文保持定義です。位置付け動的文保持は動的エスキューエル文の保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 動的文保持を障害復旧で確認します。Db2の作業記録に動的エスキューエル文の保持の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. KEEPDYNAMIC <span class="kb-ok">✅ 正解</span></li><li>C. OWNER</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答動的文保持はBです。論点動的文保持における指定名 KEEPDYNAMIC の確認軸名は動的文保持確認です。再準備コストと資源保持を比較しますので、目的名は動的文保持目的です。動的文保持で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は動的文保持説明です。誤答A動的文保持は動的SQLの権限文脈の選択で、主題は動的文保持です。除外A動的文保持では動的SQLの権限文脈を外す理由も動的文保持誤答です。Bが正解です。論点動的文保持の指定名 KEEPDYNAMIC が該当します。目的動的文保持で読むパッケージカタログの根拠名は動的文保持根拠です。誤答C動的文保持は成果物の所有者の選択で、主題は動的文保持です。除外C動的文保持では成果物の所有者を外す理由も動的文保持誤答です。誤答D動的文保持は動的SQL文の集約の選択で、主題は動的文保持です。除外D動的文保持では動的SQL文の集約を外す理由も動的文保持誤答です。初出語動的文保持として、指定名 KEEPDYNAMIC はDb2の指定または確認表であり焦点は動的文保持定義です。位置付け動的文保持は動的エスキューエル文の保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>KEEPDYNAMIC</strong></p><p>検証目的: 出力判定のDb2について、KEEPDYNAMIC は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いがに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にKEEPDYNAMICを指定し、OSKB020088の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND KEEPDYNAMIC
CASE OSKB020088
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM KEEPDYNAMIC
CASE OSKB020088
SOURCE Db2 for z/OS
KEEPDYNAMICとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020088を同じ出力で読み、出力判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020088
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020088
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020088
DSNV401IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の KEEPDYNAMIC と OSKB020088 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0011"><h3>OWNER</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>OWNERは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 所有者責任を導入設計で確認します。Db2の作業記録に成果物の所有者の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. SQLERROR</li><li>B. OWNER <span class="kb-ok">✅ 正解</span></li><li>C. CONCENTRATESTMT</li><li>D. QUALIFIER</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答所有者責任はBです。論点所有者責任における指定名 OWNER の確認軸名は所有者責任確認です。実行者識別子と所有者識別子を分けて監査しますので、目的名は所有者責任目的です。所有者責任で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は所有者責任説明です。誤答A所有者責任はSQLエラー時の成果物作成の選択で、主題は所有者責任です。除外A所有者責任ではSQLエラー時の成果物作成を外す理由も所有者責任誤答です。Bが正解です。論点所有者責任の指定名 OWNER が該当します。目的所有者責任で読むパッケージカタログの根拠名は所有者責任根拠です。誤答C所有者責任は動的SQL文の集約の選択で、主題は所有者責任です。除外C所有者責任では動的SQL文の集約を外す理由も所有者責任誤答です。誤答D所有者責任は未修飾表名のスキーマの選択で、主題は所有者責任です。除外D所有者責任では未修飾表名のスキーマを外す理由も所有者責任誤答です。初出語所有者責任として、指定名 OWNER はDb2の指定または確認表であり焦点は所有者責任定義です。位置付け所有者責任は成果物の所有者位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 所有者責任を変更審査で確認します。Db2の作業記録に成果物の所有者の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. SWITCH(PREVIOUS)</li><li>C. OWNER <span class="kb-ok">✅ 正解</span></li><li>D. APPLCOMPAT</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答所有者責任はCです。論点所有者責任における指定名 OWNER の確認軸名は所有者責任確認です。実行者識別子と所有者識別子を分けて監査しますので、目的名は所有者責任目的です。所有者責任で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は所有者責任説明です。誤答A所有者責任はアクセスパス情報の出力の選択で、主題は所有者責任です。除外A所有者責任ではアクセスパス情報の出力を外す理由も所有者責任誤答です。誤答B所有者責任は前回コピーへの切り替えの選択で、主題は所有者責任です。除外B所有者責任では前回コピーへの切り替えを外す理由も所有者責任誤答です。Cが正解です。論点所有者責任の指定名 OWNER が該当します。目的所有者責任で読むパッケージカタログの根拠名は所有者責任根拠です。誤答D所有者責任は互換性レベルの選択で、主題は所有者責任です。除外D所有者責任では互換性レベルを外す理由も所有者責任誤答です。初出語所有者責任として、指定名 OWNER はDb2の指定または確認表であり焦点は所有者責任定義です。位置付け所有者責任は成果物の所有者位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 所有者責任を性能調査で確認します。Db2の作業記録に成果物の所有者の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. ISOLATION</li><li>C. QUERYACCELERATION</li><li>D. OWNER <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答所有者責任はDです。論点所有者責任における指定名 OWNER の確認軸名は所有者責任確認です。実行者識別子と所有者識別子を分けて監査しますので、目的名は所有者責任目的です。所有者責任で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は所有者責任説明です。誤答A所有者責任は準備済み動的SQL文の保持の選択で、主題は所有者責任です。除外A所有者責任では準備済み動的SQL文の保持を外す理由も所有者責任誤答です。誤答B所有者責任は分離レベルの選択で、主題は所有者責任です。除外B所有者責任では分離レベルを外す理由も所有者責任誤答です。誤答C所有者責任はアクセラレーター利用方針の選択で、主題は所有者責任です。除外C所有者責任ではアクセラレーター利用方針を外す理由も所有者責任誤答です。Dが正解です。論点所有者責任の指定名 OWNER が該当します。目的所有者責任で読むパッケージカタログの根拠名は所有者責任根拠です。初出語所有者責任として、指定名 OWNER はDb2の指定または確認表であり焦点は所有者責任定義です。位置付け所有者責任は成果物の所有者位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 所有者責任を障害復旧で確認します。Db2の作業記録に成果物の所有者の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. OWNER <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. APPLCOMPAT</li><li>D. SWITCH(PREVIOUS)</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答所有者責任はAです。論点所有者責任における指定名 OWNER の確認軸名は所有者責任確認です。実行者識別子と所有者識別子を分けて監査しますので、目的名は所有者責任目的です。所有者責任で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は所有者責任説明です。Aが正解です。論点所有者責任の指定名 OWNER が該当します。目的所有者責任で読むパッケージカタログの根拠名は所有者責任根拠です。誤答B所有者責任はルーチン探索順序の選択で、主題は所有者責任です。除外B所有者責任ではルーチン探索順序を外す理由も所有者責任誤答です。誤答C所有者責任は互換性レベルの選択で、主題は所有者責任です。除外C所有者責任では互換性レベルを外す理由も所有者責任誤答です。誤答D所有者責任は前回コピーへの切り替えの選択で、主題は所有者責任です。除外D所有者責任では前回コピーへの切り替えを外す理由も所有者責任誤答です。初出語所有者責任として、指定名 OWNER はDb2の指定または確認表であり焦点は所有者責任定義です。位置付け所有者責任は成果物の所有者位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>OWNER</strong></p><p>検証目的: 監査検査のDb2について、OWNER は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わります。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020079の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、監査検査のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にOWNERを指定し、OSKB020079の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND OWNER
CASE OSKB020079
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM OWNER
CASE OSKB020079
SOURCE Db2 for z/OS
OWNERとOSKB020079が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020079を同じ出力で読み、監査検査のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020079
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020079
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020079
DSNV401IとOSKB020079が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の OWNER と OSKB020079 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020079 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0012"><h3>PATH</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>PATHは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（5問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索順序を導入設計で確認します。Db2の作業記録にルーチン探索順序の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. PATH <span class="kb-ok">✅ 正解</span></li><li>C. OWNER</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答探索順序はBです。論点探索順序における指定名 PATH の確認軸名は探索順序確認です。関数やプロシージャの解決先を固定しますので、目的名は探索順序目的です。探索順序で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は探索順序説明です。誤答A探索順序は動的SQLの権限文脈の選択で、主題は探索順序です。除外A探索順序では動的SQLの権限文脈を外す理由も探索順序誤答です。Bが正解です。論点探索順序の指定名 PATH が該当します。目的探索順序で読むパッケージカタログの根拠名は探索順序根拠です。誤答C探索順序は成果物の所有者の選択で、主題は探索順序です。除外C探索順序では成果物の所有者を外す理由も探索順序誤答です。誤答D探索順序は動的SQL文の集約の選択で、主題は探索順序です。除外D探索順序では動的SQL文の集約を外す理由も探索順序誤答です。初出語探索順序として、指定名 PATH はDb2の指定または確認表であり焦点は探索順序定義です。位置付け探索順序はルーチン探索順序位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 探索順序を変更審査で確認します。Db2の作業記録にルーチン探索順序の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. DEGREE</li><li>C. PATH <span class="kb-ok">✅ 正解</span></li><li>D. ACTION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答探索順序はCです。論点探索順序における指定名 PATH の確認軸名は探索順序確認です。関数やプロシージャの解決先を固定しますので、目的名は探索順序目的です。探索順序で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は探索順序説明です。誤答A探索順序はパッケージコピーの保持の選択で、主題は探索順序です。除外A探索順序ではパッケージコピーの保持を外す理由も探索順序誤答です。誤答B探索順序は並列実行の許可の選択で、主題は探索順序です。除外B探索順序では並列実行の許可を外す理由も探索順序誤答です。Cが正解です。論点探索順序の指定名 PATH が該当します。目的探索順序で読むパッケージカタログの根拠名は探索順序根拠です。誤答D探索順序は追加と置換の扱いの選択で、主題は探索順序です。除外D探索順序では追加と置換の扱いを外す理由も探索順序誤答です。初出語探索順序として、指定名 PATH はDb2の指定または確認表であり焦点は探索順序定義です。位置付け探索順序はルーチン探索順序位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 探索順序を性能調査で確認します。Db2の作業記録にルーチン探索順序の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. CURRENTDATA</li><li>B. EXPLAIN</li><li>C. DYNAMICRULES</li><li>D. PATH <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答探索順序はDです。論点探索順序における指定名 PATH の確認軸名は探索順序確認です。関数やプロシージャの解決先を固定しますので、目的名は探索順序目的です。探索順序で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は探索順序説明です。誤答A探索順序はカーソル読み取りの現在性の選択で、主題は探索順序です。除外A探索順序ではカーソル読み取りの現在性を外す理由も探索順序誤答です。誤答B探索順序はアクセスパス情報の出力の選択で、主題は探索順序です。除外B探索順序ではアクセスパス情報の出力を外す理由も探索順序誤答です。誤答C探索順序は動的SQLの権限文脈の選択で、主題は探索順序です。除外C探索順序では動的SQLの権限文脈を外す理由も探索順序誤答です。Dが正解です。論点探索順序の指定名 PATH が該当します。目的探索順序で読むパッケージカタログの根拠名は探索順序根拠です。初出語探索順序として、指定名 PATH はDb2の指定または確認表であり焦点は探索順序定義です。位置付け探索順序はルーチン探索順序位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 探索順序を障害復旧で確認します。Db2の作業記録にルーチン探索順序の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. PATH <span class="kb-ok">✅ 正解</span></li><li>B. QUERYACCELERATION</li><li>C. QUERYACCELERATION</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答探索順序はAです。論点探索順序における指定名 PATH の確認軸名は探索順序確認です。関数やプロシージャの解決先を固定しますので、目的名は探索順序目的です。探索順序で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は探索順序説明です。Aが正解です。論点探索順序の指定名 PATH が該当します。目的探索順序で読むパッケージカタログの根拠名は探索順序根拠です。誤答B探索順序はアクセラレーター利用方針の選択で、主題は探索順序です。除外B探索順序ではアクセラレーター利用方針を外す理由も探索順序誤答です。誤答C探索順序はアクセラレーター利用方針の選択で、主題は探索順序です。除外C探索順序ではアクセラレーター利用方針を外す理由も探索順序誤答です。誤答D探索順序は準備済み動的SQL文の保持の選択で、主題は探索順序です。除外D探索順序では準備済み動的SQL文の保持を外す理由も探索順序誤答です。初出語探索順序として、指定名 PATH はDb2の指定または確認表であり焦点は探索順序定義です。位置付け探索順序はルーチン探索順序位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 同名のユーザー定義関数が複数スキーマにあり、静的 SQL からどの順序で名前解決するかを固定したい状況です。対象のオプションはどれですか。</p><ul class="kb-choices"><li>A. PATH <span class="kb-ok">✅ 正解</span></li><li>B. DEGREE</li><li>C. VALIDATE</li><li>D. ACTION</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 名前探索順序の指定なので A を選択し、未修飾名を解決する順序は PATH で決めます。同名ルーチンがある環境で誤呼び出しを防ぎます。B: 並列実行可否です。C: BIND 時と実行時の検査扱いです。D: 追加または置換の動作です；背景には名前探索順を決める BIND/REBIND の PATH は、未修飾のルーチン名やデータタイプ名をどの順序で解決するかを指定します、同名オブジェクトが複数スキーマにある環境では、探索順が変わるを主な根拠にして別のルーチンを呼ぶ危険があります、移行時には、呼び出し先とスキーマ順序を一緒に残しますという関係があり、この区別で確認する名称は「PATH」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PATH</strong></p><p>検証目的: 条件判定のDb2について、PATH は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わります。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020089の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にPATHを指定し、OSKB020089の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND PATH
CASE OSKB020089
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM PATH
CASE OSKB020089
SOURCE Db2 for z/OS
PATHとOSKB020089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020089を同じ出力で読み、条件判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020089
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020089
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020089
DSNV401IとOSKB020089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の PATH と OSKB020089 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0013"><h3>PLANMGMT</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 上級</p><p>PLANMGMTは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> パッケージ保全を導入設計で確認します。Db2の作業記録に旧アクセスパスの保持の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. OPTHINT</li><li>C. PLANMGMT <span class="kb-ok">✅ 正解</span></li><li>D. PATH</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答パッケージ保全はCです。論点パッケージ保全における指定名 PLANMGMT の確認軸名はパッケージ保全確認です。切り戻し可能性を作業前に確保しますので、目的名はパッケージ保全目的です。パッケージ保全で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はパッケージ保全説明です。誤答Aパッケージ保全はアクセスパス情報の出力の選択で、主題はパッケージ保全です。除外Aパッケージ保全ではアクセスパス情報の出力を外す理由もパッケージ保全誤答です。誤答Bパッケージ保全は最適化ヒントの利用の選択で、主題はパッケージ保全です。除外Bパッケージ保全では最適化ヒントの利用を外す理由もパッケージ保全誤答です。Cが正解です。論点パッケージ保全の指定名 PLANMGMT が該当します。目的パッケージ保全で読むパッケージカタログの根拠名はパッケージ保全根拠です。誤答Dパッケージ保全はルーチン探索順序の選択で、主題はパッケージ保全です。除外Dパッケージ保全ではルーチン探索順序を外す理由もパッケージ保全誤答です。初出語パッケージ保全として、指定名 PLANMGMT はDb2の指定または確認表であり焦点はパッケージ保全定義です。位置付けパッケージ保全は旧アクセスパスの保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> パッケージ保全を変更審査で確認します。Db2の作業記録に旧アクセスパスの保持の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. APREUSE</li><li>C. PLAN_TABLE</li><li>D. PLANMGMT <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答パッケージ保全はDです。論点パッケージ保全における指定名 PLANMGMT の確認軸名はパッケージ保全確認です。切り戻し可能性を作業前に確保しますので、目的名はパッケージ保全目的です。パッケージ保全で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はパッケージ保全説明です。誤答Aパッケージ保全は準備済み動的SQL文の保持の選択で、主題はパッケージ保全です。除外Aパッケージ保全では準備済み動的SQL文の保持を外す理由もパッケージ保全誤答です。誤答Bパッケージ保全は前回アクセスパスの再利用の選択で、主題はパッケージ保全です。除外Bパッケージ保全では前回アクセスパスの再利用を外す理由もパッケージ保全誤答です。誤答Cパッケージ保全はEXPLAIN基本表の選択で、主題はパッケージ保全です。除外Cパッケージ保全ではEXPLAIN基本表を外す理由もパッケージ保全誤答です。Dが正解です。論点パッケージ保全の指定名 PLANMGMT が該当します。目的パッケージ保全で読むパッケージカタログの根拠名はパッケージ保全根拠です。初出語パッケージ保全として、指定名 PLANMGMT はDb2の指定または確認表であり焦点はパッケージ保全定義です。位置付けパッケージ保全は旧アクセスパスの保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> パッケージ保全を性能調査で確認します。Db2の作業記録に旧アクセスパスの保持の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. PLANMGMT <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. ACTION</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答パッケージ保全はAです。論点パッケージ保全における指定名 PLANMGMT の確認軸名はパッケージ保全確認です。切り戻し可能性を作業前に確保しますので、目的名はパッケージ保全目的です。パッケージ保全で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はパッケージ保全説明です。Aが正解です。論点パッケージ保全の指定名 PLANMGMT が該当します。目的パッケージ保全で読むパッケージカタログの根拠名はパッケージ保全根拠です。誤答Bパッケージ保全はルーチン探索順序の選択で、主題はパッケージ保全です。除外Bパッケージ保全ではルーチン探索順序を外す理由もパッケージ保全誤答です。誤答Cパッケージ保全は追加と置換の扱いの選択で、主題はパッケージ保全です。除外Cパッケージ保全では追加と置換の扱いを外す理由もパッケージ保全誤答です。誤答Dパッケージ保全は並列実行の許可の選択で、主題はパッケージ保全です。除外Dパッケージ保全では並列実行の許可を外す理由もパッケージ保全誤答です。初出語パッケージ保全として、指定名 PLANMGMT はDb2の指定または確認表であり焦点はパッケージ保全定義です。位置付けパッケージ保全は旧アクセスパスの保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> パッケージ保全を障害復旧で確認します。Db2の作業記録に旧アクセスパスの保持の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. PLANMGMT <span class="kb-ok">✅ 正解</span></li><li>C. RELEASE</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答パッケージ保全はBです。論点パッケージ保全における指定名 PLANMGMT の確認軸名はパッケージ保全確認です。切り戻し可能性を作業前に確保しますので、目的名はパッケージ保全目的です。パッケージ保全で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はパッケージ保全説明です。誤答Aパッケージ保全は前回アクセスパスの再利用の選択で、主題はパッケージ保全です。除外Aパッケージ保全では前回アクセスパスの再利用を外す理由もパッケージ保全誤答です。Bが正解です。論点パッケージ保全の指定名 PLANMGMT が該当します。目的パッケージ保全で読むパッケージカタログの根拠名はパッケージ保全根拠です。誤答Cパッケージ保全は資源解放の時点の選択で、主題はパッケージ保全です。除外Cパッケージ保全では資源解放の時点を外す理由もパッケージ保全誤答です。誤答Dパッケージ保全は準備済み動的SQL文の保持の選択で、主題はパッケージ保全です。除外Dパッケージ保全では準備済み動的SQL文の保持を外す理由もパッケージ保全誤答です。初出語パッケージ保全として、指定名 PLANMGMT はDb2の指定または確認表であり焦点はパッケージ保全定義です。位置付けパッケージ保全は旧アクセスパスの保持位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0014"><h3>QUALIFIER</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>QUALIFIERは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 修飾子解決を導入設計で確認します。Db2の作業記録に未修飾名の解決の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. SWITCH(PREVIOUS)</li><li>C. QUALIFIER <span class="kb-ok">✅ 正解</span></li><li>D. APPLCOMPAT</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答修飾子解決はCです。論点修飾子解決における指定名 QUALIFIER の確認軸名は修飾子解決確認です。移行先のスキーマ誤参照を防ぎますので、目的名は修飾子解決目的です。修飾子解決で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は修飾子解決説明です。誤答A修飾子解決はアクセスパス情報の出力の選択で、主題は修飾子解決です。除外A修飾子解決ではアクセスパス情報の出力を外す理由も修飾子解決誤答です。誤答B修飾子解決は前回コピーへの切り替えの選択で、主題は修飾子解決です。除外B修飾子解決では前回コピーへの切り替えを外す理由も修飾子解決誤答です。Cが正解です。論点修飾子解決の指定名 QUALIFIER が該当します。目的修飾子解決で読むパッケージカタログの根拠名は修飾子解決根拠です。誤答D修飾子解決は互換性レベルの選択で、主題は修飾子解決です。除外D修飾子解決では互換性レベルを外す理由も修飾子解決誤答です。初出語修飾子解決として、指定名 QUALIFIER はDb2の指定または確認表であり焦点は修飾子解決定義です。位置付け修飾子解決は未修飾名の解決位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 修飾子解決を変更審査で確認します。Db2の作業記録に未修飾名の解決の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. ISOLATION</li><li>C. QUERYACCELERATION</li><li>D. QUALIFIER <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答修飾子解決はDです。論点修飾子解決における指定名 QUALIFIER の確認軸名は修飾子解決確認です。移行先のスキーマ誤参照を防ぎますので、目的名は修飾子解決目的です。修飾子解決で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は修飾子解決説明です。誤答A修飾子解決は準備済み動的SQL文の保持の選択で、主題は修飾子解決です。除外A修飾子解決では準備済み動的SQL文の保持を外す理由も修飾子解決誤答です。誤答B修飾子解決は分離レベルの選択で、主題は修飾子解決です。除外B修飾子解決では分離レベルを外す理由も修飾子解決誤答です。誤答C修飾子解決はアクセラレーター利用方針の選択で、主題は修飾子解決です。除外C修飾子解決ではアクセラレーター利用方針を外す理由も修飾子解決誤答です。Dが正解です。論点修飾子解決の指定名 QUALIFIER が該当します。目的修飾子解決で読むパッケージカタログの根拠名は修飾子解決根拠です。初出語修飾子解決として、指定名 QUALIFIER はDb2の指定または確認表であり焦点は修飾子解決定義です。位置付け修飾子解決は未修飾名の解決位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 修飾子解決を性能調査で確認します。Db2の作業記録に未修飾名の解決の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. QUALIFIER <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. APPLCOMPAT</li><li>D. SWITCH(PREVIOUS)</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答修飾子解決はAです。論点修飾子解決における指定名 QUALIFIER の確認軸名は修飾子解決確認です。移行先のスキーマ誤参照を防ぎますので、目的名は修飾子解決目的です。修飾子解決で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は修飾子解決説明です。Aが正解です。論点修飾子解決の指定名 QUALIFIER が該当します。目的修飾子解決で読むパッケージカタログの根拠名は修飾子解決根拠です。誤答B修飾子解決はルーチン探索順序の選択で、主題は修飾子解決です。除外B修飾子解決ではルーチン探索順序を外す理由も修飾子解決誤答です。誤答C修飾子解決は互換性レベルの選択で、主題は修飾子解決です。除外C修飾子解決では互換性レベルを外す理由も修飾子解決誤答です。誤答D修飾子解決は前回コピーへの切り替えの選択で、主題は修飾子解決です。除外D修飾子解決では前回コピーへの切り替えを外す理由も修飾子解決誤答です。初出語修飾子解決として、指定名 QUALIFIER はDb2の指定または確認表であり焦点は修飾子解決定義です。位置付け修飾子解決は未修飾名の解決位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 修飾子解決を障害復旧で確認します。Db2の作業記録に未修飾名の解決の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. QUALIFIER <span class="kb-ok">✅ 正解</span></li><li>C. KEEPDYNAMIC</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答修飾子解決はBです。論点修飾子解決における指定名 QUALIFIER の確認軸名は修飾子解決確認です。移行先のスキーマ誤参照を防ぎますので、目的名は修飾子解決目的です。修飾子解決で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は修飾子解決説明です。誤答A修飾子解決は前回アクセスパスの再利用の選択で、主題は修飾子解決です。除外A修飾子解決では前回アクセスパスの再利用を外す理由も修飾子解決誤答です。Bが正解です。論点修飾子解決の指定名 QUALIFIER が該当します。目的修飾子解決で読むパッケージカタログの根拠名は修飾子解決根拠です。誤答C修飾子解決は準備済み動的SQL文の保持の選択で、主題は修飾子解決です。除外C修飾子解決では準備済み動的SQL文の保持を外す理由も修飾子解決誤答です。誤答D修飾子解決は並列実行の許可の選択で、主題は修飾子解決です。除外D修飾子解決では並列実行の許可を外す理由も修飾子解決誤答です。初出語修飾子解決として、指定名 QUALIFIER はDb2の指定または確認表であり焦点は修飾子解決定義です。位置付け修飾子解決は未修飾名の解決位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>QUALIFIER</strong></p><p>検証目的: 変更検査のDb2について、QUALIFIER は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020080の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更検査のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にQUALIFIERを指定し、OSKB020080の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND QUALIFIER
CASE OSKB020080
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM QUALIFIER
CASE OSKB020080
SOURCE Db2 for z/OS
QUALIFIERとOSKB020080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020080を同じ出力で読み、変更検査のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020080
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020080
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020080
DSNV401IとOSKB020080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の QUALIFIER と OSKB020080 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0015"><h3>RELEASE</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>RELEASEは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（5問）</summary><div class="kb-q"><p><strong>問題.</strong> 解放時点を導入設計で確認します。Db2の作業記録に資源解放の時点の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. RELEASE <span class="kb-ok">✅ 正解</span></li><li>C. KEEPDYNAMIC</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答解放時点はBです。論点解放時点における指定名 RELEASE の確認軸名は解放時点確認です。長時間実行ジョブの待ちを評価しますので、目的名は解放時点目的です。解放時点で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は解放時点説明です。誤答A解放時点は前回アクセスパスの再利用の選択で、主題は解放時点です。除外A解放時点では前回アクセスパスの再利用を外す理由も解放時点誤答です。Bが正解です。論点解放時点の指定名 RELEASE が該当します。目的解放時点で読むパッケージカタログの根拠名は解放時点根拠です。誤答C解放時点は準備済み動的SQL文の保持の選択で、主題は解放時点です。除外C解放時点では準備済み動的SQL文の保持を外す理由も解放時点誤答です。誤答D解放時点は並列実行の許可の選択で、主題は解放時点です。除外D解放時点では並列実行の許可を外す理由も解放時点誤答です。初出語解放時点として、指定名 RELEASE はDb2の指定または確認表であり焦点は解放時点定義です。位置付け解放時点は資源解放の時点位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 解放時点を変更審査で確認します。Db2の作業記録に資源解放の時点の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. ENCODING</li><li>C. RELEASE <span class="kb-ok">✅ 正解</span></li><li>D. CURRENTDATA</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答解放時点はCです。論点解放時点における指定名 RELEASE の確認軸名は解放時点確認です。長時間実行ジョブの待ちを評価しますので、目的名は解放時点目的です。解放時点で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は解放時点説明です。誤答A解放時点は前回コピーへの切り替えの選択で、主題は解放時点です。除外A解放時点では前回コピーへの切り替えを外す理由も解放時点誤答です。誤答B解放時点は文字データの符号化の選択で、主題は解放時点です。除外B解放時点では文字データの符号化を外す理由も解放時点誤答です。Cが正解です。論点解放時点の指定名 RELEASE が該当します。目的解放時点で読むパッケージカタログの根拠名は解放時点根拠です。誤答D解放時点はカーソル読み取りの現在性の選択で、主題は解放時点です。除外D解放時点ではカーソル読み取りの現在性を外す理由も解放時点誤答です。初出語解放時点として、指定名 RELEASE はDb2の指定または確認表であり焦点は解放時点定義です。位置付け解放時点は資源解放の時点位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 解放時点を性能調査で確認します。Db2の作業記録に資源解放の時点の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. PLAN_TABLE</li><li>C. APREUSE</li><li>D. RELEASE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答解放時点はDです。論点解放時点における指定名 RELEASE の確認軸名は解放時点確認です。長時間実行ジョブの待ちを評価しますので、目的名は解放時点目的です。解放時点で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は解放時点説明です。誤答A解放時点は成果物の所有者の選択で、主題は解放時点です。除外A解放時点では成果物の所有者を外す理由も解放時点誤答です。誤答B解放時点はEXPLAIN基本表の選択で、主題は解放時点です。除外B解放時点ではEXPLAIN基本表を外す理由も解放時点誤答です。誤答C解放時点は前回アクセスパスの再利用の選択で、主題は解放時点です。除外C解放時点では前回アクセスパスの再利用を外す理由も解放時点誤答です。Dが正解です。論点解放時点の指定名 RELEASE が該当します。目的解放時点で読むパッケージカタログの根拠名は解放時点根拠です。初出語解放時点として、指定名 RELEASE はDb2の指定または確認表であり焦点は解放時点定義です。位置付け解放時点は資源解放の時点位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 解放時点を障害復旧で確認します。Db2の作業記録に資源解放の時点の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. RELEASE <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. ISOLATION</li><li>D. QUALIFIER</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答解放時点はAです。論点解放時点における指定名 RELEASE の確認軸名は解放時点確認です。長時間実行ジョブの待ちを評価しますので、目的名は解放時点目的です。解放時点で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は解放時点説明です。Aが正解です。論点解放時点の指定名 RELEASE が該当します。目的解放時点で読むパッケージカタログの根拠名は解放時点根拠です。誤答B解放時点は分離レベルの選択で、主題は解放時点です。除外B解放時点では分離レベルを外す理由も解放時点誤答です。誤答C解放時点は分離レベルの選択で、主題は解放時点です。除外C解放時点では分離レベルを外す理由も解放時点誤答です。誤答D解放時点は未修飾表名のスキーマの選択で、主題は解放時点です。除外D解放時点では未修飾表名のスキーマを外す理由も解放時点誤答です。初出語解放時点として、指定名 RELEASE はDb2の指定または確認表であり焦点は解放時点定義です。位置付け解放時点は資源解放の時点位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 頻繁に呼ばれる静的 SQL で、COMMIT ごとに資源を解放するかスレッド終了まで保持するかを決めたい状況です。確認するオプションはどれですか。</p><ul class="kb-choices"><li>A. SQLERROR</li><li>B. RELEASE <span class="kb-ok">✅ 正解</span></li><li>C. ACTION</li><li>D. DYNAMICRULES</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 資源解放の粒度を見ているため B が合い、COMMIT 時かスレッド終了時かは RELEASE で切り替えます。性能と資源保持の性質が変わります。A: SQL エラー時の作成結果です。C: 追加または置換の動作です。D: 動的 SQL の許可検査や修飾子に関係します；背景には資源解放のタイミングを決める BIND/REBIND の RELEASE は、パッケージが使うロックや内部資源の保持期間を調整します、COMMIT ごとに解放する指定は資源を早く戻し、スレッド終了まで保持する指定は高頻度処理で有利になる場合があります、性能改善と資源占有の副作用を運用設計で比較しますという関係があり、この区別で確認する名称は「RELEASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RELEASE</strong></p><p>検証目的: 展開判定のDb2について、RELEASE は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わりまに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020082の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRELEASEを指定し、OSKB020082の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RELEASE
CASE OSKB020082
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RELEASE
CASE OSKB020082
SOURCE Db2 for z/OS
RELEASEとOSKB020082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020082を同じ出力で読み、展開判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020082
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020082
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020082
DSNV401IとOSKB020082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RELEASE と OSKB020082 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0016"><h3>REOPT</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>REOPTは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 再最適化を導入設計で確認します。Db2の作業記録に実行時値による再最適化の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. REOPT <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. ACTION</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答再最適化はAです。論点再最適化における指定名 REOPT の確認軸名は再最適化確認です。値の偏りが大きいエスキューエルで検討しますので、目的名は再最適化目的です。再最適化で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は再最適化説明です。Aが正解です。論点再最適化の指定名 REOPT が該当します。目的再最適化で読むパッケージカタログの根拠名は再最適化根拠です。誤答B再最適化はルーチン探索順序の選択で、主題は再最適化です。除外B再最適化ではルーチン探索順序を外す理由も再最適化誤答です。誤答C再最適化は追加と置換の扱いの選択で、主題は再最適化です。除外C再最適化では追加と置換の扱いを外す理由も再最適化誤答です。誤答D再最適化は並列実行の許可の選択で、主題は再最適化です。除外D再最適化では並列実行の許可を外す理由も再最適化誤答です。初出語再最適化として、指定名 REOPT はDb2の指定または確認表であり焦点は再最適化定義です。位置付け再最適化は実行時値による再最適化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 再最適化を変更審査で確認します。Db2の作業記録に実行時値による再最適化の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. REOPT <span class="kb-ok">✅ 正解</span></li><li>C. RELEASE</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答再最適化はBです。論点再最適化における指定名 REOPT の確認軸名は再最適化確認です。値の偏りが大きいエスキューエルで検討しますので、目的名は再最適化目的です。再最適化で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は再最適化説明です。誤答A再最適化は前回アクセスパスの再利用の選択で、主題は再最適化です。除外A再最適化では前回アクセスパスの再利用を外す理由も再最適化誤答です。Bが正解です。論点再最適化の指定名 REOPT が該当します。目的再最適化で読むパッケージカタログの根拠名は再最適化根拠です。誤答C再最適化は資源解放の時点の選択で、主題は再最適化です。除外C再最適化では資源解放の時点を外す理由も再最適化誤答です。誤答D再最適化は準備済み動的SQL文の保持の選択で、主題は再最適化です。除外D再最適化では準備済み動的SQL文の保持を外す理由も再最適化誤答です。初出語再最適化として、指定名 REOPT はDb2の指定または確認表であり焦点は再最適化定義です。位置付け再最適化は実行時値による再最適化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 再最適化を性能調査で確認します。Db2の作業記録に実行時値による再最適化の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. PLANMGMT</li><li>C. REOPT <span class="kb-ok">✅ 正解</span></li><li>D. APCOMPARE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答再最適化はCです。論点再最適化における指定名 REOPT の確認軸名は再最適化確認です。値の偏りが大きいエスキューエルで検討しますので、目的名は再最適化目的です。再最適化で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は再最適化説明です。誤答A再最適化は前回コピーへの切り替えの選択で、主題は再最適化です。除外A再最適化では前回コピーへの切り替えを外す理由も再最適化誤答です。誤答B再最適化はパッケージコピーの保持の選択で、主題は再最適化です。除外B再最適化ではパッケージコピーの保持を外す理由も再最適化誤答です。Cが正解です。論点再最適化の指定名 REOPT が該当します。目的再最適化で読むパッケージカタログの根拠名は再最適化根拠です。誤答D再最適化はアクセスパス差分の比較の選択で、主題は再最適化です。除外D再最適化ではアクセスパス差分の比較を外す理由も再最適化誤答です。初出語再最適化として、指定名 REOPT はDb2の指定または確認表であり焦点は再最適化定義です。位置付け再最適化は実行時値による再最適化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 再最適化を障害復旧で確認します。Db2の作業記録に実行時値による再最適化の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. QUERYACCELERATION</li><li>C. VALIDATE</li><li>D. REOPT <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答再最適化はDです。論点再最適化における指定名 REOPT の確認軸名は再最適化確認です。値の偏りが大きいエスキューエルで検討しますので、目的名は再最適化目的です。再最適化で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は再最適化説明です。誤答A再最適化は成果物の所有者の選択で、主題は再最適化です。除外A再最適化では成果物の所有者を外す理由も再最適化誤答です。誤答B再最適化はアクセラレーター利用方針の選択で、主題は再最適化です。除外B再最適化ではアクセラレーター利用方針を外す理由も再最適化誤答です。誤答C再最適化は検査時期の選択で、主題は再最適化です。除外C再最適化では検査時期を外す理由も再最適化誤答です。Dが正解です。論点再最適化の指定名 REOPT が該当します。目的再最適化で読むパッケージカタログの根拠名は再最適化根拠です。初出語再最適化として、指定名 REOPT はDb2の指定または確認表であり焦点は再最適化定義です。位置付け再最適化は実行時値による再最適化位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REOPT</strong></p><p>検証目的: 呼出判定のDb2について、REOPT は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わります。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020083の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にREOPTを指定し、OSKB020083の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND REOPT
CASE OSKB020083
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM REOPT
CASE OSKB020083
SOURCE Db2 for z/OS
REOPTとOSKB020083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020083を同じ出力で読み、呼出判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020083
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020083
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020083
DSNV401IとOSKB020083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の REOPT と OSKB020083 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0017"><h3>SQLERROR</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>SQLERRORは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> エラー時成果物を導入設計で確認します。Db2の作業記録にエスキューエルエラー時の成果物作成の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. SQLERROR <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. ISOLATION</li><li>D. QUALIFIER</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答エラー時成果物はAです。論点エラー時成果物における指定名 SQLERROR の確認軸名はエラー時成果物確認です。移行リハーサルと本番導入で値を分けますので、目的名はエラー時成果物目的です。エラー時成果物で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はエラー時成果物説明です。Aが正解です。論点エラー時成果物の指定名 SQLERROR が該当します。目的エラー時成果物で読むパッケージカタログの根拠名はエラー時成果物根拠です。誤答Bエラー時成果物は分離レベルの選択で、主題はエラー時成果物です。除外Bエラー時成果物では分離レベルを外す理由もエラー時成果物誤答です。誤答Cエラー時成果物は分離レベルの選択で、主題はエラー時成果物です。除外Cエラー時成果物では分離レベルを外す理由もエラー時成果物誤答です。誤答Dエラー時成果物は未修飾表名のスキーマの選択で、主題はエラー時成果物です。除外Dエラー時成果物では未修飾表名のスキーマを外す理由もエラー時成果物誤答です。初出語エラー時成果物として、指定名 SQLERROR はDb2の指定または確認表であり焦点はエラー時成果物定義です。位置付けエラー時成果物はエスキューエルエラー時の成果物作成位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> エラー時成果物を変更審査で確認します。Db2の作業記録にエスキューエルエラー時の成果物作成の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. SQLERROR <span class="kb-ok">✅ 正解</span></li><li>C. PLANMGMT</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答エラー時成果物はBです。論点エラー時成果物における指定名 SQLERROR の確認軸名はエラー時成果物確認です。移行リハーサルと本番導入で値を分けますので、目的名はエラー時成果物目的です。エラー時成果物で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はエラー時成果物説明です。誤答Aエラー時成果物は動的SQLの権限文脈の選択で、主題はエラー時成果物です。除外Aエラー時成果物では動的SQLの権限文脈を外す理由もエラー時成果物誤答です。Bが正解です。論点エラー時成果物の指定名 SQLERROR が該当します。目的エラー時成果物で読むパッケージカタログの根拠名はエラー時成果物根拠です。誤答Cエラー時成果物はパッケージコピーの保持の選択で、主題はエラー時成果物です。除外Cエラー時成果物ではパッケージコピーの保持を外す理由もエラー時成果物誤答です。誤答Dエラー時成果物はパッケージコピーの保持の選択で、主題はエラー時成果物です。除外Dエラー時成果物ではパッケージコピーの保持を外す理由もエラー時成果物誤答です。初出語エラー時成果物として、指定名 SQLERROR はDb2の指定または確認表であり焦点はエラー時成果物定義です。位置付けエラー時成果物はエスキューエルエラー時の成果物作成位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> エラー時成果物を性能調査で確認します。Db2の作業記録にエスキューエルエラー時の成果物作成の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. OPTHINT</li><li>C. SQLERROR <span class="kb-ok">✅ 正解</span></li><li>D. PATH</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答エラー時成果物はCです。論点エラー時成果物における指定名 SQLERROR の確認軸名はエラー時成果物確認です。移行リハーサルと本番導入で値を分けますので、目的名はエラー時成果物目的です。エラー時成果物で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はエラー時成果物説明です。誤答Aエラー時成果物はアクセスパス情報の出力の選択で、主題はエラー時成果物です。除外Aエラー時成果物ではアクセスパス情報の出力を外す理由もエラー時成果物誤答です。誤答Bエラー時成果物は最適化ヒントの利用の選択で、主題はエラー時成果物です。除外Bエラー時成果物では最適化ヒントの利用を外す理由もエラー時成果物誤答です。Cが正解です。論点エラー時成果物の指定名 SQLERROR が該当します。目的エラー時成果物で読むパッケージカタログの根拠名はエラー時成果物根拠です。誤答Dエラー時成果物はルーチン探索順序の選択で、主題はエラー時成果物です。除外Dエラー時成果物ではルーチン探索順序を外す理由もエラー時成果物誤答です。初出語エラー時成果物として、指定名 SQLERROR はDb2の指定または確認表であり焦点はエラー時成果物定義です。位置付けエラー時成果物はエスキューエルエラー時の成果物作成位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> エラー時成果物を障害復旧で確認します。Db2の作業記録にエスキューエルエラー時の成果物作成の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. APREUSE</li><li>C. PLAN_TABLE</li><li>D. SQLERROR <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答エラー時成果物はDです。論点エラー時成果物における指定名 SQLERROR の確認軸名はエラー時成果物確認です。移行リハーサルと本番導入で値を分けますので、目的名はエラー時成果物目的です。エラー時成果物で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点はエラー時成果物説明です。誤答Aエラー時成果物は準備済み動的SQL文の保持の選択で、主題はエラー時成果物です。除外Aエラー時成果物では準備済み動的SQL文の保持を外す理由もエラー時成果物誤答です。誤答Bエラー時成果物は前回アクセスパスの再利用の選択で、主題はエラー時成果物です。除外Bエラー時成果物では前回アクセスパスの再利用を外す理由もエラー時成果物誤答です。誤答Cエラー時成果物はEXPLAIN基本表の選択で、主題はエラー時成果物です。除外Cエラー時成果物ではEXPLAIN基本表を外す理由もエラー時成果物誤答です。Dが正解です。論点エラー時成果物の指定名 SQLERROR が該当します。目的エラー時成果物で読むパッケージカタログの根拠名はエラー時成果物根拠です。初出語エラー時成果物として、指定名 SQLERROR はDb2の指定または確認表であり焦点はエラー時成果物定義です。位置付けエラー時成果物はエスキューエルエラー時の成果物作成位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SQLERROR</strong></p><p>検証目的: 探索判定のDb2について、SQLERROR は、BIND または REBIND でパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わりに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索判定のDb2の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSQLERRORを指定し、OSKB020086の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SQLERROR
CASE OSKB020086
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SQLERROR
CASE OSKB020086
SOURCE Db2 for z/OS
SQLERRORとOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020086を同じ出力で読み、探索判定のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020086
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020086
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020086
DSNV401IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SQLERROR と OSKB020086 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div></details></section>


<section class="kb-item" id="c07-i0018"><h3>VALIDATE</h3><p class="kb-meta">分類: BIND/REBINDオプション &gt; BIND PACKAGE / BIND PLAN ・ 難易度: 中級</p><p>VALIDATEは、BINDまたはREBINDでパッケージ/プランの実行属性を決めるオプションです。指定値によって互換性、アクセスパス、ロック保持、動的SQLの扱いが変わります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 事前検査を導入設計で確認します。Db2の作業記録に検査時期の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. ISOLATION</li><li>C. QUERYACCELERATION</li><li>D. VALIDATE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答事前検査はDです。論点事前検査における指定名 VALIDATE の確認軸名は事前検査確認です。権限付与手順と導入順を合わせますので、目的名は事前検査目的です。事前検査で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前検査説明です。誤答A事前検査は準備済み動的SQL文の保持の選択で、主題は事前検査です。除外A事前検査では準備済み動的SQL文の保持を外す理由も事前検査誤答です。誤答B事前検査は分離レベルの選択で、主題は事前検査です。除外B事前検査では分離レベルを外す理由も事前検査誤答です。誤答C事前検査はアクセラレーター利用方針の選択で、主題は事前検査です。除外C事前検査ではアクセラレーター利用方針を外す理由も事前検査誤答です。Dが正解です。論点事前検査の指定名 VALIDATE が該当します。目的事前検査で読むパッケージカタログの根拠名は事前検査根拠です。初出語事前検査として、指定名 VALIDATE はDb2の指定または確認表であり焦点は事前検査定義です。位置付け事前検査は検査時期位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前検査を変更審査で確認します。Db2の作業記録に検査時期の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. VALIDATE <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. APPLCOMPAT</li><li>D. SWITCH(PREVIOUS)</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答事前検査はAです。論点事前検査における指定名 VALIDATE の確認軸名は事前検査確認です。権限付与手順と導入順を合わせますので、目的名は事前検査目的です。事前検査で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前検査説明です。Aが正解です。論点事前検査の指定名 VALIDATE が該当します。目的事前検査で読むパッケージカタログの根拠名は事前検査根拠です。誤答B事前検査はルーチン探索順序の選択で、主題は事前検査です。除外B事前検査ではルーチン探索順序を外す理由も事前検査誤答です。誤答C事前検査は互換性レベルの選択で、主題は事前検査です。除外C事前検査では互換性レベルを外す理由も事前検査誤答です。誤答D事前検査は前回コピーへの切り替えの選択で、主題は事前検査です。除外D事前検査では前回コピーへの切り替えを外す理由も事前検査誤答です。初出語事前検査として、指定名 VALIDATE はDb2の指定または確認表であり焦点は事前検査定義です。位置付け事前検査は検査時期位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前検査を性能調査で確認します。Db2の作業記録に検査時期の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. VALIDATE <span class="kb-ok">✅ 正解</span></li><li>C. KEEPDYNAMIC</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答事前検査はBです。論点事前検査における指定名 VALIDATE の確認軸名は事前検査確認です。権限付与手順と導入順を合わせますので、目的名は事前検査目的です。事前検査で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前検査説明です。誤答A事前検査は前回アクセスパスの再利用の選択で、主題は事前検査です。除外A事前検査では前回アクセスパスの再利用を外す理由も事前検査誤答です。Bが正解です。論点事前検査の指定名 VALIDATE が該当します。目的事前検査で読むパッケージカタログの根拠名は事前検査根拠です。誤答C事前検査は準備済み動的SQL文の保持の選択で、主題は事前検査です。除外C事前検査では準備済み動的SQL文の保持を外す理由も事前検査誤答です。誤答D事前検査は並列実行の許可の選択で、主題は事前検査です。除外D事前検査では並列実行の許可を外す理由も事前検査誤答です。初出語事前検査として、指定名 VALIDATE はDb2の指定または確認表であり焦点は事前検査定義です。位置付け事前検査は検査時期位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前検査を障害復旧で確認します。Db2の作業記録に検査時期の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. ENCODING</li><li>C. VALIDATE <span class="kb-ok">✅ 正解</span></li><li>D. CURRENTDATA</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答事前検査はCです。論点事前検査における指定名 VALIDATE の確認軸名は事前検査確認です。権限付与手順と導入順を合わせますので、目的名は事前検査目的です。事前検査で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前検査説明です。誤答A事前検査は前回コピーへの切り替えの選択で、主題は事前検査です。除外A事前検査では前回コピーへの切り替えを外す理由も事前検査誤答です。誤答B事前検査は文字データの符号化の選択で、主題は事前検査です。除外B事前検査では文字データの符号化を外す理由も事前検査誤答です。Cが正解です。論点事前検査の指定名 VALIDATE が該当します。目的事前検査で読むパッケージカタログの根拠名は事前検査根拠です。誤答D事前検査はカーソル読み取りの現在性の選択で、主題は事前検査です。除外D事前検査ではカーソル読み取りの現在性を外す理由も事前検査誤答です。初出語事前検査として、指定名 VALIDATE はDb2の指定または確認表であり焦点は事前検査定義です。位置付け事前検査は検査時期位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## BIND・パッケージ・プラン > アクセスパス管理


<section class="kb-item" id="c07-i0019"><h3>PLAN_TABLE</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; アクセスパス管理 ・ 難易度: 中級</p><p>PLAN_TABLEは、Db2 for z/OSのアクセスパス管理で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。アクセスパス管理では、指定値と対象資源、実行時の出力を突き合わせて確認する。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 経路表確認を導入設計で確認します。Db2の作業記録にアクセスパスの基本行の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. PLAN_TABLE <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. REOPT</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答経路表確認はAです。論点経路表確認における指定名 PLAN_TABLE の確認軸名は経路表確認確認です。計画番号やアクセス種別を手掛かりに読みますので、目的名は経路表確認目的です。経路表確認で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路表確認説明です。Aが正解です。論点経路表確認の指定名 PLAN_TABLE が該当します。目的経路表確認で読む説明表の根拠名は経路表確認根拠です。誤答B経路表確認は分離レベルの選択で、主題は経路表確認です。除外B経路表確認では分離レベルを外す理由も経路表確認誤答です。誤答C経路表確認は実行時値による再最適化の選択で、主題は経路表確認です。除外C経路表確認では実行時値による再最適化を外す理由も経路表確認誤答です。誤答D経路表確認は動的SQL文の集約の選択で、主題は経路表確認です。除外D経路表確認では動的SQL文の集約を外す理由も経路表確認誤答です。初出語経路表確認として、指定名 PLAN_TABLE はDb2の指定または確認表であり焦点は経路表確認定義です。位置付け経路表確認はアクセスパスの基本行位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路表確認を変更審査で確認します。Db2の作業記録にアクセスパスの基本行の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. PLAN_TABLE <span class="kb-ok">✅ 正解</span></li><li>C. PATH</li><li>D. OWNER</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答経路表確認はBです。論点経路表確認における指定名 PLAN_TABLE の確認軸名は経路表確認確認です。計画番号やアクセス種別を手掛かりに読みますので、目的名は経路表確認目的です。経路表確認で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路表確認説明です。誤答A経路表確認は動的SQLの権限文脈の選択で、主題は経路表確認です。除外A経路表確認では動的SQLの権限文脈を外す理由も経路表確認誤答です。Bが正解です。論点経路表確認の指定名 PLAN_TABLE が該当します。目的経路表確認で読む説明表の根拠名は経路表確認根拠です。誤答C経路表確認はルーチン探索順序の選択で、主題は経路表確認です。除外C経路表確認ではルーチン探索順序を外す理由も経路表確認誤答です。誤答D経路表確認は成果物の所有者の選択で、主題は経路表確認です。除外D経路表確認では成果物の所有者を外す理由も経路表確認誤答です。初出語経路表確認として、指定名 PLAN_TABLE はDb2の指定または確認表であり焦点は経路表確認定義です。位置付け経路表確認はアクセスパスの基本行位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路表確認を性能調査で確認します。Db2の作業記録にアクセスパスの基本行の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. EXPLAIN(ONLY)</li><li>C. PLAN_TABLE <span class="kb-ok">✅ 正解</span></li><li>D. SQLERROR</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答経路表確認はCです。論点経路表確認における指定名 PLAN_TABLE の確認軸名は経路表確認確認です。計画番号やアクセス種別を手掛かりに読みますので、目的名は経路表確認目的です。経路表確認で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路表確認説明です。誤答A経路表確認はパッケージコピーの保持の選択で、主題は経路表確認です。除外A経路表確認ではパッケージコピーの保持を外す理由も経路表確認誤答です。誤答B経路表確認は候補アクセスパスの事前出力の選択で、主題は経路表確認です。除外B経路表確認では候補アクセスパスの事前出力を外す理由も経路表確認誤答です。Cが正解です。論点経路表確認の指定名 PLAN_TABLE が該当します。目的経路表確認で読む説明表の根拠名は経路表確認根拠です。誤答D経路表確認はSQLエラー時の成果物作成の選択で、主題は経路表確認です。除外D経路表確認ではSQLエラー時の成果物作成を外す理由も経路表確認誤答です。初出語経路表確認として、指定名 PLAN_TABLE はDb2の指定または確認表であり焦点は経路表確認定義です。位置付け経路表確認はアクセスパスの基本行位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路表確認を障害復旧で確認します。Db2の作業記録にアクセスパスの基本行の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. CURRENTDATA</li><li>B. VALIDATE</li><li>C. OPTHINT</li><li>D. PLAN_TABLE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答経路表確認はDです。論点経路表確認における指定名 PLAN_TABLE の確認軸名は経路表確認確認です。計画番号やアクセス種別を手掛かりに読みますので、目的名は経路表確認目的です。経路表確認で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路表確認説明です。誤答A経路表確認はカーソル読み取りの現在性の選択で、主題は経路表確認です。除外A経路表確認ではカーソル読み取りの現在性を外す理由も経路表確認誤答です。誤答B経路表確認は検査時期の選択で、主題は経路表確認です。除外B経路表確認では検査時期を外す理由も経路表確認誤答です。誤答C経路表確認は最適化ヒントの利用の選択で、主題は経路表確認です。除外C経路表確認では最適化ヒントの利用を外す理由も経路表確認誤答です。Dが正解です。論点経路表確認の指定名 PLAN_TABLE が該当します。目的経路表確認で読む説明表の根拠名は経路表確認根拠です。初出語経路表確認として、指定名 PLAN_TABLE はDb2の指定または確認表であり焦点は経路表確認定義です。位置付け経路表確認はアクセスパスの基本行位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PLAN_TABLE</strong></p><p>検証目的: 探索検査のアクセスパス管理について、PLAN_TABLE は、Db2 for z/OS のアクセスパス管理で用いる Db2の性能診断やモニタリングで使う情報または収集単位です。SQL の実行計画、待ち時間、トレース情に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索検査のアクセスパス管理の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にPLAN_TABLEを指定し、OSKB010066の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND PLAN_TABLE
CASE OSKB010066
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM PLAN_TABLE
CASE OSKB010066
SOURCE Db2 for z/OS
PLAN_TABLEとOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010066を同じ出力で読み、探索検査のアクセスパス管理の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010066
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010066
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010066
DSNV401IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の PLAN_TABLE と OSKB010066 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0020"><h3>access path reuse</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; アクセスパス管理 ・ 難易度: 中級</p><p>access path reuseは、BIND・パッケージ・プランの中でアクセスパス管理に関わるDb2技術項目です。実行単位、BIND操作、アクセスパス、互換性、再バインド時の影響。一方で、SQL文の業務意味、EXPLAIN結果の詳細分析手順、JCL手順。 Db2アプリの実行単位とBIND操作として扱い、SQLの意味や性能分析そのものとは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 再バインドで性能が急変しないよう、以前の実行計画に近い判断を残したい状況です。注目する考え方は何ですか。</p><ul class="kb-choices"><li>A. 行アクセス制御。</li><li>B. 時間対応表。</li><li>C. 再利用方針。 <span class="kb-ok">✅ 正解</span></li><li>D. ログ表示。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cを選びます。この考え方は過去のアクセスパス利用を意識する管理方法です。性能変動を抑えたい再バインドで検討します。Aは行アクセス制御、Bは時間対応表、Dはログ表示であり、再バインド時のアクセスパス維持を扱う項目ではありません；背景には既存の実行計画を尊重する access path reuse は、BIND・パッケージ・プランのアクセスパス管理に関わる考え方です、再バインド時に過去のアクセスパスを再利用できるかを確認し、性能変動の抑制に使います、統計更新後でも常に同じ結果になるとは限りませんという関係があり、この区別で確認する名称は「access」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>access path reuse</strong></p><p>検証目的: 上書検査のアクセスパス管理について、access path reuseは、BIND ・パッケージ・プランの中でアクセスパス管理に関わる Db2技術項目です。実行単位、BIND 操作、アクセスパス、互換性、再バインドに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書検査のアクセスパス管理の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にaccess path reuseを指定し、OSKB010067の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND access path reuse
CASE OSKB010067
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM access path reuse
CASE OSKB010067
SOURCE Db2 for z/OS
access path reuseとOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010067を同じ出力で読み、上書検査のアクセスパス管理の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010067
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010067
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010067
DSNV401IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の access path reuse と OSKB010067 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## BIND・パッケージ・プラン > バインドオプション


<section class="kb-item" id="c07-i0021"><h3>APPLCOMPAT</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインドオプション ・ 難易度: 上級</p><p>APPLCOMPATは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（6問）</summary><div class="kb-q"><p><strong>問題.</strong> 互換性水準を導入設計で確認します。Db2の作業記録にアプリケーション互換性の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. APPLCOMPAT <span class="kb-ok">✅ 正解</span></li><li>C. PLANMGMT</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答互換性水準はBです。論点互換性水準における指定名 APPLCOMPAT の確認軸名は互換性水準確認です。機能レベル移行時のエスキューエル挙動を固定しますので、目的名は互換性水準目的です。互換性水準で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は互換性水準説明です。誤答A互換性水準は動的SQLの権限文脈の選択で、主題は互換性水準です。除外A互換性水準では動的SQLの権限文脈を外す理由も互換性水準誤答です。Bが正解です。論点互換性水準の指定名 APPLCOMPAT が該当します。目的互換性水準で読むパッケージカタログの根拠名は互換性水準根拠です。誤答C互換性水準はパッケージコピーの保持の選択で、主題は互換性水準です。除外C互換性水準ではパッケージコピーの保持を外す理由も互換性水準誤答です。誤答D互換性水準はパッケージコピーの保持の選択で、主題は互換性水準です。除外D互換性水準ではパッケージコピーの保持を外す理由も互換性水準誤答です。初出語互換性水準として、指定名 APPLCOMPAT はDb2の指定または確認表であり焦点は互換性水準定義です。位置付け互換性水準はアプリケーション互換性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 互換性水準を変更審査で確認します。Db2の作業記録にアプリケーション互換性の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. EXPLAIN</li><li>B. OPTHINT</li><li>C. APPLCOMPAT <span class="kb-ok">✅ 正解</span></li><li>D. PATH</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答互換性水準はCです。論点互換性水準における指定名 APPLCOMPAT の確認軸名は互換性水準確認です。機能レベル移行時のエスキューエル挙動を固定しますので、目的名は互換性水準目的です。互換性水準で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は互換性水準説明です。誤答A互換性水準はアクセスパス情報の出力の選択で、主題は互換性水準です。除外A互換性水準ではアクセスパス情報の出力を外す理由も互換性水準誤答です。誤答B互換性水準は最適化ヒントの利用の選択で、主題は互換性水準です。除外B互換性水準では最適化ヒントの利用を外す理由も互換性水準誤答です。Cが正解です。論点互換性水準の指定名 APPLCOMPAT が該当します。目的互換性水準で読むパッケージカタログの根拠名は互換性水準根拠です。誤答D互換性水準はルーチン探索順序の選択で、主題は互換性水準です。除外D互換性水準ではルーチン探索順序を外す理由も互換性水準誤答です。初出語互換性水準として、指定名 APPLCOMPAT はDb2の指定または確認表であり焦点は互換性水準定義です。位置付け互換性水準はアプリケーション互換性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 互換性水準を性能調査で確認します。Db2の作業記録にアプリケーション互換性の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. KEEPDYNAMIC</li><li>B. APREUSE</li><li>C. PLAN_TABLE</li><li>D. APPLCOMPAT <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答互換性水準はDです。論点互換性水準における指定名 APPLCOMPAT の確認軸名は互換性水準確認です。機能レベル移行時のエスキューエル挙動を固定しますので、目的名は互換性水準目的です。互換性水準で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は互換性水準説明です。誤答A互換性水準は準備済み動的SQL文の保持の選択で、主題は互換性水準です。除外A互換性水準では準備済み動的SQL文の保持を外す理由も互換性水準誤答です。誤答B互換性水準は前回アクセスパスの再利用の選択で、主題は互換性水準です。除外B互換性水準では前回アクセスパスの再利用を外す理由も互換性水準誤答です。誤答C互換性水準はEXPLAIN基本表の選択で、主題は互換性水準です。除外C互換性水準ではEXPLAIN基本表を外す理由も互換性水準誤答です。Dが正解です。論点互換性水準の指定名 APPLCOMPAT が該当します。目的互換性水準で読むパッケージカタログの根拠名は互換性水準根拠です。初出語互換性水準として、指定名 APPLCOMPAT はDb2の指定または確認表であり焦点は互換性水準定義です。位置付け互換性水準はアプリケーション互換性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 互換性水準を障害復旧で確認します。Db2の作業記録にアプリケーション互換性の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. APPLCOMPAT <span class="kb-ok">✅ 正解</span></li><li>B. PATH</li><li>C. ACTION</li><li>D. DEGREE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答互換性水準はAです。論点互換性水準における指定名 APPLCOMPAT の確認軸名は互換性水準確認です。機能レベル移行時のエスキューエル挙動を固定しますので、目的名は互換性水準目的です。互換性水準で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は互換性水準説明です。Aが正解です。論点互換性水準の指定名 APPLCOMPAT が該当します。目的互換性水準で読むパッケージカタログの根拠名は互換性水準根拠です。誤答B互換性水準はルーチン探索順序の選択で、主題は互換性水準です。除外B互換性水準ではルーチン探索順序を外す理由も互換性水準誤答です。誤答C互換性水準は追加と置換の扱いの選択で、主題は互換性水準です。除外C互換性水準では追加と置換の扱いを外す理由も互換性水準誤答です。誤答D互換性水準は並列実行の許可の選択で、主題は互換性水準です。除外D互換性水準では並列実行の許可を外す理由も互換性水準誤答です。初出語互換性水準として、指定名 APPLCOMPAT はDb2の指定または確認表であり焦点は互換性水準定義です。位置付け互換性水準はアプリケーション互換性位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 機能レベル更新後、アプリケーションが使えるSQL機能の範囲を段階的に管理します。該当する指定は何ですか。</p><ul class="kb-choices"><li>A. コレクション名。</li><li>B. 統計収集。</li><li>C. 互換レベル。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理権限。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cが正しいです。この指定はアプリケーション互換性と利用可能なSQL機能範囲に関係します。Aはパッケージの集合名、Bは統計収集、Dは管理権限であり、機能レベル互換を制御しません。移行時の互換性を残すための判断材料になります；背景には機能レベル互換を指定する APPLCOMPAT は、BIND・パッケージ・プランでアプリケーションが利用できるSQL機能範囲を制御します、Db2の機能レベルを上げても、既存アプリケーションの挙動を段階的に切り替えるために使います、移行計画と合わせて指定しますという関係があり、この区別で確認する名称は「APPLCOMPAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 機能レベル移行後も、特定アプリケーションの静的 SQL を旧い互換性レベルで動かし続けたい状況です。使うオプションはどれですか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. SQLERROR</li><li>C. KEEPDYNAMIC</li><li>D. APPLCOMPAT <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 互換性レベルを制御する話なので D を選び、パッケージ単位の互換性は APPLCOMPAT で固定します。新機能への移行を段階化できる点が重要です。A: 旧コピー保持の管理です。B: SQL エラー時の作成可否です。C: 準備済み動的 SQL の保持です；背景にはDb2 機能レベルを上げた後も、静的 SQL の互換性を段階的に移す場合は APPLCOMPAT を使います、パッケージごとに利用するアプリケーション互換性を固定できるため、全アプリを同時に新挙動へ移さずに済みます、サブシステム既定値との差分を移行計画の確認項目に含めますという関係があり、この区別で確認する名称は「APPLCOMPAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>APPLCOMPAT</strong></p><p>検証目的: 終端検査のバインドオプションについて、APPLCOMPAT は、Db2アプリケーションのパッケージやプランに実行時属性を与えるための BIND 関連項目です。互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端検査のバインドオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にAPPLCOMPATを指定し、OSKB010065の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND APPLCOMPAT
CASE OSKB010065
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM APPLCOMPAT
CASE OSKB010065
SOURCE Db2 for z/OS
APPLCOMPATとOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010065を同じ出力で読み、終端検査のバインドオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010065
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010065
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010065
DSNV401IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の APPLCOMPAT と OSKB010065 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010065 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0022"><h3>ISOLATION bind option</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインドオプション ・ 難易度: 初級</p><p>ISOLATION bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 照会処理で、他処理の更新をどこまで見せるかを決めます。分離レベルを扱う指定は何ですか。</p><ul class="kb-choices"><li>A. 監査ポリシー。</li><li>B. 分離レベル。 <span class="kb-ok">✅ 正解</span></li><li>C. プラン作成。</li><li>D. アーカイブログ。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bが適切です。この指定は読み取り整合性とロックの強さに関係します。Aは監査設定、Cはプラン作成操作、Dはログ資材であり、並行実行時の見え方を指定するオプションではありません。読み取り整合性と待ち時間の両方に関係します；背景には並行実行時の見え方を決める ISOLATION は、BIND・パッケージ・プランでロックと参照整合性を調整する指定です、読取中に他トランザクションの変更をどこまで許すかが、待ち時間、整合性、性能に影響します、業務要件に合う分離レベルを選びますという関係があり、この区別で確認する名称は「ISOLATION」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISOLATION bind option</strong></p><p>検証目的: 展開検査のバインドオプションについて、ISOLATION bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるための BIND 関連項目です。互換性、アクセスパス、ロック保持、動に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開検査のバインドオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にISOLATION bind optを指定し、OSKB010062の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ISOLATION bind opt
CASE OSKB010062
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ISOLATION bind opt
CASE OSKB010062
SOURCE Db2 for z/OS
ISOLATION bind optとOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010062を同じ出力で読み、展開検査のバインドオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010062
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010062
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010062
DSNV401IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ISOLATION bind opt と OSKB010062 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0023"><h3>RELEASE bind option</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインドオプション ・ 難易度: 中級</p><p>RELEASE bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 実行後の資源保持を、コミット時か終了時かで調整します。確認する指定は何ですか。</p><ul class="kb-choices"><li>A. データベース表示。</li><li>B. 資源解放時点。 <span class="kb-ok">✅ 正解</span></li><li>C. ビュー定義。</li><li>D. パッケージ解放。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bが答えです。この指定は資源をいつ解放するかに関係します。Aは表示コマンド、Cはビュー定義、Dはパッケージ解放であり、実行中の資源保持時点を指定するものではありません。処理形態により望ましい保持時間が変わります；背景には資源を手放す時点を決める RELEASE は、BIND・パッケージ・プランでコミット時やプラン終了時の資源保持を調整します、長く保持すると再利用性は上がる一方、競合や資源占有が問題になります、オンライン処理とバッチ処理で判断が変わります、保持時間も設計値として確認しますという関係があり、この区別で確認する名称は「RELEASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RELEASE bind option</strong></p><p>検証目的: 呼出検査のバインドオプションについて、RELEASE bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるための BIND 関連項目です。互換性、アクセスパス、ロック保持、動的 Sに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出検査のバインドオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRELEASE bind optioを指定し、OSKB010063の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RELEASE bind optio
CASE OSKB010063
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RELEASE bind optio
CASE OSKB010063
SOURCE Db2 for z/OS
RELEASE bind optioとOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010063を同じ出力で読み、呼出検査のバインドオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010063
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010063
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010063
DSNV401IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RELEASE bind optio と OSKB010063 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0024"><h3>REOPT bind option</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインドオプション ・ 難易度: 中級</p><p>REOPT bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ホスト変数の実値によって最適なアクセスパスが変わります。実行時値を考慮する指定は何ですか。</p><ul class="kb-choices"><li>A. 表削除。</li><li>B. トレース表示。</li><li>C. 権限ロール。</li><li>D. 実行時再最適化。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dを選びます。この指定は実行時の値を最適化へ反映するかに関係します。AはDROP TABLE、BはDISPLAY TRACE、Cは権限管理のロールであり、アクセスパスを実行時値に合わせる指定ではありません。値の偏りが大きいSQLで検討します；背景には実行時の値を使って最適化する REOPT は、BIND・パッケージ・プランでアクセスパス選択を左右する指定です、ホスト変数やパラメーターマーカーの値を考慮するかにより、汎用的なアクセスパスと実行時に寄せた判断のバランスが変わります、値の偏りが大きいSQLで効きますという関係があり、この区別で確認する名称は「REOPT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REOPT bind option</strong></p><p>検証目的: 置換検査のバインドオプションについて、REOPT bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるための BIND 関連項目です。互換性、アクセスパス、ロック保持、動的 SQLに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換検査のバインドオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にREOPT bind optionを指定し、OSKB010064の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND REOPT bind option
CASE OSKB010064
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM REOPT bind option
CASE OSKB010064
SOURCE Db2 for z/OS
REOPT bind optionとOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010064を同じ出力で読み、置換検査のバインドオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010064
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010064
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010064
DSNV401IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の REOPT bind option と OSKB010064 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010064 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0025"><h3>VALIDATE bind option</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインドオプション ・ 難易度: 中級</p><p>VALIDATE bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 権限が実行時に整う前提のパッケージを扱います。バインド時の検査動作を調整する項目は何ですか。</p><ul class="kb-choices"><li>A. 検査時点の指定。 <span class="kb-ok">✅ 正解</span></li><li>B. 表スペース作成。</li><li>C. 接続先表示。</li><li>D. プラン解放。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aが正しいです。この指定は権限などの確認時点に関係します。BはDDL、Cは表示コマンド、Dはプラン解放であり、バインド時と実行時の検査方針を決めません。権限確認の失敗をどこで扱うかが焦点です。実行時の再確認も判断材料です；背景には権限検査の時点を決める VALIDATE は、BIND・パッケージ・プランで検査動作を調整する指定です、バインド時に確認するか、実行時に再確認できる形にするかが、パッケージ作成時の失敗条件と実行時の挙動へ影響します、権限不足をどこで検出したいかを決めますという関係があり、この区別で確認する名称は「VALIDATE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VALIDATE bind option</strong></p><p>検証目的: 構文検査のバインドオプションについて、VALIDATE bind optionは、Db2アプリケーションのパッケージやプランに実行時属性を与えるための BIND 関連項目です。互換性、アクセスパス、ロック保持、動的に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文検査のバインドオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にVALIDATE bind optiを指定し、OSKB010061の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND VALIDATE bind opti
CASE OSKB010061
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM VALIDATE bind opti
CASE OSKB010061
SOURCE Db2 for z/OS
VALIDATE bind optiとOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010061を同じ出力で読み、構文検査のバインドオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010061
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010061
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010061
DSNV401IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の VALIDATE bind opti と OSKB010061 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010061 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## BIND・パッケージ・プラン > バインド操作


<section class="kb-item" id="c07-i0026"><h3>BIND PACKAGE</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインド操作 ・ 難易度: 中級</p><p>BIND PACKAGEは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認のアプリケーション実行に関する BIND PACKAGE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. -DISPLAY THREAD(*)の結果を残さず優先確認のアプリケーション実行の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認のアプリケーション実行の証跡として保存して根拠にする。</li><li>C. BIND PACKAGE の変更点を出力本文から切り離して優先確認のアプリケーション実行の承認欄のみ残す。</li><li>D. DSNV401I を含む表示を保存し、説明欄との差分を優先確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では BIND PACKAGE は「BIND PACKAGE の状態と出力メッセージを結び付ける優先確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では BIND PACKAGE の出力行と DSNV401I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では BIND PACKAGE を Db2 for z/OS の確認記録に残し、対象名は優先確認対象です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BIND PACKAGE</strong></p><p>検証目的: 優先確認のアプリケーション実行について、Db2 for z/OS の アプリケーション実行で扱う BIND PACKAGE は、SQL を含むプログラムの DBRM などからパッケージを作成または更新する操作です。アに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD(*) を入力し、優先確認のアプリケーション実行の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にBIND PACKAGEを指定し、OSKB010012の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND BIND PACKAGE
CASE OSKB010012
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM BIND PACKAGE
CASE OSKB010012
SOURCE Db2 for z/OS
BIND PACKAGEとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010012を同じ出力で読み、優先確認のアプリケーション実行の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
CASE OSKB010012
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010012
-DISPLAY THREAD(*)
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010012
DSNV401IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD(*) が画面・出力に表示されること
② ステップ2 の BIND PACKAGE と OSKB010012 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


<section class="kb-item" id="c07-i0027"><h3>BIND PLAN</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインド操作 ・ 難易度: 中級</p><p>BIND PLANは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複数のパッケージをアプリケーションの実行入口としてまとめ、カタログに保存したい状況です。選ぶ操作は何ですか。</p><ul class="kb-choices"><li>A. ログ状態を表示する操作。</li><li>B. 既存表に列を追加する操作。</li><li>C. カーソルを宣言するSQL。</li><li>D. プラン作成。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dを選びます。この操作はプランを作り、実行時に必要なパッケージや資源関係をまとめます。AはDISPLAY LOG、BはALTER TABLE、CはDECLARE CURSORであり、プラン作成の操作ではありません；背景には実行入口を作る BIND PLAN は、BIND・パッケージ・プランのバインド操作としてアプリケーションプランを作成します、パッケージリスト、コレクション、DBRMから作られるパッケージを指定できます、すべてのDb2プログラムで実行時資源を割り当てるために使いますという関係があり、この区別で確認する名称は「BIND」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0028"><h3>FREE PACKAGE</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインド操作 ・ 難易度: 中級</p><p>FREE PACKAGEは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 廃止済みプログラムのパッケージを、Db2側の管理対象から外します。対象がパッケージならどの操作を選びますか。</p><ul class="kb-choices"><li>A. パッケージ解放。 <span class="kb-ok">✅ 正解</span></li><li>B. 表の列値を更新するSQL。</li><li>C. SQLCAを参照する処理。</li><li>D. トレースの一覧表示。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aが答えです。この操作は不要になったパッケージを解放します。BはUPDATE、Cはエラー処理、DはDISPLAY TRACEであり、Db2側のパッケージ資材を含めない操作ではありません。削除前に参照プランの有無も確認します；背景には不要な実行資材を含めない FREE PACKAGE は、BIND・パッケージ・プランのバインド操作でパッケージを解放します、使われなくなったパッケージを残すと、管理対象や依存関係の確認が複雑になります、代替手段や実行中プログラムの参照有無を確認してから扱いますという関係があり、この区別で確認する名称は「PACKAGE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0029"><h3>FREE PLAN</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインド操作 ・ 難易度: 中級</p><p>FREE PLANは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 使われなくなったアプリケーションプランを削除します。パッケージではなくプランを対象にする操作は何ですか。</p><ul class="kb-choices"><li>A. ログを表示するコマンド。</li><li>B. プラン解放。 <span class="kb-ok">✅ 正解</span></li><li>C. 表へ別名を付けるDDL。</li><li>D. 分離レベルを指定するオプション。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bを選びます。この操作は不要なプランを解放し、アプリケーションの実行入口を外します。AはDISPLAY LOG、CはCREATE ALIAS、DはISOLATION指定であり、プラン削除の操作ではありません；背景にはプランを解放する FREE PLAN は、BIND・パッケージ・プランで不要になったアプリケーションプランを削除する操作です、プランを含めないと実行入口が失われるため、対象アプリケーションが停止済みか、代替プランへ切替済みかを確認します、パッケージ解放と混同しないようにしますという関係があり、この区別で確認する名称は「FREE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FREE PLAN</strong></p><p>検証目的: 変更追跡のバインド操作について、FREE PLAN は、Db2アプリケーションのパッケージやプランに実行時属性を与えるための BIND 関連項目です。互換性、アクセスパス、ロック保持、動的 SQL の扱いが変わるたに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更追跡のバインド操作の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にFREE PLANを指定し、OSKB010060の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND FREE PLAN
CASE OSKB010060
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM FREE PLAN
CASE OSKB010060
SOURCE Db2 for z/OS
FREE PLANとOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010060を同じ出力で読み、変更追跡のバインド操作の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010060
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010060
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010060
DSNV401IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の FREE PLAN と OSKB010060 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0030"><h3>REBIND PACKAGE</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインド操作 ・ 難易度: 中級</p><p>REBIND PACKAGEは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 統計収集後に既存パッケージのアクセスパスを再評価したい状況です。既存パッケージに対する操作は何ですか。</p><ul class="kb-choices"><li>A. 監査ポリシーを作成する操作。</li><li>B. パッケージ再作成。 <span class="kb-ok">✅ 正解</span></li><li>C. 表へ行を追加するSQL。</li><li>D. アーカイブログを表示する操作。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bが正しいです。この操作は既存パッケージを再処理し、アクセスパスや一部属性を見直します。Aは監査設定、CはINSERT、DはDISPLAY ARCHIVEであり、既存パッケージの再評価ではありません；背景には既存資材を作り直す REBIND PACKAGE は、BIND・パッケージ・プランのバインド操作で既存パッケージを再バインドします、SQL本文を変えない場合でも、統計、オプション、Db2機能レベルによりアクセスパスが変わる場合があります、実行影響を見積もってから適用しますという関係があり、この区別で確認する名称は「PACKAGE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0031"><h3>REBIND PLAN</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; バインド操作 ・ 難易度: 中級</p><p>REBIND PLANは、Db2アプリケーションのパッケージやプランに実行時属性を与えるためのBIND関連項目です。互換性、アクセスパス、ロック保持、動的SQLの扱いが変わるため、REBIND時の影響確認が重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アプリケーションの既存プランを、新しいバインド属性で作り直す必要があります。対象をプランにして実行する操作は何ですか。</p><ul class="kb-choices"><li>A. パッケージを削除する操作。</li><li>B. グループバッファプール表示。</li><li>C. プラン再作成。 <span class="kb-ok">✅ 正解</span></li><li>D. 表スペースを回復する操作。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cが該当します。この操作は既存プランを対象に再バインドします。AはFREE PACKAGE、BはDISPLAY GROUPBUFFERPOOL、DはRECOVER系の処理であり、プラン属性を作り直す操作ではありません；背景には既存プランを更新する REBIND PLAN は、BIND・パッケージ・プランでプランの実行属性を再作成する操作です、プランの内容、指定パッケージ、関連オプションを再評価したいときに使います、パッケージ単体の再バインドとは対象範囲が異なりますという関係があり、この区別で確認する名称は「REBIND」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## BIND・パッケージ・プラン > 実行単位


<section class="kb-item" id="c07-i0032"><h3>DBRM</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; 実行単位 ・ 難易度: 中級</p><p>DBRMは、BIND・パッケージ・プランの中で実行単位に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2アプリの実行単位とBIND操作として扱い、SQLの意味や性能分析そのものとは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRM</strong></p><p>検証目的: 値域追跡の実行単位について、DBRM は、BIND ・パッケージ・プランの中で実行単位に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2アプリに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、値域追跡の実行単位の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDBRMを指定し、OSKB010056の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DBRM
CASE OSKB010056
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DBRM
CASE OSKB010056
SOURCE Db2 for z/OS
DBRMとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010056を同じ出力で読み、値域追跡の実行単位の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010056
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010056
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010056
DSNV401IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DBRM と OSKB010056 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0033"><h3>collection</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; 実行単位 ・ 難易度: 中級</p><p>collectionは、BIND・パッケージ・プランの中で実行単位に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2アプリの実行単位とBIND操作として扱い、SQLの意味や性能分析そのものとは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> テスト用と本番用のパッケージを同名プログラムでも分けて扱いたい状況です。パッケージ集合を識別する名前空間は何ですか。</p><ul class="kb-choices"><li>A. アクティブログの切替状態。</li><li>B. 表やビューに付ける別名。</li><li>C. SQL権限をまとめるロール。</li><li>D. コレクション。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dが適切です。この名前空間はパッケージを分類して参照するために使います。Aはログ資材、BはALIAS、Cは権限管理の単位であり、パッケージ集合を識別する仕組みではありません。同名パッケージを環境別に分ける場面で効きます；背景にはパッケージを束ねる collection は、BIND・パッケージ・プランの実行単位を整理する名前空間です、プランのPKLISTや実行時の解決で、どの集合のパッケージを使うかを判断する手掛かりになります、環境別にパッケージを分ける場合は、命名と参照範囲をそろえますという関係があり、この区別で確認する名称は「collection」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>collection</strong></p><p>検証目的: 監査追跡の実行単位について、collectionは、BIND ・パッケージ・プランの中で実行単位に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、監査追跡の実行単位の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にcollectionを指定し、OSKB010059の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND collection
CASE OSKB010059
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM collection
CASE OSKB010059
SOURCE Db2 for z/OS
collectionとOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010059を同じ出力で読み、監査追跡の実行単位の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010059
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010059
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010059
DSNV401IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の collection と OSKB010059 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010059 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0034"><h3>package</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; 実行単位 ・ 難易度: 中級</p><p>packageは、BIND・パッケージ・プランの中で実行単位に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2アプリの実行単位とBIND操作として扱い、SQLの意味や性能分析そのものとは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>package</strong></p><p>検証目的: 警告追跡の実行単位について、packageは、BIND ・パッケージ・プランの中で実行単位に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、警告追跡の実行単位の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にpackageを指定し、OSKB010057の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND package
CASE OSKB010057
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM package
CASE OSKB010057
SOURCE Db2 for z/OS
packageとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010057を同じ出力で読み、警告追跡の実行単位の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010057
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010057
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010057
DSNV401IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の package と OSKB010057 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010057 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0035"><h3>plan</h3><p class="kb-meta">分類: BIND・パッケージ・プラン &gt; 実行単位 ・ 難易度: 中級</p><p>planは、BIND・パッケージ・プランの中で実行単位に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2アプリの実行単位とBIND操作として扱い、SQLの意味や性能分析そのものとは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> オンラインプログラムを実行するため、関連するパッケージをまとめて実行入口を作ります。ここで作る単位は何ですか。</p><ul class="kb-choices"><li>A. 統計を収集するユーティリティ。</li><li>B. 表へ新規行を追加する文。</li><li>C. グループバッファプールの表示結果。</li><li>D. プラン。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dが答えです。この実行入口はアプリケーション実行時に必要なDb2資源とパッケージ関係をまとめます。AはRUNSTATS、BはINSERT、Cはデータ共用の表示であり、実行入口の作成ではありません。プログラム起動時の入口になる点を確認します；背景にはアプリケーションの plan は、BIND・パッケージ・プランで実行時にDb2資源を割り当てる単位です、パッケージの一覧やDBRMから作られるパッケージを含められ、Db2カタログに保存されます、パッケージを使う構成でも、実行入口としてプランが必要ですという関係があり、この区別で確認する名称は「plan」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>plan</strong></p><p>検証目的: 復旧追跡の実行単位について、planは、BIND ・パッケージ・プランの中で実行単位に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2アプリに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、復旧追跡の実行単位の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にplanを指定し、OSKB010058の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND plan
CASE OSKB010058
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM plan
CASE OSKB010058
SOURCE Db2 for z/OS
planとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010058を同じ出力で読み、復旧追跡の実行単位の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010058
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010058
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010058
DSNV401IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の plan と OSKB010058 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## DDF・分散接続・ネットワーク > DBAT・スレッド運用


<section class="kb-item" id="c07-i0036"><h3>CMTSTAT</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DBAT・スレッド運用 ・ 難易度: 中級</p><p>CMTSTATは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 大量のクライアント接続を保持しつつ、UOWの合間にDBATをプールへ戻したい設計です。関係するサブシステムパラメータはどれですか。</p><ul class="kb-choices"><li>A. CMTSTAT <span class="kb-ok">✅ 正解</span></li><li>B. LOCKMAX</li><li>C. SEGSIZE</li><li>D. VALIDATE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aです。スレッド指定のCMTSTATはDDFスレッドの扱いに関わり、inactive connection supportの設計で確認します。Bはロック数上限です。Cは表スペース構造です。DはBIND時の検査タイミングです。接続を保持する設計ではDBATをいつ解放できるかが重要です；背景にはスレッド運用の指定として、Db2 for z/OSのCMTSTATはDDF THREADSの動きに関わるサブシステムパラメータです、設定値INACTIVEを使う構成では、接続とDBATをUOW境界で切り離し、DBATをプールへ戻せます、接続数とスレッド数を別々に見るための前提になりますという関係があり、この区別で確認する名称は「CMTSTAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div><div class="kb-q"><p><strong>問題.</strong> 分散トランザクションがコミットした後、DBATを解放しやすい状態にするか、活動状態のまま残しやすくするかを決めます。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. ロック待ち検出間隔</li><li>B. TCP/IPポート番号</li><li>C. コピー取得単位</li><li>D. コミット後スレッドをactive/inactiveにする指定 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> コミット後のDBAT状態を左右する指定なので、Dが正解です。AはIRLM周辺の待ち監視、Bは接続入口のTCP/IP値です。Cは回復用コピーを作る範囲であり、分散スレッドをactiveに残すかinactiveへ戻すかの方針ではありません；背景には分散スレッドの保持形態を決めるCMTSTATは、Db2 for z/OSのDDF・分散接続パラメータとしてコミット後のDBATをactiveまたはinactiveにする動作を指定します、現在はINACTIVEが推奨され、分散アプリケーションの拡張性や資源使用量の観点で確認しますという関係があり、この区別で確認する名称は「CMTSTAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CMTSTAT</strong></p><p>検証目的: 比較照合の・スレッド運用について、CMTSTAT は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較照合の・スレッド運用の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCMTSTATを指定し、OSKB020034の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CMTSTAT
CASE OSKB020034
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CMTSTAT
CASE OSKB020034
SOURCE Db2 for z/OS
CMTSTATとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020034を同じ出力で読み、比較照合の・スレッド運用の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020034
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020034
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020034
DSNV401IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CMTSTAT と OSKB020034 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0037"><h3>DBAT</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DBAT・スレッド運用 ・ 難易度: 中級</p><p>DBATは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 分散アプリケーションの接続は残っています。しかし、要求処理に使えるスレッドが足りない疑いがあります。DDFで処理単位として見るものはどれですか。</p><ul class="kb-choices"><li>A. catalog image copy</li><li>B. row mask</li><li>C. JCL symbolic parameter</li><li>D. database access thread <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dを選びます。リモート要求を処理するスレッドを確認すると、分散接続の処理余力を判断できます。Aはカタログ保護です。Bは列や行のアクセス制御です。CはJCL置換値です。接続数を主な根拠にしてなく、要求を処理するスレッド数を見ます；背景にはリモート要求を実行する単位として、Db2 for z/OSのDBATは分散接続からのSQLを処理するデータベースアクセススレッドです、接続数、スレッド数、プール状態、UOW境界の動きに関わります、要求が集中する時間帯は、使用中と待機中の区別が重要ですという関係があり、この区別で確認する名称は「DBAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBAT</strong></p><p>検証目的: 記録照合の・スレッド運用について、DBAT は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、記録照合の・スレッド運用の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDBATを指定し、OSKB020033の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DBAT
CASE OSKB020033
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DBAT
CASE OSKB020033
SOURCE Db2 for z/OS
DBATとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020033を同じ出力で読み、記録照合の・スレッド運用の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020033
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020033
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020033
DSNV401IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DBAT と OSKB020033 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0038"><h3>MAXDBAT</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DBAT・スレッド運用 ・ 難易度: 中級</p><p>MAXDBATは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 急にリモート接続を受け付けなくなり、DISPLAY DDF DETAILに現在値が出ています。DBAT数の上限として確認する値はどれですか。</p><ul class="kb-choices"><li>A. MAXKEEPD</li><li>B. MAXDBAT <span class="kb-ok">✅ 正解</span></li><li>C. MAXPARTITIONS</li><li>D. MAXROWS</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bが該当します。上限値のMAXDBATは同時に使えるDBAT数を制限し、0なら接続受付に影響します。Aは動的SQL保持の文脈です。Cは表スペース区画数です。DはDb2のDDF接続上限ではありません。値が低すぎると、接続待ちや受付不可の原因になります；背景には上限値として、Db2 for z/OSのMAXDBATは同時に使えるDBAT数を制限します、0の場合はDDFが接続を受け付けない理由になり、DISPLAY DDF DETAILのDSNL090Iでも値を確認できます、接続待ちや拒否の調査で重要ですという関係があり、この区別で確認する名称は「MAXDBAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div><div class="kb-q"><p><strong>問題.</strong> 分散アプリケーションの要求が集中し、同時に活動できるDBAT数をどこまで許すかを決めます。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. 接続総数の上限</li><li>B. 同時に活動できるDBAT数 <span class="kb-ok">✅ 正解</span></li><li>C. パッケージ保持期間の指定</li><li>D. DDFポートの暗号化方式</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 活動中のDBAT数そのものを制限するため、Bを選びます。Aは接続総数を広く見る別上限で、Cは動的SQL資材の保持に関わる指定です。Dは通信路の保護方式であり、活動スレッド数の調整ではありません。負荷ピーク時の待ちも観測します；背景にはリモート要求の活動量を抑えるMAXDBATは、Db2 for z/OSのDDF・分散接続パラメータとして同時に活動できるDBATの最大数を指定します、値が小さいと接続要求が待ちやすくなり、大きすぎるとスレッド資源やメモリへの影響を監視する必要がありますという関係があり、この区別で確認する名称は「MAXDBAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details></section>


## DDF・分散接続・ネットワーク > DDF基本・ポート


<section class="kb-item" id="c07-i0039"><h3>DDF</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DDF基本・ポート ・ 難易度: 中級</p><p>DDFは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リモートアプリケーションからDb2へSQL要求が届かないため、Db2側で分散要求を受け付ける機能の状態を確認します。最初に見る対象はどれですか。</p><ul class="kb-choices"><li>A. 分散要求を受け付けるDb2側の機能 <span class="kb-ok">✅ 正解</span></li><li>B. 表スペースのページサイズ</li><li>C. 監査ポリシーの保護状態</li><li>D. JCLのJOBクラス</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aを選びます。分散要求を受け付ける機能の状態を見れば、リモート接続の入口が開いているか判断できます。Bは格納設計です。Cはセキュリティ監査です。DはJESの実行分類であり、Db2の分散待ち受けではありません；背景には分散接続の入口として、Db2 for z/OSのDDFはリモートクライアントからの要求を受け付けます、分散要求にはDRDA、REST、DBAT、ポート番号、ロケーション名が関係します、接続不可の調査では、DDFが開始済みか、待ち受けポートが有効か、MAXDBATが0でないかを合わせて確認しますという関係があり、この区別で確認する名称は「DDF」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DDF</strong></p><p>検証目的: 上書照合の基本・ポートについて、DDF は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書照合の基本・ポートの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDDFを指定し、OSKB020027の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DDF
CASE OSKB020027
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DDF
CASE OSKB020027
SOURCE Db2 for z/OS
DDFとOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020027を同じ出力で読み、上書照合の基本・ポートの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020027
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020027
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020027
DSNV401IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DDF と OSKB020027 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0040"><h3>DRDA SQL port</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DDF基本・ポート ・ 難易度: 中級</p><p>DRDA SQL portは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 接続先ホストは正しいのに、通常のDRDA要求のみがDb2へ届きません。DISPLAY DDFで確認する主な待ち受け番号はどれですか。</p><ul class="kb-choices"><li>A. 監査レコード番号</li><li>B. 通常のSQL要求を受けるTCP/IPポート <span class="kb-ok">✅ 正解</span></li><li>C. BSDSのアーカイブ名</li><li>D. 表のパーティション番号</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bが該当します。通常のDRDAやREST要求は主ポートの待ち受け状態に依存します。Aは監査証跡の識別です。Cはログ管理資材です。Dはデータ配置の区分であり、接続入口の番号ではありません。入口番号の証跡を残すと、ネットワーク側との切り分けが進めやすくなります；背景には通常の入口として、Db2 for z/OSのDDFがDRDAやREST要求を受け付けるTCP/IPポートを見ます、DISPLAY DDFの出力では通常のSQLリスナーの値として示されます、0や-NONEに相当する状態なら、ネットワーク経由の要求を受け付けませんという関係があり、この区別で確認する名称は「DRDA」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DRDA SQL port</strong></p><p>検証目的: 出力照合の基本・ポートについて、DRDA SQL portは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象にに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力照合の基本・ポートの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDRDA SQL portを指定し、OSKB020028の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DRDA SQL port
CASE OSKB020028
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DRDA SQL port
CASE OSKB020028
SOURCE Db2 for z/OS
DRDA SQL portとOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020028を同じ出力で読み、出力照合の基本・ポートの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020028
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020028
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020028
DSNV401IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DRDA SQL port と OSKB020028 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0041"><h3>IPNAME</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DDF基本・ポート ・ 難易度: 中級</p><p>IPNAMEは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 動的な接続別名を設計する際、別名がどのIP名へ結び付くかを確認しています。DDF側で関連付ける値はどれですか。</p><ul class="kb-choices"><li>A. ユーティリティID</li><li>B. IP名の指定値 <span class="kb-ok">✅ 正解</span></li><li>C. 索引のクラスタ属性</li><li>D. SQLCODEの重大度</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bが適切です。IP名の指定値をDDFに関連付けることで、接続経路の名前解決を整理できます。Aはユーティリティ実行の識別です。Cは索引定義です。DはSQL実行結果の分類です。名前解決の誤りは接続不可に直結するため、別名やポートと一緒に確認します；背景には名前解決の指定として、Db2 for z/OSのIPNAMEはDDFに関連付けるIP名を示します、動的ロケーション別名やメンバー固有の接続経路を扱うとき、ホスト名、ポート、別名の組み合わせを混同しないことが重要です、変更する前に接続先名とIP名の対応を台帳へ残しますという関係があり、この区別で確認する名称は「IPNAME」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div><div class="kb-q"><p><strong>問題.</strong> Data Sharing構成で、各メンバーがTCP/IP通信上で同じグループ識別を使えるようにDDF側の名前をそろえます。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. カタログ所有者名</li><li>B. 統計履歴表の保守対象名</li><li>C. ユーティリティID</li><li>D. TCP/IP上のDDF識別名 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> TCP/IP通信でDDFを識別する名前を扱うため、Dが適切です。Aは定義表の管理主体、Bはアクセスパス診断に使う履歴表の対象です。Cは保守ジョブの実行単位で、分散接続のグループ識別とは別に扱います。開始応答でも同名を照合します；背景にはネットワーク上のDDF識別を揃えるIPNAMEは、Db2 for z/OSのDDF・分散接続パラメータとしてTCP/IP通信で使うDb2側の名前を指定します、データ共用構成ではグループ内で整合した値が求められ、DDF開始時のDSNL004IなどでLOCATIONやポートと合わせて確認しますという関係があり、この区別で確認する名称は「IPNAME」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IPNAME</strong></p><p>検証目的: 範囲照合の基本・ポートについて、IPNAME は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、範囲照合の基本・ポートの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にIPNAMEを指定し、OSKB020031の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND IPNAME
CASE OSKB020031
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM IPNAME
CASE OSKB020031
SOURCE Db2 for z/OS
IPNAMEとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020031を同じ出力で読み、範囲照合の基本・ポートの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020031
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020031
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020031
DSNV401IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の IPNAME と OSKB020031 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0042"><h3>RESPORT</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DDF基本・ポート ・ 難易度: 中級</p><p>RESPORTは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 分散トランザクション障害後、取引コーディネーターとの再同期が必要です。通常SQLの入口ではなく、再同期専用として確認する番号はどれですか。</p><ul class="kb-choices"><li>A. 表スペース番号</li><li>B. SQLCAのSQLERRD</li><li>C. 二相コミット再同期用ポート <span class="kb-ok">✅ 正解</span></li><li>D. パッケージのCOLLID</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cが正解です。二相コミットの再同期では専用ポートを使い、通常のSQLポートとは分けて管理します。Aはデータ配置側の識別です。BはSQL診断領域の値です。Dはパッケージ集合の識別子です。分散更新では通常SQLの入口と再同期入口を分けます；背景には再同期用の入口として、Db2 for z/OSのRESPORTはtwo-phase commitの再同期に使うTCP/IPポートです、Data Sharingでは同じグループの各メンバーで一意に割り当てる必要があります、通常のSQL要求を受けるPORTとは目的が違いますという関係があり、この区別で確認する名称は「RESPORT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div><div class="kb-q"><p><strong>問題.</strong> 通信障害後にトランザクション調停側から二相コミットの完了判断を受け直すため、通常SQLとは別のポートを用意します。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. 通常SQL受付口</li><li>B. 安全接続受付口</li><li>C. 再同期専用ポート <span class="kb-ok">✅ 正解</span></li><li>D. 分散接続待ち行列の上限</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 二相コミットの再同期要求を受ける用途なので、Cを選択します。Aは通常SQLの入口で、Bは暗号化通信を分ける安全側の受付です。Dは接続がDBATを待つときのキュー制御であり、復旧用ポートの値ではありません；背景には分散トランザクションの復旧で使うRESPORTは、Db2 for z/OSのDDF・分散接続パラメータとして二相コミットの再同期要求を受けるTCP/IPポートを割り当てます、通常SQL要求やセキュア接続とは別の目的であり、障害後の完了状態を整える経路として扱いますという関係があり、この区別で確認する名称は「RESPORT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>RESPORT</strong></p><p>検証目的: 区切照合の基本・ポートについて、RESPORT は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切照合の基本・ポートの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRESPORTを指定し、OSKB020030の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RESPORT
CASE OSKB020030
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RESPORT
CASE OSKB020030
SOURCE Db2 for z/OS
RESPORTとOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020030を同じ出力で読み、区切照合の基本・ポートの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020030
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020030
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020030
DSNV401IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RESPORT と OSKB020030 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>RESPORT</strong></p><p>検証目的: 上書検査の・分散接続について、RESPORT は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書検査の・分散接続の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRESPORTを指定し、OSKB020067の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RESPORT
CASE OSKB020067
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RESPORT
CASE OSKB020067
SOURCE Db2 for z/OS
RESPORTとOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020067を同じ出力で読み、上書検査の・分散接続の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020067
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020067
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020067
DSNV401IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RESPORT と OSKB020067 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0043"><h3>SECPORT</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; DDF基本・ポート ・ 難易度: 中級</p><p>SECPORTは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査で、暗号化された分散SQLのみを専用の入口で受け付ける構成か確認しています。DISPLAY DDFで見る項目はどれですか。</p><ul class="kb-choices"><li>A. LOAD utilityのRESUME指定</li><li>B. PLAN_TABLEのアクセスパス</li><li>C. row permissionの述語</li><li>D. secure SQL listenerのポート <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dを選びます。セキュアなSQLリスナー用のポートを確認すると、専用の暗号化入口が有効か判断できます。Aはユーティリティ制御です。Bは性能診断資料です。Cは行アクセス制御です。暗号化入口を分ける設計なら、通常ポートとの差も記録します；背景には安全な入口として、Db2 for z/OSのSECPORTはSSLを使うセキュアな分散要求の待ち受け番号を示します、値が未設定なら、この専用ポートでは安全な着信を受け付けません、通常ポートでSSLを使える構成とは、Db2が検証する範囲が異なりますという関係があり、この区別で確認する名称は「SECPORT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div><div class="kb-q"><p><strong>問題.</strong> 暗号化されたリモート接続のみを別の入口で受け付け、通常のDRDA受付口と分けて運用します。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. 通常DRDA受付ポート</li><li>B. SSL/TLS用の安全ポート <span class="kb-ok">✅ 正解</span></li><li>C. 再同期トランザクション用ポート</li><li>D. DBAT同時実行上限</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 暗号化接続のみを分ける入口なので、Bが該当します。Aは非セキュア側の主DRDA受付で、Cは二相コミット復旧の再同期経路です。Dは接続後に活動できるDBAT数の上限であり、ポート番号の割当ではありません；背景には安全な分散接続を受けるSECPORTは、Db2 for z/OSのDDF・分散接続パラメータとしてSSL/TLS系の接続要求に使うTCP/IPポート番号を分けます、通常ポートとは用途が異なるため、クライアント側の接続文字列やネットワーク許可と合わせて管理しますという関係があり、この区別で確認する名称は「SECPORT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECPORT</strong></p><p>検証目的: 条件照合の基本・ポートについて、SECPORT は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になりますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件照合の基本・ポートの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSECPORTを指定し、OSKB020029の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SECPORT
CASE OSKB020029
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SECPORT
CASE OSKB020029
SOURCE Db2 for z/OS
SECPORTとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020029を同じ出力で読み、条件照合の基本・ポートの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020029
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020029
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020029
DSNV401IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SECPORT と OSKB020029 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


## DDF・分散接続・ネットワーク > ネットワーク・暗号化


<section class="kb-item" id="c07-i0044"><h3>AT-TLS/SSL</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; ネットワーク・暗号化 ・ 難易度: 中級</p><p>AT-TLS/SSLは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 外部接続を暗号化する要件があり、Db2側のポートを主な根拠にしてなくTCP/IP側のポリシーも確認します。関係する仕組みはどれですか。</p><ul class="kb-choices"><li>A. SORTKEYS</li><li>B. AT-TLSまたはSSL <span class="kb-ok">✅ 正解</span></li><li>C. RUNSTATS PROFILE</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bを選びます。暗号化通信では暗号化方式であるAT-TLSやSSLの設定をDb2側とTCP/IP側で合わせて確認します。Aはユーティリティのソート関連です。Cは統計収集設定です。Dはパッケージ管理です。証明書やポリシーはDb2外の設定も含むため、担当範囲を明確にします；背景には暗号化経路として、Db2 for z/OSのDDF接続ではAT-TLSやSSLを使って通信を保護します、SECPORTの専用待ち受け、通常ポートでの暗号化、証明書設定の分担を確認し、Db2を主な根拠にしてなくTCP/IP側の設定も合わせて見ます、証明書とポートの担当範囲を分けて記録しますという関係があり、この区別で確認する名称は「AT-TLS/SSL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details></section>


<section class="kb-item" id="c07-i0045"><h3>TCP/IP hostname definition</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; ネットワーク・暗号化 ・ 難易度: 中級</p><p>TCP/IP hostname definitionは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> クライアント側の接続文字列にあるホスト名が正しいか確認しています。DDF接続でこの確認が必要になる理由はどれですか。</p><ul class="kb-choices"><li>A. パッケージ所有者を変えるため</li><li>B. ログをアーカイブするため</li><li>C. TCP/IP経路でDb2へ到達するため <span class="kb-ok">✅ 正解</span></li><li>D. 行マスクを有効化するため</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cが正解です。ホスト名はTCP/IP経路でDb2へ到達するための名前解決に関わります。AはBIND所有者の話です。Bはログ運用です。Dはデータアクセス制御です。名前解決の確認は、Db2側の表示とTCP/IP側の設定を突き合わせます；背景にはホスト名定義は、Db2 for z/OSのDDFがTCP/IP経由で到達されるための名前解決に関わります、クライアントはホスト名、ロケーション名、ポート番号を組み合わせて接続するため、DNSやVIPAの設計とDb2側の表示を突き合わせますという関係があり、この区別で確認する名称は「definition」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCP ・ IP hostname definition</strong></p><p>検証目的: 順序照合の・について、TCP/IP hostname definitionは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、順序照合の・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にTCP ・ IP hostname を指定し、OSKB020035の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND TCP ・ IP hostname 
CASE OSKB020035
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM TCP ・ IP hostname 
CASE OSKB020035
SOURCE Db2 for z/OS
TCP ・ IP hostname とOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020035を同じ出力で読み、順序照合の・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020035
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020035
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020035
DSNV401IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の TCP ・ IP hostname  と OSKB020035 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0046"><h3>secure SQL listener</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; ネットワーク・暗号化 ・ 難易度: 中級</p><p>secure SQL listenerは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 暗号化されたSQL要求のみを専用入口へ向ける設計です。通常のDRDAポートではなく、セキュアなSQL待ち受けとして確認するものはどれですか。</p><ul class="kb-choices"><li>A. 表スペースのFREEPAGE</li><li>B. SQL PLのSIGNAL文</li><li>C. 安全なSQLリスナー <span class="kb-ok">✅ 正解</span></li><li>D. RACFのDATASETプロファイル</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cが適切です。安全なSQLリスナーはセキュアな分散SQL要求の入口として確認します。Aは格納時の空き領域指定です。BはSQL PLの例外制御です。Dはデータセット保護の定義です。通常ポートとの役割差を表示結果で確認します；背景には専用の安全な待ち受けとして、Db2 for z/OSのsecure SQL listenerはセキュアな分散SQL要求を受ける入口です、値としてSECPORTが未指定なら、この専用入口では着信を受け付けません、通常ポートとの差を接続方式の設計で確認しますという関係があり、この区別で確認する名称は「listener」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>secure SQL listener</strong></p><p>検証目的: 値域照合のネットワーク・暗号化について、secure SQL listenerは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、値域照合のネットワーク・暗号化の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にsecure SQL listeneを指定し、OSKB020036の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND secure SQL listene
CASE OSKB020036
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM secure SQL listene
CASE OSKB020036
SOURCE Db2 for z/OS
secure SQL listeneとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020036を同じ出力で読み、値域照合のネットワーク・暗号化の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020036
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020036
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020036
DSNV401IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の secure SQL listene と OSKB020036 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


## DDF・分散接続・ネットワーク > ロケーション・別名


<section class="kb-item" id="c07-i0047"><h3>dynamic location alias</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; ロケーション・別名 ・ 難易度: 中級</p><p>dynamic location aliasは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 接続別名を追加した後、Db2本体を止めずに別名の開始や停止を管理したい状況です。対象になる仕組みはどれですか。</p><ul class="kb-choices"><li>A. 表スペースのLOCKSIZE</li><li>B. SQL PLの変数宣言</li><li>C. 動的に管理できる接続別名 <span class="kb-ok">✅ 正解</span></li><li>D. COPY utilityのイメージコピー</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cが正解です。動的な接続別名はMODIFY DDFで管理でき、Db2停止を伴わず状態を変えられます。Aはロック粒度です。Bはルーチン内の宣言です。Dはバックアップ取得処理です。変更前に表示結果で別名の状態を確認します；背景には動的に扱う別名として、Db2 for z/OSのdynamic location aliasは変更コマンドで開始、停止、取消、構成変更を行える接続別名です、分散機能やDb2を止めずに別名の状態を変えられるため、変更窓口と影響範囲を明確にして扱いますという関係があり、この区別で確認する名称は「dynamic」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details></section>


<section class="kb-item" id="c07-i0048"><h3>location alias</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; ロケーション・別名 ・ 難易度: 中級</p><p>location aliasは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 同じDb2グループへ接続する業務を分け、別名ごとに入口と運用状態を見たい要件があります。使う考え方はどれですか。</p><ul class="kb-choices"><li>A. ログのアクティブコピー</li><li>B. カーソルのWITH HOLD</li><li>C. カタログ表の統計行</li><li>D. ロケーションの別名 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dを選びます。ロケーションの別名を使うと、同じ接続先に別の入口や運用状態を持たせられます。Aはログ保護です。Bはカーソルの保持指定です。Cはアクセスパス判断の材料です。別名ごとの状態を表示結果で分けて確認します；背景には別名経路を使うと、Db2 for z/OSではlocation aliasで同じDb2ロケーションに別の名前や入口を持たせられます、データ共有構成やアプリケーション分離で、別名ごとにポートや運用状態を分けて確認します、別名の状態を表示で追えるようにしておきますという関係があり、この区別で確認する名称は「location」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>location alias</strong></p><p>検証目的: 優先照合のロケーション・別名について、location aliasは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、優先照合のロケーション・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にlocation aliasを指定し、OSKB020032の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND location alias
CASE OSKB020032
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM location alias
CASE OSKB020032
SOURCE Db2 for z/OS
location aliasとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020032を同じ出力で読み、優先照合のロケーション・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020032
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020032
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020032
DSNV401IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の location alias と OSKB020032 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0049"><h3>location name</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; ロケーション・別名 ・ 難易度: 中級</p><p>location nameは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> クライアント接続定義で、接続先Db2サーバーをどの名前として指定するか確認しています。分散接続でサーバーを識別する名前はどれですか。</p><ul class="kb-choices"><li>A. サーバーを表すロケーション名 <span class="kb-ok">✅ 正解</span></li><li>B. SQL文のホスト変数名</li><li>C. RACFの管理権限プロファイル</li><li>D. 表スペースのSEGSIZE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aです。ロケーション名は分散接続で接続先Db2を識別するために使います。Bはプログラム内の変数名です。Cは外部セキュリティの権限管理です。Dは表スペースの構造属性です。移行計画で重要なのは、既存クライアントが参照する名前を変えない工夫です；背景にはロケーション・別名を整理すると、Db2 for z/OSのlocation nameは分散接続で相手から見えるDb2サーバーの名前です、クライアント接続、DRDA経路、二相コミット再同期で参照されるため、移行や統合では既存名との互換性を確認しますという関係があり、この区別で確認する名称は「name」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details></section>


## DDF・分散接続・ネットワーク > 再同期・運用表示


<section class="kb-item" id="c07-i0050"><h3>DISPLAY DDF output</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; 再同期・運用表示 ・ 難易度: 中級</p><p>DISPLAY DDF outputは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 分散接続障害で、ポート番号、MAXDBAT、DDFの開始状態をまとめて証跡化したい状況です。使う表示結果はどれですか。</p><ul class="kb-choices"><li>A. EXPLAINのPLAN_TABLE</li><li>B. RACFのLISTUSER結果</li><li>C. DISPLAY DATABASEのロック一覧</li><li>D. DISPLAY DDFの結果 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dです。表示コマンドの結果にはDDF状態や各種ポート、MAXDBATなど接続入口の情報がまとまります。Aはアクセスパス資料です。Bは利用者属性の確認です。Cはデータベース資源の状態です。接続障害の一次証跡として使います；背景には運用表示の中心として、Db2 for z/OSのDISPLAY DDF outputにはDDFの開始状態、待ち受けポート、secure port、resync port、MAXDBATなどが出ます、接続不可や暗号化設定の調査では、DSNL090Iなどのメッセージを証跡として残しますという関係があり、この区別で確認する名称は「DISPLAY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details></section>


<section class="kb-item" id="c07-i0051"><h3>MODIFY DDF alias operation</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; 再同期・運用表示 ・ 難易度: 中級</p><p>MODIFY DDF alias operationは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 動的な接続別名を停止し、同じDb2グループの通常ポートは生かしたままにしたい要件があります。扱う操作はどれですか。</p><ul class="kb-choices"><li>A. MODIFY DDFでの別名操作 <span class="kb-ok">✅ 正解</span></li><li>B. RUNSTATSの統計更新</li><li>C. GRANTの権限付与</li><li>D. COPY utilityの取得</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aが該当します。変更コマンドによる別名操作は、動的ロケーション別名の開始や停止を扱います。Bは統計収集です。Cはアクセス権限です。Dはバックアップ系ユーティリティです。状態変更を伴うため、実行前に対象別名と影響範囲を確認します；背景には別名の運用操作として、Db2 for z/OSのMODIFY DDF alias operationは動的ロケーション別名の開始、停止、取消、構成変更を扱います、分散機能やDb2を止めずに別名を動かせる一方、接続影響が出るため、変更対象と状態表示を確認してから実行しますという関係があり、この区別で確認する名称は「operation」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MODIFY DDF alias operation</strong></p><p>検証目的: 警告照合の再同期・運用表示について、MODIFY DDF alias operationは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Dbに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、警告照合の再同期・運用表示の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にMODIFY DDF alias oを指定し、OSKB020037の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND MODIFY DDF alias o
CASE OSKB020037
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM MODIFY DDF alias o
CASE OSKB020037
SOURCE Db2 for z/OS
MODIFY DDF alias oとOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020037を同じ出力で読み、警告照合の再同期・運用表示の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020037
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020037
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020037
DSNV401IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の MODIFY DDF alias o と OSKB020037 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0052"><h3>two-phase commit resynchronization</h3><p class="kb-meta">分類: DDF・分散接続・ネットワーク &gt; 再同期・運用表示 ・ 難易度: 初級</p><p>two-phase commit resynchronizationは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 分散更新中の障害後、取引コーディネーターとDb2の判断をそろえ、未確定UOWを解消する必要があります。この処理はどれですか。</p><ul class="kb-choices"><li>A. アクセスパスの再計算</li><li>B. 二相コミットの再同期 <span class="kb-ok">✅ 正解</span></li><li>C. 表の再編成</li><li>D. SQLCAの初期化</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bが正解です。二相コミットの再同期は、障害後に関係するサーバー間のトランザクション状態を合わせます。Aは最適化です。Cは物理配置の整理です。Dはプログラム側の診断領域の初期化です。未確定UOWの処理では、取引の片側のみを見ても判断できません；背景には分散更新の後始末として、Db2 for z/OSのtwo-phase commit resynchronizationは障害後に取引コーディネーターと状態を合わせる処理です、再同期用にRESPORTを使い、未確定のUOWを整合させます、通常のSQL要求とは別の入口と証跡を確認しますという関係があり、この区別で確認する名称は「resynchronization」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Installation / Db2_zOS_Performance</p></div></details></section>


## DDL・データ定義 > データベース・ストレージDDL


<section class="kb-item" id="c07-i0053"><h3>CREATE DATABASE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; データベース・ストレージDDL ・ 難易度: 初級</p><p>CREATE DATABASEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。データベース・ストレージDDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 新しい業務領域の表スペースをまとめる上位単位を作ります。DBAが最初に使うデータ定義文は何ですか。</p><ul class="kb-choices"><li>A. 上位の管理単位を用意する定義文。 <span class="kb-ok">✅ 正解</span></li><li>B. 表へ列を追加する文。</li><li>C. 現行トランザクションを確定する文。</li><li>D. 分散接続の状態を表示するコマンド。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 上位のデータベース管理単位を作るためAが正しいです。この定義文は表スペースを束ねる設計単位を用意します。Bは表変更、Cは更新確定、Dは運用表示であり、データベース定義の作成ではありません。誤って表作成文を選ばないことが大切です；背景にはDb2 for z/OS のデータベース・ストレージDDLに含まれる CREATE DATABASE は、表スペースを束ねるデータベース管理単位を定義します、物理データを直接入れる器ではなく、複数の表スペースをまとめる上位の論理単位です、容量や権限の設計を始める前に位置づけを確認しますという関係があり、この区別で確認する名称は「DATABASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE DATABASE</strong></p><p>検証目的: 変更確認のデータベース・ストレージについて、CREATE DATABASE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。データベース・ストレージ DDL の作業では、対象オブジェクト、依存関係、後続に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更確認のデータベース・ストレージの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE DATABASEを指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE DATABASE
CASE OSKB010020
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE DATABASE
CASE OSKB010020
SOURCE Db2 for z/OS
CREATE DATABASEとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010020を同じ出力で読み、変更確認のデータベース・ストレージの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010020
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010020
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010020
DSNV401IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE DATABASE と OSKB010020 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0054"><h3>CREATE STOGROUP</h3><p class="kb-meta">分類: DDL・データ定義 &gt; データベース・ストレージDDL ・ 難易度: 初級</p><p>CREATE STOGROUPは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。データベース・ストレージDDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 新しい表スペースを特定のストレージ管理範囲に置きたい状況です。配置先候補を定義するDDLは何ですか。</p><ul class="kb-choices"><li>A. カーソルで結果行を順に読む文。</li><li>B. 格納先候補を管理する定義文。 <span class="kb-ok">✅ 正解</span></li><li>C. 更新前の状態へ戻す文。</li><li>D. 監査トレースの一覧を表示する文。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 格納先候補を用意するためBが該当します。この格納先定義はストレージグループを定義し、後続の表スペース配置に使います。Aは照会処理、Cは取消処理、Dはトレース表示で、配置先定義ではありません。容量配分やSMS管理との接点を見ます；背景にはDb2 for z/OS のデータベース・ストレージDDLで扱う CREATE STOGROUP は、オブジェクトの格納先候補になるストレージグループを定義します、表スペースが使う保存先を管理し、ボリュームやSMS管理との関係を整理します、単なる表定義ではなく配置設計の部品ですという関係があり、この区別で確認する名称は「STOGROUP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE STOGROUP</strong></p><p>検証目的: 構文照合のデータベース・ストレージについて、CREATE STOGROUP は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。データベース・ストレージ DDL の作業では、対象オブジェクト、依存関係、後続に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010021の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文照合のデータベース・ストレージの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE STOGROUPを指定し、OSKB010021の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE STOGROUP
CASE OSKB010021
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE STOGROUP
CASE OSKB010021
SOURCE Db2 for z/OS
CREATE STOGROUPとOSKB010021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010021を同じ出力で読み、構文照合のデータベース・ストレージの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010021
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010021
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010021
DSNV401IとOSKB010021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE STOGROUP と OSKB010021 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0055"><h3>CREATE TABLESPACE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; データベース・ストレージDDL ・ 難易度: 初級</p><p>CREATE TABLESPACEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。データベース・ストレージDDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表を置く前に、容量管理やコピー対象になる収容単位を準備します。DBAが使うDDLは何ですか。</p><ul class="kb-choices"><li>A. スレッド状態を一覧にする表示コマンド。</li><li>B. 権限を取り消すSQL。</li><li>C. データの収容単位を準備する定義文。 <span class="kb-ok">✅ 正解</span></li><li>D. ログ情報を表示するコマンド。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収容単位を準備するためCが正しいです。この記憶単位の定義は表スペースを作成し、後続の表定義や運用の単位になります。Aは処理状況表示、Bは権限操作、Dはログ運用の確認であり、データ配置の準備ではありません；背景にはデータベース・ストレージDDLの中で CREATE TABLESPACE は、表データを収容する表スペースを作成します、ページサイズ、格納先、容量の考え方が、コピー取得、再編成、回復作業の単位に影響します、表を作る前に物理配置の前提を固める操作ですという関係があり、この区別で確認する名称は「TABLESPACE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE</strong></p><p>検証目的: 展開照合のデータベース・ストレージについて、CREATE TABLESPACE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。データベース・ストレージ DDL の作業では、対象オブジェクト、依存関係、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開照合のデータベース・ストレージの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACEを指定し、OSKB010022の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE
CASE OSKB010022
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE
CASE OSKB010022
SOURCE Db2 for z/OS
CREATE TABLESPACEとOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010022を同じ出力で読み、展開照合のデータベース・ストレージの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010022
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010022
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010022
DSNV401IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE と OSKB010022 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## DDL・データ定義 > 制御オブジェクトDDL


<section class="kb-item" id="c07-i0056"><h3>CREATE TRIGGER</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 制御オブジェクトDDL ・ 難易度: 初級</p><p>CREATE TRIGGERは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。制御オブジェクトDDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 特定表への更新を契機に検査処理を動かしたい要件があります。定義するオブジェクトは何ですか。</p><ul class="kb-choices"><li>A. 一時表。</li><li>B. 接続ロケーション。</li><li>C. 監査トレース。</li><li>D. トリガー。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 更新などを契機に処理を動かすためDが正解です。このトリガー定義では発火条件と実行内容を組み合わせます。Aは作業用表、Bは接続先、Cは診断や監査の記録で、表変更に連動する処理ではありません。更新処理の副作用を見積もる必要があります；背景には表変更を契機に処理を動かす CREATE TRIGGER は、制御オブジェクトDDLとしてトリガーを定義します、対象になる INSERT、UPDATE、DELETEなどの操作に連動するため、発火条件、実行タイミング、副作用を確認します、単なる制約とは別の処理定義ですという関係があり、この区別で確認する名称は「TRIGGER」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 表の INSERT や UPDATE を契機に、指定した SQL 処理を自動実行させます。使う操作はどれですか。</p><ul class="kb-choices"><li>A. 権限剥奪</li><li>B. trigger登録 <span class="kb-ok">✅ 正解</span></li><li>C. archive表示</li><li>D. package再bind</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表操作を契機に動く処理を登録する指定であり、B に当たります。A: 権限を取り消す操作です。C: log 退避状況の確認です。D: package を再作成する運用です。実行時点と対象表を定義で明確にします；背景にはCREATE TRIGGER は、定義操作として表操作に反応して動く処理を登録します、INSERT、UPDATE、DELETE などの契機、実行時点、対象表、SQL 本体を指定します、運用では業務ロジックの隠れた実行点になるため、変更影響とデバッグ条件を確認しますという関係があり、この区別で確認する名称は「TRIGGER」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TRIGGER</strong></p><p>検証目的: 順序照合の制御オブジェクトについて、CREATE TRIGGER は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。制御オブジェクト DDL の作業では、対象オブジェクト、依存関係、後続の REBIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010035の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、順序照合の制御オブジェクトの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TRIGGERを指定し、OSKB010035の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TRIGGER
CASE OSKB010035
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TRIGGER
CASE OSKB010035
SOURCE Db2 for z/OS
CREATE TRIGGERとOSKB010035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010035を同じ出力で読み、順序照合の制御オブジェクトの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010035
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010035
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010035
DSNV401IとOSKB010035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TRIGGER と OSKB010035 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0057"><h3>CREATE TRUSTED CONTEXT</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 制御オブジェクトDDL ・ 難易度: 上級</p><p>CREATE TRUSTED CONTEXTは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。制御オブジェクトDDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 特定の接続条件に基づいてユーザーやロールの扱いを制御したい状況です。使うDDLは何ですか。</p><ul class="kb-choices"><li>A. 信頼できる接続条件を定義する文。 <span class="kb-ok">✅ 正解</span></li><li>B. 表の行を更新する文。</li><li>C. バッファプール状態を表示する文。</li><li>D. アクティブログを表示する文。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 接続条件をセキュリティ設計へ反映するためAを選びます。この接続条件の定義は信頼できる接続の条件を定義します。Bはデータ更新、Cはメモリ資源表示、Dはログ表示であり、接続条件の定義ではありません。接続元やロール条件を分けて考えます；背景には接続条件を信頼単位として扱う CREATE TRUSTED CONTEXT は、制御オブジェクトDDLとして信頼できる接続条件を定義します、接続元、ユーザー、ロールの扱いを制御するため、通常の表DDLではなくセキュリティ設計として確認します、権限付与文とは役割が異なりますという関係があり、この区別で確認する名称は「TRUSTED」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TRUSTED CONTEXT</strong></p><p>検証目的: 値域照合の制御オブジェクトについて、CREATE TRUSTED CONTEXT は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。制御オブジェクト DDL の作業では、対象オブジェクト、依存関係に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010036の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、値域照合の制御オブジェクトの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TRUSTED CONを指定し、OSKB010036の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TRUSTED CON
CASE OSKB010036
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TRUSTED CON
CASE OSKB010036
SOURCE Db2 for z/OS
CREATE TRUSTED CONとOSKB010036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010036を同じ出力で読み、値域照合の制御オブジェクトの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010036
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010036
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010036
DSNV401IとOSKB010036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TRUSTED CON と OSKB010036 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## DDL・データ定義 > 索引・ビュー・別名DDL


<section class="kb-item" id="c07-i0058"><h3>ALTER INDEX</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 索引・ビュー・別名DDL ・ 難易度: 初級</p><p>ALTER INDEXは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。索引・ビュー・別名DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 既存索引の属性を変更し、後続の性能確認に進みます。DBAが使うDDLは何ですか。</p><ul class="kb-choices"><li>A. 表定義を削除する文。</li><li>B. 索引の設定を後から調整する文。 <span class="kb-ok">✅ 正解</span></li><li>C. 更新内容を確定する文。</li><li>D. ユーティリティ状態を表示する文。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 索引の設定を調整するためBが適切です。この索引変更は既存索引の属性を調整し、アクセスパスに影響し得ます。Aは表削除、Cは確定処理、Dは運用表示で、索引属性の変更には当たりません。変更後は統計や再バインドの扱いも確認対象になります；背景には索引属性を見直す ALTER INDEX は、既存索引の設定を変更する索引・ビュー・別名DDLの索引変更文です、索引はアクセスパス、制約、再編成、統計更新と関係するため、変更前に表との関係と後続の性能確認を整理します、表データの値を直接変える文ではありませんという関係があり、この区別で確認する名称は「INDEX」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALTER INDEX</strong></p><p>検証目的: 区切照合の索引・ビュー・別名について、ALTER INDEX は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。索引・ビュー・別名 DDL の作業では、対象オブジェクト、依存関係、後続の REBINDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010030の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切照合の索引・ビュー・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にALTER INDEXを指定し、OSKB010030の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ALTER INDEX
CASE OSKB010030
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ALTER INDEX
CASE OSKB010030
SOURCE Db2 for z/OS
ALTER INDEXとOSKB010030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010030を同じ出力で読み、区切照合の索引・ビュー・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010030
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010030
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010030
DSNV401IとOSKB010030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ALTER INDEX と OSKB010030 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0059"><h3>CREATE ALIAS</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 索引・ビュー・別名DDL ・ 難易度: 初級</p><p>CREATE ALIASは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。索引・ビュー・別名DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 実体の表名を直接書かず、別の参照名でアクセスさせたい要件があります。使うDDLは何ですか。</p><ul class="kb-choices"><li>A. ログ情報を表示するコマンド。</li><li>B. 表の別名を定義する文。 <span class="kb-ok">✅ 正解</span></li><li>C. パッケージを解放する操作。</li><li>D. 行を削除する文。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 参照用の別名を作るためBが正しいです。この別名定義は実体へ到達する名前を用意します。Aはログ状態の確認、Cはパッケージ資材の解放、Dはデータ行の削除であり、オブジェクト名の別名定義ではありません。名前解決の入口を増やす点が中心です；背景には参照名を切り替える CREATE ALIAS は、表やビューなどへ別名を定義する索引・ビュー・別名DDLの別名定義です、参照名を整理できる一方、実体を複製するわけではありません、権限、基表の存在、名前解決の範囲を確認します、名前変更の影響を抑えたい場面でも利用されますという関係があり、この区別で確認する名称は「ALIAS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE ALIAS</strong></p><p>検証目的: 記録照合の索引・ビュー・別名について、CREATE ALIAS は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。索引・ビュー・別名 DDL の作業では、対象オブジェクト、依存関係、後続の REBINに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010033の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、記録照合の索引・ビュー・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE ALIASを指定し、OSKB010033の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE ALIAS
CASE OSKB010033
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE ALIAS
CASE OSKB010033
SOURCE Db2 for z/OS
CREATE ALIASとOSKB010033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010033を同じ出力で読み、記録照合の索引・ビュー・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010033
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010033
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010033
DSNV401IとOSKB010033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE ALIAS と OSKB010033 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0060"><h3>CREATE INDEX</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 索引・ビュー・別名DDL ・ 難易度: 初級</p><p>CREATE INDEXは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。索引・ビュー・別名DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE INDEX</strong></p><p>検証目的: 条件照合の索引・ビュー・別名について、CREATE INDEX は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。索引・ビュー・別名 DDL の作業では、対象オブジェクト、依存関係、後続の REBINに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010029の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件照合の索引・ビュー・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE INDEXを指定し、OSKB010029の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE INDEX
CASE OSKB010029
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE INDEX
CASE OSKB010029
SOURCE Db2 for z/OS
CREATE INDEXとOSKB010029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010029を同じ出力で読み、条件照合の索引・ビュー・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010029
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010029
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010029
DSNV401IとOSKB010029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE INDEX と OSKB010029 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0061"><h3>CREATE SEQUENCE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 索引・ビュー・別名DDL ・ 難易度: 初級</p><p>CREATE SEQUENCEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。索引・ビュー・別名DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 注文番号に使う連番を表とは別のオブジェクトとして管理したい状況です。定義するDDLは何ですか。</p><ul class="kb-choices"><li>A. トレース一覧を表示する文。</li><li>B. 表スペースを回復する文。</li><li>C. 順序オブジェクトを作成する文。 <span class="kb-ok">✅ 正解</span></li><li>D. SQL権限を取り消す文。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採番用の順序を作るためCが適切です。この順序定義は連番値をSQLから利用できるようにします。Aは表示コマンド、Bは回復処理、Dは権限操作であり、業務番号を発行する定義ではありません。キャッシュ設定や循環の有無も設計対象です；背景には索引・ビュー・別名DDL領域で扱う CREATE SEQUENCE は、連番値を生成する順序オブジェクトを用意します、主キーや業務番号に使う場合は、開始値、増分、キャッシュ、循環有無を設計します、表そのものではなく値を供給する独立した定義ですという関係があり、この区別で確認する名称は「SEQUENCE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE SEQUENCE</strong></p><p>検証目的: 比較照合の索引・ビュー・別名について、CREATE SEQUENCE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。索引・ビュー・別名 DDL の作業では、対象オブジェクト、依存関係、後続の REに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010034の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較照合の索引・ビュー・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE SEQUENCEを指定し、OSKB010034の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE SEQUENCE
CASE OSKB010034
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE SEQUENCE
CASE OSKB010034
SOURCE Db2 for z/OS
CREATE SEQUENCEとOSKB010034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010034を同じ出力で読み、比較照合の索引・ビュー・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010034
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010034
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010034
DSNV401IとOSKB010034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE SEQUENCE と OSKB010034 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0062"><h3>CREATE VIEW</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 索引・ビュー・別名DDL ・ 難易度: 初級</p><p>CREATE VIEWは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。索引・ビュー・別名DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 利用者には必要な列のみを見せ、元表を直接参照させない設計にします。使うDDLは何ですか。</p><ul class="kb-choices"><li>A. 接続数を表示するコマンド。</li><li>B. 表スペースを作る文。</li><li>C. ビューを定義する文。 <span class="kb-ok">✅ 正解</span></li><li>D. 更新を取り消す文。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 仮想的な参照先を作るためCが答えです。このビュー定義は基表をもとにビューを定義します。Aは運用表示、Bは記憶構造の定義、Dはトランザクション取消で、利用者向けの参照定義を作る文ではありません。列名や権限の見せ方を整理する目的で使います；背景には利用者に見せる形を整える CREATE VIEW は、基表や照会結果をもとにビューを定義する索引・ビュー・別名DDLのビュー定義文です、列や行の見せ方を制御できる一方、基表の変更や権限との関係も確認します、実データのコピー作成とはビュー作成の操作ではありませんという関係があり、この区別で確認する名称は「VIEW」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE VIEW</strong></p><p>検証目的: 範囲照合の索引・ビュー・別名について、CREATE VIEW は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。索引・ビュー・別名 DDL の作業では、対象オブジェクト、依存関係、後続の REBINDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010031の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、範囲照合の索引・ビュー・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE VIEWを指定し、OSKB010031の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE VIEW
CASE OSKB010031
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE VIEW
CASE OSKB010031
SOURCE Db2 for z/OS
CREATE VIEWとOSKB010031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010031を同じ出力で読み、範囲照合の索引・ビュー・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010031
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010031
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010031
DSNV401IとOSKB010031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE VIEW と OSKB010031 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0063"><h3>DROP VIEW</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 索引・ビュー・別名DDL ・ 難易度: 初級</p><p>DROP VIEWは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。索引・ビュー・別名DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 基礎表の data は残したまま、不要になった view 定義のみを削除します。使う DDL はどれですか。</p><ul class="kb-choices"><li>A. COPY</li><li>B. RECOVER</li><li>C. DISPLAY DDF</li><li>D. view削除 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> view 定義を削除する DDL なので、D が合います。A: backup 用の copy を取得する保守処理です。B: data を回復する操作です。C: 分散接続状態の表示です。依存する package と application SQL を確認します；背景には不要になった view を消す索引・ビュー・別名DDLとして、DROP VIEW は view 定義を削除します、基礎表の data を直接削除する操作ではありません、依存する package、権限、trigger、application SQL が残っていないかを事前に確認しますという関係があり、この区別で確認する名称は「DROP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.231 / Db2_zOS_Introduction.pdf p.258 / Db2_zOS_Admin_Guide.pdf p.40 / Db2_zOS_Admin_Guide.pdf p.428 / Db2_zOS_Data_Sharing.pdf p.16 / Db2_zOS_Data_Sharing.pdf p.86 / Db2_zOS_Installation.pdf p.278 / Db2_zOS_Installation.pdf p.280 / Db2_zOS_Utility_Guide.pdf p.25 / Db2_zOS_Utility_Guide.pdf p.1068 / Db2_zOS_Troubleshooting.pdf p.287 / Db2_zOS_Admin_Guide.pdf p.648</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DROP VIEW</strong></p><p>検証目的: 優先照合の索引・ビュー・別名について、DROP VIEW は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。索引・ビュー・別名 DDL の作業では、対象オブジェクト、依存関係、後続の REBIND や Rに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010032の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、優先照合の索引・ビュー・別名の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDROP VIEWを指定し、OSKB010032の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DROP VIEW
CASE OSKB010032
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DROP VIEW
CASE OSKB010032
SOURCE Db2 for z/OS
DROP VIEWとOSKB010032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010032を同じ出力で読み、優先照合の索引・ビュー・別名の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010032
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010032
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010032
DSNV401IとOSKB010032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DROP VIEW と OSKB010032 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## DDL・データ定義 > 表DDL


<section class="kb-item" id="c07-i0064"><h3>ALTER TABLE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 表DDL ・ 難易度: 初級</p><p>ALTER TABLEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。表DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 稼働中の業務表へ新しい列を追加する変更案が出ました。既存表の定義を変える文は何ですか。</p><ul class="kb-choices"><li>A. 列や制約を後から調整する文。 <span class="kb-ok">✅ 正解</span></li><li>B. 接続先ロケーションを表示するコマンド。</li><li>C. 更新を確定する文。</li><li>D. グループバッファプールを表示するコマンド。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構造を後から調整するためAが正しいです。この変更文は既存表の列や制約を変更する表DDLです。Bは分散接続の表示、Cはトランザクション確定、Dはデータ共用の表示で、表構造を変更しません。変更後は、依存するプログラムの動作確認も必要になります；背景には既存表の形を変える ALTER TABLE は、表DDLの中で列、制約、属性を変更するために使います、列追加や制約変更はアプリケーション、パッケージ、再バインドへ影響するため、利用中の処理と依存関係を確認します、単なるデータ更新とは違う構造変更ですという関係があり、この区別で確認する名称は「ALTER」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALTER TABLE</strong></p><p>検証目的: 置換照合の表について、ALTER TABLE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。表 DDL の作業では、対象オブジェクト、依存関係、後続の REBIND や RUNSTATに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010024の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換照合の表の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にALTER TABLEを指定し、OSKB010024の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ALTER TABLE
CASE OSKB010024
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ALTER TABLE
CASE OSKB010024
SOURCE Db2 for z/OS
ALTER TABLEとOSKB010024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010024を同じ出力で読み、置換照合の表の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010024
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010024
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010024
DSNV401IとOSKB010024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ALTER TABLE と OSKB010024 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0065"><h3>CREATE GLOBAL TEMPORARY TABLE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 表DDL ・ 難易度: 初級</p><p>CREATE GLOBAL TEMPORARY TABLEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。表DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アプリケーションが一時的な集計結果をセッション内で保持したいと考えています。定義に使うSQLは何ですか。</p><ul class="kb-choices"><li>A. アーカイブログ情報を表示するコマンド。</li><li>B. 既存表の列を変更する文。</li><li>C. グローバル一時表を定義する文。 <span class="kb-ok">✅ 正解</span></li><li>D. すべての更新を取り消す文。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 一時的な作業表の定義なのでCが適切です。この一時表定義はセッション内で使う中間結果の器を用意します。Aはログ表示、Bは既存表変更、Dはトランザクション取消です。作業結果を残す永続表とは寿命が違います；背景には作業用の中間結果を保持する CREATE GLOBAL TEMPORARY TABLE は、セッション単位で利用する一時表を定義する表DDLです、永続表と異なり、作業中の結果保持や処理分割に使います、通常の表削除や永続的な履歴管理と混同しないことが重要ですという関係があり、この区別で確認する名称は「TEMPORARY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE GLOBAL TEMPORARY TABLE</strong></p><p>検証目的: 探索照合の表について、CREATE GLOBAL TEMPORARY TABLE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。表 DDL の作業では、対象オブジェクト、依存関係に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010026の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索照合の表の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE GLOBAL TEMPを指定し、OSKB010026の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE GLOBAL TEMP
CASE OSKB010026
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE GLOBAL TEMP
CASE OSKB010026
SOURCE Db2 for z/OS
CREATE GLOBAL TEMPとOSKB010026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010026を同じ出力で読み、探索照合の表の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010026
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010026
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010026
DSNV401IとOSKB010026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE GLOBAL TEMP と OSKB010026 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0066"><h3>CREATE TABLE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 表DDL ・ 難易度: 初級</p><p>CREATE TABLEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。表DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 新しい取引明細を格納する表を作り、列とデータ型を定義します。この作業で使うSQLは何ですか。</p><ul class="kb-choices"><li>A. 統計を収集するユーティリティ。</li><li>B. ロック待ちを管理する機能。</li><li>C. パッケージを削除する操作。</li><li>D. 表定義を作成する文。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 列や制約を持つ表を定義するためDが適切です。この表定義は業務データの格納先を作るSQLです。Aは統計更新、Bはロック制御、Cはバインド成果物の削除で、表の作成作業とは役割が異なります。列定義を誤ると、後続の入力処理や権限設計にも影響します；背景には業務データの入れ物を定義する CREATE TABLE は、列、データ型、制約を指定して表を作る表DDLです、実際の行を投入する前に、格納先表スペース、主キー、参照制約、NULL可否を確認します、利用側から見える基本オブジェクトになりますという関係があり、この区別で確認する名称は「TABLE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLE</strong></p><p>検証目的: 呼出照合の表について、CREATE TABLE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。表 DDL の作業では、対象オブジェクト、依存関係、後続の REBIND や RUNSTAに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010023の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出照合の表の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLEを指定し、OSKB010023の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLE
CASE OSKB010023
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLE
CASE OSKB010023
SOURCE Db2 for z/OS
CREATE TABLEとOSKB010023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010023を同じ出力で読み、呼出照合の表の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010023
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010023
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010023
DSNV401IとOSKB010023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLE と OSKB010023 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0067"><h3>DROP TABLE</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 表DDL ・ 難易度: 初級</p><p>DROP TABLEは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。表DDLの作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 廃止済みの作業表を削除します。表定義そのものを取り除くSQLとして適切なのは何ですか。</p><ul class="kb-choices"><li>A. 表に行を追加する文。</li><li>B. 表定義を削除する文。 <span class="kb-ok">✅ 正解</span></li><li>C. ストレージグループを作る文。</li><li>D. 現在のトレースを表示する文。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表定義を取り除くためBが答えです。この削除文は対象表を削除するDDLで、依存関係の確認が必要です。Aは行追加、Cは格納先定義、Dは運用表示であり、表オブジェクト全体を削除する文ではありません。削除後は参照元の見直しが必要です；背景には不要になった表を取り除く DROP TABLE は、表DDLの削除操作として表定義を削除します、データ、権限、依存ビュー、アプリケーション参照に影響するため、廃止済みかどうかを確認してから実行します、行単位の削除ではなくオブジェクト単位の削除ですという関係があり、この区別で確認する名称は「DROP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DROP TABLE</strong></p><p>検証目的: 終端照合の表について、DROP TABLE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。表 DDL の作業では、対象オブジェクト、依存関係、後続の REBIND や RUNSTATSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010025の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端照合の表の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDROP TABLEを指定し、OSKB010025の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DROP TABLE
CASE OSKB010025
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DROP TABLE
CASE OSKB010025
SOURCE Db2 for z/OS
DROP TABLEとOSKB010025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010025を同じ出力で読み、終端照合の表の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010025
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010025
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010025
DSNV401IとOSKB010025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DROP TABLE と OSKB010025 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0068"><h3>clone table</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 表DDL ・ 難易度: 中級</p><p>clone tableは、DDL・データ定義の中で表DDLに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 オブジェクト定義の作成・変更・削除として扱い、データ更新処理とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 本番表を直接壊さず、入れ替えを考えた複製側の表を準備します。この設計項目は何ですか。</p><ul class="kb-choices"><li>A. 入れ替えを意識した複製表。 <span class="kb-ok">✅ 正解</span></li><li>B. 表に権限を付与する文。</li><li>C. カーソルを宣言する文。</li><li>D. DDFの受付状態表示。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 複製表を使う設計なのでAが正解です。clone tableは保守や切り替えの検討で元表との関係を見ます。Bは権限、Cは照会処理、Dは分散接続表示であり、表の入れ替えを意識した複製構成ではありません。実体を持つ表として扱う点が、単なる参照名とは違います；背景には保守時の入れ替えを考える clone table は、元表と関係を持つ複製側の表として扱う表DDL項目です、直接本番表を変更せずに準備や切り替えを考えられます、ビューや別名のような参照名ではなく、表の入れ替え設計に関係します、切り替え時の手順と戻し方を合わせて確認しますという関係があり、この区別で確認する名称は「clone」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>clone table</strong></p><p>検証目的: 出力照合の表について、clone tableは、DDL ・データ定義の中で表 DDL に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 オブジェに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010028の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力照合の表の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にclone tableを指定し、OSKB010028の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND clone table
CASE OSKB010028
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM clone table
CASE OSKB010028
SOURCE Db2 for z/OS
clone tableとOSKB010028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010028を同じ出力で読み、出力照合の表の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010028
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010028
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010028
DSNV401IとOSKB010028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の clone table と OSKB010028 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0069"><h3>temporal table</h3><p class="kb-meta">分類: DDL・データ定義 &gt; 表DDL ・ 難易度: 中級</p><p>temporal tableは、DDL・データ定義の中で表DDLに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 オブジェクト定義の作成・変更・削除として扱い、データ更新処理とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 過去時点の行状態を追える設計にしたい要件があります。時間の概念を表設計に組み込む項目は何ですか。</p><ul class="kb-choices"><li>A. 通常の接続ポート。</li><li>B. 統計収集の制御文。</li><li>C. パッケージの所有者指定。</li><li>D. 時間情報を扱う表設計。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 履歴や期間を扱う表設計なのでDを選びます。temporal tableは時間に基づく行の扱いを表現します。Aは通信設定、Bはユーティリティ指定、CはBIND属性であり、時間対応の表設計ではありません；背景には時間の概念を表に持たせる temporal table は、履歴や有効期間を扱うための表DDL設計です、過去時点の状態を参照したい要件や、期間に基づく行管理がある場合に検討します、現在値のみを保持する通常表とは、設計と確認観点が変わりますという関係があり、この区別で確認する名称は「temporal」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>temporal table</strong></p><p>検証目的: 上書照合の表について、temporal tableは、DDL ・データ定義の中で表 DDL に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 オに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010027の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書照合の表の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にtemporal tableを指定し、OSKB010027の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND temporal table
CASE OSKB010027
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM temporal table
CASE OSKB010027
SOURCE Db2 for z/OS
temporal tableとOSKB010027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010027を同じ出力で読み、上書照合の表の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010027
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010027
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010027
DSNV401IとOSKB010027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の temporal table と OSKB010027 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_AppProg_SQL_Guide</p></div></details></section>


## DML・SQL実行 > トランザクション・実行属性


<section class="kb-item" id="c07-i0070"><h3>COMMIT</h3><p class="kb-meta">分類: DML・SQL実行 &gt; トランザクション・実行属性 ・ 難易度: 初級</p><p>COMMITは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。トランザクション・実行属性では、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 一連の更新が正常終了し、他セッションからも確定済みとして扱える状態にします。ここで実行する制御はどれですか。</p><ul class="kb-choices"><li>A. 変更の確定 <span class="kb-ok">✅ 正解</span></li><li>B. 変更の取り消し</li><li>C. ログ目録の印刷</li><li>D. 索引の再構築</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 未確定変更を確定する制御なので、Aを選びます。Bは更新を取り消す制御です。CはBSDS確認の操作です。Dは壊れた索引を作り直す保守です。確定前にSQLCODEと対象件数を確認し、想定外の更新を確定しないようにします；背景には作業単位を確定するCOMMITは、Db2 for z/OSのトランザクション制御で現在の未確定変更を確定する操作です、確定後は通常のROLLBACKで戻せないため、更新件数、エラー有無、後続処理への影響を確認してから発行します、バッチでは確定点の設計も重要ですという関係があり、この区別で確認する名称は「COMMIT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details></section>


<section class="kb-item" id="c07-i0071"><h3>ROLLBACK</h3><p class="kb-meta">分類: DML・SQL実行 &gt; トランザクション・実行属性 ・ 難易度: 初級</p><p>ROLLBACKは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。トランザクション・実行属性では、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 更新途中で業務チェックが失敗し、まだ確定していない変更をなかったことにします。実行する制御として正しいものはどれですか。</p><ul class="kb-choices"><li>A. 統計収集</li><li>B. コピー統合</li><li>C. 分散接続状態表示</li><li>D. 取消し <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 未確定の作業単位を戻すため、Dが該当します。Aは統計収集です。Bはコピー世代を統合する処理です。Cは分散接続状態の表示です。取り消し範囲は直前の確定点から現在までになり、確定済み変更は別手順で扱います；背景には未確定変更を戻すROLLBACKは、Db2 for z/OSのトランザクション制御で現在の作業単位に含まれる変更を取り消す操作です、エラー検出後や業務条件不一致時に使い、どの範囲までが同じ作業単位かを理解しておく必要があります、確定済みの変更は対象外ですという関係があり、この区別で確認する名称は「ROLLBACK」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ROLLBACK</strong></p><p>検証目的: 置換追跡のトランザクション・実行属性について、ROLLBACK は、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。トランザクション・実行属性では、対象行、トランザクション境界、エラーに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換追跡のトランザクション・実行属性の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にROLLBACKを指定し、OSKB010044の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ROLLBACK
CASE OSKB010044
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ROLLBACK
CASE OSKB010044
SOURCE Db2 for z/OS
ROLLBACKとOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010044を同じ出力で読み、置換追跡のトランザクション・実行属性の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010044
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010044
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010044
DSNV401IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ROLLBACK と OSKB010044 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0072"><h3>isolation level</h3><p class="kb-meta">分類: DML・SQL実行 &gt; トランザクション・実行属性 ・ 難易度: 初級</p><p>isolation levelは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。トランザクション・実行属性では、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 同時実行中の更新をどの程度見せるか、またロック競合をどの程度許すかを設計します。調整する属性はどれですか。</p><ul class="kb-choices"><li>A. 回復用コピー</li><li>B. ホスト変数生成</li><li>C. 分離属性 <span class="kb-ok">✅ 正解</span></li><li>D. ログ管理名</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 読み取り整合性と同時実行性を調整するため、Cが正解です。Aは回復用コピーです。Bはホスト変数宣言の生成に使います。Dはログ管理資材のデータセット名です。高い分離は整合性を強める一方で待ちを増やすため、用途に合わせて選びます；背景には同時実行の分離レベルは、Db2 for z/OSで読み取り中のデータが他トランザクションの更新とどう隔離されるかを決める実行属性です、整合性、ロック待ち、同時実行性のバランスを左右するため、業務要件に合わせて選びます、検索系と更新系で選択が変わりますという関係があり、この区別で確認する名称は「isolation」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details></section>


## DML・SQL実行 > 動的SQL・エラー処理


<section class="kb-item" id="c07-i0073"><h3>SQL error handling</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 動的SQL・エラー処理 ・ 難易度: 中級</p><p>SQL error handlingは、DML・SQL実行の中で動的SQL・エラー処理に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 データ参照・更新の実行として扱い、表定義やアクセスパス管理とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> SQL実行後にSQLCODEを確認し、処理続行、取り消し、再試行、エラー通知のどれに進むかを決めます。この実装上の関心はどれですか。</p><ul class="kb-choices"><li>A. 表スペースのCOPY</li><li>B. エラー処理 <span class="kb-ok">✅ 正解</span></li><li>C. DDFロケーション設定</li><li>D. 索引ページサイズ</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> SQL結果に応じて後続動作を決めるため、Bが該当します。Aは回復用コピーの取得です。Cは分散接続の識別情報です。Dは物理設計の属性です。エラー時は作業単位を確定するか戻すか、利用者へどの情報を返すかも判断します；背景には実行後のエラー処理は、Db2 for z/OSのSQLCODE、SQLSTATE、診断情報を読み、COMMIT、ROLLBACK、再試行、利用者通知などの後続動作を決める実装上の処理です、単に異常終了させるを主な根拠にしてなく、作業単位をどう扱うかを含めて設計しますという関係があり、この区別で確認する名称は「handling」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SQL error handling</strong></p><p>検証目的: 終端追跡の動的 ・エラー処理について、SQL error handlingは、DML ・ SQL 実行の中で動的 SQL ・エラー処理に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端追跡の動的 ・エラー処理の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSQL error handlingを指定し、OSKB010045の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SQL error handling
CASE OSKB010045
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SQL error handling
CASE OSKB010045
SOURCE Db2 for z/OS
SQL error handlingとOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010045を同じ出力で読み、終端追跡の動的 ・エラー処理の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010045
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010045
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010045
DSNV401IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SQL error handling と OSKB010045 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0074"><h3>dynamic PREPARE</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 動的SQL・エラー処理 ・ 難易度: 中級</p><p>dynamic PREPAREは、DML・SQL実行の中で動的SQL・エラー処理に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 データ参照・更新の実行として扱い、表定義やアクセスパス管理とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 画面条件に応じてSQL文字列を組み立て、実行前にDb2へ解析させてから実行します。この準備段階に当たるものはどれですか。</p><ul class="kb-choices"><li>A. PREPARE <span class="kb-ok">✅ 正解</span></li><li>B. 表スペース停止操作</li><li>C. ログの二重化</li><li>D. カタログ回復</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 実行時SQLを解析して準備する段階なので、Aが正解です。Bはデータベースオブジェクトの利用制御です。Cはログ資材の可用性対策です。Dはシステム表群を戻す回復作業です。準備後のSQLCODEを見て実行可否を判断します；背景には動的SQLで使うdynamic PREPAREは、Db2 for z/OSで実行時に組み立てたSQL文を解析し、実行可能な形へ準備する操作です、可変条件のSQLを扱うアプリケーションでは、PREPARE後のSQLCODEや再利用方針を確認しますという関係があり、この区別で確認する名称は「dynamic」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details></section>


## DML・SQL実行 > 更新SQL


<section class="kb-item" id="c07-i0075"><h3>DELETE</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 更新SQL ・ 難易度: 初級</p><p>DELETEは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。更新SQLでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 退職済み社員のみを社員表から消すため、対象条件を付けて行を削除します。選ぶSQL文として最も合うものはどれですか。</p><ul class="kb-choices"><li>A. 行削除のDML <span class="kb-ok">✅ 正解</span></li><li>B. 統計収集の指示</li><li>C. 表スペースの再編成</li><li>D. ログマップ印刷</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件に合う行を削除するため、Aが正解です。BはRUNSTATSの領域で、行を消す文ではありません。CはREORGで物理配置を整える処理です。DはBSDSの内容確認に使う運用作業です。削除後はCOMMIT前に対象件数を確認します；背景には行削除の更新SQLであるDELETEは、Db2 for z/OSの表から条件に合う行を削除するデータ変更文です、WHERE句を省略すると対象表の行を広く削除する危険があるため、実務では対象条件、参照制約、トランザクション範囲を確認してから実行しますという関係があり、この区別で確認する名称は「DELETE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details></section>


<section class="kb-item" id="c07-i0076"><h3>INSERT</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 更新SQL ・ 難易度: 初級</p><p>INSERTは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。更新SQLでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 注文受付後に、注文表へ新しい1行を登録します。使うSQL文は何ですか。</p><ul class="kb-choices"><li>A. 更新を取り消す文。</li><li>B. 索引を変更する文。</li><li>C. 表へ新しい行を追加する文。 <span class="kb-ok">✅ 正解</span></li><li>D. ロック管理機能を表示する文。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 新規行を追加するためCが答えです。この登録文は表に行を入れる更新SQLです。Aは取消、Bは索引定義の変更、Dはロック調査に関する運用確認であり、業務データを登録する文ではありません。行を追加した後も、COMMITするまでは取り消しの余地が残ります；背景には新しい行を登録する INSERT は、DML・SQL実行の更新SQLとして表へ行を追加します、列リスト、値の型、NOT NULL制約、参照制約が成功可否に関係します、COMMITされるまではトランザクションの一部なので、エラー時の戻し方も確認しますという関係があり、この区別で確認する名称は「INSERT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INSERT</strong></p><p>検証目的: 変更照合の更新について、INSERT は、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。更新 SQL では、対象行、トランザクション境界、エラー時に戻せる範囲を意識に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更照合の更新の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にINSERTを指定し、OSKB010040の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND INSERT
CASE OSKB010040
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM INSERT
CASE OSKB010040
SOURCE Db2 for z/OS
INSERTとOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010040を同じ出力で読み、変更照合の更新の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010040
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010040
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010040
DSNV401IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の INSERT と OSKB010040 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0077"><h3>INSTEAD OF triggerによる更新</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 更新SQL ・ 難易度: 中級</p><p>INSTEAD OF triggerによる更新は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複数表を結合したビューに対する更新を、どの基表へどう反映するか明示したい場面です。用意する仕組みはどれですか。</p><ul class="kb-choices"><li>A. 索引圧縮</li><li>B. 代替トリガー <span class="kb-ok">✅ 正解</span></li><li>C. BSDS二重化構成</li><li>D. 統計プロファイル</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ビュー更新時の代替処理を定義するため、Bが正解です。Aは索引の物理設計です。Cはログ管理資材の可用性対策です。DはRUNSTATSの実行内容を保存します。複雑なビューでは基表操作を明示することが重要です；背景には代替実行トリガーによる更新は、Db2 for z/OSでビューにINSERT、UPDATE、DELETEが来たとき、代わりに実行する基表操作を定義する仕組みです、この仕組みはINSTEAD OF triggerとして定義し、複数表ビューや導出列を含むビューでも更新の実体を明示できますという関係があり、この区別で確認する名称は「INSTEAD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INSTEAD OF triggerによる更新</strong></p><p>検証目的: 呼出追跡のよる更新について、INSTEAD OF triggerによる更新は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出追跡のよる更新の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にINSTEAD OF triggerを指定し、OSKB010043の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND INSTEAD OF trigger
CASE OSKB010043
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM INSTEAD OF trigger
CASE OSKB010043
SOURCE Db2 for z/OS
INSTEAD OF triggerとOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010043を同じ出力で読み、呼出追跡のよる更新の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010043
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010043
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010043
DSNV401IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の INSTEAD OF trigger と OSKB010043 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0078"><h3>MERGE</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 更新SQL ・ 難易度: 初級</p><p>MERGEは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。更新SQLでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 外部から届いた顧客差分を反映し、既存顧客なら更新、新規顧客なら追加したい場面です。ひとつの文で分岐させる候補はどれですか。</p><ul class="kb-choices"><li>A. 作業単位の確定</li><li>B. BSDS印刷結果</li><li>C. MERGE <span class="kb-ok">✅ 正解</span></li><li>D. アクセスパス説明</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 一致条件で更新と追加を分けるため、Cを選びます。Aは作業単位を確定する制御です。Bはログ管理資材の印刷確認に使います。Dはアクセスパスを見る機能です。照合キーが不明確だと意図しない行を更新するため、投入前の件数照合が欠かせません；背景には更新SQLのMERGEは、入力行が既存行に一致するかどうかでUPDATEやINSERTなどの処理を分岐する文として扱います、日次連携や差分反映では、照合条件を誤ると更新と追加の境界が崩れるため、キー項目と重複条件を事前に確認します、大量反映では事前件数の突き合わせも重要ですという関係があり、この区別で確認する名称は「MERGE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MERGE</strong></p><p>検証目的: 展開追跡の更新について、MERGE は、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。更新 SQL では、対象行、トランザクション境界、エラー時に戻せる範囲を意識しに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開追跡の更新の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にMERGEを指定し、OSKB010042の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND MERGE
CASE OSKB010042
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM MERGE
CASE OSKB010042
SOURCE Db2 for z/OS
MERGEとOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010042を同じ出力で読み、展開追跡の更新の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010042
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010042
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010042
DSNV401IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の MERGE と OSKB010042 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0079"><h3>UPDATE</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 更新SQL ・ 難易度: 初級</p><p>UPDATEは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。更新SQLでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 顧客表の住所列のみを条件に合う行で変更します。使うSQL文は何ですか。</p><ul class="kb-choices"><li>A. 既存行の値を変更する文。 <span class="kb-ok">✅ 正解</span></li><li>B. 表定義を作成する文。</li><li>C. アクティブログを表示するコマンド。</li><li>D. ビューを削除する文。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 既存行の列値を変えるためAが適切です。この更新文は条件に合う行を更新する文です。Bは定義作成、Cはログ表示、Dはビュー定義の削除であり、保存済みデータの値変更には該当しません。変更対象の絞り込みを誤ると、想定外の行まで変わります；背景には既存行を変更する UPDATE は、DML・SQL実行の更新SQLとして条件に合う行の列値を変えます、WHERE条件を誤ると影響行が広がるため、対象範囲とロック影響を確認します、必要に応じてトランザクション単位で戻せるようにします、大量更新では、事前の件数確認が事故防止になりますという関係があり、この区別で確認する名称は「UPDATE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPDATE</strong></p><p>検証目的: 構文追跡の更新について、UPDATE は、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。更新 SQL では、対象行、トランザクション境界、エラー時に戻せる範囲を意識に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010041の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文追跡の更新の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にUPDATEを指定し、OSKB010041の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND UPDATE
CASE OSKB010041
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM UPDATE
CASE OSKB010041
SOURCE Db2 for z/OS
UPDATEとOSKB010041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010041を同じ出力で読み、構文追跡の更新の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010041
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010041
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010041
DSNV401IとOSKB010041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の UPDATE と OSKB010041 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>UPDATE</strong></p><p>検証目的: 構文記録のオプションについて、UPDATE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020121の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文記録のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にUPDATEを指定し、OSKB020121の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND UPDATE
CASE OSKB020121
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM UPDATE
CASE OSKB020121
SOURCE Db2 for z/OS
UPDATEとOSKB020121が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020121を同じ出力で読み、構文記録のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020121
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020121
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020121
DSNV401IとOSKB020121が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の UPDATE と OSKB020121 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020121 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide p.810</p></div></details></section>


<section class="kb-item" id="c07-i0080"><h3>view update</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 更新SQL ・ 難易度: 中級</p><p>view updateは、DML・SQL実行の中で更新SQLに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 データ参照・更新の実行として扱い、表定義やアクセスパス管理とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 基表ではなくビューへ更新SQLを発行する設計です。運用前に特に確認すべき観点はどれでしょうか。</p><ul class="kb-choices"><li>A. ログ保持世代</li><li>B. DDF受付ポート</li><li>C. バッファ容量</li><li>D. ビュー更新可否 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ビュー経由で基表更新できるかを確認するため、Dを選びます。Aは回復資材の保持に関わります。Bは分散接続の受付設定です。Cはバッファプールの容量設定です。結合や集約を含むビューでは追加定義が必要になる場合があり、基表への反映経路を事前に確認します；背景には更新SQLのビュー更新は、Db2 for z/OSでビューを通じて基表へINSERT、UPDATE、DELETEを反映する考え方です、単純なビューではDb2が基表操作へ変換できます、結合ビューなど複雑な定義では、更新可否やトリガーの有無を確認しますという関係があり、この区別で確認する名称は「update」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Codes / Db2_zOS_ODBC</p></div></details></section>


## DML・SQL実行 > 照会・カーソル


<section class="kb-item" id="c07-i0081"><h3>SELECT</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 照会・カーソル ・ 難易度: 初級</p><p>SELECTは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。照会・カーソルでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 顧客表から条件に合う行のみを読み取り、画面に表示します。使うSQL文は何ですか。</p><ul class="kb-choices"><li>A. 表を削除する文。</li><li>B. 権限を付与する文。</li><li>C. 行と列を読み取る照会文。 <span class="kb-ok">✅ 正解</span></li><li>D. トレースを停止するコマンド。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 行と列を読み取る照会なのでCが正しいです。この照会文は表やビューから結果を返す文です。Aは定義削除、Bは権限付与、Dは運用コマンドであり、業務データを読み取るSQLではありません。読み取りを主な根拠にしても、条件指定の誤りは性能問題につながります；背景には照会処理の基本となる SELECT は、DML・SQL実行で表やビューから条件に合う行と列を取り出す文です、条件指定の WHERE、結合、集約、並び順は結果と性能に影響します、取得目的、索引、権限を合わせて確認することで、余計な全件読みを避けられますという関係があり、この区別で確認する名称は「SELECT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SELECT</strong></p><p>検証目的: 警告照合の照会・カーソルについて、SELECT は、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。照会・カーソルでは、対象行、トランザクション境界、エラー時に戻せる範囲をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010037の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、警告照合の照会・カーソルの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSELECTを指定し、OSKB010037の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SELECT
CASE OSKB010037
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SELECT
CASE OSKB010037
SOURCE Db2 for z/OS
SELECTとOSKB010037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010037を同じ出力で読み、警告照合の照会・カーソルの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010037
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010037
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010037
DSNV401IとOSKB010037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SELECT と OSKB010037 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0082"><h3>cursor</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 照会・カーソル ・ 難易度: 初級</p><p>cursorは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。照会・カーソルでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 大量の照会結果をアプリケーションで1行ずつ取り出します。この処理で使う概念は何ですか。</p><ul class="kb-choices"><li>A. 行単位で結果を取り出すカーソル。 <span class="kb-ok">✅ 正解</span></li><li>B. 表を物理的に収容する表スペース。</li><li>C. データベースを削除するDDL。</li><li>D. DDFの接続レポート。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 行単位で結果を扱うためAが正しいです。cursorはOPENやFETCHを通じて結果セットを処理します。Bは記憶単位、Cは定義削除、Dは分散接続の表示であり、照会結果を逐次取得する仕組みではありません；背景には結果を逐次処理する cursor は、DML・SQL実行でSELECT結果を行単位に取り出す制御手段です、プログラム側では宣言、OPEN、FETCH、CLOSEの流れを意識します、カーソルを COMMIT 後も保持するかどうかで、処理設計とエラー時の動きが変わりますという関係があり、この区別で確認する名称は「cursor」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cursor</strong></p><p>検証目的: 監査照合の照会・カーソルについて、cursorは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。照会・カーソルでは、対象行、トランザクション境界、エラー時に戻せる範囲をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010039の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、監査照合の照会・カーソルの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にcursorを指定し、OSKB010039の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND cursor
CASE OSKB010039
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM cursor
CASE OSKB010039
SOURCE Db2 for z/OS
cursorとOSKB010039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010039を同じ出力で読み、監査照合の照会・カーソルの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010039
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010039
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010039
DSNV401IとOSKB010039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の cursor と OSKB010039 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


<section class="kb-item" id="c07-i0083"><h3>fullselect</h3><p class="kb-meta">分類: DML・SQL実行 &gt; 照会・カーソル ・ 難易度: 初級</p><p>fullselectは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。照会・カーソルでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> UNIONを含む複数の照会結果を一つの結果として扱います。この照会全体を表す項目は何ですか。</p><ul class="kb-choices"><li>A. ストレージグループ。</li><li>B. 集合演算を含む照会全体。 <span class="kb-ok">✅ 正解</span></li><li>C. アーカイブログ。</li><li>D. グループバッファプール。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 照会全体の構造を示すためBが該当します。fullselectは集合演算や副照会を含む指定を表します。Aは配置先、Cは回復用ログ、Dはデータ共用のメモリ構造で、結果セットを作る照会指定ではありません。単純な表名やログ名ではなく、照会式全体を指す点が重要です；背景には複数の照会をまとめる fullselect は、DML・SQL実行で集合演算や副照会を含むSELECT全体を表します、複数照会を結ぶ UNION や複合的な副照会を使う場合、単純なSELECT句を主な根拠にしてなく、結果列、重複、並び順の扱いを確認します、複雑な照会では、どの部分が最終結果を作るかを確認しますという関係があり、この区別で確認する名称は「fullselect」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fullselect</strong></p><p>検証目的: 復旧照合の照会・カーソルについて、fullselectは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。照会・カーソルでは、対象行、トランザクション境界、エラー時に戻せに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010038の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、復旧照合の照会・カーソルの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にfullselectを指定し、OSKB010038の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND fullselect
CASE OSKB010038
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM fullselect
CASE OSKB010038
SOURCE Db2 for z/OS
fullselectとOSKB010038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010038を同じ出力で読み、復旧照合の照会・カーソルの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010038
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010038
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010038
DSNV401IとOSKB010038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の fullselect と OSKB010038 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div></details></section>


## Data Sharing・Sysplex連携 > Coupling Facility構造


<section class="kb-item" id="c07-i0084"><h3>GBP dependency</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; Coupling Facility構造 ・ 難易度: 中級</p><p>GBP dependencyは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ある表スペースを複数メンバーが開いた後、更新ページの整合性をCF上の共有バッファで維持する状態になりました。この状態を表す説明はどれですか。</p><ul class="kb-choices"><li>A. BIND時にVALIDATE(RUN)を指定した状態</li><li>B. 監査ポリシーが自動開始する状態</li><li>C. GBPを使う依存関係がある状態 <span class="kb-ok">✅ 正解</span></li><li>D. DDFのSQLポートが閉じた状態</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cが適切です。共有バッファへの依存になると、共有バッファ、無効化、castoutを通じてメンバー間のページ整合性を守ります。Aはパッケージ作成時の検査時期です。Bは監査の開始条件です。Dは分散接続の状態です。単なるバッファプール割り当てではなく、共有更新の有無が依存関係を左右します；背景にはCoupling Facility構造を使う依存関係として、GBP dependencyはページセットやパーティションが共有バッファの整合性制御を受ける状態です、メンバー間のread/write interestがある間は、変更ページ、無効化、castoutの動きをまとめて確認しますという関係があり、この区別で確認する名称は「dependency」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>GBP dependency</strong></p><p>検証目的: 変更整理の構について、GBP dependencyは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF 構造、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010120の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更整理の構の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にGBP dependencyを指定し、OSKB010120の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND GBP dependency
CASE OSKB010120
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM GBP dependency
CASE OSKB010120
SOURCE Db2 for z/OS
GBP dependencyとOSKB010120が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010120を同じ出力で読み、変更整理の構の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010120
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010120
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010120
DSNV401IとOSKB010120が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の GBP dependency と OSKB010120 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010120 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0085"><h3>SCA</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; Coupling Facility構造 ・ 難易度: 中級</p><p>SCAは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Data Sharingグループの制御情報をCF上で共有し、メンバー状態や回復判断に使う構造を確認しています。対象はどれですか。</p><ul class="kb-choices"><li>A. Shared Communications Area <span class="kb-ok">✅ 正解</span></li><li>B. SQLCA</li><li>C. storage group</li><li>D. column mask</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aが正解です。共有制御でSCAはグループ全体の制御情報を保持するCF構造です。BはアプリケーションのSQL診断領域です。Cはデータセット配置の管理単位です。Dは列値の表示制御です。障害時はSCAが使えるかどうかで、グループ全体の復旧判断が変わります；背景には共有制御情報を置くCoupling Facility構造として、SCAはData Sharingグループ全体の状態を支えます、メンバー状態や回復に関わる制御情報を保持します、構造の定義、サイズ、再構築可否を導入前に確認することで、障害時の判断が速くなりますという関係があり、この区別で確認する名称は「SCA」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SCA</strong></p><p>検証目的: 復旧整理の構について、SCA は、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF 構造、グループ・バッファー・に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010118の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、復旧整理の構の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSCAを指定し、OSKB010118の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SCA
CASE OSKB010118
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SCA
CASE OSKB010118
SOURCE Db2 for z/OS
SCAとOSKB010118が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010118を同じ出力で読み、復旧整理の構の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010118
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010118
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010118
DSNV401IとOSKB010118が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SCA と OSKB010118 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010118 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0086"><h3>group buffer pool</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; Coupling Facility構造 ・ 難易度: 中級</p><p>group buffer poolは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> カタログ表スペースがBP0を使い、複数メンバーから参照・更新されます。CF上に対応する共有キャッシュ構造を定義する場合、確認対象はどれですか。</p><ul class="kb-choices"><li>A. DSNDB01のディレクトリ表</li><li>B. GBP0などの共有バッファ <span class="kb-ok">✅ 正解</span></li><li>C. SQLSTATEの分類表</li><li>D. SECADM権限の保有者</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bです。ローカル側のBP0などのローカルバッファプールに対応して、GBP0などのCF上キャッシュを使います。AはDb2内部資材です。CはSQL診断コードです。Dはセキュリティ管理者の権限確認です。GBPの接続状態が不明なままでは、共有ページの整合性調査を始められません；背景にはローカルバッファプールと対応するCoupling Facility構造として、group buffer poolは共有キャッシュを提供します、BP0にはGBP0のように対応させ、カタログや業務表スペースの変更ページをメンバー間で整合させます、表示コマンドで接続メンバーを確認しますという関係があり、この区別で確認する名称は「buffer」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0087"><h3>lock structure</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; Coupling Facility構造 ・ 難易度: 中級</p><p>lock structureは、Data Sharing・Sysplex連携の中でCoupling Facility構造に関わるDb2技術項目です。Db2共有資源としての役割、メンバー間影響、CF構造との関係。一方で、XCF/GRS/CF一般論、Sysplex全体設計の詳細。 Db2 data sharing固有の共有資源として扱い、Sysplex/XCF/GRS/CF一般論とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複数メンバーから同じページセットへ更新が入り、メンバー間のロック競合が発生しています。CF上でこのロック情報を扱う構造はどれですか。</p><ul class="kb-choices"><li>A. active log</li><li>B. DSNZPARM</li><li>C. package list</li><li>D. CF上のロック管理領域 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dを選びます。lock structureはData Sharingのグローバルロック要求を扱うCF構造です。Aは更新ログ資材です。Bはサブシステムパラメータです。Cは実行時に使うパッケージ探索順序です。メンバー間ロックを調べる際は、ローカル待ちとグローバル待ちを分けて記録します；背景にはCoupling Facility構造の中で、lock structureはメンバー間のグローバルロック要求を扱う領域です、共有データへの更新や参照が競合すると、各メンバーの要求はこの構造を通じて調整されます、性能調査では競合率と待ち時間を合わせて見ますという関係があり、この区別で確認する名称は「lock」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lock structure</strong></p><p>検証目的: 監査整理の構について、lock structureは、Data Sharing・ Sysplex連携の中で Coupling Facility構造に関わる Db2技術項目です。Db2共有資源としての役に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010119の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、監査整理の構の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にlock structureを指定し、OSKB010119の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND lock structure
CASE OSKB010119
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM lock structure
CASE OSKB010119
SOURCE Db2 for z/OS
lock structureとOSKB010119が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010119を同じ出力で読み、監査整理の構の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010119
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010119
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010119
DSNV401IとOSKB010119が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の lock structure と OSKB010119 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010119 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


## Data Sharing・Sysplex連携 > グループ・メンバー


<section class="kb-item" id="c07-i0088"><h3>Db2 member</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; グループ・メンバー ・ 難易度: 中級</p><p>Db2 memberは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 共有構成の障害報告で、DBD1のみ停止しDBD2は処理を継続していると記録されています。このDBD1のように、グループを構成する個別のDb2を何として扱いますか。</p><ul class="kb-choices"><li>A. group buffer pool</li><li>B. row permission</li><li>C. Db2 member <span class="kb-ok">✅ 正解</span></li><li>D. audit policy</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cを選びます。DBD1やDBD2のような個別サブシステムはメンバーとして扱い、状態や再始動を個別に確認します。AはCF上のキャッシュ構造です。Bは行アクセス制御です。Dは監査対象を定義する仕組みです。障害報告ではなく、どのメンバーが停止したかと、他メンバーが処理を継続しているかを分けて記録します；背景には個別サブシステムを示すDb2 memberは、Data Sharingグループを構成する単位です、各メンバーは固有の状態、ログ、ローカル資源を持ちます、一方で共有データへアクセスするときはCF構造を通じて整合性を保ちます、停止時は他メンバーとの関係を確認しますという関係があり、この区別で確認する名称は「member」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Db2 member</strong></p><p>検証目的: 値域整理のグループ・メンバーについて、Db2 memberは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF 構造、グループに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010116の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、値域整理のグループ・メンバーの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDb2 memberを指定し、OSKB010116の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND Db2 member
CASE OSKB010116
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM Db2 member
CASE OSKB010116
SOURCE Db2 for z/OS
Db2 memberとOSKB010116が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010116を同じ出力で読み、値域整理のグループ・メンバーの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010116
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010116
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010116
DSNV401IとOSKB010116が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の Db2 member と OSKB010116 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010116 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0089"><h3>LRSN in data sharing</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; グループ・メンバー ・ 難易度: 中級</p><p>LRSN in data sharingは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複数メンバーで同じデータを更新した後、障害時の回復順序をグループ全体でそろえて判断する必要があります。この判断で中心になる値はどれですか。</p><ul class="kb-choices"><li>A. PLAN_TABLEのCOST値</li><li>B. RACFのクラス名</li><li>C. SPUFIの出力データセット名</li><li>D. ログ順序を示すLRSN <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dです。複数メンバー間の更新順序を扱うため、LRSNを回復や整合性判断で使います。Aはアクセスパス評価です。Bは外部セキュリティの分類です。Cは対話SQLの出力先です。回復判断では、メンバーごとのログを主な根拠にしてなくグループ全体の順序を読む必要があります；背景には更新順序の判断でLRSNを使うと、グループ・メンバー間のログ時系列をそろえられます、複数メンバーが同じデータを更新するため、単独メンバーのRBAを主な根拠にしては全体の順序を表せません、ログ調査ではLRSNの前後関係を追います、障害解析では対象メンバーをまたいで比較しますという関係があり、この区別で確認する名称は「LRSN」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LRSN in data sharing</strong></p><p>検証目的: 警告整理のグループ・メンバーについて、LRSN in data sharingは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010117の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、警告整理のグループ・メンバーの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にLRSN in data shariを指定し、OSKB010117の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND LRSN in data shari
CASE OSKB010117
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM LRSN in data shari
CASE OSKB010117
SOURCE Db2 for z/OS
LRSN in data shariとOSKB010117が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010117を同じ出力で読み、警告整理のグループ・メンバーの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010117
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010117
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010117
DSNV401IとOSKB010117が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の LRSN in data shari と OSKB010117 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010117 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0090"><h3>data sharing group</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; グループ・メンバー ・ 難易度: 中級</p><p>data sharing groupは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 可用性を高めるため、複数のDb2サブシステムから同じ表スペースを使わせる構成を検討しています。設計資料でまず確認すべき構成単位はどれですか。</p><ul class="kb-choices"><li>A. アプリケーションのSQL集合</li><li>B. 共有データを扱うDb2メンバーの集合 <span class="kb-ok">✅ 正解</span></li><li>C. 単一メンバー内のローカルバッファ</li><li>D. JCLの実行クラス定義</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解はBです。共有データを扱う複数メンバーの集合として設計し、CF上の構造と合わせて管理します。Aはパッケージやプラン側の話です。Cは一つのメンバー内の資源です。DはJES側の分類であり、Db2共有構成を表しません。設計時はメンバー名を主な根拠にしてなく、グループ名とCF構造の対応も確認します；背景には複数メンバーを一つのグループ・メンバー構成として整理すると、data sharing groupは共有データへアクセスする単位になります、Db2 for z/OSではSCA、lock structure、group buffer poolを組み合わせ、単独Db2より障害時の確認点が増えます、接続名とメンバー状態を合わせて確認しますという関係があり、この区別で確認する名称は「sharing」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0091"><h3>group attach</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; グループ・メンバー ・ 難易度: 中級</p><p>group attachは、Data Sharing・Sysplex連携の中でグループ・メンバーに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2 data sharing固有の共有資源として扱い、Sysplex/XCF/GRS/CF一般論とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 新規メンバー追加後も、既存アプリケーションの接続指定を個別サブシステム名へ固定したくありません。接続先をグループ名で扱うために使う仕組みはどれですか。</p><ul class="kb-choices"><li>A. グループ名による接続 <span class="kb-ok">✅ 正解</span></li><li>B. 監査ポリシーの自動開始</li><li>C. 表スペースのLOCKMAX</li><li>D. ログアーカイブの二重化</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aが該当します。グループ名による接続により、アプリケーションは特定メンバーを直接名指しせずに接続できます。Bは監査の開始条件です。Cはロック数制御です。Dは回復資材の保護です。導入確認ではなく、接続先の名前がメンバー固有名なのかグループ名なのかを区別します；背景には接続名の設計でgroup attachを使うと、アプリケーションは個別メンバー名ではなくグループ名でDb2へ接続できます、共有グループのメンバー追加や停止時でも、接続先を特定メンバーに固定しない構成を取りやすくなります、導入時は名前登録と到達性を確認しますという関係があり、この区別で確認する名称は「attach」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details></section>


## Data Sharing・Sysplex連携 > 共有ロック・競合


<section class="kb-item" id="c07-i0092"><h3>L-lock</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 共有ロック・競合 ・ 難易度: 中級</p><p>L-lockは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 更新SQL同士の待ちを調べる際、業務トランザクションが保持する通常のロックと、ページセット単位の物理ロックを分けて見ています。前者を示すものはどれですか。</p><ul class="kb-choices"><li>A. castout処理</li><li>B. group attach名</li><li>C. DSNUTILBのTEMPLATE</li><li>D. L-lock <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dです。論理ロックであるL-lockは業務トランザクションの論理的なロックを示します。AはGBPからディスクへページを書き出す処理です。Bは接続先指定です。Cはユーティリティのデータセット割り当て支援です。同じロックという語でも、業務トランザクションの待ちとCF構造側の制御は分けて説明します；背景には論理ロックのL-lockは、共有ロック・競合を読むときにアプリケーション処理が保持する通常のロックとして扱います、行やページへの排他を示すため、ページセット単位のP-lockとは分けて調べます、待ち時間の原因を業務処理側へ戻すときに確認しますという関係があり、この区別で確認する名称は「L-lock」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>L-lock</strong></p><p>検証目的: 展開確認の共有ロック・競合について、L-lockは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF 構造、グループ・バッフに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020002の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開確認の共有ロック・競合の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にL-lockを指定し、OSKB020002の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND L-lock
CASE OSKB020002
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM L-lock
CASE OSKB020002
SOURCE Db2 for z/OS
L-lockとOSKB020002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020002を同じ出力で読み、展開確認の共有ロック・競合の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020002
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020002
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020002
DSNV401IとOSKB020002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の L-lock と OSKB020002 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0093"><h3>P-lock</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 共有ロック・競合 ・ 難易度: 中級</p><p>P-lockは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ページセットをメンバー間で共有しており、どのメンバーがそのページセットへ関心を持つかを追跡しています。Data Sharing固有の物理ロックとして見るものはどれですか。</p><ul class="kb-choices"><li>A. P-lock <span class="kb-ok">✅ 正解</span></li><li>B. SQLCODE</li><li>C. role</li><li>D. archive log command</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aが正解です。物理ロックであるP-lockはページセットやパーティションへのメンバーの関心を扱う物理ロックです。BはSQLの結果コードです。Cは権限をまとめるセキュリティ要素です。Dはログ資材の運用コマンドです。P-lockを見ることで、どのメンバーがページセットに関心を持つかを調査できます；背景には物理ロックのP-lockは、共有ロック・競合の調査でページセットやパーティションに対するメンバーの関心を示します、業務SQLが保持する行ロックとは用途が異なります、共有構成でinter-Db2 interestを追跡するために使われます、待ちの原因を分けて判断しますという関係があり、この区別で確認する名称は「P-lock」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P-lock</strong></p><p>検証目的: 構文確認の共有ロック・競合について、P-lockは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF 構造、グループ・バッフに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020001の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文確認の共有ロック・競合の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にP-lockを指定し、OSKB020001の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND P-lock
CASE OSKB020001
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM P-lock
CASE OSKB020001
SOURCE Db2 for z/OS
P-lockとOSKB020001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020001を同じ出力で読み、構文確認の共有ロック・競合の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020001
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020001
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020001
DSNV401IとOSKB020001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の P-lock と OSKB020001 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0094"><h3>XES propagation</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 共有ロック・競合 ・ 難易度: 上級</p><p>XES propagationは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Data Sharingのロック要求がメンバー内を主な根拠にして完結せず、z/OSの仕組みを通じてCF側へ伝わります。この伝播を説明する要素はどれですか。</p><ul class="kb-choices"><li>A. XESによる伝播 <span class="kb-ok">✅ 正解</span></li><li>B. SPUFIの出力編集</li><li>C. DCLGENのCOPY句</li><li>D. audit policyの保護</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aが適切です。sysplex基盤のXESはsysplex内でCF構造を使う要求の伝播に関わります。Bは対話SQLの出力表示です。Cはホスト変数定義の生成です。Dは監査設定の保護です。Db2内部のみを見ても、CFへ要求が渡る経路の遅れは判断できません；背景にはz/OSのXES propagationは、共有ロック・競合で発生するDb2の要求をCoupling Facilityへ渡す基盤動作です、ロック要求や無効化要求はXESを通じて伝わります、性能問題ではDb2、CF構造、sysplex通信を合わせて確認しますという関係があり、この区別で確認する名称は「propagation」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>XES propagation</strong></p><p>検証目的: 置換確認の共有ロック・競合について、XES propagationは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF 構造に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換確認の共有ロック・競合の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にXES propagationを指定し、OSKB020004の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND XES propagation
CASE OSKB020004
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM XES propagation
CASE OSKB020004
SOURCE Db2 for z/OS
XES propagationとOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020004を同じ出力で読み、置換確認の共有ロック・競合の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020004
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020004
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020004
DSNV401IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の XES propagation と OSKB020004 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0095"><h3>false contention</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 共有ロック・競合 ・ 難易度: 中級</p><p>false contentionは、Data Sharing・Sysplex連携の中で共有ロック・競合に関わるDb2技術項目です。Db2共有資源としての役割、メンバー間影響、CF構造との関係。一方で、XCF/GRS/CF一般論、Sysplex全体設計の詳細。 Db2 data sharing固有の共有資源として扱い、Sysplex/XCF/GRS/CF一般論とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 統計には競合が出ています。しかし、業務処理が同じ行を奪い合った証跡はありません。Data Sharingのロック調査で、実競合と分けて扱う状態はどれですか。</p><ul class="kb-choices"><li>A. SQL warning</li><li>B. 実競合ではないロック衝突 <span class="kb-ok">✅ 正解</span></li><li>C. DSN command prefix</li><li>D. row permission</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bを選びます。false contentionは実際の業務資源競合とは異なる競合として扱い、統計値を見ながら調整します。AはSQL実行結果の警告です。Cはコマンド識別子です。Dは行アクセス制御です。原因を誤ると、アプリケーション改修ではなく構造やロック設計の調整が必要な問題を見落とします；背景には実競合でない待ちを示すfalse contentionは、共有ロック・競合の統計で実際の業務資源競合とは別に扱います、アプリケーションが同じ行を奪い合っていなくても、グローバルロック処理上は競合として見えることがあります、統計値を使い、実競合と分けて調整しますという関係があり、この区別で確認する名称は「false」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>false contention</strong></p><p>検証目的: 呼出確認の共有ロック・競合について、false contentionは、Data Sharing・ Sysplex連携の中で共有ロック・競合に関わる Db2技術項目です。Db2共有資源としての役割、メンバー間影響に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020003の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出確認の共有ロック・競合の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にfalse contentionを指定し、OSKB020003の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND false contention
CASE OSKB020003
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM false contention
CASE OSKB020003
SOURCE Db2 for z/OS
false contentionとOSKB020003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020003を同じ出力で読み、呼出確認の共有ロック・競合の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020003
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020003
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020003
DSNV401IとOSKB020003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の false contention と OSKB020003 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0096"><h3>global contention</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 共有ロック・競合 ・ 難易度: 中級</p><p>global contentionは、Data Sharing・Sysplex連携の中で共有ロック・競合に関わるDb2技術項目です。Db2共有資源としての役割、メンバー間影響、CF構造との関係。一方で、XCF/GRS/CF一般論、Sysplex全体設計の詳細。 Db2 data sharing固有の共有資源として扱い、Sysplex/XCF/GRS/CF一般論とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複数メンバーの更新処理が同じ資源で待ち合い、CFへ伝わるロック要求の競合率が上がっています。調査で見るべき競合はどれですか。</p><ul class="kb-choices"><li>A. ローカルソート領域の不足</li><li>B. カタログ統計の期限切れ</li><li>C. メンバー間のグローバル競合 <span class="kb-ok">✅ 正解</span></li><li>D. SQL文末のセミコロン漏れ</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cが該当します。global contentionはメンバー間で伝播されたロック要求の実競合を示します。Aはメモリ資源の問題です。Bはアクセスパス判断に影響します。DはSQL入力の構文上の問題です。表示結果やトレースから、どのメンバー間で競合しているかを確認します；背景にはメンバー間で起こるglobal contentionは、共有ロック・競合の調査で最初に把握したい実競合です、複数メンバー間で伝播されたロック要求が待ち合っている状態を示します、accounting traceやstatistics traceを使い、対象プラン、メンバー、資源名を絞りますという関係があり、この区別で確認する名称は「global」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details></section>


## Data Sharing・Sysplex連携 > 再始動・CF障害


<section class="kb-item" id="c07-i0097"><h3>CF structure failure</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 再始動・CF障害 ・ 難易度: 上級</p><p>CF structure failureは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害連絡でSCA、lock structure、GBPのどの構造が失われたかを最初に切り分けています。この切り分けが必要になる障害はどれですか。</p><ul class="kb-choices"><li>A. SQLSTATEの桁数不一致</li><li>B. DCLGENメンバーの重複</li><li>C. CF上の共有構造が失われる障害 <span class="kb-ok">✅ 正解</span></li><li>D. JDBCドライバーのJAR不足</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cが正解です。共有構造の障害が起きると、失われた構造により再構築や影響範囲が変わります。AはSQL診断コードの扱いです。Bは開発資材の管理です。Dはクライアント実行環境の不足です。構造名を特定しないまま復旧手順へ進むと、影響範囲を誤ります；背景にはCF構造の障害を切り分けるときは、再始動・CF障害の中でSCA、lock structure、group buffer poolのどこが失われたかを見ます、失われた構造によって再構築方法と業務影響が変わります、特にsimplexのGBP障害は影響が大きくなりますという関係があり、この区別で確認する名称は「failure」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CF structure failure</strong></p><p>検証目的: 探索確認の再始動・ 障害について、CF structure failureは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバーに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020006の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索確認の再始動・ 障害の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCF structure failuを指定し、OSKB020006の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CF structure failu
CASE OSKB020006
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CF structure failu
CASE OSKB020006
SOURCE Db2 for z/OS
CF structure failuとOSKB020006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020006を同じ出力で読み、探索確認の再始動・ 障害の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020006
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020006
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020006
DSNV401IとOSKB020006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CF structure failu と OSKB020006 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0098"><h3>SETXCF FORCE for Db2 structures</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 再始動・CF障害 ・ 難易度: 中級</p><p>SETXCF FORCE for Db2 structuresは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 共有構造の障害後、通常のDb2表示や停止を主な根拠にしては残存状態を整理できません。sysplex側で強制操作を検討する場合、どの種類の操作として扱いますか。</p><ul class="kb-choices"><li>A. SETXCFによるCF構造の強制処理 <span class="kb-ok">✅ 正解</span></li><li>B. SPUFIでのSELECT再実行</li><li>C. BINDのVALIDATE変更</li><li>D. 表スペースのCOMPRESS指定</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aが該当します。sysplex側のSETXCF FORCEはsysplex側の強制処理であり、通常のDb2運用コマンドより影響が大きいため慎重に扱います。BはSQL再実行です。Cはバインド時の検査指定です。Dは格納属性です。通常の表示や停止で解消できる状態なら、強制処理へ進む必要はありません；背景には強制処理を伴うSETXCF FORCE for Db2 structuresは、再始動・CF障害で通常のDb2操作を主な根拠にしては残存状態を整理できない場合に検討します、sysplex側の強制処理に近いため、影響範囲、対象構造、実行条件を手順書で確認してから扱いますという関係があり、この区別で確認する名称は「structures」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETXCF FORCE for Db2 structures</strong></p><p>検証目的: 上書確認の再始動・ 障害について、SETXCF FORCE for Db2 structuresは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書確認の再始動・ 障害の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSETXCF FORCE for Dを指定し、OSKB020007の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SETXCF FORCE for D
CASE OSKB020007
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SETXCF FORCE for D
CASE OSKB020007
SOURCE Db2 for z/OS
SETXCF FORCE for DとOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020007を同じ出力で読み、上書確認の再始動・ 障害の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020007
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020007
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020007
DSNV401IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SETXCF FORCE for D と OSKB020007 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0099"><h3>castout</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 再始動・CF障害 ・ 難易度: 上級</p><p>castoutは、Db2 Data Sharing構成でメンバー間の整合性や共有資源に関わる項目です。Sysplex一般論ではなく、Db2メンバー、CF構造、グループ・バッファー・プールへの影響を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 共有バッファのデータページ資源が速く消費され、変更ページの書き出しが追いついているか確認しています。この処理はどれですか。</p><ul class="kb-choices"><li>A. SQLCA初期化</li><li>B. castout <span class="kb-ok">✅ 正解</span></li><li>C. role付与</li><li>D. PLAN_TABLE削除</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bを選びます。castoutはGBP内の変更ページをページセットへ反映する処理で、遅れは共有バッファ運用に影響します。Aはアプリケーション診断領域です。Cは権限管理です。Dはアクセスパス資料の削除です。回復作業ではなく、書き出しが進んでいるかを見て次の操作を判断します；背景には変更ページの書き出しであるcastoutは、再始動・CF障害の調査でgroup buffer pool内の変更済みページをページセットへ反映する処理です、データエントリーの消費や書き出し遅れがあると、共有バッファの運用に影響します、DISPLAY GROUPBUFFERPOOLの統計で傾向を確認しますという関係があり、この区別で確認する名称は「castout」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0100"><h3>restart light</h3><p class="kb-meta">分類: Data Sharing・Sysplex連携 &gt; 再始動・CF障害 ・ 難易度: 中級</p><p>restart lightは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害メンバーを通常業務へ戻す前に、未解決状態やcastoutに必要な処理のみを進めたい状況です。START DB2で検討する起動方式はどれですか。</p><ul class="kb-choices"><li>A. BIND PACKAGE ACTION(REPLACE)</li><li>B. RUNSTATS PROFILE</li><li>C. DISPLAY THREAD TYPE(ACTIVE)</li><li>D. LIGHT句を使う軽量再始動 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dです。軽量再始動のLIGHT句を使う再始動は、Data Sharingで必要な回復処理を進めるために使います。Aはパッケージ再作成です。Bは統計収集設定です。Cはスレッド表示であり、メンバーの軽量再始動ではありません。軽量再始動のLIGHT句の種類により、処理する範囲と受け付ける作業が変わります；背景には軽量再始動を担うrestart lightは、再始動・CF障害の対応で障害メンバーを限定的に起動する方式です、未確定状態の整理やcastoutなど、共有構成の回復に必要な処理を進める目的で使います、通常業務を受ける起動とは分けて判断しますという関係があり、この区別で確認する名称は「restart」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Introduction</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>restart light</strong></p><p>検証目的: 終端確認の再始動・ 障害について、restart lightは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端確認の再始動・ 障害の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にrestart lightを指定し、OSKB020005の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND restart light
CASE OSKB020005
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM restart light
CASE OSKB020005
SOURCE Db2 for z/OS
restart lightとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020005を同じ出力で読み、終端確認の再始動・ 障害の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020005
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020005
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020005
DSNV401IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の restart light と OSKB020005 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div></details></section>


## Db2コマンドオプション > 運用コマンド


<section class="kb-item" id="c07-i0101"><h3>ARCHIVE LOG MODE（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>ARCHIVE LOG MODEは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧作業に備えてアクティブログを切り替え、アーカイブログ作成の動作を指定したい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. MODE <span class="kb-ok">✅ 正解</span></li><li>B. TYPE</li><li>C. DETAIL</li><li>D. SPACENAM</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ログ切替の動作指定なので A が該当します。アーカイブ処理の進め方は MODE に表れ、復旧点の管理にも影響します。作業時刻も証跡に残します。B: スレッド種類です。C: 詳細表示です。D: データベース内スペース名です；背景にはDb2 のアクティブログをアーカイブへ切り出す操作では、ARCHIVE LOG MODE で処理の進め方を指定します、ログ管理や災害対策の作業として、新しいアーカイブログを作ったタイミングが復旧点の判断に関わります、BSDS のログ履歴確認と合わせて扱いますという関係があり、この区別で確認する名称は「ARCHIVE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ARCHIVE LOG MODE（Db2コマンド指定）</strong></p><p>検証目的: 警告記録の（ コマンドについて、ARCHIVE LOG MODE は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020137の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、警告記録の（ コマンドの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にARCHIVE LOG MODE（Dを指定し、OSKB020137の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ARCHIVE LOG MODE（D
CASE OSKB020137
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ARCHIVE LOG MODE（D
CASE OSKB020137
SOURCE Db2 for z/OS
ARCHIVE LOG MODE（DとOSKB020137が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020137を同じ出力で読み、警告記録の（ コマンドの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020137
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020137
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020137
DSNV401IとOSKB020137が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ARCHIVE LOG MODE（D と OSKB020137 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020137 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0102"><h3>DISPLAY DATABASE SPACENAM（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>DISPLAY DATABASE SPACENAMは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 特定データベースの中でも、表スペース名を指定してページセット状態や使用状況を確認したい状況です。使うキーワードはどれですか。</p><ul class="kb-choices"><li>A. ACCESS</li><li>B. SPACENAM <span class="kb-ok">✅ 正解</span></li><li>C. DEST</li><li>D. CLASS</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表スペースなどの対象指定なので B が合います。データベース内のスペース名は SPACENAM で指定し、表示範囲を狭めます。A: アクセス状態の指定です。C: トレース出力先です。D: トレースクラスです；背景にはDb2 のデータベース内で特定表スペースや索引スペースを表示対象にする指定が、DISPLAY DATABASE SPACENAM です、ページセットの状態、使用中プログラム、対象パーティションの確認で使います、データベース名を主な根拠にしては範囲が広いとき、調査対象を狭められますという関係があり、この区別で確認する名称は「SPACENAM」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0103"><h3>DISPLAY DDF（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>DISPLAY DDFは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リモート接続障害の一次調査で、DDF の起動状態、構成、接続統計を画面に出して確認したい状況です。実行するコマンド語はどれですか。</p><ul class="kb-choices"><li>A. MODIFY</li><li>B. TERM</li><li>C. RECOVER</li><li>D. DISPLAY <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 状態と統計を出す操作なので D が正解です。DDF の構成、稼働状態、接続やスレッド統計は DISPLAY DDF で確認します。A: 稼働中設定を変更します。B: ユーティリティを終了させます。C: BSDS 復旧に使います；背景にはDDF の状態、構成、接続やスレッド統計を表示する Db2 コマンドが DISPLAY DDF です、分散接続障害の一次切り分けではなく、起動状態、ロケーション情報、接続数を同じ画面で確認する目的で使います、開始や停止の結果確認にも使いますという関係があり、この区別で確認する名称は「DDF」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DISPLAY DDF（Db2コマンド指定）</strong></p><p>検証目的: 区切記録の（ コマンド指定）について、DISPLAY DDF は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020130の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDISPLAY DDF（Db2コマンを指定し、OSKB020130の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DISPLAY DDF（Db2コマン
CASE OSKB020130
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DISPLAY DDF（Db2コマン
CASE OSKB020130
SOURCE Db2 for z/OS
DISPLAY DDF（Db2コマンとOSKB020130が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020130を同じ出力で読み、区切記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020130
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020130
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020130
DSNV401IとOSKB020130が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DISPLAY DDF（Db2コマン と OSKB020130 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020130 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0104"><h3>DISPLAY GROUP DETAIL（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>DISPLAY GROUP DETAILは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Data Sharing グループ全体について、メンバーの状態や構成を詳細に表示して切替判断の材料にしたい状況です。追加するキーワードはどれですか。</p><ul class="kb-choices"><li>A. MODE</li><li>B. PARM</li><li>C. ACCESS</li><li>D. DETAIL <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> グループ情報を詳しく出すため D を選びます。メンバー状態や構成確認を深くする指定が DETAIL です。A: 停止方式などの動作モードです。B: 起動時パラメーターです。C: START DATABASE で使う利用可能状態です；背景にはDb2 Data Sharing グループのメンバーや状態を詳しく見る指定が DISPLAY GROUP DETAIL です、グループ内の稼働メンバー、接続状況、レベル差を確認すると、メンバー障害や保守切替の判断がしやすくなります、単一メンバーの表示と混同しないことが大切ですという関係があり、この区別で確認する名称は「GROUP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DISPLAY GROUP DETAIL（Db2コマンド指定）</strong></p><p>検証目的: 順序記録の（について、DISPLAY GROUP DETAIL は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020135の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、順序記録の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDISPLAY GROUP DETAを指定し、OSKB020135の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DISPLAY GROUP DETA
CASE OSKB020135
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DISPLAY GROUP DETA
CASE OSKB020135
SOURCE Db2 for z/OS
DISPLAY GROUP DETAとOSKB020135が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020135を同じ出力で読み、順序記録の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020135
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020135
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020135
DSNV401IとOSKB020135が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DISPLAY GROUP DETA と OSKB020135 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020135 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0105"><h3>DISPLAY THREAD DETAIL（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>DISPLAY THREAD DETAILは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アクティブスレッドの概要を主な根拠にしてなく、要求元やプラン、会話情報まで見て障害解析したい状況です。追加する表示キーワードはどれですか。</p><ul class="kb-choices"><li>A. TYPE</li><li>B. MODE</li><li>C. DETAIL <span class="kb-ok">✅ 正解</span></li><li>D. PARM</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 詳細情報を加えるため C を選びます。接続元や実行情報を深く表示する指定が DETAIL で、後続の切り分けに使えます。A: 表示対象の種類を絞ります。B: 停止などの動作モードです。D: 起動時モジュール指定です；背景にはスレッドの要求元、認可 ID、プラン、LUWID などを詳しく追う場合、Db2 コマンドの DISPLAY THREAD DETAIL を指定します、分散会話や待ち状態の調査ではなく、接続経路や実行位置を追う目的で概要表示に詳細を加えます、表示されたトークンは障害解析の後続操作に使いますという関係があり、この区別で確認する名称は「THREAD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DISPLAY THREAD DETAIL（Db2コマンド指定）</strong></p><p>検証目的: 範囲記録の（について、DISPLAY THREAD DETAIL は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けまに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020131の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、範囲記録の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDISPLAY THREAD DETを指定し、OSKB020131の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DISPLAY THREAD DET
CASE OSKB020131
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DISPLAY THREAD DET
CASE OSKB020131
SOURCE Db2 for z/OS
DISPLAY THREAD DETとOSKB020131が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020131を同じ出力で読み、範囲記録の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020131
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020131
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020131
DSNV401IとOSKB020131が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DISPLAY THREAD DET と OSKB020131 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020131 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0106"><h3>DISPLAY THREAD TYPE（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>DISPLAY THREAD TYPEは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 多数のスレッドから、ストアードプロシージャー実行中など特定種類のもののみを抽出して表示したい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. DETAIL</li><li>B. TYPE <span class="kb-ok">✅ 正解</span></li><li>C. SPACENAM</li><li>D. ACCESS</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> スレッド種類で絞るため B が該当します。表示対象を分類で選ぶ指定が TYPE で、広すぎる一覧を避けられます。A: 詳細情報を追加します。C: 表スペース名で範囲を絞る指定です。D: データベースアクセス状態の制御です；背景にはスレッドを種類で絞り込む Db2 コマンド指定が DISPLAY THREAD TYPE です、アクティブ、プロシージャー実行中、分散関連など、調査対象に合うスレッドのみを出すと原因箇所を追いやすくなります、大量接続時の表示抑制にも役立ちますという関係があり、この区別で確認する名称は「TYPE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0107"><h3>DISPLAY UTILITY（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>DISPLAY UTILITYは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守作業前に、実行中または停止中のユーティリティと現在フェーズを確認して記録したい状況です。実行するコマンド語はどれですか。</p><ul class="kb-choices"><li>A. TERM</li><li>B. RECOVER</li><li>C. DISPLAY <span class="kb-ok">✅ 正解</span></li><li>D. START</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 状態確認が目的なので C が正解です。ユーティリティ名、フェーズ、対象の表示には DISPLAY UTILITY を使います。A: ユーティリティを終了します。B: BSDS の復旧操作です。D: 機能やトレースの開始です；背景には実行中ユーティリティの名前、フェーズ、対象を確認する Db2 コマンドが DISPLAY UTILITY です、災害復旧や保守前の点検として、未完了ユーティリティが残っていないかを確認します、表示されたユーティリティ ID は、必要なら TERM UTILITY の判断材料になりますという関係があり、この区別で確認する名称は「DISPLAY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0108"><h3>MODIFY DDF（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>MODIFY DDFは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> DDF を全面停止せず、稼働中に分散接続まわりの動作を調整したい状況です。START や STOP ではなく確認するコマンド語はどれですか。</p><ul class="kb-choices"><li>A. DISPLAY</li><li>B. START</li><li>C. STOP</li><li>D. MODIFY <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 稼働中の調整なら D を選びます。DDF 関連の変更操作は MODIFY DDF で行い、変更後の状態確認と組み合わせます。A: 情報表示のみを行います。B: 停止中の機能を開始します。C: 機能を停止します；背景には稼働中の DDF 関連動作を変える場合、Db2 コマンドの MODIFY DDF を使います、通信設定や接続受付の調整で、完全停止を避けながら変更したい場面に向きます、変更後は DISPLAY DDF で実際の状態と統計を確認し、変更内容が反映されたかを記録しますという関係があり、この区別で確認する名称は「MODIFY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MODIFY DDF（Db2コマンド指定）</strong></p><p>検証目的: 条件記録の（ コマンド指定）について、MODIFY DDF は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020129の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にMODIFY DDF（Db2コマンドを指定し、OSKB020129の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND MODIFY DDF（Db2コマンド
CASE OSKB020129
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM MODIFY DDF（Db2コマンド
CASE OSKB020129
SOURCE Db2 for z/OS
MODIFY DDF（Db2コマンドとOSKB020129が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020129を同じ出力で読み、条件記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020129
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020129
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020129
DSNV401IとOSKB020129が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の MODIFY DDF（Db2コマンド と OSKB020129 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020129 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0109"><h3>RECOVER BSDS（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>RECOVER BSDSは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 片方の BSDS を再定義した後、正常な BSDS から内容をコピーして二重化状態を回復したい状況です。使うコマンド語はどれですか。</p><ul class="kb-choices"><li>A. DISPLAY</li><li>B. START</li><li>C. STOP</li><li>D. RECOVER <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> BSDS 二重化の復旧なので D を選択します。良好な BSDS から置換先へコピーし、二重構成を戻す操作が RECOVER BSDS です。A: 情報表示です。B: 機能開始です。C: 停止操作です；背景には二重化した BSDS の片系を失った場合、Db2 の RECOVER BSDS で正常な BSDS から置換先へコピーして二重化を戻します、交換先 BSDS が空であることや、単一 BSDS モードで継続中であることを確認します、実行後はログ目録の整合を点検しますという関係があり、この区別で確認する名称は「RECOVER」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECOVER BSDS（Db2コマンド指定）</strong></p><p>検証目的: 復旧記録の（ コマンド指定）について、RECOVER BSDS は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020138の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、復旧記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRECOVER BSDS（Db2コマを指定し、OSKB020138の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RECOVER BSDS（Db2コマ
CASE OSKB020138
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RECOVER BSDS（Db2コマ
CASE OSKB020138
SOURCE Db2 for z/OS
RECOVER BSDS（Db2コマとOSKB020138が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020138を同じ出力で読み、復旧記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020138
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020138
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020138
DSNV401IとOSKB020138が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RECOVER BSDS（Db2コマ と OSKB020138 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020138 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0110"><h3>START DATABASE ACCESS（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>START DATABASE ACCESSは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守後に停止していたデータベースオブジェクトを利用可能状態へ戻し、読み取りまたは更新の許可状態を指定したい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. ACCESS <span class="kb-ok">✅ 正解</span></li><li>B. DETAIL</li><li>C. TYPE</li><li>D. IFCID</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 利用可能状態の制御なので A が正解です。対象オブジェクトを読み取り専用や更新可能に戻す指定が ACCESS です。B: スレッド詳細表示です。C: スレッド種別の絞り込みです。D: トレースイベント番号です；背景には停止や制限状態にした Db2 データベースオブジェクトのアクセスを戻す場合、START DATABASE ACCESS を使います、読み取り専用か更新可能かという状態により、業務へ戻せる操作範囲が変わります、復旧後の開放では、対象データベースとスペース名を取り違えないようにしますという関係があり、この区別で確認する名称は「ACCESS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>START DATABASE ACCESS（Db2コマンド指定）</strong></p><p>検証目的: 記録記録の（について、START DATABASE ACCESS は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けまに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020133の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、記録記録の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTART DATABASE ACCを指定し、OSKB020133の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND START DATABASE ACC
CASE OSKB020133
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM START DATABASE ACC
CASE OSKB020133
SOURCE Db2 for z/OS
START DATABASE ACCとOSKB020133が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020133を同じ出力で読み、記録記録の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020133
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020133
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020133
DSNV401IとOSKB020133が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の START DATABASE ACC と OSKB020133 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020133 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0111"><h3>START DB2 PARM（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>START DB2 PARMは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守試験用のサブシステムパラメーターモジュールで Db2 を起動し、既定値ではなく明示したモジュールを使った証跡を残したい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. PARM <span class="kb-ok">✅ 正解</span></li><li>B. MODE</li><li>C. ACCESS</li><li>D. DETAIL</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 起動時モジュールの指定なら A を選び、START DB2 の読み込み対象は PARM で示します。既定値との差分を残す点が重要です。B: 停止やログ処理の動作モードです。C: オブジェクトの利用可否に使います。D: 表示情報を詳細化する指定です；背景には起動時に読み込む Db2 サブシステムパラメーターモジュールは、START DB2 PARM で指定します、通常は導入時の既定モジュールを使います、一方で、保守作業や切替試験では別モジュールを明示することがあります、操作記録には、サブシステム名と指定したモジュール名を残しますという関係があり、この区別で確認する名称は「PARM」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0112"><h3>START DDF（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>START DDFは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守後にリモートアプリケーションからの DRDA 接続を再開するため、停止中の分散データ機能を開始したい状況です。実行するコマンドはどれですか。</p><ul class="kb-choices"><li>A. STOP DDF</li><li>B. DISPLAY DDF</li><li>C. START DDF <span class="kb-ok">✅ 正解</span></li><li>D. MODIFY DDF</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> DDF を開始する操作なので C が正解です。START DDF は分散データ機能を起動し、TCP/IP や VTAM 経由の接続受付を再開します。A: 分散接続を停止します。B: 状態や統計を表示します。D: 稼働中設定の変更に使います；背景には分散接続を受け付けるための Db2 運用コマンドが START DDF です、分散データ機能が停止していると、リモートクライアントからの接続は利用できません、開始後は、待受ポート、ロケーション名、接続統計を DISPLAY DDF で確認しますという関係があり、この区別で確認する名称は「DDF」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0113"><h3>START TRACE DEST（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>START TRACE DESTは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> トレースを開始する際、採取した情報を SMF へ書くのか GTF へ出すのかを明示したい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. CLASS</li><li>B. TYPE</li><li>C. DEST <span class="kb-ok">✅ 正解</span></li><li>D. DETAIL</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力先の指定なので C が該当します。START TRACE の DEST は保存先を選び、後続の証跡取得方法を決めます。採取後の受け渡し先も確認します。A: トレースクラスです。B: スレッド種類です。D: 詳細表示の追加です；背景には採取した Db2 トレースをどこへ出すかは、START TRACE DEST で指定します、出力先の種類により、後続の収集方法と保管場所が変わります、class や IFCID と組み合わせる場合、既定出力先との競合にも注意します、調査依頼票には指定した保存先を残しますという関係があり、この区別で確認する名称は「DEST」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>START TRACE DEST（Db2コマンド指定）</strong></p><p>検証目的: 変更記録の（ コマンドについて、START TRACE DEST は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020140の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更記録の（ コマンドの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTART TRACE DEST（Dを指定し、OSKB020140の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND START TRACE DEST（D
CASE OSKB020140
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM START TRACE DEST（D
CASE OSKB020140
SOURCE Db2 for z/OS
START TRACE DEST（DとOSKB020140が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020140を同じ出力で読み、変更記録の（ コマンドの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020140
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020140
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020140
DSNV401IとOSKB020140が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の START TRACE DEST（D と OSKB020140 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020140 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0114"><h3>START TRACE IFCID（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 上級</p><p>START TRACE IFCIDは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> IBM Support から指定されたイベント番号のみを採取するため、トレース対象を class より細かく絞りたい状況です。使うキーワードはどれですか。</p><ul class="kb-choices"><li>A. DEST</li><li>B. IFCID <span class="kb-ok">✅ 正解</span></li><li>C. PARM</li><li>D. TYPE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> イベント番号で絞るため B を選びます。START TRACE の IFCID は採取する Db2 イベントを番号で指定し、調査目的を細かく限定できます。A: トレース出力先です。C: 起動パラメーターです。D: スレッド種類です；背景には特定イベントのみを狙って Db2 トレースを開始する場合、START TRACE IFCID を使います、IFCID は Db2 が記録するイベントや情報単位を示す番号で、class より細かい採取に使えます、IBM Support 指示の調査では、指定された IFCID と出力先を正確に残しますという関係があり、この区別で確認する名称は「IFCID」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>START TRACE IFCID（Db2コマンド指定）</strong></p><p>検証目的: 監査記録の（ コマンについて、START TRACE IFCID は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020139の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、監査記録の（ コマンの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTART TRACE IFCID（を指定し、OSKB020139の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND START TRACE IFCID（
CASE OSKB020139
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM START TRACE IFCID（
CASE OSKB020139
SOURCE Db2 for z/OS
START TRACE IFCID（とOSKB020139が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020139を同じ出力で読み、監査記録の（ コマンの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020139
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020139
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020139
DSNV401IとOSKB020139が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の START TRACE IFCID（ と OSKB020139 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020139 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0115"><h3>START TRACE class（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>START TRACE classは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 性能調査のため Db2 トレースを開始し、収集する種類や範囲をクラス番号で指定したい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. DEST</li><li>B. MODE</li><li>C. ACCESS</li><li>D. CLASS <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集範囲をクラスで選ぶため D が正解です。目的別のトレースクラスを指定するキーワードが CLASS で、取得される情報量を左右します。A: 出力先です。B: 動作モードです。C: START DATABASE 側の利用可能状態です；背景にはDb2 トレースを開始するとき、START TRACE class は収集するトレースクラスを指定します、会計、統計、性能などの種類ごとに収集される IFCID が変わるため、目的に合う class を選びます、過剰な収集は出力データ量を増やす点にも注意しますという関係があり、この区別で確認する名称は「class」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0116"><h3>STOP DATABASE（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>STOP DATABASEは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 回復作業の前に、対象データベースまたは表スペースへの利用を止めて業務アクセスを遮断したい状況です。実行するコマンドはどれですか。</p><ul class="kb-choices"><li>A. START TRACE</li><li>B. DISPLAY DDF</li><li>C. STOP DATABASE <span class="kb-ok">✅ 正解</span></li><li>D. ARCHIVE LOG</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> オブジェクト利用を止めるため C が該当します。STOP DATABASE はデータベースやスペースを保守作業向けに停止させる操作です。A: トレースを開始します。B: DDF 状態を表示します。D: ログアーカイブを要求します；背景にはデータベースや表スペースへの利用を止める Db2 運用操作が STOP DATABASE です、保守、回復、再編成の前に対象オブジェクトを静止させるために使います、停止範囲を誤ると業務影響が広がるため、DATABASE 名や SPACENAM の組み合わせを確認しますという関係があり、この区別で確認する名称は「DATABASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOP DATABASE（Db2コマンド指定）</strong></p><p>検証目的: 比較記録の（ コマンド指定）について、STOP DATABASE は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点ではに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020134の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DATABASE（Db2コを指定し、OSKB020134の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DATABASE（Db2コ
CASE OSKB020134
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DATABASE（Db2コ
CASE OSKB020134
SOURCE Db2 for z/OS
STOP DATABASE（Db2コとOSKB020134が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020134を同じ出力で読み、比較記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020134
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020134
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020134
DSNV401IとOSKB020134が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の STOP DATABASE（Db2コ と OSKB020134 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020134 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0117"><h3>STOP DB2 MODE（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>STOP DB2 MODEは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 夜間停止で処理中の作業をできるのみ完了させるか、障害対応として早く止めるかを STOP DB2 で選びたい状況です。確認するキーワードはどれですか。</p><ul class="kb-choices"><li>A. PARM</li><li>B. MODE <span class="kb-ok">✅ 正解</span></li><li>C. TYPE</li><li>D. DEST</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 停止方式の切替なので B が該当し、STOP DB2 の停止動作は MODE で指定します。通常停止と強制停止の違いを運用手順で分けます。A: 起動時モジュールです。C: スレッド表示の種類です。D: トレース出力先を示します；背景には停止方法を制御する Db2 コマンド指定として、STOP DB2 MODE は通常停止か強制停止かを分けます、運用停止では実行中作業の完了を待ち、障害対応では早急な停止を選ぶことがあります、停止前には、接続中スレッドと未完了ユーティリティの影響を確認しますという関係があり、この区別で確認する名称は「MODE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOP DB2 MODE（Db2コマンド指定）</strong></p><p>検証目的: 上書記録の（ コマンド指定）について、STOP DB2 MODE は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点ではに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020127の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DB2 MODE（Db2コを指定し、OSKB020127の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DB2 MODE（Db2コ
CASE OSKB020127
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DB2 MODE（Db2コ
CASE OSKB020127
SOURCE Db2 for z/OS
STOP DB2 MODE（Db2コとOSKB020127が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020127を同じ出力で読み、上書記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020127
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020127
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020127
DSNV401IとOSKB020127が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の STOP DB2 MODE（Db2コ と OSKB020127 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020127 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0118"><h3>STOP DDF（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>STOP DDFは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ネットワーク保守のため、新しい分散接続を止めて DDF インターフェースを停止したい状況です。対象のコマンドはどれですか。</p><ul class="kb-choices"><li>A. START DDF</li><li>B. STOP DDF <span class="kb-ok">✅ 正解</span></li><li>C. DISPLAY THREAD</li><li>D. DISPLAY GROUP</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 分散接続を止める目的なら B を選びます。STOP DDF は DDF インターフェースを停止し、MODE 指定により停止の強さを調整します。A: DDF を開始します。C: スレッドの状況表示です。D: データ共有グループ情報を表示します；背景には外部からの分散接続を止める操作は、Db2 の STOP DDF で行います、MODE を指定しない通常停止と FORCE や SUSPEND の使い分けで、既存接続や新規受付への影響が変わります、停止後も保持される関連資源があるため、必要に応じてスレッド状態を追跡しますという関係があり、この区別で確認する名称は「STOP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOP DDF（Db2コマンド指定）</strong></p><p>検証目的: 出力記録の（ コマンド指定）について、STOP DDF は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行としに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020128の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DDF（Db2コマンド指定を指定し、OSKB020128の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DDF（Db2コマンド指定
CASE OSKB020128
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DDF（Db2コマンド指定
CASE OSKB020128
SOURCE Db2 for z/OS
STOP DDF（Db2コマンド指定とOSKB020128が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020128を同じ出力で読み、出力記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020128
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020128
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020128
DSNV401IとOSKB020128が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の STOP DDF（Db2コマンド指定 と OSKB020128 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020128 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


<section class="kb-item" id="c07-i0119"><h3>TERM UTILITY（Db2コマンド指定）</h3><p class="kb-meta">分類: Db2コマンドオプション &gt; 運用コマンド ・ 難易度: 中級</p><p>TERM UTILITYは、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧先で再開できないユーティリティが残っており、状態を整理して後続作業を進めたい状況です。使用を検討するコマンド語はどれですか。</p><ul class="kb-choices"><li>A. DISPLAY</li><li>B. TERM <span class="kb-ok">✅ 正解</span></li><li>C. ARCHIVE</li><li>D. MODIFY</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 未完了ユーティリティを終了扱いにするため B を選びます。TERM UTILITY は残存したユーティリティ状態の整理に使います。A: 状態表示を主な根拠にしてす。C: ログのアーカイブ要求です。D: 稼働中設定の変更です；背景には中断したユーティリティを終了扱いにする Db2 コマンドが TERM UTILITY です、災害復旧先などで再開できないユーティリティが残る場合、SYSUTILX 上の状態を整理するために使います、ただし対象外のシステムユーティリティを誤って終了しない確認が必要ですという関係があり、この区別で確認する名称は「TERM」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TERM UTILITY（Db2コマンド指定）</strong></p><p>検証目的: 値域記録の（ コマンド指定）について、TERM UTILITY は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対応付けます。 現時点では候に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020136の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、値域記録の（ コマンド指定）の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にTERM UTILITY（Db2コマを指定し、OSKB020136の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND TERM UTILITY（Db2コマ
CASE OSKB020136
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM TERM UTILITY（Db2コマ
CASE OSKB020136
SOURCE Db2 for z/OS
TERM UTILITY（Db2コマとOSKB020136が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020136を同じ出力で読み、値域記録の（ コマンド指定）の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020136
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020136
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020136
DSNV401IとOSKB020136が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の TERM UTILITY（Db2コマ と OSKB020136 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020136 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div></details></section>


## SQL/DDL句・属性 > DDLオプション


<section class="kb-item" id="c07-i0120"><h3>CREATE INDEX BUFFERPOOL（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE INDEX BUFFERPOOLは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 索引 PAYIX を作るとき、索引ページを BP1 に載せるようDDLで指定したい状況です。制御している対象はどれですか。</p><ul class="kb-choices"><li>A. 索引用BP <span class="kb-ok">✅ 正解</span></li><li>B. 区画方式</li><li>C. 権限付与対象</li><li>D. 発火時点</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 索引ページのバッファープールを決めるため、Aが正しいです。表スペースではなく索引側のページをどこへ載せるかを指定します。Bは表データの分割方式、Cは権限を与える相手、Dはトリガーの起動時点です。表用の指定と混同しないようにします；背景には索引ページ用のメモリーを設計するときに CREATE INDEX BUFFERPOOL が Db2 の DDL オプションとして索引に使うバッファープールを指定します、表データ用とは別のBPを選ぶことで、ページサイズやアクセス傾向に合わせられます、索引のI/O特性を見て、表スペース側の指定と混同しないようにしますという関係があり、この区別で確認する名称は「BUFFERPOOL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE INDEX BUFFERPOOL（DDL 句・属性）</strong></p><p>検証目的: 記録分離の（について、CREATE INDEX BUFFERPOOL は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020153の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、記録分離の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE INDEX BUFFEを指定し、OSKB020153の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE INDEX BUFFE
CASE OSKB020153
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE INDEX BUFFE
CASE OSKB020153
SOURCE Db2 for z/OS
CREATE INDEX BUFFEとOSKB020153が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020153を同じ出力で読み、記録分離の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020153
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020153
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020153
DSNV401IとOSKB020153が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE INDEX BUFFE と OSKB020153 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020153 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0121"><h3>CREATE INDEX CLUSTER（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE INDEX CLUSTERは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 日付範囲でよく読む表について、索引順に近い並びでデータを保ち、範囲検索を助けたい状況です。この指定の意味はどれですか。</p><ul class="kb-choices"><li>A. 権限付与</li><li>B. データ圧縮</li><li>C. 近接配置 <span class="kb-ok">✅ 正解</span></li><li>D. 区画上限</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 索引順に近い配置を意図するため、Cが合います。範囲検索で読みやすい並びを保つ狙いがあります。Aは権限を与える操作、Bは表データ圧縮、Dは成長型表スペースの上限です。範囲検索には有効です。一方で、更新が多い表では再編成計画も見ます；背景には読み取り順と物理配置を近づける設計で、CREATE INDEX CLUSTER は Db2 の DDL オプションとしてクラスタリング索引を示します、表データをその索引順に近く配置する意図を持たせます、範囲検索の効率に効く一方、更新や再編成の計画も合わせて考えますという関係があり、この区別で確認する名称は「CLUSTER」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE INDEX CLUSTER（DDL 句・属性）</strong></p><p>検証目的: 範囲分離の（について、CREATE INDEX CLUSTER は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020151の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、範囲分離の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE INDEX CLUSTを指定し、OSKB020151の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE INDEX CLUST
CASE OSKB020151
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE INDEX CLUST
CASE OSKB020151
SOURCE Db2 for z/OS
CREATE INDEX CLUSTとOSKB020151が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020151を同じ出力で読み、範囲分離の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020151
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020151
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020151
DSNV401IとOSKB020151が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE INDEX CLUST と OSKB020151 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020151 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0122"><h3>CREATE INDEX PIECESIZE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE INDEX PIECESIZEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 巨大な索引について、データセットをどの大きさの単位で分けて管理するかをDDLで決めたい状況です。確認する内容はどれですか。</p><ul class="kb-choices"><li>A. 変更捕捉</li><li>B. ロック粒度</li><li>C. SMS管理属性</li><li>D. 索引片サイズ <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 大きな索引を分ける単位を決めるため、Dを選びます。索引を構成するピースの大きさを指定し、保守やユーティリティ処理の単位に影響します。Aは変更データの記録、Bはロック取得単位、Cはストレージ管理属性です。成長量を見込んで値を決めます；背景には大きな索引を扱うとき、CREATE INDEX PIECESIZE は SQL/DDL句・属性として索引データセットを分けるピース単位の大きさを指定します、値が小さいと分割数が増え、値が大きいと1単位の扱いが重くなります、索引成長量と保守作業の粒度を合わせて設計しますという関係があり、この区別で確認する名称は「PIECESIZE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE INDEX PIECESIZE（DDL 句・属性）</strong></p><p>検証目的: 優先分離の（について、CREATE INDEX PIECESIZE は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020152の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、優先分離の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE INDEX PIECEを指定し、OSKB020152の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE INDEX PIECE
CASE OSKB020152
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE INDEX PIECE
CASE OSKB020152
SOURCE Db2 for z/OS
CREATE INDEX PIECEとOSKB020152が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020152を同じ出力で読み、優先分離の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020152
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020152
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020152
DSNV401IとOSKB020152が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE INDEX PIECE と OSKB020152 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020152 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0123"><h3>CREATE INDEX UNIQUE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE INDEX UNIQUEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 社員番号に同じ値を登録させないため、索引定義でキー重複を防ぎたい状況です。DDLで指定する性質はどれですか。</p><ul class="kb-choices"><li>A. 配置DB</li><li>B. 重複防止 <span class="kb-ok">✅ 正解</span></li><li>C. 信頼属性</li><li>D. 圧縮利用</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> キーの重複を防ぐ指定として、Bを選びます。索引キーに同じ値を許さないため、社員番号などの業務キー保護に使います。Aは表を置く場所、Cは信頼接続の条件、Dは圧縮の利用有無です。既存データに重複がないことを事前に確認します；背景には重複を許さないキーを設計するときに CREATE INDEX UNIQUE が Db2 の SQL/DDL句・属性として索引キーの一意性を保証します、表の制約や業務キーの保護に使われ、同じキー値の登録を防ぎます、既存データに重複があると作成に失敗するため、移行前の確認が必要ですという関係があり、この区別で確認する名称は「UNIQUE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0124"><h3>CREATE STOGROUP DATACLAS/STORCLAS/MGMTCLAS（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE STOGROUP DATACLAS/STORCLAS/MGMTCLASは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Db2 のストレージグループ作成時に、割当や保管方針をSMSポリシーへ合わせたい状況です。DDLで示す対象はどれですか。</p><ul class="kb-choices"><li>A. 初期区画</li><li>B. ロック粒度</li><li>C. 信頼接続条件</li><li>D. SMS属性束 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ストレージ管理のクラス名をまとめて指定するため、Dを選びます。割当、性能、保管期間などのSMSポリシーとDb2の定義を結びます。Aは作成時の区画数、Bはロックの粒度、Cは信頼接続の条件です。運用部門が定義した名前と一致させます；背景にはSMS 管理の属性をそろえるために、Db2 の CREATE STOGROUP DATACLAS/STORCLAS/MGMTCLAS を確認します、データクラス、ストレージクラス、管理クラスをDDLで指定します、割当、性能、保管期間のポリシーに関係するため、運用部門の定義名と一致させますという関係があり、この区別で確認する名称は「DATACLAS/STORCLAS/MGMTCLAS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0125"><h3>CREATE STOGROUP VCAT（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE STOGROUP VCATは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ストレージグループ配下のデータセットについて、管理に使う VSAM カタログをDDLで明示したい状況です。該当する内容はどれですか。</p><ul class="kb-choices"><li>A. BP選択</li><li>B. 権限取消</li><li>C. カタログ名 <span class="kb-ok">✅ 正解</span></li><li>D. トリガー発火条件</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> データセットを管理するカタログを示すため、Cが該当します。ストレージグループのデータセットをどのVSAMカタログへ登録するかを決めます。Aはバッファープール選択、Bは権限取り消し、Dはトリガー条件です。カタログ名は命名標準と照合します；背景にはDb2 のデータセットをどのカタログで管理するかを見る作業で、CREATE STOGROUP VCAT は SQL/DDL句・属性として VSAM カタログ名を指定します、ストレージグループに属するデータセットのカタログ管理先を決める指定です、既存カタログ名と命名標準を合わせて記録しますという関係があり、この区別で確認する名称は「VCAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE STOGROUP VCAT（DDL 句・属性）</strong></p><p>検証目的: 順序分離の（について、CREATE STOGROUP VCAT は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020155の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、順序分離の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE STOGROUP VCを指定し、OSKB020155の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE STOGROUP VC
CASE OSKB020155
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE STOGROUP VC
CASE OSKB020155
SOURCE Db2 for z/OS
CREATE STOGROUP VCとOSKB020155が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020155を同じ出力で読み、順序分離の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020155
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020155
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020155
DSNV401IとOSKB020155が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE STOGROUP VC と OSKB020155 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020155 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0126"><h3>CREATE STOGROUP VOLUMES（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE STOGROUP VOLUMESは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ストレージグループを作成し、データセット配置に使えるボリューム集合またはSMS任せをDDLで示したい状況です。どれを扱いますか。</p><ul class="kb-choices"><li>A. 信頼ID</li><li>B. 候補VOLS <span class="kb-ok">✅ 正解</span></li><li>C. 索引順</li><li>D. 表データ圧縮可否</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 配置候補となるボリュームを示すので、Bを選びます。ストレージグループが利用するボリューム集合、またはSMS管理へ委ねる指定を扱います。Aは信頼接続の認可ID、Cはクラスタリング索引の意図、Dは表圧縮の有無です。運用標準と合うか確認します；背景にはストレージ配置をDb2から指定する場合、CREATE STOGROUP VOLUMES は SQL/DDL句・属性として使用候補となるボリューム集合を示します、アスタリスク指定ならSMS管理に委ねる形になります、実機ではストレージポリシーや運用標準と合うかを確認しますという関係があり、この区別で確認する名称は「VOLUMES」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE STOGROUP VOLUMES（DDL 句・属性）</strong></p><p>検証目的: 比較分離の（について、CREATE STOGROUP VOLUMES は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020154の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較分離の（の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE STOGROUP VOを指定し、OSKB020154の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE STOGROUP VO
CASE OSKB020154
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE STOGROUP VO
CASE OSKB020154
SOURCE Db2 for z/OS
CREATE STOGROUP VOとOSKB020154が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020154を同じ出力で読み、比較分離の（の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020154
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020154
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020154
DSNV401IとOSKB020154が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE STOGROUP VO と OSKB020154 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020154 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0127"><h3>CREATE TABLE DATA CAPTURE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLE DATA CAPTUREは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 更新された行の情報を下流連携で利用するため、表定義で変更内容を残すかどうかを決めたい状況です。対象の指定はどれですか。</p><ul class="kb-choices"><li>A. 変更捕捉 <span class="kb-ok">✅ 正解</span></li><li>B. 索引用BP</li><li>C. 表所属</li><li>D. 区画数</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更情報を下流へ渡す目的で使うため、Aが正解です。表で発生した更新内容を後続処理が扱えるようにする指定です。Bは索引用バッファープール、Cは表の配置先、Dは作成時の区画数です。連携先の要件とログ量を見て有効化します；背景には複製や監査へ変更情報を渡す設計では、CREATE TABLE DATA CAPTURE が Db2 の DDL オプションとして表の変更データを記録対象にするかを示します、CHANGES を指定すると、変更内容を後続処理が利用しやすくなります、ログ量や連携先の要件を確認して有効化しますという関係があり、この区別で確認する名称は「CAPTURE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLE DATA CAPTURE（DDL 句・属性）</strong></p><p>検証目的: 区切分離のオプションについて、CREATE TABLE DATA CAPTURE は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020150の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLE DATA を指定し、OSKB020150の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLE DATA 
CASE OSKB020150
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLE DATA 
CASE OSKB020150
SOURCE Db2 for z/OS
CREATE TABLE DATA とOSKB020150が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020150を同じ出力で読み、区切分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020150
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020150
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020150
DSNV401IとOSKB020150が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLE DATA  と OSKB020150 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020150 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0128"><h3>CREATE TABLE IN DATABASE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLE IN DATABASEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表スペース名までは指定せず、表をどのデータベース配下に置くかのみをDDLで明示したい状況です。管理対象はどれですか。</p><ul class="kb-choices"><li>A. 所属DB <span class="kb-ok">✅ 正解</span></li><li>B. 既存TS</li><li>C. 変更記録</li><li>D. ボリューム</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表を置くデータベースの管理境界を示すため、Aを選びます。表スペース名を直接書かない作成でも、どのデータベース配下に置くかを制御できます。Bは既存表スペースへの配置、Cは変更データの捕捉、Dはストレージグループのボリューム候補です。命名規則と権限範囲を合わせます；背景には表の管理境界をそろえる場面で、CREATE TABLE IN DATABASE は Db2 の DDL オプションとして暗黙作成される表スペースの所属先データベースを指定します、表スペース名を直接示さない場合でも、どのデータベース配下に作るかを制御できます、命名規則や権限管理の境界を合わせるために使いますという関係があり、この区別で確認する名称は「DATABASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0129"><h3>CREATE TABLE IN TABLESPACE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLE IN TABLESPACEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 既に作成済みの PAYDB.PAYTS に新しい表を格納し、領域設計を再利用したい状況です。DDLで示す内容はどれですか。</p><ul class="kb-choices"><li>A. ロック上限値</li><li>B. 既存TS配置 <span class="kb-ok">✅ 正解</span></li><li>C. 信頼接続</li><li>D. 索引片</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 既にある表スペースへ入れる指定なので、Bを選択します。容量やロックなどの既存設計を利用したいときに、データベース名と表スペース名を示します。Aはロック数の上限、Cは信頼接続の条件、Dは索引の分割単位です。暗黙作成を避けたい運用で使います；背景には既存の表スペースへ表を入れる場合、Db2 の SQL/DDL句・属性である CREATE TABLE IN TABLESPACE を使います、データベース名と表スペース名を示すことで、容量、ロック、バッファープールの既存設計を引き継げます、新規領域を暗黙作成したくない運用で重要ですという関係があり、この区別で確認する名称は「IN」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLE IN TABLESPACE（DDL 句・属性</strong></p><p>検証目的: 上書分離のオプションについて、CREATE TABLE IN TABLESPACE は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020147の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLE IN TAを指定し、OSKB020147の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLE IN TA
CASE OSKB020147
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLE IN TA
CASE OSKB020147
SOURCE Db2 for z/OS
CREATE TABLE IN TAとOSKB020147が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020147を同じ出力で読み、上書分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020147
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020147
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020147
DSNV401IとOSKB020147が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLE IN TA と OSKB020147 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020147 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0130"><h3>CREATE TABLE ORGANIZE BY（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLE ORGANIZE BYは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表のアクセス傾向に合わせて、行指向やハッシュなどの編成をDDLで選びたい状況です。確認すべき指定の役割はどれですか。</p><ul class="kb-choices"><li>A. SMS属性</li><li>B. 初期区画</li><li>C. 権限取消</li><li>D. 編成方式 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表の編成方法を選ぶ指定なので、Dが答えです。行指向、ハッシュなどの方式により、読み取りや更新の性質が変わります。AはSMSの管理属性、Bは初期パーティション数、Cは権限の取り消しです。ワークロードに合う方式を選ぶことが重要です；背景にはデータの配置方法を選ぶ設計で、Db2 の SQL/DDL句・属性として CREATE TABLE ORGANIZE BY が表の編成を指定します、行編成、ハッシュ編成、列編成などの選択により、検索や更新の性質が変わります、ワークロードの読み取り傾向と更新頻度を見て選ぶ指定ですという関係があり、この区別で確認する名称は「ORGANIZE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLE ORGANIZE BY（DDL 句・属性）</strong></p><p>検証目的: 条件分離のオプションについて、CREATE TABLE ORGANIZE BY は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020149の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLE ORGANを指定し、OSKB020149の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLE ORGAN
CASE OSKB020149
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLE ORGAN
CASE OSKB020149
SOURCE Db2 for z/OS
CREATE TABLE ORGANとOSKB020149が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020149を同じ出力で読み、条件分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020149
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020149
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020149
DSNV401IとOSKB020149が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLE ORGAN と OSKB020149 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020149 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0131"><h3>CREATE TABLE PARTITION BY（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLE PARTITION BYは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 大きな表を範囲またはサイズで分割し、保守単位とアクセスパスを制御したい状況です。このDDL句が扱うものはどれですか。</p><ul class="kb-choices"><li>A. 権限付与</li><li>B. BP選択</li><li>C. 分割キー <span class="kb-ok">✅ 正解</span></li><li>D. ログ取消</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表データをどう分けるかを扱うため、Cが該当します。キーやサイズによって区画を作り、保守単位やアクセスパスに影響します。Aは権限を与える操作、Bはバッファープールの選択、Dは権限取消やログ操作ではありません。大容量表では分割方式が運用設計の中心になります；背景には表データの分割方法を決めるとき、CREATE TABLE PARTITION BY は Db2 の DDL オプションとしてパーティションの方式や境界を定義します、範囲分割やサイズ分割により、データの配置と保守単位が変わります、大きな表では、アクセスパスとユーティリティ実行単位を見ながら設計しますという関係があり、この区別で確認する名称は「PARTITION」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLE PARTITION BY（DDL 句・属性）</strong></p><p>検証目的: 出力分離のオプションについて、CREATE TABLE PARTITION BY は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020148の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLE PARTIを指定し、OSKB020148の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLE PARTI
CASE OSKB020148
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLE PARTI
CASE OSKB020148
SOURCE Db2 for z/OS
CREATE TABLE PARTIとOSKB020148が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020148を同じ出力で読み、出力分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020148
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020148
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020148
DSNV401IとOSKB020148が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLE PARTI と OSKB020148 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020148 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0132"><h3>CREATE TABLESPACE BUFFERPOOL（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE BUFFERPOOLは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表スペース PAYTS を作成するDDLで BP0 を明示し、ページキャッシュ領域を固定したい状況です。管理者がこの指定で制御している対象はどれですか。</p><ul class="kb-choices"><li>A. 使用BP名 <span class="kb-ok">✅ 正解</span></li><li>B. ロック単位</li><li>C. ロック上限</li><li>D. 圧縮利用可否</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 使用するBP名を決める内容なので、Aを選びます。表スペースのページをどのバッファープールへ置くかをDDLに書く指定であり、BP0 などの実在名を使います。Bはロックを取る粒度、Cはロック数の上限、Dは表データ圧縮の有無です。ページサイズとBP定義の整合を確認します；背景にはページキャッシュの割当を決める場面で、Db2 の SQL/DDL句・属性として CREATE TABLESPACE BUFFERPOOL を確認します、表スペースが使うバッファープール名を明示し、ページサイズや用途に合うプールへ置きます、誤った指定は作成エラーや I/O 効率低下につながるため、表スペース設計書と実在する BP 名を照合しますという関係があり、この区別で確認する名称は「BUFFERPOOL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0133"><h3>CREATE TABLESPACE COMPRESS（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE COMPRESSは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 履歴表のディスク使用量を抑えるため、表スペース作成時にデータ圧縮を有効にするかを決めたい状況です。この指定の対象はどれですか。</p><ul class="kb-choices"><li>A. 一意性</li><li>B. 付与先</li><li>C. トリガー時点</li><li>D. 圧縮利用 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表データの圧縮を使うかどうかを表すため、Dが該当します。格納効率を高められる反面、CPU使用量やユーティリティ処理時間も評価が必要です。Aは索引キーの一意性、Bは権限の付与先、Cはトリガーの起動時点です。大容量表では効果測定を行います；背景には保管効率を改善するときに Db2 の SQL/DDL句・属性として CREATE TABLESPACE COMPRESS が表データ圧縮の利用有無を示します、圧縮はディスク使用量を減らせます、一方でCPU使用量やユーティリティ処理への影響があるため、大容量表では効果測定と合わせて採用しますという関係があり、この区別で確認する名称は「COMPRESS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE COMPRESS（DDL 句・属性</strong></p><p>検証目的: 探索分離のオプションについて、CREATE TABLESPACE COMPRESS は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020146の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACE を指定し、OSKB020146の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE 
CASE OSKB020146
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE 
CASE OSKB020146
SOURCE Db2 for z/OS
CREATE TABLESPACE とOSKB020146が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020146を同じ出力で読み、探索分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020146
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020146
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020146
DSNV401IとOSKB020146が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE  と OSKB020146 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020146 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0134"><h3>CREATE TABLESPACE DSSIZE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE DSSIZEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 成長する表スペースについて、データセット単位の大きさをDDLでそろえ、バックアップ単位も読み替えたい状況です。対象になる指定はどれですか。</p><ul class="kb-choices"><li>A. 一意性</li><li>B. 発火時点</li><li>C. 信頼接続属性</li><li>D. 物理サイズ枠 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> データセットの大きさを設計する話であり、Dが正解です。表スペースやパーティションを構成する物理単位のサイズを見積もるために使います。Aは索引キーの重複防止、Bはトリガーの起動時点、Cは信頼接続の条件です。容量計画とリカバリー単位を合わせます；背景には物理データセットの大きさを見積もる作業では、Db2 の DDL オプションとして CREATE TABLESPACE DSSIZE を確認します、この値はパーティションや表スペースを構成するデータセットのサイズ設計に関係します、成長余地を広げると回復単位も大きくなるため、容量予測とバックアップ方針を合わせますという関係があり、この区別で確認する名称は「DSSIZE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE DSSIZE（DDL 句・属性）</strong></p><p>検証目的: 呼出分離のオプションについて、CREATE TABLESPACE DSSIZE は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020143の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACE を指定し、OSKB020143の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE 
CASE OSKB020143
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE 
CASE OSKB020143
SOURCE Db2 for z/OS
CREATE TABLESPACE とOSKB020143が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020143を同じ出力で読み、呼出分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020143
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020143
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020143
DSNV401IとOSKB020143が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE  と OSKB020143 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020143 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0135"><h3>CREATE TABLESPACE LOCKMAX（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE LOCKMAXは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 大量更新ジョブでロックエスカレーションの発生条件を見直しています。表スペースで許容するロック数の扱いを決める指定はどれですか。</p><ul class="kb-choices"><li>A. 区画数</li><li>B. ログ保存先</li><li>C. ロック上限 <span class="kb-ok">✅ 正解</span></li><li>D. 所属DB</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 許容するロック数の扱いを決める指定なので、Cを選定します。上限値またはシステム既定を使い、ロックエスカレーションの起きやすさに影響します。Aはパーティション数、Bはログ保存の運用、Dは表の所属先データベースです。粒度を決める指定とは別に確認します；背景にはロック数の膨張を抑える観点で、CREATE TABLESPACE LOCKMAX は Db2 の SQL/DDL句・属性に含まれる制御値です、表スペース内で許容するロック数、またはシステム既定の利用を指定します、大量更新バッチでは、エスカレーションの起きやすさと保護範囲を合わせて評価しますという関係があり、この区別で確認する名称は「LOCKMAX」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE LOCKMAX（DDL 句・属性）</strong></p><p>検証目的: 展開分離のオプションについて、CREATE TABLESPACE LOCKMAX は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020142の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACE を指定し、OSKB020142の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE 
CASE OSKB020142
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE 
CASE OSKB020142
SOURCE Db2 for z/OS
CREATE TABLESPACE とOSKB020142が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020142を同じ出力で読み、展開分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020142
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020142
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020142
DSNV401IとOSKB020142が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE  と OSKB020142 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020142 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0136"><h3>CREATE TABLESPACE LOCKSIZE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE LOCKSIZEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 更新処理が多い表スペースで、行単位にするかページ単位にするかをDDLで明示したい状況です。確認すべき指定の役割はどれですか。</p><ul class="kb-choices"><li>A. BP選択</li><li>B. ロック単位 <span class="kb-ok">✅ 正解</span></li><li>C. 区画上限</li><li>D. 索引配置順序</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ロックを取得する単位を選ぶ内容ですから、Bが合います。行、ページ、表スペースなどの粒度により、待ち時間と管理量が変わります。Aはバッファープールの選択、Cは増加型表スペースの上限、Dは索引の配置方針です。更新が多い表では待ちの増え方を見ます；背景には更新競合を設計するときに Db2 の DDL オプションである CREATE TABLESPACE LOCKSIZE がロック取得の単位を決めます、ROW、PAGE、TABLESPACE などの選択により、同時実行性と管理負荷のバランスが変わります、頻繁に更新される表では、SQL量と待ち時間を見ながら粒度を選定しますという関係があり、この区別で確認する名称は「LOCKSIZE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE LOCKSIZE（DDL 句・属性</strong></p><p>検証目的: 構文分離のオプションについて、CREATE TABLESPACE LOCKSIZE は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020141の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACE を指定し、OSKB020141の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE 
CASE OSKB020141
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE 
CASE OSKB020141
SOURCE Db2 for z/OS
CREATE TABLESPACE とOSKB020141が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020141を同じ出力で読み、構文分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020141
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020141
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020141
DSNV401IとOSKB020141が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE  と OSKB020141 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020141 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0137"><h3>CREATE TABLESPACE MAXPARTITIONS（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE MAXPARTITIONSは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> パーティション増加型の表スペースで、将来どこまで自動的に区画を増やせるかを設計しています。確認する指定の目的はどれですか。</p><ul class="kb-choices"><li>A. 表配置</li><li>B. 更新記録</li><li>C. 成長上限 <span class="kb-ok">✅ 正解</span></li><li>D. 発火条件</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 自動的に増やせる区画の限界を決める内容で、Cが正しいです。PBG 形式の成長余地を示すため、容量監視や将来拡張の前提になります。Aは表や表スペースの配置、Bは変更情報の記録、Dはトリガーを起動する条件です。運用監視のしきい値にも使います；背景には増加型の PBG 表スペースで自動追加の限界を決めるために、Db2 の CREATE TABLESPACE MAXPARTITIONS を確認します、データ増加に応じて区画は増えます、上限値は容量計画と監視しきい値の基準になります、表の成長見込みとストレージ保守の上限を同じ資料で確認しますという関係があり、この区別で確認する名称は「MAXPARTITIONS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0138"><h3>CREATE TABLESPACE NUMPARTS（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE NUMPARTSは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲分割の表スペースを作成するとき、最初からいくつの区画を持たせるかをDDLで指定したい状況です。どの内容を扱いますか。</p><ul class="kb-choices"><li>A. SMS属性束</li><li>B. 初期区画数 <span class="kb-ok">✅ 正解</span></li><li>C. BP名</li><li>D. 権限取消</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 作成時に用意する区画数を決める指定なので、Bを選びます。最初のパーティション数を定義し、将来の成長や保守単位に影響します。AはSMS関連の属性、Cはバッファープール名、Dは権限の取り消しです。キー範囲と容量予測を合わせて決めます；背景には分割表スペースを初期設計するときに Db2 の SQL/DDL句・属性である CREATE TABLESPACE NUMPARTS が作成時に用意するパーティション数を示します、少なすぎると成長時の制約になり、多すぎると管理対象が増えます、キー範囲、容量予測、保守単位を合わせて初期値を決めますという関係があり、この区別で確認する名称は「NUMPARTS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0139"><h3>CREATE TABLESPACE SEGSIZE（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TABLESPACE SEGSIZEは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ユニバーサル表スペースで、セグメントに含めるページ数を指定して空き領域の管理単位を調整したい状況です。該当する役割はどれですか。</p><ul class="kb-choices"><li>A. セグメント幅 <span class="kb-ok">✅ 正解</span></li><li>B. 変更捕捉</li><li>C. 所属DB</li><li>D. 索引ピース容量</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> セグメント内のページ数を示すため、Aが適切です。表スペース内の空き領域管理や配置効率に関係する値として扱います。Bは表変更の記録、Cは表を置くデータベース、Dは大きな索引を分ける単位です。表スペース形式による制約も確認します；背景にはセグメント管理の粒度を決めるとき、CREATE TABLESPACE SEGSIZE は SQL/DDL句・属性の中で表スペース内のセグメント構成を指定します、値はセグメントに含めるページ数として扱われ、表スペース形式の制約も受けます、PBG やユニバーサル表スペースでは、空き領域と配置効率を見る材料になりますという関係があり、この区別で確認する名称は「SEGSIZE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE SEGSIZE（DDL 句・属性）</strong></p><p>検証目的: 置換分離のオプションについて、CREATE TABLESPACE SEGSIZE は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句とのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020144の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換分離のオプションの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACE を指定し、OSKB020144の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE 
CASE OSKB020144
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE 
CASE OSKB020144
SOURCE Db2 for z/OS
CREATE TABLESPACE とOSKB020144が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020144を同じ出力で読み、置換分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020144
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020144
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020144
DSNV401IとOSKB020144が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE  と OSKB020144 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020144 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0140"><h3>CREATE TRIGGER timing/event（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>CREATE TRIGGER timing/eventは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表 PAYROLL への INSERT 後に監査用の処理を自動実行したい状況です。DDLで定義する中心要素はどれですか。</p><ul class="kb-choices"><li>A. 表配置</li><li>B. 索引用BP</li><li>C. 権限取消</li><li>D. 発火条件 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> トリガーを動かす条件を示すため、Dが正解です。操作の前後やINSERTなどのイベントを組み合わせ、自動処理を起動します。Aは表の配置先、Bは索引用バッファープール、Cは権限取り消しです。自動処理は便利です。一方で、監査内容と副作用を確認して定義します；背景には表操作に連動して処理を走らせる設計では、CREATE TRIGGER timing/event が Db2 の DDL オプションとしていつ、どの操作でトリガーを起動するかを指定します、BEFORE、AFTER、INSERT、UPDATE、DELETE などを組み合わせます、副作用と権限を確認し、監査や整合性維持に使いますという関係があり、この区別で確認する名称は「timing/event」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0141"><h3>CREATE TRUSTED CONTEXT attributes（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 上級</p><p>CREATE TRUSTED CONTEXT attributesは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 特定サーバーからの接続のみを trusted connection として扱い、認可IDやロール利用の条件をDDLに書きたい状況です。扱うものはどれですか。</p><ul class="kb-choices"><li>A. 索引近接配置</li><li>B. 表圧縮</li><li>C. 信頼接続条件 <span class="kb-ok">✅ 正解</span></li><li>D. 区画数</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 接続を信頼扱いにする条件を定義するので、Cを選びます。認可ID、接続元、ロール利用などを組み合わせ、代理利用を許す範囲を絞ります。Aは索引順に近い配置、Bは表データ圧縮、Dはパーティション数です。条件を広げすぎないことが重要です；背景にはアプリケーションサーバー経由の接続を制御する場合、CREATE TRUSTED CONTEXT attributes は Db2 の SQL/DDL句・属性として信頼接続に使う条件を定義します、システム認可ID、接続元、ロール利用などを組み合わせます、サーバーからの代理利用を許す設計では、条件を狭く保つことが重要ですという関係があり、この区別で確認する名称は「attributes」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0142"><h3>GRANT privilege（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>GRANT privilegeは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ロール PAYREAD へ PAYROLL 表の参照を認め、アプリケーションがSELECTできるようにしたい状況です。使うSQLの役割はどれですか。</p><ul class="kb-choices"><li>A. 権限付与 <span class="kb-ok">✅ 正解</span></li><li>B. 権限取消</li><li>C. 区画作成</li><li>D. 索引分割単位</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 操作権限を与える内容なので、Aを選びます。対象オブジェクト、権限名、受け手を指定して利用を認めます。Bは既存権限の取り消し、Cは表スペースの区画作成、Dは大きな索引の分割設計です。監査では誰に何を認めたかを確認します；背景にはアクセス権を与える操作として、GRANT が Db2 の SQL/DDL句・属性として表、ビュー、ロールなどへの権限付与を行います、SELECT や INSERT など対象権限と受け手を明示します、監査では、誰に何の操作を認めたかをDDLと権限一覧で照合しますという関係があり、この区別で確認する名称は「GRANT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0143"><h3>REVOKE privilege（DDL句・属性）</h3><p class="kb-meta">分類: SQL/DDL句・属性 &gt; DDLオプション ・ 難易度: 中級</p><p>REVOKE privilegeは、SQLまたはDDLでDb2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 旧ロール OLDREAD から PAYROLL 表の参照権限を外し、使われなくなったアクセスパスを閉じたい状況です。該当する操作はどれですか。</p><ul class="kb-choices"><li>A. BP選択</li><li>B. 権限取消 <span class="kb-ok">✅ 正解</span></li><li>C. 表分割</li><li>D. 圧縮利用</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 不要な権限を含めない操作であり、Bが該当します。過去に与えた参照や更新の権限を取り消し、使われなくなった経路を閉じます。Aはバッファープール選択、Cは表の分割設計、Dは圧縮利用の指定です。依存関係や監査記録を確認して実行します；背景には不要になったアクセス権を含めないとき、REVOKE は Db2 の DDL オプション群と同じ権限管理の文脈で使用します、過去に付与した表権限やロール権限を取り消し、不要な利用経路を閉じます、依存するビューやパッケージへの影響も確認してから実行しますという関係があり、この区別で確認する名称は「REVOKE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Introduction / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REVOKE privilege（DDL 句・属性）</strong></p><p>検証目的: 警告分離の（ 句・属性について、REVOKE privilegeは、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句との違いを整理します。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020157の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、警告分離の（ 句・属性の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にREVOKE privilege（Dを指定し、OSKB020157の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND REVOKE privilege（D
CASE OSKB020157
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM REVOKE privilege（D
CASE OSKB020157
SOURCE Db2 for z/OS
REVOKE privilege（DとOSKB020157が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020157を同じ出力で読み、警告分離の（ 句・属性の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020157
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020157
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020157
DSNV401IとOSKB020157が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の REVOKE privilege（D と OSKB020157 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020157 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


## アプリケーション実行


<section class="kb-item" id="c07-i0144"><h3>BIND PACKAGE</h3><p class="kb-meta">分類: アプリケーション実行 ・ 難易度: 中級</p><p>Db2 for z/OS の アプリケーション実行で扱うBIND PACKAGEは、SQL を含むプログラムの DBRM などからパッケージを作成または更新する操作です。アクセスパス、所有者、VALIDATE などの指定が実行時の挙動に影響します。性能変更や移行後の差異を追うときは BIND オプションを確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


<section class="kb-item" id="c07-i0145"><h3>パッケージ</h3><p class="kb-meta">分類: アプリケーション実行 ・ 難易度: 中級</p><p>Db2 for z/OS の アプリケーション実行で扱うパッケージは、SQL 文のアクセスパスと実行属性を保持する Db2 の実行単位です。プログラム変更後の BIND、無効化、再バインドがアプリケーション実行に影響します。障害時はプログラム名だけでなく、コレクションとパッケージ名を確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認のパッケージでパッケージの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. パッケージの出力を取らず区切確認のパッケージの説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. -DISPLAY THREAD(*)を省略して区切確認のパッケージの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認のパッケージへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠ではパッケージは「区切確認のパッケージに関係する定義値と表示行を照合する区切確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡ではパッケージの属性行と DSNV401I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出ではパッケージを Db2 for z/OS の運用手順で確認し、初出名は区切確認初出です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>パッケージ</strong></p><p>検証目的: 区切確認のパッケージについて、Db2 for z/OS の アプリケーション実行で扱うパッケージは、SQL 文のアクセスパスと実行属性を保持する Db2 の実行単位です。プログラム変更後の BIND、無に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD(*) を入力し、区切確認のパッケージの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にパッケージを指定し、OSKB010010の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND パッケージ
CASE OSKB010010
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM パッケージ
CASE OSKB010010
SOURCE Db2 for z/OS
パッケージとOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010010を同じ出力で読み、区切確認のパッケージの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
CASE OSKB010010
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010010
-DISPLAY THREAD(*)
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010010
DSNV401IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD(*) が画面・出力に表示されること
② ステップ2 の パッケージ と OSKB010010 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


<section class="kb-item" id="c07-i0146"><h3>プラン</h3><p class="kb-meta">分類: アプリケーション実行 ・ 難易度: 中級</p><p>Db2 for z/OS の アプリケーション実行で扱うプランは、アプリケーションが Db2 資源を使うために割り当てる実行時の単位です。パッケージリストや許可と結び付き、DSN コマンドやバッチ実行で参照されます。古い設計ではプラン依存が強いため、移行時にパッケージとの関係を確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認のプランでデータベース管理の運用確認を行います。プランの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. Db2 for z/OS と無関係な一覧で範囲確認のプランを確認した扱いにする。</li><li>B. DSNV401I の有無を確認せず範囲確認のプランを正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. プランの属性行を読まず範囲確認のプランの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠ではプランは「Db2 for z/OS でプランの扱いを記録する範囲確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡ではプランの表示結果と DSNV401I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料ではプランの使い方を出典欄から追跡し、資料名は範囲確認資料です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プラン</strong></p><p>検証目的: 範囲確認のプランについて、Db2 for z/OS の アプリケーション実行で扱うプランは、アプリケーションが Db2 資源を使うために割り当てる実行時の単位です。パッケージリストや許可と結び付き、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD(*) を入力し、範囲確認のプランの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にプランを指定し、OSKB010011の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND プラン
CASE OSKB010011
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM プラン
CASE OSKB010011
SOURCE Db2 for z/OS
プランとOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010011を同じ出力で読み、範囲確認のプランの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
CASE OSKB010011
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010011
-DISPLAY THREAD(*)
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010011
DSNV401IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD(*) が画面・出力に表示されること
② ステップ2 の プラン と OSKB010011 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


## アプリケーション開発・接続方式 > Javaサーバ支援


<section class="kb-item" id="c07-i0147"><h3>Java stored procedure support</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; Javaサーバ支援 ・ 難易度: 中級</p><p>Java stored procedure supportは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Javaで書いたルーチンをDb2側で実行するため、WLM環境、JAVAENV、DSNTIJRTによる定義を整えます。対象はどれですか。</p><ul class="kb-choices"><li>A. SPUFI file input</li><li>B. ODBC/CLI API connection</li><li>C. Java stored procedure support <span class="kb-ok">✅ 正解</span></li><li>D. SQL communication area</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> JavaルーチンをWLM管理環境で動かす支援はCです。Aは入力ファイルのSQLを対話実行します。BはC系アプリケーションのAPI接続です。Dは実行状態を受けるSQL領域で、Java実行環境の設定ではありません；背景にはJavaルーチン実行支援は、アプリケーション開発・接続方式のJavaサーバ支援としてWLM管理のstored procedure address spaceを使います、JAVAENVのCLASSPATH、IBM Data Server Driver、DSNTIJRTによるルーチン定義とpackage bindが関わります、Java実行環境とDb2側定義の両方をそろえますという関係があり、この区別で確認する名称は「procedure」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details></section>


## アプリケーション開発・接続方式 > クライアントAPI・Java


<section class="kb-item" id="c07-i0148"><h3>DB2Binder</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; クライアントAPI・Java ・ 難易度: 中級</p><p>DB2Binderは、アプリケーション開発・接続方式の中でクライアントAPI・Javaに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> IBM Data Server Driver for JDBC and SQLJが使うpackageをbindし、必要に応じてEXECUTE権限も設定します。使うユーティリティはどれですか。</p><ul class="kb-choices"><li>A. DB2Binder <span class="kb-ok">✅ 正解</span></li><li>B. SPUFI file input</li><li>C. DSNTIAUL unload sample</li><li>D. SQL communication area</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ドライバ用packageをbindする役割はAです。Bは対話入力のSQLを実行する機能です。Cは表データを取り出す抽出サンプルです。Dは実行状態を受け取るSQL領域で、packageのbindは行いません；背景にはDB2Binder は、クライアントAPI・JavaでIBM Data Server Driver for JDBC and SQLJが使うDb2 packageをbindするためのツールです、必要に応じてEXECUTE権限をPUBLICへ付与し、generic bind optionsでDb2 for z/OS固有の指定を渡します、Java側のSQL実行基盤を整えますという関係があり、この区別で確認する名称は「DB2Binder」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details></section>


<section class="kb-item" id="c07-i0149"><h3>JCC driver plan</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; クライアントAPI・Java ・ 難易度: 中級</p><p>JCC driver planは、アプリケーション開発・接続方式の中でクライアントAPI・Javaに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Javaドライバから接続する際、DB2BinderやSQLJ packageをまとめる実行時plan名を指定します。この設定対象はどれですか。</p><ul class="kb-choices"><li>A. DCLGEN generated copybook</li><li>B. JCC driver plan <span class="kb-ok">✅ 正解</span></li><li>C. DSNTEP2 SYSIN SQL stream</li><li>D. ODBC link-edit sidedeck</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ドライバが参照するplan名の設定なので、正解はBです。Aは表定義の宣言部です。Cはバッチで流すSQL入力データです。Dはリンク編集で使うODBC定義で、JCCのplan名管理とは別です。接続時のplanNameと合わせます；背景にはJCC driver plan は、クライアントAPI・JavaでDB2BinderやSQLJ packageをまとめる実行時のplan名です、db2.jcc.planNameプロパティやConnection/DataSourceのplanNameで指定できます、ドライバ接続で参照するplanとpackageの対応をそろえますという関係があり、この区別で確認する名称は「driver」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JCC driver plan</strong></p><p>検証目的: 順序追跡のクライアント ・について、JCC driver planは、アプリケーション開発・接続方式の中でクライアント API ・ Javaに関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、順序追跡のクライアント ・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にJCC driver planを指定し、OSKB010055の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND JCC driver plan
CASE OSKB010055
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM JCC driver plan
CASE OSKB010055
SOURCE Db2 for z/OS
JCC driver planとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010055を同じ出力で読み、順序追跡のクライアント ・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010055
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010055
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010055
DSNV401IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の JCC driver plan と OSKB010055 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0150"><h3>JDBC</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; クライアントAPI・Java ・ 難易度: 中級</p><p>JDBCは、アプリケーション開発・接続方式の中でクライアントAPI・Javaに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Javaプログラムから標準APIでSQLを実行します。SQLJの変換工程を使わず、通常のJavaコンパイルで準備します。該当する方式はどれですか。</p><ul class="kb-choices"><li>A. SQLJ</li><li>B. DSNTIAUL</li><li>C. JDBC <span class="kb-ok">✅ 正解</span></li><li>D. DCLGEN</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Javaの標準データベースAPIで実行する方式に当たるため、Cを選びます。AはJavaで静的SQLを扱う方式です。Bはデータ抽出用サンプルです。Dはホスト言語向け宣言部生成で、Java API接続ではありません；背景にはJava標準APIである JDBC は、クライアントAPI・JavaでJavaアプリケーションがDb2へ接続する方式です、この方式のみを使うプログラムは通常のJavaプログラムと同様にjavacでコンパイルし、SQLJのようなprecompileやbind工程を必要としません、実行時の接続プロパティ管理が重要ですという関係があり、この区別で確認する名称は「JDBC」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JDBC</strong></p><p>検証目的: 記録追跡のクライアント ・について、JDBC は、アプリケーション開発・接続方式の中でクライアント API ・ Javaに関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、記録追跡のクライアント ・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にJDBCを指定し、OSKB010053の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND JDBC
CASE OSKB010053
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM JDBC
CASE OSKB010053
SOURCE Db2 for z/OS
JDBCとOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010053を同じ出力で読み、記録追跡のクライアント ・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010053
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010053
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010053
DSNV401IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の JDBC と OSKB010053 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010053 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0151"><h3>ODBC/CLI</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; クライアントAPI・Java ・ 難易度: 中級</p><p>ODBC/CLIは、アプリケーション開発・接続方式の中でクライアントAPI・Javaに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> C言語系アプリケーションがAPI呼び出しでDb2へ接続し、実行時にドライバをロードします。この接続方式はどれですか。</p><ul class="kb-choices"><li>A. SQLJ static Java SQL</li><li>B. ODBC/CLI <span class="kb-ok">✅ 正解</span></li><li>C. DSNTEP2 batch SQL sample</li><li>D. SQL communication area</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ドライバ経由のAPI接続方式はBです。AはJavaの静的SQL向け方式です。CはバッチでSQLを流す実行サンプルです。Dは実行結果を受けるSQL通信領域で、接続APIではありません。CAFやRRSAFの選択も関係します；背景にはODBC/CLI は、クライアントAPI・Javaの周辺でC言語系アプリケーションがDb2へ接続するAPIです、Db2 for z/OSではODBC driver managerに相当するCLI/ODBC driverがアプリケーションのアドレス空間にロードされます、接続方式にはCAFやRRSAFが関わりますという関係があり、この区別で確認する名称は「ODBC/CLI」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBC ・ CLI</strong></p><p>検証目的: 優先追跡の・について、ODBC/CLI は、アプリケーション開発・接続方式の中でクライアント API ・ Javaに関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、優先追跡の・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にODBC ・ CLIを指定し、OSKB010052の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ODBC ・ CLI
CASE OSKB010052
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ODBC ・ CLI
CASE OSKB010052
SOURCE Db2 for z/OS
ODBC ・ CLIとOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010052を同じ出力で読み、優先追跡の・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010052
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010052
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010052
DSNV401IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ODBC ・ CLI と OSKB010052 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010052 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0152"><h3>SQLJ</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; クライアントAPI・Java ・ 難易度: 中級</p><p>SQLJは、アプリケーション開発・接続方式の中でクライアントAPI・Javaに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Javaソースに静的SQLを記述し、serialized profileを作ってDb2用packageをbindします。この方式はどれですか。</p><ul class="kb-choices"><li>A. JDBC</li><li>B. ODBC/CLI</li><li>C. DB2Binder</li><li>D. SQLJ <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Javaで静的SQLを扱い、profileとpackageを準備する方式はDです。Aは動的SQL中心のJava APIです。BはC系API接続です。Cはドライバ用packageをbindするユーティリティで、言語方式そのものではありません；背景にはJava静的SQLを扱う SQLJ は、クライアントAPI・JavaでJavaアプリケーションに静的SQLを記述する方式です、ソース変換でgenerated Java sourceやserialized profileを作り、db2sqljcustomizeやdb2sqljbindでDb2向けpackageを用意します、準備工程はJDBCより多い点に注意しますという関係があり、この区別で確認する名称は「SQLJ」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SQLJ</strong></p><p>検証目的: 比較追跡のクライアント ・について、SQLJ は、アプリケーション開発・接続方式の中でクライアント API ・ Javaに関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較追跡のクライアント ・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSQLJを指定し、OSKB010054の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SQLJ
CASE OSKB010054
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SQLJ
CASE OSKB010054
SOURCE Db2 for z/OS
SQLJとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010054を同じ出力で読み、比較追跡のクライアント ・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010054
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010054
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010054
DSNV401IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SQLJ と OSKB010054 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


## アプリケーション開発・接続方式 > 動的SQL・対話実行ツール


<section class="kb-item" id="c07-i0153"><h3>DSNTEP2</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 動的SQL・対話実行ツール ・ 難易度: 中級</p><p>DSNTEP2は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> バッチジョブでは、JCLからSQL文を読み込み、対話画面ではなくDDLや確認SQLを実行します。該当するサンプルプログラムはどれですか。</p><ul class="kb-choices"><li>A. DSNTIAD sample runner</li><li>B. DSNTIAUL unload sample</li><li>C. SPUFI file input</li><li>D. DSNTEP2 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ジョブ制御でSQL文を処理するバッチ用サンプルとしてDを選びます。Aは別の実行補助プログラムです。BはLOAD互換形式へ表データを取り出します。CはISPFでSQLファイルを対話実行する機能です。入力メンバーも確認します；背景にはバッチでSQLを流す DSNTEP2 は、動的SQL・対話実行ツールのバッチ実行サンプルです、ジョブのSYSINなどに置いたSQL文を読み取り、Db2へ渡す前に文の前処理を行って実行します、定義変更や確認用SQLをジョブ化する場合に使われ、対話画面を開けない運用でも証跡を残しやすくなりますという関係があり、この区別で確認する名称は「DSNTEP2」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DSNTEP2</strong></p><p>検証目的: 範囲追跡の動的 ・対話実行ツールについて、DSNTEP2 は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、範囲追跡の動的 ・対話実行ツールの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTEP2を指定し、OSKB010051の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DSNTEP2
CASE OSKB010051
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DSNTEP2
CASE OSKB010051
SOURCE Db2 for z/OS
DSNTEP2とOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010051を同じ出力で読み、範囲追跡の動的 ・対話実行ツールの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010051
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010051
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010051
DSNV401IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DSNTEP2 と OSKB010051 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010051 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0154"><h3>DSNTIAUL</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 動的SQL・対話実行ツール ・ 難易度: 中級</p><p>DSNTIAULは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表の行を取り出し、LOAD utilityで戻しやすい形式と制御文を作ります。対象のサンプルプログラムはどれですか。</p><ul class="kb-choices"><li>A. DSNTIAUL <span class="kb-ok">✅ 正解</span></li><li>B. DSNTEP2</li><li>C. SPUFI</li><li>D. DCLGEN</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 戻し込み互換形式で表データを取り出す用途に当たるため、Aを選びます。BはバッチSQLを実行します。Cは入力ファイルのSQLを対話実行します。Dは表定義からプログラム用の宣言部を作る支援機能です。戻し込み用制御文を作る点も判断材料です；背景にはデータ抽出用の DSNTIAUL は、動的SQL・対話実行ツールの範囲で使われるアンロード用の提供サンプルです、最大100表までの行を取り出し、LOAD utilityと互換の形式や制御文を生成できます、アンロードユーティリティの代替として使う場面がありますという関係があり、この区別で確認する名称は「DSNTIAUL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details></section>


<section class="kb-item" id="c07-i0155"><h3>SPUFI</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 動的SQL・対話実行ツール ・ 難易度: 中級</p><p>SPUFIは、アプリケーション開発・接続方式の中で動的SQL・対話実行ツールに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ISPF上でファイルに書いたSQLをすぐ実行します。ただしhost variableやSQLCAを前提にできません。使う機能はどれですか。</p><ul class="kb-choices"><li>A. DSNTIAUL unload program</li><li>B. precompile DBRM creation</li><li>C. SPUFI <span class="kb-ok">✅ 正解</span></li><li>D. DB2Binder package utility</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cでは、ISPFのSQL入力メンバーを読み取り、その場でDb2へ文を発行します。Aは表データのアンロードに使います。Bは埋め込みSQLの準備工程です。DはJavaドライバ用パッケージをbindするユーティリティです；背景にはファイル入力型のSPUFIは、動的SQL・対話実行ツールとしてSQL文を準備し、Db2へ発行します、入力された文は対話的に処理されるため、host variableやparameter marker、SQLCAを前提にできません、検証用のSQLをすぐ流せる一方、業務バッチの代替にはしませんという関係があり、この区別で確認する名称は「SPUFI」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details></section>


<section class="kb-item" id="c07-i0156"><h3>dynamic SQL</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 動的SQL・対話実行ツール ・ 難易度: 中級</p><p>dynamic SQLは、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行うSQL実行要素です。動的SQL・対話実行ツールでは、対象行、トランザクション境界、エラー時に戻せる範囲を意識して扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 画面入力に応じてSQL文字列を組み立て、プログラム実行中にPREPAREして実行します。この方式はどれですか。</p><ul class="kb-choices"><li>A. static SQL</li><li>B. dynamic SQL <span class="kb-ok">✅ 正解</span></li><li>C. DCLGEN</li><li>D. SQLJ</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 実行中にSQL文を準備する方式としてBが該当します。Aは実行前に文を準備します。Cは宣言部を生成する支援です。DはJavaで静的SQLを扱う方式で、単純な実行時文字列準備とは別です。入力値の検証も必要です；背景には実行時に文を組み立てる dynamic SQL は、動的SQL・対話実行ツールの基礎です、アプリケーションは実行中にSQL文字列を準備し、必要に応じてparameter markerへ値を与えて実行します、入力内容の検証と権限管理を怠ると、予期しない文が実行されますという関係があり、この区別で確認する名称は「dynamic」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>dynamic SQL</strong></p><p>検証目的: 区切追跡の動的 ・対話実行ツールについて、dynamic SQL は、アプリケーションや対話実行でデータ参照、更新、確定、取消しを行う SQL 実行要素です。動的 SQL ・対話実行ツールでは、対象行、トランザクション境界、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切追跡の動的 ・対話実行ツールの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にdynamic SQLを指定し、OSKB010050の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND dynamic SQL
CASE OSKB010050
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM dynamic SQL
CASE OSKB010050
SOURCE Db2 for z/OS
dynamic SQLとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010050を同じ出力で読み、区切追跡の動的 ・対話実行ツールの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010050
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010050
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010050
DSNV401IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の dynamic SQL と OSKB010050 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


## アプリケーション開発・接続方式 > 静的SQL開発


<section class="kb-item" id="c07-i0157"><h3>DCLGEN</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 静的SQL開発 ・ 難易度: 中級</p><p>DCLGENは、アプリケーション開発・接続方式の中で静的SQL開発に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表やビューの列定義から、アプリケーションで使う宣言部やcopybookを生成します。利用する支援機能はどれですか。</p><ul class="kb-choices"><li>A. SQL communication area</li><li>B. precompile DBRM creation</li><li>C. DB2Binder package utility</li><li>D. DCLGEN <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表定義に対応した宣言部を作る支援はDです。AはSQL実行結果の状態を受け取ります。Bは埋め込みSQLを取り出してDBRMを作ります。CはJDBC/SQLJ用パッケージをbindする管理ツールです。列の型合わせにも使います；背景には表定義をプログラム側へ反映する DCLGEN は、静的SQL開発で表やビューの宣言を生成します、列名、データ型、ホスト変数宣言をcopybookなどにまとめ、プログラムと表定義のずれを減らします、生成物を使っても、業務ロジックに合わせた確認は必要ですという関係があり、この区別で確認する名称は「DCLGEN」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DCLGEN</strong></p><p>検証目的: 出力追跡の静的 開発について、DCLGEN は、アプリケーション開発・接続方式の中で静的 SQL 開発に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力追跡の静的 開発の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDCLGENを指定し、OSKB010048の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DCLGEN
CASE OSKB010048
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DCLGEN
CASE OSKB010048
SOURCE Db2 for z/OS
DCLGENとOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010048を同じ出力で読み、出力追跡の静的 開発の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010048
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010048
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010048
DSNV401IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DCLGEN と OSKB010048 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0158"><h3>SQLCA/SQLCODE handling</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 静的SQL開発 ・ 難易度: 中級</p><p>SQLCA/SQLCODE handlingは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> プログラム実行後に、SQLCODEの値を見て成功、警告、エラーを分岐します。この処理対象はどれですか。</p><ul class="kb-choices"><li>A. SQLCA <span class="kb-ok">✅ 正解</span></li><li>B. DCLGEN generated declarations</li><li>C. SPUFI input/output listing</li><li>D. ODBC link-edit sidedeck</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 状態コードを受け取る通信領域を見るため、Aを選びます。Bは宣言部を生成する支援です。Cは対話入力のSQLを実行する手段です。Dはリンク時に使うODBC定義で、実行結果判定の領域ではありません。異常時の分岐に使います；背景には実行結果を受け取る SQLCA/SQLCODE handling は、静的SQL開発でSQL文の成功、警告、例外を判断する処理です、通信領域には SQLCODE などの状態情報が入り、アプリケーションは値に応じて継続、再試行、異常処理を選びます、対話入力のSQLとは扱いが異なりますという関係があり、この区別で確認する名称は「SQLCA/SQLCODE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SQLCA ・ SQLCODE handling</strong></p><p>検証目的: 条件追跡の・について、SQLCA/SQLCODE handlingは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件追跡の・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSQLCA ・ SQLCODE haを指定し、OSKB010049の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SQLCA ・ SQLCODE ha
CASE OSKB010049
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SQLCA ・ SQLCODE ha
CASE OSKB010049
SOURCE Db2 for z/OS
SQLCA ・ SQLCODE haとOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010049を同じ出力で読み、条件追跡の・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010049
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010049
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010049
DSNV401IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SQLCA ・ SQLCODE ha と OSKB010049 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0159"><h3>host variable</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 静的SQL開発 ・ 難易度: 中級</p><p>host variableは、アプリケーション開発・接続方式の中で静的SQL開発に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 検索条件やSELECT結果を、埋め込みSQLとプログラム側のデータ項目の間で受け渡しします。この指定を何と呼びますか。</p><ul class="kb-choices"><li>A. parameter marker</li><li>B. host variable <span class="kb-ok">✅ 正解</span></li><li>C. SQL communication area</li><li>D. DCLGEN declaration member</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> プログラムのデータ項目をSQL文から参照する指定なので、該当するのはBです。Aは動的SQLで値を後から割り当てる目印です。Cは実行結果を受ける通信領域です。Dは表定義から宣言部を生成する支援機能です；背景にはホスト言語側のデータ項目は、静的SQL開発でアプリケーションのデータ領域とSQLをつなぎます、埋め込みSQLではコロン付きの名前で参照され、SELECT結果の受け取りや条件値の受け渡しに使われます、対話SQLでは文脈がないため使えません、宣言と列定義の整合も確認しますという関係があり、この区別で確認する名称は「variable」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>host variable</strong></p><p>検証目的: 探索追跡の静的 開発について、host variableは、アプリケーション開発・接続方式の中で静的 SQL 開発に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索追跡の静的 開発の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にhost variableを指定し、OSKB010046の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND host variable
CASE OSKB010046
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM host variable
CASE OSKB010046
SOURCE Db2 for z/OS
host variableとOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010046を同じ出力で読み、探索追跡の静的 開発の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010046
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010046
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010046
DSNV401IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の host variable と OSKB010046 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0160"><h3>precompiler</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 静的SQL開発 ・ 難易度: 中級</p><p>precompilerは、アプリケーション開発・接続方式の中で静的SQL開発に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ソース準備時に埋め込みSQLを処理し、修正済みソースとDBRMを作成します。この準備工程で使う機能はどれですか。</p><ul class="kb-choices"><li>A. SPUFI file input</li><li>B. DCLGEN declaration generator</li><li>C. precompiler <span class="kb-ok">✅ 正解</span></li><li>D. DSNTIAUL unload sample</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ソースからSQLを取り出してDBRMを作る工程はCです。Aは入力ファイルを対話実行する機能です。Bは表や列の宣言を生成します。DはLOAD互換形式で表データを取り出す抽出用プログラムです。実行前のbind入力を作る点が判断材料です；背景には埋め込み文を取り出すプリコンパイル処理は、静的SQL開発でソース内のSQLを処理します、処理後はホスト言語用に修正されたソースと、BINDで使うDBRMが生成されます、Db2 coprocessorを使う場合は、同等の処理をコンパイラ工程と連携させますという関係があり、この区別で確認する名称は「precompiler」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>precompiler</strong></p><p>検証目的: 上書追跡の静的 開発について、precompilerは、アプリケーション開発・接続方式の中で静的 SQL 開発に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書追跡の静的 開発の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にprecompilerを指定し、OSKB010047の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND precompiler
CASE OSKB010047
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM precompiler
CASE OSKB010047
SOURCE Db2 for z/OS
precompilerとOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010047を同じ出力で読み、上書追跡の静的 開発の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010047
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010047
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010047
DSNV401IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の precompiler と OSKB010047 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div></details></section>


<section class="kb-item" id="c07-i0161"><h3>static SQL</h3><p class="kb-meta">分類: アプリケーション開発・接続方式 &gt; 静的SQL開発 ・ 難易度: 中級</p><p>static SQLは、アプリケーション開発・接続方式の中で静的SQL開発に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 アプリケーションからDb2へ接続/実行する方式として扱い、SQL文法やBIND詳細とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 業務プログラムでは、COBOLなどのソースにSQL文を埋め込み、実行前の準備工程でDBRM化してBINDします。採用しているSQL方式はどれですか。</p><ul class="kb-choices"><li>A. static SQL <span class="kb-ok">✅ 正解</span></li><li>B. dynamic SQL prepared at run time</li><li>C. SPUFI file input</li><li>D. ODBC/CLI API connection</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 実行前にSQLを準備してpackageやplanへ結び付ける方式はAです。Bは実行中に文を準備します。CはISPFで入力ファイルを処理します。Dは接続APIを使う方式で、埋め込みSQLの準備工程そのものではありません；背景には埋め込みSQLを事前準備する static SQL は、静的SQL開発の中心になる方式です、ソース内のSQL文は、プリコンパイルまたはコプロセッサ処理、コンパイル、リンク、BINDを経て実行時資源に結び付きます、実行前にアクセスパスを固定しやすい一方、変更時は再準備が必要ですという関係があり、この区別で確認する名称は「static」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction.pdf p.261 / Db2_zOS_AppProg_SQL_Guide.pdf p.469 / Db2_zOS_AppProg_SQL_Guide.pdf p.884 / Db2_zOS_SQL_Reference.pdf p.1163 / Db2_zOS_AppProg_SQL_Guide.pdf p.1052 / Db2_zOS_AppProg_Java.pdf p.528 / Db2_zOS_AppProg_Java.pdf p.539 / Db2_zOS_ODBC.pdf p.16</p></div></details></section>


## カタログ・統計・メタデータ > カタログ・ディレクトリ


<section class="kb-item" id="c07-i0162"><h3>Db2 directory objects</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ・ディレクトリ ・ 難易度: 初級</p><p>Db2 directory objectsは、カタログ・統計・メタデータの中でカタログ・ディレクトリに関わるDb2技術項目です。役割、関連するDb2構成要素、運用者が確認する代表的な状態。一方で、個別コマンドやSQL文の詳細。 Db2メタデータと統計情報として扱い、SQL文法やユーティリティ手順とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常運用中にDb2自身が使う内部情報を保持し、利用者がSQLで広く参照する対象とは分けて管理します。この領域はどれですか。</p><ul class="kb-choices"><li>A. catalog表群</li><li>B. directory内部情報 <span class="kb-ok">✅ 正解</span></li><li>C. PLAN_TABLE行</li><li>D. RUNSTATS profile</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 内部運用情報を保持する領域として、Bを選びます。定義照会のAはcatalog表群、説明結果のCは計画表、収集条件のDは統計profileです。利用者照会用のcatalogとは用途を分けます。運用中にDb2が読む点が特徴です；背景にはDb2が通常運用に使う内部情報として、directory objects はカタログ・ディレクトリの重要な構成要素です、ログ範囲、DBD、packageの実行時情報など、システムが参照する情報を保持します、catalogのように利用者がSQLで広く参照する表群とは扱いが異なりますという関係があり、この区別で確認する名称は「directory」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Db2 directory objects</strong></p><p>検証目的: 展開判定のカタログ・ディレクトリについて、Db2 directory objectsは、カタログ・統計・メタデータの中でカタログ・ディレクトリに関わる Db2技術項目です。役割、関連する Db2構成要素、運用者が確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開判定のカタログ・ディレクトリの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDb2 directory objeを指定し、OSKB010082の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND Db2 directory obje
CASE OSKB010082
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM Db2 directory obje
CASE OSKB010082
SOURCE Db2 for z/OS
Db2 directory objeとOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010082を同じ出力で読み、展開判定のカタログ・ディレクトリの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010082
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010082
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010082
DSNV401IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の Db2 directory obje と OSKB010082 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0163"><h3>SYSCOPY</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ・ディレクトリ ・ 難易度: 中級</p><p>SYSCOPYは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表スペースのimage copy履歴やLOAD/REORG履歴を確認し、回復時に使うコピー候補を判断します。確認対象はどれですか。</p><ul class="kb-choices"><li>A. 統計profile</li><li>B. 説明表</li><li>C. コピー履歴 <span class="kb-ok">✅ 正解</span></li><li>D. thread待ち情報</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピー履歴やユーティリティ実行の記録を見る対象として、Cを採ります。Aは統計収集オプションの再利用、Bはアクセスパスの説明結果、Dは実行中処理の待ち時間分析です。履歴を読む時点も対象オブジェクトに合わせます；背景には履歴確認の観点で、SYSCOPY はカタログ・ディレクトリに関わるコピーやリカバリの記録を保持します、image copy、LOAD、REORGなどの履歴を確認し、回復時にどのコピーやログを使うか判断する材料になります、古い情報を読むときは対象オブジェクトと時点を合わせますという関係があり、この区別で確認する名称は「SYSCOPY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYSCOPY</strong></p><p>検証目的: 呼出判定のカタログ・ディレクトリについて、SYSCOPY は、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL 全体ではなく、対象指定、処理目的、実行後に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出判定のカタログ・ディレクトリの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSYSCOPYを指定し、OSKB010083の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SYSCOPY
CASE OSKB010083
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SYSCOPY
CASE OSKB010083
SOURCE Db2 for z/OS
SYSCOPYとOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010083を同じ出力で読み、呼出判定のカタログ・ディレクトリの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010083
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010083
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010083
DSNV401IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SYSCOPY と OSKB010083 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0164"><h3>SYSIBM catalog tables</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ・ディレクトリ ・ 難易度: 中級</p><p>SYSIBM catalog tablesは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表や索引、権限、package の定義をSQLで確認したいです。Db2 catalog内で参照する対象はどれですか。</p><ul class="kb-choices"><li>A. メタデータ表群 <span class="kb-ok">✅ 正解</span></li><li>B. ログ範囲管理域</li><li>C. 実行中スレッド</li><li>D. アクティブログ</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 定義メタデータをSQLで読む対象に当たるため、Aが該当します。ログ範囲を扱うBはdirectory側の用途、実行状態を示すCは監視対象、更新ログのDはデータセットです。定義確認の入口とは役割が違います；背景にはSYSIBM catalog tables は、カタログ・ディレクトリの中で Db2 catalog に含まれるメタデータ表群です、データベース DSNDB06 にあり、表、索引、権限、package などの定義情報をSQLで参照できます、運用では定義確認や影響調査の入口になりますという関係があり、この区別で確認する名称は「SYSIBM」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYSIBM catalog tables</strong></p><p>検証目的: 構文判定のカタログ・ディレクトリについて、SYSIBM catalog tablesは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文判定のカタログ・ディレクトリの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSYSIBM catalog tabを指定し、OSKB010081の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SYSIBM catalog tab
CASE OSKB010081
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SYSIBM catalog tab
CASE OSKB010081
SOURCE Db2 for z/OS
SYSIBM catalog tabとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010081を同じ出力で読み、構文判定のカタログ・ディレクトリの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010081
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010081
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010081
DSNV401IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の SYSIBM catalog tab と OSKB010081 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div></details></section>


## カタログ・統計・メタデータ > カタログ保守


<section class="kb-item" id="c07-i0165"><h3>CATMAINT</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ保守 ・ 難易度: 中級</p><p>CATMAINTは、カタログ・統計・メタデータの中でカタログ保守に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2メタデータと統計情報として扱い、SQL文法やユーティリティ手順とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> migrationやfunction level対応でDb2 catalog自体を更新し、実行後に保留状態や再編成要否を確認します。使う作業はどれですか。</p><ul class="kb-choices"><li>A. DSNTIAUL</li><li>B. CATMAINT <span class="kb-ok">✅ 正解</span></li><li>C. PLAN_TABLE</li><li>D. RUNSTATS PROFILE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> catalogを更新するmigration系utility作業として、Bが該当します。Aはデータ抽出用サンプル、Cは説明結果を読む表、Dは統計収集オプションの再利用です。構造更新後の保留状態も確認します；背景にはmigration対応のCATMAINT は、Db2 catalogをfunction levelなどに合わせて更新するutility作業です、実行前にはcatalogとdirectoryの整合性確認、image copy、必要な停止条件を確認します、実行後は保留状態やREORG要否を見ますという関係があり、この区別で確認する名称は「CATMAINT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0166"><h3>catalog REORG</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ保守 ・ 難易度: 中級</p><p>catalog REORGは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> catalog table spaceの未使用領域や断片化を減らし、CATMAINT後にAREO*となった対象も整えます。実施する保守はどれですか。</p><ul class="kb-choices"><li>A. catalog REORG <span class="kb-ok">✅ 正解</span></li><li>B. SQLCA確認</li><li>C. SYSCOPY削除</li><li>D. DCLGEN生成</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 再編成対象はcatalog table spaceなので、Aが妥当です。BはプログラムのSQL状態確認、Cは履歴表そのものの削除、Dはアプリケーション用宣言部の生成です。物理保守の目的とは違い、断片化や保留状態の解消を見ます；背景には再編成作業であるcatalog REORG は、Db2 catalog table spaceを整える作業です、DSNDB06内の未使用領域や断片化を減らし、migration前や数年単位の保守で実施します、更新後にAREO*状態になったcatalog objectsも対象になりますという関係があり、この区別で確認する名称は「REORG」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0167"><h3>catalog image copy</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ保守 ・ 難易度: 中級</p><p>catalog image copyは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> version migration前に、Db2 catalogとdirectoryを障害時に戻せるよう定期コピーを取得します。この保守作業はどれですか。</p><ul class="kb-choices"><li>A. optimizer用統計</li><li>B. アクセスパス説明</li><li>C. 回復用コピー取得 <span class="kb-ok">✅ 正解</span></li><li>D. thread待ち分析</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 回復用のcopyを取得する作業として、Cが該当します。統計情報のAはoptimizerの判断材料、説明情報のBはアクセスパス確認、待ち分析のDはスレッド待ちの調査です。コピー取得ジョブの結果もあわせて確認します；背景には回復準備として、catalog image copy はDb2 catalogとdirectoryを戻せる状態にする基本作業です、DSNTIJICなどで定期的にコピーを取得し、version migrationやfunction level activationの前にも実施します、コピー先とログ保持を合わせて確認しますという関係があり、この区別で確認する名称は「image」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0168"><h3>catalog migration impact</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ保守 ・ 難易度: 中級</p><p>catalog migration impactは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> version migration前に、catalog整合性、image copy、CHECK/REORG、CATMAINT後の状態確認まで含めて影響を見ます。これは何の検討ですか。</p><ul class="kb-choices"><li>A. Java接続確認</li><li>B. DDFポート更新</li><li>C. 移行影響確認 <span class="kb-ok">✅ 正解</span></li><li>D. lock timeout調整</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 移行前のcatalog変更影響を整理する検討として、Cを選びます。Java接続のAはドライバやルーチン環境、DDF更新のBは分散接続情報、ロック調整のDは待ち時間制御です。catalog移行前の総合確認とは別の作業です；背景にはDb2 catalog の変更影響は、version migrationやfunction level activationの前に見積もります、catalogとdirectoryの整合性、image copy、CHECK/REORGが確認対象です、更新utility後の状態確認も影響範囲に入り、停止時間と戻し方も計画しますという関係があり、この区別で確認する名称は「migration」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>catalog migration impact</strong></p><p>検証目的: 上書判定のカタログ保守について、catalog migration impactは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書判定のカタログ保守の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にcatalog migration を指定し、OSKB010087の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND catalog migration 
CASE OSKB010087
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM catalog migration 
CASE OSKB010087
SOURCE Db2 for z/OS
catalog migration とOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010087を同じ出力で読み、上書判定のカタログ保守の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010087
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010087
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010087
DSNV401IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の catalog migration  と OSKB010087 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div></details></section>


<section class="kb-item" id="c07-i0169"><h3>catalog recovery</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; カタログ保守 ・ 難易度: 中級</p><p>catalog recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> catalogやdirectoryの障害後、image copyとログを使ってメタデータ領域を戻します。実施する作業はどれですか。</p><ul class="kb-choices"><li>A. RUNSTATS再収集</li><li>B. EXPLAIN確認</li><li>C. DDF再同期</li><li>D. メタデータ復旧 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> メタデータ領域をコピーとログから戻す作業として、Dを選びます。統計処理のAは再収集、経路確認のBはアクセスパス確認、分散接続のCは通信情報同期です。catalog領域の障害復旧ではありません。保守起動などの前提も確認します；背景には障害対応で行うcatalog recovery は、Db2 catalogやdirectoryをimage copyとログから復旧する作業です、必要な権限、ACCESS(MAINT)での起動、コピー履歴、ログ範囲をそろえてから進めます、通常オブジェクトの回復より影響が大きいため手順確認が重要ですという関係があり、この区別で確認する名称は「recovery」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>catalog recovery</strong></p><p>検証目的: 探索判定のカタログ保守について、catalog recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL 全体ではなく、対象指定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010086の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索判定のカタログ保守の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にcatalog recoveryを指定し、OSKB010086の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND catalog recovery
CASE OSKB010086
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM catalog recovery
CASE OSKB010086
SOURCE Db2 for z/OS
catalog recoveryとOSKB010086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010086を同じ出力で読み、探索判定のカタログ保守の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010086
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010086
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010086
DSNV401IとOSKB010086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の catalog recovery と OSKB010086 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div></details></section>


## カタログ・統計・メタデータ > 統計・プラン情報


<section class="kb-item" id="c07-i0170"><h3>PLAN_TABLE as metadata</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; 統計・プラン情報 ・ 難易度: 中級</p><p>PLAN_TABLE as metadataは、Db2 for z/OSの統計・プラン情報で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。統計・プラン情報では、指定値と対象資源、実行時の出力を突き合わせて確認する。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 説明実行後に、表アクセス順や索引利用、結合方式を行として確認します。参照するメタデータはどれですか。</p><ul class="kb-choices"><li>A. SYSCOPY history</li><li>B. アクセスパス説明表 <span class="kb-ok">✅ 正解</span></li><li>C. active log file</li><li>D. catalog image copy</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 説明結果のアクセスパスを読む表なので、Bが該当します。履歴情報のAはコピーやユーティリティ記録、ログ出力のCは更新ログ、回復コピーのDはcatalog復旧用です。説明表の行を確認します。索引選択の確認にも使います；背景にはEXPLAIN結果を読む場面で、PLAN_TABLE as metadata は統計・プラン情報の分析対象になります、statementごとのアクセスパス、表アクセス順、索引利用、結合方式などを確認できます、実行結果そのものではなく、optimizerが選んだ計画の記録ですという関係があり、この区別で確認する名称は「PLAN_TABLE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0171"><h3>RUNSTATS</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; 統計・プラン情報 ・ 難易度: 中級</p><p>RUNSTATSは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 統計収集を保守計画で確認します。Db2の作業記録に統計収集の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は表カタログのSTATSTIME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS <span class="kb-ok">✅ 正解</span></li><li>B. REBUILD INDEX</li><li>C. RECOVER TABLESPACE</li><li>D. DISPLAY DATABASE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点統計収集は、オプティマイザーが使う表や索引の統計を更新することを目的に扱い、確認項目は統計収集証跡です。背景統計収集として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は統計収集読取です。統計収集の仕組みは、表カタログの統計取得時刻列と実行ログを照合する理由が統計収集判断です。A: 統計収集が正答です。統計反映後の再バインド要否を判断することに合うため、採否を決める説明軸は統計収集列確認です。B: 統計収集で見る索引再構築は代替にならず、今回の比較対象から外す理由は統計収集復旧です。C: 統計収集で見る表スペース回復は代替にならず、今回の比較対象から外す理由は統計収集保守です。D: 統計収集で見るデータベース状態表示は代替にならず、今回の比較対象から外す理由は統計収集棚卸です。初出語統計収集とは、技術項目名 RUNSTATS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は統計収集保守です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 統計収集を障害復旧で確認します。Db2の作業記録に統計収集の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は表カタログのSTATSTIME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. MERGECOPY</li><li>B. RUNSTATS <span class="kb-ok">✅ 正解</span></li><li>C. QUIESCE</li><li>D. CHECK DATA</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点統計収集は、オプティマイザーが使う表や索引の統計を更新することを目的に扱い、確認項目は統計収集列確認です。背景統計収集として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は統計収集復旧です。統計収集の仕組みは、表カタログの統計取得時刻列と実行ログを照合する理由が統計収集保守です。A: 統計収集で見る増分コピー統合は代替にならず、今回の比較対象から外す理由は統計収集証跡です。B: 統計収集が正答です。統計反映後の再バインド要否を判断することに合うため、採否を決める説明軸は統計収集読取です。C: 統計収集で見る静止点取得は代替にならず、今回の比較対象から外す理由は統計収集判断です。D: 統計収集で見る参照整合性検査は代替にならず、今回の比較対象から外す理由は統計収集定義です。初出語統計収集とは、技術項目名 RUNSTATS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は統計収集判断です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 統計収集を性能維持で確認します。Db2の作業記録に統計収集の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は表カタログのSTATSTIME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. TEMPLATE</li><li>B. REORG TABLESPACE</li><li>C. RUNSTATS <span class="kb-ok">✅ 正解</span></li><li>D. COPY TABLESPACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点統計収集は、オプティマイザーが使う表や索引の統計を更新することを目的に扱い、確認項目は統計収集証跡です。背景統計収集として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は統計収集読取です。統計収集の仕組みは、表カタログの統計取得時刻列と実行ログを照合する理由が統計収集判断です。A: 統計収集で見るデータセットひな形は代替にならず、今回の比較対象から外す理由は統計収集列確認です。B: 統計収集で見る表スペース再編成は代替にならず、今回の比較対象から外す理由は統計収集復旧です。C: 統計収集が正答です。統計反映後の再バインド要否を判断することに合うため、採否を決める説明軸は統計収集保守です。D: 統計収集で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由は統計収集棚卸です。初出語統計収集とは、技術項目名 RUNSTATS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は統計収集保守です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 統計収集を監査証跡で確認します。Db2の作業記録に統計収集の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は表カタログのSTATSTIME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. COPYDDN</li><li>B. SHRLEVEL CHANGE</li><li>C. SYSIBM.SYSCOPY</li><li>D. RUNSTATS <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点統計収集は、オプティマイザーが使う表や索引の統計を更新することを目的に扱い、確認項目は統計収集列確認です。背景統計収集として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は統計収集復旧です。統計収集の仕組みは、表カタログの統計取得時刻列と実行ログを照合する理由が統計収集保守です。A: 統計収集で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は統計収集証跡です。B: 統計収集で見る更新並行方式保守は代替にならず、今回の比較対象から外す理由は統計収集読取です。C: 統計収集で見るコピー履歴表は代替にならず、今回の比較対象から外す理由は統計収集判断です。D: 統計収集が正答です。統計反映後の再バインド要否を判断することに合うため、採否を決める説明軸は統計収集定義です。初出語統計収集とは、技術項目名 RUNSTATS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は統計収集判断です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>RUNSTATS</strong></p><p>検証目的: 終端判定の統計・プラン情報について、RUNSTATS は、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL 全体ではなく、対象指定、処理目的、実行に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端判定の統計・プラン情報の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRUNSTATSを指定し、OSKB010085の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RUNSTATS
CASE OSKB010085
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RUNSTATS
CASE OSKB010085
SOURCE Db2 for z/OS
RUNSTATSとOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010085を同じ出力で読み、終端判定の統計・プラン情報の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010085
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010085
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010085
DSNV401IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RUNSTATS と OSKB010085 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>RUNSTATS</strong></p><p>検証目的: 比較判定のユーティリティ本体について、RUNSTATS は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020094の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較判定のユーティリティ本体の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRUNSTATSを指定し、OSKB020094の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RUNSTATS
CASE OSKB020094
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RUNSTATS
CASE OSKB020094
SOURCE Db2 for z/OS
RUNSTATSとOSKB020094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020094を同じ出力で読み、比較判定のユーティリティ本体の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020094
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020094
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020094
DSNV401IとOSKB020094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RUNSTATS と OSKB020094 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0172"><h3>RUNSTATS PROFILE</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; 統計・プラン情報 ・ 難易度: 中級</p><p>RUNSTATS PROFILEは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 同じ表スペースに対して、あらかじめ決めた統計収集オプションを繰り返し使いたいです。使う仕組みはどれですか。</p><ul class="kb-choices"><li>A. RUNSTATS PROFILE <span class="kb-ok">✅ 正解</span></li><li>B. SYSCOPY record</li><li>C. PLAN_TABLE row</li><li>D. catalog image copy</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 統計収集オプションを再利用する仕組みとして、Aを使います。Bはコピーやユーティリティ履歴、Cはアクセスパス説明結果の格納先、Dはcatalogとdirectoryを戻せるようにするコピーです。収集内容のぶれを抑える点で区別します；背景にはRUNSTATS PROFILE は、統計・プラン情報の保守で統計収集オプションの再利用単位になります、あらかじめ定義した収集項目を使い、同じ対象へ一貫したRUNSTATSを実行できます、自律的な統計保守や定期運用で収集内容のぶれを抑えますという関係があり、この区別で確認する名称は「RUNSTATS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0173"><h3>catalog statistics</h3><p class="kb-meta">分類: カタログ・統計・メタデータ &gt; 統計・プラン情報 ・ 難易度: 中級</p><p>catalog statisticsは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 実行計画を選ぶ前に、optimizerが表や索引の件数・分布情報を参照します。この情報はどれですか。</p><ul class="kb-choices"><li>A. package実行権限</li><li>B. directory内部情報</li><li>C. SQL通信領域</li><li>D. 実行計画用の統計 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> アクセスパス選択に使う統計情報として、Dが当たります。権限情報のAは実行可否、内部情報のBはDb2運用領域、通信領域のCはプログラム結果を扱います。bind処理で索引利用や表走査を決める材料にもなります；背景には統計・プラン情報として、catalog statistics はDb2 optimizerがアクセスパスを選ぶために参照する情報です、表、索引、列の分布や件数がcatalogに保持され、BINDやREBIND時の判断に使われます、古い統計は不要なI/OやCPU消費につながりますという関係があり、この区別で確認する名称は「statistics」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_SQL_Reference.pdf p.70 / Db2_zOS_SQL_Reference.pdf p.2886 / Db2_zOS_Introduction.pdf p.244 / Db2_zOS_Performance.pdf p.527 / Db2_zOS_Utility_Guide.pdf p.631 / Db2_zOS_Installation.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>catalog statistics</strong></p><p>検証目的: 置換判定の統計・プラン情報について、catalog statisticsは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できるこに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換判定の統計・プラン情報の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にcatalog statisticsを指定し、OSKB010084の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND catalog statistics
CASE OSKB010084
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM catalog statistics
CASE OSKB010084
SOURCE Db2 for z/OS
catalog statisticsとOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010084を同じ出力で読み、置換判定の統計・プラン情報の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010084
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010084
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010084
DSNV401IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の catalog statistics と OSKB010084 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div></details></section>


## コマンド


<section class="kb-item" id="c07-i0174"><h3>DISPLAY DATABASE</h3><p class="kb-meta">分類: コマンド ・ 難易度: 初級</p><p>Db2 for z/OS の コマンドで扱うDISPLAY DATABASEは、Db2 データベース、表スペース、索引スペースなどの状態を表示するコマンドです。RESTRICT、STOP、COPY pending などの状態を調べる入口になります。ユーティリティやアプリ障害では、対象オブジェクトの状態確認に使います</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


<section class="kb-item" id="c07-i0175"><h3>START DATABASE</h3><p class="kb-meta">分類: コマンド ・ 難易度: 中級</p><p>Db2 for z/OS の コマンドで扱うSTART DATABASEは、停止中または制限状態の Db2 データベース関連オブジェクトを使用可能に戻すためのコマンドです。対象範囲を広く指定すると影響が大きいため、データベース、表スペース、パーティションの粒度を確認します。復旧後の開放操作でよく使います</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


<section class="kb-item" id="c07-i0176"><h3>STOP DATABASE</h3><p class="kb-meta">分類: コマンド ・ 難易度: 中級</p><p>Db2 for z/OS の コマンドで扱うSTOP DATABASEは、Db2 オブジェクトへのアクセスを停止または制限するためのコマンドです。保守作業や障害切り分けで使います。ただし、稼働中アプリケーションへの影響を伴います。停止範囲、オプション、実行タイミングを事前に確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


## コマンド・運用操作 > DDF制御


<section class="kb-item" id="c07-i0177"><h3>DISPLAY DDF</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; DDF制御 ・ 難易度: 中級</p><p>DISPLAY DDFは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></section>


<section class="kb-item" id="c07-i0178"><h3>MODIFY DDF</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; DDF制御 ・ 難易度: 中級</p><p>MODIFY DDFは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> DDFを完全停止せず、分散接続機能の運用属性を変更して反映状況を確認したい場面です。選ぶ操作はどれですか。</p><ul class="kb-choices"><li>A. BSDS回復</li><li>B. DDF変更 <span class="kb-ok">✅ 正解</span></li><li>C. 表行削除</li><li>D. SQL準備</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 分散接続機能の属性のみを変える場面なら、Bを採用します。Aは片側BSDS障害から二重構成へ戻す復旧作業です。Cは表データを削除するDMLで、Dは動的SQLの準備です。変更後はDDF表示で反映を見ます；背景には分散接続の運用変更で使うMODIFY DDFは、Db2 for z/OSのコマンド・運用操作としてDDFの一部属性や運用状態を変更します、停止と開始を主な根拠にしてなく、分散接続の状態確認や設定変更と合わせて、DISPLAY DDFの出力で効果を確認しますという関係があり、この区別で確認する名称は「MODIFY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0179"><h3>START DDF</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; DDF制御 ・ 難易度: 中級</p><p>START DDFは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ローカル処理は動いているが、アプリケーションサーバからのDRDA接続を受け付ける入口を開きます。使う操作はどれですか。</p><ul class="kb-choices"><li>A. BSDSログ内容の印刷確認</li><li>B. 表停止</li><li>C. DDF開始 <span class="kb-ok">✅ 正解</span></li><li>D. 索引検査</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> DRDA接続を受け付ける入口を開く操作なので、Cを選びます。AはログやBSDSの内容を帳票で点検します。Bは表スペースなどの利用停止で、Dは索引の整合性検査です。開始後はポート番号と受付状態を確認します；背景には分散接続開始で使うSTART DDFは、Db2 for z/OSのコマンド・運用操作としてDistributed Data Facilityを開始します、起動オプションのDDF STARTUP OPTIONがCOMMANDなどで準備されている場合、TCP/IPやDRDA接続を受け付ける入口を運用中に開けますという関係があり、この区別で確認する名称は「START」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>START DDF</strong></p><p>検証目的: 展開整理の制御について、START DDF は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確認でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010102の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開整理の制御の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTART DDFを指定し、OSKB010102の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND START DDF
CASE OSKB010102
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM START DDF
CASE OSKB010102
SOURCE Db2 for z/OS
START DDFとOSKB010102が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010102を同じ出力で読み、展開整理の制御の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010102
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010102
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010102
DSNV401IとOSKB010102が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の START DDF と OSKB010102 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0180"><h3>STOP DDF</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; DDF制御 ・ 難易度: 中級</p><p>STOP DDFは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 外部アプリケーションからの新規分散接続を止め、DDFのインターフェースを閉じたい場面です。実行する操作はどれですか。</p><ul class="kb-choices"><li>A. DB2起動</li><li>B. DDF停止 <span class="kb-ok">✅ 正解</span></li><li>C. 索引再構築</li><li>D. 統計履歴の詳細表示</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 新規の分散接続を止めて入口を閉じる操作は、Bです。AはDb2サブシステム自体を開始します。Cは索引を表データから再構築する保守で、Dは統計情報を読む確認です。残存リモート処理は別途スレッド表示で追います；背景には分散接続停止で使うSTOP DDFは、Db2 for z/OSのコマンド・運用操作としてDistributed Data Facilityを停止します、外部通信のTCP/IPやVTAMの接続口を閉じる操作であり、MODE指定や残っているリモート作業の扱いを確認しますという関係があり、この区別で確認する名称は「STOP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOP DDF</strong></p><p>検証目的: 呼出整理の制御について、STOP DDF は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確認できに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010103の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出整理の制御の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DDFを指定し、OSKB010103の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DDF
CASE OSKB010103
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DDF
CASE OSKB010103
SOURCE Db2 for z/OS
STOP DDFとOSKB010103が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010103を同じ出力で読み、呼出整理の制御の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010103
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010103
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010103
DSNV401IとOSKB010103が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の STOP DDF と OSKB010103 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010103 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


## コマンド・運用操作 > グループ・ユーティリティ・ログ制御


<section class="kb-item" id="c07-i0181"><h3>ARCHIVE LOG</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; グループ・ユーティリティ・ログ制御 ・ 難易度: 中級</p><p>ARCHIVE LOGは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> バックアップ取得前にログの区切りを作り、以後の回復で扱うアーカイブログを明確にしたい場面です。使う操作はどれですか。</p><ul class="kb-choices"><li>A. ログ切替 <span class="kb-ok">✅ 正解</span></li><li>B. 表ロード</li><li>C. DDF変更</li><li>D. ビュー更新</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 回復で扱うログの区切りを作る操作は、Aです。Bは外部データを表へロードするユーティリティです。CはDDFの運用属性を変え、Dはビュー経由で基表を更新する処理です。切替後はアーカイブ名を控え、回復手順へ残します；背景にはログ制御で使うARCHIVE LOGは、Db2 for z/OSのコマンド・運用操作としてアクティブログを切り替え、アーカイブログ作成へ進めます、バックアップや災害対策の節目では、ログ切替後のアーカイブデータセットとBSDSコピーの扱いを確認しますという関係があり、この区別で確認する名称は「ARCHIVE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>ARCHIVE LOG</strong></p><p>検証目的: 置換整理のグループ・ユーティリティ・ログ制御について、ARCHIVE LOG は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010104の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、置換整理のグループ・ユーティリティ・ログ制御の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にARCHIVE LOGを指定し、OSKB010104の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ARCHIVE LOG
CASE OSKB010104
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ARCHIVE LOG
CASE OSKB010104
SOURCE Db2 for z/OS
ARCHIVE LOGとOSKB010104が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010104を同じ出力で読み、置換整理のグループ・ユーティリティ・ログ制御の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010104
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010104
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010104
DSNV401IとOSKB010104が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の ARCHIVE LOG と OSKB010104 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010104 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>archive log</strong></p><p>検証目的: 上書整理のログ資材について、archive logは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010107の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、上書整理のログ資材の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にarchive logを指定し、OSKB010107の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND archive log
CASE OSKB010107
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM archive log
CASE OSKB010107
SOURCE Db2 for z/OS
archive logとOSKB010107が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010107を同じ出力で読み、上書整理のログ資材の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010107
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010107
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010107
DSNV401IとOSKB010107が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の archive log と OSKB010107 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010107 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0182"><h3>DISPLAY GROUP</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; グループ・ユーティリティ・ログ制御 ・ 難易度: 中級</p><p>DISPLAY GROUPは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Data Sharing環境で、どのメンバーがグループに参加しているかを確認し、影響範囲を切り分けます。使う表示操作はどれですか。</p><ul class="kb-choices"><li>A. ユーティリティ終了</li><li>B. DDF停止</li><li>C. グループ表示 <span class="kb-ok">✅ 正解</span></li><li>D. 表スペース停止</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Data Sharingの参加メンバーを見る目的なら、Cを選びます。Aはユーティリティを終了対象にする操作です。Bは分散接続口を閉じ、Dは表スペースなど特定オブジェクトの利用を止めます。障害範囲の切り分けに使います；背景にはデータ共用確認で使うDISPLAY GROUPは、Db2 for z/OSのコマンド・運用操作としてData Sharingグループやメンバーの状態を表示します、メンバーの参加状態、グループ情報、障害時の影響範囲を確認し、単一メンバーの問題かグループ全体の問題かを切り分けますという関係があり、この区別で確認する名称は「GROUP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0183"><h3>DISPLAY UTILITY</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; グループ・ユーティリティ・ログ制御 ・ 難易度: 中級</p><p>DISPLAY UTILITYは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></section>


<section class="kb-item" id="c07-i0184"><h3>RECOVER BSDS</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; グループ・ユーティリティ・ログ制御 ・ 難易度: 中級</p><p>RECOVER BSDSは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 二重BSDSの片側がデータセット障害で外れたため、空の代替データセットへ正常側の内容を戻して二重運用に戻します。使う操作はどれですか。</p><ul class="kb-choices"><li>A. ログ目録印刷</li><li>B. 統計履歴整理</li><li>C. BSDS二重復旧 <span class="kb-ok">✅ 正解</span></li><li>D. 表データ外部抽出処理</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 片側障害後に二重BSDSへ戻す復旧作業なら、Cが適切です。AはBSDSやログ目録を印刷物で照合する作業です。Bは統計履歴の整理で、Dは表データを外部ファイルへ取り出す処理です。代替先は空で用意します；背景には二重BSDS復旧で使うRECOVER BSDSは、Db2 for z/OSのコマンド・運用操作として片方のbootstrap data setが無効化された後に二重BSDS運用を再確立します、新しい空のBSDSを用意し、正常なコピーから内容を戻す流れで使いますという関係があり、この区別で確認する名称は「BSDS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECOVER BSDS</strong></p><p>検証目的: 終端整理のグループ・ユーティリティ・ログ制御について、RECOVER BSDS は、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL 全体ではなく、対象指定、処理目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010105の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端整理のグループ・ユーティリティ・ログ制御の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRECOVER BSDSを指定し、OSKB010105の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RECOVER BSDS
CASE OSKB010105
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RECOVER BSDS
CASE OSKB010105
SOURCE Db2 for z/OS
RECOVER BSDSとOSKB010105が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010105を同じ出力で読み、終端整理のグループ・ユーティリティ・ログ制御の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010105
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010105
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010105
DSNV401IとOSKB010105が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RECOVER BSDS と OSKB010105 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010105 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0185"><h3>TERM UTILITY</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; グループ・ユーティリティ・ログ制御 ・ 難易度: 中級</p><p>TERM UTILITYは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></section>


## コマンド・運用操作 > サブシステム制御


<section class="kb-item" id="c07-i0186"><h3>START DB2</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; サブシステム制御 ・ 難易度: 中級</p><p>START DB2は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守後に停止中のDb2を立ち上げ、必要なら保守用アクセス状態で状態確認を始めます。該当する運用操作はどれですか。</p><ul class="kb-choices"><li>A. DB2起動 <span class="kb-ok">✅ 正解</span></li><li>B. DDF停止</li><li>C. スレッド取消</li><li>D. ログ切替</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保守後にDb2サブシステムを立ち上げる操作なので、Aを選びます。Bは分散接続の入口を閉じるときに使います。Cは実行中スレッドへ終了を求め、Dはアクティブログの区切りを作ります。起動直後は稼働状況を読み取ります；背景にはサブシステム起動で使うSTART DB2は、Db2 for z/OSのコマンド・運用操作として停止中のDb2サブシステムを開始します、保守後や障害復旧後は、ACCESS(MAINT)などの起動状態、DDFの扱い、スレッドやユーティリティの残りを確認してから通常運用へ戻しますという関係があり、この区別で確認する名称は「START」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0187"><h3>STOP DB2</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; サブシステム制御 ・ 難易度: 中級</p><p>STOP DB2は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> メンテナンス時間帯にDb2全体を止める計画です。未完了処理を確認したうえで実行するサブシステム操作はどれですか。</p><ul class="kb-choices"><li>A. 表再編成</li><li>B. DB2停止 <span class="kb-ok">✅ 正解</span></li><li>C. データ共用グループ表示</li><li>D. 統計収集</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Db2全体を計画的に止める場面では、Bが該当します。Aは表スペースの物理配置を整える保守作業です。CはData Sharingメンバーを一覧で見る操作で、Dはアクセスパス判断用の統計を集めます。停止前の残処理確認が前提です；背景には計画停止で使うSTOP DB2は、Db2 for z/OSのコマンド・運用操作としてDb2サブシステムを停止します、停止方式のMODE指定や未完了ユーティリティ、接続中スレッドの状況によって進み方が変わるため、停止前には表示系コマンドで残作業を洗い出しますという関係があり、この区別で確認する名称は「STOP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOP DB2</strong></p><p>検証目的: 変更判定のサブシステム制御について、STOP DB2 は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確認できに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010100の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更判定のサブシステム制御の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DB2を指定し、OSKB010100の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DB2
CASE OSKB010100
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DB2
CASE OSKB010100
SOURCE Db2 for z/OS
STOP DB2とOSKB010100が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010100を同じ出力で読み、変更判定のサブシステム制御の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010100
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010100
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010100
DSNV401IとOSKB010100が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の STOP DB2 と OSKB010100 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


## コマンド・運用操作 > スレッド制御


<section class="kb-item" id="c07-i0188"><h3>CANCEL THREAD</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; スレッド制御 ・ 難易度: 中級</p><p>CANCEL THREADは、コマンド・運用操作の中でスレッド制御に関わるDb2技術項目です。操作対象、表示される情報、影響範囲、運用時の使いどころ。一方で、MVSコマンド一般、SDSF操作、JCL投入手順。 Db2コマンドとして扱い、MVSオペレータコマンド一般とは分けるとは分けて扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 長時間ロックを保持している接続を特定し、通常終了では解消しないためDb2側から終了を要求します。該当する操作はどれですか。</p><ul class="kb-choices"><li>A. 古い統計履歴の削除</li><li>B. THREAD取消 <span class="kb-ok">✅ 正解</span></li><li>C. COPY取得</li><li>D. 表定義変更</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> ロックを保持する接続へDb2側から終了を求めるため、Bを選択します。Aは統計履歴の保守であり、実行中処理は止めません。Cは回復用イメージコピーの取得、Dは表定義の変更です。外部待ちなら別経路も確認します；背景にはスレッド制御で使うCANCEL THREADは、Db2 for z/OSのコマンド・運用操作として問題のあるスレッドへ終了を要求します、強制指定のFORCEはサブシステム影響を伴う可能性があるため、DISPLAY THREADで対象を特定し、アプリケーション側やネットワーク側の滞留も見分けますという関係があり、この区別で確認する名称は「CANCEL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


<section class="kb-item" id="c07-i0189"><h3>DISPLAY THREAD</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; スレッド制御 ・ 難易度: 中級</p><p>DISPLAY THREADは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> スレッド表示を保守計画で確認します。Db2の作業記録にスレッド状態表示の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はユーティリティ実行カタログのMEMBER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. DISPLAY THREAD <span class="kb-ok">✅ 正解</span></li><li>B. CHECK DATA</li><li>C. COPY TABLESPACE</li><li>D. SYSIBM.SYSINDEXPART</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点スレッド表示は、接続中スレッドや処理状態を確認することを目的に扱い、確認項目はスレッド表示根拠です。背景スレッド表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はスレッド表示列確認です。スレッド表示の仕組みは、ユーティリティ実行カタログのMEMBER列と実行ログを照合する理由がスレッド表示復旧です。A: スレッド表示が正答です。保守前の利用状況を確認することに合うため、採否を決める説明軸はスレッド表示観点です。B: スレッド表示で見る参照整合性検査は代替にならず、今回の比較対象から外す理由はスレッド表示証跡です。C: スレッド表示で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由はスレッド表示読取です。D: スレッド表示で見る索引パート状態表は代替にならず、今回の比較対象から外す理由はスレッド表示判断です。初出語スレッド表示とは、技術項目名 DISPLAY THREAD で表すDb2ユーティリティ、指定、または記録名であり、用語定義はスレッド表示読取です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> スレッド表示を障害復旧で確認します。Db2の作業記録にスレッド状態表示の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はユーティリティ実行カタログのMEMBER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. MODIFY RECOVERY</li><li>B. DISPLAY THREAD <span class="kb-ok">✅ 正解</span></li><li>C. REBUILD INDEX</li><li>D. UNLOAD</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点スレッド表示は、接続中スレッドや処理状態を確認することを目的に扱い、確認項目はスレッド表示観点です。背景スレッド表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はスレッド表示証跡です。スレッド表示の仕組みは、ユーティリティ実行カタログのMEMBER列と実行ログを照合する理由がスレッド表示読取です。A: スレッド表示で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由はスレッド表示根拠です。B: スレッド表示が正答です。保守前の利用状況を確認することに合うため、採否を決める説明軸はスレッド表示列確認です。C: スレッド表示で見る索引再構築は代替にならず、今回の比較対象から外す理由はスレッド表示復旧です。D: スレッド表示で見るデータ抽出は代替にならず、今回の比較対象から外す理由はスレッド表示保守です。初出語スレッド表示とは、技術項目名 DISPLAY THREAD で表すDb2ユーティリティ、指定、または記録名であり、用語定義はスレッド表示復旧です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> スレッド表示を性能維持で確認します。Db2の作業記録にスレッド状態表示の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はユーティリティ実行カタログのMEMBER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. DSNUTILB</li><li>B. RUNSTATS</li><li>C. DISPLAY THREAD <span class="kb-ok">✅ 正解</span></li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点スレッド表示は、接続中スレッドや処理状態を確認することを目的に扱い、確認項目はスレッド表示根拠です。背景スレッド表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はスレッド表示列確認です。スレッド表示の仕組みは、ユーティリティ実行カタログのMEMBER列と実行ログを照合する理由がスレッド表示復旧です。A: スレッド表示で見るユーティリティ制御プログラムは代替にならず、今回の比較対象から外す理由はスレッド表示観点です。B: スレッド表示で見る統計収集は代替にならず、今回の比較対象から外す理由はスレッド表示証跡です。C: スレッド表示が正答です。保守前の利用状況を確認することに合うため、採否を決める説明軸はスレッド表示読取です。D: スレッド表示で見る表スペース再編成は代替にならず、今回の比較対象から外す理由はスレッド表示判断です。初出語スレッド表示とは、技術項目名 DISPLAY THREAD で表すDb2ユーティリティ、指定、または記録名であり、用語定義はスレッド表示読取です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> スレッド表示を監査証跡で確認します。Db2の作業記録にスレッド状態表示の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はユーティリティ実行カタログのMEMBER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. OPTIONS</li><li>B. RECOVERYDDN</li><li>C. FLASHCOPY</li><li>D. DISPLAY THREAD <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点スレッド表示は、接続中スレッドや処理状態を確認することを目的に扱い、確認項目はスレッド表示観点です。背景スレッド表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はスレッド表示証跡です。スレッド表示の仕組みは、ユーティリティ実行カタログのMEMBER列と実行ログを照合する理由がスレッド表示読取です。A: スレッド表示で見る実行共通指定は代替にならず、今回の比較対象から外す理由はスレッド表示根拠です。B: スレッド表示で見る回復用データ定義名は代替にならず、今回の比較対象から外す理由はスレッド表示列確認です。C: スレッド表示で見るストレージコピーは代替にならず、今回の比較対象から外す理由はスレッド表示復旧です。D: スレッド表示が正答です。保守前の利用状況を確認することに合うため、採否を決める説明軸はスレッド表示保守です。初出語スレッド表示とは、技術項目名 DISPLAY THREAD で表すDb2ユーティリティ、指定、または記録名であり、用語定義はスレッド表示復旧です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details></section>


## コマンド・運用操作 > データベースオブジェクト制御


<section class="kb-item" id="c07-i0190"><h3>DISPLAY DATABASE</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; データベースオブジェクト制御 ・ 難易度: 中級</p><p>DISPLAY DATABASEは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（6問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守後に表スペースが制限状態に残っていないか、対象オブジェクトの状態を一覧で確認します。見るための操作はどれですか。</p><ul class="kb-choices"><li>A. DATABASE表示 <span class="kb-ok">✅ 正解</span></li><li>B. DDF開始</li><li>C. ログ切替</li><li>D. スレッド強制終了要求</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 対象オブジェクトのアクセス状態を読む確認なので、Aが適切です。BはDDFを開けてリモート接続を受け付ける操作です。Cはアクティブログを切り替え、Dは問題スレッドへ終了要求を出します。制限表示で残状態を見ます；背景には状態確認で使うDISPLAY DATABASEは、Db2 for z/OSのコマンド・運用操作としてデータベース、表スペース、索引スペースのアクセス状態や制限状態を表示します、保守前後はRESTRICTやSPACENAMを使い、停止中、ユーティリティ中、保留状態を確認しますという関係があり、この区別で確認する名称は「DISPLAY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> データベース表示を保守計画で確認します。Db2の作業記録にデータベース状態表示の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は表スペースカタログのデータベースNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE</li><li>B. SYSIBM.SYSTABLESPACE</li><li>C. OPTIONS</li><li>D. DISPLAY DATABASE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点データベース表示は、対象データベースや表スペースの状態を表示することを目的に扱い、確認項目はデータベース表示定義です。背景データベース表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はデータベース表示根拠です。データベース表示の仕組みは、表スペースカタログのデータベースNAME列と実行ログを照合する理由がデータベース表示列確認です。A: データベース表示で見る表スペース回復は代替にならず、今回の比較対象から外す理由はデータベース表示棚卸です。B: データベース表示で見る表スペース状態表は代替にならず、今回の比較対象から外す理由はデータベース表示観点です。C: データベース表示で見る実行共通指定は代替にならず、今回の比較対象から外す理由はデータベース表示証跡です。D: データベース表示が正答です。ユーティリティ前後の制限状態を確認することに合うため、採否を決める説明軸はデータベース表示読取です。初出語データベース表示とは、技術項目名 DISPLAY DATABASE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はデータベース表示証跡です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> データベース表示を障害復旧で確認します。Db2の作業記録にデータベース状態表示の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は表スペースカタログのデータベースNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. DISPLAY DATABASE <span class="kb-ok">✅ 正解</span></li><li>B. CHECK DATA</li><li>C. COPY TABLESPACE</li><li>D. SYSIBM.SYSINDEXPART</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点データベース表示は、対象データベースや表スペースの状態を表示することを目的に扱い、確認項目はデータベース表示棚卸です。背景データベース表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はデータベース表示観点です。データベース表示の仕組みは、表スペースカタログのデータベースNAME列と実行ログを照合する理由がデータベース表示証跡です。A: データベース表示が正答です。ユーティリティ前後の制限状態を確認することに合うため、採否を決める説明軸はデータベース表示定義です。B: データベース表示で見る参照整合性検査は代替にならず、今回の比較対象から外す理由はデータベース表示根拠です。C: データベース表示で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由はデータベース表示列確認です。D: データベース表示で見る索引パート状態表は代替にならず、今回の比較対象から外す理由はデータベース表示復旧です。初出語データベース表示とは、技術項目名 DISPLAY DATABASE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はデータベース表示列確認です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> データベース表示を性能維持で確認します。Db2の作業記録にデータベース状態表示の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は表スペースカタログのデータベースNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. MODIFY RECOVERY</li><li>B. DISPLAY DATABASE <span class="kb-ok">✅ 正解</span></li><li>C. REBUILD INDEX</li><li>D. UNLOAD</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点データベース表示は、対象データベースや表スペースの状態を表示することを目的に扱い、確認項目はデータベース表示定義です。背景データベース表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はデータベース表示根拠です。データベース表示の仕組みは、表スペースカタログのデータベースNAME列と実行ログを照合する理由がデータベース表示列確認です。A: データベース表示で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由はデータベース表示棚卸です。B: データベース表示が正答です。ユーティリティ前後の制限状態を確認することに合うため、採否を決める説明軸はデータベース表示観点です。C: データベース表示で見る索引再構築は代替にならず、今回の比較対象から外す理由はデータベース表示証跡です。D: データベース表示で見るデータ抽出は代替にならず、今回の比較対象から外す理由はデータベース表示読取です。初出語データベース表示とは、技術項目名 DISPLAY DATABASE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はデータベース表示証跡です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> データベース表示を監査証跡で確認します。Db2の作業記録にデータベース状態表示の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は表スペースカタログのデータベースNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. DSNUTILB</li><li>B. RUNSTATS</li><li>C. DISPLAY DATABASE <span class="kb-ok">✅ 正解</span></li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点データベース表示は、対象データベースや表スペースの状態を表示することを目的に扱い、確認項目はデータベース表示棚卸です。背景データベース表示として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はデータベース表示観点です。データベース表示の仕組みは、表スペースカタログのデータベースNAME列と実行ログを照合する理由がデータベース表示証跡です。A: データベース表示で見るユーティリティ制御プログラムは代替にならず、今回の比較対象から外す理由はデータベース表示定義です。B: データベース表示で見る統計収集は代替にならず、今回の比較対象から外す理由はデータベース表示根拠です。C: データベース表示が正答です。ユーティリティ前後の制限状態を確認することに合うため、採否を決める説明軸はデータベース表示列確認です。D: データベース表示で見る表スペース再編成は代替にならず、今回の比較対象から外す理由はデータベース表示復旧です。初出語データベース表示とは、技術項目名 DISPLAY DATABASE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はデータベース表示列確認です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 記録確認のコマンドに関係する DISPLAY DATABASE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. -DISPLAY DATABASE(*) SPACENAM(*)の結果から対象行を抜き出し、記録確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. DISPLAY DATABASE の名称と担当者名のみを残して記録確認のコマンドの表示本文を確認対象に含めない。</li><li>C. データベース管理以外の画面で記録確認のコマンドを確認し同じ証跡として扱ったことにする。</li><li>D. DSNT360I の有無を見ず記録確認のコマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では DISPLAY DATABASE は「DISPLAY DATABASE の用途をデータベース管理の表示で確認する記録確認項目」と-DISPLAY DATABASE(*) SPACENAM(*)または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では Db2 for z/OS の DISPLAY DATABASE と DSNT360I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では DISPLAY DATABASE を Db2 for z/OS で扱う確認対象とし、用語名は記録確認用語です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DISPLAY DATABASE</strong></p><p>検証目的: 記録確認のコマンドについて、Db2 for z/OS の コマンドで扱う DISPLAY DATABASE は、Db2 データベース、表スペース、索引スペースなどの状態を表示するコマンドです。RESTRIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY DATABASE(*) SPACENAM(*)を実行し、DSNT360Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY DATABASE(*) SPACENAM(*) を入力し、記録確認のコマンドの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
COMMAND INPUTに-DISPLAY DATABASE(*) SPACENAM(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDISPLAY DATABASEを指定し、OSKB010013の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DISPLAY DATABASE
CASE OSKB010013
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DISPLAY DATABASE
CASE OSKB010013
SOURCE Db2 for z/OS
DISPLAY DATABASEとOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNT360IとOSKB010013を同じ出力で読み、記録確認のコマンドの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
CASE OSKB010013
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010013
-DISPLAY DATABASE(*) SPACENAM(*)
DSNT360I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010013
DSNT360IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*) が画面・出力に表示されること
② ステップ2 の DISPLAY DATABASE と OSKB010013 が画面・出力に表示されること
③ ステップ3 の DSNT360I と OSKB010013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


<section class="kb-item" id="c07-i0191"><h3>START DATABASE</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; データベースオブジェクト制御 ・ 難易度: 中級</p><p>START DATABASEは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 保守で止めていた表スペースを、ユーティリティ専用または通常利用できる状態へ戻したい場面です。使う操作はどれですか。</p><ul class="kb-choices"><li>A. 分散接続口の状態表示</li><li>B. ログ目録変更</li><li>C. DATABASE開始 <span class="kb-ok">✅ 正解</span></li><li>D. BSDS印刷</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 止めていた表スペースを利用可能側へ戻す判断なら、Cを使います。AはDDFの状態や接続口を確認する表示操作です。BはBSDSやログの目録情報を扱う作業で、Dはログ関連情報を帳票で照合する確認です。開始後のアクセス種別も見ます；背景にはオブジェクト開放で使うSTART DATABASEは、Db2 for z/OSのコマンド・運用操作としてデータベースや表スペースを利用可能な状態へ戻します、アクセス指定のACCESS(UT)やACCESS(RW)により、通常SQLを許すのかユーティリティ専用にするのかが変わりますという関係があり、この区別で確認する名称は「DATABASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 比較確認のコマンドで START DATABASE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. START DATABASE の出力を取らず比較確認のコマンドの説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. -DISPLAY DATABASE(*) SPACENAM(*)を省略して比較確認のコマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認のコマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では START DATABASE は「比較確認のコマンドに関係する定義値と表示行を照合する比較確認項目」と-DISPLAY DATABASE(*) SPACENAM(*)または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では START DATABASE の属性行と DSNT360I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では START DATABASE を Db2 for z/OS の運用手順で確認し、初出名は比較確認初出です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>START DATABASE</strong></p><p>検証目的: 比較確認のコマンドについて、Db2 for z/OS の コマンドで扱う START DATABASE は、停止中または制限状態の Db2 データベース関連オブジェクトを使用可能に戻すためのコマンドです。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY DATABASE(*) SPACENAM(*)を実行し、DSNT360Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY DATABASE(*) SPACENAM(*) を入力し、比較確認のコマンドの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
COMMAND INPUTに-DISPLAY DATABASE(*) SPACENAM(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTART DATABASEを指定し、OSKB010014の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND START DATABASE
CASE OSKB010014
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM START DATABASE
CASE OSKB010014
SOURCE Db2 for z/OS
START DATABASEとOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNT360IとOSKB010014を同じ出力で読み、比較確認のコマンドの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
CASE OSKB010014
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010014
-DISPLAY DATABASE(*) SPACENAM(*)
DSNT360I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010014
DSNT360IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*) が画面・出力に表示されること
② ステップ2 の START DATABASE と OSKB010014 が画面・出力に表示されること
③ ステップ3 の DSNT360I と OSKB010014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


<section class="kb-item" id="c07-i0192"><h3>STOP DATABASE</h3><p class="kb-meta">分類: コマンド・運用操作 &gt; データベースオブジェクト制御 ・ 難易度: 中級</p><p>STOP DATABASEは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 表スペースのみを保守対象にし、Db2全体ではなく該当オブジェクトの利用を止めます。適切な操作はどれでしょうか。</p><ul class="kb-choices"><li>A. DDF接続属性の変更</li><li>B. スレッド表示</li><li>C. パッケージ解放</li><li>D. DATABASE停止 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表スペース単位で利用を止める判断なら、Dを選びます。AはDDFの接続属性を運用中に変える場面で使います。Bは処理中スレッドの状態を見るを主な根拠にして、CはBIND済みのパッケージ資材を管理します。停止範囲は事前に絞ります；背景には対象停止で使うSTOP DATABASEは、Db2 for z/OSのコマンド・運用操作として特定データベースや表スペースの利用を止めます、保守、回復、再編成の前に対象範囲を限定して止めることで、サブシステム全体停止より影響を抑えられますという関係があり、この区別で確認する名称は「DATABASE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide / Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 順序確認のコマンドでデータベース管理の運用確認を行います。STOP DATABASE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. Db2 for z/OS と無関係な一覧で順序確認のコマンドを確認した扱いにする。</li><li>B. DSNT360I の有無を確認せず順序確認のコマンドを正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. STOP DATABASE の属性行を読まず順序確認のコマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では STOP DATABASE は「Db2 for z/OS で STOP DATABASE の扱いを記録する順序確認項目」と-DISPLAY DATABASE(*) SPACENAM(*)または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では STOP DATABASE の表示結果と DSNT360I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では STOP DATABASE の使い方を出典欄から追跡し、資料名は順序確認資料です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOP DATABASE</strong></p><p>検証目的: 構文整理のデータベースオブジェクト制御について、STOP DATABASE は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010101の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、構文整理のデータベースオブジェクト制御の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DATABASEを指定し、OSKB010101の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DATABASE
CASE OSKB010101
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DATABASE
CASE OSKB010101
SOURCE Db2 for z/OS
STOP DATABASEとOSKB010101が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010101を同じ出力で読み、構文整理のデータベースオブジェクト制御の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010101
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010101
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010101
DSNV401IとOSKB010101が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の STOP DATABASE と OSKB010101 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>STOP DATABASE</strong></p><p>検証目的: 順序確認のコマンドについて、Db2 for z/OS の コマンドで扱う STOP DATABASE は、Db2 オブジェクトへのアクセスを停止または制限するためのコマンドです。保守作業や障害切り分けで使に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY DATABASE(*) SPACENAM(*)を実行し、DSNT360Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY DATABASE(*) SPACENAM(*) を入力し、順序確認のコマンドの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
COMMAND INPUTに-DISPLAY DATABASE(*) SPACENAM(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSTOP DATABASEを指定し、OSKB010015の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND STOP DATABASE
CASE OSKB010015
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM STOP DATABASE
CASE OSKB010015
SOURCE Db2 for z/OS
STOP DATABASEとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNT360IとOSKB010015を同じ出力で読み、順序確認のコマンドの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*)
CASE OSKB010015
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010015
-DISPLAY DATABASE(*) SPACENAM(*)
DSNT360I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010015
DSNT360IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY DATABASE(*) SPACENAM(*) が画面・出力に表示されること
② ステップ2 の STOP DATABASE と OSKB010015 が画面・出力に表示されること
③ ステップ3 の DSNT360I と OSKB010015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


## サブシステムパラメータ > DDF・分散接続


<section class="kb-item" id="c07-i0193"><h3>CMTSTAT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>CMTSTATは、Db2のDDFに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0194"><h3>CONDBAT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>CONDBATは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アプリケーションサーバ側の接続プール数を合計し、Db2が同時に抱えられるリモート接続数を決めます。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. アクティブログ数</li><li>B. データセット暗号化方式</li><li>C. 同時接続できるリモート接続数 <span class="kb-ok">✅ 正解</span></li><li>D. SQL実行前のプリコンパイル指定</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 同時に保持できるリモート接続数を扱うため、Cが該当します。Aはログ資材の構成で、Bは保存データの保護方式です。Dは静的SQL開発で使う前処理の指定であり、接続プールの容量調整とは管理面が違います。プール設計で見直します；背景にはリモート接続の総量を制御するCONDBATは、Db2 for z/OSのDDF・分散接続パラメータとして同時に接続できるインバウンドDDF接続数を指定します、接続プールを持つ複数アプリケーションでは、プールサイズ合計とDBAT上限の両方を見て不足や過大設定を判断しますという関係があり、この区別で確認する名称は「CONDBAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONDBAT</strong></p><p>検証目的: 条件検査の・分散接続について、CONDBAT は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、条件検査の・分散接続の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にCONDBATを指定し、OSKB020069の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CONDBAT
CASE OSKB020069
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CONDBAT
CASE OSKB020069
SOURCE Db2 for z/OS
CONDBATとOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020069を同じ出力で読み、条件検査の・分散接続の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020069
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020069
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020069
DSNV401IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CONDBAT と OSKB020069 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0195"><h3>IDTHTOIN</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>IDTHTOINは、サブシステムパラメータの中でDDF・分散接続に関わるDb2技術項目です。何を制御するか、変更時に影響する接続、DISPLAY DDFなどで確認できる状態。一方で、Comm Server/TCP/IP一般設定の説明には広げないとは分けて扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 分散接続が処理を終えたまま長く残り、使っていないスレッドをどの時点で終了候補にするかを調整します。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. アイドルスレッド終了時間 <span class="kb-ok">✅ 正解</span></li><li>B. 分散接続待ち行列の最大保持数</li><li>C. セキュアポート番号</li><li>D. ログ切替方式</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 未使用状態のスレッドをいつ片付けるかを決めるため、Aです。BはDBAT待ちの接続キュー制御、CはTLS系接続の入口です。Dは回復資材の区切りを作るログ操作であり、アイドルDBAT整理とは目的が違います；背景には使われていない分散スレッドを片付けるIDTHTOINは、Db2 for z/OSのDDF・分散接続パラメータとしてアイドル状態のスレッドを検出し終了候補にするまでの時間を指定します、長すぎると資源が残り、短すぎると再接続や再準備の増加につながるため、ワークロードに合わせますという関係があり、この区別で確認する名称は「IDTHTOIN」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDTHTOIN</strong></p><p>検証目的: 区切検査の・分散接続について、IDTHTOIN は、サブシステムパラメータの中で DDF ・分散接続に関わる Db2技術項目です。何を制御するか、変更時に影響する接続、DISPLAY DDF などで確認できる状態に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切検査の・分散接続の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にIDTHTOINを指定し、OSKB020070の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND IDTHTOIN
CASE OSKB020070
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM IDTHTOIN
CASE OSKB020070
SOURCE Db2 for z/OS
IDTHTOINとOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020070を同じ出力で読み、区切検査の・分散接続の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020070
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020070
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020070
DSNV401IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の IDTHTOIN と OSKB020070 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020070 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0196"><h3>IPNAME</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>IPNAMEは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0197"><h3>LOCATION</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>LOCATIONは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> クライアントが接続先Db2を指定するときに使うロケーション名を、DDF開始メッセージや通信定義と突き合わせます。確認対象はどれですか。</p><ul class="kb-choices"><li>A. Db2ロケーション名 <span class="kb-ok">✅ 正解</span></li><li>B. ログアーカイブ先データセット名</li><li>C. 表スペースページサイズ</li><li>D. RIDプール容量</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 接続先として見えるDb2のロケーション名を確認するため、Aです。Bは回復資材を置くデータセット、Cは表スペース設計の属性です。Dはアクセス処理で使う作業領域の容量であり、DDFの接続名とは役割が異なります；背景には分散接続先を示すLOCATIONは、Db2 for z/OSのDDF・分散接続パラメータとしてDb2サブシステムまたはグループのロケーション名を表します、クライアント接続、通信データベース、DDF開始メッセージで同じ名前が見えるため、接続先の取り違えを防ぐ確認点になりますという関係があり、この区別で確認する名称は「LOCATION」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOCATION</strong></p><p>検証目的: 出力検査の・分散接続について、LOCATION は、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力検査の・分散接続の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にLOCATIONを指定し、OSKB020068の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND LOCATION
CASE OSKB020068
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM LOCATION
CASE OSKB020068
SOURCE Db2 for z/OS
LOCATIONとOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020068を同じ出力で読み、出力検査の・分散接続の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020068
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020068
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020068
DSNV401IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の LOCATION と OSKB020068 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0198"><h3>MAXDBAT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>MAXDBATは、Db2のDDFに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0199"><h3>PORT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>PORTは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アプリケーションサーバから通常のDRDA SQL要求を受けるTCP/IPポートを決めます。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. 主SQL受付ポート <span class="kb-ok">✅ 正解</span></li><li>B. 二相コミット再同期専用ポート</li><li>C. スレッド待機時間</li><li>D. データ共用メンバー名</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 通常のDRDA要求を受ける主ポートを扱うため、Aを選びます。Bは二相コミット復旧用の入口であり、Cは接続後の滞留時間制御です。DはData Sharingのメンバー識別で、TCP/IPの受付番号ではありません。開始時はDDF表示のTCPPORTを確認します；背景には分散接続の入口を決めるPORTは、Db2 for z/OSのDDF・分散接続パラメータとして通常のDRDA SQL要求を受け付けるTCP/IPポート番号です、開始時はDDFがそのポートにbindし、TCP/IP定義やBSDS内のDDF情報と矛盾しないことを確認しますという関係があり、この区別で確認する名称は「PORT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details></section>


<section class="kb-item" id="c07-i0200"><h3>RESPORT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>RESPORTは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0201"><h3>SECPORT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>SECPORTは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0202"><h3>TCP/IP listener</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DDF・分散接続 ・ 難易度: 中級</p><p>TCP/IP listenerは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対象になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> DDFを開始した後、指定ポートで外部アプリケーションからの接続要求を待ち受ける状態になっているかを確認します。該当する対象はどれですか。</p><ul class="kb-choices"><li>A. SQLCAの戻り領域</li><li>B. DDFが接続要求を待ち受ける口 <span class="kb-ok">✅ 正解</span></li><li>C. 表の再編成方式</li><li>D. バッファプールページセットの割当単位</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 待受け口としてDDFがTCP/IP上で接続要求を受ける状態を見るため、Bが適切です。AはSQL結果を受け取るアプリケーション領域です。Cは表の物理保守方式で、Dは入出力キャッシュの割当設計に関わります。開始メッセージで値を照合します；背景には接続要求を待ち受けるTCP/IP listenerは、Db2 for z/OSのDDF・分散接続パラメータ群と連動して、DDFが指定ポートで外部からの要求を受ける状態を指します、開始後はDSNL004IやDISPLAY DDFで、LOCATION、IPNAME、TCPPORT、SECPORT、RESPORTが期待値かを確認しますという関係があり、この区別で確認する名称は「listener」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Messages / Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_Security</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCP ・ IP listener</strong></p><p>検証目的: 範囲検査の・について、TCP/IP listenerは、Db2の分散接続、DDF、DBAT、ポート、暗号化、再同期に関わる項目です。リモート接続の受付状態、同時接続数、通信経路の切り分けで確認対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020071の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、範囲検査の・の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にTCP ・ IP listenerを指定し、OSKB020071の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND TCP ・ IP listener
CASE OSKB020071
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM TCP ・ IP listener
CASE OSKB020071
SOURCE Db2 for z/OS
TCP ・ IP listenerとOSKB020071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020071を同じ出力で読み、範囲検査の・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020071
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020071
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020071
DSNV401IとOSKB020071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の TCP ・ IP listener と OSKB020071 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


## サブシステムパラメータ > DSNZPARMマクロ群


<section class="kb-item" id="c07-i0203"><h3>DSN6ARVP</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DSNZPARMマクロ群 ・ 難易度: 上級</p><p>DSN6ARVPは、Db2のDSNZPARMに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 新しいデータ共有メンバーで、アーカイブログの第1コピーと第2コピーの接頭辞を確認します。参照するマクロはどれですか。</p><ul class="kb-choices"><li>A. DSN6ARVP <span class="kb-ok">✅ 正解</span></li><li>B. DSN6LOGP</li><li>C. DSN6GRP</li><li>D. DSN6SYSP</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> アーカイブログ名の接頭辞を持つため、Aを選びます。誤答Bはログのコピー数やオフロードの制御を扱います。誤答Cはデータ共有のグループやメンバー情報を扱い、誤答Dはシステム全体の実行時値を収める区画です；背景にはDSN6ARVP は、DSNZPARM マクロ群の中でアーカイブログデータセット名の接頭辞を扱います、ARCPFX1 と ARCPFX2 は第1コピー、第2コピーのアーカイブログ接頭辞として使われます、データ共有メンバーを追加するときは、メンバー名とログ名の対応も点検しますという関係があり、この区別で確認する名称は「DSN6ARVP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0204"><h3>DSN6FAC</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DSNZPARMマクロ群 ・ 難易度: 上級</p><p>DSN6FACは、Db2のDSNZPARMに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> DDF初期化で facility section の欠落を疑うコードが出ました。DSNZPxxx内で確認するマクロはどれですか。</p><ul class="kb-choices"><li>A. DSN6SYSP</li><li>B. DSN6FAC <span class="kb-ok">✅ 正解</span></li><li>C. DSN6LOGP</li><li>D. DSN6ARVP</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> DDF初期化で facility section の欠落を追うため、Bが該当します。誤答Aの DSN6SYSP はシステム全体の値を収める別区画です。誤答Cはログ関連の区画で、誤答Dはアーカイブログ名の接頭辞を扱う区画です；背景にはfacility section を構成する DSN6FAC は、Db2 初期化パラメータモジュール内の区画です、分散機能がこの区画を参照できない場合は、初期化エラーとして診断対象になります、作成済みの DSNZPxxx にこの CSECT が含まれるかを、導入ジョブのリストで調べますという関係があり、この区別で確認する名称は「DSN6FAC」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DSN6FAC</strong></p><p>検証目的: 展開検査のマクロ群について、DSN6FAC は、Db2の DSNZPARM に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、展開検査のマクロ群の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDSN6FACを指定し、OSKB020062の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DSN6FAC
CASE OSKB020062
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DSN6FAC
CASE OSKB020062
SOURCE Db2 for z/OS
DSN6FACとOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020062を同じ出力で読み、展開検査のマクロ群の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020062
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020062
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020062
DSNV401IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DSN6FAC と OSKB020062 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation.pdf p.442</p></div></details></section>


<section class="kb-item" id="c07-i0205"><h3>DSN6GRP</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DSNZPARMマクロ群 ・ 難易度: 上級</p><p>DSN6GRPは、Db2のDSNZPARMに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> データ共有メンバーの MEMBNAME と DSHARE の値を、起動プロシージャの指定と突き合わせます。見るべきマクロはどれですか。</p><ul class="kb-choices"><li>A. DSN6SPRM</li><li>B. DSN6LOGP</li><li>C. DSN6GRP <span class="kb-ok">✅ 正解</span></li><li>D. DSN6FAC</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> グループとメンバーの値を保持するため、Cを使います。誤答Aは広い実行時パラメータの区画です。誤答Bはログ設定を収めるマクロです。誤答DはDDF初期化時に参照されるfacility側で、メンバー名の保持には使いません；背景にはDSN6GRP は、DSNZPARM マクロ群のうちデータ共有グループとメンバーの識別に関わります、MEMBNAME や DSHARE の値は、起動プロシージャ側のメンバー名と食い違うと始動時の調査対象になります、データ共有解除や追加時は、再アセンブル範囲を誤らないことが重要ですという関係があり、この区別で確認する名称は「DSN6GRP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0206"><h3>DSN6LOGP</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DSNZPARMマクロ群 ・ 難易度: 上級</p><p>DSN6LOGPは、Db2のDSNZPARMに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> active log records のオフロードや BSDS 二重化に関わる値を、ZPARM更新前に確認します。対象のマクロはどれですか。</p><ul class="kb-choices"><li>A. DSN6SYSP</li><li>B. DSN6ARVP</li><li>C. DSN6FAC</li><li>D. DSN6LOGP <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ログ退避やBSDS二重化の指定を含むため、Dを選びます。A: システム全体の値を持つ区画との混同になります。誤答Bはアーカイブログ名の接頭辞で、誤答CはDDF初期化時に参照されるfacility側の区画を指します；背景にはログ制御の値を収める DSN6LOGP は、DSNZPARM マクロ群の一部です、OFFLOAD は active log records を archive logs へ退避するかを決め、TWOBSDS は二重 BSDS の構成と関係します、回復性を重視する本番系では、ログ退避と二重化の値を変更管理で扱いますという関係があり、この区別で確認する名称は「DSN6LOGP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0207"><h3>DSN6SPRM</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DSNZPARMマクロ群 ・ 難易度: 上級</p><p>DSN6SPRMは、Db2のDSNZPARMに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Administrative Scheduler のプロシージャ名や広い実行時値を、DSNTIJUZの再リンク前に確認します。主に見るマクロはどれですか。</p><ul class="kb-choices"><li>A. DSN6SPRM <span class="kb-ok">✅ 正解</span></li><li>B. DSN6GRP</li><li>C. DSN6LOGP</li><li>D. DSN6ARVP</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 広い実行時値と ADMTPROC を扱うため、Aを選びます。誤答Bはデータ共有メンバー情報です。誤答Cはログ退避やBSDS関連で、誤答Dはアーカイブログ名の接頭辞に寄った区画です。起動時パラメータ名との対応も確認します；背景にはDSN6SPRM は、DSNZPARM マクロ群の中心的な実行時パラメータ区画です、Administrative Scheduler のプロシージャ名を示す ADMTPROC など、起動後の運用機能に関係する値もここに現れます、再リンク時は、起動時の PARM 名とリンク編集の NAME 指定が同じかを見ますという関係があり、この区別で確認する名称は「DSN6SPRM」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542</p></div></details></section>


<section class="kb-item" id="c07-i0208"><h3>DSN6SYSP</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; DSNZPARMマクロ群 ・ 難易度: 上級</p><p>DSN6SYSPは、Db2のDSNZPARMに関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> トレース初期化値や CTHREAD など、システム全体に効く実行時区画を調査します。該当するマクロはどれですか。</p><ul class="kb-choices"><li>A. DSN6FAC</li><li>B. DSN6SYSP <span class="kb-ok">✅ 正解</span></li><li>C. DSN6ARVP</li><li>D. DSN6SPRM</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> トレース初期化値や CTHREAD を追う調査なので、Bが正解です。誤答AはDDF初期化時に参照されるfacility側の区画です。誤答Cはアーカイブログ名の接頭辞で、誤答Dは広い実行時値を持つ別区画として扱います；背景にはsystem parameter section を表す DSN6SYSP は、DSNZPARM マクロ群の実行時区画です、トレース初期化パラメータや CTHREAD など、サブシステム全体に効く値の診断で名前が現れます、古い CSECT が読み込まれた場合は、DSNTIJUZ による再アセンブルと再リンクが確認点になりますという関係があり、この区別で確認する名称は「DSN6SYSP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DSN6SYSP</strong></p><p>検証目的: 呼出検査のマクロ群について、DSN6SYSP は、Db2の DSNZPARM に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、呼出検査のマクロ群の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDSN6SYSPを指定し、OSKB020063の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DSN6SYSP
CASE OSKB020063
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DSN6SYSP
CASE OSKB020063
SOURCE Db2 for z/OS
DSN6SYSPとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020063を同じ出力で読み、呼出検査のマクロ群の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020063
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020063
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020063
DSNV401IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DSN6SYSP と OSKB020063 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation.pdf p.442</p></div></details></section>


## サブシステムパラメータ > ロック・メモリ・実行資源


<section class="kb-item" id="c07-i0209"><h3>CACHEDYN</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>CACHEDYNは、サブシステムパラメータの中でロック・メモリ・実行資源に関わるDb2技術項目です。運用者が調整理由を説明できる範囲、性能・可用性への代表的影響。一方で、チューニング手順の長い手順化や全推奨値の提示は含めないとは分けて扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 同じ動的SQLが繰り返し実行されるため、PREPAREの費用を避ける目的でステートメントの制御構造を再利用します。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. ロック待ち時間</li><li>B. DDF再同期ポート番号</li><li>C. CACHEDYN有効化 <span class="kb-ok">✅ 正解</span></li><li>D. 表スペース停止方式</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 動的SQLの準備結果をキャッシュして再利用するため、Cが該当します。Aはロック要求の待ち時間、Bは分散トランザクション復旧用の口です。Dはオブジェクトを止める運用操作で、SQL準備費用の削減とは目的が異なります；背景には動的SQLの再準備を減らすCACHEDYNは、Db2 for z/OSのロック・メモリ・実行資源パラメータとして、動的ステートメントキャッシュを有効にするかに関わります、同じSQLが繰り返し発行される環境では、EDMステートメント領域の容量とキャッシュヒットを合わせて評価しますという関係があり、この区別で確認する名称は「CACHEDYN」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance / Db2_zOS_Troubleshooting / Db2_zOS_Command_Reference</p></div></details></section>


<section class="kb-item" id="c07-i0210"><h3>DEADLOCK TIME</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>DEADLOCK TIMEは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複数トランザクションが互いにロックを待つ状態を、どの周期で見つけに行くかを調整します。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. 接続プール総数</li><li>B. 循環検出周期 <span class="kb-ok">✅ 正解</span></li><li>C. BSDS再同期用ポート番号</li><li>D. 動的SQLキャッシュ有効化</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> ロックの循環待ちを探すタイミングを決めるので、Bを選びます。AはDDF接続数の設計で、Cは分散トランザクション復旧用のポートです。DはSQL準備結果の再利用領域であり、ロック競合の発見タイミングとは別の資源です；背景にはデッドロック検出の間隔を決めるDEADLOCK TIMEは、Db2 for z/OSのロック・メモリ・実行資源パラメータとして、IRLMが循環待ちを探す周期に関係します、短くしすぎると監視負荷が増え、長すぎると競合状態の解消が遅れるため、ロック待ち調査と合わせて見ますという関係があり、この区別で確認する名称は「DEADLOCK」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance / Db2_zOS_Troubleshooting / Db2_zOS_Command_Reference</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEADLOCK TIME</strong></p><p>検証目的: 優先検査のロック・メモリ・実行資源について、DEADLOCK TIME は、Db2の Db2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、優先検査のロック・メモリ・実行資源の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDEADLOCK TIMEを指定し、OSKB020072の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DEADLOCK TIME
CASE OSKB020072
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DEADLOCK TIME
CASE OSKB020072
SOURCE Db2 for z/OS
DEADLOCK TIMEとOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020072を同じ出力で読み、優先検査のロック・メモリ・実行資源の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020072
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020072
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020072
DSNV401IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DEADLOCK TIME と OSKB020072 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020072 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0211"><h3>EDM pool</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>EDM poolは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0212"><h3>IRLMRWT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 上級</p><p>IRLMRWTは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0213"><h3>LOCK TIMEOUT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>LOCK TIMEOUTは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0214"><h3>LOCKMAX</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>LOCKMAXは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 特定表スペースのみロック数の上限を変え、サブシステム既定より個別定義を優先して管理します。確認する属性はどれですか。</p><ul class="kb-choices"><li>A. 再同期ポート番号</li><li>B. LOCKMAX属性 <span class="kb-ok">✅ 正解</span></li><li>C. EDM DBDプール</li><li>D. SQLCA戻り領域</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表スペース定義でロック上限を指定する属性なので、Bが適切です。Aは二相コミット復旧用の通信口です。Cはデータベース記述子を保持するEDM領域、DはアプリケーションがSQL結果を受け取る領域です。既定値との関係も確認します；背景には個別オブジェクトのロック数を縛るLOCKMAXは、Db2 for z/OSのロック・メモリ・実行資源パラメータ群と連動し、表スペース定義で取得可能なロック数の上限を指定します、既定値はNUMLKTSの影響を受けるため、表スペース定義とサブシステム値を一緒に確認しますという関係があり、この区別で確認する名称は「LOCKMAX」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance / Db2_zOS_Troubleshooting / Db2_zOS_Command_Reference</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOCKMAX</strong></p><p>検証目的: 順序検査のロック・メモリ・実行資源について、LOCKMAX は、Db2の Db2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行としに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、順序検査のロック・メモリ・実行資源の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にLOCKMAXを指定し、OSKB020075の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND LOCKMAX
CASE OSKB020075
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM LOCKMAX
CASE OSKB020075
SOURCE Db2 for z/OS
LOCKMAXとOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020075を同じ出力で読み、順序検査のロック・メモリ・実行資源の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020075
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020075
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020075
DSNV401IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の LOCKMAX と OSKB020075 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020075 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0215"><h3>NUMLKTS</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>NUMLKTSは、Db2内部のメモリ、ロック、待ち、バッファー、ページ管理に関わる資源項目です。性能問題や可用性低下を調べるときに、どの資源が詰まっているかを切り分ける入口になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 表スペースごとに許すロック数の既定値をサブシステム側で決め、個別定義のLOCKMAXとの関係を確認します。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. 表スペース別既定 <span class="kb-ok">✅ 正解</span></li><li>B. 安全接続ポート番号</li><li>C. 動的SQL再利用指定</li><li>D. RIDプール不足時の代替処理</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 表スペースに適用されるロック上限の既定に関わるため、Aを選びます。BはTLS系分散接続の入口で、Cは動的SQLの準備結果を再利用する指定です。DはリストプリフェッチでRID領域が足りないときのアクセスパス変化を指します；背景には表スペース単位の既定ロック上限を決めるNUMLKTSは、Db2 for z/OSのロック・メモリ・実行資源パラメータとして、CREATE TABLESPACEのLOCKMAX既定値に関係します、大量更新で表スペース内のロックが増える場合、LOCKMAX句とサブシステム既定のどちらが効くかを確認しますという関係があり、この区別で確認する名称は「NUMLKTS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance / Db2_zOS_Troubleshooting / Db2_zOS_Command_Reference</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NUMLKTS</strong></p><p>検証目的: 比較検査のロック・メモリ・実行資源について、NUMLKTS は、Db2内部のメモリ、ロック、待ち、バッファー、ページ管理に関わる資源項目です。性能問題や可用性低下を調べるときに、どの資源が詰まっているかを切り分ける入口に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、比較検査のロック・メモリ・実行資源の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にNUMLKTSを指定し、OSKB020074の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND NUMLKTS
CASE OSKB020074
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM NUMLKTS
CASE OSKB020074
SOURCE Db2 for z/OS
NUMLKTSとOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020074を同じ出力で読み、比較検査のロック・メモリ・実行資源の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020074
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020074
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020074
DSNV401IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の NUMLKTS と OSKB020074 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020074 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>


<section class="kb-item" id="c07-i0216"><h3>NUMLKUS</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>NUMLKUSは、Db2内部のメモリ、ロック、待ち、バッファー、ページ管理に関わる資源項目です。性能問題や可用性低下を調べるときに、どの資源が詰まっているかを切り分ける入口になります。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 一つの処理が大量の行ロックを保持し、IRLM資源を圧迫しないよう個別の上限を決めます。該当する設定対象はどれですか。</p><ul class="kb-choices"><li>A. バッファプールページ数</li><li>B. アーカイブログデータセット数</li><li>C. TCP/IP上のDDF識別名</li><li>D. ユーザー別上限 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 一つの実行主体が保持できるロック数を制限する指定なので、Dを選びます。Aはデータページのキャッシュ容量、Bは回復用ログ資材の数です。Cは分散接続で使うDDF側の名前で、IRLMのロック保持量ではありません；背景には利用者単位のロック上限を決めるNUMLKUSは、Db2 for z/OSのロック・メモリ・実行資源パラメータとして、単一アプリケーションが取得できるページ、行、LOBロック数の最大値を制御します、無制限に近い値はIRLMストレージ不足につながるため、コミット頻度やSQL設計も合わせて見直しますという関係があり、この区別で確認する名称は「NUMLKUS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance / Db2_zOS_Troubleshooting / Db2_zOS_Command_Reference</p></div></details></section>


<section class="kb-item" id="c07-i0217"><h3>RID pool</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>RID poolは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


<section class="kb-item" id="c07-i0218"><h3>buffer pool defaults</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>buffer pool defaultsは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> データページをメモリに保持してディスク入出力を減らす領域について、サイズやしきい値の初期値を確認します。該当する資源はどれですか。</p><ul class="kb-choices"><li>A. バッファプール既定値 <span class="kb-ok">✅ 正解</span></li><li>B. CURRENT SCHEMA値</li><li>C. ユーティリティID</li><li>D. BSDS二重化</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> データページをキャッシュするバッファプールの初期属性なので、Aを選びます。(B)はSQL名解決で使うスキーマ値、(C)は保守ジョブの実行単位です。(D)はログ管理資材の冗長化であり、データページのメモリ保持とは別です；背景にはバッファプールの既定属性は、Db2 for z/OSのロック・メモリ・実行資源として、インストール時に定義されるバッファプールサイズやしきい値の初期値に関係します、運用中はALTER BUFFERPOOLや統計レポートで、読み取り遅延や書き出し傾向を確認しますという関係があり、この区別で確認する名称は「defaults」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance / Db2_zOS_Troubleshooting / Db2_zOS_Command_Reference</p></div></details></section>


<section class="kb-item" id="c07-i0219"><h3>sort pool</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; ロック・メモリ・実行資源 ・ 難易度: 中級</p><p>sort poolは、Db2のDb2内部資源に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></section>


## サブシステムパラメータ > 導入・初期化・起動反映


<section class="kb-item" id="c07-i0220"><h3>APPLCOMPAT subsystem parameter</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 上級</p><p>APPLCOMPAT subsystem parameterは、Db2の導入/起動に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_WhatsNew.pdf p.334 / Db2_zOS_Installation.pdf p.508</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 機能レベルを進めた後も、アプリケーションが利用できるSQL機能の水準を段階的に制御します。該当するサブシステム値はどれですか。</p><ul class="kb-choices"><li>A. LOCKMAX</li><li>B. APPLCOMPAT既定値 <span class="kb-ok">✅ 正解</span></li><li>C. DDF LOCATION</li><li>D. SRTPOOL</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> SQL機能水準の既定を管理する値なので、Bが該当します。誤答Aは表スペースのロック上限、誤答Cは分散接続先名です。誤答Dはソート作業領域に関係する値で、アプリケーション互換性レベルの制御とは別です。機能レベル移行で確認します；背景には互換性レベルの既定を決めるサブシステム値が APPLCOMPAT subsystem parameter です、機能レベルを上げた Db2 で、アプリケーションがどの SQL 機能水準で動くかを段階的に管理します、新機能の利用開始を一斉ではなく管理下で進めるための値ですという関係があり、この区別で確認する名称は「APPLCOMPAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages</p></div></details></section>


<section class="kb-item" id="c07-i0221"><h3>DDF情報のBSDS更新</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 中級</p><p>DDF情報のBSDS更新は、Db2の導入/起動に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance p.216</p></section>


<section class="kb-item" id="c07-i0222"><h3>DSNHDECP</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 中級</p><p>DSNHDECPは、Db2サブシステム・パラメータ、導入資材、起動時反映に関わる項目です。DSNZPARMや導入ジョブとの関係を押さえ、変更がいつ有効になるかを確認します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance p.216</p></section>


<section class="kb-item" id="c07-i0223"><h3>DSNTIJUA</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 中級</p><p>DSNTIJUAは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance p.216</p></section>


<section class="kb-item" id="c07-i0224"><h3>DSNTIJUZ</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 中級</p><p>DSNTIJUZは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance p.216</p></section>


<section class="kb-item" id="c07-i0225"><h3>DSNZPxxx</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 中級</p><p>DSNZPxxxは、Db2の導入/起動に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance p.216</p></section>


<section class="kb-item" id="c07-i0226"><h3>RTN_PKG_APPLCOMPAT</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 上級</p><p>RTN_PKG_APPLCOMPATは、Db2の導入/起動に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_WhatsNew.pdf p.334 / Db2_zOS_Installation.pdf p.508</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> Db2提供ルーチンのパッケージをBINDまたはREBINDするとき、APPLCOMPATをどの値で付けるかを調整します。該当する設定はどれですか。</p><ul class="kb-choices"><li>A. MAXDBAT</li><li>B. DSNHDECP</li><li>C. ルーチン用APPLCOMPAT <span class="kb-ok">✅ 正解</span></li><li>D. DSNJU003 DELETE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 提供ルーチンのパッケージ互換性を決める設定なので、Cを使います。誤答Aは活動DBAT数の上限、誤答Bはアプリケーション既定値モジュールです。誤答DはBSDS操作の別用途で、ルーチンのBIND文生成とは関係しません；背景には提供ルーチンの BIND または REBIND で使う互換性値を決める DB2OPT 設定が RTN_PKG_APPLCOMPAT です、導入・初期化のルーチン構成では、DEFAULT 時に APPLCOMPAT サブシステム値が使われるため、DSNTIJRT や DSNTRIN が生成する BIND 文を確認しますという関係があり、この区別で確認する名称は「RTN_PKG_APPLCOMPAT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RTN_PKG_APPLCOMPAT</strong></p><p>検証目的: 探索検査の導入・初期化・起動反映について、RTN_PKG_APPLCOMPAT は、Db2の導入/起動に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、探索検査の導入・初期化・起動反映の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にRTN_PKG_APPLCOMPATを指定し、OSKB020066の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RTN_PKG_APPLCOMPAT
CASE OSKB020066
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RTN_PKG_APPLCOMPAT
CASE OSKB020066
SOURCE Db2 for z/OS
RTN_PKG_APPLCOMPATとOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020066を同じ出力で読み、探索検査の導入・初期化・起動反映の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020066
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020066
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020066
DSNV401IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RTN_PKG_APPLCOMPAT と OSKB020066 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_WhatsNew.pdf p.334 / Db2_zOS_Installation.pdf p.508</p></div></details></section>


<section class="kb-item" id="c07-i0227"><h3>START DB2 PARM</h3><p class="kb-meta">分類: サブシステムパラメータ &gt; 導入・初期化・起動反映 ・ 難易度: 中級</p><p>START DB2 PARMは、Db2の導入/起動に関わるサブシステム・パラメータ候補です。変更元、反映タイミング、起動後に確認する状態を結び付けて理解します</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Performance p.216</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 起動時に読み込むZPARMモジュールを明示し、通常とは別のサブシステムパラメータでDb2を開始します。使う指定はどれですか。</p><ul class="kb-choices"><li>A. 起動時PARM指定 <span class="kb-ok">✅ 正解</span></li><li>B. DDF安全ポート番号</li><li>C. RIDプール容量</li><li>D. 統計履歴表</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Db2開始時に使うZPARM名を指定するため、Aを選びます。誤答Bは暗号化された分散接続の入口です。誤答Cはリストプリフェッチの作業領域で、誤答Dはアクセスパス診断に使うカタログ統計の履歴です。起動プロシージャの値も確認します；背景には起動時に使う ZPARM 名を明示する指定が START DB2 PARM です、サブシステムパラメータの起動反映では、-START DB2 の PARM オプションや ssnmMSTR 起動プロシージャの ZPARM 指定で、どの DSNZPxxx を読むかを切り替えますという関係があり、この区別で確認する名称は「START」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages</p></div></details></section>


## ストレージ構造


<section class="kb-item" id="c07-i0228"><h3>ストレージグループ</h3><p class="kb-meta">分類: ストレージ構造 ・ 難易度: 中級</p><p>Db2 for z/OS の ストレージ構造で扱うストレージグループは、Db2 がデータセットを割り振る候補ボリューム群を表します。表スペースや索引の作成時に、どの装置群を使うかを間接的に制御します。容量計画では z/OS SMS やボリューム配置と合わせて確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認のストレージグループでストレージグループの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ストレージグループの出力を取らず探索確認のストレージグループの説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. -DISPLAY THREAD(*)を省略して探索確認のストレージグループの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認のストレージグループへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠ではストレージグループは「探索確認のストレージグループに関係する定義値と表示行を照合する探索確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡ではストレージグループの属性行と DSNV401I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出ではストレージグループを Db2 for z/OS の運用手順で確認し、初出名は探索確認初出です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ストレージグループ</strong></p><p>検証目的: 探索確認のストレージグループについて、Db2 for z/OS の ストレージ構造で扱うストレージグループは、Db2 がデータセットを割り振る候補ボリューム群を表します。表スペースや索引の作成時に、どの装置群をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD(*) を入力し、探索確認のストレージグループの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にストレージグループを指定し、OSKB010006の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND ストレージグループ
CASE OSKB010006
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM ストレージグループ
CASE OSKB010006
SOURCE Db2 for z/OS
ストレージグループとOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010006を同じ出力で読み、探索確認のストレージグループの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
CASE OSKB010006
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010006
-DISPLAY THREAD(*)
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010006
DSNV401IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD(*) が画面・出力に表示されること
② ステップ2 の ストレージグループ と OSKB010006 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


<section class="kb-item" id="c07-i0229"><h3>データベース</h3><p class="kb-meta">分類: ストレージ構造 ・ 難易度: 初級</p><p>Db2 for z/OS の ストレージ構造で扱うデータベースは、Db2 のデータベースは、表スペースや索引スペースをまとめる論理的な入れ物です。業務上のアプリケーション単位と完全に一致するとは限らず、管理、権限、バックアップの境界として使われます。DISPLAY DATABASE などで状態を確認する入口になります</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


<section class="kb-item" id="c07-i0230"><h3>索引スペース</h3><p class="kb-meta">分類: ストレージ構造 ・ 難易度: 中級</p><p>Db2 for z/OS の ストレージ構造で扱う索引スペースは、索引データを保持する Db2 の記憶構造です。索引の状態が悪いとアクセスパス、ユニーク制約、ユーティリティ処理に影響します。表スペースの回復や再編成では、関連する索引スペースの状態も合わせて確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


<section class="kb-item" id="c07-i0231"><h3>表スペース</h3><p class="kb-meta">分類: ストレージ構造 ・ 難易度: 初級</p><p>Db2 for z/OS の ストレージ構造で扱う表スペースは、Db2 表データを格納する主要な記憶構造です。分割方式、ページサイズ、ロック粒度、ユーティリティ状態が性能と保守作業に影響します。障害対応では表名だけでなく、対応する表スペース名と状態を確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></section>


## セキュリティ


<section class="kb-item" id="c07-i0232"><h3>Db2 権限モデル</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>Db2 for z/OS の セキュリティで扱うDb2 権限モデルは、Db2 の権限モデルは、システム権限、データベース権限、表やパッケージへの権限を組み合わせて制御します。RACF だけで完結せず、Db2 カタログ上の GRANT 状態も確認します。監査では誰が何に対してどの権限を持つかを分けて見ます</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認の権限モデルに関する Db2 権限モデルの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. -DISPLAY THREAD(*)の結果を残さず値域確認の権限モデルの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の権限モデルの証跡として保存して根拠にする。</li><li>C. Db2 権限モデルの変更点を出力本文から切り離して値域確認の権限モデルの承認欄のみ残す。</li><li>D. 同じ画面で対象行と DSNV401I を読み、値域確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Db2 権限モデル は「Db2 権限モデルの状態と出力メッセージを結び付ける値域確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Db2 権限モデルの出力行と DSNV401I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Db2 権限モデルを Db2 for z/OS の確認記録に残し、対象名は値域確認対象です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Db2 権限モデル</strong></p><p>検証目的: 値域確認の権限モデルについて、Db2 for z/OS の セキュリティで扱う Db2 権限モデルは、Db2 の権限モデルは、システム権限、データベース権限、表やパッケージへの権限を組み合わせて制御しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD(*) を入力し、値域確認の権限モデルの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にDb2 権限モデルを指定し、OSKB010016の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND Db2 権限モデル
CASE OSKB010016
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM Db2 権限モデル
CASE OSKB010016
SOURCE Db2 for z/OS
Db2 権限モデルとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010016を同じ出力で読み、値域確認の権限モデルの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
CASE OSKB010016
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010016
-DISPLAY THREAD(*)
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010016
DSNV401IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD(*) が画面・出力に表示されること
② ステップ2 の Db2 権限モデル と OSKB010016 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


<section class="kb-item" id="c07-i0233"><h3>SYSADM 権限</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>Db2 for z/OS の セキュリティで扱うSYSADM 権限は、SYSADM は、Db2 サブシステム管理に強い権限を持つ管理者権限です。通常のデータ参照権限とは違い、システム設定やオブジェクト管理に広く影響します。付与対象は最小限にし、監査証跡と職務分掌を確認します</p><p class="kb-src"><strong>出典:</strong> Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認の権限に関係する SYSADM 権限の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. -DISPLAY THREAD(*)で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. SYSADM 権限の名称と担当者名のみを残して警告確認の権限の表示本文を確認対象に含めない。</li><li>C. データベース管理以外の画面で警告確認の権限を確認し同じ証跡として扱ったことにする。</li><li>D. DSNV401I の有無を見ず警告確認の権限の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では SYSADM 権限 は「SYSADM 権限の用途をデータベース管理の表示で確認する警告確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では Db2 for z/OS の SYSADM 権限と DSNV401I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では SYSADM 権限を Db2 for z/OS で扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYSADM 権限</strong></p><p>検証目的: 警告確認の権限について、Db2 for z/OS の セキュリティで扱う SYSADM 権限は、SYSADM は、Db2 サブシステム管理に強い権限を持つ管理者権限です。通常のデータ参照権限とは違いに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD(*) を入力し、警告確認の権限の確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にSYSADM 権限を指定し、OSKB010017の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND SYSADM 権限
CASE OSKB010017
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM SYSADM 権限
CASE OSKB010017
SOURCE Db2 for z/OS
SYSADM 権限とOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010017を同じ出力で読み、警告確認の権限の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD(*)
CASE OSKB010017
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010017
-DISPLAY THREAD(*)
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010017
DSNV401IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD(*) が画面・出力に表示されること
② ステップ2 の SYSADM 権限 と OSKB010017 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security</p></div></details></section>


## バッファ・ストレージ・ロック > バッファプール


<section class="kb-item" id="c07-i0234"><h3>BP0</h3><p class="kb-meta">分類: バッファ・ストレージ・ロック &gt; バッファプール ・ 難易度: 中級</p><p>BP0は、Db2 for z/OSのバッファプールで用いるDb2内部のメモリ、ロック、待ち、バッファー、ページ管理に関わる資源項目です。性能問題や可用性低下を調べるときに、どの資源が詰まっているかを切り分ける入口になります。バッファプールでは、指定値と対象資源、実行時の出力を突き合わせて確認する。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> catalog 関連の page 読み込みが増え、基本 pool の入出力を確認します。最初に見る対象はどれですか。</p><ul class="kb-choices"><li>A. BP0 <span class="kb-ok">✅ 正解</span></li><li>B. archive log</li><li>C. role grant</li><li>D. CALL body</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 基本的な 4KB page の pool なので、A が正解です。B: recovery 用に退避される log です。C: 権限を role に与える操作です。D: stored procedure の呼び出し本体です。BP0 は catalog 影響を含めて扱います；背景にはBP0 は、Db2 for z/OS のバッファプールのうち基本的な 4KB page を扱う pool 名です、catalog や directory の object も関係するため、むやみに枯渇させると全体の応答へ響きます、調査では BP0 の hit ratio、同期入出力、関連 object の割り当てを分けて読みますという関係があり、この区別で確認する名称は「BP0」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference.pdf p.46 / Db2_zOS_Command_Reference.pdf p.48 / Db2_zOS_Performance.pdf p.48 / Db2_zOS_Performance.pdf p.68 / Db2_zOS_Messages.pdf p.105 / Db2_zOS_Installation.pdf p.274 / Db2_zOS_Data_Sharing.pdf p.16 / Db2_zOS_Installation.pdf p.747</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BP0</strong></p><p>検証目的: 出力確認のバッファプールについて、BP0 は、Db2 for z/OS のバッファプールで用いる Db2内部のメモリ、ロック、待ち、バッファー、ページ管理に関わる資源項目です。性能問題や可用性低下を調べるときに、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、出力確認のバッファプールの確認表示へ進みます。
［操作（入力）］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
→ Enter を押す
［画面・出力］
(Db2 Command)
COMMAND INPUT ===&gt; -DISPLAY THREAD
COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はDb2 Commandの表示結果です。FIND欄にBP0を指定し、OSKB020008の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND BP0
CASE OSKB020008
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM BP0
CASE OSKB020008
SOURCE Db2 for z/OS
BP0とOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020008を同じ出力で読み、出力確認のバッファプールの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020008
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020008
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020008
DSNV401IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の BP0 と OSKB020008 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>
