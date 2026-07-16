---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (25/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作)

### SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 2 {#c32-i3624}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 2は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切追跡の⁄で SSCP 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SSCP 機能の出力を取らず区切追跡の⁄の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、区切追跡の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して区切追跡の⁄の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の⁄へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では SSCP 機能 は「区切追跡の⁄に関係する定義値と表示行を照合する区切追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では SSCP 機能の属性行と DSI633I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では SSCP 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 3 {#c32-i3625}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 3は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲追跡の⁄でネットビューの運用確認を行います。SSCP 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲追跡の⁄を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲追跡の⁄を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、範囲追跡で再確認できる形にする。 ✅
    - D. SSCP 機能の属性行を読まず範囲追跡の⁄の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では SSCP 機能 は「IBM Z NetViewで SSCP 機能の扱いを記録する範囲追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では SSCP 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では SSCP 機能の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 4 {#c32-i3626}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 4は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先追跡の⁄に関する SSCP 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先追跡の⁄の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の⁄の証跡として保存して根拠にする。
    - C. SSCP 機能の変更点を出力本文から切り離して優先追跡の⁄の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、優先追跡の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では SSCP 機能 は「SSCP 機能の状態と出力メッセージを結び付ける優先追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では SSCP 機能の出力行と DSI633I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では SSCP 機能を IBM Z NetViewの確認記録に残し、対象名は優先追跡対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Sample AON extended module {#c32-i3627}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Sample AON extended moduleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.290) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.290)

??? question "確認問題（1問）"
    **問題.** 範囲確認のユーザーズガイド 操作でネットビューの運用確認を行います。Sample 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲確認のユーザーズガイド 操作を確認した扱いにする。
    - B. EZL000I の有無を確認せず範囲確認のユーザーズガイド 操作を正常終了として記録する。
    - C. AONSTAT で得た表示本文を使い、範囲確認の採否を説明欄に結び付ける。 ✅
    - D. Sample 機能の属性行を読まず範囲確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Sample 機能 は「IBM Z NetViewで Sample 機能の扱いを記録する範囲確認項目」と AONSTAT または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Sample 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Sample 機能の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Scheduling Commands {#c32-i3628}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Scheduling Commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.203) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.203)

??? question "確認問題（1問）"
    **問題.** 優先確認のユーザーズガイド 操作に関する Scheduling 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Scheduling 機能の変更点を出力本文から切り離して優先確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先確認として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Scheduling 機能 は「Scheduling 機能の状態と出力メッセージを結び付ける優先確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Scheduling 機能の出力行と DSI633I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Scheduling 機能を IBM Z NetViewの確認記録に残し、対象名は優先確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Searching AON components for a resource {#c32-i3629}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Searching AON components for a resourceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録確認のユーザーズガイド 操作に関係する Searching 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録確認の確認にする。 ✅
    - B. Searching 機能の名称と担当者名のみを残して記録確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず記録確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Searching 機能 は「Searching 機能の用途をネットビューの表示で確認する記録確認項目」と AONSTAT または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IBM Z NetViewの Searching 機能と EZL000I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Searching 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Secondary Recording of Event Records {#c32-i3630}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Secondary Recording of Event Recordsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較確認のユーザーズガイド 操作で Secondary 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Secondary 機能の出力を取らず比較確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、比較確認の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して比較確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Secondary 機能 は「比較確認のユーザーズガイド 操作に関係する定義値と表示行を照合する比較確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Secondary 機能の属性行と DSI633I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Secondary 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較確認初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Security Details Workspace {#c32-i3631}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Security Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.55) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.55)

??? question "確認問題（1問）"
    **問題.** 順序確認のユーザーズガイド 操作でネットビューの運用確認を行います。Security 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序確認で再確認できる形にする。 ✅
    - D. Security 機能の属性行を読まず順序確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Security 機能 は「IBM Z NetViewで Security 機能の扱いを記録する順序確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Security 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Security 機能の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Sending Commands to Multiple NetView Domains {#c32-i3632}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Sending Commands to Multiple NetView Domainsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域確認のユーザーズガイド 操作に関する Sending 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Sending 機能の変更点を出力本文から切り離して値域確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Sending 機能 は「Sending 機能の状態と出力メッセージを結び付ける値域確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Sending 機能の出力行と DSI633I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Sending 機能を IBM Z NetViewの確認記録に残し、対象名は値域確認対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Sending MSUs to an MS Transport Application (EZLSMSU) {#c32-i3633}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Sending MSUs to an MS Transport Application (EZLSMSU)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のユーザーズガイド 操作に関係する Sending 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告確認の根拠を固定する。 ✅
    - B. Sending 機能の名称と担当者名のみを残して警告確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Sending 機能 は「Sending 機能の用途をネットビューの表示で確認する警告確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Z NetViewの Sending 機能と DSI633I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Sending 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Services of the Event/Automation Service {#c32-i3634}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Services of the Event/Automation Serviceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として Services of the Event/Automa を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。構文照合保守で扱う Services of the Event/Automa は Tivoli NetView z/OS 自動化 の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として Services of the Event/Automa を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Servlets {#c32-i3635}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Servletsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.141) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.141)

??? question "確認問題（1問）"
    **問題.** 構文照合のユーザーズガイド 操作に関係する Servletsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文照合の根拠にする。 ✅
    - B. Servletsの名称と担当者名のみを残して構文照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Servlets は「Servletsの用途をネットビューの表示で確認する構文照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では IBM Z NetViewの Servletsと DSI633I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Servletsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Session Data Attributes {#c32-i3636}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Session Data Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.158) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.158)

??? question "確認問題（1問）"
    **問題.** 呼出照合のユーザーズガイド 操作でネットビューの運用確認を行います。Session 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出照合のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出照合の採否を説明欄に結び付ける。 ✅
    - D. Session 機能の属性行を読まず呼出照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では Session 機能 は「IBM Z NetViewで Session 機能の扱いを記録する呼出照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では Session 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では Session 機能の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Session Data Workspace {#c32-i3637}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Session Data Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.70) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.70)

??? question "確認問題（1問）"
    **問題.** 置換照合のユーザーズガイド 操作に関する Session 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Session 機能の変更点を出力本文から切り離して置換照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換照合として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では Session 機能 は「Session 機能の状態と出力メッセージを結び付ける置換照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では Session 機能の出力行と DSI633I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では Session 機能を IBM Z NetViewの確認記録に残し、対象名は置換照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Session between 2 SNA Advanced Peer-to-Peer Networking Subnetworks with a LEN Connection {#c32-i3638}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Session between 2 SNA Advanced Peer-to-Peer Networking Subnetworks with a LEN Connectionは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Sessions-Data Availability Scenarios {#c32-i3639}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Sessions-Data Availability Scenariosは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.275) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.275)

??? question "確認問題（1問）"
    **問題.** 終端照合のユーザーズガイド 操作に関係する Sessions-Data 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端照合の確認にする。 ✅
    - B. Sessions-Data 機能の名称と担当者名のみを残して終端照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では Sessions-Data 機能 は「Sessions-Data 機能の用途をネットビューの表示で確認する終端照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM Z NetViewの Sessions-Data 機能と DSI633I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では Sessions-Data 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Setting Network and System Security {#c32-i3640}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Setting Network and System Securityは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書照合のユーザーズガイド 操作でネットビューの運用確認を行います。Setting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書照合のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書照合で再確認できる形にする。 ✅
    - D. Setting 機能の属性行を読まず上書照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では Setting 機能 は「IBM Z NetViewで Setting 機能の扱いを記録する上書照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では Setting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では Setting 機能の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setting Panel Message Color (EZLEMCOL) {#c32-i3641}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Setting Panel Message Color (EZLEMCOL)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.328) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.328)

??? question "確認問題（1問）"
    **問題.** 出力照合のユーザーズガイド 操作に関する Setting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Setting 機能の変更点を出力本文から切り離して出力照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では Setting 機能 は「Setting 機能の状態と出力メッセージを結び付ける出力照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では Setting 機能の出力行と DSI633I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では Setting 機能を IBM Z NetViewの確認記録に残し、対象名は出力照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Setting automation thresholds {#c32-i3642}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Setting automation thresholdsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.57) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.57)

??? question "確認問題（1問）"
    **問題.** 探索照合のユーザーズガイド 操作で Setting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Setting 機能の出力を取らず探索照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、探索照合の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して探索照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では Setting 機能 は「探索照合のユーザーズガイド 操作に関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では Setting 機能の属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では Setting 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Setting the AIP User Status Bit (EZLERAIP) {#c32-i3643}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Setting the AIP User Status Bit (EZLERAIP)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件照合のユーザーズガイド 操作に関係する Setting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件照合の根拠を固定する。 ✅
    - B. Setting 機能の名称と担当者名のみを残して条件照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では Setting 機能 は「Setting 機能の用途をネットビューの表示で確認する条件照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では IBM Z NetViewの Setting 機能と DSI633I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では Setting 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setting the Primary Focal Point {#c32-i3644}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Setting the Primary Focal Pointは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切照合のユーザーズガイド 操作で Setting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Setting 機能の出力を取らず区切照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を区切照合で確認する。 ✅
    - C. BROWSE CANZLOG を省略して区切照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では Setting 機能 は「区切照合のユーザーズガイド 操作に関係する定義値と表示行を照合する区切照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では Setting 機能の属性行と DSI633I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では Setting 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切照合初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setting traces {#c32-i3645}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Setting tracesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.86) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.86)

??? question "確認問題（1問）"
    **問題.** 範囲照合のユーザーズガイド 操作でネットビューの運用確認を行います。Setting tracesの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲照合のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、範囲照合の証跡として残す。 ✅
    - D. Setting tracesの属性行を読まず範囲照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では Setting traces は「IBM Z NetViewで Setting tracesの扱いを記録する範囲照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では Setting tracesの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では Setting tracesの使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Setting up the Dynamic Display Facility for AON {#c32-i3646}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Setting up the Dynamic Display Facility for AONは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先照合のユーザーズガイド 操作に関する Setting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. AONSTAT の結果を残さず優先照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Setting 機能の変更点を出力本文から切り離して優先照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先照合の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では Setting 機能 は「Setting 機能の状態と出力メッセージを結び付ける優先照合項目」と AONSTAT または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では Setting 機能の出力行と EZL000I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では Setting 機能を IBM Z NetViewの確認記録に残し、対象名は優先照合対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Setup {#c32-i3647}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Setupは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.141) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.141)

??? question "確認問題（2問）"
    **問題.** 記録照合のユーザーズガイド 操作に関係する Setupの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録照合の根拠にする。 ✅
    - B. Setupの名称と担当者名のみを残して記録照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では Setup は「Setupの用途をネットビューの表示で確認する記録照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では IBM Z NetViewの Setupと DSI633I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では Setupを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide

    ---

    **問題.** 変更検査の管理リファレンスに関する SETUP の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の管理リファレンスの証跡として保存して根拠にする。
    - C. SETUP の変更点を出力本文から切り離して変更検査の管理リファレンスの承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、変更検査の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では SETUP は「SETUP の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では SETUP の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では SETUP を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Situation Overview {#c32-i3648}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Situation Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.26) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.26)

??? question "確認問題（1問）"
    **問題.** 比較照合のユーザーズガイド 操作で Situation Overviewの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Situation Overviewの出力を取らず比較照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較照合の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では Situation Overview は「比較照合のユーザーズガイド 操作に関係する定義値と表示行を照合する比較照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では Situation Overviewの属性行と DSI633I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では Situation Overviewを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Situations {#c32-i3649}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Situationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.97) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.97)

??? question "確認問題（1問）"
    **問題.** 順序照合のユーザーズガイド 操作でネットビューの運用確認を行います。Situationsの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序照合のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序照合のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序照合の採否を説明欄に結び付ける。 ✅
    - D. Situationsの属性行を読まず順序照合のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では Situations は「IBM Z NetViewで Situationsの扱いを記録する順序照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では Situationsの表示結果と DSI633I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では Situationsの使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Solving network problems with Help Desks {#c32-i3650}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Solving network problems with Help Desksは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端追跡のユーザーズガイド 操作に関係する Solving 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端追跡の根拠にする。 ✅
    - B. Solving 機能の名称と担当者名のみを残して終端追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では Solving 機能 は「Solving 機能の用途をネットビューの表示で確認する終端追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では IBM Z NetViewの Solving 機能と DSI633I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では Solving 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Specifying automation policy settings {#c32-i3651}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Specifying automation policy settingsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索追跡のユーザーズガイド 操作で Specifying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Specifying 機能の出力を取らず探索追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、探索追跡の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して探索追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では Specifying 機能 は「探索追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する探索追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では Specifying 機能の属性行と DSI633I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では Specifying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Specifying notification operators {#c32-i3652}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Specifying notification operatorsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書追跡のユーザーズガイド 操作でネットビューの運用確認を行います。Specifying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、上書追跡の採否を説明欄に結び付ける。 ✅
    - D. Specifying 機能の属性行を読まず上書追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では Specifying 機能 は「IBM Z NetViewで Specifying 機能の扱いを記録する上書追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では Specifying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では Specifying 機能の使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Specifying recovery settings {#c32-i3653}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Specifying recovery settingsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力追跡のユーザーズガイド 操作に関する Specifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Specifying 機能の変更点を出力本文から切り離して出力追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力追跡として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では Specifying 機能 は「Specifying 機能の状態と出力メッセージを結び付ける出力追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では Specifying 機能の出力行と DSI633I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では Specifying 機能を IBM Z NetViewの確認記録に残し、対象名は出力追跡対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stack Configuration and Status Attributes {#c32-i3654}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stack Configuration and Status Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較追跡のユーザーズガイド 操作で Stack 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Stack 機能の出力を取らず比較追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を比較追跡で確認する。 ✅
    - C. BROWSE CANZLOG を省略して比較追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では Stack 機能 は「比較追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する比較追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では Stack 機能の属性行と DSI633I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では Stack 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stack Configuration and Status Workspace {#c32-i3655}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stack Configuration and Status Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序追跡のユーザーズガイド 操作でネットビューの運用確認を行います。Stack 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、順序追跡の証跡として残す。 ✅
    - D. Stack 機能の属性行を読まず順序追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では Stack 機能 は「IBM Z NetViewで Stack 機能の扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では Stack 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では Stack 機能の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stack Situations {#c32-i3656}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stack Situationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域追跡のユーザーズガイド 操作に関する Stack Situationsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Stack Situationsの変更点を出力本文から切り離して値域追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では Stack Situations は「Stack Situationsの状態と出力メッセージを結び付ける値域追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では Stack Situationsの出力行と DSI633I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では Stack Situationsを IBM Z NetViewの確認記録に残し、対象名は値域追跡対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stack-Defined DVIPA Workspace {#c32-i3657}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stack-Defined DVIPA Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.45)

??? question "確認問題（1問）"
    **問題.** 警告追跡のユーザーズガイド 操作に関係する Stack-Defined 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告追跡の根拠にする。 ✅
    - B. Stack-Defined 機能の名称と担当者名のみを残して警告追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では Stack-Defined 機能 は「Stack-Defined 機能の用途をネットビューの表示で確認する警告追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では IBM Z NetViewの Stack-Defined 機能と DSI633I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では Stack-Defined 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Starting Cross-domain Sessions (EZLESTRT) {#c32-i3658}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Starting Cross-domain Sessions (EZLESTRT)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文検査のユーザーズガイド 操作に関係する Starting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文検査の確認にする。 ✅
    - B. Starting 機能の名称と担当者名のみを残して構文検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では Starting 機能 は「Starting 機能の用途をネットビューの表示で確認する構文検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では IBM Z NetViewの Starting 機能と DSI633I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では Starting 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Starting an Autotask to Handle Automation {#c32-i3659}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Starting an Autotask to Handle Automationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査追跡のユーザーズガイド 操作でネットビューの運用確認を行います。Starting 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査追跡の採否を説明欄に結び付ける。 ✅
    - D. Starting 機能の属性行を読まず監査追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では Starting 機能 は「IBM Z NetViewで Starting 機能の扱いを記録する監査追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では Starting 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では Starting 機能の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Starting and stopping DDF {#c32-i3660}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Starting and stopping DDFは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更追跡のユーザーズガイド 操作に関する Starting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Starting 機能の変更点を出力本文から切り離して変更追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更追跡として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では Starting 機能 は「Starting 機能の状態と出力メッセージを結び付ける変更追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では Starting 機能の出力行と DSI633I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では Starting 機能を IBM Z NetViewの確認記録に残し、対象名は変更追跡対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Starting the NetView Program {#c32-i3661}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Starting the NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開検査のユーザーズガイド 操作で Starting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Starting 機能の出力を取らず展開検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、展開検査の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して展開検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では Starting 機能 は「展開検査のユーザーズガイド 操作に関係する定義値と表示行を照合する展開検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では Starting 機能の属性行と DSI633I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では Starting 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Starting the Topology Console {#c32-i3662}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Starting the Topology Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Starting the Topology Server {#c32-i3663}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Starting the Topology Serverは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Status File Interface Command (EZLSTS) {#c32-i3664}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Status File Interface Command (EZLSTS)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.300) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.300)

??? question "確認問題（1問）"
    **問題.** 終端検査のユーザーズガイド 操作に関係する Status 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端検査の根拠を固定する。 ✅
    - B. Status 機能の名称と担当者名のみを残して終端検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Status 機能 は「Status 機能の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの Status 機能と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Status 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Stopping Cross-domain Sessions (EZLESTOP) {#c32-i3665}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stopping Cross-domain Sessions (EZLESTOP)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書検査のユーザーズガイド 操作でネットビューの運用確認を行います。Stopping 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検査のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、上書検査の証跡として残す。 ✅
    - D. Stopping 機能の属性行を読まず上書検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では Stopping 機能 は「IBM Z NetViewで Stopping 機能の扱いを記録する上書検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では Stopping 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では Stopping 機能の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stopping the Topology Console {#c32-i3666}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stopping the Topology Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力検査のユーザーズガイド 操作に関する Stopping 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Stopping 機能の変更点を出力本文から切り離して出力検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では Stopping 機能 は「Stopping 機能の状態と出力メッセージを結び付ける出力検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では Stopping 機能の出力行と DSI633I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では Stopping 機能を IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Stopping the Topology Server {#c32-i3667}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Stopping the Topology Serverは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件検査のユーザーズガイド 操作に関係する Stopping 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件検査の根拠にする。 ✅
    - B. Stopping 機能の名称と担当者名のみを残して条件検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では Stopping 機能 は「Stopping 機能の用途をネットビューの表示で確認する条件検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの Stopping 機能と DSI633I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では Stopping 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Supplied Support Files {#c32-i3668}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Supplied Support Filesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.51) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.51)

??? question "確認問題（1問）"
    **問題.** 区切検査のユーザーズガイド 操作で Supplied 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Supplied 機能の出力を取らず区切検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、区切検査の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して区切検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では Supplied 機能 は「区切検査のユーザーズガイド 操作に関係する定義値と表示行を照合する区切検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では Supplied 機能の属性行と DSI633I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では Supplied 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCP/IP Command Support (IPCMD) {#c32-i3669}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCP/IP Command Support (IPCMD)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.350) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.350)

??? question "確認問題（1問）"
    **問題.** 警告検査のTCP/IP Command Support (IPCMD)に関係する TCP 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告検査の根拠を固定する。 ✅
    - B. TCP 属性の名称と担当者名のみを残して警告検査のTCP/IP Command Support (IPCMD)の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査のTCP/IP Command Support (IPCMD)を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検査のTCP/IP Command Support (IPCMD)の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では TCP 属性 は「TCP 属性の用途をネットビューの表示で確認する警告検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの TCP 属性と DSI633I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では TCP 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCP/IP Connection Data Situations {#c32-i3670}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCP/IP Connection Data Situationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.104) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.104)

??? question "確認問題（1問）"
    **問題.** 復旧検査のTCP/IP Connection Data Situationsで TCP 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TCP 属性の出力を取らず復旧検査のTCP/IP Connection Data Situationsの説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を復旧検査で確認する。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査のTCP/IP Connection Data Situationsの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のTCP/IP Connection Data Situationsへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では TCP 属性 は「復旧検査のTCP/IP Connection Data Situationsに関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では TCP 属性の属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では TCP 属性を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCP/IP Connection Workspaces {#c32-i3671}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCP/IP Connection Workspacesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.49) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.49)

??? question "確認問題（1問）"
    **問題.** 監査検査のTCP/IP Connection Workspacesでネットビューの運用確認を行います。TCP 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査のTCP/IP Connection Workspacesを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査のTCP/IP Connection Workspacesを正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、監査検査の証跡として残す。 ✅
    - D. TCP 属性の属性行を読まず監査検査のTCP/IP Connection Workspacesの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では TCP 属性 は「IBM Z NetViewで TCP 属性の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では TCP 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では TCP 属性の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCP/IP for z/OS {#c32-i3672}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCP/IP for z/OSは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.145) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.145)

??? question "確認問題（1問）"
    **問題.** 変更検査のTCP/IP for z/OS TCP/IP for z/OSに関する TCP ・ IP for z・ OS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査のTCP/IP for z/OS ・の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のTCP/IP for z/OS ・の証跡として保存して根拠にする。
    - C. TCP ・ IP for z・ OS の変更点を出力本文から切り離して変更検査のTCP/IP for z/OS ・の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では TCP ・ IP for z・ OS は「TCP ・ IP for z・ OS の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では TCP ・ IP for z・ OS の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では TCP ・ IP for z・ OS を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCPIP Connection Data Attributes {#c32-i3673}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCPIP Connection Data Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.162) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.162)

??? question "確認問題（1問）"
    **問題.** 構文判定のユーザーズガイド 操作に関係する TCPIP 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文判定の根拠にする。 ✅
    - B. TCPIP 機能の名称と担当者名のみを残して構文判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では TCPIP 機能 は「TCPIP 機能の用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの TCPIP 機能と DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では TCPIP 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCPIP Connection Data Workspace {#c32-i3674}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCPIP Connection Data Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.56) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.56)

??? question "確認問題（1問）"
    **問題.** 展開判定のユーザーズガイド 操作で TCPIP 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TCPIP 機能の出力を取らず展開判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開判定の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では TCPIP 機能 は「展開判定のユーザーズガイド 操作に関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では TCPIP 機能の属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では TCPIP 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCPIP Connections Certificates Attributes {#c32-i3675}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCPIP Connections Certificates Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.160) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.160)

??? question "確認問題（1問）"
    **問題.** 呼出判定のユーザーズガイド 操作でネットビューの運用確認を行います。TCPIP 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出判定の採否を説明欄に結び付ける。 ✅
    - D. TCPIP 機能の属性行を読まず呼出判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では TCPIP 機能 は「IBM Z NetViewで TCPIP 機能の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では TCPIP 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では TCPIP 機能の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TCPIP Connections Encryption Data Attributes {#c32-i3676}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

TCPIP Connections Encryption Data Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.166) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.166)

??? question "確認問題（1問）"
    **問題.** 置換判定のユーザーズガイド 操作に関する TCPIP 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. TCPIP 機能の変更点を出力本文から切り離して置換判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換判定として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では TCPIP 機能 は「TCPIP 機能の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では TCPIP 機能の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では TCPIP 機能を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### TLS Cipher Suites Workspace {#c32-i3677}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

TLS Cipher Suites Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.57) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.57)

??? question "確認問題（1問）"
    **問題.** 値域判定のユーザーズガイド 操作に関する TLS 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. TLS 機能の変更点を出力本文から切り離して値域判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域判定として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では TLS 機能 は「TLS 機能の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では TLS 機能の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では TLS 機能を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Tailored routines and displays {#c32-i3678}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Tailored routines and displaysは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.206) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.206)

??? question "確認問題（1問）"
    **問題.** 範囲検査のユーザーズガイド 操作でネットビューの運用確認を行います。Tailored 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検査のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、範囲検査の採否を説明欄に結び付ける。 ✅
    - D. Tailored 機能の属性行を読まず範囲検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では Tailored 機能 は「IBM Z NetViewで Tailored 機能の扱いを記録する範囲検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では Tailored 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では Tailored 機能の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Tailoring gateways and focal points {#c32-i3679}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Tailoring gateways and focal pointsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先検査のユーザーズガイド 操作に関する Tailoring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Tailoring 機能の変更点を出力本文から切り離して優先検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先検査として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では Tailoring 機能 は「Tailoring 機能の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では Tailoring 機能の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では Tailoring 機能を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Take Action Command Overview {#c32-i3680}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Take Action Command Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.27) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.27)

??? question "確認問題（1問）"
    **問題.** 記録検査のユーザーズガイド 操作に関係する Take 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録検査の確認にする。 ✅
    - B. Take 機能の名称と担当者名のみを残して記録検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では Take 機能 は「Take 機能の用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの Take 機能と DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では Take 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Take Action Commands {#c32-i3681}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Take Action Commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.111) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.111)

??? question "確認問題（1問）"
    **問題.** 比較検査のユーザーズガイド 操作で Take 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Take 機能の出力を取らず比較検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、比較検査の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して比較検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では Take 機能 は「比較検査のユーザーズガイド 操作に関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では Take 機能の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では Take 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Telnet Server Attributes {#c32-i3682}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Telnet Server Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.183) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.183)

??? question "確認問題（1問）"
    **問題.** 探索判定のユーザーズガイド 操作で Telnet 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Telnet 機能の出力を取らず探索判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、探索判定の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して探索判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では Telnet 機能 は「探索判定のユーザーズガイド 操作に関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では Telnet 機能の属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では Telnet 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Telnet Server Configuration and Status Workspace {#c32-i3683}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Telnet Server Configuration and Status Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書判定のユーザーズガイド 操作でネットビューの運用確認を行います。Telnet 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書判定で再確認できる形にする。 ✅
    - D. Telnet 機能の属性行を読まず上書判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では Telnet 機能 は「IBM Z NetViewで Telnet 機能の扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では Telnet 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では Telnet 機能の使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Telnet Server Port Attributes {#c32-i3684}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Telnet Server Port Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.184) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.184)

??? question "確認問題（1問）"
    **問題.** 出力判定のユーザーズガイド 操作に関する Telnet 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Telnet 機能の変更点を出力本文から切り離して出力判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力判定の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では Telnet 機能 は「Telnet 機能の状態と出力メッセージを結び付ける出力判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では Telnet 機能の出力行と DSI633I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では Telnet 機能を IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Telnet Server Situations {#c32-i3685}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Telnet Server Situationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.104) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.104)

??? question "確認問題（1問）"
    **問題.** 条件判定のユーザーズガイド 操作に関係する Telnet 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件判定の根拠を固定する。 ✅
    - B. Telnet 機能の名称と担当者名のみを残して条件判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Telnet 機能 は「Telnet 機能の用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの Telnet 機能と DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Telnet 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Testing an Automation Table {#c32-i3686}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Testing an Automation Tableは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.191) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.191)

??? question "確認問題（1問）"
    **問題.** 区切判定のユーザーズガイド 操作で Testing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Testing 機能の出力を取らず区切判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を区切判定で確認する。 ✅
    - C. BROWSE CANZLOG を省略して区切判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Testing 機能 は「区切判定のユーザーズガイド 操作に関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Testing 機能の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Testing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Tivoli Enterprise Portal Overview {#c32-i3687}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Tivoli Enterprise Portal Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.19) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.19)

??? question "確認問題（1問）"
    **問題.** 比較判定のユーザーズガイド 操作で Tivoli 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Tivoli 機能の出力を取らず比較判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較判定の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Tivoli 機能 は「比較判定のユーザーズガイド 操作に関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Tivoli 機能の属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Tivoli 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Topology Console Commands {#c32-i3688}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Topology Console Commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.121) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.121)

??? question "確認問題（1問）"
    **問題.** 変更判定のユーザーズガイド 操作に関する Topology 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Topology 機能の変更点を出力本文から切り離して変更判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更判定の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Topology 機能 は「Topology 機能の状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Topology 機能の出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Topology 機能を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Topology Console Java Applications and Plug-ins {#c32-i3689}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Topology Console Java Applications and Plug-insは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文整理のユーザーズガイド 操作に関係する Topology 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文整理の根拠を固定する。 ✅
    - B. Topology 機能の名称と担当者名のみを残して構文整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では Topology 機能 は「Topology 機能の用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの Topology 機能と DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では Topology 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Topology Console Window {#c32-i3690}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Topology Console Windowは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.73) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.73)

??? question "確認問題（1問）"
    **問題.** 展開整理のユーザーズガイド 操作で Topology 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Topology 機能の出力を取らず展開整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を展開整理で確認する。 ✅
    - C. BROWSE CANZLOG を省略して展開整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では Topology 機能 は「展開整理のユーザーズガイド 操作に関係する定義値と表示行を照合する展開整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では Topology 機能の属性行と DSI633I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では Topology 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Topology Server Commands {#c32-i3691}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Topology Server Commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.109) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.109)

??? question "確認問題（1問）"
    **問題.** 呼出整理のユーザーズガイド 操作でネットビューの運用確認を行います。Topology 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、呼出整理の証跡として残す。 ✅
    - D. Topology 機能の属性行を読まず呼出整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では Topology 機能 は「IBM Z NetViewで Topology 機能の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では Topology 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では Topology 機能の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Tracing the Examples {#c32-i3692}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Tracing the Examplesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.52) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.52)

??? question "確認問題（1問）"
    **問題.** 置換整理のユーザーズガイド 操作に関する Tracing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Tracing 機能の変更点を出力本文から切り離して置換整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換整理の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では Tracing 機能 は「Tracing 機能の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では Tracing 機能の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では Tracing 機能を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding BNJ146 Message Automation {#c32-i3693}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Understanding BNJ146 Message Automationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.402) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.402)

??? question "確認問題（1問）"
    **問題.** 探索整理のユーザーズガイド 操作で Understanding 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Understanding 機能の出力を取らず探索整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、探索整理の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して探索整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Understanding 機能 は「探索整理のユーザーズガイド 操作に関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Understanding 機能の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Understanding 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding Code Point tables {#c32-i3694}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding Code Point tablesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.402) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.402)

??? question "確認問題（1問）"
    **問題.** 上書整理のユーザーズガイド 操作でネットビューの運用確認を行います。Understanding 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、上書整理の採否を説明欄に結び付ける。 ✅
    - D. Understanding 機能の属性行を読まず上書整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では Understanding 機能 は「IBM Z NetViewで Understanding 機能の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では Understanding 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では Understanding 機能の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding Command Profiles {#c32-i3695}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding Command Profilesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.95) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.95)

??? question "確認問題（1問）"
    **問題.** 出力整理のユーザーズガイド 操作に関する Understanding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Understanding 機能の変更点を出力本文から切り離して出力整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力整理として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では Understanding 機能 は「Understanding 機能の状態と出力メッセージを結び付ける出力整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では Understanding 機能の出力行と DSI633I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では Understanding 機能を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding Dynamic Display Facility (DDF) design {#c32-i3696}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding Dynamic Display Facility (DDF) designは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.209) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.209)

??? question "確認問題（1問）"
    **問題.** 条件整理のユーザーズガイド 操作に関係する Understanding 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件整理の確認にする。 ✅
    - B. Understanding 機能の名称と担当者名のみを残して条件整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では Understanding 機能 は「Understanding 機能の用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの Understanding 機能と DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では Understanding 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding Topology Server Command Exits {#c32-i3697}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Understanding Topology Server Command Exitsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.103) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.103)

??? question "確認問題（1問）"
    **問題.** 警告整理のユーザーズガイド 操作に関係する Understanding 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告整理の根拠にする。 ✅
    - B. Understanding 機能の名称と担当者名のみを残して警告整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Understanding 機能 は「Understanding 機能の用途をネットビューの表示で確認する警告整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの Understanding 機能と DSI633I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Understanding 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding Views {#c32-i3698}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding Viewsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.83) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.83)

??? question "確認問題（1問）"
    **問題.** 復旧整理のユーザーズガイド 操作で Understanding 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Understanding 機能の出力を取らず復旧整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、復旧整理の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して復旧整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Understanding 機能 は「復旧整理のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Understanding 機能の属性行と DSI633I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Understanding 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding how a panel is organized {#c32-i3699}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding how a panel is organizedは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切整理のユーザーズガイド 操作で Understanding 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Understanding 機能の出力を取らず区切整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、区切整理の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して区切整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では Understanding 機能 は「区切整理のユーザーズガイド 操作に関係する定義値と表示行を照合する区切整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では Understanding 機能の属性行と DSI633I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では Understanding 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Understanding security alerts for an incorrect XID {#c32-i3700}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Understanding security alerts for an incorrect XIDは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲整理のユーザーズガイド 操作でネットビューの運用確認を行います。Understanding 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、範囲整理で再確認できる形にする。 ✅
    - D. Understanding 機能の属性行を読まず範囲整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Understanding 機能 は「IBM Z NetViewで Understanding 機能の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Understanding 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Understanding 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Understanding the Hardware Monitor Panel Terminology {#c32-i3701}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding the Hardware Monitor Panel Terminologyは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先整理のユーザーズガイド 操作に関する Understanding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Understanding 機能の変更点を出力本文から切り離して優先整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、優先整理の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では Understanding 機能 は「Understanding 機能の状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では Understanding 機能の出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では Understanding 機能を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Understanding the Hierarchical Status display {#c32-i3702}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding the Hierarchical Status displayは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録整理のユーザーズガイド 操作に関係する Understanding 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録整理の根拠を固定する。 ✅
    - B. Understanding 機能の名称と担当者名のみを残して記録整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では Understanding 機能 は「Understanding 機能の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの Understanding 機能と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では Understanding 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Understanding the LUDRPOOL command {#c32-i3703}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding the LUDRPOOL commandは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.405) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.405)

??? question "確認問題（1問）"
    **問題.** 比較整理のユーザーズガイド 操作で Understanding 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Understanding 機能の出力を取らず比較整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を比較整理で確認する。 ✅
    - C. BROWSE CANZLOG を省略して比較整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では Understanding 機能 は「比較整理のユーザーズガイド 操作に関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では Understanding 機能の属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では Understanding 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Understanding the NPSI Hardware Monitor Enhancement {#c32-i3704}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding the NPSI Hardware Monitor Enhancementは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序整理のユーザーズガイド 操作でネットビューの運用確認を行います。Understanding 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序整理のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、順序整理の証跡として残す。 ✅
    - D. Understanding 機能の属性行を読まず順序整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では Understanding 機能 は「IBM Z NetViewで Understanding 機能の扱いを記録する順序整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では Understanding 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では Understanding 機能の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Understanding the X25INIT command {#c32-i3705}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Understanding the X25INIT commandは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.404) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.404)

??? question "確認問題（1問）"
    **問題.** 値域整理のユーザーズガイド 操作に関する Understanding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Understanding 機能の変更点を出力本文から切り離して値域整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域整理の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Understanding 機能 は「Understanding 機能の状態と出力メッセージを結び付ける値域整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Understanding 機能の出力行と DSI633I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Understanding 機能を IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Unsecured Connections Workspace {#c32-i3706}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Unsecured Connections Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.58) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.58)

??? question "確認問題（1問）"
    **問題.** 監査整理のユーザーズガイド 操作でネットビューの運用確認を行います。Unsecured 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、監査整理の採否を説明欄に結び付ける。 ✅
    - D. Unsecured 機能の属性行を読まず監査整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Unsecured 機能 は「IBM Z NetViewで Unsecured 機能の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Unsecured 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Unsecured 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Updating status {#c32-i3707}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Updating statusは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更整理のユーザーズガイド 操作に関する Updating statusの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Updating statusの変更点を出力本文から切り離して変更整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更整理として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では Updating status は「Updating statusの状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では Updating statusの出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では Updating statusを IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Updating the Business Tree {#c32-i3708}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Updating the Business Treeは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文記録のユーザーズガイド 操作に関係する Updating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文記録の確認にする。 ✅
    - B. Updating 機能の名称と担当者名のみを残して構文記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では Updating 機能 は「Updating 機能の用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの Updating 機能と DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では Updating 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Updating the Status File and Logging Messages (EZLEASLN) {#c32-i3709}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Updating the Status File and Logging Messages (EZLEASLN)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開記録のユーザーズガイド 操作で Updating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Updating 機能の出力を取らず展開記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、展開記録の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して展開記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Updating 機能 は「展開記録のユーザーズガイド 操作に関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Updating 機能の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Updating 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using AON Command Processors {#c32-i3710}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using AON Command Processorsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件記録のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件記録の根拠にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して条件記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず条件記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する条件記録項目」と AONSTAT または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの Using 機能と EZL000I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using AON commands {#c32-i3711}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using AON commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切記録のユーザーズガイド 操作で Using AON commandsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using AON commandsの出力を取らず区切記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と EZL000I を読み、区切記録の結果として保存する。 ✅
    - C. AONSTAT を省略して区切記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Using AON commands は「区切記録のユーザーズガイド 操作に関係する定義値と表示行を照合する区切記録項目」と AONSTAT または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Using AON commandsの属性行と EZL000I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Using AON commandsを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using AON with TCP/IP {#c32-i3712}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using AON with TCP/IPは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲記録のUsing AON with TCP/IPでネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録のUsing AON with TCP/IPを確認した扱いにする。
    - B. EZL000I の有無を確認せず範囲記録のUsing AON with TCP/IPを正常終了として記録する。
    - C. AONSTAT で得た表示本文を使い、範囲記録の採否を説明欄に結び付ける。 ✅
    - D. Using 機能の属性行を読まず範囲記録のUsing AON with TCP/IPの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する範囲記録項目」と AONSTAT または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Using 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Using 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using AON/SNA {#c32-i3713}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using AON/SNAは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先記録のUsing AON/SNAに関する Using AON ・ SNA の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. AONSTAT の結果を残さず優先記録のUsing AON/SNAの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録のUsing AON/SNAの証跡として保存して根拠にする。
    - C. Using AON ・ SNA の変更点を出力本文から切り離して優先記録のUsing AON/SNAの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先記録として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Using AON ・ SNA は「Using AON ・ SNA の状態と出力メッセージを結び付ける優先記録項目」と AONSTAT または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Using AON ・ SNA の出力行と EZL000I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Using AON ・ SNA を IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Active Monitoring and Recovery (EZLECATV) {#c32-i3714}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Active Monitoring and Recovery (EZLECATV)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出記録のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出記録で再確認できる形にする。 ✅
    - D. Using 機能の属性行を読まず呼出記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Using 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Advanced Peer-to-Peer Networking (APPN) {#c32-i3715}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Advanced Peer-to-Peer Networking (APPN)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換記録のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換記録の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Automation Table Management {#c32-i3716}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using Automation Table Managementは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録記録のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録記録の確認にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して記録記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Basic Data Files {#c32-i3717}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Basic Data Filesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較記録のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず比較記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、比較記録の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して比較記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Using 機能 は「比較記録のユーザーズガイド 操作に関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Cross-Domain functions {#c32-i3718}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Cross-Domain functionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序記録のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序記録で再確認できる形にする。 ✅
    - D. Using 機能の属性行を読まず順序記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Using 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Hardware Monitor Filters {#c32-i3719}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Hardware Monitor Filtersは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域記録のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して値域記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域記録の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using IP Resource Management {#c32-i3720}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using IP Resource Managementは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using NetView Commands (SNA Subarea, SNA Advanced Peer-to-Peer Networking) {#c32-i3721}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using NetView Commands (SNA Subarea, SNA Advanced Peer-to-Peer Networking)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧記録のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず復旧記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を復旧記録で確認する。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Using 機能 は「復旧記録のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using NetView Commands at the Command Line {#c32-i3722}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using NetView Commands at the Command Lineは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査記録のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、監査記録の証跡として残す。 ✅
    - D. Using 機能の属性行を読まず監査記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Using 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using NetView Management Console {#c32-i3723}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文分離のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文分離の根拠にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して構文分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する構文分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using NetView Management Console Command Profiles {#c32-i3724}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using NetView Management Console Command Profilesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開分離のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず展開分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、展開分離の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して展開分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では Using 機能 は「展開分離のユーザーズガイド 操作に関係する定義値と表示行を照合する展開分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using NetView Timer Management Panels {#c32-i3725}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using NetView Timer Management Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出分離のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出分離のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、呼出分離の採否を説明欄に結び付ける。 ✅
    - D. Using 機能の属性行を読まず呼出分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する呼出分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では Using 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using NetView from a 3270 Session {#c32-i3726}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using NetView from a 3270 Sessionは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更記録のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して変更記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更記録の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Operator MARK panels {#c32-i3727}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Operator MARK panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換分離のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換分離として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using PING {#c32-i3728}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using PINGは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using SNAMAP {#c32-i3729}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using SNAMAPは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書分離のユーザーズガイド 操作でネットビューの運用確認を行います。Using SNAMAP の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書分離で再確認できる形にする。 ✅
    - D. Using SNAMAP の属性行を読まず上書分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では Using SNAMAP は「IBM Z NetViewで Using SNAMAP の扱いを記録する上書分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では Using SNAMAP の表示結果と DSI633I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では Using SNAMAP の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using SNAMAP pop-up commands {#c32-i3730}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using SNAMAP pop-up commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力分離のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して出力分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力分離の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける出力分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using SNMP Management {#c32-i3731}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using SNMP Managementは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using SNMPView {#c32-i3732}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using SNMPViewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切分離のユーザーズガイド 操作で Using SNMPViewの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using SNMPViewの出力を取らず区切分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を区切分離で確認する。 ✅
    - C. BROWSE CANZLOG を省略して区切分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では Using SNMPView は「区切分離のユーザーズガイド 操作に関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では Using SNMPViewの属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では Using SNMPViewを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Session Monitor Filters {#c32-i3733}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Session Monitor Filtersは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索分離のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、探索分離の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して探索分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では Using 機能 は「探索分離のユーザーズガイド 操作に関係する定義値と表示行を照合する探索分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using TRACERTE {#c32-i3734}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using TRACERTEは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Using Tivoli Workload Scheduler for z/OS {#c32-i3735}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Tivoli Workload Scheduler for z/OSは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文検分のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文検分の確認にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して構文検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Topology Server Command Exits {#c32-i3736}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using Topology Server Command Exitsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開検分のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず展開検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、展開検分の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して展開検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Using 機能 は「展開検分のユーザーズガイド 操作に関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using VTAM Commands (SNA Subarea, SNA Advanced Peer-to-Peer Networking) {#c32-i3737}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using VTAM Commands (SNA Subarea, SNA Advanced Peer-to-Peer Networking)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端検分のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端検分の根拠を固定する。 ✅
    - B. Using 機能の名称と担当者名のみを残して終端検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Vital Product Data {#c32-i3738}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Vital Product Dataは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換検分のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換検分の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は置換検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using Z Decision Support {#c32-i3739}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using Z Decision Supportは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検分のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を探索検分で確認する。 ✅
    - C. BROWSE CANZLOG を省略して探索検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Using 機能 は「探索検分のユーザーズガイド 操作に関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using and Maintaining Canzlog Data {#c32-i3740}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using and Maintaining Canzlog Dataは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端記録のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端記録の根拠を固定する。 ✅
    - B. Using 機能の名称と担当者名のみを残して終端記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using and Maintaining the Network Log {#c32-i3741}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using and Maintaining the Network Logは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索記録のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を探索記録で確認する。 ✅
    - C. BROWSE CANZLOG を省略して探索記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Using 機能 は「探索記録のユーザーズガイド 操作に関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using and Maintaining the RODM Log {#c32-i3742}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using and Maintaining the RODM Logは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書記録のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録のユーザーズガイド 操作を確認した扱いにする。
    - B. EKG000I の有無を確認せず上書記録のユーザーズガイド 操作を正常終了として記録する。
    - C. RODMVIEW の結果から対象行を抜き出し、上書記録の証跡として残す。 ✅
    - D. Using 機能の属性行を読まず上書記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する上書記録項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Using 機能の表示結果と EKG000I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Using 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using and Maintaining the Session Monitor Database {#c32-i3743}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using and Maintaining the Session Monitor Databaseは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力記録のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して出力記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力記録の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using support functions {#c32-i3744}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using support functionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲分離のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、範囲分離の証跡として残す。 ✅
    - D. Using 機能の属性行を読まず範囲分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では Using 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the AON/TCP Operator Interface {#c32-i3745}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the AON/TCP Operator Interfaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 技術項目「Using the AON/TCP Operator Interface」の確認として、展開照合権限の展開照合として AON/TCP を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 展開照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正解はDです。展開照合権限で扱う AON/TCP は Tivoli NetView z/OS 自動化 の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として AON/TCP を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Command Profile Editor Batch Utility {#c32-i3746}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Command Profile Editor Batch Utilityは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較分離のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず比較分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、比較分離の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して比較分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では Using 機能 は「比較分離のユーザーズガイド 操作に関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Common Global Editor {#c32-i3747}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Common Global Editorは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序分離のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、順序分離の採否を説明欄に結び付ける。 ✅
    - D. Using 機能の属性行を読まず順序分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では Using 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Common Global Variable Command Processor (CGLOBAL) {#c32-i3748}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Common Global Variable Command Processor (CGLOBAL)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域分離のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して値域分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域分離として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Dynamic Display Facility (DDF) {#c32-i3749}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Dynamic Display Facility (DDF)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧分離のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず復旧分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧分離の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Using 機能 は「復旧分離のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the FKVXITAN Exit Routine {#c32-i3750}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using the FKVXITAN Exit Routineは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査分離のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査分離で再確認できる形にする。 ✅
    - D. Using 機能の属性行を読まず監査分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Using 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Hardware Monitor {#c32-i3751}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Hardware Monitorは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更分離のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して変更分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更分離の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Hardware Monitor Panels {#c32-i3752}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Hardware Monitor Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文読解のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文読解の根拠を固定する。 ✅
    - B. Using 機能の名称と担当者名のみを残して構文読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Help Facility Main Menu {#c32-i3753}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Help Facility Main Menuは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開読解のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず展開読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を展開読解で確認する。 ✅
    - C. BROWSE CANZLOG を省略して展開読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では Using 機能 は「展開読解のユーザーズガイド 操作に関係する定義値と表示行を照合する展開読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the IP Management Panels {#c32-i3754}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the IP Management Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換読解のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換読解の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は置換読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Inform Log utility {#c32-i3755}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Inform Log utilityは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出読解のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出読解のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、呼出読解の証跡として残す。 ✅
    - D. Using 機能の属性行を読まず呼出読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する呼出読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では Using 機能の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the MVS System Log (SYSLOG) {#c32-i3756}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the MVS System Log (SYSLOG)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端読解のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端読解の根拠にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して終端読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する終端読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NetView Automation Table {#c32-i3757}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Using the NetView Automation Tableは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索読解のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と DSI633I を読み、探索読解の結果として保存する。 ✅
    - C. BROWSE CANZLOG を省略して探索読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では Using 機能 は「探索読解のユーザーズガイド 操作に関係する定義値と表示行を照合する探索読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NetView Enterprise Management Agent {#c32-i3758}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the NetView Enterprise Management Agentは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書読解のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書読解のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG で得た表示本文を使い、上書読解の採否を説明欄に結び付ける。 ✅
    - D. Using 機能の属性行を読まず上書読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する上書読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では Using 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NetView Help Desk {#c32-i3759}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the NetView Help Deskは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力読解のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して出力読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力読解として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける出力読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は出力読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NetView Host Help {#c32-i3760}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the NetView Host Helpは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件読解のユーザーズガイド 操作に関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件読解の確認にする。 ✅
    - B. Using 機能の名称と担当者名のみを残して条件読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では Using 機能 は「Using 機能の用途をネットビューの表示で確認する条件読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM Z NetViewの Using 機能と DSI633I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では Using 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NetView Management Console {#c32-i3761}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切読解のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず区切読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、区切読解の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して区切読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では Using 機能 は「区切読解のユーザーズガイド 操作に関係する定義値と表示行を照合する区切読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the NetView Program {#c32-i3762}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲読解のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲読解のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、範囲読解で再確認できる形にする。 ✅
    - D. Using 機能の属性行を読まず範囲読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する範囲読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では Using 機能の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the RODMView Panels {#c32-i3763}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the RODMView Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先読解のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず優先読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して優先読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、優先読解の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける優先読解項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では Using 機能の出力行と EKG000I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は優先読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the SNA Help Desk {#c32-i3764}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the SNA Help Deskは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域読解のユーザーズガイド 操作に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して値域読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域読解の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける値域読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では Using 機能の出力行と DSI633I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では Using 機能を IBM Z NetViewの確認記録に残し、対象名は値域読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Servlets {#c32-i3765}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Servletsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録読解のユーザーズガイド 操作に関係する Using the Servletsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録読解の根拠を固定する。 ✅
    - B. Using the Servletsの名称と担当者名のみを残して記録読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Using the Servlets は「Using the Servletsの用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの Using the Servletsと DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Using the Servletsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Session Monitor (SNA Subarea, SNA Advanced Peer-to-Peer Networking) {#c32-i3766}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Session Monitor (SNA Subarea, SNA Advanced Peer-to-Peer Networking)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較読解のユーザーズガイド 操作で Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず比較読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を比較読解で確認する。 ✅
    - C. BROWSE CANZLOG を省略して比較読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Using 機能 は「比較読解のユーザーズガイド 操作に関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Using 機能の属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Using 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Using the Session Monitor Panels {#c32-i3767}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Using the Session Monitor Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序読解のユーザーズガイド 操作でネットビューの運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、順序読解の証跡として残す。 ✅
    - D. Using 機能の属性行を読まず順序読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Using 機能 は「IBM Z NetViewで Using 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Using 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Using 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


