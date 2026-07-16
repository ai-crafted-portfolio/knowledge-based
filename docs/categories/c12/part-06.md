---
search:
  exclude: true
---

# IBM MQ メッセージング — 詳細 (6/8)

[← IBM MQ メッセージング の概要へ戻る](index.md)


## IBM MQ メッセージング > 監視 / メトリクス

### System topics for monitoring and activity trace {#c12-i0735}
*分類: 監視 / メトリクス*  ・  難易度: 上級

System topics for monitoring and activity traceは、IBM MQ メッセージングの監視 / メトリクスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 出力判定の監視 メトリクスに関する System topics for monitoの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY TOPIC(*) ALL の結果を残さず出力判定の監視 メトリクスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の監視 メトリクスの証跡として保存して根拠にする。
    - C. System topics for monitoの変更点を出力本文から切り離して出力判定の監視 メトリクスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力判定の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では System topics for monito は「System topics for monitoの状態と出力メッセージを結び付ける出力判定項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では System topics for monitoの出力行と CSQ9022I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では System topics for monitoを IBM MQ for z/OS の確認記録に残し、対象名は出力判定対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Tuning client and server connection channels {#c12-i0736}
*分類: 監視 / メトリクス*  ・  難易度: 上級

Tuning client and server connection channelsは、IBM MQ メッセージングの監視 / メトリクスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 条件判定の監視 メトリクスに関係する Tuning client and serverの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、条件判定の点検結果を残す。 ✅
    - B. Tuning client and serverの名称と担当者名のみを残して条件判定の監視 メトリクスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件判定の監視 メトリクスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件判定の監視 メトリクスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Tuning client and server は「Tuning client and serverの用途をメッセージングの表示で確認する条件判定項目」と DISPLAY CHANNEL(*) ALL または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM MQ for z/OS の Tuning client and serverと CSQ9022I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Tuning client and serverを IBM MQ メッセージングで扱う確認対象とし、用語名は条件判定用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Tuning distributed publish/subscribe networks {#c12-i0737}
*分類: 監視 / メトリクス*  ・  難易度: 上級

「Tuning distributed publish/subscribe networks」 (監視 / メトリクス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.monitor.pdf p.377))

**出典:** MQ 9.3 監視・パフォーマンス [mq93.monitor.pdf p.377]

??? question "確認問題（1問）"
    **問題.** 区切判定の監視 メトリクスで Tuning distributed publiの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Tuning distributed publiの出力を取らず区切判定の監視 メトリクスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切判定で再確認できる形にする。 ✅
    - C. DISPLAY TOPIC(*) ALL を省略して区切判定の監視 メトリクスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の監視 メトリクスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Tuning distributed publi は「区切判定の監視 メトリクスに関係する定義値と表示行を照合する区切判定項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Tuning distributed publiの属性行と CSQ9022I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Tuning distributed publiを IBM MQ メッセージングの運用手順で確認し、初出名は区切判定初出です。

    **出典:** MQ 9.3 監視・パフォーマンス [mq93.monitor.pdf p.377]



### Tuning your IBM MQ network {#c12-i0738}
*分類: 監視 / メトリクス*  ・  難易度: 上級

「Tuning your IBM MQ network」 (監視 / メトリクス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.monitor.pdf p.376))

**出典:** MQ 9.3 監視・パフォーマンス [mq93.monitor.pdf p.376]

??? question "確認問題（1問）"
    **問題.** 範囲判定の監視 メトリクスでメッセージングの運用確認を行います。Tuning your IBM MQ netwoの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲判定の監視 メトリクスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲判定の監視 メトリクスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲判定の確認値として扱う。 ✅
    - D. Tuning your IBM MQ netwoの属性行を読まず範囲判定の監視 メトリクスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では Tuning your IBM MQ netwo は「IBM MQ for z/OS で Tuning your IBM MQ netwoの扱いを記録する範囲判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では Tuning your IBM MQ netwoの表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では Tuning your IBM MQ netwoの使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** MQ 9.3 監視・パフォーマンス [mq93.monitor.pdf p.376]




## IBM MQ メッセージング > 管理リファレンス

### Administration reference {#c12-i0739}
*分類: 管理リファレンス*  ・  難易度: 上級

Administration referenceは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5]

??? question "確認問題（1問）"
    **問題.** 優先判定の管理リファレンスに関する Administration referenceの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の管理リファレンスの証跡として保存して根拠にする。
    - C. Administration referenceの変更点を出力本文から切り離して優先判定の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では Administration reference は「Administration referenceの状態と出力メッセージを結び付ける優先判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では Administration referenceの出力行と CSQ9022I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では Administration referenceを IBM MQ for z/OS の確認記録に残し、対象名は優先判定対象です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5]



### Administrative REST API reference {#c12-i0740}
*分類: 管理リファレンス*  ・  難易度: 上級

Administrative REST API referenceは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2171] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2171]

??? question "確認問題（1問）"
    **問題.** 記録判定の管理リファレンスに関係する Administrative REST API の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を記録判定で確認する。 ✅
    - B. Administrative REST API の名称と担当者名のみを残して記録判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では Administrative REST API は「Administrative REST API の用途をメッセージングの表示で確認する記録判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM MQ for z/OS の Administrative REST API と CSQ9022I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では Administrative REST API を IBM MQ メッセージングで扱う確認対象とし、用語名は記録判定用語です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2171]



### Authorities for the MFT logger {#c12-i0741}
*分類: 管理リファレンス*  ・  難易度: 上級

Authorities for the MFT loggerは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 比較判定の管理リファレンスで Authorities for the MFT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Authorities for the MFT の出力を取らず比較判定の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、比較判定の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して比較判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Authorities for the MFT は「比較判定の管理リファレンスに関係する定義値と表示行を照合する比較判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Authorities for the MFT の属性行と CSQ9022I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Authorities for the MFT を IBM MQ メッセージングの運用手順で確認し、初出名は比較判定初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Available code pages for MFT {#c12-i0742}
*分類: 管理リファレンス*  ・  難易度: 上級

Available code pages for MFTは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 順序判定の管理リファレンスでメッセージングの運用確認を行います。Available code pages forの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序判定の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序判定の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序判定の確認記録にまとめる。 ✅
    - D. Available code pages forの属性行を読まず順序判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では Available code pages for は「IBM MQ for z/OS で Available code pages forの扱いを記録する順序判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では Available code pages forの表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では Available code pages forの使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### CL commands for IBM i reference {#c12-i0743}
*分類: 管理リファレンス*  ・  難易度: 上級

CL commands for IBM i referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 値域判定の管理リファレンスに関する CL commands for IBM i reの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の管理リファレンスの証跡として保存して根拠にする。
    - C. CL commands for IBM i reの変更点を出力本文から切り離して値域判定の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域判定の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では CL commands for IBM i re は「CL commands for IBM i reの状態と出力メッセージを結び付ける値域判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では CL commands for IBM i reの出力行と CSQ9022I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では CL commands for IBM i reを IBM MQ for z/OS の確認記録に残し、対象名は値域判定対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Command sets comparison {#c12-i0744}
*分類: 管理リファレンス*  ・  難易度: 上級

Command sets comparisonは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5]

??? question "確認問題（1問）"
    **問題.** 警告判定の管理リファレンスに関係する Command sets comparisonの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、警告判定の結果として保存する。 ✅
    - B. Command sets comparisonの名称と担当者名のみを残して警告判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では Command sets comparison は「Command sets comparisonの用途をメッセージングの表示で確認する警告判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM MQ for z/OS の Command sets comparisonと CSQ9022I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では Command sets comparisonを IBM MQ メッセージングで扱う確認対象とし、用語名は警告判定用語です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5]



### Commands reference {#c12-i0745}
*分類: 管理リファレンス*  ・  難易度: 上級

Commands referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5]

??? question "確認問題（1問）"
    **問題.** 復旧判定の管理リファレンスで Commands referenceの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Commands referenceの出力を取らず復旧判定の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、復旧判定の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では Commands reference は「復旧判定の管理リファレンスに関係する定義値と表示行を照合する復旧判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では Commands referenceの属性行と CSQ9022I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では Commands referenceを IBM MQ メッセージングの運用手順で確認し、初出名は復旧判定初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.5]



### Display queue manager information utility (CSQUDSPM) {#c12-i0746}
*分類: 管理リファレンス*  ・  難易度: 上級

Display queue manager information utility (CSQUDSPM)は、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2821] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2821]

??? question "確認問題（1問）"
    **問題.** 監査判定の管理リファレンスでメッセージングの運用確認を行います。Display queue manager inの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査判定の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査判定の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査判定として引き継ぐ。 ✅
    - D. Display queue manager inの属性行を読まず監査判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Display queue manager in は「IBM MQ for z/OS で Display queue manager inの扱いを記録する監査判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Display queue manager inの表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Display queue manager inの使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2821]



### Example: A Connect:Direct process file that calls MFT commands {#c12-i0747}
*分類: 管理リファレンス*  ・  難易度: 上級

Example: A Connect:Direct process file that calls MFT commandsは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 変更判定の: :に関する Example: A Connect:Direcの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更判定の: :の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定の: :の証跡として保存して根拠にする。
    - C. Example: A Connect:Direcの変更点を出力本文から切り離して変更判定の: :の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更判定の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Example: A Connect:Direc は「Example: A Connect:Direcの状態と出力メッセージを結び付ける変更判定項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Example: A Connect:Direcの出力行と CSQ9022I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Example: A Connect:Direcを IBM MQ for z/OS の確認記録に残し、対象名は変更判定対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### FIPS support in MFT {#c12-i0748}
*分類: 管理リファレンス*  ・  難易度: 上級

「FIPS support in MFT」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2541))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2541]

??? question "確認問題（1問）"
    **問題.** 展開整理の管理リファレンスで FIPS support in MFT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FIPS support in MFT の出力を取らず展開整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開整理で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して展開整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では FIPS support in MFT は「展開整理の管理リファレンスに関係する定義値と表示行を照合する展開整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では FIPS support in MFT の属性行と CSQ9022I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では FIPS support in MFT を IBM MQ メッセージングの運用手順で確認し、初出名は展開整理初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2541]



### FTPS server support by the protocol bridge {#c12-i0749}
*分類: 管理リファレンス*  ・  難易度: 上級

FTPS server support by the protocol bridgeは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 呼出整理の管理リファレンスでメッセージングの運用確認を行います。FTPS server support by tの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出整理の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出整理の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出整理の確認値として扱う。 ✅
    - D. FTPS server support by tの属性行を読まず呼出整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では FTPS server support by t は「IBM MQ for z/OS で FTPS server support by tの扱いを記録する呼出整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では FTPS server support by tの表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では FTPS server support by tの使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### File permissions for destination files {#c12-i0750}
*分類: 管理リファレンス*  ・  難易度: 上級

File permissions for destination filesは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 構文整理の管理リファレンスに関係する File permissions for desの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、構文整理の点検結果を残す。 ✅
    - B. File permissions for desの名称と担当者名のみを残して構文整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では File permissions for des は「File permissions for desの用途をメッセージングの表示で確認する構文整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM MQ for z/OS の File permissions for desと CSQ9022I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では File permissions for desを IBM MQ メッセージングで扱う確認対象とし、用語名は構文整理用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Guidance for setting MQ attributes and MFT properties associated with message size {#c12-i0751}
*分類: 管理リファレンス*  ・  難易度: 上級

Guidance for setting MQ attributes and MFT properties associated with message sizeは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference


### Guidance for specifying a wait time on a message-to-file transfer {#c12-i0752}
*分類: 管理リファレンス*  ・  難易度: 上級

Guidance for specifying a wait time on a message-to-file transferは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 終端整理の管理リファレンスに関係する Guidance for specifyingの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を終端整理で確認する。 ✅
    - B. Guidance for specifyingの名称と担当者名のみを残して終端整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では Guidance for specifying は「Guidance for specifyingの用途をメッセージングの表示で確認する終端整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM MQ for z/OS の Guidance for specifyingと CSQ9022I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では Guidance for specifyingを IBM MQ メッセージングで扱う確認対象とし、用語名は終端整理用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Guidelines for transferring files {#c12-i0753}
*分類: 管理リファレンス*  ・  難易度: 上級

「Guidelines for transferring files」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2502))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2502]

??? question "確認問題（1問）"
    **問題.** 探索整理の管理リファレンスで Guidelines for transferrの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Guidelines for transferrの出力を取らず探索整理の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、探索整理の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Guidelines for transferr は「探索整理の管理リファレンスに関係する定義値と表示行を照合する探索整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Guidelines for transferrの属性行と CSQ9022I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Guidelines for transferrを IBM MQ メッセージングの運用手順で確認し、初出名は探索整理初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2502]



### How MFT agents allocate source transfer slots to new requests {#c12-i0754}
*分類: 管理リファレンス*  ・  難易度: 上級

How MFT agents allocate source transfer slots to new requestsは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 上書整理の管理リファレンスでメッセージングの運用確認を行います。How MFT agents allocateの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書整理の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書整理の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書整理の確認記録にまとめる。 ✅
    - D. How MFT agents allocateの属性行を読まず上書整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では How MFT agents allocate は「IBM MQ for z/OS で How MFT agents allocateの扱いを記録する上書整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では How MFT agents allocateの表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では How MFT agents allocateの使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### How MFT agents use Java heap and native heap memory {#c12-i0755}
*分類: 管理リファレンス*  ・  難易度: 上級

How MFT agents use Java heap and native heap memoryは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 出力整理の管理リファレンスに関する How MFT agents use Javaの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず出力整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理の管理リファレンスの証跡として保存して根拠にする。
    - C. How MFT agents use Javaの変更点を出力本文から切り離して出力整理の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では How MFT agents use Java は「How MFT agents use Javaの状態と出力メッセージを結び付ける出力整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では How MFT agents use Javaの出力行と CSQ9022I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では How MFT agents use Javaを IBM MQ for z/OS の確認記録に残し、対象名は出力整理対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### How to read syntax diagrams {#c12-i0756}
*分類: 管理リファレンス*  ・  難易度: 上級

How to read syntax diagramsは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 条件整理の管理リファレンスに関係する How to read syntax diagrの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、条件整理の結果として保存する。 ✅
    - B. How to read syntax diagrの名称と担当者名のみを残して条件整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では How to read syntax diagr は「How to read syntax diagrの用途をメッセージングの表示で確認する条件整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM MQ for z/OS の How to read syntax diagrと CSQ9022I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では How to read syntax diagrを IBM MQ メッセージングで扱う確認対象とし、用語名は条件整理用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ Administration Interface reference {#c12-i0757}
*分類: 管理リファレンス*  ・  難易度: 上級

IBM MQ Administration Interface referenceは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2415] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2415]

??? question "確認問題（1問）"
    **問題.** 区切整理の管理リファレンスで IBM MQ Administration Inの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IBM MQ Administration Inの出力を取らず区切整理の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、区切整理の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して区切整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では IBM MQ Administration In は「区切整理の管理リファレンスに関係する定義値と表示行を照合する区切整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では IBM MQ Administration Inの属性行と CSQ9022I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では IBM MQ Administration Inを IBM MQ メッセージングの運用手順で確認し、初出名は区切整理初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2415]



### IBM MQ control commands reference {#c12-i0758}
*分類: 管理リファレンス*  ・  難易度: 上級

IBM MQ control commands referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.21] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.21]

??? question "確認問題（1問）"
    **問題.** 範囲整理の管理リファレンスでメッセージングの運用確認を行います。IBM MQ control commandsの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲整理の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲整理の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲整理として引き継ぐ。 ✅
    - D. IBM MQ control commandsの属性行を読まず範囲整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では IBM MQ control commands は「IBM MQ for z/OS で IBM MQ control commandsの扱いを記録する範囲整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では IBM MQ control commandsの表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では IBM MQ control commandsの使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.21]



### IBM MQ message properties read by MFT from messages on source queues {#c12-i0759}
*分類: 管理リファレンス*  ・  難易度: 上級

IBM MQ message properties read by MFT from messages on source queuesは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 優先整理の管理リファレンスに関する IBM MQ message propertieの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理の管理リファレンスの証跡として保存して根拠にする。
    - C. IBM MQ message propertieの変更点を出力本文から切り離して優先整理の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先整理の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では IBM MQ message propertie は「IBM MQ message propertieの状態と出力メッセージを結び付ける優先整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では IBM MQ message propertieの出力行と CSQ9022I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では IBM MQ message propertieを IBM MQ for z/OS の確認記録に残し、対象名は優先整理対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ utilities on z/OS by category {#c12-i0760}
*分類: 管理リファレンス*  ・  難易度: 上級

IBM MQ utilities on z/OS by categoryは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 技術項目「IBM MQ utilities on z/OS by category」の確認として、属性照合通知の属性照合として IBM を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 属性照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 名称と担当者名を保存して表示本文を確認しない。
    - D. 別分類の結果を流用して同じ証跡として扱う。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解はAです。属性照合通知で扱う IBM は IBM MQ メッセージング の確認対象です（属性照合通知用語）。属性照合通知の担当者は属性照合として、表示本文とメッセージを照合します（属性照合通知照合）。属性照合通知の対応を残すと、後続担当者は同じ出典に戻って確認できます（属性照合通知出典）。A: 属性照合通知で表示とメッセージを結ぶ場合に根拠になります（属性照合通知A）。B: 属性照合通知で定義と出力の関係がない場合は追跡できません（属性照合通知B）。C: 属性照合通知で出典名のみでは実際の表示を説明できません（属性照合通知C）。D: 属性照合通知で操作記録のみでは値や状態の確認が不足します（属性照合通知D）。属性照合通知の初出用語として IBM を扱い、分類内の確認名として保存します（属性照合通知終点）。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ utilities on z/OS reference {#c12-i0761}
*分類: 管理リファレンス*  ・  難易度: 上級

IBM MQ utilities on z/OS referenceは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 比較整理のIBM MQ utilities on z/OS referenceで IBM MQ utilities on z 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IBM MQ utilities on z 属性の出力を取らず比較整理のIBM MQ utilities on z/OS referenceの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較整理で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して比較整理のIBM MQ utilities on z/OS referenceの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理のIBM MQ utilities on z/OS referenceへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では IBM MQ utilities on z 属性 は「比較整理のIBM MQ utilities on z/OS referenceに関係する定義値と表示行を照合する比較整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では IBM MQ utilities on z 属性の属性行と CSQ9022I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では IBM MQ utilities on z 属性を IBM MQ メッセージングの運用手順で確認し、初出名は比較整理初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ utility program (CSQUTIL) on z/OS {#c12-i0762}
*分類: 管理リファレンス*  ・  難易度: 上級

IBM MQ utility program (CSQUTIL) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 順序整理の管理リファレンスでメッセージングの運用確認を行います。IBM MQ utility program 属性の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序整理の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序整理の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序整理の確認値として扱う。 ✅
    - D. IBM MQ utility program 属性の属性行を読まず順序整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では IBM MQ utility program 属性 は「IBM MQ for z/OS で IBM MQ utility program 属性の扱いを記録する順序整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では IBM MQ utility program 属性の表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では IBM MQ utility program 属性の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### MFT agent process controller status values {#c12-i0763}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT agent process controller status values」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2499))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2499]

??? question "確認問題（1問）"
    **問題.** 警告整理の管理リファレンスに関係する MFT agent process controの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を警告整理で確認する。 ✅
    - B. MFT agent process controの名称と担当者名のみを残して警告整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では MFT agent process contro は「MFT agent process controの用途をメッセージングの表示で確認する警告整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM MQ for z/OS の MFT agent process controと CSQ9022I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では MFT agent process controを IBM MQ メッセージングで扱う確認対象とし、用語名は警告整理用語です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2499]



### MFT agent status values {#c12-i0764}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT agent status values」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2496))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2496]

??? question "確認問題（1問）"
    **問題.** 復旧整理の管理リファレンスで MFT agent status valuesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MFT agent status valuesの出力を取らず復旧整理の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、復旧整理の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では MFT agent status values は「復旧整理の管理リファレンスに関係する定義値と表示行を照合する復旧整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では MFT agent status valuesの属性行と CSQ9022I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では MFT agent status valuesを IBM MQ メッセージングの運用手順で確認し、初出名は復旧整理初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2496]



### MFT commands reference {#c12-i0765}
*分類: 管理リファレンス*  ・  難易度: 上級

MFT commands referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.1989] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.1989]

??? question "確認問題（1問）"
    **問題.** 監査整理の管理リファレンスでメッセージングの運用確認を行います。MFT commands referenceの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査整理の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査整理の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査整理の確認記録にまとめる。 ✅
    - D. MFT commands referenceの属性行を読まず監査整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では MFT commands reference は「IBM MQ for z/OS で MFT commands referenceの扱いを記録する監査整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では MFT commands referenceの表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では MFT commands referenceの使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.1989]



### MFT database logger tables {#c12-i0766}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT database logger tables」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2542))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2542]

??? question "確認問題（1問）"
    **問題.** 変更整理の管理リファレンスに関する MFT database logger tablの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理の管理リファレンスの証跡として保存して根拠にする。
    - C. MFT database logger tablの変更点を出力本文から切り離して変更整理の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では MFT database logger tabl は「MFT database logger tablの状態と出力メッセージを結び付ける変更整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では MFT database logger tablの出力行と CSQ9022I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では MFT database logger tablを IBM MQ for z/OS の確認記録に残し、対象名は変更整理対象です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2542]



### MFT logger process controller status values {#c12-i0767}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT logger process controller status values」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2500))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2500]

??? question "確認問題（1問）"
    **問題.** 構文記録の管理リファレンスに関係する MFT logger process contrの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、構文記録の結果として保存する。 ✅
    - B. MFT logger process contrの名称と担当者名のみを残して構文記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では MFT logger process contr は「MFT logger process contrの用途をメッセージングの表示で確認する構文記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM MQ for z/OS の MFT logger process contrと CSQ9022I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では MFT logger process contrを IBM MQ メッセージングで扱う確認対象とし、用語名は構文記録用語です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2500]



### MFT logger status values {#c12-i0768}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT logger status values」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2500))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2500]

??? question "確認問題（1問）"
    **問題.** 展開記録の管理リファレンスで MFT logger status valuesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MFT logger status valuesの出力を取らず展開記録の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、展開記録の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して展開記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では MFT logger status values は「展開記録の管理リファレンスに関係する定義値と表示行を照合する展開記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では MFT logger status valuesの属性行と CSQ9022I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では MFT logger status valuesを IBM MQ メッセージングの運用手順で確認し、初出名は展開記録初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2500]



### MFT process controller exit codes {#c12-i0769}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT process controller exit codes」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2501))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2501]

??? question "確認問題（1問）"
    **問題.** 呼出記録の管理リファレンスでメッセージングの運用確認を行います。MFT process controller eの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出記録の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出記録の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出記録として引き継ぐ。 ✅
    - D. MFT process controller eの属性行を読まず呼出記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では MFT process controller e は「IBM MQ for z/OS で MFT process controller eの扱いを記録する呼出記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では MFT process controller eの表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では MFT process controller eの使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2501]



### MFT process controller overview {#c12-i0770}
*分類: 管理リファレンス*  ・  難易度: 上級

「MFT process controller overview」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2497))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2497]

??? question "確認問題（1問）"
    **問題.** 置換記録の管理リファレンスに関する MFT process controller oの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず置換記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録の管理リファレンスの証跡として保存して根拠にする。
    - C. MFT process controller oの変更点を出力本文から切り離して置換記録の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換記録の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では MFT process controller o は「MFT process controller oの状態と出力メッセージを結び付ける置換記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では MFT process controller oの出力行と CSQ9022I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では MFT process controller oを IBM MQ for z/OS の確認記録に残し、対象名は置換記録対象です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2497]



### MQ message properties set by MFT on messages written to destination queues {#c12-i0771}
*分類: 管理リファレンス*  ・  難易度: 上級

MQ message properties set by MFT on messages written to destination queuesは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 終端記録の管理リファレンスに関係する MQ message properties seの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、終端記録の点検結果を残す。 ✅
    - B. MQ message properties seの名称と担当者名のみを残して終端記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では MQ message properties se は「MQ message properties seの用途をメッセージングの表示で確認する終端記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM MQ for z/OS の MQ message properties seと CSQ9022I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では MQ message properties seを IBM MQ メッセージングで扱う確認対象とし、用語名は終端記録用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### MQAI calls {#c12-i0772}
*分類: 管理リファレンス*  ・  難易度: 上級

「MQAI calls」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2415))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2415]

??? question "確認問題（1問）"
    **問題.** 探索記録の管理リファレンスで MQAI callsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MQAI callsの出力を取らず探索記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索記録で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では MQAI calls は「探索記録の管理リファレンスに関係する定義値と表示行を照合する探索記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では MQAI callsの属性行と CSQ9022I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では MQAI callsを IBM MQ メッセージングの運用手順で確認し、初出名は探索記録初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2415]



### MQAI selectors {#c12-i0773}
*分類: 管理リファレンス*  ・  難易度: 上級

「MQAI selectors」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2494))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2494]

??? question "確認問題（1問）"
    **問題.** 上書記録の管理リファレンスでメッセージングの運用確認を行います。MQAI selectorsの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書記録の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書記録の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書記録の確認値として扱う。 ✅
    - D. MQAI selectorsの属性行を読まず上書記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では MQAI selectors は「IBM MQ for z/OS で MQAI selectorsの扱いを記録する上書記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では MQAI selectorsの表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では MQAI selectorsの使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2494]



### MQIPT commands reference {#c12-i0774}
*分類: 管理リファレンス*  ・  難易度: 上級

MQIPT commands referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2165] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2165]

??? question "確認問題（1問）"
    **問題.** 出力記録の管理リファレンスに関する MQIPT commands referenceの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず出力記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録の管理リファレンスの証跡として保存して根拠にする。
    - C. MQIPT commands referenceの変更点を出力本文から切り離して出力記録の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では MQIPT commands reference は「MQIPT commands referenceの状態と出力メッセージを結び付ける出力記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では MQIPT commands referenceの出力行と CSQ9022I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では MQIPT commands referenceを IBM MQ for z/OS の確認記録に残し、対象名は出力記録対象です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2165]



### MQSC commands reference {#c12-i0775}
*分類: 管理リファレンス*  ・  難易度: 上級

MQSC commands referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.249] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.249]

??? question "確認問題（1問）"
    **問題.** 条件記録の管理リファレンスに関係する MQSC commands referenceの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を条件記録で確認する。 ✅
    - B. MQSC commands referenceの名称と担当者名のみを残して条件記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では MQSC commands reference は「MQSC commands referenceの用途をメッセージングの表示で確認する条件記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM MQ for z/OS の MQSC commands referenceと CSQ9022I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では MQSC commands referenceを IBM MQ メッセージングで扱う確認対象とし、用語名は条件記録用語です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.249]



### Managed File Transfer administration reference {#c12-i0776}
*分類: 管理リファレンス*  ・  難易度: 上級

Managed File Transfer administration referenceは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2496] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2496]

??? question "確認問題（1問）"
    **問題.** 値域整理の管理リファレンスに関する Managed File Transfer adの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理の管理リファレンスの証跡として保存して根拠にする。
    - C. Managed File Transfer adの変更点を出力本文から切り離して値域整理の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域整理の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Managed File Transfer ad は「Managed File Transfer adの状態と出力メッセージを結び付ける値域整理項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Managed File Transfer adの出力行と CSQ9022I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Managed File Transfer adを IBM MQ for z/OS の確認記録に残し、対象名は値域整理対象です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2496]



### Programmable command formats (PCFs) reference {#c12-i0777}
*分類: 管理リファレンス*  ・  難易度: 上級

Programmable command formats (PCFs) referenceは、IBM MQ メッセージングの管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.986] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.986]

??? question "確認問題（1問）"
    **問題.** 区切記録の管理リファレンスで Programmable command forの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Programmable command forの出力を取らず区切記録の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、区切記録の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して区切記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Programmable command for は「区切記録の管理リファレンスに関係する定義値と表示行を照合する区切記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Programmable command forの属性行と CSQ9022I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Programmable command forを IBM MQ メッセージングの運用手順で確認し、初出名は区切記録初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.986]



### Programming interface information {#c12-i0778}
*分類: 管理リファレンス*  ・  難易度: 上級

