---
search:
  exclude: true
---

# z/OS 3.1 Core Operations — 詳細 (4/4)

[← z/OS 3.1 Core Operations の概要へ戻る](index.md)


## z/OS 3.1 Core Operations > シンボル確認

### シンボル確認 動的システムシンボル 通常状態の確認 DSYM01 {#c37-i0269}
*分類: シンボル確認*  ・  難易度: 上級

通常状態の確認では シンボル確認 の 全シンボル を主操作として DSYM01 を判定します。基準値と現在値の差への注意として「シンボル未展開文字列を実データセット名として扱う危険があります」を DSYM01 に残します。通常状態の確認を補助する IPL対応 では IEASYM00 を補助値として DSYM01 へ保存します。主判定の通常状態の確認ではシンボル確認・動的システムシンボルの 全シンボル から &SYSR2. を読み DSYM01 へ残します。証跡照合の通常状態の確認ではシンボル確認・動的システムシンボルの &SYSR2. と IEASYM00 を DSYM01 に保存します。記録対応の通常状態の確認ではシンボル確認・動的システムシンボルの SYMBOLとVALUE の証跡へ DSYM01 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で シンボル確認 の 全シンボル と IPL対応 を用い 通常状態を確定 します。動的システムシンボル はSETLOADやSETSSIなどの運用時に展開されるシステム固有値を表示し、parmlib定義の共通化を支える機能です。シンボル未展開文字列を実データセット名として扱う危険があります。&SYSR2. で対象 DSYM01 の SYMBOLとVALUE を再現できる記録はどれですか。

    - A. D IPLINFOのIEASYM00をSYMBOLとVALUEの主判定に採用する。D SYMBOLSの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. D PARMLIB(IEASYM00)のIEE252Iを&SYSR2.と同義の成功表示として扱う。D SYMBOLSは実行しない。
    - C. D SYMBOLSを先に実行する。対象DSYM01の&SYSR2.をSYMBOLとVALUEとして記録する。続いてD IPLINFOで同一対象を照合する。 ✅
    - D. D SYMBOLSが応答を返した時点で正常とする。応答中の&SYSR2.の値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cは全シンボルで &SYSR2. を読みSYMBOLとVALUEの主値として通常状態を確定しDSYM01に残します。
    背景・仕組み: 通常状態の確認ではIPL対応を補助操作とし動的システムシンボルの基準値と現在値の差をIEASYM00と対象DSYM01で照合します。
    選択肢の理由: 全シンボルとIPL対応の役割を分けるとA: IEASYM00は&SYSR2.を代替しないうえに追加前提も不正な点で動的システムシンボルに使えません、B: IEE252Iと&SYSR2.は確認項目が異なる点でDSYM01を採用できません、C: &SYSR2.を主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではSYMBOLとVALUEを判定できない点で一次資料と一致しません。結論として通常状態の確認のシンボル確認・動的システムシンボルで判定する対象は DSYM01 です。
    用語の初出定義: 通常状態の確認で使う 動的システムシンボル はシンボル確認でSYMBOLとVALUEを扱う機能を表しSYMBOLとVALUEを判定する際にDSYM01へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **シンボル確認 動的システムシンボル 通常状態の確認 DSYM01**

    - 検証目的: シンボル確認の動的システムシンボルについて通常状態を確定し、DSYM01のSYMBOLとVALUEを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象DSYM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsのシンボル確認を確認する入力画面です。COMMAND入力口へD SYMBOLSを指定し、DSYM01の全シンボルを表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D SYMBOLS
    → Enter を押す
    ```

    画面・出力:
    ```text
    &SYSNAME.=SYSA &SYSPLEX.=PLEX1 &SYSR2.=SYS2
    ```

    画面・出力にあるSYSNAME.=SYSAを読み、SYMBOLとVALUEと対象DSYM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsのシンボル確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、DSYM01のIPL対応を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I USED IEASYM00 SYSTEM SYMBOLS FOR SYSA
    ```

    画面・出力にあるIEASYM00を読み、SYMBOLとVALUEと対象DSYM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsのシンボル確認を確認する入力画面です。COMMAND入力口へD PARMLIB(IEASYM00)を指定し、DSYM01のメンバー所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB(IEASYM00)
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER IEASYM00 FOUND IN SYS1.PARMLIB
    ```

    画面・出力にあるIEE252Iを読み、SYMBOLとVALUEと対象DSYM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSNAME.=SYSA が画面・出力に表示されること
    ② ステップ2 の IEASYM00 が画面・出力に表示されること
    ③ ステップ3 の IEE252I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### シンボル確認 動的システムシンボル 障害切り分け DSYM04 {#c37-i0270}
*分類: シンボル確認*  ・  難易度: 上級

障害切り分けでは シンボル確認 の 全シンボル を主操作として DSYM04 を判定します。最初に失敗した処理への注意として「シンボル未展開文字列を実データセット名として扱う危険があります」を DSYM04 に残します。障害切り分けを補助する IPL対応 では IEASYM00 を補助値として DSYM04 へ保存します。主判定の障害切り分けではシンボル確認・動的システムシンボルの 全シンボル から &SYSR2. を読み DSYM04 へ残します。証跡照合の障害切り分けではシンボル確認・動的システムシンボルの &SYSR2. と IEASYM00 を DSYM04 に保存します。記録対応の障害切り分けではシンボル確認・動的システムシンボルの SYMBOLとVALUE の証跡へ DSYM04 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 障害切り分けで シンボル確認 の 全シンボル と IPL対応 の役割を分け 最初に失敗した処理 を調べます。動的システムシンボル はSETLOADやSETSSIなどの運用時に展開されるシステム固有値を表示し、parmlib定義の共通化を支える機能です。シンボル未展開文字列を実データセット名として扱う危険があります。対象 DSYM04 を誤判定しない進め方はどれですか。

    - A. D PARMLIB(IEASYM00)のIEE252Iを&SYSR2.と同義の成功表示として扱う。D SYMBOLSは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D SYMBOLSの出力でDSYM04と&SYSR2.が同じ応答にあることを確認する。SYMBOLとVALUEをその応答から採取する。 ✅
    - C. D SYMBOLSが応答を返した時点で正常とする。応答中の&SYSR2.の値は記録しない。
    - D. D SYMBOLSのコマンド文字列だけを記録する。&SYSR2.を含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bは全シンボルで &SYSR2. を読みSYMBOLとVALUEの主値として障害範囲を限定しDSYM04に残します。
    技術的背景: 障害切り分けではIPL対応を補助操作とし動的システムシンボルの最初に失敗した処理をIEASYM00と対象DSYM04で照合します。
    四択の評価: 全シンボルとIPL対応の役割を分けるとA: IEE252Iと&SYSR2.は確認項目が異なるうえに追加前提も不正な点でDSYM04を採用できません、B: DSYM04と&SYSR2.を同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではSYMBOLとVALUEを判定できない点で一次資料と一致しません、D: 入力記録だけではSYMBOLとVALUEを証明できない点でSYMBOLとVALUEを確認できません。結論として障害切り分けのシンボル確認・動的システムシンボルで判定する対象は DSYM04 です。
    初出語の意味: 障害切り分けで使う 動的システムシンボル はシンボル確認でSYMBOLとVALUEを扱う機能を表しSYMBOLとVALUEを判定する際にDSYM04へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **シンボル確認 動的システムシンボル 障害切り分け DSYM04**

    - 検証目的: シンボル確認の動的システムシンボルについて障害範囲を限定し、DSYM04のSYMBOLとVALUEを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象DSYM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsのシンボル確認を確認する入力画面です。COMMAND入力口へD SYMBOLSを指定し、DSYM04の全シンボルを表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D SYMBOLS
    → Enter を押す
    ```

    画面・出力:
    ```text
    &SYSNAME.=SYSA &SYSPLEX.=PLEX1 &SYSR2.=SYS2
    ```

    画面・出力にあるSYSNAME.=SYSAを読み、SYMBOLとVALUEと対象DSYM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsのシンボル確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、DSYM04のIPL対応を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I USED IEASYM00 SYSTEM SYMBOLS FOR SYSA
    ```

    画面・出力にあるIEASYM00を読み、SYMBOLとVALUEと対象DSYM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsのシンボル確認を確認する入力画面です。COMMAND入力口へD PARMLIB(IEASYM00)を指定し、DSYM04のメンバー所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB(IEASYM00)
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER IEASYM00 FOUND IN SYS1.PARMLIB
    ```

    画面・出力にあるIEE252Iを読み、SYMBOLとVALUEと対象DSYM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSNAME.=SYSA が画面・出力に表示されること
    ② ステップ2 の IEASYM00 が画面・出力に表示されること
    ③ ステップ3 の IEE252I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300




## z/OS 3.1 Core Operations > 移行前確認

### DISPLAY CF 割り込み確認 運用確認017 {#c37-i0271}
*分類: 移行前確認*  ・  難易度: 初級

