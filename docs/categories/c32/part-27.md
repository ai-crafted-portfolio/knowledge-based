---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (27/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > 管理リファレンス

### CMDLINE {#c32-i3916}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDLINEは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.313) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.313)

??? question "確認問題（1問）"
    **問題.** 上書検査の管理リファレンスでネットビューの運用確認を行います。CMDLINE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検査の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書検査の確認記録にまとめる。 ✅
    - D. CMDLINE の属性行を読まず上書検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では CMDLINE は「IBM Z NetViewで CMDLINE の扱いを記録する上書検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では CMDLINE の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では CMDLINE の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMDMDL {#c32-i3917}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDMDLは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.314) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.314)

??? question "確認問題（1問）"
    **問題.** 出力検査の管理リファレンスに関する CMDMDL の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の管理リファレンスの証跡として保存して根拠にする。
    - C. CMDMDL の変更点を出力本文から切り離して出力検査の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では CMDMDL は「CMDMDL の状態と出力メッセージを結び付ける出力検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では CMDMDL の出力行と DSI633I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では CMDMDL を IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMDRCVR {#c32-i3918}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDRCVRは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.314) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.314)

??? question "確認問題（1問）"
    **問題.** 条件検査の管理リファレンスに関係する CMDRCVR の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件検査の結果として保存する。 ✅
    - B. CMDRCVR の名称と担当者名のみを残して条件検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では CMDRCVR は「CMDRCVR の用途をネットビューの表示で確認する条件検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの CMDRCVR と DSI633I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では CMDRCVR を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMDSYN {#c32-i3919}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDSYNは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.315) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.315)

??? question "確認問題（1問）"
    **問題.** 区切検査の管理リファレンスで CMDSYN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CMDSYN の出力を取らず区切検査の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切検査の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では CMDSYN は「区切検査の管理リファレンスに関係する定義値と表示行を照合する区切検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では CMDSYN の属性行と DSI633I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では CMDSYN を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMSGCFG {#c32-i3920}
*分類: 管理リファレンス*  ・  難易度: 中級

CMSGCFGは、Tivoli NetView z/OS 自動化の管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Administration Reference (p.505) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.505)

??? question "確認問題（1問）"
    **問題.** 範囲検査の管理リファレンスでネットビューの運用確認を行います。CMSGCFG の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検査の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲検査として引き継ぐ。 ✅
    - D. CMSGCFG の属性行を読まず範囲検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では CMSGCFG は「IBM Z NetViewで CMSGCFG の扱いを記録する範囲検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では CMSGCFG の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では CMSGCFG の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CNMI {#c32-i3921}
*分類: 管理リファレンス*  ・  難易度: 中級

CNMIは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.59) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.59)

??? question "確認問題（1問）"
    **問題.** 優先検査の管理リファレンスに関する CNMI の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の管理リファレンスの証跡として保存して根拠にする。
    - C. CNMI の変更点を出力本文から切り離して優先検査の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先検査の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では CNMI は「CNMI の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では CNMI の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では CNMI を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CNMSTYLE Initialization Statements {#c32-i3922}
*分類: 管理リファレンス*  ・  難易度: 中級

CNMSTYLE Initialization Statementsは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.31) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.31)

??? question "確認問題（1問）"
    **問題.** 記録検査の管理リファレンスに関係する CNMSTYLE 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、記録検査の点検結果を残す。 ✅
    - B. CNMSTYLE 機能の名称と担当者名のみを残して記録検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では CNMSTYLE 機能 は「CNMSTYLE 機能の用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの CNMSTYLE 機能と DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では CNMSTYLE 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COLUMNHEAD {#c32-i3923}
*分類: 管理リファレンス*  ・  難易度: 中級

COLUMNHEADは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.315) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.315)

??? question "確認問題（1問）"
    **問題.** 比較検査の管理リファレンスで COLUMNHEAD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COLUMNHEAD の出力を取らず比較検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較検査で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して比較検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では COLUMNHEAD は「比較検査の管理リファレンスに関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では COLUMNHEAD の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では COLUMNHEAD を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.DUIFHNAM {#c32-i3924}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.DUIFHNAMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.68) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.68)

??? question "確認問題（1問）"
    **問題.** 値域検査の管理リファレンスに関する COMMON.DUIFHNAM の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の管理リファレンスの証跡として保存して根拠にする。
    - C. COMMON.DUIFHNAM の変更点を出力本文から切り離して値域検査の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では COMMON.DUIFHNAM は「COMMON.DUIFHNAM の状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では COMMON.DUIFHNAM の出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では COMMON.DUIFHNAM を IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.DUIFHPRC {#c32-i3925}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.DUIFHPRCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.68) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.68)

??? question "確認問題（1問）"
    **問題.** 警告検査の管理リファレンスに関係する COMMON.DUIFHPRC の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を警告検査で確認する。 ✅
    - B. COMMON.DUIFHPRC の名称と担当者名のみを残して警告検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では COMMON.DUIFHPRC は「COMMON.DUIFHPRC の用途をネットビューの表示で確認する警告検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの COMMON.DUIFHPRC と DSI633I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では COMMON.DUIFHPRC を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EKGHNAM {#c32-i3926}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EKGHNAMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.69) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.69)

??? question "確認問題（1問）"
    **問題.** 復旧検査の管理リファレンスで COMMON.EKGHNAM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COMMON.EKGHNAM の出力を取らず復旧検査の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、復旧検査の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では COMMON.EKGHNAM は「復旧検査の管理リファレンスに関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では COMMON.EKGHNAM の属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では COMMON.EKGHNAM を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EKGHPRC {#c32-i3927}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EKGHPRCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.69) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.69)

??? question "確認問題（1問）"
    **問題.** 監査検査の管理リファレンスでネットビューの運用確認を行います。COMMON.EKGHPRC の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査検査の確認記録にまとめる。 ✅
    - D. COMMON.EKGHPRC の属性行を読まず監査検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では COMMON.EKGHPRC は「IBM Z NetViewで COMMON.EKGHPRC の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では COMMON.EKGHPRC の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では COMMON.EKGHPRC の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLINITDELAY {#c32-i3928}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EZLINITDELAYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.69) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.69)

??? question "確認問題（1問）"
    **問題.** 変更検査の管理リファレンスに関する COMMON 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の管理リファレンスの証跡として保存して根拠にする。
    - C. COMMON 属性の変更点を出力本文から切り離して変更検査の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では COMMON 属性 は「COMMON 属性の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では COMMON 属性の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では COMMON 属性を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLIPTraceJCLWait {#c32-i3929}
*分類: 管理リファレンス*  ・  難易度: 上級

COMMON.EZLIPTraceJCLWaitは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.69) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.69)

??? question "確認問題（1問）"
    **問題.** 構文判定の管理リファレンスに関係する COMMON 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、構文判定の結果として保存する。 ✅
    - B. COMMON 属性の名称と担当者名のみを残して構文判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では COMMON 属性 は「COMMON 属性の用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの COMMON 属性と DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では COMMON 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLRMTTIMER {#c32-i3930}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EZLRMTTIMERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.70) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.70)

??? question "確認問題（1問）"
    **問題.** 展開判定の管理リファレンスで COMMON.EZLRMTTIMER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COMMON.EZLRMTTIMER の出力を取らず展開判定の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、展開判定の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して展開判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では COMMON.EZLRMTTIMER は「展開判定の管理リファレンスに関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では COMMON.EZLRMTTIMER の属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では COMMON.EZLRMTTIMER を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLTCPcTRACEwriter {#c32-i3931}
*分類: 管理リファレンス*  ・  難易度: 上級

COMMON.EZLTCPcTRACEwriterは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.72) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.72)

??? question "確認問題（1問）"
    **問題.** 探索判定の管理リファレンスで COMMON 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COMMON 属性の出力を取らず探索判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索判定で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では COMMON 属性 は「探索判定の管理リファレンスに関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では COMMON 属性の属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では COMMON 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLTRACED {#c32-i3932}
*分類: 管理リファレンス*  ・  難易度: 上級

COMMON.EZLTRACEDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.72) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.72)

??? question "確認問題（1問）"
    **問題.** 上書判定の管理リファレンスでネットビューの運用確認を行います。COMMON.EZLTRACED の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書判定の確認値として扱う。 ✅
    - D. COMMON.EZLTRACED の属性行を読まず上書判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では COMMON.EZLTRACED は「IBM Z NetViewで COMMON.EZLTRACED の扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では COMMON.EZLTRACED の表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では COMMON.EZLTRACED の使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLsmtpDEST {#c32-i3933}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EZLsmtpDESTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.70) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.70)

??? question "確認問題（1問）"
    **問題.** 呼出判定の管理リファレンスでネットビューの運用確認を行います。COMMON.EZLsmtpDEST の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出判定として引き継ぐ。 ✅
    - D. COMMON.EZLsmtpDEST の属性行を読まず呼出判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では COMMON.EZLsmtpDEST は「IBM Z NetViewで COMMON.EZLsmtpDEST の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では COMMON.EZLsmtpDEST の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では COMMON.EZLsmtpDEST の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLsmtpHOSTNAME {#c32-i3934}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EZLsmtpHOSTNAMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.71) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.71)

??? question "確認問題（1問）"
    **問題.** 置換判定の管理リファレンスに関する COMMON 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定の管理リファレンスの証跡として保存して根拠にする。
    - C. COMMON 属性の変更点を出力本文から切り離して置換判定の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換判定の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では COMMON 属性 は「COMMON 属性の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では COMMON 属性の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では COMMON 属性を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.EZLsmtpNAME {#c32-i3935}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.EZLsmtpNAMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.71) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.71)

??? question "確認問題（1問）"
    **問題.** 終端判定の管理リファレンスに関係する COMMON.EZLsmtpNAME の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端判定の点検結果を残す。 ✅
    - B. COMMON.EZLsmtpNAME の名称と担当者名のみを残して終端判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では COMMON.EZLsmtpNAME は「COMMON.EZLsmtpNAME の用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの COMMON.EZLsmtpNAME と DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では COMMON.EZLsmtpNAME を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.FLC_RODMNAME {#c32-i3936}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.FLC_RODMNAMEは、Tivoli NetView z/OS 自動化の管理リファレンスでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Administration Reference (p.72) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.72)

??? question "確認問題（1問）"
    **問題.** 出力判定の管理リファレンスに関する COMMON 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず出力判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の管理リファレンスの証跡として保存して根拠にする。
    - C. COMMON 属性の変更点を出力本文から切り離して出力判定の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では COMMON 属性 は「COMMON 属性の状態と出力メッセージを結び付ける出力判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では COMMON 属性の出力行と EKG000I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では COMMON 属性を IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.SMFVPD {#c32-i3937}
*分類: 管理リファレンス*  ・  難易度: 上級

COMMON.SMFVPDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.75) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.75)

??? question "確認問題（1問）"
    **問題.** 条件判定の管理リファレンスに関係する COMMON.SMFVPD の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を条件判定で確認する。 ✅
    - B. COMMON.SMFVPD の名称と担当者名のみを残して条件判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では COMMON.SMFVPD は「COMMON.SMFVPD の用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの COMMON.SMFVPD と DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では COMMON.SMFVPD を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.STACKFAMILY {#c32-i3938}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.STACKFAMILYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.76) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.76)

??? question "確認問題（1問）"
    **問題.** 区切判定の管理リファレンスで COMMON.STACKFAMILY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COMMON.STACKFAMILY の出力を取らず区切判定の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、区切判定の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して区切判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では COMMON.STACKFAMILY は「区切判定の管理リファレンスに関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では COMMON.STACKFAMILY の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では COMMON.STACKFAMILY を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.WAITTIME {#c32-i3939}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.WAITTIMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.76) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.76)

??? question "確認問題（1問）"
    **問題.** 優先判定の管理リファレンスに関する COMMON.WAITTIME の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の管理リファレンスの証跡として保存して根拠にする。
    - C. COMMON.WAITTIME の変更点を出力本文から切り離して優先判定の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先判定の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では COMMON.WAITTIME は「COMMON.WAITTIME の状態と出力メッセージを結び付ける優先判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では COMMON.WAITTIME の出力行と DSI633I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では COMMON.WAITTIME を IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.XDOMTIME {#c32-i3940}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.XDOMTIMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.76) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.76)

??? question "確認問題（1問）"
    **問題.** 記録判定の管理リファレンスに関係する COMMON.XDOMTIME の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録判定の結果として保存する。 ✅
    - B. COMMON.XDOMTIME の名称と担当者名のみを残して記録判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では COMMON.XDOMTIME は「COMMON.XDOMTIME の用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewの COMMON.XDOMTIME と DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では COMMON.XDOMTIME を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMMON.variable_name {#c32-i3941}
*分類: 管理リファレンス*  ・  難易度: 中級

COMMON.variable_nameは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.60) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.60)

??? question "確認問題（1問）"
    **問題.** 範囲判定の管理リファレンスでネットビューの運用確認を行います。COMMON 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲判定の確認記録にまとめる。 ✅
    - D. COMMON 属性の属性行を読まず範囲判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では COMMON 属性 は「IBM Z NetViewで COMMON 属性の扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では COMMON 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では COMMON 属性の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COMNTESC {#c32-i3942}
*分類: 管理リファレンス*  ・  難易度: 中級

COMNTESCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.317) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.317)

??? question "確認問題（1問）"
    **問題.** 順序判定の管理リファレンスでネットビューの運用確認を行います。COMNTESC の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序判定として引き継ぐ。 ✅
    - D. COMNTESC の属性行を読まず順序判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では COMNTESC は「IBM Z NetViewで COMNTESC の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では COMNTESC の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では COMNTESC の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CONCURRENT_USERS {#c32-i3943}
*分類: 管理リファレンス*  ・  難易度: 中級

CONCURRENT_USERSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.531) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.531)

??? question "確認問題（1問）"
    **問題.** 値域判定の管理リファレンスに関する CONCURRENT_USERS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の管理リファレンスの証跡として保存して根拠にする。
    - C. CONCURRENT_USERS の変更点を出力本文から切り離して値域判定の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域判定の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では CONCURRENT_USERS は「CONCURRENT_USERS の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では CONCURRENT_USERS の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では CONCURRENT_USERS を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CONNECT_VIOLATION_MESSAGE {#c32-i3944}
*分類: 管理リファレンス*  ・  難易度: 中級

CONNECT_VIOLATION_MESSAGEは、Tivoli NetView z/OS 自動化の管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Administration Reference (p.532) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.532)

??? question "確認問題（1問）"
    **問題.** 警告判定の管理リファレンスに関係する CONNECT_VIOLATION_MESSAG の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告判定の点検結果を残す。 ✅
    - B. CONNECT_VIOLATION_MESSAG の名称と担当者名のみを残して警告判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では CONNECT_VIOLATION_MESSAG は「CONNECT_VIOLATION_MESSAG の用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewの CONNECT_VIOLATION_MESSAG と DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では CONNECT_VIOLATION_MESSAG を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CONTACT {#c32-i3945}
*分類: 管理リファレンス*  ・  難易度: 中級

CONTACTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.493) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.493)

??? question "確認問題（1問）"
    **問題.** 構文整理の管理リファレンスに関係する CONTACT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を構文整理で確認する。 ✅
    - B. CONTACT の名称と担当者名のみを残して構文整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では CONTACT は「CONTACT の用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの CONTACT と DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では CONTACT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### COS {#c32-i3946}
*分類: 管理リファレンス*  ・  難易度: 中級

COSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.317) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.317)

??? question "確認問題（1問）"
    **問題.** 展開整理の管理リファレンスで COS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COS の出力を取らず展開整理の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、展開整理の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して展開整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では COS は「展開整理の管理リファレンスに関係する定義値と表示行を照合する展開整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では COS の属性行と DSI633I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では COS を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CPCPSESS (SNA) {#c32-i3947}
*分類: 管理リファレンス*  ・  難易度: 中級

CPCPSESS (SNA)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.419) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.419)

??? question "確認問題（1問）"
    **問題.** 呼出整理の管理リファレンスでネットビューの運用確認を行います。CPCPSESS (SNA)の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出整理の確認記録にまとめる。 ✅
    - D. CPCPSESS (SNA)の属性行を読まず呼出整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では CPCPSESS (SNA) は「IBM Z NetViewで CPCPSESS (SNA)の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では CPCPSESS (SNA)の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では CPCPSESS (SNA)の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CZ.FILTER {#c32-i3948}
*分類: 管理リファレンス*  ・  難易度: 中級

CZ.FILTERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.85) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.85)

??? question "確認問題（1問）"
    **問題.** 置換整理の管理リファレンスに関する CZ.FILTER の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理の管理リファレンスの証跡として保存して根拠にする。
    - C. CZ.FILTER の変更点を出力本文から切り離して置換整理の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では CZ.FILTER は「CZ.FILTER の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では CZ.FILTER の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では CZ.FILTER を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Common Global Variables for the Canzlog Archiving Function {#c32-i3949}
*分類: 管理リファレンス*  ・  難易度: 中級

Common Global Variables for the Canzlog Archiving Functionは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検査の管理リファレンスでネットビューの運用確認を行います。Common 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序検査の確認値として扱う。 ✅
    - D. Common 機能の属性行を読まず順序検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Common 機能 は「IBM Z NetViewで Common 機能の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Common 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Common 機能の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Community {#c32-i3950}
*分類: 管理リファレンス*  ・  難易度: 中級

Communityは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.506) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.506)

??? question "確認問題（1問）"
    **問題.** 比較判定の管理リファレンスで Communityの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Communityの出力を取らず比較判定の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、比較判定の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して比較判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Community は「比較判定の管理リファレンスに関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Communityの属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Communityを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ConnectionMode {#c32-i3951}
*分類: 管理リファレンス*  ・  難易度: 中級

ConnectionModeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.507) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.507)

??? question "確認問題（1問）"
    **問題.** 復旧判定の管理リファレンスで ConnectionModeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ConnectionModeの出力を取らず復旧判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧判定で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では ConnectionMode は「復旧判定の管理リファレンスに関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では ConnectionModeの属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では ConnectionModeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ConsFixed {#c32-i3952}
*分類: 管理リファレンス*  ・  難易度: 中級

ConsFixedは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.79) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.79)

