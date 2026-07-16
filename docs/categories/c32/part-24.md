---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (24/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > ユーザーズガイド (操作)

### Initiating Error Recovery (Status Monitor) {#c32-i3481}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Initiating Error Recovery (Status Monitor)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.239) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.239)

??? question "確認問題（1問）"
    **問題.** 呼出検査のユーザーズガイド 操作でネットビューの運用確認を行います。Initiating 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検査のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、呼出検査の点検結果を残す。 ✅
    - D. Initiating 機能の属性行を読まず呼出検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では Initiating 機能 は「IBM Z NetViewで Initiating 機能の扱いを記録する呼出検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では Initiating 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では Initiating 機能の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Installing and Customizing the NetView Management Console {#c32-i3482}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Installing and Customizing the NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端検査のユーザーズガイド 操作に関係する Installing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端検査の確認値として扱う。 ✅
    - B. Installing 機能の名称と担当者名のみを残して終端検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Installing 機能 は「Installing 機能の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの Installing 機能と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Installing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Installing the Examples {#c32-i3483}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Installing the Examplesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検査のユーザーズガイド 操作で Installing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Installing 機能の出力を取らず探索検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索検査の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して探索検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では Installing 機能 は「探索検査のユーザーズガイド 操作に関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では Installing 機能の属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では Installing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Installing the NetView Management Console {#c32-i3484}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Installing the NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書検査のユーザーズガイド 操作でネットビューの運用確認を行います。Installing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検査のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を上書検査で確認する。 ✅
    - D. Installing 機能の属性行を読まず上書検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では Installing 機能 は「IBM Z NetViewで Installing 機能の扱いを記録する上書検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では Installing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では Installing 機能の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Integrating Captured Views into the Demonstration {#c32-i3485}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Integrating Captured Views into the Demonstrationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力検査のユーザーズガイド 操作に関する Integrating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Integrating 機能の変更点を出力本文から切り離して出力検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、出力検査の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では Integrating 機能 は「Integrating 機能の状態と出力メッセージを結び付ける出力検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では Integrating 機能の出力行と DSI633I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では Integrating 機能を IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Interpreting Session Data {#c32-i3486}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Interpreting Session Dataは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.275) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.275)

??? question "確認問題（1問）"
    **問題.** 条件検査のユーザーズガイド 操作に関係する Interpreting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件検査の確認記録にまとめる。 ✅
    - B. Interpreting 機能の名称と担当者名のみを残して条件検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では Interpreting 機能 は「Interpreting 機能の用途をネットビューの表示で確認する条件検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの Interpreting 機能と DSI633I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では Interpreting 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Introducing AON customization {#c32-i3487}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Introducing AON customizationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.201) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.201)

??? question "確認問題（1問）"
    **問題.** 区切検査のユーザーズガイド 操作で Introducing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Introducing 機能の出力を取らず区切検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検査の根拠にする。 ✅
    - C. AONSTAT を省略して区切検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では Introducing 機能 は「区切検査のユーザーズガイド 操作に関係する定義値と表示行を照合する区切検査項目」と AONSTAT または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では Introducing 機能の属性行と EZL000I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では Introducing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Introducing Automated Operation Network (AON) {#c32-i3488}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Introducing Automated Operation Network (AON)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.31) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.31)

??? question "確認問題（1問）"
    **問題.** 範囲検査のユーザーズガイド 操作でネットビューの運用確認を行います。Introducing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査のユーザーズガイド 操作を確認した扱いにする。
    - B. EZL000I の有無を確認せず範囲検査のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と EZL000I を読み、範囲検査の結果として保存する。 ✅
    - D. Introducing 機能の属性行を読まず範囲検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では Introducing 機能 は「IBM Z NetViewで Introducing 機能の扱いを記録する範囲検査項目」と AONSTAT または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では Introducing 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では Introducing 機能の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Introducing Automated Operations Network {#c32-i3489}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Introducing Automated Operations Networkは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.29) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.29)

??? question "確認問題（1問）"
    **問題.** 優先検査のユーザーズガイド 操作に関する Introducing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Introducing 機能の変更点を出力本文から切り離して優先検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、優先検査の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では Introducing 機能 は「Introducing 機能の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では Introducing 機能の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では Introducing 機能を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Introducing the AON/TCP Operator Interface {#c32-i3490}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Introducing the AON/TCP Operator Interfaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録検査のIntroducing the AON/TCP Operator Interfaceに関係する Introducing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録検査として引き継ぐ。 ✅
    - B. Introducing 機能の名称と担当者名のみを残して記録検査のIntroducing the AON/TCP Operator Interfaceの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査のIntroducing the AON/TCP Operator Interfaceを確認し同じ証跡として扱ったことにする。
    - D. EZL000I の有無を見ず記録検査のIntroducing the AON/TCP Operator Interfaceの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では Introducing 機能 は「Introducing 機能の用途をネットビューの表示で確認する記録検査項目」と AONSTAT または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの Introducing 機能と EZL000I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では Introducing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Introduction {#c32-i3491}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Introductionは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Introduction to the NetView Management Console {#c32-i3492}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Introduction to the NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 順序検査のユーザーズガイド 操作でネットビューの運用確認を行います。Introduction 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、順序検査の点検結果を残す。 ✅
    - D. Introduction 機能の属性行を読まず順序検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Introduction 機能 は「IBM Z NetViewで Introduction 機能の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Introduction 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Introduction 機能の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Issuing Commands {#c32-i3493}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Issuing Commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告検査のユーザーズガイド 操作に関係する Issuing Commandsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告検査の確認値として扱う。 ✅
    - B. Issuing Commandsの名称と担当者名のみを残して警告検査のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検査のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では Issuing Commands は「Issuing Commandsの用途をネットビューの表示で確認する警告検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの Issuing Commandsと DSI633I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では Issuing Commandsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Issuing Dynamic Display Facility (DDF) commands {#c32-i3494}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Issuing Dynamic Display Facility (DDF) commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧検査のユーザーズガイド 操作で Issuing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Issuing 機能の出力を取らず復旧検査のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧検査の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では Issuing 機能 は「復旧検査のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では Issuing 機能の属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では Issuing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Issuing Resource State Reminders (EZLESRMD) {#c32-i3495}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Issuing Resource State Reminders (EZLESRMD)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査検査のユーザーズガイド 操作でネットビューの運用確認を行います。Issuing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を監査検査で確認する。 ✅
    - D. Issuing 機能の属性行を読まず監査検査のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では Issuing 機能 は「IBM Z NetViewで Issuing 機能の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では Issuing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では Issuing 機能の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Issuing VTAM commands {#c32-i3496}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Issuing VTAM commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更検査のユーザーズガイド 操作に関する Issuing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Issuing 機能の変更点を出力本文から切り離して変更検査のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更検査の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では Issuing 機能 は「Issuing 機能の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では Issuing 機能の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では Issuing 機能を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Java Applications {#c32-i3497}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Java Applicationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.53) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.53)

??? question "確認問題（1問）"
    **問題.** 構文判定のユーザーズガイド 操作に関係する Java Applicationsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文判定の確認記録にまとめる。 ✅
    - B. Java Applicationsの名称と担当者名のみを残して構文判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では Java Applications は「Java Applicationsの用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの Java Applicationsと DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では Java Applicationsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Java Plug-Ins {#c32-i3498}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Java Plug-Insは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.56) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.56)

??? question "確認問題（1問）"
    **問題.** 展開判定のユーザーズガイド 操作で Java Plug-Insの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Java Plug-Insの出力を取らず展開判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開判定の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して展開判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では Java Plug-Ins は「展開判定のユーザーズガイド 操作に関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では Java Plug-Insの属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では Java Plug-Insを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Launching and Using the NetView Management Console from Other Applications {#c32-i3499}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Launching and Using the NetView Management Console from Other Applicationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出判定のユーザーズガイド 操作でネットビューの運用確認を行います。Launching 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、呼出判定の結果として保存する。 ✅
    - D. Launching 機能の属性行を読まず呼出判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では Launching 機能 は「IBM Z NetViewで Launching 機能の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では Launching 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では Launching 機能の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Line Failure (Hardware Monitor) {#c32-i3500}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Line Failure (Hardware Monitor)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.250) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.250)

??? question "確認問題（1問）"
    **問題.** 置換判定のユーザーズガイド 操作に関する Line Failure 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Line Failure 属性の変更点を出力本文から切り離して置換判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、置換判定の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では Line Failure 属性 は「Line Failure 属性の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では Line Failure 属性の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では Line Failure 属性を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Linux on z Systems Workload Server Details Workspace {#c32-i3501}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Linux on z Systems Workload Server Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端判定のユーザーズガイド 操作に関係する Linux 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端判定として引き継ぐ。 ✅
    - B. Linux 機能の名称と担当者名のみを残して終端判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では Linux 機能 は「Linux 機能の用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの Linux 機能と DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では Linux 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Load Balancer Groups Attributes {#c32-i3502}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Load Balancer Groups Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.146) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.146)

??? question "確認問題（1問）"
    **問題.** 探索判定のユーザーズガイド 操作で Load 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Load 機能の出力を取らず探索判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索判定の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して探索判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では Load 機能 は「探索判定のユーザーズガイド 操作に関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では Load 機能の属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では Load 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Load Balancer Groups Workspace {#c32-i3503}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Load Balancer Groups Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.81) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.81)

??? question "確認問題（1問）"
    **問題.** 上書判定のユーザーズガイド 操作でネットビューの運用確認を行います。Load 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書判定の点検結果を残す。 ✅
    - D. Load 機能の属性行を読まず上書判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では Load 機能 は「IBM Z NetViewで Load 機能の扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では Load 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では Load 機能の使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Load Balancer Workloads Workspace {#c32-i3504}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Load Balancer Workloads Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.82) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.82)

??? question "確認問題（1問）"
    **問題.** 出力判定のユーザーズガイド 操作に関する Load 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Load 機能の変更点を出力本文から切り離して出力判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力判定で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では Load 機能 は「Load 機能の状態と出力メッセージを結び付ける出力判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では Load 機能の出力行と DSI633I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では Load 機能を IBM Z NetViewの確認記録に残し、対象名は出力判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Load Balancers Attributes {#c32-i3505}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Load Balancers Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.147) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.147)

??? question "確認問題（1問）"
    **問題.** 条件判定のユーザーズガイド 操作に関係する Load 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件判定の確認値として扱う。 ✅
    - B. Load 機能の名称と担当者名のみを残して条件判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Load 機能 は「Load 機能の用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの Load 機能と DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Load 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Load Balancers Workspace {#c32-i3506}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Load Balancers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.83) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.83)

??? question "確認問題（1問）"
    **問題.** 区切判定のユーザーズガイド 操作で Load 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Load 機能の出力を取らず区切判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切判定の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して区切判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Load 機能 は「区切判定のユーザーズガイド 操作に関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Load 機能の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Load 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Loading a panel member (DDFPANEL) {#c32-i3507}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Loading a panel member (DDFPANEL)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲判定のユーザーズガイド 操作でネットビューの運用確認を行います。Loading 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を範囲判定で確認する。 ✅
    - D. Loading 機能の属性行を読まず範囲判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では Loading 機能 は「IBM Z NetViewで Loading 機能の扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では Loading 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では Loading 機能の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Loading panels {#c32-i3508}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Loading panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先判定のユーザーズガイド 操作に関する Loading panelsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Loading panelsの変更点を出力本文から切り離して優先判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、優先判定の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では Loading panels は「Loading panelsの状態と出力メッセージを結び付ける優先判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では Loading panelsの出力行と DSI633I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では Loading panelsを IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Loading tree members (DDFTREE) {#c32-i3509}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Loading tree members (DDFTREE)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録判定のユーザーズガイド 操作に関係する Loading 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録判定の確認記録にまとめる。 ✅
    - B. Loading 機能の名称と担当者名のみを残して記録判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では Loading 機能 は「Loading 機能の用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewの Loading 機能と DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では Loading 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Loading tree structures {#c32-i3510}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Loading tree structuresは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較判定のユーザーズガイド 操作で Loading 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Loading 機能の出力を取らず比較判定のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較判定の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して比較判定のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Loading 機能 は「比較判定のユーザーズガイド 操作に関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Loading 機能の属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Loading 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Log File Interface Command (EZLLOG) {#c32-i3511}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Log File Interface Command (EZLLOG)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.298) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.298)

??? question "確認問題（1問）"
    **問題.** 警告判定のユーザーズガイド 操作に関係する Log 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告判定として引き継ぐ。 ✅
    - B. Log 機能の名称と担当者名のみを残して警告判定のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では Log 機能 は「Log 機能の用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewの Log 機能と DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では Log 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MQ Workload Clusters Details Workspace {#c32-i3512}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

MQ Workload Clusters Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.84) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.84)

??? question "確認問題（1問）"
    **問題.** 区切記録のユーザーズガイド 操作で MQ 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MQ 機能の出力を取らず区切記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切記録の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して区切記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では MQ 機能 は「区切記録のユーザーズガイド 操作に関係する定義値と表示行を照合する区切記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では MQ 機能の属性行と DSI633I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では MQ 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Maintaining Objects and Relationships in RODM {#c32-i3513}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Maintaining Objects and Relationships in RODMは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更判定のユーザーズガイド 操作に関する Maintaining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず変更判定のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Maintaining 機能の変更点を出力本文から切り離して変更判定のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更判定で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Maintaining 機能 は「Maintaining 機能の状態と出力メッセージを結び付ける変更判定項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Maintaining 機能の出力行と EKG000I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Maintaining 機能を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Maintaining databases {#c32-i3514}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Maintaining databasesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査判定のユーザーズガイド 操作でネットビューの運用確認を行います。Maintaining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、監査判定の点検結果を残す。 ✅
    - D. Maintaining 機能の属性行を読まず監査判定のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Maintaining 機能 は「IBM Z NetViewで Maintaining 機能の扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Maintaining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Maintaining 機能の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Maintaining the Automation Table {#c32-i3515}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Maintaining the Automation Tableは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文整理のユーザーズガイド 操作に関係する Maintaining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文整理の確認値として扱う。 ✅
    - B. Maintaining 機能の名称と担当者名のみを残して構文整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では Maintaining 機能 は「Maintaining 機能の用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの Maintaining 機能と DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では Maintaining 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Maintaining the Hardware Monitor Database {#c32-i3516}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Maintaining the Hardware Monitor Databaseは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開整理のユーザーズガイド 操作で Maintaining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Maintaining 機能の出力を取らず展開整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開整理の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して展開整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では Maintaining 機能 は「展開整理のユーザーズガイド 操作に関係する定義値と表示行を照合する展開整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では Maintaining 機能の属性行と DSI633I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では Maintaining 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Maintaining the NetView Program {#c32-i3517}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Maintaining the NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出整理のユーザーズガイド 操作でネットビューの運用確認を行います。Maintaining 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を呼出整理で確認する。 ✅
    - D. Maintaining 機能の属性行を読まず呼出整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では Maintaining 機能 は「IBM Z NetViewで Maintaining 機能の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では Maintaining 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では Maintaining 機能の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Maintaining the Save/Restore Database {#c32-i3518}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Maintaining the Save/Restore Databaseは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として Maintaining the Save/Restore を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正解はDです。構文照合保守で扱う Maintaining the Save/Restore は Tivoli NetView z/OS 自動化 の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として Maintaining the Save/Restore を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Automation Tables (AUTOCMD/EZLEF002) {#c32-i3519}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Managing Automation Tables (AUTOCMD/EZLEF002)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端整理のユーザーズガイド 操作に関係する Managing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端整理の確認記録にまとめる。 ✅
    - B. Managing 機能の名称と担当者名のみを残して終端整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では Managing 機能 は「Managing 機能の用途をネットビューの表示で確認する終端整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの Managing 機能と DSI633I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では Managing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Cross-Domain Operator Sessions {#c32-i3520}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing Cross-Domain Operator Sessionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書整理のユーザーズガイド 操作でネットビューの運用確認を行います。Managing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、上書整理の結果として保存する。 ✅
    - D. Managing 機能の属性行を読まず上書整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では Managing 機能 は「IBM Z NetViewで Managing 機能の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では Managing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では Managing 機能の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing IP Servers {#c32-i3521}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing IP Serversは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件整理のユーザーズガイド 操作に関係する Managing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件整理として引き継ぐ。 ✅
    - B. Managing 機能の名称と担当者名のみを残して条件整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では Managing 機能 は「Managing 機能の用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの Managing 機能と DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では Managing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing NetView Data {#c32-i3522}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing NetView Dataは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 範囲整理のユーザーズガイド 操作でネットビューの運用確認を行います。Managing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、範囲整理の点検結果を残す。 ✅
    - D. Managing 機能の属性行を読まず範囲整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Managing 機能 は「IBM Z NetViewで Managing 機能の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Managing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Managing 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Network Inventory {#c32-i3523}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing Network Inventoryは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録整理のユーザーズガイド 操作に関係する Managing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録整理の確認値として扱う。 ✅
    - B. Managing 機能の名称と担当者名のみを残して記録整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では Managing 機能 は「Managing 機能の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの Managing 機能と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では Managing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing Network and System Status {#c32-i3524}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing Network and System Statusは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先整理のユーザーズガイド 操作に関する Managing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Managing 機能の変更点を出力本文から切り離して優先整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先整理で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では Managing 機能 は「Managing 機能の状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では Managing 機能の出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では Managing 機能を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing cross-domain gateway sessions {#c32-i3525}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing cross-domain gateway sessionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索整理のユーザーズガイド 操作で Managing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Managing 機能の出力を取らず探索整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索整理の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して探索整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Managing 機能 は「探索整理のユーザーズガイド 操作に関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Managing 機能の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Managing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing full-screen TAF sessions {#c32-i3526}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Managing full-screen TAF sessionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力整理のユーザーズガイド 操作に関する Managing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Managing 機能の変更点を出力本文から切り離して出力整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、出力整理の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では Managing 機能 は「Managing 機能の状態と出力メッセージを結び付ける出力整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では Managing 機能の出力行と DSI633I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では Managing 機能を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Managing multiple automation tables {#c32-i3527}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Managing multiple automation tablesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（2問）"
    **問題.** 区切整理のユーザーズガイド 操作で Managing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Managing 機能の出力を取らず区切整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切整理の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して区切整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では Managing 機能 は「区切整理のユーザーズガイド 操作に関係する定義値と表示行を照合する区切整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では Managing 機能の属性行と DSI633I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では Managing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

    ---

    **問題.** 条件記録の自動化テーブル 状態判定に関係する Managing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件記録の確認にする。 ✅
    - B. Managing 機能の名称と担当者名のみを残して条件記録の自動化テーブル 状態判定の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録の自動化テーブル 状態判定を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件記録の自動化テーブル 状態判定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Managing 機能 は「Managing 機能の用途をネットビューの表示で確認する条件記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの Managing 機能と DSI633I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Managing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Measuring Response Time with Control Units Using RTM (Session Monitor) {#c32-i3528}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Measuring Response Time with Control Units Using RTM (Session Monitor)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較整理のユーザーズガイド 操作で Measuring 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Measuring 機能の出力を取らず比較整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較整理の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して比較整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では Measuring 機能 は「比較整理のユーザーズガイド 操作に関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では Measuring 機能の属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では Measuring 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Message Codes {#c32-i3529}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Message Codesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView (p.260) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.260)

??? question "確認問題（1問）"
    **問題.** 値域整理のユーザーズガイド 操作に関する Message Codesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Message Codesの変更点を出力本文から切り離して値域整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、値域整理の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Message Codes は「Message Codesの状態と出力メッセージを結び付ける値域整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Message Codesの出力行と DSI633I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Message Codesを IBM Z NetViewの確認記録に残し、対象名は値域整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Message Formats {#c32-i3530}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Message Formatsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView (p.259) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.259)

??? question "確認問題（1問）"
    **問題.** 警告整理のユーザーズガイド 操作に関係する Message Formatsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告整理の確認記録にまとめる。 ✅
    - B. Message Formatsの名称と担当者名のみを残して警告整理のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告整理のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告整理のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Message Formats は「Message Formatsの用途をネットビューの表示で確認する警告整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では IBM Z NetViewの Message Formatsと DSI633I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Message Formatsを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Modifying DDF panels {#c32-i3531}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Modifying DDF panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧整理のユーザーズガイド 操作で Modifying 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Modifying 機能の出力を取らず復旧整理のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧整理の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧整理のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Modifying 機能 は「復旧整理のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Modifying 機能の属性行と DSI633I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Modifying 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Modifying the Control File for DDF {#c32-i3532}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Modifying the Control File for DDFは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査整理のユーザーズガイド 操作でネットビューの運用確認を行います。Modifying 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、監査整理の結果として保存する。 ✅
    - D. Modifying 機能の属性行を読まず監査整理のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Modifying 機能 は「IBM Z NetViewで Modifying 機能の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Modifying 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Modifying 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Modifying the EZLTREE tree structure {#c32-i3533}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Modifying the EZLTREE tree structureは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更整理のユーザーズガイド 操作に関する Modifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Modifying 機能の変更点を出力本文から切り離して変更整理のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、変更整理の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では Modifying 機能 は「Modifying 機能の状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では Modifying 機能の出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では Modifying 機能を IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Modifying the Server Properties File {#c32-i3534}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Modifying the Server Properties Fileは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 構文記録のユーザーズガイド 操作に関係する Modifying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文記録として引き継ぐ。 ✅
    - B. Modifying 機能の名称と担当者名のみを残して構文記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では Modifying 機能 は「Modifying 機能の用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの Modifying 機能と DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では Modifying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring Hardware and Software Problems {#c32-i3535}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring Hardware and Software Problemsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 終端記録のユーザーズガイド 操作に関係する Monitoring 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端記録の確認値として扱う。 ✅
    - B. Monitoring 機能の名称と担当者名のみを残して終端記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では Monitoring 機能 は「Monitoring 機能の用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの Monitoring 機能と DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では Monitoring 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring LUDRPOOL utilization {#c32-i3536}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring LUDRPOOL utilizationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索記録のユーザーズガイド 操作で Monitoring 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Monitoring 機能の出力を取らず探索記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索記録の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して探索記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Monitoring 機能 は「探索記録のユーザーズガイド 操作に関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Monitoring 機能の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Monitoring 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring Network Resources {#c32-i3537}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring Network Resourcesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書記録のユーザーズガイド 操作でネットビューの運用確認を行います。Monitoring 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を上書記録で確認する。 ✅
    - D. Monitoring 機能の属性行を読まず上書記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Monitoring 機能 は「IBM Z NetViewで Monitoring 機能の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Monitoring 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Monitoring 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring Switched Virtual Circuit (SVC) resource utilization {#c32-i3538}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring Switched Virtual Circuit (SVC) resource utilizationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 出力記録のユーザーズガイド 操作に関する Monitoring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Monitoring 機能の変更点を出力本文から切り離して出力記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、出力記録の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Monitoring 機能 は「Monitoring 機能の状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Monitoring 機能の出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Monitoring 機能を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring and Controlling Network Configuration {#c32-i3539}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring and Controlling Network Configurationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開記録のユーザーズガイド 操作で Monitoring 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Monitoring 機能の出力を取らず展開記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開記録の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して展開記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Monitoring 機能 は「展開記録のユーザーズガイド 操作に関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Monitoring 機能の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Monitoring 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring and Controlling Your Network from a Workstation {#c32-i3540}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring and Controlling Your Network from a Workstationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換記録のユーザーズガイド 操作に関する Monitoring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Monitoring 機能の変更点を出力本文から切り離して置換記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換記録で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Monitoring 機能 は「Monitoring 機能の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Monitoring 機能の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Monitoring 機能を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Monitoring and Controlling the Network and System {#c32-i3541}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Monitoring and Controlling the Network and Systemは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 呼出記録のユーザーズガイド 操作でネットビューの運用確認を行います。Monitoring 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、呼出記録の点検結果を残す。 ✅
    - D. Monitoring 機能の属性行を読まず呼出記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Monitoring 機能 は「IBM Z NetViewで Monitoring 機能の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Monitoring 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Monitoring 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Moving VTAM Resources (EZLEVMOV) {#c32-i3542}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Moving VTAM Resources (EZLEVMOV)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.344) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.344)

??? question "確認問題（1問）"
    **問題.** 条件記録のユーザーズガイド 操作に関係する Moving 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件記録の確認記録にまとめる。 ✅
    - B. Moving 機能の名称と担当者名のみを残して条件記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Moving 機能 は「Moving 機能の用途をネットビューの表示で確認する条件記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの Moving 機能と DSI633I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Moving 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NCCF Message Format {#c32-i3543}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NCCF Message Formatは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView (p.259) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.259)

??? question "確認問題（1問）"
    **問題.** 順序記録のユーザーズガイド 操作でネットビューの運用確認を行います。NCCF 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、順序記録の点検結果を残す。 ✅
    - D. NCCF 機能の属性行を読まず順序記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では NCCF 機能 は「IBM Z NetViewで NCCF 機能の扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では NCCF 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では NCCF 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NCP VTAM messages {#c32-i3544}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

NCP VTAM messagesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.419) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.419)

??? question "確認問題（1問）"
    **問題.** 警告記録のユーザーズガイド 操作に関係する NCP VTAM messagesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告記録の確認値として扱う。 ✅
    - B. NCP VTAM messagesの名称と担当者名のみを残して警告記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では NCP VTAM messages は「NCP VTAM messagesの用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの NCP VTAM messagesと DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では NCP VTAM messagesを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NCP recovery definitions {#c32-i3545}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NCP recovery definitionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.135) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.135)

??? question "確認問題（1問）"
    **問題.** 値域記録のユーザーズガイド 操作に関する NCP 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. NCP 機能の変更点を出力本文から切り離して値域記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域記録で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では NCP 機能 は「NCP 機能の状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では NCP 機能の出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では NCP 機能を IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Navigating Network Views {#c32-i3546}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Navigating Network Viewsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.92) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.92)

??? question "確認問題（1問）"
    **問題.** 優先記録のユーザーズガイド 操作に関する Navigating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Navigating 機能の変更点を出力本文から切り離して優先記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、優先記録の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Navigating 機能 は「Navigating 機能の状態と出力メッセージを結び付ける優先記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Navigating 機能の出力行と DSI633I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Navigating 機能を IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Navigating the Hardware Monitor Panel Hierarchy {#c32-i3547}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Navigating the Hardware Monitor Panel Hierarchyは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録記録のユーザーズガイド 操作に関係する Navigating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録記録として引き継ぐ。 ✅
    - B. Navigating 機能の名称と担当者名のみを残して記録記録のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Navigating 機能 は「Navigating 機能の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの Navigating 機能と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Navigating 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Navigating through AON panels {#c32-i3548}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Navigating through AON panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.36) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.36)

??? question "確認問題（1問）"
    **問題.** 比較記録のユーザーズガイド 操作で Navigating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Navigating 機能の出力を取らず比較記録のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較記録の確認にする。 ✅
    - C. AONSTAT を省略して比較記録のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Navigating 機能 は「比較記録のユーザーズガイド 操作に関係する定義値と表示行を照合する比較記録項目」と AONSTAT または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Navigating 機能の属性行と EZL000I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Navigating 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Applications Attributes {#c32-i3549}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Applications Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.147) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.147)

??? question "確認問題（1問）"
    **問題.** 監査記録のユーザーズガイド 操作でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を監査記録で確認する。 ✅
    - D. NetView 機能の属性行を読まず監査記録のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では NetView 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Applications Workspace {#c32-i3550}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Applications Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.61) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.61)

??? question "確認問題（1問）"
    **問題.** 変更記録のユーザーズガイド 操作に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して変更記録のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更記録の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Audit Log Attributes {#c32-i3551}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Audit Log Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.149) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.149)

??? question "確認問題（1問）"
    **問題.** 構文分離のユーザーズガイド 操作に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文分離の確認記録にまとめる。 ✅
    - B. NetView 機能の名称と担当者名のみを残して構文分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する構文分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Audit Log Workspace {#c32-i3552}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Audit Log Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.66) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.66)

??? question "確認問題（1問）"
    **問題.** 展開分離のユーザーズガイド 操作で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず展開分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開分離の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して展開分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では NetView 機能 は「展開分離のユーザーズガイド 操作に関係する定義値と表示行を照合する展開分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Command Response Attributes {#c32-i3553}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Command Response Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.149) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.149)

??? question "確認問題（1問）"
    **問題.** 呼出分離のユーザーズガイド 操作でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、呼出分離の結果として保存する。 ✅
    - D. NetView 機能の属性行を読まず呼出分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する呼出分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では NetView 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Command Response Workspace {#c32-i3554}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Command Response Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.67) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.67)

??? question "確認問題（1問）"
    **問題.** 置換分離のユーザーズガイド 操作に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して置換分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、置換分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける置換分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Component Hierarchies {#c32-i3555}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Component Hierarchiesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.261) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.261)

??? question "確認問題（1問）"
    **問題.** 終端分離のユーザーズガイド 操作に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端分離として引き継ぐ。 ✅
    - B. NetView 機能の名称と担当者名のみを残して終端分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する終端分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Enterprise Management Agent Introduction {#c32-i3556}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Enterprise Management Agent Introductionは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.17) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.17)

??? question "確認問題（1問）"
    **問題.** 探索分離のユーザーズガイド 操作で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず探索分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索分離の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して探索分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では NetView 機能 は「探索分離のユーザーズガイド 操作に関係する定義値と表示行を照合する探索分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Enterprise Management Agent Overview {#c32-i3557}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Enterprise Management Agent Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.19) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.19)

??? question "確認問題（1問）"
    **問題.** 上書分離のユーザーズガイド 操作でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書分離のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、上書分離の点検結果を残す。 ✅
    - D. NetView 機能の属性行を読まず上書分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する上書分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では NetView 機能の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Enterprise Management Agent Workspaces {#c32-i3558}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Enterprise Management Agent Workspacesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.31) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.31)

??? question "確認問題（1問）"
    **問題.** 出力分離のユーザーズガイド 操作に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して出力分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける出力分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Health Workspaces {#c32-i3559}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Health Workspacesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.61) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.61)

??? question "確認問題（1問）"
    **問題.** 条件分離のユーザーズガイド 操作に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件分離の確認値として扱う。 ✅
    - B. NetView 機能の名称と担当者名のみを残して条件分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する条件分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Log Attributes {#c32-i3560}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Log Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.149) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.149)

??? question "確認問題（1問）"
    **問題.** 区切分離のユーザーズガイド 操作で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず区切分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切分離の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して区切分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では NetView 機能 は「区切分離のユーザーズガイド 操作に関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Log Workspace {#c32-i3561}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Log Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.68) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.68)

??? question "確認問題（1問）"
    **問題.** 範囲分離のユーザーズガイド 操作でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を範囲分離で確認する。 ✅
    - D. NetView 機能の属性行を読まず範囲分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では NetView 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Management Console Functions {#c32-i3562}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Management Console Functionsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.76) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.76)

??? question "確認問題（1問）"
    **問題.** 優先分離のユーザーズガイド 操作に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して優先分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、優先分離の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける優先分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は優先分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Management Console Online Help {#c32-i3563}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Management Console Online Helpは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.75) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.75)

??? question "確認問題（1問）"
    **問題.** 記録分離のユーザーズガイド 操作に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録分離の確認記録にまとめる。 ✅
    - B. NetView 機能の名称と担当者名のみを残して記録分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Management Console Topology Server Databases {#c32-i3564}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Management Console Topology Server Databasesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.77) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.77)

??? question "確認問題（1問）"
    **問題.** 比較分離のユーザーズガイド 操作で NetView 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView 機能の出力を取らず比較分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較分離の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して比較分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では NetView 機能 は「比較分離のユーザーズガイド 操作に関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では NetView 機能の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では NetView 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Task Details Workspace {#c32-i3565}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Task Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.62) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.62)

??? question "確認問題（1問）"
    **問題.** 順序分離のユーザーズガイド 操作でネットビューの運用確認を行います。NetView 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、順序分離の結果として保存する。 ✅
    - D. NetView 機能の属性行を読まず順序分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では NetView 機能 は「IBM Z NetViewで NetView 機能の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では NetView 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では NetView 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Tasks Attributes {#c32-i3566}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Tasks Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.150) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.150)

??? question "確認問題（1問）"
    **問題.** 値域分離のユーザーズガイド 操作に関する NetView 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. NetView 機能の変更点を出力本文から切り離して値域分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、値域分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では NetView 機能 は「NetView 機能の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では NetView 機能の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では NetView 機能を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NetView Tasks Workspace {#c32-i3567}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

NetView Tasks Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.62) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.62)

??? question "確認問題（1問）"
    **問題.** 警告分離のユーザーズガイド 操作に関係する NetView 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告分離として引き継ぐ。 ✅
    - B. NetView 機能の名称と担当者名のみを残して警告分離のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では NetView 機能 は「NetView 機能の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの NetView 機能と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では NetView 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Network Log Message Format {#c32-i3568}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Network Log Message Formatは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Users Guide NetView (p.259) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.259)

??? question "確認問題（1問）"
    **問題.** 復旧分離のユーザーズガイド 操作で Network 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Network 機能の出力を取らず復旧分離のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧分離の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Network 機能 は「復旧分離のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Network 機能の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Network 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Network Management for Multiple Domains {#c32-i3569}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Network Management for Multiple Domainsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査分離のユーザーズガイド 操作でネットビューの運用確認を行います。Network 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、監査分離の点検結果を残す。 ✅
    - D. Network 機能の属性行を読まず監査分離のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Network 機能 は「IBM Z NetViewで Network 機能の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Network 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Network 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Network Monitoring with the Hardware Monitor Panels {#c32-i3570}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Network Monitoring with the Hardware Monitor Panelsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 変更分離のユーザーズガイド 操作に関する Network 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Network 機能の変更点を出力本文から切り離して変更分離のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では Network 機能 は「Network 機能の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では Network 機能の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では Network 機能を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Notification forwarding example {#c32-i3571}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Notification forwarding exampleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.362) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.362)

??? question "確認問題（1問）"
    **問題.** 探索読解のユーザーズガイド 操作で Notification 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Notification 機能の出力を取らず探索読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索読解の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して探索読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では Notification 機能 は「探索読解のユーザーズガイド 操作に関係する定義値と表示行を照合する探索読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では Notification 機能の属性行と DSI633I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では Notification 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Notify Policy List (EZLENTFY) {#c32-i3572}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Notify Policy List (EZLENTFY)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.330) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.330)

??? question "確認問題（1問）"
    **問題.** 上書読解のユーザーズガイド 操作でネットビューの運用確認を行います。Notify 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書読解のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、上書読解の結果として保存する。 ✅
    - D. Notify 機能の属性行を読まず上書読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Notify 機能 は「IBM Z NetViewで Notify 機能の扱いを記録する上書読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Notify 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では Notify 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Numerics {#c32-i3573}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Numericsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.427) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.427)


### OSA Channels and Ports Attributes {#c32-i3574}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

OSA Channels and Ports Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録読解のユーザーズガイド 操作に関係する OSA 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録読解の確認値として扱う。 ✅
    - B. OSA 機能の名称と担当者名のみを残して記録読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では OSA 機能 は「OSA 機能の用途をネットビューの表示で確認する記録読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの OSA 機能と DSI633I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では OSA 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### OSA Channels and Ports Workspace {#c32-i3575}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

OSA Channels and Ports Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 比較読解のユーザーズガイド 操作で OSA 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. OSA 機能の出力を取らず比較読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較読解の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して比較読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では OSA 機能 は「比較読解のユーザーズガイド 操作に関係する定義値と表示行を照合する比較読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では OSA 機能の属性行と DSI633I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では OSA 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Open Topology Interface Network Operation {#c32-i3576}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Open Topology Interface Network Operationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 区切読解のユーザーズガイド 操作で Open 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Open 機能の出力を取らず区切読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切読解の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して区切読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では Open 機能 は「区切読解のユーザーズガイド 操作に関係する定義値と表示行を照合する区切読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では Open 機能の属性行と DSI633I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では Open 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Open Topology Interface View Objects {#c32-i3577}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Open Topology Interface View Objectsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.91) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.91)

??? question "確認問題（1問）"
    **問題.** 範囲読解のユーザーズガイド 操作でネットビューの運用確認を行います。Open 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲読解のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、範囲読解の点検結果を残す。 ✅
    - D. Open 機能の属性行を読まず範囲読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Open 機能 は「IBM Z NetViewで Open 機能の扱いを記録する範囲読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Open 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では Open 機能の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Operating the NetView Management Console {#c32-i3578}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Operating the NetView Management Consoleは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先読解のユーザーズガイド 操作に関する Operating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Operating 機能の変更点を出力本文から切り離して優先読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では Operating 機能 は「Operating 機能の状態と出力メッセージを結び付ける優先読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では Operating 機能の出力行と DSI633I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では Operating 機能を IBM Z NetViewの確認記録に残し、対象名は優先読解対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Other NetView Workspaces {#c32-i3579}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Other NetView Workspacesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.65) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.65)

??? question "確認問題（1問）"
    **問題.** 順序読解のユーザーズガイド 操作でネットビューの運用確認を行います。Other 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序読解のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を順序読解で確認する。 ✅
    - D. Other 機能の属性行を読まず順序読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Other 機能 は「IBM Z NetViewで Other 機能の扱いを記録する順序読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Other 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Other 機能の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Overview {#c32-i3580}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Overviewは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### Performing task and log maintenance {#c32-i3581}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Performing task and log maintenanceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告読解のユーザーズガイド 操作に関係する Performing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告読解の確認記録にまとめる。 ✅
    - B. Performing 機能の名称と担当者名のみを残して警告読解のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告読解のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Performing 機能 は「Performing 機能の用途をネットビューの表示で確認する警告読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの Performing 機能と DSI633I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Performing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Planning Message or MSU Automation {#c32-i3582}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Planning Message or MSU Automationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 復旧読解のユーザーズガイド 操作で Planning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning 機能の出力を取らず復旧読解のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧読解の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して復旧読解のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では Planning 機能 は「復旧読解のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では Planning 機能の属性行と DSI633I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では Planning 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Preparing to Issue NetView Timer Commands {#c32-i3583}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Preparing to Issue NetView Timer Commandsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 監査読解のユーザーズガイド 操作でネットビューの運用確認を行います。Preparing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査読解のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、監査読解の結果として保存する。 ✅
    - D. Preparing 機能の属性行を読まず監査読解のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では Preparing 機能 は「IBM Z NetViewで Preparing 機能の扱いを記録する監査読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では Preparing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では Preparing 機能の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Preventing Problems {#c32-i3584}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Preventing Problemsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.237) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.237)

??? question "確認問題（1問）"
    **問題.** 変更読解のユーザーズガイド 操作に関する Preventing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更読解のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Preventing 機能の変更点を出力本文から切り離して変更読解のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、変更読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Preventing 機能 は「Preventing 機能の状態と出力メッセージを結び付ける変更読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Preventing 機能の出力行と DSI633I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Preventing 機能を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Proactive Investigating {#c32-i3585}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Proactive Investigatingは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.237) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.237)

??? question "確認問題（1問）"
    **問題.** 構文検分のユーザーズガイド 操作に関係する Proactive 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文検分として引き継ぐ。 ✅
    - B. Proactive 機能の名称と担当者名のみを残して構文検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Proactive 機能 は「Proactive 機能の用途をネットビューの表示で確認する構文検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの Proactive 機能と DSI633I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Proactive 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Problem Determination {#c32-i3586}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Problem Determinationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Management Console (p.53) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.53)

??? question "確認問題（1問）"
    **問題.** 展開検分のユーザーズガイド 操作で Problem 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Problem 機能の出力を取らず展開検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検分の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して展開検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Problem 機能 は「展開検分のユーザーズガイド 操作に関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Problem 機能の属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Problem 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Problem Diagnostics {#c32-i3587}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Problem Diagnosticsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.235) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.235)

??? question "確認問題（1問）"
    **問題.** 呼出検分のユーザーズガイド 操作でネットビューの運用確認を行います。Problem 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検分のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、呼出検分の点検結果を残す。 ✅
    - D. Problem 機能の属性行を読まず呼出検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では Problem 機能 は「IBM Z NetViewで Problem 機能の扱いを記録する呼出検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では Problem 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では Problem 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Problem Management {#c32-i3588}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Problem Managementは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 置換検分のユーザーズガイド 操作に関する Problem Managementの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Problem Managementの変更点を出力本文から切り離して置換検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では Problem Management は「Problem Managementの状態と出力メッセージを結び付ける置換検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では Problem Managementの出力行と DSI633I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では Problem Managementを IBM Z NetViewの確認記録に残し、対象名は置換検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Processing Generic Failures (EZLEFAIL) {#c32-i3589}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Processing Generic Failures (EZLEFAIL)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.322) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.322)

??? question "確認問題（1問）"
    **問題.** 終端検分のユーザーズガイド 操作に関係する Processing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端検分の確認値として扱う。 ✅
    - B. Processing 機能の名称と担当者名のみを残して終端検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Processing 機能 は「Processing 機能の用途をネットビューの表示で確認する終端検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では IBM Z NetViewの Processing 機能と DSI633I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Processing 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Programmatic Interface for IP Trace {#c32-i3590}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Programmatic Interface for IP Traceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 探索検分のユーザーズガイド 操作で Programmatic 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Programmatic 機能の出力を取らず探索検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索検分の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して探索検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Programmatic 機能 は「探索検分のユーザーズガイド 操作に関係する定義値と表示行を照合する探索検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Programmatic 機能の属性行と DSI633I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Programmatic 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検分初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Programs That Interact with the IBM Z NetView Program {#c32-i3591}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Programs That Interact with the IBM Z NetView Programは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書検分のユーザーズガイド 操作でネットビューの運用確認を行います。Programs 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検分のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を上書検分で確認する。 ✅
    - D. Programs 機能の属性行を読まず上書検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では Programs 機能 は「IBM Z NetViewで Programs 機能の扱いを記録する上書検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では Programs 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では Programs 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Querying Command Availability (EXIST) {#c32-i3592}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Querying Command Availability (EXIST)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.307) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.307)

??? question "確認問題（1問）"
    **問題.** 出力検分のユーザーズガイド 操作に関する Querying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Querying 機能の変更点を出力本文から切り離して出力検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、出力検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では Querying 機能 は「Querying 機能の状態と出力メッセージを結び付ける出力検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では Querying 機能の出力行と DSI633I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では Querying 機能を IBM Z NetViewの確認記録に残し、対象名は出力検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Querying status descriptors (DDFQRY) {#c32-i3593}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Querying status descriptors (DDFQRY)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.282) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.282)

??? question "確認問題（1問）"
    **問題.** 条件検分のユーザーズガイド 操作に関係する Querying 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件検分の確認記録にまとめる。 ✅
    - B. Querying 機能の名称と担当者名のみを残して条件検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Querying 機能 は「Querying 機能の用途をネットビューの表示で確認する条件検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では IBM Z NetViewの Querying 機能と DSI633I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Querying 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### RODM-Based Views {#c32-i3594}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

RODM-Based Viewsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide NetView Management Console (p.83) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Management Console (p.83)

??? question "確認問題（1問）"
    **問題.** 置換確認のユーザーズガイド 操作に関する RODM-Based Viewsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RODMVIEW の結果を残さず置換確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. RODM-Based Viewsの変更点を出力本文から切り離して置換確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では RODM-Based Views は「RODM-Based Viewsの状態と出力メッセージを結び付ける置換確認項目」と RODMVIEW または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では RODM-Based Viewsの出力行と EKG000I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では RODM-Based Viewsを IBM Z NetViewの確認記録に残し、対象名は置換確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Reactive Investigating {#c32-i3595}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Reactive Investigatingは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.245) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.245)

??? question "確認問題（1問）"
    **問題.** 区切検分のユーザーズガイド 操作で Reactive 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Reactive 機能の出力を取らず区切検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検分の根拠にする。 ✅
    - C. BROWSE CANZLOG を省略して区切検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Reactive 機能 は「区切検分のユーザーズガイド 操作に関係する定義値と表示行を照合する区切検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Reactive 機能の属性行と DSI633I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Reactive 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Record Types {#c32-i3596}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Record Typesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.112) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.112)

??? question "確認問題（1問）"
    **問題.** 範囲検分のユーザーズガイド 操作でネットビューの運用確認を行います。Record Typesの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検分のユーザーズガイド 操作を正常終了として記録する。
    - C. 同じ画面で対象行と DSI633I を読み、範囲検分の結果として保存する。 ✅
    - D. Record Typesの属性行を読まず範囲検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Record Types は「IBM Z NetViewで Record Typesの扱いを記録する範囲検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Record Typesの表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Record Typesの使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Recovering Generic Resources (EZLEAGEN) {#c32-i3597}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Recovering Generic Resources (EZLEAGEN)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 優先検分のユーザーズガイド 操作に関する Recovering 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Recovering 機能の変更点を出力本文から切り離して優先検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG で得た表示本文を使い、優先検分の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Recovering 機能 は「Recovering 機能の状態と出力メッセージを結び付ける優先検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Recovering 機能の出力行と DSI633I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Recovering 機能を IBM Z NetViewの確認記録に残し、対象名は優先検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Recovering Resources (EZLERECV) {#c32-i3598}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Recovering Resources (EZLERECV)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 記録検分のユーザーズガイド 操作に関係する Recovering 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録検分として引き継ぐ。 ✅
    - B. Recovering 機能の名称と担当者名のみを残して記録検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Recovering 機能 は「Recovering 機能の用途をネットビューの表示で確認する記録検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では IBM Z NetViewの Recovering 機能と DSI633I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Recovering 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Reinitializing automation {#c32-i3599}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Reinitializing automationは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.89) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.89)

??? question "確認問題（1問）"
    **問題.** 比較検分のユーザーズガイド 操作で Reinitializing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Reinitializing 機能の出力を取らず比較検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較検分の確認にする。 ✅
    - C. BROWSE CANZLOG を省略して比較検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Reinitializing 機能 は「比較検分のユーザーズガイド 操作に関係する定義値と表示行を照合する比較検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Reinitializing 機能の属性行と DSI633I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Reinitializing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Reissuing notifications {#c32-i3600}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Reissuing notificationsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.99) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.99)

??? question "確認問題（1問）"
    **問題.** 順序検分のユーザーズガイド 操作でネットビューの運用確認を行います。Reissuing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検分のユーザーズガイド 操作を正常終了として記録する。
    - C. IBM Z NetViewの表示形式に沿って根拠行を採り、順序検分の点検結果を残す。 ✅
    - D. Reissuing 機能の属性行を読まず順序検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Reissuing 機能 は「IBM Z NetViewで Reissuing 機能の扱いを記録する順序検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Reissuing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Reissuing 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Removing an operator assignment in DDF (UNMARK) {#c32-i3601}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Removing an operator assignment in DDF (UNMARK)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域検分のユーザーズガイド 操作に関する Removing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Removing 機能の変更点を出力本文から切り離して値域検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Removing 機能 は「Removing 機能の状態と出力メッセージを結び付ける値域検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Removing 機能の出力行と DSI633I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Removing 機能を IBM Z NetViewの確認記録に残し、対象名は値域検分対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Renaming Navigation Views {#c32-i3602}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Renaming Navigation Viewsは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告検分のユーザーズガイド 操作に関係する Renaming 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告検分の確認値として扱う。 ✅
    - B. Renaming 機能の名称と担当者名のみを残して警告検分のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検分のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検分のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Renaming 機能 は「Renaming 機能の用途をネットビューの表示で確認する警告検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では IBM Z NetViewの Renaming 機能と DSI633I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Renaming 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Replication Servers Attributes {#c32-i3603}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Replication Servers Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.153) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.153)

??? question "確認問題（1問）"
    **問題.** 復旧検分のユーザーズガイド 操作で Replication 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Replication 機能の出力を取らず復旧検分のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧検分の根拠を固定する。 ✅
    - C. BROWSE CANZLOG を省略して復旧検分のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Replication 機能 は「復旧検分のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Replication 機能の属性行と DSI633I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Replication 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Replication Servers Workspace {#c32-i3604}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Replication Servers Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.85) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.85)

??? question "確認問題（1問）"
    **問題.** 監査検分のユーザーズガイド 操作でネットビューの運用確認を行います。Replication 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検分のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検分のユーザーズガイド 操作を正常終了として記録する。
    - C. DSI633I を含む表示を保存し、説明欄との差分を監査検分で確認する。 ✅
    - D. Replication 機能の属性行を読まず監査検分のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Replication 機能 は「IBM Z NetViewで Replication 機能の扱いを記録する監査検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Replication 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Replication 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Replication Workloads Attributes {#c32-i3605}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Replication Workloads Attributesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.156) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.156)

??? question "確認問題（1問）"
    **問題.** 変更検分のユーザーズガイド 操作に関する Replication 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検分のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Replication 機能の変更点を出力本文から切り離して変更検分のユーザーズガイド 操作の承認欄のみ残す。
    - D. BROWSE CANZLOG の結果から対象行を抜き出し、変更検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Replication 機能 は「Replication 機能の状態と出力メッセージを結び付ける変更検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Replication 機能の出力行と DSI633I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Replication 機能を IBM Z NetViewの確認記録に残し、対象名は変更検分対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Replication Workloads Workspace {#c32-i3606}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Replication Workloads Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.86) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.86)

??? question "確認問題（1問）"
    **問題.** 構文確認のユーザーズガイド 操作に関係する Replication 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文確認の確認にする。 ✅
    - B. Replication 機能の名称と担当者名のみを残して構文確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Replication 機能 は「Replication 機能の用途をネットビューの表示で確認する構文確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Z NetViewの Replication 機能と DSI633I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Replication 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Retrieving AON Information (EZLERTVE) {#c32-i3607}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Retrieving AON Information (EZLERTVE)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.338) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.338)

??? question "確認問題（1問）"
    **問題.** 呼出確認のユーザーズガイド 操作でネットビューの運用確認を行います。Retrieving 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出確認のユーザーズガイド 操作を確認した扱いにする。
    - B. EZL000I の有無を確認せず呼出確認のユーザーズガイド 操作を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出確認で再確認できる形にする。 ✅
    - D. Retrieving 機能の属性行を読まず呼出確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Retrieving 機能 は「IBM Z NetViewで Retrieving 機能の扱いを記録する呼出確認項目」と AONSTAT または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Retrieving 機能の表示結果と EZL000I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Retrieving 機能の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Routing Commands To Other NetView Domains (EZLERGWY) {#c32-i3608}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Routing Commands To Other NetView Domains (EZLERGWY)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 上書確認のユーザーズガイド 操作でネットビューの運用確認を行います。Routing 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書確認のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず上書確認のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、上書確認の証跡として残す。 ✅
    - D. Routing 機能の属性行を読まず上書確認のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Routing 機能 は「IBM Z NetViewで Routing 機能の扱いを記録する上書確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Routing 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Routing 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Routing Commands over Cross-Domain Sessions (EZLERCMD) {#c32-i3609}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Routing Commands over Cross-Domain Sessions (EZLERCMD)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.333) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.333)

??? question "確認問題（1問）"
    **問題.** 探索確認のユーザーズガイド 操作で Routing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Routing 機能の出力を取らず探索確認のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を探索確認で確認する。 ✅
    - C. BROWSE CANZLOG を省略して探索確認のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Routing 機能 は「探索確認のユーザーズガイド 操作に関係する定義値と表示行を照合する探索確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Routing 機能の属性行と DSI633I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Routing 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Routing NNT Cross-Domain Logon Information (EZLEROUT) {#c32-i3610}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

Routing NNT Cross-Domain Logon Information (EZLEROUT)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.337) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.337)

??? question "確認問題（1問）"
    **問題.** 出力確認のユーザーズガイド 操作に関する Routing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力確認のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. Routing 機能の変更点を出力本文から切り離して出力確認のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力確認の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では Routing 機能 は「Routing 機能の状態と出力メッセージを結び付ける出力確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では Routing 機能の出力行と DSI633I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では Routing 機能を IBM Z NetViewの確認記録に残し、対象名は出力確認対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Running Entry and Exit Traces (EZLTRACE) {#c32-i3611}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Running Entry and Exit Traces (EZLTRACE)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件確認のユーザーズガイド 操作に関係する Running 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件確認の根拠にする。 ✅
    - B. Running 機能の名称と担当者名のみを残して条件確認のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件確認のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件確認のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では Running 機能 は「Running 機能の用途をネットビューの表示で確認する条件確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Z NetViewの Running 機能と DSI633I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では Running 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### Running IP Traces {#c32-i3612}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

Running IP Tracesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


### SNA Advanced Peer-to-Peer Networking Session through Adjacent Composite Nodes {#c32-i3613}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Advanced Peer-to-Peer Networking Session through Adjacent Composite Nodesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.278) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.278)

??? question "確認問題（1問）"
    **問題.** 復旧照合のユーザーズガイド 操作で SNA 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SNA 機能の出力を取らず復旧照合のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. IBM Z NetViewの表示形式に沿って根拠行を採り、復旧照合の点検結果を残す。 ✅
    - C. BROWSE CANZLOG を省略して復旧照合のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では SNA 機能 は「復旧照合のユーザーズガイド 操作に関係する定義値と表示行を照合する復旧照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では SNA 機能の属性行と DSI633I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では SNA 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SNA Advanced Peer-to-Peer Networking Session through Non-Adjacent Composite Nodes {#c32-i3614}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Advanced Peer-to-Peer Networking Session through Non-Adjacent Composite Nodesは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.277) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.277)


### SNA Advanced Peer-to-Peer Networking Session through a Composite Node {#c32-i3615}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Advanced Peer-to-Peer Networking Session through a Composite Nodeは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域照合のユーザーズガイド 操作に関する SNA 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. SNA 機能の変更点を出力本文から切り離して値域照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域照合として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では SNA 機能 は「SNA 機能の状態と出力メッセージを結び付ける値域照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では SNA 機能の出力行と DSI633I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では SNA 機能を IBM Z NetViewの確認記録に残し、対象名は値域照合対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SNA Advanced Peer-to-Peer Networking Session through a SNI Gateway {#c32-i3616}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Advanced Peer-to-Peer Networking Session through a SNI Gatewayは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 警告照合のユーザーズガイド 操作に関係する SNA 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告照合の確認にする。 ✅
    - B. SNA 機能の名称と担当者名のみを残して警告照合のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告照合のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告照合のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では SNA 機能 は「SNA 機能の用途をネットビューの表示で確認する警告照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では IBM Z NetViewの SNA 機能と DSI633I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では SNA 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SNA Resource Automation (FKVESYNC) {#c32-i3617}
*分類: ユーザーズガイド (操作)*  ・  難易度: 上級

SNA Resource Automation (FKVESYNC)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.354) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.354)

??? question "確認問題（1問）"
    **問題.** 変更照合のユーザーズガイド 操作に関する SNA 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更照合のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. SNA 機能の変更点を出力本文から切り離して変更照合のユーザーズガイド 操作の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では SNA 機能 は「SNA 機能の状態と出力メッセージを結び付ける変更照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では SNA 機能の出力行と DSI633I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では SNA 機能を IBM Z NetViewの確認記録に残し、対象名は変更照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SNA Session {#c32-i3618}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Sessionは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.275) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.275)

??? question "確認問題（1問）"
    **問題.** 構文追跡のユーザーズガイド 操作に関係する SNA Sessionの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文追跡の根拠を固定する。 ✅
    - B. SNA Sessionの名称と担当者名のみを残して構文追跡のユーザーズガイド 操作の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文追跡のユーザーズガイド 操作を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文追跡のユーザーズガイド 操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では SNA Session は「SNA Sessionの用途をネットビューの表示で確認する構文追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では IBM Z NetViewの SNA Sessionと DSI633I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では SNA Sessionを Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SNA Session through an Advanced Peer-to-Peer Networking Network {#c32-i3619}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Session through an Advanced Peer-to-Peer Networking Networkは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 展開追跡のユーザーズガイド 操作で SNA 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SNA 機能の出力を取らず展開追跡のユーザーズガイド 操作の説明文と承認印のみを残す。
    - B. DSI633I を含む表示を保存し、説明欄との差分を展開追跡で確認する。 ✅
    - C. BROWSE CANZLOG を省略して展開追跡のユーザーズガイド 操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のユーザーズガイド 操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では SNA 機能 は「展開追跡のユーザーズガイド 操作に関係する定義値と表示行を照合する展開追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では SNA 機能の属性行と DSI633I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では SNA 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### SNA Workload Server Details Workspace {#c32-i3620}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNA Workload Server Details Workspaceは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.87) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView Enterprise Management Agent (p.87)

??? question "確認問題（1問）"
    **問題.** 呼出追跡のユーザーズガイド 操作でネットビューの運用確認を行います。SNA 機能の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出追跡のユーザーズガイド 操作を確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出追跡のユーザーズガイド 操作を正常終了として記録する。
    - C. BROWSE CANZLOG の結果から対象行を抜き出し、呼出追跡の証跡として残す。 ✅
    - D. SNA 機能の属性行を読まず呼出追跡のユーザーズガイド 操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では SNA 機能 は「IBM Z NetViewで SNA 機能の扱いを記録する呼出追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では SNA 機能の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では SNA 機能の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SNMP RFC Conversion (FKXECNVT) {#c32-i3621}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SNMP RFC Conversion (FKXECNVT)は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide Automated Operations Network (p.348) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide Automated Operations Network (p.348)

??? question "確認問題（1問）"
    **問題.** 置換追跡のユーザーズガイド 操作に関する SNMP 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換追跡のユーザーズガイド 操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のユーザーズガイド 操作の証跡として保存して根拠にする。
    - C. SNMP 機能の変更点を出力本文から切り離して置換追跡のユーザーズガイド 操作の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では SNMP 機能 は「SNMP 機能の状態と出力メッセージを結び付ける置換追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では SNMP 機能の出力行と DSI633I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では SNMP 機能を IBM Z NetViewの確認記録に残し、対象名は置換追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SSCP Takeover⁄Giveback Scenarios {#c32-i3622}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SSCP Takeover⁄Giveback Scenariosは、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Users Guide NetView (p.283) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Users Guide NetView (p.283)

??? question "確認問題（1問）"
    **問題.** 記録追跡の⁄に関係する SSCP 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録追跡の根拠を固定する。 ✅
    - B. SSCP 機能の名称と担当者名のみを残して記録追跡の⁄の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録追跡の⁄を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録追跡の⁄の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では SSCP 機能 は「SSCP 機能の用途をネットビューの表示で確認する記録追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では IBM Z NetViewの SSCP 機能と DSI633I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では SSCP 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 1 {#c32-i3623}
*分類: ユーザーズガイド (操作)*  ・  難易度: 中級

SSCP Takeover⁄Giveback of NCP BF Connection - Scenario 1は、Tivoli NetView z/OS 自動化のユーザーズガイド (操作)で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 条件追跡の⁄に関係する SSCP 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件追跡の確認にする。 ✅
    - B. SSCP 機能の名称と担当者名のみを残して条件追跡の⁄の表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件追跡の⁄を確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件追跡の⁄の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では SSCP 機能 は「SSCP 機能の用途をネットビューの表示で確認する条件追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では IBM Z NetViewの SSCP 機能と DSI633I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では SSCP 機能を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference


