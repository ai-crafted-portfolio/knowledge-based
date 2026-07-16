---
search:
  exclude: true
---

# DFSMS / IDCAMS / VSAM — 詳細 (6/6)

[← DFSMS / IDCAMS / VSAM の概要へ戻る](index.md)


## DFSMS / IDCAMS / VSAM > VSAM_CONCEPTS

### VSAM RLS (Record Level Sharing) {#c06-i0249}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

Coupling Facility 上のロック構造体を使った VSAM 共有更新方式。CICS/IMS/バッチ間の本格的データ共有を提供

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 探索追跡再のストレージ管理で VSAM RLS 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VSAM RLS 属性の出力を取らず探索追跡再のストレージ管理の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索追跡再の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して探索追跡再のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索追跡再のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡再正解では選択記号 B を採用し、正解名は探索追跡再正解です。探索追跡再根拠では VSAM RLS 属性 は「探索追跡再のストレージ管理に関係する定義値と表示行を照合する探索追跡再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は探索追跡再根拠です。探索追跡再追跡では VSAM RLS 属性の属性行と IDC0001I を合わせ、追跡名は探索追跡再追跡です。誤答側の問題点を分けます。 A: 探索追跡再不足は名称や説明だけに寄り、判定名は探索追跡再不足です。 B: 探索追跡再正答は対象出力と項目説明を結び、根拠名は探索追跡再正答です。 C: 探索追跡再欠落は戻り値や記録番号に寄り、欠落名は探索追跡再欠落です。 D: 探索追跡再流用は別カテゴリの確認であり、排除名は探索追跡再流用です。探索追跡再初出では VSAM RLS 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索追跡再初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **VSAM RLS (Record Level Sharing)**

    - 検証目的: 区切追跡のストレージ管理について、Coupling Facility 上のロック構造体を使った VSAM 共有更新方式。CICS/IMS/ バッチ間の本格的データ共有を提供に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030050の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切追跡のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    ```

    COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にVSAM RLS (Record Lを指定し、OSKB030050の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VSAM RLS (Record L
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VSAM RLS (Record L
    CASE OSKB030050
    SOURCE DFSMS
    ```

    VSAM RLS (Record LとOSKB030050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030050を同じ出力で読み、区切追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030050.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の VSAM RLS (Record L と OSKB030050 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

    ---

    **VSAM RLS (Record Level Sharing)**

    - 検証目的: 構文記録のストレージ管理について、Coupling Facility 上のロック構造体を使った VSAM 共有更新方式。CICS/IMS/ バッチ間の本格的データ共有を提供に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020121の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、構文記録のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    ```

    COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にVSAM RLS (Record Lを指定し、OSKB020121の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VSAM RLS (Record L
    CASE OSKB020121
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VSAM RLS (Record L
    CASE OSKB020121
    SOURCE DFSMS
    ```

    VSAM RLS (Record LとOSKB020121が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020121を同じ出力で読み、構文記録のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020121
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020121.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020121が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の VSAM RLS (Record L と OSKB020121 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### VSAM TVS (Transactional VSAM) {#c06-i0250}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

VSAM TVS (Transactional VSAM)は、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。RLS にトランザクション (UR) 整合性を加える機構。バッチでも RRS 連携でコミット/ロールバックが可能になる。「VSAM TVS (Transactional VSAM)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 上書追跡再のストレージ管理でストレージ管理の運用確認を行います。VSAM TVS 属性の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書追跡再のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず上書追跡再のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書追跡再の根拠を固定する。 ✅
    - D. VSAM TVS 属性の属性行を読まず上書追跡再のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡再正解では選択記号 C を採用し、正解名は上書追跡再正解です。上書追跡再根拠では VSAM TVS 属性 は「DFSMS で VSAM TVS 属性の扱いを記録する上書追跡再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は上書追跡再根拠です。上書追跡再受渡では VSAM TVS 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は上書追跡再受渡です。不適切な選択肢を整理します。 A: 上書追跡再流用は別カテゴリの確認であり、排除名は上書追跡再流用です。 B: 上書追跡再欠落は戻り値や記録番号に寄り、欠落名は上書追跡再欠落です。 C: 上書追跡再正答は対象出力と項目説明を結び、根拠名は上書追跡再正答です。 D: 上書追跡再不足は名称や説明だけに寄り、判定名は上書追跡再不足です。上書追跡再資料では VSAM TVS 属性の使い方を出典欄から追跡し、資料名は上書追跡再資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **VSAM TVS (Transactional VSAM)**

    - 検証目的: 展開記録のストレージ管理について、VSAM TVS (Transactional VSAM)は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020122の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開記録のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    ```

    COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にVSAM TVS (Transactを指定し、OSKB020122の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VSAM TVS (Transact
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VSAM TVS (Transact
    CASE OSKB020122
    SOURCE DFSMS
    ```

    VSAM TVS (TransactとOSKB020122が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020122を同じ出力で読み、展開記録のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020122.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020122が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の VSAM TVS (Transact と OSKB020122 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands




## その他

### その他（特定項目に紐づかないQA・手順） {#c06-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（1問）"
    **問題.** 出力照合のなどに関する VOLUMES(volser など)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず出力照合のなどの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力照合のなどの証跡として保存して根拠にする。
    - C. VOLUMES(volser など)の変更点を出力本文から切り離して出力照合のなどの承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、出力照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では VOLUMES(volser など) は「VOLUMES(volser など)の状態と出力メッセージを結び付ける出力照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では VOLUMES(volser など)の出力行と IDC3009I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明だけに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では VOLUMES(volser など)を DFSMS の確認記録に残し、対象名は出力照合対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（6件）"
    **VOLUMES(volser など)**

    - 検証目的: 呼出照合のなどについて、DFSMS IDCAMS VSAM の DEFINE_CLUSTER では、データセット定義、属性、AMS 出力を対応付けて確認します。DEFINE_CLUSTER は、DFSMSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010023の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出照合のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    ```

    COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にVOLUMES(volser など)を指定し、OSKB010023の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VOLUMES(volser など)
    CASE OSKB010023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VOLUMES(volser など)
    CASE OSKB010023
    SOURCE DFSMS
    ```

    VOLUMES(volser など)とOSKB010023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010023を同じ出力で読み、呼出照合のなどの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010023.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の VOLUMES(volser など) と OSKB010023 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **CONTROLPW ・ MASTERPW ・ UPDATEPW ・**

    - 検証目的: 比較照合の・ ・について、CONTROLPW / MASTERPW / UPDATEPW / READPW は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010034の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、比較照合の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    ```

    COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にCONTROLPW ・ MASTERを指定し、OSKB010034の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CONTROLPW ・ MASTER
    CASE OSKB010034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CONTROLPW ・ MASTER
    CASE OSKB010034
    SOURCE DFSMS
    ```

    CONTROLPW ・ MASTERとOSKB010034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010034を同じ出力で読み、比較照合の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010034.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の CONTROLPW ・ MASTER と OSKB010034 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **CLUSTER ・ AIX ・ PATH ・ GDG ・ NONVS**

    - 検証目的: 優先判定の・ ・ ・について、CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIAS は、DFSMS / IDCAMSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先判定の・ ・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    ```

    COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にCLUSTER ・ AIX ・ PAを指定し、OSKB010092の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CLUSTER ・ AIX ・ PA
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CLUSTER ・ AIX ・ PA
    CASE OSKB010092
    SOURCE DFSMS
    ```

    CLUSTER ・ AIX ・ PAとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010092を同じ出力で読み、優先判定の・ ・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010092.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の CLUSTER ・ AIX ・ PA と OSKB010092 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **Space Allocation (Avg ・ Primary ・**

    - 検証目的: 条件追跡の・について、Space Allocation (Avg / Primary / Secondary)は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、条件追跡の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    ```

    COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にSpace Allocation (を指定し、OSKB020049の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Space Allocation (
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Space Allocation (
    CASE OSKB020049
    SOURCE DFSMS
    ```

    Space Allocation (とOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020049を同じ出力で読み、条件追跡の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020049.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Space Allocation ( と OSKB020049 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **VSAM CISZ ・ KEYS ・ FREESPACE ・ SHA**

    - 検証目的: 比較追跡の・ ・について、VSAM CISZ / KEYS / FREESPACE / SHAREOPTIONS は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で構成値やオプに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較追跡の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    ```

    COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にVSAM CISZ ・ KEYS ・を指定し、OSKB020054の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VSAM CISZ ・ KEYS ・
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VSAM CISZ ・ KEYS ・
    CASE OSKB020054
    SOURCE DFSMS
    ```

    VSAM CISZ ・ KEYS ・とOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020054を同じ出力で読み、比較追跡の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020054.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の VSAM CISZ ・ KEYS ・ と OSKB020054 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Auto Migrate ・ Auto Backup ・ Auto**

    - 検証目的: 呼出検査の・について、Auto Migrate / Auto Backup / Auto Dumpは、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、呼出検査の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    ```

    COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にAuto Migrate ・ Autを指定し、OSKB020063の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Auto Migrate ・ Aut
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Auto Migrate ・ Aut
    CASE OSKB020063
    SOURCE DFSMS
    ```

    Auto Migrate ・ AutとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020063を同じ出力で読み、呼出検査の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020063.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Auto Migrate ・ Aut と OSKB020063 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