第十七観点 移行前確認 で DISPLAY CF は 割り込み確認 の対象です（第十七観点）。第十七観点 確認時には 接続されたカップリングファシリティの情報を表示するコマンドという性質を前提にします（第十七観点）。第十七観点 D IOS,ZHPFOPTS のMAXDATA表示 と SMFPRM31 を同じ証跡に置き、オペレーター応答漏れの防止を管理します（第十七観点）。第十七観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOS31記録017から再現します（第十七観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第十七証跡です。移行前確認 の当日作業で SMFPRM31 を追跡します。確認観点は DISPLAY CF、割り込み確認、運用確認 です。D IOS,ZHPFOPTS のMAXDATA表示 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. 作業票017では D IOS,ZHPFOPTS のMAXDATA表示 と SMFPRM31 と時刻を並べる。後続確認で DISPLAY CF の今回値を同じ対象として再確認できる。 ✅
    - B. IEASYSxx管理 の参考情報だけを作業票017へ先に書く。SMFPRM31 とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - C. DISPLAY CF の名称欄だけを作業票017で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - D. 前回の正常出力を作業票017の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の D IOS,ZHPFOPTS のMAXDATA表示 と SMFPRM31 を照合できない形にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 第十七観点 正解確認: Aは DISPLAY CF と SMFPRM31 を同じ証跡で扱うため、後続の照合に使えます（第十七観点）。第十七観点 背景確認: DISPLAY IPLINFOはIPL日時、LOADxx、IEASYSxx、IEASYMxx、IODF、IPL装置をまとめて示します（第十七観点）。第十七観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第十七観点）。第十七観点 用語メモ: GRSは資源直列化です（第十七観点）。第十七観点 RNLは資源名リストです（第十七観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **DISPLAY CF 割り込み確認 運用確認017**

    - 検証目的: DISPLAY CF の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / IPL display

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により DISPLAY CF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I 09.117.00 IPLINFO DISPLAY 716
    RELEASE z/OS 03.01.00
    LOAD PARAMETER 0A82 LOAD31
    IEASYS LIST=(31,OP) IEASYM LIST=(31)
    ```

    画面・出力には IEE254I が含まれる。IEE254I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により DISPLAY CF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SYMBOLS
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEA007I STATIC SYSTEM SYMBOL VALUES
    &SYSNAME. = SY117
    &SYSPLEX. = PLEX31
    &SYSR1. = Z31RES
    ```

    画面・出力には IEA007I が含まれる。IEA007I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により DISPLAY CF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(LOAD31)
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOAD31
    SYSPLEX(PLEX31)
    IEASYM(31)
    IODF(31)
    ARCHLVL=2
    ```

    画面・出力には LOAD31 が含まれる。LOAD31 を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE254I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEA007I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: LOAD31 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### DISPLAY IOS,ZHPF 割り込み確認 運用確認067 {#c37-i0272}
*分類: 移行前確認*  ・  難易度: 中級

第六十七観点 移行前確認 の運用では DISPLAY IOS,ZHPF を表示、定義、証跡で確認します（第六十七観点）。第六十七観点 役割は High Performance FICONの有効または無効状態を表という範囲です（第六十七観点）。第六十七観点 DISPLAY C のCNZ4100I表示 の値を IODF31 と合わせ、オペレーター応答漏れの防止を記録します（第六十七観点）。第六十七観点 確認経路は SDSF、コンソールログ、parmlib、z/OSMF の別を zOS31記録067に残します（第六十七観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第六十七証跡です。移行前確認 の当日作業で IODF31 を追跡します。確認観点は D IOS,ZHPF、割り込み確認、運用確認 です。IODF31 を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. IOS確認 の参考情報だけを作業票067へ先に書く。IODF31 とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. DISPLAY IOS,ZHPF の名称欄だけを作業票067で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - C. 作業票067では DISPLAY C のCNZ4100I表示 と IODF31 と時刻を並べる。後続確認で DISPLAY IOS,ZHPF の今回値を同じ対象として再確認できる。 ✅
    - D. 前回の正常出力を作業票067の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の DISPLAY C のCNZ4100I表示 と IODF31 を照合できない形にする。

    正解: **C** ／ 難易度: 中級

    **解説:** 第六十七観点 採用理由: Cは D IOS,ZHPF の状態を表示値と定義の両方から確認するため、記録として妥当です（第六十七観点）。第六十七観点 記録背景: SMFはSMFPRMxx、SMF=xx、SMFPRM00で記録方針を管理します（第六十七観点）。第六十七観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第六十七観点）。第六十七観点 用語確認: LOADxxはIPL制御メンバーです（第六十七観点）。第六十七観点 IEASYMxxはシステムシンボル定義です（第六十七観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **DISPLAY IOS,ZHPF 割り込み確認 運用確認067**

    - 検証目的: DISPLAY IOS,ZHPF の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により DISPLAY IOS,ZHPF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.19 GRS STATUS 886
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により DISPLAY IOS,ZHPF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.19 GRS STATUS 896
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により DISPLAY IOS,ZHPF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.19 DISPLAY XCF 906
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### DISPLAY TRACE ログ確認 運用確認034 {#c37-i0273}
*分類: 移行前確認*  ・  難易度: 中級

第三十四観点 DISPLAY TRACE は z/OS 3.1 の 移行前確認 で扱う管理項目です（第三十四観点）。第三十四観点 システムトレースやコンポーネントトレースの状態を表示するコマンドという説明を操作結果と照合します（第三十四観点）。第三十四観点 IEE843I、DISPLAY LOGGER のログストリーム表示、定義メンバーを照合し、IEASYMxx反映漏れの検出を確認します（第三十四観点）。第三十四観点 証跡には資料IDと確認値を併記し、zOS31記録034として保存します（第三十四観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第三十四証跡です。z/OS 3.1 の 移行前確認 で切分けを行います。確認観点は DISPLAY TRACE、ログ確認、運用確認 です。IEASYMxx反映漏れの検出のために、DISPLAY LOGGER のログストリーム表示 を使った運用記録として最も適切な扱いはどれか。

    - A. 作業票034では DISPLAY LOGGER のログストリーム表示 と IEE843I と時刻を並べる。後続確認で DISPLAY TRACE の今回値を同じ対象として再確認できる。 ✅
    - B. IPL情報 の参考情報だけを作業票034へ先に書く。IEE843I とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - C. DISPLAY TRACE の名称欄だけを作業票034で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - D. 前回の正常出力を作業票034の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の DISPLAY LOGGER のログストリーム表示 と IEE843I を照合できない形にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 第三十四観点 正答根拠: Aは DISPLAY LOGGER のログストリーム表示 と IEE843I を結び付けるため、対象システムの取り違えを防げます（第三十四観点）。第三十四観点 診断背景: DISPLAY GRS、DISPLAY TRACE、DISPLAY LOGGERは直列化、トレース、ログの状態確認に使います（第三十四観点）。第三十四観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第三十四観点）。第三十四観点 用語説明: zHPFはHigh Performance FICONです（第三十四観点）。第三十四観点 IOSは入出力監視の表示対象です（第三十四観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **DISPLAY TRACE ログ確認 運用確認034**

    - 検証目的: DISPLAY TRACE の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: ISPF / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により DISPLAY TRACE の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(IEASYS31)
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEASYS31
    PROG=31
    SMF=31
    GRSRNL=31
    CON=31
    SCHED=31
    ```

    画面・出力には IEASYS31 が含まれる。IEASYS31 を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により DISPLAY TRACE の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(SMFPRM31)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMFPRM31
    SYS(TYPE(0:255))
    DSNAME(SMF.MAN1,SMF.MAN2)
    ACTIVE
    JWT(0030)
    ```

    画面・出力には SMFPRM31 が含まれる。SMFPRM31 を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により DISPLAY TRACE の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I 10.010.00 PARMLIB DISPLAY 753
    DATA SET NAME
    SYS1.PARMLIB
    SYS1.PARMLIB(IEASYS31)
    ```

    画面・出力には IEE251I が含まれる。IEE251I を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEASYS31 が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: SMFPRM31 が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE251I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### SLIP表示 ログ確認 運用確認084 {#c37-i0274}
*分類: 移行前確認*  ・  難易度: 上級

第八十四観点 z/OS 3.1 Core Operations の 移行前確認 では SLIP表示 を障害調査で照合します（第八十四観点）。第八十四観点 資料上は SLIPトラップや診断条件の定義状態を確認する表示対象として扱います（第八十四観点）。第八十四観点 SYS1.PARMLIB(GRSRNL31) を起点に表示値を戻し、IEASYMxx反映漏れの検出を点検します（第八十四観点）。第八十四観点 記録ではコマンド、メッセージID、対象名、時刻を zOS31記録084へ書きます（第八十四観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第八十四証跡です。z/OS 3.1 の 移行前確認 で切分けを行います。確認観点は SLIP表示、ログ確認、運用確認 です。IEASYMxx反映漏れの検出を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. システムログ の参考情報だけを作業票084へ先に書く。SYS1.PARMLIB(GRSRNL31) とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. SLIP表示 の名称欄だけを作業票084で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - C. 作業票084では DISPLAY PARMLIB のIEE251I表示 と SYS1.PARMLIB(GRSRNL31) と時刻を並べる。後続確認で SLIP表示 の今回値を同じ対象として再確認できる。 ✅
    - D. 前回の正常出力を作業票084の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の DISPLAY PARMLIB のIEE251I表示 と SYS1.PARMLIB(GRSRNL31) を照合できない形にする。

    正解: **C** ／ 難易度: 上級

    **解説:** 第八十四観点 照合結果: Cは SYS1.PARMLIB(GRSRNL31) をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十四観点）。第八十四観点 仕組み要点: LOADxxはIPL時のSYSPLEX値やIEASYMxx一覧などを指定します（第八十四観点）。第八十四観点 誤答確認: Aは SYS1.PARMLIB(GRSRNL31) 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第八十四観点）。第八十四観点 初出定義: WTORは応答要求メッセージです（第八十四観点）。第八十四観点 OPERLOGはオペレーター関連ログです（第八十四観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **SLIP表示 ログ確認 運用確認084**

    - 検証目的: SLIP表示 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SLIP表示 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.12 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SLIP表示 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SWITCH SMF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
    IEE360I SMF NOW RECORDING ON SMF.MAN2
    ```

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SLIP表示 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD12
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD12 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### 移行前確認 z/OS 3.1移行検査 ログとの照合 MIG07 {#c37-i0275}
*分類: 移行前確認*  ・  難易度: 中級

ログとの照合では 移行前確認 の リリース確認 を主操作として MIG07 を判定します。時刻と対象識別子への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG07 に残します。ログとの照合を補助する parmlib所在 では IEE251I を補助値として MIG07 へ保存します。主判定のログとの照合では移行前確認・移行検査の リリース確認 から RELEASE を読み MIG07 へ残します。証跡照合のログとの照合では移行前確認・移行検査の RELEASE と IEE251I を MIG07 に保存します。記録対応のログとの照合では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG07 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** ログとの照合で 移行前確認 の リリース確認 と parmlib所在 を組み合わせる際は z/OS 3.1移行検査 が旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備という仕組みを前提にします。旧構成の非互換値を次回IPLへ持ち込む危険があります。RELEASE と RELEASEとMEMBER差分 を対象 MIG07 で確認する組合せはどれですか。

    - A. RELEASEを含むリリース確認の応答行を保存する。その応答を得るためD IPLINFOを使用する。対象MIG07のRELEASEとMEMBER差分として記録する。 ✅
    - B. D IPLINFOが応答を返した時点で正常とする。応答中のRELEASEの値は記録しない。IEE250IをRELEASEと同じ判定値とみなし対象MIG07の主証跡にする。
    - C. D IPLINFOのコマンド文字列だけを記録する。RELEASEを含む応答行は保存しない。
    - D. z/OS 3.1移行検査の停止または再定義を実施する。その後にD IPLINFOでRELEASEを採取する。

    正解: **A** ／ 難易度: 中級

    **解説:** 適切な判定: Aはリリース確認で RELEASE を読みRELEASEとMEMBER差分の主値として操作とログを対応しMIG07に残します。
    機能の仕組み: ログとの照合ではparmlib所在を補助操作としz/OS 3.1移行検査の時刻と対象識別子をIEE251Iと対象MIG07で照合します。
    各候補の評価: リリース確認とparmlib所在の役割を分けるとA: RELEASEの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではRELEASEとMEMBER差分を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではRELEASEとMEMBER差分を証明できない点でRELEASEとMEMBER差分を確認できません、D: 変更前のRELEASEとMEMBER差分を失う点でparmlib所在の範囲を越えます。結論としてログとの照合の移行前確認・移行検査で判定する対象は MIG07 です。
    用語の定義: ログとの照合で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG07へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 ログとの照合 MIG07**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について操作とログを対応し、MIG07のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG07のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG07のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG07のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RELEASE が画面・出力に表示されること
    ② ステップ2 の IEE251I が画面・出力に表示されること
    ③ ステップ3 の IEE250I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 代替経路の確認 MIG10 {#c37-i0276}
*分類: 移行前確認*  ・  難易度: 中級

代替経路の確認では 移行前確認 の リリース確認 を主操作として MIG10 を判定します。主経路との役割差への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG10 に残します。代替経路の確認を補助する parmlib所在 では IEE251I を補助値として MIG10 へ保存します。主判定の代替経路の確認では移行前確認・移行検査の リリース確認 から RELEASE を読み MIG10 へ残します。証跡照合の代替経路の確認では移行前確認・移行検査の RELEASE と IEE251I を MIG10 に保存します。記録対応の代替経路の確認では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG10 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 移行前確認 の リリース確認 と parmlib所在 を実施し z/OS 3.1移行検査 の役割を確認します。旧構成の非互換値を次回IPLへ持ち込む危険があります。対象 MIG10 の証跡を取る方法はどれですか。

    - A. D IPLINFOのコマンド文字列だけを記録する。RELEASEを含む応答行は保存しない。
    - B. z/OS 3.1移行検査の停止または再定義を実施する。その後にD IPLINFOでRELEASEを採取する。
    - C. IPL情報のLOADxxとIODFを確認する。その値を移行前確認のMIG10にも適用する。
    - D. D IPLINFOとD PARMLIBの対象名をそろえる。前者のRELEASEをRELEASEとMEMBER差分の判定値として採用する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい判定結果: Dはリリース確認で RELEASE を読みRELEASEとMEMBER差分の主値として代替手段の成立を確認しMIG10に残します。
    運用上の背景: 代替経路の確認ではparmlib所在を補助操作としz/OS 3.1移行検査の主経路との役割差をIEE251Iと対象MIG10で照合します。
    候補別の検討: リリース確認とparmlib所在の役割を分けるとA: 入力記録だけではRELEASEとMEMBER差分を証明できない点で一次資料と一致しません、B: 変更前のRELEASEとMEMBER差分を失う点でRELEASEとMEMBER差分を確認できません、C: IPL情報の値ではRELEASEを確認できない点でparmlib所在の範囲を越えます、D: 同じ対象名のRELEASEを採用する点で現在値を示します。結論として代替経路の確認の移行前確認・移行検査で判定する対象は MIG10 です。
    重要用語の定義: 代替経路の確認で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG10へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 代替経路の確認 MIG10**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について代替手段の成立を確認し、MIG10のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG10のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG10のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG10のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RELEASE が画面・出力に表示されること
    ② ステップ2 の IEE251I が画面・出力に表示されること
    ③ ステップ3 の IEE250I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 変更前の確認 MIG02 {#c37-i0277}
*分類: 移行前確認*  ・  難易度: 中級

変更前の確認では 移行前確認 の parmlib所在 を主操作として MIG02 を判定します。変更対象と非対象の境界への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG02 に残します。変更前の確認を補助する APF確認 では IEE250I を補助値として MIG02 へ保存します。主判定の変更前の確認では移行前確認・移行検査の parmlib所在 から IEE251I を読み MIG02 へ残します。証跡照合の変更前の確認では移行前確認・移行検査の IEE251I と IEE250I を MIG02 に保存します。記録対応の変更前の確認では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG02 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 移行前確認 の parmlib所在 と APF確認 の役割を分け 変更対象と非対象の境界 を調べます。z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備です。旧構成の非互換値を次回IPLへ持ち込む危険があります。対象 MIG02 を誤判定しない進め方はどれですか。

    - A. D PARMLIBを対象名なしで実行する。一覧の先頭行をMIG02の結果として記録する。
    - B. 前回保存したD PARMLIBの結果を使う。今回のD PROG,APFの結果と同一時点の証跡として比較する。
    - C. 保存済みのMIG02の出力を再利用する。今回のD PARMLIBとD PROG,APFは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象MIG02についてD PARMLIBの応答からIEE251Iを確認する。D PROG,APFは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 採用理由: Dはparmlib所在で IEE251I を読みRELEASEとMEMBER差分の主値として変更前の証跡を保存しMIG02に残します。
    動作の背景: 変更前の確認ではAPF確認を補助操作としz/OS 3.1移行検査の変更対象と非対象の境界をIEE250Iと対象MIG02で照合します。
    各選択肢の検討: parmlib所在とAPF確認の役割を分けるとA: 先頭行はMIG02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でparmlib所在を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で移行前確認に使いません、D: IEE251Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の移行前確認・移行検査で判定する対象は MIG02 です。
    初出用語の定義: 変更前の確認で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG02へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 変更前の確認 MIG02**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について変更前の証跡を保存し、MIG02のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG02のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG02のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG02のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE251I が画面・出力に表示されること
    ② ステップ2 の IEE250I が画面・出力に表示されること
    ③ ステップ3 の RELEASE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 変更後の確認 MIG03 {#c37-i0278}
*分類: 移行前確認*  ・  難易度: 中級

変更後の確認では 移行前確認 の APF確認 を主操作として MIG03 を判定します。反映値と残存値への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG03 に残します。変更後の確認を補助する リリース確認 では RELEASE を補助値として MIG03 へ保存します。主判定の変更後の確認では移行前確認・移行検査の APF確認 から IEE250I を読み MIG03 へ残します。証跡照合の変更後の確認では移行前確認・移行検査の IEE250I と RELEASE を MIG03 に保存します。記録対応の変更後の確認では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG03 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 移行前確認 の APF確認 と リリース確認 を使い 変更結果を検証 します。z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備です。旧構成の非互換値を次回IPLへ持ち込む危険があります。IEE250I を読み対象 MIG03 を切り分ける確認方法はどれですか。

    - A. D IPLINFOで周辺状態を押さえる。その後にD PROG,APFでIEE250Iを確認して変更結果を検証する。 ✅
    - B. z/OS 3.1移行検査の停止または再定義を実施する。その後にD PROG,APFでIEE250Iを採取する。
    - C. z/OSMF管理のSERVICE STATUSとHOME URIを確認する。その値を移行前確認のMIG03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D IPLINFOが成功したためD PROG,APFのIEE250Iも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正答の根拠: AはAPF確認で IEE250I を読みRELEASEとMEMBER差分の主値として変更結果を検証しMIG03に残します。
    内部の仕組み: 変更後の確認ではリリース確認を補助操作としz/OS 3.1移行検査の反映値と残存値をRELEASEと対象MIG03で照合します。
    誤答を含む比較: APF確認とリリース確認の役割を分けるとA: 周辺状態の後にIEE250Iを確認する点でMIG03を判定できます、B: 変更前のRELEASEとMEMBER差分を失う点でリリース確認の範囲を越えます、C: z/OSMF管理の値ではIEE250Iを確認できないうえに追加前提も不正な点でMIG03の値を示しません、D: 補助操作の成功ではIEE250Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の移行前確認・移行検査で判定する対象は MIG03 です。
    用語定義: 変更後の確認で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG03へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 変更後の確認 MIG03**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について変更結果を検証し、MIG03のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG03のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG03のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG03のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE250I が画面・出力に表示されること
    ② ステップ2 の RELEASE が画面・出力に表示されること
    ③ ステップ3 の IEE251I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 引継ぎ記録 MIG09 {#c37-i0279}
*分類: 移行前確認*  ・  難易度: 中級

引継ぎ記録では 移行前確認 の APF確認 を主操作として MIG09 を判定します。次担当者が追跡できる証跡への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG09 に残します。引継ぎ記録を補助する リリース確認 では RELEASE を補助値として MIG09 へ保存します。主判定の引継ぎ記録では移行前確認・移行検査の APF確認 から IEE250I を読み MIG09 へ残します。証跡照合の引継ぎ記録では移行前確認・移行検査の IEE250I と RELEASE を MIG09 に保存します。記録対応の引継ぎ記録では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG09 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 移行前確認 の APF確認 と リリース確認 を使い 再現可能な記録を作成 します。z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備です。旧構成の非互換値を次回IPLへ持ち込む危険があります。IEE250I を読み対象 MIG09 を切り分ける確認方法はどれですか。

    - A. D IPLINFOが成功したためD PROG,APFのIEE250Iも正常だと推定する。主出力は保存しない。
    - B. D PROG,APFを対象名なしで実行する。一覧の先頭行をMIG09の結果として記録する。
    - C. 対象名MIG09を指定してD PROG,APFを実行する。応答中のIEE250Iと時刻を保存する。D IPLINFOで周辺状態を補完する。 ✅
    - D. 前回保存したD PROG,APFの結果を使う。今回のD IPLINFOの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 中級

    **解説:** 採用操作の理由: CはAPF確認で IEE250I を読みRELEASEとMEMBER差分の主値として再現可能な記録を作成しMIG09に残します。
    製品内の仕組み: 引継ぎ記録ではリリース確認を補助操作としz/OS 3.1移行検査の次担当者が追跡できる証跡をRELEASEと対象MIG09で照合します。
    選択肢別の説明: APF確認とリリース確認の役割を分けるとA: 補助操作の成功ではIEE250Iを確定できない点でMIG09の値を示しません、B: 先頭行はMIG09と確定できない点で引継ぎ記録に合いません、C: IEE250Iと時刻を保存する点でAPF確認に合います、D: 採取時刻が異なる点で移行前確認に使いません。結論として引継ぎ記録の移行前確認・移行検査で判定する対象は MIG09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG09へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 引継ぎ記録 MIG09**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について再現可能な記録を作成し、MIG09のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG09のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG09のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG09のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE250I が画面・出力に表示されること
    ② ステップ2 の RELEASE が画面・出力に表示されること
    ③ ステップ3 の IEE251I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 復旧後の確認 MIG06 {#c37-i0280}
*分類: 移行前確認*  ・  難易度: 中級

復旧後の確認では 移行前確認 の APF確認 を主操作として MIG06 を判定します。再発していないことを示す値への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG06 に残します。復旧後の確認を補助する リリース確認 では RELEASE を補助値として MIG06 へ保存します。主判定の復旧後の確認では移行前確認・移行検査の APF確認 から IEE250I を読み MIG06 へ残します。証跡照合の復旧後の確認では移行前確認・移行検査の IEE250I と RELEASE を MIG06 に保存します。記録対応の復旧後の確認では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG06 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 移行前確認 の APF確認 と リリース確認 を照合し 再発していないことを示す値 を確かめます。z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備です。旧構成の非互換値を次回IPLへ持ち込む危険があります。IEE250I を読む前に対象 MIG06 へ行う確認はどれですか。

    - A. コンソール管理のCONSOLE NAMEとAUTHを確認する。その値を移行前確認のMIG06にも適用する。
    - B. D IPLINFOが成功したためD PROG,APFのIEE250Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象MIG06へ引き継げるものとする。
    - C. D PROG,APFを対象名なしで実行する。一覧の先頭行をMIG06の結果として記録する。
    - D. D PROG,APFでIEE250Iを取得してからD PARMLIBでIEE251Iを照合する。MIG06のRELEASEとMEMBER差分を両出力から確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答内容: DはAPF確認で IEE250I を読みRELEASEとMEMBER差分の主値として復旧後の安定性を確認しMIG06に残します。
    構成上の背景: 復旧後の確認ではリリース確認を補助操作としz/OS 3.1移行検査の再発していないことを示す値をRELEASEと対象MIG06で照合します。
    候補ごとの理由: APF確認とリリース確認の役割を分けるとA: コンソール管理の値ではIEE250Iを確認できない点でリリース確認の範囲を越えます、B: 補助操作の成功ではIEE250Iを確定できないうえに追加前提も不正な点でMIG06の値を示しません、C: 先頭行はMIG06と確定できない点で復旧後の確認に合いません、D: IEE250IとIEE251Iを順に照合する点でAPF確認に合います。結論として復旧後の確認の移行前確認・移行検査で判定する対象は MIG06 です。
    初出用語: 復旧後の確認で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG06へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 復旧後の確認 MIG06**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について復旧後の安定性を確認し、MIG06のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG06のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG06のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG06のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE250I が画面・出力に表示されること
    ② ステップ2 の RELEASE が画面・出力に表示されること
    ③ ステップ3 の IEE251I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 復旧準備 MIG05 {#c37-i0281}
*分類: 移行前確認*  ・  難易度: 中級

復旧準備では 移行前確認 の parmlib所在 を主操作として MIG05 を判定します。再開前に必要な整合性への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG05 に残します。復旧準備を補助する APF確認 では IEE250I を補助値として MIG05 へ保存します。主判定の復旧準備では移行前確認・移行検査の parmlib所在 から IEE251I を読み MIG05 へ残します。証跡照合の復旧準備では移行前確認・移行検査の IEE251I と IEE250I を MIG05 に保存します。記録対応の復旧準備では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG05 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 復旧準備で 移行前確認 の parmlib所在 と APF確認 を用い 復旧条件を確認 します。z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備です。旧構成の非互換値を次回IPLへ持ち込む危険があります。IEE251I で対象 MIG05 の RELEASEとMEMBER差分 を再現できる記録はどれですか。

    - A. 前回保存したD PARMLIBの結果を使う。今回のD PROG,APFの結果と同一時点の証跡として比較する。
    - B. 保存済みのMIG05の出力を再利用する。今回のD PARMLIBとD PROG,APFは実行済みとして扱う。
    - C. 変更を加えずD PARMLIBを実行する。IEE251Iを保存する。差分はD PROG,APFの結果と対象名で対応させる。 ✅
    - D. D PROG,APFのIEE250IをRELEASEとMEMBER差分の主判定に採用する。D PARMLIBの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 中級

    **解説:** 選定理由: Cはparmlib所在で IEE251I を読みRELEASEとMEMBER差分の主値として復旧条件を確認しMIG05に残します。
    処理の仕組み: 復旧準備ではAPF確認を補助操作としz/OS 3.1移行検査の再開前に必要な整合性をIEE250Iと対象MIG05で照合します。
    選択結果の内訳: parmlib所在とAPF確認の役割を分けるとA: 採取時刻が異なる点でparmlib所在を代替しません、B: 過去出力では今回の復旧準備を示せない点で移行前確認に使いません、C: 変更前のIEE251Iを保存する点で正答です、D: IEE250IはIEE251Iを代替しないうえに追加前提も不正な点でMIG05を採用できません。結論として復旧準備の移行前確認・移行検査で判定する対象は MIG05 です。
    用語の説明: 復旧準備で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG05へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 復旧準備 MIG05**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について復旧条件を確認し、MIG05のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG05のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG05のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG05のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE251I が画面・出力に表示されること
    ② ステップ2 の IEE250I が画面・出力に表示されること
    ③ ステップ3 の RELEASE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 構成監査 MIG08 {#c37-i0282}
*分類: 移行前確認*  ・  難易度: 中級

構成監査では 移行前確認 の parmlib所在 を主操作として MIG08 を判定します。定義値と稼働値の一致への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG08 に残します。構成監査を補助する APF確認 では IEE250I を補助値として MIG08 へ保存します。主判定の構成監査では移行前確認・移行検査の parmlib所在 から IEE251I を読み MIG08 へ残します。証跡照合の構成監査では移行前確認・移行検査の IEE251I と IEE250I を MIG08 に保存します。記録対応の構成監査では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG08 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 構成監査で 移行前確認 の parmlib所在 と APF確認 の役割を分け 定義値と稼働値の一致 を調べます。z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備です。旧構成の非互換値を次回IPLへ持ち込む危険があります。対象 MIG08 を誤判定しない進め方はどれですか。

    - A. 保存済みのMIG08の出力を再利用する。今回のD PARMLIBとD PROG,APFは実行済みとして扱う。
    - B. D PROG,APFの結果だけでは確定しない。D PARMLIBのIEE251Iを主証跡として構成差分を監査する。 ✅
    - C. D PROG,APFのIEE250IをRELEASEとMEMBER差分の主判定に採用する。D PARMLIBの応答は採取対象から外す。
    - D. D IPLINFOのRELEASEをIEE251Iと同義の成功表示として扱う。D PARMLIBは実行しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 技術上の正答: Bはparmlib所在で IEE251I を読みRELEASEとMEMBER差分の主値として構成差分を監査しMIG08に残します。
    実行時の背景: 構成監査ではAPF確認を補助操作としz/OS 3.1移行検査の定義値と稼働値の一致をIEE250Iと対象MIG08で照合します。
    四つの候補の理由: parmlib所在とAPF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点で移行前確認に使いません、B: IEE251Iを主証跡として区別する点で正答です、C: IEE250IはIEE251Iを代替しない点でMIG08を採用できません、D: RELEASEとIEE251Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の移行前確認・移行検査で判定する対象は MIG08 です。
    初出語定義: 構成監査で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG08へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 構成監査 MIG08**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について構成差分を監査し、MIG08のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG08のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG08のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG08のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE251I が画面・出力に表示されること
    ② ステップ2 の IEE250I が画面・出力に表示されること
    ③ ステップ3 の RELEASE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 通常状態の確認 MIG01 {#c37-i0283}
*分類: 移行前確認*  ・  難易度: 中級

通常状態の確認では 移行前確認 の リリース確認 を主操作として MIG01 を判定します。基準値と現在値の差への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG01 に残します。通常状態の確認を補助する parmlib所在 では IEE251I を補助値として MIG01 へ保存します。主判定の通常状態の確認では移行前確認・移行検査の リリース確認 から RELEASE を読み MIG01 へ残します。証跡照合の通常状態の確認では移行前確認・移行検査の RELEASE と IEE251I を MIG01 に保存します。記録対応の通常状態の確認では移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG01 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 移行前確認 の リリース確認 と parmlib所在 を組み合わせる際は z/OS 3.1移行検査 が旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備という仕組みを前提にします。旧構成の非互換値を次回IPLへ持ち込む危険があります。RELEASE と RELEASEとMEMBER差分 を対象 MIG01 で確認する組合せはどれですか。

    - A. D PARMLIBのIEE251IをRELEASEとMEMBER差分の主判定に採用する。D IPLINFOの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. D PROG,APFのIEE250IをRELEASEと同義の成功表示として扱う。D IPLINFOは実行しない。
    - C. D IPLINFOを先に実行する。対象MIG01のRELEASEをRELEASEとMEMBER差分として記録する。続いてD PARMLIBで同一対象を照合する。 ✅
    - D. D IPLINFOが応答を返した時点で正常とする。応答中のRELEASEの値は記録しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解の説明: Cはリリース確認で RELEASE を読みRELEASEとMEMBER差分の主値として通常状態を確定しMIG01に残します。
    背景・仕組み: 通常状態の確認ではparmlib所在を補助操作としz/OS 3.1移行検査の基準値と現在値の差をIEE251Iと対象MIG01で照合します。
    選択肢の理由: リリース確認とparmlib所在の役割を分けるとA: IEE251IはRELEASEを代替しないうえに追加前提も不正な点でz/OS 3.1移行検査に使えません、B: IEE250IとRELEASEは確認項目が異なる点でMIG01を採用できません、C: RELEASEを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではRELEASEとMEMBER差分を判定できない点で一次資料と一致しません。結論として通常状態の確認の移行前確認・移行検査で判定する対象は MIG01 です。
    用語の初出定義: 通常状態の確認で使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG01へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 通常状態の確認 MIG01**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について通常状態を確定し、MIG01のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG01のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG01のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG01のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RELEASE が画面・出力に表示されること
    ② ステップ2 の IEE251I が画面・出力に表示されること
    ③ ステップ3 の IEE250I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 移行前確認 z/OS 3.1移行検査 障害切り分け MIG04 {#c37-i0284}
*分類: 移行前確認*  ・  難易度: 中級

障害切り分けでは 移行前確認 の リリース確認 を主操作として MIG04 を判定します。最初に失敗した処理への注意として「旧構成の非互換値を次回IPLへ持ち込む危険があります」を MIG04 に残します。障害切り分けを補助する parmlib所在 では IEE251I を補助値として MIG04 へ保存します。主判定の障害切り分けでは移行前確認・移行検査の リリース確認 から RELEASE を読み MIG04 へ残します。証跡照合の障害切り分けでは移行前確認・移行検査の RELEASE と IEE251I を MIG04 に保存します。記録対応の障害切り分けでは移行前確認・移行検査の RELEASEとMEMBER差分 の証跡へ MIG04 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 移行前確認 の リリース確認 と parmlib所在 を実施し z/OS 3.1移行検査 の役割を確認します。旧構成の非互換値を次回IPLへ持ち込む危険があります。対象 MIG04 の証跡を取る方法はどれですか。

    - A. D PROG,APFのIEE250IをRELEASEと同義の成功表示として扱う。D IPLINFOは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D IPLINFOの出力でMIG04とRELEASEが同じ応答にあることを確認する。RELEASEとMEMBER差分をその応答から採取する。 ✅
    - C. D IPLINFOが応答を返した時点で正常とする。応答中のRELEASEの値は記録しない。
    - D. D IPLINFOのコマンド文字列だけを記録する。RELEASEを含む応答行は保存しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Bはリリース確認で RELEASE を読みRELEASEとMEMBER差分の主値として障害範囲を限定しMIG04に残します。
    技術的背景: 障害切り分けではparmlib所在を補助操作としz/OS 3.1移行検査の最初に失敗した処理をIEE251Iと対象MIG04で照合します。
    四択の評価: リリース確認とparmlib所在の役割を分けるとA: IEE250IとRELEASEは確認項目が異なるうえに追加前提も不正な点でMIG04を採用できません、B: MIG04とRELEASEを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではRELEASEとMEMBER差分を判定できない点で一次資料と一致しません、D: 入力記録だけではRELEASEとMEMBER差分を証明できない点でRELEASEとMEMBER差分を確認できません。結論として障害切り分けの移行前確認・移行検査で判定する対象は MIG04 です。
    初出語の意味: 障害切り分けで使う z/OS 3.1移行検査 は旧リリースの設定、削除機能、必要保守、parmlib差分をIPL前に確認する移行準備を表しRELEASEとMEMBER差分を判定する際にMIG04へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **移行前確認 z/OS 3.1移行検査 障害切り分け MIG04**

    - 検証目的: 移行前確認のz/OS 3.1移行検査について障害範囲を限定し、MIG04のRELEASEとMEMBER差分を実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象MIG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD IPLINFOを指定し、MIG04のリリース確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D IPLINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE254I RELEASE z/OS 03.01.00 LICENSE z/OS
    ```

    画面・出力にあるRELEASEを読み、RELEASEとMEMBER差分と対象MIG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PARMLIBを指定し、MIG04のparmlib所在を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PARMLIB
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE251I ACTIVE PARMLIB DATA SETS 1 SYS1.PARMLIB 2 SYS1.PARMLIB.SITE
    ```

    画面・出力にあるIEE251Iを読み、RELEASEとMEMBER差分と対象MIG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの移行前確認を確認する入力画面です。COMMAND入力口へD PROG,APFを指定し、MIG04のAPF確認を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE250I DISPLAY PROG,APF FORMAT=DYNAMIC ENTRIES 0042
    ```

    画面・出力にあるIEE250Iを読み、RELEASEとMEMBER差分と対象MIG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RELEASE が画面・出力に表示されること
    ② ステップ2 の IEE251I が画面・出力に表示されること
    ③ ステップ3 の IEE250I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300




## z/OS 3.1 Core Operations > 結合機構確認

### ISFPRMxx 定義照合 運用確認061 {#c37-i0285}
*分類: 結合機構確認*  ・  難易度: 中級

第六十一観点 結合機構確認 で ISFPRMxx は 定義照合 の対象です（第六十一観点）。第六十一観点 確認時には z/OS 3.1でSDSF設定に使用されるparmlib形式の設定メという性質を前提にします（第六十一観点）。第六十一観点 DISPLAY SYMBOLS のシンボル一覧 と SYS1.PARMLIB(SMFPRM31) を同じ証跡に置き、IEASYMxx反映漏れの検出を管理します（第六十一観点）。第六十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOS31記録061から再現します（第六十一観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第六十一証跡です。結合機構確認 の運用で ISFPRMxx を点検します。確認観点は ISFPRMxx、定義照合、運用確認 です。SYS1.PARMLIB(SMFPRM31) を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. 作業票061では DISPLAY SYMBOLS のシンボル一覧 と SYS1.PARMLIB(SMFPRM31) と時刻を並べる。後続確認で ISFPRMxx の今回値を同じ対象として再確認できる。 ✅
    - B. SMF管理 の参考情報だけを作業票061へ先に書く。SYS1.PARMLIB(SMFPRM31) とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - C. ISFPRMxx の名称欄だけを作業票061で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - D. 前回の正常出力を作業票061の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の DISPLAY SYMBOLS のシンボル一覧 と SYS1.PARMLIB(SMFPRM31) を照合できない形にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 第六十一観点 正解確認: Aは ISFPRMxx と SYS1.PARMLIB(SMFPRM31) を同じ証跡で扱うため、後続の照合に使えます（第六十一観点）。第六十一観点 記録背景: SMFはSMFPRMxx、SMF=xx、SMFPRM00で記録方針を管理します（第六十一観点）。第六十一観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第六十一観点）。第六十一観点 用語確認: LOADxxはIPL制御メンバーです（第六十一観点）。第六十一観点 IEASYMxxはシステムシンボル定義です（第六十一観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **ISFPRMxx 定義照合 運用確認061**

    - 検証目的: ISFPRMxx の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / console operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ISFPRMxx の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C,ROUT=5
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNZ4100I 15.03.13 CONSOLE DISPLAY FRAME 1 SYS=SY1
    CONSOLES MATCHING COMMAND: D C,ROUT=5
    MSG:CURR=1356 LIM=1500 RPLY:CURR=1 LIM=10
    FRED TYPE=MCS STATUS=ACT-SY2 AUTH=(MASTER) AREA=(Z,A)
    ```

    画面・出力には CNZ4100I が含まれる。CNZ4100I を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ISFPRMxx の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.13 DISPLAY R 760
    REPLY ID   MESSAGE TEXT
    005        IEA011A RESPECIFY ENTIRE IEASYMXX SUFFIX LIST OR U TO BYPASS
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ISFPRMxx の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> LOG 'ZOS31 CHECK 061 COMPLETE'
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I LOG COMMAND ACCEPTED
    OPERLOG ENTRY: ZOS31 CHECK 061 COMPLETE
    ```

    画面・出力には OPERLOG が含まれる。OPERLOG を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    - 合格条件: ステップ1: CNZ4100I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE112I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: OPERLOG が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### IZUPRMxx 出口確認 運用確認045 {#c37-i0286}
