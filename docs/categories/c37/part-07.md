---
search:
  exclude: true
---

# z/OS 3.1 Core Operations — 詳細 (7/7)

[← z/OS 3.1 Core Operations の概要へ戻る](index.md)


## z/OS 3.1 Core Operations > 結合機構確認

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


