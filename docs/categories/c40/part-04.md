---
search:
  exclude: true
---

# ユーティリティ — 詳細 (4/4)

[← ユーティリティ の概要へ戻る](index.md)


## ユーティリティ > IEHPROGM

### UNCATLG 制御文 {#c40-i0251}
*分類: IEHPROGM*  ・  難易度: 中級

UNCATLG 制御文は、ユーティリティのIEHPROGMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)

??? note "検証手順（1件）"
    **UNCATLG 制御文**

    - 検証目的: 記録検査の制御文について、UNCATLG 制御文は、ユーティリティの IEHPROGM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010073の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、記録検査の制御文の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNCATLG 制御文を指定し、OSKB010073の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNCATLG 制御文
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNCATLG 制御文
    CASE OSKB010073
    SOURCE z/OS Utilities
    ```

    UNCATLG 制御文とOSKB010073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010073を同じ出力で読み、記録検査の制御文の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010073
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I UNCATLG 制御文 PROCESSING STARTED
    IEF142I OSKB010073 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の UNCATLG 制御文 と OSKB010073 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)



### ユーティリティの基本機能 {#c40-i0252}
*分類: IEHPROGM*  ・  難易度: 初級

ユーティリティの基本機能は、ユーティリティのIEHPROGMで確認する項目です。データセットの SCRATCH (物理削除)、UNCATLG (カタログ抹消)、CATLG (カタログ登録)、RENAME (改名)、GDG 関連の BLD / DLT などを行う管理系ユーティリティ。IDCAMS で代替できる機能が多いが、レガシージョブでは現役

**出典:** z / OS DFSMSdfp Utilities (z / OS 3.1)



## ユーティリティ > ISRDDN

### DD 一覧表示の用途 {#c40-i0253}
*分類: ISRDDN*  ・  難易度: 中級

DD 一覧表示の用途は、ユーティリティのISRDDNで機能名、見出し、または確認対象として参照する項目です。ISPF 編集中の SYSPROC / SYSEXEC / STEPLIB 等の解決順を確認する。「なぜこの CLIST/REXX が実行されたか」「STEPLIB の優先順位」を追跡する診断に有用

**出典:** z / OS ISPF User's Guide Vol I (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 監査検査の一覧表示の用途でユーティリティの運用確認を行います。DD 一覧表示の用途の根拠にできる作業はどれですか。

    - A. z/OS Utilitiesと無関係な一覧で監査検査の一覧表示の用途を確認した扱いにする。
    - B. IEF142I の有無を確認せず監査検査の一覧表示の用途を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査検査の記録として扱う。 ✅
    - D. DD 一覧表示の用途の属性行を読まず監査検査の一覧表示の用途の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査の一覧表示の用途において選択記号 C を採用し、識別名は監査検査です。監査検査の一覧表示の用途において DD 一覧表示の用途 は説明欄の「z/OS Utilitiesで DD 一覧表示の用途の扱いを記録する監査検査項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は監査検査です。監査検査の一覧表示の用途を受け取る担当者は、DD 一覧表示の用途の表示結果と IEF142I を同じ確認単位として扱い、背景名は監査検査です。不適切な選択肢を整理します。 A: 監査検査の一覧表示の用途は別カテゴリの確認を流用しており、DD 一覧表示の用途の根拠にならないため監査検査ではありません。 B: 監査検査の一覧表示の用途は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため監査検査ではありません。 C: 監査検査の一覧表示の用途は対象出力と項目説明を結び、根拠を残すので監査検査です。 D: 監査検査の一覧表示の用途は名称や説明のみに寄り、状態を示す出力本文が不足するため監査検査ではありません。監査検査の一覧表示の用途が示す DD 一覧表示の用途は出典欄の資料で使い方を追跡できる項目であり、用語名は監査検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（1件）"
    **DD 一覧表示の用途**

    - 検証目的: 展開記録の一覧表示の用途について、DD 一覧表示の用途は、ユーティリティの ISRDDN で機能名、見出し、または確認対象として参照する項目です。ISPF 編集中の SYSPROC / SYSEXEC / STに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020122の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、展開記録の一覧表示の用途の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にDD 一覧表示の用途を指定し、OSKB020122の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD 一覧表示の用途
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD 一覧表示の用途
    CASE OSKB020122
    SOURCE z/OS Utilities
    ```

    DD 一覧表示の用途とOSKB020122が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020122を同じ出力で読み、展開記録の一覧表示の用途の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020122
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I DD 一覧表示の用途 PROCESSING STARTED
    IEF142I OSKB020122 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020122が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の DD 一覧表示の用途 と OSKB020122 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF User's Guide Vol I (z / OS 3.1)



### ENQ 表示機能 {#c40-i0254}
*分類: ISRDDN*  ・  難易度: 中級

ISRDDN 上で 'ENQ' サブコマンドを入力すると、対象データセットへの ENQ (シリアル化) ホルダー一覧が表示される。共有 PDS のロック衝突調査に使う

**出典:** z / OS ISPF User's Guide Vol I (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 変更検査の表示機能に関する ENQ 表示機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBUTIL の結果を残さず変更検査の表示機能の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の表示機能の証跡として保存して根拠にする。
    - C. ENQ 表示機能の変更点を出力本文から切り離して変更検査の表示機能の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査の表示機能において選択記号 D を採用し、識別名は変更検査です。変更検査の表示機能において ENQ 表示機能 は説明欄の「ISRDDN 上で 'ENQ' サブコマンドを入力すると、対象データセットへの ENQ (シリアル化) ホルダー一覧が表示される。共有 PD」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査の表示機能に関する記録は、ENQ 表示機能の出力行と IEF142I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査の表示機能は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため変更検査ではありません。 B: 変更検査の表示機能は別カテゴリの確認を流用しており、ENQ 表示機能の根拠にならないため変更検査ではありません。 C: 変更検査の表示機能は名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査の表示機能は対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査の表示機能で記録する ENQ 表示機能はz/OS Utilitiesの確認記録に残す対象名であり、用語名は変更検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（1件）"
    **ENQ 表示機能**

    - 検証目的: 呼出記録の表示機能について、ISRDDN 上で 'ENQ' サブコマンドを入力すると、対象データセットへの ENQ (シリアル化) ホルダー一覧が表示される。共有 PDS のロック衝突調査に使うに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020123の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、呼出記録の表示機能の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にENQ 表示機能を指定し、OSKB020123の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ENQ 表示機能
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ENQ 表示機能
    CASE OSKB020123
    SOURCE z/OS Utilities
    ```

    ENQ 表示機能とOSKB020123が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020123を同じ出力で読み、呼出記録の表示機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020123
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I ENQ 表示機能 PROCESSING STARTED
    IEF142I OSKB020123 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020123が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の ENQ 表示機能 と OSKB020123 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF User's Guide Vol I (z / OS 3.1)



### MEMBER サブコマンド {#c40-i0255}
*分類: ISRDDN*  ・  難易度: 中級

ISRDDN 上で 'M' / 'MEMBER' を入力すれば、注目している DD 上のメンバー一覧をその場で参照できる。STEPLIB 内のメンバー確認に便利

**出典:** z / OS ISPF User's Guide Vol I (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文判定のサブコマンドに関係する MEMBER サブコマンドの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文判定として残す。 ✅
    - B. MEMBER サブコマンドの名称と担当者名のみを残して構文判定のサブコマンドの表示本文を確認対象に含めない。
    - C. ユーティリティ以外の画面で構文判定のサブコマンドを確認し同じ証跡として扱ったことにする。
    - D. IEF142I の有無を見ず構文判定のサブコマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定のサブコマンドにおいて選択記号 A を採用し、識別名は構文判定です。構文判定のサブコマンドにおいて MEMBER サブコマンド は説明欄の「MEMBER サブコマンドの用途をユーティリティの表示で確認する構文判定項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は構文判定です。構文判定のサブコマンドに関連して、z/OS Utilitiesでは MEMBER サブコマンドの表示属性と IEF142I を同じ証跡に残し、背景名は構文判定です。他の選択肢を確認します。 A: 構文判定のサブコマンドは対象出力と項目説明を結び、根拠を残すので構文判定です。 B: 構文判定のサブコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文判定ではありません。 C: 構文判定のサブコマンドは別カテゴリの確認を流用しており、MEMBER サブコマンドの根拠にならないため構文判定ではありません。 D: 構文判定のサブコマンドは戻り値や記録番号に寄り、IEF142I や属性表示を落とすため構文判定ではありません。構文判定のサブコマンドで使う MEMBER サブコマンドという用語はユーティリティで扱う確認対象であり、用語名は構文判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（1件）"
    **MEMBER サブコマンド**

    - 検証目的: 置換記録のサブコマンドについて、ISRDDN 上で 'M' / 'MEMBER' を入力すれば、注目している DD 上のメンバー一覧をその場で参照できる。STEPLIB 内のメンバー確認に便利に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020124の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、置換記録のサブコマンドの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にMEMBER サブコマンドを指定し、OSKB020124の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MEMBER サブコマンド
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MEMBER サブコマンド
    CASE OSKB020124
    SOURCE z/OS Utilities
    ```

    MEMBER サブコマンドとOSKB020124が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020124を同じ出力で読み、置換記録のサブコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020124
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I MEMBER サブコマンド PROCESSING STARTED
    IEF142I OSKB020124 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020124が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の MEMBER サブコマンド と OSKB020124 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF User's Guide Vol I (z / OS 3.1)