*分類: 結合機構確認*  ・  難易度: 中級

第四十五観点 結合機構確認 で IZUPRMxx は 出口確認 の対象です（第四十五観点）。第四十五観点 確認時には z/OSMFサーバーやサービス構成を定義するparmlibメンバーという性質を前提にします（第四十五観点）。第四十五観点 DISPLAY GRS のISG343I表示 と SYS1.PARMLIB(IZUPRM31) を同じ証跡に置き、IODF参照値の説明性確保を管理します（第四十五観点）。第四十五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOS31記録045から再現します（第四十五観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第四十五証跡です。DISPLAY GRS のISG343I表示 を採取した後の扱いを選びます。確認観点は IZUPRMxx、出口確認、運用確認 です。DISPLAY GRS のISG343I表示 と SYS1.PARMLIB(IZUPRM31) を合わせて読む時の採用方針として正しいものはどれか。

    - A. IODF確認 の参考情報だけを作業票045へ先に書く。SYS1.PARMLIB(IZUPRM31) とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. 作業票045では DISPLAY GRS のISG343I表示 と SYS1.PARMLIB(IZUPRM31) と時刻を並べる。後続確認で IZUPRMxx の今回値を同じ対象として再確認できる。 ✅
    - C. IZUPRMxx の名称欄だけを作業票045で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - D. 前回の正常出力を作業票045の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の DISPLAY GRS のISG343I表示 と SYS1.PARMLIB(IZUPRM31) を照合できない形にする。

    正解: **B** ／ 難易度: 中級

    **解説:** 第四十五観点 正解確認: Bは IZUPRMxx と SYS1.PARMLIB(IZUPRM31) を同じ証跡で扱うため、後続の照合に使えます（第四十五観点）。第四十五観点 実行背景: D IOS,ZHPFとD IOS,ZHPFOPTSはHigh Performance FICONの状態とオプションを確認します（第四十五観点）。第四十五観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十五観点）。第四十五観点 用語整理: IODFは入出力定義ファイルです（第四十五観点）。第四十五観点 IPL装置は起動に使った装置です（第四十五観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **IZUPRMxx 出口確認 運用確認045**

    - 検証目的: IZUPRMxx の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / console operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IZUPRMxx の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C,ROUT=5
    → Enter を押す
    ```

    画面・出力:
    ```text
    CNZ4100I 15.03.21 CONSOLE DISPLAY FRAME 1 SYS=SY1
    CONSOLES MATCHING COMMAND: D C,ROUT=5
    MSG:CURR=1356 LIM=1500 RPLY:CURR=1 LIM=10
    FRED TYPE=MCS STATUS=ACT-SY2 AUTH=(MASTER) AREA=(Z,A)
    ```

    画面・出力には CNZ4100I が含まれる。CNZ4100I を読み取り、IODF参照値の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IZUPRMxx の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.21 DISPLAY R 744
    REPLY ID   MESSAGE TEXT
    005        IEA011A RESPECIFY ENTIRE IEASYMXX SUFFIX LIST OR U TO BYPASS
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、IODF参照値の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IZUPRMxx の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> LOG 'ZOS31 CHECK 045 COMPLETE'
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I LOG COMMAND ACCEPTED
    OPERLOG ENTRY: ZOS31 CHECK 045 COMPLETE
    ```

    画面・出力には OPERLOG が含まれる。OPERLOG を読み取り、IODF参照値の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: CNZ4100I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE112I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: OPERLOG が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### LNKLSTxx更新 定義照合 運用確認011 {#c37-i0287}
*分類: 結合機構確認*  ・  難易度: 初級

第十一観点 結合機構確認 の運用では LNKLSTxx更新 を表示、定義、証跡で確認します（第十一観点）。第十一観点 役割は リンクリストへ追加するライブラリーを移行時に確認する更新対象という範囲です（第十一観点）。第十一観点 D IPLINFO のIEE254I表示 の値を IEE254I と合わせ、IEASYMxx反映漏れの検出を記録します（第十一観点）。第十一観点 確認経路は SDSF、コンソールログ、parmlib、z/OSMF の別を zOS31記録011に残します（第十一観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第十一証跡です。結合機構確認 の運用で LNKLSTxx更新 を点検します。確認観点は LNKLSTxx更新、定義照合、運用確認 です。D IPLINFO のIEE254I表示 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. SLIP/DUMP の参考情報だけを作業票011へ先に書く。IEE254I とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. LNKLSTxx更新 の名称欄だけを作業票011で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - C. 前回の正常出力を作業票011の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の D IPLINFO のIEE254I表示 と IEE254I を照合できない形にする。
    - D. 作業票011では D IPLINFO のIEE254I表示 と IEE254I と時刻を並べる。後続確認で LNKLSTxx更新 の今回値を同じ対象として再確認できる。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 第十一観点 採用理由: Dは LNKLSTxx更新 の状態を表示値と定義の両方から確認するため、記録として妥当です（第十一観点）。第十一観点 背景確認: DISPLAY IPLINFOはIPL日時、LOADxx、IEASYSxx、IEASYMxx、IODF、IPL装置をまとめて示します（第十一観点）。第十一観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Cは再現性不足が理由です（第十一観点）。第十一観点 用語メモ: GRSは資源直列化です（第十一観点）。第十一観点 RNLは資源名リストです（第十一観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **LNKLSTxx更新 定義照合 運用確認011**

    - 検証目的: LNKLSTxx更新 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LNKLSTxx更新 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.11 GRS STATUS 830
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LNKLSTxx更新 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.11 GRS STATUS 840
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LNKLSTxx更新 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.11 DISPLAY XCF 850
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、IEASYMxx反映漏れの検出のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### LOGコマンド ストレージ確認 運用確認028 {#c37-i0288}
*分類: 結合機構確認*  ・  難易度: 中級