「Programming interface information」 (管理リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refadmin.pdf p.2828))

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2828]


### REST API and PCF equivalents {#c12-i0779}
*分類: 管理リファレンス*  ・  難易度: 上級

REST API and PCF equivalentsは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 記録記録の管理リファレンスに関係する REST API and PCF equivalの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、記録記録の結果として保存する。 ✅
    - B. REST API and PCF equivalの名称と担当者名のみを残して記録記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では REST API and PCF equival は「REST API and PCF equivalの用途をメッセージングの表示で確認する記録記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM MQ for z/OS の REST API and PCF equivalと CSQ9022I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では REST API and PCF equivalを IBM MQ メッセージングで扱う確認対象とし、用語名は記録記録用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### REST API resources {#c12-i0780}
*分類: 管理リファレンス*  ・  難易度: 上級

REST API resourcesは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2171] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2171]

??? question "確認問題（2問）"
    **問題.** 比較記録の管理リファレンスで REST API resourcesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. REST API resourcesの出力を取らず比較記録の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、比較記録の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して比較記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では REST API resources は「比較記録の管理リファレンスに関係する定義値と表示行を照合する比較記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では REST API resourcesの属性行と CSQ9022I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では REST API resourcesを IBM MQ メッセージングの運用手順で確認し、初出名は比較記録初出です。

    **出典:** MQ 9.3 管理リファレンス [mq93.refadmin.pdf p.2171]

    ---

    **問題.** 優先記録の開発リファレンスに関する REST API resourcesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先記録の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の開発リファレンスの証跡として保存して根拠にする。
    - C. REST API resourcesの変更点を出力本文から切り離して優先記録の開発リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と CSQ9022I を読み、優先記録の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では REST API resources は「REST API resourcesの状態と出力メッセージを結び付ける優先記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では REST API resourcesの出力行と CSQ9022I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では REST API resourcesを IBM MQ for z/OS の確認記録に残し、対象名は優先記録対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.2141]



### Regular expressions used by MFT {#c12-i0781}
*分類: 管理リファレンス*  ・  難易度: 上級

Regular expressions used by MFTは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 優先記録の管理リファレンスに関する Regular expressions usedの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の管理リファレンスの証跡として保存して根拠にする。
    - C. Regular expressions usedの変更点を出力本文から切り離して優先記録の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先記録の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Regular expressions used は「Regular expressions usedの状態と出力メッセージを結び付ける優先記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Regular expressions usedの出力行と CSQ9022I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Regular expressions usedを IBM MQ for z/OS の確認記録に残し、対象名は優先記録対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Restrictions of the Connect:Direct bridge agent {#c12-i0782}
*分類: 管理リファレンス*  ・  難易度: 上級

Restrictions of the Connect:Direct bridge agentは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 順序記録の管理リファレンスでメッセージングの運用確認を行います。Restrictions of the Connの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序記録の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序記録の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序記録として引き継ぐ。 ✅
    - D. Restrictions of the Connの属性行を読まず順序記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Restrictions of the Conn は「IBM MQ for z/OS で Restrictions of the Connの扱いを記録する順序記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Restrictions of the Connの表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Restrictions of the Connの使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### SFTP server support by the protocol bridge {#c12-i0783}
*分類: 管理リファレンス*  ・  難易度: 上級

SFTP server support by the protocol bridgeは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 値域記録の管理リファレンスに関する SFTP server support by tの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録の管理リファレンスの証跡として保存して根拠にする。
    - C. SFTP server support by tの変更点を出力本文から切り離して値域記録の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域記録の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では SFTP server support by t は「SFTP server support by tの状態と出力メッセージを結び付ける値域記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では SFTP server support by tの出力行と CSQ9022I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では SFTP server support by tを IBM MQ for z/OS の確認記録に残し、対象名は値域記録対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Substitution variables for use with user-defined Connect:Direct processes {#c12-i0784}
*分類: 管理リファレンス*  ・  難易度: 上級

Substitution variables for use with user-defined Connect:Direct processesは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 警告記録の管理リファレンスに関係する Substitution variables fの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、警告記録の点検結果を残す。 ✅
    - B. Substitution variables fの名称と担当者名のみを残して警告記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Substitution variables f は「Substitution variables fの用途をメッセージングの表示で確認する警告記録項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM MQ for z/OS の Substitution variables fと CSQ9022I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Substitution variables fを IBM MQ メッセージングで扱う確認対象とし、用語名は警告記録用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The BSDS conversion utility (CSQJUCNV) on z/OS {#c12-i0785}
*分類: 管理リファレンス*  ・  難易度: 上級

The BSDS conversion utility (CSQJUCNV) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 監査記録の管理リファレンスでメッセージングの運用確認を行います。The BSDS conversion utilの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査記録の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査記録の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査記録の確認値として扱う。 ✅
    - D. The BSDS conversion utilの属性行を読まず監査記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では The BSDS conversion util は「IBM MQ for z/OS で The BSDS conversion utilの扱いを記録する監査記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では The BSDS conversion utilの表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では The BSDS conversion utilの使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The active log preformat utility (CSQJUFMT) on z/OS {#c12-i0786}
*分類: 管理リファレンス*  ・  難易度: 上級

The active log preformat utility (CSQJUFMT) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 復旧記録の管理リファレンスで The active log preformatの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. The active log preformatの出力を取らず復旧記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧記録で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では The active log preformat は「復旧記録の管理リファレンスに関係する定義値と表示行を照合する復旧記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では The active log preformatの属性行と CSQ9022I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では The active log preformatを IBM MQ メッセージングの運用手順で確認し、初出名は復旧記録初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The change log inventory utility (CSQJU003) on z/OS {#c12-i0787}
*分類: 管理リファレンス*  ・  難易度: 上級

The change log inventory utility (CSQJU003) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 変更記録の管理リファレンスに関する The change log inventoryの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録の管理リファレンスの証跡として保存して根拠にする。
    - C. The change log inventoryの変更点を出力本文から切り離して変更記録の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では The change log inventory は「The change log inventoryの状態と出力メッセージを結び付ける変更記録項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では The change log inventoryの出力行と CSQ9022I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では The change log inventoryを IBM MQ for z/OS の確認記録に残し、対象名は変更記録対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The dead-letter queue handler utility (CSQUDLQH) on z/OS {#c12-i0788}
*分類: 管理リファレンス*  ・  難易度: 上級

The dead-letter queue handler utility (CSQUDLQH) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 構文分離の管理リファレンスに関係する The dead-letter queue haの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を構文分離で確認する。 ✅
    - B. The dead-letter queue haの名称と担当者名のみを残して構文分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では The dead-letter queue ha は「The dead-letter queue haの用途をメッセージングの表示で確認する構文分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM MQ for z/OS の The dead-letter queue haと CSQ9022I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では The dead-letter queue haを IBM MQ メッセージングで扱う確認対象とし、用語名は構文分離用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The log print utility (CSQ1LOGP) on z/OS {#c12-i0789}
*分類: 管理リファレンス*  ・  難易度: 上級

The log print utility (CSQ1LOGP) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 展開分離の管理リファレンスで The log print utility 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. The log print utility 属性の出力を取らず展開分離の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、展開分離の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して展開分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では The log print utility 属性 は「展開分離の管理リファレンスに関係する定義値と表示行を照合する展開分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では The log print utility 属性の属性行と CSQ9022I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では The log print utility 属性を IBM MQ メッセージングの運用手順で確認し、初出名は展開分離初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The message security policy utility (CSQ0UTIL) {#c12-i0790}
*分類: 管理リファレンス*  ・  難易度: 上級

The message security policy utility (CSQ0UTIL)は、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 呼出分離の管理リファレンスでメッセージングの運用確認を行います。The message security polの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出分離の管理リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出分離の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出分離の確認記録にまとめる。 ✅
    - D. The message security polの属性行を読まず呼出分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では The message security pol は「IBM MQ for z/OS で The message security polの扱いを記録する呼出分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では The message security polの表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では The message security polの使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The print log map utility (CSQJU004) on z/OS {#c12-i0791}
*分類: 管理リファレンス*  ・  難易度: 上級

The print log map utility (CSQJU004) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 置換分離の管理リファレンスに関する The print log map utilitの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず置換分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の管理リファレンスの証跡として保存して根拠にする。
    - C. The print log map utilitの変更点を出力本文から切り離して置換分離の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換分離の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では The print log map utilit は「The print log map utilitの状態と出力メッセージを結び付ける置換分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では The print log map utilitの出力行と CSQ9022I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では The print log map utilitを IBM MQ for z/OS の確認記録に残し、対象名は置換分離対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### The queue sharing group utility (CSQ5PQSG) on z/OS {#c12-i0792}
*分類: 管理リファレンス*  ・  難易度: 上級

The queue sharing group utility (CSQ5PQSG) on z/OSは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 終端分離の管理リファレンスに関係する The queue sharing groupの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、終端分離の結果として保存する。 ✅
    - B. The queue sharing groupの名称と担当者名のみを残して終端分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では The queue sharing group は「The queue sharing groupの用途をメッセージングの表示で確認する終端分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM MQ for z/OS の The queue sharing groupと CSQ9022I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では The queue sharing groupを IBM MQ メッセージングで扱う確認対象とし、用語名は終端分離用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### XML message formats used by MFT {#c12-i0793}
*分類: 管理リファレンス*  ・  難易度: 上級

XML message formats used by MFTは、IBM MQ メッセージングの管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 探索分離の管理リファレンスで XML message formats usedの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. XML message formats usedの出力を取らず探索分離の管理リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、探索分離の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では XML message formats used は「探索分離の管理リファレンスに関係する定義値と表示行を照合する探索分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では XML message formats usedの属性行と CSQ9022I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では XML message formats usedを IBM MQ メッセージングの運用手順で確認し、初出名は探索分離初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference




## IBM MQ メッセージング > 計画 (キャパシティ / 可用性)

### Architectures based on a single queue manager {#c12-i0794}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Architectures based on a single queue managerは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 上書分離の計画 キャパシティ 可用性でメッセージングの運用確認を行います。Architectures based on aの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書分離の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書分離の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書分離として引き継ぐ。 ✅
    - D. Architectures based on aの属性行を読まず上書分離の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では Architectures based on a は「IBM MQ for z/OS で Architectures based on aの扱いを記録する上書分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では Architectures based on aの表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では Architectures based on aの使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Architectures based on multiple queue managers {#c12-i0795}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Architectures based on multiple queue managersは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 出力分離の計画 キャパシティ 可用性に関する Architectures based on mの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず出力分離の計画 キャパシティ 可用性の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離の計画 キャパシティ 可用性の証跡として保存して根拠にする。
    - C. Architectures based on mの変更点を出力本文から切り離して出力分離の計画 キャパシティ 可用性の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力分離の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では Architectures based on m は「Architectures based on mの状態と出力メッセージを結び付ける出力分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では Architectures based on mの出力行と CSQ9022I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では Architectures based on mを IBM MQ for z/OS の確認記録に残し、対象名は出力分離対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Choosing circular or linear logging on Multiplatforms {#c12-i0796}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Choosing circular or linear logging on Multiplatformsは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 条件分離の計画 キャパシティ 可用性に関係する Choosing circular or linの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、条件分離の点検結果を残す。 ✅
    - B. Choosing circular or linの名称と担当者名のみを残して条件分離の計画 キャパシティ 可用性の表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件分離の計画 キャパシティ 可用性を確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件分離の計画 キャパシティ 可用性の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では Choosing circular or lin は「Choosing circular or linの用途をメッセージングの表示で確認する条件分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM MQ for z/OS の Choosing circular or linと CSQ9022I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では Choosing circular or linを IBM MQ メッセージングで扱う確認対象とし、用語名は条件分離用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Disk space requirements on Multiplatforms {#c12-i0797}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Disk space requirements on Multiplatformsは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 区切分離の計画 キャパシティ 可用性で Disk space requirementsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Disk space requirementsの出力を取らず区切分離の計画 キャパシティ 可用性の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切分離で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して区切分離の計画 キャパシティ 可用性の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離の計画 キャパシティ 可用性へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では Disk space requirements は「区切分離の計画 キャパシティ 可用性に関係する定義値と表示行を照合する区切分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では Disk space requirementsの属性行と CSQ9022I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では Disk space requirementsを IBM MQ メッセージングの運用手順で確認し、初出名は区切分離初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ and IBM MQ Appliance on premises considerations for GDPR readiness {#c12-i0798}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

IBM MQ and IBM MQ Appliance on premises considerations for GDPR readinessは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 範囲分離の計画 キャパシティ 可用性でメッセージングの運用確認を行います。IBM MQ and IBM MQ Appliaの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲分離の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲分離の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲分離の確認値として扱う。 ✅
    - D. IBM MQ and IBM MQ Appliaの属性行を読まず範囲分離の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では IBM MQ and IBM MQ Applia は「IBM MQ for z/OS で IBM MQ and IBM MQ Appliaの扱いを記録する範囲分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では IBM MQ and IBM MQ Appliaの表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では IBM MQ and IBM MQ Appliaの使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ and UNIX Process Priority {#c12-i0799}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

IBM MQ and UNIX Process Priorityは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 優先分離の計画 キャパシティ 可用性に関する IBM MQ and UNIX Processの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先分離の計画 キャパシティ 可用性の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離の計画 キャパシティ 可用性の証跡として保存して根拠にする。
    - C. IBM MQ and UNIX Processの変更点を出力本文から切り離して優先分離の計画 キャパシティ 可用性の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先分離の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では IBM MQ and UNIX Process は「IBM MQ and UNIX Processの状態と出力メッセージを結び付ける優先分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では IBM MQ and UNIX Processの出力行と CSQ9022I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では IBM MQ and UNIX Processを IBM MQ for z/OS の確認記録に残し、対象名は優先分離対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ and UNIX System V IPC resources {#c12-i0800}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

IBM MQ and UNIX System V IPC resourcesは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 記録分離の計画 キャパシティ 可用性に関係する IBM MQ and UNIX System V の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を記録分離で確認する。 ✅
    - B. IBM MQ and UNIX System V の名称と担当者名のみを残して記録分離の計画 キャパシティ 可用性の表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録分離の計画 キャパシティ 可用性を確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録分離の計画 キャパシティ 可用性の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では IBM MQ and UNIX System V は「IBM MQ and UNIX System V の用途をメッセージングの表示で確認する記録分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM MQ for z/OS の IBM MQ and UNIX System V と CSQ9022I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では IBM MQ and UNIX System V を IBM MQ メッセージングで扱う確認対象とし、用語名は記録分離用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### IBM MQ release types: planning considerations {#c12-i0801}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

IBM MQ release types: planning considerationsは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 計画ガイド [mq93.plan.pdf p.6] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.6]

??? question "確認問題（1問）"
    **問題.** 比較分離の:で IBM MQ release types: plの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IBM MQ release types: plの出力を取らず比較分離の:の説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、比較分離の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して比較分離の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では IBM MQ release types: pl は「比較分離の:に関係する定義値と表示行を照合する比較分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では IBM MQ release types: plの属性行と CSQ9022I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では IBM MQ release types: plを IBM MQ メッセージングの運用手順で確認し、初出名は比較分離初出です。

    **出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.6]



### Planning {#c12-i0802}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planningは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 計画ガイド [mq93.plan.pdf p.5] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.5]

??? question "確認問題（1問）"
    **問題.** 順序分離の計画 キャパシティ 可用性でメッセージングの運用確認を行います。Planningの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序分離の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序分離の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序分離の確認記録にまとめる。 ✅
    - D. Planningの属性行を読まず順序分離の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では Planning は「IBM MQ for z/OS で Planningの扱いを記録する順序分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では Planningの表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では Planningの使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.5]



### Planning file system support for MFT on Multiplatforms {#c12-i0803}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning file system support for MFT on Multiplatformsは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 値域分離の計画 キャパシティ 可用性に関する Planning file system supの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域分離の計画 キャパシティ 可用性の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離の計画 キャパシティ 可用性の証跡として保存して根拠にする。
    - C. Planning file system supの変更点を出力本文から切り離して値域分離の計画 キャパシティ 可用性の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域分離の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では Planning file system sup は「Planning file system supの状態と出力メッセージを結び付ける値域分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では Planning file system supの出力行と CSQ9022I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では Planning file system supを IBM MQ for z/OS の確認記録に残し、対象名は値域分離対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning file system support on Multiplatforms {#c12-i0804}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning file system support on Multiplatformsは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 警告分離の計画 キャパシティ 可用性に関係する Planning file system supの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、警告分離の結果として保存する。 ✅
    - B. Planning file system supの名称と担当者名のみを残して警告分離の計画 キャパシティ 可用性の表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告分離の計画 キャパシティ 可用性を確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告分離の計画 キャパシティ 可用性の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では Planning file system sup は「Planning file system supの用途をメッセージングの表示で確認する警告分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM MQ for z/OS の Planning file system supと CSQ9022I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では Planning file system supを IBM MQ メッセージングで扱う確認対象とし、用語名は警告分離用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning for Advanced Message Security {#c12-i0805}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning for Advanced Message Securityは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 復旧分離の計画 キャパシティ 可用性で Planning for Advanced Meの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning for Advanced Meの出力を取らず復旧分離の計画 キャパシティ 可用性の説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、復旧分離の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧分離の計画 キャパシティ 可用性の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離の計画 キャパシティ 可用性へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Planning for Advanced Me は「復旧分離の計画 キャパシティ 可用性に関係する定義値と表示行を照合する復旧分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Planning for Advanced Meの属性行と CSQ9022I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Planning for Advanced Meを IBM MQ メッセージングの運用手順で確認し、初出名は復旧分離初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning for Managed File Transfer {#c12-i0806}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning for Managed File Transferは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 変更分離の計画 キャパシティ 可用性に関する Planning for Managed Filの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更分離の計画 キャパシティ 可用性の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離の計画 キャパシティ 可用性の証跡として保存して根拠にする。
    - C. Planning for Managed Filの変更点を出力本文から切り離して変更分離の計画 キャパシティ 可用性の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更分離の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では Planning for Managed Fil は「Planning for Managed Filの状態と出力メッセージを結び付ける変更分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では Planning for Managed Filの出力行と CSQ9022I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では Planning for Managed Filを IBM MQ for z/OS の確認記録に残し、対象名は変更分離対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning for backup and recovery {#c12-i0807}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning for backup and recoveryは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 監査分離の計画 キャパシティ 可用性でメッセージングの運用確認を行います。Planning for backup andの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査分離の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査分離の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査分離として引き継ぐ。 ✅
    - D. Planning for backup andの属性行を読まず監査分離の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Planning for backup and は「IBM MQ for z/OS で Planning for backup andの扱いを記録する監査分離項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Planning for backup andの表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Planning for backup andの使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning for your queue manager {#c12-i0808}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning for your queue managerは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 構文読解の計画 キャパシティ 可用性に関係する Planning for your queueの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、構文読解の点検結果を残す。 ✅
    - B. Planning for your queueの名称と担当者名のみを残して構文読解の計画 キャパシティ 可用性の表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文読解の計画 キャパシティ 可用性を確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文読解の計画 キャパシティ 可用性の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では Planning for your queue は「Planning for your queueの用途をメッセージングの表示で確認する構文読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM MQ for z/OS の Planning for your queueと CSQ9022I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では Planning for your queueを IBM MQ メッセージングで扱う確認対象とし、用語名は構文読解用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning to use the IBM MQ Console and REST API on z/OS {#c12-i0809}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning to use the IBM MQ Console and REST API on z/OSは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 展開読解の計画 キャパシティ 可用性で Planning to use the IBM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning to use the IBM の出力を取らず展開読解の計画 キャパシティ 可用性の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開読解で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して展開読解の計画 キャパシティ 可用性の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解の計画 キャパシティ 可用性へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では Planning to use the IBM は「展開読解の計画 キャパシティ 可用性に関係する定義値と表示行を照合する展開読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では Planning to use the IBM の属性行と CSQ9022I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では Planning to use the IBM を IBM MQ メッセージングの運用手順で確認し、初出名は展開読解初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your IBM MQ environment on z/OS {#c12-i0810}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your IBM MQ environment on z/OSは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 探索読解の計画 キャパシティ 可用性で Planning your IBM MQ envの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning your IBM MQ envの出力を取らず探索読解の計画 キャパシティ 可用性の説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、探索読解の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索読解の計画 キャパシティ 可用性の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解の計画 キャパシティ 可用性へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では Planning your IBM MQ env は「探索読解の計画 キャパシティ 可用性に関係する定義値と表示行を照合する探索読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では Planning your IBM MQ envの属性行と CSQ9022I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では Planning your IBM MQ envを IBM MQ メッセージングの運用手順で確認し、初出名は探索読解初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your channel initiator {#c12-i0811}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your channel initiatorは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 呼出読解の計画 キャパシティ 可用性でメッセージングの運用確認を行います。Planning your channel inの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出読解の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出読解の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出読解の確認値として扱う。 ✅
    - D. Planning your channel inの属性行を読まず呼出読解の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では Planning your channel in は「IBM MQ for z/OS で Planning your channel inの扱いを記録する呼出読解項目」と DISPLAY CHANNEL(*) ALL または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では Planning your channel inの表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では Planning your channel inの使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your distributed publish/subscribe network {#c12-i0812}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your distributed publish/subscribe networkは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 置換読解の計画 キャパシティ 可用性に関する Planning your distributeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY TOPIC(*) ALL の結果を残さず置換読解の計画 キャパシティ 可用性の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解の計画 キャパシティ 可用性の証跡として保存して根拠にする。
    - C. Planning your distributeの変更点を出力本文から切り離して置換読解の計画 キャパシティ 可用性の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換読解の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では Planning your distribute は「Planning your distributeの状態と出力メッセージを結び付ける置換読解項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では Planning your distributeの出力行と CSQ9022I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では Planning your distributeを IBM MQ for z/OS の確認記録に残し、対象名は置換読解対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your distributed queues and clusters {#c12-i0813}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your distributed queues and clustersは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 終端読解の計画 キャパシティ 可用性に関係する Planning your distributeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を終端読解で確認する。 ✅
    - B. Planning your distributeの名称と担当者名のみを残して終端読解の計画 キャパシティ 可用性の表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端読解の計画 キャパシティ 可用性を確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端読解の計画 キャパシティ 可用性の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では Planning your distribute は「Planning your distributeの用途をメッセージングの表示で確認する終端読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM MQ for z/OS の Planning your distributeと CSQ9022I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では Planning your distributeを IBM MQ メッセージングで扱う確認対象とし、用語名は終端読解用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your queue sharing group (QSG) {#c12-i0814}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your queue sharing group (QSG)は、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 上書読解の計画 キャパシティ 可用性でメッセージングの運用確認を行います。Planning your queue sharの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書読解の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書読解の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書読解の確認記録にまとめる。 ✅
    - D. Planning your queue sharの属性行を読まず上書読解の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Planning your queue shar は「IBM MQ for z/OS で Planning your queue sharの扱いを記録する上書読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Planning your queue sharの表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では Planning your queue sharの使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your storage and performance requirements on Multiplatforms {#c12-i0815}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your storage and performance requirements on Multiplatformsは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 出力読解の計画 キャパシティ 可用性に関する Planning your storage anの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず出力読解の計画 キャパシティ 可用性の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解の計画 キャパシティ 可用性の証跡として保存して根拠にする。
    - C. Planning your storage anの変更点を出力本文から切り離して出力読解の計画 キャパシティ 可用性の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力読解の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では Planning your storage an は「Planning your storage anの状態と出力メッセージを結び付ける出力読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では Planning your storage anの出力行と CSQ9022I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では Planning your storage anを IBM MQ for z/OS の確認記録に残し、対象名は出力読解対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Planning your z/OS UNIX environment {#c12-i0816}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Planning your z/OS UNIX environmentは、IBM MQ メッセージングの計画 (キャパシティ / 可用性)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 条件読解のPlanning your z/OS UNIX environmentに関係する Planning your z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、条件読解の結果として保存する。 ✅
    - B. Planning your z 属性の名称と担当者名のみを残して条件読解のPlanning your z/OS UNIX environmentの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件読解のPlanning your z/OS UNIX environmentを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件読解のPlanning your z/OS UNIX environmentの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では Planning your z 属性 は「Planning your z 属性の用途をメッセージングの表示で確認する条件読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM MQ for z/OS の Planning your z 属性と CSQ9022I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では Planning your z 属性を IBM MQ メッセージングで扱う確認対象とし、用語名は条件読解用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Programming interface information {#c12-i0817}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

Programming interface informationは、「Programming interface information」 (計画 (キャパシティ / 可用性)) — Programming interface information

**出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.204]


### Shared memory on AIX {#c12-i0818}
*分類: 計画 (キャパシティ / 可用性)*  ・  難易度: 上級

「Shared memory on AIX」 (計画 (キャパシティ / 可用性)) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.plan.pdf p.139))

**出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.139]

??? question "確認問題（1問）"
    **問題.** 範囲読解の計画 キャパシティ 可用性でメッセージングの運用確認を行います。Shared memory on AIX の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲読解の計画 キャパシティ 可用性を確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲読解の計画 キャパシティ 可用性を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲読解として引き継ぐ。 ✅
    - D. Shared memory on AIX の属性行を読まず範囲読解の計画 キャパシティ 可用性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Shared memory on AIX は「IBM MQ for z/OS で Shared memory on AIX の扱いを記録する範囲読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Shared memory on AIX の表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では Shared memory on AIX の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** MQ 9.3 計画ガイド [mq93.plan.pdf p.139]




## IBM MQ メッセージング > 運用コマンド > ALTER QMGR

### ALTER QMGR {#c12-i0819}
*分類: 運用コマンド > ALTER QMGR*  ・  難易度: 中級

ALTER QMGRは、キューマネージャーの属性を変更するMQSCコマンドです。DEADQで到達不能キューを、CHLAUTHでチャネル認証の有効を設定します

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 上書検分のメッセージングでメッセージングの運用確認を行います。ALTER QMGR の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書検分のメッセージングを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書検分のメッセージングを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書検分の根拠を固定する。 ✅
    - D. ALTER QMGR の属性行を読まず上書検分のメッセージングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では ALTER QMGR は「IBM MQ for z/OS で ALTER QMGR の扱いを記録する上書検分項目」と DISPLAY CHLAUTH(*) ALL または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では ALTER QMGR の表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では ALTER QMGR の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference




## IBM MQ メッセージング > 運用コマンド > DISPLAY CHSTATUS

### DISPLAY CHSTATUS {#c12-i0820}
*分類: 運用コマンド > DISPLAY CHSTATUS*  ・  難易度: 中級

DISPLAY CHSTATUSは、指定したチャネルの実行時の状態を表示するMQSCコマンドで、同義語はDIS CHSです。状態がRUNNINGなら稼働中を表します

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（6問）"
    **問題.** チャネル状態表示を設計レビューで確認します。技術項目 DISPLAY CHSTATUS の設定値と管理コマンド応答を照合し、状態とサブ状態を記録します。新規経路を本番へ入れる前に、定義値と実行時状態の見方を合わせます。どのMQ項目を中心に確認しますか。

    - A. SSLCAUTH
    - B. CHLAUTH SSLPEERMAP
    - C. DISPLAY CHSTATUS ✅
    - D. XMITQ

    正解: **C** ／ 難易度: 初級

    **解説:** 正答チャネル状態表示棚卸はCです。状態面のチャネル状態表示復旧は、チャネルの実行状態とサブ状態を確認することを目的に扱う説明単位がチャネル状態表示照合です。背景チャネル状態表示復旧として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はチャネル状態表示照合です。証跡面のチャネル状態表示観点を読む管理コマンド応答は、状態とサブ状態を出典の属性説明と照合する点がチャネル状態表示証跡です。A: チャネル状態表示棚卸で見るクライアント証明書要求は役割が異なり、除外理由を説明する対象はチャネル状態表示棚卸です。B: チャネル状態表示復旧で見る証明書マップは役割が異なり、除外理由を説明する対象はチャネル状態表示復旧です。C: チャネル状態表示が正答です。チャネル状態表示照合の応答で確認できる対象はチャネル状態表示照合です。D: チャネル状態表示観点で見る伝送キューは役割が異なり、除外理由を説明する対象はチャネル状態表示観点です。初出語チャネル状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はチャネル状態表示定義です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** チャネル状態表示を変更審査で確認します。技術項目 DISPLAY CHSTATUS の設定値と管理コマンド応答を照合し、状態とサブ状態を記録します。暗号化や配信条件の変更前に、影響を受ける属性と証跡を整理します。どの選択肢が最も適切ですか。

    - A. DISPLAY CHSTATUS ✅
    - B. SUB attribute
    - C. SSLKEYR
    - D. DISPLAY QSTATUS

    正解: **A** ／ 難易度: 初級

    **解説:** 正答チャネル状態表示証跡はAです。監査面のチャネル状態表示読取は、チャネルの実行状態とサブ状態を確認することを目的に扱う説明単位がチャネル状態表示状態です。背景チャネル状態表示読取として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はチャネル状態表示状態です。引継ぎ面のチャネル状態表示定義を読む管理コマンド応答は、状態とサブ状態を出典の属性説明と照合する点がチャネル状態表示根拠です。A: チャネル状態表示が正答です。チャネル状態表示証跡の応答で確認できる対象はチャネル状態表示証跡です。B: チャネル状態表示読取で見る購読許可は役割が異なり、除外理由を説明する対象はチャネル状態表示読取です。C: チャネル状態表示状態で見る鍵リポジトリは役割が異なり、除外理由を説明する対象はチャネル状態表示状態です。D: チャネル状態表示定義で見るキュー状態表示は役割が異なり、除外理由を説明する対象はチャネル状態表示定義です。初出語チャネル状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はチャネル状態表示監査です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** チャネル状態表示を障害切り分けで確認します。技術項目 DISPLAY CHSTATUS の設定値と管理コマンド応答を照合し、状態とサブ状態を記録します。メッセージ滞留や接続失敗の原因を、MQSC応答とメッセージIDから絞ります。優先して確認する項目はどれですか。

    - A. DISCINT
    - B. SSLCIPH
    - C. DISPLAY CHSTATUS ✅
    - D. DEFPSIST

    正解: **C** ／ 難易度: 初級

    **解説:** 正答チャネル状態表示根拠はCです。記録面のチャネル状態表示応答は、チャネルの実行状態とサブ状態を確認することを目的に扱う説明単位がチャネル状態表示保守です。背景チャネル状態表示応答として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はチャネル状態表示保守です。設計面のチャネル状態表示監査を読む管理コマンド応答は、状態とサブ状態を出典の属性説明と照合する点がチャネル状態表示引継ぎです。A: チャネル状態表示根拠で見る切断間隔は役割が異なり、除外理由を説明する対象はチャネル状態表示根拠です。B: チャネル状態表示応答で見る暗号仕様は役割が異なり、除外理由を説明する対象はチャネル状態表示応答です。C: チャネル状態表示が正答です。チャネル状態表示保守の応答で確認できる対象はチャネル状態表示保守です。D: チャネル状態表示監査で見る既定永続性は役割が異なり、除外理由を説明する対象はチャネル状態表示監査です。初出語チャネル状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はチャネル状態表示照合です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** チャネル状態表示を監査証跡で確認します。技術項目 DISPLAY CHSTATUS の設定値と管理コマンド応答を照合し、状態とサブ状態を記録します。操作後に、定義、状態、出力メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. DISPLAY CHSTATUS ✅
    - B. CHLAUTH SSLPEERMAP
    - C. DISPLAY SUB
    - D. PUB attribute

    正解: **A** ／ 難易度: 初級

    **解説:** 正答チャネル状態表示引継ぎはAです。運用面のチャネル状態表示棚卸は、チャネルの実行状態とサブ状態を確認することを目的に扱う説明単位がチャネル状態表示復旧です。背景チャネル状態表示棚卸として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はチャネル状態表示復旧です。接続面のチャネル状態表示照合を読む管理コマンド応答は、状態とサブ状態を出典の属性説明と照合する点がチャネル状態表示観点です。A: チャネル状態表示が正答です。チャネル状態表示引継ぎの応答で確認できる対象はチャネル状態表示引継ぎです。B: チャネル状態表示棚卸で見る証明書マップは役割が異なり、除外理由を説明する対象はチャネル状態表示棚卸です。C: チャネル状態表示復旧で見る購読定義表示は役割が異なり、除外理由を説明する対象はチャネル状態表示復旧です。D: チャネル状態表示照合で見る発行許可は役割が異なり、除外理由を説明する対象はチャネル状態表示照合です。初出語チャネル状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はチャネル状態表示状態です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** チャネル状態表示を運用引継ぎで確認します。技術項目 DISPLAY CHSTATUS の設定値と管理コマンド応答を照合し、状態とサブ状態を記録します。担当者が交代しても同じ確認順で読めるよう、属性名と出力欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. PSPROP
    - B. DISPLAY TOPIC
    - C. DISPLAY CHSTATUS ✅
    - D. DISPLAY TPSTATUS

    正解: **C** ／ 難易度: 初級

    **解説:** 正答チャネル状態表示観点はCです。証跡面のチャネル状態表示証跡は、チャネルの実行状態とサブ状態を確認することを目的に扱う説明単位がチャネル状態表示読取です。背景チャネル状態表示証跡として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はチャネル状態表示読取です。復旧面のチャネル状態表示状態を読む管理コマンド応答は、状態とサブ状態を出典の属性説明と照合する点がチャネル状態表示定義です。A: チャネル状態表示観点で見る発行購読プロパティは役割が異なり、除外理由を説明する対象はチャネル状態表示観点です。B: チャネル状態表示証跡で見るトピック表示は役割が異なり、除外理由を説明する対象はチャネル状態表示証跡です。C: チャネル状態表示が正答です。チャネル状態表示読取の応答で確認できる対象はチャネル状態表示読取です。D: チャネル状態表示状態で見るトピック状態は役割が異なり、除外理由を説明する対象はチャネル状態表示状態です。初出語チャネル状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はチャネル状態表示保守です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** 終端検分のメッセージングに関係する DISPLAY CHSTATUS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検分で再確認できる形にする。 ✅
    - B. DISPLAY CHSTATUS の名称と担当者名のみを残して終端検分のメッセージングの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端検分のメッセージングを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端検分のメッセージングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では DISPLAY CHSTATUS は「DISPLAY CHSTATUS の用途をメッセージングの表示で確認する終端検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM MQ for z/OS の DISPLAY CHSTATUS と CSQ9022I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では DISPLAY CHSTATUS を IBM MQ メッセージングで扱う確認対象とし、用語名は終端検分用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference




## IBM MQ メッセージング > 運用コマンド > DISPLAY QSTATUS

### DISPLAY QSTATUS {#c12-i0821}
*分類: 運用コマンド > DISPLAY QSTATUS*  ・  難易度: 中級

DISPLAY QSTATUSは、指定したキューの実行時の状態を表示するMQSCコマンドです。応答のCURDEPTHで現在のメッセージ件数を確認できます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（6問）"
    **問題.** キュー状態表示を設計レビューで確認します。技術項目 DISPLAY QSTATUS の設定値と管理コマンド応答を照合し、現在深度と入力プロセス数を記録します。新規経路を本番へ入れる前に、定義値と実行時状態の見方を合わせます。どのMQ項目を中心に確認しますか。

    - A. DISCINT
    - B. TOPICSTR
    - C. DISPLAY QSTATUS ✅
    - D. DISPLAY SUB

    正解: **C** ／ 難易度: 初級

    **解説:** 正答キュー状態表示証跡はCです。照合面のキュー状態表示読取は、キュー深さや入出力プロセス数を確認することを目的に扱う説明単位がキュー状態表示状態です。背景キュー状態表示読取として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はキュー状態表示状態です。運用面のキュー状態表示定義を読む管理コマンド応答は、現在深度と入力プロセス数を出典の属性説明と照合する点がキュー状態表示根拠です。A: キュー状態表示証跡で見る切断間隔は役割が異なり、除外理由を説明する対象はキュー状態表示証跡です。B: キュー状態表示読取で見るトピック文字列は役割が異なり、除外理由を説明する対象はキュー状態表示読取です。C: キュー状態表示が正答です。キュー状態表示状態の応答で確認できる対象はキュー状態表示状態です。D: キュー状態表示定義で見る購読定義表示は役割が異なり、除外理由を説明する対象はキュー状態表示定義です。初出語キュー状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はキュー状態表示監査です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** キュー状態表示を変更審査で確認します。技術項目 DISPLAY QSTATUS の設定値と管理コマンド応答を照合し、現在深度と入力プロセス数を記録します。暗号化や配信条件の変更前に、影響を受ける属性と証跡を整理します。どの選択肢が最も適切ですか。

    - A. DISPLAY QSTATUS ✅
    - B. SSLPEER
    - C. MAXDEPTH
    - D. SSLCIPH

    正解: **A** ／ 難易度: 初級

    **解説:** 正答キュー状態表示根拠はAです。状態面のキュー状態表示応答は、キュー深さや入出力プロセス数を確認することを目的に扱う説明単位がキュー状態表示保守です。背景キュー状態表示応答として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はキュー状態表示保守です。証跡面のキュー状態表示監査を読む管理コマンド応答は、現在深度と入力プロセス数を出典の属性説明と照合する点がキュー状態表示引継ぎです。A: キュー状態表示が正答です。キュー状態表示根拠の応答で確認できる対象はキュー状態表示根拠です。B: キュー状態表示応答で見る相手証明書名は役割が異なり、除外理由を説明する対象はキュー状態表示応答です。C: キュー状態表示保守で見る最大キュー深度は役割が異なり、除外理由を説明する対象はキュー状態表示保守です。D: キュー状態表示監査で見る暗号仕様は役割が異なり、除外理由を説明する対象はキュー状態表示監査です。初出語キュー状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はキュー状態表示照合です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** キュー状態表示を障害切り分けで確認します。技術項目 DISPLAY QSTATUS の設定値と管理コマンド応答を照合し、現在深度と入力プロセス数を記録します。メッセージ滞留や接続失敗の原因を、MQSC応答とメッセージIDから絞ります。優先して確認する項目はどれですか。

    - A. DURABLE subscription
    - B. CONNAME
    - C. DISPLAY QSTATUS ✅
    - D. SSLKEYR

    正解: **C** ／ 難易度: 初級

    **解説:** 正答キュー状態表示引継ぎはCです。監査面のキュー状態表示棚卸は、キュー深さや入出力プロセス数を確認することを目的に扱う説明単位がキュー状態表示復旧です。背景キュー状態表示棚卸として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はキュー状態表示復旧です。引継ぎ面のキュー状態表示照合を読む管理コマンド応答は、現在深度と入力プロセス数を出典の属性説明と照合する点がキュー状態表示観点です。A: キュー状態表示引継ぎで見る永続購読は役割が異なり、除外理由を説明する対象はキュー状態表示引継ぎです。B: キュー状態表示棚卸で見る接続名は役割が異なり、除外理由を説明する対象はキュー状態表示棚卸です。C: キュー状態表示が正答です。キュー状態表示復旧の応答で確認できる対象はキュー状態表示復旧です。D: キュー状態表示照合で見る鍵リポジトリは役割が異なり、除外理由を説明する対象はキュー状態表示照合です。初出語キュー状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はキュー状態表示状態です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** キュー状態表示を監査証跡で確認します。技術項目 DISPLAY QSTATUS の設定値と管理コマンド応答を照合し、現在深度と入力プロセス数を記録します。操作後に、定義、状態、出力メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. DISPLAY QSTATUS ✅
    - B. TOPICSTR
    - C. STOP CHANNEL
    - D. CHLAUTH SSLPEERMAP

    正解: **A** ／ 難易度: 初級

    **解説:** 正答キュー状態表示観点はAです。記録面のキュー状態表示証跡は、キュー深さや入出力プロセス数を確認することを目的に扱う説明単位がキュー状態表示読取です。背景キュー状態表示証跡として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はキュー状態表示読取です。設計面のキュー状態表示状態を読む管理コマンド応答は、現在深度と入力プロセス数を出典の属性説明と照合する点がキュー状態表示定義です。A: キュー状態表示が正答です。キュー状態表示観点の応答で確認できる対象はキュー状態表示観点です。B: キュー状態表示証跡で見るトピック文字列は役割が異なり、除外理由を説明する対象はキュー状態表示証跡です。C: キュー状態表示読取で見るチャネル停止は役割が異なり、除外理由を説明する対象はキュー状態表示読取です。D: キュー状態表示状態で見る証明書マップは役割が異なり、除外理由を説明する対象はキュー状態表示状態です。初出語キュー状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はキュー状態表示保守です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** キュー状態表示を運用引継ぎで確認します。技術項目 DISPLAY QSTATUS の設定値と管理コマンド応答を照合し、現在深度と入力プロセス数を記録します。担当者が交代しても同じ確認順で読めるよう、属性名と出力欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. DISPLAY CHSTATUS
    - B. DEFINE CHANNEL SDR
    - C. DISPLAY QSTATUS ✅
    - D. DEFINE CHANNEL RCVR

    正解: **C** ／ 難易度: 初級

    **解説:** 正答キュー状態表示定義はCです。運用面のキュー状態表示根拠は、キュー深さや入出力プロセス数を確認することを目的に扱う説明単位がキュー状態表示応答です。背景キュー状態表示根拠として、キューマネージャーの定義値、実行時状態、応答メッセージを結ぶ証跡単位はキュー状態表示応答です。接続面のキュー状態表示保守を読む管理コマンド応答は、現在深度と入力プロセス数を出典の属性説明と照合する点がキュー状態表示監査です。A: キュー状態表示定義で見るチャネル状態表示は役割が異なり、除外理由を説明する対象はキュー状態表示定義です。B: キュー状態表示根拠で見る送信チャネル定義は役割が異なり、除外理由を説明する対象はキュー状態表示根拠です。C: キュー状態表示が正答です。キュー状態表示応答の応答で確認できる対象はキュー状態表示応答です。D: キュー状態表示保守で見る受信チャネル定義は役割が異なり、除外理由を説明する対象はキュー状態表示保守です。初出語キュー状態表示とは、IBM MQ 9.3で扱う定義、属性、または管理操作のことで、用語定義はキュー状態表示復旧です。

    **出典:** mq93.refadmin / mq93.administer / mq93.secure / mq93.reference / mq93.configure

    ---

    **問題.** 置換検分のメッセージングに関する DISPLAY QSTATUS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず置換検分のメッセージングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のメッセージングの証跡として保存して根拠にする。
    - C. DISPLAY QSTATUS の変更点を出力本文から切り離して置換検分のメッセージングの承認欄のみ残す。
    - D. IBM MQ for z/OS の表示形式に沿って根拠行を採り、置換検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では DISPLAY QSTATUS は「DISPLAY QSTATUS の状態と出力メッセージを結び付ける置換検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では DISPLAY QSTATUS の出力行と CSQ9022I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では DISPLAY QSTATUS を IBM MQ for z/OS の確認記録に残し、対象名は置換検分対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference




## IBM MQ メッセージング > 運用コマンド > runmqsc

### runmqsc {#c12-i0822}
*分類: 運用コマンド > runmqsc*  ・  難易度: 初級

runmqscは、MQSCコマンドをキューマネージャーへ渡して実行する制御コマンドです。対象のキューマネージャー名を引数に与えて起動します

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 探索検分のメッセージングでrunmqscの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. runmqscの出力を取らず探索検分のメッセージングの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索検分の確認値として扱う。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索検分のメッセージングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のメッセージングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠ではrunmqsc は「探索検分のメッセージングに関係する定義値と表示行を照合する探索検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡ではrunmqscの属性行と CSQ9022I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出ではrunmqscを IBM MQ メッセージングの運用手順で確認し、初出名は探索検分初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference




## IBM MQ メッセージング > 開発リファレンス

### .NET interfaces {#c12-i0823}
*分類: 開発リファレンス*  ・  難易度: 上級

.NET interfacesは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1929] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1929]

??? question "確認問題（1問）"
    **問題.** 優先読解の開発リファレンスに関する.NET interfacesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先読解の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解の開発リファレンスの証跡として保存して根拠にする。
    - C. .NET interfacesの変更点を出力本文から切り離して優先読解の開発リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先読解の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では.NET interfaces は「.NET interfacesの状態と出力メッセージを結び付ける優先読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では.NET interfacesの出力行と CSQ9022I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では.NET interfacesを IBM MQ for z/OS の確認記録に残し、対象名は優先読解対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1929]



### API exit reference {#c12-i0824}
*分類: 開発リファレンス*  ・  難易度: 上級

API exit referenceは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1544] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1544]

??? question "確認問題（1問）"
    **問題.** 記録読解の開発リファレンスに関係する API exit referenceの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、記録読解の点検結果を残す。 ✅
    - B. API exit referenceの名称と担当者名のみを残して記録読解の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録読解の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録読解の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では API exit reference は「API exit referenceの用途をメッセージングの表示で確認する記録読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM MQ for z/OS の API exit referenceと CSQ9022I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では API exit referenceを IBM MQ メッセージングで扱う確認対象とし、用語名は記録読解用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1544]



### APPLICATIONNAME {#c12-i0825}
*分類: 開発リファレンス*  ・  難易度: 上級

APPLICATIONNAMEは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1878] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1878]

??? question "確認問題（1問）"
    **問題.** 比較読解の開発リファレンスで APPLICATIONNAME の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. APPLICATIONNAME の出力を取らず比較読解の開発リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較読解で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して比較読解の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では APPLICATIONNAME は「比較読解の開発リファレンスに関係する定義値と表示行を照合する比較読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では APPLICATIONNAME の属性行と CSQ9022I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では APPLICATIONNAME を IBM MQ メッセージングの運用手順で確認し、初出名は比較読解初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1878]



### ASYNCEXCEPTION {#c12-i0826}
*分類: 開発リファレンス*  ・  難易度: 上級

ASYNCEXCEPTIONは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1879] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1879]

??? question "確認問題（1問）"
    **問題.** 値域読解の開発リファレンスに関する ASYNCEXCEPTION の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域読解の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解の開発リファレンスの証跡として保存して根拠にする。
    - C. ASYNCEXCEPTION の変更点を出力本文から切り離して値域読解の開発リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域読解の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では ASYNCEXCEPTION は「ASYNCEXCEPTION の状態と出力メッセージを結び付ける値域読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では ASYNCEXCEPTION の出力行と CSQ9022I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では ASYNCEXCEPTION を IBM MQ for z/OS の確認記録に残し、対象名は値域読解対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1879]



### Applications {#c12-i0827}
*分類: 開発リファレンス*  ・  難易度: 上級

「Applications」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1398))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1398]

??? question "確認問題（1問）"
    **問題.** 順序読解の開発リファレンスでメッセージングの運用確認を行います。Applicationsの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序読解の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序読解の開発リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序読解の確認値として扱う。 ✅
    - D. Applicationsの属性行を読まず順序読解の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Applications は「IBM MQ for z/OS で Applicationsの扱いを記録する順序読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Applicationsの表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Applicationsの使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1398]



### Attributes of objects {#c12-i0828}
*分類: 開発リファレンス*  ・  難易度: 上級

「Attributes of objects」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.786))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.786]

