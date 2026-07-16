---
search:
  exclude: true
---

# TSO / ISPF / SDSF — 詳細 (5/6)

[← TSO / ISPF / SDSF の概要へ戻る](index.md)


## TSO / ISPF / SDSF > TSO_MISC

### EDIT コマンド (旧 TSO EDIT) {#c30-i0308}
*分類: TSO_MISC*  ・  難易度: 中級

EDIT コマンド (旧 TSO EDIT)は、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **EDIT コマンド (旧 TSO EDIT)**

    - 検証目的: 復旧確認のコマンド 旧について、EDIT コマンド (旧 TSO EDIT)は、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、復旧確認のコマンド 旧の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にEDIT コマンド (旧 TSO Eを指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND EDIT コマンド (旧 TSO E
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM EDIT コマンド (旧 TSO E
    CASE OSKB020018
    SOURCE TSO ISPF SDSF
    ```

    EDIT コマンド (旧 TSO EとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020018を同じ出力で読み、復旧確認のコマンド 旧の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020018
    COMMAND ===> SDSF DA
    ISF031I EDIT コマンド (旧 TSO EDIT) DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の EDIT コマンド (旧 TSO E と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### END コマンド {#c30-i0309}
*分類: TSO_MISC*  ・  難易度: 中級

END コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（2件）"
    **END コマンド**

    - 検証目的: 記録確認のコマンドについて、END コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、記録確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にEND コマンドを指定し、OSKB020013の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND END コマンド
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM END コマンド
    CASE OSKB020013
    SOURCE TSO ISPF SDSF
    ```

    END コマンドとOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020013を同じ出力で読み、記録確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020013
    COMMAND ===> SDSF DA
    ISF031I END コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の END コマンド と OSKB020013 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide

    ---

    **END コマンド**

    - 検証目的: 構文整理のコマンドについて、END コマンドは、TSO / ISPF / SDSF の ISPF_EDIT_PRIMARY で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、構文整理のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にEND コマンドを指定し、OSKB020101の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND END コマンド
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM END コマンド
    CASE OSKB020101
    SOURCE TSO ISPF SDSF
    ```

    END コマンドとOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020101を同じ出力で読み、構文整理のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020101
    COMMAND ===> SDSF DA
    ISF031I END コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の END コマンド と OSKB020101 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF Edit and Edit Macros



### EXEC EXEC オペランド {#c30-i0310}
*分類: TSO_MISC*  ・  難易度: 中級

EXEC EXEC オペランドは、TSO / ISPF / SDSFのTSO_MISCで確認する項目です。メンバが REXX か CLIST か曖昧な場合に明示する EXEC タイプ指定 (省略時はメンバの 1 行目で判別)

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **EXEC EXEC オペランド**

    - 検証目的: 優先確認のオペランドについて、EXEC EXEC オペランドは、TSO / ISPF / SDSF の TSO_MISC で確認する項目です。メンバが REXX か CLIST か曖昧な場合に明示する EXEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、優先確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にEXEC EXEC オペランドを指定し、OSKB020012の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND EXEC EXEC オペランド
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM EXEC EXEC オペランド
    CASE OSKB020012
    SOURCE TSO ISPF SDSF
    ```

    EXEC EXEC オペランドとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020012を同じ出力で読み、優先確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020012
    COMMAND ===> SDSF DA
    ISF031I EXEC EXEC オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の EXEC EXEC オペランド と OSKB020012 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### EXEC コマンド {#c30-i0311}
*分類: TSO_MISC*  ・  難易度: 中級

EXEC コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **EXEC コマンド**

    - 検証目的: 範囲確認のコマンドについて、EXEC コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、範囲確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にEXEC コマンドを指定し、OSKB020011の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND EXEC コマンド
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM EXEC コマンド
    CASE OSKB020011
    SOURCE TSO ISPF SDSF
    ```

    EXEC コマンドとOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020011を同じ出力で読み、範囲確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020011
    COMMAND ===> SDSF DA
    ISF031I EXEC コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の EXEC コマンド と OSKB020011 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### HELP/TSO HELP コマンド {#c30-i0312}
*分類: TSO_MISC*  ・  難易度: 中級

HELP/TSO HELP コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **HELP ・ TSO HELP コマンド**

    - 検証目的: 条件確認の・ コマンドについて、HELP/TSO HELP コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020009の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、条件確認の・ コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にHELP ・ TSO HELP コマを指定し、OSKB020009の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND HELP ・ TSO HELP コマ
    CASE OSKB020009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM HELP ・ TSO HELP コマ
    CASE OSKB020009
    SOURCE TSO ISPF SDSF
    ```

    HELP ・ TSO HELP コマとOSKB020009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020009を同じ出力で読み、条件確認の・ コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020009
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020009
    COMMAND ===> SDSF DA
    ISF031I HELP ・ TSO HELP コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の HELP ・ TSO HELP コマ と OSKB020009 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### OUTDES/OUTPUT 動的指定 {#c30-i0313}
*分類: TSO_MISC*  ・  難易度: 中級

OUTDES/OUTPUT 動的指定は、TSO / ISPF / SDSFのTSO_MISCで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **OUTDES ・ OUTPUT 動的指定**

    - 検証目的: 変更確認の・ 動的指定について、OUTDES/OUTPUT 動的指定は、TSO / ISPF / SDSF の TSO_MISC で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更確認の・ 動的指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTDES ・ OUTPUT 動的を指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTDES ・ OUTPUT 動的
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTDES ・ OUTPUT 動的
    CASE OSKB020020
    SOURCE TSO ISPF SDSF
    ```

    OUTDES ・ OUTPUT 動的とOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020020を同じ出力で読み、変更確認の・ 動的指定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020020
    COMMAND ===> SDSF DA
    ISF031I OUTDES ・ OUTPUT 動的指定 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTDES ・ OUTPUT 動的 と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### PRINTDS コマンド {#c30-i0314}
*分類: TSO_MISC*  ・  難易度: 中級

PRINTDS コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **PRINTDS コマンド**

    - 検証目的: 上書確認のコマンドについて、PRINTDS コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、上書確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にPRINTDS コマンドを指定し、OSKB020007の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND PRINTDS コマンド
    CASE OSKB020007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM PRINTDS コマンド
    CASE OSKB020007
    SOURCE TSO ISPF SDSF
    ```

    PRINTDS コマンドとOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020007を同じ出力で読み、上書確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020007
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020007
    COMMAND ===> SDSF DA
    ISF031I PRINTDS コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の PRINTDS コマンド と OSKB020007 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### PROFILE NOPREFIX {#c30-i0315}
*分類: TSO_MISC*  ・  難易度: 中級

PROFILE NOPREFIXは、TSO / ISPF / SDSFのTSO_MISCで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **PROFILE NOPREFIX**

    - 検証目的: 値域確認の対話操作について、PROFILE NOPREFIX は、TSO / ISPF / SDSF の TSO_MISC で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域確認の対話操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にPROFILE NOPREFIXを指定し、OSKB020016の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND PROFILE NOPREFIX
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM PROFILE NOPREFIX
    CASE OSKB020016
    SOURCE TSO ISPF SDSF
    ```

    PROFILE NOPREFIXとOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020016を同じ出力で読み、値域確認の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020016
    COMMAND ===> SDSF DA
    ISF031I PROFILE NOPREFIX DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の PROFILE NOPREFIX と OSKB020016 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### PROFILE NOTICES/MSGID/MODE {#c30-i0316}
*分類: TSO_MISC*  ・  難易度: 中級

PROFILE NOTICES/MSGID/MODEは、TSO / ISPF / SDSFのTSO_MISCでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **PROFILE NOTICES ・ MSGID ・ MODE**

    - 検証目的: 警告確認の・ ・について、PROFILE NOTICES/MSGID/MODE は、TSO / ISPF / SDSF の TSO_MISC でメッセージや異常終了の原因を切り分けるための項目です。メッセーに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告確認の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にPROFILE NOTICES ・ を指定し、OSKB020017の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND PROFILE NOTICES ・ 
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM PROFILE NOTICES ・ 
    CASE OSKB020017
    SOURCE TSO ISPF SDSF
    ```

    PROFILE NOTICES ・ とOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020017を同じ出力で読み、警告確認の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020017
    COMMAND ===> SDSF DA
    ISF031I PROFILE NOTICES ・ MSGID ・ MO DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の PROFILE NOTICES ・  と OSKB020017 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### PROFILE PREFIX {#c30-i0317}
*分類: TSO_MISC*  ・  難易度: 中級

PROFILE PREFIXは、TSO / ISPF / SDSFのTSO_MISCで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? question "確認問題（3問）"
    **問題.** 選択面のデータセット接頭辞を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってプロファイル 接頭辞表示を確認する場合、この状況で優先する項目はどれですか。

    - A. SDSF H panel
    - B. SDSF ARRANGE
    - C. PROFILE PREFIX ✅
    - D. HELP command

    正解: **C** ／ 難易度: 中級

    **解説:** 通信面観点の出力確認としてデータセット接頭辞状態を読み、答えはCで、照合焦点はデータセット接頭辞定義です。照合面観点のデータセット接頭辞根拠は、単引用符なしのデータセット名に付く接頭辞を確認することを満たす入力、画面、応答を同じ証跡で確認するデータセット接頭辞根拠です。保存面観点で残すデータセット接頭辞応答は、プロファイル 接頭辞表示をコマンドまたはパネル形式と照合するデータセット接頭辞応答です。選択面観点のデータセット接頭辞保守は、TSO/Eプロファイルの入力要求と戻った表示を結び、運用状態を説明するデータセット接頭辞保守です。A: 端末面観点の比較先はHeld Output Queue定義で、要求対象はデータセット接頭辞監査です。B: 出力面観点の照合先は列配置変更根拠で、中心はデータセット接頭辞引継ぎです。C: 編集面観点のデータセット接頭辞応答は、入力名と画面内のプロファイル 接頭辞表示を結ぶデータセット接頭辞報告です。D: 監査面観点の参照先はコマンドヘルプ表示保守で、作業記録で追跡する対象はデータセット接頭辞復旧です。管理面観点の用語定義として、データセット接頭辞とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット接頭辞照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PROFILE

    ---

    **問題.** 照合面のデータセット接頭辞を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってプロファイル 接頭辞表示を確認する場合、証跡として中心に置く項目はどれですか。

    - A. PROFILE PREFIX ✅
    - B. SDSF P purge
    - C. LISTDS MEMBERS
    - D. RECEIVE DATASET

    正解: **A** ／ 難易度: 中級

    **解説:** 出力面観点で読むデータセット接頭辞根拠は正答位置Aで、記録する焦点はプロファイル 接頭辞応答です。保存面観点のデータセット接頭辞保守は、単引用符なしのデータセット名に付く接頭辞を確認することを満たす入力、画面、応答を同じ証跡で確認するデータセット接頭辞保守です。操作面観点のデータセット接頭辞監査は、プロファイル 接頭辞表示を入力記録と合わせて処理対象を見分けるデータセット接頭辞監査です。照合面観点のデータセット接頭辞引継ぎは、TSO/Eプロファイルの入力要求と戻った表示を結び、運用状態を説明するデータセット接頭辞引継ぎです。A: 制御面観点のデータセット接頭辞応答は、入力名と画面内のプロファイル 接頭辞表示を結ぶデータセット接頭辞反映です。B: 通信面観点の参照先はジョブ取消と出力削除保守で、作業記録で追跡する対象はデータセット接頭辞報告です。C: 表示面観点の比較先はメンバー一覧表示監査で、要求対象はデータセット接頭辞棚卸です。D: 投入面観点の照合先は送信データ受信引継ぎで、中心はデータセット接頭辞復旧です。選択面観点の用語定義として、データセット接頭辞とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット接頭辞選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PROFILE

    ---

    **問題.** 保存面のデータセット接頭辞を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってプロファイル 接頭辞表示を確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. RENAME DATASET
    - B. PRINTDS
    - C. PROFILE PREFIX ✅
    - D. ISPF option 6 Command

    正解: **C** ／ 難易度: 中級

    **解説:** 投入面観点の出力確認としてデータセット接頭辞保守を読み、答えはCで、照合焦点はデータセット接頭辞監査です。監査面観点のデータセット接頭辞引継ぎは、単引用符なしのデータセット名に付く接頭辞を確認することを満たす入力、画面、応答を同じ証跡で確認するデータセット接頭辞引継ぎです。確認面観点で残すデータセット接頭辞棚卸は、プロファイル 接頭辞表示をコマンドまたはパネル形式と照合するデータセット接頭辞棚卸です。保存面観点のデータセット接頭辞復旧は、TSO/Eプロファイルの入力要求と戻った表示を結び、運用状態を説明するデータセット接頭辞復旧です。A: 応答面観点の比較先はデータセット改名監査で、要求対象はデータセット接頭辞照合です。B: 表示面観点の照合先はデータセット印刷引継ぎで、中心はデータセット接頭辞報告です。C: 端末面観点のデータセット接頭辞棚卸は、入力名と画面内のプロファイル 接頭辞表示を結ぶデータセット接頭辞証跡です。D: 操作面観点の参照先はTSO Command Processor復旧で、作業記録で追跡する対象はデータセット接頭辞反映です。照合面観点の用語定義として、データセット接頭辞とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット接頭辞観点です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PROFILE


??? note "検証手順（1件）"
    **PROFILE PREFIX**

    - 検証目的: 順序確認の対話操作について、PROFILE PREFIX は、TSO / ISPF / SDSF の TSO_MISC で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、順序確認の対話操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にPROFILE PREFIXを指定し、OSKB020015の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND PROFILE PREFIX
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM PROFILE PREFIX
    CASE OSKB020015
    SOURCE TSO ISPF SDSF
    ```

    PROFILE PREFIXとOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020015を同じ出力で読み、順序確認の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020015
    COMMAND ===> SDSF DA
    ISF031I PROFILE PREFIX DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の PROFILE PREFIX と OSKB020015 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### PROFILE コマンド {#c30-i0318}
*分類: TSO_MISC*  ・  難易度: 中級

PROFILE コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（2件）"
    **PROFILE コマンド**

    - 検証目的: 比較確認のコマンドについて、PROFILE コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、比較確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にPROFILE コマンドを指定し、OSKB020014の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND PROFILE コマンド
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM PROFILE コマンド
    CASE OSKB020014
    SOURCE TSO ISPF SDSF
    ```

    PROFILE コマンドとOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020014を同じ出力で読み、比較確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020014
    COMMAND ===> SDSF DA
    ISF031I PROFILE コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の PROFILE コマンド と OSKB020014 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide

    ---

    **PROFILE コマンド**

    - 検証目的: 探索確認のコマンドについて、PROFILE コマンドは、TSO / ISPF / SDSF の ISPF_EDIT_PRIMARY で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB030006の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、探索確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にPROFILE コマンドを指定し、OSKB030006の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND PROFILE コマンド
    CASE OSKB030006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM PROFILE コマンド
    CASE OSKB030006
    SOURCE TSO ISPF SDSF
    ```

    PROFILE コマンドとOSKB030006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB030006を同じ出力で読み、探索確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB030006
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB030006
    COMMAND ===> SDSF DA
    ISF031I PROFILE コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB030006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の PROFILE コマンド と OSKB030006 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB030006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF Edit and Edit Macros



### SEND USER/LOGON/SAVE オペランド {#c30-i0319}
*分類: TSO_MISC*  ・  難易度: 中級

SEND USER/LOGON/SAVE オペランドは、TSO / ISPF / SDSFのTSO_MISCで確認する項目です。宛先 (USER)/相手ログオン時にだけ届ける/Broadcast に保存し後で読ませる、を切り分けるオプション

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **SEND USER ・ LOGON ・ SAVE オペランド**

    - 検証目的: 探索確認の・ ・ オペラについて、SEND USER/LOGON/SAVE オペランドは、TSO / ISPF / SDSF の TSO_MISC で確認する項目です。宛先 (USER)/相手ログオン時にだけ届けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020006の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、探索確認の・ ・ オペラの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSEND USER ・ LOGON を指定し、OSKB020006の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SEND USER ・ LOGON 
    CASE OSKB020006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SEND USER ・ LOGON 
    CASE OSKB020006
    SOURCE TSO ISPF SDSF
    ```

    SEND USER ・ LOGON とOSKB020006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020006を同じ出力で読み、探索確認の・ ・ オペラの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020006
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020006
    COMMAND ===> SDSF DA
    ISF031I SEND USER ・ LOGON ・ SAVE オペラ DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SEND USER ・ LOGON  と OSKB020006 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### SEND コマンド {#c30-i0320}
*分類: TSO_MISC*  ・  難易度: 中級

SEND コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **SEND コマンド**

    - 検証目的: 終端確認のコマンドについて、SEND コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、終端確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSEND コマンドを指定し、OSKB020005の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SEND コマンド
    CASE OSKB020005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SEND コマンド
    CASE OSKB020005
    SOURCE TSO ISPF SDSF
    ```

    SEND コマンドとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020005を同じ出力で読み、終端確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020005
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020005
    COMMAND ===> SDSF DA
    ISF031I SEND コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SEND コマンド と OSKB020005 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### SMCOPY コマンド (Session Manager) {#c30-i0321}
*分類: TSO_MISC*  ・  難易度: 中級

SMCOPY コマンド (Session Manager)は、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **SMCOPY コマンド (Session Manager)**

    - 検証目的: 出力確認のコマンドについて、SMCOPY コマンド (Session Manager)は、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、出力確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSMCOPY コマンド (Sessiを指定し、OSKB020008の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SMCOPY コマンド (Sessi
    CASE OSKB020008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SMCOPY コマンド (Sessi
    CASE OSKB020008
    SOURCE TSO ISPF SDSF
    ```

    SMCOPY コマンド (SessiとOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020008を同じ出力で読み、出力確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020008
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020008
    COMMAND ===> SDSF DA
    ISF031I SMCOPY コマンド (Session Man DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SMCOPY コマンド (Sessi と OSKB020008 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### TEST コマンド {#c30-i0322}
*分類: TSO_MISC*  ・  難易度: 中級

TEST コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **TEST コマンド**

    - 検証目的: 監査確認のコマンドについて、TEST コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、監査確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にTEST コマンドを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND TEST コマンド
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM TEST コマンド
    CASE OSKB020019
    SOURCE TSO ISPF SDSF
    ```

    TEST コマンドとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020019を同じ出力で読み、監査確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020019
    COMMAND ===> SDSF DA
    ISF031I TEST コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の TEST コマンド と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### TIME コマンド {#c30-i0323}
*分類: TSO_MISC*  ・  難易度: 中級

TIME コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **TIME コマンド**

    - 検証目的: 呼出確認のコマンドについて、TIME コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020003の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、呼出確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にTIME コマンドを指定し、OSKB020003の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND TIME コマンド
    CASE OSKB020003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM TIME コマンド
    CASE OSKB020003
    SOURCE TSO ISPF SDSF
    ```

    TIME コマンドとOSKB020003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020003を同じ出力で読み、呼出確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020003
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020003
    COMMAND ===> SDSF DA
    ISF031I TIME コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の TIME コマンド と OSKB020003 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### WHO コマンド {#c30-i0324}
*分類: TSO_MISC*  ・  難易度: 中級

WHO コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? question "確認問題（1問）"
    **問題.** 変更検査のコマンドに関する WHO コマンドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず変更検査のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のコマンドの証跡として保存して根拠にする。
    - C. WHO コマンドの変更点を出力本文から切り離して変更検査のコマンドの承認欄のみ残す。
    - D. SDSF DA の結果から対象行を抜き出し、変更検査の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査のコマンドにおいて選択記号 D を採用し、識別名は変更検査です。変更検査のコマンドにおいて WHO コマンド は説明欄の「WHO コマンドの状態と出力メッセージを結び付ける変更検査項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査のコマンドに関する記録は、WHO コマンドの出力行と ISF031I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査のコマンドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため変更検査ではありません。 B: 変更検査のコマンドは別カテゴリの確認を流用しており、WHO コマンドの根拠にならないため変更検査ではありません。 C: 変更検査のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査のコマンドは対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査のコマンドで記録する WHO コマンドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は変更検査です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（2件）"
    **WHO コマンド**

    - 検証目的: 置換確認のコマンドについて、WHO コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、置換確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にWHO コマンドを指定し、OSKB020004の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND WHO コマンド
    CASE OSKB020004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM WHO コマンド
    CASE OSKB020004
    SOURCE TSO ISPF SDSF
    ```

    WHO コマンドとOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020004を同じ出力で読み、置換確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020004
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020004
    COMMAND ===> SDSF DA
    ISF031I WHO コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の WHO コマンド と OSKB020004 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide

    ---

    **WHO コマンド**

    - 検証目的: 呼出整理のコマンドについて、WHO コマンドは、TSO / ISPF / SDSF の SDSF_COMMAND で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB030103の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、呼出整理のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にWHO コマンドを指定し、OSKB030103の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND WHO コマンド
    CASE OSKB030103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM WHO コマンド
    CASE OSKB030103
    SOURCE TSO ISPF SDSF
    ```

    WHO コマンドとOSKB030103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB030103を同じ出力で読み、呼出整理のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB030103
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB030103
    COMMAND ===> SDSF DA
    ISF031I WHO コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB030103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の WHO コマンド と OSKB030103 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB030103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SDSF User's Guide、z / OS SDSF Operation and Customization




## TSO / ISPF / SDSF > TSO_SUBMIT

### CANCEL PURGE オペランド {#c30-i0325}
*分類: TSO_SUBMIT*  ・  難易度: 中級

CANCEL PURGE オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 上書照合のオペランドで対話操作の運用確認を行います。CANCEL PURGE オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で上書照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず上書照合のオペランドを正常終了として記録する。
    - C. 同じ画面で対象行と ISF031I を読み、上書照合の結果として保存する。 ✅
    - D. CANCEL PURGE オペランドの属性行を読まず上書照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合のオペランドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合のオペランドにおいて CANCEL PURGE オペランド は説明欄の「TSO ISPF SDSF で CANCEL PURGE オペランドの扱いを記録する上書照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のオペランドを受け取る担当者は、CANCEL PURGE オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のオペランドは別カテゴリの確認を流用しており、CANCEL PURGE オペランドの根拠にならないため上書照合ではありません。 B: 上書照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため上書照合ではありません。 C: 上書照合のオペランドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のオペランドが示す CANCEL PURGE オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **CANCEL PURGE オペランド**

    - 検証目的: 区切判定のオペランドについて、CANCEL PURGE オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010090の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、区切判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCANCEL PURGE オペランドを指定し、OSKB010090の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND CANCEL PURGE オペランド
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM CANCEL PURGE オペランド
    CASE OSKB010090
    SOURCE TSO ISPF SDSF
    ```

    CANCEL PURGE オペランドとOSKB010090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010090を同じ出力で読み、区切判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010090
    COMMAND ===> SDSF DA
    ISF031I CANCEL PURGE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の CANCEL PURGE オペランド と OSKB010090 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### CANCEL 基本構文 {#c30-i0326}
*分類: TSO_SUBMIT*  ・  難易度: 初級

CANCEL 基本構文は、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 探索照合の基本構文で CANCEL 基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CANCEL 基本構文の出力を取らず探索照合の基本構文の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索照合の根拠にする。 ✅
    - C. SDSF DA を省略して探索照合の基本構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 探索照合の基本構文において選択記号 B を採用し、識別名は探索照合です。探索照合の基本構文において CANCEL 基本構文 は説明欄の「探索照合の基本構文に関係する定義値と表示行を照合する探索照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の基本構文の証跡を読む担当者は、CANCEL 基本構文の属性行と ISF031I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の基本構文は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため探索照合ではありません。 D: 探索照合の基本構文は別カテゴリの確認を流用しており、CANCEL 基本構文の根拠にならないため探索照合ではありません。探索照合の基本構文に出る CANCEL 基本構文は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **CANCEL 基本構文**

    - 検証目的: 条件判定の基本構文について、CANCEL 基本構文は、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010089の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、条件判定の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCANCEL 基本構文を指定し、OSKB010089の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND CANCEL 基本構文
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM CANCEL 基本構文
    CASE OSKB010089
    SOURCE TSO ISPF SDSF
    ```

    CANCEL 基本構文とOSKB010089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010089を同じ出力で読み、条件判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010089
    COMMAND ===> SDSF DA
    ISF031I CANCEL 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の CANCEL 基本構文 と OSKB010089 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### OUTPUT DELETE オペランド {#c30-i0327}
*分類: TSO_SUBMIT*  ・  難易度: 中級

OUTPUT DELETE オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 範囲照合のオペランドで対話操作の運用確認を行います。OUTPUT DELETE オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で範囲照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず範囲照合のオペランドを正常終了として記録する。
    - C. TSO ISPF SDSF の表示形式に沿って根拠行を採り、範囲照合の点検結果を残す。 ✅
    - D. OUTPUT DELETE オペランドの属性行を読まず範囲照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合のオペランドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合のオペランドにおいて OUTPUT DELETE オペランド は説明欄の「TSO ISPF SDSF で OUTPUT DELETE オペランドの扱いを記録する範囲照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のオペランドを受け取る担当者は、OUTPUT DELETE オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のオペランドは別カテゴリの確認を流用しており、OUTPUT DELETE オペランドの根拠にならないため範囲照合ではありません。 B: 範囲照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のオペランドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のオペランドが示す OUTPUT DELETE オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTPUT DELETE オペランド**

    - 検証目的: 比較判定のオペランドについて、OUTPUT DELETE オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、比較判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTPUT DELETE オペランを指定し、OSKB010094の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTPUT DELETE オペラン
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTPUT DELETE オペラン
    CASE OSKB010094
    SOURCE TSO ISPF SDSF
    ```

    OUTPUT DELETE オペランとOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010094を同じ出力で読み、比較判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010094
    COMMAND ===> SDSF DA
    ISF031I OUTPUT DELETE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTPUT DELETE オペラン と OSKB010094 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### OUTPUT DEST オペランド {#c30-i0328}
*分類: TSO_SUBMIT*  ・  難易度: 中級

OUTPUT DEST オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 記録照合のオペランドに関係する OUTPUT DEST オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録照合の確認値として扱う。 ✅
    - B. OUTPUT DEST オペランドの名称と担当者名のみを残して記録照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で記録照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず記録照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合のオペランドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合のオペランドにおいて OUTPUT DEST オペランド は説明欄の「OUTPUT DEST オペランドの用途を対話操作の表示で確認する記録照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のオペランドに関連して、TSO ISPF SDSF では OUTPUT DEST オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のオペランドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のオペランドは別カテゴリの確認を流用しており、OUTPUT DEST オペランドの根拠にならないため記録照合ではありません。 D: 記録照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため記録照合ではありません。記録照合のオペランドで使う OUTPUT DEST オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は記録照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTPUT DEST オペランド**

    - 検証目的: 値域判定のオペランドについて、OUTPUT DEST オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010096の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTPUT DEST オペランドを指定し、OSKB010096の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTPUT DEST オペランド
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTPUT DEST オペランド
    CASE OSKB010096
    SOURCE TSO ISPF SDSF
    ```

    OUTPUT DEST オペランドとOSKB010096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010096を同じ出力で読み、値域判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010096
    COMMAND ===> SDSF DA
    ISF031I OUTPUT DEST オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTPUT DEST オペランド と OSKB010096 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### OUTPUT KEEP オペランド {#c30-i0329}
*分類: TSO_SUBMIT*  ・  難易度: 中級

OUTPUT KEEP オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 区切照合のオペランドで OUTPUT KEEP オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. OUTPUT KEEP オペランドの出力を取らず区切照合のオペランドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切照合の確認にする。 ✅
    - C. SDSF DA を省略して区切照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合のオペランドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のオペランドにおいて OUTPUT KEEP オペランド は説明欄の「区切照合のオペランドに関係する定義値と表示行を照合する区切照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のオペランドの証跡を読む担当者は、OUTPUT KEEP オペランドの属性行と ISF031I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のオペランドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため区切照合ではありません。 D: 区切照合のオペランドは別カテゴリの確認を流用しており、OUTPUT KEEP オペランドの根拠にならないため区切照合ではありません。区切照合のオペランドに出る OUTPUT KEEP オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTPUT KEEP オペランド**

    - 検証目的: 記録判定のオペランドについて、OUTPUT KEEP オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010093の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、記録判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTPUT KEEP オペランドを指定し、OSKB010093の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTPUT KEEP オペランド
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTPUT KEEP オペランド
    CASE OSKB010093
    SOURCE TSO ISPF SDSF
    ```

    OUTPUT KEEP オペランドとOSKB010093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010093を同じ出力で読み、記録判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010093
    COMMAND ===> SDSF DA
    ISF031I OUTPUT KEEP オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTPUT KEEP オペランド と OSKB010093 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### OUTPUT PRINT オペランド {#c30-i0330}
*分類: TSO_SUBMIT*  ・  難易度: 中級

OUTPUT PRINT オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 優先照合のオペランドに関する OUTPUT PRINT オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず優先照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のオペランドの証跡として保存して根拠にする。
    - C. OUTPUT PRINT オペランドの変更点を出力本文から切り離して優先照合のオペランドの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合のオペランドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合のオペランドにおいて OUTPUT PRINT オペランド は説明欄の「OUTPUT PRINT オペランドの状態と出力メッセージを結び付ける優先照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のオペランドに関する記録は、OUTPUT PRINT オペランドの出力行と ISF031I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため優先照合ではありません。 B: 優先照合のオペランドは別カテゴリの確認を流用しており、OUTPUT PRINT オペランドの根拠にならないため優先照合ではありません。 C: 優先照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のオペランドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のオペランドで記録する OUTPUT PRINT オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTPUT PRINT オペランド**

    - 検証目的: 順序判定のオペランドについて、OUTPUT PRINT オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010095の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、順序判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTPUT PRINT オペランドを指定し、OSKB010095の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTPUT PRINT オペランド
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTPUT PRINT オペランド
    CASE OSKB010095
    SOURCE TSO ISPF SDSF
    ```

    OUTPUT PRINT オペランドとOSKB010095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010095を同じ出力で読み、順序判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010095
    COMMAND ===> SDSF DA
    ISF031I OUTPUT PRINT オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTPUT PRINT オペランド と OSKB010095 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### OUTPUT jobname オペランド {#c30-i0331}
*分類: TSO_SUBMIT*  ・  難易度: 中級

OUTPUT jobname オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 条件照合のオペランドに関係する OUTPUT jobname オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件照合として引き継ぐ。 ✅
    - B. OUTPUT jobname オペランドの名称と担当者名のみを残して条件照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で条件照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず条件照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合のオペランドにおいて選択記号 A を採用し、識別名は条件照合です。条件照合のオペランドにおいて OUTPUT jobname オペランド は説明欄の「OUTPUT jobname オペランドの用途を対話操作の表示で確認する条件照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のオペランドに関連して、TSO ISPF SDSF では OUTPUT jobname オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のオペランドは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のオペランドは別カテゴリの確認を流用しており、OUTPUT jobname オペランドの根拠にならないため条件照合ではありません。 D: 条件照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため条件照合ではありません。条件照合のオペランドで使う OUTPUT jobname オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTPUT jobname オペランド**

    - 検証目的: 優先判定のオペランドについて、OUTPUT jobname オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、優先判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTPUT jobname オペラを指定し、OSKB010092の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTPUT jobname オペラ
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTPUT jobname オペラ
    CASE OSKB010092
    SOURCE TSO ISPF SDSF
    ```

    OUTPUT jobname オペラとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010092を同じ出力で読み、優先判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010092
    COMMAND ===> SDSF DA
    ISF031I OUTPUT jobname オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTPUT jobname オペラ と OSKB010092 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### OUTPUT 基本構文 {#c30-i0332}
*分類: TSO_SUBMIT*  ・  難易度: 初級

OUTPUT 基本構文は、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 出力照合の基本構文に関する OUTPUT 基本構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず出力照合の基本構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の基本構文の証跡として保存して根拠にする。
    - C. OUTPUT 基本構文の変更点を出力本文から切り離して出力照合の基本構文の承認欄のみ残す。
    - D. SDSF DA で得た表示本文を使い、出力照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力照合の基本構文において選択記号 D を採用し、識別名は出力照合です。出力照合の基本構文において OUTPUT 基本構文 は説明欄の「OUTPUT 基本構文の状態と出力メッセージを結び付ける出力照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の基本構文に関する記録は、OUTPUT 基本構文の出力行と ISF031I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため出力照合ではありません。 B: 出力照合の基本構文は別カテゴリの確認を流用しており、OUTPUT 基本構文の根拠にならないため出力照合ではありません。 C: 出力照合の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の基本構文は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の基本構文で記録する OUTPUT 基本構文は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTPUT 基本構文**

    - 検証目的: 範囲判定の基本構文について、OUTPUT 基本構文は、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010091の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、範囲判定の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にOUTPUT 基本構文を指定し、OSKB010091の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND OUTPUT 基本構文
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM OUTPUT 基本構文
    CASE OSKB010091
    SOURCE TSO ISPF SDSF
    ```

    OUTPUT 基本構文とOSKB010091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010091を同じ出力で読み、範囲判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010091
    COMMAND ===> SDSF DA
    ISF031I OUTPUT 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の OUTPUT 基本構文 と OSKB010091 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### STATUS jobname オペランド {#c30-i0333}
*分類: TSO_SUBMIT*  ・  難易度: 中級

STATUS jobname オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 終端照合のオペランドに関係する STATUS jobname オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端照合の確認記録にまとめる。 ✅
    - B. STATUS jobname オペランドの名称と担当者名のみを残して終端照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で終端照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず終端照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合のオペランドにおいて選択記号 A を採用し、識別名は終端照合です。終端照合のオペランドにおいて STATUS jobname オペランド は説明欄の「STATUS jobname オペランドの用途を対話操作の表示で確認する終端照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合のオペランドに関連して、TSO ISPF SDSF では STATUS jobname オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合のオペランドは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合のオペランドは別カテゴリの確認を流用しており、STATUS jobname オペランドの根拠にならないため終端照合ではありません。 D: 終端照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため終端照合ではありません。終端照合のオペランドで使う STATUS jobname オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **STATUS jobname オペランド**

    - 検証目的: 出力判定のオペランドについて、STATUS jobname オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010088の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、出力判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSTATUS jobname オペラを指定し、OSKB010088の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND STATUS jobname オペラ
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM STATUS jobname オペラ
    CASE OSKB010088
    SOURCE TSO ISPF SDSF
    ```

    STATUS jobname オペラとOSKB010088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010088を同じ出力で読み、出力判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010088
    COMMAND ===> SDSF DA
    ISF031I STATUS jobname オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の STATUS jobname オペラ と OSKB010088 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### STATUS 基本構文 {#c30-i0334}
*分類: TSO_SUBMIT*  ・  難易度: 初級

STATUS 基本構文は、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 置換照合の基本構文に関する STATUS 基本構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず置換照合の基本構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の基本構文の証跡として保存して根拠にする。
    - C. STATUS 基本構文の変更点を出力本文から切り離して置換照合の基本構文の承認欄のみ残す。
    - D. SDSF DA の結果から対象行を抜き出し、置換照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換照合の基本構文において選択記号 D を採用し、識別名は置換照合です。置換照合の基本構文において STATUS 基本構文 は説明欄の「STATUS 基本構文の状態と出力メッセージを結び付ける置換照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の基本構文に関する記録は、STATUS 基本構文の出力行と ISF031I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため置換照合ではありません。 B: 置換照合の基本構文は別カテゴリの確認を流用しており、STATUS 基本構文の根拠にならないため置換照合ではありません。 C: 置換照合の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の基本構文は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の基本構文で記録する STATUS 基本構文は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **STATUS 基本構文**

    - 検証目的: 上書判定の基本構文について、STATUS 基本構文は、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、上書判定の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSTATUS 基本構文を指定し、OSKB010087の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND STATUS 基本構文
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM STATUS 基本構文
    CASE OSKB010087
    SOURCE TSO ISPF SDSF
    ```

    STATUS 基本構文とOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010087を同じ出力で読み、上書判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010087
    COMMAND ===> SDSF DA
    ISF031I STATUS 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の STATUS 基本構文 と OSKB010087 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### SUBMIT '...' オペランド {#c30-i0335}
*分類: TSO_SUBMIT*  ・  難易度: 中級

TSO ISPF SDSFのTSO_SUBMITでは、対象資源、指定値、実行時の出力を対応付けて確認します。TSO_SUBMITは、TSO ISPF SDSFの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUBMIT '...' オペランドの表記と許可される値を確認します。

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 監査確認のなど オペランドで対話操作の運用確認を行います。SUBMIT 'など' オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で監査確認のなど オペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず監査確認のなど オペランドを正常終了として記録する。
    - C. TSO ISPF SDSF の表示形式に沿って根拠行を採り、監査確認の点検結果を残す。 ✅
    - D. SUBMIT 'など' オペランドの属性行を読まず監査確認のなど オペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認のなど オペランドにおいて選択記号 C を採用し、識別名は監査確認です。監査確認のなど オペランドにおいて SUBMIT 'など' オペランド は説明欄の「TSO ISPF SDSF で SUBMIT 'など' オペランドの扱いを記録する監査確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のなど オペランドを受け取る担当者は、SUBMIT 'など' オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のなど オペランドは別カテゴリの確認を流用しており、SUBMIT 'など' オペランドの根拠にならないため監査確認ではありません。 B: 監査確認のなど オペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため監査確認ではありません。 C: 監査確認のなど オペランドは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のなど オペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のなど オペランドが示す SUBMIT 'など' オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200



### SUBMIT * (画面入力) {#c30-i0336}
*分類: TSO_SUBMIT*  ・  難易度: 中級

SUBMIT * (画面入力)は、TSO / ISPF / SDSFのTSO_SUBMITで操作画面や表示項目を確認するための項目です。入力欄、選択肢、実行後に変わる表示を分けて見ると、操作結果を追いやすくなります。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 変更確認の* 画面入力に関する SUBMIT * (画面入力)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず変更確認の* 画面入力の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の* 画面入力の証跡として保存して根拠にする。
    - C. SUBMIT * (画面入力)の変更点を出力本文から切り離して変更確認の* 画面入力の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認の* 画面入力において選択記号 D を採用し、識別名は変更確認です。変更確認の* 画面入力において SUBMIT * (画面入力) は説明欄の「SUBMIT * (画面入力)の状態と出力メッセージを結び付ける変更確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の* 画面入力に関する記録は、SUBMIT * (画面入力)の出力行と ISF031I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の* 画面入力は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため変更確認ではありません。 B: 変更確認の* 画面入力は別カテゴリの確認を流用しており、SUBMIT * (画面入力)の根拠にならないため変更確認ではありません。 C: 変更確認の* 画面入力は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の* 画面入力は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の* 画面入力で記録する SUBMIT * (画面入力)は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **SUBMIT * (画面入力)**

    - 検証目的: 呼出判定の* 画面入力について、SUBMIT * (画面入力)は、TSO / ISPF / SDSF の TSO_SUBMIT で操作画面や表示項目を確認するための項目です。入力欄、選択肢、実行後に変わる表示をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、呼出判定の* 画面入力の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSUBMIT * (画面入力)を指定し、OSKB010083の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SUBMIT * (画面入力)
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SUBMIT * (画面入力)
    CASE OSKB010083
    SOURCE TSO ISPF SDSF
    ```

    SUBMIT * (画面入力)とOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010083を同じ出力で読み、呼出判定の* 画面入力の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010083
    COMMAND ===> SDSF DA
    ISF031I SUBMIT * (画面入力) DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SUBMIT * (画面入力) と OSKB010083 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### SUBMIT JOBCHAR オペランド {#c30-i0337}
*分類: TSO_SUBMIT*  ・  難易度: 中級

SUBMIT JOBCHAR オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 展開照合のオペランドで SUBMIT JOBCHAR オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SUBMIT JOBCHAR オペランドの出力を取らず展開照合のオペランドの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開照合の根拠を固定する。 ✅
    - C. SDSF DA を省略して展開照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合のオペランドにおいて選択記号 B を採用し、識別名は展開照合です。展開照合のオペランドにおいて SUBMIT JOBCHAR オペランド は説明欄の「展開照合のオペランドに関係する定義値と表示行を照合する展開照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合のオペランドの証跡を読む担当者は、SUBMIT JOBCHAR オペランドの属性行と ISF031I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合のオペランドは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため展開照合ではありません。 D: 展開照合のオペランドは別カテゴリの確認を流用しており、SUBMIT JOBCHAR オペランドの根拠にならないため展開照合ではありません。展開照合のオペランドに出る SUBMIT JOBCHAR オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **SUBMIT JOBCHAR オペランド**

    - 検証目的: 終端判定のオペランドについて、SUBMIT JOBCHAR オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、終端判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSUBMIT JOBCHAR オペラを指定し、OSKB010085の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SUBMIT JOBCHAR オペラ
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SUBMIT JOBCHAR オペラ
    CASE OSKB010085
    SOURCE TSO ISPF SDSF
    ```

    SUBMIT JOBCHAR オペラとOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010085を同じ出力で読み、終端判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010085
    COMMAND ===> SDSF DA
    ISF031I SUBMIT JOBCHAR オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SUBMIT JOBCHAR オペラ と OSKB010085 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### SUBMIT NOTIFY オペランド {#c30-i0338}
*分類: TSO_SUBMIT*  ・  難易度: 中級

SUBMIT NOTIFY オペランドは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 構文照合のオペランドに関係する SUBMIT NOTIFY オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文照合の確認値として扱う。 ✅
    - B. SUBMIT NOTIFY オペランドの名称と担当者名のみを残して構文照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で構文照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず構文照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合のオペランドにおいて選択記号 A を採用し、識別名は構文照合です。構文照合のオペランドにおいて SUBMIT NOTIFY オペランド は説明欄の「SUBMIT NOTIFY オペランドの用途を対話操作の表示で確認する構文照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のオペランドに関連して、TSO ISPF SDSF では SUBMIT NOTIFY オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のオペランドは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のオペランドは別カテゴリの確認を流用しており、SUBMIT NOTIFY オペランドの根拠にならないため構文照合ではありません。 D: 構文照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため構文照合ではありません。構文照合のオペランドで使う SUBMIT NOTIFY オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **SUBMIT NOTIFY オペランド**

    - 検証目的: 置換判定のオペランドについて、SUBMIT NOTIFY オペランドは、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、置換判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSUBMIT NOTIFY オペランを指定し、OSKB010084の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SUBMIT NOTIFY オペラン
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SUBMIT NOTIFY オペラン
    CASE OSKB010084
    SOURCE TSO ISPF SDSF
    ```

    SUBMIT NOTIFY オペランとOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010084を同じ出力で読み、置換判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010084
    COMMAND ===> SDSF DA
    ISF031I SUBMIT NOTIFY オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SUBMIT NOTIFY オペラン と OSKB010084 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### SUBMIT USER/PASSWORD {#c30-i0339}
*分類: TSO_SUBMIT*  ・  難易度: 中級

SUBMIT USER/PASSWORDは、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **SUBMIT USER ・ PASSWORD**

    - 検証目的: 探索判定の・について、SUBMIT USER/PASSWORD は、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010086の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、探索判定の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSUBMIT USER ・ PASSを指定し、OSKB010086の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SUBMIT USER ・ PASS
    CASE OSKB010086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SUBMIT USER ・ PASS
    CASE OSKB010086
    SOURCE TSO ISPF SDSF
    ```

    SUBMIT USER ・ PASSとOSKB010086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010086を同じ出力で読み、探索判定の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010086
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010086
    COMMAND ===> SDSF DA
    ISF031I SUBMIT USER ・ PASSWORD DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SUBMIT USER ・ PASS と OSKB010086 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide



### SUBMIT 基本構文 {#c30-i0340}
*分類: TSO_SUBMIT*  ・  難易度: 初級

SUBMIT 基本構文は、TSO / ISPF / SDSFのTSO_SUBMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 復旧確認の基本構文で SUBMIT 基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SUBMIT 基本構文の出力を取らず復旧確認の基本構文の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧確認の確認にする。 ✅
    - C. SDSF DA を省略して復旧確認の基本構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧確認の基本構文において選択記号 B を採用し、識別名は復旧確認です。復旧確認の基本構文において SUBMIT 基本構文 は説明欄の「復旧確認の基本構文に関係する定義値と表示行を照合する復旧確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の基本構文の証跡を読む担当者は、SUBMIT 基本構文の属性行と ISF031I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の基本構文は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の基本構文は別カテゴリの確認を流用しており、SUBMIT 基本構文の根拠にならないため復旧確認ではありません。復旧確認の基本構文に出る SUBMIT 基本構文は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **SUBMIT 基本構文**

    - 検証目的: 構文判定の基本構文について、SUBMIT 基本構文は、TSO / ISPF / SDSF の TSO_SUBMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、構文判定の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSUBMIT 基本構文を指定し、OSKB010081の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SUBMIT 基本構文
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SUBMIT 基本構文
    CASE OSKB010081
    SOURCE TSO ISPF SDSF
    ```

    SUBMIT 基本構文とOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010081を同じ出力で読み、構文判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010081
    COMMAND ===> SDSF DA
    ISF031I SUBMIT 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SUBMIT 基本構文 と OSKB010081 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide




## TSO / ISPF / SDSF > TSO_XMIT

### RECEIVE DELETE オペランド {#c30-i0341}
*分類: TSO_XMIT*  ・  難易度: 中級

RECEIVE DELETE オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **RECEIVE DELETE オペランド**

    - 検証目的: 変更整理のオペランドについて、RECEIVE DELETE オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010120の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRECEIVE DELETE オペラを指定し、OSKB010120の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RECEIVE DELETE オペラ
    CASE OSKB010120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RECEIVE DELETE オペラ
    CASE OSKB010120
    SOURCE TSO ISPF SDSF
    ```

    RECEIVE DELETE オペラとOSKB010120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010120を同じ出力で読み、変更整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010120
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010120
    COMMAND ===> SDSF DA
    ISF031I RECEIVE DELETE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RECEIVE DELETE オペラ と OSKB010120 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### RECEIVE INDATASET オペランド {#c30-i0342}
*分類: TSO_XMIT*  ・  難易度: 中級

RECEIVE INDATASET オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **RECEIVE INDATASET オペランド**

    - 検証目的: 復旧整理のオペランドについて、RECEIVE INDATASET オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010118の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、復旧整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRECEIVE INDATASET を指定し、OSKB010118の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RECEIVE INDATASET 
    CASE OSKB010118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RECEIVE INDATASET 
    CASE OSKB010118
    SOURCE TSO ISPF SDSF
    ```

    RECEIVE INDATASET とOSKB010118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010118を同じ出力で読み、復旧整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010118
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010118
    COMMAND ===> SDSF DA
    ISF031I RECEIVE INDATASET オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RECEIVE INDATASET  と OSKB010118 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### RECEIVE NOTIFY オペランド {#c30-i0343}
*分類: TSO_XMIT*  ・  難易度: 中級

RECEIVE NOTIFY オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **RECEIVE NOTIFY オペランド**

    - 検証目的: 監査整理のオペランドについて、RECEIVE NOTIFY オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010119の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、監査整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRECEIVE NOTIFY オペラを指定し、OSKB010119の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RECEIVE NOTIFY オペラ
    CASE OSKB010119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RECEIVE NOTIFY オペラ
    CASE OSKB010119
    SOURCE TSO ISPF SDSF
    ```

    RECEIVE NOTIFY オペラとOSKB010119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010119を同じ出力で読み、監査整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010119
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010119
    COMMAND ===> SDSF DA
    ISF031I RECEIVE NOTIFY オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RECEIVE NOTIFY オペラ と OSKB010119 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### RECEIVE RESTORE オペランド {#c30-i0344}
*分類: TSO_XMIT*  ・  難易度: 中級

RECEIVE RESTORE オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **RECEIVE RESTORE オペランド**

    - 検証目的: 構文確認のオペランドについて、RECEIVE RESTORE オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020001の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、構文確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRECEIVE RESTORE オペを指定し、OSKB020001の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RECEIVE RESTORE オペ
    CASE OSKB020001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RECEIVE RESTORE オペ
    CASE OSKB020001
    SOURCE TSO ISPF SDSF
    ```

    RECEIVE RESTORE オペとOSKB020001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020001を同じ出力で読み、構文確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020001
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020001
    COMMAND ===> SDSF DA
    ISF031I RECEIVE RESTORE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RECEIVE RESTORE オペ と OSKB020001 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### RECEIVE 基本構文 {#c30-i0345}
*分類: TSO_XMIT*  ・  難易度: 初級

RECEIVE 基本構文は、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **RECEIVE 基本構文**

    - 検証目的: 警告整理の基本構文について、RECEIVE 基本構文は、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010117の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告整理の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRECEIVE 基本構文を指定し、OSKB010117の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RECEIVE 基本構文
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RECEIVE 基本構文
    CASE OSKB010117
    SOURCE TSO ISPF SDSF
    ```

    RECEIVE 基本構文とOSKB010117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010117を同じ出力で読み、警告整理の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010117
    COMMAND ===> SDSF DA
    ISF031I RECEIVE 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RECEIVE 基本構文 と OSKB010117 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### TRANSMIT (XMIT) 基本構文 {#c30-i0346}
*分類: TSO_XMIT*  ・  難易度: 初級

TRANSMIT (XMIT) 基本構文は、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 置換追跡の基本構文に関する TRANSMIT (XMIT) 基本構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず置換追跡の基本構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の基本構文の証跡として保存して根拠にする。
    - C. TRANSMIT (XMIT) 基本構文の変更点を出力本文から切り離して置換追跡の基本構文の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換追跡で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換追跡の基本構文において選択記号 D を採用し、識別名は置換追跡です。置換追跡の基本構文において TRANSMIT (XMIT) 基本構文 は説明欄の「TRANSMIT (XMIT) 基本構文の状態と出力メッセージを結び付ける置換追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の基本構文に関する記録は、TRANSMIT (XMIT) 基本構文の出力行と ISF031I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の基本構文は別カテゴリの確認を流用しており、TRANSMIT (XMIT) 基本構文の根拠にならないため置換追跡ではありません。 C: 置換追跡の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の基本構文は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の基本構文で記録する TRANSMIT (XMIT) 基本構文は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **TRANSMIT (XMIT) 基本構文**

    - 検証目的: 上書整理の基本構文について、TRANSMIT (XMIT) 基本構文は、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010107の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、上書整理の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にTRANSMIT (XMIT) 基本を指定し、OSKB010107の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND TRANSMIT (XMIT) 基本
    CASE OSKB010107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM TRANSMIT (XMIT) 基本
    CASE OSKB010107
    SOURCE TSO ISPF SDSF
    ```

    TRANSMIT (XMIT) 基本とOSKB010107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010107を同じ出力で読み、上書整理の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010107
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010107
    COMMAND ===> SDSF DA
    ISF031I TRANSMIT (XMIT) 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の TRANSMIT (XMIT) 基本 と OSKB010107 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT COMPRESS オペランド {#c30-i0347}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT COMPRESS オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **XMIT COMPRESS オペランド**

    - 検証目的: 値域整理のオペランドについて、XMIT COMPRESS オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010116の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT COMPRESS オペランを指定し、OSKB010116の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT COMPRESS オペラン
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT COMPRESS オペラン
    CASE OSKB010116
    SOURCE TSO ISPF SDSF
    ```

    XMIT COMPRESS オペランとOSKB010116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010116を同じ出力で読み、値域整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010116
    COMMAND ===> SDSF DA
    ISF031I XMIT COMPRESS オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT COMPRESS オペラン と OSKB010116 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT DATASET オペランド {#c30-i0348}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT DATASET オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 探索追跡のオペランドで XMIT DATASET オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. XMIT DATASET オペランドの出力を取らず探索追跡のオペランドの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索追跡の根拠を固定する。 ✅
    - C. SDSF DA を省略して探索追跡のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡のオペランドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡のオペランドにおいて XMIT DATASET オペランド は説明欄の「探索追跡のオペランドに関係する定義値と表示行を照合する探索追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のオペランドの証跡を読む担当者は、XMIT DATASET オペランドの属性行と ISF031I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のオペランドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のオペランドは別カテゴリの確認を流用しており、XMIT DATASET オペランドの根拠にならないため探索追跡ではありません。探索追跡のオペランドに出る XMIT DATASET オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **XMIT DATASET オペランド**

    - 検証目的: 条件整理のオペランドについて、XMIT DATASET オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010109の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、条件整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT DATASET オペランドを指定し、OSKB010109の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT DATASET オペランド
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT DATASET オペランド
    CASE OSKB010109
    SOURCE TSO ISPF SDSF
    ```

    XMIT DATASET オペランドとOSKB010109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010109を同じ出力で読み、条件整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010109
    COMMAND ===> SDSF DA
    ISF031I XMIT DATASET オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT DATASET オペランド と OSKB010109 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT ENCIPHER オペランド {#c30-i0349}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT ENCIPHER オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **XMIT ENCIPHER オペランド**

    - 検証目的: 順序整理のオペランドについて、XMIT ENCIPHER オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010115の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、順序整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT ENCIPHER オペランを指定し、OSKB010115の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT ENCIPHER オペラン
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT ENCIPHER オペラン
    CASE OSKB010115
    SOURCE TSO ISPF SDSF
    ```

    XMIT ENCIPHER オペランとOSKB010115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010115を同じ出力で読み、順序整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010115
    COMMAND ===> SDSF DA
    ISF031I XMIT ENCIPHER オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT ENCIPHER オペラン と OSKB010115 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT MEMBERS オペランド {#c30-i0350}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT MEMBERS オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 上書追跡のオペランドで対話操作の運用確認を行います。XMIT MEMBERS オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で上書追跡のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず上書追跡のオペランドを正常終了として記録する。
    - C. ISF031I を含む表示を保存し、説明欄との差分を上書追跡で確認する。 ✅
    - D. XMIT MEMBERS オペランドの属性行を読まず上書追跡のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のオペランドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のオペランドにおいて XMIT MEMBERS オペランド は説明欄の「TSO ISPF SDSF で XMIT MEMBERS オペランドの扱いを記録する上書追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のオペランドを受け取る担当者は、XMIT MEMBERS オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のオペランドは別カテゴリの確認を流用しており、XMIT MEMBERS オペランドの根拠にならないため上書追跡ではありません。 B: 上書追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のオペランドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のオペランドが示す XMIT MEMBERS オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **XMIT MEMBERS オペランド**

    - 検証目的: 区切整理のオペランドについて、XMIT MEMBERS オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010110の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、区切整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT MEMBERS オペランドを指定し、OSKB010110の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT MEMBERS オペランド
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT MEMBERS オペランド
    CASE OSKB010110
    SOURCE TSO ISPF SDSF
    ```

    XMIT MEMBERS オペランドとOSKB010110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010110を同じ出力で読み、区切整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010110
    COMMAND ===> SDSF DA
    ISF031I XMIT MEMBERS オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT MEMBERS オペランド と OSKB010110 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT MSGDATASET オペランド {#c30-i0351}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT MSGDATASET オペランドは、TSO / ISPF / SDSFのTSO_XMITでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 出力追跡のオペランドに関する XMIT MSGDATASET オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず出力追跡のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のオペランドの証跡として保存して根拠にする。
    - C. XMIT MSGDATASET オペランドの変更点を出力本文から切り離して出力追跡のオペランドの承認欄のみ残す。
    - D. SDSF DA の結果から対象行を抜き出し、出力追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡のオペランドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡のオペランドにおいて XMIT MSGDATASET オペランド は説明欄の「XMIT MSGDATASET オペランドの状態と出力メッセージを結び付ける出力追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のオペランドに関する記録は、XMIT MSGDATASET オペランドの出力行と ISF031I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のオペランドは別カテゴリの確認を流用しており、XMIT MSGDATASET オペランドの根拠にならないため出力追跡ではありません。 C: 出力追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のオペランドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のオペランドで記録する XMIT MSGDATASET オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **XMIT MSGDATASET オペランド**

    - 検証目的: 範囲整理のオペランドについて、XMIT MSGDATASET オペランドは、TSO / ISPF / SDSF の TSO_XMIT でメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010111の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、範囲整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT MSGDATASET オペを指定し、OSKB010111の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT MSGDATASET オペ
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT MSGDATASET オペ
    CASE OSKB010111
    SOURCE TSO ISPF SDSF
    ```

    XMIT MSGDATASET オペとOSKB010111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010111を同じ出力で読み、範囲整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010111
    COMMAND ===> SDSF DA
    ISF031I XMIT MSGDATASET オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT MSGDATASET オペ と OSKB010111 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT NOTIFY オペランド {#c30-i0352}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT NOTIFY オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 条件追跡のオペランドに関係する XMIT NOTIFY オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件追跡の確認記録にまとめる。 ✅
    - B. XMIT NOTIFY オペランドの名称と担当者名のみを残して条件追跡のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で条件追跡のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず条件追跡のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡のオペランドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡のオペランドにおいて XMIT NOTIFY オペランド は説明欄の「XMIT NOTIFY オペランドの用途を対話操作の表示で確認する条件追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡のオペランドに関連して、TSO ISPF SDSF では XMIT NOTIFY オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡のオペランドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡のオペランドは別カテゴリの確認を流用しており、XMIT NOTIFY オペランドの根拠にならないため条件追跡ではありません。 D: 条件追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため条件追跡ではありません。条件追跡のオペランドで使う XMIT NOTIFY オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は条件追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **XMIT NOTIFY オペランド**

    - 検証目的: 優先整理のオペランドについて、XMIT NOTIFY オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010112の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、優先整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT NOTIFY オペランドを指定し、OSKB010112の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT NOTIFY オペランド
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT NOTIFY オペランド
    CASE OSKB010112
    SOURCE TSO ISPF SDSF
    ```

    XMIT NOTIFY オペランドとOSKB010112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010112を同じ出力で読み、優先整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010112
    COMMAND ===> SDSF DA
    ISF031I XMIT NOTIFY オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT NOTIFY オペランド と OSKB010112 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT SYSOUT オペランド {#c30-i0353}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT SYSOUT オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? note "検証手順（1件）"
    **XMIT SYSOUT オペランド**

    - 検証目的: 比較整理のオペランドについて、XMIT SYSOUT オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010114の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、比較整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT SYSOUT オペランドを指定し、OSKB010114の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT SYSOUT オペランド
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT SYSOUT オペランド
    CASE OSKB010114
    SOURCE TSO ISPF SDSF
    ```

    XMIT SYSOUT オペランドとOSKB010114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010114を同じ出力で読み、比較整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010114
    COMMAND ===> SDSF DA
    ISF031I XMIT SYSOUT オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT SYSOUT オペランド と OSKB010114 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT TERMINAL オペランド {#c30-i0354}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT TERMINAL オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 区切追跡のオペランドで XMIT TERMINAL オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. XMIT TERMINAL オペランドの出力を取らず区切追跡のオペランドの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切追跡の根拠にする。 ✅
    - C. SDSF DA を省略して区切追跡のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡のオペランドにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡のオペランドにおいて XMIT TERMINAL オペランド は説明欄の「区切追跡のオペランドに関係する定義値と表示行を照合する区切追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡のオペランドの証跡を読む担当者は、XMIT TERMINAL オペランドの属性行と ISF031I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡のオペランドは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡のオペランドは別カテゴリの確認を流用しており、XMIT TERMINAL オペランドの根拠にならないため区切追跡ではありません。区切追跡のオペランドに出る XMIT TERMINAL オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **XMIT TERMINAL オペランド**

    - 検証目的: 記録整理のオペランドについて、XMIT TERMINAL オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010113の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、記録整理のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT TERMINAL オペランを指定し、OSKB010113の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT TERMINAL オペラン
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT TERMINAL オペラン
    CASE OSKB010113
    SOURCE TSO ISPF SDSF
    ```

    XMIT TERMINAL オペランとOSKB010113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010113を同じ出力で読み、記録整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010113
    COMMAND ===> SDSF DA
    ISF031I XMIT TERMINAL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT TERMINAL オペラン と OSKB010113 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)



### XMIT 宛先 オペランド {#c30-i0355}
*分類: TSO_XMIT*  ・  難易度: 中級

XMIT 宛先 オペランドは、TSO / ISPF / SDSFのTSO_XMITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference (TRANSMIT/RECEIVE) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)

??? question "確認問題（1問）"
    **問題.** 終端追跡の宛先 オペランドに関係する XMIT 宛先 オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端追跡の確認値として扱う。 ✅
    - B. XMIT 宛先 オペランドの名称と担当者名のみを残して終端追跡の宛先 オペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で終端追跡の宛先 オペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず終端追跡の宛先 オペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡の宛先 オペランドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡の宛先 オペランドにおいて XMIT 宛先 オペランド は説明欄の「XMIT 宛先 オペランドの用途を対話操作の表示で確認する終端追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の宛先 オペランドに関連して、TSO ISPF SDSF では XMIT 宛先 オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の宛先 オペランドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の宛先 オペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の宛先 オペランドは別カテゴリの確認を流用しており、XMIT 宛先 オペランドの根拠にならないため終端追跡ではありません。 D: 終端追跡の宛先 オペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため終端追跡ではありません。終端追跡の宛先 オペランドで使う XMIT 宛先 オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **XMIT 宛先 オペランド**

    - 検証目的: 出力整理の宛先 オペランドについて、XMIT 宛先 オペランドは、TSO / ISPF / SDSF の TSO_XMIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010108の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、出力整理の宛先 オペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にXMIT 宛先 オペランドを指定し、OSKB010108の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND XMIT 宛先 オペランド
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM XMIT 宛先 オペランド
    CASE OSKB010108
    SOURCE TSO ISPF SDSF
    ```

    XMIT 宛先 オペランドとOSKB010108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010108を同じ出力で読み、出力整理の宛先 オペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010108
    COMMAND ===> SDSF DA
    ISF031I XMIT 宛先 オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の XMIT 宛先 オペランド と OSKB010108 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TRANSMIT / RECEIVE)


