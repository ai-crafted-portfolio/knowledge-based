---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (4/4)

[← MVS オペレータコマンド の概要へ戻る](index.md)


## MVS オペレータコマンド > V TCPIP

### V TCPIP,,OBEY,dsn {#c22-i0289}
*分類: V TCPIP*  ・  難易度: 上級

V TCPIP,,OBEY,dsnは、MVS オペレータコマンドのV TCPIPで確認する項目です。TCP/IP の動的構成変更 (OBEYFILE) 指示。プロファイル PROFILE.TCPIP を OBEY 形式で取り込む

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 記録照合の操作コマンドに関係する V TCPIP,,OBEY,dsnの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 ✅
    - B. V TCPIP,,OBEY,dsnの名称と担当者名のみを残して記録照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず記録照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合の操作コマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の操作コマンドにおいて V TCPIP,,OBEY,dsn は説明欄の「V TCPIP,,OBEY,dsnの用途を操作コマンドの表示で確認する記録照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の操作コマンドに関連して、z/OS MVS Operationsでは V TCPIP,,OBEY,dsnの表示属性と IEE115I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の操作コマンドは別カテゴリの確認を流用しており、V TCPIP,,OBEY,dsnの根拠にならないため記録照合ではありません。 D: 記録照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録照合ではありません。記録照合の操作コマンドで使う V TCPIP,,OBEY,dsnという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V TCPIP,,OBEY,dsn**

    - 検証目的: 探索確認の操作コマンドについて、V TCPIP,,OBEY,dsnは、MVS オペレータコマンドの V TCPIP で確認する項目です。TCP/IP の動的構成変更 (OBEYFILE) 指示。プロファイルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030006の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、探索確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,OBEY,dsnを指定し、OSKB030006の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V TCPIP,,OBEY,dsn
    CASE OSKB030006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V TCPIP,,OBEY,dsn
    CASE OSKB030006
    SOURCE z/OS MVS Operations
    ```

    V TCPIP,,OBEY,dsnとOSKB030006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030006を同じ出力で読み、探索確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030006
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030006 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030006   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V TCPIP,,OBEY,dsn と OSKB030006 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V TCPIP,,SYNTAXCHECK,dsn {#c22-i0290}
*分類: V TCPIP*  ・  難易度: 上級

V TCPIP,,SYNTAXCHECK,dsnは、OBEYFILE の構文検査のみを実行し、活性化はしないドライラン形式

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 比較照合の操作コマンドで V TCPIP,,SYNTAXCHECK,dsnの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V TCPIP,,SYNTAXCHECK,dsnの出力を取らず比較照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 ✅
    - C. D A,L を省略して比較照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合の操作コマンドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合の操作コマンドにおいて V TCPIP,,SYNTAXCHECK,dsn は説明欄の「比較照合の操作コマンドに関係する定義値と表示行を照合する比較照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の操作コマンドの証跡を読む担当者は、V TCPIP,,SYNTAXCHECK,dsnの属性行と IEE115I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較照合ではありません。 D: 比較照合の操作コマンドは別カテゴリの確認を流用しており、V TCPIP,,SYNTAXCHECK,dsnの根拠にならないため比較照合ではありません。比較照合の操作コマンドに出る V TCPIP,,SYNTAXCHECK,dsnは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V TCPIP,,SYNTAXCHECK,dsn**

    - 検証目的: 上書確認の操作コマンドについて、V TCPIP,,SYNTAXCHECK,dsnは、OBEYFILE の構文検査のみを実行し、活性化はしないドライラン形式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030007の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,SYNTAXCHEを指定し、OSKB030007の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V TCPIP,,SYNTAXCHE
    CASE OSKB030007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V TCPIP,,SYNTAXCHE
    CASE OSKB030007
    SOURCE z/OS MVS Operations
    ```

    V TCPIP,,SYNTAXCHEとOSKB030007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030007を同じ出力で読み、上書確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030007
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030007 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030007   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V TCPIP,,SYNTAXCHE と OSKB030007 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V TCPIP,,VARY,nnnn,... {#c22-i0291}
*分類: V TCPIP*  ・  難易度: 上級

V TCPIP,,VARY,nnnn,...は、MVS オペレータコマンドのV TCPIPで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序照合のなどで操作コマンドの運用確認を行います。V TCPIP,,VARY,nnnn,などの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序照合のなどを確認した扱いにする。
    - B. IEE457I の有無を確認せず順序照合のなどを正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序照合の記録として扱う。 ✅
    - D. V TCPIP,,VARY,nnnn,などの属性行を読まず順序照合のなどの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合のなどにおいて選択記号 C を採用し、識別名は順序照合です。順序照合のなどにおいて V TCPIP,,VARY,nnnn,など は説明欄の「z/OS MVS Operationsで V TCPIP,,VARY,nnnn,などの扱いを記録する順序照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のなどを受け取る担当者は、V TCPIP,,VARY,nnnn,などの表示結果と IEE457I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のなどは別カテゴリの確認を流用しており、V TCPIP,,VARY,nnnn,などの根拠にならないため順序照合ではありません。 B: 順序照合のなどは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため順序照合ではありません。 C: 順序照合のなどは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のなどが示す V TCPIP,,VARY,nnnn,などは出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200




## MVS オペレータコマンド > V WLM

### V WLM,APPLENV=name,QUIESCE {#c22-i0292}
*分類: V WLM*  ・  難易度: 上級

V WLM,APPLENV=name,QUIESCEは、MVS オペレータコマンドのV WLMで確認する項目です。WLM アプリケーション環境を停止状態 (QUIESCE) にする。サーバ・アドレス・スペースは整理される

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 構文追跡再の操作コマンドに関係する V WLM 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文追跡再として引き継ぐ。 ✅
    - B. V WLM 命令の名称と担当者名だけを残して構文追跡再の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文追跡再の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡再正解では選択記号 A を採用し、正解名は構文追跡再正解です。構文追跡再根拠では V WLM 命令 は「V WLM 命令の用途を操作コマンドの表示で確認する構文追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は構文追跡再根拠です。構文追跡再背景ではz/OS MVS Operationsの V WLM 命令と IEE115I を同じ証跡に残し、背景名は構文追跡再背景です。他の選択肢を確認します。 A: 構文追跡再正答は対象出力と項目説明を結び、根拠名は構文追跡再正答です。 B: 構文追跡再不足は名称や説明だけに寄り、判定名は構文追跡再不足です。 C: 構文追跡再流用は別カテゴリの確認であり、排除名は構文追跡再流用です。 D: 構文追跡再欠落は戻り値や記録番号に寄り、欠落名は構文追跡再欠落です。構文追跡再用語では V WLM 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文追跡再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 呼出照合の操作コマンドで操作コマンドの運用確認を行います。V WLM,APPLENV=name,QUIES の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出照合の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 ✅
    - D. V WLM,APPLENV=name,QUIES の属性行を読まず呼出照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合の操作コマンドにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合の操作コマンドにおいて V WLM,APPLENV=name,QUIES は説明欄の「z/OS MVS Operationsで V WLM,APPLENV=name,QUIES の扱いを記録する呼出照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の操作コマンドを受け取る担当者は、V WLM,APPLENV=name,QUIES の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,APPLENV=name,QUIES の根拠にならないため呼出照合ではありません。 B: 呼出照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の操作コマンドが示す V WLM,APPLENV=name,QUIES は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **V WLM,APPLENV=name,QUIESCE**

    - 検証目的: 構文追跡の操作コマンドについて、V WLM,APPLENV=name,QUIESCE は、MVS オペレータコマンドの V WLM で確認する項目です。WLM アプリケーション環境を停止状態 (QUIESCE)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040041の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,APPLENV=nameを指定し、OSKB040041の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V WLM,APPLENV=name
    CASE OSKB040041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V WLM,APPLENV=name
    CASE OSKB040041
    SOURCE z/OS MVS Operations
    ```

    V WLM,APPLENV=nameとOSKB040041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040041を同じ出力で読み、構文追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040041 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040041   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V WLM,APPLENV=name と OSKB040041 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **V WLM,APPLENV=name,QUIESCE**

    - 検証目的: 値域整理の操作コマンドについて、V WLM,APPLENV=name,QUIESCE は、MVS オペレータコマンドの V WLM で確認する項目です。WLM アプリケーション環境を停止状態 (QUIESCE)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,APPLENV=nameを指定し、OSKB020116の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V WLM,APPLENV=name
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V WLM,APPLENV=name
    CASE OSKB020116
    SOURCE z/OS MVS Operations
    ```

    V WLM,APPLENV=nameとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020116を同じ出力で読み、値域整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020116 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020116   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V WLM,APPLENV=name と OSKB020116 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V WLM,APPLENV=name,RESUME {#c22-i0293}
*分類: V WLM*  ・  難易度: 上級

V WLM,APPLENV=name,RESUMEは、MVS オペレータコマンドのV WLMで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 変更照合再の操作コマンドに関する V WLM 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更照合再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更照合再の操作コマンドの証跡として保存して根拠にする。
    - C. V WLM 命令の変更点を出力本文から切り離して変更照合再の操作コマンドの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、変更照合再の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合再正解では選択記号 D を採用し、正解名は変更照合再正解です。変更照合再根拠では V WLM 命令 は「V WLM 命令の状態と出力メッセージを結び付ける変更照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は変更照合再根拠です。変更照合再保存では V WLM 命令の出力行と IEE115I を一緒に残し、保存名は変更照合再保存です。選択肢ごとの違いを示します。 A: 変更照合再欠落は戻り値や記録番号に寄り、欠落名は変更照合再欠落です。 B: 変更照合再流用は別カテゴリの確認であり、排除名は変更照合再流用です。 C: 変更照合再不足は名称や説明だけに寄り、判定名は変更照合再不足です。 D: 変更照合再正答は対象出力と項目説明を結び、根拠名は変更照合再正答です。変更照合再対象では V WLM 命令をz/OS MVS Operationsの確認記録に残し、対象名は変更照合再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 展開照合の操作コマンドで V WLM,APPLENV=name,RESUM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V WLM,APPLENV=name,RESUM の出力を取らず展開照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 ✅
    - C. D A,L を省略して展開照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合の操作コマンドにおいて選択記号 B を採用し、識別名は展開照合です。展開照合の操作コマンドにおいて V WLM,APPLENV=name,RESUM は説明欄の「展開照合の操作コマンドに関係する定義値と表示行を照合する展開照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の操作コマンドの証跡を読む担当者は、V WLM,APPLENV=name,RESUM の属性行と IEE115I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開照合ではありません。 D: 展開照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,APPLENV=name,RESUM の根拠にならないため展開照合ではありません。展開照合の操作コマンドに出る V WLM,APPLENV=name,RESUM は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V WLM,APPLENV=name,RESUME**

    - 検証目的: 順序整理の操作コマンドについて、V WLM,APPLENV=name,RESUME は、MVS オペレータコマンドの V WLM で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,APPLENV=nameを指定し、OSKB020115の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V WLM,APPLENV=name
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V WLM,APPLENV=name
    CASE OSKB020115
    SOURCE z/OS MVS Operations
    ```

    V WLM,APPLENV=nameとOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020115を同じ出力で読み、順序整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020115 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020115   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V WLM,APPLENV=name と OSKB020115 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V WLM,POLICY=name {#c22-i0294}
*分類: V WLM*  ・  難易度: 上級

V WLM,POLICY=nameは、MVS オペレータコマンドのV WLMで確認する項目です。WLM サービス・ポリシーを動的に切り替える。日中/夜間プロファイル切替の典型

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 監査照合再の操作コマンドで操作コマンドの運用確認を行います。V WLM 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査照合再の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査照合再の操作コマンドを正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、監査照合再の結果として保存する。 ✅
    - D. V WLM 命令の属性行を読まず監査照合再の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合再正解では選択記号 C を採用し、正解名は監査照合再正解です。監査照合再根拠では V WLM 命令 は「z/OS MVS Operationsで V WLM 命令の扱いを記録する監査照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は監査照合再根拠です。監査照合再受渡では V WLM 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査照合再受渡です。不適切な選択肢を整理します。 A: 監査照合再流用は別カテゴリの確認であり、排除名は監査照合再流用です。 B: 監査照合再欠落は戻り値や記録番号に寄り、欠落名は監査照合再欠落です。 C: 監査照合再正答は対象出力と項目説明を結び、根拠名は監査照合再正答です。 D: 監査照合再不足は名称や説明だけに寄り、判定名は監査照合再不足です。監査照合再資料では V WLM 命令の使い方を出典欄から追跡し、資料名は監査照合再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 構文照合の操作コマンドに関係する V WLM,POLICY=nameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 ✅
    - B. V WLM,POLICY=nameの名称と担当者名のみを残して構文照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で構文照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合の操作コマンドにおいて選択記号 A を採用し、識別名は構文照合です。構文照合の操作コマンドにおいて V WLM,POLICY=name は説明欄の「V WLM,POLICY=nameの用途を操作コマンドの表示で確認する構文照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の操作コマンドに関連して、z/OS MVS Operationsでは V WLM,POLICY=nameの表示属性と IEE115I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,POLICY=nameの根拠にならないため構文照合ではありません。 D: 構文照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文照合ではありません。構文照合の操作コマンドで使う V WLM,POLICY=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V WLM,POLICY=name**

    - 検証目的: 比較整理の操作コマンドについて、V WLM,POLICY=nameは、MVS オペレータコマンドの V WLM で確認する項目です。WLM サービス・ポリシーを動的に切り替える。日中/夜間プロファイル切替の典に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,POLICY=nameを指定し、OSKB020114の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V WLM,POLICY=name
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V WLM,POLICY=name
    CASE OSKB020114
    SOURCE z/OS MVS Operations
    ```

    V WLM,POLICY=nameとOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020114を同じ出力で読み、比較整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020114 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020114   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V WLM,POLICY=name と OSKB020114 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V WLM,SCHENV=name,OFF {#c22-i0295}
*分類: V WLM*  ・  難易度: 上級

V WLM,SCHENV=name,OFFは、スケジューリング環境をオフにし、新規ジョブの実行を抑止する (Quiesce)

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 呼出追跡再の操作コマンドで操作コマンドの運用確認を行います。V WLM 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出追跡再の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出追跡再の操作コマンドを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出追跡再の点検結果を残す。 ✅
    - D. V WLM 命令の属性行を読まず呼出追跡再の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡再正解では選択記号 C を採用し、正解名は呼出追跡再正解です。呼出追跡再根拠では V WLM 命令 は「z/OS MVS Operationsで V WLM 命令の扱いを記録する呼出追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出追跡再根拠です。呼出追跡再受渡では V WLM 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出追跡再受渡です。不適切な選択肢を整理します。 A: 呼出追跡再流用は別カテゴリの確認であり、排除名は呼出追跡再流用です。 B: 呼出追跡再欠落は戻り値や記録番号に寄り、欠落名は呼出追跡再欠落です。 C: 呼出追跡再正答は対象出力と項目説明を結び、根拠名は呼出追跡再正答です。 D: 呼出追跡再不足は名称や説明だけに寄り、判定名は呼出追跡再不足です。呼出追跡再資料では V WLM 命令の使い方を出典欄から追跡し、資料名は呼出追跡再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 終端照合の操作コマンドに関係する V WLM,SCHENV=name,OFF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 ✅
    - B. V WLM,SCHENV=name,OFF の名称と担当者名のみを残して終端照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で終端照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合の操作コマンドにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の操作コマンドにおいて V WLM,SCHENV=name,OFF は説明欄の「V WLM,SCHENV=name,OFF の用途を操作コマンドの表示で確認する終端照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の操作コマンドに関連して、z/OS MVS Operationsでは V WLM,SCHENV=name,OFF の表示属性と IEE115I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,SCHENV=name,OFF の根拠にならないため終端照合ではありません。 D: 終端照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端照合ではありません。終端照合の操作コマンドで使う V WLM,SCHENV=name,OFF という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V WLM,SCHENV=name,OFF**

    - 検証目的: 復旧整理の操作コマンドについて、V WLM,SCHENV=name,OFF は、スケジューリング環境をオフにし、新規ジョブの実行を抑止する (Quiesce)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、復旧整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,SCHENV=name,を指定し、OSKB020118の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V WLM,SCHENV=name,
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V WLM,SCHENV=name,
    CASE OSKB020118
    SOURCE z/OS MVS Operations
    ```

    V WLM,SCHENV=name,とOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020118を同じ出力で読み、復旧整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020118 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020118   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V WLM,SCHENV=name, と OSKB020118 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V WLM,SCHENV=name,ON {#c22-i0296}
*分類: V WLM*  ・  難易度: 上級

V WLM,SCHENV=name,ONは、スケジューリング環境をオン状態 (リソース利用可能) にし、待機ジョブを実行可能化する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 展開追跡再の操作コマンドで V WLM 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V WLM 命令の出力を取らず展開追跡再の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開追跡再の確認にする。 ✅
    - C. D A,L を省略して展開追跡再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開追跡再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡再正解では選択記号 B を採用し、正解名は展開追跡再正解です。展開追跡再根拠では V WLM 命令 は「展開追跡再の操作コマンドに関係する定義値と表示行を照合する展開追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は展開追跡再根拠です。展開追跡再追跡では V WLM 命令の属性行と IEE115I を合わせ、追跡名は展開追跡再追跡です。誤答側の問題点を分けます。 A: 展開追跡再不足は名称や説明だけに寄り、判定名は展開追跡再不足です。 B: 展開追跡再正答は対象出力と項目説明を結び、根拠名は展開追跡再正答です。 C: 展開追跡再欠落は戻り値や記録番号に寄り、欠落名は展開追跡再欠落です。 D: 展開追跡再流用は別カテゴリの確認であり、排除名は展開追跡再流用です。展開追跡再初出では V WLM 命令を MVS オペレータコマンドの運用手順で確認し、初出名は展開追跡再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 置換照合の操作コマンドに関する V WLM,SCHENV=name,ON の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず置換照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の操作コマンドの証跡として保存して根拠にする。
    - C. V WLM,SCHENV=name,ON の変更点を出力本文から切り離して置換照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合の操作コマンドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合の操作コマンドにおいて V WLM,SCHENV=name,ON は説明欄の「V WLM,SCHENV=name,ON の状態と出力メッセージを結び付ける置換照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の操作コマンドに関する記録は、V WLM,SCHENV=name,ON の出力行と IEE115I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換照合ではありません。 B: 置換照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,SCHENV=name,ON の根拠にならないため置換照合ではありません。 C: 置換照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の操作コマンドで記録する V WLM,SCHENV=name,ON はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V WLM,SCHENV=name,ON**

    - 検証目的: 警告整理の操作コマンドについて、V WLM,SCHENV=name,ON は、スケジューリング環境をオン状態 (リソース利用可能) にし、待機ジョブを実行可能化するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、警告整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,SCHENV=name,を指定し、OSKB020117の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V WLM,SCHENV=name,
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V WLM,SCHENV=name,
    CASE OSKB020117
    SOURCE z/OS MVS Operations
    ```

    V WLM,SCHENV=name,とOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020117を同じ出力で読み、警告整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020117 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020117   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V WLM,SCHENV=name, と OSKB020117 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V XCF

### V XCF,sysname,OFFLINE {#c22-i0297}
*分類: V XCF*  ・  難易度: 中級

V XCF,sysname,OFFLINEは、MVS オペレータコマンドのV XCFで確認する項目です。Sysplex から指定システムを除外する。SYSGONE 状態へ遷移し、Couple DS の再構成が走る

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書追跡再の操作コマンドで操作コマンドの運用確認を行います。V XCF 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書追跡再の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず上書追跡再の操作コマンドを正常終了として記録する。
    - C. IEE115I を含む表示を保存し、説明欄との差分を上書追跡再で確認する。 ✅
    - D. V XCF 命令の属性行を読まず上書追跡再の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡再正解では選択記号 C を採用し、正解名は上書追跡再正解です。上書追跡再根拠では V XCF 命令 は「z/OS MVS Operationsで V XCF 命令の扱いを記録する上書追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は上書追跡再根拠です。上書追跡再受渡では V XCF 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書追跡再受渡です。不適切な選択肢を整理します。 A: 上書追跡再流用は別カテゴリの確認であり、排除名は上書追跡再流用です。 B: 上書追跡再欠落は戻り値や記録番号に寄り、欠落名は上書追跡再欠落です。 C: 上書追跡再正答は対象出力と項目説明を結び、根拠名は上書追跡再正答です。 D: 上書追跡再不足は名称や説明だけに寄り、判定名は上書追跡再不足です。上書追跡再資料では V XCF 命令の使い方を出典欄から追跡し、資料名は上書追跡再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件照合の操作コマンドに関係する V XCF,sysname,OFFLINE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. V XCF,sysname,OFFLINE の名称と担当者名のみを残して条件照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合の操作コマンドにおいて選択記号 A を採用し、識別名は条件照合です。条件照合の操作コマンドにおいて V XCF,sysname,OFFLINE は説明欄の「V XCF,sysname,OFFLINE の用途を操作コマンドの表示で確認する条件照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の操作コマンドに関連して、z/OS MVS Operationsでは V XCF,sysname,OFFLINE の表示属性と IEE115I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の操作コマンドは別カテゴリの確認を流用しており、V XCF,sysname,OFFLINE の根拠にならないため条件照合ではありません。 D: 条件照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件照合ではありません。条件照合の操作コマンドで使う V XCF,sysname,OFFLINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **V XCF,sysname,OFFLINE**

    - 検証目的: 展開追跡の操作コマンドについて、V XCF,sysname,OFFLINE は、MVS オペレータコマンドの V XCF で確認する項目です。Sysplex から指定システムを除外する。SYSGONE 状態へ遷に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040042の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV XCF,sysname,OFFLを指定し、OSKB040042の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V XCF,sysname,OFFL
    CASE OSKB040042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V XCF,sysname,OFFL
    CASE OSKB040042
    SOURCE z/OS MVS Operations
    ```

    V XCF,sysname,OFFLとOSKB040042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040042を同じ出力で読み、展開追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040042
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040042 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040042   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V XCF,sysname,OFFL と OSKB040042 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **V XCF,sysname,OFFLINE**

    - 検証目的: 展開確認の操作コマンドについて、V XCF,sysname,OFFLINE は、MVS オペレータコマンドの V XCF で確認する項目です。Sysplex から指定システムを除外する。SYSGONE 状態へ遷に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030002の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV XCF,sysname,OFFLを指定し、OSKB030002の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V XCF,sysname,OFFL
    CASE OSKB030002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V XCF,sysname,OFFL
    CASE OSKB030002
    SOURCE z/OS MVS Operations
    ```

    V XCF,sysname,OFFLとOSKB030002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030002を同じ出力で読み、展開確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030002
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030002 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030002   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V XCF,sysname,OFFL と OSKB030002 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V dev

### V (devnum1,devnum2,...) 複数指定 {#c22-i0298}
*分類: V dev*  ・  難易度: 中級

V (devnum1,devnum2,...) 複数指定は、MVS オペレータコマンドのV devで確認する項目です。複数装置を 1 コマンドで同時に状態変更する形式。範囲指定はカッコ内のリストで行う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序確認のなど 複で操作コマンドの運用確認を行います。V (devnum1,devnum2,など) 複の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序確認のなど 複を確認した扱いにする。
    - B. IEE115I の有無を確認せず順序確認のなど 複を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序確認の記録として扱う。 ✅
    - D. V (devnum1,devnum2,など) 複の属性行を読まず順序確認のなど 複の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認のなど 複において選択記号 C を採用し、識別名は順序確認です。順序確認のなど 複において V (devnum1,devnum2,など) 複 は説明欄の「z/OS MVS Operationsで V (devnum1,devnum2,など) 複の扱いを記録する順序確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のなど 複を受け取る担当者は、V (devnum1,devnum2,など) 複の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のなど 複は別カテゴリの確認を流用しており、V (devnum1,devnum2,など) 複の根拠にならないため順序確認ではありません。 B: 順序確認のなど 複は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序確認ではありません。 C: 順序確認のなど 複は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のなど 複は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のなど 複が示す V (devnum1,devnum2,など) 複は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200



### V devnum,OFFLINE {#c22-i0299}
*分類: V dev*  ・  難易度: 中級

V devnum,OFFLINEは、MVS オペレータコマンドのV devで確認する項目です。指定装置をオフラインにする。ALLOC 中の装置はオフライン保留状態 (BOX) となる場合あり

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 範囲照合再の操作コマンドで操作コマンドの運用確認を行います。V devnum 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲照合再の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず範囲照合再の操作コマンドを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲照合再の点検結果を残す。 ✅
    - D. V devnum 命令の属性行を読まず範囲照合再の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合再正解では選択記号 C を採用し、正解名は範囲照合再正解です。範囲照合再根拠では V devnum 命令 は「z/OS MVS Operationsで V devnum 命令の扱いを記録する範囲照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲照合再根拠です。範囲照合再受渡では V devnum 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲照合再受渡です。不適切な選択肢を整理します。 A: 範囲照合再流用は別カテゴリの確認であり、排除名は範囲照合再流用です。 B: 範囲照合再欠落は戻り値や記録番号に寄り、欠落名は範囲照合再欠落です。 C: 範囲照合再正答は対象出力と項目説明を結び、根拠名は範囲照合再正答です。 D: 範囲照合再不足は名称や説明だけに寄り、判定名は範囲照合再不足です。範囲照合再資料では V devnum 命令の使い方を出典欄から追跡し、資料名は範囲照合再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 記録確認の操作コマンドに関係する V devnum,OFFLINE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録確認として残す。 ✅
    - B. V devnum,OFFLINE の名称と担当者名のみを残して記録確認の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で記録確認の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず記録確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認の操作コマンドにおいて選択記号 A を採用し、識別名は記録確認です。記録確認の操作コマンドにおいて V devnum,OFFLINE は説明欄の「V devnum,OFFLINE の用途を操作コマンドの表示で確認する記録確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の操作コマンドに関連して、z/OS MVS Operationsでは V devnum,OFFLINE の表示属性と IEE115I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の操作コマンドは別カテゴリの確認を流用しており、V devnum,OFFLINE の根拠にならないため記録確認ではありません。 D: 記録確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録確認ではありません。記録確認の操作コマンドで使う V devnum,OFFLINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V devnum,OFFLINE**

    - 検証目的: 探索整理の操作コマンドについて、V devnum,OFFLINE は、MVS オペレータコマンドの V devで確認する項目です。指定装置をオフラインにする。ALLOC 中の装置はオフライン保留状態 (BOXに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020106の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、探索整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum,OFFLINEを指定し、OSKB020106の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V devnum,OFFLINE
    CASE OSKB020106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V devnum,OFFLINE
    CASE OSKB020106
    SOURCE z/OS MVS Operations
    ```

    V devnum,OFFLINEとOSKB020106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020106を同じ出力で読み、探索整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020106
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020106 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020106   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V devnum,OFFLINE と OSKB020106 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V devnum,OFFLINE,FORCE {#c22-i0300}
*分類: V dev*  ・  難易度: 中級

V devnum,OFFLINE,FORCEは、MVS オペレータコマンドのV devで確認する項目です。ALLOC 中でも強制オフライン化する。データセット破損リスクがあるため緊急時に限定

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 優先照合再の操作コマンドに関する V devnum 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先照合再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先照合再の操作コマンドの証跡として保存して根拠にする。
    - C. V devnum 命令の変更点を出力本文から切り離して優先照合再の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先照合再で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合再正解では選択記号 D を採用し、正解名は優先照合再正解です。優先照合再根拠では V devnum 命令 は「V devnum 命令の状態と出力メッセージを結び付ける優先照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は優先照合再根拠です。優先照合再保存では V devnum 命令の出力行と IEE115I を一緒に残し、保存名は優先照合再保存です。選択肢ごとの違いを示します。 A: 優先照合再欠落は戻り値や記録番号に寄り、欠落名は優先照合再欠落です。 B: 優先照合再流用は別カテゴリの確認であり、排除名は優先照合再流用です。 C: 優先照合再不足は名称や説明だけに寄り、判定名は優先照合再不足です。 D: 優先照合再正答は対象出力と項目説明を結び、根拠名は優先照合再正答です。優先照合再対象では V devnum 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先照合再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 比較確認の操作コマンドで V devnum,OFFLINE,FORCE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V devnum,OFFLINE,FORCE の出力を取らず比較確認の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 ✅
    - C. D A,L を省略して比較確認の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認の操作コマンドにおいて選択記号 B を採用し、識別名は比較確認です。比較確認の操作コマンドにおいて V devnum,OFFLINE,FORCE は説明欄の「比較確認の操作コマンドに関係する定義値と表示行を照合する比較確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の操作コマンドの証跡を読む担当者は、V devnum,OFFLINE,FORCE の属性行と IEE115I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較確認ではありません。 D: 比較確認の操作コマンドは別カテゴリの確認を流用しており、V devnum,OFFLINE,FORCE の根拠にならないため比較確認ではありません。比較確認の操作コマンドに出る V devnum,OFFLINE,FORCE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V devnum,OFFLINE,FORCE**

    - 検証目的: 上書整理の操作コマンドについて、V devnum,OFFLINE,FORCE は、MVS オペレータコマンドの V devで確認する項目です。ALLOC 中でも強制オフライン化する。データセット破損リスクがあに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum,OFFLINE,Fを指定し、OSKB020107の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V devnum,OFFLINE,F
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V devnum,OFFLINE,F
    CASE OSKB020107
    SOURCE z/OS MVS Operations
    ```

    V devnum,OFFLINE,FとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020107を同じ出力で読み、上書整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020107 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020107   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V devnum,OFFLINE,F と OSKB020107 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V devnum,ONLINE {#c22-i0301}
*分類: V dev*  ・  難易度: 中級

V devnum,ONLINEは、MVS オペレータコマンドのV devで確認する項目です。指定装置 (DASD / TAPE / 端末 / プリンタ) をオンライン化する。VOLSER 認識と UCB 状態の正常化が同時に走る

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 区切照合再の操作コマンドで V devnum,ONLINE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V devnum,ONLINE の出力を取らず区切照合再の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切照合再の確認にする。 ✅
    - C. D A,L を省略して区切照合再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切照合再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合再正解では選択記号 B を採用し、正解名は区切照合再正解です。区切照合再根拠では V devnum,ONLINE は「区切照合再の操作コマンドに関係する定義値と表示行を照合する区切照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は区切照合再根拠です。区切照合再追跡では V devnum,ONLINE の属性行と IEE115I を合わせ、追跡名は区切照合再追跡です。誤答側の問題点を分けます。 A: 区切照合再不足は名称や説明だけに寄り、判定名は区切照合再不足です。 B: 区切照合再正答は対象出力と項目説明を結び、根拠名は区切照合再正答です。 C: 区切照合再欠落は戻り値や記録番号に寄り、欠落名は区切照合再欠落です。 D: 区切照合再流用は別カテゴリの確認であり、排除名は区切照合再流用です。区切照合再初出では V devnum,ONLINE を MVS オペレータコマンドの運用手順で確認し、初出名は区切照合再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 優先確認の操作コマンドに関する V devnum,ONLINE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先確認の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の操作コマンドの証跡として保存して根拠にする。
    - C. V devnum,ONLINE の変更点を出力本文から切り離して優先確認の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認の操作コマンドにおいて選択記号 D を採用し、識別名は優先確認です。優先確認の操作コマンドにおいて V devnum,ONLINE は説明欄の「V devnum,ONLINE の状態と出力メッセージを結び付ける優先確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の操作コマンドに関する記録は、V devnum,ONLINE の出力行と IEE115I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先確認ではありません。 B: 優先確認の操作コマンドは別カテゴリの確認を流用しており、V devnum,ONLINE の根拠にならないため優先確認ではありません。 C: 優先確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の操作コマンドで記録する V devnum,ONLINE はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V devnum,ONLINE**

    - 検証目的: 終端整理の操作コマンドについて、V devnum,ONLINE は、MVS オペレータコマンドの V devで確認する項目です。指定装置 (DASD / TAPE / 端末 / プリンタ) をオンライン化するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020105の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum,ONLINEを指定し、OSKB020105の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V devnum,ONLINE
    CASE OSKB020105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V devnum,ONLINE
    CASE OSKB020105
    SOURCE z/OS MVS Operations
    ```

    V devnum,ONLINEとOSKB020105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020105を同じ出力で読み、終端整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020105
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020105 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020105   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V devnum,ONLINE と OSKB020105 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V devnum-devnum,ONLINE 範囲 {#c22-i0302}
*分類: V dev*  ・  難易度: 中級

V devnum-devnum,ONLINE 範囲は、MVS オペレータコマンドのV devで確認する項目です。ハイフン区切りで連続装置範囲を一括オンライン化する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 比較照合再の範で V devnum-devnum 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V devnum-devnum 命令の出力を取らず比較照合再の範の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較照合再の根拠を固定する。 ✅
    - C. D A,L を省略して比較照合再の範の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較照合再の範へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合再正解では選択記号 B を採用し、正解名は比較照合再正解です。比較照合再根拠では V devnum-devnum 命令 は「比較照合再の範に関係する定義値と表示行を照合する比較照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は比較照合再根拠です。比較照合再追跡では V devnum-devnum 命令の属性行と IEE115I を合わせ、追跡名は比較照合再追跡です。誤答側の問題点を分けます。 A: 比較照合再不足は名称や説明だけに寄り、判定名は比較照合再不足です。 B: 比較照合再正答は対象出力と項目説明を結び、根拠名は比較照合再正答です。 C: 比較照合再欠落は戻り値や記録番号に寄り、欠落名は比較照合再欠落です。 D: 比較照合再流用は別カテゴリの確認であり、排除名は比較照合再流用です。比較照合再初出では V devnum-devnum 命令を MVS オペレータコマンドの運用手順で確認し、初出名は比較照合再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 値域確認の範に関する V devnum-devnum,ONLINE 範の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域確認の範の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の範の証跡として保存して根拠にする。
    - C. V devnum-devnum,ONLINE 範の変更点を出力本文から切り離して値域確認の範の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認の範において選択記号 D を採用し、識別名は値域確認です。値域確認の範において V devnum-devnum,ONLINE 範 は説明欄の「V devnum-devnum,ONLINE 範の状態と出力メッセージを結び付ける値域確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の範に関する記録は、V devnum-devnum,ONLINE 範の出力行と IEE115I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の範は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域確認ではありません。 B: 値域確認の範は別カテゴリの確認を流用しており、V devnum-devnum,ONLINE 範の根拠にならないため値域確認ではありません。 C: 値域確認の範は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の範は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の範で記録する V devnum-devnum,ONLINE 範はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V devnum-devnum,ONLINE 範囲**

    - 検証目的: 条件整理の範について、V devnum-devnum,ONLINE 範囲は、MVS オペレータコマンドの V devで確認する項目です。ハイフン区切りで連続装置範囲を一括オンライン化するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020109の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件整理の範の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum-devnum,ONを指定し、OSKB020109の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V devnum-devnum,ON
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V devnum-devnum,ON
    CASE OSKB020109
    SOURCE z/OS MVS Operations
    ```

    V devnum-devnum,ONとOSKB020109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020109を同じ出力で読み、条件整理の範の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020109 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020109   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V devnum-devnum,ON と OSKB020109 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > WTOR

### DESC コード (Descriptor) {#c22-i0303}
*分類: WTOR*  ・  難易度: 中級

WTO/WTOR メッセージの DESC=(n,...) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使用

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 終端検査のコードに関係する DESC コード (Descriptor)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端検査として残す。 ✅
    - B. DESC コード (Descriptor)の名称と担当者名のみを残して終端検査のコードの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で終端検査のコードを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端検査のコードの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査のコードにおいて選択記号 A を採用し、識別名は終端検査です。終端検査のコードにおいて DESC コード (Descriptor) は説明欄の「WTO/WTOR メッセージの DESC=(n,など) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使」と D A,L または該当パネルの出力を照合する対象で、答え名は終端検査です。終端検査のコードに関連して、z/OS MVS Operationsでは DESC コード (Descriptor)の表示属性と IEE115I を同じ証跡に残し、背景名は終端検査です。他の選択肢を確認します。 A: 終端検査のコードは対象出力と項目説明を結び、根拠を残すので終端検査です。 B: 終端検査のコードは名称や説明のみに寄り、状態を示す出力本文が不足するため終端検査ではありません。 C: 終端検査のコードは別カテゴリの確認を流用しており、DESC コード (Descriptor)の根拠にならないため終端検査ではありません。 D: 終端検査のコードは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端検査ではありません。終端検査のコードで使う DESC コード (Descriptor)という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **DESC コード (Descriptor)**

    - 検証目的: 出力追跡のコードについて、WTO/WTOR メッセージの DESC=(n,など) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040048の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、出力追跡のコードの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にDESC コード (Descriptを指定し、OSKB040048の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND DESC コード (Descript
    CASE OSKB040048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM DESC コード (Descript
    CASE OSKB040048
    SOURCE z/OS MVS Operations
    ```

    DESC コード (DescriptとOSKB040048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040048を同じ出力で読み、出力追跡のコードの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040048 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040048   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の DESC コード (Descript と OSKB040048 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **DESC コード (Descriptor)**

    - 検証目的: 復旧照合のコードについて、WTO/WTOR メッセージの DESC=(n,など) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030038の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、復旧照合のコードの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にDESC コード (Descriptを指定し、OSKB030038の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND DESC コード (Descript
    CASE OSKB030038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM DESC コード (Descript
    CASE OSKB030038
    SOURCE z/OS MVS Operations
    ```

    DESC コード (DescriptとOSKB030038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030038を同じ出力で読み、復旧照合のコードの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030038
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030038 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030038   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の DESC コード (Descript と OSKB030038 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### ROUTCDE (ルート・コード) {#c22-i0304}
*分類: WTOR*  ・  難易度: 中級

WTO/WTOR の配信先カテゴリ (MASTER, TAPE LIB, PROD CONTROL 等)。コンソールの ROUTCDE と一致したものを受信

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 探索検査のルート・コードで ROUTCDE (ルート・コード)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ROUTCDE (ルート・コード)の出力を取らず探索検査のルート・コードの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索検査の確認結果にする。 ✅
    - C. D A,L を省略して探索検査のルート・コードの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査のルート・コードへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査のルート・コードにおいて選択記号 B を採用し、識別名は探索検査です。探索検査のルート・コードにおいて ROUTCDE (ルート・コード) は説明欄の「探索検査のルート・コードに関係する定義値と表示行を照合する探索検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索検査です。探索検査のルート・コードの証跡を読む担当者は、ROUTCDE (ルート・コード)の属性行と IEE115I を合わせて追跡し、背景名は探索検査です。誤答側の問題点を分けます。 A: 探索検査のルート・コードは名称や説明のみに寄り、状態を示す出力本文が不足するため探索検査ではありません。 B: 探索検査のルート・コードは対象出力と項目説明を結び、根拠を残すので探索検査です。 C: 探索検査のルート・コードは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索検査ではありません。 D: 探索検査のルート・コードは別カテゴリの確認を流用しており、ROUTCDE (ルート・コード)の根拠にならないため探索検査ではありません。探索検査のルート・コードに出る ROUTCDE (ルート・コード)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **ROUTCDE (ルート・コード)**

    - 検証目的: 監査照合のルート・コードについて、WTO/WTOR の配信先カテゴリ (MASTER, TAPE LIB, PROD CONTROL 等)。コンソールの ROUTCDE と一致したものを受信に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030039の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査照合のルート・コードの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTCDE (ルート・コード)を指定し、OSKB030039の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTCDE (ルート・コード)
    CASE OSKB030039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTCDE (ルート・コード)
    CASE OSKB030039
    SOURCE z/OS MVS Operations
    ```

    ROUTCDE (ルート・コード)とOSKB030039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030039を同じ出力で読み、監査照合のルート・コードの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030039 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030039   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTCDE (ルート・コード) と OSKB030039 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### WTOR メッセージの保持 {#c22-i0305}
*分類: WTOR*  ・  難易度: 中級

WTOR メッセージの保持は、MVS オペレータコマンドのWTORで確認する項目です。WTOR は応答が来るまで OS 内に保持され、再表示要求 (K M,REF) で再描画できる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力検査のメッセージの保持に関する WTOR メッセージの保持の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力検査のメッセージの保持の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のメッセージの保持の証跡として保存して根拠にする。
    - C. WTOR メッセージの保持の変更点を出力本文から切り離して出力検査のメッセージの保持の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査のメッセージの保持において選択記号 D を採用し、識別名は出力検査です。出力検査のメッセージの保持において WTOR メッセージの保持 は説明欄の「WTOR メッセージの保持の状態と出力メッセージを結び付ける出力検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査のメッセージの保持に関する記録は、WTOR メッセージの保持の出力行と IEE115I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査のメッセージの保持は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力検査ではありません。 B: 出力検査のメッセージの保持は別カテゴリの確認を流用しており、WTOR メッセージの保持の根拠にならないため出力検査ではありません。 C: 出力検査のメッセージの保持は名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査のメッセージの保持は対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査のメッセージの保持で記録する WTOR メッセージの保持はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **WTOR メッセージの保持**

    - 検証目的: 構文追跡のメッセージの保持について、WTOR メッセージの保持は、MVS オペレータコマンドの WTOR で確認する項目です。WTOR は応答が来るまで OS 内に保持され、再表示要求 (K M,REF) で再描に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030041の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文追跡のメッセージの保持の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にWTOR メッセージの保持を指定し、OSKB030041の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND WTOR メッセージの保持
    CASE OSKB030041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM WTOR メッセージの保持
    CASE OSKB030041
    SOURCE z/OS MVS Operations
    ```

    WTOR メッセージの保持とOSKB030041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030041を同じ出力で読み、構文追跡のメッセージの保持の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030041 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030041   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の WTOR メッセージの保持 と OSKB030041 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 応答番号 (reply ID) の上限 {#c22-i0306}
*分類: WTOR*  ・  難易度: 中級

未応答 WTOR の同時保持上限は IEACMD/CONSOLxx の REPLY 制限に依存。閾値超えはシステム障害化のリスク

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 上書検査の応答番号 の上限で操作コマンドの運用確認を行います。応答番号 (reply ID) の上限の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書検査の応答番号 の上限を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書検査の応答番号 の上限を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書検査の記録として扱う。 ✅
    - D. 応答番号 (reply ID) の上限の属性行を読まず上書検査の応答番号 の上限の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査の応答番号 の上限において選択記号 C を採用し、識別名は上書検査です。上書検査の応答番号 の上限において応答番号 (reply ID) の上限 は説明欄の「z/OS MVS Operationsで応答番号 (reply ID) の上限の扱いを記録する上書検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書検査です。上書検査の応答番号 の上限を受け取る担当者は、応答番号 (reply ID) の上限の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書検査です。不適切な選択肢を整理します。 A: 上書検査の応答番号 の上限は別カテゴリの確認を流用しており、応答番号 (reply ID) の上限の根拠にならないため上書検査ではありません。 B: 上書検査の応答番号 の上限は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書検査ではありません。 C: 上書検査の応答番号 の上限は対象出力と項目説明を結び、根拠を残すので上書検査です。 D: 上書検査の応答番号 の上限は名称や説明のみに寄り、状態を示す出力本文が不足するため上書検査ではありません。上書検査の応答番号 の上限が示す応答番号 (reply ID) の上限は出典欄の資料で使い方を追跡できる項目であり、用語名は上書検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **応答番号 (reply ID) の上限**

    - 検証目的: 変更照合の応答番号 の上限について、未応答 WTOR の同時保持上限は IEACMD/CONSOLxx の REPLY 制限に依存。閾値超えはシステム障害化のリスクに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030040の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更照合の応答番号 の上限の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に応答番号 (reply ID) の上を指定し、OSKB030040の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 応答番号 (reply ID) の上
    CASE OSKB030040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 応答番号 (reply ID) の上
    CASE OSKB030040
    SOURCE z/OS MVS Operations
    ```

    応答番号 (reply ID) の上とOSKB030040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030040を同じ出力で読み、変更照合の応答番号 の上限の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030040 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030040   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の 応答番号 (reply ID) の上 と OSKB030040 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > Z

### Z EOD {#c22-i0307}
*分類: Z*  ・  難易度: 中級

Z EODは、MVS オペレータコマンドのZで状態表示や操作を行うためのコマンド関連項目です。End-Of-Day の意で、SMF / LOGREC / SYSLOG / ハードコピーのデータをフラッシュし、停止前の整合性を取る。IPL 前に必須

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 値域照合の操作コマンドに関する Z EOD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の操作コマンドの証跡として保存して根拠にする。
    - C. Z EOD の変更点を出力本文から切り離して値域照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合の操作コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の操作コマンドにおいて Z EOD は説明欄の「Z EOD の状態と出力メッセージを結び付ける値域照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の操作コマンドに関する記録は、Z EOD の出力行と IEE115I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域照合ではありません。 B: 値域照合の操作コマンドは別カテゴリの確認を流用しており、Z EOD の根拠にならないため値域照合ではありません。 C: 値域照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の操作コマンドで記録する Z EOD はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **Z EOD**

    - 検証目的: 条件確認の操作コマンドについて、Z EOD は、MVS オペレータコマンドの Z で状態表示や操作を行うためのコマンド関連項目です。End-Of-Day の意で、SMF / LOGREC / SYSLOG /に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030009の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にZ EODを指定し、OSKB030009の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Z EOD
    CASE OSKB030009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Z EOD
    CASE OSKB030009
    SOURCE z/OS MVS Operations
    ```

    Z EODとOSKB030009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030009を同じ出力で読み、条件確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030009
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030009 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030009   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の Z EOD と OSKB030009 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### Z NET {#c22-i0308}
*分類: Z*  ・  難易度: 中級

Z NETは、MVS オペレータコマンドのZで確認する項目です。VTAM を停止する標準形式。すべてのセッション・APPL を正常クローズしてから停止

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告照合の操作コマンドに関係する Z NET の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 ✅
    - B. Z NET の名称と担当者名のみを残して警告照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合の操作コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合の操作コマンドにおいて Z NET は説明欄の「Z NET の用途を操作コマンドの表示で確認する警告照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の操作コマンドに関連して、z/OS MVS Operationsでは Z NET の表示属性と IEE115I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の操作コマンドは別カテゴリの確認を流用しており、Z NET の根拠にならないため警告照合ではありません。 D: 警告照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告照合ではありません。警告照合の操作コマンドで使う Z NET という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **Z NET**

    - 検証目的: 区切確認の操作コマンドについて、Z NET は、MVS オペレータコマンドの Z で確認する項目です。VTAM を停止する標準形式。すべてのセッション・ APPL を正常クローズしてから停止に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にZ NETを指定し、OSKB030010の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Z NET
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Z NET
    CASE OSKB030010
    SOURCE z/OS MVS Operations
    ```

    Z NETとOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030010を同じ出力で読み、区切確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030010 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030010   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の Z NET と OSKB030010 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### Z NET,CANCEL {#c22-i0309}
*分類: Z*  ・  難易度: 中級

Z NET,CANCELは、MVS オペレータコマンドのZで確認する項目です。VTAM の全セッションを即時キャンセルして停止する最も強い形式

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査照合の操作コマンドで操作コマンドの運用確認を行います。Z NET,CANCEL の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査照合の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. Z NET,CANCEL の属性行を読まず監査照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合の操作コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の操作コマンドにおいて Z NET,CANCEL は説明欄の「z/OS MVS Operationsで Z NET,CANCEL の扱いを記録する監査照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の操作コマンドを受け取る担当者は、Z NET,CANCEL の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の操作コマンドは別カテゴリの確認を流用しており、Z NET,CANCEL の根拠にならないため監査照合ではありません。 B: 監査照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査照合ではありません。 C: 監査照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の操作コマンドが示す Z NET,CANCEL は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **Z NET,CANCEL**

    - 検証目的: 優先確認の操作コマンドについて、Z NET,CANCEL は、MVS オペレータコマンドの Z で確認する項目です。VTAM の全セッションを即時キャンセルして停止する最も強い形式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030012の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にZ NET,CANCELを指定し、OSKB030012の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Z NET,CANCEL
    CASE OSKB030012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Z NET,CANCEL
    CASE OSKB030012
    SOURCE z/OS MVS Operations
    ```

    Z NET,CANCELとOSKB030012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030012を同じ出力で読み、優先確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030012
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030012 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030012   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の Z NET,CANCEL と OSKB030012 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### Z NET,QUICK {#c22-i0310}
*分類: Z*  ・  難易度: 中級

Z NET,QUICKは、MVS オペレータコマンドのZで確認する項目です。VTAM を即時停止 (セッション正常クローズなし) する形式。緊急時のみ使用

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧照合の操作コマンドで Z NET,QUICK の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Z NET,QUICK の出力を取らず復旧照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 ✅
    - C. D A,L を省略して復旧照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合の操作コマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の操作コマンドにおいて Z NET,QUICK は説明欄の「復旧照合の操作コマンドに関係する定義値と表示行を照合する復旧照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の操作コマンドの証跡を読む担当者は、Z NET,QUICK の属性行と IEE115I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の操作コマンドは別カテゴリの確認を流用しており、Z NET,QUICK の根拠にならないため復旧照合ではありません。復旧照合の操作コマンドに出る Z NET,QUICK は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **Z NET,QUICK**

    - 検証目的: 範囲確認の操作コマンドについて、Z NET,QUICK は、MVS オペレータコマンドの Z で確認する項目です。VTAM を即時停止 (セッション正常クローズなし) する形式。緊急時のみ使用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030011の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にZ NET,QUICKを指定し、OSKB030011の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Z NET,QUICK
    CASE OSKB030011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Z NET,QUICK
    CASE OSKB030011
    SOURCE z/OS MVS Operations
    ```

    Z NET,QUICKとOSKB030011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030011を同じ出力で読み、範囲確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030011
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030011 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030011   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の Z NET,QUICK と OSKB030011 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## その他

### その他（特定項目に紐づかないQA・手順） {#c22-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（4問）"
    **問題.** 範囲検分のなどの不在で操作コマンドの運用確認を行います。S TRACE,などの不在の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲検分のなどの不在を確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲検分のなどの不在を正常終了として記録する。
    - C. 同じ画面で対象行と IEE457I を読み、範囲検分の結果として保存する。 ✅
    - D. S TRACE,などの不在の属性行を読まず範囲検分のなどの不在の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では S TRACE,などの不在 は「z/OS MVS Operationsで S TRACE,などの不在の扱いを記録する範囲検分項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では S TRACE,などの不在の表示結果と IEE457I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明だけに寄り、判定名は範囲検分不足です。範囲検分資料では S TRACE,などの不在の使い方を出典欄から追跡し、資料名は範囲検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 記録確認再のなど 管理に関係する F NET 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録確認再の確認記録にまとめる。 ✅
    - B. F NET 命令の名称と担当者名だけを残して記録確認再のなど 管理の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録確認再のなど 管理を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず記録確認再のなど 管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認再正解では選択記号 A を採用し、正解名は記録確認再正解です。記録確認再根拠では F NET 命令 は「F NET 命令の用途を操作コマンドの表示で確認する記録確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は記録確認再根拠です。記録確認再背景ではz/OS MVS Operationsの F NET 命令と IEE115I を同じ証跡に残し、背景名は記録確認再背景です。他の選択肢を確認します。 A: 記録確認再正答は対象出力と項目説明を結び、根拠名は記録確認再正答です。 B: 記録確認再不足は名称や説明だけに寄り、判定名は記録確認再不足です。 C: 記録確認再流用は別カテゴリの確認であり、排除名は記録確認再流用です。 D: 記録確認再欠落は戻り値や記録番号に寄り、欠落名は記録確認再欠落です。記録確認再用語では F NET 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録確認再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 監査確認再のなどで操作コマンドの運用確認を行います。F BPXOINIT 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査確認再のなどを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査確認再のなどを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査確認再の点検結果を残す。 ✅
    - D. F BPXOINIT 命令の属性行を読まず監査確認再のなどの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認再正解では選択記号 C を採用し、正解名は監査確認再正解です。監査確認再根拠では F BPXOINIT 命令 は「z/OS MVS Operationsで F BPXOINIT 命令の扱いを記録する監査確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は監査確認再根拠です。監査確認再受渡では F BPXOINIT 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査確認再受渡です。不適切な選択肢を整理します。 A: 監査確認再流用は別カテゴリの確認であり、排除名は監査確認再流用です。 B: 監査確認再欠落は戻り値や記録番号に寄り、欠落名は監査確認再欠落です。 C: 監査確認再正答は対象出力と項目説明を結び、根拠名は監査確認再正答です。 D: 監査確認再不足は名称や説明だけに寄り、判定名は監査確認再不足です。監査確認再資料では F BPXOINIT 命令の使い方を出典欄から追跡し、資料名は監査確認再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 記録照合再のなど 複に関係する V 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録照合再の確認値として扱う。 ✅
    - B. V 属性の名称と担当者名だけを残して記録照合再のなど 複の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録照合再のなど 複を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず記録照合再のなど 複の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合再正解では選択記号 A を採用し、正解名は記録照合再正解です。記録照合再根拠では V 属性 は「V 属性の用途を操作コマンドの表示で確認する記録照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は記録照合再根拠です。記録照合再背景ではz/OS MVS Operationsの V 属性と IEE115I を同じ証跡に残し、背景名は記録照合再背景です。他の選択肢を確認します。 A: 記録照合再正答は対象出力と項目説明を結び、根拠名は記録照合再正答です。 B: 記録照合再不足は名称や説明だけに寄り、判定名は記録照合再不足です。 C: 記録照合再流用は別カテゴリの確認であり、排除名は記録照合再流用です。 D: 記録照合再欠落は戻り値や記録番号に寄り、欠落名は記録照合再欠落です。記録照合再用語では V 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は記録照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（8件）"
    **V TCPIP,,VARY,nnnn,など**

    - 検証目的: 呼出追跡のなどについて、V TCPIP,,VARY,nnnn,などは、MVS オペレータコマンドの V TCPIP で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040043の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、呼出追跡のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,VARY,nnnnを指定し、OSKB040043の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V TCPIP,,VARY,nnnn
    CASE OSKB040043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V TCPIP,,VARY,nnnn
    CASE OSKB040043
    SOURCE z/OS MVS Operations
    ```

    V TCPIP,,VARY,nnnnとOSKB040043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040043を同じ出力で読み、呼出追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040043
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040043 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040043   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の V TCPIP,,VARY,nnnn と OSKB040043 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **S TRACE,などの不在**

    - 検証目的: 探索検査のなどの不在について、トレースは S ではなく TRACE CT,ON / SET TRACE で開始する点に注意。S は使用しないに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索検査のなどの不在の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS TRACE,などの不在を指定し、OSKB020066の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S TRACE,などの不在
    CASE OSKB020066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S TRACE,などの不在
    CASE OSKB020066
    SOURCE z/OS MVS Operations
    ```

    S TRACE,などの不在とOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020066を同じ出力で読み、探索検査のなどの不在の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020066
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020066 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020066   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の S TRACE,などの不在 と OSKB020066 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **F NET,USER,など VTAM 管理**

    - 検証目的: 出力判定のなど 管理について、F NET,USER,など VTAM 管理は、VTAM に対する SNA リソース個別制御 (例: F NET,USER,ID=name,ACT)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、出力判定のなど 管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,USER,など VTAMを指定し、OSKB020088の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F NET,USER,など VTAM
    CASE OSKB020088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F NET,USER,など VTAM
    CASE OSKB020088
    SOURCE z/OS MVS Operations
    ```

    F NET,USER,など VTAMとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020088を同じ出力で読み、出力判定のなど 管理の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020088
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020088 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020088   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の F NET,USER,など VTAM と OSKB020088 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **F BPXOINIT,FILESYS= など**

    - 検証目的: 比較判定のなどについて、F BPXOINIT,FILESYS= などは、USS ファイルシステムに対する個別操作 (DISPLAY/UNMOUNT/MOVE) を行う MODIFY サブコマンド群に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020094の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較判定のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF BPXOINIT,FILESYSを指定し、OSKB020094の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F BPXOINIT,FILESYS
    CASE OSKB020094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F BPXOINIT,FILESYS
    CASE OSKB020094
    SOURCE z/OS MVS Operations
    ```

    F BPXOINIT,FILESYSとOSKB020094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020094を同じ出力で読み、比較判定のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020094
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020094 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020094   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の F BPXOINIT,FILESYS と OSKB020094 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **V (devnum1,devnum2,など) 複数指定**

    - 検証目的: 出力整理のなど 複について、V (devnum1,devnum2,など) 複数指定は、MVS オペレータコマンドの V devで確認する項目です。複数装置を 1 コマンドで同時に状態変更する形式。範囲指に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020108の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、出力整理のなど 複の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV (devnum1,devnum2を指定し、OSKB020108の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V (devnum1,devnum2
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V (devnum1,devnum2
    CASE OSKB020108
    SOURCE z/OS MVS Operations
    ```

    V (devnum1,devnum2とOSKB020108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020108を同じ出力で読み、出力整理のなど 複の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020108 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020108   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V (devnum1,devnum2 と OSKB020108 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **V TCPIP,,VARY,nnnn,など**

    - 検証目的: 出力確認のなどについて、V TCPIP,,VARY,nnnn,などは、MVS オペレータコマンドの V TCPIP で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030008の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力確認のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,VARY,nnnnを指定し、OSKB030008の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V TCPIP,,VARY,nnnn
    CASE OSKB030008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V TCPIP,,VARY,nnnn
    CASE OSKB030008
    SOURCE z/OS MVS Operations
    ```

    V TCPIP,,VARY,nnnnとOSKB030008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030008を同じ出力で読み、出力確認のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030008
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030008 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030008   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の V TCPIP,,VARY,nnnn と OSKB030008 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **ROUTE T=seconds,など**

    - 検証目的: 記録照合のなどについて、ROUTE T=seconds,などは、MVS オペレータコマンドの ROUTE で確認する項目です。応答待ちタイムアウトを指定。Sysplex 内応答が揃わない場合の待ち時間に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030033の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録照合のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE T=seconds,などを指定し、OSKB030033の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE T=seconds,など
    CASE OSKB030033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE T=seconds,など
    CASE OSKB030033
    SOURCE z/OS MVS Operations
    ```

    ROUTE T=seconds,などとOSKB030033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030033を同じ出力で読み、記録照合のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030033 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030033   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE T=seconds,など と OSKB030033 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **K S,DEL= など**

    - 検証目的: 優先追跡のなどについて、MVS オペレータコマンドの K では、対象資源、指定値、実行時の出力を対応付けて確認します。K は、MVS オペレータコマンドの運用で指定値、構文上の位置、反映後の出力を読み分に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030052の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先追跡のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にK S,DEL= などを指定し、OSKB030052の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND K S,DEL= など
    CASE OSKB030052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM K S,DEL= など
    CASE OSKB030052
    SOURCE z/OS MVS Operations
    ```

    K S,DEL= などとOSKB030052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030052を同じ出力で読み、優先追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030052
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030052 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030052   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の K S,DEL= など と OSKB030052 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