??? question "確認問題（1問）"
    **問題.** 警告読解の開発リファレンスに関係する Attributes of objectsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を警告読解で確認する。 ✅
    - B. Attributes of objectsの名称と担当者名のみを残して警告読解の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告読解の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告読解の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Attributes of objects は「Attributes of objectsの用途をメッセージングの表示で確認する警告読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM MQ for z/OS の Attributes of objectsと CSQ9022I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Attributes of objectsを IBM MQ メッセージングで扱う確認対象とし、用語名は警告読解用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.786]



### Attributes of objects on IBM i {#c12-i0829}
*分類: 開発リファレンス*  ・  難易度: 上級

Attributes of objects on IBM iは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 復旧読解の開発リファレンスで Attributes of objects onの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Attributes of objects onの出力を取らず復旧読解の開発リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、復旧読解の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧読解の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では Attributes of objects on は「復旧読解の開発リファレンスに関係する定義値と表示行を照合する復旧読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では Attributes of objects onの属性行と CSQ9022I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では Attributes of objects onを IBM MQ メッセージングの運用手順で確認し、初出名は復旧読解初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### BALOPTIONS {#c12-i0830}
*分類: 開発リファレンス*  ・  難易度: 上級

BALOPTIONSは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1880] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1880]

??? question "確認問題（1問）"
    **問題.** 監査読解の開発リファレンスでメッセージングの運用確認を行います。BALOPTIONS の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査読解の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査読解の開発リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査読解の確認記録にまとめる。 ✅
    - D. BALOPTIONS の属性行を読まず監査読解の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では BALOPTIONS は「IBM MQ for z/OS で BALOPTIONS の扱いを記録する監査読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では BALOPTIONS の表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では BALOPTIONS の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1880]



