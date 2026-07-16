---
search:
  exclude: true
---

# Db2 for z/OS — 詳細 (6/7)

[← Db2 for z/OS の概要へ戻る](index.md)


## Db2 for z/OS > 導入・移行・サブシステムパラメータ > 導入・移行ジョブ

### DSNTIJUZ {#c07-i0390}
*分類: 導入・移行・サブシステムパラメータ > 導入・移行ジョブ*  ・  難易度: 中級

DSNTIJUZは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（2問）"
    **問題.** 導入後に実行時パラメータのロードモジュールを作り、選択したDSN6系マクロ値を反映します。実行するジョブはどれですか。

    - A. DSNTIJRT
    - B. DSNTIJUZ ✅
    - C. DSNTEP2
    - D. DSNJU004

    正解: **B** ／ 難易度: 中級

    **解説:** ZPARMを作る導入ジョブを選ぶため、Bが該当します。誤答AはDb2提供ルーチンの構成で使うジョブです。誤答CはSQL実行サンプルプログラムで、誤答Dはログ目録を印刷するユーティリティです。警告の扱いを確認して次工程へ進みます；背景には選択したサブシステムパラメータをロードモジュールへ組み込む導入ジョブが DSNTIJUZ です、このジョブは DSNZPxxx を作成し、Db2 起動時に参照できる形へ整えます、戻りコード4の警告が出た場合は、継続前に警告内容と生成されたメンバー名を確認しますという関係があり、この区別で確認する名称は「DSNTIJUZ」です。

    **出典:** Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages

    ---

    **問題.** 導入パネルで選んだ実行時パラメータを、DSNZPxxx としてアセンブル・リンクします。実行するジョブはどれですか。

    - A. DSNTIJUA
    - B. DSNTIJUM
    - C. DSNTIJUZ ✅
    - D. DSNTIJUL

    正解: **C** ／ 難易度: 中級

    **解説:** サブシステムパラメータモジュールを作る導入ジョブなので、Cを選びます。誤答Aはアプリケーション既定値のジョブです。誤答Bはオフラインメッセージ変換用CCSIDの資材で、誤答DはDDF関連のBSDS情報を更新します；背景には導入・移行ジョブ群で DSNZPxxx を作成するジョブが DSNTIJUZ です、ISPF パネルで選んだ実行時パラメータを DSN6ARVP、DSN6FAC、DSN6GRP、DSN6LOGP、DSN6SPRM、DSN6SYSP の展開として組み込みます、戻りコード4の警告は、次工程へ進む前に内容を判断しますという関係があり、この区別で確認する名称は「DSNTIJUZ」です。

    **出典:** Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542


??? note "検証手順（2件）"
    **DSNTIJUZ**

    - 検証目的: 範囲確認の導入・移行ジョブについて、DSNTIJUZ は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、範囲確認の導入・移行ジョブの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJUZを指定し、OSKB010011の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJUZ
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJUZ
    CASE OSKB010011
    SOURCE Db2 for z/OS
    ```

    DSNTIJUZとOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010011を同じ出力で読み、範囲確認の導入・移行ジョブの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010011
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010011
    ```

    DSNV401IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJUZ と OSKB010011 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

    ---

    **DSNTIJUZ**

    - 検証目的: 置換検査の導入・初期化・起動反映について、DSNTIJUZ は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、置換検査の導入・初期化・起動反映の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJUZを指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJUZ
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJUZ
    CASE OSKB020064
    SOURCE Db2 for z/OS
    ```

    DSNTIJUZとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020064を同じ出力で読み、置換検査の導入・初期化・起動反映の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020064
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020064
    ```

    DSNV401IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJUZ と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Performance p.216




## Db2 for z/OS > 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ

### DSNTIJIC {#c07-i0391}
*分類: 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ*  ・  難易度: 中級

DSNTIJICは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** 導入後に Db2 catalog と directory を回復できるよう、対象表スペースのイメージコピーを作成します。使うジョブはどれですか。

    - A. DSNTIJIC ✅
    - B. DSNTIJRT
    - C. DSNTIJSO
    - D. DSNTIJSA

    正解: **A** ／ 難易度: 中級

    **解説:** カタログとディレクトリのバックアップを作る場面なので、Aを選びます。B: ルーチンの導入と構成を行うジョブです。C: 停止用ジョブで、Dは開始用ジョブです。回復性のためのコピー作成という点で区別します；背景にはDb2 の導入後保守で使う DSNTIJIC は、Db2 ディレクトリとカタログのイメージコピーを作成します、ジョブには対象表スペースの一覧が含まれ、COPY ユーティリティでディスクまたはテープへ退避します、失敗時は装置設定、I/O エラー、ログを確認しますという関係があり、この区別で確認する名称は「DSNTIJIC」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891



### DSNTIJRT {#c07-i0392}
*分類: 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ*  ・  難易度: 中級

DSNTIJRTは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** Db2提供ルーチンと支援オブジェクトを導入し、DSNTRIN で構成制御文を処理します。使うジョブはどれですか。

    - A. DSNTIJRV
    - B. DSNTIJRT ✅
    - C. DSNTIJIC
    - D. DSNTIJUL

    正解: **B** ／ 難易度: 中級

    **解説:** 提供ルーチンを導入・構成する作業なので、Bが該当します。A: 導入済みルーチンの検証を行います。C: catalogとdirectoryを退避する別ジョブです。D: DDF関連情報をBSDSに更新するジョブです；背景には導入・移行の保守ジョブとして、DSNTIJRT は Db2-supplied routines と supporting objects を導入・構成します、DSNTRIN を実行し、構成制御文に基づいて WLMENV や GRANTTO などの指定を反映します、実行前には許可先と既存パッケージの扱いを確認しますという関係があり、この区別で確認する名称は「DSNTIJRT」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891



### DSNTIJRV {#c07-i0393}
*分類: 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ*  ・  難易度: 中級

DSNTIJRVは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** Db2提供ルーチンを導入した後、成功・警告・失敗を含む検証レポートで結果を確認します。該当するジョブはどれですか。

    - A. DSNTIJUL
    - B. DSNTIJSA
    - C. DSNTIJSO
    - D. DSNTIJRV ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 導入済みルーチンの検証レポートを見る作業なので、Dを選びます。A: DDF関連のBSDS更新です。B: Db2開始のサンプルジョブです。C: 停止操作であり、ルーチン検証レポートは出しません。成功、警告、失敗の件数も確認します；背景にはDSNTIJRT の後続確認として、DSNTIJRV は Db2-supplied routines の導入結果を検証します、導入後検証では、新機能に依存するルーチンを検証し、成功、警告、失敗を示すレポートを出します、ルーチンが期待どおり使える状態かを確かめますという関係があり、この区別で確認する名称は「DSNTIJRV」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891


??? note "検証手順（1件）"
    **DSNTIJRV**

    - 検証目的: 値域確認の導入後検証・保守ジョブについて、DSNTIJRV は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、値域確認の導入後検証・保守ジョブの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJRVを指定し、OSKB010016の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJRV
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJRV
    CASE OSKB010016
    SOURCE Db2 for z/OS
    ```

    DSNTIJRVとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010016を同じ出力で読み、値域確認の導入後検証・保守ジョブの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010016
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010016
    ```

    DSNV401IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJRV と OSKB010016 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### DSNTIJSA {#c07-i0394}
*分類: 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ*  ・  難易度: 中級

DSNTIJSAは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** 保守作業後、z/OSMF workflow から stand-alone program を呼び出して Db2 を開始します。該当するサンプルジョブはどれですか。

    - A. DSNTIJSO
    - B. DSNTIJIC
    - C. DSNTIJSA ✅
    - D. DSNTIJUM

    正解: **C** ／ 難易度: 中級

    **解説:** サブシステム開始を行うサンプルジョブに当たるため、Cを選びます。A: 停止のジョブです。B: catalog と directory のコピーを作ります。D: offline message generator CCSID module を定義する導入ジョブです；背景にはz/OSMF workflow での Db2 導入・移行自動化では、DSNTIJSA がサブシステム開始のサンプルジョブになります、DSNTMVSB stand-alone program を呼び出して開始を実行します、停止やログ初期化の後に、開始結果を確認しますという関係があり、この区別で確認する名称は「DSNTIJSA」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891


??? note "検証手順（1件）"
    **DSNTIJSA**

    - 検証目的: 順序確認の導入後検証・保守ジョブについて、DSNTIJSA は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、順序確認の導入後検証・保守ジョブの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJSAを指定し、OSKB010015の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJSA
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJSA
    CASE OSKB010015
    SOURCE Db2 for z/OS
    ```

    DSNTIJSAとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010015を同じ出力で読み、順序確認の導入後検証・保守ジョブの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010015
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010015
    ```

    DSNV401IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJSA と OSKB010015 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### DSNTIJSO {#c07-i0395}
*分類: 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ*  ・  難易度: 中級

DSNTIJSOは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** 任意保守ステップで、active log 初期化の前に Db2 サブシステムを停止する必要があります。選ぶジョブはどれですか。

    - A. DSNTIJSA
    - B. DSNTIJIC
    - C. DSNTIJRV
    - D. DSNTIJSO ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 停止を行うジョブなので、Dが正解です。A: 停止後にサブシステムを開始するジョブです。B: カタログとディレクトリのイメージコピーです。C: Db2提供ルーチンの検証で、停止操作そのものではありません；背景には停止を伴う導入後保守で使う DSNTIJSO は、Db2 サブシステムを停止するために用意されます、DSNTIPMJ の任意ステップでは、このジョブで停止し、必要なら active logs を初期化してから DSNTIJSA で開始します、停止前にはジョブ状況と利用者影響を確認しますという関係があり、この区別で確認する名称は「DSNTIJSO」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891


??? note "検証手順（1件）"
    **DSNTIJSO**

    - 検証目的: 比較確認の導入後検証・保守ジョブについて、DSNTIJSO は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、比較確認の導入後検証・保守ジョブの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJSOを指定し、OSKB010014の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJSO
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJSO
    CASE OSKB010014
    SOURCE Db2 for z/OS
    ```

    DSNTIJSOとOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010014を同じ出力で読み、比較確認の導入後検証・保守ジョブの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010014
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010014
    ```

    DSNV401IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJSO と OSKB010014 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### 移行検証 {#c07-i0396}
*分類: 導入・移行・サブシステムパラメータ > 導入後検証・保守ジョブ*  ・  難易度: 中級

移行検証は、導入・移行・サブシステムパラメータの中で導入後検証・保守ジョブに関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 導入・移行で理解する資材として扱い、具体的な画面操作やJCL全文は手順書側へ送るとは分けて扱います

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** Db2 13 への移行可否を判断するため、code level と catalog/function level を DISPLAY GROUP 出力で見ます。これは何の確認ですか。

    - A. active log 初期化
    - B. 移行検証 ✅
    - C. DDFポート更新
    - D. ルーチン導入

    正解: **B** ／ 難易度: 中級

    **解説:** 移行準備状態をレベル値で判断する確認なので、Bが正解です。A: ログデータセットの事前整形です。C: BSDSの通信レコード更新です。D: 提供ルーチンの構成作業で、グループ全体の移行可否判定とは別です；背景にはDb2 の移行検証は、code level、catalog level、current function level を DISPLAY GROUP などで確認する作業です、highest activated function level も見ます、機能レベル活性化や移行可否は、全メンバーのコード水準とカタログ状態がそろっているかで判断しますという関係があり、この区別で確認する名称は「移行検証」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891




## Db2 for z/OS > 性能・モニタリング・トレース > IFCID

### IFCID 0150 {#c07-i0397}
*分類: 性能・モニタリング・トレース > IFCID*  ・  難易度: 上級

IFCID 0150は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** trace output に出た番号から、どの event record を取得したかを確認します。番号体系として見るものはどれですか。

    - A. IFCID ✅
    - B. DBRM
    - C. GBP
    - D. LOB

    正解: **A** ／ 難易度: 中級

    **解説:** trace record の識別番号体系なので、A が正解です。B: precompile 後の SQL 情報です。C: group buffer pool です。D: large object のデータ型です。class と取得目的を合わせて読みます；背景にはIFCID 0150 は、Db2 for z/OS の trace record を識別する IFCID の一つとして扱います、START TRACE や trace output の読み取りでは、この番号から取得 event を判断します、実務では番号単体を暗記するより、class、取得目的、DSNWMSGS などの説明資料で確かめますという関係があり、この区別で確認する名称は「0150」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **IFCID 0150**

    - 検証目的: 呼出照合のDb2について、IFCID 0150は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、呼出照合のDb2の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にIFCID 0150を指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND IFCID 0150
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM IFCID 0150
    CASE OSKB020023
    SOURCE Db2 for z/OS
    ```

    IFCID 0150とOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020023を同じ出力で読み、呼出照合のDb2の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020023
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020023
    ```

    DSNV401IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の IFCID 0150 と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### IFCID 0199 {#c07-i0398}
*分類: 性能・モニタリング・トレース > IFCID*  ・  難易度: 上級

IFCID 0199は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** 資料では 0199、別の出力では 199 と見えます。同じ event record として照合する番号体系はどれですか。

    - A. SQLCODE
    - B. IFCID ✅
    - C. PGSTEAL
    - D. APPLCOMPAT

    正解: **B** ／ 難易度: 中級

    **解説:** trace record を区別する IFCID の表記なので、B が該当します。A: SQL 実行結果コードです。C: page steal の方式です。D: application compatibility level です。leading zero の有無を主な根拠にして異なる記録と扱わないよう確認します；背景にはIFCID 0199 は、Db2 for z/OS の trace record を区別する IFCID の一つです、3 桁または 4 桁の表記で示されることがあり、同じ番号でも資料によって leading zero が付きます、調査では START TRACE の指定、出力先、record 説明を対応付けますという関係があり、この区別で確認する名称は「0199」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **IFCID 0199**

    - 検証目的: 置換照合のDb2について、IFCID 0199は、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVS コマンド一般ではなく、Db2側で何が変わり、どの表示で確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、置換照合のDb2の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にIFCID 0199を指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND IFCID 0199
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM IFCID 0199
    CASE OSKB020024
    SOURCE Db2 for z/OS
    ```

    IFCID 0199とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020024を同じ出力で読み、置換照合のDb2の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020024
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020024
    ```

    DSNV401IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の IFCID 0199 と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference




## Db2 for z/OS > 性能・モニタリング・トレース > アクセスパス診断

### EXPLAIN {#c07-i0399}
*分類: 性能・モニタリング・トレース > アクセスパス診断*  ・  難易度: 中級