??? question "確認問題（1問）"
    **問題.** 監査判定の管理リファレンスでネットビューの運用確認を行います。ConsFixedの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査判定の確認値として扱う。 ✅
    - D. ConsFixedの属性行を読まず監査判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では ConsFixed は「IBM Z NetViewで ConsFixedの扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では ConsFixedの表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では ConsFixedの使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ConsMask {#c32-i3953}
*分類: 管理リファレンス*  ・  難易度: 中級

ConsMaskは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.79) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.79)

??? question "確認問題（1問）"
    **問題.** 変更判定の管理リファレンスに関する ConsMaskの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定の管理リファレンスの証跡として保存して根拠にする。
    - C. ConsMaskの変更点を出力本文から切り離して変更判定の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では ConsMask は「ConsMaskの状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では ConsMaskの出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では ConsMaskを IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DB2SEC {#c32-i3954}
*分類: 管理リファレンス*  ・  難易度: 中級

DB2SECは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.88) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.88)

??? question "確認問題（1問）"
    **問題.** 終端整理の管理リファレンスに関係する DB2SEC の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端整理の結果として保存する。 ✅
    - B. DB2SEC の名称と担当者名のみを残して終端整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では DB2SEC は「DB2SEC の用途をネットビューの表示で確認する終端整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの DB2SEC と DSI633I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では DB2SEC を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DBFULL {#c32-i3955}
*分類: 管理リファレンス*  ・  難易度: 中級

DBFULLは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.318) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.318)