### コマンドの基本機能 {#c40-i0256}
*分類: ISRDDN*  ・  難易度: 初級

コマンドの基本機能は、TSO/ISPF セッションのコマンド行で 'TSO ISRDDN' (または短縮 'DDLIST') と入力すると、現在割り当て中の全 DD のリストを表示する診断ツール

**出典:** z / OS ISPF User's Guide Vol I (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 復旧検査のコマンドの基本機能でコマンドの基本機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. コマンドの基本機能の出力を取らず復旧検査のコマンドの基本機能の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧検査の確認結果にする。 ✅
    - C. ST OSKBUTIL を省略して復旧検査のコマンドの基本機能の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のコマンドの基本機能へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧検査のコマンドの基本機能において選択記号 B を採用し、識別名は復旧検査です。復旧検査のコマンドの基本機能においてコマンドの基本機能は説明欄の「復旧検査のコマンドの基本機能に関係する定義値と表示行を照合する復旧検査項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は復旧検査です。復旧検査のコマンドの基本機能の証跡を読む担当者は、コマンドの基本機能の属性行と IEF142I を合わせて追跡し、背景名は復旧検査です。誤答側の問題点を分けます。 A: 復旧検査のコマンドの基本機能は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧検査ではありません。 B: 復旧検査のコマンドの基本機能は対象出力と項目説明を結び、根拠を残すので復旧検査です。 C: 復旧検査のコマンドの基本機能は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため復旧検査ではありません。 D: 復旧検査のコマンドの基本機能は別カテゴリの確認を流用しており、コマンドの基本機能の根拠にならないため復旧検査ではありません。復旧検査のコマンドの基本機能に出るコマンドの基本機能はユーティリティの運用手順で意味を確認する対象であり、用語名は復旧検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（1件）"
    **コマンドの基本機能**

    - 検証目的: 構文記録のコマンドの基本機能について、コマンドの基本機能は、TSO/ISPF セッションのコマンド行で 'TSO ISRDDN' (または短縮 'DDLIST') と入力すると、現在割り当て中の全 DD のリスに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020121の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、構文記録のコマンドの基本機能の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にコマンドの基本機能を指定し、OSKB020121の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND コマンドの基本機能
    CASE OSKB020121
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM コマンドの基本機能
    CASE OSKB020121
    SOURCE z/OS Utilities
    ```

    コマンドの基本機能とOSKB020121が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020121を同じ出力で読み、構文記録のコマンドの基本機能の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020121
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020121
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I コマンドの基本機能 PROCESSING STARTED
    IEF142I OSKB020121 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020121が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の コマンドの基本機能 と OSKB020121 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF User's Guide Vol I (z / OS 3.1)



### コンカテネーション順表示 {#c40-i0257}
*分類: ISRDDN*  ・  難易度: 中級

コンカテネーション順表示は、ユーティリティのISRDDNで機能名、見出し、または確認対象として参照する項目です。コンカテネーションされた DD は 1 行ずつ展開され、解決順 (先頭から検索される順) も併せて表示される。CLIST/REXX の挙動解析の決定打

**出典:** z / OS ISPF User's Guide Vol I (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開判定のコンカテネーション順表示でコンカテネーション順表示の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. コンカテネーション順表示の出力を取らず展開判定のコンカテネーション順表示の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開判定の確認結果にする。 ✅
    - C. ST OSKBUTIL を省略して展開判定のコンカテネーション順表示の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のコンカテネーション順表示へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定のコンカテネーション順表示において選択記号 B を採用し、識別名は展開判定です。展開判定のコンカテネーション順表示においてコンカテネーション順表示は説明欄の「展開判定のコンカテネーション順表示に関係する定義値と表示行を照合する展開判定項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は展開判定です。展開判定のコンカテネーション順表示の証跡を読む担当者は、コンカテネーション順表示の属性行と IEF142I を合わせて追跡し、背景名は展開判定です。誤答側の問題点を分けます。 A: 展開判定のコンカテネーション順表示は名称や説明のみに寄り、状態を示す出力本文が不足するため展開判定ではありません。 B: 展開判定のコンカテネーション順表示は対象出力と項目説明を結び、根拠を残すので展開判定です。 C: 展開判定のコンカテネーション順表示は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため展開判定ではありません。 D: 展開判定のコンカテネーション順表示は別カテゴリの確認を流用しており、コンカテネーション順表示の根拠にならないため展開判定ではありません。展開判定のコンカテネーション順表示に出るコンカテネーション順表示はユーティリティの運用手順で意味を確認する対象であり、用語名は展開判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（1件）"
    **コンカテネーション順表示**

    - 検証目的: 終端記録のコンカテネーション順表示について、コンカテネーション順表示は、ユーティリティの ISRDDN で機能名、見出し、または確認対象として参照する項目です。コンカテネーションされた DD は 1 行ずつ展開され、解決に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020125の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、終端記録のコンカテネーション順表示の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にコンカテネーション順表示を指定し、OSKB020125の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND コンカテネーション順表示
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM コンカテネーション順表示
    CASE OSKB020125
    SOURCE z/OS Utilities
    ```

    コンカテネーション順表示とOSKB020125が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020125を同じ出力で読み、終端記録のコンカテネーション順表示の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020125
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I コンカテネーション順表示 PROCESSING STARTED
    IEF142I OSKB020125 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020125が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の コンカテネーション順表示 と OSKB020125 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS ISPF User's Guide Vol I (z / OS 3.1)




