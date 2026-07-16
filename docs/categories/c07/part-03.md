---
search:
  exclude: true
---

# Db2 for z/OS — 詳細 (3/3)

[← Db2 for z/OS の概要へ戻る](index.md)


## その他


<section class="kb-item" id="c07-other"><h3>その他（特定項目に紐づかないQA・手順）</h3><p class="kb-meta">項目名が個別の技術項目に一致しなかったQA・手順です。</p><details class="kb-block"><summary>確認問題（109問）</summary><div class="kb-q"><p><strong>問題.</strong> 最適化ヒントを導入設計で確認します。Db2の作業記録に最適化ヒントの利用の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. QUERYACCELERATION</li><li>C. VALIDATE</li><li>D. OPTHINT <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答最適化ヒントはDです。論点最適化ヒントにおける指定名 OPTHINT の確認軸名は最適化ヒント確認です。ヒントが現行エスキューエルと一致するか確認しますので、目的名は最適化ヒント目的です。最適化ヒントで読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は最適化ヒント説明です。誤答A最適化ヒントは成果物の所有者の選択で、主題は最適化ヒントです。除外A最適化ヒントでは成果物の所有者を外す理由も最適化ヒント誤答です。誤答B最適化ヒントはアクセラレーター利用方針の選択で、主題は最適化ヒントです。除外B最適化ヒントではアクセラレーター利用方針を外す理由も最適化ヒント誤答です。誤答C最適化ヒントは検査時期の選択で、主題は最適化ヒントです。除外C最適化ヒントでは検査時期を外す理由も最適化ヒント誤答です。Dが正解です。論点最適化ヒントの指定名 OPTHINT が該当します。目的最適化ヒントで読む説明表の根拠名は最適化ヒント根拠です。初出語最適化ヒントとして、指定名 OPTHINT はDb2の指定または確認表であり焦点は最適化ヒント定義です。位置付け最適化ヒントは最適化ヒントの利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 加速器利用を導入設計で確認します。Db2の作業記録にアクセラレーター利用の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. QUERYACCELERATION <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. APCOMPARE</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答加速器利用はAです。論点加速器利用における指定名 QUERYACCELERATION の確認軸名は加速器利用確認です。加速対象外の戻り動作も確認しますので、目的名は加速器利用目的です。加速器利用で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は加速器利用説明です。Aが正解です。論点加速器利用の指定名 QUERYACCELERATION が該当します。目的加速器利用で読むパッケージカタログの根拠名は加速器利用根拠です。誤答B加速器利用は分離レベルの選択で、主題は加速器利用です。除外B加速器利用では分離レベルを外す理由も加速器利用誤答です。誤答C加速器利用はアクセスパス差分の比較の選択で、主題は加速器利用です。除外C加速器利用ではアクセスパス差分の比較を外す理由も加速器利用誤答です。誤答D加速器利用はパッケージコピーの保持の選択で、主題は加速器利用です。除外D加速器利用ではパッケージコピーの保持を外す理由も加速器利用誤答です。初出語加速器利用として、指定名 QUERYACCELERATION はDb2の指定または確認表であり焦点は加速器利用定義です。位置付け加速器利用はアクセラレーター利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 文集約を導入設計で確認します。Db2の作業記録に動的エスキューエル文の集約の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. DEGREE</li><li>C. CONCENTRATESTMT <span class="kb-ok">✅ 正解</span></li><li>D. ACTION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答文集約はCです。論点文集約における指定名 CONCENTRATESTMT の確認軸名は文集約確認です。動的ステートメントキャッシュの効率を確認しますので、目的名は文集約目的です。文集約で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は文集約説明です。誤答A文集約はパッケージコピーの保持の選択で、主題は文集約です。除外A文集約ではパッケージコピーの保持を外す理由も文集約誤答です。誤答B文集約は並列実行の許可の選択で、主題は文集約です。除外B文集約では並列実行の許可を外す理由も文集約誤答です。Cが正解です。論点文集約の指定名 CONCENTRATESTMT が該当します。目的文集約で読むパッケージカタログの根拠名は文集約根拠です。誤答D文集約は追加と置換の扱いの選択で、主題は文集約です。除外D文集約では追加と置換の扱いを外す理由も文集約誤答です。初出語文集約として、指定名 CONCENTRATESTMT はDb2の指定または確認表であり焦点は文集約定義です。位置付け文集約は動的エスキューエル文の集約位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路再利用を導入設計で確認します。Db2の作業記録に前回アクセスパスの再利用の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. APREUSE <span class="kb-ok">✅ 正解</span></li><li>B. QUERYACCELERATION</li><li>C. QUERYACCELERATION</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路再利用はAです。論点経路再利用における指定名 APREUSE の確認軸名は経路再利用確認です。再利用できないエスキューエルを説明表で確認しますので、目的名は経路再利用目的です。経路再利用で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路再利用説明です。Aが正解です。論点経路再利用の指定名 APREUSE が該当します。目的経路再利用で読む説明表の根拠名は経路再利用根拠です。誤答B経路再利用はアクセラレーター利用方針の選択で、主題は経路再利用です。除外B経路再利用ではアクセラレーター利用方針を外す理由も経路再利用誤答です。誤答C経路再利用はアクセラレーター利用方針の選択で、主題は経路再利用です。除外C経路再利用ではアクセラレーター利用方針を外す理由も経路再利用誤答です。誤答D経路再利用は準備済み動的SQL文の保持の選択で、主題は経路再利用です。除外D経路再利用では準備済み動的SQL文の保持を外す理由も経路再利用誤答です。初出語経路再利用として、指定名 APREUSE はDb2の指定または確認表であり焦点は経路再利用定義です。位置付け経路再利用は前回アクセスパスの再利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路比較を導入設計で確認します。Db2の作業記録にアクセスパス差分の比較の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. ENCODING</li><li>B. APCOMPARE <span class="kb-ok">✅ 正解</span></li><li>C. EXPLAIN(ONLY)</li><li>D. EXPLAIN(ONLY)</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路比較はBです。論点経路比較における指定名 APCOMPARE の確認軸名は経路比較確認です。経路比較メッセージと説明表の結果を照合しますので、目的名は経路比較目的です。経路比較で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路比較説明です。誤答A経路比較は文字データの符号化の選択で、主題は経路比較です。除外A経路比較では文字データの符号化を外す理由も経路比較誤答です。Bが正解です。論点経路比較の指定名 APCOMPARE が該当します。目的経路比較で読む説明表の根拠名は経路比較根拠です。誤答C経路比較は候補アクセスパスの事前出力の選択で、主題は経路比較です。除外C経路比較では候補アクセスパスの事前出力を外す理由も経路比較誤答です。誤答D経路比較は候補アクセスパスの事前出力の選択で、主題は経路比較です。除外D経路比較では候補アクセスパスの事前出力を外す理由も経路比較誤答です。初出語経路比較として、指定名 APCOMPARE はDb2の指定または確認表であり焦点は経路比較定義です。位置付け経路比較はアクセスパス差分の比較位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前説明出力を導入設計で確認します。Db2の作業記録に再バインドを完了せずに候補を見るの根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. QUALIFIER</li><li>C. EXPLAIN(ONLY) <span class="kb-ok">✅ 正解</span></li><li>D. ISOLATION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答事前説明出力はCです。論点事前説明出力における指定名 EXPLAIN(ONLY) の確認軸名は事前説明出力確認です。変更影響を本番反映前に評価しますので、目的名は事前説明出力目的です。事前説明出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前説明出力説明です。誤答A事前説明出力は前回コピーへの切り替えの選択で、主題は事前説明出力です。除外A事前説明出力では前回コピーへの切り替えを外す理由も事前説明出力誤答です。誤答B事前説明出力は未修飾表名のスキーマの選択で、主題は事前説明出力です。除外B事前説明出力では未修飾表名のスキーマを外す理由も事前説明出力誤答です。Cが正解です。論点事前説明出力の指定名 EXPLAIN(ONLY) が該当します。目的事前説明出力で読む説明表の根拠名は事前説明出力根拠です。誤答D事前説明出力は分離レベルの選択で、主題は事前説明出力です。除外D事前説明出力では分離レベルを外す理由も事前説明出力誤答です。初出語事前説明出力として、指定名 EXPLAIN(ONLY) はDb2の指定または確認表であり焦点は事前説明出力定義です。位置付け事前説明出力は再バインドを完了せずに候補を見る位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 前回版切替を導入設計で確認します。Db2の作業記録に前回コピーへの切り替えの根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. DYNAMICRULES</li><li>C. EXPLAIN</li><li>D. SWITCH(PREVIOUS) <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答前回版切替はDです。論点前回版切替における指定名 SWITCH(PREVIOUS) の確認軸名は前回版切替確認です。性能劣化時の即時切り戻しを支えますので、目的名は前回版切替目的です。前回版切替で読むパッケージコピー表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は前回版切替説明です。誤答A前回版切替は成果物の所有者の選択で、主題は前回版切替です。除外A前回版切替では成果物の所有者を外す理由も前回版切替誤答です。誤答B前回版切替は動的SQLの権限文脈の選択で、主題は前回版切替です。除外B前回版切替では動的SQLの権限文脈を外す理由も前回版切替誤答です。誤答C前回版切替はアクセスパス情報の出力の選択で、主題は前回版切替です。除外C前回版切替ではアクセスパス情報の出力を外す理由も前回版切替誤答です。Dが正解です。論点前回版切替の指定名 SWITCH(PREVIOUS) が該当します。目的前回版切替で読むパッケージコピー表の根拠名は前回版切替根拠です。初出語前回版切替として、指定名 SWITCH(PREVIOUS) はDb2の指定または確認表であり焦点は前回版切替定義です。位置付け前回版切替は前回コピーへの切り替え位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 最適化ヒントを変更審査で確認します。Db2の作業記録に最適化ヒントの利用の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. OPTHINT <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. APCOMPARE</li><li>D. PLANMGMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答最適化ヒントはAです。論点最適化ヒントにおける指定名 OPTHINT の確認軸名は最適化ヒント確認です。ヒントが現行エスキューエルと一致するか確認しますので、目的名は最適化ヒント目的です。最適化ヒントで読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は最適化ヒント説明です。Aが正解です。論点最適化ヒントの指定名 OPTHINT が該当します。目的最適化ヒントで読む説明表の根拠名は最適化ヒント根拠です。誤答B最適化ヒントは分離レベルの選択で、主題は最適化ヒントです。除外B最適化ヒントでは分離レベルを外す理由も最適化ヒント誤答です。誤答C最適化ヒントはアクセスパス差分の比較の選択で、主題は最適化ヒントです。除外C最適化ヒントではアクセスパス差分の比較を外す理由も最適化ヒント誤答です。誤答D最適化ヒントはパッケージコピーの保持の選択で、主題は最適化ヒントです。除外D最適化ヒントではパッケージコピーの保持を外す理由も最適化ヒント誤答です。初出語最適化ヒントとして、指定名 OPTHINT はDb2の指定または確認表であり焦点は最適化ヒント定義です。位置付け最適化ヒントは最適化ヒントの利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 加速器利用を変更審査で確認します。Db2の作業記録にアクセラレーター利用の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. QUERYACCELERATION <span class="kb-ok">✅ 正解</span></li><li>C. OWNER</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答加速器利用はBです。論点加速器利用における指定名 QUERYACCELERATION の確認軸名は加速器利用確認です。加速対象外の戻り動作も確認しますので、目的名は加速器利用目的です。加速器利用で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は加速器利用説明です。誤答A加速器利用は動的SQLの権限文脈の選択で、主題は加速器利用です。除外A加速器利用では動的SQLの権限文脈を外す理由も加速器利用誤答です。Bが正解です。論点加速器利用の指定名 QUERYACCELERATION が該当します。目的加速器利用で読むパッケージカタログの根拠名は加速器利用根拠です。誤答C加速器利用は成果物の所有者の選択で、主題は加速器利用です。除外C加速器利用では成果物の所有者を外す理由も加速器利用誤答です。誤答D加速器利用は動的SQL文の集約の選択で、主題は加速器利用です。除外D加速器利用では動的SQL文の集約を外す理由も加速器利用誤答です。初出語加速器利用として、指定名 QUERYACCELERATION はDb2の指定または確認表であり焦点は加速器利用定義です。位置付け加速器利用はアクセラレーター利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 文集約を変更審査で確認します。Db2の作業記録に動的エスキューエル文の集約の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. CURRENTDATA</li><li>B. EXPLAIN</li><li>C. DYNAMICRULES</li><li>D. CONCENTRATESTMT <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答文集約はDです。論点文集約における指定名 CONCENTRATESTMT の確認軸名は文集約確認です。動的ステートメントキャッシュの効率を確認しますので、目的名は文集約目的です。文集約で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は文集約説明です。誤答A文集約はカーソル読み取りの現在性の選択で、主題は文集約です。除外A文集約ではカーソル読み取りの現在性を外す理由も文集約誤答です。誤答B文集約はアクセスパス情報の出力の選択で、主題は文集約です。除外B文集約ではアクセスパス情報の出力を外す理由も文集約誤答です。誤答C文集約は動的SQLの権限文脈の選択で、主題は文集約です。除外C文集約では動的SQLの権限文脈を外す理由も文集約誤答です。Dが正解です。論点文集約の指定名 CONCENTRATESTMT が該当します。目的文集約で読むパッケージカタログの根拠名は文集約根拠です。初出語文集約として、指定名 CONCENTRATESTMT はDb2の指定または確認表であり焦点は文集約定義です。位置付け文集約は動的エスキューエル文の集約位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路再利用を変更審査で確認します。Db2の作業記録に前回アクセスパスの再利用の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. ENCODING</li><li>B. APREUSE <span class="kb-ok">✅ 正解</span></li><li>C. EXPLAIN(ONLY)</li><li>D. EXPLAIN(ONLY)</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路再利用はBです。論点経路再利用における指定名 APREUSE の確認軸名は経路再利用確認です。再利用できないエスキューエルを説明表で確認しますので、目的名は経路再利用目的です。経路再利用で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路再利用説明です。誤答A経路再利用は文字データの符号化の選択で、主題は経路再利用です。除外A経路再利用では文字データの符号化を外す理由も経路再利用誤答です。Bが正解です。論点経路再利用の指定名 APREUSE が該当します。目的経路再利用で読む説明表の根拠名は経路再利用根拠です。誤答C経路再利用は候補アクセスパスの事前出力の選択で、主題は経路再利用です。除外C経路再利用では候補アクセスパスの事前出力を外す理由も経路再利用誤答です。誤答D経路再利用は候補アクセスパスの事前出力の選択で、主題は経路再利用です。除外D経路再利用では候補アクセスパスの事前出力を外す理由も経路再利用誤答です。初出語経路再利用として、指定名 APREUSE はDb2の指定または確認表であり焦点は経路再利用定義です。位置付け経路再利用は前回アクセスパスの再利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路比較を変更審査で確認します。Db2の作業記録にアクセスパス差分の比較の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. QUALIFIER</li><li>C. APCOMPARE <span class="kb-ok">✅ 正解</span></li><li>D. ISOLATION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路比較はCです。論点経路比較における指定名 APCOMPARE の確認軸名は経路比較確認です。経路比較メッセージと説明表の結果を照合しますので、目的名は経路比較目的です。経路比較で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路比較説明です。誤答A経路比較は前回コピーへの切り替えの選択で、主題は経路比較です。除外A経路比較では前回コピーへの切り替えを外す理由も経路比較誤答です。誤答B経路比較は未修飾表名のスキーマの選択で、主題は経路比較です。除外B経路比較では未修飾表名のスキーマを外す理由も経路比較誤答です。Cが正解です。論点経路比較の指定名 APCOMPARE が該当します。目的経路比較で読む説明表の根拠名は経路比較根拠です。誤答D経路比較は分離レベルの選択で、主題は経路比較です。除外D経路比較では分離レベルを外す理由も経路比較誤答です。初出語経路比較として、指定名 APCOMPARE はDb2の指定または確認表であり焦点は経路比較定義です。位置付け経路比較はアクセスパス差分の比較位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前説明出力を変更審査で確認します。Db2の作業記録に再バインドを完了せずに候補を見るの根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. DYNAMICRULES</li><li>C. EXPLAIN</li><li>D. EXPLAIN(ONLY) <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答事前説明出力はDです。論点事前説明出力における指定名 EXPLAIN(ONLY) の確認軸名は事前説明出力確認です。変更影響を本番反映前に評価しますので、目的名は事前説明出力目的です。事前説明出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前説明出力説明です。誤答A事前説明出力は成果物の所有者の選択で、主題は事前説明出力です。除外A事前説明出力では成果物の所有者を外す理由も事前説明出力誤答です。誤答B事前説明出力は動的SQLの権限文脈の選択で、主題は事前説明出力です。除外B事前説明出力では動的SQLの権限文脈を外す理由も事前説明出力誤答です。誤答C事前説明出力はアクセスパス情報の出力の選択で、主題は事前説明出力です。除外C事前説明出力ではアクセスパス情報の出力を外す理由も事前説明出力誤答です。Dが正解です。論点事前説明出力の指定名 EXPLAIN(ONLY) が該当します。目的事前説明出力で読む説明表の根拠名は事前説明出力根拠です。初出語事前説明出力として、指定名 EXPLAIN(ONLY) はDb2の指定または確認表であり焦点は事前説明出力定義です。位置付け事前説明出力は再バインドを完了せずに候補を見る位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 前回版切替を変更審査で確認します。Db2の作業記録に前回コピーへの切り替えの根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS) <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. REOPT</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答前回版切替はAです。論点前回版切替における指定名 SWITCH(PREVIOUS) の確認軸名は前回版切替確認です。性能劣化時の即時切り戻しを支えますので、目的名は前回版切替目的です。前回版切替で読むパッケージコピー表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は前回版切替説明です。Aが正解です。論点前回版切替の指定名 SWITCH(PREVIOUS) が該当します。目的前回版切替で読むパッケージコピー表の根拠名は前回版切替根拠です。誤答B前回版切替は分離レベルの選択で、主題は前回版切替です。除外B前回版切替では分離レベルを外す理由も前回版切替誤答です。誤答C前回版切替は実行時値による再最適化の選択で、主題は前回版切替です。除外C前回版切替では実行時値による再最適化を外す理由も前回版切替誤答です。誤答D前回版切替は動的SQL文の集約の選択で、主題は前回版切替です。除外D前回版切替では動的SQL文の集約を外す理由も前回版切替誤答です。初出語前回版切替として、指定名 SWITCH(PREVIOUS) はDb2の指定または確認表であり焦点は前回版切替定義です。位置付け前回版切替は前回コピーへの切り替え位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 最適化ヒントを性能調査で確認します。Db2の作業記録に最適化ヒントの利用の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. OPTHINT <span class="kb-ok">✅ 正解</span></li><li>C. OWNER</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答最適化ヒントはBです。論点最適化ヒントにおける指定名 OPTHINT の確認軸名は最適化ヒント確認です。ヒントが現行エスキューエルと一致するか確認しますので、目的名は最適化ヒント目的です。最適化ヒントで読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は最適化ヒント説明です。誤答A最適化ヒントは動的SQLの権限文脈の選択で、主題は最適化ヒントです。除外A最適化ヒントでは動的SQLの権限文脈を外す理由も最適化ヒント誤答です。Bが正解です。論点最適化ヒントの指定名 OPTHINT が該当します。目的最適化ヒントで読む説明表の根拠名は最適化ヒント根拠です。誤答C最適化ヒントは成果物の所有者の選択で、主題は最適化ヒントです。除外C最適化ヒントでは成果物の所有者を外す理由も最適化ヒント誤答です。誤答D最適化ヒントは動的SQL文の集約の選択で、主題は最適化ヒントです。除外D最適化ヒントでは動的SQL文の集約を外す理由も最適化ヒント誤答です。初出語最適化ヒントとして、指定名 OPTHINT はDb2の指定または確認表であり焦点は最適化ヒント定義です。位置付け最適化ヒントは最適化ヒントの利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 加速器利用を性能調査で確認します。Db2の作業記録にアクセラレーター利用の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. DEGREE</li><li>C. QUERYACCELERATION <span class="kb-ok">✅ 正解</span></li><li>D. ACTION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答加速器利用はCです。論点加速器利用における指定名 QUERYACCELERATION の確認軸名は加速器利用確認です。加速対象外の戻り動作も確認しますので、目的名は加速器利用目的です。加速器利用で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は加速器利用説明です。誤答A加速器利用はパッケージコピーの保持の選択で、主題は加速器利用です。除外A加速器利用ではパッケージコピーの保持を外す理由も加速器利用誤答です。誤答B加速器利用は並列実行の許可の選択で、主題は加速器利用です。除外B加速器利用では並列実行の許可を外す理由も加速器利用誤答です。Cが正解です。論点加速器利用の指定名 QUERYACCELERATION が該当します。目的加速器利用で読むパッケージカタログの根拠名は加速器利用根拠です。誤答D加速器利用は追加と置換の扱いの選択で、主題は加速器利用です。除外D加速器利用では追加と置換の扱いを外す理由も加速器利用誤答です。初出語加速器利用として、指定名 QUERYACCELERATION はDb2の指定または確認表であり焦点は加速器利用定義です。位置付け加速器利用はアクセラレーター利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 文集約を性能調査で確認します。Db2の作業記録に動的エスキューエル文の集約の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. CONCENTRATESTMT <span class="kb-ok">✅ 正解</span></li><li>B. QUERYACCELERATION</li><li>C. QUERYACCELERATION</li><li>D. KEEPDYNAMIC</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答文集約はAです。論点文集約における指定名 CONCENTRATESTMT の確認軸名は文集約確認です。動的ステートメントキャッシュの効率を確認しますので、目的名は文集約目的です。文集約で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は文集約説明です。Aが正解です。論点文集約の指定名 CONCENTRATESTMT が該当します。目的文集約で読むパッケージカタログの根拠名は文集約根拠です。誤答B文集約はアクセラレーター利用方針の選択で、主題は文集約です。除外B文集約ではアクセラレーター利用方針を外す理由も文集約誤答です。誤答C文集約はアクセラレーター利用方針の選択で、主題は文集約です。除外C文集約ではアクセラレーター利用方針を外す理由も文集約誤答です。誤答D文集約は準備済み動的SQL文の保持の選択で、主題は文集約です。除外D文集約では準備済み動的SQL文の保持を外す理由も文集約誤答です。初出語文集約として、指定名 CONCENTRATESTMT はDb2の指定または確認表であり焦点は文集約定義です。位置付け文集約は動的エスキューエル文の集約位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路再利用を性能調査で確認します。Db2の作業記録に前回アクセスパスの再利用の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. SWITCH(PREVIOUS)</li><li>B. QUALIFIER</li><li>C. APREUSE <span class="kb-ok">✅ 正解</span></li><li>D. ISOLATION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路再利用はCです。論点経路再利用における指定名 APREUSE の確認軸名は経路再利用確認です。再利用できないエスキューエルを説明表で確認しますので、目的名は経路再利用目的です。経路再利用で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路再利用説明です。誤答A経路再利用は前回コピーへの切り替えの選択で、主題は経路再利用です。除外A経路再利用では前回コピーへの切り替えを外す理由も経路再利用誤答です。誤答B経路再利用は未修飾表名のスキーマの選択で、主題は経路再利用です。除外B経路再利用では未修飾表名のスキーマを外す理由も経路再利用誤答です。Cが正解です。論点経路再利用の指定名 APREUSE が該当します。目的経路再利用で読む説明表の根拠名は経路再利用根拠です。誤答D経路再利用は分離レベルの選択で、主題は経路再利用です。除外D経路再利用では分離レベルを外す理由も経路再利用誤答です。初出語経路再利用として、指定名 APREUSE はDb2の指定または確認表であり焦点は経路再利用定義です。位置付け経路再利用は前回アクセスパスの再利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路比較を性能調査で確認します。Db2の作業記録にアクセスパス差分の比較の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. DYNAMICRULES</li><li>C. EXPLAIN</li><li>D. APCOMPARE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路比較はDです。論点経路比較における指定名 APCOMPARE の確認軸名は経路比較確認です。経路比較メッセージと説明表の結果を照合しますので、目的名は経路比較目的です。経路比較で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路比較説明です。誤答A経路比較は成果物の所有者の選択で、主題は経路比較です。除外A経路比較では成果物の所有者を外す理由も経路比較誤答です。誤答B経路比較は動的SQLの権限文脈の選択で、主題は経路比較です。除外B経路比較では動的SQLの権限文脈を外す理由も経路比較誤答です。誤答C経路比較はアクセスパス情報の出力の選択で、主題は経路比較です。除外C経路比較ではアクセスパス情報の出力を外す理由も経路比較誤答です。Dが正解です。論点経路比較の指定名 APCOMPARE が該当します。目的経路比較で読む説明表の根拠名は経路比較根拠です。初出語経路比較として、指定名 APCOMPARE はDb2の指定または確認表であり焦点は経路比較定義です。位置付け経路比較はアクセスパス差分の比較位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前説明出力を性能調査で確認します。Db2の作業記録に再バインドを完了せずに候補を見るの根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. EXPLAIN(ONLY) <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. REOPT</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答事前説明出力はAです。論点事前説明出力における指定名 EXPLAIN(ONLY) の確認軸名は事前説明出力確認です。変更影響を本番反映前に評価しますので、目的名は事前説明出力目的です。事前説明出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前説明出力説明です。Aが正解です。論点事前説明出力の指定名 EXPLAIN(ONLY) が該当します。目的事前説明出力で読む説明表の根拠名は事前説明出力根拠です。誤答B事前説明出力は分離レベルの選択で、主題は事前説明出力です。除外B事前説明出力では分離レベルを外す理由も事前説明出力誤答です。誤答C事前説明出力は実行時値による再最適化の選択で、主題は事前説明出力です。除外C事前説明出力では実行時値による再最適化を外す理由も事前説明出力誤答です。誤答D事前説明出力は動的SQL文の集約の選択で、主題は事前説明出力です。除外D事前説明出力では動的SQL文の集約を外す理由も事前説明出力誤答です。初出語事前説明出力として、指定名 EXPLAIN(ONLY) はDb2の指定または確認表であり焦点は事前説明出力定義です。位置付け事前説明出力は再バインドを完了せずに候補を見る位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 前回版切替を性能調査で確認します。Db2の作業記録に前回コピーへの切り替えの根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. SWITCH(PREVIOUS) <span class="kb-ok">✅ 正解</span></li><li>C. PATH</li><li>D. OWNER</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答前回版切替はBです。論点前回版切替における指定名 SWITCH(PREVIOUS) の確認軸名は前回版切替確認です。性能劣化時の即時切り戻しを支えますので、目的名は前回版切替目的です。前回版切替で読むパッケージコピー表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は前回版切替説明です。誤答A前回版切替は動的SQLの権限文脈の選択で、主題は前回版切替です。除外A前回版切替では動的SQLの権限文脈を外す理由も前回版切替誤答です。Bが正解です。論点前回版切替の指定名 SWITCH(PREVIOUS) が該当します。目的前回版切替で読むパッケージコピー表の根拠名は前回版切替根拠です。誤答C前回版切替はルーチン探索順序の選択で、主題は前回版切替です。除外C前回版切替ではルーチン探索順序を外す理由も前回版切替誤答です。誤答D前回版切替は成果物の所有者の選択で、主題は前回版切替です。除外D前回版切替では成果物の所有者を外す理由も前回版切替誤答です。初出語前回版切替として、指定名 SWITCH(PREVIOUS) はDb2の指定または確認表であり焦点は前回版切替定義です。位置付け前回版切替は前回コピーへの切り替え位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 最適化ヒントを障害復旧で確認します。Db2の作業記録に最適化ヒントの利用の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. DEGREE</li><li>C. OPTHINT <span class="kb-ok">✅ 正解</span></li><li>D. ACTION</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答最適化ヒントはCです。論点最適化ヒントにおける指定名 OPTHINT の確認軸名は最適化ヒント確認です。ヒントが現行エスキューエルと一致するか確認しますので、目的名は最適化ヒント目的です。最適化ヒントで読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は最適化ヒント説明です。誤答A最適化ヒントはパッケージコピーの保持の選択で、主題は最適化ヒントです。除外A最適化ヒントではパッケージコピーの保持を外す理由も最適化ヒント誤答です。誤答B最適化ヒントは並列実行の許可の選択で、主題は最適化ヒントです。除外B最適化ヒントでは並列実行の許可を外す理由も最適化ヒント誤答です。Cが正解です。論点最適化ヒントの指定名 OPTHINT が該当します。目的最適化ヒントで読む説明表の根拠名は最適化ヒント根拠です。誤答D最適化ヒントは追加と置換の扱いの選択で、主題は最適化ヒントです。除外D最適化ヒントでは追加と置換の扱いを外す理由も最適化ヒント誤答です。初出語最適化ヒントとして、指定名 OPTHINT はDb2の指定または確認表であり焦点は最適化ヒント定義です。位置付け最適化ヒントは最適化ヒントの利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 加速器利用を障害復旧で確認します。Db2の作業記録にアクセラレーター利用の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. CURRENTDATA</li><li>B. EXPLAIN</li><li>C. DYNAMICRULES</li><li>D. QUERYACCELERATION <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答加速器利用はDです。論点加速器利用における指定名 QUERYACCELERATION の確認軸名は加速器利用確認です。加速対象外の戻り動作も確認しますので、目的名は加速器利用目的です。加速器利用で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は加速器利用説明です。誤答A加速器利用はカーソル読み取りの現在性の選択で、主題は加速器利用です。除外A加速器利用ではカーソル読み取りの現在性を外す理由も加速器利用誤答です。誤答B加速器利用はアクセスパス情報の出力の選択で、主題は加速器利用です。除外B加速器利用ではアクセスパス情報の出力を外す理由も加速器利用誤答です。誤答C加速器利用は動的SQLの権限文脈の選択で、主題は加速器利用です。除外C加速器利用では動的SQLの権限文脈を外す理由も加速器利用誤答です。Dが正解です。論点加速器利用の指定名 QUERYACCELERATION が該当します。目的加速器利用で読むパッケージカタログの根拠名は加速器利用根拠です。初出語加速器利用として、指定名 QUERYACCELERATION はDb2の指定または確認表であり焦点は加速器利用定義です。位置付け加速器利用はアクセラレーター利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 文集約を障害復旧で確認します。Db2の作業記録に動的エスキューエル文の集約の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. APREUSE</li><li>B. CONCENTRATESTMT <span class="kb-ok">✅ 正解</span></li><li>C. EXPLAIN(ONLY)</li><li>D. EXPLAIN(ONLY)</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答文集約はBです。論点文集約における指定名 CONCENTRATESTMT の確認軸名は文集約確認です。動的ステートメントキャッシュの効率を確認しますので、目的名は文集約目的です。文集約で読むパッケージカタログの列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は文集約説明です。誤答A文集約は前回アクセスパスの再利用の選択で、主題は文集約です。除外A文集約では前回アクセスパスの再利用を外す理由も文集約誤答です。Bが正解です。論点文集約の指定名 CONCENTRATESTMT が該当します。目的文集約で読むパッケージカタログの根拠名は文集約根拠です。誤答C文集約は候補アクセスパスの事前出力の選択で、主題は文集約です。除外C文集約では候補アクセスパスの事前出力を外す理由も文集約誤答です。誤答D文集約は候補アクセスパスの事前出力の選択で、主題は文集約です。除外D文集約では候補アクセスパスの事前出力を外す理由も文集約誤答です。初出語文集約として、指定名 CONCENTRATESTMT はDb2の指定または確認表であり焦点は文集約定義です。位置付け文集約は動的エスキューエル文の集約位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路再利用を障害復旧で確認します。Db2の作業記録に前回アクセスパスの再利用の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. OWNER</li><li>B. DYNAMICRULES</li><li>C. EXPLAIN</li><li>D. APREUSE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路再利用はDです。論点経路再利用における指定名 APREUSE の確認軸名は経路再利用確認です。再利用できないエスキューエルを説明表で確認しますので、目的名は経路再利用目的です。経路再利用で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路再利用説明です。誤答A経路再利用は成果物の所有者の選択で、主題は経路再利用です。除外A経路再利用では成果物の所有者を外す理由も経路再利用誤答です。誤答B経路再利用は動的SQLの権限文脈の選択で、主題は経路再利用です。除外B経路再利用では動的SQLの権限文脈を外す理由も経路再利用誤答です。誤答C経路再利用はアクセスパス情報の出力の選択で、主題は経路再利用です。除外C経路再利用ではアクセスパス情報の出力を外す理由も経路再利用誤答です。Dが正解です。論点経路再利用の指定名 APREUSE が該当します。目的経路再利用で読む説明表の根拠名は経路再利用根拠です。初出語経路再利用として、指定名 APREUSE はDb2の指定または確認表であり焦点は経路再利用定義です。位置付け経路再利用は前回アクセスパスの再利用位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 経路比較を障害復旧で確認します。Db2の作業記録にアクセスパス差分の比較の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. APCOMPARE <span class="kb-ok">✅ 正解</span></li><li>B. ISOLATION</li><li>C. REOPT</li><li>D. CONCENTRATESTMT</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答経路比較はAです。論点経路比較における指定名 APCOMPARE の確認軸名は経路比較確認です。経路比較メッセージと説明表の結果を照合しますので、目的名は経路比較目的です。経路比較で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は経路比較説明です。Aが正解です。論点経路比較の指定名 APCOMPARE が該当します。目的経路比較で読む説明表の根拠名は経路比較根拠です。誤答B経路比較は分離レベルの選択で、主題は経路比較です。除外B経路比較では分離レベルを外す理由も経路比較誤答です。誤答C経路比較は実行時値による再最適化の選択で、主題は経路比較です。除外C経路比較では実行時値による再最適化を外す理由も経路比較誤答です。誤答D経路比較は動的SQL文の集約の選択で、主題は経路比較です。除外D経路比較では動的SQL文の集約を外す理由も経路比較誤答です。初出語経路比較として、指定名 APCOMPARE はDb2の指定または確認表であり焦点は経路比較定義です。位置付け経路比較はアクセスパス差分の比較位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 事前説明出力を障害復旧で確認します。Db2の作業記録に再バインドを完了せずに候補を見るの根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. DYNAMICRULES</li><li>B. EXPLAIN(ONLY) <span class="kb-ok">✅ 正解</span></li><li>C. PATH</li><li>D. OWNER</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答事前説明出力はBです。論点事前説明出力における指定名 EXPLAIN(ONLY) の確認軸名は事前説明出力確認です。変更影響を本番反映前に評価しますので、目的名は事前説明出力目的です。事前説明出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は事前説明出力説明です。誤答A事前説明出力は動的SQLの権限文脈の選択で、主題は事前説明出力です。除外A事前説明出力では動的SQLの権限文脈を外す理由も事前説明出力誤答です。Bが正解です。論点事前説明出力の指定名 EXPLAIN(ONLY) が該当します。目的事前説明出力で読む説明表の根拠名は事前説明出力根拠です。誤答C事前説明出力はルーチン探索順序の選択で、主題は事前説明出力です。除外C事前説明出力ではルーチン探索順序を外す理由も事前説明出力誤答です。誤答D事前説明出力は成果物の所有者の選択で、主題は事前説明出力です。除外D事前説明出力では成果物の所有者を外す理由も事前説明出力誤答です。初出語事前説明出力として、指定名 EXPLAIN(ONLY) はDb2の指定または確認表であり焦点は事前説明出力定義です。位置付け事前説明出力は再バインドを完了せずに候補を見る位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 前回版切替を障害復旧で確認します。Db2の作業記録に前回コピーへの切り替えの根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。</p><ul class="kb-choices"><li>A. PLANMGMT</li><li>B. EXPLAIN(ONLY)</li><li>C. SWITCH(PREVIOUS) <span class="kb-ok">✅ 正解</span></li><li>D. SQLERROR</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答前回版切替はCです。論点前回版切替における指定名 SWITCH(PREVIOUS) の確認軸名は前回版切替確認です。性能劣化時の即時切り戻しを支えますので、目的名は前回版切替目的です。前回版切替で読むパッケージコピー表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は前回版切替説明です。誤答A前回版切替はパッケージコピーの保持の選択で、主題は前回版切替です。除外A前回版切替ではパッケージコピーの保持を外す理由も前回版切替誤答です。誤答B前回版切替は候補アクセスパスの事前出力の選択で、主題は前回版切替です。除外B前回版切替では候補アクセスパスの事前出力を外す理由も前回版切替誤答です。Cが正解です。論点前回版切替の指定名 SWITCH(PREVIOUS) が該当します。目的前回版切替で読むパッケージコピー表の根拠名は前回版切替根拠です。誤答D前回版切替はSQLエラー時の成果物作成の選択で、主題は前回版切替です。除外D前回版切替ではSQLエラー時の成果物作成を外す理由も前回版切替誤答です。初出語前回版切替として、指定名 SWITCH(PREVIOUS) はDb2の指定または確認表であり焦点は前回版切替定義です。位置付け前回版切替は前回コピーへの切り替え位置です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-q"><p><strong>問題.</strong> 複数のCOPYジョブで共通のTEMPLATE定義を別DDから読ませ、ジョブごとのSYSINを短く保ちたい状況です。指定している内容はどれですか。</p><ul class="kb-choices"><li>A. 雛形DD指定 <span class="kb-ok">✅ 正解</span></li><li>B. 出力DD雛形</li><li>C. 対象集合定義</li><li>D. 統計表示レポート</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 外部DDからTEMPLATE定義を読ませるため、Aを選びます。この指定はOPTIONS文で示し、後続の制御文が使うTEMPLATEライブラリを切り替えます。Bは雛形DD指定と別の TEMPLATE本体の定義、Cは雛形DD指定と別の LISTDEFの対象集合、Dは雛形DD指定と別の RUNSTATSのREPORTです。共通化した割当規則を使う点が要点です；背景には共通TEMPLATEを外部DDで管理する設計では、Db2 のユーティリティ制御文オプションとして OPTIONS TEMPLATEDD を使います、以後のユーティリティ制御文が参照するTEMPLATEライブラリのDD名を示します、ジョブ内に同じ雛形を何度も書かず、標準化した割当規則を適用できますという関係があり、この区別で確認する名称は「TEMPLATEDD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> コピー出力の割当雛形を使い、表スペース名や時刻からデータセット名を作りたい状況です。中心になる制御文はどれですか。</p><ul class="kb-choices"><li>A. 除外条件</li><li>B. DD割当雛形 <span class="kb-ok">✅ 正解</span></li><li>C. ログ停止点</li><li>D. 制約検査</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> データセット割当の雛形を作るため、Bが正解です。DD割当雛形の説明として、TEMPLATEは名前規則や割当属性をまとめ、COPYDDNなどから参照されます。AはDD割当雛形と別の EXCLUDEによる対象除外、CはDD割当雛形と別の TOLOGPOINTなどの回復位置、DはDD割当雛形と別の LOADのENFORCEです。DD割当雛形の説明として、DD文を増やさず標準名を使えることが利点です；背景には動的割当を使うユーティリティでは、TEMPLATE が Db2 のDSNUTILBオプションとして出力データセットの命名規則や割当属性を定義します、DD割当雛形の説明として、DSN、UNIT、SPACE、DISP などを含めて、JCL DD文を個別に書かずに済ませます、DD割当雛形の説明として、LISTDEFと組み合わせると、多数オブジェクトのコピー名を標準化できますという関係があり、この区別で確認する名称は「TEMPLATE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 複数の表スペースを同じ基準でまとめ、COPYやRUNSTATSから同じ集合を参照したい状況です。定義すべきものはどれですか。</p><ul class="kb-choices"><li>A. 容量割当</li><li>B. ロード方式</li><li>C. 対象リスト <span class="kb-ok">✅ 正解</span></li><li>D. 災対DD名</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 再利用できる対象集合を作るため、Cが合います。対象リストの説明として、LISTDEFでリスト名を定義し、後続ユーティリティはそのリストを参照できます。Aは対象リストと別の TEMPLATEのSPACE、Bは対象リストと別の LOADのRESUMEやREPLACE、Dは対象リストと別の RECOVERYDDNです。対象の選び方を一箇所で管理できます；背景には多数の表スペースをまとめて処理する場合、LISTDEF は Db2 のユーティリティ制御文オプションとして再利用できる対象リストを定義します、対象リストの説明として、INCLUDEで対象を加え、必要に応じてEXCLUDEで外します、対象リストの説明として、COPY、RUNSTATS、REORGなどで同じ対象集合を使う運用に向きますという関係があり、この区別で確認する名称は「LISTDEF」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 対象追加の確認として、LISTDEFで PAYDB 配下の表スペースを処理対象に加え、その後COPY LISTからまとめて参照したい状況です。この句の働きはどれですか。</p><ul class="kb-choices"><li>A. コピーDD選択</li><li>B. 統計保存</li><li>C. RBA指定</li><li>D. 対象追加 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 対象をリストへ加える句なので、Dが正解です。対象追加の説明として、INCLUDEはLISTDEFの基礎になる集合を作り、条件に合うオブジェクトを処理対象にします。Aは対象追加と別の COPYDDN、Bは対象追加と別の RUNSTATS UPDATE、Cは対象追加と別の TORBAです。対象集合を作る最初の入口として使います；背景には対象追加の説明として、LISTDEFの対象を増やす場面で、INCLUDE は Db2 のDSNUTILBオプションとして条件に合うオブジェクトをリストへ追加します、最初のLISTDEFでは、少なくとも一つのINCLUDE句が必要です、データベース、表スペース、索引などを条件で選び、後続処理へ渡しますという関係があり、この区別で確認する名称は「INCLUDE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 対象除外の確認として、LISTDEFでデータベース全体を集めた後、保守対象外の一部表スペースのみを外したい状況です。使う役割はどれですか。</p><ul class="kb-choices"><li>A. 対象除外 <span class="kb-ok">✅ 正解</span></li><li>B. 対象追加</li><li>C. 容量指定</li><li>D. 頻度統計</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> リストから対象を取り除くため、Aを選びます。対象除外の説明として、EXCLUDEはINCLUDEで作った集合から例外を含めないときに使います。Bは対象除外と別の INCLUDEの役割、Cは対象除外と別の TEMPLATEのSPACE、Dは対象除外と別の RUNSTATSのFREQVALです。大きく集めてから例外を削る運用で有効です；背景には対象除外の説明として、LISTDEFから一部を含めない作業では、EXCLUDE が Db2 のユーティリティ制御文オプションとして既存リストから条件一致オブジェクトを除きます、対象除外の説明として、INCLUDEで大きく集めてから、保守対象外や例外資源を引くときに使います、処理対象の過不足を防ぐため、除外条件は実行前にPREVIEWで確認しますという関係があり、この区別で確認する名称は「EXCLUDE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> コピー出力の名前規則として、データベース名、表スペース名、実行時刻を組み合わせたい状況です。TEMPLATE内で決める内容はどれですか。</p><ul class="kb-choices"><li>A. 装置種別</li><li>B. DS名規則 <span class="kb-ok">✅ 正解</span></li><li>C. 更新可否</li><li>D. 戻し先時点</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> データセット名の作り方を示すため、Bが該当します。DS名規則の説明として、DSNはTEMPLATEの中で名前文字列と置換変数を指定します。AはDS名規則と別の UNIT、CはDS名規則と別の RUNSTATS UPDATE、DはDS名規則と別の RECOVERの時点指定です。命名規則が崩れると出力の識別が難しくなります；背景にはDS名規則の説明として、TEMPLATEでデータセット名を標準化するとき、DSN は Db2 のDSNUTILBオプションとして命名規則を指定します、データベース名、表スペース名、時刻などの置換変数を使って出力名を組み立てます、再実行時に同じ名前を使うか、新しい世代を作るかの管理にも関係しますという関係があり、この区別で確認する名称は「DSN」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 装置種別の確認として、TEMPLATEで作るコピー用データセットをSYSDA相当の装置へ割り当てるよう、制御文で示したい状況です。どれを指定していますか。</p><ul class="kb-choices"><li>A. DD名対応</li><li>B. 統計表示</li><li>C. 装置種別 <span class="kb-ok">✅ 正解</span></li><li>D. 破棄件数</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 出力先の装置種別を示すため、Cを選びます。装置種別の説明として、UNITは動的割当で使うユニット名や装置クラスに関係します。Aは装置種別と別の COPYDDNやRECOVERYDDN、Bは装置種別と別の REPORT、Dは装置種別と別の DISCARDSです。ストレージ管理方式に合わせて使う値を確認します；背景には動的にデータセットを割り当てる場合、UNIT は Db2 のユーティリティ制御文オプションとして装置種別やユニット名を指定します、装置種別の説明として、TEMPLATE内で使うと、出力先の装置クラスをJCL DD文なしでそろえられます、装置種別の説明として、SMS環境ではSTORCLASなどとの役割分担も確認しますという関係があり、この区別で確認する名称は「UNIT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 容量指定の確認として、TEMPLATEで作るイメージコピー用データセットについて、一次量や二次量の割当方針を制御したい状況です。対象はどれですか。</p><ul class="kb-choices"><li>A. 権限取消</li><li>B. 対象除外</li><li>C. 履歴表示</li><li>D. 容量指定 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> データセット容量の割当を扱うため、Dが正しいです。容量指定の説明として、SPACEはTEMPLATEで作る出力データセットの大きさを決める指定です。Aは権限操作、Bは容量指定と別の LISTDEFのEXCLUDE、Cは容量指定と別の REPORTの表示とは異なります。大きなコピー出力では不足が起きない値を選びます；背景にはコピーやアンロード出力の容量を制御するため、SPACE は Db2 のDSNUTILBオプションとしてTEMPLATE内の割当量を指定します、シリンダやトラックなどの単位、一次量、二次量を決める材料になります、指定しない場合はDb2が見積もることもあります、一方で、標準化したい出力では明示しますという関係があり、この区別で確認する名称は「SPACE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ユーティリティが作成する出力データセットについて、正常終了時に保存するか削除するかをTEMPLATEで決めたい状況です。扱う内容はどれですか。</p><ul class="kb-choices"><li>A. 後処理属性 <span class="kb-ok">✅ 正解</span></li><li>B. 装置割当</li><li>C. 統計列数</li><li>D. ログ停止点</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 作成後の扱いを決めるため、Aが該当します。後処理属性の説明として、DISPは動的に割り当てたデータセットを保存、削除、再利用する規則に関係します。Bは後処理属性と別の UNIT、Cは後処理属性と別の RUNSTATSの列数指定、Dは後処理属性と別の TOLOGPOINTです。再実行時に古い出力とぶつからないよう確認します；背景には動的割当データセットの扱いを決めるとき、DISP は Db2 のユーティリティ制御文オプションとして作成後の状態や異常終了時の扱いを示します、後処理属性の説明として、TEMPLATE内で使うことで、出力データセットの保存や削除の規則を統一できます、再実行時の既存データセットとの衝突にも注意しますという関係があり、この区別で確認する名称は「DISP」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 並行可否の確認として、COPYやLOADの実行中に、アプリケーションの参照や変更をどこまで許すかを制御したい状況です。確認する指定はどれですか。</p><ul class="kb-choices"><li>A. コピーDD</li><li>B. 並行可否 <span class="kb-ok">✅ 正解</span></li><li>C. 区画上限</li><li>D. 頻度値</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 実行中の共有レベルを決めるため、Bを選択します。並行可否の説明として、SHRLEVELはユーティリティとアプリケーション処理の並行性に関係します。Aは並行可否と別の COPYDDN、Cは表スペースの上限設定、Dは並行可否と別の RUNSTATSのFREQVALです。停止時間を短くしたい場合ほど重要になります；背景にはユーティリティ中のアクセス可否を決める場合、SHRLEVEL は Db2 のDSNUTILBオプションとして対象オブジェクトをどの程度共有できるかを指定します、並行可否の説明として、REFERENCE、CHANGE、NONE などにより、読取りや更新との並行性が変わります、業務停止時間と整合性要件を見て選びますという関係があり、この区別で確認する名称は「SHRLEVEL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 既存の明細表を空にせず、新しいレコードのみをLOADで追加したい状況です。確認すべき指定の意味はどれですか。</p><ul class="kb-choices"><li>A. 追加入力 <span class="kb-ok">✅ 正解</span></li><li>B. 入替ロード</li><li>C. 統計更新</li><li>D. 対象除外</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 既存行を残して追加するため、Aを選びます。追加入力の説明として、RESUMEはLOAD時に追記するかどうかを決める指定です。Bは追加入力と別の REPLACEの動作、Cは追加入力と別の RUNSTATS UPDATE、Dは追加入力と別の LISTDEFのEXCLUDEです。誤って入替ロードにしないよう本番前に確認します；背景には既存表にデータを追加ロードする場合、RESUME は Db2 のユーティリティ制御文オプションとしてLOAD対象を空にせず追加入力するかを示します、追加入力の説明として、YESなら既存データを残して追加し、NOやREPLACEとは動作が異なります、再ロードか追記かを誤ると業務データに大きく影響しますという関係があり、この区別で確認する名称は「RESUME」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> テスト表を全件作り直すため、既存行を残さずLOAD入力で置き換えたい状況です。この動作を示すものはどれですか。</p><ul class="kb-choices"><li>A. 追記ロード</li><li>B. 入替ロード <span class="kb-ok">✅ 正解</span></li><li>C. コピーDD</li><li>D. ヒストグラム</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 既存内容を置き換えるため、Bが正解です。入替ロードの説明として、REPLACEは追記ではなく入替を行うLOAD動作です。Aは入替ロードと別の RESUMEの考え方、Cは入替ロードと別の COPYDDN、Dは入替ロードと別の RUNSTATS HISTOGRAMです。実行前に対象表とバックアップの有無を確認します；背景には表の内容を入れ替えるLOADでは、REPLACE が Db2 のDSNUTILBオプションとして既存データを置き換える動作を示します、入替ロードの説明として、RESUMEによる追記とは違い、対象を再作成するような扱いになります、テスト再投入や全件再ロードでは便利です、一方で、誤指定すると既存データ喪失につながりますという関係があり、この区別で確認する名称は「REPLACE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ログ記録の確認として、LOADの性能を上げたい一方で、障害時の回復方法が変わるため、ログをどこまで残すかを判断しています。対象になる指定はどれですか。</p><ul class="kb-choices"><li>A. 容量割当</li><li>B. 統計表示</li><li>C. ログ記録 <span class="kb-ok">✅ 正解</span></li><li>D. DD雛形</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ロード処理のログ扱いを決めるため、Cが該当します。ログ記録の説明として、LOGは回復性と性能のバランスに関係します。Aはログ記録と別の SPACE、Bはログ記録と別の REPORT、Dはログ記録と別の TEMPLATEです。ログ記録の説明として、LOGを抑えた運用では障害後の復旧手順を先に決めておきます；背景にはログ記録の説明として、LOADのログ量を制御する作業で、LOG は Db2 のユーティリティ制御文オプションとして入力データのロード処理をどの程度ログ記録するかに関係します、ログ記録の説明として、LOG YESなら回復性を優先し、NOは性能やログ量を抑える代わりに復旧手順を厳しくします、中断時の対応にも影響しますという関係があり、この区別で確認する名称は「LOG」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 大量LOADで制約検査の扱いを明示し、投入速度とデータ整合性のバランスを決めたい状況です。どれを確認しますか。</p><ul class="kb-choices"><li>A. 装置指定</li><li>B. 頻度統計</li><li>C. 対象リスト</li><li>D. 制約検査 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 制約を検査するかに関わるため、Dが正しいです。制約検査の説明として、ENFORCEはLOAD中の整合性確認の扱いを示します。Aは制約検査と別の UNIT、Bは制約検査と別の FREQVAL、Cは制約検査と別の LISTDEFです。検査を行わない場合は後でCHECK DATAなどの確認を計画します；背景には制約検査の説明として、LOAD時の制約扱いを決める場合、ENFORCE は Db2 のDSNUTILBオプションとして参照整合性やチェック制約などの検査を行うかを示します、検査を弱めると投入は進みやすくなります、一方で、後続の整合性確認が必要になります、データ品質と投入時間のどちらを優先するかで選びますという関係があり、この区別で確認する名称は「ENFORCE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 破棄上限の確認として、LOADで形式不正の入力行を一定件数まで許し、上限を超えたら処理を止めたい状況です。指定しているものはどれですか。</p><ul class="kb-choices"><li>A. 破棄上限 <span class="kb-ok">✅ 正解</span></li><li>B. ログ停止点</li><li>C. DD名規則</li><li>D. 索引配置</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 破棄できる件数の上限を扱うため、Aが合います。破棄上限の説明として、DISCARDSはLOAD中の不正入力をどこまで許すかを決めます。Bは破棄上限と別の TOLOGPOINT、Cは破棄上限と別の TEMPLATEのDSN、Dは索引設計です。破棄された行の証跡も合わせて確認します；背景には破棄上限の説明として、LOADで不正レコードが出たときの許容範囲を決めるため、DISCARDS は Db2 のユーティリティ制御文オプションとして破棄できる件数の上限を指定します、上限を超えると処理を止める判断に使われます、入力データ品質を監視するため、破棄DDやエラー確認と合わせますという関係があり、この区別で確認する名称は「DISCARDS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ソートキー数の確認として、LOB列を含む表のLOADで、再始動条件に影響するキーソートの扱いを明示したい状況です。対象となる指定はどれですか。</p><ul class="kb-choices"><li>A. コピーDD</li><li>B. ソートキー数 <span class="kb-ok">✅ 正解</span></li><li>C. 制約検査</li><li>D. 統計表示</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> キーソートの扱いに関係するため、Bを選びます。ソートキー数の説明として、SORTKEYSはLOAD処理のソート見積りや再始動条件で注意が必要な指定です。Aはソートキー数と別の COPYDDN、Cはソートキー数と別の ENFORCE、Dはソートキー数と別の REPORTです。ソートキー数の説明として、LOBを持つ表では中断時の手順も確認します；背景にはソートキー数の説明として、LOADのソート処理や再始動性を見るとき、SORTKEYS は Db2 のDSNUTILBオプションとしてキーソートの見積りや扱いに関係します、値の指定によりLOADの処理計画や中断後の再始動条件が変わる場合があります、ソートキー数の説明として、LOB列を含む表では、再始動可否の注意点として確認しますという関係があり、この区別で確認する名称は「SORTKEYS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ユーティリティ実行に合わせて表や索引の統計も集め、後続のアクセスパス選択に反映したい状況です。扱う内容はどれですか。</p><ul class="kb-choices"><li>A. 災対DD</li><li>B. 対象除外</li><li>C. 統計収集 <span class="kb-ok">✅ 正解</span></li><li>D. ログ適用</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表や索引の統計を集めるため、Cが正解です。統計収集の説明として、STATISTICSはユーティリティ実行時の統計収集に関係します。Aは統計収集と別の RECOVERYDDN、Bは統計収集と別の EXCLUDE、Dは統計収集と別の LOGONLYです。アクセスパス改善を狙うときは収集範囲と更新方法を確認します；背景にはユーティリティ中に統計を取る場合、STATISTICS は Db2 のユーティリティ制御文オプションとして対象オブジェクトの統計収集を指示します、統計収集の説明として、LOADやREORGのインライン統計、RUNSTATSの制御文で使われます、アクセスパスに効く情報を取得するため、更新先と収集範囲を確認しますという関係があり、この区別で確認する名称は「STATISTICS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> キー基数の確認として、RUNSTATSで索引キー値の種類数を集め、結合順や索引利用の判断材料にしたい状況です。指定する統計はどれですか。</p><ul class="kb-choices"><li>A. 容量指定</li><li>B. DD雛形</li><li>C. ログ停止点</li><li>D. キー基数 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> キー値の基数を集めるため、Dを選びます。キー基数の説明として、KEYCARDは索引キーのカーディナリティ情報に関係します。Aはキー基数と別の SPACE、Bはキー基数と別の TEMPLATE、Cはキー基数と別の TOLOGPOINTです。複合索引では接頭列単位の統計がアクセスパスに効きます；背景には索引キーの基数情報を集めるとき、KEYCARD は Db2 のDSNUTILBオプションとしてRUNSTATSの統計収集範囲に関係します、キー値の種類数はオプティマイザーがアクセスパスを選ぶ材料になります、複合索引では、どの接頭列まで統計を取るかを設計しますという関係があり、この区別で確認する名称は「KEYCARD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ある列で特定コードのみが極端に多く、アクセスパスの見積りを改善したい状況です。RUNSTATSで取るべき情報はどれですか。</p><ul class="kb-choices"><li>A. 頻度値 <span class="kb-ok">✅ 正解</span></li><li>B. 容量割当</li><li>C. 対象追加</li><li>D. 権限取消</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 頻出する値の統計を取るため、Aが該当します。頻度値の説明として、FREQVALは値の偏りをオプティマイザーへ伝える材料です。Bは頻度値と別の SPACE、Cは頻度値と別の INCLUDE、Dは権限操作です。偏りの強い列では通常の行数統計を主な根拠にしては不足する場合があります；背景には偏った値の分布を把握するため、FREQVAL は Db2 のユーティリティ制御文オプションとしてRUNSTATSで頻出値統計を収集します、よく出る値を記録すると、オプティマイザーが選択度をより正確に見積もれます、偏りが強い列や索引で有効ですという関係があり、この区別で確認する名称は「FREQVAL」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 日付列の範囲検索が多く、値域全体の偏りを区間ごとに把握してアクセスパス見積りを改善したい状況です。該当する統計はどれですか。</p><ul class="kb-choices"><li>A. 後処理属性</li><li>B. 分布区間 <span class="kb-ok">✅ 正解</span></li><li>C. コピーDD</li><li>D. 制約検査</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域を区間に分ける統計なので、Bを選びます。分布区間の説明として、HISTOGRAMは範囲条件の選択度を見積もるための分布情報を集めます。Aは分布区間と別の DISP、Cは分布区間と別の COPYDDN、Dは分布区間と別の ENFORCEです。日付や金額のような連続的な列で役立ちます；背景には広い値域の分布を表す場合、HISTOGRAM は Db2 のDSNUTILBオプションとしてRUNSTATSで値域を複数区間に分けた統計を収集します、分布区間の説明として、NUMQUANTILESなどで区間数を指定し、範囲条件の見積りを助けます、連続値や日付範囲の偏りを見るときに使いますという関係があり、この区別で確認する名称は「HISTOGRAM」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> カタログ更新の確認として、RUNSTATSで集めた統計をカタログへ反映し、次回BINDや動的SQLの見積りに使わせたい状況です。確認する指定はどれですか。</p><ul class="kb-choices"><li>A. 対象除外</li><li>B. RBA停止点</li><li>C. カタログ更新 <span class="kb-ok">✅ 正解</span></li><li>D. DD名規則</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 統計をカタログへ反映するかを決めるため、Cが合います。カタログ更新の説明として、UPDATEは収集結果を実際に更新するかを制御します。Aはカタログ更新と別の EXCLUDE、Bはカタログ更新と別の TORBA、Dはカタログ更新と別の TEMPLATEのDSNです。カタログ更新の説明として、REPORTのみ出して更新しない運用と区別します；背景にはカタログ更新の説明として、RUNSTATSで収集した結果の反映先を決めるため、UPDATE は Db2 のユーティリティ制御文オプションとしてカタログ統計を更新するかを示します、カタログ更新の説明として、ALLやNONEなどの指定により、収集のみにするかアクセスパスへ反映するかが変わります、検証時はREPORTと組み合わせて結果を確認しますという関係があり、この区別で確認する名称は「UPDATE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> レポート出力の確認として、RUNSTATSの結果をジョブログ上で確認し、どの統計が収集されたかを証跡に残したい状況です。対象となる指定はどれですか。</p><ul class="kb-choices"><li>A. ログ記録</li><li>B. 装置種別</li><li>C. 対象リスト</li><li>D. レポート出力 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 結果の表示を制御するため、Dが正解です。レポート出力の説明として、REPORTは統計収集の内容を出力して確認するための指定です。Aはレポート出力と別の LOADのLOG、Bはレポート出力と別の UNIT、Cはレポート出力と別の LISTDEFです。更新有無と別に、収集結果の証跡を残す目的で使います；背景には統計取得の内容を確認するため、REPORT は Db2 のDSNUTILBオプションとしてRUNSTATSなどの結果出力を制御します、レポート出力の説明として、YESにすると収集内容をレポートとして確認できます、カタログ更新を伴う場合でも、どの統計が取れたかを証跡として残す用途がありますという関係があり、この区別で確認する名称は「REPORT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 障害前の特定RBAまで表スペースを戻し、以後のログ適用を止めたい状況です。指定している回復位置はどれですか。</p><ul class="kb-choices"><li>A. RBA停止点 <span class="kb-ok">✅ 正解</span></li><li>B. ログ名規則</li><li>C. 統計区間</li><li>D. 対象追加</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> ログ上のRBAを停止点にするため、Aを選びます。RBA停止点の説明として、TORBAはRBA停止点と別の RECOVERのポイントインタイム回復で使う位置指定です。BはRBA停止点と別の TEMPLATEのDSN、CはRBA停止点と別の HISTOGRAM、DはRBA停止点と別の INCLUDEです。複数オブジェクトは同じ時点でそろえる必要があります；背景には過去時点へ戻すRECOVERでは、TORBA が Db2 のユーティリティ制御文オプションとして回復を停止するRBAを指定します、ログ上の位置を使うため、データ共有開始前後の制約や一貫性確認が必要です、関連オブジェクトを同じ時点へ戻す計画で扱いますという関係があり、この区別で確認する名称は「TORBA」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ログ停止点の確認として、RECOVERでログ上の特定時点まで適用し、その後の変更は戻したい状況です。扱う指定はどれですか。</p><ul class="kb-choices"><li>A. 破棄上限</li><li>B. ログ停止点 <span class="kb-ok">✅ 正解</span></li><li>C. DD雛形</li><li>D. 制約検査</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> ログ上の停止点を示すため、Bが該当します。ログ停止点の説明として、TOLOGPOINTはRECOVERの回復停止位置を指定します。Aはログ停止点と別の DISCARDS、Cはログ停止点と別の TEMPLATE、Dはログ停止点と別の ENFORCEです。関連する表スペースや索引を同じ時点にそろえることが重要です；背景にはログ上の特定点まで回復する作業では、TOLOGPOINT が Db2 のDSNUTILBオプションとしてRECOVERの停止位置を指定します、ログ停止点の説明として、TORBAと同様にポイントインタイム回復で使われます、データ共有環境や関連オブジェクトの同期を考慮して、回復点を選びますという関係があり、この区別で確認する名称は「TOLOGPOINT」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 複数のイメージコピーがある中で、回復の起点に使うコピーを明示してRECOVERしたい状況です。指定する内容はどれですか。</p><ul class="kb-choices"><li>A. 装置割当</li><li>B. 統計更新</li><li>C. コピー指定 <span class="kb-ok">✅ 正解</span></li><li>D. 並行可否</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 回復元コピーを明示するため、Cを選択します。コピー指定の説明として、FROMCOPYはRECOVERで使うコピーを指定する考え方です。Aはコピー指定と別の UNIT、Bはコピー指定と別の RUNSTATS UPDATE、Dはコピー指定と別の SHRLEVELです。選んだコピー以降に必要なログが残っているかを確認します；背景には使用するイメージコピーを明示するRECOVERでは、FROMCOPY が Db2 のユーティリティ制御文オプションとして回復元コピーを指定します、通常の選択に任せず、特定のコピーを基点にしたい場合に使います、コピーの利用可否と後続ログ適用の範囲を確認しますという関係があり、この区別で確認する名称は「FROMCOPY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 目的時点より後のコピーを使わず、指定時点より前に取得されたコピーを基点にしてRECOVERしたい状況です。扱う指定はどれですか。</p><ul class="kb-choices"><li>A. 頻度値</li><li>B. コピーDD</li><li>C. ログ記録</li><li>D. 前時点復元 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 指定時点より前のコピーを使う考え方なので、Dが正解です。前時点復元の説明として、RESTOREBEFOREはRECOVERで復元基点を選ぶときの判断に関係します。Aは前時点復元と別の FREQVAL、Bは前時点復元と別の COPYDDN、Cは前時点復元と別の LOADのLOGです。基点コピーとログ適用範囲が矛盾しないように確認します；背景には回復で使うコピーの時点を制御する場合、RESTOREBEFORE は Db2 のDSNUTILBオプションとして指定時点より前のコピーを復元候補にする考え方に関係します、ポイントインタイム回復では、コピー選択とログ適用の組み合わせが整合性を左右します、目的時点に対して安全な基点を選ぶために確認しますという関係があり、この区別で確認する名称は「RESTOREBEFORE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 外部手段でデータセットを戻した後、Db2のRECOVERではイメージコピー復元を行わずログ適用のみ進めたい状況です。指定の役割はどれですか。</p><ul class="kb-choices"><li>A. ログ適用のみ <span class="kb-ok">✅ 正解</span></li><li>B. 区画作成</li><li>C. 対象追加</li><li>D. 統計表示</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復元フェーズを飛ばしてログ適用を行うため、Aが該当します。ログ適用のみの説明として、LOGONLYは既にデータセットが戻されている前提で使うRECOVERの指定です。Bは表スペース設計、Cはログ適用のみと別の INCLUDE、Dはログ適用のみと別の REPORTです。外部復元の完了確認とログ範囲の確認が前提になります；背景には外部でデータセットを戻した後にログのみ適用する場合、LOGONLY は Db2 のユーティリティ制御文オプションとしてRECOVERの復元フェーズを行わない指定です、既にボリューム復元済みの環境や特定の回復手順で使われます、現在時点または過去時点までの前方回復と組み合わせますという関係があり、この区別で確認する名称は「LOGONLY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Admin_Guide / Db2_zOS_Performance / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 新しい月次明細ファイルを PAYROLL 表へ一括投入し、入力行をDb2表に格納したい状況です。使うユーティリティ本体はどれですか。</p><ul class="kb-choices"><li>A. 表ロード <span class="kb-ok">✅ 正解</span></li><li>B. 統計収集</li><li>C. コピー統合</li><li>D. 整合性検査</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 表へ入力データを格納する処理なので、Aを選びます。ロード処理は外部データを表へ取り込むユーティリティです。Bは表ロードと別の統計収集による統計取得です。Cは表ロードと別のコピー統合のコピー統合です。Dは表ロードと別の表データ検査や索引検査が担う確認です。追記か入替かを必ず見分けます；背景には外部ファイルから表へ大量データを取り込む作業では、LOAD が Db2 のユーティリティ制御文として使われます、追記、入替、制約検査、ログ取得などを指定しながら、表やパーティションへ入力データを格納します、業務データを壊さないため、RESUME と REPLACE の違いを実行前に確認しますという関係があり、この区別で確認する名称は「LOAD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 本番表の一部データを検証環境へ渡すため、Db2表から順序立てて外部ファイルへ取り出したい状況です。選ぶ処理はどれですか。</p><ul class="kb-choices"><li>A. 索引再構築</li><li>B. 表抽出 <span class="kb-ok">✅ 正解</span></li><li>C. 権限削除</li><li>D. ログ適用</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 表データを外へ取り出す処理であり、Bが正解です。表抽出は表や表スペースの内容をデータセットへ出力します。Aは表抽出と別の索引再構築です。Cは権限操作でありユーティリティ本体ではありません。Dは表抽出と別の回復処理の回復処理です。再ロードに使う場合は出力形式も確認します；背景には表や表スペースの内容を外部データセットへ取り出すとき、UNLOAD は Db2 のユーティリティ制御文として利用されます、抽出データは移行、検証、再ロード用の入力として使えます、出力形式や生成されるLOAD制御文を確認し、後続処理が読み取れる形にしますという関係があり、この区別で確認する名称は「UNLOAD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> PAYDB.PAYTS のリカバリーに備え、表スペースのイメージコピーを定期取得する運用を組みます。採るべき処理はどれですか。</p><ul class="kb-choices"><li>A. 統計更新</li><li>B. 表再編成</li><li>C. 画像コピー <span class="kb-ok">✅ 正解</span></li><li>D. 入力整合検査</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 回復用のイメージコピーを取得するため、Cを選びます。COPYは表スペースや索引スペースの内容をリカバリー用コピーとして保存します。Aは外部ファイルから表へ行を投入する処理です。Bは表から外部ファイルへデータを取り出します。Dはコピーとログを使ってオブジェクトを戻します。取得先と保存世代を運用ルールに合わせます；背景には回復に備えてイメージコピーを取得する場合、COPY は Db2 のユーティリティ制御文として表スペースや索引スペースのリカバリー用コピーを取得します、ローカル用と災対用のコピーを分けられ、COPYDDNやRECOVERYDDNで出力先を指定できます、コピー未取得状態を避けるため、対象と共有レベルを確認しますという関係があり、この区別で確認する名称は「COPY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 誤更新の直前まで PAYDB.PAYTS を戻し、コピーとログから整合した状態を作り直します。対象の制御文はどれですか。</p><ul class="kb-choices"><li>A. 対象リスト</li><li>B. ロード入力</li><li>C. 統計採取</li><li>D. 回復処理 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーとログを使って戻す処理なので、Dが正解です。回復処理は表スペースなどを現在時点または過去時点へ回復します。Aは回復処理と別の対象リスト定義です。Bは回復処理と別のロード処理です。Cは回復処理と別の統計収集です。関連する索引や参照関係を同じ回復点にそろえます；背景には障害後にオブジェクトを戻す作業では、RECOVER が Db2 のユーティリティ制御文としてイメージコピーとログを使い、表スペースや索引を回復します、現在時点まで戻す場合と、TORBAやTOLOGPOINTで過去時点へ戻す場合があります、複数オブジェクトの一貫性を保つ計画が必要ですという関係があり、この区別で確認する名称は「RECOVER」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 更新を重ねた表スペースでデータ配置が乱れ、範囲検索の効率を戻す必要があります。実施対象として最も適切なものはどれですか。</p><ul class="kb-choices"><li>A. 表再編成 <span class="kb-ok">✅ 正解</span></li><li>B. 索引検査</li><li>C. コピー統合</li><li>D. 診断採取</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表スペースのデータ配置を整えるため、Aを選びます。表スペース再編成はデータを再配置して断片化や配置の乱れを改善します。Bは表再編成と別の索引検査です。Cは表再編成と別のコピー統合です。Dは表再編成と別の診断資料取得や低レベル修復系の調査です。停止時間を抑えるには共有レベルも見ます；背景には表スペース内のデータ配置を整えるとき、REORG TABLESPACE は Db2 のユーティリティ制御文としてデータを再編成します、断片化やページの空き、クラスタリング順の乱れを改善し、必要に応じて統計も同時取得できます、共有レベルの指定により、業務処理との並行性が変わりますという関係があり、この区別で確認する名称は「TABLESPACE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 表データではなく特定索引の構造のみを整え、検索効率を改善します。選択すべき処理はどれですか。</p><ul class="kb-choices"><li>A. 表コピー取得</li><li>B. 索引再編成 <span class="kb-ok">✅ 正解</span></li><li>C. ログ回復</li><li>D. 統計削除</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 索引スペースを再編成する処理なので、Bが合います。索引再編成は索引の配置や空き状態を整えます。Aはバックアップ用コピーを取得する処理です。Cはコピーとログを使って戻す処理です。Dは古い統計履歴を整理する保守処理です。表スペース再編成と対象を分けて判断します；背景には索引の構造を整える場合、REORG INDEX は Db2 のユーティリティ制御文として索引スペースを再編成します、索引の物理配置や空き状態を改善し、検索性能の回復に使われます、表データ全体を再配置するREORG TABLESPACEとは対象が異なりますという関係があり、この区別で確認する名称は「REORG」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> オプティマイザーが最新の行数や値分布を使えるよう、表と索引の統計を取り直したい状況です。実行するものはどれですか。</p><ul class="kb-choices"><li>A. 回復停止点</li><li>B. 入力破棄</li><li>C. 統計収集 <span class="kb-ok">✅ 正解</span></li><li>D. コピー取得</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 統計を集める処理なので、Cが該当します。統計収集はDb2オブジェクトの統計を収集し、アクセスパス選択の材料にします。Aは統計収集と別の回復処理の位置指定です。Bは統計収集と別のロード処理のDISCARDSです。Dは統計収集と別のコピー取得です。更新頻度の高い表では定期実行が重要です；背景にはアクセスパスの見積りを改善するため、RUNSTATS は Db2 のユーティリティ制御文として表、表スペース、索引の統計を収集します、カーディナリティ、頻度値、ヒストグラムなどを取得できます、収集結果をカタログへ反映するか、レポートのみ出すかも確認しますという関係があり、この区別で確認する名称は「RUNSTATS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> ロード後に参照制約違反の有無を確認し、表スペースの CHECK-pending を解消します。確認に使う処理はどれですか。</p><ul class="kb-choices"><li>A. 統計収集処理</li><li>B. コピー統合処理</li><li>C. 索引再構築処理</li><li>D. 表検査 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 表データと制約の整合性を検査するため、Dが正解です。表データ検査は表スペース内の行と制約違反を確認します。Aは統計系で、アクセスパス用の材料を集めます。Bはコピー世代を統合して復旧時の扱いを減らします。Cは壊れた索引を表データから作り直します。索引整合性も必要に応じて確認します；背景には表データと参照制約の整合性を確認するとき、CHECK DATA は Db2 のユーティリティ制御文として表スペース内のデータを検査します、ロード後や条件付き再始動後に、CHECK-pending状態の解消や不整合検出に使われます、索引が正しいことを前提にするため、必要ならCHECK INDEXも先に確認しますという関係があり、この区別で確認する名称は「DATA」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 障害後に索引が表データと一致しているかを調べ、必要なら再構築へ進めたい状況です。最初に使う検査はどれですか。</p><ul class="kb-choices"><li>A. 索引検査 <span class="kb-ok">✅ 正解</span></li><li>B. 表ロード</li><li>C. コピー取得</li><li>D. 統計削除</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 索引の整合性を見る処理なので、Aを選びます。索引検査は索引とデータの対応を確認します。Bは外部入力を表へ格納するロード処理です。Cはリカバリーに使うコピーを取得します。Dは古い統計収集結果を保持方針に沿って整理します。問題が見つかれば索引再構築へ進みます；背景には索引と表データの対応を確認する場合、CHECK INDEX は Db2 のユーティリティ制御文として索引の整合性を検査します、不整合な索引はREBUILD INDEXで再作成する判断につながります、表データ検査が索引を利用する場面では、先に索引の信頼性を確認することがありますという関係があり、この区別で確認する名称は「CHECK」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 索引が REBUILD-pending になり、表データを基に作り直す必要があります。実行候補として正しいものはどれですか。</p><ul class="kb-choices"><li>A. 索引再編成</li><li>B. 索引再構築 <span class="kb-ok">✅ 正解</span></li><li>C. 表抽出</li><li>D. 回復情報表示</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 索引を表データから作り直すため、Bが正解です。索引再構築は壊れた索引や保留状態の索引を再構築します。Aは索引再構築と別の索引再編成で、既存索引を整理する処理です。Cは索引再構築と別の表抽出です。Dは索引再構築と別の回復情報報告です。状態解消後にアクセス可否を確認します；背景には壊れた索引を作り直す場合、REBUILD INDEX は Db2 のユーティリティ制御文として表データから索引を再構築します、REBUILD-pending状態やCHECK INDEXで見つかった不整合の解消に使われます、表データを正とし、索引構造を新しく作る点がREORG INDEXと違いますという関係があり、この区別で確認する名称は「REBUILD」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 過去の RUNSTATS 履歴が増えすぎたため、保存方針に従って古い統計情報を整理します。この対象を扱う処理はどれですか。</p><ul class="kb-choices"><li>A. コピー取得処理</li><li>B. 表検査</li><li>C. 索引再構築処理</li><li>D. 統計履歴 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 統計関連の履歴を整理するため、Dを選びます。統計履歴整理は古い収集結果を保持方針に沿って管理します。Aは回復用のコピーを保存する処理です。Bは表データの制約違反を確認します。Cは壊れた索引を表データから復元します。現在のアクセスパス検討に必要な統計を残します；背景には古くなった統計履歴を整理する場合、MODIFY STATISTICS は Db2 のユーティリティ制御文としてカタログ内の統計関連履歴を削除または整理します、統計収集で増えた履歴を保持方針に沿って減らすために使います、最新のアクセスパス判断に必要な統計を消さないよう注意しますという関係があり、この区別で確認する名称は「STATISTICS」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 回復作業を始める前に、必要なコピーやログ情報を一覧で確認し、復旧計画の材料にしたい状況です。使うものはどれですか。</p><ul class="kb-choices"><li>A. 表再編成処理</li><li>B. 容量割当</li><li>C. 回復情報 <span class="kb-ok">✅ 正解</span></li><li>D. 制約検査</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 回復に必要な情報を報告するため、Cが正解です。回復情報報告はコピーやログの状況を確認するための処理です。Aは表スペースの物理配置を改善します。Bは出力データセットの大きさをTEMPLATEなどで決めます。Dはロード後の制約整合性を確認します。実際の回復前に証跡として残します；背景には復旧に必要な情報を調べるとき、REPORT RECOVERY は Db2 のユーティリティ制御文としてコピー、ログ、回復関連の情報を出力します、回復実行前に、どのコピーやログが必要かを確認する材料になります、障害対応時には、SYSIBM.SYSCOPYの状態確認にも役立ちますという関係があり、この区別で確認する名称は「RECOVERY」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> 通常のRECOVERやREBUILDでは直せない不整合について、IBMサポートの指示に従い低レベルの診断・修復を行う状況です。該当するものはどれですか。</p><ul class="kb-choices"><li>A. 統計収集処理</li><li>B. コピー取得処理</li><li>C. 表抽出</li><li>D. 低レベル <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 低レベルの診断や修復を行うため、Dが正解です。修復系の処理は強力です。一方で、誤った使い方で整合性を失う危険があります。Aはアクセスパス向けの統計情報を集めます。Bはリカバリー用のコピーを保存します。Cは表データを外部ファイルへ出します。通常の保守ではなく、手順と承認を明確にして使います；背景にはデータやカタログの不整合を診断・修復する特別な作業では、REPAIR が Db2 のユーティリティ制御文として使われます、位置特定、検証、置換、ダンプ、状態設定などの機能があります、誤用するとデータ保全を損なうため、通常運用ではなく障害対応として慎重に扱いますという関係があり、この区別で確認する名称は「REPAIR」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> データ不整合が疑われるが、まず内部状態を調べる資料を取得し、修復判断の材料にしたい状況です。実行するものはどれですか。</p><ul class="kb-choices"><li>A. 診断資料 <span class="kb-ok">✅ 正解</span></li><li>B. 表ロード</li><li>C. コピー統合</li><li>D. 統計更新</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 診断用の資料を集めるため、Aを選びます。診断資料取得は問題の判断材料を出すユーティリティです。Bは診断資料と別のロード処理です。Cは診断資料と別のコピー統合です。Dは診断資料と別の統計収集や統計履歴整理の領域です。修復を行う前の調査として扱います；背景には障害解析用の情報を集める場合、DIAGNOSE は Db2 のユーティリティ制御文として内部状態やオブジェクト状態の診断資料を出力します、修復そのものより、問題判定やサポート連携の材料を得る目的で使います、出力の読み取りにはDb2内部構造の知識が必要ですという関係があり、この区別で確認する名称は「DIAGNOSE」です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_Introduction / Db2_zOS_Troubleshooting / Db2_zOS_Messages</p></div><div class="kb-q"><p><strong>問題.</strong> コピー作成を保守計画で確認します。Db2の作業記録にイメージコピー作成の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. TEMPLATE</li><li>B. RUNSTATS</li><li>C. COPY TABLESPACE <span class="kb-ok">✅ 正解</span></li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点コピー作成は、回復に使うフルまたは増分コピーを登録することを目的に扱い、確認項目はコピー作成判断です。背景コピー作成として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー作成定義です。コピー作成の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー作成根拠です。A: コピー作成で見るデータセットひな形は代替にならず、今回の比較対象から外す理由はコピー作成保守です。B: コピー作成で見る統計収集は代替にならず、今回の比較対象から外す理由はコピー作成棚卸です。C: コピー作成が正答です。コピー登録とデータセット存在を照合することに合うため、採否を決める説明軸はコピー作成観点です。D: コピー作成で見る表スペース再編成は代替にならず、今回の比較対象から外す理由はコピー作成証跡です。初出語コピー作成とは、技術項目名 COPY TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー作成観点です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース回復を保守計画で確認します。Db2の作業記録に表スペース回復の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はコピー履歴カタログのSTART_ログ位置列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. COPYDDN</li><li>B. SHRLEVEL CHANGE</li><li>C. SYSIBM.SYSCOPY</li><li>D. RECOVER TABLESPACE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点表スペース回復は、イメージコピーとログを使って表スペースを戻することを目的に扱い、確認項目は表スペース回復定義です。背景表スペース回復として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース回復根拠です。表スペース回復の仕組みは、コピー履歴カタログの開始ログ位置列と実行ログを照合する理由が表スペース回復列確認です。A: 表スペース回復で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は表スペース回復棚卸です。B: 表スペース回復で見る更新並行方式保守は代替にならず、今回の比較対象から外す理由は表スペース回復観点です。C: 表スペース回復で見るコピー履歴表は代替にならず、今回の比較対象から外す理由は表スペース回復証跡です。D: 表スペース回復が正答です。回復点とコピー履歴を確認することに合うため、採否を決める説明軸は表スペース回復読取です。初出語表スペース回復とは、技術項目名 RECOVER TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース回復証跡です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 置換ロードを保守計画で確認します。Db2の作業記録に置換ロードの根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は表スペースカタログのロード_STATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. LOAD REPLACE <span class="kb-ok">✅ 正解</span></li><li>B. FLASHCOPY</li><li>C. DISPLAY DATABASE</li><li>D. COPY TABLESPACE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点置換ロードは、既存データを置き換えて入力データをロードすることを目的に扱い、確認項目は置換ロード根拠です。背景置換ロードとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は置換ロード列確認です。置換ロードの仕組みは、表スペースカタログのロード状態列と実行ログを照合する理由が置換ロード復旧です。A: 置換ロードが正答です。ロード後の制限状態と統計収集を確認することに合うため、採否を決める説明軸は置換ロード観点です。B: 置換ロードで見るストレージコピーは代替にならず、今回の比較対象から外す理由は置換ロード証跡です。C: 置換ロードで見るデータベース状態表示は代替にならず、今回の比較対象から外す理由は置換ロード読取です。D: 置換ロードで見るイメージコピー作成は代替にならず、今回の比較対象から外す理由は置換ロード判断です。初出語置換ロードとは、技術項目名 LOAD REPLACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は置換ロード読取です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 状態補修を保守計画で確認します。Db2の作業記録に制限状態の補修の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. COPYDDN</li><li>B. MODIFY RECOVERY</li><li>C. RECOVER TABLESPACE</li><li>D. REPAIR SET <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点状態補修は、カタログ状態やページ情報を補修するために使うことを目的に扱い、確認項目は状態補修読取です。背景状態補修として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は状態補修判断です。状態補修の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が状態補修定義です。A: 状態補修で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は状態補修復旧です。B: 状態補修で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由は状態補修保守です。C: 状態補修で見る表スペース回復は代替にならず、今回の比較対象から外す理由は状態補修棚卸です。D: 状態補修が正答です。補修対象とメッセージを厳密に限定することに合うため、採否を決める説明軸は状態補修観点です。初出語状態補修とは、技術項目名 REPAIR SET で表すDb2ユーティリティ、指定、または記録名であり、用語定義は状態補修棚卸です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 共通指定を保守計画で確認します。Db2の作業記録に実行共通指定の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はユーティリティ実行カタログのUTILITY列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE</li><li>B. UNLOAD</li><li>C. REBUILD INDEX</li><li>D. OPTIONS <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点共通指定は、対象リストやひな形のライブラリなどを上書きすることを目的に扱い、確認項目は共通指定列確認です。背景共通指定として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は共通指定復旧です。共通指定の仕組みは、ユーティリティ実行カタログのユーティリティ名列と実行ログを照合する理由が共通指定保守です。A: 共通指定で見る表スペース回復は代替にならず、今回の比較対象から外す理由は共通指定証跡です。B: 共通指定で見るデータ抽出は代替にならず、今回の比較対象から外す理由は共通指定読取です。C: 共通指定で見る索引再構築は代替にならず、今回の比較対象から外す理由は共通指定判断です。D: 共通指定が正答です。ジョブ単位の既定値と差分を確認することに合うため、採否を決める説明軸は共通指定定義です。初出語共通指定とは、技術項目名 OPTIONS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は共通指定判断です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 更新並行方式を保守計画で確認します。Db2の作業記録に更新並行方式保守の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は表スペースカタログのTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. DSNUTILB</li><li>B. SYSIBM.SYSTABLESPACE</li><li>C. SHRLEVEL CHANGE <span class="kb-ok">✅ 正解</span></li><li>D. LOAD REPLACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点更新並行方式は、ユーティリティ中も更新を許す方式を選ぶことを目的に扱い、確認項目は更新並行方式棚卸です。背景更新並行方式として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は更新並行方式観点です。更新並行方式の仕組みは、表スペースカタログのTYPE列と実行ログを照合する理由が更新並行方式証跡です。A: 更新並行方式で見るユーティリティ制御プログラムは代替にならず、今回の比較対象から外す理由は更新並行方式定義です。B: 更新並行方式で見る表スペース状態表は代替にならず、今回の比較対象から外す理由は更新並行方式根拠です。C: 更新並行方式が正答です。並行更新とログ適用の影響を確認することに合うため、採否を決める説明軸は更新並行方式列確認です。D: 更新並行方式で見る置換ロードは代替にならず、今回の比較対象から外す理由は更新並行方式復旧です。初出語更新並行方式とは、技術項目名 SHRLEVEL CHANGE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は更新並行方式列確認です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 高速コピーを保守計画で確認します。Db2の作業記録にストレージコピーの根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はコピー履歴カタログのDSVOLSER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. OPTIONS</li><li>B. REORG TABLESPACE</li><li>C. REPAIR SET</li><li>D. FLASHCOPY <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点高速コピーは、ストレージ機能で高速にコピーを作成することを目的に扱い、確認項目は高速コピー観点です。背景高速コピーとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は高速コピー証跡です。高速コピーの仕組みは、コピー履歴カタログのDSVOLSER列と実行ログを照合する理由が高速コピー読取です。A: 高速コピーで見る実行共通指定は代替にならず、今回の比較対象から外す理由は高速コピー根拠です。B: 高速コピーで見る表スペース再編成は代替にならず、今回の比較対象から外す理由は高速コピー列確認です。C: 高速コピーで見る制限状態の補修は代替にならず、今回の比較対象から外す理由は高速コピー復旧です。D: 高速コピーが正答です。バックアウト情報と回復入力を確認することに合うため、採否を決める説明軸は高速コピー保守です。初出語高速コピーとは、技術項目名 FLASHCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義は高速コピー復旧です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー履歴を保守計画で確認します。Db2の作業記録にコピー履歴表の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSCOPY <span class="kb-ok">✅ 正解</span></li><li>B. SHRLEVEL CHANGE</li><li>C. CHECK DATA</li><li>D. RUNSTATS</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点コピー履歴は、コピーや回復に必要な履歴を保持することを目的に扱い、確認項目はコピー履歴証跡です。背景コピー履歴として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー履歴読取です。コピー履歴の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー履歴判断です。A: コピー履歴が正答です。データセット名と回復可能性を確認することに合うため、採否を決める説明軸はコピー履歴列確認です。B: コピー履歴で見る更新並行方式保守は代替にならず、今回の比較対象から外す理由はコピー履歴復旧です。C: コピー履歴で見る参照整合性検査は代替にならず、今回の比較対象から外す理由はコピー履歴保守です。D: コピー履歴で見る統計収集は代替にならず、今回の比較対象から外す理由はコピー履歴棚卸です。初出語コピー履歴とは、技術項目名 SYSIBM.SYSCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー履歴保守です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース状態を保守計画で確認します。Db2の作業記録に表スペース状態表の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. SYSIBM.SYSTABLESPACE <span class="kb-ok">✅ 正解</span></li><li>C. REPAIR SET</li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点表スペース状態は、表スペースの定義や状態を確認することを目的に扱い、確認項目は表スペース状態読取です。背景表スペース状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース状態判断です。表スペース状態の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が表スペース状態定義です。A: 表スペース状態で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は表スペース状態復旧です。B: 表スペース状態が正答です。制限状態や保守対象を確認することに合うため、採否を決める説明軸は表スペース状態保守です。C: 表スペース状態で見る制限状態の補修は代替にならず、今回の比較対象から外す理由は表スペース状態棚卸です。D: 表スペース状態で見る表スペース再編成は代替にならず、今回の比較対象から外す理由は表スペース状態観点です。初出語表スペース状態とは、技術項目名 SYSIBM.SYSTABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース状態棚卸です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 索引パート状態を保守計画で確認します。Db2の作業記録に索引パート状態表の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時は索引パートカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. COPYDDN</li><li>C. SYSIBM.SYSINDEXPART <span class="kb-ok">✅ 正解</span></li><li>D. QUIESCE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点索引パート状態は、索引パートの状態を確認することを目的に扱い、確認項目は索引パート状態判断です。背景索引パート状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は索引パート状態定義です。索引パート状態の仕組みは、索引パートカタログの状態列と実行ログを照合する理由が索引パート状態根拠です。A: 索引パート状態で見る統計収集は代替にならず、今回の比較対象から外す理由は索引パート状態保守です。B: 索引パート状態で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は索引パート状態棚卸です。C: 索引パート状態が正答です。索引再構築の要否を判断することに合うため、採否を決める説明軸は索引パート状態観点です。D: 索引パート状態で見る静止点取得は代替にならず、今回の比較対象から外す理由は索引パート状態証跡です。初出語索引パート状態とは、技術項目名 SYSIBM.SYSINDEXPART で表すDb2ユーティリティ、指定、または記録名であり、用語定義は索引パート状態観点です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー作成を障害復旧で確認します。Db2の作業記録にイメージコピー作成の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. COPYDDN</li><li>B. SHRLEVEL CHANGE</li><li>C. SYSIBM.SYSCOPY</li><li>D. COPY TABLESPACE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点コピー作成は、回復に使うフルまたは増分コピーを登録することを目的に扱い、確認項目はコピー作成保守です。背景コピー作成として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー作成棚卸です。コピー作成の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー作成観点です。A: コピー作成で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由はコピー作成判断です。B: コピー作成で見る更新並行方式保守は代替にならず、今回の比較対象から外す理由はコピー作成定義です。C: コピー作成で見るコピー履歴表は代替にならず、今回の比較対象から外す理由はコピー作成根拠です。D: コピー作成が正答です。コピー登録とデータセット存在を照合することに合うため、採否を決める説明軸はコピー作成列確認です。初出語コピー作成とは、技術項目名 COPY TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー作成根拠です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース回復を障害復旧で確認します。Db2の作業記録に表スペース回復の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はコピー履歴カタログのSTART_ログ位置列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE <span class="kb-ok">✅ 正解</span></li><li>B. FLASHCOPY</li><li>C. DISPLAY DATABASE</li><li>D. COPY TABLESPACE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点表スペース回復は、イメージコピーとログを使って表スペースを戻することを目的に扱い、確認項目は表スペース回復棚卸です。背景表スペース回復として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース回復観点です。表スペース回復の仕組みは、コピー履歴カタログの開始ログ位置列と実行ログを照合する理由が表スペース回復証跡です。A: 表スペース回復が正答です。回復点とコピー履歴を確認することに合うため、採否を決める説明軸は表スペース回復定義です。B: 表スペース回復で見るストレージコピーは代替にならず、今回の比較対象から外す理由は表スペース回復根拠です。C: 表スペース回復で見るデータベース状態表示は代替にならず、今回の比較対象から外す理由は表スペース回復列確認です。D: 表スペース回復で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由は表スペース回復復旧です。初出語表スペース回復とは、技術項目名 RECOVER TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース回復列確認です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 置換ロードを障害復旧で確認します。Db2の作業記録に置換ロードの根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は表スペースカタログのロード_STATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. LOAD REPLACE <span class="kb-ok">✅ 正解</span></li><li>C. RECOVER TABLESPACE</li><li>D. MERGECOPY</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点置換ロードは、既存データを置き換えて入力データをロードすることを目的に扱い、確認項目は置換ロード観点です。背景置換ロードとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は置換ロード証跡です。置換ロードの仕組みは、表スペースカタログのロード状態列と実行ログを照合する理由が置換ロード読取です。A: 置換ロードで見る索引パート状態表は代替にならず、今回の比較対象から外す理由は置換ロード根拠です。B: 置換ロードが正答です。ロード後の制限状態と統計収集を確認することに合うため、採否を決める説明軸は置換ロード列確認です。C: 置換ロードで見る表スペース回復は代替にならず、今回の比較対象から外す理由は置換ロード復旧です。D: 置換ロードで見る増分コピー統合は代替にならず、今回の比較対象から外す理由は置換ロード保守です。初出語置換ロードとは、技術項目名 LOAD REPLACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は置換ロード復旧です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 状態補修を障害復旧で確認します。Db2の作業記録に制限状態の補修の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. REPAIR SET <span class="kb-ok">✅ 正解</span></li><li>B. FLASHCOPY</li><li>C. OPTIONS</li><li>D. MERGECOPY</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点状態補修は、カタログ状態やページ情報を補修するために使うことを目的に扱い、確認項目は状態補修復旧です。背景状態補修として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は状態補修保守です。状態補修の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が状態補修棚卸です。A: 状態補修が正答です。補修対象とメッセージを厳密に限定することに合うため、採否を決める説明軸は状態補修読取です。B: 状態補修で見るストレージコピーは代替にならず、今回の比較対象から外す理由は状態補修判断です。C: 状態補修で見る実行共通指定は代替にならず、今回の比較対象から外す理由は状態補修定義です。D: 状態補修で見る増分コピー統合は代替にならず、今回の比較対象から外す理由は状態補修根拠です。初出語状態補修とは、技術項目名 REPAIR SET で表すDb2ユーティリティ、指定、または記録名であり、用語定義は状態補修定義です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 共通指定を障害復旧で確認します。Db2の作業記録に実行共通指定の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はユーティリティ実行カタログのUTILITY列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. OPTIONS <span class="kb-ok">✅ 正解</span></li><li>B. CHECK DATA</li><li>C. MERGECOPY</li><li>D. LISTDEF</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点共通指定は、対象リストやひな形のライブラリなどを上書きすることを目的に扱い、確認項目は共通指定証跡です。背景共通指定として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は共通指定読取です。共通指定の仕組みは、ユーティリティ実行カタログのユーティリティ名列と実行ログを照合する理由が共通指定判断です。A: 共通指定が正答です。ジョブ単位の既定値と差分を確認することに合うため、採否を決める説明軸は共通指定列確認です。B: 共通指定で見る参照整合性検査は代替にならず、今回の比較対象から外す理由は共通指定復旧です。C: 共通指定で見る増分コピー統合は代替にならず、今回の比較対象から外す理由は共通指定保守です。D: 共通指定で見る対象リスト定義は代替にならず、今回の比較対象から外す理由は共通指定棚卸です。初出語共通指定とは、技術項目名 OPTIONS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は共通指定保守です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 更新並行方式を障害復旧で確認します。Db2の作業記録に更新並行方式保守の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は表スペースカタログのTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. OPTIONS</li><li>B. REORG TABLESPACE</li><li>C. REPAIR SET</li><li>D. SHRLEVEL CHANGE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点更新並行方式は、ユーティリティ中も更新を許す方式を選ぶことを目的に扱い、確認項目は更新並行方式定義です。背景更新並行方式として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は更新並行方式根拠です。更新並行方式の仕組みは、表スペースカタログのTYPE列と実行ログを照合する理由が更新並行方式列確認です。A: 更新並行方式で見る実行共通指定は代替にならず、今回の比較対象から外す理由は更新並行方式棚卸です。B: 更新並行方式で見る表スペース再編成は代替にならず、今回の比較対象から外す理由は更新並行方式観点です。C: 更新並行方式で見る制限状態の補修は代替にならず、今回の比較対象から外す理由は更新並行方式証跡です。D: 更新並行方式が正答です。並行更新とログ適用の影響を確認することに合うため、採否を決める説明軸は更新並行方式読取です。初出語更新並行方式とは、技術項目名 SHRLEVEL CHANGE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は更新並行方式証跡です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 高速コピーを障害復旧で確認します。Db2の作業記録にストレージコピーの根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はコピー履歴カタログのDSVOLSER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. FLASHCOPY <span class="kb-ok">✅ 正解</span></li><li>B. SHRLEVEL CHANGE</li><li>C. CHECK DATA</li><li>D. RUNSTATS</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点高速コピーは、ストレージ機能で高速にコピーを作成することを目的に扱い、確認項目は高速コピー根拠です。背景高速コピーとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は高速コピー列確認です。高速コピーの仕組みは、コピー履歴カタログのDSVOLSER列と実行ログを照合する理由が高速コピー復旧です。A: 高速コピーが正答です。バックアウト情報と回復入力を確認することに合うため、採否を決める説明軸は高速コピー観点です。B: 高速コピーで見る更新並行方式保守は代替にならず、今回の比較対象から外す理由は高速コピー証跡です。C: 高速コピーで見る参照整合性検査は代替にならず、今回の比較対象から外す理由は高速コピー読取です。D: 高速コピーで見る統計収集は代替にならず、今回の比較対象から外す理由は高速コピー判断です。初出語高速コピーとは、技術項目名 FLASHCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義は高速コピー読取です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー履歴を障害復旧で確認します。Db2の作業記録にコピー履歴表の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. SYSIBM.SYSCOPY <span class="kb-ok">✅ 正解</span></li><li>C. REPAIR SET</li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点コピー履歴は、コピーや回復に必要な履歴を保持することを目的に扱い、確認項目はコピー履歴列確認です。背景コピー履歴として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー履歴復旧です。コピー履歴の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー履歴保守です。A: コピー履歴で見る索引パート状態表は代替にならず、今回の比較対象から外す理由はコピー履歴証跡です。B: コピー履歴が正答です。データセット名と回復可能性を確認することに合うため、採否を決める説明軸はコピー履歴読取です。C: コピー履歴で見る制限状態の補修は代替にならず、今回の比較対象から外す理由はコピー履歴判断です。D: コピー履歴で見る表スペース再編成は代替にならず、今回の比較対象から外す理由はコピー履歴定義です。初出語コピー履歴とは、技術項目名 SYSIBM.SYSCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー履歴判断です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース状態を障害復旧で確認します。Db2の作業記録に表スペース状態表の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. COPYDDN</li><li>C. SYSIBM.SYSTABLESPACE <span class="kb-ok">✅ 正解</span></li><li>D. QUIESCE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点表スペース状態は、表スペースの定義や状態を確認することを目的に扱い、確認項目は表スペース状態復旧です。背景表スペース状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース状態保守です。表スペース状態の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が表スペース状態棚卸です。A: 表スペース状態で見る統計収集は代替にならず、今回の比較対象から外す理由は表スペース状態読取です。B: 表スペース状態で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は表スペース状態判断です。C: 表スペース状態が正答です。制限状態や保守対象を確認することに合うため、採否を決める説明軸は表スペース状態定義です。D: 表スペース状態で見る静止点取得は代替にならず、今回の比較対象から外す理由は表スペース状態根拠です。初出語表スペース状態とは、技術項目名 SYSIBM.SYSTABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース状態定義です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 索引パート状態を障害復旧で確認します。Db2の作業記録に索引パート状態表の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時は索引パートカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE</li><li>B. SYSIBM.SYSTABLESPACE</li><li>C. OPTIONS</li><li>D. SYSIBM.SYSINDEXPART <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点索引パート状態は、索引パートの状態を確認することを目的に扱い、確認項目は索引パート状態保守です。背景索引パート状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は索引パート状態棚卸です。索引パート状態の仕組みは、索引パートカタログの状態列と実行ログを照合する理由が索引パート状態観点です。A: 索引パート状態で見る表スペース回復は代替にならず、今回の比較対象から外す理由は索引パート状態判断です。B: 索引パート状態で見る表スペース状態表は代替にならず、今回の比較対象から外す理由は索引パート状態定義です。C: 索引パート状態で見る実行共通指定は代替にならず、今回の比較対象から外す理由は索引パート状態根拠です。D: 索引パート状態が正答です。索引再構築の要否を判断することに合うため、採否を決める説明軸は索引パート状態列確認です。初出語索引パート状態とは、技術項目名 SYSIBM.SYSINDEXPART で表すDb2ユーティリティ、指定、または記録名であり、用語定義は索引パート状態根拠です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー作成を性能維持で確認します。Db2の作業記録にイメージコピー作成の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. COPY TABLESPACE <span class="kb-ok">✅ 正解</span></li><li>B. FLASHCOPY</li><li>C. DISPLAY DATABASE</li><li>D. RECOVER TABLESPACE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点コピー作成は、回復に使うフルまたは増分コピーを登録することを目的に扱い、確認項目はコピー作成判断です。背景コピー作成として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー作成定義です。コピー作成の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー作成根拠です。A: コピー作成が正答です。コピー登録とデータセット存在を照合することに合うため、採否を決める説明軸はコピー作成保守です。B: コピー作成で見るストレージコピーは代替にならず、今回の比較対象から外す理由はコピー作成棚卸です。C: コピー作成で見るデータベース状態表示は代替にならず、今回の比較対象から外す理由はコピー作成観点です。D: コピー作成で見る表スペース回復は代替にならず、今回の比較対象から外す理由はコピー作成証跡です。初出語コピー作成とは、技術項目名 COPY TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー作成観点です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース回復を性能維持で確認します。Db2の作業記録に表スペース回復の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はコピー履歴カタログのSTART_ログ位置列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. RECOVER TABLESPACE <span class="kb-ok">✅ 正解</span></li><li>C. LOAD REPLACE</li><li>D. MERGECOPY</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点表スペース回復は、イメージコピーとログを使って表スペースを戻することを目的に扱い、確認項目は表スペース回復定義です。背景表スペース回復として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース回復根拠です。表スペース回復の仕組みは、コピー履歴カタログの開始ログ位置列と実行ログを照合する理由が表スペース回復列確認です。A: 表スペース回復で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は表スペース回復棚卸です。B: 表スペース回復が正答です。回復点とコピー履歴を確認することに合うため、採否を決める説明軸は表スペース回復観点です。C: 表スペース回復で見る置換ロードは代替にならず、今回の比較対象から外す理由は表スペース回復証跡です。D: 表スペース回復で見る増分コピー統合は代替にならず、今回の比較対象から外す理由は表スペース回復読取です。初出語表スペース回復とは、技術項目名 RECOVER TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース回復証跡です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 置換ロードを性能維持で確認します。Db2の作業記録に置換ロードの根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は表スペースカタログのロード_STATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. MODIFY RECOVERY</li><li>C. LOAD REPLACE <span class="kb-ok">✅ 正解</span></li><li>D. RECOVERYDDN</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点置換ロードは、既存データを置き換えて入力データをロードすることを目的に扱い、確認項目は置換ロード根拠です。背景置換ロードとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は置換ロード列確認です。置換ロードの仕組みは、表スペースカタログのロード状態列と実行ログを照合する理由が置換ロード復旧です。A: 置換ロードで見る統計収集は代替にならず、今回の比較対象から外す理由は置換ロード観点です。B: 置換ロードで見る回復履歴の削除は代替にならず、今回の比較対象から外す理由は置換ロード証跡です。C: 置換ロードが正答です。ロード後の制限状態と統計収集を確認することに合うため、採否を決める説明軸は置換ロード読取です。D: 置換ロードで見る回復用データ定義名は代替にならず、今回の比較対象から外す理由は置換ロード判断です。初出語置換ロードとは、技術項目名 LOAD REPLACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は置換ロード読取です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 状態補修を性能維持で確認します。Db2の作業記録に制限状態の補修の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. REPAIR SET <span class="kb-ok">✅ 正解</span></li><li>C. SYSIBM.SYSCOPY</li><li>D. SHRLEVEL CHANGE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点状態補修は、カタログ状態やページ情報を補修するために使うことを目的に扱い、確認項目は状態補修読取です。背景状態補修として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は状態補修判断です。状態補修の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が状態補修定義です。A: 状態補修で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は状態補修復旧です。B: 状態補修が正答です。補修対象とメッセージを厳密に限定することに合うため、採否を決める説明軸は状態補修保守です。C: 状態補修で見るコピー履歴表は代替にならず、今回の比較対象から外す理由は状態補修棚卸です。D: 状態補修で見る更新並行方式保守は代替にならず、今回の比較対象から外す理由は状態補修観点です。初出語状態補修とは、技術項目名 REPAIR SET で表すDb2ユーティリティ、指定、または記録名であり、用語定義は状態補修棚卸です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 共通指定を性能維持で確認します。Db2の作業記録に実行共通指定の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はユーティリティ実行カタログのUTILITY列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. MODIFY RECOVERY</li><li>B. OPTIONS <span class="kb-ok">✅ 正解</span></li><li>C. COPYDDN</li><li>D. SYSIBM.SYSINDEXPART</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点共通指定は、対象リストやひな形のライブラリなどを上書きすることを目的に扱い、確認項目は共通指定列確認です。背景共通指定として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は共通指定復旧です。共通指定の仕組みは、ユーティリティ実行カタログのユーティリティ名列と実行ログを照合する理由が共通指定保守です。A: 共通指定で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由は共通指定証跡です。B: 共通指定が正答です。ジョブ単位の既定値と差分を確認することに合うため、採否を決める説明軸は共通指定読取です。C: 共通指定で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は共通指定判断です。D: 共通指定で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は共通指定定義です。初出語共通指定とは、技術項目名 OPTIONS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は共通指定判断です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 更新並行方式を性能維持で確認します。Db2の作業記録に更新並行方式保守の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は表スペースカタログのTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SHRLEVEL CHANGE <span class="kb-ok">✅ 正解</span></li><li>B. FLASHCOPY</li><li>C. CHECK DATA</li><li>D. RUNSTATS</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点更新並行方式は、ユーティリティ中も更新を許す方式を選ぶことを目的に扱い、確認項目は更新並行方式棚卸です。背景更新並行方式として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は更新並行方式観点です。更新並行方式の仕組みは、表スペースカタログのTYPE列と実行ログを照合する理由が更新並行方式証跡です。A: 更新並行方式が正答です。並行更新とログ適用の影響を確認することに合うため、採否を決める説明軸は更新並行方式定義です。B: 更新並行方式で見るストレージコピーは代替にならず、今回の比較対象から外す理由は更新並行方式根拠です。C: 更新並行方式で見る参照整合性検査は代替にならず、今回の比較対象から外す理由は更新並行方式列確認です。D: 更新並行方式で見る統計収集は代替にならず、今回の比較対象から外す理由は更新並行方式復旧です。初出語更新並行方式とは、技術項目名 SHRLEVEL CHANGE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は更新並行方式列確認です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 高速コピーを性能維持で確認します。Db2の作業記録にストレージコピーの根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はコピー履歴カタログのDSVOLSER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. FLASHCOPY <span class="kb-ok">✅ 正解</span></li><li>C. REPAIR SET</li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点高速コピーは、ストレージ機能で高速にコピーを作成することを目的に扱い、確認項目は高速コピー観点です。背景高速コピーとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は高速コピー証跡です。高速コピーの仕組みは、コピー履歴カタログのDSVOLSER列と実行ログを照合する理由が高速コピー読取です。A: 高速コピーで見る索引パート状態表は代替にならず、今回の比較対象から外す理由は高速コピー根拠です。B: 高速コピーが正答です。バックアウト情報と回復入力を確認することに合うため、採否を決める説明軸は高速コピー列確認です。C: 高速コピーで見る制限状態の補修は代替にならず、今回の比較対象から外す理由は高速コピー復旧です。D: 高速コピーで見る表スペース再編成は代替にならず、今回の比較対象から外す理由は高速コピー保守です。初出語高速コピーとは、技術項目名 FLASHCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義は高速コピー復旧です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー履歴を性能維持で確認します。Db2の作業記録にコピー履歴表の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. COPYDDN</li><li>C. SYSIBM.SYSCOPY <span class="kb-ok">✅ 正解</span></li><li>D. QUIESCE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点コピー履歴は、コピーや回復に必要な履歴を保持することを目的に扱い、確認項目はコピー履歴証跡です。背景コピー履歴として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー履歴読取です。コピー履歴の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー履歴判断です。A: コピー履歴で見る統計収集は代替にならず、今回の比較対象から外す理由はコピー履歴列確認です。B: コピー履歴で見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由はコピー履歴復旧です。C: コピー履歴が正答です。データセット名と回復可能性を確認することに合うため、採否を決める説明軸はコピー履歴保守です。D: コピー履歴で見る静止点取得は代替にならず、今回の比較対象から外す理由はコピー履歴棚卸です。初出語コピー履歴とは、技術項目名 SYSIBM.SYSCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー履歴保守です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース状態を性能維持で確認します。Db2の作業記録に表スペース状態表の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE</li><li>B. SYSIBM.SYSINDEXPART</li><li>C. OPTIONS</li><li>D. SYSIBM.SYSTABLESPACE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点表スペース状態は、表スペースの定義や状態を確認することを目的に扱い、確認項目は表スペース状態読取です。背景表スペース状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース状態判断です。表スペース状態の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が表スペース状態定義です。A: 表スペース状態で見る表スペース回復は代替にならず、今回の比較対象から外す理由は表スペース状態復旧です。B: 表スペース状態で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は表スペース状態保守です。C: 表スペース状態で見る実行共通指定は代替にならず、今回の比較対象から外す理由は表スペース状態棚卸です。D: 表スペース状態が正答です。制限状態や保守対象を確認することに合うため、採否を決める説明軸は表スペース状態観点です。初出語表スペース状態とは、技術項目名 SYSIBM.SYSTABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース状態棚卸です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 索引パート状態を性能維持で確認します。Db2の作業記録に索引パート状態表の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時は索引パートカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART <span class="kb-ok">✅ 正解</span></li><li>B. CHECK DATA</li><li>C. COPY TABLESPACE</li><li>D. DISPLAY DATABASE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点索引パート状態は、索引パートの状態を確認することを目的に扱い、確認項目は索引パート状態判断です。背景索引パート状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は索引パート状態定義です。索引パート状態の仕組みは、索引パートカタログの状態列と実行ログを照合する理由が索引パート状態根拠です。A: 索引パート状態が正答です。索引再構築の要否を判断することに合うため、採否を決める説明軸は索引パート状態保守です。B: 索引パート状態で見る参照整合性検査は代替にならず、今回の比較対象から外す理由は索引パート状態棚卸です。C: 索引パート状態で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由は索引パート状態観点です。D: 索引パート状態で見るデータベース状態表示は代替にならず、今回の比較対象から外す理由は索引パート状態証跡です。初出語索引パート状態とは、技術項目名 SYSIBM.SYSINDEXPART で表すDb2ユーティリティ、指定、または記録名であり、用語定義は索引パート状態観点です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー作成を監査証跡で確認します。Db2の作業記録にイメージコピー作成の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. COPY TABLESPACE <span class="kb-ok">✅ 正解</span></li><li>C. LOAD REPLACE</li><li>D. MERGECOPY</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点コピー作成は、回復に使うフルまたは増分コピーを登録することを目的に扱い、確認項目はコピー作成保守です。背景コピー作成として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー作成棚卸です。コピー作成の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー作成観点です。A: コピー作成で見る索引パート状態表は代替にならず、今回の比較対象から外す理由はコピー作成判断です。B: コピー作成が正答です。コピー登録とデータセット存在を照合することに合うため、採否を決める説明軸はコピー作成定義です。C: コピー作成で見る置換ロードは代替にならず、今回の比較対象から外す理由はコピー作成根拠です。D: コピー作成で見る増分コピー統合は代替にならず、今回の比較対象から外す理由はコピー作成列確認です。初出語コピー作成とは、技術項目名 COPY TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー作成根拠です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース回復を監査証跡で確認します。Db2の作業記録に表スペース回復の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はコピー履歴カタログのSTART_ログ位置列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. MODIFY RECOVERY</li><li>C. RECOVER TABLESPACE <span class="kb-ok">✅ 正解</span></li><li>D. RECOVERYDDN</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点表スペース回復は、イメージコピーとログを使って表スペースを戻することを目的に扱い、確認項目は表スペース回復棚卸です。背景表スペース回復として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース回復観点です。表スペース回復の仕組みは、コピー履歴カタログの開始ログ位置列と実行ログを照合する理由が表スペース回復証跡です。A: 表スペース回復で見る統計収集は代替にならず、今回の比較対象から外す理由は表スペース回復定義です。B: 表スペース回復で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由は表スペース回復根拠です。C: 表スペース回復が正答です。回復点とコピー履歴を確認することに合うため、採否を決める説明軸は表スペース回復列確認です。D: 表スペース回復で見る回復用データ定義名は代替にならず、今回の比較対象から外す理由は表スペース回復復旧です。初出語表スペース回復とは、技術項目名 RECOVER TABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース回復列確認です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 置換ロードを監査証跡で確認します。Db2の作業記録に置換ロードの根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は表スペースカタログのロード_STATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE</li><li>B. LISTDEF</li><li>C. DISPLAY THREAD</li><li>D. LOAD REPLACE <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点置換ロードは、既存データを置き換えて入力データをロードすることを目的に扱い、確認項目は置換ロード観点です。背景置換ロードとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は置換ロード証跡です。置換ロードの仕組みは、表スペースカタログのロード状態列と実行ログを照合する理由が置換ロード読取です。A: 置換ロードで見る表スペース回復は代替にならず、今回の比較対象から外す理由は置換ロード根拠です。B: 置換ロードで見る対象リスト定義は代替にならず、今回の比較対象から外す理由は置換ロード列確認です。C: 置換ロードで見るスレッド状態表示は代替にならず、今回の比較対象から外す理由は置換ロード復旧です。D: 置換ロードが正答です。ロード後の制限状態と統計収集を確認することに合うため、採否を決める説明軸は置換ロード保守です。初出語置換ロードとは、技術項目名 LOAD REPLACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は置換ロード復旧です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 状態補修を監査証跡で確認します。Db2の作業記録に制限状態の補修の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. REORG TABLESPACE</li><li>C. REPAIR SET <span class="kb-ok">✅ 正解</span></li><li>D. COPY TABLESPACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点状態補修は、カタログ状態やページ情報を補修するために使うことを目的に扱い、確認項目は状態補修復旧です。背景状態補修として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は状態補修保守です。状態補修の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が状態補修棚卸です。A: 状態補修で見る統計収集は代替にならず、今回の比較対象から外す理由は状態補修読取です。B: 状態補修で見る表スペース再編成は代替にならず、今回の比較対象から外す理由は状態補修判断です。C: 状態補修が正答です。補修対象とメッセージを厳密に限定することに合うため、採否を決める説明軸は状態補修定義です。D: 状態補修で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由は状態補修根拠です。初出語状態補修とは、技術項目名 REPAIR SET で表すDb2ユーティリティ、指定、または記録名であり、用語定義は状態補修定義です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 共通指定を監査証跡で確認します。Db2の作業記録に実行共通指定の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はユーティリティ実行カタログのUTILITY列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. DSNUTILB</li><li>B. SYSIBM.SYSTABLESPACE</li><li>C. OPTIONS <span class="kb-ok">✅ 正解</span></li><li>D. LOAD REPLACE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点共通指定は、対象リストやひな形のライブラリなどを上書きすることを目的に扱い、確認項目は共通指定証跡です。背景共通指定として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は共通指定読取です。共通指定の仕組みは、ユーティリティ実行カタログのユーティリティ名列と実行ログを照合する理由が共通指定判断です。A: 共通指定で見るユーティリティ制御プログラムは代替にならず、今回の比較対象から外す理由は共通指定列確認です。B: 共通指定で見る表スペース状態表は代替にならず、今回の比較対象から外す理由は共通指定復旧です。C: 共通指定が正答です。ジョブ単位の既定値と差分を確認することに合うため、採否を決める説明軸は共通指定保守です。D: 共通指定で見る置換ロードは代替にならず、今回の比較対象から外す理由は共通指定棚卸です。初出語共通指定とは、技術項目名 OPTIONS で表すDb2ユーティリティ、指定、または記録名であり、用語定義は共通指定保守です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 更新並行方式を監査証跡で確認します。Db2の作業記録に更新並行方式保守の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は表スペースカタログのTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSINDEXPART</li><li>B. SHRLEVEL CHANGE <span class="kb-ok">✅ 正解</span></li><li>C. REPAIR SET</li><li>D. REORG TABLESPACE</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点更新並行方式は、ユーティリティ中も更新を許す方式を選ぶことを目的に扱い、確認項目は更新並行方式定義です。背景更新並行方式として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は更新並行方式根拠です。更新並行方式の仕組みは、表スペースカタログのTYPE列と実行ログを照合する理由が更新並行方式列確認です。A: 更新並行方式で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は更新並行方式棚卸です。B: 更新並行方式が正答です。並行更新とログ適用の影響を確認することに合うため、採否を決める説明軸は更新並行方式観点です。C: 更新並行方式で見る制限状態の補修は代替にならず、今回の比較対象から外す理由は更新並行方式証跡です。D: 更新並行方式で見る表スペース再編成は代替にならず、今回の比較対象から外す理由は更新並行方式読取です。初出語更新並行方式とは、技術項目名 SHRLEVEL CHANGE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は更新並行方式証跡です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 高速コピーを監査証跡で確認します。Db2の作業記録にストレージコピーの根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はコピー履歴カタログのDSVOLSER列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RUNSTATS</li><li>B. COPYDDN</li><li>C. FLASHCOPY <span class="kb-ok">✅ 正解</span></li><li>D. QUIESCE</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 論点高速コピーは、ストレージ機能で高速にコピーを作成することを目的に扱い、確認項目は高速コピー根拠です。背景高速コピーとして、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は高速コピー列確認です。高速コピーの仕組みは、コピー履歴カタログのDSVOLSER列と実行ログを照合する理由が高速コピー復旧です。A: 高速コピーで見る統計収集は代替にならず、今回の比較対象から外す理由は高速コピー観点です。B: 高速コピーで見るコピー用データ定義名は代替にならず、今回の比較対象から外す理由は高速コピー証跡です。C: 高速コピーが正答です。バックアウト情報と回復入力を確認することに合うため、採否を決める説明軸は高速コピー読取です。D: 高速コピーで見る静止点取得は代替にならず、今回の比較対象から外す理由は高速コピー判断です。初出語高速コピーとは、技術項目名 FLASHCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義は高速コピー読取です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> コピー履歴を監査証跡で確認します。Db2の作業記録にコピー履歴表の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はコピー履歴カタログのICTYPE列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. RECOVER TABLESPACE</li><li>B. SYSIBM.SYSINDEXPART</li><li>C. OPTIONS</li><li>D. SYSIBM.SYSCOPY <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点コピー履歴は、コピーや回復に必要な履歴を保持することを目的に扱い、確認項目はコピー履歴列確認です。背景コピー履歴として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名はコピー履歴復旧です。コピー履歴の仕組みは、コピー履歴カタログのコピー種別列と実行ログを照合する理由がコピー履歴保守です。A: コピー履歴で見る表スペース回復は代替にならず、今回の比較対象から外す理由はコピー履歴証跡です。B: コピー履歴で見る索引パート状態表は代替にならず、今回の比較対象から外す理由はコピー履歴読取です。C: コピー履歴で見る実行共通指定は代替にならず、今回の比較対象から外す理由はコピー履歴判断です。D: コピー履歴が正答です。データセット名と回復可能性を確認することに合うため、採否を決める説明軸はコピー履歴定義です。初出語コピー履歴とは、技術項目名 SYSIBM.SYSCOPY で表すDb2ユーティリティ、指定、または記録名であり、用語定義はコピー履歴判断です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 表スペース状態を監査証跡で確認します。Db2の作業記録に表スペース状態表の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は表スペースカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. SYSIBM.SYSTABLESPACE <span class="kb-ok">✅ 正解</span></li><li>B. CHECK DATA</li><li>C. COPY TABLESPACE</li><li>D. DISPLAY DATABASE</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 論点表スペース状態は、表スペースの定義や状態を確認することを目的に扱い、確認項目は表スペース状態復旧です。背景表スペース状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は表スペース状態保守です。表スペース状態の仕組みは、表スペースカタログの状態列と実行ログを照合する理由が表スペース状態棚卸です。A: 表スペース状態が正答です。制限状態や保守対象を確認することに合うため、採否を決める説明軸は表スペース状態読取です。B: 表スペース状態で見る参照整合性検査は代替にならず、今回の比較対象から外す理由は表スペース状態判断です。C: 表スペース状態で見るイメージコピー作成は代替にならず、今回の比較対象から外す理由は表スペース状態定義です。D: 表スペース状態で見るデータベース状態表示は代替にならず、今回の比較対象から外す理由は表スペース状態根拠です。初出語表スペース状態とは、技術項目名 SYSIBM.SYSTABLESPACE で表すDb2ユーティリティ、指定、または記録名であり、用語定義は表スペース状態定義です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-q"><p><strong>問題.</strong> 索引パート状態を監査証跡で確認します。Db2の作業記録に索引パート状態表の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時は索引パートカタログのSTATUS列も照合対象にします。この条件で、どの選択肢が適切ですか。</p><ul class="kb-choices"><li>A. MODIFY RECOVERY</li><li>B. SYSIBM.SYSINDEXPART <span class="kb-ok">✅ 正解</span></li><li>C. REBUILD INDEX</li><li>D. UNLOAD</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 論点索引パート状態は、索引パートの状態を確認することを目的に扱い、確認項目は索引パート状態保守です。背景索引パート状態として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は索引パート状態棚卸です。索引パート状態の仕組みは、索引パートカタログの状態列と実行ログを照合する理由が索引パート状態観点です。A: 索引パート状態で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由は索引パート状態判断です。B: 索引パート状態が正答です。索引再構築の要否を判断することに合うため、採否を決める説明軸は索引パート状態定義です。C: 索引パート状態で見る索引再構築は代替にならず、今回の比較対象から外す理由は索引パート状態根拠です。D: 索引パート状態で見るデータ抽出は代替にならず、今回の比較対象から外す理由は索引パート状態列確認です。初出語索引パート状態とは、技術項目名 SYSIBM.SYSINDEXPART で表すDb2ユーティリティ、指定、または記録名であり、用語定義は索引パート状態根拠です。</p><p class="kb-src"><strong>出典:</strong> Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div></details><details class="kb-block"><summary>検証手順（138件）</summary><div class="kb-p"><p class="kb-pname"><strong>RACF ACM administrative authority</strong></p><p>検証目的: 変更検査のDb2について、RACF ACM administrative authority profileは、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Dbに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010080の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はDb2 Commandの表示結果です。FIND欄にRACF ACM administrを指定し、OSKB010080の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND RACF ACM administr
CASE OSKB010080
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM RACF ACM administr
CASE OSKB010080
SOURCE Db2 for z/OS
RACF ACM administrとOSKB010080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010080を同じ出力で読み、変更検査のDb2の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB010080
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB010080
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB010080
DSNV401IとOSKB010080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の RACF ACM administr と OSKB010080 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB010080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>external to native procedure migra</strong></p><p>検証目的: 区切追跡の実行・移行について、external to native procedure migrationは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、区切追跡の実行・移行の確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にexternal to nativeを指定し、OSKB020050の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND external to native
CASE OSKB020050
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM external to native
CASE OSKB020050
SOURCE Db2 for z/OS
external to nativeとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020050を同じ出力で読み、区切追跡の実行・移行の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020050
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020050
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020050
DSNV401IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の external to native と OSKB020050 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>IFCID reference in problem determi</strong></p><p>検証目的: 変更追跡の診断資料について、IFCID reference in problem determinationは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、変更追跡の診断資料の確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にIFCID reference inを指定し、OSKB020060の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND IFCID reference in
CASE OSKB020060
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM IFCID reference in
CASE OSKB020060
SOURCE Db2 for z/OS
IFCID reference inとOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020060を同じ出力で読み、変更追跡の診断資料の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020060
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020060
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020060
DSNV401IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の IFCID reference in と OSKB020060 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY DATABASE SPACENAM（Db2コマンド指</strong></p><p>検証目的: 優先記録の運用コマンドについて、DISPLAY DATABASE SPACENAM は、Db2運用コマンドのキーワードまたは指定値です。操作対象、表示範囲、影響範囲を確認し、実行後のメッセージや表示項目と対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020132の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、優先記録の運用コマンドの確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にDISPLAY DATABASE Sを指定し、OSKB020132の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND DISPLAY DATABASE S
CASE OSKB020132
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM DISPLAY DATABASE S
CASE OSKB020132
SOURCE Db2 for z/OS
DISPLAY DATABASE SとOSKB020132が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020132を同じ出力で読み、優先記録の運用コマンドの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020132
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020132
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020132
DSNV401IとOSKB020132が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の DISPLAY DATABASE S と OSKB020132 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020132 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE MAXPARTITIONS（DD</strong></p><p>検証目的: 終端分離のオプションについて、CREATE TABLESPACE MAXPARTITIONS は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020145の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、終端分離のオプションの確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TABLESPACE を指定し、OSKB020145の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TABLESPACE 
CASE OSKB020145
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TABLESPACE 
CASE OSKB020145
SOURCE Db2 for z/OS
CREATE TABLESPACE とOSKB020145が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020145を同じ出力で読み、終端分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020145
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020145
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020145
DSNV401IとOSKB020145が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TABLESPACE  と OSKB020145 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020145 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE STOGROUP DATACLAS ・ STORCLAS ・</strong></p><p>検証目的: 値域分離のオプションについて、CREATE STOGROUP DATACLAS/STORCLAS/MGMTCLAS は、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020156の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、値域分離のオプションの確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE STOGROUP DAを指定し、OSKB020156の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE STOGROUP DA
CASE OSKB020156
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE STOGROUP DA
CASE OSKB020156
SOURCE Db2 for z/OS
CREATE STOGROUP DAとOSKB020156が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020156を同じ出力で読み、値域分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020156
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020156
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020156
DSNV401IとOSKB020156が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE STOGROUP DA と OSKB020156 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020156 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TRUSTED CONTEXT attributes（</strong></p><p>検証目的: 復旧分離のオプションについて、CREATE TRUSTED CONTEXT attributesは、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020158の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、復旧分離のオプションの確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TRUSTED CONを指定し、OSKB020158の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TRUSTED CON
CASE OSKB020158
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TRUSTED CON
CASE OSKB020158
SOURCE Db2 for z/OS
CREATE TRUSTED CONとOSKB020158が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020158を同じ出力で読み、復旧分離のオプションの根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020158
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020158
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020158
DSNV401IとOSKB020158が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TRUSTED CON と OSKB020158 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020158 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TRIGGER timing・event（DDL 句・属</strong></p><p>検証目的: 監査分離の・について、CREATE TRIGGER timing/eventは、SQL または DDL で Db2オブジェクトの定義や振る舞いを変える句・属性候補です。定義対象、運用上の影響、隣接する句に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020159の検証用出力を記録できる。</p><p>セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===&gt; に -DISPLAY THREAD を入力し、監査分離の・の確認表示へ進みます。
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
現在の画面はDb2 Commandの表示結果です。FIND欄にCREATE TRIGGER timを指定し、OSKB020159の対象行を見つけます。
［操作（入力）］
(Db2 Command Result)
COMMAND INPUT ===&gt; FIND CREATE TRIGGER tim
CASE OSKB020159
→ Enter を押す
［画面・出力］
(Db2 Command Result)
ITEM CREATE TRIGGER tim
CASE OSKB020159
SOURCE Db2 for z/OS
CREATE TRIGGER timとOSKB020159が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020159を同じ出力で読み、監査分離の・の根拠を記録します。
［操作（入力）］
(Db2 Command Detail)
COMMAND INPUT ===&gt; -DISPLAY THREAD
CASE OSKB020159
→ Enter を押す
［画面・出力］
DSN COMMAND RESPONSE OSKB020159
-DISPLAY THREAD
DSNV401I - DISPLAY REPORT FOLLOWS -
DSNV402I - ACTIVE THREADS -
NAME     ST A REQ ID OSKB020159
DSNV401IとOSKB020159が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; -DISPLAY THREAD が画面・出力に表示されること
② ステップ2 の CREATE TRIGGER tim と OSKB020159 が画面・出力に表示されること
③ ステップ3 の DSNV401I と OSKB020159 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNTIJUM 確認手順</strong></p><p>検証目的: DSNTIJUM と DSNTIJUL の役割を机上確認します。DSNHMCIDの作成とDDF関連BSDS更新を、DSNTIJUZやDSNTIJUAとは別のジョブとして読み分けます。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、prefix.SDSNEXIT、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではDSNZPARM、DSNHDECP、DSNHMCID、BSDS通信情報の変更は変更管理承認を得てから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブとSYSLOGの机上出力を確認します。ジョブ投入とコマンド出力は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のコマンドまたはジョブ投入行を入力します。この操作で、対象ジョブや表示コマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUM)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUM)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUM)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ名、マクロ名、生成資材名、またはBSDS値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12362 DSNTIJUM DSNHMCID BUILT CCSID=1208
JOB12363 DSNTIJUL DSNJU003 DDF LOCATION=DB2A PORT=446
NORMAL COMPLETION
DSNHMCID BUILT CCSID=1208 が表示されていれば、机上例では対象の導入値を確認できます。NORMAL COMPLETION も同じ画面で確認し、エラー応答ではないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として、同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12362 DSNTIJUM DSNHMCID BUILT CCSID=1208
JOB12363 DSNTIJUL DSNJU003 DDF LOCATION=DB2A PORT=446
ISSUER=USER1
DSNHMCID BUILT CCSID=1208 と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUM)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNHMCID BUILT CCSID=1208 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNTIJIC 確認手順</strong></p><p>検証目的: DSNTIJIC による Db2 catalog と directory のイメージコピーを机上確認します。コピー対象表スペースと終了コードを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、SDSF、カタログ/ディレクトリのコピー先、BSDS、active log定義の机上確認ができる前提です。実機では停止要否、利用者影響、変更承認、バックアウト手順を確認してから実施します。</p><p>セッション環境: DB2I COMMANDS と SDSF で、導入後検証・保守ジョブとサブシステム資材の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のジョブ投入または表示コマンドを入力します。対象のジョブ名やコマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ終了、生成資材、レベル値、または更新された値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12370 DSNTIJIC RC=0000
COPY UTILITY COMPLETED CATALOG=DSNDB06 DIRECTORY=DSNDB01 UNIT=TAPE
NORMAL COMPLETION
DSNTIJIC RC=0000 が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12370 DSNTIJIC RC=0000
COPY UTILITY COMPLETED CATALOG=DSNDB06 DIRECTORY=DSNDB01 UNIT=TAPE
ISSUER=USER1
DSNTIJIC RC=0000 と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNTIJIC RC=0000 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNTIJRT 確認手順</strong></p><p>検証目的: DSNTIJRT と DSNTIJRV の机上結果を確認します。提供ルーチンの導入・構成と、その後の検証レポートを分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、SDSF、カタログ/ディレクトリのコピー先、BSDS、active log定義の机上確認ができる前提です。実機では停止要否、利用者影響、変更承認、バックアウト手順を確認してから実施します。</p><p>セッション環境: DB2I COMMANDS と SDSF で、導入後検証・保守ジョブとサブシステム資材の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のジョブ投入または表示コマンドを入力します。対象のジョブ名やコマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ終了、生成資材、レベル値、または更新された値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12371 DSNTIJRT DSNTRIN COMPLETED ROUTINES=INSTALLED
JOB12372 DSNTIJRV VALIDATION REPORT SUCCESS=42 WARNING=0 FAILURE=0
NORMAL COMPLETION
DSNTRIN COMPLETED が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12371 DSNTIJRT DSNTRIN COMPLETED ROUTINES=INSTALLED
JOB12372 DSNTIJRV VALIDATION REPORT SUCCESS=42 WARNING=0 FAILURE=0
ISSUER=USER1
DSNTRIN COMPLETED と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNTRIN COMPLETED が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages</p></div><div class="kb-p"><p class="kb-pname"><strong>移行検証 確認手順</strong></p><p>検証目的: 移行検証で使う DISPLAY GROUP の机上出力を確認します。code level、catalog level、function level が期待値かを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、SDSF、カタログ/ディレクトリのコピー先、BSDS、active log定義の机上確認ができる前提です。実機では停止要否、利用者影響、変更承認、バックアウト手順を確認してから実施します。</p><p>セッション環境: DB2I COMMANDS と SDSF で、導入後検証・保守ジョブとサブシステム資材の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のジョブ投入または表示コマンドを入力します。対象のジョブ名やコマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY GROUP DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY GROUP DETAIL
-DISPLAY GROUP DETAIL が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ終了、生成資材、レベル値、または更新された値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSN7100I DISPLAY GROUP DETAIL MEMBER=DB2A DB2 LVL=V13R1M500
CATALOG LEVEL=V13R1M500 CURRENT FUNCTION LEVEL=V13R1M500 HIGHEST ACTIVATED FUNCTION LEVEL=V13R1M500
NORMAL COMPLETION
CURRENT FUNCTION LEVEL=V13R1M500 が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSN7100I DISPLAY GROUP DETAIL MEMBER=DB2A DB2 LVL=V13R1M500
CATALOG LEVEL=V13R1M500 CURRENT FUNCTION LEVEL=V13R1M500 HIGHEST ACTIVATED FUNCTION LEVEL=V13R1M500
ISSUER=USER1
CURRENT FUNCTION LEVEL=V13R1M500 と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY GROUP DETAIL が操作（入力）に記載されていること
② ステップ2 の CURRENT FUNCTION LEVEL=V13R1M500 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages</p></div><div class="kb-p"><p class="kb-pname"><strong>active log初期化 確認手順</strong></p><p>検証目的: active log初期化とBSDS二重化の机上結果を確認します。DSNJLOGFの事前整形とRECOVER BSDSの結果を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、SDSF、カタログ/ディレクトリのコピー先、BSDS、active log定義の机上確認ができる前提です。実機では停止要否、利用者影響、変更承認、バックアウト手順を確認してから実施します。</p><p>セッション環境: DB2I COMMANDS と SDSF で、導入後検証・保守ジョブとサブシステム資材の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のジョブ投入または表示コマンドを入力します。対象のジョブ名やコマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJL1)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJL1)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJL1)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ終了、生成資材、レベル値、または更新された値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12373 DSNJLOGF PREFORMAT ACTIVELOG=DSNDB2.ACTLOG1 RC=0000
RECOVER BSDS COMPLETED TWOBSDS=YES BSDS2=DSNDB2.BSDS2
NORMAL COMPLETION
DSNJLOGF PREFORMAT が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12373 DSNJLOGF PREFORMAT ACTIVELOG=DSNDB2.ACTLOG1 RC=0000
RECOVER BSDS COMPLETED TWOBSDS=YES BSDS2=DSNDB2.BSDS2
ISSUER=USER1
DSNJLOGF PREFORMAT と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJL1)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNJLOGF PREFORMAT が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages</p></div><div class="kb-p"><p class="kb-pname"><strong>DDF情報のBSDS更新 確認手順</strong></p><p>検証目的: DDF情報のBSDS更新と、DSNZPxxx/DSNHDECPの資材名を机上確認します。分散接続値と起動・アプリケーション既定値の資材を分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、SDSF、カタログ/ディレクトリのコピー先、BSDS、active log定義の机上確認ができる前提です。実機では停止要否、利用者影響、変更承認、バックアウト手順を確認してから実施します。</p><p>セッション環境: DB2I COMMANDS と SDSF で、導入後検証・保守ジョブとサブシステム資材の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のジョブ投入または表示コマンドを入力します。対象のジョブ名やコマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ終了、生成資材、レベル値、または更新された値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12374 DSNTIJUL DSNJU003 DDF LOCATION=DB2A PORT=446 RESPORT=5001 IPNAME=DB2AIP
PARAMETER MODULE=DSNZPDB2 APPL DEFAULTS=DSNHDECP
NORMAL COMPLETION
DDF LOCATION=DB2A が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12374 DSNTIJUL DSNJU003 DDF LOCATION=DB2A PORT=446 RESPORT=5001 IPNAME=DB2AIP
PARAMETER MODULE=DSNZPDB2 APPL DEFAULTS=DSNHDECP
ISSUER=USER1
DDF LOCATION=DB2A と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27; が操作（入力）に記載されていること
② ステップ2 の DDF LOCATION=DB2A が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages</p></div><div class="kb-p"><p class="kb-pname"><strong>DELETE 確認手順</strong></p><p>検証目的: 更新SQLのDELETEとMERGEを机上例で確認します。削除対象条件と差分反映の照合条件を混同しないよう、出力上の文とSQLCODEを見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2SQL.JCL を編集でき、Db2サブシステム DB2A でDSNTEP2またはアプリケーションSQLの机上確認を行う前提です。実機では更新SQLは検証用表に限定し、COMMIT前に対象件数を確認します。</p><p>セッション環境: ISPF EditでSQL実行JCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNTEP2出力またはSQLメッセージを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNTEP2でSQLを実行するJCLを入力します。この操作ではJCL本文だけを作成し、保存は次のステップで行います。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //SQ01 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 DELETE FROM APP1.EMP WHERE STATUS = &#x27;RETIRED&#x27;;
000012 MERGE INTO APP1.CUSTOMER T USING APP1.CUSTOMER_STAGE S ON T.CUSTNO = S.CUSTNO WHEN MATCHED THEN UPDATE SET NAME = S.NAME WHEN NOT MATCHED THEN INSERT (CUSTNO, NAME) VALUES (S.CUSTNO, S.NAME);
000013 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ01 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 DELETE FROM APP1.EMP WHERE STATUS = &#x27;RETIRED&#x27;;
000012 MERGE INTO APP1.CUSTOMER T USING APP1.CUSTOMER_STAGE S ON T.CUSTNO = S.CUSTNO WHEN MATCHED THEN UPDATE SET NAME = S.NAME WHEN NOT MATCHED THEN INSERT (CUSTNO, NAME) VALUES (S.CUSTNO, S.NAME);
000013 /*
000001 から始まるJCL行が表示されていれば、SQL実行用JCLが本文入力行に入っています。SYSIN内のSQL文が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文を保存します。SQL文は変更せず、保存完了メッセージを確認します。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ01 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 DELETE FROM APP1.EMP WHERE STATUS = &#x27;RETIRED&#x27;;
000012 MERGE INTO APP1.CUSTOMER T USING APP1.CUSTOMER_STAGE S ON T.CUSTNO = S.CUSTNO WHEN MATCHED THEN UPDATE SET NAME = S.NAME WHEN NOT MATCHED THEN INSERT (CUSTNO, NAME) VALUES (S.CUSTNO, S.NAME);
000013 /*
*** Member SQ01 saved
Member SQ01 saved が表示されていれば、JCLとSQL文が保存されています。画面にDSNTEP2の実行指定が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2SQL.JCL(SQ01)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2SQL.JCL(SQ01)&#x27;
→ Enter を押す
［画面・出力］
JOB SQ01 SUBMITTED
IKJ56250I JOB SQ01(JOB01234) SUBMITTED
JOB SQ01 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した SQ01 のジョブログを開きます。この操作でSQL文、SQLCODE、DSNTEP2の完了状態を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    SQ01     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DELETE FROM APP1.EMP WHERE STATUS = &#x27;RETIRED&#x27;
SQLCODE=0 ROWS AFFECTED=3
MERGE INTO APP1.CUSTOMER
SQLCODE=0 ROWS MERGED=12
DSNTEP2 COMPLETED
MERGE INTO APP1.CUSTOMER が表示されていれば、机上例では検証対象のSQL動作を確認できています。DSNTEP2 COMPLETED も同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB SQ01 SUBMITTED が画面・出力に表示されること
② ステップ4 の MERGE INTO APP1.CUSTOMER が画面・出力に表示されること
③ ステップ4 の DSNTEP2 COMPLETED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>view update 確認手順</strong></p><p>検証目的: ビュー更新とINSTEAD OF triggerの関係を確認します。複雑なビューに対する更新では、基表への反映方法を明示する必要があることを机上例で見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2SQL.JCL を編集でき、Db2サブシステム DB2A でDSNTEP2またはアプリケーションSQLの机上確認を行う前提です。実機では更新SQLは検証用表に限定し、COMMIT前に対象件数を確認します。</p><p>セッション環境: ISPF EditでSQL実行JCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNTEP2出力またはSQLメッセージを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNTEP2でSQLを実行するJCLを入力します。この操作ではJCL本文だけを作成し、保存は次のステップで行います。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //SQ02 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 UPDATE APP1.V_EMP SET DEPTNO = &#x27;D02&#x27; WHERE EMPNO = &#x27;000010&#x27;;
000012 CREATE TRIGGER APP1.V_EMP_IOU INSTEAD OF UPDATE ON APP1.V_EMP REFERENCING NEW AS N OLD AS O FOR EACH ROW MODE DB2SQL UPDATE APP1.EMP SET DEPTNO = N.DEPTNO WHERE EMPNO = O.EMPNO;
000013 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ02 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 UPDATE APP1.V_EMP SET DEPTNO = &#x27;D02&#x27; WHERE EMPNO = &#x27;000010&#x27;;
000012 CREATE TRIGGER APP1.V_EMP_IOU INSTEAD OF UPDATE ON APP1.V_EMP REFERENCING NEW AS N OLD AS O FOR EACH ROW MODE DB2SQL UPDATE APP1.EMP SET DEPTNO = N.DEPTNO WHERE EMPNO = O.EMPNO;
000013 /*
000001 から始まるJCL行が表示されていれば、SQL実行用JCLが本文入力行に入っています。SYSIN内のSQL文が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文を保存します。SQL文は変更せず、保存完了メッセージを確認します。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ02 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 UPDATE APP1.V_EMP SET DEPTNO = &#x27;D02&#x27; WHERE EMPNO = &#x27;000010&#x27;;
000012 CREATE TRIGGER APP1.V_EMP_IOU INSTEAD OF UPDATE ON APP1.V_EMP REFERENCING NEW AS N OLD AS O FOR EACH ROW MODE DB2SQL UPDATE APP1.EMP SET DEPTNO = N.DEPTNO WHERE EMPNO = O.EMPNO;
000013 /*
*** Member SQ02 saved
Member SQ02 saved が表示されていれば、JCLとSQL文が保存されています。画面にDSNTEP2の実行指定が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2SQL.JCL(SQ02)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2SQL.JCL(SQ02)&#x27;
→ Enter を押す
［画面・出力］
JOB SQ02 SUBMITTED
IKJ56250I JOB SQ02(JOB01234) SUBMITTED
JOB SQ02 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した SQ02 のジョブログを開きます。この操作でSQL文、SQLCODE、DSNTEP2の完了状態を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    SQ02     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
UPDATE APP1.V_EMP SET DEPTNO=&#x27;D02&#x27;
SQLCODE=0 VIEW UPDATE ACCEPTED
CREATE TRIGGER APP1.V_EMP_IOU
SQLCODE=0 TRIGGER CREATED
DSNTEP2 COMPLETED
CREATE TRIGGER APP1.V_EMP_IOU が表示されていれば、机上例では検証対象のSQL動作を確認できています。DSNTEP2 COMPLETED も同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB SQ02 SUBMITTED が画面・出力に表示されること
② ステップ4 の CREATE TRIGGER APP1.V_EMP_IOU が画面・出力に表示されること
③ ステップ4 の DSNTEP2 COMPLETED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>COMMIT 確認手順</strong></p><p>検証目的: 作業単位の確定と取消しを確認します。更新件数とSQLCODEを見て、確定する場面と戻す場面を切り分けます。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2SQL.JCL を編集でき、Db2サブシステム DB2A でDSNTEP2またはアプリケーションSQLの机上確認を行う前提です。実機では更新SQLは検証用表に限定し、COMMIT前に対象件数を確認します。</p><p>セッション環境: ISPF EditでSQL実行JCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNTEP2出力またはSQLメッセージを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNTEP2でSQLを実行するJCLを入力します。この操作ではJCL本文だけを作成し、保存は次のステップで行います。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //SQ03 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 UPDATE APP1.EMP SET STATUS = &#x27;A&#x27; WHERE EMPNO = &#x27;000010&#x27;;
000012 COMMIT;
000013 UPDATE APP1.EMP SET STATUS = &#x27;X&#x27; WHERE EMPNO = &#x27;999999&#x27;;
000014 ROLLBACK;
000015 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ03 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 UPDATE APP1.EMP SET STATUS = &#x27;A&#x27; WHERE EMPNO = &#x27;000010&#x27;;
000012 COMMIT;
000013 UPDATE APP1.EMP SET STATUS = &#x27;X&#x27; WHERE EMPNO = &#x27;999999&#x27;;
000014 ROLLBACK;
000015 /*
000001 から始まるJCL行が表示されていれば、SQL実行用JCLが本文入力行に入っています。SYSIN内のSQL文が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文を保存します。SQL文は変更せず、保存完了メッセージを確認します。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ03 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 UPDATE APP1.EMP SET STATUS = &#x27;A&#x27; WHERE EMPNO = &#x27;000010&#x27;;
000012 COMMIT;
000013 UPDATE APP1.EMP SET STATUS = &#x27;X&#x27; WHERE EMPNO = &#x27;999999&#x27;;
000014 ROLLBACK;
000015 /*
*** Member SQ03 saved
Member SQ03 saved が表示されていれば、JCLとSQL文が保存されています。画面にDSNTEP2の実行指定が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2SQL.JCL(SQ03)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2SQL.JCL(SQ03)&#x27;
→ Enter を押す
［画面・出力］
JOB SQ03 SUBMITTED
IKJ56250I JOB SQ03(JOB01234) SUBMITTED
JOB SQ03 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した SQ03 のジョブログを開きます。この操作でSQL文、SQLCODE、DSNTEP2の完了状態を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    SQ03     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
UPDATE APP1.EMP SET STATUS=&#x27;A&#x27;
SQLCODE=0 ROWS AFFECTED=1
COMMIT
SQLCODE=0 UNIT OF WORK COMMITTED
ROLLBACK
SQLCODE=0 UNIT OF WORK ROLLED BACK
DSNTEP2 COMPLETED
UNIT OF WORK COMMITTED が表示されていれば、机上例では検証対象のSQL動作を確認できています。DSNTEP2 COMPLETED も同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB SQ03 SUBMITTED が画面・出力に表示されること
② ステップ4 の UNIT OF WORK COMMITTED が画面・出力に表示されること
③ ステップ4 の DSNTEP2 COMPLETED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>isolation level 確認手順</strong></p><p>検証目的: isolation levelが読み取り整合性と同時実行性に関わることを確認します。カーソル宣言や実行属性の指定が出力に反映される形で見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2SQL.JCL を編集でき、Db2サブシステム DB2A でDSNTEP2またはアプリケーションSQLの机上確認を行う前提です。実機では更新SQLは検証用表に限定し、COMMIT前に対象件数を確認します。</p><p>セッション環境: ISPF EditでSQL実行JCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNTEP2出力またはSQLメッセージを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNTEP2でSQLを実行するJCLを入力します。この操作ではJCL本文だけを作成し、保存は次のステップで行います。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //SQ04 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 DECLARE C1 CURSOR WITH ISOLATION CS FOR SELECT EMPNO, NAME FROM APP1.EMP WHERE DEPTNO = &#x27;D01&#x27;;
000012 OPEN C1;
000013 FETCH C1;
000014 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ04 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 DECLARE C1 CURSOR WITH ISOLATION CS FOR SELECT EMPNO, NAME FROM APP1.EMP WHERE DEPTNO = &#x27;D01&#x27;;
000012 OPEN C1;
000013 FETCH C1;
000014 /*
000001 から始まるJCL行が表示されていれば、SQL実行用JCLが本文入力行に入っています。SYSIN内のSQL文が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文を保存します。SQL文は変更せず、保存完了メッセージを確認します。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ04 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 DECLARE C1 CURSOR WITH ISOLATION CS FOR SELECT EMPNO, NAME FROM APP1.EMP WHERE DEPTNO = &#x27;D01&#x27;;
000012 OPEN C1;
000013 FETCH C1;
000014 /*
*** Member SQ04 saved
Member SQ04 saved が表示されていれば、JCLとSQL文が保存されています。画面にDSNTEP2の実行指定が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2SQL.JCL(SQ04)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2SQL.JCL(SQ04)&#x27;
→ Enter を押す
［画面・出力］
JOB SQ04 SUBMITTED
IKJ56250I JOB SQ04(JOB01234) SUBMITTED
JOB SQ04 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した SQ04 のジョブログを開きます。この操作でSQL文、SQLCODE、DSNTEP2の完了状態を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    SQ04     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DECLARE CURSOR C1 WITH ISOLATION CS
SQLCODE=0 CURSOR DECLARED
OPEN C1
SQLCODE=0
FETCH C1
SQLCODE=0 ROW RETURNED
DSNTEP2 COMPLETED
WITH ISOLATION CS が表示されていれば、机上例では検証対象のSQL動作を確認できています。DSNTEP2 COMPLETED も同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB SQ04 SUBMITTED が画面・出力に表示されること
② ステップ4 の WITH ISOLATION CS が画面・出力に表示されること
③ ステップ4 の DSNTEP2 COMPLETED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>dynamic PREPARE 確認手順</strong></p><p>検証目的: 動的SQLの準備とSQLCODEに基づく後続判断を確認します。実行前のPREPAREと実行後のエラー処理を別の確認点として扱います。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2SQL.JCL を編集でき、Db2サブシステム DB2A でDSNTEP2またはアプリケーションSQLの机上確認を行う前提です。実機では更新SQLは検証用表に限定し、COMMIT前に対象件数を確認します。</p><p>セッション環境: ISPF EditでSQL実行JCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNTEP2出力またはSQLメッセージを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNTEP2でSQLを実行するJCLを入力します。この操作ではJCL本文だけを作成し、保存は次のステップで行います。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //SQ05 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 PREPARE S1 FROM &#x27;SELECT NAME FROM APP1.EMP WHERE EMPNO = ?&#x27;;
000012 EXECUTE S1 USING &#x27;000010&#x27;;
000013 -- CHECK SQLCODE AND SQLSTATE AFTER EXECUTE
000014 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ05 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 PREPARE S1 FROM &#x27;SELECT NAME FROM APP1.EMP WHERE EMPNO = ?&#x27;;
000012 EXECUTE S1 USING &#x27;000010&#x27;;
000013 -- CHECK SQLCODE AND SQLSTATE AFTER EXECUTE
000014 /*
000001 から始まるJCL行が表示されていれば、SQL実行用JCLが本文入力行に入っています。SYSIN内のSQL文が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文を保存します。SQL文は変更せず、保存完了メッセージを確認します。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //SQ05 JOB (ACCT),&#x27;DB2SQL&#x27;,CLASS=A,MSGCLASS=X
000002 //SQL EXEC PGM=IKJEFT01
000003 //SYSTSPRT DD SYSOUT=*
000004 //SYSPRINT DD SYSOUT=*
000005 //SYSTSIN DD *
000006   DSN SYSTEM(DB2A)
000007   RUN PROGRAM(DSNTEP2) PLAN(DSNTEP13) LIB(&#x27;DB2A.RUNLIB.LOAD&#x27;)
000008   END
000009 /*
000010 //SYSIN DD *
000011 PREPARE S1 FROM &#x27;SELECT NAME FROM APP1.EMP WHERE EMPNO = ?&#x27;;
000012 EXECUTE S1 USING &#x27;000010&#x27;;
000013 -- CHECK SQLCODE AND SQLSTATE AFTER EXECUTE
000014 /*
*** Member SQ05 saved
Member SQ05 saved が表示されていれば、JCLとSQL文が保存されています。画面にDSNTEP2の実行指定が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2SQL.JCL(SQ05)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2SQL.JCL(SQ05)&#x27;
→ Enter を押す
［画面・出力］
JOB SQ05 SUBMITTED
IKJ56250I JOB SQ05(JOB01234) SUBMITTED
JOB SQ05 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した SQ05 のジョブログを開きます。この操作でSQL文、SQLCODE、DSNTEP2の完了状態を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    SQ05     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
PREPARE S1
SQLCODE=0 STATEMENT PREPARED
EXECUTE S1
SQLCODE=0 SQLSTATE=00000
ERROR HANDLING ACTION=CONTINUE
DSNTEP2 COMPLETED
STATEMENT PREPARED が表示されていれば、机上例では検証対象のSQL動作を確認できています。DSNTEP2 COMPLETED も同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB SQ05 SUBMITTED が画面・出力に表示されること
② ステップ4 の STATEMENT PREPARED が画面・出力に表示されること
③ ステップ4 の DSNTEP2 COMPLETED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>static SQL 確認手順</strong></p><p>検証目的: static SQL の準備工程を机上確認します。precompileでDBRMが作られ、BINDでpackageとplanに結び付くことを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2サンプルライブラリ、アプリケーションソース、DBRM/LOADライブラリ、JDBC/SQLJドライバ導入先、SDSFを机上確認できる前提です。実機では権限、SSID、collection、plan、package、WLM環境、出力データセット名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、静的SQL準備、対話/バッチSQL実行、Java接続支援の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用の準備、実行、またはbind確認コマンドを入力します。対象のプログラム、package、plan、またはサンプル名を明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; PREP/BIND APP=PAYROLL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; PREP/BIND APP=PAYROLL
PREP/BIND APP=PAYROLL が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではDBRM、package、SQL実行結果、またはJava支援資材の状態を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
PRECOMPILE APP=PAYROLL DBRM=PAYROLL
BIND PACKAGE PAYCOLL.PAYROLL SQLERROR=N
BIND PLAN PAYPLAN PKLIST=PAYCOLL.PAYROLL
NORMAL COMPLETION
DBRM=PAYROLL が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
PRECOMPILE APP=PAYROLL DBRM=PAYROLL
BIND PACKAGE PAYCOLL.PAYROLL SQLERROR=N
BIND PLAN PAYPLAN PKLIST=PAYCOLL.PAYROLL
ISSUER=USER1
DBRM=PAYROLL と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の PREP/BIND APP=PAYROLL が操作（入力）に記載されていること
② ステップ2 の DBRM=PAYROLL が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div><div class="kb-p"><p class="kb-pname"><strong>SPUFI 確認手順</strong></p><p>検証目的: SPUFI によるファイル入力SQLの机上実行を確認します。対話SQLではhost variableやSQLCAを前提にしないことも確認します。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2サンプルライブラリ、アプリケーションソース、DBRM/LOADライブラリ、JDBC/SQLJドライバ導入先、SDSFを机上確認できる前提です。実機では権限、SSID、collection、plan、package、WLM環境、出力データセット名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、静的SQL準備、対話/バッチSQL実行、Java接続支援の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用の準備、実行、またはbind確認コマンドを入力します。対象のプログラム、package、plan、またはサンプル名を明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SPUFI INPUT=&#x27;USER1.SQL(CHECK1)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SPUFI INPUT=&#x27;USER1.SQL(CHECK1)&#x27;
SPUFI INPUT=&#x27;USER1.SQL(CHECK1)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではDBRM、package、SQL実行結果、またはJava支援資材の状態を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
SPUFI INPUT USER1.SQL(CHECK1)
SQLCODE=000 ROWS SELECTED=3
HOST VARIABLES NOT USED
NORMAL COMPLETION
SQLCODE=000 が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
SPUFI INPUT USER1.SQL(CHECK1)
SQLCODE=000 ROWS SELECTED=3
HOST VARIABLES NOT USED
ISSUER=USER1
SQLCODE=000 と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SPUFI INPUT=&#x27;USER1.SQL(CHECK1)&#x27; が操作（入力）に記載されていること
② ステップ2 の SQLCODE=000 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNTIAUL 確認手順</strong></p><p>検証目的: DSNTIAUL による表データ抽出を机上確認します。LOAD互換形式の出力と制御文生成を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2サンプルライブラリ、アプリケーションソース、DBRM/LOADライブラリ、JDBC/SQLJドライバ導入先、SDSFを机上確認できる前提です。実機では権限、SSID、collection、plan、package、WLM環境、出力データセット名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、静的SQL準備、対話/バッチSQL実行、Java接続支援の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用の準備、実行、またはbind確認コマンドを入力します。対象のプログラム、package、plan、またはサンプル名を明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; RUN PROGRAM(DSNTIAUL) SYSIN=&#x27;USER1.SQL(UNLOAD1)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; RUN PROGRAM(DSNTIAUL) SYSIN=&#x27;USER1.SQL(UNLOAD1)&#x27;
RUN PROGRAM(DSNTIAUL) SYSIN=&#x27;USER1.SQL(UNLOAD1)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではDBRM、package、SQL実行結果、またはJava支援資材の状態を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNTIAUL UNLOAD TABLE=USER1.EMP ROWS=120
LOAD CONTROL STATEMENTS GENERATED
OUTPUT FORMAT=LOADCOMPAT
NORMAL COMPLETION
DSNTIAUL UNLOAD が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNTIAUL UNLOAD TABLE=USER1.EMP ROWS=120
LOAD CONTROL STATEMENTS GENERATED
OUTPUT FORMAT=LOADCOMPAT
ISSUER=USER1
DSNTIAUL UNLOAD と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の RUN PROGRAM(DSNTIAUL) SYSIN=&#x27;USER1.SQL(UNLOAD1)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNTIAUL UNLOAD が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div><div class="kb-p"><p class="kb-pname"><strong>DB2Binder 確認手順</strong></p><p>検証目的: DB2Binder によるJDBC/SQLJドライバ用package bindを机上確認します。collection、package、EXECUTE権限の状態を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2サンプルライブラリ、アプリケーションソース、DBRM/LOADライブラリ、JDBC/SQLJドライバ導入先、SDSFを机上確認できる前提です。実機では権限、SSID、collection、plan、package、WLM環境、出力データセット名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、静的SQL準備、対話/バッチSQL実行、Java接続支援の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用の準備、実行、またはbind確認コマンドを入力します。対象のプログラム、package、plan、またはサンプル名を明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; java com.ibm.db2.jcc.DB2Binder -url jdbc:db2://host:446/DB2A -collection JCCCOLL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; java com.ibm.db2.jcc.DB2Binder -url jdbc:db2://host:446/DB2A -collection JCCCOLL
java com.ibm.db2.jcc.DB2Binder -url jdbc:db2://host:446/DB2A -collection JCCCOLL が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではDBRM、package、SQL実行結果、またはJava支援資材の状態を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DB2Binder COLLECTION=JCCCOLL ACTION=BIND PACKAGES=COMPLETE
GRANT EXECUTE TO PUBLIC COMPLETE
NORMAL COMPLETION
PACKAGES=COMPLETE が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DB2Binder COLLECTION=JCCCOLL ACTION=BIND PACKAGES=COMPLETE
GRANT EXECUTE TO PUBLIC COMPLETE
ISSUER=USER1
PACKAGES=COMPLETE と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の java com.ibm.db2.jcc.DB2Binder -url jdbc:db2://host:446/DB2A -collection JCCCOLL が操作（入力）に記載されていること
② ステップ2 の PACKAGES=COMPLETE が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div><div class="kb-p"><p class="kb-pname"><strong>Java stored procedure support 確認手順</strong></p><p>検証目的: Java stored procedure support の机上構成を確認します。WLM環境、JAVAENV、DSNTIJRTによる定義とpackage bindの結果を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2サンプルライブラリ、アプリケーションソース、DBRM/LOADライブラリ、JDBC/SQLJドライバ導入先、SDSFを机上確認できる前提です。実機では権限、SSID、collection、plan、package、WLM環境、出力データセット名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、静的SQL準備、対話/バッチSQL実行、Java接続支援の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用の準備、実行、またはbind確認コマンドを入力します。対象のプログラム、package、plan、またはサンプル名を明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではDBRM、package、SQL実行結果、またはJava支援資材の状態を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNTIJRT DSNTRIN COMPLETED WLMENV=DSNWLM_GENERAL
JAVAENV CLASSPATH=/usr/lpp/db2/jdbc/classes
STORED PROCEDURE PACKAGES=BIND COMPLETE
NORMAL COMPLETION
WLMENV=DSNWLM_GENERAL が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNTIJRT DSNTRIN COMPLETED WLMENV=DSNWLM_GENERAL
JAVAENV CLASSPATH=/usr/lpp/db2/jdbc/classes
STORED PROCEDURE PACKAGES=BIND COMPLETE
ISSUER=USER1
WLMENV=DSNWLM_GENERAL と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27; が操作（入力）に記載されていること
② ステップ2 の WLMENV=DSNWLM_GENERAL が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_AppProg_Java / Db2_zOS_Introduction</p></div><div class="kb-p"><p class="kb-pname"><strong>BIND PACKAGE 確認手順</strong></p><p>検証目的: DBRMからアプリケーションパッケージを作成します。新規プログラムを実行可能な資材としてDb2へ登録する入口を確認します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムのDSNサブコマンドを実行できる権限があること。例示名 APP1、COLL1、USER1 は机上確認用であり、実機では環境の命名規則に合わせること。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に BIND PACKAGE(COLL1) MEMBER(APP1) ACTION(REPLACE) ISOLATION(CS) を入力し、BIND PACKAGE の机上確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; BIND PACKAGE(COLL1) MEMBER(APP1) ACTION(REPLACE) ISOLATION(CS)
→ Enter を押す
［画面・出力］
DSN&gt;
BIND PACKAGE(COLL1) MEMBER(APP1) ACTION(REPLACE) ISOLATION(CS)
BIND PACKAGE SUCCESSFUL
PACKAGE = COLL1.APP1
ACTION = REPLACE
DSN&gt;
BIND PACKAGE SUCCESSFUL と PACKAGE = COLL1.APP1 が表示されていれば、BIND PACKAGE の操作結果を確認できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の BIND PACKAGE SUCCESSFUL が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>BIND PLAN 確認手順</strong></p><p>検証目的: パッケージを含むアプリケーションプランを作成します。実行時に参照されるプラン名とPKLISTの関係を確認します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムのDSNサブコマンドを実行できる権限があること。例示名 APP1、COLL1、USER1 は机上確認用であり、実機では環境の命名規則に合わせること。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に BIND PLAN(APPPLAN) PKLIST(COLL1.APP1) ACTION(REPLACE) を入力し、BIND PLAN の机上確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; BIND PLAN(APPPLAN) PKLIST(COLL1.APP1) ACTION(REPLACE)
→ Enter を押す
［画面・出力］
DSN&gt;
BIND PLAN(APPPLAN) PKLIST(COLL1.APP1) ACTION(REPLACE)
BIND PLAN SUCCESSFUL
PLAN = APPPLAN
PKLIST = COLL1.APP1
DSN&gt;
BIND PLAN SUCCESSFUL と PLAN = APPPLAN が表示されていれば、BIND PLAN の操作結果を確認できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の BIND PLAN SUCCESSFUL が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>REBIND PACKAGE 確認手順</strong></p><p>検証目的: 既存パッケージを再バインドします。統計更新後やオプション変更後の再作成結果を確認します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムのDSNサブコマンドを実行できる権限があること。例示名 APP1、COLL1、USER1 は机上確認用であり、実機では環境の命名規則に合わせること。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に REBIND PACKAGE(COLL1.APP1) APREUSE(NO) を入力し、REBIND PACKAGE の机上確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; REBIND PACKAGE(COLL1.APP1) APREUSE(NO)
→ Enter を押す
［画面・出力］
DSN&gt;
REBIND PACKAGE(COLL1.APP1) APREUSE(NO)
REBIND PACKAGE SUCCESSFUL
PACKAGE = COLL1.APP1
APREUSE = NO
DSN&gt;
REBIND PACKAGE SUCCESSFUL と PACKAGE = COLL1.APP1 が表示されていれば、REBIND PACKAGE の操作結果を確認できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の REBIND PACKAGE SUCCESSFUL が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>REBIND PLAN 確認手順</strong></p><p>検証目的: 既存プランを再バインドします。プラン単位の属性変更やパッケージ指定の確認に使う操作を記録します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムのDSNサブコマンドを実行できる権限があること。例示名 APP1、COLL1、USER1 は机上確認用であり、実機では環境の命名規則に合わせること。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に REBIND PLAN(APPPLAN) VALIDATE(BIND) を入力し、REBIND PLAN の机上確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; REBIND PLAN(APPPLAN) VALIDATE(BIND)
→ Enter を押す
［画面・出力］
DSN&gt;
REBIND PLAN(APPPLAN) VALIDATE(BIND)
REBIND PLAN SUCCESSFUL
PLAN = APPPLAN
VALIDATE = BIND
DSN&gt;
REBIND PLAN SUCCESSFUL と PLAN = APPPLAN が表示されていれば、REBIND PLAN の操作結果を確認できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の REBIND PLAN SUCCESSFUL が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>FREE PACKAGE 確認手順</strong></p><p>検証目的: 不要になったパッケージを解放します。廃止済みアプリケーション資材をDb2管理対象から外す操作を確認します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムのDSNサブコマンドを実行できる権限があること。例示名 APP1、COLL1、USER1 は机上確認用であり、実機では環境の命名規則に合わせること。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に FREE PACKAGE(COLL1.APP1) を入力し、FREE PACKAGE の机上確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; FREE PACKAGE(COLL1.APP1)
→ Enter を押す
［画面・出力］
DSN&gt;
FREE PACKAGE(COLL1.APP1)
FREE PACKAGE SUCCESSFUL
PACKAGE = COLL1.APP1
STATUS = FREED
DSN&gt;
FREE PACKAGE SUCCESSFUL と PACKAGE = COLL1.APP1 が表示されていれば、FREE PACKAGE の操作結果を確認できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の FREE PACKAGE SUCCESSFUL が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_AppProg_SQL_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>SYSADM 確認手順</strong></p><p>検証目的: 管理権限の付与状態をカタログで確認します。強い権限を持つIDを棚卸しし、職務分離の確認材料にします。</p><p>前提条件: TSOログオン済でSPUFIを起動でき、対象Db2サブシステムの参照またはDDL実行権限があること。ここでは机上例としてAPPDBA、APPUSER、EMPLOYEE、AUDIT_APPを使う。</p><p>セッション環境: TSO/ISPF からSPUFIへ入り、DBD1サブシステムに接続してSQLを実行する。変更系SQLは机上確認であり、実機適用前に権限承認を取る。</p><pre class="kb-code">■ ステップ 1
現在の画面はISPFのコマンド入力画面です。Command ===&gt; に =SPUFI を入力し、SQLを投入するSPUFI画面へ移動します。
［操作（入力）］
Command ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DB2 SSID ===&gt; DBD1 が表示されていれば、DBD1向けにSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT GRANTEE, SYSADMAUTH FROM SYSIBM.SYSUSERAUTH WHERE GRANTEE = &#x27;APPDBA&#x27;; から始まるSQLを入力し、SYSADM付与状況確認 の確認結果を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT GRANTEE, SYSADMAUTH FROM SYSIBM.SYSUSERAUTH WHERE GRANTEE = &#x27;APPDBA&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
GRANTEE  SYSADMAUTH
APPDBA   Y
1 ROW SELECTED
SQLCODE = 0
SPUFI OUTPUT と APPDBA が表示されていれば、SYSADM付与状況確認 の確認結果を取得できています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。Command ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
Command ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIの確認作業を終了できています。
――――</pre><p>合格条件: ① ステップ 1 の SPUFI が表示されること
② ステップ 2 の APPDBA が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>trusted context 確認手順</strong></p><p>検証目的: 接続条件に基づくtrusted context定義を確認します。特定接続元だけに追加の扱いを許す設計を机上で確認します。</p><p>前提条件: TSOログオン済でSPUFIを起動でき、対象Db2サブシステムの参照またはDDL実行権限があること。ここでは机上例としてAPPDBA、APPUSER、EMPLOYEE、AUDIT_APPを使う。</p><p>セッション環境: TSO/ISPF からSPUFIへ入り、DBD1サブシステムに接続してSQLを実行する。変更系SQLは机上確認であり、実機適用前に権限承認を取る。</p><pre class="kb-code">■ ステップ 1
現在の画面はISPFのコマンド入力画面です。Command ===&gt; に =SPUFI を入力し、SQLを投入するSPUFI画面へ移動します。
［操作（入力）］
Command ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DB2 SSID ===&gt; DBD1 が表示されていれば、DBD1向けにSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT NAME, ENABLED FROM SYSIBM.SYSCONTEXT WHERE NAME = &#x27;TC_APP&#x27;; から始まるSQLを入力し、trusted context定義確認 の確認結果を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT NAME, ENABLED FROM SYSIBM.SYSCONTEXT WHERE NAME = &#x27;TC_APP&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
NAME    ENABLED
TC_APP  Y
1 ROW SELECTED
SQLCODE = 0
SPUFI OUTPUT と TC_APP が表示されていれば、trusted context定義確認 の確認結果を取得できています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。Command ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
Command ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIの確認作業を終了できています。
――――</pre><p>合格条件: ① ステップ 1 の SPUFI が表示されること
② ステップ 2 の TC_APP が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>row permission 確認手順</strong></p><p>検証目的: 行アクセス制御の定義を確認します。利用者ごとの表示行がデータベース側で制御されることを確認します。</p><p>前提条件: TSOログオン済でSPUFIを起動でき、対象Db2サブシステムの参照またはDDL実行権限があること。ここでは机上例としてAPPDBA、APPUSER、EMPLOYEE、AUDIT_APPを使う。</p><p>セッション環境: TSO/ISPF からSPUFIへ入り、DBD1サブシステムに接続してSQLを実行する。変更系SQLは机上確認であり、実機適用前に権限承認を取る。</p><pre class="kb-code">■ ステップ 1
現在の画面はISPFのコマンド入力画面です。Command ===&gt; に =SPUFI を入力し、SQLを投入するSPUFI画面へ移動します。
［操作（入力）］
Command ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DB2 SSID ===&gt; DBD1 が表示されていれば、DBD1向けにSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT NAME, ENABLED FROM SYSIBM.SYSPERMISSIONS WHERE TBNAME = &#x27;EMPLOYEE&#x27;; から始まるSQLを入力し、row permission確認 の確認結果を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT NAME, ENABLED FROM SYSIBM.SYSPERMISSIONS WHERE TBNAME = &#x27;EMPLOYEE&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
NAME          ENABLED
EMP_DEPT_PERM Y
1 ROW SELECTED
SQLCODE = 0
SPUFI OUTPUT と EMP_DEPT_PERM が表示されていれば、row permission確認 の確認結果を取得できています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。Command ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
Command ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIの確認作業を終了できています。
――――</pre><p>合格条件: ① ステップ 1 の SPUFI が表示されること
② ステップ 2 の EMP_DEPT_PERM が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>column mask 確認手順</strong></p><p>検証目的: 列マスク定義を確認します。機密列の表示値が権限条件に応じて変わる設計を机上で確認します。</p><p>前提条件: TSOログオン済でSPUFIを起動でき、対象Db2サブシステムの参照またはDDL実行権限があること。ここでは机上例としてAPPDBA、APPUSER、EMPLOYEE、AUDIT_APPを使う。</p><p>セッション環境: TSO/ISPF からSPUFIへ入り、DBD1サブシステムに接続してSQLを実行する。変更系SQLは机上確認であり、実機適用前に権限承認を取る。</p><pre class="kb-code">■ ステップ 1
現在の画面はISPFのコマンド入力画面です。Command ===&gt; に =SPUFI を入力し、SQLを投入するSPUFI画面へ移動します。
［操作（入力）］
Command ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DB2 SSID ===&gt; DBD1 が表示されていれば、DBD1向けにSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT NAME, ENABLED FROM SYSIBM.SYSMASKS WHERE TBNAME = &#x27;EMPLOYEE&#x27;; から始まるSQLを入力し、column mask確認 の確認結果を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT NAME, ENABLED FROM SYSIBM.SYSMASKS WHERE TBNAME = &#x27;EMPLOYEE&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
NAME         ENABLED
EMP_SAL_MASK Y
1 ROW SELECTED
SQLCODE = 0
SPUFI OUTPUT と EMP_SAL_MASK が表示されていれば、column mask確認 の確認結果を取得できています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。Command ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
Command ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIの確認作業を終了できています。
――――</pre><p>合格条件: ① ステップ 1 の SPUFI が表示されること
② ステップ 2 の EMP_SAL_MASK が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>tamper-proof audit policy 確認手順</strong></p><p>検証目的: 改ざん耐性監査ポリシーの設定を確認します。DB2START=T の監査ポリシーが保護対象として扱われることを確認します。</p><p>前提条件: TSOログオン済でSPUFIを起動でき、対象Db2サブシステムの参照またはDDL実行権限があること。ここでは机上例としてAPPDBA、APPUSER、EMPLOYEE、AUDIT_APPを使う。</p><p>セッション環境: TSO/ISPF からSPUFIへ入り、DBD1サブシステムに接続してSQLを実行する。変更系SQLは机上確認であり、実機適用前に権限承認を取る。</p><pre class="kb-code">■ ステップ 1
現在の画面はISPFのコマンド入力画面です。Command ===&gt; に =SPUFI を入力し、SQLを投入するSPUFI画面へ移動します。
［操作（入力）］
Command ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DB2 SSID ===&gt; DBD1 が表示されていれば、DBD1向けにSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT AUDITPOLICYNAME, DB2START FROM SYSIBM.SYSAUDITPOLICIES WHERE AUDITPOLICYNAME = &#x27;AUDIT_APP&#x27;; から始まるSQLを入力し、tamper-proof audit policy確認 の確認結果を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT AUDITPOLICYNAME, DB2START FROM SYSIBM.SYSAUDITPOLICIES WHERE AUDITPOLICYNAME = &#x27;AUDIT_APP&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
AUDITPOLICYNAME  DB2START
AUDIT_APP        T
1 ROW SELECTED
SQLCODE = 0
SPUFI OUTPUT と AUDIT_APP が表示されていれば、tamper-proof audit policy確認 の確認結果を取得できています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。Command ===&gt; に END を入力し、確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
Command ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIの確認作業を終了できています。
――――</pre><p>合格条件: ① ステップ 1 の SPUFI が表示されること
② ステップ 2 の AUDIT_APP が表示されること
③ ステップ 3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>RUNSTATS PROFILE 確認手順</strong></p><p>検証目的: RUNSTATS PROFILE を使った統計収集の机上結果を確認します。profile利用、catalog statistics更新、対象オブジェクトを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2 catalogとdirectoryの対象名、SDSNSAMP、SDSF、RUNSTATS/REORG/COPYを机上確認できる前提です。実機ではSSID、権限、対象table space、image copy先、停止要否、バックアウト手順を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、catalog/directory、統計、PLAN_TABLE、catalog保守の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; にcatalog保守、統計収集、または説明情報確認の机上コマンドを入力します。対象名を明示して、次の応答で同じ対象の結果を読み取ります。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; RUNSTATS TABLESPACE DBPAY.TSPAY USE PROFILE
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; RUNSTATS TABLESPACE DBPAY.TSPAY USE PROFILE
RUNSTATS TABLESPACE DBPAY.TSPAY USE PROFILE が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではcopy、統計、PLAN_TABLE行、REORG、またはCATMAINT結果を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
RUNSTATS PROFILE USED TABLESPACE=DBPAY.TSPAY
CATALOG STATISTICS UPDATED TABLES=4 INDEXES=7
NORMAL COMPLETION
PROFILE USED が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
RUNSTATS PROFILE USED TABLESPACE=DBPAY.TSPAY
CATALOG STATISTICS UPDATED TABLES=4 INDEXES=7
ISSUER=USER1
PROFILE USED と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の RUNSTATS TABLESPACE DBPAY.TSPAY USE PROFILE が操作（入力）に記載されていること
② ステップ2 の PROFILE USED が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>PLAN_TABLE as metadata 確認手順</strong></p><p>検証目的: EXPLAIN結果がPLAN_TABLEに記録される机上結果を確認します。QUERYNO、access type、索引利用の有無を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2 catalogとdirectoryの対象名、SDSNSAMP、SDSF、RUNSTATS/REORG/COPYを机上確認できる前提です。実機ではSSID、権限、対象table space、image copy先、停止要否、バックアウト手順を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、catalog/directory、統計、PLAN_TABLE、catalog保守の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; にcatalog保守、統計収集、または説明情報確認の机上コマンドを入力します。対象名を明示して、次の応答で同じ対象の結果を読み取ります。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; EXPLAIN PLAN SET QUERYNO = 2101 FOR SELECT * FROM SYSIBM.SYSTABLES WHERE NAME=&#x27;EMP&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; EXPLAIN PLAN SET QUERYNO = 2101 FOR SELECT * FROM SYSIBM.SYSTABLES WHERE NAME=&#x27;EMP&#x27;
EXPLAIN PLAN SET QUERYNO = 2101 FOR SELECT * FROM SYSIBM.SYSTABLES WHERE NAME=&#x27;EMP&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではcopy、統計、PLAN_TABLE行、REORG、またはCATMAINT結果を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
PLAN_TABLE QUERYNO=2101 METHOD=0 ACCESSTYPE=I MATCHCOLS=1
OBJECT=SYSIBM.SYSTABLES INDEX=DSNDXX01
NORMAL COMPLETION
QUERYNO=2101 が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
PLAN_TABLE QUERYNO=2101 METHOD=0 ACCESSTYPE=I MATCHCOLS=1
OBJECT=SYSIBM.SYSTABLES INDEX=DSNDXX01
ISSUER=USER1
QUERYNO=2101 と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の EXPLAIN PLAN SET QUERYNO = 2101 FOR SELECT * FROM SYSIBM.SYSTABLES WHERE NAME=&#x27;EMP&#x27; が操作（入力）に記載されていること
② ステップ2 の QUERYNO=2101 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>catalog image copy 確認手順</strong></p><p>検証目的: catalogとdirectoryのimage copy取得結果を机上確認します。コピー対象、copy完了、回復に使う履歴の有無を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2 catalogとdirectoryの対象名、SDSNSAMP、SDSF、RUNSTATS/REORG/COPYを机上確認できる前提です。実機ではSSID、権限、対象table space、image copy先、停止要否、バックアウト手順を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、catalog/directory、統計、PLAN_TABLE、catalog保守の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; にcatalog保守、統計収集、または説明情報確認の机上コマンドを入力します。対象名を明示して、次の応答で同じ対象の結果を読み取ります。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではcopy、統計、PLAN_TABLE行、REORG、またはCATMAINT結果を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12410 DSNTIJIC COPY COMPLETED DATABASE=DSNDB06 DIRECTORY=DSNDB01
SYSCOPY RECORDS INSERTED COPYTYPE=FULL
NORMAL COMPLETION
COPY COMPLETED が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12410 DSNTIJIC COPY COMPLETED DATABASE=DSNDB06 DIRECTORY=DSNDB01
SYSCOPY RECORDS INSERTED COPYTYPE=FULL
ISSUER=USER1
COPY COMPLETED と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJIC)&#x27; が操作（入力）に記載されていること
② ステップ2 の COPY COMPLETED が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>catalog REORG 確認手順</strong></p><p>検証目的: catalog table spaceのREORG机上結果を確認します。対象、完了状態、AREO*解消の有無を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2 catalogとdirectoryの対象名、SDSNSAMP、SDSF、RUNSTATS/REORG/COPYを机上確認できる前提です。実機ではSSID、権限、対象table space、image copy先、停止要否、バックアウト手順を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、catalog/directory、統計、PLAN_TABLE、catalog保守の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; にcatalog保守、統計収集、または説明情報確認の机上コマンドを入力します。対象名を明示して、次の応答で同じ対象の結果を読み取ります。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; REORG TABLESPACE DSNDB06.SYSTSDBA
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; REORG TABLESPACE DSNDB06.SYSTSDBA
REORG TABLESPACE DSNDB06.SYSTSDBA が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではcopy、統計、PLAN_TABLE行、REORG、またはCATMAINT結果を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
REORG TABLESPACE DSNDB06.SYSTSDBA COMPLETED RC=0000
ADVISORY STATUS AREO* CLEARED
NORMAL COMPLETION
REORG TABLESPACE が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
REORG TABLESPACE DSNDB06.SYSTSDBA COMPLETED RC=0000
ADVISORY STATUS AREO* CLEARED
ISSUER=USER1
REORG TABLESPACE と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の REORG TABLESPACE DSNDB06.SYSTSDBA が操作（入力）に記載されていること
② ステップ2 の REORG TABLESPACE が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>CATMAINT 確認手順</strong></p><p>検証目的: CATMAINT実行後のcatalog更新と保守影響を机上確認します。更新完了、AREO*対象、後続REORG要否を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2 catalogとdirectoryの対象名、SDSNSAMP、SDSF、RUNSTATS/REORG/COPYを机上確認できる前提です。実機ではSSID、権限、対象table space、image copy先、停止要否、バックアウト手順を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF で、catalog/directory、統計、PLAN_TABLE、catalog保守の机上出力を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; にcatalog保守、統計収集、または説明情報確認の机上コマンドを入力します。対象名を明示して、次の応答で同じ対象の結果を読み取ります。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; CATMAINT UPDATE LEVEL(V13R1M500)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; CATMAINT UPDATE LEVEL(V13R1M500)
CATMAINT UPDATE LEVEL(V13R1M500) が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではcopy、統計、PLAN_TABLE行、REORG、またはCATMAINT結果を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
CATMAINT UPDATE COMPLETED LEVEL=V13R1M500
CATALOG OBJECTS ALTERED=12 AREO*=3 REORG REQUIRED
NORMAL COMPLETION
CATMAINT UPDATE COMPLETED が表示されていれば、机上例では対象作業の結果を確認できます。NORMAL COMPLETION も同じ画面で見て、異常終了ではないことを確認します。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、対象ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
CATMAINT UPDATE COMPLETED LEVEL=V13R1M500
CATALOG OBJECTS ALTERED=12 AREO*=3 REORG REQUIRED
ISSUER=USER1
CATMAINT UPDATE COMPLETED と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の CATMAINT UPDATE LEVEL(V13R1M500) が操作（入力）に記載されていること
② ステップ2 の CATMAINT UPDATE COMPLETED が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Utility_Guide</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNUTILB 確認手順</strong></p><p>検証目的: DSNUTILB から LOAD utility を起動し、TEMPLATE と LISTDEF を使った対象指定がログに残ることを確認します。開始応答、LOAD 完了、操作者証跡を分けて読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の保守コマンドを実行できる権限、SDSF で対象ジョブと SYSLOG を確認できる権限、対象 table space と utility ID の運用承認があります。実機では対象名、停止可否、backup の取得状況を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、utility の投入、応答、ログ証跡を机上例として確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象 utility の指示を入力し、処理を開始するために Enter を押します。ここでは実行対象と utility ID を同じ行で確認できるようにします。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(LOADPAY)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(LOADPAY)
DSNU000I DSNUTILB UTILITY STARTED
DSNU000I が表示されていれば、Db2 が utility の開始要求を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、入力した指示と応答を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、utility ジョブの出力を開くために Enter を押します。対象 JobName と JobID を画面上で確認してから選択します。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2UTIL  JOB12522 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(SDSF JOB OUTPUT)
DSNU050I TEMPLATE PAYOUT DSN=DB2A.PAY.COPY0001
DSNU052I LISTDEF PAYLIST INCLUDED TABLESPACE DBPAY.TSPAY
DSNU100I LOAD TABLE PAY.EMP RECORDS=125000 RC=0000
DSNU100I が出力に含まれていれば、この手順で期待する utility 結果を確認できます。JOB12522 の出力として読めるため、別ジョブのログと取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ utility のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DSNUTILB
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU000I UTILID=LOADPAY START TIME=22.10.01
DSNU010I ISSUER=USER1 SSID=DB2A
DSNU100I LOAD COMPLETE RC=0000
ISSUER=USER1 が SYSLOG に出ていれば、対象 utility の実行者または制御結果を証跡として追えます。DB2A と UTILID も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNU000I が表示されていること
② ステップ 2 の DSNU100I が期待どおりであること
③ ステップ 3 の ISSUER=USER1 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>UNLOAD 確認手順</strong></p><p>検証目的: UNLOAD の抽出結果と、保守処理中に取得した inline copy の証跡を机上で確認します。抽出件数、出力先、copy 完了メッセージを同じ utility ID で照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の保守コマンドを実行できる権限、SDSF で対象ジョブと SYSLOG を確認できる権限、対象 table space と utility ID の運用承認があります。実機では対象名、停止可否、backup の取得状況を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、utility の投入、応答、ログ証跡を机上例として確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象 utility の指示を入力し、処理を開始するために Enter を押します。ここでは実行対象と utility ID を同じ行で確認できるようにします。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(UNLDCOPY)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(UNLDCOPY)
DSNU000I DSNUTILB UTILITY STARTED
DSNU000I が表示されていれば、Db2 が utility の開始要求を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、入力した指示と応答を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、utility ジョブの出力を開くために Enter を押します。対象 JobName と JobID を画面上で確認してから選択します。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2UTIL  JOB12522 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(SDSF JOB OUTPUT)
DSNU200I UNLOAD TABLE PAY.EMP ROWS=125000 OUTDDN=SYSREC
DSNU210I INLINE COPY DDNAME=ICCOPY1 COPYTYPE=FULL
DSNU299I UNLOAD COMPLETE RC=0000
DSNU299I が出力に含まれていれば、この手順で期待する utility 結果を確認できます。JOB12522 の出力として読めるため、別ジョブのログと取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ utility のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DSNUTILB
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU000I UTILID=UNLDCOPY START TIME=23.05.14
DSNU010I ISSUER=USER1 SSID=DB2A
DSNU210I INLINE COPY COMPLETE DDNAME=ICCOPY1
INLINE COPY COMPLETE が SYSLOG に出ていれば、対象 utility の実行者または制御結果を証跡として追えます。DB2A と UTILID も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNU000I が表示されていること
② ステップ 2 の DSNU299I が期待どおりであること
③ ステップ 3 の INLINE COPY COMPLETE が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>COPY 確認手順</strong></p><p>検証目的: image copy 取得の utility 出力を机上で確認します。対象 object、copy data set、return code を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で catalog、command、utility output、log 関連情報を机上確認できる権限があります。実機では database 名、object 名、thread、utility ID、log data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、Db2 for z/OS の基礎構造、DDL、utility、log、command 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; COPY TABLESPACE PAYDB.PAYTS SHRLEVEL CHANGE
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; COPY TABLESPACE PAYDB.PAYTS SHRLEVEL CHANGE
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT30  JOB13030 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNU000I COPY TABLESPACE PAYDB.PAYTS STARTED
DSNU1044I IMAGE COPY DATA SET=USER1.PAYTS.IC.COPY1
DSNU010I UTILITY EXECUTION COMPLETE, HIGHEST RETURN CODE=0
DSNU1044I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB13030 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に subsystem と対象名を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT30
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU000I COPY PAYDB.PAYTS STARTED SSID=DB2A
DSNU1044I DATA SET=USER1.PAYTS.IC.COPY1
DSNU010I HIGHEST RETURN CODE=0
USER1.PAYTS.IC.COPY1 が SYSLOG に出ていれば、対象操作の証跡を追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNU1044I が期待どおりであること
③ ステップ3 の USER1.PAYTS.IC.COPY1 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>REORG TABLESPACE 確認手順</strong></p><p>検証目的: REORG TABLESPACE の完了と、後続 RUNSTATS による catalog 統計更新を確認します。再編成、統計収集、戻りコードを分けて記録します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の保守コマンドを実行できる権限、SDSF で対象ジョブと SYSLOG を確認できる権限、対象 table space と utility ID の運用承認があります。実機では対象名、停止可否、backup の取得状況を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、utility の投入、応答、ログ証跡を机上例として確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象 utility の指示を入力し、処理を開始するために Enter を押します。ここでは実行対象と utility ID を同じ行で確認できるようにします。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(REORGPAY)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(REORGPAY)
DSNU000I DSNUTILB UTILITY STARTED
DSNU000I が表示されていれば、Db2 が utility の開始要求を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、入力した指示と応答を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、utility ジョブの出力を開くために Enter を押します。対象 JobName と JobID を画面上で確認してから選択します。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2UTIL  JOB12522 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(SDSF JOB OUTPUT)
DSNU300I REORG TABLESPACE DBPAY.TSPAY PHASE=RELOAD COMPLETE
DSNU320I RUNSTATS TABLESPACE DBPAY.TSPAY UPDATED CATALOG STATISTICS
DSNU399I REORG COMPLETE RC=0000
DSNU399I が出力に含まれていれば、この手順で期待する utility 結果を確認できます。JOB12522 の出力として読めるため、別ジョブのログと取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ utility のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DSNUTILB
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU000I UTILID=REORGPAY START TIME=00.12.43
DSNU010I ISSUER=USER1 SSID=DB2A
DSNU320I RUNSTATS COMPLETE TABLES=4 INDEXES=7
RUNSTATS COMPLETE が SYSLOG に出ていれば、対象 utility の実行者または制御結果を証跡として追えます。DB2A と UTILID も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNU000I が表示されていること
② ステップ 2 の DSNU399I が期待どおりであること
③ ステップ 3 の RUNSTATS COMPLETE が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>CHECK INDEX 確認手順</strong></p><p>検証目的: CHECK INDEX の検査結果を読み、再作成が必要な場合に REBUILD INDEX の完了を確認します。索引名、検査結果、再作成完了コードを証跡として残します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の保守コマンドを実行できる権限、SDSF で対象ジョブと SYSLOG を確認できる権限、対象 table space と utility ID の運用承認があります。実機では対象名、停止可否、backup の取得状況を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、utility の投入、応答、ログ証跡を机上例として確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象 utility の指示を入力し、処理を開始するために Enter を押します。ここでは実行対象と utility ID を同じ行で確認できるようにします。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(IXFIX01)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; RUN UTILITY DSNUTILB UTILID(IXFIX01)
DSNU000I DSNUTILB UTILITY STARTED
DSNU000I が表示されていれば、Db2 が utility の開始要求を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、入力した指示と応答を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、utility ジョブの出力を開くために Enter を押します。対象 JobName と JobID を画面上で確認してから選択します。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2UTIL  JOB12522 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(SDSF JOB OUTPUT)
DSNU400I CHECK INDEX IX_PAY_EMP ERROR COUNT=2
DSNU410I REBUILD INDEX IX_PAY_EMP STARTED
DSNU499I REBUILD INDEX IX_PAY_EMP COMPLETE RC=0000
DSNU499I が出力に含まれていれば、この手順で期待する utility 結果を確認できます。JOB12522 の出力として読めるため、別ジョブのログと取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ utility のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DSNUTILB
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU000I UTILID=IXFIX01 START TIME=01.30.22
DSNU010I ISSUER=USER1 SSID=DB2A
DSNU499I REBUILD INDEX COMPLETE INDEX=IX_PAY_EMP
INDEX=IX_PAY_EMP が SYSLOG に出ていれば、対象 utility の実行者または制御結果を証跡として追えます。DB2A と UTILID も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNU000I が表示されていること
② ステップ 2 の DSNU499I が期待どおりであること
③ ステップ 3 の INDEX=IX_PAY_EMP が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY UTILITY 確認手順</strong></p><p>検証目的: DISPLAY UTILITY で長時間実行中の utility 状態を確認し、運用判断後に TERM UTILITY の指示結果を机上で確認します。終了前後の UTILID と phase を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の保守コマンドを実行できる権限、SDSF で対象ジョブと SYSLOG を確認できる権限、対象 table space と utility ID の運用承認があります。実機では対象名、停止可否、backup の取得状況を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、utility の投入、応答、ログ証跡を机上例として確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象 utility の指示を入力し、処理を開始するために Enter を押します。ここでは実行対象と utility ID を同じ行で確認できるようにします。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY UTILITY(UTILID LONGLOAD)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY UTILITY(UTILID LONGLOAD)
DSNU000I DSNUTILB UTILITY STARTED
DSNU000I が表示されていれば、Db2 が utility の開始要求を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、入力した指示と応答を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、utility ジョブの出力を開くために Enter を押します。対象 JobName と JobID を画面上で確認してから選択します。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2UTIL  JOB12522 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNU105I DISPLAY UTILITY UTILID=LONGLOAD PHASE=LOAD STATUS=STOPWAIT
DSNU106I DATABASE=DBPAY TABLESPACE=TSPAY
DSN9022I -DB2A DSNU COMMAND NORMAL COMPLETION
DSNU105I が出力に含まれていれば、この手順で期待する utility 結果を確認できます。JOB12522 の出力として読めるため、別ジョブのログと取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ utility のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DSNUTILB
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU000I UTILID=LONGLOAD TERM REQUEST ACCEPTED
DSNU010I ISSUER=USER1 SSID=DB2A
DSNU180I TERM UTILITY COMPLETE UTILID=LONGLOAD
TERM UTILITY COMPLETE が SYSLOG に出ていれば、対象 utility の実行者または制御結果を証跡として追えます。DB2A と UTILID も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNU000I が表示されていること
② ステップ 2 の DSNU105I が期待どおりであること
③ ステップ 3 の TERM UTILITY COMPLETE が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Codes</p></div><div class="kb-p"><p class="kb-pname"><strong>START DB2 確認手順</strong></p><p>検証目的: START DB2とSTOP DB2の机上応答を確認します。保守用起動と計画停止を分けて、メッセージとMODE指定を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機では開始・停止・取消・回復系コマンドは変更管理承認を得て、対象SSIDと影響範囲を確認してから実行します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDb2コマンドを入力し、SDSFまたはコマンド応答画面でメッセージと対象名を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象のDb2コマンドを入力します。この操作では入力するコマンドと対象名を確認し、Enterで応答を取得します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -START DB2 ACCESS(MAINT)
Command ===&gt; -DISPLAY THREAD(*) TYPE(*)
Command ===&gt; -STOP DB2 MODE(QUIESCE)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -START DB2 ACCESS(MAINT)
Command ===&gt; -DISPLAY THREAD(*) TYPE(*)
Command ===&gt; -STOP DB2 MODE(QUIESCE)
-START DB2 ACCESS(MAINT) が入力欄に表示されていれば、机上例の対象コマンドを実行する準備ができています。対象名やMODE指定が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを確認します。操作欄には追加入力を入れず、応答のメッセージIDと対象名を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNY001I -START DB2 ACCESS(MAINT) ACCEPTED
DSNV401I DISPLAY THREAD NORMAL COMPLETION
DSNY002I -STOP DB2 MODE(QUIESCE) ACCEPTED
NORMAL COMPLETION
-START DB2 ACCESS(MAINT) が表示されていれば、机上例では対象コマンドの応答を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、コマンド応答がシステムログにも残っているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNY001I -START DB2 ACCESS(MAINT) ACCEPTED
DSNV401I DISPLAY THREAD NORMAL COMPLETION
DSNY002I -STOP DB2 MODE(QUIESCE) ACCEPTED
ISSUER=USER1
-START DB2 ACCESS(MAINT) と ISSUER=USER1 が表示されていれば、誰がどの操作を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの対象名が一致していることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -START DB2 ACCESS(MAINT) が操作（入力）に記載されていること
② ステップ2 の -START DB2 ACCESS(MAINT) が画面・出力に表示されること
③ ステップ2 の NORMAL COMPLETION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>START DATABASE 確認手順</strong></p><p>検証目的: START DATABASE、STOP DATABASE、DISPLAY DATABASEの使い分けを確認します。対象表スペースの停止、開始、制限状態表示を同じ対象名で追います。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機では開始・停止・取消・回復系コマンドは変更管理承認を得て、対象SSIDと影響範囲を確認してから実行します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDb2コマンドを入力し、SDSFまたはコマンド応答画面でメッセージと対象名を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象のDb2コマンドを入力します。この操作では入力するコマンドと対象名を確認し、Enterで応答を取得します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -STOP DATABASE(PAYDB) SPACENAM(PAYTS)
Command ===&gt; -START DATABASE(PAYDB) SPACENAM(PAYTS) ACCESS(UT)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) RESTRICT
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -STOP DATABASE(PAYDB) SPACENAM(PAYTS)
Command ===&gt; -START DATABASE(PAYDB) SPACENAM(PAYTS) ACCESS(UT)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) RESTRICT
-STOP DATABASE(PAYDB) SPACENAM(PAYTS) が入力欄に表示されていれば、机上例の対象コマンドを実行する準備ができています。対象名やMODE指定が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを確認します。操作欄には追加入力を入れず、応答のメッセージIDと対象名を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNT360I -STOP DATABASE(PAYDB) SPACENAM(PAYTS) ACCEPTED
DSNT361I -START DATABASE(PAYDB) SPACENAM(PAYTS) ACCESS(UT) ACCEPTED
DSNT365I DATABASE=PAYDB SPACENAME=PAYTS STATUS=UT
NORMAL COMPLETION
DATABASE=PAYDB SPACENAME=PAYTS STATUS=UT が表示されていれば、机上例では対象コマンドの応答を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、コマンド応答がシステムログにも残っているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT360I -STOP DATABASE(PAYDB) SPACENAM(PAYTS) ACCEPTED
DSNT361I -START DATABASE(PAYDB) SPACENAM(PAYTS) ACCESS(UT) ACCEPTED
DSNT365I DATABASE=PAYDB SPACENAME=PAYTS STATUS=UT
ISSUER=USER1
DATABASE=PAYDB SPACENAME=PAYTS STATUS=UT と ISSUER=USER1 が表示されていれば、誰がどの操作を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの対象名が一致していることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -STOP DATABASE(PAYDB) SPACENAM(PAYTS) が操作（入力）に記載されていること
② ステップ2 の DATABASE=PAYDB SPACENAME=PAYTS STATUS=UT が画面・出力に表示されること
③ ステップ2 の NORMAL COMPLETION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY DATABASE 確認手順</strong></p><p>検証目的: 対象データベースと表スペースの状態を表示し、停止や制限状態がないかを確認します。DB1.TS1の状態行を証跡として記録します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムの表示系コマンドを実行できる権限があること。表示コマンドのみを使い、停止や変更を伴う操作は行わないこと。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に -DISPLAY DATABASE(DB1) SPACENAM(TS1) を入力し、DISPLAY DATABASE の確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; -DISPLAY DATABASE(DB1) SPACENAM(TS1)
→ Enter を押す
［画面・出力］
DSN&gt;
-DISPLAY DATABASE(DB1) SPACENAM(TS1)
DSNT360I -DBD1 ***********************************
DSNT361I -DBD1 *  DISPLAY DATABASE SUMMARY
DSNT362I -DBD1     DATABASE = DB1  STATUS = RW
DSNT397I -DBD1     SPACENAM = TS1  STATUS = RW
DSN&gt;
DSNT361I と DATABASE = DB1 が表示されていれば、DB1の表示結果を取得できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、表示確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の DSNT361I が表示されること
③ ステップ 2 の STATUS = RW が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY THREAD 確認手順</strong></p><p>検証目的: 実行中 thread の状態を机上で確認します。plan、authid、状態、待ち情報を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で catalog、command、utility output、log 関連情報を机上確認できる権限があります。実機では database 名、object 名、thread、utility ID、log data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、Db2 for z/OS の基礎構造、DDL、utility、log、command 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT30  JOB13030 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNV401I THREAD DETAIL REPORT FOLLOWS
DSNV402I PLAN=PAYPLAN AUTHID=USER1 STATUS=INDB2 WAIT=LOCK
DSN9022I -DB2A DISPLAY THREAD NORMAL COMPLETION
DSNV402I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB13030 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に subsystem と対象名を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT30
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNV401I DISPLAY THREAD DETAIL ISSUED
DSNV402I PLAN=PAYPLAN STATUS=INDB2 SSID=DB2A
DSN9022I NORMAL COMPLETION
PLAN=PAYPLAN が SYSLOG に出ていれば、対象操作の証跡を追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNV402I が期待どおりであること
③ ステップ3 の PLAN=PAYPLAN が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>CANCEL THREAD 確認手順</strong></p><p>検証目的: CANCEL THREADとDDF開始停止の応答を確認します。スレッド取消と分散接続口の開閉を混同しないよう、対象IDとDDF状態を分けて見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機では開始・停止・取消・回復系コマンドは変更管理承認を得て、対象SSIDと影響範囲を確認してから実行します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDb2コマンドを入力し、SDSFまたはコマンド応答画面でメッセージと対象名を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象のDb2コマンドを入力します。この操作では入力するコマンドと対象名を確認し、Enterで応答を取得します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -CANCEL THREAD(12345)
Command ===&gt; -START DDF
Command ===&gt; -STOP DDF MODE(SUSPEND)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -CANCEL THREAD(12345)
Command ===&gt; -START DDF
Command ===&gt; -STOP DDF MODE(SUSPEND)
-CANCEL THREAD(12345) が入力欄に表示されていれば、机上例の対象コマンドを実行する準備ができています。対象名やMODE指定が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを確認します。操作欄には追加入力を入れず、応答のメッセージIDと対象名を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNV414I THREAD 12345 CANCEL SCHEDULED
DSNL003I START DDF ACCEPTED
DSNL004I STOP DDF MODE(SUSPEND) ACCEPTED
NORMAL COMPLETION
THREAD 12345 CANCEL SCHEDULED が表示されていれば、机上例では対象コマンドの応答を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、コマンド応答がシステムログにも残っているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNV414I THREAD 12345 CANCEL SCHEDULED
DSNL003I START DDF ACCEPTED
DSNL004I STOP DDF MODE(SUSPEND) ACCEPTED
ISSUER=USER1
THREAD 12345 CANCEL SCHEDULED と ISSUER=USER1 が表示されていれば、誰がどの操作を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの対象名が一致していることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -CANCEL THREAD(12345) が操作（入力）に記載されていること
② ステップ2 の THREAD 12345 CANCEL SCHEDULED が画面・出力に表示されること
③ ステップ2 の NORMAL COMPLETION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY DDF 確認手順</strong></p><p>検証目的: DDF の接続状態を机上で確認します。location、port、active DBAT、queued connection を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で catalog、command、utility output、log 関連情報を机上確認できる権限があります。実機では database 名、object 名、thread、utility ID、log data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、Db2 for z/OS の基礎構造、DDL、utility、log、command 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT30  JOB13030 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNL080I DDF DISPLAY DETAIL REPORT FOLLOWS
DSNL081I LOCATION=DB2A PORT=446 ACTIVE DBAT=238 QUEUED=12
DSN9022I -DB2A DISPLAY DDF NORMAL COMPLETION
DSNL081I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB13030 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に subsystem と対象名を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT30
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL ISSUED
DSNL081I LOCATION=DB2A ACTIVE DBAT=238
DSN9022I NORMAL COMPLETION
ACTIVE DBAT=238 が SYSLOG に出ていれば、対象操作の証跡を追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNL081I が期待どおりであること
③ ステップ3 の ACTIVE DBAT=238 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>MODIFY DDF 確認手順</strong></p><p>検証目的: MODIFY DDFとDISPLAY GROUPの机上応答を確認します。DDF運用属性の変更とData Sharingグループ表示を別の確認点として扱います。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機では開始・停止・取消・回復系コマンドは変更管理承認を得て、対象SSIDと影響範囲を確認してから実行します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDb2コマンドを入力し、SDSFまたはコマンド応答画面でメッセージと対象名を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象のDb2コマンドを入力します。この操作では入力するコマンドと対象名を確認し、Enterで応答を取得します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -MODIFY DDF PKGREL(COMMIT)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -DISPLAY GROUP
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -MODIFY DDF PKGREL(COMMIT)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -DISPLAY GROUP
-MODIFY DDF PKGREL(COMMIT) が入力欄に表示されていれば、机上例の対象コマンドを実行する準備ができています。対象名やMODE指定が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを確認します。操作欄には追加入力を入れず、応答のメッセージIDと対象名を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNL030I MODIFY DDF PKGREL(COMMIT) ACCEPTED
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A TCPPORT=446
DSN7100I DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE
NORMAL COMPLETION
DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE が表示されていれば、机上例では対象コマンドの応答を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、コマンド応答がシステムログにも残っているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL030I MODIFY DDF PKGREL(COMMIT) ACCEPTED
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A TCPPORT=446
DSN7100I DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE
ISSUER=USER1
DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE と ISSUER=USER1 が表示されていれば、誰がどの操作を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの対象名が一致していることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -MODIFY DDF PKGREL(COMMIT) が操作（入力）に記載されていること
② ステップ2 の DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE が画面・出力に表示されること
③ ステップ2 の NORMAL COMPLETION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY GROUP 確認手順</strong></p><p>検証目的: Db2グループのコードレベル、カタログレベル、機能レベルを表示します。移行や共存状態の確認で使うレベル情報を取得します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムの表示系コマンドを実行できる権限があること。表示コマンドのみを使い、停止や変更を伴う操作は行わないこと。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に -DISPLAY GROUP DETAIL を入力し、DISPLAY GROUP の確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; -DISPLAY GROUP DETAIL
→ Enter を押す
［画面・出力］
DSN&gt;
-DISPLAY GROUP DETAIL
DSN7100I -DBD1 DSN7GCMD
*** BEGIN DISPLAY OF GROUP(........) CATALOG LEVEL(V13R1M500)
CURRENT FUNCTION LEVEL(V13R1M500)
HIGHEST ACTIVATED FUNCTION LEVEL(V13R1M500)
DSN9022I -DBD1 DSN7GCMD &#x27;DISPLAY GROUP&#x27; NORMAL COMPLETION
DSN&gt;
DSN7100I と CURRENT FUNCTION LEVEL が表示されていれば、グループ情報を取得できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、表示確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の DSN7100I が表示されること
③ ステップ 2 の CURRENT FUNCTION LEVEL が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY UTILITY 確認手順</strong></p><p>検証目的: Db2が認識しているユーティリティジョブの状態を表示します。保守前に実行中または停止中のユーティリティの有無を記録します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムの表示系コマンドを実行できる権限があること。表示コマンドのみを使い、停止や変更を伴う操作は行わないこと。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DBD1 とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DBD1) を入力し、DBD1のDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DBD1)
DSN&gt;
DSN SYSTEM(DBD1) と DSN&gt; が表示されていれば、DBD1のDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に -DISPLAY UTILITY(*) を入力し、DISPLAY UTILITY の確認に必要な表示を取得します。
［操作（入力）］
DSN ===&gt; -DISPLAY UTILITY(*)
→ Enter を押す
［画面・出力］
DSN&gt;
-DISPLAY UTILITY(*)
DSNU100I -DBD1 DSNUGDIS - USERID = SAMPID
MEMBER = DBD1
UTILID = RUNTS
PROCESSING UTILITY STATEMENT 1
DSN9022I -DBD1 DSNUGCC &#x27;-DISPLAY UTILITY&#x27; NORMAL COMPLETION
DSN&gt;
DSNU100I と UTILID = RUNTS が表示されていれば、ユーティリティ状態の表示結果を取得できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、表示確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の DSNU100I が表示されること
③ ステップ 2 の NORMAL COMPLETION が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>TERM UTILITY 確認手順</strong></p><p>検証目的: TERM UTILITY、ARCHIVE LOG、RECOVER BSDSの応答を確認します。保守ジョブ終了、ログ切替、二重BSDS復旧の対象が異なることを机上例で見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機では開始・停止・取消・回復系コマンドは変更管理承認を得て、対象SSIDと影響範囲を確認してから実行します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDb2コマンドを入力し、SDSFまたはコマンド応答画面でメッセージと対象名を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に対象のDb2コマンドを入力します。この操作では入力するコマンドと対象名を確認し、Enterで応答を取得します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -TERM UTILITY(UTIL0007)
Command ===&gt; -ARCHIVE LOG MODE(QUIESCE)
Command ===&gt; -RECOVER BSDS
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -TERM UTILITY(UTIL0007)
Command ===&gt; -ARCHIVE LOG MODE(QUIESCE)
Command ===&gt; -RECOVER BSDS
-TERM UTILITY(UTIL0007) が入力欄に表示されていれば、机上例の対象コマンドを実行する準備ができています。対象名やMODE指定が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを確認します。操作欄には追加入力を入れず、応答のメッセージIDと対象名を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNU102I TERM UTILITY UTIL0007 ACCEPTED
DSNJ001I ARCHIVE LOG MODE(QUIESCE) ACCEPTED
DSNJ120I RECOVER BSDS RESTORING DUAL BSDS
NORMAL COMPLETION
RECOVER BSDS RESTORING DUAL BSDS が表示されていれば、机上例では対象コマンドの応答を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、コマンド応答がシステムログにも残っているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU102I TERM UTILITY UTIL0007 ACCEPTED
DSNJ001I ARCHIVE LOG MODE(QUIESCE) ACCEPTED
DSNJ120I RECOVER BSDS RESTORING DUAL BSDS
ISSUER=USER1
RECOVER BSDS RESTORING DUAL BSDS と ISSUER=USER1 が表示されていれば、誰がどの操作を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの対象名が一致していることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -TERM UTILITY(UTIL0007) が操作（入力）に記載されていること
② ステップ2 の RECOVER BSDS RESTORING DUAL BSDS が画面・出力に表示されること
③ ステップ2 の NORMAL COMPLETION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Command_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>dual logging 確認手順</strong></p><p>検証目的: ログ二重化とBSDS上のログ範囲確認を机上例で追います。片側障害時に、BSDSとログデータセットの登録内容が一致しているかを見る流れを確認します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2LOG.JCL を編集でき、Db2サブシステム DB2A のログ・回復関連ジョブを机上確認する前提です。実機では更新系・再始動系の操作は変更管理承認とバックアウト計画を用意してから実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでジョブログまたはSYSPRINTを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にログ・回復確認用のJCLを入力します。この操作ではJCL本文だけを作成し、保存コマンドは次のステップで入力します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //LR01 JOB (ACCT),&#x27;DB2LOG&#x27;,CLASS=A,MSGCLASS=X
000002 //PRINT EXEC PGM=DSNJU004
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR01 JOB (ACCT),&#x27;DB2LOG&#x27;,CLASS=A,MSGCLASS=X
000002 //PRINT EXEC PGM=DSNJU004
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面内のプログラム名とSYSIN内容が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加の文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR01 JOB (ACCT),&#x27;DB2LOG&#x27;,CLASS=A,MSGCLASS=X
000002 //PRINT EXEC PGM=DSNJU004
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
*** Member LR01 saved
Member LR01 saved が表示されていれば、JCLが保存されています。画面には検証対象のステートメントが残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2LOG.JCL(LR01)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2LOG.JCL(LR01)&#x27;
→ Enter を押す
［画面・出力］
JOB LR01 SUBMITTED
IKJ56250I JOB LR01(JOB01234) SUBMITTED
JOB LR01 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した LR01 のジョブログを開きます。この操作でログ・回復関連の出力と戻りコードを確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    LR01     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNJU004 PRINT LOG MAP
BSDS=DB2A.BSDS01
ACTIVE LOG COPY1=DB2A.LOGCOPY1.A000001
ACTIVE LOG COPY2=DB2A.LOGCOPY2.A000001
STARTRBA=000000000000 ENDRBA=0000000F0000
DSNU010I DSNUTILB COMPLETED, MAXCC=0
ACTIVE LOG COPY2=DB2A.LOGCOPY2.A000001 が表示されていれば、机上例では確認対象のログ・回復情報を取得できています。MAXCC=0 が表示されることも同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB LR01 SUBMITTED が画面・出力に表示されること
② ステップ4 の ACTIVE LOG COPY2=DB2A.LOGCOPY2.A000001 が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>BSDS 確認手順</strong></p><p>検証目的: BSDS に登録された log 情報を机上で確認します。active log、archive log、checkpoint を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で catalog、command、utility output、log 関連情報を机上確認できる権限があります。実機では database 名、object 名、thread、utility ID、log data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、Db2 for z/OS の基礎構造、DDL、utility、log、command 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; DSNJU004 PRINT LOG MAP FOR DB2A
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; DSNJU004 PRINT LOG MAP FOR DB2A
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT30  JOB13030 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNJ100I BSDS LOG MAP FOR DB2A
DSNJ110I ACTIVE LOG COPY1=DB2A.ACTLOG1 ARCHIVE LOG=DB2A.ARC0007
DSNJ120I CHECKPOINT RBA=0000000009A4
DSNJ100I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB13030 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に subsystem と対象名を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT30
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNJ100I BSDS LOG MAP PRINTED SSID=DB2A
DSNJ110I ARCHIVE LOG=DB2A.ARC0007
DSNJ120I CHECKPOINT RBA=0000000009A4
ARCHIVE LOG=DB2A.ARC0007 が SYSLOG に出ていれば、対象操作の証跡を追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNJ100I が期待どおりであること
③ ステップ3 の ARCHIVE LOG=DB2A.ARC0007 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNJU003 確認手順</strong></p><p>検証目的: BSDS更新ユーティリティと印刷ユーティリティの使い分けを確認します。変更作業の前後で、目録更新と印刷確認を分けて扱うことを机上例で示します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2LOG.JCL を編集でき、Db2サブシステム DB2A のログ・回復関連ジョブを机上確認する前提です。実機では更新系・再始動系の操作は変更管理承認とバックアウト計画を用意してから実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでジョブログまたはSYSPRINTを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にログ・回復確認用のJCLを入力します。この操作ではJCL本文だけを作成し、保存コマンドは次のステップで入力します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //LR02 JOB (ACCT),&#x27;BSDSMAP&#x27;,CLASS=A,MSGCLASS=X
000002 //CHG EXEC PGM=DSNJU003
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=OLD,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
000006 //SYSIN DD *
000007   DDF LOCATION=DB2A
000008 /*
000009 //PRT EXEC PGM=DSNJU004
000010 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000011 //SYSPRINT DD SYSOUT=*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR02 JOB (ACCT),&#x27;BSDSMAP&#x27;,CLASS=A,MSGCLASS=X
000002 //CHG EXEC PGM=DSNJU003
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=OLD,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
000006 //SYSIN DD *
000007   DDF LOCATION=DB2A
000008 /*
000009 //PRT EXEC PGM=DSNJU004
000010 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000011 //SYSPRINT DD SYSOUT=*
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面内のプログラム名とSYSIN内容が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加の文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR02 JOB (ACCT),&#x27;BSDSMAP&#x27;,CLASS=A,MSGCLASS=X
000002 //CHG EXEC PGM=DSNJU003
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=OLD,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
000006 //SYSIN DD *
000007   DDF LOCATION=DB2A
000008 /*
000009 //PRT EXEC PGM=DSNJU004
000010 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000011 //SYSPRINT DD SYSOUT=*
*** Member LR02 saved
Member LR02 saved が表示されていれば、JCLが保存されています。画面には検証対象のステートメントが残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2LOG.JCL(LR02)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2LOG.JCL(LR02)&#x27;
→ Enter を押す
［画面・出力］
JOB LR02 SUBMITTED
IKJ56250I JOB LR02(JOB01234) SUBMITTED
JOB LR02 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した LR02 のジョブログを開きます。この操作でログ・回復関連の出力と戻りコードを確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    LR02     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNJU003 CHANGE LOG INVENTORY
DDF LOCATION=DB2A
DSNJU004 PRINT LOG MAP
LOCATION=DB2A
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNJU003 CHANGE LOG INVENTORY が表示されていれば、机上例では確認対象のログ・回復情報を取得できています。MAXCC=0 が表示されることも同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB LR02 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNJU003 CHANGE LOG INVENTORY が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>conditional restart control record 確認手順</strong></p><p>検証目的: 条件付き再始動で使うENDRBA、RBA、LRSNの見方を確認します。停止点を扱う値が、単なるジョブIDやSQL名ではなくログ順序を示す値であることを整理します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2LOG.JCL を編集でき、Db2サブシステム DB2A のログ・回復関連ジョブを机上確認する前提です。実機では更新系・再始動系の操作は変更管理承認とバックアウト計画を用意してから実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでジョブログまたはSYSPRINTを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にログ・回復確認用のJCLを入力します。この操作ではJCL本文だけを作成し、保存コマンドは次のステップで入力します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //LR03 JOB (ACCT),&#x27;CRCR&#x27;,CLASS=A,MSGCLASS=X
000002 //PRINT EXEC PGM=DSNJU004
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR03 JOB (ACCT),&#x27;CRCR&#x27;,CLASS=A,MSGCLASS=X
000002 //PRINT EXEC PGM=DSNJU004
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面内のプログラム名とSYSIN内容が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加の文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR03 JOB (ACCT),&#x27;CRCR&#x27;,CLASS=A,MSGCLASS=X
000002 //PRINT EXEC PGM=DSNJU004
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSUT1 DD DISP=SHR,DSN=DB2A.BSDS01
000005 //SYSPRINT DD SYSOUT=*
*** Member LR03 saved
Member LR03 saved が表示されていれば、JCLが保存されています。画面には検証対象のステートメントが残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2LOG.JCL(LR03)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2LOG.JCL(LR03)&#x27;
→ Enter を押す
［画面・出力］
JOB LR03 SUBMITTED
IKJ56250I JOB LR03(JOB01234) SUBMITTED
JOB LR03 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した LR03 のジョブログを開きます。この操作でログ・回復関連の出力と戻りコードを確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    LR03     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNJU004 PRINT LOG MAP
CHECKPOINT RBA=000000000123
ENDRBA=000000000456
LRSN=00D7F3A4B501
DSNU010I DSNUTILB COMPLETED, MAXCC=0
ENDRBA=000000000456 が表示されていれば、机上例では確認対象のログ・回復情報を取得できています。MAXCC=0 が表示されることも同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB LR03 SUBMITTED が画面・出力に表示されること
② ステップ4 の ENDRBA=000000000456 が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>image copy 確認手順</strong></p><p>検証目的: イメージコピーを基点にした時点指定回復の流れを確認します。REPORT RECOVERYで必要なコピーとログ停止点を見てから、RECOVERのTOLOGPOINTを読む形にします。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2LOG.JCL を編集でき、Db2サブシステム DB2A のログ・回復関連ジョブを机上確認する前提です。実機では更新系・再始動系の操作は変更管理承認とバックアウト計画を用意してから実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでジョブログまたはSYSPRINTを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にログ・回復確認用のJCLを入力します。この操作ではJCL本文だけを作成し、保存コマンドは次のステップで入力します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //LR04 JOB (ACCT),&#x27;PITRCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,LR04&#x27;
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSIN DD *
000005   REPORT RECOVERY TABLESPACE PAYDB.PAYTS
000006   RECOVER TABLESPACE PAYDB.PAYTS TOLOGPOINT X&#x27;000000000789&#x27;
000007 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR04 JOB (ACCT),&#x27;PITRCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,LR04&#x27;
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSIN DD *
000005   REPORT RECOVERY TABLESPACE PAYDB.PAYTS
000006   RECOVER TABLESPACE PAYDB.PAYTS TOLOGPOINT X&#x27;000000000789&#x27;
000007 /*
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面内のプログラム名とSYSIN内容が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加の文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR04 JOB (ACCT),&#x27;PITRCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,LR04&#x27;
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSIN DD *
000005   REPORT RECOVERY TABLESPACE PAYDB.PAYTS
000006   RECOVER TABLESPACE PAYDB.PAYTS TOLOGPOINT X&#x27;000000000789&#x27;
000007 /*
*** Member LR04 saved
Member LR04 saved が表示されていれば、JCLが保存されています。画面には検証対象のステートメントが残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2LOG.JCL(LR04)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2LOG.JCL(LR04)&#x27;
→ Enter を押す
［画面・出力］
JOB LR04 SUBMITTED
IKJ56250I JOB LR04(JOB01234) SUBMITTED
JOB LR04 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した LR04 のジョブログを開きます。この操作でログ・回復関連の出力と戻りコードを確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    LR04     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
REPORT RECOVERY TABLESPACE=PAYDB.PAYTS
IMAGE COPY PITLRSN=000000000700
RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000789&#x27;
DSNU010I DSNUTILB COMPLETED, MAXCC=0
RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000789&#x27; が表示されていれば、机上例では確認対象のログ・回復情報を取得できています。MAXCC=0 が表示されることも同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB LR04 SUBMITTED が画面・出力に表示されること
② ステップ4 の RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000789&#x27; が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>catalog and directory recovery 確認手順</strong></p><p>検証目的: カタログ・ディレクトリ回復、ページ回復、ログ障害後の再始動確認をひとつの保守シナリオとして整理します。BSDS印刷、保守アクセス、回復対象確認を分けて見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2LOG.JCL を編集でき、Db2サブシステム DB2A のログ・回復関連ジョブを机上確認する前提です。実機では更新系・再始動系の操作は変更管理承認とバックアウト計画を用意してから実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでジョブログまたはSYSPRINTを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にログ・回復確認用のJCLを入力します。この操作ではJCL本文だけを作成し、保存コマンドは次のステップで入力します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //LR05 JOB (ACCT),&#x27;CATRCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,LR05&#x27;
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSIN DD *
000005   REPORT RECOVERY TABLESPACE DSNDB06.SYSCOPY
000006   RECOVER TABLESPACE DSNDB06.SYSCOPY
000007   RECOVER TABLESPACE PAYDB.PAYTS PAGE(000001)
000008 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR05 JOB (ACCT),&#x27;CATRCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,LR05&#x27;
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSIN DD *
000005   REPORT RECOVERY TABLESPACE DSNDB06.SYSCOPY
000006   RECOVER TABLESPACE DSNDB06.SYSCOPY
000007   RECOVER TABLESPACE PAYDB.PAYTS PAGE(000001)
000008 /*
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面内のプログラム名とSYSIN内容が検証対象と一致していることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加の文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //LR05 JOB (ACCT),&#x27;CATRCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,LR05&#x27;
000003 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000004 //SYSIN DD *
000005   REPORT RECOVERY TABLESPACE DSNDB06.SYSCOPY
000006   RECOVER TABLESPACE DSNDB06.SYSCOPY
000007   RECOVER TABLESPACE PAYDB.PAYTS PAGE(000001)
000008 /*
*** Member LR05 saved
Member LR05 saved が表示されていれば、JCLが保存されています。画面には検証対象のステートメントが残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2LOG.JCL(LR05)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2LOG.JCL(LR05)&#x27;
→ Enter を押す
［画面・出力］
JOB LR05 SUBMITTED
IKJ56250I JOB LR05(JOB01234) SUBMITTED
JOB LR05 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した LR05 のジョブログを開きます。この操作でログ・回復関連の出力と戻りコードを確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    LR05     JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
REPORT RECOVERY TABLESPACE=DSNDB06.SYSCOPY
RECOVER TABLESPACE=DSNDB06.SYSCOPY
RECOVER TABLESPACE=PAYDB.PAYTS PAGE=000001
DSNU010I DSNUTILB COMPLETED, MAXCC=0
REPORT RECOVERY TABLESPACE=DSNDB06.SYSCOPY が表示されていれば、机上例では確認対象のログ・回復情報を取得できています。MAXCC=0 が表示されることも同じ画面で確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB LR05 SUBMITTED が画面・出力に表示されること
② ステップ4 の REPORT RECOVERY TABLESPACE=DSNDB06.SYSCOPY が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>data sharing group 確認手順</strong></p><p>検証目的: Data Sharingグループに属するメンバーの稼働状態を確認します。障害時の影響範囲や再始動対象を決める前に、ACTIVEのメンバーを把握します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムまたはグループ接続名に接続できる権限があること。表示コマンドを実行するだけの確認手順であり、START、STOP、SETXCF FORCEなど状態変更を伴う操作は実施しないこと。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2コマンドの表示結果を確認する。ここでは机上例としてDBD1、DBD2、DB2G、GBP0、DSNDB06を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。READYのコマンド入力口に DSN SYSTEM(DBD1) を入力し、対象Db2へ入るためにDSNコマンドプロセッサを起動します。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できるDSN画面へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY GROUP DETAIL を入力し、Data Sharingグループ状態確認の状態を表示します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY GROUP DETAIL
→ Enter を押す
［画面・出力］
DSN7100I -DBD1 DSN7GCMD
GROUP NAME: DB2G
MEMBER NAME  STATUS    SUBSYSTEM
DBD1         ACTIVE    DBD1
DBD2         ACTIVE    DBD2
GROUP ATTACH NAME: DB2G
DSN9022I -DBD1 DSN7GCMD &#x27;DISPLAY GROUP&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
DBD1 DBD2 ACTIVE DSN9022I が画面・出力に表示されていれば、Data Sharingグループ状態確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の DBD1 DBD2 ACTIVE DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>group attach 確認手順</strong></p><p>検証目的: 個別メンバー名ではなくグループ接続名でDb2へ入れるかを確認します。アプリケーション接続を特定メンバーへ固定しない設計の前提確認に使います。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムまたはグループ接続名に接続できる権限があること。表示コマンドを実行するだけの確認手順であり、START、STOP、SETXCF FORCEなど状態変更を伴う操作は実施しないこと。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2コマンドの表示結果を確認する。ここでは机上例としてDBD1、DBD2、DB2G、GBP0、DSNDB06を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。READYのコマンド入力口に DSN SYSTEM(DB2G) を入力し、対象Db2へ入るためにDSNコマンドプロセッサを起動します。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DB2G)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できるDSN画面へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY GROUP DETAIL を入力し、group attach接続確認の状態を表示します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY GROUP DETAIL
→ Enter を押す
［画面・出力］
DSN7100I -DBD1 DSN7GCMD
GROUP NAME: DB2G
MEMBER NAME  STATUS    SUBSYSTEM
DBD1         ACTIVE    DBD1
DBD2         ACTIVE    DBD2
DSN9022I -DBD1 DSN7GCMD &#x27;DISPLAY GROUP&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
DB2G ACTIVE DSN9022I が画面・出力に表示されていれば、group attach接続確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の DB2G ACTIVE DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>group buffer pool 確認手順</strong></p><p>検証目的: 対象group buffer poolにどのDb2メンバーが接続しているかを確認します。共有バッファを使うページセットの調査前に、GBP0への接続状態を把握します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムまたはグループ接続名に接続できる権限があること。表示コマンドを実行するだけの確認手順であり、START、STOP、SETXCF FORCEなど状態変更を伴う操作は実施しないこと。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2コマンドの表示結果を確認する。ここでは机上例としてDBD1、DBD2、DB2G、GBP0、DSNDB06を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。READYのコマンド入力口に DSN SYSTEM(DBD1) を入力し、対象Db2へ入るためにDSNコマンドプロセッサを起動します。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できるDSN画面へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY GROUPBUFFERPOOL(GBP0) TYPE(GCONN) を入力し、group buffer pool接続確認の状態を表示します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY GROUPBUFFERPOOL(GBP0) TYPE(GCONN)
→ Enter を押す
［画面・出力］
DSNB750I -DBD1 DISPLAY FOR GROUP BUFFER POOL GBP0
DSNB756I -DBD1 MEMBER DBD1 IS CONNECTED TO GBP0
DSNB756I -DBD1 MEMBER DBD2 IS CONNECTED TO GBP0
DSNB790I -DISPLAY FOR GROUP BUFFER POOL GBP0 IS COMPLETE
DSN9022I -DBD1 DSNB1CMD &#x27;DISPLAY GROUPBUFFERPOOL&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
GBP0 DBD1 DBD2 DSN9022I が画面・出力に表示されていれば、group buffer pool接続確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の GBP0 DBD1 DBD2 DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>global contention 確認手順</strong></p><p>検証目的: Data Sharing環境でグローバルロックの存在を確認します。複数メンバー間の待ち合わせを調べる前に、LOCKS ONLYの表示結果を証跡として残します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムまたはグループ接続名に接続できる権限があること。表示コマンドを実行するだけの確認手順であり、START、STOP、SETXCF FORCEなど状態変更を伴う操作は実施しないこと。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2コマンドの表示結果を確認する。ここでは机上例としてDBD1、DBD2、DB2G、GBP0、DSNDB06を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。READYのコマンド入力口に DSN SYSTEM(DBD1) を入力し、対象Db2へ入るためにDSNコマンドプロセッサを起動します。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できるDSN画面へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY DATABASE(DSNDB06) SPACENAM(*) LOCKS ONLY を入力し、グローバルロック表示確認の状態を表示します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY DATABASE(DSNDB06) SPACENAM(*) LOCKS ONLY
→ Enter を押す
［画面・出力］
DSNT360I -DBD1 ****************************************************
DSNT361I -DBD1 * DISPLAY DATABASE SUMMARY
DSNT361I -DBD1 * GLOBAL LOCKS
DATABASE = DSNDB06  SPACE = SYSTSDBA  MEMBER = DBD2
DSNT360I -DBD1 ****************************************************
DSN9022I -DBD1 DSNTDDIS &#x27;DISPLAY DATABASE&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
GLOBAL LOCKS DSNDB06 DBD2 DSN9022I が画面・出力に表示されていれば、グローバルロック表示確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の GLOBAL LOCKS DSNDB06 DBD2 DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>castout 確認手順</strong></p><p>検証目的: group buffer poolのcastout関連統計を確認します。GBP内の変更ページ書き出しが遅れていないかを判断するため、GDETAILの表示を記録します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムまたはグループ接続名に接続できる権限があること。表示コマンドを実行するだけの確認手順であり、START、STOP、SETXCF FORCEなど状態変更を伴う操作は実施しないこと。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2コマンドの表示結果を確認する。ここでは机上例としてDBD1、DBD2、DB2G、GBP0、DSNDB06を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。READYのコマンド入力口に DSN SYSTEM(DBD1) を入力し、対象Db2へ入るためにDSNコマンドプロセッサを起動します。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できるDSN画面へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY GROUPBUFFERPOOL(GBP0) GDETAIL を入力し、castout統計確認の状態を表示します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY GROUPBUFFERPOOL(GBP0) GDETAIL
→ Enter を押す
［画面・出力］
DSNB750I -DBD1 DISPLAY FOR GROUP BUFFER POOL GBP0
DSNB771I -DBD1 GROUP DETAIL STATISTICS FOR GBP0
CASTOUTS INITIATED = 00000042
DATA ENTRIES IN USE = 00001280
DSNB790I -DISPLAY FOR GROUP BUFFER POOL GBP0 IS COMPLETE
DSN9022I -DBD1 DSNB1CMD &#x27;DISPLAY GROUPBUFFERPOOL&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
CASTOUTS GBP0 DSN9022I が画面・出力に表示されていれば、castout統計確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の CASTOUTS GBP0 DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>buffer pool 確認手順</strong></p><p>検証目的: buffer pool の稼働値を机上で確認します。hit ratio、read、page steal を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で catalog、command、utility output、log 関連情報を机上確認できる権限があります。実機では database 名、object 名、thread、utility ID、log data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、Db2 for z/OS の基礎構造、DDL、utility、log、command 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY BUFFERPOOL(BP8K0) DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY BUFFERPOOL(BP8K0) DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT30  JOB13030 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNB401I BUFFERPOOL BP8K0 DETAIL REPORT
DSNB402I HITRATIO=93 SYNCREAD=184 PAGESTEAL=44
DSN9022I -DB2A DISPLAY BUFFERPOOL NORMAL COMPLETION
DSNB402I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB13030 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に subsystem と対象名を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT30
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNB401I DISPLAY BUFFERPOOL BP8K0 DETAIL
DSNB402I HITRATIO=93 SSID=DB2A
DSN9022I NORMAL COMPLETION
HITRATIO=93 が SYSLOG に出ていれば、対象操作の証跡を追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNB402I が期待どおりであること
③ ステップ3 の HITRATIO=93 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>VPSIZE 確認手順</strong></p><p>検証目的: BP8K0 の VPSIZE 変更結果を机上で確認します。対象 pool、変更前後の値、完了メッセージを照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で buffer pool、lock、page set 状態を確認できる権限があります。実機では pool 名、database 名、table space 名、utility ID を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、バッファ・ストレージ・ロック領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command または utility 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -ALTER BUFFERPOOL(BP8K0) VPSIZE(40000)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -ALTER BUFFERPOOL(BP8K0) VPSIZE(40000)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT26  JOB12626 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNB401I BUFFERPOOL BP8K0 ALTER ACCEPTED
DSNB402I BP8K0 VPSIZE OLD=30000 NEW=40000
DSN9022I -DB2A DSNB ALTER BUFFERPOOL NORMAL COMPLETION
DSNB402I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12626 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT26
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNB401I ALTER BUFFERPOOL BP8K0 ISSUED
DSNB402I BP8K0 VPSIZE=40000 SSID=DB2A
DSN9022I NORMAL COMPLETION
VPSIZE=40000 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNB402I が期待どおりであること
③ ステップ 3 の VPSIZE=40000 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>EDM pool 確認手順</strong></p><p>検証目的: EDM pool の保持効率を机上で確認します。hit ratio、failure、statement cache の関連値を読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で buffer pool、lock、page set 状態を確認できる権限があります。実機では pool 名、database 名、table space 名、utility ID を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、バッファ・ストレージ・ロック領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command または utility 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(EDMPOOL)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(EDMPOOL)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT26  JOB12626 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSND100I EDMPOOL STATISTICS REPORT
DSND101I HITRATIO=96 FAILURES=0 DBD=1840 PACKAGES=920
DSN9022I -DB2A DISPLAY STATS NORMAL COMPLETION
DSND101I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12626 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT26
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSND100I DISPLAY STATS EDMPOOL ISSUED
DSND101I HITRATIO=96 SSID=DB2A
DSN9022I NORMAL COMPLETION
HITRATIO=96 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSND101I が期待どおりであること
③ ステップ 3 の HITRATIO=96 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>IRLMRWT 確認手順</strong></p><p>検証目的: resource timeout の基準値を机上で確認します。IRLMRWT、対象 subsystem、変更可否の証跡を読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で buffer pool、lock、page set 状態を確認できる権限があります。実機では pool 名、database 名、table space 名、utility ID を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、バッファ・ストレージ・ロック領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command または utility 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) TYPE(SYSTEM)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) TYPE(SYSTEM)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT26  JOB12626 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNV401I THREAD DISPLAY REPORT FOLLOWS
DSNV402I IRLMRWT=30 RESOURCE TIMEOUT SECONDS
DSN9022I -DB2A DISPLAY THREAD NORMAL COMPLETION
DSNV402I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12626 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT26
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNV401I DISPLAY THREAD ISSUED
DSNV402I IRLMRWT=30 SSID=DB2A
DSN9022I NORMAL COMPLETION
IRLMRWT=30 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNV402I が期待どおりであること
③ ステップ 3 の IRLMRWT=30 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>group buffer pool read/write 確認手順</strong></p><p>検証目的: data sharing の group buffer pool read/write を机上で確認します。GBP 名、read hit、write、castout の値を読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で buffer pool、lock、page set 状態を確認できる権限があります。実機では pool 名、database 名、table space 名、utility ID を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、バッファ・ストレージ・ロック領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command または utility 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY GROUPBUFFERPOOL(GBP0) DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY GROUPBUFFERPOOL(GBP0) DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT26  JOB12626 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNB750I GBP0 DETAIL REPORT FOLLOWS
DSNB751I READS=1200 WRITES=340 CASTOUTS=22
DSNB752I DUPLEX=YES STATUS=ACTIVE
DSN9022I -DB2A DISPLAY GBP NORMAL COMPLETION
DSNB751I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12626 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT26
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNB750I DISPLAY GROUPBUFFERPOOL GBP0
DSNB752I GBP0 STATUS=ACTIVE SSID=DB2A
DSN9022I NORMAL COMPLETION
GBP0 STATUS=ACTIVE が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNB751I が期待どおりであること
③ ステップ 3 の GBP0 STATUS=ACTIVE が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>page set status 確認手順</strong></p><p>検証目的: table space の page set status を机上で確認します。DISPLAY DATABASE の状態行と pending 表示を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で buffer pool、lock、page set 状態を確認できる権限があります。実機では pool 名、database 名、table space 名、utility ID を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、バッファ・ストレージ・ロック領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command または utility 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DATABASE(DBPAY) SPACENAM(TSPAY)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DATABASE(DBPAY) SPACENAM(TSPAY)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT26  JOB12626 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT360I DATABASE DBPAY SPACENAM TSPAY STATUS
DSNT361I STATUS=RW COPY-PENDING=NO CHECK-PENDING=NO
DSN9022I -DB2A DISPLAY DATABASE NORMAL COMPLETION
DSNT361I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12626 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT26
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT360I DISPLAY DATABASE DBPAY TSPAY
DSNT361I STATUS=RW SSID=DB2A
DSN9022I NORMAL COMPLETION
STATUS=RW が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNT361I が期待どおりであること
③ ステップ 3 の STATUS=RW が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>EXPLAIN 確認手順</strong></p><p>検証目的: EXPLAIN の結果を机上で確認します。query number、PLAN_TABLE 行、利用 index を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で EXPLAIN、trace 表示、monitoring 出力を確認できる権限があります。実機では query number、trace number、plan 名、report 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、性能・モニタリング・トレース領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command、SQL、または trace 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; EXPLAIN PLAN SET QUERYNO = 2701 FOR SELECT * FROM PAYROLL.EMP WHERE EMPNO = &#x27;A001&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; EXPLAIN PLAN SET QUERYNO = 2701 FOR SELECT * FROM PAYROLL.EMP WHERE EMPNO = &#x27;A001&#x27;
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT27  JOB12727 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = 0, EXPLAIN SUCCESSFUL QUERYNO=2701
DSNT418I PLAN_TABLE ROW INSERTED METHOD=INDEX ACCESSNAME=IXEMP01
DSN9022I -DB2A EXPLAIN NORMAL COMPLETION
DSNT408I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12727 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT27
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I EXPLAIN QUERYNO=2701 SQLCODE=0
DSNT418I ACCESSNAME=IXEMP01 SSID=DB2A
DSN9022I NORMAL COMPLETION
ACCESSNAME=IXEMP01 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNT408I が期待どおりであること
③ ステップ 3 の ACCESSNAME=IXEMP01 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>performance trace 確認手順</strong></p><p>検証目的: START TRACE(PERFM) の受け付けと trace number を机上で確認します。class、IFCID、出力先を読み取ります。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で EXPLAIN、trace 表示、monitoring 出力を確認できる権限があります。実機では query number、trace number、plan 名、report 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、性能・モニタリング・トレース領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command、SQL、または trace 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -START TRACE(PERFM) CLASS(3) IFCID(199) DEST(GTF)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -START TRACE(PERFM) CLASS(3) IFCID(199) DEST(GTF)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT27  JOB12727 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNW127I START TRACE ACCEPTED TRACE NUMBER 05
DSNW130I TRACE TYPE=PERFM CLASS=3 IFCID=199 DEST=GTF
DSN9022I -DB2A START TRACE NORMAL COMPLETION
DSNW127I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12727 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT27
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNW127I START TRACE PERFM TRACE NUMBER 05
DSNW130I IFCID=199 SSID=DB2A
DSN9022I NORMAL COMPLETION
IFCID=199 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNW127I が期待どおりであること
③ ステップ 3 の IFCID=199 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>buffer pool report 確認手順</strong></p><p>検証目的: buffer pool report の主要値を机上で確認します。hit ratio、synchronous read、page steal を読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で EXPLAIN、trace 表示、monitoring 出力を確認できる権限があります。実機では query number、trace number、plan 名、report 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、性能・モニタリング・トレース領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command、SQL、または trace 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY BUFFERPOOL(BP8K0) DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY BUFFERPOOL(BP8K0) DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT27  JOB12727 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNB401I BUFFERPOOL BP8K0 DETAIL REPORT
DSNB402I HITRATIO=93 SYNCREAD=184 PAGESTEAL=44
DSN9022I -DB2A DISPLAY BUFFERPOOL NORMAL COMPLETION
DSNB402I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12727 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT27
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNB401I DISPLAY BUFFERPOOL BP8K0 DETAIL
DSNB402I HITRATIO=93 SSID=DB2A
DSN9022I NORMAL COMPLETION
HITRATIO=93 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNB402I が期待どおりであること
③ ステップ 3 の HITRATIO=93 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>thread wait analysis 確認手順</strong></p><p>検証目的: thread wait analysis の出力を机上で確認します。class 3 suspension、lock wait、I/O wait を分けて読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で EXPLAIN、trace 表示、monitoring 出力を確認できる権限があります。実機では query number、trace number、plan 名、report 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、性能・モニタリング・トレース領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command、SQL、または trace 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT27  JOB12727 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNV401I THREAD DETAIL REPORT FOLLOWS
DSNV402I PLAN=PAYPLAN CLASS3=1.280 LOCKWAIT=0.410 IOWAIT=0.620
DSN9022I -DB2A DISPLAY THREAD NORMAL COMPLETION
DSNV402I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12727 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT27
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNV401I DISPLAY THREAD DETAIL ISSUED
DSNV402I PLAN=PAYPLAN CLASS3=1.280 SSID=DB2A
DSN9022I NORMAL COMPLETION
PLAN=PAYPLAN が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNV402I が期待どおりであること
③ ステップ 3 の PLAN=PAYPLAN が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>DBAT monitoring 確認手順</strong></p><p>検証目的: DDF 経由 workload の DBAT 状態を机上で確認します。active DBAT、MAXDBAT、queued connection を読みます。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で EXPLAIN、trace 表示、monitoring 出力を確認できる権限があります。実機では query number、trace number、plan 名、report 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、性能・モニタリング・トレース領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の command、SQL、または trace 指示を入力し、対象名と操作内容を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した指示を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT27  JOB12727 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNL080I DDF DISPLAY DETAIL REPORT FOLLOWS
DSNL081I MAXDBAT=400 ACTIVE DBAT=238 QUEUED=12
DSN9022I -DB2A DISPLAY DDF NORMAL COMPLETION
DSNL081I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12727 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作者と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT27
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL ISSUED
DSNL081I ACTIVE DBAT=238 SSID=DB2A
DSN9022I NORMAL COMPLETION
ACTIVE DBAT=238 が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ 1 の DSNT400I が表示されていること
② ステップ 2 の DSNL081I が期待どおりであること
③ ステップ 3 の ACTIVE DBAT=238 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference</p></div><div class="kb-p"><p class="kb-pname"><strong>location name 確認手順</strong></p><p>検証目的: DISPLAY LOCATION INCOMPLTで、DDF開始後に不完全接続として終了したリモートロケーションと接続数を表示し、location nameの実表示を確認します。</p><p>前提条件: TSOログオン済で、対象Db2サブシステムの表示系コマンドを実行できる権限があること。表示コマンドのみを使い、停止や変更を伴う操作は行わないこと。</p><p>セッション環境: TSO/ISPF から DSN コマンドで Db2コマンドプロセッサに入る。対象サブシステム名は DB2A とする。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO/ISPFのコマンド入力画面です。Command ===&gt; に TSO DSN SYSTEM(DB2A) を入力し、DB2AのDb2コマンドプロセッサへ接続します。
［操作（入力）］
Command ===&gt; TSO DSN SYSTEM(DB2A)
→ Enter を押す
［画面・出力］
DSN
DSN SYSTEM(DB2A)
DSN&gt;
DSN SYSTEM(DB2A) と DSN&gt; が表示されていれば、DB2AのDb2コマンドプロセッサへ入れています。
――――
■ ステップ 2
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に-DISPLAY LOCATION INCOMPLTを入力し、不完全接続として終了したロケーションを表示します。
［操作（入力）］
DSN ===&gt; -DISPLAY LOCATION INCOMPLT
→ Enter を押す
［画面・出力］
DSN&gt;
-DISPLAY LOCATION INCOMPLT
DSNL200I -DB2A DISPLAY LOCATION REPORT FOLLOWS-
       LOCATION                    CONNS
       ::10.1.43.29                    47
       ::10.1.24.149                   60
DISPLAY LOCATION REPORT COMPLETE
DSN&gt;
DSNL200IにLOCATIONとCONNSが表示され、末尾のDISPLAY LOCATION REPORT COMPLETEまで取得できています。
――――
■ ステップ 3
現在の画面はDb2コマンドプロセッサです。DSN ===&gt; に END を入力し、表示確認を終えてTSOのREADY状態へ戻します。
［操作（入力）］
DSN ===&gt; END
→ Enter を押す
［画面・出力］
DSN&gt;
END
READY
READY が表示されていれば、Db2コマンドプロセッサを終了できています。
――――</pre><p>合格条件: ① ステップ 1 の DSN&gt; が表示されること
② ステップ 2 の DSNL200I が表示されること
③ ステップ 2 の DISPLAY LOCATION REPORT COMPLETE が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>dynamic location alias 確認手順</strong></p><p>検証目的: DDFのロケーション別名が定義済みで、開始状態か停止状態かを確認します。MODIFY DDFで変更する前に、表示結果でALIAS1の状態とポートを記録します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムの表示コマンドを実行できる権限があること。DDFを停止・開始・変更する操作は行わず、表示結果だけを確認すること。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2表示コマンドでDDF状態を確認する。ここでは机上例としてDBD1、DBD2、DB2G、ALIAS1、446、448、5020を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に DSN SYSTEM(DBD1) を入力し、対象Db2のコマンドプロセッサへ入ります。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できる状態へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY DDF DETAIL を入力し、動的ロケーション別名状態確認の表示結果を取得します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
DSNL080I -DBD1 DSNLTDDF DISPLAY DDF REPORT FOLLOWS
DSNL096I -DBD1 LOCATION ALIAS ALIAS1 STATUS=STARTD PORT=1446 SECPORT=1448
DSNL099I -DBD1 DSNLTDDF DISPLAY DDF REPORT COMPLETE
DSN9022I -DBD1 DSNLTDDF &#x27;DISPLAY DDF&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
ALIAS1 STARTD PORT DSN9022I が画面・出力に表示されていれば、動的ロケーション別名状態確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の ALIAS1 STARTD PORT DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>MAXDBAT 確認手順</strong></p><p>検証目的: DDFのスレッド上限と接続受付可否を確認します。MAXDBATが0でないこと、DBAT関連値が期待範囲にあることをDISPLAY DDF DETAILで記録します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムの表示コマンドを実行できる権限があること。DDFを停止・開始・変更する操作は行わず、表示結果だけを確認すること。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2表示コマンドでDDF状態を確認する。ここでは机上例としてDBD1、DBD2、DB2G、ALIAS1、446、448、5020を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に DSN SYSTEM(DBD1) を入力し、対象Db2のコマンドプロセッサへ入ります。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できる状態へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY DDF DETAIL を入力し、MAXDBATとDBAT状態確認の表示結果を取得します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
DSNL080I -DBD1 DSNLTDDF DISPLAY DDF REPORT FOLLOWS
DSNL090I -DBD1 TCPPORT=446 SECPORT=448 RESPORT=5020
DSNL092I -DBD1 MAXDBAT=200 CONDBAT=1000 CMTSTAT=INACTIVE
DSNL099I -DBD1 DSNLTDDF DISPLAY DDF REPORT COMPLETE
DSN9022I -DBD1 DSNLTDDF &#x27;DISPLAY DDF&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
MAXDBAT CMTSTAT DSN9022I が画面・出力に表示されていれば、MAXDBATとDBAT状態確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の MAXDBAT CMTSTAT DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>AT-TLS/SSL 確認手順</strong></p><p>検証目的: secure portと暗号化接続の入口を確認します。SECPORTが有効な値を持つかをDISPLAY DDF DETAILで確認し、AT-TLSやSSL設定の調査へ進む前の証跡にします。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムの表示コマンドを実行できる権限があること。DDFを停止・開始・変更する操作は行わず、表示結果だけを確認すること。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2表示コマンドでDDF状態を確認する。ここでは机上例としてDBD1、DBD2、DB2G、ALIAS1、446、448、5020を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に DSN SYSTEM(DBD1) を入力し、対象Db2のコマンドプロセッサへ入ります。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できる状態へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY DDF DETAIL を入力し、セキュア接続入口確認の表示結果を取得します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
DSNL080I -DBD1 DSNLTDDF DISPLAY DDF REPORT FOLLOWS
DSNL090I -DBD1 TCPPORT=446 SECPORT=448 RESPORT=5020
DSNL094I -DBD1 SECURE SQL LISTENER IS ACTIVE
DSNL099I -DBD1 DSNLTDDF DISPLAY DDF REPORT COMPLETE
DSN9022I -DBD1 DSNLTDDF &#x27;DISPLAY DDF&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
SECPORT SECURE DSN9022I が画面・出力に表示されていれば、セキュア接続入口確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の SECPORT SECURE DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>two-phase commit resynchronization 確認手順</strong></p><p>検証目的: two-phase commit resynchronizationで使うresync portを確認します。分散更新障害の調査前に、RESPORTの値とDDF状態を証跡化します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムの表示コマンドを実行できる権限があること。DDFを停止・開始・変更する操作は行わず、表示結果だけを確認すること。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2表示コマンドでDDF状態を確認する。ここでは机上例としてDBD1、DBD2、DB2G、ALIAS1、446、448、5020を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に DSN SYSTEM(DBD1) を入力し、対象Db2のコマンドプロセッサへ入ります。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できる状態へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY DDF DETAIL を入力し、二相コミット再同期入口確認の表示結果を取得します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
DSNL080I -DBD1 DSNLTDDF DISPLAY DDF REPORT FOLLOWS
DSNL090I -DBD1 TCPPORT=446 SECPORT=448 RESPORT=5020
DSNL093I -DBD1 RESYNC PORT IS ACTIVE
DSNL099I -DBD1 DSNLTDDF DISPLAY DDF REPORT COMPLETE
DSN9022I -DBD1 DSNLTDDF &#x27;DISPLAY DDF&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
RESPORT RESYNC DSN9022I が画面・出力に表示されていれば、二相コミット再同期入口確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の RESPORT RESYNC DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY DDF output 確認手順</strong></p><p>検証目的: DDFの開始状態、主ポート、secure port、resync portをまとめて確認します。分散接続障害の一次証跡として、DSNL080I、DSNL090I、DSNL099Iを記録します。</p><p>前提条件: TSOログオン済みで、対象Db2サブシステムの表示コマンドを実行できる権限があること。DDFを停止・開始・変更する操作は行わず、表示結果だけを確認すること。</p><p>セッション環境: TSO READY状態からDSNコマンドプロセッサへ入り、Db2表示コマンドでDDF状態を確認する。ここでは机上例としてDBD1、DBD2、DB2G、ALIAS1、446、448、5020を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に DSN SYSTEM(DBD1) を入力し、対象Db2のコマンドプロセッサへ入ります。
［操作（入力）］
READY
COMMAND ===&gt; DSN SYSTEM(DBD1)
→ Enter を押す
［画面・出力］
DSN
DSN9000I -DBD1 DSN COMMAND PROCESSOR READY
DSN COMMAND ===&gt;
DSN9000I と DBD1 が表示されていれば、Db2コマンドを入力できる状態へ到達しています。
――――
■ ステップ 2
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に -DISPLAY DDF DETAIL を入力し、DISPLAY DDF詳細確認の表示結果を取得します。
［操作（入力）］
DSN COMMAND ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
DSNL080I -DBD1 DSNLTDDF DISPLAY DDF REPORT FOLLOWS
DSNL081I -DBD1 STATUS=STARTD
DSNL090I -DBD1 TCPPORT=446 SECPORT=448 RESPORT=5020 IPNAME=DB2A
DSNL099I -DBD1 DSNLTDDF DISPLAY DDF REPORT COMPLETE
DSN9022I -DBD1 DSNLTDDF &#x27;DISPLAY DDF&#x27; NORMAL COMPLETION
DSN COMMAND ===&gt;
DSNL090I TCPPORT SECPORT RESPORT DSN9022I が画面・出力に表示されていれば、DISPLAY DDF詳細確認の確認対象が取得できています。DSN9022I があれば、Db2コマンドは正常完了しています。
――――
■ ステップ 3
現在の画面はDSNコマンドプロセッサです。DSN COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
DSN COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、DSNコマンドプロセッサを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の DSN9000I が表示されること
② ステップ2 の DSNL090I TCPPORT SECPORT RESPORT DSN9022I が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Security</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE PROCEDURE 確認手順</strong></p><p>検証目的: stored procedure の新規登録を机上で確認します。schema、procedure 名、WLM 環境、dynamic result sets を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で SQL DDL の机上確認、routine 定義確認、SYSLOG 参照ができる権限があります。実機では schema 名、WLM 環境名、procedure 名、function 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、ルーチン・トリガー・SQL PL 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。入力内容と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; CREATE PROCEDURE APP.PAY_SUM(IN P_DEPT CHAR(3)) LANGUAGE SQL DYNAMIC RESULT SETS 1 BEGIN DECLARE C1 CURSOR WITH RETURN FOR SELECT EMPNO FROM PAYROLL.EMP WHERE DEPT = P_DEPT; OPEN C1; END
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; CREATE PROCEDURE APP.PAY_SUM(IN P_DEPT CHAR(3)) LANGUAGE SQL DYNAMIC RESULT SETS 1 BEGIN DECLARE C1 CURSOR WITH RETURN FOR SELECT EMPNO FROM PAYROLL.EMP WHERE DEPT = P_DEPT; OPEN C1; END
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した SQL または command を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT28  JOB12828 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = 0, CREATE PROCEDURE APP.PAY_SUM SUCCESSFUL
DSNT418I DYNAMIC RESULT SETS=1 LANGUAGE SQL
DSN9022I -DB2A CREATE PROCEDURE NORMAL COMPLETION
DSNT408I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12828 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT28
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I CREATE PROCEDURE APP.PAY_SUM SQLCODE=0
DSNT418I LANGUAGE SQL SSID=DB2A
DSN9022I NORMAL COMPLETION
APP.PAY_SUM が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT408I が期待どおりであること
③ ステップ3 の APP.PAY_SUM が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE FUNCTION 確認手順</strong></p><p>検証目的: 利用者定義関数の登録を机上で確認します。関数名、引数型、戻り型、SQL 本体を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で SQL DDL の机上確認、routine 定義確認、SYSLOG 参照ができる権限があります。実機では schema 名、WLM 環境名、procedure 名、function 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、ルーチン・トリガー・SQL PL 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。入力内容と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; CREATE FUNCTION APP.TAX_AMT(P_AMT DECIMAL(9,2)) RETURNS DECIMAL(9,2) LANGUAGE SQL RETURN P_AMT * DECIMAL(0.10,3,2)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; CREATE FUNCTION APP.TAX_AMT(P_AMT DECIMAL(9,2)) RETURNS DECIMAL(9,2) LANGUAGE SQL RETURN P_AMT * DECIMAL(0.10,3,2)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した SQL または command を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT28  JOB12828 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = 0, CREATE FUNCTION APP.TAX_AMT SUCCESSFUL
DSNT418I RETURNS DECIMAL(9,2) LANGUAGE SQL
DSN9022I -DB2A CREATE FUNCTION NORMAL COMPLETION
DSNT408I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12828 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT28
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I CREATE FUNCTION APP.TAX_AMT SQLCODE=0
DSNT418I RETURNS DECIMAL(9,2) SSID=DB2A
DSN9022I NORMAL COMPLETION
APP.TAX_AMT が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT408I が期待どおりであること
③ ステップ3 の APP.TAX_AMT が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TRIGGER 確認手順</strong></p><p>検証目的: trigger 定義の登録を机上で確認します。対象表、契機、実行時点、trigger 名を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で SQL DDL の机上確認、routine 定義確認、SYSLOG 参照ができる権限があります。実機では schema 名、WLM 環境名、procedure 名、function 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、ルーチン・トリガー・SQL PL 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。入力内容と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; CREATE TRIGGER APP.EMP_AUD AFTER UPDATE ON PAYROLL.EMP REFERENCING NEW AS N FOR EACH ROW INSERT INTO AUDIT.EMP_LOG VALUES(N.EMPNO, CURRENT TIMESTAMP)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; CREATE TRIGGER APP.EMP_AUD AFTER UPDATE ON PAYROLL.EMP REFERENCING NEW AS N FOR EACH ROW INSERT INTO AUDIT.EMP_LOG VALUES(N.EMPNO, CURRENT TIMESTAMP)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した SQL または command を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT28  JOB12828 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = 0, CREATE TRIGGER APP.EMP_AUD SUCCESSFUL
DSNT418I AFTER UPDATE ON PAYROLL.EMP
DSN9022I -DB2A CREATE TRIGGER NORMAL COMPLETION
DSNT408I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12828 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT28
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I CREATE TRIGGER APP.EMP_AUD SQLCODE=0
DSNT418I TARGET=PAYROLL.EMP SSID=DB2A
DSN9022I NORMAL COMPLETION
APP.EMP_AUD が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT408I が期待どおりであること
③ ステップ3 の APP.EMP_AUD が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>WLM ENVIRONMENT 確認手順</strong></p><p>検証目的: 外部 routine の WLM 環境指定を机上で確認します。routine 名、WLM 環境名、実行方式を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で SQL DDL の机上確認、routine 定義確認、SYSLOG 参照ができる権限があります。実機では schema 名、WLM 環境名、procedure 名、function 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、ルーチン・トリガー・SQL PL 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。入力内容と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; CREATE PROCEDURE APP.EXT_PAY(IN P1 CHAR(3)) LANGUAGE COBOL EXTERNAL NAME &#x27;PAYROLL.PAYPROC&#x27; WLM ENVIRONMENT PAYWLM PARAMETER STYLE GENERAL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; CREATE PROCEDURE APP.EXT_PAY(IN P1 CHAR(3)) LANGUAGE COBOL EXTERNAL NAME &#x27;PAYROLL.PAYPROC&#x27; WLM ENVIRONMENT PAYWLM PARAMETER STYLE GENERAL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した SQL または command を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT28  JOB12828 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = 0, CREATE PROCEDURE APP.EXT_PAY SUCCESSFUL
DSNT418I WLM ENVIRONMENT=PAYWLM PARAMETER STYLE GENERAL
DSN9022I -DB2A CREATE PROCEDURE NORMAL COMPLETION
DSNT418I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12828 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT28
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I CREATE PROCEDURE APP.EXT_PAY SQLCODE=0
DSNT418I WLMENV=PAYWLM SSID=DB2A
DSN9022I NORMAL COMPLETION
WLMENV=PAYWLM が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT418I が期待どおりであること
③ ステップ3 の WLMENV=PAYWLM が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNTPSMP 確認手順</strong></p><p>検証目的: external SQL procedure の作成支援経路を机上で確認します。DSNTPSMP 呼び出し、対象 procedure、完了 message を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A で SQL DDL の机上確認、routine 定義確認、SYSLOG 参照ができる権限があります。実機では schema 名、WLM 環境名、procedure 名、function 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、ルーチン・トリガー・SQL PL 領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の SQL または Db2 command を入力します。入力内容と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; CALL SYSPROC.DSNTPSMP(&#x27;APP.OLD_SQL_PROC&#x27;,&#x27;PREPARE&#x27;)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; CALL SYSPROC.DSNTPSMP(&#x27;APP.OLD_SQL_PROC&#x27;,&#x27;PREPARE&#x27;)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した SQL または command を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象処理の出力を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT28  JOB12828 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = 0, CALL SYSPROC.DSNTPSMP SUCCESSFUL
DSNT418I TARGET PROCEDURE=APP.OLD_SQL_PROC ACTION=PREPARE
DSN9022I -DB2A CALL NORMAL COMPLETION
DSNT408I が出力に含まれていれば、この手順で期待する結果を確認できます。JOB12828 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行単位のシステムログ証跡を開くために Enter を押します。出力本文とは別に、操作と subsystem を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT28
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I CALL SYSPROC.DSNTPSMP SQLCODE=0
DSNT418I TARGET=APP.OLD_SQL_PROC SSID=DB2A
DSN9022I NORMAL COMPLETION
SYSPROC.DSNTPSMP が SYSLOG に出ていれば、対象操作の実行者または完了状態を証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT408I が期待どおりであること
③ ステップ3 の SYSPROC.DSNTPSMP が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>SQLCODE 確認手順</strong></p><p>検証目的: SQL 実行結果の SQLCODE と SQLSTATE を机上で確認します。statement、戻り値、関連 message を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の message、utility output、SYSLOG、dump 関連情報を机上確認できる権限があります。実機では job name、message ID、reason code、dump data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、メッセージ・コード・障害解析領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の照会、SQL、または Db2 command を入力します。message ID と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SELECT * FROM PAYROLL.MISSING_TABLE
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SELECT * FROM PAYROLL.MISSING_TABLE
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象の job output を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT29  JOB12929 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT408I SQLCODE = -204, SQLSTATE = 42704
DSNT418I OBJECT PAYROLL.MISSING_TABLE NOT FOUND
DSN9022I -DB2A SQL ERROR COMPLETED
SQLCODE = -204 が出力に含まれていれば、この手順で期待する message または code を確認できます。JOB12929 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に、subsystem と発生時刻を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT29
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT408I SQLCODE=-204 SQLSTATE=42704 SSID=DB2A
DSNT418I OBJECT=PAYROLL.MISSING_TABLE
DSN9022I SQL ERROR COMPLETED
SQLSTATE=42704 が SYSLOG に出ていれば、対象 message または code を時系列証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の SQLCODE = -204 が期待どおりであること
③ ステップ3 の SQLSTATE=42704 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>00E reason code 確認手順</strong></p><p>検証目的: Db2のメッセージまたはダンプ見出しから4バイトの理由コードを採取し、診断用検索語へ変換して該当コードの処置情報へ突合します。</p><p>前提条件: 対象障害のSYSLOGまたはSVCダンプを閲覧できること。表示と資料照合だけを行い、Db2の停止、再始動、設定変更は実施しないこと。</p><p>セッション環境: SDSFまたはISPF Browseで障害時のログとダンプ見出しを参照し、Db2 CodesおよびTroubleshootingを別画面で参照する。</p><pre class="kb-code">■ ステップ 1
現在の画面は障害時ダンプのBrowse画面です。Command ===&gt; にF &#x27;REASON=&#x27;を入力し、終了理由を示す見出しへ移動します。
［操作（入力）］
Command ===&gt; F &#x27;REASON=&#x27;
→ Enter を押す
［画面・出力］
BROWSE  SYS1.DUMP00
DB2 SUBSYSTEM TERMINATION REQUESTED
REASON=00E50041
DB2 SUBSYSTEM TERMINATION REQUESTEDの直下にREASON=00E50041が表示され、4バイト理由コードを採取できます。
――――
■ ステップ 2
現在の画面は一次資料の検索画面です。検索 ===&gt; にABEND04E RC00E50041を入力し、異常終了と理由コードを組にして照合します。
［操作（入力）］
検索 ===&gt; ABEND04E RC00E50041
→ Enter を押す
［画面・出力］
ABEND04E RC00E50041
00E50041
説明: terminate agent structure要求の処理中に回復不能エラー
システム処置: Db2サブシステム終了
オペレーター処置: システムプログラマーへ通知してDb2を再始動
RC00E50041で該当項目を特定し、00E50041の説明、システム処置、オペレーター処置を障害記録へ対応付けます。
――――</pre><p>合格条件: ① ステップ 1 の REASON=00E50041 が表示されること
② ステップ 2 の RC00E50041 が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNT500I 確認手順</strong></p><p>検証目的: resource unavailable の message を机上で確認します。reason code、resource type、resource name を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の message、utility output、SYSLOG、dump 関連情報を机上確認できる権限があります。実機では job name、message ID、reason code、dump data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、メッセージ・コード・障害解析領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の照会、SQL、または Db2 command を入力します。message ID と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象の job output を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT29  JOB12929 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT500I RESOURCE UNAVAILABLE REASON 00C90084 TYPE 00000200 NAME PAYDB.PAYTS
DSNT501I RESOURCE WAIT DETECTED PLAN PAYPLAN
DSN9022I -DB2A DISPLAY DATABASE NORMAL COMPLETION
DSNT500I が出力に含まれていれば、この手順で期待する message または code を確認できます。JOB12929 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に、subsystem と発生時刻を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT29
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT500I REASON=00C90084 TYPE=00000200 NAME=PAYDB.PAYTS SSID=DB2A
DSNT501I PLAN=PAYPLAN WAITING
DSN9022I NORMAL COMPLETION
00C90084 が SYSLOG に出ていれば、対象 message または code を時系列証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT500I が期待どおりであること
③ ステップ3 の 00C90084 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNU256I 確認手順</strong></p><p>検証目的: utility job の DSNU message を机上で確認します。utility 名、対象 object、return code を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の message、utility output、SYSLOG、dump 関連情報を机上確認できる権限があります。実機では job name、message ID、reason code、dump data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、メッセージ・コード・障害解析領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の照会、SQL、または Db2 command を入力します。message ID と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; DISPLAY UTILITY(*)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; DISPLAY UTILITY(*)
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象の job output を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT29  JOB12929 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNU256I RUNSTATS UTILITY COMPLETED OBJECT=PAYDB.PAYTS
DSNU010I UTILITY EXECUTION COMPLETE, HIGHEST RETURN CODE=0
DSN9022I -DB2A DISPLAY UTILITY NORMAL COMPLETION
DSNU256I が出力に含まれていれば、この手順で期待する message または code を確認できます。JOB12929 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に、subsystem と発生時刻を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT29
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNU256I RUNSTATS OBJECT=PAYDB.PAYTS SSID=DB2A
DSNU010I HIGHEST RETURN CODE=0
DSN9022I NORMAL COMPLETION
HIGHEST RETURN CODE=0 が SYSLOG に出ていれば、対象 message または code を時系列証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNU256I が期待どおりであること
③ ステップ3 の HIGHEST RETURN CODE=0 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNL032I 確認手順</strong></p><p>検証目的: DDF/DRDA 通信障害の message を机上で確認します。LUWID、IFCID sequence、相手 system を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の message、utility output、SYSLOG、dump 関連情報を机上確認できる権限があります。実機では job name、message ID、reason code、dump data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、メッセージ・コード・障害解析領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の照会、SQL、または Db2 command を入力します。message ID と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象の job output を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT29  JOB12929 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNL032I DDF COMMUNICATION FAILURE LUWID=NETA.DB2A.12929
DSNL033I IFCID SEQUENCE=004812 REMOTE SYSTEM=APPHOST1
DSN9022I -DB2A DISPLAY DDF NORMAL COMPLETION
DSNL032I が出力に含まれていれば、この手順で期待する message または code を確認できます。JOB12929 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に、subsystem と発生時刻を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT29
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL032I LUWID=NETA.DB2A.12929 SSID=DB2A
DSNL033I IFCID SEQUENCE=004812 REMOTE=APPHOST1
DSN9022I NORMAL COMPLETION
IFCID SEQUENCE=004812 が SYSLOG に出ていれば、対象 message または code を時系列証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNL032I が期待どおりであること
③ ステップ3 の IFCID SEQUENCE=004812 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>dump collection 確認手順</strong></p><p>検証目的: 異常終了時の dump 保全を机上で確認します。dump data set、abend reason code、関連 message を照合します。</p><p>前提条件: TSO/ISPF にログオン済みです。Db2 subsystem DB2A の message、utility output、SYSLOG、dump 関連情報を机上確認できる権限があります。実機では job name、message ID、reason code、dump data set 名を環境に合わせます。</p><p>セッション環境: DB2I COMMANDS と SDSF を使い、メッセージ・コード・障害解析領域の机上証跡を確認します。検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; に確認対象の照会、SQL、または Db2 command を入力します。message ID と対象名を同じ行で確認してから Enter を押します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; DISPLAY DUMP STATUS FOR DB2A
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; DISPLAY DUMP STATUS FOR DB2A
DSNT400I REQUEST ACCEPTED
DSNT400I が表示されていれば、Db2 が入力内容を受け付けたことを確認できます。Command ===&gt; の行も同じ画面に残るため、送信した内容を照合できます。
――――
■ ステップ 2
現在の画面は SDSF ST のジョブ一覧です。NP 欄に S を入力し、対象の job output を開くために Enter を押します。JobName と JobID を確認してから対象行を選びます。
［操作（入力）］
(SDSF ST)
NP   JobName  JobID    Owner  Queue
S    DB2IT29  JOB12929 USER1  OUTPUT
→ Enter を押す
［画面・出力］
(DB2 COMMAND RESPONSE)
DSNT900I DUMP DATA SET SYS1.DUMP12 RETAINED FOR DB2A
DSNT901I ABEND=04E REASON=00E40318 RELATED MESSAGE=DSNT500I
DSN9022I -DB2A DISPLAY DUMP NORMAL COMPLETION
DSNT900I が出力に含まれていれば、この手順で期待する message または code を確認できます。JOB12929 の出力として読めるため、別ジョブの結果と取り違えていないことも確認できます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧です。NP 欄に S を入力し、同じ実行時間帯のシステムログ証跡を開くために Enter を押します。出力本文とは別に、subsystem と発生時刻を確認します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    DB2IT29
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT900I SYS1.DUMP12 RETAINED SSID=DB2A
DSNT901I ABEND=04E REASON=00E40318 MESSAGE=DSNT500I
DSN9022I NORMAL COMPLETION
SYS1.DUMP12 が SYSLOG に出ていれば、対象 message または code を時系列証跡として追えます。DB2A も同じ出力にあるため、対象 subsystem を取り違えていないことが分かります。
――――</pre><p>合格条件: ① ステップ1 の DSNT400I が表示されていること
② ステップ2 の DSNT900I が期待どおりであること
③ ステップ3 の SYS1.DUMP12 が確認できること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Messages / Db2_zOS_Codes / Db2_zOS_Troubleshooting</p></div><div class="kb-p"><p class="kb-pname"><strong>DSN6ARVP 確認手順</strong></p><p>検証目的: DSNTIJUZ が作る DSNZPxxx の構成を机上確認します。6つの DSN6 系マクロがサブシステムパラメータモジュールに含まれることを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、prefix.SDSNEXIT、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではDSNZPARM、DSNHDECP、DSNHMCID、BSDS通信情報の変更は変更管理承認を得てから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブとSYSLOGの机上出力を確認します。ジョブ投入とコマンド出力は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のコマンドまたはジョブ投入行を入力します。この操作で、対象ジョブや表示コマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ名、マクロ名、生成資材名、またはBSDS値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12360 DSNTIJUZ RC=0000
DSNZPDB2 INCLUDES DSN6ARVP DSN6FAC DSN6GRP DSN6LOGP DSN6SPRM DSN6SYSP
NORMAL COMPLETION
DSNZPDB2 INCLUDES が表示されていれば、机上例では対象の導入値を確認できます。NORMAL COMPLETION も同じ画面で確認し、エラー応答ではないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として、同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12360 DSNTIJUZ RC=0000
DSNZPDB2 INCLUDES DSN6ARVP DSN6FAC DSN6GRP DSN6LOGP DSN6SPRM DSN6SYSP
ISSUER=USER1
DSNZPDB2 INCLUDES と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNZPDB2 INCLUDES が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation.pdf p.442</p></div><div class="kb-p"><p class="kb-pname"><strong>DSN6GRP 確認手順</strong></p><p>検証目的: DSN6GRP のメンバー値を机上確認します。MEMBNAME、GROUP、DSHAREが起動プロシージャ側の指定と矛盾しないことを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、prefix.SDSNEXIT、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではDSNZPARM、DSNHDECP、DSNHMCID、BSDS通信情報の変更は変更管理承認を得てから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブとSYSLOGの机上出力を確認します。ジョブ投入とコマンド出力は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のコマンドまたはジョブ投入行を入力します。この操作で、対象ジョブや表示コマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY GROUP
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY GROUP
-DISPLAY GROUP が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ名、マクロ名、生成資材名、またはBSDS値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSN7100I DISPLAY GROUP MEMBER=DB2A GROUP=DSNGRP STATUS=ACTIVE
DSN6GRP MEMBNAME=DB2A GROUP=DSNGRP DSHARE=YES
NORMAL COMPLETION
DSN6GRP MEMBNAME=DB2A が表示されていれば、机上例では対象の導入値を確認できます。NORMAL COMPLETION も同じ画面で確認し、エラー応答ではないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として、同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSN7100I DISPLAY GROUP MEMBER=DB2A GROUP=DSNGRP STATUS=ACTIVE
DSN6GRP MEMBNAME=DB2A GROUP=DSNGRP DSHARE=YES
ISSUER=USER1
DSN6GRP MEMBNAME=DB2A と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY GROUP が操作（入力）に記載されていること
② ステップ2 の DSN6GRP MEMBNAME=DB2A が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation.pdf p.442</p></div><div class="kb-p"><p class="kb-pname"><strong>DSN6LOGP 確認手順</strong></p><p>検証目的: DSN6ARVP と DSN6LOGP の机上値を確認します。アーカイブログ接頭辞、ログオフロード、二重BSDSの値を同じ導入出力から読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、prefix.SDSNEXIT、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではDSNZPARM、DSNHDECP、DSNHMCID、BSDS通信情報の変更は変更管理承認を得てから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブとSYSLOGの机上出力を確認します。ジョブ投入とコマンド出力は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のコマンドまたはジョブ投入行を入力します。この操作で、対象ジョブや表示コマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27;
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27; が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ名、マクロ名、生成資材名、またはBSDS値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12361 DSNTIJUZ RC=0000
DSN6ARVP ARCPFX1=DB2A.ARCHLOG1 ARCPFX2=DB2A.ARCHLOG2
DSN6LOGP OFFLOAD=YES TWOBSDS=YES
NORMAL COMPLETION
DSN6LOGP OFFLOAD=YES が表示されていれば、机上例では対象の導入値を確認できます。NORMAL COMPLETION も同じ画面で確認し、エラー応答ではないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として、同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12361 DSNTIJUZ RC=0000
DSN6ARVP ARCPFX1=DB2A.ARCHLOG1 ARCPFX2=DB2A.ARCHLOG2
DSN6LOGP OFFLOAD=YES TWOBSDS=YES
ISSUER=USER1
DSN6LOGP OFFLOAD=YES と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSN6LOGP OFFLOAD=YES が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation.pdf p.442</p></div><div class="kb-p"><p class="kb-pname"><strong>DSN6SPRM 確認手順</strong></p><p>検証目的: DSN6SPRM と DSN6SYSP の机上値を確認します。Administrative Scheduler、CTHREAD、トレース初期化に関係する値を分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。Db2導入ライブラリ、prefix.NEW.SDSNSAMP、prefix.SDSNEXIT、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではDSNZPARM、DSNHDECP、DSNHMCID、BSDS通信情報の変更は変更管理承認を得てから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブとSYSLOGの机上出力を確認します。ジョブ投入とコマンド出力は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS の入力画面です。Command ===&gt; に机上確認用のコマンドまたはジョブ投入行を入力します。この操作で、対象ジョブや表示コマンドを明示してから応答を確認します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(SYSPARM)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(SYSPARM)
-DISPLAY STATS(SYSPARM) が入力欄に見えていれば、このステップの入力内容を確認できます。次のステップで同じ対象に対する応答を読み取ります。
――――
■ ステップ 2
現在の画面はコマンド応答の表示待ち状態です。追加の文字入力は行わず、前ステップで送信した対象の結果を受け取ります。ここではジョブ名、マクロ名、生成資材名、またはBSDS値を確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNT770I SYSPARM DSN6SPRM ADMTPROC=DB2AADMT CACHEDYN=YES
DSNT771I SYSPARM DSN6SYSP CTHREAD=200 UIFCIDS=YES
NORMAL COMPLETION
DSN6SPRM ADMTPROC=DB2AADMT が表示されていれば、机上例では対象の導入値を確認できます。NORMAL COMPLETION も同じ画面で確認し、エラー応答ではないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入ジョブまたはコマンド応答がシステムログにも残っているかを確認します。運用証跡として、同じ値がログ側に見えることを読み取ります。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT770I SYSPARM DSN6SPRM ADMTPROC=DB2AADMT CACHEDYN=YES
DSNT771I SYSPARM DSN6SYSP CTHREAD=200 UIFCIDS=YES
ISSUER=USER1
DSN6SPRM ADMTPROC=DB2AADMT と ISSUER=USER1 が表示されていれば、誰が対象確認を行ったかを机上例として追跡できます。コマンド応答とSYSLOGの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY STATS(SYSPARM) が操作（入力）に記載されていること
② ステップ2 の DSN6SPRM ADMTPROC=DB2AADMT が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation.pdf p.442</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNZPxxx 確認手順</strong></p><p>検証目的: DSNTIJUZとDSNZPxxxの机上出力を確認します。DSN6系マクロからサブシステムパラメータ・モジュールが作られる流れを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。導入ライブラリ、SDSNSAMP、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではZPARM、DSNHDECP、APPLCOMPAT、DDF BSDS情報の変更は変更管理承認を得て、停止要否とフォールバック手順を確認してから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブ、起動パラメータ、DDF BSDS更新の机上出力を確認します。ジョブ投入は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS または導入確認用の入力画面です。Command ===&gt; に机上確認用の表示コマンドを入力します。この操作では確認したいジョブ名、ZPARM名、またはDDF値が出る指定であることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27;
Command ===&gt; -DISPLAY GROUP
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27;
Command ===&gt; -DISPLAY GROUP
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27; が入力欄に表示されていれば、机上例の導入確認を始める準備ができています。対象名と値が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面は導入値確認の応答画面です。前ステップで送信した表示結果を読み取ります。操作欄には追加入力を入れず、ジョブ名、モジュール名、APPLCOMPAT値、DDF値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12345 DSNTIJUZ ENDED RC=0004 WARNING REVIEWED
DSNZPDB2 BUILT FROM DSN6ARVP DSN6FAC DSN6GRP DSN6LOGP DSN6SPRM DSN6SYSP
NORMAL COMPLETION
DSNZPDB2 BUILT が表示されていれば、机上例では対象の導入値を確認できています。NORMAL COMPLETION も同じ画面で確認し、エラーがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入確認の応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12345 DSNTIJUZ ENDED RC=0004 WARNING REVIEWED
DSNZPDB2 BUILT FROM DSN6ARVP DSN6FAC DSN6GRP DSN6LOGP DSN6SPRM DSN6SYSP
ISSUER=USER1
DSNZPDB2 BUILT と ISSUER=USER1 が表示されていれば、誰がどの導入確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUZ)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNZPDB2 BUILT が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Performance p.216</p></div><div class="kb-p"><p class="kb-pname"><strong>DSNTIJUA 確認手順</strong></p><p>検証目的: DSNTIJUAとDSNHDECPの机上出力を確認します。CCSIDなどのサイト既定値がアプリケーション用ロードモジュールとして準備されることを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。導入ライブラリ、SDSNSAMP、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではZPARM、DSNHDECP、APPLCOMPAT、DDF BSDS情報の変更は変更管理承認を得て、停止要否とフォールバック手順を確認してから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブ、起動パラメータ、DDF BSDS更新の机上出力を確認します。ジョブ投入は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS または導入確認用の入力画面です。Command ===&gt; に机上確認用の表示コマンドを入力します。この操作では確認したいジョブ名、ZPARM名、またはDDF値が出る指定であることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUA)&#x27;
Command ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUA)&#x27;
Command ===&gt; -DISPLAY DDF DETAIL
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUA)&#x27; が入力欄に表示されていれば、机上例の導入確認を始める準備ができています。対象名と値が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面は導入値確認の応答画面です。前ステップで送信した表示結果を読み取ります。操作欄には追加入力を入れず、ジョブ名、モジュール名、APPLCOMPAT値、DDF値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12346 DSNTIJUA ENDED RC=0000
DSNHDECP BUILT CCSID=037 APPLDEFAULTS=DSNHDECP
NORMAL COMPLETION
DSNHDECP BUILT CCSID=037 が表示されていれば、机上例では対象の導入値を確認できています。NORMAL COMPLETION も同じ画面で確認し、エラーがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入確認の応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12346 DSNTIJUA ENDED RC=0000
DSNHDECP BUILT CCSID=037 APPLDEFAULTS=DSNHDECP
ISSUER=USER1
DSNHDECP BUILT CCSID=037 と ISSUER=USER1 が表示されていれば、誰がどの導入確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUA)&#x27; が操作（入力）に記載されていること
② ステップ2 の DSNHDECP BUILT CCSID=037 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Performance p.216</p></div><div class="kb-p"><p class="kb-pname"><strong>START DB2 PARM 確認手順</strong></p><p>検証目的: START DB2 PARMの机上応答を確認します。起動時にどのZPARMモジュールを読むかを明示する指定を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。導入ライブラリ、SDSNSAMP、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではZPARM、DSNHDECP、APPLCOMPAT、DDF BSDS情報の変更は変更管理承認を得て、停止要否とフォールバック手順を確認してから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブ、起動パラメータ、DDF BSDS更新の机上出力を確認します。ジョブ投入は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS または導入確認用の入力画面です。Command ===&gt; に机上確認用の表示コマンドを入力します。この操作では確認したいジョブ名、ZPARM名、またはDDF値が出る指定であることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -START DB2 PARM(DSNZPDB2)
Command ===&gt; -DISPLAY GROUP
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -START DB2 PARM(DSNZPDB2)
Command ===&gt; -DISPLAY GROUP
-START DB2 PARM(DSNZPDB2) が入力欄に表示されていれば、机上例の導入確認を始める準備ができています。対象名と値が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面は導入値確認の応答画面です。前ステップで送信した表示結果を読み取ります。操作欄には追加入力を入れず、ジョブ名、モジュール名、APPLCOMPAT値、DDF値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNY001I -START DB2 PARM(DSNZPDB2) ACCEPTED
DSN7100I DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE ZPARM=DSNZPDB2
NORMAL COMPLETION
ZPARM=DSNZPDB2 が表示されていれば、机上例では対象の導入値を確認できています。NORMAL COMPLETION も同じ画面で確認し、エラーがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入確認の応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNY001I -START DB2 PARM(DSNZPDB2) ACCEPTED
DSN7100I DISPLAY GROUP MEMBER=DB2A STATUS=ACTIVE ZPARM=DSNZPDB2
ISSUER=USER1
ZPARM=DSNZPDB2 と ISSUER=USER1 が表示されていれば、誰がどの導入確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -START DB2 PARM(DSNZPDB2) が操作（入力）に記載されていること
② ステップ2 の ZPARM=DSNZPDB2 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Performance p.216</p></div><div class="kb-p"><p class="kb-pname"><strong>APPLCOMPAT subsystem parameter 確認手順</strong></p><p>検証目的: APPLCOMPAT subsystem parameterとRTN_PKG_APPLCOMPATの机上値を確認します。通常アプリケーションの互換性既定と、Db2提供ルーチンのBIND/REBIND値を分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。導入ライブラリ、SDSNSAMP、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではZPARM、DSNHDECP、APPLCOMPAT、DDF BSDS情報の変更は変更管理承認を得て、停止要否とフォールバック手順を確認してから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブ、起動パラメータ、DDF BSDS更新の机上出力を確認します。ジョブ投入は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS または導入確認用の入力画面です。Command ===&gt; に机上確認用の表示コマンドを入力します。この操作では確認したいジョブ名、ZPARM名、またはDDF値が出る指定であることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(SYSPARM)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27;
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(SYSPARM)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJRT)&#x27;
-DISPLAY STATS(SYSPARM) が入力欄に表示されていれば、机上例の導入確認を始める準備ができています。対象名と値が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面は導入値確認の応答画面です。前ステップで送信した表示結果を読み取ります。操作欄には追加入力を入れず、ジョブ名、モジュール名、APPLCOMPAT値、DDF値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNT770I SYSPARM APPLCOMPAT=V13R1M500
JOB12347 DSNTIJRT DB2OPT RTN_PKG_APPLCOMPAT=DEFAULT
NORMAL COMPLETION
APPLCOMPAT=V13R1M500 が表示されていれば、机上例では対象の導入値を確認できています。NORMAL COMPLETION も同じ画面で確認し、エラーがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入確認の応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT770I SYSPARM APPLCOMPAT=V13R1M500
JOB12347 DSNTIJRT DB2OPT RTN_PKG_APPLCOMPAT=DEFAULT
ISSUER=USER1
APPLCOMPAT=V13R1M500 と ISSUER=USER1 が表示されていれば、誰がどの導入確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY STATS(SYSPARM) が操作（入力）に記載されていること
② ステップ2 の APPLCOMPAT=V13R1M500 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_WhatsNew.pdf p.334 / Db2_zOS_Installation.pdf p.508</p></div><div class="kb-p"><p class="kb-pname"><strong>DDF情報のBSDS更新 確認手順</strong></p><p>検証目的: DDF情報のBSDS更新を机上確認します。DSNJU003のDDF statementでLOCATION、PORT、RESPORT、IPNAMEがBSDSに記録され、DDF表示と一致することを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。導入ライブラリ、SDSNSAMP、起動プロシージャ、BSDS更新ジョブの机上確認ができる前提です。実機ではZPARM、DSNHDECP、APPLCOMPAT、DDF BSDS情報の変更は変更管理承認を得て、停止要否とフォールバック手順を確認してから実施します。</p><p>セッション環境: ISPF Edit、DB2I COMMANDS、SDSFで導入ジョブ、起動パラメータ、DDF BSDS更新の机上出力を確認します。ジョブ投入は机上例であり、検証状態は常に机上です。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS または導入確認用の入力画面です。Command ===&gt; に机上確認用の表示コマンドを入力します。この操作では確認したいジョブ名、ZPARM名、またはDDF値が出る指定であることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27;
Command ===&gt; -DISPLAY DDF DETAIL
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27;
Command ===&gt; -DISPLAY DDF DETAIL
SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27; が入力欄に表示されていれば、机上例の導入確認を始める準備ができています。対象名と値が目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面は導入値確認の応答画面です。前ステップで送信した表示結果を読み取ります。操作欄には追加入力を入れず、ジョブ名、モジュール名、APPLCOMPAT値、DDF値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
JOB12348 DSNTIJUL DSNJU003 DDF LOCATION=DB2A PORT=446 RESPORT=5001 IPNAME=DB2AIP
DSNL084I TCPPORT=446 RESPORT=5001 IPNAME=DB2AIP
NORMAL COMPLETION
LOCATION=DB2A PORT=446 が表示されていれば、机上例では対象の導入値を確認できています。NORMAL COMPLETION も同じ画面で確認し、エラーがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、導入確認の応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
JOB12348 DSNTIJUL DSNJU003 DDF LOCATION=DB2A PORT=446 RESPORT=5001 IPNAME=DB2AIP
DSNL084I TCPPORT=446 RESPORT=5001 IPNAME=DB2AIP
ISSUER=USER1
LOCATION=DB2A PORT=446 と ISSUER=USER1 が表示されていれば、誰がどの導入確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の SUBMIT &#x27;DSN1310.NEW.SDSNSAMP(DSNTIJUL)&#x27; が操作（入力）に記載されていること
② ステップ2 の LOCATION=DB2A PORT=446 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Installation / Db2_zOS_Performance p.216</p></div><div class="kb-p"><p class="kb-pname"><strong>PORT 確認手順</strong></p><p>検証目的: PORTとLOCATIONの机上応答を確認します。通常のDRDA SQL要求を受けるTCPPORTが、接続定義で使うロケーション名と一致して見えることを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機ではDDFやサブシステムパラメータの確認は変更管理承認を得て、対象SSID、LOCATION、ポート番号、接続中アプリケーションへの影響を確認してから実施します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDISPLAY DDFやSTART DDFの机上コマンドを入力し、コマンド応答画面またはSDSF SYSLOGでメッセージ、ポート、LOCATION、IPNAME、DBAT関連値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にDDF確認用のDb2コマンドを入力します。この操作では確認したいポート、LOCATION、DBAT関連値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -START DDF
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -START DDF
-DISPLAY DDF DETAIL が入力欄に表示されていれば、机上例のDDF確認コマンドを実行する準備ができています。コマンド名と対象SSIDが目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はDDFコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、メッセージID、LOCATION、ポート、DBAT関連値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A TCPPORT=446 STATUS=STARTED
DSNL004I DDF STARTED LOCATION=DB2A TCPPORT=446 IPNAME=DB2AIP
NORMAL COMPLETION
LOCATION=DB2A TCPPORT=446 が表示されていれば、机上例ではDDF関連値を確認できています。NORMAL COMPLETION も同じ画面で確認し、対象値が合格条件と一致していることを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、DDF確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A TCPPORT=446 STATUS=STARTED
DSNL004I DDF STARTED LOCATION=DB2A TCPPORT=446 IPNAME=DB2AIP
ISSUER=USER1
LOCATION=DB2A TCPPORT=446 と ISSUER=USER1 が表示されていれば、誰がどのDDF確認を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY DDF DETAIL が操作（入力）に記載されていること
② ステップ2 の LOCATION=DB2A TCPPORT=446 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>SECPORT 確認手順</strong></p><p>検証目的: SECPORTとRESPORTの机上応答を確認します。暗号化接続用の入口と二相コミット再同期用の入口が、通常ポートと別値で表示されることを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機ではDDFやサブシステムパラメータの確認は変更管理承認を得て、対象SSID、LOCATION、ポート番号、接続中アプリケーションへの影響を確認してから実施します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDISPLAY DDFやSTART DDFの机上コマンドを入力し、コマンド応答画面またはSDSF SYSLOGでメッセージ、ポート、LOCATION、IPNAME、DBAT関連値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にDDF確認用のDb2コマンドを入力します。この操作では確認したいポート、LOCATION、DBAT関連値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -START DDF
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -START DDF
-DISPLAY DDF DETAIL が入力欄に表示されていれば、机上例のDDF確認コマンドを実行する準備ができています。コマンド名と対象SSIDが目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はDDFコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、メッセージID、LOCATION、ポート、DBAT関連値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A TCPPORT=446 SECPORT=448 RESPORT=5001
DSNL004I DDF STARTED LOCATION=DB2A SECPORT=448 RESPORT=5001
NORMAL COMPLETION
SECPORT=448 RESPORT=5001 が表示されていれば、机上例ではDDF関連値を確認できています。NORMAL COMPLETION も同じ画面で確認し、対象値が合格条件と一致していることを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、DDF確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A TCPPORT=446 SECPORT=448 RESPORT=5001
DSNL004I DDF STARTED LOCATION=DB2A SECPORT=448 RESPORT=5001
ISSUER=USER1
SECPORT=448 RESPORT=5001 と ISSUER=USER1 が表示されていれば、誰がどのDDF確認を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY DDF DETAIL が操作（入力）に記載されていること
② ステップ2 の SECPORT=448 RESPORT=5001 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>IPNAME 確認手順</strong></p><p>検証目的: IPNAMEの机上応答を確認します。Data SharingでそろえるDDF識別名が、LOCATIONやTCPPORTと同じ応答に表示されることを読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機ではDDFやサブシステムパラメータの確認は変更管理承認を得て、対象SSID、LOCATION、ポート番号、接続中アプリケーションへの影響を確認してから実施します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDISPLAY DDFやSTART DDFの机上コマンドを入力し、コマンド応答画面またはSDSF SYSLOGでメッセージ、ポート、LOCATION、IPNAME、DBAT関連値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にDDF確認用のDb2コマンドを入力します。この操作では確認したいポート、LOCATION、DBAT関連値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -START DDF
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -START DDF
-DISPLAY DDF DETAIL が入力欄に表示されていれば、机上例のDDF確認コマンドを実行する準備ができています。コマンド名と対象SSIDが目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はDDFコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、メッセージID、LOCATION、ポート、DBAT関連値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A IPNAME=DB2AIP TCPPORT=446
DSNL004I DDF STARTED LOCATION=DB2A IPNAME=DB2AIP TCPPORT=446
NORMAL COMPLETION
IPNAME=DB2AIP が表示されていれば、机上例ではDDF関連値を確認できています。NORMAL COMPLETION も同じ画面で確認し、対象値が合格条件と一致していることを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、DDF確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL LOCATION=DB2A IPNAME=DB2AIP TCPPORT=446
DSNL004I DDF STARTED LOCATION=DB2A IPNAME=DB2AIP TCPPORT=446
ISSUER=USER1
IPNAME=DB2AIP と ISSUER=USER1 が表示されていれば、誰がどのDDF確認を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY DDF DETAIL が操作（入力）に記載されていること
② ステップ2 の IPNAME=DB2AIP が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>MAXDBAT 確認手順</strong></p><p>検証目的: MAXDBATとCONDBATの机上応答を確認します。活動中DBAT数の上限と、同時に抱えられるリモート接続数の上限を分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機ではDDFやサブシステムパラメータの確認は変更管理承認を得て、対象SSID、LOCATION、ポート番号、接続中アプリケーションへの影響を確認してから実施します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDISPLAY DDFやSTART DDFの机上コマンドを入力し、コマンド応答画面またはSDSF SYSLOGでメッセージ、ポート、LOCATION、IPNAME、DBAT関連値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にDDF確認用のDb2コマンドを入力します。この操作では確認したいポート、LOCATION、DBAT関連値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -DISPLAY THREAD(*) TYPE(INACTIVE)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -DISPLAY THREAD(*) TYPE(INACTIVE)
-DISPLAY DDF DETAIL が入力欄に表示されていれば、机上例のDDF確認コマンドを実行する準備ができています。コマンド名と対象SSIDが目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はDDFコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、メッセージID、LOCATION、ポート、DBAT関連値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNL080I DISPLAY DDF DETAIL MAXDBAT=200 CONDBAT=1000 CMTSTAT=INACTIVE
DSNV401I DISPLAY THREAD TYPE(INACTIVE) NORMAL COMPLETION
NORMAL COMPLETION
MAXDBAT=200 CONDBAT=1000 が表示されていれば、机上例ではDDF関連値を確認できています。NORMAL COMPLETION も同じ画面で確認し、対象値が合格条件と一致していることを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、DDF確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL MAXDBAT=200 CONDBAT=1000 CMTSTAT=INACTIVE
DSNV401I DISPLAY THREAD TYPE(INACTIVE) NORMAL COMPLETION
ISSUER=USER1
MAXDBAT=200 CONDBAT=1000 と ISSUER=USER1 が表示されていれば、誰がどのDDF確認を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY DDF DETAIL が操作（入力）に記載されていること
② ステップ2 の MAXDBAT=200 CONDBAT=1000 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CMTSTAT 確認手順</strong></p><p>検証目的: CMTSTATとIDTHTOINの机上応答を確認します。コミット後DBATの保持形態と、アイドル状態のスレッドを終了候補にする時間を読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDSまたはDSNセッションでDb2コマンドを机上確認できる前提です。実機ではDDFやサブシステムパラメータの確認は変更管理承認を得て、対象SSID、LOCATION、ポート番号、接続中アプリケーションへの影響を確認してから実施します。</p><p>セッション環境: DSNセッションまたはDB2I COMMANDSでDISPLAY DDFやSTART DDFの机上コマンドを入力し、コマンド応答画面またはSDSF SYSLOGでメッセージ、ポート、LOCATION、IPNAME、DBAT関連値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にDDF確認用のDb2コマンドを入力します。この操作では確認したいポート、LOCATION、DBAT関連値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -DISPLAY THREAD(*) TYPE(INACTIVE)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DDF DETAIL
Command ===&gt; -DISPLAY THREAD(*) TYPE(INACTIVE)
-DISPLAY DDF DETAIL が入力欄に表示されていれば、机上例のDDF確認コマンドを実行する準備ができています。コマンド名と対象SSIDが目的と合っていることを確認します。
――――
■ ステップ 2
現在の画面はDDFコマンド応答確認の画面です。前ステップで送信したDb2コマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、メッセージID、LOCATION、ポート、DBAT関連値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNL080I DISPLAY DDF DETAIL CMTSTAT=INACTIVE IDTHTOIN=120
DSNV401I DISPLAY THREAD TYPE(INACTIVE) IDLE THREADS ELIGIBLE
NORMAL COMPLETION
CMTSTAT=INACTIVE IDTHTOIN=120 が表示されていれば、机上例ではDDF関連値を確認できています。NORMAL COMPLETION も同じ画面で確認し、対象値が合格条件と一致していることを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、DDF確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNL080I DISPLAY DDF DETAIL CMTSTAT=INACTIVE IDTHTOIN=120
DSNV401I DISPLAY THREAD TYPE(INACTIVE) IDLE THREADS ELIGIBLE
ISSUER=USER1
CMTSTAT=INACTIVE IDTHTOIN=120 と ISSUER=USER1 が表示されていれば、誰がどのDDF確認を行ったかを机上例として追跡できます。コマンド応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY DDF DETAIL が操作（入力）に記載されていること
② ステップ2 の CMTSTAT=INACTIVE IDTHTOIN=120 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>IRLMRWT 確認手順</strong></p><p>検証目的: IRLMRWTとLOCK TIMEOUTの机上値を確認します。サブシステム既定のロック待ちと、SQL実行時の上書き可能性を分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDS、SDSF、性能レポートまたはDISPLAY系の机上出力を確認できる前提です。実機でロック、EDM、RID、ソート、バッファプール関連値を変更する場合は、変更管理承認と対象SSID、ピーク時間帯、影響アプリケーションを事前に確認します。</p><p>セッション環境: DB2I COMMANDSまたはDSNセッションでDISPLAY系コマンドを入力し、SDSF SYSLOGや性能レポートの机上出力でロック待ち、EDM、RID、ソート、バッファプールの値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にロックまたはメモリ資源の確認コマンドを入力します。この操作では確認対象の値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) TYPE(*)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY THREAD(*) TYPE(*)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS
-DISPLAY THREAD(*) TYPE(*) が入力欄に表示されていれば、机上例の資源確認コマンドを実行する準備ができています。対象SSIDと表示範囲が目的に合っていることを確認します。
――――
■ ステップ 2
現在の画面は資源値確認の応答画面です。前ステップで送信したDb2コマンドまたは机上レポートの応答を読み取ります。操作欄には追加入力を入れず、対象値と警告の有無を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNV401I DISPLAY THREAD LOCK WAIT IRLMRWT=30 CURRENT LOCK TIMEOUT=15
DSNT375I DATABASE=PAYDB SPACENAME=PAYTS LOCKS ACTIVE
NORMAL COMPLETION
IRLMRWT=30 CURRENT LOCK TIMEOUT=15 が表示されていれば、机上例では対象資源の値を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、資源確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNV401I DISPLAY THREAD LOCK WAIT IRLMRWT=30 CURRENT LOCK TIMEOUT=15
DSNT375I DATABASE=PAYDB SPACENAME=PAYTS LOCKS ACTIVE
ISSUER=USER1
IRLMRWT=30 CURRENT LOCK TIMEOUT=15 と ISSUER=USER1 が表示されていれば、誰がどの資源確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY THREAD(*) TYPE(*) が操作（入力）に記載されていること
② ステップ2 の IRLMRWT=30 CURRENT LOCK TIMEOUT=15 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>NUMLKUS 確認手順</strong></p><p>検証目的: NUMLKUS、NUMLKTS、LOCKMAXの机上値を確認します。利用者単位、表スペース単位、個別定義のロック上限を混同しないよう同じ対象で見ます。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDS、SDSF、性能レポートまたはDISPLAY系の机上出力を確認できる前提です。実機でロック、EDM、RID、ソート、バッファプール関連値を変更する場合は、変更管理承認と対象SSID、ピーク時間帯、影響アプリケーションを事前に確認します。</p><p>セッション環境: DB2I COMMANDSまたはDSNセッションでDISPLAY系コマンドを入力し、SDSF SYSLOGや性能レポートの机上出力でロック待ち、EDM、RID、ソート、バッファプールの値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にロックまたはメモリ資源の確認コマンドを入力します。この操作では確認対象の値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS
Command ===&gt; -DISPLAY THREAD(*) TYPE(*)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS
Command ===&gt; -DISPLAY THREAD(*) TYPE(*)
-DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS が入力欄に表示されていれば、机上例の資源確認コマンドを実行する準備ができています。対象SSIDと表示範囲が目的に合っていることを確認します。
――――
■ ステップ 2
現在の画面は資源値確認の応答画面です。前ステップで送信したDb2コマンドまたは机上レポートの応答を読み取ります。操作欄には追加入力を入れず、対象値と警告の有無を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNT375I DATABASE=PAYDB SPACENAME=PAYTS NUMLKTS=2000 LOCKMAX=SYSTEM
DSNV401I DISPLAY THREAD USER LOCKS NUMLKUS=10000
NORMAL COMPLETION
NUMLKTS=2000 LOCKMAX=SYSTEM が表示されていれば、机上例では対象資源の値を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、資源確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT375I DATABASE=PAYDB SPACENAME=PAYTS NUMLKTS=2000 LOCKMAX=SYSTEM
DSNV401I DISPLAY THREAD USER LOCKS NUMLKUS=10000
ISSUER=USER1
NUMLKTS=2000 LOCKMAX=SYSTEM と ISSUER=USER1 が表示されていれば、誰がどの資源確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) LOCKS が操作（入力）に記載されていること
② ステップ2 の NUMLKTS=2000 LOCKMAX=SYSTEM が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CACHEDYN 確認手順</strong></p><p>検証目的: CACHEDYNとEDM poolの机上値を確認します。動的SQLキャッシュの有効化と、EDMステートメント領域の容量を同じ文脈で読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDS、SDSF、性能レポートまたはDISPLAY系の机上出力を確認できる前提です。実機でロック、EDM、RID、ソート、バッファプール関連値を変更する場合は、変更管理承認と対象SSID、ピーク時間帯、影響アプリケーションを事前に確認します。</p><p>セッション環境: DB2I COMMANDSまたはDSNセッションでDISPLAY系コマンドを入力し、SDSF SYSLOGや性能レポートの机上出力でロック待ち、EDM、RID、ソート、バッファプールの値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にロックまたはメモリ資源の確認コマンドを入力します。この操作では確認対象の値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(SQLCACHE)
Command ===&gt; -DISPLAY STATS(EDM)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(SQLCACHE)
Command ===&gt; -DISPLAY STATS(EDM)
-DISPLAY STATS(SQLCACHE) が入力欄に表示されていれば、机上例の資源確認コマンドを実行する準備ができています。対象SSIDと表示範囲が目的に合っていることを確認します。
――――
■ ステップ 2
現在の画面は資源値確認の応答画面です。前ステップで送信したDb2コマンドまたは机上レポートの応答を読み取ります。操作欄には追加入力を入れず、対象値と警告の有無を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNT750I DYNAMIC STATEMENT CACHE CACHEDYN=YES HITRATIO=82
DSNT751I EDM STATEMENT POOL EDMSTMTC=113386 USED=64200
NORMAL COMPLETION
CACHEDYN=YES HITRATIO=82 が表示されていれば、机上例では対象資源の値を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、資源確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT750I DYNAMIC STATEMENT CACHE CACHEDYN=YES HITRATIO=82
DSNT751I EDM STATEMENT POOL EDMSTMTC=113386 USED=64200
ISSUER=USER1
CACHEDYN=YES HITRATIO=82 と ISSUER=USER1 が表示されていれば、誰がどの資源確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY STATS(SQLCACHE) が操作（入力）に記載されていること
② ステップ2 の CACHEDYN=YES HITRATIO=82 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>buffer pool defaults 確認手順</strong></p><p>検証目的: buffer pool defaultsの机上値を確認します。バッファプールサイズとしきい値を読み、データページの読み取り遅延や書き出し傾向を見る入口にします。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDS、SDSF、性能レポートまたはDISPLAY系の机上出力を確認できる前提です。実機でロック、EDM、RID、ソート、バッファプール関連値を変更する場合は、変更管理承認と対象SSID、ピーク時間帯、影響アプリケーションを事前に確認します。</p><p>セッション環境: DB2I COMMANDSまたはDSNセッションでDISPLAY系コマンドを入力し、SDSF SYSLOGや性能レポートの机上出力でロック待ち、EDM、RID、ソート、バッファプールの値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にロックまたはメモリ資源の確認コマンドを入力します。この操作では確認対象の値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY BUFFERPOOL(BP0) DETAIL
Command ===&gt; -ALTER BUFFERPOOL(BP0) VPSIZE(50000)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY BUFFERPOOL(BP0) DETAIL
Command ===&gt; -ALTER BUFFERPOOL(BP0) VPSIZE(50000)
-DISPLAY BUFFERPOOL(BP0) DETAIL が入力欄に表示されていれば、机上例の資源確認コマンドを実行する準備ができています。対象SSIDと表示範囲が目的に合っていることを確認します。
――――
■ ステップ 2
現在の画面は資源値確認の応答画面です。前ステップで送信したDb2コマンドまたは机上レポートの応答を読み取ります。操作欄には追加入力を入れず、対象値と警告の有無を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNB401I BUFFERPOOL BP0 VPSIZE=50000 VPSEQT=80 DWQT=30
DSNB402I ALTER BUFFERPOOL BP0 VPSIZE(50000) ACCEPTED
NORMAL COMPLETION
BUFFERPOOL BP0 VPSIZE=50000 が表示されていれば、机上例では対象資源の値を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、資源確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNB401I BUFFERPOOL BP0 VPSIZE=50000 VPSEQT=80 DWQT=30
DSNB402I ALTER BUFFERPOOL BP0 VPSIZE(50000) ACCEPTED
ISSUER=USER1
BUFFERPOOL BP0 VPSIZE=50000 と ISSUER=USER1 が表示されていれば、誰がどの資源確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY BUFFERPOOL(BP0) DETAIL が操作（入力）に記載されていること
② ステップ2 の BUFFERPOOL BP0 VPSIZE=50000 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>RID pool 確認手順</strong></p><p>検証目的: RID poolとsort poolの机上値を確認します。リストプリフェッチで使うRID領域と、ORDER BYやGROUP BYで使うソート領域を分けて読み取ります。</p><p>前提条件: TSO/ISPFにログオン済みです。DB2I COMMANDS、SDSF、性能レポートまたはDISPLAY系の机上出力を確認できる前提です。実機でロック、EDM、RID、ソート、バッファプール関連値を変更する場合は、変更管理承認と対象SSID、ピーク時間帯、影響アプリケーションを事前に確認します。</p><p>セッション環境: DB2I COMMANDSまたはDSNセッションでDISPLAY系コマンドを入力し、SDSF SYSLOGや性能レポートの机上出力でロック待ち、EDM、RID、ソート、バッファプールの値を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2I COMMANDS のコマンド入力画面です。Command ===&gt; にロックまたはメモリ資源の確認コマンドを入力します。この操作では確認対象の値が出るコマンドであることを見直してから送信します。
［操作（入力）］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(RIDPOOL)
Command ===&gt; -DISPLAY STATS(SORT)
→ Enter を押す
［画面・出力］
(DB2I COMMANDS)
Command ===&gt; -DISPLAY STATS(RIDPOOL)
Command ===&gt; -DISPLAY STATS(SORT)
-DISPLAY STATS(RIDPOOL) が入力欄に表示されていれば、机上例の資源確認コマンドを実行する準備ができています。対象SSIDと表示範囲が目的に合っていることを確認します。
――――
■ ステップ 2
現在の画面は資源値確認の応答画面です。前ステップで送信したDb2コマンドまたは机上レポートの応答を読み取ります。操作欄には追加入力を入れず、対象値と警告の有無を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(Command Response)
DSNT760I RIDPOOL MAXRBLK=400000 LIST PREFETCH ACTIVE
DSNT761I SORTPOOL MAXSORT_IN_MEMORY=20480 SRTPOOL=12000
NORMAL COMPLETION
RIDPOOL MAXRBLK=400000 が表示されていれば、机上例では対象資源の値を確認できています。NORMAL COMPLETION も同じ画面で確認し、異常メッセージがないことを見ます。
――――
■ ステップ 3
現在の画面は SDSF SYSLOG の一覧画面です。NP 欄に S を入力し、資源確認コマンドの応答がシステムログにも残っているか確認します。この操作で運用証跡として保存するメッセージを探します。
［操作（入力）］
(SDSF SYSLOG)
NP   DDNAME    StepName
S    SYSLOG    CONSOLE
→ Enter を押す
［画面・出力］
(SDSF SYSLOG)
DSNT760I RIDPOOL MAXRBLK=400000 LIST PREFETCH ACTIVE
DSNT761I SORTPOOL MAXSORT_IN_MEMORY=20480 SRTPOOL=12000
ISSUER=USER1
RIDPOOL MAXRBLK=400000 と ISSUER=USER1 が表示されていれば、誰がどの資源確認を行ったかを机上例として追跡できます。応答画面とSYSLOGの値が同じであることも確認します。
――――</pre><p>合格条件: ① ステップ1 の -DISPLAY STATS(RIDPOOL) が操作（入力）に記載されていること
② ステップ2 の RIDPOOL MAXRBLK=400000 が画面・出力に表示されること
③ ステップ3 の ISSUER=USER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>VALIDATE 確認手順</strong></p><p>検証目的: 既存パッケージのVALIDATE、ISOLATION、RELEASEをカタログで確認します。導入時の検査タイミング、分離レベル、資源解放タイミングを証跡化します。</p><p>前提条件: TSOログオン済みでSPUFIを起動でき、対象Db2のカタログ照会権限があること。BINDやREBINDの実行は行わず、既存パッケージのカタログ値を照会する机上確認に限定すること。</p><p>セッション環境: TSO/ISPFからSPUFIへ入り、DBD1サブシステムに対してカタログ照会SQLを実行する。ここでは机上例としてAPP1、PAYROLL、PKG01、V13R1M508を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に =SPUFI を入力し、SQLを実行するSPUFI画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象Db2へSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT COLLID, NAME, VALIDATE, ISOLATION, RELEASE FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;; から始まる照会を入力し、VALIDATEとISOLATION確認のカタログ値を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT COLLID, NAME, VALIDATE, ISOLATION, RELEASE FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
COLLID  NAME     VALIDATE  ISOLATION  RELEASE
APP1    PAYROLL  BIND      CS         COMMIT
1 ROW SELECTED
SQLCODE = 0
VALIDATE ISOLATION RELEASE がSPUFI OUTPUTに表示されていれば、VALIDATEとISOLATION確認の確認対象が取得できています。SQLCODE = 0 があれば、照会は正常終了しています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の VALIDATE ISOLATION RELEASE が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div><div class="kb-p"><p class="kb-pname"><strong>APPLCOMPAT 確認手順</strong></p><p>検証目的: 既存パッケージのアプリケーション互換性レベルを確認します。機能レベル移行後に、対象アプリケーションがどの互換性で動くかを証跡化します。</p><p>前提条件: TSOログオン済みでSPUFIを起動でき、対象Db2のカタログ照会権限があること。BINDやREBINDの実行は行わず、既存パッケージのカタログ値を照会する机上確認に限定すること。</p><p>セッション環境: TSO/ISPFからSPUFIへ入り、DBD1サブシステムに対してカタログ照会SQLを実行する。ここでは机上例としてAPP1、PAYROLL、PKG01、V13R1M508を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に =SPUFI を入力し、SQLを実行するSPUFI画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象Db2へSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT COLLID, NAME, APPLCOMPAT FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;; から始まる照会を入力し、APPLCOMPAT確認のカタログ値を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT COLLID, NAME, APPLCOMPAT FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
COLLID  NAME     APPLCOMPAT
APP1    PAYROLL  V13R1M508
1 ROW SELECTED
SQLCODE = 0
APPLCOMPAT V13R1M508 がSPUFI OUTPUTに表示されていれば、APPLCOMPAT確認の確認対象が取得できています。SQLCODE = 0 があれば、照会は正常終了しています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の APPLCOMPAT V13R1M508 が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div><div class="kb-p"><p class="kb-pname"><strong>EXPLAIN 確認手順</strong></p><p>検証目的: 既存パッケージのEXPLAIN、DEGREE、CURRENTDATAを確認します。性能レビューでアクセスパス出力、並列処理、現行データ要求の指定をまとめて残します。</p><p>前提条件: TSOログオン済みでSPUFIを起動でき、対象Db2のカタログ照会権限があること。BINDやREBINDの実行は行わず、既存パッケージのカタログ値を照会する机上確認に限定すること。</p><p>セッション環境: TSO/ISPFからSPUFIへ入り、DBD1サブシステムに対してカタログ照会SQLを実行する。ここでは机上例としてAPP1、PAYROLL、PKG01、V13R1M508を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に =SPUFI を入力し、SQLを実行するSPUFI画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象Db2へSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT COLLID, NAME, EXPLAIN, DEGREE, CURRENTDATA FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;; から始まる照会を入力し、EXPLAINとDEGREE確認のカタログ値を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT COLLID, NAME, EXPLAIN, DEGREE, CURRENTDATA FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
COLLID  NAME     EXPLAIN  DEGREE  CURRENTDATA
APP1    PAYROLL  YES      1       NO
1 ROW SELECTED
SQLCODE = 0
EXPLAIN DEGREE CURRENTDATA がSPUFI OUTPUTに表示されていれば、EXPLAINとDEGREE確認の確認対象が取得できています。SQLCODE = 0 があれば、照会は正常終了しています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の EXPLAIN DEGREE CURRENTDATA が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div><div class="kb-p"><p class="kb-pname"><strong>DYNAMICRULES 確認手順</strong></p><p>検証目的: 既存パッケージのDYNAMICRULESとKEEPDYNAMICを確認します。動的SQLの権限規則と、準備済み文をCOMMIT後も保持するかを証跡化します。</p><p>前提条件: TSOログオン済みでSPUFIを起動でき、対象Db2のカタログ照会権限があること。BINDやREBINDの実行は行わず、既存パッケージのカタログ値を照会する机上確認に限定すること。</p><p>セッション環境: TSO/ISPFからSPUFIへ入り、DBD1サブシステムに対してカタログ照会SQLを実行する。ここでは机上例としてAPP1、PAYROLL、PKG01、V13R1M508を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に =SPUFI を入力し、SQLを実行するSPUFI画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象Db2へSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT COLLID, NAME, DYNAMICRULES, KEEPDYNAMIC FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;; から始まる照会を入力し、動的SQL関連オプション確認のカタログ値を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT COLLID, NAME, DYNAMICRULES, KEEPDYNAMIC FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
COLLID  NAME     DYNAMICRULES  KEEPDYNAMIC
APP1    PAYROLL  RUN           NO
1 ROW SELECTED
SQLCODE = 0
DYNAMICRULES KEEPDYNAMIC がSPUFI OUTPUTに表示されていれば、動的SQL関連オプション確認の確認対象が取得できています。SQLCODE = 0 があれば、照会は正常終了しています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の DYNAMICRULES KEEPDYNAMIC が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div><div class="kb-p"><p class="kb-pname"><strong>PLANMGMT 確認手順</strong></p><p>検証目的: 既存パッケージのPLANMGMTとPATHを確認します。再バインド時の戻し可能性と、未修飾ルーチン名の探索順序を証跡化します。</p><p>前提条件: TSOログオン済みでSPUFIを起動でき、対象Db2のカタログ照会権限があること。BINDやREBINDの実行は行わず、既存パッケージのカタログ値を照会する机上確認に限定すること。</p><p>セッション環境: TSO/ISPFからSPUFIへ入り、DBD1サブシステムに対してカタログ照会SQLを実行する。ここでは机上例としてAPP1、PAYROLL、PKG01、V13R1M508を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO READYです。COMMAND ===&gt; に =SPUFI を入力し、SQLを実行するSPUFI画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象Db2へSQLを入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面はSPUFIのSQL入力画面です。SQL INPUT ===&gt; に SELECT COLLID, NAME, PLANMGMT, PATH FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;; から始まる照会を入力し、PLANMGMTとPATH確認のカタログ値を取得します。
［操作（入力）］
SQL INPUT ===&gt; SELECT COLLID, NAME, PLANMGMT, PATH FROM SYSIBM.SYSPACKAGE WHERE COLLID = &#x27;APP1&#x27; AND NAME = &#x27;PAYROLL&#x27;;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
COLLID  NAME     PLANMGMT  PATH
APP1    PAYROLL  EXTENDED  SYSIBM,APP1
1 ROW SELECTED
SQLCODE = 0
PLANMGMT PATH がSPUFI OUTPUTに表示されていれば、PLANMGMTとPATH確認の確認対象が取得できています。SQLCODE = 0 があれば、照会は正常終了しています。
――――
■ ステップ 3
現在の画面はSPUFIの結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えてTSO READYへ戻します。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFIを抜けてTSO READY状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の PLANMGMT PATH が表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_AppProg_SQL_Guide p.862 / Db2_zOS_WhatsNew.pdf p.334</p></div><div class="kb-p"><p class="kb-pname"><strong>LOAD 確認手順</strong></p><p>検証目的: LOADとUNLOADの基本制御文を確認します。外部データの投入と表データの抽出を同じDSNUTILB実行形式で見比べます。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象オブジェクトを検証用に限定し、更新系ユーティリティは変更管理承認後に実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNUTILB出力を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UB01 JOB (ACCT),&#x27;DB2UTIL&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB01&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSREC DD DISP=SHR,DSN=USER1.DB2.LOADIN
000002 //UNLDOUT DD DSN=USER1.DB2.UNLOAD.PAYROLL,DISP=(NEW,CATLG),UNIT=SYSDA,SPACE=(CYL,(10,5))
000002 //SYSIN DD *
000002   LOAD DATA INDDN SYSREC RESUME YES INTO TABLE APP1.PAYROLL
000002   UNLOAD TABLESPACE PAYDB.PAYTS UNLDDN UNLDOUT
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB01 JOB (ACCT),&#x27;DB2UTIL&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB01&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB01 JOB (ACCT),&#x27;DB2UTIL&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB01&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UB01 saved
Member UB01 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UB01)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UB01)&#x27;
→ Enter を押す
［画面・出力］
JOB UB01 SUBMITTED
IKJ56250I JOB UB01(JOB01234) SUBMITTED
JOB UB01 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UB01 のジョブログを開きます。この操作でDSNUTILBのメッセージとユーティリティ本体の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UB01   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
LOAD TABLE=APP1.PAYROLL RESUME=YES
UNLOAD TABLESPACE=PAYDB.PAYTS UNLDDN=UNLDOUT
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、LOAD TABLE=APP1.PAYROLL RESUME=YES、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。対象名とユーティリティ名がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UB01 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と LOAD TABLE=APP1.PAYROLL RESUME=YES が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>COPY 確認手順</strong></p><p>検証目的: COPYとRECOVERの基本制御文を確認します。イメージコピーの取得と、コピー・ログを使った回復の関係を机上例で追います。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象オブジェクトを検証用に限定し、更新系ユーティリティは変更管理承認後に実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNUTILB出力を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UB02 JOB (ACCT),&#x27;DB2RCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB02&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //COPYDD DD DSN=USER1.DB2.COPY.PAYTS,DISP=(NEW,CATLG),UNIT=SYSDA,SPACE=(CYL,(20,5))
000002 //SYSIN DD *
000002   COPY TABLESPACE PAYDB.PAYTS COPYDDN(COPYDD) SHRLEVEL REFERENCE
000002   RECOVER TABLESPACE PAYDB.PAYTS TOLOGPOINT X&#x27;000000000123&#x27;
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB02 JOB (ACCT),&#x27;DB2RCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB02&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB02 JOB (ACCT),&#x27;DB2RCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB02&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UB02 saved
Member UB02 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UB02)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UB02)&#x27;
→ Enter を押す
［画面・出力］
JOB UB02 SUBMITTED
IKJ56250I JOB UB02(JOB01234) SUBMITTED
JOB UB02 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UB02 のジョブログを開きます。この操作でDSNUTILBのメッセージとユーティリティ本体の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UB02   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
COPY TABLESPACE=PAYDB.PAYTS COPYDDN=COPYDD SHRLEVEL=REFERENCE
RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000123&#x27;
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000123&#x27;、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。対象名とユーティリティ名がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UB02 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000123&#x27; が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>REORG TABLESPACE 確認手順</strong></p><p>検証目的: REORG TABLESPACE、REORG INDEX、RUNSTATSの基本制御文を確認します。物理配置の整理と統計収集を分けて読めるようにします。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象オブジェクトを検証用に限定し、更新系ユーティリティは変更管理承認後に実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNUTILB出力を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UB03 JOB (ACCT),&#x27;DB2REORG&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB03&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSIN DD *
000002   REORG TABLESPACE PAYDB.PAYTS SHRLEVEL REFERENCE
000002   REORG INDEX APP1.PAYIX SHRLEVEL REFERENCE
000002   RUNSTATS TABLESPACE PAYDB.PAYTS TABLE(ALL) INDEX(ALL) UPDATE ALL REPORT YES
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB03 JOB (ACCT),&#x27;DB2REORG&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB03&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB03 JOB (ACCT),&#x27;DB2REORG&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB03&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UB03 saved
Member UB03 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UB03)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UB03)&#x27;
→ Enter を押す
［画面・出力］
JOB UB03 SUBMITTED
IKJ56250I JOB UB03(JOB01234) SUBMITTED
JOB UB03 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UB03 のジョブログを開きます。この操作でDSNUTILBのメッセージとユーティリティ本体の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UB03   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
REORG TABLESPACE=PAYDB.PAYTS SHRLEVEL=REFERENCE
REORG INDEX=APP1.PAYIX SHRLEVEL=REFERENCE
RUNSTATS TABLESPACE=PAYDB.PAYTS UPDATE=ALL REPORT=YES
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、REORG TABLESPACE=PAYDB.PAYTS SHRLEVEL=REFERENCE、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。対象名とユーティリティ名がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UB03 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と REORG TABLESPACE=PAYDB.PAYTS SHRLEVEL=REFERENCE が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CHECK DATA 確認手順</strong></p><p>検証目的: CHECK DATA、CHECK INDEX、REBUILD INDEXを確認します。整合性検査から索引再構築へ進む保守の流れを机上例で確認します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象オブジェクトを検証用に限定し、更新系ユーティリティは変更管理承認後に実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNUTILB出力を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UB04 JOB (ACCT),&#x27;DB2CHK&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB04&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSIN DD *
000002   CHECK DATA TABLESPACE PAYDB.PAYTS
000002   CHECK INDEX APP1.PAYIX
000002   REBUILD INDEX APP1.PAYIX
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB04 JOB (ACCT),&#x27;DB2CHK&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB04&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB04 JOB (ACCT),&#x27;DB2CHK&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB04&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UB04 saved
Member UB04 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UB04)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UB04)&#x27;
→ Enter を押す
［画面・出力］
JOB UB04 SUBMITTED
IKJ56250I JOB UB04(JOB01234) SUBMITTED
JOB UB04 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UB04 のジョブログを開きます。この操作でDSNUTILBのメッセージとユーティリティ本体の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UB04   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
CHECK DATA TABLESPACE=PAYDB.PAYTS
CHECK INDEX=APP1.PAYIX
REBUILD INDEX=APP1.PAYIX
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、CHECK DATA TABLESPACE=PAYDB.PAYTS、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。対象名とユーティリティ名がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UB04 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と CHECK DATA TABLESPACE=PAYDB.PAYTS が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>MODIFY RECOVERY 確認手順</strong></p><p>検証目的: MODIFY RECOVERY、MODIFY STATISTICS、QUIESCE、MERGECOPY、REPORT RECOVERY、REPAIR、DIAGNOSEの役割を確認します。回復履歴整理、整合点作成、診断・修復系を混同しないようにします。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象オブジェクトを検証用に限定し、更新系ユーティリティは変更管理承認後に実行します。</p><p>セッション環境: ISPF EditでJCLを入力・保存し、TSO SUBMITで投入後、SDSF STでDSNUTILB出力を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UB05 JOB (ACCT),&#x27;DB2MAINT&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB05&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSIN DD *
000002   MODIFY RECOVERY TABLESPACE PAYDB.PAYTS DELETE AGE(30)
000002   MODIFY STATISTICS TABLESPACE PAYDB.PAYTS DELETE AGE(30)
000002   QUIESCE TABLESPACE PAYDB.PAYTS WRITE YES
000002   MERGECOPY TABLESPACE PAYDB.PAYTS
000002   REPORT RECOVERY TABLESPACE PAYDB.PAYTS
000002   DIAGNOSE DISPLAY TABLESPACE PAYDB.PAYTS
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB05 JOB (ACCT),&#x27;DB2MAINT&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB05&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UB05 JOB (ACCT),&#x27;DB2MAINT&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UB05&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UB05 saved
Member UB05 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UB05)&#x27; を入力し、保存済みJCLを投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UB05)&#x27;
→ Enter を押す
［画面・出力］
JOB UB05 SUBMITTED
IKJ56250I JOB UB05(JOB01234) SUBMITTED
JOB UB05 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UB05 のジョブログを開きます。この操作でDSNUTILBのメッセージとユーティリティ本体の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UB05   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
MODIFY RECOVERY TABLESPACE=PAYDB.PAYTS DELETE AGE=30
MODIFY STATISTICS TABLESPACE=PAYDB.PAYTS DELETE AGE=30
QUIESCE TABLESPACE=PAYDB.PAYTS WRITE=YES
MERGECOPY TABLESPACE=PAYDB.PAYTS
REPORT RECOVERY TABLESPACE=PAYDB.PAYTS
DIAGNOSE DISPLAY TABLESPACE=PAYDB.PAYTS
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、REPORT RECOVERY TABLESPACE=PAYDB.PAYTS、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。対象名とユーティリティ名がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UB05 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と REPORT RECOVERY TABLESPACE=PAYDB.PAYTS が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>OPTIONS TEMPLATEDD 確認手順</strong></p><p>検証目的: OPTIONS TEMPLATEDD、TEMPLATE、LISTDEF、INCLUDE、EXCLUDEを含むDSNUTILB制御文を確認します。外部TEMPLATEライブラリと対象リストがCOPY制御文で参照される形を追えるようにします。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象表スペースを検証用に限定し、業務データを更新しない環境で実施します。</p><p>セッション環境: ISPF EditでJCLを保存し、TSO SUBMITで投入後、SDSF STでジョブログを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UTL01 JOB (ACCT),&#x27;DB2UTIL&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL01&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //UTEMPL DD DISP=SHR,DSN=USER1.DB2.TEMPLATE
000002 //SYSIN DD *
000002   OPTIONS TEMPLATEDD UTEMPL
000002   LISTDEF PAYLIST INCLUDE TABLESPACES DATABASE PAYDB EXCLUDE TABLESPACE PAYDB.OLDTS
000002   COPY LIST PAYLIST COPYDDN(CPY) SHRLEVEL REFERENCE
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL01 JOB (ACCT),&#x27;DB2UTIL&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL01&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL01 JOB (ACCT),&#x27;DB2UTIL&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL01&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UTL01 saved
Member UTL01 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL01)&#x27; を入力し、保存済みJCLをJESへ投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL01)&#x27;
→ Enter を押す
［画面・出力］
JOB UTL01 SUBMITTED
IKJ56250I JOB UTL01(JOB01234) SUBMITTED
JOB UTL01 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UTL01 のジョブログを開きます。この操作でDSNUTILBのメッセージと制御文の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UTL01   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
OPTIONS TEMPLATEDD=UTEMPL
LISTDEF=PAYLIST INCLUDE=PAYDB EXCLUDE=PAYDB.OLDTS
COPY LIST PAYLIST COPYDDN=CPY SHRLEVEL=REFERENCE
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、LISTDEF=PAYLIST INCLUDE=PAYDB EXCLUDE=PAYDB.OLDTS、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。出力内の対象名とオプション値がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UTL01 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と LISTDEF=PAYLIST INCLUDE=PAYDB EXCLUDE=PAYDB.OLDTS が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide p.810</p></div><div class="kb-p"><p class="kb-pname"><strong>SHRLEVEL 確認手順</strong></p><p>検証目的: COPYのSHRLEVEL、COPYDDN、RECOVERYDDNを確認します。ローカルサイト用コピーとリカバリーサイト用コピーを分け、ユーティリティ実行中の共有レベルも確認します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象表スペースを検証用に限定し、業務データを更新しない環境で実施します。</p><p>セッション環境: ISPF EditでJCLを保存し、TSO SUBMITで投入後、SDSF STでジョブログを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UTL03 JOB (ACCT),&#x27;DB2COPY&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL03&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSIN DD *
000002   TEMPLATE CPY DSN(&#x27;USER1.COPY.&amp;DB..&amp;TS..P&#x27;) UNIT SYSDA SPACE CYL(10,5) DISP(NEW,CATLG,CATLG)
000002   TEMPLATE RCV DSN(&#x27;USER1.RECV.&amp;DB..&amp;TS..P&#x27;) UNIT SYSDA SPACE CYL(10,5) DISP(NEW,CATLG,CATLG)
000002   COPY TABLESPACE PAYDB.PAYTS COPYDDN(CPY,CPY) RECOVERYDDN(RCV,RCV) SHRLEVEL REFERENCE
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL03 JOB (ACCT),&#x27;DB2COPY&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL03&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL03 JOB (ACCT),&#x27;DB2COPY&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL03&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UTL03 saved
Member UTL03 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL03)&#x27; を入力し、保存済みJCLをJESへ投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL03)&#x27;
→ Enter を押す
［画面・出力］
JOB UTL03 SUBMITTED
IKJ56250I JOB UTL03(JOB01234) SUBMITTED
JOB UTL03 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UTL03 のジョブログを開きます。この操作でDSNUTILBのメッセージと制御文の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UTL03   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
COPY TABLESPACE=PAYDB.PAYTS COPYDDN=CPY RECOVERYDDN=RCV SHRLEVEL=REFERENCE
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、COPYDDN=CPY RECOVERYDDN=RCV SHRLEVEL=REFERENCE、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。出力内の対象名とオプション値がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UTL03 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と COPYDDN=CPY RECOVERYDDN=RCV SHRLEVEL=REFERENCE が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide p.810</p></div><div class="kb-p"><p class="kb-pname"><strong>RESUME 確認手順</strong></p><p>検証目的: LOADのRESUME、REPLACE、LOG、ENFORCE、DISCARDS、SORTKEYSを確認します。追記か入替か、ログ取得と制約検査、破棄件数、ソートキー指定を一つのSYSINで読み取れるようにします。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象表スペースを検証用に限定し、業務データを更新しない環境で実施します。</p><p>セッション環境: ISPF EditでJCLを保存し、TSO SUBMITで投入後、SDSF STでジョブログを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UTL02 JOB (ACCT),&#x27;DB2LOAD&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL02&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSREC DD DISP=SHR,DSN=USER1.DB2.LOADIN
000002 //SYSIN DD *
000002   LOAD DATA INDDN SYSREC RESUME YES LOG NO ENFORCE NO DISCARDS 10 SORTKEYS NO INTO TABLE APP1.PAYROLL
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL02 JOB (ACCT),&#x27;DB2LOAD&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL02&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL02 JOB (ACCT),&#x27;DB2LOAD&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL02&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UTL02 saved
Member UTL02 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL02)&#x27; を入力し、保存済みJCLをJESへ投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL02)&#x27;
→ Enter を押す
［画面・出力］
JOB UTL02 SUBMITTED
IKJ56250I JOB UTL02(JOB01234) SUBMITTED
JOB UTL02 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UTL02 のジョブログを開きます。この操作でDSNUTILBのメッセージと制御文の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UTL02   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
LOAD TABLE=APP1.PAYROLL RESUME=YES LOG=NO ENFORCE=NO DISCARDS=10 SORTKEYS=NO
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、RESUME=YES LOG=NO ENFORCE=NO DISCARDS=10 SORTKEYS=NO、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。出力内の対象名とオプション値がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UTL02 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と RESUME=YES LOG=NO ENFORCE=NO DISCARDS=10 SORTKEYS=NO が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide p.810</p></div><div class="kb-p"><p class="kb-pname"><strong>STATISTICS 確認手順</strong></p><p>検証目的: RUNSTATSのSTATISTICS、KEYCARD、FREQVAL、HISTOGRAM、UPDATE、REPORTを確認します。統計収集、カタログ更新、レポート出力が同じ制御文でどう表れるかを確認します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象表スペースを検証用に限定し、業務データを更新しない環境で実施します。</p><p>セッション環境: ISPF EditでJCLを保存し、TSO SUBMITで投入後、SDSF STでジョブログを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UTL04 JOB (ACCT),&#x27;DB2STAT&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL04&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSIN DD *
000002   RUNSTATS TABLESPACE PAYDB.PAYTS TABLE(ALL) INDEX(ALL) KEYCARD FREQVAL NUMCOLS 1 COUNT 10 MOST HISTOGRAM NUMCOLS 1 NUMQUANTILES 5 UPDATE ALL REPORT YES
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL04 JOB (ACCT),&#x27;DB2STAT&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL04&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL04 JOB (ACCT),&#x27;DB2STAT&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL04&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UTL04 saved
Member UTL04 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL04)&#x27; を入力し、保存済みJCLをJESへ投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL04)&#x27;
→ Enter を押す
［画面・出力］
JOB UTL04 SUBMITTED
IKJ56250I JOB UTL04(JOB01234) SUBMITTED
JOB UTL04 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UTL04 のジョブログを開きます。この操作でDSNUTILBのメッセージと制御文の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UTL04   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
RUNSTATS TABLESPACE=PAYDB.PAYTS KEYCARD=YES FREQVAL=YES HISTOGRAM=YES UPDATE=ALL REPORT=YES
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、KEYCARD=YES FREQVAL=YES HISTOGRAM=YES UPDATE=ALL REPORT=YES、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。出力内の対象名とオプション値がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UTL04 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と KEYCARD=YES FREQVAL=YES HISTOGRAM=YES UPDATE=ALL REPORT=YES が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide p.810</p></div><div class="kb-p"><p class="kb-pname"><strong>TORBA 確認手順</strong></p><p>検証目的: RECOVERのTORBA、TOLOGPOINT、FROMCOPY、RESTOREBEFORE、LOGONLYを確認します。回復停止点、回復元コピー、ログだけを適用する運用を机上例で確認します。</p><p>前提条件: TSO/ISPFにログオン済みです。ISPF Editで USER1.DB2UTIL.JCL を編集でき、Db2サブシステム DB2A に対するDSNUTILB実行権限があります。実機では対象表スペースを検証用に限定し、業務データを更新しない環境で実施します。</p><p>セッション環境: ISPF EditでJCLを保存し、TSO SUBMITで投入後、SDSF STでジョブログを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面は ISPF Edit のJCL編集画面です。本文入力行にDSNUTILBを実行するJCLとSYSIN制御文を入力します。この操作では本文入力行だけを使い、保存コマンドは次のステップで実行します。
［操作（入力）］
(ISPF Edit)
Command ===&gt;
000001 //UTL05 JOB (ACCT),&#x27;DB2RCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL05&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
000002 //SYSIN DD *
000002   RECOVER TABLESPACE PAYDB.PAYTS TOLOGPOINT X&#x27;000000000123&#x27; FROMCOPY FULLCOPY1 RESTOREBEFORE X&#x27;000000000123&#x27; LOGONLY
000002 /*
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL05 JOB (ACCT),&#x27;DB2RCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL05&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
000001 から始まるJCL行が表示されていれば、本文入力行に検証用JCLが入っています。画面にDSNUTILBとSYSIN制御文の先頭が見えていることを確認します。
――――
■ ステップ 2
現在の画面は ISPF Edit のJCL編集画面です。Command ===&gt; に SAVE を入力し、前ステップで入力したJCL本文をメンバーへ保存します。本文入力行には追加で文字を入れません。
［操作（入力）］
(ISPF Edit)
Command ===&gt; SAVE
→ Enter を押す
［画面・出力］
(ISPF Edit)
Command ===&gt;
000001 //UTL05 JOB (ACCT),&#x27;DB2RCV&#x27;,CLASS=A,MSGCLASS=X
000002 //UTIL EXEC PGM=DSNUTILB,PARM=&#x27;DB2A,UTL05&#x27;
000002 //STEPLIB DD DISP=SHR,DSN=DB2A.SDSNLOAD
...
****** ***************************** Bottom of Data ******************************
Member UTL05 saved
Member UTL05 saved が表示されていれば、JCLとSYSIN制御文が保存されています。画面にはDSNUTILBと検証対象の制御文が残っていることも確認します。
――――
■ ステップ 3
現在の画面は TSO READY のコマンド入力画面です。Command ===&gt; に SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL05)&#x27; を入力し、保存済みJCLをJESへ投入します。投入後はジョブIDを控えてSDSFで同じジョブを開きます。
［操作（入力）］
(TSO READY)
Command ===&gt; SUBMIT &#x27;USER1.DB2UTIL.JCL(UTL05)&#x27;
→ Enter を押す
［画面・出力］
JOB UTL05 SUBMITTED
IKJ56250I JOB UTL05(JOB01234) SUBMITTED
JOB UTL05 SUBMITTED と IKJ56250I が表示されていれば、JESへ投入されています。JOB01234 は机上例のジョブIDであり、実行ごとに変わります。
――――
■ ステップ 4
現在の画面は SDSF ST のジョブ一覧画面です。NP 欄に S を入力し、投入した UTL05 のジョブログを開きます。この操作でDSNUTILBのメッセージと制御文の反映結果を確認します。
［操作（入力）］
(SDSF ST)
NP   JOBNAME  JobID    Owner    Queue
S    UTL05   JOB01234 USER1    OUTPUT
→ Enter を押す
［画面・出力］
(SDSF Job Output)
DSNU000I DSNUTILB STARTED, SSID=DB2A
RECOVER TABLESPACE=PAYDB.PAYTS TOLOGPOINT=X&#x27;000000000123&#x27; FROMCOPY=FULLCOPY1 RESTOREBEFORE=X&#x27;000000000123&#x27; LOGONLY=YES
DSNU010I DSNUTILB COMPLETED, MAXCC=0
DSNU000I、TOLOGPOINT=X&#x27;000000000123&#x27; FROMCOPY=FULLCOPY1 RESTOREBEFORE=X&#x27;000000000123&#x27; LOGONLY=YES、MAXCC=0 が表示されていれば、机上例では制御文が受理され正常終了した形です。出力内の対象名とオプション値がJCLのSYSINと一致していることを確認します。
――――</pre><p>合格条件: ① ステップ3 の JOB UTL05 SUBMITTED が画面・出力に表示されること
② ステップ4 の DSNU000I と TOLOGPOINT=X&#x27;000000000123&#x27; FROMCOPY=FULLCOPY1 RESTOREBEFORE=X&#x27;000000000123&#x27; LOGONLY=YES が画面・出力に表示されること
③ ステップ4 の MAXCC=0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Utility_Guide p.810</p></div><div class="kb-p"><p class="kb-pname"><strong>START DB2 PARM（Db2コマンド指定） 確認手順</strong></p><p>検証目的: START DB2 の PARM と STOP DB2 の MODE を、DB2 COMMANDS パネルで入力した場合の証跡として整理します。起動モジュールと停止方式の違いを手順上で分離します。</p><p>前提条件: TSO/ISPF にログオン済みです。DB2 COMMANDS パネルを開ける権限があります。対象サブシステム DB2A の運用コマンド実行権限があります。机上手順のため、実機では変更管理承認後に実行します。</p><p>セッション環境: ISPF DB2 COMMANDS パネル</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A START DB2 PARM(DSNZP001) を入力します。この操作で 起動時に読み込むパラメーターモジュール を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A START DB2 PARM(DSNZP001)
→ Enter を押す
［画面・出力］
DSN9022I -DB2A DSNYASCP &#x27;START DB2 PARM(DSNZP001)&#x27; NORMAL COMPLETION
DSN9022I と START DB2 PARM(DSNZP001) が表示されていれば、机上例では起動コマンドが正常完了した証跡になります。
――――
■ ステップ 2
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A STOP DB2 MODE(QUIESCE) を入力します。この操作で 停止方式に QUIESCE を指定する操作 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A STOP DB2 MODE(QUIESCE)
→ Enter を押す
［画面・出力］
DSN9022I -DB2A DSNYASCP &#x27;STOP DB2 MODE(QUIESCE)&#x27; NORMAL COMPLETION
DSN9022I と STOP DB2 MODE(QUIESCE) が同じ出力にあれば、停止方式を指定した操作として記録できます。
――――</pre><p>合格条件: ① ステップ1 の DSN9022I に START DB2 と DSNZP001 が含まれること
② ステップ2 の DSN9022I に STOP DB2 と QUIESCE が含まれること
③ ステップ1 とステップ2 の DB2A が同じサブシステム ID であること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div><div class="kb-p"><p class="kb-pname"><strong>START DDF（Db2コマンド指定） 確認手順</strong></p><p>検証目的: START DDF、STOP DDF、DISPLAY DDF の操作と出力を分けて、分散接続の起動状態を確認します。DDF の開始停止と状態表示を同じ手順で混同しないようにします。</p><p>前提条件: TSO/ISPF にログオン済みです。DB2 COMMANDS パネルを開ける権限があります。対象サブシステム DB2A の運用コマンド実行権限があります。机上手順のため、実機では変更管理承認後に実行します。</p><p>セッション環境: ISPF DB2 COMMANDS パネル</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A START DDF を入力します。この操作で DDF を開始する操作 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A START DDF
→ Enter を押す
［画面・出力］
DSNL004I -DB2A DDF START COMPLETE
DSN9022I -DB2A DSNLSTRT &#x27;START DDF&#x27; NORMAL COMPLETION
DSNL004I と DDF START COMPLETE が出ていれば、分散接続機能の開始を確認できます。
――――
■ ステップ 2
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A DISPLAY DDF を入力します。この操作で DDF の状態と接続情報 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A DISPLAY DDF
→ Enter を押す
［画面・出力］
DSNL080I -DB2A DISPLAY DDF REPORT FOLLOWS
LOCATION=DB2A.LOCAL  TCPPORT=446  STATUS=STARTED
DSN9022I -DB2A DSNLTDDF &#x27;DISPLAY DDF&#x27; NORMAL COMPLETION
DSNL080I、LOCATION=DB2A.LOCAL、STATUS=STARTED が表示されていれば、DDF の状態表示として使えます。
――――
■ ステップ 3
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A STOP DDF MODE(SUSPEND) を入力します。この操作で DDF を停止または中断する操作 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A STOP DDF MODE(SUSPEND)
→ Enter を押す
［画面・出力］
DSNL010I -DB2A DDF STOP COMPLETE MODE(SUSPEND)
DSN9022I -DB2A DSNLSTOP &#x27;STOP DDF&#x27; NORMAL COMPLETION
DSNL010I と MODE(SUSPEND) が表示されていれば、DDF 停止方式を指定した証跡になります。
――――</pre><p>合格条件: ① ステップ1 の DSNL004I に DDF START COMPLETE が含まれること
② ステップ2 の DSNL080I に LOCATION と TCPPORT が含まれること
③ ステップ3 の DSNL010I に DDF STOP COMPLETE が含まれること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY THREAD TYPE（Db2コマンド指定） 確認手順</strong></p><p>検証目的: DISPLAY THREAD、DISPLAY DATABASE、DISPLAY GROUP の表示キーワードを分けて確認します。スレッド種別、表スペース範囲、Data Sharing グループ状態を別の証跡として扱います。</p><p>前提条件: TSO/ISPF にログオン済みです。DB2 COMMANDS パネルを開ける権限があります。対象サブシステム DB2A の運用コマンド実行権限があります。机上手順のため、実機では変更管理承認後に実行します。</p><p>セッション環境: ISPF DB2 COMMANDS パネル</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A DISPLAY THREAD(*) TYPE(PROC) DETAIL を入力します。この操作で ストアードプロシージャー実行中スレッドの詳細表示 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A DISPLAY THREAD(*) TYPE(PROC) DETAIL
→ Enter を押す
［画面・出力］
DSNV401I -DB2A DISPLAY THREAD REPORT FOLLOWS
TYPE(PROC)  NAME=PROC  AUTHID=APPUSR  PLAN=DSNTEP2  TOKEN=23
DSN9022I -DB2A DSNVDT &#x27;DISPLAY THREAD&#x27; NORMAL COMPLETION
DSNV401I と TYPE(PROC) があり、AUTHID と PLAN が表示されていれば、スレッド詳細の証跡になります。
――――
■ ステップ 2
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) USE を入力します。この操作で 指定表スペースの使用状況 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A DISPLAY DATABASE(PAYDB) SPACENAM(PAYTS) USE
→ Enter を押す
［画面・出力］
DSNT360I -DB2A DISPLAY DATABASE REPORT FOLLOWS
DATABASE=PAYDB  SPACENAM=PAYTS  STATUS=RW  USE=APPUSR
DSN9022I -DB2A DSNTDDIS &#x27;DISPLAY DATABASE&#x27; NORMAL COMPLETION
DSNT360I、DATABASE=PAYDB、SPACENAM=PAYTS が表示されていれば、対象スペースの状態確認として記録できます。
――――
■ ステップ 3
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A DISPLAY GROUP DETAIL を入力します。この操作で Data Sharing グループの詳細状態 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A DISPLAY GROUP DETAIL
→ Enter を押す
［画面・出力］
DSN7100I -DB2A DISPLAY GROUP REPORT FOLLOWS
GROUP=DB2G  MEMBER=DB2A  STATUS=ACTIVE  LEVEL=V13R1M500
DSN9022I -DB2A DSN7GCMD &#x27;DISPLAY GROUP&#x27; NORMAL COMPLETION
DSN7100I、GROUP=DB2G、MEMBER=DB2A が同じ出力にあるため、グループ詳細の表示結果として扱えます。
――――</pre><p>合格条件: ① ステップ1 の DSNV401I に TYPE(PROC) が含まれること
② ステップ2 の DSNT360I に PAYDB と PAYTS が含まれること
③ ステップ3 の DSN7100I に DB2G と MEMBER が含まれること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div><div class="kb-p"><p class="kb-pname"><strong>DISPLAY UTILITY（Db2コマンド指定） 確認手順</strong></p><p>検証目的: DISPLAY UTILITY、TERM UTILITY、ARCHIVE LOG、RECOVER BSDS の操作を机上証跡に分けます。ユーティリティ状態、ログ切替、BSDS復旧を同一操作として扱わないようにします。</p><p>前提条件: TSO/ISPF にログオン済みです。DB2 COMMANDS パネルを開ける権限があります。対象サブシステム DB2A の運用コマンド実行権限があります。机上手順のため、実機では変更管理承認後に実行します。</p><p>セッション環境: ISPF DB2 COMMANDS パネル</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A DISPLAY UTILITY(UTIL123) を入力します。この操作で ユーティリティの現在フェーズ表示 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A DISPLAY UTILITY(UTIL123)
→ Enter を押す
［画面・出力］
DSNU105I -DB2A DISPLAY UTILITY REPORT FOLLOWS
UTILID=UTIL123  NAME=LOAD  PHASE=RELOAD  STATUS=STOPPED
DSN9022I -DB2A DSNUTIL &#x27;DISPLAY UTILITY&#x27; NORMAL COMPLETION
DSNU105I、UTILID=UTIL123、PHASE=RELOAD が表示されていれば、ユーティリティ状態の証跡になります。
――――
■ ステップ 2
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A TERM UTILITY(UTIL123) を入力します。この操作で 残存ユーティリティ状態の終了扱い を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A TERM UTILITY(UTIL123)
→ Enter を押す
［画面・出力］
DSNU112I -DB2A TERM UTILITY(UTIL123) ACCEPTED
DSN9022I -DB2A DSNUTIL &#x27;TERM UTILITY&#x27; NORMAL COMPLETION
DSNU112I と TERM UTILITY(UTIL123) が出ていれば、対象ユーティリティを終了扱いにした記録になります。
――――
■ ステップ 3
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A ARCHIVE LOG MODE(QUIESCE) を入力します。この操作で アクティブログのアーカイブ要求 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A ARCHIVE LOG MODE(QUIESCE)
→ Enter を押す
［画面・出力］
DSNJ110I -DB2A ARCHIVE LOG MODE(QUIESCE) ACCEPTED
ARCHIVE LOG DATA SET=DB2A.ARCHLOG1.A0001234
DSN9022I -DB2A DSNJLOG &#x27;ARCHIVE LOG&#x27; NORMAL COMPLETION
DSNJ110I と ARCHIVE LOG DATA SET=DB2A.ARCHLOG1.A0001234 が表示されていれば、ログ切替の証跡になります。
――――
■ ステップ 4
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A RECOVER BSDS を入力します。この操作で BSDS 二重化の回復操作 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A RECOVER BSDS
→ Enter を押す
［画面・出力］
DSNJ125I -DB2A RECOVER BSDS SUCCESSFUL
DUAL BSDS MODE REESTABLISHED
DSN9022I -DB2A DSNJBSDS &#x27;RECOVER BSDS&#x27; NORMAL COMPLETION
DSNJ125I と DUAL BSDS MODE REESTABLISHED が表示されていれば、BSDS 二重化回復の机上証跡になります。
――――</pre><p>合格条件: ① ステップ1 の DSNU105I に UTIL123 と PHASE=RELOAD が含まれること
② ステップ2 の DSNU112I に TERM UTILITY(UTIL123) が含まれること
③ ステップ3 の DSNJ110I に ARCHIVE LOG MODE(QUIESCE) が含まれること
④ ステップ4 の DSNJ125I に RECOVER BSDS が含まれること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div><div class="kb-p"><p class="kb-pname"><strong>START TRACE class（Db2コマンド指定） 確認手順</strong></p><p>検証目的: START TRACE の CLASS、IFCID、DEST を分けて入力し、収集対象と出力先の違いを証跡化します。IBM Support 指示の調査で指定値を取り違えないようにします。</p><p>前提条件: TSO/ISPF にログオン済みです。DB2 COMMANDS パネルを開ける権限があります。対象サブシステム DB2A の運用コマンド実行権限があります。机上手順のため、実機では変更管理承認後に実行します。</p><p>セッション環境: ISPF DB2 COMMANDS パネル</p><pre class="kb-code">■ ステップ 1
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A START TRACE(PERFM) CLASS(1,2) を入力します。この操作で 性能トレースのクラス指定 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A START TRACE(PERFM) CLASS(1,2)
→ Enter を押す
［画面・出力］
DSNW130I -DB2A TRACE STARTED
TRACE(PERFM) CLASS(1,2) DEST(GTF)
DSN9022I -DB2A DSNWVCM1 &#x27;START TRACE&#x27; NORMAL COMPLETION
DSNW130I、TRACE(PERFM)、CLASS(1,2) が出ていれば、クラス指定の開始として確認できます。
――――
■ ステップ 2
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A START TRACE(PERFM) CLASS(30) IFCID(0006,0007) を入力します。この操作で イベント番号を指定したトレース開始 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A START TRACE(PERFM) CLASS(30) IFCID(0006,0007)
→ Enter を押す
［画面・出力］
DSNW130I -DB2A TRACE STARTED
TRACE(PERFM) CLASS(30) IFCID(0006,0007)
DSN9022I -DB2A DSNWVCM1 &#x27;START TRACE&#x27; NORMAL COMPLETION
DSNW130I と IFCID(0006,0007) が表示されていれば、イベント番号を絞ったトレース開始を示します。
――――
■ ステップ 3
現在の画面は DB2 COMMANDS パネルです。COMMAND INPUT ===&gt; に -DB2A START TRACE(ACCTG) CLASS(1,2,3) DEST(SMF) を入力します。この操作で トレース出力先を SMF に指定する操作 を確認します。
［操作（入力）］
(DB2 COMMANDS)
COMMAND INPUT ===&gt; -DB2A START TRACE(ACCTG) CLASS(1,2,3) DEST(SMF)
→ Enter を押す
［画面・出力］
DSNW130I -DB2A TRACE STARTED
TRACE(ACCTG) CLASS(1,2,3) DEST(SMF)
DSN9022I -DB2A DSNWVCM1 &#x27;START TRACE&#x27; NORMAL COMPLETION
DSNW130I、TRACE(ACCTG)、DEST(SMF) が同じ出力にあるため、出力先指定の証跡になります。
――――</pre><p>合格条件: ① ステップ1 の DSNW130I に TRACE(PERFM) と CLASS(1,2) が含まれること
② ステップ2 の DSNW130I に IFCID(0006,0007) が含まれること
③ ステップ3 の DSNW130I に DEST(SMF) が含まれること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Performance p.822 / Db2_zOS_Troubleshooting p.44</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE BUFFERPOOL（DDL句・属性） 確認手順</strong></p><p>検証目的: CREATE TABLESPACE の BUFFERPOOL、LOCKSIZE、LOCKMAX、DSSIZE、SEGSIZE を含む DDL 例を確認します。表スペースのメモリー、ロック、サイズ、セグメント設計を一つの定義で追えるようにします。</p><p>前提条件: TSO/ISPF にログオン済みです。SPUFI を起動でき、対象 Db2 サブシステム DBD1 に対する机上確認用の SQL 実行権限があります。実機では変更管理承認後に、検証用スキーマ APP1 で実行します。</p><p>セッション環境: TSO READY から SPUFI を開き、DDL を入力して実行します。</p><pre class="kb-code">■ ステップ 1
現在の画面は TSO READY です。COMMAND ===&gt; に =SPUFI を入力します。この操作で SQL を実行する SPUFI 画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象 Db2 へ SQL を入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面は SPUFI の SQL 入力画面です。SQL INPUT ===&gt; に CREATE TABLESPACE PAYTS IN PAYDB BUFFERPOOL BP0 LOCKSIZE ROW LOCKMAX SYSTEM DSSIZE 4G SEGSIZE 32; から始まる DDL を入力します。この操作で 表スペース物理属性確認 の指定例を机上確認します。
［操作（入力）］
SQL INPUT ===&gt; CREATE TABLESPACE PAYTS IN PAYDB BUFFERPOOL BP0 LOCKSIZE ROW LOCKMAX SYSTEM DSSIZE 4G SEGSIZE 32;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
DSNT400I SQLCODE = 0, SUCCESSFUL EXECUTION
OBJECT=PAYDB.PAYTS
BUFFERPOOL=BP0 LOCKSIZE=ROW LOCKMAX=SYSTEM DSSIZE=4G SEGSIZE=32
SQLCODE = 0
BUFFERPOOL=BP0 LOCKSIZE=ROW LOCKMAX=SYSTEM DSSIZE=4G SEGSIZE=32 が SPUFI OUTPUT に表示されていれば、表スペース物理属性確認 の確認対象が出力に含まれています。SQLCODE = 0 があれば、机上例では SQL が正常終了した形です。
――――
■ ステップ 3
現在の画面は SPUFI の結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えて TSO READY へ戻ります。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFI を閉じて TSO READY 状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の BUFFERPOOL=BP0 LOCKSIZE=ROW LOCKMAX=SYSTEM DSSIZE=4G SEGSIZE=32 が画面・出力に表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLESPACE NUMPARTS（DDL句・属性） 確認手順</strong></p><p>検証目的: CREATE TABLESPACE の NUMPARTS、MAXPARTITIONS、COMPRESS を含む DDL 例を確認します。区画数、成長上限、圧縮指定を分けて記録します。</p><p>前提条件: TSO/ISPF にログオン済みです。SPUFI を起動でき、対象 Db2 サブシステム DBD1 に対する机上確認用の SQL 実行権限があります。実機では変更管理承認後に、検証用スキーマ APP1 で実行します。</p><p>セッション環境: TSO READY から SPUFI を開き、DDL を入力して実行します。</p><pre class="kb-code">■ ステップ 1
現在の画面は TSO READY です。COMMAND ===&gt; に =SPUFI を入力します。この操作で SQL を実行する SPUFI 画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象 Db2 へ SQL を入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面は SPUFI の SQL 入力画面です。SQL INPUT ===&gt; に CREATE TABLESPACE HISTTS IN PAYDB NUMPARTS 4 MAXPARTITIONS 16 COMPRESS YES SEGSIZE 32; から始まる DDL を入力します。この操作で パーティション表スペース確認 の指定例を机上確認します。
［操作（入力）］
SQL INPUT ===&gt; CREATE TABLESPACE HISTTS IN PAYDB NUMPARTS 4 MAXPARTITIONS 16 COMPRESS YES SEGSIZE 32;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
DSNT400I SQLCODE = 0, SUCCESSFUL EXECUTION
OBJECT=PAYDB.HISTTS
NUMPARTS=4 MAXPARTITIONS=16 COMPRESS=YES SEGSIZE=32
SQLCODE = 0
NUMPARTS=4 MAXPARTITIONS=16 COMPRESS=YES が SPUFI OUTPUT に表示されていれば、パーティション表スペース確認 の確認対象が出力に含まれています。SQLCODE = 0 があれば、机上例では SQL が正常終了した形です。
――――
■ ステップ 3
現在の画面は SPUFI の結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えて TSO READY へ戻ります。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFI を閉じて TSO READY 状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の NUMPARTS=4 MAXPARTITIONS=16 COMPRESS=YES が画面・出力に表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE TABLE IN DATABASE（DDL句・属性） 確認手順</strong></p><p>検証目的: CREATE TABLE の IN DATABASE、IN TABLESPACE、PARTITION BY、DATA CAPTURE を含む DDL 例を確認します。表の所属先、分割方式、変更データ捕捉を同じ出力で追えるようにします。</p><p>前提条件: TSO/ISPF にログオン済みです。SPUFI を起動でき、対象 Db2 サブシステム DBD1 に対する机上確認用の SQL 実行権限があります。実機では変更管理承認後に、検証用スキーマ APP1 で実行します。</p><p>セッション環境: TSO READY から SPUFI を開き、DDL を入力して実行します。</p><pre class="kb-code">■ ステップ 1
現在の画面は TSO READY です。COMMAND ===&gt; に =SPUFI を入力します。この操作で SQL を実行する SPUFI 画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象 Db2 へ SQL を入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面は SPUFI の SQL 入力画面です。SQL INPUT ===&gt; に CREATE TABLE APP1.PAYROLL (EMPID INTEGER NOT NULL, DEPT CHAR(4), AMT DECIMAL(9,2)) IN PAYDB.PAYTS PARTITION BY SIZE EVERY 4G DATA CAPTURE CHANGES; から始まる DDL を入力します。この操作で 表配置と表属性確認 の指定例を机上確認します。
［操作（入力）］
SQL INPUT ===&gt; CREATE TABLE APP1.PAYROLL (EMPID INTEGER NOT NULL, DEPT CHAR(4), AMT DECIMAL(9,2)) IN PAYDB.PAYTS PARTITION BY SIZE EVERY 4G DATA CAPTURE CHANGES;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
DSNT400I SQLCODE = 0, SUCCESSFUL EXECUTION
TABLE=APP1.PAYROLL IN=PAYDB.PAYTS
PARTITION BY SIZE EVERY 4G DATA CAPTURE=CHANGES
SQLCODE = 0
TABLE=APP1.PAYROLL IN=PAYDB.PAYTS PARTITION BY SIZE EVERY 4G DATA CAPTURE=CHANGES が SPUFI OUTPUT に表示されていれば、表配置と表属性確認 の確認対象が出力に含まれています。SQLCODE = 0 があれば、机上例では SQL が正常終了した形です。
――――
■ ステップ 3
現在の画面は SPUFI の結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えて TSO READY へ戻ります。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFI を閉じて TSO READY 状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の TABLE=APP1.PAYROLL IN=PAYDB.PAYTS PARTITION BY SIZE EVERY 4G DATA CAPTURE=CHANGES が画面・出力に表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>CREATE INDEX UNIQUE（DDL句・属性） 確認手順</strong></p><p>検証目的: CREATE INDEX の UNIQUE、CLUSTER、PIECESIZE、BUFFERPOOL と CREATE STOGROUP の VOLUMES、VCAT、SMS クラスを確認します。索引物理設計とストレージ管理指定を分けて記録します。</p><p>前提条件: TSO/ISPF にログオン済みです。SPUFI を起動でき、対象 Db2 サブシステム DBD1 に対する机上確認用の SQL 実行権限があります。実機では変更管理承認後に、検証用スキーマ APP1 で実行します。</p><p>セッション環境: TSO READY から SPUFI を開き、DDL を入力して実行します。</p><pre class="kb-code">■ ステップ 1
現在の画面は TSO READY です。COMMAND ===&gt; に =SPUFI を入力します。この操作で SQL を実行する SPUFI 画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象 Db2 へ SQL を入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面は SPUFI の SQL 入力画面です。SQL INPUT ===&gt; に CREATE INDEX APP1.PAYIX ON APP1.PAYROLL(EMPID) UNIQUE CLUSTER PIECESIZE 2G BUFFERPOOL BP1; CREATE STOGROUP PAYSG VOLUMES(&#x27;*&#x27;) VCAT DB2CAT DATACLAS DBDATA STORCLAS DBFAST MGMTCLAS DBMGMT; から始まる DDL を入力します。この操作で 索引とストレージグループ確認 の指定例を机上確認します。
［操作（入力）］
SQL INPUT ===&gt; CREATE INDEX APP1.PAYIX ON APP1.PAYROLL(EMPID) UNIQUE CLUSTER PIECESIZE 2G BUFFERPOOL BP1; CREATE STOGROUP PAYSG VOLUMES(&#x27;*&#x27;) VCAT DB2CAT DATACLAS DBDATA STORCLAS DBFAST MGMTCLAS DBMGMT;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
DSNT400I SQLCODE = 0, SUCCESSFUL EXECUTION
INDEX=APP1.PAYIX UNIQUE=YES CLUSTER=YES PIECESIZE=2G BUFFERPOOL=BP1
STOGROUP=PAYSG VOLUMES=* VCAT=DB2CAT DATACLAS=DBDATA STORCLAS=DBFAST MGMTCLAS=DBMGMT
SQLCODE = 0
UNIQUE=YES CLUSTER=YES PIECESIZE=2G BUFFERPOOL=BP1 STOGROUP=PAYSG が SPUFI OUTPUT に表示されていれば、索引とストレージグループ確認 の確認対象が出力に含まれています。SQLCODE = 0 があれば、机上例では SQL が正常終了した形です。
――――
■ ステップ 3
現在の画面は SPUFI の結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えて TSO READY へ戻ります。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFI を閉じて TSO READY 状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の UNIQUE=YES CLUSTER=YES PIECESIZE=2G BUFFERPOOL=BP1 STOGROUP=PAYSG が画面・出力に表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div><div class="kb-p"><p class="kb-pname"><strong>GRANT privilege（DDL句・属性） 確認手順</strong></p><p>検証目的: GRANT、REVOKE、CREATE TRUSTED CONTEXT、CREATE TRIGGER の DDL 例を確認します。権限変更、信頼接続、トリガーの発火条件を同じ手順で混同しないようにします。</p><p>前提条件: TSO/ISPF にログオン済みです。SPUFI を起動でき、対象 Db2 サブシステム DBD1 に対する机上確認用の SQL 実行権限があります。実機では変更管理承認後に、検証用スキーマ APP1 で実行します。</p><p>セッション環境: TSO READY から SPUFI を開き、DDL を入力して実行します。</p><pre class="kb-code">■ ステップ 1
現在の画面は TSO READY です。COMMAND ===&gt; に =SPUFI を入力します。この操作で SQL を実行する SPUFI 画面へ移動します。
［操作（入力）］
READY
COMMAND ===&gt; =SPUFI
→ Enter を押す
［画面・出力］
SPUFI
DB2 SSID ===&gt; DBD1
SQL INPUT ===&gt;
SPUFI と DBD1 が表示されていれば、対象 Db2 へ SQL を入力できる画面へ到達しています。
――――
■ ステップ 2
現在の画面は SPUFI の SQL 入力画面です。SQL INPUT ===&gt; に GRANT SELECT ON TABLE APP1.PAYROLL TO ROLE PAYREAD; REVOKE SELECT ON TABLE APP1.PAYROLL FROM ROLE OLDREAD; CREATE TRUSTED CONTEXT PAYCTX BASED UPON CONNECTION USING SYSTEM AUTHID APPUSR ENABLE; CREATE TRIGGER APP1.PAYTRG AFTER INSERT ON APP1.PAYROLL FOR EACH ROW MODE DB2SQL VALUES 1; から始まる DDL を入力します。この操作で 権限とセキュリティDDL確認 の指定例を机上確認します。
［操作（入力）］
SQL INPUT ===&gt; GRANT SELECT ON TABLE APP1.PAYROLL TO ROLE PAYREAD; REVOKE SELECT ON TABLE APP1.PAYROLL FROM ROLE OLDREAD; CREATE TRUSTED CONTEXT PAYCTX BASED UPON CONNECTION USING SYSTEM AUTHID APPUSR ENABLE; CREATE TRIGGER APP1.PAYTRG AFTER INSERT ON APP1.PAYROLL FOR EACH ROW MODE DB2SQL VALUES 1;
→ Enter を押す
［画面・出力］
SPUFI OUTPUT
DSNT400I SQLCODE = 0, SUCCESSFUL EXECUTION
GRANT SELECT TO ROLE PAYREAD
REVOKE SELECT FROM ROLE OLDREAD
TRUSTED CONTEXT=PAYCTX STATUS=ENABLED
TRIGGER=APP1.PAYTRG TIMING=AFTER EVENT=INSERT
SQLCODE = 0
GRANT SELECT REVOKE SELECT TRUSTED CONTEXT=PAYCTX TRIGGER=APP1.PAYTRG が SPUFI OUTPUT に表示されていれば、権限とセキュリティDDL確認 の確認対象が出力に含まれています。SQLCODE = 0 があれば、机上例では SQL が正常終了した形です。
――――
■ ステップ 3
現在の画面は SPUFI の結果表示画面です。COMMAND ===&gt; に END を入力し、確認作業を終えて TSO READY へ戻ります。
［操作（入力）］
COMMAND ===&gt; END
→ Enter を押す
［画面・出力］
READY
READY が表示されていれば、SPUFI を閉じて TSO READY 状態へ戻っています。
――――</pre><p>合格条件: ① ステップ1 の SPUFI と DBD1 が表示されること
② ステップ2 の GRANT SELECT REVOKE SELECT TRUSTED CONTEXT=PAYCTX TRIGGER=APP1.PAYTRG が画面・出力に表示されること
③ ステップ3 の READY が表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation</p></div></details></section>
