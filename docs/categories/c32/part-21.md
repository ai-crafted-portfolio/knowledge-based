---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (21/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > トラブルシューティング

### Using NetView online message and command help for the NetView agent {#c32-i3025}
*分類: トラブルシューティング*  ・  難易度: 中級

Using NetView online message and command help for the NetView agentは、Tivoli NetView z/OS 自動化のトラブルシューティングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文検分のトラブルシューティングに関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文検分の根拠にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して構文検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using commands {#c32-i3026}
*分類: トラブルシューティング*  ・  難易度: 中級

Using commandsは、Tivoli NetView z/OS 自動化のトラブルシューティングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using online help {#c32-i3027}
*分類: トラブルシューティング*  ・  難易度: 中級

Using online helpは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開検分のトラブルシューティングで Using online helpの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using online helpの出力を取らず展開検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開検分の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Using online help は「展開検分のトラブルシューティングに関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Using online helpの属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Using online helpを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the CNMTRACE function for NetView host components of the NetView agent function {#c32-i3028}
*分類: トラブルシューティング*  ・  難易度: 上級

Using the CNMTRACE function for NetView host components of the NetView agent functionは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using the DISPPI command to troubleshoot a PPI connection between NetView and the NetView agent {#c32-i3029}
*分類: トラブルシューティング*  ・  難易度: 中級

Using the DISPPI command to troubleshoot a PPI connection between NetView and the NetView agentは、Tivoli NetView z/OS 自動化のトラブルシューティングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using the NACTL command to troubleshoot the NetView agent {#c32-i3030}
*分類: トラブルシューティング*  ・  難易度: 中級

Using the NACTL command to troubleshoot the NetView agentは、Tivoli NetView z/OS 自動化のトラブルシューティングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端検分のトラブルシューティングに関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端検分の確認にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して終端検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the TestMode statement {#c32-i3031}
*分類: トラブルシューティング*  ・  難易度: 中級

Using the TestMode statementは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検分のトラブルシューティングで Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、探索検分の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して探索検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Using 機能 は「探索検分のトラブルシューティングに関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### View problems {#c32-i3032}
*分類: トラブルシューティング*  ・  難易度: 中級

'View problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 上書検分のトラブルシューティングでネットビューの運用確認を行います。View problemsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分のトラブルシューティングを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書検分で再確認できる形にする。 ✅
    - D. View problemsの属性行を読まず上書検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では View problems は「IBM Z NetViewで View problemsの扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では View problemsの表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では View problemsの使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### WAIT timeout and storage limits {#c32-i3033}
*分類: トラブルシューティング*  ・  難易度: 中級

WAIT timeout and storage limitsは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力検分のトラブルシューティングに関する WAIT 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. WAIT 機能の変更点を出力本文から切り離して出力検分のトラブルシューティングの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力検分の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では WAIT 機能 は「WAIT 機能の状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では WAIT 機能の出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では WAIT 機能を IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Working with IBM Software Support {#c32-i3034}
*分類: トラブルシューティング*  ・  難易度: 中級

Working with IBM Software Supportは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件検分のトラブルシューティングに関係する Working 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件検分の根拠を固定する。 ✅
    - B. Working 機能の名称と担当者名のみを残して条件検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Working 機能 は「Working 機能の用途をネットビューの表示で確認する条件検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの Working 機能と DSI633I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Working 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Workspace issues {#c32-i3035}
*分類: トラブルシューティング*  ・  難易度: 中級

'Workspace issues' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Programming_Assembler.pdf p.277

??? question "確認問題（1問）"
    **問題.** 区切検分のトラブルシューティングで Workspace issuesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Workspace issuesの出力を取らず区切検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を区切検分で確認する。 ✅
    - C. BROWSE CANZLOG を省略して区切検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Workspace issues は「区切検分のトラブルシューティングに関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Workspace issuesの属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Workspace issuesを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Programming_Assembler.pdf p.277



### Workspace names displayed in navigation tree are unreadable {#c32-i3036}
*分類: トラブルシューティング*  ・  難易度: 中級

Workspace names displayed in navigation tree are unreadableは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲検分のトラブルシューティングでネットビューの運用確認を行います。Workspace 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、範囲検分の証跡として残す。 ✅
    - D. Workspace 機能の属性行を読まず範囲検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Workspace 機能 は「IBM Z NetViewで Workspace 機能の扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Workspace 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Workspace 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Z NetView subnode unexpectedly goes offline {#c32-i3037}
*分類: トラブルシューティング*  ・  難易度: 中級

'Z NetView subnode unexpectedly goes offline' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 優先検分のトラブルシューティングに関する Z 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Z 機能の変更点を出力本文から切り離して優先検分のトラブルシューティングの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先検分の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Z 機能 は「Z 機能の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Z 機能の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Z 機能を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### zERT notification problem worksheet {#c32-i3038}
*分類: トラブルシューティング*  ・  難易度: 中級

'zERT notification problem worksheet' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 記録検分のトラブルシューティングに関係するzERT 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録検分の根拠にする。 ✅
    - B. zERT 機能の名称と担当者名のみを残して記録検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠ではzERT 機能 は「zERT 機能の用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewのzERT 機能と DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語ではzERT 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47




## Tivoli NetView z/OS 自動化 > トラブルシューティング > AUTOTEST STATUS

### AUTOTEST STATUS {#c32-i3039}
*分類: トラブルシューティング > AUTOTEST STATUS*  ・  難易度: 上級

AUTOTEST STATUSは、テスト中の活性メンバーや起動した操作者、最後に活性化した時刻を確認するコマンドです。テスト継続の可否を判断します

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲整理のネットビューでネットビューの運用確認を行います。AUTOTEST STATUS の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理のネットビューを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理のネットビューを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲整理の確認記録にまとめる。 ✅
    - D. AUTOTEST STATUS の属性行を読まず範囲整理のネットビューの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では AUTOTEST STATUS は「IBM Z NetViewで AUTOTEST STATUS の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では AUTOTEST STATUS の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では AUTOTEST STATUS の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > パフォーマンス・チューニング

### AUTOCNT Command {#c32-i3040}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'AUTOCNT Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 復旧検分のパフォーマンス・チューニングで AUTOCNT Commandの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AUTOCNT Commandの出力を取らず復旧検分のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧検分の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では AUTOCNT Command は「復旧検分のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では AUTOCNT Commandの属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では AUTOCNT Commandを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### AVAIL Option {#c32-i3041}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'AVAIL Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 呼出確認のパフォーマンス・チューニングでネットビューの運用確認を行います。AVAIL Optionの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出確認のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出確認として引き継ぐ。 ✅
    - D. AVAIL Optionの属性行を読まず呼出確認のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では AVAIL Option は「IBM Z NetViewで AVAIL Optionの扱いを記録する呼出確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では AVAIL Optionの表示結果と DSI633I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では AVAIL Optionの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### Achieving Performance Goals {#c32-i3042}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Achieving Performance Goals' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.10

??? question "確認問題（1問）"
    **問題.** 比較検分のパフォーマンス・チューニングで Achieving 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Achieving 機能の出力を取らず比較検分のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較検分の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較検分のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Achieving 機能 は「比較検分のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Achieving 機能の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Achieving 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.10



### Additional Tuning Considerations {#c32-i3043}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Additional Tuning Considerations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 順序検分のパフォーマンス・チューニングでネットビューの運用確認を行います。Additional 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検分のパフォーマンス・チューニングを正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序検分の採否を説明欄に結び付ける。 ✅
    - D. Additional 機能の属性行を読まず順序検分のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Additional 機能 は「IBM Z NetViewで Additional 機能の扱いを記録する順序検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Additional 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Additional 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Address Space Dispatch Priority {#c32-i3044}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Address Space Dispatch Priority' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Automation_Guide.pdf p.371

??? question "確認問題（1問）"
    **問題.** 値域検分のパフォーマンス・チューニングに関する Address 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Address 機能の変更点を出力本文から切り離して値域検分のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域検分として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Address 機能 は「Address 機能の状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Address 機能の出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Address 機能を IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Automation_Guide.pdf p.371



### Alerts-Dynamic Panel {#c32-i3045}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Alerts-Dynamic Panel' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView.pdf p.127


### Automated Operations Network (AON) Performance Considerations {#c32-i3046}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Automated Operations Network (AON) Performance Considerations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.201

??? question "確認問題（1問）"
    **問題.** 監査検分のパフォーマンス・チューニングでネットビューの運用確認を行います。Automated 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分のパフォーマンス・チューニングを確認した扱いにする。
    - B. EZL000I の有無を確認せず監査検分のパフォーマンス・チューニングを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査検分で再確認できる形にする。 ✅
    - D. Automated 機能の属性行を読まず監査検分のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Automated 機能 は「IBM Z NetViewで Automated 機能の扱いを記録する監査検分項目」と AONSTAT または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Automated 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Automated 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.201



### Automating Hardware Monitor Records {#c32-i3047}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Automating Hardware Monitor Records' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220

??? question "確認問題（1問）"
    **問題.** 変更検分のパフォーマンス・チューニングに関する Automating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検分のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Automating 機能の変更点を出力本文から切り離して変更検分のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更検分の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Automating 機能 は「Automating 機能の状態と出力メッセージを結び付ける変更検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Automating 機能の出力行と DSI633I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Automating 機能を IBM Z NetViewの確認記録に残し、対象名は変更検分対象です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220



### Automation Table {#c32-i3048}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Automation Table' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.89


### Automation Tasks (Autotasks) {#c32-i3049}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Automation Tasks (Autotasks)' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.45

??? question "確認問題（1問）"
    **問題.** 展開確認のパフォーマンス・チューニングで Automation 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Automation 機能の出力を取らず展開確認のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、展開確認の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して展開確認のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Automation 機能 は「展開確認のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Automation 機能の属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Automation 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.45



### Browse {#c32-i3050}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Browse' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Customization_Guide.pdf p.76

??? question "確認問題（1問）"
    **問題.** 置換確認のパフォーマンス・チューニングに関する Browseの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Browseの変更点を出力本文から切り離して置換確認のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換確認の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Browse は「Browseの状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Browseの出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Browseを IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Customization_Guide.pdf p.76



### Buffer Pool Sizes {#c32-i3051}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Buffer Pool Sizes' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 終端確認のパフォーマンス・チューニングに関係する Buffer Pool Sizesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端確認の点検結果を残す。 ✅
    - B. Buffer Pool Sizesの名称と担当者名のみを残して終端確認のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端確認のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端確認のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Buffer Pool Sizes は「Buffer Pool Sizesの用途をネットビューの表示で確認する終端確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Z NetViewの Buffer Pool Sizesと DSI633I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Buffer Pool Sizesを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### CNMCMD Resident Option {#c32-i3052}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'CNMCMD Resident Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 優先確認のパフォーマンス・チューニングに関する CNMCMD 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先確認のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. CNMCMD 機能の変更点を出力本文から切り離して優先確認のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では CNMCMD 機能 は「CNMCMD 機能の状態と出力メッセージを結び付ける優先確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では CNMCMD 機能の出力行と DSI633I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では CNMCMD 機能を IBM Z NetViewの確認記録に残し、対象名は優先確認対象です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### Calculating Task Utilizations with Two Observations of TASKUTIL {#c32-i3053}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Calculating Task Utilizations with Two Observations of TASKUTILは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索確認のパフォーマンス・チューニングで Calculating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Calculating 機能の出力を取らず探索確認のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索確認で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索確認のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Calculating 機能 は「探索確認のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Calculating 機能の属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Calculating 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Canzlog Archive Storage Requirements {#c32-i3054}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Canzlog Archive Storage Requirements' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.70

??? question "確認問題（1問）"
    **問題.** 上書確認のパフォーマンス・チューニングでネットビューの運用確認を行います。Canzlog 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書確認の確認値として扱う。 ✅
    - D. Canzlog 機能の属性行を読まず上書確認のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Canzlog 機能 は「IBM Z NetViewで Canzlog 機能の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Canzlog 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Canzlog 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.70



### Canzlog Archiving {#c32-i3055}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Canzlog Archiving' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.70

??? question "確認問題（1問）"
    **問題.** 出力確認のパフォーマンス・チューニングに関する Canzlog Archivingの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力確認のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Canzlog Archivingの変更点を出力本文から切り離して出力確認のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力確認の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では Canzlog Archiving は「Canzlog Archivingの状態と出力メッセージを結び付ける出力確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では Canzlog Archivingの出力行と DSI633I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では Canzlog Archivingを IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.70



### Canzlog Data Access {#c32-i3056}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Canzlog Data Access' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView.pdf p.38

??? question "確認問題（1問）"
    **問題.** 条件確認のパフォーマンス・チューニングに関係する Canzlog 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を条件確認で確認する。 ✅
    - B. Canzlog 機能の名称と担当者名のみを残して条件確認のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件確認のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件確認のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では Canzlog 機能 は「Canzlog 機能の用途をネットビューの表示で確認する条件確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Z NetViewの Canzlog 機能と DSI633I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では Canzlog 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** NetView_6.4_Users_Guide_NetView.pdf p.38



### Canzlog Data Set Characteristics {#c32-i3057}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Canzlog Data Set Characteristics' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.70

??? question "確認問題（1問）"
    **問題.** 区切確認のパフォーマンス・チューニングで Canzlog 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Canzlog 機能の出力を取らず区切確認のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、区切確認の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して区切確認のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Canzlog 機能 は「区切確認のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Canzlog 機能の属性行と DSI633I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Canzlog 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切確認初出です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.70



### Client Performance {#c32-i3058}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Client Performance' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 範囲確認のパフォーマンス・チューニングでネットビューの運用確認を行います。Client Performanceの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲確認のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲確認の確認記録にまとめる。 ✅
    - D. Client Performanceの属性行を読まず範囲確認のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Client Performance は「IBM Z NetViewで Client Performanceの扱いを記録する範囲確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Client Performanceの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Client Performanceの使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Coding RES=N on Command Definition Statements {#c32-i3059}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Coding RES=N on Command Definition Statementsは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録確認のパフォーマンス・チューニングに関係する Coding 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録確認の結果として保存する。 ✅
    - B. Coding 属性の名称と担当者名のみを残して記録確認のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録確認のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Coding 属性 は「Coding 属性の用途をネットビューの表示で確認する記録確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewの Coding 属性と DSI633I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Coding 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Command Lists {#c32-i3060}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Command Lists' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19


### Command Processors {#c32-i3061}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Command Processors' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 値域確認のパフォーマンス・チューニングに関する Command Processorsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Command Processorsの変更点を出力本文から切り離して値域確認のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域確認の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Command Processors は「Command Processorsの状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Command Processorsの出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Command Processorsを IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Command Processors Written in a High-Level Language {#c32-i3062}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Command Processors Written in a High-Level Languageは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のパフォーマンス・チューニングに関係する Command 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告確認の点検結果を残す。 ✅
    - B. Command 機能の名称と担当者名のみを残して警告確認のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Command 機能 は「Command 機能の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの Command 機能と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Command 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Command Security {#c32-i3063}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Command Security' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.248

??? question "確認問題（1問）"
    **問題.** 復旧確認のパフォーマンス・チューニングで Command Securityの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Command Securityの出力を取らず復旧確認のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧確認で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Command Security は「復旧確認のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Command Securityの属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Command Securityを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.248



### Command Statistics {#c32-i3064}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Command Statistics' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 監査確認のパフォーマンス・チューニングでネットビューの運用確認を行います。Command Statisticsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査確認の確認値として扱う。 ✅
    - D. Command Statisticsの属性行を読まず監査確認のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Command Statistics は「IBM Z NetViewで Command Statisticsの扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Command Statisticsの表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Command Statisticsの使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Command and Message Forwarding {#c32-i3065}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Command and Message Forwarding' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol2_DUI-IHS.pdf p.157

??? question "確認問題（1問）"
    **問題.** 比較確認のパフォーマンス・チューニングで Command 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Command 機能の出力を取らず比較確認のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、比較確認の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して比較確認のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Command 機能 は「比較確認のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Command 機能の属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Command 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol2_DUI-IHS.pdf p.157



### Compiled REXX/370 Command Lists {#c32-i3066}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Compiled REXX/370 Command Lists' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Programming_REXX_and_NetView_Command_List_Language.pdf p.181

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として REXX/370 を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。構文照合保守で扱う REXX/370 は Tivoli NetView z/OS 自動化 の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として REXX/370 を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** NetView_6.4_Programming_REXX_and_NetView_Command_List_Language.pdf p.181



### Customization Parameters {#c32-i3067}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Customization Parameters' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol2_DUI-IHS.pdf p.330

??? question "確認問題（1問）"
    **問題.** 構文照合のパフォーマンス・チューニングに関係する Customization 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を構文照合で確認する。 ✅
    - B. Customization 機能の名称と担当者名のみを残して構文照合のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Customization 機能 は「Customization 機能の用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの Customization 機能と DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Customization 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol2_DUI-IHS.pdf p.330



### DASD Filtering {#c32-i3068}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'DASD Filtering' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開照合のパフォーマンス・チューニングで DASD Filteringの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DASD Filteringの出力を取らず展開照合のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、展開照合の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して展開照合のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では DASD Filtering は「展開照合のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では DASD Filteringの属性行と DSI633I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では DASD Filteringを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開照合初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### DASD Option {#c32-i3069}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'DASD Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 呼出照合のパフォーマンス・チューニングでネットビューの運用確認を行います。DASD Optionの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出照合のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出照合の確認記録にまとめる。 ✅
    - D. DASD Optionの属性行を読まず呼出照合のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では DASD Option は「IBM Z NetViewで DASD Optionの扱いを記録する呼出照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では DASD Optionの表示結果と DSI633I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では DASD Optionの使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### DDF Tree and Panel {#c32-i3070}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'DDF Tree and Panel' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Data_Model_Reference.pdf p.79

??? question "確認問題（1問）"
    **問題.** 終端照合のパフォーマンス・チューニングに関係する DDF Tree and Panelの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端照合の結果として保存する。 ✅
    - B. DDF Tree and Panelの名称と担当者名のみを残して終端照合のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端照合のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端照合のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では DDF Tree and Panel は「DDF Tree and Panelの用途をネットビューの表示で確認する終端照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM Z NetViewの DDF Tree and Panelと DSI633I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では DDF Tree and Panelを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.79



### DGROUP Option {#c32-i3071}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'DGROUP Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 上書照合のパフォーマンス・チューニングでネットビューの運用確認を行います。DGROUP Optionの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書照合のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書照合のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書照合として引き継ぐ。 ✅
    - D. DGROUP Optionの属性行を読まず上書照合のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では DGROUP Option は「IBM Z NetViewで DGROUP Optionの扱いを記録する上書照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では DGROUP Optionの表示結果と DSI633I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では DGROUP Optionの使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### DSICLD Library {#c32-i3072}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'DSICLD Library' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.270

??? question "確認問題（1問）"
    **問題.** 出力照合のパフォーマンス・チューニングに関する DSICLD Libraryの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力照合のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. DSICLD Libraryの変更点を出力本文から切り離して出力照合のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力照合の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では DSICLD Library は「DSICLD Libraryの状態と出力メッセージを結び付ける出力照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では DSICLD Libraryの出力行と DSI633I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では DSICLD Libraryを IBM Z NetViewの確認記録に残し、対象名は出力照合対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.270



### DUIGINIT Parameters {#c32-i3073}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'DUIGINIT Parameters' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.549

??? question "確認問題（1問）"
    **問題.** 条件照合のパフォーマンス・チューニングに関係する DUIGINIT 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件照合の点検結果を残す。 ✅
    - B. DUIGINIT 機能の名称と担当者名のみを残して条件照合のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件照合のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件照合のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では DUIGINIT 機能 は「DUIGINIT 機能の用途をネットビューの表示で確認する条件照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では IBM Z NetViewの DUIGINIT 機能と DSI633I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では DUIGINIT 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.549



### Data Services Request Blocks (DSRBs) {#c32-i3074}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Data Services Request Blocks (DSRBs)' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.365

??? question "確認問題（1問）"
    **問題.** 置換照合のパフォーマンス・チューニングに関する Data 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換照合のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Data 機能の変更点を出力本文から切り離して置換照合のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換照合の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では Data 機能 は「Data 機能の状態と出力メッセージを結び付ける置換照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では Data 機能の出力行と DSI633I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では Data 機能を IBM Z NetViewの確認記録に残し、対象名は置換照合対象です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.365



### Definitions for LSR and DFR {#c32-i3075}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Definitions for LSR and DFRは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索照合のパフォーマンス・チューニングで Definitions 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Definitions 機能の出力を取らず探索照合のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、探索照合の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して探索照合のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では Definitions 機能 は「探索照合のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では Definitions 機能の属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では Definitions 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enhancing Performance {#c32-i3076}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Enhancing Performance' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 区切照合のパフォーマンス・チューニングで Enhancing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Enhancing 機能の出力を取らず区切照合のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切照合で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して区切照合のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では Enhancing 機能 は「区切照合のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では Enhancing 機能の属性行と DSI633I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では Enhancing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切照合初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Error-to-Traffic (E/T) Ratio Thresholds {#c32-i3077}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Error-to-Traffic (E/T) Ratio Thresholds' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.325

??? question "確認問題（1問）"
    **問題.** 範囲照合のError-to-Traffic (E/T) Ratio Thresholdsでネットビューの運用確認を行います。Error-to-Traffic 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲照合のError-to-Traffic (E/T) Ratio Thresholdsを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲照合のError-to-Traffic (E/T) Ratio Thresholdsを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲照合の確認値として扱う。 ✅
    - D. Error-to-Traffic 属性の属性行を読まず範囲照合のError-to-Traffic (E/T) Ratio Thresholdsの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では Error-to-Traffic 属性 は「IBM Z NetViewで Error-to-Traffic 属性の扱いを記録する範囲照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では Error-to-Traffic 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では Error-to-Traffic 属性の使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.325



### Estimating Storage Usage {#c32-i3078}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Estimating Storage Usage' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 優先照合のパフォーマンス・チューニングに関する Estimating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先照合のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Estimating 機能の変更点を出力本文から切り離して優先照合のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先照合の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では Estimating 機能 は「Estimating 機能の状態と出力メッセージを結び付ける優先照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では Estimating 機能の出力行と DSI633I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では Estimating 機能を IBM Z NetViewの確認記録に残し、対象名は優先照合対象です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Event/Automation Service {#c32-i3079}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Event/Automation Service' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.27


### Filtering Hardware Monitor Records {#c32-i3080}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Filtering Hardware Monitor Records' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220

??? question "確認問題（1問）"
    **問題.** 比較照合のパフォーマンス・チューニングで Filtering 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Filtering 機能の出力を取らず比較照合のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較照合の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較照合のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では Filtering 機能 は「比較照合のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では Filtering 機能の属性行と DSI633I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では Filtering 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較照合初出です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220



### Global Tracing {#c32-i3081}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Global Tracing' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Automation_Guide.pdf p.240

??? question "確認問題（1問）"
    **問題.** 順序照合のパフォーマンス・チューニングでネットビューの運用確認を行います。Global Tracingの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序照合のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序照合のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序照合の確認記録にまとめる。 ✅
    - D. Global Tracingの属性行を読まず順序照合のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では Global Tracing は「IBM Z NetViewで Global Tracingの扱いを記録する順序照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では Global Tracingの表示結果と DSI633I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では Global Tracingの使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** NetView_6.4_Automation_Guide.pdf p.240



### Global Variables {#c32-i3082}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Global Variables' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.49

??? question "確認問題（1問）"
    **問題.** 値域照合のパフォーマンス・チューニングに関する Global Variablesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域照合のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Global Variablesの変更点を出力本文から切り離して値域照合のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域照合の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では Global Variables は「Global Variablesの状態と出力メッセージを結び付ける値域照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では Global Variablesの出力行と DSI633I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では Global Variablesを IBM Z NetViewの確認記録に残し、対象名は値域照合対象です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.49



### HMSTATS Command {#c32-i3083}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'HMSTATS Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 監査照合のパフォーマンス・チューニングでネットビューの運用確認を行います。HMSTATS Commandの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査照合のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査照合のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査照合として引き継ぐ。 ✅
    - D. HMSTATS Commandの属性行を読まず監査照合のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では HMSTATS Command は「IBM Z NetViewで HMSTATS Commandの扱いを記録する監査照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では HMSTATS Commandの表示結果と DSI633I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では HMSTATS Commandの使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Hardware Monitor Filters {#c32-i3084}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Hardware Monitor Filters' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220

??? question "確認問題（1問）"
    **問題.** 警告照合のパフォーマンス・チューニングに関係する Hardware 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告照合の結果として保存する。 ✅
    - B. Hardware 機能の名称と担当者名のみを残して警告照合のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告照合のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告照合のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では Hardware 機能 は「Hardware 機能の用途をネットビューの表示で確認する警告照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では IBM Z NetViewの Hardware 機能と DSI633I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では Hardware 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220



### Hardware Requirements {#c32-i3085}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Hardware Requirements' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220

??? question "確認問題（1問）"
    **問題.** 復旧照合のパフォーマンス・チューニングで Hardware 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Hardware 機能の出力を取らず復旧照合のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧照合の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧照合のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では Hardware 機能 は「復旧照合のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では Hardware 機能の属性行と DSI633I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では Hardware 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.220



### Host Tuning Techniques {#c32-i3086}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Host Tuning Techniques' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 変更照合のパフォーマンス・チューニングに関する Host 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更照合のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Host 機能の変更点を出力本文から切り離して変更照合のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更照合の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では Host 機能 は「Host 機能の状態と出力メッセージを結び付ける変更照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では Host 機能の出力行と DSI633I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では Host 機能を IBM Z NetViewの確認記録に残し、対象名は変更照合対象です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### How to Compile REXX Procedures {#c32-i3087}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

How to Compile REXX Proceduresは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文追跡のパフォーマンス・チューニングに関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文追跡の点検結果を残す。 ✅
    - B. How 機能の名称と担当者名のみを残して構文追跡のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文追跡のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI039I の有無を見ず構文追跡のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では How 機能 は「How 機能の用途をネットビューの表示で確認する構文追跡項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では IBM Z NetViewの How 機能と DSI039I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では How 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### IBM Z NetView Enterprise Management Agent {#c32-i3088}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'IBM Z NetView Enterprise Management Agent' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47


### Improving NetView Performance {#c32-i3089}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Improving NetView Performance' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 呼出追跡のパフォーマンス・チューニングでネットビューの運用確認を行います。Improving 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出追跡のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出追跡のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出追跡の確認値として扱う。 ✅
    - D. Improving 機能の属性行を読まず呼出追跡のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では Improving 機能 は「IBM Z NetViewで Improving 機能の扱いを記録する呼出追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では Improving 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では Improving 機能の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Initialization Specifications {#c32-i3090}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Initialization Specifications' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.137

??? question "確認問題（1問）"
    **問題.** 置換追跡のパフォーマンス・チューニングに関する Initialization 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換追跡のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Initialization 機能の変更点を出力本文から切り離して置換追跡のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換追跡の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では Initialization 機能 は「Initialization 機能の状態と出力メッセージを結び付ける置換追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では Initialization 機能の出力行と DSI633I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では Initialization 機能を IBM Z NetViewの確認記録に残し、対象名は置換追跡対象です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.137



### Installation Exits {#c32-i3091}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Installation Exits' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Programming_Assembler.pdf p.71


### KEEPPIU Option {#c32-i3092}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'KEEPPIU Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 出力追跡のパフォーマンス・チューニングに関する KEEPPIU Optionの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力追跡のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. KEEPPIU Optionの変更点を出力本文から切り離して出力追跡のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力追跡の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では KEEPPIU Option は「KEEPPIU Optionの状態と出力メッセージを結び付ける出力追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では KEEPPIU Optionの出力行と DSI633I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では KEEPPIU Optionを IBM Z NetViewの確認記録に残し、対象名は出力追跡対象です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### KEEPPIU Parameter {#c32-i3093}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'KEEPPIU Parameter' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.73

??? question "確認問題（1問）"
    **問題.** 条件追跡のパフォーマンス・チューニングに関係する KEEPPIU Parameterの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件追跡の結果として保存する。 ✅
    - B. KEEPPIU Parameterの名称と担当者名のみを残して条件追跡のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件追跡のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件追跡のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では KEEPPIU Parameter は「KEEPPIU Parameterの用途をネットビューの表示で確認する条件追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では IBM Z NetViewの KEEPPIU Parameterと DSI633I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では KEEPPIU Parameterを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.73



### KEEPSESS Option {#c32-i3094}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'KEEPSESS Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 区切追跡のパフォーマンス・チューニングで KEEPSESS Optionの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. KEEPSESS Optionの出力を取らず区切追跡のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切追跡の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切追跡のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では KEEPSESS Option は「区切追跡のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では KEEPSESS Optionの属性行と DSI633I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では KEEPSESS Optionを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### Keep Classes {#c32-i3095}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Keep Classes' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196

??? question "確認問題（1問）"
    **問題.** 探索追跡のパフォーマンス・チューニングで Keep Classesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Keep Classesの出力を取らず探索追跡のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索追跡の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索追跡のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では Keep Classes は「探索追跡のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では Keep Classesの属性行と DSI633I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では Keep Classesを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196



### Keeping Track of Virtual Storage and Other System Resource Usage {#c32-i3096}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Keeping Track of Virtual Storage and Other System Resource Usageは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書追跡のパフォーマンス・チューニングでネットビューの運用確認を行います。Keeping 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書追跡のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書追跡のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書追跡の確認記録にまとめる。 ✅
    - D. Keeping 機能の属性行を読まず上書追跡のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では Keeping 機能 は「IBM Z NetViewで Keeping 機能の扱いを記録する上書追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では Keeping 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では Keeping 機能の使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Keywords for Resource Limits {#c32-i3097}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Keywords for Resource Limits' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 範囲追跡のパフォーマンス・チューニングでネットビューの運用確認を行います。Keywords 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲追跡のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲追跡のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲追跡として引き継ぐ。 ✅
    - D. Keywords 機能の属性行を読まず範囲追跡のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では Keywords 機能 は「IBM Z NetViewで Keywords 機能の扱いを記録する範囲追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では Keywords 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では Keywords 機能の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### LISTCAT Command {#c32-i3098}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'LISTCAT Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 記録追跡のパフォーマンス・チューニングに関係する LISTCAT Commandの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、記録追跡の点検結果を残す。 ✅
    - B. LISTCAT Commandの名称と担当者名のみを残して記録追跡のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録追跡のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録追跡のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では LISTCAT Command は「LISTCAT Commandの用途をネットビューの表示で確認する記録追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では IBM Z NetViewの LISTCAT Commandと DSI633I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では LISTCAT Commandを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### LOGTSTAT Command {#c32-i3099}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'LOGTSTAT Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 順序追跡のパフォーマンス・チューニングでネットビューの運用確認を行います。LOGTSTAT Commandの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序追跡の確認値として扱う。 ✅
    - D. LOGTSTAT Commandの属性行を読まず順序追跡のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では LOGTSTAT Command は「IBM Z NetViewで LOGTSTAT Commandの扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では LOGTSTAT Commandの表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では LOGTSTAT Commandの使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### LU 6.2 Transport {#c32-i3100}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'LU 6.2 Transport' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Application_Programmers_Guide.pdf p.77

??? question "確認問題（1問）"
    **問題.** 値域追跡のパフォーマンス・チューニングに関する LU 6.2 Transportの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域追跡のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. LU 6.2 Transportの変更点を出力本文から切り離して値域追跡のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域追跡の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では LU 6.2 Transport は「LU 6.2 Transportの状態と出力メッセージを結び付ける値域追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では LU 6.2 Transportの出力行と DSI633I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では LU 6.2 Transportを IBM Z NetViewの確認記録に残し、対象名は値域追跡対象です。

    **出典:** NetView_6.4_Application_Programmers_Guide.pdf p.77



### LUCOUNT Parameter {#c32-i3101}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'LUCOUNT Parameter' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.73

??? question "確認問題（1問）"
    **問題.** 警告追跡のパフォーマンス・チューニングに関係する LUCOUNT Parameterの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を警告追跡で確認する。 ✅
    - B. LUCOUNT Parameterの名称と担当者名のみを残して警告追跡のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告追跡のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告追跡のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では LUCOUNT Parameter は「LUCOUNT Parameterの用途をネットビューの表示で確認する警告追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では IBM Z NetViewの LUCOUNT Parameterと DSI633I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では LUCOUNT Parameterを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.73



### Limiting System Messages {#c32-i3102}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Limiting System Messages' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.617

??? question "確認問題（1問）"
    **問題.** 優先追跡のパフォーマンス・チューニングに関する Limiting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先追跡のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Limiting 機能の変更点を出力本文から切り離して優先追跡のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先追跡の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では Limiting 機能 は「Limiting 機能の状態と出力メッセージを結び付ける優先追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では Limiting 機能の出力行と DSI633I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では Limiting 機能を IBM Z NetViewの確認記録に残し、対象名は優先追跡対象です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.617



### Local Shared Resources (LSR) and Deferred Write (DFR) {#c32-i3103}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Local Shared Resources (LSR) and Deferred Write (DFR)は、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較追跡のパフォーマンス・チューニングで Local 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Local 機能の出力を取らず比較追跡のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較追跡で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して比較追跡のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では Local 機能 は「比較追跡のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では Local 機能の属性行と DSI633I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では Local 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### MAXSESS Keyword {#c32-i3104}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'MAXSESS Keyword' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.29

??? question "確認問題（1問）"
    **問題.** 展開検査のパフォーマンス・チューニングで MAXSESS Keywordの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MAXSESS Keywordの出力を取らず展開検査のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、展開検査の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して展開検査のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では MAXSESS Keyword は「展開検査のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では MAXSESS Keywordの属性行と DSI633I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では MAXSESS Keywordを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検査初出です。

    **出典:** NetView_6.4_Installation_Migration_Guide.pdf p.29



### Major Tuning Techniques for the Session Monitor {#c32-i3105}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Major Tuning Techniques for the Session Monitorは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧追跡のパフォーマンス・チューニングで Major 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Major 機能の出力を取らず復旧追跡のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、復旧追跡の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧追跡のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では Major 機能 は「復旧追跡のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では Major 機能の属性行と DSI633I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では Major 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Command Lists with AUTODROP {#c32-i3106}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Managing Command Lists with AUTODROPは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査追跡のパフォーマンス・チューニングでネットビューの運用確認を行います。Managing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査追跡のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI039I の有無を確認せず監査追跡のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査追跡の確認記録にまとめる。 ✅
    - D. Managing 機能の属性行を読まず監査追跡のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では Managing 機能 は「IBM Z NetViewで Managing 機能の扱いを記録する監査追跡項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では Managing 機能の表示結果と DSI039I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では Managing 機能の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Database Size {#c32-i3107}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Managing Database Sizeは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更追跡のパフォーマンス・チューニングに関する Managing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更追跡のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Managing 機能の変更点を出力本文から切り離して変更追跡のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更追跡の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では Managing 機能 は「Managing 機能の状態と出力メッセージを結び付ける変更追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では Managing 機能の出力行と DSI633I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では Managing 機能を IBM Z NetViewの確認記録に残し、対象名は変更追跡対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing the Session Monitor Database {#c32-i3108}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Managing the Session Monitor Databaseは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文検査のパフォーマンス・チューニングに関係する Managing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、構文検査の結果として保存する。 ✅
    - B. Managing 機能の名称と担当者名のみを残して構文検査のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検査のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検査のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では Managing 機能 は「Managing 機能の用途をネットビューの表示で確認する構文検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では IBM Z NetViewの Managing 機能と DSI633I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では Managing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Minimizing Storage Usage {#c32-i3109}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Minimizing Storage Usage' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 呼出検査のパフォーマンス・チューニングでネットビューの運用確認を行います。Minimizing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検査のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検査のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出検査として引き継ぐ。 ✅
    - D. Minimizing 機能の属性行を読まず呼出検査のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では Minimizing 機能 は「IBM Z NetViewで Minimizing 機能の扱いを記録する呼出検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では Minimizing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では Minimizing 機能の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Monitoring VSAM Performance {#c32-i3110}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Monitoring VSAM Performanceは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換検査のパフォーマンス・チューニングに関する Monitoring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検査のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Monitoring 機能の変更点を出力本文から切り離して置換検査のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換検査の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では Monitoring 機能 は「Monitoring 機能の状態と出力メッセージを結び付ける置換検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では Monitoring 機能の出力行と DSI633I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では Monitoring 機能を IBM Z NetViewの確認記録に残し、対象名は置換検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Multiple NetView Programs {#c32-i3111}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Multiple NetView Programs' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.32

??? question "確認問題（1問）"
    **問題.** 終端検査のパフォーマンス・チューニングに関係する Multiple 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端検査の点検結果を残す。 ✅
    - B. Multiple 機能の名称と担当者名のみを残して終端検査のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Multiple 機能 は「Multiple 機能の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの Multiple 機能と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Multiple 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.32



### NCCF TRACE Options {#c32-i3112}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'NCCF TRACE Options' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.262

??? question "確認問題（1問）"
    **問題.** 探索検査のパフォーマンス・チューニングで NCCF TRACE Optionsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NCCF TRACE Optionsの出力を取らず探索検査のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索検査で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索検査のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では NCCF TRACE Options は「探索検査のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では NCCF TRACE Optionsの属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では NCCF TRACE Optionsを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.262



### NETCONV {#c32-i3113}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'NETCONV' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.355

??? question "確認問題（1問）"
    **問題.** 上書検査のパフォーマンス・チューニングでネットビューの運用確認を行います。NETCONV の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検査のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書検査の確認値として扱う。 ✅
    - D. NETCONV の属性行を読まず上書検査のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では NETCONV は「IBM Z NetViewで NETCONV の扱いを記録する上書検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では NETCONV の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では NETCONV の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.355



### NPDA.RATE Statement Initialization Specifications {#c32-i3114}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'NPDA.RATE Statement Initialization Specifications' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.31

??? question "確認問題（1問）"
    **問題.** 警告検査のパフォーマンス・チューニングに関係する NPDA 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告検査の点検結果を残す。 ✅
    - B. NPDA 属性の名称と担当者名のみを残して警告検査のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず警告検査のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では NPDA 属性 は「NPDA 属性の用途をネットビューの表示で確認する警告検査項目」と NPDA または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの NPDA 属性と BNH160I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では NPDA 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.31



### NetView Access from the Web Browser {#c32-i3115}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

NetView Access from the Web Browserは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力検査のパフォーマンス・チューニングに関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検査のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して出力検査のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける出力検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NetView Automation Table {#c32-i3116}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'NetView Automation Table' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Automation_Guide.pdf p.240

??? question "確認問題（1問）"
    **問題.** 条件検査のパフォーマンス・チューニングに関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を条件検査で確認する。 ✅
    - B. NetView 機能の名称と担当者名のみを残して条件検査のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検査のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する条件検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Automation_Guide.pdf p.240



### NetView Constants Module (DSICTMOD) {#c32-i3117}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'NetView Constants Module (DSICTMOD)' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 区切検査のパフォーマンス・チューニングで NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず区切検査のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、区切検査の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して区切検査のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では NetView 機能 は「区切検査のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Installation_Migration_Guide.pdf p.64



### NetView Program-to-Program Interface {#c32-i3118}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'NetView Program-to-Program Interface' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.88

??? question "確認問題（1問）"
    **問題.** 範囲検査のパフォーマンス・チューニングでネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検査のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲検査の確認記録にまとめる。 ✅
    - D. NetView 機能の属性行を読まず範囲検査のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する範囲検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では NetView 機能の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.88



### NetView Subsystem Address Space {#c32-i3119}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'NetView Subsystem Address Space' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Application_Programmers_Guide.pdf p.27

??? question "確認問題（1問）"
    **問題.** 優先検査のパフォーマンス・チューニングに関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して優先検査のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Application_Programmers_Guide.pdf p.27



### NetView-NetView Communication {#c32-i3120}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

NetView-NetView Communicationは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録検査のパフォーマンス・チューニングに関係する NetView-NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録検査の結果として保存する。 ✅
    - B. NetView-NetView 機能の名称と担当者名のみを残して記録検査のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では NetView-NetView 機能 は「NetView-NetView 機能の用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの NetView-NetView 機能と DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では NetView-NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Network Asset Management Facility {#c32-i3121}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Network Asset Management Facility' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 比較検査のパフォーマンス・チューニングで Network 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Network 機能の出力を取らず比較検査のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、比較検査の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して比較検査のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では Network 機能 は「比較検査のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では Network 機能の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では Network 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### Network Resource Naming Conventions {#c32-i3122}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Network Resource Naming Conventions' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 順序検査のパフォーマンス・チューニングでネットビューの運用確認を行います。Network 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序検査として引き継ぐ。 ✅
    - D. Network 機能の属性行を読まず順序検査のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Network 機能 は「IBM Z NetViewで Network 機能の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Network 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Network 機能の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Node Automation {#c32-i3123}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Node Automation' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.45

??? question "確認問題（1問）"
    **問題.** 値域検査のパフォーマンス・チューニングに関する Node Automationの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Node Automationの変更点を出力本文から切り離して値域検査のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域検査の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では Node Automation は「Node Automationの状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では Node Automationの出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では Node Automationを IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.45



### Operations {#c32-i3124}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Operations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.201

??? question "確認問題（1問）"
    **問題.** 復旧検査のパフォーマンス・チューニングで Operationsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Operationsの出力を取らず復旧検査のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧検査で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では Operations は「復旧検査のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では Operationsの属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では Operationsを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.201



### PIU Buffer Allocation and Tuning {#c32-i3125}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

PIU Buffer Allocation and Tuningは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文判定のパフォーマンス・チューニングに関係する PIU 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を構文判定で確認する。 ✅
    - B. PIU 機能の名称と担当者名のみを残して構文判定のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では PIU 機能 は「PIU 機能の用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの PIU 機能と DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では PIU 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Partitioned Data Set (PDS) Allocation {#c32-i3126}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Partitioned Data Set (PDS) Allocation' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.31

??? question "確認問題（1問）"
    **問題.** 監査検査のパフォーマンス・チューニングでネットビューの運用確認を行います。Partitioned 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査検査の確認値として扱う。 ✅
    - D. Partitioned 機能の属性行を読まず監査検査のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では Partitioned 機能 は「IBM Z NetViewで Partitioned 機能の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では Partitioned 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では Partitioned 機能の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.31



### Persistent and Nonpersistent LUC Sessions {#c32-i3127}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Persistent and Nonpersistent LUC Sessionsは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更検査のパフォーマンス・チューニングに関する Persistent 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Persistent 機能の変更点を出力本文から切り離して変更検査のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では Persistent 機能 は「Persistent 機能の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では Persistent 機能の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では Persistent 機能を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Preloading Command Lists {#c32-i3128}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Preloading Command Lists' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 展開判定のパフォーマンス・チューニングで Preloading 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Preloading 機能の出力を取らず展開判定のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. LIST CLIST の結果から対象行を抜き出し、展開判定の証跡として残す。 ✅
    - C. LIST CLIST を省略して展開判定のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では Preloading 機能 は「展開判定のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開判定項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では Preloading 機能の属性行と DSI039I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では Preloading 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Programming Recommendations {#c32-i3129}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Programming Recommendations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Customization_Guide.pdf p.97

??? question "確認問題（1問）"
    **問題.** 呼出判定のパフォーマンス・チューニングでネットビューの運用確認を行います。Programming 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出判定の確認記録にまとめる。 ✅
    - D. Programming 機能の属性行を読まず呼出判定のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では Programming 機能 は「IBM Z NetViewで Programming 機能の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では Programming 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では Programming 機能の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Customization_Guide.pdf p.97



### RATIO Statement Initialization Specifications {#c32-i3130}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'RATIO Statement Initialization Specifications' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.31

??? question "確認問題（1問）"
    **問題.** 置換判定のパフォーマンス・チューニングに関する RATIO 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. RATIO 機能の変更点を出力本文から切り離して置換判定のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換判定の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では RATIO 機能 は「RATIO 機能の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では RATIO 機能の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では RATIO 機能を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.31



### RESOURCE Command {#c32-i3131}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'RESOURCE Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 探索判定のパフォーマンス・チューニングで RESOURCE Commandの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RESOURCE Commandの出力を取らず探索判定のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、探索判定の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して探索判定のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では RESOURCE Command は「探索判定のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では RESOURCE Commandの属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では RESOURCE Commandを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### REXX Command Lists {#c32-i3132}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'REXX Command Lists' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Programming_REXX_and_NetView_Command_List_Language.pdf p.181

??? question "確認問題（1問）"
    **問題.** 出力判定のパフォーマンス・チューニングに関する REXX Command Listsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LIST CLIST の結果を残さず出力判定のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. REXX Command Listsの変更点を出力本文から切り離して出力判定のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力判定の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では REXX Command Lists は「REXX Command Listsの状態と出力メッセージを結び付ける出力判定項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では REXX Command Listsの出力行と DSI039I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では REXX Command Listsを IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Programming_REXX_and_NetView_Command_List_Language.pdf p.181



### REXX Function Packages {#c32-i3133}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'REXX Function Packages' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.579

??? question "確認問題（1問）"
    **問題.** 条件判定のパフォーマンス・チューニングに関係する REXX 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件判定の点検結果を残す。 ✅
    - B. REXX 機能の名称と担当者名のみを残して条件判定のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI039I の有無を見ず条件判定のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では REXX 機能 は「REXX 機能の用途をネットビューの表示で確認する条件判定項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの REXX 機能と DSI039I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では REXX 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.579



### RODM API Statistics {#c32-i3134}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'RODM API Statistics' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.270

??? question "確認問題（1問）"
    **問題.** 区切判定のパフォーマンス・チューニングで RODM 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RODM 機能の出力を取らず区切判定のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切判定で再確認できる形にする。 ✅
    - C. RODMVIEW を省略して区切判定のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では RODM 機能 は「区切判定のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では RODM 機能の属性行と EKG000I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では RODM 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.270



### RODM Cell Pool Statistics {#c32-i3135}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'RODM Cell Pool Statistics' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 範囲判定のパフォーマンス・チューニングでネットビューの運用確認を行います。RODM 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定のパフォーマンス・チューニングを確認した扱いにする。
    - B. EKG000I の有無を確認せず範囲判定のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲判定の確認値として扱う。 ✅
    - D. RODM 機能の属性行を読まず範囲判定のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では RODM 機能 は「IBM Z NetViewで RODM 機能の扱いを記録する範囲判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では RODM 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では RODM 機能の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### RODM Data Sets {#c32-i3136}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'RODM Data Sets' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.90

??? question "確認問題（1問）"
    **問題.** 優先判定のパフォーマンス・チューニングに関する RODM Data Setsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず優先判定のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. RODM Data Setsの変更点を出力本文から切り離して優先判定のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では RODM Data Sets は「RODM Data Setsの状態と出力メッセージを結び付ける優先判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では RODM Data Setsの出力行と EKG000I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では RODM Data Setsを IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Installation_Migration_Guide.pdf p.90



### RTM Data Collection {#c32-i3137}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'RTM Data Collection' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.137

??? question "確認問題（1問）"
    **問題.** 記録判定のパフォーマンス・チューニングに関係する RTM 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を記録判定で確認する。 ✅
    - B. RTM 機能の名称と担当者名のみを残して記録判定のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では RTM 機能 は「RTM 機能の用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewの RTM 機能と DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では RTM 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.137



### Region Size {#c32-i3138}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Region Size' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.453

??? question "確認問題（1問）"
    **問題.** 終端判定のパフォーマンス・チューニングに関係する Region Sizeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端判定の結果として保存する。 ✅
    - B. Region Sizeの名称と担当者名のみを残して終端判定のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では Region Size は「Region Sizeの用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの Region Sizeと DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では Region Sizeを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.453



### Resource Limits {#c32-i3139}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Resource Limits' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 上書判定のパフォーマンス・チューニングでネットビューの運用確認を行います。Resource Limitsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書判定として引き継ぐ。 ✅
    - D. Resource Limitsの属性行を読まず上書判定のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では Resource Limits は「IBM Z NetViewで Resource Limitsの扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では Resource Limitsの表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では Resource Limitsの使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Running High-level Language Programs in a Preinitialized Environment {#c32-i3140}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Running High-level Language Programs in a Preinitialized Environmentは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較判定のパフォーマンス・チューニングで Running 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Running 機能の出力を取らず比較判定のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較判定の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較判定のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Running 機能 は「比較判定のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Running 機能の属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Running 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SAW Buffer Allocation and Tuning {#c32-i3141}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

SAW Buffer Allocation and Tuningは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域判定のパフォーマンス・チューニングに関する SAW 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. SAW 機能の変更点を出力本文から切り離して値域判定のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域判定の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では SAW 機能 は「SAW 機能の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では SAW 機能の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では SAW 機能を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SAW Data {#c32-i3142}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'SAW Data' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.187

??? question "確認問題（1問）"
    **問題.** 警告判定のパフォーマンス・チューニングに関係する SAW Dataの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告判定の結果として保存する。 ✅
    - B. SAW Dataの名称と担当者名のみを残して警告判定のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では SAW Data は「SAW Dataの用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewの SAW Dataと DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では SAW Dataを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.187



### SAW Option {#c32-i3143}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'SAW Option' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.151

??? question "確認問題（1問）"
    **問題.** 復旧判定のパフォーマンス・チューニングで SAW Optionの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SAW Optionの出力を取らず復旧判定のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧判定の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では SAW Option は「復旧判定のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では SAW Optionの属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では SAW Optionを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Security_Reference.pdf p.151



### SESSMDIS Command {#c32-i3144}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'SESSMDIS Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 展開整理のパフォーマンス・チューニングで SESSMDIS Commandの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SESSMDIS Commandの出力を取らず展開整理のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開整理で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して展開整理のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では SESSMDIS Command は「展開整理のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では SESSMDIS Commandの属性行と DSI633I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では SESSMDIS Commandを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### SRFILTER and SRATIO Commands {#c32-i3145}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'SRFILTER and SRATIO Commands' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.248

??? question "確認問題（1問）"
    **問題.** 置換整理のパフォーマンス・チューニングに関する SRFILTER 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. SRFILTER 機能の変更点を出力本文から切り離して置換整理のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換整理の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では SRFILTER 機能 は「SRFILTER 機能の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では SRFILTER 機能の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では SRFILTER 機能を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.248



### STEPLIB DD Statements {#c32-i3146}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'STEPLIB DD Statements' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.27

??? question "確認問題（1問）"
    **問題.** 上書整理のパフォーマンス・チューニングでネットビューの運用確認を行います。STEPLIB 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書整理の確認記録にまとめる。 ✅
    - D. STEPLIB 機能の属性行を読まず上書整理のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では STEPLIB 機能 は「IBM Z NetViewで STEPLIB 機能の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では STEPLIB 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では STEPLIB 機能の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Installation_Migration_Guide.pdf p.27



### SWRAP Command {#c32-i3147}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'SWRAP Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 優先整理のパフォーマンス・チューニングに関する SWRAP Commandの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. SWRAP Commandの変更点を出力本文から切り離して優先整理のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先整理の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では SWRAP Command は「SWRAP Commandの状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では SWRAP Commandの出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では SWRAP Commandを IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Save/Restore Processing {#c32-i3148}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Save/Restore Processing' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.111

??? question "確認問題（1問）"
    **問題.** 順序判定のSave/Restore Processingでネットビューの運用確認を行います。Save 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定のSave/Restore Processingを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定のSave/Restore Processingを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序判定の確認記録にまとめる。 ✅
    - D. Save 属性の属性行を読まず順序判定のSave/Restore Processingの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では Save 属性 は「IBM Z NetViewで Save 属性の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では Save 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では Save 属性の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.111



### Selective Tracing {#c32-i3149}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Selective Tracing' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Programming_PL_I_and_C.pdf p.33

??? question "確認問題（1問）"
    **問題.** 監査判定のパフォーマンス・チューニングでネットビューの運用確認を行います。Selective Tracingの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査判定として引き継ぐ。 ✅
    - D. Selective Tracingの属性行を読まず監査判定のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Selective Tracing は「IBM Z NetViewで Selective Tracingの扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Selective Tracingの表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Selective Tracingの使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Programming_PL_I_and_C.pdf p.33



### Separation of the Automation Workload from Other NetView Workloads {#c32-i3150}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

Separation of the Automation Workload from Other NetView Workloadsは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更判定のパフォーマンス・チューニングに関する Separation 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Separation 機能の変更点を出力本文から切り離して変更判定のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更判定の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Separation 機能 は「Separation 機能の状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Separation 機能の出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Separation 機能を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Server-Client Configurations {#c32-i3151}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Server-Client Configurations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.85

??? question "確認問題（1問）"
    **問題.** 構文整理のパフォーマンス・チューニングに関係する Server-Client 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文整理の点検結果を残す。 ✅
    - B. Server-Client 機能の名称と担当者名のみを残して構文整理のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では Server-Client 機能 は「Server-Client 機能の用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの Server-Client 機能と DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では Server-Client 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.85



### Single NetView Program Using WLM Enclaves {#c32-i3152}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Single NetView Program Using WLM Enclaves' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Automation_Guide.pdf p.216

??? question "確認問題（1問）"
    **問題.** 呼出整理のパフォーマンス・チューニングでネットビューの運用確認を行います。Single 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出整理の確認値として扱う。 ✅
    - D. Single 機能の属性行を読まず呼出整理のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では Single 機能 は「IBM Z NetViewで Single 機能の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では Single 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では Single 機能の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Automation_Guide.pdf p.216



### Status Focal Point to Programmable Workstation Connectivity {#c32-i3153}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Status Focal Point to Programmable Workstation Connectivityは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端整理のパフォーマンス・チューニングに関係する Status 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を終端整理で確認する。 ✅
    - B. Status 機能の名称と担当者名のみを残して終端整理のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端整理のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では Status 機能 は「Status 機能の用途をネットビューの表示で確認する終端整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの Status 機能と DSI633I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では Status 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Status Monitor STATOPT Filtering {#c32-i3154}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Status Monitor STATOPT Filtering' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 探索整理のパフォーマンス・チューニングで Status 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Status 機能の出力を取らず探索整理のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索整理の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索整理のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Status 機能 は「探索整理のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Status 機能の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Status 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### Storage Considerations {#c32-i3155}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Storage Considerations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19


### Storage Estimates {#c32-i3156}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Storage Estimates' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 条件整理のパフォーマンス・チューニングに関係する Storage Estimatesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件整理の結果として保存する。 ✅
    - B. Storage Estimatesの名称と担当者名のみを残して条件整理のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では Storage Estimates は「Storage Estimatesの用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの Storage Estimatesと DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では Storage Estimatesを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### Subroutines {#c32-i3157}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Subroutines' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.539

??? question "確認問題（1問）"
    **問題.** 区切整理のパフォーマンス・チューニングで Subroutinesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Subroutinesの出力を取らず区切整理のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切整理の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切整理のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では Subroutines は「区切整理のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では Subroutinesの属性行と DSI633I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では Subroutinesを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.539



### Suggestions for Using TASKUTIL {#c32-i3158}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Suggestions for Using TASKUTIL' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 範囲整理のパフォーマンス・チューニングでネットビューの運用確認を行います。Suggestions 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲整理として引き継ぐ。 ✅
    - D. Suggestions 機能の属性行を読まず範囲整理のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Suggestions 機能 は「IBM Z NetViewで Suggestions 機能の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Suggestions 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Suggestions 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### TASKMON Command {#c32-i3159}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'TASKMON Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 記録整理のパフォーマンス・チューニングに関係する TASKMON Commandの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、記録整理の点検結果を残す。 ✅
    - B. TASKMON Commandの名称と担当者名のみを残して記録整理のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では TASKMON Command は「TASKMON Commandの用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの TASKMON Commandと DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では TASKMON Commandを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### TASKUTIL Command {#c32-i3160}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'TASKUTIL Command' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 比較整理のパフォーマンス・チューニングで TASKUTIL Commandの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TASKUTIL Commandの出力を取らず比較整理のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較整理で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して比較整理のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では TASKUTIL Command は「比較整理のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では TASKUTIL Commandの属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では TASKUTIL Commandを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### TASKUTIL Command Output {#c32-i3161}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'TASKUTIL Command Output' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.19

??? question "確認問題（1問）"
    **問題.** 順序整理のパフォーマンス・チューニングでネットビューの運用確認を行います。TASKUTIL 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序整理の確認値として扱う。 ✅
    - D. TASKUTIL 機能の属性行を読まず順序整理のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では TASKUTIL 機能 は「IBM Z NetViewで TASKUTIL 機能の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では TASKUTIL 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では TASKUTIL 機能の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.19



### TCP/IP Support for AON {#c32-i3162}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'TCP/IP Support for AON' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView.pdf p.38

??? question "確認問題（1問）"
    **問題.** 値域整理のTCP/IP Support for AONに関する TCP 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. AONSTAT の結果を残さず値域整理のTCP/IP Support for AONの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理のTCP/IP Support for AONの証跡として保存して根拠にする。
    - C. TCP 属性の変更点を出力本文から切り離して値域整理のTCP/IP Support for AONの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域整理の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では TCP 属性 は「TCP 属性の状態と出力メッセージを結び付ける値域整理項目」と AONSTAT または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では TCP 属性の出力行と EZL000I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では TCP 属性を IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Users_Guide_NetView.pdf p.38



### TRACEGW Parameter {#c32-i3163}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'TRACEGW Parameter' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.73

??? question "確認問題（1問）"
    **問題.** 復旧整理のパフォーマンス・チューニングで TRACEGW Parameterの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TRACEGW Parameterの出力を取らず復旧整理のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、復旧整理の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧整理のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では TRACEGW Parameter は「復旧整理のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では TRACEGW Parameterの属性行と DSI633I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では TRACEGW Parameterを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.73



### Trace Data {#c32-i3164}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Trace Data' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.137

??? question "確認問題（1問）"
    **問題.** 警告整理のパフォーマンス・チューニングに関係する Trace Dataの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を警告整理で確認する。 ✅
    - B. Trace Dataの名称と担当者名のみを残して警告整理のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告整理のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Trace Data は「Trace Dataの用途をネットビューの表示で確認する警告整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの Trace Dataと DSI633I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Trace Dataを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.137



### Tuning Considerations {#c32-i3165}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Tuning Considerations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 監査整理のパフォーマンス・チューニングでネットビューの運用確認を行います。Tuning 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査整理の確認記録にまとめる。 ✅
    - D. Tuning 機能の属性行を読まず監査整理のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Tuning 機能 は「IBM Z NetViewで Tuning 機能の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Tuning 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Tuning 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Tuning REXX Environments {#c32-i3166}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

'Tuning REXX Environments' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 出力記録のパフォーマンス・チューニングに関する Tuning 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LIST CLIST の結果を残さず出力記録のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Tuning 機能の変更点を出力本文から切り離して出力記録のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Tuning 機能 は「Tuning 機能の状態と出力メッセージを結び付ける出力記録項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Tuning 機能の出力行と DSI039I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Tuning 機能を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Tuning Techniques {#c32-i3167}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Tuning Techniques' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 条件記録のパフォーマンス・チューニングに関係する Tuning Techniquesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を条件記録で確認する。 ✅
    - B. Tuning Techniquesの名称と担当者名のみを残して条件記録のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件記録のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Tuning Techniques は「Tuning Techniquesの用途をネットビューの表示で確認する条件記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの Tuning Techniquesと DSI633I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Tuning Techniquesを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Tuning for AON {#c32-i3168}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Tuning for AON' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.6

??? question "確認問題（1問）"
    **問題.** 変更整理のパフォーマンス・チューニングに関する Tuning for AON の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. AONSTAT の結果を残さず変更整理のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Tuning for AON の変更点を出力本文から切り離して変更整理のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では Tuning for AON は「Tuning for AON の状態と出力メッセージを結び付ける変更整理項目」と AONSTAT または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では Tuning for AON の出力行と EZL000I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では Tuning for AON を IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.6



### Tuning for Automated Operations {#c32-i3169}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Tuning for Automated Operations' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.6

??? question "確認問題（1問）"
    **問題.** 構文記録のパフォーマンス・チューニングに関係する Tuning 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、構文記録の結果として保存する。 ✅
    - B. Tuning 機能の名称と担当者名のみを残して構文記録のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では Tuning 機能 は「Tuning 機能の用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの Tuning 機能と DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では Tuning 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.6



### Tuning for Command Procedures {#c32-i3170}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Tuning for Command Procedures' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 展開記録のパフォーマンス・チューニングで Tuning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Tuning 機能の出力を取らず展開記録のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、展開記録の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して展開記録のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Tuning 機能 は「展開記録のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Tuning 機能の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Tuning 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Tuning for VSAM {#c32-i3171}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

'Tuning for VSAM' (Lv2: パフォーマンス・チューニング) は IBM NetView 6.4 における パフォーマンス・チューニング 領域の項目

**出典:** NetView_6.4_Tuning_Guide.pdf p.17

??? question "確認問題（1問）"
    **問題.** 上書記録のパフォーマンス・チューニングでネットビューの運用確認を行います。Tuning for VSAM の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書記録の確認値として扱う。 ✅
    - D. Tuning for VSAM の属性行を読まず上書記録のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Tuning for VSAM は「IBM Z NetViewで Tuning for VSAM の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Tuning for VSAM の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Tuning for VSAM の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Tuning_Guide.pdf p.17



### Tuning for the Hardware Monitor {#c32-i3172}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Tuning for the Hardware Monitorは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出記録のパフォーマンス・チューニングでネットビューの運用確認を行います。Tuning 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出記録として引き継ぐ。 ✅
    - D. Tuning 機能の属性行を読まず呼出記録のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Tuning 機能 は「IBM Z NetViewで Tuning 機能の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Tuning 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Tuning 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Tuning for the NetView Management Console {#c32-i3173}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Tuning for the NetView Management Consoleは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換記録のパフォーマンス・チューニングに関する Tuning 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Tuning 機能の変更点を出力本文から切り離して置換記録のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換記録の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Tuning 機能 は「Tuning 機能の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Tuning 機能の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Tuning 機能を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Tuning for the Resource Object Data Manager {#c32-i3174}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Tuning for the Resource Object Data Managerは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端記録のパフォーマンス・チューニングに関係する Tuning 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端記録の点検結果を残す。 ✅
    - B. Tuning 機能の名称と担当者名のみを残して終端記録のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では Tuning 機能 は「Tuning 機能の用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの Tuning 機能と DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では Tuning 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Tuning for the Session Monitor {#c32-i3175}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Tuning for the Session Monitorは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索記録のパフォーマンス・チューニングで Tuning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Tuning 機能の出力を取らず探索記録のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索記録で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索記録のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Tuning 機能 は「探索記録のパフォーマンス・チューニングに関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Tuning 機能の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Tuning 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Tuning the SAW Buffer Allocation {#c32-i3176}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Tuning the SAW Buffer Allocationは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切記録のパフォーマンス・チューニングで Tuning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Tuning 機能の出力を取らず区切記録のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、区切記録の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して区切記録のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Tuning 機能 は「区切記録のパフォーマンス・チューニングに関係する定義値と表示行を照合する区切記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Tuning 機能の属性行と DSI633I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Tuning 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using BEGIN/END to Improve Efficiency {#c32-i3177}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using BEGIN/END to Improve Efficiencyは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として BEGIN/END を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 展開照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正解はDです。展開照合権限で扱う BEGIN/END は Tivoli NetView z/OS 自動化 の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として BEGIN/END を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Background Pictures {#c32-i3178}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using Background Picturesは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲記録のパフォーマンス・チューニングでネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲記録の確認記録にまとめる。 ✅
    - D. Using 機能の属性行を読まず範囲記録のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Using 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using EMCS Console Support {#c32-i3179}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using EMCS Console Supportは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録記録のパフォーマンス・チューニングに関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録記録の結果として保存する。 ✅
    - B. Using 機能の名称と担当者名のみを残して記録記録のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Full-Screen Automation {#c32-i3180}
*分類: パフォーマンス・チューニング*  ・  難易度: 上級

Using Full-Screen Automationは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較記録のパフォーマンス・チューニングで Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず比較記録のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、比較記録の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して比較記録のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Using 機能 は「比較記録のパフォーマンス・チューニングに関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using General Techniques {#c32-i3181}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using General Techniquesは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序記録のパフォーマンス・チューニングでネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録のパフォーマンス・チューニングを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序記録として引き継ぐ。 ✅
    - D. Using 機能の属性行を読まず順序記録のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Using 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Multiple Autotasks {#c32-i3182}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using Multiple Autotasksは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域記録のパフォーマンス・チューニングに関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して値域記録のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域記録の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Nonpersistent Sessions over Dialed Lines {#c32-i3183}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using Nonpersistent Sessions over Dialed Linesは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告記録のパフォーマンス・チューニングに関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告記録の点検結果を残す。 ✅
    - B. Using 機能の名称と担当者名のみを残して警告記録のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Other Techniques to Improve Efficiency {#c32-i3184}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using Other Techniques to Improve Efficiencyは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧記録のパフォーマンス・チューニングで Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず復旧記録のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧記録で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Using 機能 は「復旧記録のパフォーマンス・チューニングに関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Resource Limits {#c32-i3185}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using Resource Limitsは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査記録のパフォーマンス・チューニングでネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録のパフォーマンス・チューニングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録のパフォーマンス・チューニングを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査記録の確認値として扱う。 ✅
    - D. Using 機能の属性行を読まず監査記録のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Using 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Histogram Data {#c32-i3186}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using the Histogram Dataは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更記録のパフォーマンス・チューニングに関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して変更記録のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NPDA.ALCACHE Statement {#c32-i3187}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using the NPDA.ALCACHE Statementは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文分離のパフォーマンス・チューニングに関係する Using the NPDA 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BNH160I を含む表示を保存し、説明欄との差分を構文分離で確認する。 ✅
    - B. Using the NPDA 属性の名称と担当者名のみを残して構文分離のパフォーマンス・チューニングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離のパフォーマンス・チューニングを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず構文分離のパフォーマンス・チューニングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Using the NPDA 属性 は「Using the NPDA 属性の用途をネットビューの表示で確認する構文分離項目」と NPDA または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの Using the NPDA 属性と BNH160I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Using the NPDA 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NPDA.ALERTFWD Statement {#c32-i3188}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using the NPDA.ALERTFWD Statementは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開分離のパフォーマンス・チューニングで Using the NPDA 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using the NPDA 属性の出力を取らず展開分離のパフォーマンス・チューニングの説明文と承認印のみを残す。
    - B. NPDA の結果から対象行を抜き出し、展開分離の証跡として残す。 ✅
    - C. NPDA を省略して展開分離のパフォーマンス・チューニングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離のパフォーマンス・チューニングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では Using the NPDA 属性 は「展開分離のパフォーマンス・チューニングに関係する定義値と表示行を照合する展開分離項目」と NPDA または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では Using the NPDA 属性の属性行と BNH160I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では Using the NPDA 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NPDA.ALERTLOG Statement {#c32-i3189}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using the NPDA.ALERTLOG Statementは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出分離のパフォーマンス・チューニングでネットビューの運用確認を行います。Using the NPDA 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離のパフォーマンス・チューニングを確認した扱いにする。
    - B. BNH160I の有無を確認せず呼出分離のパフォーマンス・チューニングを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出分離の確認記録にまとめる。 ✅
    - D. Using the NPDA 属性の属性行を読まず呼出分離のパフォーマンス・チューニングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では Using the NPDA 属性 は「IBM Z NetViewで Using the NPDA 属性の扱いを記録する呼出分離項目」と NPDA または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では Using the NPDA 属性の表示結果と BNH160I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では Using the NPDA 属性の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NPDA.DSRBO Statement {#c32-i3190}
*分類: パフォーマンス・チューニング*  ・  難易度: 中級

Using the NPDA.DSRBO Statementは、Tivoli NetView z/OS 自動化のパフォーマンス・チューニングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換分離のパフォーマンス・チューニングに関する Using the NPDA 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. NPDA の結果を残さず置換分離のパフォーマンス・チューニングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離のパフォーマンス・チューニングの証跡として保存して根拠にする。
    - C. Using the NPDA 属性の変更点を出力本文から切り離して置換分離のパフォーマンス・チューニングの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換分離の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Using the NPDA 属性 は「Using the NPDA 属性の状態と出力メッセージを結び付ける置換分離項目」と NPDA または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Using the NPDA 属性の出力行と BNH160I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Using the NPDA 属性を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


