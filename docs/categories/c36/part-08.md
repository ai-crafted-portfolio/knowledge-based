---
search:
  exclude: true
---

# Z System Automation (TSA) — 詳細 (8/12)

[← Z System Automation (TSA) の概要へ戻る](index.md)


## Z System Automation (TSA) > ユーザーズガイド

### Inform List concepts {#c36-i1012}
*分類: ユーザーズガイド*  ・  難易度: 上級

Inform List conceptsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 呼出検分のユーザーズガイドで自動化管理の運用確認を行います。Inform 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出検分のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出検分のユーザーズガイドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出検分の確認にする。 ✅
    - D. Inform 機能の属性行を読まず呼出検分のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では Inform 機能 は「SA z/OS で Inform 機能の扱いを記録する呼出検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では Inform 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では Inform 機能の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Interacting with the Automation Manager {#c36-i1013}
*分類: ユーザーズガイド*  ・  難易度: 上級

Interacting with the Automation Managerは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換検分のユーザーズガイドに関する Interacting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換検分のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検分のユーザーズガイドの証跡として保存して根拠にする。
    - C. Interacting 機能の変更点を出力本文から切り離して置換検分のユーザーズガイドの承認欄のみ残す。
    - D. SA z/OS の表示形式に沿って根拠行を採り、置換検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では Interacting 機能 は「Interacting 機能の状態と出力メッセージを結び付ける置換検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では Interacting 機能の出力行と INGKYST0I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明のみに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では Interacting 機能を SA z/OS の確認記録に残し、対象名は置換検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Introducing Service Management Unite Automation {#c36-i1014}
*分類: ユーザーズガイド*  ・  難易度: 上級

Introducing Service Management Unite Automationは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 終端検分のユーザーズガイドに関係する Introducing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検分で再確認できる形にする。 ✅
    - B. Introducing 機能の名称と担当者名のみを残して終端検分のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端検分のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端検分のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では Introducing 機能 は「Introducing 機能の用途を自動化管理の表示で確認する終端検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では SA z/OS の Introducing 機能と INGKYST0I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明のみに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では Introducing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Introducing Z System Automation {#c36-i1015}
*分類: ユーザーズガイド*  ・  難易度: 上級

Introducing Z System Automationは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 探索検分のユーザーズガイドで Introducing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Introducing 機能の出力を取らず探索検分のユーザーズガイドの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索検分の確認値として扱う。 ✅
    - C. INGLIST を省略して探索検分のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検分のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では Introducing 機能 は「探索検分のユーザーズガイドに関係する定義値と表示行を照合する探索検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では Introducing 機能の属性行と INGKYST0I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明のみに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では Introducing 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索検分初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Introduction and Concepts {#c36-i1016}
*分類: ユーザーズガイド*  ・  難易度: 上級

Introduction and Conceptsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書検分のユーザーズガイドで自動化管理の運用確認を行います。Introduction 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書検分のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書検分のユーザーズガイドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書検分の根拠を固定する。 ✅
    - D. Introduction 機能の属性行を読まず上書検分のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では Introduction 機能 は「SA z/OS で Introduction 機能の扱いを記録する上書検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では Introduction 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明のみに寄り、判定名は上書検分不足です。上書検分資料では Introduction 機能の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Issuing Commands {#c36-i1017}
*分類: ユーザーズガイド*  ・  難易度: 上級

Issuing Commandsは、Z System Automation (TSA)のユーザーズガイドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力検分のユーザーズガイドに関する Issuing Commandsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力検分のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分のユーザーズガイドの証跡として保存して根拠にする。
    - C. Issuing Commandsの変更点を出力本文から切り離して出力検分のユーザーズガイドの承認欄のみ残す。
    - D. INGKYST0I を含む表示を保存し、説明欄との差分を出力検分で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では Issuing Commands は「Issuing Commandsの状態と出力メッセージを結び付ける出力検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では Issuing Commandsの出力行と INGKYST0I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では Issuing Commandsを SA z/OS の確認記録に残し、対象名は出力検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Maintaining System Status during a Status Forwarding Path Failure {#c36-i1018}
*分類: ユーザーズガイド*  ・  難易度: 上級

Maintaining System Status during a Status Forwarding Path Failureは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件検分のユーザーズガイドに関係する Maintaining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGLIST の結果から対象行を抜き出し、条件検分の証跡として残す。 ✅
    - B. Maintaining 機能の名称と担当者名のみを残して条件検分のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件検分のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件検分のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Maintaining 機能 は「Maintaining 機能の用途を自動化管理の表示で確認する条件検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では SA z/OS の Maintaining 機能と INGKYST0I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明のみに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Maintaining 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Message Automation {#c36-i1019}
*分類: ユーザーズガイド*  ・  難易度: 上級

Message Automationは、Z System Automation (TSA)のユーザーズガイドでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide


### Monitoring and Controlling Logical Partitions and Guest Systems {#c36-i1020}
*分類: ユーザーズガイド*  ・  難易度: 上級

Monitoring and Controlling Logical Partitions and Guest Systemsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先検分のユーザーズガイドに関する Monitoring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先検分のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分のユーザーズガイドの証跡として保存して根拠にする。
    - C. Monitoring 機能の変更点を出力本文から切り離して優先検分のユーザーズガイドの承認欄のみ残す。
    - D. 同じ画面で対象行と INGKYST0I を読み、優先検分の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Monitoring 機能 は「Monitoring 機能の状態と出力メッセージを結び付ける優先検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Monitoring 機能の出力行と INGKYST0I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Monitoring 機能を SA z/OS の確認記録に残し、対象名は優先検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Monitoring and Controlling a Sysplex {#c36-i1021}
*分類: ユーザーズガイド*  ・  難易度: 上級

Monitoring and Controlling a Sysplexは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲検分のユーザーズガイドで自動化管理の運用確認を行います。Monitoring 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲検分のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲検分のユーザーズガイドを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲検分の根拠にする。 ✅
    - D. Monitoring 機能の属性行を読まず範囲検分のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では Monitoring 機能 は「SA z/OS で Monitoring 機能の扱いを記録する範囲検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では Monitoring 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明のみに寄り、判定名は範囲検分不足です。範囲検分資料では Monitoring 機能の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Monitoring for IPL Completion {#c36-i1022}
*分類: ユーザーズガイド*  ・  難易度: 上級

Monitoring for IPL Completionは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録検分のユーザーズガイドに関係する Monitoring 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGLIST で得た表示本文を使い、記録検分の採否を説明欄に結び付ける。 ✅
    - B. Monitoring 機能の名称と担当者名のみを残して記録検分のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録検分のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録検分のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Monitoring 機能 は「Monitoring 機能の用途を自動化管理の表示で確認する記録検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では SA z/OS の Monitoring 機能と INGKYST0I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Monitoring 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Monitoring of Resources {#c36-i1023}
*分類: ユーザーズガイド*  ・  難易度: 上級

Monitoring of Resourcesは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較検分のユーザーズガイドで Monitoring 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Monitoring 機能の出力を取らず比較検分のユーザーズガイドの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較検分として引き継ぐ。 ✅
    - C. INGLIST を省略して比較検分のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Monitoring 機能 は「比較検分のユーザーズガイドに関係する定義値と表示行を照合する比較検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Monitoring 機能の属性行と INGKYST0I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Monitoring 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Monitoring with the Status Display Facility {#c36-i1024}
*分類: ユーザーズガイド*  ・  難易度: 上級

Monitoring with the Status Display Facilityは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序検分のユーザーズガイドで自動化管理の運用確認を行います。Monitoring 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序検分のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序検分のユーザーズガイドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序検分の確認にする。 ✅
    - D. Monitoring 機能の属性行を読まず順序検分のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Monitoring 機能 は「SA z/OS で Monitoring 機能の扱いを記録する順序検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Monitoring 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Monitoring 機能の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Moving Sysplex Application Groups {#c36-i1025}
*分類: ユーザーズガイド*  ・  難易度: 上級

Moving Sysplex Application Groupsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 値域検分のユーザーズガイドに関する Moving 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域検分のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分のユーザーズガイドの証跡として保存して根拠にする。
    - C. Moving 機能の変更点を出力本文から切り離して値域検分のユーザーズガイドの承認欄のみ残す。
    - D. SA z/OS の表示形式に沿って根拠行を採り、値域検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Moving 機能 は「Moving 機能の状態と出力メッセージを結び付ける値域検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Moving 機能の出力行と INGKYST0I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Moving 機能を SA z/OS の確認記録に残し、対象名は値域検分対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Other Ways to Refresh Automation Policy {#c36-i1026}
*分類: ユーザーズガイド*  ・  難易度: 上級

Other Ways to Refresh Automation Policyは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告検分のユーザーズガイドに関係する Other 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告検分で再確認できる形にする。 ✅
    - B. Other 機能の名称と担当者名のみを残して警告検分のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告検分のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告検分のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Other 機能 は「Other 機能の用途を自動化管理の表示で確認する警告検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では SA z/OS の Other 機能と INGKYST0I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Other 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Overview {#c36-i1027}
*分類: ユーザーズガイド*  ・  難易度: 上級

Overviewは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Problem Determination {#c36-i1028}
*分類: ユーザーズガイド*  ・  難易度: 上級

Problem Determinationは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 監査検分のユーザーズガイドで自動化管理の運用確認を行います。Problem 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査検分のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査検分のユーザーズガイドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査検分の根拠を固定する。 ✅
    - D. Problem 機能の属性行を読まず監査検分のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Problem 機能 は「SA z/OS で Problem 機能の扱いを記録する監査検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Problem 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Problem 機能の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Processor Operations – setup for dynamic target system names {#c36-i1029}
*分類: ユーザーズガイド*  ・  難易度: 上級

Processor Operations – setup for dynamic target system namesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更検分の–に関する Processor 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更検分の–の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分の–の証跡として保存して根拠にする。
    - C. Processor 機能の変更点を出力本文から切り離して変更検分の–の承認欄のみ残す。
    - D. INGKYST0I を含む表示を保存し、説明欄との差分を変更検分で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Processor 機能 は「Processor 機能の状態と出力メッセージを結び付ける変更検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Processor 機能の出力行と INGKYST0I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Processor 機能を SA z/OS の確認記録に残し、対象名は変更検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Recovery of Processor Operations Target System Connections in the event of Hardware Management Console Outage {#c36-i1030}
*分類: ユーザーズガイド*  ・  難易度: 上級

Recovery of Processor Operations Target System Connections in the event of Hardware Management Console Outageは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Refreshing Automation Policy {#c36-i1031}
*分類: ユーザーズガイド*  ・  難易度: 上級

Refreshing Automation Policyは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 展開確認のユーザーズガイドで Refreshing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Refreshing 機能の出力を取らず展開確認のユーザーズガイドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開確認の確認にする。 ✅
    - C. INGLIST を省略して展開確認のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Refreshing 機能 は「展開確認のユーザーズガイドに関係する定義値と表示行を照合する展開確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Refreshing 機能の属性行と INGKYST0I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Refreshing 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開確認初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Refreshing Automation Policy using INGAMS command {#c36-i1032}
*分類: ユーザーズガイド*  ・  難易度: 上級

Refreshing Automation Policy using INGAMS commandは、Z System Automation (TSA)のユーザーズガイドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 呼出確認のユーザーズガイドで自動化管理の運用確認を行います。Refreshing 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出確認のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出確認のユーザーズガイドを正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、呼出確認の点検結果を残す。 ✅
    - D. Refreshing 機能の属性行を読まず呼出確認のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Refreshing 機能 は「SA z/OS で Refreshing 機能の扱いを記録する呼出確認項目」と INGAMS または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Refreshing 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Refreshing 機能の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Related Online Information {#c36-i1033}
*分類: ユーザーズガイド*  ・  難易度: 上級

Related Online Informationは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換確認のユーザーズガイドに関する Related 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換確認のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のユーザーズガイドの証跡として保存して根拠にする。
    - C. Related 機能の変更点を出力本文から切り離して置換確認のユーザーズガイドの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Related 機能 は「Related 機能の状態と出力メッセージを結び付ける置換確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Related 機能の出力行と INGKYST0I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Related 機能を SA z/OS の確認記録に残し、対象名は置換確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### SA z/OS Automation Flags {#c36-i1034}
*分類: ユーザーズガイド*  ・  難易度: 上級

SA z/OS Automation Flagsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 終端確認のSA z/OS Automation Flagsに関係する SA z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端確認の確認値として扱う。 ✅
    - B. SA z 属性の名称と担当者名のみを残して終端確認のSA z/OS Automation Flagsの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端確認のSA z/OS Automation Flagsを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端確認のSA z/OS Automation Flagsの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では SA z 属性 は「SA z 属性の用途を自動化管理の表示で確認する終端確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では SA z/OS の SA z 属性と INGKYST0I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では SA z 属性を Z System Automation (TSA)で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### SA-BCPii Use Cases {#c36-i1035}
*分類: ユーザーズガイド*  ・  難易度: 上級

SA-BCPii Use Casesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 探索確認のユーザーズガイドで SA-BCPii Use Casesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SA-BCPii Use Casesの出力を取らず探索確認のユーザーズガイドの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索確認の根拠を固定する。 ✅
    - C. INGLIST を省略して探索確認のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では SA-BCPii Use Cases は「探索確認のユーザーズガイドに関係する定義値と表示行を照合する探索確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では SA-BCPii Use Casesの属性行と INGKYST0I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では SA-BCPii Use Casesを Z System Automation (TSA)の運用手順で確認し、初出名は探索確認初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Setting Timers {#c36-i1036}
*分類: ユーザーズガイド*  ・  難易度: 上級

Setting Timersは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 上書確認のユーザーズガイドで自動化管理の運用確認を行います。Setting Timersの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書確認のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書確認のユーザーズガイドを正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を上書確認で確認する。 ✅
    - D. Setting Timersの属性行を読まず上書確認のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Setting Timers は「SA z/OS で Setting Timersの扱いを記録する上書確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Setting Timersの表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Setting Timersの使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Solving Problems with Resources {#c36-i1037}
*分類: ユーザーズガイド*  ・  難易度: 上級

Solving Problems with Resourcesは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 出力確認のユーザーズガイドに関する Solving 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力確認のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のユーザーズガイドの証跡として保存して根拠にする。
    - C. Solving 機能の変更点を出力本文から切り離して出力確認のユーザーズガイドの承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、出力確認の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では Solving 機能 は「Solving 機能の状態と出力メッセージを結び付ける出力確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では Solving 機能の出力行と INGKYST0I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では Solving 機能を SA z/OS の確認記録に残し、対象名は出力確認対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Starting and Stopping NetView {#c36-i1038}
*分類: ユーザーズガイド*  ・  難易度: 上級

Starting and Stopping NetViewは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件確認のユーザーズガイドに関係する Starting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件確認の確認記録にまとめる。 ✅
    - B. Starting 機能の名称と担当者名のみを残して条件確認のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件確認のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件確認のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では Starting 機能 は「Starting 機能の用途を自動化管理の表示で確認する条件確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では SA z/OS の Starting 機能と INGKYST0I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では Starting 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting and Stopping Processor Operations {#c36-i1039}
*分類: ユーザーズガイド*  ・  難易度: 上級

Starting and Stopping Processor Operationsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切確認のユーザーズガイドで Starting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Starting 機能の出力を取らず区切確認のユーザーズガイドの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切確認の根拠にする。 ✅
    - C. INGLIST を省略して区切確認のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Starting 機能 は「区切確認のユーザーズガイドに関係する定義値と表示行を照合する区切確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Starting 機能の属性行と INGKYST0I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Starting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting and Stopping SA z/OS {#c36-i1040}
*分類: ユーザーズガイド*  ・  難易度: 上級

Starting and Stopping SA z/OSは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲確認のユーザーズガイドで自動化管理の運用確認を行います。Starting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲確認のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲確認のユーザーズガイドを正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、範囲確認の結果として保存する。 ✅
    - D. Starting 機能の属性行を読まず範囲確認のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Starting 機能 は「SA z/OS で Starting 機能の扱いを記録する範囲確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Starting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Starting 機能の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting, Stopping and Suspending Resources {#c36-i1041}
*分類: ユーザーズガイド*  ・  難易度: 上級

Starting, Stopping and Suspending Resourcesは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先確認のユーザーズガイドに関する Starting 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先確認のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のユーザーズガイドの証跡として保存して根拠にする。
    - C. Starting 命令の変更点を出力本文から切り離して優先確認のユーザーズガイドの承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、優先確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Starting 命令 は「Starting 命令の状態と出力メッセージを結び付ける優先確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Starting 命令の出力行と INGKYST0I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Starting 命令を SA z/OS の確認記録に残し、対象名は優先確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Starting, Stopping, and Maintaining the Automation Manager {#c36-i1042}
*分類: ユーザーズガイド*  ・  難易度: 上級

Starting, Stopping, and Maintaining the Automation Managerは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録確認のユーザーズガイドに関係する Starting 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録確認として引き継ぐ。 ✅
    - B. Starting 命令の名称と担当者名のみを残して記録確認のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録確認のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録確認のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では Starting 命令 は「Starting 命令の用途を自動化管理の表示で確認する記録確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では SA z/OS の Starting 命令と INGKYST0I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では Starting 命令を Z System Automation (TSA)で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Statuses Supplied by the Automation Manager {#c36-i1043}
*分類: ユーザーズガイド*  ・  難易度: 上級

Statuses Supplied by the Automation Managerは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較確認のユーザーズガイドで Statuses 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Statuses 機能の出力を取らず比較確認のユーザーズガイドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較確認の確認にする。 ✅
    - C. INGLIST を省略して比較確認のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Statuses 機能 は「比較確認のユーザーズガイドに関係する定義値と表示行を照合する比較確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Statuses 機能の属性行と INGKYST0I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Statuses 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Suspend and Resume Functionality {#c36-i1044}
*分類: ユーザーズガイド*  ・  難易度: 上級

Suspend and Resume Functionalityは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 順序確認のユーザーズガイドで自動化管理の運用確認を行います。Suspend 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序確認のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序確認のユーザーズガイドを正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、順序確認の点検結果を残す。 ✅
    - D. Suspend 機能の属性行を読まず順序確認のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Suspend 機能 は「SA z/OS で Suspend 機能の扱いを記録する順序確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Suspend 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Suspend 機能の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### System Automation Info Broker {#c36-i1045}
*分類: ユーザーズガイド*  ・  難易度: 上級

System Automation Info Brokerは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 値域確認のユーザーズガイドに関する System 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域確認のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のユーザーズガイドの証跡として保存して根拠にする。
    - C. System 機能の変更点を出力本文から切り離して値域確認のユーザーズガイドの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では System 機能 は「System 機能の状態と出力メッセージを結び付ける値域確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では System 機能の出力行と INGKYST0I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では System 機能を SA z/OS の確認記録に残し、対象名は値域確認対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Tracing and Debugging for ProcOps and the BCP Internal Interface {#c36-i1046}
*分類: ユーザーズガイド*  ・  難易度: 上級

Tracing and Debugging for ProcOps and the BCP Internal Interfaceは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告確認のユーザーズガイドに関係する Tracing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告確認の確認値として扱う。 ✅
    - B. Tracing 機能の名称と担当者名のみを残して警告確認のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告確認のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告確認のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Tracing 機能 は「Tracing 機能の用途を自動化管理の表示で確認する警告確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では SA z/OS の Tracing 機能と INGKYST0I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Tracing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Use Case: GDPS is managing your mainframes {#c36-i1047}
*分類: ユーザーズガイド*  ・  難易度: 上級

Use Case: GDPS is managing your mainframesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 復旧確認の:で Use 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Use 機能の出力を取らず復旧確認の:の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧確認の根拠を固定する。 ✅
    - C. INGLIST を省略して復旧確認の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Use 機能 は「復旧確認の:に関係する定義値と表示行を照合する復旧確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Use 機能の属性行と INGKYST0I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Use 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Use Case: Monitoring the Hardware Management Consoles {#c36-i1048}
*分類: ユーザーズガイド*  ・  難易度: 上級

Use Case: Monitoring the Hardware Management Consolesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査確認の:で自動化管理の運用確認を行います。Use 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査確認の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査確認の:を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を監査確認で確認する。 ✅
    - D. Use 機能の属性行を読まず監査確認の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Use 機能 は「SA z/OS で Use 機能の扱いを記録する監査確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Use 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Use 機能の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Use Case: Options to limit the number of SA-BCPii connections {#c36-i1049}
*分類: ユーザーズガイド*  ・  難易度: 上級

Use Case: Options to limit the number of SA-BCPii connectionsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更確認の:に関する Use 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更確認の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の:の証跡として保存して根拠にする。
    - C. Use 機能の変更点を出力本文から切り離して変更確認の:の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、変更確認の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Use 機能 は「Use 機能の状態と出力メッセージを結び付ける変更確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Use 機能の出力行と INGKYST0I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Use 機能を SA z/OS の確認記録に残し、対象名は変更確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Use Case: ProcOps over SA-BCPii is managing your mainframes {#c36-i1050}
*分類: ユーザーズガイド*  ・  難易度: 上級

Use Case: ProcOps over SA-BCPii is managing your mainframesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Users Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Users Guide

??? question "確認問題（1問）"
    **問題.** 構文照合の:に関係する Use 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文照合の確認記録にまとめる。 ✅
    - B. Use 機能の名称と担当者名のみを残して構文照合の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文照合の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文照合の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Use 機能 は「Use 機能の用途を自動化管理の表示で確認する構文照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では SA z/OS の Use 機能と INGKYST0I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Use 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Use Case: Working with GDPS and ProcOps {#c36-i1051}
*分類: ユーザーズガイド*  ・  難易度: 上級

Use Case: Working with GDPS and ProcOpsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開照合の:で Use 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Use 機能の出力を取らず展開照合の:の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開照合の根拠にする。 ✅
    - C. INGLIST を省略して展開照合の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では Use 機能 は「展開照合の:に関係する定義値と表示行を照合する展開照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では Use 機能の属性行と INGKYST0I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では Use 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using AOCTRACE {#c36-i1052}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using AOCTRACEは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出照合のユーザーズガイドで自動化管理の運用確認を行います。Using AOCTRACE の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出照合のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出照合のユーザーズガイドを正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、呼出照合の結果として保存する。 ✅
    - D. Using AOCTRACE の属性行を読まず呼出照合のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では Using AOCTRACE は「SA z/OS で Using AOCTRACE の扱いを記録する呼出照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では Using AOCTRACE の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では Using AOCTRACE の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using Command Dialogs {#c36-i1053}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using Command Dialogsは、Z System Automation (TSA)のユーザーズガイドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換照合のユーザーズガイドに関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換照合のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のユーザーズガイドの証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して置換照合のユーザーズガイドの承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、置換照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける置換照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では Using 機能の出力行と INGKYST0I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では Using 機能を SA z/OS の確認記録に残し、対象名は置換照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using DISPINFO to Display Detailed Information {#c36-i1054}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using DISPINFO to Display Detailed Informationは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端照合のユーザーズガイドに関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端照合として引き継ぐ。 ✅
    - B. Using 機能の名称と担当者名のみを残して終端照合のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端照合のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端照合のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では Using 機能 は「Using 機能の用途を自動化管理の表示で確認する終端照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では SA z/OS の Using 機能と INGKYST0I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では Using 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using DISPTREE to Display Dependency Information {#c36-i1055}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using DISPTREE to Display Dependency Informationは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索照合のユーザーズガイドで Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず探索照合のユーザーズガイドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索照合の確認にする。 ✅
    - C. INGLIST を省略して探索照合のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では Using 機能 は「探索照合のユーザーズガイドに関係する定義値と表示行を照合する探索照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では Using 機能の属性行と INGKYST0I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では Using 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using INGINFO to View a Selected Resource {#c36-i1056}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using INGINFO to View a Selected Resourceは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書照合のユーザーズガイドで自動化管理の運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書照合のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書照合のユーザーズガイドを正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、上書照合の点検結果を残す。 ✅
    - D. Using 機能の属性行を読まず上書照合のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では Using 機能 は「SA z/OS で Using 機能の扱いを記録する上書照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では Using 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では Using 機能の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using INGLIST to View Resources {#c36-i1057}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using INGLIST to View Resourcesは、Z System Automation (TSA)のユーザーズガイドでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力照合のユーザーズガイドに関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力照合のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のユーザーズガイドの証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して出力照合のユーザーズガイドの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける出力照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では Using 機能の出力行と INGKYST0I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では Using 機能を SA z/OS の確認記録に残し、対象名は出力照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using Runmodes {#c36-i1058}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using Runmodesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件照合のユーザーズガイドに関係する Using Runmodesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件照合の確認値として扱う。 ✅
    - B. Using Runmodesの名称と担当者名のみを残して条件照合のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件照合のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件照合のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では Using Runmodes は「Using Runmodesの用途を自動化管理の表示で確認する条件照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では SA z/OS の Using Runmodesと INGKYST0I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では Using Runmodesを Z System Automation (TSA)で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using SA z/OS for Monitoring {#c36-i1059}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using SA z/OS for Monitoringは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切照合のUsing SA z/OS for Monitoringで Using SA z 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using SA z 属性の出力を取らず区切照合のUsing SA z/OS for Monitoringの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切照合の根拠を固定する。 ✅
    - C. INGLIST を省略して区切照合のUsing SA z/OS for Monitoringの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のUsing SA z/OS for Monitoringへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では Using SA z 属性 は「区切照合のUsing SA z/OS for Monitoringに関係する定義値と表示行を照合する区切照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では Using SA z 属性の属性行と INGKYST0I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では Using SA z 属性を Z System Automation (TSA)の運用手順で確認し、初出名は区切照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using SA z/OS on the Host {#c36-i1060}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using SA z/OS on the Hostは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲照合のUsing SA z/OS on the Hostで自動化管理の運用確認を行います。Using SA z 属性の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲照合のUsing SA z/OS on the Hostを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲照合のUsing SA z/OS on the Hostを正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を範囲照合で確認する。 ✅
    - D. Using SA z 属性の属性行を読まず範囲照合のUsing SA z/OS on the Hostの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では Using SA z 属性 は「SA z/OS で Using SA z 属性の扱いを記録する範囲照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では Using SA z 属性の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では Using SA z 属性の使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using Schedules {#c36-i1061}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using Schedulesは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先照合のユーザーズガイドに関する Using Schedulesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先照合のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のユーザーズガイドの証跡として保存して根拠にする。
    - C. Using Schedulesの変更点を出力本文から切り離して優先照合のユーザーズガイドの承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、優先照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では Using Schedules は「Using Schedulesの状態と出力メッセージを結び付ける優先照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では Using Schedulesの出力行と INGKYST0I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では Using Schedulesを SA z/OS の確認記録に残し、対象名は優先照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using Trace Services for the Automation Manager and Agent {#c36-i1062}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using Trace Services for the Automation Manager and Agentは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序照合のユーザーズガイドで自動化管理の運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序照合のユーザーズガイドを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序照合のユーザーズガイドを正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、順序照合の結果として保存する。 ✅
    - D. Using 機能の属性行を読まず順序照合のユーザーズガイドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では Using 機能 は「SA z/OS で Using 機能の扱いを記録する順序照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では Using 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では Using 機能の使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using UP Status Delay {#c36-i1063}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using UP Status Delayは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域照合のユーザーズガイドに関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域照合のユーザーズガイドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のユーザーズガイドの証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して値域照合のユーザーズガイドの承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、値域照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける値域照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では Using 機能の出力行と INGKYST0I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では Using 機能を SA z/OS の確認記録に残し、対象名は値域照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using the ProcOps HOLD Session Mode {#c36-i1064}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using the ProcOps HOLD Session Modeは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録照合のユーザーズガイドに関係する Using 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録照合の確認記録にまとめる。 ✅
    - B. Using 機能の名称と担当者名のみを残して記録照合のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録照合のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録照合のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では Using 機能 は「Using 機能の用途を自動化管理の表示で確認する記録照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では SA z/OS の Using 機能と INGKYST0I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では Using 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using the Suspend File {#c36-i1065}
*分類: ユーザーズガイド*  ・  難易度: 上級

Using the Suspend Fileは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較照合のユーザーズガイドで Using 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using 機能の出力を取らず比較照合のユーザーズガイドの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較照合の根拠にする。 ✅
    - C. INGLIST を省略して比較照合のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では Using 機能 は「比較照合のユーザーズガイドに関係する定義値と表示行を照合する比較照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では Using 機能の属性行と INGKYST0I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では Using 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Working with Application Groups {#c36-i1066}
*分類: ユーザーズガイド*  ・  難易度: 上級

Working with Application Groupsは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告照合のユーザーズガイドに関係する Working 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告照合として引き継ぐ。 ✅
    - B. Working 機能の名称と担当者名のみを残して警告照合のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告照合のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告照合のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では Working 機能 は「Working 機能の用途を自動化管理の表示で確認する警告照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では SA z/OS の Working 機能と INGKYST0I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では Working 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Working with the Looping Address Space Monitor {#c36-i1067}
*分類: ユーザーズガイド*  ・  難易度: 上級

Working with the Looping Address Space Monitorは、Z System Automation (TSA)のユーザーズガイドで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧照合のユーザーズガイドで Working 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Working 機能の出力を取らず復旧照合のユーザーズガイドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧照合の確認にする。 ✅
    - C. INGLIST を省略して復旧照合のユーザーズガイドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のユーザーズガイドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では Working 機能 は「復旧照合のユーザーズガイドに関係する定義値と表示行を照合する復旧照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では Working 機能の属性行と INGKYST0I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では Working 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 概要 / 開始

### A new policy database {#c36-i1068}
*分類: 概要 / 開始*  ・  難易度: 上級

A new policy databaseは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 監査照合の概要 開始で自動化管理の運用確認を行います。A 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査照合の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査照合の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、監査照合の点検結果を残す。 ✅
    - D. A 機能の属性行を読まず監査照合の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では A 機能 は「SA z/OS で A 機能の扱いを記録する監査照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では A 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では A 機能の使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Adapt the sample policies {#c36-i1069}
*分類: 概要 / 開始*  ・  難易度: 上級

Adapt the sample policiesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 変更照合の概要 開始に関する Adapt 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更照合の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の概要 開始の証跡として保存して根拠にする。
    - C. Adapt 機能の変更点を出力本文から切り離して変更照合の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では Adapt 機能 は「Adapt 機能の状態と出力メッセージを結び付ける変更照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では Adapt 機能の出力行と INGKYST0I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では Adapt 機能を SA z/OS の確認記録に残し、対象名は変更照合対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Adapting Application Job Names {#c36-i1070}
*分類: 概要 / 開始*  ・  難易度: 上級

Adapting Application Job Namesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 構文追跡の概要 開始に関係する Adapting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文追跡の確認値として扱う。 ✅
    - B. Adapting 機能の名称と担当者名のみを残して構文追跡の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文追跡の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文追跡の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では Adapting 機能 は「Adapting 機能の用途を自動化管理の表示で確認する構文追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では SA z/OS の Adapting 機能と INGKYST0I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では Adapting 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Adapting the System Name {#c36-i1071}
*分類: 概要 / 開始*  ・  難易度: 上級

Adapting the System Nameは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 展開追跡の概要 開始で Adapting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Adapting 機能の出力を取らず展開追跡の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開追跡の根拠を固定する。 ✅
    - C. INGLIST を省略して展開追跡の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では Adapting 機能 は「展開追跡の概要 開始に関係する定義値と表示行を照合する展開追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では Adapting 機能の属性行と INGKYST0I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では Adapting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Adding applications {#c36-i1072}
*分類: 概要 / 開始*  ・  難易度: 上級

Adding applicationsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出追跡の概要 開始で自動化管理の運用確認を行います。Adding 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出追跡の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出追跡の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を呼出追跡で確認する。 ✅
    - D. Adding 機能の属性行を読まず呼出追跡の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では Adding 機能 は「SA z/OS で Adding 機能の扱いを記録する呼出追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では Adding 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では Adding 機能の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Adding more systems {#c36-i1073}
*分類: 概要 / 開始*  ・  難易度: 上級

Adding more systemsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換追跡の概要 開始に関する Adding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換追跡の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の概要 開始の証跡として保存して根拠にする。
    - C. Adding 機能の変更点を出力本文から切り離して置換追跡の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、置換追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では Adding 機能 は「Adding 機能の状態と出力メッセージを結び付ける置換追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では Adding 機能の出力行と INGKYST0I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では Adding 機能を SA z/OS の確認記録に残し、対象名は置換追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Adding sample policies {#c36-i1074}
*分類: 概要 / 開始*  ・  難易度: 上級

Adding sample policiesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端追跡の概要 開始に関係する Adding 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端追跡の確認記録にまとめる。 ✅
    - B. Adding 機能の名称と担当者名のみを残して終端追跡の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端追跡の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端追跡の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では Adding 機能 は「Adding 機能の用途を自動化管理の表示で確認する終端追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では SA z/OS の Adding 機能と INGKYST0I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では Adding 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Additional configuration considerations {#c36-i1075}
*分類: 概要 / 開始*  ・  難易度: 上級

Additional configuration considerationsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 探索追跡の概要 開始で Additional 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Additional 機能の出力を取らず探索追跡の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索追跡の根拠にする。 ✅
    - C. INGLIST を省略して探索追跡の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では Additional 機能 は「探索追跡の概要 開始に関係する定義値と表示行を照合する探索追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では Additional 機能の属性行と INGKYST0I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では Additional 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Additional deployment plans {#c36-i1076}
*分類: 概要 / 開始*  ・  難易度: 上級

Additional deployment plansは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 上書追跡の概要 開始で自動化管理の運用確認を行います。Additional 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書追跡の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書追跡の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、上書追跡の結果として保存する。 ✅
    - D. Additional 機能の属性行を読まず上書追跡の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では Additional 機能 は「SA z/OS で Additional 機能の扱いを記録する上書追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では Additional 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では Additional 機能の使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Application Groups {#c36-i1077}
*分類: 概要 / 開始*  ・  難易度: 上級

Application Groupsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 出力追跡の概要 開始に関する Application Groupsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力追跡の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の概要 開始の証跡として保存して根拠にする。
    - C. Application Groupsの変更点を出力本文から切り離して出力追跡の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、出力追跡の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では Application Groups は「Application Groupsの状態と出力メッセージを結び付ける出力追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では Application Groupsの出力行と INGKYST0I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では Application Groupsを SA z/OS の確認記録に残し、対象名は出力追跡対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Automation Manager and Automation Agent {#c36-i1078}
*分類: 概要 / 開始*  ・  難易度: 上級

Automation Manager and Automation Agentは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件追跡の概要 開始に関係する Automation 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件追跡として引き継ぐ。 ✅
    - B. Automation 機能の名称と担当者名のみを残して条件追跡の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件追跡の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件追跡の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では Automation 機能 は「Automation 機能の用途を自動化管理の表示で確認する条件追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では SA z/OS の Automation 機能と INGKYST0I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では Automation 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Automation policy management {#c36-i1079}
*分類: 概要 / 開始*  ・  難易度: 上級

Automation policy managementは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 区切追跡の概要 開始で Automation 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Automation 機能の出力を取らず区切追跡の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切追跡の確認にする。 ✅
    - C. INGLIST を省略して区切追跡の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では Automation 機能 は「区切追跡の概要 開始に関係する定義値と表示行を照合する区切追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では Automation 機能の属性行と INGKYST0I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では Automation 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Building a minimal automation policy {#c36-i1080}
*分類: 概要 / 開始*  ・  難易度: 上級

Building a minimal automation policyは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲追跡の概要 開始で自動化管理の運用確認を行います。Building 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲追跡の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲追跡の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、範囲追跡の点検結果を残す。 ✅
    - D. Building 機能の属性行を読まず範囲追跡の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では Building 機能 は「SA z/OS で Building 機能の扱いを記録する範囲追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では Building 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では Building 機能の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Building blocks {#c36-i1081}
*分類: 概要 / 開始*  ・  難易度: 上級

Building blocksは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先追跡の概要 開始に関する Building blocksの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先追跡の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の概要 開始の証跡として保存して根拠にする。
    - C. Building blocksの変更点を出力本文から切り離して優先追跡の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先追跡で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では Building blocks は「Building blocksの状態と出力メッセージを結び付ける優先追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では Building blocksの出力行と INGKYST0I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では Building blocksを SA z/OS の確認記録に残し、対象名は優先追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Building the Configuration Files {#c36-i1082}
*分類: 概要 / 開始*  ・  難易度: 上級

Building the Configuration Filesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（2問）"
    **問題.** 記録追跡の概要 開始に関係する Building 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録追跡の確認値として扱う。 ✅
    - B. Building 機能の名称と担当者名のみを残して記録追跡の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録追跡の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録追跡の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では Building 機能 は「Building 機能の用途を自動化管理の表示で確認する記録追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では SA z/OS の Building 機能と INGKYST0I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では Building 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 優先読解の自動化ポリシー定義に関する Building 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先読解の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Building 機能の変更点を出力本文から切り離して優先読解の自動化ポリシー定義の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では Building 機能 は「Building 機能の状態と出力メッセージを結び付ける優先読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では Building 機能の出力行と INGKYST0I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では Building 機能を SA z/OS の確認記録に残し、対象名は優先読解対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Building your policy {#c36-i1083}
*分類: 概要 / 開始*  ・  難易度: 上級

Building your policyは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較追跡の概要 開始で Building 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Building 機能の出力を取らず比較追跡の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較追跡の根拠を固定する。 ✅
    - C. INGLIST を省略して比較追跡の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では Building 機能 は「比較追跡の概要 開始に関係する定義値と表示行を照合する比較追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では Building 機能の属性行と INGKYST0I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では Building 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Bulk update {#c36-i1084}
*分類: 概要 / 開始*  ・  難易度: 上級

Bulk updateは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 順序追跡の概要 開始で自動化管理の運用確認を行います。Bulk updateの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序追跡の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序追跡の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を順序追跡で確認する。 ✅
    - D. Bulk updateの属性行を読まず順序追跡の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では Bulk update は「SA z/OS で Bulk updateの扱いを記録する順序追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では Bulk updateの表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では Bulk updateの使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### CNMSTYLE Customization {#c36-i1085}
*分類: 概要 / 開始*  ・  難易度: 上級

CNMSTYLE Customizationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更追跡の概要 開始に関する CNMSTYLE 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更追跡の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡の概要 開始の証跡として保存して根拠にする。
    - C. CNMSTYLE 機能の変更点を出力本文から切り離して変更追跡の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、変更追跡の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では CNMSTYLE 機能 は「CNMSTYLE 機能の状態と出力メッセージを結び付ける変更追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では CNMSTYLE 機能の出力行と INGKYST0I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では CNMSTYLE 機能を SA z/OS の確認記録に残し、対象名は変更追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Changing System Defaults {#c36-i1086}
*分類: 概要 / 開始*  ・  難易度: 上級

Changing System Defaultsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 警告追跡の概要 開始に関係する Changing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告追跡の確認記録にまとめる。 ✅
    - B. Changing 機能の名称と担当者名のみを残して警告追跡の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告追跡の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告追跡の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では Changing 機能 は「Changing 機能の用途を自動化管理の表示で確認する警告追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では SA z/OS の Changing 機能と INGKYST0I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では Changing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Changing symbolic variables {#c36-i1087}
*分類: 概要 / 開始*  ・  難易度: 上級

Changing symbolic variablesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 値域追跡の概要 開始に関する Changing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域追跡の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡の概要 開始の証跡として保存して根拠にする。
    - C. Changing 機能の変更点を出力本文から切り離して値域追跡の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、値域追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では Changing 機能 は「Changing 機能の状態と出力メッセージを結び付ける値域追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では Changing 機能の出力行と INGKYST0I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では Changing 機能を SA z/OS の確認記録に残し、対象名は値域追跡対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Cloning definitions {#c36-i1088}
*分類: 概要 / 開始*  ・  難易度: 上級

Cloning definitionsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 復旧追跡の概要 開始で Cloning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Cloning 機能の出力を取らず復旧追跡の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧追跡の根拠にする。 ✅
    - C. INGLIST を省略して復旧追跡の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では Cloning 機能 は「復旧追跡の概要 開始に関係する定義値と表示行を照合する復旧追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では Cloning 機能の属性行と INGKYST0I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では Cloning 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Cloning with symbolic values {#c36-i1089}
*分類: 概要 / 開始*  ・  難易度: 上級

Cloning with symbolic valuesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 監査追跡の概要 開始で自動化管理の運用確認を行います。Cloning 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査追跡の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査追跡の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、監査追跡の結果として保存する。 ✅
    - D. Cloning 機能の属性行を読まず監査追跡の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では Cloning 機能 は「SA z/OS で Cloning 機能の扱いを記録する監査追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では Cloning 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では Cloning 機能の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Complete the replication {#c36-i1090}
*分類: 概要 / 開始*  ・  難易度: 上級

Complete the replicationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 構文検査の概要 開始に関係する Complete 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文検査として引き継ぐ。 ✅
    - B. Complete 機能の名称と担当者名のみを残して構文検査の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文検査の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文検査の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では Complete 機能 は「Complete 機能の用途を自動化管理の表示で確認する構文検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では SA z/OS の Complete 機能と INGKYST0I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では Complete 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Components {#c36-i1091}
*分類: 概要 / 開始*  ・  難易度: 上級

Componentsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 展開検査の概要 開始で Componentsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Componentsの出力を取らず展開検査の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検査の確認にする。 ✅
    - C. INGLIST を省略して展開検査の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では Components は「展開検査の概要 開始に関係する定義値と表示行を照合する展開検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では Componentsの属性行と INGKYST0I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では Componentsを Z System Automation (TSA)の運用手順で確認し、初出名は展開検査初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Configuring SA z/OS {#c36-i1092}
*分類: 概要 / 開始*  ・  難易度: 上級

Configuring SA z/OSは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出検査のConfiguring SA z/OSで自動化管理の運用確認を行います。Configuring SA z 属性の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出検査のConfiguring SA z/OSを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出検査のConfiguring SA z/OSを正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、呼出検査の点検結果を残す。 ✅
    - D. Configuring SA z 属性の属性行を読まず呼出検査のConfiguring SA z/OSの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では Configuring SA z 属性 は「SA z/OS で Configuring SA z 属性の扱いを記録する呼出検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では Configuring SA z 属性の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では Configuring SA z 属性の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Configuring the operator environment {#c36-i1093}
*分類: 概要 / 開始*  ・  難易度: 上級

Configuring the operator environmentは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換検査の概要 開始に関する Configuring 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換検査の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の概要 開始の証跡として保存して根拠にする。
    - C. Configuring 機能の変更点を出力本文から切り離して置換検査の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検査で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では Configuring 機能 は「Configuring 機能の状態と出力メッセージを結び付ける置換検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では Configuring 機能の出力行と INGKYST0I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では Configuring 機能を SA z/OS の確認記録に残し、対象名は置換検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Configuring the target systems {#c36-i1094}
*分類: 概要 / 開始*  ・  難易度: 上級

Configuring the target systemsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端検査の概要 開始に関係する Configuring 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端検査の確認値として扱う。 ✅
    - B. Configuring 機能の名称と担当者名のみを残して終端検査の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端検査の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端検査の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Configuring 機能 は「Configuring 機能の用途を自動化管理の表示で確認する終端検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では SA z/OS の Configuring 機能と INGKYST0I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Configuring 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Connectivity and Functionality at a Glance {#c36-i1095}
*分類: 概要 / 開始*  ・  難易度: 上級

Connectivity and Functionality at a Glanceは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索検査の概要 開始で Connectivity 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Connectivity 機能の出力を取らず探索検査の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索検査の根拠を固定する。 ✅
    - C. INGLIST を省略して探索検査の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では Connectivity 機能 は「探索検査の概要 開始に関係する定義値と表示行を照合する探索検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では Connectivity 機能の属性行と INGKYST0I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では Connectivity 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Console operations {#c36-i1096}
*分類: 概要 / 開始*  ・  難易度: 上級

Console operationsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 上書検査の概要 開始で自動化管理の運用確認を行います。Console operationsの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書検査の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書検査の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を上書検査で確認する。 ✅
    - D. Console operationsの属性行を読まず上書検査の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では Console operations は「SA z/OS で Console operationsの扱いを記録する上書検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では Console operationsの表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では Console operationsの使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a Group {#c36-i1097}
*分類: 概要 / 開始*  ・  難易度: 上級

Creating a Groupは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件検査の概要 開始に関係する Creating a Groupの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件検査の確認記録にまとめる。 ✅
    - B. Creating a Groupの名称と担当者名のみを残して条件検査の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件検査の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件検査の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では Creating a Group は「Creating a Groupの用途を自動化管理の表示で確認する条件検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では SA z/OS の Creating a Groupと INGKYST0I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では Creating a Groupを Z System Automation (TSA)で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a System {#c36-i1098}
*分類: 概要 / 開始*  ・  難易度: 上級

Creating a Systemは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲検査の概要 開始で自動化管理の運用確認を行います。Creating a Systemの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲検査の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲検査の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、範囲検査の結果として保存する。 ✅
    - D. Creating a Systemの属性行を読まず範囲検査の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では Creating a System は「SA z/OS で Creating a Systemの扱いを記録する範囲検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では Creating a Systemの表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では Creating a Systemの使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a basic PDB {#c36-i1099}
*分類: 概要 / 開始*  ・  難易度: 上級

Creating a basic PDBは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力検査の概要 開始に関する Creating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力検査の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の概要 開始の証跡として保存して根拠にする。
    - C. Creating 機能の変更点を出力本文から切り離して出力検査の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、出力検査の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では Creating 機能 は「Creating 機能の状態と出力メッセージを結び付ける出力検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では Creating 機能の出力行と INGKYST0I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では Creating 機能を SA z/OS の確認記録に残し、対象名は出力検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Creating a new policy database {#c36-i1100}
*分類: 概要 / 開始*  ・  難易度: 上級

Creating a new policy databaseは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（2問）"
    **問題.** 区切検査の概要 開始で Creating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Creating 機能の出力を取らず区切検査の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検査の根拠にする。 ✅
    - C. INGLIST を省略して区切検査の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では Creating 機能 は「区切検査の概要 開始に関係する定義値と表示行を照合する区切検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では Creating 機能の属性行と INGKYST0I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では Creating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 警告検分の自動化ポリシー定義に関係する Creating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告検分の確認値として扱う。 ✅
    - B. Creating 機能の名称と担当者名のみを残して警告検分の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告検分の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告検分の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Creating 機能 は「Creating 機能の用途を自動化管理の表示で確認する警告検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では SA z/OS の Creating 機能と INGKYST0I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Creating 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告検分用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Customization {#c36-i1101}
*分類: 概要 / 開始*  ・  難易度: 上級

Customizationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Customization Dialog tutorial {#c36-i1102}
*分類: 概要 / 開始*  ・  難易度: 上級

Customization Dialog tutorialは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 記録検査の概要 開始に関係する Customization 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録検査として引き継ぐ。 ✅
    - B. Customization 機能の名称と担当者名のみを残して記録検査の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録検査の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録検査の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では Customization 機能 は「Customization 機能の用途を自動化管理の表示で確認する記録検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では SA z/OS の Customization 機能と INGKYST0I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では Customization 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Customization tools {#c36-i1103}
*分類: 概要 / 開始*  ・  難易度: 上級

Customization toolsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 比較検査の概要 開始で Customization 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Customization 機能の出力を取らず比較検査の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較検査の確認にする。 ✅
    - C. INGLIST を省略して比較検査の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では Customization 機能 は「比較検査の概要 開始に関係する定義値と表示行を照合する比較検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では Customization 機能の属性行と INGKYST0I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では Customization 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較検査初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Defaults, classes, and inheritance {#c36-i1104}
*分類: 概要 / 開始*  ・  難易度: 上級

Defaults, classes, and inheritanceは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 順序検査の概要 開始で自動化管理の運用確認を行います。Defaults 命令の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序検査の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序検査の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、順序検査の点検結果を残す。 ✅
    - D. Defaults 命令の属性行を読まず順序検査の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Defaults 命令 は「SA z/OS で Defaults 命令の扱いを記録する順序検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Defaults 命令の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Defaults 命令の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Deploying SA z/OS {#c36-i1105}
*分類: 概要 / 開始*  ・  難易度: 上級

Deploying SA z/OSは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 値域検査のDeploying SA z/OSに関する Deploying SA z・ OS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域検査のDeploying SA z/OSの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のDeploying SA z/OSの証跡として保存して根拠にする。
    - C. Deploying SA z・ OS の変更点を出力本文から切り離して値域検査のDeploying SA z/OSの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検査で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では Deploying SA z・ OS は「Deploying SA z・ OS の状態と出力メッセージを結び付ける値域検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では Deploying SA z・ OS の出力行と INGKYST0I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では Deploying SA z・ OS を SA z/OS の確認記録に残し、対象名は値域検査対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Distributing your policy {#c36-i1106}
*分類: 概要 / 開始*  ・  難易度: 上級

Distributing your policyは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 警告検査の概要 開始に関係する Distributing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告検査の確認値として扱う。 ✅
    - B. Distributing 機能の名称と担当者名のみを残して警告検査の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告検査の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告検査の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では Distributing 機能 は「Distributing 機能の用途を自動化管理の表示で確認する警告検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では SA z/OS の Distributing 機能と INGKYST0I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では Distributing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Enabling INTERNAL Communication {#c36-i1107}
*分類: 概要 / 開始*  ・  難易度: 上級

Enabling INTERNAL Communicationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧検査の概要 開始で Enabling 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Enabling 機能の出力を取らず復旧検査の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧検査の根拠を固定する。 ✅
    - C. INGLIST を省略して復旧検査の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では Enabling 機能 は「復旧検査の概要 開始に関係する定義値と表示行を照合する復旧検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では Enabling 機能の属性行と INGKYST0I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では Enabling 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Establishing naming conventions {#c36-i1108}
*分類: 概要 / 開始*  ・  難易度: 上級

Establishing naming conventionsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 監査検査の概要 開始で自動化管理の運用確認を行います。Establishing 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査検査の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査検査の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を監査検査で確認する。 ✅
    - D. Establishing 機能の属性行を読まず監査検査の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では Establishing 機能 は「SA z/OS で Establishing 機能の扱いを記録する監査検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では Establishing 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では Establishing 機能の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Expanding and maintaining your automation policy {#c36-i1109}
*分類: 概要 / 開始*  ・  難易度: 上級

Expanding and maintaining your automation policyは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更検査の概要 開始に関する Expanding 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更検査の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の概要 開始の証跡として保存して根拠にする。
    - C. Expanding 機能の変更点を出力本文から切り離して変更検査の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、変更検査の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では Expanding 機能 は「Expanding 機能の状態と出力メッセージを結び付ける変更検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では Expanding 機能の出力行と INGKYST0I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では Expanding 機能を SA z/OS の確認記録に残し、対象名は変更検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Getting help {#c36-i1110}
*分類: 概要 / 開始*  ・  難易度: 上級

Getting helpは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（2問）"
    **問題.** 構文判定の概要 開始に関係する Getting helpの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文判定の確認記録にまとめる。 ✅
    - B. Getting helpの名称と担当者名のみを残して構文判定の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文判定の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文判定の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では Getting help は「Getting helpの用途を自動化管理の表示で確認する構文判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では SA z/OS の Getting helpと INGKYST0I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では Getting helpを Z System Automation (TSA)で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 範囲照合の自動化ポリシー定義で自動化管理の運用確認を行います。Getting Helpの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲照合の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲照合の自動化ポリシー定義を正常終了として記録する。
    - C. INGLIST の結果から対象行を抜き出し、範囲照合の証跡として残す。 ✅
    - D. Getting Helpの属性行を読まず範囲照合の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では Getting Help は「SA z/OS で Getting Helpの扱いを記録する範囲照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では Getting Helpの表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では Getting Helpの使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Goal driven automation {#c36-i1111}
*分類: 概要 / 開始*  ・  難易度: 上級

Goal driven automationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 展開判定の概要 開始で Goal 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Goal 機能の出力を取らず展開判定の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開判定の根拠にする。 ✅
    - C. INGLIST を省略して展開判定の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では Goal 機能 は「展開判定の概要 開始に関係する定義値と表示行を照合する展開判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では Goal 機能の属性行と INGKYST0I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では Goal 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開判定初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Grouping applications {#c36-i1112}
*分類: 概要 / 開始*  ・  難易度: 上級

Grouping applicationsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 呼出判定の概要 開始で自動化管理の運用確認を行います。Grouping 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出判定の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出判定の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、呼出判定の結果として保存する。 ✅
    - D. Grouping 機能の属性行を読まず呼出判定の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では Grouping 機能 は「SA z/OS で Grouping 機能の扱いを記録する呼出判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では Grouping 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では Grouping 機能の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Grouping support {#c36-i1113}
*分類: 概要 / 開始*  ・  難易度: 上級

Grouping supportは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 置換判定の概要 開始に関する Grouping supportの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換判定の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定の概要 開始の証跡として保存して根拠にする。
    - C. Grouping supportの変更点を出力本文から切り離して置換判定の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、置換判定の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では Grouping support は「Grouping supportの状態と出力メッセージを結び付ける置換判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では Grouping supportの出力行と INGKYST0I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では Grouping supportを SA z/OS の確認記録に残し、対象名は置換判定対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### HMC task mapping {#c36-i1114}
*分類: 概要 / 開始*  ・  難易度: 上級

HMC task mappingは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 上書判定の概要 開始で自動化管理の運用確認を行います。HMC task mappingの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書判定の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書判定の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、上書判定の点検結果を残す。 ✅
    - D. HMC task mappingの属性行を読まず上書判定の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では HMC task mapping は「SA z/OS で HMC task mappingの扱いを記録する上書判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では HMC task mappingの表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では HMC task mappingの使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Hardware Preparation {#c36-i1115}
*分類: 概要 / 開始*  ・  難易度: 上級

Hardware Preparationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 終端判定の概要 開始に関係する Hardware 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端判定として引き継ぐ。 ✅
    - B. Hardware 機能の名称と担当者名のみを残して終端判定の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端判定の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端判定の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では Hardware 機能 は「Hardware 機能の用途を自動化管理の表示で確認する終端判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では SA z/OS の Hardware 機能と INGKYST0I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では Hardware 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Hardware Resource Security {#c36-i1116}
*分類: 概要 / 開始*  ・  難易度: 上級

Hardware Resource Securityは、Z System Automation (TSA)の概要 / 開始で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 探索判定の概要 開始で Hardware 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Hardware 機能の出力を取らず探索判定の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索判定の確認にする。 ✅
    - C. INGLIST を省略して探索判定の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では Hardware 機能 は「探索判定の概要 開始に関係する定義値と表示行を照合する探索判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では Hardware 機能の属性行と INGKYST0I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では Hardware 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索判定初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Identify initial target systems {#c36-i1117}
*分類: 概要 / 開始*  ・  難易度: 上級

Identify initial target systemsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 出力判定の概要 開始に関する Identify 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力判定の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の概要 開始の証跡として保存して根拠にする。
    - C. Identify 機能の変更点を出力本文から切り離して出力判定の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力判定で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では Identify 機能 は「Identify 機能の状態と出力メッセージを結び付ける出力判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では Identify 機能の出力行と INGKYST0I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では Identify 機能を SA z/OS の確認記録に残し、対象名は出力判定対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Improving your automation policy {#c36-i1118}
*分類: 概要 / 開始*  ・  難易度: 上級

Improving your automation policyは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 条件判定の概要 開始に関係する Improving 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件判定の確認値として扱う。 ✅
    - B. Improving 機能の名称と担当者名のみを残して条件判定の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件判定の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件判定の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Improving 機能 は「Improving 機能の用途を自動化管理の表示で確認する条件判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では SA z/OS の Improving 機能と INGKYST0I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Improving 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Infrastructure {#c36-i1119}
*分類: 概要 / 開始*  ・  難易度: 上級

Infrastructureは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 区切判定の概要 開始で Infrastructureの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Infrastructureの出力を取らず区切判定の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切判定の根拠を固定する。 ✅
    - C. INGLIST を省略して区切判定の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Infrastructure は「区切判定の概要 開始に関係する定義値と表示行を照合する区切判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Infrastructureの属性行と INGKYST0I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Infrastructureを Z System Automation (TSA)の運用手順で確認し、初出名は区切判定初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Installation and Configuration {#c36-i1120}
*分類: 概要 / 開始*  ・  難易度: 上級

Installation and Configurationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（2問）"
    **問題.** 範囲判定の概要 開始で自動化管理の運用確認を行います。Installation 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲判定の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲判定の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を範囲判定で確認する。 ✅
    - D. Installation 機能の属性行を読まず範囲判定の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では Installation 機能 は「SA z/OS で Installation 機能の扱いを記録する範囲判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では Installation 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では Installation 機能の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 順序追跡の計画 インストールで自動化管理の運用確認を行います。Installation 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序追跡の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序追跡の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序追跡の確認記録にまとめる。 ✅
    - D. Installation 機能の属性行を読まず順序追跡の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では Installation 機能 は「SA z/OS で Installation 機能の扱いを記録する順序追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では Installation 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では Installation 機能の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Installing SA z/OS {#c36-i1121}
*分類: 概要 / 開始*  ・  難易度: 上級

Installing SA z/OSは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録判定のInstalling SA z/OSに関係する Installing SA z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録判定の確認記録にまとめる。 ✅
    - B. Installing SA z 属性の名称と担当者名のみを残して記録判定のInstalling SA z/OSの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録判定のInstalling SA z/OSを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録判定のInstalling SA z/OSの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では Installing SA z 属性 は「Installing SA z 属性の用途を自動化管理の表示で確認する記録判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では SA z/OS の Installing SA z 属性と INGKYST0I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では Installing SA z 属性を Z System Automation (TSA)で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Installing and deploying SMP/E {#c36-i1122}
*分類: 概要 / 開始*  ・  難易度: 上級

Installing and deploying SMP/Eは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先判定の概要 開始に関する Installing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先判定の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の概要 開始の証跡として保存して根拠にする。
    - C. Installing 機能の変更点を出力本文から切り離して優先判定の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、優先判定の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では Installing 機能 は「Installing 機能の状態と出力メッセージを結び付ける優先判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では Installing 機能の出力行と INGKYST0I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では Installing 機能を SA z/OS の確認記録に残し、対象名は優先判定対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Introduction and Overview {#c36-i1123}
*分類: 概要 / 開始*  ・  難易度: 上級

Introduction and Overviewは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較判定の概要 開始で Introduction 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Introduction 機能の出力を取らず比較判定の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較判定の根拠にする。 ✅
    - C. INGLIST を省略して比較判定の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では Introduction 機能 は「比較判定の概要 開始に関係する定義値と表示行を照合する比較判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では Introduction 機能の属性行と INGKYST0I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では Introduction 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較判定初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Key concepts {#c36-i1124}
*分類: 概要 / 開始*  ・  難易度: 上級

Key conceptsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 順序判定の概要 開始で自動化管理の運用確認を行います。Key conceptsの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序判定の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序判定の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、順序判定の結果として保存する。 ✅
    - D. Key conceptsの属性行を読まず順序判定の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では Key concepts は「SA z/OS で Key conceptsの扱いを記録する順序判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では Key conceptsの表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では Key conceptsの使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Mainframes That Are Supported {#c36-i1125}
*分類: 概要 / 開始*  ・  難易度: 上級

Mainframes That Are Supportedは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 値域判定の概要 開始に関する Mainframes 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域判定の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の概要 開始の証跡として保存して根拠にする。
    - C. Mainframes 機能の変更点を出力本文から切り離して値域判定の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、値域判定の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では Mainframes 機能 は「Mainframes 機能の状態と出力メッセージを結び付ける値域判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では Mainframes 機能の出力行と INGKYST0I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では Mainframes 機能を SA z/OS の確認記録に残し、対象名は値域判定対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Maintenance {#c36-i1126}
*分類: 概要 / 開始*  ・  難易度: 上級

Maintenanceは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 警告判定の概要 開始に関係する Maintenanceの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告判定として引き継ぐ。 ✅
    - B. Maintenanceの名称と担当者名のみを残して警告判定の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告判定の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告判定の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では Maintenance は「Maintenanceの用途を自動化管理の表示で確認する警告判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では SA z/OS の Maintenanceと INGKYST0I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では Maintenanceを Z System Automation (TSA)で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Mapping Processor Hardware Interface Items to Customization Dialog {#c36-i1127}
*分類: 概要 / 開始*  ・  難易度: 上級

Mapping Processor Hardware Interface Items to Customization Dialogは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧判定の概要 開始で Mapping 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Mapping 機能の出力を取らず復旧判定の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧判定の確認にする。 ✅
    - C. INGLIST を省略して復旧判定の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では Mapping 機能 は「復旧判定の概要 開始に関係する定義値と表示行を照合する復旧判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では Mapping 機能の属性行と INGKYST0I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では Mapping 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Modifying the NetView subsystem interface procedure {#c36-i1128}
*分類: 概要 / 開始*  ・  難易度: 上級

Modifying the NetView subsystem interface procedureは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更判定の概要 開始に関する Modifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更判定の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定の概要 開始の証跡として保存して根拠にする。
    - C. Modifying 機能の変更点を出力本文から切り離して変更判定の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更判定で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Modifying 機能 は「Modifying 機能の状態と出力メッセージを結び付ける変更判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Modifying 機能の出力行と INGKYST0I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Modifying 機能を SA z/OS の確認記録に残し、対象名は変更判定対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Modifying the maximum number of Language Processor (REXX) environments for NetView {#c36-i1129}
*分類: 概要 / 開始*  ・  難易度: 上級

Modifying the maximum number of Language Processor (REXX) environments for NetViewは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Monitoring resources {#c36-i1130}
*分類: 概要 / 開始*  ・  難易度: 上級

Monitoring resourcesは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文整理の概要 開始に関係する Monitoring 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文整理の確認値として扱う。 ✅
    - B. Monitoring 機能の名称と担当者名のみを残して構文整理の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文整理の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文整理の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では Monitoring 機能 は「Monitoring 機能の用途を自動化管理の表示で確認する構文整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では SA z/OS の Monitoring 機能と INGKYST0I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では Monitoring 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### NetView console {#c36-i1131}
*分類: 概要 / 開始*  ・  難易度: 上級

NetView consoleは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 展開整理の概要 開始で NetView consoleの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NetView consoleの出力を取らず展開整理の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開整理の根拠を固定する。 ✅
    - C. INGLIST を省略して展開整理の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では NetView console は「展開整理の概要 開始に関係する定義値と表示行を照合する展開整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では NetView consoleの属性行と INGKYST0I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では NetView consoleを Z System Automation (TSA)の運用手順で確認し、初出名は展開整理初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Operating SA z/OS {#c36-i1132}
*分類: 概要 / 開始*  ・  難易度: 上級

Operating SA z/OSは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 呼出整理のOperating SA z/OSで自動化管理の運用確認を行います。Operating SA z・ OS の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出整理のOperating SA z/OSを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出整理のOperating SA z/OSを正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を呼出整理で確認する。 ✅
    - D. Operating SA z・ OS の属性行を読まず呼出整理のOperating SA z/OSの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では Operating SA z・ OS は「SA z/OS で Operating SA z・ OS の扱いを記録する呼出整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では Operating SA z・ OS の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では Operating SA z・ OS の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Operating the Processor Hardware Interfaces {#c36-i1133}
*分類: 概要 / 開始*  ・  難易度: 上級

Operating the Processor Hardware Interfacesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換整理の概要 開始に関する Operating 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換整理の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理の概要 開始の証跡として保存して根拠にする。
    - C. Operating 機能の変更点を出力本文から切り離して置換整理の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、置換整理の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では Operating 機能 は「Operating 機能の状態と出力メッセージを結び付ける置換整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では Operating 機能の出力行と INGKYST0I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では Operating 機能を SA z/OS の確認記録に残し、対象名は置換整理対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Operations {#c36-i1134}
*分類: 概要 / 開始*  ・  難易度: 上級

Operationsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 終端整理の概要 開始に関係する Operationsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端整理の確認記録にまとめる。 ✅
    - B. Operationsの名称と担当者名のみを残して終端整理の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端整理の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端整理の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では Operations は「Operationsの用途を自動化管理の表示で確認する終端整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では SA z/OS の Operationsと INGKYST0I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では Operationsを Z System Automation (TSA)で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Other functions {#c36-i1135}
*分類: 概要 / 開始*  ・  難易度: 上級

Other functionsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 探索整理の概要 開始で Other functionsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Other functionsの出力を取らず探索整理の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索整理の根拠にする。 ✅
    - C. INGLIST を省略して探索整理の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では Other functions は「探索整理の概要 開始に関係する定義値と表示行を照合する探索整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では Other functionsの属性行と INGKYST0I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では Other functionsを Z System Automation (TSA)の運用手順で確認し、初出名は探索整理初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Planning {#c36-i1136}
*分類: 概要 / 開始*  ・  難易度: 上級

Planningは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（2問）"
    **問題.** 上書整理の概要 開始で自動化管理の運用確認を行います。Planningの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書整理の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書整理の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、上書整理の結果として保存する。 ✅
    - D. Planningの属性行を読まず上書整理の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では Planning は「SA z/OS で Planningの扱いを記録する上書整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では Planningの表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では Planningの使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 監査検査の計画 インストールで自動化管理の運用確認を行います。Planningの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査検査の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査検査の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査検査の確認記録にまとめる。 ✅
    - D. Planningの属性行を読まず監査検査の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では Planning は「SA z/OS で Planningの扱いを記録する監査検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では Planningの表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では Planningの使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Planning for SA z/OS {#c36-i1137}
*分類: 概要 / 開始*  ・  難易度: 上級

Planning for SA z/OSは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として Planning for SA z/OS を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。構文照合保守で扱う Planning for SA z/OS は Z System Automation (TSA) の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として Planning for SA z/OS を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning worksheet {#c36-i1138}
*分類: 概要 / 開始*  ・  難易度: 上級

Planning worksheetは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件整理の概要 開始に関係する Planning worksheetの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件整理として引き継ぐ。 ✅
    - B. Planning worksheetの名称と担当者名のみを残して条件整理の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件整理の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件整理の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では Planning worksheet は「Planning worksheetの用途を自動化管理の表示で確認する条件整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では SA z/OS の Planning worksheetと INGKYST0I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では Planning worksheetを Z System Automation (TSA)で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Policy-based automation {#c36-i1139}
*分類: 概要 / 開始*  ・  難易度: 上級

Policy-based automationは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 区切整理の概要 開始で Policy-based 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Policy-based 機能の出力を取らず区切整理の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切整理の確認にする。 ✅
    - C. INGLIST を省略して区切整理の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では Policy-based 機能 は「区切整理の概要 開始に関係する定義値と表示行を照合する区切整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では Policy-based 機能の属性行と INGKYST0I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では Policy-based 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切整理初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Preparation and Configuration {#c36-i1140}
*分類: 概要 / 開始*  ・  難易度: 上級

Preparation and Configurationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲整理の概要 開始で自動化管理の運用確認を行います。Preparation 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲整理の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲整理の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、範囲整理の点検結果を残す。 ✅
    - D. Preparation 機能の属性行を読まず範囲整理の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Preparation 機能 は「SA z/OS で Preparation 機能の扱いを記録する範囲整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Preparation 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Preparation 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Preparing the Autotasks {#c36-i1141}
*分類: 概要 / 開始*  ・  難易度: 上級

Preparing the Autotasksは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 優先整理の概要 開始に関する Preparing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先整理の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理の概要 開始の証跡として保存して根拠にする。
    - C. Preparing 機能の変更点を出力本文から切り離して優先整理の概要 開始の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先整理で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では Preparing 機能 は「Preparing 機能の状態と出力メッセージを結び付ける優先整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では Preparing 機能の出力行と INGKYST0I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では Preparing 機能を SA z/OS の確認記録に残し、対象名は優先整理対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Preparing to Configure System Automation {#c36-i1142}
*分類: 概要 / 開始*  ・  難易度: 上級

Preparing to Configure System Automationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（2問）"
    **問題.** 記録整理の概要 開始に関係する Preparing 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録整理の確認値として扱う。 ✅
    - B. Preparing 機能の名称と担当者名のみを残して記録整理の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録整理の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録整理の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では Preparing 機能 は「Preparing 機能の用途を自動化管理の表示で確認する記録整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では SA z/OS の Preparing 機能と INGKYST0I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では Preparing 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 優先判定の計画 インストールに関する Preparing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先判定の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の計画 インストールの証跡として保存して根拠にする。
    - C. Preparing 機能の変更点を出力本文から切り離して優先判定の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先判定の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では Preparing 機能 は「Preparing 機能の状態と出力メッセージを結び付ける優先判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では Preparing 機能の出力行と INGKYST0I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では Preparing 機能を SA z/OS の確認記録に残し、対象名は優先判定対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Processor Hardware Interfaces {#c36-i1143}
*分類: 概要 / 開始*  ・  難易度: 上級

Processor Hardware Interfacesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 比較整理の概要 開始で Processor 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Processor 機能の出力を取らず比較整理の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較整理の根拠を固定する。 ✅
    - C. INGLIST を省略して比較整理の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では Processor 機能 は「比較整理の概要 開始に関係する定義値と表示行を照合する比較整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では Processor 機能の属性行と INGKYST0I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では Processor 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較整理初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Product benefits {#c36-i1144}
*分類: 概要 / 開始*  ・  難易度: 上級

Product benefitsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 順序整理の概要 開始で自動化管理の運用確認を行います。Product benefitsの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序整理の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序整理の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を順序整理で確認する。 ✅
    - D. Product benefitsの属性行を読まず順序整理の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では Product benefits は「SA z/OS で Product benefitsの扱いを記録する順序整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では Product benefitsの表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では Product benefitsの使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Product introduction {#c36-i1145}
*分類: 概要 / 開始*  ・  難易度: 上級

Product introductionは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 値域整理の概要 開始に関する Product 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域整理の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理の概要 開始の証跡として保存して根拠にする。
    - C. Product 機能の変更点を出力本文から切り離して値域整理の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、値域整理の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では Product 機能 は「Product 機能の状態と出力メッセージを結び付ける値域整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では Product 機能の出力行と INGKYST0I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では Product 機能を SA z/OS の確認記録に残し、対象名は値域整理対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Product overview {#c36-i1146}
*分類: 概要 / 開始*  ・  難易度: 上級

Product overviewは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 警告整理の概要 開始に関係する Product overviewの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告整理の確認記録にまとめる。 ✅
    - B. Product overviewの名称と担当者名のみを残して警告整理の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告整理の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告整理の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では Product overview は「Product overviewの用途を自動化管理の表示で確認する警告整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では SA z/OS の Product overviewと INGKYST0I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では Product overviewを Z System Automation (TSA)で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Quick planning exercise {#c36-i1147}
*分類: 概要 / 開始*  ・  難易度: 上級

Quick planning exerciseは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 復旧整理の概要 開始で Quick 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Quick 機能の出力を取らず復旧整理の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧整理の根拠にする。 ✅
    - C. INGLIST を省略して復旧整理の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Quick 機能 は「復旧整理の概要 開始に関係する定義値と表示行を照合する復旧整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Quick 機能の属性行と INGKYST0I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Quick 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Related Hardware Documentation {#c36-i1148}
*分類: 概要 / 開始*  ・  難易度: 上級

Related Hardware Documentationは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査整理の概要 開始で自動化管理の運用確認を行います。Related 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査整理の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査整理の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、監査整理の結果として保存する。 ✅
    - D. Related 機能の属性行を読まず監査整理の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では Related 機能 は「SA z/OS で Related 機能の扱いを記録する監査整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では Related 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では Related 機能の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Relationships {#c36-i1149}
*分類: 概要 / 開始*  ・  難易度: 上級

Relationshipsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 変更整理の概要 開始に関する Relationshipsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更整理の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理の概要 開始の証跡として保存して根拠にする。
    - C. Relationshipsの変更点を出力本文から切り離して変更整理の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、変更整理の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では Relationships は「Relationshipsの状態と出力メッセージを結び付ける変更整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では Relationshipsの出力行と INGKYST0I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では Relationshipsを SA z/OS の確認記録に残し、対象名は変更整理対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Relationships and dependencies {#c36-i1150}
*分類: 概要 / 開始*  ・  難易度: 上級

Relationships and dependenciesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 構文記録の概要 開始に関係する Relationships 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文記録として引き継ぐ。 ✅
    - B. Relationships 機能の名称と担当者名のみを残して構文記録の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文記録の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文記録の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では Relationships 機能 は「Relationships 機能の用途を自動化管理の表示で確認する構文記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では SA z/OS の Relationships 機能と INGKYST0I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では Relationships 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Reporting {#c36-i1151}
*分類: 概要 / 開始*  ・  難易度: 上級

Reportingは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 展開記録の概要 開始で Reportingの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Reportingの出力を取らず展開記録の概要 開始の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開記録の確認にする。 ✅
    - C. INGLIST を省略して展開記録の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Reporting は「展開記録の概要 開始に関係する定義値と表示行を照合する展開記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Reportingの属性行と INGKYST0I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Reportingを Z System Automation (TSA)の運用手順で確認し、初出名は展開記録初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Resources {#c36-i1152}
*分類: 概要 / 開始*  ・  難易度: 上級

Resourcesは、Z System Automation (TSA)の概要 / 開始でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（2問）"
    **問題.** 呼出記録の概要 開始で自動化管理の運用確認を行います。Resourcesの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出記録の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出記録の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、呼出記録の点検結果を残す。 ✅
    - D. Resourcesの属性行を読まず呼出記録の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Resources は「SA z/OS で Resourcesの扱いを記録する呼出記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Resourcesの表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Resourcesの使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 警告判定の計画 インストールに関係する Resourcesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、警告判定の点検結果を残す。 ✅
    - B. Resourcesの名称と担当者名のみを残して警告判定の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告判定の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告判定の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では Resources は「Resourcesの用途を自動化管理の表示で確認する警告判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では SA z/OS の Resourcesと INGKYST0I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では Resourcesを Z System Automation (TSA)で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Restarting SA z/OS {#c36-i1153}
*分類: 概要 / 開始*  ・  難易度: 上級

Restarting SA z/OSは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換記録のRestarting SA z/OSに関する Restarting SA z 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換記録のRestarting SA z/OSの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録のRestarting SA z/OSの証跡として保存して根拠にする。
    - C. Restarting SA z 属性の変更点を出力本文から切り離して置換記録のRestarting SA z/OSの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換記録で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Restarting SA z 属性 は「Restarting SA z 属性の状態と出力メッセージを結び付ける置換記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Restarting SA z 属性の出力行と INGKYST0I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Restarting SA z 属性を SA z/OS の確認記録に残し、対象名は置換記録対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Review {#c36-i1154}
*分類: 概要 / 開始*  ・  難易度: 上級

Reviewは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 終端記録の概要 開始に関係する Reviewの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端記録の確認値として扱う。 ✅
    - B. Reviewの名称と担当者名のみを残して終端記録の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端記録の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端記録の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では Review は「Reviewの用途を自動化管理の表示で確認する終端記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では SA z/OS の Reviewと INGKYST0I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では Reviewを Z System Automation (TSA)で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Roles and responsibilities {#c36-i1155}
*分類: 概要 / 開始*  ・  難易度: 上級

Roles and responsibilitiesは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 探索記録の概要 開始で Roles 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Roles 機能の出力を取らず探索記録の概要 開始の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索記録の根拠を固定する。 ✅
    - C. INGLIST を省略して探索記録の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Roles 機能 は「探索記録の概要 開始に関係する定義値と表示行を照合する探索記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Roles 機能の属性行と INGKYST0I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Roles 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索記録初出です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Saving Automation Manager data sets into Generation Data Groups {#c36-i1156}
*分類: 概要 / 開始*  ・  難易度: 上級

Saving Automation Manager data sets into Generation Data Groupsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 上書記録の概要 開始で自動化管理の運用確認を行います。Saving 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書記録の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書記録の概要 開始を正常終了として記録する。
    - C. INGKYST0I を含む表示を保存し、説明欄との差分を上書記録で確認する。 ✅
    - D. Saving 機能の属性行を読まず上書記録の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Saving 機能 は「SA z/OS で Saving 機能の扱いを記録する上書記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Saving 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Saving 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Scope of Control {#c36-i1157}
*分類: 概要 / 開始*  ・  難易度: 上級

Scope of Controlは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 出力記録の概要 開始に関する Scope of Controlの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力記録の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録の概要 開始の証跡として保存して根拠にする。
    - C. Scope of Controlの変更点を出力本文から切り離して出力記録の概要 開始の承認欄のみ残す。
    - D. INGLIST の結果から対象行を抜き出し、出力記録の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Scope of Control は「Scope of Controlの状態と出力メッセージを結び付ける出力記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Scope of Controlの出力行と INGKYST0I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Scope of Controlを SA z/OS の確認記録に残し、対象名は出力記録対象です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Security {#c36-i1158}
*分類: 概要 / 開始*  ・  難易度: 上級

Securityは、Z System Automation (TSA)の概要 / 開始で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。TSA z/OS Get Started Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS Get Started Guide

??? question "確認問題（1問）"
    **問題.** 条件記録の概要 開始に関係する Securityの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件記録の確認記録にまとめる。 ✅
    - B. Securityの名称と担当者名のみを残して条件記録の概要 開始の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件記録の概要 開始を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件記録の概要 開始の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Security は「Securityの用途を自動化管理の表示で確認する条件記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では SA z/OS の Securityと INGKYST0I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Securityを Z System Automation (TSA)で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Customizing_and_Programming



### Selecting the appropriate Interface to use {#c36-i1159}
*分類: 概要 / 開始*  ・  難易度: 上級

Selecting the appropriate Interface to useは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切記録の概要 開始で Selecting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Selecting 機能の出力を取らず区切記録の概要 開始の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切記録の根拠にする。 ✅
    - C. INGLIST を省略して区切記録の概要 開始の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録の概要 開始へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Selecting 機能 は「区切記録の概要 開始に関係する定義値と表示行を照合する区切記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Selecting 機能の属性行と INGKYST0I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Selecting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切記録初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Setting up your systems {#c36-i1160}
*分類: 概要 / 開始*  ・  難易度: 上級

Setting up your systemsは、Z System Automation (TSA)の概要 / 開始で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲記録の概要 開始で自動化管理の運用確認を行います。Setting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲記録の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲記録の概要 開始を正常終了として記録する。
    - C. 同じ画面で対象行と INGKYST0I を読み、範囲記録の結果として保存する。 ✅
    - D. Setting 機能の属性行を読まず範囲記録の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Setting 機能 は「SA z/OS で Setting 機能の扱いを記録する範囲記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Setting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Setting 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Specifying the subsystem command designator {#c36-i1161}
*分類: 概要 / 開始*  ・  難易度: 上級

Specifying the subsystem command designatorは、Z System Automation (TSA)の概要 / 開始で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先記録の概要 開始に関する Specifying 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先記録の概要 開始の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の概要 開始の証跡として保存して根拠にする。
    - C. Specifying 機能の変更点を出力本文から切り離して優先記録の概要 開始の承認欄のみ残す。
    - D. INGLIST で得た表示本文を使い、優先記録の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Specifying 機能 は「Specifying 機能の状態と出力メッセージを結び付ける優先記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Specifying 機能の出力行と INGKYST0I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Specifying 機能を SA z/OS の確認記録に残し、対象名は優先記録対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


