---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (26/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作)

### Using the Status Monitor (SNA Subarea) {#c32-i3768}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Status Monitor (SNA Subarea)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告読解のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告読解の根拠にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して警告読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する警告読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Status Monitor Panels {#c32-i3769}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Status Monitor Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧読解のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず復旧読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、復旧読解の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して復旧読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では Using 機能 は「復旧読解のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Target System Control Facility {#c32-i3770}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Target System Control Facilityは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査読解のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査読解のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査読解の採否を説明欄に結び付ける。 ✅
    - D. Using 機能の属性行を読まず監査読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する監査読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では Using 機能の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Topology Server Command Exits {#c32-i3771}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using the Topology Server Command Exitsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更読解のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して変更読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更読解として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the browse facility {#c32-i3772}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the browse facilityは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録分離のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録分離の根拠にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して記録分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the definition procedure {#c32-i3773}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the definition procedureは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告分離のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告分離の確認にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して警告分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### VIPA Routes Attributes {#c32-i3774}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

VIPA Routes Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.184) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.184)

??? question "確認問題（1問）"
    **問題.** 警告検分のユーザーズガイド 操作に関係する VIPA 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告検分の根拠を固定する。 ✅
    - B. VIPA 機能の名称と担当者名のみを残して警告検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では VIPA 機能 は「VIPA 機能の用途をネットビューの表示で確認する警告検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM Z NetViewの VIPA 機能と DSI633I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では VIPA 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### VIPA Routes Workspace {#c32-i3775}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

VIPA Routes Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.46) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.46)

??? question "確認問題（1問）"
    **問題.** 復旧検分のユーザーズガイド 操作で VIPA 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VIPA 機能の出力を取らず復旧検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を復旧検分で確認する。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では VIPA 機能 は「復旧検分のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では VIPA 機能の属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では VIPA 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### VSAM Replication Apply Details Attributes {#c32-i3776}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

VSAM Replication Apply Details Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.185) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.185)

??? question "確認問題（1問）"
    **問題.** 監査検分のユーザーズガイド 操作でネットビューの運用確認を行います。VSAM 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検分のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、監査検分の証跡として残す。 ✅
    - D. VSAM 機能の属性行を読まず監査検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では VSAM 機能 は「IBM Z NetViewで VSAM 機能の扱いを記録する監査検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では VSAM 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では VSAM 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### VSAM Replication Capture Details Attributes {#c32-i3777}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

VSAM Replication Capture Details Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.186) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.186)

??? question "確認問題（1問）"
    **問題.** 変更検分のユーザーズガイド 操作に関する VSAM 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. VSAM 機能の変更点を出力本文から切り離して変更検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更検分の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では VSAM 機能 は「VSAM 機能の状態と出力メッセージを結び付ける変更検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では VSAM 機能の出力行と DSI633I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では VSAM 機能を IBM Z NetViewの確認記録に残し、対象名は変更検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### VSAM Replication Details Workspace {#c32-i3778}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

VSAM Replication Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.88) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.88)

??? question "確認問題（1問）"
    **問題.** 構文確認のユーザーズガイド 操作に関係する VSAM 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文確認の点検結果を残す。 ✅
    - B. VSAM 機能の名称と担当者名のみを残して構文確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では VSAM 機能 は「VSAM 機能の用途をネットビューの表示で確認する構文確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Z NetViewの VSAM 機能と DSI633I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では VSAM 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### VTAM messages {#c32-i3779}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

VTAM messagesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.415) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.415)

??? question "確認問題（1問）"
    **問題.** 展開確認のユーザーズガイド 操作で VTAM messagesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VTAM messagesの出力を取らず展開確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開確認で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して展開確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では VTAM messages は「展開確認のユーザーズガイド 操作に関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では VTAM messagesの属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では VTAM messagesを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Viewing Open Networks {#c32-i3780}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Viewing Open Networksは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.92) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.92)

??? question "確認問題（1問）"
    **問題.** 区切検分のユーザーズガイド 操作で Viewing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Viewing 機能の出力を取らず区切検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、区切検分の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して区切検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Viewing 機能 は「区切検分のユーザーズガイド 操作に関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Viewing 機能の属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Viewing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Viewing lower connected nodes {#c32-i3781}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Viewing lower connected nodesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.120) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.120)

??? question "確認問題（1問）"
    **問題.** 条件検分のユーザーズガイド 操作に関係する Viewing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件検分の根拠にする。 ✅
    - B. Viewing 機能の名称と担当者名のみを残して条件検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Viewing 機能 は「Viewing 機能の用途をネットビューの表示で確認する条件検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの Viewing 機能と DSI633I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Viewing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Viewing resource information {#c32-i3782}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Viewing resource informationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.139) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.139)

??? question "確認問題（1問）"
    **問題.** 範囲検分のユーザーズガイド 操作でネットビューの運用確認を行います。Viewing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、範囲検分の採否を説明欄に結び付ける。 ✅
    - D. Viewing 機能の属性行を読まず範囲検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Viewing 機能 は「IBM Z NetViewで Viewing 機能の扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Viewing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Viewing 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Views Containing Resources for Which You Are Not Authorized {#c32-i3783}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Views Containing Resources for Which You Are Not Authorizedは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較検分のユーザーズガイド 操作で Views 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Views 機能の出力を取らず比較検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、比較検分の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して比較検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Views 機能 は「比較検分のユーザーズガイド 操作に関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Views 機能の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Views 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Views Containing Scheduled Resources {#c32-i3784}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Views Containing Scheduled Resourcesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide NetView Management Console (p.89) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.89)

??? question "確認問題（1問）"
    **問題.** 順序検分のユーザーズガイド 操作でネットビューの運用確認を行います。Views 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序検分で再確認できる形にする。 ✅
    - D. Views 機能の属性行を読まず順序検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Views 機能 は「IBM Z NetViewで Views 機能の扱いを記録する順序検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Views 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Views 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### What Are Network Management Tasks? {#c32-i3785}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

What Are Network Management Tasks?は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.45) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.45)

??? question "確認問題（1問）"
    **問題.** 呼出確認のユーザーズガイド 操作でネットビューの運用確認を行います。What 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出確認の確認値として扱う。 ✅
    - D. What 機能の属性行を読まず呼出確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では What 機能 は「IBM Z NetViewで What 機能の扱いを記録する呼出確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では What 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では What 機能の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### What You Can Do with NetView Management Console {#c32-i3786}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

What You Can Do with NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換確認のユーザーズガイド 操作に関する What 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. What 機能の変更点を出力本文から切り離して置換確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換確認の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では What 機能 は「What 機能の状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では What 機能の出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では What 機能を IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Working with Solicited Messages {#c32-i3787}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Working with Solicited Messagesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端確認のユーザーズガイド 操作に関係する Working 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を終端確認で確認する。 ✅
    - B. Working 機能の名称と担当者名のみを残して終端確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Working 機能 は「Working 機能の用途をネットビューの表示で確認する終端確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Z NetViewの Working 機能と DSI633I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Working 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Working with Unsolicited Messages {#c32-i3788}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Working with Unsolicited Messagesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索確認のユーザーズガイド 操作で Working 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Working 機能の出力を取らず探索確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索確認の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Working 機能 は「探索確認のユーザーズガイド 操作に関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Working 機能の属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Working 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Workload Lifeline Advisors Attributes {#c32-i3789}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Lifeline Advisors Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.187) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.187)

??? question "確認問題（1問）"
    **問題.** 上書確認のユーザーズガイド 操作でネットビューの運用確認を行います。Workload 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書確認の確認記録にまとめる。 ✅
    - D. Workload 機能の属性行を読まず上書確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Workload 機能 は「IBM Z NetViewで Workload 機能の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Workload 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Workload 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Lifeline Advisors Workspace {#c32-i3790}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Lifeline Advisors Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.89) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.89)

??? question "確認問題（1問）"
    **問題.** 出力確認のユーザーズガイド 操作に関する Workload 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Workload 機能の変更点を出力本文から切り離して出力確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では Workload 機能 は「Workload 機能の状態と出力メッセージを結び付ける出力確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では Workload 機能の出力行と DSI633I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では Workload 機能を IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Lifeline Agents Attributes {#c32-i3791}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Lifeline Agents Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.187) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.187)

??? question "確認問題（1問）"
    **問題.** 条件確認のユーザーズガイド 操作に関係する Workload 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、条件確認の結果として保存する。 ✅
    - B. Workload 機能の名称と担当者名のみを残して条件確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では Workload 機能 は「Workload 機能の用途をネットビューの表示で確認する条件確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Z NetViewの Workload 機能と DSI633I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では Workload 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Lifeline Agents Workspace {#c32-i3792}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Lifeline Agents Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.90) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.90)

??? question "確認問題（1問）"
    **問題.** 区切確認のユーザーズガイド 操作で Workload 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Workload 機能の出力を取らず区切確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、区切確認の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して区切確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Workload 機能 は「区切確認のユーザーズガイド 操作に関係する定義値と表示行を照合する区切確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Workload 機能の属性行と DSI633I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Workload 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Servers Attributes {#c32-i3793}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Servers Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.188) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.188)

??? question "確認問題（1問）"
    **問題.** 範囲確認のユーザーズガイド 操作でネットビューの運用確認を行います。Workload 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲確認として引き継ぐ。 ✅
    - D. Workload 機能の属性行を読まず範囲確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Workload 機能 は「IBM Z NetViewで Workload 機能の扱いを記録する範囲確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Workload 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Workload 機能の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Servers Workspace {#c32-i3794}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Servers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.91) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.91)

??? question "確認問題（1問）"
    **問題.** 優先確認のユーザーズガイド 操作に関する Workload 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Workload 機能の変更点を出力本文から切り離して優先確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先確認の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Workload 機能 は「Workload 機能の状態と出力メッセージを結び付ける優先確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Workload 機能の出力行と DSI633I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Workload 機能を IBM Z NetViewの確認記録に残し、対象名は優先確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Site Details Workspace {#c32-i3795}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Site Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.92) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.92)

??? question "確認問題（1問）"
    **問題.** 記録確認のユーザーズガイド 操作に関係する Workload 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、記録確認の点検結果を残す。 ✅
    - B. Workload 機能の名称と担当者名のみを残して記録確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Workload 機能 は「Workload 機能の用途をネットビューの表示で確認する記録確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewの Workload 機能と DSI633I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Workload 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Sites Attributes {#c32-i3796}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Sites Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.191) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.191)

??? question "確認問題（1問）"
    **問題.** 比較確認のユーザーズガイド 操作で Workload 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Workload 機能の出力を取らず比較確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較確認で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して比較確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Workload 機能 は「比較確認のユーザーズガイド 操作に関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Workload 機能の属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Workload 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workload Sites Workspace {#c32-i3797}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workload Sites Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.93) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.93)

??? question "確認問題（1問）"
    **問題.** 順序確認のユーザーズガイド 操作でネットビューの運用確認を行います。Workload 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序確認の確認値として扱う。 ✅
    - D. Workload 機能の属性行を読まず順序確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Workload 機能 は「IBM Z NetViewで Workload 機能の扱いを記録する順序確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Workload 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Workload 機能の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workloads Attributes {#c32-i3798}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workloads Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.191) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.191)

??? question "確認問題（1問）"
    **問題.** 値域確認のユーザーズガイド 操作に関する Workloads 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Workloads 機能の変更点を出力本文から切り離して値域確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域確認の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Workloads 機能 は「Workloads 機能の状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Workloads 機能の出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Workloads 機能を IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workloads Workspace {#c32-i3799}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workloads Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.94) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.94)

??? question "確認問題（1問）"
    **問題.** 警告確認のユーザーズガイド 操作に関係する Workloads 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を警告確認で確認する。 ✅
    - B. Workloads 機能の名称と担当者名のみを残して警告確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Workloads 機能 は「Workloads 機能の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの Workloads 機能と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Workloads 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workspace Overview {#c32-i3800}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workspace Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.20) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.20)

??? question "確認問題（1問）"
    **問題.** 復旧確認のユーザーズガイド 操作で Workspace Overviewの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Workspace Overviewの出力を取らず復旧確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、復旧確認の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Workspace Overview は「復旧確認のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Workspace Overviewの属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Workspace Overviewを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Workspaces and Attribute Groups {#c32-i3801}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Workspaces and Attribute Groupsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.195) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.195)

??? question "確認問題（1問）"
    **問題.** 監査確認のユーザーズガイド 操作でネットビューの運用確認を行います。Workspaces 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査確認の確認記録にまとめる。 ✅
    - D. Workspaces 機能の属性行を読まず監査確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Workspaces 機能 は「IBM Z NetViewで Workspaces 機能の扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Workspaces 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Workspaces 機能の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### action ELEMENT {#c32-i3802}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

action ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Customization_Guide.pdf p.97 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Customization_Guide.pdf p.97

??? question "確認問題（1問）"
    **問題.** 記録検分のユーザーズガイド 操作に関係するaction ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録検分の結果として保存する。 ✅
    - B. action ELEMENT の名称と担当者名のみを残して記録検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠ではaction ELEMENT は「action ELEMENT の用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewのaction ELEMENT と DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語ではaction ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Customization_Guide.pdf p.97



### admin ELEMENT {#c32-i3803}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

'admin ELEMENT' (Lv2: ユーザーズガイド (操作)) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換確認のユーザーズガイド 操作に関するadmin ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. admin ELEMENT の変更点を出力本文から切り離して置換確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、置換確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠ではadmin ELEMENT は「admin ELEMENT の状態と出力メッセージを結び付ける置換確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存ではadmin ELEMENT の出力行と DSI633I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象ではadmin ELEMENT を IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### aggPri ELEMENT {#c32-i3804}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

'aggPri ELEMENT' (Lv2: ユーザーズガイド (操作)) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索確認のユーザーズガイド 操作でaggPri ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. aggPri ELEMENT の出力を取らず探索確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索確認の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して探索確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠ではaggPri ELEMENT は「探索確認のユーザーズガイド 操作に関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡ではaggPri ELEMENT の属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出ではaggPri ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### aggregation ELEMENT {#c32-i3805}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

aggregation ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。NetView_6.4_Data_Model_Reference.pdf p.23 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Data_Model_Reference.pdf p.23

??? question "確認問題（1問）"
    **問題.** 上書確認のユーザーズガイド 操作でネットビューの運用確認を行います。aggregation 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書確認の根拠を固定する。 ✅
    - D. aggregation 機能の属性行を読まず上書確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠ではaggregation 機能 は「IBM Z NetViewでaggregation 機能の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡ではaggregation 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料ではaggregation 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Data_Model_Reference.pdf p.23



### auditEntry ELEMENT {#c32-i3806}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

'auditEntry ELEMENT' (Lv2: ユーザーズガイド (操作)) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出照合のユーザーズガイド 操作でネットビューの運用確認を行います。auditEntry ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出照合のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出照合の根拠にする。 ✅
    - D. auditEntry ELEMENT の属性行を読まず呼出照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠ではauditEntry ELEMENT は「IBM Z NetViewでauditEntry ELEMENT の扱いを記録する呼出照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡ではauditEntry ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料ではauditEntry ELEMENT の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### auditLog ELEMENT {#c32-i3807}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

'auditLog ELEMENT' (Lv2: ユーザーズガイド (操作)) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索照合のユーザーズガイド 操作でauditLog ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. auditLog ELEMENT の出力を取らず探索照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索照合として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して探索照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠ではauditLog ELEMENT は「探索照合のユーザーズガイド 操作に関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡ではauditLog ELEMENT の属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出ではauditLog ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### cmd ELEMENT {#c32-i3808}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

cmd ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。NetView_6.4_Automation_Guide.pdf p.240 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** NetView_6.4_Automation_Guide.pdf p.240

??? question "確認問題（1問）"
    **問題.** 条件追跡のユーザーズガイド 操作に関係するcmd ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、条件追跡の採否を説明欄に結び付ける。 ✅
    - B. cmd ELEMENT の名称と担当者名のみを残して条件追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠ではcmd ELEMENT は「cmd ELEMENT の用途をネットビューの表示で確認する条件追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では IBM Z NetViewのcmd ELEMENT と DSI633I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語ではcmd ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** NetView_6.4_Automation_Guide.pdf p.240



### cmdResp ELEMENT {#c32-i3809}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

'cmdResp ELEMENT' (Lv2: ユーザーズガイド (操作)) は IBM NetView 6.4 マニュアル群の見出しだが、本バッチの 検索コーパスに該当チャンクなし。 実機検証時は NetView 6.4 マニュアル本文の直接参照が必要 (※ 要実機確認)

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切追跡のユーザーズガイド 操作でcmdResp ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. cmdResp ELEMENT の出力を取らず区切追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切追跡として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して区切追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠ではcmdResp ELEMENT は「区切追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する区切追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡ではcmdResp ELEMENT の属性行と DSI633I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出ではcmdResp ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### command ELEMENT {#c32-i3810}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

command ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.152) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.152)

??? question "確認問題（1問）"
    **問題.** 優先追跡のユーザーズガイド 操作に関するcommand ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. command ELEMENT の変更点を出力本文から切り離して優先追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、優先追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠ではcommand ELEMENT は「command ELEMENT の状態と出力メッセージを結び付ける優先追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存ではcommand ELEMENT の出力行と DSI633I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象ではcommand ELEMENT を IBM Z NetViewの確認記録に残し、対象名は優先追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### config {#c32-i3811}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

configは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.109) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.109)

??? question "確認問題（1問）"
    **問題.** 順序追跡のユーザーズガイド 操作でネットビューの運用確認を行います。configの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序追跡の根拠を固定する。 ✅
    - D. configの属性行を読まず順序追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠ではconfig は「IBM Z NetViewでconfigの扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡ではconfigの表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料ではconfigの使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### corrId ELEMENT {#c32-i3812}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

corrId ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.153) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.153)

??? question "確認問題（1問）"
    **問題.** 範囲検査のユーザーズガイド 操作でネットビューの運用確認を行います。corrId ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検査のユーザーズガイド 操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲検査の根拠にする。 ✅
    - D. corrId ELEMENT の属性行を読まず範囲検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠ではcorrId ELEMENT は「IBM Z NetViewでcorrId ELEMENT の扱いを記録する範囲検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡ではcorrId ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料ではcorrId ELEMENT の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### cpe ELEMENT {#c32-i3813}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

cpe ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.153) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.153)

??? question "確認問題（1問）"
    **問題.** 優先検査のユーザーズガイド 操作に関するcpe ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. cpe ELEMENT の変更点を出力本文から切り離して優先検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、優先検査の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠ではcpe ELEMENT は「cpe ELEMENT の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存ではcpe ELEMENT の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象ではcpe ELEMENT を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### cpebatch {#c32-i3814}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

cpebatchは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.109) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.109)

??? question "確認問題（1問）"
    **問題.** 記録検査のユーザーズガイド 操作に関係するcpebatchの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、記録検査の採否を説明欄に結び付ける。 ✅
    - B. cpebatchの名称と担当者名のみを残して記録検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠ではcpebatch は「cpebatchの用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewのcpebatchと DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語ではcpebatchを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### date ELEMENT {#c32-i3815}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

date ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.153) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.153)

??? question "確認問題（1問）"
    **問題.** 置換判定のユーザーズガイド 操作に関するdate ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. date ELEMENT の変更点を出力本文から切り離して置換判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、置換判定の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠ではdate ELEMENT は「date ELEMENT の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存ではdate ELEMENT の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象ではdate ELEMENT を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### dbtransfer {#c32-i3816}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

dbtransferは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.111) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.111)

??? question "確認問題（1問）"
    **問題.** 範囲判定のユーザーズガイド 操作でネットビューの運用確認を行います。dbtransferの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲判定の根拠を固定する。 ✅
    - D. dbtransferの属性行を読まず範囲判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠ではdbtransfer は「IBM Z NetViewでdbtransferの扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡ではdbtransferの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料ではdbtransferの使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### extSearch ELEMENT {#c32-i3817}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

extSearch ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.153) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.153)

??? question "確認問題（1問）"
    **問題.** 区切検分のユーザーズガイド 操作でextSearch ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. extSearch ELEMENT の出力を取らず区切検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切検分の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して区切検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠ではextSearch ELEMENT は「区切検分のユーザーズガイド 操作に関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡ではextSearch ELEMENT の属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出ではextSearch ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### flag ELEMENT {#c32-i3818}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

flag ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.154) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.154)

??? question "確認問題（1問）"
    **問題.** 上書確認のユーザーズガイド 操作でネットビューの運用確認を行います。flag ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を上書確認で確認する。 ✅
    - D. flag ELEMENT の属性行を読まず上書確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠ではflag ELEMENT は「IBM Z NetViewでflag ELEMENT の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡ではflag ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料ではflag ELEMENT の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### flagMask ELEMENT {#c32-i3819}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

flagMask ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.154) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.154)

??? question "確認問題（1問）"
    **問題.** 出力確認のユーザーズガイド 操作に関するflagMask ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. flagMask ELEMENT の変更点を出力本文から切り離して出力確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、出力確認の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠ではflagMask ELEMENT は「flagMask ELEMENT の状態と出力メッセージを結び付ける出力確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存ではflagMask ELEMENT の出力行と DSI633I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象ではflagMask ELEMENT を IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### flagValue ELEMENT {#c32-i3820}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

flagValue ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.154) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.154)

??? question "確認問題（1問）"
    **問題.** 条件確認のユーザーズガイド 操作に関係するflagValue ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件確認の確認記録にまとめる。 ✅
    - B. flagValue ELEMENT の名称と担当者名のみを残して条件確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠ではflagValue ELEMENT は「flagValue ELEMENT の用途をネットビューの表示で確認する条件確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Z NetViewのflagValue ELEMENT と DSI633I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語ではflagValue ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### fromHostname ELEMENT {#c32-i3821}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

fromHostname ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.155) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.155)

??? question "確認問題（1問）"
    **問題.** 記録確認のユーザーズガイド 操作に関係するfromHostname 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録確認として引き継ぐ。 ✅
    - B. fromHostname 機能の名称と担当者名のみを残して記録確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠ではfromHostname 機能 は「fromHostname 機能の用途をネットビューの表示で確認する記録確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewのfromHostname 機能と DSI633I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語ではfromHostname 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### fromId ELEMENT {#c32-i3822}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

fromId ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.155) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.155)

??? question "確認問題（1問）"
    **問題.** 比較確認のユーザーズガイド 操作でfromId ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. fromId ELEMENT の出力を取らず比較確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較確認の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して比較確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠ではfromId ELEMENT は「比較確認のユーザーズガイド 操作に関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡ではfromId ELEMENT の属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出ではfromId ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### fromIpAddr ELEMENT {#c32-i3823}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

fromIpAddr ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.155) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.155)

??? question "確認問題（1問）"
    **問題.** 順序確認のユーザーズガイド 操作でネットビューの運用確認を行います。fromIpAddr ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序確認のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、順序確認の点検結果を残す。 ✅
    - D. fromIpAddr ELEMENT の属性行を読まず順序確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠ではfromIpAddr ELEMENT は「IBM Z NetViewでfromIpAddr ELEMENT の扱いを記録する順序確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡ではfromIpAddr ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料ではfromIpAddr ELEMENT の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### getpd {#c32-i3824}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

getpdは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.111) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.111)

??? question "確認問題（1問）"
    **問題.** 監査確認のユーザーズガイド 操作でネットビューの運用確認を行います。getpdの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を監査確認で確認する。 ✅
    - D. getpdの属性行を読まず監査確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠ではgetpd は「IBM Z NetViewでgetpdの扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡ではgetpdの表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料ではgetpdの使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### hostcmd {#c32-i3825}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

hostcmdは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.112) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.112)

??? question "確認問題（1問）"
    **問題.** 区切照合のユーザーズガイド 操作でhostcmdの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. hostcmdの出力を取らず区切照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切照合の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して区切照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠ではhostcmd は「区切照合のユーザーズガイド 操作に関係する定義値と表示行を照合する区切照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡ではhostcmdの属性行と DSI633I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出ではhostcmdを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### hostcmdoper {#c32-i3826}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

hostcmdoperは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.113) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.113)

??? question "確認問題（1問）"
    **問題.** 範囲照合のユーザーズガイド 操作でネットビューの運用確認を行います。hostcmdoperの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲照合のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を範囲照合で確認する。 ✅
    - D. hostcmdoperの属性行を読まず範囲照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠ではhostcmdoper は「IBM Z NetViewでhostcmdoperの扱いを記録する範囲照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡ではhostcmdoperの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料ではhostcmdoperの使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### hostname ELEMENT {#c32-i3827}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

hostname ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.155) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.155)

??? question "確認問題（1問）"
    **問題.** 優先照合のユーザーズガイド 操作に関するhostname ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. hostname ELEMENT の変更点を出力本文から切り離して優先照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、優先照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠ではhostname ELEMENT は「hostname ELEMENT の状態と出力メッセージを結び付ける優先照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存ではhostname ELEMENT の出力行と DSI633I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象ではhostname ELEMENT を IBM Z NetViewの確認記録に残し、対象名は優先照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### id ELEMENT {#c32-i3828}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

id ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.156) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.156)

??? question "確認問題（1問）"
    **問題.** 置換追跡のユーザーズガイド 操作に関するid ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. id ELEMENT の変更点を出力本文から切り離して置換追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、置換追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠ではid ELEMENT は「id ELEMENT の状態と出力メッセージを結び付ける置換追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存ではid ELEMENT の出力行と DSI633I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象ではid ELEMENT を IBM Z NetViewの確認記録に残し、対象名は置換追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ihszfmt {#c32-i3829}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

ihszfmtは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.114) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.114)

??? question "確認問題（1問）"
    **問題.** 出力追跡のユーザーズガイド 操作に関するihszfmtの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. ihszfmtの変更点を出力本文から切り離して出力追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、出力追跡の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠ではihszfmt は「ihszfmtの状態と出力メッセージを結び付ける出力追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存ではihszfmtの出力行と DSI633I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象ではihszfmtを IBM Z NetViewの確認記録に残し、対象名は出力追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ihszset {#c32-i3830}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

ihszsetは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.114) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.114)

??? question "確認問題（1問）"
    **問題.** 条件追跡のユーザーズガイド 操作に関係するihszsetの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件追跡として引き継ぐ。 ✅
    - B. ihszsetの名称と担当者名のみを残して条件追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠ではihszset は「ihszsetの用途をネットビューの表示で確認する条件追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では IBM Z NetViewのihszsetと DSI633I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語ではihszsetを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ihszsett {#c32-i3831}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

ihszsettは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.115) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.115)

??? question "確認問題（1問）"
    **問題.** 区切追跡のユーザーズガイド 操作でihszsettの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ihszsettの出力を取らず区切追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切追跡の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して区切追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠ではihszsett は「区切追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する区切追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡ではihszsettの属性行と DSI633I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出ではihszsettを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### initRes ELEMENT {#c32-i3832}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

