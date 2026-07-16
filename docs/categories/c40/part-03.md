---
search:
  exclude: true
---

# ユーティリティ — 詳細 (3/4)

[← ユーティリティ の概要へ戻る](index.md)


## ユーティリティ > IEBGENER

### GENERATE MAXLITS オペランド {#c40-i0163}
*分類: IEBGENER*  ・  難易度: 中級

GENERATE MAXLITS オペランドは、ユーティリティのIEBGENERで確認する項目です。FIELD パラメータで使用するリテラル (定数文字列) の総バイト数を申告する。リテラル挿入を行う編集で必要

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **GENERATE MAXLITS オペランド**

    - 検証目的: 区切確認のオペランドについて、GENERATE MAXLITS オペランドは、ユーティリティの IEBGENER で確認する項目です。FIELD パラメータで使用するリテラル (定数文字列) の総バイト数をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、区切確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にGENERATE MAXLITS オを指定し、OSKB010010の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND GENERATE MAXLITS オ
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM GENERATE MAXLITS オ
    CASE OSKB010010
    SOURCE z/OS Utilities
    ```

    GENERATE MAXLITS オとOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010010を同じ出力で読み、区切確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010010
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I GENERATE MAXLITS オペランド PROCESSING STARTED
    IEF142I OSKB010010 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の GENERATE MAXLITS オ と OSKB010010 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### GENERATE MAXNAME オペランド {#c40-i0164}
*分類: IEBGENER*  ・  難易度: 中級

GENERATE MAXNAME オペランドは、ユーティリティのIEBGENERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **GENERATE MAXNAME オペランド**

    - 検証目的: 条件確認のオペランドについて、GENERATE MAXNAME オペランドは、ユーティリティの IEBGENER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、条件確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にGENERATE MAXNAME オを指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND GENERATE MAXNAME オ
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM GENERATE MAXNAME オ
    CASE OSKB010009
    SOURCE z/OS Utilities
    ```

    GENERATE MAXNAME オとOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010009を同じ出力で読み、条件確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010009
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I GENERATE MAXNAME オペランド PROCESSING STARTED
    IEF142I OSKB010009 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の GENERATE MAXNAME オ と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### GENERATE 制御文 {#c40-i0165}
*分類: IEBGENER*  ・  難易度: 中級

GENERATE 制御文は、ユーティリティのIEBGENERで確認する項目です。RECORD/MEMBER で部分編集を行う場合に冒頭に置く宣言文。MAXFLDS=n / MAXNAME=n で編集領域と名前テーブルサイズを宣言する

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **GENERATE 制御文**

    - 検証目的: 上書確認の制御文について、GENERATE 制御文は、ユーティリティの IEBGENER で確認する項目です。RECORD/MEMBER で部分編集を行う場合に冒頭に置く宣言文。MAXFLDS=n /に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、上書確認の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にGENERATE 制御文を指定し、OSKB010007の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND GENERATE 制御文
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM GENERATE 制御文
    CASE OSKB010007
    SOURCE z/OS Utilities
    ```

    GENERATE 制御文とOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010007を同じ出力で読み、上書確認の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010007
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I GENERATE 制御文 PROCESSING STARTED
    IEF142I OSKB010007 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の GENERATE 制御文 と OSKB010007 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ICEGENER (DFSORT 高速版) との関係 {#c40-i0166}
*分類: IEBGENER*  ・  難易度: 中級

ICEGENER (DFSORT 高速版) との関係は、ユーティリティのIEBGENERで確認する項目です。DFSORT 導入環境では IEBGENER の SVC が ICEGENER に置換され、内部で SORT COPY 相当に高速実行されることがある。JCL 上は IEBGENER のままで透過置換される

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **ICEGENER (DFSORT 高速版) との関係**

    - 検証目的: 構文照合の高速版 とのについて、ICEGENER (DFSORT 高速版) との関係は、ユーティリティの IEBGENER で確認する項目です。DFSORT 導入環境では IEBGENER の SVC が Iに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010021の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、構文照合の高速版 とのの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    ```

    COMMAND INPUTにST OSKBSORTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にICEGENER (DFSORT 高を指定し、OSKB010021の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ICEGENER (DFSORT 高
    CASE OSKB010021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ICEGENER (DFSORT 高
    CASE OSKB010021
    SOURCE z/OS Utilities
    ```

    ICEGENER (DFSORT 高とOSKB010021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB010021を同じ出力で読み、構文照合の高速版 とのの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB010021
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010021
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I ICEGENER (DFSORT 高速版) との PROCESSING STARTED
    IEF142I OSKB010021 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB010021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の ICEGENER (DFSORT 高 と OSKB010021 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB010021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### MEMBER NAME=メンバー名 {#c40-i0167}
*分類: IEBGENER*  ・  難易度: 中級

MEMBER NAME=メンバー名は、ユーティリティのIEBGENERで確認する項目です。MEMBER 制御文のオペランド。8 文字以内のメンバー名を指定する。複数 MEMBER を並べて 1 度の実行で複数メンバーを生成できる

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **MEMBER NAME= メンバー名**

    - 検証目的: 優先確認のメンバー名について、MEMBER NAME= メンバー名は、ユーティリティの IEBGENER で確認する項目です。MEMBER 制御文のオペランド。8 文字以内のメンバー名を指定する。複数 MEMに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、優先確認のメンバー名の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMEMBER NAME= メンバー名を指定し、OSKB010012の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MEMBER NAME= メンバー名
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MEMBER NAME= メンバー名
    CASE OSKB010012
    SOURCE z/OS Utilities
    ```

    MEMBER NAME= メンバー名とOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010012を同じ出力で読み、優先確認のメンバー名の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010012
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I MEMBER NAME= メンバー名 PROCESSING STARTED
    IEF142I OSKB010012 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の MEMBER NAME= メンバー名 と OSKB010012 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### MEMBER 制御文 {#c40-i0168}
*分類: IEBGENER*  ・  難易度: 中級

MEMBER 制御文は、ユーティリティのIEBGENERで確認する項目です。出力先 PDS の中で新しく作成 (または置換) するメンバー名を指定する。続く RECORD 制御文の対象メンバーとなる

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（2件）"
    **MEMBER 制御文**

    - 検証目的: 範囲確認の制御文について、MEMBER 制御文は、ユーティリティの IEBGENER で確認する項目です。出力先 PDS の中で新しく作成 (または置換) するメンバー名を指定する。続く RECORDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、範囲確認の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMEMBER 制御文を指定し、OSKB010011の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MEMBER 制御文
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MEMBER 制御文
    CASE OSKB010011
    SOURCE z/OS Utilities
    ```

    MEMBER 制御文とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010011を同じ出力で読み、範囲確認の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010011
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I MEMBER 制御文 PROCESSING STARTED
    IEF142I OSKB010011 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の MEMBER 制御文 と OSKB010011 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **MEMBER 制御文**

    - 検証目的: 上書判定の制御文について、MEMBER 制御文は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、上書判定の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMEMBER 制御文を指定し、OSKB010087の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MEMBER 制御文
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MEMBER 制御文
    CASE OSKB010087
    SOURCE z/OS Utilities
    ```

    MEMBER 制御文とOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010087を同じ出力で読み、上書判定の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010087
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I MEMBER 制御文 PROCESSING STARTED
    IEF142I OSKB010087 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の MEMBER 制御文 と OSKB010087 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### PDS メンバーへの出力 (DSN=lib(mem)) {#c40-i0169}
*分類: IEBGENER*  ・  難易度: 中級

PDS メンバーへの出力 (DSN=lib(mem))は、ユーティリティのIEBGENERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **PDS メンバーへの出力 (DSN=lib(mem))**

    - 検証目的: 監査確認のメンバーへの出力について、PDS メンバーへの出力 (DSN=lib(mem))は、ユーティリティの IEBGENER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、監査確認のメンバーへの出力の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPDS メンバーへの出力 (DSN=を指定し、OSKB010019の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PDS メンバーへの出力 (DSN=
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PDS メンバーへの出力 (DSN=
    CASE OSKB010019
    SOURCE z/OS Utilities
    ```

    PDS メンバーへの出力 (DSN=とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010019を同じ出力で読み、監査確認のメンバーへの出力の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010019
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I PDS メンバーへの出力 (DSN=lib(me PROCESSING STARTED
    IEF142I OSKB010019 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の PDS メンバーへの出力 (DSN= と OSKB010019 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RECORD FIELD オペランド {#c40-i0170}
*分類: IEBGENER*  ・  難易度: 中級

RECORD FIELD オペランドは、ユーティリティのIEBGENERで確認する項目です。(長さ,入力位置,変換,出力位置) の 4 要素で 1 フィールドの編集を指定する。1 個の RECORD 制御文に複数 FIELD を並べられる

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **RECORD FIELD オペランド**

    - 検証目的: 順序確認のオペランドについて、RECORD FIELD オペランドは、ユーティリティの IEBGENER で確認する項目です。(長さ,入力位置,変換,出力位置) の 4 要素で 1 フィールドの編集を指定すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、順序確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD FIELD オペランドを指定し、OSKB010015の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD FIELD オペランド
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD FIELD オペランド
    CASE OSKB010015
    SOURCE z/OS Utilities
    ```

    RECORD FIELD オペランドとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010015を同じ出力で読み、順序確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010015
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RECORD FIELD オペランド PROCESSING STARTED
    IEF142I OSKB010015 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RECORD FIELD オペランド と OSKB010015 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RECORD FIELD リテラル挿入 {#c40-i0171}
*分類: IEBGENER*  ・  難易度: 中級

RECORD FIELD リテラル挿入は、ユーティリティのIEBGENERで確認する項目です。入力位置の代わりに 'C''abc''' のようなリテラル指定で固定文字列を出力に埋め込むことができる。GENERATE MAXLITS で総量を申告する

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **RECORD FIELD リテラル挿入**

    - 検証目的: 警告確認のリテラル挿入について、RECORD FIELD リテラル挿入は、ユーティリティの IEBGENER で確認する項目です。入力位置の代わりに 'C''abc''' のようなリテラル指定で固定文字列を出に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、警告確認のリテラル挿入の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD FIELD リテラル挿を指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD FIELD リテラル挿
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD FIELD リテラル挿
    CASE OSKB010017
    SOURCE z/OS Utilities
    ```

    RECORD FIELD リテラル挿とOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010017を同じ出力で読み、警告確認のリテラル挿入の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010017
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RECORD FIELD リテラル挿入 PROCESSING STARTED
    IEF142I OSKB010017 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RECORD FIELD リテラル挿 と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RECORD FIELD 変換コード {#c40-i0172}
*分類: IEBGENER*  ・  難易度: 中級

RECORD FIELD 変換コードは、ユーティリティのIEBGENERで機能名、見出し、または確認対象として参照する項目です。PZ (Packed[...]Zoned)、ZP (Zoned[...]Packed)、HE (16進[...]EBCDIC) などの変換コードを指定する。省略時は変換無しのバイト単位コピー。PZ (Packed→Zoned)、ZP (Zoned→Packed)、HE (16進→EBCDIC) などの変換コードを指定する。省略時は変換無しのバイト単位コピー

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **RECORD FIELD 変換コード**

    - 検証目的: 値域確認の変換コードについて、RECORD FIELD 変換コードは、ユーティリティの IEBGENER で機能名、見出し、または確認対象として参照する項目です。PZ (Packed[など]Zoned)、Zに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、値域確認の変換コードの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD FIELD 変換コードを指定し、OSKB010016の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD FIELD 変換コード
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD FIELD 変換コード
    CASE OSKB010016
    SOURCE z/OS Utilities
    ```

    RECORD FIELD 変換コードとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010016を同じ出力で読み、値域確認の変換コードの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010016
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RECORD FIELD 変換コード PROCESSING STARTED
    IEF142I OSKB010016 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RECORD FIELD 変換コード と OSKB010016 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RECORD IDENT オペランド {#c40-i0173}
*分類: IEBGENER*  ・  難易度: 中級

RECORD IDENT オペランドは、ユーティリティのIEBGENERで確認する項目です。(長さ,'文字列',位置) の 3 要素で識別レコードを指定する。指定した識別レコードに到達するまで前段の編集を続け、到達後に次の RECORD ブロックへ移る

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **RECORD IDENT オペランド**

    - 検証目的: 比較確認のオペランドについて、RECORD IDENT オペランドは、ユーティリティの IEBGENER で確認する項目です。(長さ,'文字列',位置) の 3 要素で識別レコードを指定する。指定した識別レに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、比較確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD IDENT オペランドを指定し、OSKB010014の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD IDENT オペランド
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD IDENT オペランド
    CASE OSKB010014
    SOURCE z/OS Utilities
    ```

    RECORD IDENT オペランドとOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010014を同じ出力で読み、比較確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010014
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RECORD IDENT オペランド PROCESSING STARTED
    IEF142I OSKB010014 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RECORD IDENT オペランド と OSKB010014 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RECORD 制御文 {#c40-i0174}
*分類: IEBGENER*  ・  難易度: 中級

RECORD 制御文は、ユーティリティのIEBGENERで確認する項目です。コピー対象となる入力レコード範囲と編集内容を指定する。IDENT / FIELD オペランドで「どこから」と「何を編集」を表現する

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 条件照合の制御文に関係する RECORD 制御文の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. RECORD 制御文の名称と担当者名のみを残して条件照合の制御文の表示本文を確認対象に含めない。
    - C. ユーティリティ以外の画面で条件照合の制御文を確認し同じ証跡として扱ったことにする。
    - D. ICE000I の有無を見ず条件照合の制御文の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合の制御文において選択記号 A を採用し、識別名は条件照合です。条件照合の制御文において RECORD 制御文 は説明欄の「RECORD 制御文の用途をユーティリティの表示で確認する条件照合項目」と ST OSKBSORT または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の制御文に関連して、z/OS Utilitiesでは RECORD 制御文の表示属性と ICE000I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の制御文は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の制御文は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の制御文は別カテゴリの確認を流用しており、RECORD 制御文の根拠にならないため条件照合ではありません。 D: 条件照合の制御文は戻り値や記録番号に寄り、ICE000I や属性表示を落とすため条件照合ではありません。条件照合の制御文で使う RECORD 制御文という用語はユーティリティで扱う確認対象であり、用語名は条件照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（3件）"
    **RECORD 制御文**

    - 検証目的: 記録確認の制御文について、RECORD 制御文は、ユーティリティの IEBGENER で確認する項目です。コピー対象となる入力レコード範囲と編集内容を指定する。IDENT / FIELD オペランドで「に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、記録確認の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD 制御文を指定し、OSKB010013の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD 制御文
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD 制御文
    CASE OSKB010013
    SOURCE z/OS Utilities
    ```

    RECORD 制御文とOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010013を同じ出力で読み、記録確認の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010013
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RECORD 制御文 PROCESSING STARTED
    IEF142I OSKB010013 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RECORD 制御文 と OSKB010013 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **RECORD 制御文**

    - 検証目的: 出力判定の制御文について、RECORD 制御文は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010088の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、出力判定の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD 制御文を指定し、OSKB010088の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD 制御文
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD 制御文
    CASE OSKB010088
    SOURCE z/OS Utilities
    ```

    RECORD 制御文とOSKB010088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010088を同じ出力で読み、出力判定の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010088
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RECORD 制御文 PROCESSING STARTED
    IEF142I OSKB010088 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RECORD 制御文 と OSKB010088 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **RECORD 制御文**

    - 検証目的: 優先検査の制御文について、RECORD 制御文は、ユーティリティの DFSORT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、優先検査の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    ```

    COMMAND INPUTにST OSKBSORTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORD 制御文を指定し、OSKB020072の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORD 制御文
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORD 制御文
    CASE OSKB020072
    SOURCE z/OS Utilities
    ```

    RECORD 制御文とOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020072を同じ出力で読み、優先検査の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020072
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I RECORD 制御文 PROCESSING STARTED
    IEF142I OSKB020072 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の RECORD 制御文 と OSKB020072 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)



### SYSIN DD (制御文) {#c40-i0175}
*分類: IEBGENER*  ・  難易度: 中級

SYSIN DD (制御文)は、ユーティリティのIEBGENERで機能名、見出し、または確認対象として参照する項目です。GENERATE / RECORD / MEMBER などの制御文を入力する DD。単純コピーであれば DD DUMMY または //SYSIN DD DUMMY とする

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SYSIN DD (制御文)**

    - 検証目的: 終端確認の制御文について、SYSIN DD (制御文)は、ユーティリティの IEBGENER で機能名、見出し、または確認対象として参照する項目です。GENERATE / RECORD / MEMBERに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、終端確認の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSIN DD (制御文)を指定し、OSKB010005の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSIN DD (制御文)
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSIN DD (制御文)
    CASE OSKB010005
    SOURCE z/OS Utilities
    ```

    SYSIN DD (制御文)とOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010005を同じ出力で読み、終端確認の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010005
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSIN DD (制御文) PROCESSING STARTED
    IEF142I OSKB010005 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSIN DD (制御文) と OSKB010005 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSIN DD DUMMY (制御文無しの単純コピー) {#c40-i0176}
*分類: IEBGENER*  ・  難易度: 中級

SYSIN DD DUMMY (制御文無しの単純コピー)は、ユーティリティのIEBGENERで確認する項目です。制御文を全く与えない場合は SYSIN DD DUMMY を書く。SYSUT1[...]SYSUT2 のレコード単純コピーが実行される

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SYSIN DD DUMMY (制御文無しの単純コピー)**

    - 検証目的: 探索確認の制御文無しの単純について、SYSIN DD DUMMY (制御文無しの単純コピー)は、ユーティリティの IEBGENER で確認する項目です。制御文を全く与えない場合は SYSIN DD DUMMY をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、探索確認の制御文無しの単純の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSIN DD DUMMY (制御を指定し、OSKB010006の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSIN DD DUMMY (制御
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSIN DD DUMMY (制御
    CASE OSKB010006
    SOURCE z/OS Utilities
    ```

    SYSIN DD DUMMY (制御とOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010006を同じ出力で読み、探索確認の制御文無しの単純の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010006
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSIN DD DUMMY (制御文無しの単純 PROCESSING STARTED
    IEF142I OSKB010006 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSIN DD DUMMY (制御 と OSKB010006 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSOUT への印刷用途 {#c40-i0177}
*分類: IEBGENER*  ・  難易度: 中級

SYSOUT への印刷用途は、ユーティリティのIEBGENERで確認する項目です。SYSUT2 を SYSOUT=A や SYSOUT=* にすれば順次データセットをそのまま印刷キューに送れる。SDSF で見るデバッグ出力用途で頻出

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SYSOUT への印刷用途**

    - 検証目的: 変更確認のへの印刷用途について、SYSOUT への印刷用途は、ユーティリティの IEBGENER で確認する項目です。SYSUT2 を SYSOUT=A や SYSOUT=* にすれば順次データセットをそのまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、変更確認のへの印刷用途の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSOUT への印刷用途を指定し、OSKB010020の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSOUT への印刷用途
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSOUT への印刷用途
    CASE OSKB010020
    SOURCE z/OS Utilities
    ```

    SYSOUT への印刷用途とOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010020を同じ出力で読み、変更確認のへの印刷用途の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010020
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSOUT への印刷用途 PROCESSING STARTED
    IEF142I OSKB010020 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSOUT への印刷用途 と OSKB010020 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSPRINT DD (メッセージ出力) {#c40-i0178}
*分類: IEBGENER*  ・  難易度: 中級

ユーティリティのメッセージと統計情報を出力する DD。SYSOUT=* が典型値。省略すると JCL ERROR

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SYSPRINT DD (メッセージ出力)**

    - 検証目的: 置換確認のメッセージ出力について、ユーティリティのメッセージと統計情報を出力する DD。SYSOUT=* が典型値。省略すると JCL ERRORに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、置換確認のメッセージ出力の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSPRINT DD (メッセージを指定し、OSKB010004の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSPRINT DD (メッセージ
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSPRINT DD (メッセージ
    CASE OSKB010004
    SOURCE z/OS Utilities
    ```

    SYSPRINT DD (メッセージとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010004を同じ出力で読み、置換確認のメッセージ出力の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010004
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSPRINT DD (メッセージ出力) PROCESSING STARTED
    IEF142I OSKB010004 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSPRINT DD (メッセージ と OSKB010004 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSUT1 DD (入力) {#c40-i0179}
*分類: IEBGENER*  ・  難易度: 中級

SYSUT1 DD (入力)は、ユーティリティのIEBGENERで確認する項目です。コピー元の入力データセットを指定する DD。順次データセット、PDS メンバー、SYSIN 形式の埋め込みデータも入力にできる

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（2件）"
    **SYSUT1 DD (入力)**

    - 検証目的: 展開確認の入力について、SYSUT1 DD (入力)は、ユーティリティの IEBGENER で確認する項目です。コピー元の入力データセットを指定する DD。順次データセット、PDS メンバー、SYSIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開確認の入力の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSUT1 DD (入力)を指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSUT1 DD (入力)
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSUT1 DD (入力)
    CASE OSKB010002
    SOURCE z/OS Utilities
    ```

    SYSUT1 DD (入力)とOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010002を同じ出力で読み、展開確認の入力の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010002
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSUT1 DD (入力) PROCESSING STARTED
    IEF142I OSKB010002 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSUT1 DD (入力) と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **SYSUT1 DD (入力)**

    - 検証目的: 変更検査の入力について、SYSUT1 DD (入力)は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010080の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、変更検査の入力の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSUT1 DD (入力)を指定し、OSKB010080の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSUT1 DD (入力)
    CASE OSKB010080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSUT1 DD (入力)
    CASE OSKB010080
    SOURCE z/OS Utilities
    ```

    SYSUT1 DD (入力)とOSKB010080が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010080を同じ出力で読み、変更検査の入力の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010080
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010080
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSUT1 DD (入力) PROCESSING STARTED
    IEF142I OSKB010080 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010080が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSUT1 DD (入力) と OSKB010080 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSUT2 DD (出力) {#c40-i0180}
*分類: IEBGENER*  ・  難易度: 中級

SYSUT2 DD (出力)は、ユーティリティのIEBGENERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（2件）"
    **SYSUT2 DD (出力)**

    - 検証目的: 呼出確認の出力について、SYSUT2 DD (出力)は、ユーティリティの IEBGENER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、呼出確認の出力の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSUT2 DD (出力)を指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSUT2 DD (出力)
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSUT2 DD (出力)
    CASE OSKB010003
    SOURCE z/OS Utilities
    ```

    SYSUT2 DD (出力)とOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010003を同じ出力で読み、呼出確認の出力の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010003
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSUT2 DD (出力) PROCESSING STARTED
    IEF142I OSKB010003 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSUT2 DD (出力) と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **SYSUT2 DD (出力)**

    - 検証目的: 構文判定の出力について、SYSUT2 DD (出力)は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。印刷時は SYSPRINT 形式 (RECFM=FBに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、構文判定の出力の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSUT2 DD (出力)を指定し、OSKB010081の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSUT2 DD (出力)
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSUT2 DD (出力)
    CASE OSKB010081
    SOURCE z/OS Utilities
    ```

    SYSUT2 DD (出力)とOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010081を同じ出力で読み、構文判定の出力の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010081
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSUT2 DD (出力) PROCESSING STARTED
    IEF142I OSKB010081 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSUT2 DD (出力) と OSKB010081 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ユーティリティの基本機能 {#c40-i0181}
*分類: IEBGENER*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEBGENERで確認する項目です。順次データセット (PS) の単純コピー・印刷・PDS メンバー化を行う標準ユーティリティ。SYSUT1 から SYSUT2 へレコードを転送する

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? question "確認問題（3問）"
    **問題.** 上書追跡のユーティリティの基本機能でユーティリティの運用確認を行います。ユーティリティの基本機能の根拠にできる作業はどれですか。

    - A. z/OS Utilitiesと無関係な一覧で上書追跡のユーティリティの基本機能を確認した扱いにする。
    - B. ICE000I の有無を確認せず上書追跡のユーティリティの基本機能を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. ユーティリティの基本機能の属性行を読まず上書追跡のユーティリティの基本機能の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書追跡のユーティリティの基本機能において選択記号 C を採用し、識別名は上書追跡です。上書追跡のユーティリティの基本機能においてユーティリティの基本機能は説明欄の「z/OS Utilitiesでユーティリティの基本機能の扱いを記録する上書追跡項目」と ST OSKBSORT または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のユーティリティの基本機能を受け取る担当者は、ユーティリティの基本機能の表示結果と ICE000I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のユーティリティの基本機能は別カテゴリの確認を流用しており、ユーティリティの基本機能の根拠にならないため上書追跡ではありません。 B: 上書追跡のユーティリティの基本機能は戻り値や記録番号に寄り、ICE000I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のユーティリティの基本機能は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のユーティリティの基本機能は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のユーティリティの基本機能が示すユーティリティの基本機能は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200

    ---

    **問題.** 範囲検査のユーティリティの基本機能でユーティリティの運用確認を行います。ユーティリティの基本機能の根拠にできる作業はどれですか。

    - A. z/OS Utilitiesと無関係な一覧で範囲検査のユーティリティの基本機能を確認した扱いにする。
    - B. IEF142I の有無を確認せず範囲検査のユーティリティの基本機能を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲検査の記録として扱う。 ✅
    - D. ユーティリティの基本機能の属性行を読まず範囲検査のユーティリティの基本機能の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 範囲検査のユーティリティの基本機能において選択記号 C を採用し、識別名は範囲検査です。範囲検査のユーティリティの基本機能においてユーティリティの基本機能は説明欄の「z/OS Utilitiesでユーティリティの基本機能の扱いを記録する範囲検査項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は範囲検査です。範囲検査のユーティリティの基本機能を受け取る担当者は、ユーティリティの基本機能の表示結果と IEF142I を同じ確認単位として扱い、背景名は範囲検査です。不適切な選択肢を整理します。 A: 範囲検査のユーティリティの基本機能は別カテゴリの確認を流用しており、ユーティリティの基本機能の根拠にならないため範囲検査ではありません。 B: 範囲検査のユーティリティの基本機能は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため範囲検査ではありません。 C: 範囲検査のユーティリティの基本機能は対象出力と項目説明を結び、根拠を残すので範囲検査です。 D: 範囲検査のユーティリティの基本機能は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲検査ではありません。範囲検査のユーティリティの基本機能が示すユーティリティの基本機能は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200

    ---

    **問題.** 呼出判定のユーティリティの基本機能でユーティリティの運用確認を行います。ユーティリティの基本機能の根拠にできる作業はどれですか。

    - A. z/OS Utilitiesと無関係な一覧で呼出判定のユーティリティの基本機能を確認した扱いにする。
    - B. IEF142I の有無を確認せず呼出判定のユーティリティの基本機能を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出判定の記録として扱う。 ✅
    - D. ユーティリティの基本機能の属性行を読まず呼出判定のユーティリティの基本機能の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 呼出判定のユーティリティの基本機能において選択記号 C を採用し、識別名は呼出判定です。呼出判定のユーティリティの基本機能においてユーティリティの基本機能は説明欄の「z/OS Utilitiesでユーティリティの基本機能の扱いを記録する呼出判定項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は呼出判定です。呼出判定のユーティリティの基本機能を受け取る担当者は、ユーティリティの基本機能の表示結果と IEF142I を同じ確認単位として扱い、背景名は呼出判定です。不適切な選択肢を整理します。 A: 呼出判定のユーティリティの基本機能は別カテゴリの確認を流用しており、ユーティリティの基本機能の根拠にならないため呼出判定ではありません。 B: 呼出判定のユーティリティの基本機能は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため呼出判定ではありません。 C: 呼出判定のユーティリティの基本機能は対象出力と項目説明を結び、根拠を残すので呼出判定です。 D: 呼出判定のユーティリティの基本機能は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出判定ではありません。呼出判定のユーティリティの基本機能が示すユーティリティの基本機能は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（17件）"
    **ユーティリティの基本機能**

    - 検証目的: 構文確認のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBGENER で確認する項目です。順次データセット (PS) の単純コピー・印刷・ PDS メンバー化を行う標準ユーティリティ。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、構文確認のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010001の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010001
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010001を同じ出力で読み、構文確認のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010001
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010001 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010001 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 展開照合のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBCOPY で確認する項目です。PDS / PDSE の全体コピー、メンバー選択コピー、圧縮、UNLOAD/LOAD を行う標に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開照合のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010022の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010022
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010022を同じ出力で読み、展開照合のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010022
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010022
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010022 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010022 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 置換追跡のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBCOMPR で確認する項目です。2 つの順次データセット、または 2 つの PDS をレコード単位で比較し、不一致を SYSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、置換追跡のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010044の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010044
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010044を同じ出力で読み、置換追跡のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010044
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010044 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010044 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 範囲追跡のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEHLIST で確認する項目です。VTOC、カタログ、PDS ディレクトリの内容を SYSPRINT に出力する診断系ユーティリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、範囲追跡のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010051の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010051
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010051を同じ出力で読み、範囲追跡のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010051
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010051 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010051 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 置換検査のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEHPROGM で確認する項目です。データセットの SCRATCH (物理削除)、UNCATLG (カタログ抹消)、CATLGに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、置換検査のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010064の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010064
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010064を同じ出力で読み、置換検査のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010064
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010064 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010064 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 監査検査のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBPTPCH で確認する項目です。データセット (順次 / PDS) を SYSPRINT に印刷したり、SYSPUNCH (に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、監査検査のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010079の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010079
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010079を同じ出力で読み、監査検査のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010079
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010079 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010079 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 優先判定のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBUPDTE で確認する項目です。PDS メンバーの追加・置換・行単位の編集を行う。SYSIN に「./」で始まる制御文と新規に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、優先判定のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010092の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010092
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010092を同じ出力で読み、優先判定のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010092
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010092 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010092 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 呼出整理のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBDG で確認する項目です。テストデータを定義に従って自動生成するユーティリティ。FD / CREATE / REPEAT /に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010103の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、呼出整理のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010103の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010103
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010103を同じ出力で読み、呼出整理のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010103
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010103 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010103 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 範囲整理のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEBEDIT で確認する項目です。JCL ストリームから特定のジョブ / ステップだけを抜き出して別 SYSOUT (例: INに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010111の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、範囲整理のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010111の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010111
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010111を同じ出力で読み、範囲整理のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010111
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010111 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010111 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 警告整理のユーティリティの基本機能について、DASD ボリュームの初期化、ラベル変更、不良トラックの検査・代替化、ボリュームコピー、コピー前検査などを行うストレージ管理ユーティリティ。PARM='ONLINE' /に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010117の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDASDを実行し、ICK00001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDASD を入力し、警告整理のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDASD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDASD
    ```

    COMMAND INPUTにST OSKBDASDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB010117の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB010117
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB010117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICK00001IとOSKB010117を同じ出力で読み、警告整理のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDASD
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010117
    //STEP1 EXEC PGM=OSKBDASD
    ICK00001I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB010117 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICK00001IとOSKB010117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDASD が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB010117 が画面・出力に表示されること
    ③ ステップ3 の ICK00001I と OSKB010117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Device Support Facilities (ICKDSF) ICKDSF R17 User's Guide (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 区切確認のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEHINITT で確認する項目です。テープボリュームを IBM 標準ラベルまたは ANSI ラベルで初期化する。複数巻のテープにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、区切確認のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020010の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020010
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020010を同じ出力で読み、区切確認のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020010
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020010 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020010 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 値域確認のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの IEHMOVE で確認する項目です。データセット (PS/PDS) やボリューム全体のコピー・移動を行う旧式ユーティリティ。現代でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、値域確認のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020016の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020016
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020016を同じ出力で読み、値域確認のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020016
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020016 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020016 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 置換照合のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの DFSORT で機能名、見出し、または確認対象として参照する項目です。IBM の高機能ソート/マージ/コピーユーティリティ。SORに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、置換照合のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    ```

    COMMAND INPUTにST OSKBSORTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020024
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020024を同じ出力で読み、置換照合のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020024
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020024 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 区切判定のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの ICETOOL で機能名、見出し、または確認対象として参照する項目です。DFSORT の高位ラッパー。1 ステップで複数の SORに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、区切判定のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBSORT
    ```

    COMMAND INPUTにST OSKBSORTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020090の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020090
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020090を同じ出力で読み、区切判定のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020090
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020090
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020090 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020090 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 上書整理のユーティリティの基本機能について、ロードモジュールやデータレコードに対して 16 進パッチを当てるサービスエイドユーティリティ。プログラム修正の最終手段として使われるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、上書整理のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020107の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020107
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020107を同じ出力で読み、上書整理のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020107
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020107 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020107 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Program Management: Advanced Facilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 比較整理のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの AMBLIST で確認する項目です。ロードモジュール、プログラムオブジェクト、オブジェクトモジュールの構造解析・ MAP 出力を行うに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、比較整理のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020114の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020114
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020114を同じ出力で読み、比較整理のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020114
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020114 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020114 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Program Management: Advanced Facilities (z / OS 3.1)

    ---

    **ユーティリティの基本機能**

    - 検証目的: 探索記録のユーティリティの基本機能について、ユーティリティの基本機能は、ユーティリティの BPXBATCH で機能名、見出し、または確認対象として参照する項目です。JCL からバッチジョブとして UNIX Systemに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020126の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、探索記録のユーティリティの基本機能の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの基本機能を指定し、OSKB020126の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの基本機能
    CASE OSKB020126
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの基本機能
    CASE OSKB020126
    SOURCE z/OS Utilities
    ```

    ユーティリティの基本機能とOSKB020126が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020126を同じ出力で読み、探索記録のユーティリティの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020126
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020126
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの基本機能 PROCESSING STARTED
    IEF142I OSKB020126 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020126が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの基本機能 と OSKB020126 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020126 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide (z / OS 3.1)




## ユーティリティ > IEBPTPCH

### MAXFLDS / MAXNAME / MAXLITS {#c40-i0182}
*分類: IEBPTPCH*  ・  難易度: 中級

MAXFLDS / MAXNAME / MAXLITSは、ユーティリティのIEBPTPCHで確認する項目です。RECORD/MEMBER 制御文で使うフィールド数・メンバー数・リテラル総量の最大値申告。IEBGENER と同じ意味

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **MAXFLDS ・ MAXNAME ・ MAXLITS**

    - 検証目的: 終端判定の・ ・について、MAXFLDS / MAXNAME / MAXLITS は、ユーティリティの IEBPTPCH で確認する項目です。RECORD/MEMBER 制御文で使うフィールド数・メンバーに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、終端判定の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMAXFLDS ・ MAXNAME を指定し、OSKB010085の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MAXFLDS ・ MAXNAME 
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MAXFLDS ・ MAXNAME 
    CASE OSKB010085
    SOURCE z/OS Utilities
    ```

    MAXFLDS ・ MAXNAME とOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010085を同じ出力で読み、終端判定の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010085
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I MAXFLDS ・ MAXNAME ・ MAXL PROCESSING STARTED
    IEF142I OSKB010085 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の MAXFLDS ・ MAXNAME  と OSKB010085 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### MEMBER 制御文 {#c40-i0183}
*分類: IEBPTPCH*  ・  難易度: 中級

MEMBER 制御文は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### PREFORM オペランド {#c40-i0184}
*分類: IEBPTPCH*  ・  難易度: 中級

PREFORM オペランドは、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **PREFORM オペランド**

    - 検証目的: 条件判定のオペランドについて、PREFORM オペランドは、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010089の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、条件判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPREFORM オペランドを指定し、OSKB010089の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PREFORM オペランド
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PREFORM オペランド
    CASE OSKB010089
    SOURCE z/OS Utilities
    ```

    PREFORM オペランドとOSKB010089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010089を同じ出力で読み、条件判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010089
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I PREFORM オペランド PROCESSING STARTED
    IEF142I OSKB010089 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の PREFORM オペランド と OSKB010089 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### PRINT 制御文 {#c40-i0185}
*分類: IEBPTPCH*  ・  難易度: 中級

PRINT 制御文は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **PRINT 制御文**

    - 検証目的: 展開判定の制御文について、PRINT 制御文は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開判定の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPRINT 制御文を指定し、OSKB010082の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PRINT 制御文
    CASE OSKB010082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PRINT 制御文
    CASE OSKB010082
    SOURCE z/OS Utilities
    ```

    PRINT 制御文とOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010082を同じ出力で読み、展開判定の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010082
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010082
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I PRINT 制御文 PROCESSING STARTED
    IEF142I OSKB010082 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の PRINT 制御文 と OSKB010082 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### PUNCH 制御文 {#c40-i0186}
*分類: IEBPTPCH*  ・  難易度: 中級

PUNCH 制御文は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **PUNCH 制御文**

    - 検証目的: 呼出判定の制御文について、PUNCH 制御文は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、呼出判定の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPUNCH 制御文を指定し、OSKB010083の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PUNCH 制御文
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PUNCH 制御文
    CASE OSKB010083
    SOURCE z/OS Utilities
    ```

    PUNCH 制御文とOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010083を同じ出力で読み、呼出判定の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010083
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I PUNCH 制御文 PROCESSING STARTED
    IEF142I OSKB010083 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の PUNCH 制御文 と OSKB010083 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RECORD 制御文 {#c40-i0187}
*分類: IEBPTPCH*  ・  難易度: 中級

RECORD 制御文は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### STRTAFT / STOPAFT オペランド {#c40-i0188}
*分類: IEBPTPCH*  ・  難易度: 中級

STRTAFT / STOPAFT オペランドは、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **STRTAFT ・ STOPAFT オペランド**

    - 検証目的: 範囲判定の・ オペランドについて、STRTAFT / STOPAFT オペランドは、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010091の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、範囲判定の・ オペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSTRTAFT ・ STOPAFT を指定し、OSKB010091の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND STRTAFT ・ STOPAFT 
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM STRTAFT ・ STOPAFT 
    CASE OSKB010091
    SOURCE z/OS Utilities
    ```

    STRTAFT ・ STOPAFT とOSKB010091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010091を同じ出力で読み、範囲判定の・ オペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010091
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I STRTAFT ・ STOPAFT オペランド PROCESSING STARTED
    IEF142I OSKB010091 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の STRTAFT ・ STOPAFT  と OSKB010091 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSUT1 DD (入力) {#c40-i0189}
*分類: IEBPTPCH*  ・  難易度: 中級

SYSUT1 DD (入力)は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### SYSUT2 DD (出力) {#c40-i0190}
*分類: IEBPTPCH*  ・  難易度: 中級

SYSUT2 DD (出力)は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。印刷時は SYSPRINT 形式 (RECFM=FBA LRECL=121)、PUNCH 時はカード形式 (RECFM=FB LRECL=80) の出力 DD

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### TITLE 制御文 {#c40-i0191}
*分類: IEBPTPCH*  ・  難易度: 中級

TITLE 制御文は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **TITLE 制御文**

    - 検証目的: 探索判定の制御文について、TITLE 制御文は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010086の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、探索判定の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTITLE 制御文を指定し、OSKB010086の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TITLE 制御文
    CASE OSKB010086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TITLE 制御文
    CASE OSKB010086
    SOURCE z/OS Utilities
    ```

    TITLE 制御文とOSKB010086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010086を同じ出力で読み、探索判定の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010086
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010086
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I TITLE 制御文 PROCESSING STARTED
    IEF142I OSKB010086 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の TITLE 制御文 と OSKB010086 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### TOTCONV=XE / PZ (全体変換) {#c40-i0192}
*分類: IEBPTPCH*  ・  難易度: 中級

TOTCONV=XE / PZ (全体変換)は、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。入力全体を 16 進または Packed[...]Zoned 変換しながら印刷する。デバッグダンプに頻用。入力全体を 16 進または Packed→Zoned 変換しながら印刷する。デバッグダンプに頻用

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **TOTCONV=XE ・ PZ (全体変換)**

    - 検証目的: 区切判定の・ 全体変換について、TOTCONV=XE / PZ (全体変換)は、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。入力全体を 16 進または Packに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010090の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、区切判定の・ 全体変換の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTOTCONV=XE ・ PZ (全を指定し、OSKB010090の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TOTCONV=XE ・ PZ (全
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TOTCONV=XE ・ PZ (全
    CASE OSKB010090
    SOURCE z/OS Utilities
    ```

    TOTCONV=XE ・ PZ (全とOSKB010090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010090を同じ出力で読み、区切判定の・ 全体変換の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010090
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I TOTCONV=XE ・ PZ (全体変換) PROCESSING STARTED
    IEF142I OSKB010090 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の TOTCONV=XE ・ PZ (全 と OSKB010090 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### TYPORG オペランド {#c40-i0193}
*分類: IEBPTPCH*  ・  難易度: 中級

TYPORG オペランドは、ユーティリティのIEBPTPCHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **TYPORG オペランド**

    - 検証目的: 置換判定のオペランドについて、TYPORG オペランドは、ユーティリティの IEBPTPCH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、置換判定のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTYPORG オペランドを指定し、OSKB010084の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TYPORG オペランド
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TYPORG オペランド
    CASE OSKB010084
    SOURCE z/OS Utilities
    ```

    TYPORG オペランドとOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010084を同じ出力で読み、置換判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010084
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I TYPORG オペランド PROCESSING STARTED
    IEF142I OSKB010084 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の TYPORG オペランド と OSKB010084 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ユーティリティの基本機能 {#c40-i0194}
*分類: IEBPTPCH*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEBPTPCHで確認する項目です。データセット (順次 / PDS) を SYSPRINT に印刷したり、SYSPUNCH (カード形式) に出力したりする。フォーマット制御文で部分編集も可能

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)



## ユーティリティ > IEBUPDTE

### ./ ADD 制御文 {#c40-i0195}
*分類: IEBUPDTE*  ・  難易度: 中級

./ ADD 制御文は、ユーティリティのIEBUPDTEで確認する項目です。新規メンバーを追加する。NAME=memname / LIST=ALL 等のオペランドを取る。続く行群が新メンバーの本文となる

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ ADD 制御文**

    - 検証目的: 記録判定の・ 制御文について、./ ADD 制御文は、ユーティリティの IEBUPDTE で確認する項目です。新規メンバーを追加する。NAME=memname / LIST=ALL 等のオペランドを取る。続に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010093の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、記録判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ ADD 制御文を指定し、OSKB010093の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ ADD 制御文
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ ADD 制御文
    CASE OSKB010093
    SOURCE z/OS Utilities
    ```

    .・ ADD 制御文とOSKB010093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010093を同じ出力で読み、記録判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010093
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ ADD 制御文 PROCESSING STARTED
    IEF142I OSKB010093 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ ADD 制御文 と OSKB010093 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ./ CHANGE 制御文 {#c40-i0196}
*分類: IEBUPDTE*  ・  難易度: 中級

./ CHANGE 制御文は、ユーティリティのIEBUPDTEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ CHANGE 制御文**

    - 検証目的: 値域判定の・ 制御文について、./ CHANGE 制御文は、ユーティリティの IEBUPDTE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010096の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、値域判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ CHANGE 制御文を指定し、OSKB010096の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ CHANGE 制御文
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ CHANGE 制御文
    CASE OSKB010096
    SOURCE z/OS Utilities
    ```

    .・ CHANGE 制御文とOSKB010096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010096を同じ出力で読み、値域判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010096
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ CHANGE 制御文 PROCESSING STARTED
    IEF142I OSKB010096 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ CHANGE 制御文 と OSKB010096 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ./ DELETE 制御文 {#c40-i0197}
*分類: IEBUPDTE*  ・  難易度: 中級

./ DELETE 制御文は、ユーティリティのIEBUPDTEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ DELETE 制御文**

    - 検証目的: 順序判定の・ 制御文について、./ DELETE 制御文は、ユーティリティの IEBUPDTE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010095の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、順序判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ DELETE 制御文を指定し、OSKB010095の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ DELETE 制御文
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ DELETE 制御文
    CASE OSKB010095
    SOURCE z/OS Utilities
    ```

    .・ DELETE 制御文とOSKB010095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010095を同じ出力で読み、順序判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010095
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ DELETE 制御文 PROCESSING STARTED
    IEF142I OSKB010095 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ DELETE 制御文 と OSKB010095 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ./ ENDUP 制御文 {#c40-i0198}
*分類: IEBUPDTE*  ・  難易度: 中級

./ ENDUP 制御文は、ユーティリティのIEBUPDTEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ ENDUP 制御文**

    - 検証目的: 監査判定の・ 制御文について、./ ENDUP 制御文は、ユーティリティの IEBUPDTE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010099の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、監査判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ ENDUP 制御文を指定し、OSKB010099の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ ENDUP 制御文
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ ENDUP 制御文
    CASE OSKB010099
    SOURCE z/OS Utilities
    ```

    .・ ENDUP 制御文とOSKB010099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010099を同じ出力で読み、監査判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010099
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ ENDUP 制御文 PROCESSING STARTED
    IEF142I OSKB010099 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ ENDUP 制御文 と OSKB010099 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ./ LABEL 制御文 {#c40-i0199}
*分類: IEBUPDTE*  ・  難易度: 中級

./ LABEL 制御文は、ユーティリティのIEBUPDTEで確認する項目です。メンバー先頭にラベル情報 (SSI 等) を埋め込む。SMP/E が管理する一部の SYSMOD で利用される

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ LABEL 制御文**

    - 検証目的: 復旧判定の・ 制御文について、./ LABEL 制御文は、ユーティリティの IEBUPDTE で確認する項目です。メンバー先頭にラベル情報 (SSI 等) を埋め込む。SMP/E が管理する一部の SYSMに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010098の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、復旧判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ LABEL 制御文を指定し、OSKB010098の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ LABEL 制御文
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ LABEL 制御文
    CASE OSKB010098
    SOURCE z/OS Utilities
    ```

    .・ LABEL 制御文とOSKB010098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010098を同じ出力で読み、復旧判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010098
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ LABEL 制御文 PROCESSING STARTED
    IEF142I OSKB010098 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ LABEL 制御文 と OSKB010098 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ./ NUMBER 制御文 {#c40-i0200}
*分類: IEBUPDTE*  ・  難易度: 中級

./ NUMBER 制御文は、ユーティリティのIEBUPDTEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ NUMBER 制御文**

    - 検証目的: 警告判定の・ 制御文について、./ NUMBER 制御文は、ユーティリティの IEBUPDTE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010097の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、警告判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ NUMBER 制御文を指定し、OSKB010097の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ NUMBER 制御文
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ NUMBER 制御文
    CASE OSKB010097
    SOURCE z/OS Utilities
    ```

    .・ NUMBER 制御文とOSKB010097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010097を同じ出力で読み、警告判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010097
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ NUMBER 制御文 PROCESSING STARTED
    IEF142I OSKB010097 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ NUMBER 制御文 と OSKB010097 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ./ REPL 制御文 {#c40-i0201}
*分類: IEBUPDTE*  ・  難易度: 中級

./ REPL 制御文は、ユーティリティのIEBUPDTEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **.・ REPL 制御文**

    - 検証目的: 比較判定の・ 制御文について、./ REPL 制御文は、ユーティリティの IEBUPDTE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、比較判定の・ 制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に.・ REPL 制御文を指定し、OSKB010094の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND .・ REPL 制御文
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM .・ REPL 制御文
    CASE OSKB010094
    SOURCE z/OS Utilities
    ```

    .・ REPL 制御文とOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010094を同じ出力で読み、比較判定の・ 制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010094
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I .・ REPL 制御文 PROCESSING STARTED
    IEF142I OSKB010094 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の .・ REPL 制御文 と OSKB010094 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### PARM=NEW vs PARM=MOD {#c40-i0202}
*分類: IEBUPDTE*  ・  難易度: 中級

PARM=NEW vs PARM=MODは、ユーティリティのIEBUPDTEで構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **PARM=NEW vs PARM=MOD**

    - 検証目的: 構文整理のユーティリティについて、PARM=NEW vs PARM=MOD は、ユーティリティの IEBUPDTE で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010101の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、構文整理のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPARM=NEW vs PARM=Mを指定し、OSKB010101の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PARM=NEW vs PARM=M
    CASE OSKB010101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PARM=NEW vs PARM=M
    CASE OSKB010101
    SOURCE z/OS Utilities
    ```

    PARM=NEW vs PARM=MとOSKB010101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010101を同じ出力で読み、構文整理のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010101
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010101
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I PARM=NEW vs PARM=MOD PROCESSING STARTED
    IEF142I OSKB010101 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の PARM=NEW vs PARM=M と OSKB010101 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### シーケンス番号カラム (73-80) {#c40-i0203}
*分類: IEBUPDTE*  ・  難易度: 中級

シーケンス番号カラム (73-80)は、ユーティリティのIEBUPDTEで確認する項目です。IEBUPDTE は固定長 80 バイトレコードの 73-80 桁を行番号として扱う。CHANGE/DELETE はこの番号を基準に行を特定する

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **シーケンス番号カラム (73-80)**

    - 検証目的: 変更判定のシーケンス番号カラムについて、シーケンス番号カラム (73-80)は、ユーティリティの IEBUPDTE で確認する項目です。IEBUPDTE は固定長 80 バイトレコードの 73-80 桁を行番号としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010100の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、変更判定のシーケンス番号カラムの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にシーケンス番号カラム (73-80)を指定し、OSKB010100の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND シーケンス番号カラム (73-80)
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM シーケンス番号カラム (73-80)
    CASE OSKB010100
    SOURCE z/OS Utilities
    ```

    シーケンス番号カラム (73-80)とOSKB010100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010100を同じ出力で読み、変更判定のシーケンス番号カラムの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010100
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I シーケンス番号カラム (73-80) PROCESSING STARTED
    IEF142I OSKB010100 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の シーケンス番号カラム (73-80) と OSKB010100 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ユーティリティの基本機能 {#c40-i0204}
*分類: IEBUPDTE*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEBUPDTEで確認する項目です。PDS メンバーの追加・置換・行単位の編集を行う。SYSIN に「./」で始まる制御文と新規ソース行を混在させる伝統的形式

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### 代替制御文字 ./ {#c40-i0205}
*分類: IEBUPDTE*  ・  難易度: 中級

代替制御文字 ./は、ユーティリティのIEBUPDTEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **代替制御文字 .・**

    - 検証目的: 展開整理の代替制御文字 ・について、代替制御文字 ./は、ユーティリティの IEBUPDTE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010102の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開整理の代替制御文字 ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に代替制御文字 .・を指定し、OSKB010102の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 代替制御文字 .・
    CASE OSKB010102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 代替制御文字 .・
    CASE OSKB010102
    SOURCE z/OS Utilities
    ```

    代替制御文字 .・とOSKB010102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010102を同じ出力で読み、展開整理の代替制御文字 ・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010102
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010102
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I 代替制御文字 .・ PROCESSING STARTED
    IEF142I OSKB010102 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の 代替制御文字 .・ と OSKB010102 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)




## ユーティリティ > IEFBR14

### DISP=(NEW,CATLG) でのデータセット作成用途 {#c40-i0206}
*分類: IEFBR14*  ・  難易度: 中級

DISP=(NEW,CATLG) でのデータセット作成用途は、PGM=IEFBR14 と DD 文 (DISP=(NEW,CATLG,DELETE)) を組み合わせてデータセットを「割り当てるだけ」のジョブステップを書く典型用途

**出典:** z / OS MVS JCL User's Guide (z / OS 3.1)


### DISP=(OLD,DELETE) でのデータセット削除用途 {#c40-i0207}
*分類: IEFBR14*  ・  難易度: 中級

既存データセットを DD で指定し、ステップ終了時に DELETE してカタログから抹消する用途。SCRATCH/UNCATLG ユーティリティ無しでもデータセット削除が可能

**出典:** z / OS MVS JCL User's Guide (z / OS 3.1)


### PARM 指定は無視される {#c40-i0208}
*分類: IEFBR14*  ・  難易度: 中級

PARM= を書いても IEFBR14 は何も処理しないので無効。ダミーステップでパラメータを明示したい場合のみ書く慣習はある

**出典:** z / OS MVS JCL User's Guide (z / OS 3.1)


### プログラム本体の役割 {#c40-i0209}
*分類: IEFBR14*  ・  難易度: 中級

プログラム本体の役割は、ユーティリティのIEFBR14で機能名、見出し、または確認対象として参照する項目です。BR 14 (Branch Register 14, 復帰) 1 命令だけを実行して RC=0 で終了する最小のロードモジュール。プログラム自体は何もしないため、DD 文の割当て・解放だけが処理対象となる

**出典:** z / OS MVS JCL User's Guide (z / OS 3.1)


### 戻りコード (RC) は常に 0 {#c40-i0210}
*分類: IEFBR14*  ・  難易度: 中級

BR 14 だけを実行するため、IEFBR14 自身が異常 RC を返すことはない。ただし DD 割当て失敗 (JCL ERROR) や DISP 処理失敗時にはステップ自体が異常終了する

**出典:** z / OS MVS JCL User's Guide (z / OS 3.1)



## ユーティリティ > IEFUSI

### REGION 強制設定の用途 {#c40-i0211}
*分類: IEFUSI*  ・  難易度: 中級

REGION 強制設定の用途は、ユーティリティのIEFUSIで確認する項目です。ジョブ側で REGION=0M が指定されていてもインストール標準値で上書きするなど、管理者ポリシーを反映する典型用途

**出典:** z / OS MVS Installation Exits (z / OS 3.1)

??? note "検証手順（1件）"
    **REGION 強制設定の用途**

    - 検証目的: 展開照合の強制設定の用途について、REGION 強制設定の用途は、ユーティリティの IEFUSI で確認する項目です。ジョブ側で REGION=0M が指定されていてもインストール標準値で上書きするなど、管理者に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開照合の強制設定の用途の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にREGION 強制設定の用途を指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND REGION 強制設定の用途
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM REGION 強制設定の用途
    CASE OSKB020022
    SOURCE z/OS Utilities
    ```

    REGION 強制設定の用途とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020022を同じ出力で読み、展開照合の強制設定の用途の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020022
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I REGION 強制設定の用途 PROCESSING STARTED
    IEF142I OSKB020022 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の REGION 強制設定の用途 と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Installation Exits (z / OS 3.1)



### 出口ルーチンの概念 {#c40-i0212}
*分類: IEFUSI*  ・  難易度: 中級

出口ルーチンの概念は、ユーティリティのIEFUSIで確認する項目です。ジョブステップ起動時に呼び出されるシステム出口 (User Exit) で、ステップに REGION / MEMLIMIT / 出力制限などの動的制約を強制するためのフック点。ユーティリティではないが、運用設計で頻出するキーワード

**出典:** z / OS MVS Installation Exits (z / OS 3.1)

??? note "検証手順（1件）"
    **出口ルーチンの概念**

    - 検証目的: 構文照合の出口ルーチンの概念について、出口ルーチンの概念は、ユーティリティの IEFUSI で確認する項目です。ジョブステップ起動時に呼び出されるシステム出口 (User Exit) で、ステップに REGIONに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、構文照合の出口ルーチンの概念の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に出口ルーチンの概念を指定し、OSKB020021の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 出口ルーチンの概念
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 出口ルーチンの概念
    CASE OSKB020021
    SOURCE z/OS Utilities
    ```

    出口ルーチンの概念とOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020021を同じ出力で読み、構文照合の出口ルーチンの概念の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020021
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I 出口ルーチンの概念 PROCESSING STARTED
    IEF142I OSKB020021 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の 出口ルーチンの概念 と OSKB020021 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Installation Exits (z / OS 3.1)




## ユーティリティ > IEHATLAS

### ユーティリティの概念 {#c40-i0213}
*分類: IEHATLAS*  ・  難易度: 中級

ユーティリティの概念は、ユーティリティのIEHATLASで確認する項目です。不良トラックに対する代替トラック割当てを行う旧時代のユーティリティ。現代の z/OS では ICKDSF INSPECT に役割が引き継がれている

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（2件）"
    **ユーティリティの概念**

    - 検証目的: 変更確認のユーティリティの概念について、ユーティリティの概念は、ユーティリティの IEHATLAS で確認する項目です。不良トラックに対する代替トラック割当てを行う旧時代のユーティリティ。現代の z/OS では ICに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDASDを実行し、ICK00001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDASD を入力し、変更確認のユーティリティの概念の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDASD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDASD
    ```

    COMMAND INPUTにST OSKBDASDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの概念を指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの概念
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの概念
    CASE OSKB020020
    SOURCE z/OS Utilities
    ```

    ユーティリティの概念とOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICK00001IとOSKB020020を同じ出力で読み、変更確認のユーティリティの概念の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDASD
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020020
    //STEP1 EXEC PGM=OSKBDASD
    ICK00001I ユーティリティの概念 PROCESSING STARTED
    IEF142I OSKB020020 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICK00001IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDASD が画面・出力に表示されること
    ② ステップ2 の ユーティリティの概念 と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の ICK00001I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **ユーティリティの概念**

    - 検証目的: 呼出照合のユーティリティの概念について、ユーティリティの概念は、ユーティリティの IEHDASDR で確認する項目です。DASD ボリュームのフルダンプ・リストアを行うレガシーユーティリティ。現代では DFSMSdsに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、呼出照合のユーティリティの概念の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にユーティリティの概念を指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ユーティリティの概念
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ユーティリティの概念
    CASE OSKB020023
    SOURCE z/OS Utilities
    ```

    ユーティリティの概念とOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020023を同じ出力で読み、呼出照合のユーティリティの概念の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020023
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ユーティリティの概念 PROCESSING STARTED
    IEF142I OSKB020023 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ユーティリティの概念 と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)




## ユーティリティ > IEHDASDR

### ユーティリティの概念 {#c40-i0214}
*分類: IEHDASDR*  ・  難易度: 中級

ユーティリティの概念は、ユーティリティのIEHDASDRで確認する項目です。DASD ボリュームのフルダンプ・リストアを行うレガシーユーティリティ。現代では DFSMSdss DUMP/RESTORE に取って代わられた

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)



## ユーティリティ > IEHINITT

### INITT LABTYPE オペランド {#c40-i0215}
*分類: IEHINITT*  ・  難易度: 中級

INITT LABTYPE オペランドは、ユーティリティのIEHINITTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **INITT LABTYPE オペランド**

    - 検証目的: 記録確認のオペランドについて、INITT LABTYPE オペランドは、ユーティリティの IEHINITT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、記録確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にINITT LABTYPE オペランを指定し、OSKB020013の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND INITT LABTYPE オペラン
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM INITT LABTYPE オペラン
    CASE OSKB020013
    SOURCE z/OS Utilities
    ```

    INITT LABTYPE オペランとOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020013を同じ出力で読み、記録確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020013
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I INITT LABTYPE オペランド PROCESSING STARTED
    IEF142I OSKB020013 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の INITT LABTYPE オペラン と OSKB020013 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### INITT NUMBTAPE オペランド {#c40-i0216}
*分類: IEHINITT*  ・  難易度: 中級

INITT NUMBTAPE オペランドは、ユーティリティのIEHINITTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **INITT NUMBTAPE オペランド**

    - 検証目的: 順序確認のオペランドについて、INITT NUMBTAPE オペランドは、ユーティリティの IEHINITT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、順序確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にINITT NUMBTAPE オペラを指定し、OSKB020015の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND INITT NUMBTAPE オペラ
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM INITT NUMBTAPE オペラ
    CASE OSKB020015
    SOURCE z/OS Utilities
    ```

    INITT NUMBTAPE オペラとOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020015を同じ出力で読み、順序確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020015
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I INITT NUMBTAPE オペランド PROCESSING STARTED
    IEF142I OSKB020015 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の INITT NUMBTAPE オペラ と OSKB020015 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### INITT OWNER オペランド {#c40-i0217}
*分類: IEHINITT*  ・  難易度: 中級

INITT OWNER オペランドは、ユーティリティのIEHINITTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **INITT OWNER オペランド**

    - 検証目的: 比較確認のオペランドについて、INITT OWNER オペランドは、ユーティリティの IEHINITT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、比較確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にINITT OWNER オペランドを指定し、OSKB020014の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND INITT OWNER オペランド
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM INITT OWNER オペランド
    CASE OSKB020014
    SOURCE z/OS Utilities
    ```

    INITT OWNER オペランドとOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020014を同じ出力で読み、比較確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020014
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I INITT OWNER オペランド PROCESSING STARTED
    IEF142I OSKB020014 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の INITT OWNER オペランド と OSKB020014 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### INITT SER オペランド {#c40-i0218}
*分類: IEHINITT*  ・  難易度: 中級

INITT SER オペランドは、ユーティリティのIEHINITTで確認する項目です。新しい VOLSER (テープシリアル) を指定する。NUMBTAPE と組み合わせると指定数だけ連番で書ける

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **INITT SER オペランド**

    - 検証目的: 優先確認のオペランドについて、INITT SER オペランドは、ユーティリティの IEHINITT で確認する項目です。新しい VOLSER (テープシリアル) を指定する。NUMBTAPE と組み合わせるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、優先確認のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にINITT SER オペランドを指定し、OSKB020012の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND INITT SER オペランド
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM INITT SER オペランド
    CASE OSKB020012
    SOURCE z/OS Utilities
    ```

    INITT SER オペランドとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020012を同じ出力で読み、優先確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020012
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I INITT SER オペランド PROCESSING STARTED
    IEF142I OSKB020012 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の INITT SER オペランド と OSKB020012 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### INITT 制御文 {#c40-i0219}
*分類: IEHINITT*  ・  難易度: 中級

INITT 制御文は、ユーティリティのIEHINITTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **INITT 制御文**

    - 検証目的: 範囲確認の制御文について、INITT 制御文は、ユーティリティの IEHINITT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、範囲確認の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にINITT 制御文を指定し、OSKB020011の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND INITT 制御文
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM INITT 制御文
    CASE OSKB020011
    SOURCE z/OS Utilities
    ```

    INITT 制御文とOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020011を同じ出力で読み、範囲確認の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020011
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I INITT 制御文 PROCESSING STARTED
    IEF142I OSKB020011 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の INITT 制御文 と OSKB020011 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ユーティリティの基本機能 {#c40-i0220}
*分類: IEHINITT*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEHINITTで確認する項目です。テープボリュームを IBM 標準ラベルまたは ANSI ラベルで初期化する。複数巻のテープに連番でラベルを書く機能を持つ

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)



## ユーティリティ > IEHLIST

### LISTCTLG NODE オペランド {#c40-i0221}
*分類: IEHLIST*  ・  難易度: 中級

LISTCTLG NODE オペランドは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTCTLG NODE オペランド**

    - 検証目的: 呼出検査のオペランドについて、LISTCTLG NODE オペランドは、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、呼出検査のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTCTLG NODE オペランを指定し、OSKB010063の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTCTLG NODE オペラン
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTCTLG NODE オペラン
    CASE OSKB010063
    SOURCE z/OS Utilities
    ```

    LISTCTLG NODE オペランとOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010063を同じ出力で読み、呼出検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010063
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTCTLG NODE オペランド PROCESSING STARTED
    IEF142I OSKB010063 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTCTLG NODE オペラン と OSKB010063 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTCTLG 制御文 {#c40-i0222}
*分類: IEHLIST*  ・  難易度: 中級

LISTCTLG 制御文は、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTCTLG 制御文**

    - 検証目的: 展開検査の制御文について、LISTCTLG 制御文は、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開検査の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTCTLG 制御文を指定し、OSKB010062の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTCTLG 制御文
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTCTLG 制御文
    CASE OSKB010062
    SOURCE z/OS Utilities
    ```

    LISTCTLG 制御文とOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010062を同じ出力で読み、展開検査の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010062
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTCTLG 制御文 PROCESSING STARTED
    IEF142I OSKB010062 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTCTLG 制御文 と OSKB010062 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTPDS DUMP オペランド {#c40-i0223}
*分類: IEHLIST*  ・  難易度: 中級

LISTPDS DUMP オペランドは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTPDS DUMP オペランド**

    - 検証目的: 構文検査のオペランドについて、LISTPDS DUMP オペランドは、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、構文検査のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTPDS DUMP オペランドを指定し、OSKB010061の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTPDS DUMP オペランド
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTPDS DUMP オペランド
    CASE OSKB010061
    SOURCE z/OS Utilities
    ```

    LISTPDS DUMP オペランドとOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010061を同じ出力で読み、構文検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010061
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTPDS DUMP オペランド PROCESSING STARTED
    IEF142I OSKB010061 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTPDS DUMP オペランド と OSKB010061 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTPDS FORMAT オペランド {#c40-i0224}
*分類: IEHLIST*  ・  難易度: 中級

LISTPDS FORMAT オペランドは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTPDS FORMAT オペランド**

    - 検証目的: 変更追跡のオペランドについて、LISTPDS FORMAT オペランドは、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、変更追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTPDS FORMAT オペラを指定し、OSKB010060の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTPDS FORMAT オペラ
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTPDS FORMAT オペラ
    CASE OSKB010060
    SOURCE z/OS Utilities
    ```

    LISTPDS FORMAT オペラとOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010060を同じ出力で読み、変更追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010060
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTPDS FORMAT オペランド PROCESSING STARTED
    IEF142I OSKB010060 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTPDS FORMAT オペラ と OSKB010060 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTPDS 制御文 {#c40-i0225}
*分類: IEHLIST*  ・  難易度: 中級

LISTPDS 制御文は、ユーティリティのIEHLISTで確認する項目です。PDS のディレクトリエントリ (メンバー名、ISPF 統計、エイリアス) を出力する。DSNAME= で対象 PDS を指定する

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTPDS 制御文**

    - 検証目的: 監査追跡の制御文について、LISTPDS 制御文は、ユーティリティの IEHLIST で確認する項目です。PDS のディレクトリエントリ (メンバー名、ISPF 統計、エイリアス) を出力する。DSNAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、監査追跡の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTPDS 制御文を指定し、OSKB010059の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTPDS 制御文
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTPDS 制御文
    CASE OSKB010059
    SOURCE z/OS Utilities
    ```

    LISTPDS 制御文とOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010059を同じ出力で読み、監査追跡の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010059
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTPDS 制御文 PROCESSING STARTED
    IEF142I OSKB010059 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTPDS 制御文 と OSKB010059 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTVTOC DSNAME オペランド {#c40-i0226}
*分類: IEHLIST*  ・  難易度: 中級

LISTVTOC DSNAME オペランドは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTVTOC DSNAME オペランド**

    - 検証目的: 警告追跡のオペランドについて、LISTVTOC DSNAME オペランドは、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、警告追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTVTOC DSNAME オペを指定し、OSKB010057の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTVTOC DSNAME オペ
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTVTOC DSNAME オペ
    CASE OSKB010057
    SOURCE z/OS Utilities
    ```

    LISTVTOC DSNAME オペとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010057を同じ出力で読み、警告追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010057
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTVTOC DSNAME オペランド PROCESSING STARTED
    IEF142I OSKB010057 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTVTOC DSNAME オペ と OSKB010057 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTVTOC DUMP オペランド {#c40-i0227}
*分類: IEHLIST*  ・  難易度: 中級

LISTVTOC DUMP オペランドは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTVTOC DUMP オペランド**

    - 検証目的: 値域追跡のオペランドについて、LISTVTOC DUMP オペランドは、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、値域追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTVTOC DUMP オペランを指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTVTOC DUMP オペラン
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTVTOC DUMP オペラン
    CASE OSKB010056
    SOURCE z/OS Utilities
    ```

    LISTVTOC DUMP オペランとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010056を同じ出力で読み、値域追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010056
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTVTOC DUMP オペランド PROCESSING STARTED
    IEF142I OSKB010056 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTVTOC DUMP オペラン と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTVTOC FORMAT オペランド {#c40-i0228}
*分類: IEHLIST*  ・  難易度: 中級

LISTVTOC FORMAT オペランドは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTVTOC FORMAT オペランド**

    - 検証目的: 順序追跡のオペランドについて、LISTVTOC FORMAT オペランドは、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、順序追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTVTOC FORMAT オペを指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTVTOC FORMAT オペ
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTVTOC FORMAT オペ
    CASE OSKB010055
    SOURCE z/OS Utilities
    ```

    LISTVTOC FORMAT オペとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010055を同じ出力で読み、順序追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010055
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTVTOC FORMAT オペランド PROCESSING STARTED
    IEF142I OSKB010055 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTVTOC FORMAT オペ と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTVTOC VOL=オペランド {#c40-i0229}
*分類: IEHLIST*  ・  難易度: 中級

LISTVTOC VOL=オペランドは、ユーティリティのIEHLISTで確認する項目です。VOL=3390=VOLSER のように装置タイプとボリュームシリアル番号を指定する。対応する DD で物理ボリュームを明示する必要がある

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTVTOC VOL= オペランド**

    - 検証目的: 復旧追跡のオペランドについて、LISTVTOC VOL= オペランドは、ユーティリティの IEHLIST で確認する項目です。VOL=3390=VOLSER のように装置タイプとボリュームシリアル番号を指定すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、復旧追跡のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTVTOC VOL= オペランを指定し、OSKB010058の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTVTOC VOL= オペラン
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTVTOC VOL= オペラン
    CASE OSKB010058
    SOURCE z/OS Utilities
    ```

    LISTVTOC VOL= オペランとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010058を同じ出力で読み、復旧追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010058
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTVTOC VOL= オペランド PROCESSING STARTED
    IEF142I OSKB010058 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTVTOC VOL= オペラン と OSKB010058 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### LISTVTOC 制御文 {#c40-i0230}
*分類: IEHLIST*  ・  難易度: 中級

LISTVTOC 制御文は、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。指定ボリュームの VTOC 内容を一覧する。VOL=type=serial / DATE=date / FORMAT / DUMP 等のオペランドを取る

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **LISTVTOC 制御文**

    - 検証目的: 比較追跡の制御文について、LISTVTOC 制御文は、ユーティリティの IEHLIST で機能名、見出し、または確認対象として参照する項目です。指定ボリュームの VTOC 内容を一覧する。VOL=typに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、比較追跡の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLISTVTOC 制御文を指定し、OSKB010054の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LISTVTOC 制御文
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LISTVTOC 制御文
    CASE OSKB010054
    SOURCE z/OS Utilities
    ```

    LISTVTOC 制御文とOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010054を同じ出力で読み、比較追跡の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010054
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I LISTVTOC 制御文 PROCESSING STARTED
    IEF142I OSKB010054 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の LISTVTOC 制御文 と OSKB010054 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSIN DD {#c40-i0231}
*分類: IEHLIST*  ・  難易度: 中級

SYSIN DDは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### SYSPRINT DD {#c40-i0232}
*分類: IEHLIST*  ・  難易度: 中級

SYSPRINT DDは、ユーティリティのIEHLISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### ユーティリティの基本機能 {#c40-i0233}
*分類: IEHLIST*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEHLISTで確認する項目です。VTOC、カタログ、PDS ディレクトリの内容を SYSPRINT に出力する診断系ユーティリティ。LISTVTOC / LISTCTLG / LISTPDS の 3 機能を持つ

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)



## ユーティリティ > IEHMOVE

### COPY 制御文 {#c40-i0234}
*分類: IEHMOVE*  ・  難易度: 中級

COPY 制御文は、ユーティリティのIEHMOVEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)


### MOVE 制御文 {#c40-i0235}
*分類: IEHMOVE*  ・  難易度: 中級

MOVE 制御文は、ユーティリティのIEHMOVEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **MOVE 制御文**

    - 検証目的: 復旧確認の制御文について、MOVE 制御文は、ユーティリティの IEHMOVE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、復旧確認の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMOVE 制御文を指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MOVE 制御文
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MOVE 制御文
    CASE OSKB020018
    SOURCE z/OS Utilities
    ```

    MOVE 制御文とOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020018を同じ出力で読み、復旧確認の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020018
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I MOVE 制御文 PROCESSING STARTED
    IEF142I OSKB020018 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の MOVE 制御文 と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### TO / FROM オペランド {#c40-i0236}
*分類: IEHMOVE*  ・  難易度: 中級

TO / FROM オペランドは、ユーティリティのIEHMOVEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **TO ・ FROM オペランド**

    - 検証目的: 監査確認の・ オペランドについて、TO / FROM オペランドは、ユーティリティの IEHMOVE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、監査確認の・ オペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTO ・ FROM オペランドを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TO ・ FROM オペランド
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TO ・ FROM オペランド
    CASE OSKB020019
    SOURCE z/OS Utilities
    ```

    TO ・ FROM オペランドとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020019を同じ出力で読み、監査確認の・ オペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020019
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I TO ・ FROM オペランド PROCESSING STARTED
    IEF142I OSKB020019 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の TO ・ FROM オペランド と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ユーティリティの基本機能 {#c40-i0237}
*分類: IEHMOVE*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEHMOVEで確認する項目です。データセット (PS/PDS) やボリューム全体のコピー・移動を行う旧式ユーティリティ。現代では IDCAMS REPRO / IEBCOPY / DFSMSdss に置き換えられているが、レガシー JCL に残る

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)



## ユーティリティ > IEHPROGM

### BLDA 制御文 (Alias 作成) {#c40-i0238}
*分類: IEHPROGM*  ・  難易度: 中級

BLDA 制御文 (Alias 作成)は、ユーティリティのIEHPROGMで確認する項目です。ICF カタログ用のエイリアスを作成する。NAME= で別名、RELATE= で実体ノードを指定する。IDCAMS DEFINE ALIAS の前身

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **BLDA 制御文 (Alias 作成)**

    - 検証目的: 順序検査の制御文 作成について、BLDA 制御文 (Alias 作成)は、ユーティリティの IEHPROGM で確認する項目です。ICF カタログ用のエイリアスを作成する。NAME= で別名、RELATE=に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010075の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、順序検査の制御文 作成の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBLDA 制御文 (Alias 作成を指定し、OSKB010075の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BLDA 制御文 (Alias 作成
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BLDA 制御文 (Alias 作成
    CASE OSKB010075
    SOURCE z/OS Utilities
    ```

    BLDA 制御文 (Alias 作成とOSKB010075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010075を同じ出力で読み、順序検査の制御文 作成の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010075
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I BLDA 制御文 (Alias 作成) PROCESSING STARTED
    IEF142I OSKB010075 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の BLDA 制御文 (Alias 作成 と OSKB010075 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### BLDG 制御文 (GDG ベース作成) {#c40-i0239}
*分類: IEHPROGM*  ・  難易度: 中級

BLDG 制御文 (GDG ベース作成)は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。GDG ベースを定義する。INDEX= (ベース名)、ENTRIES= (世代数)、EMPTY/NOEMPTY、SCRATCH/NOSCRATCH 等のオプションを取る。IDCAMS DEFINE GDG の旧形式

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **BLDG 制御文 (GDG ベース作成)**

    - 検証目的: 比較検査の制御文 ベース作成について、BLDG 制御文 (GDG ベース作成)は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。GDG ベースを定義する。INDEX=に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010074の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、比較検査の制御文 ベース作成の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBLDG 制御文 (GDG ベース作を指定し、OSKB010074の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BLDG 制御文 (GDG ベース作
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BLDG 制御文 (GDG ベース作
    CASE OSKB010074
    SOURCE z/OS Utilities
    ```

    BLDG 制御文 (GDG ベース作とOSKB010074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010074を同じ出力で読み、比較検査の制御文 ベース作成の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010074
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I BLDG 制御文 (GDG ベース作成) PROCESSING STARTED
    IEF142I OSKB010074 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の BLDG 制御文 (GDG ベース作 と OSKB010074 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### BLDX 制御文 (インデックス作成) {#c40-i0240}
*分類: IEHPROGM*  ・  難易度: 中級

BLDX 制御文 (インデックス作成)は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **BLDX 制御文 (インデックス作成)**

    - 検証目的: 値域検査の制御文 インデックス作成について、BLDX 制御文 (インデックス作成)は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010076の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、値域検査の制御文 インデックス作成の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBLDX 制御文 (インデックス作成を指定し、OSKB010076の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BLDX 制御文 (インデックス作成
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BLDX 制御文 (インデックス作成
    CASE OSKB010076
    SOURCE z/OS Utilities
    ```

    BLDX 制御文 (インデックス作成とOSKB010076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010076を同じ出力で読み、値域検査の制御文 インデックス作成の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010076
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I BLDX 制御文 (インデックス作成) PROCESSING STARTED
    IEF142I OSKB010076 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の BLDX 制御文 (インデックス作成 と OSKB010076 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### CATLG 制御文 {#c40-i0241}
*分類: IEHPROGM*  ・  難易度: 中級

CATLG 制御文は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **CATLG 制御文**

    - 検証目的: 優先検査の制御文について、CATLG 制御文は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、優先検査の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCATLG 制御文を指定し、OSKB010072の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CATLG 制御文
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CATLG 制御文
    CASE OSKB010072
    SOURCE z/OS Utilities
    ```

    CATLG 制御文とOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010072を同じ出力で読み、優先検査の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010072
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I CATLG 制御文 PROCESSING STARTED
    IEF142I OSKB010072 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の CATLG 制御文 と OSKB010072 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### DLTA 制御文 (Alias 削除) {#c40-i0242}
*分類: IEHPROGM*  ・  難易度: 中級

DLTA 制御文 (Alias 削除)は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **DLTA 制御文 (Alias 削除)**

    - 検証目的: 警告検査の制御文 削除について、DLTA 制御文 (Alias 削除)は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010077の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、警告検査の制御文 削除の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDLTA 制御文 (Alias 削除を指定し、OSKB010077の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DLTA 制御文 (Alias 削除
    CASE OSKB010077
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DLTA 制御文 (Alias 削除
    CASE OSKB010077
    SOURCE z/OS Utilities
    ```

    DLTA 制御文 (Alias 削除とOSKB010077が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010077を同じ出力で読み、警告検査の制御文 削除の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010077
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010077
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I DLTA 制御文 (Alias 削除) PROCESSING STARTED
    IEF142I OSKB010077 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010077が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の DLTA 制御文 (Alias 削除 と OSKB010077 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### DLTX 制御文 (インデックス削除) {#c40-i0243}
*分類: IEHPROGM*  ・  難易度: 中級

DLTX 制御文 (インデックス削除)は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **DLTX 制御文 (インデックス削除)**

    - 検証目的: 復旧検査の制御文 インデックス削除について、DLTX 制御文 (インデックス削除)は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、復旧検査の制御文 インデックス削除の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDLTX 制御文 (インデックス削除を指定し、OSKB010078の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DLTX 制御文 (インデックス削除
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DLTX 制御文 (インデックス削除
    CASE OSKB010078
    SOURCE z/OS Utilities
    ```

    DLTX 制御文 (インデックス削除とOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010078を同じ出力で読み、復旧検査の制御文 インデックス削除の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010078
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I DLTX 制御文 (インデックス削除) PROCESSING STARTED
    IEF142I OSKB010078 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の DLTX 制御文 (インデックス削除 と OSKB010078 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RENAME MEMBER オペランド {#c40-i0244}
*分類: IEHPROGM*  ・  難易度: 中級

RENAME MEMBER オペランドは、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **RENAME MEMBER オペランド**

    - 検証目的: 範囲検査のオペランドについて、RENAME MEMBER オペランドは、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、範囲検査のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRENAME MEMBER オペランを指定し、OSKB010071の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RENAME MEMBER オペラン
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RENAME MEMBER オペラン
    CASE OSKB010071
    SOURCE z/OS Utilities
    ```

    RENAME MEMBER オペランとOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010071を同じ出力で読み、範囲検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010071
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RENAME MEMBER オペランド PROCESSING STARTED
    IEF142I OSKB010071 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RENAME MEMBER オペラン と OSKB010071 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### RENAME 制御文 {#c40-i0245}
*分類: IEHPROGM*  ・  難易度: 中級

RENAME 制御文は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **RENAME 制御文**

    - 検証目的: 区切検査の制御文について、RENAME 制御文は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、区切検査の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRENAME 制御文を指定し、OSKB010070の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RENAME 制御文
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RENAME 制御文
    CASE OSKB010070
    SOURCE z/OS Utilities
    ```

    RENAME 制御文とOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010070を同じ出力で読み、区切検査の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010070
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I RENAME 制御文 PROCESSING STARTED
    IEF142I OSKB010070 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の RENAME 制御文 と OSKB010070 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SCRATCH MEMBER オペランド {#c40-i0246}
*分類: IEHPROGM*  ・  難易度: 中級

SCRATCH MEMBER オペランドは、ユーティリティのIEHPROGMで確認する項目です。PDS メンバーだけを削除する場合に MEMBER=name を付ける。PDS 全体ではなくメンバー単位の削除になる

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SCRATCH MEMBER オペランド**

    - 検証目的: 条件検査のオペランドについて、SCRATCH MEMBER オペランドは、ユーティリティの IEHPROGM で確認する項目です。PDS メンバーだけを削除する場合に MEMBER=name を付ける。PDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、条件検査のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSCRATCH MEMBER オペラを指定し、OSKB010069の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SCRATCH MEMBER オペラ
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SCRATCH MEMBER オペラ
    CASE OSKB010069
    SOURCE z/OS Utilities
    ```

    SCRATCH MEMBER オペラとOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010069を同じ出力で読み、条件検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010069
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SCRATCH MEMBER オペランド PROCESSING STARTED
    IEF142I OSKB010069 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SCRATCH MEMBER オペラ と OSKB010069 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SCRATCH PURGE オペランド {#c40-i0247}
*分類: IEHPROGM*  ・  難易度: 中級

SCRATCH PURGE オペランドは、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SCRATCH PURGE オペランド**

    - 検証目的: 出力検査のオペランドについて、SCRATCH PURGE オペランドは、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、出力検査のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSCRATCH PURGE オペランを指定し、OSKB010068の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SCRATCH PURGE オペラン
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SCRATCH PURGE オペラン
    CASE OSKB010068
    SOURCE z/OS Utilities
    ```

    SCRATCH PURGE オペランとOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010068を同じ出力で読み、出力検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010068
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SCRATCH PURGE オペランド PROCESSING STARTED
    IEF142I OSKB010068 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SCRATCH PURGE オペラン と OSKB010068 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SCRATCH VOL オペランド {#c40-i0248}
*分類: IEHPROGM*  ・  難易度: 中級

SCRATCH VOL オペランドは、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SCRATCH VOL オペランド**

    - 検証目的: 上書検査のオペランドについて、SCRATCH VOL オペランドは、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、上書検査のオペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSCRATCH VOL オペランドを指定し、OSKB010067の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SCRATCH VOL オペランド
    CASE OSKB010067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SCRATCH VOL オペランド
    CASE OSKB010067
    SOURCE z/OS Utilities
    ```

    SCRATCH VOL オペランドとOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010067を同じ出力で読み、上書検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010067
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010067
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SCRATCH VOL オペランド PROCESSING STARTED
    IEF142I OSKB010067 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SCRATCH VOL オペランド と OSKB010067 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SCRATCH 制御文 {#c40-i0249}
*分類: IEHPROGM*  ・  難易度: 中級

SCRATCH 制御文は、ユーティリティのIEHPROGMで確認する項目です。データセットを物理的に削除する。DSNAME= で対象 DSN、VOL= で常駐ボリューム、PURGE で保護期間内でも削除を強制

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SCRATCH 制御文**

    - 検証目的: 探索検査の制御文について、SCRATCH 制御文は、ユーティリティの IEHPROGM で確認する項目です。データセットを物理的に削除する。DSNAME= で対象 DSN、VOL= で常駐ボリューム、Pに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、探索検査の制御文の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSCRATCH 制御文を指定し、OSKB010066の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SCRATCH 制御文
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SCRATCH 制御文
    CASE OSKB010066
    SOURCE z/OS Utilities
    ```

    SCRATCH 制御文とOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010066を同じ出力で読み、探索検査の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010066
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SCRATCH 制御文 PROCESSING STARTED
    IEF142I OSKB010066 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SCRATCH 制御文 と OSKB010066 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### SYSPRINT / SYSIN DD {#c40-i0250}
*分類: IEHPROGM*  ・  難易度: 中級

SYSPRINT / SYSIN DDは、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **SYSPRINT ・ SYSIN DD**

    - 検証目的: 終端検査の・について、SYSPRINT / SYSIN DD は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、終端検査の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBUTIL
    ```

    COMMAND INPUTにST OSKBUTILが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSPRINT ・ SYSIN Dを指定し、OSKB010065の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSPRINT ・ SYSIN D
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSPRINT ・ SYSIN D
    CASE OSKB010065
    SOURCE z/OS Utilities
    ```

    SYSPRINT ・ SYSIN DとOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010065を同じ出力で読み、終端検査の・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010065
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I SYSPRINT ・ SYSIN DD PROCESSING STARTED
    IEF142I OSKB010065 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の SYSPRINT ・ SYSIN D と OSKB010065 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)