## ユーティリティ > LISTPS

### 概要 {#c40-i0258}
*分類: LISTPS*  ・  難易度: 中級

順次データセット (DSORG=PS) の DCB やボリューム所在を一覧する場合、独立した「LISTPS」ユーティリティではなく ISPF 3.4 / IDCAMS LISTCAT / IEHLIST LISTVTOC で代替するのが現代の標準。レガシードキュメントで LISTPS という呼称を見かけたら IEHLIST 系の操作を指していると解釈する

**出典:** z / OS DFSMS Access Method Services Commands (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 警告検査の概要に関係する概要の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告検査として残す。 ✅
    - B. 概要の名称と担当者名のみを残して警告検査の概要の表示本文を確認対象に含めない。
    - C. ユーティリティ以外の画面で警告検査の概要を確認し同じ証跡として扱ったことにする。
    - D. IEF142I の有無を見ず警告検査の概要の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査の概要において選択記号 A を採用し、識別名は警告検査です。警告検査の概要において概要は説明欄の「概要の用途をユーティリティの表示で確認する警告検査項目」と ST OSKBUTIL または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査の概要に関連して、z/OS Utilitiesでは概要の表示属性と IEF142I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査の概要は対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査の概要は名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査の概要は別カテゴリの確認を流用しており、概要の根拠にならないため警告検査ではありません。 D: 警告検査の概要は戻り値や記録番号に寄り、IEF142I や属性表示を落とすため警告検査ではありません。警告検査の概要で使う概要という用語はユーティリティで扱う確認対象であり、用語名は警告検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800 / zOS31_ieav200


??? note "検証手順（1件）"
    **概要**

    - 検証目的: 変更整理の概要について、順次データセット (DSORG=PS) の DCB やボリューム所在を一覧する場合、独立した「LISTPS」ユーティリティではなく ISPF 3.4 / IDCAMS LIに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、変更整理の概要の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄に概要を指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 概要
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 概要
    CASE OSKB020120
    SOURCE z/OS Utilities
    ```

    概要とOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB020120を同じ出力で読み、変更整理の概要の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020120
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I 概要 PROCESSING STARTED
    IEF142I OSKB020120 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の 概要 と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands (z / OS 3.1)




## その他

### その他（特定項目に紐づかないQA・手順） {#c40-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? note "検証手順（5件）"
    **PDS から PDSE 変換**

    - 検証目的: 変更照合のから 変換について、INDD が PDS、OUTDD が PDSE であれば、IEBCOPY 経由でフォーマット変換コピーが行われる。逆方向も可に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBUTILを実行し、IEF142Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBUTIL を入力し、変更照合のから 変換の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPDS から PDSE 変換を指定し、OSKB010040の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PDS から PDSE 変換
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PDS から PDSE 変換
    CASE OSKB010040
    SOURCE z/OS Utilities
    ```

    PDS から PDSE 変換とOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF142IとOSKB010040を同じ出力で読み、変更照合のから 変換の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBUTIL
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010040
    //STEP1 EXEC PGM=OSKBUTIL
    IEF142I PDS から PDSE 変換 PROCESSING STARTED
    IEF142I OSKB010040 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    IEF142IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBUTIL が画面・出力に表示されること
    ② ステップ2 の PDS から PDSE 変換 と OSKB010040 が画面・出力に表示されること
    ③ ステップ3 の IEF142I と OSKB010040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Utilities (z / OS 3.1)

    ---

    **SORT 型コード FI (Fixed-point Signed I**

    - 検証目的: 監査照合の型コードについて、SORT 型コード FI (Fixed-point Signed Integer)は、ユーティリティの DFSORT で機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、監査照合の型コードの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にSORT 型コード FI (Fixeを指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SORT 型コード FI (Fixe
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SORT 型コード FI (Fixe
    CASE OSKB020039
    SOURCE z/OS Utilities
    ```

    SORT 型コード FI (FixeとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020039を同じ出力で読み、監査照合の型コードの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020039
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I SORT 型コード FI (Fixed-poin PROCESSING STARTED
    IEF142I OSKB020039 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の SORT 型コード FI (Fixe と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)

    ---

    **OUTREC FIELDS=(など)**

    - 検証目的: 順序追跡のなどについて、ユーティリティの DFSORT では、対象資源、指定値、実行時の出力を対応付けて確認します。DFSORT は、ユーティリティの運用で指定値、構文上の位置、反映後の出力を読み分けるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、順序追跡のなどの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にOUTREC FIELDS=(など)を指定し、OSKB020055の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND OUTREC FIELDS=(など)
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM OUTREC FIELDS=(など)
    CASE OSKB020055
    SOURCE z/OS Utilities
    ```

    OUTREC FIELDS=(など)とOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020055を同じ出力で読み、順序追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020055
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I OUTREC FIELDS=(など) PROCESSING STARTED
    IEF142I OSKB020055 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の OUTREC FIELDS=(など) と OSKB020055 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)

    ---

    **OUTREC リテラル C'など'**

    - 検証目的: 値域追跡のリテラル などについて、ユーティリティの DFSORT では、対象資源、指定値、実行時の出力を対応付けて確認します。DFSORT は、ユーティリティの運用で指定値、構文上の位置、反映後の出力を読み分けるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、値域追跡のリテラル などの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にOUTREC リテラル C'など'を指定し、OSKB020056の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND OUTREC リテラル C'など'
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM OUTREC リテラル C'など'
    CASE OSKB020056
    SOURCE z/OS Utilities
    ```

    OUTREC リテラル C'など'とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020056を同じ出力で読み、値域追跡のリテラル などの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020056
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I OUTREC リテラル C'など' PROCESSING STARTED
    IEF142I OSKB020056 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の OUTREC リテラル C'など' と OSKB020056 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)

    ---

    **OUTREC リテラル X'など'**

    - 検証目的: 警告追跡のリテラル などについて、ユーティリティの DFSORT では、対象資源、指定値、実行時の出力を対応付けて確認します。DFSORT は、ユーティリティの運用で指定値、構文上の位置、反映後の出力を読み分けるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBSORTを実行し、ICE000Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBSORT を入力し、警告追跡のリテラル などの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にOUTREC リテラル X'など'を指定し、OSKB020057の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND OUTREC リテラル X'など'
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM OUTREC リテラル X'など'
    CASE OSKB020057
    SOURCE z/OS Utilities
    ```

    OUTREC リテラル X'など'とOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ICE000IとOSKB020057を同じ出力で読み、警告追跡のリテラル などの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBSORT
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB020057
    //STEP1 EXEC PGM=OSKBSORT
    ICE000I OUTREC リテラル X'など' PROCESSING STARTED
    IEF142I OSKB020057 STEP1 - STEP WAS EXECUTED - COND CODE 0000
    ```

    ICE000IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBSORT が画面・出力に表示されること
    ② ステップ2 の OUTREC リテラル X'など' と OSKB020057 が画面・出力に表示されること
    ③ ステップ3 の ICE000I と OSKB020057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSORT Application Programming Guide (z / OS 3.1)