??? question "確認問題（1問）"
    **問題.** 探索整理の管理リファレンスで DBFULL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DBFULL の出力を取らず探索整理の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、探索整理の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して探索整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では DBFULL は「探索整理の管理リファレンスに関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では DBFULL の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では DBFULL を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DDFGENERIC {#c32-i3956}
*分類: 管理リファレンス*  ・  難易度: 中級

DDFGENERICは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.419) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.419)

??? question "確認問題（1問）"
    **問題.** 上書整理の管理リファレンスでネットビューの運用確認を行います。DDFGENERIC の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書整理として引き継ぐ。 ✅
    - D. DDFGENERIC の属性行を読まず上書整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では DDFGENERIC は「IBM Z NetViewで DDFGENERIC の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では DDFGENERIC の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では DDFGENERIC の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DDFGROUP {#c32-i3957}
*分類: 管理リファレンス*  ・  難易度: 中級

DDFGROUPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.421) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.421)

??? question "確認問題（1問）"
    **問題.** 出力整理の管理リファレンスに関する DDFGROUP の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理の管理リファレンスの証跡として保存して根拠にする。
    - C. DDFGROUP の変更点を出力本文から切り離して出力整理の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力整理の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では DDFGROUP は「DDFGROUP の状態と出力メッセージを結び付ける出力整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では DDFGROUP の出力行と DSI633I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では DDFGROUP を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DEFAULTS {#c32-i3958}
*分類: 管理リファレンス*  ・  難易度: 中級

DEFAULTSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.88) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.88)

??? question "確認問題（1問）"
    **問題.** 条件整理の管理リファレンスに関係する DEFAULTS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件整理の点検結果を残す。 ✅
    - B. DEFAULTS の名称と担当者名のみを残して条件整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では DEFAULTS は「DEFAULTS の用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの DEFAULTS と DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では DEFAULTS を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DEFENTPT {#c32-i3959}
*分類: 管理リファレンス*  ・  難易度: 中級

DEFENTPTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.318) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.318)

??? question "確認問題（1問）"
    **問題.** 区切整理の管理リファレンスで DEFENTPT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DEFENTPT の出力を取らず区切整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切整理で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して区切整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では DEFENTPT は「区切整理の管理リファレンスに関係する定義値と表示行を照合する区切整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では DEFENTPT の属性行と DSI633I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では DEFENTPT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DEFFOCPT {#c32-i3960}
*分類: 管理リファレンス*  ・  難易度: 中級

DEFFOCPTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.319) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.319)

??? question "確認問題（1問）"
    **問題.** 範囲整理の管理リファレンスでネットビューの運用確認を行います。DEFFOCPT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲整理の確認値として扱う。 ✅
    - D. DEFFOCPT の属性行を読まず範囲整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では DEFFOCPT は「IBM Z NetViewで DEFFOCPT の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では DEFFOCPT の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では DEFFOCPT の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DEFFOCPT Statement in DSI6INIT {#c32-i3961}
*分類: 管理リファレンス*  ・  難易度: 中級

DEFFOCPT Statement in DSI6INITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.320) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.320)

??? question "確認問題（1問）"
    **問題.** 優先整理の管理リファレンスに関する DEFFOCPT 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理の管理リファレンスの証跡として保存して根拠にする。
    - C. DEFFOCPT 機能の変更点を出力本文から切り離して優先整理の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先整理の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では DEFFOCPT 機能 は「DEFFOCPT 機能の状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では DEFFOCPT 機能の出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では DEFFOCPT 機能を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DEFFOCPT Statement in DSICRTTD {#c32-i3962}
*分類: 管理リファレンス*  ・  難易度: 中級

DEFFOCPT Statement in DSICRTTDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.319) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.319)

??? question "確認問題（1問）"
    **問題.** 記録整理の管理リファレンスに関係する DEFFOCPT 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を記録整理で確認する。 ✅
    - B. DEFFOCPT 機能の名称と担当者名のみを残して記録整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では DEFFOCPT 機能 は「DEFFOCPT 機能の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの DEFFOCPT 機能と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では DEFFOCPT 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DISCOVERY.INTAPPL {#c32-i3963}
*分類: 管理リファレンス*  ・  難易度: 中級

DISCOVERY.INTAPPLは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.89) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.89)

??? question "確認問題（1問）"
    **問題.** 比較整理の管理リファレンスで DISCOVERY.INTAPPL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DISCOVERY.INTAPPL の出力を取らず比較整理の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較整理の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では DISCOVERY.INTAPPL は「比較整理の管理リファレンスに関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では DISCOVERY.INTAPPL の属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では DISCOVERY.INTAPPL を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DISCOVERY.INTINTERFACE {#c32-i3964}
*分類: 管理リファレンス*  ・  難易度: 中級

DISCOVERY.INTINTERFACEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.89) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.89)

??? question "確認問題（1問）"
    **問題.** 順序整理の管理リファレンスでネットビューの運用確認を行います。DISCOVERY 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序整理の確認記録にまとめる。 ✅
    - D. DISCOVERY 属性の属性行を読まず順序整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では DISCOVERY 属性 は「IBM Z NetViewで DISCOVERY 属性の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では DISCOVERY 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では DISCOVERY 属性の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DISCOVERY.INTTELNET {#c32-i3965}
*分類: 管理リファレンス*  ・  難易度: 中級

DISCOVERY.INTTELNETは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.90) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.90)

??? question "確認問題（1問）"
    **問題.** 値域整理の管理リファレンスに関する DISCOVERY 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理の管理リファレンスの証跡として保存して根拠にする。
    - C. DISCOVERY 属性の変更点を出力本文から切り離して値域整理の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では DISCOVERY 属性 は「DISCOVERY 属性の状態と出力メッセージを結び付ける値域整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では DISCOVERY 属性の出力行と DSI633I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では DISCOVERY 属性を IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DISCOVERY.NetViewOnly {#c32-i3966}
*分類: 管理リファレンス*  ・  難易度: 中級

DISCOVERY.NetViewOnlyは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.90) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.90)

??? question "確認問題（1問）"
    **問題.** 警告整理の管理リファレンスに関係する DISCOVERY 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告整理の結果として保存する。 ✅
    - B. DISCOVERY 属性の名称と担当者名のみを残して警告整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では DISCOVERY 属性 は「DISCOVERY 属性の用途をネットビューの表示で確認する警告整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの DISCOVERY 属性と DSI633I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では DISCOVERY 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DISCOVERY.SNMP {#c32-i3967}
*分類: 管理リファレンス*  ・  難易度: 中級

DISCOVERY.SNMPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.91) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.91)

