---
search:
  exclude: true
---

# RACF SETROPTS/RDEFINE/RACDCERT — 詳細 (5/6)

[← RACF SETROPTS/RDEFINE/RACDCERT の概要へ戻る](index.md)


## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE オペランド

### AUDIT(ALL(READ)) {#c26-i0298}
*分類: RDEFINE オペランド*  ・  難易度: 上級

AUDIT(ALL(READ))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **AUDIT(ALL(READ))**

    - 検証目的: 順序確認のオペランドについて、AUDIT(ALL(READ))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(ALL(READ))を指定し、OSKB020015の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND AUDIT(ALL(READ))
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM AUDIT(ALL(READ))
    CASE OSKB020015
    SOURCE RACF
    ```

    AUDIT(ALL(READ))とOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020015を同じ出力で読み、順序確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020015 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I AUDIT(ALL(READ)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の AUDIT(ALL(READ)) と OSKB020015 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### AUDIT(ALL|SUCCESS|FAILURES|NONE) {#c26-i0299}
*分類: RDEFINE オペランド*  ・  難易度: 上級

AUDIT(ALL|SUCCESS|FAILURES|NONE)は、アクセス監査レベル指定。「AUDIT(ALL|SUCCESS|FAILURES|NONE)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **AUDIT(ALL|SUCCESS|FAILURES|NONE)**

    - 検証目的: 比較確認の| |について、AUDIT(ALL|SUCCESS|FAILURES|NONE)は、アクセス監査レベル指定。「AUDIT(ALL|SUCCESS|FAILURES|NONE)」を確認するとに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較確認の| |の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(ALL|SUCCESS|を指定し、OSKB020014の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND AUDIT(ALL|SUCCESS|
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM AUDIT(ALL|SUCCESS|
    CASE OSKB020014
    SOURCE RACF
    ```

    AUDIT(ALL|SUCCESS|とOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020014を同じ出力で読み、比較確認の| |の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020014 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I AUDIT(ALL|SUCCESS|FAILUR INFORMATION LISTED
    ```

    IRRD105IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の AUDIT(ALL|SUCCESS| と OSKB020014 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### AUDIT(FAILURES(UPDATE)) {#c26-i0300}
*分類: RDEFINE オペランド*  ・  難易度: 上級

AUDIT(FAILURES(UPDATE))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **AUDIT(FAILURES(UPDATE))**

    - 検証目的: 値域確認のオペランドについて、AUDIT(FAILURES(UPDATE))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(FAILURES(UPDを指定し、OSKB020016の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND AUDIT(FAILURES(UPD
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM AUDIT(FAILURES(UPD
    CASE OSKB020016
    SOURCE RACF
    ```

    AUDIT(FAILURES(UPDとOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020016を同じ出力で読み、値域確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020016 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I AUDIT(FAILURES(UPDATE)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の AUDIT(FAILURES(UPD と OSKB020016 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### CATEGORY(name1,name2,…) {#c26-i0301}
*分類: RDEFINE オペランド*  ・  難易度: 上級

CATEGORY(name1,name2,…)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### DATA('text') {#c26-i0302}
*分類: RDEFINE オペランド*  ・  難易度: 上級

DATA('text')は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **DATA('text')**

    - 検証目的: 展開照合のオペランドについて、DATA('text')は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にDATA('text')を指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DATA('text')
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DATA('text')
    CASE OSKB020022
    SOURCE RACF
    ```

    DATA('text')とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020022を同じ出力で読み、展開照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020022 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DATA('text') INFORMATION LISTED
    ```

    IRRD105IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DATA('text') と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### FCLASS(クラス名) {#c26-i0303}
*分類: RDEFINE オペランド*  ・  難易度: 上級

FCLASS(クラス名)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **FCLASS(クラス名)**

    - 検証目的: 上書照合のクラス名について、FCLASS(クラス名)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書照合のクラス名の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にFCLASS(クラス名)を指定し、OSKB020027の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND FCLASS(クラス名)
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM FCLASS(クラス名)
    CASE OSKB020027
    SOURCE RACF
    ```

    FCLASS(クラス名)とOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020027を同じ出力で読み、上書照合のクラス名の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020027 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I FCLASS(クラス名) INFORMATION LISTED
    ```

    IRRD105IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の FCLASS(クラス名) と OSKB020027 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### FGENERIC {#c26-i0304}
*分類: RDEFINE オペランド*  ・  難易度: 上級

FGENERICは、FROM の汎用プロファイル指定。「FGENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **FGENERIC**

    - 検証目的: 条件照合のオペランドについて、FGENERIC は、FROM の汎用プロファイル指定。「FGENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にFGENERICを指定し、OSKB020029の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND FGENERIC
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM FGENERIC
    CASE OSKB020029
    SOURCE RACF
    ```

    FGENERICとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020029を同じ出力で読み、条件照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020029 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I FGENERIC INFORMATION LISTED
    ```

    IRRD105IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の FGENERIC と OSKB020029 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### FROM(プロファイル名) {#c26-i0305}
*分類: RDEFINE オペランド*  ・  難易度: 上級

FROM(プロファイル名)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **FROM(プロファイル名)**

    - 検証目的: 出力照合のプロファイル名について、FROM(プロファイル名)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力照合のプロファイル名の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にFROM(プロファイル名)を指定し、OSKB020028の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND FROM(プロファイル名)
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM FROM(プロファイル名)
    CASE OSKB020028
    SOURCE RACF
    ```

    FROM(プロファイル名)とOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020028を同じ出力で読み、出力照合のプロファイル名の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020028 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I FROM(プロファイル名) INFORMATION LISTED
    ```

    IRRD105IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の FROM(プロファイル名) と OSKB020028 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### LEVEL(n) {#c26-i0306}
*分類: RDEFINE オペランド*  ・  難易度: 上級

LEVEL(n)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **LEVEL(n)**

    - 検証目的: 構文照合のオペランドについて、LEVEL(n)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にLEVEL(n)を指定し、OSKB020021の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND LEVEL(n)
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM LEVEL(n)
    CASE OSKB020021
    SOURCE RACF
    ```

    LEVEL(n)とOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020021を同じ出力で読み、構文照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020021 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I LEVEL(n) INFORMATION LISTED
    ```

    IRRD105IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の LEVEL(n) と OSKB020021 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### MODEL(profile) {#c26-i0307}
*分類: RDEFINE オペランド*  ・  難易度: 上級

MODEL(profile)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **MODEL(profile)**

    - 検証目的: 区切照合のオペランドについて、MODEL(profile)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にMODEL(profile)を指定し、OSKB020030の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND MODEL(profile)
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM MODEL(profile)
    CASE OSKB020030
    SOURCE RACF
    ```

    MODEL(profile)とOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020030を同じ出力で読み、区切照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020030 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I MODEL(profile) INFORMATION LISTED
    ```

    IRRD105IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の MODEL(profile) と OSKB020030 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### NONOTIFY {#c26-i0308}
*分類: RDEFINE オペランド*  ・  難易度: 上級

NONOTIFYは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **NONOTIFY**

    - 検証目的: 復旧確認のオペランドについて、NONOTIFY は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNONOTIFYを指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NONOTIFY
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NONOTIFY
    CASE OSKB020018
    SOURCE RACF
    ```

    NONOTIFYとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020018を同じ出力で読み、復旧確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020018 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I NONOTIFY INFORMATION LISTED
    ```

    IRRD105IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の NONOTIFY と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### NOTIFY(userid) {#c26-i0309}
*分類: RDEFINE オペランド*  ・  難易度: 上級

NOTIFY(userid)は、アクセス違反時に通知するユーザ ID。「NOTIFY(userid)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **NOTIFY(userid)**

    - 検証目的: 警告確認のオペランドについて、NOTIFY(userid)は、アクセス違反時に通知するユーザ ID。「NOTIFY(userid)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNOTIFY(userid)を指定し、OSKB020017の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NOTIFY(userid)
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NOTIFY(userid)
    CASE OSKB020017
    SOURCE RACF
    ```

    NOTIFY(userid)とOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020017を同じ出力で読み、警告確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020017 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I NOTIFY(userid) INFORMATION LISTED
    ```

    IRRD105IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の NOTIFY(userid) と OSKB020017 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### NOWARNING {#c26-i0310}
*分類: RDEFINE オペランド*  ・  難易度: 上級

NOWARNINGは、WARNING モード解除。「NOWARNING」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **NOWARNING**

    - 検証目的: 変更確認のオペランドについて、NOWARNING は、WARNING モード解除。「NOWARNING」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNOWARNINGを指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NOWARNING
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NOWARNING
    CASE OSKB020020
    SOURCE RACF
    ```

    NOWARNINGとOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020020を同じ出力で読み、変更確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020020 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I NOWARNING INFORMATION LISTED
    ```

    IRRD105IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の NOWARNING と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### OWNER(userid|group) {#c26-i0311}
*分類: RDEFINE オペランド*  ・  難易度: 上級

OWNER(userid|group)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **OWNER(userid|group)**

    - 検証目的: 記録確認の|について、OWNER(userid|group)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録確認の|の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にOWNER(userid|groupを指定し、OSKB020013の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND OWNER(userid|group
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM OWNER(userid|group
    CASE OSKB020013
    SOURCE RACF
    ```

    OWNER(userid|groupとOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020013を同じ出力で読み、記録確認の|の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020013 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I OWNER(userid|group) INFORMATION LISTED
    ```

    IRRD105IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の OWNER(userid|group と OSKB020013 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLABEL(label) {#c26-i0312}
*分類: RDEFINE オペランド*  ・  難易度: 上級

SECLABEL(label)は、セキュリティ ラベル (MLS 環境用)。「SECLABEL(label)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLABEL(label)**

    - 検証目的: 探索照合のオペランドについて、SECLABEL(label)は、セキュリティ ラベル (MLS 環境用)。「SECLABEL(label)」を確認すると、SETROPTS、RDEFINE、RACDCERに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL(label)を指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLABEL(label)
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLABEL(label)
    CASE OSKB020026
    SOURCE RACF
    ```

    SECLABEL(label)とOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020026を同じ出力で読み、探索照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020026 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLABEL(label) INFORMATION LISTED
    ```

    IRRD105IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLABEL(label) と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLEVEL(name) {#c26-i0313}
*分類: RDEFINE オペランド*  ・  難易度: 上級

SECLEVEL(name)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLEVEL(name)**

    - 検証目的: 置換照合のオペランドについて、SECLEVEL(name)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLEVEL(name)を指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLEVEL(name)
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLEVEL(name)
    CASE OSKB020024
    SOURCE RACF
    ```

    SECLEVEL(name)とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020024を同じ出力で読み、置換照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020024 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLEVEL(name) INFORMATION LISTED
    ```

    IRRD105IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLEVEL(name) と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SINGLEDSN {#c26-i0314}
*分類: RDEFINE オペランド*  ・  難易度: 上級

SINGLEDSNは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SINGLEDSN**

    - 検証目的: 値域照合のオペランドについて、SINGLEDSN は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSINGLEDSNを指定し、OSKB020036の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SINGLEDSN
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SINGLEDSN
    CASE OSKB020036
    SOURCE RACF
    ```

    SINGLEDSNとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020036を同じ出力で読み、値域照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020036 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SINGLEDSN INFORMATION LISTED
    ```

    IRRD105IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SINGLEDSN と OSKB020036 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### TIMEZONE(±hh:mm) {#c26-i0315}
*分類: RDEFINE オペランド*  ・  難易度: 上級

TIMEZONE(±hh:mm)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **TIMEZONE(±hh:mm)**

    - 検証目的: 範囲照合の± :について、TIMEZONE(±hh:mm)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲照合の± :の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にTIMEZONE(±hh:mm)を指定し、OSKB020031の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND TIMEZONE(±hh:mm)
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM TIMEZONE(±hh:mm)
    CASE OSKB020031
    SOURCE RACF
    ```

    TIMEZONE(±hh:mm)とOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020031を同じ出力で読み、範囲照合の± :の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020031 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I TIMEZONE(±hh:mm) INFORMATION LISTED
    ```

    IRRD105IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の TIMEZONE(±hh:mm) と OSKB020031 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### UACC(READ|UPDATE|CONTROL|ALTER|NONE) {#c26-i0316}
*分類: RDEFINE オペランド*  ・  難易度: 上級

UACC(READ|UPDATE|CONTROL|ALTER|NONE)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### VOLUME(volser) {#c26-i0317}
*分類: RDEFINE オペランド*  ・  難易度: 上級

VOLUME(volser)は、TAPEVOL/DASDVOL のボリューム名。「VOLUME(volser)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **VOLUME(volser)**

    - 検証目的: 順序照合のオペランドについて、VOLUME(volser)は、TAPEVOL/DASDVOL のボリューム名。「VOLUME(volser)」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序照合のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にVOLUME(volser)を指定し、OSKB020035の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND VOLUME(volser)
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM VOLUME(volser)
    CASE OSKB020035
    SOURCE RACF
    ```

    VOLUME(volser)とOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020035を同じ出力で読み、順序照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020035 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I VOLUME(volser) INFORMATION LISTED
    ```

    IRRD105IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の VOLUME(volser) と OSKB020035 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### WARNING {#c26-i0318}
*分類: RDEFINE オペランド*  ・  難易度: 上級

WARNINGは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **WARNING**

    - 検証目的: 監査確認のオペランドについて、WARNING は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にWARNINGを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WARNING
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WARNING
    CASE OSKB020019
    SOURCE RACF
    ```

    WARNINGとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020019を同じ出力で読み、監査確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020019 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I WARNING INFORMATION LISTED
    ```

    IRRD105IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の WARNING と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### WHEN(DAYS(…)|TIME(…)) {#c26-i0319}
*分類: RDEFINE オペランド*  ・  難易度: 上級

WHEN(DAYS(…)|TIME(…))は、アクセス可能な曜日/時間帯。「WHEN(DAYS(…)|TIME(…))」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)



## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE 基本

### GENERIC キーワード {#c26-i0320}
*分類: RDEFINE 基本*  ・  難易度: 上級

GENERIC キーワードは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **GENERIC キーワード**

    - 検証目的: 区切確認のキーワードについて、GENERIC キーワードは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切確認のキーワードの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にGENERIC キーワードを指定し、OSKB020010の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND GENERIC キーワード
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM GENERIC キーワード
    CASE OSKB020010
    SOURCE RACF
    ```

    GENERIC キーワードとOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020010を同じ出力で読み、区切確認のキーワードの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020010 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I GENERIC キーワード INFORMATION LISTED
    ```

    IRRD105IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の GENERIC キーワード と OSKB020010 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDEFINE の目的 {#c26-i0321}
*分類: RDEFINE 基本*  ・  難易度: 上級

RDEFINE の目的は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **RDEFINE の目的**

    - 検証目的: 置換確認のの目的について、RDEFINE の目的は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換確認のの目的の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDEFINE の目的を指定し、OSKB020004の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDEFINE の目的
    CASE OSKB020004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDEFINE の目的
    CASE OSKB020004
    SOURCE RACF
    ```

    RDEFINE の目的とOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020004を同じ出力で読み、置換確認のの目的の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020004
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020004 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDEFINE の目的 INFORMATION LISTED
    ```

    IRRD105IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDEFINE の目的 と OSKB020004 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDEFINE 構文 {#c26-i0322}
*分類: RDEFINE 基本*  ・  難易度: 上級

RDEFINE 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **RDEFINE 構文**

    - 検証目的: 探索確認の構文について、RDEFINE 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020006の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索確認の構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDEFINE 構文を指定し、OSKB020006の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDEFINE 構文
    CASE OSKB020006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDEFINE 構文
    CASE OSKB020006
    SOURCE RACF
    ```

    RDEFINE 構文とOSKB020006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020006を同じ出力で読み、探索確認の構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020006
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020006 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDEFINE 構文 INFORMATION LISTED
    ```

    IRRD105IとOSKB020006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDEFINE 構文 と OSKB020006 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDEFINE 短縮形 RDEF {#c26-i0323}
*分類: RDEFINE 基本*  ・  難易度: 上級

RDEFINE は RDEF と省略可。「RDEFINE 短縮形 RDEF」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **RDEFINE 短縮形 RDEF**

    - 検証目的: 終端確認の短縮形について、RDEFINE は RDEF と省略可。「RDEFINE 短縮形 RDEF」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端確認の短縮形の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDEFINE 短縮形 RDEFを指定し、OSKB020005の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDEFINE 短縮形 RDEF
    CASE OSKB020005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDEFINE 短縮形 RDEF
    CASE OSKB020005
    SOURCE RACF
    ```

    RDEFINE 短縮形 RDEFとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020005を同じ出力で読み、終端確認の短縮形の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020005
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020005 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDEFINE 短縮形 RDEF INFORMATION LISTED
    ```

    IRRD105IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDEFINE 短縮形 RDEF と OSKB020005 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### クラス名指定 {#c26-i0324}
*分類: RDEFINE 基本*  ・  難易度: 上級

クラス名指定は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **クラス名指定**

    - 検証目的: 上書確認のクラス名指定について、クラス名指定は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書確認のクラス名指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にクラス名指定を指定し、OSKB020007の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND クラス名指定
    CASE OSKB020007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM クラス名指定
    CASE OSKB020007
    SOURCE RACF
    ```

    クラス名指定とOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020007を同じ出力で読み、上書確認のクラス名指定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020007
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020007 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I クラス名指定 INFORMATION LISTED
    ```

    IRRD105IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の クラス名指定 と OSKB020007 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### プロファイル名長 {#c26-i0325}
*分類: RDEFINE 基本*  ・  難易度: 上級

プロファイル名長は、クラスごとに最大長が CDT で定義 (通常 246 文字)。「プロファイル名長」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **プロファイル名長**

    - 検証目的: 出力確認のプロファイル名長について、プロファイル名長は、クラスごとに最大長が CDT で定義 (通常 246 文字)。「プロファイル名長」を確認すると、SETROPTS、RDEFINE、RACDCERT の変に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力確認のプロファイル名長の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にプロファイル名長を指定し、OSKB020008の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND プロファイル名長
    CASE OSKB020008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM プロファイル名長
    CASE OSKB020008
    SOURCE RACF
    ```

    プロファイル名長とOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020008を同じ出力で読み、出力確認のプロファイル名長の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020008
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020008 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I プロファイル名長 INFORMATION LISTED
    ```

    IRRD105IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の プロファイル名長 と OSKB020008 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### メンバ クラス vs グルーピング クラス {#c26-i0326}
*分類: RDEFINE 基本*  ・  難易度: 上級

メンバ クラス vs グルーピング クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。メンバ クラス vs グルーピング クラスは、メンバ クラス (FACILITY 等) と GROUP クラス (GFACILIT 等) の対

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **メンバ クラス vs グルーピング クラス**

    - 検証目的: 範囲確認のメンバ クラス グルーピング クラスについて、メンバ クラス vs グルーピング クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲確認のメンバ クラス グルーピング クラスの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にメンバ クラス vs グルーピング を指定し、OSKB020011の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND メンバ クラス vs グルーピング 
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM メンバ クラス vs グルーピング 
    CASE OSKB020011
    SOURCE RACF
    ```

    メンバ クラス vs グルーピング とOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020011を同じ出力で読み、範囲確認のメンバ クラス グルーピング クラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020011 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I メンバ クラス vs グルーピング クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の メンバ クラス vs グルーピング  と OSKB020011 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### 汎用プロファイル指定 {#c26-i0327}
*分類: RDEFINE 基本*  ・  難易度: 上級

汎用プロファイル指定は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **汎用プロファイル指定**

    - 検証目的: 条件確認の汎用プロファイル指定について、汎用プロファイル指定は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020009の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件確認の汎用プロファイル指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄に汎用プロファイル指定を指定し、OSKB020009の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND 汎用プロファイル指定
    CASE OSKB020009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM 汎用プロファイル指定
    CASE OSKB020009
    SOURCE RACF
    ```

    汎用プロファイル指定とOSKB020009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020009を同じ出力で読み、条件確認の汎用プロファイル指定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020009
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020009 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I 汎用プロファイル指定 INFORMATION LISTED
    ```

    IRRD105IとOSKB020009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の 汎用プロファイル指定 と OSKB020009 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDELETE

### RDELETE GENERIC {#c26-i0328}
*分類: RDELETE*  ・  難易度: 上級

RDELETE GENERICは、汎用プロファイルを明示削除。「RDELETE GENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 呼出照合のセキュリティ設定でセキュリティ設定の運用確認を行います。RDELETE GENERIC の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で呼出照合のセキュリティ設定を確認した扱いにする。
    - B. IRRD105I の有無を確認せず呼出照合のセキュリティ設定を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出照合の根拠にする。 ✅
    - D. RDELETE GENERIC の属性行を読まず呼出照合のセキュリティ設定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合のセキュリティ設定において選択記号 C を採用し、識別名は呼出照合です。呼出照合のセキュリティ設定において RDELETE GENERIC は説明欄の「RACF で RDELETE GENERIC の扱いを記録する呼出照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のセキュリティ設定を受け取る担当者は、RDELETE GENERIC の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のセキュリティ設定は別カテゴリの確認を流用しており、RDELETE GENERIC の根拠にならないため呼出照合ではありません。 B: 呼出照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のセキュリティ設定が示す RDELETE GENERIC は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RDELETE GENERIC**

    - 検証目的: 値域整理のセキュリティ設定について、RDELETE GENERIC は、汎用プロファイルを明示削除。「RDELETE GENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域整理のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE GENERICを指定し、OSKB020116の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDELETE GENERIC
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDELETE GENERIC
    CASE OSKB020116
    SOURCE RACF
    ```

    RDELETE GENERICとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020116を同じ出力で読み、値域整理のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020116 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDELETE GENERIC INFORMATION LISTED
    ```

    IRRD105IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDELETE GENERIC と OSKB020116 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDELETE の権限 {#c26-i0329}
*分類: RDELETE*  ・  難易度: 上級

RDELETE の権限は、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 置換照合のの権限に関する RDELETE の権限の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず置換照合のの権限の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のの権限の証跡として保存して根拠にする。
    - C. RDELETE の権限の変更点を出力本文から切り離して置換照合のの権限の承認欄のみ残す。
    - D. 同じ画面で対象行と IRRD105I を読み、置換照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合のの権限において選択記号 D を採用し、識別名は置換照合です。置換照合のの権限において RDELETE の権限 は説明欄の「RDELETE の権限の状態と出力メッセージを結び付ける置換照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のの権限に関する記録は、RDELETE の権限の出力行と IRRD105I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のの権限は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため置換照合ではありません。 B: 置換照合のの権限は別カテゴリの確認を流用しており、RDELETE の権限の根拠にならないため置換照合ではありません。 C: 置換照合のの権限は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のの権限は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のの権限で記録する RDELETE の権限は RACF の確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RDELETE の権限**

    - 検証目的: 警告整理のの権限について、RDELETE の権限は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告整理のの権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE の権限を指定し、OSKB020117の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDELETE の権限
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDELETE の権限
    CASE OSKB020117
    SOURCE RACF
    ```

    RDELETE の権限とOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020117を同じ出力で読み、警告整理のの権限の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020117 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDELETE の権限 INFORMATION LISTED
    ```

    IRRD105IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDELETE の権限 と OSKB020117 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDELETE の目的 {#c26-i0330}
*分類: RDELETE*  ・  難易度: 上級

RDELETE の目的は、一般リソース プロファイルを削除。「RDELETE の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 変更確認のの目的に関する RDELETE の目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず変更確認のの目的の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のの目的の証跡として保存して根拠にする。
    - C. RDELETE の目的の変更点を出力本文から切り離して変更確認のの目的の承認欄のみ残す。
    - D. IRRD105I を含む表示を保存し、説明欄との差分を変更確認で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認のの目的において選択記号 D を採用し、識別名は変更確認です。変更確認のの目的において RDELETE の目的 は説明欄の「RDELETE の目的の状態と出力メッセージを結び付ける変更確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のの目的に関する記録は、RDELETE の目的の出力行と IRRD105I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のの目的は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため変更確認ではありません。 B: 変更確認のの目的は別カテゴリの確認を流用しており、RDELETE の目的の根拠にならないため変更確認ではありません。 C: 変更確認のの目的は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のの目的は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のの目的で記録する RDELETE の目的は RACF の確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RDELETE の目的**

    - 検証目的: 記録整理のの目的について、RDELETE の目的は、一般リソース プロファイルを削除。「RDELETE の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録整理のの目的の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE の目的を指定し、OSKB020113の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDELETE の目的
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDELETE の目的
    CASE OSKB020113
    SOURCE RACF
    ```

    RDELETE の目的とOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020113を同じ出力で読み、記録整理のの目的の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020113 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDELETE の目的 INFORMATION LISTED
    ```

    IRRD105IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDELETE の目的 と OSKB020113 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDELETE 後の REFRESH {#c26-i0331}
*分類: RDELETE*  ・  難易度: 上級

RDELETE 後の REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 終端照合の後のに関係する RDELETE 後の REFRESH の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、終端照合の採否を説明欄に結び付ける。 ✅
    - B. RDELETE 後の REFRESH の名称と担当者名のみを残して終端照合の後のの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で終端照合の後のを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず終端照合の後のの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合の後のにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の後のにおいて RDELETE 後の REFRESH は説明欄の「RDELETE 後の REFRESH の用途をセキュリティ設定の表示で確認する終端照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の後のに関連して、RACF では RDELETE 後の REFRESH の表示属性と IRRD105I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の後のは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の後のは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の後のは別カテゴリの確認を流用しており、RDELETE 後の REFRESH の根拠にならないため終端照合ではありません。 D: 終端照合の後のは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため終端照合ではありません。終端照合の後ので使う RDELETE 後の REFRESH という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RDELETE 後の REFRESH**

    - 検証目的: 復旧整理の後のについて、RDELETE 後の REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧整理の後のの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE 後の REFRESHを指定し、OSKB020118の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDELETE 後の REFRESH
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDELETE 後の REFRESH
    CASE OSKB020118
    SOURCE RACF
    ```

    RDELETE 後の REFRESHとOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020118を同じ出力で読み、復旧整理の後のの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020118 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDELETE 後の REFRESH INFORMATION LISTED
    ```

    IRRD105IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDELETE 後の REFRESH と OSKB020118 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDELETE 構文 {#c26-i0332}
*分類: RDELETE*  ・  難易度: 上級

RDELETE 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開照合の構文で RDELETE 構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RDELETE 構文の出力を取らず展開照合の構文の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開照合の確認記録にまとめる。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して展開照合の構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合の構文において選択記号 B を採用し、識別名は展開照合です。展開照合の構文において RDELETE 構文 は説明欄の「展開照合の構文に関係する定義値と表示行を照合する展開照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の構文の証跡を読む担当者は、RDELETE 構文の属性行と IRRD105I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の構文は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の構文は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の構文は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開照合ではありません。 D: 展開照合の構文は別カテゴリの確認を流用しており、RDELETE 構文の根拠にならないため展開照合ではありません。展開照合の構文に出る RDELETE 構文は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RDELETE 構文**

    - 検証目的: 順序整理の構文について、RDELETE 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序整理の構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE 構文を指定し、OSKB020115の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDELETE 構文
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDELETE 構文
    CASE OSKB020115
    SOURCE RACF
    ```

    RDELETE 構文とOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020115を同じ出力で読み、順序整理の構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020115 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDELETE 構文 INFORMATION LISTED
    ```

    IRRD105IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDELETE 構文 と OSKB020115 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RDELETE 短縮形 RDEL {#c26-i0333}
*分類: RDELETE*  ・  難易度: 上級

RDELETE 短縮形 RDELは、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文照合の短縮形に関係する RDELETE 短縮形 RDEL の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、構文照合の証跡として残す。 ✅
    - B. RDELETE 短縮形 RDEL の名称と担当者名のみを残して構文照合の短縮形の表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で構文照合の短縮形を確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず構文照合の短縮形の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合の短縮形において選択記号 A を採用し、識別名は構文照合です。構文照合の短縮形において RDELETE 短縮形 RDEL は説明欄の「RDELETE 短縮形 RDEL の用途をセキュリティ設定の表示で確認する構文照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の短縮形に関連して、RACF では RDELETE 短縮形 RDEL の表示属性と IRRD105I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の短縮形は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の短縮形は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の短縮形は別カテゴリの確認を流用しており、RDELETE 短縮形 RDEL の根拠にならないため構文照合ではありません。 D: 構文照合の短縮形は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文照合ではありません。構文照合の短縮形で使う RDELETE 短縮形 RDEL という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RDELETE 短縮形 RDEL**

    - 検証目的: 比較整理の短縮形について、RDELETE 短縮形 RDEL は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較整理の短縮形の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE 短縮形 RDELを指定し、OSKB020114の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RDELETE 短縮形 RDEL
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RDELETE 短縮形 RDEL
    CASE OSKB020114
    SOURCE RACF
    ```

    RDELETE 短縮形 RDELとOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020114を同じ出力で読み、比較整理の短縮形の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020114 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RDELETE 短縮形 RDEL INFORMATION LISTED
    ```

    IRRD105IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RDELETE 短縮形 RDEL と OSKB020114 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > REFRESH

### GENERIC(クラス名) REFRESH {#c26-i0334}
*分類: REFRESH*  ・  難易度: 上級

GENERIC(クラス名) REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのREFRESHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 条件確認のクラス名に関係する GENERIC 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 ✅
    - B. GENERIC 属性の名称と担当者名のみを残して条件確認のクラス名の表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で条件確認のクラス名を確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず条件確認のクラス名の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認のクラス名において選択記号 A を採用し、識別名は条件確認です。条件確認のクラス名において GENERIC 属性 は説明欄の「GENERIC 属性の用途をセキュリティ設定の表示で確認する条件確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のクラス名に関連して、RACF では GENERIC 属性の表示属性と IRRD105I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のクラス名は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のクラス名は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のクラス名は別カテゴリの確認を流用しており、GENERIC 属性の根拠にならないため条件確認ではありません。 D: 条件確認のクラス名は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件確認ではありません。条件確認のクラス名で使う GENERIC 属性という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **GENERIC(クラス名) REFRESH**

    - 検証目的: 展開照合のクラス名について、GENERIC(クラス名) REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の REFRESH で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開照合のクラス名の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にGENERIC(クラス名) REFRを指定し、OSKB010022の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND GENERIC(クラス名) REFR
    CASE OSKB010022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM GENERIC(クラス名) REFR
    CASE OSKB010022
    SOURCE RACF
    ```

    GENERIC(クラス名) REFRとOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010022を同じ出力で読み、展開照合のクラス名の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010022
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010022 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I GENERIC(クラス名) REFRESH INFORMATION LISTED
    ```

    IRRD105IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の GENERIC(クラス名) REFR と OSKB010022 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### GLOBAL(クラス名) REFRESH {#c26-i0335}
*分類: REFRESH*  ・  難易度: 上級

GLOBAL(クラス名) REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのREFRESHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 優先確認のクラス名に関する GLOBAL 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先確認のクラス名の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のクラス名の証跡として保存して根拠にする。
    - C. GLOBAL 属性の変更点を出力本文から切り離して優先確認のクラス名の承認欄のみ残す。
    - D. IRRD105I を含む表示を保存し、説明欄との差分を優先確認で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認のクラス名において選択記号 D を採用し、識別名は優先確認です。優先確認のクラス名において GLOBAL 属性 は説明欄の「GLOBAL 属性の状態と出力メッセージを結び付ける優先確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認のクラス名に関する記録は、GLOBAL 属性の出力行と IRRD105I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認のクラス名は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先確認ではありません。 B: 優先確認のクラス名は別カテゴリの確認を流用しており、GLOBAL 属性の根拠にならないため優先確認ではありません。 C: 優先確認のクラス名は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認のクラス名は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認のクラス名で記録する GLOBAL 属性は RACF の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **GLOBAL(クラス名) REFRESH**

    - 検証目的: 終端照合のクラス名について、GLOBAL(クラス名) REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の REFRESH で認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010025の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端照合のクラス名の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にGLOBAL(クラス名) REFREを指定し、OSKB010025の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND GLOBAL(クラス名) REFRE
    CASE OSKB010025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM GLOBAL(クラス名) REFRE
    CASE OSKB010025
    SOURCE RACF
    ```

    GLOBAL(クラス名) REFREとOSKB010025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010025を同じ出力で読み、終端照合のクラス名の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010025
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010025 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I GLOBAL(クラス名) REFRESH INFORMATION LISTED
    ```

    IRRD105IとOSKB010025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の GLOBAL(クラス名) REFRE と OSKB010025 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RACLIST(クラス名) REFRESH {#c26-i0336}
*分類: REFRESH*  ・  難易度: 上級

RACLIST(クラス名) REFRESHは、RACLIST 済プロファイル変更後の再ロード。「RACLIST(クラス名) REFRESH」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### REFRESH の RRSF 伝播 {#c26-i0337}
*分類: REFRESH*  ・  難易度: 上級

REFRESH の RRSF 伝播は、RRSF 接続先ノードに自動伝播される。「REFRESH の RRSF 伝播」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 記録確認のの 伝播に関係する REFRESH の RRSF 伝播の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、記録確認の証跡として残す。 ✅
    - B. REFRESH の RRSF 伝播の名称と担当者名のみを残して記録確認のの 伝播の表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で記録確認のの 伝播を確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず記録確認のの 伝播の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認のの 伝播において選択記号 A を採用し、識別名は記録確認です。記録確認のの 伝播において REFRESH の RRSF 伝播 は説明欄の「REFRESH の RRSF 伝播の用途をセキュリティ設定の表示で確認する記録確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認のの 伝播に関連して、RACF では REFRESH の RRSF 伝播の表示属性と IRRD105I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認のの 伝播は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認のの 伝播は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認のの 伝播は別カテゴリの確認を流用しており、REFRESH の RRSF 伝播の根拠にならないため記録確認ではありません。 D: 記録確認のの 伝播は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録確認ではありません。記録確認のの 伝播で使う REFRESH の RRSF 伝播という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **REFRESH の RRSF 伝播**

    - 検証目的: 探索照合のの 伝播について、REFRESH の RRSF 伝播は、RRSF 接続先ノードに自動伝播される。「REFRESH の RRSF 伝播」を確認すると、SETROPTS、RDEFINE、RACDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010026の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索照合のの 伝播の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にREFRESH の RRSF 伝播を指定し、OSKB010026の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND REFRESH の RRSF 伝播
    CASE OSKB010026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM REFRESH の RRSF 伝播
    CASE OSKB010026
    SOURCE RACF
    ```

    REFRESH の RRSF 伝播とOSKB010026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010026を同じ出力で読み、探索照合のの 伝播の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010026
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010026 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I REFRESH の RRSF 伝播 INFORMATION LISTED
    ```

    IRRD105IとOSKB010026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の REFRESH の RRSF 伝播 と OSKB010026 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### WHEN(PROGRAM) REFRESH {#c26-i0338}
*分類: REFRESH*  ・  難易度: 上級

WHEN(PROGRAM) REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのREFRESHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 範囲確認のセキュリティ設定でセキュリティ設定の運用確認を行います。WHEN 属性の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で範囲確認のセキュリティ設定を確認した扱いにする。
    - B. IRRD105I の有無を確認せず範囲確認のセキュリティ設定を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 ✅
    - D. WHEN 属性の属性行を読まず範囲確認のセキュリティ設定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認のセキュリティ設定において選択記号 C を採用し、識別名は範囲確認です。範囲確認のセキュリティ設定において WHEN 属性 は説明欄の「RACF で WHEN 属性の扱いを記録する範囲確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認のセキュリティ設定を受け取る担当者は、WHEN 属性の表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認のセキュリティ設定は別カテゴリの確認を流用しており、WHEN 属性の根拠にならないため範囲確認ではありません。 B: 範囲確認のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認のセキュリティ設定が示す WHEN 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **WHEN(PROGRAM) REFRESH**

    - 検証目的: 置換照合のセキュリティ設定について、WHEN(PROGRAM) REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の REFRESH で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010024の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換照合のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(PROGRAM) REFRを指定し、OSKB010024の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WHEN(PROGRAM) REFR
    CASE OSKB010024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WHEN(PROGRAM) REFR
    CASE OSKB010024
    SOURCE RACF
    ```

    WHEN(PROGRAM) REFRとOSKB010024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010024を同じ出力で読み、置換照合のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010024
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010024 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I WHEN(PROGRAM) REFRESH INFORMATION LISTED
    ```

    IRRD105IとOSKB010024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の WHEN(PROGRAM) REFR と OSKB010024 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RLIST

### RLIST * (ワイルドカード) {#c26-i0339}
*分類: RLIST*  ・  難易度: 上級

RLIST * (ワイルドカード)は、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 値域照合の* ワイルドカードに関する RLIST * (ワイルドカード)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず値域照合の* ワイルドカードの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の* ワイルドカードの証跡として保存して根拠にする。
    - C. RLIST * (ワイルドカード)の変更点を出力本文から切り離して値域照合の* ワイルドカードの承認欄のみ残す。
    - D. 同じ画面で対象行と IRRD105I を読み、値域照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合の* ワイルドカードにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の* ワイルドカードにおいて RLIST * (ワイルドカード) は説明欄の「RLIST * (ワイルドカード)の状態と出力メッセージを結び付ける値域照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の* ワイルドカードに関する記録は、RLIST * (ワイルドカード)の出力行と IRRD105I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の* ワイルドカードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため値域照合ではありません。 B: 値域照合の* ワイルドカードは別カテゴリの確認を流用しており、RLIST * (ワイルドカード)の根拠にならないため値域照合ではありません。 C: 値域照合の* ワイルドカードは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の* ワイルドカードは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の* ワイルドカードで記録する RLIST * (ワイルドカード)は RACF の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST * (ワイルドカード)**

    - 検証目的: 条件確認の* ワイルドカードについて、RLIST * (ワイルドカード)は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030009の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件確認の* ワイルドカードの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST * (ワイルドカード)を指定し、OSKB030009の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST * (ワイルドカード)
    CASE OSKB030009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST * (ワイルドカード)
    CASE OSKB030009
    SOURCE RACF
    ```

    RLIST * (ワイルドカード)とOSKB030009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030009を同じ出力で読み、条件確認の* ワイルドカードの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030009
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030009 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST * (ワイルドカード) INFORMATION LISTED
    ```

    IRRD105IとOSKB030009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST * (ワイルドカード) と OSKB030009 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST ALL {#c26-i0340}
*分類: RLIST*  ・  難易度: 上級

RLIST ALLは、全属性・全セグメント・統計を出力。「RLIST ALL」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 条件照合のセキュリティ設定に関係する RLIST ALL の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件照合で再確認できる形にする。 ✅
    - B. RLIST ALL の名称と担当者名のみを残して条件照合のセキュリティ設定の表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で条件照合のセキュリティ設定を確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず条件照合のセキュリティ設定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合のセキュリティ設定において選択記号 A を採用し、識別名は条件照合です。条件照合のセキュリティ設定において RLIST ALL は説明欄の「RLIST ALL の用途をセキュリティ設定の表示で確認する条件照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のセキュリティ設定に関連して、RACF では RLIST ALL の表示属性と IRRD105I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST ALL の根拠にならないため条件照合ではありません。 D: 条件照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件照合ではありません。条件照合のセキュリティ設定で使う RLIST ALL という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST ALL**

    - 検証目的: 展開確認のセキュリティ設定について、RLIST ALL は、全属性・全セグメント・統計を出力。「RLIST ALL」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030002の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST ALLを指定し、OSKB030002の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST ALL
    CASE OSKB030002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST ALL
    CASE OSKB030002
    SOURCE RACF
    ```

    RLIST ALLとOSKB030002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030002を同じ出力で読み、展開確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030002
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030002 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST ALL INFORMATION LISTED
    ```

    IRRD105IとOSKB030002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST ALL と OSKB030002 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST AUTHUSER {#c26-i0341}
*分類: RLIST*  ・  難易度: 上級

RLIST AUTHUSERは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 記録照合のセキュリティ設定に関係する RLIST AUTHUSER の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、記録照合の証跡として残す。 ✅
    - B. RLIST AUTHUSER の名称と担当者名のみを残して記録照合のセキュリティ設定の表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で記録照合のセキュリティ設定を確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず記録照合のセキュリティ設定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合のセキュリティ設定において選択記号 A を採用し、識別名は記録照合です。記録照合のセキュリティ設定において RLIST AUTHUSER は説明欄の「RLIST AUTHUSER の用途をセキュリティ設定の表示で確認する記録照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のセキュリティ設定に関連して、RACF では RLIST AUTHUSER の表示属性と IRRD105I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST AUTHUSER の根拠にならないため記録照合ではありません。 D: 記録照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録照合ではありません。記録照合のセキュリティ設定で使う RLIST AUTHUSER という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST AUTHUSER**

    - 検証目的: 探索確認のセキュリティ設定について、RLIST AUTHUSER は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030006の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST AUTHUSERを指定し、OSKB030006の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST AUTHUSER
    CASE OSKB030006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST AUTHUSER
    CASE OSKB030006
    SOURCE RACF
    ```

    RLIST AUTHUSERとOSKB030006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030006を同じ出力で読み、探索確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030006
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030006 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST AUTHUSER INFORMATION LISTED
    ```

    IRRD105IとOSKB030006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST AUTHUSER と OSKB030006 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST GENERIC {#c26-i0342}
*分類: RLIST*  ・  難易度: 上級

RLIST GENERICは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 比較照合のセキュリティ設定で RLIST GENERIC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RLIST GENERIC の出力を取らず比較照合のセキュリティ設定の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較照合の確認記録にまとめる。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して比較照合のセキュリティ設定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のセキュリティ設定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合のセキュリティ設定において選択記号 B を採用し、識別名は比較照合です。比較照合のセキュリティ設定において RLIST GENERIC は説明欄の「比較照合のセキュリティ設定に関係する定義値と表示行を照合する比較照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のセキュリティ設定の証跡を読む担当者は、RLIST GENERIC の属性行と IRRD105I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため比較照合ではありません。 D: 比較照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST GENERIC の根拠にならないため比較照合ではありません。比較照合のセキュリティ設定に出る RLIST GENERIC は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST GENERIC**

    - 検証目的: 上書確認のセキュリティ設定について、RLIST GENERIC は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030007の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST GENERICを指定し、OSKB030007の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST GENERIC
    CASE OSKB030007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST GENERIC
    CASE OSKB030007
    SOURCE RACF
    ```

    RLIST GENERICとOSKB030007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030007を同じ出力で読み、上書確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030007
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030007 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST GENERIC INFORMATION LISTED
    ```

    IRRD105IとOSKB030007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST GENERIC と OSKB030007 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST HISTORY {#c26-i0343}
*分類: RLIST*  ・  難易度: 上級

RLIST HISTORYは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 区切照合のセキュリティ設定で RLIST HISTORY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RLIST HISTORY の出力を取らず区切照合のセキュリティ設定の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切照合の確認値として扱う。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して区切照合のセキュリティ設定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のセキュリティ設定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合のセキュリティ設定において選択記号 B を採用し、識別名は区切照合です。区切照合のセキュリティ設定において RLIST HISTORY は説明欄の「区切照合のセキュリティ設定に関係する定義値と表示行を照合する区切照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のセキュリティ設定の証跡を読む担当者は、RLIST HISTORY の属性行と IRRD105I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため区切照合ではありません。 D: 区切照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST HISTORY の根拠にならないため区切照合ではありません。区切照合のセキュリティ設定に出る RLIST HISTORY は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST HISTORY**

    - 検証目的: 呼出確認のセキュリティ設定について、RLIST HISTORY は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST HISTORYを指定し、OSKB030003の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST HISTORY
    CASE OSKB030003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST HISTORY
    CASE OSKB030003
    SOURCE RACF
    ```

    RLIST HISTORYとOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030003を同じ出力で読み、呼出確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030003
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030003 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST HISTORY INFORMATION LISTED
    ```

    IRRD105IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST HISTORY と OSKB030003 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST NORACF {#c26-i0344}
*分類: RLIST*  ・  難易度: 上級

RLIST NORACFは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 出力照合のセキュリティ設定に関する RLIST NORACF の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力照合のセキュリティ設定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のセキュリティ設定の証跡として保存して根拠にする。
    - C. RLIST NORACF の変更点を出力本文から切り離して出力照合のセキュリティ設定の承認欄のみ残す。
    - D. RACF の表示形式に沿って根拠行を採り、出力照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合のセキュリティ設定において選択記号 D を採用し、識別名は出力照合です。出力照合のセキュリティ設定において RLIST NORACF は説明欄の「RLIST NORACF の状態と出力メッセージを結び付ける出力照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のセキュリティ設定に関する記録は、RLIST NORACF の出力行と IRRD105I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力照合ではありません。 B: 出力照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST NORACF の根拠にならないため出力照合ではありません。 C: 出力照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のセキュリティ設定で記録する RLIST NORACF は RACF の確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST NORACF**

    - 検証目的: 構文確認のセキュリティ設定について、RLIST NORACF は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030001の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST NORACFを指定し、OSKB030001の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST NORACF
    CASE OSKB030001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST NORACF
    CASE OSKB030001
    SOURCE RACF
    ```

    RLIST NORACFとOSKB030001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030001を同じ出力で読み、構文確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030001
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030001 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST NORACF INFORMATION LISTED
    ```

    IRRD105IとOSKB030001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST NORACF と OSKB030001 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST RESGROUP {#c26-i0345}
*分類: RLIST*  ・  難易度: 上級

RLIST RESGROUPは、メンバが属する GROUP プロファイルを表示。「RLIST RESGROUP」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 優先照合のセキュリティ設定に関する RLIST RESGROUP の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先照合のセキュリティ設定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のセキュリティ設定の証跡として保存して根拠にする。
    - C. RLIST RESGROUP の変更点を出力本文から切り離して優先照合のセキュリティ設定の承認欄のみ残す。
    - D. IRRD105I を含む表示を保存し、説明欄との差分を優先照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合のセキュリティ設定において選択記号 D を採用し、識別名は優先照合です。優先照合のセキュリティ設定において RLIST RESGROUP は説明欄の「RLIST RESGROUP の状態と出力メッセージを結び付ける優先照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のセキュリティ設定に関する記録は、RLIST RESGROUP の出力行と IRRD105I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先照合ではありません。 B: 優先照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST RESGROUP の根拠にならないため優先照合ではありません。 C: 優先照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のセキュリティ設定で記録する RLIST RESGROUP は RACF の確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST RESGROUP**

    - 検証目的: 終端確認のセキュリティ設定について、RLIST RESGROUP は、メンバが属する GROUP プロファイルを表示。「RLIST RESGROUP」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030005の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST RESGROUPを指定し、OSKB030005の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST RESGROUP
    CASE OSKB030005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST RESGROUP
    CASE OSKB030005
    SOURCE RACF
    ```

    RLIST RESGROUPとOSKB030005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030005を同じ出力で読み、終端確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030005
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030005 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST RESGROUP INFORMATION LISTED
    ```

    IRRD105IとOSKB030005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST RESGROUP と OSKB030005 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST STATISTICS {#c26-i0346}
*分類: RLIST*  ・  難易度: 上級

RLIST STATISTICSは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 範囲照合のセキュリティ設定でセキュリティ設定の運用確認を行います。RLIST STATISTICS の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で範囲照合のセキュリティ設定を確認した扱いにする。
    - B. IRRD105I の有無を確認せず範囲照合のセキュリティ設定を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲照合の根拠を固定する。 ✅
    - D. RLIST STATISTICS の属性行を読まず範囲照合のセキュリティ設定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合のセキュリティ設定において選択記号 C を採用し、識別名は範囲照合です。範囲照合のセキュリティ設定において RLIST STATISTICS は説明欄の「RACF で RLIST STATISTICS の扱いを記録する範囲照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のセキュリティ設定を受け取る担当者は、RLIST STATISTICS の表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST STATISTICS の根拠にならないため範囲照合ではありません。 B: 範囲照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のセキュリティ設定が示す RLIST STATISTICS は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST STATISTICS**

    - 検証目的: 置換確認のセキュリティ設定について、RLIST STATISTICS は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換確認のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST STATISTICSを指定し、OSKB030004の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST STATISTICS
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST STATISTICS
    CASE OSKB030004
    SOURCE RACF
    ```

    RLIST STATISTICSとOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030004を同じ出力で読み、置換確認のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030004 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST STATISTICS INFORMATION LISTED
    ```

    IRRD105IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST STATISTICS と OSKB030004 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST STDATA/TME/SSIGNON 等セグメント {#c26-i0347}
*分類: RLIST*  ・  難易度: 上級

RLIST STDATA/TME/SSIGNON 等セグメントは、クラス特有のセグメントを表示。「RLIST STDATA/TME/SSIGNON 等セグメント」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 属性照合通知の属性照合として RLIST を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 承認欄の記入を優先して出力メッセージを保存しない。
    - B. 名称と担当者名を保存して表示本文を確認しない。
    - C. 属性照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 別分類の結果を流用して同じ証跡として扱う。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。属性照合通知で扱う RLIST は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（属性照合通知用語）。属性照合通知の担当者は属性照合として、表示本文とメッセージを照合します（属性照合通知照合）。属性照合通知の対応を残すと、後続担当者は同じ出典に戻って確認できます（属性照合通知出典）。A: 属性照合通知で表示とメッセージを結ぶ場合に根拠になります（属性照合通知A）。B: 属性照合通知で定義と出力の関係がない場合は追跡できません（属性照合通知B）。C: 属性照合通知で出典名のみでは実際の表示を説明できません（属性照合通知C）。D: 属性照合通知で操作記録のみでは値や状態の確認が不足します（属性照合通知D）。属性照合通知の初出用語として RLIST を扱い、分類内の確認名として保存します（属性照合通知終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST STDATA ・ TME ・ SSIGNON 等セグメント**

    - 検証目的: 出力確認の・ ・について、RLIST STDATA/TME/SSIGNON 等セグメントは、クラス特有のセグメントを表示。「RLIST STDATA/TME/SSIGNON 等セグメント」を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030008の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力確認の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST STDATA ・ TMEを指定し、OSKB030008の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST STDATA ・ TME
    CASE OSKB030008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST STDATA ・ TME
    CASE OSKB030008
    SOURCE RACF
    ```

    RLIST STDATA ・ TMEとOSKB030008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030008を同じ出力で読み、出力確認の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030008
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030008 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST STDATA ・ TME ・ SSIGNON INFORMATION LISTED
    ```

    IRRD105IとOSKB030008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST STDATA ・ TME と OSKB030008 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST と AUDITOR {#c26-i0348}
*分類: RLIST*  ・  難易度: 上級

RLIST と AUDITORは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 警告照合のとに関係する RLIST と AUDITOR の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、警告照合の採否を説明欄に結び付ける。 ✅
    - B. RLIST と AUDITOR の名称と担当者名のみを残して警告照合のとの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で警告照合のとを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず警告照合のとの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合のとにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のとにおいて RLIST と AUDITOR は説明欄の「RLIST と AUDITOR の用途をセキュリティ設定の表示で確認する警告照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のとに関連して、RACF では RLIST と AUDITOR の表示属性と IRRD105I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のとは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のとは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のとは別カテゴリの確認を流用しており、RLIST と AUDITOR の根拠にならないため警告照合ではありません。 D: 警告照合のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため警告照合ではありません。警告照合のとで使う RLIST と AUDITOR という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は警告照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST と AUDITOR**

    - 検証目的: 区切確認のとについて、RLIST と AUDITOR は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切確認のとの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST と AUDITORを指定し、OSKB030010の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST と AUDITOR
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST と AUDITOR
    CASE OSKB030010
    SOURCE RACF
    ```

    RLIST と AUDITORとOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030010を同じ出力で読み、区切確認のとの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030010 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST と AUDITOR INFORMATION LISTED
    ```

    IRRD105IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST と AUDITOR と OSKB030010 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST の目的 {#c26-i0349}
*分類: RLIST*  ・  難易度: 上級

RLIST の目的は、一般リソース プロファイルの属性表示。「RLIST の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 探索照合のの目的で RLIST の目的の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RLIST の目的の出力を取らず探索照合のの目的の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索照合として引き継ぐ。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して探索照合のの目的の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のの目的へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合のの目的において選択記号 B を採用し、識別名は探索照合です。探索照合のの目的において RLIST の目的 は説明欄の「探索照合のの目的に関係する定義値と表示行を照合する探索照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のの目的の証跡を読む担当者は、RLIST の目的の属性行と IRRD105I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のの目的は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のの目的は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のの目的は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため探索照合ではありません。 D: 探索照合のの目的は別カテゴリの確認を流用しており、RLIST の目的の根拠にならないため探索照合ではありません。探索照合のの目的に出る RLIST の目的は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST の目的**

    - 検証目的: 監査整理のの目的について、RLIST の目的は、一般リソース プロファイルの属性表示。「RLIST の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査整理のの目的の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST の目的を指定し、OSKB020119の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST の目的
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST の目的
    CASE OSKB020119
    SOURCE RACF
    ```

    RLIST の目的とOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020119を同じ出力で読み、監査整理のの目的の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020119 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST の目的 INFORMATION LISTED
    ```

    IRRD105IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST の目的 と OSKB020119 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RLIST 構文 {#c26-i0350}
*分類: RLIST*  ・  難易度: 上級

RLIST 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 上書照合の構文でセキュリティ設定の運用確認を行います。RLIST 構文の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で上書照合の構文を確認した扱いにする。
    - B. IRRD105I の有無を確認せず上書照合の構文を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書照合の確認にする。 ✅
    - D. RLIST 構文の属性行を読まず上書照合の構文の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合の構文において選択記号 C を採用し、識別名は上書照合です。上書照合の構文において RLIST 構文 は説明欄の「RACF で RLIST 構文の扱いを記録する上書照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の構文を受け取る担当者は、RLIST 構文の表示結果と IRRD105I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の構文は別カテゴリの確認を流用しており、RLIST 構文の根拠にならないため上書照合ではありません。 B: 上書照合の構文は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため上書照合ではありません。 C: 上書照合の構文は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の構文は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の構文が示す RLIST 構文は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RLIST 構文**

    - 検証目的: 変更整理の構文について、RLIST 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更整理の構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRLIST 構文を指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RLIST 構文
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RLIST 構文
    CASE OSKB020120
    SOURCE RACF
    ```

    RLIST 構文とOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020120を同じ出力で読み、変更整理の構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020120 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RLIST 構文 INFORMATION LISTED
    ```

    IRRD105IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RLIST 構文 と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > SECLABEL

### COMPATMODE {#c26-i0351}
*分類: SECLABEL*  ・  難易度: 上級

COMPATMODEは、古い MLS 互換モード (CC EAL 評価用)。「COMPATMODE」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **COMPATMODE**

    - 検証目的: 呼出判定のセキュリティ設定について、COMPATMODE は、古い MLS 互換モード (CC EAL 評価用)。「COMPATMODE」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出判定のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にCOMPATMODEを指定し、OSKB010083の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND COMPATMODE
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM COMPATMODE
    CASE OSKB010083
    SOURCE RACF
    ```

    COMPATMODEとOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010083を同じ出力で読み、呼出判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010083 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I COMPATMODE INFORMATION LISTED
    ```

    IRRD105IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の COMPATMODE と OSKB010083 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### NOCOMPATMODE {#c26-i0352}
*分類: SECLABEL*  ・  難易度: 上級

NOCOMPATMODEは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **NOCOMPATMODE**

    - 検証目的: 置換判定のセキュリティ設定について、NOCOMPATMODE は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換判定のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNOCOMPATMODEを指定し、OSKB010084の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NOCOMPATMODE
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NOCOMPATMODE
    CASE OSKB010084
    SOURCE RACF
    ```

    NOCOMPATMODEとOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010084を同じ出力で読み、置換判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010084 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I NOCOMPATMODE INFORMATION LISTED
    ```

    IRRD105IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の NOCOMPATMODE と OSKB010084 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### NOSECLABELCONTROL {#c26-i0353}
*分類: SECLABEL*  ・  難易度: 上級

NOSECLABELCONTROLは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **NOSECLABELCONTROL**

    - 検証目的: 展開判定のセキュリティ設定について、NOSECLABELCONTROL は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開判定のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にNOSECLABELCONTROLを指定し、OSKB010082の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NOSECLABELCONTROL
    CASE OSKB010082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NOSECLABELCONTROL
    CASE OSKB010082
    SOURCE RACF
    ```

    NOSECLABELCONTROLとOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010082を同じ出力で読み、展開判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010082
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010082 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I NOSECLABELCONTROL INFORMATION LISTED
    ```

    IRRD105IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の NOSECLABELCONTROL と OSKB010082 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLABELAUDIT {#c26-i0354}
*分類: SECLABEL*  ・  難易度: 上級

SECLABELAUDITは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLABELAUDIT**

    - 検証目的: 終端判定のセキュリティ設定について、SECLABELAUDIT は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端判定のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLABELAUDITを指定し、OSKB010085の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLABELAUDIT
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLABELAUDIT
    CASE OSKB010085
    SOURCE RACF
    ```

    SECLABELAUDITとOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010085を同じ出力で読み、終端判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010085 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLABELAUDIT INFORMATION LISTED
    ```

    IRRD105IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLABELAUDIT と OSKB010085 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLABELCONTROL {#c26-i0355}
*分類: SECLABEL*  ・  難易度: 上級

SECLABELCONTROLは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLABELCONTROL**

    - 検証目的: 構文判定のセキュリティ設定について、SECLABELCONTROL は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文判定のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLABELCONTROLを指定し、OSKB010081の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLABELCONTROL
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLABELCONTROL
    CASE OSKB010081
    SOURCE RACF
    ```

    SECLABELCONTROLとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010081を同じ出力で読み、構文判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010081 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLABELCONTROL INFORMATION LISTED
    ```

    IRRD105IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLABELCONTROL と OSKB010081 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > SETROPTS 基本

### SETROPTS LIST {#c26-i0356}
*分類: SETROPTS 基本*  ・  難易度: 上級

現行 RACF オプション設定を全件表示。AUDITOR でも可。「SETROPTS LIST」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### SETROPTS と RACF データベース {#c26-i0357}
*分類: SETROPTS 基本*  ・  難易度: 上級

SETROPTS と RACF データベースは、DB が読み専用の場合 SETROPTS の更新系は失敗。「SETROPTS と RACF データベース」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SETROPTS と RACF データベース**

    - 検証目的: 展開確認のと データベースについて、SETROPTS と RACF データベースは、DB が読み専用の場合 SETROPTS の更新系は失敗。「SETROPTS と RACF データベース」を確認すると、SEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開確認のと データベースの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSETROPTS と RACF デーを指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SETROPTS と RACF デー
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SETROPTS と RACF デー
    CASE OSKB010002
    SOURCE RACF
    ```

    SETROPTS と RACF デーとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010002を同じ出力で読み、展開確認のと データベースの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010002 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SETROPTS と RACF データベース INFORMATION LISTED
    ```

    IRRD105IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SETROPTS と RACF デー と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SETROPTS の伝播 {#c26-i0358}
*分類: SETROPTS 基本*  ・  難易度: 上級

SETROPTS の伝播は、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SETROPTS の伝播**

    - 検証目的: 構文確認のの伝播について、SETROPTS の伝播は、RACF SETROPTS/RDEFINE/RACDCERT の SETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文確認のの伝播の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSETROPTS の伝播を指定し、OSKB010001の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SETROPTS の伝播
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SETROPTS の伝播
    CASE OSKB010001
    SOURCE RACF
    ```

    SETROPTS の伝播とOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010001を同じ出力で読み、構文確認のの伝播の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010001 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SETROPTS の伝播 INFORMATION LISTED
    ```

    IRRD105IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SETROPTS の伝播 と OSKB010001 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SETROPTS の永続性 {#c26-i0359}
*分類: SETROPTS 基本*  ・  難易度: 上級

SETROPTS の永続性は、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### SETROPTS の目的 {#c26-i0360}
*分類: SETROPTS 基本*  ・  難易度: 上級

SETROPTS の目的は、RACF システム全体のオプションを動的に変更するコマンド。「SETROPTS の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### SETROPTS 実行権限 {#c26-i0361}
*分類: SETROPTS 基本*  ・  難易度: 上級

SETROPTS 実行権限は、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### SETROPTS 短縮形 SETR {#c26-i0362}
*分類: SETROPTS 基本*  ・  難易度: 上級

SETROPTS 短縮形 SETRは、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)



## RACF SETROPTS/RDEFINE/RACDCERT > SMF 80

### IRRADU00 と DB2 LOAD {#c26-i0363}
*分類: SMF 80*  ・  難易度: 上級

IRRADU00 と DB2 LOADは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開追跡のとで IRRADU00 と DB2 LOAD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IRRADU00 と DB2 LOAD の出力を取らず展開追跡のとの説明文と承認印のみを残す。
    - B. IRRD105I を含む表示を保存し、説明欄との差分を展開追跡で確認する。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して展開追跡のとの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のとへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡のとにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のとにおいて IRRADU00 と DB2 LOAD は説明欄の「展開追跡のとに関係する定義値と表示行を照合する展開追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のとの証跡を読む担当者は、IRRADU00 と DB2 LOAD の属性行と IRRD105I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のとは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のとは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のとは別カテゴリの確認を流用しており、IRRADU00 と DB2 LOAD の根拠にならないため展開追跡ではありません。展開追跡のとに出る IRRADU00 と DB2 LOAD は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRADU00 と DB2 LOAD**

    - 検証目的: 順序整理のとについて、IRRADU00 と DB2 LOAD は、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030115の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序整理のとの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRADU00 と DB2 LOAを指定し、OSKB030115の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRADU00 と DB2 LOA
    CASE OSKB030115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRADU00 と DB2 LOA
    CASE OSKB030115
    SOURCE RACF
    ```

    IRRADU00 と DB2 LOAとOSKB030115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030115を同じ出力で読み、順序整理のとの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030115
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030115 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRADU00 と DB2 LOAD INFORMATION LISTED
    ```

    IRRD105IとOSKB030115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRADU00 と DB2 LOA と OSKB030115 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RACFRW (RACF Report Writer) {#c26-i0364}
*分類: SMF 80*  ・  難易度: 上級

RACFRW (RACF Report Writer)は、古い SMF 80 レポート ツール (非推奨)。「RACFRW (RACF Report Writer)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 呼出追跡のセキュリティ設定でセキュリティ設定の運用確認を行います。RACFRW 属性の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で呼出追跡のセキュリティ設定を確認した扱いにする。
    - B. IRRD105I の有無を確認せず呼出追跡のセキュリティ設定を正常終了として記録する。
    - C. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、呼出追跡の証跡として残す。 ✅
    - D. RACFRW 属性の属性行を読まず呼出追跡のセキュリティ設定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡のセキュリティ設定において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のセキュリティ設定において RACFRW 属性 は説明欄の「RACF で RACFRW 属性の扱いを記録する呼出追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のセキュリティ設定を受け取る担当者は、RACFRW 属性の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のセキュリティ設定は別カテゴリの確認を流用しており、RACFRW 属性の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のセキュリティ設定が示す RACFRW 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RACFRW (RACF Report Writer)**

    - 検証目的: 値域整理のセキュリティ設定について、RACFRW (RACF Report Writer)は、古い SMF 80 レポート ツール (非推奨)。「RACFRW (RACF Report Writer)」を確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030116の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域整理のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRACFRW (RACF Reporを指定し、OSKB030116の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RACFRW (RACF Repor
    CASE OSKB030116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RACFRW (RACF Repor
    CASE OSKB030116
    SOURCE RACF
    ```

    RACFRW (RACF ReporとOSKB030116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030116を同じ出力で読み、値域整理のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030116
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030116 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RACFRW (RACF Report Writ INFORMATION LISTED
    ```

    IRRD105IとOSKB030116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RACFRW (RACF Repor と OSKB030116 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 80 と IRRADU00 {#c26-i0365}
*分類: SMF 80*  ・  難易度: 上級

SMF 80 と IRRADU00は、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文追跡のとに関係する SMF 80 と IRRADU00 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文追跡の根拠を固定する。 ✅
    - B. SMF 80 と IRRADU00 の名称と担当者名のみを残して構文追跡のとの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で構文追跡のとを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず構文追跡のとの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡のとにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のとにおいて SMF 80 と IRRADU00 は説明欄の「SMF 80 と IRRADU00 の用途をセキュリティ設定の表示で確認する構文追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のとに関連して、RACF では SMF 80 と IRRADU00 の表示属性と IRRD105I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のとは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のとは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のとは別カテゴリの確認を流用しており、SMF 80 と IRRADU00 の根拠にならないため構文追跡ではありません。 D: 構文追跡のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文追跡ではありません。構文追跡のとで使う SMF 80 と IRRADU00 という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 80 と IRRADU00**

    - 検証目的: 比較整理のとについて、SMF 80 と IRRADU00 は、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030114の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較整理のとの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 と IRRADU00を指定し、OSKB030114の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 80 と IRRADU00
    CASE OSKB030114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 80 と IRRADU00
    CASE OSKB030114
    SOURCE RACF
    ```

    SMF 80 と IRRADU00とOSKB030114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030114を同じ出力で読み、比較整理のとの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030114
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030114 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 80 と IRRADU00 INFORMATION LISTED
    ```

    IRRD105IとOSKB030114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 80 と IRRADU00 と OSKB030114 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 80 と OMEGAMON/zSecure {#c26-i0366}
*分類: SMF 80*  ・  難易度: 上級

SMF 80 と OMEGAMON/zSecureは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 範囲照合入力の範囲照合として SMF を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 範囲照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 名称と担当者名を保存して表示本文を確認しない。
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解はAです。範囲照合入力で扱う SMF は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（範囲照合入力用語）。範囲照合入力の担当者は範囲照合として、表示本文とメッセージを照合します（範囲照合入力照合）。範囲照合入力の対応を残すと、後続担当者は同じ出典に戻って確認できます（範囲照合入力出典）。A: 範囲照合入力で表示とメッセージを結ぶ場合に根拠になります（範囲照合入力A）。B: 範囲照合入力で定義と出力の関係がない場合は追跡できません（範囲照合入力B）。C: 範囲照合入力で出典名のみでは実際の表示を説明できません（範囲照合入力C）。D: 範囲照合入力で操作記録のみでは値や状態の確認が不足します（範囲照合入力D）。範囲照合入力の初出用語として SMF を扱い、分類内の確認名として保存します（範囲照合入力終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 80 と OMEGAMON ・zSecure**

    - 検証目的: 復旧整理のと ・について、SMF 80 と OMEGAMON/zSecureは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030118の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧整理のと ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 と OMEGAMON を指定し、OSKB030118の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 80 と OMEGAMON 
    CASE OSKB030118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 80 と OMEGAMON 
    CASE OSKB030118
    SOURCE RACF
    ```

    SMF 80 と OMEGAMON とOSKB030118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030118を同じ出力で読み、復旧整理のと ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030118
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030118 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 80 と OMEGAMON ・zSecur INFORMATION LISTED
    ```

    IRRD105IとOSKB030118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 80 と OMEGAMON  と OSKB030118 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 80 イベント コード {#c26-i0367}
*分類: SMF 80*  ・  難易度: 上級

SMF 80 イベント コードは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 監査照合のイベント コードでセキュリティ設定の運用確認を行います。SMF 80 イベント コードの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で監査照合のイベント コードを確認した扱いにする。
    - B. IRRD105I の有無を確認せず監査照合のイベント コードを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査照合で再確認できる形にする。 ✅
    - D. SMF 80 イベント コードの属性行を読まず監査照合のイベント コードの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合のイベント コードにおいて選択記号 C を採用し、識別名は監査照合です。監査照合のイベント コードにおいて SMF 80 イベント コード は説明欄の「RACF で SMF 80 イベント コードの扱いを記録する監査照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のイベント コードを受け取る担当者は、SMF 80 イベント コードの表示結果と IRRD105I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のイベント コードは別カテゴリの確認を流用しており、SMF 80 イベント コードの根拠にならないため監査照合ではありません。 B: 監査照合のイベント コードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため監査照合ではありません。 C: 監査照合のイベント コードは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のイベント コードは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のイベント コードが示す SMF 80 イベント コードは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 80 イベント コード**

    - 検証目的: 優先整理のイベント コードについて、SMF 80 イベント コードは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030112の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先整理のイベント コードの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 イベント コードを指定し、OSKB030112の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 80 イベント コード
    CASE OSKB030112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 80 イベント コード
    CASE OSKB030112
    SOURCE RACF
    ```

    SMF 80 イベント コードとOSKB030112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030112を同じ出力で読み、優先整理のイベント コードの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030112
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030112 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 80 イベント コード INFORMATION LISTED
    ```

    IRRD105IとOSKB030112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 80 イベント コード と OSKB030112 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 80 サブタイプ {#c26-i0368}
*分類: SMF 80*  ・  難易度: 上級

SMF 80 サブタイプは、イベントの詳細分類。「SMF 80 サブタイプ」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 変更照合のサブタイプに関する SMF 80 サブタイプの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず変更照合のサブタイプの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のサブタイプの証跡として保存して根拠にする。
    - C. SMF 80 サブタイプの変更点を出力本文から切り離して変更照合のサブタイプの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合のサブタイプにおいて選択記号 D を採用し、識別名は変更照合です。変更照合のサブタイプにおいて SMF 80 サブタイプ は説明欄の「SMF 80 サブタイプの状態と出力メッセージを結び付ける変更照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のサブタイプに関する記録は、SMF 80 サブタイプの出力行と IRRD105I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のサブタイプは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため変更照合ではありません。 B: 変更照合のサブタイプは別カテゴリの確認を流用しており、SMF 80 サブタイプの根拠にならないため変更照合ではありません。 C: 変更照合のサブタイプは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のサブタイプは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のサブタイプで記録する SMF 80 サブタイプは RACF の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 80 サブタイプ**

    - 検証目的: 記録整理のサブタイプについて、SMF 80 サブタイプは、イベントの詳細分類。「SMF 80 サブタイプ」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030113の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録整理のサブタイプの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 サブタイプを指定し、OSKB030113の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 80 サブタイプ
    CASE OSKB030113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 80 サブタイプ
    CASE OSKB030113
    SOURCE RACF
    ```

    SMF 80 サブタイプとOSKB030113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030113を同じ出力で読み、記録整理のサブタイプの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030113
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030113 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 80 サブタイプ INFORMATION LISTED
    ```

    IRRD105IとOSKB030113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 80 サブタイプ と OSKB030113 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 80 フィールド {#c26-i0369}
*分類: SMF 80*  ・  難易度: 上級

SMF 80 フィールドは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 置換追跡のフィールドに関する SMF 80 フィールドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず置換追跡のフィールドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のフィールドの証跡として保存して根拠にする。
    - C. SMF 80 フィールドの変更点を出力本文から切り離して置換追跡のフィールドの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡のフィールドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のフィールドにおいて SMF 80 フィールド は説明欄の「SMF 80 フィールドの状態と出力メッセージを結び付ける置換追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のフィールドに関する記録は、SMF 80 フィールドの出力行と IRRD105I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のフィールドは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のフィールドは別カテゴリの確認を流用しており、SMF 80 フィールドの根拠にならないため置換追跡ではありません。 C: 置換追跡のフィールドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のフィールドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のフィールドで記録する SMF 80 フィールドは RACF の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 80 フィールド**

    - 検証目的: 警告整理のフィールドについて、SMF 80 フィールドは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030117の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告整理のフィールドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 フィールドを指定し、OSKB030117の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 80 フィールド
    CASE OSKB030117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 80 フィールド
    CASE OSKB030117
    SOURCE RACF
    ```

    SMF 80 フィールドとOSKB030117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030117を同じ出力で読み、警告整理のフィールドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030117
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030117 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 80 フィールド INFORMATION LISTED
    ```

    IRRD105IとOSKB030117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 80 フィールド と OSKB030117 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 80 生成制御 {#c26-i0370}
*分類: SMF 80*  ・  難易度: 上級

SMF 80 生成制御は、SETROPTS AUDIT/SAUDIT/OPERAUDIT/LOGOPTIONS 等で制御。「SMF 80 生成制御」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 探索追跡の生成制御で SMF 80 生成制御の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SMF 80 生成制御の出力を取らず探索追跡の生成制御の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IRRD105I を読み、探索追跡の結果として保存する。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して探索追跡の生成制御の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の生成制御へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡の生成制御において選択記号 B を採用し、識別名は探索追跡です。探索追跡の生成制御において SMF 80 生成制御 は説明欄の「探索追跡の生成制御に関係する定義値と表示行を照合する探索追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の生成制御の証跡を読む担当者は、SMF 80 生成制御の属性行と IRRD105I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の生成制御は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の生成制御は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の生成制御は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の生成制御は別カテゴリの確認を流用しており、SMF 80 生成制御の根拠にならないため探索追跡ではありません。探索追跡の生成制御に出る SMF 80 生成制御は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 80 生成制御**

    - 検証目的: 監査整理の生成制御について、SMF 80 生成制御は、SETROPTS AUDIT/SAUDIT/OPERAUDIT/LOGOPTIONS 等で制御。「SMF 80 生成制御」を確認すると、SETROに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030119の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査整理の生成制御の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 生成制御を指定し、OSKB030119の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 80 生成制御
    CASE OSKB030119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 80 生成制御
    CASE OSKB030119
    SOURCE RACF
    ```

    SMF 80 生成制御とOSKB030119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030119を同じ出力で読み、監査整理の生成制御の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030119
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030119 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 80 生成制御 INFORMATION LISTED
    ```

    IRRD105IとOSKB030119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 80 生成制御 と OSKB030119 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 81 レコード {#c26-i0371}
*分類: SMF 80*  ・  難易度: 上級

SMF 81 レコードは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 上書追跡のレコードでセキュリティ設定の運用確認を行います。SMF 81 レコードの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で上書追跡のレコードを確認した扱いにする。
    - B. IRRD105I の有無を確認せず上書追跡のレコードを正常終了として記録する。
    - C. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、上書追跡の採否を説明欄に結び付ける。 ✅
    - D. SMF 81 レコードの属性行を読まず上書追跡のレコードの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡のレコードにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のレコードにおいて SMF 81 レコード は説明欄の「RACF で SMF 81 レコードの扱いを記録する上書追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のレコードを受け取る担当者は、SMF 81 レコードの表示結果と IRRD105I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のレコードは別カテゴリの確認を流用しており、SMF 81 レコードの根拠にならないため上書追跡ではありません。 B: 上書追跡のレコードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のレコードは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のレコードは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のレコードが示す SMF 81 レコードは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 81 レコード**

    - 検証目的: 変更整理のレコードについて、SMF 81 レコードは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030120の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更整理のレコードの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 81 レコードを指定し、OSKB030120の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 81 レコード
    CASE OSKB030120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 81 レコード
    CASE OSKB030120
    SOURCE RACF
    ```

    SMF 81 レコードとOSKB030120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030120を同じ出力で読み、変更整理のレコードの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030120
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030120 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 81 レコード INFORMATION LISTED
    ```

    IRRD105IとOSKB030120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 81 レコード と OSKB030120 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF 83 レコード {#c26-i0372}
*分類: SMF 80*  ・  難易度: 上級

SMF 83 レコードは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 出力追跡のレコードに関する SMF 83 レコードの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力追跡のレコードの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のレコードの証跡として保存して根拠にする。
    - C. SMF 83 レコードの変更点を出力本文から切り離して出力追跡のレコードの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、出力追跡として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡のレコードにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡のレコードにおいて SMF 83 レコード は説明欄の「SMF 83 レコードの状態と出力メッセージを結び付ける出力追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のレコードに関する記録は、SMF 83 レコードの出力行と IRRD105I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のレコードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のレコードは別カテゴリの確認を流用しており、SMF 83 レコードの根拠にならないため出力追跡ではありません。 C: 出力追跡のレコードは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のレコードは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のレコードで記録する SMF 83 レコードは RACF の確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SMF 83 レコード**

    - 検証目的: 構文記録のレコードについて、SMF 83 レコードは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030121の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文記録のレコードの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF 83 レコードを指定し、OSKB030121の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF 83 レコード
    CASE OSKB030121
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF 83 レコード
    CASE OSKB030121
    SOURCE RACF
    ```

    SMF 83 レコードとOSKB030121が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030121を同じ出力で読み、構文記録のレコードの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030121
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030121 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF 83 レコード INFORMATION LISTED
    ```

    IRRD105IとOSKB030121が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF 83 レコード と OSKB030121 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SMF Type 80 とは {#c26-i0373}
*分類: SMF 80*  ・  難易度: 上級

SMF Type 80 とはは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SMF Type 80 とは**

    - 検証目的: 範囲整理のとはについて、SMF Type 80 とはは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030111の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲整理のとはの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSMF Type 80 とはを指定し、OSKB030111の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SMF Type 80 とは
    CASE OSKB030111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SMF Type 80 とは
    CASE OSKB030111
    SOURCE RACF
    ```

    SMF Type 80 とはとOSKB030111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030111を同じ出力で読み、範囲整理のとはの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030111
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030111 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SMF Type 80 とは INFORMATION LISTED
    ```

    IRRD105IとOSKB030111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SMF Type 80 とは と OSKB030111 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > z/OS 3.1

### MFA ポリシー拡張 {#c26-i0374}
*分類: z/OS 3.1*  ・  難易度: 上級

MFA ポリシー拡張は、MFADEF クラスでの細粒度ポリシー。「MFA ポリシー拡張」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 区切検査のポリシー拡張で MFA ポリシー拡張の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MFA ポリシー拡張の出力を取らず区切検査のポリシー拡張の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IRRD105I を読み、区切検査の結果として保存する。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して区切検査のポリシー拡張の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のポリシー拡張へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検査のポリシー拡張において選択記号 B を採用し、識別名は区切検査です。区切検査のポリシー拡張において MFA ポリシー拡張 は説明欄の「区切検査のポリシー拡張に関係する定義値と表示行を照合する区切検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は区切検査です。区切検査のポリシー拡張の証跡を読む担当者は、MFA ポリシー拡張の属性行と IRRD105I を合わせて追跡し、背景名は区切検査です。誤答側の問題点を分けます。 A: 区切検査のポリシー拡張は名称や説明のみに寄り、状態を示す出力本文が不足するため区切検査ではありません。 B: 区切検査のポリシー拡張は対象出力と項目説明を結び、根拠を残すので区切検査です。 C: 区切検査のポリシー拡張は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため区切検査ではありません。 D: 区切検査のポリシー拡張は別カテゴリの確認を流用しており、MFA ポリシー拡張の根拠にならないため区切検査ではありません。区切検査のポリシー拡張に出る MFA ポリシー拡張は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は区切検査です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **MFA ポリシー拡張**

    - 検証目的: 呼出分離のポリシー拡張について、MFA ポリシー拡張は、MFADEF クラスでの細粒度ポリシー。「MFA ポリシー拡張」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030143の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出分離のポリシー拡張の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にMFA ポリシー拡張を指定し、OSKB030143の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND MFA ポリシー拡張
    CASE OSKB030143
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM MFA ポリシー拡張
    CASE OSKB030143
    SOURCE RACF
    ```

    MFA ポリシー拡張とOSKB030143が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030143を同じ出力で読み、呼出分離のポリシー拡張の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030143
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030143 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I MFA ポリシー拡張 INFORMATION LISTED
    ```

    IRRD105IとOSKB030143が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の MFA ポリシー拡張 と OSKB030143 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030143 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)


