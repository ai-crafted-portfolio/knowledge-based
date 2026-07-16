---
search:
  exclude: true
---

# TSO / ISPF / SDSF — 詳細 (4/6)

[← TSO / ISPF / SDSF の概要へ戻る](index.md)


## TSO / ISPF / SDSF > TSO_ALLOCATE

### UNIT オペランド {#c30-i0243}
*分類: TSO_ALLOCATE*  ・  難易度: 中級

UNIT オペランドは、TSO / ISPF / SDSFのTSO_ALLOCATEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? question "確認問題（1問）"
    **問題.** 呼出確認のオペランドで対話操作の運用確認を行います。UNIT オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で呼出確認のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず呼出確認のオペランドを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. UNIT オペランドの属性行を読まず呼出確認のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認のオペランドにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認のオペランドにおいて UNIT オペランド は説明欄の「TSO ISPF SDSF で UNIT オペランドの扱いを記録する呼出確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認のオペランドを受け取る担当者は、UNIT オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認のオペランドは別カテゴリの確認を流用しており、UNIT オペランドの根拠にならないため呼出確認ではありません。 B: 呼出確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認のオペランドは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認のオペランドが示す UNIT オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **UNIT オペランド**

    - 検証目的: 値域確認のオペランドについて、UNIT オペランドは、TSO / ISPF / SDSF の TSO_ALLOCATE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域確認のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にUNIT オペランドを指定し、OSKB010016の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND UNIT オペランド
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM UNIT オペランド
    CASE OSKB010016
    SOURCE TSO ISPF SDSF
    ```

    UNIT オペランドとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010016を同じ出力で読み、値域確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010016
    COMMAND ===> SDSF DA
    ISF031I UNIT オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の UNIT オペランド と OSKB010016 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### USING オペランド {#c30-i0244}
*分類: TSO_ALLOCATE*  ・  難易度: 中級

USING オペランドは、TSO / ISPF / SDSFのTSO_ALLOCATEで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? question "確認問題（1問）"
    **問題.** 上書確認のオペランドで対話操作の運用確認を行います。USING オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で上書確認のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず上書確認のオペランドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 ✅
    - D. USING オペランドの属性行を読まず上書確認のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認のオペランドにおいて選択記号 C を採用し、識別名は上書確認です。上書確認のオペランドにおいて USING オペランド は説明欄の「TSO ISPF SDSF で USING オペランドの扱いを記録する上書確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のオペランドを受け取る担当者は、USING オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のオペランドは別カテゴリの確認を流用しており、USING オペランドの根拠にならないため上書確認ではありません。 B: 上書確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため上書確認ではありません。 C: 上書確認のオペランドは対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のオペランドが示す USING オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **USING オペランド**

    - 検証目的: 変更確認のオペランドについて、USING オペランドは、TSO / ISPF / SDSF の TSO_ALLOCATE で自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更確認のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にUSING オペランドを指定し、OSKB010020の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND USING オペランド
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM USING オペランド
    CASE OSKB010020
    SOURCE TSO ISPF SDSF
    ```

    USING オペランドとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010020を同じ出力で読み、変更確認のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010020
    COMMAND ===> SDSF DA
    ISF031I USING オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の USING オペランド と OSKB010020 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### VOLUME/VOL オペランド {#c30-i0245}
*分類: TSO_ALLOCATE*  ・  難易度: 中級

VOLUME/VOL オペランドは、TSO / ISPF / SDSFのTSO_ALLOCATEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **VOLUME ・ VOL オペランド**

    - 検証目的: 警告確認の・ オペランドについて、VOLUME/VOL オペランドは、TSO / ISPF / SDSF の TSO_ALLOCATE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告確認の・ オペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にVOLUME ・ VOL オペランドを指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND VOLUME ・ VOL オペランド
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM VOLUME ・ VOL オペランド
    CASE OSKB010017
    SOURCE TSO ISPF SDSF
    ```

    VOLUME ・ VOL オペランドとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010017を同じ出力で読み、警告確認の・ オペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010017
    COMMAND ===> SDSF DA
    ISF031I VOLUME ・ VOL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の VOLUME ・ VOL オペランド と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide




## TSO / ISPF / SDSF > TSO_COPY

### COPY NONUM オペランド {#c30-i0246}
*分類: TSO_COPY*  ・  難易度: 中級

COPY NONUM オペランドは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 条件追跡のオペランドに関係する COPY NONUM オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SDSF DA の結果から対象行を抜き出し、条件追跡の証跡として残す。 ✅
    - B. COPY NONUM オペランドの名称と担当者名のみを残して条件追跡のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で条件追跡のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず条件追跡のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡のオペランドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡のオペランドにおいて COPY NONUM オペランド は説明欄の「COPY NONUM オペランドの用途を対話操作の表示で確認する条件追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡のオペランドに関連して、TSO ISPF SDSF では COPY NONUM オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡のオペランドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡のオペランドは別カテゴリの確認を流用しており、COPY NONUM オペランドの根拠にならないため条件追跡ではありません。 D: 条件追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため条件追跡ではありません。条件追跡のオペランドで使う COPY NONUM オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は条件追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY NONUM オペランド**

    - 検証目的: 展開検査のオペランドについて、COPY NONUM オペランドは、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、展開検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY NONUM オペランドを指定し、OSKB010062の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY NONUM オペランド
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY NONUM オペランド
    CASE OSKB010062
    SOURCE TSO ISPF SDSF
    ```

    COPY NONUM オペランドとOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010062を同じ出力で読み、展開検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010062
    COMMAND ===> SDSF DA
    ISF031I COPY NONUM オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY NONUM オペランド と OSKB010062 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY NOPACK オペランド {#c30-i0247}
*分類: TSO_COPY*  ・  難易度: 中級

COPY NOPACK オペランドは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 呼出確認のオペランドで対話操作の運用確認を行います。COPY NOPACK オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で呼出確認のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず呼出確認のオペランドを正常終了として記録する。
    - C. 同じ画面で対象行と ISF031I を読み、呼出確認の結果として保存する。 ✅
    - D. COPY NOPACK オペランドの属性行を読まず呼出確認のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認のオペランドにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認のオペランドにおいて COPY NOPACK オペランド は説明欄の「TSO ISPF SDSF で COPY NOPACK オペランドの扱いを記録する呼出確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認のオペランドを受け取る担当者は、COPY NOPACK オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認のオペランドは別カテゴリの確認を流用しており、COPY NOPACK オペランドの根拠にならないため呼出確認ではありません。 B: 呼出確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認のオペランドは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認のオペランドが示す COPY NOPACK オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY NOPACK オペランド**

    - 検証目的: 探索検査のオペランドについて、COPY NOPACK オペランドは、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、探索検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY NOPACK オペランドを指定し、OSKB010066の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY NOPACK オペランド
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY NOPACK オペランド
    CASE OSKB010066
    SOURCE TSO ISPF SDSF
    ```

    COPY NOPACK オペランドとOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010066を同じ出力で読み、探索検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010066
    COMMAND ===> SDSF DA
    ISF031I COPY NOPACK オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY NOPACK オペランド と OSKB010066 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY PACK オペランド {#c30-i0248}
*分類: TSO_COPY*  ・  難易度: 中級

COPY PACK オペランドは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 展開確認のオペランドで COPY PACK オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COPY PACK オペランドの出力を取らず展開確認のオペランドの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開確認の根拠にする。 ✅
    - C. SDSF DA を省略して展開確認のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認のオペランドにおいて選択記号 B を採用し、識別名は展開確認です。展開確認のオペランドにおいて COPY PACK オペランド は説明欄の「展開確認のオペランドに関係する定義値と表示行を照合する展開確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認のオペランドの証跡を読む担当者は、COPY PACK オペランドの属性行と ISF031I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認のオペランドは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため展開確認ではありません。 D: 展開確認のオペランドは別カテゴリの確認を流用しており、COPY PACK オペランドの根拠にならないため展開確認ではありません。展開確認のオペランドに出る COPY PACK オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY PACK オペランド**

    - 検証目的: 終端検査のオペランドについて、COPY PACK オペランドは、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、終端検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY PACK オペランドを指定し、OSKB010065の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY PACK オペランド
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY PACK オペランド
    CASE OSKB010065
    SOURCE TSO ISPF SDSF
    ```

    COPY PACK オペランドとOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010065を同じ出力で読み、終端検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010065
    COMMAND ===> SDSF DA
    ISF031I COPY PACK オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY PACK オペランド と OSKB010065 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY PDS→PDS {#c30-i0249}
*分類: TSO_COPY*  ・  難易度: 中級

COPY PDS→PDSは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 探索確認のからで COPY PDS から PDS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COPY PDS から PDS の出力を取らず探索確認のからの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索確認の確認にする。 ✅
    - C. SDSF DA を省略して探索確認のからの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のからへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認のからにおいて選択記号 B を採用し、識別名は探索確認です。探索確認のからにおいて COPY PDS から PDS は説明欄の「探索確認のからに関係する定義値と表示行を照合する探索確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のからの証跡を読む担当者は、COPY PDS から PDS の属性行と ISF031I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のからは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のからは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のからは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため探索確認ではありません。 D: 探索確認のからは別カテゴリの確認を流用しており、COPY PDS から PDS の根拠にならないため探索確認ではありません。探索確認のからに出る COPY PDS から PDS は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は探索確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200



### COPY RENUM オペランド {#c30-i0250}
*分類: TSO_COPY*  ・  難易度: 中級

COPY RENUM オペランドは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 区切追跡のオペランドで COPY RENUM オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. COPY RENUM オペランドの出力を取らず区切追跡のオペランドの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切追跡の確認記録にまとめる。 ✅
    - C. SDSF DA を省略して区切追跡のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡のオペランドにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡のオペランドにおいて COPY RENUM オペランド は説明欄の「区切追跡のオペランドに関係する定義値と表示行を照合する区切追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡のオペランドの証跡を読む担当者は、COPY RENUM オペランドの属性行と ISF031I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡のオペランドは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡のオペランドは別カテゴリの確認を流用しており、COPY RENUM オペランドの根拠にならないため区切追跡ではありません。区切追跡のオペランドに出る COPY RENUM オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY RENUM オペランド**

    - 検証目的: 呼出検査のオペランドについて、COPY RENUM オペランドは、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、呼出検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY RENUM オペランドを指定し、OSKB010063の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY RENUM オペランド
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY RENUM オペランド
    CASE OSKB010063
    SOURCE TSO ISPF SDSF
    ```

    COPY RENUM オペランドとOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010063を同じ出力で読み、呼出検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010063
    COMMAND ===> SDSF DA
    ISF031I COPY RENUM オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY RENUM オペランド と OSKB010063 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY REPLACE オペランド {#c30-i0251}
*分類: TSO_COPY*  ・  難易度: 中級

COPY REPLACE オペランドは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 構文確認のオペランドに関係する COPY REPLACE オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文確認の確認記録にまとめる。 ✅
    - B. COPY REPLACE オペランドの名称と担当者名のみを残して構文確認のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で構文確認のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず構文確認のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認のオペランドにおいて選択記号 A を採用し、識別名は構文確認です。構文確認のオペランドにおいて COPY REPLACE オペランド は説明欄の「COPY REPLACE オペランドの用途を対話操作の表示で確認する構文確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認のオペランドに関連して、TSO ISPF SDSF では COPY REPLACE オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認のオペランドは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認のオペランドは別カテゴリの確認を流用しており、COPY REPLACE オペランドの根拠にならないため構文確認ではありません。 D: 構文確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため構文確認ではありません。構文確認のオペランドで使う COPY REPLACE オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は構文確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY REPLACE オペランド**

    - 検証目的: 置換検査のオペランドについて、COPY REPLACE オペランドは、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、置換検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY REPLACE オペランドを指定し、OSKB010064の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY REPLACE オペランド
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY REPLACE オペランド
    CASE OSKB010064
    SOURCE TSO ISPF SDSF
    ```

    COPY REPLACE オペランドとOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010064を同じ出力で読み、置換検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010064
    COMMAND ===> SDSF DA
    ISF031I COPY REPLACE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY REPLACE オペランド と OSKB010064 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY SHARE オペランド {#c30-i0252}
*分類: TSO_COPY*  ・  難易度: 中級

COPY SHARE オペランドは、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 置換確認のオペランドに関する COPY SHARE オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず置換確認のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のオペランドの証跡として保存して根拠にする。
    - C. COPY SHARE オペランドの変更点を出力本文から切り離して置換確認のオペランドの承認欄のみ残す。
    - D. SDSF DA で得た表示本文を使い、置換確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認のオペランドにおいて選択記号 D を採用し、識別名は置換確認です。置換確認のオペランドにおいて COPY SHARE オペランド は説明欄の「COPY SHARE オペランドの状態と出力メッセージを結び付ける置換確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認のオペランドに関する記録は、COPY SHARE オペランドの出力行と ISF031I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため置換確認ではありません。 B: 置換確認のオペランドは別カテゴリの確認を流用しており、COPY SHARE オペランドの根拠にならないため置換確認ではありません。 C: 置換確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認のオペランドは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認のオペランドで記録する COPY SHARE オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は置換確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY SHARE オペランド**

    - 検証目的: 上書検査のオペランドについて、COPY SHARE オペランドは、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、上書検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY SHARE オペランドを指定し、OSKB010067の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY SHARE オペランド
    CASE OSKB010067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY SHARE オペランド
    CASE OSKB010067
    SOURCE TSO ISPF SDSF
    ```

    COPY SHARE オペランドとOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010067を同じ出力で読み、上書検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010067
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010067
    COMMAND ===> SDSF DA
    ISF031I COPY SHARE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY SHARE オペランド と OSKB010067 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY メンバ単位 {#c30-i0253}
*分類: TSO_COPY*  ・  難易度: 中級

COPY メンバ単位は、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 上書確認のメンバ単位で対話操作の運用確認を行います。COPY メンバ単位の根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で上書確認のメンバ単位を確認した扱いにする。
    - B. ISF031I の有無を確認せず上書確認のメンバ単位を正常終了として記録する。
    - C. TSO ISPF SDSF の表示形式に沿って根拠行を採り、上書確認の点検結果を残す。 ✅
    - D. COPY メンバ単位の属性行を読まず上書確認のメンバ単位の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認のメンバ単位において選択記号 C を採用し、識別名は上書確認です。上書確認のメンバ単位において COPY メンバ単位 は説明欄の「TSO ISPF SDSF で COPY メンバ単位の扱いを記録する上書確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のメンバ単位を受け取る担当者は、COPY メンバ単位の表示結果と ISF031I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のメンバ単位は別カテゴリの確認を流用しており、COPY メンバ単位の根拠にならないため上書確認ではありません。 B: 上書確認のメンバ単位は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため上書確認ではありません。 C: 上書確認のメンバ単位は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のメンバ単位は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のメンバ単位が示す COPY メンバ単位は出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY メンバ単位**

    - 検証目的: 区切検査のメンバ単位について、COPY メンバ単位は、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、区切検査のメンバ単位の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY メンバ単位を指定し、OSKB010070の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY メンバ単位
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY メンバ単位
    CASE OSKB010070
    SOURCE TSO ISPF SDSF
    ```

    COPY メンバ単位とOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010070を同じ出力で読み、区切検査のメンバ単位の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010070
    COMMAND ===> SDSF DA
    ISF031I COPY メンバ単位 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY メンバ単位 と OSKB010070 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY 基本構文 {#c30-i0254}
*分類: TSO_COPY*  ・  難易度: 初級

ソース により ターゲットのデータセット/メンバコピー。IEBCOPY 相当だが TSO/ISPF 向け。ソース→ターゲットのデータセット/メンバコピー。IEBCOPY 相当だが TSO/ISPF 向け

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 出力追跡の基本構文に関する COPY 基本構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず出力追跡の基本構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の基本構文の証跡として保存して根拠にする。
    - C. COPY 基本構文の変更点を出力本文から切り離して出力追跡の基本構文の承認欄のみ残す。
    - D. ISF031I を含む表示を保存し、説明欄との差分を出力追跡で確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力追跡の基本構文において選択記号 D を採用し、識別名は出力追跡です。出力追跡の基本構文において COPY 基本構文 は説明欄の「ソース により ターゲットのデータセット/メンバコピー。IEBCOPY 相当だが TSO/ISPF 向け。ソースからターゲットのデータセット」と SDSF DA または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の基本構文に関する記録は、COPY 基本構文の出力行と ISF031I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の基本構文は別カテゴリの確認を流用しており、COPY 基本構文の根拠にならないため出力追跡ではありません。 C: 出力追跡の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の基本構文は対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の基本構文で記録する COPY 基本構文は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **COPY 基本構文**

    - 検証目的: 構文検査の基本構文について、ソース により ターゲットのデータセット/メンバコピー。IEBCOPY 相当だが TSO/ISPF 向け。ソースからターゲットのデータセット/メンバコピー。IEBCOPYに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、構文検査の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY 基本構文を指定し、OSKB010061の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY 基本構文
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY 基本構文
    CASE OSKB010061
    SOURCE TSO ISPF SDSF
    ```

    COPY 基本構文とOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010061を同じ出力で読み、構文検査の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010061
    COMMAND ===> SDSF DA
    ISF031I COPY 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY 基本構文 と OSKB010061 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)



### COPY 順次→順次 {#c30-i0255}
*分類: TSO_COPY*  ・  難易度: 中級

COPY 順次→順次は、TSO / ISPF / SDSFのTSO_COPYで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS DFSMSdfp Utilities (IEBCOPY) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

??? question "確認問題（1問）"
    **問題.** 終端確認の順次から順次に関係する COPY 順次から順次の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、終端確認として引き継ぐ。 ✅
    - B. COPY 順次から順次の名称と担当者名のみを残して終端確認の順次から順次の表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で終端確認の順次から順次を確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず終端確認の順次から順次の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認の順次から順次において選択記号 A を採用し、識別名は終端確認です。終端確認の順次から順次において COPY 順次から順次 は説明欄の「COPY 順次から順次の用途を対話操作の表示で確認する終端確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の順次から順次に関連して、TSO ISPF SDSF では COPY 順次から順次の表示属性と ISF031I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の順次から順次は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の順次から順次は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の順次から順次は別カテゴリの確認を流用しており、COPY 順次から順次の根拠にならないため終端確認ではありません。 D: 終端確認の順次から順次は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため終端確認ではありません。終端確認の順次から順次で使う COPY 順次から順次という用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は終端確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200




## TSO / ISPF / SDSF > TSO_DEL_REN

### DELETE CLUSTER オペランド {#c30-i0256}
*分類: TSO_DEL_REN*  ・  難易度: 中級

DELETE CLUSTER オペランドは、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 条件確認のオペランドに関係する DELETE CLUSTER オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件確認の確認値として扱う。 ✅
    - B. DELETE CLUSTER オペランドの名称と担当者名のみを残して条件確認のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で条件確認のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず条件確認のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認のオペランドにおいて選択記号 A を採用し、識別名は条件確認です。条件確認のオペランドにおいて DELETE CLUSTER オペランド は説明欄の「DELETE CLUSTER オペランドの用途を対話操作の表示で確認する条件確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のオペランドに関連して、TSO ISPF SDSF では DELETE CLUSTER オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のオペランドは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のオペランドは別カテゴリの確認を流用しており、DELETE CLUSTER オペランドの根拠にならないため条件確認ではありません。 D: 条件確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため条件確認ではありません。条件確認のオペランドで使う DELETE CLUSTER オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は条件確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DELETE CLUSTER オペランド**

    - 検証目的: 優先検査のオペランドについて、DELETE CLUSTER オペランドは、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、優先検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDELETE CLUSTER オペラを指定し、OSKB010072の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DELETE CLUSTER オペラ
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DELETE CLUSTER オペラ
    CASE OSKB010072
    SOURCE TSO ISPF SDSF
    ```

    DELETE CLUSTER オペラとOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010072を同じ出力で読み、優先検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010072
    COMMAND ===> SDSF DA
    ISF031I DELETE CLUSTER オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DELETE CLUSTER オペラ と OSKB010072 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### DELETE FILE オペランド {#c30-i0257}
*分類: TSO_DEL_REN*  ・  難易度: 中級

DELETE FILE オペランドは、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 優先確認のオペランドに関する DELETE FILE オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず優先確認のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のオペランドの証跡として保存して根拠にする。
    - C. DELETE FILE オペランドの変更点を出力本文から切り離して優先確認のオペランドの承認欄のみ残す。
    - D. SDSF DA の結果から対象行を抜き出し、優先確認の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認のオペランドにおいて選択記号 D を採用し、識別名は優先確認です。優先確認のオペランドにおいて DELETE FILE オペランド は説明欄の「DELETE FILE オペランドの状態と出力メッセージを結び付ける優先確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認のオペランドに関する記録は、DELETE FILE オペランドの出力行と ISF031I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため優先確認ではありません。 B: 優先確認のオペランドは別カテゴリの確認を流用しており、DELETE FILE オペランドの根拠にならないため優先確認ではありません。 C: 優先確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認のオペランドは対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認のオペランドで記録する DELETE FILE オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DELETE FILE オペランド**

    - 検証目的: 順序検査のオペランドについて、DELETE FILE オペランドは、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010075の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、順序検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDELETE FILE オペランドを指定し、OSKB010075の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DELETE FILE オペランド
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DELETE FILE オペランド
    CASE OSKB010075
    SOURCE TSO ISPF SDSF
    ```

    DELETE FILE オペランドとOSKB010075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010075を同じ出力で読み、順序検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010075
    COMMAND ===> SDSF DA
    ISF031I DELETE FILE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DELETE FILE オペランド と OSKB010075 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### DELETE NOSCRATCH オペランド {#c30-i0258}
*分類: TSO_DEL_REN*  ・  難易度: 中級

DELETE NOSCRATCH オペランドは、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 範囲確認のオペランドで対話操作の運用確認を行います。DELETE NOSCRATCH オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で範囲確認のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず範囲確認のオペランドを正常終了として記録する。
    - C. ISF031I を含む表示を保存し、説明欄との差分を範囲確認で確認する。 ✅
    - D. DELETE NOSCRATCH オペランドの属性行を読まず範囲確認のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認のオペランドにおいて選択記号 C を採用し、識別名は範囲確認です。範囲確認のオペランドにおいて DELETE NOSCRATCH オペランド は説明欄の「TSO ISPF SDSF で DELETE NOSCRATCH オペランドの扱いを記録する範囲確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認のオペランドを受け取る担当者は、DELETE NOSCRATCH オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認のオペランドは別カテゴリの確認を流用しており、DELETE NOSCRATCH オペランドの根拠にならないため範囲確認ではありません。 B: 範囲確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認のオペランドは対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認のオペランドが示す DELETE NOSCRATCH オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DELETE NOSCRATCH オペランド**

    - 検証目的: 比較検査のオペランドについて、DELETE NOSCRATCH オペランドは、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010074の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、比較検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDELETE NOSCRATCH オを指定し、OSKB010074の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DELETE NOSCRATCH オ
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DELETE NOSCRATCH オ
    CASE OSKB010074
    SOURCE TSO ISPF SDSF
    ```

    DELETE NOSCRATCH オとOSKB010074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010074を同じ出力で読み、比較検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010074
    COMMAND ===> SDSF DA
    ISF031I DELETE NOSCRATCH オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DELETE NOSCRATCH オ と OSKB010074 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### DELETE PURGE オペランド {#c30-i0259}
*分類: TSO_DEL_REN*  ・  難易度: 中級

DELETE PURGE オペランドは、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 区切確認のオペランドで DELETE PURGE オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DELETE PURGE オペランドの出力を取らず区切確認のオペランドの説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切確認の根拠を固定する。 ✅
    - C. SDSF DA を省略して区切確認のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認のオペランドにおいて選択記号 B を採用し、識別名は区切確認です。区切確認のオペランドにおいて DELETE PURGE オペランド は説明欄の「区切確認のオペランドに関係する定義値と表示行を照合する区切確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認のオペランドの証跡を読む担当者は、DELETE PURGE オペランドの属性行と ISF031I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認のオペランドは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため区切確認ではありません。 D: 区切確認のオペランドは別カテゴリの確認を流用しており、DELETE PURGE オペランドの根拠にならないため区切確認ではありません。区切確認のオペランドに出る DELETE PURGE オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DELETE PURGE オペランド**

    - 検証目的: 記録検査のオペランドについて、DELETE PURGE オペランドは、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010073の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、記録検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDELETE PURGE オペランドを指定し、OSKB010073の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DELETE PURGE オペランド
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DELETE PURGE オペランド
    CASE OSKB010073
    SOURCE TSO ISPF SDSF
    ```

    DELETE PURGE オペランドとOSKB010073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010073を同じ出力で読み、記録検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010073
    COMMAND ===> SDSF DA
    ISF031I DELETE PURGE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DELETE PURGE オペランド と OSKB010073 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### DELETE メンバ指定 {#c30-i0260}
*分類: TSO_DEL_REN*  ・  難易度: 中級

DELETE メンバ指定は、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 記録確認のメンバ指定に関係する DELETE メンバ指定の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録確認の確認記録にまとめる。 ✅
    - B. DELETE メンバ指定の名称と担当者名のみを残して記録確認のメンバ指定の表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で記録確認のメンバ指定を確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず記録確認のメンバ指定の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認のメンバ指定において選択記号 A を採用し、識別名は記録確認です。記録確認のメンバ指定において DELETE メンバ指定 は説明欄の「DELETE メンバ指定の用途を対話操作の表示で確認する記録確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認のメンバ指定に関連して、TSO ISPF SDSF では DELETE メンバ指定の表示属性と ISF031I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認のメンバ指定は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認のメンバ指定は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認のメンバ指定は別カテゴリの確認を流用しており、DELETE メンバ指定の根拠にならないため記録確認ではありません。 D: 記録確認のメンバ指定は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため記録確認ではありません。記録確認のメンバ指定で使う DELETE メンバ指定という用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は記録確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DELETE メンバ指定**

    - 検証目的: 値域検査のメンバ指定について、DELETE メンバ指定は、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010076の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域検査のメンバ指定の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDELETE メンバ指定を指定し、OSKB010076の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DELETE メンバ指定
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DELETE メンバ指定
    CASE OSKB010076
    SOURCE TSO ISPF SDSF
    ```

    DELETE メンバ指定とOSKB010076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010076を同じ出力で読み、値域検査のメンバ指定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010076
    COMMAND ===> SDSF DA
    ISF031I DELETE メンバ指定 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DELETE メンバ指定 と OSKB010076 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### DELETE 基本構文 {#c30-i0261}
*分類: TSO_DEL_REN*  ・  難易度: 初級

DELETE 基本構文は、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 出力確認の基本構文に関する DELETE 基本構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず出力確認の基本構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の基本構文の証跡として保存して根拠にする。
    - C. DELETE 基本構文の変更点を出力本文から切り離して出力確認の基本構文の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力確認の基本構文において選択記号 D を採用し、識別名は出力確認です。出力確認の基本構文において DELETE 基本構文 は説明欄の「DELETE 基本構文の状態と出力メッセージを結び付ける出力確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の基本構文に関する記録は、DELETE 基本構文の出力行と ISF031I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため出力確認ではありません。 B: 出力確認の基本構文は別カテゴリの確認を流用しており、DELETE 基本構文の根拠にならないため出力確認ではありません。 C: 出力確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の基本構文は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の基本構文で記録する DELETE 基本構文は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DELETE 基本構文**

    - 検証目的: 範囲検査の基本構文について、DELETE 基本構文は、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、範囲検査の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDELETE 基本構文を指定し、OSKB010071の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DELETE 基本構文
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DELETE 基本構文
    CASE OSKB010071
    SOURCE TSO ISPF SDSF
    ```

    DELETE 基本構文とOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010071を同じ出力で読み、範囲検査の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010071
    COMMAND ===> SDSF DA
    ISF031I DELETE 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DELETE 基本構文 と OSKB010071 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### RENAME ALIAS オペランド {#c30-i0262}
*分類: TSO_DEL_REN*  ・  難易度: 中級

RENAME ALIAS オペランドは、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のオペランドに関係する RENAME ALIAS オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告確認として引き継ぐ。 ✅
    - B. RENAME ALIAS オペランドの名称と担当者名のみを残して警告確認のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で警告確認のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず警告確認のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認のオペランドにおいて選択記号 A を採用し、識別名は警告確認です。警告確認のオペランドにおいて RENAME ALIAS オペランド は説明欄の「RENAME ALIAS オペランドの用途を対話操作の表示で確認する警告確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のオペランドに関連して、TSO ISPF SDSF では RENAME ALIAS オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のオペランドは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のオペランドは別カテゴリの確認を流用しており、RENAME ALIAS オペランドの根拠にならないため警告確認ではありません。 D: 警告確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため警告確認ではありません。警告確認のオペランドで使う RENAME ALIAS オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は警告確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **RENAME ALIAS オペランド**

    - 検証目的: 変更検査のオペランドについて、RENAME ALIAS オペランドは、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010080の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更検査のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRENAME ALIAS オペランドを指定し、OSKB010080の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RENAME ALIAS オペランド
    CASE OSKB010080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RENAME ALIAS オペランド
    CASE OSKB010080
    SOURCE TSO ISPF SDSF
    ```

    RENAME ALIAS オペランドとOSKB010080が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010080を同じ出力で読み、変更検査のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010080
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010080
    COMMAND ===> SDSF DA
    ISF031I RENAME ALIAS オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010080が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RENAME ALIAS オペランド と OSKB010080 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### RENAME メンバ単位 {#c30-i0263}
*分類: TSO_DEL_REN*  ・  難易度: 中級

RENAME メンバ単位は、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 値域確認のメンバ単位に関する RENAME メンバ単位の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず値域確認のメンバ単位の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のメンバ単位の証跡として保存して根拠にする。
    - C. RENAME メンバ単位の変更点を出力本文から切り離して値域確認のメンバ単位の承認欄のみ残す。
    - D. SDSF DA で得た表示本文を使い、値域確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認のメンバ単位において選択記号 D を採用し、識別名は値域確認です。値域確認のメンバ単位において RENAME メンバ単位 は説明欄の「RENAME メンバ単位の状態と出力メッセージを結び付ける値域確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認のメンバ単位に関する記録は、RENAME メンバ単位の出力行と ISF031I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認のメンバ単位は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため値域確認ではありません。 B: 値域確認のメンバ単位は別カテゴリの確認を流用しており、RENAME メンバ単位の根拠にならないため値域確認ではありません。 C: 値域確認のメンバ単位は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認のメンバ単位は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認のメンバ単位で記録する RENAME メンバ単位は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **RENAME メンバ単位**

    - 検証目的: 監査検査のメンバ単位について、RENAME メンバ単位は、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、監査検査のメンバ単位の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRENAME メンバ単位を指定し、OSKB010079の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RENAME メンバ単位
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RENAME メンバ単位
    CASE OSKB010079
    SOURCE TSO ISPF SDSF
    ```

    RENAME メンバ単位とOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010079を同じ出力で読み、監査検査のメンバ単位の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010079
    COMMAND ===> SDSF DA
    ISF031I RENAME メンバ単位 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RENAME メンバ単位 と OSKB010079 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### RENAME 基本構文 {#c30-i0264}
*分類: TSO_DEL_REN*  ・  難易度: 初級

RENAME 基本構文は、TSO / ISPF / SDSFのTSO_DEL_RENで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 比較確認の基本構文で RENAME 基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RENAME 基本構文の出力を取らず比較確認の基本構文の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較確認の根拠にする。 ✅
    - C. SDSF DA を省略して比較確認の基本構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 比較確認の基本構文において選択記号 B を採用し、識別名は比較確認です。比較確認の基本構文において RENAME 基本構文 は説明欄の「比較確認の基本構文に関係する定義値と表示行を照合する比較確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の基本構文の証跡を読む担当者は、RENAME 基本構文の属性行と ISF031I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の基本構文は対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため比較確認ではありません。 D: 比較確認の基本構文は別カテゴリの確認を流用しており、RENAME 基本構文の根拠にならないため比較確認ではありません。比較確認の基本構文に出る RENAME 基本構文は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は比較確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **RENAME 基本構文**

    - 検証目的: 警告検査の基本構文について、RENAME 基本構文は、TSO / ISPF / SDSF の TSO_DEL_REN で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010077の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告検査の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRENAME 基本構文を指定し、OSKB010077の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RENAME 基本構文
    CASE OSKB010077
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RENAME 基本構文
    CASE OSKB010077
    SOURCE TSO ISPF SDSF
    ```

    RENAME 基本構文とOSKB010077が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010077を同じ出力で読み、警告検査の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010077
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010077
    COMMAND ===> SDSF DA
    ISF031I RENAME 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010077が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RENAME 基本構文 と OSKB010077 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### RENAME 旧名 新名 {#c30-i0265}
*分類: TSO_DEL_REN*  ・  難易度: 中級

RENAME 旧名 新名は、TSO / ISPF / SDSFのTSO_DEL_RENで確認する項目です。シングルクォート/プレフィックス補完規則は他コマンドと同じ。VSAM クラスタ全体改名は AMS が必要なケースも

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 順序確認の旧名 新名で対話操作の運用確認を行います。RENAME 旧名 新名の根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で順序確認の旧名 新名を確認した扱いにする。
    - B. ISF031I の有無を確認せず順序確認の旧名 新名を正常終了として記録する。
    - C. 同じ画面で対象行と ISF031I を読み、順序確認の結果として保存する。 ✅
    - D. RENAME 旧名 新名の属性行を読まず順序確認の旧名 新名の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認の旧名 新名において選択記号 C を採用し、識別名は順序確認です。順序確認の旧名 新名において RENAME 旧名 新名 は説明欄の「TSO ISPF SDSF で RENAME 旧名 新名の扱いを記録する順序確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の旧名 新名を受け取る担当者は、RENAME 旧名 新名の表示結果と ISF031I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の旧名 新名は別カテゴリの確認を流用しており、RENAME 旧名 新名の根拠にならないため順序確認ではありません。 B: 順序確認の旧名 新名は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため順序確認ではありません。 C: 順序確認の旧名 新名は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の旧名 新名は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の旧名 新名が示す RENAME 旧名 新名は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **RENAME 旧名 新名**

    - 検証目的: 復旧検査の旧名 新名について、RENAME 旧名 新名は、TSO / ISPF / SDSF の TSO_DEL_REN で確認する項目です。シングルクォート/プレフィックス補完規則は他コマンドと同じ。VSAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、復旧検査の旧名 新名の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にRENAME 旧名 新名を指定し、OSKB010078の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND RENAME 旧名 新名
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM RENAME 旧名 新名
    CASE OSKB010078
    SOURCE TSO ISPF SDSF
    ```

    RENAME 旧名 新名とOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010078を同じ出力で読み、復旧検査の旧名 新名の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010078
    COMMAND ===> SDSF DA
    ISF031I RENAME 旧名 新名 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の RENAME 旧名 新名 と OSKB010078 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference




## TSO / ISPF / SDSF > TSO_FREE

### FREE ALL オペランド {#c30-i0266}
*分類: TSO_FREE*  ・  難易度: 中級

FREE ALL オペランドは、TSO / ISPF / SDSFのTSO_FREEで確認する項目です。ユーザ動的割当のうち、属性 NOHOLD のすべての DD を一括解除。ログオン プロシージャの DD は対象外

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 構文照合のオペランドに関係する FREE ALL オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文照合で再確認できる形にする。 ✅
    - B. FREE ALL オペランドの名称と担当者名のみを残して構文照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で構文照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず構文照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合のオペランドにおいて選択記号 A を採用し、識別名は構文照合です。構文照合のオペランドにおいて FREE ALL オペランド は説明欄の「FREE ALL オペランドの用途を対話操作の表示で確認する構文照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のオペランドに関連して、TSO ISPF SDSF では FREE ALL オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のオペランドは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のオペランドは別カテゴリの確認を流用しており、FREE ALL オペランドの根拠にならないため構文照合ではありません。 D: 構文照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため構文照合ではありません。構文照合のオペランドで使う FREE ALL オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE ALL オペランド**

    - 検証目的: 比較照合のオペランドについて、FREE ALL オペランドは、TSO / ISPF / SDSF の TSO_FREE で確認する項目です。ユーザ動的割当のうち、属性 NOHOLD のすべての DD を一括解に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010034の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、比較照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE ALL オペランドを指定し、OSKB010034の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE ALL オペランド
    CASE OSKB010034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE ALL オペランド
    CASE OSKB010034
    SOURCE TSO ISPF SDSF
    ```

    FREE ALL オペランドとOSKB010034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010034を同じ出力で読み、比較照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010034
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010034
    COMMAND ===> SDSF DA
    ISF031I FREE ALL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE ALL オペランド と OSKB010034 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE ATTRLIST オペランド {#c30-i0267}
*分類: TSO_FREE*  ・  難易度: 中級

FREE ATTRLIST オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 展開照合のオペランドで FREE ATTRLIST オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FREE ATTRLIST オペランドの出力を取らず展開照合のオペランドの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開照合の確認値として扱う。 ✅
    - C. SDSF DA を省略して展開照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合のオペランドにおいて選択記号 B を採用し、識別名は展開照合です。展開照合のオペランドにおいて FREE ATTRLIST オペランド は説明欄の「展開照合のオペランドに関係する定義値と表示行を照合する展開照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合のオペランドの証跡を読む担当者は、FREE ATTRLIST オペランドの属性行と ISF031I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合のオペランドは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため展開照合ではありません。 D: 展開照合のオペランドは別カテゴリの確認を流用しており、FREE ATTRLIST オペランドの根拠にならないため展開照合ではありません。展開照合のオペランドに出る FREE ATTRLIST オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE ATTRLIST オペランド**

    - 検証目的: 順序照合のオペランドについて、FREE ATTRLIST オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010035の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、順序照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE ATTRLIST オペランを指定し、OSKB010035の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE ATTRLIST オペラン
    CASE OSKB010035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE ATTRLIST オペラン
    CASE OSKB010035
    SOURCE TSO ISPF SDSF
    ```

    FREE ATTRLIST オペランとOSKB010035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010035を同じ出力で読み、順序照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010035
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010035
    COMMAND ===> SDSF DA
    ISF031I FREE ATTRLIST オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE ATTRLIST オペラン と OSKB010035 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE CATALOG オペランド {#c30-i0268}
*分類: TSO_FREE*  ・  難易度: 中級

FREE CATALOG オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 終端照合のオペランドに関係する FREE CATALOG オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SDSF DA の結果から対象行を抜き出し、終端照合の証跡として残す。 ✅
    - B. FREE CATALOG オペランドの名称と担当者名のみを残して終端照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で終端照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず終端照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合のオペランドにおいて選択記号 A を採用し、識別名は終端照合です。終端照合のオペランドにおいて FREE CATALOG オペランド は説明欄の「FREE CATALOG オペランドの用途を対話操作の表示で確認する終端照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合のオペランドに関連して、TSO ISPF SDSF では FREE CATALOG オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合のオペランドは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合のオペランドは別カテゴリの確認を流用しており、FREE CATALOG オペランドの根拠にならないため終端照合ではありません。 D: 終端照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため終端照合ではありません。終端照合のオペランドで使う FREE CATALOG オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE CATALOG オペランド**

    - 検証目的: 復旧照合のオペランドについて、FREE CATALOG オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010038の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、復旧照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE CATALOG オペランドを指定し、OSKB010038の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE CATALOG オペランド
    CASE OSKB010038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE CATALOG オペランド
    CASE OSKB010038
    SOURCE TSO ISPF SDSF
    ```

    FREE CATALOG オペランドとOSKB010038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010038を同じ出力で読み、復旧照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010038
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010038
    COMMAND ===> SDSF DA
    ISF031I FREE CATALOG オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE CATALOG オペランド と OSKB010038 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE DATASET オペランド {#c30-i0269}
*分類: TSO_FREE*  ・  難易度: 中級

FREE DATASET オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 監査確認のオペランドで対話操作の運用確認を行います。FREE DATASET オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で監査確認のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず監査確認のオペランドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 ✅
    - D. FREE DATASET オペランドの属性行を読まず監査確認のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認のオペランドにおいて選択記号 C を採用し、識別名は監査確認です。監査確認のオペランドにおいて FREE DATASET オペランド は説明欄の「TSO ISPF SDSF で FREE DATASET オペランドの扱いを記録する監査確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のオペランドを受け取る担当者は、FREE DATASET オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のオペランドは別カテゴリの確認を流用しており、FREE DATASET オペランドの根拠にならないため監査確認ではありません。 B: 監査確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため監査確認ではありません。 C: 監査確認のオペランドは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のオペランドが示す FREE DATASET オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE DATASET オペランド**

    - 検証目的: 優先照合のオペランドについて、FREE DATASET オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010032の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、優先照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE DATASET オペランドを指定し、OSKB010032の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE DATASET オペランド
    CASE OSKB010032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE DATASET オペランド
    CASE OSKB010032
    SOURCE TSO ISPF SDSF
    ```

    FREE DATASET オペランドとOSKB010032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010032を同じ出力で読み、優先照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010032
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010032
    COMMAND ===> SDSF DA
    ISF031I FREE DATASET オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE DATASET オペランド と OSKB010032 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE DELETE オペランド {#c30-i0270}
*分類: TSO_FREE*  ・  難易度: 中級

FREE DELETE オペランドは、TSO / ISPF / SDSFのTSO_FREEで確認する項目です。解除時にデータセットを削除する後処理を上書き指定。元の ALLOCATE で DELETE を指定し忘れたときに使う

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出照合のオペランドで対話操作の運用確認を行います。FREE DELETE オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で呼出照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず呼出照合のオペランドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出照合の根拠を固定する。 ✅
    - D. FREE DELETE オペランドの属性行を読まず呼出照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合のオペランドにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合のオペランドにおいて FREE DELETE オペランド は説明欄の「TSO ISPF SDSF で FREE DELETE オペランドの扱いを記録する呼出照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のオペランドを受け取る担当者は、FREE DELETE オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のオペランドは別カテゴリの確認を流用しており、FREE DELETE オペランドの根拠にならないため呼出照合ではありません。 B: 呼出照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のオペランドは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のオペランドが示す FREE DELETE オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE DELETE オペランド**

    - 検証目的: 値域照合のオペランドについて、FREE DELETE オペランドは、TSO / ISPF / SDSF の TSO_FREE で確認する項目です。解除時にデータセットを削除する後処理を上書き指定。元の ALLに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010036の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE DELETE オペランドを指定し、OSKB010036の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE DELETE オペランド
    CASE OSKB010036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE DELETE オペランド
    CASE OSKB010036
    SOURCE TSO ISPF SDSF
    ```

    FREE DELETE オペランドとOSKB010036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010036を同じ出力で読み、値域照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010036
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010036
    COMMAND ===> SDSF DA
    ISF031I FREE DELETE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE DELETE オペランド と OSKB010036 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE FILE オペランド {#c30-i0271}
*分類: TSO_FREE*  ・  難易度: 中級

FREE FILE オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 変更確認のオペランドに関する FREE FILE オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず変更確認のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のオペランドの証跡として保存して根拠にする。
    - C. FREE FILE オペランドの変更点を出力本文から切り離して変更確認のオペランドの承認欄のみ残す。
    - D. TSO ISPF SDSF の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認のオペランドにおいて選択記号 D を採用し、識別名は変更確認です。変更確認のオペランドにおいて FREE FILE オペランド は説明欄の「FREE FILE オペランドの状態と出力メッセージを結び付ける変更確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のオペランドに関する記録は、FREE FILE オペランドの出力行と ISF031I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため変更確認ではありません。 B: 変更確認のオペランドは別カテゴリの確認を流用しており、FREE FILE オペランドの根拠にならないため変更確認ではありません。 C: 変更確認のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のオペランドは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のオペランドで記録する FREE FILE オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE FILE オペランド**

    - 検証目的: 記録照合のオペランドについて、FREE FILE オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010033の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、記録照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE FILE オペランドを指定し、OSKB010033の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE FILE オペランド
    CASE OSKB010033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE FILE オペランド
    CASE OSKB010033
    SOURCE TSO ISPF SDSF
    ```

    FREE FILE オペランドとOSKB010033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010033を同じ出力で読み、記録照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010033
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010033
    COMMAND ===> SDSF DA
    ISF031I FREE FILE オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE FILE オペランド と OSKB010033 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE KEEP オペランド {#c30-i0272}
*分類: TSO_FREE*  ・  難易度: 中級

FREE KEEP オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 置換照合のオペランドに関する FREE KEEP オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず置換照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のオペランドの証跡として保存して根拠にする。
    - C. FREE KEEP オペランドの変更点を出力本文から切り離して置換照合のオペランドの承認欄のみ残す。
    - D. ISF031I を含む表示を保存し、説明欄との差分を置換照合で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合のオペランドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合のオペランドにおいて FREE KEEP オペランド は説明欄の「FREE KEEP オペランドの状態と出力メッセージを結び付ける置換照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のオペランドに関する記録は、FREE KEEP オペランドの出力行と ISF031I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため置換照合ではありません。 B: 置換照合のオペランドは別カテゴリの確認を流用しており、FREE KEEP オペランドの根拠にならないため置換照合ではありません。 C: 置換照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のオペランドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のオペランドで記録する FREE KEEP オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE KEEP オペランド**

    - 検証目的: 警告照合のオペランドについて、FREE KEEP オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010037の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE KEEP オペランドを指定し、OSKB010037の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE KEEP オペランド
    CASE OSKB010037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE KEEP オペランド
    CASE OSKB010037
    SOURCE TSO ISPF SDSF
    ```

    FREE KEEP オペランドとOSKB010037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010037を同じ出力で読み、警告照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010037
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010037
    COMMAND ===> SDSF DA
    ISF031I FREE KEEP オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE KEEP オペランド と OSKB010037 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE SYSOUT オペランド {#c30-i0273}
*分類: TSO_FREE*  ・  難易度: 中級

FREE SYSOUT オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 上書照合のオペランドで対話操作の運用確認を行います。FREE SYSOUT オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で上書照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず上書照合のオペランドを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書照合の根拠にする。 ✅
    - D. FREE SYSOUT オペランドの属性行を読まず上書照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合のオペランドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合のオペランドにおいて FREE SYSOUT オペランド は説明欄の「TSO ISPF SDSF で FREE SYSOUT オペランドの扱いを記録する上書照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のオペランドを受け取る担当者は、FREE SYSOUT オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のオペランドは別カテゴリの確認を流用しており、FREE SYSOUT オペランドの根拠にならないため上書照合ではありません。 B: 上書照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため上書照合ではありません。 C: 上書照合のオペランドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のオペランドが示す FREE SYSOUT オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE SYSOUT オペランド**

    - 検証目的: 変更照合のオペランドについて、FREE SYSOUT オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE SYSOUT オペランドを指定し、OSKB010040の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE SYSOUT オペランド
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE SYSOUT オペランド
    CASE OSKB010040
    SOURCE TSO ISPF SDSF
    ```

    FREE SYSOUT オペランドとOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010040を同じ出力で読み、変更照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010040
    COMMAND ===> SDSF DA
    ISF031I FREE SYSOUT オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE SYSOUT オペランド と OSKB010040 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE UNCATALOG オペランド {#c30-i0274}
*分類: TSO_FREE*  ・  難易度: 中級

FREE UNCATALOG オペランドは、TSO / ISPF / SDSFのTSO_FREEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 探索照合のオペランドで FREE UNCATALOG オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FREE UNCATALOG オペランドの出力を取らず探索照合のオペランドの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索照合の確認記録にまとめる。 ✅
    - C. SDSF DA を省略して探索照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合のオペランドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合のオペランドにおいて FREE UNCATALOG オペランド は説明欄の「探索照合のオペランドに関係する定義値と表示行を照合する探索照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のオペランドの証跡を読む担当者は、FREE UNCATALOG オペランドの属性行と ISF031I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のオペランドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため探索照合ではありません。 D: 探索照合のオペランドは別カテゴリの確認を流用しており、FREE UNCATALOG オペランドの根拠にならないため探索照合ではありません。探索照合のオペランドに出る FREE UNCATALOG オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE UNCATALOG オペランド**

    - 検証目的: 監査照合のオペランドについて、FREE UNCATALOG オペランドは、TSO / ISPF / SDSF の TSO_FREE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010039の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、監査照合のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE UNCATALOG オペラを指定し、OSKB010039の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE UNCATALOG オペラ
    CASE OSKB010039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE UNCATALOG オペラ
    CASE OSKB010039
    SOURCE TSO ISPF SDSF
    ```

    FREE UNCATALOG オペラとOSKB010039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010039を同じ出力で読み、監査照合のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010039
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010039
    COMMAND ===> SDSF DA
    ISF031I FREE UNCATALOG オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE UNCATALOG オペラ と OSKB010039 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### FREE 基本構文 {#c30-i0275}
*分類: TSO_FREE*  ・  難易度: 初級

FREE 基本構文は、TSO / ISPF / SDSFのTSO_FREEで確認する項目です。ALLOCATE で割り当てた DD を解除するコマンド (省略形 FREE)。プログラム実行中はクローズ後に解除すべき

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 復旧確認の基本構文で FREE 基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FREE 基本構文の出力を取らず復旧確認の基本構文の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 ✅
    - C. SDSF DA を省略して復旧確認の基本構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧確認の基本構文において選択記号 B を採用し、識別名は復旧確認です。復旧確認の基本構文において FREE 基本構文 は説明欄の「復旧確認の基本構文に関係する定義値と表示行を照合する復旧確認項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の基本構文の証跡を読む担当者は、FREE 基本構文の属性行と ISF031I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の基本構文は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の基本構文は別カテゴリの確認を流用しており、FREE 基本構文の根拠にならないため復旧確認ではありません。復旧確認の基本構文に出る FREE 基本構文は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **FREE 基本構文**

    - 検証目的: 範囲照合の基本構文について、FREE 基本構文は、TSO / ISPF / SDSF の TSO_FREE で確認する項目です。ALLOCATE で割り当てた DD を解除するコマンド (省略形 FREE)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010031の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、範囲照合の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にFREE 基本構文を指定し、OSKB010031の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND FREE 基本構文
    CASE OSKB010031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM FREE 基本構文
    CASE OSKB010031
    SOURCE TSO ISPF SDSF
    ```

    FREE 基本構文とOSKB010031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010031を同じ出力で読み、範囲照合の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010031
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010031
    COMMAND ===> SDSF DA
    ISF031I FREE 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の FREE 基本構文 と OSKB010031 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference




## TSO / ISPF / SDSF > TSO_LIST

### LISTALC HISTORY オペランド {#c30-i0276}
*分類: TSO_LIST*  ・  難易度: 中級

LISTALC HISTORY オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 探索追跡のオペランドで LISTALC HISTORY オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LISTALC HISTORY オペランドの出力を取らず探索追跡のオペランドの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索追跡の確認値として扱う。 ✅
    - C. SDSF DA を省略して探索追跡のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡のオペランドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡のオペランドにおいて LISTALC HISTORY オペランド は説明欄の「探索追跡のオペランドに関係する定義値と表示行を照合する探索追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のオペランドの証跡を読む担当者は、LISTALC HISTORY オペランドの属性行と ISF031I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のオペランドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のオペランドは別カテゴリの確認を流用しており、LISTALC HISTORY オペランドの根拠にならないため探索追跡ではありません。探索追跡のオペランドに出る LISTALC HISTORY オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTALC HISTORY オペランド**

    - 検証目的: 監査追跡のオペランドについて、LISTALC HISTORY オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、監査追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTALC HISTORY オペを指定し、OSKB010059の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTALC HISTORY オペ
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTALC HISTORY オペ
    CASE OSKB010059
    SOURCE TSO ISPF SDSF
    ```

    LISTALC HISTORY オペとOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010059を同じ出力で読み、監査追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010059
    COMMAND ===> SDSF DA
    ISF031I LISTALC HISTORY オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTALC HISTORY オペ と OSKB010059 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTALC STATUS オペランド {#c30-i0277}
*分類: TSO_LIST*  ・  難易度: 中級

LISTALC STATUS オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 終端追跡のオペランドに関係する LISTALC STATUS オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端追跡で再確認できる形にする。 ✅
    - B. LISTALC STATUS オペランドの名称と担当者名のみを残して終端追跡のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で終端追跡のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず終端追跡のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡のオペランドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡のオペランドにおいて LISTALC STATUS オペランド は説明欄の「LISTALC STATUS オペランドの用途を対話操作の表示で確認する終端追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のオペランドに関連して、TSO ISPF SDSF では LISTALC STATUS オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のオペランドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のオペランドは別カテゴリの確認を流用しており、LISTALC STATUS オペランドの根拠にならないため終端追跡ではありません。 D: 終端追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため終端追跡ではありません。終端追跡のオペランドで使う LISTALC STATUS オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTALC STATUS オペランド**

    - 検証目的: 復旧追跡のオペランドについて、LISTALC STATUS オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、復旧追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTALC STATUS オペラを指定し、OSKB010058の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTALC STATUS オペラ
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTALC STATUS オペラ
    CASE OSKB010058
    SOURCE TSO ISPF SDSF
    ```

    LISTALC STATUS オペラとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010058を同じ出力で読み、復旧追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010058
    COMMAND ===> SDSF DA
    ISF031I LISTALC STATUS オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTALC STATUS オペラ と OSKB010058 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTALC SYSNAMES オペランド {#c30-i0278}
*分類: TSO_LIST*  ・  難易度: 中級

LISTALC SYSNAMES オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 上書追跡のオペランドで対話操作の運用確認を行います。LISTALC SYSNAMES オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で上書追跡のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず上書追跡のオペランドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書追跡の根拠を固定する。 ✅
    - D. LISTALC SYSNAMES オペランドの属性行を読まず上書追跡のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のオペランドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のオペランドにおいて LISTALC SYSNAMES オペランド は説明欄の「TSO ISPF SDSF で LISTALC SYSNAMES オペランドの扱いを記録する上書追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のオペランドを受け取る担当者は、LISTALC SYSNAMES オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のオペランドは別カテゴリの確認を流用しており、LISTALC SYSNAMES オペランドの根拠にならないため上書追跡ではありません。 B: 上書追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のオペランドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のオペランドが示す LISTALC SYSNAMES オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTALC SYSNAMES オペランド**

    - 検証目的: 変更追跡のオペランドについて、LISTALC SYSNAMES オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTALC SYSNAMES オを指定し、OSKB010060の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTALC SYSNAMES オ
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTALC SYSNAMES オ
    CASE OSKB010060
    SOURCE TSO ISPF SDSF
    ```

    LISTALC SYSNAMES オとOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010060を同じ出力で読み、変更追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010060
    COMMAND ===> SDSF DA
    ISF031I LISTALC SYSNAMES オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTALC SYSNAMES オ と OSKB010060 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTALC コマンド {#c30-i0279}
*分類: TSO_LIST*  ・  難易度: 中級

LISTALC コマンドは、TSO / ISPF / SDSFのTSO_LISTで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 置換追跡のコマンドに関する LISTALC コマンドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず置換追跡のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のコマンドの証跡として保存して根拠にする。
    - C. LISTALC コマンドの変更点を出力本文から切り離して置換追跡のコマンドの承認欄のみ残す。
    - D. TSO ISPF SDSF の表示形式に沿って根拠行を採り、置換追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡のコマンドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のコマンドにおいて LISTALC コマンド は説明欄の「LISTALC コマンドの状態と出力メッセージを結び付ける置換追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のコマンドに関する記録は、LISTALC コマンドの出力行と ISF031I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のコマンドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のコマンドは別カテゴリの確認を流用しており、LISTALC コマンドの根拠にならないため置換追跡ではありません。 C: 置換追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のコマンドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のコマンドで記録する LISTALC コマンドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTALC コマンド**

    - 検証目的: 警告追跡のコマンドについて、LISTALC コマンドは、TSO / ISPF / SDSF の TSO_LIST で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告追跡のコマンドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTALC コマンドを指定し、OSKB010057の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTALC コマンド
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTALC コマンド
    CASE OSKB010057
    SOURCE TSO ISPF SDSF
    ```

    LISTALC コマンドとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010057を同じ出力で読み、警告追跡のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010057
    COMMAND ===> SDSF DA
    ISF031I LISTALC コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTALC コマンド と OSKB010057 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTBC MAIL オペランド {#c30-i0280}
*分類: TSO_LIST*  ・  難易度: 中級

LISTBC MAIL オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出追跡のオペランドで対話操作の運用確認を行います。LISTBC MAIL オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で呼出追跡のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず呼出追跡のオペランドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 ✅
    - D. LISTBC MAIL オペランドの属性行を読まず呼出追跡のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡のオペランドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のオペランドにおいて LISTBC MAIL オペランド は説明欄の「TSO ISPF SDSF で LISTBC MAIL オペランドの扱いを記録する呼出追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のオペランドを受け取る担当者は、LISTBC MAIL オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のオペランドは別カテゴリの確認を流用しており、LISTBC MAIL オペランドの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のオペランドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のオペランドが示す LISTBC MAIL オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTBC MAIL オペランド**

    - 検証目的: 値域追跡のオペランドについて、LISTBC MAIL オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、値域追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTBC MAIL オペランドを指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTBC MAIL オペランド
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTBC MAIL オペランド
    CASE OSKB010056
    SOURCE TSO ISPF SDSF
    ```

    LISTBC MAIL オペランドとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010056を同じ出力で読み、値域追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010056
    COMMAND ===> SDSF DA
    ISF031I LISTBC MAIL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTBC MAIL オペランド と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTBC NOTICES オペランド {#c30-i0281}
*分類: TSO_LIST*  ・  難易度: 中級

LISTBC NOTICES オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 展開追跡のオペランドで LISTBC NOTICES オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LISTBC NOTICES オペランドの出力を取らず展開追跡のオペランドの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開追跡として引き継ぐ。 ✅
    - C. SDSF DA を省略して展開追跡のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡のオペランドにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のオペランドにおいて LISTBC NOTICES オペランド は説明欄の「展開追跡のオペランドに関係する定義値と表示行を照合する展開追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のオペランドの証跡を読む担当者は、LISTBC NOTICES オペランドの属性行と ISF031I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のオペランドは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のオペランドは別カテゴリの確認を流用しており、LISTBC NOTICES オペランドの根拠にならないため展開追跡ではありません。展開追跡のオペランドに出る LISTBC NOTICES オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTBC NOTICES オペランド**

    - 検証目的: 順序追跡のオペランドについて、LISTBC NOTICES オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、順序追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTBC NOTICES オペラを指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTBC NOTICES オペラ
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTBC NOTICES オペラ
    CASE OSKB010055
    SOURCE TSO ISPF SDSF
    ```

    LISTBC NOTICES オペラとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010055を同じ出力で読み、順序追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010055
    COMMAND ===> SDSF DA
    ISF031I LISTBC NOTICES オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTBC NOTICES オペラ と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTBC コマンド {#c30-i0282}
*分類: TSO_LIST*  ・  難易度: 中級

LISTBC コマンドは、TSO / ISPF / SDSFのTSO_LISTで確認する項目です。システム共通通知 (Broadcast Data Set 内のメッセージ) を表示。ログオン直後にも自動表示される

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 構文追跡のコマンドに関係する LISTBC コマンドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SDSF DA で得た表示本文を使い、構文追跡の採否を説明欄に結び付ける。 ✅
    - B. LISTBC コマンドの名称と担当者名のみを残して構文追跡のコマンドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で構文追跡のコマンドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず構文追跡のコマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡のコマンドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のコマンドにおいて LISTBC コマンド は説明欄の「LISTBC コマンドの用途を対話操作の表示で確認する構文追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のコマンドに関連して、TSO ISPF SDSF では LISTBC コマンドの表示属性と ISF031I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のコマンドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のコマンドは別カテゴリの確認を流用しており、LISTBC コマンドの根拠にならないため構文追跡ではありません。 D: 構文追跡のコマンドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため構文追跡ではありません。構文追跡のコマンドで使う LISTBC コマンドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は構文追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTBC コマンド**

    - 検証目的: 比較追跡のコマンドについて、LISTBC コマンドは、TSO / ISPF / SDSF の TSO_LIST で確認する項目です。システム共通通知 (Broadcast Data Set 内のメッセージ)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、比較追跡のコマンドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTBC コマンドを指定し、OSKB010054の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTBC コマンド
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTBC コマンド
    CASE OSKB010054
    SOURCE TSO ISPF SDSF
    ```

    LISTBC コマンドとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010054を同じ出力で読み、比較追跡のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010054
    COMMAND ===> SDSF DA
    ISF031I LISTBC コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTBC コマンド と OSKB010054 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT ALL オペランド {#c30-i0283}
*分類: TSO_LIST*  ・  難易度: 中級

LISTCAT ALL オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 警告照合のオペランドに関係する LISTCAT ALL オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SDSF DA の結果から対象行を抜き出し、警告照合の証跡として残す。 ✅
    - B. LISTCAT ALL オペランドの名称と担当者名のみを残して警告照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で警告照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず警告照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合のオペランドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のオペランドにおいて LISTCAT ALL オペランド は説明欄の「LISTCAT ALL オペランドの用途を対話操作の表示で確認する警告照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のオペランドに関連して、TSO ISPF SDSF では LISTCAT ALL オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のオペランドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のオペランドは別カテゴリの確認を流用しており、LISTCAT ALL オペランドの根拠にならないため警告照合ではありません。 D: 警告照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため警告照合ではありません。警告照合のオペランドで使う LISTCAT ALL オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は警告照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT ALL オペランド**

    - 検証目的: 区切追跡のオペランドについて、LISTCAT ALL オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、区切追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT ALL オペランドを指定し、OSKB010050の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT ALL オペランド
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT ALL オペランド
    CASE OSKB010050
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT ALL オペランドとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010050を同じ出力で読み、区切追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010050
    COMMAND ===> SDSF DA
    ISF031I LISTCAT ALL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT ALL オペランド と OSKB010050 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT ALLOCATION オペランド {#c30-i0284}
*分類: TSO_LIST*  ・  難易度: 中級

LISTCAT ALLOCATION オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 変更照合のオペランドに関する LISTCAT ALLOCATION オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず変更照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のオペランドの証跡として保存して根拠にする。
    - C. LISTCAT ALLOCATION オペランドの変更点を出力本文から切り離して変更照合のオペランドの承認欄のみ残す。
    - D. 同じ画面で対象行と ISF031I を読み、変更照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合のオペランドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合のオペランドにおいて LISTCAT ALLOCATION オペランド は説明欄の「LISTCAT ALLOCATION オペランドの状態と出力メッセージを結び付ける変更照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のオペランドに関する記録は、LISTCAT ALLOCATION オペランドの出力行と ISF031I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため変更照合ではありません。 B: 変更照合のオペランドは別カテゴリの確認を流用しており、LISTCAT ALLOCATION オペランドの根拠にならないため変更照合ではありません。 C: 変更照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のオペランドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のオペランドで記録する LISTCAT ALLOCATION オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT ALLOCATION オペランド**

    - 検証目的: 記録追跡のオペランドについて、LISTCAT ALLOCATION オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、記録追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT ALLOCATIONを指定し、OSKB010053の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT ALLOCATION
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT ALLOCATION
    CASE OSKB010053
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT ALLOCATIONとOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010053を同じ出力で読み、記録追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010053
    COMMAND ===> SDSF DA
    ISF031I LISTCAT ALLOCATION オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT ALLOCATION と OSKB010053 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT ENTRIES オペランド {#c30-i0285}
*分類: TSO_LIST*  ・  難易度: 中級

LISTCAT ENTRIES オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 順序照合のオペランドで対話操作の運用確認を行います。LISTCAT ENTRIES オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で順序照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず順序照合のオペランドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序照合の根拠を固定する。 ✅
    - D. LISTCAT ENTRIES オペランドの属性行を読まず順序照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合のオペランドにおいて選択記号 C を採用し、識別名は順序照合です。順序照合のオペランドにおいて LISTCAT ENTRIES オペランド は説明欄の「TSO ISPF SDSF で LISTCAT ENTRIES オペランドの扱いを記録する順序照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のオペランドを受け取る担当者は、LISTCAT ENTRIES オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のオペランドは別カテゴリの確認を流用しており、LISTCAT ENTRIES オペランドの根拠にならないため順序照合ではありません。 B: 順序照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため順序照合ではありません。 C: 順序照合のオペランドは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のオペランドが示す LISTCAT ENTRIES オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT ENTRIES オペランド**

    - 検証目的: 出力追跡のオペランドについて、LISTCAT ENTRIES オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、出力追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT ENTRIES オペを指定し、OSKB010048の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT ENTRIES オペ
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT ENTRIES オペ
    CASE OSKB010048
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT ENTRIES オペとOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010048を同じ出力で読み、出力追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010048
    COMMAND ===> SDSF DA
    ISF031I LISTCAT ENTRIES オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT ENTRIES オペ と OSKB010048 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT HISTORY オペランド {#c30-i0286}
*分類: TSO_LIST*  ・  難易度: 中級

LISTCAT HISTORY オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 監査照合のオペランドで対話操作の運用確認を行います。LISTCAT HISTORY オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で監査照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず監査照合のオペランドを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査照合の根拠にする。 ✅
    - D. LISTCAT HISTORY オペランドの属性行を読まず監査照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合のオペランドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合のオペランドにおいて LISTCAT HISTORY オペランド は説明欄の「TSO ISPF SDSF で LISTCAT HISTORY オペランドの扱いを記録する監査照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のオペランドを受け取る担当者は、LISTCAT HISTORY オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のオペランドは別カテゴリの確認を流用しており、LISTCAT HISTORY オペランドの根拠にならないため監査照合ではありません。 B: 監査照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため監査照合ではありません。 C: 監査照合のオペランドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のオペランドが示す LISTCAT HISTORY オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT HISTORY オペランド**

    - 検証目的: 優先追跡のオペランドについて、LISTCAT HISTORY オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、優先追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT HISTORY オペを指定し、OSKB010052の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT HISTORY オペ
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT HISTORY オペ
    CASE OSKB010052
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT HISTORY オペとOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010052を同じ出力で読み、優先追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010052
    COMMAND ===> SDSF DA
    ISF031I LISTCAT HISTORY オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT HISTORY オペ と OSKB010052 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT LEVEL オペランド {#c30-i0287}
*分類: TSO_LIST*  ・  難易度: 中級

LISTCAT LEVEL オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 値域照合のオペランドに関する LISTCAT LEVEL オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず値域照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のオペランドの証跡として保存して根拠にする。
    - C. LISTCAT LEVEL オペランドの変更点を出力本文から切り離して値域照合のオペランドの承認欄のみ残す。
    - D. ISF031I を含む表示を保存し、説明欄との差分を値域照合で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合のオペランドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合のオペランドにおいて LISTCAT LEVEL オペランド は説明欄の「LISTCAT LEVEL オペランドの状態と出力メッセージを結び付ける値域照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のオペランドに関する記録は、LISTCAT LEVEL オペランドの出力行と ISF031I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため値域照合ではありません。 B: 値域照合のオペランドは別カテゴリの確認を流用しており、LISTCAT LEVEL オペランドの根拠にならないため値域照合ではありません。 C: 値域照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のオペランドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のオペランドで記録する LISTCAT LEVEL オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT LEVEL オペランド**

    - 検証目的: 条件追跡のオペランドについて、LISTCAT LEVEL オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、条件追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT LEVEL オペランを指定し、OSKB010049の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT LEVEL オペラン
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT LEVEL オペラン
    CASE OSKB010049
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT LEVEL オペランとOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010049を同じ出力で読み、条件追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010049
    COMMAND ===> SDSF DA
    ISF031I LISTCAT LEVEL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT LEVEL オペラン と OSKB010049 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT VOLUME オペランド {#c30-i0288}
*分類: TSO_LIST*  ・  難易度: 中級

LISTCAT VOLUME オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 復旧照合のオペランドで LISTCAT VOLUME オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LISTCAT VOLUME オペランドの出力を取らず復旧照合のオペランドの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧照合の確認記録にまとめる。 ✅
    - C. SDSF DA を省略して復旧照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合のオペランドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合のオペランドにおいて LISTCAT VOLUME オペランド は説明欄の「復旧照合のオペランドに関係する定義値と表示行を照合する復旧照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のオペランドの証跡を読む担当者は、LISTCAT VOLUME オペランドの属性行と ISF031I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のオペランドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のオペランドは別カテゴリの確認を流用しており、LISTCAT VOLUME オペランドの根拠にならないため復旧照合ではありません。復旧照合のオペランドに出る LISTCAT VOLUME オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT VOLUME オペランド**

    - 検証目的: 範囲追跡のオペランドについて、LISTCAT VOLUME オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、範囲追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT VOLUME オペラを指定し、OSKB010051の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT VOLUME オペラ
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT VOLUME オペラ
    CASE OSKB010051
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT VOLUME オペラとOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010051を同じ出力で読み、範囲追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010051
    COMMAND ===> SDSF DA
    ISF031I LISTCAT VOLUME オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT VOLUME オペラ と OSKB010051 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTCAT 基本構文 {#c30-i0289}
*分類: TSO_LIST*  ・  難易度: 初級

LISTCAT 基本構文は、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 比較照合の基本構文で LISTCAT 基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LISTCAT 基本構文の出力を取らず比較照合の基本構文の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較照合の確認値として扱う。 ✅
    - C. SDSF DA を省略して比較照合の基本構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 比較照合の基本構文において選択記号 B を採用し、識別名は比較照合です。比較照合の基本構文において LISTCAT 基本構文 は説明欄の「比較照合の基本構文に関係する定義値と表示行を照合する比較照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の基本構文の証跡を読む担当者は、LISTCAT 基本構文の属性行と ISF031I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の基本構文は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため比較照合ではありません。 D: 比較照合の基本構文は別カテゴリの確認を流用しており、LISTCAT 基本構文の根拠にならないため比較照合ではありません。比較照合の基本構文に出る LISTCAT 基本構文は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT 基本構文**

    - 検証目的: 上書追跡の基本構文について、LISTCAT 基本構文は、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、上書追跡の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTCAT 基本構文を指定し、OSKB010047の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTCAT 基本構文
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTCAT 基本構文
    CASE OSKB010047
    SOURCE TSO ISPF SDSF
    ```

    LISTCAT 基本構文とOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010047を同じ出力で読み、上書追跡の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010047
    COMMAND ===> SDSF DA
    ISF031I LISTCAT 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTCAT 基本構文 と OSKB010047 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTDS HISTORY オペランド {#c30-i0290}
*分類: TSO_LIST*  ・  難易度: 中級

LISTDS HISTORY オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 範囲照合のオペランドで対話操作の運用確認を行います。LISTDS HISTORY オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で範囲照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず範囲照合のオペランドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲照合の確認にする。 ✅
    - D. LISTDS HISTORY オペランドの属性行を読まず範囲照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合のオペランドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合のオペランドにおいて LISTDS HISTORY オペランド は説明欄の「TSO ISPF SDSF で LISTDS HISTORY オペランドの扱いを記録する範囲照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のオペランドを受け取る担当者は、LISTDS HISTORY オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のオペランドは別カテゴリの確認を流用しており、LISTDS HISTORY オペランドの根拠にならないため範囲照合ではありません。 B: 範囲照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のオペランドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のオペランドが示す LISTDS HISTORY オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTDS HISTORY オペランド**

    - 検証目的: 置換追跡のオペランドについて、LISTDS HISTORY オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、置換追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTDS HISTORY オペラを指定し、OSKB010044の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTDS HISTORY オペラ
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTDS HISTORY オペラ
    CASE OSKB010044
    SOURCE TSO ISPF SDSF
    ```

    LISTDS HISTORY オペラとOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010044を同じ出力で読み、置換追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010044
    COMMAND ===> SDSF DA
    ISF031I LISTDS HISTORY オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTDS HISTORY オペラ と OSKB010044 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTDS LABEL オペランド {#c30-i0291}
*分類: TSO_LIST*  ・  難易度: 中級

LISTDS LABEL オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 記録照合のオペランドに関係する LISTDS LABEL オペランドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録照合で再確認できる形にする。 ✅
    - B. LISTDS LABEL オペランドの名称と担当者名のみを残して記録照合のオペランドの表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で記録照合のオペランドを確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず記録照合のオペランドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合のオペランドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合のオペランドにおいて LISTDS LABEL オペランド は説明欄の「LISTDS LABEL オペランドの用途を対話操作の表示で確認する記録照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のオペランドに関連して、TSO ISPF SDSF では LISTDS LABEL オペランドの表示属性と ISF031I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のオペランドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のオペランドは別カテゴリの確認を流用しており、LISTDS LABEL オペランドの根拠にならないため記録照合ではありません。 D: 記録照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため記録照合ではありません。記録照合のオペランドで使う LISTDS LABEL オペランドという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は記録照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTDS LABEL オペランド**

    - 検証目的: 探索追跡のオペランドについて、LISTDS LABEL オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、探索追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTDS LABEL オペランドを指定し、OSKB010046の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTDS LABEL オペランド
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTDS LABEL オペランド
    CASE OSKB010046
    SOURCE TSO ISPF SDSF
    ```

    LISTDS LABEL オペランドとOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010046を同じ出力で読み、探索追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010046
    COMMAND ===> SDSF DA
    ISF031I LISTDS LABEL オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTDS LABEL オペランド と OSKB010046 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTDS MEMBERS オペランド {#c30-i0292}
*分類: TSO_LIST*  ・  難易度: 中級

PDS/PDSE のメンバ一覧を表示。最終更新日や ID は MEMBERS だけでは出ない (ISPF 3.1 が便利)

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 優先照合のオペランドに関する LISTDS MEMBERS オペランドの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず優先照合のオペランドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のオペランドの証跡として保存して根拠にする。
    - C. LISTDS MEMBERS オペランドの変更点を出力本文から切り離して優先照合のオペランドの承認欄のみ残す。
    - D. TSO ISPF SDSF の表示形式に沿って根拠行を採り、優先照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合のオペランドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合のオペランドにおいて LISTDS MEMBERS オペランド は説明欄の「LISTDS MEMBERS オペランドの状態と出力メッセージを結び付ける優先照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のオペランドに関する記録は、LISTDS MEMBERS オペランドの出力行と ISF031I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため優先照合ではありません。 B: 優先照合のオペランドは別カテゴリの確認を流用しており、LISTDS MEMBERS オペランドの根拠にならないため優先照合ではありません。 C: 優先照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のオペランドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のオペランドで記録する LISTDS MEMBERS オペランドは TSO ISPF SDSF の確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTDS MEMBERS オペランド**

    - 検証目的: 終端追跡のオペランドについて、PDS/PDSE のメンバ一覧を表示。最終更新日や ID は MEMBERS だけでは出ない (ISPF 3.1 が便利)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、終端追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTDS MEMBERS オペラを指定し、OSKB010045の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTDS MEMBERS オペラ
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTDS MEMBERS オペラ
    CASE OSKB010045
    SOURCE TSO ISPF SDSF
    ```

    LISTDS MEMBERS オペラとOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010045を同じ出力で読み、終端追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010045
    COMMAND ===> SDSF DA
    ISF031I LISTDS MEMBERS オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTDS MEMBERS オペラ と OSKB010045 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTDS STATUS オペランド {#c30-i0293}
*分類: TSO_LIST*  ・  難易度: 中級

LISTDS STATUS オペランドは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 区切照合のオペランドで LISTDS STATUS オペランドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LISTDS STATUS オペランドの出力を取らず区切照合のオペランドの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切照合として引き継ぐ。 ✅
    - C. SDSF DA を省略して区切照合のオペランドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のオペランドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合のオペランドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のオペランドにおいて LISTDS STATUS オペランド は説明欄の「区切照合のオペランドに関係する定義値と表示行を照合する区切照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のオペランドの証跡を読む担当者は、LISTDS STATUS オペランドの属性行と ISF031I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のオペランドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため区切照合ではありません。 D: 区切照合のオペランドは別カテゴリの確認を流用しており、LISTDS STATUS オペランドの根拠にならないため区切照合ではありません。区切照合のオペランドに出る LISTDS STATUS オペランドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTDS STATUS オペランド**

    - 検証目的: 呼出追跡のオペランドについて、LISTDS STATUS オペランドは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、呼出追跡のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTDS STATUS オペランを指定し、OSKB010043の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTDS STATUS オペラン
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTDS STATUS オペラン
    CASE OSKB010043
    SOURCE TSO ISPF SDSF
    ```

    LISTDS STATUS オペランとOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010043を同じ出力で読み、呼出追跡のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010043
    COMMAND ===> SDSF DA
    ISF031I LISTDS STATUS オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTDS STATUS オペラン と OSKB010043 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTDS dsname {#c30-i0294}
*分類: TSO_LIST*  ・  難易度: 中級

LISTDS dsnameは、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 条件照合の対話操作に関係する LISTDS dsnameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. SDSF DA で得た表示本文を使い、条件照合の採否を説明欄に結び付ける。 ✅
    - B. LISTDS dsnameの名称と担当者名のみを残して条件照合の対話操作の表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で条件照合の対話操作を確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず条件照合の対話操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合の対話操作において選択記号 A を採用し、識別名は条件照合です。条件照合の対話操作において LISTDS dsname は説明欄の「LISTDS dsnameの用途を対話操作の表示で確認する条件照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の対話操作に関連して、TSO ISPF SDSF では LISTDS dsnameの表示属性と ISF031I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の対話操作は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の対話操作は別カテゴリの確認を流用しており、LISTDS dsnameの根拠にならないため条件照合ではありません。 D: 条件照合の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため条件照合ではありません。条件照合の対話操作で使う LISTDS dsnameという用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTDS dsname**

    - 検証目的: 展開追跡の対話操作について、LISTDS dsnameは、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、展開追跡の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTDS dsnameを指定し、OSKB010042の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTDS dsname
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTDS dsname
    CASE OSKB010042
    SOURCE TSO ISPF SDSF
    ```

    LISTDS dsnameとOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010042を同じ出力で読み、展開追跡の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010042
    COMMAND ===> SDSF DA
    ISF031I LISTDS dsname DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTDS dsname と OSKB010042 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference



### LISTDS 基本構文 {#c30-i0295}
*分類: TSO_LIST*  ・  難易度: 初級

LISTDS 基本構文は、TSO / ISPF / SDSFのTSO_LISTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference

??? question "確認問題（1問）"
    **問題.** 出力照合の基本構文に関する LISTDS 基本構文の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず出力照合の基本構文の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の基本構文の証跡として保存して根拠にする。
    - C. LISTDS 基本構文の変更点を出力本文から切り離して出力照合の基本構文の承認欄のみ残す。
    - D. 同じ画面で対象行と ISF031I を読み、出力照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力照合の基本構文において選択記号 D を採用し、識別名は出力照合です。出力照合の基本構文において LISTDS 基本構文 は説明欄の「LISTDS 基本構文の状態と出力メッセージを結び付ける出力照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の基本構文に関する記録は、LISTDS 基本構文の出力行と ISF031I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため出力照合ではありません。 B: 出力照合の基本構文は別カテゴリの確認を流用しており、LISTDS 基本構文の根拠にならないため出力照合ではありません。 C: 出力照合の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の基本構文は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の基本構文で記録する LISTDS 基本構文は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTDS 基本構文**

    - 検証目的: 構文追跡の基本構文について、LISTDS 基本構文は、TSO / ISPF / SDSF の TSO_LIST で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010041の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、構文追跡の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLISTDS 基本構文を指定し、OSKB010041の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LISTDS 基本構文
    CASE OSKB010041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LISTDS 基本構文
    CASE OSKB010041
    SOURCE TSO ISPF SDSF
    ```

    LISTDS 基本構文とOSKB010041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010041を同じ出力で読み、構文追跡の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010041
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010041
    COMMAND ===> SDSF DA
    ISF031I LISTDS 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LISTDS 基本構文 と OSKB010041 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference




## TSO / ISPF / SDSF > TSO_LOGON

### DISCONNECT コマンド {#c30-i0296}
*分類: TSO_LOGON*  ・  難易度: 中級

DISCONNECT コマンドは、TSO / ISPF / SDSFのTSO_LOGONで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 呼出追跡のコマンドで対話操作の運用確認を行います。DISCONNECT コマンドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で呼出追跡のコマンドを確認した扱いにする。
    - B. ISF031I の有無を確認せず呼出追跡のコマンドを正常終了として記録する。
    - C. TSO ISPF SDSF の表示形式に沿って根拠行を採り、呼出追跡の点検結果を残す。 ✅
    - D. DISCONNECT コマンドの属性行を読まず呼出追跡のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡のコマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のコマンドにおいて DISCONNECT コマンド は説明欄の「TSO ISPF SDSF で DISCONNECT コマンドの扱いを記録する呼出追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のコマンドを受け取る担当者は、DISCONNECT コマンドの表示結果と ISF031I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のコマンドは別カテゴリの確認を流用しており、DISCONNECT コマンドの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のコマンドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のコマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のコマンドが示す DISCONNECT コマンドは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **DISCONNECT コマンド**

    - 検証目的: 探索整理のコマンドについて、DISCONNECT コマンドは、TSO / ISPF / SDSF の TSO_LOGON で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010106の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、探索整理のコマンドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にDISCONNECT コマンドを指定し、OSKB010106の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND DISCONNECT コマンド
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM DISCONNECT コマンド
    CASE OSKB010106
    SOURCE TSO ISPF SDSF
    ```

    DISCONNECT コマンドとOSKB010106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010106を同じ出力で読み、探索整理のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010106
    COMMAND ===> SDSF DA
    ISF031I DISCONNECT コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の DISCONNECT コマンド と OSKB010106 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGOFF コマンド {#c30-i0297}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGOFF コマンドは、TSO / ISPF / SDSFのTSO_LOGONで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 展開追跡のコマンドで LOGOFF コマンドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LOGOFF コマンドの出力を取らず展開追跡のコマンドの説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開追跡の確認にする。 ✅
    - C. SDSF DA を省略して展開追跡のコマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のコマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡のコマンドにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のコマンドにおいて LOGOFF コマンド は説明欄の「展開追跡のコマンドに関係する定義値と表示行を照合する展開追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のコマンドの証跡を読む担当者は、LOGOFF コマンドの属性行と ISF031I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のコマンドは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のコマンドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のコマンドは別カテゴリの確認を流用しており、LOGOFF コマンドの根拠にならないため展開追跡ではありません。展開追跡のコマンドに出る LOGOFF コマンドは TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGOFF コマンド**

    - 検証目的: 終端整理のコマンドについて、LOGOFF コマンドは、TSO / ISPF / SDSF の TSO_LOGON で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010105の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、終端整理のコマンドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGOFF コマンドを指定し、OSKB010105の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGOFF コマンド
    CASE OSKB010105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGOFF コマンド
    CASE OSKB010105
    SOURCE TSO ISPF SDSF
    ```

    LOGOFF コマンドとOSKB010105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010105を同じ出力で読み、終端整理のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010105
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010105
    COMMAND ===> SDSF DA
    ISF031I LOGOFF コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGOFF コマンド と OSKB010105 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON ACCT {#c30-i0298}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGON ACCTは、TSO / ISPF / SDSFのTSO_LOGONで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 監査照合の対話操作で対話操作の運用確認を行います。LOGON ACCT の根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で監査照合の対話操作を確認した扱いにする。
    - B. ISF031I の有無を確認せず監査照合の対話操作を正常終了として記録する。
    - C. 同じ画面で対象行と ISF031I を読み、監査照合の結果として保存する。 ✅
    - D. LOGON ACCT の属性行を読まず監査照合の対話操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合の対話操作において選択記号 C を採用し、識別名は監査照合です。監査照合の対話操作において LOGON ACCT は説明欄の「TSO ISPF SDSF で LOGON ACCT の扱いを記録する監査照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の対話操作を受け取る担当者は、LOGON ACCT の表示結果と ISF031I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の対話操作は別カテゴリの確認を流用しており、LOGON ACCT の根拠にならないため監査照合ではありません。 B: 監査照合の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため監査照合ではありません。 C: 監査照合の対話操作は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の対話操作が示す LOGON ACCT は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON ACCT**

    - 検証目的: 展開整理の対話操作について、LOGON ACCT は、TSO / ISPF / SDSF の TSO_LOGON で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010102の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、展開整理の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON ACCTを指定し、OSKB010102の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON ACCT
    CASE OSKB010102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON ACCT
    CASE OSKB010102
    SOURCE TSO ISPF SDSF
    ```

    LOGON ACCTとOSKB010102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010102を同じ出力で読み、展開整理の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010102
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010102
    COMMAND ===> SDSF DA
    ISF031I LOGON ACCT DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON ACCT と OSKB010102 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON NEW {#c30-i0299}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGON NEWは、TSO / ISPF / SDSFのTSO_LOGONで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 警告照合の対話操作に関係する LOGON NEW の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告照合の確認記録にまとめる。 ✅
    - B. LOGON NEW の名称と担当者名のみを残して警告照合の対話操作の表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で警告照合の対話操作を確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず警告照合の対話操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合の対話操作において選択記号 A を採用し、識別名は警告照合です。警告照合の対話操作において LOGON NEW は説明欄の「LOGON NEW の用途を対話操作の表示で確認する警告照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の対話操作に関連して、TSO ISPF SDSF では LOGON NEW の表示属性と ISF031I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の対話操作は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の対話操作は別カテゴリの確認を流用しており、LOGON NEW の根拠にならないため警告照合ではありません。 D: 警告照合の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため警告照合ではありません。警告照合の対話操作で使う LOGON NEW という用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は警告照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON NEW**

    - 検証目的: 変更判定の対話操作について、LOGON NEW は、TSO / ISPF / SDSF の TSO_LOGON で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010100の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、変更判定の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON NEWを指定し、OSKB010100の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON NEW
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON NEW
    CASE OSKB010100
    SOURCE TSO ISPF SDSF
    ```

    LOGON NEWとOSKB010100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010100を同じ出力で読み、変更判定の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010100
    COMMAND ===> SDSF DA
    ISF031I LOGON NEW DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON NEW と OSKB010100 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON PASSWORD {#c30-i0300}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGON PASSWORDは、TSO / ISPF / SDSFのTSO_LOGONで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 値域照合の対話操作に関する LOGON PASSWORD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず値域照合の対話操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の対話操作の証跡として保存して根拠にする。
    - C. LOGON PASSWORD の変更点を出力本文から切り離して値域照合の対話操作の承認欄のみ残す。
    - D. SDSF DA の結果から対象行を抜き出し、値域照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合の対話操作において選択記号 D を採用し、識別名は値域照合です。値域照合の対話操作において LOGON PASSWORD は説明欄の「LOGON PASSWORD の状態と出力メッセージを結び付ける値域照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の対話操作に関する記録は、LOGON PASSWORD の出力行と ISF031I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため値域照合ではありません。 B: 値域照合の対話操作は別カテゴリの確認を流用しており、LOGON PASSWORD の根拠にならないため値域照合ではありません。 C: 値域照合の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の対話操作は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の対話操作で記録する LOGON PASSWORD は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON PASSWORD**

    - 検証目的: 監査判定の対話操作について、LOGON PASSWORD は、TSO / ISPF / SDSF の TSO_LOGON で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010099の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、監査判定の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON PASSWORDを指定し、OSKB010099の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON PASSWORD
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON PASSWORD
    CASE OSKB010099
    SOURCE TSO ISPF SDSF
    ```

    LOGON PASSWORDとOSKB010099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010099を同じ出力で読み、監査判定の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010099
    COMMAND ===> SDSF DA
    ISF031I LOGON PASSWORD DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON PASSWORD と OSKB010099 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON PERFORM {#c30-i0301}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGON PERFORMは、TSO / ISPF / SDSFのTSO_LOGONで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 構文追跡の対話操作に関係する LOGON PERFORM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文追跡として引き継ぐ。 ✅
    - B. LOGON PERFORM の名称と担当者名のみを残して構文追跡の対話操作の表示本文を確認対象に含めない。
    - C. 対話操作以外の画面で構文追跡の対話操作を確認し同じ証跡として扱ったことにする。
    - D. ISF031I の有無を見ず構文追跡の対話操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡の対話操作において選択記号 A を採用し、識別名は構文追跡です。構文追跡の対話操作において LOGON PERFORM は説明欄の「LOGON PERFORM の用途を対話操作の表示で確認する構文追跡項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の対話操作に関連して、TSO ISPF SDSF では LOGON PERFORM の表示属性と ISF031I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の対話操作は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の対話操作は別カテゴリの確認を流用しており、LOGON PERFORM の根拠にならないため構文追跡ではありません。 D: 構文追跡の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため構文追跡ではありません。構文追跡の対話操作で使う LOGON PERFORM という用語は TSO / ISPF / SDSF で扱う確認対象であり、用語名は構文追跡です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON PERFORM**

    - 検証目的: 置換整理の対話操作について、LOGON PERFORM は、TSO / ISPF / SDSF の TSO_LOGON で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010104の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、置換整理の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON PERFORMを指定し、OSKB010104の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON PERFORM
    CASE OSKB010104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON PERFORM
    CASE OSKB010104
    SOURCE TSO ISPF SDSF
    ```

    LOGON PERFORMとOSKB010104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010104を同じ出力で読み、置換整理の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010104
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010104
    COMMAND ===> SDSF DA
    ISF031I LOGON PERFORM DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON PERFORM と OSKB010104 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON PROC {#c30-i0302}
*分類: TSO_LOGON*  ・  難易度: 上級

TSO ログオン・プロシージャを指定 (例: IKJACCNT)。CLPA 後の DD 構成・初期割当が決まる

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 復旧照合の対話操作で LOGON PROC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LOGON PROC の出力を取らず復旧照合の対話操作の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧照合の根拠にする。 ✅
    - C. SDSF DA を省略して復旧照合の対話操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の対話操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合の対話操作において選択記号 B を採用し、識別名は復旧照合です。復旧照合の対話操作において LOGON PROC は説明欄の「TSO ログオン・プロシージャを指定 (例: IKJACCNT)。CLPA 後の DD 構成・初期割当が決まる」と SDSF DA または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の対話操作の証跡を読む担当者は、LOGON PROC の属性行と ISF031I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の対話操作は対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の対話操作は別カテゴリの確認を流用しており、LOGON PROC の根拠にならないため復旧照合ではありません。復旧照合の対話操作に出る LOGON PROC は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON PROC**

    - 検証目的: 構文整理の対話操作について、TSO ログオン・プロシージャを指定 (例: IKJACCNT)。CLPA 後の DD 構成・初期割当が決まるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010101の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、構文整理の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON PROCを指定し、OSKB010101の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON PROC
    CASE OSKB010101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON PROC
    CASE OSKB010101
    SOURCE TSO ISPF SDSF
    ```

    LOGON PROCとOSKB010101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010101を同じ出力で読み、構文整理の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010101
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010101
    COMMAND ===> SDSF DA
    ISF031I LOGON PROC DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON PROC と OSKB010101 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON SIZE {#c30-i0303}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGON SIZEは、TSO / ISPF / SDSFのTSO_LOGONで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 変更照合の対話操作に関する LOGON SIZE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. SDSF DA の結果を残さず変更照合の対話操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の対話操作の証跡として保存して根拠にする。
    - C. LOGON SIZE の変更点を出力本文から切り離して変更照合の対話操作の承認欄のみ残す。
    - D. SDSF DA で得た表示本文を使い、変更照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合の対話操作において選択記号 D を採用し、識別名は変更照合です。変更照合の対話操作において LOGON SIZE は説明欄の「LOGON SIZE の状態と出力メッセージを結び付ける変更照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の対話操作に関する記録は、LOGON SIZE の出力行と ISF031I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の対話操作は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため変更照合ではありません。 B: 変更照合の対話操作は別カテゴリの確認を流用しており、LOGON SIZE の根拠にならないため変更照合ではありません。 C: 変更照合の対話操作は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の対話操作は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の対話操作で記録する LOGON SIZE は TSO ISPF SDSF の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON SIZE**

    - 検証目的: 呼出整理の対話操作について、LOGON SIZE は、TSO / ISPF / SDSF の TSO_LOGON で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010103の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、呼出整理の対話操作の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON SIZEを指定し、OSKB010103の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON SIZE
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON SIZE
    CASE OSKB010103
    SOURCE TSO ISPF SDSF
    ```

    LOGON SIZEとOSKB010103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010103を同じ出力で読み、呼出整理の対話操作の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010103
    COMMAND ===> SDSF DA
    ISF031I LOGON SIZE DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON SIZE と OSKB010103 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON userid オペランド {#c30-i0304}
*分類: TSO_LOGON*  ・  難易度: 中級

LOGON userid オペランドは、TSO / ISPF / SDSFのTSO_LOGONで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS TSO/E Command Reference、z/OS TSO/E Customization を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 順序照合のオペランドで対話操作の運用確認を行います。LOGON userid オペランドの根拠にできる作業はどれですか。

    - A. TSO ISPF SDSF と無関係な一覧で順序照合のオペランドを確認した扱いにする。
    - B. ISF031I の有無を確認せず順序照合のオペランドを正常終了として記録する。
    - C. ISF031I を含む表示を保存し、説明欄との差分を順序照合で確認する。 ✅
    - D. LOGON userid オペランドの属性行を読まず順序照合のオペランドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合のオペランドにおいて選択記号 C を採用し、識別名は順序照合です。順序照合のオペランドにおいて LOGON userid オペランド は説明欄の「TSO ISPF SDSF で LOGON userid オペランドの扱いを記録する順序照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のオペランドを受け取る担当者は、LOGON userid オペランドの表示結果と ISF031I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のオペランドは別カテゴリの確認を流用しており、LOGON userid オペランドの根拠にならないため順序照合ではありません。 B: 順序照合のオペランドは戻り値や記録番号に寄り、ISF031I や属性表示を落とすため順序照合ではありません。 C: 順序照合のオペランドは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のオペランドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のオペランドが示す LOGON userid オペランドは出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON userid オペランド**

    - 検証目的: 復旧判定のオペランドについて、LOGON userid オペランドは、TSO / ISPF / SDSF の TSO_LOGON で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010098の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、復旧判定のオペランドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON userid オペランドを指定し、OSKB010098の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON userid オペランド
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON userid オペランド
    CASE OSKB010098
    SOURCE TSO ISPF SDSF
    ```

    LOGON userid オペランドとOSKB010098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010098を同じ出力で読み、復旧判定のオペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010098
    COMMAND ===> SDSF DA
    ISF031I LOGON userid オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON userid オペランド と OSKB010098 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization



### LOGON 基本構文 {#c30-i0305}
*分類: TSO_LOGON*  ・  難易度: 初級

TSO セッションを開始する VTAM ベースのアプリケーション。USER/PASSWORD/PROC/ACCT を指定

**出典:** z / OS TSO / E Command Reference、z / E Customization

??? question "確認問題（1問）"
    **問題.** 比較照合の基本構文で LOGON 基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LOGON 基本構文の出力を取らず比較照合の基本構文の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較照合の根拠を固定する。 ✅
    - C. SDSF DA を省略して比較照合の基本構文の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 比較照合の基本構文において選択記号 B を採用し、識別名は比較照合です。比較照合の基本構文において LOGON 基本構文 は説明欄の「比較照合の基本構文に関係する定義値と表示行を照合する比較照合項目」と SDSF DA または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の基本構文の証跡を読む担当者は、LOGON 基本構文の属性行と ISF031I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の基本構文は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の基本構文は戻り値や記録番号に寄り、ISF031I や属性表示を落とすため比較照合ではありません。 D: 比較照合の基本構文は別カテゴリの確認を流用しており、LOGON 基本構文の根拠にならないため比較照合ではありません。比較照合の基本構文に出る LOGON 基本構文は TSO / ISPF / SDSF の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** zOS31_ikjb400 / OS SDSF（zOS31_isfa600） / zOS31_f54u200


??? note "検証手順（1件）"
    **LOGON 基本構文**

    - 検証目的: 警告判定の基本構文について、TSO セッションを開始する VTAM ベースのアプリケーション。USER/PASSWORD/PROC/ACCT を指定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010097の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、警告判定の基本構文の確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にLOGON 基本構文を指定し、OSKB010097の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND LOGON 基本構文
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM LOGON 基本構文
    CASE OSKB010097
    SOURCE TSO ISPF SDSF
    ```

    LOGON 基本構文とOSKB010097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010097を同じ出力で読み、警告判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010097
    COMMAND ===> SDSF DA
    ISF031I LOGON 基本構文 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の LOGON 基本構文 と OSKB010097 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E Customization




## TSO / ISPF / SDSF > TSO_MISC

### ATTRIB コマンド {#c30-i0306}
*分類: TSO_MISC*  ・  難易度: 中級

ATTRIB コマンドは、TSO / ISPF / SDSFのTSO_MISCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS TSO/E Command Reference、z/OS TSO/E User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **ATTRIB コマンド**

    - 検証目的: 区切確認のコマンドについて、ATTRIB コマンドは、TSO / ISPF / SDSF の TSO_MISC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、区切確認のコマンドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にATTRIB コマンドを指定し、OSKB020010の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND ATTRIB コマンド
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM ATTRIB コマンド
    CASE OSKB020010
    SOURCE TSO ISPF SDSF
    ```

    ATTRIB コマンドとOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020010を同じ出力で読み、区切確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020010
    COMMAND ===> SDSF DA
    ISF031I ATTRIB コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の ATTRIB コマンド と OSKB020010 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide



### CALL コマンド {#c30-i0307}
*分類: TSO_MISC*  ・  難易度: 中級

CALL コマンドは、TSO / ISPF / SDSFのTSO_MISCで確認する項目です。ロード モジュールを直接呼出す。CALL 'LOAD(MEM)' [パラメータ]。テスト・ユーティリティ単発実行で使う

**出典:** z / OS TSO / E Command Reference、z / E User's Guide

??? note "検証手順（1件）"
    **CALL コマンド**

    - 検証目的: 展開確認のコマンドについて、CALL コマンドは、TSO / ISPF / SDSF の TSO_MISC で確認する項目です。ロード モジュールを直接呼出す。CALL 'LOAD(MEM)' [パラメータに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB020002の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、展開確認のコマンドの確認表示へ進みます。
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
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCALL コマンドを指定し、OSKB020002の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND CALL コマンド
    CASE OSKB020002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM CALL コマンド
    CASE OSKB020002
    SOURCE TSO ISPF SDSF
    ```

    CALL コマンドとOSKB020002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB020002を同じ出力で読み、展開確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB020002
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB020002
    COMMAND ===> SDSF DA
    ISF031I CALL コマンド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB020002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の CALL コマンド と OSKB020002 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB020002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / E User's Guide


