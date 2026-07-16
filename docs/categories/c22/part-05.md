---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (5/7)

[← MVS オペレータコマンド の概要へ戻る](index.md)


## MVS オペレータコマンド > P LLA

### P LLA 停止 {#c22-i0206}
*分類: P LLA*  ・  難易度: 中級

LLA を停止する。LNKLST ロード時に LLA 経由のメモリ・コピーが使われなくなる影響を理解した上で実施

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更検分の停止に関する P LLA 停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更検分の停止の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更検分の停止の証跡として保存して根拠にする。
    - C. P LLA 停止の変更点を出力本文から切り離して変更検分の停止の承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、変更検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では P LLA 停止 は「P LLA 停止の状態と出力メッセージを結び付ける変更検分項目」と D A,L または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では P LLA 停止の出力行と IEE115I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明だけに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では P LLA 停止をz/OS MVS Operationsの確認記録に残し、対象名は変更検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P LLA 停止**

    - 検証目的: 順序検査の停止について、LLA を停止する。LNKLST ロード時に LLA 経由のメモリ・コピーが使われなくなる影響を理解した上で実施に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序検査の停止の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にP LLA 停止を指定し、OSKB020075の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P LLA 停止
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P LLA 停止
    CASE OSKB020075
    SOURCE z/OS MVS Operations
    ```

    P LLA 停止とOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020075を同じ出力で読み、順序検査の停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020075 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020075   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P LLA 停止 と OSKB020075 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P NET

### P NET VTAM 停止 {#c22-i0207}
*分類: P NET*  ・  難易度: 上級

P NET VTAM 停止は、MVS オペレータコマンドのP NETで確認する項目です。VTAM を停止する。Z NET,QUICK と異なり、未完セッションのクリーンアップを待つ標準停止

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序検分の停止で操作コマンドの運用確認を行います。P NET VTAM 停止の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序検分の停止を確認した扱いにする。
    - B. IEE115I の有無を確認せず順序検分の停止を正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、順序検分の点検結果を残す。 ✅
    - D. P NET VTAM 停止の属性行を読まず順序検分の停止の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では P NET VTAM 停止 は「z/OS MVS Operationsで P NET VTAM 停止の扱いを記録する順序検分項目」と D A,L または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では P NET VTAM 停止の表示結果と IEE115I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明だけに寄り、判定名は順序検分不足です。順序検分資料では P NET VTAM 停止の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P NET VTAM 停止**

    - 検証目的: 区切検査の停止について、P NET VTAM 停止は、MVS オペレータコマンドの P NET で確認する項目です。VTAM を停止する。Z NET,QUICK と異なり、未完セッションのクリーンアッに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切検査の停止の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にP NET VTAM 停止を指定し、OSKB020070の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P NET VTAM 停止
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P NET VTAM 停止
    CASE OSKB020070
    SOURCE z/OS MVS Operations
    ```

    P NET VTAM 停止とOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020070を同じ出力で読み、区切検査の停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020070 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020070   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P NET VTAM 停止 と OSKB020070 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P SCH

### P ASCH スケジューラ停止 {#c22-i0208}
*分類: P SCH*  ・  難易度: 中級

P ASCH スケジューラ停止は、MVS オペレータコマンドのP SCHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文確認再のスケジューラ停止に関係する P ASCH スケジューラ停止の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文確認再の確認記録にまとめる。 ✅
    - B. P ASCH スケジューラ停止の名称と担当者名だけを残して構文確認再のスケジューラ停止の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文確認再のスケジューラ停止を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文確認再のスケジューラ停止の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認再正解では選択記号 A を採用し、正解名は構文確認再正解です。構文確認再根拠では P ASCH スケジューラ停止 は「P ASCH スケジューラ停止の用途を操作コマンドの表示で確認する構文確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は構文確認再根拠です。構文確認再背景ではz/OS MVS Operationsの P ASCH スケジューラ停止と IEE115I を同じ証跡に残し、背景名は構文確認再背景です。他の選択肢を確認します。 A: 構文確認再正答は対象出力と項目説明を結び、根拠名は構文確認再正答です。 B: 構文確認再不足は名称や説明だけに寄り、判定名は構文確認再不足です。 C: 構文確認再流用は別カテゴリの確認であり、排除名は構文確認再流用です。 D: 構文確認再欠落は戻り値や記録番号に寄り、欠落名は構文確認再欠落です。構文確認再用語では P ASCH スケジューラ停止を MVS オペレータコマンドで扱う確認対象とし、用語名は構文確認再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P ASCH スケジューラ停止**

    - 検証目的: 値域検査のスケジューラ停止について、P ASCH スケジューラ停止は、MVS オペレータコマンドの P SCH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020076の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域検査のスケジューラ停止の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にP ASCH スケジューラ停止を指定し、OSKB020076の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P ASCH スケジューラ停止
    CASE OSKB020076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P ASCH スケジューラ停止
    CASE OSKB020076
    SOURCE z/OS MVS Operations
    ```

    P ASCH スケジューラ停止とOSKB020076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020076を同じ出力で読み、値域検査のスケジューラ停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020076
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020076 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020076   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P ASCH スケジューラ停止 と OSKB020076 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P TRACE

### P TRACE = TRACE CT,OFF {#c22-i0209}
*分類: P TRACE*  ・  難易度: 上級

コンポーネント・トレースを停止する場合は TRACE CT,OFF,COMP=name を使う (P TRACE は使わない)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧検分の操作コマンドで P 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. P 属性の出力を取らず復旧検分の操作コマンドの説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧検分の根拠を固定する。 ✅
    - C. D A,L を省略して復旧検分の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧検分の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では P 属性 は「復旧検分の操作コマンドに関係する定義値と表示行を照合する復旧検分項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では P 属性の属性行と IEE115I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明だけに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では P 属性を MVS オペレータコマンドの運用手順で確認し、初出名は復旧検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P TRACE = TRACE CT,OFF**

    - 検証目的: 記録検査の操作コマンドについて、コンポーネント・トレースを停止する場合は TRACE CT,OFF,COMP=name を使う (P TRACE は使わない)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録検査の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にP TRACE = TRACE CTを指定し、OSKB020073の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P TRACE = TRACE CT
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P TRACE = TRACE CT
    CASE OSKB020073
    SOURCE z/OS MVS Operations
    ```

    P TRACE = TRACE CTとOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020073を同じ出力で読み、記録検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020073 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020073   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P TRACE = TRACE CT と OSKB020073 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P TSO

### P TSO サブシステム停止 {#c22-i0210}
*分類: P TSO*  ・  難易度: 中級

P TSO サブシステム停止は、MVS オペレータコマンドのP TSOで確認する項目です。TSO/E サブシステムを停止し、新規 LOGON を拒否する。既存ユーザに事前通知が必要

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告検分のサブシステム停止に関係する P TSO サブシステム停止の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告検分の確認値として扱う。 ✅
    - B. P TSO サブシステム停止の名称と担当者名だけを残して警告検分のサブシステム停止の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告検分のサブシステム停止を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告検分のサブシステム停止の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では P TSO サブシステム停止 は「P TSO サブシステム停止の用途を操作コマンドの表示で確認する警告検分項目」と D A,L または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景ではz/OS MVS Operationsの P TSO サブシステム停止と IEE115I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明だけに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では P TSO サブシステム停止を MVS オペレータコマンドで扱う確認対象とし、用語名は警告検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P TSO サブシステム停止**

    - 検証目的: 優先検査のサブシステム停止について、P TSO サブシステム停止は、MVS オペレータコマンドの P TSO で確認する項目です。TSO/E サブシステムを停止し、新規 LOGON を拒否する。既存ユーザに事前通に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先検査のサブシステム停止の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にP TSO サブシステム停止を指定し、OSKB020072の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P TSO サブシステム停止
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P TSO サブシステム停止
    CASE OSKB020072
    SOURCE z/OS MVS Operations
    ```

    P TSO サブシステム停止とOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020072を同じ出力で読み、優先検査のサブシステム停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020072 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020072   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P TSO サブシステム停止 と OSKB020072 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > R

### R nn,CANCEL (DUMP) {#c22-i0211}
*分類: R*  ・  難易度: 中級

R nn,CANCEL (DUMP)は、MVS オペレータコマンドのRで状態表示や操作を行うためのコマンド関連項目です。R nn,CANCEL (DUMP)は、WTOR を出している側のジョブの規約により CANCEL や DUMP を指示できる典型応答 (例: IEA911E ダンプ続行)

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力照合再の操作コマンドに関する R nn 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力照合再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力照合再の操作コマンドの証跡として保存して根拠にする。
    - C. R nn 命令の変更点を出力本文から切り離して出力照合再の操作コマンドの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、出力照合再の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合再正解では選択記号 D を採用し、正解名は出力照合再正解です。出力照合再根拠では R nn 命令 は「R nn 命令の状態と出力メッセージを結び付ける出力照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力照合再根拠です。出力照合再保存では R nn 命令の出力行と IEE115I を一緒に残し、保存名は出力照合再保存です。選択肢ごとの違いを示します。 A: 出力照合再欠落は戻り値や記録番号に寄り、欠落名は出力照合再欠落です。 B: 出力照合再流用は別カテゴリの確認であり、排除名は出力照合再流用です。 C: 出力照合再不足は名称や説明だけに寄り、判定名は出力照合再不足です。 D: 出力照合再正答は対象出力と項目説明を結び、根拠名は出力照合再正答です。出力照合再対象では R nn 命令をz/OS MVS Operationsの確認記録に残し、対象名は出力照合再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切確認の操作コマンドで R nn,CANCEL (DUMP)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. R nn,CANCEL (DUMP)の出力を取らず区切確認の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 ✅
    - C. D A,L を省略して区切確認の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認の操作コマンドにおいて選択記号 B を採用し、識別名は区切確認です。区切確認の操作コマンドにおいて R nn,CANCEL (DUMP) は説明欄の「区切確認の操作コマンドに関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の操作コマンドの証跡を読む担当者は、R nn,CANCEL (DUMP)の属性行と IEE115I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切確認ではありません。 D: 区切確認の操作コマンドは別カテゴリの確認を流用しており、R nn,CANCEL (DUMP)の根拠にならないため区切確認ではありません。区切確認の操作コマンドに出る R nn,CANCEL (DUMP)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **R nn,CANCEL (DUMP)**

    - 検証目的: 呼出整理の操作コマンドについて、R nn,CANCEL (DUMP)は、MVS オペレータコマンドの R で状態表示や操作を行うためのコマンド関連項目です。R nn,CANCEL (DUMP)は、WTOR をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020103の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出整理の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,CANCEL (DUMP)を指定し、OSKB020103の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R nn,CANCEL (DUMP)
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R nn,CANCEL (DUMP)
    CASE OSKB020103
    SOURCE z/OS MVS Operations
    ```

    R nn,CANCEL (DUMP)とOSKB020103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020103を同じ出力で読み、呼出整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020103 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020103   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R nn,CANCEL (DUMP) と OSKB020103 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### R nn,U / R nn,'U' (Continue) {#c22-i0212}
*分類: R*  ・  難易度: 中級

R nn,U / R nn,'U' (Continue)は、MVS オペレータコマンドのRで確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メッセージの規約に従う

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 条件照合再の・に関係する R nn,U 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件照合再として引き継ぐ。 ✅
    - B. R nn,U 属性の名称と担当者名だけを残して条件照合再の・の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件照合再の・を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件照合再の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合再正解では選択記号 A を採用し、正解名は条件照合再正解です。条件照合再根拠では R nn,U 属性 は「R nn,U 属性の用途を操作コマンドの表示で確認する条件照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は条件照合再根拠です。条件照合再背景ではz/OS MVS Operationsの R nn,U 属性と IEE115I を同じ証跡に残し、背景名は条件照合再背景です。他の選択肢を確認します。 A: 条件照合再正答は対象出力と項目説明を結び、根拠名は条件照合再正答です。 B: 条件照合再不足は名称や説明だけに寄り、判定名は条件照合再不足です。 C: 条件照合再流用は別カテゴリの確認であり、排除名は条件照合再流用です。 D: 条件照合再欠落は戻り値や記録番号に寄り、欠落名は条件照合再欠落です。条件照合再用語では R nn,U 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 構文照合保守の構文照合として R nn,U / R nn,'U' (Continue) を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 構文照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解はCです。構文照合保守で扱う R nn,U / R nn,'U' (Continue) は MVS オペレータコマンド の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として R nn,U / R nn,'U' (Continue) を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **R nn,U ・ R nn,'U' (Continue)**

    - 検証目的: 監査照合の・について、R nn,U / R nn,'U' (Continue)は、MVS オペレータコマンドの R で確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040039の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査照合の・の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,U ・ R nn,'U' を指定し、OSKB040039の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R nn,U ・ R nn,'U' 
    CASE OSKB040039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R nn,U ・ R nn,'U' 
    CASE OSKB040039
    SOURCE z/OS MVS Operations
    ```

    R nn,U ・ R nn,'U' とOSKB040039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040039を同じ出力で読み、監査照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040039 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040039   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R nn,U ・ R nn,'U'  と OSKB040039 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **R nn,U ・ R nn,'U' (Continue)**

    - 検証目的: 置換整理の・について、R nn,U / R nn,'U' (Continue)は、MVS オペレータコマンドの R で確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020104の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換整理の・の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,U ・ R nn,'U' を指定し、OSKB020104の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R nn,U ・ R nn,'U' 
    CASE OSKB020104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R nn,U ・ R nn,'U' 
    CASE OSKB020104
    SOURCE z/OS MVS Operations
    ```

    R nn,U ・ R nn,'U' とOSKB020104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020104を同じ出力で読み、置換整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020104
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020104 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020104   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R nn,U ・ R nn,'U'  と OSKB020104 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### R 基本構文 R nn,'text' {#c22-i0213}
*分類: R*  ・  難易度: 初級

