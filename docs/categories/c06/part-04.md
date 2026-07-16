---
search:
  exclude: true
---

# DFSMS / IDCAMS / VSAM — 詳細 (4/6)

[← DFSMS / IDCAMS / VSAM の概要へ戻る](index.md)


## DFSMS / IDCAMS / VSAM > ICF

### VVR (VSAM Volume Record) {#c06-i0149}
*分類: ICF*  ・  難易度: 上級

VVR (VSAM Volume Record)は、DFSMS / IDCAMS / VSAMのICFで機能名、見出し、または確認対象として参照する項目です。VVDS 内の VSAM ボリュームレコード。CISZ, FREESPACE, HURBA, HARBA, 統計を保持する。「VVR (VSAM Volume Record)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 優先照合再のストレージ管理に関する VVR 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先照合再のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先照合再のストレージ管理の証跡として保存して根拠にする。
    - C. VVR 属性の変更点を出力本文から切り離して優先照合再のストレージ管理の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、優先照合再の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合再正解では選択記号 D を採用し、正解名は優先照合再正解です。優先照合再根拠では VVR 属性 は「VVR 属性の状態と出力メッセージを結び付ける優先照合再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先照合再根拠です。優先照合再保存では VVR 属性の出力行と IDC3009I を一緒に残し、保存名は優先照合再保存です。選択肢ごとの違いを示します。 A: 優先照合再欠落は戻り値や記録番号に寄り、欠落名は優先照合再欠落です。 B: 優先照合再流用は別カテゴリの確認であり、排除名は優先照合再流用です。 C: 優先照合再不足は名称や説明だけに寄り、判定名は優先照合再不足です。 D: 優先照合再正答は対象出力と項目説明を結び、根拠名は優先照合再正答です。優先照合再対象では VVR 属性を DFSMS の確認記録に残し、対象名は優先照合再対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **VVR (VSAM Volume Record)**

    - 検証目的: 上書整理のストレージ管理について、VVR (VSAM Volume Record)は、DFSMS / IDCAMS / VSAM の ICF で機能名、見出し、または確認対象として参照する項目です。VVDS 内のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVVR (VSAM Volume Rを指定し、OSKB020107の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VVR (VSAM Volume R
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VVR (VSAM Volume R
    CASE OSKB020107
    SOURCE DFSMS
    ```

    VVR (VSAM Volume RとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020107を同じ出力で読み、上書整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020107.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の VVR (VSAM Volume R と OSKB020107 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > IMPORT

### IMPORT 基本 {#c06-i0150}
*分類: IMPORT*  ・  難易度: 上級

IMPORT 基本は、DFSMS / IDCAMS / VSAMのIMPORTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 呼出分離の基本でストレージ管理の運用確認を行います。IMPORT 基本の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出分離の基本を確認した扱いにする。
    - B. IDC0001I の有無を確認せず呼出分離の基本を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出分離の根拠にする。 ✅
    - D. IMPORT 基本の属性行を読まず呼出分離の基本の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では IMPORT 基本 は「DFSMS で IMPORT 基本の扱いを記録する呼出分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では IMPORT 基本の表示結果と IDC0001I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明だけに寄り、判定名は呼出分離不足です。呼出分離資料では IMPORT 基本の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **IMPORT 基本**

    - 検証目的: 復旧確認の基本について、IMPORT 基本は、DFSMS / IDCAMS / VSAM の IMPORT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、復旧確認の基本の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にIMPORT 基本を指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND IMPORT 基本
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM IMPORT 基本
    CASE OSKB020018
    SOURCE DFSMS
    ```

    IMPORT 基本とOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020018を同じ出力で読み、復旧確認の基本の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020018.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の IMPORT 基本 と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### INTOEMPTY {#c06-i0151}
*分類: IMPORT*  ・  難易度: 上級

事前に空のクラスターを準備し、その属性で IMPORT する。属性を IMPORT 元から維持したくない場合に使う

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 置換分離のストレージ管理に関する INTOEMPTY の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換分離のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換分離のストレージ管理の証跡として保存して根拠にする。
    - C. INTOEMPTY の変更点を出力本文から切り離して置換分離のストレージ管理の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、置換分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では INTOEMPTY は「INTOEMPTY の状態と出力メッセージを結び付ける置換分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では INTOEMPTY の出力行と IDC0001I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明だけに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では INTOEMPTY を DFSMS の確認記録に残し、対象名は置換分離対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **INTOEMPTY**

    - 検証目的: 監査確認のストレージ管理について、事前に空のクラスターを準備し、その属性で IMPORT する。属性を IMPORT 元から維持したくない場合に使うに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査確認のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にINTOEMPTYを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND INTOEMPTY
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM INTOEMPTY
    CASE OSKB020019
    SOURCE DFSMS
    ```

    INTOEMPTYとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020019を同じ出力で読み、監査確認のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020019.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の INTOEMPTY と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### OBJECTS (IMPORT) {#c06-i0152}
*分類: IMPORT*  ・  難易度: 上級

OBJECTS (IMPORT)は、DFSMS / IDCAMS / VSAMのIMPORTで機能名、見出し、または確認対象として参照する項目です。再構築時の個別属性上書き。NEWNAME, VOLUMES, FILE, KEYRANGES 等を指定可能。「OBJECTS (IMPORT)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 終端分離のストレージ管理に関係する OBJECTS (IMPORT)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、終端分離の採否を説明欄に結び付ける。 ✅
    - B. OBJECTS (IMPORT)の名称と担当者名だけを残して終端分離のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端分離のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず終端分離のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では OBJECTS (IMPORT) は「OBJECTS (IMPORT)の用途をストレージ管理の表示で確認する終端分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では DFSMS の OBJECTS (IMPORT)と IDC3009I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明だけに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では OBJECTS (IMPORT)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **OBJECTS (IMPORT)**

    - 検証目的: 変更確認のストレージ管理について、OBJECTS (IMPORT)は、DFSMS / IDCAMS / VSAM の IMPORT で機能名、見出し、または確認対象として参照する項目です。再構築時の個別属性上書きに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更確認のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にOBJECTS (IMPORT)を指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND OBJECTS (IMPORT)
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM OBJECTS (IMPORT)
    CASE OSKB020020
    SOURCE DFSMS
    ```

    OBJECTS (IMPORT)とOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020020を同じ出力で読み、変更確認のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020020.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の OBJECTS (IMPORT) と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > IMPORTRA

### IMPORTRA (リカバリ用) {#c06-i0153}
*分類: IMPORTRA*  ・  難易度: 上級

EXPORTRA で取得した RA データからカタログを再構築する旧 IDCAMS コマンド。現行は ICF DIAGNOSE/REPRO で代替されることが多い

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 上書分離のリカバリ用でストレージ管理の運用確認を行います。IMPORTRA (リカバリ用)の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書分離のリカバリ用を確認した扱いにする。
    - B. IDC0005I の有無を確認せず上書分離のリカバリ用を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書分離の確認にする。 ✅
    - D. IMPORTRA (リカバリ用)の属性行を読まず上書分離のリカバリ用の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では IMPORTRA (リカバリ用) は「DFSMS で IMPORTRA (リカバリ用)の扱いを記録する上書分離項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では IMPORTRA (リカバリ用)の表示結果と IDC0005I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明だけに寄り、判定名は上書分離不足です。上書分離資料では IMPORTRA (リカバリ用)の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **IMPORTRA (リカバリ用)**

    - 検証目的: 展開照合のリカバリ用について、EXPORTRA で取得した RA データからカタログを再構築する旧 IDCAMS コマンド。現行は ICF DIAGNOSE/REPRO で代替されることが多いに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、展開照合のリカバリ用の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にIMPORTRA (リカバリ用)を指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND IMPORTRA (リカバリ用)
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM IMPORTRA (リカバリ用)
    CASE OSKB020022
    SOURCE DFSMS
    ```

    IMPORTRA (リカバリ用)とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020022を同じ出力で読み、展開照合のリカバリ用の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB020022.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の IMPORTRA (リカバリ用) と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > LISTCAT

### ALL {#c06-i0154}
*分類: LISTCAT*  ・  難易度: 上級

ALLは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 置換整理のストレージ管理に関する ALL の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換整理のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換整理のストレージ管理の証跡として保存して根拠にする。
    - C. ALL の変更点を出力本文から切り離して置換整理のストレージ管理の承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を置換整理で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では ALL は「ALL の状態と出力メッセージを結び付ける置換整理項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では ALL の出力行と IDC0001I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明だけに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では ALL を DFSMS の確認記録に残し、対象名は置換整理対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **ALL**

    - 検証目的: 監査判定のストレージ管理について、ALL は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010099の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にALLを指定し、OSKB010099の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND ALL
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM ALL
    CASE OSKB010099
    SOURCE DFSMS
    ```

    ALLとOSKB010099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010099を同じ出力で読み、監査判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010099
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010099.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の ALL と OSKB010099 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### ALLOCATION {#c06-i0155}
*分類: LISTCAT*  ・  難易度: 上級

ALLOCATIONは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 監査判定のストレージ管理でストレージ管理の運用確認を行います。ALLOCATION の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査判定のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず監査判定のストレージ管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査判定の確認にする。 ✅
    - D. ALLOCATION の属性行を読まず監査判定のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では ALLOCATION は「DFSMS で ALLOCATION の扱いを記録する監査判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では ALLOCATION の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明だけに寄り、判定名は監査判定不足です。監査判定資料では ALLOCATION の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **ALLOCATION**

    - 検証目的: 比較判定のストレージ管理について、ALLOCATION は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にALLOCATIONを指定し、OSKB010094の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND ALLOCATION
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM ALLOCATION
    CASE OSKB010094
    SOURCE DFSMS
    ```

    ALLOCATIONとOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010094を同じ出力で読み、比較判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010094.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の ALLOCATION と OSKB010094 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### CATALOG(catname) {#c06-i0156}
*分類: LISTCAT*  ・  難易度: 上級

CATALOG(catname)は、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。問い合わせ先カタログを明示。エイリアス解決を経ずに特定カタログを直接見たいときに使用。「CATALOG(catname)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands


### CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIAS {#c06-i0157}
*分類: LISTCAT*  ・  難易度: 上級

CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIASは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。対象タイプを限定するフィルタ。複数並べて指定可能。「CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIAS」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 警告判定の・ ・ ・に関係する CLUSTER 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、警告判定の採否を説明欄に結び付ける。 ✅
    - B. CLUSTER 属性の名称と担当者名だけを残して警告判定の・ ・ ・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で警告判定の・ ・ ・を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず警告判定の・ ・ ・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では CLUSTER 属性 は「CLUSTER 属性の用途をストレージ管理の表示で確認する警告判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では DFSMS の CLUSTER 属性と IDC3009I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明だけに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では CLUSTER 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200



### CREATION / EXPIRATION {#c06-i0158}
*分類: LISTCAT*  ・  難易度: 上級

CREATION / EXPIRATIONは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。作成日 (CREATION) と有効期限 (EXPIRATION) を出力。世代管理の見える化に有用。「CREATION / EXPIRATION」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 変更判定の・に関する CREATION 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず変更判定の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更判定の・の証跡として保存して根拠にする。
    - C. CREATION 属性の変更点を出力本文から切り離して変更判定の・の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、変更判定の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では CREATION 属性 は「CREATION 属性の状態と出力メッセージを結び付ける変更判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では CREATION 属性の出力行と IDC3009I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明だけに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では CREATION 属性を DFSMS の確認記録に残し、対象名は変更判定対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **CREATION ・ EXPIRATION**

    - 検証目的: 順序判定の・について、CREATION / EXPIRATION は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。作成日 (Cに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010095の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、順序判定の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCREATION ・ EXPIRATを指定し、OSKB010095の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CREATION ・ EXPIRAT
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CREATION ・ EXPIRAT
    CASE OSKB010095
    SOURCE DFSMS
    ```

    CREATION ・ EXPIRATとOSKB010095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010095を同じ出力で読み、順序判定の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010095.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の CREATION ・ EXPIRAT と OSKB010095 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### ENTRIES(name) / LEVEL(prefix) {#c06-i0159}
*分類: LISTCAT*  ・  難易度: 上級

ENTRIES(name) / LEVEL(prefix)は、DFSMS / IDCAMS / VSAMのLISTCATで確認する項目です。個別エントリ列挙 (ENTRIES) と、HLQ を含むプレフィックスからの一括列挙 (LEVEL)。LEVEL は再帰的

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 値域判定の・に関する ENTRIES 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず値域判定の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域判定の・の証跡として保存して根拠にする。
    - C. ENTRIES 属性の変更点を出力本文から切り離して値域判定の・の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、値域判定の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では ENTRIES 属性 は「ENTRIES 属性の状態と出力メッセージを結び付ける値域判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では ENTRIES 属性の出力行と IDC0001I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明だけに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では ENTRIES 属性を DFSMS の確認記録に残し、対象名は値域判定対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **ENTRIES(name) ・ LEVEL(prefix)**

    - 検証目的: 変更確認の・について、ENTRIES(name) / LEVEL(prefix)は、DFSMS / IDCAMS / VSAM の LISTCAT で確認する項目です。個別エントリ列挙 (ENTRIEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030020の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、変更確認の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にENTRIES(name) ・ LEを指定し、OSKB030020の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND ENTRIES(name) ・ LE
    CASE OSKB030020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM ENTRIES(name) ・ LE
    CASE OSKB030020
    SOURCE DFSMS
    ```

    ENTRIES(name) ・ LEとOSKB030020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030020を同じ出力で読み、変更確認の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030020
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030020.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の ENTRIES(name) ・ LE と OSKB030020 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **ENTRIES(name) ・ LEVEL(prefix)**

    - 検証目的: 範囲判定の・について、ENTRIES(name) / LEVEL(prefix)は、DFSMS / IDCAMS / VSAM の LISTCAT で確認する項目です。個別エントリ列挙 (ENTRIEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010091の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、範囲判定の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にENTRIES(name) ・ LEを指定し、OSKB010091の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND ENTRIES(name) ・ LE
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM ENTRIES(name) ・ LE
    CASE OSKB010091
    SOURCE DFSMS
    ```

    ENTRIES(name) ・ LEとOSKB010091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010091を同じ出力で読み、範囲判定の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010091.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の ENTRIES(name) ・ LE と OSKB010091 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### HISTORY {#c06-i0160}
*分類: LISTCAT*  ・  難易度: 上級

HISTORYは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 構文整理のストレージ管理に関係する HISTORY の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文整理で再確認できる形にする。 ✅
    - B. HISTORY の名称と担当者名だけを残して構文整理のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で構文整理のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず構文整理のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では HISTORY は「HISTORY の用途をストレージ管理の表示で確認する構文整理項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では DFSMS の HISTORY と IDC0001I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明だけに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では HISTORY を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **HISTORY**

    - 検証目的: 構文照合のストレージ管理について、HISTORY は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030021の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、構文照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にHISTORYを指定し、OSKB030021の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND HISTORY
    CASE OSKB030021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM HISTORY
    CASE OSKB030021
    SOURCE DFSMS
    ```

    HISTORYとOSKB030021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030021を同じ出力で読み、構文照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030021
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030021.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の HISTORY と OSKB030021 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **HISTORY**

    - 検証目的: 値域判定のストレージ管理について、HISTORY は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010096の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、値域判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にHISTORYを指定し、OSKB010096の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND HISTORY
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM HISTORY
    CASE OSKB010096
    SOURCE DFSMS
    ```

    HISTORYとOSKB010096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010096を同じ出力で読み、値域判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010096
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010096.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の HISTORY と OSKB010096 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### LISTCAT 基本 {#c06-i0161}
*分類: LISTCAT*  ・  難易度: 上級

LISTCAT 基本は、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 順序判定の基本でストレージ管理の運用確認を行います。LISTCAT 基本の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で順序判定の基本を確認した扱いにする。
    - B. IDC0001I の有無を確認せず順序判定の基本を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序判定の根拠にする。 ✅
    - D. LISTCAT 基本の属性行を読まず順序判定の基本の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では LISTCAT 基本 は「DFSMS で LISTCAT 基本の扱いを記録する順序判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では LISTCAT 基本の表示結果と IDC0001I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明だけに寄り、判定名は順序判定不足です。順序判定資料では LISTCAT 基本の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **LISTCAT 基本**

    - 検証目的: 区切判定の基本について、LISTCAT 基本は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010090の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切判定の基本の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にLISTCAT 基本を指定し、OSKB010090の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND LISTCAT 基本
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM LISTCAT 基本
    CASE OSKB010090
    SOURCE DFSMS
    ```

    LISTCAT 基本とOSKB010090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010090を同じ出力で読み、区切判定の基本の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010090.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の LISTCAT 基本 と OSKB010090 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### NAMES {#c06-i0162}
*分類: LISTCAT*  ・  難易度: 上級

NAMESは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 復旧判定のストレージ管理で NAMES の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NAMES の出力を取らず復旧判定のストレージ管理の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧判定として引き継ぐ。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して復旧判定のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧判定のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では NAMES は「復旧判定のストレージ管理に関係する定義値と表示行を照合する復旧判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では NAMES の属性行と IDC0001I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明だけに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では NAMES を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **NAMES**

    - 検証目的: 記録判定のストレージ管理について、NAMES は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010093の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にNAMESを指定し、OSKB010093の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND NAMES
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM NAMES
    CASE OSKB010093
    SOURCE DFSMS
    ```

    NAMESとOSKB010093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010093を同じ出力で読み、記録判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010093.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の NAMES と OSKB010093 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### OUTFILE(ddname) {#c06-i0163}
*分類: LISTCAT*  ・  難易度: 上級

OUTFILE(ddname)は、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 終端整理のストレージ管理に関係する OUTFILE(ddname)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、終端整理の証跡として残す。 ✅
    - B. OUTFILE(ddname)の名称と担当者名だけを残して終端整理のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端整理のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず終端整理のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では OUTFILE(ddname) は「OUTFILE(ddname)の用途をストレージ管理の表示で確認する終端整理項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では DFSMS の OUTFILE(ddname)と IDC0001I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明だけに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では OUTFILE(ddname)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **OUTFILE(ddname)**

    - 検証目的: 変更判定のストレージ管理について、OUTFILE(ddname)は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010100の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、変更判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にOUTFILE(ddname)を指定し、OSKB010100の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND OUTFILE(ddname)
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM OUTFILE(ddname)
    CASE OSKB010100
    SOURCE DFSMS
    ```

    OUTFILE(ddname)とOSKB010100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010100を同じ出力で読み、変更判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010100
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010100.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の OUTFILE(ddname) と OSKB010100 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### SPACE {#c06-i0164}
*分類: LISTCAT*  ・  難易度: 上級

SPACEは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 展開整理のストレージ管理で SPACE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SPACE の出力を取らず展開整理のストレージ管理の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開整理の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して展開整理のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開整理のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では SPACE は「展開整理のストレージ管理に関係する定義値と表示行を照合する展開整理項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では SPACE の属性行と IDC0001I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明だけに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では SPACE を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開整理初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **SPACE**

    - 検証目的: 警告判定のストレージ管理について、SPACE は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010097の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、警告判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にSPACEを指定し、OSKB010097の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND SPACE
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM SPACE
    CASE OSKB010097
    SOURCE DFSMS
    ```

    SPACEとOSKB010097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010097を同じ出力で読み、警告判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB010097
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB010097.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB010097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の SPACE と OSKB010097 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB010097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### VOLUME {#c06-i0165}
*分類: LISTCAT*  ・  難易度: 上級

VOLUMEは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。エントリが存在するボリュームを表示。ボリューム整理の調査に有効。「VOLUME」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 呼出整理のストレージ管理でストレージ管理の運用確認を行います。VOLUME の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出整理のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず呼出整理のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出整理の根拠を固定する。 ✅
    - D. VOLUME の属性行を読まず呼出整理のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では VOLUME は「DFSMS で VOLUME の扱いを記録する呼出整理項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では VOLUME の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明だけに寄り、判定名は呼出整理不足です。呼出整理資料では VOLUME の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **VOLUME**

    - 検証目的: 復旧判定のストレージ管理について、VOLUME は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。エントリが存在するボリュームを表示。ボリュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010098の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVOLUMEを指定し、OSKB010098の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VOLUME
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VOLUME
    CASE OSKB010098
    SOURCE DFSMS
    ```

    VOLUMEとOSKB010098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010098を同じ出力で読み、復旧判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010098
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010098.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の VOLUME と OSKB010098 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > PRINT

### CHARACTER {#c06-i0166}
*分類: PRINT*  ・  難易度: 上級

CHARACTERは、DFSMS / IDCAMS / VSAMのPRINTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 展開記録のストレージ管理で CHARACTER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CHARACTER の出力を取らず展開記録のストレージ管理の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開記録として引き継ぐ。 ✅
    - C. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)を省略して展開記録のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開記録のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では CHARACTER は「展開記録のストレージ管理に関係する定義値と表示行を照合する展開記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では CHARACTER の属性行と IDC0005I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明だけに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では CHARACTER を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開記録初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **CHARACTER**

    - 検証目的: 警告整理のストレージ管理について、CHARACTER は、DFSMS / IDCAMS / VSAM の PRINT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010117の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、警告整理のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にCHARACTERを指定し、OSKB010117の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CHARACTER
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CHARACTER
    CASE OSKB010117
    SOURCE DFSMS
    ```

    CHARACTERとOSKB010117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010117を同じ出力で読み、警告整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010117
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010117.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の CHARACTER と OSKB010117 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### DUMP (既定) {#c06-i0167}
*分類: PRINT*  ・  難易度: 上級

DUMP (既定)は、DFSMS / IDCAMS / VSAMのPRINTで機能名、見出し、または確認対象として参照する項目です。16 進と文字を併記。最も情報量が多くトラブルシュート向け。「DUMP (既定)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 置換記録の既定に関する DUMP (既定)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換記録の既定の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換記録の既定の証跡として保存して根拠にする。
    - C. DUMP (既定)の変更点を出力本文から切り離して置換記録の既定の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、置換記録の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では DUMP (既定) は「DUMP (既定)の状態と出力メッセージを結び付ける置換記録項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では DUMP (既定)の出力行と IDC3009I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明だけに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では DUMP (既定)を DFSMS の確認記録に残し、対象名は置換記録対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **DUMP (既定)**

    - 検証目的: 監査整理の既定について、DUMP (既定)は、DFSMS / IDCAMS / VSAM の PRINT で機能名、見出し、または確認対象として参照する項目です。16 進と文字を併記。最も情報量が多くトに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010119の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査整理の既定の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にDUMP (既定)を指定し、OSKB010119の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND DUMP (既定)
    CASE OSKB010119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM DUMP (既定)
    CASE OSKB010119
    SOURCE DFSMS
    ```

    DUMP (既定)とOSKB010119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010119を同じ出力で読み、監査整理の既定の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010119
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010119.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の DUMP (既定) と OSKB010119 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### FROMKEY/TOKEY/COUNT/SKIP (PRINT) {#c06-i0168}
*分類: PRINT*  ・  難易度: 上級

FROMKEY/TOKEY/COUNT/SKIP (PRINT)は、DFSMS / IDCAMS / VSAMのPRINTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 終端記録の・ ・ ・に関係する FROMKEY 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端記録で再確認できる形にする。 ✅
    - B. FROMKEY 属性の名称と担当者名だけを残して終端記録の・ ・ ・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端記録の・ ・ ・を確認し同じ証跡として扱ったことにする。
    - D. IDC0005I の有無を見ず終端記録の・ ・ ・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では FROMKEY 属性 は「FROMKEY 属性の用途をストレージ管理の表示で確認する終端記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では DFSMS の FROMKEY 属性と IDC0005I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明だけに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では FROMKEY 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **FROMKEY ・ TOKEY ・ COUNT ・ SKIP (PRINT)**

    - 検証目的: 変更整理の・ ・ ・について、FROMKEY/TOKEY/COUNT/SKIP (PRINT)は、DFSMS / IDCAMS / VSAM の PRINT で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010120の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、変更整理の・ ・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にFROMKEY ・ TOKEY ・ を指定し、OSKB010120の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND FROMKEY ・ TOKEY ・ 
    CASE OSKB010120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM FROMKEY ・ TOKEY ・ 
    CASE OSKB010120
    SOURCE DFSMS
    ```

    FROMKEY ・ TOKEY ・ とOSKB010120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010120を同じ出力で読み、変更整理の・ ・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010120
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010120.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の FROMKEY ・ TOKEY ・  と OSKB010120 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### HEX {#c06-i0169}
*分類: PRINT*  ・  難易度: 上級

HEXは、DFSMS / IDCAMS / VSAMのPRINTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 呼出記録のストレージ管理でストレージ管理の運用確認を行います。HEX の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出記録のストレージ管理を確認した扱いにする。
    - B. IDC0005I の有無を確認せず呼出記録のストレージ管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出記録の確認にする。 ✅
    - D. HEX の属性行を読まず呼出記録のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では HEX は「DFSMS で HEX の扱いを記録する呼出記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では HEX の表示結果と IDC0005I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明だけに寄り、判定名は呼出記録不足です。呼出記録資料では HEX の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **HEX**

    - 検証目的: 復旧整理のストレージ管理について、HEX は、DFSMS / IDCAMS / VSAM の PRINT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010118の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、復旧整理のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にHEXを指定し、OSKB010118の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND HEX
    CASE OSKB010118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM HEX
    CASE OSKB010118
    SOURCE DFSMS
    ```

    HEXとOSKB010118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010118を同じ出力で読み、復旧整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010118
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010118.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の HEX と OSKB010118 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### INFILE(ddname) / INDATASET(name) {#c06-i0170}
*分類: PRINT*  ・  難易度: 上級

INFILE(ddname) / INDATASET(name)は、DFSMS / IDCAMS / VSAMのPRINTで機能名、見出し、または確認対象として参照する項目です。入力指定。REPRO と同じ形式。「INFILE(ddname) / INDATASET(name)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 構文記録の・に関係する INFILE 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、構文記録の採否を説明欄に結び付ける。 ✅
    - B. INFILE 属性の名称と担当者名だけを残して構文記録の・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で構文記録の・を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず構文記録の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では INFILE 属性 は「INFILE 属性の用途をストレージ管理の表示で確認する構文記録項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では DFSMS の INFILE 属性と IDC3009I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明だけに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では INFILE 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **INFILE(ddname) ・ INDATASET(name)**

    - 検証目的: 終端照合の・について、INFILE(ddname) / INDATASET(name)は、DFSMS / IDCAMS / VSAM の PRINT で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030025の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端照合の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にINFILE(ddname) ・ Iを指定し、OSKB030025の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND INFILE(ddname) ・ I
    CASE OSKB030025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM INFILE(ddname) ・ I
    CASE OSKB030025
    SOURCE DFSMS
    ```

    INFILE(ddname) ・ IとOSKB030025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030025を同じ出力で読み、終端照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB030025
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB030025.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB030025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の INFILE(ddname) ・ I と OSKB030025 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB030025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **INFILE(ddname) ・ INDATASET(name)**

    - 検証目的: 値域整理の・について、INFILE(ddname) / INDATASET(name)は、DFSMS / IDCAMS / VSAM の PRINT で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010116の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域整理の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にINFILE(ddname) ・ Iを指定し、OSKB010116の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND INFILE(ddname) ・ I
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM INFILE(ddname) ・ I
    CASE OSKB010116
    SOURCE DFSMS
    ```

    INFILE(ddname) ・ IとOSKB010116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010116を同じ出力で読み、値域整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010116.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の INFILE(ddname) ・ I と OSKB010116 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### PRINT 基本 {#c06-i0171}
*分類: PRINT*  ・  難易度: 上級

データセット内容を SYSPRINT に印刷する IDCAMS コマンド。VSAM/QSAM の内容ダンプに使用

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 変更整理の基本に関する PRINT 基本の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)の結果を残さず変更整理の基本の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更整理の基本の証跡として保存して根拠にする。
    - C. PRINT 基本の変更点を出力本文から切り離して変更整理の基本の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0005I を読み、変更整理の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では PRINT 基本 は「PRINT 基本の状態と出力メッセージを結び付ける変更整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では PRINT 基本の出力行と IDC0005I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明だけに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では PRINT 基本を DFSMS の確認記録に残し、対象名は変更整理対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **PRINT 基本**

    - 検証目的: 順序整理の基本について、データセット内容を SYSPRINT に印刷する IDCAMS コマンド。VSAM/QSAM の内容ダンプに使用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010115の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、順序整理の基本の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にPRINT 基本を指定し、OSKB010115の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND PRINT 基本
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM PRINT 基本
    CASE OSKB010115
    SOURCE DFSMS
    ```

    PRINT 基本とOSKB010115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010115を同じ出力で読み、順序整理の基本の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010115.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の PRINT 基本 と OSKB010115 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > REPRO

### COUNT(n) {#c06-i0172}
*分類: REPRO*  ・  難易度: 上級

COUNT(n)は、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 記録整理のストレージ管理に関係する COUNT(n)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録整理で再確認できる形にする。 ✅
    - B. COUNT(n)の名称と担当者名だけを残して記録整理のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で記録整理のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0005I の有無を見ず記録整理のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では COUNT(n) は「COUNT(n)の用途をストレージ管理の表示で確認する記録整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では DFSMS の COUNT(n)と IDC0005I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明だけに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では COUNT(n)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **COUNT(n)**

    - 検証目的: 出力整理のストレージ管理について、COUNT(n)は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010108の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、出力整理のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にCOUNT(n)を指定し、OSKB010108の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND COUNT(n)
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM COUNT(n)
    CASE OSKB010108
    SOURCE DFSMS
    ```

    COUNT(n)とOSKB010108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010108を同じ出力で読み、出力整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010108.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の COUNT(n) と OSKB010108 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### FROMADDRESS / TOADDRESS {#c06-i0173}
*分類: REPRO*  ・  難易度: 上級

FROMADDRESS / TOADDRESSは、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 範囲整理の・でストレージ管理の運用確認を行います。FROMADDRESS 属性の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で範囲整理の・を確認した扱いにする。
    - B. IDC0005I の有無を確認せず範囲整理の・を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲整理の確認にする。 ✅
    - D. FROMADDRESS 属性の属性行を読まず範囲整理の・の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では FROMADDRESS 属性 は「DFSMS で FROMADDRESS 属性の扱いを記録する範囲整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では FROMADDRESS 属性の表示結果と IDC0005I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明だけに寄り、判定名は範囲整理不足です。範囲整理資料では FROMADDRESS 属性の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **FROMADDRESS ・ TOADDRESS**

    - 検証目的: 呼出照合の・について、FROMADDRESS / TOADDRESS は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030023の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、呼出照合の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にFROMADDRESS ・ TOADを指定し、OSKB030023の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND FROMADDRESS ・ TOAD
    CASE OSKB030023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM FROMADDRESS ・ TOAD
    CASE OSKB030023
    SOURCE DFSMS
    ```

    FROMADDRESS ・ TOADとOSKB030023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB030023を同じ出力で読み、呼出照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB030023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB030023.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB030023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の FROMADDRESS ・ TOAD と OSKB030023 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB030023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **FROMADDRESS ・ TOADDRESS**

    - 検証目的: 探索整理の・について、FROMADDRESS / TOADDRESS は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010106の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、探索整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にFROMADDRESS ・ TOADを指定し、OSKB010106の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND FROMADDRESS ・ TOAD
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM FROMADDRESS ・ TOAD
    CASE OSKB010106
    SOURCE DFSMS
    ```

    FROMADDRESS ・ TOADとOSKB010106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010106を同じ出力で読み、探索整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010106.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の FROMADDRESS ・ TOAD と OSKB010106 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### FROMKEY / TOKEY {#c06-i0174}
*分類: REPRO*  ・  難易度: 上級

FROMKEY / TOKEYは、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 区切整理の・で FROMKEY ・ TOKEY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FROMKEY ・ TOKEY の出力を取らず区切整理の・の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切整理として引き継ぐ。 ✅
    - C. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)を省略して区切整理の・の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切整理の・へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では FROMKEY ・ TOKEY は「区切整理の・に関係する定義値と表示行を照合する区切整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では FROMKEY ・ TOKEY の属性行と IDC0005I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明だけに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では FROMKEY ・ TOKEY を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切整理初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **FROMKEY ・ TOKEY**

    - 検証目的: 終端整理の・について、FROMKEY / TOKEY は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010105の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、終端整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にFROMKEY ・ TOKEYを指定し、OSKB010105の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND FROMKEY ・ TOKEY
    CASE OSKB010105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM FROMKEY ・ TOKEY
    CASE OSKB010105
    SOURCE DFSMS
    ```

    FROMKEY ・ TOKEYとOSKB010105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010105を同じ出力で読み、終端整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010105
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010105.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の FROMKEY ・ TOKEY と OSKB010105 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### FROMNUMBER / TONUMBER {#c06-i0175}
*分類: REPRO*  ・  難易度: 上級

FROMNUMBER / TONUMBERは、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。RRDS のレコード番号範囲指定。「FROMNUMBER / TONUMBER」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 優先整理の・に関する FROMNUMBER 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先整理の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先整理の・の証跡として保存して根拠にする。
    - C. FROMNUMBER 属性の変更点を出力本文から切り離して優先整理の・の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、優先整理の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では FROMNUMBER 属性 は「FROMNUMBER 属性の状態と出力メッセージを結び付ける優先整理項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では FROMNUMBER 属性の出力行と IDC3009I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明だけに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では FROMNUMBER 属性を DFSMS の確認記録に残し、対象名は優先整理対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **FROMNUMBER ・ TONUMBER**

    - 検証目的: 上書整理の・について、FROMNUMBER / TONUMBER は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。RRDS のレコに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010107の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書整理の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にFROMNUMBER ・ TONUMを指定し、OSKB010107の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND FROMNUMBER ・ TONUM
    CASE OSKB010107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM FROMNUMBER ・ TONUM
    CASE OSKB010107
    SOURCE DFSMS
    ```

    FROMNUMBER ・ TONUMとOSKB010107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010107を同じ出力で読み、上書整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010107
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010107.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の FROMNUMBER ・ TONUM と OSKB010107 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### INDATASET(name) / OUTDATASET(name) {#c06-i0176}
*分類: REPRO*  ・  難易度: 上級

INDATASET(name) / OUTDATASET(name)は、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。DSN を直接指定する形式。DD 文を省略できるが動的割り振り扱いになる。「INDATASET(name) / OUTDATASET(name)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 条件整理の・に関係する INDATASET 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、条件整理の採否を説明欄に結び付ける。 ✅
    - B. INDATASET 属性の名称と担当者名だけを残して条件整理の・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で条件整理の・を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず条件整理の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では INDATASET 属性 は「INDATASET 属性の用途をストレージ管理の表示で確認する条件整理項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では DFSMS の INDATASET 属性と IDC3009I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明だけに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では INDATASET 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **INDATASET(name) ・ OUTDATASET(name)**

    - 検証目的: 置換整理の・について、INDATASET(name) / OUTDATASET(name)は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010104の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、置換整理の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にINDATASET(name) ・ を指定し、OSKB010104の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND INDATASET(name) ・ 
    CASE OSKB010104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM INDATASET(name) ・ 
    CASE OSKB010104
    SOURCE DFSMS
    ```

    INDATASET(name) ・ とOSKB010104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010104を同じ出力で読み、置換整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010104
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010104.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の INDATASET(name) ・  と OSKB010104 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### INFILE(ddname) / OUTFILE(ddname) {#c06-i0177}
*分類: REPRO*  ・  難易度: 上級

INFILE(ddname) / OUTFILE(ddname)は、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 出力整理の・に関する INFILE 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)の結果を残さず出力整理の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力整理の・の証跡として保存して根拠にする。
    - C. INFILE 属性の変更点を出力本文から切り離して出力整理の・の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0005I を読み、出力整理の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では INFILE 属性 は「INFILE 属性の状態と出力メッセージを結び付ける出力整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では INFILE 属性の出力行と IDC0005I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明だけに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では INFILE 属性を DFSMS の確認記録に残し、対象名は出力整理対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **INFILE(ddname) ・ OUTFILE(ddname)**

    - 検証目的: 呼出整理の・について、INFILE(ddname) / OUTFILE(ddname)は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010103の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、呼出整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にINFILE(ddname) ・ Oを指定し、OSKB010103の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND INFILE(ddname) ・ O
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM INFILE(ddname) ・ O
    CASE OSKB010103
    SOURCE DFSMS
    ```

    INFILE(ddname) ・ OとOSKB010103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010103を同じ出力で読み、呼出整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010103
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010103.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の INFILE(ddname) ・ O と OSKB010103 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### INFILECOPY (カタログ複写) {#c06-i0178}
*分類: REPRO*  ・  難易度: 上級

INFILECOPY (カタログ複写)は、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。ICF カタログ間の高速コピー。バックアップ/移行に使用される特殊オプション。「INFILECOPY (カタログ複写)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 復旧整理のカタログ複写で INFILECOPY 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. INFILECOPY 属性の出力を取らず復旧整理のカタログ複写の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧整理の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して復旧整理のカタログ複写の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧整理のカタログ複写へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では INFILECOPY 属性 は「復旧整理のカタログ複写に関係する定義値と表示行を照合する復旧整理項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では INFILECOPY 属性の属性行と IDC3009I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明だけに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では INFILECOPY 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **INFILECOPY (カタログ複写)**

    - 検証目的: 記録整理のカタログ複写について、INFILECOPY (カタログ複写)は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。ICF カタログ間のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010113の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、記録整理のカタログ複写の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にINFILECOPY (カタログ複写を指定し、OSKB010113の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND INFILECOPY (カタログ複写
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM INFILECOPY (カタログ複写
    CASE OSKB010113
    SOURCE DFSMS
    ```

    INFILECOPY (カタログ複写とOSKB010113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010113を同じ出力で読み、記録整理のカタログ複写の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010113.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の INFILECOPY (カタログ複写 と OSKB010113 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### MERGECAT / NOMERGECAT {#c06-i0179}
*分類: REPRO*  ・  難易度: 上級

MERGECAT / NOMERGECATは、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 警告整理の・に関係する MERGECAT 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)の結果から対象行を抜き出し、警告整理の証跡として残す。 ✅
    - B. MERGECAT 属性の名称と担当者名だけを残して警告整理の・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で警告整理の・を確認し同じ証跡として扱ったことにする。
    - D. IDC0005I の有無を見ず警告整理の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では MERGECAT 属性 は「MERGECAT 属性の用途をストレージ管理の表示で確認する警告整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景では DFSMS の MERGECAT 属性と IDC0005I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明だけに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では MERGECAT 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告整理用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **MERGECAT ・ NOMERGECAT**

    - 検証目的: 優先整理の・について、MERGECAT / NOMERGECAT は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010112の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、優先整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にMERGECAT ・ NOMERGEを指定し、OSKB010112の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND MERGECAT ・ NOMERGE
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM MERGECAT ・ NOMERGE
    CASE OSKB010112
    SOURCE DFSMS
    ```

    MERGECAT ・ NOMERGEとOSKB010112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010112を同じ出力で読み、優先整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010112.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の MERGECAT ・ NOMERGE と OSKB010112 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### REPLACE {#c06-i0180}
*分類: REPRO*  ・  難易度: 上級

REPLACEは、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 値域整理のストレージ管理に関する REPLACE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)の結果を残さず値域整理のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域整理のストレージ管理の証跡として保存して根拠にする。
    - C. REPLACE の変更点を出力本文から切り離して値域整理のストレージ管理の承認欄だけ残す。
    - D. IDC0005I を含む表示を保存し、説明欄との差分を値域整理で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では REPLACE は「REPLACE の状態と出力メッセージを結び付ける値域整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では REPLACE の出力行と IDC0005I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明だけに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では REPLACE を DFSMS の確認記録に残し、対象名は値域整理対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **REPLACE**

    - 検証目的: 置換照合のストレージ管理について、REPLACE は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030024の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、置換照合のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にREPLACEを指定し、OSKB030024の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND REPLACE
    CASE OSKB030024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM REPLACE
    CASE OSKB030024
    SOURCE DFSMS
    ```

    REPLACEとOSKB030024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB030024を同じ出力で読み、置換照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB030024
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB030024.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB030024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の REPLACE と OSKB030024 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB030024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **REPLACE**

    - 検証目的: 範囲整理のストレージ管理について、REPLACE は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010111の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、範囲整理のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にREPLACEを指定し、OSKB010111の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND REPLACE
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM REPLACE
    CASE OSKB010111
    SOURCE DFSMS
    ```

    REPLACEとOSKB010111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010111を同じ出力で読み、範囲整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010111.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の REPLACE と OSKB010111 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### REPRO 初期ロード {#c06-i0181}
*分類: REPRO*  ・  難易度: 上級

新規空 KSDS への REPRO は順次ロード経路を取り、SPEED 指定時は最速。レコードはキー順に整列済みであること

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 監査整理の初期ロードでストレージ管理の運用確認を行います。REPRO 初期ロードの根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査整理の初期ロードを確認した扱いにする。
    - B. IDC0005I の有無を確認せず監査整理の初期ロードを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査整理の根拠にする。 ✅
    - D. REPRO 初期ロードの属性行を読まず監査整理の初期ロードの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では REPRO 初期ロード は「DFSMS で REPRO 初期ロードの扱いを記録する監査整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では REPRO 初期ロードの表示結果と IDC0005I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明だけに寄り、判定名は監査整理不足です。監査整理資料では REPRO 初期ロードの使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **REPRO 初期ロード**

    - 検証目的: 比較整理の初期ロードについて、新規空 KSDS への REPRO は順次ロード経路を取り、SPEED 指定時は最速。レコードはキー順に整列済みであることに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010114の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、比較整理の初期ロードの確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にREPRO 初期ロードを指定し、OSKB010114の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND REPRO 初期ロード
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM REPRO 初期ロード
    CASE OSKB010114
    SOURCE DFSMS
    ```

    REPRO 初期ロードとOSKB010114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010114を同じ出力で読み、比較整理の初期ロードの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010114.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の REPRO 初期ロード と OSKB010114 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### REPRO 基本 {#c06-i0182}
*分類: REPRO*  ・  難易度: 上級

データセット間コピー (VSAM⇔QSAM 等) の IDCAMS コマンド。バックアップ/再編成/移行で最も使う

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 上書整理の基本でストレージ管理の運用確認を行います。REPRO 基本の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書整理の基本を確認した扱いにする。
    - B. IDC0005I の有無を確認せず上書整理の基本を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書整理の根拠にする。 ✅
    - D. REPRO 基本の属性行を読まず上書整理の基本の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では REPRO 基本 は「DFSMS で REPRO 基本の扱いを記録する上書整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では REPRO 基本の表示結果と IDC0005I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明だけに寄り、判定名は上書整理不足です。上書整理資料では REPRO 基本の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **REPRO 基本**

    - 検証目的: 展開整理の基本について、データセット間コピー (VSAM⇔QSAM 等) の IDCAMS コマンド。バックアップ/再編成/移行で最も使うに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010102の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、展開整理の基本の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にREPRO 基本を指定し、OSKB010102の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND REPRO 基本
    CASE OSKB010102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM REPRO 基本
    CASE OSKB010102
    SOURCE DFSMS
    ```

    REPRO 基本とOSKB010102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010102を同じ出力で読み、展開整理の基本の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010102
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010102.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の REPRO 基本 と OSKB010102 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### REUSE (REPRO) {#c06-i0183}
*分類: REPRO*  ・  難易度: 上級

REUSE (REPRO)は、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。出力クラスターが REUSE 属性なら既存内容をリセットして再ロード。OPEN OUTPUT 相当。「REUSE (REPRO)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 順序整理のストレージ管理でストレージ管理の運用確認を行います。REUSE (REPRO)の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で順序整理のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず順序整理のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序整理の根拠を固定する。 ✅
    - D. REUSE (REPRO)の属性行を読まず順序整理のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では REUSE (REPRO) は「DFSMS で REUSE (REPRO)の扱いを記録する順序整理項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では REUSE (REPRO)の表示結果と IDC3009I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明だけに寄り、判定名は順序整理不足です。順序整理資料では REUSE (REPRO)の使い方を出典欄から追跡し、資料名は順序整理資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **REUSE (REPRO)**

    - 検証目的: 区切整理のストレージ管理について、REUSE (REPRO)は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。出力クラスターが REUSE 属に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010110の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、区切整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にREUSE (REPRO)を指定し、OSKB010110の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND REUSE (REPRO)
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM REUSE (REPRO)
    CASE OSKB010110
    SOURCE DFSMS
    ```

    REUSE (REPRO)とOSKB010110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010110を同じ出力で読み、区切整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB010110.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB010110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の REUSE (REPRO) と OSKB010110 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB010110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### SKIP(n) {#c06-i0184}
*分類: REPRO*  ・  難易度: 上級

SKIP(n)は、DFSMS / IDCAMS / VSAMのREPROで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 比較整理のストレージ管理で SKIP(n)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SKIP(n)の出力を取らず比較整理のストレージ管理の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較整理の確認値として扱う。 ✅
    - C. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)を省略して比較整理のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較整理のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では SKIP(n) は「比較整理のストレージ管理に関係する定義値と表示行を照合する比較整理項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では SKIP(n)の属性行と IDC0005I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明だけに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では SKIP(n)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較整理初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **SKIP(n)**

    - 検証目的: 条件整理のストレージ管理について、SKIP(n)は、DFSMS / IDCAMS / VSAM の REPRO で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010109の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、条件整理のストレージ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    ```

    COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIDCAMSの表示結果です。FIND欄にSKIP(n)を指定し、OSKB010109の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND SKIP(n)
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM SKIP(n)
    CASE OSKB010109
    SOURCE DFSMS
    ```

    SKIP(n)とOSKB010109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010109を同じ出力で読み、条件整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB010109.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB010109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の SKIP(n) と OSKB010109 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB010109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > RMM

### DFSMSrmm 概要 {#c06-i0185}
*分類: RMM*  ・  難易度: 上級

DFSMSrmm 概要は、DFSMS / IDCAMS / VSAMのRMMで確認する項目です。テープ運用管理 (Removable Media Manager)。ボリューム/ラック/ロケーション/データセット/保持期限を統合管理

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 構文照合再の概要に関係する DFSMSrmm 概要の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文照合再で再確認できる形にする。 ✅
    - B. DFSMSrmm 概要の名称と担当者名だけを残して構文照合再の概要の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で構文照合再の概要を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず構文照合再の概要の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合再正解では選択記号 A を採用し、正解名は構文照合再正解です。構文照合再根拠では DFSMSrmm 概要 は「DFSMSrmm 概要の用途をストレージ管理の表示で確認する構文照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は構文照合再根拠です。構文照合再背景では DFSMS の DFSMSrmm 概要と IDC0001I を同じ証跡に残し、背景名は構文照合再背景です。他の選択肢を確認します。 A: 構文照合再正答は対象出力と項目説明を結び、根拠名は構文照合再正答です。 B: 構文照合再不足は名称や説明だけに寄り、判定名は構文照合再不足です。 C: 構文照合再流用は別カテゴリの確認であり、排除名は構文照合再流用です。 D: 構文照合再欠落は戻り値や記録番号に寄り、欠落名は構文照合再欠落です。構文照合再用語では DFSMSrmm 概要を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文照合再用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 記録追跡の概要に関係する DFSMSrmm 概要の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録追跡として残す。 ✅
    - B. DFSMSrmm 概要の名称と担当者名のみを残して記録追跡の概要の表示本文を確認対象に含めない。
    - C. ストレージ管理以外の画面で記録追跡の概要を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず記録追跡の概要の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録追跡の概要において選択記号 A を採用し、識別名は記録追跡です。記録追跡の概要において DFSMSrmm 概要 は説明欄の「DFSMSrmm 概要の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は記録追跡です。記録追跡の概要に関連して、DFSMS では DFSMSrmm 概要の表示属性と IDC0001I を同じ証跡に残し、背景名は記録追跡です。他の選択肢を確認します。 A: 記録追跡の概要は対象出力と項目説明を結び、根拠を残すので記録追跡です。 B: 記録追跡の概要は名称や説明のみに寄り、状態を示す出力本文が不足するため記録追跡ではありません。 C: 記録追跡の概要は別カテゴリの確認を流用しており、DFSMSrmm 概要の根拠にならないため記録追跡ではありません。 D: 記録追跡の概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため記録追跡ではありません。記録追跡の概要で使う DFSMSrmm 概要という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は記録追跡です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **DFSMSrmm 概要**

    - 検証目的: 終端追跡の概要について、DFSMSrmm 概要は、DFSMS / IDCAMS / VSAM の RMM で確認する項目です。テープ運用管理 (Removable Media Manager)。ボリューに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030045の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、終端追跡の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にDFSMSrmm 概要を指定し、OSKB030045の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND DFSMSrmm 概要
    CASE OSKB030045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM DFSMSrmm 概要
    CASE OSKB030045
    SOURCE DFSMS
    ```

    DFSMSrmm 概要とOSKB030045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030045を同じ出力で読み、終端追跡の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030045.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の DFSMSrmm 概要 と OSKB030045 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media

    ---

    **DFSMSrmm 概要**

    - 検証目的: 値域判定の概要について、DFSMSrmm 概要は、DFSMS / IDCAMS / VSAM の RMM で確認する項目です。テープ運用管理 (Removable Media Manager)。ボリューに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020096の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、値域判定の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にDFSMSrmm 概要を指定し、OSKB020096の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND DFSMSrmm 概要
    CASE OSKB020096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM DFSMSrmm 概要
    CASE OSKB020096
    SOURCE DFSMS
    ```

    DFSMSrmm 概要とOSKB020096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020096を同じ出力で読み、値域判定の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020096
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020096.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の DFSMSrmm 概要 と OSKB020096 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### RMM ADDRACK {#c06-i0186}
*分類: RMM*  ・  難易度: 上級

RMM ADDRACKは、DFSMS / IDCAMS / VSAMのRMMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 置換照合再のストレージ管理に関する RMM ADDRACK の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換照合再のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換照合再のストレージ管理の証跡として保存して根拠にする。
    - C. RMM ADDRACK の変更点を出力本文から切り離して置換照合再のストレージ管理の承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を置換照合再で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合再正解では選択記号 D を採用し、正解名は置換照合再正解です。置換照合再根拠では RMM ADDRACK は「RMM ADDRACK の状態と出力メッセージを結び付ける置換照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換照合再根拠です。置換照合再保存では RMM ADDRACK の出力行と IDC0001I を一緒に残し、保存名は置換照合再保存です。選択肢ごとの違いを示します。 A: 置換照合再欠落は戻り値や記録番号に寄り、欠落名は置換照合再欠落です。 B: 置換照合再流用は別カテゴリの確認であり、排除名は置換照合再流用です。 C: 置換照合再不足は名称や説明だけに寄り、判定名は置換照合再不足です。 D: 置換照合再正答は対象出力と項目説明を結び、根拠名は置換照合再正答です。置換照合再対象では RMM ADDRACK を DFSMS の確認記録に残し、対象名は置換照合再対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 値域追跡のストレージ管理に関する RMM ADDRACK の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず値域追跡のストレージ管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡のストレージ管理の証跡として保存して根拠にする。
    - C. RMM ADDRACK の変更点を出力本文から切り離して値域追跡のストレージ管理の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域追跡のストレージ管理において選択記号 D を採用し、識別名は値域追跡です。値域追跡のストレージ管理において RMM ADDRACK は説明欄の「RMM ADDRACK の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は値域追跡です。値域追跡のストレージ管理に関する記録は、RMM ADDRACK の出力行と IDC0001I を一緒に保存し、背景名は値域追跡です。選択肢ごとの違いを示します。 A: 値域追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため値域追跡ではありません。 B: 値域追跡のストレージ管理は別カテゴリの確認を流用しており、RMM ADDRACK の根拠にならないため値域追跡ではありません。 C: 値域追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため値域追跡ではありません。 D: 値域追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので値域追跡です。値域追跡のストレージ管理で記録する RMM ADDRACK は DFSMS の確認記録に残す対象名であり、用語名は値域追跡です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **RMM ADDRACK**

    - 検証目的: 監査判定のストレージ管理について、RMM ADDRACK は、DFSMS / IDCAMS / VSAM の RMM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020099の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM ADDRACKを指定し、OSKB020099の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM ADDRACK
    CASE OSKB020099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM ADDRACK
    CASE OSKB020099
    SOURCE DFSMS
    ```

    RMM ADDRACKとOSKB020099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020099を同じ出力で読み、監査判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020099
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020099.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の RMM ADDRACK と OSKB020099 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### RMM ADDVOLUME / DELETEVOLUME {#c06-i0187}
*分類: RMM*  ・  難易度: 上級

RMM 制御下の VOLSER 追加/削除。物理ボリューム搬入出に合わせる。「RMM ADDVOLUME / DELETEVOLUME」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 探索照合再の・で RMM ADDVOLUME 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RMM ADDVOLUME 属性の出力を取らず探索照合再の・の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、探索照合再の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索照合再の・の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索照合再の・へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合再正解では選択記号 B を採用し、正解名は探索照合再正解です。探索照合再根拠では RMM ADDVOLUME 属性 は「探索照合再の・に関係する定義値と表示行を照合する探索照合再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索照合再根拠です。探索照合再追跡では RMM ADDVOLUME 属性の属性行と IDC3009I を合わせ、追跡名は探索照合再追跡です。誤答側の問題点を分けます。 A: 探索照合再不足は名称や説明だけに寄り、判定名は探索照合再不足です。 B: 探索照合再正答は対象出力と項目説明を結び、根拠名は探索照合再正答です。 C: 探索照合再欠落は戻り値や記録番号に寄り、欠落名は探索照合再欠落です。 D: 探索照合再流用は別カテゴリの確認であり、排除名は探索照合再流用です。探索照合再初出では RMM ADDVOLUME 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索照合再初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 状態照合保守の状態照合として RMM を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 状態照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。状態照合保守で扱う RMM は DFSMS / IDCAMS / VSAM の確認対象です（状態照合保守用語）。状態照合保守の担当者は状態照合として、表示本文とメッセージを照合します（状態照合保守照合）。状態照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（状態照合保守出典）。A: 状態照合保守で表示とメッセージを結ぶ場合に根拠になります（状態照合保守A）。B: 状態照合保守で定義と出力の関係がない場合は追跡できません（状態照合保守B）。C: 状態照合保守で出典名のみでは実際の表示を説明できません（状態照合保守C）。D: 状態照合保守で操作記録のみでは値や状態の確認が不足します（状態照合保守D）。状態照合保守の初出用語として RMM を扱い、分類内の確認名として保存します（状態照合保守終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **RMM ADDVOLUME ・ DELETEVOLUME**

    - 検証目的: 探索追跡の・について、RMM 制御下の VOLSER 追加/削除。物理ボリューム搬入出に合わせる。「RMM ADDVOLUME / DELETEVOLUME」を読むと、DEFINE、ALTER、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030046の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索追跡の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM ADDVOLUME ・ DEを指定し、OSKB030046の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM ADDVOLUME ・ DE
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM ADDVOLUME ・ DE
    CASE OSKB030046
    SOURCE DFSMS
    ```

    RMM ADDVOLUME ・ DEとOSKB030046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030046を同じ出力で読み、探索追跡の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB030046.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB030046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の RMM ADDVOLUME ・ DE と OSKB030046 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB030046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media

    ---

    **RMM ADDVOLUME ・ DELETEVOLUME**

    - 検証目的: 構文整理の・について、RMM 制御下の VOLSER 追加/削除。物理ボリューム搬入出に合わせる。「RMM ADDVOLUME / DELETEVOLUME」を読むと、DEFINE、ALTER、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文整理の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM ADDVOLUME ・ DEを指定し、OSKB020101の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM ADDVOLUME ・ DE
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM ADDVOLUME ・ DE
    CASE OSKB020101
    SOURCE DFSMS
    ```

    RMM ADDVOLUME ・ DEとOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020101を同じ出力で読み、構文整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020101.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の RMM ADDVOLUME ・ DE と OSKB020101 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### RMM CHANGERACK {#c06-i0188}
*分類: RMM*  ・  難易度: 上級

RMM CHANGERACKは、DFSMS / IDCAMS / VSAMのRMMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 終端照合再のストレージ管理に関係する RMM CHANGERACK の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、終端照合再の証跡として残す。 ✅
    - B. RMM CHANGERACK の名称と担当者名だけを残して終端照合再のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端照合再のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず終端照合再のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合再正解では選択記号 A を採用し、正解名は終端照合再正解です。終端照合再根拠では RMM CHANGERACK は「RMM CHANGERACK の用途をストレージ管理の表示で確認する終端照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は終端照合再根拠です。終端照合再背景では DFSMS の RMM CHANGERACK と IDC0001I を同じ証跡に残し、背景名は終端照合再背景です。他の選択肢を確認します。 A: 終端照合再正答は対象出力と項目説明を結び、根拠名は終端照合再正答です。 B: 終端照合再不足は名称や説明だけに寄り、判定名は終端照合再不足です。 C: 終端照合再流用は別カテゴリの確認であり、排除名は終端照合再流用です。 D: 終端照合再欠落は戻り値や記録番号に寄り、欠落名は終端照合再欠落です。終端照合再用語では RMM CHANGERACK を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端照合再用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 警告追跡のストレージ管理に関係する RMM CHANGERACK の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告追跡として残す。 ✅
    - B. RMM CHANGERACK の名称と担当者名のみを残して警告追跡のストレージ管理の表示本文を確認対象に含めない。
    - C. ストレージ管理以外の画面で警告追跡のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず警告追跡のストレージ管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告追跡のストレージ管理において選択記号 A を採用し、識別名は警告追跡です。警告追跡のストレージ管理において RMM CHANGERACK は説明欄の「RMM CHANGERACK の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は警告追跡です。警告追跡のストレージ管理に関連して、DFSMS では RMM CHANGERACK の表示属性と IDC0001I を同じ証跡に残し、背景名は警告追跡です。他の選択肢を確認します。 A: 警告追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので警告追跡です。 B: 警告追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため警告追跡ではありません。 C: 警告追跡のストレージ管理は別カテゴリの確認を流用しており、RMM CHANGERACK の根拠にならないため警告追跡ではありません。 D: 警告追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため警告追跡ではありません。警告追跡のストレージ管理で使う RMM CHANGERACK という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は警告追跡です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **RMM CHANGERACK**

    - 検証目的: 変更判定のストレージ管理について、RMM CHANGERACK は、DFSMS / IDCAMS / VSAM の RMM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020100の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、変更判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM CHANGERACKを指定し、OSKB020100の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM CHANGERACK
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM CHANGERACK
    CASE OSKB020100
    SOURCE DFSMS
    ```

    RMM CHANGERACKとOSKB020100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020100を同じ出力で読み、変更判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020100.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の RMM CHANGERACK と OSKB020100 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### RMM CHANGEVOLUME {#c06-i0189}
*分類: RMM*  ・  難易度: 上級

RMM CHANGEVOLUMEは、DFSMS / IDCAMS / VSAMのRMMで機能名、見出し、または確認対象として参照する項目です。ボリューム属性を変更。期限変更、ライブラリ移動 (MOVE) 指示等を行う。「RMM CHANGEVOLUME」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 呼出照合再のストレージ管理でストレージ管理の運用確認を行います。RMM CHANGEVOLUME の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出照合再のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず呼出照合再のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出照合再の根拠を固定する。 ✅
    - D. RMM CHANGEVOLUME の属性行を読まず呼出照合再のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合再正解では選択記号 C を採用し、正解名は呼出照合再正解です。呼出照合再根拠では RMM CHANGEVOLUME は「DFSMS で RMM CHANGEVOLUME の扱いを記録する呼出照合再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出照合再根拠です。呼出照合再受渡では RMM CHANGEVOLUME の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出照合再受渡です。不適切な選択肢を整理します。 A: 呼出照合再流用は別カテゴリの確認であり、排除名は呼出照合再流用です。 B: 呼出照合再欠落は戻り値や記録番号に寄り、欠落名は呼出照合再欠落です。 C: 呼出照合再正答は対象出力と項目説明を結び、根拠名は呼出照合再正答です。 D: 呼出照合再不足は名称や説明だけに寄り、判定名は呼出照合再不足です。呼出照合再資料では RMM CHANGEVOLUME の使い方を出典欄から追跡し、資料名は呼出照合再資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 順序追跡のストレージ管理でストレージ管理の運用確認を行います。RMM CHANGEVOLUME の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で順序追跡のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず順序追跡のストレージ管理を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序追跡の記録として扱う。 ✅
    - D. RMM CHANGEVOLUME の属性行を読まず順序追跡のストレージ管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序追跡のストレージ管理において選択記号 C を採用し、識別名は順序追跡です。順序追跡のストレージ管理において RMM CHANGEVOLUME は説明欄の「DFSMS で RMM CHANGEVOLUME の扱いを記録する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は順序追跡です。順序追跡のストレージ管理を受け取る担当者は、RMM CHANGEVOLUME の表示結果と IDC3009I を同じ確認単位として扱い、背景名は順序追跡です。不適切な選択肢を整理します。 A: 順序追跡のストレージ管理は別カテゴリの確認を流用しており、RMM CHANGEVOLUME の根拠にならないため順序追跡ではありません。 B: 順序追跡のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため順序追跡ではありません。 C: 順序追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので順序追跡です。 D: 順序追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため順序追跡ではありません。順序追跡のストレージ管理が示す RMM CHANGEVOLUME は出典欄の資料で使い方を追跡できる項目であり、用語名は順序追跡です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **RMM CHANGEVOLUME**

    - 検証目的: 復旧判定のストレージ管理について、RMM CHANGEVOLUME は、DFSMS / IDCAMS / VSAM の RMM で機能名、見出し、または確認対象として参照する項目です。ボリューム属性を変更。期限変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020098の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM CHANGEVOLUMEを指定し、OSKB020098の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM CHANGEVOLUME
    CASE OSKB020098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM CHANGEVOLUME
    CASE OSKB020098
    SOURCE DFSMS
    ```

    RMM CHANGEVOLUMEとOSKB020098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020098を同じ出力で読み、復旧判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020098
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020098.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の RMM CHANGEVOLUME と OSKB020098 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### RMM LISTDATASET {#c06-i0190}
*分類: RMM*  ・  難易度: 上級

RMM LISTDATASETは、DFSMS / IDCAMS / VSAMのRMMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 上書照合再のストレージ管理でストレージ管理の運用確認を行います。RMM LISTDATASET の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書照合再のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず上書照合再のストレージ管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書照合再の根拠にする。 ✅
    - D. RMM LISTDATASET の属性行を読まず上書照合再のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合再正解では選択記号 C を採用し、正解名は上書照合再正解です。上書照合再根拠では RMM LISTDATASET は「DFSMS で RMM LISTDATASET の扱いを記録する上書照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は上書照合再根拠です。上書照合再受渡では RMM LISTDATASET の表示結果と IDC0001I を同じ確認単位にし、受渡名は上書照合再受渡です。不適切な選択肢を整理します。 A: 上書照合再流用は別カテゴリの確認であり、排除名は上書照合再流用です。 B: 上書照合再欠落は戻り値や記録番号に寄り、欠落名は上書照合再欠落です。 C: 上書照合再正答は対象出力と項目説明を結び、根拠名は上書照合再正答です。 D: 上書照合再不足は名称や説明だけに寄り、判定名は上書照合再不足です。上書照合再資料では RMM LISTDATASET の使い方を出典欄から追跡し、資料名は上書照合再資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 監査追跡のストレージ管理でストレージ管理の運用確認を行います。RMM LISTDATASET の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査追跡のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず監査追跡のストレージ管理を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査追跡の記録として扱う。 ✅
    - D. RMM LISTDATASET の属性行を読まず監査追跡のストレージ管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡のストレージ管理において選択記号 C を採用し、識別名は監査追跡です。監査追跡のストレージ管理において RMM LISTDATASET は説明欄の「DFSMS で RMM LISTDATASET の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は監査追跡です。監査追跡のストレージ管理を受け取る担当者は、RMM LISTDATASET の表示結果と IDC0001I を同じ確認単位として扱い、背景名は監査追跡です。不適切な選択肢を整理します。 A: 監査追跡のストレージ管理は別カテゴリの確認を流用しており、RMM LISTDATASET の根拠にならないため監査追跡ではありません。 B: 監査追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため監査追跡ではありません。 C: 監査追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので監査追跡です。 D: 監査追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため監査追跡ではありません。監査追跡のストレージ管理が示す RMM LISTDATASET は出典欄の資料で使い方を追跡できる項目であり、用語名は監査追跡です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **RMM LISTDATASET**

    - 検証目的: 展開整理のストレージ管理について、RMM LISTDATASET は、DFSMS / IDCAMS / VSAM の RMM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020102の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、展開整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM LISTDATASETを指定し、OSKB020102の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM LISTDATASET
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM LISTDATASET
    CASE OSKB020102
    SOURCE DFSMS
    ```

    RMM LISTDATASETとOSKB020102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020102を同じ出力で読み、展開整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020102.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の RMM LISTDATASET と OSKB020102 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### RMM LISTVOLUME {#c06-i0191}
*分類: RMM*  ・  難易度: 上級

RMM LISTVOLUMEは、DFSMS / IDCAMS / VSAMのRMMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（2問）"
    **問題.** 展開照合再のストレージ管理で RMM LISTVOLUME の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RMM LISTVOLUME の出力を取らず展開照合再のストレージ管理の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開照合再の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して展開照合再のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開照合再のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合再正解では選択記号 B を採用し、正解名は展開照合再正解です。展開照合再根拠では RMM LISTVOLUME は「展開照合再のストレージ管理に関係する定義値と表示行を照合する展開照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は展開照合再根拠です。展開照合再追跡では RMM LISTVOLUME の属性行と IDC0001I を合わせ、追跡名は展開照合再追跡です。誤答側の問題点を分けます。 A: 展開照合再不足は名称や説明だけに寄り、判定名は展開照合再不足です。 B: 展開照合再正答は対象出力と項目説明を結び、根拠名は展開照合再正答です。 C: 展開照合再欠落は戻り値や記録番号に寄り、欠落名は展開照合再欠落です。 D: 展開照合再流用は別カテゴリの確認であり、排除名は展開照合再流用です。展開照合再初出では RMM LISTVOLUME を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開照合再初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 比較追跡のストレージ管理で RMM LISTVOLUME の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RMM LISTVOLUME の出力を取らず比較追跡のストレージ管理の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較追跡の確認結果にする。 ✅
    - C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して比較追跡のストレージ管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡のストレージ管理において選択記号 B を採用し、識別名は比較追跡です。比較追跡のストレージ管理において RMM LISTVOLUME は説明欄の「比較追跡のストレージ管理に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は比較追跡です。比較追跡のストレージ管理の証跡を読む担当者は、RMM LISTVOLUME の属性行と IDC0001I を合わせて追跡し、背景名は比較追跡です。誤答側の問題点を分けます。 A: 比較追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため比較追跡ではありません。 B: 比較追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので比較追跡です。 C: 比較追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため比較追跡ではありません。 D: 比較追跡のストレージ管理は別カテゴリの確認を流用しており、RMM LISTVOLUME の根拠にならないため比較追跡ではありません。比較追跡のストレージ管理に出る RMM LISTVOLUME は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は比較追跡です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **RMM LISTVOLUME**

    - 検証目的: 警告判定のストレージ管理について、RMM LISTVOLUME は、DFSMS / IDCAMS / VSAM の RMM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020097の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、警告判定のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRMM LISTVOLUMEを指定し、OSKB020097の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RMM LISTVOLUME
    CASE OSKB020097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RMM LISTVOLUME
    CASE OSKB020097
    SOURCE DFSMS
    ```

    RMM LISTVOLUMEとOSKB020097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020097を同じ出力で読み、警告判定のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020097
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020097.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の RMM LISTVOLUME と OSKB020097 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media



### Vital Record Specification (VRS) {#c06-i0192}
*分類: RMM*  ・  難易度: 上級

Vital Record Specification (VRS)は、DFSMS / IDCAMS / VSAMのRMMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSrmm Managing and Using Removable Media

??? question "確認問題（1問）"
    **問題.** 出力照合再のストレージ管理に関する Vital 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず出力照合再のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力照合再のストレージ管理の証跡として保存して根拠にする。
    - C. Vital 機能の変更点を出力本文から切り離して出力照合再のストレージ管理の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、出力照合再の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合再正解では選択記号 D を採用し、正解名は出力照合再正解です。出力照合再根拠では Vital 機能 は「Vital 機能の状態と出力メッセージを結び付ける出力照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は出力照合再根拠です。出力照合再保存では Vital 機能の出力行と IDC0001I を一緒に残し、保存名は出力照合再保存です。選択肢ごとの違いを示します。 A: 出力照合再欠落は戻り値や記録番号に寄り、欠落名は出力照合再欠落です。 B: 出力照合再流用は別カテゴリの確認であり、排除名は出力照合再流用です。 C: 出力照合再不足は名称や説明だけに寄り、判定名は出力照合再不足です。 D: 出力照合再正答は対象出力と項目説明を結び、根拠名は出力照合再正答です。出力照合再対象では Vital 機能を DFSMS の確認記録に残し、対象名は出力照合再対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Vital Record Specification (VRS)**

    - 検証目的: 呼出整理のストレージ管理について、Vital Record Specification (VRS)は、DFSMS / IDCAMS / VSAM の RMM で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020103の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、呼出整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVital Record Speciを指定し、OSKB020103の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Vital Record Speci
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Vital Record Speci
    CASE OSKB020103
    SOURCE DFSMS
    ```

    Vital Record SpeciとOSKB020103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020103を同じ出力で読み、呼出整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020103.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Vital Record Speci と OSKB020103 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSrmm Managing and Using Removable Media




## DFSMS / IDCAMS / VSAM > SMS_DATACLAS

### Compaction {#c06-i0193}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Compactionは、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。DASD 圧縮 (DBB / zEDC) の適用指定。Extended Format 前提。「Compaction」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 復旧読解のストレージ管理で Compactionの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Compactionの出力を取らず復旧読解のストレージ管理の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧読解の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して復旧読解のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧読解のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では Compaction は「復旧読解のストレージ管理に関係する定義値と表示行を照合する復旧読解項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では Compactionの属性行と IDC3009I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明だけに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では Compactionを DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 区切確認のストレージ管理で Compactionの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Compactionの出力を取らず区切確認のストレージ管理の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 ✅
    - C. DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を省略して区切確認のストレージ管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認のストレージ管理において選択記号 B を採用し、識別名は区切確認です。区切確認のストレージ管理において Compaction は説明欄の「区切確認のストレージ管理に関係する定義値と表示行を照合する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認のストレージ管理の証跡を読む担当者は、Compactionの属性行と IDC3009I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認のストレージ管理は対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため区切確認ではありません。 D: 区切確認のストレージ管理は別カテゴリの確認を流用しており、Compactionの根拠にならないため区切確認ではありません。区切確認のストレージ管理に出る Compactionは DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Compaction**

    - 検証目的: 記録追跡のストレージ管理について、Compactionは、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。DASD 圧縮 (DBBに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、記録追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCompactionを指定し、OSKB020053の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Compaction
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Compaction
    CASE OSKB020053
    SOURCE DFSMS
    ```

    CompactionとOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020053を同じ出力で読み、記録追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020053.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Compaction と OSKB020053 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### DSORG {#c06-i0194}
*分類: SMS_DATACLAS*  ・  難易度: 上級

DSORGは、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 記録読解のストレージ管理に関係する DSORG の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録読解で再確認できる形にする。 ✅
    - B. DSORG の名称と担当者名だけを残して記録読解のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で記録読解のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず記録読解のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では DSORG は「DSORG の用途をストレージ管理の表示で確認する記録読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では DFSMS の DSORG と IDC0001I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明だけに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では DSORG を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 終端確認のストレージ管理に関係する DSORG の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端確認として残す。 ✅
    - B. DSORG の名称と担当者名のみを残して終端確認のストレージ管理の表示本文を確認対象に含めない。
    - C. ストレージ管理以外の画面で終端確認のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず終端確認のストレージ管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認のストレージ管理において選択記号 A を採用し、識別名は終端確認です。終端確認のストレージ管理において DSORG は説明欄の「DSORG の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認のストレージ管理に関連して、DFSMS では DSORG の表示属性と IDC0001I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認のストレージ管理は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認のストレージ管理は別カテゴリの確認を流用しており、DSORG の根拠にならないため終端確認ではありません。 D: 終端確認のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため終端確認ではありません。終端確認のストレージ管理で使う DSORG という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は終端確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **DSORG**

    - 検証目的: 出力追跡のストレージ管理について、DSORG は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、出力追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にDSORGを指定し、OSKB020048の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND DSORG
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM DSORG
    CASE OSKB020048
    SOURCE DFSMS
    ```

    DSORGとOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020048を同じ出力で読み、出力追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020048.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の DSORG と OSKB020048 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Data Class 概要 {#c06-i0195}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Data Class 概要は、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 範囲読解の概要でストレージ管理の運用確認を行います。Data Class 概要の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で範囲読解の概要を確認した扱いにする。
    - B. IDC0001I の有無を確認せず範囲読解の概要を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲読解の確認にする。 ✅
    - D. Data Class 概要の属性行を読まず範囲読解の概要の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では Data Class 概要 は「DFSMS で Data Class 概要の扱いを記録する範囲読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では Data Class 概要の表示結果と IDC0001I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明だけに寄り、判定名は範囲読解不足です。範囲読解資料では Data Class 概要の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 呼出確認の概要でストレージ管理の運用確認を行います。Data Class 概要の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出確認の概要を確認した扱いにする。
    - B. IDC0001I の有無を確認せず呼出確認の概要を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 ✅
    - D. Data Class 概要の属性行を読まず呼出確認の概要の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認の概要において選択記号 C を採用し、識別名は呼出確認です。呼出確認の概要において Data Class 概要 は説明欄の「DFSMS で Data Class 概要の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の概要を受け取る担当者は、Data Class 概要の表示結果と IDC0001I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の概要は別カテゴリの確認を流用しており、Data Class 概要の根拠にならないため呼出確認ではありません。 B: 呼出確認の概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の概要は対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の概要は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の概要が示す Data Class 概要は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **Data Class 概要**

    - 検証目的: 順序照合の概要について、Data Class 概要は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030035の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序照合の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にData Class 概要を指定し、OSKB030035の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Data Class 概要
    CASE OSKB030035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Data Class 概要
    CASE OSKB030035
    SOURCE DFSMS
    ```

    Data Class 概要とOSKB030035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030035を同じ出力で読み、順序照合の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030035
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030035.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Data Class 概要 と OSKB030035 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Data Class 概要**

    - 検証目的: 探索追跡の概要について、Data Class 概要は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、探索追跡の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にData Class 概要を指定し、OSKB020046の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Data Class 概要
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Data Class 概要
    CASE OSKB020046
    SOURCE DFSMS
    ```

    Data Class 概要とOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020046を同じ出力で読み、探索追跡の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020046.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Data Class 概要 と OSKB020046 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Extended Addressability (EA) {#c06-i0196}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Extended Addressability (EA)は、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 警告読解のストレージ管理に関係する Extended 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、警告読解の証跡として残す。 ✅
    - B. Extended 機能の名称と担当者名だけを残して警告読解のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で警告読解のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず警告読解のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では Extended 機能 は「Extended 機能の用途をストレージ管理の表示で確認する警告読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では DFSMS の Extended 機能と IDC0001I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明だけに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では Extended 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Extended Addressability (EA)**

    - 検証目的: 優先追跡のストレージ管理について、Extended Addressability (EA)は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、優先追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にExtended Addressabを指定し、OSKB020052の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Extended Addressab
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Extended Addressab
    CASE OSKB020052
    SOURCE DFSMS
    ```

    Extended AddressabとOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020052を同じ出力で読み、優先追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020052.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Extended Addressab と OSKB020052 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Extended Format {#c06-i0197}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Extended Formatは、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 値域読解のストレージ管理に関する Extended Formatの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず値域読解のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域読解のストレージ管理の証跡として保存して根拠にする。
    - C. Extended Formatの変更点を出力本文から切り離して値域読解のストレージ管理の承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を値域読解で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では Extended Format は「Extended Formatの状態と出力メッセージを結び付ける値域読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では Extended Formatの出力行と IDC0001I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明だけに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では Extended Formatを DFSMS の確認記録に残し、対象名は値域読解対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 出力確認のストレージ管理に関する Extended Formatの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず出力確認のストレージ管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のストレージ管理の証跡として保存して根拠にする。
    - C. Extended Formatの変更点を出力本文から切り離して出力確認のストレージ管理の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認のストレージ管理において選択記号 D を採用し、識別名は出力確認です。出力確認のストレージ管理において Extended Format は説明欄の「Extended Formatの状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認のストレージ管理に関する記録は、Extended Formatの出力行と IDC0001I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため出力確認ではありません。 B: 出力確認のストレージ管理は別カテゴリの確認を流用しており、Extended Formatの根拠にならないため出力確認ではありません。 C: 出力確認のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認のストレージ管理は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認のストレージ管理で記録する Extended Formatは DFSMS の確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **Extended Format**

    - 検証目的: 値域照合のストレージ管理について、Extended Formatは、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030036の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、値域照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にExtended Formatを指定し、OSKB030036の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Extended Format
    CASE OSKB030036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Extended Format
    CASE OSKB030036
    SOURCE DFSMS
    ```

    Extended FormatとOSKB030036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030036を同じ出力で読み、値域照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030036
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030036.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Extended Format と OSKB030036 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Extended Format**

    - 検証目的: 範囲追跡のストレージ管理について、Extended Formatは、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、範囲追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にExtended Formatを指定し、OSKB020051の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Extended Format
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Extended Format
    CASE OSKB020051
    SOURCE DFSMS
    ```

    Extended FormatとOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020051を同じ出力で読み、範囲追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020051.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Extended Format と OSKB020051 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Imbed/Replicate (廃止) {#c06-i0198}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Imbed/Replicate (廃止)は、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。Data Class で旧属性を残存指定可能だが現行 z/OS は無視。「Imbed/Replicate (廃止)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 構文検分の・ 廃止に関係する Imbed 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、構文検分の採否を説明欄に結び付ける。 ✅
    - B. Imbed 属性の名称と担当者名だけを残して構文検分の・ 廃止の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で構文検分の・ 廃止を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず構文検分の・ 廃止の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では Imbed 属性 は「Imbed 属性の用途をストレージ管理の表示で確認する構文検分項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では DFSMS の Imbed 属性と IDC3009I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明だけに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では Imbed 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 属性照合通知の属性照合として Imbed/Replicate (廃止) を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 属性照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 名称と担当者名を保存して表示本文を確認しない。
    - D. 別分類の結果を流用して同じ証跡として扱う。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解はAです。属性照合通知で扱う Imbed/Replicate (廃止) は DFSMS / IDCAMS / VSAM の確認対象です（属性照合通知用語）。属性照合通知の担当者は属性照合として、表示本文とメッセージを照合します（属性照合通知照合）。属性照合通知の対応を残すと、後続担当者は同じ出典に戻って確認できます（属性照合通知出典）。A: 属性照合通知で表示とメッセージを結ぶ場合に根拠になります（属性照合通知A）。B: 属性照合通知で定義と出力の関係がない場合は追跡できません（属性照合通知B）。C: 属性照合通知で出典名のみでは実際の表示を説明できません（属性照合通知C）。D: 属性照合通知で操作記録のみでは値や状態の確認が不足します（属性照合通知D）。属性照合通知の初出用語として Imbed/Replicate (廃止) を扱い、分類内の確認名として保存します（属性照合通知終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **Imbed・ Replicate (廃止)**

    - 検証目的: 警告照合の・ 廃止について、Imbed/Replicate (廃止)は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。Daに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030037の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告照合の・ 廃止の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にImbed・ Replicate (を指定し、OSKB030037の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Imbed・ Replicate (
    CASE OSKB030037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Imbed・ Replicate (
    CASE OSKB030037
    SOURCE DFSMS
    ```

    Imbed・ Replicate (とOSKB030037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030037を同じ出力で読み、警告照合の・ 廃止の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB030037
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB030037.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB030037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Imbed・ Replicate ( と OSKB030037 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB030037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Imbed・ Replicate (廃止)**

    - 検証目的: 値域追跡の・ 廃止について、Imbed/Replicate (廃止)は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。Daに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域追跡の・ 廃止の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にImbed・ Replicate (を指定し、OSKB020056の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Imbed・ Replicate (
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Imbed・ Replicate (
    CASE OSKB020056
    SOURCE DFSMS
    ```

    Imbed・ Replicate (とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020056を同じ出力で読み、値域追跡の・ 廃止の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020056.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Imbed・ Replicate ( と OSKB020056 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration


