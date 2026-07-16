---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (23/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作)

### Defining Resources in the Network {#c32-i3340}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining Resources in the Networkは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索整理のユーザーズガイド 操作で Defining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Defining 機能の出力を取らず探索整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索整理の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して探索整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Defining 機能 は「探索整理のユーザーズガイド 操作に関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Defining 機能の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Defining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining View Information {#c32-i3341}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining View Informationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序整理のユーザーズガイド 操作でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序整理の根拠を固定する。 ✅
    - D. Defining 機能の属性行を読まず順序整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では Defining 機能の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining a Demonstration View {#c32-i3342}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining a Demonstration Viewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序判定のユーザーズガイド 操作でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序判定の根拠にする。 ✅
    - D. Defining 機能の属性行を読まず順序判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では Defining 機能の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining a Link Resource in a View {#c32-i3343}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining a Link Resource in a Viewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域判定のユーザーズガイド 操作に関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して値域判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、値域判定の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では Defining 機能の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では Defining 機能を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining a MessageView display {#c32-i3344}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining a MessageView displayは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告判定のユーザーズガイド 操作に関係する Defining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、警告判定の採否を説明欄に結び付ける。 ✅
    - B. Defining 機能の名称と担当者名のみを残して警告判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では Defining 機能 は「Defining 機能の用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewの Defining 機能と DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では Defining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining a NetView Command {#c32-i3345}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining a NetView Commandは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧判定のユーザーズガイド 操作で Defining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Defining 機能の出力を取らず復旧判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧判定として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では Defining 機能 は「復旧判定のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では Defining 機能の属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では Defining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining a Node Resource in a View {#c32-i3346}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining a Node Resource in a Viewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査判定のユーザーズガイド 操作でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査判定の確認にする。 ✅
    - D. Defining 機能の属性行を読まず監査判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Defining 機能の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining and Deleting NetView Operators {#c32-i3347}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining and Deleting NetView Operatorsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更判定のユーザーズガイド 操作に関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して変更判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、変更判定の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Defining 機能の出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Defining 機能を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining dependencies {#c32-i3348}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining dependenciesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文整理のユーザーズガイド 操作に関係する Defining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文整理で再確認できる形にする。 ✅
    - B. Defining 機能の名称と担当者名のみを残して構文整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では Defining 機能 は「Defining 機能の用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの Defining 機能と DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では Defining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining initialization statements (EZLINIT) {#c32-i3349}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining initialization statements (EZLINIT)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出整理のユーザーズガイド 操作でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出整理の根拠を固定する。 ✅
    - D. Defining 機能の属性行を読まず呼出整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では Defining 機能の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining multiple systems {#c32-i3350}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining multiple systemsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換整理のユーザーズガイド 操作に関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して置換整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を置換整理で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では Defining 機能の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では Defining 機能を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining status panels {#c32-i3351}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining status panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書整理のユーザーズガイド 操作でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書整理の根拠にする。 ✅
    - D. Defining 機能の属性行を読まず上書整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では Defining 機能の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the IBM Z NetView User ID and Password on the Topology Server {#c32-i3352}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the IBM Z NetView User ID and Password on the Topology Serverは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件整理のユーザーズガイド 操作に関係する Defining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、条件整理の採否を説明欄に結び付ける。 ✅
    - B. Defining 機能の名称と担当者名のみを残して条件整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では Defining 機能 は「Defining 機能の用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの Defining 機能と DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では Defining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the Pop-up Menu Items {#c32-i3353}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the Pop-up Menu Itemsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先整理のユーザーズガイド 操作に関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して優先整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、優先整理の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では Defining 機能の出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では Defining 機能を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the Properties File {#c32-i3354}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the Properties Fileは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較整理のユーザーズガイド 操作で Defining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Defining 機能の出力を取らず比較整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較整理の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して比較整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では Defining 機能 は「比較整理のユーザーズガイド 操作に関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では Defining 機能の属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では Defining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the contents of DDF {#c32-i3355}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the contents of DDFは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力整理のユーザーズガイド 操作に関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して出力整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、出力整理の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける出力整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では Defining 機能の出力行と DSI633I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では Defining 機能を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the panel hierarchy (EZLTREE) {#c32-i3356}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the panel hierarchy (EZLTREE)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切整理のユーザーズガイド 操作で Defining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Defining 機能の出力を取らず区切整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切整理として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して区切整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では Defining 機能 は「区切整理のユーザーズガイド 操作に関係する定義値と表示行を照合する区切整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では Defining 機能の属性行と DSI633I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では Defining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the panel statements (EZLPNLS) {#c32-i3357}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the panel statements (EZLPNLS)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲整理のユーザーズガイド 操作でネットビューの運用確認を行います。Defining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲整理の確認にする。 ✅
    - D. Defining 機能の属性行を読まず範囲整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Defining 機能 は「IBM Z NetViewで Defining 機能の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Defining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Defining 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Defining the priority and color of the resources {#c32-i3358}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Defining the priority and color of the resourcesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録整理のユーザーズガイド 操作に関係する Defining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録整理で再確認できる形にする。 ✅
    - B. Defining 機能の名称と担当者名のみを残して記録整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では Defining 機能 は「Defining 機能の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの Defining 機能と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では Defining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Deleting status descriptors (DDFDEL) {#c32-i3359}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Deleting status descriptors (DDFDEL)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域整理のユーザーズガイド 操作に関する Deleting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Deleting 機能の変更点を出力本文から切り離して値域整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を値域整理で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Deleting 機能 は「Deleting 機能の状態と出力メッセージを結び付ける値域整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Deleting 機能の出力行と DSI633I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Deleting 機能を IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Describing the correlation between INOP messages and NPSI alerts {#c32-i3360}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Describing the correlation between INOP messages and NPSI alertsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告整理のユーザーズガイド 操作に関係する Describing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、警告整理の証跡として残す。 ✅
    - B. Describing 機能の名称と担当者名のみを残して警告整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Describing 機能 は「Describing 機能の用途をネットビューの表示で確認する警告整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの Describing 機能と DSI633I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Describing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why Automation Is Taking Too Much Processing Time {#c32-i3361}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Determining Why Automation Is Taking Too Much Processing Timeは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索記録のユーザーズガイド 操作で Determining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Determining 機能の出力を取らず探索記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索記録の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して探索記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Determining 機能 は「探索記録のユーザーズガイド 操作に関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Determining 機能の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Determining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why a Command List Does Not Complete {#c32-i3362}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why a Command List Does Not Completeは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧整理のユーザーズガイド 操作で Determining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Determining 機能の出力を取らず復旧整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧整理の確認記録にまとめる。 ✅
    - C. LIST CLIST を省略して復旧整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Determining 機能 は「復旧整理のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧整理項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Determining 機能の属性行と DSI039I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Determining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why a Message Is Not Automated by the Automation Table {#c32-i3363}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Determining Why a Message Is Not Automated by the Automation Tableは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査整理のユーザーズガイド 操作でネットビューの運用確認を行います。Determining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査整理の根拠にする。 ✅
    - D. Determining 機能の属性行を読まず監査整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Determining 機能 は「IBM Z NetViewで Determining 機能の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Determining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Determining 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why a Message Is Routed to the Wrong Operator {#c32-i3364}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why a Message Is Routed to the Wrong Operatorは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更整理のユーザーズガイド 操作に関する Determining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Determining 機能の変更点を出力本文から切り離して変更整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、変更整理の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では Determining 機能 は「Determining 機能の状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では Determining 機能の出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では Determining 機能を IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why a Pipe Command Does Not Process Correctly {#c32-i3365}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why a Pipe Command Does Not Process Correctlyは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文記録のユーザーズガイド 操作に関係する Determining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、構文記録の採否を説明欄に結び付ける。 ✅
    - B. Determining 機能の名称と担当者名のみを残して構文記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では Determining 機能 は「Determining 機能の用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの Determining 機能と DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では Determining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why a Timed Command Does Not Run {#c32-i3366}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why a Timed Command Does Not Runは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開記録のユーザーズガイド 操作で Determining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Determining 機能の出力を取らず展開記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開記録として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して展開記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Determining 機能 は「展開記録のユーザーズガイド 操作に関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Determining 機能の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Determining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why an Alert Is Not Automated {#c32-i3367}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why an Alert Is Not Automatedは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出記録のユーザーズガイド 操作でネットビューの運用確認を行います。Determining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出記録の確認にする。 ✅
    - D. Determining 機能の属性行を読まず呼出記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Determining 機能 は「IBM Z NetViewで Determining 機能の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Determining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Determining 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Determining Why an Alert Is Not Displayed in the Tivoli Netcool/OMNIbus Event List {#c32-i3368}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why an Alert Is Not Displayed in the Tivoli Netcool/OMNIbus Event Listは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Determining Why an Event Integration Facility Event Is Not Forwarded to the NetView Program {#c32-i3369}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Determining Why an Event Integration Facility Event Is Not Forwarded to the NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Displaying Control Points {#c32-i3370}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Control Pointsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.132) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.132)

??? question "確認問題（1問）"
    **問題.** 出力記録のユーザーズガイド 操作に関する Displaying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Displaying 機能の変更点を出力本文から切り離して出力記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を出力記録で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Displaying 機能 は「Displaying 機能の状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Displaying 機能の出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Displaying 機能を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying Data Sets Used by the NetView Program {#c32-i3371}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Data Sets Used by the NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件記録のユーザーズガイド 操作に関係する Displaying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、条件記録の証跡として残す。 ✅
    - B. Displaying 機能の名称と担当者名のみを残して条件記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Displaying 機能 は「Displaying 機能の用途をネットビューの表示で確認する条件記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの Displaying 機能と DSI633I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Displaying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying Host Help Information {#c32-i3372}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Host Help Informationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.261) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.261)

??? question "確認問題（1問）"
    **問題.** 区切記録のユーザーズガイド 操作で Displaying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Displaying 機能の出力を取らず区切記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切記録の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して区切記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Displaying 機能 は「区切記録のユーザーズガイド 操作に関係する定義値と表示行を照合する区切記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Displaying 機能の属性行と DSI633I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Displaying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying Network Status on a single panel {#c32-i3373}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Network Status on a single panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先記録のユーザーズガイド 操作に関する Displaying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Displaying 機能の変更点を出力本文から切り離して優先記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、優先記録の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Displaying 機能 は「Displaying 機能の状態と出力メッセージを結び付ける優先記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Displaying 機能の出力行と DSI633I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Displaying 機能を IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying Network Status on multiple panels {#c32-i3374}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Network Status on multiple panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録記録のユーザーズガイド 操作に関係する Displaying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、記録記録の採否を説明欄に結び付ける。 ✅
    - B. Displaying 機能の名称と担当者名のみを残して記録記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Displaying 機能 は「Displaying 機能の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの Displaying 機能と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Displaying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying Resource Status (Status Monitor) {#c32-i3375}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Resource Status (Status Monitor)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide NetView (p.240) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.240)

??? question "確認問題（1問）"
    **問題.** 復旧記録のユーザーズガイド 操作で Displaying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Displaying 機能の出力を取らず復旧記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧記録の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Displaying 機能 は「復旧記録のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Displaying 機能の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Displaying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying SNA resource information with AutoView {#c32-i3376}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying SNA resource information with AutoViewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査記録のユーザーズガイド 操作でネットビューの運用確認を行います。Displaying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査記録の根拠を固定する。 ✅
    - D. Displaying 機能の属性行を読まず監査記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Displaying 機能 は「IBM Z NetViewで Displaying 機能の扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Displaying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Displaying 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying Views in a Web Browser {#c32-i3377}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying Views in a Web Browserは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件分離のユーザーズガイド 操作に関係する Displaying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件分離で再確認できる形にする。 ✅
    - B. Displaying 機能の名称と担当者名のみを残して条件分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では Displaying 機能 は「Displaying 機能の用途をネットビューの表示で確認する条件分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM Z NetViewの Displaying 機能と DSI633I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では Displaying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying configuration data {#c32-i3378}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying configuration dataは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.78) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.78)

??? question "確認問題（1問）"
    **問題.** 上書記録のユーザーズガイド 操作でネットビューの運用確認を行います。Displaying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書記録の根拠を固定する。 ✅
    - D. Displaying 機能の属性行を読まず上書記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Displaying 機能 は「IBM Z NetViewで Displaying 機能の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Displaying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Displaying 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying network status {#c32-i3379}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying network statusは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.123) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.123)

??? question "確認問題（1問）"
    **問題.** 範囲記録のユーザーズガイド 操作でネットビューの運用確認を行います。Displaying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲記録の根拠にする。 ✅
    - D. Displaying 機能の属性行を読まず範囲記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Displaying 機能 は「IBM Z NetViewで Displaying 機能の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Displaying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Displaying 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying or replacing a definition {#c32-i3380}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying or replacing a definitionは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較記録のユーザーズガイド 操作で Displaying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Displaying 機能の出力を取らず比較記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較記録として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して比較記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Displaying 機能 は「比較記録のユーザーズガイド 操作に関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Displaying 機能の属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Displaying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying or replacing an option definition table {#c32-i3381}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying or replacing an option definition tableは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序記録のユーザーズガイド 操作でネットビューの運用確認を行います。Displaying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序記録の確認にする。 ✅
    - D. Displaying 機能の属性行を読まず順序記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Displaying 機能 は「IBM Z NetViewで Displaying 機能の扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Displaying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Displaying 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying resource information (an SNA example) {#c32-i3382}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying resource information (an SNA example)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.46) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.46)

??? question "確認問題（1問）"
    **問題.** 値域記録のユーザーズガイド 操作に関する Displaying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Displaying 機能の変更点を出力本文から切り離して値域記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、値域記録の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では Displaying 機能 は「Displaying 機能の状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では Displaying 機能の出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では Displaying 機能を IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying resource information with AutoView {#c32-i3383}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying resource information with AutoViewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告記録のユーザーズガイド 操作に関係する Displaying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告記録で再確認できる形にする。 ✅
    - B. Displaying 機能の名称と担当者名のみを残して警告記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Displaying 機能 は「Displaying 機能の用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの Displaying 機能と DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Displaying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying status data {#c32-i3384}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying status dataは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.81) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.81)

??? question "確認問題（1問）"
    **問題.** 変更記録のユーザーズガイド 操作に関する Displaying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Displaying 機能の変更点を出力本文から切り離して変更記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を変更記録で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Displaying 機能 は「Displaying 機能の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Displaying 機能の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Displaying 機能を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Displaying the AON Base Functions Panel {#c32-i3385}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the AON Base Functions Panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文分離のユーザーズガイド 操作に関係する Displaying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. AONSTAT の結果から対象行を抜き出し、構文分離の証跡として残す。 ✅
    - B. Displaying 機能の名称と担当者名のみを残して構文分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず構文分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Displaying 機能 は「Displaying 機能の用途をネットビューの表示で確認する構文分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの Displaying 機能と EZL000I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Displaying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the AON Help Desk {#c32-i3386}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the AON Help Deskは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開分離のユーザーズガイド 操作で Displaying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Displaying 機能の出力を取らず展開分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開分離の確認記録にまとめる。 ✅
    - C. AONSTAT を省略して展開分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では Displaying 機能 は「展開分離のユーザーズガイド 操作に関係する定義値と表示行を照合する展開分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では Displaying 機能の属性行と EZL000I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では Displaying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the AON: AutoView panel {#c32-i3387}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the AON: AutoView panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換分離の:に関する Displaying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. AONSTAT の結果を残さず置換分離の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の:の証跡として保存して根拠にする。
    - C. Displaying 機能の変更点を出力本文から切り離して置換分離の:の承認欄のみ残す。
    - D. 同じ画面で対象行と EZL000I を読み、置換分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Displaying 機能 は「Displaying 機能の状態と出力メッセージを結び付ける置換分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Displaying 機能の出力行と EZL000I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Displaying 機能を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the AON: Automation Settings Panel {#c32-i3388}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Displaying the AON: Automation Settings Panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出分離の:でネットビューの運用確認を行います。Displaying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離の:を確認した扱いにする。
    - B. EZL000I の有無を確認せず呼出分離の:を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出分離の根拠にする。 ✅
    - D. Displaying 機能の属性行を読まず呼出分離の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では Displaying 機能 は「IBM Z NetViewで Displaying 機能の扱いを記録する呼出分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では Displaying 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では Displaying 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the AON: Operator Commands Main Menu {#c32-i3389}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the AON: Operator Commands Main Menuは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端分離の:に関係する Displaying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. AONSTAT で得た表示本文を使い、終端分離の採否を説明欄に結び付ける。 ✅
    - B. Displaying 機能の名称と担当者名のみを残して終端分離の:の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離の:を確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず終端分離の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では Displaying 機能 は「Displaying 機能の用途をネットビューの表示で確認する終端分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの Displaying 機能と EZL000I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では Displaying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the AON: Task and Log Maintenance panel {#c32-i3390}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the AON: Task and Log Maintenance panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索分離の:で Displaying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Displaying 機能の出力を取らず探索分離の:の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索分離として引き継ぐ。 ✅
    - C. AONSTAT を省略して探索分離の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では Displaying 機能 は「探索分離の:に関係する定義値と表示行を照合する探索分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では Displaying 機能の属性行と EZL000I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では Displaying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the Cross-Domain Functions panel {#c32-i3391}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the Cross-Domain Functions panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書分離のユーザーズガイド 操作でネットビューの運用確認を行います。Displaying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書分離の確認にする。 ✅
    - D. Displaying 機能の属性行を読まず上書分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では Displaying 機能 は「IBM Z NetViewで Displaying 機能の扱いを記録する上書分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では Displaying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では Displaying 機能の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Displaying the Support Functions panel {#c32-i3392}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Displaying the Support Functions panelは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力分離のユーザーズガイド 操作に関する Displaying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Displaying 機能の変更点を出力本文から切り離して出力分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、出力分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では Displaying 機能 は「Displaying 機能の状態と出力メッセージを結び付ける出力分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では Displaying 機能の出力行と DSI633I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では Displaying 機能を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Distributed DVIPA Connection Routing Attributes {#c32-i3393}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Connection Routing Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.127) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.127)

??? question "確認問題（1問）"
    **問題.** 範囲分離のユーザーズガイド 操作でネットビューの運用確認を行います。Distributed 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲分離の根拠を固定する。 ✅
    - D. Distributed 機能の属性行を読まず範囲分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では Distributed 機能 は「IBM Z NetViewで Distributed 機能の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では Distributed 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では Distributed 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Connection Routing Workspace {#c32-i3394}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Connection Routing Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.34) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.34)

??? question "確認問題（1問）"
    **問題.** 優先分離のユーザーズガイド 操作に関する Distributed 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Distributed 機能の変更点を出力本文から切り離して優先分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を優先分離で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では Distributed 機能 は「Distributed 機能の状態と出力メッセージを結び付ける優先分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では Distributed 機能の出力行と DSI633I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では Distributed 機能を IBM Z NetViewの確認記録に残し、対象名は優先分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Server Health Attributes {#c32-i3395}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Server Health Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.128) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.128)

??? question "確認問題（1問）"
    **問題.** 記録分離のユーザーズガイド 操作に関係する Distributed 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、記録分離の証跡として残す。 ✅
    - B. Distributed 機能の名称と担当者名のみを残して記録分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では Distributed 機能 は「Distributed 機能の用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの Distributed 機能と DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では Distributed 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Server Health Details Workspace {#c32-i3396}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Server Health Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.36) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.36)

??? question "確認問題（1問）"
    **問題.** 比較分離のユーザーズガイド 操作で Distributed 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Distributed 機能の出力を取らず比較分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較分離の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して比較分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では Distributed 機能 は「比較分離のユーザーズガイド 操作に関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では Distributed 機能の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では Distributed 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Server Health Workspace {#c32-i3397}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Server Health Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.35) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.35)

??? question "確認問題（1問）"
    **問題.** 順序分離のユーザーズガイド 操作でネットビューの運用確認を行います。Distributed 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序分離の根拠にする。 ✅
    - D. Distributed 機能の属性行を読まず順序分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では Distributed 機能 は「IBM Z NetViewで Distributed 機能の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では Distributed 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では Distributed 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Targets Attributes {#c32-i3398}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Targets Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.130) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.130)

??? question "確認問題（1問）"
    **問題.** 値域分離のユーザーズガイド 操作に関する Distributed 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Distributed 機能の変更点を出力本文から切り離して値域分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、値域分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では Distributed 機能 は「Distributed 機能の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では Distributed 機能の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では Distributed 機能を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Targets Workspace {#c32-i3399}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Targets Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.37) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.37)

??? question "確認問題（1問）"
    **問題.** 警告分離のユーザーズガイド 操作に関係する Distributed 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、警告分離の採否を説明欄に結び付ける。 ✅
    - B. Distributed 機能の名称と担当者名のみを残して警告分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では Distributed 機能 は「Distributed 機能の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの Distributed 機能と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では Distributed 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed DVIPA Unhealthy Servers Workspace {#c32-i3400}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed DVIPA Unhealthy Servers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.38) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.38)

??? question "確認問題（1問）"
    **問題.** 復旧分離のユーザーズガイド 操作で Distributed 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Distributed 機能の出力を取らず復旧分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧分離として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Distributed 機能 は「復旧分離のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Distributed 機能の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Distributed 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Distributed Database Retrieval {#c32-i3401}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Distributed Database Retrievalは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.125) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.125)

??? question "確認問題（1問）"
    **問題.** 区切分離のユーザーズガイド 操作で Distributed 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Distributed 機能の出力を取らず区切分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切分離の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して区切分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では Distributed 機能 は「区切分離のユーザーズガイド 操作に関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では Distributed 機能の属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では Distributed 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Driving the Inform Policy (EZLENFRM) {#c32-i3402}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Driving the Inform Policy (EZLENFRM)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査分離のユーザーズガイド 操作でネットビューの運用確認を行います。Driving 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査分離の確認にする。 ✅
    - D. Driving 機能の属性行を読まず監査分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Driving 機能 は「IBM Z NetViewで Driving 機能の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Driving 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Driving 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### During Initial Sign On {#c32-i3403}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

During Initial Sign Onは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.175) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.175)

??? question "確認問題（1問）"
    **問題.** 変更分離のユーザーズガイド 操作に関する During 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. During 機能の変更点を出力本文から切り離して変更分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、変更分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では During 機能 は「During 機能の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では During 機能の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では During 機能を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### During Installation {#c32-i3404}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

During Installationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.175) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.175)

??? question "確認問題（1問）"
    **問題.** 構文読解のユーザーズガイド 操作に関係する During 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文読解で再確認できる形にする。 ✅
    - B. During 機能の名称と担当者名のみを残して構文読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では During 機能 は「During 機能の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewの During 機能と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では During 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### During Subsequent Sign On {#c32-i3405}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

During Subsequent Sign Onは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.176) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.176)

??? question "確認問題（1問）"
    **問題.** 展開読解のユーザーズガイド 操作で During 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. During 機能の出力を取らず展開読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開読解の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して展開読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では During 機能 は「展開読解のユーザーズガイド 操作に関係する定義値と表示行を照合する展開読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では During 機能の属性行と DSI633I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では During 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT01 - EXIT04 processing during NCP recovery {#c32-i3406}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT01 - EXIT04 processing during NCP recoveryは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.368) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.368)

??? question "確認問題（1問）"
    **問題.** 監査読解のユーザーズガイド 操作でネットビューの運用確認を行います。EXIT01 出口の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査読解のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査読解の根拠にする。 ✅
    - D. EXIT01 出口の属性行を読まず監査読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では EXIT01 出口 は「IBM Z NetViewで EXIT01 出口の扱いを記録する監査読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では EXIT01 出口の表示結果と DSI633I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では EXIT01 出口の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT05 processing (EZLEAGRN) {#c32-i3407}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT05 processing (EZLEAGRN)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.370) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.370)

??? question "確認問題（1問）"
    **問題.** 変更読解のユーザーズガイド 操作に関する EXIT05 processing 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. EXIT05 processing 属性の変更点を出力本文から切り離して変更読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、変更読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では EXIT05 processing 属性 は「EXIT05 processing 属性の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では EXIT05 processing 属性の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では EXIT05 processing 属性を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT06 processing (EZLEATHR) {#c32-i3408}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT06 processing (EZLEATHR)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.371) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.371)

??? question "確認問題（1問）"
    **問題.** 構文検分のユーザーズガイド 操作に関係する EXIT06 processing 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、構文検分の採否を説明欄に結び付ける。 ✅
    - B. EXIT06 processing 属性の名称と担当者名のみを残して構文検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では EXIT06 processing 属性 は「EXIT06 processing 属性の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの EXIT06 processing 属性と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では EXIT06 processing 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT07 Processing (EZLECAUT) {#c32-i3409}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT07 Processing (EZLECAUT)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.373) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.373)

??? question "確認問題（1問）"
    **問題.** 展開検分のユーザーズガイド 操作で EXIT07 Processing 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EXIT07 Processing 属性の出力を取らず展開検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開検分として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して展開検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では EXIT07 Processing 属性 は「展開検分のユーザーズガイド 操作に関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では EXIT07 Processing 属性の属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では EXIT07 Processing 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT08 processing (AON messaging) {#c32-i3410}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT08 processing (AON messaging)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.375) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.375)

??? question "確認問題（1問）"
    **問題.** 呼出検分のユーザーズガイド 操作でネットビューの運用確認を行います。EXIT08 processing 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分のユーザーズガイド 操作を確認した扱いにする。
    - B. EZL000I の有無を確認せず呼出検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出検分の確認にする。 ✅
    - D. EXIT08 processing 属性の属性行を読まず呼出検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では EXIT08 processing 属性 は「IBM Z NetViewで EXIT08 processing 属性の扱いを記録する呼出検分項目」と AONSTAT または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では EXIT08 processing 属性の表示結果と EZL000I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では EXIT08 processing 属性の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT09 processing (EZLECATV) {#c32-i3411}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT09 processing (EZLECATV)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.376) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.376)

??? question "確認問題（1問）"
    **問題.** 置換検分のユーザーズガイド 操作に関する EXIT09 processing 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. EXIT09 processing 属性の変更点を出力本文から切り離して置換検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、置換検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では EXIT09 processing 属性 は「EXIT09 processing 属性の状態と出力メッセージを結び付ける置換検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では EXIT09 processing 属性の出力行と DSI633I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では EXIT09 processing 属性を IBM Z NetViewの確認記録に残し、対象名は置換検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT10 processing (EZLENTFY) {#c32-i3412}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT10 processing (EZLENTFY)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.378) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.378)

??? question "確認問題（1問）"
    **問題.** 終端検分のユーザーズガイド 操作に関係する EXIT10 processing 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検分で再確認できる形にする。 ✅
    - B. EXIT10 processing 属性の名称と担当者名のみを残して終端検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では EXIT10 processing 属性 は「EXIT10 processing 属性の用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの EXIT10 processing 属性と DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では EXIT10 processing 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT11 and EXIT12 Inform Policy processing {#c32-i3413}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT11 and EXIT12 Inform Policy processingは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検分のユーザーズガイド 操作で EXIT11 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EXIT11 機能の出力を取らず探索検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索検分の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して探索検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では EXIT11 機能 は「探索検分のユーザーズガイド 操作に関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では EXIT11 機能の属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では EXIT11 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### EXIT13 Socket Monitoring {#c32-i3414}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT13 Socket Monitoringは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書検分のユーザーズガイド 操作でネットビューの運用確認を行います。EXIT13 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書検分の根拠を固定する。 ✅
    - D. EXIT13 機能の属性行を読まず上書検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では EXIT13 機能 は「IBM Z NetViewで EXIT13 機能の扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では EXIT13 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では EXIT13 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### EXIT14 SNMP MIB polling {#c32-i3415}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT14 SNMP MIB pollingは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.383) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.383)

??? question "確認問題（1問）"
    **問題.** 出力検分のユーザーズガイド 操作に関する EXIT14 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. EXIT14 機能の変更点を出力本文から切り離して出力検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を出力検分で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では EXIT14 機能 は「EXIT14 機能の状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では EXIT14 機能の出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では EXIT14 機能を IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### EXIT15 SNMP MIB thresholding {#c32-i3416}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

EXIT15 SNMP MIB thresholdingは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.385) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.385)

??? question "確認問題（1問）"
    **問題.** 条件検分のユーザーズガイド 操作に関係する EXIT15 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、条件検分の証跡として残す。 ✅
    - B. EXIT15 機能の名称と担当者名のみを残して条件検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では EXIT15 機能 は「EXIT15 機能の用途をネットビューの表示で確認する条件検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの EXIT15 機能と DSI633I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では EXIT15 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Editing EZLPNLS {#c32-i3417}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Editing EZLPNLSは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録読解のユーザーズガイド 操作に関係する Editing EZLPNLS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録読解で再確認できる形にする。 ✅
    - B. Editing EZLPNLS の名称と担当者名のみを残して記録読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Editing EZLPNLS は「Editing EZLPNLS の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの Editing EZLPNLS と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Editing EZLPNLS を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Elements in the ihsaudit.xml file {#c32-i3418}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Elements in the ihsaudit.xml fileは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較読解のユーザーズガイド 操作で Elements 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Elements 機能の出力を取らず比較読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較読解の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して比較読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Elements 機能 は「比較読解のユーザーズガイド 操作に関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Elements 機能の属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Elements 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enabling and Disabling Sections of an Automation Table {#c32-i3419}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Enabling and Disabling Sections of an Automation Tableは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域読解のユーザーズガイド 操作に関する Enabling 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Enabling 機能の変更点を出力本文から切り離して値域読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を値域読解で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では Enabling 機能 は「Enabling 機能の状態と出力メッセージを結び付ける値域読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では Enabling 機能の出力行と DSI633I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では Enabling 機能を IBM Z NetViewの確認記録に残し、対象名は値域読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enabling and disabling automation {#c32-i3420}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Enabling and disabling automationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序読解のユーザーズガイド 操作でネットビューの運用確認を行います。Enabling 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序読解の根拠を固定する。 ✅
    - D. Enabling 機能の属性行を読まず順序読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Enabling 機能 は「IBM Z NetViewで Enabling 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Enabling 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Enabling 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enabling the Examples {#c32-i3421}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Enabling the Examplesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告読解のユーザーズガイド 操作に関係する Enabling 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、警告読解の証跡として残す。 ✅
    - B. Enabling 機能の名称と担当者名のみを残して警告読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Enabling 機能 は「Enabling 機能の用途をネットビューの表示で確認する警告読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの Enabling 機能と DSI633I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Enabling 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Enterprise Management Agent Changes {#c32-i3422}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Enterprise Management Agent Changesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.29) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.29)


### Filtered DVIPA Connections Workspace {#c32-i3423}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered DVIPA Connections Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45)

??? question "確認問題（1問）"
    **問題.** 比較検分のユーザーズガイド 操作で Filtered 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Filtered 機能の出力を取らず比較検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較検分として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して比較検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Filtered 機能 は「比較検分のユーザーズガイド 操作に関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Filtered 機能の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Filtered 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered DVIPA Definition and Status Workspace {#c32-i3424}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered DVIPA Definition and Status Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検分のユーザーズガイド 操作でネットビューの運用確認を行います。Filtered 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序検分の確認にする。 ✅
    - D. Filtered 機能の属性行を読まず順序検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Filtered 機能 は「IBM Z NetViewで Filtered 機能の扱いを記録する順序検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Filtered 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Filtered 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Filtered DVIPA Sysplex Distributors Workspace {#c32-i3425}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered DVIPA Sysplex Distributors Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45)

??? question "確認問題（1問）"
    **問題.** 値域検分のユーザーズガイド 操作に関する Filtered 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Filtered 機能の変更点を出力本文から切り離して値域検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、値域検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Filtered 機能 は「Filtered 機能の状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Filtered 機能の出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Filtered 機能を IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Distributed DVIPA Server Health Workspace {#c32-i3426}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Distributed DVIPA Server Health Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.44) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.44)

??? question "確認問題（1問）"
    **問題.** 範囲検分のユーザーズガイド 操作でネットビューの運用確認を行います。Filtered 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲検分の根拠にする。 ✅
    - D. Filtered 機能の属性行を読まず範囲検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Filtered 機能 は「IBM Z NetViewで Filtered 機能の扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Filtered 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Filtered 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Distributed DVIPA Targets Workspace {#c32-i3427}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Distributed DVIPA Targets Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.44) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.44)

??? question "確認問題（1問）"
    **問題.** 優先検分のユーザーズガイド 操作に関する Filtered 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Filtered 機能の変更点を出力本文から切り離して優先検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、優先検分の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Filtered 機能 は「Filtered 機能の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Filtered 機能の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Filtered 機能を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Distributed DVIPA Unhealthy Servers Workspace {#c32-i3428}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Distributed DVIPA Unhealthy Servers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45)

??? question "確認問題（1問）"
    **問題.** 記録検分のユーザーズガイド 操作に関係する Filtered 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、記録検分の採否を説明欄に結び付ける。 ✅
    - B. Filtered 機能の名称と担当者名のみを残して記録検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Filtered 機能 は「Filtered 機能の用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewの Filtered 機能と DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Filtered 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Inactive TCPIP Connection Data Workspace {#c32-i3429}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Filtered Inactive TCPIP Connection Data Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.53) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.53)

??? question "確認問題（1問）"
    **問題.** 警告検分のユーザーズガイド 操作に関係する Filtered 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告検分で再確認できる形にする。 ✅
    - B. Filtered 機能の名称と担当者名のみを残して警告検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Filtered 機能 は「Filtered 機能の用途をネットビューの表示で確認する警告検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM Z NetViewの Filtered 機能と DSI633I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Filtered 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Replication Servers Workspace {#c32-i3430}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Replication Servers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.78) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.78)

??? question "確認問題（1問）"
    **問題.** 復旧検分のユーザーズガイド 操作で Filtered 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Filtered 機能の出力を取らず復旧検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧検分の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Filtered 機能 は「復旧検分のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Filtered 機能の属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Filtered 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Session Data Workspace {#c32-i3431}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Session Data Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.65) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.65)

??? question "確認問題（1問）"
    **問題.** 監査検分のユーザーズガイド 操作でネットビューの運用確認を行います。Filtered 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査検分の根拠を固定する。 ✅
    - D. Filtered 機能の属性行を読まず監査検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Filtered 機能 は「IBM Z NetViewで Filtered 機能の扱いを記録する監査検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Filtered 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Filtered 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered TCPIP Connection Data Workspace {#c32-i3432}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Filtered TCPIP Connection Data Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.53) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.53)

??? question "確認問題（1問）"
    **問題.** 変更検分のユーザーズガイド 操作に関する Filtered 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Filtered 機能の変更点を出力本文から切り離して変更検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を変更検分で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Filtered 機能 は「Filtered 機能の状態と出力メッセージを結び付ける変更検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Filtered 機能の出力行と DSI633I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Filtered 機能を IBM Z NetViewの確認記録に残し、対象名は変更検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Telnet Server Configuration and Status Workspace {#c32-i3433}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Telnet Server Configuration and Status Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文確認のユーザーズガイド 操作に関係する Filtered 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文確認として引き継ぐ。 ✅
    - B. Filtered 機能の名称と担当者名のみを残して構文確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Filtered 機能 は「Filtered 機能の用途をネットビューの表示で確認する構文確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Z NetViewの Filtered 機能と DSI633I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Filtered 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Filtered Workload Servers Workspace {#c32-i3434}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Workload Servers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.78) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.78)

??? question "確認問題（1問）"
    **問題.** 展開確認のユーザーズガイド 操作で Filtered 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Filtered 機能の出力を取らず展開確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開確認の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して展開確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Filtered 機能 は「展開確認のユーザーズガイド 操作に関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Filtered 機能の属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Filtered 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Filtered Workloads Workspace {#c32-i3435}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Filtered Workloads Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.79) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.79)

??? question "確認問題（1問）"
    **問題.** 呼出確認のユーザーズガイド 操作でネットビューの運用確認を行います。Filtered 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出確認のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、呼出確認の点検結果を残す。 ✅
    - D. Filtered 機能の属性行を読まず呼出確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Filtered 機能 は「IBM Z NetViewで Filtered 機能の扱いを記録する呼出確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Filtered 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Filtered 機能の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Finding Resources {#c32-i3436}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Finding Resourcesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide NetView Management Console (p.92) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.92)

??? question "確認問題（1問）"
    **問題.** 終端確認のユーザーズガイド 操作に関係する Finding Resourcesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端確認の確認値として扱う。 ✅
    - B. Finding Resourcesの名称と担当者名のみを残して終端確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Finding Resources は「Finding Resourcesの用途をネットビューの表示で確認する終端確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Z NetViewの Finding Resourcesと DSI633I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Finding Resourcesを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Finding defined resources {#c32-i3437}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Finding defined resourcesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.138) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.138)

??? question "確認問題（1問）"
    **問題.** 置換確認のユーザーズガイド 操作に関する Finding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Finding 機能の変更点を出力本文から切り離して置換確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Finding 機能 は「Finding 機能の状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Finding 機能の出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Finding 機能を IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Finding the Resource ID {#c32-i3438}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Finding the Resource IDは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide NetView Management Console (p.135) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.135)

??? question "確認問題（1問）"
    **問題.** 探索確認のユーザーズガイド 操作で Finding 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Finding 機能の出力を取らず探索確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索確認の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して探索確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Finding 機能 は「探索確認のユーザーズガイド 操作に関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Finding 機能の属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Finding 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Format for option definition table entries {#c32-i3439}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Format for option definition table entriesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切確認のユーザーズガイド 操作で Format 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Format 機能の出力を取らず区切確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切確認の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して区切確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Format 機能 は「区切確認のユーザーズガイド 操作に関係する定義値と表示行を照合する区切確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Format 機能の属性行と DSI633I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Format 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Formatting Panel Messages (EZLEMSG) {#c32-i3440}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Formatting Panel Messages (EZLEMSG)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.329) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.329)

??? question "確認問題（1問）"
    **問題.** 範囲確認のユーザーズガイド 操作でネットビューの運用確認を行います。Formatting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、範囲確認の結果として保存する。 ✅
    - D. Formatting 機能の属性行を読まず範囲確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Formatting 機能 は「IBM Z NetViewで Formatting 機能の扱いを記録する範囲確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Formatting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Formatting 機能の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Forwarding User Messages (EZLE1UFW) {#c32-i3441}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Forwarding User Messages (EZLE1UFW)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.309) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.309)

??? question "確認問題（1問）"
    **問題.** 優先確認のユーザーズガイド 操作に関する Forwarding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Forwarding 機能の変更点を出力本文から切り離して優先確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、優先確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Forwarding 機能 は「Forwarding 機能の状態と出力メッセージを結び付ける優先確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Forwarding 機能の出力行と DSI633I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Forwarding 機能を IBM Z NetViewの確認記録に残し、対象名は優先確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### GDPS Continuous Availability Solution Situations {#c32-i3442}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

GDPS Continuous Availability Solution Situationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.105) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.105)

??? question "確認問題（1問）"
    **問題.** 値域確認のユーザーズガイド 操作に関する GDPS 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. GDPS 機能の変更点を出力本文から切り離して値域確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では GDPS 機能 は「GDPS 機能の状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では GDPS 機能の出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では GDPS 機能を IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### GDPS Continuous Availability Solution Workspaces {#c32-i3443}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

GDPS Continuous Availability Solution Workspacesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.75) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.75)

??? question "確認問題（1問）"
    **問題.** 警告確認のユーザーズガイド 操作に関係する GDPS 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告確認の確認値として扱う。 ✅
    - B. GDPS 機能の名称と担当者名のみを残して警告確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では GDPS 機能 は「GDPS 機能の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの GDPS 機能と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では GDPS 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### General Resource VTAM messages {#c32-i3444}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

General Resource VTAM messagesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.415) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.415)

??? question "確認問題（1問）"
    **問題.** 復旧確認のユーザーズガイド 操作で General 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. General 機能の出力を取らず復旧確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧確認の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では General 機能 は「復旧確認のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では General 機能の属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では General 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Getting Resource Information (EZLEAGRN) {#c32-i3445}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Getting Resource Information (EZLEAGRN)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.311) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.311)

??? question "確認問題（1問）"
    **問題.** 構文照合のユーザーズガイド 操作に関係する Getting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文照合の確認記録にまとめる。 ✅
    - B. Getting 機能の名称と担当者名のみを残して構文照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Getting 機能 は「Getting 機能の用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの Getting 機能と DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Getting 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Getting help {#c32-i3446}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Getting helpは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更確認のユーザーズガイド 操作に関する Getting helpの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Getting helpの変更点を出力本文から切り離して変更確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更確認の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Getting help は「Getting helpの状態と出力メッセージを結び付ける変更確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Getting helpの出力行と DSI633I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Getting helpを IBM Z NetViewの確認記録に残し、対象名は変更確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Getting started {#c32-i3447}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Getting startedは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Getting started with AON/SNA {#c32-i3448}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Getting started with AON/SNAは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出照合のユーザーズガイド 操作でネットビューの運用確認を行います。Getting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合のユーザーズガイド 操作を確認した扱いにする。
    - B. EZL000I の有無を確認せず呼出照合のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と EZL000I を読み、呼出照合の結果として保存する。 ✅
    - D. Getting 機能の属性行を読まず呼出照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では Getting 機能 は「IBM Z NetViewで Getting 機能の扱いを記録する呼出照合項目」と AONSTAT または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では Getting 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では Getting 機能の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Grouping resources in DDF {#c32-i3449}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Grouping resources in DDFは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.267) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.267)

??? question "確認問題（1問）"
    **問題.** 置換照合のユーザーズガイド 操作に関する Grouping 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Grouping 機能の変更点を出力本文から切り離して置換照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、置換照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では Grouping 機能 は「Grouping 機能の状態と出力メッセージを結び付ける置換照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では Grouping 機能の出力行と DSI633I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では Grouping 機能を IBM Z NetViewの確認記録に残し、対象名は置換照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Guidelines for option definition table entries {#c32-i3450}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Guidelines for option definition table entriesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端照合のユーザーズガイド 操作に関係する Guidelines 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端照合として引き継ぐ。 ✅
    - B. Guidelines 機能の名称と担当者名のみを残して終端照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では Guidelines 機能 は「Guidelines 機能の用途をネットビューの表示で確認する終端照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM Z NetViewの Guidelines 機能と DSI633I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では Guidelines 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Health Situations {#c32-i3451}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Health Situationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.100)

??? question "確認問題（1問）"
    **問題.** 探索照合のユーザーズガイド 操作で Health Situationsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Health Situationsの出力を取らず探索照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索照合の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して探索照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では Health Situations は「探索照合のユーザーズガイド 操作に関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では Health Situationsの属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では Health Situationsを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### HiperSockets Configuration and Status Attributes {#c32-i3452}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

HiperSockets Configuration and Status Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書照合のユーザーズガイド 操作でネットビューの運用確認を行います。HiperSockets 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書照合のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書照合の点検結果を残す。 ✅
    - D. HiperSockets 機能の属性行を読まず上書照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では HiperSockets 機能 は「IBM Z NetViewで HiperSockets 機能の扱いを記録する上書照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では HiperSockets 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では HiperSockets 機能の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### HiperSockets Configuration and Status Workspace {#c32-i3453}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

HiperSockets Configuration and Status Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力照合のユーザーズガイド 操作に関する HiperSockets 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. HiperSockets 機能の変更点を出力本文から切り離して出力照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では HiperSockets 機能 は「HiperSockets 機能の状態と出力メッセージを結び付ける出力照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では HiperSockets 機能の出力行と DSI633I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では HiperSockets 機能を IBM Z NetViewの確認記録に残し、対象名は出力照合対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Host VTAM messages {#c32-i3454}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Host VTAM messagesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.418) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.418)

??? question "確認問題（1問）"
    **問題.** 条件照合のユーザーズガイド 操作に関係する Host VTAM messagesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件照合の確認値として扱う。 ✅
    - B. Host VTAM messagesの名称と担当者名のみを残して条件照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では Host VTAM messages は「Host VTAM messagesの用途をネットビューの表示で確認する条件照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では IBM Z NetViewの Host VTAM messagesと DSI633I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では Host VTAM messagesを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How AON uses option definition tables {#c32-i3455}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How AON uses option definition tablesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.389) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.389)

??? question "確認問題（1問）"
    **問題.** 記録照合のユーザーズガイド 操作に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録照合の確認記録にまとめる。 ✅
    - B. How 機能の名称と担当者名のみを残して記録照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず記録照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では How 機能 は「How 機能の用途をネットビューの表示で確認する記録照合項目」と AONSTAT または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では IBM Z NetViewの How 機能と EZL000I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では How 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How Commands and Responses Flow {#c32-i3456}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How Commands and Responses Flowは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較照合のユーザーズガイド 操作で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず比較照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較照合の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して比較照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では How 機能 は「比較照合のユーザーズガイド 操作に関係する定義値と表示行を照合する比較照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では How 機能の属性行と DSI633I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では How 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較照合初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### How Data Is Sent to the Z NetView Program {#c32-i3457}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How Data Is Sent to the Z NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序照合のユーザーズガイド 操作でネットビューの運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序照合のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、順序照合の結果として保存する。 ✅
    - D. How 機能の属性行を読まず順序照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では How 機能 は「IBM Z NetViewで How 機能の扱いを記録する順序照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では How 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では How 機能の使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### How Events, Statistics, and Alerts Flow {#c32-i3458}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How Events, Statistics, and Alerts Flowは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域照合のユーザーズガイド 操作に関する How Events 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. How Events 命令の変更点を出力本文から切り離して値域照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、値域照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では How Events 命令 は「How Events 命令の状態と出力メッセージを結び付ける値域照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では How Events 命令の出力行と DSI633I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では How Events 命令を IBM Z NetViewの確認記録に残し、対象名は値域照合対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### How Messages Flow {#c32-i3459}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How Messages Flowは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView (p.290) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.290)

??? question "確認問題（1問）"
    **問題.** 警告照合のユーザーズガイド 操作に関係する How Messages Flowの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告照合として引き継ぐ。 ✅
    - B. How Messages Flowの名称と担当者名のみを残して警告照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では How Messages Flow は「How Messages Flowの用途をネットビューの表示で確認する警告照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では IBM Z NetViewの How Messages Flowと DSI633I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では How Messages Flowを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How programs use AON control file routines {#c32-i3460}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How programs use AON control file routinesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.287) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.287)

??? question "確認問題（1問）"
    **問題.** 復旧照合のユーザーズガイド 操作で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず復旧照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧照合の確認にする。 ✅
    - C. AONSTAT を省略して復旧照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では How 機能 は「復旧照合のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧照合項目」と AONSTAT または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では How 機能の属性行と EZL000I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では How 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### How the NetView Management Console Works {#c32-i3461}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

How the NetView Management Console Worksは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査照合のユーザーズガイド 操作でネットビューの運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査照合のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、監査照合の点検結果を残す。 ✅
    - D. How 機能の属性行を読まず監査照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では How 機能 は「IBM Z NetViewで How 機能の扱いを記録する監査照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では How 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では How 機能の使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Hung Session (Session Monitor) {#c32-i3462}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Hung Session (Session Monitor)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.245) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.245)

??? question "確認問題（1問）"
    **問題.** 構文追跡のユーザーズガイド 操作に関係する Hung Session 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文追跡の確認値として扱う。 ✅
    - B. Hung Session 属性の名称と担当者名のみを残して構文追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では Hung Session 属性 は「Hung Session 属性の用途をネットビューの表示で確認する構文追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では IBM Z NetViewの Hung Session 属性と DSI633I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では Hung Session 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Hung or Looping NetView Tasks (Command Facility) {#c32-i3463}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Hung or Looping NetView Tasks (Command Facility)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更照合のユーザーズガイド 操作に関する Hung 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Hung 機能の変更点を出力本文から切り離して変更照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では Hung 機能 は「Hung 機能の状態と出力メッセージを結び付ける変更照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では Hung 機能の出力行と DSI633I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では Hung 機能を IBM Z NetViewの確認記録に残し、対象名は変更照合対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### IBM Z NetView Components {#c32-i3464}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

IBM Z NetView Componentsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.35) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.35)

??? question "確認問題（1問）"
    **問題.** 展開追跡のユーザーズガイド 操作で IBM 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IBM 機能の出力を取らず展開追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開追跡の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して展開追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では IBM 機能 は「展開追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する展開追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では IBM 機能の属性行と DSI633I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では IBM 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IBM Z NetView Overview {#c32-i3465}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

IBM Z NetView Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.29) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.29)

??? question "確認問題（1問）"
    **問題.** 呼出追跡のユーザーズガイド 操作でネットビューの運用確認を行います。IBM 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を呼出追跡で確認する。 ✅
    - D. IBM 機能の属性行を読まず呼出追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では IBM 機能 は「IBM Z NetViewで IBM 機能の扱いを記録する呼出追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では IBM 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では IBM 機能の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IMS Replication Apply Details Attributes {#c32-i3466}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

IMS Replication Apply Details Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.142) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.142)

??? question "確認問題（1問）"
    **問題.** 値域追跡のユーザーズガイド 操作に関する IMS 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. IMS 機能の変更点を出力本文から切り離して値域追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、値域追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では IMS 機能 は「IMS 機能の状態と出力メッセージを結び付ける値域追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では IMS 機能の出力行と DSI633I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では IMS 機能を IBM Z NetViewの確認記録に残し、対象名は値域追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IMS Replication Capture Details Attributes {#c32-i3467}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

IMS Replication Capture Details Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.143) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.143)

??? question "確認問題（1問）"
    **問題.** 警告追跡のユーザーズガイド 操作に関係する IMS 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告追跡の確認記録にまとめる。 ✅
    - B. IMS 機能の名称と担当者名のみを残して警告追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では IMS 機能 は「IMS 機能の用途をネットビューの表示で確認する警告追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では IBM Z NetViewの IMS 機能と DSI633I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では IMS 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IMS Replication Details Workspace {#c32-i3468}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

IMS Replication Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.79) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.79)

??? question "確認問題（1問）"
    **問題.** 復旧追跡のユーザーズガイド 操作で IMS 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IMS 機能の出力を取らず復旧追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧追跡の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では IMS 機能 は「復旧追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では IMS 機能の属性行と DSI633I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では IMS 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INFORM Action (EZLECALL) {#c32-i3469}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

INFORM Action (EZLECALL)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.320) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.320)

??? question "確認問題（1問）"
    **問題.** 展開検査のユーザーズガイド 操作で INFORM Action 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. INFORM Action 属性の出力を取らず展開検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検査の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して展開検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では INFORM Action 属性 は「展開検査のユーザーズガイド 操作に関係する定義値と表示行を照合する展開検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では INFORM Action 属性の属性行と DSI633I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では INFORM Action 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Identifying Intermittent Problems (Hardware Monitor) {#c32-i3470}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Identifying Intermittent Problems (Hardware Monitor)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.242) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.242)

??? question "確認問題（1問）"
    **問題.** 終端追跡のユーザーズガイド 操作に関係する Identifying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端追跡の確認記録にまとめる。 ✅
    - B. Identifying 機能の名称と担当者名のみを残して終端追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では Identifying 機能 は「Identifying 機能の用途をネットビューの表示で確認する終端追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では IBM Z NetViewの Identifying 機能と DSI633I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では Identifying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IhsLocRes Servlet {#c32-i3471}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

IhsLocRes Servletは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.142) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.142)

??? question "確認問題（1問）"
    **問題.** 探索追跡のユーザーズガイド 操作で IhsLocRes Servletの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IhsLocRes Servletの出力を取らず探索追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索追跡の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して探索追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では IhsLocRes Servlet は「探索追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する探索追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では IhsLocRes Servletの属性行と DSI633I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では IhsLocRes Servletを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IhsRunning Servlet {#c32-i3472}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

IhsRunning Servletは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.143) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.143)

??? question "確認問題（1問）"
    **問題.** 上書追跡のユーザーズガイド 操作でネットビューの運用確認を行います。IhsRunning Servletの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、上書追跡の結果として保存する。 ✅
    - D. IhsRunning Servletの属性行を読まず上書追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では IhsRunning Servlet は「IBM Z NetViewで IhsRunning Servletの扱いを記録する上書追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では IhsRunning Servletの表示結果と DSI633I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では IhsRunning Servletの使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Implementing DDF {#c32-i3473}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Implementing DDFは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先追跡のユーザーズガイド 操作に関する Implementing DDF の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Implementing DDF の変更点を出力本文から切り離して優先追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先追跡で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では Implementing DDF は「Implementing DDF の状態と出力メッセージを結び付ける優先追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では Implementing DDF の出力行と DSI633I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では Implementing DDF を IBM Z NetViewの確認記録に残し、対象名は優先追跡対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementing DDF in a focal point environment {#c32-i3474}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Implementing DDF in a focal point environmentは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録追跡のユーザーズガイド 操作に関係する Implementing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録追跡の確認値として扱う。 ✅
    - B. Implementing 機能の名称と担当者名のみを残して記録追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では Implementing 機能 は「Implementing 機能の用途をネットビューの表示で確認する記録追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では IBM Z NetViewの Implementing 機能と DSI633I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では Implementing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementing Dynamic Display Facility (DDF) {#c32-i3475}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Implementing Dynamic Display Facility (DDF)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較追跡のユーザーズガイド 操作で Implementing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Implementing 機能の出力を取らず比較追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較追跡の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して比較追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では Implementing 機能 は「比較追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する比較追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では Implementing 機能の属性行と DSI633I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では Implementing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementing X.25 Monitoring Support {#c32-i3476}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Implementing X.25 Monitoring Supportは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序追跡のユーザーズガイド 操作でネットビューの運用確認を行います。Implementing X 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を順序追跡で確認する。 ✅
    - D. Implementing X 属性の属性行を読まず順序追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では Implementing X 属性 は「IBM Z NetViewで Implementing X 属性の扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では Implementing X 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では Implementing X 属性の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Implementing an alert through GENALERT {#c32-i3477}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Implementing an alert through GENALERTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲追跡のユーザーズガイド 操作でネットビューの運用確認を行います。Implementing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、範囲追跡の点検結果を残す。 ✅
    - D. Implementing 機能の属性行を読まず範囲追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では Implementing 機能 は「IBM Z NetViewで Implementing 機能の扱いを記録する範囲追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では Implementing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では Implementing 機能の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Inactive TCPIP Connection Count Attributes {#c32-i3478}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Inactive TCPIP Connection Count Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.144) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.144)

??? question "確認問題（1問）"
    **問題.** 監査追跡のユーザーズガイド 操作でネットビューの運用確認を行います。Inactive 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、監査追跡の結果として保存する。 ✅
    - D. Inactive 機能の属性行を読まず監査追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では Inactive 機能 は「IBM Z NetViewで Inactive 機能の扱いを記録する監査追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では Inactive 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では Inactive 機能の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Inactive TCPIP Connection Data Attributes {#c32-i3479}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Inactive TCPIP Connection Data Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.144) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.144)

??? question "確認問題（1問）"
    **問題.** 変更追跡のユーザーズガイド 操作に関する Inactive 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Inactive 機能の変更点を出力本文から切り離して変更追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、変更追跡の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では Inactive 機能 は「Inactive 機能の状態と出力メッセージを結び付ける変更追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では Inactive 機能の出力行と DSI633I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では Inactive 機能を IBM Z NetViewの確認記録に残し、対象名は変更追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Inactive TCPIP Connection Data Workspace {#c32-i3480}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Inactive TCPIP Connection Data Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.54) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.54)

??? question "確認問題（1問）"
    **問題.** 構文検査のユーザーズガイド 操作に関係する Inactive 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文検査として引き継ぐ。 ✅
    - B. Inactive 機能の名称と担当者名のみを残して構文検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では Inactive 機能 は「Inactive 機能の用途をネットビューの表示で確認する構文検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では IBM Z NetViewの Inactive 機能と DSI633I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では Inactive 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide


