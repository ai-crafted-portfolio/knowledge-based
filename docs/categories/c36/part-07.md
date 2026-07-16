---
search:
  exclude: true
---

# Z System Automation (TSA) — 詳細 (7/7)

[← Z System Automation (TSA) の概要へ戻る](index.md)


## Z System Automation (TSA) > 計画 / インストール

### Support Element characteristics {#c36-i1605}
*分類: 計画 / インストール*  ・  難易度: 上級

Support Element characteristicsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 監査分離の計画 インストールで自動化管理の運用確認を行います。Support 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査分離の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査分離の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、監査分離の確認値として扱う。 ✅
    - D. Support 機能の属性行を読まず監査分離の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Support 機能 は「SA z/OS で Support 機能の扱いを記録する監査分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Support 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では Support 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### Supported Hardware {#c36-i1606}
*分類: 計画 / インストール*  ・  難易度: 上級

Supported Hardwareは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 変更分離の計画 インストールに関する Supported Hardwareの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず変更分離の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離の計画 インストールの証跡として保存して根拠にする。
    - C. Supported Hardwareの変更点を出力本文から切り離して変更分離の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて変更分離の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では Supported Hardware は「Supported Hardwareの状態と出力メッセージを結び付ける変更分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では Supported Hardwareの出力行と INGKYST0I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では Supported Hardwareを SA z/OS の確認記録に残し、対象名は変更分離対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール



### Supported Operating Systems {#c36-i1607}
*分類: 計画 / インストール*  ・  難易度: 上級

Supported Operating Systemsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 構文読解の計画 インストールに関係する Supported 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を構文読解で確認する。 ✅
    - B. Supported 機能の名称と担当者名のみを残して構文読解の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文読解の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文読解の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では Supported 機能 は「Supported 機能の用途を自動化管理の表示で確認する構文読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では SA z/OS の Supported 機能と INGKYST0I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では Supported 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール



### Syntax for HSAPRM00 {#c36-i1608}
*分類: 計画 / インストール*  ・  難易度: 上級

Syntax for HSAPRM00は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 展開読解の計画 インストールで Syntax 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Syntax 機能の出力を取らず展開読解の計画 インストールの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、展開読解の証跡として残す。 ✅
    - C. INGLIST を省略して展開読解の計画 インストールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解の計画 インストールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では Syntax 機能 は「展開読解の計画 インストールに関係する定義値と表示行を照合する展開読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では Syntax 機能の属性行と INGKYST0I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では Syntax 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開読解初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### System Operations Considerations {#c36-i1609}
*分類: 計画 / インストール*  ・  難易度: 上級

System Operations Considerationsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 呼出読解の計画 インストールで自動化管理の運用確認を行います。System 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で呼出読解の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず呼出読解の計画 インストールを正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出読解の確認記録にまとめる。 ✅
    - D. System 機能の属性行を読まず呼出読解の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では System 機能 は「SA z/OS で System 機能の扱いを記録する呼出読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では System 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では System 機能の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.290) / OS 計画およびインストール



### Testing CI Performance for SNMP Connections {#c36-i1610}
*分類: 計画 / インストール*  ・  難易度: 上級

Testing CI Performance for SNMP Connectionsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 置換読解の計画 インストールに関する Testing 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず置換読解の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解の計画 インストールの証跡として保存して根拠にする。
    - C. Testing 機能の変更点を出力本文から切り離して置換読解の計画 インストールの承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換読解の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では Testing 機能 は「Testing 機能の状態と出力メッセージを結び付ける置換読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では Testing 機能の出力行と INGKYST0I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では Testing 機能を SA z/OS の確認記録に残し、対象名は置換読解対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### The Focal Point System and Its Target Systems {#c36-i1611}
*分類: 計画 / インストール*  ・  難易度: 上級

