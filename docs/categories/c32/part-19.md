---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (19/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > データモデル

### GMFHS Class Reference {#c32-i2710}
*分類: データモデル*  ・  難易度: 中級

GMFHS Class Referenceは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.321 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.321

??? question "確認問題（1問）"
    **問題.** 上書検査のデータモデルでネットビューの運用確認を行います。GMFHS 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず上書検査のデータモデルを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書検査の点検結果を残す。 ✅
    - D. GMFHS 機能の属性行を読まず上書検査のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では GMFHS 機能 は「IBM Z NetViewで GMFHS 機能の扱いを記録する上書検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では GMFHS 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では GMFHS 機能の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.321



### GMFHS Data Model {#c32-i2711}
*分類: データモデル*  ・  難易度: 中級

GMFHS Data Modelは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Data_Model_Reference.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.79

??? question "確認問題（1問）"
    **問題.** 出力検査のデータモデルに関する GMFHS Data Modelの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず出力検査のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のデータモデルの証跡として保存して根拠にする。
    - C. GMFHS Data Modelの変更点を出力本文から切り離して出力検査のデータモデルの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力検査で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では GMFHS Data Model は「GMFHS Data Modelの状態と出力メッセージを結び付ける出力検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では GMFHS Data Modelの出力行と EKG000I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では GMFHS Data Modelを IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.79



### GMFHS Data Model Overview {#c32-i2712}
*分類: データモデル*  ・  難易度: 中級

GMFHS Data Model Overviewは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Data_Model_Reference.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.79

??? question "確認問題（1問）"
    **問題.** 条件検査のデータモデルに関係する GMFHS 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件検査の確認値として扱う。 ✅
    - B. GMFHS 機能の名称と担当者名のみを残して条件検査のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず条件検査のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では GMFHS 機能 は「GMFHS 機能の用途をネットビューの表示で確認する条件検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの GMFHS 機能と EKG000I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では GMFHS 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.79



### GMFHS_Aggregate_NRM_Objects_Class {#c32-i2713}
*分類: データモデル*  ・  難易度: 中級

'GMFHS_Aggregate_NRM_Objects_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切検査のデータモデルで GMFHS_Aggregate_NRM_Objeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. GMFHS_Aggregate_NRM_Objeの出力を取らず区切検査のデータモデルの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切検査の根拠を固定する。 ✅
    - C. RODMVIEW を省略して区切検査のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では GMFHS_Aggregate_NRM_Obje は「区切検査のデータモデルに関係する定義値と表示行を照合する区切検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では GMFHS_Aggregate_NRM_Objeの属性行と EKG000I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では GMFHS_Aggregate_NRM_Objeを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### GMFHS_Aggregate_Objects_Class {#c32-i2714}
*分類: データモデル*  ・  難易度: 中級

GMFHS_Aggregate_Objects_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.23 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.23

??? question "確認問題（1問）"
    **問題.** 範囲検査のデータモデルでネットビューの運用確認を行います。GMFHS_Aggregate_Objects_の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず範囲検査のデータモデルを正常終了として記録する。
    - C. EKG000I を含む表示を保存し、説明欄との差分を範囲検査で確認する。 ✅
    - D. GMFHS_Aggregate_Objects_の属性行を読まず範囲検査のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では GMFHS_Aggregate_Objects_ は「IBM Z NetViewで GMFHS_Aggregate_Objects_の扱いを記録する範囲検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では GMFHS_Aggregate_Objects_の表示結果と EKG000I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では GMFHS_Aggregate_Objects_の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.23



### GMFHS_Displayable_Objects_Parent_Class {#c32-i2715}
*分類: データモデル*  ・  難易度: 中級

'GMFHS_Displayable_Objects_Parent_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先検査のデータモデルに関する GMFHS_Displayable_Objectの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず優先検査のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のデータモデルの証跡として保存して根拠にする。
    - C. GMFHS_Displayable_Objectの変更点を出力本文から切り離して優先検査のデータモデルの承認欄のみ残す。
    - D. RODMVIEW の結果から対象行を抜き出し、優先検査の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では GMFHS_Displayable_Object は「GMFHS_Displayable_Objectの状態と出力メッセージを結び付ける優先検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では GMFHS_Displayable_Objectの出力行と EKG000I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では GMFHS_Displayable_Objectを IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### GMFHS_Managed_Real_NRM_Objects_Class {#c32-i2716}
*分類: データモデル*  ・  難易度: 中級

'GMFHS_Managed_Real_NRM_Objects_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録検査のデータモデルに関係する GMFHS_Managed_Real_NRM_O の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録検査の確認記録にまとめる。 ✅
    - B. GMFHS_Managed_Real_NRM_O の名称と担当者名のみを残して記録検査のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず記録検査のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では GMFHS_Managed_Real_NRM_O は「GMFHS_Managed_Real_NRM_O の用途をネットビューの表示で確認する記録検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの GMFHS_Managed_Real_NRM_O と EKG000I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では GMFHS_Managed_Real_NRM_O を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### GMFHS_Managed_Real_Objects_Class {#c32-i2717}
*分類: データモデル*  ・  難易度: 中級

GMFHS_Managed_Real_Objects_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.23 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.23

??? question "確認問題（1問）"
    **問題.** 比較検査のデータモデルで GMFHS_Managed_Real_Objecの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. GMFHS_Managed_Real_Objecの出力を取らず比較検査のデータモデルの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較検査の根拠にする。 ✅
    - C. RODMVIEW を省略して比較検査のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では GMFHS_Managed_Real_Objec は「比較検査のデータモデルに関係する定義値と表示行を照合する比較検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では GMFHS_Managed_Real_Objecの属性行と EKG000I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では GMFHS_Managed_Real_Objecを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.23



### GMFHS_Monitorable_Objects_Parent_Class {#c32-i2718}
*分類: データモデル*  ・  難易度: 中級

'GMFHS_Monitorable_Objects_Parent_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検査のデータモデルでネットビューの運用確認を行います。GMFHS_Monitorable_Objectの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず順序検査のデータモデルを正常終了として記録する。
    - C. 同じ画面で対象行と EKG000I を読み、順序検査の結果として保存する。 ✅
    - D. GMFHS_Monitorable_Objectの属性行を読まず順序検査のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では GMFHS_Monitorable_Object は「IBM Z NetViewで GMFHS_Monitorable_Objectの扱いを記録する順序検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では GMFHS_Monitorable_Objectの表示結果と EKG000I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では GMFHS_Monitorable_Objectの使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### GMFHS_Real_Objects_Class {#c32-i2719}
*分類: データモデル*  ・  難易度: 中級

'GMFHS_Real_Objects_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域検査のデータモデルに関する GMFHS_Real_Objects_Classの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず値域検査のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のデータモデルの証跡として保存して根拠にする。
    - C. GMFHS_Real_Objects_Classの変更点を出力本文から切り離して値域検査のデータモデルの承認欄のみ残す。
    - D. RODMVIEW で得た表示本文を使い、値域検査の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では GMFHS_Real_Objects_Class は「GMFHS_Real_Objects_Classの状態と出力メッセージを結び付ける値域検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では GMFHS_Real_Objects_Classの出力行と EKG000I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では GMFHS_Real_Objects_Classを IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### GMFHS_Shadow_Objects_Class {#c32-i2720}
*分類: データモデル*  ・  難易度: 中級

'GMFHS_Shadow_Objects_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告検査のデータモデルに関係する GMFHS_Shadow_Objects_Claの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告検査として引き継ぐ。 ✅
    - B. GMFHS_Shadow_Objects_Claの名称と担当者名のみを残して警告検査のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず警告検査のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では GMFHS_Shadow_Objects_Cla は「GMFHS_Shadow_Objects_Claの用途をネットビューの表示で確認する警告検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの GMFHS_Shadow_Objects_Claと EKG000I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では GMFHS_Shadow_Objects_Claを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Global_Aggregation_Parameters_Class {#c32-i2721}
*分類: データモデル*  ・  難易度: 中級

'Global_Aggregation_Parameters_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端検査のデータモデルに関係する Global_Aggregation_Paramの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端検査として引き継ぐ。 ✅
    - B. Global_Aggregation_Paramの名称と担当者名のみを残して終端検査のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Global_Aggregation_Param は「Global_Aggregation_Paramの用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの Global_Aggregation_Paramと DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Global_Aggregation_Paramを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Global_NLS_Parameters_Class {#c32-i2722}
*分類: データモデル*  ・  難易度: 中級

'Global_NLS_Parameters_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検査のデータモデルで Global_NLS_Parameters_Clの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Global_NLS_Parameters_Clの出力を取らず探索検査のデータモデルの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索検査の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して探索検査のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では Global_NLS_Parameters_Cl は「探索検査のデータモデルに関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では Global_NLS_Parameters_Clの属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では Global_NLS_Parameters_Clを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Host Resources {#c32-i2723}
*分類: データモデル*  ・  難易度: 中級

Host Resourcesは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 復旧検査のデータモデルで Host Resourcesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Host Resourcesの出力を取らず復旧検査のデータモデルの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧検査の確認にする。 ✅
    - C. RODMVIEW を省略して復旧検査のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では Host Resources は「復旧検査のデータモデルに関係する定義値と表示行を照合する復旧検査項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では Host Resourcesの属性行と EKG000I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では Host Resourcesを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### How the NetView Data Models Work Together {#c32-i2724}
*分類: データモデル*  ・  難易度: 中級

How the NetView Data Models Work Togetherは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査検査のデータモデルでネットビューの運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査のデータモデルを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査のデータモデルを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、監査検査の点検結果を残す。 ✅
    - D. How 機能の属性行を読まず監査検査のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では How 機能 は「IBM Z NetViewで How 機能の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では How 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では How 機能の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Icon Cross-Reference {#c32-i2725}
*分類: データモデル*  ・  難易度: 中級

Icon Cross-Referenceは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.321 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.321

??? question "確認問題（1問）"
    **問題.** 変更検査のデータモデルに関する Icon 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のデータモデルの証跡として保存して根拠にする。
    - C. Icon 機能の変更点を出力本文から切り離して変更検査のデータモデルの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更検査で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では Icon 機能 は「Icon 機能の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では Icon 機能の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では Icon 機能を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.321



### Layout_Parameters_For_Object_Class {#c32-i2726}
*分類: データモデル*  ・  難易度: 中級

Layout_Parameters_For_Object_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 構文判定のデータモデルに関係する Layout_Parameters_For_Obの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文判定の確認値として扱う。 ✅
    - B. Layout_Parameters_For_Obの名称と担当者名のみを残して構文判定のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では Layout_Parameters_For_Ob は「Layout_Parameters_For_Obの用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの Layout_Parameters_For_Obと DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では Layout_Parameters_For_Obを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### Layout_Parameters_For_View_Class {#c32-i2727}
*分類: データモデル*  ・  難易度: 中級

Layout_Parameters_For_View_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 展開判定のデータモデルで Layout_Parameters_For_Viの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Layout_Parameters_For_Viの出力を取らず展開判定のデータモデルの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開判定の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して展開判定のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では Layout_Parameters_For_Vi は「展開判定のデータモデルに関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では Layout_Parameters_For_Viの属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では Layout_Parameters_For_Viを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### Link Resources {#c32-i2728}
*分類: データモデル*  ・  難易度: 中級

Link Resourcesは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 呼出判定のデータモデルでネットビューの運用確認を行います。Link Resourcesの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず呼出判定のデータモデルを正常終了として記録する。
    - C. EKG000I を含む表示を保存し、説明欄との差分を呼出判定で確認する。 ✅
    - D. Link Resourcesの属性行を読まず呼出判定のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では Link Resources は「IBM Z NetViewで Link Resourcesの扱いを記録する呼出判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では Link Resourcesの表示結果と EKG000I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では Link Resourcesの使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### More Detail View Classes {#c32-i2729}
*分類: データモデル*  ・  難易度: 中級

More Detail View Classesは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.126 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.126

??? question "確認問題（1問）"
    **問題.** 置換判定のデータモデルに関する More 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず置換判定のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のデータモデルの証跡として保存して根拠にする。
    - C. More 機能の変更点を出力本文から切り離して置換判定のデータモデルの承認欄のみ残す。
    - D. RODMVIEW の結果から対象行を抜き出し、置換判定の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では More 機能 は「More 機能の状態と出力メッセージを結び付ける置換判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では More 機能の出力行と EKG000I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では More 機能を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.126



### More_Detail_Logical_View_Class {#c32-i2730}
*分類: データモデル*  ・  難易度: 中級

'More_Detail_Logical_View_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端判定のデータモデルに関係する More_Detail_Logical_Viewの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端判定の確認記録にまとめる。 ✅
    - B. More_Detail_Logical_Viewの名称と担当者名のみを残して終端判定のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では More_Detail_Logical_View は「More_Detail_Logical_Viewの用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの More_Detail_Logical_Viewと DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では More_Detail_Logical_Viewを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### More_Detail_Physical_View_Class {#c32-i2731}
*分類: データモデル*  ・  難易度: 中級

'More_Detail_Physical_View_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索判定のデータモデルで More_Detail_Physical_Vieの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. More_Detail_Physical_Vieの出力を取らず探索判定のデータモデルの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索判定の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して探索判定のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では More_Detail_Physical_Vie は「探索判定のデータモデルに関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では More_Detail_Physical_Vieの属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では More_Detail_Physical_Vieを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### NMG_Class {#c32-i2732}
*分類: データモデル*  ・  難易度: 中級

NMG_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Troubleshooting_Guide.pdf p.209 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.209

??? question "確認問題（1問）"
    **問題.** 範囲判定のデータモデルでネットビューの運用確認を行います。NMG_Classの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定のデータモデルを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定のデータモデルを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、範囲判定の点検結果を残す。 ✅
    - D. NMG_Classの属性行を読まず範囲判定のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では NMG_Class は「IBM Z NetViewで NMG_Classの扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では NMG_Classの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では NMG_Classの使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.209



### Name_Space_Parent_Class {#c32-i2733}
*分類: データモデル*  ・  難易度: 中級

Name_Space_Parent_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.68 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.68

??? question "確認問題（1問）"
    **問題.** 上書判定のデータモデルでネットビューの運用確認を行います。Name_Space_Parent_Classの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定のデータモデルを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定のデータモデルを正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、上書判定の結果として保存する。 ✅
    - D. Name_Space_Parent_Classの属性行を読まず上書判定のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では Name_Space_Parent_Class は「IBM Z NetViewで Name_Space_Parent_Classの扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では Name_Space_Parent_Classの表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では Name_Space_Parent_Classの使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.68



### NetView Data Model Field Reference {#c32-i2734}
*分類: データモデル*  ・  難易度: 中級

NetView Data Model Field Referenceは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Data_Model_Reference.pdf p.307 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.307

??? question "確認問題（1問）"
    **問題.** 出力判定のデータモデルに関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力判定のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定のデータモデルの証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して出力判定のデータモデルの承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、出力判定の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける出力判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.307



### Network_View_Class {#c32-i2735}
*分類: データモデル*  ・  難易度: 中級

Network_View_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.35_v2 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.35_v2

??? question "確認問題（1問）"
    **問題.** 条件判定のデータモデルに関係する Network_View_Classの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件判定として引き継ぐ。 ✅
    - B. Network_View_Classの名称と担当者名のみを残して条件判定のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Network_View_Class は「Network_View_Classの用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの Network_View_Classと DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Network_View_Classを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.35_v2



### Network_View_Collection_Class {#c32-i2736}
*分類: データモデル*  ・  難易度: 中級

Network_View_Collection_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.68 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.68

??? question "確認問題（1問）"
    **問題.** 区切判定のデータモデルで Network_View_Collection_の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Network_View_Collection_の出力を取らず区切判定のデータモデルの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切判定の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して区切判定のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Network_View_Collection_ は「区切判定のデータモデルに関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Network_View_Collection_の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Network_View_Collection_を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.68



### Node Resources {#c32-i2737}
*分類: データモデル*  ・  難易度: 中級

Node Resourcesは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 優先判定のデータモデルに関する Node Resourcesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず優先判定のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定のデータモデルの証跡として保存して根拠にする。
    - C. Node Resourcesの変更点を出力本文から切り離して優先判定のデータモデルの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先判定で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では Node Resources は「Node Resourcesの状態と出力メッセージを結び付ける優先判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では Node Resourcesの出力行と EKG000I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では Node Resourcesを IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### Non_SNA_Domain_Class {#c32-i2738}
*分類: データモデル*  ・  難易度: 中級

'Non_SNA_Domain_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録判定のデータモデルに関係する Non_SNA_Domain_Classの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録判定の確認値として扱う。 ✅
    - B. Non_SNA_Domain_Classの名称と担当者名のみを残して記録判定のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では Non_SNA_Domain_Class は「Non_SNA_Domain_Classの用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewの Non_SNA_Domain_Classと DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では Non_SNA_Domain_Classを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Null_Objects_Class {#c32-i2739}
*分類: データモデル*  ・  難易度: 中級

Null_Objects_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 比較判定のデータモデルで Null_Objects_Classの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Null_Objects_Classの出力を取らず比較判定のデータモデルの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較判定の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して比較判定のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Null_Objects_Class は「比較判定のデータモデルに関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Null_Objects_Classの属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Null_Objects_Classを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### Package Names {#c32-i2740}
*分類: データモデル*  ・  難易度: 中級

Package Namesは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196

??? question "確認問題（1問）"
    **問題.** 順序判定のデータモデルでネットビューの運用確認を行います。Package Namesの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず順序判定のデータモデルを正常終了として記録する。
    - C. EKG000I を含む表示を保存し、説明欄との差分を順序判定で確認する。 ✅
    - D. Package Namesの属性行を読まず順序判定のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では Package Names は「IBM Z NetViewで Package Namesの扱いを記録する順序判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では Package Namesの表示結果と EKG000I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では Package Namesの使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196



### Presentation_Services_Global_Parameters_Class {#c32-i2741}
*分類: データモデル*  ・  難易度: 中級

Presentation_Services_Global_Parameters_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 値域判定のデータモデルに関する Presentation_Services_Glの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定のデータモデルの証跡として保存して根拠にする。
    - C. Presentation_Services_Glの変更点を出力本文から切り離して値域判定のデータモデルの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、値域判定の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では Presentation_Services_Gl は「Presentation_Services_Glの状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では Presentation_Services_Glの出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では Presentation_Services_Glを IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### Presentation_Services_Parent_Class {#c32-i2742}
*分類: データモデル*  ・  難易度: 中級

Presentation_Services_Parent_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 警告判定のデータモデルに関係する Presentation_Services_Paの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告判定の確認記録にまとめる。 ✅
    - B. Presentation_Services_Paの名称と担当者名のみを残して警告判定のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では Presentation_Services_Pa は「Presentation_Services_Paの用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewの Presentation_Services_Paと DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では Presentation_Services_Paを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### SELFDEFINING {#c32-i2743}
*分類: データモデル*  ・  難易度: 中級

SELFDEFININGは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 復旧判定のデータモデルで SELFDEFINING の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SELFDEFINING の出力を取らず復旧判定のデータモデルの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧判定の根拠にする。 ✅
    - C. RODMVIEW を省略して復旧判定のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では SELFDEFINING は「復旧判定のデータモデルに関係する定義値と表示行を照合する復旧判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では SELFDEFINING の属性行と EKG000I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では SELFDEFINING を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (1) {#c32-i2744}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (1)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 監査判定のデータモデルでネットビューの運用確認を行います。SELFDEFINING (1)の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず監査判定のデータモデルを正常終了として記録する。
    - C. 同じ画面で対象行と EKG000I を読み、監査判定の結果として保存する。 ✅
    - D. SELFDEFINING (1)の属性行を読まず監査判定のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では SELFDEFINING (1) は「IBM Z NetViewで SELFDEFINING (1)の扱いを記録する監査判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では SELFDEFINING (1)の表示結果と EKG000I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では SELFDEFINING (1)の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (10) {#c32-i2745}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (10)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 変更判定のデータモデルに関する SELFDEFINING (10)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず変更判定のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定のデータモデルの証跡として保存して根拠にする。
    - C. SELFDEFINING (10)の変更点を出力本文から切り離して変更判定のデータモデルの承認欄のみ残す。
    - D. RODMVIEW で得た表示本文を使い、変更判定の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では SELFDEFINING (10) は「SELFDEFINING (10)の状態と出力メッセージを結び付ける変更判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では SELFDEFINING (10)の出力行と EKG000I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では SELFDEFINING (10)を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (11) {#c32-i2746}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (11)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 構文整理のデータモデルに関係する SELFDEFINING (11)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文整理として引き継ぐ。 ✅
    - B. SELFDEFINING (11)の名称と担当者名のみを残して構文整理のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず構文整理のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では SELFDEFINING (11) は「SELFDEFINING (11)の用途をネットビューの表示で確認する構文整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの SELFDEFINING (11)と EKG000I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では SELFDEFINING (11)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (12) {#c32-i2747}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (12)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 展開整理のデータモデルで SELFDEFINING (12)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SELFDEFINING (12)の出力を取らず展開整理のデータモデルの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開整理の確認にする。 ✅
    - C. RODMVIEW を省略して展開整理のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では SELFDEFINING (12) は「展開整理のデータモデルに関係する定義値と表示行を照合する展開整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では SELFDEFINING (12)の属性行と EKG000I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では SELFDEFINING (12)を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (13) {#c32-i2748}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (13)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 呼出整理のデータモデルでネットビューの運用確認を行います。SELFDEFINING (13)の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず呼出整理のデータモデルを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、呼出整理の点検結果を残す。 ✅
    - D. SELFDEFINING (13)の属性行を読まず呼出整理のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では SELFDEFINING (13) は「IBM Z NetViewで SELFDEFINING (13)の扱いを記録する呼出整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では SELFDEFINING (13)の表示結果と EKG000I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では SELFDEFINING (13)の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (14) {#c32-i2749}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (14)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 置換整理のデータモデルに関する SELFDEFINING (14)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず置換整理のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理のデータモデルの証跡として保存して根拠にする。
    - C. SELFDEFINING (14)の変更点を出力本文から切り離して置換整理のデータモデルの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換整理で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では SELFDEFINING (14) は「SELFDEFINING (14)の状態と出力メッセージを結び付ける置換整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では SELFDEFINING (14)の出力行と EKG000I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では SELFDEFINING (14)を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (15) {#c32-i2750}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (15)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 終端整理のデータモデルに関係する SELFDEFINING (15)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端整理の確認値として扱う。 ✅
    - B. SELFDEFINING (15)の名称と担当者名のみを残して終端整理のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず終端整理のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では SELFDEFINING (15) は「SELFDEFINING (15)の用途をネットビューの表示で確認する終端整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの SELFDEFINING (15)と EKG000I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では SELFDEFINING (15)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (2) {#c32-i2751}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (2)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 探索整理のデータモデルで SELFDEFINING (2)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SELFDEFINING (2)の出力を取らず探索整理のデータモデルの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索整理の根拠を固定する。 ✅
    - C. RODMVIEW を省略して探索整理のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では SELFDEFINING (2) は「探索整理のデータモデルに関係する定義値と表示行を照合する探索整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では SELFDEFINING (2)の属性行と EKG000I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では SELFDEFINING (2)を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (3) {#c32-i2752}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (3)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 上書整理のデータモデルでネットビューの運用確認を行います。SELFDEFINING (3)の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず上書整理のデータモデルを正常終了として記録する。
    - C. EKG000I を含む表示を保存し、説明欄との差分を上書整理で確認する。 ✅
    - D. SELFDEFINING (3)の属性行を読まず上書整理のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では SELFDEFINING (3) は「IBM Z NetViewで SELFDEFINING (3)の扱いを記録する上書整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では SELFDEFINING (3)の表示結果と EKG000I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では SELFDEFINING (3)の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (4) {#c32-i2753}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (4)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 出力整理のデータモデルに関する SELFDEFINING (4)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず出力整理のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理のデータモデルの証跡として保存して根拠にする。
    - C. SELFDEFINING (4)の変更点を出力本文から切り離して出力整理のデータモデルの承認欄のみ残す。
    - D. RODMVIEW の結果から対象行を抜き出し、出力整理の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では SELFDEFINING (4) は「SELFDEFINING (4)の状態と出力メッセージを結び付ける出力整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では SELFDEFINING (4)の出力行と EKG000I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では SELFDEFINING (4)を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (5) {#c32-i2754}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (5)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 条件整理のデータモデルに関係する SELFDEFINING (5)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件整理の確認記録にまとめる。 ✅
    - B. SELFDEFINING (5)の名称と担当者名のみを残して条件整理のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず条件整理のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では SELFDEFINING (5) は「SELFDEFINING (5)の用途をネットビューの表示で確認する条件整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの SELFDEFINING (5)と EKG000I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では SELFDEFINING (5)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (6) {#c32-i2755}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (6)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 区切整理のデータモデルで SELFDEFINING (6)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SELFDEFINING (6)の出力を取らず区切整理のデータモデルの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切整理の根拠にする。 ✅
    - C. RODMVIEW を省略して区切整理のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では SELFDEFINING (6) は「区切整理のデータモデルに関係する定義値と表示行を照合する区切整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では SELFDEFINING (6)の属性行と EKG000I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では SELFDEFINING (6)を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (7) {#c32-i2756}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (7)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 範囲整理のデータモデルでネットビューの運用確認を行います。SELFDEFINING (7)の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理のデータモデルを確認した扱いにする。
    - B. EKG000I の有無を確認せず範囲整理のデータモデルを正常終了として記録する。
    - C. 同じ画面で対象行と EKG000I を読み、範囲整理の結果として保存する。 ✅
    - D. SELFDEFINING (7)の属性行を読まず範囲整理のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では SELFDEFINING (7) は「IBM Z NetViewで SELFDEFINING (7)の扱いを記録する範囲整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では SELFDEFINING (7)の表示結果と EKG000I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では SELFDEFINING (7)の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (8) {#c32-i2757}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (8)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 優先整理のデータモデルに関する SELFDEFINING (8)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず優先整理のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理のデータモデルの証跡として保存して根拠にする。
    - C. SELFDEFINING (8)の変更点を出力本文から切り離して優先整理のデータモデルの承認欄のみ残す。
    - D. RODMVIEW で得た表示本文を使い、優先整理の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では SELFDEFINING (8) は「SELFDEFINING (8)の状態と出力メッセージを結び付ける優先整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では SELFDEFINING (8)の出力行と EKG000I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では SELFDEFINING (8)を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SELFDEFINING (9) {#c32-i2758}
*分類: データモデル*  ・  難易度: 中級

SELFDEFINING (9)は、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220

??? question "確認問題（1問）"
    **問題.** 記録整理のデータモデルに関係する SELFDEFINING (9)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録整理として引き継ぐ。 ✅
    - B. SELFDEFINING (9)の名称と担当者名のみを残して記録整理のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず記録整理のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では SELFDEFINING (9) は「SELFDEFINING (9)の用途をネットビューの表示で確認する記録整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの SELFDEFINING (9)と EKG000I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では SELFDEFINING (9)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.220



### SNA_Domain_Class {#c32-i2759}
*分類: データモデル*  ・  難易度: 中級

'SNA_Domain_Class' (Lv2: データモデル) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較整理のデータモデルで SNA_Domain_Classの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SNA_Domain_Classの出力を取らず比較整理のデータモデルの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較整理の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して比較整理のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では SNA_Domain_Class は「比較整理のデータモデルに関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では SNA_Domain_Classの属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では SNA_Domain_Classを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### System Defined Classes and Fields {#c32-i2760}
*分類: データモデル*  ・  難易度: 中級

System Defined Classes and Fieldsは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序整理のデータモデルでネットビューの運用確認を行います。System 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理のデータモデルを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理のデータモデルを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、順序整理の点検結果を残す。 ✅
    - D. System 機能の属性行を読まず順序整理のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では System 機能 は「IBM Z NetViewで System 機能の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では System 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では System 機能の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Terminal Resources {#c32-i2761}
*分類: データモデル*  ・  難易度: 中級

Terminal Resourcesは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 値域整理のデータモデルに関する Terminal Resourcesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず値域整理のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理のデータモデルの証跡として保存して根拠にする。
    - C. Terminal Resourcesの変更点を出力本文から切り離して値域整理のデータモデルの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域整理で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Terminal Resources は「Terminal Resourcesの状態と出力メッセージを結び付ける値域整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Terminal Resourcesの出力行と EKG000I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Terminal Resourcesを IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### Topology_Manager Class {#c32-i2762}
*分類: データモデル*  ・  難易度: 中級

Topology_Manager Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196

??? question "確認問題（1問）"
    **問題.** 警告整理のデータモデルに関係する Topology_Manager 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告整理の確認値として扱う。 ✅
    - B. Topology_Manager 機能の名称と担当者名のみを残して警告整理のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず警告整理のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Topology_Manager 機能 は「Topology_Manager 機能の用途をネットビューの表示で確認する警告整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの Topology_Manager 機能と EKG000I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Topology_Manager 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196



### Transceiver Resources {#c32-i2763}
*分類: データモデル*  ・  難易度: 中級

Transceiver Resourcesは、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103

??? question "確認問題（1問）"
    **問題.** 復旧整理のデータモデルで Transceiver 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Transceiver 機能の出力を取らず復旧整理のデータモデルの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧整理の根拠を固定する。 ✅
    - C. RODMVIEW を省略して復旧整理のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Transceiver 機能 は「復旧整理のデータモデルに関係する定義値と表示行を照合する復旧整理項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Transceiver 機能の属性行と EKG000I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Transceiver 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.103



### UniversalClass {#c32-i2764}
*分類: データモデル*  ・  難易度: 中級

UniversalClassは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.79

??? question "確認問題（1問）"
    **問題.** 監査整理のデータモデルでネットビューの運用確認を行います。UniversalClassの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理のデータモデルを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理のデータモデルを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を監査整理で確認する。 ✅
    - D. UniversalClassの属性行を読まず監査整理のデータモデルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では UniversalClass は「IBM Z NetViewで UniversalClassの扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では UniversalClassの表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では UniversalClassの使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.79



### View_Information_Object_Class {#c32-i2765}
*分類: データモデル*  ・  難易度: 中級

View_Information_Object_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 変更整理のデータモデルに関する View_Information_Object_の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理のデータモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理のデータモデルの証跡として保存して根拠にする。
    - C. View_Information_Object_の変更点を出力本文から切り離して変更整理のデータモデルの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更整理の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では View_Information_Object_ は「View_Information_Object_の状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では View_Information_Object_の出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では View_Information_Object_を IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### View_Information_Reference_Class {#c32-i2766}
*分類: データモデル*  ・  難易度: 中級

View_Information_Reference_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.537 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.537

??? question "確認問題（1問）"
    **問題.** 構文記録のデータモデルに関係する View_Information_Referenの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文記録の確認記録にまとめる。 ✅
    - B. View_Information_Referenの名称と担当者名のみを残して構文記録のデータモデルの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録のデータモデルを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録のデータモデルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では View_Information_Referen は「View_Information_Referenの用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの View_Information_Referenと DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では View_Information_Referenを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.537



### View_Parent_Class {#c32-i2767}
*分類: データモデル*  ・  難易度: 中級

View_Parent_Classは、Tivoli NetView z/OS 自動化のデータモデルで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.76 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.76

??? question "確認問題（1問）"
    **問題.** 展開記録のデータモデルで View_Parent_Classの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. View_Parent_Classの出力を取らず展開記録のデータモデルの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開記録の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して展開記録のデータモデルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録のデータモデルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では View_Parent_Class は「展開記録のデータモデルに関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では View_Parent_Classの属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では View_Parent_Classを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.76



### What Is a Data Model? {#c32-i2768}
*分類: データモデル*  ・  難易度: 中級

What Is a Data Model?は、Tivoli NetView z/OS 自動化のデータモデルでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出記録の?でネットビューの運用確認を行います。What 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録の?を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録の?を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、呼出記録の結果として保存する。 ✅
    - D. What 機能の属性行を読まず呼出記録の?の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では What 機能 は「IBM Z NetViewで What 機能の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では What 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では What 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > トラブルシューティング

### A GDPS Continuous Availability solution workspace has no data {#c32-i2769}
*分類: トラブルシューティング*  ・  難易度: 上級

A GDPS Continuous Availability solution workspace has no dataは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端記録のトラブルシューティングに関係する A 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端記録として引き継ぐ。 ✅
    - B. A 機能の名称と担当者名のみを残して終端記録のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では A 機能 は「A 機能の用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの A 機能と DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では A 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### A NetView operator cannot browse archived data {#c32-i2770}
*分類: トラブルシューティング*  ・  難易度: 中級

A NetView operator cannot browse archived dataは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書記録のトラブルシューティングでネットビューの運用確認を行います。A 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書記録の点検結果を残す。 ✅
    - D. A 機能の属性行を読まず上書記録のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では A 機能 は「IBM Z NetViewで A 機能の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では A 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では A 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### A command issued with DOMAIN=ALL from a sysplex master NetView program returns incomplete data {#c32-i2771}
*分類: トラブルシューティング*  ・  難易度: 中級

A command issued with DOMAIN=ALL from a sysplex master NetView program returns incomplete dataは、Tivoli NetView z/OS 自動化のトラブルシューティングで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### A message is incorrectly cached {#c32-i2772}
*分類: トラブルシューティング*  ・  難易度: 中級

A message is incorrectly cachedは、Tivoli NetView z/OS 自動化のトラブルシューティングでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索記録のトラブルシューティングで A 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. A 機能の出力を取らず探索記録のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索記録の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して探索記録のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では A 機能 は「探索記録のトラブルシューティングに関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では A 機能の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では A 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### A service does not complete initialization {#c32-i2773}
*分類: トラブルシューティング*  ・  難易度: 中級

A service does not complete initializationは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力記録のトラブルシューティングに関する A 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録のトラブルシューティングの証跡として保存して根拠にする。
    - C. A 機能の変更点を出力本文から切り離して出力記録のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力記録で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では A 機能 は「A 機能の状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では A 機能の出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では A 機能を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### AON and NetView initialization {#c32-i2774}
*分類: トラブルシューティング*  ・  難易度: 中級

'AON and NetView initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.31

??? question "確認問題（1問）"
    **問題.** 上書分離のトラブルシューティングでネットビューの運用確認を行います。AON 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離のトラブルシューティングを確認した扱いにする。
    - B. EZL000I の有無を確認せず上書分離のトラブルシューティングを正常終了として記録する。
    - C. 同じ画面で対象行と EZL000I を読み、上書分離の結果として保存する。 ✅
    - D. AON 機能の属性行を読まず上書分離のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では AON 機能 は「IBM Z NetViewで AON 機能の扱いを記録する上書分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では AON 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では AON 機能の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.31



### AON automation routines {#c32-i2775}
*分類: トラブルシューティング*  ・  難易度: 上級

'AON automation routines' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 出力分離のトラブルシューティングに関する AON 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. AONSTAT の結果を残さず出力分離のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離のトラブルシューティングの証跡として保存して根拠にする。
    - C. AON 機能の変更点を出力本文から切り離して出力分離のトラブルシューティングの承認欄のみ残す。
    - D. AONSTAT で得た表示本文を使い、出力分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では AON 機能 は「AON 機能の状態と出力メッセージを結び付ける出力分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では AON 機能の出力行と EZL000I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では AON 機能を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### AON problem worksheet {#c32-i2776}
*分類: トラブルシューティング*  ・  難易度: 中級

'AON problem worksheet' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 条件分離のトラブルシューティングに関係する AON 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件分離として引き継ぐ。 ✅
    - B. AON 機能の名称と担当者名のみを残して条件分離のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件分離のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず条件分離のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では AON 機能 は「AON 機能の用途をネットビューの表示で確認する条件分離項目」と AONSTAT または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM Z NetViewの AON 機能と EZL000I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では AON 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### Abend 0C8 is received at RODM initialization {#c32-i2777}
*分類: トラブルシューティング*  ・  難易度: 上級

'Abend 0C8 is received at RODM initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196

??? question "確認問題（1問）"
    **問題.** 条件記録のトラブルシューティングに関係する Abend 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件記録の確認値として扱う。 ✅
    - B. Abend 機能の名称と担当者名のみを残して条件記録のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず条件記録のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Abend 機能 は「Abend 機能の用途をネットビューの表示で確認する条件記録項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの Abend 機能と EKG000I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Abend 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.196



### Abend 301 is received {#c32-i2778}
*分類: トラブルシューティング*  ・  難易度: 上級

'Abend 301 is received' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 区切記録のトラブルシューティングで Abend 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Abend 機能の出力を取らず区切記録のトラブルシューティングの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切記録の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して区切記録のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Abend 機能 は「区切記録のトラブルシューティングに関係する定義値と表示行を照合する区切記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Abend 機能の属性行と DSI633I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Abend 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### Abend 9C5 is received {#c32-i2779}
*分類: トラブルシューティング*  ・  難易度: 上級

'Abend 9C5 is received' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 範囲記録のトラブルシューティングでネットビューの運用確認を行います。Abend 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録のトラブルシューティングを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を範囲記録で確認する。 ✅
    - D. Abend 機能の属性行を読まず範囲記録のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Abend 機能 は「IBM Z NetViewで Abend 機能の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Abend 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Abend 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### Abend A78 received at task or NetView termination {#c32-i2780}
*分類: トラブルシューティング*  ・  難易度: 上級

Abend A78 received at task or NetView terminationは、Tivoli NetView z/OS 自動化のトラブルシューティングでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先記録のトラブルシューティングに関する Abend 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先記録のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録のトラブルシューティングの証跡として保存して根拠にする。
    - C. Abend 機能の変更点を出力本文から切り離して優先記録のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、優先記録の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Abend 機能 は「Abend 機能の状態と出力メッセージを結び付ける優先記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Abend 機能の出力行と DSI633I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Abend 機能を IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Abend U0258, U0268, or U0269 is received {#c32-i2781}
*分類: トラブルシューティング*  ・  難易度: 上級

Abend U0258, U0268, or U0269 is receivedは、Tivoli NetView z/OS 自動化のトラブルシューティングでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較記録のトラブルシューティングで Abend U0258 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Abend U0258 命令の出力を取らず比較記録のトラブルシューティングの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較記録の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して比較記録のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Abend U0258 命令 は「比較記録のトラブルシューティングに関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Abend U0258 命令の属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Abend U0258 命令を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Abend code (0C4 or other) or unexpected results occurred during delinearization {#c32-i2782}
*分類: トラブルシューティング*  ・  難易度: 上級

Abend code (0C4 or other) or unexpected results occurred during delinearizationは、Tivoli NetView z/OS 自動化のトラブルシューティングでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録記録のトラブルシューティングに関係する Abend code 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録記録の確認記録にまとめる。 ✅
    - B. Abend code 属性の名称と担当者名のみを残して記録記録のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Abend code 属性 は「Abend code 属性の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの Abend code 属性と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Abend code 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Abnormal reaction from RODM {#c32-i2783}
*分類: トラブルシューティング*  ・  難易度: 中級

'Abnormal reaction from RODM' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 順序記録のトラブルシューティングでネットビューの運用確認を行います。Abnormal 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録のトラブルシューティングを確認した扱いにする。
    - B. EKG000I の有無を確認せず順序記録のトラブルシューティングを正常終了として記録する。
    - C. 同じ画面で対象行と EKG000I を読み、順序記録の結果として保存する。 ✅
    - D. Abnormal 機能の属性行を読まず順序記録のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Abnormal 機能 は「IBM Z NetViewで Abnormal 機能の扱いを記録する順序記録項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Abnormal 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Abnormal 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### Active/Active Sites subnode is not displayed in the physical Navigator view {#c32-i2784}
*分類: トラブルシューティング*  ・  難易度: 中級

Active/Active Sites subnode is not displayed in the physical Navigator viewは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として Active/Active Sites subnode  を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正解はDです。構文照合保守で扱う Active/Active Sites subnode  は Tivoli NetView z/OS 自動化 の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として Active/Active Sites subnode  を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Additional support information {#c32-i2785}
*分類: トラブルシューティング*  ・  難易度: 中級

'Additional support information' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Security_Reference.pdf p.145

??? question "確認問題（1問）"
    **問題.** 警告記録のトラブルシューティングに関係する Additional 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告記録として引き継ぐ。 ✅
    - B. Additional 機能の名称と担当者名のみを残して警告記録のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Additional 機能 は「Additional 機能の用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの Additional 機能と DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Additional 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Security_Reference.pdf p.145



### Alert adapter fails to initialize {#c32-i2786}
*分類: トラブルシューティング*  ・  難易度: 中級

Alert adapter fails to initializeは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧記録のトラブルシューティングで Alert 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Alert 機能の出力を取らず復旧記録のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧記録の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Alert 機能 は「復旧記録のトラブルシューティングに関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Alert 機能の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Alert 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Alert adapter service information {#c32-i2787}
*分類: トラブルシューティング*  ・  難易度: 中級

'Alert adapter service information' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView.pdf p.127

??? question "確認問題（1問）"
    **問題.** 監査記録のトラブルシューティングでネットビューの運用確認を行います。Alert 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、監査記録の点検結果を残す。 ✅
    - D. Alert 機能の属性行を読まず監査記録のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Alert 機能 は「IBM Z NetViewで Alert 機能の扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Alert 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Alert 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Users_Guide_NetView.pdf p.127



### Alert and Alert History problems {#c32-i2788}
*分類: トラブルシューティング*  ・  難易度: 中級

Alert and Alert History problemsは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更記録のトラブルシューティングに関する Alert 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録のトラブルシューティングの証跡として保存して根拠にする。
    - C. Alert 機能の変更点を出力本文から切り離して変更記録のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更記録で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Alert 機能 は「Alert 機能の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Alert 機能の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Alert 機能を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Alert-to-trap service fails to initialize {#c32-i2789}
*分類: トラブルシューティング*  ・  難易度: 中級

Alert-to-trap service fails to initializeは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文分離のトラブルシューティングに関係する Alert-to-trap 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文分離の確認値として扱う。 ✅
    - B. Alert-to-trap 機能の名称と担当者名のみを残して構文分離のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文分離のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Alert-to-trap 機能 は「Alert-to-trap 機能の用途をネットビューの表示で確認する構文分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの Alert-to-trap 機能と DSI633I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Alert-to-trap 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Alert-to-trap service information {#c32-i2790}
*分類: トラブルシューティング*  ・  難易度: 中級

'Alert-to-trap service information' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.387

??? question "確認問題（1問）"
    **問題.** 展開分離のトラブルシューティングで Alert-to-trap 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Alert-to-trap 機能の出力を取らず展開分離のトラブルシューティングの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開分離の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して展開分離のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では Alert-to-trap 機能 は「展開分離のトラブルシューティングに関係する定義値と表示行を照合する展開分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では Alert-to-trap 機能の属性行と DSI633I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では Alert-to-trap 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.387



### Alerts are not converted to the expected Event Integration Facility events {#c32-i2791}
*分類: トラブルシューティング*  ・  難易度: 中級

Alerts are not converted to the expected Event Integration Facility eventsは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出分離のトラブルシューティングでネットビューの運用確認を行います。Alerts 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出分離のトラブルシューティングを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を呼出分離で確認する。 ✅
    - D. Alerts 機能の属性行を読まず呼出分離のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では Alerts 機能 は「IBM Z NetViewで Alerts 機能の扱いを記録する呼出分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では Alerts 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では Alerts 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Alerts are not forwarded to the expected event server {#c32-i2792}
*分類: トラブルシューティング*  ・  難易度: 中級

Alerts are not forwarded to the expected event serverは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換分離のトラブルシューティングに関する Alerts 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換分離のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離のトラブルシューティングの証跡として保存して根拠にする。
    - C. Alerts 機能の変更点を出力本文から切り離して置換分離のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、置換分離の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Alerts 機能 は「Alerts 機能の状態と出力メッセージを結び付ける置換分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Alerts 機能の出力行と DSI633I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Alerts 機能を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### An Alert is continuously forwarded {#c32-i2793}
*分類: トラブルシューティング*  ・  難易度: 中級

An Alert is continuously forwardedは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端分離のトラブルシューティングに関係する An 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端分離の確認記録にまとめる。 ✅
    - B. An 機能の名称と担当者名のみを残して終端分離のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端分離のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では An 機能 は「An 機能の用途をネットビューの表示で確認する終端分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの An 機能と DSI633I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では An 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### An Alert is incorrectly cached {#c32-i2794}
*分類: トラブルシューティング*  ・  難易度: 中級

An Alert is incorrectly cachedは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索分離のトラブルシューティングで An 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. An 機能の出力を取らず探索分離のトラブルシューティングの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索分離の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して探索分離のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では An 機能 は「探索分離のトラブルシューティングに関係する定義値と表示行を照合する探索分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では An 機能の属性行と DSI633I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では An 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Application failure {#c32-i2795}
*分類: トラブルシューティング*  ・  難易度: 中級

'Application failure' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.45

??? question "確認問題（1問）"
    **問題.** 区切分離のトラブルシューティングで Application 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Application 機能の出力を取らず区切分離のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切分離の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して区切分離のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では Application 機能 は「区切分離のトラブルシューティングに関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では Application 機能の属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では Application 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.45



### Asynchronous method looping {#c32-i2796}
*分類: トラブルシューティング*  ・  難易度: 中級

'Asynchronous method looping' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.325

??? question "確認問題（1問）"
    **問題.** 範囲分離のトラブルシューティングでネットビューの運用確認を行います。Asynchronous 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、範囲分離の点検結果を残す。 ✅
    - D. Asynchronous 機能の属性行を読まず範囲分離のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では Asynchronous 機能 は「IBM Z NetViewで Asynchronous 機能の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では Asynchronous 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では Asynchronous 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.325



### BNH067I message is received; unexpected switch of master NetView {#c32-i2797}
*分類: トラブルシューティング*  ・  難易度: 中級

'BNH067I message is received; unexpected switch of master NetView' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230

??? question "確認問題（1問）"
    **問題.** 優先分離のトラブルシューティングに関する BNH067I 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先分離のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離のトラブルシューティングの証跡として保存して根拠にする。
    - C. BNH067I 機能の変更点を出力本文から切り離して優先分離のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では BNH067I 機能 は「BNH067I 機能の状態と出力メッセージを結び付ける優先分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では BNH067I 機能の出力行と DSI633I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では BNH067I 機能を IBM Z NetViewの確認記録に残し、対象名は優先分離対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230



### BNH160I–BNH163I messages {#c32-i2798}
*分類: トラブルシューティング*  ・  難易度: 中級

'BNH160I–BNH163I messages' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.224

??? question "確認問題（1問）"
    **問題.** 記録分離の–に関係する BNH160I–BNH163I 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録分離の確認値として扱う。 ✅
    - B. BNH160I–BNH163I 機能の名称と担当者名のみを残して記録分離の–の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離の–を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離の–の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では BNH160I–BNH163I 機能 は「BNH160I–BNH163I 機能の用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの BNH160I–BNH163I 機能と DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では BNH160I–BNH163I 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.224



### BNH558E message is received; master NetView unable to contact enterprise system {#c32-i2799}
*分類: トラブルシューティング*  ・  難易度: 中級

'BNH558E message is received; master NetView unable to contact enterprise system' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.617

??? question "確認問題（1問）"
    **問題.** 比較分離のトラブルシューティングで BNH558E 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BNH558E 機能の出力を取らず比較分離のトラブルシューティングの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較分離の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して比較分離のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では BNH558E 機能 は「比較分離のトラブルシューティングに関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では BNH558E 機能の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では BNH558E 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.617



### BNH587I message is received during NetView initialization {#c32-i2800}
*分類: トラブルシューティング*  ・  難易度: 中級

'BNH587I message is received during NetView initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.62

??? question "確認問題（1問）"
    **問題.** 順序分離のトラブルシューティングでネットビューの運用確認を行います。BNH587I 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離のトラブルシューティングを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を順序分離で確認する。 ✅
    - D. BNH587I 機能の属性行を読まず順序分離のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では BNH587I 機能 は「IBM Z NetViewで BNH587I 機能の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では BNH587I 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では BNH587I 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.62



### BNH638I message issued per stack for Discovery Manager Resource {#c32-i2801}
*分類: トラブルシューティング*  ・  難易度: 中級

'BNH638I message issued per stack for Discovery Manager Resource' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_IP_Management.pdf p.29

??? question "確認問題（1問）"
    **問題.** 値域分離のトラブルシューティングに関する BNH638I 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離のトラブルシューティングの証跡として保存して根拠にする。
    - C. BNH638I 機能の変更点を出力本文から切り離して値域分離のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、値域分離の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では BNH638I 機能 は「BNH638I 機能の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では BNH638I 機能の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では BNH638I 機能を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_IP_Management.pdf p.29



### Browser does not trust the website's certificate {#c32-i2802}
*分類: トラブルシューティング*  ・  難易度: 上級

Browser does not trust the website's certificateは、Tivoli NetView z/OS 自動化のトラブルシューティングで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告分離のトラブルシューティングに関係する Browser 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告分離の確認記録にまとめる。 ✅
    - B. Browser 機能の名称と担当者名のみを残して警告分離のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では Browser 機能 は「Browser 機能の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの Browser 機能と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では Browser 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### CNM983E, CNM998E, or CNM999E message is received {#c32-i2803}
*分類: トラブルシューティング*  ・  難易度: 中級

CNM983E, CNM998E, or CNM999E message is receivedは、Tivoli NetView z/OS 自動化のトラブルシューティングでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文読解のトラブルシューティングに関係する CNM983E 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文読解として引き継ぐ。 ✅
    - B. CNM983E 命令の名称と担当者名のみを残して構文読解のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では CNM983E 命令 は「CNM983E 命令の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewの CNM983E 命令と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では CNM983E 命令を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### CNMTRACE {#c32-i2804}
*分類: トラブルシューティング*  ・  難易度: 上級

'CNMTRACE' (Lv2: トラブルシューティング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開読解のトラブルシューティングで CNMTRACE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CNMTRACE の出力を取らず展開読解のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開読解の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して展開読解のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では CNMTRACE は「展開読解のトラブルシューティングに関係する定義値と表示行を照合する展開読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では CNMTRACE の属性行と DSI633I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では CNMTRACE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Cannot start the NetView agent {#c32-i2805}
*分類: トラブルシューティング*  ・  難易度: 中級

Cannot start the NetView agentは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧分離のトラブルシューティングで Cannot 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Cannot 機能の出力を取らず復旧分離のトラブルシューティングの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧分離の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Cannot 機能 は「復旧分離のトラブルシューティングに関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Cannot 機能の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Cannot 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Capturing Message Log Data {#c32-i2806}
*分類: トラブルシューティング*  ・  難易度: 中級

'Capturing Message Log Data' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Application_Programmers_Guide.pdf p.55

??? question "確認問題（1問）"
    **問題.** 監査分離のトラブルシューティングでネットビューの運用確認を行います。Capturing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離のトラブルシューティングを正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、監査分離の結果として保存する。 ✅
    - D. Capturing 機能の属性行を読まず監査分離のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Capturing 機能 は「IBM Z NetViewで Capturing 機能の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Capturing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Capturing 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Application_Programmers_Guide.pdf p.55



### Classifying problems {#c32-i2807}
*分類: トラブルシューティング*  ・  難易度: 中級

'Classifying problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 変更分離のトラブルシューティングに関する Classifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離のトラブルシューティングの証跡として保存して根拠にする。
    - C. Classifying 機能の変更点を出力本文から切り離して変更分離のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、変更分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では Classifying 機能 は「Classifying 機能の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では Classifying 機能の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では Classifying 機能を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### Collecting problem data {#c32-i2808}
*分類: トラブルシューティング*  ・  難易度: 中級

'Collecting problem data' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.191

??? question "確認問題（1問）"
    **問題.** 呼出読解のトラブルシューティングでネットビューの運用確認を行います。Collecting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出読解のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出読解のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、呼出読解の点検結果を残す。 ✅
    - D. Collecting 機能の属性行を読まず呼出読解のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では Collecting 機能 は「IBM Z NetViewで Collecting 機能の扱いを記録する呼出読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では Collecting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では Collecting 機能の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.191



### Command problems {#c32-i2809}
*分類: トラブルシューティング*  ・  難易度: 中級

'Command problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 置換読解のトラブルシューティングに関する Command problemsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換読解のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解のトラブルシューティングの証跡として保存して根拠にする。
    - C. Command problemsの変更点を出力本文から切り離して置換読解のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では Command problems は「Command problemsの状態と出力メッセージを結び付ける置換読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では Command problemsの出力行と DSI633I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では Command problemsを IBM Z NetViewの確認記録に残し、対象名は置換読解対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### Common requirements for SMF and SYSLOGD notifications {#c32-i2810}
*分類: トラブルシューティング*  ・  難易度: 上級

Common requirements for SMF and SYSLOGD notificationsは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端読解のトラブルシューティングに関係する Common 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端読解の確認値として扱う。 ✅
    - B. Common 機能の名称と担当者名のみを残して終端読解のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端読解のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端読解のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では Common 機能 は「Common 機能の用途をネットビューの表示で確認する終端読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM Z NetViewの Common 機能と DSI633I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では Common 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Confirmed alert adapter fails to initialize {#c32-i2811}
*分類: トラブルシューティング*  ・  難易度: 中級

Confirmed alert adapter fails to initializeは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索読解のトラブルシューティングで Confirmed 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Confirmed 機能の出力を取らず探索読解のトラブルシューティングの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索読解の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して探索読解のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では Confirmed 機能 は「探索読解のトラブルシューティングに関係する定義値と表示行を照合する探索読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では Confirmed 機能の属性行と DSI633I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では Confirmed 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Confirmed alert adapter service information {#c32-i2812}
*分類: トラブルシューティング*  ・  難易度: 中級

'Confirmed alert adapter service information' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView.pdf p.127

??? question "確認問題（1問）"
    **問題.** 上書読解のトラブルシューティングでネットビューの運用確認を行います。Confirmed 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書読解のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書読解のトラブルシューティングを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を上書読解で確認する。 ✅
    - D. Confirmed 機能の属性行を読まず上書読解のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Confirmed 機能 は「IBM Z NetViewで Confirmed 機能の扱いを記録する上書読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Confirmed 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では Confirmed 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** NetView_6.4_Users_Guide_NetView.pdf p.127



### Confirmed message adapter fails to initialize {#c32-i2813}
*分類: トラブルシューティング*  ・  難易度: 中級

Confirmed message adapter fails to initializeは、Tivoli NetView z/OS 自動化のトラブルシューティングでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力読解のトラブルシューティングに関する Confirmed 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力読解のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解のトラブルシューティングの証跡として保存して根拠にする。
    - C. Confirmed 機能の変更点を出力本文から切り離して出力読解のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、出力読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では Confirmed 機能 は「Confirmed 機能の状態と出力メッセージを結び付ける出力読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では Confirmed 機能の出力行と DSI633I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では Confirmed 機能を IBM Z NetViewの確認記録に残し、対象名は出力読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Confirmed message adapter service information {#c32-i2814}
*分類: トラブルシューティング*  ・  難易度: 中級

'Confirmed message adapter service information' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView.pdf p.127

??? question "確認問題（1問）"
    **問題.** 条件読解のトラブルシューティングに関係する Confirmed 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件読解の確認記録にまとめる。 ✅
    - B. Confirmed 機能の名称と担当者名のみを残して条件読解のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件読解のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件読解のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では Confirmed 機能 は「Confirmed 機能の用途をネットビューの表示で確認する条件読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM Z NetViewの Confirmed 機能と DSI633I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では Confirmed 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** NetView_6.4_Users_Guide_NetView.pdf p.127



### Console log window {#c32-i2815}
*分類: トラブルシューティング*  ・  難易度: 中級

'Console log window' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Users_Guide_NetView_Management_Console.pdf p.69

??? question "確認問題（1問）"
    **問題.** 区切読解のトラブルシューティングで Console log windowの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Console log windowの出力を取らず区切読解のトラブルシューティングの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切読解の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して区切読解のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では Console log window は「区切読解のトラブルシューティングに関係する定義値と表示行を照合する区切読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では Console log windowの属性行と DSI633I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では Console log windowを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切読解初出です。

    **出典:** NetView_6.4_Users_Guide_NetView_Management_Console.pdf p.69



### Contacting IBM Software Support {#c32-i2816}
*分類: トラブルシューティング*  ・  難易度: 中級

'Contacting IBM Software Support' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Application_Programmers_Guide.pdf p.53

??? question "確認問題（1問）"
    **問題.** 範囲読解のトラブルシューティングでネットビューの運用確認を行います。Contacting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲読解のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲読解のトラブルシューティングを正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、範囲読解の結果として保存する。 ✅
    - D. Contacting 機能の属性行を読まず範囲読解のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Contacting 機能 は「IBM Z NetViewで Contacting 機能の扱いを記録する範囲読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Contacting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では Contacting 機能の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** NetView_6.4_Application_Programmers_Guide.pdf p.53



### Control blocks {#c32-i2817}
*分類: トラブルシューティング*  ・  難易度: 中級

'Control blocks' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.32


### Control blocks used during Command Facility initialization {#c32-i2818}
*分類: トラブルシューティング*  ・  難易度: 中級

'Control blocks used during Command Facility initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.74

??? question "確認問題（1問）"
    **問題.** 記録読解のトラブルシューティングに関係する Control 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録読解として引き継ぐ。 ✅
    - B. Control 機能の名称と担当者名のみを残して記録読解のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Control 機能 は「Control 機能の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの Control 機能と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Control 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.74



### Control blocks used during Hardware Monitor initialization {#c32-i2819}
*分類: トラブルシューティング*  ・  難易度: 中級

'Control blocks used during Hardware Monitor initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Automation_Guide.pdf p.322

??? question "確認問題（1問）"
    **問題.** 比較読解のトラブルシューティングで Control 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Control 機能の出力を取らず比較読解のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較読解の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して比較読解のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Control 機能 は「比較読解のトラブルシューティングに関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Control 機能の属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Control 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Automation_Guide.pdf p.322



### Control blocks used during Operator Station logon (TVB) {#c32-i2820}
*分類: トラブルシューティング*  ・  難易度: 中級

'Control blocks used during Operator Station logon (TVB)' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.665

??? question "確認問題（1問）"
    **問題.** 順序読解のトラブルシューティングでネットビューの運用確認を行います。Control 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、順序読解の点検結果を残す。 ✅
    - D. Control 機能の属性行を読まず順序読解のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Control 機能 は「IBM Z NetViewで Control 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Control 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Control 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.665



### Control blocks used during Session Monitor initialization {#c32-i2821}
*分類: トラブルシューティング*  ・  難易度: 中級

'Control blocks used during Session Monitor initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230

??? question "確認問題（1問）"
    **問題.** 値域読解のトラブルシューティングに関する Control 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域読解のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解のトラブルシューティングの証跡として保存して根拠にする。
    - C. Control 機能の変更点を出力本文から切り離して値域読解のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では Control 機能 は「Control 機能の状態と出力メッセージを結び付ける値域読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では Control 機能の出力行と DSI633I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では Control 機能を IBM Z NetViewの確認記録に残し、対象名は値域読解対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230



### Control blocks used during Status Monitor initialization {#c32-i2822}
*分類: トラブルシューティング*  ・  難易度: 中級

'Control blocks used during Status Monitor initialization' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Administration_Reference.pdf p.295

??? question "確認問題（1問）"
    **問題.** 警告読解のトラブルシューティングに関係する Control 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告読解の確認値として扱う。 ✅
    - B. Control 機能の名称と担当者名のみを残して警告読解のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告読解のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Control 機能 は「Control 機能の用途をネットビューの表示で確認する警告読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの Control 機能と DSI633I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Control 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Administration_Reference.pdf p.295



### Cross-Product links missing from link list {#c32-i2823}
*分類: トラブルシューティング*  ・  難易度: 中級

'Cross-Product links missing from link list' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.397

??? question "確認問題（1問）"
    **問題.** 復旧読解のトラブルシューティングで Cross-Product 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Cross-Product 機能の出力を取らず復旧読解のトラブルシューティングの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧読解の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して復旧読解のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では Cross-Product 機能 は「復旧読解のトラブルシューティングに関係する定義値と表示行を照合する復旧読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では Cross-Product 機能の属性行と DSI633I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では Cross-Product 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.397



### DSI124I message is received {#c32-i2824}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSI124I message is received' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230

??? question "確認問題（1問）"
    **問題.** 記録確認のトラブルシューティングに関係する DSI124I 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録確認の根拠にする。 ✅
    - B. DSI124I 機能の名称と担当者名のみを残して記録確認のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録確認のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では DSI124I 機能 は「DSI124I 機能の用途をネットビューの表示で確認する記録確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewの DSI124I 機能と DSI633I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では DSI124I 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230



### DSI24TRC {#c32-i2825}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSI24TRC' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.453

??? question "確認問題（1問）"
    **問題.** 比較確認のトラブルシューティングで DSI24TRC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DSI24TRC の出力を取らず比較確認のトラブルシューティングの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較確認の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較確認のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では DSI24TRC は「比較確認のトラブルシューティングに関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では DSI24TRC の属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では DSI24TRC を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.453



### DSIGADHX {#c32-i2826}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSIGADHX' (Lv2: トラブルシューティング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序確認のトラブルシューティングでネットビューの運用確認を行います。DSIGADHX の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序確認のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序確認のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序確認の採否を説明欄に結び付ける。 ✅
    - D. DSIGADHX の属性行を読まず順序確認のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では DSIGADHX は「IBM Z NetViewで DSIGADHX の扱いを記録する順序確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では DSIGADHX の表示結果と DSI633I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では DSIGADHX の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### DSIGTVBA {#c32-i2827}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSIGTVBA' (Lv2: トラブルシューティング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域確認のトラブルシューティングに関する DSIGTVBA の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のトラブルシューティングの証跡として保存して根拠にする。
    - C. DSIGTVBA の変更点を出力本文から切り離して値域確認のトラブルシューティングの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域確認として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では DSIGTVBA は「DSIGTVBA の状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では DSIGTVBA の出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では DSIGTVBA を IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### DSIGV2VR {#c32-i2828}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSIGV2VR' (Lv2: トラブルシューティング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のトラブルシューティングに関係する DSIGV2VR の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告確認の確認にする。 ✅
    - B. DSIGV2VR の名称と担当者名のみを残して警告確認のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では DSIGV2VR は「DSIGV2VR の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの DSIGV2VR と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では DSIGV2VR を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### DSIMODQY {#c32-i2829}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSIMODQY' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.453

??? question "確認問題（1問）"
    **問題.** 復旧確認のトラブルシューティングで DSIMODQY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DSIMODQY の出力を取らず復旧確認のトラブルシューティングの説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧確認の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では DSIMODQY は「復旧確認のトラブルシューティングに関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では DSIMODQY の属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では DSIMODQY を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.453



### DSINDEF data set format {#c32-i2830}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSINDEF data set format' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Migration_Guide.pdf p.65

??? question "確認問題（1問）"
    **問題.** 監査確認のトラブルシューティングでネットビューの運用確認を行います。DSINDEF 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認のトラブルシューティングを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査確認で再確認できる形にする。 ✅
    - D. DSINDEF 機能の属性行を読まず監査確認のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では DSINDEF 機能 は「IBM Z NetViewで DSINDEF 機能の扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では DSINDEF 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では DSINDEF 機能の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Installation_Migration_Guide.pdf p.65



### DSISHWVR {#c32-i2831}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSISHWVR' (Lv2: トラブルシューティング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更確認のトラブルシューティングに関する DSISHWVR の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更確認のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のトラブルシューティングの証跡として保存して根拠にする。
    - C. DSISHWVR の変更点を出力本文から切り離して変更確認のトラブルシューティングの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では DSISHWVR は「DSISHWVR の状態と出力メッセージを結び付ける変更確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では DSISHWVR の出力行と DSI633I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では DSISHWVR を IBM Z NetViewの確認記録に残し、対象名は変更確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### DSISTRLS {#c32-i2832}
*分類: トラブルシューティング*  ・  難易度: 中級

'DSISTRLS' (Lv2: トラブルシューティング) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文照合のトラブルシューティングに関係する DSISTRLS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文照合の根拠を固定する。 ✅
    - B. DSISTRLS の名称と担当者名のみを残して構文照合のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では DSISTRLS は「DSISTRLS の用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの DSISTRLS と DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では DSISTRLS を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### DWO049W message is received for a DSIFRE request {#c32-i2833}
*分類: トラブルシューティング*  ・  難易度: 中級

'DWO049W message is received for a DSIFRE request' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.365

??? question "確認問題（1問）"
    **問題.** 呼出照合のトラブルシューティングでネットビューの運用確認を行います。DWO049W 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出照合のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、呼出照合の証跡として残す。 ✅
    - D. DWO049W 機能の属性行を読まず呼出照合のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では DWO049W 機能 は「IBM Z NetViewで DWO049W 機能の扱いを記録する呼出照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では DWO049W 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では DWO049W 機能の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.365



### DWO049W message is received for a DSIGET request {#c32-i2834}
*分類: トラブルシューティング*  ・  難易度: 中級

'DWO049W message is received for a DSIGET request' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.365

??? question "確認問題（1問）"
    **問題.** 置換照合のトラブルシューティングに関する DWO049W 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換照合のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のトラブルシューティングの証跡として保存して根拠にする。
    - C. DWO049W 機能の変更点を出力本文から切り離して置換照合のトラブルシューティングの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換照合の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では DWO049W 機能 は「DWO049W 機能の状態と出力メッセージを結び付ける置換照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では DWO049W 機能の出力行と DSI633I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では DWO049W 機能を IBM Z NetViewの確認記録に残し、対象名は置換照合対象です。

    **出典:** NetView_6.4_Messages_and_Codes_Vol1_AAU-DSI.pdf p.365



### DWO090A message is received {#c32-i2835}
*分類: トラブルシューティング*  ・  難易度: 中級

'DWO090A message is received' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230

??? question "確認問題（1問）"
    **問題.** 終端照合のトラブルシューティングに関係する DWO090A 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端照合の根拠にする。 ✅
    - B. DWO090A 機能の名称と担当者名のみを残して終端照合のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端照合のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端照合のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では DWO090A 機能 は「DWO090A 機能の用途をネットビューの表示で確認する終端照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM Z NetViewの DWO090A 機能と DSI633I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では DWO090A 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230



### DWO158W message is received {#c32-i2836}
*分類: トラブルシューティング*  ・  難易度: 中級

'DWO158W message is received' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230

??? question "確認問題（1問）"
    **問題.** 探索照合のトラブルシューティングで DWO158W 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DWO158W 機能の出力を取らず探索照合のトラブルシューティングの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、探索照合の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して探索照合のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では DWO158W 機能 は「探索照合のトラブルシューティングに関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では DWO158W 機能の属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では DWO158W 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230



### DWO627E message is received (MS Transport cancels) {#c32-i2837}
*分類: トラブルシューティング*  ・  難易度: 中級

'DWO627E message is received (MS Transport cancels)' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Application_Programmers_Guide.pdf p.55

??? question "確認問題（1問）"
    **問題.** 上書照合のトラブルシューティングでネットビューの運用確認を行います。DWO627E 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書照合のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書照合のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、上書照合の採否を説明欄に結び付ける。 ✅
    - D. DWO627E 機能の属性行を読まず上書照合のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では DWO627E 機能 は「IBM Z NetViewで DWO627E 機能の扱いを記録する上書照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では DWO627E 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では DWO627E 機能の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** NetView_6.4_Application_Programmers_Guide.pdf p.55



### Debugging methods {#c32-i2838}
*分類: トラブルシューティング*  ・  難易度: 中級

'Debugging methods' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.579

??? question "確認問題（1問）"
    **問題.** 監査読解のトラブルシューティングでネットビューの運用確認を行います。Debugging methodsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査読解のトラブルシューティングを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を監査読解で確認する。 ✅
    - D. Debugging methodsの属性行を読まず監査読解のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では Debugging methods は「IBM Z NetViewで Debugging methodsの扱いを記録する監査読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では Debugging methodsの表示結果と DSI633I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では Debugging methodsの使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Resource_Object_Data_Manager_and_GMFHS_Programmers_Guide.pdf p.579



### Detail qualifier vector {#c32-i2839}
*分類: トラブルシューティング*  ・  難易度: 中級

'Detail qualifier vector' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Customization_Guide.pdf p.97

??? question "確認問題（1問）"
    **問題.** 変更読解のトラブルシューティングに関する Detail 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解のトラブルシューティングの証跡として保存して根拠にする。
    - C. Detail 機能の変更点を出力本文から切り離して変更読解のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Detail 機能 は「Detail 機能の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Detail 機能の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Detail 機能を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Customization_Guide.pdf p.97



### Diagnosing Automated Operations Network problems {#c32-i2840}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnosing Automated Operations Network problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.201

??? question "確認問題（1問）"
    **問題.** 構文検分のトラブルシューティングに関係する Diagnosing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文検分の確認記録にまとめる。 ✅
    - B. Diagnosing 機能の名称と担当者名のみを残して構文検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Diagnosing 機能 は「Diagnosing 機能の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの Diagnosing 機能と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Diagnosing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.201



### Diagnosing Event/Automation Service problems {#c32-i2841}
*分類: トラブルシューティング*  ・  難易度: 上級

'Diagnosing Event/Automation Service problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として Diagnosing Event/Automation  を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 展開照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。展開照合権限で扱う Diagnosing Event/Automation  は Tivoli NetView z/OS 自動化 の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として Diagnosing Event/Automation  を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### Diagnosing NetView Management Console and GMFHS problems {#c32-i2842}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnosing NetView Management Console and GMFHS problemsは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出検分のトラブルシューティングでネットビューの運用確認を行います。Diagnosing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分のトラブルシューティングを確認した扱いにする。
    - B. EKG000I の有無を確認せず呼出検分のトラブルシューティングを正常終了として記録する。
    - C. 同じ画面で対象行と EKG000I を読み、呼出検分の結果として保存する。 ✅
    - D. Diagnosing 機能の属性行を読まず呼出検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では Diagnosing 機能 は「IBM Z NetViewで Diagnosing 機能の扱いを記録する呼出検分項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では Diagnosing 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では Diagnosing 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnosing NetView REST Server and NetView Zowe CLI Plug-ins problems {#c32-i2843}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnosing NetView REST Server and NetView Zowe CLI Plug-ins problemsは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端検分のトラブルシューティングに関係する Diagnosing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端検分として引き継ぐ。 ✅
    - B. Diagnosing 機能の名称と担当者名のみを残して終端検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Diagnosing 機能 は「Diagnosing 機能の用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの Diagnosing 機能と DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Diagnosing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnosing NetView problems related to the GDPS Active/Active Continuous Availability solution {#c32-i2844}
*分類: トラブルシューティング*  ・  難易度: 上級

Diagnosing NetView problems related to the GDPS Active/Active Continuous Availability solutionは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Diagnosing NetView security problems {#c32-i2845}
*分類: トラブルシューティング*  ・  難易度: 上級

'Diagnosing NetView security problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Getting_Started.pdf p.110

??? question "確認問題（1問）"
    **問題.** 探索検分のトラブルシューティングで Diagnosing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Diagnosing 機能の出力を取らず探索検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索検分の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して探索検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Diagnosing 機能 は「探索検分のトラブルシューティングに関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Diagnosing 機能の属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Diagnosing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Installation_Getting_Started.pdf p.110



### Diagnosing NetView zERT notification messages problems {#c32-i2846}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnosing NetView zERT notification messages problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.224

??? question "確認問題（1問）"
    **問題.** 上書検分のトラブルシューティングでネットビューの運用確認を行います。Diagnosing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書検分の点検結果を残す。 ✅
    - D. Diagnosing 機能の属性行を読まず上書検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では Diagnosing 機能 は「IBM Z NetViewで Diagnosing 機能の扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では Diagnosing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では Diagnosing 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.224



### Diagnosing RODM problems {#c32-i2847}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnosing RODM problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 条件検分のトラブルシューティングに関係する Diagnosing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件検分の確認値として扱う。 ✅
    - B. Diagnosing 機能の名称と担当者名のみを残して条件検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず条件検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Diagnosing 機能 は「Diagnosing 機能の用途をネットビューの表示で確認する条件検分項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの Diagnosing 機能と EKG000I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Diagnosing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### Diagnosing Z NetView Enterprise Management Agent problems {#c32-i2848}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnosing Z NetView Enterprise Management Agent problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 範囲検分のトラブルシューティングでネットビューの運用確認を行います。Diagnosing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分のトラブルシューティングを正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を範囲検分で確認する。 ✅
    - D. Diagnosing 機能の属性行を読まず範囲検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Diagnosing 機能 は「IBM Z NetViewで Diagnosing 機能の扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Diagnosing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Diagnosing 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### Diagnosing problems {#c32-i2849}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnosing problems' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64

??? question "確認問題（1問）"
    **問題.** 出力検分のトラブルシューティングに関する Diagnosing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Diagnosing 機能の変更点を出力本文から切り離して出力検分のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では Diagnosing 機能 は「Diagnosing 機能の状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では Diagnosing 機能の出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では Diagnosing 機能を IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.64



### Diagnosing the NetView program {#c32-i2850}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnosing the NetView program' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47

??? question "確認問題（1問）"
    **問題.** 区切検分のトラブルシューティングで Diagnosing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Diagnosing 機能の出力を取らず区切検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切検分の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して区切検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Diagnosing 機能 は「区切検分のトラブルシューティングに関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Diagnosing 機能の属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Diagnosing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.47



### Diagnostic command summary {#c32-i2851}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnostic command summary' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.270

??? question "確認問題（1問）"
    **問題.** 優先検分のトラブルシューティングに関する Diagnostic 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Diagnostic 機能の変更点を出力本文から切り離して優先検分のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、優先検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Diagnostic 機能 は「Diagnostic 機能の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Diagnostic 機能の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Diagnostic 機能を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.270



### Diagnostic tools for GMFHS {#c32-i2852}
*分類: トラブルシューティング*  ・  難易度: 中級

'Diagnostic tools for GMFHS' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230

??? question "確認問題（1問）"
    **問題.** 記録検分のトラブルシューティングに関係する Diagnostic 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録検分の確認記録にまとめる。 ✅
    - B. Diagnostic 機能の名称と担当者名のみを残して記録検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず記録検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Diagnostic 機能 は「Diagnostic 機能の用途をネットビューの表示で確認する記録検分項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewの Diagnostic 機能と EKG000I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Diagnostic 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Troubleshooting_Guide.pdf p.230



### Diagnostic tools for IP Management {#c32-i2853}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for IP Managementは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較検分のトラブルシューティングで Diagnostic 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Diagnostic 機能の出力を取らず比較検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較検分の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して比較検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Diagnostic 機能 は「比較検分のトラブルシューティングに関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Diagnostic 機能の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Diagnostic 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for NetView Management Console and GMFHS {#c32-i2854}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for NetView Management Console and GMFHSは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検分のトラブルシューティングでネットビューの運用確認を行います。Diagnostic 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分のトラブルシューティングを確認した扱いにする。
    - B. EKG000I の有無を確認せず順序検分のトラブルシューティングを正常終了として記録する。
    - C. 同じ画面で対象行と EKG000I を読み、順序検分の結果として保存する。 ✅
    - D. Diagnostic 機能の属性行を読まず順序検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Diagnostic 機能 は「IBM Z NetViewで Diagnostic 機能の扱いを記録する順序検分項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Diagnostic 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Diagnostic 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for NetView REST Server {#c32-i2855}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for NetView REST Serverは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域検分のトラブルシューティングに関する Diagnostic 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Diagnostic 機能の変更点を出力本文から切り離して値域検分のトラブルシューティングの承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、値域検分の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Diagnostic 機能 は「Diagnostic 機能の状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Diagnostic 機能の出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Diagnostic 機能を IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for the Event/Automation Service {#c32-i2856}
*分類: トラブルシューティング*  ・  難易度: 上級

Diagnostic tools for the Event/Automation Serviceは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告検分のトラブルシューティングに関係する Diagnostic 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告検分として引き継ぐ。 ✅
    - B. Diagnostic 機能の名称と担当者名のみを残して警告検分のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検分のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検分のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Diagnostic 機能 は「Diagnostic 機能の用途をネットビューの表示で確認する警告検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM Z NetViewの Diagnostic 機能と DSI633I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Diagnostic 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for the IBM Z NetView Enterprise Management Agent {#c32-i2857}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for the IBM Z NetView Enterprise Management Agentは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧検分のトラブルシューティングで Diagnostic 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Diagnostic 機能の出力を取らず復旧検分のトラブルシューティングの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧検分の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Diagnostic 機能 は「復旧検分のトラブルシューティングに関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Diagnostic 機能の属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Diagnostic 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for the NetView Management Console {#c32-i2858}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for the NetView Management Consoleは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査検分のトラブルシューティングでネットビューの運用確認を行います。Diagnostic 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検分のトラブルシューティングを正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、監査検分の点検結果を残す。 ✅
    - D. Diagnostic 機能の属性行を読まず監査検分のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Diagnostic 機能 は「IBM Z NetViewで Diagnostic 機能の扱いを記録する監査検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Diagnostic 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Diagnostic 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for the NetView program {#c32-i2859}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for the NetView programは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更検分のトラブルシューティングに関する Diagnostic 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検分のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分のトラブルシューティングの証跡として保存して根拠にする。
    - C. Diagnostic 機能の変更点を出力本文から切り離して変更検分のトラブルシューティングの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Diagnostic 機能 は「Diagnostic 機能の状態と出力メッセージを結び付ける変更検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Diagnostic 機能の出力行と DSI633I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Diagnostic 機能を IBM Z NetViewの確認記録に残し、対象名は変更検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools for the Resource Object Data Manager (RODM) {#c32-i2860}
*分類: トラブルシューティング*  ・  難易度: 中級

Diagnostic tools for the Resource Object Data Manager (RODM)は、Tivoli NetView z/OS 自動化のトラブルシューティングでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文確認のトラブルシューティングに関係する Diagnostic 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文確認の根拠にする。 ✅
    - B. Diagnostic 機能の名称と担当者名のみを残して構文確認のトラブルシューティングの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文確認のトラブルシューティングを確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず構文確認のトラブルシューティングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Diagnostic 機能 は「Diagnostic 機能の用途をネットビューの表示で確認する構文確認項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Z NetViewの Diagnostic 機能と EKG000I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Diagnostic 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Diagnostic tools to use with the GDPS Continuous Availability solution {#c32-i2861}
*分類: トラブルシューティング*  ・  難易度: 上級

Diagnostic tools to use with the GDPS Continuous Availability solutionは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開確認のトラブルシューティングで Diagnostic 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Diagnostic 機能の出力を取らず展開確認のトラブルシューティングの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開確認の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開確認のトラブルシューティングの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のトラブルシューティングへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Diagnostic 機能 は「展開確認のトラブルシューティングに関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Diagnostic 機能の属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Diagnostic 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Discovery commands fail {#c32-i2862}
*分類: トラブルシューティング*  ・  難易度: 中級

'Discovery commands fail' (Lv2: トラブルシューティング) は IBM NetView 6.4 における トラブルシューティング 領域の項目

**出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.150

??? question "確認問題（1問）"
    **問題.** 呼出確認のトラブルシューティングでネットビューの運用確認を行います。Discovery 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認のトラブルシューティングを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出確認のトラブルシューティングを正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出確認の採否を説明欄に結び付ける。 ✅
    - D. Discovery 機能の属性行を読まず呼出確認のトラブルシューティングの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Discovery 機能 は「IBM Z NetViewで Discovery 機能の扱いを記録する呼出確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Discovery 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Discovery 機能の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Installation_Configuring_Additional_Components.pdf p.150



### Distributed DVIPA Connection Routing data is incomplete in the workspace {#c32-i2863}
*分類: トラブルシューティング*  ・  難易度: 中級

Distributed DVIPA Connection Routing data is incomplete in the workspaceは、Tivoli NetView z/OS 自動化のトラブルシューティングで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換確認のトラブルシューティングに関する Distributed 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認のトラブルシューティングの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のトラブルシューティングの証跡として保存して根拠にする。
    - C. Distributed 機能の変更点を出力本文から切り離して置換確認のトラブルシューティングの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換確認として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Distributed 機能 は「Distributed 機能の状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Distributed 機能の出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Distributed 機能を IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