??? question "確認問題（1問）"
    **問題.** 復旧整理の管理リファレンスで DISCOVERY.SNMP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DISCOVERY.SNMP の出力を取らず復旧整理の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧整理の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では DISCOVERY.SNMP は「復旧整理の管理リファレンスに関係する定義値と表示行を照合する復旧整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では DISCOVERY.SNMP の属性行と DSI633I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では DISCOVERY.SNMP を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.cmdb_ftp_server {#c32-i3968}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.cmdb_ftp_serverは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.91) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.91)

??? question "確認問題（1問）"
    **問題.** 監査整理の管理リファレンスでネットビューの運用確認を行います。DLA 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査整理として引き継ぐ。 ✅
    - D. DLA 属性の属性行を読まず監査整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では DLA 属性 は「IBM Z NetViewで DLA 属性の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では DLA 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では DLA 属性の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.debug {#c32-i3969}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.debugは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.92) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.92)

??? question "確認問題（1問）"
    **問題.** 変更整理の管理リファレンスに関する DLA.debugの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理の管理リファレンスの証跡として保存して根拠にする。
    - C. DLA.debugの変更点を出力本文から切り離して変更整理の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更整理の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では DLA.debug は「DLA.debugの状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では DLA.debugの出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では DLA.debugを IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_log_blocksize {#c32-i3970}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_log_blocksizeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.92) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.92)

??? question "確認問題（1問）"
    **問題.** 構文記録の管理リファレンスに関係する DLA 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文記録の点検結果を残す。 ✅
    - B. DLA 属性の名称と担当者名のみを残して構文記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では DLA 属性 は「DLA 属性の用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの DLA 属性と DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では DLA 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_log_filename {#c32-i3971}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_log_filenameは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.93) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.93)

??? question "確認問題（1問）"
    **問題.** 展開記録の管理リファレンスで DLA 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLA 属性の出力を取らず展開記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開記録で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して展開記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では DLA 属性 は「展開記録の管理リファレンスに関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では DLA 属性の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では DLA 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_log_space_pri {#c32-i3972}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_log_space_priは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.93) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.93)

??? question "確認問題（1問）"
    **問題.** 呼出記録の管理リファレンスでネットビューの運用確認を行います。DLA 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出記録の確認値として扱う。 ✅
    - D. DLA 属性の属性行を読まず呼出記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では DLA 属性 は「IBM Z NetViewで DLA 属性の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では DLA 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では DLA 属性の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_log_space_sec {#c32-i3973}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_log_space_secは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.94) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.94)

??? question "確認問題（1問）"
    **問題.** 置換記録の管理リファレンスに関する DLA 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録の管理リファレンスの証跡として保存して根拠にする。
    - C. DLA 属性の変更点を出力本文から切り離して置換記録の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では DLA 属性 は「DLA 属性の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では DLA 属性の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では DLA 属性を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_log_unit {#c32-i3974}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_log_unitは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.94) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.94)

??? question "確認問題（1問）"
    **問題.** 終端記録の管理リファレンスに関係する DLA.ftp_log_unitの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を終端記録で確認する。 ✅
    - B. DLA.ftp_log_unitの名称と担当者名のみを残して終端記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では DLA.ftp_log_unit は「DLA.ftp_log_unitの用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの DLA.ftp_log_unitと DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では DLA.ftp_log_unitを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_log_volume {#c32-i3975}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_log_volumeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.95) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.95)

??? question "確認問題（1問）"
    **問題.** 探索記録の管理リファレンスで DLA.ftp_log_volumeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLA.ftp_log_volumeの出力を取らず探索記録の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索記録の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では DLA.ftp_log_volume は「探索記録の管理リファレンスに関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では DLA.ftp_log_volumeの属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では DLA.ftp_log_volumeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_max_xmit_tm {#c32-i3976}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_max_xmit_tmは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.96) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.96)

??? question "確認問題（1問）"
    **問題.** 上書記録の管理リファレンスでネットビューの運用確認を行います。DLA 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書記録の確認記録にまとめる。 ✅
    - D. DLA 属性の属性行を読まず上書記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では DLA 属性 は「IBM Z NetViewで DLA 属性の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では DLA 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では DLA 属性の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_remote_dir {#c32-i3977}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_remote_dirは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.96) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.96)

??? question "確認問題（1問）"
    **問題.** 出力記録の管理リファレンスに関する DLA.ftp_remote_dirの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録の管理リファレンスの証跡として保存して根拠にする。
    - C. DLA.ftp_remote_dirの変更点を出力本文から切り離して出力記録の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力記録の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では DLA.ftp_remote_dir は「DLA.ftp_remote_dirの状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では DLA.ftp_remote_dirの出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では DLA.ftp_remote_dirを IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_timeout {#c32-i3978}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_timeoutは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.97) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.97)

??? question "確認問題（1問）"
    **問題.** 条件記録の管理リファレンスに関係する DLA.ftp_timeoutの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件記録の結果として保存する。 ✅
    - B. DLA.ftp_timeoutの名称と担当者名のみを残して条件記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では DLA.ftp_timeout は「DLA.ftp_timeoutの用途をネットビューの表示で確認する条件記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの DLA.ftp_timeoutと DSI633I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では DLA.ftp_timeoutを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.ftp_uid {#c32-i3979}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.ftp_uidは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.97) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.97)

??? question "確認問題（1問）"
    **問題.** 区切記録の管理リファレンスで DLA.ftp_uidの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLA.ftp_uidの出力を取らず区切記録の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切記録の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では DLA.ftp_uid は「区切記録の管理リファレンスに関係する定義値と表示行を照合する区切記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では DLA.ftp_uidの属性行と DSI633I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では DLA.ftp_uidを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.is_second_level {#c32-i3980}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.is_second_levelは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.98) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.98)

??? question "確認問題（1問）"
    **問題.** 範囲記録の管理リファレンスでネットビューの運用確認を行います。DLA 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲記録として引き継ぐ。 ✅
    - D. DLA 属性の属性行を読まず範囲記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では DLA 属性 は「IBM Z NetViewで DLA 属性の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では DLA 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では DLA 属性の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.statefile {#c32-i3981}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.statefileは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.98) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.98)

??? question "確認問題（1問）"
    **問題.** 優先記録の管理リファレンスに関する DLA.statefileの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の管理リファレンスの証跡として保存して根拠にする。
    - C. DLA.statefileの変更点を出力本文から切り離して優先記録の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先記録の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では DLA.statefile は「DLA.statefileの状態と出力メッセージを結び付ける優先記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では DLA.statefileの出力行と DSI633I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では DLA.statefileを IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.tsouser {#c32-i3982}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.tsouserは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.99) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.99)

??? question "確認問題（1問）"
    **問題.** 記録記録の管理リファレンスに関係する DLA.tsouserの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、記録記録の点検結果を残す。 ✅
    - B. DLA.tsouserの名称と担当者名のみを残して記録記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では DLA.tsouser は「DLA.tsouserの用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの DLA.tsouserと DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では DLA.tsouserを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.xml_blocksize {#c32-i3983}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.xml_blocksizeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.99) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.99)

??? question "確認問題（1問）"
    **問題.** 比較記録の管理リファレンスで DLA.xml_blocksizeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLA.xml_blocksizeの出力を取らず比較記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較記録で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して比較記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では DLA.xml_blocksize は「比較記録の管理リファレンスに関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では DLA.xml_blocksizeの属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では DLA.xml_blocksizeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.xml_filename {#c32-i3984}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.xml_filenameは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.100)

??? question "確認問題（1問）"
    **問題.** 順序記録の管理リファレンスでネットビューの運用確認を行います。DLA.xml_filenameの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序記録の確認値として扱う。 ✅
    - D. DLA.xml_filenameの属性行を読まず順序記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では DLA.xml_filename は「IBM Z NetViewで DLA.xml_filenameの扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では DLA.xml_filenameの表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では DLA.xml_filenameの使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.xml_space_pri {#c32-i3985}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.xml_space_priは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.100)

??? question "確認問題（1問）"
    **問題.** 値域記録の管理リファレンスに関する DLA.xml_space_priの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録の管理リファレンスの証跡として保存して根拠にする。
    - C. DLA.xml_space_priの変更点を出力本文から切り離して値域記録の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では DLA.xml_space_pri は「DLA.xml_space_priの状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では DLA.xml_space_priの出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では DLA.xml_space_priを IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.xml_space_sec {#c32-i3986}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.xml_space_secは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.101) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.101)

??? question "確認問題（1問）"
    **問題.** 警告記録の管理リファレンスに関係する DLA.xml_space_secの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を警告記録で確認する。 ✅
    - B. DLA.xml_space_secの名称と担当者名のみを残して警告記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では DLA.xml_space_sec は「DLA.xml_space_secの用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの DLA.xml_space_secと DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では DLA.xml_space_secを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.xml_unit {#c32-i3987}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.xml_unitは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.101) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.101)

??? question "確認問題（1問）"
    **問題.** 復旧記録の管理リファレンスで DLA.xml_unitの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLA.xml_unitの出力を取らず復旧記録の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、復旧記録の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では DLA.xml_unit は「復旧記録の管理リファレンスに関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では DLA.xml_unitの属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では DLA.xml_unitを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DLA.xml_volume {#c32-i3988}
*分類: 管理リファレンス*  ・  難易度: 中級

DLA.xml_volumeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.102) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.102)

??? question "確認問題（1問）"
    **問題.** 監査記録の管理リファレンスでネットビューの運用確認を行います。DLA.xml_volumeの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査記録の確認記録にまとめる。 ✅
    - D. DLA.xml_volumeの属性行を読まず監査記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では DLA.xml_volume は「IBM Z NetViewで DLA.xml_volumeの扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では DLA.xml_volumeの表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では DLA.xml_volumeの使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DOMAIN {#c32-i3989}
*分類: 管理リファレンス*  ・  難易度: 中級

DOMAINは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.102) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.102)

??? question "確認問題（1問）"
    **問題.** 変更記録の管理リファレンスに関する DOMAIN の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録の管理リファレンスの証跡として保存して根拠にする。
    - C. DOMAIN の変更点を出力本文から切り離して変更記録の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更記録の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では DOMAIN は「DOMAIN の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では DOMAIN の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では DOMAIN を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DOMAINS {#c32-i3990}
*分類: 管理リファレンス*  ・  難易度: 中級

DOMAINSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.322) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.322)

??? question "確認問題（1問）"
    **問題.** 構文分離の管理リファレンスに関係する DOMAINS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、構文分離の結果として保存する。 ✅
    - B. DOMAINS の名称と担当者名のみを残して構文分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では DOMAINS は「DOMAINS の用途をネットビューの表示で確認する構文分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの DOMAINS と DSI633I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では DOMAINS を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DSTINIT {#c32-i3991}
*分類: 管理リファレンス*  ・  難易度: 中級

DSTINITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.323) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.323)

??? question "確認問題（1問）"
    **問題.** 展開分離の管理リファレンスで DSTINIT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DSTINIT の出力を取らず展開分離の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、展開分離の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して展開分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では DSTINIT は「展開分離の管理リファレンスに関係する定義値と表示行を照合する展開分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では DSTINIT の属性行と DSI633I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では DSTINIT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DUMP_FOR_BAD_USER_DATA {#c32-i3992}
*分類: 管理リファレンス*  ・  難易度: 中級

DUMP_FOR_BAD_USER_DATAは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.532) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.532)

??? question "確認問題（1問）"
    **問題.** 呼出分離の管理リファレンスでネットビューの運用確認を行います。DUMP_FOR_BAD_USER_DATA の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出分離の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出分離として引き継ぐ。 ✅
    - D. DUMP_FOR_BAD_USER_DATA の属性行を読まず呼出分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では DUMP_FOR_BAD_USER_DATA は「IBM Z NetViewで DUMP_FOR_BAD_USER_DATA の扱いを記録する呼出分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では DUMP_FOR_BAD_USER_DATA の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では DUMP_FOR_BAD_USER_DATA の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DUMP_LIMIT {#c32-i3993}
*分類: 管理リファレンス*  ・  難易度: 中級

DUMP_LIMITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.532) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.532)

??? question "確認問題（1問）"
    **問題.** 置換分離の管理リファレンスに関する DUMP_LIMIT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の管理リファレンスの証跡として保存して根拠にする。
    - C. DUMP_LIMIT の変更点を出力本文から切り離して置換分離の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換分離の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では DUMP_LIMIT は「DUMP_LIMIT の状態と出力メッセージを結び付ける置換分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では DUMP_LIMIT の出力行と DSI633I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では DUMP_LIMIT を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DUMP_SCOPE {#c32-i3994}
*分類: 管理リファレンス*  ・  難易度: 中級

DUMP_SCOPEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.533) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.533)

??? question "確認問題（1問）"
    **問題.** 終端分離の管理リファレンスに関係する DUMP_SCOPE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端分離の点検結果を残す。 ✅
    - B. DUMP_SCOPE の名称と担当者名のみを残して終端分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では DUMP_SCOPE は「DUMP_SCOPE の用途をネットビューの表示で確認する終端分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの DUMP_SCOPE と DSI633I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では DUMP_SCOPE を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DVIPA.INTDVCONN {#c32-i3995}
*分類: 管理リファレンス*  ・  難易度: 中級

DVIPA.INTDVCONNは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.104) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.104)

??? question "確認問題（1問）"
    **問題.** 探索分離の管理リファレンスで DVIPA.INTDVCONN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DVIPA.INTDVCONN の出力を取らず探索分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索分離で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では DVIPA.INTDVCONN は「探索分離の管理リファレンスに関係する定義値と表示行を照合する探索分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では DVIPA.INTDVCONN の属性行と DSI633I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では DVIPA.INTDVCONN を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DVIPA.INTDVDEF {#c32-i3996}
*分類: 管理リファレンス*  ・  難易度: 中級

DVIPA.INTDVDEFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.104) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.104)

??? question "確認問題（1問）"
    **問題.** 上書分離の管理リファレンスでネットビューの運用確認を行います。DVIPA.INTDVDEF の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書分離の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書分離の確認値として扱う。 ✅
    - D. DVIPA.INTDVDEF の属性行を読まず上書分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では DVIPA.INTDVDEF は「IBM Z NetViewで DVIPA.INTDVDEF の扱いを記録する上書分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では DVIPA.INTDVDEF の表示結果と DSI633I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では DVIPA.INTDVDEF の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DVIPA.INTDVROUT {#c32-i3997}
*分類: 管理リファレンス*  ・  難易度: 中級

DVIPA.INTDVROUTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.105) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.105)

??? question "確認問題（1問）"
    **問題.** 出力分離の管理リファレンスに関する DVIPA.INTDVROUT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離の管理リファレンスの証跡として保存して根拠にする。
    - C. DVIPA.INTDVROUT の変更点を出力本文から切り離して出力分離の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力分離の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では DVIPA.INTDVROUT は「DVIPA.INTDVROUT の状態と出力メッセージを結び付ける出力分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では DVIPA.INTDVROUT の出力行と DSI633I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では DVIPA.INTDVROUT を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### DVIPA.INTDVTAD {#c32-i3998}
*分類: 管理リファレンス*  ・  難易度: 中級

DVIPA.INTDVTADは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.103) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.103)

??? question "確認問題（1問）"
    **問題.** 条件分離の管理リファレンスに関係する DVIPA.INTDVTAD の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を条件分離で確認する。 ✅
    - B. DVIPA.INTDVTAD の名称と担当者名のみを残して条件分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では DVIPA.INTDVTAD は「DVIPA.INTDVTAD の用途をネットビューの表示で確認する条件分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM Z NetViewの DVIPA.INTDVTAD と DSI633I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では DVIPA.INTDVTAD を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EMAAUTO {#c32-i3999}
*分類: 管理リファレンス*  ・  難易度: 中級

EMAAUTOは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.110) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.110)

??? question "確認問題（1問）"
    **問題.** 区切分離の管理リファレンスで EMAAUTO の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EMAAUTO の出力を取らず区切分離の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、区切分離の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して区切分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では EMAAUTO は「区切分離の管理リファレンスに関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では EMAAUTO の属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では EMAAUTO を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### END {#c32-i4000}
*分類: 管理リファレンス*  ・  難易度: 中級

ENDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.328) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.328)

??? question "確認問題（1問）"
    **問題.** 範囲分離の管理リファレンスでネットビューの運用確認を行います。END の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲分離の確認記録にまとめる。 ✅
    - D. END の属性行を読まず範囲分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では END は「IBM Z NetViewで END の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では END の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では END の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ENVIRON AIP {#c32-i4001}
*分類: 管理リファレンス*  ・  難易度: 中級

ENVIRON AIPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.422) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.422)

??? question "確認問題（1問）"
    **問題.** 比較分離の管理リファレンスで ENVIRON AIP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ENVIRON AIP の出力を取らず比較分離の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、比較分離の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して比較分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では ENVIRON AIP は「比較分離の管理リファレンスに関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では ENVIRON AIP の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では ENVIRON AIP を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ENVIRON DDF {#c32-i4002}
*分類: 管理リファレンス*  ・  難易度: 中級

ENVIRON DDFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.423) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.423)

??? question "確認問題（1問）"
    **問題.** 順序分離の管理リファレンスでネットビューの運用確認を行います。ENVIRON DDF の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序分離として引き継ぐ。 ✅
    - D. ENVIRON DDF の属性行を読まず順序分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では ENVIRON DDF は「IBM Z NetViewで ENVIRON DDF の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では ENVIRON DDF の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では ENVIRON DDF の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ENVIRON EXIT {#c32-i4003}
*分類: 管理リファレンス*  ・  難易度: 上級

ENVIRON EXITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.425) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.425)

??? question "確認問題（1問）"
    **問題.** 値域分離の管理リファレンスに関する ENVIRON EXIT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離の管理リファレンスの証跡として保存して根拠にする。
    - C. ENVIRON EXIT の変更点を出力本文から切り離して値域分離の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域分離の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では ENVIRON EXIT は「ENVIRON EXIT の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では ENVIRON EXIT の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では ENVIRON EXIT を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ENVIRON RACF {#c32-i4004}
*分類: 管理リファレンス*  ・  難易度: 中級

ENVIRON RACFは、Tivoli NetView z/OS 自動化の管理リファレンスで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Administration Reference (p.426) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.426)

??? question "確認問題（1問）"
    **問題.** 警告分離の管理リファレンスに関係する ENVIRON RACF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告分離の点検結果を残す。 ✅
    - B. ENVIRON RACF の名称と担当者名のみを残して警告分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では ENVIRON RACF は「ENVIRON RACF の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの ENVIRON RACF と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では ENVIRON RACF を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ENVIRON SETUP {#c32-i4005}
*分類: 管理リファレンス*  ・  難易度: 中級

ENVIRON SETUPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.428) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.428)

??? question "確認問題（1問）"
    **問題.** 復旧分離の管理リファレンスで ENVIRON SETUP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ENVIRON SETUP の出力を取らず復旧分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧分離で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では ENVIRON SETUP は「復旧分離の管理リファレンスに関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では ENVIRON SETUP の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では ENVIRON SETUP を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ENVIRON TIMEOUT {#c32-i4006}
*分類: 管理リファレンス*  ・  難易度: 中級

ENVIRON TIMEOUTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.431) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.431)