第二十八観点 z/OS 3.1 Core Operations の 結合機構確認 では LOGコマンド を障害調査で照合します（第二十八観点）。第二十八観点 資料上は オペレーターがシステムログまたはOPERLOGへ任意の記録を残すコマとして扱います（第二十八観点）。第二十八観点 IPLDEV=0A82 を起点に表示値を戻し、移行前parmlib差分の記録を点検します（第二十八観点）。第二十八観点 記録ではコマンド、メッセージID、対象名、時刻を zOS31記録028へ書きます（第二十八観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第二十八証跡です。LOGコマンド の記録を監査用に整えます。確認観点は LOGコマンド、ストレージ確認、運用確認 です。移行前parmlib差分の記録のために、D IOS,ZHPF のIOS630I表示 を使った運用記録として最も適切な扱いはどれか。

    - A. zHPF確認 の参考情報だけを作業票028へ先に書く。IPLDEV=0A82 とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. LOGコマンド の名称欄だけを作業票028で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - C. 前回の正常出力を作業票028の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の D IOS,ZHPF のIOS630I表示 と IPLDEV=0A82 を照合できない形にする。
    - D. 作業票028では D IOS,ZHPF のIOS630I表示 と IPLDEV=0A82 と時刻を並べる。後続確認で LOGコマンド の今回値を同じ対象として再確認できる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第二十八観点 照合結果: Dは IPLDEV=0A82 をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第二十八観点）。第二十八観点 診断背景: DISPLAY GRS、DISPLAY TRACE、DISPLAY LOGGERは直列化、トレース、ログの状態確認に使います（第二十八観点）。第二十八観点 誤答確認: Aは IPLDEV=0A82 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第二十八観点）。第二十八観点 用語説明: zHPFはHigh Performance FICONです（第二十八観点）。第二十八観点 IOSは入出力監視の表示対象です（第二十八観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **LOGコマンド ストレージ確認 運用確認028**

    - 検証目的: LOGコマンド の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LOGコマンド の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.04 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、移行前parmlib差分の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LOGコマンド の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SWITCH SMF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
    IEE360I SMF NOW RECORDING ON SMF.MAN2
    ```

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、移行前parmlib差分の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LOGコマンド の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD04
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD04 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、移行前parmlib差分の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### OPERLOG ストレージ確認 運用確認078 {#c37-i0289}
*分類: 結合機構確認*  ・  難易度: 中級

第七十八観点 OPERLOG は z/OS 3.1 の 結合機構確認 で扱う管理項目です（第七十八観点）。第七十八観点 複数システムのオペレーター関連メッセージを収集して確認できるログという説明を操作結果と照合します（第七十八観点）。第七十八観点 SYS1.PARMLIB(IEASYS31)、DISPLAY SMF の記録状態表示、定義メンバーを照合し、移行前parmlib差分の記録を確認します（第七十八観点）。第七十八観点 証跡には資料IDと確認値を併記し、zOS31記録078として保存します（第七十八観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第七十八証跡です。OPERLOG の記録を監査用に整えます。確認観点は OPERLOG、ストレージ確認、運用確認 です。移行前parmlib差分の記録を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. PARMLIB更新 の参考情報だけを作業票078へ先に書く。SYS1.PARMLIB(IEASYS31) とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. OPERLOG の名称欄だけを作業票078で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - C. 前回の正常出力を作業票078の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の DISPLAY SMF の記録状態表示 と SYS1.PARMLIB(IEASYS31) を照合できない形にする。
    - D. 作業票078では DISPLAY SMF の記録状態表示 と SYS1.PARMLIB(IEASYS31) と時刻を並べる。後続確認で OPERLOG の今回値を同じ対象として再確認できる。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第七十八観点 正答根拠: Dは DISPLAY SMF の記録状態表示 と SYS1.PARMLIB(IEASYS31) を結び付けるため、対象システムの取り違えを防げます（第七十八観点）。第七十八観点 仕組み要点: LOADxxはIPL時のSYSPLEX値やIEASYMxx一覧などを指定します（第七十八観点）。第七十八観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第七十八観点）。第七十八観点 初出定義: WTORは応答要求メッセージです（第七十八観点）。第七十八観点 OPERLOGはオペレーター関連ログです（第七十八観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **OPERLOG ストレージ確認 運用確認078**

    - 検証目的: OPERLOG の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / IOS and trace

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により OPERLOG の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D IOS,ZHPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IOS630I 13.10.06 ZHPF DISPLAY 317
    ZHPF FACILITY STATUS: ENABLED
    SYSTEM=SY106
    ```

    画面・出力には IOS630I が含まれる。IOS630I を読み取り、移行前parmlib差分の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により OPERLOG の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D IOS,ZHPFOPTS
    → Enter を押す
    ```

    画面・出力:
    ```text
    IOS631I 13.11.06 ZHPF OPTIONS DISPLAY
    MAXDATA=2048K
    PAV=SUPPORTED
    HPF=ENABLED
    ```

    画面・出力には MAXDATA=2048K が含まれる。MAXDATA=2048K を読み取り、移行前parmlib差分の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により OPERLOG の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.30.06 TRACE DISPLAY 177
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
    ```

    画面・出力には IEE843I が含まれる。IEE843I を読み取り、移行前parmlib差分の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: IOS630I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: MAXDATA=2048K が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE843I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### Parmlib Management 出口確認 運用確認095 {#c37-i0290}
*分類: 結合機構確認*  ・  難易度: 上級

第九十五観点 結合機構確認 の運用では Parmlib Management を表示、定義、証跡で確認します（第九十五観点）。第九十五観点 役割は z/OSMFからparmlibメンバーの構文検証や更新確認を行う機能という範囲です（第九十五観点）。第九十五観点 D IPLINFO のIEE254I表示 の値を IEE112I と合わせ、IODF参照値の説明性確保を記録します（第九十五観点）。第九十五観点 確認経路は SDSF、コンソールログ、parmlib、z/OSMF の別を zOS31記録095に残します（第九十五観点）。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx

??? question "確認問題（1問）"
    **問題.** 運用第九十五証跡です。D IPLINFO のIEE254I表示 を採取した後の扱いを選びます。確認観点は Parmlib Mgmt、出口確認、運用確認 です。D IPLINFO のIEE254I表示 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. LOADxx管理 の参考情報だけを作業票095へ先に書く。IEE112I とメッセージIDと時刻の対応を別紙扱いにして対象確認を後続者が再現できない形にする。
    - B. Parmlib Management の名称欄だけを作業票095で確定する。表示出力とparmlibとジョブログの差分確認を翌日の口頭確認へ回して採取値の根拠を分離する。
    - C. 前回の正常出力を作業票095の今回値として転記する。システム名とASIDとメンバー名とメッセージIDと時刻差を記録しないため今回の D IPLINFO のIEE254I表示 と IEE112I を照合できない形にする。
    - D. 作業票095では D IPLINFO のIEE254I表示 と IEE112I と時刻を並べる。後続確認で Parmlib Management の今回値を同じ対象として再確認できる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 第九十五観点 採用理由: Dは Parmlib Mgmt の状態を表示値と定義の両方から確認するため、記録として妥当です（第九十五観点）。第九十五観点 背景確認: DISPLAY IPLINFOはIPL日時、LOADxx、IEASYSxx、IEASYMxx、IODF、IPL装置をまとめて示します（第九十五観点）。第九十五観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Cは再現性不足が理由です（第九十五観点）。第九十五観点 用語メモ: GRSは資源直列化です（第九十五観点）。第九十五観点 RNLは資源名リストです（第九十五観点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx


??? note "検証手順（1件）"
    **Parmlib Management 出口確認 運用確認095**

    - 検証目的: Parmlib Management の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS 3.1 の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / system display

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により Parmlib Management の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.05.23 ACTIVE JOBS DISPLAY 614
    JOBNAME  ASID  STATUS
    WLM      000A  ACTIVE
    JES2     0012  ACTIVE
    ```

    画面・出力には IEE114I が含まれる。IEE114I を読み取り、IODF参照値の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により Parmlib Management の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.06.23 DISPLAY M 624
    PROCESSOR STATUS
    CPU 00 ONLINE
    CPU 01 ONLINE
    ```

    画面・出力には IEE174I が含まれる。IEE174I を読み取り、IODF参照値の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により Parmlib Management の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC357I 12.07.23 DISPLAY CF 634
    CFNAME     STATUS
    CF01       ACTIVE
    COUPLING FACILITY ATTACHED
    ```

    画面・出力には IXC357I が含まれる。IXC357I を読み取り、IODF参照値の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE174I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IXC357I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300 / zOS31_ieag100 DISPLAY IPLINFO / zOS31_ieag100 CNZ4100I / zOS31_ieag200 SMFPRMxx / zOS31_ieam600 IEA011A / zOS31_ieah700 wait state LOADxx



### 結合機構確認 Coupling Facility構造 ログとの照合 CF07 {#c37-i0291}
*分類: 結合機構確認*  ・  難易度: 中級

ログとの照合では 結合機構確認 の CF一覧 を主操作として CF07 を判定します。時刻と対象識別子への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF07 に残します。ログとの照合を補助する 構造表示 では IXC360I を補助値として CF07 へ保存します。主判定のログとの照合では結合機構確認・構造の CF一覧 から IXL150I を読み CF07 へ残します。証跡照合のログとの照合では結合機構確認・構造の IXL150I と IXC360I を CF07 に保存します。記録対応のログとの照合では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF07 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** ログとの照合で 結合機構確認 の CF一覧 と 構造表示 を用い 操作とログを対応 します。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。IXL150I で対象 CF07 の STRUCTUREとCONNECTION を再現できる記録はどれですか。

    - A. D CFが応答を返した時点で正常とする。応答中のIXL150Iの値は記録しない。IXC361IをIXL150Iと同じ判定値とみなし対象CF07の主証跡にする。
    - B. D CFのコマンド文字列だけを記録する。IXL150Iを含む応答行は保存しない。
    - C. IXL150Iを含むCF一覧の応答行を保存する。その応答を得るためD CFを使用する。対象CF07のSTRUCTUREとCONNECTIONとして記録する。 ✅
    - D. Coupling Facility構造の停止または再定義を実施する。その後にD CFでIXL150Iを採取する。

    正解: **C** ／ 難易度: 中級

    **解説:** 適切な判定: CはCF一覧で IXL150I を読みSTRUCTUREとCONNECTIONの主値として操作とログを対応しCF07に残します。
    機能の仕組み: ログとの照合では構造表示を補助操作としCoupling Facility構造の時刻と対象識別子をIXC360Iと対象CF07で照合します。
    各候補の評価: CF一覧と構造表示の役割を分けるとA: 応答の有無だけではSTRUCTUREとCONNECTIONを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではSTRUCTUREとCONNECTIONを証明できない点で一次資料と一致しません、C: IXL150Iの実値を対象別に残す点でCF07を判定できます、D: 変更前のSTRUCTUREとCONNECTIONを失う点で構造表示の範囲を越えます。結論としてログとの照合の結合機構確認・構造で判定する対象は CF07 です。
    用語の定義: ログとの照合で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF07へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 ログとの照合 CF07**

    - 検証目的: 結合機構確認のCoupling Facility構造について操作とログを対応し、CF07のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF07のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF07を指定し、CF07の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF07
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF07 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF07のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXL150I が画面・出力に表示されること
    ② ステップ2 の IXC360I が画面・出力に表示されること
    ③ ステップ3 の IXC361I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 代替経路の確認 CF10 {#c37-i0292}
*分類: 結合機構確認*  ・  難易度: 中級

代替経路の確認では 結合機構確認 の CF一覧 を主操作として CF10 を判定します。主経路との役割差への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF10 に残します。代替経路の確認を補助する 構造表示 では IXC360I を補助値として CF10 へ保存します。主判定の代替経路の確認では結合機構確認・構造の CF一覧 から IXL150I を読み CF10 へ残します。証跡照合の代替経路の確認では結合機構確認・構造の IXL150I と IXC360I を CF10 に保存します。記録対応の代替経路の確認では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF10 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 結合機構確認 の CF一覧 と 構造表示 の役割を分け 主経路との役割差 を調べます。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。対象 CF10 を誤判定しない進め方はどれですか。

    - A. D CFのコマンド文字列だけを記録する。IXL150Iを含む応答行は保存しない。
    - B. D CFとD XCF,STR,STRNAME=CF10の対象名をそろえる。前者のIXL150IをSTRUCTUREとCONNECTIONの判定値として採用する。 ✅
    - C. Coupling Facility構造の停止または再定義を実施する。その後にD CFでIXL150Iを採取する。
    - D. 結合機構確認のSTRUCTUREとCONNECTIONを確認する。その値を結合機構確認のCF10にも適用する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい判定結果: BはCF一覧で IXL150I を読みSTRUCTUREとCONNECTIONの主値として代替手段の成立を確認しCF10に残します。
    運用上の背景: 代替経路の確認では構造表示を補助操作としCoupling Facility構造の主経路との役割差をIXC360Iと対象CF10で照合します。
    候補別の検討: CF一覧と構造表示の役割を分けるとA: 入力記録だけではSTRUCTUREとCONNECTIONを証明できない点で一次資料と一致しません、B: 同じ対象名のIXL150Iを採用する点でCF10を判定できます、C: 変更前のSTRUCTUREとCONNECTIONを失う点で構造表示の範囲を越えます、D: 結合機構確認の値ではIXL150Iを確認できない点でCF10の値を示しません。結論として代替経路の確認の結合機構確認・構造で判定する対象は CF10 です。
    重要用語の定義: 代替経路の確認で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF10へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 代替経路の確認 CF10**

    - 検証目的: 結合機構確認のCoupling Facility構造について代替手段の成立を確認し、CF10のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF10のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF10を指定し、CF10の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF10
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF10 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF10のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXL150I が画面・出力に表示されること
    ② ステップ2 の IXC360I が画面・出力に表示されること
    ③ ステップ3 の IXC361I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 変更前の確認 CF02 {#c37-i0293}
*分類: 結合機構確認*  ・  難易度: 中級

変更前の確認では 結合機構確認 の 構造表示 を主操作として CF02 を判定します。変更対象と非対象の境界への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF02 に残します。変更前の確認を補助する CF活動 では IXC361I を補助値として CF02 へ保存します。主判定の変更前の確認では結合機構確認・構造の 構造表示 から IXC360I を読み CF02 へ残します。証跡照合の変更前の確認では結合機構確認・構造の IXC360I と IXC361I を CF02 に保存します。記録対応の変更前の確認では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF02 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 結合機構確認 の 構造表示 と CF活動 を照合し 変更対象と非対象の境界 を確かめます。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。IXC360I を読む前に対象 CF02 へ行う確認はどれですか。

    - A. D XCF,STR,STRNAME=CF02を対象名なしで実行する。一覧の先頭行をCF02の結果として記録する。
    - B. 対象CF02についてD XCF,STR,STRNAME=CF02の応答からIXC360Iを確認する。D XCF,CF,CFNAME=CF01は補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したD XCF,STR,STRNAME=CF02の結果を使う。今回のD XCF,CF,CFNAME=CF01の結果と同一時点の証跡として比較する。
    - D. 保存済みのCF02の出力を再利用する。今回のD XCF,STR,STRNAME=CF02とD XCF,CF,CFNAME=CF01は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 中級

    **解説:** 採用理由: Bは構造表示で IXC360I を読みSTRUCTUREとCONNECTIONの主値として変更前の証跡を保存しCF02に残します。
    動作の背景: 変更前の確認ではCF活動を補助操作としCoupling Facility構造の変更対象と非対象の境界をIXC361Iと対象CF02で照合します。
    各選択肢の検討: 構造表示とCF活動の役割を分けるとA: 先頭行はCF02と確定できない点で変更前の確認に合いません、B: IXC360Iと補助証跡の時刻を合わせる点で構造表示に合います、C: 採取時刻が異なる点で結合機構確認に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でCoupling Facility構造に使えません。結論として変更前の確認の結合機構確認・構造で判定する対象は CF02 です。
    初出用語の定義: 変更前の確認で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF02へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 変更前の確認 CF02**

    - 検証目的: 結合機構確認のCoupling Facility構造について変更前の証跡を保存し、CF02のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF02を指定し、CF02の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF02
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF02 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF02のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF02のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXC360I が画面・出力に表示されること
    ② ステップ2 の IXC361I が画面・出力に表示されること
    ③ ステップ3 の IXL150I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 変更後の確認 CF03 {#c37-i0294}
*分類: 結合機構確認*  ・  難易度: 中級

変更後の確認では 結合機構確認 の CF活動 を主操作として CF03 を判定します。反映値と残存値への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF03 に残します。変更後の確認を補助する CF一覧 では IXL150I を補助値として CF03 へ保存します。主判定の変更後の確認では結合機構確認・構造の CF活動 から IXC361I を読み CF03 へ残します。証跡照合の変更後の確認では結合機構確認・構造の IXC361I と IXL150I を CF03 に保存します。記録対応の変更後の確認では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF03 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 結合機構確認 の CF活動 と CF一覧 を組み合わせる際は Coupling Facility構造 がXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みという仕組みを前提にします。DEGRADED接続を構造全体の停止と取り違える危険があります。IXC361I と STRUCTUREとCONNECTION を対象 CF03 で確認する組合せはどれですか。

    - A. Coupling Facility構造の停止または再定義を実施する。その後にD XCF,CF,CFNAME=CF01でIXC361Iを採取する。
    - B. IEASYMxx管理のSYMBOL名と展開値を確認する。その値を結合機構確認のCF03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - C. D CFで周辺状態を押さえる。その後にD XCF,CF,CFNAME=CF01でIXC361Iを確認して変更結果を検証する。 ✅
    - D. D CFが成功したためD XCF,CF,CFNAME=CF01のIXC361Iも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正答の根拠: CはCF活動で IXC361I を読みSTRUCTUREとCONNECTIONの主値として変更結果を検証しCF03に残します。
    内部の仕組み: 変更後の確認ではCF一覧を補助操作としCoupling Facility構造の反映値と残存値をIXL150Iと対象CF03で照合します。
    誤答を含む比較: CF活動とCF一覧の役割を分けるとA: 変更前のSTRUCTUREとCONNECTIONを失う点でSTRUCTUREとCONNECTIONを確認できません、B: IEASYMxx管理の値ではIXC361Iを確認できないうえに追加前提も不正な点でCF一覧の範囲を越えます、C: 周辺状態の後にIXC361Iを確認する点で現在値を示します、D: 補助操作の成功ではIXC361Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の結合機構確認・構造で判定する対象は CF03 です。
    用語定義: 変更後の確認で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF03へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 変更後の確認 CF03**

    - 検証目的: 結合機構確認のCoupling Facility構造について変更結果を検証し、CF03のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF03のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF03のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF03を指定し、CF03の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF03
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF03 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXC361I が画面・出力に表示されること
    ② ステップ2 の IXL150I が画面・出力に表示されること
    ③ ステップ3 の IXC360I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 引継ぎ記録 CF09 {#c37-i0295}
*分類: 結合機構確認*  ・  難易度: 中級

引継ぎ記録では 結合機構確認 の CF活動 を主操作として CF09 を判定します。次担当者が追跡できる証跡への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF09 に残します。引継ぎ記録を補助する CF一覧 では IXL150I を補助値として CF09 へ保存します。主判定の引継ぎ記録では結合機構確認・構造の CF活動 から IXC361I を読み CF09 へ残します。証跡照合の引継ぎ記録では結合機構確認・構造の IXC361I と IXL150I を CF09 に保存します。記録対応の引継ぎ記録では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF09 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 結合機構確認 の CF活動 と CF一覧 を組み合わせる際は Coupling Facility構造 がXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みという仕組みを前提にします。DEGRADED接続を構造全体の停止と取り違える危険があります。IXC361I と STRUCTUREとCONNECTION を対象 CF09 で確認する組合せはどれですか。

    - A. 対象名CF09を指定してD XCF,CF,CFNAME=CF01を実行する。応答中のIXC361Iと時刻を保存する。D CFで周辺状態を補完する。 ✅
    - B. D CFが成功したためD XCF,CF,CFNAME=CF01のIXC361Iも正常だと推定する。主出力は保存しない。
    - C. D XCF,CF,CFNAME=CF01を対象名なしで実行する。一覧の先頭行をCF09の結果として記録する。
    - D. 前回保存したD XCF,CF,CFNAME=CF01の結果を使う。今回のD CFの結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 中級

    **解説:** 採用操作の理由: AはCF活動で IXC361I を読みSTRUCTUREとCONNECTIONの主値として再現可能な記録を作成しCF09に残します。
    製品内の仕組み: 引継ぎ記録ではCF一覧を補助操作としCoupling Facility構造の次担当者が追跡できる証跡をIXL150Iと対象CF09で照合します。
    選択肢別の説明: CF活動とCF一覧の役割を分けるとA: IXC361Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではIXC361Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はCF09と確定できない点でCF活動を代替しません、D: 採取時刻が異なる点で結合機構確認に使いません。結論として引継ぎ記録の結合機構確認・構造で判定する対象は CF09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF09へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 引継ぎ記録 CF09**

    - 検証目的: 結合機構確認のCoupling Facility構造について再現可能な記録を作成し、CF09のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF09のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF09のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF09を指定し、CF09の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF09
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF09 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXC361I が画面・出力に表示されること
    ② ステップ2 の IXL150I が画面・出力に表示されること
    ③ ステップ3 の IXC360I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 復旧後の確認 CF06 {#c37-i0296}
*分類: 結合機構確認*  ・  難易度: 中級

復旧後の確認では 結合機構確認 の CF活動 を主操作として CF06 を判定します。再発していないことを示す値への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF06 に残します。復旧後の確認を補助する CF一覧 では IXL150I を補助値として CF06 へ保存します。主判定の復旧後の確認では結合機構確認・構造の CF活動 から IXC361I を読み CF06 へ残します。証跡照合の復旧後の確認では結合機構確認・構造の IXC361I と IXL150I を CF06 に保存します。記録対応の復旧後の確認では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF06 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 結合機構確認 の CF活動 と CF一覧 を実施し Coupling Facility構造 の役割を確認します。DEGRADED接続を構造全体の停止と取り違える危険があります。対象 CF06 の証跡を取る方法はどれですか。

    - A. SMF管理のRECORDINGとMEMBERを確認する。その値を結合機構確認のCF06にも適用する。
    - B. D XCF,CF,CFNAME=CF01でIXC361Iを取得してからD XCF,STR,STRNAME=CF06でIXC360Iを照合する。CF06のSTRUCTUREとCONNECTIONを両出力から確定する。 ✅
    - C. D CFが成功したためD XCF,CF,CFNAME=CF01のIXC361Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象CF06へ引き継げるものとする。Coupling Facility構造の再発していないことを示す値は確認済みとして扱う。さらにD XCF,STR,STRNAME=CF06のIXC360IをIXC361Iと同種の値として併記する。
    - D. D XCF,CF,CFNAME=CF01を対象名なしで実行する。一覧の先頭行をCF06の結果として記録する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正答内容: BはCF活動で IXC361I を読みSTRUCTUREとCONNECTIONの主値として復旧後の安定性を確認しCF06に残します。
    構成上の背景: 復旧後の確認ではCF一覧を補助操作としCoupling Facility構造の再発していないことを示す値をIXL150Iと対象CF06で照合します。
    候補ごとの理由: CF活動とCF一覧の役割を分けるとA: SMF管理の値ではIXC361Iを確認できない点でCF一覧の範囲を越えます、B: IXC361IとIXC360Iを順に照合する点で現在値を示します、C: 補助操作の成功ではIXC361Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はCF06と確定できない点でCF活動を代替しません。結論として復旧後の確認の結合機構確認・構造で判定する対象は CF06 です。
    初出用語: 復旧後の確認で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF06へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 復旧後の確認 CF06**

    - 検証目的: 結合機構確認のCoupling Facility構造について復旧後の安定性を確認し、CF06のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF06のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF06のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF06を指定し、CF06の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF06
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF06 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXC361I が画面・出力に表示されること
    ② ステップ2 の IXL150I が画面・出力に表示されること
    ③ ステップ3 の IXC360I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 復旧準備 CF05 {#c37-i0297}
*分類: 結合機構確認*  ・  難易度: 中級

復旧準備では 結合機構確認 の 構造表示 を主操作として CF05 を判定します。再開前に必要な整合性への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF05 に残します。復旧準備を補助する CF活動 では IXC361I を補助値として CF05 へ保存します。主判定の復旧準備では結合機構確認・構造の 構造表示 から IXC360I を読み CF05 へ残します。証跡照合の復旧準備では結合機構確認・構造の IXC360I と IXC361I を CF05 に保存します。記録対応の復旧準備では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF05 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 復旧準備で 結合機構確認 の 構造表示 と CF活動 を使い 復旧条件を確認 します。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。IXC360I を読み対象 CF05 を切り分ける確認方法はどれですか。

    - A. 変更を加えずD XCF,STR,STRNAME=CF05を実行する。IXC360Iを保存する。差分はD XCF,CF,CFNAME=CF01の結果と対象名で対応させる。 ✅
    - B. 前回保存したD XCF,STR,STRNAME=CF05の結果を使う。今回のD XCF,CF,CFNAME=CF01の結果と同一時点の証跡として比較する。
    - C. 保存済みのCF05の出力を再利用する。今回のD XCF,STR,STRNAME=CF05とD XCF,CF,CFNAME=CF01は実行済みとして扱う。
    - D. D XCF,CF,CFNAME=CF01のIXC361IをSTRUCTUREとCONNECTIONの主判定に採用する。D XCF,STR,STRNAME=CF05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 中級

    **解説:** 選定理由: Aは構造表示で IXC360I を読みSTRUCTUREとCONNECTIONの主値として復旧条件を確認しCF05に残します。
    処理の仕組み: 復旧準備ではCF活動を補助操作としCoupling Facility構造の再開前に必要な整合性をIXC361Iと対象CF05で照合します。
    選択結果の内訳: 構造表示とCF活動の役割を分けるとA: 変更前のIXC360Iを保存する点で構造表示に合います、B: 採取時刻が異なる点で結合機構確認に使いません、C: 過去出力では今回の復旧準備を示せない点でCoupling Facility構造に使えません、D: IXC361IはIXC360Iを代替しないうえに追加前提も不正な点でCF05を採用できません。結論として復旧準備の結合機構確認・構造で判定する対象は CF05 です。
    用語の説明: 復旧準備で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF05へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 復旧準備 CF05**

    - 検証目的: 結合機構確認のCoupling Facility構造について復旧条件を確認し、CF05のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF05を指定し、CF05の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF05
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF05 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF05のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF05のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXC360I が画面・出力に表示されること
    ② ステップ2 の IXC361I が画面・出力に表示されること
    ③ ステップ3 の IXL150I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 構成監査 CF08 {#c37-i0298}
*分類: 結合機構確認*  ・  難易度: 中級

構成監査では 結合機構確認 の 構造表示 を主操作として CF08 を判定します。定義値と稼働値の一致への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF08 に残します。構成監査を補助する CF活動 では IXC361I を補助値として CF08 へ保存します。主判定の構成監査では結合機構確認・構造の 構造表示 から IXC360I を読み CF08 へ残します。証跡照合の構成監査では結合機構確認・構造の IXC360I と IXC361I を CF08 に保存します。記録対応の構成監査では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF08 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 構成監査で 結合機構確認 の 構造表示 と CF活動 を照合し 定義値と稼働値の一致 を確かめます。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。IXC360I を読む前に対象 CF08 へ行う確認はどれですか。

    - A. 保存済みのCF08の出力を再利用する。今回のD XCF,STR,STRNAME=CF08とD XCF,CF,CFNAME=CF01は実行済みとして扱う。
    - B. D XCF,CF,CFNAME=CF01のIXC361IをSTRUCTUREとCONNECTIONの主判定に採用する。D XCF,STR,STRNAME=CF08の応答は採取対象から外す。
    - C. D CFのIXL150IをIXC360Iと同義の成功表示として扱う。D XCF,STR,STRNAME=CF08は実行しない。
    - D. D XCF,CF,CFNAME=CF01の結果だけでは確定しない。D XCF,STR,STRNAME=CF08のIXC360Iを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 技術上の正答: Dは構造表示で IXC360I を読みSTRUCTUREとCONNECTIONの主値として構成差分を監査しCF08に残します。
    実行時の背景: 構成監査ではCF活動を補助操作としCoupling Facility構造の定義値と稼働値の一致をIXC361Iと対象CF08で照合します。
    四つの候補の理由: 構造表示とCF活動の役割を分けるとA: 過去出力では今回の構成監査を示せない点で結合機構確認に使いません、B: IXC361IはIXC360Iを代替しない点でCoupling Facility構造に使えません、C: IXL150IとIXC360Iは確認項目が異なる点でCF08を採用できません、D: IXC360Iを主証跡として区別する点で主証跡になります。結論として構成監査の結合機構確認・構造で判定する対象は CF08 です。
    初出語定義: 構成監査で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF08へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 構成監査 CF08**

    - 検証目的: 結合機構確認のCoupling Facility構造について構成差分を監査し、CF08のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF08を指定し、CF08の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF08
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF08 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF08のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF08のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXC360I が画面・出力に表示されること
    ② ステップ2 の IXC361I が画面・出力に表示されること
    ③ ステップ3 の IXL150I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 通常状態の確認 CF01 {#c37-i0299}
*分類: 結合機構確認*  ・  難易度: 中級

通常状態の確認では 結合機構確認 の CF一覧 を主操作として CF01 を判定します。基準値と現在値の差への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF01 に残します。通常状態の確認を補助する 構造表示 では IXC360I を補助値として CF01 へ保存します。主判定の通常状態の確認では結合機構確認・構造の CF一覧 から IXL150I を読み CF01 へ残します。証跡照合の通常状態の確認では結合機構確認・構造の IXL150I と IXC360I を CF01 に保存します。記録対応の通常状態の確認では結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF01 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 結合機構確認 の CF一覧 と 構造表示 を用い 通常状態を確定 します。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。IXL150I で対象 CF01 の STRUCTUREとCONNECTION を再現できる記録はどれですか。

    - A. D CFを先に実行する。対象CF01のIXL150IをSTRUCTUREとCONNECTIONとして記録する。続いてD XCF,STR,STRNAME=CF01で同一対象を照合する。 ✅
    - B. D XCF,STR,STRNAME=CF01のIXC360IをSTRUCTUREとCONNECTIONの主判定に採用する。D CFの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. D XCF,CF,CFNAME=CF01のIXC361IをIXL150Iと同義の成功表示として扱う。D CFは実行しない。
    - D. D CFが応答を返した時点で正常とする。応答中のIXL150Iの値は記録しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正解の説明: AはCF一覧で IXL150I を読みSTRUCTUREとCONNECTIONの主値として通常状態を確定しCF01に残します。
    背景・仕組み: 通常状態の確認では構造表示を補助操作としCoupling Facility構造の基準値と現在値の差をIXC360Iと対象CF01で照合します。
    選択肢の理由: CF一覧と構造表示の役割を分けるとA: IXL150Iを主値として補助結果と照合する点で正答です、B: IXC360IはIXL150Iを代替しないうえに追加前提も不正な点でCF01を採用できません、C: IXC361IとIXL150Iは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではSTRUCTUREとCONNECTIONを判定できない点で一次資料と一致しません。結論として通常状態の確認の結合機構確認・構造で判定する対象は CF01 です。
    用語の初出定義: 通常状態の確認で使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF01へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 通常状態の確認 CF01**

    - 検証目的: 結合機構確認のCoupling Facility構造について通常状態を確定し、CF01のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF01のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF01を指定し、CF01の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF01 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF01のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXL150I が画面・出力に表示されること
    ② ステップ2 の IXC360I が画面・出力に表示されること
    ③ ステップ3 の IXC361I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300



### 結合機構確認 Coupling Facility構造 障害切り分け CF04 {#c37-i0300}
*分類: 結合機構確認*  ・  難易度: 中級

障害切り分けでは 結合機構確認 の CF一覧 を主操作として CF04 を判定します。最初に失敗した処理への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF04 に残します。障害切り分けを補助する 構造表示 では IXC360I を補助値として CF04 へ保存します。主判定の障害切り分けでは結合機構確認・構造の CF一覧 から IXL150I を読み CF04 へ残します。証跡照合の障害切り分けでは結合機構確認・構造の IXL150I と IXC360I を CF04 に保存します。記録対応の障害切り分けでは結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF04 を結びます。

**出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 結合機構確認 の CF一覧 と 構造表示 の役割を分け 最初に失敗した処理 を調べます。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。対象 CF04 を誤判定しない進め方はどれですか。

    - A. D XCF,CF,CFNAME=CF01のIXC361IをIXL150Iと同義の成功表示として扱う。D CFは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D CFが応答を返した時点で正常とする。応答中のIXL150Iの値は記録しない。
    - C. D CFのコマンド文字列だけを記録する。IXL150Iを含む応答行は保存しない。
    - D. D CFの出力でCF04とIXL150Iが同じ応答にあることを確認する。STRUCTUREとCONNECTIONをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい操作の説明: DはCF一覧で IXL150I を読みSTRUCTUREとCONNECTIONの主値として障害範囲を限定しCF04に残します。
    技術的背景: 障害切り分けでは構造表示を補助操作としCoupling Facility構造の最初に失敗した処理をIXC360Iと対象CF04で照合します。
    四択の評価: CF一覧と構造表示の役割を分けるとA: IXC361IとIXL150Iは確認項目が異なるうえに追加前提も不正な点でCF04を採用できません、B: 応答の有無だけではSTRUCTUREとCONNECTIONを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではSTRUCTUREとCONNECTIONを証明できない点で一次資料と一致しません、D: CF04とIXL150Iを同じ応答で結ぶ点でCF04を判定できます。結論として障害切り分けの結合機構確認・構造で判定する対象は CF04 です。
    初出語の意味: 障害切り分けで使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF04へ適用します。

    **出典:** OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


??? note "検証手順（1件）"
    **結合機構確認 Coupling Facility構造 障害切り分け CF04**

    - 検証目的: 結合機構確認のCoupling Facility構造について障害範囲を限定し、CF04のSTRUCTUREとCONNECTIONを実出力で確認する。
    - 前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF04のCF一覧を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D CF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
    ```

    画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF04を指定し、CF04の構造表示を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,STR,STRNAME=CF04
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I STRUCTURE CF04 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
    ```

    画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF04のCF活動を表示します。
    操作（入力）:
    ```text
    z/OS 3.1 Core Operations 操作画面
    COMMAND ===> D XCF,CF,CFNAME=CF01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
    ```

    画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IXL150I が画面・出力に表示されること
    ② ステップ2 の IXC360I が画面・出力に表示されること
    ③ ステップ3 の IXC361I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300