### BALTIMEOUT {#c12-i0831}
*分類: 開発リファレンス*  ・  難易度: 上級

BALTIMEOUTは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1881] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1881]

??? question "確認問題（1問）"
    **問題.** 変更読解の開発リファレンスに関する BALTIMEOUT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更読解の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解の開発リファレンスの証跡として保存して根拠にする。
    - C. BALTIMEOUT の変更点を出力本文から切り離して変更読解の開発リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更読解の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では BALTIMEOUT は「BALTIMEOUT の状態と出力メッセージを結び付ける変更読解項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では BALTIMEOUT の出力行と CSQ9022I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では BALTIMEOUT を IBM MQ for z/OS の確認記録に残し、対象名は変更読解対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1881]



### BALTYPE {#c12-i0832}
*分類: 開発リファレンス*  ・  難易度: 上級

BALTYPEは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1880] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1880]

??? question "確認問題（1問）"
    **問題.** 構文検分の開発リファレンスに関係する BALTYPE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、構文検分の結果として保存する。 ✅
    - B. BALTYPE の名称と担当者名のみを残して構文検分の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文検分の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文検分の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では BALTYPE は「BALTYPE の用途をメッセージングの表示で確認する構文検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM MQ for z/OS の BALTYPE と CSQ9022I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では BALTYPE を IBM MQ メッセージングで扱う確認対象とし、用語名は構文検分用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1880]



### BROKERCCDURSUBQ {#c12-i0833}
*分類: 開発リファレンス*  ・  難易度: 上級

BROKERCCDURSUBQは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1881] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1881]

??? question "確認問題（1問）"
    **問題.** 展開検分の開発リファレンスで BROKERCCDURSUBQ の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BROKERCCDURSUBQ の出力を取らず展開検分の開発リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY TOPIC(*) ALL で得た表示本文を使い、展開検分の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY TOPIC(*) ALL を省略して展開検分の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では BROKERCCDURSUBQ は「展開検分の開発リファレンスに関係する定義値と表示行を照合する展開検分項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では BROKERCCDURSUBQ の属性行と CSQ9022I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では BROKERCCDURSUBQ を IBM MQ メッセージングの運用手順で確認し、初出名は展開検分初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1881]



### BROKERCCSUBQ {#c12-i0834}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERCCSUBQ」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1882))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1882]

??? question "確認問題（1問）"
    **問題.** 呼出検分の開発リファレンスでメッセージングの運用確認を行います。BROKERCCSUBQ の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出検分の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出検分の開発リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出検分として引き継ぐ。 ✅
    - D. BROKERCCSUBQ の属性行を読まず呼出検分の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では BROKERCCSUBQ は「IBM MQ for z/OS で BROKERCCSUBQ の扱いを記録する呼出検分項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では BROKERCCSUBQ の表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では BROKERCCSUBQ の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1882]



### BROKERCONQ {#c12-i0835}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERCONQ」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1882))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1882]

??? question "確認問題（1問）"
    **問題.** 置換検分の開発リファレンスに関する BROKERCONQ の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず置換検分の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分の開発リファレンスの証跡として保存して根拠にする。
    - C. BROKERCONQ の変更点を出力本文から切り離して置換検分の開発リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換検分の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では BROKERCONQ は「BROKERCONQ の状態と出力メッセージを結び付ける置換検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では BROKERCONQ の出力行と CSQ9022I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では BROKERCONQ を IBM MQ for z/OS の確認記録に残し、対象名は置換検分対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1882]



### BROKERDURSUBQ {#c12-i0836}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERDURSUBQ」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1883))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1883]

??? question "確認問題（1問）"
    **問題.** 終端検分の開発リファレンスに関係する BROKERDURSUBQ の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、終端検分の点検結果を残す。 ✅
    - B. BROKERDURSUBQ の名称と担当者名のみを残して終端検分の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端検分の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端検分の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では BROKERDURSUBQ は「BROKERDURSUBQ の用途をメッセージングの表示で確認する終端検分項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM MQ for z/OS の BROKERDURSUBQ と CSQ9022I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では BROKERDURSUBQ を IBM MQ メッセージングで扱う確認対象とし、用語名は終端検分用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1883]



### BROKERPUBQ {#c12-i0837}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERPUBQ」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1883))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1883]

??? question "確認問題（1問）"
    **問題.** 探索検分の開発リファレンスで BROKERPUBQ の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BROKERPUBQ の出力を取らず探索検分の開発リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索検分で再確認できる形にする。 ✅
    - C. DISPLAY TOPIC(*) ALL を省略して探索検分の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では BROKERPUBQ は「探索検分の開発リファレンスに関係する定義値と表示行を照合する探索検分項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では BROKERPUBQ の属性行と CSQ9022I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では BROKERPUBQ を IBM MQ メッセージングの運用手順で確認し、初出名は探索検分初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1883]



### BROKERPUBQMGR {#c12-i0838}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERPUBQMGR」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1884))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1884]

??? question "確認問題（1問）"
    **問題.** 上書検分の開発リファレンスでメッセージングの運用確認を行います。BROKERPUBQMGR の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書検分の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書検分の開発リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書検分の確認値として扱う。 ✅
    - D. BROKERPUBQMGR の属性行を読まず上書検分の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では BROKERPUBQMGR は「IBM MQ for z/OS で BROKERPUBQMGR の扱いを記録する上書検分項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では BROKERPUBQMGR の表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では BROKERPUBQMGR の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1884]



### BROKERQMGR {#c12-i0839}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERQMGR」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1884))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1884]

??? question "確認問題（1問）"
    **問題.** 出力検分の開発リファレンスに関する BROKERQMGR の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず出力検分の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分の開発リファレンスの証跡として保存して根拠にする。
    - C. BROKERQMGR の変更点を出力本文から切り離して出力検分の開発リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力検分の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では BROKERQMGR は「BROKERQMGR の状態と出力メッセージを結び付ける出力検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では BROKERQMGR の出力行と CSQ9022I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では BROKERQMGR を IBM MQ for z/OS の確認記録に残し、対象名は出力検分対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1884]



### BROKERSUBQ {#c12-i0840}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERSUBQ」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1884))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1884]

??? question "確認問題（1問）"
    **問題.** 条件検分の開発リファレンスに関係する BROKERSUBQ の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. CSQ9022I を含む表示を保存し、説明欄との差分を条件検分で確認する。 ✅
    - B. BROKERSUBQ の名称と担当者名のみを残して条件検分の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件検分の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件検分の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では BROKERSUBQ は「BROKERSUBQ の用途をメッセージングの表示で確認する条件検分項目」と DISPLAY TOPIC(*) ALL または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM MQ for z/OS の BROKERSUBQ と CSQ9022I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では BROKERSUBQ を IBM MQ メッセージングで扱う確認対象とし、用語名は条件検分用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1884]



### BROKERVER {#c12-i0841}
*分類: 開発リファレンス*  ・  難易度: 上級

「BROKERVER」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1885))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1885]

??? question "確認問題（1問）"
    **問題.** 区切検分の開発リファレンスで BROKERVER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BROKERVER の出力を取らず区切検分の開発リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、区切検分の証跡として残す。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して区切検分の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では BROKERVER は「区切検分の開発リファレンスに関係する定義値と表示行を照合する区切検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では BROKERVER の属性行と CSQ9022I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では BROKERVER を IBM MQ メッセージングの運用手順で確認し、初出名は区切検分初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1885]



### C++ and MQI cross-reference {#c12-i0842}
*分類: 開発リファレンス*  ・  難易度: 上級

「C++ and MQI cross-reference」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1766))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1766]

