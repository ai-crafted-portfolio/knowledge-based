---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (18/18)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > 自動化テーブル / 状態判定

### Using the Interfaces {#c32-i4717}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Using the Interfacesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換検査の自動化テーブル 状態判定に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検査の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換検査の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は置換検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Log Analysis Program {#c32-i4718}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Using the Log Analysis Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端検査の自動化テーブル 状態判定に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端検査の結果として保存する。 ✅
    - B. Using 機能の名称と担当者名のみを残して終端検査の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Message Suppression Sample Set {#c32-i4719}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Using the Message Suppression Sample Setは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検査の自動化テーブル 状態判定で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索検査の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、探索検査の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して探索検査の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では Using 機能 は「探索検査の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Policy API {#c32-i4720}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Using the Policy APIは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書検査の自動化テーブル 状態判定でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検査の自動化テーブル 状態判定を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書検査として引き継ぐ。 ✅
    - D. Using 機能の属性行を読まず上書検査の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する上書検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では Using 機能の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Sample Set for Automation {#c32-i4721}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Using the Sample Set for Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力検査の自動化テーブル 状態判定に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検査の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して出力検査の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力検査の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける出力検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### VTAM Message Suppression Criteria {#c32-i4722}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

VTAM Message Suppression Criteriaは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.476) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.476)

??? question "確認問題（1問）"
    **問題.** 範囲検査の自動化テーブル 状態判定でネットビューの運用確認を行います。VTAM 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検査の自動化テーブル 状態判定を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲検査の確認値として扱う。 ✅
    - D. VTAM 機能の属性行を読まず範囲検査の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では VTAM 機能 は「IBM Z NetViewで VTAM 機能の扱いを記録する範囲検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では VTAM 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では VTAM 機能の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### VTAM Message and Command Processing {#c32-i4723}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

VTAM Message and Command Processingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切検査の自動化テーブル 状態判定で VTAM 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VTAM 機能の出力を取らず区切検査の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切検査で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して区切検査の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では VTAM 機能 は「区切検査の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では VTAM 機能の属性行と DSI633I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では VTAM 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Verifying Commands Issued from RODM Methods {#c32-i4724}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Verifying Commands Issued from RODM Methodsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件検査の自動化テーブル 状態判定に関係する Verifying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件検査の点検結果を残す。 ✅
    - B. Verifying 機能の名称と担当者名のみを残して条件検査の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず条件検査の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では Verifying 機能 は「Verifying 機能の用途をネットビューの表示で確認する条件検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの Verifying 機能と EKG000I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では Verifying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### WHEN Statement {#c32-i4725}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

WHEN Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.141) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.141)

??? question "確認問題（1問）"
    **問題.** 復旧検査の自動化テーブル 状態判定で WHEN Statementの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. WHEN Statementの出力を取らず復旧検査の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧検査の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では WHEN Statement は「復旧検査の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では WHEN Statementの属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では WHEN Statementを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Waiting for a Specific Event {#c32-i4726}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Waiting for a Specific Eventは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先検査の自動化テーブル 状態判定に関する Waiting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Waiting 機能の変更点を出力本文から切り離して優先検査の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では Waiting 機能 は「Waiting 機能の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では Waiting 機能の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では Waiting 機能を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### What Are Installation Exits? {#c32-i4727}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

What Are Installation Exits?は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.289) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.289)

??? question "確認問題（1問）"
    **問題.** 記録検査の自動化テーブル 状態判定に関係する What 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を記録検査で確認する。 ✅
    - B. What 機能の名称と担当者名のみを残して記録検査の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では What 機能 は「What 機能の用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの What 機能と DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では What 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### What Does NetView Automation Mean? {#c32-i4728}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

What Does NetView Automation Mean?は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.37) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.37)

??? question "確認問題（1問）"
    **問題.** 比較検査の自動化テーブル 状態判定で What 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. What 機能の出力を取らず比較検査の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較検査の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較検査の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では What 機能 は「比較検査の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では What 機能の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では What 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### What Is the Automation Table? {#c32-i4729}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

What Is the Automation Table?は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検査の自動化テーブル 状態判定でネットビューの運用確認を行います。What 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査の自動化テーブル 状態判定を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序検査の確認記録にまとめる。 ✅
    - D. What 機能の属性行を読まず順序検査の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では What 機能 は「IBM Z NetViewで What 機能の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では What 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では What 機能の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### What Is the Command Revision Table? {#c32-i4730}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

What Is the Command Revision Table?は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域検査の自動化テーブル 状態判定に関する What 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. What 機能の変更点を出力本文から切り離して値域検査の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では What 機能 は「What 機能の状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では What 機能の出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では What 機能を IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### What Is the Message Revision Table? {#c32-i4731}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