EXPLAINは、Db2 for z/OSのアクセスパス診断で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。アクセスパス診断では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（6問）"
    **問題.** 説明表出力を導入設計で確認します。Db2の作業記録にアクセスパス情報の出力の根拠を残します。導入レビューで、値の目的と戻し方を設計書へ残す必要があります。どの項目を中心に確認しますか。

    - A. KEEPDYNAMIC
    - B. APREUSE
    - C. PLAN_TABLE
    - D. EXPLAIN ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答説明表出力はDです。論点説明表出力における指定名 EXPLAIN の確認軸名は説明表出力確認です。エスキューエル変更前後の差分を確認しますので、目的名は説明表出力目的です。説明表出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は説明表出力説明です。誤答A説明表出力は準備済み動的SQL文の保持の選択で、主題は説明表出力です。除外A説明表出力では準備済み動的SQL文の保持を外す理由も説明表出力誤答です。誤答B説明表出力は前回アクセスパスの再利用の選択で、主題は説明表出力です。除外B説明表出力では前回アクセスパスの再利用を外す理由も説明表出力誤答です。誤答C説明表出力はEXPLAIN基本表の選択で、主題は説明表出力です。除外C説明表出力ではEXPLAIN基本表を外す理由も説明表出力誤答です。Dが正解です。論点説明表出力の指定名 EXPLAIN が該当します。目的説明表出力で読む説明表の根拠名は説明表出力根拠です。初出語説明表出力として、指定名 EXPLAIN はDb2の指定または確認表であり焦点は説明表出力定義です。位置付け説明表出力はアクセスパス情報の出力位置です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide

    ---

    **問題.** 説明表出力を変更審査で確認します。Db2の作業記録にアクセスパス情報の出力の根拠を残します。本番変更前に、既存パッケージへ与える影響を説明する必要があります。どの指定または表を確認しますか。

    - A. EXPLAIN ✅
    - B. PATH
    - C. ACTION
    - D. DEGREE

    正解: **A** ／ 難易度: 中級

    **解説:** 正答説明表出力はAです。論点説明表出力における指定名 EXPLAIN の確認軸名は説明表出力確認です。エスキューエル変更前後の差分を確認しますので、目的名は説明表出力目的です。説明表出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は説明表出力説明です。Aが正解です。論点説明表出力の指定名 EXPLAIN が該当します。目的説明表出力で読む説明表の根拠名は説明表出力根拠です。誤答B説明表出力はルーチン探索順序の選択で、主題は説明表出力です。除外B説明表出力ではルーチン探索順序を外す理由も説明表出力誤答です。誤答C説明表出力は追加と置換の扱いの選択で、主題は説明表出力です。除外C説明表出力では追加と置換の扱いを外す理由も説明表出力誤答です。誤答D説明表出力は並列実行の許可の選択で、主題は説明表出力です。除外D説明表出力では並列実行の許可を外す理由も説明表出力誤答です。初出語説明表出力として、指定名 EXPLAIN はDb2の指定または確認表であり焦点は説明表出力定義です。位置付け説明表出力はアクセスパス情報の出力位置です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide

    ---

    **問題.** 説明表出力を性能調査で確認します。Db2の作業記録にアクセスパス情報の出力の根拠を残します。SQL応答時間の変化を追うため、選択されたアクセスパスの根拠を残します。どの情報を使うのが適切ですか。

    - A. APREUSE
    - B. EXPLAIN ✅
    - C. RELEASE
    - D. KEEPDYNAMIC

    正解: **B** ／ 難易度: 中級

    **解説:** 正答説明表出力はBです。論点説明表出力における指定名 EXPLAIN の確認軸名は説明表出力確認です。エスキューエル変更前後の差分を確認しますので、目的名は説明表出力目的です。説明表出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は説明表出力説明です。誤答A説明表出力は前回アクセスパスの再利用の選択で、主題は説明表出力です。除外A説明表出力では前回アクセスパスの再利用を外す理由も説明表出力誤答です。Bが正解です。論点説明表出力の指定名 EXPLAIN が該当します。目的説明表出力で読む説明表の根拠名は説明表出力根拠です。誤答C説明表出力は資源解放の時点の選択で、主題は説明表出力です。除外C説明表出力では資源解放の時点を外す理由も説明表出力誤答です。誤答D説明表出力は準備済み動的SQL文の保持の選択で、主題は説明表出力です。除外D説明表出力では準備済み動的SQL文の保持を外す理由も説明表出力誤答です。初出語説明表出力として、指定名 EXPLAIN はDb2の指定または確認表であり焦点は説明表出力定義です。位置付け説明表出力はアクセスパス情報の出力位置です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide

    ---

    **問題.** 説明表出力を障害復旧で確認します。Db2の作業記録にアクセスパス情報の出力の根拠を残します。変更後に性能や権限の問題が出たため、切り戻しと原因確認の証跡を集めます。優先して見る項目はどれですか。

    - A. SWITCH(PREVIOUS)
    - B. PLANMGMT
    - C. EXPLAIN ✅
    - D. APCOMPARE

    正解: **C** ／ 難易度: 中級

    **解説:** 正答説明表出力はCです。論点説明表出力における指定名 EXPLAIN の確認軸名は説明表出力確認です。エスキューエル変更前後の差分を確認しますので、目的名は説明表出力目的です。説明表出力で読む説明表の列値は実行資産とアクセスパスの根拠になり、Db2のバインドや再バインド後に説明する論点は説明表出力説明です。誤答A説明表出力は前回コピーへの切り替えの選択で、主題は説明表出力です。除外A説明表出力では前回コピーへの切り替えを外す理由も説明表出力誤答です。誤答B説明表出力はパッケージコピーの保持の選択で、主題は説明表出力です。除外B説明表出力ではパッケージコピーの保持を外す理由も説明表出力誤答です。Cが正解です。論点説明表出力の指定名 EXPLAIN が該当します。目的説明表出力で読む説明表の根拠名は説明表出力根拠です。誤答D説明表出力はアクセスパス差分の比較の選択で、主題は説明表出力です。除外D説明表出力ではアクセスパス差分の比較を外す理由も説明表出力誤答です。初出語説明表出力として、指定名 EXPLAIN はDb2の指定または確認表であり焦点は説明表出力定義です。位置付け説明表出力はアクセスパス情報の出力位置です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Performance / Db2_zOS_SQL_Reference / Db2_zOS_AppProg_SQL_Guide

    ---

    **問題.** 再バインド後のアクセスパスを後で比較できるように、作成時点で説明表へ情報を残したい状況です。使うオプションはどれですか。

    - A. RELEASE
    - B. DYNAMICRULES
    - C. EXPLAIN ✅
    - D. IMMEDWRITE

    正解: **C** ／ 難易度: 中級

    **解説:** アクセスパス証跡を残すなら C が該当し、説明表への出力は EXPLAIN で指定します。性能調査や変更前後比較の根拠になります。A: 資源解放のタイミングです。B: 動的 SQL の許可検査規則です。D: 共有バッファ依存ページの書き込み制御です；背景にはアクセスパス証跡を残す BIND/REBIND の EXPLAIN は、最適化結果を説明表へ出力します、再バインド前後の比較、性能レビュー、索引変更の影響確認で重要な証跡になります、対象パッケージ、出力表、採取タイミングを合わせて管理しますという関係があり、この区別で確認する名称は「EXPLAIN」です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_AppProg_SQL_Guide / Db2_zOS_Performance

    ---

    **問題.** 遅い SQL がどの索引を使うか、実行前に access path を記録して確認します。使う機能はどれですか。

    - A. EXPLAIN ✅
    - B. RECOVER
    - C. LOCKS
    - D. DSNTEP2

    正解: **A** ／ 難易度: 中級

    **解説:** SQL の access path を記録するため、A が正解です。B: object を復旧する保守機能です。C: lock holder や waiter を見る表示です。D: SQL を batch 実行する sample program です。統計と bind 条件もそろえて解釈します；背景にはEXPLAIN は、Db2 for z/OS で SQL の access path を事前または事後に確認する機能です、optimizer が選んだ表アクセス、索引利用、join 順序を PLAN_TABLE などに記録します、性能調査では統計情報、bind 時点、query number をそろえて結果を読みますという関係があり、この区別で確認する名称は「EXPLAIN」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172



### PLAN_TABLE analysis {#c07-i0400}
*分類: 性能・モニタリング・トレース > アクセスパス診断*  ・  難易度: 中級

PLAN_TABLE analysisは、Db2 for z/OSのアクセスパス診断で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。アクセスパス診断では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** 結果表を読み、join 順序や利用 index を比較します。中心になる作業はどれですか。

    - A. archive 選定
    - B. PLAN分析 ✅
    - C. role 付与
    - D. WLM 起動

    正解: **B** ／ 難易度: 中級

    **解説:** 結果表の内容を分析する作業なので、B が該当します。A: log 保管や復旧設計の話です。C: 権限をまとめて付与する操作です。D: address space の起動管理です。列の意味と統計時点をそろえて読みます；背景にはアクセスパス診断では、EXPLAIN 結果を PLAN_TABLE から読み解く作業を PLAN_TABLE analysis と呼びます、access method、index 名、join 順序、predicate の扱いを確認できます、環境差を比べる場合は、統計、APPLCOMPAT、表の列構成をそろえますという関係があり、この区別で確認する名称は「PLAN_TABLE」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **PLAN_TABLE analysis**

    - 検証目的: 警告確認のアクセスパス診断について、PLAN_TABLE analysisは、Db2 for z/OS のアクセスパス診断で用いる Db2の性能診断やモニタリングで使う情報または収集単位です。SQL の実行計画、待に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、警告確認のアクセスパス診断の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にPLAN_TABLE analysiを指定し、OSKB020017の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND PLAN_TABLE analysi
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM PLAN_TABLE analysi
    CASE OSKB020017
    SOURCE Db2 for z/OS
    ```

    PLAN_TABLE analysiとOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020017を同じ出力で読み、警告確認のアクセスパス診断の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020017
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020017
    ```

    DSNV401IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の PLAN_TABLE analysi と OSKB020017 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### RUNSTATS impact on access path {#c07-i0401}
*分類: 性能・モニタリング・トレース > アクセスパス診断*  ・  難易度: 中級

RUNSTATS impact on access pathは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** RUNSTATS 後に同じ SQL の索引選択が変わりました。確認すべき影響はどれですか。

    - A. routine 権限
    - B. log offload
    - C. DDF port
    - D. 統計影響 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 統計更新が access path を変えた可能性を見るため、D が合います。A: stored procedure などの実行権限です。B: active log の退避処理です。C: distributed access の接続口です。RUNSTATS 後は EXPLAIN と REBIND を対で確認します；背景にはRUNSTATS impact on access path は、Db2 for z/OS の統計更新が access path 選択へ与える影響を扱います、件数、分布、列相関の統計が変わると、同じ SQL でも別の索引や join 順序になる場合があります、実施前後では EXPLAIN 結果と REBIND 有無を照合しますという関係があり、この区別で確認する名称は「RUNSTATS」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **RUNSTATS impact on access path**

    - 検証目的: 監査確認のアクセスパス診断について、RUNSTATS impact on access pathは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、監査確認のアクセスパス診断の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にRUNSTATS impact onを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND RUNSTATS impact on
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM RUNSTATS impact on
    CASE OSKB020019
    SOURCE Db2 for z/OS
    ```

    RUNSTATS impact onとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020019を同じ出力で読み、監査確認のアクセスパス診断の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020019
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020019
    ```

    DSNV401IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の RUNSTATS impact on と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### access path problem {#c07-i0402}
*分類: 性能・モニタリング・トレース > アクセスパス診断*  ・  難易度: 中級

access path problemは、性能・モニタリング・トレースの中でアクセスパス診断に関わるDb2技術項目です。実行単位、BIND操作、アクセスパス、互換性、再バインド時の影響。一方で、SQL文の業務意味、EXPLAIN結果の詳細分析手順、JCL手順。 性能観測・分析の観点として扱い、資源そのものの定義とは分けるとは分けて扱います

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** 統計更新後に SQL の入出力が急増し、以前と違う経路が選ばれた疑いがあります。調べる問題はどれですか。

    - A. GBP duplex
    - B. DSNL message
    - C. 経路問題 ✅
    - D. COPYDDN

    正解: **C** ／ 難易度: 中級

    **解説:** SQL の選択経路が悪化した疑いなので、C と判断します。A: data sharing 構造の二重化です。B: DDF 系 message の確認です。D: image copy の DD 名指定です。access path problem は統計と REBIND 条件を結び付けて見ます；背景にはaccess path problem は、Db2 for z/OS で optimizer が期待と違う経路を選び、応答悪化や入出力増加が起きる状態です、原因には統計不足、索引不足、parameter marker、REBIND 条件差があります、調査では EXPLAIN、RUNSTATS、REBIND 履歴を分けて確認しますという関係があり、この区別で確認する名称は「problem」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **access path problem**

    - 検証目的: 復旧確認のアクセスパス診断について、access path problemは、性能・モニタリング・トレースの中でアクセスパス診断に関わる Db2技術項目です。実行単位、BIND 操作、アクセスパス、互換性、再バイに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、復旧確認のアクセスパス診断の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にaccess path probleを指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND access path proble
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM access path proble
    CASE OSKB020018
    SOURCE Db2 for z/OS
    ```

    access path probleとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020018を同じ出力で読み、復旧確認のアクセスパス診断の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020018
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020018
    ```

    DSNV401IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の access path proble と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference




## Db2 for z/OS > 性能・モニタリング・トレース > トレース種別

### accounting trace {#c07-i0403}
*分類: 性能・モニタリング・トレース > トレース種別*  ・  難易度: 中級

accounting traceは、Db2 for z/OSのトレース種別で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。トレース種別では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** 特定 plan の CPU と待ち時間を thread 単位で分析し、利用者別の影響を見ます。使う trace はどれですか。

    - A. thread使用量記録 ✅
    - B. COPY utility
    - C. BP0
    - D. CREATE VIEW

    正解: **A** ／ 難易度: 中級

    **解説:** plan や package に紐づく thread 使用量を見るため、A を選びます。B: image copy を取得する保守処理です。C: Db2 の基本 buffer pool 名です。D: view を定義する DDL です。CPU と待ち時間を同じ単位で読む点が要点です；背景にはトレース種別では、accounting trace を thread 単位の利用量確認に使います、CPU、class 3 wait、lock/latch wait を plan や package に結び付けて読みます、application 別の消費量を確認し、利用者や処理単位ごとの影響を切り分けますという関係があり、この区別で確認する名称は「accounting」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **accounting trace**

    - 検証目的: 変更確認のトレース種別について、accounting traceは、Db2 for z/OS のトレース種別で用いる Db2の性能診断やモニタリングで使う情報または収集単位です。SQL の実行計画、待ち時間、トに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、変更確認のトレース種別の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にaccounting traceを指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND accounting trace
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM accounting trace
    CASE OSKB020020
    SOURCE Db2 for z/OS
    ```

    accounting traceとOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020020を同じ出力で読み、変更確認のトレース種別の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020020
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020020
    ```

    DSNV401IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の accounting trace と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### monitor trace {#c07-i0404}
*分類: 性能・モニタリング・トレース > トレース種別*  ・  難易度: 中級

monitor traceは、Db2 for z/OSのトレース種別で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。トレース種別では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** オンライン monitor で thread や subsystem 状態を見ます。表示 tool にデータを渡す trace 系統はどれですか。

    - A. QUIESCE
    - B. WLM ENV
    - C. audit role
    - D. 監視tool連携 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 表示 tool のデータ連携に関係するため、D が合います。A: recovery point を作る保守処理です。B: routine 実行環境の指定です。C: 権限監査寄りの観点です。集計間隔と保存有無も確認します；背景には表示系トレース種別では、monitor trace が表示 tool へ渡す情報の流れを担います、online monitor は subsystem 状態や thread 状態を表示するため、この基礎データを使います、利用時は表示 tool の集計間隔、対象 IFCID、保存有無を確認しますという関係があり、この区別で確認する名称は「monitor」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **monitor trace**

    - 検証目的: 展開照合のトレース種別について、monitor traceは、Db2 for z/OS のトレース種別で用いる Db2の性能診断やモニタリングで使う情報または収集単位です。SQL の実行計画、待ち時間、トレースに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、展開照合のトレース種別の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にmonitor traceを指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND monitor trace
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM monitor trace
    CASE OSKB020022
    SOURCE Db2 for z/OS
    ```

    monitor traceとOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020022を同じ出力で読み、展開照合のトレース種別の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020022
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020022
    ```

    DSNV401IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の monitor trace と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### performance trace {#c07-i0405}
*分類: 性能・モニタリング・トレース > トレース種別*  ・  難易度: 中級

performance traceは、Db2 for z/OSのトレース種別で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。トレース種別では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** WAIT 問題を深掘りするため、class と IFCID を指定して詳細イベントを短時間のみ集めます。使う trace はどれですか。

    - A. PLAN_TABLE
    - B. IRLMRWT
    - C. 詳細event収集 ✅
    - D. RUNSTATS

    正解: **C** ／ 難易度: 中級

    **解説:** 詳細な性能イベントを集めるため、C と判断します。A: EXPLAIN 結果の表です。B: lock wait の timeout parameter です。D: 統計収集処理です。採取範囲を絞り、overhead を抑える運用が必要です；背景には詳細な性能診断イベントを Db2 for z/OS から短時間のみ採る場合は、START TRACE(PERFM) を使います、class や IFCID により取得対象を絞ります、待ち問題や contention を深掘りする場合は、取得量と overhead を意識して採取時間を限定しますという関係があり、この区別で確認する名称は「performance」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172



### statistics trace {#c07-i0406}
*分類: 性能・モニタリング・トレース > トレース種別*  ・  難易度: 中級

statistics traceは、Db2 for z/OSのトレース種別で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。トレース種別では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** 時間帯ごとの buffer pool 活動や lock 活動を見て、subsystem 全体の傾向を把握します。使う trace はどれですか。

    - A. UDF path
    - B. DSN1COPY
    - C. DROP VIEW
    - D. 全体傾向記録 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** subsystem 全体の活動量を時間帯ごとに見るため、D が適切です。A: function の名前解決順序です。B: data set レベルの copy tool です。C: 不要になった view を消す定義操作です。日次傾向や容量計画の確認に使います；背景にはstatistics trace は、Db2 subsystem 全体の活動量を時間帯ごとの傾向として採取する記録です、対象には buffer pool、lock、log、DDF、SQL 活動が含まれます、短い SQL 1 本の詳細を追う用途ではなく、日次の傾向確認や容量計画に向きますという関係があり、この区別で確認する名称は「statistics」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **statistics trace**

    - 検証目的: 構文照合のトレース種別について、statistics traceは、Db2 for z/OS のトレース種別で用いる Db2の性能診断やモニタリングで使う情報または収集単位です。SQL の実行計画、待ち時間、トに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、構文照合のトレース種別の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にstatistics traceを指定し、OSKB020021の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND statistics trace
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM statistics trace
    CASE OSKB020021
    SOURCE Db2 for z/OS
    ```

    statistics traceとOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020021を同じ出力で読み、構文照合のトレース種別の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020021
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020021
    ```

    DSNV401IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の statistics trace と OSKB020021 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference




## Db2 for z/OS > 性能・モニタリング・トレース > レポート・待ち分析

### DBAT monitoring {#c07-i0407}
*分類: 性能・モニタリング・トレース > レポート・待ち分析*  ・  難易度: 中級

