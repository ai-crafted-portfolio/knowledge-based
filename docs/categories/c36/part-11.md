---
search:
  exclude: true
---

# Z System Automation (TSA) — 詳細 (11/12)

[← Z System Automation (TSA) の概要へ戻る](index.md)


## Z System Automation (TSA) > 自動化ポリシー定義

### UPWARD CLASS Policy Item {#c36-i1443}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

UPWARD CLASS Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 探索確認の自動化ポリシー定義で UPWARD 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UPWARD 機能の出力を取らず探索確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、探索確認の証跡として残す。 ✅
    - C. INGLIST を省略して探索確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では UPWARD 機能 は「探索確認の自動化ポリシー定義に関係する定義値と表示行を照合する探索確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では UPWARD 機能の属性行と INGKYST0I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では UPWARD 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索確認初出です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.173) / OS 自動化ポリシー定義



### USER MSG CLASSES Policy Item {#c36-i1444}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

USER MSG CLASSES Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.39) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 出力確認の自動化ポリシー定義に関する USER 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. USER 機能の変更点を出力本文から切り離して出力確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では USER 機能 は「USER 機能の状態と出力メッセージを結び付ける出力確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では USER 機能の出力行と INGKYST0I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では USER 機能を SA z/OS の確認記録に残し、対象名は出力確認対象です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.39) / OS 自動化ポリシー定義



### Updating Policy Objects Using Text Files {#c36-i1445}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Updating Policy Objects Using Text Filesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端確認の自動化ポリシー定義に関係する Updating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を終端確認で確認する。 ✅
    - B. Updating 機能の名称と担当者名のみを残して終端確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Updating 機能 は「Updating 機能の用途を自動化管理の表示で確認する終端確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では SA z/OS の Updating 機能と INGKYST0I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Updating 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### User E-T Pairs Entry Type {#c36-i1446}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

User E-T Pairs Entry Typeは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 上書確認の自動化ポリシー定義で自動化管理の運用確認を行います。User 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書確認の自動化ポリシー定義を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書確認の確認記録にまとめる。 ✅
    - D. User 機能の属性行を読まず上書確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では User 機能 は「SA z/OS で User 機能の扱いを記録する上書確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では User 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では User 機能の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.337) / OS 自動化ポリシー定義



### User-written Functions {#c36-i1447}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

User-written Functionsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 条件確認の自動化ポリシー定義に関係する User-written 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、条件確認の結果として保存する。 ✅
    - B. User-written 機能の名称と担当者名のみを残して条件確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では User-written 機能 は「User-written 機能の用途を自動化管理の表示で確認する条件確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では SA z/OS の User-written 機能と INGKYST0I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では User-written 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.188) / OS 自動化ポリシー定義



### Using SA z/OS Sample Policies {#c36-i1448}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Using SA z/OS Sample Policiesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切確認のUsing SA z/OS Sample Policiesで Using SA z 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using SA z 属性の出力を取らず区切確認のUsing SA z/OS Sample Policiesの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、区切確認の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して区切確認のUsing SA z/OS Sample Policiesの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のUsing SA z/OS Sample Policiesへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Using SA z 属性 は「区切確認のUsing SA z/OS Sample Policiesに関係する定義値と表示行を照合する区切確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Using SA z 属性の属性行と INGKYST0I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Using SA z 属性を Z System Automation (TSA)の運用手順で確認し、初出名は区切確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using System Symbols and System Automation Symbols {#c36-i1449}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Using System Symbols and System Automation Symbolsは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲確認の自動化ポリシー定義で自動化管理の運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲確認の自動化ポリシー定義を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲確認として引き継ぐ。 ✅
    - D. Using 機能の属性行を読まず範囲確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Using 機能 は「SA z/OS で Using 機能の扱いを記録する範囲確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Using 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Using 機能の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using the Customization Dialog {#c36-i1450}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Using the Customization Dialogは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先確認の自動化ポリシー定義に関する Using 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先確認の自動化ポリシー定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の自動化ポリシー定義の証跡として保存して根拠にする。
    - C. Using 機能の変更点を出力本文から切り離して優先確認の自動化ポリシー定義の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先確認の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Using 機能 は「Using 機能の状態と出力メッセージを結び付ける優先確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Using 機能の出力行と INGKYST0I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Using 機能を SA z/OS の確認記録に残し、対象名は優先確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### WHERE USED Policy Item {#c36-i1451}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

WHERE USED Policy Itemは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義

??? question "確認問題（1問）"
    **問題.** 記録確認の自動化ポリシー定義に関係する WHERE 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、記録確認の点検結果を残す。 ✅
    - B. WHERE 機能の名称と担当者名のみを残して記録確認の自動化ポリシー定義の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録確認の自動化ポリシー定義を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録確認の自動化ポリシー定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では WHERE 機能 は「WHERE 機能の用途を自動化管理の表示で確認する記録確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では SA z/OS の WHERE 機能と INGKYST0I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では WHERE 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** TSA z / OS 自動化ポリシー定義 (TSA_z_OS_4.3_Defining_Automation_Policy.pdf p.54) / OS 自動化ポリシー定義



### Working with MONITOR Resources {#c36-i1452}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Working with MONITOR Resourcesは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較確認の自動化ポリシー定義で Working 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Working 機能の出力を取らず比較確認の自動化ポリシー定義の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較確認で再確認できる形にする。 ✅
    - C. INGLIST を省略して比較確認の自動化ポリシー定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の自動化ポリシー定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Working 機能 は「比較確認の自動化ポリシー定義に関係する定義値と表示行を照合する比較確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Working 機能の属性行と INGKYST0I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Working 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較確認初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Write Data to File using a Batch Job {#c36-i1453}
*分類: 自動化ポリシー定義*  ・  難易度: 上級

Write Data to File using a Batch Jobは、Z System Automation (TSA)の自動化ポリシー定義でリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序確認の自動化ポリシー定義で自動化管理の運用確認を行います。Write 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序確認の自動化ポリシー定義を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序確認の自動化ポリシー定義を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序確認の確認値として扱う。 ✅
    - D. Write 機能の属性行を読まず順序確認の自動化ポリシー定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Write 機能 は「SA z/OS で Write 機能の扱いを記録する順序確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Write 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Write 機能の使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 自動化ポリシー定義 > MOVE group

### MOVE group {#c36-i1454}
*分類: 自動化ポリシー定義 > MOVE group*  ・  難易度: 上級

MOVE groupは、同時に一つの構成員だけが活動するシスプレックス・アプリケーション・グループです。INGMOVEで活動する場所を切り替えます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開確認再の自動化管理で MOVE groupの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MOVE groupの出力を取らず展開確認再の自動化管理の説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、展開確認再の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して展開確認再の自動化管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認再の自動化管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認再正解では選択記号 B を採用し、正解名は展開確認再正解です。展開確認再根拠では MOVE group は「展開確認再の自動化管理に関係する定義値と表示行を照合する展開確認再項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開確認再根拠です。展開確認再追跡では MOVE groupの属性行と INGKYST0I を合わせ、追跡名は展開確認再追跡です。誤答側の問題点を分けます。 A: 展開確認再不足は名称や説明のみに寄り、判定名は展開確認再不足です。 B: 展開確認再正答は対象出力と項目説明を結び、根拠名は展開確認再正答です。 C: 展開確認再欠落は戻り値や記録番号に寄り、欠落名は展開確認再欠落です。 D: 展開確認再流用は別カテゴリの確認であり、排除名は展開確認再流用です。展開確認再初出では MOVE groupを Z System Automation (TSA)の運用手順で確認し、初出名は展開確認再初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 自動化ポリシー定義 > dynamic resource

### dynamic resource {#c36-i1455}
*分類: 自動化ポリシー定義 > dynamic resource*  ・  難易度: 上級

dynamic resourceは、運用中に動的に生じる資源です。静的な資源へ変えるときは、手動で動的な資源を削除して定義を加えます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換確認再の自動化管理に関するdynamic resourceの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換確認再の自動化管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認再の自動化管理の証跡として保存して根拠にする。
    - C. dynamic resourceの変更点を出力本文から切り離して置換確認再の自動化管理の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換確認再の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認再正解では選択記号 D を採用し、正解名は置換確認再正解です。置換確認再根拠ではdynamic resource は「dynamic resourceの状態と出力メッセージを結び付ける置換確認再項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換確認再根拠です。置換確認再保存ではdynamic resourceの出力行と INGKYST0I を一緒に残し、保存名は置換確認再保存です。選択肢ごとの違いを示します。 A: 置換確認再欠落は戻り値や記録番号に寄り、欠落名は置換確認再欠落です。 B: 置換確認再流用は別カテゴリの確認であり、排除名は置換確認再流用です。 C: 置換確認再不足は名称や説明のみに寄り、判定名は置換確認再不足です。 D: 置換確認再正答は対象出力と項目説明を結び、根拠名は置換確認再正答です。置換確認再対象ではdynamic resourceを SA z/OS の確認記録に残し、対象名は置換確認再対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 自動化ポリシー定義 > static resource

### static resource {#c36-i1456}
*分類: 自動化ポリシー定義 > static resource*  ・  難易度: 中級

static resourceは、ポリシーにあらかじめ定義される静的な資源です。自動化マネージャーのデータモデルに保持されます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出確認再の自動化管理で自動化管理の運用確認を行います。static resourceの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出確認再の自動化管理を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出確認再の自動化管理を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出確認再として引き継ぐ。 ✅
    - D. static resourceの属性行を読まず呼出確認再の自動化管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認再正解では選択記号 C を採用し、正解名は呼出確認再正解です。呼出確認再根拠ではstatic resource は「SA z/OS でstatic resourceの扱いを記録する呼出確認再項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出確認再根拠です。呼出確認再受渡ではstatic resourceの表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出確認再受渡です。不適切な選択肢を整理します。 A: 呼出確認再流用は別カテゴリの確認であり、排除名は呼出確認再流用です。 B: 呼出確認再欠落は戻り値や記録番号に寄り、欠落名は呼出確認再欠落です。 C: 呼出確認再正答は対象出力と項目説明を結び、根拠名は呼出確認再正答です。 D: 呼出確認再不足は名称や説明のみに寄り、判定名は呼出確認再不足です。呼出確認再資料ではstatic resourceの使い方を出典欄から追跡し、資料名は呼出確認再資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 自動化ポリシー定義 > sysplex application group

### sysplex application group {#c36-i1457}
*分類: 自動化ポリシー定義 > sysplex application group*  ・  難易度: 上級

sysplex application groupは、シスプレックスにまたがる複数の構成員をまとめて扱う資源のグループです。MOVE型やServer型で運用の仕方が変わります

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文確認再の自動化管理に関係するsysplex 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、構文確認再の結果として保存する。 ✅
    - B. sysplex 機能の名称と担当者名のみを残して構文確認再の自動化管理の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文確認再の自動化管理を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文確認再の自動化管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認再正解では選択記号 A を採用し、正解名は構文確認再正解です。構文確認再根拠ではsysplex 機能 は「sysplex 機能の用途を自動化管理の表示で確認する構文確認再項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文確認再根拠です。構文確認再背景では SA z/OS のsysplex 機能と INGKYST0I を同じ証跡に残し、背景名は構文確認再背景です。他の選択肢を確認します。 A: 構文確認再正答は対象出力と項目説明を結び、根拠名は構文確認再正答です。 B: 構文確認再不足は名称や説明のみに寄り、判定名は構文確認再不足です。 C: 構文確認再流用は別カテゴリの確認であり、排除名は構文確認再流用です。 D: 構文確認再欠落は戻り値や記録番号に寄り、欠落名は構文確認再欠落です。構文確認再用語ではsysplex 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文確認再用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 自動化マネージャー > INGAMS

### INGAMS {#c36-i1458}
*分類: 自動化マネージャー > INGAMS*  ・  難易度: 上級

INGAMSは、自動化マネージャーの定義を動的にリフレッシュしたり、二次を一次へ昇格させたりするコマンドです。パネルのFL列は有効な機能水準を示します

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 自動化マネージャー > INGAMS REFRESH

### INGAMS REFRESH {#c36-i1459}
*分類: 自動化マネージャー > INGAMS REFRESH*  ・  難易度: 上級

INGAMS REFRESHは、自動化マネージャーの定義データを指定した構成データセットの内容へ動的に置き換える操作です。矛盾する定義は取り込み時に退けられます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（4問）"
    **問題.** 保守面のポリシー再読込を運用変更で確認します。要求面の対象項目では入力と操作画面応答を照合し、再読込 optionを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. INGAMS REFRESH ✅
    - B. SERVICE PERIOD Policy Item
    - C. USS CONTROL Policy Item
    - D. INGVOTE

    正解: **A** ／ 難易度: 上級

    **解説:** 照合面の判定ではAを選び、対象はポリシー再読込復旧です。運用面の識別語は 自動化マネージャー表示 再読込 で、ポリシー再読込復旧の対象名です。引継ぎ面のポリシー再読込照合は、自動化ポリシー変更をsysplex全体へ反映することを目的に扱う説明単位がポリシー再読込観点です。構成面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はポリシー再読込証跡です。応答面のポリシー再読込読取を読む応答では、再読込 optionを出典の属性説明と照合する点がポリシー再読込状態です。A: 設計面のポリシー再読込復旧が正答です。監査面のポリシー再読込復旧応答で確認できる対象はポリシー再読込復旧です。B: 変更面のポリシー再読込照合で見るサービス期間は役割が異なり、除外理由を説明する対象はポリシー再読込照合です。C: 障害面のポリシー再読込観点で見るユーエスエス制御項目は役割が異なり、除外理由を説明する対象はポリシー再読込観点です。D: 監査面のポリシー再読込証跡で見る投票表示は役割が異なり、除外理由を説明する対象はポリシー再読込証跡です。記録面の初出語説明として、ポリシー再読込とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はポリシー再読込根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.126

    ---

    **問題.** 復旧面のポリシー再読込を障害切り分けで確認します。運用面の対象項目では入力と操作画面応答を照合し、再読込 optionを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. INGMOVE
    - B. Configuration Member
    - C. INGAMS REFRESH ✅
    - D. DB2 CONTROL Policy Item

    正解: **C** ／ 難易度: 上級

    **解説:** 保守面の判定ではCを選び、対象はポリシー再読込引継ぎです。照合面の識別語は 自動化マネージャー表示 再読込 で、ポリシー再読込引継ぎの対象名です。監査面のポリシー再読込棚卸は、自動化ポリシー変更をsysplex全体へ反映することを目的に扱う説明単位がポリシー再読込復旧です。要求面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はポリシー再読込照合です。引継ぎ面のポリシー再読込観点を読む応答では、再読込 optionを出典の属性説明と照合する点がポリシー再読込証跡です。A: 表示面のポリシー再読込引継ぎで見る移動要求は役割が異なり、除外理由を説明する対象はポリシー再読込引継ぎです。B: 設計面のポリシー再読込棚卸で見る構成メンバーは役割が異なり、除外理由を説明する対象はポリシー再読込棚卸です。C: 変更面のポリシー再読込復旧が正答です。引継ぎ面のポリシー再読込復旧応答で確認できる対象はポリシー再読込復旧です。D: 障害面のポリシー再読込照合で見るDb2制御項目は役割が異なり、除外理由を説明する対象はポリシー再読込照合です。構成面の初出語説明として、ポリシー再読込とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はポリシー再読込状態です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.126

    ---

    **問題.** 証跡面のポリシー再読込を監査記録で確認します。照合面の対象項目では入力と操作画面応答を照合し、再読込 optionを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGAMS REFRESH ✅
    - B. DB2 CONTROL Policy Item
    - C. Compound Status
    - D. APPLICATION Entry Type

    正解: **A** ／ 難易度: 上級

    **解説:** 復旧面の判定ではAを選び、対象はポリシー再読込保守です。保守面の識別語は 自動化マネージャー表示 再読込 で、ポリシー再読込保守の対象名です。障害面のポリシー再読込監査は、自動化ポリシー変更をsysplex全体へ反映することを目的に扱う説明単位がポリシー再読込引継ぎです。運用面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はポリシー再読込棚卸です。監査面のポリシー再読込復旧を読む応答では、再読込 optionを出典の属性説明と照合する点がポリシー再読込照合です。A: 記録面のポリシー再読込保守が正答です。変更面のポリシー再読込保守応答で確認できる対象はポリシー再読込保守です。B: 表示面のポリシー再読込監査で見るDb2制御項目は役割が異なり、除外理由を説明する対象はポリシー再読込監査です。C: 設計面のポリシー再読込引継ぎで見る複合状態は役割が異なり、除外理由を説明する対象はポリシー再読込引継ぎです。D: 変更面のポリシー再読込棚卸で見るアプリケーション定義は役割が異なり、除外理由を説明する対象はポリシー再読込棚卸です。要求面の初出語説明として、ポリシー再読込とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はポリシー再読込証跡です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.126

    ---

    **問題.** 出力検分の自動化管理に関する INGAMS REFRESH の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGAMS の結果を残さず出力検分の自動化管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検分の自動化管理の証跡として保存して根拠にする。
    - C. INGAMS REFRESH の変更点を出力本文から切り離して出力検分の自動化管理の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力検分の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では INGAMS REFRESH は「INGAMS REFRESH の状態と出力メッセージを結び付ける出力検分項目」と INGAMS または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では INGAMS REFRESH の出力行と INGKYST0I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明のみに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では INGAMS REFRESH を SA z/OS の確認記録に残し、対象名は出力検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 自動化制御 > INGAUTO

### INGAUTO {#c36-i1460}
*分類: 自動化制御 > INGAUTO*  ・  難易度: 中級

INGAUTOは、特定の資源やグループの自動化フラグの有効と無効を切り替えるコマンドです。操作が済むとFUNCTION COMPLETEDが表示されます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



## Z System Automation (TSA) > 自動化制御 > automation flag

### automation flag {#c36-i1461}
*分類: 自動化制御 > automation flag*  ・  難易度: 中級

automation flagは、資源に対する自動化の効きを表す設定です。有効にすると自動化マネージャーが起動や停止を進め、無効にすると自動化が止まります

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切検分の自動化管理でautomation flagの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. automation flagの出力を取らず区切検分の自動化管理の説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、区切検分の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して区切検分の自動化管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検分の自動化管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠ではautomation flag は「区切検分の自動化管理に関係する定義値と表示行を照合する区切検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡ではautomation flagの属性行と INGKYST0I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明のみに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出ではautomation flagを Z System Automation (TSA)の運用手順で確認し、初出名は区切検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 計画 / インストール

### Alert Notification Infrastructure in SA z/OS {#c36-i1462}
*分類: 計画 / インストール*  ・  難易度: 上級

Alert Notification Infrastructure in SA z/OSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域確認の計画 インストールに関する Alert 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域確認の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の計画 インストールの証跡として保存して根拠にする。
    - C. Alert 機能の変更点を出力本文から切り離して値域確認の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域確認の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Alert 機能 は「Alert 機能の状態と出力メッセージを結び付ける値域確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Alert 機能の出力行と INGKYST0I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Alert 機能を SA z/OS の確認記録に残し、対象名は値域確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Authorization of the Started Procedures {#c36-i1463}
*分類: 計画 / インストール*  ・  難易度: 上級

Authorization of the Started Proceduresは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告確認の計画 インストールに関係する Authorization 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を警告確認で確認する。 ✅
    - B. Authorization 機能の名称と担当者名のみを残して警告確認の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告確認の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告確認の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Authorization 機能 は「Authorization 機能の用途を自動化管理の表示で確認する警告確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では SA z/OS の Authorization 機能と INGKYST0I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Authorization 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Automating Multi-Line z/OS Messages {#c36-i1464}
*分類: 計画 / インストール*  ・  難易度: 上級

Automating Multi-Line z/OS Messagesは、Z System Automation (TSA)の計画 / インストールでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 復旧確認のAutomating Multi-Line z/OS Messagesで Automating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Automating 機能の出力を取らず復旧確認のAutomating Multi-Line z/OS Messagesの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、復旧確認の証跡として残す。 ✅
    - C. INGLIST を省略して復旧確認のAutomating Multi-Line z/OS Messagesの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のAutomating Multi-Line z/OS Messagesへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Automating 機能 は「復旧確認のAutomating Multi-Line z/OS Messagesに関係する定義値と表示行を照合する復旧確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Automating 機能の属性行と INGKYST0I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Automating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Automation Manager Considerations {#c36-i1465}
*分類: 計画 / インストール*  ・  難易度: 上級

Automation Manager Considerationsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 監査確認の計画 インストールで自動化管理の運用確認を行います。Automation 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査確認の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査確認の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査確認の確認記録にまとめる。 ✅
    - D. Automation 機能の属性行を読まず監査確認の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Automation 機能 は「SA z/OS で Automation 機能の扱いを記録する監査確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Automation 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Automation 機能の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Avoid outages caused by LPAR security setting changes {#c36-i1466}
*分類: 計画 / インストール*  ・  難易度: 上級

Avoid outages caused by LPAR security setting changesは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更確認の計画 インストールに関する Avoid 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更確認の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の計画 インストールの証跡として保存して根拠にする。
    - C. Avoid 機能の変更点を出力本文から切り離して変更確認の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更確認の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Avoid 機能 は「Avoid 機能の状態と出力メッセージを結び付ける変更確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Avoid 機能の出力行と INGKYST0I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Avoid 機能を SA z/OS の確認記録に残し、対象名は変更確認対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Avoiding inconsistent console definitions {#c36-i1467}
*分類: 計画 / インストール*  ・  難易度: 上級

Avoiding inconsistent console definitionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 構文照合の計画 インストールに関係する Avoiding 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、構文照合の結果として保存する。 ✅
    - B. Avoiding 機能の名称と担当者名のみを残して構文照合の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文照合の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文照合の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では Avoiding 機能 は「Avoiding 機能の用途を自動化管理の表示で確認する構文照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では SA z/OS の Avoiding 機能と INGKYST0I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では Avoiding 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文照合用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Base SA z/OS Configuration Using the Configuration Assistant {#c36-i1468}
*分類: 計画 / インストール*  ・  難易度: 上級

Base SA z/OS Configuration Using the Configuration Assistantは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として Base SA z/OS Configuration U を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 構文照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。構文照合保守で扱う Base SA z/OS Configuration U は Z System Automation (TSA) の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として Base SA z/OS Configuration U を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### CI Automation Basics {#c36-i1469}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Automation Basicsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 出力照合の計画 インストールに関する CI 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力照合の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の計画 インストールの証跡として保存して根拠にする。
    - C. CI 機能の変更点を出力本文から切り離して出力照合の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力照合の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では CI 機能 は「CI 機能の状態と出力メッセージを結び付ける出力照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では CI 機能の出力行と INGKYST0I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では CI 機能を SA z/OS の確認記録に残し、対象名は出力照合対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### CI Configuration for Remote Automation {#c36-i1470}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Configuration for Remote Automationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件照合の計画 インストールに関係する CI 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を条件照合で確認する。 ✅
    - B. CI 機能の名称と担当者名のみを残して条件照合の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件照合の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件照合の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では CI 機能 は「CI 機能の用途を自動化管理の表示で確認する条件照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では SA z/OS の CI 機能と INGKYST0I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では CI 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### CI Differences to 3270-Based Console Devices {#c36-i1471}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Differences to 3270-Based Console Devicesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切照合の計画 インストールで CI 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CI 機能の出力を取らず区切照合の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、区切照合の証跡として残す。 ✅
    - C. INGLIST を省略して区切照合の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では CI 機能 は「区切照合の計画 インストールに関係する定義値と表示行を照合する区切照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では CI 機能の属性行と INGKYST0I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では CI 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### CI Performance Factors {#c36-i1472}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Performance Factorsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 範囲照合の計画 インストールで自動化管理の運用確認を行います。CI 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲照合の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲照合の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲照合の確認記録にまとめる。 ✅
    - D. CI 機能の属性行を読まず範囲照合の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では CI 機能 は「SA z/OS で CI 機能の扱いを記録する範囲照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では CI 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では CI 機能の使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール



### CI Protocols and Automation Interfaces {#c36-i1473}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Protocols and Automation Interfacesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先照合の計画 インストールに関する CI 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先照合の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の計画 インストールの証跡として保存して根拠にする。
    - C. CI 機能の変更点を出力本文から切り離して優先照合の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先照合の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では CI 機能 は「CI 機能の状態と出力メッセージを結び付ける優先照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では CI 機能の出力行と INGKYST0I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では CI 機能を SA z/OS の確認記録に残し、対象名は優先照合対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### CI Security with SA z/OS {#c36-i1474}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Security with SA z/OSは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録照合のCI Security with SA z/OSに関係する CI 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、記録照合の結果として保存する。 ✅
    - B. CI 機能の名称と担当者名のみを残して記録照合のCI Security with SA z/OSの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録照合のCI Security with SA z/OSを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録照合のCI Security with SA z/OSの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では CI 機能 は「CI 機能の用途を自動化管理の表示で確認する記録照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では SA z/OS の CI 機能と INGKYST0I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では CI 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### CI Usage in IBM System Automation Products {#c36-i1475}
*分類: 計画 / インストール*  ・  難易度: 上級

CI Usage in IBM System Automation Productsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較照合の計画 インストールで CI 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CI 機能の出力を取らず比較照合の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、比較照合の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して比較照合の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では CI 機能 は「比較照合の計画 インストールに関係する定義値と表示行を照合する比較照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では CI 機能の属性行と INGKYST0I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では CI 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較照合初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Changed Commands and Displays {#c36-i1476}
*分類: 計画 / インストール*  ・  難易度: 上級

Changed Commands and Displaysは、Z System Automation (TSA)の計画 / インストールで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 呼出照合の計画 インストールで自動化管理の運用確認を行います。Changed 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出照合の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出照合の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出照合として引き継ぐ。 ✅
    - D. Changed 機能の属性行を読まず呼出照合の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では Changed 機能 は「SA z/OS で Changed 機能の扱いを記録する呼出照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では Changed 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では Changed 機能の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Changed Exits {#c36-i1477}
*分類: 計画 / インストール*  ・  難易度: 上級

Changed Exitsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 置換照合の計画 インストールに関する Changed Exitsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換照合の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の計画 インストールの証跡として保存して根拠にする。
    - C. Changed Exitsの変更点を出力本文から切り離して置換照合の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換照合の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では Changed Exits は「Changed Exitsの状態と出力メッセージを結び付ける置換照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では Changed Exitsの出力行と INGKYST0I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では Changed Exitsを SA z/OS の確認記録に残し、対象名は置換照合対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Changed Low-Level Qualifiers (LLQs) of Installation Data Sets {#c36-i1478}
*分類: 計画 / インストール*  ・  難易度: 上級

Changed Low-Level Qualifiers (LLQs) of Installation Data Setsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端照合の計画 インストールに関係する Changed 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、終端照合の点検結果を残す。 ✅
    - B. Changed 機能の名称と担当者名のみを残して終端照合の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端照合の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端照合の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では Changed 機能 は「Changed 機能の用途を自動化管理の表示で確認する終端照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では SA z/OS の Changed 機能と INGKYST0I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では Changed 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Changes to Command Security {#c36-i1479}
*分類: 計画 / インストール*  ・  難易度: 上級

Changes to Command Securityは、Z System Automation (TSA)の計画 / インストールで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 探索照合の計画 インストールで Changes 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Changes 機能の出力を取らず探索照合の計画 インストールの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索照合で再確認できる形にする。 ✅
    - C. INGLIST を省略して探索照合の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では Changes 機能 は「探索照合の計画 インストールに関係する定義値と表示行を照合する探索照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では Changes 機能の属性行と INGKYST0I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では Changes 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索照合初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### Changes to Customization Dialog {#c36-i1480}
*分類: 計画 / インストール*  ・  難易度: 上級

Changes to Customization Dialogは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 上書照合の計画 インストールで自動化管理の運用確認を行います。Changes 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書照合の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書照合の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書照合の確認値として扱う。 ✅
    - D. Changes 機能の属性行を読まず上書照合の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では Changes 機能 は「SA z/OS で Changes 機能の扱いを記録する上書照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では Changes 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では Changes 機能の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### Cloning on z/OS Systems {#c36-i1481}
*分類: 計画 / インストール*  ・  難易度: 上級

Cloning on z/OS Systemsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 順序照合のCloning on z/OS Systemsで自動化管理の運用確認を行います。Cloning on z 属性の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序照合のCloning on z/OS Systemsを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序照合のCloning on z/OS Systemsを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序照合として引き継ぐ。 ✅
    - D. Cloning on z 属性の属性行を読まず順序照合のCloning on z/OS Systemsの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では Cloning on z 属性 は「SA z/OS で Cloning on z 属性の扱いを記録する順序照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では Cloning on z 属性の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では Cloning on z 属性の使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### Coexistence of SA z/OS 4.3 with Previous Releases {#c36-i1482}
*分類: 計画 / インストール*  ・  難易度: 上級

Coexistence of SA z/OS 4.3 with Previous Releasesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として Coexistence of SA z/OS 4.3 w を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 展開照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。展開照合権限で扱う Coexistence of SA z/OS 4.3 w は Z System Automation (TSA) の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として Coexistence of SA z/OS 4.3 w を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Commands {#c36-i1483}
*分類: 計画 / インストール*  ・  難易度: 上級

Commandsは、Z System Automation (TSA)の計画 / インストールで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 警告照合の計画 インストールに関係する Commandsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、警告照合の点検結果を残す。 ✅
    - B. Commandsの名称と担当者名のみを残して警告照合の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告照合の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告照合の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では Commands は「Commandsの用途を自動化管理の表示で確認する警告照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では SA z/OS の Commandsと INGKYST0I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では Commandsを Z System Automation (TSA)で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール



### Component Description {#c36-i1484}
*分類: 計画 / インストール*  ・  難易度: 上級

Component Descriptionは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール


### Configuring IBM Tivoli Netcool/OMNIbus {#c36-i1485}
*分類: 計画 / インストール*  ・  難易度: 上級

Configuring IBM Tivoli Netcool/OMNIbusは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査照合の計画 インストールで自動化管理の運用確認を行います。Configuring 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査照合の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査照合の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査照合の確認値として扱う。 ✅
    - D. Configuring 機能の属性行を読まず監査照合の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では Configuring 機能 は「SA z/OS で Configuring 機能の扱いを記録する監査照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では Configuring 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では Configuring 機能の使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Configuring SA z/OS Workstation Components {#c36-i1486}
*分類: 計画 / インストール*  ・  難易度: 上級

Configuring SA z/OS Workstation Componentsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力照合照合の出力照合として Configuring SA z/OS Workstat を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 名称と担当者名を保存して表示本文を確認しない。
    - D. 出力照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。出力照合照合で扱う Configuring SA z/OS Workstat は Z System Automation (TSA) の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として Configuring SA z/OS Workstat を扱い、分類内の確認名として保存します（出力照合照合終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Configuring Tivoli Service Request Manager through Tivoli Directory Integrator {#c36-i1487}
*分類: 計画 / インストール*  ・  難易度: 上級

Configuring Tivoli Service Request Manager through Tivoli Directory Integratorは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文追跡の計画 インストールに関係する Configuring 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を構文追跡で確認する。 ✅
    - B. Configuring 機能の名称と担当者名のみを残して構文追跡の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文追跡の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文追跡の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では Configuring 機能 は「Configuring 機能の用途を自動化管理の表示で確認する構文追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では SA z/OS の Configuring 機能と INGKYST0I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明のみに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では Configuring 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Continuous Enhancements (post-GA service-level) {#c36-i1488}
*分類: 計画 / インストール*  ・  難易度: 上級

Continuous Enhancements (post-GA service-level)は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 展開追跡の計画 インストールで Continuous 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Continuous 機能の出力を取らず展開追跡の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、展開追跡の証跡として残す。 ✅
    - C. INGLIST を省略して展開追跡の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では Continuous 機能 は「展開追跡の計画 インストールに関係する定義値と表示行を照合する展開追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では Continuous 機能の属性行と INGKYST0I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では Continuous 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール



### Controlling Access to the Processor Hardware Functions {#c36-i1489}
*分類: 計画 / インストール*  ・  難易度: 上級

Controlling Access to the Processor Hardware Functionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出追跡の計画 インストールで自動化管理の運用確認を行います。Controlling 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出追跡の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出追跡の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出追跡の確認記録にまとめる。 ✅
    - D. Controlling 機能の属性行を読まず呼出追跡の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では Controlling 機能 は「SA z/OS で Controlling 機能の扱いを記録する呼出追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では Controlling 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では Controlling 機能の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Defining Processor Operations Communications Links {#c36-i1490}
*分類: 計画 / インストール*  ・  難易度: 上級

Defining Processor Operations Communications Linksは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換追跡の計画 インストールに関する Defining 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換追跡の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の計画 インストールの証跡として保存して根拠にする。
    - C. Defining 機能の変更点を出力本文から切り離して置換追跡の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換追跡の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では Defining 機能 は「Defining 機能の状態と出力メッセージを結び付ける置換追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では Defining 機能の出力行と INGKYST0I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では Defining 機能を SA z/OS の確認記録に残し、対象名は置換追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Defining System Operations Connectivity {#c36-i1491}
*分類: 計画 / インストール*  ・  難易度: 上級

Defining System Operations Connectivityは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端追跡の計画 インストールに関係する Defining 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、終端追跡の結果として保存する。 ✅
    - B. Defining 機能の名称と担当者名のみを残して終端追跡の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端追跡の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端追跡の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では Defining 機能 は「Defining 機能の用途を自動化管理の表示で確認する終端追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では SA z/OS の Defining 機能と INGKYST0I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では Defining 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Establishing Authorization with Network Security Program {#c36-i1492}
*分類: 計画 / インストール*  ・  難易度: 上級

Establishing Authorization with Network Security Programは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索追跡の計画 インストールで Establishing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Establishing 機能の出力を取らず探索追跡の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、探索追跡の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して探索追跡の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では Establishing 機能 は「探索追跡の計画 インストールに関係する定義値と表示行を照合する探索追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では Establishing 機能の属性行と INGKYST0I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では Establishing 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Function levels {#c36-i1493}
*分類: 計画 / インストール*  ・  難易度: 上級

Function levelsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 上書追跡の計画 インストールで自動化管理の運用確認を行います。Function levelsの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書追跡の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書追跡の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書追跡として引き継ぐ。 ✅
    - D. Function levelsの属性行を読まず上書追跡の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では Function levels は「SA z/OS で Function levelsの扱いを記録する上書追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では Function levelsの表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では Function levelsの使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Further Processor Operations Names {#c36-i1494}
*分類: 計画 / インストール*  ・  難易度: 上級

Further Processor Operations Namesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 出力追跡の計画 インストールに関する Further 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力追跡の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の計画 インストールの証跡として保存して根拠にする。
    - C. Further 機能の変更点を出力本文から切り離して出力追跡の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力追跡の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では Further 機能 は「Further 機能の状態と出力メッセージを結び付ける出力追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では Further 機能の出力行と INGKYST0I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では Further 機能を SA z/OS の確認記録に残し、対象名は出力追跡対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### Granting NetView and the STC-User Access to Data Sets {#c36-i1495}
*分類: 計画 / インストール*  ・  難易度: 上級

Granting NetView and the STC-User Access to Data Setsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件追跡の計画 インストールに関係する Granting 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、条件追跡の点検結果を残す。 ✅
    - B. Granting 機能の名称と担当者名のみを残して条件追跡の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件追跡の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件追跡の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では Granting 機能 は「Granting 機能の用途を自動化管理の表示で確認する条件追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では SA z/OS の Granting 機能と INGKYST0I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では Granting 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Hardware Management Console characteristics {#c36-i1496}
*分類: 計画 / インストール*  ・  難易度: 上級

Hardware Management Console characteristicsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 区切追跡の計画 インストールで Hardware 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Hardware 機能の出力を取らず区切追跡の計画 インストールの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切追跡で再確認できる形にする。 ✅
    - C. INGLIST を省略して区切追跡の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では Hardware 機能 は「区切追跡の計画 インストールに関係する定義値と表示行を照合する区切追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では Hardware 機能の属性行と INGKYST0I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では Hardware 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Hardware Requirements {#c36-i1497}
*分類: 計画 / インストール*  ・  難易度: 上級

Hardware Requirementsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 範囲追跡の計画 インストールで自動化管理の運用確認を行います。Hardware 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲追跡の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲追跡の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲追跡の確認値として扱う。 ✅
    - D. Hardware 機能の属性行を読まず範囲追跡の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では Hardware 機能 は「SA z/OS で Hardware 機能の扱いを記録する範囲追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では Hardware 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では Hardware 機能の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### How HMC Integrated Console Tasks impact System Console Message Automation {#c36-i1498}
*分類: 計画 / インストール*  ・  難易度: 上級

How HMC Integrated Console Tasks impact System Console Message Automationは、Z System Automation (TSA)の計画 / インストールでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 優先追跡の計画 インストールに関する How 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先追跡の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の計画 インストールの証跡として保存して根拠にする。
    - C. How 機能の変更点を出力本文から切り離して優先追跡の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先追跡の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では How 機能 は「How 機能の状態と出力メッセージを結び付ける優先追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では How 機能の出力行と INGKYST0I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では How 機能を SA z/OS の確認記録に残し、対象名は優先追跡対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### IBM Z SNMP Application Programming Interface {#c36-i1499}
*分類: 計画 / インストール*  ・  難易度: 上級

IBM Z SNMP Application Programming Interfaceは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 記録追跡の計画 インストールに関係する IBM 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を記録追跡で確認する。 ✅
    - B. IBM 機能の名称と担当者名のみを残して記録追跡の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録追跡の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録追跡の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では IBM 機能 は「IBM 機能の用途を自動化管理の表示で確認する記録追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では SA z/OS の IBM 機能と INGKYST0I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では IBM 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### INGDLG Command {#c36-i1500}
*分類: 計画 / インストール*  ・  難易度: 上級

INGDLG Commandは、Z System Automation (TSA)の計画 / インストールで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 比較追跡の計画 インストールで INGDLG Commandの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. INGDLG Commandの出力を取らず比較追跡の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、比較追跡の証跡として残す。 ✅
    - C. INGLIST を省略して比較追跡の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では INGDLG Command は「比較追跡の計画 インストールに関係する定義値と表示行を照合する比較追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では INGDLG Commandの属性行と INGKYST0I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では INGDLG Commandを Z System Automation (TSA)の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### INTERNAL (BCPii Base Control Program Internal Interface) {#c36-i1501}
*分類: 計画 / インストール*  ・  難易度: 上級

INTERNAL (BCPii Base Control Program Internal Interface)は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 変更追跡の計画 インストールに関する INTERNAL 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更追跡の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡の計画 インストールの証跡として保存して根拠にする。
    - C. INTERNAL 属性の変更点を出力本文から切り離して変更追跡の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更追跡の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では INTERNAL 属性 は「INTERNAL 属性の状態と出力メッセージを結び付ける変更追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では INTERNAL 属性の出力行と INGKYST0I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では INTERNAL 属性を SA z/OS の確認記録に残し、対象名は変更追跡対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### IP Stack Considerations {#c36-i1502}
*分類: 計画 / インストール*  ・  難易度: 上級

IP Stack Considerationsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 展開検査の計画 インストールで IP 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IP 機能の出力を取らず展開検査の計画 インストールの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開検査で再確認できる形にする。 ✅
    - C. INGLIST を省略して展開検査の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では IP 機能 は「展開検査の計画 インストールに関係する定義値と表示行を照合する展開検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では IP 機能の属性行と INGKYST0I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では IP 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開検査初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Installation and Configuration {#c36-i1503}
*分類: 計画 / インストール*  ・  難易度: 上級

Installation and Configurationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Integration by User-defined Alert Handler {#c36-i1504}
*分類: 計画 / インストール*  ・  難易度: 上級

Integration by User-defined Alert Handlerは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域追跡の計画 インストールに関する Integration 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域追跡の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡の計画 インストールの証跡として保存して根拠にする。
    - C. Integration 機能の変更点を出力本文から切り離して値域追跡の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域追跡の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では Integration 機能 は「Integration 機能の状態と出力メッセージを結び付ける値域追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では Integration 機能の出力行と INGKYST0I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では Integration 機能を SA z/OS の確認記録に残し、対象名は値域追跡対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Integration via EIF Events {#c36-i1505}
*分類: 計画 / インストール*  ・  難易度: 上級

Integration via EIF Eventsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 警告追跡の計画 インストールに関係する Integration 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、警告追跡の結果として保存する。 ✅
    - B. Integration 機能の名称と担当者名のみを残して警告追跡の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告追跡の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告追跡の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では Integration 機能 は「Integration 機能の用途を自動化管理の表示で確認する警告追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では SA z/OS の Integration 機能と INGKYST0I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では Integration 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Integration via SA IOM Peer-To-Peer Protocol {#c36-i1506}
*分類: 計画 / インストール*  ・  難易度: 上級

Integration via SA IOM Peer-To-Peer Protocolは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 復旧追跡の計画 インストールで Integration 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Integration 機能の出力を取らず復旧追跡の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、復旧追跡の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して復旧追跡の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では Integration 機能 は「復旧追跡の計画 インストールに関係する定義値と表示行を照合する復旧追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では Integration 機能の属性行と INGKYST0I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では Integration 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Integration via Trouble Ticket Information XML {#c36-i1507}
*分類: 計画 / インストール*  ・  難易度: 上級

Integration via Trouble Ticket Information XMLは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.87) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 監査追跡の計画 インストールで自動化管理の運用確認を行います。Integration 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査追跡の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査追跡の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、監査追跡として引き継ぐ。 ✅
    - D. Integration 機能の属性行を読まず監査追跡の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では Integration 機能 は「SA z/OS で Integration 機能の扱いを記録する監査追跡項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では Integration 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では Integration 機能の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.87) / OS 計画およびインストール



### Introduction of Alert Notification by SA z/OS {#c36-i1508}
*分類: 計画 / インストール*  ・  難易度: 上級

Introduction of Alert Notification by SA z/OSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文検査の計画 インストールに関係する Introduction 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、構文検査の点検結果を残す。 ✅
    - B. Introduction 機能の名称と担当者名のみを残して構文検査の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文検査の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文検査の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では Introduction 機能 は「Introduction 機能の用途を自動化管理の表示で確認する構文検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では SA z/OS の Introduction 機能と INGKYST0I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では Introduction 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Limiting the Number of z/OS IPL Messages Displayed on CI {#c36-i1509}
*分類: 計画 / インストール*  ・  難易度: 上級

Limiting the Number of z/OS IPL Messages Displayed on CIは、Z System Automation (TSA)の計画 / インストールでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出検査の計画 インストールで自動化管理の運用確認を行います。Limiting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出検査の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出検査の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出検査の確認値として扱う。 ✅
    - D. Limiting 機能の属性行を読まず呼出検査の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では Limiting 機能 は「SA z/OS で Limiting 機能の扱いを記録する呼出検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では Limiting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では Limiting 機能の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Managing IBM Z console availability exceptions {#c36-i1510}
*分類: 計画 / インストール*  ・  難易度: 上級

Managing IBM Z console availability exceptionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換検査の計画 インストールに関する Managing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換検査の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の計画 インストールの証跡として保存して根拠にする。
    - C. Managing 機能の変更点を出力本文から切り離して置換検査の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では Managing 機能 は「Managing 機能の状態と出力メッセージを結び付ける置換検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では Managing 機能の出力行と INGKYST0I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では Managing 機能を SA z/OS の確認記録に残し、対象名は置換検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Message Delivery Considerations {#c36-i1511}
*分類: 計画 / インストール*  ・  難易度: 上級

Message Delivery Considerationsは、Z System Automation (TSA)の計画 / インストールでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 終端検査の計画 インストールに関係する Message 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を終端検査で確認する。 ✅
    - B. Message 機能の名称と担当者名のみを残して終端検査の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端検査の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端検査の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では Message 機能 は「Message 機能の用途を自動化管理の表示で確認する終端検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では SA z/OS の Message 機能と INGKYST0I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では Message 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### Migrating from LPAR Management to ProcOps {#c36-i1512}
*分類: 計画 / インストール*  ・  難易度: 上級

Migrating from LPAR Management to ProcOpsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索検査の計画 インストールで Migrating 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Migrating 機能の出力を取らず探索検査の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、探索検査の証跡として残す。 ✅
    - C. INGLIST を省略して探索検査の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では Migrating 機能 は「探索検査の計画 インストールに関係する定義値と表示行を照合する探索検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では Migrating 機能の属性行と INGKYST0I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では Migrating 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Migration Information {#c36-i1513}
*分類: 計画 / インストール*  ・  難易度: 上級

Migration Informationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.87) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 上書検査の計画 インストールで自動化管理の運用確認を行います。Migration 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書検査の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書検査の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書検査の確認記録にまとめる。 ✅
    - D. Migration 機能の属性行を読まず上書検査の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では Migration 機能 は「SA z/OS で Migration 機能の扱いを記録する上書検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では Migration 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では Migration 機能の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.87) / OS 計画およびインストール



### Migration Notes and Advice when Migrating from SA z/OS 4.1 {#c36-i1514}
*分類: 計画 / インストール*  ・  難易度: 上級

Migration Notes and Advice when Migrating from SA z/OS 4.1は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力検査の計画 インストールに関する Migration 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力検査の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の計画 インストールの証跡として保存して根拠にする。
    - C. Migration 機能の変更点を出力本文から切り離して出力検査の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では Migration 機能 は「Migration 機能の状態と出力メッセージを結び付ける出力検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では Migration 機能の出力行と INGKYST0I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では Migration 機能を SA z/OS の確認記録に残し、対象名は出力検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Migration Notes and Advice when Migrating to SA z/OS 4.3 {#c36-i1515}
*分類: 計画 / インストール*  ・  難易度: 上級

Migration Notes and Advice when Migrating to SA z/OS 4.3は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件検査の計画 インストールに関係する Migration 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、条件検査の結果として保存する。 ✅
    - B. Migration 機能の名称と担当者名のみを残して条件検査の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件検査の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件検査の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では Migration 機能 は「Migration 機能の用途を自動化管理の表示で確認する条件検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では SA z/OS の Migration 機能と INGKYST0I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では Migration 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Migration Steps to SA z/OS 4.3 {#c36-i1516}
*分類: 計画 / インストール*  ・  難易度: 上級

Migration Steps to SA z/OS 4.3は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切検査のMigration Steps to SA z/OS 4.3で Migration 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Migration 機能の出力を取らず区切検査のMigration Steps to SA z/OS 4.3の説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、区切検査の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して区切検査のMigration Steps to SA z/OS 4.3の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のMigration Steps to SA z/OS 4.3へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では Migration 機能 は「区切検査のMigration Steps to SA z/OS 4.3に関係する定義値と表示行を照合する区切検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では Migration 機能の属性行と INGKYST0I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では Migration 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Miscellaneous {#c36-i1517}
*分類: 計画 / インストール*  ・  難易度: 上級

Miscellaneousは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 範囲検査の計画 インストールで自動化管理の運用確認を行います。Miscellaneousの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲検査の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲検査の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲検査として引き継ぐ。 ✅
    - D. Miscellaneousの属性行を読まず範囲検査の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では Miscellaneous は「SA z/OS で Miscellaneousの扱いを記録する範囲検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では Miscellaneousの表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では Miscellaneousの使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Naming Conventions {#c36-i1518}
*分類: 計画 / インストール*  ・  難易度: 上級

Naming Conventionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 優先検査の計画 インストールに関する Naming Conventionsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先検査の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の計画 インストールの証跡として保存して根拠にする。
    - C. Naming Conventionsの変更点を出力本文から切り離して優先検査の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先検査の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では Naming Conventions は「Naming Conventionsの状態と出力メッセージを結び付ける優先検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では Naming Conventionsの出力行と INGKYST0I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では Naming Conventionsを SA z/OS の確認記録に残し、対象名は優先検査対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### Network Dependencies {#c36-i1519}
*分類: 計画 / インストール*  ・  難易度: 上級

Network Dependenciesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 記録検査の計画 インストールに関係する Network 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、記録検査の点検結果を残す。 ✅
    - B. Network 機能の名称と担当者名のみを残して記録検査の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録検査の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録検査の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では Network 機能 は「Network 機能の用途を自動化管理の表示で確認する記録検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では SA z/OS の Network 機能と INGKYST0I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では Network 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Notes on Terminology {#c36-i1520}
*分類: 計画 / インストール*  ・  難易度: 上級

Notes on Terminologyは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### OS Message Format Support with ProcOps/BCPii {#c36-i1521}
*分類: 計画 / インストール*  ・  難易度: 上級

OS Message Format Support with ProcOps/BCPiiは、Z System Automation (TSA)の計画 / インストールでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 値域検査の計画 インストールに関する OS 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域検査の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の計画 インストールの証跡として保存して根拠にする。
    - C. OS 機能の変更点を出力本文から切り離して値域検査の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域検査の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では OS 機能 は「OS 機能の状態と出力メッセージを結び付ける値域検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では OS 機能の出力行と INGKYST0I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では OS 機能を SA z/OS の確認記録に残し、対象名は値域検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Operators {#c36-i1522}
*分類: 計画 / インストール*  ・  難易度: 上級

Operatorsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 順序検査の計画 インストールで自動化管理の運用確認を行います。Operatorsの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序検査の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序検査の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序検査の確認値として扱う。 ✅
    - D. Operatorsの属性行を読まず順序検査の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では Operators は「SA z/OS で Operatorsの扱いを記録する順序検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では Operatorsの表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では Operatorsの使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Other Security Options {#c36-i1523}
*分類: 計画 / インストール*  ・  難易度: 上級

Other Security Optionsは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 警告検査の計画 インストールに関係する Other 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を警告検査で確認する。 ✅
    - B. Other 機能の名称と担当者名のみを残して警告検査の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告検査の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告検査の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では Other 機能 は「Other 機能の用途を自動化管理の表示で確認する警告検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では SA z/OS の Other 機能と INGKYST0I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では Other 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### Overview of Configuration Tasks {#c36-i1524}
*分類: 計画 / インストール*  ・  難易度: 上級

Overview of Configuration Tasksは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧検査の計画 インストールで Overview 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Overview 機能の出力を取らず復旧検査の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、復旧検査の証跡として残す。 ✅
    - C. INGLIST を省略して復旧検査の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では Overview 機能 は「復旧検査の計画 インストールに関係する定義値と表示行を照合する復旧検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では Overview 機能の属性行と INGKYST0I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では Overview 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning {#c36-i1525}
*分類: 計画 / インストール*  ・  難易度: 上級

Planningは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール


### Planning Processor Operations Connections {#c36-i1526}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning Processor Operations Connectionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索判定の計画 インストールで Planning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning 機能の出力を取らず探索判定の計画 インストールの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索判定で再確認できる形にする。 ✅
    - C. INGLIST を省略して探索判定の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では Planning 機能 は「探索判定の計画 インストールに関係する定義値と表示行を照合する探索判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では Planning 機能の属性行と INGKYST0I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では Planning 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索判定初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning automation routines to handle suspend and resume {#c36-i1527}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning automation routines to handle suspend and resumeは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更検査の計画 インストールに関する Planning 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更検査の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の計画 インストールの証跡として保存して根拠にする。
    - C. Planning 機能の変更点を出力本文から切り離して変更検査の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では Planning 機能 は「Planning 機能の状態と出力メッセージを結び付ける変更検査項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では Planning 機能の出力行と INGKYST0I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では Planning 機能を SA z/OS の確認記録に残し、対象名は変更検査対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning for Automation Connectivity {#c36-i1528}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning for Automation Connectivityは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文判定の計画 インストールに関係する Planning 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、構文判定の結果として保存する。 ✅
    - B. Planning 機能の名称と担当者名のみを残して構文判定の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文判定の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文判定の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では Planning 機能 は「Planning 機能の用途を自動化管理の表示で確認する構文判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では SA z/OS の Planning 機能と INGKYST0I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では Planning 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning for Integration with IBM Tivoli Monitoring {#c36-i1529}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning for Integration with IBM Tivoli Monitoringは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 展開判定の計画 インストールで Planning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning 機能の出力を取らず展開判定の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、展開判定の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して展開判定の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では Planning 機能 は「展開判定の計画 インストールに関係する定義値と表示行を照合する展開判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では Planning 機能の属性行と INGKYST0I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では Planning 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開判定初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning for Looping Address Space Suppression {#c36-i1530}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning for Looping Address Space Suppressionは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換判定の計画 インストールに関する Planning 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換判定の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定の計画 インストールの証跡として保存して根拠にする。
    - C. Planning 機能の変更点を出力本文から切り離して置換判定の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換判定の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では Planning 機能 は「Planning 機能の状態と出力メッセージを結び付ける置換判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では Planning 機能の出力行と INGKYST0I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では Planning 機能を SA z/OS の確認記録に残し、対象名は置換判定対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning for SOAP over HTTPS {#c36-i1531}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning for SOAP over HTTPSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端判定の計画 インストールに関係する Planning 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、終端判定の点検結果を残す。 ✅
    - B. Planning 機能の名称と担当者名のみを残して終端判定の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端判定の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端判定の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では Planning 機能 は「Planning 機能の用途を自動化管理の表示で確認する終端判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では SA z/OS の Planning 機能と INGKYST0I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では Planning 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning for longer console outages {#c36-i1532}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning for longer console outagesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出判定の計画 インストールで自動化管理の運用確認を行います。Planning 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出判定の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出判定の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出判定として引き継ぐ。 ✅
    - D. Planning 機能の属性行を読まず呼出判定の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では Planning 機能 は「SA z/OS で Planning 機能の扱いを記録する呼出判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では Planning 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では Planning 機能の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning the Hardware Interfaces {#c36-i1533}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning the Hardware Interfacesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書判定の計画 インストールで自動化管理の運用確認を行います。Planning 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書判定の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書判定の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書判定の確認値として扱う。 ✅
    - D. Planning 機能の属性行を読まず上書判定の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では Planning 機能 は「SA z/OS で Planning 機能の扱いを記録する上書判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では Planning 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では Planning 機能の使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning to Install Alert Notification by SA z/OS {#c36-i1534}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning to Install Alert Notification by SA z/OSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件判定の計画 インストールに関係する Planning 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を条件判定で確認する。 ✅
    - B. Planning 機能の名称と担当者名のみを残して条件判定の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件判定の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件判定の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では Planning 機能 は「Planning 機能の用途を自動化管理の表示で確認する条件判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では SA z/OS の Planning 機能と INGKYST0I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では Planning 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning to Install SA z/OS on Host Systems {#c36-i1535}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning to Install SA z/OS on Host Systemsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切判定の計画 インストールで Planning 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning 機能の出力を取らず区切判定の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、区切判定の証跡として残す。 ✅
    - C. INGLIST を省略して区切判定の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では Planning 機能 は「区切判定の計画 インストールに関係する定義値と表示行を照合する区切判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では Planning 機能の属性行と INGKYST0I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では Planning 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切判定初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Planning to choose feasible CPC names {#c36-i1536}
*分類: 計画 / インストール*  ・  難易度: 上級

Planning to choose feasible CPC namesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力判定の計画 インストールに関する Planning 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力判定の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の計画 インストールの証跡として保存して根拠にする。
    - C. Planning 機能の変更点を出力本文から切り離して出力判定の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて出力判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では Planning 機能 は「Planning 機能の状態と出力メッセージを結び付ける出力判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では Planning 機能の出力行と INGKYST0I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明のみに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では Planning 機能を SA z/OS の確認記録に残し、対象名は出力判定対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Post SMP/E Steps {#c36-i1537}
*分類: 計画 / インストール*  ・  難易度: 上級

Post SMP/E Stepsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 範囲判定のPost SMP/E Stepsで自動化管理の運用確認を行います。Post SMP ・ E Stepsの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲判定のPost SMP/E Stepsを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲判定のPost SMP/E Stepsを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、範囲判定の確認記録にまとめる。 ✅
    - D. Post SMP ・ E Stepsの属性行を読まず範囲判定のPost SMP/E Stepsの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では Post SMP ・ E Steps は「SA z/OS で Post SMP ・ E Stepsの扱いを記録する範囲判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では Post SMP ・ E Stepsの表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では Post SMP ・ E Stepsの使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### Preparing to Configure System Automation {#c36-i1538}
*分類: 計画 / インストール*  ・  難易度: 上級

Preparing to Configure System Automationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### ProcOps SNMP Sessions {#c36-i1539}
*分類: 計画 / インストール*  ・  難易度: 上級

ProcOps SNMP Sessionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 記録判定の計画 インストールに関係する ProcOps 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、記録判定の結果として保存する。 ✅
    - B. ProcOps 機能の名称と担当者名のみを残して記録判定の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録判定の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録判定の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では ProcOps 機能 は「ProcOps 機能の用途を自動化管理の表示で確認する記録判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では SA z/OS の ProcOps 機能と INGKYST0I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では ProcOps 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### REXX Considerations {#c36-i1540}
*分類: 計画 / インストール*  ・  難易度: 上級

REXX Considerationsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 構文整理の計画 インストールに関係する REXX 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を構文整理で確認する。 ✅
    - B. REXX 機能の名称と担当者名のみを残して構文整理の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文整理の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文整理の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では REXX 機能 は「REXX 機能の用途を自動化管理の表示で確認する構文整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では SA z/OS の REXX 機能と INGKYST0I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では REXX 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Recommended z/OS Console Settings for CI Usage with SA z/OS {#c36-i1541}
*分類: 計画 / インストール*  ・  難易度: 上級

Recommended z/OS Console Settings for CI Usage with SA z/OSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 属性照合通知の属性照合として Recommended z/OS Console Set を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 承認欄の記入を優先して出力メッセージを保存しない。
    - B. 属性照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 名称と担当者名を保存して表示本文を確認しない。
    - D. 別分類の結果を流用して同じ証跡として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。属性照合通知で扱う Recommended z/OS Console Set は Z System Automation (TSA) の確認対象です（属性照合通知用語）。属性照合通知の担当者は属性照合として、表示本文とメッセージを照合します（属性照合通知照合）。属性照合通知の対応を残すと、後続担当者は同じ出典に戻って確認できます（属性照合通知出典）。A: 属性照合通知で表示とメッセージを結ぶ場合に根拠になります（属性照合通知A）。B: 属性照合通知で定義と出力の関係がない場合は追跡できません（属性照合通知B）。C: 属性照合通知で出典名のみでは実際の表示を説明できません（属性照合通知C）。D: 属性照合通知で操作記録のみでは値や状態の確認が不足します（属性照合通知D）。属性照合通知の初出用語として Recommended z/OS Console Set を扱い、分類内の確認名として保存します（属性照合通知終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Related Information {#c36-i1542}
*分類: 計画 / インストール*  ・  難易度: 上級

Related Informationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 順序判定の計画 インストールで自動化管理の運用確認を行います。Related 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序判定の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序判定の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、順序判定として引き継ぐ。 ✅
    - D. Related 機能の属性行を読まず順序判定の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では Related 機能 は「SA z/OS で Related 機能の扱いを記録する順序判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では Related 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では Related 機能の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Requesting CEEDUMPs and DYNDUMPs {#c36-i1543}
*分類: 計画 / インストール*  ・  難易度: 上級

Requesting CEEDUMPs and DYNDUMPsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 値域判定の計画 インストールに関する Requesting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域判定の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の計画 インストールの証跡として保存して根拠にする。
    - C. Requesting 機能の変更点を出力本文から切り離して値域判定の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、値域判定の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では Requesting 機能 は「Requesting 機能の状態と出力メッセージを結び付ける値域判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では Requesting 機能の出力行と INGKYST0I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では Requesting 機能を SA z/OS の確認記録に残し、対象名は値域判定対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Resources {#c36-i1544}
*分類: 計画 / インストール*  ・  難易度: 上級

Resourcesは、Z System Automation (TSA)の計画 / インストールでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール


### Restricting Access to Change PDB Activity Log Options {#c36-i1545}
*分類: 計画 / インストール*  ・  難易度: 上級

Restricting Access to Change PDB Activity Log Optionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧判定の計画 インストールで Restricting 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Restricting 機能の出力を取らず復旧判定の計画 インストールの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、復旧判定で再確認できる形にする。 ✅
    - C. INGLIST を省略して復旧判定の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では Restricting 機能 は「復旧判定の計画 インストールに関係する定義値と表示行を照合する復旧判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では Restricting 機能の属性行と INGKYST0I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では Restricting 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Restricting Access to INGPLEX and INGCF Functions {#c36-i1546}
*分類: 計画 / インストール*  ・  難易度: 上級

Restricting Access to INGPLEX and INGCF Functionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査判定の計画 インストールで自動化管理の運用確認を行います。Restricting 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査判定の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査判定の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査判定の確認値として扱う。 ✅
    - D. Restricting 機能の属性行を読まず監査判定の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Restricting 機能 は「SA z/OS で Restricting 機能の扱いを記録する監査判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Restricting 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Restricting 機能の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Restricting Access to Joblog Monitoring Task INGTJLM {#c36-i1547}
*分類: 計画 / インストール*  ・  難易度: 上級

Restricting Access to Joblog Monitoring Task INGTJLMは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更判定の計画 インストールに関する Restricting 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更判定の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定の計画 インストールの証跡として保存して根拠にする。
    - C. Restricting 機能の変更点を出力本文から切り離して変更判定の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更判定の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では Restricting 機能 は「Restricting 機能の状態と出力メッセージを結び付ける変更判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では Restricting 機能の出力行と INGKYST0I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では Restricting 機能を SA z/OS の確認記録に残し、対象名は変更判定対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Roles {#c36-i1548}
*分類: 計画 / インストール*  ・  難易度: 上級

Rolesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 展開整理の計画 インストールで Rolesの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Rolesの出力を取らず展開整理の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、展開整理の証跡として残す。 ✅
    - C. INGLIST を省略して展開整理の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では Roles は「展開整理の計画 インストールに関係する定義値と表示行を照合する展開整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では Rolesの属性行と INGKYST0I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では Rolesを Z System Automation (TSA)の運用手順で確認し、初出名は展開整理初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Running with the z/OS System Console Deactivated {#c36-i1549}
*分類: 計画 / インストール*  ・  難易度: 上級

Running with the z/OS System Console Deactivatedは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲照合入力の範囲照合として Running with the z/OS System を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 範囲照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。範囲照合入力で扱う Running with the z/OS System は Z System Automation (TSA) の確認対象です（範囲照合入力用語）。範囲照合入力の担当者は範囲照合として、表示本文とメッセージを照合します（範囲照合入力照合）。範囲照合入力の対応を残すと、後続担当者は同じ出典に戻って確認できます（範囲照合入力出典）。A: 範囲照合入力で表示とメッセージを結ぶ場合に根拠になります（範囲照合入力A）。B: 範囲照合入力で定義と出力の関係がない場合は追跡できません（範囲照合入力B）。C: 範囲照合入力で出典名のみでは実際の表示を説明できません（範囲照合入力C）。D: 範囲照合入力で操作記録のみでは値や状態の確認が不足します（範囲照合入力D）。範囲照合入力の初出用語として Running with the z/OS System を扱い、分類内の確認名として保存します（範囲照合入力終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### SA z/OS Components {#c36-i1550}
*分類: 計画 / インストール*  ・  難易度: 上級

SA z/OS Componentsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 終端整理のSA z/OS Componentsに関係する SA z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、終端整理の結果として保存する。 ✅
    - B. SA z 属性の名称と担当者名のみを残して終端整理のSA z/OS Componentsの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端整理のSA z/OS Componentsを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端整理のSA z/OS Componentsの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では SA z 属性 は「SA z 属性の用途を自動化管理の表示で確認する終端整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では SA z/OS の SA z 属性と INGKYST0I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では SA z 属性を Z System Automation (TSA)で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### SA z/OS Hardware Interface: Important Considerations {#c36-i1551}
*分類: 計画 / インストール*  ・  難易度: 上級

SA z/OS Hardware Interface: Important Considerationsは、SA z/OS Hardware Interface: Important Considerations は 計画/インストール の項目

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 記録照合識別の記録照合として SA z/OS Hardware Interface:  を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 記録照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。記録照合識別で扱う SA z/OS Hardware Interface:  は Z System Automation (TSA) の確認対象です（記録照合識別用語）。記録照合識別の担当者は記録照合として、表示本文とメッセージを照合します（記録照合識別照合）。記録照合識別の対応を残すと、後続担当者は同じ出典に戻って確認できます（記録照合識別出典）。A: 記録照合識別で表示とメッセージを結ぶ場合に根拠になります（記録照合識別A）。B: 記録照合識別で定義と出力の関係がない場合は追跡できません（記録照合識別B）。C: 記録照合識別で出典名のみでは実際の表示を説明できません（記録照合識別C）。D: 記録照合識別で操作記録のみでは値や状態の確認が不足します（記録照合識別D）。記録照合識別の初出用語として SA z/OS Hardware Interface:  を扱い、分類内の確認名として保存します（記録照合識別終点）。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### SA z/OS Prerequisites and Supported Equipment {#c36-i1552}
*分類: 計画 / インストール*  ・  難易度: 上級

SA z/OS Prerequisites and Supported Equipmentは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更照合更新の変更照合として SA z/OS Prerequisites and Su を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 変更照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。変更照合更新で扱う SA z/OS Prerequisites and Su は Z System Automation (TSA) の確認対象です（変更照合更新用語）。変更照合更新の担当者は変更照合として、表示本文とメッセージを照合します（変更照合更新照合）。変更照合更新の対応を残すと、後続担当者は同じ出典に戻って確認できます（変更照合更新出典）。A: 変更照合更新で表示とメッセージを結ぶ場合に根拠になります（変更照合更新A）。B: 変更照合更新で定義と出力の関係がない場合は追跡できません（変更照合更新B）。C: 変更照合更新で出典名のみでは実際の表示を説明できません（変更照合更新C）。D: 変更照合更新で操作記録のみでは値や状態の確認が不足します（変更照合更新D）。変更照合更新の初出用語として SA z/OS Prerequisites and Su を扱い、分類内の確認名として保存します（変更照合更新終点）。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### SA z/OS Processor Operations (ProcOps) {#c36-i1553}
*分類: 計画 / インストール*  ・  難易度: 上級

SA z/OS Processor Operations (ProcOps)は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 値域照合条件の値域照合として SA z/OS Processor Operations を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 承認欄の記入を優先して出力メッセージを保存しない。
    - B. 名称と担当者名を保存して表示本文を確認しない。
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 値域照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。値域照合条件で扱う SA z/OS Processor Operations は Z System Automation (TSA) の確認対象です（値域照合条件用語）。値域照合条件の担当者は値域照合として、表示本文とメッセージを照合します（値域照合条件照合）。値域照合条件の対応を残すと、後続担当者は同じ出典に戻って確認できます（値域照合条件出典）。A: 値域照合条件で表示とメッセージを結ぶ場合に根拠になります（値域照合条件A）。B: 値域照合条件で定義と出力の関係がない場合は追跡できません（値域照合条件B）。C: 値域照合条件で出典名のみでは実際の表示を説明できません（値域照合条件C）。D: 値域照合条件で操作記録のみでは値や状態の確認が不足します（値域照合条件D）。値域照合条件の初出用語として SA z/OS Processor Operations を扱い、分類内の確認名として保存します（値域照合条件終点）。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### SA z/OS System Names {#c36-i1554}
*分類: 計画 / インストール*  ・  難易度: 上級

SA z/OS System Namesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 条件整理のSA z/OS System Namesに関係する SA z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、条件整理の点検結果を残す。 ✅
    - B. SA z 属性の名称と担当者名のみを残して条件整理のSA z/OS System Namesの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件整理のSA z/OS System Namesを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件整理のSA z/OS System Namesの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では SA z 属性 は「SA z 属性の用途を自動化管理の表示で確認する条件整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では SA z/OS の SA z 属性と INGKYST0I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では SA z 属性を Z System Automation (TSA)で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### SA z/OS and Sysplex Hardware {#c36-i1555}
*分類: 計画 / インストール*  ・  難易度: 上級

SA z/OS and Sysplex Hardwareは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換整理のSA z/OS and Sysplex Hardwareに関する SA z 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換整理のSA z/OS and Sysplex Hardwareの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理のSA z/OS and Sysplex Hardwareの証跡として保存して根拠にする。
    - C. SA z 属性の変更点を出力本文から切り離して置換整理のSA z/OS and Sysplex Hardwareの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では SA z 属性 は「SA z 属性の状態と出力メッセージを結び付ける置換整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では SA z 属性の出力行と INGKYST0I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では SA z 属性を SA z/OS の確認記録に残し、対象名は置換整理対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### SMP/E Installation {#c36-i1556}
*分類: 計画 / インストール*  ・  難易度: 上級

SMP/E Installationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 値域整理のSMP/E Installationに関する SMP 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域整理のSMP/E Installationの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域整理のSMP/E Installationの証跡として保存して根拠にする。
    - C. SMP 属性の変更点を出力本文から切り離して値域整理のSMP/E Installationの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて値域整理の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では SMP 属性 は「SMP 属性の状態と出力メッセージを結び付ける値域整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では SMP 属性の出力行と INGKYST0I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明のみに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では SMP 属性を SA z/OS の確認記録に残し、対象名は値域整理対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.65) / OS 計画およびインストール



### SNMP {#c36-i1557}
*分類: 計画 / インストール*  ・  難易度: 上級

SNMPは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 警告整理の計画 インストールに関係する SNMP の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、警告整理の結果として保存する。 ✅
    - B. SNMP の名称と担当者名のみを残して警告整理の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告整理の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告整理の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では SNMP は「SNMP の用途を自動化管理の表示で確認する警告整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では SA z/OS の SNMP と INGKYST0I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明のみに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では SNMP を Z System Automation (TSA)で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Securing Focal Point Systems and Target Systems {#c36-i1558}
*分類: 計画 / インストール*  ・  難易度: 上級

Securing Focal Point Systems and Target Systemsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切整理の計画 インストールで Securing 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Securing 機能の出力を取らず区切整理の計画 インストールの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切整理で再確認できる形にする。 ✅
    - C. INGLIST を省略して区切整理の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では Securing 機能 は「区切整理の計画 インストールに関係する定義値と表示行を照合する区切整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では Securing 機能の属性行と INGKYST0I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では Securing 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切整理初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Securing the Policy Services Provider {#c36-i1559}
*分類: 計画 / インストール*  ・  難易度: 上級

Securing the Policy Services Providerは、Z System Automation (TSA)の計画 / インストールでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲整理の計画 インストールで自動化管理の運用確認を行います。Securing 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲整理の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲整理の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲整理の確認値として扱う。 ✅
    - D. Securing 機能の属性行を読まず範囲整理の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では Securing 機能 は「SA z/OS で Securing 機能の扱いを記録する範囲整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では Securing 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では Securing 機能の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Security and Authorization {#c36-i1560}
*分類: 計画 / インストール*  ・  難易度: 上級

Security and Authorizationは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 優先整理の計画 インストールに関する Security 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先整理の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理の計画 インストールの証跡として保存して根拠にする。
    - C. Security 機能の変更点を出力本文から切り離して優先整理の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先整理の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では Security 機能 は「Security 機能の状態と出力メッセージを結び付ける優先整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では Security 機能の出力行と INGKYST0I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では Security 機能を SA z/OS の確認記録に残し、対象名は優先整理対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Security considerations to control Db2 subsystems {#c36-i1561}
*分類: 計画 / インストール*  ・  難易度: 上級

Security considerations to control Db2 subsystemsは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録整理の計画 インストールに関係する Security 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を記録整理で確認する。 ✅
    - B. Security 機能の名称と担当者名のみを残して記録整理の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録整理の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録整理の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では Security 機能 は「Security 機能の用途を自動化管理の表示で確認する記録整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では SA z/OS の Security 機能と INGKYST0I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では Security 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Security for IBM Tivoli Monitoring Products {#c36-i1562}
*分類: 計画 / インストール*  ・  難易度: 上級

Security for IBM Tivoli Monitoring Productsは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 比較整理の計画 インストールで Security 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Security 機能の出力を取らず比較整理の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、比較整理の証跡として残す。 ✅
    - C. INGLIST を省略して比較整理の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では Security 機能 は「比較整理の計画 インストールに関係する定義値と表示行を照合する比較整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では Security 機能の属性行と INGKYST0I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では Security 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較整理初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Short-term console outages {#c36-i1563}
*分類: 計画 / インストール*  ・  難易度: 上級

Short-term console outagesは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 順序整理の計画 インストールで自動化管理の運用確認を行います。Short-term 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序整理の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序整理の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、順序整理の確認記録にまとめる。 ✅
    - D. Short-term 機能の属性行を読まず順序整理の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では Short-term 機能 は「SA z/OS で Short-term 機能の扱いを記録する順序整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では Short-term 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明のみに寄り、判定名は順序整理不足です。順序整理資料では Short-term 機能の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Software Requirements {#c36-i1564}
*分類: 計画 / インストール*  ・  難易度: 上級

Software Requirementsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 復旧整理の計画 インストールで Software 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Software 機能の出力を取らず復旧整理の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、復旧整理の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して復旧整理の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では Software 機能 は「復旧整理の計画 インストールに関係する定義値と表示行を照合する復旧整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では Software 機能の属性行と INGKYST0I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では Software 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Start SA z/OS for the first time {#c36-i1565}
*分類: 計画 / インストール*  ・  難易度: 上級

Start SA z/OS for the first timeは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Step 10: Configure the Component Trace {#c36-i1566}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 10: Configure the Component Traceは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 変更整理の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更整理の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して変更整理の:の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更整理の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける変更整理項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では Step 機能を SA z/OS の確認記録に残し、対象名は変更整理対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 11: Configure the System Logger {#c36-i1567}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 11: Configure the System Loggerは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文記録の:に関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、構文記録の点検結果を残す。 ✅
    - B. Step 機能の名称と担当者名のみを残して構文記録の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文記録の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文記録の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する構文記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 12: Configure ISPF Dialog Panels {#c36-i1568}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 12: Configure ISPF Dialog Panelsは、Step 12: Configure ISPF Dialog Panels は 計画/インストール の項目

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 展開記録の:で Step 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 機能の出力を取らず展開記録の:の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、展開記録で再確認できる形にする。 ✅
    - C. INGLIST を省略して展開記録の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では Step 機能 は「展開記録の:に関係する定義値と表示行を照合する展開記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では Step 機能の属性行と INGKYST0I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では Step 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開記録初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Step 13: Verify the Number of available REXX Environments {#c36-i1569}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 13: Verify the Number of available REXX Environmentsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出記録の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出記録の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出記録の:を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、呼出記録の確認値として扱う。 ✅
    - D. Step 機能の属性行を読まず呼出記録の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する呼出記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では Step 機能の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 14: Configure Function Packages for TSO {#c36-i1570}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 14: Configure Function Packages for TSOは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換記録の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換記録の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して置換記録の:の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける置換記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では Step 機能を SA z/OS の確認記録に残し、対象名は置換記録対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 15: Configure Alert Notification for SA z/OS {#c36-i1571}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 15: Configure Alert Notification for SA z/OSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端記録の:に関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を終端記録で確認する。 ✅
    - B. Step 機能の名称と担当者名のみを残して終端記録の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端記録の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端記録の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する終端記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 16: Compile SA z/OS REXX Procedures {#c36-i1572}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 16: Compile SA z/OS REXX Proceduresは、Step 16: Compile SA z/OS REXX Procedures は 計画/インストール の項目

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 探索記録の: Step 16: Compile SA z/OS REXX Proceduresで Step 16: Compile SA z 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 16: Compile SA z 属性の出力を取らず探索記録の: ・の説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、探索記録の証跡として残す。 ✅
    - C. INGLIST を省略して探索記録の: ・の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録の: ・へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では Step 16: Compile SA z 属性 は「探索記録の: Step 16: Compile SA z/OS REXX Proceduresに関係する定義値と表示行を照合する探索記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では Step 16: Compile SA z 属性の属性行と INGKYST0I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では Step 16: Compile SA z 属性を Z System Automation (TSA)の運用手順で確認し、初出名は探索記録初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Step 17: Defining Automation Policy {#c36-i1573}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 17: Defining Automation Policyは、Step 17: Defining Automation Policy は 計画/インストール の項目

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 上書記録の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書記録の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書記録の:を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、上書記録の確認記録にまとめる。 ✅
    - D. Step 機能の属性行を読まず上書記録の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する上書記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では Step 機能の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Step 18: Define Host-to-Host Communications {#c36-i1574}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 18: Define Host-to-Host Communicationsは、Step 18: Define Host-to-Host Communications は 計画/インストール の項目

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 出力記録の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力記録の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して出力記録の:の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて出力記録の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける出力記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では Step 機能を SA z/OS の確認記録に残し、対象名は出力記録対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Step 19: Enabling SA z/OS to Restart Automatic Restart Manager Enabled Subsystems {#c36-i1575}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 19: Enabling SA z/OS to Restart Automatic Restart Manager Enabled Subsystemsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Step 20: Define Security {#c36-i1576}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 20: Define Securityは、Z System Automation (TSA)の計画 / インストールで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 区切記録の:で Step 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 機能の出力を取らず区切記録の:の説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、区切記録の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して区切記録の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では Step 機能 は「区切記録の:に関係する定義値と表示行を照合する区切記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では Step 機能の属性行と INGKYST0I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では Step 機能を Z System Automation (TSA)の運用手順で確認し、初出名は区切記録初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.103) / OS 計画およびインストール



### Step 21: Configure the Status Display Facility (SDF) {#c36-i1577}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 21: Configure the Status Display Facility (SDF)は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 範囲記録の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲記録の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲記録の:を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、範囲記録として引き継ぐ。 ✅
    - D. Step 機能の属性行を読まず範囲記録の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する範囲記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では Step 機能の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 22: Configure System Automation Info Broker {#c36-i1578}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 22: Configure System Automation Info Brokerは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 優先記録の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先記録の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して優先記録の:の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先記録の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける優先記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では Step 機能を SA z/OS の確認記録に残し、対象名は優先記録対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール



### Step 23: Check for Required IPL {#c36-i1579}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 23: Check for Required IPLは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 記録記録の:に関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、記録記録の点検結果を残す。 ✅
    - B. Step 機能の名称と担当者名のみを残して記録記録の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録記録の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録記録の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する記録記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 24: Automate System Operations Startup {#c36-i1580}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 24: Automate System Operations Startupは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 比較記録の:で Step 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 機能の出力を取らず比較記録の:の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較記録で再確認できる形にする。 ✅
    - C. INGLIST を省略して比較記録の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では Step 機能 は「比較記録の:に関係する定義値と表示行を照合する比較記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では Step 機能の属性行と INGKYST0I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では Step 機能を Z System Automation (TSA)の運用手順で確認し、初出名は比較記録初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール



### Step 25: Verify Automatic System Operations Startup {#c36-i1581}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 25: Verify Automatic System Operations Startupは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 順序記録の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序記録の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序記録の:を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序記録の確認値として扱う。 ✅
    - D. Step 機能の属性行を読まず順序記録の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する順序記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では Step 機能の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール



### Step 26: Configure USS Automation {#c36-i1582}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 26: Configure USS Automationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 値域記録の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域記録の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して値域記録の:の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域記録の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける値域記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では Step 機能を SA z/OS の確認記録に残し、対象名は値域記録対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.144) / OS 計画およびインストール



### Step 27: Configure and Run the System Automation Data Store {#c36-i1583}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 27: Configure and Run the System Automation Data Storeは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 警告記録の:に関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を警告記録で確認する。 ✅
    - B. Step 機能の名称と担当者名のみを残して警告記録の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告記録の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告記録の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する警告記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 28: Configure Db2 as an alternative database of dynamic resources {#c36-i1584}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 28: Configure Db2 as an alternative database of dynamic resourcesは、Z System Automation (TSA)の計画 / インストールでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 復旧記録の:で Step 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 機能の出力を取らず復旧記録の:の説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、復旧記録の証跡として残す。 ✅
    - C. INGLIST を省略して復旧記録の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では Step 機能 は「復旧記録の:に関係する定義値と表示行を照合する復旧記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では Step 機能の属性行と INGKYST0I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では Step 機能を Z System Automation (TSA)の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 29: Configure and Run the System Automation Operations REST Server {#c36-i1585}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 29: Configure and Run the System Automation Operations REST Serverは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 監査記録の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査記録の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査記録の:を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、監査記録の確認記録にまとめる。 ✅
    - D. Step 機能の属性行を読まず監査記録の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する監査記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では Step 機能の使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 2: Allocate System-Unique Data Sets {#c36-i1586}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 2: Allocate System-Unique Data Setsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.87) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 変更記録の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更記録の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して変更記録の:の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて変更記録の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける変更記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では Step 機能を SA z/OS の確認記録に残し、対象名は変更記録対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.87) / OS 計画およびインストール



### Step 30: Configure the Policy Services Provider {#c36-i1587}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 30: Configure the Policy Services Providerは、Z System Automation (TSA)の計画 / インストールでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 構文分離の:に関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、構文分離の結果として保存する。 ✅
    - B. Step 機能の名称と担当者名のみを残して構文分離の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文分離の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文分離の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する構文分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 31: Enable the End-to-End Automation and Connect an SAplex to Service Management Unite {#c36-i1588}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 31: Enable the End-to-End Automation and Connect an SAplex to Service Management Uniteは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### Step 32: Copy and Update Sample Exits {#c36-i1589}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 32: Copy and Update Sample Exitsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 呼出分離の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出分離の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出分離の:を正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、呼出分離として引き継ぐ。 ✅
    - D. Step 機能の属性行を読まず呼出分離の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する呼出分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では Step 機能の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 33: Install Relational Data Services (RDS) {#c36-i1590}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 33: Install Relational Data Services (RDS)は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.165) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 置換分離の:に関する Step 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換分離の:の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の:の証跡として保存して根拠にする。
    - C. Step 機能の変更点を出力本文から切り離して置換分離の:の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、置換分離の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では Step 機能 は「Step 機能の状態と出力メッセージを結び付ける置換分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では Step 機能の出力行と INGKYST0I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では Step 機能を SA z/OS の確認記録に残し、対象名は置換分離対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.165) / OS 計画およびインストール



### Step 34: Install CICS Automation in CICS {#c36-i1591}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 34: Install CICS Automation in CICSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端分離の:に関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、終端分離の点検結果を残す。 ✅
    - B. Step 機能の名称と担当者名のみを残して終端分離の:の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端分離の:を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端分離の:の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する終端分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 35: Install IMS Automation in IMS {#c36-i1592}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 35: Install IMS Automation in IMSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索分離の:で Step 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 機能の出力を取らず探索分離の:の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、探索分離で再確認できる形にする。 ✅
    - C. INGLIST を省略して探索分離の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では Step 機能 は「探索分離の:に関係する定義値と表示行を照合する探索分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では Step 機能の属性行と INGKYST0I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では Step 機能を Z System Automation (TSA)の運用手順で確認し、初出名は探索分離初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Step 36: Install ZWS Automation in ZWS {#c36-i1593}
*分類: 計画 / インストール*  ・  難易度: 上級

Step 36: Install ZWS Automation in ZWSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 上書分離の:で自動化管理の運用確認を行います。Step 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書分離の:を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書分離の:を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、上書分離の確認値として扱う。 ✅
    - D. Step 機能の属性行を読まず上書分離の:の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では Step 機能 は「SA z/OS で Step 機能の扱いを記録する上書分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では Step 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では Step 機能の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


