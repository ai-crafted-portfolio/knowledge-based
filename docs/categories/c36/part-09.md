---
search:
  exclude: true
---

# Z System Automation (TSA) — 詳細 (9/12)

[← Z System Automation (TSA) の概要へ戻る](index.md)


## Z System Automation (TSA) > 概要 / 開始

### Start SA z/OS for the first time {#c36-i1162}
*分類: 概要 / 開始*  ・  難易度: 上級

Start SA z/OS for the first timeは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（2問）"
    **問題.** 記録記録のStart SA z/OS for the first timeに関係する Start SA z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録記録として引き継ぐ。 ✅
    - B. Start SA z 属性の名称と担当者名のみを残して記録記録のStart SA z/OS for the first timeの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録記録のStart SA z/OS for the first timeを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録記録のStart SA z/OS for the first timeの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Start SA z 属性 は「Start SA z 属性の用途を自動化管理の表示で確認する記録記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では SA z/OS の Start SA z 属性と INGKYST0I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Start SA z 属性を Z System Automation (TSA)で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 監査整理のStart SA z/OS for the first timeで自動化管理の運用確認を行います。Start SA z 属性の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査整理のStart SA z/OS for the first timeを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査整理のStart SA z/OS for the first timeを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査整理として引き継ぐ。 ✅
    - D. Start SA z 属性の属性行を読まず監査整理のStart SA z/OS for the first timeの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Start SA z 属性 は「SA z/OS で Start SA z 属性の扱いを記録する監査整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Start SA z 属性の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Start SA z 属性の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting SA z/OS and verifying your installation {#c36-i1163}
*分類: 概要 / 開始*  ・  難易度: 上級

Starting SA z/OS and verifying your installationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として Starting SA z/OS and verifyi を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 展開照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。展開照合権限で扱う Starting SA z/OS and verifyi は Z System Automation (TSA) の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として Starting SA z/OS and verifyi を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting and stopping resources {#c36-i1164}
*分類: 概要 / 開始*  ・  難易度: 上級

Starting and stopping resourcesは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較記録の概要 開始で Starting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Starting 機能の出力を取らず比較記録の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較記録の確認にする。 ✅
    - C. INGLIST を省略して比較記録の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Starting 機能 は「比較記録の概要 開始に関係する定義値と表示行を照合する比較記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Starting 機能の属性行と INGKYST0I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Starting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較記録初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting the Automation Agent {#c36-i1165}
*分類: 概要 / 開始*  ・  難易度: 上級

Starting the Automation Agentは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域記録の概要 開始に関する Starting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域記録の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録の概要 開始の証跡として保存して根拠にする。
    - C. Starting 機能の変更点を出力本文から切り離して値域記録の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域記録で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では Starting 機能 は「Starting 機能の状態と出力メッセージを結び付ける値域記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では Starting 機能の出力行と INGKYST0I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では Starting 機能を SA z/OS の確認記録に残し、対象名は値域記録対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting the Automation Manager {#c36-i1166}
*分類: 概要 / 開始*  ・  難易度: 上級

Starting the Automation Managerは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告記録の概要 開始に関係する Starting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告記録の確認値として扱う。 ✅
    - B. Starting 機能の名称と担当者名のみを残して警告記録の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告記録の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告記録の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Starting 機能 は「Starting 機能の用途を自動化管理の表示で確認する警告記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では SA z/OS の Starting 機能と INGKYST0I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Starting 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting the Customization Dialog {#c36-i1167}
*分類: 概要 / 開始*  ・  難易度: 上級

Starting the Customization Dialogは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧記録の概要 開始で Starting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Starting 機能の出力を取らず復旧記録の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧記録の根拠を固定する。 ✅
    - C. INGLIST を省略して復旧記録の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Starting 機能 は「復旧記録の概要 開始に関係する定義値と表示行を照合する復旧記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Starting 機能の属性行と INGKYST0I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Starting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting the Subsystem Interface Task {#c36-i1168}
*分類: 概要 / 開始*  ・  難易度: 上級

Starting the Subsystem Interface Taskは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査記録の概要 開始で自動化管理の運用確認を行います。Starting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査記録の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査記録の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を監査記録で確認する。 ✅
    - D. Starting 機能の属性行を読まず監査記録の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Starting 機能 は「SA z/OS で Starting 機能の扱いを記録する監査記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Starting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Starting 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Support {#c36-i1169}
*分類: 概要 / 開始*  ・  難易度: 上級

Supportは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 変更記録の概要 開始に関する Supportの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更記録の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録の概要 開始の証跡として保存して根拠にする。
    - C. Supportの変更点を出力本文から切り離して変更記録の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、変更記録の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Support は「Supportの状態と出力メッセージを結び付ける変更記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Supportの出力行と INGKYST0I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Supportを SA z/OS の確認記録に残し、対象名は変更記録対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Testing your automation policy {#c36-i1170}
*分類: 概要 / 開始*  ・  難易度: 上級

Testing your automation policyは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 構文分離の概要 開始に関係する Testing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文分離の確認記録にまとめる。 ✅
    - B. Testing 機能の名称と担当者名のみを残して構文分離の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文分離の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文分離の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Testing 機能 は「Testing 機能の用途を自動化管理の表示で確認する構文分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では SA z/OS の Testing 機能と INGKYST0I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Testing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### The Automation Agent’s started task {#c36-i1171}
*分類: 概要 / 開始*  ・  難易度: 上級

The Automation Agent’s started taskは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開分離の’で The 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. The 機能の出力を取らず展開分離の’の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開分離の根拠にする。 ✅
    - C. INGLIST を省略して展開分離の’の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離の’へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では The 機能 は「展開分離の’に関係する定義値と表示行を照合する展開分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では The 機能の属性行と INGKYST0I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では The 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開分離初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### The Automation Manager’s started task {#c36-i1172}
*分類: 概要 / 開始*  ・  難易度: 上級

The Automation Manager’s started taskは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出分離の’で自動化管理の運用確認を行います。The 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出分離の’を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出分離の’を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、呼出分離の結果として保存する。 ✅
    - D. The 機能の属性行を読まず呼出分離の’の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では The 機能 は「SA z/OS で The 機能の扱いを記録する呼出分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では The 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では The 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Training your operators {#c36-i1173}
*分類: 概要 / 開始*  ・  難易度: 上級

Training your operatorsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 置換分離の概要 開始に関する Training 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換分離の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の概要 開始の証跡として保存して根拠にする。
    - C. Training 機能の変更点を出力本文から切り離して置換分離の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、置換分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Training 機能 は「Training 機能の状態と出力メッセージを結び付ける置換分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Training 機能の出力行と INGKYST0I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Training 機能を SA z/OS の確認記録に残し、対象名は置換分離対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Usage and Operation {#c36-i1174}
*分類: 概要 / 開始*  ・  難易度: 上級

Usage and Operationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端分離の概要 開始に関係する Usage 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端分離として引き継ぐ。 ✅
    - B. Usage 機能の名称と担当者名のみを残して終端分離の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端分離の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端分離の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では Usage 機能 は「Usage 機能の用途を自動化管理の表示で確認する終端分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では SA z/OS の Usage 機能と INGKYST0I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では Usage 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Verification {#c36-i1175}
*分類: 概要 / 開始*  ・  難易度: 上級

Verificationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 探索分離の概要 開始で Verificationの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Verificationの出力を取らず探索分離の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索分離の確認にする。 ✅
    - C. INGLIST を省略して探索分離の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では Verification は「探索分離の概要 開始に関係する定義値と表示行を照合する探索分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では Verificationの属性行と INGKYST0I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では Verificationを Z System Automation (TSA)の運用手順で確認し、初出名は探索分離初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### What is in a policy database? {#c36-i1176}
*分類: 概要 / 開始*  ・  難易度: 上級

What is in a policy database?は、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書分離の概要 開始で自動化管理の運用確認を行います。What 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書分離の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書分離の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、上書分離の点検結果を残す。 ✅
    - D. What 機能の属性行を読まず上書分離の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では What 機能 は「SA z/OS で What 機能の扱いを記録する上書分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では What 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では What 機能の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Working with data logs and databases {#c36-i1177}
*分類: 概要 / 開始*  ・  難易度: 上級

Working with data logs and databasesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力分離の概要 開始に関する Working 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力分離の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離の概要 開始の証跡として保存して根拠にする。
    - C. Working 機能の変更点を出力本文から切り離して出力分離の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では Working 機能 は「Working 機能の状態と出力メッセージを結び付ける出力分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では Working 機能の出力行と INGKYST0I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では Working 機能を SA z/OS の確認記録に残し、対象名は出力分離対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 概要 / 開始 > automation agent

### automation agent {#c36-i1178}
*分類: 概要 / 開始 > automation agent*  ・  難易度: 中級

automation agentは、各システムで資源を実際に起動や停止し、状態を自動化マネージャーへ報告する実行側です。DISPINFOでその視点を確認できます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更検分の自動化管理に関するautomation agentの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更検分の自動化管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分の自動化管理の証跡として保存して根拠にする。
    - C. automation agentの変更点を出力本文から切り離して変更検分の自動化管理の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更検分の根拠にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠ではautomation agent は「automation agentの状態と出力メッセージを結び付ける変更検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存ではautomation agentの出力行と INGKYST0I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象ではautomation agentを SA z/OS の確認記録に残し、対象名は変更検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 概要 / 開始 > automation manager

### automation manager {#c36-i1179}
*分類: 概要 / 開始 > automation manager*  ・  難易度: 中級

automation managerは、資源の目標状態を管理し、観測状態とのずれに応じて起動や停止の判断を下す中枢です。要求や票を受けて動作を決めます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査検分の自動化管理で自動化管理の運用確認を行います。automation managerの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査検分の自動化管理を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査検分の自動化管理を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査検分の確認記録にまとめる。 ✅
    - D. automation managerの属性行を読まず監査検分の自動化管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠ではautomation manager は「SA z/OS でautomation managerの扱いを記録する監査検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡ではautomation managerの表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料ではautomation managerの使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 状態照会 > DISPINFO

### DISPINFO {#c36-i1180}
*分類: 状態照会 > DISPINFO*  ・  難易度: 中級

DISPINFOは、自動化エージェントから見た資源の現在の詳細を表示する対話です。INGINFOのパネルからPF4で切り替わります

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 状態照会 > INGINFO

### INGINFO {#c36-i1181}
*分類: 状態照会 > INGINFO*  ・  難易度: 中級

INGINFOは、個々の資源やアプリケーション・グループの多くの詳細を表示するコマンドです。パネルでPF4を押すとDISPINFOへ切り替わります

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 状態照会 > INGLIST

### INGLIST {#c36-i1182}
*分類: 状態照会 > INGLIST*  ・  難易度: 初級

INGLISTは、一つ以上の資源について観測状態や目標状態、自動化フラグ、掛かっている票をまとめて表示するコマンドです。監視の入り口として使います

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 状態照会 > INGVOTE

### INGVOTE {#c36-i1183}
*分類: 状態照会 > INGVOTE*  ・  難易度: 中級

INGVOTEは、指定した資源に対して現在保留中の要求と票を表示するコマンドです。票の優先度から目標状態を決める要求を読み取ります

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 状態監視 > INGSTOBS

### INGSTOBS {#c36-i1184}
*分類: 状態監視 > INGSTOBS*  ・  難易度: 上級

INGSTOBSは、一つ以上の資源の状態オブザーバーとして登録するコマンドです。状態が変わるたびに自動化マネージャーから通知が届きます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 監視 > Detail Status Display

### Detail Status Display {#c36-i1185}
*分類: 監視 > Detail Status Display*  ・  難易度: 中級

Detail Status Displayは、SDFで色が変わった資源にカーソルを合わせてPF2を押すと開く詳細の状態表示パネルです。原因の資源を確かめます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧検分の自動化管理で Detail 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Detail 機能の出力を取らず復旧検分の自動化管理の説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、復旧検分の証跡として残す。 ✅
    - C. INGLIST を省略して復旧検分の自動化管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分の自動化管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Detail 機能 は「復旧検分の自動化管理に関係する定義値と表示行を照合する復旧検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Detail 機能の属性行と INGKYST0I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Detail 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 監視 > SDF

### SDF {#c36-i1186}
*分類: 監視 > SDF*  ・  難易度: 初級

SDFは、自動化されたシステムや資源の状態を割り当てた色で表示する状態表示機能です。緑は起動を、赤は停止や問題を表します

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 自動化ポリシー定義

### A Grouping Scenario {#c36-i1187}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

A Grouping Scenarioは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.63) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 条件分離の自動化ポリシー定義に関係する A 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件分離の確認値として扱う。 ✅
    - B. A 機能の名称と担当者名のみを残して条件分離の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件分離の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件分離の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では A 機能 は「A 機能の用途を自動化管理の表示で確認する条件分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では SA z/OS の A 機能と INGKYST0I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では A 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.63) / OS 自動化ポリシー定義



### A Possible Solution {#c36-i1188}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

A Possible Solutionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 区切分離の自動化ポリシー定義で A 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. A 機能の出力を取らず区切分離の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切分離の根拠を固定する。 ✅
    - C. INGLIST を省略して区切分離の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では A 機能 は「区切分離の自動化ポリシー定義に関係する定義値と表示行を照合する区切分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では A 機能の属性行と INGKYST0I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では A 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切分離初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義



### APPLGROUP INFO Policy Item {#c36-i1189}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

APPLGROUP INFO Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.137) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 優先分離の自動化ポリシー定義に関する APPLGROUP 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先分離の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. APPLGROUP 機能の変更点を出力本文から切り離して優先分離の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、優先分離の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では APPLGROUP 機能 は「APPLGROUP 機能の状態と出力メッセージを結び付ける優先分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では APPLGROUP 機能の出力行と INGKYST0I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では APPLGROUP 機能を SA z/OS の確認記録に残し、対象名は優先分離対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.137) / OS 自動化ポリシー定義



### APPLICATION INFO Policy Item {#c36-i1190}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

APPLICATION INFO Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 順序分離の自動化ポリシー定義で自動化管理の運用確認を行います。APPLICATION 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序分離の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序分離の自動化ポリシー定義を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、順序分離の結果として保存する。 ✅
    - D. APPLICATION 機能の属性行を読まず順序分離の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では APPLICATION 機能 は「SA z/OS で APPLICATION 機能の扱いを記録する順序分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では APPLICATION 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では APPLICATION 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### APPLICATION SYMBOLS Policy Item {#c36-i1191}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

APPLICATION SYMBOLS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.186) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 値域分離の自動化ポリシー定義に関する APPLICATION 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域分離の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. APPLICATION 機能の変更点を出力本文から切り離して値域分離の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、値域分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では APPLICATION 機能 は「APPLICATION 機能の状態と出力メッセージを結び付ける値域分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では APPLICATION 機能の出力行と INGKYST0I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では APPLICATION 機能を SA z/OS の確認記録に残し、対象名は値域分離対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.186) / OS 自動化ポリシー定義



### APPLICATIONS Policy Item {#c36-i1192}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

APPLICATIONS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.148) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 復旧分離の自動化ポリシー定義で APPLICATIONS 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. APPLICATIONS 機能の出力を取らず復旧分離の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧分離の確認にする。 ✅
    - C. INGLIST を省略して復旧分離の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では APPLICATIONS 機能 は「復旧分離の自動化ポリシー定義に関係する定義値と表示行を照合する復旧分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では APPLICATIONS 機能の属性行と INGKYST0I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では APPLICATIONS 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.148) / OS 自動化ポリシー定義



### AT/MRT INSERTS Policy Item {#c36-i1193}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

AT/MRT INSERTS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 変更分離のAT/MRT INSERTS Policy Itemに関する AT 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更分離のAT/MRT INSERTS Policy Itemの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離のAT/MRT INSERTS Policy Itemの証跡として保存して根拠にする。
    - C. AT 属性の変更点を出力本文から切り離して変更分離のAT/MRT INSERTS Policy Itemの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では AT 属性 は「AT 属性の状態と出力メッセージを結び付ける変更分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では AT 属性の出力行と INGKYST0I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では AT 属性を SA z/OS の確認記録に残し、対象名は変更分離対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### ATTEND TIME Policy Item {#c36-i1194}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

ATTEND TIME Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.275) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 構文読解の自動化ポリシー定義に関係する ATTEND 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文読解の確認値として扱う。 ✅
    - B. ATTEND 機能の名称と担当者名のみを残して構文読解の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文読解の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文読解の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では ATTEND 機能 は「ATTEND 機能の用途を自動化管理の表示で確認する構文読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では SA z/OS の ATTEND 機能と INGKYST0I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では ATTEND 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.275) / OS 自動化ポリシー定義



### AUTHENTICATION Policy Item {#c36-i1195}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

AUTHENTICATION Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 展開読解の自動化ポリシー定義で AUTHENTICATION 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AUTHENTICATION 機能の出力を取らず展開読解の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開読解の根拠を固定する。 ✅
    - C. INGLIST を省略して展開読解の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では AUTHENTICATION 機能 は「展開読解の自動化ポリシー定義に関係する定義値と表示行を照合する展開読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では AUTHENTICATION 機能の属性行と INGKYST0I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では AUTHENTICATION 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開読解初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### AUTOMATION CONSOLE Policy Item {#c36-i1196}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

AUTOMATION CONSOLE Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 呼出読解の自動化ポリシー定義で自動化管理の運用確認を行います。AUTOMATION 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出読解の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出読解の自動化ポリシー定義を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を呼出読解で確認する。 ✅
    - D. AUTOMATION 機能の属性行を読まず呼出読解の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では AUTOMATION 機能 は「SA z/OS で AUTOMATION 機能の扱いを記録する呼出読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では AUTOMATION 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では AUTOMATION 機能の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### AUTOMATION FLAGS Policy Item {#c36-i1197}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

AUTOMATION FLAGS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.186) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 置換読解の自動化ポリシー定義に関する AUTOMATION 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換読解の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. AUTOMATION 機能の変更点を出力本文から切り離して置換読解の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、置換読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では AUTOMATION 機能 は「AUTOMATION 機能の状態と出力メッセージを結び付ける置換読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では AUTOMATION 機能の出力行と INGKYST0I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では AUTOMATION 機能を SA z/OS の確認記録に残し、対象名は置換読解対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.186) / OS 自動化ポリシー定義



### AUTOMATION OPTIONS Policy Item {#c36-i1198}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

AUTOMATION OPTIONS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 探索読解の自動化ポリシー定義で AUTOMATION 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AUTOMATION 機能の出力を取らず探索読解の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索読解の根拠にする。 ✅
    - C. INGLIST を省略して探索読解の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では AUTOMATION 機能 は「探索読解の自動化ポリシー定義に関係する定義値と表示行を照合する探索読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では AUTOMATION 機能の属性行と INGKYST0I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では AUTOMATION 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索読解初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### AUTOMATION SYMBOLS Policy Item {#c36-i1199}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

AUTOMATION SYMBOLS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 上書読解の自動化ポリシー定義で自動化管理の運用確認を行います。AUTOMATION 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書読解の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書読解の自動化ポリシー定義を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、上書読解の結果として保存する。 ✅
    - D. AUTOMATION 機能の属性行を読まず上書読解の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では AUTOMATION 機能 は「SA z/OS で AUTOMATION 機能の扱いを記録する上書読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では AUTOMATION 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では AUTOMATION 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### Alternate and Tertiary Configuration Support {#c36-i1200}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Alternate and Tertiary Configuration Supportは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲分離の自動化ポリシー定義で自動化管理の運用確認を行います。Alternate 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲分離の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲分離の自動化ポリシー定義を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を範囲分離で確認する。 ✅
    - D. Alternate 機能の属性行を読まず範囲分離の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では Alternate 機能 は「SA z/OS で Alternate 機能の扱いを記録する範囲分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では Alternate 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では Alternate 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Application Defaults Entry Type {#c36-i1201}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Application Defaults Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.249) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 記録分離の自動化ポリシー定義に関係する Application 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録分離の確認記録にまとめる。 ✅
    - B. Application 機能の名称と担当者名のみを残して記録分離の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録分離の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録分離の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では Application 機能 は「Application 機能の用途を自動化管理の表示で確認する記録分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では SA z/OS の Application 機能と INGKYST0I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では Application 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.249) / OS 自動化ポリシー定義



### Application Entry Type {#c36-i1202}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Application Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.164) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 比較分離の自動化ポリシー定義で Application 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Application 機能の出力を取らず比較分離の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較分離の根拠にする。 ✅
    - C. INGLIST を省略して比較分離の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では Application 機能 は「比較分離の自動化ポリシー定義に関係する定義値と表示行を照合する比較分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では Application 機能の属性行と INGKYST0I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では Application 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較分離初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.164) / OS 自動化ポリシー定義



### ApplicationGroup Entry Type {#c36-i1203}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

ApplicationGroup Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.137) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 警告分離の自動化ポリシー定義に関係する ApplicationGroup 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告分離として引き継ぐ。 ✅
    - B. ApplicationGroup 機能の名称と担当者名のみを残して警告分離の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告分離の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告分離の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では ApplicationGroup 機能 は「ApplicationGroup 機能の用途を自動化管理の表示で確認する警告分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では SA z/OS の ApplicationGroup 機能と INGKYST0I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では ApplicationGroup 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.137) / OS 自動化ポリシー定義



### Assigning System Automation Symbols (AOCCLONE) {#c36-i1204}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Assigning System Automation Symbols (AOCCLONE)は、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.40) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 監査分離の自動化ポリシー定義で自動化管理の運用確認を行います。Assigning 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査分離の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査分離の自動化ポリシー定義を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、監査分離の点検結果を残す。 ✅
    - D. Assigning 機能の属性行を読まず監査分離の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Assigning 機能 は「SA z/OS で Assigning 機能の扱いを記録する監査分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Assigning 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Assigning 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.40) / OS 自動化ポリシー定義



### Automation Operators Entry Type {#c36-i1205}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Automation Operators Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 終端読解の自動化ポリシー定義に関係する Automation 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端読解の確認記録にまとめる。 ✅
    - B. Automation 機能の名称と担当者名のみを残して終端読解の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端読解の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端読解の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では Automation 機能 は「Automation 機能の用途を自動化管理の表示で確認する終端読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では SA z/OS の Automation 機能と INGKYST0I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では Automation 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義



### Automation Table, Message Revision Table, and MPFLSTxx member {#c36-i1206}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Automation Table, Message Revision Table, and MPFLSTxx memberは、Z System Automation (TSA)の自動化ポリシー定義でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力読解の自動化ポリシー定義に関する Automation 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力読解の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Automation 機能の変更点を出力本文から切り離して出力読解の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、出力読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では Automation 機能 は「Automation 機能の状態と出力メッセージを結び付ける出力読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では Automation 機能の出力行と INGKYST0I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では Automation 機能を SA z/OS の確認記録に残し、対象名は出力読解対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### BUILD CONTROL Policy Item {#c36-i1207}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

BUILD CONTROL Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.39) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 区切読解の自動化ポリシー定義で BUILD 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BUILD 機能の出力を取らず区切読解の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切読解の確認にする。 ✅
    - C. INGLIST を省略して区切読解の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では BUILD 機能 は「区切読解の自動化ポリシー定義に関係する定義値と表示行を照合する区切読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では BUILD 機能の属性行と INGKYST0I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では BUILD 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切読解初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.39) / OS 自動化ポリシー定義



### Batch Import with Data Modification {#c36-i1208}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Batch Import with Data Modificationは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件読解の自動化ポリシー定義に関係する Batch 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件読解として引き継ぐ。 ✅
    - B. Batch 機能の名称と担当者名のみを残して条件読解の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件読解の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件読解の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では Batch 機能 は「Batch 機能の用途を自動化管理の表示で確認する条件読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では SA z/OS の Batch 機能と INGKYST0I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では Batch 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Building and Distributing Configuration Files {#c36-i1209}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Building and Distributing Configuration Filesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲読解の自動化ポリシー定義で自動化管理の運用確認を行います。Building 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲読解の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲読解の自動化ポリシー定義を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、範囲読解の点検結果を残す。 ✅
    - D. Building 機能の属性行を読まず範囲読解の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Building 機能 は「SA z/OS で Building 機能の扱いを記録する範囲読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Building 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では Building 機能の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Building the Configuration Files {#c36-i1210}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Building the Configuration Filesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### COMMAND DEFINITIONS Policy Item {#c36-i1211}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

COMMAND DEFINITIONS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 警告読解の自動化ポリシー定義に関係する COMMAND 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告読解の確認記録にまとめる。 ✅
    - B. COMMAND 機能の名称と担当者名のみを残して警告読解の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告読解の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告読解の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では COMMAND 機能 は「COMMAND 機能の用途を自動化管理の表示で確認する警告読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では SA z/OS の COMMAND 機能と INGKYST0I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では COMMAND 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### COMMAND FLOODING Policy Item {#c36-i1212}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

COMMAND FLOODING Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 復旧読解の自動化ポリシー定義で COMMAND 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COMMAND 機能の出力を取らず復旧読解の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧読解の根拠にする。 ✅
    - C. INGLIST を省略して復旧読解の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では COMMAND 機能 は「復旧読解の自動化ポリシー定義に関係する定義値と表示行を照合する復旧読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では COMMAND 機能の属性行と INGKYST0I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では COMMAND 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### CONDITION Policy Item {#c36-i1213}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

CONDITION Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.234) / OS 自動化ポリシー定義

??? question "確認問題（4問）"
    **問題.** 構成面の条件定義を運用変更で確認します。設計面の対象項目では入力と操作画面応答を照合し、startup/shutdown conditionを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. DISPINFO
    - B. Observed Status
    - C. CONDITION Policy Item ✅
    - D. INGSUSPD SUSPEND

    正解: **C** ／ 難易度: 上級

    **解説:** 記録面の判定ではCを選び、対象は条件定義保守です。表示面の識別語は 条件 ポリシー項目 で、条件定義保守の対象名です。証跡面の条件定義監査は、トリガーで使う開始条件と停止条件を確認することを目的に扱う説明単位が条件定義引継ぎです。変更面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は条件定義棚卸です。復旧面の条件定義復旧を読む応答では、startup/shutdown conditionを出典の属性説明と照合する点が条件定義照合です。A: 引継ぎ面の条件定義保守で見るエージェント視点表示は役割が異なり、除外理由を説明する対象は条件定義保守です。B: 応答面の条件定義監査で見る観測状態は役割が異なり、除外理由を説明する対象は条件定義監査です。C: 定義面の条件定義引継ぎが正答です。復旧面の条件定義引継ぎ応答で確認できる対象は条件定義引継ぎです。D: 状態面の条件定義棚卸で見る自動化一時停止は役割が異なり、除外理由を説明する対象は条件定義棚卸です。障害面の初出語説明として、条件定義とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は条件定義証跡です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Defining Automation Policy p.210

    ---

    **問題.** 要求面の条件定義を障害切り分けで確認します。表示面の対象項目では入力と操作画面応答を照合し、startup/shutdown conditionを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. CONDITION Policy Item ✅
    - B. Configuration Dataset
    - C. SHUTDOWN Policy Item
    - D. INGVOTE

    正解: **A** ／ 難易度: 上級

    **解説:** 構成面の判定ではAを選び、対象は条件定義根拠です。記録面の識別語は 条件 ポリシー項目 で、条件定義根拠の対象名です。状態面の条件定義応答は、トリガーで使う開始条件と停止条件を確認することを目的に扱う説明単位が条件定義保守です。設計面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は条件定義監査です。証跡面の条件定義引継ぎを読む応答では、startup/shutdown conditionを出典の属性説明と照合する点が条件定義棚卸です。A: 監査面の条件定義根拠が正答です。定義面の条件定義根拠応答で確認できる対象は条件定義根拠です。B: 引継ぎ面の条件定義応答で見る構成データセットは役割が異なり、除外理由を説明する対象は条件定義応答です。C: 応答面の条件定義保守で見る停止ポリシーは役割が異なり、除外理由を説明する対象は条件定義保守です。D: 定義面の条件定義監査で見る投票表示は役割が異なり、除外理由を説明する対象は条件定義監査です。変更面の初出語説明として、条件定義とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は条件定義照合です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Defining Automation Policy p.210

    ---

    **問題.** 運用面の条件定義を監査記録で確認します。記録面の対象項目では入力と操作画面応答を照合し、startup/shutdown conditionを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGVOTE
    - B. INGAMS
    - C. CONDITION Policy Item ✅
    - D. DB2 CONTROL Policy Item

    正解: **C** ／ 難易度: 上級

    **解説:** 要求面の判定ではCを選び、対象は条件定義状態です。構成面の識別語は 条件 ポリシー項目 で、条件定義状態の対象名です。定義面の条件定義定義は、トリガーで使う開始条件と停止条件を確認することを目的に扱う説明単位が条件定義根拠です。表示面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は条件定義応答です。状態面の条件定義保守を読む応答では、startup/shutdown conditionを出典の属性説明と照合する点が条件定義監査です。A: 障害面の条件定義状態で見る投票表示は役割が異なり、除外理由を説明する対象は条件定義状態です。B: 監査面の条件定義定義で見るマネージャー一覧は役割が異なり、除外理由を説明する対象は条件定義定義です。C: 引継ぎ面の条件定義根拠が正答です。状態面の条件定義根拠応答で確認できる対象は条件定義根拠です。D: 応答面の条件定義応答で見るDb2制御項目は役割が異なり、除外理由を説明する対象は条件定義応答です。設計面の初出語説明として、条件定義とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は条件定義棚卸です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Defining Automation Policy p.210

    ---

    **問題.** 置換検分の自動化ポリシー定義に関する CONDITION 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換検分の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. CONDITION 機能の変更点を出力本文から切り離して置換検分の自動化ポリシー定義の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では CONDITION 機能 は「CONDITION 機能の状態と出力メッセージを結び付ける置換検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では CONDITION 機能の出力行と INGKYST0I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では CONDITION 機能を SA z/OS の確認記録に残し、対象名は置換検分対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.234) / OS 自動化ポリシー定義



### COPY Policy Item {#c36-i1214}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

COPY Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 優先検分の自動化ポリシー定義に関する COPY Policy Itemの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先検分の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. COPY Policy Itemの変更点を出力本文から切り離して優先検分の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、優先検分の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では COPY Policy Item は「COPY Policy Itemの状態と出力メッセージを結び付ける優先検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では COPY Policy Itemの出力行と INGKYST0I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では COPY Policy Itemを SA z/OS の確認記録に残し、対象名は優先検分対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義



### Changing Links {#c36-i1215}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Changing Linksは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 記録読解の自動化ポリシー定義に関係する Changing Linksの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録読解の確認値として扱う。 ✅
    - B. Changing Linksの名称と担当者名のみを残して記録読解の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録読解の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録読解の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では Changing Links は「Changing Linksの用途を自動化管理の表示で確認する記録読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では SA z/OS の Changing Linksと INGKYST0I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では Changing Linksを Z System Automation (TSA)で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義



### Changing Your Customization Dialog Environment {#c36-i1216}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Changing Your Customization Dialog Environmentは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.63) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 比較読解の自動化ポリシー定義で Changing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Changing 機能の出力を取らず比較読解の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較読解の根拠を固定する。 ✅
    - C. INGLIST を省略して比較読解の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Changing 機能 は「比較読解の自動化ポリシー定義に関係する定義値と表示行を照合する比較読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Changing 機能の属性行と INGKYST0I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Changing 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較読解初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.63) / OS 自動化ポリシー定義



### Class Hierarchy {#c36-i1217}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Class Hierarchyは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.40) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 順序読解の自動化ポリシー定義で自動化管理の運用確認を行います。Class Hierarchyの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序読解の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序読解の自動化ポリシー定義を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を順序読解で確認する。 ✅
    - D. Class Hierarchyの属性行を読まず順序読解の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Class Hierarchy は「SA z/OS で Class Hierarchyの扱いを記録する順序読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Class Hierarchyの表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では Class Hierarchyの使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.40) / OS 自動化ポリシー定義



### Code Processing for OPC Workstation Domains {#c36-i1218}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Code Processing for OPC Workstation Domainsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域読解の自動化ポリシー定義に関する Code 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域読解の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Code 機能の変更点を出力本文から切り離して値域読解の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、値域読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では Code 機能 は「Code 機能の状態と出力メッセージを結び付ける値域読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では Code 機能の出力行と INGKYST0I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では Code 機能を SA z/OS の確認記録に残し、対象名は値域読解対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Common Policy Items {#c36-i1219}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Common Policy Itemsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 監査読解の自動化ポリシー定義で自動化管理の運用確認を行います。Common 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査読解の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査読解の自動化ポリシー定義を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、監査読解の結果として保存する。 ✅
    - D. Common 機能の属性行を読まず監査読解の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では Common 機能 は「SA z/OS で Common 機能の扱いを記録する監査読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では Common 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では Common 機能の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義



### Concurrent Customization by Multiple Users {#c36-i1220}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Concurrent Customization by Multiple Usersは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更読解の自動化ポリシー定義に関する Concurrent 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更読解の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Concurrent 機能の変更点を出力本文から切り離して変更読解の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、変更読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Concurrent 機能 は「Concurrent 機能の状態と出力メッセージを結び付ける変更読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Concurrent 機能の出力行と INGKYST0I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Concurrent 機能を SA z/OS の確認記録に残し、対象名は変更読解対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Concurrent User Access {#c36-i1221}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Concurrent User Accessは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 構文検分の自動化ポリシー定義に関係する Concurrent 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文検分として引き継ぐ。 ✅
    - B. Concurrent 機能の名称と担当者名のみを残して構文検分の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文検分の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文検分の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Concurrent 機能 は「Concurrent 機能の用途を自動化管理の表示で確認する構文検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では SA z/OS の Concurrent 機能と INGKYST0I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Concurrent 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義



### Concurrent User Access Capabilities {#c36-i1222}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Concurrent User Access Capabilitiesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 展開検分の自動化ポリシー定義で Concurrent 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Concurrent 機能の出力を取らず展開検分の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検分の確認にする。 ✅
    - C. INGLIST を省略して展開検分の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Concurrent 機能 は「展開検分の自動化ポリシー定義に関係する定義値と表示行を照合する展開検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Concurrent 機能の属性行と INGKYST0I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Concurrent 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開検分初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義



### Concurrent User Access within the Customization Dialog {#c36-i1223}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Concurrent User Access within the Customization Dialogは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出検分の自動化ポリシー定義で自動化管理の運用確認を行います。Concurrent 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出検分の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出検分の自動化ポリシー定義を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、呼出検分の点検結果を残す。 ✅
    - D. Concurrent 機能の属性行を読まず呼出検分の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では Concurrent 機能 は「SA z/OS で Concurrent 機能の扱いを記録する呼出検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では Concurrent 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では Concurrent 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Configuration Files Build Options {#c36-i1224}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Configuration Files Build Optionsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 終端検分の自動化ポリシー定義に関係する Configuration 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端検分の確認値として扱う。 ✅
    - B. Configuration 機能の名称と担当者名のみを残して終端検分の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端検分の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端検分の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Configuration 機能 は「Configuration 機能の用途を自動化管理の表示で確認する終端検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では SA z/OS の Configuration 機能と INGKYST0I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Configuration 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義



### Configuring a Resource that is Externally Stopped {#c36-i1225}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Configuring a Resource that is Externally Stoppedは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書検分の自動化ポリシー定義で自動化管理の運用確認を行います。Configuring 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書検分の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書検分の自動化ポリシー定義を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を上書検分で確認する。 ✅
    - D. Configuring 機能の属性行を読まず上書検分の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では Configuring 機能 は「SA z/OS で Configuring 機能の扱いを記録する上書検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では Configuring 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では Configuring 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Configuring a resource that is externally started {#c36-i1226}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Configuring a resource that is externally startedは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索検分の自動化ポリシー定義で Configuring 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Configuring 機能の出力を取らず探索検分の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索検分の根拠を固定する。 ✅
    - C. INGLIST を省略して探索検分の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Configuring 機能 は「探索検分の自動化ポリシー定義に関係する定義値と表示行を照合する探索検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Configuring 機能の属性行と INGKYST0I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Configuring 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Considerations for Automation {#c36-i1227}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Considerations for Automationは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力検分の自動化ポリシー定義に関する Considerations 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力検分の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Considerations 機能の変更点を出力本文から切り離して出力検分の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、出力検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では Considerations 機能 は「Considerations 機能の状態と出力メッセージを結び付ける出力検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では Considerations 機能の出力行と INGKYST0I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では Considerations 機能を SA z/OS の確認記録に残し、対象名は出力検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Conversion Function {#c36-i1228}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Conversion Functionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 条件検分の自動化ポリシー定義に関係する Conversion 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件検分の確認記録にまとめる。 ✅
    - B. Conversion 機能の名称と担当者名のみを残して条件検分の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件検分の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件検分の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Conversion 機能 は「Conversion 機能の用途を自動化管理の表示で確認する条件検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では SA z/OS の Conversion 機能と INGKYST0I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Conversion 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義



### Converting from SA z/OS 4.1 {#c36-i1229}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Converting from SA z/OS 4.1は、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 区切検分のConverting from SA z/OS 4.1で Converting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Converting 機能の出力を取らず区切検分のConverting from SA z/OS 4.1の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検分の根拠にする。 ✅
    - C. INGLIST を省略して区切検分のConverting from SA z/OS 4.1の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分のConverting from SA z/OS 4.1へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Converting 機能 は「区切検分のConverting from SA z/OS 4.1に関係する定義値と表示行を照合する区切検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Converting 機能の属性行と INGKYST0I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Converting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切検分初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義



### Converting from SA z/OS 4.2 {#c36-i1230}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Converting from SA z/OS 4.2は、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 範囲検分のConverting from SA z/OS 4.2で自動化管理の運用確認を行います。Converting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲検分のConverting from SA z/OS 4.2を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲検分のConverting from SA z/OS 4.2を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、範囲検分の結果として保存する。 ✅
    - D. Converting 機能の属性行を読まず範囲検分のConverting from SA z/OS 4.2の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Converting 機能 は「SA z/OS で Converting 機能の扱いを記録する範囲検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Converting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Converting 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義



### Creating New Policy Objects Using Text Files {#c36-i1231}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating New Policy Objects Using Text Filesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文確認の自動化ポリシー定義に関係する Creating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文確認の確認にする。 ✅
    - B. Creating 機能の名称と担当者名のみを残して構文確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Creating 機能 は「Creating 機能の用途を自動化管理の表示で確認する構文確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では SA z/OS の Creating 機能と INGKYST0I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Creating 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating Reports about Policy Databases {#c36-i1232}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating Reports about Policy Databasesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開確認の自動化ポリシー定義で Creating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Creating 機能の出力を取らず展開確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、展開確認の点検結果を残す。 ✅
    - C. INGLIST を省略して展開確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Creating 機能 は「展開確認の自動化ポリシー定義に関係する定義値と表示行を照合する展開確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Creating 機能の属性行と INGKYST0I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Creating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New Application {#c36-i1233}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Applicationは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録検分の自動化ポリシー定義に関係する Creating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録検分として引き継ぐ。 ✅
    - B. Creating 機能の名称と担当者名のみを残して記録検分の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録検分の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録検分の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Creating 機能 は「Creating 機能の用途を自動化管理の表示で確認する記録検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では SA z/OS の Creating 機能と INGKYST0I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Creating 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New Application Group {#c36-i1234}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Application Groupは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較検分の自動化ポリシー定義で Creating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Creating 機能の出力を取らず比較検分の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較検分の確認にする。 ✅
    - C. INGLIST を省略して比較検分の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Creating 機能 は「比較検分の自動化ポリシー定義に関係する定義値と表示行を照合する比較検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Creating 機能の属性行と INGKYST0I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Creating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New Event {#c36-i1235}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Eventは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序検分の自動化ポリシー定義で自動化管理の運用確認を行います。Creating 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序検分の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序検分の自動化ポリシー定義を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、順序検分の点検結果を残す。 ✅
    - D. Creating 機能の属性行を読まず順序検分の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Creating 機能 は「SA z/OS で Creating 機能の扱いを記録する順序検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Creating 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Creating 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New Group {#c36-i1236}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Groupは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域検分の自動化ポリシー定義に関する Creating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域検分の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Creating 機能の変更点を出力本文から切り離して値域検分の自動化ポリシー定義の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Creating 機能 は「Creating 機能の状態と出力メッセージを結び付ける値域検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Creating 機能の出力行と INGKYST0I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Creating 機能を SA z/OS の確認記録に残し、対象名は値域検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New Policy Database {#c36-i1237}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Policy Databaseは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Creating a New Processor {#c36-i1238}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Processorは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧検分の自動化ポリシー定義で Creating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Creating 機能の出力を取らず復旧検分の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧検分の根拠を固定する。 ✅
    - C. INGLIST を省略して復旧検分の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Creating 機能 は「復旧検分の自動化ポリシー定義に関係する定義値と表示行を照合する復旧検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Creating 機能の属性行と INGKYST0I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Creating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New SubGroup {#c36-i1239}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New SubGroupは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査検分の自動化ポリシー定義で自動化管理の運用確認を行います。Creating 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査検分の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査検分の自動化ポリシー定義を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を監査検分で確認する。 ✅
    - D. Creating 機能の属性行を読まず監査検分の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Creating 機能 は「SA z/OS で Creating 機能の扱いを記録する監査検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Creating 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Creating 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a New System {#c36-i1240}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Creating a New Systemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更検分の自動化ポリシー定義に関する Creating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更検分の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Creating 機能の変更点を出力本文から切り離して変更検分の自動化ポリシー定義の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、変更検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Creating 機能 は「Creating 機能の状態と出力メッセージを結び付ける変更検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Creating 機能の出力行と INGKYST0I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Creating 機能を SA z/OS の確認記録に残し、対象名は変更検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### DESCRIPTION Policy Item {#c36-i1241}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

DESCRIPTION Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 出力確認の自動化ポリシー定義に関する DESCRIPTION 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. DESCRIPTION 機能の変更点を出力本文から切り離して出力確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力確認の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では DESCRIPTION 機能 は「DESCRIPTION 機能の状態と出力メッセージを結び付ける出力確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では DESCRIPTION 機能の出力行と INGKYST0I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では DESCRIPTION 機能を SA z/OS の確認記録に残し、対象名は出力確認対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義



### DOMAIN INFO Policy Item {#c36-i1242}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

DOMAIN INFO Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 区切確認の自動化ポリシー定義で DOMAIN 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DOMAIN 機能の出力を取らず区切確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と INGKYST0I を読み、区切確認の結果として保存する。 ✅
    - C. INGLIST を省略して区切確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では DOMAIN 機能 は「区切確認の自動化ポリシー定義に関係する定義値と表示行を照合する区切確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では DOMAIN 機能の属性行と INGKYST0I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では DOMAIN 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切確認初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### DOWNWARD CLASS/INST Policy Item {#c36-i1243}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

DOWNWARD CLASS/INST Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 範囲確認のDOWNWARD CLASS/INST Policy Itemで自動化管理の運用確認を行います。DOWNWARD CLASS 属性の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲確認のDOWNWARD CLASS/INST Policy Itemを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲確認のDOWNWARD CLASS/INST Policy Itemを正常終了として記録する。
    - C. INGLIST で得た表示本文を使い、範囲確認の採否を説明欄に結び付ける。 ✅
    - D. DOWNWARD CLASS 属性の属性行を読まず範囲確認のDOWNWARD CLASS/INST Policy Itemの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では DOWNWARD CLASS 属性 は「SA z/OS で DOWNWARD CLASS 属性の扱いを記録する範囲確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では DOWNWARD CLASS 属性の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では DOWNWARD CLASS 属性の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### Data Management {#c36-i1244}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Data Managementは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出確認の自動化ポリシー定義で自動化管理の運用確認を行います。Data Managementの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出確認の自動化ポリシー定義を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出確認で再確認できる形にする。 ✅
    - D. Data Managementの属性行を読まず呼出確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Data Management は「SA z/OS で Data Managementの扱いを記録する呼出確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Data Managementの表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Data Managementの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Defining Automation for OPC Components {#c36-i1245}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Defining Automation for OPC Componentsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換確認の自動化ポリシー定義に関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して置換確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける置換確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Defining 機能の出力行と INGKYST0I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Defining 機能を SA z/OS の確認記録に残し、対象名は置換確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Defining Data Sets for Batch Processing {#c36-i1246}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Defining Data Sets for Batch Processingは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端確認の自動化ポリシー定義に関係する Defining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端確認の根拠を固定する。 ✅
    - B. Defining 機能の名称と担当者名のみを残して終端確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Defining 機能 は「Defining 機能の用途を自動化管理の表示で確認する終端確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では SA z/OS の Defining 機能と INGKYST0I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Defining 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Defining ISPF Temporary Data Sets for Batch Build {#c36-i1247}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Defining ISPF Temporary Data Sets for Batch Buildは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索確認の自動化ポリシー定義で Defining 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Defining 機能の出力を取らず探索確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGKYST0I を含む表示を保存し、説明欄との差分を探索確認で確認する。 ✅
    - C. INGLIST を省略して探索確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Defining 機能 は「探索確認の自動化ポリシー定義に関係する定義値と表示行を照合する探索確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Defining 機能の属性行と INGKYST0I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Defining 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Deleting Policy Objects Using Text Files {#c36-i1248}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Deleting Policy Objects Using Text Filesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書確認の自動化ポリシー定義で自動化管理の運用確認を行います。Deleting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書確認の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST の結果から対象行を抜き出し、上書確認の証跡として残す。 ✅
    - D. Deleting 機能の属性行を読まず上書確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Deleting 機能 は「SA z/OS で Deleting 機能の扱いを記録する上書確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Deleting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Deleting 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Distributing the Configuration Files {#c36-i1249}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Distributing the Configuration Filesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.341) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 条件確認の自動化ポリシー定義に関係する Distributing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件確認の根拠にする。 ✅
    - B. Distributing 機能の名称と担当者名のみを残して条件確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では Distributing 機能 は「Distributing 機能の用途を自動化管理の表示で確認する条件確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では SA z/OS の Distributing 機能と INGKYST0I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では Distributing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.341) / OS 自動化ポリシー定義



### E-T DATA Policy Item {#c36-i1250}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

E-T DATA Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 優先確認の自動化ポリシー定義に関する E-T 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. E-T 機能の変更点を出力本文から切り離して優先確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先確認として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では E-T 機能 は「E-T 機能の状態と出力メッセージを結び付ける優先確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では E-T 機能の出力行と INGKYST0I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では E-T 機能を SA z/OS の確認記録に残し、対象名は優先確認対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### Early Start {#c36-i1251}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Early Startは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 記録確認の自動化ポリシー定義に関係する Early Startの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録確認の確認にする。 ✅
    - B. Early Startの名称と担当者名のみを残して記録確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Early Start は「Early Startの用途を自動化管理の表示で確認する記録確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では SA z/OS の Early Startと INGKYST0I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Early Startを Z System Automation (TSA)で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義



### Enabling AT Updates {#c36-i1252}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Enabling AT Updatesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序確認の自動化ポリシー定義で自動化管理の運用確認を行います。Enabling 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序確認の自動化ポリシー定義を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序確認で再確認できる形にする。 ✅
    - D. Enabling 機能の属性行を読まず順序確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Enabling 機能 は「SA z/OS で Enabling 機能の扱いを記録する順序確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Enabling 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Enabling 機能の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Enabling and Disabling AT / MRT Syntax Checking {#c36-i1253}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Enabling and Disabling AT / MRT Syntax Checkingは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較確認の自動化ポリシー定義で Enabling 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Enabling 機能の出力を取らず比較確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、比較確認の点検結果を残す。 ✅
    - C. INGLIST を省略して比較確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Enabling 機能 は「比較確認の自動化ポリシー定義に関係する定義値と表示行を照合する比較確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Enabling 機能の属性行と INGKYST0I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Enabling 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Enterprise Entry Type {#c36-i1254}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Enterprise Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 値域確認の自動化ポリシー定義に関する Enterprise 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Enterprise 機能の変更点を出力本文から切り離して値域確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Enterprise 機能 は「Enterprise 機能の状態と出力メッセージを結び付ける値域確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Enterprise 機能の出力行と INGKYST0I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Enterprise 機能を SA z/OS の確認記録に残し、対象名は値域確認対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義



### Entry Name Selection {#c36-i1255}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Entry Name Selectionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告確認の自動化ポリシー定義に関係する Entry 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告確認の根拠を固定する。 ✅
    - B. Entry 機能の名称と担当者名のみを残して警告確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Entry 機能 は「Entry 機能の用途を自動化管理の表示で確認する警告確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では SA z/OS の Entry 機能と INGKYST0I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Entry 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Entry Type Introduction {#c36-i1256}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Entry Type Introductionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.26) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 復旧確認の自動化ポリシー定義で Entry 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Entry 機能の出力を取らず復旧確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGKYST0I を含む表示を保存し、説明欄との差分を復旧確認で確認する。 ✅
    - C. INGLIST を省略して復旧確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Entry 機能 は「復旧確認の自動化ポリシー定義に関係する定義値と表示行を照合する復旧確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Entry 機能の属性行と INGKYST0I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Entry 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.26) / OS 自動化ポリシー定義



### Entry Type Reference {#c36-i1257}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Entry Type Reference は 自動化ポリシー定義 の項目。Figure 118 on page 176. Message Automation Definitions for Applications.

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.203) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 監査確認の自動化ポリシー定義で自動化管理の運用確認を行います。Entry 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査確認の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST の結果から対象行を抜き出し、監査確認の証跡として残す。 ✅
    - D. Entry 機能の属性行を読まず監査確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Entry 機能 は「SA z/OS で Entry 機能の扱いを記録する監査確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Entry 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Entry 機能の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.203) / OS 自動化ポリシー定義



### Entry Type Selection {#c36-i1258}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Entry Type Selectionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更確認の自動化ポリシー定義に関する Entry 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Entry 機能の変更点を出力本文から切り離して変更確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更確認の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Entry 機能 は「Entry 機能の状態と出力メッセージを結び付ける変更確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Entry 機能の出力行と INGKYST0I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Entry 機能を SA z/OS の確認記録に残し、対象名は変更確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Events Entry Type {#c36-i1259}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Events Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.234) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 構文照合の自動化ポリシー定義に関係する Events Entry Typeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文照合の根拠にする。 ✅
    - B. Events Entry Typeの名称と担当者名のみを残して構文照合の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文照合の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文照合の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Events Entry Type は「Events Entry Typeの用途を自動化管理の表示で確認する構文照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では SA z/OS の Events Entry Typeと INGKYST0I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Events Entry Typeを Z System Automation (TSA)で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.234) / OS 自動化ポリシー定義



### Extending Policy Definitions {#c36-i1260}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Extending Policy Definitionsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 展開照合の自動化ポリシー定義で Extending 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Extending 機能の出力を取らず展開照合の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と INGKYST0I を読み、展開照合の結果として保存する。 ✅
    - C. INGLIST を省略して展開照合の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では Extending 機能 は「展開照合の自動化ポリシー定義に関係する定義値と表示行を照合する展開照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では Extending 機能の属性行と INGKYST0I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では Extending 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開照合初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義



### External Startup Sequence {#c36-i1261}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

External Startup Sequenceは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.94) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 呼出照合の自動化ポリシー定義で自動化管理の運用確認を行います。External 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出照合の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出照合の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST で得た表示本文を使い、呼出照合の採否を説明欄に結び付ける。 ✅
    - D. External 機能の属性行を読まず呼出照合の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では External 機能 は「SA z/OS で External 機能の扱いを記録する呼出照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では External 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では External 機能の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.94) / OS 自動化ポリシー定義



### FORCEDOWN - Configuring a Resource to be Automatically Shutdown {#c36-i1262}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

FORCEDOWN - Configuring a Resource to be Automatically Shutdownは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換照合の自動化ポリシー定義に関する FORCEDOWN 出口の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換照合の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. FORCEDOWN 出口の変更点を出力本文から切り離して置換照合の自動化ポリシー定義の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換照合として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では FORCEDOWN 出口 は「FORCEDOWN 出口の状態と出力メッセージを結び付ける置換照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では FORCEDOWN 出口の出力行と INGKYST0I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では FORCEDOWN 出口を SA z/OS の確認記録に残し、対象名は置換照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### FULL SESSIONS Policy Item {#c36-i1263}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

FULL SESSIONS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 終端照合の自動化ポリシー定義に関係する FULL 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端照合の確認にする。 ✅
    - B. FULL 機能の名称と担当者名のみを残して終端照合の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端照合の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端照合の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では FULL 機能 は「FULL 機能の用途を自動化管理の表示で確認する終端照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では SA z/OS の FULL 機能と INGKYST0I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では FULL 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### GATEWAY Policy Item {#c36-i1264}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

GATEWAY Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 探索照合の自動化ポリシー定義で GATEWAY 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. GATEWAY 機能の出力を取らず探索照合の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、探索照合の点検結果を残す。 ✅
    - C. INGLIST を省略して探索照合の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では GATEWAY 機能 は「探索照合の自動化ポリシー定義に関係する定義値と表示行を照合する探索照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では GATEWAY 機能の属性行と INGKYST0I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では GATEWAY 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索照合初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### GENERATED RESOURCES Policy Item {#c36-i1265}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

GENERATED RESOURCES Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.164) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 上書照合の自動化ポリシー定義で自動化管理の運用確認を行います。GENERATED 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書照合の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書照合の自動化ポリシー定義を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書照合で再確認できる形にする。 ✅
    - D. GENERATED 機能の属性行を読まず上書照合の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では GENERATED 機能 は「SA z/OS で GENERATED 機能の扱いを記録する上書照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では GENERATED 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では GENERATED 機能の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.164) / OS 自動化ポリシー定義



### GROUP INFO Policy Item {#c36-i1266}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

GROUP INFO Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.148) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 記録照合の自動化ポリシー定義に関係する GROUP 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録照合の根拠にする。 ✅
    - B. GROUP 機能の名称と担当者名のみを残して記録照合の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録照合の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録照合の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では GROUP 機能 は「GROUP 機能の用途を自動化管理の表示で確認する記録照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では SA z/OS の GROUP 機能と INGKYST0I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では GROUP 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録照合用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.148) / OS 自動化ポリシー定義



### Generating a Job for Batch Build {#c36-i1267}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Generating a Job for Batch Buildは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力照合の自動化ポリシー定義に関する Generating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力照合の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Generating 機能の変更点を出力本文から切り離して出力照合の自動化ポリシー定義の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では Generating 機能 は「Generating 機能の状態と出力メッセージを結び付ける出力照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では Generating 機能の出力行と INGKYST0I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では Generating 機能を SA z/OS の確認記録に残し、対象名は出力照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Generating a Job for Batch Conversion {#c36-i1268}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Generating a Job for Batch Conversionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件照合の自動化ポリシー定義に関係する Generating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件照合の根拠を固定する。 ✅
    - B. Generating 機能の名称と担当者名のみを残して条件照合の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件照合の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件照合の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では Generating 機能 は「Generating 機能の用途を自動化管理の表示で確認する条件照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では SA z/OS の Generating 機能と INGKYST0I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では Generating 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Generating a Job for Batch Update {#c36-i1269}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Generating a Job for Batch Updateは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切照合の自動化ポリシー定義で Generating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Generating 機能の出力を取らず区切照合の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGKYST0I を含む表示を保存し、説明欄との差分を区切照合で確認する。 ✅
    - C. INGLIST を省略して区切照合の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では Generating 機能 は「区切照合の自動化ポリシー定義に関係する定義値と表示行を照合する区切照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では Generating 機能の属性行と INGKYST0I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では Generating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Getting Help {#c36-i1270}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Getting Helpは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Group Entry Type {#c36-i1271}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Group Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.249) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 優先照合の自動化ポリシー定義に関する Group Entry Typeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先照合の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Group Entry Typeの変更点を出力本文から切り離して優先照合の自動化ポリシー定義の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先照合の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では Group Entry Type は「Group Entry Typeの状態と出力メッセージを結び付ける優先照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では Group Entry Typeの出力行と INGKYST0I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では Group Entry Typeを SA z/OS の確認記録に残し、対象名は優先照合対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.249) / OS 自動化ポリシー定義



### Grouping the Resources {#c36-i1272}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Grouping the Resourcesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.63) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 比較照合の自動化ポリシー定義で Grouping 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Grouping 機能の出力を取らず比較照合の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と INGKYST0I を読み、比較照合の結果として保存する。 ✅
    - C. INGLIST を省略して比較照合の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では Grouping 機能 は「比較照合の自動化ポリシー定義に関係する定義値と表示行を照合する比較照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では Grouping 機能の属性行と INGKYST0I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では Grouping 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較照合初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.63) / OS 自動化ポリシー定義



### HEALTHSTATE Policy Item {#c36-i1273}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

HEALTHSTATE Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 順序照合の自動化ポリシー定義で自動化管理の運用確認を行います。HEALTHSTATE 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序照合の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序照合の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST で得た表示本文を使い、順序照合の採否を説明欄に結び付ける。 ✅
    - D. HEALTHSTATE 機能の属性行を読まず順序照合の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では HEALTHSTATE 機能 は「SA z/OS で HEALTHSTATE 機能の扱いを記録する順序照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では HEALTHSTATE 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では HEALTHSTATE 機能の使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### How to Apply Service Updates {#c36-i1274}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Apply Service Updatesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域照合の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域照合の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して値域照合の自動化ポリシー定義の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域照合として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける値域照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では How 機能を SA z/OS の確認記録に残し、対象名は値域照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Browse a Policy Item {#c36-i1275}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Browse a Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告照合の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告照合の確認にする。 ✅
    - B. How 機能の名称と担当者名のみを残して警告照合の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告照合の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告照合の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する警告照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Build Alternate and Tertiary Configurations {#c36-i1276}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Build Alternate and Tertiary Configurationsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧照合の自動化ポリシー定義で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず復旧照合の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、復旧照合の点検結果を残す。 ✅
    - C. INGLIST を省略して復旧照合の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では How 機能 は「復旧照合の自動化ポリシー定義に関係する定義値と表示行を照合する復旧照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では How 機能の属性行と INGKYST0I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では How 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Cancel Input on a Panel {#c36-i1277}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Cancel Input on a Panelは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査照合の自動化ポリシー定義で自動化管理の運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査照合の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査照合の自動化ポリシー定義を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査照合で再確認できる形にする。 ✅
    - D. How 機能の属性行を読まず監査照合の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では How 機能 は「SA z/OS で How 機能の扱いを記録する監査照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では How 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では How 機能の使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Convert an APG from Model 1 to Model 2 {#c36-i1278}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Convert an APG from Model 1 to Model 2は、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更照合の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更照合の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して変更照合の自動化ポリシー定義の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける変更照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では How 機能を SA z/OS の確認記録に残し、対象名は変更照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Create New Policy Objects {#c36-i1279}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Create New Policy Objectsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開追跡の自動化ポリシー定義で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず展開追跡の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGKYST0I を含む表示を保存し、説明欄との差分を展開追跡で確認する。 ✅
    - C. INGLIST を省略して展開追跡の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では How 機能 は「展開追跡の自動化ポリシー定義に関係する定義値と表示行を照合する展開追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では How 機能の属性行と INGKYST0I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では How 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Create a Policy Database Report in JSON Format {#c36-i1280}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Create a Policy Database Report in JSON Formatは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文追跡の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文追跡の根拠を固定する。 ✅
    - B. How 機能の名称と担当者名のみを残して構文追跡の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文追跡の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文追跡の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する構文追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Define Alternate and Tertiary Configurations for Systems {#c36-i1281}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Define Alternate and Tertiary Configurations for Systemsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出追跡の自動化ポリシー定義で自動化管理の運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出追跡の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出追跡の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST の結果から対象行を抜き出し、呼出追跡の証跡として残す。 ✅
    - D. How 機能の属性行を読まず呼出追跡の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では How 機能 は「SA z/OS で How 機能の扱いを記録する呼出追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では How 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では How 機能の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Define Automation Policy: An Outline {#c36-i1282}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Define Automation Policy: An Outlineは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換追跡の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換追跡の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して置換追跡の自動化ポリシー定義の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける置換追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では How 機能を SA z/OS の確認記録に残し、対象名は置換追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Define Data Sets for Build Processing {#c36-i1283}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Define Data Sets for Build Processingは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端追跡の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端追跡の根拠にする。 ✅
    - B. How 機能の名称と担当者名のみを残して終端追跡の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端追跡の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端追跡の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する終端追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Delete Policy Objects {#c36-i1284}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Delete Policy Objectsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書追跡の自動化ポリシー定義で自動化管理の運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書追跡の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書追跡の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST で得た表示本文を使い、上書追跡の採否を説明欄に結び付ける。 ✅
    - D. How 機能の属性行を読まず上書追跡の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では How 機能 は「SA z/OS で How 機能の扱いを記録する上書追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では How 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では How 機能の使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Delete Several Policy Objects in One Go (Bulk Deletion) {#c36-i1285}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Delete Several Policy Objects in One Go (Bulk Deletion)は、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力追跡の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力追跡の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して出力追跡の自動化ポリシー定義の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力追跡として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける出力追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では How 機能を SA z/OS の確認記録に残し、対象名は出力追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Delete a Single Policy Object {#c36-i1286}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Delete a Single Policy Objectは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索追跡の自動化ポリシー定義で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず探索追跡の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と INGKYST0I を読み、探索追跡の結果として保存する。 ✅
    - C. INGLIST を省略して探索追跡の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では How 機能 は「探索追跡の自動化ポリシー定義に関係する定義値と表示行を照合する探索追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では How 機能の属性行と INGKYST0I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では How 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Find Data in a Policy Item {#c36-i1287}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Find Data in a Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件追跡の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件追跡の確認にする。 ✅
    - B. How 機能の名称と担当者名のみを残して条件追跡の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件追跡の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件追跡の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する条件追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Implement Message Processing with User-Defined Data {#c36-i1288}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Implement Message Processing with User-Defined Dataは、Z System Automation (TSA)の自動化ポリシー定義でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切追跡の自動化ポリシー定義で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず区切追跡の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、区切追跡の点検結果を残す。 ✅
    - C. INGLIST を省略して区切追跡の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では How 機能 は「区切追跡の自動化ポリシー定義に関係する定義値と表示行を照合する区切追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では How 機能の属性行と INGKYST0I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では How 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Navigate in the Customization Dialog {#c36-i1289}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Navigate in the Customization Dialogは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲追跡の自動化ポリシー定義で自動化管理の運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲追跡の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲追跡の自動化ポリシー定義を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、範囲追跡で再確認できる形にする。 ✅
    - D. How 機能の属性行を読まず範囲追跡の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では How 機能 は「SA z/OS で How 機能の扱いを記録する範囲追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では How 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では How 機能の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Rename a Policy Object {#c36-i1290}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Rename a Policy Objectは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先追跡の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先追跡の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して優先追跡の自動化ポリシー定義の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、優先追跡の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける優先追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では How 機能を SA z/OS の確認記録に残し、対象名は優先追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Start the Customization Dialog {#c36-i1291}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Start the Customization Dialogは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録追跡の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録追跡の根拠を固定する。 ✅
    - B. How 機能の名称と担当者名のみを残して記録追跡の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録追跡の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録追跡の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する記録追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Use Schedules (Service Periods) {#c36-i1292}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Use Schedules (Service Periods)は、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域追跡の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域追跡の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して値域追跡の自動化ポリシー定義の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける値域追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では How 機能を SA z/OS の確認記録に残し、対象名は値域追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Use Triggers and Events {#c36-i1293}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Use Triggers and Eventsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告追跡の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告追跡の根拠にする。 ✅
    - B. How 機能の名称と担当者名のみを残して警告追跡の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告追跡の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告追跡の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する警告追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Use User E-T Pairs {#c36-i1294}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Use User E-T Pairsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧追跡の自動化ポリシー定義で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず復旧追跡の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と INGKYST0I を読み、復旧追跡の結果として保存する。 ✅
    - C. INGLIST を省略して復旧追跡の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では How 機能 は「復旧追跡の自動化ポリシー定義に関係する定義値と表示行を照合する復旧追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では How 機能の属性行と INGKYST0I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では How 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Use a Policy Item as a Fast Path {#c36-i1295}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Use a Policy Item as a Fast Pathは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較追跡の自動化ポリシー定義で How 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. How 機能の出力を取らず比較追跡の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGKYST0I を含む表示を保存し、説明欄との差分を比較追跡で確認する。 ✅
    - C. INGLIST を省略して比較追跡の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では How 機能 は「比較追跡の自動化ポリシー定義に関係する定義値と表示行を照合する比較追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では How 機能の属性行と INGKYST0I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では How 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Use an Entry Type as a Fast Path {#c36-i1296}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Use an Entry Type as a Fast Pathは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序追跡の自動化ポリシー定義で自動化管理の運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序追跡の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序追跡の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST の結果から対象行を抜き出し、順序追跡の証跡として残す。 ✅
    - D. How 機能の属性行を読まず順序追跡の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では How 機能 は「SA z/OS で How 機能の扱いを記録する順序追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では How 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では How 機能の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to View Long Input Fields in Full Length {#c36-i1297}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to View Long Input Fields in Full Lengthは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査追跡の自動化ポリシー定義で自動化管理の運用確認を行います。How 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査追跡の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査追跡の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST で得た表示本文を使い、監査追跡の採否を説明欄に結び付ける。 ✅
    - D. How 機能の属性行を読まず監査追跡の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では How 機能 は「SA z/OS で How 機能の扱いを記録する監査追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では How 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では How 機能の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Work with Externally Stopped and Started Resources {#c36-i1298}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Work with Externally Stopped and Started Resourcesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更追跡の自動化ポリシー定義に関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更追跡の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して変更追跡の自動化ポリシー定義の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更追跡として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける変更追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では How 機能を SA z/OS の確認記録に残し、対象名は変更追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### How to Work with Resources {#c36-i1299}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

How to Work with Resourcesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文検査の自動化ポリシー定義に関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文検査の確認にする。 ✅
    - B. How 機能の名称と担当者名のみを残して構文検査の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文検査の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文検査の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する構文検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### INGSEND PARMS Policy Item {#c36-i1300}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

INGSEND PARMS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 置換検査の自動化ポリシー定義に関する INGSEND 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換検査の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. INGSEND 機能の変更点を出力本文から切り離して置換検査の自動化ポリシー定義の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換検査の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では INGSEND 機能 は「INGSEND 機能の状態と出力メッセージを結び付ける置換検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では INGSEND 機能の出力行と INGKYST0I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では INGSEND 機能を SA z/OS の確認記録に残し、対象名は置換検査対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### IPL INFO Policy Item {#c36-i1301}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

IPL INFO Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.137) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 出力検査の自動化ポリシー定義に関する IPL 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力検査の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. IPL 機能の変更点を出力本文から切り離して出力検査の自動化ポリシー定義の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では IPL 機能 は「IPL 機能の状態と出力メッセージを結び付ける出力検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では IPL 機能の出力行と INGKYST0I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では IPL 機能を SA z/OS の確認記録に残し、対象名は出力検査対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.137) / OS 自動化ポリシー定義



### Importing Policy Database Data {#c36-i1302}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Importing Policy Database Dataは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開検査の自動化ポリシー定義で Importing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Importing 機能の出力を取らず展開検査の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、展開検査の点検結果を残す。 ✅
    - C. INGLIST を省略して展開検査の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では Importing 機能 は「展開検査の自動化ポリシー定義に関係する定義値と表示行を照合する展開検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では Importing 機能の属性行と INGKYST0I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では Importing 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Importing Sample Add-On Policies {#c36-i1303}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Importing Sample Add-On Policiesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出検査の自動化ポリシー定義で自動化管理の運用確認を行います。Importing 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出検査の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出検査の自動化ポリシー定義を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出検査で再確認できる形にする。 ✅
    - D. Importing 機能の属性行を読まず呼出検査の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では Importing 機能 は「SA z/OS で Importing 機能の扱いを記録する呼出検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では Importing 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では Importing 機能の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Inheritance and Defaulting {#c36-i1304}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Inheritance and Defaultingは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.40) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 終端検査の自動化ポリシー定義に関係する Inheritance 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端検査の根拠を固定する。 ✅
    - B. Inheritance 機能の名称と担当者名のみを残して終端検査の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端検査の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端検査の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Inheritance 機能 は「Inheritance 機能の用途を自動化管理の表示で確認する終端検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では SA z/OS の Inheritance 機能と INGKYST0I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Inheritance 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.40) / OS 自動化ポリシー定義



### Initial Policy Database Conversion {#c36-i1305}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Initial Policy Database Conversionは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 探索検査の自動化ポリシー定義で Initial 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Initial 機能の出力を取らず探索検査の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGKYST0I を含む表示を保存し、説明欄との差分を探索検査で確認する。 ✅
    - C. INGLIST を省略して探索検査の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では Initial 機能 は「探索検査の自動化ポリシー定義に関係する定義値と表示行を照合する探索検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では Initial 機能の属性行と INGKYST0I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では Initial 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索検査初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義



### Introducing the Customization Dialog {#c36-i1306}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Introducing the Customization Dialogは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.26) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 上書検査の自動化ポリシー定義で自動化管理の運用確認を行います。Introducing 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書検査の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書検査の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST の結果から対象行を抜き出し、上書検査の証跡として残す。 ✅
    - D. Introducing 機能の属性行を読まず上書検査の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では Introducing 機能 は「SA z/OS で Introducing 機能の扱いを記録する上書検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では Introducing 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では Introducing 機能の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.26) / OS 自動化ポリシー定義



### JOB DEFINITIONS Policy Item {#c36-i1307}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

JOB DEFINITIONS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 条件検査の自動化ポリシー定義に関係する JOB 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件検査の根拠にする。 ✅
    - B. JOB 機能の名称と担当者名のみを残して条件検査の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件検査の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件検査の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では JOB 機能 は「JOB 機能の用途を自動化管理の表示で確認する条件検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では SA z/OS の JOB 機能と INGKYST0I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では JOB 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### JOB/ASID DEFINITIONS Policy Item {#c36-i1308}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

JOB/ASID DEFINITIONS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 区切検査のJOB/ASID DEFINITIONS Policy Itemで JOB 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. JOB 属性の出力を取らず区切検査のJOB/ASID DEFINITIONS Policy Itemの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と INGKYST0I を読み、区切検査の結果として保存する。 ✅
    - C. INGLIST を省略して区切検査のJOB/ASID DEFINITIONS Policy Itemの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のJOB/ASID DEFINITIONS Policy Itemへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では JOB 属性 は「区切検査のJOB/ASID DEFINITIONS Policy Itemに関係する定義値と表示行を照合する区切検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では JOB 属性の属性行と INGKYST0I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では JOB 属性を Z System Automation (TSA)の運用手順で確認し、初出名は区切検査初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.218) / OS 自動化ポリシー定義



### LOCAL PAGE DATA SET Policy Item {#c36-i1309}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

LOCAL PAGE DATA SET Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 範囲検査の自動化ポリシー定義で自動化管理の運用確認を行います。LOCAL 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲検査の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲検査の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST で得た表示本文を使い、範囲検査の採否を説明欄に結び付ける。 ✅
    - D. LOCAL 機能の属性行を読まず範囲検査の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では LOCAL 機能 は「SA z/OS で LOCAL 機能の扱いを記録する範囲検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では LOCAL 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では LOCAL 機能の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### Logging Policy Database Modifications {#c36-i1310}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Logging Policy Database Modificationsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 優先検査の自動化ポリシー定義に関する Logging 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先検査の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Logging 機能の変更点を出力本文から切り離して優先検査の自動化ポリシー定義の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先検査として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では Logging 機能 は「Logging 機能の状態と出力メッセージを結び付ける優先検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では Logging 機能の出力行と INGKYST0I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では Logging 機能を SA z/OS の確認記録に残し、対象名は優先検査対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.45) / OS 自動化ポリシー定義



### MEMBER OF Policy Item {#c36-i1311}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

MEMBER OF Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.164) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 比較検査の自動化ポリシー定義で MEMBER 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MEMBER 機能の出力を取らず比較検査の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. SA z/OS の表示形式に沿って根拠行を採り、比較検査の点検結果を残す。 ✅
    - C. INGLIST を省略して比較検査の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では MEMBER 機能 は「比較検査の自動化ポリシー定義に関係する定義値と表示行を照合する比較検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では MEMBER 機能の属性行と INGKYST0I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では MEMBER 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較検査初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.164) / OS 自動化ポリシー定義


