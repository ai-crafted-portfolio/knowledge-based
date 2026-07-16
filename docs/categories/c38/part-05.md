---
search:
  exclude: true
---

# z/OS System Programming — 詳細 (5/7)

[← z/OS System Programming の概要へ戻る](index.md)


## z/OS System Programming > SVC処理

### SVC割り込み 直列化確認 運用確認076 {#c38-i0193}
*分類: SVC処理*  ・  難易度: 中級

第七十六観点 z/OS System Programming の SVC処理 では SVC割り込み を障害調査で照合します（第七十六観点）。第七十六観点 資料上は 問題プログラムからz/OSサービスを要求し、監視プログラム状態へ制御として扱います（第七十六観点）。第七十六観点 ROUTCDE=ALL を起点に表示値を戻し、オペレーター応答漏れの防止を点検します（第七十六観点）。第七十六観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録076へ書きます（第七十六観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第七十六証跡です。運用確認076 の確認で SVC割り込み を見直します。確認観点は SVC割り込み、直列化確認、運用確認 です。オペレーター応答漏れの防止のために、D TRACE のIEE843I表示 を使った運用記録として最も適切な扱いはどれか。

    - A. LPA管理 の一般メモを採り、ROUTCDE=ALL、メッセージID、時刻の対応を記録外に置き、zOSSP誤記076として調査範囲を狭める。
    - B. SVC割り込み の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延076として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在076として残す。
    - D. D TRACE のIEE843I表示 と ROUTCDE=ALL を同一票へ記録し、SVC割り込み を zOSSP正076で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第七十六観点 照合結果: Dは ROUTCDE=ALL をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第七十六観点）。第七十六観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第七十六観点）。第七十六観点 誤答確認: Aは ROUTCDE=ALL 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第七十六観点）。第七十六観点 用語説明: WTOは通知メッセージです（第七十六観点）。第七十六観点 WTORは応答を求めるメッセージです（第七十六観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SVC割り込み 直列化確認 運用確認076**

    - 検証目的: SVC割り込み の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC割り込み の値を確認し、対象の現在値を固定する。
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

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC割り込み の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC割り込み の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SVC新PSW 直列化確認 運用確認026 {#c38-i0194}
*分類: SVC処理*  ・  難易度: 中級

第二十六観点 SVC新PSW は z/OS System Programming の SVC処理 で扱う管理項目です（第二十六観点）。第二十六観点 SVC割り込み後に使用され、FLIHが制御を受けるためのプログラム状という説明を操作結果と照合します（第二十六観点）。第二十六観点 RNAME=SYS1.PARMLIB、D TRACE のIEE843I表示、定義メンバーを照合し、オペレーター応答漏れの防止を確認します（第二十六観点）。第二十六観点 証跡には資料IDと確認値を併記し、zOSSP記録026として保存します（第二十六観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第二十六証跡です。運用確認026 の確認で SVC新PSW を見直します。確認観点は SVC新PSW、直列化確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。

    - A. ディスパッチ制御 の一般メモを採り、RNAME=SYS1.PARMLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記026として調査範囲を狭める。
    - B. SVC新PSW の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延026として扱う。
    - C. D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を同一票へ記録し、SVC新PSW を zOSSP正026で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在026として残す。

    正解: **C** ／ 難易度: 中級

    **解説:** 第二十六観点 正答根拠: Cは D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を結び付けるため、対象システムの取り違えを防げます（第二十六観点）。第二十六観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第二十六観点）。第二十六観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Dは時刻差の欠落が理由です（第二十六観点）。第二十六観点 用語補足: ENQは資源を直列化します（第二十六観点）。第二十六観点 DEQは取得した資源を解放します（第二十六観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SVC新PSW 直列化確認 運用確認026**

    - 検証目的: SVC新PSW の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC新PSW の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(PROGSP)
    → Enter を押す
    ```

    画面・出力:
    ```text
    APF FORMAT(DYNAMIC)
    APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
    LPA ADD MODNAME(MOD02) DSNAME(SYS1.LPALIB)
    ```

    画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC新PSW の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SET PROG=SP
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
    IEE536I PROG VALUE SP NOW IN EFFECT
    ```

    画面・出力には IEE252I が含まれる。IEE252I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC新PSW の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 06.10.02 PROG,APF DISPLAY 825
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
      12  MPRES3 MYPROG.LOADLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SWITCH SMF 状態確認 運用確認060 {#c38-i0195}
*分類: SVC処理*  ・  難易度: 中級

第六十観点 z/OS System Programming の SVC処理 では SWITCH SMF を障害調査で照合します（第六十観点）。第六十観点 資料上は SMF記録先の切替とバッファ書き出しを行い、ダンプ出口へ制御を渡す操として扱います（第六十観点）。第六十観点 SYS1.PARMLIB(GRSRNLSP) を起点に表示値を戻し、診断ログの再現性確保を点検します（第六十観点）。第六十観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録060へ書きます（第六十観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第六十証跡です。SWITCH SMF の表示とメッセージIDを比べます。確認観点は SWITCH SMF、状態確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. GRS資源直列化 の一般メモを採り、SYS1.PARMLIB(GRSRNLSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記060として調査範囲を狭める。
    - B. SWITCH SMF の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延060として扱う。
    - C. SETPROG APF後のCSV410I表示 と SYS1.PARMLIB(GRSRNLSP) を同一票へ記録し、SWITCH SMF を zOSSP正060で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在060として残す。

    正解: **C** ／ 難易度: 中級

    **解説:** 第六十観点 照合結果: Cは SYS1.PARMLIB(GRSRNLSP) をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第六十観点）。第六十観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第六十観点）。第六十観点 誤答確認: Aは SYS1.PARMLIB(GRSRNLSP) 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第六十観点）。第六十観点 初出定義: PSWは実行状態を示す語です（第六十観点）。第六十観点 SVCは監視プログラム呼出しです（第六十観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SWITCH SMF 状態確認 運用確認060**

    - 検証目的: SWITCH SMF の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SWITCH SMF の値を確認し、対象の現在値を固定する。
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

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SWITCH SMF の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SWITCH SMF の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### VERBX LOGDATA 表示確認 運用確認093 {#c38-i0196}
*分類: SVC処理*  ・  難易度: 上級

第九十三観点 SVC処理 で VERBX LOGDATA は 表示確認 の対象です（第九十三観点）。第九十三観点 確認時には ダンプ内のLOGREC記録を整形し、EREP形式で確認するIPCS処という性質を前提にします（第九十三観点）。第九十三観点 DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同じ証跡に置き、共通ストレージ変更の記録を管理します（第九十三観点）。第九十三観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録093から再現します（第九十三観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第九十三証跡です。zOSSP記録093として TCB=008F21A0 の証跡を残します。確認観点は VERBX LOGDATA、表示確認、運用確認 です。DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を合わせて読む時の採用方針として正しいものはどれか。

    - A. トレース診断 の一般メモを採り、TCB=008F21A0、メッセージID、時刻の対応を記録外に置き、zOSSP誤記093として調査範囲を狭める。
    - B. DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同一票へ記録し、VERBX LOGDATA を zOSSP正093で確定する。 ✅
    - C. VERBX LOGDATA の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延093として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在093として残す。

    正解: **B** ／ 難易度: 上級

    **解説:** 第九十三観点 正解確認: Bは VERBX LOGDATA と TCB=008F21A0 を同じ証跡で扱うため、後続の照合に使えます（第九十三観点）。第九十三観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第九十三観点）。第九十三観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第九十三観点）。第九十三観点 用語整理: SMFはシステム測定記録です（第九十三観点）。第九十三観点 IFASMFDPはSMFデータ退避に使います（第九十三観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **VERBX LOGDATA 表示確認 運用確認093**

    - 検証目的: VERBX LOGDATA の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により VERBX LOGDATA の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.21 DISPLAY R 712
    REPLY ID   MESSAGE TEXT
    005        IEA793A SPECIFY DUMP OPTION FOR TCB=008F21A0
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により VERBX LOGDATA の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.21 CONSOLE DISPLAY 522
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により VERBX LOGDATA の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> R 005,INFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO 005 IS;INFO
    IEA631I OPERATOR OPER21 NOW ACTIVE, SYSTEM=SC65
    ```

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110




## z/OS System Programming > TCB/SRB管理

### D TRACE ログ確認 運用確認094 {#c38-i0197}
*分類: TCB/SRB管理*  ・  難易度: 上級

第九十四観点 D TRACE は z/OS System Programming の TCB/SRB管理 で扱う管理項目です（第九十四観点）。第九十四観点 システムまたはコンポーネントのトレース状態を表示する診断コマンドという説明を操作結果と照合します（第九十四観点）。第九十四観点 SRB=00AF1100、SWITCH SMF後のSMF切替記録、定義メンバーを照合し、資源競合時の保有者確認を確認します（第九十四観点）。第九十四観点 証跡には資料IDと確認値を併記し、zOSSP記録094として保存します（第九十四観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第九十四証跡です。z/OS System Programming の TCB/SRB管理 で切分けを行います。確認観点は D TRACE、ログ確認、運用確認 です。資源競合時の保有者確認のために、SWITCH SMF後のSMF切替記録 を使った運用記録として最も適切な扱いはどれか。

    - A. SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を同一票へ記録し、D TRACE を zOSSP正094で確定する。 ✅
    - B. APF管理 の一般メモを採り、SRB=00AF1100、メッセージID、時刻の対応を記録外に置き、zOSSP誤記094として調査範囲を狭める。
    - C. D TRACE の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延094として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在094として残す。

    正解: **A** ／ 難易度: 上級

    **解説:** 第九十四観点 正答根拠: Aは SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を結び付けるため、対象システムの取り違えを防げます（第九十四観点）。第九十四観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第九十四観点）。第九十四観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第九十四観点）。第九十四観点 用語説明: WTOは通知メッセージです（第九十四観点）。第九十四観点 WTORは応答を求めるメッセージです（第九十四観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **D TRACE ログ確認 運用確認094**

    - 検証目的: D TRACE の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: IPCS / dump analysis

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により D TRACE の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    IPCS option 6
    COMMAND ===> VERBX LOGDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOGDATA VERBEXIT PROCESSING
    LOGREC BUFFER RECORDS LOCATED
    EREP DETAIL EDIT REPORT FOLLOWS
    ```

    画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により D TRACE の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.30.22 TRACE DISPLAY 193
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
    ```

    画面・出力には IEE843I が含まれる。IEE843I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により D TRACE の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    IPCS command line
    COMMAND ===> STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IPCS STATUS CPU
    PSW=070C1000 81234567  ASID=0010
    CURRENT TCB ADDRESS SRB=00AF1100
    ```

    画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### FLIH処理 割り込み確認 運用確認027 {#c38-i0198}
*分類: TCB/SRB管理*  ・  難易度: 中級

第二十七観点 TCB/SRB管理 の運用では FLIH処理 を表示、定義、証跡で確認します（第二十七観点）。第二十七観点 役割は 割り込みを受け、PSWやレジスター状態を保存して適切な処理へ渡す入口という範囲です（第二十七観点）。第二十七観点 IPCS VERBX LOGDATA出力 の値を SMF.MAN1 と合わせ、実行単位の優先順位確認を記録します（第二十七観点）。第二十七観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録027に残します（第二十七観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **FLIH処理 割り込み確認 運用確認027**

    - 検証目的: FLIH処理 の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により FLIH処理 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.03 GRS STATUS 846
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により FLIH処理 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.03 GRS STATUS 856
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により FLIH処理 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.03 DISPLAY XCF 866
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SVC新PSW 割り込み確認 運用確認077 {#c38-i0199}
*分類: TCB/SRB管理*  ・  難易度: 中級

第七十七観点 TCB/SRB管理 で SVC新PSW は 割り込み確認 の対象です（第七十七観点）。第七十七観点 確認時には SVC割り込み後に使用され、FLIHが制御を受けるためのプログラム状という性質を前提にします（第七十七観点）。第七十七観点 IPCS VERBX LOGDATA出力 と AUTH=CMDS を同じ証跡に置き、実行単位の優先順位確認を管理します（第七十七観点）。第七十七観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録077から再現します（第七十七観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **SVC新PSW 割り込み確認 運用確認077**

    - 検証目的: SVC新PSW の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC新PSW の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.05 DISPLAY R 776
    REPLY ID   MESSAGE TEXT
    005        IEA793A SPECIFY DUMP OPTION FOR AUTH=CMDS
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC新PSW の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.05 CONSOLE DISPLAY 506
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC新PSW の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> R 005,INFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO 005 IS;INFO
    IEA631I OPERATOR OPER05 NOW ACTIVE, SYSTEM=SC65
    ```

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### TCB/SRB管理 TCBとSRB ログとの照合 TCB07 {#c38-i0200}
*分類: TCB/SRB管理*  ・  難易度: 上級

ログとの照合では TCB/SRB管理 の TCBサマリー を主操作として TCB07 を判定します。時刻と対象識別子への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB07 に残します。ログとの照合を補助する SRB情報 では SRB を補助値として TCB07 へ保存します。主判定のログとの照合では管理の TCBサマリー から TCB を読み TCB07 へ残します。証跡照合のログとの照合では管理の TCB と SRB を TCB07 に保存します。記録対応のログとの照合では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で TCB/SRB管理 の TCBサマリー と SRB情報 を組み合わせる際は TCBとSRB がタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックという仕組みを前提にします。SRB時間をアプリケーションTCB時間として評価する危険があります。TCB と TCB/SRB ADDRESSとWAIT を対象 TCB07 で確認する組合せはどれですか。

    - A. IP SUMMARY FORMAT ASID(X07)が応答を返した時点で正常とする。応答中のTCBの値は記録しない。CURRENTをTCBと同じ判定値とみなし対象TCB07の主証跡にする。TCBとSRBの時刻と対象識別子は確認済みとして扱う。さらにIP STATUS CPUのCURRENTをTCBと同種の値として併記する。
    - B. IP SUMMARY FORMAT ASID(X07)のコマンド文字列だけを記録する。TCBを含む応答行は保存しない。
    - C. TCBを含むTCBサマリーの応答行を保存する。その応答を得るためIP SUMMARY FORMAT ASID(X07)を使用する。対象TCB07のTCB/SRB ADDRESSとWAITとして記録する。 ✅
    - D. TCBとSRBの停止または再定義を実施する。その後にIP SUMMARY FORMAT ASID(X07)でTCBを採取する。

    正解: **C** ／ 難易度: 上級

    **解説:** 適切な判定: CはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として操作とログを対応しTCB07に残します。
    機能の仕組み: ログとの照合ではSRB情報を補助操作としTCBとSRBの時刻と対象識別子をSRBと対象TCB07で照合します。
    各候補の評価: TCBサマリーとSRB情報の役割を分けるとA: 応答の有無だけではTCB/SRB ADDRESSとWAITを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではTCB/SRB ADDRESSとWAITを証明できない点で一次資料と一致しません、C: TCBの実値を対象別に残す点でTCB07を判定できます、D: 変更前のTCB/SRB ADDRESSとWAITを失う点でSRB情報の範囲を越えます。結論としてログとの照合の管理で判定する対象は TCB07 です。
    用語の定義: ログとの照合で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB ログとの照合 TCB07**

    - 検証目的: TCB/SRB管理のTCBとSRBについて操作とログを対応し、TCB07のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X07)を指定し、TCB07のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X07)を指定し、TCB07のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB07のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0007 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
    ② ステップ2 の AF1100 が画面・出力に表示されること
    ③ ステップ3 の CURRENT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 代替経路の確認 TCB10 {#c38-i0201}
*分類: TCB/SRB管理*  ・  難易度: 上級

代替経路の確認では TCB/SRB管理 の TCBサマリー を主操作として TCB10 を判定します。主経路との役割差への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB10 に残します。代替経路の確認を補助する SRB情報 では SRB を補助値として TCB10 へ保存します。主判定の代替経路の確認では管理の TCBサマリー から TCB を読み TCB10 へ残します。証跡照合の代替経路の確認では管理の TCB と SRB を TCB10 に保存します。記録対応の代替経路の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で TCB/SRB管理 の TCBサマリー と SRB情報 を実施し TCBとSRB の役割を確認します。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB10 の証跡を取る方法はどれですか。

    - A. IP SUMMARY FORMAT ASID(X10)のコマンド文字列だけを記録する。TCBを含む応答行は保存しない。
    - B. IP SUMMARY FORMAT ASID(X10)とIP VERBX SRMDATA ASID(X10)の対象名をそろえる。前者のTCBをTCB/SRB ADDRESSとWAITの判定値として採用する。 ✅
    - C. TCBとSRBの停止または再定義を実施する。その後にIP SUMMARY FORMAT ASID(X10)でTCBを採取する。
    - D. SVC処理のSVC番号とROUTINEを確認する。その値をTCB/SRB管理のTCB10にも適用する。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい判定結果: BはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として代替手段の成立を確認しTCB10に残します。
    運用上の背景: 代替経路の確認ではSRB情報を補助操作としTCBとSRBの主経路との役割差をSRBと対象TCB10で照合します。
    候補別の検討: TCBサマリーとSRB情報の役割を分けるとA: 入力記録だけではTCB/SRB ADDRESSとWAITを証明できない点で一次資料と一致しません、B: 同じ対象名のTCBを採用する点でTCB10を判定できます、C: 変更前のTCB/SRB ADDRESSとWAITを失う点でSRB情報の範囲を越えます、D: SVC処理の値ではTCBを確認できない点でTCB10の値を示しません。結論として代替経路の確認の管理で判定する対象は TCB10 です。
    重要用語の定義: 代替経路の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 代替経路の確認 TCB10**

    - 検証目的: TCB/SRB管理のTCBとSRBについて代替手段の成立を確認し、TCB10のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X10)を指定し、TCB10のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X10)を指定し、TCB10のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB10のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0010 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
    ② ステップ2 の AF1100 が画面・出力に表示されること
    ③ ステップ3 の CURRENT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 変更前の確認 TCB02 {#c38-i0202}
*分類: TCB/SRB管理*  ・  難易度: 上級

変更前の確認では TCB/SRB管理 の SRB情報 を主操作として TCB02 を判定します。変更対象と非対象の境界への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB02 に残します。変更前の確認を補助する CPU状態 では CURRENT を補助値として TCB02 へ保存します。主判定の変更前の確認では管理の SRB情報 から SRB を読み TCB02 へ残します。証跡照合の変更前の確認では管理の SRB と CURRENT を TCB02 に保存します。記録対応の変更前の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で TCB/SRB管理 の SRB情報 と CPU状態 の役割を分け 変更対象と非対象の境界 を調べます。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB02 を誤判定しない進め方はどれですか。

    - A. IP VERBX SRMDATA ASID(X02)を対象名なしで実行する。一覧の先頭行をTCB02の結果として記録する。
    - B. 対象TCB02についてIP VERBX SRMDATA ASID(X02)の応答からSRBを確認する。IP STATUS CPUは補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したIP VERBX SRMDATA ASID(X02)の結果を使う。今回のIP STATUS CPUの結果と同一時点の証跡として比較する。
    - D. 保存済みのTCB02の出力を再利用する。今回のIP VERBX SRMDATA ASID(X02)とIP STATUS CPUは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 上級

    **解説:** 採用理由: BはSRB情報で SRB を読みTCB/SRB ADDRESSとWAITの主値として変更前の証跡を保存しTCB02に残します。
    動作の背景: 変更前の確認ではCPU状態を補助操作としTCBとSRBの変更対象と非対象の境界をCURRENTと対象TCB02で照合します。
    各選択肢の検討: SRB情報とCPU状態の役割を分けるとA: 先頭行はTCB02と確定できない点で変更前の確認に合いません、B: SRBと補助証跡の時刻を合わせる点でSRB情報に合います、C: 採取時刻が異なる点でTCB/SRB管理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でTCBとSRBに使えません。結論として変更前の確認の管理で判定する対象は TCB02 です。
    初出用語の定義: 変更前の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 変更前の確認 TCB02**

    - 検証目的: TCB/SRB管理のTCBとSRBについて変更前の証跡を保存し、TCB02のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X02)を指定し、TCB02のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB02のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0002 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X02)を指定し、TCB02のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の AF1100 が画面・出力に表示されること
    ② ステップ2 の CURRENT が画面・出力に表示されること
    ③ ステップ3 の F21A0 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 変更後の確認 TCB03 {#c38-i0203}
*分類: TCB/SRB管理*  ・  難易度: 上級

変更後の確認では TCB/SRB管理 の CPU状態 を主操作として TCB03 を判定します。反映値と残存値への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB03 に残します。変更後の確認を補助する TCBサマリー では TCB を補助値として TCB03 へ保存します。主判定の変更後の確認では管理の CPU状態 から CURRENT を読み TCB03 へ残します。証跡照合の変更後の確認では管理の CURRENT と TCB を TCB03 に保存します。記録対応の変更後の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で TCB/SRB管理 の CPU状態 と TCBサマリー を使い 変更結果を検証 します。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。CURRENT を読み対象 TCB03 を切り分ける確認方法はどれですか。

    - A. TCBとSRBの停止または再定義を実施する。その後にIP STATUS CPUでCURRENTを採取する。
    - B. LNKLST管理のSET名とDATASET順序を確認する。その値をTCB/SRB管理のTCB03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - C. IP SUMMARY FORMAT ASID(X03)で周辺状態を押さえる。その後にIP STATUS CPUでCURRENTを確認して変更結果を検証する。 ✅
    - D. IP SUMMARY FORMAT ASID(X03)が成功したためIP STATUS CPUのCURRENTも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正答の根拠: CはCPU状態で CURRENT を読みTCB/SRB ADDRESSとWAITの主値として変更結果を検証しTCB03に残します。
    内部の仕組み: 変更後の確認ではTCBサマリーを補助操作としTCBとSRBの反映値と残存値をTCBと対象TCB03で照合します。
    誤答を含む比較: CPU状態とTCBサマリーの役割を分けるとA: 変更前のTCB/SRB ADDRESSとWAITを失う点でTCB/SRB ADDRESSとWAITを確認できません、B: LNKLST管理の値ではCURRENTを確認できないうえに追加前提も不正な点でTCBサマリーの範囲を越えます、C: 周辺状態の後にCURRENTを確認する点で現在値を示します、D: 補助操作の成功ではCURRENTを確定できない点で変更後の確認に合いません。結論として変更後の確認の管理で判定する対象は TCB03 です。
    用語定義: 変更後の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 変更後の確認 TCB03**

    - 検証目的: TCB/SRB管理のTCBとSRBについて変更結果を検証し、TCB03のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB03のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0003 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X03)を指定し、TCB03のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X03)を指定し、TCB03のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CURRENT が画面・出力に表示されること
    ② ステップ2 の F21A0 が画面・出力に表示されること
    ③ ステップ3 の AF1100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 引継ぎ記録 TCB09 {#c38-i0204}
*分類: TCB/SRB管理*  ・  難易度: 上級

引継ぎ記録では TCB/SRB管理 の CPU状態 を主操作として TCB09 を判定します。次担当者が追跡できる証跡への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB09 に残します。引継ぎ記録を補助する TCBサマリー では TCB を補助値として TCB09 へ保存します。主判定の引継ぎ記録では管理の CPU状態 から CURRENT を読み TCB09 へ残します。証跡照合の引継ぎ記録では管理の CURRENT と TCB を TCB09 に保存します。記録対応の引継ぎ記録では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で TCB/SRB管理 の CPU状態 と TCBサマリー を使い 再現可能な記録を作成 します。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。CURRENT を読み対象 TCB09 を切り分ける確認方法はどれですか。

    - A. 対象名TCB09を指定してIP STATUS CPUを実行する。応答中のCURRENTと時刻を保存する。IP SUMMARY FORMAT ASID(X09)で周辺状態を補完する。 ✅
    - B. IP SUMMARY FORMAT ASID(X09)が成功したためIP STATUS CPUのCURRENTも正常だと推定する。主出力は保存しない。
    - C. IP STATUS CPUを対象名なしで実行する。一覧の先頭行をTCB09の結果として記録する。
    - D. 前回保存したIP STATUS CPUの結果を使う。今回のIP SUMMARY FORMAT ASID(X09)の結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 上級

    **解説:** 採用操作の理由: AはCPU状態で CURRENT を読みTCB/SRB ADDRESSとWAITの主値として再現可能な記録を作成しTCB09に残します。
    製品内の仕組み: 引継ぎ記録ではTCBサマリーを補助操作としTCBとSRBの次担当者が追跡できる証跡をTCBと対象TCB09で照合します。
    選択肢別の説明: CPU状態とTCBサマリーの役割を分けるとA: CURRENTと時刻を保存する点で現在値を示します、B: 補助操作の成功ではCURRENTを確定できない点で引継ぎ記録に合いません、C: 先頭行はTCB09と確定できない点でCPU状態を代替しません、D: 採取時刻が異なる点でTCB/SRB管理に使いません。結論として引継ぎ記録の管理で判定する対象は TCB09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 引継ぎ記録 TCB09**

    - 検証目的: TCB/SRB管理のTCBとSRBについて再現可能な記録を作成し、TCB09のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB09のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0009 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X09)を指定し、TCB09のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X09)を指定し、TCB09のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CURRENT が画面・出力に表示されること
    ② ステップ2 の F21A0 が画面・出力に表示されること
    ③ ステップ3 の AF1100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 復旧後の確認 TCB06 {#c38-i0205}
*分類: TCB/SRB管理*  ・  難易度: 上級

復旧後の確認では TCB/SRB管理 の CPU状態 を主操作として TCB06 を判定します。再発していないことを示す値への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB06 に残します。復旧後の確認を補助する TCBサマリー では TCB を補助値として TCB06 へ保存します。主判定の復旧後の確認では管理の CPU状態 から CURRENT を読み TCB06 へ残します。証跡照合の復旧後の確認では管理の CURRENT と TCB を TCB06 に保存します。記録対応の復旧後の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で TCB/SRB管理 の CPU状態 と TCBサマリー を照合し 再発していないことを示す値 を確かめます。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。CURRENT を読む前に対象 TCB06 へ行う確認はどれですか。

    - A. GRS資源直列化のSYSTEMとMODEを確認する。その値をTCB/SRB管理のTCB06にも適用する。
    - B. IP STATUS CPUでCURRENTを取得してからIP VERBX SRMDATA ASID(X06)でSRBを照合する。TCB06のTCB/SRB ADDRESSとWAITを両出力から確定する。 ✅
    - C. IP SUMMARY FORMAT ASID(X06)が成功したためIP STATUS CPUのCURRENTも正常だと推定する。主出力は保存しない。別資源で得た状態を対象TCB06へ引き継げるものとする。
    - D. IP STATUS CPUを対象名なしで実行する。一覧の先頭行をTCB06の結果として記録する。

    正解: **B** ／ 難易度: 上級

    **解説:** 正答内容: BはCPU状態で CURRENT を読みTCB/SRB ADDRESSとWAITの主値として復旧後の安定性を確認しTCB06に残します。
    構成上の背景: 復旧後の確認ではTCBサマリーを補助操作としTCBとSRBの再発していないことを示す値をTCBと対象TCB06で照合します。
    候補ごとの理由: CPU状態とTCBサマリーの役割を分けるとA: GRS資源直列化の値ではCURRENTを確認できない点でTCBサマリーの範囲を越えます、B: CURRENTとSRBを順に照合する点で現在値を示します、C: 補助操作の成功ではCURRENTを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はTCB06と確定できない点でCPU状態を代替しません。結論として復旧後の確認の管理で判定する対象は TCB06 です。
    初出用語: 復旧後の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 復旧後の確認 TCB06**

    - 検証目的: TCB/SRB管理のTCBとSRBについて復旧後の安定性を確認し、TCB06のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB06のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0006 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X06)を指定し、TCB06のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X06)を指定し、TCB06のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CURRENT が画面・出力に表示されること
    ② ステップ2 の F21A0 が画面・出力に表示されること
    ③ ステップ3 の AF1100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 復旧準備 TCB05 {#c38-i0206}
*分類: TCB/SRB管理*  ・  難易度: 上級

復旧準備では TCB/SRB管理 の SRB情報 を主操作として TCB05 を判定します。再開前に必要な整合性への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB05 に残します。復旧準備を補助する CPU状態 では CURRENT を補助値として TCB05 へ保存します。主判定の復旧準備では管理の SRB情報 から SRB を読み TCB05 へ残します。証跡照合の復旧準備では管理の SRB と CURRENT を TCB05 に保存します。記録対応の復旧準備では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で TCB/SRB管理 の SRB情報 と CPU状態 を用い 復旧条件を確認 します。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。SRB で対象 TCB05 の TCB/SRB ADDRESSとWAIT を再現できる記録はどれですか。

    - A. 変更を加えずIP VERBX SRMDATA ASID(X05)を実行する。SRBを保存する。差分はIP STATUS CPUの結果と対象名で対応させる。 ✅
    - B. 前回保存したIP VERBX SRMDATA ASID(X05)の結果を使う。今回のIP STATUS CPUの結果と同一時点の証跡として比較する。
    - C. 保存済みのTCB05の出力を再利用する。今回のIP VERBX SRMDATA ASID(X05)とIP STATUS CPUは実行済みとして扱う。
    - D. IP STATUS CPUのCURRENTをTCB/SRB ADDRESSとWAITの主判定に採用する。IP VERBX SRMDATA ASID(X05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 上級

    **解説:** 選定理由: AはSRB情報で SRB を読みTCB/SRB ADDRESSとWAITの主値として復旧条件を確認しTCB05に残します。
    処理の仕組み: 復旧準備ではCPU状態を補助操作としTCBとSRBの再開前に必要な整合性をCURRENTと対象TCB05で照合します。
    選択結果の内訳: SRB情報とCPU状態の役割を分けるとA: 変更前のSRBを保存する点でSRB情報に合います、B: 採取時刻が異なる点でTCB/SRB管理に使いません、C: 過去出力では今回の復旧準備を示せない点でTCBとSRBに使えません、D: CURRENTはSRBを代替しないうえに追加前提も不正な点でTCB05を採用できません。結論として復旧準備の管理で判定する対象は TCB05 です。
    用語の説明: 復旧準備で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 復旧準備 TCB05**

    - 検証目的: TCB/SRB管理のTCBとSRBについて復旧条件を確認し、TCB05のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X05)を指定し、TCB05のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB05のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0005 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X05)を指定し、TCB05のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の AF1100 が画面・出力に表示されること
    ② ステップ2 の CURRENT が画面・出力に表示されること
    ③ ステップ3 の F21A0 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 構成監査 TCB08 {#c38-i0207}
*分類: TCB/SRB管理*  ・  難易度: 上級

構成監査では TCB/SRB管理 の SRB情報 を主操作として TCB08 を判定します。定義値と稼働値の一致への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB08 に残します。構成監査を補助する CPU状態 では CURRENT を補助値として TCB08 へ保存します。主判定の構成監査では管理の SRB情報 から SRB を読み TCB08 へ残します。証跡照合の構成監査では管理の SRB と CURRENT を TCB08 に保存します。記録対応の構成監査では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で TCB/SRB管理 の SRB情報 と CPU状態 の役割を分け 定義値と稼働値の一致 を調べます。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB08 を誤判定しない進め方はどれですか。

    - A. 保存済みのTCB08の出力を再利用する。今回のIP VERBX SRMDATA ASID(X08)とIP STATUS CPUは実行済みとして扱う。
    - B. IP STATUS CPUのCURRENTをTCB/SRB ADDRESSとWAITの主判定に採用する。IP VERBX SRMDATA ASID(X08)の応答は採取対象から外す。
    - C. IP SUMMARY FORMAT ASID(X08)のTCBをSRBと同義の成功表示として扱う。IP VERBX SRMDATA ASID(X08)は実行しない。
    - D. IP STATUS CPUの結果だけでは確定しない。IP VERBX SRMDATA ASID(X08)のSRBを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 技術上の正答: DはSRB情報で SRB を読みTCB/SRB ADDRESSとWAITの主値として構成差分を監査しTCB08に残します。
    実行時の背景: 構成監査ではCPU状態を補助操作としTCBとSRBの定義値と稼働値の一致をCURRENTと対象TCB08で照合します。
    四つの候補の理由: SRB情報とCPU状態の役割を分けるとA: 過去出力では今回の構成監査を示せない点でTCB/SRB管理に使いません、B: CURRENTはSRBを代替しない点でTCBとSRBに使えません、C: TCBとSRBは確認項目が異なる点でTCB08を採用できません、D: SRBを主証跡として区別する点で主証跡になります。結論として構成監査の管理で判定する対象は TCB08 です。
    初出語定義: 構成監査で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 構成監査 TCB08**

    - 検証目的: TCB/SRB管理のTCBとSRBについて構成差分を監査し、TCB08のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X08)を指定し、TCB08のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB08のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0008 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X08)を指定し、TCB08のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の AF1100 が画面・出力に表示されること
    ② ステップ2 の CURRENT が画面・出力に表示されること
    ③ ステップ3 の F21A0 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 通常状態の確認 TCB01 {#c38-i0208}
*分類: TCB/SRB管理*  ・  難易度: 上級

通常状態の確認では TCB/SRB管理 の TCBサマリー を主操作として TCB01 を判定します。基準値と現在値の差への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB01 に残します。通常状態の確認を補助する SRB情報 では SRB を補助値として TCB01 へ保存します。主判定の通常状態の確認では管理の TCBサマリー から TCB を読み TCB01 へ残します。証跡照合の通常状態の確認では管理の TCB と SRB を TCB01 に保存します。記録対応の通常状態の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で TCB/SRB管理 の TCBサマリー と SRB情報 を組み合わせる際は TCBとSRB がタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックという仕組みを前提にします。SRB時間をアプリケーションTCB時間として評価する危険があります。TCB と TCB/SRB ADDRESSとWAIT を対象 TCB01 で確認する組合せはどれですか。

    - A. IP SUMMARY FORMAT ASID(X01)を先に実行する。対象TCB01のTCBをTCB/SRB ADDRESSとWAITとして記録する。続いてIP VERBX SRMDATA ASID(X01)で同一対象を照合する。 ✅
    - B. IP VERBX SRMDATA ASID(X01)のSRBをTCB/SRB ADDRESSとWAITの主判定に採用する。IP SUMMARY FORMAT ASID(X01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. IP STATUS CPUのCURRENTをTCBと同義の成功表示として扱う。IP SUMMARY FORMAT ASID(X01)は実行しない。
    - D. IP SUMMARY FORMAT ASID(X01)が応答を返した時点で正常とする。応答中のTCBの値は記録しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解の説明: AはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として通常状態を確定しTCB01に残します。
    背景・仕組み: 通常状態の確認ではSRB情報を補助操作としTCBとSRBの基準値と現在値の差をSRBと対象TCB01で照合します。
    選択肢の理由: TCBサマリーとSRB情報の役割を分けるとA: TCBを主値として補助結果と照合する点で正答です、B: SRBはTCBを代替しないうえに追加前提も不正な点でTCB01を採用できません、C: CURRENTとTCBは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではTCB/SRB ADDRESSとWAITを判定できない点で一次資料と一致しません。結論として通常状態の確認の管理で判定する対象は TCB01 です。
    用語の初出定義: 通常状態の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 通常状態の確認 TCB01**

    - 検証目的: TCB/SRB管理のTCBとSRBについて通常状態を確定し、TCB01のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X01)を指定し、TCB01のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X01)を指定し、TCB01のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB01のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0001 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
    ② ステップ2 の AF1100 が画面・出力に表示されること
    ③ ステップ3 の CURRENT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### TCB/SRB管理 TCBとSRB 障害切り分け TCB04 {#c38-i0209}
*分類: TCB/SRB管理*  ・  難易度: 上級

障害切り分けでは TCB/SRB管理 の TCBサマリー を主操作として TCB04 を判定します。最初に失敗した処理への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB04 に残します。障害切り分けを補助する SRB情報 では SRB を補助値として TCB04 へ保存します。主判定の障害切り分けでは管理の TCBサマリー から TCB を読み TCB04 へ残します。証跡照合の障害切り分けでは管理の TCB と SRB を TCB04 に保存します。記録対応の障害切り分けでは管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで TCB/SRB管理 の TCBサマリー と SRB情報 を実施し TCBとSRB の役割を確認します。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB04 の証跡を取る方法はどれですか。

    - A. IP STATUS CPUのCURRENTをTCBと同義の成功表示として扱う。IP SUMMARY FORMAT ASID(X04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. IP SUMMARY FORMAT ASID(X04)が応答を返した時点で正常とする。応答中のTCBの値は記録しない。
    - C. IP SUMMARY FORMAT ASID(X04)のコマンド文字列だけを記録する。TCBを含む応答行は保存しない。
    - D. IP SUMMARY FORMAT ASID(X04)の出力でTCB04とTCBが同じ応答にあることを確認する。TCB/SRB ADDRESSとWAITをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正しい操作の説明: DはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として障害範囲を限定しTCB04に残します。
    技術的背景: 障害切り分けではSRB情報を補助操作としTCBとSRBの最初に失敗した処理をSRBと対象TCB04で照合します。
    四択の評価: TCBサマリーとSRB情報の役割を分けるとA: CURRENTとTCBは確認項目が異なるうえに追加前提も不正な点でTCB04を採用できません、B: 応答の有無だけではTCB/SRB ADDRESSとWAITを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではTCB/SRB ADDRESSとWAITを証明できない点で一次資料と一致しません、D: TCB04とTCBを同じ応答で結ぶ点でTCB04を判定できます。結論として障害切り分けの管理で判定する対象は TCB04 です。
    初出語の意味: 障害切り分けで使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **TCB/SRB管理 TCBとSRB 障害切り分け TCB04**

    - 検証目的: TCB/SRB管理のTCBとSRBについて障害範囲を限定し、TCB04のTCB/SRB ADDRESSとWAITを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TCB04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X04)を指定し、TCB04のTCBサマリーを表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SUMMARY FORMAT ASID(X04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
    ```

    画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X04)を指定し、TCB04のSRB情報を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP VERBX SRMDATA ASID(X04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
    ```

    画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB04のCPU状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    CPU 0000 CURRENT ASID 0004 TCB 008F21A0 PSW 078D1000
    ```

    画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
    ② ステップ2 の AF1100 が画面・出力に表示されること
    ③ ステップ3 の CURRENT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### コンポーネントトレース ログ確認 運用確認044 {#c38-i0210}
*分類: TCB/SRB管理*  ・  難易度: 中級

第四十四観点 z/OS System Programming の TCB/SRB管理 では コンポーネントトレース を障害調査で照合します（第四十四観点）。第四十四観点 資料上は 指定コンポーネントの内部事象を記録し、障害調査に使うトレース機構として扱います（第四十四観点）。第四十四観点 ISGLOCK を起点に表示値を戻し、資源競合時の保有者確認を点検します（第四十四観点）。第四十四観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録044へ書きます（第四十四観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十四証跡です。z/OS System Programming の TCB/SRB管理 で切分けを行います。確認観点は TRACE、ログ確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。

    - A. SVC処理 の一般メモを採り、ISGLOCK、メッセージID、時刻の対応を記録外に置き、zOSSP誤記044として調査範囲を狭める。
    - B. SWITCH SMF後のSMF切替記録 と ISGLOCK を同一票へ記録し、TRACE を zOSSP正044で確定する。 ✅
    - C. コンポーネントトレース の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延044として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在044として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第四十四観点 照合結果: Bは ISGLOCK をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第四十四観点）。第四十四観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第四十四観点）。第四十四観点 誤答確認: Aは ISGLOCK 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第四十四観点）。第四十四観点 用語補足: ENQは資源を直列化します（第四十四観点）。第四十四観点 DEQは取得した資源を解放します（第四十四観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **コンポーネントトレース ログ確認 運用確認044**

    - 検証目的: コンポーネントトレース の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により コンポーネントトレース の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.20 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により コンポーネントトレース の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により コンポーネントトレース の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD20
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD20 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110




## z/OS System Programming > WTOR応答管理

### LOGRECバッファ 権限確認 運用確認092 {#c38-i0211}
*分類: WTOR応答管理*  ・  難易度: 上級

第九十二観点 z/OS System Programming の WTOR応答管理 では LOGRECバッファ を障害調査で照合します（第九十二観点）。第九十二観点 資料上は エラー記録を保持し、IPCSやEREPの診断対象になる記録領域として扱います（第九十二観点）。第九十二観点 ASID=0010 を起点に表示値を戻し、許可ライブラリーの誤登録防止を点検します（第九十二観点）。第九十二観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録092へ書きます（第九十二観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第九十二証跡です。LOGRECバッファ に関する設定変更を扱います。確認観点は LOGRECバッファ、権限確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。

    - A. LOGREC診断 の一般メモを採り、ASID=0010、メッセージID、時刻の対応を記録外に置き、zOSSP誤記092として調査範囲を狭める。
    - B. DISPLAY GRS のISG343I表示 と ASID=0010 を同一票へ記録し、LOGRECバッファ を zOSSP正092で確定する。 ✅
    - C. LOGRECバッファ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延092として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在092として残す。

    正解: **B** ／ 難易度: 上級

    **解説:** 第九十二観点 照合結果: Bは ASID=0010 をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第九十二観点）。第九十二観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第九十二観点）。第九十二観点 誤答確認: Aは ASID=0010 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第九十二観点）。第九十二観点 用語補足: ENQは資源を直列化します（第九十二観点）。第九十二観点 DEQは取得した資源を解放します（第九十二観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **LOGRECバッファ 権限確認 運用確認092**

    - 検証目的: LOGRECバッファ の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LOGRECバッファ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.20 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LOGRECバッファ の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LOGRECバッファ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD20
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD20 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SMFPRMxx 優先順位確認 運用確認059 {#c38-i0212}
*分類: WTOR応答管理*  ・  難易度: 中級

第五十九観点 WTOR応答管理 の運用では SMFPRMxx を表示、定義、証跡で確認します（第五十九観点）。第五十九観点 役割は SMF記録対象、バッファ、データセット、ログストリーム動作を定義するという範囲です（第五十九観点）。第五十九観点 D PROG,APF のCSV450I表示 の値を SYS1.PARMLIB(SMFSP) と合わせ、実行単位の優先順位確認を記録します（第五十九観点）。第五十九観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録059に残します（第五十九観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **SMFPRMxx 優先順位確認 運用確認059**

    - 検証目的: SMFPRMxx の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SMFPRMxx の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.11 GRS STATUS 878
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SMFPRMxx の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.11 GRS STATUS 888
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SMFPRMxx の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.11 DISPLAY XCF 898
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SWITCH SMF 優先順位確認 運用確認009 {#c38-i0213}
*分類: WTOR応答管理*  ・  難易度: 初級

第九観点 WTOR応答管理 で SWITCH SMF は 優先順位確認 の対象です（第九観点）。第九観点 確認時には SMF記録先の切替とバッファ書き出しを行い、ダンプ出口へ制御を渡す操という性質を前提にします（第九観点）。第九観点 D PROG,APF のCSV450I表示 と DUMPIN を同じ証跡に置き、実行単位の優先順位確認を管理します（第九観点）。第九観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録009から再現します（第九観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **SWITCH SMF 優先順位確認 運用確認009**

    - 検証目的: SWITCH SMF の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SDSF LOG

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SWITCH SMF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.18.09 PROG,APF DISPLAY 908
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       2  MPRES1 SYS1.SVCLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SWITCH SMF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
    ```

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SWITCH SMF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF,ENTRY=(1-5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.26.09 PROG,APF DISPLAY 958
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       5  MPRES1 ISF.SISFLPA
    ```

    画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### VERBX LOGDATA 権限確認 運用確認042 {#c38-i0214}
*分類: WTOR応答管理*  ・  難易度: 中級

第四十二観点 VERBX LOGDATA は z/OS System Programming の WTOR応答管理 で扱う管理項目です（第四十二観点）。第四十二観点 ダンプ内のLOGREC記録を整形し、EREP形式で確認するIPCS処という説明を操作結果と照合します（第四十二観点）。第四十二観点 SYS1.SVCLIB、DISPLAY GRS のISG343I表示、定義メンバーを照合し、許可ライブラリーの誤登録防止を確認します（第四十二観点）。第四十二観点 証跡には資料IDと確認値を併記し、zOSSP記録042として保存します（第四十二観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十二証跡です。VERBX LOGDATA に関する設定変更を扱います。確認観点は VERBX LOGDATA、権限確認、運用確認 です。許可ライブラリーの誤登録防止を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. WTOメッセージ の一般メモを採り、SYS1.SVCLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記042として調査範囲を狭める。
    - B. VERBX LOGDATA の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延042として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在042として残す。
    - D. DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を同一票へ記録し、VERBX LOGDATA を zOSSP正042で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第四十二観点 正答根拠: Dは DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を結び付けるため、対象システムの取り違えを防げます（第四十二観点）。第四十二観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第四十二観点）。第四十二観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第四十二観点）。第四十二観点 初出定義: PSWは実行状態を示す語です（第四十二観点）。第四十二観点 SVCは監視プログラム呼出しです（第四十二観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **VERBX LOGDATA 権限確認 運用確認042**

    - 検証目的: VERBX LOGDATA の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により VERBX LOGDATA の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(PROGSP)
    → Enter を押す
    ```

    画面・出力:
    ```text
    APF FORMAT(DYNAMIC)
    APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
    LPA ADD MODNAME(MOD18) DSNAME(SYS1.LPALIB)
    ```

    画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により VERBX LOGDATA の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SET PROG=SP
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
    IEE536I PROG VALUE SP NOW IN EFFECT
    ```

    画面・出力には IEE252I が含まれる。IEE252I を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により VERBX LOGDATA の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 06.10.18 PROG,APF DISPLAY 841
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
      12  MPRES3 MYPROG.LOADLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### WTOR応答管理 未応答WTOR ログとの照合 WTOR07 {#c38-i0215}
*分類: WTOR応答管理*  ・  難易度: 中級

ログとの照合では WTOR応答管理 の 未応答一覧 を主操作として WTOR07 を判定します。時刻と対象識別子への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR07 に残します。ログとの照合を補助する 発行元確認 では IEE115I を補助値として WTOR07 へ保存します。主判定のログとの照合では応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR07 へ残します。証跡照合のログとの照合では応答管理・未応答の IEE112I と IEE115I を WTOR07 に保存します。記録対応のログとの照合では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で WTOR応答管理 の 未応答一覧 と 発行元確認 を組み合わせる際は 未応答WTOR が応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能という仕組みを前提にします。別WTORへ応答すると停止や再試行の対象を誤ります。IEE112I と REPLY IDと発行ジョブ を対象 WTOR07 で確認する組合せはどれですか。

    - A. IEE112Iを含む未応答一覧の応答行を保存する。その応答を得るためD R,Lを使用する。対象WTOR07のREPLY IDと発行ジョブとして記録する。 ✅
    - B. D R,Lが応答を返した時点で正常とする。応答中のIEE112Iの値は記録しない。IEE600IをIEE112Iと同じ判定値とみなし対象WTOR07の主証跡にする。
    - C. D R,Lのコマンド文字列だけを記録する。IEE112Iを含む応答行は保存しない。
    - D. 未応答WTORの停止または再定義を実施する。その後にD R,LでIEE112Iを採取する。

    正解: **A** ／ 難易度: 中級

    **解説:** 適切な判定: Aは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として操作とログを対応しWTOR07に残します。
    機能の仕組み: ログとの照合では発行元確認を補助操作とし未応答WTORの時刻と対象識別子をIEE115Iと対象WTOR07で照合します。
    各候補の評価: 未応答一覧と発行元確認の役割を分けるとA: IEE112Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではREPLY IDと発行ジョブを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではREPLY IDと発行ジョブを証明できない点でREPLY IDと発行ジョブを確認できません、D: 変更前のREPLY IDと発行ジョブを失う点で発行元確認の範囲を越えます。結論としてログとの照合の応答管理・未応答で判定する対象は WTOR07 です。
    用語の定義: ログとの照合で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR ログとの照合 WTOR07**

    - 検証目的: WTOR応答管理の未応答WTORについて操作とログを対応し、WTOR07のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR07の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB07,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB07を指定し、WTOR07の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB07 ACTIVE ON SYSA ASID=0007
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR07の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
    ② ステップ2 の IEE115I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 代替経路の確認 WTOR10 {#c38-i0216}
*分類: WTOR応答管理*  ・  難易度: 中級

代替経路の確認では WTOR応答管理 の 未応答一覧 を主操作として WTOR10 を判定します。主経路との役割差への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR10 に残します。代替経路の確認を補助する 発行元確認 では IEE115I を補助値として WTOR10 へ保存します。主判定の代替経路の確認では応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR10 へ残します。証跡照合の代替経路の確認では応答管理・未応答の IEE112I と IEE115I を WTOR10 に保存します。記録対応の代替経路の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で WTOR応答管理 の 未応答一覧 と 発行元確認 を実施し 未応答WTOR の役割を確認します。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR10 の証跡を取る方法はどれですか。

    - A. D R,Lのコマンド文字列だけを記録する。IEE112Iを含む応答行は保存しない。
    - B. 未応答WTORの停止または再定義を実施する。その後にD R,LでIEE112Iを採取する。
    - C. APF管理のDSNAMEとVOLSERを確認する。その値をWTOR応答管理のWTOR10にも適用する。
    - D. D R,LとD A,JOB10の対象名をそろえる。前者のIEE112IをREPLY IDと発行ジョブの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい判定結果: Dは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として代替手段の成立を確認しWTOR10に残します。
    運用上の背景: 代替経路の確認では発行元確認を補助操作とし未応答WTORの主経路との役割差をIEE115Iと対象WTOR10で照合します。
    候補別の検討: 未応答一覧と発行元確認の役割を分けるとA: 入力記録だけではREPLY IDと発行ジョブを証明できない点で一次資料と一致しません、B: 変更前のREPLY IDと発行ジョブを失う点でREPLY IDと発行ジョブを確認できません、C: APF管理の値ではIEE112Iを確認できない点で発行元確認の範囲を越えます、D: 同じ対象名のIEE112Iを採用する点で現在値を示します。結論として代替経路の確認の応答管理・未応答で判定する対象は WTOR10 です。
    重要用語の定義: 代替経路の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 代替経路の確認 WTOR10**

    - 検証目的: WTOR応答管理の未応答WTORについて代替手段の成立を確認し、WTOR10のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR10の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB10,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB10を指定し、WTOR10の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB10 ACTIVE ON SYSA ASID=0010
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR10の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
    ② ステップ2 の IEE115I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 変更前の確認 WTOR02 {#c38-i0217}
*分類: WTOR応答管理*  ・  難易度: 中級

変更前の確認では WTOR応答管理 の 発行元確認 を主操作として WTOR02 を判定します。変更対象と非対象の境界への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR02 に残します。変更前の確認を補助する 応答記録 では IEE600I を補助値として WTOR02 へ保存します。主判定の変更前の確認では応答管理・未応答の 発行元確認 から IEE115I を読み WTOR02 へ残します。証跡照合の変更前の確認では応答管理・未応答の IEE115I と IEE600I を WTOR02 に保存します。記録対応の変更前の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で WTOR応答管理 の 発行元確認 と 応答記録 の役割を分け 変更対象と非対象の境界 を調べます。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR02 を誤判定しない進め方はどれですか。

    - A. D A,JOB02を対象名なしで実行する。一覧の先頭行をWTOR02の結果として記録する。
    - B. 前回保存したD A,JOB02の結果を使う。今回のSDSF LOG FIND REPLYの結果と同一時点の証跡として比較する。
    - C. 保存済みのWTOR02の出力を再利用する。今回のD A,JOB02とSDSF LOG FIND REPLYは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象WTOR02についてD A,JOB02の応答からIEE115Iを確認する。SDSF LOG FIND REPLYは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 採用理由: Dは発行元確認で IEE115I を読みREPLY IDと発行ジョブの主値として変更前の証跡を保存しWTOR02に残します。
    動作の背景: 変更前の確認では応答記録を補助操作とし未応答WTORの変更対象と非対象の境界をIEE600Iと対象WTOR02で照合します。
    各選択肢の検討: 発行元確認と応答記録の役割を分けるとA: 先頭行はWTOR02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で発行元確認を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でWTOR応答管理に使いません、D: IEE115Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の応答管理・未応答で判定する対象は WTOR02 です。
    初出用語の定義: 変更前の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 変更前の確認 WTOR02**

    - 検証目的: WTOR応答管理の未応答WTORについて変更前の証跡を保存し、WTOR02のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB02を指定し、WTOR02の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB02 ACTIVE ON SYSA ASID=0002
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR02の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR02の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB02,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE115I が画面・出力に表示されること
    ② ステップ2 の IEE600I が画面・出力に表示されること
    ③ ステップ3 の IEE112I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 変更後の確認 WTOR03 {#c38-i0218}
*分類: WTOR応答管理*  ・  難易度: 中級

変更後の確認では WTOR応答管理 の 応答記録 を主操作として WTOR03 を判定します。反映値と残存値への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR03 に残します。変更後の確認を補助する 未応答一覧 では IEE112I を補助値として WTOR03 へ保存します。主判定の変更後の確認では応答管理・未応答の 応答記録 から IEE600I を読み WTOR03 へ残します。証跡照合の変更後の確認では応答管理・未応答の IEE600I と IEE112I を WTOR03 に保存します。記録対応の変更後の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で WTOR応答管理 の 応答記録 と 未応答一覧 を使い 変更結果を検証 します。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE600I を読み対象 WTOR03 を切り分ける確認方法はどれですか。

    - A. D R,Lで周辺状態を押さえる。その後にSDSF LOG FIND REPLYでIEE600Iを確認して変更結果を検証する。 ✅
    - B. 未応答WTORの停止または再定義を実施する。その後にSDSF LOG FIND REPLYでIEE600Iを採取する。
    - C. SAF連携のSAF RCとRACF RCを確認する。その値をWTOR応答管理のWTOR03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D R,Lが成功したためSDSF LOG FIND REPLYのIEE600Iも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正答の根拠: Aは応答記録で IEE600I を読みREPLY IDと発行ジョブの主値として変更結果を検証しWTOR03に残します。
    内部の仕組み: 変更後の確認では未応答一覧を補助操作とし未応答WTORの反映値と残存値をIEE112Iと対象WTOR03で照合します。
    誤答を含む比較: 応答記録と未応答一覧の役割を分けるとA: 周辺状態の後にIEE600Iを確認する点でWTOR03を判定できます、B: 変更前のREPLY IDと発行ジョブを失う点で未応答一覧の範囲を越えます、C: SAF連携の値ではIEE600Iを確認できないうえに追加前提も不正な点でWTOR03の値を示しません、D: 補助操作の成功ではIEE600Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の応答管理・未応答で判定する対象は WTOR03 です。
    用語定義: 変更後の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 変更後の確認 WTOR03**

    - 検証目的: WTOR応答管理の未応答WTORについて変更結果を検証し、WTOR03のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR03の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR03の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB03,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB03を指定し、WTOR03の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB03 ACTIVE ON SYSA ASID=0003
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
    ② ステップ2 の IEE112I が画面・出力に表示されること
    ③ ステップ3 の IEE115I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 引継ぎ記録 WTOR09 {#c38-i0219}
*分類: WTOR応答管理*  ・  難易度: 中級

引継ぎ記録では WTOR応答管理 の 応答記録 を主操作として WTOR09 を判定します。次担当者が追跡できる証跡への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR09 に残します。引継ぎ記録を補助する 未応答一覧 では IEE112I を補助値として WTOR09 へ保存します。主判定の引継ぎ記録では応答管理・未応答の 応答記録 から IEE600I を読み WTOR09 へ残します。証跡照合の引継ぎ記録では応答管理・未応答の IEE600I と IEE112I を WTOR09 に保存します。記録対応の引継ぎ記録では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で WTOR応答管理 の 応答記録 と 未応答一覧 を使い 再現可能な記録を作成 します。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE600I を読み対象 WTOR09 を切り分ける確認方法はどれですか。

    - A. D R,Lが成功したためSDSF LOG FIND REPLYのIEE600Iも正常だと推定する。主出力は保存しない。
    - B. SDSF LOG FIND REPLYを対象名なしで実行する。一覧の先頭行をWTOR09の結果として記録する。
    - C. 対象名WTOR09を指定してSDSF LOG FIND REPLYを実行する。応答中のIEE600Iと時刻を保存する。D R,Lで周辺状態を補完する。 ✅
    - D. 前回保存したSDSF LOG FIND REPLYの結果を使う。今回のD R,Lの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 中級

    **解説:** 採用操作の理由: Cは応答記録で IEE600I を読みREPLY IDと発行ジョブの主値として再現可能な記録を作成しWTOR09に残します。
    製品内の仕組み: 引継ぎ記録では未応答一覧を補助操作とし未応答WTORの次担当者が追跡できる証跡をIEE112Iと対象WTOR09で照合します。
    選択肢別の説明: 応答記録と未応答一覧の役割を分けるとA: 補助操作の成功ではIEE600Iを確定できない点でWTOR09の値を示しません、B: 先頭行はWTOR09と確定できない点で引継ぎ記録に合いません、C: IEE600Iと時刻を保存する点で応答記録に合います、D: 採取時刻が異なる点でWTOR応答管理に使いません。結論として引継ぎ記録の応答管理・未応答で判定する対象は WTOR09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 引継ぎ記録 WTOR09**

    - 検証目的: WTOR応答管理の未応答WTORについて再現可能な記録を作成し、WTOR09のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR09の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR09の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB09,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB09を指定し、WTOR09の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB09 ACTIVE ON SYSA ASID=0009
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
    ② ステップ2 の IEE112I が画面・出力に表示されること
    ③ ステップ3 の IEE115I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 復旧後の確認 WTOR06 {#c38-i0220}
*分類: WTOR応答管理*  ・  難易度: 中級

復旧後の確認では WTOR応答管理 の 応答記録 を主操作として WTOR06 を判定します。再発していないことを示す値への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR06 に残します。復旧後の確認を補助する 未応答一覧 では IEE112I を補助値として WTOR06 へ保存します。主判定の復旧後の確認では応答管理・未応答の 応答記録 から IEE600I を読み WTOR06 へ残します。証跡照合の復旧後の確認では応答管理・未応答の IEE600I と IEE112I を WTOR06 に保存します。記録対応の復旧後の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で WTOR応答管理 の 応答記録 と 未応答一覧 を照合し 再発していないことを示す値 を確かめます。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE600I を読む前に対象 WTOR06 へ行う確認はどれですか。

    - A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をWTOR応答管理のWTOR06にも適用する。
    - B. D R,Lが成功したためSDSF LOG FIND REPLYのIEE600Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象WTOR06へ引き継げるものとする。未応答WTORの再発していないことを示す値は確認済みとして扱う。さらにD A,JOB06のIEE115IをIEE600Iと同種の値として併記する。
    - C. SDSF LOG FIND REPLYを対象名なしで実行する。一覧の先頭行をWTOR06の結果として記録する。
    - D. SDSF LOG FIND REPLYでIEE600Iを取得してからD A,JOB06でIEE115Iを照合する。WTOR06のREPLY IDと発行ジョブを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答内容: Dは応答記録で IEE600I を読みREPLY IDと発行ジョブの主値として復旧後の安定性を確認しWTOR06に残します。
    構成上の背景: 復旧後の確認では未応答一覧を補助操作とし未応答WTORの再発していないことを示す値をIEE112Iと対象WTOR06で照合します。
    候補ごとの理由: 応答記録と未応答一覧の役割を分けるとA: Cross Memoryの値ではIEE600Iを確認できない点で未応答一覧の範囲を越えます、B: 補助操作の成功ではIEE600Iを確定できないうえに追加前提も不正な点でWTOR06の値を示しません、C: 先頭行はWTOR06と確定できない点で復旧後の確認に合いません、D: IEE600IとIEE115Iを順に照合する点で応答記録に合います。結論として復旧後の確認の応答管理・未応答で判定する対象は WTOR06 です。
    初出用語: 復旧後の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 復旧後の確認 WTOR06**

    - 検証目的: WTOR応答管理の未応答WTORについて復旧後の安定性を確認し、WTOR06のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR06の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR06の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB06,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB06を指定し、WTOR06の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB06 ACTIVE ON SYSA ASID=0006
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
    ② ステップ2 の IEE112I が画面・出力に表示されること
    ③ ステップ3 の IEE115I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 復旧準備 WTOR05 {#c38-i0221}
*分類: WTOR応答管理*  ・  難易度: 中級

復旧準備では WTOR応答管理 の 発行元確認 を主操作として WTOR05 を判定します。再開前に必要な整合性への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR05 に残します。復旧準備を補助する 応答記録 では IEE600I を補助値として WTOR05 へ保存します。主判定の復旧準備では応答管理・未応答の 発行元確認 から IEE115I を読み WTOR05 へ残します。証跡照合の復旧準備では応答管理・未応答の IEE115I と IEE600I を WTOR05 に保存します。記録対応の復旧準備では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で WTOR応答管理 の 発行元確認 と 応答記録 を用い 復旧条件を確認 します。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE115I で対象 WTOR05 の REPLY IDと発行ジョブ を再現できる記録はどれですか。

    - A. 前回保存したD A,JOB05の結果を使う。今回のSDSF LOG FIND REPLYの結果と同一時点の証跡として比較する。
    - B. 保存済みのWTOR05の出力を再利用する。今回のD A,JOB05とSDSF LOG FIND REPLYは実行済みとして扱う。
    - C. 変更を加えずD A,JOB05を実行する。IEE115Iを保存する。差分はSDSF LOG FIND REPLYの結果と対象名で対応させる。 ✅
    - D. SDSF LOG FIND REPLYのIEE600IをREPLY IDと発行ジョブの主判定に採用する。D A,JOB05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 中級

    **解説:** 選定理由: Cは発行元確認で IEE115I を読みREPLY IDと発行ジョブの主値として復旧条件を確認しWTOR05に残します。
    処理の仕組み: 復旧準備では応答記録を補助操作とし未応答WTORの再開前に必要な整合性をIEE600Iと対象WTOR05で照合します。
    選択結果の内訳: 発行元確認と応答記録の役割を分けるとA: 採取時刻が異なる点で発行元確認を代替しません、B: 過去出力では今回の復旧準備を示せない点でWTOR応答管理に使いません、C: 変更前のIEE115Iを保存する点で正答です、D: IEE600IはIEE115Iを代替しないうえに追加前提も不正な点でWTOR05を採用できません。結論として復旧準備の応答管理・未応答で判定する対象は WTOR05 です。
    用語の説明: 復旧準備で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 復旧準備 WTOR05**

    - 検証目的: WTOR応答管理の未応答WTORについて復旧条件を確認し、WTOR05のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB05を指定し、WTOR05の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB05 ACTIVE ON SYSA ASID=0005
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR05の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR05の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB05,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE115I が画面・出力に表示されること
    ② ステップ2 の IEE600I が画面・出力に表示されること
    ③ ステップ3 の IEE112I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 構成監査 WTOR08 {#c38-i0222}
*分類: WTOR応答管理*  ・  難易度: 中級

構成監査では WTOR応答管理 の 発行元確認 を主操作として WTOR08 を判定します。定義値と稼働値の一致への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR08 に残します。構成監査を補助する 応答記録 では IEE600I を補助値として WTOR08 へ保存します。主判定の構成監査では応答管理・未応答の 発行元確認 から IEE115I を読み WTOR08 へ残します。証跡照合の構成監査では応答管理・未応答の IEE115I と IEE600I を WTOR08 に保存します。記録対応の構成監査では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で WTOR応答管理 の 発行元確認 と 応答記録 の役割を分け 定義値と稼働値の一致 を調べます。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR08 を誤判定しない進め方はどれですか。

    - A. 保存済みのWTOR08の出力を再利用する。今回のD A,JOB08とSDSF LOG FIND REPLYは実行済みとして扱う。
    - B. SDSF LOG FIND REPLYの結果だけでは確定しない。D A,JOB08のIEE115Iを主証跡として構成差分を監査する。 ✅
    - C. SDSF LOG FIND REPLYのIEE600IをREPLY IDと発行ジョブの主判定に採用する。D A,JOB08の応答は採取対象から外す。
    - D. D R,LのIEE112IをIEE115Iと同義の成功表示として扱う。D A,JOB08は実行しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 技術上の正答: Bは発行元確認で IEE115I を読みREPLY IDと発行ジョブの主値として構成差分を監査しWTOR08に残します。
    実行時の背景: 構成監査では応答記録を補助操作とし未応答WTORの定義値と稼働値の一致をIEE600Iと対象WTOR08で照合します。
    四つの候補の理由: 発行元確認と応答記録の役割を分けるとA: 過去出力では今回の構成監査を示せない点でWTOR応答管理に使いません、B: IEE115Iを主証跡として区別する点で正答です、C: IEE600IはIEE115Iを代替しない点でWTOR08を採用できません、D: IEE112IとIEE115Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の応答管理・未応答で判定する対象は WTOR08 です。
    初出語定義: 構成監査で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 構成監査 WTOR08**

    - 検証目的: WTOR応答管理の未応答WTORについて構成差分を監査し、WTOR08のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB08を指定し、WTOR08の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB08 ACTIVE ON SYSA ASID=0008
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR08の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR08の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB08,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE115I が画面・出力に表示されること
    ② ステップ2 の IEE600I が画面・出力に表示されること
    ③ ステップ3 の IEE112I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 通常状態の確認 WTOR01 {#c38-i0223}
*分類: WTOR応答管理*  ・  難易度: 中級

通常状態の確認では WTOR応答管理 の 未応答一覧 を主操作として WTOR01 を判定します。基準値と現在値の差への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR01 に残します。通常状態の確認を補助する 発行元確認 では IEE115I を補助値として WTOR01 へ保存します。主判定の通常状態の確認では応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR01 へ残します。証跡照合の通常状態の確認では応答管理・未応答の IEE112I と IEE115I を WTOR01 に保存します。記録対応の通常状態の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で WTOR応答管理 の 未応答一覧 と 発行元確認 を組み合わせる際は 未応答WTOR が応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能という仕組みを前提にします。別WTORへ応答すると停止や再試行の対象を誤ります。IEE112I と REPLY IDと発行ジョブ を対象 WTOR01 で確認する組合せはどれですか。

    - A. D A,JOB01のIEE115IをREPLY IDと発行ジョブの主判定に採用する。D R,Lの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. SDSF LOG FIND REPLYのIEE600IをIEE112Iと同義の成功表示として扱う。D R,Lは実行しない。
    - C. D R,Lを先に実行する。対象WTOR01のIEE112IをREPLY IDと発行ジョブとして記録する。続いてD A,JOB01で同一対象を照合する。 ✅
    - D. D R,Lが応答を返した時点で正常とする。応答中のIEE112Iの値は記録しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解の説明: Cは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として通常状態を確定しWTOR01に残します。
    背景・仕組み: 通常状態の確認では発行元確認を補助操作とし未応答WTORの基準値と現在値の差をIEE115Iと対象WTOR01で照合します。
    選択肢の理由: 未応答一覧と発行元確認の役割を分けるとA: IEE115IはIEE112Iを代替しないうえに追加前提も不正な点で未応答WTORに使えません、B: IEE600IとIEE112Iは確認項目が異なる点でWTOR01を採用できません、C: IEE112Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではREPLY IDと発行ジョブを判定できない点で一次資料と一致しません。結論として通常状態の確認の応答管理・未応答で判定する対象は WTOR01 です。
    用語の初出定義: 通常状態の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 通常状態の確認 WTOR01**

    - 検証目的: WTOR応答管理の未応答WTORについて通常状態を確定し、WTOR01のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR01の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB01,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB01を指定し、WTOR01の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB01 ACTIVE ON SYSA ASID=0001
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR01の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
    ② ステップ2 の IEE115I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOR応答管理 未応答WTOR 障害切り分け WTOR04 {#c38-i0224}
*分類: WTOR応答管理*  ・  難易度: 中級

障害切り分けでは WTOR応答管理 の 未応答一覧 を主操作として WTOR04 を判定します。最初に失敗した処理への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR04 に残します。障害切り分けを補助する 発行元確認 では IEE115I を補助値として WTOR04 へ保存します。主判定の障害切り分けでは応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR04 へ残します。証跡照合の障害切り分けでは応答管理・未応答の IEE112I と IEE115I を WTOR04 に保存します。記録対応の障害切り分けでは応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで WTOR応答管理 の 未応答一覧 と 発行元確認 を実施し 未応答WTOR の役割を確認します。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR04 の証跡を取る方法はどれですか。

    - A. SDSF LOG FIND REPLYのIEE600IをIEE112Iと同義の成功表示として扱う。D R,Lは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D R,Lの出力でWTOR04とIEE112Iが同じ応答にあることを確認する。REPLY IDと発行ジョブをその応答から採取する。 ✅
    - C. D R,Lが応答を返した時点で正常とする。応答中のIEE112Iの値は記録しない。
    - D. D R,Lのコマンド文字列だけを記録する。IEE112Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Bは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として障害範囲を限定しWTOR04に残します。
    技術的背景: 障害切り分けでは発行元確認を補助操作とし未応答WTORの最初に失敗した処理をIEE115Iと対象WTOR04で照合します。
    四択の評価: 未応答一覧と発行元確認の役割を分けるとA: IEE600IとIEE112Iは確認項目が異なるうえに追加前提も不正な点でWTOR04を採用できません、B: WTOR04とIEE112Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではREPLY IDと発行ジョブを判定できない点で一次資料と一致しません、D: 入力記録だけではREPLY IDと発行ジョブを証明できない点でREPLY IDと発行ジョブを確認できません。結論として障害切り分けの応答管理・未応答で判定する対象は WTOR04 です。
    初出語の意味: 障害切り分けで使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOR応答管理 未応答WTOR 障害切り分け WTOR04**

    - 検証目的: WTOR応答管理の未応答WTORについて障害範囲を限定し、WTOR04のREPLY IDと発行ジョブを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR04の未応答一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D R,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 12.20.10 DISPLAY R 123
    001 R SYS1,REPLY U OR C
    002 R JOB04,MOUNT VOLUME
    ```

    画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB04を指定し、WTOR04の発行元確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,JOB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I JOB04 ACTIVE ON SYSA ASID=0004
    ```

    画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR04の応答記録を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND REPLY
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
    ```

    画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
    ② ステップ2 の IEE115I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12




## z/OS System Programming > WTOメッセージ

### CONSOLE表示 出口確認 運用確認075 {#c38-i0225}
*分類: WTOメッセージ*  ・  難易度: 中級

第七十五観点 WTOメッセージ の運用では CONSOLE表示 を表示、定義、証跡で確認します（第七十五観点）。第七十五観点 役割は コンソールID、権限、経路コード、応答数などの運用情報を確認する表示という範囲です（第七十五観点）。第七十五観点 IFASMFDPジョブログのSYSPRINT の値を WTOR reply 005 と合わせ、共通ストレージ変更の記録を記録します（第七十五観点）。第七十五観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録075に残します（第七十五観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第七十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は CONSOLE表示、出口確認、運用確認 です。IFASMFDPジョブログのSYSPRINT と WTOR reply 005 を合わせて読む時の採用方針として正しいものはどれか。

    - A. PROGxx運用 の一般メモを採り、WTOR reply 005、メッセージID、時刻の対応を記録外に置き、zOSSP誤記075として調査範囲を狭める。
    - B. IFASMFDPジョブログのSYSPRINT と WTOR reply 005 を同一票へ記録し、CONSOLE表示 を zOSSP正075で確定する。 ✅
    - C. CONSOLE表示 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延075として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在075として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第七十五観点 採用理由: Bは CONSOLE表示 の状態を表示値と定義の両方から確認するため、記録として妥当です（第七十五観点）。第七十五観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第七十五観点）。第七十五観点 誤答整理: Aは一般メモ偏重、Cはジョブログ除外、Dは再現性不足が理由です（第七十五観点）。第七十五観点 用語整理: SMFはシステム測定記録です（第七十五観点）。第七十五観点 IFASMFDPはSMFデータ退避に使います（第七十五観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **CONSOLE表示 出口確認 運用確認075**

    - 検証目的: CONSOLE表示 の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により CONSOLE表示 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.03 GRS STATUS 824
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により CONSOLE表示 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.03 GRS STATUS 834
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により CONSOLE表示 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.03 DISPLAY XCF 844
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### IEFU84出口 定義照合 運用確認091 {#c38-i0226}
*分類: WTOメッセージ*  ・  難易度: 上級

第九十一観点 WTOメッセージ の運用では IEFU84出口 を表示、定義、証跡で確認します（第九十一観点）。第九十一観点 役割は SMFレコードの事後処理や選択に関わるインストール出口という範囲です（第九十一観点）。第九十一観点 SET PROG=xx後のIEE252I表示 の値を TRACE DISPLAY と合わせ、アドレス空間分離の確認を記録します（第九十一観点）。第九十一観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録091に残します（第九十一観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第九十一証跡です。WTOメッセージ の運用で IEFU84出口 を点検します。確認観点は IEFU84出口、定義照合、運用確認 です。TRACE DISPLAY を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. システム出口 の一般メモを採り、TRACE DISPLAY、メッセージID、時刻の対応を記録外に置き、zOSSP誤記091として調査範囲を狭める。
    - B. IEFU84出口 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延091として扱う。
    - C. SET PROG=xx後のIEE252I表示 と TRACE DISPLAY を同一票へ記録し、IEFU84出口 を zOSSP正091で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在091として残す。

    正解: **C** ／ 難易度: 上級

    **解説:** 第九十一観点 採用理由: Cは IEFU84出口 の状態を表示値と定義の両方から確認するため、記録として妥当です（第九十一観点）。第九十一観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第九十一観点）。第九十一観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第九十一観点）。第九十一観点 用語確認: APFは許可ライブラリーの管理機能です（第九十一観点）。第九十一観点 PROGxxは動的なプログラム管理指定です（第九十一観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **IEFU84出口 定義照合 運用確認091**

    - 検証目的: IEFU84出口 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU84出口 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.19 GRS STATUS 840
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU84出口 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.19 GRS STATUS 850
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU84出口 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.19 DISPLAY XCF 860
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### LNKAUTH指定 ストレージ確認 運用確認058 {#c38-i0227}
*分類: WTOメッセージ*  ・  難易度: 中級

第五十八観点 LNKAUTH指定 は z/OS System Programming の WTOメッセージ で扱う管理項目です（第五十八観点）。第五十八観点 LNKLSTライブラリーをAPF許可とみなすかを制御するシステム指定という説明を操作結果と照合します（第五十八観点）。第五十八観点 SYS1.PARMLIB(PROGSP)、parmlibメンバーの該当ステートメント、定義メンバーを照合し、オペレーター応答漏れの防止を確認します（第五十八観点）。第五十八観点 証跡には資料IDと確認値を併記し、zOSSP記録058として保存します（第五十八観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第五十八証跡です。LNKAUTH指定 の記録を監査用に整えます。確認観点は LNKAUTH指定、ストレージ確認、運用確認 です。オペレーター応答漏れの防止のために、parmlibメンバーの該当ステートメント を使った運用記録として最も適切な扱いはどれか。

    - A. parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を同一票へ記録し、LNKAUTH指定 を zOSSP正058で確定する。 ✅
    - B. SMF記録 の一般メモを採り、SYS1.PARMLIB(PROGSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記058として調査範囲を狭める。
    - C. LNKAUTH指定 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延058として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在058として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第五十八観点 正答根拠: Aは parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を結び付けるため、対象システムの取り違えを防げます（第五十八観点）。第五十八観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第五十八観点）。第五十八観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第五十八観点）。第五十八観点 用語説明: WTOは通知メッセージです（第五十八観点）。第五十八観点 WTORは応答を求めるメッセージです（第五十八観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **LNKAUTH指定 ストレージ確認 運用確認058**

    - 検証目的: LNKAUTH指定 の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LNKAUTH指定 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(PROGSP)
    → Enter を押す
    ```

    画面・出力:
    ```text
    APF FORMAT(DYNAMIC)
    APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
    LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
    ```

    画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LNKAUTH指定 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SET PROG=SP
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
    IEE536I PROG VALUE SP NOW IN EFFECT
    ```

    画面・出力には IEE252I が含まれる。IEE252I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LNKAUTH指定 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 06.10.10 PROG,APF DISPLAY 857
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
      12  MPRES3 MYPROG.LOADLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### LOGRECバッファ 定義照合 運用確認041 {#c38-i0228}
*分類: WTOメッセージ*  ・  難易度: 中級

第四十一観点 WTOメッセージ で LOGRECバッファ は 定義照合 の対象です（第四十一観点）。第四十一観点 確認時には エラー記録を保持し、IPCSやEREPの診断対象になる記録領域という性質を前提にします（第四十一観点）。第四十一観点 SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同じ証跡に置き、アドレス空間分離の確認を管理します（第四十一観点）。第四十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録041から再現します（第四十一観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十一証跡です。WTOメッセージ の運用で LOGRECバッファ を点検します。確認観点は LOGRECバッファ、定義照合、運用確認 です。SET PROG=xx後のIEE252I表示 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同一票へ記録し、LOGRECバッファ を zOSSP正041で確定する。 ✅
    - B. ENQ資源管理 の一般メモを採り、SYS1.LINKLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記041として調査範囲を狭める。
    - C. LOGRECバッファ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延041として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在041として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第四十一観点 正解確認: Aは LOGRECバッファ と SYS1.LINKLIB を同じ証跡で扱うため、後続の照合に使えます（第四十一観点）。第四十一観点 背景確認: APF、LPA、LNKLSTはプログラム取得と許可範囲に関係します（第四十一観点）。第四十一観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十一観点）。第四十一観点 用語メモ: TCBはタスクの制御ブロックです（第四十一観点）。第四十一観点 SRBは非同期作業の実行単位です（第四十一観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **LOGRECバッファ 定義照合 運用確認041**

    - 検証目的: LOGRECバッファ の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SDSF LOG

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LOGRECバッファ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.18.17 PROG,APF DISPLAY 940
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       2  MPRES1 SYS1.SVCLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LOGRECバッファ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
    ```

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LOGRECバッファ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF,ENTRY=(1-5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.26.17 PROG,APF DISPLAY 950
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       5  MPRES1 ISF.SISFLPA
    ```

    画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SMFPRMxx ストレージ確認 運用確認008 {#c38-i0229}
*分類: WTOメッセージ*  ・  難易度: 初級

第八観点 z/OS System Programming の WTOメッセージ では SMFPRMxx を障害調査で照合します（第八観点）。第八観点 資料上は SMF記録対象、バッファ、データセット、ログストリーム動作を定義するとして扱います（第八観点）。第八観点 SMF.LOGSTREAM.SP を起点に表示値を戻し、オペレーター応答漏れの防止を点検します（第八観点）。第八観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録008へ書きます（第八観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **SMFPRMxx ストレージ確認 運用確認008**

    - 検証目的: SMFPRMxx の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: ISPF / SAF review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SMFPRMxx の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(IEASYS08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEASYS08
    PROG=SP
    SMF=SP
    GRSRNL=SP
    LNKAUTH=LNKLST
    ```

    画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SMFPRMxx の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> FILTER PREFIX CSV
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
    CSV450I PROG,APF DISPLAY
    ```

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SMFPRMxx の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> FILTER PREFIX IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
    IEE536I PROG VALUE SP NOW IN EFFECT
    ```

    画面・出力には IEE536I が含まれる。IEE536I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SVC割り込み 出口確認 運用確認025 {#c38-i0230}
*分類: WTOメッセージ*  ・  難易度: 中級

第二十五観点 WTOメッセージ で SVC割り込み は 出口確認 の対象です（第二十五観点）。第二十五観点 確認時には 問題プログラムからz/OSサービスを要求し、監視プログラム状態へ制御という性質を前提にします（第二十五観点）。第二十五観点 IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同じ証跡に置き、共通ストレージ変更の記録を管理します（第二十五観点）。第二十五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録025から再現します（第二十五観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第二十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は SVC割り込み、出口確認、運用確認 です。QNAME=SYSDSN を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同一票へ記録し、SVC割り込み を zOSSP正025で確定する。 ✅
    - B. TCB/SRB管理 の一般メモを採り、QNAME=SYSDSN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記025として調査範囲を狭める。
    - C. SVC割り込み の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延025として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在025として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第二十五観点 正解確認: Aは SVC割り込み と QNAME=SYSDSN を同じ証跡で扱うため、後続の照合に使えます（第二十五観点）。第二十五観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第二十五観点）。第二十五観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第二十五観点）。第二十五観点 用語確認: APFは許可ライブラリーの管理機能です（第二十五観点）。第二十五観点 PROGxxは動的なプログラム管理指定です（第二十五観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SVC割り込み 出口確認 運用確認025**

    - 検証目的: SVC割り込み の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SDSF LOG

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC割り込み の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.18.01 PROG,APF DISPLAY 924
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       2  MPRES1 SYS1.SVCLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC割り込み の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
    ```

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC割り込み の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF,ENTRY=(1-5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.26.01 PROG,APF DISPLAY 974
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       5  MPRES1 ISF.SISFLPA
    ```

    画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### WTOメッセージ WTO経路コード ログとの照合 WTO07 {#c38-i0231}
*分類: WTOメッセージ*  ・  難易度: 中級

ログとの照合では WTOメッセージ の MPF表示 を主操作として WTO07 を判定します。時刻と対象識別子への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO07 に残します。ログとの照合を補助する コンソール表示 では IEE889I を補助値として WTO07 へ保存します。主判定のログとの照合ではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO07 へ残します。証跡照合のログとの照合ではメッセージ・経路コードの MPFLST と IEE889I を WTO07 に保存します。記録対応のログとの照合ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で WTOメッセージ の MPF表示 と コンソール表示 を使い 操作とログを対応 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読み対象 WTO07 を切り分ける確認方法はどれですか。

    - A. D MPFが応答を返した時点で正常とする。応答中のMPFLSTの値は記録しない。IEE600IをMPFLSTと同じ判定値とみなし対象WTO07の主証跡にする。
    - B. D MPFのコマンド文字列だけを記録する。MPFLSTを含む応答行は保存しない。
    - C. MPFLSTを含むMPF表示の応答行を保存する。その応答を得るためD MPFを使用する。対象WTO07のMESSAGE IDとROUTCDEとして記録する。 ✅
    - D. WTO経路コードの停止または再定義を実施する。その後にD MPFでMPFLSTを採取する。

    正解: **C** ／ 難易度: 中級

    **解説:** 適切な判定: CはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として操作とログを対応しWTO07に残します。
    機能の仕組み: ログとの照合ではコンソール表示を補助操作としWTO経路コードの時刻と対象識別子をIEE889Iと対象WTO07で照合します。
    各候補の評価: MPF表示とコンソール表示の役割を分けるとA: 応答の有無だけではMESSAGE IDとROUTCDEを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではMESSAGE IDとROUTCDEを証明できない点で一次資料と一致しません、C: MPFLSTの実値を対象別に残す点でWTO07を判定できます、D: 変更前のMESSAGE IDとROUTCDEを失う点でコンソール表示の範囲を越えます。結論としてログとの照合のメッセージ・経路コードで判定する対象は WTO07 です。
    用語の定義: ログとの照合で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード ログとの照合 WTO07**

    - 検証目的: WTOメッセージのWTO経路コードについて操作とログを対応し、WTO07のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO07のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST07 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO07のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON07 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO07のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE07 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
    ② ステップ2 の IEE889I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 代替経路の確認 WTO10 {#c38-i0232}
*分類: WTOメッセージ*  ・  難易度: 中級

代替経路の確認では WTOメッセージ の MPF表示 を主操作として WTO10 を判定します。主経路との役割差への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO10 に残します。代替経路の確認を補助する コンソール表示 では IEE889I を補助値として WTO10 へ保存します。主判定の代替経路の確認ではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO10 へ残します。証跡照合の代替経路の確認ではメッセージ・経路コードの MPFLST と IEE889I を WTO10 に保存します。記録対応の代替経路の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で WTOメッセージ の MPF表示 と コンソール表示 を照合し 主経路との役割差 を確かめます。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読む前に対象 WTO10 へ行う確認はどれですか。

    - A. D MPFのコマンド文字列だけを記録する。MPFLSTを含む応答行は保存しない。
    - B. D MPFとD CONSOLESの対象名をそろえる。前者のMPFLSTをMESSAGE IDとROUTCDEの判定値として採用する。 ✅
    - C. WTO経路コードの停止または再定義を実施する。その後にD MPFでMPFLSTを採取する。
    - D. SVC処理のSVC番号とROUTINEを確認する。その値をWTOメッセージのWTO10にも適用する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい判定結果: BはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として代替手段の成立を確認しWTO10に残します。
    運用上の背景: 代替経路の確認ではコンソール表示を補助操作としWTO経路コードの主経路との役割差をIEE889Iと対象WTO10で照合します。
    候補別の検討: MPF表示とコンソール表示の役割を分けるとA: 入力記録だけではMESSAGE IDとROUTCDEを証明できない点で一次資料と一致しません、B: 同じ対象名のMPFLSTを採用する点でWTO10を判定できます、C: 変更前のMESSAGE IDとROUTCDEを失う点でコンソール表示の範囲を越えます、D: SVC処理の値ではMPFLSTを確認できない点でWTO10の値を示しません。結論として代替経路の確認のメッセージ・経路コードで判定する対象は WTO10 です。
    重要用語の定義: 代替経路の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 代替経路の確認 WTO10**

    - 検証目的: WTOメッセージのWTO経路コードについて代替手段の成立を確認し、WTO10のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO10のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST10 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO10のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON10 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO10のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE10 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
    ② ステップ2 の IEE889I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 変更前の確認 WTO02 {#c38-i0233}
*分類: WTOメッセージ*  ・  難易度: 中級

変更前の確認では WTOメッセージ の コンソール表示 を主操作として WTO02 を判定します。変更対象と非対象の境界への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO02 に残します。変更前の確認を補助する SYSLOG検索 では IEE600I を補助値として WTO02 へ保存します。主判定の変更前の確認ではメッセージ・経路コードの コンソール表示 から IEE889I を読み WTO02 へ残します。証跡照合の変更前の確認ではメッセージ・経路コードの IEE889I と IEE600I を WTO02 に保存します。記録対応の変更前の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で WTOメッセージ の コンソール表示 と SYSLOG検索 を実施し WTO経路コード の役割を確認します。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。対象 WTO02 の証跡を取る方法はどれですか。

    - A. D CONSOLESを対象名なしで実行する。一覧の先頭行をWTO02の結果として記録する。
    - B. 対象WTO02についてD CONSOLESの応答からIEE889Iを確認する。SDSF LOG FIND IEEは補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したD CONSOLESの結果を使う。今回のSDSF LOG FIND IEEの結果と同一時点の証跡として比較する。
    - D. 保存済みのWTO02の出力を再利用する。今回のD CONSOLESとSDSF LOG FIND IEEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 中級

    **解説:** 採用理由: Bはコンソール表示で IEE889I を読みMESSAGE IDとROUTCDEの主値として変更前の証跡を保存しWTO02に残します。
    動作の背景: 変更前の確認ではSYSLOG検索を補助操作としWTO経路コードの変更対象と非対象の境界をIEE600Iと対象WTO02で照合します。
    各選択肢の検討: コンソール表示とSYSLOG検索の役割を分けるとA: 先頭行はWTO02と確定できない点で変更前の確認に合いません、B: IEE889Iと補助証跡の時刻を合わせる点でコンソール表示に合います、C: 採取時刻が異なる点でWTOメッセージに使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でWTO経路コードに使えません。結論として変更前の確認のメッセージ・経路コードで判定する対象は WTO02 です。
    初出用語の定義: 変更前の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 変更前の確認 WTO02**

    - 検証目的: WTOメッセージのWTO経路コードについて変更前の証跡を保存し、WTO02のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO02のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON02 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO02のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE02 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO02のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST02 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE889I が画面・出力に表示されること
    ② ステップ2 の IEE600I が画面・出力に表示されること
    ③ ステップ3 の MPFLST が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 変更後の確認 WTO03 {#c38-i0234}
*分類: WTOメッセージ*  ・  難易度: 中級

変更後の確認では WTOメッセージ の SYSLOG検索 を主操作として WTO03 を判定します。反映値と残存値への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO03 に残します。変更後の確認を補助する MPF表示 では MPFLST を補助値として WTO03 へ保存します。主判定の変更後の確認ではメッセージ・経路コードの SYSLOG検索 から IEE600I を読み WTO03 へ残します。証跡照合の変更後の確認ではメッセージ・経路コードの IEE600I と MPFLST を WTO03 に保存します。記録対応の変更後の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で WTOメッセージ の SYSLOG検索 と MPF表示 を用い 変更結果を検証 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。IEE600I で対象 WTO03 の MESSAGE IDとROUTCDE を再現できる記録はどれですか。

    - A. WTO経路コードの停止または再定義を実施する。その後にSDSF LOG FIND IEEでIEE600Iを採取する。
    - B. LNKLST管理のSET名とDATASET順序を確認する。その値をWTOメッセージのWTO03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - C. D MPFで周辺状態を押さえる。その後にSDSF LOG FIND IEEでIEE600Iを確認して変更結果を検証する。 ✅
    - D. D MPFが成功したためSDSF LOG FIND IEEのIEE600Iも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正答の根拠: CはSYSLOG検索で IEE600I を読みMESSAGE IDとROUTCDEの主値として変更結果を検証しWTO03に残します。
    内部の仕組み: 変更後の確認ではMPF表示を補助操作としWTO経路コードの反映値と残存値をMPFLSTと対象WTO03で照合します。
    誤答を含む比較: SYSLOG検索とMPF表示の役割を分けるとA: 変更前のMESSAGE IDとROUTCDEを失う点でMESSAGE IDとROUTCDEを確認できません、B: LNKLST管理の値ではIEE600Iを確認できないうえに追加前提も不正な点でMPF表示の範囲を越えます、C: 周辺状態の後にIEE600Iを確認する点で現在値を示します、D: 補助操作の成功ではIEE600Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のメッセージ・経路コードで判定する対象は WTO03 です。
    用語定義: 変更後の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 変更後の確認 WTO03**

    - 検証目的: WTOメッセージのWTO経路コードについて変更結果を検証し、WTO03のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO03のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE03 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO03のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST03 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO03のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON03 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
    ② ステップ2 の MPFLST が画面・出力に表示されること
    ③ ステップ3 の IEE889I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 引継ぎ記録 WTO09 {#c38-i0235}
*分類: WTOメッセージ*  ・  難易度: 中級

引継ぎ記録では WTOメッセージ の SYSLOG検索 を主操作として WTO09 を判定します。次担当者が追跡できる証跡への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO09 に残します。引継ぎ記録を補助する MPF表示 では MPFLST を補助値として WTO09 へ保存します。主判定の引継ぎ記録ではメッセージ・経路コードの SYSLOG検索 から IEE600I を読み WTO09 へ残します。証跡照合の引継ぎ記録ではメッセージ・経路コードの IEE600I と MPFLST を WTO09 に保存します。記録対応の引継ぎ記録ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で WTOメッセージ の SYSLOG検索 と MPF表示 を用い 再現可能な記録を作成 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。IEE600I で対象 WTO09 の MESSAGE IDとROUTCDE を再現できる記録はどれですか。

    - A. 対象名WTO09を指定してSDSF LOG FIND IEEを実行する。応答中のIEE600Iと時刻を保存する。D MPFで周辺状態を補完する。 ✅
    - B. D MPFが成功したためSDSF LOG FIND IEEのIEE600Iも正常だと推定する。主出力は保存しない。
    - C. SDSF LOG FIND IEEを対象名なしで実行する。一覧の先頭行をWTO09の結果として記録する。
    - D. 前回保存したSDSF LOG FIND IEEの結果を使う。今回のD MPFの結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 中級

    **解説:** 採用操作の理由: AはSYSLOG検索で IEE600I を読みMESSAGE IDとROUTCDEの主値として再現可能な記録を作成しWTO09に残します。
    製品内の仕組み: 引継ぎ記録ではMPF表示を補助操作としWTO経路コードの次担当者が追跡できる証跡をMPFLSTと対象WTO09で照合します。
    選択肢別の説明: SYSLOG検索とMPF表示の役割を分けるとA: IEE600Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではIEE600Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はWTO09と確定できない点でSYSLOG検索を代替しません、D: 採取時刻が異なる点でWTOメッセージに使いません。結論として引継ぎ記録のメッセージ・経路コードで判定する対象は WTO09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 引継ぎ記録 WTO09**

    - 検証目的: WTOメッセージのWTO経路コードについて再現可能な記録を作成し、WTO09のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO09のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE09 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO09のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST09 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO09のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON09 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
    ② ステップ2 の MPFLST が画面・出力に表示されること
    ③ ステップ3 の IEE889I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 復旧後の確認 WTO06 {#c38-i0236}
*分類: WTOメッセージ*  ・  難易度: 中級

復旧後の確認では WTOメッセージ の SYSLOG検索 を主操作として WTO06 を判定します。再発していないことを示す値への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO06 に残します。復旧後の確認を補助する MPF表示 では MPFLST を補助値として WTO06 へ保存します。主判定の復旧後の確認ではメッセージ・経路コードの SYSLOG検索 から IEE600I を読み WTO06 へ残します。証跡照合の復旧後の確認ではメッセージ・経路コードの IEE600I と MPFLST を WTO06 に保存します。記録対応の復旧後の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で WTOメッセージ の SYSLOG検索 と MPF表示 の役割を分け 再発していないことを示す値 を調べます。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。対象 WTO06 を誤判定しない進め方はどれですか。

    - A. GRS資源直列化のSYSTEMとMODEを確認する。その値をWTOメッセージのWTO06にも適用する。
    - B. SDSF LOG FIND IEEでIEE600Iを取得してからD CONSOLESでIEE889Iを照合する。WTO06のMESSAGE IDとROUTCDEを両出力から確定する。 ✅
    - C. D MPFが成功したためSDSF LOG FIND IEEのIEE600Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象WTO06へ引き継げるものとする。WTO経路コードの再発していないことを示す値は確認済みとして扱う。さらにD CONSOLESのIEE889IをIEE600Iと同種の値として併記する。
    - D. SDSF LOG FIND IEEを対象名なしで実行する。一覧の先頭行をWTO06の結果として記録する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正答内容: BはSYSLOG検索で IEE600I を読みMESSAGE IDとROUTCDEの主値として復旧後の安定性を確認しWTO06に残します。
    構成上の背景: 復旧後の確認ではMPF表示を補助操作としWTO経路コードの再発していないことを示す値をMPFLSTと対象WTO06で照合します。
    候補ごとの理由: SYSLOG検索とMPF表示の役割を分けるとA: GRS資源直列化の値ではIEE600Iを確認できない点でMPF表示の範囲を越えます、B: IEE600IとIEE889Iを順に照合する点で現在値を示します、C: 補助操作の成功ではIEE600Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はWTO06と確定できない点でSYSLOG検索を代替しません。結論として復旧後の確認のメッセージ・経路コードで判定する対象は WTO06 です。
    初出用語: 復旧後の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 復旧後の確認 WTO06**

    - 検証目的: WTOメッセージのWTO経路コードについて復旧後の安定性を確認し、WTO06のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO06のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE06 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO06のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST06 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO06のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON06 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
    ② ステップ2 の MPFLST が画面・出力に表示されること
    ③ ステップ3 の IEE889I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 復旧準備 WTO05 {#c38-i0237}
*分類: WTOメッセージ*  ・  難易度: 中級

復旧準備では WTOメッセージ の コンソール表示 を主操作として WTO05 を判定します。再開前に必要な整合性への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO05 に残します。復旧準備を補助する SYSLOG検索 では IEE600I を補助値として WTO05 へ保存します。主判定の復旧準備ではメッセージ・経路コードの コンソール表示 から IEE889I を読み WTO05 へ残します。証跡照合の復旧準備ではメッセージ・経路コードの IEE889I と IEE600I を WTO05 に保存します。記録対応の復旧準備ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で WTOメッセージ の コンソール表示 と SYSLOG検索 を組み合わせる際は WTO経路コード がシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みという仕組みを前提にします。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。IEE889I と MESSAGE IDとROUTCDE を対象 WTO05 で確認する組合せはどれですか。

    - A. 変更を加えずD CONSOLESを実行する。IEE889Iを保存する。差分はSDSF LOG FIND IEEの結果と対象名で対応させる。 ✅
    - B. 前回保存したD CONSOLESの結果を使う。今回のSDSF LOG FIND IEEの結果と同一時点の証跡として比較する。
    - C. 保存済みのWTO05の出力を再利用する。今回のD CONSOLESとSDSF LOG FIND IEEは実行済みとして扱う。
    - D. SDSF LOG FIND IEEのIEE600IをMESSAGE IDとROUTCDEの主判定に採用する。D CONSOLESの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 中級

    **解説:** 選定理由: Aはコンソール表示で IEE889I を読みMESSAGE IDとROUTCDEの主値として復旧条件を確認しWTO05に残します。
    処理の仕組み: 復旧準備ではSYSLOG検索を補助操作としWTO経路コードの再開前に必要な整合性をIEE600Iと対象WTO05で照合します。
    選択結果の内訳: コンソール表示とSYSLOG検索の役割を分けるとA: 変更前のIEE889Iを保存する点でコンソール表示に合います、B: 採取時刻が異なる点でWTOメッセージに使いません、C: 過去出力では今回の復旧準備を示せない点でWTO経路コードに使えません、D: IEE600IはIEE889Iを代替しないうえに追加前提も不正な点でWTO05を採用できません。結論として復旧準備のメッセージ・経路コードで判定する対象は WTO05 です。
    用語の説明: 復旧準備で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 復旧準備 WTO05**

    - 検証目的: WTOメッセージのWTO経路コードについて復旧条件を確認し、WTO05のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO05のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON05 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO05のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE05 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO05のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST05 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE889I が画面・出力に表示されること
    ② ステップ2 の IEE600I が画面・出力に表示されること
    ③ ステップ3 の MPFLST が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 構成監査 WTO08 {#c38-i0238}
*分類: WTOメッセージ*  ・  難易度: 中級

構成監査では WTOメッセージ の コンソール表示 を主操作として WTO08 を判定します。定義値と稼働値の一致への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO08 に残します。構成監査を補助する SYSLOG検索 では IEE600I を補助値として WTO08 へ保存します。主判定の構成監査ではメッセージ・経路コードの コンソール表示 から IEE889I を読み WTO08 へ残します。証跡照合の構成監査ではメッセージ・経路コードの IEE889I と IEE600I を WTO08 に保存します。記録対応の構成監査ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で WTOメッセージ の コンソール表示 と SYSLOG検索 を実施し WTO経路コード の役割を確認します。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。対象 WTO08 の証跡を取る方法はどれですか。

    - A. 保存済みのWTO08の出力を再利用する。今回のD CONSOLESとSDSF LOG FIND IEEは実行済みとして扱う。
    - B. SDSF LOG FIND IEEのIEE600IをMESSAGE IDとROUTCDEの主判定に採用する。D CONSOLESの応答は採取対象から外す。
    - C. D MPFのMPFLSTをIEE889Iと同義の成功表示として扱う。D CONSOLESは実行しない。
    - D. SDSF LOG FIND IEEの結果だけでは確定しない。D CONSOLESのIEE889Iを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 技術上の正答: Dはコンソール表示で IEE889I を読みMESSAGE IDとROUTCDEの主値として構成差分を監査しWTO08に残します。
    実行時の背景: 構成監査ではSYSLOG検索を補助操作としWTO経路コードの定義値と稼働値の一致をIEE600Iと対象WTO08で照合します。
    四つの候補の理由: コンソール表示とSYSLOG検索の役割を分けるとA: 過去出力では今回の構成監査を示せない点でWTOメッセージに使いません、B: IEE600IはIEE889Iを代替しない点でWTO経路コードに使えません、C: MPFLSTとIEE889Iは確認項目が異なる点でWTO08を採用できません、D: IEE889Iを主証跡として区別する点で主証跡になります。結論として構成監査のメッセージ・経路コードで判定する対象は WTO08 です。
    初出語定義: 構成監査で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 構成監査 WTO08**

    - 検証目的: WTOメッセージのWTO経路コードについて構成差分を監査し、WTO08のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO08のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON08 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO08のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE08 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO08のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST08 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE889I が画面・出力に表示されること
    ② ステップ2 の IEE600I が画面・出力に表示されること
    ③ ステップ3 の MPFLST が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 通常状態の確認 WTO01 {#c38-i0239}
*分類: WTOメッセージ*  ・  難易度: 中級

通常状態の確認では WTOメッセージ の MPF表示 を主操作として WTO01 を判定します。基準値と現在値の差への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO01 に残します。通常状態の確認を補助する コンソール表示 では IEE889I を補助値として WTO01 へ保存します。主判定の通常状態の確認ではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO01 へ残します。証跡照合の通常状態の確認ではメッセージ・経路コードの MPFLST と IEE889I を WTO01 に保存します。記録対応の通常状態の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で WTOメッセージ の MPF表示 と コンソール表示 を使い 通常状態を確定 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読み対象 WTO01 を切り分ける確認方法はどれですか。

    - A. D MPFを先に実行する。対象WTO01のMPFLSTをMESSAGE IDとROUTCDEとして記録する。続いてD CONSOLESで同一対象を照合する。 ✅
    - B. D CONSOLESのIEE889IをMESSAGE IDとROUTCDEの主判定に採用する。D MPFの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. SDSF LOG FIND IEEのIEE600IをMPFLSTと同義の成功表示として扱う。D MPFは実行しない。
    - D. D MPFが応答を返した時点で正常とする。応答中のMPFLSTの値は記録しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正解の説明: AはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として通常状態を確定しWTO01に残します。
    背景・仕組み: 通常状態の確認ではコンソール表示を補助操作としWTO経路コードの基準値と現在値の差をIEE889Iと対象WTO01で照合します。
    選択肢の理由: MPF表示とコンソール表示の役割を分けるとA: MPFLSTを主値として補助結果と照合する点で正答です、B: IEE889IはMPFLSTを代替しないうえに追加前提も不正な点でWTO01を採用できません、C: IEE600IとMPFLSTは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではMESSAGE IDとROUTCDEを判定できない点で一次資料と一致しません。結論として通常状態の確認のメッセージ・経路コードで判定する対象は WTO01 です。
    用語の初出定義: 通常状態の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 通常状態の確認 WTO01**

    - 検証目的: WTOメッセージのWTO経路コードについて通常状態を確定し、WTO01のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO01のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST01 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO01のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON01 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO01のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE01 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
    ② ステップ2 の IEE889I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### WTOメッセージ WTO経路コード 障害切り分け WTO04 {#c38-i0240}
*分類: WTOメッセージ*  ・  難易度: 中級

障害切り分けでは WTOメッセージ の MPF表示 を主操作として WTO04 を判定します。最初に失敗した処理への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO04 に残します。障害切り分けを補助する コンソール表示 では IEE889I を補助値として WTO04 へ保存します。主判定の障害切り分けではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO04 へ残します。証跡照合の障害切り分けではメッセージ・経路コードの MPFLST と IEE889I を WTO04 に保存します。記録対応の障害切り分けではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで WTOメッセージ の MPF表示 と コンソール表示 を照合し 最初に失敗した処理 を確かめます。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読む前に対象 WTO04 へ行う確認はどれですか。

    - A. SDSF LOG FIND IEEのIEE600IをMPFLSTと同義の成功表示として扱う。D MPFは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D MPFが応答を返した時点で正常とする。応答中のMPFLSTの値は記録しない。
    - C. D MPFのコマンド文字列だけを記録する。MPFLSTを含む応答行は保存しない。
    - D. D MPFの出力でWTO04とMPFLSTが同じ応答にあることを確認する。MESSAGE IDとROUTCDEをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい操作の説明: DはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として障害範囲を限定しWTO04に残します。
    技術的背景: 障害切り分けではコンソール表示を補助操作としWTO経路コードの最初に失敗した処理をIEE889Iと対象WTO04で照合します。
    四択の評価: MPF表示とコンソール表示の役割を分けるとA: IEE600IとMPFLSTは確認項目が異なるうえに追加前提も不正な点でWTO04を採用できません、B: 応答の有無だけではMESSAGE IDとROUTCDEを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではMESSAGE IDとROUTCDEを証明できない点で一次資料と一致しません、D: WTO04とMPFLSTを同じ応答で結ぶ点でWTO04を判定できます。結論として障害切り分けのメッセージ・経路コードで判定する対象は WTO04 です。
    初出語の意味: 障害切り分けで使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **WTOメッセージ WTO経路コード 障害切り分け WTO04**

    - 検証目的: WTOメッセージのWTO経路コードについて障害範囲を限定し、WTO04のMESSAGE IDとROUTCDEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象WTO04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO04のMPF表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D MPF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER MPFLST04 FOUND IN SYS1.PARMLIB MPF ACTIVE
    ```

    画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO04のコンソール表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D CONSOLES
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I CONSOLes STATUS CONSOLE NAME=CON04 STATUS=ACTIVE AUTH=MASTER
    ```

    画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO04のSYSLOG検索を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF LOG FIND IEE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO MESSAGE IEE04 RECORDED IN SYSLOG
    ```

    画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
    ② ステップ2 の IEE889I が画面・出力に表示されること
    ③ ステップ3 の IEE600I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