initRes ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.156) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.156)

??? question "確認問題（1問）"
    **問題.** 置換検査のユーザーズガイド 操作に関するinitRes ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. initRes ELEMENT の変更点を出力本文から切り離して置換検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検査で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠ではinitRes ELEMENT は「initRes ELEMENT の状態と出力メッセージを結び付ける置換検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存ではinitRes ELEMENT の出力行と DSI633I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象ではinitRes ELEMENT を IBM Z NetViewの確認記録に残し、対象名は置換検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ipAddr ELEMENT {#c32-i3833}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

ipAddr ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.156) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.156)

??? question "確認問題（1問）"
    **問題.** 値域検査のユーザーズガイド 操作に関するipAddr ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. ipAddr ELEMENT の変更点を出力本文から切り離して値域検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検査で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠ではipAddr ELEMENT は「ipAddr ELEMENT の状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存ではipAddr ELEMENT の出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象ではipAddr ELEMENT を IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### locRes Java Class {#c32-i3834}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

locRes Java Classは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.143) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.143)

??? question "確認問題（1問）"
    **問題.** 値域判定のユーザーズガイド 操作に関するlocRes Java Classの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. locRes Java Classの変更点を出力本文から切り離して値域判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、値域判定の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠ではlocRes Java Class は「locRes Java Classの状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存ではlocRes Java Classの出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象ではlocRes Java Classを IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### locateName ELEMENT {#c32-i3835}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

locateName ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.156) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.156)

??? question "確認問題（1問）"
    **問題.** 順序判定のユーザーズガイド 操作でネットビューの運用確認を行います。locateName ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、順序判定の結果として保存する。 ✅
    - D. locateName ELEMENT の属性行を読まず順序判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠ではlocateName ELEMENT は「IBM Z NetViewでlocateName ELEMENT の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡ではlocateName ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料ではlocateName ELEMENT の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### lu62name ELEMENT {#c32-i3836}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

lu62name ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.157) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.157)

??? question "確認問題（1問）"
    **問題.** 復旧判定のユーザーズガイド 操作でlu62name ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. lu62name ELEMENT の出力を取らず復旧判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧判定の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠ではlu62name ELEMENT は「復旧判定のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡ではlu62name ELEMENT の属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出ではlu62name ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### menuText ELEMENT {#c32-i3837}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

menuText ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.157) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.157)

??? question "確認問題（1問）"
    **問題.** 順序整理のユーザーズガイド 操作でネットビューの運用確認を行います。menuText ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を順序整理で確認する。 ✅
    - D. menuText ELEMENT の属性行を読まず順序整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠ではmenuText ELEMENT は「IBM Z NetViewでmenuText ELEMENT の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡ではmenuText ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料ではmenuText ELEMENT の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### msg ELEMENT {#c32-i3838}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

msg ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView Management Console (p.158) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.158)

??? question "確認問題（1問）"
    **問題.** 範囲記録のユーザーズガイド 操作でネットビューの運用確認を行います。msg ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、範囲記録の結果として保存する。 ✅
    - D. msg ELEMENT の属性行を読まず範囲記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠ではmsg ELEMENT は「IBM Z NetViewでmsg ELEMENT の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡ではmsg ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料ではmsg ELEMENT の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### netconv ELEMENT {#c32-i3839}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

netconv ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.158) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.158)

??? question "確認問題（1問）"
    **問題.** 復旧記録のユーザーズガイド 操作でnetconv ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. netconv ELEMENT の出力を取らず復旧記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧記録の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠ではnetconv ELEMENT は「復旧記録のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡ではnetconv ELEMENT の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出ではnetconv ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### nmcConsole ELEMENT {#c32-i3840}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

nmcConsole ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.158) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.158)

??? question "確認問題（1問）"
    **問題.** 構文読解のユーザーズガイド 操作に関係するnmcConsole ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文読解の確認値として扱う。 ✅
    - B. nmcConsole ELEMENT の名称と担当者名のみを残して構文読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠ではnmcConsole ELEMENT は「nmcConsole ELEMENT の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewのnmcConsole ELEMENT と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語ではnmcConsole ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### nmcRunning Java Class {#c32-i3841}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

nmcRunning Java Classは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.144) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.144)

??? question "確認問題（1問）"
    **問題.** 展開読解のユーザーズガイド 操作でnmcRunning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. nmcRunning 機能の出力を取らず展開読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開読解の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して展開読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠ではnmcRunning 機能 は「展開読解のユーザーズガイド 操作に関係する定義値と表示行を照合する展開読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡ではnmcRunning 機能の属性行と DSI633I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出ではnmcRunning 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### nmcServer ELEMENT {#c32-i3842}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

nmcServer ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.159) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.159)

??? question "確認問題（1問）"
    **問題.** 呼出読解のユーザーズガイド 操作でネットビューの運用確認を行います。nmcServer ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出読解のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を呼出読解で確認する。 ✅
    - D. nmcServer ELEMENT の属性行を読まず呼出読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠ではnmcServer ELEMENT は「IBM Z NetViewでnmcServer ELEMENT の扱いを記録する呼出読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡ではnmcServer ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料ではnmcServer ELEMENT の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### note ELEMENT {#c32-i3843}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

note ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換読解のユーザーズガイド 操作に関するnote ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. note ELEMENT の変更点を出力本文から切り離して置換読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、置換読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠ではnote ELEMENT は「note ELEMENT の状態と出力メッセージを結び付ける置換読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存ではnote ELEMENT の出力行と DSI633I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象ではnote ELEMENT を IBM Z NetViewの確認記録に残し、対象名は置換読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### noteMask ELEMENT {#c32-i3844}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

noteMask ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.159) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.159)

??? question "確認問題（1問）"
    **問題.** 終端読解のユーザーズガイド 操作に関係するnoteMask ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端読解の確認記録にまとめる。 ✅
    - B. noteMask ELEMENT の名称と担当者名のみを残して終端読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠ではnoteMask ELEMENT は「noteMask ELEMENT の用途をネットビューの表示で確認する終端読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM Z NetViewのnoteMask ELEMENT と DSI633I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語ではnoteMask ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### nvDomain Element {#c32-i3845}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

nvDomain Elementは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.159) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.159)

??? question "確認問題（1問）"
    **問題.** 条件読解のユーザーズガイド 操作に関係するnvDomain Elementの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件読解として引き継ぐ。 ✅
    - B. nvDomain Elementの名称と担当者名のみを残して条件読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠ではnvDomain Element は「nvDomain Elementの用途をネットビューの表示で確認する条件読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM Z NetViewのnvDomain Elementと DSI633I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語ではnvDomain Elementを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### res ELEMENT {#c32-i3846}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

res ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.160) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.160)

??? question "確認問題（1問）"
    **問題.** 展開確認のユーザーズガイド 操作でres ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. res ELEMENT の出力を取らず展開確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、展開確認の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して展開確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠ではres ELEMENT は「展開確認のユーザーズガイド 操作に関係する定義値と表示行を照合する展開確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡ではres ELEMENT の属性行と DSI633I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出ではres ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### rodmId ELEMENT {#c32-i3847}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

rodmId ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide NetView Management Console (p.160) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.160)

??? question "確認問題（1問）"
    **問題.** 終端確認のユーザーズガイド 操作に関係するrodmId ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端確認の根拠を固定する。 ✅
    - B. rodmId ELEMENT の名称と担当者名のみを残して終端確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. EKG000I の有無を見ず終端確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠ではrodmId ELEMENT は「rodmId ELEMENT の用途をネットビューの表示で確認する終端確認項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Z NetViewのrodmId ELEMENT と EKG000I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語ではrodmId ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### sendMsg ELEMENT {#c32-i3848}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

sendMsg ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView Management Console (p.160) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.160)

??? question "確認問題（1問）"
    **問題.** 復旧確認のユーザーズガイド 操作でsendMsg ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. sendMsg ELEMENT の出力を取らず復旧確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を復旧確認で確認する。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠ではsendMsg ELEMENT は「復旧確認のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡ではsendMsg ELEMENT の属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出ではsendMsg ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### service {#c32-i3849}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

serviceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.115) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.115)

??? question "確認問題（1問）"
    **問題.** 監査確認のユーザーズガイド 操作でネットビューの運用確認を行います。serviceの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査確認のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、監査確認の証跡として残す。 ✅
    - D. serviceの属性行を読まず監査確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠ではservice は「IBM Z NetViewでserviceの扱いを記録する監査確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡ではserviceの表示結果と DSI633I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料ではserviceの使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### start {#c32-i3850}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

startは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.116) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.116)

??? question "確認問題（1問）"
    **問題.** 復旧追跡のユーザーズガイド 操作でstartの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. startの出力を取らず復旧追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、復旧追跡の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して復旧追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠ではstart は「復旧追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡ではstartの属性行と DSI633I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出ではstartを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### stop {#c32-i3851}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

stopは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.117) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.117)

