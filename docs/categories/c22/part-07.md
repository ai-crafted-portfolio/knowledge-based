---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (7/7)

[← MVS オペレータコマンド の概要へ戻る](index.md)


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