DBAT monitoringは、Db2 for z/OSのレポート・待ち分析で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。レポート・待ち分析では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** DDF 経由の remote application が増え、active DBAT と待ち行列を確認します。監視対象はどれですか。

    - A. PGFIX
    - B. SQL PL
    - C. DBAT監視 ✅
    - D. DSNU256I

    正解: **C** ／ 難易度: 中級

    **解説:** DDF 経由 thread の状態を見るため、C が妥当です。A: buffer pool の固定指定です。B: SQL procedure の言語です。D: utility message の一つです。DBAT monitoring は MAXDBAT と connection pool を並べて見ます；背景にはDBAT monitoring は、Db2 for z/OS の DDF 経由 workload を監視する作業です、稼働中 DBAT、待ち接続、MAXDBAT、remote application の待ちを見ます、急増時は接続 pool、application server、DDF thread 上限、timeout も併せて見ますという関係があり、この区別で確認する名称は「monitoring」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172



### I/O wait analysis {#c07-i0408}
*分類: 性能・モニタリング・トレース > レポート・待ち分析*  ・  難易度: 中級

I/O wait analysisは、Db2 for z/OSのレポート・待ち分析で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。レポート・待ち分析では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** SQL の遅さが storage 側の read 待ちなのか、access path の問題なのかを切り分けます。見る分析はどれですか。

    - A. 入出力待ち分析 ✅
    - B. WLM ENVIRONMENT
    - C. DROP VIEW
    - D. reason code

    正解: **A** ／ 難易度: 中級

    **解説:** 入出力待ちを分けて見る分析なので、A を選びます。B: routine 実行環境の指定です。C: DROP VIEW で行う schema object の整理です。D: 障害時の理由番号です。I/O wait analysis は buffer pool と log の待ちを分けます；背景にはI/O wait analysis は、Db2 for z/OS の応答時間のうち入出力待ちを切り分ける分析です、確認対象は synchronous read、prefetch、log write、work file I/O に分けます、SQL の access path 問題か、storage 側の遅延かを分けるために、trace と report を突き合わせますという関係があり、この区別で確認する名称は「I/O」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **I ・ O wait analysis**

    - 検証目的: 終端照合の・について、I/O wait analysisは、Db2 for z/OS のレポート・待ち分析で用いる Db2の性能診断やモニタリングで使う情報または収集単位です。SQL の実行計画、待ちに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、終端照合の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にI ・ O wait analysiを指定し、OSKB020025の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND I ・ O wait analysi
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM I ・ O wait analysi
    CASE OSKB020025
    SOURCE Db2 for z/OS
    ```

    I ・ O wait analysiとOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020025を同じ出力で読み、終端照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020025
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020025
    ```

    DSNV401IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の I ・ O wait analysi と OSKB020025 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### buffer pool report {#c07-i0409}
*分類: 性能・モニタリング・トレース > レポート・待ち分析*  ・  難易度: 中級

buffer pool reportは、Db2 for z/OSのレポート・待ち分析で用いるDb2内部のメモリ、ロック、待ち、バッファー、ページ管理に関わる資源項目です。性能問題や可用性低下を調べるときに、どの資源が詰まっているかを切り分ける入口になります。レポート・待ち分析では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** BP8K0 の同期 read が増えているか、page steal が多いかをレポートで確認します。見る資料はどれですか。

    - A. DROP VIEW
    - B. pool活動表 ✅
    - C. SECURITY USER
    - D. CALL

    正解: **B** ／ 難易度: 中級

    **解説:** pool の read や page steal をまとめる資料なので、B が適切です。A: 既存 view を取り除くための DDL です。C: routine 実行権限の属性です。D: procedure を呼び出す SQL 文です。workload の時間帯差も合わせて見ます；背景にはbuffer pool report は、Db2 for z/OS の buffer pool 活動をまとめて見る性能レポートです、hit ratio、synchronous read、write、page steal、prefetch の値を読み、どの pool が詰まっているかを切り分けます、単発値を主な根拠にしてなく、時間帯と workload の変化を比較しますという関係があり、この区別で確認する名称は「buffer」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172



### lock contention analysis {#c07-i0410}
*分類: 性能・モニタリング・トレース > レポート・待ち分析*  ・  難易度: 中級

lock contention analysisは、性能・モニタリング・トレースの中でレポート・待ち分析に関わるDb2技術項目です。Db2共有資源としての役割、メンバー間影響、CF構造との関係。一方で、XCF/GRS/CF一般論、Sysplex全体設計の詳細。 性能観測・分析の観点として扱い、資源そのものの定義とは分けるとは分けて扱います

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** 複数 member で同じ object への待ちが増え、どの plan が競合しているかを調べます。分析はどれですか。

    - A. RUNSTATS PROFILE
    - B. lock競合分析 ✅
    - C. DCLGEN
    - D. COPYTOCOPY

    正解: **B** ／ 難易度: 中級

    **解説:** lock 競合の相手と影響を調べるため、B が該当します。A: 統計収集条件の再利用です。C: host variable 宣言の生成です。D: copy を別 copy へ複製する保守処理です。data sharing では CF 側の情報も見ます；背景には性能・モニタリング領域で扱う lock contention analysis は、ロック待ちや全体競合を分析する作業です、会計系トレースや性能系トレースから、どのプラン、利用者、対象オブジェクトが競合しているかを読みます、データ共用では CF 側のロック構造の活動も併読しますという関係があり、この区別で確認する名称は「contention」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172


??? note "検証手順（1件）"
    **lock contention analysis**

    - 検証目的: 探索照合のレポート・待ち分析について、lock contention analysisは、性能・モニタリング・トレースの中でレポート・待ち分析に関わる Db2技術項目です。Db2共有資源としての役割、メンバー間影に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、探索照合のレポート・待ち分析の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にlock contention anを指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND lock contention an
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM lock contention an
    CASE OSKB020026
    SOURCE Db2 for z/OS
    ```

    lock contention anとOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020026を同じ出力で読み、探索照合のレポート・待ち分析の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020026
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020026
    ```

    DSNV401IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の lock contention an と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference



### thread wait analysis {#c07-i0411}
*分類: 性能・モニタリング・トレース > レポート・待ち分析*  ・  難易度: 中級

thread wait analysisは、Db2 for z/OSのレポート・待ち分析で用いるDb2の性能診断やモニタリングで使う情報または収集単位です。SQLの実行計画、待ち時間、トレース情報を読み、原因候補を絞る場面で使います。レポート・待ち分析では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Performance / Db2_zOS_Data_Sharing / Db2_zOS_Command_Reference

??? question "確認問題（1問）"
    **問題.** ある application の応答遅延について、Db2 内部のどの待ち時間が大きいかを thread 単位で見ます。分析はどれですか。

    - A. DSNU message
    - B. archive lag
    - C. thread待ち内訳 ✅
    - D. index DDL

    正解: **C** ／ 難易度: 中級

    **解説:** thread ごとの待ち内訳を見るため、C と判断します。A: utility message の分類です。B: archive log 退避遅れです。D: index 定義の変更です。待ち分析では class 3 suspension の内訳が要点です；背景にはthread wait analysis は、Db2 for z/OS の thread がどこで待っているかを分解する分析です、class 3 suspension time には buffer pool I/O、log I/O、lock/latch などの待ちが含まれます、application 側の遅延と Db2 内部待ちを分けて説明するために使いますという関係があり、この区別で確認する名称は「thread」です。

    **出典:** Db2_zOS_Performance.pdf p.412 / Db2_zOS_Performance.pdf p.624 / Db2_zOS_Performance.pdf p.653 / Db2_zOS_Performance.pdf p.661 / Db2_zOS_Performance.pdf p.707 / Db2_zOS_Performance.pdf p.723 / Db2_zOS_Performance.pdf p.822 / Db2_zOS_Performance.pdf p.872 / Db2_zOS_Command_Reference.pdf p.656 / Db2_zOS_Data_Sharing.pdf p.172




## Db2 for z/OS > 権限・監査・RACF ACM > RACF ACM

### RACF ACM administrative authority profile {#c07-i0412}
*分類: 権限・監査・RACF ACM > RACF ACM*  ・  難易度: 上級

RACF ACM administrative authority profileは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** Db2のSYSADMやSYSCTRLをRACFプロファイルとして管理します。管理権限を表す項目は何ですか。

    - A. 表の行アクセス制御。
    - B. アーカイブログ一覧。
    - C. 管理権限プロファイル。 ✅
    - D. 実行時再最適化。

    正解: **C** ／ 難易度: 上級

    **解説:** Cが該当します。このプロファイルはDb2管理権限をRACF側の資源名として扱います。Aはrow permission、BはDISPLAY ARCHIVE、DはREOPTであり、SYSADMなどを外部セキュリティで表す項目ではありません；背景には管理権限をRACF側で表す administrative authority profile は、Db2のRACF ACMでSYSADMやSYSCTRLなどをプロファイルとして扱う項目です、例としてDb2サブシステム名と権限名を組み合わせ、DSNADMなどのクラスで判定しますという関係があり、この区別で確認する名称は「administrative」です。

    **出典:** Db2_zOS_RACF_ACM / Db2_zOS_Security