??? question "確認問題（1問）"
    **問題.** 範囲検分の開発リファレンスでメッセージングの運用確認を行います。C++ and MQI cross-refereの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲検分の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲検分の開発リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲検分の確認記録にまとめる。 ✅
    - D. C++ and MQI cross-refereの属性行を読まず範囲検分の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では C++ and MQI cross-refere は「IBM MQ for z/OS で C++ and MQI cross-refereの扱いを記録する範囲検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では C++ and MQI cross-refereの表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では C++ and MQI cross-refereの使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1766]



### CCDTURL {#c12-i0843}
*分類: 開発リファレンス*  ・  難易度: 上級

「CCDTURL」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1886))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1886]

??? question "確認問題（1問）"
    **問題.** 優先検分の開発リファレンスに関する CCDTURL の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先検分の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分の開発リファレンスの証跡として保存して根拠にする。
    - C. CCDTURL の変更点を出力本文から切り離して優先検分の開発リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先検分の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では CCDTURL は「CCDTURL の状態と出力メッセージを結び付ける優先検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では CCDTURL の出力行と CSQ9022I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では CCDTURL を IBM MQ for z/OS の確認記録に残し、対象名は優先検分対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1886]



### CCSID {#c12-i0844}
*分類: 開発リファレンス*  ・  難易度: 上級

「CCSID」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1886))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1886]

??? question "確認問題（1問）"
    **問題.** 記録検分の開発リファレンスに関係する CCSID の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と CSQ9022I を読み、記録検分の結果として保存する。 ✅
    - B. CCSID の名称と担当者名のみを残して記録検分の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録検分の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録検分の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では CCSID は「CCSID の用途をメッセージングの表示で確認する記録検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM MQ for z/OS の CCSID と CSQ9022I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では CCSID を IBM MQ メッセージングで扱う確認対象とし、用語名は記録検分用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1886]



### CHANNEL {#c12-i0845}
*分類: 開発リファレンス*  ・  難易度: 上級

「CHANNEL」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1887))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1887]

??? question "確認問題（1問）"
    **問題.** 比較検分の開発リファレンスで CHANNEL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CHANNEL の出力を取らず比較検分の開発リファレンスの説明文と承認印のみを残す。
    - B. DISPLAY CHANNEL(*) ALL で得た表示本文を使い、比較検分の採否を説明欄に結び付ける。 ✅
    - C. DISPLAY CHANNEL(*) ALL を省略して比較検分の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では CHANNEL は「比較検分の開発リファレンスに関係する定義値と表示行を照合する比較検分項目」と DISPLAY CHANNEL(*) ALL または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では CHANNEL の属性行と CSQ9022I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では CHANNEL を IBM MQ メッセージングの運用手順で確認し、初出名は比較検分初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1887]



### CLEANUP {#c12-i0846}
*分類: 開発リファレンス*  ・  難易度: 上級

「CLEANUP」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1887))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1887]

??? question "確認問題（1問）"
    **問題.** 警告検分の開発リファレンスに関係する CLEANUP の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM MQ for z/OS の表示形式に沿って根拠行を採り、警告検分の点検結果を残す。 ✅
    - B. CLEANUP の名称と担当者名のみを残して警告検分の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告検分の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告検分の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では CLEANUP は「CLEANUP の用途をメッセージングの表示で確認する警告検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM MQ for z/OS の CLEANUP と CSQ9022I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では CLEANUP を IBM MQ メッセージングで扱う確認対象とし、用語名は警告検分用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1887]



### CLEANUPINT {#c12-i0847}
*分類: 開発リファレンス*  ・  難易度: 上級

「CLEANUPINT」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1888))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1888]

??? question "確認問題（1問）"
    **問題.** 復旧検分の開発リファレンスで CLEANUPINT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CLEANUPINT の出力を取らず復旧検分の開発リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧検分で再確認できる形にする。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧検分の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では CLEANUPINT は「復旧検分の開発リファレンスに関係する定義値と表示行を照合する復旧検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では CLEANUPINT の属性行と CSQ9022I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では CLEANUPINT を IBM MQ メッセージングの運用手順で確認し、初出名は復旧検分初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1888]



### CLIENTID {#c12-i0848}
*分類: 開発リファレンス*  ・  難易度: 上級

「CLIENTID」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1890))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1890]

??? question "確認問題（1問）"
    **問題.** 監査検分の開発リファレンスでメッセージングの運用確認を行います。CLIENTID の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査検分の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査検分の開発リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査検分の確認値として扱う。 ✅
    - D. CLIENTID の属性行を読まず監査検分の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では CLIENTID は「IBM MQ for z/OS で CLIENTID の扱いを記録する監査検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では CLIENTID の表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では CLIENTID の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1890]



### CLIENTRECONNECTOPTIONS {#c12-i0849}
*分類: 開発リファレンス*  ・  難易度: 上級

「CLIENTRECONNECTOPTIONS」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1888))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1888]

??? question "確認問題（1問）"
    **問題.** 変更検分の開発リファレンスに関する CLIENTRECONNECTOPTIONS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更検分の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分の開発リファレンスの証跡として保存して根拠にする。
    - C. CLIENTRECONNECTOPTIONS の変更点を出力本文から切り離して変更検分の開発リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更検分の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では CLIENTRECONNECTOPTIONS は「CLIENTRECONNECTOPTIONS の状態と出力メッセージを結び付ける変更検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では CLIENTRECONNECTOPTIONS の出力行と CSQ9022I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では CLIENTRECONNECTOPTIONS を IBM MQ for z/OS の確認記録に残し、対象名は変更検分対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1888]



### CLIENTRECONNECTTIMEOUT {#c12-i0850}
*分類: 開発リファレンス*  ・  難易度: 上級

「CLIENTRECONNECTTIMEOUT」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1889))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1889]

??? question "確認問題（1問）"
    **問題.** 構文確認の開発リファレンスに関係する CLIENTRECONNECTTIMEOUT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、構文確認の採否を説明欄に結び付ける。 ✅
    - B. CLIENTRECONNECTTIMEOUT の名称と担当者名のみを残して構文確認の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文確認の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文確認の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では CLIENTRECONNECTTIMEOUT は「CLIENTRECONNECTTIMEOUT の用途をメッセージングの表示で確認する構文確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM MQ for z/OS の CLIENTRECONNECTTIMEOUT と CSQ9022I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では CLIENTRECONNECTTIMEOUT を IBM MQ メッセージングで扱う確認対象とし、用語名は構文確認用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1889]



### CLONESUPP {#c12-i0851}
*分類: 開発リファレンス*  ・  難易度: 上級

「CLONESUPP」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1890))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1890]

??? question "確認問題（1問）"
    **問題.** 展開確認の開発リファレンスで CLONESUPP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CLONESUPP の出力を取らず展開確認の開発リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開確認として引き継ぐ。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して展開確認の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では CLONESUPP は「展開確認の開発リファレンスに関係する定義値と表示行を照合する展開確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では CLONESUPP の属性行と CSQ9022I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では CLONESUPP を IBM MQ メッセージングの運用手順で確認し、初出名は展開確認初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1890]



### COMPHDR {#c12-i0852}
*分類: 開発リファレンス*  ・  難易度: 上級

「COMPHDR」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1891))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1891]

??? question "確認問題（1問）"
    **問題.** 上書確認の開発リファレンスでメッセージングの運用確認を行います。COMPHDR の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書確認の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書確認の開発リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書確認の根拠を固定する。 ✅
    - D. COMPHDR の属性行を読まず上書確認の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では COMPHDR は「IBM MQ for z/OS で COMPHDR の扱いを記録する上書確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では COMPHDR の表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では COMPHDR の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1891]



### COMPMSG {#c12-i0853}
*分類: 開発リファレンス*  ・  難易度: 上級

「COMPMSG」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1891))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1891]

??? question "確認問題（1問）"
    **問題.** 出力確認の開発リファレンスに関する COMPMSG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず出力確認の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の開発リファレンスの証跡として保存して根拠にする。
    - C. COMPMSG の変更点を出力本文から切り離して出力確認の開発リファレンスの承認欄のみ残す。
    - D. CSQ9022I を含む表示を保存し、説明欄との差分を出力確認で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では COMPMSG は「COMPMSG の状態と出力メッセージを結び付ける出力確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では COMPMSG の出力行と CSQ9022I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では COMPMSG を IBM MQ for z/OS の確認記録に残し、対象名は出力確認対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1891]



### CONNECTIONNAMELIST {#c12-i0854}
*分類: 開発リファレンス*  ・  難易度: 上級

「CONNECTIONNAMELIST」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1888))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1888]

??? question "確認問題（1問）"
    **問題.** 条件確認の開発リファレンスに関係する CONNECTIONNAMELIST の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、条件確認の証跡として残す。 ✅
    - B. CONNECTIONNAMELIST の名称と担当者名のみを残して条件確認の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件確認の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件確認の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では CONNECTIONNAMELIST は「CONNECTIONNAMELIST の用途をメッセージングの表示で確認する条件確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM MQ for z/OS の CONNECTIONNAMELIST と CSQ9022I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では CONNECTIONNAMELIST を IBM MQ メッセージングで扱う確認対象とし、用語名は条件確認用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1888]



### CONNOPT {#c12-i0855}
*分類: 開発リファレンス*  ・  難易度: 上級

「CONNOPT」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1892))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1892]

??? question "確認問題（1問）"
    **問題.** 区切確認の開発リファレンスで CONNOPT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CONNOPT の出力を取らず区切確認の開発リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切確認の確認記録にまとめる。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して区切確認の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では CONNOPT は「区切確認の開発リファレンスに関係する定義値と表示行を照合する区切確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では CONNOPT の属性行と CSQ9022I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では CONNOPT を IBM MQ メッセージングの運用手順で確認し、初出名は区切確認初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1892]



### CONNTAG {#c12-i0856}
*分類: 開発リファレンス*  ・  難易度: 上級

「CONNTAG」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1893))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1893]

??? question "確認問題（1問）"
    **問題.** 範囲確認の開発リファレンスでメッセージングの運用確認を行います。CONNTAG の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲確認の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲確認の開発リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲確認の根拠にする。 ✅
    - D. CONNTAG の属性行を読まず範囲確認の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では CONNTAG は「IBM MQ for z/OS で CONNTAG の扱いを記録する範囲確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では CONNTAG の表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では CONNTAG の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1893]



### Channel-exit calls and data structures {#c12-i0857}
*分類: 開発リファレンス*  ・  難易度: 上級

Channel-exit calls and data structuresは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 順序検分の開発リファレンスでメッセージングの運用確認を行います。Channel-exit calls and dの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序検分の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序検分の開発リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序検分として引き継ぐ。 ✅
    - D. Channel-exit calls and dの属性行を読まず順序検分の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Channel-exit calls and d は「IBM MQ for z/OS で Channel-exit calls and dの扱いを記録する順序検分項目」と DISPLAY CHANNEL(*) ALL または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Channel-exit calls and dの表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Channel-exit calls and dの使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Character set identifiers for .NET applications {#c12-i0858}
*分類: 開発リファレンス*  ・  難易度: 上級

Character set identifiers for .NET applicationsは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 値域検分の開発リファレンスに関する Character set identifierの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域検分の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分の開発リファレンスの証跡として保存して根拠にする。
    - C. Character set identifierの変更点を出力本文から切り離して値域検分の開発リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域検分の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Character set identifier は「Character set identifierの状態と出力メッセージを結び付ける値域検分項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Character set identifierの出力行と CSQ9022I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Character set identifierを IBM MQ for z/OS の確認記録に残し、対象名は値域検分対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Cluster workload exit call and data structures {#c12-i0859}
*分類: 開発リファレンス*  ・  難易度: 上級

Cluster workload exit call and data structuresは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 呼出確認の開発リファレンスでメッセージングの運用確認を行います。Cluster workload exit caの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出確認の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出確認の開発リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出確認の確認にする。 ✅
    - D. Cluster workload exit caの属性行を読まず呼出確認の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Cluster workload exit ca は「IBM MQ for z/OS で Cluster workload exit caの扱いを記録する呼出確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Cluster workload exit caの表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Cluster workload exit caの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Code examples {#c12-i0860}
*分類: 開発リファレンス*  ・  難易度: 上級

「Code examples」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.8))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.8]

??? question "確認問題（1問）"
    **問題.** 置換確認の開発リファレンスに関する Code examplesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず置換確認の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の開発リファレンスの証跡として保存して根拠にする。
    - C. Code examplesの変更点を出力本文から切り離して置換確認の開発リファレンスの承認欄のみ残す。
    - D. IBM MQ for z/OS の表示形式に沿って根拠行を採り、置換確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Code examples は「Code examplesの状態と出力メッセージを結び付ける置換確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Code examplesの出力行と CSQ9022I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Code examplesを IBM MQ for z/OS の確認記録に残し、対象名は置換確認対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.8]



### Code page conversion {#c12-i0861}
*分類: 開発リファレンス*  ・  難易度: 上級

「Code page conversion」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.926))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.926]

??? question "確認問題（1問）"
    **問題.** 終端確認の開発リファレンスに関係する Code page conversionの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端確認で再確認できる形にする。 ✅
    - B. Code page conversionの名称と担当者名のみを残して終端確認の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端確認の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端確認の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Code page conversion は「Code page conversionの用途をメッセージングの表示で確認する終端確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM MQ for z/OS の Code page conversionと CSQ9022I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Code page conversionを IBM MQ メッセージングで扱う確認対象とし、用語名は終端確認用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.926]



### Coding standards on 64-bit platforms {#c12-i0862}
*分類: 開発リファレンス*  ・  難易度: 上級

Coding standards on 64-bit platformsは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 探索確認の開発リファレンスで Coding standards on 64-bの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Coding standards on 64-bの出力を取らず探索確認の開発リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索確認の確認値として扱う。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索確認の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Coding standards on 64-b は「探索確認の開発リファレンスに関係する定義値と表示行を照合する探索確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Coding standards on 64-bの属性行と CSQ9022I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Coding standards on 64-bを IBM MQ メッセージングの運用手順で確認し、初出名は探索確認初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Constants {#c12-i0863}
*分類: 開発リファレンス*  ・  難易度: 上級

Constantsは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.59] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.59]

??? question "確認問題（1問）"
    **問題.** 優先確認の開発リファレンスに関する Constantsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず優先確認の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の開発リファレンスの証跡として保存して根拠にする。
    - C. Constantsの変更点を出力本文から切り離して優先確認の開発リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と CSQ9022I を読み、優先確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Constants は「Constantsの状態と出力メッセージを結び付ける優先確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Constantsの出力行と CSQ9022I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Constantsを IBM MQ for z/OS の確認記録に残し、対象名は優先確認対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.59]



### Conversion of report messages on IBM i {#c12-i0864}
*分類: 開発リファレンス*  ・  難易度: 上級

Conversion of report messages on IBM iは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 記録確認の開発リファレンスに関係する Conversion of report mesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、記録確認の採否を説明欄に結び付ける。 ✅
    - B. Conversion of report mesの名称と担当者名のみを残して記録確認の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録確認の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録確認の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Conversion of report mes は「Conversion of report mesの用途をメッセージングの表示で確認する記録確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM MQ for z/OS の Conversion of report mesと CSQ9022I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Conversion of report mesを IBM MQ メッセージングで扱う確認対象とし、用語名は記録確認用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Conversion processing on IBM i {#c12-i0865}
*分類: 開発リファレンス*  ・  難易度: 上級

Conversion processing on IBM iは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 比較確認の開発リファレンスで Conversion processing onの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Conversion processing onの出力を取らず比較確認の開発リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較確認として引き継ぐ。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して比較確認の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Conversion processing on は「比較確認の開発リファレンスに関係する定義値と表示行を照合する比較確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Conversion processing onの属性行と CSQ9022I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Conversion processing onを IBM MQ メッセージングの運用手順で確認し、初出名は比較確認初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### DESCRIPTION {#c12-i0866}
*分類: 開発リファレンス*  ・  難易度: 上級

「DESCRIPTION」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1893))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1893]

??? question "確認問題（1問）"
    **問題.** 構文照合の開発リファレンスに関係する DESCRIPTION の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、構文照合の証跡として残す。 ✅
    - B. DESCRIPTION の名称と担当者名のみを残して構文照合の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で構文照合の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず構文照合の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では DESCRIPTION は「DESCRIPTION の用途をメッセージングの表示で確認する構文照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM MQ for z/OS の DESCRIPTION と CSQ9022I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では DESCRIPTION を IBM MQ メッセージングで扱う確認対象とし、用語名は構文照合用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1893]



### DIRECTAUTH {#c12-i0867}
*分類: 開発リファレンス*  ・  難易度: 上級

「DIRECTAUTH」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1894))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1894]

??? question "確認問題（1問）"
    **問題.** 呼出照合の開発リファレンスでメッセージングの運用確認を行います。DIRECTAUTH の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で呼出照合の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず呼出照合の開発リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出照合の根拠にする。 ✅
    - D. DIRECTAUTH の属性行を読まず呼出照合の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では DIRECTAUTH は「IBM MQ for z/OS で DIRECTAUTH の扱いを記録する呼出照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では DIRECTAUTH の表示結果と CSQ9022I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では DIRECTAUTH の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1894]



### Data conversion on IBM i {#c12-i0868}
*分類: 開発リファレンス*  ・  難易度: 上級

Data conversion on IBM iは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 順序確認の開発リファレンスでメッセージングの運用確認を行います。Data conversion on IBM iの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で順序確認の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず順序確認の開発リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序確認の確認にする。 ✅
    - D. Data conversion on IBM iの属性行を読まず順序確認の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Data conversion on IBM i は「IBM MQ for z/OS で Data conversion on IBM iの扱いを記録する順序確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Data conversion on IBM iの表示結果と CSQ9022I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Data conversion on IBM iの使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Data type descriptions on IBM i {#c12-i0869}
*分類: 開発リファレンス*  ・  難易度: 上級

Data type descriptions on IBM iは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 値域確認の開発リファレンスに関する Data type descriptions oの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず値域確認の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の開発リファレンスの証跡として保存して根拠にする。
    - C. Data type descriptions oの変更点を出力本文から切り離して値域確認の開発リファレンスの承認欄のみ残す。
    - D. IBM MQ for z/OS の表示形式に沿って根拠行を採り、値域確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Data type descriptions o は「Data type descriptions oの状態と出力メッセージを結び付ける値域確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Data type descriptions oの出力行と CSQ9022I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Data type descriptions oを IBM MQ for z/OS の確認記録に残し、対象名は値域確認対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Data types used in the MQI {#c12-i0870}
*分類: 開発リファレンス*  ・  難易度: 上級

Data types used in the MQIは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 警告確認の開発リファレンスに関係する Data types used in the M の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告確認で再確認できる形にする。 ✅
    - B. Data types used in the M の名称と担当者名のみを残して警告確認の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で警告確認の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず警告確認の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Data types used in the M は「Data types used in the M の用途をメッセージングの表示で確認する警告確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM MQ for z/OS の Data types used in the M と CSQ9022I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Data types used in the M を IBM MQ メッセージングで扱う確認対象とし、用語名は警告確認用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Data-conversion exit {#c12-i0871}
*分類: 開発リファレンス*  ・  難易度: 上級

Data-conversion exitは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.895] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.895]

??? question "確認問題（1問）"
    **問題.** 復旧確認の開発リファレンスで Data-conversion exitの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Data-conversion exitの出力を取らず復旧確認の開発リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧確認の確認値として扱う。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して復旧確認の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Data-conversion exit は「復旧確認の開発リファレンスに関係する定義値と表示行を照合する復旧確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Data-conversion exitの属性行と CSQ9022I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Data-conversion exitを IBM MQ メッセージングの運用手順で確認し、初出名は復旧確認初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.895]



### Data-conversion exit reference {#c12-i0872}
*分類: 開発リファレンス*  ・  難易度: 上級

Data-conversion exit referenceは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1445] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1445]

??? question "確認問題（1問）"
    **問題.** 監査確認の開発リファレンスでメッセージングの運用確認を行います。Data-conversion exit refの根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で監査確認の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず監査確認の開発リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査確認の根拠を固定する。 ✅
    - D. Data-conversion exit refの属性行を読まず監査確認の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Data-conversion exit ref は「IBM MQ for z/OS で Data-conversion exit refの扱いを記録する監査確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Data-conversion exit refの表示結果と CSQ9022I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Data-conversion exit refの使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1445]



### Dependencies between properties of IBM MQ classes for JMS objects {#c12-i0873}
*分類: 開発リファレンス*  ・  難易度: 上級

Dependencies between properties of IBM MQ classes for JMS objectsは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 変更確認の開発リファレンスに関する Dependencies between proの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず変更確認の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の開発リファレンスの証跡として保存して根拠にする。
    - C. Dependencies between proの変更点を出力本文から切り離して変更確認の開発リファレンスの承認欄のみ残す。
    - D. CSQ9022I を含む表示を保存し、説明欄との差分を変更確認で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Dependencies between pro は「Dependencies between proの状態と出力メッセージを結び付ける変更確認項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Dependencies between proの出力行と CSQ9022I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Dependencies between proを IBM MQ for z/OS の確認記録に残し、対象名は変更確認対象です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### Developing applications reference {#c12-i0874}
*分類: 開発リファレンス*  ・  難易度: 上級

Developing applications referenceは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.7] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.7]

??? question "確認問題（1問）"
    **問題.** 展開照合の開発リファレンスで Developing applicationsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Developing applicationsの出力を取らず展開照合の開発リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開照合の確認記録にまとめる。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して展開照合の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では Developing applications は「展開照合の開発リファレンスに関係する定義値と表示行を照合する展開照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では Developing applicationsの属性行と CSQ9022I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では Developing applicationsを IBM MQ メッセージングの運用手順で確認し、初出名は展開照合初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.7]



### ENCODING {#c12-i0875}
*分類: 開発リファレンス*  ・  難易度: 上級

「ENCODING」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1894))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1894]

??? question "確認問題（1問）"
    **問題.** 置換照合の開発リファレンスに関する ENCODING の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果を残さず置換照合の開発リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の開発リファレンスの証跡として保存して根拠にする。
    - C. ENCODING の変更点を出力本文から切り離して置換照合の開発リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と CSQ9022I を読み、置換照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では ENCODING は「ENCODING の状態と出力メッセージを結び付ける置換照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では ENCODING の出力行と CSQ9022I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では ENCODING を IBM MQ for z/OS の確認記録に残し、対象名は置換照合対象です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1894]



### EXPIRY {#c12-i0876}
*分類: 開発リファレンス*  ・  難易度: 上級

「EXPIRY」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1895))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1895]

??? question "確認問題（1問）"
    **問題.** 探索照合の開発リファレンスで EXPIRY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EXPIRY の出力を取らず探索照合の開発リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索照合として引き継ぐ。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して探索照合の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では EXPIRY は「探索照合の開発リファレンスに関係する定義値と表示行を照合する探索照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では EXPIRY の属性行と CSQ9022I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では EXPIRY を IBM MQ メッセージングの運用手順で確認し、初出名は探索照合初出です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1895]



### Examples of using fteCreateTransfer to start programs {#c12-i0877}
*分類: 開発リファレンス*  ・  難易度: 上級

Examples of using fteCreateTransfer to start programsは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 終端照合の開発リファレンスに関係する Examples of using fteCreの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL で得た表示本文を使い、終端照合の採否を説明欄に結び付ける。 ✅
    - B. Examples of using fteCreの名称と担当者名のみを残して終端照合の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で終端照合の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず終端照合の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では Examples of using fteCre は「Examples of using fteCreの用途をメッセージングの表示で確認する終端照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM MQ for z/OS の Examples of using fteCreと CSQ9022I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では Examples of using fteCreを IBM MQ メッセージングで扱う確認対象とし、用語名は終端照合用語です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### FAILIFQUIESCE {#c12-i0878}
*分類: 開発リファレンス*  ・  難易度: 上級

「FAILIFQUIESCE」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1895))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1895]

??? question "確認問題（1問）"
    **問題.** 上書照合の開発リファレンスでメッセージングの運用確認を行います。FAILIFQUIESCE の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で上書照合の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず上書照合の開発リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書照合の確認にする。 ✅
    - D. FAILIFQUIESCE の属性行を読まず上書照合の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では FAILIFQUIESCE は「IBM MQ for z/OS で FAILIFQUIESCE の扱いを記録する上書照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では FAILIFQUIESCE の表示結果と CSQ9022I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では FAILIFQUIESCE の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1895]



### Function calls {#c12-i0879}
*分類: 開発リファレンス*  ・  難易度: 上級

Function callsは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。MQ 9.3 開発リファレンス [mq93.refdev.pdf p.618] を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.618]

??? question "確認問題（1問）"
    **問題.** 条件照合の開発リファレンスに関係する Function callsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件照合で再確認できる形にする。 ✅
    - B. Function callsの名称と担当者名のみを残して条件照合の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で条件照合の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず条件照合の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では Function calls は「Function callsの用途をメッセージングの表示で確認する条件照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では IBM MQ for z/OS の Function callsと CSQ9022I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では Function callsを IBM MQ メッセージングで扱う確認対象とし、用語名は条件照合用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.618]



### Function calls on IBM i {#c12-i0880}
*分類: 開発リファレンス*  ・  難易度: 上級

Function calls on IBM iは、IBM MQ メッセージングの開発リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM MQ メッセージング の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference

??? question "確認問題（1問）"
    **問題.** 区切照合の開発リファレンスで Function calls on IBM iの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Function calls on IBM iの出力を取らず区切照合の開発リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切照合の確認値として扱う。 ✅
    - C. DISPLAY QLOCAL(OSKBQUEUE) ALL を省略して区切照合の開発リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の開発リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では Function calls on IBM i は「区切照合の開発リファレンスに関係する定義値と表示行を照合する区切照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では Function calls on IBM iの属性行と CSQ9022I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では Function calls on IBM iを IBM MQ メッセージングの運用手順で確認し、初出名は区切照合初出です。

    **出典:** mq93.administer / mq93.configure / mq93.refadmin / mq93.reference



### HOSTNAME {#c12-i0881}
*分類: 開発リファレンス*  ・  難易度: 上級

「HOSTNAME」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1896))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1896]

??? question "確認問題（1問）"
    **問題.** 範囲照合の開発リファレンスでメッセージングの運用確認を行います。HOSTNAME の根拠にできる作業はどれですか。

    - A. IBM MQ for z/OS と無関係な一覧で範囲照合の開発リファレンスを確認した扱いにする。
    - B. CSQ9022I の有無を確認せず範囲照合の開発リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲照合の根拠を固定する。 ✅
    - D. HOSTNAME の属性行を読まず範囲照合の開発リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では HOSTNAME は「IBM MQ for z/OS で HOSTNAME の扱いを記録する範囲照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では HOSTNAME の表示結果と CSQ9022I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では HOSTNAME の使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1896]



### IBM MQ C++ classes {#c12-i0882}
*分類: 開発リファレンス*  ・  難易度: 上級

「IBM MQ C++ classes」 (開発リファレンス) — 該当 Lv3 ページ周辺のチャンク取得失敗。要再調査 (参考 summary: (mq93.refdev.pdf p.1764))

**出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1764]

??? question "確認問題（1問）"
    **問題.** 記録照合の開発リファレンスに関係する IBM MQ C++ classesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DISPLAY QLOCAL(OSKBQUEUE) ALL の結果から対象行を抜き出し、記録照合の証跡として残す。 ✅
    - B. IBM MQ C++ classesの名称と担当者名のみを残して記録照合の開発リファレンスの表示本文を確認対象に含めない。
    - C. メッセージング以外の画面で記録照合の開発リファレンスを確認し同じ証跡として扱ったことにする。
    - D. CSQ9022I の有無を見ず記録照合の開発リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では IBM MQ C++ classes は「IBM MQ C++ classesの用途をメッセージングの表示で確認する記録照合項目」と DISPLAY QLOCAL(OSKB.QUEUE) ALL または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では IBM MQ for z/OS の IBM MQ C++ classesと CSQ9022I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では IBM MQ C++ classesを IBM MQ メッセージングで扱う確認対象とし、用語名は記録照合用語です。

    **出典:** MQ 9.3 開発リファレンス [mq93.refdev.pdf p.1764]


