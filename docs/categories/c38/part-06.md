---
search:
  exclude: true
---

# z/OS System Programming — 詳細 (6/7)

[← z/OS System Programming の概要へ戻る](index.md)


## z/OS System Programming > アドレス空間

### GRSリング 表示確認 運用確認013 {#c38-i0241}
*分類: アドレス空間*  ・  難易度: 初級

第十三観点 アドレス空間 で GRSリング は 表示確認 の対象です（第十三観点）。第十三観点 確認時には 複数システム間の資源直列化状態を管理し、DISPLAY GRSで確認という性質を前提にします（第十三観点）。第十三観点 DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同じ証跡に置き、割り込み経路の説明性確保を管理します（第十三観点）。第十三観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録013から再現します（第十三観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第十三証跡です。zOSSP記録013として TCB=008F21A0 の証跡を残します。確認観点は GRS、表示確認、運用確認 です。TCB=008F21A0 を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同一票へ記録し、GRS を zOSSP正013で確定する。 ✅
    - B. トレース診断 の一般メモを採り、TCB=008F21A0、メッセージID、時刻の対応を記録外に置き、zOSSP誤記013として調査範囲を狭める。
    - C. GRSリング の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延013として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在013として残す。

    正解: **A** ／ 難易度: 初級

    **解説:** 第十三観点 正解確認: Aは GRS と TCB=008F21A0 を同じ証跡で扱うため、後続の照合に使えます（第十三観点）。第十三観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第十三観点）。第十三観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第十三観点）。第十三観点 用語確認: APFは許可ライブラリーの管理機能です（第十三観点）。第十三観点 PROGxxは動的なプログラム管理指定です（第十三観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **GRSリング 表示確認 運用確認013**

    - 検証目的: GRSリング の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により GRSリング の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.13 DISPLAY R 712
    REPLY ID   MESSAGE TEXT
    005        IEA793A SPECIFY DUMP OPTION FOR TCB=008F21A0
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により GRSリング の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.13 CONSOLE DISPLAY 502
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により GRSリング の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> R 005,INFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO 005 IS;INFO
    IEA631I OPERATOR OPER13 NOW ACTIVE, SYSTEM=SC65
    ```

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SET PROG=xx 直列化確認 運用確認046 {#c38-i0242}
*分類: アドレス空間*  ・  難易度: 中級

第四十六観点 SET PROG=xx は z/OS System Programming の アドレス空間 で扱う管理項目です（第四十六観点）。第四十六観点 PROGxxメンバーを有効化し、APFやLPAなどの動的指定を反映すという説明を操作結果と照合します（第四十六観点）。第四十六観点 RNAME=SYS1.PARMLIB、D TRACE のIEE843I表示、定義メンバーを照合し、診断ログの再現性確保を確認します（第四十六観点）。第四十六観点 証跡には資料IDと確認値を併記し、zOSSP記録046として保存します（第四十六観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十六証跡です。運用確認046 の確認で SET PROG=xx を見直します。確認観点は SET PROG=xx、直列化確認、運用確認 です。診断ログの再現性確保のために、D TRACE のIEE843I表示 を使った運用記録として最も適切な扱いはどれか。

    - A. D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を同一票へ記録し、SET PROG=xx を zOSSP正046で確定する。 ✅
    - B. ディスパッチ制御 の一般メモを採り、RNAME=SYS1.PARMLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記046として調査範囲を狭める。
    - C. SET PROG=xx の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延046として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在046として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第四十六観点 正答根拠: Aは D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を結び付けるため、対象システムの取り違えを防げます（第四十六観点）。第四十六観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第四十六観点）。第四十六観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第四十六観点）。第四十六観点 用語説明: WTOは通知メッセージです（第四十六観点）。第四十六観点 WTORは応答を求めるメッセージです（第四十六観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SET PROG=xx 直列化確認 運用確認046**

    - 検証目的: SET PROG=xx の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: IPCS / dump analysis

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SET PROG=xx の値を確認し、対象の現在値を固定する。
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

    画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SET PROG=xx の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.30.22 TRACE DISPLAY 215
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
    ```

    画面・出力には IEE843I が含まれる。IEE843I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SET PROG=xx の値を確認し、同じ対象として記録できることを確認する。
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
    CURRENT TCB ADDRESS RNAME=SYS1.PARMLIB
    ```

    画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SMFログストリーム 表示確認 運用確認063 {#c38-i0243}
*分類: アドレス空間*  ・  難易度: 中級

第六十三観点 アドレス空間 の運用では SMFログストリーム を表示、定義、証跡で確認します（第六十三観点）。第六十三観点 役割は SMFレコードをシスプレックスロガー経由で記録する方式という範囲です（第六十三観点）。第六十三観点 DISPLAY R,ALL の未応答要求表示 の値を MYPROG.LOADLIB と合わせ、割り込み経路の説明性確保を記録します（第六十三観点）。第六十三観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録063に残します（第六十三観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第六十三証跡です。zOSSP記録063として MYPROG.LOADLIB の証跡を残します。確認観点は SMFログストリーム、表示確認、運用確認 です。DISPLAY R,ALL の未応答要求表示 と MYPROG.LOADLIB を合わせて読む時の採用方針として正しいものはどれか。

    - A. WTOR応答管理 の一般メモを採り、MYPROG.LOADLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記063として調査範囲を狭める。
    - B. DISPLAY R,ALL の未応答要求表示 と MYPROG.LOADLIB を同一票へ記録し、SMFログストリーム を zOSSP正063で確定する。 ✅
    - C. SMFログストリーム の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延063として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在063として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第六十三観点 採用理由: Bは SMFログストリーム の状態を表示値と定義の両方から確認するため、記録として妥当です（第六十三観点）。第六十三観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第六十三観点）。第六十三観点 誤答整理: Aは一般メモ偏重、Cはジョブログ除外、Dは再現性不足が理由です（第六十三観点）。第六十三観点 用語整理: SMFはシステム測定記録です（第六十三観点）。第六十三観点 IFASMFDPはSMFデータ退避に使います（第六十三観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SMFログストリーム 表示確認 運用確認063**

    - 検証目的: SMFログストリーム の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / WLM dispatch

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SMFログストリーム の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.05.15 ACTIVE JOBS DISPLAY 662
    JOBNAME  ASID  STATUS
    WLM      000A  ACTIVE
    JES2     0012  ACTIVE
    ```

    画面・出力には IEE114I が含まれる。IEE114I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SMFログストリーム の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    IWM026I 12.06.15 WLM DISPLAY 672
    SYSTEM   MODE     POLICY
    SC65     GOAL     POLSP15
    ```

    画面・出力には GOAL が含まれる。GOAL を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SMFログストリーム の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF DA panel
    COMMAND ===> DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF DA DISPLAY
    JOBNAME  ASID  CPU%  DP
    BATCH15 0015  02.1  245
    ```

    画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SRB 状態確認 運用確認080 {#c38-i0244}
*分類: アドレス空間*  ・  難易度: 中級

第八十観点 z/OS System Programming の アドレス空間 では SRB を障害調査で照合します（第八十観点）。第八十観点 資料上は サービス要求ブロックとして非同期のシステム作業を表すディスパッチ単位として扱います（第八十観点）。第八十観点 SYS1.PARMLIB(GRSRNLSP) を起点に表示値を戻し、SMF記録欠落の早期検出を点検します（第八十観点）。第八十観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録080へ書きます（第八十観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第八十証跡です。SRB の表示とメッセージIDを比べます。確認観点は SRB、状態確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。

    - A. GRS資源直列化 の一般メモを採り、SYS1.PARMLIB(GRSRNLSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記080として調査範囲を狭める。
    - B. SETPROG APF後のCSV410I表示 と SYS1.PARMLIB(GRSRNLSP) を同一票へ記録し、SRB を zOSSP正080で確定する。 ✅
    - C. SRB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延080として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在080として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第八十観点 照合結果: Bは SYS1.PARMLIB(GRSRNLSP) をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十観点）。第八十観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第八十観点）。第八十観点 誤答確認: Aは SYS1.PARMLIB(GRSRNLSP) 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第八十観点）。第八十観点 用語補足: ENQは資源を直列化します（第八十観点）。第八十観点 DEQは取得した資源を解放します（第八十観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SRB 状態確認 運用確認080**

    - 検証目的: SRB の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: ISPF / SAF review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SRB の値を確認し、対象の現在値を固定する。
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

    画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SRB の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SRB の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IEE536I が含まれる。IEE536I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。

    - 合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SYS1.PARMLIB 直列化確認 運用確認096 {#c38-i0245}
*分類: アドレス空間*  ・  難易度: 上級

第九十六観点 z/OS System Programming の アドレス空間 では SYS1.PARMLIB を障害調査で照合します（第九十六観点）。第九十六観点 資料上は IEASYSxx、PROGxx、SMFPRMxx、GRSRNLxxなとして扱います（第九十六観点）。第九十六観点 ROUTCDE=ALL を起点に表示値を戻し、診断ログの再現性確保を点検します（第九十六観点）。第九十六観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録096へ書きます（第九十六観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第九十六証跡です。運用確認096 の確認で SYS1.PARMLIB を見直します。確認観点は SYS1.PARMLIB、直列化確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. LPA管理 の一般メモを採り、ROUTCDE=ALL、メッセージID、時刻の対応を記録外に置き、zOSSP誤記096として調査範囲を狭める。
    - B. SYS1.PARMLIB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延096として扱う。
    - C. D TRACE のIEE843I表示 と ROUTCDE=ALL を同一票へ記録し、SYS1.PARMLIB を zOSSP正096で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在096として残す。

    正解: **C** ／ 難易度: 上級

    **解説:** 第九十六観点 照合結果: Cは ROUTCDE=ALL をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第九十六観点）。第九十六観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第九十六観点）。第九十六観点 誤答確認: Aは ROUTCDE=ALL 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第九十六観点）。第九十六観点 初出定義: PSWは実行状態を示す語です（第九十六観点）。第九十六観点 SVCは監視プログラム呼出しです（第九十六観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SYS1.PARMLIB 直列化確認 運用確認096**

    - 検証目的: SYS1.PARMLIB の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: ISPF / SAF review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SYS1.PARMLIB の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(IEASYS24)
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEASYS24
    PROG=SP
    SMF=SP
    GRSRNL=SP
    LNKAUTH=LNKLST
    ```

    画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SYS1.PARMLIB の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SYS1.PARMLIB の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IEE536I が含まれる。IEE536I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### アドレス空間 ASID管理 ログとの照合 ASID07 {#c38-i0246}
*分類: アドレス空間*  ・  難易度: 中級

ログとの照合では アドレス空間 の 稼働一覧 を主操作として ASID07 を判定します。時刻と対象識別子への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID07 に残します。ログとの照合を補助する 個別表示 では ASID=00 を補助値として ASID07 へ保存します。主判定のログとの照合ではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID07 へ残します。証跡照合のログとの照合ではアドレス空間・管理の IEE114I と ASID=00 を ASID07 に保存します。記録対応のログとの照合ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で アドレス空間 の 稼働一覧 と 個別表示 を組み合わせる際は ASID管理 がジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みという仕組みを前提にします。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。IEE114I と JOBNAMEとASID を対象 ASID07 で確認する組合せはどれですか。

    - A. D A,Lが応答を返した時点で正常とする。応答中のIEE114Iの値は記録しない。JOBNAMEをIEE114Iと同じ判定値とみなし対象ASID07の主証跡にする。
    - B. D A,Lのコマンド文字列だけを記録する。IEE114Iを含む応答行は保存しない。
    - C. IEE114Iを含む稼働一覧の応答行を保存する。その応答を得るためD A,Lを使用する。対象ASID07のJOBNAMEとASIDとして記録する。 ✅
    - D. ASID管理の停止または再定義を実施する。その後にD A,LでIEE114Iを採取する。

    正解: **C** ／ 難易度: 中級

    **解説:** 適切な判定: Cは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として操作とログを対応しASID07に残します。
    機能の仕組み: ログとの照合では個別表示を補助操作としASID管理の時刻と対象識別子をASID=00と対象ASID07で照合します。
    各候補の評価: 稼働一覧と個別表示の役割を分けるとA: 応答の有無だけではJOBNAMEとASIDを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではJOBNAMEとASIDを証明できない点で一次資料と一致しません、C: IEE114Iの実値を対象別に残す点でASID07を判定できます、D: 変更前のJOBNAMEとASIDを失う点で個別表示の範囲を越えます。結論としてログとの照合のアドレス空間・管理で判定する対象は ASID07 です。
    用語の定義: ログとの照合で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 ログとの照合 ASID07**

    - 検証目的: アドレス空間のASID管理について操作とログを対応し、ASID07のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID07の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB07
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB07を指定し、ASID07の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB07を指定し、ASID07のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
    ② ステップ2 の ASID=00 が画面・出力に表示されること
    ③ ステップ3 の JOBNAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 代替経路の確認 ASID10 {#c38-i0247}
*分類: アドレス空間*  ・  難易度: 中級

代替経路の確認では アドレス空間 の 稼働一覧 を主操作として ASID10 を判定します。主経路との役割差への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID10 に残します。代替経路の確認を補助する 個別表示 では ASID=00 を補助値として ASID10 へ保存します。主判定の代替経路の確認ではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID10 へ残します。証跡照合の代替経路の確認ではアドレス空間・管理の IEE114I と ASID=00 を ASID10 に保存します。記録対応の代替経路の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で アドレス空間 の 稼働一覧 と 個別表示 を実施し ASID管理 の役割を確認します。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID10 の証跡を取る方法はどれですか。

    - A. D A,Lのコマンド文字列だけを記録する。IEE114Iを含む応答行は保存しない。
    - B. D A,LとD A,JOB10の対象名をそろえる。前者のIEE114IをJOBNAMEとASIDの判定値として採用する。 ✅
    - C. ASID管理の停止または再定義を実施する。その後にD A,LでIEE114Iを採取する。
    - D. SVC処理のSVC番号とROUTINEを確認する。その値をアドレス空間のASID10にも適用する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい判定結果: Bは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として代替手段の成立を確認しASID10に残します。
    運用上の背景: 代替経路の確認では個別表示を補助操作としASID管理の主経路との役割差をASID=00と対象ASID10で照合します。
    候補別の検討: 稼働一覧と個別表示の役割を分けるとA: 入力記録だけではJOBNAMEとASIDを証明できない点で一次資料と一致しません、B: 同じ対象名のIEE114Iを採用する点でASID10を判定できます、C: 変更前のJOBNAMEとASIDを失う点で個別表示の範囲を越えます、D: SVC処理の値ではIEE114Iを確認できない点でASID10の値を示しません。結論として代替経路の確認のアドレス空間・管理で判定する対象は ASID10 です。
    重要用語の定義: 代替経路の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 代替経路の確認 ASID10**

    - 検証目的: アドレス空間のASID管理について代替手段の成立を確認し、ASID10のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID10の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB10
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB10を指定し、ASID10の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB10を指定し、ASID10のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
    ② ステップ2 の ASID=00 が画面・出力に表示されること
    ③ ステップ3 の JOBNAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 変更前の確認 ASID02 {#c38-i0248}
*分類: アドレス空間*  ・  難易度: 中級

変更前の確認では アドレス空間 の 個別表示 を主操作として ASID02 を判定します。変更対象と非対象の境界への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID02 に残します。変更前の確認を補助する SDSF確認 では JOBNAME を補助値として ASID02 へ保存します。主判定の変更前の確認ではアドレス空間・管理の 個別表示 から ASID=00 を読み ASID02 へ残します。証跡照合の変更前の確認ではアドレス空間・管理の ASID=00 と JOBNAME を ASID02 に保存します。記録対応の変更前の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で アドレス空間 の 個別表示 と SDSF確認 の役割を分け 変更対象と非対象の境界 を調べます。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID02 を誤判定しない進め方はどれですか。

    - A. D A,JOB02を対象名なしで実行する。一覧の先頭行をASID02の結果として記録する。
    - B. 対象ASID02についてD A,JOB02の応答からASID=00を確認する。SDSF DA PREFIX JOB02は補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したD A,JOB02の結果を使う。今回のSDSF DA PREFIX JOB02の結果と同一時点の証跡として比較する。
    - D. 保存済みのASID02の出力を再利用する。今回のD A,JOB02とSDSF DA PREFIX JOB02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 中級

    **解説:** 採用理由: Bは個別表示で ASID=00 を読みJOBNAMEとASIDの主値として変更前の証跡を保存しASID02に残します。
    動作の背景: 変更前の確認ではSDSF確認を補助操作としASID管理の変更対象と非対象の境界をJOBNAMEと対象ASID02で照合します。
    各選択肢の検討: 個別表示とSDSF確認の役割を分けるとA: 先頭行はASID02と確定できない点で変更前の確認に合いません、B: ASID=00と補助証跡の時刻を合わせる点で個別表示に合います、C: 採取時刻が異なる点でアドレス空間に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でASID管理に使えません。結論として変更前の確認のアドレス空間・管理で判定する対象は ASID02 です。
    初出用語の定義: 変更前の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 変更前の確認 ASID02**

    - 検証目的: アドレス空間のASID管理について変更前の証跡を保存し、ASID02のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB02を指定し、ASID02の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB02を指定し、ASID02のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID02の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB02
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ASID=00 が画面・出力に表示されること
    ② ステップ2 の JOBNAME が画面・出力に表示されること
    ③ ステップ3 の IEE114I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 変更後の確認 ASID03 {#c38-i0249}
*分類: アドレス空間*  ・  難易度: 中級

変更後の確認では アドレス空間 の SDSF確認 を主操作として ASID03 を判定します。反映値と残存値への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID03 に残します。変更後の確認を補助する 稼働一覧 では IEE114I を補助値として ASID03 へ保存します。主判定の変更後の確認ではアドレス空間・管理の SDSF確認 から JOBNAME を読み ASID03 へ残します。証跡照合の変更後の確認ではアドレス空間・管理の JOBNAME と IEE114I を ASID03 に保存します。記録対応の変更後の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で アドレス空間 の SDSF確認 と 稼働一覧 を使い 変更結果を検証 します。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。JOBNAME を読み対象 ASID03 を切り分ける確認方法はどれですか。

    - A. ASID管理の停止または再定義を実施する。その後にSDSF DA PREFIX JOB03でJOBNAMEを採取する。
    - B. LNKLST管理のSET名とDATASET順序を確認する。その値をアドレス空間のASID03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - C. D A,Lで周辺状態を押さえる。その後にSDSF DA PREFIX JOB03でJOBNAMEを確認して変更結果を検証する。 ✅
    - D. D A,Lが成功したためSDSF DA PREFIX JOB03のJOBNAMEも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正答の根拠: CはSDSF確認で JOBNAME を読みJOBNAMEとASIDの主値として変更結果を検証しASID03に残します。
    内部の仕組み: 変更後の確認では稼働一覧を補助操作としASID管理の反映値と残存値をIEE114Iと対象ASID03で照合します。
    誤答を含む比較: SDSF確認と稼働一覧の役割を分けるとA: 変更前のJOBNAMEとASIDを失う点でJOBNAMEとASIDを確認できません、B: LNKLST管理の値ではJOBNAMEを確認できないうえに追加前提も不正な点で稼働一覧の範囲を越えます、C: 周辺状態の後にJOBNAMEを確認する点で現在値を示します、D: 補助操作の成功ではJOBNAMEを確定できない点で変更後の確認に合いません。結論として変更後の確認のアドレス空間・管理で判定する対象は ASID03 です。
    用語定義: 変更後の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 変更後の確認 ASID03**

    - 検証目的: アドレス空間のASID管理について変更結果を検証し、ASID03のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB03を指定し、ASID03のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID03の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB03
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB03を指定し、ASID03の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の JOBNAME が画面・出力に表示されること
    ② ステップ2 の IEE114I が画面・出力に表示されること
    ③ ステップ3 の ASID=00 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 引継ぎ記録 ASID09 {#c38-i0250}
*分類: アドレス空間*  ・  難易度: 中級

引継ぎ記録では アドレス空間 の SDSF確認 を主操作として ASID09 を判定します。次担当者が追跡できる証跡への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID09 に残します。引継ぎ記録を補助する 稼働一覧 では IEE114I を補助値として ASID09 へ保存します。主判定の引継ぎ記録ではアドレス空間・管理の SDSF確認 から JOBNAME を読み ASID09 へ残します。証跡照合の引継ぎ記録ではアドレス空間・管理の JOBNAME と IEE114I を ASID09 に保存します。記録対応の引継ぎ記録ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で アドレス空間 の SDSF確認 と 稼働一覧 を使い 再現可能な記録を作成 します。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。JOBNAME を読み対象 ASID09 を切り分ける確認方法はどれですか。

    - A. 対象名ASID09を指定してSDSF DA PREFIX JOB09を実行する。応答中のJOBNAMEと時刻を保存する。D A,Lで周辺状態を補完する。 ✅
    - B. D A,Lが成功したためSDSF DA PREFIX JOB09のJOBNAMEも正常だと推定する。主出力は保存しない。
    - C. SDSF DA PREFIX JOB09を対象名なしで実行する。一覧の先頭行をASID09の結果として記録する。
    - D. 前回保存したSDSF DA PREFIX JOB09の結果を使う。今回のD A,Lの結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 中級

    **解説:** 採用操作の理由: AはSDSF確認で JOBNAME を読みJOBNAMEとASIDの主値として再現可能な記録を作成しASID09に残します。
    製品内の仕組み: 引継ぎ記録では稼働一覧を補助操作としASID管理の次担当者が追跡できる証跡をIEE114Iと対象ASID09で照合します。
    選択肢別の説明: SDSF確認と稼働一覧の役割を分けるとA: JOBNAMEと時刻を保存する点で現在値を示します、B: 補助操作の成功ではJOBNAMEを確定できない点で引継ぎ記録に合いません、C: 先頭行はASID09と確定できない点でSDSF確認を代替しません、D: 採取時刻が異なる点でアドレス空間に使いません。結論として引継ぎ記録のアドレス空間・管理で判定する対象は ASID09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 引継ぎ記録 ASID09**

    - 検証目的: アドレス空間のASID管理について再現可能な記録を作成し、ASID09のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB09を指定し、ASID09のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID09の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB09
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB09を指定し、ASID09の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の JOBNAME が画面・出力に表示されること
    ② ステップ2 の IEE114I が画面・出力に表示されること
    ③ ステップ3 の ASID=00 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 復旧後の確認 ASID06 {#c38-i0251}
*分類: アドレス空間*  ・  難易度: 中級

復旧後の確認では アドレス空間 の SDSF確認 を主操作として ASID06 を判定します。再発していないことを示す値への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID06 に残します。復旧後の確認を補助する 稼働一覧 では IEE114I を補助値として ASID06 へ保存します。主判定の復旧後の確認ではアドレス空間・管理の SDSF確認 から JOBNAME を読み ASID06 へ残します。証跡照合の復旧後の確認ではアドレス空間・管理の JOBNAME と IEE114I を ASID06 に保存します。記録対応の復旧後の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で アドレス空間 の SDSF確認 と 稼働一覧 を照合し 再発していないことを示す値 を確かめます。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。JOBNAME を読む前に対象 ASID06 へ行う確認はどれですか。

    - A. GRS資源直列化のSYSTEMとMODEを確認する。その値をアドレス空間のASID06にも適用する。
    - B. SDSF DA PREFIX JOB06でJOBNAMEを取得してからD A,JOB06でASID=00を照合する。ASID06のJOBNAMEとASIDを両出力から確定する。 ✅
    - C. D A,Lが成功したためSDSF DA PREFIX JOB06のJOBNAMEも正常だと推定する。主出力は保存しない。別資源で得た状態を対象ASID06へ引き継げるものとする。
    - D. SDSF DA PREFIX JOB06を対象名なしで実行する。一覧の先頭行をASID06の結果として記録する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正答内容: BはSDSF確認で JOBNAME を読みJOBNAMEとASIDの主値として復旧後の安定性を確認しASID06に残します。
    構成上の背景: 復旧後の確認では稼働一覧を補助操作としASID管理の再発していないことを示す値をIEE114Iと対象ASID06で照合します。
    候補ごとの理由: SDSF確認と稼働一覧の役割を分けるとA: GRS資源直列化の値ではJOBNAMEを確認できない点で稼働一覧の範囲を越えます、B: JOBNAMEとASID=00を順に照合する点で現在値を示します、C: 補助操作の成功ではJOBNAMEを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はASID06と確定できない点でSDSF確認を代替しません。結論として復旧後の確認のアドレス空間・管理で判定する対象は ASID06 です。
    初出用語: 復旧後の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 復旧後の確認 ASID06**

    - 検証目的: アドレス空間のASID管理について復旧後の安定性を確認し、ASID06のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB06を指定し、ASID06のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID06の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB06
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB06を指定し、ASID06の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の JOBNAME が画面・出力に表示されること
    ② ステップ2 の IEE114I が画面・出力に表示されること
    ③ ステップ3 の ASID=00 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 復旧準備 ASID05 {#c38-i0252}
*分類: アドレス空間*  ・  難易度: 中級

復旧準備では アドレス空間 の 個別表示 を主操作として ASID05 を判定します。再開前に必要な整合性への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID05 に残します。復旧準備を補助する SDSF確認 では JOBNAME を補助値として ASID05 へ保存します。主判定の復旧準備ではアドレス空間・管理の 個別表示 から ASID=00 を読み ASID05 へ残します。証跡照合の復旧準備ではアドレス空間・管理の ASID=00 と JOBNAME を ASID05 に保存します。記録対応の復旧準備ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で アドレス空間 の 個別表示 と SDSF確認 を用い 復旧条件を確認 します。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。ASID=00 で対象 ASID05 の JOBNAMEとASID を再現できる記録はどれですか。

    - A. 変更を加えずD A,JOB05を実行する。ASID=00を保存する。差分はSDSF DA PREFIX JOB05の結果と対象名で対応させる。 ✅
    - B. 前回保存したD A,JOB05の結果を使う。今回のSDSF DA PREFIX JOB05の結果と同一時点の証跡として比較する。
    - C. 保存済みのASID05の出力を再利用する。今回のD A,JOB05とSDSF DA PREFIX JOB05は実行済みとして扱う。
    - D. SDSF DA PREFIX JOB05のJOBNAMEをJOBNAMEとASIDの主判定に採用する。D A,JOB05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 中級

    **解説:** 選定理由: Aは個別表示で ASID=00 を読みJOBNAMEとASIDの主値として復旧条件を確認しASID05に残します。
    処理の仕組み: 復旧準備ではSDSF確認を補助操作としASID管理の再開前に必要な整合性をJOBNAMEと対象ASID05で照合します。
    選択結果の内訳: 個別表示とSDSF確認の役割を分けるとA: 変更前のASID=00を保存する点で個別表示に合います、B: 採取時刻が異なる点でアドレス空間に使いません、C: 過去出力では今回の復旧準備を示せない点でASID管理に使えません、D: JOBNAMEはASID=00を代替しないうえに追加前提も不正な点でASID05を採用できません。結論として復旧準備のアドレス空間・管理で判定する対象は ASID05 です。
    用語の説明: 復旧準備で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 復旧準備 ASID05**

    - 検証目的: アドレス空間のASID管理について復旧条件を確認し、ASID05のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB05を指定し、ASID05の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB05を指定し、ASID05のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID05の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB05
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ASID=00 が画面・出力に表示されること
    ② ステップ2 の JOBNAME が画面・出力に表示されること
    ③ ステップ3 の IEE114I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 構成監査 ASID08 {#c38-i0253}
*分類: アドレス空間*  ・  難易度: 中級

構成監査では アドレス空間 の 個別表示 を主操作として ASID08 を判定します。定義値と稼働値の一致への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID08 に残します。構成監査を補助する SDSF確認 では JOBNAME を補助値として ASID08 へ保存します。主判定の構成監査ではアドレス空間・管理の 個別表示 から ASID=00 を読み ASID08 へ残します。証跡照合の構成監査ではアドレス空間・管理の ASID=00 と JOBNAME を ASID08 に保存します。記録対応の構成監査ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で アドレス空間 の 個別表示 と SDSF確認 の役割を分け 定義値と稼働値の一致 を調べます。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID08 を誤判定しない進め方はどれですか。

    - A. 保存済みのASID08の出力を再利用する。今回のD A,JOB08とSDSF DA PREFIX JOB08は実行済みとして扱う。
    - B. SDSF DA PREFIX JOB08のJOBNAMEをJOBNAMEとASIDの主判定に採用する。D A,JOB08の応答は採取対象から外す。
    - C. D A,LのIEE114IをASID=00と同義の成功表示として扱う。D A,JOB08は実行しない。
    - D. SDSF DA PREFIX JOB08の結果だけでは確定しない。D A,JOB08のASID=00を主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 技術上の正答: Dは個別表示で ASID=00 を読みJOBNAMEとASIDの主値として構成差分を監査しASID08に残します。
    実行時の背景: 構成監査ではSDSF確認を補助操作としASID管理の定義値と稼働値の一致をJOBNAMEと対象ASID08で照合します。
    四つの候補の理由: 個別表示とSDSF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でアドレス空間に使いません、B: JOBNAMEはASID=00を代替しない点でASID管理に使えません、C: IEE114IとASID=00は確認項目が異なる点でASID08を採用できません、D: ASID=00を主証跡として区別する点で主証跡になります。結論として構成監査のアドレス空間・管理で判定する対象は ASID08 です。
    初出語定義: 構成監査で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 構成監査 ASID08**

    - 検証目的: アドレス空間のASID管理について構成差分を監査し、ASID08のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB08を指定し、ASID08の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB08を指定し、ASID08のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID08の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB08
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ASID=00 が画面・出力に表示されること
    ② ステップ2 の JOBNAME が画面・出力に表示されること
    ③ ステップ3 の IEE114I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 通常状態の確認 ASID01 {#c38-i0254}
*分類: アドレス空間*  ・  難易度: 中級

通常状態の確認では アドレス空間 の 稼働一覧 を主操作として ASID01 を判定します。基準値と現在値の差への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID01 に残します。通常状態の確認を補助する 個別表示 では ASID=00 を補助値として ASID01 へ保存します。主判定の通常状態の確認ではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID01 へ残します。証跡照合の通常状態の確認ではアドレス空間・管理の IEE114I と ASID=00 を ASID01 に保存します。記録対応の通常状態の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で アドレス空間 の 稼働一覧 と 個別表示 を組み合わせる際は ASID管理 がジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みという仕組みを前提にします。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。IEE114I と JOBNAMEとASID を対象 ASID01 で確認する組合せはどれですか。

    - A. D A,Lを先に実行する。対象ASID01のIEE114IをJOBNAMEとASIDとして記録する。続いてD A,JOB01で同一対象を照合する。 ✅
    - B. D A,JOB01のASID=00をJOBNAMEとASIDの主判定に採用する。D A,Lの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. SDSF DA PREFIX JOB01のJOBNAMEをIEE114Iと同義の成功表示として扱う。D A,Lは実行しない。
    - D. D A,Lが応答を返した時点で正常とする。応答中のIEE114Iの値は記録しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正解の説明: Aは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として通常状態を確定しASID01に残します。
    背景・仕組み: 通常状態の確認では個別表示を補助操作としASID管理の基準値と現在値の差をASID=00と対象ASID01で照合します。
    選択肢の理由: 稼働一覧と個別表示の役割を分けるとA: IEE114Iを主値として補助結果と照合する点で正答です、B: ASID=00はIEE114Iを代替しないうえに追加前提も不正な点でASID01を採用できません、C: JOBNAMEとIEE114Iは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではJOBNAMEとASIDを判定できない点で一次資料と一致しません。結論として通常状態の確認のアドレス空間・管理で判定する対象は ASID01 です。
    用語の初出定義: 通常状態の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 通常状態の確認 ASID01**

    - 検証目的: アドレス空間のASID管理について通常状態を確定し、ASID01のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID01の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB01
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB01を指定し、ASID01の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB01を指定し、ASID01のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
    ② ステップ2 の ASID=00 が画面・出力に表示されること
    ③ ステップ3 の JOBNAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### アドレス空間 ASID管理 障害切り分け ASID04 {#c38-i0255}
*分類: アドレス空間*  ・  難易度: 中級

障害切り分けでは アドレス空間 の 稼働一覧 を主操作として ASID04 を判定します。最初に失敗した処理への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID04 に残します。障害切り分けを補助する 個別表示 では ASID=00 を補助値として ASID04 へ保存します。主判定の障害切り分けではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID04 へ残します。証跡照合の障害切り分けではアドレス空間・管理の IEE114I と ASID=00 を ASID04 に保存します。記録対応の障害切り分けではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで アドレス空間 の 稼働一覧 と 個別表示 を実施し ASID管理 の役割を確認します。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID04 の証跡を取る方法はどれですか。

    - A. SDSF DA PREFIX JOB04のJOBNAMEをIEE114Iと同義の成功表示として扱う。D A,Lは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D A,Lが応答を返した時点で正常とする。応答中のIEE114Iの値は記録しない。
    - C. D A,Lのコマンド文字列だけを記録する。IEE114Iを含む応答行は保存しない。
    - D. D A,Lの出力でASID04とIEE114Iが同じ応答にあることを確認する。JOBNAMEとASIDをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Dは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として障害範囲を限定しASID04に残します。
    技術的背景: 障害切り分けでは個別表示を補助操作としASID管理の最初に失敗した処理をASID=00と対象ASID04で照合します。
    四択の評価: 稼働一覧と個別表示の役割を分けるとA: JOBNAMEとIEE114Iは確認項目が異なるうえに追加前提も不正な点でASID04を採用できません、B: 応答の有無だけではJOBNAMEとASIDを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではJOBNAMEとASIDを証明できない点で一次資料と一致しません、D: ASID04とIEE114Iを同じ応答で結ぶ点でASID04を判定できます。結論として障害切り分けのアドレス空間・管理で判定する対象は ASID04 です。
    初出語の意味: 障害切り分けで使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **アドレス空間 ASID管理 障害切り分け ASID04**

    - 検証目的: アドレス空間のASID管理について障害範囲を限定し、ASID04のJOBNAMEとASIDを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象ASID04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID04の稼働一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB04
    ```

    画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB04を指定し、ASID04の個別表示を表示します。
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

    画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB04を指定し、ASID04のSDSF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> SDSF DA PREFIX JOB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
    ```

    画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
    ② ステップ2 の ASID=00 が画面・出力に表示されること
    ③ ステップ3 の JOBNAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ優先順位 状態確認 運用確認030 {#c38-i0256}
*分類: アドレス空間*  ・  難易度: 中級

第三十観点 ディスパッチ優先順位 は z/OS System Programming の アドレス空間 で扱う管理項目です（第三十観点）。第三十観点 TCBやSRBなどの実行単位がCPUサービスを受ける順序を示す数値という説明を操作結果と照合します（第三十観点）。第三十観点 SYSPRINT、SETPROG APF後のCSV410I表示、定義メンバーを照合し、SMF記録欠落の早期検出を確認します（第三十観点）。第三十観点 証跡には資料IDと確認値を併記し、zOSSP記録030として保存します（第三十観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第三十証跡です。ディスパッチ優先順位 の表示とメッセージIDを比べます。確認観点は DP、状態確認、運用確認 です。SMF記録欠落の早期検出を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. SAF連携 の一般メモを採り、SYSPRINT、メッセージID、時刻の対応を記録外に置き、zOSSP誤記030として調査範囲を狭める。
    - B. ディスパッチ優先順位 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延030として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在030として残す。
    - D. SETPROG APF後のCSV410I表示 と SYSPRINT を同一票へ記録し、DP を zOSSP正030で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第三十観点 正答根拠: Dは SETPROG APF後のCSV410I表示 と SYSPRINT を結び付けるため、対象システムの取り違えを防げます（第三十観点）。第三十観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第三十観点）。第三十観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第三十観点）。第三十観点 初出定義: PSWは実行状態を示す語です（第三十観点）。第三十観点 SVCは監視プログラム呼出しです（第三十観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **ディスパッチ優先順位 状態確認 運用確認030**

    - 検証目的: ディスパッチ優先順位 の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: IPCS / dump analysis

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ディスパッチ優先順位 の値を確認し、対象の現在値を固定する。
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

    画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ディスパッチ優先順位 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.30.06 TRACE DISPLAY 199
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
    ```

    画面・出力には IEE843I が含まれる。IEE843I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ディスパッチ優先順位 の値を確認し、同じ対象として記録できることを確認する。
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
    CURRENT TCB ADDRESS SYSPRINT
    ```

    画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。

    - 合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110




## z/OS System Programming > システム出口

### CSV410I 優先順位確認 運用確認049 {#c38-i0257}
*分類: システム出口*  ・  難易度: 中級

第四十九観点 システム出口 で CSV410I は 優先順位確認 の対象です（第四十九観点）。第四十九観点 確認時には APFリストへデータセットを追加または削除したことを示すメッセージという性質を前提にします（第四十九観点）。第四十九観点 D PROG,APF のCSV450I表示 と DUMPIN を同じ証跡に置き、オペレーター応答漏れの防止を管理します（第四十九観点）。第四十九観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録049から再現します（第四十九観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十九証跡です。D PROG,APF のCSV450I表示 と DUMPIN の対応を確認します。確認観点は CSV410I、優先順位確認、運用確認 です。DUMPIN を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. D PROG,APF のCSV450I表示 と DUMPIN を同一票へ記録し、CSV410I を zOSSP正049で確定する。 ✅
    - B. Cross Memory の一般メモを採り、DUMPIN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記049として調査範囲を狭める。
    - C. CSV410I の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延049として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在049として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第四十九観点 正解確認: Aは CSV410I と DUMPIN を同じ証跡で扱うため、後続の照合に使えます（第四十九観点）。第四十九観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第四十九観点）。第四十九観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十九観点）。第四十九観点 用語確認: APFは許可ライブラリーの管理機能です（第四十九観点）。第四十九観点 PROGxxは動的なプログラム管理指定です（第四十九観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **CSV410I 優先順位確認 運用確認049**

    - 検証目的: CSV410I の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SDSF LOG

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により CSV410I の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.18.01 PROG,APF DISPLAY 948
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       2  MPRES1 SYS1.SVCLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により CSV410I の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により CSV410I の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF,ENTRY=(1-5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.26.01 PROG,APF DISPLAY 958
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       5  MPRES1 ISF.SISFLPA
    ```

    画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### IEE252I 優先順位確認 運用確認099 {#c38-i0258}
*分類: システム出口*  ・  難易度: 上級

第九十九観点 システム出口 の運用では IEE252I を表示、定義、証跡で確認します（第九十九観点）。第九十九観点 役割は SETコマンドで指定したparmlibメンバーを検出したことを示すメという範囲です（第九十九観点）。第九十九観点 D PROG,APF のCSV450I表示 の値を SYS1.PARMLIB(SMFSP) と合わせ、オペレーター応答漏れの防止を記録します（第九十九観点）。第九十九観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録099に残します（第九十九観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **IEE252I 優先順位確認 運用確認099**

    - 検証目的: IEE252I の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEE252I の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.03 GRS STATUS 848
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEE252I の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.03 GRS STATUS 858
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEE252I の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.03 DISPLAY XCF 868
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### WLMゴールモード 権限確認 運用確認082 {#c38-i0259}
*分類: システム出口*  ・  難易度: 中級

第八十二観点 WLMゴールモード は z/OS System Programming の システム出口 で扱う管理項目です（第八十二観点）。第八十二観点 サービスクラス目標に基づいて作業の優先度と資源配分を管理する運用方式という説明を操作結果と照合します（第八十二観点）。第八十二観点 SYS1.SVCLIB、DISPLAY GRS のISG343I表示、定義メンバーを照合し、アドレス空間分離の確認を確認します（第八十二観点）。第八十二観点 証跡には資料IDと確認値を併記し、zOSSP記録082として保存します（第八十二観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第八十二証跡です。WLMゴールモード に関する設定変更を扱います。確認観点は WLMゴールモード、権限確認、運用確認 です。アドレス空間分離の確認のために、DISPLAY GRS のISG343I表示 を使った運用記録として最も適切な扱いはどれか。

    - A. DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を同一票へ記録し、WLMゴールモード を zOSSP正082で確定する。 ✅
    - B. WTOメッセージ の一般メモを採り、SYS1.SVCLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記082として調査範囲を狭める。
    - C. WLMゴールモード の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延082として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在082として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第八十二観点 正答根拠: Aは DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を結び付けるため、対象システムの取り違えを防げます（第八十二観点）。第八十二観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第八十二観点）。第八十二観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第八十二観点）。第八十二観点 用語説明: WTOは通知メッセージです（第八十二観点）。第八十二観点 WTORは応答を求めるメッセージです（第八十二観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **WLMゴールモード 権限確認 運用確認082**

    - 検証目的: WLMゴールモード の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により WLMゴールモード の値を確認し、対象の現在値を固定する。
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

    画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により WLMゴールモード の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には IEE252I が含まれる。IEE252I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により WLMゴールモード の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 06.10.10 PROG,APF DISPLAY 881
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
      12  MPRES3 MYPROG.LOADLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### アドレス空間 権限確認 運用確認032 {#c38-i0260}
*分類: システム出口*  ・  難易度: 中級

第三十二観点 z/OS System Programming の システム出口 では アドレス空間 を障害調査で照合します（第三十二観点）。第三十二観点 資料上は プログラムとデータを他の利用者領域から分離して管理する仮想記憶単位として扱います（第三十二観点）。第三十二観点 ASID=0010 を起点に表示値を戻し、アドレス空間分離の確認を点検します（第三十二観点）。第三十二観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録032へ書きます（第三十二観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第三十二証跡です。アドレス空間 に関する設定変更を扱います。確認観点は アドレス空間、権限確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。

    - A. LOGREC診断 の一般メモを採り、ASID=0010、メッセージID、時刻の対応を記録外に置き、zOSSP誤記032として調査範囲を狭める。
    - B. DISPLAY GRS のISG343I表示 と ASID=0010 を同一票へ記録し、アドレス空間 を zOSSP正032で確定する。 ✅
    - C. アドレス空間 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延032として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在032として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第三十二観点 照合結果: Bは ASID=0010 をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第三十二観点）。第三十二観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第三十二観点）。第三十二観点 誤答確認: Aは ASID=0010 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第三十二観点）。第三十二観点 用語補足: ENQは資源を直列化します（第三十二観点）。第三十二観点 DEQは取得した資源を解放します（第三十二観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **アドレス空間 権限確認 運用確認032**

    - 検証目的: アドレス空間 の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: ISPF / SAF review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により アドレス空間 の値を確認し、対象の現在値を固定する。
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

    画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により アドレス空間 の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により アドレス空間 の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IEE536I が含まれる。IEE536I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### システム出口 動的出口管理 ログとの照合 EXIT07 {#c38-i0261}
*分類: システム出口*  ・  難易度: 上級

ログとの照合では システム出口 の 出口一覧 を主操作として EXIT07 を判定します。時刻と対象識別子への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT07 に残します。ログとの照合を補助する 個別出口 では CSV463I を補助値として EXIT07 へ保存します。主判定のログとの照合ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT07 へ残します。証跡照合のログとの照合ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT07 に保存します。記録対応のログとの照合ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で システム出口 の 出口一覧 と 個別出口 を用い 操作とログを対応 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV460I で対象 EXIT07 の EXIT名とMODULE を再現できる記録はどれですか。

    - A. CSV460Iを含む出口一覧の応答行を保存する。その応答を得るためD PROG,EXITを使用する。対象EXIT07のEXIT名とMODULEとして記録する。 ✅
    - B. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。CSV411IをCSV460Iと同じ判定値とみなし対象EXIT07の主証跡にする。
    - C. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。
    - D. 動的出口管理の停止または再定義を実施する。その後にD PROG,EXITでCSV460Iを採取する。

    正解: **A** ／ 難易度: 上級

    **解説:** 適切な判定: Aは出口一覧で CSV460I を読みEXIT名とMODULEの主値として操作とログを対応しEXIT07に残します。
    機能の仕組み: ログとの照合では個別出口を補助操作とし動的出口管理の時刻と対象識別子をCSV463Iと対象EXIT07で照合します。
    各候補の評価: 出口一覧と個別出口の役割を分けるとA: CSV460Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではEXIT名とMODULEを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではEXIT名とMODULEを証明できない点でEXIT名とMODULEを確認できません、D: 変更前のEXIT名とMODULEを失う点で個別出口の範囲を越えます。結論としてログとの照合のシステム出口・動的出口管理で判定する対象は EXIT07 です。
    用語の定義: ログとの照合で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 ログとの照合 EXIT07**

    - 検証目的: システム出口の動的出口管理について操作とログを対応し、EXIT07のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT07の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT07 MODULE MOD07 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT07を指定し、EXIT07の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT07
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT07 MODULE MOD07 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD07を指定し、EXIT07のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD07
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD07 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
    ② ステップ2 の CSV463I が画面・出力に表示されること
    ③ ステップ3 の CSV411I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 代替経路の確認 EXIT10 {#c38-i0262}
*分類: システム出口*  ・  難易度: 上級

代替経路の確認では システム出口 の 出口一覧 を主操作として EXIT10 を判定します。主経路との役割差への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT10 に残します。代替経路の確認を補助する 個別出口 では CSV463I を補助値として EXIT10 へ保存します。主判定の代替経路の確認ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT10 へ残します。証跡照合の代替経路の確認ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT10 に保存します。記録対応の代替経路の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で システム出口 の 出口一覧 と 個別出口 の役割を分け 主経路との役割差 を調べます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT10 を誤判定しない進め方はどれですか。

    - A. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。
    - B. 動的出口管理の停止または再定義を実施する。その後にD PROG,EXITでCSV460Iを採取する。
    - C. APF管理のDSNAMEとVOLSERを確認する。その値をシステム出口のEXIT10にも適用する。
    - D. D PROG,EXITとD PROG,EXIT,EX=EXIT10の対象名をそろえる。前者のCSV460IをEXIT名とMODULEの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正しい判定結果: Dは出口一覧で CSV460I を読みEXIT名とMODULEの主値として代替手段の成立を確認しEXIT10に残します。
    運用上の背景: 代替経路の確認では個別出口を補助操作とし動的出口管理の主経路との役割差をCSV463Iと対象EXIT10で照合します。
    候補別の検討: 出口一覧と個別出口の役割を分けるとA: 入力記録だけではEXIT名とMODULEを証明できない点で一次資料と一致しません、B: 変更前のEXIT名とMODULEを失う点でEXIT名とMODULEを確認できません、C: APF管理の値ではCSV460Iを確認できない点で個別出口の範囲を越えます、D: 同じ対象名のCSV460Iを採用する点で現在値を示します。結論として代替経路の確認のシステム出口・動的出口管理で判定する対象は EXIT10 です。
    重要用語の定義: 代替経路の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 代替経路の確認 EXIT10**

    - 検証目的: システム出口の動的出口管理について代替手段の成立を確認し、EXIT10のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT10の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT10 MODULE MOD10 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT10を指定し、EXIT10の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT10
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT10 MODULE MOD10 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD10を指定し、EXIT10のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD10
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD10 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
    ② ステップ2 の CSV463I が画面・出力に表示されること
    ③ ステップ3 の CSV411I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 変更前の確認 EXIT02 {#c38-i0263}
*分類: システム出口*  ・  難易度: 上級

変更前の確認では システム出口 の 個別出口 を主操作として EXIT02 を判定します。変更対象と非対象の境界への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT02 に残します。変更前の確認を補助する モジュール所在 では CSV411I を補助値として EXIT02 へ保存します。主判定の変更前の確認ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT02 へ残します。証跡照合の変更前の確認ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT02 に保存します。記録対応の変更前の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で システム出口 の 個別出口 と モジュール所在 を照合し 変更対象と非対象の境界 を確かめます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読む前に対象 EXIT02 へ行う確認はどれですか。

    - A. D PROG,EXIT,EX=EXIT02を対象名なしで実行する。一覧の先頭行をEXIT02の結果として記録する。
    - B. 前回保存したD PROG,EXIT,EX=EXIT02の結果を使う。今回のD PROG,LPA,MODNAME=MOD02の結果と同一時点の証跡として比較する。
    - C. 保存済みのEXIT02の出力を再利用する。今回のD PROG,EXIT,EX=EXIT02とD PROG,LPA,MODNAME=MOD02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象EXIT02についてD PROG,EXIT,EX=EXIT02の応答からCSV463Iを確認する。D PROG,LPA,MODNAME=MOD02は補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 採用理由: Dは個別出口で CSV463I を読みEXIT名とMODULEの主値として変更前の証跡を保存しEXIT02に残します。
    動作の背景: 変更前の確認ではモジュール所在を補助操作とし動的出口管理の変更対象と非対象の境界をCSV411Iと対象EXIT02で照合します。
    各選択肢の検討: 個別出口とモジュール所在の役割を分けるとA: 先頭行はEXIT02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で個別出口を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でシステム出口に使いません、D: CSV463Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のシステム出口・動的出口管理で判定する対象は EXIT02 です。
    初出用語の定義: 変更前の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 変更前の確認 EXIT02**

    - 検証目的: システム出口の動的出口管理について変更前の証跡を保存し、EXIT02のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT02を指定し、EXIT02の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT02
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT02 MODULE MOD02 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD02を指定し、EXIT02のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD02
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD02 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT02の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT02 MODULE MOD02 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
    ② ステップ2 の CSV411I が画面・出力に表示されること
    ③ ステップ3 の CSV460I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 変更後の確認 EXIT03 {#c38-i0264}
*分類: システム出口*  ・  難易度: 上級

変更後の確認では システム出口 の モジュール所在 を主操作として EXIT03 を判定します。反映値と残存値への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT03 に残します。変更後の確認を補助する 出口一覧 では CSV460I を補助値として EXIT03 へ保存します。主判定の変更後の確認ではシステム出口・動的出口管理の モジュール所在 から CSV411I を読み EXIT03 へ残します。証跡照合の変更後の確認ではシステム出口・動的出口管理の CSV411I と CSV460I を EXIT03 に保存します。記録対応の変更後の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で システム出口 の モジュール所在 と 出口一覧 を組み合わせる際は 動的出口管理 が出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能という仕組みを前提にします。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV411I と EXIT名とMODULE を対象 EXIT03 で確認する組合せはどれですか。

    - A. D PROG,EXITで周辺状態を押さえる。その後にD PROG,LPA,MODNAME=MOD03でCSV411Iを確認して変更結果を検証する。 ✅
    - B. 動的出口管理の停止または再定義を実施する。その後にD PROG,LPA,MODNAME=MOD03でCSV411Iを採取する。
    - C. SAF連携のSAF RCとRACF RCを確認する。その値をシステム出口のEXIT03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D PROG,EXITが成功したためD PROG,LPA,MODNAME=MOD03のCSV411Iも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正答の根拠: Aはモジュール所在で CSV411I を読みEXIT名とMODULEの主値として変更結果を検証しEXIT03に残します。
    内部の仕組み: 変更後の確認では出口一覧を補助操作とし動的出口管理の反映値と残存値をCSV460Iと対象EXIT03で照合します。
    誤答を含む比較: モジュール所在と出口一覧の役割を分けるとA: 周辺状態の後にCSV411Iを確認する点でEXIT03を判定できます、B: 変更前のEXIT名とMODULEを失う点で出口一覧の範囲を越えます、C: SAF連携の値ではCSV411Iを確認できないうえに追加前提も不正な点でEXIT03の値を示しません、D: 補助操作の成功ではCSV411Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のシステム出口・動的出口管理で判定する対象は EXIT03 です。
    用語定義: 変更後の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 変更後の確認 EXIT03**

    - 検証目的: システム出口の動的出口管理について変更結果を検証し、EXIT03のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD03を指定し、EXIT03のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD03
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD03 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT03の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT03 MODULE MOD03 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT03を指定し、EXIT03の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT03
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT03 MODULE MOD03 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
    ② ステップ2 の CSV460I が画面・出力に表示されること
    ③ ステップ3 の CSV463I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 引継ぎ記録 EXIT09 {#c38-i0265}
*分類: システム出口*  ・  難易度: 上級

引継ぎ記録では システム出口 の モジュール所在 を主操作として EXIT09 を判定します。次担当者が追跡できる証跡への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT09 に残します。引継ぎ記録を補助する 出口一覧 では CSV460I を補助値として EXIT09 へ保存します。主判定の引継ぎ記録ではシステム出口・動的出口管理の モジュール所在 から CSV411I を読み EXIT09 へ残します。証跡照合の引継ぎ記録ではシステム出口・動的出口管理の CSV411I と CSV460I を EXIT09 に保存します。記録対応の引継ぎ記録ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で システム出口 の モジュール所在 と 出口一覧 を組み合わせる際は 動的出口管理 が出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能という仕組みを前提にします。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV411I と EXIT名とMODULE を対象 EXIT09 で確認する組合せはどれですか。

    - A. D PROG,EXITが成功したためD PROG,LPA,MODNAME=MOD09のCSV411Iも正常だと推定する。主出力は保存しない。
    - B. D PROG,LPA,MODNAME=MOD09を対象名なしで実行する。一覧の先頭行をEXIT09の結果として記録する。
    - C. 対象名EXIT09を指定してD PROG,LPA,MODNAME=MOD09を実行する。応答中のCSV411Iと時刻を保存する。D PROG,EXITで周辺状態を補完する。 ✅
    - D. 前回保存したD PROG,LPA,MODNAME=MOD09の結果を使う。今回のD PROG,EXITの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 上級

    **解説:** 採用操作の理由: Cはモジュール所在で CSV411I を読みEXIT名とMODULEの主値として再現可能な記録を作成しEXIT09に残します。
    製品内の仕組み: 引継ぎ記録では出口一覧を補助操作とし動的出口管理の次担当者が追跡できる証跡をCSV460Iと対象EXIT09で照合します。
    選択肢別の説明: モジュール所在と出口一覧の役割を分けるとA: 補助操作の成功ではCSV411Iを確定できない点でEXIT09の値を示しません、B: 先頭行はEXIT09と確定できない点で引継ぎ記録に合いません、C: CSV411Iと時刻を保存する点でモジュール所在に合います、D: 採取時刻が異なる点でシステム出口に使いません。結論として引継ぎ記録のシステム出口・動的出口管理で判定する対象は EXIT09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 引継ぎ記録 EXIT09**

    - 検証目的: システム出口の動的出口管理について再現可能な記録を作成し、EXIT09のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD09を指定し、EXIT09のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD09
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD09 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT09の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT09 MODULE MOD09 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT09を指定し、EXIT09の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT09
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT09 MODULE MOD09 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
    ② ステップ2 の CSV460I が画面・出力に表示されること
    ③ ステップ3 の CSV463I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 復旧後の確認 EXIT06 {#c38-i0266}
*分類: システム出口*  ・  難易度: 上級

復旧後の確認では システム出口 の モジュール所在 を主操作として EXIT06 を判定します。再発していないことを示す値への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT06 に残します。復旧後の確認を補助する 出口一覧 では CSV460I を補助値として EXIT06 へ保存します。主判定の復旧後の確認ではシステム出口・動的出口管理の モジュール所在 から CSV411I を読み EXIT06 へ残します。証跡照合の復旧後の確認ではシステム出口・動的出口管理の CSV411I と CSV460I を EXIT06 に保存します。記録対応の復旧後の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で システム出口 の モジュール所在 と 出口一覧 を実施し 動的出口管理 の役割を確認します。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT06 の証跡を取る方法はどれですか。

    - A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をシステム出口のEXIT06にも適用する。
    - B. D PROG,EXITが成功したためD PROG,LPA,MODNAME=MOD06のCSV411Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象EXIT06へ引き継げるものとする。動的出口管理の再発していないことを示す値は確認済みとして扱う。さらにD PROG,EXIT,EX=EXIT06のCSV463IをCSV411Iと同種の値として併記する。
    - C. D PROG,LPA,MODNAME=MOD06を対象名なしで実行する。一覧の先頭行をEXIT06の結果として記録する。
    - D. D PROG,LPA,MODNAME=MOD06でCSV411Iを取得してからD PROG,EXIT,EX=EXIT06でCSV463Iを照合する。EXIT06のEXIT名とMODULEを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正答内容: Dはモジュール所在で CSV411I を読みEXIT名とMODULEの主値として復旧後の安定性を確認しEXIT06に残します。
    構成上の背景: 復旧後の確認では出口一覧を補助操作とし動的出口管理の再発していないことを示す値をCSV460Iと対象EXIT06で照合します。
    候補ごとの理由: モジュール所在と出口一覧の役割を分けるとA: Cross Memoryの値ではCSV411Iを確認できない点で出口一覧の範囲を越えます、B: 補助操作の成功ではCSV411Iを確定できないうえに追加前提も不正な点でEXIT06の値を示しません、C: 先頭行はEXIT06と確定できない点で復旧後の確認に合いません、D: CSV411IとCSV463Iを順に照合する点でモジュール所在に合います。結論として復旧後の確認のシステム出口・動的出口管理で判定する対象は EXIT06 です。
    初出用語: 復旧後の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 復旧後の確認 EXIT06**

    - 検証目的: システム出口の動的出口管理について復旧後の安定性を確認し、EXIT06のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD06を指定し、EXIT06のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD06
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD06 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT06の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT06 MODULE MOD06 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT06を指定し、EXIT06の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT06
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT06 MODULE MOD06 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
    ② ステップ2 の CSV460I が画面・出力に表示されること
    ③ ステップ3 の CSV463I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 復旧準備 EXIT05 {#c38-i0267}
*分類: システム出口*  ・  難易度: 上級

復旧準備では システム出口 の 個別出口 を主操作として EXIT05 を判定します。再開前に必要な整合性への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT05 に残します。復旧準備を補助する モジュール所在 では CSV411I を補助値として EXIT05 へ保存します。主判定の復旧準備ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT05 へ残します。証跡照合の復旧準備ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT05 に保存します。記録対応の復旧準備ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で システム出口 の 個別出口 と モジュール所在 を使い 復旧条件を確認 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読み対象 EXIT05 を切り分ける確認方法はどれですか。

    - A. 前回保存したD PROG,EXIT,EX=EXIT05の結果を使う。今回のD PROG,LPA,MODNAME=MOD05の結果と同一時点の証跡として比較する。
    - B. 保存済みのEXIT05の出力を再利用する。今回のD PROG,EXIT,EX=EXIT05とD PROG,LPA,MODNAME=MOD05は実行済みとして扱う。
    - C. 変更を加えずD PROG,EXIT,EX=EXIT05を実行する。CSV463Iを保存する。差分はD PROG,LPA,MODNAME=MOD05の結果と対象名で対応させる。 ✅
    - D. D PROG,LPA,MODNAME=MOD05のCSV411IをEXIT名とMODULEの主判定に採用する。D PROG,EXIT,EX=EXIT05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: Cは個別出口で CSV463I を読みEXIT名とMODULEの主値として復旧条件を確認しEXIT05に残します。
    処理の仕組み: 復旧準備ではモジュール所在を補助操作とし動的出口管理の再開前に必要な整合性をCSV411Iと対象EXIT05で照合します。
    選択結果の内訳: 個別出口とモジュール所在の役割を分けるとA: 採取時刻が異なる点で個別出口を代替しません、B: 過去出力では今回の復旧準備を示せない点でシステム出口に使いません、C: 変更前のCSV463Iを保存する点で正答です、D: CSV411IはCSV463Iを代替しないうえに追加前提も不正な点でEXIT05を採用できません。結論として復旧準備のシステム出口・動的出口管理で判定する対象は EXIT05 です。
    用語の説明: 復旧準備で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 復旧準備 EXIT05**

    - 検証目的: システム出口の動的出口管理について復旧条件を確認し、EXIT05のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT05を指定し、EXIT05の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT05
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT05 MODULE MOD05 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD05を指定し、EXIT05のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD05
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD05 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT05の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT05 MODULE MOD05 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
    ② ステップ2 の CSV411I が画面・出力に表示されること
    ③ ステップ3 の CSV460I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 構成監査 EXIT08 {#c38-i0268}
*分類: システム出口*  ・  難易度: 上級

構成監査では システム出口 の 個別出口 を主操作として EXIT08 を判定します。定義値と稼働値の一致への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT08 に残します。構成監査を補助する モジュール所在 では CSV411I を補助値として EXIT08 へ保存します。主判定の構成監査ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT08 へ残します。証跡照合の構成監査ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT08 に保存します。記録対応の構成監査ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で システム出口 の 個別出口 と モジュール所在 を照合し 定義値と稼働値の一致 を確かめます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読む前に対象 EXIT08 へ行う確認はどれですか。

    - A. 保存済みのEXIT08の出力を再利用する。今回のD PROG,EXIT,EX=EXIT08とD PROG,LPA,MODNAME=MOD08は実行済みとして扱う。
    - B. D PROG,LPA,MODNAME=MOD08の結果だけでは確定しない。D PROG,EXIT,EX=EXIT08のCSV463Iを主証跡として構成差分を監査する。 ✅
    - C. D PROG,LPA,MODNAME=MOD08のCSV411IをEXIT名とMODULEの主判定に採用する。D PROG,EXIT,EX=EXIT08の応答は採取対象から外す。
    - D. D PROG,EXITのCSV460IをCSV463Iと同義の成功表示として扱う。D PROG,EXIT,EX=EXIT08は実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: Bは個別出口で CSV463I を読みEXIT名とMODULEの主値として構成差分を監査しEXIT08に残します。
    実行時の背景: 構成監査ではモジュール所在を補助操作とし動的出口管理の定義値と稼働値の一致をCSV411Iと対象EXIT08で照合します。
    四つの候補の理由: 個別出口とモジュール所在の役割を分けるとA: 過去出力では今回の構成監査を示せない点でシステム出口に使いません、B: CSV463Iを主証跡として区別する点で正答です、C: CSV411IはCSV463Iを代替しない点でEXIT08を採用できません、D: CSV460IとCSV463Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のシステム出口・動的出口管理で判定する対象は EXIT08 です。
    初出語定義: 構成監査で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 構成監査 EXIT08**

    - 検証目的: システム出口の動的出口管理について構成差分を監査し、EXIT08のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT08を指定し、EXIT08の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT08
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT08 MODULE MOD08 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD08を指定し、EXIT08のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD08
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD08 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT08の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT08 MODULE MOD08 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
    ② ステップ2 の CSV411I が画面・出力に表示されること
    ③ ステップ3 の CSV460I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 通常状態の確認 EXIT01 {#c38-i0269}
*分類: システム出口*  ・  難易度: 上級

通常状態の確認では システム出口 の 出口一覧 を主操作として EXIT01 を判定します。基準値と現在値の差への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT01 に残します。通常状態の確認を補助する 個別出口 では CSV463I を補助値として EXIT01 へ保存します。主判定の通常状態の確認ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT01 へ残します。証跡照合の通常状態の確認ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT01 に保存します。記録対応の通常状態の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で システム出口 の 出口一覧 と 個別出口 を用い 通常状態を確定 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV460I で対象 EXIT01 の EXIT名とMODULE を再現できる記録はどれですか。

    - A. D PROG,EXIT,EX=EXIT01のCSV463IをEXIT名とMODULEの主判定に採用する。D PROG,EXITの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. D PROG,LPA,MODNAME=MOD01のCSV411IをCSV460Iと同義の成功表示として扱う。D PROG,EXITは実行しない。
    - C. D PROG,EXITを先に実行する。対象EXIT01のCSV460IをEXIT名とMODULEとして記録する。続いてD PROG,EXIT,EX=EXIT01で同一対象を照合する。 ✅
    - D. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cは出口一覧で CSV460I を読みEXIT名とMODULEの主値として通常状態を確定しEXIT01に残します。
    背景・仕組み: 通常状態の確認では個別出口を補助操作とし動的出口管理の基準値と現在値の差をCSV463Iと対象EXIT01で照合します。
    選択肢の理由: 出口一覧と個別出口の役割を分けるとA: CSV463IはCSV460Iを代替しないうえに追加前提も不正な点で動的出口管理に使えません、B: CSV411IとCSV460Iは確認項目が異なる点でEXIT01を採用できません、C: CSV460Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではEXIT名とMODULEを判定できない点で一次資料と一致しません。結論として通常状態の確認のシステム出口・動的出口管理で判定する対象は EXIT01 です。
    用語の初出定義: 通常状態の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 通常状態の確認 EXIT01**

    - 検証目的: システム出口の動的出口管理について通常状態を確定し、EXIT01のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT01の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT01 MODULE MOD01 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT01を指定し、EXIT01の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT01
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT01 MODULE MOD01 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD01を指定し、EXIT01のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD01
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD01 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
    ② ステップ2 の CSV463I が画面・出力に表示されること
    ③ ステップ3 の CSV411I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 障害切り分け EXIT04 {#c38-i0270}
*分類: システム出口*  ・  難易度: 上級

障害切り分けでは システム出口 の 出口一覧 を主操作として EXIT04 を判定します。最初に失敗した処理への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT04 に残します。障害切り分けを補助する 個別出口 では CSV463I を補助値として EXIT04 へ保存します。主判定の障害切り分けではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT04 へ残します。証跡照合の障害切り分けではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT04 に保存します。記録対応の障害切り分けではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで システム出口 の 出口一覧 と 個別出口 の役割を分け 最初に失敗した処理 を調べます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT04 を誤判定しない進め方はどれですか。

    - A. D PROG,LPA,MODNAME=MOD04のCSV411IをCSV460Iと同義の成功表示として扱う。D PROG,EXITは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D PROG,EXITの出力でEXIT04とCSV460Iが同じ応答にあることを確認する。EXIT名とMODULEをその応答から採取する。 ✅
    - C. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。
    - D. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bは出口一覧で CSV460I を読みEXIT名とMODULEの主値として障害範囲を限定しEXIT04に残します。
    技術的背景: 障害切り分けでは個別出口を補助操作とし動的出口管理の最初に失敗した処理をCSV463Iと対象EXIT04で照合します。
    四択の評価: 出口一覧と個別出口の役割を分けるとA: CSV411IとCSV460Iは確認項目が異なるうえに追加前提も不正な点でEXIT04を採用できません、B: EXIT04とCSV460Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではEXIT名とMODULEを判定できない点で一次資料と一致しません、D: 入力記録だけではEXIT名とMODULEを証明できない点でEXIT名とMODULEを確認できません。結論として障害切り分けのシステム出口・動的出口管理で判定する対象は EXIT04 です。
    初出語の意味: 障害切り分けで使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 障害切り分け EXIT04**

    - 検証目的: システム出口の動的出口管理について障害範囲を限定し、EXIT04のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT04の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT04 MODULE MOD04 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT04を指定し、EXIT04の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT04
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT04 MODULE MOD04 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD04を指定し、EXIT04のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD04
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD04 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
    ② ステップ2 の CSV463I が画面・出力に表示されること
    ③ ステップ3 の CSV411I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12




## z/OS System Programming > ディスパッチ制御

### FLIH処理 ストレージ確認 運用確認078 {#c38-i0271}
*分類: ディスパッチ制御*  ・  難易度: 中級

第七十八観点 FLIH処理 は z/OS System Programming の ディスパッチ制御 で扱う管理項目です（第七十八観点）。第七十八観点 割り込みを受け、PSWやレジスター状態を保存して適切な処理へ渡す入口という説明を操作結果と照合します（第七十八観点）。第七十八観点 SYS1.PARMLIB(PROGSP)、parmlibメンバーの該当ステートメント、定義メンバーを照合し、診断ログの再現性確保を確認します（第七十八観点）。第七十八観点 証跡には資料IDと確認値を併記し、zOSSP記録078として保存します（第七十八観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第七十八証跡です。FLIH処理 の記録を監査用に整えます。確認観点は FLIH処理、ストレージ確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. SMF記録 の一般メモを採り、SYS1.PARMLIB(PROGSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記078として調査範囲を狭める。
    - B. FLIH処理 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延078として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在078として残す。
    - D. parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を同一票へ記録し、FLIH処理 を zOSSP正078で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第七十八観点 正答根拠: Dは parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を結び付けるため、対象システムの取り違えを防げます（第七十八観点）。第七十八観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第七十八観点）。第七十八観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第七十八観点）。第七十八観点 初出定義: PSWは実行状態を示す語です（第七十八観点）。第七十八観点 SVCは監視プログラム呼出しです（第七十八観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **FLIH処理 ストレージ確認 運用確認078**

    - 検証目的: FLIH処理 の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: IPCS / dump analysis

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により FLIH処理 の値を確認し、対象の現在値を固定する。
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

    画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により FLIH処理 の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には IEE843I が含まれる。IEE843I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により FLIH処理 の値を確認し、同じ対象として記録できることを確認する。
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
    CURRENT TCB ADDRESS SYS1.PARMLIB(PROGSP)
    ```

    画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### IEFU29出口 定義照合 運用確認061 {#c38-i0272}
*分類: ディスパッチ制御*  ・  難易度: 中級

第六十一観点 ディスパッチ制御 で IEFU29出口 は 定義照合 の対象です（第六十一観点）。第六十一観点 確認時には SMF記録データセットが満杯になった時にダンプ処理へつなぐ出口という性質を前提にします（第六十一観点）。第六十一観点 SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同じ証跡に置き、共通ストレージ変更の記録を管理します（第六十一観点）。第六十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録061から再現します（第六十一観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第六十一証跡です。ディスパッチ制御 の運用で IEFU29出口 を点検します。確認観点は IEFU29出口、定義照合、運用確認 です。SYS1.LINKLIB を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同一票へ記録し、IEFU29出口 を zOSSP正061で確定する。 ✅
    - B. ENQ資源管理 の一般メモを採り、SYS1.LINKLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記061として調査範囲を狭める。
    - C. IEFU29出口 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延061として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在061として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第六十一観点 正解確認: Aは IEFU29出口 と SYS1.LINKLIB を同じ証跡で扱うため、後続の照合に使えます（第六十一観点）。第六十一観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第六十一観点）。第六十一観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第六十一観点）。第六十一観点 用語確認: APFは許可ライブラリーの管理機能です（第六十一観点）。第六十一観点 PROGxxは動的なプログラム管理指定です（第六十一観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **IEFU29出口 定義照合 運用確認061**

    - 検証目的: IEFU29出口 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU29出口 の値を確認し、対象の現在値を固定する。
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
    005        IEA793A SPECIFY DUMP OPTION FOR SYS1.LINKLIB
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU29出口 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.13 CONSOLE DISPLAY 490
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU29出口 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> R 005,INFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO 005 IS;INFO
    IEA631I OPERATOR OPER13 NOW ACTIVE, SYSTEM=SC65
    ```

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### IFASMFDP 定義照合 運用確認011 {#c38-i0273}
*分類: ディスパッチ制御*  ・  難易度: 初級

第十一観点 ディスパッチ制御 の運用では IFASMFDP を表示、定義、証跡で確認します（第十一観点）。第十一観点 役割は SMFデータセットの内容を別データセットへ退避し、再利用できる状態へという範囲です（第十一観点）。第十一観点 SET PROG=xx後のIEE252I表示 の値を TRACE DISPLAY と合わせ、共通ストレージ変更の記録を記録します（第十一観点）。第十一観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録011に残します（第十一観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **IFASMFDP 定義照合 運用確認011**

    - 検証目的: IFASMFDP の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IFASMFDP の値を確認し、対象の現在値を固定する。
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

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IFASMFDP の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IFASMFDP の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SYS1.PARMLIB 出口確認 運用確認045 {#c38-i0274}
*分類: ディスパッチ制御*  ・  難易度: 中級

第四十五観点 ディスパッチ制御 で SYS1.PARMLIB は 出口確認 の対象です（第四十五観点）。第四十五観点 確認時には IEASYSxx、PROGxx、SMFPRMxx、GRSRNLxxなという性質を前提にします（第四十五観点）。第四十五観点 IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同じ証跡に置き、割り込み経路の説明性確保を管理します（第四十五観点）。第四十五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録045から再現します（第四十五観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は SYS1.PARMLIB、出口確認、運用確認 です。IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を合わせて読む時の採用方針として正しいものはどれか。

    - A. TCB/SRB管理 の一般メモを採り、QNAME=SYSDSN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記045として調査範囲を狭める。
    - B. IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同一票へ記録し、SYS1.PARMLIB を zOSSP正045で確定する。 ✅
    - C. SYS1.PARMLIB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延045として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在045として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第四十五観点 正解確認: Bは SYS1.PARMLIB と QNAME=SYSDSN を同じ証跡で扱うため、後続の照合に使えます（第四十五観点）。第四十五観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第四十五観点）。第四十五観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十五観点）。第四十五観点 用語整理: SMFはシステム測定記録です（第四十五観点）。第四十五観点 IFASMFDPはSMFデータ退避に使います（第四十五観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SYS1.PARMLIB 出口確認 運用確認045**

    - 検証目的: SYS1.PARMLIB の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SYS1.PARMLIB の値を確認し、対象の現在値を固定する。
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
    005        IEA793A SPECIFY DUMP OPTION FOR QNAME=SYSDSN
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SYS1.PARMLIB の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.21 CONSOLE DISPLAY 534
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SYS1.PARMLIB の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### TCB ストレージ確認 運用確認028 {#c38-i0275}
*分類: ディスパッチ制御*  ・  難易度: 中級

第二十八観点 z/OS System Programming の ディスパッチ制御 では TCB を障害調査で照合します（第二十八観点）。第二十八観点 資料上は タスクの状態、保存情報、実行文脈を保持する制御ブロックとして扱います（第二十八観点）。第二十八観点 SMF.LOGSTREAM.SP を起点に表示値を戻し、診断ログの再現性確保を点検します（第二十八観点）。第二十八観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録028へ書きます（第二十八観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第二十八証跡です。TCB の記録を監査用に整えます。確認観点は TCB、ストレージ確認、運用確認 です。診断ログの再現性確保のために、parmlibメンバーの該当ステートメント を使った運用記録として最も適切な扱いはどれか。

    - A. アドレス空間 の一般メモを採り、SMF.LOGSTREAM.SP、メッセージID、時刻の対応を記録外に置き、zOSSP誤記028として調査範囲を狭める。
    - B. TCB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延028として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在028として残す。
    - D. parmlibメンバーの該当ステートメント と SMF.LOGSTREAM.SP を同一票へ記録し、TCB を zOSSP正028で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第二十八観点 照合結果: Dは SMF.LOGSTREAM.SP をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第二十八観点）。第二十八観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第二十八観点）。第二十八観点 誤答確認: Aは SMF.LOGSTREAM.SP 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第二十八観点）。第二十八観点 用語説明: WTOは通知メッセージです（第二十八観点）。第二十八観点 WTORは応答を求めるメッセージです（第二十八観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **TCB ストレージ確認 運用確認028**

    - 検証目的: TCB の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により TCB の値を確認し、対象の現在値を固定する。
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

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により TCB の値を確認し、定義と資料上の項目を照合する。
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
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により TCB の値を確認し、同じ対象として記録できることを確認する。
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

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### コンポーネントトレース 出口確認 運用確認095 {#c38-i0276}
*分類: ディスパッチ制御*  ・  難易度: 上級

第九十五観点 ディスパッチ制御 の運用では コンポーネントトレース を表示、定義、証跡で確認します（第九十五観点）。第九十五観点 役割は 指定コンポーネントの内部事象を記録し、障害調査に使うトレース機構という範囲です（第九十五観点）。第九十五観点 IFASMFDPジョブログのSYSPRINT の値を WTOR reply 005 と合わせ、割り込み経路の説明性確保を記録します（第九十五観点）。第九十五観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録095に残します（第九十五観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **コンポーネントトレース 出口確認 運用確認095**

    - 検証目的: コンポーネントトレース の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / WLM dispatch

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により コンポーネントトレース の値を確認し、対象の現在値を固定する。
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

    画面・出力には IEE114I が含まれる。IEE114I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により コンポーネントトレース の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    IWM026I 12.06.23 WLM DISPLAY 624
    SYSTEM   MODE     POLICY
    SC65     GOAL     POLSP23
    ```

    画面・出力には GOAL が含まれる。GOAL を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により コンポーネントトレース の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF DA panel
    COMMAND ===> DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF DA DISPLAY
    JOBNAME  ASID  CPU%  DP
    BATCH23 0023  02.1  245
    ```

    画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### ディスパッチ制御 SRMディスパッチ状態 ログとの照合 SRM07 {#c38-i0277}
*分類: ディスパッチ制御*  ・  難易度: 中級

ログとの照合では ディスパッチ制御 の CPU表示 を主操作として SRM07 を判定します。時刻と対象識別子への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM07 に残します。ログとの照合を補助する SRM表示 では IRA200I を補助値として SRM07 へ保存します。主判定のログとの照合ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM07 へ残します。証跡照合のログとの照合ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM07 に保存します。記録対応のログとの照合ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で ディスパッチ制御 の CPU表示 と SRM表示 を使い 操作とログを対応 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読み対象 SRM07 を切り分ける確認方法はどれですか。

    - A. IEE174Iを含むCPU表示の応答行を保存する。その応答を得るためD M=CPUを使用する。対象SRM07のCPU使用率と待ちとして記録する。 ✅
    - B. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。RMFをIEE174Iと同じ判定値とみなし対象SRM07の主証跡にする。
    - C. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。
    - D. SRMディスパッチ状態の停止または再定義を実施する。その後にD M=CPUでIEE174Iを採取する。

    正解: **A** ／ 難易度: 中級

    **解説:** 適切な判定: AはCPU表示で IEE174I を読みCPU使用率と待ちの主値として操作とログを対応しSRM07に残します。
    機能の仕組み: ログとの照合ではSRM表示を補助操作としSRMディスパッチ状態の時刻と対象識別子をIRA200Iと対象SRM07で照合します。
    各候補の評価: CPU表示とSRM表示の役割を分けるとA: IEE174Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではCPU使用率と待ちを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではCPU使用率と待ちを証明できない点でCPU使用率と待ちを確認できません、D: 変更前のCPU使用率と待ちを失う点でSRM表示の範囲を越えます。結論としてログとの照合のディスパッチ制御・ディスパッチ状態で判定する対象は SRM07 です。
    用語の定義: ログとの照合で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 ログとの照合 SRM07**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について操作とログを対応し、SRM07のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM07のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM07のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM07のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 代替経路の確認 SRM10 {#c38-i0278}
*分類: ディスパッチ制御*  ・  難易度: 中級

代替経路の確認では ディスパッチ制御 の CPU表示 を主操作として SRM10 を判定します。主経路との役割差への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM10 に残します。代替経路の確認を補助する SRM表示 では IRA200I を補助値として SRM10 へ保存します。主判定の代替経路の確認ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM10 へ残します。証跡照合の代替経路の確認ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM10 に保存します。記録対応の代替経路の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で ディスパッチ制御 の CPU表示 と SRM表示 を照合し 主経路との役割差 を確かめます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読む前に対象 SRM10 へ行う確認はどれですか。

    - A. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。
    - B. SRMディスパッチ状態の停止または再定義を実施する。その後にD M=CPUでIEE174Iを採取する。
    - C. APF管理のDSNAMEとVOLSERを確認する。その値をディスパッチ制御のSRM10にも適用する。
    - D. D M=CPUとD SRMの対象名をそろえる。前者のIEE174IをCPU使用率と待ちの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい判定結果: DはCPU表示で IEE174I を読みCPU使用率と待ちの主値として代替手段の成立を確認しSRM10に残します。
    運用上の背景: 代替経路の確認ではSRM表示を補助操作としSRMディスパッチ状態の主経路との役割差をIRA200Iと対象SRM10で照合します。
    候補別の検討: CPU表示とSRM表示の役割を分けるとA: 入力記録だけではCPU使用率と待ちを証明できない点で一次資料と一致しません、B: 変更前のCPU使用率と待ちを失う点でCPU使用率と待ちを確認できません、C: APF管理の値ではIEE174Iを確認できない点でSRM表示の範囲を越えます、D: 同じ対象名のIEE174Iを採用する点で現在値を示します。結論として代替経路の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM10 です。
    重要用語の定義: 代替経路の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 代替経路の確認 SRM10**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について代替手段の成立を確認し、SRM10のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM10のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM10のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM10のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 変更前の確認 SRM02 {#c38-i0279}
*分類: ディスパッチ制御*  ・  難易度: 中級

変更前の確認では ディスパッチ制御 の SRM表示 を主操作として SRM02 を判定します。変更対象と非対象の境界への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM02 に残します。変更前の確認を補助する RMF確認 では RMF を補助値として SRM02 へ保存します。主判定の変更前の確認ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM02 へ残します。証跡照合の変更前の確認ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM02 に保存します。記録対応の変更前の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で ディスパッチ制御 の SRM表示 と RMF確認 を実施し SRMディスパッチ状態 の役割を確認します。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM02 の証跡を取る方法はどれですか。

    - A. D SRMを対象名なしで実行する。一覧の先頭行をSRM02の結果として記録する。
    - B. 前回保存したD SRMの結果を使う。今回のRMF III DELAYの結果と同一時点の証跡として比較する。
    - C. 保存済みのSRM02の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象SRM02についてD SRMの応答からIRA200Iを確認する。RMF III DELAYは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 採用理由: DはSRM表示で IRA200I を読みCPU使用率と待ちの主値として変更前の証跡を保存しSRM02に残します。
    動作の背景: 変更前の確認ではRMF確認を補助操作としSRMディスパッチ状態の変更対象と非対象の境界をRMFと対象SRM02で照合します。
    各選択肢の検討: SRM表示とRMF確認の役割を分けるとA: 先頭行はSRM02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でSRM表示を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でディスパッチ制御に使いません、D: IRA200Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM02 です。
    初出用語の定義: 変更前の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 変更前の確認 SRM02**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について変更前の証跡を保存し、SRM02のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM02のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM02のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM02のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
    ② ステップ2 の DELAY が画面・出力に表示されること
    ③ ステップ3 の IEE174I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 変更後の確認 SRM03 {#c38-i0280}
*分類: ディスパッチ制御*  ・  難易度: 中級

変更後の確認では ディスパッチ制御 の RMF確認 を主操作として SRM03 を判定します。反映値と残存値への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM03 に残します。変更後の確認を補助する CPU表示 では IEE174I を補助値として SRM03 へ保存します。主判定の変更後の確認ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM03 へ残します。証跡照合の変更後の確認ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM03 に保存します。記録対応の変更後の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で ディスパッチ制御 の RMF確認 と CPU表示 を用い 変更結果を検証 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。RMF で対象 SRM03 の CPU使用率と待ち を再現できる記録はどれですか。

    - A. D M=CPUで周辺状態を押さえる。その後にRMF III DELAYでRMFを確認して変更結果を検証する。 ✅
    - B. SRMディスパッチ状態の停止または再定義を実施する。その後にRMF III DELAYでRMFを採取する。
    - C. SAF連携のSAF RCとRACF RCを確認する。その値をディスパッチ制御のSRM03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正答の根拠: AはRMF確認で RMF を読みCPU使用率と待ちの主値として変更結果を検証しSRM03に残します。
    内部の仕組み: 変更後の確認ではCPU表示を補助操作としSRMディスパッチ状態の反映値と残存値をIEE174Iと対象SRM03で照合します。
    誤答を含む比較: RMF確認とCPU表示の役割を分けるとA: 周辺状態の後にRMFを確認する点でSRM03を判定できます、B: 変更前のCPU使用率と待ちを失う点でCPU表示の範囲を越えます、C: SAF連携の値ではRMFを確認できないうえに追加前提も不正な点でSRM03の値を示しません、D: 補助操作の成功ではRMFを確定できない点で変更後の確認に合いません。結論として変更後の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM03 です。
    用語定義: 変更後の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 変更後の確認 SRM03**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について変更結果を検証し、SRM03のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM03のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM03のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM03のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
    ② ステップ2 の IEE174I が画面・出力に表示されること
    ③ ステップ3 の IRA200I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 引継ぎ記録 SRM09 {#c38-i0281}
*分類: ディスパッチ制御*  ・  難易度: 中級

引継ぎ記録では ディスパッチ制御 の RMF確認 を主操作として SRM09 を判定します。次担当者が追跡できる証跡への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM09 に残します。引継ぎ記録を補助する CPU表示 では IEE174I を補助値として SRM09 へ保存します。主判定の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM09 へ残します。証跡照合の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM09 に保存します。記録対応の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で ディスパッチ制御 の RMF確認 と CPU表示 を用い 再現可能な記録を作成 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。RMF で対象 SRM09 の CPU使用率と待ち を再現できる記録はどれですか。

    - A. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。
    - B. RMF III DELAYを対象名なしで実行する。一覧の先頭行をSRM09の結果として記録する。
    - C. 対象名SRM09を指定してRMF III DELAYを実行する。応答中のRMFと時刻を保存する。D M=CPUで周辺状態を補完する。 ✅
    - D. 前回保存したRMF III DELAYの結果を使う。今回のD M=CPUの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 中級

    **解説:** 採用操作の理由: CはRMF確認で RMF を読みCPU使用率と待ちの主値として再現可能な記録を作成しSRM09に残します。
    製品内の仕組み: 引継ぎ記録ではCPU表示を補助操作としSRMディスパッチ状態の次担当者が追跡できる証跡をIEE174Iと対象SRM09で照合します。
    選択肢別の説明: RMF確認とCPU表示の役割を分けるとA: 補助操作の成功ではRMFを確定できない点でSRM09の値を示しません、B: 先頭行はSRM09と確定できない点で引継ぎ記録に合いません、C: RMFと時刻を保存する点でRMF確認に合います、D: 採取時刻が異なる点でディスパッチ制御に使いません。結論として引継ぎ記録のディスパッチ制御・ディスパッチ状態で判定する対象は SRM09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 引継ぎ記録 SRM09**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について再現可能な記録を作成し、SRM09のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM09のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM09のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM09のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
    ② ステップ2 の IEE174I が画面・出力に表示されること
    ③ ステップ3 の IRA200I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 復旧後の確認 SRM06 {#c38-i0282}
*分類: ディスパッチ制御*  ・  難易度: 中級

復旧後の確認では ディスパッチ制御 の RMF確認 を主操作として SRM06 を判定します。再発していないことを示す値への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM06 に残します。復旧後の確認を補助する CPU表示 では IEE174I を補助値として SRM06 へ保存します。主判定の復旧後の確認ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM06 へ残します。証跡照合の復旧後の確認ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM06 に保存します。記録対応の復旧後の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で ディスパッチ制御 の RMF確認 と CPU表示 の役割を分け 再発していないことを示す値 を調べます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM06 を誤判定しない進め方はどれですか。

    - A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をディスパッチ制御のSRM06にも適用する。
    - B. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SRM06へ引き継げるものとする。
    - C. RMF III DELAYを対象名なしで実行する。一覧の先頭行をSRM06の結果として記録する。
    - D. RMF III DELAYでRMFを取得してからD SRMでIRA200Iを照合する。SRM06のCPU使用率と待ちを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答内容: DはRMF確認で RMF を読みCPU使用率と待ちの主値として復旧後の安定性を確認しSRM06に残します。
    構成上の背景: 復旧後の確認ではCPU表示を補助操作としSRMディスパッチ状態の再発していないことを示す値をIEE174Iと対象SRM06で照合します。
    候補ごとの理由: RMF確認とCPU表示の役割を分けるとA: Cross Memoryの値ではRMFを確認できない点でCPU表示の範囲を越えます、B: 補助操作の成功ではRMFを確定できないうえに追加前提も不正な点でSRM06の値を示しません、C: 先頭行はSRM06と確定できない点で復旧後の確認に合いません、D: RMFとIRA200Iを順に照合する点でRMF確認に合います。結論として復旧後の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM06 です。
    初出用語: 復旧後の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 復旧後の確認 SRM06**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について復旧後の安定性を確認し、SRM06のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM06のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM06のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM06のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
    ② ステップ2 の IEE174I が画面・出力に表示されること
    ③ ステップ3 の IRA200I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 復旧準備 SRM05 {#c38-i0283}
*分類: ディスパッチ制御*  ・  難易度: 中級

復旧準備では ディスパッチ制御 の SRM表示 を主操作として SRM05 を判定します。再開前に必要な整合性への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM05 に残します。復旧準備を補助する RMF確認 では RMF を補助値として SRM05 へ保存します。主判定の復旧準備ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM05 へ残します。証跡照合の復旧準備ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM05 に保存します。記録対応の復旧準備ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で ディスパッチ制御 の SRM表示 と RMF確認 を組み合わせる際は SRMディスパッチ状態 がサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能という仕組みを前提にします。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IRA200I と CPU使用率と待ち を対象 SRM05 で確認する組合せはどれですか。

    - A. 前回保存したD SRMの結果を使う。今回のRMF III DELAYの結果と同一時点の証跡として比較する。
    - B. 保存済みのSRM05の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。
    - C. 変更を加えずD SRMを実行する。IRA200Iを保存する。差分はRMF III DELAYの結果と対象名で対応させる。 ✅
    - D. RMF III DELAYのRMFをCPU使用率と待ちの主判定に採用する。D SRMの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 中級

    **解説:** 選定理由: CはSRM表示で IRA200I を読みCPU使用率と待ちの主値として復旧条件を確認しSRM05に残します。
    処理の仕組み: 復旧準備ではRMF確認を補助操作としSRMディスパッチ状態の再開前に必要な整合性をRMFと対象SRM05で照合します。
    選択結果の内訳: SRM表示とRMF確認の役割を分けるとA: 採取時刻が異なる点でSRM表示を代替しません、B: 過去出力では今回の復旧準備を示せない点でディスパッチ制御に使いません、C: 変更前のIRA200Iを保存する点で正答です、D: RMFはIRA200Iを代替しないうえに追加前提も不正な点でSRM05を採用できません。結論として復旧準備のディスパッチ制御・ディスパッチ状態で判定する対象は SRM05 です。
    用語の説明: 復旧準備で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 復旧準備 SRM05**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について復旧条件を確認し、SRM05のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM05のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM05のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM05のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
    ② ステップ2 の DELAY が画面・出力に表示されること
    ③ ステップ3 の IEE174I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 構成監査 SRM08 {#c38-i0284}
*分類: ディスパッチ制御*  ・  難易度: 中級

構成監査では ディスパッチ制御 の SRM表示 を主操作として SRM08 を判定します。定義値と稼働値の一致への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM08 に残します。構成監査を補助する RMF確認 では RMF を補助値として SRM08 へ保存します。主判定の構成監査ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM08 へ残します。証跡照合の構成監査ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM08 に保存します。記録対応の構成監査ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で ディスパッチ制御 の SRM表示 と RMF確認 を実施し SRMディスパッチ状態 の役割を確認します。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM08 の証跡を取る方法はどれですか。

    - A. 保存済みのSRM08の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。
    - B. RMF III DELAYの結果だけでは確定しない。D SRMのIRA200Iを主証跡として構成差分を監査する。 ✅
    - C. RMF III DELAYのRMFをCPU使用率と待ちの主判定に採用する。D SRMの応答は採取対象から外す。
    - D. D M=CPUのIEE174IをIRA200Iと同義の成功表示として扱う。D SRMは実行しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 技術上の正答: BはSRM表示で IRA200I を読みCPU使用率と待ちの主値として構成差分を監査しSRM08に残します。
    実行時の背景: 構成監査ではRMF確認を補助操作としSRMディスパッチ状態の定義値と稼働値の一致をRMFと対象SRM08で照合します。
    四つの候補の理由: SRM表示とRMF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でディスパッチ制御に使いません、B: IRA200Iを主証跡として区別する点で正答です、C: RMFはIRA200Iを代替しない点でSRM08を採用できません、D: IEE174IとIRA200Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のディスパッチ制御・ディスパッチ状態で判定する対象は SRM08 です。
    初出語定義: 構成監査で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 構成監査 SRM08**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について構成差分を監査し、SRM08のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM08のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM08のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM08のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
    ② ステップ2 の DELAY が画面・出力に表示されること
    ③ ステップ3 の IEE174I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 通常状態の確認 SRM01 {#c38-i0285}
*分類: ディスパッチ制御*  ・  難易度: 中級

通常状態の確認では ディスパッチ制御 の CPU表示 を主操作として SRM01 を判定します。基準値と現在値の差への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM01 に残します。通常状態の確認を補助する SRM表示 では IRA200I を補助値として SRM01 へ保存します。主判定の通常状態の確認ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM01 へ残します。証跡照合の通常状態の確認ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM01 に保存します。記録対応の通常状態の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で ディスパッチ制御 の CPU表示 と SRM表示 を使い 通常状態を確定 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読み対象 SRM01 を切り分ける確認方法はどれですか。

    - A. D SRMのIRA200IをCPU使用率と待ちの主判定に採用する。D M=CPUの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. RMF III DELAYのRMFをIEE174Iと同義の成功表示として扱う。D M=CPUは実行しない。
    - C. D M=CPUを先に実行する。対象SRM01のIEE174IをCPU使用率と待ちとして記録する。続いてD SRMで同一対象を照合する。 ✅
    - D. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解の説明: CはCPU表示で IEE174I を読みCPU使用率と待ちの主値として通常状態を確定しSRM01に残します。
    背景・仕組み: 通常状態の確認ではSRM表示を補助操作としSRMディスパッチ状態の基準値と現在値の差をIRA200Iと対象SRM01で照合します。
    選択肢の理由: CPU表示とSRM表示の役割を分けるとA: IRA200IはIEE174Iを代替しないうえに追加前提も不正な点でSRMディスパッチ状態に使えません、B: RMFとIEE174Iは確認項目が異なる点でSRM01を採用できません、C: IEE174Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではCPU使用率と待ちを判定できない点で一次資料と一致しません。結論として通常状態の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM01 です。
    用語の初出定義: 通常状態の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 通常状態の確認 SRM01**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について通常状態を確定し、SRM01のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM01のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM01のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM01のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 障害切り分け SRM04 {#c38-i0286}
*分類: ディスパッチ制御*  ・  難易度: 中級

障害切り分けでは ディスパッチ制御 の CPU表示 を主操作として SRM04 を判定します。最初に失敗した処理への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM04 に残します。障害切り分けを補助する SRM表示 では IRA200I を補助値として SRM04 へ保存します。主判定の障害切り分けではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM04 へ残します。証跡照合の障害切り分けではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM04 に保存します。記録対応の障害切り分けではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで ディスパッチ制御 の CPU表示 と SRM表示 を照合し 最初に失敗した処理 を確かめます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読む前に対象 SRM04 へ行う確認はどれですか。

    - A. RMF III DELAYのRMFをIEE174Iと同義の成功表示として扱う。D M=CPUは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D M=CPUの出力でSRM04とIEE174Iが同じ応答にあることを確認する。CPU使用率と待ちをその応答から採取する。 ✅
    - C. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。
    - D. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい操作の説明: BはCPU表示で IEE174I を読みCPU使用率と待ちの主値として障害範囲を限定しSRM04に残します。
    技術的背景: 障害切り分けではSRM表示を補助操作としSRMディスパッチ状態の最初に失敗した処理をIRA200Iと対象SRM04で照合します。
    四択の評価: CPU表示とSRM表示の役割を分けるとA: RMFとIEE174Iは確認項目が異なるうえに追加前提も不正な点でSRM04を採用できません、B: SRM04とIEE174Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではCPU使用率と待ちを判定できない点で一次資料と一致しません、D: 入力記録だけではCPU使用率と待ちを証明できない点でCPU使用率と待ちを確認できません。結論として障害切り分けのディスパッチ制御・ディスパッチ状態で判定する対象は SRM04 です。
    初出語の意味: 障害切り分けで使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 障害切り分け SRM04**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について障害範囲を限定し、SRM04のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM04のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM04のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM04のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12




## z/OS System Programming > トレース診断

### DEQマクロ 割り込み確認 運用確認067 {#c38-i0287}
*分類: トレース診断*  ・  難易度: 中級

第六十七観点 トレース診断 の運用では DEQマクロ を表示、定義、証跡で確認します（第六十七観点）。第六十七観点 役割は ENQで取得した資源の直列化を解放し、後続処理へ資源を渡すマクロという範囲です（第六十七観点）。第六十七観点 IPCS VERBX LOGDATA出力 の値を SMF.MAN1 と合わせ、オペレーター応答漏れの防止を記録します（第六十七観点）。第六十七観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録067に残します（第六十七観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第六十七証跡です。トレース診断 の当日作業で SMF.MAN1 を追跡します。確認観点は DEQマクロ、割り込み確認、運用確認 です。SMF.MAN1 を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. PSW/割り込み の一般メモを採り、SMF.MAN1、メッセージID、時刻の対応を記録外に置き、zOSSP誤記067として調査範囲を狭める。
    - B. DEQマクロ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延067として扱う。
    - C. IPCS VERBX LOGDATA出力 と SMF.MAN1 を同一票へ記録し、DEQマクロ を zOSSP正067で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在067として残す。

    正解: **C** ／ 難易度: 中級

    **解説:** 第六十七観点 採用理由: Cは DEQマクロ の状態を表示値と定義の両方から確認するため、記録として妥当です（第六十七観点）。第六十七観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第六十七観点）。第六十七観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第六十七観点）。第六十七観点 用語確認: APFは許可ライブラリーの管理機能です（第六十七観点）。第六十七観点 PROGxxは動的なプログラム管理指定です（第六十七観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **DEQマクロ 割り込み確認 運用確認067**

    - 検証目的: DEQマクロ の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により DEQマクロ の値を確認し、対象の現在値を固定する。
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
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により DEQマクロ の値を確認し、定義と資料上の項目を照合する。
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
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により DEQマクロ の値を確認し、同じ対象として記録できることを確認する。
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
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### ISGENQマクロ 割り込み確認 運用確認017 {#c38-i0288}
*分類: トレース診断*  ・  難易度: 初級

第十七観点 トレース診断 で ISGENQマクロ は 割り込み確認 の対象です（第十七観点）。第十七観点 確認時には ENQ、DEQ、RESERVEの機能を統合し、31ビットと64ビットという性質を前提にします（第十七観点）。第十七観点 IPCS VERBX LOGDATA出力 と AUTH=CMDS を同じ証跡に置き、オペレーター応答漏れの防止を管理します（第十七観点）。第十七観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録017から再現します（第十七観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **ISGENQマクロ 割り込み確認 運用確認017**

    - 検証目的: ISGENQマクロ の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SDSF LOG

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ISGENQマクロ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.18.17 PROG,APF DISPLAY 916
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       2  MPRES1 SYS1.SVCLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ISGENQマクロ の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ISGENQマクロ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF,ENTRY=(1-5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.26.17 PROG,APF DISPLAY 966
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       5  MPRES1 ISF.SISFLPA
    ```

    画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