??? question "確認問題（1問）"
    **問題.** 探索検査のユーザーズガイド 操作でstopの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. stopの出力を取らず探索検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を探索検査で確認する。 ✅
    - C. BROWSE CANZLOG を省略して探索検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠ではstop は「探索検査のユーザーズガイド 操作に関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡ではstopの属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出ではstopを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### tappxx {#c32-i3852}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

tappxxは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.123) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.123)

??? question "確認問題（1問）"
    **問題.** 順序検査のユーザーズガイド 操作でネットビューの運用確認を行います。tappxxの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序検査で再確認できる形にする。 ✅
    - D. tappxxの属性行を読まず順序検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠ではtappxx は「IBM Z NetViewでtappxxの扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡ではtappxxの表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料ではtappxxの使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### tconsolexx {#c32-i3853}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

tconsolexxは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.121) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.121)

??? question "確認問題（1問）"
    **問題.** 値域検査のユーザーズガイド 操作に関するtconsolexxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. tconsolexxの変更点を出力本文から切り離して値域検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域検査の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠ではtconsolexx は「tconsolexxの状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存ではtconsolexxの出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象ではtconsolexxを IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### tcpipkey {#c32-i3854}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

tcpipkeyは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.117) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.117)

??? question "確認問題（1問）"
    **問題.** 終端判定のユーザーズガイド 操作に関係するtcpipkeyの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端判定の確認にする。 ✅
    - B. tcpipkeyの名称と担当者名のみを残して終端判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠ではtcpipkey は「tcpipkeyの用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewのtcpipkeyと DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語ではtcpipkeyを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### thresholdDeg ELEMENT {#c32-i3855}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

thresholdDeg ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.160) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.160)

??? question "確認問題（1問）"
    **問題.** 範囲判定のユーザーズガイド 操作でネットビューの運用確認を行います。thresholdDeg 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、範囲判定の証跡として残す。 ✅
    - D. thresholdDeg 機能の属性行を読まず範囲判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠ではthresholdDeg 機能 は「IBM Z NetViewでthresholdDeg 機能の扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡ではthresholdDeg 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料ではthresholdDeg 機能の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### thresholdSevDeg ELEMENT {#c32-i3856}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

thresholdSevDeg ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.161) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.161)

??? question "確認問題（1問）"
    **問題.** 優先判定のユーザーズガイド 操作に関するthresholdSevDeg 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. thresholdSevDeg 機能の変更点を出力本文から切り離して優先判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先判定の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠ではthresholdSevDeg 機能 は「thresholdSevDeg 機能の状態と出力メッセージを結び付ける優先判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存ではthresholdSevDeg 機能の出力行と DSI633I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象ではthresholdSevDeg 機能を IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### thresholdUnsat ELEMENT {#c32-i3857}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

thresholdUnsat ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.161) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.161)

??? question "確認問題（1問）"
    **問題.** 記録判定のユーザーズガイド 操作に関係するthresholdUnsat 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録判定の根拠にする。 ✅
    - B. thresholdUnsat 機能の名称と担当者名のみを残して記録判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠ではthresholdUnsat 機能 は「thresholdUnsat 機能の用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewのthresholdUnsat 機能と DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語ではthresholdUnsat 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### tlocResxx Script {#c32-i3858}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

tlocResxx Scriptは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.145) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.145)

??? question "確認問題（1問）"
    **問題.** 順序判定のユーザーズガイド 操作でネットビューの運用確認を行います。tlocResxx Scriptの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序判定の採否を説明欄に結び付ける。 ✅
    - D. tlocResxx Scriptの属性行を読まず順序判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠ではtlocResxx Script は「IBM Z NetViewでtlocResxx Scriptの扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡ではtlocResxx Scriptの表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料ではtlocResxx Scriptの使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### toHostname ELEMENT {#c32-i3859}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

toHostname ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.161) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.161)

??? question "確認問題（1問）"
    **問題.** 警告判定のユーザーズガイド 操作に関係するtoHostname ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告判定の確認にする。 ✅
    - B. toHostname ELEMENT の名称と担当者名のみを残して警告判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠ではtoHostname ELEMENT は「toHostname ELEMENT の用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewのtoHostname ELEMENT と DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語ではtoHostname ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### toId ELEMENT {#c32-i3860}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

toId ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.161) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.161)

??? question "確認問題（1問）"
    **問題.** 復旧判定のユーザーズガイド 操作でtoId ELEMENT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. toId ELEMENT の出力を取らず復旧判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧判定の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠ではtoId ELEMENT は「復旧判定のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡ではtoId ELEMENT の属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出ではtoId ELEMENT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### toIpAddr ELEMENT {#c32-i3861}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

toIpAddr ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.162) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.162)

??? question "確認問題（1問）"
    **問題.** 監査判定のユーザーズガイド 操作でネットビューの運用確認を行います。toIpAddr ELEMENT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査判定で再確認できる形にする。 ✅
    - D. toIpAddr ELEMENT の属性行を読まず監査判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠ではtoIpAddr ELEMENT は「IBM Z NetViewでtoIpAddr ELEMENT の扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡ではtoIpAddr ELEMENT の表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料ではtoIpAddr ELEMENT の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### tserver {#c32-i3862}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

tserverは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.118) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.118)

??? question "確認問題（1問）"
    **問題.** 終端整理のユーザーズガイド 操作に関係するtserverの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端整理の根拠にする。 ✅
    - B. tserverの名称と担当者名のみを残して終端整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠ではtserver は「tserverの用途をネットビューの表示で確認する終端整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewのtserverと DSI633I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語ではtserverを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### utility {#c32-i3863}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

utilityは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.119) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.119)

??? question "確認問題（1問）"
    **問題.** 上書検分のユーザーズガイド 操作でネットビューの運用確認を行います。utilityの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、上書検分の証跡として残す。 ✅
    - D. utilityの属性行を読まず上書検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠ではutility は「IBM Z NetViewでutilityの扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡ではutilityの表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料ではutilityの使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### viewCust ELEMENT {#c32-i3864}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

viewCust ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.162) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.162)

??? question "確認問題（1問）"
    **問題.** 出力検分のユーザーズガイド 操作に関するviewCust ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. viewCust ELEMENT の変更点を出力本文から切り離して出力検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力検分の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠ではviewCust ELEMENT は「viewCust ELEMENT の状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存ではviewCust ELEMENT の出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象ではviewCust ELEMENT を IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### viewName ELEMENT {#c32-i3865}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

viewName ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.162) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.162)

??? question "確認問題（1問）"
    **問題.** 優先検分のユーザーズガイド 操作に関するviewName ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. viewName ELEMENT の変更点を出力本文から切り離して優先検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先検分として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠ではviewName ELEMENT は「viewName ELEMENT の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存ではviewName ELEMENT の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象ではviewName ELEMENT を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### viewNav ELEMENT {#c32-i3866}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

viewNav ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.163) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.163)

??? question "確認問題（1問）"
    **問題.** 記録検分のユーザーズガイド 操作に関係するviewNav ELEMENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録検分の確認にする。 ✅
    - B. viewNav ELEMENT の名称と担当者名のみを残して記録検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠ではviewNav ELEMENT は「viewNav ELEMENT の用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewのviewNav ELEMENT と DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語ではviewNav ELEMENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### viewType ELEMENT {#c32-i3867}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

viewType ELEMENTは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.163) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.163)

??? question "確認問題（1問）"
    **問題.** 値域検分のユーザーズガイド 操作に関するviewType ELEMENT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. viewType ELEMENT の変更点を出力本文から切り離して値域検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域検分の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠ではviewType ELEMENT は「viewType ELEMENT の状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存ではviewType ELEMENT の出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象ではviewType ELEMENT を IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### z/OS Workload Server Details Workspace {#c32-i3868}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

z/OS Workload Server Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.95) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.95)

??? question "確認問題（1問）"
    **問題.** 変更確認のz/OS Workload Server Details Workspaceに関するz 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更確認のz/OS Workload Server Details Workspaceの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のz/OS Workload Server Details Workspaceの証跡として保存して根拠にする。
    - C. z 属性の変更点を出力本文から切り離して変更確認のz/OS Workload Server Details Workspaceの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠ではz 属性 は「z 属性の状態と出力メッセージを結び付ける変更確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存ではz 属性の出力行と DSI633I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象ではz 属性を IBM Z NetViewの確認記録に残し、対象名は変更確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide




## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作) > ALERTSH

### ALERTSH {#c32-i3869}
*分類: ユーザーズガイド (操作) > ALERTSH*  ・  難易度: 中級

ALERTSHは、ハードウェア・モニターに記録された警報の履歴を表示するコマンドです。過去に発生した警報を時系列で振り返ります

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索整理のネットビューで ALERTSH の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ALERTSH の出力を取らず探索整理のネットビューの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索整理で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索整理のネットビューの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理のネットビューへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では ALERTSH は「探索整理のネットビューに関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では ALERTSH の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では ALERTSH を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作) > BROWSE CANZLOG

### BROWSE CANZLOG {#c32-i3870}
*分類: ユーザーズガイド (操作) > BROWSE CANZLOG*  ・  難易度: 初級

BROWSE CANZLOGは、監査とNetViewとz/OSのログを統合したCanzlogを表示するコマンドです。MVSメッセージやNetViewメッセージ、DOMをまとめて追えます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換整理のネットビューに関する BROWSE CANZLOG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理のネットビューの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理のネットビューの証跡として保存して根拠にする。
    - C. BROWSE CANZLOG の変更点を出力本文から切り離して置換整理のネットビューの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換整理の確認にする。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では BROWSE CANZLOG は「BROWSE CANZLOG の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では BROWSE CANZLOG の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では BROWSE CANZLOG を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作) > NPDA

### NPDA {#c32-i3871}
*分類: ユーザーズガイド (操作) > NPDA*  ・  難易度: 中級

NPDAは、ハードウェア・モニターの主メニューを開くコマンドです。ALDで動的な警報表示を呼び出し、障害の警報を確認します

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端整理のネットビューに関係する NPDA の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端整理の点検結果を残す。 ✅
    - B. NPDA の名称と担当者名のみを残して終端整理のネットビューの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理のネットビューを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず終端整理のネットビューの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では NPDA は「NPDA の用途をネットビューの表示で確認する終端整理項目」と NPDA または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの NPDA と BNH160I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では NPDA を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference




## Tivoli NetView z/OS 自動化 > 管理リファレンス

### %INCLUDE {#c32-i3872}
*分類: 管理リファレンス*  ・  難易度: 中級

%INCLUDEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.337) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.337)

??? question "確認問題（1問）"
    **問題.** 構文照合の%に関係する%INCLUDE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、構文照合の結果として保存する。 ✅
    - B. %INCLUDE の名称と担当者名のみを残して構文照合の%の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合の%を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合の%の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では%INCLUDE は「%INCLUDE の用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの%INCLUDE と DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では%INCLUDE を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### A (Alert) {#c32-i3873}
*分類: 管理リファレンス*  ・  難易度: 中級

A (Alert)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.295) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.295)

??? question "確認問題（1問）"
    **問題.** 展開照合の管理リファレンスで A (Alert)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. A (Alert)の出力を取らず展開照合の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、展開照合の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して展開照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では A (Alert) は「展開照合の管理リファレンスに関係する定義値と表示行を照合する展開照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では A (Alert)の属性行と DSI633I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では A (Alert)を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ACBpassword {#c32-i3874}
*分類: 管理リファレンス*  ・  難易度: 中級

ACBpasswordは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.31) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.31)

??? question "確認問題（1問）"
    **問題.** 呼出照合の管理リファレンスでネットビューの運用確認を行います。ACBpasswordの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出照合の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出照合として引き継ぐ。 ✅
    - D. ACBpasswordの属性行を読まず呼出照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では ACBpassword は「IBM Z NetViewで ACBpasswordの扱いを記録する呼出照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では ACBpasswordの表示結果と DSI633I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では ACBpasswordの使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ACCESS {#c32-i3875}
*分類: 管理リファレンス*  ・  難易度: 中級

ACCESSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.297) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.297)

??? question "確認問題（1問）"
    **問題.** 置換照合の管理リファレンスに関する ACCESS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の管理リファレンスの証跡として保存して根拠にする。
    - C. ACCESS の変更点を出力本文から切り離して置換照合の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換照合の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では ACCESS は「ACCESS の状態と出力メッセージを結び付ける置換照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では ACCESS の出力行と DSI633I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では ACCESS を IBM Z NetViewの確認記録に残し、対象名は置換照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ACTION {#c32-i3876}
*分類: 管理リファレンス*  ・  難易度: 中級

ACTIONは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.298) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.298)

??? question "確認問題（1問）"
    **問題.** 終端照合の管理リファレンスに関係する ACTION の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、終端照合の点検結果を残す。 ✅
    - B. ACTION の名称と担当者名のみを残して終端照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では ACTION は「ACTION の用途をネットビューの表示で確認する終端照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM Z NetViewの ACTION と DSI633I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では ACTION を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ACTMON {#c32-i3877}
*分類: 管理リファレンス*  ・  難易度: 中級

ACTMONは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.409) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.409)

??? question "確認問題（1問）"
    **問題.** 探索照合の管理リファレンスで ACTMON の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ACTMON の出力を取らず探索照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索照合で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して探索照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では ACTMON は「探索照合の管理リファレンスに関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では ACTMON の属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では ACTMON を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ALIASMEM {#c32-i3878}
*分類: 管理リファレンス*  ・  難易度: 中級

ALIASMEMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.299) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.299)

??? question "確認問題（1問）"
    **問題.** 区切照合の管理リファレンスで ALIASMEM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ALIASMEM の出力を取らず区切照合の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、区切照合の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して区切照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では ALIASMEM は「区切照合の管理リファレンスに関係する定義値と表示行を照合する区切照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では ALIASMEM の属性行と DSI633I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では ALIASMEM を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ALRTCFG {#c32-i3879}
*分類: 管理リファレンス*  ・  難易度: 中級

ALRTCFGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.498) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.498)

??? question "確認問題（1問）"
    **問題.** 範囲照合の管理リファレンスでネットビューの運用確認を行います。ALRTCFG の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲照合の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲照合の確認記録にまとめる。 ✅
    - D. ALRTCFG の属性行を読まず範囲照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では ALRTCFG は「IBM Z NetViewで ALRTCFG の扱いを記録する範囲照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では ALRTCFG の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では ALRTCFG の使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ALRTTCFG {#c32-i3880}
*分類: 管理リファレンス*  ・  難易度: 中級

ALRTTCFGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.498) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.498)

??? question "確認問題（1問）"
    **問題.** 優先照合の管理リファレンスに関する ALRTTCFG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の管理リファレンスの証跡として保存して根拠にする。
    - C. ALRTTCFG の変更点を出力本文から切り離して優先照合の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先照合の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では ALRTTCFG は「ALRTTCFG の状態と出力メッセージを結び付ける優先照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では ALRTTCFG の出力行と DSI633I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では ALRTTCFG を IBM Z NetViewの確認記録に残し、対象名は優先照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AMELINIT {#c32-i3881}
*分類: 管理リファレンス*  ・  難易度: 中級

AMELINITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.300) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.300)

??? question "確認問題（1問）"
    **問題.** 記録照合の管理リファレンスに関係する AMELINIT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、記録照合の結果として保存する。 ✅
    - B. AMELINIT の名称と担当者名のみを残して記録照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では AMELINIT は「AMELINIT の用途をネットビューの表示で確認する記録照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では IBM Z NetViewの AMELINIT と DSI633I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では AMELINIT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### API {#c32-i3882}
*分類: 管理リファレンス*  ・  難易度: 中級

APIは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.549) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.549)

??? question "確認問題（1問）"
    **問題.** 比較照合の管理リファレンスで API の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. API の出力を取らず比較照合の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、比較照合の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して比較照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では API は「比較照合の管理リファレンスに関係する定義値と表示行を照合する比較照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では API の属性行と DSI633I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では API を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### APSERV.PREFIX {#c32-i3883}
*分類: 管理リファレンス*  ・  難易度: 中級

APSERV.PREFIXは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.32) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.32)

??? question "確認問題（1問）"
    **問題.** 順序照合の管理リファレンスでネットビューの運用確認を行います。APSERV.PREFIX の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序照合の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序照合として引き継ぐ。 ✅
    - D. APSERV.PREFIX の属性行を読まず順序照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では APSERV.PREFIX は「IBM Z NetViewで APSERV.PREFIX の扱いを記録する順序照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では APSERV.PREFIX の表示結果と DSI633I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では APSERV.PREFIX の使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ARCHIVE.ACCESSDELAY {#c32-i3884}
*分類: 管理リファレンス*  ・  難易度: 中級

ARCHIVE.ACCESSDELAYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.33) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.33)

??? question "確認問題（1問）"
    **問題.** 値域照合の管理リファレンスに関する ARCHIVE 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の管理リファレンスの証跡として保存して根拠にする。
    - C. ARCHIVE 属性の変更点を出力本文から切り離して値域照合の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域照合の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では ARCHIVE 属性 は「ARCHIVE 属性の状態と出力メッセージを結び付ける値域照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では ARCHIVE 属性の出力行と DSI633I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では ARCHIVE 属性を IBM Z NetViewの確認記録に残し、対象名は値域照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ARCHIVE.HLQ {#c32-i3885}
*分類: 管理リファレンス*  ・  難易度: 中級

ARCHIVE.HLQは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.35) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.35)

??? question "確認問題（1問）"
    **問題.** 警告照合の管理リファレンスに関係する ARCHIVE.HLQ の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、警告照合の点検結果を残す。 ✅
    - B. ARCHIVE.HLQ の名称と担当者名のみを残して警告照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では ARCHIVE.HLQ は「ARCHIVE.HLQ の用途をネットビューの表示で確認する警告照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では IBM Z NetViewの ARCHIVE.HLQ と DSI633I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では ARCHIVE.HLQ を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ARCHIVE.WRITE {#c32-i3886}
*分類: 管理リファレンス*  ・  難易度: 中級

ARCHIVE.WRITEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.50) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.50)

??? question "確認問題（1問）"
    **問題.** 復旧照合の管理リファレンスで ARCHIVE.WRITE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ARCHIVE.WRITE の出力を取らず復旧照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧照合で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では ARCHIVE.WRITE は「復旧照合の管理リファレンスに関係する定義値と表示行を照合する復旧照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では ARCHIVE.WRITE の属性行と DSI633I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では ARCHIVE.WRITE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ASSIGN {#c32-i3887}
*分類: 管理リファレンス*  ・  難易度: 中級

ASSIGNは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.51) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.51)

??? question "確認問題（1問）"
    **問題.** 監査照合の管理リファレンスでネットビューの運用確認を行います。ASSIGN の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査照合の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査照合の確認値として扱う。 ✅
    - D. ASSIGN の属性行を読まず監査照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では ASSIGN は「IBM Z NetViewで ASSIGN の扱いを記録する監査照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では ASSIGN の表示結果と DSI633I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では ASSIGN の使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ASYNC_TASKS {#c32-i3888}
*分類: 管理リファレンス*  ・  難易度: 中級

ASYNC_TASKSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.527) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.527)

??? question "確認問題（1問）"
    **問題.** 変更照合の管理リファレンスに関する ASYNC_TASKS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の管理リファレンスの証跡として保存して根拠にする。
    - C. ASYNC_TASKS の変更点を出力本文から切り離して変更照合の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更照合の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では ASYNC_TASKS は「ASYNC_TASKS の状態と出力メッセージを結び付ける変更照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では ASYNC_TASKS の出力行と DSI633I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では ASYNC_TASKS を IBM Z NetViewの確認記録に残し、対象名は変更照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AUTH {#c32-i3889}
*分類: 管理リファレンス*  ・  難易度: 中級

AUTHは、Tivoli NetView z/OS 自動化の管理リファレンスで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Administration Reference (p.301) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.301)

??? question "確認問題（1問）"
    **問題.** 構文追跡の管理リファレンスに関係する AUTH の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を構文追跡で確認する。 ✅
    - B. AUTH の名称と担当者名のみを残して構文追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では AUTH は「AUTH の用途をネットビューの表示で確認する構文追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では IBM Z NetViewの AUTH と DSI633I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では AUTH を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AUTOCMD {#c32-i3890}
*分類: 管理リファレンス*  ・  難易度: 中級

AUTOCMDは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.52) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.52)

??? question "確認問題（2問）"
    **問題.** 展開追跡の管理リファレンスで AUTOCMD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AUTOCMD の出力を取らず展開追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、展開追跡の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して展開追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では AUTOCMD は「展開追跡の管理リファレンスに関係する定義値と表示行を照合する展開追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では AUTOCMD の属性行と DSI633I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では AUTOCMD を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide

    ---

    **問題.** 順序判定のネットビューでネットビューの運用確認を行います。AUTOCMD の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定のネットビューを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定のネットビューを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序判定の確認値として扱う。 ✅
    - D. AUTOCMD の属性行を読まず順序判定のネットビューの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では AUTOCMD は「IBM Z NetViewで AUTOCMD の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では AUTOCMD の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では AUTOCMD の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### AUTOOPS {#c32-i3891}
*分類: 管理リファレンス*  ・  難易度: 中級

AUTOOPSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.413) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.413)

??? question "確認問題（1問）"
    **問題.** 呼出追跡の管理リファレンスでネットビューの運用確認を行います。AUTOOPS の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出追跡の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出追跡の確認記録にまとめる。 ✅
    - D. AUTOOPS の属性行を読まず呼出追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では AUTOOPS は「IBM Z NetViewで AUTOOPS の扱いを記録する呼出追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では AUTOOPS の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では AUTOOPS の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AUTOTASK {#c32-i3892}
*分類: 管理リファレンス*  ・  難易度: 中級

AUTOTASKは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.53) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.53)

??? question "確認問題（1問）"
    **問題.** 置換追跡の管理リファレンスに関する AUTOTASK の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. AUTOTASK の変更点を出力本文から切り離して置換追跡の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換追跡の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では AUTOTASK は「AUTOTASK の状態と出力メッセージを結び付ける置換追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では AUTOTASK の出力行と DSI633I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では AUTOTASK を IBM Z NetViewの確認記録に残し、対象名は置換追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AUTOTEST.HLQ {#c32-i3893}
*分類: 管理リファレンス*  ・  難易度: 中級

AUTOTEST.HLQは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.54) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.54)

??? question "確認問題（1問）"
    **問題.** 終端追跡の管理リファレンスに関係する AUTOTEST.HLQ の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、終端追跡の結果として保存する。 ✅
    - B. AUTOTEST.HLQ の名称と担当者名のみを残して終端追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では AUTOTEST.HLQ は「AUTOTEST.HLQ の用途をネットビューの表示で確認する終端追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では IBM Z NetViewの AUTOTEST.HLQ と DSI633I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では AUTOTEST.HLQ を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AdapterCdsFile {#c32-i3894}
*分類: 管理リファレンス*  ・  難易度: 中級

AdapterCdsFileは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.495) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.495)

??? question "確認問題（1問）"
    **問題.** 上書照合の管理リファレンスでネットビューの運用確認を行います。AdapterCdsFileの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書照合の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書照合の確認値として扱う。 ✅
    - D. AdapterCdsFileの属性行を読まず上書照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では AdapterCdsFile は「IBM Z NetViewで AdapterCdsFileの扱いを記録する上書照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では AdapterCdsFileの表示結果と DSI633I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では AdapterCdsFileの使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AdapterFmtFile {#c32-i3895}
*分類: 管理リファレンス*  ・  難易度: 中級

AdapterFmtFileは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.497) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.497)

??? question "確認問題（1問）"
    **問題.** 出力照合の管理リファレンスに関する AdapterFmtFileの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の管理リファレンスの証跡として保存して根拠にする。
    - C. AdapterFmtFileの変更点を出力本文から切り離して出力照合の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力照合の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では AdapterFmtFile は「AdapterFmtFileの状態と出力メッセージを結び付ける出力照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では AdapterFmtFileの出力行と DSI633I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では AdapterFmtFileを IBM Z NetViewの確認記録に残し、対象名は出力照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### AlertRcvName {#c32-i3896}
*分類: 管理リファレンス*  ・  難易度: 中級

AlertRcvNameは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.31) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.31)

??? question "確認問題（1問）"
    **問題.** 条件照合の管理リファレンスに関係する AlertRcvNameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を条件照合で確認する。 ✅
    - B. AlertRcvNameの名称と担当者名のみを残して条件照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では AlertRcvName は「AlertRcvNameの用途をネットビューの表示で確認する条件照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では IBM Z NetViewの AlertRcvNameと DSI633I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では AlertRcvNameを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufEvtMaxSize {#c32-i3897}
*分類: 管理リファレンス*  ・  難易度: 中級

BufEvtMaxSizeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.499) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.499)

??? question "確認問題（1問）"
    **問題.** 出力追跡の管理リファレンスに関する BufEvtMaxSizeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. BufEvtMaxSizeの変更点を出力本文から切り離して出力追跡の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力追跡の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では BufEvtMaxSize は「BufEvtMaxSizeの状態と出力メッセージを結び付ける出力追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では BufEvtMaxSizeの出力行と DSI633I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では BufEvtMaxSizeを IBM Z NetViewの確認記録に残し、対象名は出力追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufEvtNegRespLimit {#c32-i3898}
*分類: 管理リファレンス*  ・  難易度: 中級

BufEvtNegRespLimitは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.500) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.500)

??? question "確認問題（1問）"
    **問題.** 条件追跡の管理リファレンスに関係する BufEvtNegRespLimitの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、条件追跡の点検結果を残す。 ✅
    - B. BufEvtNegRespLimitの名称と担当者名のみを残して条件追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では BufEvtNegRespLimit は「BufEvtNegRespLimitの用途をネットビューの表示で確認する条件追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では IBM Z NetViewの BufEvtNegRespLimitと DSI633I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では BufEvtNegRespLimitを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufEvtPath {#c32-i3899}
*分類: 管理リファレンス*  ・  難易度: 中級

BufEvtPathは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.501) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.501)

??? question "確認問題（1問）"
    **問題.** 区切追跡の管理リファレンスで BufEvtPathの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BufEvtPathの出力を取らず区切追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切追跡で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して区切追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では BufEvtPath は「区切追跡の管理リファレンスに関係する定義値と表示行を照合する区切追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では BufEvtPathの属性行と DSI633I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では BufEvtPathを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufEvtRdBlklen {#c32-i3900}
*分類: 管理リファレンス*  ・  難易度: 中級

BufEvtRdBlklenは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.501) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.501)

??? question "確認問題（1問）"
    **問題.** 範囲追跡の管理リファレンスでネットビューの運用確認を行います。BufEvtRdBlklenの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲追跡の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲追跡の確認値として扱う。 ✅
    - D. BufEvtRdBlklenの属性行を読まず範囲追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では BufEvtRdBlklen は「IBM Z NetViewで BufEvtRdBlklenの扱いを記録する範囲追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では BufEvtRdBlklenの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では BufEvtRdBlklenの使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufEvtShrinkSize {#c32-i3901}
*分類: 管理リファレンス*  ・  難易度: 中級

BufEvtShrinkSizeは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.502) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.502)