### RACF ACM classification model {#c07-i0413}
*分類: 権限・監査・RACF ACM > RACF ACM*  ・  難易度: 上級

RACF ACM classification modelは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** Db2資源の種類ごとに、どのRACFプロファイルで権限判定するかを整理します。該当する考え方は何ですか。

    - A. ログ二重化。
    - B. RACF ACMの分類モデル。 ✅
    - C. 列マスクの表示値。
    - D. パッケージの解放。

    正解: **B** ／ 難易度: 上級

    **解説:** Bが正しいです。この分類モデルはDb2資源種別とRACF側のチェックを対応付けます。Aは回復設計、Cは列アクセス制御、DはFREE PACKAGEであり、RACF ACMの資源分類ではありません。資源名の作り方を誤ると判定先がずれます；背景には判定資源を分類する RACF ACM classification model は、Db2のRACF ACMで資源種別と権限チェックを対応付ける考え方です、表、ストレージグループ、trusted contextなど、Db2資源ごとにRACFプロファイルの形が変わりますという関係があり、この区別で確認する名称は「classification」です。

    **出典:** Db2_zOS_RACF_ACM / Db2_zOS_Security


??? note "検証手順（1件）"
    **RACF ACM classification model**

    - 検証目的: 監査検査のDb2について、RACF ACM classification modelは、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、監査検査のDb2の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にRACF ACM classificを指定し、OSKB010079の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND RACF ACM classific
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM RACF ACM classific
    CASE OSKB010079
    SOURCE Db2 for z/OS
    ```

    RACF ACM classificとOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010079を同じ出力で読み、監査検査のDb2の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010079
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010079
    ```

    DSNV401IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の RACF ACM classific と OSKB010079 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### RACF DSNR class {#c07-i0414}
*分類: 権限・監査・RACF ACM > RACF ACM*  ・  難易度: 上級

RACF DSNR classは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** Db2資源のアクセス判定をRACF側のクラス定義で管理します。確認するDb2向けRACFクラスは何ですか。

    - A. DSNR系クラス。 ✅
    - B. 表スペース名。
    - C. SQLCA領域。
    - D. グループバッファプール。

    正解: **A** ／ 難易度: 上級

    **解説:** Aを選びます。このクラスはRACF ACMでDb2資源のアクセス判定に使われます。Bは記憶構造、CはSQL診断領域、DはData Sharingの資源であり、RACF側のDb2権限判定クラスではありません；背景には外部セキュリティで使う RACF DSNR class は、Db2のRACF ACMでDb2資源へのアクセス判定に関わるクラスです、Db2サブシステム名や管理権限のプロファイルと結び付き、Db2内部権限を主な根拠にしてなくRACF側の定義も確認しますという関係があり、この区別で確認する名称は「class」です。

    **出典:** Db2_zOS_RACF_ACM / Db2_zOS_Security


??? note "検証手順（1件）"
    **RACF DSNR class**

    - 検証目的: 復旧検査のDb2について、RACF DSNR classは、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、復旧検査のDb2の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にRACF DSNR classを指定し、OSKB010078の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND RACF DSNR class
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM RACF DSNR class
    CASE OSKB010078
    SOURCE Db2 for z/OS
    ```

    RACF DSNR classとOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010078を同じ出力で読み、復旧検査のDb2の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010078
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010078
    ```

    DSNV401IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の RACF DSNR class と OSKB010078 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference




## Db2 for z/OS > 権限・監査・RACF ACM > SQL権限付与

### GRANT {#c07-i0415}
*分類: 権限・監査・RACF ACM > SQL権限付与*  ・  難易度: 中級

GRANTは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 新しいアプリケーションIDへ、必要な表アクセス権限を明示的に与えます。使うSQL文は何ですか。

    - A. REBIND PLAN。
    - B. GRANT。 ✅
    - C. DISPLAY LOG。
    - D. CREATE SEQUENCE。

    正解: **B** ／ 難易度: 初級

    **解説:** Bが正しいです。この文は利用者やロールに権限を付与します。Aはプラン再バインド、Cはログ表示、Dは順序定義であり、表アクセス権限を与えるSQLではありません。付与対象と範囲を監査できる形で残します。実行IDの確認にもつながります；背景にはSQL権限付与で使う GRANT は、Db2オブジェクトや権限を利用者、ロール、PUBLICなどへ与えるSQL文です、パッケージ実行や表アクセスで権限不足が出る場合、どの権限を誰に与えるかを明確にします、監査のため、付与理由と対象範囲を残しますという関係があり、この区別で確認する名称は「GRANT」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **GRANT**

    - 検証目的: 比較検査の権限付与について、GRANT は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010074の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、比較検査の権限付与の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にGRANTを指定し、OSKB010074の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND GRANT
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM GRANT
    CASE OSKB010074
    SOURCE Db2 for z/OS
    ```

    GRANTとOSKB010074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010074を同じ出力で読み、比較検査の権限付与の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010074
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010074
    ```

    DSNV401IとOSKB010074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の GRANT と OSKB010074 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### REVOKE {#c07-i0416}
*分類: 権限・監査・RACF ACM > SQL権限付与*  ・  難易度: 中級

REVOKEは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 退職者IDや役割変更後のIDから、不要になった表アクセス権限を取り消します。使うSQL文は何ですか。

    - A. REVOKE。 ✅
    - B. BIND PACKAGE。
    - C. RUNSTATS。
    - D. CREATE DATABASE。

    正解: **A** ／ 難易度: 初級

    **解説:** Aを選びます。この文は付与済み権限を取り消します。Bはパッケージ作成、Cは統計収集、Dはデータベース定義であり、利用者から権限を含めない文ではありません。取り消し後の実行確認も必要です。依存権限の有無も確認します；背景には不要権限を含めない REVOKE は、Db2のSQL権限付与カテゴリで権限を取り消すSQL文です、職務分離や利用者変更を見直すときは、依存する権限や後続影響も確認します、誤って必要権限を含めないと、パッケージ実行や業務SQLが失敗します、取り消し理由も記録しますという関係があり、この区別で確認する名称は「REVOKE」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **REVOKE**

    - 検証目的: 順序検査の権限付与について、REVOKE は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010075の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、順序検査の権限付与の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にREVOKEを指定し、OSKB010075の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND REVOKE
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM REVOKE
    CASE OSKB010075
    SOURCE Db2 for z/OS
    ```

    REVOKEとOSKB010075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010075を同じ出力で読み、順序検査の権限付与の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010075
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010075
    ```

    DSNV401IとOSKB010075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の REVOKE と OSKB010075 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### role {#c07-i0417}
*分類: 権限・監査・RACF ACM > SQL権限付与*  ・  難易度: 中級

roleは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 複数の利用者へ同じ権限セットを割り当て、職務単位で管理したい状況です。Db2で使う管理単位は何ですか。

    - A. 表スペース。
    - B. ログコピー。
    - C. ロール。 ✅
    - D. カーソル。

    正解: **C** ／ 難易度: 中級

    **解説:** Cが適切です。この管理単位は権限セットをまとめ、利用者や条件に割り当てるための単位です。Aは記憶構造、Bは回復資材、Dは照会結果の取り出し制御であり、権限セットの管理単位ではありません。直接付与を減らす設計で役立ちます；背景には権限をまとめる role は、Db2のSQL権限付与で複数権限を利用者や接続条件へ割り当てやすくする管理単位です、個別IDへ直接権限をばらまくより、職務単位で付与と取り消しを整理できます、trusted context と組み合わせる設計もありますという関係があり、この区別で確認する名称は「role」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **role**

    - 検証目的: 値域検査の権限付与について、roleは、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010076の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、値域検査の権限付与の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にroleを指定し、OSKB010076の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND role
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM role
    CASE OSKB010076
    SOURCE Db2 for z/OS
    ```

    roleとOSKB010076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010076を同じ出力で読み、値域検査の権限付与の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010076
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010076
    ```

    DSNV401IとOSKB010076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の role と OSKB010076 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference




## Db2 for z/OS > 権限・監査・RACF ACM > コンテキスト・行列アクセス制御

### column mask {#c07-i0418}
*分類: 権限・監査・RACF ACM > コンテキスト・行列アクセス制御*  ・  難易度: 中級

column maskは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 給与列を参照できる画面でも、権限のない利用者には値を隠して表示したい状況です。使う制御は何ですか。

    - A. 表スペース回復。
    - B. 列値のマスク。 ✅
    - C. ログの切替。
    - D. SQLパッケージ作成。

    正解: **B** ／ 難易度: 中級

    **解説:** Bを選びます。この制御は列の表示値を利用者条件に応じて変えます。AはRECOVER系の処理、Cはログ運用、DはBIND PACKAGEであり、機密列を伏せる仕組みではありません。元データを削除せず、見せ方を制御する点が要点です；背景には列値を隠す column mask は、Db2のコンテキスト・行列アクセス制御で、利用者や条件に応じて列の表示値を変える仕組みです、給与や個人情報の列を、権限のない利用者には伏せ字や代替値で見せる設計に使います、監査や照会画面では、元値を保持したまま表示値のみを制御しますという関係があり、この区別で確認する名称は「column」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference



### row permission {#c07-i0419}
*分類: 権限・監査・RACF ACM > コンテキスト・行列アクセス制御*  ・  難易度: 中級

row permissionは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 部門コードに応じて、同じ表でも利用者ごとに見える行を変えたい状況です。使う制御は何ですか。

    - A. 行アクセス制御。 ✅
    - B. アーカイブログ表示。
    - C. プラン解放。
    - D. ストレージグループ定義。

    正解: **A** ／ 難易度: 中級

    **解説:** Aが正しいです。この制御は表の行を条件で絞り、利用者ごとの可視範囲を制限します。Bはログ運用、CはFREE PLAN、DはCREATE STOGROUPであり、行単位のアクセス制御ではありません。実装改修漏れへの補強にもなります；背景には行単位の絞り込みを行う row permission は、Db2のコンテキスト・行列アクセス制御で、利用者に見せる行を条件で制限します、実装側でWHERE句を忘れても、データベース側のポリシーとして行アクセスを制御できます、部門別の参照範囲を表側で守りたい場合に検討しますという関係があり、この区別で確認する名称は「permission」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference



### trusted context {#c07-i0420}
*分類: 権限・監査・RACF ACM > コンテキスト・行列アクセス制御*  ・  難易度: 上級

trusted contextは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** アプリケーションサーバーからの接続のみ、特定ロールを使えるように制御します。接続条件を基準にする機能は何ですか。

    - A. 表を削除する文。
    - B. パッケージの再バインド。
    - C. ログ表示のコマンド。
    - D. 信頼接続条件の定義。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dを選びます。この機能は接続元やユーザー条件を使って権限の扱いを制御します。AはDROP TABLE、BはREBIND PACKAGE、CはDISPLAY LOGであり、接続条件に基づくセキュリティ制御ではありません；背景には接続条件を信頼単位にする trusted context は、Db2のコンテキスト・行列アクセス制御に関わるセキュリティ機能です、接続元、ユーザー、ロールの条件を組み合わせ、特定の接続条件でのみ追加の扱いを許す設計に使います、特定サーバー経由の接続のみを特別扱いする設計で使いますという関係があり、この区別で確認する名称は「trusted」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference




## Db2 for z/OS > 権限・監査・RACF ACM > 監査

### audit policy {#c07-i0421}
*分類: 権限・監査・RACF ACM > 監査*  ・  難易度: 中級

audit policyは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 管理権限の使用を監査証跡として残すため、監査対象の活動をポリシー化します。使う項目は何ですか。

    - A. カーソル宣言。
    - B. アクセスパス再利用。
    - C. 監査ポリシー。 ✅
    - D. 表の別名。

    正解: **C** ／ 難易度: 中級

    **解説:** Cが答えです。このポリシーは監査対象の活動を定義し、証跡取得に使います。Aは照会制御、Bは性能管理、DはCREATE ALIASであり、管理権限の使用を監査する設定ではありません。記録対象を事前に決めることが重要です；背景には監査カテゴリの audit policy は、Db2で監査対象の活動を定義し、必要な証跡を取得するためのポリシーです、SECADM権限で作成、表示、有効化、無効化を管理し、管理権限の使用や表アクセスを記録する設計に使います、取得した証跡は、後日の説明責任や不正調査で使いますという関係があり、この区別で確認する名称は「policy」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **audit policy**

    - 検証目的: 警告検査の監査について、audit policyは、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010077の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、警告検査の監査の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にaudit policyを指定し、OSKB010077の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND audit policy
    CASE OSKB010077
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM audit policy
    CASE OSKB010077
    SOURCE Db2 for z/OS
    ```

    audit policyとOSKB010077が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010077を同じ出力で読み、警告検査の監査の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010077
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010077
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010077
    ```

    DSNV401IとOSKB010077が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の audit policy と OSKB010077 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### tamper-proof audit policy {#c07-i0422}
*分類: 権限・監査・RACF ACM > 監査*  ・  難易度: 中級

tamper-proof audit policyは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 重要監査を勝手に止められないよう、外部セキュリティ製品の許可を必要にします。該当する監査機能は何ですか。

    - A. 通常の表別名。
    - B. 標準カーソル。
    - C. 動的SQL準備。
    - D. 改ざん耐性監査ポリシー。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dが適切です。この監査ポリシーは変更や停止に外部セキュリティ製品の許可を要求します。AはALIAS、Bはcursor、CはPREPAREであり、監査停止を保護する仕組みではありません。監査の停止権限も外部側で確認します；背景には改ざん耐性を高める tamper-proof audit policy は、Db2の監査ポリシーを外部セキュリティ製品の許可なしに変更や停止できないようにします、SYSIBM.SYSAUDITPOLICIESでDB2STARTをTにする設計が示され、RACFなどの外部権限と連動しますという関係があり、この区別で確認する名称は「tamper-proof」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference




## Db2 for z/OS > 権限・監査・RACF ACM > 管理権限

### ACCESSCTRL {#c07-i0423}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 中級

ACCESSCTRLは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 利用者への権限付与や取り消しを管理する担当を、データ閲覧担当とは別にします。該当する管理権限は何ですか。

    - A. 順序番号を発行する定義。
    - B. 権限管理向けの権限。 ✅
    - C. 表データの物理領域。
    - D. カーソルの保持指定。

    正解: **B** ／ 難易度: 中級

    **解説:** Bが正しいです。この管理権限はアクセス制御を管理する役割に対応します。AはCREATE SEQUENCE、Cは表スペース、Dはカーソル属性であり、権限付与や取り消しの管理権限ではありません。権限変更の実施者を限定するために使います；背景には権限付与を管理する ACCESSCTRL は、Db2の管理権限の中でアクセス制御の管理に関わります、データ内容を読む役割とは分け、誰にどの権限を付与または取り消すかを扱う担当者へ限定して付与します、付与操作そのものを監査できるよう、申請経路と実施者を分けますという関係があり、この区別で確認する名称は「ACCESSCTRL」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **ACCESSCTRL**

    - 検証目的: 優先検査の管理権限について、ACCESSCTRL は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、優先検査の管理権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にACCESSCTRLを指定し、OSKB010072の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND ACCESSCTRL
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM ACCESSCTRL
    CASE OSKB010072
    SOURCE Db2 for z/OS
    ```

    ACCESSCTRLとOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010072を同じ出力で読み、優先検査の管理権限の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010072
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010072
    ```

    DSNV401IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の ACCESSCTRL と OSKB010072 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### DATAACCESS {#c07-i0424}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 中級

DATAACCESSは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 調査担当者に広範なデータ参照と更新を許す依頼があります。データそのものへの影響が最も大きい管理権限は何ですか。

    - A. データアクセス権限。 ✅
    - B. システム制御権限。
    - C. 監査ポリシー名。
    - D. パッケージ集合名。

    正解: **A** ／ 難易度: 上級

    **解説:** Aを選びます。この管理権限は利用者表やビューへの広いアクセスに関わります。BはSYSCTRL、Cはaudit policy、Dはcollectionであり、データそのものへの広範なアクセスを示す権限ではありません；背景には業務データへアクセスする DATAACCESS は、Db2の管理権限として利用者表、ビュー、マテリアライズ照会表へのアクセスや更新を広く許します、プラン、パッケージ、関数、プロシージャの実行にも関係するため、監査対象として扱います、付与すると影響範囲が広いため、通常の個別権限とは別に審査しますという関係があり、この区別で確認する名称は「DATAACCESS」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **DATAACCESS**

    - 検証目的: 範囲検査の管理権限について、DATAACCESS は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、範囲検査の管理権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDATAACCESSを指定し、OSKB010071の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DATAACCESS
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DATAACCESS
    CASE OSKB010071
    SOURCE Db2 for z/OS
    ```

    DATAACCESSとOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010071を同じ出力で読み、範囲検査の管理権限の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010071
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010071
    ```

    DSNV401IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DATAACCESS と OSKB010071 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### SECADM {#c07-i0425}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 上級

SECADMは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 表データの参照担当ではなく、権限・ロール・監査設定の管理担当を分けたい状況です。該当する管理権限は何ですか。

    - A. パッケージを再作成する操作。
    - B. 表データを格納する単位。
    - C. ログ状態を表示するコマンド。
    - D. セキュリティ管理向けの権限。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dが答えです。この管理権限はセキュリティ関連の管理を担い、データ参照権限そのものとは分けて考えます。AはREBIND、Bは表スペース、CはDISPLAY LOGであり、権限や監査の管理者を示しません；背景にはセキュリティ管理を担う SECADM は、Db2の管理権限としてセキュリティ関連オブジェクトとアクセス制御を扱います、表データを読むための権限ではなく、権限、ロール、監査、行列アクセス制御などの管理責任を分離するために使います、権限設計を変更する際は、データ参照権限と混同しないことが重要ですという関係があり、この区別で確認する名称は「SECADM」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **SECADM**

    - 検証目的: 区切検査の管理権限について、SECADM は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、区切検査の管理権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSECADMを指定し、OSKB010070の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SECADM
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SECADM
    CASE OSKB010070
    SOURCE Db2 for z/OS
    ```

    SECADMとOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010070を同じ出力で読み、区切検査の管理権限の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010070
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010070
    ```

    DSNV401IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SECADM と OSKB010070 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### SEPARATE_SECURITY {#c07-i0426}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 中級

SEPARATE_SECURITYは、権限・監査・RACF ACMの中で管理権限に関わるDb2技術項目です。権限の意味、付与/取消、監査対象、RACF ACM連携時の判定点。一方で、RACFユーザー/グループ管理そのもの、Db2外の汎用監査設計。 Db2側の権限・監査・RACF ACMとして扱い、RACF USER/GROUP/DATASET本体とは分けるとは分けて扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** SYSADMにセキュリティ管理まで集中しないよう、管理責任を分けたい状況です。関係する考え方は何ですか。

    - A. 表スペースのページサイズ。
    - B. SQL文の分離レベル。
    - C. セキュリティ職務分離。 ✅
    - D. ログのオフロード。

    正解: **C** ／ 難易度: 上級

    **解説:** Cが該当します。この考え方はセキュリティ管理とシステム管理の責任を分けるために使います。Aは記憶設計、BはISOLATION、Dはログ運用であり、SYSADMからセキュリティ責任を分ける話ではありません；背景には職務分離を強める SEPARATE_SECURITY は、Db2の管理権限設計でSYSADMからセキュリティ管理を分ける考え方に関わります、SECADMなどへ責任を分けることで、システム管理者が無条件にセキュリティ管理まで持つ状態を避けますという関係があり、この区別で確認する名称は「SEPARATE_SECURITY」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **SEPARATE_SECURITY**

    - 検証目的: 記録検査の管理権限について、SEPARATE_SECURITY は、権限・監査・ RACF ACM の中で管理権限に関わる Db2技術項目です。権限の意味、付与/取消、監査対象、RACF ACM 連携時の判定点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010073の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、記録検査の管理権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSEPARATE_SECURITYを指定し、OSKB010073の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SEPARATE_SECURITY
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SEPARATE_SECURITY
    CASE OSKB010073
    SOURCE Db2 for z/OS
    ```

    SEPARATE_SECURITYとOSKB010073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010073を同じ出力で読み、記録検査の管理権限の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010073
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010073
    ```

    DSNV401IとOSKB010073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SEPARATE_SECURITY と OSKB010073 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### SYSADM {#c07-i0427}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 上級

SYSADMは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 新任DBAへDb2全体の強力な管理権限を与える依頼が来ました。職務分離への影響を最も大きく見るべき権限は何ですか。

    - A. 最高位の管理権限。 ✅
    - B. ログ表示のみを行う権限。
    - C. 表の行を追加するSQL文。
    - D. 分散接続の表示結果。

    正解: **A** ／ 難易度: 上級

    **解説:** Aが正しいです。この管理権限はDb2全体へ強い操作能力を持つため、付与対象を最小限にします。Bは運用表示、CはINSERT、DはDDF関連の確認であり、強力な管理権限の説明ではありません。棚卸し対象としても最優先で確認します；背景にはサブシステム全体を管理する SYSADM は、Db2の管理権限の中でも広い権限を持つ上位権限です、セキュリティ管理、システム管理、データベース管理を一人に集中させると職務分離が弱くなるため、付与対象を厳しく限定します、監査では、付与理由と承認者を証跡として残しますという関係があり、この区別で確認する名称は「SYSADM」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference



### SYSCTRL {#c07-i0428}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 中級

SYSCTRLは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 機密表の内容を読ませずに、Db2サブシステムの運用制御を担当させたい状況です。検討する管理権限は何ですか。

    - A. 表データを直接読むための権限。
    - B. システム制御向けの管理権限。 ✅
    - C. 監査ポリシーを保護する設定。
    - D. 列値をマスクする定義。

    正解: **B** ／ 難易度: 中級

    **解説:** Bを選びます。この権限はシステム制御に寄った管理操作を担います。AはDATAACCESSの方向、Cは監査ポリシー、Dはcolumn maskであり、サブシステム制御を任せる管理権限とは異なります。機密データを扱う環境では分離が重要です；背景にはシステム運用を担う SYSCTRL は、Db2の管理権限のうちサブシステム制御に近い操作を行うための権限です、機密データを直接読む役割とは切り分け、起動停止、資源管理、保守操作の責任範囲として設計します、データ閲覧を避けたい環境で、運用責任のみを切り出す場面に向きますという関係があり、この区別で確認する名称は「SYSCTRL」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **SYSCTRL**

    - 検証目的: 出力検査の管理権限について、SYSCTRL は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、出力検査の管理権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSYSCTRLを指定し、OSKB010068の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SYSCTRL
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SYSCTRL
    CASE OSKB010068
    SOURCE Db2 for z/OS
    ```

    SYSCTRLとOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010068を同じ出力で読み、出力検査の管理権限の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010068
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010068
    ```

    DSNV401IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SYSCTRL と OSKB010068 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference



### SYSOPR {#c07-i0429}
*分類: 権限・監査・RACF ACM > 管理権限*  ・  難易度: 中級

SYSOPRは、Db2の権限判定、監査、またはRACF連携に関わるセキュリティ項目です。誰が、どのDb2オブジェクトに、どの操作を許されるかを説明できる粒度で扱います

**出典:** Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference

??? question "確認問題（1問）"
    **問題.** 運用担当者に、日常の表示や起動停止に必要な範囲のみを持たせたい状況です。候補になる管理権限は何ですか。

    - A. すべての表へ更新できる権限。
    - B. SQLの実行計画を保存する表。
    - C. 運用操作向けの管理権限。 ✅
    - D. RACFクラス定義の名前。

    正解: **C** ／ 難易度: 中級

    **解説:** Cが適切です。この権限は運用操作を担う担当者向けに使います。Aはデータ更新権限、BはPLAN_TABLE、DはRACF ACMの管理要素であり、日常運用の権限を示すものではありません。データ管理者ではなく運用担当者向けです；背景には運用操作に絞る SYSOPR は、Db2の管理権限として日常運用の起動、停止、表示、回復支援に関わる操作を担います、開発者や監査担当へ広く与える権限ではなく、オペレーション担当の作業範囲に合わせて管理します、夜間運用や障害対応の担当範囲を定義するときに確認しますという関係があり、この区別で確認する名称は「SYSOPR」です。

    **出典:** Db2_zOS_Security / Db2_zOS_SQL_Reference


??? note "検証手順（1件）"
    **SYSOPR**

    - 検証目的: 条件検査の管理権限について、SYSOPR は、Db2の権限判定、監査、または RACF 連携に関わるセキュリティ項目です。誰が、どの Db2オブジェクトに、どの操作を許されるかを説明できる粒度で扱いますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、条件検査の管理権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSYSOPRを指定し、OSKB010069の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SYSOPR
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SYSOPR
    CASE OSKB010069
    SOURCE Db2 for z/OS
    ```

    SYSOPRとOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010069を同じ出力で読み、条件検査の管理権限の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010069
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010069
    ```

    DSNV401IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SYSOPR と OSKB010069 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Security / Db2_zOS_RACF_ACM / Db2_zOS_SQL_Reference


