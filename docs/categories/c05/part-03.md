---
search:
  exclude: true
---

# Comm Server / VTAM / TCP/IP — 詳細 (3/4)

[← Comm Server / VTAM / TCP/IP の概要へ戻る](index.md)


## Comm Server / VTAM / TCP/IP > VTAM F NET コマンド

### F NET,TABLE {#c05-i0248}
*分類: VTAM F NET コマンド*  ・  難易度: 上級

F NET,TABLEは、Comm Server / VTAM / TCP/IPのVTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 順序照合のコマンドで通信サーバーの運用確認を行います。F NET,TABLE の根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で順序照合のコマンドを確認した扱いにする。
    - B. IST097I の有無を確認せず順序照合のコマンドを正常終了として記録する。
    - C. IST097I を含む表示を保存し、説明欄との差分を順序照合で確認する。 ✅
    - D. F NET,TABLE の属性行を読まず順序照合のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合のコマンドにおいて選択記号 C を採用し、識別名は順序照合です。順序照合のコマンドにおいて F NET,TABLE は説明欄の「z/OS Communications Serverで F NET,TABLE の扱いを記録する順序照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のコマンドを受け取る担当者は、F NET,TABLE の表示結果と IST097I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のコマンドは別カテゴリの確認を流用しており、F NET,TABLE の根拠にならないため順序照合ではありません。 B: 順序照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため順序照合ではありません。 C: 順序照合のコマンドは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のコマンドが示す F NET,TABLE は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **F NET,TABLE**

    - 検証目的: 復旧判定のコマンドについて、F NET,TABLE は、Comm Server / VTAM / TCP/IP の VTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010098の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、復旧判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,TABLEを指定し、OSKB010098の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F NET,TABLE
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F NET,TABLE
    CASE OSKB010098
    SOURCE z/OS Communications Server
    ```

    F NET,TABLEとOSKB010098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010098を同じ出力で読み、復旧判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010098 F NET,TABLE
    ```

    IST097IとOSKB010098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の F NET,TABLE と OSKB010098 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### F NET,TRACE {#c05-i0249}
*分類: VTAM F NET コマンド*  ・  難易度: 上級

F NET,TRACEは、Comm Server / VTAM / TCP/IPのVTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 警告照合のコマンドに関係する F NET,TRACE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告照合の確認記録にまとめる。 ✅
    - B. F NET,TRACE の名称と担当者名のみを残して警告照合のコマンドの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で警告照合のコマンドを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず警告照合のコマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合のコマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のコマンドにおいて F NET,TRACE は説明欄の「F NET,TRACE の用途を通信サーバーの表示で確認する警告照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のコマンドに関連して、z/OS Communications Serverでは F NET,TRACE の表示属性と IST097I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のコマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のコマンドは別カテゴリの確認を流用しており、F NET,TRACE の根拠にならないため警告照合ではありません。 D: 警告照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため警告照合ではありません。警告照合のコマンドで使う F NET,TRACE という用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は警告照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **F NET,TRACE**

    - 検証目的: 変更判定のコマンドについて、F NET,TRACE は、Comm Server / VTAM / TCP/IP の VTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010100の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、変更判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,TRACEを指定し、OSKB010100の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F NET,TRACE
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F NET,TRACE
    CASE OSKB010100
    SOURCE z/OS Communications Server
    ```

    F NET,TRACEとOSKB010100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010100を同じ出力で読み、変更判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010100 F NET,TRACE
    ```

    IST097IとOSKB010100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の F NET,TRACE と OSKB010100 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### F NET,USSTAB {#c05-i0250}
*分類: VTAM F NET コマンド*  ・  難易度: 上級

F NET,USSTABは、Comm Server / VTAM / TCP/IPのVTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 比較照合のコマンドで F NET,USSTAB の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. F NET,USSTAB の出力を取らず比較照合のコマンドの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較照合の根拠を固定する。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して比較照合のコマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のコマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合のコマンドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合のコマンドにおいて F NET,USSTAB は説明欄の「比較照合のコマンドに関係する定義値と表示行を照合する比較照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のコマンドの証跡を読む担当者は、F NET,USSTAB の属性行と IST097I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のコマンドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため比較照合ではありません。 D: 比較照合のコマンドは別カテゴリの確認を流用しており、F NET,USSTAB の根拠にならないため比較照合ではありません。比較照合のコマンドに出る F NET,USSTAB は Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **F NET,USSTAB**

    - 検証目的: 警告判定のコマンドについて、F NET,USSTAB は、Comm Server / VTAM / TCP/IP の VTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010097の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、警告判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,USSTABを指定し、OSKB010097の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F NET,USSTAB
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F NET,USSTAB
    CASE OSKB010097
    SOURCE z/OS Communications Server
    ```

    F NET,USSTABとOSKB010097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010097を同じ出力で読み、警告判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010097 F NET,USSTAB
    ```

    IST097IとOSKB010097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の F NET,USSTAB と OSKB010097 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### F NET,VTAMOPTS {#c05-i0251}
*分類: VTAM F NET コマンド*  ・  難易度: 上級

F NET,VTAMOPTSは、Comm Server / VTAM / TCP/IPのVTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 値域照合のコマンドに関する F NET,VTAMOPTS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず値域照合のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のコマンドの証跡として保存して根拠にする。
    - C. F NET,VTAMOPTS の変更点を出力本文から切り離して値域照合のコマンドの承認欄のみ残す。
    - D. D NET,ID=OSKBAPPL,E の結果から対象行を抜き出し、値域照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合のコマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合のコマンドにおいて F NET,VTAMOPTS は説明欄の「F NET,VTAMOPTS の状態と出力メッセージを結び付ける値域照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のコマンドに関する記録は、F NET,VTAMOPTS の出力行と IST097I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため値域照合ではありません。 B: 値域照合のコマンドは別カテゴリの確認を流用しており、F NET,VTAMOPTS の根拠にならないため値域照合ではありません。 C: 値域照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のコマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のコマンドで記録する F NET,VTAMOPTS はz/OS Communications Serverの確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **F NET,VTAMOPTS**

    - 検証目的: 監査判定のコマンドについて、F NET,VTAMOPTS は、Comm Server / VTAM / TCP/IP の VTAM F NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010099の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、監査判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,VTAMOPTSを指定し、OSKB010099の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F NET,VTAMOPTS
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F NET,VTAMOPTS
    CASE OSKB010099
    SOURCE z/OS Communications Server
    ```

    F NET,VTAMOPTSとOSKB010099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010099を同じ出力で読み、監査判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010099 F NET,VTAMOPTS
    ```

    IST097IとOSKB010099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の F NET,VTAMOPTS と OSKB010099 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM HPR

### ANR (Automatic Network Routing) {#c05-i0252}
*分類: VTAM HPR*  ・  難易度: 上級

ANR (Automatic Network Routing)は、Comm Server / VTAM / TCP/IPのVTAM HPRで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **ANR (Automatic Network Routing)**

    - 検証目的: 呼出確認の通信サーバーについて、ANR (Automatic Network Routing)は、Comm Server / VTAM / TCP/IP の VTAM HPR で自動化処理や復旧動作を確認する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020003の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、呼出確認の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にANR (Automatic Netを指定し、OSKB020003の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ANR (Automatic Net
    CASE OSKB020003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ANR (Automatic Net
    CASE OSKB020003
    SOURCE z/OS Communications Server
    ```

    ANR (Automatic NetとOSKB020003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB020003を同じ出力で読み、呼出確認の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB020003
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB020003 ANR (Automatic Network R
    ```

    IST097IとOSKB020003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の ANR (Automatic Net と OSKB020003 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB020003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### HPR の役割 {#c05-i0253}
*分類: VTAM HPR*  ・  難易度: 上級

HPR の役割は、Comm Server / VTAM / TCP/IPのVTAM HPRで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **HPR の役割**

    - 検証目的: 展開確認のの役割について、HPR の役割は、Comm Server / VTAM / TCP/IP の VTAM HPR で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020002の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、展開確認のの役割の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にHPR の役割を指定し、OSKB020002の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND HPR の役割
    CASE OSKB020002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM HPR の役割
    CASE OSKB020002
    SOURCE z/OS Communications Server
    ```

    HPR の役割とOSKB020002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB020002を同じ出力で読み、展開確認のの役割の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB020002
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB020002 HPR の役割
    ```

    IST097IとOSKB020002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の HPR の役割 と OSKB020002 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB020002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### Path Switch {#c05-i0254}
*分類: VTAM HPR*  ・  難易度: 上級

Path Switchは、Comm Server / VTAM / TCP/IPのVTAM HPRで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **Path Switch**

    - 検証目的: 終端確認の通信サーバーについて、Path Switchは、Comm Server / VTAM / TCP/IP の VTAM HPR で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、終端確認の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPath Switchを指定し、OSKB020005の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Path Switch
    CASE OSKB020005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Path Switch
    CASE OSKB020005
    SOURCE z/OS Communications Server
    ```

    Path SwitchとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB020005を同じ出力で読み、終端確認の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB020005
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB020005 Path Switch
    ```

    IST097IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の Path Switch と OSKB020005 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB020005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### RTP (Rapid Transport Protocol) {#c05-i0255}
*分類: VTAM HPR*  ・  難易度: 上級

RTP (Rapid Transport Protocol)は、Comm Server / VTAM / TCP/IPのVTAM HPRで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **RTP (Rapid Transport Protocol)**

    - 検証目的: 置換確認の通信サーバーについて、RTP (Rapid Transport Protocol)は、Comm Server / VTAM / TCP/IP の VTAM HPR で機能名、見出し、または確認対象としに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、置換確認の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にRTP (Rapid Transpoを指定し、OSKB020004の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND RTP (Rapid Transpo
    CASE OSKB020004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM RTP (Rapid Transpo
    CASE OSKB020004
    SOURCE z/OS Communications Server
    ```

    RTP (Rapid TranspoとOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB020004を同じ出力で読み、置換確認の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB020004
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB020004 RTP (Rapid Transport Pro
    ```

    IST097IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の RTP (Rapid Transpo と OSKB020004 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB020004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM LU 定義

### LU LOCADDR オペランド {#c05-i0256}
*分類: VTAM LU 定義*  ・  難易度: 上級

LU LOCADDR オペランドは、Comm Server / VTAM / TCP/IPのVTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 比較照合のオペランドで LU LOCADDR オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LU LOCADDR オペランドの出力を取らず比較照合のオペランドの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較照合の確認値として扱う。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して比較照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合のオペランドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合のオペランドにおいて LU LOCADDR オペランド は説明欄の「比較照合のオペランドに関係する定義値と表示行を照合する比較照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のオペランドの証跡を読む担当者は、LU LOCADDR オペランドの属性行と IST097I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のオペランドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため比較照合ではありません。 D: 比較照合のオペランドは別カテゴリの確認を流用しており、LU LOCADDR オペランドの根拠にならないため比較照合ではありません。比較照合のオペランドに出る LU LOCADDR オペランドは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LU LOCADDR オペランド**

    - 検証目的: 上書追跡のオペランドについて、LU LOCADDR オペランドは、Comm Server / VTAM / TCP/IP の VTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、上書追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLU LOCADDR オペランドを指定し、OSKB010047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LU LOCADDR オペランド
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LU LOCADDR オペランド
    CASE OSKB010047
    SOURCE z/OS Communications Server
    ```

    LU LOCADDR オペランドとOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010047を同じ出力で読み、上書追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010047 LU LOCADDR オペランド
    ```

    IST097IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LU LOCADDR オペランド と OSKB010047 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LU LOGAPPL オペランド {#c05-i0257}
*分類: VTAM LU 定義*  ・  難易度: 上級

LU LOGAPPL オペランドは、Comm Server / VTAM / TCP/IPのVTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 警告照合のオペランドに関係する LU LOGAPPL オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果から対象行を抜き出し、警告照合の証跡として残す。 ✅
    - B. LU LOGAPPL オペランドの名称と担当者名のみを残して警告照合のオペランドの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で警告照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず警告照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合のオペランドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のオペランドにおいて LU LOGAPPL オペランド は説明欄の「LU LOGAPPL オペランドの用途を通信サーバーの表示で確認する警告照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のオペランドに関連して、z/OS Communications Serverでは LU LOGAPPL オペランドの表示属性と IST097I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のオペランドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のオペランドは別カテゴリの確認を流用しており、LU LOGAPPL オペランドの根拠にならないため警告照合ではありません。 D: 警告照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため警告照合ではありません。警告照合のオペランドで使う LU LOGAPPL オペランドという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は警告照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LU LOGAPPL オペランド**

    - 検証目的: 区切追跡のオペランドについて、LU LOGAPPL オペランドは、Comm Server / VTAM / TCP/IP の VTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、区切追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLU LOGAPPL オペランドを指定し、OSKB010050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LU LOGAPPL オペランド
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LU LOGAPPL オペランド
    CASE OSKB010050
    SOURCE z/OS Communications Server
    ```

    LU LOGAPPL オペランドとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010050を同じ出力で読み、区切追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010050 LU LOGAPPL オペランド
    ```

    IST097IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LU LOGAPPL オペランド と OSKB010050 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LU MODETAB/DLOGMOD {#c05-i0258}
*分類: VTAM LU 定義*  ・  難易度: 上級

LU MODETAB/DLOGMODは、Comm Server / VTAM / TCP/IPのVTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 属性照合通知の属性照合として MODETAB/DLOGMOD を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 承認欄の記入を優先して出力メッセージを保存しない。
    - B. 名称と担当者名を保存して表示本文を確認しない。
    - C. 属性照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 別分類の結果を流用して同じ証跡として扱う。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。属性照合通知で扱う MODETAB/DLOGMOD は Comm Server / VTAM / TCP/IP の確認対象です（属性照合通知用語）。属性照合通知の担当者は属性照合として、表示本文とメッセージを照合します（属性照合通知照合）。属性照合通知の対応を残すと、後続担当者は同じ出典に戻って確認できます（属性照合通知出典）。A: 属性照合通知で表示とメッセージを結ぶ場合に根拠になります（属性照合通知A）。B: 属性照合通知で定義と出力の関係がない場合は追跡できません（属性照合通知B）。C: 属性照合通知で出典名のみでは実際の表示を説明できません（属性照合通知C）。D: 属性照合通知で操作記録のみでは値や状態の確認が不足します（属性照合通知D）。属性照合通知の初出用語として MODETAB/DLOGMOD を扱い、分類内の確認名として保存します（属性照合通知終点）。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LU MODETAB ・ DLOGMOD**

    - 検証目的: 出力追跡の・について、LU MODETAB/DLOGMOD は、Comm Server / VTAM / TCP/IP の VTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、出力追跡の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLU MODETAB ・ DLOGMを指定し、OSKB010048の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LU MODETAB ・ DLOGM
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LU MODETAB ・ DLOGM
    CASE OSKB010048
    SOURCE z/OS Communications Server
    ```

    LU MODETAB ・ DLOGMとOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010048を同じ出力で読み、出力追跡の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010048 LU MODETAB ・ DLOGMOD
    ```

    IST097IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LU MODETAB ・ DLOGM と OSKB010048 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LU PACING オペランド {#c05-i0259}
*分類: VTAM LU 定義*  ・  難易度: 上級

LU PACING オペランドは、Comm Server / VTAM / TCP/IPのVTAM LU 定義で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 復旧照合のオペランドで LU PACING オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LU PACING オペランドの出力を取らず復旧照合のオペランドの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧照合の確認記録にまとめる。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して復旧照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合のオペランドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合のオペランドにおいて LU PACING オペランド は説明欄の「復旧照合のオペランドに関係する定義値と表示行を照合する復旧照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のオペランドの証跡を読む担当者は、LU PACING オペランドの属性行と IST097I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のオペランドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のオペランドは別カテゴリの確認を流用しており、LU PACING オペランドの根拠にならないため復旧照合ではありません。復旧照合のオペランドに出る LU PACING オペランドは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LU PACING オペランド**

    - 検証目的: 範囲追跡のオペランドについて、LU PACING オペランドは、Comm Server / VTAM / TCP/IP の VTAM LU 定義で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、範囲追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLU PACING オペランドを指定し、OSKB010051の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LU PACING オペランド
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LU PACING オペランド
    CASE OSKB010051
    SOURCE z/OS Communications Server
    ```

    LU PACING オペランドとOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010051を同じ出力で読み、範囲追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010051 LU PACING オペランド
    ```

    IST097IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LU PACING オペランド と OSKB010051 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LU USSTAB オペランド {#c05-i0260}
*分類: VTAM LU 定義*  ・  難易度: 上級

LU USSTAB オペランドは、Comm Server / VTAM / TCP/IPのVTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 値域照合のオペランドに関する LU USSTAB オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず値域照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のオペランドの証跡として保存して根拠にする。
    - C. LU USSTAB オペランドの変更点を出力本文から切り離して値域照合のオペランドの承認欄のみ残す。
    - D. IST097I を含む表示を保存し、説明欄との差分を値域照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合のオペランドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合のオペランドにおいて LU USSTAB オペランド は説明欄の「LU USSTAB オペランドの状態と出力メッセージを結び付ける値域照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のオペランドに関する記録は、LU USSTAB オペランドの出力行と IST097I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため値域照合ではありません。 B: 値域照合のオペランドは別カテゴリの確認を流用しており、LU USSTAB オペランドの根拠にならないため値域照合ではありません。 C: 値域照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のオペランドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のオペランドで記録する LU USSTAB オペランドはz/OS Communications Serverの確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LU USSTAB オペランド**

    - 検証目的: 条件追跡のオペランドについて、LU USSTAB オペランドは、Comm Server / VTAM / TCP/IP の VTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、条件追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLU USSTAB オペランドを指定し、OSKB010049の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LU USSTAB オペランド
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LU USSTAB オペランド
    CASE OSKB010049
    SOURCE z/OS Communications Server
    ```

    LU USSTAB オペランドとOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010049を同じ出力で読み、条件追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010049 LU USSTAB オペランド
    ```

    IST097IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LU USSTAB オペランド と OSKB010049 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LU マクロの位置付け {#c05-i0261}
*分類: VTAM LU 定義*  ・  難易度: 上級

LU マクロの位置付けは、Comm Server / VTAM / TCP/IPのVTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 記録照合のマクロの位置付けに関係する LU マクロの位置付けの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録照合で再確認できる形にする。 ✅
    - B. LU マクロの位置付けの名称と担当者名のみを残して記録照合のマクロの位置付けの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で記録照合のマクロの位置付けを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず記録照合のマクロの位置付けの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合のマクロの位置付けにおいて選択記号 A を採用し、識別名は記録照合です。記録照合のマクロの位置付けにおいて LU マクロの位置付け は説明欄の「LU マクロの位置付けの用途を通信サーバーの表示で確認する記録照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のマクロの位置付けに関連して、z/OS Communications Serverでは LU マクロの位置付けの表示属性と IST097I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のマクロの位置付けは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のマクロの位置付けは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のマクロの位置付けは別カテゴリの確認を流用しており、LU マクロの位置付けの根拠にならないため記録照合ではありません。 D: 記録照合のマクロの位置付けは戻り値や記録番号に寄り、IST097I や属性表示を落とすため記録照合ではありません。記録照合のマクロの位置付けで使う LU マクロの位置付けという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は記録照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LU マクロの位置付け**

    - 検証目的: 探索追跡のマクロの位置付けについて、LU マクロの位置付けは、Comm Server / VTAM / TCP/IP の VTAM LU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、探索追跡のマクロの位置付けの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLU マクロの位置付けを指定し、OSKB010046の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LU マクロの位置付け
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LU マクロの位置付け
    CASE OSKB010046
    SOURCE z/OS Communications Server
    ```

    LU マクロの位置付けとOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010046を同じ出力で読み、探索追跡のマクロの位置付けの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010046 LU マクロの位置付け
    ```

    IST097IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LU マクロの位置付け と OSKB010046 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM MODE TABLE

### MODEENT COMPROT {#c05-i0262}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT COMPROTは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 呼出照合の通信サーバーで通信サーバーの運用確認を行います。MODEENT COMPROT の根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で呼出照合の通信サーバーを確認した扱いにする。
    - B. IST097I の有無を確認せず呼出照合の通信サーバーを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出照合の根拠を固定する。 ✅
    - D. MODEENT COMPROT の属性行を読まず呼出照合の通信サーバーの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合の通信サーバーにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合の通信サーバーにおいて MODEENT COMPROT は説明欄の「z/OS Communications Serverで MODEENT COMPROT の扱いを記録する呼出照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の通信サーバーを受け取る担当者は、MODEENT COMPROT の表示結果と IST097I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の通信サーバーは別カテゴリの確認を流用しており、MODEENT COMPROT の根拠にならないため呼出照合ではありません。 B: 呼出照合の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の通信サーバーは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の通信サーバーが示す MODEENT COMPROT は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT COMPROT**

    - 検証目的: 値域照合の通信サーバーについて、MODEENT COMPROT は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010036の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、値域照合の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT COMPROTを指定し、OSKB010036の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT COMPROT
    CASE OSKB010036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT COMPROT
    CASE OSKB010036
    SOURCE z/OS Communications Server
    ```

    MODEENT COMPROTとOSKB010036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010036を同じ出力で読み、値域照合の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010036
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010036 MODEENT COMPROT
    ```

    IST097IとOSKB010036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT COMPROT と OSKB010036 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT COS オペランド {#c05-i0263}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT COS オペランドは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 出力照合のオペランドに関する MODEENT COS オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず出力照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のオペランドの証跡として保存して根拠にする。
    - C. MODEENT COS オペランドの変更点を出力本文から切り離して出力照合のオペランドの承認欄のみ残す。
    - D. 同じ画面で対象行と IST097I を読み、出力照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合のオペランドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合のオペランドにおいて MODEENT COS オペランド は説明欄の「MODEENT COS オペランドの状態と出力メッセージを結び付ける出力照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のオペランドに関する記録は、MODEENT COS オペランドの出力行と IST097I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため出力照合ではありません。 B: 出力照合のオペランドは別カテゴリの確認を流用しており、MODEENT COS オペランドの根拠にならないため出力照合ではありません。 C: 出力照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のオペランドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のオペランドで記録する MODEENT COS オペランドはz/OS Communications Serverの確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT COS オペランド**

    - 検証目的: 構文追跡のオペランドについて、MODEENT COS オペランドは、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010041の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、構文追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT COS オペランドを指定し、OSKB010041の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT COS オペランド
    CASE OSKB010041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT COS オペランド
    CASE OSKB010041
    SOURCE z/OS Communications Server
    ```

    MODEENT COS オペランドとOSKB010041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010041を同じ出力で読み、構文追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010041 MODEENT COS オペランド
    ```

    IST097IとOSKB010041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT COS オペランド と OSKB010041 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT ENCR オペランド {#c05-i0264}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT ENCR オペランドは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 条件照合のオペランドに関係する MODEENT ENCR オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E で得た表示本文を使い、条件照合の採否を説明欄に結び付ける。 ✅
    - B. MODEENT ENCR オペランドの名称と担当者名のみを残して条件照合のオペランドの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で条件照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず条件照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合のオペランドにおいて選択記号 A を採用し、識別名は条件照合です。条件照合のオペランドにおいて MODEENT ENCR オペランド は説明欄の「MODEENT ENCR オペランドの用途を通信サーバーの表示で確認する条件照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のオペランドに関連して、z/OS Communications Serverでは MODEENT ENCR オペランドの表示属性と IST097I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のオペランドは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のオペランドは別カテゴリの確認を流用しており、MODEENT ENCR オペランドの根拠にならないため条件照合ではありません。 D: 条件照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため条件照合ではありません。条件照合のオペランドで使う MODEENT ENCR オペランドという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT ENCR オペランド**

    - 検証目的: 展開追跡のオペランドについて、MODEENT ENCR オペランドは、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、展開追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT ENCR オペランドを指定し、OSKB010042の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT ENCR オペランド
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT ENCR オペランド
    CASE OSKB010042
    SOURCE z/OS Communications Server
    ```

    MODEENT ENCR オペランドとOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010042を同じ出力で読み、展開追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010042 MODEENT ENCR オペランド
    ```

    IST097IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT ENCR オペランド と OSKB010042 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT FMPROF {#c05-i0265}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT FMPROFは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 変更確認の通信サーバーに関する MODEENT FMPROF の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず変更確認の通信サーバーの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の通信サーバーの証跡として保存して根拠にする。
    - C. MODEENT FMPROF の変更点を出力本文から切り離して変更確認の通信サーバーの承認欄のみ残す。
    - D. z/OS Communications Serverの表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認の通信サーバーにおいて選択記号 D を採用し、識別名は変更確認です。変更確認の通信サーバーにおいて MODEENT FMPROF は説明欄の「MODEENT FMPROF の状態と出力メッセージを結び付ける変更確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の通信サーバーに関する記録は、MODEENT FMPROF の出力行と IST097I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため変更確認ではありません。 B: 変更確認の通信サーバーは別カテゴリの確認を流用しており、MODEENT FMPROF の根拠にならないため変更確認ではありません。 C: 変更確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の通信サーバーで記録する MODEENT FMPROF はz/OS Communications Serverの確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT FMPROF**

    - 検証目的: 記録照合の通信サーバーについて、MODEENT FMPROF は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010033の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、記録照合の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT FMPROFを指定し、OSKB010033の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT FMPROF
    CASE OSKB010033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT FMPROF
    CASE OSKB010033
    SOURCE z/OS Communications Server
    ```

    MODEENT FMPROFとOSKB010033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010033を同じ出力で読み、記録照合の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010033 MODEENT FMPROF
    ```

    IST097IとOSKB010033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT FMPROF と OSKB010033 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT LOGMODE {#c05-i0266}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT LOGMODEは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 監査確認の通信サーバーで通信サーバーの運用確認を行います。MODEENT LOGMODE の根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で監査確認の通信サーバーを確認した扱いにする。
    - B. IST097I の有無を確認せず監査確認の通信サーバーを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 ✅
    - D. MODEENT LOGMODE の属性行を読まず監査確認の通信サーバーの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認の通信サーバーにおいて選択記号 C を採用し、識別名は監査確認です。監査確認の通信サーバーにおいて MODEENT LOGMODE は説明欄の「z/OS Communications Serverで MODEENT LOGMODE の扱いを記録する監査確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の通信サーバーを受け取る担当者は、MODEENT LOGMODE の表示結果と IST097I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の通信サーバーは別カテゴリの確認を流用しており、MODEENT LOGMODE の根拠にならないため監査確認ではありません。 B: 監査確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため監査確認ではありません。 C: 監査確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の通信サーバーが示す MODEENT LOGMODE は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT LOGMODE**

    - 検証目的: 優先照合の通信サーバーについて、MODEENT LOGMODE は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、優先照合の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT LOGMODEを指定し、OSKB010032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT LOGMODE
    CASE OSKB010032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT LOGMODE
    CASE OSKB010032
    SOURCE z/OS Communications Server
    ```

    MODEENT LOGMODEとOSKB010032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010032を同じ出力で読み、優先照合の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010032 MODEENT LOGMODE
    ```

    IST097IとOSKB010032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT LOGMODE と OSKB010032 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT MAXRU 概念 {#c05-i0267}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT MAXRU 概念は、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 終端照合の概念に関係する MODEENT MAXRU 概念の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果から対象行を抜き出し、終端照合の証跡として残す。 ✅
    - B. MODEENT MAXRU 概念の名称と担当者名のみを残して終端照合の概念の表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で終端照合の概念を確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず終端照合の概念の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合の概念において選択記号 A を採用し、識別名は終端照合です。終端照合の概念において MODEENT MAXRU 概念 は説明欄の「MODEENT MAXRU 概念の用途を通信サーバーの表示で確認する終端照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の概念に関連して、z/OS Communications Serverでは MODEENT MAXRU 概念の表示属性と IST097I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の概念は対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の概念は名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の概念は別カテゴリの確認を流用しており、MODEENT MAXRU 概念の根拠にならないため終端照合ではありません。 D: 終端照合の概念は戻り値や記録番号に寄り、IST097I や属性表示を落とすため終端照合ではありません。終端照合の概念で使う MODEENT MAXRU 概念という用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT MAXRU 概念**

    - 検証目的: 復旧照合の概念について、MODEENT MAXRU 概念は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010038の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、復旧照合の概念の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT MAXRU 概念を指定し、OSKB010038の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT MAXRU 概念
    CASE OSKB010038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT MAXRU 概念
    CASE OSKB010038
    SOURCE z/OS Communications Server
    ```

    MODEENT MAXRU 概念とOSKB010038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010038を同じ出力で読み、復旧照合の概念の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010038
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010038 MODEENT MAXRU 概念
    ```

    IST097IとOSKB010038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT MAXRU 概念 と OSKB010038 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT PRIPROT/SECPROT {#c05-i0268}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT PRIPROT/SECPROTは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として MODEENT を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 構文照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。構文照合保守で扱う MODEENT は Comm Server / VTAM / TCP/IP の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として MODEENT を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT PRIPROT ・ SECPROT**

    - 検証目的: 順序照合の・について、MODEENT PRIPROT/SECPROT は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象としに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010035の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、順序照合の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT PRIPROT ・ を指定し、OSKB010035の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT PRIPROT ・ 
    CASE OSKB010035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT PRIPROT ・ 
    CASE OSKB010035
    SOURCE z/OS Communications Server
    ```

    MODEENT PRIPROT ・ とOSKB010035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010035を同じ出力で読み、順序照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010035
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010035 MODEENT PRIPROT ・ SECPROT
    ```

    IST097IとOSKB010035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT PRIPROT ・  と OSKB010035 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT PSERVIC {#c05-i0269}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT PSERVICは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 探索照合の通信サーバーで MODEENT PSERVIC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MODEENT PSERVIC の出力を取らず探索照合の通信サーバーの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索照合の確認記録にまとめる。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して探索照合の通信サーバーの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の通信サーバーへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合の通信サーバーにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の通信サーバーにおいて MODEENT PSERVIC は説明欄の「探索照合の通信サーバーに関係する定義値と表示行を照合する探索照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の通信サーバーの証跡を読む担当者は、MODEENT PSERVIC の属性行と IST097I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の通信サーバーは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため探索照合ではありません。 D: 探索照合の通信サーバーは別カテゴリの確認を流用しており、MODEENT PSERVIC の根拠にならないため探索照合ではありません。探索照合の通信サーバーに出る MODEENT PSERVIC は Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT PSERVIC**

    - 検証目的: 監査照合の通信サーバーについて、MODEENT PSERVIC は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010039の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、監査照合の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT PSERVICを指定し、OSKB010039の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT PSERVIC
    CASE OSKB010039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT PSERVIC
    CASE OSKB010039
    SOURCE z/OS Communications Server
    ```

    MODEENT PSERVICとOSKB010039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010039を同じ出力で読み、監査照合の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010039 MODEENT PSERVIC
    ```

    IST097IとOSKB010039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT PSERVIC と OSKB010039 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT PSNDPAC/SSNDPAC {#c05-i0270}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT PSNDPAC/SSNDPACは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 出力照合照合の出力照合として MODEENT を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 出力照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。出力照合照合で扱う MODEENT は Comm Server / VTAM / TCP/IP の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として MODEENT を扱い、分類内の確認名として保存します（出力照合照合終点）。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT PSNDPAC ・ SSNDPAC**

    - 検証目的: 置換追跡の・について、MODEENT PSNDPAC/SSNDPAC は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象としに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、置換追跡の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT PSNDPAC ・ を指定し、OSKB010044の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT PSNDPAC ・ 
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT PSNDPAC ・ 
    CASE OSKB010044
    SOURCE z/OS Communications Server
    ```

    MODEENT PSNDPAC ・ とOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010044を同じ出力で読み、置換追跡の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010044 MODEENT PSNDPAC ・ SSNDPAC
    ```

    IST097IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT PSNDPAC ・  と OSKB010044 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT RUSIZES {#c05-i0271}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT RUSIZESは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 置換照合の通信サーバーに関する MODEENT RUSIZES の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず置換照合の通信サーバーの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の通信サーバーの証跡として保存して根拠にする。
    - C. MODEENT RUSIZES の変更点を出力本文から切り離して置換照合の通信サーバーの承認欄のみ残す。
    - D. IST097I を含む表示を保存し、説明欄との差分を置換照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合の通信サーバーにおいて選択記号 D を採用し、識別名は置換照合です。置換照合の通信サーバーにおいて MODEENT RUSIZES は説明欄の「MODEENT RUSIZES の状態と出力メッセージを結び付ける置換照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の通信サーバーに関する記録は、MODEENT RUSIZES の出力行と IST097I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため置換照合ではありません。 B: 置換照合の通信サーバーは別カテゴリの確認を流用しており、MODEENT RUSIZES の根拠にならないため置換照合ではありません。 C: 置換照合の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の通信サーバーは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の通信サーバーで記録する MODEENT RUSIZES はz/OS Communications Serverの確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT RUSIZES**

    - 検証目的: 警告照合の通信サーバーについて、MODEENT RUSIZES は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010037の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、警告照合の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT RUSIZESを指定し、OSKB010037の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT RUSIZES
    CASE OSKB010037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT RUSIZES
    CASE OSKB010037
    SOURCE z/OS Communications Server
    ```

    MODEENT RUSIZESとOSKB010037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010037を同じ出力で読み、警告照合の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010037
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010037 MODEENT RUSIZES
    ```

    IST097IとOSKB010037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT RUSIZES と OSKB010037 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT SRCVPAC/SSNDPAC {#c05-i0272}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT SRCVPAC/SSNDPACは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として MODEENT を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 展開照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。展開照合権限で扱う MODEENT は Comm Server / VTAM / TCP/IP の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として MODEENT を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT SRCVPAC ・ SSNDPAC**

    - 検証目的: 呼出追跡の・について、MODEENT SRCVPAC/SSNDPAC は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象としに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、呼出追跡の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT SRCVPAC ・ を指定し、OSKB010043の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT SRCVPAC ・ 
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT SRCVPAC ・ 
    CASE OSKB010043
    SOURCE z/OS Communications Server
    ```

    MODEENT SRCVPAC ・ とOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010043を同じ出力で読み、呼出追跡の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010043 MODEENT SRCVPAC ・ SSNDPAC
    ```

    IST097IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT SRCVPAC ・  と OSKB010043 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT TSPROF {#c05-i0273}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT TSPROFは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 構文照合の通信サーバーに関係する MODEENT TSPROF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文照合で再確認できる形にする。 ✅
    - B. MODEENT TSPROF の名称と担当者名のみを残して構文照合の通信サーバーの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で構文照合の通信サーバーを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず構文照合の通信サーバーの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合の通信サーバーにおいて選択記号 A を採用し、識別名は構文照合です。構文照合の通信サーバーにおいて MODEENT TSPROF は説明欄の「MODEENT TSPROF の用途を通信サーバーの表示で確認する構文照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の通信サーバーに関連して、z/OS Communications Serverでは MODEENT TSPROF の表示属性と IST097I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の通信サーバーは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の通信サーバーは別カテゴリの確認を流用しており、MODEENT TSPROF の根拠にならないため構文照合ではありません。 D: 構文照合の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため構文照合ではありません。構文照合の通信サーバーで使う MODEENT TSPROF という用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT TSPROF**

    - 検証目的: 比較照合の通信サーバーについて、MODEENT TSPROF は、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、比較照合の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT TSPROFを指定し、OSKB010034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT TSPROF
    CASE OSKB010034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT TSPROF
    CASE OSKB010034
    SOURCE z/OS Communications Server
    ```

    MODEENT TSPROFとOSKB010034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010034を同じ出力で読み、比較照合の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010034 MODEENT TSPROF
    ```

    IST097IとOSKB010034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT TSPROF と OSKB010034 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT マクロ {#c05-i0274}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT マクロは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 復旧確認のマクロで MODEENT マクロの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MODEENT マクロの出力を取らず復旧確認のマクロの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して復旧確認のマクロの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のマクロへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認のマクロにおいて選択記号 B を採用し、識別名は復旧確認です。復旧確認のマクロにおいて MODEENT マクロ は説明欄の「復旧確認のマクロに関係する定義値と表示行を照合する復旧確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認のマクロの証跡を読む担当者は、MODEENT マクロの属性行と IST097I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認のマクロは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認のマクロは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認のマクロは戻り値や記録番号に寄り、IST097I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認のマクロは別カテゴリの確認を流用しており、MODEENT マクロの根拠にならないため復旧確認ではありません。復旧確認のマクロに出る MODEENT マクロは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT マクロ**

    - 検証目的: 範囲照合のマクロについて、MODEENT マクロは、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、範囲照合のマクロの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT マクロを指定し、OSKB010031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT マクロ
    CASE OSKB010031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT マクロ
    CASE OSKB010031
    SOURCE z/OS Communications Server
    ```

    MODEENT マクロとOSKB010031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010031を同じ出力で読み、範囲照合のマクロの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010031 MODEENT マクロ
    ```

    IST097IとOSKB010031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT マクロ と OSKB010031 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODEENT 画面サイズ {#c05-i0275}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODEENT 画面サイズは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで操作画面や表示項目を確認するための項目です。入力欄、選択肢、実行後に変わる表示を分けて見ると、操作結果を追いやすくなります。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 上書照合の画面サイズで通信サーバーの運用確認を行います。MODEENT 画面サイズの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で上書照合の画面サイズを確認した扱いにする。
    - B. IST097I の有無を確認せず上書照合の画面サイズを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書照合の根拠にする。 ✅
    - D. MODEENT 画面サイズの属性行を読まず上書照合の画面サイズの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合の画面サイズにおいて選択記号 C を採用し、識別名は上書照合です。上書照合の画面サイズにおいて MODEENT 画面サイズ は説明欄の「z/OS Communications Serverで MODEENT 画面サイズの扱いを記録する上書照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の画面サイズを受け取る担当者は、MODEENT 画面サイズの表示結果と IST097I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の画面サイズは別カテゴリの確認を流用しており、MODEENT 画面サイズの根拠にならないため上書照合ではありません。 B: 上書照合の画面サイズは戻り値や記録番号に寄り、IST097I や属性表示を落とすため上書照合ではありません。 C: 上書照合の画面サイズは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の画面サイズは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の画面サイズが示す MODEENT 画面サイズは出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODEENT 画面サイズ**

    - 検証目的: 変更照合の画面サイズについて、MODEENT 画面サイズは、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で操作画面や表示項目を確認するための項目です。入力欄、選に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、変更照合の画面サイズの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODEENT 画面サイズを指定し、OSKB010040の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODEENT 画面サイズ
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODEENT 画面サイズ
    CASE OSKB010040
    SOURCE z/OS Communications Server
    ```

    MODEENT 画面サイズとOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010040を同じ出力で読み、変更照合の画面サイズの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010040 MODEENT 画面サイズ
    ```

    IST097IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODEENT 画面サイズ と OSKB010040 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODETAB のロード {#c05-i0276}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODETAB のロードは、Comm Server / VTAM / TCP/IPのVTAM MODE TABLEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 優先照合ののロードに関する MODETAB のロードの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず優先照合ののロードの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合ののロードの証跡として保存して根拠にする。
    - C. MODETAB のロードの変更点を出力本文から切り離して優先照合ののロードの承認欄のみ残す。
    - D. z/OS Communications Serverの表示形式に沿って根拠行を採り、優先照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合ののロードにおいて選択記号 D を採用し、識別名は優先照合です。優先照合ののロードにおいて MODETAB のロード は説明欄の「MODETAB のロードの状態と出力メッセージを結び付ける優先照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合ののロードに関する記録は、MODETAB のロードの出力行と IST097I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合ののロードは戻り値や記録番号に寄り、IST097I や属性表示を落とすため優先照合ではありません。 B: 優先照合ののロードは別カテゴリの確認を流用しており、MODETAB のロードの根拠にならないため優先照合ではありません。 C: 優先照合ののロードは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合ののロードは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合ののロードで記録する MODETAB のロードはz/OS Communications Serverの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODETAB のロード**

    - 検証目的: 終端追跡ののロードについて、MODETAB のロードは、Comm Server / VTAM / TCP/IP の VTAM MODE TABLE で機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、終端追跡ののロードの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODETAB のロードを指定し、OSKB010045の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODETAB のロード
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODETAB のロード
    CASE OSKB010045
    SOURCE z/OS Communications Server
    ```

    MODETAB のロードとOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010045を同じ出力で読み、終端追跡ののロードの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010045 MODETAB のロード
    ```

    IST097IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODETAB のロード と OSKB010045 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODETAB アセンブル {#c05-i0277}
*分類: VTAM MODE TABLE*  ・  難易度: 上級

MODETAB アセンブルは、MODETAB マクロでテーブル開始、MODEEND で終了、SYS1.VTAMLIB へロード

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のアセンブルに関係する MODETAB アセンブルの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 ✅
    - B. MODETAB アセンブルの名称と担当者名のみを残して警告確認のアセンブルの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で警告確認のアセンブルを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず警告確認のアセンブルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認のアセンブルにおいて選択記号 A を採用し、識別名は警告確認です。警告確認のアセンブルにおいて MODETAB アセンブル は説明欄の「MODETAB アセンブルの用途を通信サーバーの表示で確認する警告確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のアセンブルに関連して、z/OS Communications Serverでは MODETAB アセンブルの表示属性と IST097I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のアセンブルは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のアセンブルは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のアセンブルは別カテゴリの確認を流用しており、MODETAB アセンブルの根拠にならないため警告確認ではありません。 D: 警告確認のアセンブルは戻り値や記録番号に寄り、IST097I や属性表示を落とすため警告確認ではありません。警告確認のアセンブルで使う MODETAB アセンブルという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は警告確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **MODETAB アセンブル**

    - 検証目的: 区切照合のアセンブルについて、MODETAB アセンブルは、MODETAB マクロでテーブル開始、MODEEND で終了、SYS1.VTAMLIB へロードに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、区切照合のアセンブルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODETAB アセンブルを指定し、OSKB010030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODETAB アセンブル
    CASE OSKB010030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODETAB アセンブル
    CASE OSKB010030
    SOURCE z/OS Communications Server
    ```

    MODETAB アセンブルとOSKB010030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010030を同じ出力で読み、区切照合のアセンブルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010030 MODETAB アセンブル
    ```

    IST097IとOSKB010030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODETAB アセンブル と OSKB010030 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM Major Node

### APPL Major Node {#c05-i0278}
*分類: VTAM Major Node*  ・  難易度: 上級

APPL Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 展開確認の通信サーバーで APPL Major Nodeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. APPL Major Nodeの出力を取らず展開確認の通信サーバーの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開確認の根拠にする。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して展開確認の通信サーバーの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の通信サーバーへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認の通信サーバーにおいて選択記号 B を採用し、識別名は展開確認です。展開確認の通信サーバーにおいて APPL Major Node は説明欄の「展開確認の通信サーバーに関係する定義値と表示行を照合する展開確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の通信サーバーの証跡を読む担当者は、APPL Major Nodeの属性行と IST097I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため展開確認ではありません。 D: 展開確認の通信サーバーは別カテゴリの確認を流用しており、APPL Major Nodeの根拠にならないため展開確認ではありません。展開確認の通信サーバーに出る APPL Major Nodeは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **APPL Major Node**

    - 検証目的: 終端検査の通信サーバーについて、APPL Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、終端検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にAPPL Major Nodeを指定し、OSKB010065の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND APPL Major Node
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM APPL Major Node
    CASE OSKB010065
    SOURCE z/OS Communications Server
    ```

    APPL Major NodeとOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010065を同じ出力で読み、終端検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010065 APPL Major Node
    ```

    IST097IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の APPL Major Node と OSKB010065 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### CDRM Major Node {#c05-i0279}
*分類: VTAM Major Node*  ・  難易度: 上級

CDRM Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 構文確認の通信サーバーに関係する CDRM Major Nodeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文確認の確認記録にまとめる。 ✅
    - B. CDRM Major Nodeの名称と担当者名のみを残して構文確認の通信サーバーの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で構文確認の通信サーバーを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず構文確認の通信サーバーの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認の通信サーバーにおいて選択記号 A を採用し、識別名は構文確認です。構文確認の通信サーバーにおいて CDRM Major Node は説明欄の「CDRM Major Nodeの用途を通信サーバーの表示で確認する構文確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の通信サーバーに関連して、z/OS Communications Serverでは CDRM Major Nodeの表示属性と IST097I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の通信サーバーは別カテゴリの確認を流用しており、CDRM Major Nodeの根拠にならないため構文確認ではありません。 D: 構文確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため構文確認ではありません。構文確認の通信サーバーで使う CDRM Major Nodeという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は構文確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **CDRM Major Node**

    - 検証目的: 置換検査の通信サーバーについて、CDRM Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、置換検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCDRM Major Nodeを指定し、OSKB010064の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CDRM Major Node
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CDRM Major Node
    CASE OSKB010064
    SOURCE z/OS Communications Server
    ```

    CDRM Major NodeとOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010064を同じ出力で読み、置換検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010064 CDRM Major Node
    ```

    IST097IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の CDRM Major Node と OSKB010064 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### CDRSC Major Node {#c05-i0280}
*分類: VTAM Major Node*  ・  難易度: 上級

CDRSC Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 区切追跡の通信サーバーで CDRSC Major Nodeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CDRSC Major Nodeの出力を取らず区切追跡の通信サーバーの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切追跡の確認記録にまとめる。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して区切追跡の通信サーバーの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の通信サーバーへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡の通信サーバーにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡の通信サーバーにおいて CDRSC Major Node は説明欄の「区切追跡の通信サーバーに関係する定義値と表示行を照合する区切追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の通信サーバーの証跡を読む担当者は、CDRSC Major Nodeの属性行と IST097I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の通信サーバーは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の通信サーバーは別カテゴリの確認を流用しており、CDRSC Major Nodeの根拠にならないため区切追跡ではありません。区切追跡の通信サーバーに出る CDRSC Major Nodeは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **CDRSC Major Node**

    - 検証目的: 呼出検査の通信サーバーについて、CDRSC Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、呼出検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCDRSC Major Nodeを指定し、OSKB010063の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CDRSC Major Node
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CDRSC Major Node
    CASE OSKB010063
    SOURCE z/OS Communications Server
    ```

    CDRSC Major NodeとOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010063を同じ出力で読み、呼出検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010063 CDRSC Major Node
    ```

    IST097IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の CDRSC Major Node と OSKB010063 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LBUILD / Local SNA Major Node {#c05-i0281}
*分類: VTAM Major Node*  ・  難易度: 上級

LBUILD / Local SNA Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 範囲照合入力の範囲照合として LBUILD を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 範囲照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 名称と担当者名を保存して表示本文を確認しない。
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解はAです。範囲照合入力で扱う LBUILD は Comm Server / VTAM / TCP/IP の確認対象です（範囲照合入力用語）。範囲照合入力の担当者は範囲照合として、表示本文とメッセージを照合します（範囲照合入力照合）。範囲照合入力の対応を残すと、後続担当者は同じ出典に戻って確認できます（範囲照合入力出典）。A: 範囲照合入力で表示とメッセージを結ぶ場合に根拠になります（範囲照合入力A）。B: 範囲照合入力で定義と出力の関係がない場合は追跡できません（範囲照合入力B）。C: 範囲照合入力で出典名のみでは実際の表示を説明できません（範囲照合入力C）。D: 範囲照合入力で操作記録のみでは値や状態の確認が不足します（範囲照合入力D）。範囲照合入力の初出用語として LBUILD を扱い、分類内の確認名として保存します（範囲照合入力終点）。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LBUILD ・ Local SNA Major Node**

    - 検証目的: 展開検査の・について、LBUILD / Local SNA Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、またはに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、展開検査の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLBUILD ・ Local SNAを指定し、OSKB010062の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LBUILD ・ Local SNA
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LBUILD ・ Local SNA
    CASE OSKB010062
    SOURCE z/OS Communications Server
    ```

    LBUILD ・ Local SNAとOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010062を同じ出力で読み、展開検査の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010062 LBUILD ・ Local SNA Major
    ```

    IST097IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LBUILD ・ Local SNA と OSKB010062 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### LOCAL Major Node {#c05-i0282}
*分類: VTAM Major Node*  ・  難易度: 上級

LOCAL Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 上書追跡の通信サーバーで通信サーバーの運用確認を行います。LOCAL Major Nodeの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で上書追跡の通信サーバーを確認した扱いにする。
    - B. IST097I の有無を確認せず上書追跡の通信サーバーを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書追跡の根拠を固定する。 ✅
    - D. LOCAL Major Nodeの属性行を読まず上書追跡の通信サーバーの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡の通信サーバーにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡の通信サーバーにおいて LOCAL Major Node は説明欄の「z/OS Communications Serverで LOCAL Major Nodeの扱いを記録する上書追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の通信サーバーを受け取る担当者は、LOCAL Major Nodeの表示結果と IST097I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の通信サーバーは別カテゴリの確認を流用しており、LOCAL Major Nodeの根拠にならないため上書追跡ではありません。 B: 上書追跡の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の通信サーバーは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の通信サーバーが示す LOCAL Major Nodeは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **LOCAL Major Node**

    - 検証目的: 変更追跡の通信サーバーについて、LOCAL Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、変更追跡の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLOCAL Major Nodeを指定し、OSKB010060の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LOCAL Major Node
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LOCAL Major Node
    CASE OSKB010060
    SOURCE z/OS Communications Server
    ```

    LOCAL Major NodeとOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010060を同じ出力で読み、変更追跡の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010060 LOCAL Major Node
    ```

    IST097IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の LOCAL Major Node と OSKB010060 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### Model Major Node {#c05-i0283}
*分類: VTAM Major Node*  ・  難易度: 上級

Model Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 終端確認の通信サーバーに関係する Model Major Nodeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端確認として引き継ぐ。 ✅
    - B. Model Major Nodeの名称と担当者名のみを残して終端確認の通信サーバーの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で終端確認の通信サーバーを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず終端確認の通信サーバーの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認の通信サーバーにおいて選択記号 A を採用し、識別名は終端確認です。終端確認の通信サーバーにおいて Model Major Node は説明欄の「Model Major Nodeの用途を通信サーバーの表示で確認する終端確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の通信サーバーに関連して、z/OS Communications Serverでは Model Major Nodeの表示属性と IST097I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の通信サーバーは別カテゴリの確認を流用しており、Model Major Nodeの根拠にならないため終端確認ではありません。 D: 終端確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため終端確認ではありません。終端確認の通信サーバーで使う Model Major Nodeという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は終端確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **Model Major Node**

    - 検証目的: 出力検査の通信サーバーについて、Model Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeでリソース定義、モデル、またはポリシーを読むためのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、出力検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にModel Major Nodeを指定し、OSKB010068の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Model Major Node
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Model Major Node
    CASE OSKB010068
    SOURCE z/OS Communications Server
    ```

    Model Major NodeとOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010068を同じ出力で読み、出力検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010068 Model Major Node
    ```

    IST097IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の Model Major Node と OSKB010068 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### SWITCHED Major Node {#c05-i0284}
*分類: VTAM Major Node*  ・  難易度: 上級

SWITCHED Major Nodeは、スイッチド回線/SDLC ダイヤルイン用、ダイナミック XID で接続

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 出力追跡の通信サーバーに関する SWITCHED Major Nodeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず出力追跡の通信サーバーの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の通信サーバーの証跡として保存して根拠にする。
    - C. SWITCHED Major Nodeの変更点を出力本文から切り離して出力追跡の通信サーバーの承認欄のみ残す。
    - D. IST097I を含む表示を保存し、説明欄との差分を出力追跡で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡の通信サーバーにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の通信サーバーにおいて SWITCHED Major Node は説明欄の「SWITCHED Major Nodeの状態と出力メッセージを結び付ける出力追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の通信サーバーに関する記録は、SWITCHED Major Nodeの出力行と IST097I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の通信サーバーは別カテゴリの確認を流用しており、SWITCHED Major Nodeの根拠にならないため出力追跡ではありません。 C: 出力追跡の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の通信サーバーは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の通信サーバーで記録する SWITCHED Major Nodeはz/OS Communications Serverの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **SWITCHED Major Node**

    - 検証目的: 構文検査の通信サーバーについて、SWITCHED Major Nodeは、スイッチド回線/SDLC ダイヤルイン用、ダイナミック XID で接続に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、構文検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSWITCHED Major Nodを指定し、OSKB010061の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SWITCHED Major Nod
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SWITCHED Major Nod
    CASE OSKB010061
    SOURCE z/OS Communications Server
    ```

    SWITCHED Major NodとOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010061を同じ出力で読み、構文検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010061 SWITCHED Major Node
    ```

    IST097IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の SWITCHED Major Nod と OSKB010061 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### TRL Major Node {#c05-i0285}
*分類: VTAM Major Node*  ・  難易度: 上級

TRL Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 呼出確認の通信サーバーで通信サーバーの運用確認を行います。TRL Major Nodeの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で呼出確認の通信サーバーを確認した扱いにする。
    - B. IST097I の有無を確認せず呼出確認の通信サーバーを正常終了として記録する。
    - C. 同じ画面で対象行と IST097I を読み、呼出確認の結果として保存する。 ✅
    - D. TRL Major Nodeの属性行を読まず呼出確認の通信サーバーの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認の通信サーバーにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認の通信サーバーにおいて TRL Major Node は説明欄の「z/OS Communications Serverで TRL Major Nodeの扱いを記録する呼出確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の通信サーバーを受け取る担当者は、TRL Major Nodeの表示結果と IST097I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の通信サーバーは別カテゴリの確認を流用しており、TRL Major Nodeの根拠にならないため呼出確認ではありません。 B: 呼出確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の通信サーバーが示す TRL Major Nodeは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **TRL Major Node**

    - 検証目的: 探索検査の通信サーバーについて、TRL Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、探索検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRL Major Nodeを指定し、OSKB010066の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRL Major Node
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRL Major Node
    CASE OSKB010066
    SOURCE z/OS Communications Server
    ```

    TRL Major NodeとOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010066を同じ出力で読み、探索検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010066 TRL Major Node
    ```

    IST097IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の TRL Major Node と OSKB010066 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### VBUILD TYPE 指定 {#c05-i0286}
*分類: VTAM Major Node*  ・  難易度: 上級

VBUILD TYPE 指定は、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 探索確認の指定で VBUILD TYPE 指定の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VBUILD TYPE 指定の出力を取らず探索確認の指定の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索確認の確認にする。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して探索確認の指定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の指定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認の指定において選択記号 B を採用し、識別名は探索確認です。探索確認の指定において VBUILD TYPE 指定 は説明欄の「探索確認の指定に関係する定義値と表示行を照合する探索確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認の指定の証跡を読む担当者は、VBUILD TYPE 指定の属性行と IST097I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認の指定は名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認の指定は対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認の指定は戻り値や記録番号に寄り、IST097I や属性表示を落とすため探索確認ではありません。 D: 探索確認の指定は別カテゴリの確認を流用しており、VBUILD TYPE 指定の根拠にならないため探索確認ではありません。探索確認の指定に出る VBUILD TYPE 指定は Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は探索確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **VBUILD TYPE 指定**

    - 検証目的: 条件検査の指定について、VBUILD TYPE 指定は、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、条件検査の指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にVBUILD TYPE 指定を指定し、OSKB010069の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND VBUILD TYPE 指定
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM VBUILD TYPE 指定
    CASE OSKB010069
    SOURCE z/OS Communications Server
    ```

    VBUILD TYPE 指定とOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010069を同じ出力で読み、条件検査の指定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010069 VBUILD TYPE 指定
    ```

    IST097IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の VBUILD TYPE 指定 と OSKB010069 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### XCA Major Node {#c05-i0287}
*分類: VTAM Major Node*  ・  難易度: 上級

XCA Major Nodeは、Comm Server / VTAM / TCP/IPのVTAM Major Nodeで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 置換確認の通信サーバーに関する XCA Major Nodeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず置換確認の通信サーバーの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の通信サーバーの証跡として保存して根拠にする。
    - C. XCA Major Nodeの変更点を出力本文から切り離して置換確認の通信サーバーの承認欄のみ残す。
    - D. D NET,ID=OSKBAPPL,E で得た表示本文を使い、置換確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認の通信サーバーにおいて選択記号 D を採用し、識別名は置換確認です。置換確認の通信サーバーにおいて XCA Major Node は説明欄の「XCA Major Nodeの状態と出力メッセージを結び付ける置換確認項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の通信サーバーに関する記録は、XCA Major Nodeの出力行と IST097I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の通信サーバーは戻り値や記録番号に寄り、IST097I や属性表示を落とすため置換確認ではありません。 B: 置換確認の通信サーバーは別カテゴリの確認を流用しており、XCA Major Nodeの根拠にならないため置換確認ではありません。 C: 置換確認の通信サーバーは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の通信サーバーは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の通信サーバーで記録する XCA Major Nodeはz/OS Communications Serverの確認記録に残す対象名であり、用語名は置換確認です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **XCA Major Node**

    - 検証目的: 上書検査の通信サーバーについて、XCA Major Nodeは、Comm Server / VTAM / TCP/IP の VTAM Major Nodeで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、上書検査の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にXCA Major Nodeを指定し、OSKB010067の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND XCA Major Node
    CASE OSKB010067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM XCA Major Node
    CASE OSKB010067
    SOURCE z/OS Communications Server
    ```

    XCA Major NodeとOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010067を同じ出力で読み、上書検査の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010067
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010067 XCA Major Node
    ```

    IST097IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の XCA Major Node と OSKB010067 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM PU 定義

### PU ADDR オペランド {#c05-i0288}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU ADDR オペランドは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 構文追跡のオペランドに関係する PU ADDR オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E で得た表示本文を使い、構文追跡の採否を説明欄に結び付ける。 ✅
    - B. PU ADDR オペランドの名称と担当者名のみを残して構文追跡のオペランドの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で構文追跡のオペランドを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず構文追跡のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡のオペランドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のオペランドにおいて PU ADDR オペランド は説明欄の「PU ADDR オペランドの用途を通信サーバーの表示で確認する構文追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のオペランドに関連して、z/OS Communications Serverでは PU ADDR オペランドの表示属性と IST097I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のオペランドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のオペランドは別カテゴリの確認を流用しており、PU ADDR オペランドの根拠にならないため構文追跡ではありません。 D: 構文追跡のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため構文追跡ではありません。構文追跡のオペランドで使う PU ADDR オペランドという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は構文追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU ADDR オペランド**

    - 検証目的: 比較追跡のオペランドについて、PU ADDR オペランドは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、比較追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU ADDR オペランドを指定し、OSKB010054の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU ADDR オペランド
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU ADDR オペランド
    CASE OSKB010054
    SOURCE z/OS Communications Server
    ```

    PU ADDR オペランドとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010054を同じ出力で読み、比較追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010054 PU ADDR オペランド
    ```

    IST097IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU ADDR オペランド と OSKB010054 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU CPNAME オペランド {#c05-i0289}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU CPNAME オペランドは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 呼出追跡のオペランドで通信サーバーの運用確認を行います。PU CPNAME オペランドの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で呼出追跡のオペランドを確認した扱いにする。
    - B. IST097I の有無を確認せず呼出追跡のオペランドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 ✅
    - D. PU CPNAME オペランドの属性行を読まず呼出追跡のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡のオペランドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のオペランドにおいて PU CPNAME オペランド は説明欄の「z/OS Communications Serverで PU CPNAME オペランドの扱いを記録する呼出追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のオペランドを受け取る担当者は、PU CPNAME オペランドの表示結果と IST097I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のオペランドは別カテゴリの確認を流用しており、PU CPNAME オペランドの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のオペランドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のオペランドが示す PU CPNAME オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU CPNAME オペランド**

    - 検証目的: 値域追跡のオペランドについて、PU CPNAME オペランドは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、値域追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU CPNAME オペランドを指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU CPNAME オペランド
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU CPNAME オペランド
    CASE OSKB010056
    SOURCE z/OS Communications Server
    ```

    PU CPNAME オペランドとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010056を同じ出力で読み、値域追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010056 PU CPNAME オペランド
    ```

    IST097IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU CPNAME オペランド と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU DISCNT オペランド {#c05-i0290}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU DISCNT オペランドは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 終端追跡のオペランドに関係する PU DISCNT オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端追跡で再確認できる形にする。 ✅
    - B. PU DISCNT オペランドの名称と担当者名のみを残して終端追跡のオペランドの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で終端追跡のオペランドを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず終端追跡のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡のオペランドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡のオペランドにおいて PU DISCNT オペランド は説明欄の「PU DISCNT オペランドの用途を通信サーバーの表示で確認する終端追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のオペランドに関連して、z/OS Communications Serverでは PU DISCNT オペランドの表示属性と IST097I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のオペランドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のオペランドは別カテゴリの確認を流用しており、PU DISCNT オペランドの根拠にならないため終端追跡ではありません。 D: 終端追跡のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため終端追跡ではありません。終端追跡のオペランドで使う PU DISCNT オペランドという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU DISCNT オペランド**

    - 検証目的: 復旧追跡のオペランドについて、PU DISCNT オペランドは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、復旧追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU DISCNT オペランドを指定し、OSKB010058の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU DISCNT オペランド
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU DISCNT オペランド
    CASE OSKB010058
    SOURCE z/OS Communications Server
    ```

    PU DISCNT オペランドとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010058を同じ出力で読み、復旧追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010058 PU DISCNT オペランド
    ```

    IST097IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU DISCNT オペランド と OSKB010058 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU IDBLK/IDNUM {#c05-i0291}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU IDBLK/IDNUMは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **PU IDBLK ・ IDNUM**

    - 検証目的: 順序追跡の・について、PU IDBLK/IDNUM は、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、順序追跡の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU IDBLK ・ IDNUMを指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU IDBLK ・ IDNUM
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU IDBLK ・ IDNUM
    CASE OSKB010055
    SOURCE z/OS Communications Server
    ```

    PU IDBLK ・ IDNUMとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010055を同じ出力で読み、順序追跡の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010055 PU IDBLK ・ IDNUM
    ```

    IST097IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU IDBLK ・ IDNUM と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU MAXDATA オペランド {#c05-i0292}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU MAXDATA オペランドは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 置換追跡のオペランドに関する PU MAXDATA オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず置換追跡のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のオペランドの証跡として保存して根拠にする。
    - C. PU MAXDATA オペランドの変更点を出力本文から切り離して置換追跡のオペランドの承認欄のみ残す。
    - D. z/OS Communications Serverの表示形式に沿って根拠行を採り、置換追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡のオペランドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のオペランドにおいて PU MAXDATA オペランド は説明欄の「PU MAXDATA オペランドの状態と出力メッセージを結び付ける置換追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のオペランドに関する記録は、PU MAXDATA オペランドの出力行と IST097I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のオペランドは別カテゴリの確認を流用しており、PU MAXDATA オペランドの根拠にならないため置換追跡ではありません。 C: 置換追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のオペランドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のオペランドで記録する PU MAXDATA オペランドはz/OS Communications Serverの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU MAXDATA オペランド**

    - 検証目的: 警告追跡のオペランドについて、PU MAXDATA オペランドは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、警告追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU MAXDATA オペランドを指定し、OSKB010057の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU MAXDATA オペランド
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU MAXDATA オペランド
    CASE OSKB010057
    SOURCE z/OS Communications Server
    ```

    PU MAXDATA オペランドとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010057を同じ出力で読み、警告追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010057 PU MAXDATA オペランド
    ```

    IST097IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU MAXDATA オペランド と OSKB010057 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU PUTYPE オペランド {#c05-i0293}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU PUTYPE オペランドは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 変更照合のオペランドに関する PU PUTYPE オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず変更照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のオペランドの証跡として保存して根拠にする。
    - C. PU PUTYPE オペランドの変更点を出力本文から切り離して変更照合のオペランドの承認欄のみ残す。
    - D. 同じ画面で対象行と IST097I を読み、変更照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合のオペランドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合のオペランドにおいて PU PUTYPE オペランド は説明欄の「PU PUTYPE オペランドの状態と出力メッセージを結び付ける変更照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のオペランドに関する記録は、PU PUTYPE オペランドの出力行と IST097I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため変更照合ではありません。 B: 変更照合のオペランドは別カテゴリの確認を流用しており、PU PUTYPE オペランドの根拠にならないため変更照合ではありません。 C: 変更照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のオペランドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のオペランドで記録する PU PUTYPE オペランドはz/OS Communications Serverの確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU PUTYPE オペランド**

    - 検証目的: 記録追跡のオペランドについて、PU PUTYPE オペランドは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、記録追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU PUTYPE オペランドを指定し、OSKB010053の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU PUTYPE オペランド
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU PUTYPE オペランド
    CASE OSKB010053
    SOURCE z/OS Communications Server
    ```

    PU PUTYPE オペランドとOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010053を同じ出力で読み、記録追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010053 PU PUTYPE オペランド
    ```

    IST097IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU PUTYPE オペランド と OSKB010053 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU SSCPFM オペランド {#c05-i0294}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU SSCPFM オペランドは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 探索追跡のオペランドで PU SSCPFM オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PU SSCPFM オペランドの出力を取らず探索追跡のオペランドの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索追跡の確認値として扱う。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して探索追跡のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡のオペランドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡のオペランドにおいて PU SSCPFM オペランド は説明欄の「探索追跡のオペランドに関係する定義値と表示行を照合する探索追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のオペランドの証跡を読む担当者は、PU SSCPFM オペランドの属性行と IST097I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のオペランドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のオペランドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のオペランドは別カテゴリの確認を流用しており、PU SSCPFM オペランドの根拠にならないため探索追跡ではありません。探索追跡のオペランドに出る PU SSCPFM オペランドは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU SSCPFM オペランド**

    - 検証目的: 監査追跡のオペランドについて、PU SSCPFM オペランドは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、監査追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU SSCPFM オペランドを指定し、OSKB010059の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU SSCPFM オペランド
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU SSCPFM オペランド
    CASE OSKB010059
    SOURCE z/OS Communications Server
    ```

    PU SSCPFM オペランドとOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010059を同じ出力で読み、監査追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010059 PU SSCPFM オペランド
    ```

    IST097IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU SSCPFM オペランド と OSKB010059 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PU マクロの位置付け {#c05-i0295}
*分類: VTAM PU 定義*  ・  難易度: 上級

PU マクロの位置付けは、Comm Server / VTAM / TCP/IPのVTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 監査照合のマクロの位置付けで通信サーバーの運用確認を行います。PU マクロの位置付けの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で監査照合のマクロの位置付けを確認した扱いにする。
    - B. IST097I の有無を確認せず監査照合のマクロの位置付けを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査照合の根拠にする。 ✅
    - D. PU マクロの位置付けの属性行を読まず監査照合のマクロの位置付けの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合のマクロの位置付けにおいて選択記号 C を採用し、識別名は監査照合です。監査照合のマクロの位置付けにおいて PU マクロの位置付け は説明欄の「z/OS Communications Serverで PU マクロの位置付けの扱いを記録する監査照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のマクロの位置付けを受け取る担当者は、PU マクロの位置付けの表示結果と IST097I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のマクロの位置付けは別カテゴリの確認を流用しており、PU マクロの位置付けの根拠にならないため監査照合ではありません。 B: 監査照合のマクロの位置付けは戻り値や記録番号に寄り、IST097I や属性表示を落とすため監査照合ではありません。 C: 監査照合のマクロの位置付けは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のマクロの位置付けは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のマクロの位置付けが示す PU マクロの位置付けは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PU マクロの位置付け**

    - 検証目的: 優先追跡のマクロの位置付けについて、PU マクロの位置付けは、Comm Server / VTAM / TCP/IP の VTAM PU 定義で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、優先追跡のマクロの位置付けの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPU マクロの位置付けを指定し、OSKB010052の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PU マクロの位置付け
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PU マクロの位置付け
    CASE OSKB010052
    SOURCE z/OS Communications Server
    ```

    PU マクロの位置付けとOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010052を同じ出力で読み、優先追跡のマクロの位置付けの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010052 PU マクロの位置付け
    ```

    IST097IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PU マクロの位置付け と OSKB010052 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM V NET コマンド

### V NET,ACT {#c05-i0296}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,ACTは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 置換照合のコマンドに関する V NET,ACT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず置換照合のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のコマンドの証跡として保存して根拠にする。
    - C. V NET,ACT の変更点を出力本文から切り離して置換照合のコマンドの承認欄のみ残す。
    - D. D NET,ID=OSKBAPPL,E の結果から対象行を抜き出し、置換照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合のコマンドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合のコマンドにおいて V NET,ACT は説明欄の「V NET,ACT の状態と出力メッセージを結び付ける置換照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のコマンドに関する記録は、V NET,ACT の出力行と IST097I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため置換照合ではありません。 B: 置換照合のコマンドは別カテゴリの確認を流用しており、V NET,ACT の根拠にならないため置換照合ではありません。 C: 置換照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のコマンドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のコマンドで記録する V NET,ACT はz/OS Communications Serverの確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,ACT**

    - 検証目的: 上書判定のコマンドについて、V NET,ACT は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、上書判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,ACTを指定し、OSKB010087の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,ACT
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,ACT
    CASE OSKB010087
    SOURCE z/OS Communications Server
    ```

    V NET,ACTとOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010087を同じ出力で読み、上書判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010087 V NET,ACT
    ```

    IST097IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,ACT と OSKB010087 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,ACT,ID=name,SCOPE=ALL {#c05-i0297}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,ACT,ID=name,SCOPE=ALLは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **V NET,ACT,ID=name,SCOPE=ALL**

    - 検証目的: 出力判定のコマンドについて、V NET,ACT,ID=name,SCOPE=ALL は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010088の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、出力判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,ACT,ID=name,を指定し、OSKB010088の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,ACT,ID=name,
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,ACT,ID=name,
    CASE OSKB010088
    SOURCE z/OS Communications Server
    ```

    V NET,ACT,ID=name,とOSKB010088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010088を同じ出力で読み、出力判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010088 V NET,ACT,ID=name,SCOPE=
    ```

    IST097IとOSKB010088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,ACT,ID=name, と OSKB010088 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,INACT {#c05-i0298}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,INACTは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 探索照合のコマンドで V NET,INACT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V NET,INACT の出力を取らず探索照合のコマンドの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索照合の根拠にする。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して探索照合のコマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のコマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合のコマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合のコマンドにおいて V NET,INACT は説明欄の「探索照合のコマンドに関係する定義値と表示行を照合する探索照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のコマンドの証跡を読む担当者は、V NET,INACT の属性行と IST097I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のコマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため探索照合ではありません。 D: 探索照合のコマンドは別カテゴリの確認を流用しており、V NET,INACT の根拠にならないため探索照合ではありません。探索照合のコマンドに出る V NET,INACT は Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,INACT**

    - 検証目的: 条件判定のコマンドについて、V NET,INACT は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010089の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、条件判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,INACTを指定し、OSKB010089の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,INACT
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,INACT
    CASE OSKB010089
    SOURCE z/OS Communications Server
    ```

    V NET,INACTとOSKB010089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010089を同じ出力で読み、条件判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010089 V NET,INACT
    ```

    IST097IとOSKB010089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,INACT と OSKB010089 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,INACT,F {#c05-i0299}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,INACT,Fは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 出力照合のコマンドに関する V NET,INACT,F の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず出力照合のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のコマンドの証跡として保存して根拠にする。
    - C. V NET,INACT,F の変更点を出力本文から切り離して出力照合のコマンドの承認欄のみ残す。
    - D. D NET,ID=OSKBAPPL,E で得た表示本文を使い、出力照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合のコマンドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合のコマンドにおいて V NET,INACT,F は説明欄の「V NET,INACT,F の状態と出力メッセージを結び付ける出力照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のコマンドに関する記録は、V NET,INACT,F の出力行と IST097I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため出力照合ではありません。 B: 出力照合のコマンドは別カテゴリの確認を流用しており、V NET,INACT,F の根拠にならないため出力照合ではありません。 C: 出力照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のコマンドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のコマンドで記録する V NET,INACT,F はz/OS Communications Serverの確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,INACT,F**

    - 検証目的: 範囲判定のコマンドについて、V NET,INACT,F は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010091の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、範囲判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,INACT,Fを指定し、OSKB010091の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,INACT,F
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,INACT,F
    CASE OSKB010091
    SOURCE z/OS Communications Server
    ```

    V NET,INACT,FとOSKB010091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010091を同じ出力で読み、範囲判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010091 V NET,INACT,F
    ```

    IST097IとOSKB010091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,INACT,F と OSKB010091 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,INACT,GIVEBACK {#c05-i0300}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,INACT,GIVEBACKは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **V NET,INACT,GIVEBACK**

    - 検証目的: 優先判定のコマンドについて、V NET,INACT,GIVEBACK は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、優先判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,INACT,GIVEBAを指定し、OSKB010092の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,INACT,GIVEBA
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,INACT,GIVEBA
    CASE OSKB010092
    SOURCE z/OS Communications Server
    ```

    V NET,INACT,GIVEBAとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010092を同じ出力で読み、優先判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010092 V NET,INACT,GIVEBACK
    ```

    IST097IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,INACT,GIVEBA と OSKB010092 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,INACT,I {#c05-i0301}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,INACT,Iは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 上書照合のコマンドで通信サーバーの運用確認を行います。V NET,INACT,I の根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で上書照合のコマンドを確認した扱いにする。
    - B. IST097I の有無を確認せず上書照合のコマンドを正常終了として記録する。
    - C. 同じ画面で対象行と IST097I を読み、上書照合の結果として保存する。 ✅
    - D. V NET,INACT,I の属性行を読まず上書照合のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合のコマンドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合のコマンドにおいて V NET,INACT,I は説明欄の「z/OS Communications Serverで V NET,INACT,I の扱いを記録する上書照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のコマンドを受け取る担当者は、V NET,INACT,I の表示結果と IST097I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のコマンドは別カテゴリの確認を流用しており、V NET,INACT,I の根拠にならないため上書照合ではありません。 B: 上書照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため上書照合ではありません。 C: 上書照合のコマンドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のコマンドが示す V NET,INACT,I は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,INACT,I**

    - 検証目的: 区切判定のコマンドについて、V NET,INACT,I は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010090の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、区切判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,INACT,Iを指定し、OSKB010090の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,INACT,I
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,INACT,I
    CASE OSKB010090
    SOURCE z/OS Communications Server
    ```

    V NET,INACT,IとOSKB010090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010090を同じ出力で読み、区切判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010090 V NET,INACT,I
    ```

    IST097IとOSKB010090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,INACT,I と OSKB010090 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,LOGON {#c05-i0302}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,LOGONは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 範囲照合のコマンドで通信サーバーの運用確認を行います。V NET,LOGON の根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で範囲照合のコマンドを確認した扱いにする。
    - B. IST097I の有無を確認せず範囲照合のコマンドを正常終了として記録する。
    - C. z/OS Communications Serverの表示形式に沿って根拠行を採り、範囲照合の点検結果を残す。 ✅
    - D. V NET,LOGON の属性行を読まず範囲照合のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合のコマンドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合のコマンドにおいて V NET,LOGON は説明欄の「z/OS Communications Serverで V NET,LOGON の扱いを記録する範囲照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のコマンドを受け取る担当者は、V NET,LOGON の表示結果と IST097I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のコマンドは別カテゴリの確認を流用しており、V NET,LOGON の根拠にならないため範囲照合ではありません。 B: 範囲照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のコマンドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のコマンドが示す V NET,LOGON は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,LOGON**

    - 検証目的: 比較判定のコマンドについて、V NET,LOGON は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、比較判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,LOGONを指定し、OSKB010094の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,LOGON
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,LOGON
    CASE OSKB010094
    SOURCE z/OS Communications Server
    ```

    V NET,LOGONとOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010094を同じ出力で読み、比較判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010094 V NET,LOGON
    ```

    IST097IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,LOGON と OSKB010094 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,RECYCLE {#c05-i0303}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,RECYCLEは、リソースを停止 により 活性化、Hot Standby 切替に利用。リソースを停止→活性化、Hot Standby 切替に利用

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 優先照合のコマンドに関する V NET,RECYCLE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず優先照合のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のコマンドの証跡として保存して根拠にする。
    - C. V NET,RECYCLE の変更点を出力本文から切り離して優先照合のコマンドの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合のコマンドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合のコマンドにおいて V NET,RECYCLE は説明欄の「V NET,RECYCLE の状態と出力メッセージを結び付ける優先照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のコマンドに関する記録は、V NET,RECYCLE の出力行と IST097I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため優先照合ではありません。 B: 優先照合のコマンドは別カテゴリの確認を流用しており、V NET,RECYCLE の根拠にならないため優先照合ではありません。 C: 優先照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のコマンドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のコマンドで記録する V NET,RECYCLE はz/OS Communications Serverの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,RECYCLE**

    - 検証目的: 順序判定のコマンドについて、V NET,RECYCLE は、リソースを停止 により 活性化、Hot Standby 切替に利用。リソースを停止から活性化、Hot Standby 切替に利用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010095の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、順序判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,RECYCLEを指定し、OSKB010095の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,RECYCLE
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,RECYCLE
    CASE OSKB010095
    SOURCE z/OS Communications Server
    ```

    V NET,RECYCLEとOSKB010095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010095を同じ出力で読み、順序判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010095 V NET,RECYCLE
    ```

    IST097IとOSKB010095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,RECYCLE と OSKB010095 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,RELEASE {#c05-i0304}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,RELEASEは、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 記録照合のコマンドに関係する V NET,RELEASE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録照合の確認値として扱う。 ✅
    - B. V NET,RELEASE の名称と担当者名のみを残して記録照合のコマンドの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で記録照合のコマンドを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず記録照合のコマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合のコマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合のコマンドにおいて V NET,RELEASE は説明欄の「V NET,RELEASE の用途を通信サーバーの表示で確認する記録照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のコマンドに関連して、z/OS Communications Serverでは V NET,RELEASE の表示属性と IST097I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のコマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のコマンドは別カテゴリの確認を流用しており、V NET,RELEASE の根拠にならないため記録照合ではありません。 D: 記録照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため記録照合ではありません。記録照合のコマンドで使う V NET,RELEASE という用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は記録照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,RELEASE**

    - 検証目的: 値域判定のコマンドについて、V NET,RELEASE は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010096の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、値域判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,RELEASEを指定し、OSKB010096の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,RELEASE
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,RELEASE
    CASE OSKB010096
    SOURCE z/OS Communications Server
    ```

    V NET,RELEASEとOSKB010096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010096を同じ出力で読み、値域判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010096 V NET,RELEASE
    ```

    IST097IとOSKB010096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,RELEASE と OSKB010096 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### V NET,TERM,LU1=,LU2= {#c05-i0305}
*分類: VTAM V NET コマンド*  ・  難易度: 上級

V NET,TERM,LU1=,LU2=は、Comm Server / VTAM / TCP/IPのVTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 区切照合のコマンドで V NET,TERM,LU1=,LU2= の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V NET,TERM,LU1=,LU2= の出力を取らず区切照合のコマンドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切照合の確認にする。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して区切照合のコマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のコマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合のコマンドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のコマンドにおいて V NET,TERM,LU1=,LU2= は説明欄の「区切照合のコマンドに関係する定義値と表示行を照合する区切照合項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のコマンドの証跡を読む担当者は、V NET,TERM,LU1=,LU2= の属性行と IST097I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のコマンドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のコマンドは戻り値や記録番号に寄り、IST097I や属性表示を落とすため区切照合ではありません。 D: 区切照合のコマンドは別カテゴリの確認を流用しており、V NET,TERM,LU1=,LU2= の根拠にならないため区切照合ではありません。区切照合のコマンドに出る V NET,TERM,LU1=,LU2= は Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **V NET,TERM,LU1=,LU2=**

    - 検証目的: 記録判定のコマンドについて、V NET,TERM,LU1=,LU2= は、Comm Server / VTAM / TCP/IP の VTAM V NET コマンドで状態表示や操作を行うためのコマンド関連項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010093の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、記録判定のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV NET,TERM,LU1=,LUを指定し、OSKB010093の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V NET,TERM,LU1=,LU
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V NET,TERM,LU1=,LU
    CASE OSKB010093
    SOURCE z/OS Communications Server
    ```

    V NET,TERM,LU1=,LUとOSKB010093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010093を同じ出力で読み、記録判定のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010093 V NET,TERM,LU1=,LU2=
    ```

    IST097IとOSKB010093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の V NET,TERM,LU1=,LU と OSKB010093 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > VTAM トレース

### BUFFER トレース {#c05-i0306}
*分類: VTAM トレース*  ・  難易度: 上級

BUFFER トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 展開追跡のトレースで BUFFER トレースの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BUFFER トレースの出力を取らず展開追跡のトレースの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開追跡の確認にする。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して展開追跡のトレースの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のトレースへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡のトレースにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のトレースにおいて BUFFER トレース は説明欄の「展開追跡のトレースに関係する定義値と表示行を照合する展開追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のトレースの証跡を読む担当者は、BUFFER トレースの属性行と IST097I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のトレースは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のトレースは別カテゴリの確認を流用しており、BUFFER トレースの根拠にならないため展開追跡ではありません。展開追跡のトレースに出る BUFFER トレースは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **BUFFER トレース**

    - 検証目的: 終端整理のトレースについて、BUFFER トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010105の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、終端整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にBUFFER トレースを指定し、OSKB010105の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND BUFFER トレース
    CASE OSKB010105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM BUFFER トレース
    CASE OSKB010105
    SOURCE z/OS Communications Server
    ```

    BUFFER トレースとOSKB010105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010105を同じ出力で読み、終端整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010105
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010105 BUFFER トレース
    ```

    IST097IとOSKB010105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の BUFFER トレース と OSKB010105 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### GPT トレース {#c05-i0307}
*分類: VTAM トレース*  ・  難易度: 上級

GPT トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 呼出追跡のトレースで通信サーバーの運用確認を行います。GPT トレースの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で呼出追跡のトレースを確認した扱いにする。
    - B. IST097I の有無を確認せず呼出追跡のトレースを正常終了として記録する。
    - C. z/OS Communications Serverの表示形式に沿って根拠行を採り、呼出追跡の点検結果を残す。 ✅
    - D. GPT トレースの属性行を読まず呼出追跡のトレースの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡のトレースにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のトレースにおいて GPT トレース は説明欄の「z/OS Communications Serverで GPT トレースの扱いを記録する呼出追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のトレースを受け取る担当者は、GPT トレースの表示結果と IST097I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のトレースは別カテゴリの確認を流用しており、GPT トレースの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のトレースは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のトレースが示す GPT トレースは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **GPT トレース**

    - 検証目的: 探索整理のトレースについて、GPT トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010106の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、探索整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にGPT トレースを指定し、OSKB010106の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND GPT トレース
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM GPT トレース
    CASE OSKB010106
    SOURCE z/OS Communications Server
    ```

    GPT トレースとOSKB010106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010106を同じ出力で読み、探索整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010106 GPT トレース
    ```

    IST097IとOSKB010106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の GPT トレース と OSKB010106 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### IO トレース {#c05-i0308}
*分類: VTAM トレース*  ・  難易度: 上級

IO トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 探索追跡のトレースで IO トレースの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IO トレースの出力を取らず探索追跡のトレースの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索追跡の根拠を固定する。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して探索追跡のトレースの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のトレースへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡のトレースにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡のトレースにおいて IO トレース は説明欄の「探索追跡のトレースに関係する定義値と表示行を照合する探索追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のトレースの証跡を読む担当者は、IO トレースの属性行と IST097I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のトレースは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のトレースは別カテゴリの確認を流用しており、IO トレースの根拠にならないため探索追跡ではありません。探索追跡のトレースに出る IO トレースは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **IO トレース**

    - 検証目的: 条件整理のトレースについて、IO トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010109の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、条件整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIO トレースを指定し、OSKB010109の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IO トレース
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IO トレース
    CASE OSKB010109
    SOURCE z/OS Communications Server
    ```

    IO トレースとOSKB010109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010109を同じ出力で読み、条件整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010109 IO トレース
    ```

    IST097IとOSKB010109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の IO トレース と OSKB010109 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### MODULE トレース {#c05-i0309}
*分類: VTAM トレース*  ・  難易度: 上級

MODULE トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **MODULE トレース**

    - 検証目的: 比較整理のトレースについて、MODULE トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010114の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、比較整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMODULE トレースを指定し、OSKB010114の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MODULE トレース
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MODULE トレース
    CASE OSKB010114
    SOURCE z/OS Communications Server
    ```

    MODULE トレースとOSKB010114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010114を同じ出力で読み、比較整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010114 MODULE トレース
    ```

    IST097IとOSKB010114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の MODULE トレース と OSKB010114 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### PIU トレース {#c05-i0310}
*分類: VTAM トレース*  ・  難易度: 上級

PIU トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 置換追跡のトレースに関する PIU トレースの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず置換追跡のトレースの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のトレースの証跡として保存して根拠にする。
    - C. PIU トレースの変更点を出力本文から切り離して置換追跡のトレースの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換追跡で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡のトレースにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のトレースにおいて PIU トレース は説明欄の「PIU トレースの状態と出力メッセージを結び付ける置換追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のトレースに関する記録は、PIU トレースの出力行と IST097I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のトレースは別カテゴリの確認を流用しており、PIU トレースの根拠にならないため置換追跡ではありません。 C: 置換追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のトレースは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のトレースで記録する PIU トレースはz/OS Communications Serverの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **PIU トレース**

    - 検証目的: 上書整理のトレースについて、PIU トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010107の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、上書整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPIU トレースを指定し、OSKB010107の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PIU トレース
    CASE OSKB010107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PIU トレース
    CASE OSKB010107
    SOURCE z/OS Communications Server
    ```

    PIU トレースとOSKB010107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010107を同じ出力で読み、上書整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010107
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010107 PIU トレース
    ```

    IST097IとOSKB010107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の PIU トレース と OSKB010107 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### SIO トレース {#c05-i0311}
*分類: VTAM トレース*  ・  難易度: 上級

SIO トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 条件追跡のトレースに関係する SIO トレースの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件追跡の確認記録にまとめる。 ✅
    - B. SIO トレースの名称と担当者名のみを残して条件追跡のトレースの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で条件追跡のトレースを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず条件追跡のトレースの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡のトレースにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡のトレースにおいて SIO トレース は説明欄の「SIO トレースの用途を通信サーバーの表示で確認する条件追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡のトレースに関連して、z/OS Communications Serverでは SIO トレースの表示属性と IST097I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡のトレースは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡のトレースは別カテゴリの確認を流用しており、SIO トレースの根拠にならないため条件追跡ではありません。 D: 条件追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため条件追跡ではありません。条件追跡のトレースで使う SIO トレースという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は条件追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **SIO トレース**

    - 検証目的: 優先整理のトレースについて、SIO トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010112の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、優先整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIO トレースを指定し、OSKB010112の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIO トレース
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIO トレース
    CASE OSKB010112
    SOURCE z/OS Communications Server
    ```

    SIO トレースとOSKB010112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010112を同じ出力で読み、優先整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010112 SIO トレース
    ```

    IST097IとOSKB010112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の SIO トレース と OSKB010112 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### SMS トレース {#c05-i0312}
*分類: VTAM トレース*  ・  難易度: 上級

SMS トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 出力追跡のトレースに関する SMS トレースの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D NET,ID=OSKBAPPL,E の結果を残さず出力追跡のトレースの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のトレースの証跡として保存して根拠にする。
    - C. SMS トレースの変更点を出力本文から切り離して出力追跡のトレースの承認欄のみ残す。
    - D. D NET,ID=OSKBAPPL,E の結果から対象行を抜き出し、出力追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡のトレースにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡のトレースにおいて SMS トレース は説明欄の「SMS トレースの状態と出力メッセージを結び付ける出力追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のトレースに関する記録は、SMS トレースの出力行と IST097I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のトレースは別カテゴリの確認を流用しており、SMS トレースの根拠にならないため出力追跡ではありません。 C: 出力追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のトレースは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のトレースで記録する SMS トレースはz/OS Communications Serverの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **SMS トレース**

    - 検証目的: 範囲整理のトレースについて、SMS トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010111の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、範囲整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSMS トレースを指定し、OSKB010111の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SMS トレース
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SMS トレース
    CASE OSKB010111
    SOURCE z/OS Communications Server
    ```

    SMS トレースとOSKB010111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010111を同じ出力で読み、範囲整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010111 SMS トレース
    ```

    IST097IとOSKB010111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の SMS トレース と OSKB010111 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### STATE トレース {#c05-i0313}
*分類: VTAM トレース*  ・  難易度: 上級

STATE トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 上書追跡のトレースで通信サーバーの運用確認を行います。STATE トレースの根拠にできる作業はどれですか。

    - A. z/OS Communications Serverと無関係な一覧で上書追跡のトレースを確認した扱いにする。
    - B. IST097I の有無を確認せず上書追跡のトレースを正常終了として記録する。
    - C. IST097I を含む表示を保存し、説明欄との差分を上書追跡で確認する。 ✅
    - D. STATE トレースの属性行を読まず上書追跡のトレースの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡のトレースにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のトレースにおいて STATE トレース は説明欄の「z/OS Communications Serverで STATE トレースの扱いを記録する上書追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のトレースを受け取る担当者は、STATE トレースの表示結果と IST097I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のトレースは別カテゴリの確認を流用しており、STATE トレースの根拠にならないため上書追跡ではありません。 B: 上書追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のトレースは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のトレースが示す STATE トレースは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **STATE トレース**

    - 検証目的: 区切整理のトレースについて、STATE トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010110の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、区切整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSTATE トレースを指定し、OSKB010110の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND STATE トレース
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM STATE トレース
    CASE OSKB010110
    SOURCE z/OS Communications Server
    ```

    STATE トレースとOSKB010110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010110を同じ出力で読み、区切整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010110 STATE トレース
    ```

    IST097IとOSKB010110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の STATE トレース と OSKB010110 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### TG トレース {#c05-i0314}
*分類: VTAM トレース*  ・  難易度: 上級

TG トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 終端追跡のトレースに関係する TG トレースの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端追跡の確認値として扱う。 ✅
    - B. TG トレースの名称と担当者名のみを残して終端追跡のトレースの表示本文を確認対象に含めない。
    - C. 通信サーバー以外の画面で終端追跡のトレースを確認し同じ証跡として扱ったことにする。
    - D. IST097I の有無を見ず終端追跡のトレースの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡のトレースにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡のトレースにおいて TG トレース は説明欄の「TG トレースの用途を通信サーバーの表示で確認する終端追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のトレースに関連して、z/OS Communications Serverでは TG トレースの表示属性と IST097I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のトレースは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のトレースは別カテゴリの確認を流用しており、TG トレースの根拠にならないため終端追跡ではありません。 D: 終端追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため終端追跡ではありません。終端追跡のトレースで使う TG トレースという用語は Comm Server / VTAM / TCP/IP で扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **TG トレース**

    - 検証目的: 出力整理のトレースについて、TG トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010108の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、出力整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTG トレースを指定し、OSKB010108の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TG トレース
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TG トレース
    CASE OSKB010108
    SOURCE z/OS Communications Server
    ```

    TG トレースとOSKB010108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010108を同じ出力で読み、出力整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010108 TG トレース
    ```

    IST097IとOSKB010108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の TG トレース と OSKB010108 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### TPM トレース {#c05-i0315}
*分類: VTAM トレース*  ・  難易度: 上級

TPM トレースは、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? question "確認問題（1問）"
    **問題.** 区切追跡のトレースで TPM トレースの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TPM トレースの出力を取らず区切追跡のトレースの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切追跡の根拠にする。 ✅
    - C. D NET,ID=OSKBAPPL,E を省略して区切追跡のトレースの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のトレースへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡のトレースにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡のトレースにおいて TPM トレース は説明欄の「区切追跡のトレースに関係する定義値と表示行を照合する区切追跡項目」と D NET,ID=OSKBAPPL,E または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡のトレースの証跡を読む担当者は、TPM トレースの属性行と IST097I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡のトレースは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡のトレースは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡のトレースは戻り値や記録番号に寄り、IST097I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡のトレースは別カテゴリの確認を流用しており、TPM トレースの根拠にならないため区切追跡ではありません。区切追跡のトレースに出る TPM トレースは Comm Server / VTAM / TCP/IP の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** zOS31_ipcom / OS MVS System Commands（zOS31_ieag100） / zOS31_ieam300


??? note "検証手順（1件）"
    **TPM トレース**

    - 検証目的: 記録整理のトレースについて、TPM トレースは、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010113の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、記録整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTPM トレースを指定し、OSKB010113の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TPM トレース
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TPM トレース
    CASE OSKB010113
    SOURCE z/OS Communications Server
    ```

    TPM トレースとOSKB010113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010113を同じ出力で読み、記録整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010113 TPM トレース
    ```

    IST097IとOSKB010113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の TPM トレース と OSKB010113 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### VIT (Internal Trace) {#c05-i0316}
*分類: VTAM トレース*  ・  難易度: 上級

VIT (Internal Trace)は、VTAM Internal Trace、メモリ常駐記録、SMP/E PTF レベル不要で常時 ON 推奨

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **VIT (Internal Trace)**

    - 検証目的: 順序整理のトレースについて、VIT (Internal Trace)は、VTAM Internal Trace、メモリ常駐記録、SMP/E PTF レベル不要で常時 ON 推奨に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010115の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、順序整理のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にVIT (Internal Tracを指定し、OSKB010115の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND VIT (Internal Trac
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM VIT (Internal Trac
    CASE OSKB010115
    SOURCE z/OS Communications Server
    ```

    VIT (Internal TracとOSKB010115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010115を同じ出力で読み、順序整理のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010115 VIT (Internal Trace)
    ```

    IST097IとOSKB010115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の VIT (Internal Trac と OSKB010115 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### VIT サイズ指定 {#c05-i0317}
*分類: VTAM トレース*  ・  難易度: 上級

VIT サイズ指定は、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **VIT サイズ指定**

    - 検証目的: 値域整理のサイズ指定について、VIT サイズ指定は、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010116の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、値域整理のサイズ指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にVIT サイズ指定を指定し、OSKB010116の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND VIT サイズ指定
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM VIT サイズ指定
    CASE OSKB010116
    SOURCE z/OS Communications Server
    ```

    VIT サイズ指定とOSKB010116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010116を同じ出力で読み、値域整理のサイズ指定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010116 VIT サイズ指定
    ```

    IST097IとOSKB010116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の VIT サイズ指定 と OSKB010116 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### トレース出力先 {#c05-i0318}
*分類: VTAM トレース*  ・  難易度: 上級

トレース出力先は、Comm Server / VTAM / TCP/IPのVTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **トレース出力先**

    - 検証目的: 警告整理のトレース出力先について、トレース出力先は、Comm Server / VTAM / TCP/IP の VTAM トレースで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010117の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、警告整理のトレース出力先の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にトレース出力先を指定し、OSKB010117の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND トレース出力先
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM トレース出力先
    CASE OSKB010117
    SOURCE z/OS Communications Server
    ```

    トレース出力先とOSKB010117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB010117を同じ出力で読み、警告整理のトレース出力先の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB010117 トレース出力先
    ```

    IST097IとOSKB010117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の トレース出力先 と OSKB010117 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB010117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference




## Comm Server / VTAM / TCP/IP > z/OS SNMP

### SNMP サーバ位置付け {#c05-i0319}
*分類: z/OS SNMP*  ・  難易度: 上級

SNMP サーバ位置付けは、Comm Server / VTAM / TCP/IPのz/OS SNMPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **SNMP サーバ位置付け**

    - 検証目的: 構文追跡のサーバ位置付けについて、SNMP サーバ位置付けは、Comm Server / VTAM / TCP/IP のz/OS SNMP で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030041の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、構文追跡のサーバ位置付けの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSNMP サーバ位置付けを指定し、OSKB030041の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SNMP サーバ位置付け
    CASE OSKB030041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SNMP サーバ位置付け
    CASE OSKB030041
    SOURCE z/OS Communications Server
    ```

    SNMP サーバ位置付けとOSKB030041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB030041を同じ出力で読み、構文追跡のサーバ位置付けの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB030041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB030041 SNMP サーバ位置付け
    ```

    IST097IとOSKB030041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の SNMP サーバ位置付け と OSKB030041 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB030041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### SNMPD.CONF {#c05-i0320}
*分類: z/OS SNMP*  ・  難易度: 上級

SNMPD.CONFは、Comm Server / VTAM / TCP/IPのz/OS SNMPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **SNMPD.CONF**

    - 検証目的: 展開追跡の通信サーバーについて、SNMPD.CONF は、Comm Server / VTAM / TCP/IP のz/OS SNMP で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030042の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、展開追跡の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSNMPD.CONFを指定し、OSKB030042の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SNMPD.CONF
    CASE OSKB030042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SNMPD.CONF
    CASE OSKB030042
    SOURCE z/OS Communications Server
    ```

    SNMPD.CONFとOSKB030042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB030042を同じ出力で読み、展開追跡の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB030042
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB030042 SNMPD.CONF
    ```

    IST097IとOSKB030042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の SNMPD.CONF と OSKB030042 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB030042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### snmp コマンド (USS) {#c05-i0321}
*分類: z/OS SNMP*  ・  難易度: 上級

snmp コマンド (USS)は、Comm Server / VTAM / TCP/IPのz/OS SNMPで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **snmp コマンド (USS)**

    - 検証目的: 置換追跡のコマンドについて、snmp コマンド (USS)は、Comm Server / VTAM / TCP/IP のz/OS SNMP で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030044の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、置換追跡のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にsnmp コマンド (USS)を指定し、OSKB030044の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND snmp コマンド (USS)
    CASE OSKB030044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM snmp コマンド (USS)
    CASE OSKB030044
    SOURCE z/OS Communications Server
    ```

    snmp コマンド (USS)とOSKB030044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB030044を同じ出力で読み、置換追跡のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB030044
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB030044 snmp コマンド (USS)
    ```

    IST097IとOSKB030044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の snmp コマンド (USS) と OSKB030044 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB030044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference



### subagent (DPI) {#c05-i0322}
*分類: z/OS SNMP*  ・  難易度: 上級

subagent (DPI)は、Comm Server / VTAM / TCP/IPのz/OS SNMPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS Communications Server SNA Operation、z/OS Communications Server IP Configuration Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference

??? note "検証手順（1件）"
    **subagent (DPI)**

    - 検証目的: 呼出追跡の通信サーバーについて、subagent (DPI)は、Comm Server / VTAM / TCP/IP のz/OS SNMP で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030043の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD NET,ID=OSKBAPPL,Eを実行し、IST097Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D NET,ID=OSKBAPPL,E を入力し、呼出追跡の通信サーバーの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    ```

    COMMAND INPUTにD NET,ID=OSKBAPPL,Eが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にsubagent (DPI)を指定し、OSKB030043の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND subagent (DPI)
    CASE OSKB030043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM subagent (DPI)
    CASE OSKB030043
    SOURCE z/OS Communications Server
    ```

    subagent (DPI)とOSKB030043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IST097IとOSKB030043を同じ出力で読み、呼出追跡の通信サーバーの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D NET,ID=OSKBAPPL,E
    CASE OSKB030043
    → Enter を押す
    ```

    画面・出力:
    ```text
    IST097I TCP/IP NETSTAT CS V2R5
    CONN  LOCAL SOCKET           FOREIGN SOCKET         STATE
    0001  192.0.2.1..443         198.51.100.1..52000    ESTABLISHED
    OSKB030043 subagent (DPI)
    ```

    IST097IとOSKB030043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D NET,ID=OSKBAPPL,E が画面・出力に表示されること
    ② ステップ2 の subagent (DPI) と OSKB030043 が画面・出力に表示されること
    ③ ステップ3 の IST097I と OSKB030043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Communications Server SNA Operation、z / OS Communications Server IP Configuration Reference