??? question "確認問題（1問）"
    **問題.** 監査分離の管理リファレンスでネットビューの運用確認を行います。ENVIRON TIMEOUT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査分離の確認値として扱う。 ✅
    - D. ENVIRON TIMEOUT の属性行を読まず監査分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では ENVIRON TIMEOUT は「IBM Z NetViewで ENVIRON TIMEOUT の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では ENVIRON TIMEOUT の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では ENVIRON TIMEOUT の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ERCVCFG {#c32-i4007}
*分類: 管理リファレンス*  ・  難易度: 中級

ERCVCFGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.508) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.508)

??? question "確認問題（1問）"
    **問題.** 変更分離の管理リファレンスに関する ERCVCFG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離の管理リファレンスの証跡として保存して根拠にする。
    - C. ERCVCFG の変更点を出力本文から切り離して変更分離の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更分離の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では ERCVCFG は「ERCVCFG の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では ERCVCFG の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では ERCVCFG を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXTEND_HEAP_SIZE {#c32-i4008}
*分類: 管理リファレンス*  ・  難易度: 中級

EXTEND_HEAP_SIZEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.534) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.534)

??? question "確認問題（1問）"
    **問題.** 呼出読解の管理リファレンスでネットビューの運用確認を行います。EXTEND_HEAP_SIZE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出読解の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出読解の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出読解の確認記録にまとめる。 ✅
    - D. EXTEND_HEAP_SIZE の属性行を読まず呼出読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では EXTEND_HEAP_SIZE は「IBM Z NetViewで EXTEND_HEAP_SIZE の扱いを記録する呼出読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では EXTEND_HEAP_SIZE の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では EXTEND_HEAP_SIZE の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EZLTLOG {#c32-i4009}
*分類: 管理リファレンス*  ・  難易度: 中級

EZLTLOGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.433) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.433)

??? question "確認問題（1問）"
    **問題.** 置換読解の管理リファレンスに関する EZLTLOG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解の管理リファレンスの証跡として保存して根拠にする。
    - C. EZLTLOG の変更点を出力本文から切り離して置換読解の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換読解の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では EZLTLOG は「EZLTLOG の状態と出力メッセージを結び付ける置換読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では EZLTLOG の出力行と DSI633I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では EZLTLOG を IBM Z NetViewの確認記録に残し、対象名は置換読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Enterpriseoid {#c32-i4010}
*分類: 管理リファレンス*  ・  難易度: 中級

Enterpriseoidは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.507) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.507)

??? question "確認問題（1問）"
    **問題.** 記録分離の管理リファレンスに関係する Enterpriseoidの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録分離の結果として保存する。 ✅
    - B. Enterpriseoidの名称と担当者名のみを残して記録分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では Enterpriseoid は「Enterpriseoidの用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの Enterpriseoidと DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では Enterpriseoidを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Event/Automation Service Definition Statements {#c32-i4011}
*分類: 管理リファレンス*  ・  難易度: 上級

Event/Automation Service Definition Statementsは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.495) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.495)

??? question "確認問題（1問）"
    **問題.** 構文読解のEvent/Automation Service Definition Statementsに関係する Event 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を構文読解で確認する。 ✅
    - B. Event 属性の名称と担当者名のみを残して構文読解のEvent/Automation Service Definition Statementsの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解のEvent/Automation Service Definition Statementsを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解のEvent/Automation Service Definition Statementsの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では Event 属性 は「Event 属性の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewの Event 属性と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では Event 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EventMaxSize {#c32-i4012}
*分類: 管理リファレンス*  ・  難易度: 中級

EventMaxSizeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.509) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.509)

??? question "確認問題（1問）"
    **問題.** 展開読解の管理リファレンスで EventMaxSizeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EventMaxSizeの出力を取らず展開読解の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、展開読解の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して展開読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では EventMaxSize は「展開読解の管理リファレンスに関係する定義値と表示行を照合する展開読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では EventMaxSizeの属性行と DSI633I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では EventMaxSizeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### F (Filter) {#c32-i4013}
*分類: 管理リファレンス*  ・  難易度: 中級

F (Filter)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.328) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.328)

??? question "確認問題（1問）"
    **問題.** 終端読解の管理リファレンスに関係する F (Filter)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端読解の結果として保存する。 ✅
    - B. F (Filter)の名称と担当者名のみを残して終端読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では F (Filter) は「F (Filter)の用途をネットビューの表示で確認する終端読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM Z NetViewの F (Filter)と DSI633I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では F (Filter)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### FORWARD FOCALPT {#c32-i4014}
*分類: 管理リファレンス*  ・  難易度: 中級

FORWARD FOCALPTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.434) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.434)

??? question "確認問題（1問）"
    **問題.** 区切読解の管理リファレンスで FORWARD FOCALPT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FORWARD FOCALPT の出力を取らず区切読解の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切読解で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して区切読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では FORWARD FOCALPT は「区切読解の管理リファレンスに関係する定義値と表示行を照合する区切読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では FORWARD FOCALPT の属性行と DSI633I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では FORWARD FOCALPT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### FULLSESS {#c32-i4015}
*分類: 管理リファレンス*  ・  難易度: 中級

FULLSESSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.435) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.435)

??? question "確認問題（1問）"
    **問題.** 範囲読解の管理リファレンスでネットビューの運用確認を行います。FULLSESS の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲読解の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲読解の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲読解の確認値として扱う。 ✅
    - D. FULLSESS の属性行を読まず範囲読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では FULLSESS は「IBM Z NetViewで FULLSESS の扱いを記録する範囲読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では FULLSESS の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では FULLSESS の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### FailbackValue {#c32-i4016}
*分類: 管理リファレンス*  ・  難易度: 中級

FailbackValueは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.509) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.509)

??? question "確認問題（1問）"
    **問題.** 探索読解の管理リファレンスで FailbackValueの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FailbackValueの出力を取らず探索読解の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、探索読解の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して探索読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では FailbackValue は「探索読解の管理リファレンスに関係する定義値と表示行を照合する探索読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では FailbackValueの属性行と DSI633I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では FailbackValueを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filter {#c32-i4017}
*分類: 管理リファレンス*  ・  難易度: 中級

Filterは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.510) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.510)

??? question "確認問題（1問）"
    **問題.** 上書読解の管理リファレンスでネットビューの運用確認を行います。Filterの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書読解の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書読解の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書読解として引き継ぐ。 ✅
    - D. Filterの属性行を読まず上書読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Filter は「IBM Z NetViewで Filterの扱いを記録する上書読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Filterの表示結果と DSI633I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では Filterの使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### FilterCache {#c32-i4018}
*分類: 管理リファレンス*  ・  難易度: 中級

FilterCacheは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.511) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.511)

??? question "確認問題（1問）"
    **問題.** 出力読解の管理リファレンスに関する FilterCacheの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解の管理リファレンスの証跡として保存して根拠にする。
    - C. FilterCacheの変更点を出力本文から切り離して出力読解の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力読解の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では FilterCache は「FilterCacheの状態と出力メッセージを結び付ける出力読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では FilterCacheの出力行と DSI633I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では FilterCacheを IBM Z NetViewの確認記録に残し、対象名は出力読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### FilterMode {#c32-i4019}
*分類: 管理リファレンス*  ・  難易度: 中級

FilterModeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.511) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.511)

??? question "確認問題（1問）"
    **問題.** 条件読解の管理リファレンスに関係する FilterModeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件読解の点検結果を残す。 ✅
    - B. FilterModeの名称と担当者名のみを残して条件読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では FilterMode は「FilterModeの用途をネットビューの表示で確認する条件読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM Z NetViewの FilterModeと DSI633I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では FilterModeを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### GHB.TCPANAME {#c32-i4020}
*分類: 管理リファレンス*  ・  難易度: 中級

GHB.TCPANAMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.116) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.116)

??? question "確認問題（1問）"
    **問題.** 記録読解の管理リファレンスに関係する GHB.TCPANAME の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を記録読解で確認する。 ✅
    - B. GHB.TCPANAME の名称と担当者名のみを残して記録読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では GHB.TCPANAME は「GHB.TCPANAME の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの GHB.TCPANAME と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では GHB.TCPANAME を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### GMTOFFSET {#c32-i4021}
*分類: 管理リファレンス*  ・  難易度: 中級

GMTOFFSETは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.551) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.551)

??? question "確認問題（1問）"
    **問題.** 比較読解の管理リファレンスで GMTOFFSET の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. GMTOFFSET の出力を取らず比較読解の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較読解の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では GMTOFFSET は「比較読解の管理リファレンスに関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では GMTOFFSET の属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では GMTOFFSET を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### GROUP {#c32-i4022}
*分類: 管理リファレンス*  ・  難易度: 中級

GROUPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.492) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.492)

??? question "確認問題（1問）"
    **問題.** 値域読解の管理リファレンスに関する GROUP の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解の管理リファレンスの証跡として保存して根拠にする。
    - C. GROUP の変更点を出力本文から切り離して値域読解の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域読解の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では GROUP は「GROUP の状態と出力メッセージを結び付ける値域読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では GROUP の出力行と DSI633I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では GROUP を IBM Z NetViewの確認記録に残し、対象名は値域読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Graphic Monitor Facility Host Subsystem Statements {#c32-i4023}
*分類: 管理リファレンス*  ・  難易度: 中級

Graphic Monitor Facility Host Subsystem Statementsは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.549) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.549)

??? question "確認問題（1問）"
    **問題.** 順序読解の管理リファレンスでネットビューの運用確認を行います。Graphic 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序読解の確認記録にまとめる。 ✅
    - D. Graphic 機能の属性行を読まず順序読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Graphic 機能 は「IBM Z NetViewで Graphic 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Graphic 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Graphic 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### HARDCOPY {#c32-i4024}
*分類: 管理リファレンス*  ・  難易度: 中級

HARDCOPYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.117) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.117)

??? question "確認問題（1問）"
    **問題.** 警告読解の管理リファレンスに関係する HARDCOPY の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告読解の結果として保存する。 ✅
    - B. HARDCOPY の名称と担当者名のみを残して警告読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では HARDCOPY は「HARDCOPY の用途をネットビューの表示で確認する警告読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの HARDCOPY と DSI633I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では HARDCOPY を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### HELD {#c32-i4025}
*分類: 管理リファレンス*  ・  難易度: 中級

HELDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.332) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.332)

??? question "確認問題（1問）"
    **問題.** 復旧読解の管理リファレンスで HELD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. HELD の出力を取らず復旧読解の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧読解の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では HELD は「復旧読解の管理リファレンスに関係する定義値と表示行を照合する復旧読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では HELD の属性行と DSI633I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では HELD を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### HLLENV {#c32-i4026}
*分類: 管理リファレンス*  ・  難易度: 中級

HLLENVは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.118) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.118)

??? question "確認問題（1問）"
    **問題.** 監査読解の管理リファレンスでネットビューの運用確認を行います。HLLENV の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査読解の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査読解として引き継ぐ。 ✅
    - D. HLLENV の属性行を読まず監査読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では HLLENV は「IBM Z NetViewで HLLENV の扱いを記録する監査読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では HLLENV の表示結果と DSI633I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では HLLENV の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### HOLDPCNT {#c32-i4027}
*分類: 管理リファレンス*  ・  難易度: 中級

HOLDPCNTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.333) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.333)

??? question "確認問題（1問）"
    **問題.** 変更読解の管理リファレンスに関する HOLDPCNT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解の管理リファレンスの証跡として保存して根拠にする。
    - C. HOLDPCNT の変更点を出力本文から切り離して変更読解の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更読解の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では HOLDPCNT は「HOLDPCNT の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では HOLDPCNT の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では HOLDPCNT を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### HOLDWARN {#c32-i4028}
*分類: 管理リファレンス*  ・  難易度: 中級

HOLDWARNは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.334) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.334)

??? question "確認問題（1問）"
    **問題.** 構文検分の管理リファレンスに関係する HOLDWARN の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文検分の点検結果を残す。 ✅
    - B. HOLDWARN の名称と担当者名のみを残して構文検分の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では HOLDWARN は「HOLDWARN の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの HOLDWARN と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では HOLDWARN を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Hostname {#c32-i4029}
*分類: 管理リファレンス*  ・  難易度: 中級

Hostnameは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.512) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.512)