??? question "確認問題（1問）"
    **問題.** 優先追跡の管理リファレンスに関する BufEvtShrinkSizeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. BufEvtShrinkSizeの変更点を出力本文から切り離して優先追跡の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先追跡の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では BufEvtShrinkSize は「BufEvtShrinkSizeの状態と出力メッセージを結び付ける優先追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では BufEvtShrinkSizeの出力行と DSI633I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では BufEvtShrinkSizeを IBM Z NetViewの確認記録に残し、対象名は優先追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufferEvents {#c32-i3902}
*分類: 管理リファレンス*  ・  難易度: 中級

BufferEventsは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.503) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.503)

??? question "確認問題（1問）"
    **問題.** 記録追跡の管理リファレンスに関係する BufferEventsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を記録追跡で確認する。 ✅
    - B. BufferEventsの名称と担当者名のみを残して記録追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では BufferEvents は「BufferEventsの用途をネットビューの表示で確認する記録追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では IBM Z NetViewの BufferEventsと DSI633I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では BufferEventsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufferEventsLimit {#c32-i3903}
*分類: 管理リファレンス*  ・  難易度: 中級

BufferEventsLimitは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.503) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.503)

??? question "確認問題（1問）"
    **問題.** 比較追跡の管理リファレンスで BufferEventsLimitの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BufferEventsLimitの出力を取らず比較追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、比較追跡の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して比較追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では BufferEventsLimit は「比較追跡の管理リファレンスに関係する定義値と表示行を照合する比較追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では BufferEventsLimitの属性行と DSI633I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では BufferEventsLimitを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### BufferFlushRate {#c32-i3904}
*分類: 管理リファレンス*  ・  難易度: 中級

BufferFlushRateは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.504) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.504)

??? question "確認問題（1問）"
    **問題.** 順序追跡の管理リファレンスでネットビューの運用確認を行います。BufferFlushRateの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡の管理リファレンスを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序追跡の確認記録にまとめる。 ✅
    - D. BufferFlushRateの属性行を読まず順序追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では BufferFlushRate は「IBM Z NetViewで BufferFlushRateの扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では BufferFlushRateの表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では BufferFlushRateの使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### C (Command List) {#c32-i3905}
*分類: 管理リファレンス*  ・  難易度: 中級

C (Command List)は、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.305) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.305)

??? question "確認問題（1問）"
    **問題.** 値域追跡の管理リファレンスに関する C (Command List)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LIST CLIST の結果を残さず値域追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. C (Command List)の変更点を出力本文から切り離して値域追跡の管理リファレンスの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域追跡の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では C (Command List) は「C (Command List)の状態と出力メッセージを結び付ける値域追跡項目」と LIST CLIST または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では C (Command List)の出力行と DSI039I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では C (Command List)を IBM Z NetViewの確認記録に残し、対象名は値域追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CALRTCFG {#c32-i3906}
*分類: 管理リファレンス*  ・  難易度: 中級

CALRTCFGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.505) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.505)

??? question "確認問題（1問）"
    **問題.** 警告追跡の管理リファレンスに関係する CALRTCFG の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と DSI633I を読み、警告追跡の結果として保存する。 ✅
    - B. CALRTCFG の名称と担当者名のみを残して警告追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では CALRTCFG は「CALRTCFG の用途をネットビューの表示で確認する警告追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では IBM Z NetViewの CALRTCFG と DSI633I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では CALRTCFG を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CCDEF {#c32-i3907}
*分類: 管理リファレンス*  ・  難易度: 中級

CCDEFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.55) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.55)

??? question "確認問題（1問）"
    **問題.** 復旧追跡の管理リファレンスで CCDEF の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CCDEF の出力を取らず復旧追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG で得た表示本文を使い、復旧追跡の採否を説明欄に結び付ける。 ✅
    - C. BROWSE CANZLOG を省略して復旧追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では CCDEF は「復旧追跡の管理リファレンスに関係する定義値と表示行を照合する復旧追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では CCDEF の属性行と DSI633I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では CCDEF を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CDLOG {#c32-i3908}
*分類: 管理リファレンス*  ・  難易度: 中級

CDLOGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.417) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.417)

??? question "確認問題（1問）"
    **問題.** 監査追跡の管理リファレンスでネットビューの運用確認を行います。CDLOG の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査追跡の管理リファレンスを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査追跡として引き継ぐ。 ✅
    - D. CDLOG の属性行を読まず監査追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では CDLOG は「IBM Z NetViewで CDLOG の扱いを記録する監査追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では CDLOG の表示結果と DSI633I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では CDLOG の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CELL_POOLS {#c32-i3909}
*分類: 管理リファレンス*  ・  難易度: 中級

CELL_POOLSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.527) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.527)

??? question "確認問題（1問）"
    **問題.** 変更追跡の管理リファレンスに関する CELL_POOLS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. CELL_POOLS の変更点を出力本文から切り離して変更追跡の管理リファレンスの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更追跡の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では CELL_POOLS は「CELL_POOLS の状態と出力メッセージを結び付ける変更追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では CELL_POOLS の出力行と DSI633I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では CELL_POOLS を IBM Z NetViewの確認記録に残し、対象名は変更追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CHARACTER_VALIDATION {#c32-i3910}
*分類: 管理リファレンス*  ・  難易度: 中級

CHARACTER_VALIDATIONは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.529) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.529)

??? question "確認問題（1問）"
    **問題.** 構文検査の管理リファレンスに関係する CHARACTER_VALIDATION の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. IBM Z NetViewの表示形式に沿って根拠行を採り、構文検査の点検結果を残す。 ✅
    - B. CHARACTER_VALIDATION の名称と担当者名のみを残して構文検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では CHARACTER_VALIDATION は「CHARACTER_VALIDATION の用途をネットビューの表示で確認する構文検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では IBM Z NetViewの CHARACTER_VALIDATION と DSI633I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では CHARACTER_VALIDATION を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CHECKPOINT {#c32-i3911}
*分類: 管理リファレンス*  ・  難易度: 中級

CHECKPOINTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.550) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.550)

??? question "確認問題（1問）"
    **問題.** 展開検査の管理リファレンスで CHECKPOINT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CHECKPOINT の出力を取らず展開検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開検査で再確認できる形にする。 ✅
    - C. BROWSE CANZLOG を省略して展開検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では CHECKPOINT は「展開検査の管理リファレンスに関係する定義値と表示行を照合する展開検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では CHECKPOINT の属性行と DSI633I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では CHECKPOINT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CHECKPOINT_FUNCTION {#c32-i3912}
*分類: 管理リファレンス*  ・  難易度: 中級

CHECKPOINT_FUNCTIONは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.530) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.530)

??? question "確認問題（1問）"
    **問題.** 呼出検査の管理リファレンスでネットビューの運用確認を行います。CHECKPOINT_FUNCTION の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検査の管理リファレンスを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出検査の確認値として扱う。 ✅
    - D. CHECKPOINT_FUNCTION の属性行を読まず呼出検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では CHECKPOINT_FUNCTION は「IBM Z NetViewで CHECKPOINT_FUNCTION の扱いを記録する呼出検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では CHECKPOINT_FUNCTION の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では CHECKPOINT_FUNCTION の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMDCLASS {#c32-i3913}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDCLASSは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.306) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.306)

??? question "確認問題（1問）"
    **問題.** 置換検査の管理リファレンスに関する CMDCLASS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の管理リファレンスの証跡として保存して根拠にする。
    - C. CMDCLASS の変更点を出力本文から切り離して置換検査の管理リファレンスの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では CMDCLASS は「CMDCLASS の状態と出力メッセージを結び付ける置換検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では CMDCLASS の出力行と DSI633I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では CMDCLASS を IBM Z NetViewの確認記録に残し、対象名は置換検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMDDEF {#c32-i3914}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDDEFは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.306) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.306)

??? question "確認問題（1問）"
    **問題.** 終端検査の管理リファレンスに関係する CMDDEF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DSI633I を含む表示を保存し、説明欄との差分を終端検査で確認する。 ✅
    - B. CMDDEF の名称と担当者名のみを残して終端検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では CMDDEF は「CMDDEF の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの CMDDEF と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では CMDDEF を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### CMDEDIT {#c32-i3915}
*分類: 管理リファレンス*  ・  難易度: 中級

CMDEDITは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.56) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.56)

??? question "確認問題（1問）"
    **問題.** 探索検査の管理リファレンスで CMDEDIT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CMDEDIT の出力を取らず探索検査の管理リファレンスの説明文と承認印のみを残す。
    - B. BROWSE CANZLOG の結果から対象行を抜き出し、探索検査の証跡として残す。 ✅
    - C. BROWSE CANZLOG を省略して探索検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では CMDEDIT は「探索検査の管理リファレンスに関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では CMDEDIT の属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では CMDEDIT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide


