---
search:
  exclude: true
---

# RACF SETROPTS/RDEFINE/RACDCERT — 詳細 (4/6)

[← RACF SETROPTS/RDEFINE/RACDCERT の概要へ戻る](index.md)


## RACF SETROPTS/RDEFINE/RACDCERT > RALTER オペランド

### ADDCATEGORY/DELCATEGORY {#c26-i0219}
*分類: RALTER オペランド*  ・  難易度: 上級

ADDCATEGORY/DELCATEGORYは、RACF SETROPTS/RDEFINE/RACDCERTのRALTER オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として ADDCATEGORY/DELCATEGORY を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 構文照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。構文照合保守で扱う ADDCATEGORY/DELCATEGORY は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として ADDCATEGORY/DELCATEGORY を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **ADDCATEGORY ・ DELCATEGORY**

    - 検証目的: 出力整理の・について、ADDCATEGORY/DELCATEGORY は、RACF SETROPTS/RDEFINE/RACDCERT の RALTER オペランドで認証、権限、またはセキュリティ設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020108の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力整理の・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にADDCATEGORY ・ DELCを指定し、OSKB020108の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ADDCATEGORY ・ DELC
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ADDCATEGORY ・ DELC
    CASE OSKB020108
    SOURCE RACF
    ```

    ADDCATEGORY ・ DELCとOSKB020108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020108を同じ出力で読み、出力整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020108 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ADDCATEGORY ・ DELCATEGORY INFORMATION LISTED
    ```

    IRRD105IとOSKB020108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ADDCATEGORY ・ DELC と OSKB020108 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### ADDMEM/DELMEM {#c26-i0220}
*分類: RALTER オペランド*  ・  難易度: 上級

ADDMEM/DELMEMは、GROUP クラスのメンバを追加/削除。「ADDMEM/DELMEM」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ADDMEM ・ DELMEM**

    - 検証目的: 上書整理の・について、ADDMEM/DELMEM は、GROUP クラスのメンバを追加/削除。「ADDMEM/DELMEM」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書整理の・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にADDMEM ・ DELMEMを指定し、OSKB020107の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ADDMEM ・ DELMEM
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ADDMEM ・ DELMEM
    CASE OSKB020107
    SOURCE RACF
    ```

    ADDMEM ・ DELMEMとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020107を同じ出力で読み、上書整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020107 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ADDMEM ・ DELMEM INFORMATION LISTED
    ```

    IRRD105IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ADDMEM ・ DELMEM と OSKB020107 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### GLOBALAUDIT(level) {#c26-i0221}
*分類: RALTER オペランド*  ・  難易度: 上級

GLOBALAUDIT(level)は、RACF SETROPTS/RDEFINE/RACDCERTのRALTER オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 監査確認のオペランドでセキュリティ設定の運用確認を行います。GLOBALAUDIT(level)の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で監査確認のオペランドを確認した扱いにする。
    - B. IRRD105I の有無を確認せず監査確認のオペランドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査確認の根拠を固定する。 ✅
    - D. GLOBALAUDIT(level)の属性行を読まず監査確認のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認のオペランドにおいて選択記号 C を採用し、識別名は監査確認です。監査確認のオペランドにおいて GLOBALAUDIT(level) は説明欄の「RACF で GLOBALAUDIT(level)の扱いを記録する監査確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のオペランドを受け取る担当者は、GLOBALAUDIT(level)の表示結果と IRRD105I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のオペランドは別カテゴリの確認を流用しており、GLOBALAUDIT(level)の根拠にならないため監査確認ではありません。 B: 監査確認のオペランドは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため監査確認ではありません。 C: 監査確認のオペランドは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のオペランドが示す GLOBALAUDIT(level)は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **GLOBALAUDIT(level)**

    - 検証目的: 優先整理のオペランドについて、GLOBALAUDIT(level)は、RACF SETROPTS/RDEFINE/RACDCERT の RALTER オペランドで認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先整理のオペランドの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にGLOBALAUDIT(level)を指定し、OSKB020112の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND GLOBALAUDIT(level)
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM GLOBALAUDIT(level)
    CASE OSKB020112
    SOURCE RACF
    ```

    GLOBALAUDIT(level)とOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020112を同じ出力で読み、優先整理のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020112 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I GLOBALAUDIT(level) INFORMATION LISTED
    ```

    IRRD105IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の GLOBALAUDIT(level) と OSKB020112 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RALTER 共通属性変更 {#c26-i0222}
*分類: RALTER オペランド*  ・  難易度: 上級

RALTER 共通属性変更は、UACC/OWNER/AUDIT/NOTIFY/WARNING/LEVEL/DATA/APPLDATA を RDEFINE と同じ構文で変更可

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 記録確認の共通属性変更に関係する RALTER 共通属性変更の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、記録確認の採否を説明欄に結び付ける。 ✅
    - B. RALTER 共通属性変更の名称と担当者名のみを残して記録確認の共通属性変更の表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で記録確認の共通属性変更を確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず記録確認の共通属性変更の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認の共通属性変更において選択記号 A を採用し、識別名は記録確認です。記録確認の共通属性変更において RALTER 共通属性変更 は説明欄の「RALTER 共通属性変更の用途をセキュリティ設定の表示で確認する記録確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の共通属性変更に関連して、RACF では RALTER 共通属性変更の表示属性と IRRD105I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の共通属性変更は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の共通属性変更は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の共通属性変更は別カテゴリの確認を流用しており、RALTER 共通属性変更の根拠にならないため記録確認ではありません。 D: 記録確認の共通属性変更は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録確認ではありません。記録確認の共通属性変更で使う RALTER 共通属性変更という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RALTER 共通属性変更**

    - 検証目的: 探索整理の共通属性変更について、RALTER 共通属性変更は、UACC/OWNER/AUDIT/NOTIFY/WARNING/LEVEL/DATA/APPLDATA を RDEFINE と同じ構文で変更可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020106の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索整理の共通属性変更の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にRALTER 共通属性変更を指定し、OSKB020106の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RALTER 共通属性変更
    CASE OSKB020106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RALTER 共通属性変更
    CASE OSKB020106
    SOURCE RACF
    ```

    RALTER 共通属性変更とOSKB020106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020106を同じ出力で読み、探索整理の共通属性変更の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020106
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020106 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RALTER 共通属性変更 INFORMATION LISTED
    ```

    IRRD105IとOSKB020106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RALTER 共通属性変更 と OSKB020106 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLABEL(label)/NOSECLABEL {#c26-i0223}
*分類: RALTER オペランド*  ・  難易度: 上級

SECLABEL(label)/NOSECLABELは、SECLABEL 変更/削除。「SECLABEL(label)/NOSECLABEL」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 出力照合照合の出力照合として SECLABEL を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 出力照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解はAです。出力照合照合で扱う SECLABEL は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として SECLABEL を扱い、分類内の確認名として保存します（出力照合照合終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SECLABEL(label)・ NOSECLABEL**

    - 検証目的: 区切整理の・について、SECLABEL(label)/NOSECLABEL は、SECLABEL 変更/削除。「SECLABEL(label)/NOSECLABEL」を確認すると、SETROPTSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切整理の・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL(label)・ Nを指定し、OSKB020110の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLABEL(label)・ N
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLABEL(label)・ N
    CASE OSKB020110
    SOURCE RACF
    ```

    SECLABEL(label)・ NとOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020110を同じ出力で読み、区切整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020110 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLABEL(label)・ NOSECLAB INFORMATION LISTED
    ```

    IRRD105IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLABEL(label)・ N と OSKB020110 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLEVEL(name)/NOSECLEVEL {#c26-i0224}
*分類: RALTER オペランド*  ・  難易度: 上級

SECLEVEL(name)/NOSECLEVELは、RACF SETROPTS/RDEFINE/RACDCERTのRALTER オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として SECLEVEL を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 展開照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。展開照合権限で扱う SECLEVEL は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として SECLEVEL を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SECLEVEL(name)・ NOSECLEVEL**

    - 検証目的: 条件整理の・について、SECLEVEL(name)/NOSECLEVEL は、RACF SETROPTS/RDEFINE/RACDCERT の RALTER オペランドで認証、権限、またはセキュリティに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020109の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件整理の・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLEVEL(name)・ NOを指定し、OSKB020109の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLEVEL(name)・ NO
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLEVEL(name)・ NO
    CASE OSKB020109
    SOURCE RACF
    ```

    SECLEVEL(name)・ NOとOSKB020109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020109を同じ出力で読み、条件整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020109 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLEVEL(name)・ NOSECLEVE INFORMATION LISTED
    ```

    IRRD105IとOSKB020109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLEVEL(name)・ NO と OSKB020109 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### TIMEZONE/WHEN {#c26-i0225}
*分類: RALTER オペランド*  ・  難易度: 上級

TIMEZONE/WHENは、RACF SETROPTS/RDEFINE/RACDCERTのRALTER オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **TIMEZONE ・ WHEN**

    - 検証目的: 範囲整理の・について、TIMEZONE/WHEN は、RACF SETROPTS/RDEFINE/RACDCERT の RALTER オペランドで認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020111の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲整理の・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にTIMEZONE ・ WHENを指定し、OSKB020111の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND TIMEZONE ・ WHEN
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM TIMEZONE ・ WHEN
    CASE OSKB020111
    SOURCE RACF
    ```

    TIMEZONE ・ WHENとOSKB020111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020111を同じ出力で読み、範囲整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020111 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I TIMEZONE ・ WHEN INFORMATION LISTED
    ```

    IRRD105IとOSKB020111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の TIMEZONE ・ WHEN と OSKB020111 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RALTER 基本

### RALTER の目的 {#c26-i0226}
*分類: RALTER 基本*  ・  難易度: 上級

RALTER の目的は、RACF SETROPTS/RDEFINE/RACDCERTのRALTER 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 区切確認のの目的で RALTER の目的の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RALTER の目的の出力を取らず区切確認のの目的の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切確認の確認記録にまとめる。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して区切確認のの目的の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のの目的へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認のの目的において選択記号 B を採用し、識別名は区切確認です。区切確認のの目的において RALTER の目的 は説明欄の「区切確認のの目的に関係する定義値と表示行を照合する区切確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認のの目的の証跡を読む担当者は、RALTER の目的の属性行と IRRD105I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認のの目的は名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認のの目的は対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認のの目的は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため区切確認ではありません。 D: 区切確認のの目的は別カテゴリの確認を流用しており、RALTER の目的の根拠にならないため区切確認ではありません。区切確認のの目的に出る RALTER の目的は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RALTER の目的**

    - 検証目的: 呼出整理のの目的について、RALTER の目的は、RACF SETROPTS/RDEFINE/RACDCERT の RALTER 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020103の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出整理のの目的の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にRALTER の目的を指定し、OSKB020103の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RALTER の目的
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RALTER の目的
    CASE OSKB020103
    SOURCE RACF
    ```

    RALTER の目的とOSKB020103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020103を同じ出力で読み、呼出整理のの目的の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020103 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RALTER の目的 INFORMATION LISTED
    ```

    IRRD105IとOSKB020103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RALTER の目的 と OSKB020103 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RALTER 構文 {#c26-i0227}
*分類: RALTER 基本*  ・  難易度: 上級

RALTER 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRALTER 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 優先確認の構文に関する RALTER 構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先確認の構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の構文の証跡として保存して根拠にする。
    - C. RALTER 構文の変更点を出力本文から切り離して優先確認の構文の承認欄のみ残す。
    - D. 同じ画面で対象行と IRRD105I を読み、優先確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認の構文において選択記号 D を採用し、識別名は優先確認です。優先確認の構文において RALTER 構文 は説明欄の「RALTER 構文の状態と出力メッセージを結び付ける優先確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の構文に関する記録は、RALTER 構文の出力行と IRRD105I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の構文は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先確認ではありません。 B: 優先確認の構文は別カテゴリの確認を流用しており、RALTER 構文の根拠にならないため優先確認ではありません。 C: 優先確認の構文は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の構文は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の構文で記録する RALTER 構文は RACF の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RALTER 構文**

    - 検証目的: 終端整理の構文について、RALTER 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RALTER 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020105の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端整理の構文の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にRALTER 構文を指定し、OSKB020105の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RALTER 構文
    CASE OSKB020105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RALTER 構文
    CASE OSKB020105
    SOURCE RACF
    ```

    RALTER 構文とOSKB020105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020105を同じ出力で読み、終端整理の構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020105
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020105 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RALTER 構文 INFORMATION LISTED
    ```

    IRRD105IとOSKB020105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RALTER 構文 と OSKB020105 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RALTER 短縮形 {#c26-i0228}
*分類: RALTER 基本*  ・  難易度: 上級

RALTER 短縮形は、RALT と省略可。「RALTER 短縮形」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 範囲確認の短縮形でセキュリティ設定の運用確認を行います。RALTER 短縮形の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で範囲確認の短縮形を確認した扱いにする。
    - B. IRRD105I の有無を確認せず範囲確認の短縮形を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲確認の根拠にする。 ✅
    - D. RALTER 短縮形の属性行を読まず範囲確認の短縮形の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認の短縮形において選択記号 C を採用し、識別名は範囲確認です。範囲確認の短縮形において RALTER 短縮形 は説明欄の「RACF で RALTER 短縮形の扱いを記録する範囲確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認の短縮形を受け取る担当者は、RALTER 短縮形の表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認の短縮形は別カテゴリの確認を流用しており、RALTER 短縮形の根拠にならないため範囲確認ではありません。 B: 範囲確認の短縮形は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認の短縮形は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認の短縮形は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認の短縮形が示す RALTER 短縮形は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RALTER 短縮形**

    - 検証目的: 置換整理の短縮形について、RALTER 短縮形は、RALT と省略可。「RALTER 短縮形」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020104の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換整理の短縮形の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にRALTER 短縮形を指定し、OSKB020104の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RALTER 短縮形
    CASE OSKB020104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RALTER 短縮形
    CASE OSKB020104
    SOURCE RACF
    ```

    RALTER 短縮形とOSKB020104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020104を同じ出力で読み、置換整理の短縮形の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020104
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020104 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RALTER 短縮形 INFORMATION LISTED
    ```

    IRRD105IとOSKB020104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RALTER 短縮形 と OSKB020104 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE APPL

### APPL クラス {#c26-i0229}
*分類: RDEFINE APPL*  ・  難易度: 上級

APPL クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE APPLで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **APPL クラス**

    - 検証目的: 出力判定のクラスについて、APPL クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE APPL で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にAPPL クラスを指定し、OSKB020088の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND APPL クラス
    CASE OSKB020088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM APPL クラス
    CASE OSKB020088
    SOURCE RACF
    ```

    APPL クラスとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020088を同じ出力で読み、出力判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020088
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020088 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I APPL クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の APPL クラス と OSKB020088 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE CONSOLE

### CONSOLE クラス {#c26-i0230}
*分類: RDEFINE CONSOLE*  ・  難易度: 上級

CONSOLE クラスは、コンソール デバイスのアクセス制御。「CONSOLE クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **CONSOLE クラス**

    - 検証目的: 条件判定のクラスについて、CONSOLE クラスは、コンソール デバイスのアクセス制御。「CONSOLE クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020089の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にCONSOLE クラスを指定し、OSKB020089の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CONSOLE クラス
    CASE OSKB020089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CONSOLE クラス
    CASE OSKB020089
    SOURCE RACF
    ```

    CONSOLE クラスとOSKB020089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020089を同じ出力で読み、条件判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020089
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020089 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I CONSOLE クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の CONSOLE クラス と OSKB020089 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE CSFKEYS

### CSFKEYS クラス {#c26-i0231}
*分類: RDEFINE CSFKEYS*  ・  難易度: 上級

CSFKEYS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE CSFKEYSで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **CSFKEYS クラス**

    - 検証目的: 記録判定のクラスについて、CSFKEYS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE CSFKEYS で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020093の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にCSFKEYS クラスを指定し、OSKB020093の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CSFKEYS クラス
    CASE OSKB020093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CSFKEYS クラス
    CASE OSKB020093
    SOURCE RACF
    ```

    CSFKEYS クラスとOSKB020093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020093を同じ出力で読み、記録判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020093
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020093 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I CSFKEYS クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の CSFKEYS クラス と OSKB020093 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE CSFSERV

### CSFSERV クラス {#c26-i0232}
*分類: RDEFINE CSFSERV*  ・  難易度: 上級

CSFSERV クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE CSFSERVで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文確認のクラスに関係する CSFSERV クラスの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、構文確認の採否を説明欄に結び付ける。 ✅
    - B. CSFSERV クラスの名称と担当者名のみを残して構文確認のクラスの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で構文確認のクラスを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず構文確認のクラスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認のクラスにおいて選択記号 A を採用し、識別名は構文確認です。構文確認のクラスにおいて CSFSERV クラス は説明欄の「CSFSERV クラスの用途をセキュリティ設定の表示で確認する構文確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認のクラスに関連して、RACF では CSFSERV クラスの表示属性と IRRD105I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認のクラスは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認のクラスは別カテゴリの確認を流用しており、CSFSERV クラスの根拠にならないため構文確認ではありません。 D: 構文確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文確認ではありません。構文確認のクラスで使う CSFSERV クラスという用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **CSFSERV クラス**

    - 検証目的: 比較判定のクラスについて、CSFSERV クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE CSFSERV で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020094の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にCSFSERV クラスを指定し、OSKB020094の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CSFSERV クラス
    CASE OSKB020094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CSFSERV クラス
    CASE OSKB020094
    SOURCE RACF
    ```

    CSFSERV クラスとOSKB020094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020094を同じ出力で読み、比較判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020094
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020094 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I CSFSERV クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の CSFSERV クラス と OSKB020094 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE DIGTCERT

### DIGTCERT クラス {#c26-i0233}
*分類: RDEFINE DIGTCERT*  ・  難易度: 上級

DIGTCERT クラスは、デジタル証明書プロファイル (RACDCERT 管理)。「DIGTCERT クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開確認のクラスで DIGTCERT クラスの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DIGTCERT クラスの出力を取らず展開確認のクラスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開確認として引き継ぐ。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して展開確認のクラスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のクラスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認のクラスにおいて選択記号 B を採用し、識別名は展開確認です。展開確認のクラスにおいて DIGTCERT クラス は説明欄の「展開確認のクラスに関係する定義値と表示行を照合する展開確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認のクラスの証跡を読む担当者は、DIGTCERT クラスの属性行と IRRD105I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認のクラスは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開確認ではありません。 D: 展開確認のクラスは別カテゴリの確認を流用しており、DIGTCERT クラスの根拠にならないため展開確認ではありません。展開確認のクラスに出る DIGTCERT クラスは RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **DIGTCERT クラス**

    - 検証目的: 順序判定のクラスについて、DIGTCERT クラスは、デジタル証明書プロファイル (RACDCERT 管理)。「DIGTCERT クラス」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020095の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にDIGTCERT クラスを指定し、OSKB020095の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DIGTCERT クラス
    CASE OSKB020095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DIGTCERT クラス
    CASE OSKB020095
    SOURCE RACF
    ```

    DIGTCERT クラスとOSKB020095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020095を同じ出力で読み、順序判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020095
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020095 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DIGTCERT クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DIGTCERT クラス と OSKB020095 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE DIGTNMAP

### DIGTNMAP クラス {#c26-i0234}
*分類: RDEFINE DIGTNMAP*  ・  難易度: 上級

DIGTNMAP クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE DIGTNMAPで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 置換確認のクラスに関する DIGTNMAP クラスの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず置換確認のクラスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のクラスの証跡として保存して根拠にする。
    - C. DIGTNMAP クラスの変更点を出力本文から切り離して置換確認のクラスの承認欄のみ残す。
    - D. RACF の表示形式に沿って根拠行を採り、置換確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認のクラスにおいて選択記号 D を採用し、識別名は置換確認です。置換確認のクラスにおいて DIGTNMAP クラス は説明欄の「DIGTNMAP クラスの状態と出力メッセージを結び付ける置換確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認のクラスに関する記録は、DIGTNMAP クラスの出力行と IRRD105I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため置換確認ではありません。 B: 置換確認のクラスは別カテゴリの確認を流用しており、DIGTNMAP クラスの根拠にならないため置換確認ではありません。 C: 置換確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認のクラスは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認のクラスで記録する DIGTNMAP クラスは RACF の確認記録に残す対象名であり、用語名は置換確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **DIGTNMAP クラス**

    - 検証目的: 警告判定のクラスについて、DIGTNMAP クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE DIGTNMAP で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020097の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にDIGTNMAP クラスを指定し、OSKB020097の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DIGTNMAP クラス
    CASE OSKB020097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DIGTNMAP クラス
    CASE OSKB020097
    SOURCE RACF
    ```

    DIGTNMAP クラスとOSKB020097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020097を同じ出力で読み、警告判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020097
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020097 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DIGTNMAP クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DIGTNMAP クラス と OSKB020097 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE DIGTRING

### DIGTRING クラス {#c26-i0235}
*分類: RDEFINE DIGTRING*  ・  難易度: 上級

DIGTRING クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE DIGTRINGで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 呼出確認のクラスでセキュリティ設定の運用確認を行います。DIGTRING クラスの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で呼出確認のクラスを確認した扱いにする。
    - B. IRRD105I の有無を確認せず呼出確認のクラスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出確認の確認にする。 ✅
    - D. DIGTRING クラスの属性行を読まず呼出確認のクラスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認のクラスにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認のクラスにおいて DIGTRING クラス は説明欄の「RACF で DIGTRING クラスの扱いを記録する呼出確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認のクラスを受け取る担当者は、DIGTRING クラスの表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認のクラスは別カテゴリの確認を流用しており、DIGTRING クラスの根拠にならないため呼出確認ではありません。 B: 呼出確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認のクラスは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認のクラスが示す DIGTRING クラスは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **DIGTRING クラス**

    - 検証目的: 値域判定のクラスについて、DIGTRING クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE DIGTRING で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020096の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にDIGTRING クラスを指定し、OSKB020096の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DIGTRING クラス
    CASE OSKB020096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DIGTRING クラス
    CASE OSKB020096
    SOURCE RACF
    ```

    DIGTRING クラスとOSKB020096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020096を同じ出力で読み、値域判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020096
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020096 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DIGTRING クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DIGTRING クラス と OSKB020096 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE FACILITY

### BPX.* プロファイル {#c26-i0236}
*分類: RDEFINE FACILITY*  ・  難易度: 上級

BPX.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。BPX.* プロファイルは、z/OS UNIX 関連権限 (BPX.SUPERUSER 等)。「BPX.* プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **BPX.* プロファイル**

    - 検証目的: 復旧照合の* プロファイルについて、BPX.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧照合の* プロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にBPX.* プロファイルを指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND BPX.* プロファイル
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM BPX.* プロファイル
    CASE OSKB020038
    SOURCE RACF
    ```

    BPX.* プロファイルとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020038を同じ出力で読み、復旧照合の* プロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020038 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I BPX.* プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の BPX.* プロファイル と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### FACILITY クラスの用途 {#c26-i0237}
*分類: RDEFINE FACILITY*  ・  難易度: 上級

FACILITY クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **FACILITY クラスの用途**

    - 検証目的: 警告照合のクラスの用途について、FACILITY クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告照合のクラスの用途の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にFACILITY クラスの用途を指定し、OSKB020037の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND FACILITY クラスの用途
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM FACILITY クラスの用途
    CASE OSKB020037
    SOURCE RACF
    ```

    FACILITY クラスの用途とOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020037を同じ出力で読み、警告照合のクラスの用途の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020037 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I FACILITY クラスの用途 INFORMATION LISTED
    ```

    IRRD105IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の FACILITY クラスの用途 と OSKB020037 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRR.* プロファイル {#c26-i0238}
*分類: RDEFINE FACILITY*  ・  難易度: 上級

IRR.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **IRR.* プロファイル**

    - 検証目的: 監査照合の* プロファイルについて、IRR.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査照合の* プロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にIRR.* プロファイルを指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRR.* プロファイル
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRR.* プロファイル
    CASE OSKB020039
    SOURCE RACF
    ```

    IRR.* プロファイルとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020039を同じ出力で読み、監査照合の* プロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020039 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRR.* プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRR.* プロファイル と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STGADMIN.* プロファイル {#c26-i0239}
*分類: RDEFINE FACILITY*  ・  難易度: 上級

STGADMIN.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STGADMIN.* プロファイル**

    - 検証目的: 変更照合の* プロファイルについて、STGADMIN.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更照合の* プロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTGADMIN.* プロファイルを指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STGADMIN.* プロファイル
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STGADMIN.* プロファイル
    CASE OSKB020040
    SOURCE RACF
    ```

    STGADMIN.* プロファイルとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020040を同じ出力で読み、変更照合の* プロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020040 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STGADMIN.* プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STGADMIN.* プロファイル と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE JES

### JESINPUT クラス {#c26-i0240}
*分類: RDEFINE JES*  ・  難易度: 上級

JESINPUT クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **JESINPUT クラス**

    - 検証目的: 範囲追跡のクラスについて、JESINPUT クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲追跡のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にJESINPUT クラスを指定し、OSKB020051の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JESINPUT クラス
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JESINPUT クラス
    CASE OSKB020051
    SOURCE RACF
    ```

    JESINPUT クラスとOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020051を同じ出力で読み、範囲追跡のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020051 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JESINPUT クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JESINPUT クラス と OSKB020051 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### JESJOBS CANCEL.nodeid.userid.jobname {#c26-i0241}
*分類: RDEFINE JES*  ・  難易度: 上級

JESJOBS CANCEL.nodeid.userid.jobnameは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### JESJOBS SUBMIT.nodeid.jobname.owner {#c26-i0242}
*分類: RDEFINE JES*  ・  難易度: 上級

JESJOBS SUBMIT.nodeid.jobname.ownerは、ジョブ サブミット権限プロファイル。「JESJOBS SUBMIT.nodeid.jobname.owner」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### JESJOBS クラス {#c26-i0243}
*分類: RDEFINE JES*  ・  難易度: 上級

JESJOBS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **JESJOBS クラス**

    - 検証目的: 優先追跡のクラスについて、JESJOBS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先追跡のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にJESJOBS クラスを指定し、OSKB020052の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JESJOBS クラス
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JESJOBS クラス
    CASE OSKB020052
    SOURCE RACF
    ```

    JESJOBS クラスとOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020052を同じ出力で読み、優先追跡のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020052 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JESJOBS クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JESJOBS クラス と OSKB020052 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### JESSPOOL クラス {#c26-i0244}
*分類: RDEFINE JES*  ・  難易度: 上級

JESSPOOL クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **JESSPOOL クラス**

    - 検証目的: 順序追跡のクラスについて、JESSPOOL クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序追跡のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にJESSPOOL クラスを指定し、OSKB020055の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JESSPOOL クラス
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JESSPOOL クラス
    CASE OSKB020055
    SOURCE RACF
    ```

    JESSPOOL クラスとOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020055を同じ出力で読み、順序追跡のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020055 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JESSPOOL クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JESSPOOL クラス と OSKB020055 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### JESSPOOL プロファイル形式 {#c26-i0245}
*分類: RDEFINE JES*  ・  難易度: 上級

JESSPOOL プロファイル形式は、nodeid.userid.jobname.jobid.dsid.dsname。「JESSPOOL プロファイル形式」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **JESSPOOL プロファイル形式**

    - 検証目的: 値域追跡のプロファイル形式について、JESSPOOL プロファイル形式は、nodeid.userid.jobname.jobid.dsid.dsname。「JESSPOOL プロファイル形式」を確認すると、Sに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域追跡のプロファイル形式の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にJESSPOOL プロファイル形式を指定し、OSKB020056の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JESSPOOL プロファイル形式
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JESSPOOL プロファイル形式
    CASE OSKB020056
    SOURCE RACF
    ```

    JESSPOOL プロファイル形式とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020056を同じ出力で読み、値域追跡のプロファイル形式の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020056 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JESSPOOL プロファイル形式 INFORMATION LISTED
    ```

    IRRD105IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JESSPOOL プロファイル形式 と OSKB020056 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### NODES クラス {#c26-i0246}
*分類: RDEFINE JES*  ・  難易度: 上級

NODES クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **NODES クラス**

    - 検証目的: 復旧追跡のクラスについて、NODES クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧追跡のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にNODES クラスを指定し、OSKB020058の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND NODES クラス
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM NODES クラス
    CASE OSKB020058
    SOURCE RACF
    ```

    NODES クラスとOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020058を同じ出力で読み、復旧追跡のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020058 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I NODES クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の NODES クラス と OSKB020058 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### WRITER クラス {#c26-i0247}
*分類: RDEFINE JES*  ・  難易度: 上級

WRITER クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **WRITER クラス**

    - 検証目的: 警告追跡のクラスについて、WRITER クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告追跡のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にWRITER クラスを指定し、OSKB020057の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WRITER クラス
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WRITER クラス
    CASE OSKB020057
    SOURCE RACF
    ```

    WRITER クラスとOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020057を同じ出力で読み、警告追跡のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020057 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I WRITER クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の WRITER クラス と OSKB020057 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE OPERCMDS

### JES2.* プロファイル {#c26-i0248}
*分類: RDEFINE OPERCMDS*  ・  難易度: 上級

JES2.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。JES2.* プロファイルは、JES2 コマンド。「JES2.* プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **JES2.* プロファイル**

    - 検証目的: 展開検査の* プロファイルについて、JES2.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開検査の* プロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にJES2.* プロファイルを指定し、OSKB020062の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JES2.* プロファイル
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JES2.* プロファイル
    CASE OSKB020062
    SOURCE RACF
    ```

    JES2.* プロファイルとOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020062を同じ出力で読み、展開検査の* プロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020062 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JES2.* プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JES2.* プロファイル と OSKB020062 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### JES3.* プロファイル {#c26-i0249}
*分類: RDEFINE OPERCMDS*  ・  難易度: 上級

JES3.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **JES3.* プロファイル**

    - 検証目的: 呼出検査の* プロファイルについて、JES3.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出検査の* プロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にJES3.* プロファイルを指定し、OSKB020063の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JES3.* プロファイル
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JES3.* プロファイル
    CASE OSKB020063
    SOURCE RACF
    ```

    JES3.* プロファイルとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020063を同じ出力で読み、呼出検査の* プロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020063 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JES3.* プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JES3.* プロファイル と OSKB020063 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### MVS.* プロファイル {#c26-i0250}
*分類: RDEFINE OPERCMDS*  ・  難易度: 上級

MVS.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **MVS.* プロファイル**

    - 検証目的: 構文検査の* プロファイルについて、MVS.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文検査の* プロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にMVS.* プロファイルを指定し、OSKB020061の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND MVS.* プロファイル
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM MVS.* プロファイル
    CASE OSKB020061
    SOURCE RACF
    ```

    MVS.* プロファイルとOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020061を同じ出力で読み、構文検査の* プロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020061 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I MVS.* プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の MVS.* プロファイル と OSKB020061 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### OPERCMDS クラス {#c26-i0251}
*分類: RDEFINE OPERCMDS*  ・  難易度: 上級

OPERCMDS クラスは、コンソール オペレータ コマンドのアクセス制御。「OPERCMDS クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **OPERCMDS クラス**

    - 検証目的: 監査追跡のクラスについて、OPERCMDS クラスは、コンソール オペレータ コマンドのアクセス制御。「OPERCMDS クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査追跡のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にOPERCMDS クラスを指定し、OSKB020059の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND OPERCMDS クラス
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM OPERCMDS クラス
    CASE OSKB020059
    SOURCE RACF
    ```

    OPERCMDS クラスとOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020059を同じ出力で読み、監査追跡のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020059 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I OPERCMDS クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の OPERCMDS クラス と OSKB020059 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### プロファイル形式 {#c26-i0252}
*分類: RDEFINE OPERCMDS*  ・  難易度: 上級

プロファイル形式は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **プロファイル形式**

    - 検証目的: 変更追跡のプロファイル形式について、プロファイル形式は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目です。実行対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更追跡のプロファイル形式の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にプロファイル形式を指定し、OSKB020060の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND プロファイル形式
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM プロファイル形式
    CASE OSKB020060
    SOURCE RACF
    ```

    プロファイル形式とOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020060を同じ出力で読み、変更追跡のプロファイル形式の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020060 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I プロファイル形式 INFORMATION LISTED
    ```

    IRRD105IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の プロファイル形式 と OSKB020060 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE PROGRAM

### ADDMEM(library/volser/PADCHK) {#c26-i0253}
*分類: RDEFINE PROGRAM*  ・  難易度: 上級

ADDMEM(library/volser/PADCHK)は、対象ライブラリ・ボリューム・PADS チェック有無。「ADDMEM(library/volser/PADCHK)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ADDMEM(library・volser・ PADCHK)**

    - 検証目的: 終端検査の・ ・について、ADDMEM(library/volser/PADCHK)は、対象ライブラリ・ボリューム・ PADS チェック有無。「ADDMEM(library/volser/PADCHKに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端検査の・ ・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にADDMEM(library・volを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ADDMEM(library・vol
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ADDMEM(library・vol
    CASE OSKB020065
    SOURCE RACF
    ```

    ADDMEM(library・volとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020065を同じ出力で読み、終端検査の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020065 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ADDMEM(library・volser・ PA INFORMATION LISTED
    ```

    IRRD105IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ADDMEM(library・vol と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### PADCHK/NOPADCHK {#c26-i0254}
*分類: RDEFINE PROGRAM*  ・  難易度: 上級

PADCHK/NOPADCHKは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE PROGRAMで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **PADCHK ・ NOPADCHK**

    - 検証目的: 探索検査の・について、PADCHK/NOPADCHK は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE PROGRAM で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索検査の・の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にPADCHK ・ NOPADCHKを指定し、OSKB020066の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND PADCHK ・ NOPADCHK
    CASE OSKB020066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM PADCHK ・ NOPADCHK
    CASE OSKB020066
    SOURCE RACF
    ```

    PADCHK ・ NOPADCHKとOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020066を同じ出力で読み、探索検査の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020066
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020066 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I PADCHK ・ NOPADCHK INFORMATION LISTED
    ```

    IRRD105IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の PADCHK ・ NOPADCHK と OSKB020066 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### PROGRAM クラス {#c26-i0255}
*分類: RDEFINE PROGRAM*  ・  難易度: 上級

PROGRAM クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE PROGRAMで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **PROGRAM クラス**

    - 検証目的: 置換検査のクラスについて、PROGRAM クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE PROGRAM で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にPROGRAM クラスを指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND PROGRAM クラス
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM PROGRAM クラス
    CASE OSKB020064
    SOURCE RACF
    ```

    PROGRAM クラスとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020064を同じ出力で読み、置換検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020064 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I PROGRAM クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の PROGRAM クラス と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### WHEN(PROGRAM) 連携 {#c26-i0256}
*分類: RDEFINE PROGRAM*  ・  難易度: 上級

WHEN(PROGRAM) 連携は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE PROGRAMで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **WHEN(PROGRAM) 連携**

    - 検証目的: 上書検査の連携について、WHEN(PROGRAM) 連携は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE PROGRAM で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書検査の連携の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(PROGRAM) 連携を指定し、OSKB020067の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WHEN(PROGRAM) 連携
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WHEN(PROGRAM) 連携
    CASE OSKB020067
    SOURCE RACF
    ```

    WHEN(PROGRAM) 連携とOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020067を同じ出力で読み、上書検査の連携の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020067 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I WHEN(PROGRAM) 連携 INFORMATION LISTED
    ```

    IRRD105IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の WHEN(PROGRAM) 連携 と OSKB020067 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE SDSF

### ISFAUTH プロファイル {#c26-i0257}
*分類: RDEFINE SDSF*  ・  難易度: 上級

ISFAUTH プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SDSFで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ISFAUTH プロファイル**

    - 検証目的: 区切検査のプロファイルについて、ISFAUTH プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SDSF で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切検査のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にISFAUTH プロファイルを指定し、OSKB020070の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ISFAUTH プロファイル
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ISFAUTH プロファイル
    CASE OSKB020070
    SOURCE RACF
    ```

    ISFAUTH プロファイルとOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020070を同じ出力で読み、区切検査のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020070 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ISFAUTH プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ISFAUTH プロファイル と OSKB020070 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### ISFCMD プロファイル {#c26-i0258}
*分類: RDEFINE SDSF*  ・  難易度: 上級

ISFCMD プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SDSFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ISFCMD プロファイル**

    - 検証目的: 条件検査のプロファイルについて、ISFCMD プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SDSF で状態表示や操作を行うためのコマンド関連項目です。実行対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件検査のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にISFCMD プロファイルを指定し、OSKB020069の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ISFCMD プロファイル
    CASE OSKB020069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ISFCMD プロファイル
    CASE OSKB020069
    SOURCE RACF
    ```

    ISFCMD プロファイルとOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020069を同じ出力で読み、条件検査のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020069
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020069 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ISFCMD プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ISFCMD プロファイル と OSKB020069 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### ISFOPER プロファイル {#c26-i0259}
*分類: RDEFINE SDSF*  ・  難易度: 上級

ISFOPER プロファイルは、オペレータ コマンド権限。「ISFOPER プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ISFOPER プロファイル**

    - 検証目的: 範囲検査のプロファイルについて、ISFOPER プロファイルは、オペレータ コマンド権限。「ISFOPER プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020071の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲検査のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にISFOPER プロファイルを指定し、OSKB020071の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ISFOPER プロファイル
    CASE OSKB020071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ISFOPER プロファイル
    CASE OSKB020071
    SOURCE RACF
    ```

    ISFOPER プロファイルとOSKB020071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020071を同じ出力で読み、範囲検査のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020071
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020071 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ISFOPER プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ISFOPER プロファイル と OSKB020071 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SDSF クラス {#c26-i0260}
*分類: RDEFINE SDSF*  ・  難易度: 上級

SDSF クラスは、SDSF パネル/コマンド/カラムのアクセス制御。「SDSF クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SDSF クラス**

    - 検証目的: 出力検査のクラスについて、SDSF クラスは、SDSF パネル/コマンド/カラムのアクセス制御。「SDSF クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSDSF クラスを指定し、OSKB020068の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SDSF クラス
    CASE OSKB020068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SDSF クラス
    CASE OSKB020068
    SOURCE RACF
    ```

    SDSF クラスとOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020068を同じ出力で読み、出力検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020068
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020068 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SDSF クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SDSF クラス と OSKB020068 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE SECDATA

### CATEGORY プロファイル {#c26-i0261}
*分類: RDEFINE SECDATA*  ・  難易度: 上級

CATEGORY プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SECDATAで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **CATEGORY プロファイル**

    - 検証目的: 終端判定のプロファイルについて、CATEGORY プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SECDATA で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020085の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端判定のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にCATEGORY プロファイルを指定し、OSKB020085の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CATEGORY プロファイル
    CASE OSKB020085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CATEGORY プロファイル
    CASE OSKB020085
    SOURCE RACF
    ```

    CATEGORY プロファイルとOSKB020085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020085を同じ出力で読み、終端判定のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020085
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020085 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I CATEGORY プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の CATEGORY プロファイル と OSKB020085 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECDATA クラス {#c26-i0262}
*分類: RDEFINE SECDATA*  ・  難易度: 上級

SECDATA クラスは、SECLEVEL/CATEGORY 定義用。「SECDATA クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECDATA クラス**

    - 検証目的: 呼出判定のクラスについて、SECDATA クラスは、SECLEVEL/CATEGORY 定義用。「SECDATA クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020083の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSECDATA クラスを指定し、OSKB020083の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECDATA クラス
    CASE OSKB020083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECDATA クラス
    CASE OSKB020083
    SOURCE RACF
    ```

    SECDATA クラスとOSKB020083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020083を同じ出力で読み、呼出判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020083
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020083 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECDATA クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECDATA クラス と OSKB020083 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLEVEL プロファイル {#c26-i0263}
*分類: RDEFINE SECDATA*  ・  難易度: 上級

SECLEVEL プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SECDATAで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLEVEL プロファイル**

    - 検証目的: 置換判定のプロファイルについて、SECLEVEL プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SECDATA で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020084の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換判定のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLEVEL プロファイルを指定し、OSKB020084の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLEVEL プロファイル
    CASE OSKB020084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLEVEL プロファイル
    CASE OSKB020084
    SOURCE RACF
    ```

    SECLEVEL プロファイルとOSKB020084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020084を同じ出力で読み、置換判定のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020084
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020084 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLEVEL プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLEVEL プロファイル と OSKB020084 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE SECLABEL

### SECLABEL クラス {#c26-i0264}
*分類: RDEFINE SECLABEL*  ・  難易度: 上級

SECLABEL クラスは、MLS 環境のセキュリティ ラベル。「SECLABEL クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLABEL クラス**

    - 検証目的: 探索判定のクラスについて、SECLABEL クラスは、MLS 環境のセキュリティ ラベル。「SECLABEL クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL クラスを指定し、OSKB020086の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLABEL クラス
    CASE OSKB020086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLABEL クラス
    CASE OSKB020086
    SOURCE RACF
    ```

    SECLABEL クラスとOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020086を同じ出力で読み、探索判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020086
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020086 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLABEL クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLABEL クラス と OSKB020086 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SECLABEL システムラベル {#c26-i0265}
*分類: RDEFINE SECLABEL*  ・  難易度: 上級

SECLABEL システムラベルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SECLABEL システムラベル**

    - 検証目的: 上書判定のシステムラベルについて、SECLABEL システムラベルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SECLABEL で認証、権限、またはセキュリティ設定を確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020087の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書判定のシステムラベルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL システムラベルを指定し、OSKB020087の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SECLABEL システムラベル
    CASE OSKB020087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SECLABEL システムラベル
    CASE OSKB020087
    SOURCE RACF
    ```

    SECLABEL システムラベルとOSKB020087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020087を同じ出力で読み、上書判定のシステムラベルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020087
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020087 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SECLABEL システムラベル INFORMATION LISTED
    ```

    IRRD105IとOSKB020087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SECLABEL システムラベル と OSKB020087 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE SERVAUTH

### EZB.PORTACCESS {#c26-i0266}
*分類: RDEFINE SERVAUTH*  ・  難易度: 上級

EZB.PORTACCESSは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SERVAUTHで認証、権限、またはセキュリティ設定を確認する項目です。EZB.PORTACCESSは、予約ポート使用権。「EZB.PORTACCESS」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **EZB.PORTACCESS**

    - 検証目的: 優先判定のセキュリティ設定について、EZB.PORTACCESS は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SERVAUTH で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020092の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先判定のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にEZB.PORTACCESSを指定し、OSKB020092の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND EZB.PORTACCESS
    CASE OSKB020092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM EZB.PORTACCESS
    CASE OSKB020092
    SOURCE RACF
    ```

    EZB.PORTACCESSとOSKB020092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020092を同じ出力で読み、優先判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020092
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020092 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I EZB.PORTACCESS INFORMATION LISTED
    ```

    IRRD105IとOSKB020092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の EZB.PORTACCESS と OSKB020092 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### EZB.STACKACCESS {#c26-i0267}
*分類: RDEFINE SERVAUTH*  ・  難易度: 上級

EZB.STACKACCESSは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SERVAUTHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **EZB.STACKACCESS**

    - 検証目的: 範囲判定のセキュリティ設定について、EZB.STACKACCESS は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SERVAUTH で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020091の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲判定のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にEZB.STACKACCESSを指定し、OSKB020091の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND EZB.STACKACCESS
    CASE OSKB020091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM EZB.STACKACCESS
    CASE OSKB020091
    SOURCE RACF
    ```

    EZB.STACKACCESSとOSKB020091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020091を同じ出力で読み、範囲判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020091
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020091 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I EZB.STACKACCESS INFORMATION LISTED
    ```

    IRRD105IとOSKB020091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の EZB.STACKACCESS と OSKB020091 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SERVAUTH クラス {#c26-i0268}
*分類: RDEFINE SERVAUTH*  ・  難易度: 上級

SERVAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SERVAUTHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SERVAUTH クラス**

    - 検証目的: 区切判定のクラスについて、SERVAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SERVAUTH で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSERVAUTH クラスを指定し、OSKB020090の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SERVAUTH クラス
    CASE OSKB020090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SERVAUTH クラス
    CASE OSKB020090
    SOURCE RACF
    ```

    SERVAUTH クラスとOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020090を同じ出力で読み、区切判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020090
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020090 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SERVAUTH クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SERVAUTH クラス と OSKB020090 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE STARTED

### STARTED と ICHRIN03 の関係 {#c26-i0269}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STARTED クラスは ICHRIN03 テーブルの動的版。「STARTED と ICHRIN03 の関係」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STARTED と ICHRIN03 の関係**

    - 検証目的: 上書追跡のと の関係について、STARTED クラスは ICHRIN03 テーブルの動的版。「STARTED と ICHRIN03 の関係」を確認すると、SETROPTS、RDEFINE、RACDCERに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書追跡のと の関係の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTARTED と ICHRIN03を指定し、OSKB020047の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STARTED と ICHRIN03
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STARTED と ICHRIN03
    CASE OSKB020047
    SOURCE RACF
    ```

    STARTED と ICHRIN03とOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020047を同じ出力で読み、上書追跡のと の関係の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020047 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STARTED と ICHRIN03 の関係 INFORMATION LISTED
    ```

    IRRD105IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STARTED と ICHRIN03 と OSKB020047 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STARTED クラスの用途 {#c26-i0270}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STARTED クラスの用途は、STC (Started Task) にユーザ/グループ ID を割当。「STARTED クラスの用途」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STARTED クラスの用途**

    - 検証目的: 構文追跡のクラスの用途について、STARTED クラスの用途は、STC (Started Task) にユーザ/グループ ID を割当。「STARTED クラスの用途」を確認すると、SETROPTS、RDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文追跡のクラスの用途の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTARTED クラスの用途を指定し、OSKB020041の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STARTED クラスの用途
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STARTED クラスの用途
    CASE OSKB020041
    SOURCE RACF
    ```

    STARTED クラスの用途とOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020041を同じ出力で読み、構文追跡のクラスの用途の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020041 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STARTED クラスの用途 INFORMATION LISTED
    ```

    IRRD105IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STARTED クラスの用途 と OSKB020041 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STDATA セグメント {#c26-i0271}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STDATA セグメントは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STDATA セグメント**

    - 検証目的: 展開追跡のセグメントについて、STDATA セグメントは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開追跡のセグメントの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA セグメントを指定し、OSKB020042の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STDATA セグメント
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STDATA セグメント
    CASE OSKB020042
    SOURCE RACF
    ```

    STDATA セグメントとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020042を同じ出力で読み、展開追跡のセグメントの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020042 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STDATA セグメント INFORMATION LISTED
    ```

    IRRD105IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STDATA セグメント と OSKB020042 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STDATA(GROUP(id)) {#c26-i0272}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STDATA(GROUP(id))は、STC グループ ID。「STDATA(GROUP(id))」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STDATA(GROUP(id))**

    - 検証目的: 置換追跡のセキュリティ設定について、STDATA(GROUP(id))は、STC グループ ID。「STDATA(GROUP(id))」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換追跡のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(GROUP(id))を指定し、OSKB020044の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STDATA(GROUP(id))
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STDATA(GROUP(id))
    CASE OSKB020044
    SOURCE RACF
    ```

    STDATA(GROUP(id))とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020044を同じ出力で読み、置換追跡のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020044 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STDATA(GROUP(id)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STDATA(GROUP(id)) と OSKB020044 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STDATA(PRIVILEGED(YES)) {#c26-i0273}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STDATA(PRIVILEGED(YES))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STDATA(PRIVILEGED(YES))**

    - 検証目的: 探索追跡のセキュリティ設定について、STDATA(PRIVILEGED(YES))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリテに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索追跡のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(PRIVILEGED(を指定し、OSKB020046の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STDATA(PRIVILEGED(
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STDATA(PRIVILEGED(
    CASE OSKB020046
    SOURCE RACF
    ```

    STDATA(PRIVILEGED(とOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020046を同じ出力で読み、探索追跡のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020046 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STDATA(PRIVILEGED(YES)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STDATA(PRIVILEGED( と OSKB020046 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STDATA(TRUSTED(YES)) {#c26-i0274}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STDATA(TRUSTED(YES))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STDATA(TRUSTED(YES))**

    - 検証目的: 終端追跡のセキュリティ設定について、STDATA(TRUSTED(YES))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリティ設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端追跡のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(TRUSTED(YESを指定し、OSKB020045の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STDATA(TRUSTED(YES
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STDATA(TRUSTED(YES
    CASE OSKB020045
    SOURCE RACF
    ```

    STDATA(TRUSTED(YESとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020045を同じ出力で読み、終端追跡のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020045 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STDATA(TRUSTED(YES)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STDATA(TRUSTED(YES と OSKB020045 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### STDATA(USER(id)) {#c26-i0275}
*分類: RDEFINE STARTED*  ・  難易度: 上級

STDATA(USER(id))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **STDATA(USER(id))**

    - 検証目的: 呼出追跡のセキュリティ設定について、STDATA(USER(id))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出追跡のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(USER(id))を指定し、OSKB020043の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND STDATA(USER(id))
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM STDATA(USER(id))
    CASE OSKB020043
    SOURCE RACF
    ```

    STDATA(USER(id))とOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020043を同じ出力で読み、呼出追跡のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020043 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I STDATA(USER(id)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の STDATA(USER(id)) と OSKB020043 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE SURROGAT

### BPX.SRV.userid プロファイル {#c26-i0276}
*分類: RDEFINE SURROGAT*  ・  難易度: 上級

RACF SETROPTS RDEFINE RACDCERTのRDEFINE SURROGATでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE SURROGATは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、BPX.SRV.userid プロファイルの表記と許可される値を確認します。

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **BPX.SRV.userid プロファイル**

    - 検証目的: 区切追跡のプロファイルについて、RACF SETROPTS RDEFINE RACDCERT の RDEFINE SURROGAT では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切追跡のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にBPX.SRV.userid プロフを指定し、OSKB020050の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND BPX.SRV.userid プロフ
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM BPX.SRV.userid プロフ
    CASE OSKB020050
    SOURCE RACF
    ```

    BPX.SRV.userid プロフとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020050を同じ出力で読み、区切追跡のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020050 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I BPX.SRV.userid プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の BPX.SRV.userid プロフ と OSKB020050 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SURROGAT クラスの用途 {#c26-i0277}
*分類: RDEFINE SURROGAT*  ・  難易度: 上級

SURROGAT クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SURROGATで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SURROGAT クラスの用途**

    - 検証目的: 出力追跡のクラスの用途について、SURROGAT クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SURROGAT で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力追跡のクラスの用途の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSURROGAT クラスの用途を指定し、OSKB020048の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SURROGAT クラスの用途
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SURROGAT クラスの用途
    CASE OSKB020048
    SOURCE RACF
    ```

    SURROGAT クラスの用途とOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020048を同じ出力で読み、出力追跡のクラスの用途の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020048 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SURROGAT クラスの用途 INFORMATION LISTED
    ```

    IRRD105IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SURROGAT クラスの用途 と OSKB020048 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### userid.SUBMIT プロファイル {#c26-i0278}
*分類: RDEFINE SURROGAT*  ・  難易度: 上級

userid.SUBMIT プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SURROGATで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **userid.SUBMIT プロファイル**

    - 検証目的: 条件追跡のプロファイルについて、userid.SUBMIT プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SURROGAT で認証、権限、またはセキュリティ設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件追跡のプロファイルの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にuserid.SUBMIT プロファを指定し、OSKB020049の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND userid.SUBMIT プロファ
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM userid.SUBMIT プロファ
    CASE OSKB020049
    SOURCE RACF
    ```

    userid.SUBMIT プロファとOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020049を同じ出力で読み、条件追跡のプロファイルの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020049 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I userid.SUBMIT プロファイル INFORMATION LISTED
    ```

    IRRD105IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の userid.SUBMIT プロファ と OSKB020049 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE TSO

### ACCTNUM クラス {#c26-i0279}
*分類: RDEFINE TSO*  ・  難易度: 上級

ACCTNUM クラスは、TSO アカウント番号制御。「ACCTNUM クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ACCTNUM クラス**

    - 検証目的: 比較検査のクラスについて、ACCTNUM クラスは、TSO アカウント番号制御。「ACCTNUM クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にACCTNUM クラスを指定し、OSKB020074の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ACCTNUM クラス
    CASE OSKB020074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ACCTNUM クラス
    CASE OSKB020074
    SOURCE RACF
    ```

    ACCTNUM クラスとOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020074を同じ出力で読み、比較検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020074
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020074 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ACCTNUM クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ACCTNUM クラス と OSKB020074 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### PERFGRP クラス {#c26-i0280}
*分類: RDEFINE TSO*  ・  難易度: 上級

PERFGRP クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE TSOで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **PERFGRP クラス**

    - 検証目的: 順序検査のクラスについて、PERFGRP クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE TSO で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にPERFGRP クラスを指定し、OSKB020075の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND PERFGRP クラス
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM PERFGRP クラス
    CASE OSKB020075
    SOURCE RACF
    ```

    PERFGRP クラスとOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020075を同じ出力で読み、順序検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020075 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I PERFGRP クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の PERFGRP クラス と OSKB020075 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### TSOAUTH クラス {#c26-i0281}
*分類: RDEFINE TSO*  ・  難易度: 上級

TSOAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE TSOで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **TSOAUTH クラス**

    - 検証目的: 記録検査のクラスについて、TSOAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE TSO で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にTSOAUTH クラスを指定し、OSKB020073の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND TSOAUTH クラス
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM TSOAUTH クラス
    CASE OSKB020073
    SOURCE RACF
    ```

    TSOAUTH クラスとOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020073を同じ出力で読み、記録検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020073 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I TSOAUTH クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の TSOAUTH クラス と OSKB020073 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### TSOPROC クラス {#c26-i0282}
*分類: RDEFINE TSO*  ・  難易度: 上級

TSOPROC クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE TSOで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **TSOPROC クラス**

    - 検証目的: 優先検査のクラスについて、TSOPROC クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE TSO で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にTSOPROC クラスを指定し、OSKB020072の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND TSOPROC クラス
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM TSOPROC クラス
    CASE OSKB020072
    SOURCE RACF
    ```

    TSOPROC クラスとOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020072を同じ出力で読み、優先検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020072 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I TSOPROC クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の TSOPROC クラス と OSKB020072 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE UNIXPRIV

### CHOWN.UNRESTRICTED {#c26-i0283}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

CHOWN.UNRESTRICTEDは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE UNIXPRIVで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **CHOWN.UNRESTRICTED**

    - 検証目的: 構文判定のセキュリティ設定について、CHOWN.UNRESTRICTED は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE UNIXPRIV で認証、権限、またはセキュリティ設定をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020081の検証用出力を記録できる。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にCHOWN.UNRESTRICTEDを指定し、OSKB020081の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CHOWN.UNRESTRICTED
    CASE OSKB020081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CHOWN.UNRESTRICTED
    CASE OSKB020081
    SOURCE RACF
    ```

    CHOWN.UNRESTRICTEDとOSKB020081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020081を同じ出力で読み、構文判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020081
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020081 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I CHOWN.UNRESTRICTED INFORMATION LISTED
    ```

    IRRD105IとOSKB020081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の CHOWN.UNRESTRICTED と OSKB020081 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RESTRICTED.FILESYS.ACCESS {#c26-i0284}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、RESTRICTED.FILESYS.ACCESSの表記と許可される値を確認します。

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **RESTRICTED.FILESYS.ACCESS**

    - 検証目的: 展開判定のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020082の検証用出力を記録できる。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にRESTRICTED.FILESYSを指定し、OSKB020082の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RESTRICTED.FILESYS
    CASE OSKB020082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RESTRICTED.FILESYS
    CASE OSKB020082
    SOURCE RACF
    ```

    RESTRICTED.FILESYSとOSKB020082が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020082を同じ出力で読み、展開判定のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020082
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020082 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RESTRICTED.FILESYS.ACCES INFORMATION LISTED
    ```

    IRRD105IとOSKB020082が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RESTRICTED.FILESYS と OSKB020082 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SUPERUSER.FILESYS {#c26-i0285}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

SUPERUSER.FILESYSは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE UNIXPRIVで認証、権限、またはセキュリティ設定を確認する項目です。SUPERUSER.FILESYSは、ファイルシステム特権アクセス。「SUPERUSER.FILESYS」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SUPERUSER.FILESYS**

    - 検証目的: 警告検査のセキュリティ設定について、SUPERUSER.FILESYS は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE UNIXPRIV で認証、権限、またはセキュリティ設定を確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020077の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告検査のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.FILESYSを指定し、OSKB020077の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SUPERUSER.FILESYS
    CASE OSKB020077
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SUPERUSER.FILESYS
    CASE OSKB020077
    SOURCE RACF
    ```

    SUPERUSER.FILESYSとOSKB020077が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020077を同じ出力で読み、警告検査のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020077
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020077 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SUPERUSER.FILESYS INFORMATION LISTED
    ```

    IRRD105IとOSKB020077が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SUPERUSER.FILESYS と OSKB020077 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SUPERUSER.FILESYS.CHOWN {#c26-i0286}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUPERUSER.FILESYS.CHOWNの表記と許可される値を確認します。

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SUPERUSER.FILESYS.CHOWN**

    - 検証目的: 監査検査のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020079の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査検査のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.FILESYS.を指定し、OSKB020079の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SUPERUSER.FILESYS.
    CASE OSKB020079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SUPERUSER.FILESYS.
    CASE OSKB020079
    SOURCE RACF
    ```

    SUPERUSER.FILESYS.とOSKB020079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020079を同じ出力で読み、監査検査のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020079
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020079 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SUPERUSER.FILESYS.CHOWN INFORMATION LISTED
    ```

    IRRD105IとOSKB020079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SUPERUSER.FILESYS. と OSKB020079 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SUPERUSER.FILESYS.MOUNT {#c26-i0287}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUPERUSER.FILESYS.MOUNTの表記と許可される値を確認します。

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SUPERUSER.FILESYS.MOUNT**

    - 検証目的: 復旧検査のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020078の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧検査のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.FILESYS.を指定し、OSKB020078の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SUPERUSER.FILESYS.
    CASE OSKB020078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SUPERUSER.FILESYS.
    CASE OSKB020078
    SOURCE RACF
    ```

    SUPERUSER.FILESYS.とOSKB020078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020078を同じ出力で読み、復旧検査のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020078
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020078 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SUPERUSER.FILESYS.MOUNT INFORMATION LISTED
    ```

    IRRD105IとOSKB020078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SUPERUSER.FILESYS. と OSKB020078 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SUPERUSER.PROCESS.KILL {#c26-i0288}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUPERUSER.PROCESS.KILLの表記と許可される値を確認します。

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **SUPERUSER.PROCESS.KILL**

    - 検証目的: 変更検査のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020080の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更検査のセキュリティ設定の確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.PROCESS.を指定し、OSKB020080の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SUPERUSER.PROCESS.
    CASE OSKB020080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SUPERUSER.PROCESS.
    CASE OSKB020080
    SOURCE RACF
    ```

    SUPERUSER.PROCESS.とOSKB020080が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020080を同じ出力で読み、変更検査のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020080
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020080 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SUPERUSER.PROCESS.KILL INFORMATION LISTED
    ```

    IRRD105IとOSKB020080が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SUPERUSER.PROCESS. と OSKB020080 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### UNIXPRIV クラス {#c26-i0289}
*分類: RDEFINE UNIXPRIV*  ・  難易度: 上級

UNIXPRIV クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE UNIXPRIVで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **UNIXPRIV クラス**

    - 検証目的: 値域検査のクラスについて、UNIXPRIV クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE UNIXPRIV で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020076の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域検査のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にUNIXPRIV クラスを指定し、OSKB020076の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND UNIXPRIV クラス
    CASE OSKB020076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM UNIXPRIV クラス
    CASE OSKB020076
    SOURCE RACF
    ```

    UNIXPRIV クラスとOSKB020076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020076を同じ出力で読み、値域検査のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020076
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020076 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I UNIXPRIV クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の UNIXPRIV クラス と OSKB020076 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE その他

### DLFCLASS クラス {#c26-i0290}
*分類: RDEFINE その他*  ・  難易度: 上級

DLFCLASS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 探索確認のクラスで DLFCLASS クラスの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLFCLASS クラスの出力を取らず探索確認のクラスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索確認の確認値として扱う。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して探索確認のクラスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のクラスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認のクラスにおいて選択記号 B を採用し、識別名は探索確認です。探索確認のクラスにおいて DLFCLASS クラス は説明欄の「探索確認のクラスに関係する定義値と表示行を照合する探索確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のクラスの証跡を読む担当者は、DLFCLASS クラスの属性行と IRRD105I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のクラスは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため探索確認ではありません。 D: 探索確認のクラスは別カテゴリの確認を流用しており、DLFCLASS クラスの根拠にならないため探索確認ではありません。探索確認のクラスに出る DLFCLASS クラスは RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は探索確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **DLFCLASS クラス**

    - 検証目的: 監査判定のクラスについて、DLFCLASS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020099の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、監査判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にDLFCLASS クラスを指定し、OSKB020099の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DLFCLASS クラス
    CASE OSKB020099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DLFCLASS クラス
    CASE OSKB020099
    SOURCE RACF
    ```

    DLFCLASS クラスとOSKB020099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020099を同じ出力で読み、監査判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020099
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020099 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DLFCLASS クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DLFCLASS クラス と OSKB020099 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### DSNR クラス {#c26-i0291}
*分類: RDEFINE その他*  ・  難易度: 上級

DSNR クラスは、Db2 サブシステム アクセス制御。「DSNR クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 終端確認のクラスに関係する DSNR クラスの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端確認で再確認できる形にする。 ✅
    - B. DSNR クラスの名称と担当者名のみを残して終端確認のクラスの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で終端確認のクラスを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず終端確認のクラスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認のクラスにおいて選択記号 A を採用し、識別名は終端確認です。終端確認のクラスにおいて DSNR クラス は説明欄の「DSNR クラスの用途をセキュリティ設定の表示で確認する終端確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認のクラスに関連して、RACF では DSNR クラスの表示属性と IRRD105I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認のクラスは対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認のクラスは別カテゴリの確認を流用しており、DSNR クラスの根拠にならないため終端確認ではありません。 D: 終端確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため終端確認ではありません。終端確認のクラスで使う DSNR クラスという用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は終端確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **DSNR クラス**

    - 検証目的: 復旧判定のクラスについて、DSNR クラスは、Db2 サブシステム アクセス制御。「DSNR クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020098の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にDSNR クラスを指定し、OSKB020098の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DSNR クラス
    CASE OSKB020098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DSNR クラス
    CASE OSKB020098
    SOURCE RACF
    ```

    DSNR クラスとOSKB020098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020098を同じ出力で読み、復旧判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020098
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020098 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DSNR クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DSNR クラス と OSKB020098 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### GLOBAL クラス {#c26-i0292}
*分類: RDEFINE その他*  ・  難易度: 上級

GLOBAL クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 上書確認のクラスでセキュリティ設定の運用確認を行います。GLOBAL クラスの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で上書確認のクラスを確認した扱いにする。
    - B. IRRD105I の有無を確認せず上書確認のクラスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書確認の根拠を固定する。 ✅
    - D. GLOBAL クラスの属性行を読まず上書確認のクラスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認のクラスにおいて選択記号 C を採用し、識別名は上書確認です。上書確認のクラスにおいて GLOBAL クラス は説明欄の「RACF で GLOBAL クラスの扱いを記録する上書確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のクラスを受け取る担当者は、GLOBAL クラスの表示結果と IRRD105I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のクラスは別カテゴリの確認を流用しており、GLOBAL クラスの根拠にならないため上書確認ではありません。 B: 上書確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため上書確認ではありません。 C: 上書確認のクラスは対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のクラスが示す GLOBAL クラスは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **GLOBAL クラス**

    - 検証目的: 変更判定のクラスについて、GLOBAL クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020100の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、変更判定のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にGLOBAL クラスを指定し、OSKB020100の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND GLOBAL クラス
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM GLOBAL クラス
    CASE OSKB020100
    SOURCE RACF
    ```

    GLOBAL クラスとOSKB020100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020100を同じ出力で読み、変更判定のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020100 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I GLOBAL クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の GLOBAL クラス と OSKB020100 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IDIDMAP クラス {#c26-i0293}
*分類: RDEFINE その他*  ・  難易度: 上級

IDIDMAP クラスは、分散 ID マッピング。「IDIDMAP クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 出力確認のクラスに関する IDIDMAP クラスの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力確認のクラスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のクラスの証跡として保存して根拠にする。
    - C. IDIDMAP クラスの変更点を出力本文から切り離して出力確認のクラスの承認欄のみ残す。
    - D. IRRD105I を含む表示を保存し、説明欄との差分を出力確認で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認のクラスにおいて選択記号 D を採用し、識別名は出力確認です。出力確認のクラスにおいて IDIDMAP クラス は説明欄の「IDIDMAP クラスの状態と出力メッセージを結び付ける出力確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認のクラスに関する記録は、IDIDMAP クラスの出力行と IRRD105I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力確認ではありません。 B: 出力確認のクラスは別カテゴリの確認を流用しており、IDIDMAP クラスの根拠にならないため出力確認ではありません。 C: 出力確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認のクラスは対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認のクラスで記録する IDIDMAP クラスは RACF の確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IDIDMAP クラス**

    - 検証目的: 構文整理のクラスについて、IDIDMAP クラスは、分散 ID マッピング。「IDIDMAP クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文整理のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にIDIDMAP クラスを指定し、OSKB020101の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IDIDMAP クラス
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IDIDMAP クラス
    CASE OSKB020101
    SOURCE RACF
    ```

    IDIDMAP クラスとOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020101を同じ出力で読み、構文整理のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020101 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IDIDMAP クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IDIDMAP クラス と OSKB020101 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### SOMDOBJS クラス {#c26-i0294}
*分類: RDEFINE その他*  ・  難易度: 上級

SOMDOBJS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 条件確認のクラスに関係する SOMDOBJS クラスの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、条件確認の証跡として残す。 ✅
    - B. SOMDOBJS クラスの名称と担当者名のみを残して条件確認のクラスの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で条件確認のクラスを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず条件確認のクラスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認のクラスにおいて選択記号 A を採用し、識別名は条件確認です。条件確認のクラスにおいて SOMDOBJS クラス は説明欄の「SOMDOBJS クラスの用途をセキュリティ設定の表示で確認する条件確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のクラスに関連して、RACF では SOMDOBJS クラスの表示属性と IRRD105I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のクラスは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のクラスは別カテゴリの確認を流用しており、SOMDOBJS クラスの根拠にならないため条件確認ではありません。 D: 条件確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件確認ではありません。条件確認のクラスで使う SOMDOBJS クラスという用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **SOMDOBJS クラス**

    - 検証目的: 展開整理のクラスについて、SOMDOBJS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020102の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開整理のクラスの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にSOMDOBJS クラスを指定し、OSKB020102の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SOMDOBJS クラス
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SOMDOBJS クラス
    CASE OSKB020102
    SOURCE RACF
    ```

    SOMDOBJS クラスとOSKB020102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020102を同じ出力で読み、展開整理のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020102 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SOMDOBJS クラス INFORMATION LISTED
    ```

    IRRD105IとOSKB020102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SOMDOBJS クラス と OSKB020102 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > RDEFINE オペランド

### ADDCATEGORY(category) {#c26-i0295}
*分類: RDEFINE オペランド*  ・  難易度: 上級

ADDCATEGORY(category)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **ADDCATEGORY(category)**

    - 検証目的: 比較照合のオペランドについて、ADDCATEGORY(category)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にADDCATEGORY(categoを指定し、OSKB020034の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ADDCATEGORY(catego
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ADDCATEGORY(catego
    CASE OSKB020034
    SOURCE RACF
    ```

    ADDCATEGORY(categoとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020034を同じ出力で読み、比較照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020034 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ADDCATEGORY(category) INFORMATION LISTED
    ```

    IRRD105IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ADDCATEGORY(catego と OSKB020034 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### ADDMEM(member1,member2,…) {#c26-i0296}
*分類: RDEFINE オペランド*  ・  難易度: 上級

ADDMEM(member1,member2,…)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)


### APPLDATA('text') {#c26-i0297}
*分類: RDEFINE オペランド*  ・  難易度: 上級

APPLDATA('text')は、アプリケーション用データ 255 文字。「APPLDATA('text')」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **APPLDATA('text')**

    - 検証目的: 呼出照合のオペランドについて、APPLDATA('text')は、アプリケーション用データ 255 文字。「APPLDATA('text')」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO RACFの表示結果です。FIND欄にAPPLDATA('text')を指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND APPLDATA('text')
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM APPLDATA('text')
    CASE OSKB020023
    SOURCE RACF
    ```

    APPLDATA('text')とOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020023を同じ出力で読み、呼出照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020023 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I APPLDATA('text') INFORMATION LISTED
    ```

    IRRD105IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の APPLDATA('text') と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)