The Focal Point System and Its Target Systemsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 終端読解の計画 インストールに関係する The 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、終端読解の結果として保存する。 ✅
    - B. The 機能の名称と担当者名のみを残して終端読解の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で終端読解の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず終端読解の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では The 機能 は「The 機能の用途を自動化管理の表示で確認する終端読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では SA z/OS の The 機能と INGKYST0I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では The 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Traditional SA z/OS Configuration {#c36-i1612}
*分類: 計画 / インストール*  ・  難易度: 上級

Traditional SA z/OS Configurationは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 探索読解のTraditional SA z/OS Configurationで Traditional SA z 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Traditional SA z 属性の出力を取らず探索読解のTraditional SA z/OS Configurationの説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、探索読解の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して探索読解のTraditional SA z/OS Configurationの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解のTraditional SA z/OS Configurationへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では Traditional SA z 属性 は「探索読解のTraditional SA z/OS Configurationに関係する定義値と表示行を照合する探索読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では Traditional SA z 属性の属性行と INGKYST0I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では Traditional SA z 属性を Z System Automation (TSA)の運用手順で確認し、初出名は探索読解初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Unpredictable console outages overview {#c36-i1613}
*分類: 計画 / インストール*  ・  難易度: 上級

Unpredictable console outages overviewは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 上書読解の計画 インストールで自動化管理の運用確認を行います。Unpredictable 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で上書読解の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず上書読解の計画 インストールを正常終了として記録する。
    - C. 資料上の説明と画面上の表示行を突き合わせ、上書読解として引き継ぐ。 ✅
    - D. Unpredictable 機能の属性行を読まず上書読解の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Unpredictable 機能 は「SA z/OS で Unpredictable 機能の扱いを記録する上書読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Unpredictable 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では Unpredictable 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### Use of Commands Cross System {#c36-i1614}
*分類: 計画 / インストール*  ・  難易度: 上級

Use of Commands Cross Systemは、Z System Automation (TSA)の計画 / インストールで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 出力読解の計画 インストールに関する Use 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず出力読解の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解の計画 インストールの証跡として保存して根拠にする。
    - C. Use 機能の変更点を出力本文から切り離して出力読解の計画 インストールの承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、出力読解の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では Use 機能 は「Use 機能の状態と出力メッセージを結び付ける出力読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では Use 機能の出力行と INGKYST0I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では Use 機能を SA z/OS の確認記録に残し、対象名は出力読解対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Use of Commands from TSO or Batch {#c36-i1615}
*分類: 計画 / インストール*  ・  難易度: 上級

Use of Commands from TSO or Batchは、Z System Automation (TSA)の計画 / インストールで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 条件読解の計画 インストールに関係する Use 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、条件読解の点検結果を残す。 ✅
    - B. Use 機能の名称と担当者名のみを残して条件読解の計画 インストールの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件読解の計画 インストールを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件読解の計画 インストールの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では Use 機能 は「Use 機能の用途を自動化管理の表示で確認する条件読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では SA z/OS の Use 機能と INGKYST0I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では Use 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using CI in a z/OS Sysplex Environment {#c36-i1616}
*分類: 計画 / インストール*  ・  難易度: 上級

Using CI in a z/OS Sysplex Environmentは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（1問）"
    **問題.** 区切読解のUsing CI in a z/OS Sysplex Environmentで Using CI in a z 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Using CI in a z 属性の出力を取らず区切読解のUsing CI in a z/OS Sysplex Environmentの説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、区切読解で再確認できる形にする。 ✅
    - C. INGLIST を省略して区切読解のUsing CI in a z/OS Sysplex Environmentの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解のUsing CI in a z/OS Sysplex Environmentへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では Using CI in a z 属性 は「区切読解のUsing CI in a z/OS Sysplex Environmentに関係する定義値と表示行を照合する区切読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では Using CI in a z 属性の属性行と INGKYST0I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では Using CI in a z 属性を Z System Automation (TSA)の運用手順で確認し、初出名は区切読解初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming



### Using the Hardware Integrated Console of IBM Z for External Automation with SA z/OS {#c36-i1617}
*分類: 計画 / インストール*  ・  難易度: 上級

Using the Hardware Integrated Console of IBM Z for External Automation with SA z/OSは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Z System Automation (TSA) の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


### What's New (GA-level) {#c36-i1618}
*分類: 計画 / インストール*  ・  難易度: 上級

What's New (GA-level)は、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 優先読解の計画 インストールに関する What's New 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先読解の計画 インストールの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解の計画 インストールの証跡として保存して根拠にする。
    - C. What's New 属性の変更点を出力本文から切り離して優先読解の計画 インストールの承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて優先読解の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では What's New 属性 は「What's New 属性の状態と出力メッセージを結び付ける優先読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では What's New 属性の出力行と INGKYST0I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では What's New 属性を SA z/OS の確認記録に残し、対象名は優先読解対象です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.27) / OS 計画およびインストール



### z/OS Considerations {#c36-i1619}
*分類: 計画 / インストール*  ・  難易度: 上級

z/OS Considerationsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 記録読解のz/OS Considerationsに関係するz 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGKYST0I を含む表示を保存し、説明欄との差分を記録読解で確認する。 ✅
    - B. z 属性の名称と担当者名のみを残して記録読解のz/OS Considerationsの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録読解のz/OS Considerationsを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録読解のz/OS Considerationsの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠ではz 属性 は「z 属性の用途を自動化管理の表示で確認する記録読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では SA z/OS のz 属性と INGKYST0I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語ではz 属性を Z System Automation (TSA)で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール



### z/OS Health Checker Considerations {#c36-i1620}
*分類: 計画 / インストール*  ・  難易度: 上級

z/OS Health Checker Considerationsは、Z System Automation (TSA)の計画 / インストールで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。TSA z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール

??? question "確認問題（1問）"
    **問題.** 比較読解のz/OS Health Checker Considerationsでz 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. z 属性の出力を取らず比較読解のz/OS Health Checker Considerationsの説明文と承認印のみを残す。
    - B. INGLIST の結果から対象行を抜き出し、比較読解の証跡として残す。 ✅
    - C. INGLIST を省略して比較読解のz/OS Health Checker Considerationsの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解のz/OS Health Checker Considerationsへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠ではz 属性 は「比較読解のz/OS Health Checker Considerationsに関係する定義値と表示行を照合する比較読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡ではz 属性の属性行と INGKYST0I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出ではz 属性を Z System Automation (TSA)の運用手順で確認し、初出名は比較読解初出です。

    **出典:** TSA z / OS 計画およびインストール (TSA_z_OS_4.3_Planning_and_Installation.pdf p.26) / OS 計画およびインストール




## Z System Automation (TSA) > 資源状態 > Automation status

### Automation status {#c36-i1621}
*分類: 資源状態 > Automation status*  ・  難易度: 中級

Automation statusは、資源に対する自動化が現在どのように働いているかを表す状態です。自動化が有効か中断中かを読み取れます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（4問）"
    **問題.** 記録面の自動化状態を引継ぎ確認で確認します。変更面の対象項目では入力と操作画面応答を照合し、automation status valueを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Automation Status ✅
    - B. Application Group
    - C. CONDITION Policy Item
    - D. Pacing Gate

    正解: **A** ／ 難易度: 中級

    **解説:** 表示面の判定ではAを選び、対象は自動化状態照合です。設計面の識別語は 自動化 状態 で、自動化状態照合の対象名です。復旧面の自動化状態観点は、自動化処理が稼働中か待機中かを読むことを目的に扱う説明単位が自動化状態証跡です。障害面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化状態読取です。保守面の自動化状態状態を読む応答では、automation status valueを出典の属性説明と照合する点が自動化状態定義です。A: 応答面の自動化状態照合が正答です。証跡面の自動化状態照合応答で確認できる対象は自動化状態照合です。B: 定義面の自動化状態観点で見るアプリケーショングループは役割が異なり、除外理由を説明する対象は自動化状態観点です。C: 状態面の自動化状態証跡で見る条件定義は役割が異なり、除外理由を説明する対象は自動化状態証跡です。D: 証跡面の自動化状態読取で見るペーシングゲートは役割が異なり、除外理由を説明する対象は自動化状態読取です。監査面の初出語説明として、自動化状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化状態応答です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 構成面の自動化状態をポリシー見直しで確認します。設計面の対象項目では入力と操作画面応答を照合し、automation status valueを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. INGREQ START
    - B. INGAMS Diagnostic
    - C. Automation Status ✅
    - D. MESSAGES/USER DATA Policy Item

    正解: **C** ／ 難易度: 中級

    **解説:** 記録面の判定ではCを選び、対象は自動化状態棚卸です。表示面の識別語は 自動化 状態 で、自動化状態棚卸の対象名です。証跡面の自動化状態復旧は、自動化処理が稼働中か待機中かを読むことを目的に扱う説明単位が自動化状態照合です。変更面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化状態観点です。復旧面の自動化状態証跡を読む応答では、automation status valueを出典の属性説明と照合する点が自動化状態読取です。A: 引継ぎ面の自動化状態棚卸で見る始動要求は役割が異なり、除外理由を説明する対象は自動化状態棚卸です。B: 応答面の自動化状態復旧で見る診断機能は役割が異なり、除外理由を説明する対象は自動化状態復旧です。C: 定義面の自動化状態照合が正答です。復旧面の自動化状態照合応答で確認できる対象は自動化状態照合です。D: 状態面の自動化状態観点で見るメッセージ条件は役割が異なり、除外理由を説明する対象は自動化状態観点です。障害面の初出語説明として、自動化状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化状態定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 要求面の自動化状態を運用変更で確認します。表示面の対象項目では入力と操作画面応答を照合し、automation status valueを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. Automation Status ✅
    - B. MESSAGES/USER DATA Policy Item
    - C. INGFILT
    - D. Configuration Member

    正解: **A** ／ 難易度: 中級

    **解説:** 構成面の判定ではAを選び、対象は自動化状態監査です。記録面の識別語は 自動化 状態 で、自動化状態監査の対象名です。状態面の自動化状態引継ぎは、自動化処理が稼働中か待機中かを読むことを目的に扱う説明単位が自動化状態棚卸です。設計面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化状態復旧です。証跡面の自動化状態照合を読む応答では、automation status valueを出典の属性説明と照合する点が自動化状態観点です。A: 監査面の自動化状態監査が正答です。定義面の自動化状態監査応答で確認できる対象は自動化状態監査です。B: 引継ぎ面の自動化状態引継ぎで見るメッセージ条件は役割が異なり、除外理由を説明する対象は自動化状態引継ぎです。C: 応答面の自動化状態棚卸で見る表示フィルターは役割が異なり、除外理由を説明する対象は自動化状態棚卸です。D: 定義面の自動化状態復旧で見る構成メンバーは役割が異なり、除外理由を説明する対象は自動化状態復旧です。変更面の初出語説明として、自動化状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化状態読取です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 比較検分の自動化管理で Automation statusの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Automation statusの出力を取らず比較検分の自動化管理の説明文と承認印のみを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較検分で再確認できる形にする。 ✅
    - C. INGLIST を省略して比較検分の自動化管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分の自動化管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Automation status は「比較検分の自動化管理に関係する定義値と表示行を照合する比較検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Automation statusの属性行と INGKYST0I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Automation statusを Z System Automation (TSA)の運用手順で確認し、初出名は比較検分初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 資源状態 > Compound status

### Compound status {#c36-i1622}
*分類: 資源状態 > Compound status*  ・  難易度: 上級

Compound statusは、観測状態や目標状態、健康状態などの要素を束ね、資源がおおむね良好かを一目に表す統合の状態です

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（4問）"
    **問題.** 表示面の複合状態をポリシー見直しで確認します。障害面の対象項目では入力と操作画面応答を照合し、compound statusを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. USS CONTROL Policy Item
    - B. Compound Status ✅
    - C. DISPINFO
    - D. Health Status

    正解: **B** ／ 難易度: 中級

    **解説:** 設計面の判定ではBを選び、対象は複合状態観点です。変更面の識別語は 複合 状態 で、複合状態観点の対象名です。保守面の複合状態証跡は、複数状態を要約した表示で影響を判断することを目的に扱う説明単位が複合状態読取です。監査面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は複合状態状態です。照合面の複合状態定義を読む応答では、compound statusを出典の属性説明と照合する点が複合状態根拠です。A: 定義面の複合状態観点で見るユーエスエス制御項目は役割が異なり、除外理由を説明する対象は複合状態観点です。B: 状態面の複合状態証跡が正答です。保守面の複合状態証跡応答で確認できる対象は複合状態証跡です。C: 証跡面の複合状態読取で見るエージェント視点表示は役割が異なり、除外理由を説明する対象は複合状態読取です。D: 復旧面の複合状態状態で見るヘルス状態は役割が異なり、除外理由を説明する対象は複合状態状態です。引継ぎ面の初出語説明として、複合状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は複合状態保守です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 記録面の複合状態を運用変更で確認します。変更面の対象項目では入力と操作画面応答を照合し、compound statusを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. ACF Load
    - B. Suspend Override
    - C. INGLIST
    - D. Compound Status ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 表示面の判定ではDを選び、対象は複合状態復旧です。設計面の識別語は 複合 状態 で、複合状態復旧の対象名です。復旧面の複合状態照合は、複数状態を要約した表示で影響を判断することを目的に扱う説明単位が複合状態観点です。障害面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は複合状態証跡です。保守面の複合状態読取を読む応答では、compound statusを出典の属性説明と照合する点が複合状態状態です。A: 応答面の複合状態復旧で見る制御ファイル読込は役割が異なり、除外理由を説明する対象は複合状態復旧です。B: 定義面の複合状態照合で見る一時停止上書きは役割が異なり、除外理由を説明する対象は複合状態照合です。C: 状態面の複合状態観点で見る資源一覧表示は役割が異なり、除外理由を説明する対象は複合状態観点です。D: 証跡面の複合状態証跡が正答です。照合面の複合状態証跡応答で確認できる対象は複合状態証跡です。監査面の初出語説明として、複合状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は複合状態根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 構成面の複合状態を障害切り分けで確認します。設計面の対象項目では入力と操作画面応答を照合し、compound statusを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. INGLIST
    - B. Compound Status ✅
    - C. INGSUSPD RESUME
    - D. TRIGGER Policy Item

    正解: **B** ／ 難易度: 中級

    **解説:** 記録面の判定ではBを選び、対象は複合状態引継ぎです。表示面の識別語は 複合 状態 で、複合状態引継ぎの対象名です。証跡面の複合状態棚卸は、複数状態を要約した表示で影響を判断することを目的に扱う説明単位が複合状態復旧です。変更面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は複合状態照合です。復旧面の複合状態観点を読む応答では、compound statusを出典の属性説明と照合する点が複合状態証跡です。A: 引継ぎ面の複合状態引継ぎで見る資源一覧表示は役割が異なり、除外理由を説明する対象は複合状態引継ぎです。B: 応答面の複合状態棚卸が正答です。証跡面の複合状態棚卸応答で確認できる対象は複合状態棚卸です。C: 定義面の複合状態復旧で見る自動化再開は役割が異なり、除外理由を説明する対象は複合状態復旧です。D: 状態面の複合状態照合で見るトリガー定義は役割が異なり、除外理由を説明する対象は複合状態照合です。障害面の初出語説明として、複合状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は複合状態状態です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 順序検分の自動化管理で自動化管理の運用確認を行います。Compound statusの根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で順序検分の自動化管理を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず順序検分の自動化管理を正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、順序検分の確認値として扱う。 ✅
    - D. Compound statusの属性行を読まず順序検分の自動化管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Compound status は「SA z/OS で Compound statusの扱いを記録する順序検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Compound statusの表示結果と INGKYST0I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Compound statusの使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 資源状態 > Desired status

### Desired status {#c36-i1623}
*分類: 資源状態 > Desired status*  ・  難易度: 中級

Desired statusは、資源がそうあるべき状態を表すゴールです。自動化マネージャーはこの目標へ資源を近づけようとします

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（4問）"
    **問題.** 構成面の目標状態を監査記録で確認します。設計面の対象項目では入力と操作画面応答を照合し、desired valueを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGAMS
    - B. Agent READY Status
    - C. Timer Resume
    - D. Desired Status ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 記録面の判定ではDを選び、対象は目標状態復旧です。表示面の識別語は 目標 状態 で、目標状態復旧の対象名です。証跡面の目標状態照合は、自動化マネージャーが到達させる状態を読むことを目的に扱う説明単位が目標状態観点です。変更面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は目標状態証跡です。復旧面の目標状態読取を読む応答では、desired valueを出典の属性説明と照合する点が目標状態状態です。A: 引継ぎ面の目標状態復旧で見るマネージャー一覧は役割が異なり、除外理由を説明する対象は目標状態復旧です。B: 応答面の目標状態照合で見るエージェント準備状態は役割が異なり、除外理由を説明する対象は目標状態照合です。C: 定義面の目標状態観点で見るタイマー再開は役割が異なり、除外理由を説明する対象は目標状態観点です。D: 状態面の目標状態証跡が正答です。保守面の目標状態証跡応答で確認できる対象は目標状態証跡です。障害面の初出語説明として、目標状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は目標状態根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Programmers Reference p.170

    ---

    **問題.** 要求面の目標状態を引継ぎ確認で確認します。表示面の対象項目では入力と操作画面応答を照合し、desired valueを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. IMS CONTROL Policy Item
    - B. Desired Status ✅
    - C. INGWHY
    - D. INGAMS Diagnostic

    正解: **B** ／ 難易度: 初級

    **解説:** 構成面の判定ではBを選び、対象は目標状態引継ぎです。記録面の識別語は 目標 状態 で、目標状態引継ぎの対象名です。状態面の目標状態棚卸は、自動化マネージャーが到達させる状態を読むことを目的に扱う説明単位が目標状態復旧です。設計面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は目標状態照合です。証跡面の目標状態観点を読む応答では、desired valueを出典の属性説明と照合する点が目標状態証跡です。A: 監査面の目標状態引継ぎで見るアイエムエス制御項目は役割が異なり、除外理由を説明する対象は目標状態引継ぎです。B: 引継ぎ面の目標状態棚卸が正答です。状態面の目標状態棚卸応答で確認できる対象は目標状態棚卸です。C: 応答面の目標状態復旧で見る理由照会は役割が異なり、除外理由を説明する対象は目標状態復旧です。D: 定義面の目標状態照合で見る診断機能は役割が異なり、除外理由を説明する対象は目標状態照合です。変更面の初出語説明として、目標状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は目標状態状態です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Programmers Reference p.170

    ---

    **問題.** 運用面の目標状態をポリシー見直しで確認します。記録面の対象項目では入力と操作画面応答を照合し、desired valueを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. INGAMS Diagnostic
    - B. SHUTDOWN Policy Item
    - C. INGREQ START
    - D. Desired Status ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 要求面の判定ではDを選び、対象は目標状態保守です。構成面の識別語は 目標 状態 で、目標状態保守の対象名です。定義面の目標状態監査は、自動化マネージャーが到達させる状態を読むことを目的に扱う説明単位が目標状態引継ぎです。表示面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は目標状態棚卸です。状態面の目標状態復旧を読む応答では、desired valueを出典の属性説明と照合する点が目標状態照合です。A: 障害面の目標状態保守で見る診断機能は役割が異なり、除外理由を説明する対象は目標状態保守です。B: 監査面の目標状態監査で見る停止ポリシーは役割が異なり、除外理由を説明する対象は目標状態監査です。C: 引継ぎ面の目標状態引継ぎで見る始動要求は役割が異なり、除外理由を説明する対象は目標状態引継ぎです。D: 応答面の目標状態棚卸が正答です。証跡面の目標状態棚卸応答で確認できる対象は目標状態棚卸です。設計面の初出語説明として、目標状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は目標状態証跡です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Programmers Reference p.170

    ---

    **問題.** 記録検分の自動化管理に関係する Desired statusの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SA z/OS の表示形式に沿って根拠行を採り、記録検分の点検結果を残す。 ✅
    - B. Desired statusの名称と担当者名のみを残して記録検分の自動化管理の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で記録検分の自動化管理を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず記録検分の自動化管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Desired status は「Desired statusの用途を自動化管理の表示で確認する記録検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では SA z/OS の Desired statusと INGKYST0I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Desired statusを Z System Automation (TSA)で扱う確認対象とし、用語名は記録検分用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 資源状態 > Health status

### Health status {#c36-i1624}
*分類: 資源状態 > Health status*  ・  難易度: 上級

Health statusは、資源の健全さを表す状態です。自動化マネージャーは健康状態の変化に応じて必要な自動化を引き起こします

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（4問）"
    **問題.** 設計面のヘルス状態を運用変更で確認します。監査面の対象項目では入力と操作画面応答を照合し、health statusを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. Desired Status
    - B. INGREQ STOP
    - C. Health Status ✅
    - D. INGAMS Details

    正解: **C** ／ 難易度: 中級

    **解説:** 変更面の判定ではCを選び、対象はヘルス状態証跡です。障害面の識別語は ヘルス 状態 で、ヘルス状態証跡の対象名です。照合面のヘルス状態読取は、正常性の変化を自動化判断に使うことを目的に扱う説明単位がヘルス状態状態です。引継ぎ面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はヘルス状態定義です。運用面のヘルス状態根拠を読む応答では、health statusを出典の属性説明と照合する点がヘルス状態応答です。A: 状態面のヘルス状態証跡で見る目標状態は役割が異なり、除外理由を説明する対象はヘルス状態証跡です。B: 証跡面のヘルス状態読取で見る停止要求は役割が異なり、除外理由を説明する対象はヘルス状態読取です。C: 復旧面のヘルス状態状態が正答です。運用面のヘルス状態状態応答で確認できる対象はヘルス状態状態です。D: 保守面のヘルス状態定義で見る構成詳細は役割が異なり、除外理由を説明する対象はヘルス状態定義です。応答面の初出語説明として、ヘルス状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はヘルス状態監査です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.86

    ---

    **問題.** 表示面のヘルス状態を障害切り分けで確認します。障害面の対象項目では入力と操作画面応答を照合し、health statusを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. Health Status ✅
    - B. APPLICATION Entry Type
    - C. DB2 CONTROL Policy Item
    - D. Dependency Status

    正解: **A** ／ 難易度: 中級

    **解説:** 設計面の判定ではAを選び、対象はヘルス状態照合です。変更面の識別語は ヘルス 状態 で、ヘルス状態照合の対象名です。保守面のヘルス状態観点は、正常性の変化を自動化判断に使うことを目的に扱う説明単位がヘルス状態証跡です。監査面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はヘルス状態読取です。照合面のヘルス状態状態を読む応答では、health statusを出典の属性説明と照合する点がヘルス状態定義です。A: 定義面のヘルス状態照合が正答です。復旧面のヘルス状態照合応答で確認できる対象はヘルス状態照合です。B: 状態面のヘルス状態観点で見るアプリケーション定義は役割が異なり、除外理由を説明する対象はヘルス状態観点です。C: 証跡面のヘルス状態証跡で見るDb2制御項目は役割が異なり、除外理由を説明する対象はヘルス状態証跡です。D: 復旧面のヘルス状態読取で見る依存関係状態は役割が異なり、除外理由を説明する対象はヘルス状態読取です。引継ぎ面の初出語説明として、ヘルス状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はヘルス状態応答です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.86

    ---

    **問題.** 記録面のヘルス状態を監査記録で確認します。変更面の対象項目では入力と操作画面応答を照合し、health statusを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. Dependency Status
    - B. SAM Role
    - C. Health Status ✅
    - D. INGINFO

    正解: **C** ／ 難易度: 中級

    **解説:** 表示面の判定ではCを選び、対象はヘルス状態棚卸です。設計面の識別語は ヘルス 状態 で、ヘルス状態棚卸の対象名です。復旧面のヘルス状態復旧は、正常性の変化を自動化判断に使うことを目的に扱う説明単位がヘルス状態照合です。障害面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はヘルス状態観点です。保守面のヘルス状態証跡を読む応答では、health statusを出典の属性説明と照合する点がヘルス状態読取です。A: 応答面のヘルス状態棚卸で見る依存関係状態は役割が異なり、除外理由を説明する対象はヘルス状態棚卸です。B: 定義面のヘルス状態復旧で見る副マネージャー役割は役割が異なり、除外理由を説明する対象はヘルス状態復旧です。C: 状態面のヘルス状態照合が正答です。保守面のヘルス状態照合応答で確認できる対象はヘルス状態照合です。D: 証跡面のヘルス状態観点で見る資源詳細表示は役割が異なり、除外理由を説明する対象はヘルス状態観点です。監査面の初出語説明として、ヘルス状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はヘルス状態定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.86

    ---

    **問題.** 値域検分の自動化管理に関する Health statusの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず値域検分の自動化管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分の自動化管理の証跡として保存して根拠にする。
    - C. Health statusの変更点を出力本文から切り離して値域検分の自動化管理の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて値域検分の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Health status は「Health statusの状態と出力メッセージを結び付ける値域検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Health statusの出力行と INGKYST0I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Health statusを SA z/OS の確認記録に残し、対象名は値域検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## Z System Automation (TSA) > 資源状態 > Observed status

### Observed status {#c36-i1625}
*分類: 資源状態 > Observed status*  ・  難易度: 中級

Observed statusは、自動化マネージャーが監視している資源の現在の状態を表します。目標状態とのずれが起動や停止の自動化を生みます

**出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

??? question "確認問題（4問）"
    **問題.** 要求面の観測状態を障害切り分けで確認します。表示面の対象項目では入力と操作画面応答を照合し、observed valueを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. Desired Status
    - B. INGREQ START
    - C. Observed Status ✅
    - D. INGAMS REFRESH

    正解: **C** ／ 難易度: 初級

    **解説:** 構成面の判定ではCを選び、対象は観測状態棚卸です。記録面の識別語は 観測 状態 で、観測状態棚卸の対象名です。状態面の観測状態復旧は、自動化エージェントが見る現在状態を読むことを目的に扱う説明単位が観測状態照合です。設計面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は観測状態観点です。証跡面の観測状態証跡を読む応答では、observed valueを出典の属性説明と照合する点が観測状態読取です。A: 監査面の観測状態棚卸で見る目標状態は役割が異なり、除外理由を説明する対象は観測状態棚卸です。B: 引継ぎ面の観測状態復旧で見る始動要求は役割が異なり、除外理由を説明する対象は観測状態復旧です。C: 応答面の観測状態照合が正答です。証跡面の観測状態照合応答で確認できる対象は観測状態照合です。D: 定義面の観測状態観点で見るポリシー再読込は役割が異なり、除外理由を説明する対象は観測状態観点です。変更面の初出語説明として、観測状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は観測状態定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 運用面の観測状態を監査記録で確認します。記録面の対象項目では入力と操作画面応答を照合し、observed valueを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. Observed Status ✅
    - B. Suspend Override
    - C. MINOR RESOURCES Policy Item
    - D. Health Status

    正解: **A** ／ 難易度: 初級

    **解説:** 要求面の判定ではAを選び、対象は観測状態監査です。構成面の識別語は 観測 状態 で、観測状態監査の対象名です。定義面の観測状態引継ぎは、自動化エージェントが見る現在状態を読むことを目的に扱う説明単位が観測状態棚卸です。表示面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は観測状態復旧です。状態面の観測状態照合を読む応答では、observed valueを出典の属性説明と照合する点が観測状態観点です。A: 障害面の観測状態監査が正答です。応答面の観測状態監査応答で確認できる対象は観測状態監査です。B: 監査面の観測状態引継ぎで見る一時停止上書きは役割が異なり、除外理由を説明する対象は観測状態引継ぎです。C: 引継ぎ面の観測状態棚卸で見る副資源定義は役割が異なり、除外理由を説明する対象は観測状態棚卸です。D: 応答面の観測状態復旧で見るヘルス状態は役割が異なり、除外理由を説明する対象は観測状態復旧です。設計面の初出語説明として、観測状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は観測状態読取です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 照合面の観測状態を引継ぎ確認で確認します。構成面の対象項目では入力と操作画面応答を照合し、observed valueを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Health Status
    - B. PAM Role
    - C. Observed Status ✅
    - D. INGLIST

    正解: **C** ／ 難易度: 初級

    **解説:** 運用面の判定ではCを選び、対象は観測状態応答です。要求面の識別語は 観測 状態 で、観測状態応答の対象名です。応答面の観測状態保守は、自動化エージェントが見る現在状態を読むことを目的に扱う説明単位が観測状態監査です。記録面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は観測状態引継ぎです。定義面の観測状態棚卸を読む応答では、observed valueを出典の属性説明と照合する点が観測状態復旧です。A: 変更面の観測状態応答で見るヘルス状態は役割が異なり、除外理由を説明する対象は観測状態応答です。B: 障害面の観測状態保守で見る主マネージャー役割は役割が異なり、除外理由を説明する対象は観測状態保守です。C: 監査面の観測状態監査が正答です。定義面の観測状態監査応答で確認できる対象は観測状態監査です。D: 引継ぎ面の観測状態引継ぎで見る資源一覧表示は役割が異なり、除外理由を説明する対象は観測状態引継ぎです。表示面の初出語説明として、観測状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は観測状態観点です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.87

    ---

    **問題.** 優先検分の自動化管理に関する Observed statusの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. INGLIST の結果を残さず優先検分の自動化管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分の自動化管理の証跡として保存して根拠にする。
    - C. Observed statusの変更点を出力本文から切り離して優先検分の自動化管理の承認欄のみ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先検分の確認にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Observed status は「Observed statusの状態と出力メッセージを結び付ける優先検分項目」と INGLIST または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Observed statusの出力行と INGKYST0I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Observed statusを SA z/OS の確認記録に残し、対象名は優先検分対象です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming




## その他

### その他（特定項目に紐づかないQA・手順） {#c36-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（52問）"
    **問題.** 変更面のDb2制御項目をポリシー見直しで確認します。引継ぎ面の対象項目では入力と操作画面応答を照合し、Db2 control settingを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. Observed Status
    - B. Dependency Status
    - C. DB2 CONTROL Policy Item ✅
    - D. INGAMS

    正解: **C** ／ 難易度: 上級

    **解説:** 障害面の判定ではCを選び、対象はDb2制御項目復旧です。監査面の識別語は Db2 制御 ポリシー項目 で、Db2制御項目復旧の対象名です。運用面のDb2制御項目照合は、Db2固有の自動化制御をポリシーで扱うことを目的に扱う説明単位がDb2制御項目観点です。応答面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はDb2制御項目証跡です。要求面のDb2制御項目読取を読む応答では、Db2 control settingを出典の属性説明と照合する点がDb2制御項目状態です。A: 証跡面のDb2制御項目復旧で見る観測状態は役割が異なり、除外理由を説明する対象はDb2制御項目復旧です。B: 復旧面のDb2制御項目照合で見る依存関係状態は役割が異なり、除外理由を説明する対象はDb2制御項目照合です。C: 保守面のDb2制御項目観点が正答です。要求面のDb2制御項目観点応答で確認できる対象はDb2制御項目観点です。D: 照合面のDb2制御項目証跡で見るマネージャー一覧は役割が異なり、除外理由を説明する対象はDb2制御項目証跡です。定義面の初出語説明として、Db2制御項目とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はDb2制御項目根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Defining Automation Policy p.198

    ---

    **問題.** 引継ぎ面の自動化フラグを監査記録で確認します。状態面の対象項目では入力と操作画面応答を照合し、automation flag settingを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. MESSAGES/USER DATA Policy Item
    - B. Automation Flags ✅
    - C. MINOR RESOURCES Policy Item
    - D. DISPSTAT

    正解: **B** ／ 難易度: 中級

    **解説:** 応答面の判定ではBを選び、対象は自動化フラグ証跡です。定義面の識別語は 自動化 フラグ で、自動化フラグ証跡の対象名です。記録面の自動化フラグ読取は、自動化が資源を扱えるかを状態表示で確認することを目的に扱う説明単位が自動化フラグ状態です。証跡面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化フラグ定義です。表示面の自動化フラグ根拠を読む応答では、automation flag settingを出典の属性説明と照合する点が自動化フラグ応答です。A: 照合面の自動化フラグ証跡で見るメッセージ条件は役割が異なり、除外理由を説明する対象は自動化フラグ証跡です。B: 運用面の自動化フラグ読取が正答です。記録面の自動化フラグ読取応答で確認できる対象は自動化フラグ読取です。C: 要求面の自動化フラグ状態で見る副資源定義は役割が異なり、除外理由を説明する対象は自動化フラグ状態です。D: 構成面の自動化フラグ定義で見る状態表示パネルは役割が異なり、除外理由を説明する対象は自動化フラグ定義です。復旧面の初出語説明として、自動化フラグとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化フラグ監査です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 応答面のペーシングゲートを引継ぎ確認で確認します。証跡面の対象項目では入力と操作画面応答を照合し、pacing gate indicatorを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. USS CONTROL Policy Item
    - B. DISPSTAT
    - C. Pacing Gate ✅
    - D. Health Status

    正解: **C** ／ 難易度: 上級

    **解説:** 定義面の判定ではCを選び、対象はペーシングゲート読取です。状態面の識別語は ペーシングゲート で、ペーシングゲート読取の対象名です。表示面のペーシングゲート状態は、資源処理が待たされる理由を表示で追跡することを目的に扱う説明単位がペーシングゲート定義です。復旧面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はペーシングゲート根拠です。設計面のペーシングゲート応答を読む応答では、pacing gate indicatorを出典の属性説明と照合する点がペーシングゲート保守です。A: 運用面のペーシングゲート読取で見るユーエスエス制御項目は役割が異なり、除外理由を説明する対象はペーシングゲート読取です。B: 要求面のペーシングゲート状態で見る状態表示パネルは役割が異なり、除外理由を説明する対象はペーシングゲート状態です。C: 構成面のペーシングゲート定義が正答です。設計面のペーシングゲート定義応答で確認できる対象はペーシングゲート定義です。D: 記録面のペーシングゲート根拠で見るヘルス状態は役割が異なり、除外理由を説明する対象はペーシングゲート根拠です。保守面の初出語説明として、ペーシングゲートとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はペーシングゲート引継ぎです。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 変更面の依存関係状態を障害切り分けで確認します。引継ぎ面の対象項目では入力と操作画面応答を照合し、dependency satisfied fieldを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. PAM Role
    - B. INGSTOBS
    - C. MESSAGES/USER DATA Policy Item
    - D. Dependency Status ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 障害面の判定ではDを選び、対象は依存関係状態読取です。監査面の識別語は 依存関係 状態 で、依存関係状態読取の対象名です。運用面の依存関係状態状態は、依存関係が満たされているかを確認することを目的に扱う説明単位が依存関係状態定義です。応答面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は依存関係状態根拠です。要求面の依存関係状態応答を読む応答では、dependency satisfied fieldを出典の属性説明と照合する点が依存関係状態保守です。A: 証跡面の依存関係状態読取で見る主マネージャー役割は役割が異なり、除外理由を説明する対象は依存関係状態読取です。B: 復旧面の依存関係状態状態で見る状態監視購読は役割が異なり、除外理由を説明する対象は依存関係状態状態です。C: 保守面の依存関係状態定義で見るメッセージ条件は役割が異なり、除外理由を説明する対象は依存関係状態定義です。D: 照合面の依存関係状態根拠が正答です。構成面の依存関係状態根拠応答で確認できる対象は依存関係状態根拠です。定義面の初出語説明として、依存関係状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は依存関係状態引継ぎです。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 障害面の始動要求を監査記録で確認します。応答面の対象項目では入力と操作画面応答を照合し、REQ=始動 requestを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGREQ START ✅
    - B. Suspend Override
    - C. MESSAGES/USER DATA Policy Item
    - D. USS CONTROL Policy Item

    正解: **A** ／ 難易度: 中級

    **解説:** 監査面の判定ではAを選び、対象は始動要求状態です。引継ぎ面の識別語は 要求発行 始動 で、始動要求状態の対象名です。要求面の始動要求定義は、資源を利用可能にする要求を発行することを目的に扱う説明単位が始動要求根拠です。定義面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は始動要求応答です。構成面の始動要求保守を読む応答では、REQ=始動 requestを出典の属性説明と照合する点が始動要求監査です。A: 復旧面の始動要求状態が正答です。運用面の始動要求状態応答で確認できる対象は始動要求状態です。B: 保守面の始動要求定義で見る一時停止上書きは役割が異なり、除外理由を説明する対象は始動要求定義です。C: 照合面の始動要求根拠で見るメッセージ条件は役割が異なり、除外理由を説明する対象は始動要求根拠です。D: 運用面の始動要求応答で見るユーエスエス制御項目は役割が異なり、除外理由を説明する対象は始動要求応答です。状態面の初出語説明として、始動要求とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は始動要求棚卸です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.177

    ---

    **問題.** 監査面の停止要求を引継ぎ確認で確認します。定義面の対象項目では入力と操作画面応答を照合し、REQ=停止 requestを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. IMS CONTROL Policy Item
    - B. INGREQ STOP ✅
    - C. INGINFO
    - D. Automation Status

    正解: **B** ／ 難易度: 中級

    **解説:** 引継ぎ面の判定ではBを選び、対象は停止要求定義です。応答面の識別語は 要求発行 停止 で、停止要求定義の対象名です。構成面の停止要求根拠は、資源を利用不可にする要求を発行することを目的に扱う説明単位が停止要求応答です。状態面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は停止要求保守です。記録面の停止要求監査を読む応答では、REQ=停止 requestを出典の属性説明と照合する点が停止要求引継ぎです。A: 保守面の停止要求定義で見るアイエムエス制御項目は役割が異なり、除外理由を説明する対象は停止要求定義です。B: 照合面の停止要求根拠が正答です。構成面の停止要求根拠応答で確認できる対象は停止要求根拠です。C: 運用面の停止要求応答で見る資源詳細表示は役割が異なり、除外理由を説明する対象は停止要求応答です。D: 要求面の停止要求保守で見る自動化状態は役割が異なり、除外理由を説明する対象は停止要求保守です。証跡面の初出語説明として、停止要求とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は停止要求復旧です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.177

    ---

    **問題.** 引継ぎ面の自動化一時停止をポリシー見直しで確認します。状態面の対象項目では入力と操作画面応答を照合し、REQ=一時停止を記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. INGREQ STOP
    - B. INGAMS
    - C. INGSUSPD SUSPEND ✅
    - D. Configuration Dataset

    正解: **C** ／ 難易度: 上級

    **解説:** 応答面の判定ではCを選び、対象は自動化一時停止根拠です。定義面の識別語は 自動化一時停止 一時停止 で、自動化一時停止根拠の対象名です。記録面の自動化一時停止応答は、資源に対する自動化を一時停止することを目的に扱う説明単位が自動化一時停止保守です。証跡面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化一時停止監査です。表示面の自動化一時停止引継ぎを読む応答では、REQ=一時停止を出典の属性説明と照合する点が自動化一時停止棚卸です。A: 照合面の自動化一時停止根拠で見る停止要求は役割が異なり、除外理由を説明する対象は自動化一時停止根拠です。B: 運用面の自動化一時停止応答で見るマネージャー一覧は役割が異なり、除外理由を説明する対象は自動化一時停止応答です。C: 要求面の自動化一時停止保守が正答です。表示面の自動化一時停止保守応答で確認できる対象は自動化一時停止保守です。D: 構成面の自動化一時停止監査で見る構成データセットは役割が異なり、除外理由を説明する対象は自動化一時停止監査です。復旧面の初出語説明として、自動化一時停止とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化一時停止照合です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.260

    ---

    **問題.** 応答面の自動化再開を運用変更で確認します。証跡面の対象項目では入力と操作画面応答を照合し、resume automationを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. SAM Role
    - B. INGTWS
    - C. TRIGGER Policy Item
    - D. INGSUSPD RESUME ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 定義面の判定ではDを選び、対象は自動化再開応答です。状態面の識別語は 自動化一時停止 再開 で、自動化再開応答の対象名です。表示面の自動化再開保守は、一時停止した自動化を再開することを目的に扱う説明単位が自動化再開監査です。復旧面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化再開引継ぎです。設計面の自動化再開棚卸を読む応答では、resume automationを出典の属性説明と照合する点が自動化再開復旧です。A: 運用面の自動化再開応答で見る副マネージャー役割は役割が異なり、除外理由を説明する対象は自動化再開応答です。B: 要求面の自動化再開保守で見る計画連携要求は役割が異なり、除外理由を説明する対象は自動化再開保守です。C: 構成面の自動化再開監査で見るトリガー定義は役割が異なり、除外理由を説明する対象は自動化再開監査です。D: 記録面の自動化再開引継ぎが正答です。変更面の自動化再開引継ぎ応答で確認できる対象は自動化再開引継ぎです。保守面の初出語説明として、自動化再開とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化再開観点です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.261

    ---

    **問題.** 照合面の構成詳細を障害切り分けで確認します。構成面の対象項目では入力と操作画面応答を照合し、config dataset/memberを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. INGVOTE
    - B. INGAMS Details ✅
    - C. Compound Status
    - D. INGMOVE

    正解: **B** ／ 難易度: 中級

    **解説:** 運用面の判定ではBを選び、対象は構成詳細照合です。要求面の識別語は 自動化マネージャー表示 詳細 で、構成詳細照合の対象名です。応答面の構成詳細観点は、現在の構成データセットとメンバーを確認することを目的に扱う説明単位が構成詳細証跡です。記録面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成詳細読取です。定義面の構成詳細状態を読む応答では、config dataset/memberを出典の属性説明と照合する点が構成詳細定義です。A: 変更面の構成詳細照合で見る投票表示は役割が異なり、除外理由を説明する対象は構成詳細照合です。B: 障害面の構成詳細観点が正答です。応答面の構成詳細観点応答で確認できる対象は構成詳細観点です。C: 監査面の構成詳細証跡で見る複合状態は役割が異なり、除外理由を説明する対象は構成詳細証跡です。D: 引継ぎ面の構成詳細読取で見る移動要求は役割が異なり、除外理由を説明する対象は構成詳細読取です。表示面の初出語説明として、構成詳細とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成詳細応答です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 運用面の診断機能を監査記録で確認します。記録面の対象項目では入力と操作画面応答を照合し、diagnostic optionを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGAMS REFRESH
    - B. SAM Role
    - C. INGAMS Diagnostic ✅
    - D. APPLICATION Entry Type

    正解: **C** ／ 難易度: 上級

    **解説:** 要求面の判定ではCを選び、対象は診断機能観点です。構成面の識別語は 自動化マネージャー表示 診断 で、診断機能観点の対象名です。定義面の診断機能証跡は、状態イメージや作業統計などを診断することを目的に扱う説明単位が診断機能読取です。表示面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は診断機能状態です。状態面の診断機能定義を読む応答では、diagnostic optionを出典の属性説明と照合する点が診断機能根拠です。A: 障害面の診断機能観点で見るポリシー再読込は役割が異なり、除外理由を説明する対象は診断機能観点です。B: 監査面の診断機能証跡で見る副マネージャー役割は役割が異なり、除外理由を説明する対象は診断機能証跡です。C: 引継ぎ面の診断機能読取が正答です。状態面の診断機能読取応答で確認できる対象は診断機能読取です。D: 応答面の診断機能状態で見るアプリケーション定義は役割が異なり、除外理由を説明する対象は診断機能状態です。設計面の初出語説明として、診断機能とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は診断機能保守です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.242

    ---

    **問題.** 要求面の制御ファイル読込を引継ぎ確認で確認します。表示面の対象項目では入力と操作画面応答を照合し、制御ファイル load processを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. PAM Role
    - B. INGSTOBS
    - C. MESSAGES/USER DATA Policy Item
    - D. ACF Load ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 構成面の判定ではDを選び、対象は制御ファイル読込証跡です。記録面の識別語は 制御ファイル 読込 で、制御ファイル読込証跡の対象名です。状態面の制御ファイル読込読取は、自動化 Control Fileの読込状態を確認することを目的に扱う説明単位が制御ファイル読込状態です。設計面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は制御ファイル読込定義です。証跡面の制御ファイル読込根拠を読む応答では、制御ファイル load processを出典の属性説明と照合する点が制御ファイル読込応答です。A: 監査面の制御ファイル読込証跡で見る主マネージャー役割は役割が異なり、除外理由を説明する対象は制御ファイル読込証跡です。B: 引継ぎ面の制御ファイル読込読取で見る状態監視購読は役割が異なり、除外理由を説明する対象は制御ファイル読込読取です。C: 応答面の制御ファイル読込状態で見るメッセージ条件は役割が異なり、除外理由を説明する対象は制御ファイル読込状態です。D: 定義面の制御ファイル読込定義が正答です。復旧面の制御ファイル読込定義応答で確認できる対象は制御ファイル読込定義です。変更面の初出語説明として、制御ファイル読込とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は制御ファイル読込監査です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Messages and Codes p.251

    ---

    **問題.** 設計面の構成データセットを監査記録で確認します。監査面の対象項目では入力と操作画面応答を照合し、Config dataset nameを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. SERVICE PERIOD Policy Item
    - B. USS CONTROL Policy Item
    - C. INGVOTE
    - D. Configuration Dataset ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更面の判定ではDを選び、対象は構成データセット根拠です。障害面の識別語は 構成 データセット で、構成データセット根拠の対象名です。照合面の構成データセット応答は、構成ファイルを格納するデータセット名を記録することを目的に扱う説明単位が構成データセット保守です。引継ぎ面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成データセット監査です。運用面の構成データセット引継ぎを読む応答では、Config dataset nameを出典の属性説明と照合する点が構成データセット棚卸です。A: 状態面の構成データセット根拠で見るサービス期間は役割が異なり、除外理由を説明する対象は構成データセット根拠です。B: 証跡面の構成データセット応答で見るユーエスエス制御項目は役割が異なり、除外理由を説明する対象は構成データセット応答です。C: 復旧面の構成データセット保守で見る投票表示は役割が異なり、除外理由を説明する対象は構成データセット保守です。D: 保守面の構成データセット監査が正答です。要求面の構成データセット監査応答で確認できる対象は構成データセット監査です。応答面の初出語説明として、構成データセットとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成データセット照合です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 変更面の構成メンバーを引継ぎ確認で確認します。引継ぎ面の対象項目では入力と操作画面応答を照合し、Config memberを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Configuration Member ✅
    - B. INGFILT
    - C. Automation Status
    - D. INGSET

    正解: **A** ／ 難易度: 中級

    **解説:** 障害面の判定ではAを選び、対象は構成メンバー応答です。監査面の識別語は 構成 メンバー で、構成メンバー応答の対象名です。運用面の構成メンバー保守は、読み込まれている構成メンバー名を記録することを目的に扱う説明単位が構成メンバー監査です。応答面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成メンバー引継ぎです。要求面の構成メンバー棚卸を読む応答では、Config memberを出典の属性説明と照合する点が構成メンバー復旧です。A: 証跡面の構成メンバー応答が正答です。照合面の構成メンバー応答応答で確認できる対象は構成メンバー応答です。B: 復旧面の構成メンバー保守で見る表示フィルターは役割が異なり、除外理由を説明する対象は構成メンバー保守です。C: 保守面の構成メンバー監査で見る自動化状態は役割が異なり、除外理由を説明する対象は構成メンバー監査です。D: 照合面の構成メンバー引継ぎで見る状態属性設定は役割が異なり、除外理由を説明する対象は構成メンバー引継ぎです。定義面の初出語説明として、構成メンバーとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成メンバー観点です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 応答面のタイマー再開を監査記録で確認します。証跡面の対象項目では入力と操作画面応答を照合し、resume suspended timerを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. Timer Resume ✅
    - B. Pacing Gate
    - C. INGFILT
    - D. Dependency Status

    正解: **A** ／ 難易度: 中級

    **解説:** 定義面の判定ではAを選び、対象はタイマー再開棚卸です。状態面の識別語は タイマー Resume で、タイマー再開棚卸の対象名です。表示面のタイマー再開復旧は、停止中のタイマーを再開または再活性化することを目的に扱う説明単位がタイマー再開照合です。復旧面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はタイマー再開観点です。設計面のタイマー再開証跡を読む応答では、resume suspended timerを出典の属性説明と照合する点がタイマー再開読取です。A: 運用面のタイマー再開棚卸が正答です。記録面のタイマー再開棚卸応答で確認できる対象はタイマー再開棚卸です。B: 要求面のタイマー再開復旧で見るペーシングゲートは役割が異なり、除外理由を説明する対象はタイマー再開復旧です。C: 構成面のタイマー再開照合で見る表示フィルターは役割が異なり、除外理由を説明する対象はタイマー再開照合です。D: 記録面のタイマー再開観点で見る依存関係状態は役割が異なり、除外理由を説明する対象はタイマー再開観点です。保守面の初出語説明として、タイマー再開とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はタイマー再開定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.161

    ---

    **問題.** 定義面の一時停止上書きを引継ぎ確認で確認します。復旧面の対象項目では入力と操作画面応答を照合し、OVERRIDE=SUSを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. INGSUSPD RESUME
    - B. Suspend Override ✅
    - C. INGAMS REFRESH
    - D. Configuration Member

    正解: **B** ／ 難易度: 上級

    **解説:** 状態面の判定ではBを選び、対象は一時停止上書き復旧です。証跡面の識別語は Suspend 上書き で、一時停止上書き復旧の対象名です。設計面の一時停止上書き照合は、停止要求を上書きして始動する条件を確認することを目的に扱う説明単位が一時停止上書き観点です。保守面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は一時停止上書き証跡です。変更面の一時停止上書き読取を読む応答では、OVERRIDE=SUSを出典の属性説明と照合する点が一時停止上書き状態です。A: 要求面の一時停止上書き復旧で見る自動化再開は役割が異なり、除外理由を説明する対象は一時停止上書き復旧です。B: 構成面の一時停止上書き照合が正答です。設計面の一時停止上書き照合応答で確認できる対象は一時停止上書き照合です。C: 記録面の一時停止上書き観点で見るポリシー再読込は役割が異なり、除外理由を説明する対象は一時停止上書き観点です。D: 表示面の一時停止上書き証跡で見る構成メンバーは役割が異なり、除外理由を説明する対象は一時停止上書き証跡です。照合面の初出語説明として、一時停止上書きとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は一時停止上書き根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.220

    ---

    **問題.** 設計面のDb2制御項目を運用変更で確認します。監査面の対象項目では入力と操作画面応答を照合し、Db2 control settingを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. DB2 CONTROL Policy Item ✅
    - B. Timer Resume
    - C. THRESHOLDS Policy Item
    - D. Compound Status

    正解: **A** ／ 難易度: 上級

    **解説:** 変更面の判定ではAを選び、対象はDb2制御項目引継ぎです。障害面の識別語は Db2 制御 ポリシー項目 で、Db2制御項目引継ぎの対象名です。照合面のDb2制御項目棚卸は、Db2固有の自動化制御をポリシーで扱うことを目的に扱う説明単位がDb2制御項目復旧です。引継ぎ面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はDb2制御項目照合です。運用面のDb2制御項目観点を読む応答では、Db2 control settingを出典の属性説明と照合する点がDb2制御項目証跡です。A: 状態面のDb2制御項目引継ぎが正答です。保守面のDb2制御項目引継ぎ応答で確認できる対象はDb2制御項目引継ぎです。B: 証跡面のDb2制御項目棚卸で見るタイマー再開は役割が異なり、除外理由を説明する対象はDb2制御項目棚卸です。C: 復旧面のDb2制御項目復旧で見るしきい値定義は役割が異なり、除外理由を説明する対象はDb2制御項目復旧です。D: 保守面のDb2制御項目照合で見る複合状態は役割が異なり、除外理由を説明する対象はDb2制御項目照合です。応答面の初出語説明として、Db2制御項目とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はDb2制御項目状態です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Defining Automation Policy p.198

    ---

    **問題.** 監査面の自動化フラグを引継ぎ確認で確認します。定義面の対象項目では入力と操作画面応答を照合し、automation flag settingを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. INGSUSPD RESUME
    - B. PAM Role
    - C. SERVICE PERIOD Policy Item
    - D. Automation Flags ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 引継ぎ面の判定ではDを選び、対象は自動化フラグ照合です。応答面の識別語は 自動化 フラグ で、自動化フラグ照合の対象名です。構成面の自動化フラグ観点は、自動化が資源を扱えるかを状態表示で確認することを目的に扱う説明単位が自動化フラグ証跡です。状態面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化フラグ読取です。記録面の自動化フラグ状態を読む応答では、automation flag settingを出典の属性説明と照合する点が自動化フラグ定義です。A: 保守面の自動化フラグ照合で見る自動化再開は役割が異なり、除外理由を説明する対象は自動化フラグ照合です。B: 照合面の自動化フラグ観点で見る主マネージャー役割は役割が異なり、除外理由を説明する対象は自動化フラグ観点です。C: 運用面の自動化フラグ証跡で見るサービス期間は役割が異なり、除外理由を説明する対象は自動化フラグ証跡です。D: 要求面の自動化フラグ読取が正答です。表示面の自動化フラグ読取応答で確認できる対象は自動化フラグ読取です。証跡面の初出語説明として、自動化フラグとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化フラグ応答です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 引継ぎ面のペーシングゲートをポリシー見直しで確認します。状態面の対象項目では入力と操作画面応答を照合し、pacing gate indicatorを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. Pacing Gate ✅
    - B. ACF Load
    - C. Suspend Override
    - D. INGINFO

    正解: **A** ／ 難易度: 上級

    **解説:** 応答面の判定ではAを選び、対象はペーシングゲート観点です。定義面の識別語は ペーシングゲート で、ペーシングゲート観点の対象名です。記録面のペーシングゲート証跡は、資源処理が待たされる理由を表示で追跡することを目的に扱う説明単位がペーシングゲート読取です。証跡面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はペーシングゲート状態です。表示面のペーシングゲート定義を読む応答では、pacing gate indicatorを出典の属性説明と照合する点がペーシングゲート根拠です。A: 照合面のペーシングゲート観点が正答です。構成面のペーシングゲート観点応答で確認できる対象はペーシングゲート観点です。B: 運用面のペーシングゲート証跡で見る制御ファイル読込は役割が異なり、除外理由を説明する対象はペーシングゲート証跡です。C: 要求面のペーシングゲート読取で見る一時停止上書きは役割が異なり、除外理由を説明する対象はペーシングゲート読取です。D: 構成面のペーシングゲート状態で見る資源詳細表示は役割が異なり、除外理由を説明する対象はペーシングゲート状態です。復旧面の初出語説明として、ペーシングゲートとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はペーシングゲート保守です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 設計面の依存関係状態を監査記録で確認します。監査面の対象項目では入力と操作画面応答を照合し、dependency satisfied fieldを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. DISPINFO
    - B. Dependency Status ✅
    - C. INGREQ START
    - D. Configuration Member

    正解: **B** ／ 難易度: 上級

    **解説:** 変更面の判定ではBを選び、対象は依存関係状態観点です。障害面の識別語は 依存関係 状態 で、依存関係状態観点の対象名です。照合面の依存関係状態証跡は、依存関係が満たされているかを確認することを目的に扱う説明単位が依存関係状態読取です。引継ぎ面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は依存関係状態状態です。運用面の依存関係状態定義を読む応答では、dependency satisfied fieldを出典の属性説明と照合する点が依存関係状態根拠です。A: 状態面の依存関係状態観点で見るエージェント視点表示は役割が異なり、除外理由を説明する対象は依存関係状態観点です。B: 証跡面の依存関係状態証跡が正答です。照合面の依存関係状態証跡応答で確認できる対象は依存関係状態証跡です。C: 復旧面の依存関係状態読取で見る始動要求は役割が異なり、除外理由を説明する対象は依存関係状態読取です。D: 保守面の依存関係状態状態で見る構成メンバーは役割が異なり、除外理由を説明する対象は依存関係状態状態です。応答面の初出語説明として、依存関係状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は依存関係状態保守です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 変更面の始動要求を引継ぎ確認で確認します。引継ぎ面の対象項目では入力と操作画面応答を照合し、REQ=始動 requestを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Compound Status
    - B. INGAMS REFRESH
    - C. INGREQ START ✅
    - D. STARTUP Policy Item

    正解: **C** ／ 難易度: 中級

    **解説:** 障害面の判定ではCを選び、対象は始動要求証跡です。監査面の識別語は 要求発行 始動 で、始動要求証跡の対象名です。運用面の始動要求読取は、資源を利用可能にする要求を発行することを目的に扱う説明単位が始動要求状態です。応答面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は始動要求定義です。要求面の始動要求根拠を読む応答では、REQ=始動 requestを出典の属性説明と照合する点が始動要求応答です。A: 証跡面の始動要求証跡で見る複合状態は役割が異なり、除外理由を説明する対象は始動要求証跡です。B: 復旧面の始動要求読取で見るポリシー再読込は役割が異なり、除外理由を説明する対象は始動要求読取です。C: 保守面の始動要求状態が正答です。要求面の始動要求状態応答で確認できる対象は始動要求状態です。D: 照合面の始動要求定義で見る始動ポリシーは役割が異なり、除外理由を説明する対象は始動要求定義です。定義面の初出語説明として、始動要求とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は始動要求監査です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.177

    ---

    **問題.** 障害面の停止要求をポリシー見直しで確認します。応答面の対象項目では入力と操作画面応答を照合し、REQ=停止 requestを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. INGAMS Diagnostic
    - B. Timer Resume
    - C. Pacing Gate
    - D. INGREQ STOP ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 監査面の判定ではDを選び、対象は停止要求読取です。引継ぎ面の識別語は 要求発行 停止 で、停止要求読取の対象名です。要求面の停止要求状態は、資源を利用不可にする要求を発行することを目的に扱う説明単位が停止要求定義です。定義面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は停止要求根拠です。構成面の停止要求応答を読む応答では、REQ=停止 requestを出典の属性説明と照合する点が停止要求保守です。A: 復旧面の停止要求読取で見る診断機能は役割が異なり、除外理由を説明する対象は停止要求読取です。B: 保守面の停止要求状態で見るタイマー再開は役割が異なり、除外理由を説明する対象は停止要求状態です。C: 照合面の停止要求定義で見るペーシングゲートは役割が異なり、除外理由を説明する対象は停止要求定義です。D: 運用面の停止要求根拠が正答です。記録面の停止要求根拠応答で確認できる対象は停止要求根拠です。状態面の初出語説明として、停止要求とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は停止要求引継ぎです。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.177

    ---

    **問題.** 監査面の自動化一時停止を運用変更で確認します。定義面の対象項目では入力と操作画面応答を照合し、REQ=一時停止を記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. INGSUSPD SUSPEND ✅
    - B. CONDITION Policy Item
    - C. INGINFO
    - D. INGMOVE

    正解: **A** ／ 難易度: 上級

    **解説:** 引継ぎ面の判定ではAを選び、対象は自動化一時停止状態です。応答面の識別語は 自動化一時停止 一時停止 で、自動化一時停止状態の対象名です。構成面の自動化一時停止定義は、資源に対する自動化を一時停止することを目的に扱う説明単位が自動化一時停止根拠です。状態面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化一時停止応答です。記録面の自動化一時停止保守を読む応答では、REQ=一時停止を出典の属性説明と照合する点が自動化一時停止監査です。A: 保守面の自動化一時停止状態が正答です。要求面の自動化一時停止状態応答で確認できる対象は自動化一時停止状態です。B: 照合面の自動化一時停止定義で見る条件定義は役割が異なり、除外理由を説明する対象は自動化一時停止定義です。C: 運用面の自動化一時停止根拠で見る資源詳細表示は役割が異なり、除外理由を説明する対象は自動化一時停止根拠です。D: 要求面の自動化一時停止応答で見る移動要求は役割が異なり、除外理由を説明する対象は自動化一時停止応答です。証跡面の初出語説明として、自動化一時停止とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化一時停止棚卸です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.260

    ---

    **問題.** 引継ぎ面の自動化再開を障害切り分けで確認します。状態面の対象項目では入力と操作画面応答を照合し、resume automationを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. DISPSTAT
    - B. INGSUSPD RESUME ✅
    - C. INGREQ START
    - D. INGRCHCK

    正解: **B** ／ 難易度: 上級

    **解説:** 応答面の判定ではBを選び、対象は自動化再開定義です。定義面の識別語は 自動化一時停止 再開 で、自動化再開定義の対象名です。記録面の自動化再開根拠は、一時停止した自動化を再開することを目的に扱う説明単位が自動化再開応答です。証跡面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化再開保守です。表示面の自動化再開監査を読む応答では、resume automationを出典の属性説明と照合する点が自動化再開引継ぎです。A: 照合面の自動化再開定義で見る状態表示パネルは役割が異なり、除外理由を説明する対象は自動化再開定義です。B: 運用面の自動化再開根拠が正答です。記録面の自動化再開根拠応答で確認できる対象は自動化再開根拠です。C: 要求面の自動化再開応答で見る始動要求は役割が異なり、除外理由を説明する対象は自動化再開応答です。D: 構成面の自動化再開保守で見る資源状態待機は役割が異なり、除外理由を説明する対象は自動化再開保守です。復旧面の初出語説明として、自動化再開とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化再開復旧です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.261

    ---

    **問題.** 保守面の構成詳細を監査記録で確認します。要求面の対象項目では入力と操作画面応答を照合し、config dataset/memberを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGTWS
    - B. SERVICE PERIOD Policy Item
    - C. Desired Status
    - D. INGAMS Details ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 照合面の判定ではDを選び、対象は構成詳細棚卸です。運用面の識別語は 自動化マネージャー表示 詳細 で、構成詳細棚卸の対象名です。引継ぎ面の構成詳細復旧は、現在の構成データセットとメンバーを確認することを目的に扱う説明単位が構成詳細照合です。構成面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成詳細観点です。応答面の構成詳細証跡を読む応答では、config dataset/memberを出典の属性説明と照合する点が構成詳細読取です。A: 設計面の構成詳細棚卸で見る計画連携要求は役割が異なり、除外理由を説明する対象は構成詳細棚卸です。B: 変更面の構成詳細復旧で見るサービス期間は役割が異なり、除外理由を説明する対象は構成詳細復旧です。C: 障害面の構成詳細照合で見る目標状態は役割が異なり、除外理由を説明する対象は構成詳細照合です。D: 監査面の構成詳細観点が正答です。定義面の構成詳細観点応答で確認できる対象は構成詳細観点です。記録面の初出語説明として、構成詳細とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成詳細定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 照合面の診断機能を引継ぎ確認で確認します。構成面の対象項目では入力と操作画面応答を照合し、diagnostic optionを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. INGAMS Diagnostic ✅
    - B. Automation Flags
    - C. Desired Status
    - D. Agent READY Status

    正解: **A** ／ 難易度: 上級

    **解説:** 運用面の判定ではAを選び、対象は診断機能復旧です。要求面の識別語は 自動化マネージャー表示 診断 で、診断機能復旧の対象名です。応答面の診断機能照合は、状態イメージや作業統計などを診断することを目的に扱う説明単位が診断機能観点です。記録面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は診断機能証跡です。定義面の診断機能読取を読む応答では、diagnostic optionを出典の属性説明と照合する点が診断機能状態です。A: 変更面の診断機能復旧が正答です。引継ぎ面の診断機能復旧応答で確認できる対象は診断機能復旧です。B: 障害面の診断機能照合で見る自動化フラグは役割が異なり、除外理由を説明する対象は診断機能照合です。C: 監査面の診断機能観点で見る目標状態は役割が異なり、除外理由を説明する対象は診断機能観点です。D: 引継ぎ面の診断機能証跡で見るエージェント準備状態は役割が異なり、除外理由を説明する対象は診断機能証跡です。表示面の初出語説明として、診断機能とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は診断機能根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.242

    ---

    **問題.** 運用面の制御ファイル読込をポリシー見直しで確認します。記録面の対象項目では入力と操作画面応答を照合し、制御ファイル load processを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. DISPINFO
    - B. ACF Load ✅
    - C. Dependency Status
    - D. Configuration Member

    正解: **B** ／ 難易度: 上級

    **解説:** 要求面の判定ではBを選び、対象は制御ファイル読込照合です。構成面の識別語は 制御ファイル 読込 で、制御ファイル読込照合の対象名です。定義面の制御ファイル読込観点は、自動化 Control Fileの読込状態を確認することを目的に扱う説明単位が制御ファイル読込証跡です。表示面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は制御ファイル読込読取です。状態面の制御ファイル読込状態を読む応答では、制御ファイル load processを出典の属性説明と照合する点が制御ファイル読込定義です。A: 障害面の制御ファイル読込照合で見るエージェント視点表示は役割が異なり、除外理由を説明する対象は制御ファイル読込照合です。B: 監査面の制御ファイル読込観点が正答です。定義面の制御ファイル読込観点応答で確認できる対象は制御ファイル読込観点です。C: 引継ぎ面の制御ファイル読込証跡で見る依存関係状態は役割が異なり、除外理由を説明する対象は制御ファイル読込証跡です。D: 応答面の制御ファイル読込読取で見る構成メンバーは役割が異なり、除外理由を説明する対象は制御ファイル読込読取です。設計面の初出語説明として、制御ファイル読込とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は制御ファイル読込応答です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Messages and Codes p.251

    ---

    **問題.** 表示面の構成データセットを引継ぎ確認で確認します。障害面の対象項目では入力と操作画面応答を照合し、Config dataset nameを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. INGMOVE
    - B. Configuration Dataset ✅
    - C. Configuration Member
    - D. DB2 CONTROL Policy Item

    正解: **B** ／ 難易度: 中級

    **解説:** 設計面の判定ではBを選び、対象は構成データセット状態です。変更面の識別語は 構成 データセット で、構成データセット状態の対象名です。保守面の構成データセット定義は、構成ファイルを格納するデータセット名を記録することを目的に扱う説明単位が構成データセット根拠です。監査面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成データセット応答です。照合面の構成データセット保守を読む応答では、Config dataset nameを出典の属性説明と照合する点が構成データセット監査です。A: 定義面の構成データセット状態で見る移動要求は役割が異なり、除外理由を説明する対象は構成データセット状態です。B: 状態面の構成データセット定義が正答です。保守面の構成データセット定義応答で確認できる対象は構成データセット定義です。C: 証跡面の構成データセット根拠で見る構成メンバーは役割が異なり、除外理由を説明する対象は構成データセット根拠です。D: 復旧面の構成データセット応答で見るDb2制御項目は役割が異なり、除外理由を説明する対象は構成データセット応答です。引継ぎ面の初出語説明として、構成データセットとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成データセット棚卸です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 設計面の構成メンバーをポリシー見直しで確認します。監査面の対象項目では入力と操作画面応答を照合し、Config memberを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. INGSTOBS
    - B. CONDITION Policy Item
    - C. Configuration Member ✅
    - D. Observed Status

    正解: **C** ／ 難易度: 中級

    **解説:** 変更面の判定ではCを選び、対象は構成メンバー定義です。障害面の識別語は 構成 メンバー で、構成メンバー定義の対象名です。照合面の構成メンバー根拠は、読み込まれている構成メンバー名を記録することを目的に扱う説明単位が構成メンバー応答です。引継ぎ面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成メンバー保守です。運用面の構成メンバー監査を読む応答では、Config memberを出典の属性説明と照合する点が構成メンバー引継ぎです。A: 状態面の構成メンバー定義で見る状態監視購読は役割が異なり、除外理由を説明する対象は構成メンバー定義です。B: 証跡面の構成メンバー根拠で見る条件定義は役割が異なり、除外理由を説明する対象は構成メンバー根拠です。C: 復旧面の構成メンバー応答が正答です。運用面の構成メンバー応答応答で確認できる対象は構成メンバー応答です。D: 保守面の構成メンバー保守で見る観測状態は役割が異なり、除外理由を説明する対象は構成メンバー保守です。応答面の初出語説明として、構成メンバーとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成メンバー復旧です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 引継ぎ面のタイマー再開を引継ぎ確認で確認します。状態面の対象項目では入力と操作画面応答を照合し、resume suspended timerを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Agent READY Status
    - B. Application Group
    - C. Timer Resume ✅
    - D. DISPINFO

    正解: **C** ／ 難易度: 中級

    **解説:** 応答面の判定ではCを選び、対象はタイマー再開監査です。定義面の識別語は タイマー Resume で、タイマー再開監査の対象名です。記録面のタイマー再開引継ぎは、停止中のタイマーを再開または再活性化することを目的に扱う説明単位がタイマー再開棚卸です。証跡面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はタイマー再開復旧です。表示面のタイマー再開照合を読む応答では、resume suspended timerを出典の属性説明と照合する点がタイマー再開観点です。A: 照合面のタイマー再開監査で見るエージェント準備状態は役割が異なり、除外理由を説明する対象はタイマー再開監査です。B: 運用面のタイマー再開引継ぎで見るアプリケーショングループは役割が異なり、除外理由を説明する対象はタイマー再開引継ぎです。C: 要求面のタイマー再開棚卸が正答です。表示面のタイマー再開棚卸応答で確認できる対象はタイマー再開棚卸です。D: 構成面のタイマー再開復旧で見るエージェント視点表示は役割が異なり、除外理由を説明する対象はタイマー再開復旧です。復旧面の初出語説明として、タイマー再開とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はタイマー再開読取です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.161

    ---

    **問題.** 応答面の一時停止上書きをポリシー見直しで確認します。証跡面の対象項目では入力と操作画面応答を照合し、OVERRIDE=SUSを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. THRESHOLDS Policy Item
    - B. DISPSTAT
    - C. INGGROUP
    - D. Suspend Override ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 定義面の判定ではDを選び、対象は一時停止上書き引継ぎです。状態面の識別語は Suspend 上書き で、一時停止上書き引継ぎの対象名です。表示面の一時停止上書き棚卸は、停止要求を上書きして始動する条件を確認することを目的に扱う説明単位が一時停止上書き復旧です。復旧面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は一時停止上書き照合です。設計面の一時停止上書き観点を読む応答では、OVERRIDE=SUSを出典の属性説明と照合する点が一時停止上書き証跡です。A: 運用面の一時停止上書き引継ぎで見るしきい値定義は役割が異なり、除外理由を説明する対象は一時停止上書き引継ぎです。B: 要求面の一時停止上書き棚卸で見る状態表示パネルは役割が異なり、除外理由を説明する対象は一時停止上書き棚卸です。C: 構成面の一時停止上書き復旧で見るグループ要求は役割が異なり、除外理由を説明する対象は一時停止上書き復旧です。D: 記録面の一時停止上書き照合が正答です。変更面の一時停止上書き照合応答で確認できる対象は一時停止上書き照合です。保守面の初出語説明として、一時停止上書きとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は一時停止上書き状態です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.220

    ---

    **問題.** 表示面のDb2制御項目を障害切り分けで確認します。障害面の対象項目では入力と操作画面応答を照合し、Db2 control settingを記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. Compound Status
    - B. Agent READY Status
    - C. DB2 CONTROL Policy Item ✅
    - D. INGLIST

    正解: **C** ／ 難易度: 上級

    **解説:** 設計面の判定ではCを選び、対象はDb2制御項目保守です。変更面の識別語は Db2 制御 ポリシー項目 で、Db2制御項目保守の対象名です。保守面のDb2制御項目監査は、Db2固有の自動化制御をポリシーで扱うことを目的に扱う説明単位がDb2制御項目引継ぎです。監査面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はDb2制御項目棚卸です。照合面のDb2制御項目復旧を読む応答では、Db2 control settingを出典の属性説明と照合する点がDb2制御項目照合です。A: 定義面のDb2制御項目保守で見る複合状態は役割が異なり、除外理由を説明する対象はDb2制御項目保守です。B: 状態面のDb2制御項目監査で見るエージェント準備状態は役割が異なり、除外理由を説明する対象はDb2制御項目監査です。C: 証跡面のDb2制御項目引継ぎが正答です。照合面のDb2制御項目引継ぎ応答で確認できる対象はDb2制御項目引継ぎです。D: 復旧面のDb2制御項目棚卸で見る資源一覧表示は役割が異なり、除外理由を説明する対象はDb2制御項目棚卸です。引継ぎ面の初出語説明として、Db2制御項目とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はDb2制御項目証跡です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Defining Automation Policy p.198

    ---

    **問題.** 障害面の自動化フラグをポリシー見直しで確認します。応答面の対象項目では入力と操作画面応答を照合し、automation flag settingを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. SERVICE PERIOD Policy Item
    - B. Automation Flags ✅
    - C. Desired Status
    - D. INGTWS

    正解: **B** ／ 難易度: 中級

    **解説:** 監査面の判定ではBを選び、対象は自動化フラグ棚卸です。引継ぎ面の識別語は 自動化 フラグ で、自動化フラグ棚卸の対象名です。要求面の自動化フラグ復旧は、自動化が資源を扱えるかを状態表示で確認することを目的に扱う説明単位が自動化フラグ照合です。定義面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化フラグ観点です。構成面の自動化フラグ証跡を読む応答では、automation flag settingを出典の属性説明と照合する点が自動化フラグ読取です。A: 復旧面の自動化フラグ棚卸で見るサービス期間は役割が異なり、除外理由を説明する対象は自動化フラグ棚卸です。B: 保守面の自動化フラグ復旧が正答です。要求面の自動化フラグ復旧応答で確認できる対象は自動化フラグ復旧です。C: 照合面の自動化フラグ照合で見る目標状態は役割が異なり、除外理由を説明する対象は自動化フラグ照合です。D: 運用面の自動化フラグ観点で見る計画連携要求は役割が異なり、除外理由を説明する対象は自動化フラグ観点です。状態面の初出語説明として、自動化フラグとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化フラグ定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 監査面のペーシングゲートを運用変更で確認します。定義面の対象項目では入力と操作画面応答を照合し、pacing gate indicatorを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. INGINFO
    - B. INGSUSPD RESUME
    - C. Pacing Gate ✅
    - D. TRIGGER Policy Item

    正解: **C** ／ 難易度: 上級

    **解説:** 引継ぎ面の判定ではCを選び、対象はペーシングゲート復旧です。応答面の識別語は ペーシングゲート で、ペーシングゲート復旧の対象名です。構成面のペーシングゲート照合は、資源処理が待たされる理由を表示で追跡することを目的に扱う説明単位がペーシングゲート観点です。状態面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はペーシングゲート証跡です。記録面のペーシングゲート読取を読む応答では、pacing gate indicatorを出典の属性説明と照合する点がペーシングゲート状態です。A: 保守面のペーシングゲート復旧で見る資源詳細表示は役割が異なり、除外理由を説明する対象はペーシングゲート復旧です。B: 照合面のペーシングゲート照合で見る自動化再開は役割が異なり、除外理由を説明する対象はペーシングゲート照合です。C: 運用面のペーシングゲート観点が正答です。記録面のペーシングゲート観点応答で確認できる対象はペーシングゲート観点です。D: 要求面のペーシングゲート証跡で見るトリガー定義は役割が異なり、除外理由を説明する対象はペーシングゲート証跡です。証跡面の初出語説明として、ペーシングゲートとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はペーシングゲート根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 表示面の依存関係状態を引継ぎ確認で確認します。障害面の対象項目では入力と操作画面応答を照合し、dependency satisfied fieldを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Configuration Member
    - B. MINOR RESOURCES Policy Item
    - C. INGGROUP
    - D. Dependency Status ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 設計面の判定ではDを選び、対象は依存関係状態復旧です。変更面の識別語は 依存関係 状態 で、依存関係状態復旧の対象名です。保守面の依存関係状態照合は、依存関係が満たされているかを確認することを目的に扱う説明単位が依存関係状態観点です。監査面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は依存関係状態証跡です。照合面の依存関係状態読取を読む応答では、dependency satisfied fieldを出典の属性説明と照合する点が依存関係状態状態です。A: 定義面の依存関係状態復旧で見る構成メンバーは役割が異なり、除外理由を説明する対象は依存関係状態復旧です。B: 状態面の依存関係状態照合で見る副資源定義は役割が異なり、除外理由を説明する対象は依存関係状態照合です。C: 証跡面の依存関係状態観点で見るグループ要求は役割が異なり、除外理由を説明する対象は依存関係状態観点です。D: 復旧面の依存関係状態証跡が正答です。運用面の依存関係状態証跡応答で確認できる対象は依存関係状態証跡です。引継ぎ面の初出語説明として、依存関係状態とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は依存関係状態根拠です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.137

    ---

    **問題.** 設計面の始動要求をポリシー見直しで確認します。監査面の対象項目では入力と操作画面応答を照合し、REQ=始動 requestを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. INGREQ START ✅
    - B. STARTUP Policy Item
    - C. DISPINFO
    - D. SAM Role

    正解: **A** ／ 難易度: 中級

    **解説:** 変更面の判定ではAを選び、対象は始動要求照合です。障害面の識別語は 要求発行 始動 で、始動要求照合の対象名です。照合面の始動要求観点は、資源を利用可能にする要求を発行することを目的に扱う説明単位が始動要求証跡です。引継ぎ面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は始動要求読取です。運用面の始動要求状態を読む応答では、REQ=始動 requestを出典の属性説明と照合する点が始動要求定義です。A: 状態面の始動要求照合が正答です。保守面の始動要求照合応答で確認できる対象は始動要求照合です。B: 証跡面の始動要求観点で見る始動ポリシーは役割が異なり、除外理由を説明する対象は始動要求観点です。C: 復旧面の始動要求証跡で見るエージェント視点表示は役割が異なり、除外理由を説明する対象は始動要求証跡です。D: 保守面の始動要求読取で見る副マネージャー役割は役割が異なり、除外理由を説明する対象は始動要求読取です。応答面の初出語説明として、始動要求とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は始動要求応答です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.177

    ---

    **問題.** 変更面の停止要求を運用変更で確認します。引継ぎ面の対象項目では入力と操作画面応答を照合し、REQ=停止 requestを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. Pacing Gate
    - B. INGREQ STOP ✅
    - C. INGSUSPD SUSPEND
    - D. MESSAGES/USER DATA Policy Item

    正解: **B** ／ 難易度: 中級

    **解説:** 障害面の判定ではBを選び、対象は停止要求観点です。監査面の識別語は 要求発行 停止 で、停止要求観点の対象名です。運用面の停止要求証跡は、資源を利用不可にする要求を発行することを目的に扱う説明単位が停止要求読取です。応答面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は停止要求状態です。要求面の停止要求定義を読む応答では、REQ=停止 requestを出典の属性説明と照合する点が停止要求根拠です。A: 証跡面の停止要求観点で見るペーシングゲートは役割が異なり、除外理由を説明する対象は停止要求観点です。B: 復旧面の停止要求証跡が正答です。運用面の停止要求証跡応答で確認できる対象は停止要求証跡です。C: 保守面の停止要求読取で見る自動化一時停止は役割が異なり、除外理由を説明する対象は停止要求読取です。D: 照合面の停止要求状態で見るメッセージ条件は役割が異なり、除外理由を説明する対象は停止要求状態です。定義面の初出語説明として、停止要求とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は停止要求保守です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.177

    ---

    **問題.** 障害面の自動化一時停止を障害切り分けで確認します。応答面の対象項目では入力と操作画面応答を照合し、REQ=一時停止を記録します。資源が目標状態へ進まない理由を、要求、投票、状態から確認します。優先して確認する項目はどれですか。

    - A. INGMOVE
    - B. Timer Resume
    - C. INGSUSPD SUSPEND ✅
    - D. Observed Status

    正解: **C** ／ 難易度: 上級

    **解説:** 監査面の判定ではCを選び、対象は自動化一時停止証跡です。引継ぎ面の識別語は 自動化一時停止 一時停止 で、自動化一時停止証跡の対象名です。要求面の自動化一時停止読取は、資源に対する自動化を一時停止することを目的に扱う説明単位が自動化一時停止状態です。定義面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化一時停止定義です。構成面の自動化一時停止根拠を読む応答では、REQ=一時停止を出典の属性説明と照合する点が自動化一時停止応答です。A: 復旧面の自動化一時停止証跡で見る移動要求は役割が異なり、除外理由を説明する対象は自動化一時停止証跡です。B: 保守面の自動化一時停止読取で見るタイマー再開は役割が異なり、除外理由を説明する対象は自動化一時停止読取です。C: 照合面の自動化一時停止状態が正答です。構成面の自動化一時停止状態応答で確認できる対象は自動化一時停止状態です。D: 運用面の自動化一時停止定義で見る観測状態は役割が異なり、除外理由を説明する対象は自動化一時停止定義です。状態面の初出語説明として、自動化一時停止とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化一時停止監査です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.260

    ---

    **問題.** 監査面の自動化再開を監査記録で確認します。定義面の対象項目では入力と操作画面応答を照合し、resume automationを記録します。操作後に、入力、表示、メッセージを同じ記録で説明します。証跡として残すべき項目はどれですか。

    - A. INGRCHCK
    - B. DB2 CONTROL Policy Item
    - C. INGAMS
    - D. INGSUSPD RESUME ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 引継ぎ面の判定ではDを選び、対象は自動化再開読取です。応答面の識別語は 自動化一時停止 再開 で、自動化再開読取の対象名です。構成面の自動化再開状態は、一時停止した自動化を再開することを目的に扱う説明単位が自動化再開定義です。状態面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は自動化再開根拠です。記録面の自動化再開応答を読む応答では、resume automationを出典の属性説明と照合する点が自動化再開保守です。A: 保守面の自動化再開読取で見る資源状態待機は役割が異なり、除外理由を説明する対象は自動化再開読取です。B: 照合面の自動化再開状態で見るDb2制御項目は役割が異なり、除外理由を説明する対象は自動化再開状態です。C: 運用面の自動化再開定義で見るマネージャー一覧は役割が異なり、除外理由を説明する対象は自動化再開定義です。D: 要求面の自動化再開根拠が正答です。表示面の自動化再開根拠応答で確認できる対象は自動化再開根拠です。証跡面の初出語説明として、自動化再開とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は自動化再開引継ぎです。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Operators Commands p.261

    ---

    **問題.** 復旧面の構成詳細を引継ぎ確認で確認します。運用面の対象項目では入力と操作画面応答を照合し、config dataset/memberを記録します。担当者が交代しても同じ手順で読めるよう、用語と表示欄を対応させます。この条件で適切な確認対象はどれですか。

    - A. Desired Status
    - B. INGAMS Details ✅
    - C. ACF Load
    - D. Automation Flags

    正解: **B** ／ 難易度: 中級

    **解説:** 保守面の判定ではBを選び、対象は構成詳細監査です。照合面の識別語は 自動化マネージャー表示 詳細 で、構成詳細監査の対象名です。監査面の構成詳細引継ぎは、現在の構成データセットとメンバーを確認することを目的に扱う説明単位が構成詳細棚卸です。要求面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成詳細復旧です。引継ぎ面の構成詳細照合を読む応答では、config dataset/memberを出典の属性説明と照合する点が構成詳細観点です。A: 表示面の構成詳細監査で見る目標状態は役割が異なり、除外理由を説明する対象は構成詳細監査です。B: 設計面の構成詳細引継ぎが正答です。監査面の構成詳細引継ぎ応答で確認できる対象は構成詳細引継ぎです。C: 変更面の構成詳細棚卸で見る制御ファイル読込は役割が異なり、除外理由を説明する対象は構成詳細棚卸です。D: 障害面の構成詳細復旧で見る自動化フラグは役割が異なり、除外理由を説明する対象は構成詳細復旧です。構成面の初出語説明として、構成詳細とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成詳細読取です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 保守面の診断機能をポリシー見直しで確認します。要求面の対象項目では入力と操作画面応答を照合し、diagnostic optionを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. Agent READY Status
    - B. TRIGGER Policy Item
    - C. INGAMS Diagnostic ✅
    - D. INGREQ STOP

    正解: **C** ／ 難易度: 上級

    **解説:** 照合面の判定ではCを選び、対象は診断機能引継ぎです。運用面の識別語は 自動化マネージャー表示 診断 で、診断機能引継ぎの対象名です。引継ぎ面の診断機能棚卸は、状態イメージや作業統計などを診断することを目的に扱う説明単位が診断機能復旧です。構成面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は診断機能照合です。応答面の診断機能観点を読む応答では、diagnostic optionを出典の属性説明と照合する点が診断機能証跡です。A: 設計面の診断機能引継ぎで見るエージェント準備状態は役割が異なり、除外理由を説明する対象は診断機能引継ぎです。B: 変更面の診断機能棚卸で見るトリガー定義は役割が異なり、除外理由を説明する対象は診断機能棚卸です。C: 障害面の診断機能復旧が正答です。応答面の診断機能復旧応答で確認できる対象は診断機能復旧です。D: 監査面の診断機能照合で見る停止要求は役割が異なり、除外理由を説明する対象は診断機能照合です。記録面の初出語説明として、診断機能とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は診断機能状態です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.242

    ---

    **問題.** 照合面の制御ファイル読込を運用変更で確認します。構成面の対象項目では入力と操作画面応答を照合し、制御ファイル load processを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. Configuration Member
    - B. MINOR RESOURCES Policy Item
    - C. INGMOVE
    - D. ACF Load ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 運用面の判定ではDを選び、対象は制御ファイル読込棚卸です。要求面の識別語は 制御ファイル 読込 で、制御ファイル読込棚卸の対象名です。応答面の制御ファイル読込復旧は、自動化 Control Fileの読込状態を確認することを目的に扱う説明単位が制御ファイル読込照合です。記録面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は制御ファイル読込観点です。定義面の制御ファイル読込証跡を読む応答では、制御ファイル load processを出典の属性説明と照合する点が制御ファイル読込読取です。A: 変更面の制御ファイル読込棚卸で見る構成メンバーは役割が異なり、除外理由を説明する対象は制御ファイル読込棚卸です。B: 障害面の制御ファイル読込復旧で見る副資源定義は役割が異なり、除外理由を説明する対象は制御ファイル読込復旧です。C: 監査面の制御ファイル読込照合で見る移動要求は役割が異なり、除外理由を説明する対象は制御ファイル読込照合です。D: 引継ぎ面の制御ファイル読込観点が正答です。状態面の制御ファイル読込観点応答で確認できる対象は制御ファイル読込観点です。表示面の初出語説明として、制御ファイル読込とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は制御ファイル読込定義です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Messages and Codes p.251

    ---

    **問題.** 記録面の構成データセットをポリシー見直しで確認します。変更面の対象項目では入力と操作画面応答を照合し、Config dataset nameを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. DB2 CONTROL Policy Item
    - B. Compound Status
    - C. APPLICATION Entry Type
    - D. Configuration Dataset ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 表示面の判定ではDを選び、対象は構成データセット証跡です。設計面の識別語は 構成 データセット で、構成データセット証跡の対象名です。復旧面の構成データセット読取は、構成ファイルを格納するデータセット名を記録することを目的に扱う説明単位が構成データセット状態です。障害面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成データセット定義です。保守面の構成データセット根拠を読む応答では、Config dataset nameを出典の属性説明と照合する点が構成データセット応答です。A: 応答面の構成データセット証跡で見るDb2制御項目は役割が異なり、除外理由を説明する対象は構成データセット証跡です。B: 定義面の構成データセット読取で見る複合状態は役割が異なり、除外理由を説明する対象は構成データセット読取です。C: 状態面の構成データセット状態で見るアプリケーション定義は役割が異なり、除外理由を説明する対象は構成データセット状態です。D: 証跡面の構成データセット定義が正答です。照合面の構成データセット定義応答で確認できる対象は構成データセット定義です。監査面の初出語説明として、構成データセットとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成データセット監査です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 表示面の構成メンバーを運用変更で確認します。障害面の対象項目では入力と操作画面応答を照合し、Config memberを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. Configuration Member ✅
    - B. Observed Status
    - C. INGAMS Details
    - D. USS CONTROL Policy Item

    正解: **A** ／ 難易度: 中級

    **解説:** 設計面の判定ではAを選び、対象は構成メンバー読取です。変更面の識別語は 構成 メンバー で、構成メンバー読取の対象名です。保守面の構成メンバー状態は、読み込まれている構成メンバー名を記録することを目的に扱う説明単位が構成メンバー定義です。監査面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は構成メンバー根拠です。照合面の構成メンバー応答を読む応答では、Config memberを出典の属性説明と照合する点が構成メンバー保守です。A: 定義面の構成メンバー読取が正答です。復旧面の構成メンバー読取応答で確認できる対象は構成メンバー読取です。B: 状態面の構成メンバー状態で見る観測状態は役割が異なり、除外理由を説明する対象は構成メンバー状態です。C: 証跡面の構成メンバー定義で見る構成詳細は役割が異なり、除外理由を説明する対象は構成メンバー定義です。D: 復旧面の構成メンバー根拠で見るユーエスエス制御項目は役割が異なり、除外理由を説明する対象は構成メンバー根拠です。引継ぎ面の初出語説明として、構成メンバーとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は構成メンバー引継ぎです。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.125

    ---

    **問題.** 監査面のタイマー再開をポリシー見直しで確認します。定義面の対象項目では入力と操作画面応答を照合し、resume suspended timerを記録します。変更前にポリシー項目と実行時表示を対応させます。どのTSA項目を確認対象にしますか。

    - A. Timer Resume ✅
    - B. DISPINFO
    - C. INGSET
    - D. SERVICE PERIOD Policy Item

    正解: **A** ／ 難易度: 中級

    **解説:** 引継ぎ面の判定ではAを選び、対象はタイマー再開応答です。応答面の識別語は タイマー Resume で、タイマー再開応答の対象名です。構成面のタイマー再開保守は、停止中のタイマーを再開または再活性化することを目的に扱う説明単位がタイマー再開監査です。状態面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位はタイマー再開引継ぎです。記録面のタイマー再開棚卸を読む応答では、resume suspended timerを出典の属性説明と照合する点がタイマー再開復旧です。A: 保守面のタイマー再開応答が正答です。要求面のタイマー再開応答応答で確認できる対象はタイマー再開応答です。B: 照合面のタイマー再開保守で見るエージェント視点表示は役割が異なり、除外理由を説明する対象はタイマー再開保守です。C: 運用面のタイマー再開監査で見る状態属性設定は役割が異なり、除外理由を説明する対象はタイマー再開監査です。D: 要求面のタイマー再開引継ぎで見るサービス期間は役割が異なり、除外理由を説明する対象はタイマー再開引継ぎです。証跡面の初出語説明として、タイマー再開とはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義はタイマー再開観点です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.161

    ---

    **問題.** 引継ぎ面の一時停止上書きを運用変更で確認します。状態面の対象項目では入力と操作画面応答を照合し、OVERRIDE=SUSを記録します。自動化要求を入れる前に、影響する状態と証跡を整理します。どの選択肢が最も適切ですか。

    - A. INGGROUP
    - B. Suspend Override ✅
    - C. APPLICATION Entry Type
    - D. Automation Status

    正解: **B** ／ 難易度: 上級

    **解説:** 応答面の判定ではBを選び、対象は一時停止上書き保守です。定義面の識別語は Suspend 上書き で、一時停止上書き保守の対象名です。記録面の一時停止上書き監査は、停止要求を上書きして始動する条件を確認することを目的に扱う説明単位が一時停止上書き引継ぎです。証跡面の背景説明として、要求、状態、投票、構成情報を同じ作業証跡で結ぶ単位は一時停止上書き棚卸です。表示面の一時停止上書き復旧を読む応答では、OVERRIDE=SUSを出典の属性説明と照合する点が一時停止上書き照合です。A: 照合面の一時停止上書き保守で見るグループ要求は役割が異なり、除外理由を説明する対象は一時停止上書き保守です。B: 運用面の一時停止上書き監査が正答です。記録面の一時停止上書き監査応答で確認できる対象は一時停止上書き監査です。C: 要求面の一時停止上書き引継ぎで見るアプリケーション定義は役割が異なり、除外理由を説明する対象は一時停止上書き引継ぎです。D: 構成面の一時停止上書き棚卸で見る自動化状態は役割が異なり、除外理由を説明する対象は一時停止上書き棚卸です。復旧面の初出語説明として、一時停止上書きとはIBM Z System Automationで扱うポリシー、資源状態、または自動化要求のことで、用語定義は一時停止上書き証跡です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Defining_Automation_Policy / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Messages_and_Codes / Users Guide p.220

    ---

    **問題.** 警告照合のカスタマイズ プログラミングに関係する Automating 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告照合の根拠にする。 ✅
    - B. Automating 機能の名称と担当者名のみを残して警告照合のカスタマイズ プログラミングの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告照合のカスタマイズ プログラミングを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告照合のカスタマイズ プログラミングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では Automating 機能 は「Automating 機能の用途を自動化管理の表示で確認する警告照合項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では SA z/OS の Automating 機能と INGKYST0I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では Automating 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 警告読解のユーザーズガイドに関係する How 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. INGLIST の結果から対象行を抜き出し、警告読解の証跡として残す。 ✅
    - B. How 機能の名称と担当者名のみを残して警告読解のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で警告読解のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず警告読解のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では How 機能 は「How 機能の用途を自動化管理の表示で確認する警告読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では SA z/OS の How 機能と INGKYST0I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では How 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 構文確認のユーザーズガイドに関係する Recovery 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文確認として引き継ぐ。 ✅
    - B. Recovery 機能の名称と担当者名のみを残して構文確認のユーザーズガイドの表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で構文確認のユーザーズガイドを確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず構文確認のユーザーズガイドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Recovery 機能 は「Recovery 機能の用途を自動化管理の表示で確認する構文確認項目」と INGLIST または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では SA z/OS の Recovery 機能と INGKYST0I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Recovery 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 監査判定の概要 開始で自動化管理の運用確認を行います。Modifying 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で監査判定の概要 開始を確認した扱いにする。
    - B. INGKYST0I の有無を確認せず監査判定の概要 開始を正常終了として記録する。
    - C. SA z/OS の表示形式に沿って根拠行を採り、監査判定の点検結果を残す。 ✅
    - D. Modifying 機能の属性行を読まず監査判定の概要 開始の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では Modifying 機能 は「SA z/OS で Modifying 機能の扱いを記録する監査判定項目」と INGLIST または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では Modifying 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では Modifying 機能の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 条件記録の: Step 19: Enabling SA z/OS to Restart Automatic Restart Manager Enabled Subsystemに関係する Step 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と INGKYST0I を読み、条件記録の結果として保存する。 ✅
    - B. Step 機能の名称と担当者名のみを残して条件記録の: ・の表示本文を確認対象に含めない。
    - C. 自動化管理以外の画面で条件記録の: ・を確認し同じ証跡として扱ったことにする。
    - D. INGKYST0I の有無を見ず条件記録の: ・の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では Step 機能 は「Step 機能の用途を自動化管理の表示で確認する条件記録項目」と INGLIST または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では SA z/OS の Step 機能と INGKYST0I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では Step 機能を Z System Automation (TSA)で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 展開分離の:で Step 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Step 機能の出力を取らず展開分離の:の説明文と承認印のみを残す。
    - B. INGLIST で得た表示本文を使い、展開分離の採否を説明欄に結び付ける。 ✅
    - C. INGLIST を省略して展開分離の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では Step 機能 は「展開分離の:に関係する定義値と表示行を照合する展開分離項目」と INGLIST または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では Step 機能の属性行と INGKYST0I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では Step 機能を Z System Automation (TSA)の運用手順で確認し、初出名は展開分離初出です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **問題.** 範囲読解の計画 インストールで自動化管理の運用確認を行います。Using 機能の根拠にできる作業はどれですか。

    - A. SA z/OS と無関係な一覧で範囲読解の計画 インストールを確認した扱いにする。
    - B. INGKYST0I の有無を確認せず範囲読解の計画 インストールを正常終了として記録する。
    - C. 机上確認でも実出力の見出しに合わせ、範囲読解の確認値として扱う。 ✅
    - D. Using 機能の属性行を読まず範囲読解の計画 インストールの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Using 機能 は「SA z/OS で Using 機能の扱いを記録する範囲読解項目」と INGLIST または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Using 機能の表示結果と INGKYST0I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では Using 機能の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming


??? note "検証手順（33件）"
    **INGREQ 確認手順**

    - 検証目的: INGREQ で発行した停止要求が要求一覧に登録され、要求値と発行元を追跡できることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。外部連携元を識別できる停止要求を登録するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGREQ SUBSYS1/APL/AOC4 REQ=STOP,OUTMODE=LINE,SOURCE=EXTERNAL,VERIFY=NO
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。登録された要求の状態と発行元を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE SUBSYS1/APL/AOC4 STATUS=ALL,SOURCE=EXTERNAL
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : SUBSYS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : STOP
    Source : EXTERNAL
    ```

    SUBSYS1/APL/AOC4 の Request : STOP と Source : EXTERNAL により、INGREQ の登録内容を確認できます。

    - 合格条件: ① ステップ2の SUBSYS1/APL/AOC4 と STOP が表示されること
    ② ステップ2の EXTERNAL と Winning が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGREQ REQ=START 確認手順**

    - 検証目的: REQ=START で登録した開始要求が対象資源の勝ち要求として評価されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。CICS1 の開始要求を登録するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGREQ CICS1/APL/AOC4 REQ=START,VERIFY=NO
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。現在有効な勝ち要求を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE CICS1/APL/AOC4 STATUS=WINNING
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : CICS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : START
    Source : OPERATOR
    ```

    Request : START と Status : Winning は開始要求が現在の勝ち要求であることを示します。

    - 合格条件: ① ステップ2の CICS1/APL/AOC4 と START が表示されること
    ② ステップ2の Winning が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **OVERRIDE 確認手順**

    - 検証目的: OVERRIDE=YES を指定した開始要求が中断状態を上書きする要求として記録されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。中断状態を上書きする開始要求を登録するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGREQ CICS1/APL/AOC4 REQ=START,OVERRIDE=YES,VERIFY=NO
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。勝ち要求の詳細を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE CICS1/APL/AOC4 STATUS=WINNING
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : CICS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : START
    Source : OPERATOR
    Override : YES
    ```

    Override : YES は勝ち要求に上書き指定が保持されていることを示します。

    - 合格条件: ① ステップ2の Override : YES が表示されること
    ② ステップ2の Winning が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INTERRUPT 確認手順**

    - 検証目的: INTERRUPT=YES の停止要求が、既存の開始投票へ割り込む要求として登録されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。既存要求へ割り込む停止要求を登録するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGREQ CICS1/APL/AOC4 REQ=STOP,INTERRUPT=YES,VERIFY=NO
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。停止要求の割込み属性を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE CICS1/APL/AOC4 STATUS=WINNING
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : CICS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : STOP
    Source : OPERATOR
    Interrupt : YES
    ```

    Request : STOP と Interrupt : YES により、割込み指定付き停止要求を確認できます。

    - 合格条件: ① ステップ2の Request : STOP が表示されること
    ② ステップ2の Interrupt : YES が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **PRECHECK 確認手順**

    - 検証目的: PRECHECK=YES を指定した要求が、確認処理の前に事前検査を行う指定で登録されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。事前検査を有効にした開始要求を登録するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGREQ CICS1/APL/AOC4 REQ=START,PRECHECK=YES,VERIFY=NO
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。登録要求の事前検査属性を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE CICS1/APL/AOC4 STATUS=WINNING
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : CICS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : START
    Source : OPERATOR
    Precheck : YES
    ```

    Precheck : YES と Request : START は、事前検査付き開始要求の登録内容を示します。

    - 合格条件: ① ステップ2の Precheck : YES が表示されること
    ② ステップ2の Request : START が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGLIST 確認手順**

    - 検証目的: INGLIST で管理資源の種別、システム、複合状態、観測状態、目標状態を一覧確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源の管理状態を一覧表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGLIST CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYST0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGLIST ----------
    Cmd  Resource             Type System  Compound      Observed   Desired
         CICS1/APL/AOC4       APL  AOC4    SATISFACTORY  AVAILABLE  AVAILABLE
         CICSGRP/APG/AOC4     APG  AOC4    SATISFACTORY  AVAILABLE  AVAILABLE
    ```

    CICS1/APL/AOC4 行の Compound、Observed、Desired 列に SATISFACTORY と AVAILABLE が表示されます。

    - 合格条件: ① ステップ1の CICS1/APL/AOC4 と AVAILABLE が表示されること
    ② ステップ1の SATISFACTORY が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGINFO 確認手順**

    - 検証目的: INGINFO で資源の観測状態、目標状態、自動化状態、開始可能性、複合状態、健全性を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。自動化マネージャーが保持する資源詳細を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGINFO CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYIN0 SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Observed         : AVAILABLE
    Desired          : AVAILABLE
    Automation       : IDLE
    Startability     : YES
    Compound         : SATISFACTORY
    Health Status    : N/A
    ```

    Observed : AVAILABLE、Automation : IDLE、Compound : SATISFACTORY から管理状態を確認できます。

    - 合格条件: ① ステップ1の Observed : AVAILABLE が表示されること
    ② ステップ1の Automation : IDLE と Compound : SATISFACTORY が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **DISPINFO 確認手順**

    - 検証目的: DISPINFO へ切り替え、自動化エージェントが保持する状態と最後のメッセージを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS の選択パネルです。INGINFO から DISPINFO のエージェント視点へ切り替えるため、定義されたファンクション・キーを押して表示を切り替えます。
    操作（入力）:
    ```text
    → PF4 を押す
    ```

    画面・出力:
    ```text
    DISPINFO SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Automation Status: IDLE
    Automation Flags : -
    Observed Status  : AVAILABLE
    Last Message     : DFHSI1517
    ```

    DISPINFO の Automation Status: IDLE と Last Message : DFHSI1517 はエージェント側の保持情報です。

    - 合格条件: ① ステップ1の DISPINFO と Automation Status: IDLE が表示されること
    ② ステップ1の DFHSI1517 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGVOTE 確認手順**

    - 検証目的: INGVOTE で資源に対する要求を一覧し、勝ち要求、要求ID、要求値、発行元を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源に登録されたすべての要求を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE CICS1/APL/AOC4 STATUS=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : CICS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : START
    Source : OPERATOR
    ```

    Request ID : 20260716-0007 と Status : Winning により、採用中の START 要求を識別できます。

    - 合格条件: ① ステップ1の Request ID : 20260716-0007 が表示されること
    ② ステップ1の Status : Winning と Request : START が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGGROUP 確認手順**

    - 検証目的: INGGROUP でアプリケーション・グループの性質と構成メンバー、可用性、優先値を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。グループの性質とメンバー構成を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGGROUP CICSGRP/APG/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYGR0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGGROUP ----------
    Group : CICSGRP/APG/AOC4   Nature : MOVE
    Cmd  Member               System  Avail  Pref  Result      Eff
         CICS1/APL/AOC4       AOC4    YES    2800  AVAILABLE   2800
         CICS2/APL/AOC5       AOC5    YES    2400  UNAVAILABLE 2400
    ```

    Nature : MOVE と CICS1/APL/AOC4 行の Avail、Pref、Result、Eff で構成と評価値を確認できます。

    - 合格条件: ① ステップ1の Nature : MOVE が表示されること
    ② ステップ1の CICS1/APL/AOC4 と Pref 2800 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGMOVE 確認手順**

    - 検証目的: INGMOVE の確認画面で、移動対象グループ、現在システム、移動先システム、操作種別を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。グループ移動の実行前確認画面を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGMOVE CICSGRP/APG/AOC4 TO=AOC5,ACTION=MOVE,VERIFY=YES
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYMV0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGMOVE ----------
    Group          : CICSGRP/APG/AOC4
    Current system : AOC4
    New system     : AOC5
    Action         : MOVE
    Press ENTER to confirm or END to cancel
    ```

    INGMOVE 確認画面の Current system : AOC4、New system : AOC5、Action : MOVE で移動内容を照合できます。

    - 合格条件: ① ステップ1の Group : CICSGRP/APG/AOC4 が表示されること
    ② ステップ1の Current system : AOC4 と New system : AOC5 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **preference value 確認手順**

    - 検証目的: グループ・メンバーの優先値が許容範囲内で、実効優先値として評価されていることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。メンバーの設定優先値と実効優先値を比較するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGGROUP CICSGRP/APG/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYGR0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGGROUP ----------
    Group : CICSGRP/APG/AOC4   Nature : MOVE
    Cmd  Member               System  Avail  Pref  Result      Eff
         CICS1/APL/AOC4       AOC4    YES    2800  AVAILABLE   2800
         CICS2/APL/AOC5       AOC5    YES    2400  UNAVAILABLE 2400
    ```

    CICS1/APL/AOC4 行の Pref 2800 と Eff 2800 が一致し、設定値が評価に使われています。

    - 合格条件: ① ステップ1の CICS1/APL/AOC4 と Pref 2800 が表示されること
    ② ステップ1の Eff 2800 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGAMS 確認手順**

    - 検証目的: INGAMS で自動化マネージャーとエージェントの役割、準備状態、フラグを一覧確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。自動化管理構成の役割と状態を一覧表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGAMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYAM0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGAMS ----------
    Name     System   Role   Status  FL
    AOC4     AOC4     PAM    READY   
    AOC5     AOC5     SAM    READY   
    AOC6     AOC6     AGENT  READY
    ```

    AOC4 行の Role PAM と AOC6 行の Role AGENT、各 Status READY により構成を確認できます。

    - 合格条件: ① ステップ1の AOC4 と PAM と READY が表示されること
    ② ステップ1の AOC6 と AGENT と READY が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGAMS REFRESH 確認手順**

    - 検証目的: INGAMS REFRESH 後にマネージャー詳細を再表示し、使用中の構成データ・セットを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。準備済みの各エージェントへ管理構成を再読み込みするため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGAMS REFRESH CFG=SYS1.SINGPARM
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。主マネージャーが参照する構成データ・セットを確認するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGAMS DETAILS AOC4 OUTMODE=LINE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Manager : AOC4
    Role : PAM
    Status : READY
    Configuration data set : SYS1.SINGPARM
    Automation control file : SYS1.SINGACF
    ```

    Manager : AOC4 の Status : READY と Configuration data set : SYS1.SINGPARM で再読込み対象を確認できます。

    - 合格条件: ① ステップ2の Manager : AOC4 が表示されること
    ② ステップ2の Configuration data set : SYS1.SINGPARM が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGAUTO 確認手順**

    - 検証目的: INGAUTO で対象資源の自動化を停止し、コマンド処理の正常完了メッセージを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源だけの自動化フラグを停止するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGAUTO OFF CICS1/APL/AOC4 SCOPE=ONLY,FLAG=AUTOMATION
    → Enter を押す
    ```

    画面・出力:
    ```text
    AOF099I FUNCTION COMPLETED
    ```

    AOF099I FUNCTION COMPLETED は INGAUTO のフラグ変更処理が完了したことを示します。

    - 合格条件: ① ステップ1の AOF099I と FUNCTION COMPLETED が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **automation flag 確認手順**

    - 検証目的: 自動化制御ファイルの AUTO 値を表示し、資源タイプの自動化フラグ既定値を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。CICST タイプの START エントリーに設定された自動化フラグを表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> ACF REQ=DISP,ENTRY=START,TYPE=CICST
    → Enter を押す
    ```

    画面・出力:
    ```text
    AOF111I AUTOMATION CONFIGURATION DISPLAY - ENTRY= START
    AOF112I ACTIVE TYPE= CICST      , DESIRED TYPE= CICST
    AOF113I DATA IS AUTO=Y
    AOF113I DATA IS NOAUTO=(TUESDAY,10:00,12:00)
    AOF002I END OF MULTILINE MESSAGE GROUP
    ```

    AOF112I の ACTIVE TYPE= CICST と AOF113I の DATA IS AUTO=Y が有効な自動化フラグを示します。

    - 合格条件: ① ステップ1の ACTIVE TYPE= CICST が表示されること
    ② ステップ1の DATA IS AUTO=Y が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGSTOBS 確認手順**

    - 検証目的: INGSTOBS で状況監視出口を登録し、LIST 出力に資源と出口の対応が表示されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。CICS1 の状況変更を MSG2OPER 出口へ通知する登録を行うため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGSTOBS REGISTER,TEST2,MSG2OPER,CICS1/APL/AOC4
    → Enter を押す
    ```


    **ステップ 2**
    現在の画面は SA z/OS のコマンド入力画面です。TEST2 に関連付けられた資源と出口を一覧表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGSTOBS LIST,TEST2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Resource                 Exits
    CICS1/APL/AOC4          TEST2/MSG2OPER
    *** End of Display ***
    ```

    CICS1/APL/AOC4 行の TEST2/MSG2OPER と *** End of Display *** により登録一覧を確認できます。

    - 合格条件: ① ステップ2の CICS1/APL/AOC4 が表示されること
    ② ステップ2の TEST2/MSG2OPER と End of Display が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **Observed status 確認手順**

    - 検証目的: Observed status が自動化エージェントから報告された実際の資源状態を表すことを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源の現在の観測状態を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGINFO CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYIN0 SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Observed         : AVAILABLE
    Desired          : AVAILABLE
    Automation       : IDLE
    Startability     : YES
    Compound         : SATISFACTORY
    Health Status    : N/A
    ```

    Observed : AVAILABLE は自動化エージェントが資源を使用可能と観測していることを示します。

    - 合格条件: ① ステップ1の Observed : AVAILABLE が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **Desired status 確認手順**

    - 検証目的: Desired status が要求評価後に自動化マネージャーが目標とする資源状態を表すことを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源に対して決定された目標状態を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGINFO CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYIN0 SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Observed         : AVAILABLE
    Desired          : AVAILABLE
    Automation       : IDLE
    Startability     : YES
    Compound         : SATISFACTORY
    Health Status    : N/A
    ```

    Desired : AVAILABLE は自動化マネージャーの現在の目標が使用可能状態であることを示します。

    - 合格条件: ① ステップ1の Desired : AVAILABLE が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **Automation status 確認手順**

    - 検証目的: Automation status が資源に対する自動化処理の進行状態を示すことを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源の自動化処理状態を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGINFO CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYIN0 SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Observed         : AVAILABLE
    Desired          : AVAILABLE
    Automation       : IDLE
    Startability     : YES
    Compound         : SATISFACTORY
    Health Status    : N/A
    ```

    Automation : IDLE は対象資源に対する自動化処理が現在進行していないことを示します。

    - 合格条件: ① ステップ1の Automation : IDLE が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **Compound status 確認手順**

    - 検証目的: Compound status が観測状態と目標状態などを集約した総合状態として表示されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源の総合的な複合状態を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGINFO CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYIN0 SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Observed         : AVAILABLE
    Desired          : AVAILABLE
    Automation       : IDLE
    Startability     : YES
    Compound         : SATISFACTORY
    Health Status    : N/A
    ```

    Compound : SATISFACTORY は観測状態が目標状態を満たす総合評価であることを示します。

    - 合格条件: ① ステップ1の Compound : SATISFACTORY が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **Health status 確認手順**

    - 検証目的: Health status が資源から提供される健全性情報として独立表示されることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源から提供される健全性情報を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGINFO CICS1/APL/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYIN0 SA z/OS - Command Dialogs
    Resource         : CICS1/APL/AOC4
    Observed         : AVAILABLE
    Desired          : AVAILABLE
    Automation       : IDLE
    Startability     : YES
    Compound         : SATISFACTORY
    Health Status    : N/A
    ```

    Health Status : N/A はこの例では資源固有の健全性値が提供されていないことを示します。

    - 合格条件: ① ステップ1の Health Status : N/A が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **SDF 確認手順**

    - 検証目的: SDF の色と状態語を使用して、正常資源と問題資源を同じ状況表示から識別します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SDF のコマンド入力画面です。Status Display Facility の最新状況を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SDF ===> SDF
    → Enter を押す
    ```

    画面・出力:
    ```text
    AOC4 SA z/OS Status Display
    System   Color  Status
    AOC4     GREEN  UP
    Resource Color  Status
    CICS2    RED    BROKEN
    ===>
    ```

    AOC4 の GREEN UP は正常、CICS2 の RED BROKEN は問題状態として SDF に強調表示されています。

    - 合格条件: ① ステップ1の AOC4 と GREEN と UP が表示されること
    ② ステップ1の CICS2 と RED と BROKEN が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **Detail Status Display 確認手順**

    - 検証目的: SDF から Detail Status Display を開き、問題資源の状態記述子と直近メッセージを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS の選択パネルです。SDF で選択した CICS2 の詳細状況を開くため、定義されたファンクション・キーを押して表示を切り替えます。
    操作（入力）:
    ```text
    → PF2 を押す
    ```

    画面・出力:
    ```text
    SA z/OS Detail Status Display
    Resource          CICS2
    System            AOC4
    Status Descriptor BROKEN
    Message ID        DFHSI1517
    Color             RED
    ```

    Detail Status Display の Status Descriptor BROKEN と Message ID DFHSI1517 により問題の根拠を確認できます。

    - 合格条件: ① ステップ1の Detail Status Display と CICS2 が表示されること
    ② ステップ1の BROKEN と DFHSI1517 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **automation manager 確認手順**

    - 検証目的: INGAMS の役割列から、自動化マネージャーが主マネージャーとして意思決定を担当することを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。意思決定を担当する主自動化マネージャーを識別するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGAMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYAM0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGAMS ----------
    Name     System   Role   Status  FL
    AOC4     AOC4     PAM    READY   
    AOC5     AOC5     SAM    READY   
    AOC6     AOC6     AGENT  READY
    ```

    AOC4 行の Role PAM と Status READY は、AOC4 が稼働中の主自動化マネージャーであることを示します。

    - 合格条件: ① ステップ1の AOC4 と PAM と READY が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **automation agent 確認手順**

    - 検証目的: INGAMS の役割列から、自動化エージェントが各システムの監視・操作を担当することを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。監視と操作を担当する自動化エージェントを識別するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGAMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYAM0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGAMS ----------
    Name     System   Role   Status  FL
    AOC4     AOC4     PAM    READY   
    AOC5     AOC5     SAM    READY   
    AOC6     AOC6     AGENT  READY
    ```

    AOC6 行の Role AGENT と Status READY は、自動化エージェントが管理通信可能な状態であることを示します。

    - 合格条件: ① ステップ1の AOC6 と AGENT と READY が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **sysplex application group 確認手順**

    - 検証目的: シスプレックス・アプリケーション・グループが複数システムのメンバーをまとめて管理することを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。複数システムにまたがるグループ・メンバーを表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGGROUP CICSGRP/APG/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYGR0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGGROUP ----------
    Group : CICSGRP/APG/AOC4   Nature : MOVE
    Cmd  Member               System  Avail  Pref  Result      Eff
         CICS1/APL/AOC4       AOC4    YES    2800  AVAILABLE   2800
         CICS2/APL/AOC5       AOC5    YES    2400  UNAVAILABLE 2400
    ```

    CICSGRP/APG/AOC4 に AOC4 の CICS1 と AOC5 の CICS2 が含まれ、シスプレックス横断の構成を確認できます。

    - 合格条件: ① ステップ1の CICSGRP/APG/AOC4 が表示されること
    ② ステップ1の AOC4 と AOC5 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **MOVE group 確認手順**

    - 検証目的: MOVE グループで実行可能なメンバーが複数あっても、使用可能となるメンバーが一つであることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。MOVE グループで現在選択されている一つのメンバーを確認するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGGROUP CICSGRP/APG/AOC4
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYGR0 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGGROUP ----------
    Group : CICSGRP/APG/AOC4   Nature : MOVE
    Cmd  Member               System  Avail  Pref  Result      Eff
         CICS1/APL/AOC4       AOC4    YES    2800  AVAILABLE   2800
         CICS2/APL/AOC5       AOC5    YES    2400  UNAVAILABLE 2400
    ```

    Nature : MOVE の一覧で CICS1/APL/AOC4 は AVAILABLE、CICS2/APL/AOC5 は UNAVAILABLE です。

    - 合格条件: ① ステップ1の Nature : MOVE が表示されること
    ② ステップ1の CICS1/APL/AOC4 と AVAILABLE が表示されること
    ③ ステップ1の CICS2/APL/AOC5 と UNAVAILABLE が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **static resource 確認手順**

    - 検証目的: INGLIST の DYNRES=NO フィルターで、ポリシー定義に基づく静的資源だけを表示します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。動的資源を除外して静的資源だけを表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGLIST * DYNRES=NO OUTMODE=LINE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Resource : CICS1/APL/AOC4
    Type : APL
    System : AOC4
    Dynamic : NO
    Compound : SATISFACTORY
    ```

    CICS1/APL/AOC4 の Dynamic : NO はポリシー定義に基づく静的資源であることを示します。

    - 合格条件: ① ステップ1の CICS1/APL/AOC4 と Dynamic : NO が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **dynamic resource 確認手順**

    - 検証目的: INGLIST の DYNRES=YES フィルターで、実行時に追加された動的資源だけを表示します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。実行時に追加された動的資源だけを表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGLIST * DYNRES=YES OUTMODE=LINE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Resource : JOBTEMP/APL/AOC4
    Type : APL
    System : AOC4
    Dynamic : YES
    Compound : SATISFACTORY
    ```

    JOBTEMP/APL/AOC4 の Dynamic : YES は自動化マネージャーへ動的に追加された資源であることを示します。

    - 合格条件: ① ステップ1の JOBTEMP/APL/AOC4 と Dynamic : YES が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **request ID 確認手順**

    - 検証目的: INGVOTE の要求IDを記録し、取消し対象となる要求を一意に識別できることを確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。対象資源の要求IDと要求状態を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGVOTE CICS1/APL/AOC4 STATUS=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYRQ2 SA z/OS - Command Dialogs Line 1 of 25
    Domain ID = IPUFA ---------- INGVOTE ----------
    Cmd: C Cancel request  K Kill request  S Show details  V Show votes
    Resource : CICS1/APL/AOC4
    Request ID : 20260716-0007
    Status : Winning
    Request : START
    Source : OPERATOR
    ```

    Request ID : 20260716-0007 により Winning 状態の START 要求を一意に識別できます。

    - 合格条件: ① ステップ1の Request ID : 20260716-0007 が表示されること
    ② ステップ1の Status : Winning が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **INGSCHE 確認手順**

    - 検証目的: 正規コマンド INGSCHED でスケジュール定義と関連資源を表示し、運用時間帯を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。SHIFT1 の時間帯と関連資源を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> INGSCHED SHIFT1 REQ=DISP
    → Enter を押す
    ```

    画面・出力:
    ```text
    INGKYSP1 SA z/OS - Command Dialogs
    Domain ID = IPUFA ---------- INGSCHED ----------
    Schedule : SHIFT1
    Day      : MON-FRI
    Time     : 08:00-18:00
    Resource : CICS1/APL/AOC4
    ```

    INGSCHED 画面の Schedule : SHIFT1、Time : 08:00-18:00、Resource : CICS1/APL/AOC4 で定義内容を確認できます。

    - 合格条件: ① ステップ1の INGSCHED と Schedule : SHIFT1 が表示されること
    ② ステップ1の CICS1/APL/AOC4 と 08:00-18:00 が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

    ---

    **ACF 確認手順**

    - 検証目的: ACF で有効な自動化制御ファイルのエントリーとタイプ、AUTO 設定、時間帯例外を確認します。
    - 前提条件: 検証用の SA z/OS 4.3 ドメイン IPUFA に、対象コマンドを実行できる権限で接続します。変更操作は検証環境でのみ行います。
    - セッション環境: SA z/OS 4.3 が稼働する NetView コマンド・ダイアログ。SDF の項目では Status Display Facility を使用します。

    **ステップ 1**
    現在の画面は SA z/OS のコマンド入力画面です。START エントリーの有効タイプと自動化設定を表示するため、入力口に実在するコマンドを指定して実行します。
    操作（入力）:
    ```text
    SA z/OS ===> ACF REQ=DISP,ENTRY=START,TYPE=CICST
    → Enter を押す
    ```

    画面・出力:
    ```text
    AOF111I AUTOMATION CONFIGURATION DISPLAY - ENTRY= START
    AOF112I ACTIVE TYPE= CICST      , DESIRED TYPE= CICST
    AOF113I DATA IS AUTO=Y
    AOF113I DATA IS NOAUTO=(TUESDAY,10:00,12:00)
    AOF002I END OF MULTILINE MESSAGE GROUP
    ```

    AOF111I、AOF112I、AOF113I により ENTRY= START の CICST タイプと AUTO=Y、NOAUTO 時間帯を確認できます。

    - 合格条件: ① ステップ1の AOF111I と ENTRY= START が表示されること
    ② ステップ1の AUTO=Y と NOAUTO=(TUESDAY,10:00,12:00) が表示されること
    ③ ステップ1の AOF002I が表示されること
    - 検証状態: 机上
    - 出典: TSA_z_OS_4.3_Users_Guide / TSA_z_OS_4.3_Operators_Commands / TSA_z_OS_4.3_Programmers_Reference / TSA_z_OS_4.3_Customizing_and_Programming

