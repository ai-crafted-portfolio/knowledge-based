---
search:
  exclude: true
---

# RACF USER/GROUP/DATASET — 詳細 (7/7)

[← RACF USER/GROUP/DATASET の概要へ戻る](index.md)


## その他

### その他（特定項目に紐づかないQA・手順） {#c27-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（21問）"
    **問題.** 置換確認の| |に関する AUDIT(SUCCESS|FAILURES|A の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTDSD DATASET('OSKBDATA') ALL の結果を残さず置換確認の| |の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の| |の証跡として保存して根拠にする。
    - C. AUDIT(SUCCESS|FAILURES|A の変更点を出力本文から切り離して置換確認の| |の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認の| |において選択記号 D を採用し、識別名は置換確認です。置換確認の| |において AUDIT(SUCCESS|FAILURES|A は説明欄の「AUDIT(SUCCESS|FAILURES|A の状態と出力メッセージを結び付ける置換確認項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の| |に関する記録は、AUDIT(SUCCESS|FAILURES|A の出力行と ICH35001I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の| |は戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため置換確認ではありません。 B: 置換確認の| |は別カテゴリの確認を流用しており、AUDIT(SUCCESS|FAILURES|A の根拠にならないため置換確認ではありません。 C: 置換確認の| |は名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の| |は対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の| |で記録する AUDIT(SUCCESS|FAILURES|A は RACF の確認記録に残す対象名であり、用語名は置換確認です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 条件確認の| などに関係する ID(uid|grp,など)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件確認の根拠にする。 ✅
    - B. ID(uid|grp,など)の名称と担当者名のみを残して条件確認の| などの表示本文を確認対象に含めない。
    - C. セキュリティ管理以外の画面で条件確認の| などを確認し同じ証跡として扱ったことにする。
    - D. ICH35001I の有無を見ず条件確認の| などの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認の| などにおいて選択記号 A を採用し、識別名は条件確認です。条件確認の| などにおいて ID(uid|grp,など) は説明欄の「ID(uid|grp,など)の用途をセキュリティ管理の表示で確認する条件確認項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の| などに関連して、RACF では ID(uid|grp,など)の表示属性と ICH35001I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の| などは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の| などは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の| などは別カテゴリの確認を流用しており、ID(uid|grp,など)の根拠にならないため条件確認ではありません。 D: 条件確認の| などは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため条件確認ではありません。条件確認の| などで使う ID(uid|grp,など)という用語は RACF USER/GROUP/DATASET で扱う確認対象であり、用語名は条件確認です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 終端照合の|に関係する WHEN(DAYS(WEEKDAYS|ANYDA の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端照合の確認にする。 ✅
    - B. WHEN(DAYS(WEEKDAYS|ANYDA の名称と担当者名のみを残して終端照合の|の表示本文を確認対象に含めない。
    - C. セキュリティ管理以外の画面で終端照合の|を確認し同じ証跡として扱ったことにする。
    - D. ICH35001I の有無を見ず終端照合の|の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合の|において選択記号 A を採用し、識別名は終端照合です。終端照合の|において WHEN(DAYS(WEEKDAYS|ANYDA は説明欄の「WHEN(DAYS(WEEKDAYS|ANYDA の用途をセキュリティ管理の表示で確認する終端照合項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の|に関連して、RACF では WHEN(DAYS(WEEKDAYS|ANYDA の表示属性と ICH35001I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の|は対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の|は名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の|は別カテゴリの確認を流用しており、WHEN(DAYS(WEEKDAYS|ANYDA の根拠にならないため終端照合ではありません。 D: 終端照合の|は戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため終端照合ではありません。終端照合の|で使う WHEN(DAYS(WEEKDAYS|ANYDA という用語は RACF USER/GROUP/DATASET で扱う確認対象であり、用語名は終端照合です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 上書検査のセグメントとはでセキュリティ管理の運用確認を行います。ADDUSER DFP セグメントとはの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で上書検査のセグメントとはを確認した扱いにする。
    - B. ICH35001I の有無を確認せず上書検査のセグメントとはを正常終了として記録する。
    - C. LISTDSD DATASET('OSKBDATA') ALL の結果から対象行を抜き出し、上書検査の証跡として残す。 ✅
    - D. ADDUSER DFP セグメントとはの属性行を読まず上書検査のセグメントとはの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書検査のセグメントとはにおいて選択記号 C を採用し、識別名は上書検査です。上書検査のセグメントとはにおいて ADDUSER DFP セグメントとは は説明欄の「RACF で ADDUSER DFP セグメントとはの扱いを記録する上書検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は上書検査です。上書検査のセグメントとはを受け取る担当者は、ADDUSER DFP セグメントとはの表示結果と ICH35001I を同じ確認単位として扱い、背景名は上書検査です。不適切な選択肢を整理します。 A: 上書検査のセグメントとはは別カテゴリの確認を流用しており、ADDUSER DFP セグメントとはの根拠にならないため上書検査ではありません。 B: 上書検査のセグメントとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため上書検査ではありません。 C: 上書検査のセグメントとはは対象出力と項目説明を結び、根拠を残すので上書検査です。 D: 上書検査のセグメントとはは名称や説明のみに寄り、状態を示す出力本文が不足するため上書検査ではありません。上書検査のセグメントとはが示す ADDUSER DFP セグメントとはは出典欄の資料で使い方を追跡できる項目であり、用語名は上書検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **問題.** 範囲検査のセグメントとはでセキュリティ管理の運用確認を行います。ADDUSER DCE セグメントとはの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で範囲検査のセグメントとはを確認した扱いにする。
    - B. ICH35001I の有無を確認せず範囲検査のセグメントとはを正常終了として記録する。
    - C. LISTDSD DATASET('OSKBDATA') ALL で得た表示本文を使い、範囲検査の採否を説明欄に結び付ける。 ✅
    - D. ADDUSER DCE セグメントとはの属性行を読まず範囲検査のセグメントとはの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 範囲検査のセグメントとはにおいて選択記号 C を採用し、識別名は範囲検査です。範囲検査のセグメントとはにおいて ADDUSER DCE セグメントとは は説明欄の「RACF で ADDUSER DCE セグメントとはの扱いを記録する範囲検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は範囲検査です。範囲検査のセグメントとはを受け取る担当者は、ADDUSER DCE セグメントとはの表示結果と ICH35001I を同じ確認単位として扱い、背景名は範囲検査です。不適切な選択肢を整理します。 A: 範囲検査のセグメントとはは別カテゴリの確認を流用しており、ADDUSER DCE セグメントとはの根拠にならないため範囲検査ではありません。 B: 範囲検査のセグメントとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため範囲検査ではありません。 C: 範囲検査のセグメントとはは対象出力と項目説明を結び、根拠を残すので範囲検査です。 D: 範囲検査のセグメントとはは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲検査ではありません。範囲検査のセグメントとはが示す ADDUSER DCE セグメントとはは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **問題.** 優先検査のとはに関する ALTUSER とはの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTDSD DATASET('OSKBDATA') ALL の結果を残さず優先検査のとはの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のとはの証跡として保存して根拠にする。
    - C. ALTUSER とはの変更点を出力本文から切り離して優先検査のとはの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先検査として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 優先検査のとはにおいて選択記号 D を採用し、識別名は優先検査です。優先検査のとはにおいて ALTUSER とは は説明欄の「ALTUSER とはの状態と出力メッセージを結び付ける優先検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査のとはに関する記録は、ALTUSER とはの出力行と ICH35001I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため優先検査ではありません。 B: 優先検査のとはは別カテゴリの確認を流用しており、ALTUSER とはの根拠にならないため優先検査ではありません。 C: 優先検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査のとはは対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査のとはで記録する ALTUSER とはは RACF の確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 記録検査のとはに関係する DELUSER とはの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録検査の確認にする。 ✅
    - B. DELUSER とはの名称と担当者名のみを残して記録検査のとはの表示本文を確認対象に含めない。
    - C. セキュリティ管理以外の画面で記録検査のとはを確認し同じ証跡として扱ったことにする。
    - D. ICH35001I の有無を見ず記録検査のとはの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 記録検査のとはにおいて選択記号 A を採用し、識別名は記録検査です。記録検査のとはにおいて DELUSER とは は説明欄の「DELUSER とはの用途をセキュリティ管理の表示で確認する記録検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は記録検査です。記録検査のとはに関連して、RACF では DELUSER とはの表示属性と ICH35001I を同じ証跡に残し、背景名は記録検査です。他の選択肢を確認します。 A: 記録検査のとはは対象出力と項目説明を結び、根拠を残すので記録検査です。 B: 記録検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため記録検査ではありません。 C: 記録検査のとはは別カテゴリの確認を流用しており、DELUSER とはの根拠にならないため記録検査ではありません。 D: 記録検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため記録検査ではありません。記録検査のとはで使う DELUSER とはという用語は RACF USER/GROUP/DATASET で扱う確認対象であり、用語名は記録検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / SA23-2290 z / OS Security Server RACF General User's Guide

    ---

    **問題.** 比較検査のとはで LISTUSER とはの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LISTUSER とはの出力を取らず比較検査のとはの説明文と承認印のみを残す。
    - B. RACF の表示形式に沿って根拠行を採り、比較検査の点検結果を残す。 ✅
    - C. LISTDSD DATASET('OSKBDATA') ALL を省略して比較検査のとはの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のとはへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 比較検査のとはにおいて選択記号 B を採用し、識別名は比較検査です。比較検査のとはにおいて LISTUSER とは は説明欄の「比較検査のとはに関係する定義値と表示行を照合する比較検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は比較検査です。比較検査のとはの証跡を読む担当者は、LISTUSER とはの属性行と ICH35001I を合わせて追跡し、背景名は比較検査です。誤答側の問題点を分けます。 A: 比較検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため比較検査ではありません。 B: 比較検査のとはは対象出力と項目説明を結び、根拠を残すので比較検査です。 C: 比較検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため比較検査ではありません。 D: 比較検査のとはは別カテゴリの確認を流用しており、LISTUSER とはの根拠にならないため比較検査ではありません。比較検査のとはに出る LISTUSER とはは RACF USER/GROUP/DATASET の運用手順で意味を確認する対象であり、用語名は比較検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / SA23-2290 z / OS Security Server RACF General User's Guide

    ---

    **問題.** 順序検査のコマンドとはでセキュリティ管理の運用確認を行います。PASSWORD コマンドとはの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で順序検査のコマンドとはを確認した扱いにする。
    - B. ICH35001I の有無を確認せず順序検査のコマンドとはを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序検査で再確認できる形にする。 ✅
    - D. PASSWORD コマンドとはの属性行を読まず順序検査のコマンドとはの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 順序検査のコマンドとはにおいて選択記号 C を採用し、識別名は順序検査です。順序検査のコマンドとはにおいて PASSWORD コマンドとは は説明欄の「RACF で PASSWORD コマンドとはの扱いを記録する順序検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は順序検査です。順序検査のコマンドとはを受け取る担当者は、PASSWORD コマンドとはの表示結果と ICH35001I を同じ確認単位として扱い、背景名は順序検査です。不適切な選択肢を整理します。 A: 順序検査のコマンドとはは別カテゴリの確認を流用しており、PASSWORD コマンドとはの根拠にならないため順序検査ではありません。 B: 順序検査のコマンドとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため順序検査ではありません。 C: 順序検査のコマンドとはは対象出力と項目説明を結び、根拠を残すので順序検査です。 D: 順序検査のコマンドとはは名称や説明のみに寄り、状態を示す出力本文が不足するため順序検査ではありません。順序検査のコマンドとはが示す PASSWORD コマンドとはは出典欄の資料で使い方を追跡できる項目であり、用語名は順序検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / SA23-2290 z / OS Security Server RACF General User's Guide

    ---

    **問題.** 値域検査のとはに関する ADDGROUP とはの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTDSD DATASET('OSKBDATA') ALL の結果を残さず値域検査のとはの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のとはの証跡として保存して根拠にする。
    - C. ADDGROUP とはの変更点を出力本文から切り離して値域検査のとはの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域検査の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 値域検査のとはにおいて選択記号 D を採用し、識別名は値域検査です。値域検査のとはにおいて ADDGROUP とは は説明欄の「ADDGROUP とはの状態と出力メッセージを結び付ける値域検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査のとはに関する記録は、ADDGROUP とはの出力行と ICH35001I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため値域検査ではありません。 B: 値域検査のとはは別カテゴリの確認を流用しており、ADDGROUP とはの根拠にならないため値域検査ではありません。 C: 値域検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査のとはは対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査のとはで記録する ADDGROUP とはは RACF の確認記録に残す対象名であり、用語名は値域検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS UNIX System Services User's Guide (zOS31_bpxb200.pdf)

    ---

    **問題.** 警告検査のとはに関係する ALTGROUP とはの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告検査の根拠を固定する。 ✅
    - B. ALTGROUP とはの名称と担当者名のみを残して警告検査のとはの表示本文を確認対象に含めない。
    - C. セキュリティ管理以外の画面で警告検査のとはを確認し同じ証跡として扱ったことにする。
    - D. ICH35001I の有無を見ず警告検査のとはの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 警告検査のとはにおいて選択記号 A を採用し、識別名は警告検査です。警告検査のとはにおいて ALTGROUP とは は説明欄の「ALTGROUP とはの用途をセキュリティ管理の表示で確認する警告検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査のとはに関連して、RACF では ALTGROUP とはの表示属性と ICH35001I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査のとはは対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査のとはは別カテゴリの確認を流用しており、ALTGROUP とはの根拠にならないため警告検査ではありません。 D: 警告検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため警告検査ではありません。警告検査のとはで使う ALTGROUP とはという用語は RACF USER/GROUP/DATASET で扱う確認対象であり、用語名は警告検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 復旧検査のとはで DELGROUP とはの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DELGROUP とはの出力を取らず復旧検査のとはの説明文と承認印のみを残す。
    - B. ICH35001I を含む表示を保存し、説明欄との差分を復旧検査で確認する。 ✅
    - C. LISTDSD DATASET('OSKBDATA') ALL を省略して復旧検査のとはの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のとはへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧検査のとはにおいて選択記号 B を採用し、識別名は復旧検査です。復旧検査のとはにおいて DELGROUP とは は説明欄の「復旧検査のとはに関係する定義値と表示行を照合する復旧検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は復旧検査です。復旧検査のとはの証跡を読む担当者は、DELGROUP とはの属性行と ICH35001I を合わせて追跡し、背景名は復旧検査です。誤答側の問題点を分けます。 A: 復旧検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧検査ではありません。 B: 復旧検査のとはは対象出力と項目説明を結び、根拠を残すので復旧検査です。 C: 復旧検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため復旧検査ではありません。 D: 復旧検査のとはは別カテゴリの確認を流用しており、DELGROUP とはの根拠にならないため復旧検査ではありません。復旧検査のとはに出る DELGROUP とはは RACF USER/GROUP/DATASET の運用手順で意味を確認する対象であり、用語名は復旧検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 監査検査のとはでセキュリティ管理の運用確認を行います。LISTGRP とはの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で監査検査のとはを確認した扱いにする。
    - B. ICH35001I の有無を確認せず監査検査のとはを正常終了として記録する。
    - C. LISTDSD DATASET('OSKBDATA') ALL の結果から対象行を抜き出し、監査検査の証跡として残す。 ✅
    - D. LISTGRP とはの属性行を読まず監査検査のとはの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 監査検査のとはにおいて選択記号 C を採用し、識別名は監査検査です。監査検査のとはにおいて LISTGRP とは は説明欄の「RACF で LISTGRP とはの扱いを記録する監査検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は監査検査です。監査検査のとはを受け取る担当者は、LISTGRP とはの表示結果と ICH35001I を同じ確認単位として扱い、背景名は監査検査です。不適切な選択肢を整理します。 A: 監査検査のとはは別カテゴリの確認を流用しており、LISTGRP とはの根拠にならないため監査検査ではありません。 B: 監査検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため監査検査ではありません。 C: 監査検査のとはは対象出力と項目説明を結び、根拠を残すので監査検査です。 D: 監査検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため監査検査ではありません。監査検査のとはが示す LISTGRP とはは出典欄の資料で使い方を追跡できる項目であり、用語名は監査検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 変更検査のとはに関する CONNECT とはの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTDSD DATASET('OSKBDATA') ALL の結果を残さず変更検査のとはの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のとはの証跡として保存して根拠にする。
    - C. CONNECT とはの変更点を出力本文から切り離して変更検査のとはの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 変更検査のとはにおいて選択記号 D を採用し、識別名は変更検査です。変更検査のとはにおいて CONNECT とは は説明欄の「CONNECT とはの状態と出力メッセージを結び付ける変更検査項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査のとはに関する記録は、CONNECT とはの出力行と ICH35001I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため変更検査ではありません。 B: 変更検査のとはは別カテゴリの確認を流用しており、CONNECT とはの根拠にならないため変更検査ではありません。 C: 変更検査のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査のとはは対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査のとはで記録する CONNECT とはは RACF の確認記録に残す対象名であり、用語名は変更検査です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 構文判定のとはに関係する REMOVE とはの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文判定の根拠にする。 ✅
    - B. REMOVE とはの名称と担当者名のみを残して構文判定のとはの表示本文を確認対象に含めない。
    - C. セキュリティ管理以外の画面で構文判定のとはを確認し同じ証跡として扱ったことにする。
    - D. ICH35001I の有無を見ず構文判定のとはの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 構文判定のとはにおいて選択記号 A を採用し、識別名は構文判定です。構文判定のとはにおいて REMOVE とは は説明欄の「REMOVE とはの用途をセキュリティ管理の表示で確認する構文判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は構文判定です。構文判定のとはに関連して、RACF では REMOVE とはの表示属性と ICH35001I を同じ証跡に残し、背景名は構文判定です。他の選択肢を確認します。 A: 構文判定のとはは対象出力と項目説明を結び、根拠を残すので構文判定です。 B: 構文判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため構文判定ではありません。 C: 構文判定のとはは別カテゴリの確認を流用しており、REMOVE とはの根拠にならないため構文判定ではありません。 D: 構文判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため構文判定ではありません。構文判定のとはで使う REMOVE とはという用語は RACF USER/GROUP/DATASET で扱う確認対象であり、用語名は構文判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 展開判定のとはで ADDSD とはの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ADDSD とはの出力を取らず展開判定のとはの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と ICH35001I を読み、展開判定の結果として保存する。 ✅
    - C. LISTDSD DATASET('OSKBDATA') ALL を省略して展開判定のとはの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のとはへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 展開判定のとはにおいて選択記号 B を採用し、識別名は展開判定です。展開判定のとはにおいて ADDSD とは は説明欄の「展開判定のとはに関係する定義値と表示行を照合する展開判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は展開判定です。展開判定のとはの証跡を読む担当者は、ADDSD とはの属性行と ICH35001I を合わせて追跡し、背景名は展開判定です。誤答側の問題点を分けます。 A: 展開判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため展開判定ではありません。 B: 展開判定のとはは対象出力と項目説明を結び、根拠を残すので展開判定です。 C: 展開判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため展開判定ではありません。 D: 展開判定のとはは別カテゴリの確認を流用しており、ADDSD とはの根拠にならないため展開判定ではありません。展開判定のとはに出る ADDSD とはは RACF USER/GROUP/DATASET の運用手順で意味を確認する対象であり、用語名は展開判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 呼出判定のとはでセキュリティ管理の運用確認を行います。ALTDSD とはの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で呼出判定のとはを確認した扱いにする。
    - B. ICH35001I の有無を確認せず呼出判定のとはを正常終了として記録する。
    - C. LISTDSD DATASET('OSKBDATA') ALL で得た表示本文を使い、呼出判定の採否を説明欄に結び付ける。 ✅
    - D. ALTDSD とはの属性行を読まず呼出判定のとはの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 呼出判定のとはにおいて選択記号 C を採用し、識別名は呼出判定です。呼出判定のとはにおいて ALTDSD とは は説明欄の「RACF で ALTDSD とはの扱いを記録する呼出判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は呼出判定です。呼出判定のとはを受け取る担当者は、ALTDSD とはの表示結果と ICH35001I を同じ確認単位として扱い、背景名は呼出判定です。不適切な選択肢を整理します。 A: 呼出判定のとはは別カテゴリの確認を流用しており、ALTDSD とはの根拠にならないため呼出判定ではありません。 B: 呼出判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため呼出判定ではありません。 C: 呼出判定のとはは対象出力と項目説明を結び、根拠を残すので呼出判定です。 D: 呼出判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出判定ではありません。呼出判定のとはが示す ALTDSD とはは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 置換判定のとはに関する DELDSD とはの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTDSD DATASET('OSKBDATA') ALL の結果を残さず置換判定のとはの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のとはの証跡として保存して根拠にする。
    - C. DELDSD とはの変更点を出力本文から切り離して置換判定のとはの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換判定として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換判定のとはにおいて選択記号 D を採用し、識別名は置換判定です。置換判定のとはにおいて DELDSD とは は説明欄の「DELDSD とはの状態と出力メッセージを結び付ける置換判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は置換判定です。置換判定のとはに関する記録は、DELDSD とはの出力行と ICH35001I を一緒に保存し、背景名は置換判定です。選択肢ごとの違いを示します。 A: 置換判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため置換判定ではありません。 B: 置換判定のとはは別カテゴリの確認を流用しており、DELDSD とはの根拠にならないため置換判定ではありません。 C: 置換判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため置換判定ではありません。 D: 置換判定のとはは対象出力と項目説明を結び、根拠を残すので置換判定です。置換判定のとはで記録する DELDSD とはは RACF の確認記録に残す対象名であり、用語名は置換判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 終端判定のとはに関係する LISTDSD とはの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端判定の確認にする。 ✅
    - B. LISTDSD とはの名称と担当者名のみを残して終端判定のとはの表示本文を確認対象に含めない。
    - C. セキュリティ管理以外の画面で終端判定のとはを確認し同じ証跡として扱ったことにする。
    - D. ICH35001I の有無を見ず終端判定のとはの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 終端判定のとはにおいて選択記号 A を採用し、識別名は終端判定です。終端判定のとはにおいて LISTDSD とは は説明欄の「LISTDSD とはの用途をセキュリティ管理の表示で確認する終端判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は終端判定です。終端判定のとはに関連して、RACF では LISTDSD とはの表示属性と ICH35001I を同じ証跡に残し、背景名は終端判定です。他の選択肢を確認します。 A: 終端判定のとはは対象出力と項目説明を結び、根拠を残すので終端判定です。 B: 終端判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため終端判定ではありません。 C: 終端判定のとはは別カテゴリの確認を流用しており、LISTDSD とはの根拠にならないため終端判定ではありません。 D: 終端判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため終端判定ではありません。終端判定のとはで使う LISTDSD とはという用語は RACF USER/GROUP/DATASET で扱う確認対象であり、用語名は終端判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 探索判定のとはで PERMIT とはの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PERMIT とはの出力を取らず探索判定のとはの説明文と承認印のみを残す。
    - B. RACF の表示形式に沿って根拠行を採り、探索判定の点検結果を残す。 ✅
    - C. LISTDSD DATASET('OSKBDATA') ALL を省略して探索判定のとはの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定のとはへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 探索判定のとはにおいて選択記号 B を採用し、識別名は探索判定です。探索判定のとはにおいて PERMIT とは は説明欄の「探索判定のとはに関係する定義値と表示行を照合する探索判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は探索判定です。探索判定のとはの証跡を読む担当者は、PERMIT とはの属性行と ICH35001I を合わせて追跡し、背景名は探索判定です。誤答側の問題点を分けます。 A: 探索判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため探索判定ではありません。 B: 探索判定のとはは対象出力と項目説明を結び、根拠を残すので探索判定です。 C: 探索判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため探索判定ではありません。 D: 探索判定のとはは別カテゴリの確認を流用しており、PERMIT とはの根拠にならないため探索判定ではありません。探索判定のとはに出る PERMIT とはは RACF USER/GROUP/DATASET の運用手順で意味を確認する対象であり、用語名は探索判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **問題.** 上書判定のとはでセキュリティ管理の運用確認を行います。SEARCH とはの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で上書判定のとはを確認した扱いにする。
    - B. ICH35001I の有無を確認せず上書判定のとはを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書判定で再確認できる形にする。 ✅
    - D. SEARCH とはの属性行を読まず上書判定のとはの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書判定のとはにおいて選択記号 C を採用し、識別名は上書判定です。上書判定のとはにおいて SEARCH とは は説明欄の「RACF で SEARCH とはの扱いを記録する上書判定項目」と LISTDSD DATASET('OSKB.DATA') ALL または該当パネルの出力を照合する対象で、答え名は上書判定です。上書判定のとはを受け取る担当者は、SEARCH とはの表示結果と ICH35001I を同じ確認単位として扱い、背景名は上書判定です。不適切な選択肢を整理します。 A: 上書判定のとはは別カテゴリの確認を流用しており、SEARCH とはの根拠にならないため上書判定ではありません。 B: 上書判定のとはは戻り値や記録番号に寄り、ICH35001I や属性表示を落とすため上書判定ではありません。 C: 上書判定のとはは対象出力と項目説明を結び、根拠を残すので上書判定です。 D: 上書判定のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため上書判定ではありません。上書判定のとはが示す SEARCH とはは出典欄の資料で使い方を追跡できる項目であり、用語名は上書判定です。

    **出典:** SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide


??? note "検証手順（16件）"
    **CICS(OPCLASS(n,など))**

    - 検証目的: 条件検査のなどについて、CICS オペレータのクラス番号は CICS(OPCLASS) で指定します。OPCLASS の値は ADDUSER の CICS セグメントに入り、BMS メッセージの配に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、条件検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にCICS(OPCLASS(n,など)を指定し、OSKB010069の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CICS(OPCLASS(n,など)
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CICS(OPCLASS(n,など)
    CASE OSKB010069
    SOURCE RACF
    ```

    CICS(OPCLASS(n,など)とOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB010069を同じ出力で読み、条件検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB010069 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I CICS(OPCLASS(n,など)) INFORMATION LISTED
    ```

    ICH35001IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の CICS(OPCLASS(n,など) と OSKB010069 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB010069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **KERB(ENCRYPT(など))**

    - 検証目的: 比較判定のなどについて、認証連携属性の説明として、KERB(ENCRYPT) は ADDUSER の該当セグメントで その利用者の Kerberos 鍵で使える暗号方式を指定します。環境が許す方式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、比較判定のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にKERB(ENCRYPT(など))を指定し、OSKB010094の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND KERB(ENCRYPT(など))
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM KERB(ENCRYPT(など))
    CASE OSKB010094
    SOURCE RACF
    ```

    KERB(ENCRYPT(など))とOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB010094を同じ出力で読み、比較判定のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB010094 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I KERB(ENCRYPT(など)) INFORMATION LISTED
    ```

    ICH35001IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の KERB(ENCRYPT(など)) と OSKB010094 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB010094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **NETVIEW(CTL(GLOBAL|GENERAL|SPECIFI**

    - 検証目的: 構文整理の|について、検査種別は、ADDUSER の NETVIEW(CTL) で NetView オペレータに設定します。span を使う時やクロスドメインログオンを行う時のセキュリティ検査種に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010101の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、構文整理の|の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNETVIEW(CTL(GLOBALを指定し、OSKB010101の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NETVIEW(CTL(GLOBAL
    CASE OSKB010101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NETVIEW(CTL(GLOBAL
    CASE OSKB010101
    SOURCE RACF
    ```

    NETVIEW(CTL(GLOBALとOSKB010101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB010101を同じ出力で読み、構文整理の|の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB010101
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB010101 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I NETVIEW(CTL(GLOBAL|GENER INFORMATION LISTED
    ```

    ICH35001IとOSKB010101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の NETVIEW(CTL(GLOBAL と OSKB010101 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB010101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **NETVIEW(OPCLASS(n,など))**

    - 検証目的: 呼出整理のなどについて、範囲クラスは、ADDUSER の NETVIEW(OPCLASS) で NetView オペレータに割り当てます。操作範囲クラスの説明として、CICS にも OPCLASSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010103の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、呼出整理のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNETVIEW(OPCLASS(n,を指定し、OSKB010103の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NETVIEW(OPCLASS(n,
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NETVIEW(OPCLASS(n,
    CASE OSKB010103
    SOURCE RACF
    ```

    NETVIEW(OPCLASS(n,とOSKB010103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB010103を同じ出力で読み、呼出整理のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB010103 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I NETVIEW(OPCLASS(n,など)) INFORMATION LISTED
    ```

    ICH35001IとOSKB010103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の NETVIEW(OPCLASS(n, と OSKB010103 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB010103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **NETVIEW(DOMAINS(d,など))**

    - 検証目的: 置換整理のなどについて、ドメイン一覧は、ADDUSER の NETVIEW(DOMAINS) で NetView オペレータに登録します。別ドメインの NetView プログラムに対する権限を示すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010104の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、置換整理のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNETVIEW(DOMAINS(d,を指定し、OSKB010104の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NETVIEW(DOMAINS(d,
    CASE OSKB010104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NETVIEW(DOMAINS(d,
    CASE OSKB010104
    SOURCE RACF
    ```

    NETVIEW(DOMAINS(d,とOSKB010104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB010104を同じ出力で読み、置換整理のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB010104
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB010104 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I NETVIEW(DOMAINS(d,など)) INFORMATION LISTED
    ```

    ICH35001IとOSKB010104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の NETVIEW(DOMAINS(d, と OSKB010104 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB010104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS MVS Planning: APPC / MVS Management / RACF Support for IBM MFA

    ---

    **ALTUSER TSO(など)**

    - 検証目的: 復旧確認のなどについて、利用者変更の説明として、TSO 属性保守で使う ALTUSER TSO(など) は、既存利用者の TSO セグメント内の項目を変更します。利用者変更の説明として、ACCTNUに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、復旧確認のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にALTUSER TSO(など)を指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ALTUSER TSO(など)
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ALTUSER TSO(など)
    CASE OSKB020018
    SOURCE RACF
    ```

    ALTUSER TSO(など)とOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB020018を同じ出力で読み、復旧確認のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB020018 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I ALTUSER TSO(など) INFORMATION LISTED
    ```

    ICH35001IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の ALTUSER TSO(など) と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **ALTUSER OMVS(など)**

    - 検証目的: 監査確認のなどについて、削除指定判断で使う ALTUSER OMVS(など) は、既存利用者の z/OS UNIX 用 OMVS セグメントを変更します。利用者 UNIX 属性の説明として、UID、Hに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、監査確認のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にALTUSER OMVS(など)を指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ALTUSER OMVS(など)
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ALTUSER OMVS(など)
    CASE OSKB020019
    SOURCE RACF
    ```

    ALTUSER OMVS(など)とOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB020019を同じ出力で読み、監査確認のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB020019 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I ALTUSER OMVS(など) INFORMATION LISTED
    ```

    ICH35001IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の ALTUSER OMVS(など) と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **ALTUSER CICS ・ DFP ・ NETVIEW ・ KERB など**

    - 検証目的: 構文照合の・ ・について、複数セグメント更新の説明として、ALTUSER は CICS、DFP、NETVIEW、KERB などの各種セグメントも部分更新できます。複数セグメント更新の説明として、ADに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、構文照合の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にALTUSER CICS ・ DFPを指定し、OSKB020021の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ALTUSER CICS ・ DFP
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ALTUSER CICS ・ DFP
    CASE OSKB020021
    SOURCE RACF
    ```

    ALTUSER CICS ・ DFPとOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB020021を同じ出力で読み、構文照合の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB020021 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I ALTUSER CICS ・ DFP ・ NETVIEW INFORMATION LISTED
    ```

    ICH35001IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の ALTUSER CICS ・ DFP と OSKB020021 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB020021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **LISTUSER KERB ・ EIM ・ PROXY ・ LANGUAGE ・ M**

    - 検証目的: 変更照合の・ ・ ・について、外部 ID 連携属性の説明として、LISTUSER は KERB、EIM、PROXY、LANGUAGE、MFA などのセグメントも指定して表示できます。Kerberos priに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、変更照合の・ ・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にLISTUSER KERB ・ EIを指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND LISTUSER KERB ・ EI
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM LISTUSER KERB ・ EI
    CASE OSKB020040
    SOURCE RACF
    ```

    LISTUSER KERB ・ EIとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB020040を同じ出力で読み、変更照合の・ ・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB020040 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I LISTUSER KERB ・ EIM ・ PROXY ・ INFORMATION LISTED
    ```

    ICH35001IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の LISTUSER KERB ・ EI と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / SA23-2290 z / OS Security Server RACF General User's Guide

    ---

    **DFP(STORCLAS ・ MGMTCLAS ・ DATACLAS ・ DAT**

    - 検証目的: 置換検査の・ ・について、グループ用の STORCLAS、MGMTCLAS、DATACLAS、DATAAPPL を指定できます。保管クラスの説明として、RACF グループに SMS 関連の既定値を持に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、置換検査の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にDFP(STORCLAS ・ MGMを指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DFP(STORCLAS ・ MGM
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DFP(STORCLAS ・ MGM
    CASE OSKB020064
    SOURCE RACF
    ```

    DFP(STORCLAS ・ MGMとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB020064を同じ出力で読み、置換検査の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB020064 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I DFP(STORCLAS ・ MGMTCLAS ・ DA INFORMATION LISTED
    ```

    ICH35001IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の DFP(STORCLAS ・ MGM と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide / z / OS UNIX System Services User's Guide (zOS31_bpxb200.pdf)

    ---

    **UACC(NONE|EXECUTE|READ|UPDATE|CONT**

    - 検証目的: 置換確認の| | |について、UACC は、ADDSD でアクセスリストに載っていない利用者へ与える汎用アクセス権限を定めます。低い権限から強い権限まで段階があり、値を高くすると明示許可なしの利用範囲がに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、置換確認の| | |の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にUACC(NONE|EXECUTE|を指定し、OSKB030004の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND UACC(NONE|EXECUTE|
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM UACC(NONE|EXECUTE|
    CASE OSKB030004
    SOURCE RACF
    ```

    UACC(NONE|EXECUTE|とOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB030004を同じ出力で読み、置換確認の| | |の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB030004 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I UACC(NONE|EXECUTE|READ|U INFORMATION LISTED
    ```

    ICH35001IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の UACC(NONE|EXECUTE| と OSKB030004 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB030004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **AUDIT(SUCCESS|FAILURES|ALL|NONE(など**

    - 検証目的: 条件確認の| |について、AUDIT は、ADDSD で対象プロファイルへのアクセス試行をどの条件で記録するかを設定します。成功、失敗、全件、なしを選び、必要に応じてアクセスレベルを組み合わせます。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030009の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、条件確認の| |の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(SUCCESS|FAILを指定し、OSKB030009の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND AUDIT(SUCCESS|FAIL
    CASE OSKB030009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM AUDIT(SUCCESS|FAIL
    CASE OSKB030009
    SOURCE RACF
    ```

    AUDIT(SUCCESS|FAILとOSKB030009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB030009を同じ出力で読み、条件確認の| |の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB030009
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB030009 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I AUDIT(SUCCESS|FAILURES|A INFORMATION LISTED
    ```

    ICH35001IとOSKB030009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の AUDIT(SUCCESS|FAIL と OSKB030009 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB030009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **AUDIT(READ|UPDATE|CONTROL|ALTER) 詳**

    - 検証目的: 区切確認の| |について、AUDIT の詳細指定では、ADDSD の中で READ、UPDATE、CONTROL、ALTER などのアクセスレベルを選べます。たとえば失敗した READ 以上だけを記に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、区切確認の| |の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(READ|UPDATE|を指定し、OSKB030010の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND AUDIT(READ|UPDATE|
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM AUDIT(READ|UPDATE|
    CASE OSKB030010
    SOURCE RACF
    ```

    AUDIT(READ|UPDATE|とOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB030010を同じ出力で読み、区切確認の| |の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB030010 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I AUDIT(READ|UPDATE|CONTRO INFORMATION LISTED
    ```

    ICH35001IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の AUDIT(READ|UPDATE| と OSKB030010 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB030010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **ID(uid|grp,など)**

    - 検証目的: 置換検査の| などについて、権限の受け手を示すために、PERMIT では ID(uid|grp,など) を使います。アクセスリストへ追加、変更、削除する利用者 ID またはグループ ID を並べられまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030064の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、置換検査の| などの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にID(uid|grp,など)を指定し、OSKB030064の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ID(uid|grp,など)
    CASE OSKB030064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ID(uid|grp,など)
    CASE OSKB030064
    SOURCE RACF
    ```

    ID(uid|grp,など)とOSKB030064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB030064を同じ出力で読み、置換検査の| などの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB030064
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB030064 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I ID(uid|grp,など) INFORMATION LISTED
    ```

    ICH35001IとOSKB030064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の ID(uid|grp,など) と OSKB030064 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB030064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **WHEN(DAYS(WEEKDAYS|ANYDAY|MONDAY|な**

    - 検証目的: 変更検査の|について、曜日で絞る PERMIT 条件には、WHEN(DAYS(など)) を使います。平日だけ許可する、週末だけ止めるといった運用条件を RACF 側に持たせる指定です。業務カレンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030080の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、変更検査の|の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(DAYS(WEEKDAYSを指定し、OSKB030080の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WHEN(DAYS(WEEKDAYS
    CASE OSKB030080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WHEN(DAYS(WEEKDAYS
    CASE OSKB030080
    SOURCE RACF
    ```

    WHEN(DAYS(WEEKDAYSとOSKB030080が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB030080を同じ出力で読み、変更検査の|の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB030080
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB030080 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I WHEN(DAYS(WEEKDAYS|ANYDA INFORMATION LISTED
    ```

    ICH35001IとOSKB030080が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の WHEN(DAYS(WEEKDAYS と OSKB030080 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB030080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

    ---

    **WHEN(CRITERIA(SQLROLE= など))**

    - 検証目的: 出力判定のなどについて、キーと値で絞る PERMIT 条件には、WHEN(CRITERIA(など)) を使います。条件名と値を対にして残せるため、SQL ロールなどの属性を構造的に表現できます。個に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030088の検証用出力を記録できる。
    - セッション環境: TSO RACFでLISTDSD DATASET('OSKB.DATA') ALLを実行し、ICH35001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に LISTDSD DATASET('OSKB.DATA') ALL を入力し、出力判定のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    ```

    COMMAND INPUTにLISTDSD DATASET('OSKB.DATA') ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(CRITERIA(SQLRを指定し、OSKB030088の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WHEN(CRITERIA(SQLR
    CASE OSKB030088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WHEN(CRITERIA(SQLR
    CASE OSKB030088
    SOURCE RACF
    ```

    WHEN(CRITERIA(SQLRとOSKB030088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。ICH35001IとOSKB030088を同じ出力で読み、出力判定のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL
    CASE OSKB030088
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    LISTDSD DATASET('OSKB.DATA') ALL
    USER=OSKB030088 OWNER=SYS1 DEFAULT-GROUP=SYS1
    ICH35001I WHEN(CRITERIA(SQLROLE= など INFORMATION LISTED
    ```

    ICH35001IとOSKB030088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTDSD DATASET('OSKB.DATA') ALL が画面・出力に表示されること
    ② ステップ2 の WHEN(CRITERIA(SQLR と OSKB030088 が画面・出力に表示されること
    ③ ステップ3 の ICH35001I と OSKB030088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SA23-2292 z / OS Security Server RACF Command Language Reference (zOS31_icha400.pdf) / SA23-2288 z / OS Security Server RACF Security Administrator's Guide