What Is the Message Revision Table?は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告検査の自動化テーブル 状態判定に関係する What 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告検査の結果として保存する。 ✅
    - B. What 機能の名称と担当者名のみを残して警告検査の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検査の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では What 機能 は「What 機能の用途をネットビューの表示で確認する警告検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの What 機能と DSI633I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では What 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Writing Automation Table Statements to Automate MSUs {#c32-i4732}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Writing Automation Table Statements to Automate MSUsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更検査の自動化テーブル 状態判定に関する Writing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Writing 機能の変更点を出力本文から切り離して変更検査の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更検査の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では Writing 機能 は「Writing 機能の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では Writing 機能の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では Writing 機能を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Writing Automation Table Statements to Automate Messages {#c32-i4733}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Writing Automation Table Statements to Automate Messagesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査検査の自動化テーブル 状態判定でネットビューの運用確認を行います。Writing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査の自動化テーブル 状態判定を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査検査として引き継ぐ。 ✅
    - D. Writing 機能の属性行を読まず監査検査の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では Writing 機能 は「IBM Z NetViewで Writing 機能の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では Writing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では Writing 機能の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Writing Simple Command Procedures {#c32-i4734}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Writing Simple Command Proceduresは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.311) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.311)

??? question "確認問題（1問）"
    **問題.** 構文判定の自動化テーブル 状態判定に関係する Writing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文判定の点検結果を残す。 ✅
    - B. Writing 機能の名称と担当者名のみを残して構文判定の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では Writing 機能 は「Writing 機能の用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの Writing 機能と DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では Writing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide




## Tivoli NetView z/OS 自動化 > 自動化テーブル / 状態判定 > LOGSEQ

### LOGSEQ {#c32-i4735}
*分類: 自動化テーブル / 状態判定 > LOGSEQ*  ・  難易度: 上級

LOGSEQは、自動化テーブルで一致しなかったメッセージを順に記録するコマンド処理です。末尾にANYIDと組で置き、未自動化のメッセージを書き出します

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書整理のネットビューでネットビューの運用確認を行います。LOGSEQ の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理のネットビューを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理のネットビューを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書整理の確認値として扱う。 ✅
    - D. LOGSEQ の属性行を読まず上書整理のネットビューの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では LOGSEQ は「IBM Z NetViewで LOGSEQ の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では LOGSEQ の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では LOGSEQ の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > ANYID

### ANYID {#c32-i4736}
*分類: 自動化テーブル > ANYID*  ・  難易度: 中級

ANYIDは、自動化テーブルでメッセージIDの条件として任意のIDに一致させる特別な指定です。未自動化のメッセージをまとめて拾う総括処理に用います

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索判定のネットビューで ANYID の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ANYID の出力を取らず探索判定のネットビューの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索判定の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索判定のネットビューの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定のネットビューへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では ANYID は「探索判定のネットビューに関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では ANYID の属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では ANYID を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > CMD

### CMD {#c32-i4737}
*分類: 自動化テーブル > CMD*  ・  難易度: 初級

CMDは、自動化テーブルのEXECで実際に発行するコマンドの文字列を包む書き方です。丸括弧の中に対象のコマンドを引用符で与えます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録整理のネットビューに関係する CMD の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録整理の結果として保存する。 ✅
    - B. CMD の名称と担当者名のみを残して記録整理のネットビューの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理のネットビューを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理のネットビューの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では CMD は「CMD の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの CMD と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では CMD を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > CONTINUE

### CONTINUE {#c32-i4738}
*分類: 自動化テーブル > CONTINUE*  ・  難易度: 中級

CONTINUEは、自動化テーブルでアクション後にメッセージを後続のステートメントへ渡すかを制御する指定です。CONTINUE(Y)で照合を続け、Nで止めます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換判定のネットビューに関する CONTINUE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定のネットビューの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のネットビューの証跡として保存して根拠にする。
    - C. CONTINUE の変更点を出力本文から切り離して置換判定のネットビューの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では CONTINUE は「CONTINUE の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では CONTINUE の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では CONTINUE を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > EXEC

### EXEC {#c32-i4739}
*分類: 自動化テーブル > EXEC*  ・  難易度: 初級

EXECは、自動化テーブルのアクション節で、CMDに渡した文字列のコマンドやコマンドリストを起動する書き方です。一致したメッセージに動作を結び付けます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出判定のネットビューでネットビューの運用確認を行います。EXEC の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定のネットビューを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定のネットビューを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出判定の確認値として扱う。 ✅
    - D. EXEC の属性行を読まず呼出判定のネットビューの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では EXEC は「IBM Z NetViewで EXEC の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では EXEC の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では EXEC の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > IF MSGID

### IF MSGID {#c32-i4740}
*分類: 自動化テーブル > IF MSGID*  ・  難易度: 初級

IF MSGIDは、自動化テーブルの条件節で、届いたメッセージのIDと指定した値を突き合わせる書き方です。一致するとTHENに続くアクション節が実行されます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開判定のネットビューで IF MSGID の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IF MSGID の出力を取らず展開判定のネットビューの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開判定で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して展開判定のネットビューの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のネットビューへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では IF MSGID は「展開判定のネットビューに関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では IF MSGID の属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では IF MSGID を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > OTHERWISE

### OTHERWISE {#c32-i4741}
*分類: 自動化テーブル > OTHERWISE*  ・  難易度: 中級

OTHERWISEは、自動化テーブルのSELECT分岐で、先行するWHENのいずれにも一致しなかったメッセージの処理を書く節です。想定外のメッセージを既定へ導きます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端判定のネットビューに関係する OTHERWISE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を終端判定で確認する。 ✅
    - B. OTHERWISE の名称と担当者名のみを残して終端判定のネットビューの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定のネットビューを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定のネットビューの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では OTHERWISE は「OTHERWISE の用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの OTHERWISE と DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では OTHERWISE を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル > SELECT

### SELECT {#c32-i4742}
*分類: 自動化テーブル > SELECT*  ・  難易度: 中級

SELECTは、自動化テーブルで複数のWHEN条件を並べて分岐させる構文です。最初に一致したWHENの処理を実行し、どれにも合わなければOTHERWISEへ進みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書判定のネットビューでネットビューの運用確認を行います。SELECT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定のネットビューを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定のネットビューを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書判定の確認記録にまとめる。 ✅
    - D. SELECT の属性行を読まず上書判定のネットビューの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では SELECT は「IBM Z NetViewで SELECT の扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では SELECT の表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では SELECT の使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル運用 > AUTOMAN

### AUTOMAN {#c32-i4743}
*分類: 自動化テーブル運用 > AUTOMAN*  ・  難易度: 上級

AUTOMANは、複数の自動化テーブルをまとめて活性化や停止、テスト、状態確認するコマンドです。ステートメント単位でも有効と無効を切り替えます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切判定のネットビューで AUTOMAN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AUTOMAN の出力を取らず区切判定のネットビューの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切判定の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切判定のネットビューの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定のネットビューへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では AUTOMAN は「区切判定のネットビューに関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では AUTOMAN の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では AUTOMAN を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル運用 > AUTOTBL

### AUTOTBL {#c32-i4744}
*分類: 自動化テーブル運用 > AUTOTBL*  ・  難易度: 中級

AUTOTBLは、自動化テーブルの活性化やテスト、リスト表示、状態確認を行うコマンドです。MEMBERで対象を指定し、TESTで構文を検査します

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力判定のネットビューに関する AUTOTBL の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力判定のネットビューの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定のネットビューの証跡として保存して根拠にする。
    - C. AUTOTBL の変更点を出力本文から切り離して出力判定のネットビューの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力判定の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では AUTOTBL は「AUTOTBL の状態と出力メッセージを結び付ける出力判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では AUTOTBL の出力行と DSI633I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では AUTOTBL を IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 自動化テーブル運用 > AUTOTEST

### AUTOTEST {#c32-i4745}
*分類: 自動化テーブル運用 > AUTOTEST*  ・  難易度: 中級

AUTOTESTは、記録した入力ストリームで自動化テーブルの動きを検査するコマンドです。MEMBER、SOURCE、LISTING、REPORTで対象と出力先を指定します

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件判定のネットビューに関係する AUTOTEST の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件判定の結果として保存する。 ✅
    - B. AUTOTEST の名称と担当者名のみを残して条件判定のネットビューの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定のネットビューを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定のネットビューの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では AUTOTEST は「AUTOTEST の用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの AUTOTEST と DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では AUTOTEST を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## その他

### その他（特定項目に紐づかないQA・手順） {#c32-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（38問）"
    **問題.** 順序判定の小なりでネットビューの運用確認を行います。PIPE 小なり 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定の小なりを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定の小なりを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を順序判定で確認する。 ✅
    - D. PIPE 小なり 属性の属性行を読まず順序判定の小なりの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では PIPE 小なり 属性 は「IBM Z NetViewで PIPE 小なり 属性の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では PIPE 小なり 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では PIPE 小なり 属性の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide

    ---

    **問題.** 値域判定の大なりに関する PIPE 大なり (To Disk)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定の大なりの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の大なりの証跡として保存して根拠にする。
    - C. PIPE 大なり (To Disk)の変更点を出力本文から切り離して値域判定の大なりの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、値域判定の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では PIPE 大なり (To Disk) は「PIPE 大なり (To Disk)の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では PIPE 大なり (To Disk)の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では PIPE 大なり (To Disk)を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide

    ---

    **問題.** 値域読解の: 小なりに関する Reading 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域読解の: 小なりの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解の: 小なりの証跡として保存して根拠にする。
    - C. Reading 機能の変更点を出力本文から切り離して値域読解の: 小なりの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では Reading 機能 は「Reading 機能の状態と出力メッセージを結び付ける値域読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では Reading 機能の出力行と DSI633I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では Reading 機能を IBM Z NetViewの確認記録に残し、対象名は値域読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide

    ---

    **問題.** 変更読解のネットビューに関する Release 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解のネットビューの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解のネットビューの証跡として保存して根拠にする。
    - C. Release 機能の変更点を出力本文から切り離して変更読解のネットビューの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Release 機能 は「Release 機能の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Release 機能の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Release 機能を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 上書検分のネットビューでネットビューの運用確認を行います。Selecting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分のネットビューを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分のネットビューを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書検分の点検結果を残す。 ✅
    - D. Selecting 機能の属性行を読まず上書検分のネットビューの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では Selecting 機能 は「IBM Z NetViewで Selecting 機能の扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では Selecting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では Selecting 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 範囲確認の:でネットビューの運用確認を行います。Working 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認の:を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲確認の:を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、範囲確認の証跡として残す。 ✅
    - D. Working 機能の属性行を読まず範囲確認の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Working 機能 は「IBM Z NetViewで Working 機能の扱いを記録する範囲確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Working 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Working 機能の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 区切検分のコマンドリストで Comparison 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Comparison 機能の出力を取らず区切検分のコマンドリストの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検分の根拠にする。 ✅
    - C. LIST CLIST を省略して区切検分のコマンドリストの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のコマンドリストへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Comparison 機能 は「区切検分のコマンドリストに関係する定義値と表示行を照合する区切検分項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Comparison 機能の属性行と DSI039I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Comparison 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 範囲検分のコマンドリストでネットビューの運用確認を行います。Comparison 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分のコマンドリストを確認した扱いにする。
    - B. DSI039I の有無を確認せず範囲検分のコマンドリストを正常終了として記録する。
    - C. 同じ画面で対象行と DSI039I を読み、範囲検分の結果として保存する。 ✅
    - D. Comparison 機能の属性行を読まず範囲検分のコマンドリストの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Comparison 機能 は「IBM Z NetViewで Comparison 機能の扱いを記録する範囲検分項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Comparison 機能の表示結果と DSI039I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Comparison 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 復旧整理のインストール 構成で Configuring 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Configuring 機能の出力を取らず復旧整理のインストール 構成の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧整理として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して復旧整理のインストール 構成の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理のインストール 構成へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Configuring 機能 は「復旧整理のインストール 構成に関係する定義値と表示行を照合する復旧整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Configuring 機能の属性行と DSI633I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Configuring 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 順序読解のインストール 構成でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解のインストール 構成を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解のインストール 構成を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序読解の根拠にする。 ✅
    - D. Defining 機能の属性行を読まず順序読解のインストール 構成の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Defining 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 記録読解のインストール 構成に関係する Loading 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録読解の確認記録にまとめる。 ✅
    - B. Loading 機能の名称と担当者名のみを残して記録読解のインストール 構成の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解のインストール 構成を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解のインストール 構成の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Loading 機能 は「Loading 機能の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの Loading 機能と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Loading 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 比較読解のインストール 構成で Loading 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Loading 機能の出力を取らず比較読解のインストール 構成の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較読解の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して比較読解のインストール 構成の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解のインストール 構成へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Loading 機能 は「比較読解のインストール 構成に関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Loading 機能の属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Loading 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 出力確認のインストール 構成に関する Modifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LIST CLIST の結果を残さず出力確認のインストール 構成の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のインストール 構成の証跡として保存して根拠にする。
    - C. Modifying 機能の変更点を出力本文から切り離して出力確認のインストール 構成の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力確認として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では Modifying 機能 は「Modifying 機能の状態と出力メッセージを結び付ける出力確認項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では Modifying 機能の出力行と DSI039I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では Modifying 機能を IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 監査整理の:でネットビューの運用確認を行います。Scenario 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理の:を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理の:を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査整理で再確認できる形にする。 ✅
    - D. Scenario 機能の属性行を読まず監査整理の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Scenario 機能 は「IBM Z NetViewで Scenario 機能の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Scenario 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Scenario 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 順序検査のカスタマイズ 等でネットビューの運用確認を行います。Alert 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査のカスタマイズ 等を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査のカスタマイズ 等を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序検査の確認記録にまとめる。 ✅
    - D. Alert 機能の属性行を読まず順序検査のカスタマイズ 等の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Alert 機能 は「IBM Z NetViewで Alert 機能の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Alert 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Alert 機能の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 構文照合のセキュリティ 連携に関係する Application 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文照合で再確認できる形にする。 ✅
    - B. Application 機能の名称と担当者名のみを残して構文照合のセキュリティ 連携の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合のセキュリティ 連携を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合のセキュリティ 連携の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Application 機能 は「Application 機能の用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの Application 機能と DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Application 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 終端分離のセキュリティ 連携に関係する Restricting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、終端分離の証跡として残す。 ✅
    - B. Restricting 機能の名称と担当者名のみを残して終端分離のセキュリティ 連携の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離のセキュリティ 連携を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端分離のセキュリティ 連携の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では Restricting 機能 は「Restricting 機能の用途をネットビューの表示で確認する終端分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの Restricting 機能と DSI633I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では Restricting 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 復旧分離の:で Scenario 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Scenario 機能の出力を取らず復旧分離の:の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧分離の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Scenario 機能 は「復旧分離の:に関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Scenario 機能の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Scenario 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 置換記録のトラブルシューティングに関する A 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録のトラブルシューティングの証跡として保存して根拠にする。
    - C. A 機能の変更点を出力本文から切り離して置換記録のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、置換記録の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では A 機能 は「A 機能の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では A 機能の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では A 機能を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 置換検分のトラブルシューティングに関する Diagnosing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Diagnosing 機能の変更点を出力本文から切り離して置換検分のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、置換検分の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では Diagnosing 機能 は「Diagnosing 機能の状態と出力メッセージを結び付ける置換検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では Diagnosing 機能の出力行と DSI633I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では Diagnosing 機能を IBM Z NetViewの確認記録に残し、対象名は置換検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 警告照合のトラブルシューティングに関係する Expected 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告照合の根拠にする。 ✅
    - B. Expected 機能の名称と担当者名のみを残して警告照合のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告照合のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告照合のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では Expected 機能 は「Expected 機能の用途をネットビューの表示で確認する警告照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では IBM Z NetViewの Expected 機能と DSI633I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では Expected 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 順序追跡のトラブルシューティングでネットビューの運用確認を行います。Incorrect 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡のトラブルシューティングを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序追跡で再確認できる形にする。 ✅
    - D. Incorrect 機能の属性行を読まず順序追跡のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では Incorrect 機能 は「IBM Z NetViewで Incorrect 機能の扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では Incorrect 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では Incorrect 機能の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 終端検査の"に関係する Message 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端検査の確認にする。 ✅
    - B. Message 機能の名称と担当者名のみを残して終端検査の"の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査の"を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査の"の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Message 機能 は「Message 機能の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの Message 機能と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Message 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 区切検査のトラブルシューティングで Missing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Missing 機能の出力を取らず区切検査のトラブルシューティングの説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を区切検査で確認する。 ✅
    - C. BROWSE CANZLOG を省略して区切検査のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では Missing 機能 は「区切検査のトラブルシューティングに関係する定義値と表示行を照合する区切検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では Missing 機能の属性行と DSI633I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では Missing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 比較検査のトラブルシューティングで Negative 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Negative 機能の出力を取らず比較検査のトラブルシューティングの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較検査の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較検査のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では Negative 機能 は「比較検査のトラブルシューティングに関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では Negative 機能の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では Negative 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 変更判定のトラブルシューティングに関する No 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定のトラブルシューティングの証跡として保存して根拠にする。
    - C. No 機能の変更点を出力本文から切り離して変更判定のトラブルシューティングの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更判定として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では No 機能 は「No 機能の状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では No 機能の出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では No 機能を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 監査分離のトラブルシューティングでネットビューの運用確認を行います。Tivoli 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査分離の採否を説明欄に結び付ける。 ✅
    - D. Tivoli 機能の属性行を読まず監査分離のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Tivoli 機能 は「IBM Z NetViewで Tivoli 機能の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Tivoli 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Tivoli 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 優先読解のトラブルシューティングに関する Troubleshooting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先読解のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解のトラブルシューティングの証跡として保存して根拠にする。
    - C. Troubleshooting 機能の変更点を出力本文から切り離して優先読解のトラブルシューティングの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先読解として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では Troubleshooting 機能 は「Troubleshooting 機能の状態と出力メッセージを結び付ける優先読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では Troubleshooting 機能の出力行と DSI633I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では Troubleshooting 機能を IBM Z NetViewの確認記録に残し、対象名は優先読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 記録読解のトラブルシューティングに関係する Troubleshooting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録読解の確認にする。 ✅
    - B. Troubleshooting 機能の名称と担当者名のみを残して記録読解のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Troubleshooting 機能 は「Troubleshooting 機能の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの Troubleshooting 機能と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Troubleshooting 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 呼出検分のトラブルシューティングでネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検分のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出検分の採否を説明欄に結び付ける。 ✅
    - D. Using 機能の属性行を読まず呼出検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する呼出検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では Using 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 置換検分のトラブルシューティングに関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換検分のトラブルシューティングの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換検分として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は置換検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 置換記録のユーザーズガイド 操作に関する Determining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Determining 機能の変更点を出力本文から切り離して置換記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、置換記録の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Determining 機能 は「Determining 機能の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Determining 機能の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Determining 機能を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 終端記録のユーザーズガイド 操作に関係する Determining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端記録で再確認できる形にする。 ✅
    - B. Determining 機能の名称と担当者名のみを残して終端記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では Determining 機能 は「Determining 機能の用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの Determining 機能と DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では Determining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 展開照合のユーザーズガイド 操作で Session 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Session 機能の出力を取らず展開照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開照合の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では Session 機能 は「展開照合のユーザーズガイド 操作に関係する定義値と表示行を照合する展開照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では Session 機能の属性行と DSI633I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では Session 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開照合初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 監査照合のユーザーズガイド 操作でネットビューの運用確認を行います。SNA 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査照合のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査照合で再確認できる形にする。 ✅
    - D. SNA 機能の属性行を読まず監査照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では SNA 機能 は「IBM Z NetViewで SNA 機能の扱いを記録する監査照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では SNA 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では SNA 機能の使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide

    ---

    **問題.** 値域確認の自動化テーブル 状態判定に関する Solicited 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Solicited 機能の変更点を出力本文から切り離して値域確認の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Solicited 機能 は「Solicited 機能の状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Solicited 機能の出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Solicited 機能を IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 警告追跡の自動化テーブル 状態判定に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告追跡の点検結果を残す。 ✅
    - B. Using 機能の名称と担当者名のみを残して警告追跡の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告追跡の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI039I の有無を見ず警告追跡の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する警告追跡項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では IBM Z NetViewの Using 機能と DSI039I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 復旧追跡の自動化テーブル 状態判定で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず復旧追跡の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧追跡で再確認できる形にする。 ✅
    - C. LIST CLIST を省略して復旧追跡の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では Using 機能 は「復旧追跡の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧追跡項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では Using 機能の属性行と DSI039I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


??? note "検証手順（32件）"
    **IF MSGID 確認手順**

    - 検証目的: IF MSGID 条件が対象メッセージ識別子を比較し、指定した処理へ分岐する構文であることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。IF MSGID の定義行を実データ・セットから確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(NVIFMSG)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(NVIFMSG) -- Line 00000000 Col 001 080
    Command ===>
    000001 IF MSGID = 'XYZ123I' THEN
    000002   EXEC(CMD('MSG OPER1 AUTOMATION IS RECEIVING XYZ123I'))
    000003   CONTINUE(Y);
    ```

    NVIFMSG の表示行に IF MSGID があり、検証対象の自動化テーブル構文を確認できます。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。NVIFMSG を活動化せずに自動化テーブル構文だけ検査するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL MEMBER=NVIFMSG,TEST
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNM501I TEST OF NETVIEW AUTOMATION FILE "NVIFMSG" WAS SUCCESSFUL
    ```

    CNM501I と NVIFMSG は、表示した自動化テーブル構文の検査が成功したことを示します。

    - 合格条件: ① ステップ1の IF MSGID が表示されること
    ② ステップ2の CNM501I と NVIFMSG が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **EXEC 確認手順**

    - 検証目的: EXEC の CMD パラメーターが、条件一致時に実在する NetView コマンドを実行する構文であることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。EXEC(CMD の定義行を実データ・セットから確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(NVEXEC)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(NVEXEC) -- Line 00000000 Col 001 080
    Command ===>
    000001 IF MSGID = 'XYZ123I' THEN
    000002   EXEC(CMD('MSG OPER1 AUTOMATION IS RECEIVING XYZ123I'));
    ```

    NVEXEC の表示行に EXEC(CMD があり、検証対象の自動化テーブル構文を確認できます。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。NVEXEC を活動化せずに自動化テーブル構文だけ検査するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL MEMBER=NVEXEC,TEST
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNM501I TEST OF NETVIEW AUTOMATION FILE "NVEXEC" WAS SUCCESSFUL
    ```

    CNM501I と NVEXEC は、表示した自動化テーブル構文の検査が成功したことを示します。

    - 合格条件: ① ステップ1の EXEC(CMD が表示されること
    ② ステップ2の CNM501I と NVEXEC が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **CONTINUE 確認手順**

    - 検証目的: CONTINUE(Y) により一致後も後続の自動化テーブル文が評価されることを構文検査で確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。CONTINUE(Y) の定義行を実データ・セットから確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(NVCONT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(NVCONT) -- Line 00000000 Col 001 080
    Command ===>
    000001 IF MSGID = 'XYZ123I' THEN
    000002   EXEC(CMD('MSG OPER1 AUTOMATION IS RECEIVING XYZ123I'))
    000003   CONTINUE(Y);
    ```

    NVCONT の表示行に CONTINUE(Y) があり、検証対象の自動化テーブル構文を確認できます。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。NVCONT を活動化せずに自動化テーブル構文だけ検査するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL MEMBER=NVCONT,TEST
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNM501I TEST OF NETVIEW AUTOMATION FILE "NVCONT" WAS SUCCESSFUL
    ```

    CNM501I と NVCONT は、表示した自動化テーブル構文の検査が成功したことを示します。

    - 合格条件: ① ステップ1の CONTINUE(Y) が表示されること
    ② ステップ2の CNM501I と NVCONT が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **OTHERWISE 確認手順**

    - 検証目的: REXX の SELECT でどの WHEN にも一致しない場合に OTHERWISE 分岐が実行されることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。CHKMSG の SELECT と OTHERWISE 分岐を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSICLD(CHKMSG)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSICLD(CHKMSG) -- Line 00000000 Col 001 080
    Command ===>
    000001 /* REXX */
    000002 parse arg msgid
    000003 SELECT
    000004   WHEN msgid='XYZ123I' then say 'MATCH='msgid
    000005   OTHERWISE say 'UNHANDLED='msgid
    000006 end
    ```

    CHKMSG の SELECT 内に OTHERWISE と UNHANDLED= の出力処理が定義されています。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。既知の WHEN に一致しないメッセージを command list へ渡すため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> CHKMSG DSI999I
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNHANDLED=DSI999I
    ```

    UNHANDLED=DSI999I は DSI999I が OTHERWISE 分岐で処理された結果です。

    - 合格条件: ① ステップ1の OTHERWISE と UNHANDLED= が表示されること
    ② ステップ2の UNHANDLED=DSI999I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **ANYID 確認手順**

    - 検証目的: ANYID が特定識別子に限定せず未自動化メッセージを LOGSEQ へ渡す条件として使われることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。MSGID = ANYID の定義行を実データ・セットから確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(NVANYID)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(NVANYID) -- Line 00000000 Col 001 080
    Command ===>
    000001 IF MSGID = ANYID THEN
    000002   EXEC(CMD('LOGSEQ ' ANYID ' NOT AUTOMATED'));
    ```

    NVANYID の表示行に MSGID = ANYID があり、検証対象の自動化テーブル構文を確認できます。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。NVANYID を活動化せずに自動化テーブル構文だけ検査するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL MEMBER=NVANYID,TEST
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNM501I TEST OF NETVIEW AUTOMATION FILE "NVANYID" WAS SUCCESSFUL
    ```

    CNM501I と NVANYID は、表示した自動化テーブル構文の検査が成功したことを示します。

    - 合格条件: ① ステップ1の MSGID = ANYID が表示されること
    ② ステップ2の CNM501I と NVANYID が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **SELECT 確認手順**

    - 検証目的: REXX の SELECT が入力メッセージ識別子に対応する WHEN 分岐を一つ選ぶことを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。CHKMSG の SELECT と WHEN 分岐を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSICLD(CHKMSG)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSICLD(CHKMSG) -- Line 00000000 Col 001 080
    Command ===>
    000001 /* REXX */
    000002 parse arg msgid
    000003 SELECT
    000004   WHEN msgid='XYZ123I' then say 'MATCH='msgid
    000005   OTHERWISE say 'UNHANDLED='msgid
    000006 end
    ```

    CHKMSG の SELECT 内に XYZ123I を比較する WHEN と MATCH= の出力処理があります。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。WHEN 条件に一致するメッセージを command list へ渡すため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> CHKMSG XYZ123I
    → Enter を押す
    ```

    画面・出力:
    ```text
    MATCH=XYZ123I
    ```

    MATCH=XYZ123I は SELECT が XYZ123I の WHEN 分岐を選択した結果です。

    - 合格条件: ① ステップ1の SELECT と WHEN が表示されること
    ② ステップ2の MATCH=XYZ123I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **AUTOTBL 確認手順**

    - 検証目的: AUTOTBL の TEST と STATUS を使い、構文検査と現在活動中の自動化テーブルを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。DSITBL01 を活動化せず構文検査するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL MEMBER=DSITBL01,TEST
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNM501I TEST OF NETVIEW AUTOMATION FILE "DSITBL01" WAS SUCCESSFUL
    ```

    CNM501I と DSITBL01 は自動化テーブル構文の検査成功を示します。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。現在活動中の自動化テーブルと活動化情報を表示するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSI410I DSIPARM MEMBER DSITBL01 BEING USED FOR NETVIEW AUTOMATION
    DWO040I AUTOMATION TABLE DSITBL01
    ACTIVATED 05/21/10 10:36:44 BY CNM01PPT
    ```

    DSI410I と DWO040I は DSITBL01 が CNM01PPT により活動化されていることを示します。

    - 合格条件: ① ステップ1の CNM501I と DSITBL01 が表示されること
    ② ステップ2の DSI410I と DWO040I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **AUTOTEST 確認手順**

    - 検証目的: AUTOTEST で記録済みメッセージを使った自動化テーブル試験を実行し、リスト作成と試験終了を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。TESTRECS を入力に TESTTBL1 の試験と報告作成を行うため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTEST MEMBER=TESTTBL1,LISTING=LIST1,SOURCE=TESTRECS,REPORT=TESTRPT1
    → Enter を押す
    ```

    画面・出力:
    ```text
    BNH347I TEST AUTOMATION TABLE LISTING LIST1 SUCCESSFULLY GENERATED
    BNH382I AUTOMATION TABLE TESTING STOPPED, SOURCE=TESTRECS
    ```

    BNH347I は LIST1 の生成、BNH382I は SOURCE=TESTRECS の試験終了を示します。

    - 合格条件: ① ステップ1の BNH347I と LIST1 が表示されること
    ② ステップ1の BNH382I と TESTRECS が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **AUTOMAN 確認手順**

    - 検証目的: AUTOMAN の全画面パネルで複数自動化テーブルの位置、名前、状態、マーカー、担当タスクを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。複数の活動中自動化テーブルと状態を一覧するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOMAN
    → Enter を押す
    ```

    画面・出力:
    ```text
    EZLK8500                  Automation Table Management
    AUTOMATION TABLE           Enter any character in the selection fields
    SEL     POS     NAME         STATUS     MARKERS     TASK     DATE     TIME
     _       1      DISTABLE     ENABLED                NETOP2   03/18/11 13:15:24
     _       2      DSITBL01     ENABLED    (AON)       NETOP    03/18/11 13:11:09
    Command ===>
    F1=Help F3=Return F5=Refresh F8=Forward F10=Global Commands F12=Cancel
    ```

    EZLK8500 パネルの DISTABLE と DSITBL01 行に STATUS ENABLED と位置、マーカー、タスクが表示されます。

    - 合格条件: ① ステップ1の EZLK8500 と DSITBL01 が表示されること
    ② ステップ1の DISTABLE と ENABLED が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **BNH382I 確認手順**

    - 検証目的: AUTOTEST が入力記録の末尾へ達したとき、BNH382I で停止と入力メンバー名が通知されることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。記録済み入力を最後まで処理して試験停止通知を得るため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTEST MEMBER=TESTTBL1,SOURCE=TESTRECS,REPORT=TESTRPT1
    → Enter を押す
    ```

    画面・出力:
    ```text
    BNH382I AUTOMATION TABLE TESTING STOPPED, SOURCE=TESTRECS
    ```

    BNH382I と SOURCE=TESTRECS は TESTRECS の末尾で自動化テーブル試験が停止したことを示します。

    - 合格条件: ① ステップ1の BNH382I と SOURCE=TESTRECS が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **DSI039I 確認手順**

    - 検証目的: MSG コマンドで指定オペレーターへ送った本文が DSI039I として受信されることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。OPER1 へ自動化受信確認メッセージを送るため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> MSG OPER1 AUTOMATION IS RECEIVING XYZ123I
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSI039I AUTOMATION IS RECEIVING XYZ123I
    ```

    DSI039I の本文 AUTOMATION IS RECEIVING XYZ123I は OPER1 への通知内容です。

    - 合格条件: ① ステップ1の DSI039I と XYZ123I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **CNMSTYLE 確認手順**

    - 検証目的: 初期設定の基点である CNMSTYLE を表示し、共通設定とユーザー設定メンバーの解決順を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。初期化設定とユーザー設定メンバーの参照を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(CNMSTYLE)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(CNMSTYLE) -- Line 00000000 Col 001 080
    Command ===>
    000001 * IBM Z NetView CNMSTYLE initialization statements
    000002 %INCLUDE CNMSTUSR
    000003 AUTOCMD.DSITBL01.list = DSITBL01
    000004 AUTOCMD.DSITBL01.order = A
    ```

    CNMSTYLE の %INCLUDE CNMSTUSR と AUTOCMD.DSITBL01 行で初期化時の設定連鎖を確認できます。

    - 合格条件: ① ステップ1の CNMSTYLE と CNMSTUSR が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **CNMSTUSR 確認手順**

    - 検証目的: CNMSTUSR に置いたローカル変更が、IBM 提供の CNMSTYLE を直接変更せず上書きに使われることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。CNMSTUSR に置かれたローカル上書き設定を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(CNMSTUSR)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(CNMSTUSR) -- Line 00000000 Col 001 080
    Command ===>
    000001 * Installation-specific NetView initialization
    000002 SSI.ProcString = CNMPSSI.SS,SUB=MSTR,ARM='*ARM'
    000003 AUTOCMD.LOCALTBL.list = LOCALIST
    000004 AUTOCMD.LOCALTBL.order = B
    ```

    CNMSTUSR の SSI.ProcString と AUTOCMD.LOCALTBL はローカル上書きとして解決されます。

    - 合格条件: ① ステップ1の CNMSTUSR と SSI.ProcString が表示されること
    ② ステップ1の CNMPSSI が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **AUTOCMD 確認手順**

    - 検証目的: CNMSTYLE の AUTOCMD 文で自動化テーブル名、リスト名、マーカー、ロード順が指定されることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。ローカル自動化テーブルのロード属性を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(CNMSTUSR)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(CNMSTUSR) -- Line 00000000 Col 001 080
    Command ===>
    000001 AUTOCMD.LOCALTBL.list = LOCALIST
    000002 AUTOCMD.LOCALTBL.marker = LOCAL
    000003 AUTOCMD.LOCALTBL.order = B
    ```

    AUTOCMD.LOCALTBL の list、marker、order 行に LOCALIST、LOCAL、B が設定されています。

    - 合格条件: ① ステップ1の AUTOCMD.LOCALTBL と LOCALIST が表示されること
    ② ステップ1の marker = LOCAL と order = B が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **DSIPARM 確認手順**

    - 検証目的: DSIPARM 連結内の CNMSTYLE を表示し、NetView 初期化定義が格納されるデータ・セットを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。DSIPARM 内の CNMSTYLE と主要初期化文を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(CNMSTYLE)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(CNMSTYLE) -- Line 00000000 Col 001 080
    Command ===>
    000001 * DSIPARM member CNMSTYLE
    000002 %INCLUDE CNMSTUSR
    000003 AUTOCMD.DSITBL01.list = DSITBL01
    ```

    BROWSE のデータ・セット名 DSIPARM とメンバー CNMSTYLE から初期化定義の格納場所を確認できます。

    - 合格条件: ① ステップ1の DSIPARM と CNMSTYLE が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **DSITBL01 確認手順**

    - 検証目的: 既定の DSITBL01 が活動中の NetView 自動化テーブルとして使われていることを STATUS で確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。現在活動中の既定自動化テーブルを表示するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSI410I DSIPARM MEMBER DSITBL01 BEING USED FOR NETVIEW AUTOMATION
    DWO040I AUTOMATION TABLE DSITBL01
    ACTIVATED 05/21/10 10:36:44 BY CNM01PPT
    ```

    DSI410I と DWO040I は DSITBL01 が CNM01PPT により活動化された状態を示します。

    - 合格条件: ① ステップ1の DSI410I と DSITBL01 が表示されること
    ② ステップ1の DWO040I と CNM01PPT が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **CNMPROC 確認手順**

    - 検証目的: z/OS 操作卓から CNMPROC を開始し、NetView 主アドレス空間の開始メッセージを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は Console のコマンド入力画面です。DSIMNT を指定して NetView 主アドレス空間を開始するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    Console ===> S CNMPROC,PROG=DSIMNT
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP373 CNMPROC STARTED
    IEF403I CNMPROC - STARTED - TIME=12.14.02
    CNM01PPT NETVIEW PROGRAM DSIMNT INITIALIZATION IN PROGRESS
    ```

    $HASP373 と IEF403I は CNMPROC の開始、DSIMNT は指定した NetView 主プログラムを示します。

    - 合格条件: ① ステップ1の CNMPROC と DSIMNT が表示されること
    ② ステップ1の $HASP373 と IEF403I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **CNMPSSI 確認手順**

    - 検証目的: CNMPSSI の開始後、PPI 初期化完了と NetView サブシステムの使用可能状態を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は Console のコマンド入力画面です。NetView サブシステム・インターフェースを開始するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    Console ===> S CNMPSSI
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP373 CNMPSSI  STARTED
    IEF403I CNMPSSI - STARTED - TIME=12.13.35
    CNM226I NetView Program to Program Interface initialization is completed
    CNM541I NetView subsystem CNMP is fully functional
    ```

    CNM226I は PPI 初期化完了、CNM541I はサブシステム CNMP が使用可能であることを示します。

    - 合格条件: ① ステップ1の $HASP373 と CNMPSSI が表示されること
    ② ステップ1の CNM226I と CNM541I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **OPERATOR 確認手順**

    - 検証目的: DSIOPF の OPERATOR 文でオペレーターID、認証値、関連プロファイルが定義されることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。NEWOPER の OPERATOR 文と PROFILEN 文を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(DSIOPF)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(DSIOPF) -- Line 00000000 Col 001 080
    Command ===>
    000001 NEWOPER   OPERATOR  PASSWORD=NEWOPER
    000002           PROFILEN  DSIPROFA
    000003           END
    ```

    NEWOPER の OPERATOR 行と PROFILEN DSIPROFA 行でIDとプロファイルの対応を確認できます。

    - 合格条件: ① ステップ1の NEWOPER と OPERATOR が表示されること
    ② ステップ1の PROFILEN と DSIPROFA が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **DSIOPF 確認手順**

    - 検証目的: DSIOPF メンバーが複数のオペレーター定義をまとめ、各IDを DSIPRF プロファイルへ関連付けることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。OPER1 と DSIPROFX の関連付けを確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(DSIOPF)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(DSIOPF) -- Line 00000000 Col 001 080
    Command ===>
    000001 OPER1     OPERATOR PASSWORD=PWORD
    000002           PROFILEN DSIPROFX
    000003           END
    ```

    DSIOPF の OPER1 行と PROFILEN DSIPROFX 行により、オペレーターとプロファイルの対応を確認できます。

    - 合格条件: ① ステップ1の DSIOPF と OPER1 が表示されること
    ② ステップ1の DSIPROFX が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **DSIPRF 確認手順**

    - 検証目的: DSIPRF の PROFILE、AUTH、END 文からログオン初期コマンドと制御権限を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。DSIPROFA の初期コマンドと認可属性を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPRF(DSIPROFA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPRF(DSIPROFA) -- Line 00000000 Col 001 080
    Command ===>
    000001 DSIPROFA  PROFILE IC=LOGPROF1
    000002            AUTH    MSGRECVR=NO,CTL=GLOBAL
    000003            END
    ```

    PROFILE IC=LOGPROF1 と AUTH MSGRECVR=NO,CTL=GLOBAL が DSIPROFA のログオン動作と権限を示します。

    - 合格条件: ① ステップ1の PROFILE IC=LOGPROF1 が表示されること
    ② ステップ1の MSGRECVR=NO と CTL=GLOBAL が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **SPAN 確認手順**

    - 検証目的: 特定制御のオペレーター・プロファイルに読み取り可能な SPAN と初期 SPAN が定義されることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。特定制御プロファイルの SPAN と ISPAN を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPRF(DSIPROFX)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPRF(DSIPROFX) -- Line 00000000 Col 001 080
    Command ===>
    000001 DSIPROFX  PROFILE  IC=OP1INIT
    000002            AUTH     CTL=SPECIFIC,NGMFVSPN=ANNN
    000003            SPAN     SPAN1(R),SPAN2(R)
    000004            ISPAN    SPAN3(R),SPAN4(R)
    000005            END
    ```

    CTL=SPECIFIC の DSIPROFX に SPAN1(R) と ISPAN SPAN3(R) が定義されています。

    - 合格条件: ① ステップ1の CTL=SPECIFIC と SPAN1(R) が表示されること
    ② ステップ1の ISPAN と SPAN3(R) が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **BROWSE CANZLOG 確認手順**

    - 検証目的: BROWSE CANZLOG で NetView、z/OS、DOM、コマンド・エコーを統合時系列から確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。統合ログの最新時刻範囲とメッセージを表示するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE CANZLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    Canzlog  TAG=(NVMSG,MVSMSG,DOM)                   05/22/22 15:57:07 -- 15:59:20
    15:58:02 NVMSG CNM01 DSI410I DSIPARM MEMBER DSITBL01 BEING USED FOR NETVIEW AUTOMATION
    15:58:10 MVSMSG CNM01 IEF403I CNMPROC - STARTED
    Command ===>
    ```

    Canzlog の TAG=(NVMSG,MVSMSG,DOM) と DSI410I、IEF403I により複数ログ種別を同じ時系列で確認できます。

    - 合格条件: ① ステップ1の Canzlog と TAG=(NVMSG,MVSMSG,DOM) が表示されること
    ② ステップ1の DSI410I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **NPDA 確認手順**

    - 検証目的: NPDA コマンドで Hardware Monitor の主メニューを開き、アラートとイベントの管理入口を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。Hardware Monitor の主メニューを表示するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> NPDA
    → Enter を押す
    ```

    画面・出力:
    ```text
    BNJ90PDA              NetView Hardware Monitor - NPDA
    Domain CNM01
    1 ALERTS       Display current alerts
    2 ALERT HISTORY
    3 EVENTS
    Command ===>
    ```

    NetView Hardware Monitor - NPDA と Domain CNM01、ALERTS の選択肢が主メニューに表示されます。

    - 合格条件: ① ステップ1の NPDA と Hardware Monitor が表示されること
    ② ステップ1の CNM01 と ALERTS が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **ALERTSH 確認手順**

    - 検証目的: ALERTSH で Hardware Monitor データベースに記録されたアラート履歴と資源名を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。保存済みアラートの日時、資源、メッセージを一覧するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> ALERTSH
    → Enter を押す
    ```

    画面・出力:
    ```text
    BNJ81AHS              Alerts-History
    Date     Time     Resource Severity Message
    07/16/26 10:42:11 PU001   MAJOR    IST619I ID = PU001 FAILED
    Command ===>
    ```

    Alerts-History の PU001 行に MAJOR と IST619I が表示され、保存された障害履歴を確認できます。

    - 合格条件: ① ステップ1の Alerts-History と PU001 が表示されること
    ② ステップ1の IST619I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **LOGSEQ 確認手順**

    - 検証目的: ANYID の未一致メッセージを LOGSEQ へ渡し、順次ログに未自動化記録が残ることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。未自動化メッセージを LOGSEQ へ渡す最終文を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(NVANYID)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(NVANYID) -- Line 00000000 Col 001 080
    Command ===>
    000001 IF MSGID = ANYID THEN
    000002   EXEC(CMD('LOGSEQ ' ANYID ' NOT AUTOMATED'));
    ```

    MSGID = ANYID と EXEC(CMD('LOGSEQ ' により未一致メッセージを順次ログへ渡す構文です。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。LOGSEQ が書き込んだ未自動化メッセージ記録を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.USER.LOGSEQ
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.USER.LOGSEQ -- Line 00000000 Col 001 080
    Command ===>
    000001 2026-07-16 10:44:28 XYZ999I NOT AUTOMATED
    ```

    NETVIEW.USER.LOGSEQ の XYZ999I NOT AUTOMATED は未自動化メッセージの記録です。

    - 合格条件: ① ステップ1の MSGID = ANYID と LOGSEQ が表示されること
    ② ステップ2の XYZ999I NOT AUTOMATED が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **command list 確認手順**

    - 検証目的: DSICLD に格納した REXX command list を名前で呼び出し、引数に応じた処理結果を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。CHKMSG の引数解析と分岐処理を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSICLD(CHKMSG)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSICLD(CHKMSG) -- Line 00000000 Col 001 080
    Command ===>
    000001 /* REXX */
    000002 parse arg msgid
    000003 if msgid='XYZ123I' then say 'MATCH='msgid
    000004 else say 'UNHANDLED='msgid
    ```

    CHKMSG の parse arg と MATCH= 出力行が command list の入力処理を示します。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。command list 名と引数をコマンド・ファシリティから実行するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> CHKMSG XYZ123I
    → Enter を押す
    ```

    画面・出力:
    ```text
    MATCH=XYZ123I
    ```

    MATCH=XYZ123I は CHKMSG が引数 XYZ123I を受け取り一致分岐を実行した結果です。

    - 合格条件: ① ステップ1の CHKMSG と parse arg が表示されること
    ② ステップ2の MATCH=XYZ123I が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **MSGRECVR 確認手順**

    - 検証目的: プロファイルの MSGRECVR 属性から、配送不能メッセージの許可受信者になる資格を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。DSIPROFA の AUTH 文にある MSGRECVR 属性を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPRF(DSIPROFA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPRF(DSIPROFA) -- Line 00000000 Col 001 080
    Command ===>
    000001 DSIPROFA  PROFILE IC=LOGPROF1
    000002            AUTH    MSGRECVR=NO,CTL=GLOBAL
    000003            END
    ```

    AUTH MSGRECVR=NO は DSIPROFA が配送不能メッセージの許可受信者ではないことを示します。

    - 合格条件: ① ステップ1の DSIPROFA と MSGRECVR=NO が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **IC 確認手順**

    - 検証目的: PROFILE の IC 属性から、オペレーター・ログオン時に自動実行される初期 command list を確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。PROFILE 文の IC 値を確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPRF(DSIPROFA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPRF(DSIPROFA) -- Line 00000000 Col 001 080
    Command ===>
    000001 DSIPROFA  PROFILE IC=LOGPROF1
    000002            AUTH    MSGRECVR=NO,CTL=GLOBAL
    000003            END
    ```

    PROFILE IC=LOGPROF1 は DSIPROFA のログオン時に LOGPROF1 を実行する指定です。

    - 合格条件: ① ステップ1の PROFILE IC=LOGPROF1 が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **AUTOTEST STATUS 確認手順**

    - 検証目的: AUTOTEST STATUS で自動化テーブル試験が現在活動中か停止中かを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。自動化テーブル試験の現在状態を問い合わせるため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTEST STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    BNH337I AUTOMATION TABLE TESTING IS NOT ACTIVE
    ```

    BNH337I と NOT ACTIVE は自動化テーブル試験が現在動作していないことを示します。

    - 合格条件: ① ステップ1の BNH337I と NOT ACTIVE が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **NV2I 確認手順**

    - 検証目的: 開始パラメーター NV2I の値に対応する CxxSTYLE と CxxSTGEN が個別初期化メンバーとして選ばれることを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。NV2I の既定値と選択される個別設定メンバーを確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.CNMPROC(CNMPROC)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.CNMPROC(CNMPROC) -- Line 00000000 Col 001 080
    Command ===>
    000001 //CNMPROC PROC NV2I=NM,PROG=DSIMNT
    000002 //* NV2I=NM selects CNMSTYLE
    000003 //* Included user member resolves to CNMSTGEN
    ```

    NV2I=NM により CxxSTYLE は CNMSTYLE、CxxSTGEN は CNMSTGEN として解決されます。

    - 合格条件: ① ステップ1の NV2I=NM と CNMSTYLE が表示されること
    ② ステップ1の CNMSTGEN が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **CMD 確認手順**

    - 検証目的: EXEC アクションの CMD 値がリテラルの NetView コマンドとして指定され、構文検査に成功することを確認します。
    - 前提条件: 検証用の IBM Z NetView 6.4 ドメイン CNM01 に、対象コマンドと定義メンバーを参照できる権限で接続します。変更を伴う操作は検証環境でのみ行います。
    - セッション環境: IBM Z NetView 6.4 の 3270 コマンド・ファシリティ。CNMPROC と CNMPSSI の開始確認だけは z/OS 操作卓を使用します。

    **ステップ 1**
    現在の画面は NetView のコマンド入力画面です。CMD('MSG OPER1 の定義行を実データ・セットから確認するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE NETVIEW.V6R4M0.DSIPARM(NVCMD)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- NETVIEW.V6R4M0.DSIPARM(NVCMD) -- Line 00000000 Col 001 080
    Command ===>
    000001 IF MSGID = 'XYZ123I' THEN
    000002   EXEC(CMD('MSG OPER1 AUTOMATION IS RECEIVING XYZ123I'));
    ```

    NVCMD の表示行に CMD('MSG OPER1 があり、検証対象の自動化テーブル構文を確認できます。

    **ステップ 2**
    現在の画面は NetView のコマンド入力画面です。NVCMD を活動化せずに自動化テーブル構文だけ検査するため、入力口に構文を確認したコマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> AUTOTBL MEMBER=NVCMD,TEST
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNM501I TEST OF NETVIEW AUTOMATION FILE "NVCMD" WAS SUCCESSFUL
    ```

    CNM501I と NVCMD は、表示した自動化テーブル構文の検査が成功したことを示します。

    - 合格条件: ① ステップ1の CMD('MSG OPER1 が表示されること
    ② ステップ2の CNM501I と NVCMD が表示されること
    - 検証状態: 机上
    - 出典: NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

