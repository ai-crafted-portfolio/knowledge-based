---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (6/7)

[← MVS オペレータコマンド の概要へ戻る](index.md)


## MVS オペレータコマンド > SET SMS

### SET SMS=xx {#c22-i0261}
*分類: SET SMS*  ・  難易度: 中級

SET SMS=xxは、IGDSMSxx を活性化し、ACS ルーチン・トレース、ACDS 切替などを反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 置換読解の操作コマンドに関する SET SMS=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず置換読解の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換読解の操作コマンドの証跡として保存して根拠にする。
    - C. SET SMS=xxの変更点を出力本文から切り離して置換読解の操作コマンドの承認欄だけ残す。
    - D. D OPDATA の結果から対象行を抜き出し、置換読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では SET SMS=xx は「SET SMS=xxの状態と出力メッセージを結び付ける置換読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では SET SMS=xxの出力行と IEE457I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明だけに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では SET SMS=xxをz/OS MVS Operationsの確認記録に残し、対象名は置換読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 探索追跡の操作コマンドで SET SMS=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET SMS=xxの出力を取らず探索追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 ✅
    - C. D OPDATA を省略して探索追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡の操作コマンドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の操作コマンドにおいて SET SMS=xx は説明欄の「探索追跡の操作コマンドに関係する定義値と表示行を照合する探索追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の操作コマンドの証跡を読む担当者は、SET SMS=xxの属性行と IEE457I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の操作コマンドは別カテゴリの確認を流用しており、SET SMS=xxの根拠にならないため探索追跡ではありません。探索追跡の操作コマンドに出る SET SMS=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET SMS=xx**

    - 検証目的: 監査照合の操作コマンドについて、SET SMS=xxは、IGDSMSxx を活性化し、ACS ルーチン・トレース、ACDS 切替などを反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、監査照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMS=xxを指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SMS=xx
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SMS=xx
    CASE OSKB020039
    SOURCE z/OS MVS Operations
    ```

    SET SMS=xxとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020039を同じ出力で読み、監査照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020039 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020039   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SMS=xx と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET TIME

### SET DATE=yyyy.ddd {#c22-i0262}
*分類: SET TIME*  ・  難易度: 中級

SET DATE=yyyy.dddは、MVS オペレータコマンドのSET TIMEで確認する項目です。ユリウス日形式でシステム日付を更新する。SET TIME と組み合わせて使用される

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書読解の操作コマンドで操作コマンドの運用確認を行います。SET 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書読解の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず上書読解の操作コマンドを正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、上書読解の結果として保存する。 ✅
    - D. SET 属性の属性行を読まず上書読解の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では SET 属性 は「z/OS MVS Operationsで SET 属性の扱いを記録する上書読解項目」と D A,L または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では SET 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明だけに寄り、判定名は上書読解不足です。上書読解資料では SET 属性の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件追跡の操作コマンドに関係する SET DATE=yyyy.dddの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. SET DATE=yyyy.dddの名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて SET DATE=yyyy.ddd は説明欄の「SET DATE=yyyy.dddの用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは SET DATE=yyyy.dddの表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、SET DATE=yyyy.dddの根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う SET DATE=yyyy.dddという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DATE=yyyy.ddd**

    - 検証目的: 展開追跡の操作コマンドについて、SET DATE=yyyy.dddは、MVS オペレータコマンドの SET TIME で確認する項目です。ユリウス日形式でシステム日付を更新する。SET TIME と組み合わせに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DATE=yyyy.dddを指定し、OSKB020042の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DATE=yyyy.ddd
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DATE=yyyy.ddd
    CASE OSKB020042
    SOURCE z/OS MVS Operations
    ```

    SET DATE=yyyy.dddとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020042を同じ出力で読み、展開追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020042 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020042   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SET DATE=yyyy.ddd と OSKB020042 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET TIME=hh.mm.ss {#c22-i0263}
*分類: SET TIME*  ・  難易度: 中級

SET TIME=hh.mm.ssは、MVS オペレータコマンドのSET TIMEで確認する項目です。システム時刻の手動更新。STP/Sysplex Timer 配下では通常使用せず、独立システムでの矯正に限定する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 探索読解の操作コマンドで SET 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET 属性の出力を取らず探索読解の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索読解の根拠にする。 ✅
    - C. D OPDATA を省略して探索読解の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索読解の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では SET 属性 は「探索読解の操作コマンドに関係する定義値と表示行を照合する探索読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では SET 属性の属性行と IEE457I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明だけに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では SET 属性を MVS オペレータコマンドの運用手順で確認し、初出名は探索読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 出力追跡の操作コマンドに関する SET TIME=hh.mm.ssの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。
    - C. SET TIME=hh.mm.ssの変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて SET TIME=hh.mm.ss は説明欄の「SET TIME=hh.mm.ssの状態と出力メッセージを結び付ける出力追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、SET TIME=hh.mm.ssの出力行と IEE457I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、SET TIME=hh.mm.ssの根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する SET TIME=hh.mm.ssはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET TIME=hh.mm.ss**

    - 検証目的: 構文追跡の操作コマンドについて、SET TIME=hh.mm.ssは、MVS オペレータコマンドの SET TIME で確認する項目です。システム時刻の手動更新。STP/Sysplex Timer 配下では通に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、構文追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET TIME=hh.mm.ssを指定し、OSKB020041の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET TIME=hh.mm.ss
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET TIME=hh.mm.ss
    CASE OSKB020041
    SOURCE z/OS MVS Operations
    ```

    SET TIME=hh.mm.ssとOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020041を同じ出力で読み、構文追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020041 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020041   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET TIME=hh.mm.ss と OSKB020041 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET TRACE

### SET TRACE,ON {#c22-i0264}
*分類: SET TRACE*  ・  難易度: 上級

SET TRACE,ONは、MVS オペレータコマンドのSET TRACEで確認する項目です。システム・トレースを動的に有効化する基本形。バッファサイズ・対象 ASID も同時に指定可能

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力読解の操作コマンドに関する SET TRACE,ON の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力読解の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力読解の操作コマンドの証跡として保存して根拠にする。
    - C. SET TRACE,ON の変更点を出力本文から切り離して出力読解の操作コマンドの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、出力読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では SET TRACE,ON は「SET TRACE,ON の状態と出力メッセージを結び付ける出力読解項目」と D A,L または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では SET TRACE,ON の出力行と IEE115I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明だけに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では SET TRACE,ON をz/OS MVS Operationsの確認記録に残し、対象名は出力読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切追跡の操作コマンドで SET TRACE,ON の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET TRACE,ON の出力を取らず区切追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 ✅
    - C. D A,L を省略して区切追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡の操作コマンドにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡の操作コマンドにおいて SET TRACE,ON は説明欄の「区切追跡の操作コマンドに関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の操作コマンドの証跡を読む担当者は、SET TRACE,ON の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の操作コマンドは別カテゴリの確認を流用しており、SET TRACE,ON の根拠にならないため区切追跡ではありません。区切追跡の操作コマンドに出る SET TRACE,ON は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET TRACE,ON**

    - 検証目的: 呼出追跡の操作コマンドについて、SET TRACE,ON は、MVS オペレータコマンドの SET TRACE で確認する項目です。システム・トレースを動的に有効化する基本形。バッファサイズ・対象 ASID もに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET TRACE,ONを指定し、OSKB020043の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET TRACE,ON
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET TRACE,ON
    CASE OSKB020043
    SOURCE z/OS MVS Operations
    ```

    SET TRACE,ONとOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020043を同じ出力で読み、呼出追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020043 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020043   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SET TRACE,ON と OSKB020043 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### TRACE CT (CTRACE 動的) {#c22-i0265}
*分類: SET TRACE*  ・  難易度: 上級

TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件読解の動的に関係する TRACE CT 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件読解として引き継ぐ。 ✅
    - B. TRACE CT 属性の名称と担当者名だけを残して条件読解の動的の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件読解の動的を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件読解の動的の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では TRACE CT 属性 は「TRACE CT 属性の用途を操作コマンドの表示で確認する条件読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景ではz/OS MVS Operationsの TRACE CT 属性と IEE457I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明だけに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では TRACE CT 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **TRACE CT (CTRACE 動的)**

    - 検証目的: 条件照合の動的について、TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040029の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、条件照合の動的の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRACE CT (CTRACE 動を指定し、OSKB040029の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRACE CT (CTRACE 動
    CASE OSKB040029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRACE CT (CTRACE 動
    CASE OSKB040029
    SOURCE z/OS MVS Operations
    ```

    TRACE CT (CTRACE 動とOSKB040029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040029を同じ出力で読み、条件照合の動的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040029
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040029 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040029   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の TRACE CT (CTRACE 動 と OSKB040029 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **TRACE CT (CTRACE 動的)**

    - 検証目的: 置換追跡の動的について、TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、置換追跡の動的の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRACE CT (CTRACE 動を指定し、OSKB020044の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRACE CT (CTRACE 動
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRACE CT (CTRACE 動
    CASE OSKB020044
    SOURCE z/OS MVS Operations
    ```

    TRACE CT (CTRACE 動とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020044を同じ出力で読み、置換追跡の動的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020044 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020044   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の TRACE CT (CTRACE 動 と OSKB020044 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET XCF

### SET XCF=xx {#c22-i0266}
*分類: SET XCF*  ・  難易度: 中級

SET XCF=xxは、COUPLExx を再活性化し、Sysplex の Couple DS 設定や SFM/CFRM ポリシー名の動的入替を行う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切読解の操作コマンドで SET XCF=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET XCF=xxの出力を取らず区切読解の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切読解の確認にする。 ✅
    - C. D OPDATA を省略して区切読解の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切読解の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では SET XCF=xx は「区切読解の操作コマンドに関係する定義値と表示行を照合する区切読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では SET XCF=xxの属性行と IEE457I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明だけに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では SET XCF=xxを MVS オペレータコマンドの運用手順で確認し、初出名は区切読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET XCF=xx**

    - 検証目的: 終端追跡の操作コマンドについて、SET XCF=xxは、COUPLExx を再活性化し、Sysplex の Couple DS 設定や SFM/CFRM ポリシー名の動的入替を行うに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、終端追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET XCF=xxを指定し、OSKB020045の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET XCF=xx
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET XCF=xx
    CASE OSKB020045
    SOURCE z/OS MVS Operations
    ```

    SET XCF=xxとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020045 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020045   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET XCF=xx と OSKB020045 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETXCF COUPLE,ACOUPLE=dsn {#c22-i0267}
*分類: SET XCF*  ・  難易度: 中級

SETXCF COUPLE,ACOUPLE=dsnは、予備 Couple DS を動的に追加し、PSWITCH で本番側に昇格させる無停止切替手順を構成する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 記録読解の操作コマンドに関係する SETXCF COUPLE 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録読解の確認値として扱う。 ✅
    - B. SETXCF COUPLE 命令の名称と担当者名だけを残して記録読解の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録読解の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録読解の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では SETXCF COUPLE 命令 は「SETXCF COUPLE 命令の用途を操作コマンドの表示で確認する記録読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景ではz/OS MVS Operationsの SETXCF COUPLE 命令と IEE457I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明だけに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では SETXCF COUPLE 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETXCF COUPLE,ACOUPLE=dsn**

    - 検証目的: 出力追跡の操作コマンドについて、SETXCF COUPLE,ACOUPLE=dsnは、予備 Couple DS を動的に追加し、PSWITCH で本番側に昇格させる無停止切替手順を構成するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF COUPLE,ACOUを指定し、OSKB020048の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETXCF COUPLE,ACOU
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETXCF COUPLE,ACOU
    CASE OSKB020048
    SOURCE z/OS MVS Operations
    ```

    SETXCF COUPLE,ACOUとOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020048を同じ出力で読み、出力追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020048 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020048   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SETXCF COUPLE,ACOU と OSKB020048 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETXCF MODIFY,STRNAME=name {#c22-i0268}
*分類: SET XCF*  ・  難易度: 中級

SETXCF MODIFY,STRNAME=nameは、CF 構造のサイズ・配置を動的に変更する (リビルド要因)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先読解の操作コマンドに関する SETXCF MODIFY 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず優先読解の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先読解の操作コマンドの証跡として保存して根拠にする。
    - C. SETXCF MODIFY 命令の変更点を出力本文から切り離して優先読解の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では SETXCF MODIFY 命令 は「SETXCF MODIFY 命令の状態と出力メッセージを結び付ける優先読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では SETXCF MODIFY 命令の出力行と IEE457I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明だけに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では SETXCF MODIFY 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETXCF MODIFY,STRNAME=name**

    - 検証目的: 上書追跡の操作コマンドについて、SETXCF MODIFY,STRNAME=nameは、CF 構造のサイズ・配置を動的に変更する (リビルド要因)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、上書追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF MODIFY,STRNを指定し、OSKB020047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETXCF MODIFY,STRN
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETXCF MODIFY,STRN
    CASE OSKB020047
    SOURCE z/OS MVS Operations
    ```

    SETXCF MODIFY,STRNとOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020047 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020047   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SETXCF MODIFY,STRN と OSKB020047 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETXCF START,POLICY,TYPE=type {#c22-i0269}
*分類: SET XCF*  ・  難易度: 上級

CFRM/SFM/LOGR/ARM の新規ポリシーを活性化する動的コマンド。SET XCF とは別系統だがセットで使われる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 範囲読解の操作コマンドで操作コマンドの運用確認を行います。SETXCF START 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲読解の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲読解の操作コマンドを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲読解の点検結果を残す。 ✅
    - D. SETXCF START 命令の属性行を読まず範囲読解の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では SETXCF START 命令 は「z/OS MVS Operationsで SETXCF START 命令の扱いを記録する範囲読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では SETXCF START 命令の表示結果と IEE457I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明だけに寄り、判定名は範囲読解不足です。範囲読解資料では SETXCF START 命令の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETXCF START,POLICY,TYPE=type**

    - 検証目的: 探索追跡の操作コマンドについて、CFRM/SFM/LOGR/ARM の新規ポリシーを活性化する動的コマンド。SET XCF とは別系統だがセットで使われるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF START,POLICを指定し、OSKB020046の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETXCF START,POLIC
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETXCF START,POLIC
    CASE OSKB020046
    SOURCE z/OS MVS Operations
    ```

    SETXCF START,POLICとOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020046 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020046   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SETXCF START,POLIC と OSKB020046 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > STOPMN

### STOPMN JOBNAMES {#c22-i0270}
*分類: STOPMN*  ・  難易度: 中級

STOPMN JOBNAMESは、MVS オペレータコマンドのSTOPMNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力判定の操作コマンドに関する STOPMN JOBNAMES の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力判定の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の操作コマンドの証跡として保存して根拠にする。
    - C. STOPMN JOBNAMES の変更点を出力本文から切り離して出力判定の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定の操作コマンドにおいて選択記号 D を採用し、識別名は出力判定です。出力判定の操作コマンドにおいて STOPMN JOBNAMES は説明欄の「STOPMN JOBNAMES の状態と出力メッセージを結び付ける出力判定項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力判定です。出力判定の操作コマンドに関する記録は、STOPMN JOBNAMES の出力行と IEE457I を一緒に保存し、背景名は出力判定です。選択肢ごとの違いを示します。 A: 出力判定の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力判定ではありません。 B: 出力判定の操作コマンドは別カテゴリの確認を流用しており、STOPMN JOBNAMES の根拠にならないため出力判定ではありません。 C: 出力判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力判定ではありません。 D: 出力判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力判定です。出力判定の操作コマンドで記録する STOPMN JOBNAMES はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **STOPMN JOBNAMES**

    - 検証目的: 構文検査の操作コマンドについて、STOPMN JOBNAMES は、MVS オペレータコマンドの STOPMN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030061の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、構文検査の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSTOPMN JOBNAMESを指定し、OSKB030061の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND STOPMN JOBNAMES
    CASE OSKB030061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM STOPMN JOBNAMES
    CASE OSKB030061
    SOURCE z/OS MVS Operations
    ```

    STOPMN JOBNAMESとOSKB030061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030061を同じ出力で読み、構文検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030061
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030061 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030061   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の STOPMN JOBNAMES と OSKB030061 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### STOPMN STATUS {#c22-i0271}
*分類: STOPMN*  ・  難易度: 中級

STOPMN STATUSは、MVS オペレータコマンドのSTOPMNで確認する項目です。MN STATUS を停止する。継続使用は SYSLOG 肥大化のため必要に応じてオフにする

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件判定の操作コマンドに関係する STOPMN STATUS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件判定として残す。 ✅
    - B. STOPMN STATUS の名称と担当者名のみを残して条件判定の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件判定の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件判定の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定の操作コマンドにおいて選択記号 A を採用し、識別名は条件判定です。条件判定の操作コマンドにおいて STOPMN STATUS は説明欄の「STOPMN STATUS の用途を操作コマンドの表示で確認する条件判定項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は条件判定です。条件判定の操作コマンドに関連して、z/OS MVS Operationsでは STOPMN STATUS の表示属性と IEE457I を同じ証跡に残し、背景名は条件判定です。他の選択肢を確認します。 A: 条件判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件判定です。 B: 条件判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件判定ではありません。 C: 条件判定の操作コマンドは別カテゴリの確認を流用しており、STOPMN STATUS の根拠にならないため条件判定ではありません。 D: 条件判定の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため条件判定ではありません。条件判定の操作コマンドで使う STOPMN STATUS という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **STOPMN STATUS**

    - 検証目的: 展開検査の操作コマンドについて、STOPMN STATUS は、MVS オペレータコマンドの STOPMN で確認する項目です。MN STATUS を停止する。継続使用は SYSLOG 肥大化のため必要に応じてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030062の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、展開検査の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSTOPMN STATUSを指定し、OSKB030062の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND STOPMN STATUS
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM STOPMN STATUS
    CASE OSKB030062
    SOURCE z/OS MVS Operations
    ```

    STOPMN STATUSとOSKB030062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030062を同じ出力で読み、展開検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030062 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030062   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の STOPMN STATUS と OSKB030062 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SYMBOL

### &SYSCLONE {#c22-i0272}
*分類: SYMBOL*  ・  難易度: 中級

&SYSCLONEは、MVS オペレータコマンドのSYMBOLで確認する項目です。SYSNAME の 2 桁短縮 (CLONE) を返すシステム・シンボル。DSN プレフィックス分離などに使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 比較検査の操作コマンドで&SYSCLONE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. &SYSCLONE の出力を取らず比較検査の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較検査の確認結果にする。 ✅
    - C. D A,L を省略して比較検査の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査の操作コマンドにおいて選択記号 B を採用し、識別名は比較検査です。比較検査の操作コマンドにおいて&SYSCLONE は説明欄の「比較検査の操作コマンドに関係する定義値と表示行を照合する比較検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較検査です。比較検査の操作コマンドの証跡を読む担当者は、&SYSCLONE の属性行と IEE115I を合わせて追跡し、背景名は比較検査です。誤答側の問題点を分けます。 A: 比較検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較検査ではありません。 B: 比較検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較検査です。 C: 比較検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較検査ではありません。 D: 比較検査の操作コマンドは別カテゴリの確認を流用しており、&SYSCLONE の根拠にならないため比較検査ではありません。比較検査の操作コマンドに出る&SYSCLONE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSCLONE**

    - 検証目的: 上書追跡の操作コマンドについて、&SYSCLONE は、MVS オペレータコマンドの SYMBOL で確認する項目です。SYSNAME の 2 桁短縮 (CLONE) を返すシステム・シンボル。DSN プレフィに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030047の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSCLONEを指定し、OSKB030047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSCLONE
    CASE OSKB030047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSCLONE
    CASE OSKB030047
    SOURCE z/OS MVS Operations
    ```

    &SYSCLONEとOSKB030047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030047 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030047   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSCLONE と OSKB030047 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### &SYSNAME {#c22-i0273}
*分類: SYMBOL*  ・  難易度: 中級

&SYSNAMEは、MVS オペレータコマンドのSYMBOLで確認する項目です。Sysplex システム名を返すシステム・シンボル。PARMLIB / JCL / EXEC の汎用化に最頻出

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先検査の操作コマンドに関する&SYSNAME の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先検査の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の操作コマンドの証跡として保存して根拠にする。
    - C. &SYSNAME の変更点を出力本文から切り離して優先検査の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査の操作コマンドにおいて選択記号 D を採用し、識別名は優先検査です。優先検査の操作コマンドにおいて&SYSNAME は説明欄の「&SYSNAME の状態と出力メッセージを結び付ける優先検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査の操作コマンドに関する記録は、&SYSNAME の出力行と IEE115I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先検査ではありません。 B: 優先検査の操作コマンドは別カテゴリの確認を流用しており、&SYSNAME の根拠にならないため優先検査ではありません。 C: 優先検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査の操作コマンドで記録する&SYSNAME はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSNAME**

    - 検証目的: 終端追跡の操作コマンドについて、&SYSNAME は、MVS オペレータコマンドの SYMBOL で確認する項目です。Sysplex システム名を返すシステム・シンボル。PARMLIB / JCL / EXECに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030045の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSNAMEを指定し、OSKB030045の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSNAME
    CASE OSKB030045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSNAME
    CASE OSKB030045
    SOURCE z/OS MVS Operations
    ```

    &SYSNAMEとOSKB030045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030045 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030045   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSNAME と OSKB030045 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### &SYSPLEX {#c22-i0274}
*分類: SYMBOL*  ・  難易度: 中級

&SYSPLEXは、MVS オペレータコマンドのSYMBOLで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 記録検査の操作コマンドに関係する&SYSPLEX の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録検査として残す。 ✅
    - B. &SYSPLEX の名称と担当者名のみを残して記録検査の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で記録検査の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず記録検査の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査の操作コマンドにおいて選択記号 A を採用し、識別名は記録検査です。記録検査の操作コマンドにおいて&SYSPLEX は説明欄の「&SYSPLEX の用途を操作コマンドの表示で確認する記録検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録検査です。記録検査の操作コマンドに関連して、z/OS MVS Operationsでは&SYSPLEX の表示属性と IEE115I を同じ証跡に残し、背景名は記録検査です。他の選択肢を確認します。 A: 記録検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録検査です。 B: 記録検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録検査ではありません。 C: 記録検査の操作コマンドは別カテゴリの確認を流用しており、&SYSPLEX の根拠にならないため記録検査ではありません。 D: 記録検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録検査ではありません。記録検査の操作コマンドで使う&SYSPLEX という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSPLEX**

    - 検証目的: 探索追跡の操作コマンドについて、&SYSPLEX は、MVS オペレータコマンドの SYMBOL で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030046の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、探索追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSPLEXを指定し、OSKB030046の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSPLEX
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSPLEX
    CASE OSKB030046
    SOURCE z/OS MVS Operations
    ```

    &SYSPLEXとOSKB030046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030046 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030046   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSPLEX と OSKB030046 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### &SYSR1 {#c22-i0275}
*分類: SYMBOL*  ・  難易度: 中級

&SYSR1は、MVS オペレータコマンドのSYMBOLで確認する項目です。IPL 装置のボリュームシリアル (SYSRES) を返すシステム・シンボル。PARMLIB 直接参照時に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序検査の操作コマンドで操作コマンドの運用確認を行います。&SYSR1 の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序検査の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず順序検査の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序検査の記録として扱う。 ✅
    - D. &SYSR1 の属性行を読まず順序検査の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査の操作コマンドにおいて選択記号 C を採用し、識別名は順序検査です。順序検査の操作コマンドにおいて&SYSR1 は説明欄の「z/OS MVS Operationsで&SYSR1 の扱いを記録する順序検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序検査です。順序検査の操作コマンドを受け取る担当者は、&SYSR1 の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序検査です。不適切な選択肢を整理します。 A: 順序検査の操作コマンドは別カテゴリの確認を流用しており、&SYSR1 の根拠にならないため順序検査ではありません。 B: 順序検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序検査ではありません。 C: 順序検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので順序検査です。 D: 順序検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序検査ではありません。順序検査の操作コマンドが示す&SYSR1 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSR1**

    - 検証目的: 出力追跡の操作コマンドについて、&SYSR1 は、MVS オペレータコマンドの SYMBOL で確認する項目です。IPL 装置のボリュームシリアル (SYSRES) を返すシステム・シンボル。PARMLIB 直に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030048の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、出力追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSR1を指定し、OSKB030048の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSR1
    CASE OSKB030048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSR1
    CASE OSKB030048
    SOURCE z/OS MVS Operations
    ```

    &SYSR1とOSKB030048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030048を同じ出力で読み、出力追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030048 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030048   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSR1 と OSKB030048 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### D SYMBOLS 表示 {#c22-i0276}
*分類: SYMBOL*  ・  難易度: 中級

D SYMBOLS 表示は、MVS オペレータコマンドのSYMBOLで確認する項目です。現在解決可能なシステム・シンボルとその値を一覧表示するコマンド。PARMLIB の汎用化チェックに必須

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 値域検査の表示に関する D SYMBOLS 表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域検査の表示の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の表示の証跡として保存して根拠にする。
    - C. D SYMBOLS 表示の変更点を出力本文から切り離して値域検査の表示の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査の表示において選択記号 D を採用し、識別名は値域検査です。値域検査の表示において D SYMBOLS 表示 は説明欄の「D SYMBOLS 表示の状態と出力メッセージを結び付ける値域検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査の表示に関する記録は、D SYMBOLS 表示の出力行と IEE115I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査の表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域検査ではありません。 B: 値域検査の表示は別カテゴリの確認を流用しており、D SYMBOLS 表示の根拠にならないため値域検査ではありません。 C: 値域検査の表示は名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査の表示は対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査の表示で記録する D SYMBOLS 表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **D SYMBOLS 表示**

    - 検証目的: 条件追跡の表示について、D SYMBOLS 表示は、MVS オペレータコマンドの SYMBOL で確認する項目です。現在解決可能なシステム・シンボルとその値を一覧表示するコマンド。PARMLIB の汎に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030049の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件追跡の表示の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にD SYMBOLS 表示を指定し、OSKB030049の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND D SYMBOLS 表示
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM D SYMBOLS 表示
    CASE OSKB030049
    SOURCE z/OS MVS Operations
    ```

    D SYMBOLS 表示とOSKB030049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030049を同じ出力で読み、条件追跡の表示の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030049 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030049   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の D SYMBOLS 表示 と OSKB030049 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### IEASYMxx での定義 {#c22-i0277}
*分類: SYMBOL*  ・  難易度: 中級

IEASYMxx での定義は、MVS オペレータコマンドのSYMBOLで確認する項目です。ユーザ・シンボル (&USRSYM 等) は IEASYMxx で定義する。LOAD パラメータの 3 桁目で SUFFIX を選ぶ

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告検査のでの定義に関係する IEASYMxx での定義の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告検査として残す。 ✅
    - B. IEASYMxx での定義の名称と担当者名のみを残して警告検査のでの定義の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告検査のでの定義を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告検査のでの定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査のでの定義において選択記号 A を採用し、識別名は警告検査です。警告検査のでの定義において IEASYMxx での定義 は説明欄の「IEASYMxx での定義の用途を操作コマンドの表示で確認する警告検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査のでの定義に関連して、z/OS MVS Operationsでは IEASYMxx での定義の表示属性と IEE115I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査のでの定義は対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査のでの定義は名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査のでの定義は別カテゴリの確認を流用しており、IEASYMxx での定義の根拠にならないため警告検査ではありません。 D: 警告検査のでの定義は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告検査ではありません。警告検査のでの定義で使う IEASYMxx での定義という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **IEASYMxx での定義**

    - 検証目的: 区切追跡のの定義について、IEASYMxx での定義は、MVS オペレータコマンドの SYMBOL で確認する項目です。ユーザ・シンボル (&USRSYM 等) は IEASYMxx で定義する。LOAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切追跡のの定義の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にIEASYMxx での定義を指定し、OSKB040050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IEASYMxx での定義
    CASE OSKB040050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IEASYMxx での定義
    CASE OSKB040050
    SOURCE z/OS MVS Operations
    ```

    IEASYMxx での定義とOSKB040050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040050を同じ出力で読み、区切追跡のの定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040050 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040050   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の IEASYMxx での定義 と OSKB040050 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **IEASYMxx での定義**

    - 検証目的: 区切追跡のでの定義について、IEASYMxx での定義は、MVS オペレータコマンドの SYMBOL で確認する項目です。ユーザ・シンボル (&USRSYM 等) は IEASYMxx で定義する。LOAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切追跡のでの定義の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にIEASYMxx での定義を指定し、OSKB030050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IEASYMxx での定義
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IEASYMxx での定義
    CASE OSKB030050
    SOURCE z/OS MVS Operations
    ```

    IEASYMxx での定義とOSKB030050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030050を同じ出力で読み、区切追跡のでの定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030050 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030050   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の IEASYMxx での定義 と OSKB030050 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > TRACK

### TRACK 全体 {#c22-i0278}
*分類: TRACK*  ・  難易度: 中級

TRACK 全体は、TRACK コマンドで現在稼働中のアドレス・スペース活動とハードウェア利用状況を 1 行ずつ追跡表示する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文検査の全体に関係する TRACK 全体の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文検査として残す。 ✅
    - B. TRACK 全体の名称と担当者名のみを残して構文検査の全体の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で構文検査の全体を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文検査の全体の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査の全体において選択記号 A を採用し、識別名は構文検査です。構文検査の全体において TRACK 全体 は説明欄の「TRACK 全体の用途を操作コマンドの表示で確認する構文検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文検査です。構文検査の全体に関連して、z/OS MVS Operationsでは TRACK 全体の表示属性と IEE115I を同じ証跡に残し、背景名は構文検査です。他の選択肢を確認します。 A: 構文検査の全体は対象出力と項目説明を結び、根拠を残すので構文検査です。 B: 構文検査の全体は名称や説明のみに寄り、状態を示す出力本文が不足するため構文検査ではありません。 C: 構文検査の全体は別カテゴリの確認を流用しており、TRACK 全体の根拠にならないため構文検査ではありません。 D: 構文検査の全体は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文検査ではありません。構文検査の全体で使う TRACK 全体という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **TRACK 全体**

    - 検証目的: 比較照合の全体について、TRACK 全体は、TRACK コマンドで現在稼働中のアドレス・スペース活動とハードウェア利用状況を 1 行ずつ追跡表示するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較照合の全体の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRACK 全体を指定し、OSKB030034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRACK 全体
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRACK 全体
    CASE OSKB030034
    SOURCE z/OS MVS Operations
    ```

    TRACK 全体とOSKB030034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030034を同じ出力で読み、比較照合の全体の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030034 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030034   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の TRACK 全体 と OSKB030034 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V CN

### V CN(*),ACTIVATE {#c22-i0279}
*分類: V CN*  ・  難易度: 中級

V CN(*),ACTIVATEは、全ての該当コンソールを一括処理する形式 (発行コンソール側で扱える対象に限定)

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 警告照合再の*に関係する V CN(*) 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告照合再の確認記録にまとめる。 ✅
    - B. V CN(*) 命令の名称と担当者名だけを残して警告照合再の*の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告照合再の*を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告照合再の*の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合再正解では選択記号 A を採用し、正解名は警告照合再正解です。警告照合再根拠では V CN(*) 命令 は「V CN(*) 命令の用途を操作コマンドの表示で確認する警告照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は警告照合再根拠です。警告照合再背景ではz/OS MVS Operationsの V CN(*) 命令と IEE115I を同じ証跡に残し、背景名は警告照合再背景です。他の選択肢を確認します。 A: 警告照合再正答は対象出力と項目説明を結び、根拠名は警告照合再正答です。 B: 警告照合再不足は名称や説明だけに寄り、判定名は警告照合再不足です。 C: 警告照合再流用は別カテゴリの確認であり、排除名は警告照合再流用です。 D: 警告照合再欠落は戻り値や記録番号に寄り、欠落名は警告照合再欠落です。警告照合再用語では V CN(*) 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は警告照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 監査確認の*で操作コマンドの運用確認を行います。V CN(*),ACTIVATE の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査確認の*を確認した扱いにする。
    - B. IEE115I の有無を確認せず監査確認の*を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査確認の記録として扱う。 ✅
    - D. V CN(*),ACTIVATE の属性行を読まず監査確認の*の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認の*において選択記号 C を採用し、識別名は監査確認です。監査確認の*において V CN(*),ACTIVATE は説明欄の「z/OS MVS Operationsで V CN(*),ACTIVATE の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の*を受け取る担当者は、V CN(*),ACTIVATE の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の*は別カテゴリの確認を流用しており、V CN(*),ACTIVATE の根拠にならないため監査確認ではありません。 B: 監査確認の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査確認ではありません。 C: 監査確認の*は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の*は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の*が示す V CN(*),ACTIVATE は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CN(*),ACTIVATE**

    - 検証目的: 優先整理の*について、V CN(*),ACTIVATE は、全ての該当コンソールを一括処理する形式 (発行コンソール側で扱える対象に限定)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先整理の*の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(*),ACTIVATEを指定し、OSKB020112の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(*),ACTIVATE
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(*),ACTIVATE
    CASE OSKB020112
    SOURCE z/OS MVS Operations
    ```

    V CN(*),ACTIVATEとOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020112を同じ出力で読み、優先整理の*の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020112 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020112   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(*),ACTIVATE と OSKB020112 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V CN(name),ACTIVE {#c22-i0280}
*分類: V CN*  ・  難易度: 中級

V CN(name),ACTIVEは、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにする

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 順序照合再の操作コマンドで操作コマンドの運用確認を行います。V CN(name) 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序照合再の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず順序照合再の操作コマンドを正常終了として記録する。
    - C. IEE115I を含む表示を保存し、説明欄との差分を順序照合再で確認する。 ✅
    - D. V CN(name) 命令の属性行を読まず順序照合再の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合再正解では選択記号 C を採用し、正解名は順序照合再正解です。順序照合再根拠では V CN(name) 命令 は「z/OS MVS Operationsで V CN(name) 命令の扱いを記録する順序照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は順序照合再根拠です。順序照合再受渡では V CN(name) 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序照合再受渡です。不適切な選択肢を整理します。 A: 順序照合再流用は別カテゴリの確認であり、排除名は順序照合再流用です。 B: 順序照合再欠落は戻り値や記録番号に寄り、欠落名は順序照合再欠落です。 C: 順序照合再正答は対象出力と項目説明を結び、根拠名は順序照合再正答です。 D: 順序照合再不足は名称や説明だけに寄り、判定名は順序照合再不足です。順序照合再資料では V CN(name) 命令の使い方を出典欄から追跡し、資料名は順序照合再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 警告確認の操作コマンドに関係する V CN(name),ACTIVE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 ✅
    - B. V CN(name),ACTIVE の名称と担当者名のみを残して警告確認の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告確認の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認の操作コマンドにおいて選択記号 A を採用し、識別名は警告確認です。警告確認の操作コマンドにおいて V CN(name),ACTIVE は説明欄の「V CN(name),ACTIVE の用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の操作コマンドに関連して、z/OS MVS Operationsでは V CN(name),ACTIVE の表示属性と IEE115I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),ACTIVE の根拠にならないため警告確認ではありません。 D: 警告確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告確認ではありません。警告確認の操作コマンドで使う V CN(name),ACTIVE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **V CN(name),ACTIVE**

    - 検証目的: 変更照合の操作コマンドについて、V CN(name),ACTIVE は、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにするに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040040の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),ACTIVEを指定し、OSKB040040の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),ACTIVE
    CASE OSKB040040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),ACTIVE
    CASE OSKB040040
    SOURCE z/OS MVS Operations
    ```

    V CN(name),ACTIVEとOSKB040040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040040を同じ出力で読み、変更照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040040 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040040   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),ACTIVE と OSKB040040 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **V CN(name),ACTIVE**

    - 検証目的: 区切整理の操作コマンドについて、V CN(name),ACTIVE は、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにするに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切整理の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),ACTIVEを指定し、OSKB020110の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),ACTIVE
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),ACTIVE
    CASE OSKB020110
    SOURCE z/OS MVS Operations
    ```

    V CN(name),ACTIVEとOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020110を同じ出力で読み、区切整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020110 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020110   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),ACTIVE と OSKB020110 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V CN(name),AUTH=MASTER {#c22-i0281}
*分類: V CN*  ・  難易度: 中級

V CN(name),AUTH=MASTERは、MVS オペレータコマンドのV CNで確認する項目です。コンソール権限をマスタ・コンソールに昇格させる動的変更

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 値域照合再の操作コマンドに関する V CN 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域照合再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域照合再の操作コマンドの証跡として保存して根拠にする。
    - C. V CN 属性の変更点を出力本文から切り離して値域照合再の操作コマンドの承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、値域照合再の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合再正解では選択記号 D を採用し、正解名は値域照合再正解です。値域照合再根拠では V CN 属性 は「V CN 属性の状態と出力メッセージを結び付ける値域照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は値域照合再根拠です。値域照合再保存では V CN 属性の出力行と IEE115I を一緒に残し、保存名は値域照合再保存です。選択肢ごとの違いを示します。 A: 値域照合再欠落は戻り値や記録番号に寄り、欠落名は値域照合再欠落です。 B: 値域照合再流用は別カテゴリの確認であり、排除名は値域照合再流用です。 C: 値域照合再不足は名称や説明だけに寄り、判定名は値域照合再不足です。 D: 値域照合再正答は対象出力と項目説明を結び、根拠名は値域照合再正答です。値域照合再対象では V CN 属性をz/OS MVS Operationsの確認記録に残し、対象名は値域照合再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 復旧確認の操作コマンドで V CN(name),AUTH=MASTER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V CN(name),AUTH=MASTER の出力を取らず復旧確認の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 ✅
    - C. D A,L を省略して復旧確認の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認の操作コマンドにおいて選択記号 B を採用し、識別名は復旧確認です。復旧確認の操作コマンドにおいて V CN(name),AUTH=MASTER は説明欄の「復旧確認の操作コマンドに関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の操作コマンドの証跡を読む担当者は、V CN(name),AUTH=MASTER の属性行と IEE115I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),AUTH=MASTER の根拠にならないため復旧確認ではありません。復旧確認の操作コマンドに出る V CN(name),AUTH=MASTER は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CN(name),AUTH=MASTER**

    - 検証目的: 範囲整理の操作コマンドについて、V CN(name),AUTH=MASTER は、MVS オペレータコマンドの V CN で確認する項目です。コンソール権限をマスタ・コンソールに昇格させる動的変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020111の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲整理の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),AUTH=MAを指定し、OSKB020111の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),AUTH=MA
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),AUTH=MA
    CASE OSKB020111
    SOURCE z/OS MVS Operations
    ```

    V CN(name),AUTH=MAとOSKB020111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020111を同じ出力で読み、範囲整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020111 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020111   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),AUTH=MA と OSKB020111 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V CN(name),LU=lu {#c22-i0282}
*分類: V CN*  ・  難易度: 中級

V CN(name),LU=luは、MVS オペレータコマンドのV CNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 復旧照合再の操作コマンドで V CN(name) 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V CN(name) 命令の出力を取らず復旧照合再の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧照合再の根拠にする。 ✅
    - C. D A,L を省略して復旧照合再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧照合再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合再正解では選択記号 B を採用し、正解名は復旧照合再正解です。復旧照合再根拠では V CN(name) 命令 は「復旧照合再の操作コマンドに関係する定義値と表示行を照合する復旧照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧照合再根拠です。復旧照合再追跡では V CN(name) 命令の属性行と IEE115I を合わせ、追跡名は復旧照合再追跡です。誤答側の問題点を分けます。 A: 復旧照合再不足は名称や説明だけに寄り、判定名は復旧照合再不足です。 B: 復旧照合再正答は対象出力と項目説明を結び、根拠名は復旧照合再正答です。 C: 復旧照合再欠落は戻り値や記録番号に寄り、欠落名は復旧照合再欠落です。 D: 復旧照合再流用は別カテゴリの確認であり、排除名は復旧照合再流用です。復旧照合再初出では V CN(name) 命令を MVS オペレータコマンドの運用手順で確認し、初出名は復旧照合再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 変更確認の操作コマンドに関する V CN(name),LU=luの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更確認の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の操作コマンドの証跡として保存して根拠にする。
    - C. V CN(name),LU=luの変更点を出力本文から切り離して変更確認の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認の操作コマンドにおいて選択記号 D を採用し、識別名は変更確認です。変更確認の操作コマンドにおいて V CN(name),LU=lu は説明欄の「V CN(name),LU=luの状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の操作コマンドに関する記録は、V CN(name),LU=luの出力行と IEE115I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更確認ではありません。 B: 変更確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),LU=luの根拠にならないため変更確認ではありません。 C: 変更確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の操作コマンドで記録する V CN(name),LU=luはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CN(name),LU=lu**

    - 検証目的: 記録整理の操作コマンドについて、V CN(name),LU=luは、MVS オペレータコマンドの V CN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録整理の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),LU=luを指定し、OSKB020113の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),LU=lu
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),LU=lu
    CASE OSKB020113
    SOURCE z/OS MVS Operations
    ```

    V CN(name),LU=luとOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020113を同じ出力で読み、記録整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020113 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020113   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),LU=lu と OSKB020113 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V CONSOLE

### V CONSOLE,name,ALT=name2 {#c22-i0283}
*分類: V CONSOLE*  ・  難易度: 中級

V CONSOLE,name,ALT=name2は、コンソールの代替コンソール (障害時切替先) を動的に変更する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 区切追跡再の操作コマンドで V CONSOLE 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V CONSOLE 命令の出力を取らず区切追跡再の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切追跡再の根拠にする。 ✅
    - C. D A,L を省略して区切追跡再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切追跡再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡再正解では選択記号 B を採用し、正解名は区切追跡再正解です。区切追跡再根拠では V CONSOLE 命令 は「区切追跡再の操作コマンドに関係する定義値と表示行を照合する区切追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は区切追跡再根拠です。区切追跡再追跡では V CONSOLE 命令の属性行と IEE115I を合わせ、追跡名は区切追跡再追跡です。誤答側の問題点を分けます。 A: 区切追跡再不足は名称や説明だけに寄り、判定名は区切追跡再不足です。 B: 区切追跡再正答は対象出力と項目説明を結び、根拠名は区切追跡再正答です。 C: 区切追跡再欠落は戻り値や記録番号に寄り、欠落名は区切追跡再欠落です。 D: 区切追跡再流用は別カテゴリの確認であり、排除名は区切追跡再流用です。区切追跡再初出では V CONSOLE 命令を MVS オペレータコマンドの運用手順で確認し、初出名は区切追跡再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 優先照合の操作コマンドに関する V CONSOLE,name,ALT=name2の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の操作コマンドの証跡として保存して根拠にする。
    - C. V CONSOLE,name,ALT=name2の変更点を出力本文から切り離して優先照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合の操作コマンドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合の操作コマンドにおいて V CONSOLE,name,ALT=name2 は説明欄の「V CONSOLE,name,ALT=name2の状態と出力メッセージを結び付ける優先照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の操作コマンドに関する記録は、V CONSOLE,name,ALT=name2の出力行と IEE115I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先照合ではありません。 B: 優先照合の操作コマンドは別カテゴリの確認を流用しており、V CONSOLE,name,ALT=name2の根拠にならないため優先照合ではありません。 C: 優先照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の操作コマンドで記録する V CONSOLE,name,ALT=name2はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CONSOLE,name,ALT=name2**

    - 検証目的: 終端確認の操作コマンドについて、V CONSOLE,name,ALT=name2は、コンソールの代替コンソール (障害時切替先) を動的に変更するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030005の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端確認の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CONSOLE,name,ALTを指定し、OSKB030005の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CONSOLE,name,ALT
    CASE OSKB030005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CONSOLE,name,ALT
    CASE OSKB030005
    SOURCE z/OS MVS Operations
    ```

    V CONSOLE,name,ALTとOSKB030005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030005を同じ出力で読み、終端確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030005
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030005 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030005   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CONSOLE,name,ALT と OSKB030005 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V GRS

### V GRS(ALL),RESTART {#c22-i0284}
*分類: V GRS*  ・  難易度: 中級

V GRS(ALL),RESTARTは、MVS オペレータコマンドのV GRSで確認する項目です。Sysplex 全体の GRS を一括復帰させる。リング再構成のリカバリ手段

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 探索追跡再の操作コマンドで V GRS(ALL) 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V GRS(ALL) 命令の出力を取らず探索追跡再の操作コマンドの説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索追跡再の根拠を固定する。 ✅
    - C. D OPDATA を省略して探索追跡再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索追跡再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡再正解では選択記号 B を採用し、正解名は探索追跡再正解です。探索追跡再根拠では V GRS(ALL) 命令 は「探索追跡再の操作コマンドに関係する定義値と表示行を照合する探索追跡再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は探索追跡再根拠です。探索追跡再追跡では V GRS(ALL) 命令の属性行と IEE457I を合わせ、追跡名は探索追跡再追跡です。誤答側の問題点を分けます。 A: 探索追跡再不足は名称や説明だけに寄り、判定名は探索追跡再不足です。 B: 探索追跡再正答は対象出力と項目説明を結び、根拠名は探索追跡再正答です。 C: 探索追跡再欠落は戻り値や記録番号に寄り、欠落名は探索追跡再欠落です。 D: 探索追跡再流用は別カテゴリの確認であり、排除名は探索追跡再流用です。探索追跡再初出では V GRS(ALL) 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索追跡再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 出力照合の操作コマンドに関する V GRS(ALL),RESTART の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の操作コマンドの証跡として保存して根拠にする。
    - C. V GRS(ALL),RESTART の変更点を出力本文から切り離して出力照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合の操作コマンドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合の操作コマンドにおいて V GRS(ALL),RESTART は説明欄の「V GRS(ALL),RESTART の状態と出力メッセージを結び付ける出力照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の操作コマンドに関する記録は、V GRS(ALL),RESTART の出力行と IEE457I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力照合ではありません。 B: 出力照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(ALL),RESTART の根拠にならないため出力照合ではありません。 C: 出力照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の操作コマンドで記録する V GRS(ALL),RESTART はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V GRS(ALL),RESTART**

    - 検証目的: 構文確認の操作コマンドについて、V GRS(ALL),RESTART は、MVS オペレータコマンドの V GRS で確認する項目です。Sysplex 全体の GRS を一括復帰させる。リング再構成のリカバリ手に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030001の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、構文確認の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(ALL),RESTARTを指定し、OSKB030001の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V GRS(ALL),RESTART
    CASE OSKB030001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V GRS(ALL),RESTART
    CASE OSKB030001
    SOURCE z/OS MVS Operations
    ```

    V GRS(ALL),RESTARTとOSKB030001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030001を同じ出力で読み、構文確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030001
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030001 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030001   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の V GRS(ALL),RESTART と OSKB030001 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V GRS(sysname),QUIESCE {#c22-i0285}
*分類: V GRS*  ・  難易度: 中級

V GRS(sysname),QUIESCEは、MVS オペレータコマンドのV GRSで確認する項目です。指定システムを GRS 複合体から切り離す前段階。ENQ 要求が拒否される状態に遷移

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 置換追跡再の操作コマンドに関する V GRS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず置換追跡再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換追跡再の操作コマンドの証跡として保存して根拠にする。
    - C. V GRS 属性の変更点を出力本文から切り離して置換追跡再の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換追跡再で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡再正解では選択記号 D を採用し、正解名は置換追跡再正解です。置換追跡再根拠では V GRS 属性 は「V GRS 属性の状態と出力メッセージを結び付ける置換追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は置換追跡再根拠です。置換追跡再保存では V GRS 属性の出力行と IEE115I を一緒に残し、保存名は置換追跡再保存です。選択肢ごとの違いを示します。 A: 置換追跡再欠落は戻り値や記録番号に寄り、欠落名は置換追跡再欠落です。 B: 置換追跡再流用は別カテゴリの確認であり、排除名は置換追跡再流用です。 C: 置換追跡再不足は名称や説明だけに寄り、判定名は置換追跡再不足です。 D: 置換追跡再正答は対象出力と項目説明を結び、根拠名は置換追跡再正答です。置換追跡再対象では V GRS 属性をz/OS MVS Operationsの確認記録に残し、対象名は置換追跡再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 探索照合の操作コマンドで V GRS(sysname),QUIESCE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V GRS(sysname),QUIESCE の出力を取らず探索照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 ✅
    - C. D A,L を省略して探索照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合の操作コマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の操作コマンドにおいて V GRS(sysname),QUIESCE は説明欄の「探索照合の操作コマンドに関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の操作コマンドの証跡を読む担当者は、V GRS(sysname),QUIESCE の属性行と IEE115I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索照合ではありません。 D: 探索照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(sysname),QUIESCE の根拠にならないため探索照合ではありません。探索照合の操作コマンドに出る V GRS(sysname),QUIESCE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V GRS(sysname),QUIESCE**

    - 検証目的: 監査整理の操作コマンドについて、V GRS(sysname),QUIESCE は、MVS オペレータコマンドの V GRS で確認する項目です。指定システムを GRS 複合体から切り離す前段階。ENQ 要求が拒に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査整理の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(sysname),QUIを指定し、OSKB020119の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V GRS(sysname),QUI
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V GRS(sysname),QUI
    CASE OSKB020119
    SOURCE z/OS MVS Operations
    ```

    V GRS(sysname),QUIとOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020119を同じ出力で読み、監査整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020119 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020119   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V GRS(sysname),QUI と OSKB020119 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V GRS(sysname),RESTART {#c22-i0286}
*分類: V GRS*  ・  難易度: 中級

V GRS(sysname),RESTARTは、MVS オペレータコマンドのV GRSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 終端追跡再の操作コマンドに関係する V GRS 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端追跡再の確認値として扱う。 ✅
    - B. V GRS 属性の名称と担当者名だけを残して終端追跡再の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず終端追跡再の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡再正解では選択記号 A を採用し、正解名は終端追跡再正解です。終端追跡再根拠では V GRS 属性 は「V GRS 属性の用途を操作コマンドの表示で確認する終端追跡再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は終端追跡再根拠です。終端追跡再背景ではz/OS MVS Operationsの V GRS 属性と IEE457I を同じ証跡に残し、背景名は終端追跡再背景です。他の選択肢を確認します。 A: 終端追跡再正答は対象出力と項目説明を結び、根拠名は終端追跡再正答です。 B: 終端追跡再不足は名称や説明だけに寄り、判定名は終端追跡再不足です。 C: 終端追跡再流用は別カテゴリの確認であり、排除名は終端追跡再流用です。 D: 終端追跡再欠落は戻り値や記録番号に寄り、欠落名は終端追跡再欠落です。終端追跡再用語では V GRS 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端追跡再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 上書照合の操作コマンドで操作コマンドの運用確認を行います。V GRS(sysname),RESTART の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書照合の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず上書照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書照合の記録として扱う。 ✅
    - D. V GRS(sysname),RESTART の属性行を読まず上書照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合の操作コマンドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合の操作コマンドにおいて V GRS(sysname),RESTART は説明欄の「z/OS MVS Operationsで V GRS(sysname),RESTART の扱いを記録する上書照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の操作コマンドを受け取る担当者は、V GRS(sysname),RESTART の表示結果と IEE457I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(sysname),RESTART の根拠にならないため上書照合ではありません。 B: 上書照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため上書照合ではありません。 C: 上書照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の操作コマンドが示す V GRS(sysname),RESTART は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V GRS(sysname),RESTART**

    - 検証目的: 変更整理の操作コマンドについて、V GRS(sysname),RESTART は、MVS オペレータコマンドの V GRS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、変更整理の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(sysname),RESを指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V GRS(sysname),RES
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V GRS(sysname),RES
    CASE OSKB020120
    SOURCE z/OS MVS Operations
    ```

    V GRS(sysname),RESとOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020120を同じ出力で読み、変更整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020120 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020120   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の V GRS(sysname),RES と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V PATH

### V PATH(devnum,chp),OFFLINE {#c22-i0287}
*分類: V PATH*  ・  難易度: 中級

V PATH(devnum,chp),OFFLINEは、MVS オペレータコマンドのV PATHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 条件追跡再の操作コマンドに関係する V PATH 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件追跡再の確認記録にまとめる。 ✅
    - B. V PATH 属性の名称と担当者名だけを残して条件追跡再の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件追跡再の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡再正解では選択記号 A を採用し、正解名は条件追跡再正解です。条件追跡再根拠では V PATH 属性 は「V PATH 属性の用途を操作コマンドの表示で確認する条件追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は条件追跡再根拠です。条件追跡再背景ではz/OS MVS Operationsの V PATH 属性と IEE115I を同じ証跡に残し、背景名は条件追跡再背景です。他の選択肢を確認します。 A: 条件追跡再正答は対象出力と項目説明を結び、根拠名は条件追跡再正答です。 B: 条件追跡再不足は名称や説明だけに寄り、判定名は条件追跡再不足です。 C: 条件追跡再流用は別カテゴリの確認であり、排除名は条件追跡再流用です。 D: 条件追跡再欠落は戻り値や記録番号に寄り、欠落名は条件追跡再欠落です。条件追跡再用語では V PATH 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件追跡再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 範囲照合の操作コマンドで操作コマンドの運用確認を行います。V PATH(devnum,chp),OFFLI の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲照合の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず範囲照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. V PATH(devnum,chp),OFFLI の属性行を読まず範囲照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合の操作コマンドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合の操作コマンドにおいて V PATH(devnum,chp),OFFLI は説明欄の「z/OS MVS Operationsで V PATH(devnum,chp),OFFLI の扱いを記録する範囲照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の操作コマンドを受け取る担当者は、V PATH(devnum,chp),OFFLI の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の操作コマンドは別カテゴリの確認を流用しており、V PATH(devnum,chp),OFFLI の根拠にならないため範囲照合ではありません。 B: 範囲照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の操作コマンドが示す V PATH(devnum,chp),OFFLI は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V PATH(devnum,chp),OFFLINE**

    - 検証目的: 置換確認の操作コマンドについて、V PATH(devnum,chp),OFFLINE は、MVS オペレータコマンドの V PATH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示さに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換確認の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV PATH(devnum,chp)を指定し、OSKB030004の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V PATH(devnum,chp)
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V PATH(devnum,chp)
    CASE OSKB030004
    SOURCE z/OS MVS Operations
    ```

    V PATH(devnum,chp)とOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030004を同じ出力で読み、置換確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030004 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030004   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V PATH(devnum,chp) と OSKB030004 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V PATH(devnum,chp),ONLINE {#c22-i0288}
*分類: V PATH*  ・  難易度: 中級

V PATH(devnum,chp),ONLINEは、MVS オペレータコマンドのV PATHで確認する項目です。指定装置の特定チャネル・パス (CHPID) をオンライン化する。装置レベルではなく経路レベルの制御

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力追跡再の操作コマンドに関する V PATH 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力追跡再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力追跡再の操作コマンドの証跡として保存して根拠にする。
    - C. V PATH 属性の変更点を出力本文から切り離して出力追跡再の操作コマンドの承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、出力追跡再の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡再正解では選択記号 D を採用し、正解名は出力追跡再正解です。出力追跡再根拠では V PATH 属性 は「V PATH 属性の状態と出力メッセージを結び付ける出力追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力追跡再根拠です。出力追跡再保存では V PATH 属性の出力行と IEE115I を一緒に残し、保存名は出力追跡再保存です。選択肢ごとの違いを示します。 A: 出力追跡再欠落は戻り値や記録番号に寄り、欠落名は出力追跡再欠落です。 B: 出力追跡再流用は別カテゴリの確認であり、排除名は出力追跡再流用です。 C: 出力追跡再不足は名称や説明だけに寄り、判定名は出力追跡再不足です。 D: 出力追跡再正答は対象出力と項目説明を結び、根拠名は出力追跡再正答です。出力追跡再対象では V PATH 属性をz/OS MVS Operationsの確認記録に残し、対象名は出力追跡再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切照合の操作コマンドで V PATH(devnum,chp),ONLIN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V PATH(devnum,chp),ONLIN の出力を取らず区切照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. D A,L を省略して区切照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合の操作コマンドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合の操作コマンドにおいて V PATH(devnum,chp),ONLIN は説明欄の「区切照合の操作コマンドに関係する定義値と表示行を照合する区切照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の操作コマンドの証跡を読む担当者は、V PATH(devnum,chp),ONLIN の属性行と IEE115I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切照合ではありません。 D: 区切照合の操作コマンドは別カテゴリの確認を流用しており、V PATH(devnum,chp),ONLIN の根拠にならないため区切照合ではありません。区切照合の操作コマンドに出る V PATH(devnum,chp),ONLIN は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V PATH(devnum,chp),ONLINE**

    - 検証目的: 呼出確認の操作コマンドについて、V PATH(devnum,chp),ONLINE は、MVS オペレータコマンドの V PATH で確認する項目です。指定装置の特定チャネル・パス (CHPID) をオンラインに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出確認の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にV PATH(devnum,chp)を指定し、OSKB030003の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V PATH(devnum,chp)
    CASE OSKB030003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V PATH(devnum,chp)
    CASE OSKB030003
    SOURCE z/OS MVS Operations
    ```

    V PATH(devnum,chp)とOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030003を同じ出力で読み、呼出確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030003
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030003 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030003   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V PATH(devnum,chp) と OSKB030003 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




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