??? question "確認問題（1問）"
    **問題.** 展開検分の管理リファレンスで Hostnameの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Hostnameの出力を取らず展開検分の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開検分で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して展開検分の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Hostname は「展開検分の管理リファレンスに関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Hostnameの属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Hostnameを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How to Use the NetView Definition Statement Reference {#c32-i4030}
*分類: 管理リファレンス*  ・  難易度: 中級

How to Use the NetView Definition Statement Referenceは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出検分の管理リファレンスでネットビューの運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検分の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出検分の確認値として扱う。 ✅
    - D. How 機能の属性行を読まず呼出検分の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では How 機能 は「IBM Z NetViewで How 機能の扱いを記録する呼出検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では How 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では How 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### IDS.Attack_Cmd {#c32-i4031}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Attack_Cmdは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.120) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.120)

??? question "確認問題（1問）"
    **問題.** 終端検分の管理リファレンスに関係する IDS.Attack_Cmdの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を終端検分で確認する。 ✅
    - B. IDS.Attack_Cmdの名称と担当者名のみを残して終端検分の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では IDS.Attack_Cmd は「IDS.Attack_Cmdの用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの IDS.Attack_Cmdと DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では IDS.Attack_Cmdを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Attack_CmdType {#c32-i4032}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Attack_CmdTypeは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.121) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.121)

??? question "確認問題（1問）"
    **問題.** 探索検分の管理リファレンスで IDS.Attack_CmdTypeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.Attack_CmdTypeの出力を取らず探索検分の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索検分の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索検分の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では IDS.Attack_CmdType は「探索検分の管理リファレンスに関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では IDS.Attack_CmdTypeの属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では IDS.Attack_CmdTypeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Auto_Intvl {#c32-i4033}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Auto_Intvlは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.122) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.122)

??? question "確認問題（1問）"
    **問題.** 上書検分の管理リファレンスでネットビューの運用確認を行います。IDS.Auto_Intvlの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書検分の確認記録にまとめる。 ✅
    - D. IDS.Auto_Intvlの属性行を読まず上書検分の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では IDS.Auto_Intvl は「IBM Z NetViewで IDS.Auto_Intvlの扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では IDS.Auto_Intvlの表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では IDS.Auto_Intvlの使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Auto_Thresh {#c32-i4034}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Auto_Threshは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.122) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.122)

??? question "確認問題（1問）"
    **問題.** 出力検分の管理リファレンスに関する IDS.Auto_Threshの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS.Auto_Threshの変更点を出力本文から切り離して出力検分の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力検分の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では IDS.Auto_Thresh は「IDS.Auto_Threshの状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では IDS.Auto_Threshの出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では IDS.Auto_Threshを IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.CONSOLEMSG {#c32-i4035}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.CONSOLEMSGは、Tivoli NetView z/OS 自動化の管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Administration Reference (p.126) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.126)

??? question "確認問題（1問）"
    **問題.** 比較検分の管理リファレンスで IDS.CONSOLEMSG の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.CONSOLEMSG の出力を取らず比較検分の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較検分で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して比較検分の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では IDS.CONSOLEMSG は「比較検分の管理リファレンスに関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では IDS.CONSOLEMSG の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では IDS.CONSOLEMSG を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.ClearStat_Day {#c32-i4036}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.ClearStat_Dayは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.123) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.123)

??? question "確認問題（1問）"
    **問題.** 条件検分の管理リファレンスに関係する IDS.ClearStat_Dayの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件検分の結果として保存する。 ✅
    - B. IDS.ClearStat_Dayの名称と担当者名のみを残して条件検分の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検分の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では IDS.ClearStat_Day は「IDS.ClearStat_Dayの用途をネットビューの表示で確認する条件検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの IDS.ClearStat_Dayと DSI633I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では IDS.ClearStat_Dayを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.ClearStat_Inform {#c32-i4037}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.ClearStat_Informは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.124) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.124)

??? question "確認問題（1問）"
    **問題.** 区切検分の管理リファレンスで IDS 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS 属性の出力を取らず区切検分の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切検分の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切検分の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では IDS 属性 は「区切検分の管理リファレンスに関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では IDS 属性の属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では IDS 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.ClearStat_Log {#c32-i4038}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.ClearStat_Logは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.125) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.125)

??? question "確認問題（1問）"
    **問題.** 範囲検分の管理リファレンスでネットビューの運用確認を行います。IDS.ClearStat_Logの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲検分として引き継ぐ。 ✅
    - D. IDS.ClearStat_Logの属性行を読まず範囲検分の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では IDS.ClearStat_Log は「IBM Z NetViewで IDS.ClearStat_Logの扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では IDS.ClearStat_Logの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では IDS.ClearStat_Logの使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.ClearStat_Log_File {#c32-i4039}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.ClearStat_Log_Fileは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.125) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.125)

??? question "確認問題（1問）"
    **問題.** 優先検分の管理リファレンスに関する IDS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS 属性の変更点を出力本文から切り離して優先検分の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先検分の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では IDS 属性 は「IDS 属性の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では IDS 属性の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では IDS 属性を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.ClearStat_Time {#c32-i4040}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.ClearStat_Timeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.126) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.126)

??? question "確認問題（1問）"
    **問題.** 記録検分の管理リファレンスに関係する IDS.ClearStat_Timeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、記録検分の点検結果を残す。 ✅
    - B. IDS.ClearStat_Timeの名称と担当者名のみを残して記録検分の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では IDS.ClearStat_Time は「IDS.ClearStat_Timeの用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewの IDS.ClearStat_Timeと DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では IDS.ClearStat_Timeを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.DSIPARM {#c32-i4041}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.DSIPARMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.127) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.127)

??? question "確認問題（1問）"
    **問題.** 順序検分の管理リファレンスでネットビューの運用確認を行います。IDS.DSIPARM の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検分の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序検分の確認値として扱う。 ✅
    - D. IDS.DSIPARM の属性行を読まず順序検分の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では IDS.DSIPARM は「IBM Z NetViewで IDS.DSIPARM の扱いを記録する順序検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では IDS.DSIPARM の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では IDS.DSIPARM の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Event_Inform {#c32-i4042}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Event_Informは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.127) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.127)

??? question "確認問題（1問）"
    **問題.** 値域検分の管理リファレンスに関する IDS.Event_Informの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS.Event_Informの変更点を出力本文から切り離して値域検分の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域検分の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では IDS.Event_Inform は「IDS.Event_Informの状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では IDS.Event_Informの出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では IDS.Event_Informを IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Event_Limit {#c32-i4043}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Event_Limitは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.128) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.128)

??? question "確認問題（1問）"
    **問題.** 警告検分の管理リファレンスに関係する IDS.Event_Limitの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を警告検分で確認する。 ✅
    - B. IDS.Event_Limitの名称と担当者名のみを残して警告検分の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検分の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検分の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では IDS.Event_Limit は「IDS.Event_Limitの用途をネットビューの表示で確認する警告検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM Z NetViewの IDS.Event_Limitと DSI633I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では IDS.Event_Limitを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Event_Log {#c32-i4044}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Event_Logは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.128) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.128)

??? question "確認問題（1問）"
    **問題.** 復旧検分の管理リファレンスで IDS.Event_Logの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.Event_Logの出力を取らず復旧検分の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、復旧検分の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では IDS.Event_Log は「復旧検分の管理リファレンスに関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では IDS.Event_Logの属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では IDS.Event_Logを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Event_Log_File {#c32-i4045}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Event_Log_Fileは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.129) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.129)

??? question "確認問題（1問）"
    **問題.** 監査検分の管理リファレンスでネットビューの運用確認を行います。IDS.Event_Log_Fileの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検分の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査検分の確認記録にまとめる。 ✅
    - D. IDS.Event_Log_Fileの属性行を読まず監査検分の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では IDS.Event_Log_File は「IBM Z NetViewで IDS.Event_Log_Fileの扱いを記録する監査検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では IDS.Event_Log_Fileの表示結果と DSI633I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では IDS.Event_Log_Fileの使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Flood_Cmd {#c32-i4046}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Flood_Cmdは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.129) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.129)

??? question "確認問題（1問）"
    **問題.** 変更検分の管理リファレンスに関する IDS.Flood_Cmdの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検分の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS.Flood_Cmdの変更点を出力本文から切り離して変更検分の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更検分の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では IDS.Flood_Cmd は「IDS.Flood_Cmdの状態と出力メッセージを結び付ける変更検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では IDS.Flood_Cmdの出力行と DSI633I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では IDS.Flood_Cmdを IBM Z NetViewの確認記録に残し、対象名は変更検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Flood_CmdType {#c32-i4047}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Flood_CmdTypeは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.130) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.130)

??? question "確認問題（1問）"
    **問題.** 構文確認の管理リファレンスに関係する IDS.Flood_CmdTypeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文確認で再確認できる形にする。 ✅
    - B. IDS.Flood_CmdTypeの名称と担当者名のみを残して構文確認の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文確認の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文確認の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では IDS.Flood_CmdType は「IDS.Flood_CmdTypeの用途をネットビューの表示で確認する構文確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Z NetViewの IDS.Flood_CmdTypeと DSI633I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では IDS.Flood_CmdTypeを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Report_Cmd {#c32-i4048}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Report_Cmdは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.132) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.132)

??? question "確認問題（1問）"
    **問題.** 呼出確認の管理リファレンスでネットビューの運用確認を行います。IDS.Report_Cmdの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出確認の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出確認の根拠を固定する。 ✅
    - D. IDS.Report_Cmdの属性行を読まず呼出確認の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では IDS.Report_Cmd は「IBM Z NetViewで IDS.Report_Cmdの扱いを記録する呼出確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では IDS.Report_Cmdの表示結果と DSI633I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では IDS.Report_Cmdの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Report_CmdType {#c32-i4049}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Report_CmdTypeは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.133) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.133)

??? question "確認問題（1問）"
    **問題.** 置換確認の管理リファレンスに関する IDS.Report_CmdTypeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS.Report_CmdTypeの変更点を出力本文から切り離して置換確認の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を置換確認で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では IDS.Report_CmdType は「IDS.Report_CmdTypeの状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では IDS.Report_CmdTypeの出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では IDS.Report_CmdTypeを IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Report_Inform {#c32-i4050}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Report_Informは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.134) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.134)

??? question "確認問題（1問）"
    **問題.** 終端確認の管理リファレンスに関係する IDS.Report_Informの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、終端確認の証跡として残す。 ✅
    - B. IDS.Report_Informの名称と担当者名のみを残して終端確認の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端確認の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端確認の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では IDS.Report_Inform は「IDS.Report_Informの用途をネットビューの表示で確認する終端確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Z NetViewの IDS.Report_Informと DSI633I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では IDS.Report_Informを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Report_Log {#c32-i4051}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Report_Logは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.134) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.134)

??? question "確認問題（1問）"
    **問題.** 探索確認の管理リファレンスで IDS.Report_Logの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.Report_Logの出力を取らず探索確認の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索確認の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して探索確認の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では IDS.Report_Log は「探索確認の管理リファレンスに関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では IDS.Report_Logの属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では IDS.Report_Logを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Report_Log_File {#c32-i4052}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Report_Log_Fileは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.135) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.135)

??? question "確認問題（1問）"
    **問題.** 上書確認の管理リファレンスでネットビューの運用確認を行います。IDS 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書確認の根拠にする。 ✅
    - D. IDS 属性の属性行を読まず上書確認の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では IDS 属性 は「IBM Z NetViewで IDS 属性の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では IDS 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では IDS 属性の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.SYSLOGMSG {#c32-i4053}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.SYSLOGMSGは、Tivoli NetView z/OS 自動化の管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Administration Reference (p.138) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.138)

??? question "確認問題（1問）"
    **問題.** 区切確認の管理リファレンスで IDS.SYSLOGMSG の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.SYSLOGMSG の出力を取らず区切確認の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切確認として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して区切確認の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では IDS.SYSLOGMSG は「区切確認の管理リファレンスに関係する定義値と表示行を照合する区切確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では IDS.SYSLOGMSG の属性行と DSI633I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では IDS.SYSLOGMSG を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Scan_Cmd {#c32-i4054}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Scan_Cmdは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.135) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.135)

??? question "確認問題（1問）"
    **問題.** 出力確認の管理リファレンスに関する IDS.Scan_Cmdの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力確認の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS.Scan_Cmdの変更点を出力本文から切り離して出力確認の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、出力確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では IDS.Scan_Cmd は「IDS.Scan_Cmdの状態と出力メッセージを結び付ける出力確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では IDS.Scan_Cmdの出力行と DSI633I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では IDS.Scan_Cmdを IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.Scan_CmdType {#c32-i4055}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.Scan_CmdTypeは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.136) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.136)

??? question "確認問題（1問）"
    **問題.** 条件確認の管理リファレンスに関係する IDS.Scan_CmdTypeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、条件確認の採否を説明欄に結び付ける。 ✅
    - B. IDS.Scan_CmdTypeの名称と担当者名のみを残して条件確認の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件確認の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件確認の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では IDS.Scan_CmdType は「IDS.Scan_CmdTypeの用途をネットビューの表示で確認する条件確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Z NetViewの IDS.Scan_CmdTypeと DSI633I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では IDS.Scan_CmdTypeを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.TCP_Cmd {#c32-i4056}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.TCP_Cmdは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.138) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.138)

??? question "確認問題（1問）"
    **問題.** 範囲確認の管理リファレンスでネットビューの運用確認を行います。IDS.TCP_Cmdの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲確認の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲確認の確認にする。 ✅
    - D. IDS.TCP_Cmdの属性行を読まず範囲確認の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では IDS.TCP_Cmd は「IBM Z NetViewで IDS.TCP_Cmdの扱いを記録する範囲確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では IDS.TCP_Cmdの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では IDS.TCP_Cmdの使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.TCP_CmdType {#c32-i4057}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.TCP_CmdTypeは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.139) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.139)

??? question "確認問題（1問）"
    **問題.** 優先確認の管理リファレンスに関する IDS.TCP_CmdTypeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先確認の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の管理リファレンスの証跡として保存して根拠にする。
    - C. IDS.TCP_CmdTypeの変更点を出力本文から切り離して優先確認の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、優先確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では IDS.TCP_CmdType は「IDS.TCP_CmdTypeの状態と出力メッセージを結び付ける優先確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では IDS.TCP_CmdTypeの出力行と DSI633I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では IDS.TCP_CmdTypeを IBM Z NetViewの確認記録に残し、対象名は優先確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.UDP_Cmd {#c32-i4058}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.UDP_Cmdは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.140) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.140)

??? question "確認問題（1問）"
    **問題.** 記録確認の管理リファレンスに関係する IDS.UDP_Cmdの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録確認で再確認できる形にする。 ✅
    - B. IDS.UDP_Cmdの名称と担当者名のみを残して記録確認の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録確認の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では IDS.UDP_Cmd は「IDS.UDP_Cmdの用途をネットビューの表示で確認する記録確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewの IDS.UDP_Cmdと DSI633I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では IDS.UDP_Cmdを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.UDP_CmdType {#c32-i4059}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.UDP_CmdTypeは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.140) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.140)

??? question "確認問題（1問）"
    **問題.** 比較確認の管理リファレンスで IDS.UDP_CmdTypeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.UDP_CmdTypeの出力を取らず比較確認の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較確認の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して比較確認の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では IDS.UDP_CmdType は「比較確認の管理リファレンスに関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では IDS.UDP_CmdTypeの属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では IDS.UDP_CmdTypeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IDS.probeid {#c32-i4060}
*分類: 管理リファレンス*  ・  難易度: 中級

IDS.probeidは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.131) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.131)

??? question "確認問題（1問）"
    **問題.** 展開確認の管理リファレンスで IDS.probeidの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IDS.probeidの出力を取らず展開確認の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開確認の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して展開確認の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では IDS.probeid は「展開確認の管理リファレンスに関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では IDS.probeidの属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では IDS.probeidを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IMDAREA {#c32-i4061}
*分類: 管理リファレンス*  ・  難易度: 中級

IMDAREAは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.336) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.336)

??? question "確認問題（1問）"
    **問題.** 順序確認の管理リファレンスでネットビューの運用確認を行います。IMDAREA の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序確認の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序確認の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序確認の根拠を固定する。 ✅
    - D. IMDAREA の属性行を読まず順序確認の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では IMDAREA は「IBM Z NetViewで IMDAREA の扱いを記録する順序確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では IMDAREA の表示結果と DSI633I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では IMDAREA の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INDENT {#c32-i4062}
*分類: 管理リファレンス*  ・  難易度: 中級

INDENTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.340) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.340)

??? question "確認問題（1問）"
    **問題.** 値域確認の管理リファレンスに関する INDENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の管理リファレンスの証跡として保存して根拠にする。
    - C. INDENT の変更点を出力本文から切り離して値域確認の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を値域確認で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では INDENT は「INDENT の状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では INDENT の出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では INDENT を IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INFORM {#c32-i4063}
*分類: 管理リファレンス*  ・  難易度: 中級

INFORMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.493) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.493)

??? question "確認問題（1問）"
    **問題.** 警告確認の管理リファレンスに関係する INFORM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、警告確認の証跡として残す。 ✅
    - B. INFORM の名称と担当者名のみを残して警告確認の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では INFORM は「INFORM の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの INFORM と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では INFORM を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.CONNSEC {#c32-i4064}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.CONNSECは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.142) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.142)

??? question "確認問題（1問）"
    **問題.** 監査確認の管理リファレンスでネットビューの運用確認を行います。INIT.CONNSEC の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査確認の根拠にする。 ✅
    - D. INIT.CONNSEC の属性行を読まず監査確認の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では INIT.CONNSEC は「IBM Z NetViewで INIT.CONNSEC の扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では INIT.CONNSEC の表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では INIT.CONNSEC の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.DVIPASTATS {#c32-i4065}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.DVIPASTATSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.142) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.142)

??? question "確認問題（1問）"
    **問題.** 変更確認の管理リファレンスに関する INIT.DVIPASTATS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更確認の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の管理リファレンスの証跡として保存して根拠にする。
    - C. INIT.DVIPASTATS の変更点を出力本文から切り離して変更確認の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、変更確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では INIT.DVIPASTATS は「INIT.DVIPASTATS の状態と出力メッセージを結び付ける変更確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では INIT.DVIPASTATS の出力行と DSI633I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では INIT.DVIPASTATS を IBM Z NetViewの確認記録に残し、対象名は変更確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.EMAAUTO {#c32-i4066}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.EMAAUTOは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.143) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.143)

??? question "確認問題（1問）"
    **問題.** 構文照合の管理リファレンスに関係する INIT.EMAAUTO の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、構文照合の採否を説明欄に結び付ける。 ✅
    - B. INIT.EMAAUTO の名称と担当者名のみを残して構文照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では INIT.EMAAUTO は「INIT.EMAAUTO の用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの INIT.EMAAUTO と DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では INIT.EMAAUTO を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.NRM {#c32-i4067}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.NRMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.144) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.144)

??? question "確認問題（1問）"
    **問題.** 展開照合の管理リファレンスで INIT.NRM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. INIT.NRM の出力を取らず展開照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開照合として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して展開照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では INIT.NRM は「展開照合の管理リファレンスに関係する定義値と表示行を照合する展開照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では INIT.NRM の属性行と DSI633I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では INIT.NRM を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.OPKT {#c32-i4068}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.OPKTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.144) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.144)

??? question "確認問題（1問）"
    **問題.** 呼出照合の管理リファレンスでネットビューの運用確認を行います。INIT.OPKT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出照合の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出照合の確認にする。 ✅
    - D. INIT.OPKT の属性行を読まず呼出照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では INIT.OPKT は「IBM Z NetViewで INIT.OPKT の扱いを記録する呼出照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では INIT.OPKT の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では INIT.OPKT の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.PKTS {#c32-i4069}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.PKTSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.145) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.145)

??? question "確認問題（1問）"
    **問題.** 置換照合の管理リファレンスに関する INIT.PKTS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の管理リファレンスの証跡として保存して根拠にする。
    - C. INIT.PKTS の変更点を出力本文から切り離して置換照合の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、置換照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では INIT.PKTS は「INIT.PKTS の状態と出力メッセージを結び付ける置換照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では INIT.PKTS の出力行と DSI633I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では INIT.PKTS を IBM Z NetViewの確認記録に残し、対象名は置換照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide


