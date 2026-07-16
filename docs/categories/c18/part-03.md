---
search:
  exclude: true
---

# JCL EXEC 文 — 詳細 (3/3)

[← JCL EXEC 文 の概要へ戻る](index.md)


## JCL EXEC 文 > 後方参照

### 後方参照の有効範囲 {#c18-i0142}
*分類: 後方参照*  ・  難易度: 中級

後方参照の有効範囲は、JCL EXEC 文の後方参照で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference / z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 性能分類の監査確認に関するジョブログを確認します。EXEC文の扱いとして適切なものはどれですか。

    - A. DD名の一覧から後方参照の有効範囲を決めてJESMSGLGの応答を確認しない。
    - B. SDSFの表示時刻を根拠に後方参照の有効範囲を確定して変換後JCLを読まない。
    - C. 後方参照の有効範囲をステップ単位の指定として読みMAXCCやIEFメッセージと照合します。 ✅
    - D. JOB文の会計欄で後方参照の有効範囲を判断してEXEC行の再掲確認を省く。

    正解: **C** ／ 難易度: 中級

    **解説:** 正答はC。性能分類の監査確認では後方参照の有効範囲をEXEC文の実行対象または実行属性として扱うことを監査確認で確認します。性能分類の監査確認の再確認ではジョブログ内の再掲値と処理結果を対応させます。A: 性能分類の監査確認では入出力側の情報と実行側の情報を分離して扱いますので、SDSF上の表示入口と本文を分けます。 B: 性能分類の監査確認では一覧情報からIEF142Iの対象ステップを確定できませんので、JCL変換後の値を基準にします。 C: 性能分類の監査確認は指定値と完了応答を分けて残せるため、性能分類の照合に使いますので、実行属性として採った根拠を残します。 D: 性能分類の監査確認では会計情報を読んでもJESMSGLGの対象行が残りませんので、後続レビューでは出力本文を読みます。 資源語として、性能分類の監査確認の領域指定はステップが利用する記憶域の扱いに関わります。性能分類では指定根拠を応答根拠へつなげます。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / OS SDSF（zOS31_isfa600）

    ---

    **問題.** 原記法 後方参照の有効範囲 を対象にします。後方参照の有効範囲をレビューするとき、最初に確認すべき意味はどれですか 省略値や境界値がある場合はそこも考えてください。 正しいものはどれですか。

    - A. 後方参照の有効範囲を先行ステップや手続内ステップへの後方参照として読む ✅
    - B. 時間制限を解除する無制限指定として読む。後方参照の有効範囲とは別機能なので変換後JCLで切り分ける
    - C. 会計情報の下位値を並べる指定として扱う。ジョブログと照合しても対象欄が一致しないため除含めないる
    - D. 条件文を閉じる終了記号として扱う。投入前レビューでは別のEXEC指定として記録する

    正解: **A** ／ 難易度: 上級

    **解説:** 後方参照の有効範囲ではAが正解です。確認対象は後方参照の有効範囲です。手続展開後は、後方参照では、ジョブステップ名、手続ステップ名、データ定義名の階層を取り違えないことが重要であるため、背景対象は後方参照の有効範囲の背景。選択肢(B)については時間制限を解除する無制限指定として読むので、戻りコードの扱いと一致しません、対象は後方参照の有効範囲の候補B。(C)は会計情報の下位値を並べる指定として扱うので、参照名の階層が違います、対象は後方参照の有効範囲の候補Cため不適切です。誤答Dは条件文を閉じる終了記号として扱うので、実行対象の指定ではありません、対象は後方参照の有効範囲の候補D。用語として、後方参照の有効範囲はジョブ文側指定との比較点です。

    **出典:** zOS_MVS_JCL_Reference / zOS_MVS_JCL_Users_Guide / zOS_MVS_System_Messages




## その他

### その他（特定項目に紐づかないQA・手順） {#c18-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? note "検証手順（75件）"
    **EXEC 文の構文位置 検証手順**

    - 検証目的: JCL EXEC文のEXEC 文の構文位置について、SDSFで変換後JCLと実行メッセージを机上確認します。EXEC 文の構文位置は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。を構文照合の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX163 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX163 を入力し、EXEC 文の構文位置の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX163
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX163
    ```

    `COMMAND INPUT ===> ST JCLX163` が表示されていれば、JCLX163 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX163 の出力を開き、JESJCLに表示されたEXEC行からEXEC 文の構文位置の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX163
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX163 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC 文の構文位置の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX163 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX163 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX163 ENDED AT N1 MAXCC=0004
    ISSUER=OPER163
    ```

    `$HASP165 JCLX163 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、EXEC 文の構文位置の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX163 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC 文の必須要素 検証手順**

    - 検証目的: JCL EXEC文のEXEC 文の必須要素について、SDSFで変換後JCLと実行メッセージを机上確認します。PGM= または PROC= のどちらか 1 つは必須。「EXEC 文の必須要素」はジョブステップのレビューで、実行対象、パラメータ渡し、条件付き実行の切り分けに使うを実行属性確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX164 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX164 を入力し、EXEC 文の必須要素の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX164
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX164
    ```

    `COMMAND INPUT ===> ST JCLX164` が表示されていれば、JCLX164 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX164 の出力を開き、JESJCLに表示されたEXEC行からEXEC 文の必須要素の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX164
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX164 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC 文の必須要素の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX164 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX164 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX164 ENDED AT N1 MAXCC=0008
    ISSUER=OPER164
    ```

    `$HASP165 JCLX164 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、EXEC 文の必須要素の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX164 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 (省略可) 検証手順**

    - 検証目的: JCL EXEC文のステップ名 (省略可)について、SDSFで変換後JCLと実行メッセージを机上確認します。ステップ名 (省略可)は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。を会計情報確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX165 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX165 を入力し、ステップ名 (省略可)の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX165
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX165
    ```

    `COMMAND INPUT ===> ST JCLX165` が表示されていれば、JCLX165 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX165 の出力を開き、JESJCLに表示されたEXEC行からステップ名 (省略可)の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX165
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX165 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでステップ名 (省略可)の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX165 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX165 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX165 ENDED AT N1 MAXCC=0012
    ISSUER=OPER165
    ```

    `$HASP165 JCLX165 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、ステップ名 (省略可)の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX165 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 文字数 検証手順**

    - 検証目的: JCL EXEC文のステップ名 文字数について、SDSFで変換後JCLと実行メッセージを机上確認します。ステップ名 文字数は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/を再始動確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX166 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX166 を入力し、ステップ名 文字数の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX166
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX166
    ```

    `COMMAND INPUT ===> ST JCLX166` が表示されていれば、JCLX166 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX166 の出力を開き、JESJCLに表示されたEXEC行からステップ名 文字数の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX166
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX166 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでステップ名 文字数の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX166 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX166 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX166 ENDED AT N1 MAXCC=0016
    ISSUER=OPER166
    ```

    `$HASP165 JCLX166 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、ステップ名 文字数の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX166 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 先頭文字 検証手順**

    - 検証目的: JCL EXEC文のステップ名 先頭文字について、SDSFで変換後JCLと実行メッセージを机上確認します。ステップ名 先頭文字は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。英字または国別文字 ($,#,@) で始めること。「ステップ名 先頭文字」はジョを通知確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX167 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX167 を入力し、ステップ名 先頭文字の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX167
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX167
    ```

    `COMMAND INPUT ===> ST JCLX167` が表示されていれば、JCLX167 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX167 の出力を開き、JESJCLに表示されたEXEC行からステップ名 先頭文字の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX167
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX167 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでステップ名 先頭文字の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX167 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX167 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX167 ENDED AT N1 MAXCC=0000
    ISSUER=OPER167
    ```

    `$HASP165 JCLX167 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、ステップ名 先頭文字の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX167 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 重複禁止 検証手順**

    - 検証目的: JCL EXEC文のステップ名 重複禁止について、SDSFで変換後JCLと実行メッセージを机上確認します。ステップ名 重複禁止は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。zをクラス確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX168 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX168 を入力し、ステップ名 重複禁止の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX168
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX168
    ```

    `COMMAND INPUT ===> ST JCLX168` が表示されていれば、JCLX168 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX168 の出力を開き、JESJCLに表示されたEXEC行からステップ名 重複禁止の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX168
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX168 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでステップ名 重複禁止の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX168 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX168 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX168 ENDED AT N1 MAXCC=0004
    ISSUER=OPER168
    ```

    `$HASP165 JCLX168 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、ステップ名 重複禁止の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX168 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 省略時の挙動 検証手順**

    - 検証目的: JCL EXEC文のステップ名 省略時の挙動について、SDSFで変換後JCLと実行メッセージを机上確認します。ステップ名 省略時の挙動は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認しますを条件確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX169 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX169 を入力し、ステップ名 省略時の挙動の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX169
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX169
    ```

    `COMMAND INPUT ===> ST JCLX169` が表示されていれば、JCLX169 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX169 の出力を開き、JESJCLに表示されたEXEC行からステップ名 省略時の挙動の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX169
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX169 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでステップ名 省略時の挙動の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX169 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX169 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX169 ENDED AT N1 MAXCC=0008
    ISSUER=OPER169
    ```

    `$HASP165 JCLX169 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、ステップ名 省略時の挙動の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX169 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **オペランド区切り 検証手順**

    - 検証目的: JCL EXEC文のオペランド区切りについて、SDSFで変換後JCLと実行メッセージを机上確認します。オペランド区切りは、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。オペランドはカンマで区切り、空白で終了。「オペランド区切り」はジョブステップのレビュを権限確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX170 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX170 を入力し、オペランド区切りの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX170
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX170
    ```

    `COMMAND INPUT ===> ST JCLX170` が表示されていれば、JCLX170 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX170 の出力を開き、JESJCLに表示されたEXEC行からオペランド区切りの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX170
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX170 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでオペランド区切りの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX170 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX170 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX170 ENDED AT N1 MAXCC=0012
    ISSUER=OPER170
    ```

    `$HASP165 JCLX170 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、オペランド区切りの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX170 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **継続行 検証手順**

    - 検証目的: JCL EXEC文の継続行について、SDSFで変換後JCLと実行メッセージを机上確認します。継続行は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVSを識別確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX171 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX171 を入力し、継続行の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX171
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX171
    ```

    `COMMAND INPUT ===> ST JCLX171` が表示されていれば、JCLX171 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX171 の出力を開き、JESJCLに表示されたEXEC行から継続行の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX171
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX171 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLで継続行の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX171 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX171 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX171 ENDED AT N1 MAXCC=0016
    ISSUER=OPER171
    ```

    `$HASP165 JCLX171 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、継続行の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX171 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **コメント記入位置 検証手順**

    - 検証目的: JCL EXEC文のコメント記入位置について、SDSFで変換後JCLと実行メッセージを机上確認します。コメント記入位置は、JCL EXEC 文のEXEC 文 基本で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/Oを変換確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX172 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX172 を入力し、コメント記入位置の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX172
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX172
    ```

    `COMMAND INPUT ===> ST JCLX172` が表示されていれば、JCLX172 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX172 の出力を開き、JESJCLに表示されたEXEC行からコメント記入位置の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX172
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX172 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでコメント記入位置の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX172 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX172 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX172 ENDED AT N1 MAXCC=0000
    ISSUER=OPER172
    ```

    `$HASP165 JCLX172 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、コメント記入位置の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX172 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC PGM=progname 検証手順**

    - 検証目的: JCL EXEC文のEXEC PGM=prognameについて、SDSFで変換後JCLと実行メッセージを机上確認します。EXEC PGM=prognameは、STEPLIB/JOBLIB/LNKLST にあるロードモジュールを実行。「EXEC PGM=progname」はジョブステップのレビューで、実行対象、パラメータをログ照合の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX173 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX173 を入力し、EXEC PGM=prognameの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX173
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX173
    ```

    `COMMAND INPUT ===> ST JCLX173` が表示されていれば、JCLX173 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX173 の出力を開き、JESJCLに表示されたEXEC行からEXEC PGM=prognameの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX173
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX173 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC PGM=prognameの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX173 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX173 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX173 ENDED AT N1 MAXCC=0004
    ISSUER=OPER173
    ```

    `$HASP165 JCLX173 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、EXEC PGM=prognameの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX173 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **progname 文字数 検証手順**

    - 検証目的: JCL EXEC文のprogname 文字数について、SDSFで変換後JCLと実行メッセージを机上確認します。progname 文字数は、JCL EXEC 文のPGM= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。zを運用証跡確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX174 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX174 を入力し、progname 文字数の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX174
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX174
    ```

    `COMMAND INPUT ===> ST JCLX174` が表示されていれば、JCLX174 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX174 の出力を開き、JESJCLに表示されたEXEC行からprogname 文字数の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX174
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX174 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでprogname 文字数の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX174 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX174 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX174 ENDED AT N1 MAXCC=0008
    ISSUER=OPER174
    ```

    `$HASP165 JCLX174 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、progname 文字数の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX174 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC PGM=*.stepname.ddname 検証手順**

    - 検証目的: JCL EXEC文のEXEC PGM=*.stepname.ddnameについて、SDSFで変換後JCLと実行メッセージを机上確認します。EXEC PGM=*.stepname.ddnameは、前ステップで作成したロードモジュールを実行 (一時データセット参照)を経路確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX175 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX175 を入力し、EXEC PGM=*.stepname.ddnameの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX175
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX175
    ```

    `COMMAND INPUT ===> ST JCLX175` が表示されていれば、JCLX175 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX175 の出力を開き、JESJCLに表示されたEXEC行からEXEC PGM=*.stepname.ddnameの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX175
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX175 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC PGM=*.stepname.ddnameの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX175 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX175 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX175 ENDED AT N1 MAXCC=0012
    ISSUER=OPER175
    ```

    `$HASP165 JCLX175 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、EXEC PGM=*.stepname.ddnameの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX175 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC PGM=*.procstep.ddname 検証手順**

    - 検証目的: JCL EXEC文のEXEC PGM=*.procstep.ddnameについて、SDSFで変換後JCLと実行メッセージを机上確認します。EXEC PGM=*.procstep.ddnameは、プロシジャ内ステップの DD を参照。「EXEC PGM=*.procstep.ddname」はジョブステップのレビューで、実行対象、パラメータを終了確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX176 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX176 を入力し、EXEC PGM=*.procstep.ddnameの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX176
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX176
    ```

    `COMMAND INPUT ===> ST JCLX176` が表示されていれば、JCLX176 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX176 の出力を開き、JESJCLに表示されたEXEC行からEXEC PGM=*.procstep.ddnameの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX176
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX176 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC PGM=*.procstep.ddnameの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX176 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX176 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX176 ENDED AT N1 MAXCC=0016
    ISSUER=OPER176
    ```

    `$HASP165 JCLX176 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、EXEC PGM=*.procstep.ddnameの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX176 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM=IEFBR14 検証手順**

    - 検証目的: JCL EXEC文のPGM=IEFBR14について、SDSFで変換後JCLと実行メッセージを机上確認します。PGM=IEFBR14は、JCL EXEC 文のPGM= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/を保守確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX177 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX177 を入力し、PGM=IEFBR14の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX177
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX177
    ```

    `COMMAND INPUT ===> ST JCLX177` が表示されていれば、JCLX177 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX177 の出力を開き、JESJCLに表示されたEXEC行からPGM=IEFBR14の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX177
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX177 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPGM=IEFBR14の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX177 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX177 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX177 ENDED AT N1 MAXCC=0000
    ISSUER=OPER177
    ```

    `$HASP165 JCLX177 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、PGM=IEFBR14の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX177 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM=IEBGENER 等システムユーティリティ 検証手順**

    - 検証目的: JCL EXEC文のPGM=IEBGENER 等システムユーティリティについて、SDSFで変換後JCLと実行メッセージを机上確認します。PGM=IEBGENER 等システムユーティリティは、ロードライブラリ SYS1.LINKLIB から直接呼出可を構文照合の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX178 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX178 を入力し、PGM=IEBGENER 等システムユーティリティの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX178
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX178
    ```

    `COMMAND INPUT ===> ST JCLX178` が表示されていれば、JCLX178 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX178 の出力を開き、JESJCLに表示されたEXEC行からPGM=IEBGENER 等システムユーティリティの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX178
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX178 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPGM=IEBGENER 等システムユーティリティの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX178 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX178 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX178 ENDED AT N1 MAXCC=0004
    ISSUER=OPER178
    ```

    `$HASP165 JCLX178 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、PGM=IEBGENER 等システムユーティリティの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX178 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM= と STEPLIB 連結 検証手順**

    - 検証目的: JCL EXEC文のPGM= と STEPLIB 連結について、SDSFで変換後JCLと実行メッセージを机上確認します。PGM= と STEPLIB 連結は、//STEPLIB DD でモジュール検索ライブラリを指定。「PGM= と STEPLIB 連結」はジョブステップのレビューで、実行対象、パラメータ渡し、条件付きを実行属性確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX179 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX179 を入力し、PGM= と STEPLIB 連結の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX179
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX179
    ```

    `COMMAND INPUT ===> ST JCLX179` が表示されていれば、JCLX179 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX179 の出力を開き、JESJCLに表示されたEXEC行からPGM= と STEPLIB 連結の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX179
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX179 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPGM= と STEPLIB 連結の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX179 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX179 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX179 ENDED AT N1 MAXCC=0008
    ISSUER=OPER179
    ```

    `$HASP165 JCLX179 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、PGM= と STEPLIB 連結の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX179 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM= と JOBLIB の優先順 検証手順**

    - 検証目的: JCL EXEC文のPGM= と JOBLIB の優先順について、SDSFで変換後JCLと実行メッセージを机上確認します。PGM= と JOBLIB の優先順は、JCL EXEC 文のPGM= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確を会計情報確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX180 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX180 を入力し、PGM= と JOBLIB の優先順の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX180
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX180
    ```

    `COMMAND INPUT ===> ST JCLX180` が表示されていれば、JCLX180 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX180 の出力を開き、JESJCLに表示されたEXEC行からPGM= と JOBLIB の優先順の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX180
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX180 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPGM= と JOBLIB の優先順の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX180 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX180 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX180 ENDED AT N1 MAXCC=0012
    ISSUER=OPER180
    ```

    `$HASP165 JCLX180 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、PGM= と JOBLIB の優先順の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX180 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM= と LNKLST 検証手順**

    - 検証目的: JCL EXEC文のPGM= と LNKLSTについて、SDSFで変換後JCLと実行メッセージを机上確認します。PGM= と LNKLSTは、JCL EXEC 文のPGM= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。を再始動確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX181 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX181 を入力し、PGM= と LNKLSTの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX181
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX181
    ```

    `COMMAND INPUT ===> ST JCLX181` が表示されていれば、JCLX181 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX181 の出力を開き、JESJCLに表示されたEXEC行からPGM= と LNKLSTの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX181
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX181 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPGM= と LNKLSTの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX181 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX181 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX181 ENDED AT N1 MAXCC=0016
    ISSUER=OPER181
    ```

    `$HASP165 JCLX181 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、PGM= と LNKLSTの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX181 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC PROC=procname 検証手順**

    - 検証目的: JCL EXEC文のEXEC PROC=procnameについて、SDSFで変換後JCLと実行メッセージを机上確認します。カタログ式 (PROCLIB) または インストリーム プロシジャを起動。「EXEC PROC=procname」はジョブステップのレビューで、実行対象、パラメータ渡し、条件付き実行の切り分けに使うを通知確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX182 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX182 を入力し、EXEC PROC=procnameの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX182
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX182
    ```

    `COMMAND INPUT ===> ST JCLX182` が表示されていれば、JCLX182 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX182 の出力を開き、JESJCLに表示されたEXEC行からEXEC PROC=procnameの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX182
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX182 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC PROC=procnameの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX182 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX182 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX182 ENDED AT N1 MAXCC=0000
    ISSUER=OPER182
    ```

    `$HASP165 JCLX182 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、EXEC PROC=procnameの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX182 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC procname (PROC= 省略) 検証手順**

    - 検証目的: JCL EXEC文のEXEC procname (PROC= 省略)について、SDSFで変換後JCLと実行メッセージを机上確認します。EXEC procname (PROC= 省略)は、JCL EXEC 文のPROC= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニをクラス確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX183 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX183 を入力し、EXEC procname (PROC= 省略)の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX183
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX183
    ```

    `COMMAND INPUT ===> ST JCLX183` が表示されていれば、JCLX183 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX183 の出力を開き、JESJCLに表示されたEXEC行からEXEC procname (PROC= 省略)の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX183
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX183 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでEXEC procname (PROC= 省略)の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX183 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX183 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX183 ENDED AT N1 MAXCC=0004
    ISSUER=OPER183
    ```

    `$HASP165 JCLX183 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、EXEC procname (PROC= 省略)の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX183 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **procname 文字数 検証手順**

    - 検証目的: JCL EXEC文のprocname 文字数について、SDSFで変換後JCLと実行メッセージを机上確認します。procname 文字数は、JCL EXEC 文のPROC= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。を条件確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX184 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX184 を入力し、procname 文字数の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX184
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX184
    ```

    `COMMAND INPUT ===> ST JCLX184` が表示されていれば、JCLX184 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX184 の出力を開き、JESJCLに表示されたEXEC行からprocname 文字数の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX184
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX184 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでprocname 文字数の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX184 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX184 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX184 ENDED AT N1 MAXCC=0008
    ISSUER=OPER184
    ```

    `$HASP165 JCLX184 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、procname 文字数の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX184 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **インストリーム プロシジャ 検証手順**

    - 検証目的: JCL EXEC文のインストリーム プロシジャについて、SDSFで変換後JCLと実行メッセージを机上確認します。インストリーム プロシジャは、JCL EXEC 文のPROC= 形式で機能名、見出し、または確認対象として参照する項目です。インストリーム プロシジャは、// pname PROC  // PEND を権限確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX185 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX185 を入力し、インストリーム プロシジャの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX185
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX185
    ```

    `COMMAND INPUT ===> ST JCLX185` が表示されていれば、JCLX185 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX185 の出力を開き、JESJCLに表示されたEXEC行からインストリーム プロシジャの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX185
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX185 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでインストリーム プロシジャの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX185 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX185 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX185 ENDED AT N1 MAXCC=0012
    ISSUER=OPER185
    ```

    `$HASP165 JCLX185 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、インストリーム プロシジャの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX185 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **カタログ式プロシジャ 検証手順**

    - 検証目的: JCL EXEC文のカタログ式プロシジャについて、SDSFで変換後JCLと実行メッセージを机上確認します。カタログ式プロシジャは、JCL EXEC 文のPROC= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/を識別確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX186 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX186 を入力し、カタログ式プロシジャの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX186
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX186
    ```

    `COMMAND INPUT ===> ST JCLX186` が表示されていれば、JCLX186 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX186 の出力を開き、JESJCLに表示されたEXEC行からカタログ式プロシジャの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX186
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX186 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでカタログ式プロシジャの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX186 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX186 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX186 ENDED AT N1 MAXCC=0016
    ISSUER=OPER186
    ```

    `$HASP165 JCLX186 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、カタログ式プロシジャの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX186 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **JCLLIB との併用 検証手順**

    - 検証目的: JCL EXEC文のJCLLIB との併用について、SDSFで変換後JCLと実行メッセージを机上確認します。JCLLIB との併用は、JCL EXEC 文のPROC= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。zを変換確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX187 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX187 を入力し、JCLLIB との併用の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX187
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX187
    ```

    `COMMAND INPUT ===> ST JCLX187` が表示されていれば、JCLX187 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX187 の出力を開き、JESJCLに表示されたEXEC行からJCLLIB との併用の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX187
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX187 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでJCLLIB との併用の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX187 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX187 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX187 ENDED AT N1 MAXCC=0000
    ISSUER=OPER187
    ```

    `$HASP165 JCLX187 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、JCLLIB との併用の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX187 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **プロシジャ シンボルパラメータ 検証手順**

    - 検証目的: JCL EXEC文のプロシジャ シンボルパラメータについて、SDSFで変換後JCLと実行メッセージを机上確認します。プロシジャ シンボルパラメータは、EXEC PROC=,SYMBOL=value 形式でシンボル値を上書き。「プロシジャ シンボルパラメータ」はジョブステップのレビューで、実行対象、パラメータ渡し、条をログ照合の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX188 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX188 を入力し、プロシジャ シンボルパラメータの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX188
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX188
    ```

    `COMMAND INPUT ===> ST JCLX188` が表示されていれば、JCLX188 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX188 の出力を開き、JESJCLに表示されたEXEC行からプロシジャ シンボルパラメータの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX188
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX188 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでプロシジャ シンボルパラメータの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX188 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX188 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX188 ENDED AT N1 MAXCC=0004
    ISSUER=OPER188
    ```

    `$HASP165 JCLX188 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、プロシジャ シンボルパラメータの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX188 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM= と PROC= の排他 検証手順**

    - 検証目的: JCL EXEC文のPGM= と PROC= の排他について、SDSFで変換後JCLと実行メッセージを机上確認します。PGM= と PROC= の排他は、JCL EXEC 文のPROC= 形式で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認を運用証跡確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX189 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX189 を入力し、PGM= と PROC= の排他の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX189
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX189
    ```

    `COMMAND INPUT ===> ST JCLX189` が表示されていれば、JCLX189 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX189 の出力を開き、JESJCLに表示されたEXEC行からPGM= と PROC= の排他の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX189
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX189 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPGM= と PROC= の排他の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX189 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX189 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX189 ENDED AT N1 MAXCC=0008
    ISSUER=OPER189
    ```

    `$HASP165 JCLX189 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、PGM= と PROC= の排他の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX189 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM= の用途 検証手順**

    - 検証目的: JCL EXEC文のPARM= の用途について、SDSFで変換後JCLと実行メッセージを机上確認します。PARM= の用途は、JCL EXEC 文のPARM=で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS MVS JCL Referencを経路確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX190 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX190 を入力し、PARM= の用途の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX190
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX190
    ```

    `COMMAND INPUT ===> ST JCLX190` が表示されていれば、JCLX190 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX190 の出力を開き、JESJCLに表示されたEXEC行からPARM= の用途の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX190
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX190 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM= の用途の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX190 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX190 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX190 ENDED AT N1 MAXCC=0012
    ISSUER=OPER190
    ```

    `$HASP165 JCLX190 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、PARM= の用途の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX190 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM=value (単純文字列) 検証手順**

    - 検証目的: JCL EXEC文のPARM=value (単純文字列)について、SDSFで変換後JCLと実行メッセージを机上確認します。PARM=value (単純文字列)は、英数字のみで括弧不要の単純指定。「PARM=value (単純文字列)」はジョブステップのレビューで、実行対象、パラメータ渡し、条件付き実行の切り分けに使うを終了確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX191 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX191 を入力し、PARM=value (単純文字列)の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX191
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX191
    ```

    `COMMAND INPUT ===> ST JCLX191` が表示されていれば、JCLX191 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX191 の出力を開き、JESJCLに表示されたEXEC行からPARM=value (単純文字列)の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX191
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX191 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM=value (単純文字列)の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX191 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX191 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX191 ENDED AT N1 MAXCC=0016
    ISSUER=OPER191
    ```

    `$HASP165 JCLX191 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、PARM=value (単純文字列)の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX191 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM='value with spaces' 検証手順**

    - 検証目的: JCL EXEC文のPARM='value with spaces'について、SDSFで変換後JCLと実行メッセージを机上確認します。PARM='value with spaces'は、JCL EXEC 文のPARM= 形式で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/Oを保守確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX192 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX192 を入力し、PARM='value with spaces'の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX192
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX192
    ```

    `COMMAND INPUT ===> ST JCLX192` が表示されていれば、JCLX192 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX192 の出力を開き、JESJCLに表示されたEXEC行からPARM='value with spaces'の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX192
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX192 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM='value with spaces'の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX192 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX192 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX192 ENDED AT N1 MAXCC=0000
    ISSUER=OPER192
    ```

    `$HASP165 JCLX192 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、PARM='value with spaces'の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX192 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM=(sub1,sub2,…) 検証手順**

    - 検証目的: JCL EXEC文のPARM=(sub1,sub2,…)について、SDSFで変換後JCLと実行メッセージを机上確認します。PARM=(sub1,sub2,)は、JCL EXEC 文のPARM= 形式で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS MVS Jを構文照合の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX193 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0004 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX193 を入力し、PARM=(sub1,sub2,…)の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX193
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX193
    ```

    `COMMAND INPUT ===> ST JCLX193` が表示されていれば、JCLX193 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX193 の出力を開き、JESJCLに表示されたEXEC行からPARM=(sub1,sub2,…)の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX193
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX193 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM=(sub1,sub2,…)の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX193 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX193 STEP1 - STEP WAS EXECUTED - COND CODE 0004
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX193 ENDED AT N1 MAXCC=0004
    ISSUER=OPER193
    ```

    `$HASP165 JCLX193 ENDED AT N1 MAXCC=0004` と `IEF374I` がJESMSGLGに表示されていれば、PARM=(sub1,sub2,…)の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX193 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM=(sub1,'sub 2',sub3) 検証手順**

    - 検証目的: JCL EXEC文のPARM=(sub1,'sub 2',sub3)について、SDSFで変換後JCLと実行メッセージを机上確認します。PARM=(sub1,'sub 2',sub3)は、サブパラメータ単位でアポストロフィ可。「PARM=(sub1,'sub 2',sub3)」はジョブステップのレビューで、実行対象、パラメータ渡し、条を実行属性確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX194 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0008 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX194 を入力し、PARM=(sub1,'sub 2',sub3)の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX194
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX194
    ```

    `COMMAND INPUT ===> ST JCLX194` が表示されていれば、JCLX194 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX194 の出力を開き、JESJCLに表示されたEXEC行からPARM=(sub1,'sub 2',sub3)の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX194
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX194 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM=(sub1,'sub 2',sub3)の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX194 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX194 STEP1 - STEP WAS EXECUTED - COND CODE 0008
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX194 ENDED AT N1 MAXCC=0008
    ISSUER=OPER194
    ```

    `$HASP165 JCLX194 ENDED AT N1 MAXCC=0008` と `IEF374I` がJESMSGLGに表示されていれば、PARM=(sub1,'sub 2',sub3)の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX194 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM= 最大長 100 バイト 検証手順**

    - 検証目的: JCL EXEC文のPARM= 最大長 100 バイトについて、SDSFで変換後JCLと実行メッセージを机上確認します。PARM= 最大長 100 バイトは、JCL EXEC 文のPARM= 内容で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS MVS Jを会計情報確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX195 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0012 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX195 を入力し、PARM= 最大長 100 バイトの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX195
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX195
    ```

    `COMMAND INPUT ===> ST JCLX195` が表示されていれば、JCLX195 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX195 の出力を開き、JESJCLに表示されたEXEC行からPARM= 最大長 100 バイトの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX195
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX195 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM= 最大長 100 バイトの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX195 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX195 STEP1 - STEP WAS EXECUTED - COND CODE 0012
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX195 ENDED AT N1 MAXCC=0012
    ISSUER=OPER195
    ```

    `$HASP165 JCLX195 ENDED AT N1 MAXCC=0012` と `IEF374I` がJESMSGLGに表示されていれば、PARM= 最大長 100 バイトの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX195 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM= 継続記述 検証手順**

    - 検証目的: JCL EXEC文のPARM= 継続記述について、SDSFで変換後JCLと実行メッセージを机上確認します。PARM= 継続記述は、JCL EXEC 文のPARM= 内容で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS MVS JCL Refeを再始動確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX196 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0016 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX196 を入力し、PARM= 継続記述の机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX196
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX196
    ```

    `COMMAND INPUT ===> ST JCLX196` が表示されていれば、JCLX196 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX196 の出力を開き、JESJCLに表示されたEXEC行からPARM= 継続記述の指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX196
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX196 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでPARM= 継続記述の指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX196 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX196 STEP1 - STEP WAS EXECUTED - COND CODE 0016
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX196 ENDED AT N1 MAXCC=0016
    ISSUER=OPER196
    ```

    `$HASP165 JCLX196 ENDED AT N1 MAXCC=0016` と `IEF374I` がJESMSGLGに表示されていれば、PARM= 継続記述の机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX196 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **アポストロフィのエスケープ 検証手順**

    - 検証目的: JCL EXEC文のアポストロフィのエスケープについて、SDSFで変換後JCLと実行メッセージを机上確認します。アポストロフィのエスケープは、JCL EXEC 文のPARM= 内容で構成値やオプションの意味を確認する項目です。文字列中のアポストロフィは '' (連続 2 個) と書く。「アポストロフィのエスケーを通知確認の観点で確認します。
    - 前提条件: SDSFにログオン済みで、確認対象のジョブ出力を参照できる前提です。実機ではジョブ投入や再実行は変更管理の承認後に行います。
    - セッション環境: SDSFのCOMMAND INPUTから ST JCLX197 を入力し、JESJCLとJESMSGLGで EXEC、IEF142I、IEF374I、$HASP165、MAXCC=0000 を確認します。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST JCLX197 を入力し、アポストロフィのエスケープの机上確認に使うジョブ状態を呼び出します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JCLX197
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JCLX197
    ```

    `COMMAND INPUT ===> ST JCLX197` が表示されていれば、JCLX197 の状態表示を開始できます。

    **ステップ 2**
    現在の画面はSDSFのST一覧です。NP欄に S を入力して JCLX197 の出力を開き、JESJCLに表示されたEXEC行からアポストロフィのエスケープの指定を確認します。
    操作（入力）:
    ```text
    (SDSF ST)
    NP   JOBNAME
    S    JCLX197
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESJCL)
    //JCLX197 JOB (A123),'EXEC CHECK'
    //STEP1 EXEC PGM=IEFBR14
    //SYSIN  DD DUMMY
    ```

    `EXEC PGM=IEFBR14` がJESJCLに表示されていれば、変換後JCLでアポストロフィのエスケープの指定位置を確認できます。

    **ステップ 3**
    現在の画面はSDSF OUTPUTのDD一覧です。NP欄に S を入力してJESMSGLGを開き、JCLX197 の実行メッセージとMAXCCを確認します。
    操作（入力）:
    ```text
    (SDSF OUTPUT)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF OUTPUT - JESMSGLG)
    IEF142I JCLX197 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/STEP1/START 2026.194
    IEF374I STEP/STEP1/STOP  2026.194 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JCLX197 ENDED AT N1 MAXCC=0000
    ISSUER=OPER197
    ```

    `$HASP165 JCLX197 ENDED AT N1 MAXCC=0000` と `IEF374I` がJESMSGLGに表示されていれば、アポストロフィのエスケープの机上確認結果を記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JCLX197 が画面・出力に表示されること
    ② ステップ2 の EXEC PGM=IEFBR14 が画面・出力に表示されること
    ③ ステップ3 の $HASP165 と MAXCC=0000 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC 文の構文位置 確認手順**

    - 検証目的: EXEC 文の構文位置について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00201を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00201を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00201
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00201
    ```

    COMMAND INPUTにST JEX00201が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S10 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00201 S10 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S10/START 2026.196
    IEF374I STEP/S10/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00201 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00201が表示されること
    ステップ2 の JESJCLに//S10 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **プロシジャ ステップ単位上書き 確認手順**

    - 検証目的: プロシジャ ステップ単位上書きについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00202を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,PARM='TEST'とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00202を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00202
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00202
    ```

    COMMAND INPUTにST JEX00202が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S11 EXEC PGM=IEFBR14,PARM='TEST'
    ```

    EXEC行にPGM=IEFBR14,PARM='TEST'が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00202 S11 - STEP WAS EXECUTED - PARM='TEST'
    IEF373I STEP/S11/START 2026.196
    IEF374I STEP/S11/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00202 ENDED AT N1 MAXCC=0004
    ```

    IEF142IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00202が表示されること
    ステップ2 の JESJCLに//S11 EXEC PGM=IEFBR14,PARM='TEST'が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **REGION=nK 確認手順**

    - 検証目的: REGION=nKについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00203を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,REGION=64MとIEF373Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00203を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00203
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00203
    ```

    COMMAND INPUTにST JEX00203が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S12 EXEC PGM=IEFBR14,REGION=64M
    ```

    EXEC行にPGM=IEFBR14,REGION=64Mが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF373I JEX00203 S12 - STEP WAS EXECUTED - REGION=64M
    IEF373I STEP/S12/START 2026.196
    IEF374I STEP/S12/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00203 ENDED AT N1 MAXCC=0008
    ```

    IEF373IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00203が表示されること
    ステップ2 の JESJCLに//S12 EXEC PGM=IEFBR14,REGION=64Mが表示されること
    ステップ3 の JESMSGLGにIEF373IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **比較演算子 EQ/= 確認手順**

    - 検証目的: 比較演算子 EQ/=について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00204を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00204を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00204
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00204
    ```

    COMMAND INPUTにST JEX00204が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S13 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00204 S13 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S13/START 2026.196
    IEF374I STEP/S13/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00204 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00204が表示されること
    ステップ2 の JESJCLに//S13 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 省略時の挙動 確認手順**

    - 検証目的: ステップ名 省略時の挙動について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00205を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00205を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00205
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00205
    ```

    COMMAND INPUTにST JEX00205が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S14 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00205 S14 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S14/START 2026.196
    IEF374I STEP/S14/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00205 ENDED AT N1 MAXCC=0004
    ```

    IEF142IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00205が表示されること
    ステップ2 の JESJCLに//S14 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **COND=(code,oper) 確認手順**

    - 検証目的: COND=(code,oper)について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00206を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00206を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00206
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00206
    ```

    COMMAND INPUTにST JEX00206が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S15 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00206 S15 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S15/START 2026.196
    IEF374I STEP/S15/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00206 ENDED AT N1 MAXCC=0008
    ```

    IEF272IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00206が表示されること
    ステップ2 の JESJCLに//S15 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **REGION と MEMLIMIT の関係 確認手順**

    - 検証目的: REGION と MEMLIMIT の関係について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00207を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,REGION=64MとIEF373Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00207を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00207
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00207
    ```

    COMMAND INPUTにST JEX00207が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S16 EXEC PGM=IEFBR14,REGION=64M
    ```

    EXEC行にPGM=IEFBR14,REGION=64Mが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF373I JEX00207 S16 - STEP WAS EXECUTED - REGION=64M
    IEF373I STEP/S16/START 2026.196
    IEF374I STEP/S16/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00207 ENDED AT N1 MAXCC=0000
    ```

    IEF373IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00207が表示されること
    ステップ2 の JESJCLに//S16 EXEC PGM=IEFBR14,REGION=64Mが表示されること
    ステップ3 の JESMSGLGにIEF373IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **論理 AND (&) 確認手順**

    - 検証目的: 論理 AND (&)について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00208を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00208を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00208
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00208
    ```

    COMMAND INPUTにST JEX00208が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S17 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00208 S17 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S17/START 2026.196
    IEF374I STEP/S17/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00208 ENDED AT N1 MAXCC=0004
    ```

    IEF142IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00208が表示されること
    ステップ2 の JESJCLに//S17 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **EXEC PGM=*.stepname.ddname 確認手順**

    - 検証目的: EXEC PGM=*.stepname.ddnameについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00209を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00209を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00209
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00209
    ```

    COMMAND INPUTにST JEX00209が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S18 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00209 S18 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S18/START 2026.196
    IEF374I STEP/S18/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00209 ENDED AT N1 MAXCC=0008
    ```

    IEF142IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00209が表示されること
    ステップ2 の JESJCLに//S18 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **COND oper=GE (≥) 確認手順**

    - 検証目的: COND oper=GE (≥)について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00210を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00210を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00210
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00210
    ```

    COMMAND INPUTにST JEX00210が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S19 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00210 S19 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S19/START 2026.196
    IEF374I STEP/S19/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00210 ENDED AT N1 MAXCC=0000
    ```

    IEF272IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00210が表示されること
    ステップ2 の JESJCLに//S19 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **DYNAMNBR と TSO/E 確認手順**

    - 検証目的: DYNAMNBR と TSO/Eについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00211を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,DYNAMNBR=20とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00211を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00211
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00211
    ```

    COMMAND INPUTにST JEX00211が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S20 EXEC PGM=IEFBR14,DYNAMNBR=20
    ```

    EXEC行にPGM=IEFBR14,DYNAMNBR=20が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00211 S20 - STEP WAS EXECUTED - DYNAMNBR=20
    IEF373I STEP/S20/START 2026.196
    IEF374I STEP/S20/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00211 ENDED AT N1 MAXCC=0004
    ```

    IEF142IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00211が表示されること
    ステップ2 の JESJCLに//S20 EXEC PGM=IEFBR14,DYNAMNBR=20が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **&LASTRC キーワード 確認手順**

    - 検証目的: &LASTRC キーワードについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00212を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00212を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00212
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00212
    ```

    COMMAND INPUTにST JEX00212が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S21 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00212 S21 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S21/START 2026.196
    IEF374I STEP/S21/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00212 ENDED AT N1 MAXCC=0008
    ```

    IEF272IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00212が表示されること
    ステップ2 の JESJCLに//S21 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM= と LNKLST 確認手順**

    - 検証目的: PGM= と LNKLSTについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00213を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00213を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00213
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00213
    ```

    COMMAND INPUTにST JEX00213が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S22 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00213 S22 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S22/START 2026.196
    IEF374I STEP/S22/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00213 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00213が表示されること
    ステップ2 の JESJCLに//S22 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **COND=EVEN 確認手順**

    - 検証目的: COND=EVENについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00214を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00214を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00214
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00214
    ```

    COMMAND INPUTにST JEX00214が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S23 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00214 S23 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S23/START 2026.196
    IEF374I STEP/S23/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00214 ENDED AT N1 MAXCC=0004
    ```

    IEF272IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00214が表示されること
    ステップ2 の JESJCLに//S23 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ACCT 最大長 確認手順**

    - 検証目的: ACCT 最大長について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00215を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,ACCT=(A123,TEST)とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00215を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00215
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00215
    ```

    COMMAND INPUTにST JEX00215が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S24 EXEC PGM=IEFBR14,ACCT=(A123,TEST)
    ```

    EXEC行にPGM=IEFBR14,ACCT=(A123,TEST)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00215 S24 - STEP WAS EXECUTED - ACCT=(A123,TEST)
    IEF373I STEP/S24/START 2026.196
    IEF374I STEP/S24/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00215 ENDED AT N1 MAXCC=0008
    ```

    IEF142IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00215が表示されること
    ステップ2 の JESJCLに//S24 EXEC PGM=IEFBR14,ACCT=(A123,TEST)が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ABEND の論理値 確認手順**

    - 検証目的: ABEND の論理値について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00216を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00216を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00216
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00216
    ```

    COMMAND INPUTにST JEX00216が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S25 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00216 S25 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S25/START 2026.196
    IEF374I STEP/S25/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00216 ENDED AT N1 MAXCC=0000
    ```

    IEF272IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00216が表示されること
    ステップ2 の JESJCLに//S25 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **JCLLIB との併用 確認手順**

    - 検証目的: JCLLIB との併用について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00217を表示し、JESJCLとJESMSGLGを順に開いてPROC=PROCEXとIEFC653Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00217を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00217
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00217
    ```

    COMMAND INPUTにST JEX00217が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S26 EXEC PROC=PROCEX
    ```

    EXEC行にPROC=PROCEXが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEFC653I JEX00217 S26 - STEP WAS EXECUTED - PROC=PROCEX
    IEF373I STEP/S26/START 2026.196
    IEF374I STEP/S26/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00217 ENDED AT N1 MAXCC=0004
    ```

    IEFC653IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00217が表示されること
    ステップ2 の JESJCLに//S26 EXEC PROC=PROCEXが表示されること
    ステップ3 の JESMSGLGにIEFC653IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **COND と IF/THEN の使い分け 確認手順**

    - 検証目的: COND と IF/THEN の使い分けについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00218を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00218を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00218
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00218
    ```

    COMMAND INPUTにST JEX00218が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S27 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00218 S27 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S27/START 2026.196
    IEF374I STEP/S27/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00218 ENDED AT N1 MAXCC=0008
    ```

    IEF272IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00218が表示されること
    ステップ2 の JESJCLに//S27 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PERFORM の用途 確認手順**

    - 検証目的: PERFORM の用途について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00219を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00219を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00219
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00219
    ```

    COMMAND INPUTにST JEX00219が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S28 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00219 S28 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S28/START 2026.196
    IEF374I STEP/S28/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00219 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00219が表示されること
    ステップ2 の JESJCLに//S28 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    ***.stepname.procstep.ddname 形式 確認手順**

    - 検証目的: *.stepname.procstep.ddname 形式について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00220を表示し、JESJCLとJESMSGLGを順に開いてPROC=PROCEXとIEFC653Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00220を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00220
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00220
    ```

    COMMAND INPUTにST JEX00220が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S29 EXEC PROC=PROCEX
    ```

    EXEC行にPROC=PROCEXが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEFC653I JEX00220 S29 - STEP WAS EXECUTED - PROC=PROCEX
    IEF373I STEP/S29/START 2026.196
    IEF374I STEP/S29/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00220 ENDED AT N1 MAXCC=0004
    ```

    IEFC653IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00220が表示されること
    ステップ2 の JESJCLに//S29 EXEC PROC=PROCEXが表示されること
    ステップ3 の JESMSGLGにIEFC653IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PARM=(sub1,sub2,…) 確認手順**

    - 検証目的: PARM=(sub1,sub2,…)について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00221を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,PARM='TEST'とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00221を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00221
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00221
    ```

    COMMAND INPUTにST JEX00221が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S30 EXEC PGM=IEFBR14,PARM='TEST'
    ```

    EXEC行にPGM=IEFBR14,PARM='TEST'が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00221 S30 - STEP WAS EXECUTED - PARM='TEST'
    IEF373I STEP/S30/START 2026.196
    IEF374I STEP/S30/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00221 ENDED AT N1 MAXCC=0008
    ```

    IEF142IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00221が表示されること
    ステップ2 の JESJCLに//S30 EXEC PGM=IEFBR14,PARM='TEST'が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **TIME=NOLIMIT 確認手順**

    - 検証目的: TIME=NOLIMITについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00222を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,TIME=(1,0)とIEF374Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00222を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00222
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00222
    ```

    COMMAND INPUTにST JEX00222が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S31 EXEC PGM=IEFBR14,TIME=(1,0)
    ```

    EXEC行にPGM=IEFBR14,TIME=(1,0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF374I JEX00222 S31 - STEP WAS EXECUTED - CPU 0MIN 00.01SEC
    IEF373I STEP/S31/START 2026.196
    IEF374I STEP/S31/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00222 ENDED AT N1 MAXCC=0000
    ```

    IEF374IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00222が表示されること
    ステップ2 の JESJCLに//S31 EXEC PGM=IEFBR14,TIME=(1,0)が表示されること
    ステップ3 の JESMSGLGにIEF374IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PROCESS= 確認手順**

    - 検証目的: PROCESS=について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00223を表示し、JESJCLとJESMSGLGを順に開いてPROC=PROCEXとIEFC653Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00223を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00223
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00223
    ```

    COMMAND INPUTにST JEX00223が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S32 EXEC PROC=PROCEX
    ```

    EXEC行にPROC=PROCEXが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEFC653I JEX00223 S32 - STEP WAS EXECUTED - PROC=PROCEX
    IEF373I STEP/S32/START 2026.196
    IEF374I STEP/S32/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00223 ENDED AT N1 MAXCC=0004
    ```

    IEFC653IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00223が表示されること
    ステップ2 の JESJCLに//S32 EXEC PROC=PROCEXが表示されること
    ステップ3 の JESMSGLGにIEFC653IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **後方参照と RESTART 確認手順**

    - 検証目的: 後方参照と RESTARTについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00224を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00224を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00224
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00224
    ```

    COMMAND INPUTにST JEX00224が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S33 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00224 S33 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S33/START 2026.196
    IEF374I STEP/S33/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00224 ENDED AT N1 MAXCC=0008
    ```

    IEF142IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00224が表示されること
    ステップ2 の JESJCLに//S33 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **プロシジャ側 PARM 上書き 確認手順**

    - 検証目的: プロシジャ側 PARM 上書きについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00225を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,PARM='TEST'とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00225を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00225
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00225
    ```

    COMMAND INPUTにST JEX00225が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S34 EXEC PGM=IEFBR14,PARM='TEST'
    ```

    EXEC行にPGM=IEFBR14,PARM='TEST'が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00225 S34 - STEP WAS EXECUTED - PARM='TEST'
    IEF373I STEP/S34/START 2026.196
    IEF374I STEP/S34/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00225 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00225が表示されること
    ステップ2 の JESJCLに//S34 EXEC PGM=IEFBR14,PARM='TEST'が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **REGION の目的 確認手順**

    - 検証目的: REGION の目的について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00226を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,REGION=64MとIEF373Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00226を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00226
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00226
    ```

    COMMAND INPUTにST JEX00226が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S35 EXEC PGM=IEFBR14,REGION=64M
    ```

    EXEC行にPGM=IEFBR14,REGION=64Mが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF373I JEX00226 S35 - STEP WAS EXECUTED - REGION=64M
    IEF373I STEP/S35/START 2026.196
    IEF374I STEP/S35/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00226 ENDED AT N1 MAXCC=0004
    ```

    IEF373IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00226が表示されること
    ステップ2 の JESJCLに//S35 EXEC PGM=IEFBR14,REGION=64Mが表示されること
    ステップ3 の JESMSGLGにIEF373IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ラベル名 制限 確認手順**

    - 検証目的: ラベル名 制限について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00227を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00227を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00227
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00227
    ```

    COMMAND INPUTにST JEX00227が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S36 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00227 S36 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S36/START 2026.196
    IEF374I STEP/S36/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00227 ENDED AT N1 MAXCC=0008
    ```

    IEF142IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00227が表示されること
    ステップ2 の JESJCLに//S36 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ステップ名 重複禁止 確認手順**

    - 検証目的: ステップ名 重複禁止について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00228を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00228を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00228
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00228
    ```

    COMMAND INPUTにST JEX00228が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S37 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00228 S37 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S37/START 2026.196
    IEF374I STEP/S37/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00228 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00228が表示されること
    ステップ2 の JESJCLに//S37 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **COND の目的 確認手順**

    - 検証目的: COND の目的について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00229を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00229を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00229
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00229
    ```

    COMMAND INPUTにST JEX00229が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S38 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00229 S38 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S38/START 2026.196
    IEF374I STEP/S38/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00229 ENDED AT N1 MAXCC=0004
    ```

    IEF272IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00229が表示されること
    ステップ2 の JESJCLに//S38 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **REGION=0M とアドレス空間 確認手順**

    - 検証目的: REGION=0M とアドレス空間について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00230を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,REGION=64MとIEF373Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00230を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00230
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00230
    ```

    COMMAND INPUTにST JEX00230が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S39 EXEC PGM=IEFBR14,REGION=64M
    ```

    EXEC行にPGM=IEFBR14,REGION=64Mが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF373I JEX00230 S39 - STEP WAS EXECUTED - REGION=64M
    IEF373I STEP/S39/START 2026.196
    IEF374I STEP/S39/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00230 ENDED AT N1 MAXCC=0008
    ```

    IEF373IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00230が表示されること
    ステップ2 の JESJCLに//S39 EXEC PGM=IEFBR14,REGION=64Mが表示されること
    ステップ3 の JESMSGLGにIEF373IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **比較演算子 LE/<= 確認手順**

    - 検証目的: 比較演算子 LE/<=について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00231を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00231を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00231
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00231
    ```

    COMMAND INPUTにST JEX00231が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S40 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00231 S40 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S40/START 2026.196
    IEF374I STEP/S40/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00231 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00231が表示されること
    ステップ2 の JESJCLに//S40 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **progname 文字数 確認手順**

    - 検証目的: progname 文字数について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00232を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00232を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00232
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00232
    ```

    COMMAND INPUTにST JEX00232が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S41 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00232 S41 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S41/START 2026.196
    IEF374I STEP/S41/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00232 ENDED AT N1 MAXCC=0004
    ```

    IEF142IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00232が表示されること
    ステップ2 の JESJCLに//S41 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **COND oper=GT (>) 確認手順**

    - 検証目的: COND oper=GT (>)について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00233を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00233を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00233
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00233
    ```

    COMMAND INPUTにST JEX00233が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S42 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00233 S42 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S42/START 2026.196
    IEF374I STEP/S42/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00233 ENDED AT N1 MAXCC=0008
    ```

    IEF272IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00233が表示されること
    ステップ2 の JESJCLに//S42 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **DYNAMNBR 既定値 確認手順**

    - 検証目的: DYNAMNBR 既定値について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00234を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,DYNAMNBR=20とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00234を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00234
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00234
    ```

    COMMAND INPUTにST JEX00234が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S43 EXEC PGM=IEFBR14,DYNAMNBR=20
    ```

    EXEC行にPGM=IEFBR14,DYNAMNBR=20が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00234 S43 - STEP WAS EXECUTED - DYNAMNBR=20
    IEF373I STEP/S43/START 2026.196
    IEF374I STEP/S43/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00234 ENDED AT N1 MAXCC=0000
    ```

    IEF142IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00234が表示されること
    ステップ2 の JESJCLに//S43 EXEC PGM=IEFBR14,DYNAMNBR=20が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **&MAXRC キーワード 確認手順**

    - 検証目的: &MAXRC キーワードについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00235を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00235を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00235
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00235
    ```

    COMMAND INPUTにST JEX00235が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S44 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00235 S44 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S44/START 2026.196
    IEF374I STEP/S44/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00235 ENDED AT N1 MAXCC=0004
    ```

    IEF272IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00235が表示されること
    ステップ2 の JESJCLに//S44 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **PGM= と JOBLIB の優先順 確認手順**

    - 検証目的: PGM= と JOBLIB の優先順について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00236を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00236を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00236
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00236
    ```

    COMMAND INPUTにST JEX00236が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S45 EXEC PGM=IEFBR14
    ```

    EXEC行にPGM=IEFBR14が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00236 S45 - STEP WAS EXECUTED - COND CODE 0000
    IEF373I STEP/S45/START 2026.196
    IEF374I STEP/S45/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00236 ENDED AT N1 MAXCC=0008
    ```

    IEF142IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00236が表示されること
    ステップ2 の JESJCLに//S45 EXEC PGM=IEFBR14が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **演算子の論理 確認手順**

    - 検証目的: 演算子の論理について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00237を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00237を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00237
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00237
    ```

    COMMAND INPUTにST JEX00237が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S46 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00237 S46 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S46/START 2026.196
    IEF374I STEP/S46/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00237 ENDED AT N1 MAXCC=0000
    ```

    IEF272IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00237が表示されること
    ステップ2 の JESJCLに//S46 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **ACCT と JOB アカウント情報 確認手順**

    - 検証目的: ACCT と JOB アカウント情報について、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00238を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,ACCT=(A123,TEST)とIEF142Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00238を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00238
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00238
    ```

    COMMAND INPUTにST JEX00238が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S47 EXEC PGM=IEFBR14,ACCT=(A123,TEST)
    ```

    EXEC行にPGM=IEFBR14,ACCT=(A123,TEST)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF142I JEX00238 S47 - STEP WAS EXECUTED - ACCT=(A123,TEST)
    IEF373I STEP/S47/START 2026.196
    IEF374I STEP/S47/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00238 ENDED AT N1 MAXCC=0004
    ```

    IEF142IとMAXCC=0004が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00238が表示されること
    ステップ2 の JESJCLに//S47 EXEC PGM=IEFBR14,ACCT=(A123,TEST)が表示されること
    ステップ3 の JESMSGLGにIEF142IとMAXCC=0004が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **stepname.ABENDCC キーワード 確認手順**

    - 検証目的: stepname.ABENDCC キーワードについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00239を表示し、JESJCLとJESMSGLGを順に開いてPGM=IEFBR14,COND=(4,LT,STEP0)とIEF272Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00239を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00239
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00239
    ```

    COMMAND INPUTにST JEX00239が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S48 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)
    ```

    EXEC行にPGM=IEFBR14,COND=(4,LT,STEP0)が表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEF272I JEX00239 S48 - STEP WAS EXECUTED - STEP WAS NOT EXECUTED
    IEF373I STEP/S48/START 2026.196
    IEF374I STEP/S48/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00239 ENDED AT N1 MAXCC=0008
    ```

    IEF272IとMAXCC=0008が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00239が表示されること
    ステップ2 の JESJCLに//S48 EXEC PGM=IEFBR14,COND=(4,LT,STEP0)が表示されること
    ステップ3 の JESMSGLGにIEF272IとMAXCC=0008が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

    ---

    **カタログ式プロシジャ 確認手順**

    - 検証目的: カタログ式プロシジャについて、EXEC行、JESJCL再掲、JESMSGLG応答を机上で確認します。
    - 前提条件: SDSFにログオン済みで、対象ジョブのJESJCLとJESMSGLGを閲覧できる前提です。実機投入は変更管理承認後に検証用ジョブで行います。
    - セッション環境: SDSFのジョブ一覧でJEX00240を表示し、JESJCLとJESMSGLGを順に開いてPROC=PROCEXとIEFC653Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUTにST JEX00240を入力し、対象ジョブの出力データセット一覧を表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JEX00240
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JEX00240
    ```

    COMMAND INPUTにST JEX00240が表示され、対象ジョブを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。JESJCLを開き、JESが解釈したEXEC行の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //S49 EXEC PROC=PROCEX
    ```

    EXEC行にPROC=PROCEXが表示され、入力指定が変換後JCLに残っています。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。JESMSGLGを開き、ステップ実行メッセージとジョブ終了行を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESMSGLG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESMSGLG)
    IEFC653I JEX00240 S49 - STEP WAS EXECUTED - PROC=PROCEX
    IEF373I STEP/S49/START 2026.196
    IEF374I STEP/S49/STOP  2026.196 CPU 0MIN 00.01SEC SRB 0MIN 00.00SEC
    $HASP165 JEX00240 ENDED AT N1 MAXCC=0000
    ```

    IEFC653IとMAXCC=0000が同じ出力に現れるため、EXEC文の指定と実行結果を対応付けられます。

    - 合格条件: ステップ1 の COMMAND INPUTにST JEX00240が表示されること
    ステップ2 の JESJCLに//S49 EXEC PROC=PROCEXが表示されること
    ステップ3 の JESMSGLGにIEFC653IとMAXCC=0000が表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference / OS MVS JCL User's Guide

