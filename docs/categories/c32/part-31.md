---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (31/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > 自動化テーブル / 状態判定

### DoForeignFrom Statement {#c32-i4526}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

DoForeignFrom Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.139) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.139)

??? question "確認問題（1問）"
    **問題.** 記録検査の自動化テーブル 状態判定に関係する DoForeignFrom 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録検査の根拠を固定する。 ✅
    - B. DoForeignFrom 機能の名称と担当者名のみを残して記録検査の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では DoForeignFrom 機能 は「DoForeignFrom 機能の用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの DoForeignFrom 機能と DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では DoForeignFrom 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### END Statement {#c32-i4527}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

END Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.139) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.139)

??? question "確認問題（1問）"
    **問題.** 値域検査の自動化テーブル 状態判定に関する END Statementの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. END Statementの変更点を出力本文から切り離して値域検査の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では END Statement は「END Statementの状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では END Statementの出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では END Statementを IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT Statement {#c32-i4528}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

EXIT Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.139) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.139)

??? question "確認問題（1問）"
    **問題.** 探索判定の自動化テーブル 状態判定で EXIT Statementの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EXIT Statementの出力を取らず探索判定の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を探索判定で確認する。 ✅
    - C. BROWSE CANZLOG を省略して探索判定の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では EXIT Statement は「探索判定の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では EXIT Statementの属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では EXIT Statementを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Enabling MVS Command Management in the NetView Environment {#c32-i4529}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Enabling MVS Command Management in the NetView Environmentは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較検査の自動化テーブル 状態判定で Enabling 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Enabling 機能の出力を取らず比較検査の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を比較検査で確認する。 ✅
    - C. BROWSE CANZLOG を省略して比較検査の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では Enabling 機能 は「比較検査の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では Enabling 機能の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では Enabling 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enabling the MVS Command Exit on MVS {#c32-i4530}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Enabling the MVS Command Exit on MVSは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検査の自動化テーブル 状態判定でネットビューの運用確認を行います。Enabling 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、順序検査の証跡として残す。 ✅
    - D. Enabling 機能の属性行を読まず順序検査の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Enabling 機能 は「IBM Z NetViewで Enabling 機能の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Enabling 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Enabling 機能の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enhancing the Operator Interface {#c32-i4531}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Enhancing the Operator Interfaceは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.335) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.335)

??? question "確認問題（1問）"
    **問題.** 警告検査の自動化テーブル 状態判定に関係する Enhancing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告検査の根拠にする。 ✅
    - B. Enhancing 機能の名称と担当者名のみを残して警告検査の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検査の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では Enhancing 機能 は「Enhancing 機能の用途をネットビューの表示で確認する警告検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの Enhancing 機能と DSI633I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では Enhancing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Establishing Communication between the NetView System and the Operating System {#c32-i4532}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Establishing Communication between the NetView System and the Operating Systemは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧検査の自動化テーブル 状態判定で Establishing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Establishing 機能の出力を取らず復旧検査の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、復旧検査の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では Establishing 機能 は「復旧検査の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では Establishing 機能の属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では Establishing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Establishing Coordinated Automation {#c32-i4533}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Establishing Coordinated Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.331) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.331)

??? question "確認問題（1問）"
    **問題.** 監査検査の自動化テーブル 状態判定でネットビューの運用確認を行います。Establishing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査検査の採否を説明欄に結び付ける。 ✅
    - D. Establishing 機能の属性行を読まず監査検査の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では Establishing 機能 は「IBM Z NetViewで Establishing 機能の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では Establishing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では Establishing 機能の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Event/Automation Service {#c32-i4534}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Event/Automation Serviceは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.369) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.369)


### Example of SNMP trap automation {#c32-i4535}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Example of SNMP trap automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出判定の自動化テーブル 状態判定でネットビューの運用確認を行います。Example 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出判定で再確認できる形にする。 ✅
    - D. Example 機能の属性行を読まず呼出判定の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では Example 機能 は「IBM Z NetViewで Example 機能の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では Example 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では Example 機能の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Example of a Message Revision Table {#c32-i4536}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Example of a Message Revision Tableは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文判定の自動化テーブル 状態判定に関係する Example 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文判定の確認にする。 ✅
    - B. Example 機能の名称と担当者名のみを残して構文判定の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では Example 機能 は「Example 機能の用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの Example 機能と DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では Example 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Example of an Automation-Table Listing {#c32-i4537}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Example of an Automation-Table Listingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開判定の自動化テーブル 状態判定で Example 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Example 機能の出力を取らず展開判定の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、展開判定の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して展開判定の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では Example 機能 は「展開判定の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では Example 機能の属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では Example 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Examples of Using NetView Program Interfaces {#c32-i4538}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Examples of Using NetView Program Interfacesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換判定の自動化テーブル 状態判定に関する Examples 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Examples 機能の変更点を出力本文から切り離して置換判定の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換判定の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では Examples 機能 は「Examples 機能の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では Examples 機能の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では Examples 機能を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Exclusion or Inclusion Lists {#c32-i4539}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Exclusion or Inclusion Listsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.504) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.504)

??? question "確認問題（1問）"
    **問題.** 終端判定の自動化テーブル 状態判定に関係する Exclusion 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端判定の根拠を固定する。 ✅
    - B. Exclusion 機能の名称と担当者名のみを残して終端判定の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では Exclusion 機能 は「Exclusion 機能の用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの Exclusion 機能と DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では Exclusion 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtering Alerts {#c32-i4540}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Filtering Alertsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.301) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.301)

??? question "確認問題（1問）"
    **問題.** 上書判定の自動化テーブル 状態判定でネットビューの運用確認を行います。Filtering Alertsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、上書判定の証跡として残す。 ✅
    - D. Filtering Alertsの属性行を読まず上書判定の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では Filtering Alerts は「IBM Z NetViewで Filtering Alertsの扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では Filtering Alertsの表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では Filtering Alertsの使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Flow Descriptions {#c32-i4541}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Flow Descriptionsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.488) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.488)

??? question "確認問題（1問）"
    **問題.** 出力判定の自動化テーブル 状態判定に関する Flow Descriptionsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力判定の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Flow Descriptionsの変更点を出力本文から切り離して出力判定の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力判定の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では Flow Descriptions は「Flow Descriptionsの状態と出力メッセージを結び付ける出力判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では Flow Descriptionsの出力行と DSI633I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では Flow Descriptionsを IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Flow Diagrams {#c32-i4542}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Flow Diagramsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.479) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.479)

??? question "確認問題（1問）"
    **問題.** 条件判定の自動化テーブル 状態判定に関係する Flow Diagramsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件判定の根拠にする。 ✅
    - B. Flow Diagramsの名称と担当者名のみを残して条件判定の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Flow Diagrams は「Flow Diagramsの用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの Flow Diagramsと DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Flow Diagramsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Focal Point Support Unique to the NetView Program {#c32-i4543}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Focal Point Support Unique to the NetView Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切判定の自動化テーブル 状態判定で Focal 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Focal 機能の出力を取らず区切判定の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、区切判定の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して区切判定の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Focal 機能 は「区切判定の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Focal 機能の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Focal 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Full-Screen Functions and the Terminal Access Facility {#c32-i4544}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Full-Screen Functions and the Terminal Access Facilityは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲判定の自動化テーブル 状態判定でネットビューの運用確認を行います。Full-Screen 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、範囲判定の採否を説明欄に結び付ける。 ✅
    - D. Full-Screen 機能の属性行を読まず範囲判定の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では Full-Screen 機能 は「IBM Z NetViewで Full-Screen 機能の扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では Full-Screen 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では Full-Screen 機能の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### General Processing of CONSOLE and COMMAND Inclusion and Exclusion Lists {#c32-i4545}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

General Processing of CONSOLE and COMMAND Inclusion and Exclusion Listsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先判定の自動化テーブル 状態判定に関する General 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先判定の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. General 機能の変更点を出力本文から切り離して優先判定の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先判定として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では General 機能 は「General 機能の状態と出力メッセージを結び付ける優先判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では General 機能の出力行と DSI633I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では General 機能を IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Hardware Monitor Alerts {#c32-i4546}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Hardware Monitor Alertsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.420) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.420)

??? question "確認問題（1問）"
    **問題.** 記録判定の自動化テーブル 状態判定に関係する Hardware 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録判定の確認にする。 ✅
    - B. Hardware 機能の名称と担当者名のみを残して記録判定の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では Hardware 機能 は「Hardware 機能の用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewの Hardware 機能と DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では Hardware 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How Foreign Messages are Processed {#c32-i4547}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

How Foreign Messages are Processedは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.97) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.97)

??? question "確認問題（1問）"
    **問題.** 比較判定の自動化テーブル 状態判定で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず比較判定の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、比較判定の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して比較判定の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では How 機能 は「比較判定の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では How 機能の属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では How 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How TAF Works {#c32-i4548}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

How TAF Worksは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.391) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.391)

??? question "確認問題（1問）"
    **問題.** 順序判定の自動化テーブル 状態判定でネットビューの運用確認を行います。How TAF Worksの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序判定で再確認できる形にする。 ✅
    - D. How TAF Worksの属性行を読まず順序判定の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では How TAF Works は「IBM Z NetViewで How TAF Worksの扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では How TAF Worksの表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では How TAF Worksの使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How to Consolidate Consoles {#c32-i4549}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

How to Consolidate Consolesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域判定の自動化テーブル 状態判定に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して値域判定の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域判定の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では How 機能の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では How 機能を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### IBM Z System Automation {#c32-i4550}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

IBM Z System Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.64) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.64)


### IF-THEN Statement {#c32-i4551}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

IF-THEN Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.161) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.161)

??? question "確認問題（1問）"
    **問題.** 構文整理の自動化テーブル 状態判定に関係する IF-THEN Statementの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文整理の根拠にする。 ✅
    - B. IF-THEN Statementの名称と担当者名のみを残して構文整理の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では IF-THEN Statement は「IF-THEN Statementの用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの IF-THEN Statementと DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では IF-THEN Statementを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Identifying Events with the Automation Table {#c32-i4552}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Identifying Events with the Automation Tableは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧判定の自動化テーブル 状態判定で Identifying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Identifying 機能の出力を取らず復旧判定の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を復旧判定で確認する。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では Identifying 機能 は「復旧判定の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では Identifying 機能の属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では Identifying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Identifying Unsuppressable Messages {#c32-i4553}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Identifying Unsuppressable Messagesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.477) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.477)

??? question "確認問題（1問）"
    **問題.** 変更判定の自動化テーブル 状態判定に関する Identifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Identifying 機能の変更点を出力本文から切り離して変更判定の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更判定の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Identifying 機能 は「Identifying 機能の状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Identifying 機能の出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Identifying 機能を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Identifying the Goals of Your Organization {#c32-i4554}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Identifying the Goals of Your Organizationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査判定の自動化テーブル 状態判定でネットビューの運用確認を行います。Identifying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、監査判定の証跡として残す。 ✅
    - D. Identifying 機能の属性行を読まず監査判定の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Identifying 機能 は「IBM Z NetViewで Identifying 機能の扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Identifying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Identifying 機能の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementation {#c32-i4555}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Implementationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開整理の自動化テーブル 状態判定で Implementationの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Implementationの出力を取らず展開整理の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開整理の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開整理の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では Implementation は「展開整理の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では Implementationの属性行と DSI633I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では Implementationを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementation Tasks {#c32-i4556}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Implementation Tasksは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.85) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.85)

??? question "確認問題（1問）"
    **問題.** 呼出整理の自動化テーブル 状態判定でネットビューの運用確認を行います。Implementation 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出整理の採否を説明欄に結び付ける。 ✅
    - D. Implementation 機能の属性行を読まず呼出整理の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では Implementation 機能 は「IBM Z NetViewで Implementation 機能の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では Implementation 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では Implementation 機能の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Implementing Automation Incrementally {#c32-i4557}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Implementing Automation Incrementallyは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端整理の自動化テーブル 状態判定に関係する Implementing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端整理の確認にする。 ✅
    - B. Implementing 機能の名称と担当者名のみを残して終端整理の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端整理の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では Implementing 機能 は「Implementing 機能の用途をネットビューの表示で確認する終端整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの Implementing 機能と DSI633I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では Implementing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementing an Automation Project {#c32-i4558}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Implementing an Automation Projectは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換整理の自動化テーブル 状態判定に関する Implementing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Implementing 機能の変更点を出力本文から切り離して置換整理の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換整理として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では Implementing 機能 は「Implementing 機能の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では Implementing 機能の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では Implementing 機能を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Including Forwarding {#c32-i4559}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Including Forwardingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.342) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.342)

??? question "確認問題（1問）"
    **問題.** 探索整理の自動化テーブル 状態判定で Including 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Including 機能の出力を取らず探索整理の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、探索整理の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して探索整理の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Including 機能 は「探索整理の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Including 機能の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Including 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Installation Exit DSIEX02A {#c32-i4560}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Installation Exit DSIEX02Aは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.289) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.289)

??? question "確認問題（1問）"
    **問題.** 上書整理の自動化テーブル 状態判定でネットビューの運用確認を行います。Installation 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書整理で再確認できる形にする。 ✅
    - D. Installation 機能の属性行を読まず上書整理の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では Installation 機能 は「IBM Z NetViewで Installation 機能の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では Installation 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では Installation 機能の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Installation Exit DSIEX17 {#c32-i4561}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Installation Exit DSIEX17は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.290) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.290)

??? question "確認問題（1問）"
    **問題.** 出力整理の自動化テーブル 状態判定に関する Installation 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力整理の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Installation 機能の変更点を出力本文から切り離して出力整理の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力整理の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では Installation 機能 は「Installation 機能の状態と出力メッセージを結び付ける出力整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では Installation 機能の出力行と DSI633I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では Installation 機能を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Installation Exit XITCI for BNJDSERV {#c32-i4562}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Installation Exit XITCI for BNJDSERVは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件整理の自動化テーブル 状態判定に関係する Installation 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件整理の根拠を固定する。 ✅
    - B. Installation 機能の名称と担当者名のみを残して条件整理の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では Installation 機能 は「Installation 機能の用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの Installation 機能と DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では Installation 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Installation Exits {#c32-i4563}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Installation Exitsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.289) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.289)


### Installation Exits DSIEX16 and DSIEX16B {#c32-i4564}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Installation Exits DSIEX16 and DSIEX16Bは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲整理の自動化テーブル 状態判定でネットビューの運用確認を行います。Installation 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、範囲整理の証跡として残す。 ✅
    - D. Installation 機能の属性行を読まず範囲整理の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Installation 機能 は「IBM Z NetViewで Installation 機能の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Installation 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Installation 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Installing Multiple NetView Programs {#c32-i4565}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Installing Multiple NetView Programsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録整理の自動化テーブル 状態判定に関係する Installing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録整理の根拠にする。 ✅
    - B. Installing 機能の名称と担当者名のみを残して記録整理の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では Installing 機能 は「Installing 機能の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの Installing 機能と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では Installing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Installing and Testing Before Distribution {#c32-i4566}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Installing and Testing Before Distributionは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先整理の自動化テーブル 状態判定に関する Installing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Installing 機能の変更点を出力本文から切り離して優先整理の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先整理の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では Installing 機能 は「Installing 機能の状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では Installing 機能の出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では Installing 機能を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Introducing Automation {#c32-i4567}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Introducing Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.35) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.35)

??? question "確認問題（1問）"
    **問題.** 比較整理の自動化テーブル 状態判定で Introducing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Introducing 機能の出力を取らず比較整理の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較整理の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較整理の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では Introducing 機能 は「比較整理の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では Introducing 機能の属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では Introducing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Introducing NetView Automation {#c32-i4568}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Introducing NetView Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.37) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.37)

??? question "確認問題（1問）"
    **問題.** 順序整理の自動化テーブル 状態判定でネットビューの運用確認を行います。Introducing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序整理の採否を説明欄に結び付ける。 ✅
    - D. Introducing 機能の属性行を読まず順序整理の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では Introducing 機能 は「IBM Z NetViewで Introducing 機能の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では Introducing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では Introducing 機能の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Introducing the Resource Object Data Manager {#c32-i4569}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Introducing the Resource Object Data Managerは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域整理の自動化テーブル 状態判定に関する Introducing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域整理の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Introducing 機能の変更点を出力本文から切り離して値域整理の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域整理として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Introducing 機能 は「Introducing 機能の状態と出力メッセージを結び付ける値域整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Introducing 機能の出力行と DSI633I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Introducing 機能を IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Issuing Commands from RODM Methods {#c32-i4570}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Issuing Commands from RODM Methodsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧整理の自動化テーブル 状態判定で Issuing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Issuing 機能の出力を取らず復旧整理の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧整理の点検結果を残す。 ✅
    - C. RODMVIEW を省略して復旧整理の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Issuing 機能 は「復旧整理の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Issuing 機能の属性行と EKG000I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Issuing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Issuing an MVS Command from a NetView Operator ID {#c32-i4571}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Issuing an MVS Command from a NetView Operator IDは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告整理の自動化テーブル 状態判定に関係する Issuing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告整理の確認にする。 ✅
    - B. Issuing 機能の名称と担当者名のみを残して警告整理の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告整理の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Issuing 機能 は「Issuing 機能の用途をネットビューの表示で確認する警告整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの Issuing 機能と DSI633I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Issuing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Job Entry Subsystem 3 (JES3) Automation {#c32-i4572}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Job Entry Subsystem 3 (JES3) Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.439) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.439)

??? question "確認問題（1問）"
    **問題.** 監査整理の自動化テーブル 状態判定でネットビューの運用確認を行います。Job 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査整理で再確認できる形にする。 ✅
    - D. Job 機能の属性行を読まず監査整理の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Job 機能 は「IBM Z NetViewで Job 機能の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Job 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Job 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LIST TIMER and PURGE TIMER {#c32-i4573}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

LIST TIMER and PURGE TIMERは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更整理の自動化テーブル 状態判定に関する LIST 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. LIST 機能の変更点を出力本文から切り離して変更整理の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更整理の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では LIST 機能 は「LIST 機能の状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では LIST 機能の出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では LIST 機能を IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Loading Command Lists into Storage {#c32-i4574}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Loading Command Lists into Storageは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Locating and Renaming the Sample Set for Automation {#c32-i4575}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Locating and Renaming the Sample Set for Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開記録の自動化テーブル 状態判定で Locating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Locating 機能の出力を取らず展開記録の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を展開記録で確認する。 ✅
    - C. BROWSE CANZLOG を省略して展開記録の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Locating 機能 は「展開記録の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Locating 機能の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Locating 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Log Analysis Program {#c32-i4576}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Log Analysis Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.415) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.415)

??? question "確認問題（1問）"
    **問題.** 呼出記録の自動化テーブル 状態判定でネットビューの運用確認を行います。Log 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、呼出記録の証跡として残す。 ✅
    - D. Log 機能の属性行を読まず呼出記録の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Log 機能 は「IBM Z NetViewで Log 機能の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Log 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Log 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Log Analysis Samples {#c32-i4577}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Log Analysis Samplesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.549) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.549)

??? question "確認問題（1問）"
    **問題.** 置換記録の自動化テーブル 状態判定に関する Log 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Log 機能の変更点を出力本文から切り離して置換記録の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換記録の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Log 機能 は「Log 機能の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Log 機能の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Log 機能を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Logging {#c32-i4578}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Loggingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.435) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.435)


### Logging Considerations {#c32-i4579}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Logging Considerationsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.435) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.435)

??? question "確認問題（1問）"
    **問題.** 探索記録の自動化テーブル 状態判定で Logging 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Logging 機能の出力を取らず探索記録の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、探索記録の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して探索記録の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Logging 機能 は「探索記録の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Logging 機能の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Logging 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Logging Intrasystem Automation {#c32-i4580}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Logging Intrasystem Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.342) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.342)

??? question "確認問題（1問）"
    **問題.** 上書記録の自動化テーブル 状態判定でネットビューの運用確認を行います。Logging 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、上書記録の採否を説明欄に結び付ける。 ✅
    - D. Logging 機能の属性行を読まず上書記録の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Logging 機能 は「IBM Z NetViewで Logging 機能の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Logging 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Logging 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Logical PARMLIB Member - CNMCAUaa {#c32-i4581}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Logical PARMLIB Member - CNMCAUaaは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.505) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.505)

??? question "確認問題（1問）"
    **問題.** 出力記録の自動化テーブル 状態判定に関する Logical 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Logical 機能の変更点を出力本文から切り離して出力記録の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力記録として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Logical 機能 は「Logical 機能の状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Logical 機能の出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Logical 機能を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVS Command Management (Deprecated) {#c32-i4582}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS Command Management (Deprecated)は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.501) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.501)

??? question "確認問題（1問）"
    **問題.** 出力分離の自動化テーブル 状態判定に関する MVS 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力分離の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. MVS 機能の変更点を出力本文から切り離して出力分離の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力分離の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では MVS 機能 は「MVS 機能の状態と出力メッセージを結び付ける出力分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では MVS 機能の出力行と DSI633I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では MVS 機能を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVS Command Management Processing on the NetView Program {#c32-i4583}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS Command Management Processing on the NetView Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件分離の自動化テーブル 状態判定に関係する MVS 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件分離の根拠にする。 ✅
    - B. MVS 機能の名称と担当者名のみを残して条件分離の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件分離の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件分離の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では MVS 機能 は「MVS 機能の用途をネットビューの表示で確認する条件分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM Z NetViewの MVS 機能と DSI633I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では MVS 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### MVS Commands Issued by the NetView Program {#c32-i4584}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS Commands Issued by the NetView Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切分離の自動化テーブル 状態判定で MVS 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MVS 機能の出力を取らず区切分離の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、区切分離の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して区切分離の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では MVS 機能 は「区切分離の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では MVS 機能の属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では MVS 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### MVS Message and Command Processing {#c32-i4585}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS Message and Command Processingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲分離の自動化テーブル 状態判定でネットビューの運用確認を行います。MVS 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、範囲分離の採否を説明欄に結び付ける。 ✅
    - D. MVS 機能の属性行を読まず範囲分離の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では MVS 機能 は「IBM Z NetViewで MVS 機能の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では MVS 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では MVS 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### MVS Sysplex {#c32-i4586}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS Sysplexは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.95) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.95)

??? question "確認問題（1問）"
    **問題.** 優先分離の自動化テーブル 状態判定に関する MVS Sysplexの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先分離の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. MVS Sysplexの変更点を出力本文から切り離して優先分離の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先分離として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では MVS Sysplex は「MVS Sysplexの状態と出力メッセージを結び付ける優先分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では MVS Sysplexの出力行と DSI633I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では MVS Sysplexを IBM Z NetViewの確認記録に残し、対象名は優先分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVS System Log (SYSLOG) {#c32-i4587}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS System Log (SYSLOG)は、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.436) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.436)

??? question "確認問題（1問）"
    **問題.** 記録分離の自動化テーブル 状態判定に関係する MVS System Log 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録分離の確認にする。 ✅
    - B. MVS System Log 属性の名称と担当者名のみを残して記録分離の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では MVS System Log 属性 は「MVS System Log 属性の用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの MVS System Log 属性と DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では MVS System Log 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVS System Log and NetView Network Log Records {#c32-i4588}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

MVS System Log and NetView Network Log Recordsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較分離の自動化テーブル 状態判定で MVS 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MVS 機能の出力を取らず比較分離の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、比較分離の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して比較分離の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では MVS 機能 は「比較分離の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では MVS 機能の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では MVS 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Multiple Automation Tables {#c32-i4589}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Managing Multiple Automation Tablesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Managing Multiple RODM Data Caches {#c32-i4590}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Managing Multiple RODM Data Cachesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切記録の自動化テーブル 状態判定で Managing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Managing 機能の出力を取らず区切記録の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、区切記録の点検結果を残す。 ✅
    - C. RODMVIEW を省略して区切記録の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Managing 機能 は「区切記録の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切記録項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Managing 機能の属性行と EKG000I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Managing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Message Flooding Prevention Table {#c32-i4591}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Flooding Prevention Tableは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.475) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.475)

??? question "確認問題（1問）"
    **問題.** 優先記録の自動化テーブル 状態判定に関する Message 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先記録の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Message 機能の変更点を出力本文から切り離して優先記録の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、優先記録の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Message 機能 は「Message 機能の状態と出力メッセージを結び付ける優先記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Message 機能の出力行と DSI633I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Message 機能を IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Flow in MVS {#c32-i4592}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Flow in MVSは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.467) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.467)

??? question "確認問題（1問）"
    **問題.** 比較記録の自動化テーブル 状態判定で Message 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Message 機能の出力を取らず比較記録の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を比較記録で確認する。 ✅
    - C. BROWSE CANZLOG を省略して比較記録の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Message 機能 は「比較記録の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Message 機能の属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Message 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Flow in a JES3 Complex {#c32-i4593}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Flow in a JES3 Complexは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録記録の自動化テーブル 状態判定に関係する Message 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録記録の根拠を固定する。 ✅
    - B. Message 機能の名称と担当者名のみを残して記録記録の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Message 機能 は「Message 機能の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの Message 機能と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Message 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Message Processing Facility {#c32-i4594}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Processing Facilityは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.467) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.467)

??? question "確認問題（1問）"
    **問題.** 順序記録の自動化テーブル 状態判定でネットビューの運用確認を行います。Message 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、順序記録の証跡として残す。 ✅
    - D. Message 機能の属性行を読まず順序記録の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Message 機能 は「IBM Z NetViewで Message 機能の扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Message 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Message 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Revision Table {#c32-i4595}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Revision Tableは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.137) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.137)

??? question "確認問題（1問）"
    **問題.** 値域記録の自動化テーブル 状態判定に関する Message 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Message 機能の変更点を出力本文から切り離して値域記録の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域記録の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では Message 機能 は「Message 機能の状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では Message 機能の出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では Message 機能を IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Revision Table Testing {#c32-i4596}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Revision Table Testingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.143) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.143)

??? question "確認問題（1問）"
    **問題.** 警告記録の自動化テーブル 状態判定に関係する Message 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告記録の根拠にする。 ✅
    - B. Message 機能の名称と担当者名のみを残して警告記録の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Message 機能 は「Message 機能の用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの Message 機能と DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Message 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Routing Flow {#c32-i4597}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Routing Flowは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.109) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.109)

??? question "確認問題（1問）"
    **問題.** 復旧記録の自動化テーブル 状態判定で Message 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Message 機能の出力を取らず復旧記録の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、復旧記録の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Message 機能 は「復旧記録の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Message 機能の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Message 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Suppression Samples {#c32-i4598}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Message Suppression Samplesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.549) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.549)

??? question "確認問題（1問）"
    **問題.** 監査記録の自動化テーブル 状態判定でネットビューの運用確認を行います。Message 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査記録の採否を説明欄に結び付ける。 ✅
    - D. Message 機能の属性行を読まず監査記録の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Message 機能 は「IBM Z NetViewで Message 機能の扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Message 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Message 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message and Command Flow in VTAM {#c32-i4599}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Message and Command Flow in VTAMは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲記録の自動化テーブル 状態判定でネットビューの運用確認を行います。Message 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、範囲記録で再確認できる形にする。 ✅
    - D. Message 機能の属性行を読まず範囲記録の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Message 機能 は「IBM Z NetViewで Message 機能の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Message 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Message 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Messages Issued as WTOs to Be Displayed or Processed by the NetView Program {#c32-i4600}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Messages Issued as WTOs to Be Displayed or Processed by the NetView Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文分離の自動化テーブル 状態判定に関係する Messages 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文分離の確認にする。 ✅
    - B. Messages 機能の名称と担当者名のみを残して構文分離の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文分離の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Messages 機能 は「Messages 機能の用途をネットビューの表示で確認する構文分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの Messages 機能と DSI633I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Messages 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Messages and Commands through VTAM Interfaces {#c32-i4601}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Messages and Commands through VTAM Interfacesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更記録の自動化テーブル 状態判定に関する Messages 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Messages 機能の変更点を出力本文から切り離して変更記録の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更記録として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Messages 機能 は「Messages 機能の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Messages 機能の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Messages 機能を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Modifying Command Procedures {#c32-i4602}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Modifying Command Proceduresは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開分離の自動化テーブル 状態判定で Modifying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Modifying 機能の出力を取らず展開分離の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、展開分離の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して展開分離の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では Modifying 機能 は「展開分離の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では Modifying 機能の属性行と DSI633I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では Modifying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring Alerts with the Hardware Monitor {#c32-i4603}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Monitoring Alerts with the Hardware Monitorは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出分離の自動化テーブル 状態判定でネットビューの運用確認を行います。Monitoring 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出分離の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出分離で再確認できる形にする。 ✅
    - D. Monitoring 機能の属性行を読まず呼出分離の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では Monitoring 機能 は「IBM Z NetViewで Monitoring 機能の扱いを記録する呼出分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では Monitoring 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では Monitoring 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring Alerts with the NetView Management Console {#c32-i4604}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Monitoring Alerts with the NetView Management Consoleは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換分離の自動化テーブル 状態判定に関する Monitoring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換分離の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Monitoring 機能の変更点を出力本文から切り離して置換分離の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換分離の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Monitoring 機能 は「Monitoring 機能の状態と出力メッセージを結び付ける置換分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Monitoring 機能の出力行と DSI633I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Monitoring 機能を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### MultiSystem Automation {#c32-i4605}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

MultiSystem Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.339) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.339)

??? question "確認問題（1問）"
    **問題.** 上書分離の自動化テーブル 状態判定でネットビューの運用確認を行います。MultiSystem 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書分離の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、上書分離の証跡として残す。 ✅
    - D. MultiSystem 機能の属性行を読まず上書分離の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では MultiSystem 機能 は「IBM Z NetViewで MultiSystem 機能の扱いを記録する上書分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では MultiSystem 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では MultiSystem 機能の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Multiple Console Support {#c32-i4606}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Multiple Console Supportは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.469) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.469)

??? question "確認問題（1問）"
    **問題.** 終端分離の自動化テーブル 状態判定に関係する Multiple 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端分離の根拠を固定する。 ✅
    - B. Multiple 機能の名称と担当者名のみを残して終端分離の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端分離の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では Multiple 機能 は「Multiple 機能の用途をネットビューの表示で確認する終端分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの Multiple 機能と DSI633I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では Multiple 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Multiple Console Support Operator Use of Command Lists {#c32-i4607}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Multiple Console Support Operator Use of Command Listsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索分離の自動化テーブル 状態判定で Multiple 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Multiple 機能の出力を取らず探索分離の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI039I を含む表示を保存し、説明欄との差分を探索分離で確認する。 ✅
    - C. LIST CLIST を省略して探索分離の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では Multiple 機能 は「探索分離の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索分離項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では Multiple 機能の属性行と DSI039I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では Multiple 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NETVONLY Statement {#c32-i4608}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NETVONLY Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.139) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.139)

??? question "確認問題（1問）"
    **問題.** 条件読解の自動化テーブル 状態判定に関係する NETVONLY Statementの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件読解の根拠を固定する。 ✅
    - B. NETVONLY Statementの名称と担当者名のみを残して条件読解の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件読解の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件読解の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では NETVONLY Statement は「NETVONLY Statementの用途をネットビューの表示で確認する条件読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM Z NetViewの NETVONLY Statementと DSI633I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では NETVONLY Statementを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Architected Focal Point Support {#c32-i4609}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Architected Focal Point Supportは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.347) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.347)

??? question "確認問題（1問）"
    **問題.** 順序分離の自動化テーブル 状態判定でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序分離で再確認できる形にする。 ✅
    - D. NetView 機能の属性行を読まず順序分離の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では NetView 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Commands Issued as Subsystem Commands from an MVS Console {#c32-i4610}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Commands Issued as Subsystem Commands from an MVS Consoleは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域分離の自動化テーブル 状態判定に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して値域分離の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域分離の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NetView Commands Issued with MODIFY (F) Command from an MVS Console {#c32-i4611}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Commands Issued with MODIFY (F) Command from an MVS Consoleは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告分離の自動化テーブル 状態判定に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告分離の根拠を固定する。 ✅
    - B. NetView 機能の名称と担当者名のみを残して警告分離の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NetView Commands Used for TAF {#c32-i4612}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Commands Used for TAFは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧分離の自動化テーブル 状態判定で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず復旧分離の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を復旧分離で確認する。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では NetView 機能 は「復旧分離の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NetView Interfaces and Functions {#c32-i4613}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Interfaces and Functionsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.408) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.408)

??? question "確認問題（1問）"
    **問題.** 監査分離の自動化テーブル 状態判定でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、監査分離の証跡として残す。 ✅
    - D. NetView 機能の属性行を読まず監査分離の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では NetView 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Interfaces with MVS {#c32-i4614}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Interfaces with MVSは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.470) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.470)

??? question "確認問題（1問）"
    **問題.** 変更分離の自動化テーブル 状態判定に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して変更分離の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更分離の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Logging Capabilities {#c32-i4615}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Logging Capabilitiesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.437) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.437)

??? question "確認問題（1問）"
    **問題.** 構文読解の自動化テーブル 状態判定に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文読解の根拠にする。 ✅
    - B. NetView 機能の名称と担当者名のみを残して構文読解の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Message Type (HDRMTYPE) Descriptions {#c32-i4616}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Message Type (HDRMTYPE) Descriptionsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.497) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.497)

??? question "確認問題（1問）"
    **問題.** 展開読解の自動化テーブル 状態判定で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず展開読解の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開読解の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開読解の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では NetView 機能 は「展開読解の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Program Automation Facilities {#c32-i4617}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

NetView Program Automation Facilitiesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.53) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.53)

??? question "確認問題（1問）"
    **問題.** 呼出読解の自動化テーブル 状態判定でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出読解の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出読解の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出読解の採否を説明欄に結び付ける。 ✅
    - D. NetView 機能の属性行を読まず呼出読解の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する呼出読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では NetView 機能の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Program Command Routing {#c32-i4618}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Program Command Routingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.118) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.118)

??? question "確認問題（1問）"
    **問題.** 置換読解の自動化テーブル 状態判定に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換読解の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して置換読解の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換読解として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける置換読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は置換読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Program Hardware-Monitor Data and MSU Routing {#c32-i4619}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Program Hardware-Monitor Data and MSU Routingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端読解の自動化テーブル 状態判定に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端読解の確認にする。 ✅
    - B. NetView 機能の名称と担当者名のみを残して終端読解の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端読解の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端読解の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する終端読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NetView Program Information Routing for Automation {#c32-i4620}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

NetView Program Information Routing for Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索読解の自動化テーブル 状態判定で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず探索読解の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、探索読解の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して探索読解の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では NetView 機能 は「探索読解の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NetView Program Interfaces {#c32-i4621}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Program Interfacesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.101) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.101)

??? question "確認問題（1問）"
    **問題.** 上書読解の自動化テーブル 状態判定でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書読解の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書読解の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書読解で再確認できる形にする。 ✅
    - D. NetView 機能の属性行を読まず上書読解の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する上書読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では NetView 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Program Message Routing {#c32-i4622}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

NetView Program Message Routingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.103) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.103)

??? question "確認問題（1問）"
    **問題.** 出力読解の自動化テーブル 状態判定に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力読解の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して出力読解の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力読解の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける出力読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は出力読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Network Log {#c32-i4623}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Network Logは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.436) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.436)

??? question "確認問題（1問）"
    **問題.** 区切読解の自動化テーブル 状態判定で Network Logの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Network Logの出力を取らず区切読解の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を区切読解で確認する。 ✅
    - C. BROWSE CANZLOG を省略して区切読解の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では Network Log は「区切読解の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では Network Logの属性行と DSI633I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では Network Logを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Numerics {#c32-i4624}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Numericsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.555) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.555)


### OTHERWISE Statement {#c32-i4625}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

OTHERWISE Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.140) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.140)

??? question "確認問題（1問）"
    **問題.** 順序読解の自動化テーブル 状態判定でネットビューの運用確認を行います。OTHERWISE 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序読解の採否を説明欄に結び付ける。 ✅
    - D. OTHERWISE 機能の属性行を読まず順序読解の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では OTHERWISE 機能 は「IBM Z NetViewで OTHERWISE 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では OTHERWISE 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では OTHERWISE 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Obtaining Messages and MSUs {#c32-i4626}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Obtaining Messages and MSUsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Automation Guide (p.123) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.123)

??? question "確認問題（1問）"
    **問題.** 優先読解の自動化テーブル 状態判定に関する Obtaining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先読解の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Obtaining 機能の変更点を出力本文から切り離して優先読解の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先読解の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では Obtaining 機能 は「Obtaining 機能の状態と出力メッセージを結び付ける優先読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では Obtaining 機能の出力行と DSI633I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では Obtaining 機能を IBM Z NetViewの確認記録に残し、対象名は優先読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Operating-System Automation Facilities and Interactions with the NetView Program {#c32-i4627}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Operating-System Automation Facilities and Interactions with the NetView Programは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録読解の自動化テーブル 状態判定に関係する Operating-System 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録読解の根拠にする。 ✅
    - B. Operating-System 機能の名称と担当者名のみを残して記録読解の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Operating-System 機能 は「Operating-System 機能の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの Operating-System 機能と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Operating-System 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Order of matching {#c32-i4628}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Order of matchingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.508) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.508)

??? question "確認問題（1問）"
    **問題.** 比較読解の自動化テーブル 状態判定で Order of matchingの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Order of matchingの出力を取らず比較読解の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較読解の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較読解の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Order of matching は「比較読解の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Order of matchingの属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Order of matchingを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Overview {#c32-i4629}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Overviewは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Overview of Automation Products {#c32-i4630}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Overview of Automation Productsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告読解の自動化テーブル 状態判定に関係する Overview 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告読解の確認にする。 ✅
    - B. Overview 機能の名称と担当者名のみを残して警告読解の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告読解の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Overview 機能 は「Overview 機能の用途をネットビューの表示で確認する警告読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの Overview 機能と DSI633I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Overview 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Overview of Timer Commands {#c32-i4631}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Overview of Timer Commandsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧読解の自動化テーブル 状態判定で Overview 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Overview 機能の出力を取らず復旧読解の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧読解の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧読解の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では Overview 機能 は「復旧読解の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では Overview 機能の属性行と DSI633I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では Overview 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Planning Charts {#c32-i4632}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Planning Chartsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査読解の自動化テーブル 状態判定でネットビューの運用確認を行います。Planning Chartsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査読解の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査読解で再確認できる形にする。 ✅
    - D. Planning Chartsの属性行を読まず監査読解の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では Planning Charts は「IBM Z NetViewで Planning Chartsの扱いを記録する監査読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では Planning Chartsの表示結果と DSI633I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では Planning Chartsの使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Planning for Automation in Selected Environments {#c32-i4633}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Planning for Automation in Selected Environmentsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文検分の自動化テーブル 状態判定に関係する Planning 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文検分の根拠を固定する。 ✅
    - B. Planning 機能の名称と担当者名のみを残して構文検分の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Planning 機能 は「Planning 機能の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの Planning 機能と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Planning 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Planning for Automation in a Sysplex {#c32-i4634}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Planning for Automation in a Sysplexは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更読解の自動化テーブル 状態判定に関する Planning 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Planning 機能の変更点を出力本文から切り離して変更読解の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更読解の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Planning 機能 は「Planning 機能の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Planning 機能の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Planning 機能を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Planning for Extended Multiple Console Support Consoles {#c32-i4635}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Planning for Extended Multiple Console Support Consolesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開検分の自動化テーブル 状態判定で Planning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning 機能の出力を取らず展開検分の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を展開検分で確認する。 ✅
    - C. BROWSE CANZLOG を省略して展開検分の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Planning 機能 は「展開検分の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Planning 機能の属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Planning 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Planning for Using RODM in Automation {#c32-i4636}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Planning for Using RODM in Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出検分の自動化テーブル 状態判定でネットビューの運用確認を行います。Planning 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分の自動化テーブル 状態判定を確認した扱いにする。
    - B. EKG000I の有無を確認せず呼出検分の自動化テーブル 状態判定を正常終了として記録する。
    - C. RODMVIEW の結果から対象行を抜き出し、呼出検分の証跡として残す。 ✅
    - D. Planning 機能の属性行を読まず呼出検分の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では Planning 機能 は「IBM Z NetViewで Planning 機能の扱いを記録する呼出検分項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では Planning 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では Planning 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Policy File Management {#c32-i4637}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Policy File Managementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換検分の自動化テーブル 状態判定に関する Policy 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検分の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Policy 機能の変更点を出力本文から切り離して置換検分の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換検分の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では Policy 機能 は「Policy 機能の状態と出力メッセージを結び付ける置換検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では Policy 機能の出力行と DSI633I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では Policy 機能を IBM Z NetViewの確認記録に残し、対象名は置換検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Policy File Syntax {#c32-i4638}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Policy File Syntaxは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Automation Guide (p.268) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.268)

??? question "確認問題（1問）"
    **問題.** 終端検分の自動化テーブル 状態判定に関係する Policy File Syntaxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端検分の根拠にする。 ✅
    - B. Policy File Syntaxの名称と担当者名のみを残して終端検分の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Policy File Syntax は「Policy File Syntaxの用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの Policy File Syntaxと DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Policy File Syntaxを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Policy Services Overview {#c32-i4639}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Policy Services Overviewは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Automation Guide (p.267) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.267)

??? question "確認問題（1問）"
    **問題.** 探索検分の自動化テーブル 状態判定で Policy 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Policy 機能の出力を取らず探索検分の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、探索検分の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して探索検分の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Policy 機能 は「探索検分の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Policy 機能の属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Policy 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Preparing to Use the Advanced Automation Sample Set {#c32-i4640}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Preparing to Use the Advanced Automation Sample Setは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書検分の自動化テーブル 状態判定でネットビューの運用確認を行います。Preparing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、上書検分の採否を説明欄に結び付ける。 ✅
    - D. Preparing 機能の属性行を読まず上書検分の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では Preparing 機能 は「IBM Z NetViewで Preparing 機能の扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では Preparing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では Preparing 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Processing Determination {#c32-i4641}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Processing Determinationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.469) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.469)

??? question "確認問題（1問）"
    **問題.** 出力検分の自動化テーブル 状態判定に関する Processing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Processing 機能の変更点を出力本文から切り離して出力検分の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力検分として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では Processing 機能 は「Processing 機能の状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では Processing 機能の出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では Processing 機能を IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Production {#c32-i4642}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Productionは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.459) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.459)

??? question "確認問題（1問）"
    **問題.** 条件検分の自動化テーブル 状態判定に関係する Productionの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件検分の確認にする。 ✅
    - B. Productionの名称と担当者名のみを残して条件検分の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検分の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Production は「Productionの用途をネットビューの表示で確認する条件検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの Productionと DSI633I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Productionを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Production Tasks {#c32-i4643}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Production Tasksは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.85) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.85)

??? question "確認問題（1問）"
    **問題.** 区切検分の自動化テーブル 状態判定で Production Tasksの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Production Tasksの出力を取らず区切検分の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、区切検分の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して区切検分の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Production Tasks は「区切検分の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Production Tasksの属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Production Tasksを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Project Definition {#c32-i4644}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Project Definitionは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.456) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.456)

??? question "確認問題（1問）"
    **問題.** 範囲検分の自動化テーブル 状態判定でネットビューの運用確認を行います。Project Definitionの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分の自動化テーブル 状態判定を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、範囲検分で再確認できる形にする。 ✅
    - D. Project Definitionの属性行を読まず範囲検分の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Project Definition は「IBM Z NetViewで Project Definitionの扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Project Definitionの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Project Definitionの使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Project Definition Tasks {#c32-i4645}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Project Definition Tasksは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.69) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.69)

??? question "確認問題（1問）"
    **問題.** 優先検分の自動化テーブル 状態判定に関する Project 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Project 機能の変更点を出力本文から切り離して優先検分の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、優先検分の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Project 機能 は「Project 機能の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Project 機能の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Project 機能を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Project Design Tasks {#c32-i4646}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Project Design Tasksは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.77) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.77)

??? question "確認問題（1問）"
    **問題.** 記録検分の自動化テーブル 状態判定に関係する Project 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録検分の根拠を固定する。 ✅
    - B. Project 機能の名称と担当者名のみを残して記録検分の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Project 機能 は「Project 機能の用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewの Project 機能と DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Project 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Propagating Automation to Other NetView Systems {#c32-i4647}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Propagating Automation to Other NetView Systemsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較検分の自動化テーブル 状態判定で Propagating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Propagating 機能の出力を取らず比較検分の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を比較検分で確認する。 ✅
    - C. BROWSE CANZLOG を省略して比較検分の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Propagating 機能 は「比較検分の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Propagating 機能の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Propagating 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Protecting MVS Command Management Processing {#c32-i4648}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Protecting MVS Command Management Processingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.513) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.513)

??? question "確認問題（1問）"
    **問題.** 順序検分の自動化テーブル 状態判定でネットビューの運用確認を行います。Protecting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検分の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、順序検分の証跡として残す。 ✅
    - D. Protecting 機能の属性行を読まず順序検分の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Protecting 機能 は「IBM Z NetViewで Protecting 機能の扱いを記録する順序検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Protecting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Protecting 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Putting Your Automation Statements into Effect {#c32-i4649}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Putting Your Automation Statements into Effectは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.328) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.328)

??? question "確認問題（1問）"
    **問題.** 値域検分の自動化テーブル 状態判定に関する Putting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Putting 機能の変更点を出力本文から切り離して値域検分の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域検分の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Putting 機能 は「Putting 機能の状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Putting 機能の出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Putting 機能を IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### REVISE Statement {#c32-i4650}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

REVISE Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.140) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.140)

??? question "確認問題（1問）"
    **問題.** 構文確認の自動化テーブル 状態判定に関係する REVISE Statementの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を構文確認で確認する。 ✅
    - B. REVISE Statementの名称と担当者名のみを残して構文確認の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文確認の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文確認の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では REVISE Statement は「REVISE Statementの用途をネットビューの表示で確認する構文確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Z NetViewの REVISE Statementと DSI633I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では REVISE Statementを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Required NetView Tasks {#c32-i4651}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Required NetView Tasksは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.268) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.268)

??? question "確認問題（1問）"
    **問題.** 警告検分の自動化テーブル 状態判定に関係する Required 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告検分の根拠にする。 ✅
    - B. Required 機能の名称と担当者名のみを残して警告検分の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検分の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検分の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Required 機能 は「Required 機能の用途をネットビューの表示で確認する警告検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM Z NetViewの Required 機能と DSI633I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Required 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Resource Controls, Task Priorities, and Multitasking {#c32-i4652}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Resource Controls, Task Priorities, and Multitaskingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧検分の自動化テーブル 状態判定で Resource 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Resource 機能の出力を取らず復旧検分の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、復旧検分の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Resource 機能 は「復旧検分の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Resource 機能の属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Resource 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Resource Recovery and Thresholds {#c32-i4653}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Resource Recovery and Thresholdsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Automation Guide (p.399) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.399)

??? question "確認問題（1問）"
    **問題.** 監査検分の自動化テーブル 状態判定でネットビューの運用確認を行います。Resource 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検分の自動化テーブル 状態判定を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査検分の採否を説明欄に結び付ける。 ✅
    - D. Resource 機能の属性行を読まず監査検分の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Resource 機能 は「IBM Z NetViewで Resource 機能の扱いを記録する監査検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Resource 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Resource 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Restrictions {#c32-i4654}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Restrictionsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Running Multiple NetView Programs Per System {#c32-i4655}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Running Multiple NetView Programs Per Systemは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開確認の自動化テーブル 状態判定で Running 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Running 機能の出力を取らず展開確認の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、展開確認の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して展開確認の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Running 機能 は「展開確認の自動化テーブル 状態判定に関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Running 機能の属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Running 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SELECT Statement {#c32-i4656}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

SELECT Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.140) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.140)

??? question "確認問題（1問）"
    **問題.** 出力確認の自動化テーブル 状態判定に関する SELECT Statementの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力確認の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. SELECT Statementの変更点を出力本文から切り離して出力確認の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力確認の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では SELECT Statement は「SELECT Statementの状態と出力メッセージを結び付ける出力確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では SELECT Statementの出力行と DSI633I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では SELECT Statementを IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SNMP Trap Automation {#c32-i4657}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

SNMP Trap Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.445) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.445)

??? question "確認問題（1問）"
    **問題.** 比較確認の自動化テーブル 状態判定で SNMP 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SNMP 機能の出力を取らず比較確認の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較確認の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較確認の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では SNMP 機能 は「比較確認の自動化テーブル 状態判定に関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では SNMP 機能の属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では SNMP 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SNMP Trap Automation CP-MSU {#c32-i4658}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

SNMP Trap Automation CP-MSUは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.448) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.448)

??? question "確認問題（1問）"
    **問題.** 順序確認の自動化テーブル 状態判定でネットビューの運用確認を行います。SNMP 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序確認の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序確認の自動化テーブル 状態判定を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序確認の確認記録にまとめる。 ✅
    - D. SNMP 機能の属性行を読まず順序確認の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では SNMP 機能 は「IBM Z NetViewで SNMP 機能の扱いを記録する順序確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では SNMP 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では SNMP 機能の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SYN Statement {#c32-i4659}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

SYN Statementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.237) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.237)

??? question "確認問題（1問）"
    **問題.** 範囲照合の自動化テーブル 状態判定でネットビューの運用確認を行います。SYN Statementの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲照合の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲照合の自動化テーブル 状態判定を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲照合として引き継ぐ。 ✅
    - D. SYN Statementの属性行を読まず範囲照合の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では SYN Statement は「IBM Z NetViewで SYN Statementの扱いを記録する範囲照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では SYN Statementの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では SYN Statementの使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Sample Progress Measurements {#c32-i4660}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Sample Progress Measurementsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.463) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.463)

??? question "確認問題（1問）"
    **問題.** 呼出確認の自動化テーブル 状態判定でネットビューの運用確認を行います。Sample 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出確認の自動化テーブル 状態判定を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出確認の確認記録にまとめる。 ✅
    - D. Sample 機能の属性行を読まず呼出確認の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Sample 機能 は「IBM Z NetViewで Sample 機能の扱いを記録する呼出確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Sample 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Sample 機能の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Sample Project Plan {#c32-i4661}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Sample Project Planは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.455) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.455)

??? question "確認問題（1問）"
    **問題.** 置換確認の自動化テーブル 状態判定に関する Sample 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Sample 機能の変更点を出力本文から切り離して置換確認の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Sample 機能 は「Sample 機能の状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Sample 機能の出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Sample 機能を IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Saving Information {#c32-i4662}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Saving Informationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.124) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.124)

??? question "確認問題（1問）"
    **問題.** 探索確認の自動化テーブル 状態判定で Saving Informationの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Saving Informationの出力を取らず探索確認の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、探索確認の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して探索確認の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Saving Information は「探索確認の自動化テーブル 状態判定に関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Saving Informationの属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Saving Informationを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Saving and Restoring Timer Commands {#c32-i4663}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Saving and Restoring Timer Commandsは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端確認の自動化テーブル 状態判定に関係する Saving 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端確認の結果として保存する。 ✅
    - B. Saving 機能の名称と担当者名のみを残して終端確認の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端確認の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端確認の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Saving 機能 は「Saving 機能の用途をネットビューの表示で確認する終端確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Z NetViewの Saving 機能と DSI633I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Saving 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Securing Commitment {#c32-i4664}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Securing Commitmentは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.76) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.76)

??? question "確認問題（1問）"
    **問題.** 上書確認の自動化テーブル 状態判定でネットビューの運用確認を行います。Securing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認の自動化テーブル 状態判定を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書確認として引き継ぐ。 ✅
    - D. Securing 機能の属性行を読まず上書確認の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Securing 機能 は「IBM Z NetViewで Securing 機能の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Securing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Securing 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Sending Email or Alphanumeric Pages {#c32-i4665}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Sending Email or Alphanumeric Pagesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件確認の自動化テーブル 状態判定に関係する Sending 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件確認の点検結果を残す。 ✅
    - B. Sending 機能の名称と担当者名のみを残して条件確認の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件確認の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件確認の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では Sending 機能 は「Sending 機能の用途をネットビューの表示で確認する条件確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Z NetViewの Sending 機能と DSI633I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では Sending 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setting Up Communication between the NetView Program and MVS {#c32-i4666}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Setting Up Communication between the NetView Program and MVSは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切確認の自動化テーブル 状態判定で Setting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Setting 機能の出力を取らず区切確認の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切確認で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して区切確認の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Setting 機能 は「区切確認の自動化テーブル 状態判定に関係する定義値と表示行を照合する区切確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Setting 機能の属性行と DSI633I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Setting 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setting Up TAF {#c32-i4667}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Setting Up TAFは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲確認の自動化テーブル 状態判定でネットビューの運用確認を行います。Setting Up TAF の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲確認の自動化テーブル 状態判定を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲確認の確認値として扱う。 ✅
    - D. Setting Up TAF の属性行を読まず範囲確認の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Setting Up TAF は「IBM Z NetViewで Setting Up TAF の扱いを記録する範囲確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Setting Up TAF の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Setting Up TAF の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setup Samples {#c32-i4668}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Setup Samplesは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.549) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.549)

??? question "確認問題（1問）"
    **問題.** 優先確認の自動化テーブル 状態判定に関する Setup Samplesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先確認の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Setup Samplesの変更点を出力本文から切り離して優先確認の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先確認の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Setup Samples は「Setup Samplesの状態と出力メッセージを結び付ける優先確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Setup Samplesの出力行と DSI633I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Setup Samplesを IBM Z NetViewの確認記録に残し、対象名は優先確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Single-System Automation {#c32-i4669}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Single-System Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.291) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.291)

??? question "確認問題（1問）"
    **問題.** 記録確認の自動化テーブル 状態判定に関係する Single-System 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を記録確認で確認する。 ✅
    - B. Single-System 機能の名称と担当者名のみを残して記録確認の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録確認の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Single-System 機能 は「Single-System 機能の用途をネットビューの表示で確認する記録確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewの Single-System 機能と DSI633I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Single-System 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Solicited and Unsolicited System MVS Extended Console Messages for an OST, NNT, or Autotask {#c32-i4670}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Solicited and Unsolicited System MVS Extended Console Messages for an OST, NNT, or Autotaskは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Solicited and Unsolicited System MVS Extended Console Messages for the PPT {#c32-i4671}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Solicited and Unsolicited System MVS Extended Console Messages for the PPTは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告確認の自動化テーブル 状態判定に関係する Solicited 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告確認の結果として保存する。 ✅
    - B. Solicited 機能の名称と担当者名のみを残して警告確認の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Solicited 機能 は「Solicited 機能の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの Solicited 機能と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Solicited 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stages of Automation {#c32-i4672}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 上級

Stages of Automationは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Automation Guide (p.40) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Automation Guide (p.40)

??? question "確認問題（1問）"
    **問題.** 復旧確認の自動化テーブル 状態判定で Stages 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Stages 機能の出力を取らず復旧確認の自動化テーブル 状態判定の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧確認の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認の自動化テーブル 状態判定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の自動化テーブル 状態判定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Stages 機能 は「復旧確認の自動化テーブル 状態判定に関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Stages 機能の属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Stages 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Starting MVS Command Management {#c32-i4673}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Starting MVS Command Managementは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査確認の自動化テーブル 状態判定でネットビューの運用確認を行います。Starting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認の自動化テーブル 状態判定を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認の自動化テーブル 状態判定を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査確認として引き継ぐ。 ✅
    - D. Starting 機能の属性行を読まず監査確認の自動化テーブル 状態判定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Starting 機能 は「IBM Z NetViewで Starting 機能の扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Starting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Starting 機能の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Starting MVS Command Processing {#c32-i4674}
*分類: 自動化テーブル / 状態判定*  ・  難易度: 中級

Starting MVS Command Processingは、Tivoli NetView z/OS 自動化の自動化テーブル / 状態判定で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更確認の自動化テーブル 状態判定に関する Starting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更確認の自動化テーブル 状態判定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の自動化テーブル 状態判定の証跡として保存して根拠にする。
    - C. Starting 機能の変更点を出力本文から切り離して変更確認の自動化テーブル 状態判定の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更確認の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Starting 機能 は「Starting 機能の状態と出力メッセージを結び付ける変更確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Starting 機能の出力行と DSI633I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Starting 機能を IBM Z NetViewの確認記録に残し、対象名は変更確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