R 基本構文 R nn,'text'は、MVS オペレータコマンドのRで確認する項目です。未応答 WTOR (D R,L で取れた応答番号 nn) に対しテキスト応答を返す。MVS オペレーションの基本動作

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 終端照合再の基本構文に関係する R 基本構文 R nn 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端照合再の確認記録にまとめる。 ✅
    - B. R 基本構文 R nn 命令の名称と担当者名だけを残して終端照合再の基本構文の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端照合再の基本構文を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端照合再の基本構文の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 終端照合再正解では選択記号 A を採用し、正解名は終端照合再正解です。終端照合再根拠では R 基本構文 R nn 命令 は「R 基本構文 R nn 命令の用途を操作コマンドの表示で確認する終端照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は終端照合再根拠です。終端照合再背景ではz/OS MVS Operationsの R 基本構文 R nn 命令と IEE115I を同じ証跡に残し、背景名は終端照合再背景です。他の選択肢を確認します。 A: 終端照合再正答は対象出力と項目説明を結び、根拠名は終端照合再正答です。 B: 終端照合再不足は名称や説明だけに寄り、判定名は終端照合再不足です。 C: 終端照合再流用は別カテゴリの確認であり、排除名は終端照合再流用です。 D: 終端照合再欠落は戻り値や記録番号に寄り、欠落名は終端照合再欠落です。終端照合再用語では R 基本構文 R nn 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 上書確認の基本構文で操作コマンドの運用確認を行います。R 基本構文 R nn,'text'の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書確認の基本構文を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書確認の基本構文を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書確認の記録として扱う。 ✅
    - D. R 基本構文 R nn,'text'の属性行を読まず上書確認の基本構文の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書確認の基本構文において選択記号 C を採用し、識別名は上書確認です。上書確認の基本構文において R 基本構文 R nn,'text' は説明欄の「z/OS MVS Operationsで R 基本構文 R nn,'text'の扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の基本構文を受け取る担当者は、R 基本構文 R nn,'text'の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の基本構文は別カテゴリの確認を流用しており、R 基本構文 R nn,'text'の根拠にならないため上書確認ではありません。 B: 上書確認の基本構文は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書確認ではありません。 C: 上書確認の基本構文は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の基本構文が示す R 基本構文 R nn,'text'は出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **R 基本構文 R nn,'text'**

    - 検証目的: 変更判定の基本構文について、R 基本構文 R nn,'text'は、MVS オペレータコマンドの R で確認する項目です。未応答 WTOR (D R,L で取れた応答番号 nn) に対しテキスト応答を返すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020100の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更判定の基本構文の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にR 基本構文 R nn,'text'を指定し、OSKB020100の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R 基本構文 R nn,'text'
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R 基本構文 R nn,'text'
    CASE OSKB020100
    SOURCE z/OS MVS Operations
    ```

    R 基本構文 R nn,'text'とOSKB020100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020100を同じ出力で読み、変更判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020100 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020100   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R 基本構文 R nn,'text' と OSKB020100 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 応答テキストの引用符 {#c22-i0214}
*分類: R*  ・  難易度: 中級

応答テキストの引用符は、MVS オペレータコマンドのRで確認する項目です。空白・カンマ等を含む応答は単一引用符で囲む。引用符内の引用符は二重指定でエスケープ

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書照合再の応答テキストの引用符で操作コマンドの運用確認を行います。応答テキストの引用符の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書照合再の応答テキストの引用符を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書照合再の応答テキストの引用符を正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、上書照合再の結果として保存する。 ✅
    - D. 応答テキストの引用符の属性行を読まず上書照合再の応答テキストの引用符の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合再正解では選択記号 C を採用し、正解名は上書照合再正解です。上書照合再根拠では応答テキストの引用符は「z/OS MVS Operationsで応答テキストの引用符の扱いを記録する上書照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は上書照合再根拠です。上書照合再受渡では応答テキストの引用符の表示結果と IEE115I を同じ確認単位にし、受渡名は上書照合再受渡です。不適切な選択肢を整理します。 A: 上書照合再流用は別カテゴリの確認であり、排除名は上書照合再流用です。 B: 上書照合再欠落は戻り値や記録番号に寄り、欠落名は上書照合再欠落です。 C: 上書照合再正答は対象出力と項目説明を結び、根拠名は上書照合再正答です。 D: 上書照合再不足は名称や説明だけに寄り、判定名は上書照合再不足です。上書照合再資料では応答テキストの引用符の使い方を出典欄から追跡し、資料名は上書照合再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件確認の応答テキストの引用符に関係する応答テキストの引用符の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 ✅
    - B. 応答テキストの引用符の名称と担当者名のみを残して条件確認の応答テキストの引用符の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件確認の応答テキストの引用符を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件確認の応答テキストの引用符の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認の応答テキストの引用符において選択記号 A を採用し、識別名は条件確認です。条件確認の応答テキストの引用符において応答テキストの引用符は説明欄の「応答テキストの引用符の用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の応答テキストの引用符に関連して、z/OS MVS Operationsでは応答テキストの引用符の表示属性と IEE115I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の応答テキストの引用符は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の応答テキストの引用符は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の応答テキストの引用符は別カテゴリの確認を流用しており、応答テキストの引用符の根拠にならないため条件確認ではありません。 D: 条件確認の応答テキストの引用符は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件確認ではありません。条件確認の応答テキストの引用符で使う応答テキストの引用符という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **応答テキストの引用符**

    - 検証目的: 展開整理の応答テキストの引用符について、応答テキストの引用符は、MVS オペレータコマンドの R で確認する項目です。空白・カンマ等を含む応答は単一引用符で囲む。引用符内の引用符は二重指定でエスケープに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020102の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開整理の応答テキストの引用符の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に応答テキストの引用符を指定し、OSKB020102の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 応答テキストの引用符
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 応答テキストの引用符
    CASE OSKB020102
    SOURCE z/OS MVS Operations
    ```

    応答テキストの引用符とOSKB020102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020102を同じ出力で読み、展開整理の応答テキストの引用符の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020102 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020102   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の 応答テキストの引用符 と OSKB020102 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 応答番号 nn の形式 {#c22-i0215}
*分類: R*  ・  難易度: 中級

応答番号 nn の形式は、MVS オペレータコマンドのRで確認する項目です。nn は 00〜99 (1, 2 桁) を表示時の番号で指定する。番号は WTOR 単位に動的割当てされ、応答後は再利用される

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 探索照合再の応答番号 の形式で応答番号 nn の形式の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 応答番号 nn の形式の出力を取らず探索照合再の応答番号 の形式の説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索照合再の根拠にする。 ✅
    - C. D A,L を省略して探索照合再の応答番号 の形式の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索照合再の応答番号 の形式へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合再正解では選択記号 B を採用し、正解名は探索照合再正解です。探索照合再根拠では応答番号 nn の形式 は「探索照合再の応答番号 の形式に関係する定義値と表示行を照合する探索照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は探索照合再根拠です。探索照合再追跡では応答番号 nn の形式の属性行と IEE115I を合わせ、追跡名は探索照合再追跡です。誤答側の問題点を分けます。 A: 探索照合再不足は名称や説明だけに寄り、判定名は探索照合再不足です。 B: 探索照合再正答は対象出力と項目説明を結び、根拠名は探索照合再正答です。 C: 探索照合再欠落は戻り値や記録番号に寄り、欠落名は探索照合再欠落です。 D: 探索照合再流用は別カテゴリの確認であり、排除名は探索照合再流用です。探索照合再初出では応答番号 nn の形式を MVS オペレータコマンドの運用手順で確認し、初出名は探索照合再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 出力確認の応答番号 の形式に関する応答番号 nn の形式の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力確認の応答番号 の形式の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の応答番号 の形式の証跡として保存して根拠にする。
    - C. 応答番号 nn の形式の変更点を出力本文から切り離して出力確認の応答番号 の形式の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認の応答番号 の形式において選択記号 D を採用し、識別名は出力確認です。出力確認の応答番号 の形式において応答番号 nn の形式 は説明欄の「応答番号 nn の形式の状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の応答番号 の形式に関する記録は、応答番号 nn の形式の出力行と IEE115I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の応答番号 の形式は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力確認ではありません。 B: 出力確認の応答番号 の形式は別カテゴリの確認を流用しており、応答番号 nn の形式の根拠にならないため出力確認ではありません。 C: 出力確認の応答番号 の形式は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の応答番号 の形式は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の応答番号 の形式で記録する応答番号 nn の形式はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **応答番号 nn の形式**

    - 検証目的: 構文整理の応答番号 の形式について、応答番号 nn の形式は、MVS オペレータコマンドの R で確認する項目です。nn は 00〜99 (1, 2 桁) を表示時の番号で指定する。番号は WTOR 単位に動的割に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文整理の応答番号 の形式の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に応答番号 nn の形式を指定し、OSKB020101の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 応答番号 nn の形式
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 応答番号 nn の形式
    CASE OSKB020101
    SOURCE z/OS MVS Operations
    ```

    応答番号 nn の形式とOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020101を同じ出力で読み、構文整理の応答番号 の形式の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020101 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020101   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の 応答番号 nn の形式 と OSKB020101 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > ROUTE

### ROUTE (sys1,sys2),cmd {#c22-i0216}
*分類: ROUTE*  ・  難易度: 中級

ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドのROUTEで確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査追跡の操作コマンドで操作コマンドの運用確認を行います。ROUTE (sys1,sys2),cmdの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査追跡の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査追跡の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査追跡の記録として扱う。 ✅
    - D. ROUTE (sys1,sys2),cmdの属性行を読まず監査追跡の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査追跡の操作コマンドにおいて選択記号 C を採用し、識別名は監査追跡です。監査追跡の操作コマンドにおいて ROUTE (sys1,sys2),cmd は説明欄の「z/OS MVS Operationsで ROUTE (sys1,sys2),cmdの扱いを記録する監査追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査追跡です。監査追跡の操作コマンドを受け取る担当者は、ROUTE (sys1,sys2),cmdの表示結果と IEE115I を同じ確認単位として扱い、背景名は監査追跡です。不適切な選択肢を整理します。 A: 監査追跡の操作コマンドは別カテゴリの確認を流用しており、ROUTE (sys1,sys2),cmdの根拠にならないため監査追跡ではありません。 B: 監査追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査追跡ではありません。 C: 監査追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査追跡です。 D: 監査追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査追跡ではありません。監査追跡の操作コマンドが示す ROUTE (sys1,sys2),cmdは出典欄の資料で使い方を追跡できる項目であり、用語名は監査追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **ROUTE (sys1,sys2),cmd**

    - 検証目的: 上書追跡の操作コマンドについて、ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドの ROUTE で確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040047の検証用出力を記録できる。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE (sys1,sys2),を指定し、OSKB040047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE (sys1,sys2),
    CASE OSKB040047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE (sys1,sys2),
    CASE OSKB040047
    SOURCE z/OS MVS Operations
    ```

    ROUTE (sys1,sys2),とOSKB040047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040047 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040047   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE (sys1,sys2), と OSKB040047 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **ROUTE (sys1,sys2),cmd**

    - 検証目的: 優先照合の操作コマンドについて、ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドの ROUTE で確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE (sys1,sys2),を指定し、OSKB030032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE (sys1,sys2),
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE (sys1,sys2),
    CASE OSKB030032
    SOURCE z/OS MVS Operations
    ```

    ROUTE (sys1,sys2),とOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030032を同じ出力で読み、優先照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030032 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030032   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE (sys1,sys2), と OSKB030032 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### ROUTE *ALL,cmd {#c22-i0217}
*分類: ROUTE*  ・  難易度: 中級

ROUTE *ALL,cmdは、MVS オペレータコマンドのROUTEで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告追跡の*に関係する ROUTE *ALL,cmdの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告追跡として残す。 ✅
    - B. ROUTE *ALL,cmdの名称と担当者名のみを残して警告追跡の*の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告追跡の*を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告追跡の*の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡の*において選択記号 A を採用し、識別名は警告追跡です。警告追跡の*において ROUTE *ALL,cmd は説明欄の「ROUTE *ALL,cmdの用途を操作コマンドの表示で確認する警告追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告追跡です。警告追跡の*に関連して、z/OS MVS Operationsでは ROUTE *ALL,cmdの表示属性と IEE115I を同じ証跡に残し、背景名は警告追跡です。他の選択肢を確認します。 A: 警告追跡の*は対象出力と項目説明を結び、根拠を残すので警告追跡です。 B: 警告追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため警告追跡ではありません。 C: 警告追跡の*は別カテゴリの確認を流用しており、ROUTE *ALL,cmdの根拠にならないため警告追跡ではありません。 D: 警告追跡の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告追跡ではありません。警告追跡の*で使う ROUTE *ALL,cmdという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **ROUTE *ALL,cmd**

    - 検証目的: 区切照合の*について、ROUTE *ALL,cmdは、MVS オペレータコマンドの ROUTE で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切照合の*の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE *ALL,cmdを指定し、OSKB030030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE *ALL,cmd
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE *ALL,cmd
    CASE OSKB030030
    SOURCE z/OS MVS Operations
    ```

    ROUTE *ALL,cmdとOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030030を同じ出力で読み、区切照合の*の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030030 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030030   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE *ALL,cmd と OSKB030030 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### ROUTE T=seconds,... {#c22-i0218}
*分類: ROUTE*  ・  難易度: 中級

ROUTE T=seconds,...は、MVS オペレータコマンドのROUTEで確認する項目です。応答待ちタイムアウトを指定。Sysplex 内応答が揃わない場合の待ち時間制御

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更追跡のなどに関する ROUTE T=seconds,などの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更追跡のなどの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡のなどの証跡として保存して根拠にする。
    - C. ROUTE T=seconds,などの変更点を出力本文から切り離して変更追跡のなどの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡のなどにおいて選択記号 D を採用し、識別名は変更追跡です。変更追跡のなどにおいて ROUTE T=seconds,など は説明欄の「ROUTE T=seconds,などの状態と出力メッセージを結び付ける変更追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更追跡です。変更追跡のなどに関する記録は、ROUTE T=seconds,などの出力行と IEE115I を一緒に保存し、背景名は変更追跡です。選択肢ごとの違いを示します。 A: 変更追跡のなどは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更追跡ではありません。 B: 変更追跡のなどは別カテゴリの確認を流用しており、ROUTE T=seconds,などの根拠にならないため変更追跡ではありません。 C: 変更追跡のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため変更追跡ではありません。 D: 変更追跡のなどは対象出力と項目説明を結び、根拠を残すので変更追跡です。変更追跡のなどで記録する ROUTE T=seconds,などはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200



### ROUTE sysname,cmd {#c22-i0219}
*分類: ROUTE*  ・  難易度: 中級

ROUTE sysname,cmdは、特定の Sysplex メンバ・システムにコマンドをルーティングする形式

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧追跡の操作コマンドで ROUTE sysname,cmdの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ROUTE sysname,cmdの出力を取らず復旧追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧追跡の確認結果にする。 ✅
    - C. D A,L を省略して復旧追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡の操作コマンドにおいて選択記号 B を採用し、識別名は復旧追跡です。復旧追跡の操作コマンドにおいて ROUTE sysname,cmd は説明欄の「復旧追跡の操作コマンドに関係する定義値と表示行を照合する復旧追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧追跡です。復旧追跡の操作コマンドの証跡を読む担当者は、ROUTE sysname,cmdの属性行と IEE115I を合わせて追跡し、背景名は復旧追跡です。誤答側の問題点を分けます。 A: 復旧追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧追跡ではありません。 B: 復旧追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧追跡です。 C: 復旧追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧追跡ではありません。 D: 復旧追跡の操作コマンドは別カテゴリの確認を流用しており、ROUTE sysname,cmdの根拠にならないため復旧追跡ではありません。復旧追跡の操作コマンドに出る ROUTE sysname,cmdは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **ROUTE sysname,cmd**

    - 検証目的: 範囲照合の操作コマンドについて、ROUTE sysname,cmdは、特定の Sysplex メンバ・システムにコマンドをルーティングする形式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE sysname,cmdを指定し、OSKB030031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE sysname,cmd
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE sysname,cmd
    CASE OSKB030031
    SOURCE z/OS MVS Operations
    ```

    ROUTE sysname,cmdとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030031を同じ出力で読み、範囲照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030031 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030031   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE sysname,cmd と OSKB030031 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S

### JOBNAME= 指定 {#c22-i0220}
*分類: S*  ・  難易度: 中級

JOBNAME= 指定は、MVS オペレータコマンドのSで確認する項目です。STC のジョブ名を明示的に指定する。同一プロシージャで複数インスタンスを区別する典型用途

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告読解の指定に関係する JOBNAME= 指定の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告読解の確認記録にまとめる。 ✅
    - B. JOBNAME= 指定の名称と担当者名だけを残して警告読解の指定の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告読解の指定を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告読解の指定の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では JOBNAME= 指定 は「JOBNAME= 指定の用途を操作コマンドの表示で確認する警告読解項目」と D A,L または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景ではz/OS MVS Operationsの JOBNAME= 指定と IEE115I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明だけに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では JOBNAME= 指定を MVS オペレータコマンドで扱う確認対象とし、用語名は警告読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **JOBNAME= 指定**

    - 検証目的: 優先追跡の指定について、JOBNAME= 指定は、MVS オペレータコマンドの S で確認する項目です。STC のジョブ名を明示的に指定する。同一プロシージャで複数インスタンスを区別する典型用途に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先追跡の指定の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にJOBNAME= 指定を指定し、OSKB020052の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND JOBNAME= 指定
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM JOBNAME= 指定
    CASE OSKB020052
    SOURCE z/OS MVS Operations
    ```

    JOBNAME= 指定とOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020052を同じ出力で読み、優先追跡の指定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020052 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020052   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の JOBNAME= 指定 と OSKB020052 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### REUSASID=YES 指定 {#c22-i0221}
*分類: S*  ・  難易度: 中級

REUSASID=YES 指定は、MVS オペレータコマンドのSで確認する項目です。新規 STC 起動時に再利用可能 ASID を割り当てる。ASID 枯渇対策時に使用する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 値域読解の指定に関する REUSASID=YES 指定の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域読解の指定の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域読解の指定の証跡として保存して根拠にする。
    - C. REUSASID=YES 指定の変更点を出力本文から切り離して値域読解の指定の承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、値域読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では REUSASID=YES 指定 は「REUSASID=YES 指定の状態と出力メッセージを結び付ける値域読解項目」と D A,L または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では REUSASID=YES 指定の出力行と IEE115I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明だけに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では REUSASID=YES 指定をz/OS MVS Operationsの確認記録に残し、対象名は値域読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **REUSASID=YES 指定**

    - 検証目的: 範囲追跡の指定について、REUSASID=YES 指定は、MVS オペレータコマンドの S で確認する項目です。新規 STC 起動時に再利用可能 ASID を割り当てる。ASID 枯渇対策時に使用するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲追跡の指定の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にREUSASID=YES 指定を指定し、OSKB020051の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND REUSASID=YES 指定
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM REUSASID=YES 指定
    CASE OSKB020051
    SOURCE z/OS MVS Operations
    ```

    REUSASID=YES 指定とOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020051を同じ出力で読み、範囲追跡の指定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020051 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020051   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の REUSASID=YES 指定 と OSKB020051 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### S コマンド基本構文 {#c22-i0222}
*分類: S*  ・  難易度: 初級

S コマンド基本構文は、MVS オペレータコマンドのSで状態表示や操作を行うためのコマンド関連項目です。S procname.identifier,parm=value の形でカタログ・プロシージャを起動する。短縮形 S。実行は新規アドレス・スペースで行われる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 比較読解のコマンド基本構文で S コマンド基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S コマンド基本構文の出力を取らず比較読解のコマンド基本構文の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較読解の根拠を固定する。 ✅
    - C. D A,L を省略して比較読解のコマンド基本構文の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較読解のコマンド基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では S コマンド基本構文 は「比較読解のコマンド基本構文に関係する定義値と表示行を照合する比較読解項目」と D A,L または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では S コマンド基本構文の属性行と IEE115I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明だけに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では S コマンド基本構文を MVS オペレータコマンドの運用手順で確認し、初出名は比較読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S コマンド基本構文**

    - 検証目的: 条件追跡のコマンド基本構文について、S コマンド基本構文は、MVS オペレータコマンドの S で状態表示や操作を行うためのコマンド関連項目です。S procname.identifier,parm=value のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件追跡のコマンド基本構文の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS コマンド基本構文を指定し、OSKB020049の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S コマンド基本構文
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S コマンド基本構文
    CASE OSKB020049
    SOURCE z/OS MVS Operations
    ```

    S コマンド基本構文とOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020049を同じ出力で読み、条件追跡のコマンド基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020049 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020049   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S コマンド基本構文 と OSKB020049 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 識別子 (identifier) の役割 {#c22-i0223}
*分類: S*  ・  難易度: 中級

識別子 (identifier) の役割は、MVS オペレータコマンドのSで確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別する。MODIFY/STOP の対象指定にも使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序読解の識別子 の役割で操作コマンドの運用確認を行います。識別子 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序読解の識別子 の役割を確認した扱いにする。
    - B. IEE457I の有無を確認せず順序読解の識別子 の役割を正常終了として記録する。
    - C. IEE457I を含む表示を保存し、説明欄との差分を順序読解で確認する。 ✅
    - D. 識別子 属性の属性行を読まず順序読解の識別子 の役割の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では識別子 属性は「z/OS MVS Operationsで識別子 属性の扱いを記録する順序読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では識別子 属性の表示結果と IEE457I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明だけに寄り、判定名は順序読解不足です。順序読解資料では識別子 属性の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **識別子 (identifier) の役割**

    - 検証目的: 区切照合の識別子 の役割について、識別子 (identifier) の役割は、MVS オペレータコマンドの S で確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、区切照合の識別子 の役割の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に識別子 (identifier) のを指定し、OSKB040030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 識別子 (identifier) の
    CASE OSKB040030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 識別子 (identifier) の
    CASE OSKB040030
    SOURCE z/OS MVS Operations
    ```

    識別子 (identifier) のとOSKB040030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040030を同じ出力で読み、区切照合の識別子 の役割の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040030 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040030   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の 識別子 (identifier) の と OSKB040030 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **識別子 (identifier) の役割**

    - 検証目的: 区切追跡の識別子 の役割について、識別子 (identifier) の役割は、MVS オペレータコマンドの S で確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、区切追跡の識別子 の役割の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄に識別子 (identifier) のを指定し、OSKB020050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 識別子 (identifier) の
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 識別子 (identifier) の
    CASE OSKB020050
    SOURCE z/OS MVS Operations
    ```

    識別子 (identifier) のとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020050を同じ出力で読み、区切追跡の識別子 の役割の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020050 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020050   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の 識別子 (identifier) の と OSKB020050 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S APPC

### S APPC APPC/MVS 起動 {#c22-i0224}
*分類: S APPC*  ・  難易度: 中級

APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 上書検分の・ 起動で操作コマンドの運用確認を行います。S APPC APPC 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書検分の・ 起動を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書検分の・ 起動を正常終了として記録する。
    - C. IEE115I を含む表示を保存し、説明欄との差分を上書検分で確認する。 ✅
    - D. S APPC APPC 属性の属性行を読まず上書検分の・ 起動の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では S APPC APPC 属性 は「z/OS MVS Operationsで S APPC APPC 属性の扱いを記録する上書検分項目」と D A,L または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では S APPC APPC 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明だけに寄り、判定名は上書検分不足です。上書検分資料では S APPC APPC 属性の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **S APPC APPC ・ MVS 起動**

    - 検証目的: 優先照合の・ 起動について、APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先照合の・ 起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS APPC APPC ・ MVS を指定し、OSKB040032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S APPC APPC ・ MVS 
    CASE OSKB040032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S APPC APPC ・ MVS 
    CASE OSKB040032
    SOURCE z/OS MVS Operations
    ```

    S APPC APPC ・ MVS とOSKB040032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040032を同じ出力で読み、優先照合の・ 起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040032 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040032   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S APPC APPC ・ MVS  と OSKB040032 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **S APPC APPC ・ MVS 起動**

    - 検証目的: 展開検査の・ 起動について、APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開検査の・ 起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS APPC APPC ・ MVS を指定し、OSKB020062の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S APPC APPC ・ MVS 
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S APPC APPC ・ MVS 
    CASE OSKB020062
    SOURCE z/OS MVS Operations
    ```

    S APPC APPC ・ MVS とOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020062を同じ出力で読み、展開検査の・ 起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020062 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020062   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S APPC APPC ・ MVS  と OSKB020062 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S CICS

### S CICS リージョン起動 {#c22-i0225}
*分類: S CICS*  ・  難易度: 上級

CICS Transaction Server のリージョンを起動。S CICSPROD.CICSPROD のように識別子で本番/開発を区別する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更読解のリージョン起動に関する S CICS リージョン起動の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更読解のリージョン起動の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更読解のリージョン起動の証跡として保存して根拠にする。
    - C. S CICS リージョン起動の変更点を出力本文から切り離して変更読解のリージョン起動の承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、変更読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では S CICS リージョン起動 は「S CICS リージョン起動の状態と出力メッセージを結び付ける変更読解項目」と D A,L または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では S CICS リージョン起動の出力行と IEE115I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明だけに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では S CICS リージョン起動をz/OS MVS Operationsの確認記録に残し、対象名は変更読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S CICS リージョン起動**

    - 検証目的: 順序追跡のリージョン起動について、CICS Transaction Server のリージョンを起動。S CICSPROD.CICSPROD のように識別子で本番/開発を区別するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序追跡のリージョン起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS CICS リージョン起動を指定し、OSKB020055の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S CICS リージョン起動
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S CICS リージョン起動
    CASE OSKB020055
    SOURCE z/OS MVS Operations
    ```

    S CICS リージョン起動とOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020055を同じ出力で読み、順序追跡のリージョン起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020055 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020055   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S CICS リージョン起動 と OSKB020055 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S DB2

### S DB2 サブシステム起動 {#c22-i0226}
*分類: S DB2*  ・  難易度: 中級

S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンド

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文検分のサブシステム起動に関係する S DB2 サブシステム起動の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文検分として引き継ぐ。 ✅
    - B. S DB2 サブシステム起動の名称と担当者名だけを残して構文検分のサブシステム起動の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文検分のサブシステム起動を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文検分のサブシステム起動の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では S DB2 サブシステム起動 は「S DB2 サブシステム起動の用途を操作コマンドの表示で確認する構文検分項目」と D A,L または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景ではz/OS MVS Operationsの S DB2 サブシステム起動と IEE115I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明だけに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では S DB2 サブシステム起動を MVS オペレータコマンドで扱う確認対象とし、用語名は構文検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **S DB2 サブシステム起動**

    - 検証目的: 範囲照合のサブシステム起動について、S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲照合のサブシステム起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DB2 サブシステム起動を指定し、OSKB040031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DB2 サブシステム起動
    CASE OSKB040031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DB2 サブシステム起動
    CASE OSKB040031
    SOURCE z/OS MVS Operations
    ```

    S DB2 サブシステム起動とOSKB040031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040031を同じ出力で読み、範囲照合のサブシステム起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040031 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040031   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DB2 サブシステム起動 と OSKB040031 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **S DB2 サブシステム起動**

    - 検証目的: 値域追跡のサブシステム起動について、S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域追跡のサブシステム起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DB2 サブシステム起動を指定し、OSKB020056の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DB2 サブシステム起動
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DB2 サブシステム起動
    CASE OSKB020056
    SOURCE z/OS MVS Operations
    ```

    S DB2 サブシステム起動とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020056を同じ出力で読み、値域追跡のサブシステム起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020056 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020056   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DB2 サブシステム起動 と OSKB020056 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S DLF

### S DLF Hiperbatch 起動 {#c22-i0227}
*分類: S DLF*  ・  難易度: 中級

S DLF Hiperbatch 起動は、MVS オペレータコマンドのS DLFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 探索検分の起動で S DLF Hiperbatch 起動の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S DLF Hiperbatch 起動の出力を取らず探索検分の起動の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索検分の根拠を固定する。 ✅
    - C. D A,L を省略して探索検分の起動の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索検分の起動へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では S DLF Hiperbatch 起動 は「探索検分の起動に関係する定義値と表示行を照合する探索検分項目」と D A,L または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では S DLF Hiperbatch 起動の属性行と IEE115I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明だけに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では S DLF Hiperbatch 起動を MVS オペレータコマンドの運用手順で確認し、初出名は探索検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S DLF Hiperbatch 起動**

    - 検証目的: 構文検査の起動について、S DLF Hiperbatch 起動は、MVS オペレータコマンドの S DLF で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文検査の起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DLF Hiperbatch 起を指定し、OSKB020061の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DLF Hiperbatch 起
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DLF Hiperbatch 起
    CASE OSKB020061
    SOURCE z/OS MVS Operations
    ```

    S DLF Hiperbatch 起とOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020061を同じ出力で読み、構文検査の起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020061 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020061   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DLF Hiperbatch 起 と OSKB020061 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S DUMPSRV

### S DUMPSRV SVC ダンプ・サービス {#c22-i0228}
*分類: S DUMPSRV*  ・  難易度: 中級

S DUMPSRV SVC ダンプ・サービスは、MVS オペレータコマンドのS DUMPSRVで確認する項目です。DUMPSRV (SVC ダンプ・サービス) を起動する。通常 IPL 時自動起動で手動の再起動用

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先検分のダンプ・サービスに関する S DUMPSRV SVC ダンプ 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先検分のダンプ・サービスの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先検分のダンプ・サービスの証跡として保存して根拠にする。
    - C. S DUMPSRV SVC ダンプ 属性の変更点を出力本文から切り離して優先検分のダンプ・サービスの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、優先検分の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では S DUMPSRV SVC ダンプ 属性 は「S DUMPSRV SVC ダンプ 属性の状態と出力メッセージを結び付ける優先検分項目」と D A,L または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では S DUMPSRV SVC ダンプ 属性の出力行と IEE115I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明だけに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では S DUMPSRV SVC ダンプ 属性をz/OS MVS Operationsの確認記録に残し、対象名は優先検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S DUMPSRV SVC ダンプ・サービス**

    - 検証目的: 上書検査のダンプ・サービスについて、S DUMPSRV SVC ダンプ・サービスは、MVS オペレータコマンドの S DUMPSRV で確認する項目です。DUMPSRV (SVC ダンプ・サービス) を起動する。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書検査のダンプ・サービスの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DUMPSRV SVC ダンプ・を指定し、OSKB020067の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DUMPSRV SVC ダンプ・
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DUMPSRV SVC ダンプ・
    CASE OSKB020067
    SOURCE z/OS MVS Operations
    ```

    S DUMPSRV SVC ダンプ・とOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020067を同じ出力で読み、上書検査のダンプ・サービスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020067 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020067   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DUMPSRV SVC ダンプ・ と OSKB020067 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S JES2

### S JES2 起動 {#c22-i0229}
*分類: S JES2*  ・  難易度: 中級

S JES2 起動は、MVS オペレータコマンドのS JES2で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 置換検分の起動に関する S JES2 起動の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず置換検分の起動の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換検分の起動の証跡として保存して根拠にする。
    - C. S JES2 起動の変更点を出力本文から切り離して置換検分の起動の承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では S JES2 起動 は「S JES2 起動の状態と出力メッセージを結び付ける置換検分項目」と D A,L または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では S JES2 起動の出力行と IEE115I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明だけに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では S JES2 起動をz/OS MVS Operationsの確認記録に残し、対象名は置換検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S JES2 起動**

    - 検証目的: 監査追跡の起動について、S JES2 起動は、MVS オペレータコマンドの S JES2 で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査追跡の起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS JES2 起動を指定し、OSKB020059の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S JES2 起動
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S JES2 起動
    CASE OSKB020059
    SOURCE z/OS MVS Operations
    ```

    S JES2 起動とOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020059を同じ出力で読み、監査追跡の起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020059 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020059   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S JES2 起動 と OSKB020059 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### S JES2,PARM='WARM,NOREQ' {#c22-i0230}
*分類: S JES2*  ・  難易度: 中級

S JES2,PARM='WARM,NOREQ'は、MVS オペレータコマンドのS JES2で確認する項目です。通常起動 (WARM) で対話プロンプトなし。運用自動化での標準形

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 終端検分の操作コマンドに関係する S JES2 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端検分の確認値として扱う。 ✅
    - B. S JES2 命令の名称と担当者名だけを残して終端検分の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端検分の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端検分の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では S JES2 命令 は「S JES2 命令の用途を操作コマンドの表示で確認する終端検分項目」と D A,L または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景ではz/OS MVS Operationsの S JES2 命令と IEE115I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明だけに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では S JES2 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S JES2,PARM='WARM,NOREQ'**

    - 検証目的: 変更追跡の操作コマンドについて、S JES2,PARM='WARM,NOREQ'は、MVS オペレータコマンドの S JES2 で確認する項目です。通常起動 (WARM) で対話プロンプトなし。運用自動化でのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS JES2,PARM='WARM,を指定し、OSKB020060の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S JES2,PARM='WARM,
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S JES2,PARM='WARM,
    CASE OSKB020060
    SOURCE z/OS MVS Operations
    ```

    S JES2,PARM='WARM,とOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020060を同じ出力で読み、変更追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020060 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020060   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S JES2,PARM='WARM, と OSKB020060 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S LLA

### S LLA Library Lookaside {#c22-i0231}
*分類: S LLA*  ・  難易度: 中級

S LLA Library Lookasideは、MVS オペレータコマンドのS LLAで用いるLLA (Library Lookaside) を起動する。LNKLST ロード性能改善の前提コンポーネント。S LLAでは、指定値と対象資源、実行時の出力を突き合わせて確認する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力検分の操作コマンドに関する S 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力検分の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力検分の操作コマンドの証跡として保存して根拠にする。
    - C. S 機能の変更点を出力本文から切り離して出力検分の操作コマンドの承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、出力検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では S 機能 は「S 機能の状態と出力メッセージを結び付ける出力検分項目」と D A,L または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では S 機能の出力行と IEE115I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明だけに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では S 機能をz/OS MVS Operationsの確認記録に残し、対象名は出力検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S LLA Library Lookaside**

    - 検証目的: 呼出検査の操作コマンドについて、S LLA Library Lookasideは、MVS オペレータコマンドの S LLA で用いる LLA (Library Lookaside) を起動する。LNKLST ロに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出検査の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS LLA Library Lookを指定し、OSKB020063の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S LLA Library Look
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S LLA Library Look
    CASE OSKB020063
    SOURCE z/OS MVS Operations
    ```

    S LLA Library LookとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020063を同じ出力で読み、呼出検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020063 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020063   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S LLA Library Look と OSKB020063 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S NET

### S NET VTAM 起動 {#c22-i0232}
*分類: S NET*  ・  難易度: 上級

S NET VTAM 起動は、MVS オペレータコマンドのS NETで状態表示や操作を行うためのコマンド関連項目です。VTAM (Communications Server) を起動する。SNA / TCP/IP のうち SNA 側および APPL 配下の前提となる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査読解の起動で操作コマンドの運用確認を行います。S NET VTAM 起動の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査読解の起動を確認した扱いにする。
    - B. IEE115I の有無を確認せず監査読解の起動を正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、監査読解の結果として保存する。 ✅
    - D. S NET VTAM 起動の属性行を読まず監査読解の起動の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では S NET VTAM 起動 は「z/OS MVS Operationsで S NET VTAM 起動の扱いを記録する監査読解項目」と D A,L または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では S NET VTAM 起動の表示結果と IEE115I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明だけに寄り、判定名は監査読解不足です。監査読解資料では S NET VTAM 起動の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S NET VTAM 起動**

    - 検証目的: 比較追跡の起動について、S NET VTAM 起動は、MVS オペレータコマンドの S NET で状態表示や操作を行うためのコマンド関連項目です。VTAM (Communications Serverに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較追跡の起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS NET VTAM 起動を指定し、OSKB020054の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S NET VTAM 起動
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S NET VTAM 起動
    CASE OSKB020054
    SOURCE z/OS MVS Operations
    ```

    S NET VTAM 起動とOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020054を同じ出力で読み、比較追跡の起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020054 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020054   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S NET VTAM 起動 と OSKB020054 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S OMVS

### S OMVS=xx {#c22-i0233}
*分類: S OMVS*  ・  難易度: 中級

S OMVS=xxは、MVS オペレータコマンドのS OMVSで確認する項目です。z/OS UNIX を BPXPRMxx 指定で初期化または再初期化する。F BPXOINIT,SHUTDOWN 後の再起動でも使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 展開検分の操作コマンドで S OMVS=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S OMVS=xxの出力を取らず展開検分の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検分の確認にする。 ✅
    - C. D A,L を省略して展開検分の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開検分の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では S OMVS=xx は「展開検分の操作コマンドに関係する定義値と表示行を照合する展開検分項目」と D A,L または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では S OMVS=xxの属性行と IEE115I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明だけに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では S OMVS=xxを MVS オペレータコマンドの運用手順で確認し、初出名は展開検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S OMVS=xx**

    - 検証目的: 警告追跡の操作コマンドについて、S OMVS=xxは、MVS オペレータコマンドの S OMVS で確認する項目です。z/OS UNIX を BPXPRMxx 指定で初期化または再初期化する。F BPXOINに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、警告追跡の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS OMVS=xxを指定し、OSKB020057の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S OMVS=xx
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S OMVS=xx
    CASE OSKB020057
    SOURCE z/OS MVS Operations
    ```

    S OMVS=xxとOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020057を同じ出力で読み、警告追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020057 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020057   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S OMVS=xx と OSKB020057 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S RACF

### S RACF/ICHRDSNT 関連 {#c22-i0234}
*分類: S RACF*  ・  難易度: 中級

RACF サブシステム・アドレス・スペース (RACF SUBSYS) を起動する。RACF コマンド・プレフィックス利用の前提

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 呼出検分の・ 関連で操作コマンドの運用確認を行います。S RACF 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出検分の・ 関連を確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出検分の・ 関連を正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出検分の点検結果を残す。 ✅
    - D. S RACF 属性の属性行を読まず呼出検分の・ 関連の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では S RACF 属性 は「z/OS MVS Operationsで S RACF 属性の扱いを記録する呼出検分項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では S RACF 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明だけに寄り、判定名は呼出検分不足です。呼出検分資料では S RACF 属性の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S RACF ・ ICHRDSNT 関連**

    - 検証目的: 復旧追跡の・ 関連について、RACF サブシステム・アドレス・スペース (RACF SUBSYS) を起動する。RACF コマンド・プレフィックス利用の前提に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、復旧追跡の・ 関連の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS RACF ・ ICHRDSNT を指定し、OSKB020058の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S RACF ・ ICHRDSNT 
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S RACF ・ ICHRDSNT 
    CASE OSKB020058
    SOURCE z/OS MVS Operations
    ```

    S RACF ・ ICHRDSNT とOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020058を同じ出力で読み、復旧追跡の・ 関連の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020058 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020058   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S RACF ・ ICHRDSNT  と OSKB020058 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S SCH

### S ASCH スケジューラ {#c22-i0235}
*分類: S SCH*  ・  難易度: 中級

S ASCH スケジューラは、MVS オペレータコマンドのS SCHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切検分のスケジューラで S ASCH スケジューラの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S ASCH スケジューラの出力を取らず区切検分のスケジューラの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検分の根拠にする。 ✅
    - C. D A,L を省略して区切検分のスケジューラの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切検分のスケジューラへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では S ASCH スケジューラ は「区切検分のスケジューラに関係する定義値と表示行を照合する区切検分項目」と D A,L または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では S ASCH スケジューラの属性行と IEE115I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明だけに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では S ASCH スケジューラを MVS オペレータコマンドの運用手順で確認し、初出名は区切検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S ASCH スケジューラ**

    - 検証目的: 終端検査のスケジューラについて、S ASCH スケジューラは、MVS オペレータコマンドの S SCH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端検査のスケジューラの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS ASCH スケジューラを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S ASCH スケジューラ
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S ASCH スケジューラ
    CASE OSKB020065
    SOURCE z/OS MVS Operations
    ```

    S ASCH スケジューラとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020065を同じ出力で読み、終端検査のスケジューラの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020065 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020065   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S ASCH スケジューラ と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S TRACE

### S TRACE,...の不在 {#c22-i0236}
*分類: S TRACE*  ・  難易度: 上級

トレースは S ではなく TRACE CT,ON / SET TRACE で開始する点に注意。S は使用しない

**出典:** z / OS MVS System Commands



## MVS オペレータコマンド > S TSO

### S TSO TSO/E 起動 {#c22-i0237}
*分類: S TSO*  ・  難易度: 中級

S TSO TSO/E 起動は、MVS オペレータコマンドのS TSOで確認する項目です。TSO/E サブシステム (TSO サブシステム・アドレス・スペース) を起動する。LOGON 受付の前提

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧読解の・ 起動で S TSO TSO ・ E 起動の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S TSO TSO ・ E 起動の出力を取らず復旧読解の・ 起動の説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧読解の根拠にする。 ✅
    - C. D A,L を省略して復旧読解の・ 起動の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧読解の・ 起動へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では S TSO TSO ・ E 起動 は「復旧読解の・ 起動に関係する定義値と表示行を照合する復旧読解項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では S TSO TSO ・ E 起動の属性行と IEE115I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明だけに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では S TSO TSO ・ E 起動を MVS オペレータコマンドの運用手順で確認し、初出名は復旧読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S TSO TSO ・ E 起動**

    - 検証目的: 記録追跡の・ 起動について、S TSO TSO/E 起動は、MVS オペレータコマンドの S TSO で確認する項目です。TSO/E サブシステム (TSO サブシステム・アドレス・スペース) を起動するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録追跡の・ 起動の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS TSO TSO ・ E 起動を指定し、OSKB020053の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S TSO TSO ・ E 起動
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S TSO TSO ・ E 起動
    CASE OSKB020053
    SOURCE z/OS MVS Operations
    ```

    S TSO TSO ・ E 起動とOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020053を同じ出力で読み、記録追跡の・ 起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020053 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020053   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S TSO TSO ・ E 起動 と OSKB020053 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S VLF

### S VLF Virtual Lookaside {#c22-i0238}
*分類: S VLF*  ・  難易度: 中級

VLF (Virtual Lookaside Facility) を起動する。CSVLLA・キャタログ・RACF の各キャッシュの前提

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件検分の操作コマンドに関係する S 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件検分の確認記録にまとめる。 ✅
    - B. S 機能の名称と担当者名だけを残して条件検分の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件検分の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件検分の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では S 機能 は「S 機能の用途を操作コマンドの表示で確認する条件検分項目」と D A,L または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景ではz/OS MVS Operationsの S 機能と IEE115I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明だけに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では S 機能を MVS オペレータコマンドで扱う確認対象とし、用語名は条件検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S VLF Virtual Lookaside**

    - 検証目的: 置換検査の操作コマンドについて、VLF (Virtual Lookaside Facility) を起動する。CSVLLA ・キャタログ・ RACF の各キャッシュの前提に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換検査の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にS VLF Virtual Lookを指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S VLF Virtual Look
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S VLF Virtual Look
    CASE OSKB020064
    SOURCE z/OS MVS Operations
    ```

    S VLF Virtual LookとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020064を同じ出力で読み、置換検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020064 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020064   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S VLF Virtual Look と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SEND

### SEND 'text',CN=(*ALL) {#c22-i0239}
*分類: SEND*  ・  難易度: 中級

SEND 'text',CN=(*ALL)は、MVS オペレータコマンドのSENDで確認する項目です。Sysplex 全コンソールに一斉送信する形式。停止予告など全員告知に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切追跡の*で SEND 'text',CN=(*ALL)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SEND 'text',CN=(*ALL)の出力を取らず区切追跡の*の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 ✅
    - C. D A,L を省略して区切追跡の*の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の*へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡の*において選択記号 B を採用し、識別名は区切追跡です。区切追跡の*において SEND 'text',CN=(*ALL) は説明欄の「区切追跡の*に関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の*の証跡を読む担当者は、SEND 'text',CN=(*ALL)の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の*は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の*は別カテゴリの確認を流用しており、SEND 'text',CN=(*ALL)の根拠にならないため区切追跡ではありません。区切追跡の*に出る SEND 'text',CN=(*ALL)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',CN=(*ALL)**

    - 検証目的: 呼出照合の*について、SEND 'text',CN=(*ALL)は、MVS オペレータコマンドの SEND で確認する項目です。Sysplex 全コンソールに一斉送信する形式。停止予告など全員告知にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030023の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出照合の*の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',CN=(*Aを指定し、OSKB030023の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',CN=(*A
    CASE OSKB030023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',CN=(*A
    CASE OSKB030023
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',CN=(*AとOSKB030023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030023を同じ出力で読み、呼出照合の*の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030023 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030023   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',CN=(*A と OSKB030023 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SEND 'text',CN=name {#c22-i0240}
*分類: SEND*  ・  難易度: 中級

SEND 'text',CN=nameは、MVS オペレータコマンドのSENDで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件追跡の操作コマンドに関係する SEND 'text',CN=nameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. SEND 'text',CN=nameの名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて SEND 'text',CN=name は説明欄の「SEND 'text',CN=nameの用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは SEND 'text',CN=nameの表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、SEND 'text',CN=nameの根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う SEND 'text',CN=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',CN=name**

    - 検証目的: 展開照合の操作コマンドについて、SEND 'text',CN=nameは、MVS オペレータコマンドの SEND で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030022の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',CN=namを指定し、OSKB030022の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',CN=nam
    CASE OSKB030022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',CN=nam
    CASE OSKB030022
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',CN=namとOSKB030022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030022を同じ出力で読み、展開照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030022
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030022 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030022   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',CN=nam と OSKB030022 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SEND 'text',NOW {#c22-i0241}
*分類: SEND*  ・  難易度: 中級

SEND 'text',NOWは、MVS オペレータコマンドのSENDで確認する項目です。即時表示モード。受信側で SAVE モードを設定しても無視して直ちに表示する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 範囲追跡の操作コマンドで操作コマンドの運用確認を行います。SEND 'text',NOW の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲追跡の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず範囲追跡の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲追跡の記録として扱う。 ✅
    - D. SEND 'text',NOW の属性行を読まず範囲追跡の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡の操作コマンドにおいて選択記号 C を採用し、識別名は範囲追跡です。範囲追跡の操作コマンドにおいて SEND 'text',NOW は説明欄の「z/OS MVS Operationsで SEND 'text',NOW の扱いを記録する範囲追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲追跡です。範囲追跡の操作コマンドを受け取る担当者は、SEND 'text',NOW の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲追跡です。不適切な選択肢を整理します。 A: 範囲追跡の操作コマンドは別カテゴリの確認を流用しており、SEND 'text',NOW の根拠にならないため範囲追跡ではありません。 B: 範囲追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲追跡ではありません。 C: 範囲追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲追跡です。 D: 範囲追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲追跡ではありません。範囲追跡の操作コマンドが示す SEND 'text',NOW は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',NOW**

    - 検証目的: 置換照合の操作コマンドについて、SEND 'text',NOW は、MVS オペレータコマンドの SEND で確認する項目です。即時表示モード。受信側で SAVE モードを設定しても無視して直ちに表示するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030024の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',NOWを指定し、OSKB030024の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',NOW
    CASE OSKB030024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',NOW
    CASE OSKB030024
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',NOWとOSKB030024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030024を同じ出力で読み、置換照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030024
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030024 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030024   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',NOW と OSKB030024 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SEND 'text',USER=userid {#c22-i0242}
*分類: SEND*  ・  難易度: 中級

SEND 'text',USER=useridは、MVS オペレータコマンドのSENDで確認する項目です。TSO ユーザに即時メッセージを送る形式。受信ユーザ側で M / N コマンドの設定が必要な点に注意

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力追跡の操作コマンドに関する SEND 'text',USER=useridの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。
    - C. SEND 'text',USER=useridの変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて SEND 'text',USER=userid は説明欄の「SEND 'text',USER=useridの状態と出力メッセージを結び付ける出力追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、SEND 'text',USER=useridの出力行と IEE115I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、SEND 'text',USER=useridの根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する SEND 'text',USER=useridはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',USER=userid**

    - 検証目的: 構文照合の操作コマンドについて、SEND 'text',USER=useridは、MVS オペレータコマンドの SEND で確認する項目です。TSO ユーザに即時メッセージを送る形式。受信ユーザ側で M /に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030021の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',USER=uを指定し、OSKB030021の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',USER=u
    CASE OSKB030021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',USER=u
    CASE OSKB030021
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',USER=uとOSKB030021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030021を同じ出力で読み、構文照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030021
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030021 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030021   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',USER=u と OSKB030021 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET DAE

### SET DAE=00 リセット {#c22-i0243}
*分類: SET DAE*  ・  難易度: 中級

SET DAE=00 リセットは、MVS オペレータコマンドのSET DAEで確認する項目です。ADYSET00 にて DAE をデフォルト状態に戻す典型的な用法。テスト中の調整から本番値に戻す際に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力分離のリセットに関する SET DAE=00 リセットの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力分離のリセットの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力分離のリセットの証跡として保存して根拠にする。
    - C. SET DAE=00 リセットの変更点を出力本文から切り離して出力分離のリセットの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では SET DAE=00 リセット は「SET DAE=00 リセットの状態と出力メッセージを結び付ける出力分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では SET DAE=00 リセットの出力行と IEE457I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明だけに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では SET DAE=00 リセットをz/OS MVS Operationsの確認記録に残し、対象名は出力分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切照合のリセットで SET DAE=00 リセットの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET DAE=00 リセットの出力を取らず区切照合のリセットの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. D OPDATA を省略して区切照合のリセットの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のリセットへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合のリセットにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のリセットにおいて SET DAE=00 リセット は説明欄の「区切照合のリセットに関係する定義値と表示行を照合する区切照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のリセットの証跡を読む担当者は、SET DAE=00 リセットの属性行と IEE457I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のリセットは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のリセットは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のリセットは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため区切照合ではありません。 D: 区切照合のリセットは別カテゴリの確認を流用しており、SET DAE=00 リセットの根拠にならないため区切照合ではありません。区切照合のリセットに出る SET DAE=00 リセットは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DAE=00 リセット**

    - 検証目的: 呼出照合のリセットについて、SET DAE=00 リセットは、MVS オペレータコマンドの SET DAE で確認する項目です。ADYSET00 にて DAE をデフォルト状態に戻す典型的な用法。テスト中に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、呼出照合のリセットの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DAE=00 リセットを指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DAE=00 リセット
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DAE=00 リセット
    CASE OSKB020023
    SOURCE z/OS MVS Operations
    ```

    SET DAE=00 リセットとOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020023を同じ出力で読み、呼出照合のリセットの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020023 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020023   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DAE=00 リセット と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET DAE=xx 目的 {#c22-i0244}
*分類: SET DAE*  ・  難易度: 初級

ADYSETxx PARMLIB メンバを動的に再活性化し、重複ダンプ抑止 (DAE) の規則を変更する。再 IPL なしで運用変更可能

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書分離の目的で操作コマンドの運用確認を行います。SET DAE=xx 目的の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書分離の目的を確認した扱いにする。
    - B. IEE457I の有無を確認せず上書分離の目的を正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、上書分離の点検結果を残す。 ✅
    - D. SET DAE=xx 目的の属性行を読まず上書分離の目的の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では SET DAE=xx 目的 は「z/OS MVS Operationsで SET DAE=xx 目的の扱いを記録する上書分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では SET DAE=xx 目的の表示結果と IEE457I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明だけに寄り、判定名は上書分離不足です。上書分離資料では SET DAE=xx 目的の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件照合の目的に関係する SET DAE=xx 目的の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. SET DAE=xx 目的の名称と担当者名のみを残して条件照合の目的の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件照合の目的を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件照合の目的の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 条件照合の目的において選択記号 A を採用し、識別名は条件照合です。条件照合の目的において SET DAE=xx 目的 は説明欄の「SET DAE=xx 目的の用途を操作コマンドの表示で確認する条件照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の目的に関連して、z/OS MVS Operationsでは SET DAE=xx 目的の表示属性と IEE457I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の目的は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の目的は別カテゴリの確認を流用しており、SET DAE=xx 目的の根拠にならないため条件照合ではありません。 D: 条件照合の目的は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため条件照合ではありません。条件照合の目的で使う SET DAE=xx 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DAE=xx 目的**

    - 検証目的: 展開照合の目的について、ADYSETxx PARMLIB メンバを動的に再活性化し、重複ダンプ抑止 (DAE) の規則を変更する。再 IPL なしで運用変更可能に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、展開照合の目的の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DAE=xx 目的を指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DAE=xx 目的
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DAE=xx 目的
    CASE OSKB020022
    SOURCE z/OS MVS Operations
    ```

    SET DAE=xx 目的とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020022を同じ出力で読み、展開照合の目的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020022 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020022   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DAE=xx 目的 と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET DUMP

### SET DUMP=NODUMP 緊急停止 {#c22-i0245}
*分類: SET DUMP*  ・  難易度: 中級

SET DUMP=NODUMP 緊急停止は、MVS オペレータコマンドのSET DUMPで確認する項目です。ダンプ生成を一時的に止める用途。容量逼迫時に応急処置として使うが、原因分析資料を失うリスクを併記

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 区切分離の緊急停止で SET 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET 属性の出力を取らず区切分離の緊急停止の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切分離の根拠を固定する。 ✅
    - C. D OPDATA を省略して区切分離の緊急停止の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切分離の緊急停止へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では SET 属性 は「区切分離の緊急停止に関係する定義値と表示行を照合する区切分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では SET 属性の属性行と IEE457I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明だけに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では SET 属性を MVS オペレータコマンドの運用手順で確認し、初出名は区切分離初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 優先照合の緊急停止に関する SET DUMP=NODUMP 緊急停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず優先照合の緊急停止の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の緊急停止の証跡として保存して根拠にする。
    - C. SET DUMP=NODUMP 緊急停止の変更点を出力本文から切り離して優先照合の緊急停止の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合の緊急停止において選択記号 D を採用し、識別名は優先照合です。優先照合の緊急停止において SET DUMP=NODUMP 緊急停止 は説明欄の「SET DUMP=NODUMP 緊急停止の状態と出力メッセージを結び付ける優先照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の緊急停止に関する記録は、SET DUMP=NODUMP 緊急停止の出力行と IEE457I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の緊急停止は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため優先照合ではありません。 B: 優先照合の緊急停止は別カテゴリの確認を流用しており、SET DUMP=NODUMP 緊急停止の根拠にならないため優先照合ではありません。 C: 優先照合の緊急停止は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の緊急停止は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の緊急停止で記録する SET DUMP=NODUMP 緊急停止はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DUMP=NODUMP 緊急停止**

    - 検証目的: 終端照合の緊急停止について、SET DUMP=NODUMP 緊急停止は、MVS オペレータコマンドの SET DUMP で確認する項目です。ダンプ生成を一時的に止める用途。容量逼迫時に応急処置として使うがに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、終端照合の緊急停止の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DUMP=NODUMP 緊急を指定し、OSKB020025の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DUMP=NODUMP 緊急
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DUMP=NODUMP 緊急
    CASE OSKB020025
    SOURCE z/OS MVS Operations
    ```

    SET DUMP=NODUMP 緊急とOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020025を同じ出力で読み、終端照合の緊急停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020025 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020025   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DUMP=NODUMP 緊急 と OSKB020025 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET DUMP=xx 目的 {#c22-i0246}
*分類: SET DUMP*  ・  難易度: 初級

SET DUMP=xx 目的は、DIAGxx などダンプ関連 PARMLIB メンバを動的活性化し、SVC ダンプの SDATA 既定や CHNGDUMP オプションを反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 条件分離の目的に関係する SET DUMP=xx 目的の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件分離の確認値として扱う。 ✅
    - B. SET DUMP=xx 目的の名称と担当者名だけを残して条件分離の目的の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件分離の目的を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件分離の目的の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では SET DUMP=xx 目的 は「SET DUMP=xx 目的の用途を操作コマンドの表示で確認する条件分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景ではz/OS MVS Operationsの SET DUMP=xx 目的と IEE457I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明だけに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では SET DUMP=xx 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は条件分離用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 範囲照合の目的で操作コマンドの運用確認を行います。SET DUMP=xx 目的の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲照合の目的を確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲照合の目的を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. SET DUMP=xx 目的の属性行を読まず範囲照合の目的の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 範囲照合の目的において選択記号 C を採用し、識別名は範囲照合です。範囲照合の目的において SET DUMP=xx 目的 は説明欄の「z/OS MVS Operationsで SET DUMP=xx 目的の扱いを記録する範囲照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の目的を受け取る担当者は、SET DUMP=xx 目的の表示結果と IEE457I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の目的は別カテゴリの確認を流用しており、SET DUMP=xx 目的の根拠にならないため範囲照合ではありません。 B: 範囲照合の目的は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の目的は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の目的が示す SET DUMP=xx 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DUMP=xx 目的**

    - 検証目的: 置換照合の目的について、SET DUMP=xx 目的は、DIAGxx などダンプ関連 PARMLIB メンバを動的活性化し、SVC ダンプの SDATA 既定や CHNGDUMP オプションを反映に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、置換照合の目的の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DUMP=xx 目的を指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DUMP=xx 目的
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DUMP=xx 目的
    CASE OSKB020024
    SOURCE z/OS MVS Operations
    ```

    SET DUMP=xx 目的とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020024を同じ出力で読み、置換照合の目的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020024 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020024   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DUMP=xx 目的 と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET IEASYS

### SET IEASYS=xx {#c22-i0247}
*分類: SET IEASYS*  ・  難易度: 中級

IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多い

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 範囲分離の操作コマンドで操作コマンドの運用確認を行います。SET IEASYS=xxの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲分離の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲分離の操作コマンドを正常終了として記録する。
    - C. IEE457I を含む表示を保存し、説明欄との差分を範囲分離で確認する。 ✅
    - D. SET IEASYS=xxの属性行を読まず範囲分離の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では SET IEASYS=xx は「z/OS MVS Operationsで SET IEASYS=xxの扱いを記録する範囲分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では SET IEASYS=xxの表示結果と IEE457I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明だけに寄り、判定名は範囲分離不足です。範囲分離資料では SET IEASYS=xxの使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 記録照合の操作コマンドに関係する SET IEASYS=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 ✅
    - B. SET IEASYS=xxの名称と担当者名のみを残して記録照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合の操作コマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の操作コマンドにおいて SET IEASYS=xx は説明欄の「IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多い」と D OPDATA または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の操作コマンドに関連して、z/OS MVS Operationsでは SET IEASYS=xxの表示属性と IEE457I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の操作コマンドは別カテゴリの確認を流用しており、SET IEASYS=xxの根拠にならないため記録照合ではありません。 D: 記録照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため記録照合ではありません。記録照合の操作コマンドで使う SET IEASYS=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **SET IEASYS=xx**

    - 検証目的: 探索照合の操作コマンドについて、IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多いに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040026の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET IEASYS=xxを指定し、OSKB040026の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET IEASYS=xx
    CASE OSKB040026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET IEASYS=xx
    CASE OSKB040026
    SOURCE z/OS MVS Operations
    ```

    SET IEASYS=xxとOSKB040026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040026
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040026 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040026   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET IEASYS=xx と OSKB040026 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **SET IEASYS=xx**

    - 検証目的: 探索照合の操作コマンドについて、IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多いに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET IEASYS=xxを指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET IEASYS=xx
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET IEASYS=xx
    CASE OSKB020026
    SOURCE z/OS MVS Operations
    ```

    SET IEASYS=xxとOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020026 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020026   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET IEASYS=xx と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET MPF

### SET MPF=(xx,yy) 連結 {#c22-i0248}
*分類: SET MPF*  ・  難易度: 中級

SET MPF=(xx,yy) 連結は、MVS オペレータコマンドのSET MPFで確認する項目です。複数 MPF メンバを連結指定。基本規則 + サイト追加分という二重構造で運用する典型形

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 記録分離の連結に関係する SET MPF=(xx 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録分離の確認記録にまとめる。 ✅
    - B. SET MPF=(xx 命令の名称と担当者名だけを残して記録分離の連結の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録分離の連結を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録分離の連結の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では SET MPF=(xx 命令 は「SET MPF=(xx 命令の用途を操作コマンドの表示で確認する記録分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景ではz/OS MVS Operationsの SET MPF=(xx 命令と IEE457I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明だけに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では SET MPF=(xx 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録分離用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 順序照合の連結で操作コマンドの運用確認を行います。SET MPF=(xx,yy) 連結の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序照合の連結を確認した扱いにする。
    - B. IEE457I の有無を確認せず順序照合の連結を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序照合の記録として扱う。 ✅
    - D. SET MPF=(xx,yy) 連結の属性行を読まず順序照合の連結の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合の連結において選択記号 C を採用し、識別名は順序照合です。順序照合の連結において SET MPF=(xx,yy) 連結 は説明欄の「z/OS MVS Operationsで SET MPF=(xx,yy) 連結の扱いを記録する順序照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の連結を受け取る担当者は、SET MPF=(xx,yy) 連結の表示結果と IEE457I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の連結は別カテゴリの確認を流用しており、SET MPF=(xx,yy) 連結の根拠にならないため順序照合ではありません。 B: 順序照合の連結は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため順序照合ではありません。 C: 順序照合の連結は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の連結は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の連結が示す SET MPF=(xx,yy) 連結は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET MPF=(xx,yy) 連結**

    - 検証目的: 出力照合の連結について、SET MPF=(xx,yy) 連結は、MVS オペレータコマンドの SET MPF で確認する項目です。複数 MPF メンバを連結指定。基本規則 + サイト追加分という二重構に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力照合の連結の確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET MPF=(xx,yy) 連結を指定し、OSKB020028の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET MPF=(xx,yy) 連結
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET MPF=(xx,yy) 連結
    CASE OSKB020028
    SOURCE z/OS MVS Operations
    ```

    SET MPF=(xx,yy) 連結とOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020028を同じ出力で読み、出力照合の連結の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020028 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020028   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET MPF=(xx,yy) 連結 と OSKB020028 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET MPF=xx {#c22-i0249}
*分類: SET MPF*  ・  難易度: 中級

SET MPF=xxは、MVS オペレータコマンドのSET MPFで用いるMPFLSTxx を動的活性化し、抑止メッセージ・自動化対象・色付け規則を更新する。最頻出 SET 系の一つ。SET MPFでは、指定値と対象資源、実行時の出力を突き合わせて確認する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 優先分離の操作コマンドに関する SET MPF=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず優先分離の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先分離の操作コマンドの証跡として保存して根拠にする。
    - C. SET MPF=xxの変更点を出力本文から切り離して優先分離の操作コマンドの承認欄だけ残す。
    - D. D OPDATA の結果から対象行を抜き出し、優先分離の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では SET MPF=xx は「SET MPF=xxの状態と出力メッセージを結び付ける優先分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では SET MPF=xxの出力行と IEE457I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明だけに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では SET MPF=xxをz/OS MVS Operationsの確認記録に残し、対象名は優先分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 比較照合の操作コマンドで SET MPF=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET MPF=xxの出力を取らず比較照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 ✅
    - C. D OPDATA を省略して比較照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合の操作コマンドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合の操作コマンドにおいて SET MPF=xx は説明欄の「比較照合の操作コマンドに関係する定義値と表示行を照合する比較照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の操作コマンドの証跡を読む担当者は、SET MPF=xxの属性行と IEE457I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため比較照合ではありません。 D: 比較照合の操作コマンドは別カテゴリの確認を流用しており、SET MPF=xxの根拠にならないため比較照合ではありません。比較照合の操作コマンドに出る SET MPF=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET MPF=xx**

    - 検証目的: 上書照合の操作コマンドについて、SET MPF=xxは、MVS オペレータコマンドの SET MPF で用いる MPFLSTxx を動的活性化し、抑止メッセージ・自動化対象・色付け規則を更新する。最頻出 SETに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、上書照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET MPF=xxを指定し、OSKB020027の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET MPF=xx
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET MPF=xx
    CASE OSKB020027
    SOURCE z/OS MVS Operations
    ```

    SET MPF=xxとOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020027 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020027   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET MPF=xx と OSKB020027 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET OMVS

### SET OMVS RESET=xx {#c22-i0250}
*分類: SET OMVS*  ・  難易度: 中級

SET OMVS RESET=xxは、MVS オペレータコマンドのSET OMVSで確認する項目です。現行設定を破棄して指定 BPXPRMxx 値で完全置換する形式。マウント情報には影響しない注意点を併記

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 順序分離の操作コマンドで操作コマンドの運用確認を行います。SET 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序分離の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず順序分離の操作コマンドを正常終了として記録する。
    - C. 同じ画面で対象行と IEE457I を読み、順序分離の結果として保存する。 ✅
    - D. SET 属性の属性行を読まず順序分離の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では SET 属性 は「z/OS MVS Operationsで SET 属性の扱いを記録する順序分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では SET 属性の表示結果と IEE457I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明だけに寄り、判定名は順序分離不足です。順序分離資料では SET 属性の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 警告照合の操作コマンドに関係する SET OMVS RESET=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 ✅
    - B. SET OMVS RESET=xxの名称と担当者名のみを残して警告照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず警告照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合の操作コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合の操作コマンドにおいて SET OMVS RESET=xx は説明欄の「SET OMVS RESET=xxの用途を操作コマンドの表示で確認する警告照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の操作コマンドに関連して、z/OS MVS Operationsでは SET OMVS RESET=xxの表示属性と IEE457I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の操作コマンドは別カテゴリの確認を流用しており、SET OMVS RESET=xxの根拠にならないため警告照合ではありません。 D: 警告照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため警告照合ではありません。警告照合の操作コマンドで使う SET OMVS RESET=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET OMVS RESET=xx**

    - 検証目的: 区切照合の操作コマンドについて、SET OMVS RESET=xxは、MVS オペレータコマンドの SET OMVS で確認する項目です。現行設定を破棄して指定 BPXPRMxx 値で完全置換する形式。マウンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、区切照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET OMVS RESET=xxを指定し、OSKB020030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET OMVS RESET=xx
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET OMVS RESET=xx
    CASE OSKB020030
    SOURCE z/OS MVS Operations
    ```

    SET OMVS RESET=xxとOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020030を同じ出力で読み、区切照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020030 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020030   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET OMVS RESET=xx と OSKB020030 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET OMVS=xx {#c22-i0251}
*分類: SET OMVS*  ・  難易度: 中級

SET OMVS=xxは、BPXPRMxx を動的活性化し、MAXPROCSYS など多くの z/OS UNIX 上限値を再 IPL なしで変更する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 比較分離の操作コマンドで SET OMVS=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET OMVS=xxの出力を取らず比較分離の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較分離の根拠にする。 ✅
    - C. D OPDATA を省略して比較分離の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較分離の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では SET OMVS=xx は「比較分離の操作コマンドに関係する定義値と表示行を照合する比較分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では SET OMVS=xxの属性行と IEE457I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明だけに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では SET OMVS=xxを MVS オペレータコマンドの運用手順で確認し、初出名は比較分離初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 値域照合の操作コマンドに関する SET OMVS=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず値域照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の操作コマンドの証跡として保存して根拠にする。
    - C. SET OMVS=xxの変更点を出力本文から切り離して値域照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合の操作コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の操作コマンドにおいて SET OMVS=xx は説明欄の「SET OMVS=xxの状態と出力メッセージを結び付ける値域照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の操作コマンドに関する記録は、SET OMVS=xxの出力行と IEE457I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため値域照合ではありません。 B: 値域照合の操作コマンドは別カテゴリの確認を流用しており、SET OMVS=xxの根拠にならないため値域照合ではありません。 C: 値域照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の操作コマンドで記録する SET OMVS=xxはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET OMVS=xx**

    - 検証目的: 条件照合の操作コマンドについて、SET OMVS=xxは、BPXPRMxx を動的活性化し、MAXPROCSYS など多くの z/OS UNIX 上限値を再 IPL なしで変更するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、条件照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET OMVS=xxを指定し、OSKB020029の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET OMVS=xx
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET OMVS=xx
    CASE OSKB020029
    SOURCE z/OS MVS Operations
    ```

    SET OMVS=xxとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020029を同じ出力で読み、条件照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020029 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020029   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET OMVS=xx と OSKB020029 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET PFK

### SET PFK=xx {#c22-i0252}
*分類: SET PFK*  ・  難易度: 中級

SET PFK=xxは、MVS オペレータコマンドのSET PFKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 値域分離の操作コマンドに関する SET PFK=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず値域分離の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域分離の操作コマンドの証跡として保存して根拠にする。
    - C. SET PFK=xxの変更点を出力本文から切り離して値域分離の操作コマンドの承認欄だけ残す。
    - D. D OPDATA で得た表示本文を使い、値域分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では SET PFK=xx は「SET PFK=xxの状態と出力メッセージを結び付ける値域分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では SET PFK=xxの出力行と IEE457I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明だけに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では SET PFK=xxをz/OS MVS Operationsの確認記録に残し、対象名は値域分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 復旧照合の操作コマンドで SET PFK=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET PFK=xxの出力を取らず復旧照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 ✅
    - C. D OPDATA を省略して復旧照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合の操作コマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の操作コマンドにおいて SET PFK=xx は説明欄の「復旧照合の操作コマンドに関係する定義値と表示行を照合する復旧照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の操作コマンドの証跡を読む担当者は、SET PFK=xxの属性行と IEE457I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の操作コマンドは別カテゴリの確認を流用しており、SET PFK=xxの根拠にならないため復旧照合ではありません。復旧照合の操作コマンドに出る SET PFK=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET PFK=xx**

    - 検証目的: 範囲照合の操作コマンドについて、SET PFK=xxは、MVS オペレータコマンドの SET PFK で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、範囲照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET PFK=xxを指定し、OSKB020031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET PFK=xx
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET PFK=xx
    CASE OSKB020031
    SOURCE z/OS MVS Operations
    ```

    SET PFK=xxとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020031を同じ出力で読み、範囲照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020031 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020031   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET PFK=xx と OSKB020031 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET PROG

### SET PROG=xx {#c22-i0253}
*分類: SET PROG*  ・  難易度: 中級

SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 警告分離の操作コマンドに関係する SET PROG=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告分離として引き継ぐ。 ✅
    - B. SET PROG=xxの名称と担当者名だけを残して警告分離の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告分離の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず警告分離の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では SET PROG=xx は「SET PROG=xxの用途を操作コマンドの表示で確認する警告分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景ではz/OS MVS Operationsの SET PROG=xxと IEE457I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明だけに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では SET PROG=xxを MVS オペレータコマンドで扱う確認対象とし、用語名は警告分離用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 監査照合の操作コマンドで操作コマンドの運用確認を行います。SET PROG=xxの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査照合の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず監査照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. SET PROG=xxの属性行を読まず監査照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合の操作コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の操作コマンドにおいて SET PROG=xx は説明欄の「z/OS MVS Operationsで SET PROG=xxの扱いを記録する監査照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の操作コマンドを受け取る担当者は、SET PROG=xxの表示結果と IEE457I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の操作コマンドは別カテゴリの確認を流用しており、SET PROG=xxの根拠にならないため監査照合ではありません。 B: 監査照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため監査照合ではありません。 C: 監査照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の操作コマンドが示す SET PROG=xxは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **SET PROG=xx**

    - 検証目的: 上書照合の操作コマンドについて、SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040027の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、上書照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET PROG=xxを指定し、OSKB040027の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET PROG=xx
    CASE OSKB040027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET PROG=xx
    CASE OSKB040027
    SOURCE z/OS MVS Operations
    ```

    SET PROG=xxとOSKB040027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040027
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040027 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040027   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET PROG=xx と OSKB040027 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **SET PROG=xx**

    - 検証目的: 優先照合の操作コマンドについて、SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、優先照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET PROG=xxを指定し、OSKB020032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET PROG=xx
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET PROG=xx
    CASE OSKB020032
    SOURCE z/OS MVS Operations
    ```

    SET PROG=xxとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020032を同じ出力で読み、優先照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020032 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020032   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET PROG=xx と OSKB020032 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG APF,ADD {#c22-i0254}
*分類: SET PROG*  ・  難易度: 中級

SETPROG APF,ADDは、MVS オペレータコマンドのSET PROGで確認する項目です。個別データセットを動的に APF 許可リストへ追加するサブコマンド。緊急のソフトウェア導入時に多用

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 復旧分離の操作コマンドで SETPROG APF,ADD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SETPROG APF,ADD の出力を取らず復旧分離の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧分離の確認にする。 ✅
    - C. D A,L を省略して復旧分離の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧分離の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では SETPROG APF,ADD は「復旧分離の操作コマンドに関係する定義値と表示行を照合する復旧分離項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では SETPROG APF,ADD の属性行と IEE115I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明だけに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では SETPROG APF,ADD を MVS オペレータコマンドの運用手順で確認し、初出名は復旧分離初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 変更照合の操作コマンドに関する SETPROG APF,ADD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の操作コマンドの証跡として保存して根拠にする。
    - C. SETPROG APF,ADD の変更点を出力本文から切り離して変更照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合の操作コマンドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合の操作コマンドにおいて SETPROG APF,ADD は説明欄の「SETPROG APF,ADD の状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の操作コマンドに関する記録は、SETPROG APF,ADD の出力行と IEE115I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更照合ではありません。 B: 変更照合の操作コマンドは別カテゴリの確認を流用しており、SETPROG APF,ADD の根拠にならないため変更照合ではありません。 C: 変更照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の操作コマンドで記録する SETPROG APF,ADD はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG APF,ADD**

    - 検証目的: 記録照合の操作コマンドについて、SETPROG APF,ADD は、MVS オペレータコマンドの SET PROG で確認する項目です。個別データセットを動的に APF 許可リストへ追加するサブコマンド。緊急のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG APF,ADDを指定し、OSKB020033の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG APF,ADD
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG APF,ADD
    CASE OSKB020033
    SOURCE z/OS MVS Operations
    ```

    SETPROG APF,ADDとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020033を同じ出力で読み、記録照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020033 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020033   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG APF,ADD と OSKB020033 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG EXIT,ADD {#c22-i0255}
*分類: SET PROG*  ・  難易度: 上級

SETPROG EXIT,ADDは、MVS オペレータコマンドのSET PROGで確認する項目です。動的出口にルーチンを動的に登録する。OS の振る舞いを再 IPL なしで拡張・差替する手段

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 構文読解の操作コマンドに関係する SETPROG EXIT 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文読解の確認値として扱う。 ✅
    - B. SETPROG EXIT 命令の名称と担当者名だけを残して構文読解の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文読解の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文読解の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では SETPROG EXIT 命令 は「SETPROG EXIT 命令の用途を操作コマンドの表示で確認する構文読解項目」と D A,L または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景ではz/OS MVS Operationsの SETPROG EXIT 命令と IEE115I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明だけに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では SETPROG EXIT 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 呼出追跡の操作コマンドで操作コマンドの運用確認を行います。SETPROG EXIT,ADD の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出追跡の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出追跡の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 ✅
    - D. SETPROG EXIT,ADD の属性行を読まず呼出追跡の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡の操作コマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の操作コマンドにおいて SETPROG EXIT,ADD は説明欄の「z/OS MVS Operationsで SETPROG EXIT,ADD の扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の操作コマンドを受け取る担当者は、SETPROG EXIT,ADD の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG EXIT,ADD の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の操作コマンドが示す SETPROG EXIT,ADD は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG EXIT,ADD**

    - 検証目的: 値域照合の操作コマンドについて、SETPROG EXIT,ADD は、MVS オペレータコマンドの SET PROG で確認する項目です。動的出口にルーチンを動的に登録する。OS の振る舞いを再 IPL なしでに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG EXIT,ADDを指定し、OSKB020036の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG EXIT,ADD
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG EXIT,ADD
    CASE OSKB020036
    SOURCE z/OS MVS Operations
    ```

    SETPROG EXIT,ADDとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020036を同じ出力で読み、値域照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020036 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020036   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG EXIT,ADD と OSKB020036 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG LNKLST,DEFINE {#c22-i0256}
*分類: SET PROG*  ・  難易度: 中級

SETPROG LNKLST,DEFINEは、新しい LNKLST セットを定義 / ADD / ACTIVATE の動的入替手順を構成するサブコマンド。新しい LNKLST セットを定義 → ADD → ACTIVATE の動的入替手順を構成するサブコマンド

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 監査分離の操作コマンドで操作コマンドの運用確認を行います。SETPROG LNKLST 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査分離の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査分離の操作コマンドを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査分離の点検結果を残す。 ✅
    - D. SETPROG LNKLST 命令の属性行を読まず監査分離の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では SETPROG LNKLST 命令 は「z/OS MVS Operationsで SETPROG LNKLST 命令の扱いを記録する監査分離項目」と D A,L または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では SETPROG LNKLST 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明だけに寄り、判定名は監査分離不足です。監査分離資料では SETPROG LNKLST 命令の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 構文追跡の操作コマンドに関係する SETPROG LNKLST,DEFINE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 ✅
    - B. SETPROG LNKLST,DEFINE の名称と担当者名のみを残して構文追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で構文追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡の操作コマンドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡の操作コマンドにおいて SETPROG LNKLST,DEFINE は説明欄の「SETPROG LNKLST,DEFINE の用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の操作コマンドに関連して、z/OS MVS Operationsでは SETPROG LNKLST,DEFINE の表示属性と IEE115I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG LNKLST,DEFINE の根拠にならないため構文追跡ではありません。 D: 構文追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文追跡ではありません。構文追跡の操作コマンドで使う SETPROG LNKLST,DEFINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG LNKLST,DEFINE**

    - 検証目的: 比較照合の操作コマンドについて、SETPROG LNKLST,DEFINE は、新しい LNKLST セットを定義 / ADD / ACTIVATE の動的入替手順を構成するサブコマンド。新しい LNKLSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG LNKLST,DEFを指定し、OSKB020034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG LNKLST,DEF
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG LNKLST,DEF
    CASE OSKB020034
    SOURCE z/OS MVS Operations
    ```

    SETPROG LNKLST,DEFとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020034を同じ出力で読み、比較照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020034 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020034   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG LNKLST,DEF と OSKB020034 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG LPA,ADD {#c22-i0257}
*分類: SET PROG*  ・  難易度: 中級

SETPROG LPA,ADDは、Dynamic LPA に個別モジュール / データセット内モジュールを動的追加する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 変更分離の操作コマンドに関する SETPROG LPA,ADD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更分離の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更分離の操作コマンドの証跡として保存して根拠にする。
    - C. SETPROG LPA,ADD の変更点を出力本文から切り離して変更分離の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では SETPROG LPA,ADD は「SETPROG LPA,ADD の状態と出力メッセージを結び付ける変更分離項目」と D A,L または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では SETPROG LPA,ADD の出力行と IEE115I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明だけに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では SETPROG LPA,ADD をz/OS MVS Operationsの確認記録に残し、対象名は変更分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 展開追跡の操作コマンドで SETPROG LPA,ADD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SETPROG LPA,ADD の出力を取らず展開追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 ✅
    - C. D A,L を省略して展開追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡の操作コマンドにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡の操作コマンドにおいて SETPROG LPA,ADD は説明欄の「展開追跡の操作コマンドに関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の操作コマンドの証跡を読む担当者は、SETPROG LPA,ADD の属性行と IEE115I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG LPA,ADD の根拠にならないため展開追跡ではありません。展開追跡の操作コマンドに出る SETPROG LPA,ADD は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG LPA,ADD**

    - 検証目的: 順序照合の操作コマンドについて、SETPROG LPA,ADD は、Dynamic LPA に個別モジュール / データセット内モジュールを動的追加するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG LPA,ADDを指定し、OSKB020035の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG LPA,ADD
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG LPA,ADD
    CASE OSKB020035
    SOURCE z/OS MVS Operations
    ```

    SETPROG LPA,ADDとOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020035を同じ出力で読み、順序照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020035 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020035   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG LPA,ADD と OSKB020035 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SCH

### SET SCH=xx {#c22-i0258}
*分類: SET SCH*  ・  難易度: 中級

SCHEDxx を活性化し、プログラム特性テーブル (PPT) を更新する。AUTH/SYSTEM/NOSWAP 等の属性変更

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 展開読解の操作コマンドで SET SCH=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET SCH=xxの出力を取らず展開読解の操作コマンドの説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開読解の根拠を固定する。 ✅
    - C. D OPDATA を省略して展開読解の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開読解の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では SET SCH=xx は「展開読解の操作コマンドに関係する定義値と表示行を照合する展開読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では SET SCH=xxの属性行と IEE457I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明だけに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では SET SCH=xxを MVS オペレータコマンドの運用手順で確認し、初出名は展開読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 置換追跡の操作コマンドに関する SET SCH=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず置換追跡の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の操作コマンドの証跡として保存して根拠にする。
    - C. SET SCH=xxの変更点を出力本文から切り離して置換追跡の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡の操作コマンドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡の操作コマンドにおいて SET SCH=xx は説明欄の「SET SCH=xxの状態と出力メッセージを結び付ける置換追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の操作コマンドに関する記録は、SET SCH=xxの出力行と IEE457I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の操作コマンドは別カテゴリの確認を流用しており、SET SCH=xxの根拠にならないため置換追跡ではありません。 C: 置換追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の操作コマンドで記録する SET SCH=xxはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET SCH=xx**

    - 検証目的: 警告照合の操作コマンドについて、SCHEDxx を活性化し、プログラム特性テーブル (PPT) を更新する。AUTH/SYSTEM/NOSWAP 等の属性変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、警告照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SCH=xxを指定し、OSKB020037の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SCH=xx
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SCH=xx
    CASE OSKB020037
    SOURCE z/OS MVS Operations
    ```

    SET SCH=xxとOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020037を同じ出力で読み、警告照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020037 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020037   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SCH=xx と OSKB020037 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SLIP

### SLIP コマンド (SET SLIP=xx) {#c22-i0259}
*分類: SET SLIP*  ・  難易度: 中級

SLIP コマンド (SET SLIP=xx)は、IEASLPxx を動的活性化し、定義済み SLIP トラップ群を一括導入する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 終端読解のコマンドに関係する SLIP コマンド 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端読解の確認記録にまとめる。 ✅
    - B. SLIP コマンド 属性の名称と担当者名だけを残して終端読解のコマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端読解のコマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず終端読解のコマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では SLIP コマンド 属性 は「SLIP コマンド 属性の用途を操作コマンドの表示で確認する終端読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景ではz/OS MVS Operationsの SLIP コマンド 属性と IEE457I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明だけに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では SLIP コマンド 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 上書追跡のコマンドで操作コマンドの運用確認を行います。SLIP コマンド (SET SLIP=xx)の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書追跡のコマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず上書追跡のコマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. SLIP コマンド (SET SLIP=xx)の属性行を読まず上書追跡のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のコマンドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のコマンドにおいて SLIP コマンド (SET SLIP=xx) は説明欄の「z/OS MVS Operationsで SLIP コマンド (SET SLIP=xx)の扱いを記録する上書追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のコマンドを受け取る担当者は、SLIP コマンド (SET SLIP=xx)の表示結果と IEE457I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のコマンドは別カテゴリの確認を流用しており、SLIP コマンド (SET SLIP=xx)の根拠にならないため上書追跡ではありません。 B: 上書追跡のコマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のコマンドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のコマンドが示す SLIP コマンド (SET SLIP=xx)は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SLIP コマンド (SET SLIP=xx)**

    - 検証目的: 変更照合のコマンドについて、SLIP コマンド (SET SLIP=xx)は、IEASLPxx を動的活性化し、定義済み SLIP トラップ群を一括導入するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、変更照合のコマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSLIP コマンド (SET SLIを指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SLIP コマンド (SET SLI
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SLIP コマンド (SET SLI
    CASE OSKB020040
    SOURCE z/OS MVS Operations
    ```

    SLIP コマンド (SET SLIとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020040を同じ出力で読み、変更照合のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020040 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020040   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SLIP コマンド (SET SLI と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SMF

### SET SMF=xx {#c22-i0260}
*分類: SET SMF*  ・  難易度: 上級

SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 呼出読解の操作コマンドで操作コマンドの運用確認を行います。SET SMF=xxの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出読解の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず呼出読解の操作コマンドを正常終了として記録する。
    - C. IEE457I を含む表示を保存し、説明欄との差分を呼出読解で確認する。 ✅
    - D. SET SMF=xxの属性行を読まず呼出読解の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では SET SMF=xx は「z/OS MVS Operationsで SET SMF=xxの扱いを記録する呼出読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では SET SMF=xxの表示結果と IEE457I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明だけに寄り、判定名は呼出読解不足です。呼出読解資料では SET SMF=xxの使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 終端追跡の操作コマンドに関係する SET SMF=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 ✅
    - B. SET SMF=xxの名称と担当者名のみを残して終端追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で終端追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず終端追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡の操作コマンドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡の操作コマンドにおいて SET SMF=xx は説明欄の「SET SMF=xxの用途を操作コマンドの表示で確認する終端追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の操作コマンドに関連して、z/OS MVS Operationsでは SET SMF=xxの表示属性と IEE457I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の操作コマンドは別カテゴリの確認を流用しており、SET SMF=xxの根拠にならないため終端追跡ではありません。 D: 終端追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため終端追跡ではありません。終端追跡の操作コマンドで使う SET SMF=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **SET SMF=xx**

    - 検証目的: 出力照合の操作コマンドについて、SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040028の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMF=xxを指定し、OSKB040028の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SMF=xx
    CASE OSKB040028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SMF=xx
    CASE OSKB040028
    SOURCE z/OS MVS Operations
    ```

    SET SMF=xxとOSKB040028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040028を同じ出力で読み、出力照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040028
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040028 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040028   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SMF=xx と OSKB040028 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **SET SMF=xx**

    - 検証目的: 復旧照合の操作コマンドについて、SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、復旧照合の操作コマンドの確認表示へ進みます。
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
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMF=xxを指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SMF=xx
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SMF=xx
    CASE OSKB020038
    SOURCE z/OS MVS Operations
    ```

    SET SMF=xxとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020038を同じ出力で読み、復旧照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020038 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020038   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SMF=xx と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands


