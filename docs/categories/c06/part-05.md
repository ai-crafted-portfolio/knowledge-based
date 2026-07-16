---
search:
  exclude: true
---

# DFSMS / IDCAMS / VSAM — 詳細 (5/6)

[← DFSMS / IDCAMS / VSAM の概要へ戻る](index.md)


## DFSMS / IDCAMS / VSAM > SMS_DATACLAS

### RECFM / LRECL / BLKSIZE {#c06-i0199}
*分類: SMS_DATACLAS*  ・  難易度: 上級

RECFM / LRECL / BLKSIZEは、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。順次/区分データセット用の基本 DCB 属性。BLKSIZE=0 はシステム決定 (SDB)。「RECFM / LRECL / BLKSIZE」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 優先読解の・ ・に関する RECFM 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先読解の・ ・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先読解の・ ・の証跡として保存して根拠にする。
    - C. RECFM 属性の変更点を出力本文から切り離して優先読解の・ ・の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、優先読解の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では RECFM 属性 は「RECFM 属性の状態と出力メッセージを結び付ける優先読解項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では RECFM 属性の出力行と IDC3009I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明だけに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では RECFM 属性を DFSMS の確認記録に残し、対象名は優先読解対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 構文照合保守の構文照合として RECFM を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。構文照合保守で扱う RECFM は DFSMS / IDCAMS / VSAM の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として RECFM を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **RECFM ・ LRECL ・ BLKSIZE**

    - 検証目的: 上書追跡の・ ・について、RECFM / LRECL / BLKSIZE は、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書追跡の・ ・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRECFM ・ LRECL ・ BLを指定し、OSKB020047の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND RECFM ・ LRECL ・ BL
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM RECFM ・ LRECL ・ BL
    CASE OSKB020047
    SOURCE DFSMS
    ```

    RECFM ・ LRECL ・ BLとOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020047を同じ出力で読み、上書追跡の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020047.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の RECFM ・ LRECL ・ BL と OSKB020047 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Reuse {#c06-i0200}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Reuseは、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 変更読解のストレージ管理に関する Reuseの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず変更読解のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更読解のストレージ管理の証跡として保存して根拠にする。
    - C. Reuseの変更点を出力本文から切り離して変更読解のストレージ管理の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、変更読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では Reuse は「Reuseの状態と出力メッセージを結び付ける変更読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では Reuseの出力行と IDC0001I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明だけに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では Reuseを DFSMS の確認記録に残し、対象名は変更読解対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 優先確認のストレージ管理に関する Reuseの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず優先確認のストレージ管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のストレージ管理の証跡として保存して根拠にする。
    - C. Reuseの変更点を出力本文から切り離して優先確認のストレージ管理の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認のストレージ管理において選択記号 D を採用し、識別名は優先確認です。優先確認のストレージ管理において Reuse は説明欄の「Reuseの状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認のストレージ管理に関する記録は、Reuseの出力行と IDC0001I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため優先確認ではありません。 B: 優先確認のストレージ管理は別カテゴリの確認を流用しており、Reuseの根拠にならないため優先確認ではありません。 C: 優先確認のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認のストレージ管理は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認のストレージ管理で記録する Reuseは DFSMS の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Reuse**

    - 検証目的: 順序追跡のストレージ管理について、Reuseは、DFSMS / IDCAMS / VSAM の SMS_DATACLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にReuseを指定し、OSKB020055の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Reuse
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Reuse
    CASE OSKB020055
    SOURCE DFSMS
    ```

    ReuseとOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020055を同じ出力で読み、順序追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020055.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Reuse と OSKB020055 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Space Allocation (Avg / Primary / Secondary) {#c06-i0201}
*分類: SMS_DATACLAS*  ・  難易度: 上級

Space Allocation (Avg / Primary / Secondary)は、DFSMS / IDCAMS / VSAMのSMS_DATACLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 比較読解の・で Space 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Space 機能の出力を取らず比較読解の・の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較読解の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して比較読解の・の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較読解の・へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では Space 機能 は「比較読解の・に関係する定義値と表示行を照合する比較読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では Space 機能の属性行と IDC0001I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明だけに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では Space 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較読解初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 展開照合権限の展開照合として Space Allocation (Avg / Prim を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 展開照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。展開照合権限で扱う Space Allocation (Avg / Prim は DFSMS / IDCAMS / VSAM の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として Space Allocation (Avg / Prim を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200



### VSAM CISZ / KEYS / FREESPACE / SHAREOPTIONS {#c06-i0202}
*分類: SMS_DATACLAS*  ・  難易度: 上級

VSAM CISZ / KEYS / FREESPACE / SHAREOPTIONSは、DFSMS / IDCAMS / VSAMのSMS_DATACLASで構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 監査読解の・ ・でストレージ管理の運用確認を行います。VSAM CISZ 属性の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査読解の・ ・を確認した扱いにする。
    - B. IDC0001I の有無を確認せず監査読解の・ ・を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査読解の根拠にする。 ✅
    - D. VSAM CISZ 属性の属性行を読まず監査読解の・ ・の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では VSAM CISZ 属性 は「DFSMS で VSAM CISZ 属性の扱いを記録する監査読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では VSAM CISZ 属性の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明だけに寄り、判定名は監査読解不足です。監査読解資料では VSAM CISZ 属性の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 出力照合照合の出力照合として VSAM を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 出力照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。出力照合照合で扱う VSAM は DFSMS / IDCAMS / VSAM の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として VSAM を扱い、分類内の確認名として保存します（出力照合照合終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200



### Volume Count {#c06-i0203}
*分類: SMS_DATACLAS*  ・  難易度: 上級

多巻データセットの初期ボリューム数。マルチボリューム VSAM の予告として有効。「Volume Count」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 順序読解のストレージ管理でストレージ管理の運用確認を行います。Volume Countの根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で順序読解のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず順序読解のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序読解の根拠を固定する。 ✅
    - D. Volume Countの属性行を読まず順序読解のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では Volume Count は「DFSMS で Volume Countの扱いを記録する順序読解項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では Volume Countの表示結果と IDC3009I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明だけに寄り、判定名は順序読解不足です。順序読解資料では Volume Countの使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 上書確認のストレージ管理でストレージ管理の運用確認を行います。Volume Countの根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書確認のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず上書確認のストレージ管理を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書確認の記録として扱う。 ✅
    - D. Volume Countの属性行を読まず上書確認のストレージ管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認のストレージ管理において選択記号 C を採用し、識別名は上書確認です。上書確認のストレージ管理において Volume Count は説明欄の「DFSMS で Volume Countの扱いを記録する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のストレージ管理を受け取る担当者は、Volume Countの表示結果と IDC3009I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のストレージ管理は別カテゴリの確認を流用しており、Volume Countの根拠にならないため上書確認ではありません。 B: 上書確認のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため上書確認ではありません。 C: 上書確認のストレージ管理は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のストレージ管理が示す Volume Countは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Volume Count**

    - 検証目的: 区切追跡のストレージ管理について、多巻データセットの初期ボリューム数。マルチボリューム VSAM の予告として有効。「Volume Count」を読むと、DEFINE、ALTER、DELETE、LISTCAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、区切追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVolume Countを指定し、OSKB020050の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Volume Count
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Volume Count
    CASE OSKB020050
    SOURCE DFSMS
    ```

    Volume CountとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020050を同じ出力で読み、区切追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020050.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Volume Count と OSKB020050 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration




## DFSMS / IDCAMS / VSAM > SMS_MGMTCLAS

### # GDG Elements on Primary {#c06-i0204}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

# GDG Elements on Primaryは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。Primary 領域に残す GDG 世代数。古い世代は自動マイグレーション。「# GDG Elements on Primary」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 条件読解のストレージ管理に関係する# 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、条件読解の採否を説明欄に結び付ける。 ✅
    - B. # 機能の名称と担当者名だけを残して条件読解のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で条件読解のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず条件読解のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では# 機能は「# 機能の用途をストレージ管理の表示で確認する条件読解項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では DFSMS の# 機能と IDC3009I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明だけに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では# 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **# GDG Elements on Primary**

    - 検証目的: 置換追跡のストレージ管理について、# GDG Elements on Primaryは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、置換追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄に# GDG Elements on を指定し、OSKB020044の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND # GDG Elements on 
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM # GDG Elements on 
    CASE OSKB020044
    SOURCE DFSMS
    ```

    # GDG Elements on とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020044を同じ出力で読み、置換追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020044.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の # GDG Elements on  と OSKB020044 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Admin or User Command Backup {#c06-i0205}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Admin or User Command Backupは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。('BAS', 'ZOS31') を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 出力読解のストレージ管理に関する Admin 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず出力読解のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力読解のストレージ管理の証跡として保存して根拠にする。
    - C. Admin 機能の変更点を出力本文から切り離して出力読解のストレージ管理の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、出力読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では Admin 機能 は「Admin 機能の状態と出力メッセージを結び付ける出力読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では Admin 機能の出力行と IDC0001I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明だけに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では Admin 機能を DFSMS の確認記録に残し、対象名は出力読解対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Admin or User Command Backup**

    - 検証目的: 呼出追跡のストレージ管理について、Admin or User Command Backupは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で状態表示や操作を行うためのコマンド関連項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、呼出追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にAdmin or User Commを指定し、OSKB020043の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Admin or User Comm
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Admin or User Comm
    CASE OSKB020043
    SOURCE DFSMS
    ```

    Admin or User CommとOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020043を同じ出力で読み、呼出追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020043.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Admin or User Comm と OSKB020043 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Backup Frequency {#c06-i0206}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Backup Frequencyは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 終端読解のストレージ管理に関係する Backup Frequencyの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、終端読解の証跡として残す。 ✅
    - B. Backup Frequencyの名称と担当者名だけを残して終端読解のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端読解のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず終端読解のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では Backup Frequency は「Backup Frequencyの用途をストレージ管理の表示で確認する終端読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では DFSMS の Backup Frequencyと IDC0001I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明だけに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では Backup Frequencyを DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Backup Frequency**

    - 検証目的: 変更照合のストレージ管理について、Backup Frequencyは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、変更照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にBackup Frequencyを指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Backup Frequency
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Backup Frequency
    CASE OSKB020040
    SOURCE DFSMS
    ```

    Backup FrequencyとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020040を同じ出力で読み、変更照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020040.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Backup Frequency と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Command or Auto Migrate {#c06-i0207}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Command or Auto Migrateは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで状態表示や操作を行うためのコマンド関連項目です。AUTO/COMMAND/NONE。AUTO は HSM サイクルで自動マイグレート、COMMAND は HMIGRATE 限定、NONE は対象外

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 置換読解のストレージ管理に関する Command 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換読解のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換読解のストレージ管理の証跡として保存して根拠にする。
    - C. Command 機能の変更点を出力本文から切り離して置換読解のストレージ管理の承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を置換読解で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では Command 機能 は「Command 機能の状態と出力メッセージを結び付ける置換読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では Command 機能の出力行と IDC0001I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明だけに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では Command 機能を DFSMS の確認記録に残し、対象名は置換読解対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Command or Auto Migrate**

    - 検証目的: 監査照合のストレージ管理について、Command or Auto Migrateは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で状態表示や操作を行うためのコマンド関連項目です。AUに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCommand or Auto Miを指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Command or Auto Mi
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Command or Auto Mi
    CASE OSKB020039
    SOURCE DFSMS
    ```

    Command or Auto MiとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020039を同じ出力で読み、監査照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020039.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Command or Auto Mi と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Expire after Date/Days {#c06-i0208}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Expire after Date/Daysは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。作成からの絶対経過日数または絶対日付で期限切れ。固定保管期間用。「Expire after Date/Days」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 変更分離の・に関する Expire 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず変更分離の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更分離の・の証跡として保存して根拠にする。
    - C. Expire 機能の変更点を出力本文から切り離して変更分離の・の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、変更分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では Expire 機能 は「Expire 機能の状態と出力メッセージを結び付ける変更分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では Expire 機能の出力行と IDC3009I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明だけに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では Expire 機能を DFSMS の確認記録に残し、対象名は変更分離対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Expire after Date・ Days**

    - 検証目的: 順序照合の・について、Expire after Date/Daysは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、順序照合の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にExpire after Date・を指定し、OSKB020035の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Expire after Date・
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Expire after Date・
    CASE OSKB020035
    SOURCE DFSMS
    ```

    Expire after Date・とOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020035を同じ出力で読み、順序照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020035.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Expire after Date・ と OSKB020035 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Expire after Days Non-usage {#c06-i0209}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Expire after Days Non-usageは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 監査分離のストレージ管理でストレージ管理の運用確認を行います。Expire 機能の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査分離のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず監査分離のストレージ管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査分離の確認にする。 ✅
    - D. Expire 機能の属性行を読まず監査分離のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では Expire 機能 は「DFSMS で Expire 機能の扱いを記録する監査分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では Expire 機能の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明だけに寄り、判定名は監査分離不足です。監査分離資料では Expire 機能の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Expire after Days Non-usage**

    - 検証目的: 比較照合のストレージ管理について、Expire after Days Non-usageは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にExpire after Days を指定し、OSKB020034の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Expire after Days 
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Expire after Days 
    CASE OSKB020034
    SOURCE DFSMS
    ```

    Expire after Days とOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020034を同じ出力で読み、比較照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020034.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Expire after Days  と OSKB020034 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Level 1 Days Non-usage {#c06-i0210}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Level 1 Days Non-usageは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。ML1 から ML2 (テープ/仮想テープ) へ移送するまでの未参照日数。「Level 1 Days Non-usage」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 呼出読解のストレージ管理でストレージ管理の運用確認を行います。Level 機能の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出読解のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず呼出読解のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出読解の根拠を固定する。 ✅
    - D. Level 機能の属性行を読まず呼出読解のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では Level 機能 は「DFSMS で Level 機能の扱いを記録する呼出読解項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では Level 機能の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明だけに寄り、判定名は呼出読解不足です。呼出読解資料では Level 機能の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Level 1 Days Non-usage**

    - 検証目的: 復旧照合のストレージ管理について、Level 1 Days Non-usageは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にLevel 1 Days Non-uを指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Level 1 Days Non-u
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Level 1 Days Non-u
    CASE OSKB020038
    SOURCE DFSMS
    ```

    Level 1 Days Non-uとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020038を同じ出力で読み、復旧照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020038.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Level 1 Days Non-u と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Management Class 概要 {#c06-i0211}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

保持期限・マイグレーション・バックアップ・世代管理を宣言する SMS クラス。DFSMShsm のポリシードライバ

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 復旧分離の概要で Management 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Management 機能の出力を取らず復旧分離の概要の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧分離として引き継ぐ。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して復旧分離の概要の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧分離の概要へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では Management 機能 は「復旧分離の概要に関係する定義値と表示行を照合する復旧分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では Management 機能の属性行と IDC0001I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明だけに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では Management 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Management Class 概要**

    - 検証目的: 記録照合の概要について、保持期限・マイグレーション・バックアップ・世代管理を宣言する SMS クラス。DFSMShsm のポリシードライバに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録照合の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にManagement Class 概を指定し、OSKB020033の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Management Class 概
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Management Class 概
    CASE OSKB020033
    SOURCE DFSMS
    ```

    Management Class 概とOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020033を同じ出力で読み、記録照合の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020033.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Management Class 概 と OSKB020033 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Number of Backup Versions {#c06-i0212}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Number of Backup Versionsは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。保持するバックアップ世代数。Data Set Exists / Deleted 別に指定。「Number of Backup Versions」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 探索読解のストレージ管理で Number 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Number 機能の出力を取らず探索読解のストレージ管理の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、探索読解の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索読解のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索読解のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では Number 機能 は「探索読解のストレージ管理に関係する定義値と表示行を照合する探索読解項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では Number 機能の属性行と IDC3009I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明だけに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では Number 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索読解初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **Number of Backup Versions**

    - 検証目的: 比較照合のストレージ管理について、Number of Backup Versionsは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030034の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、比較照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にNumber of Backup Vを指定し、OSKB030034の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Number of Backup V
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Number of Backup V
    CASE OSKB030034
    SOURCE DFSMS
    ```

    Number of Backup VとOSKB030034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030034を同じ出力で読み、比較照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB030034.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB030034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Number of Backup V と OSKB030034 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB030034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Number of Backup Versions**

    - 検証目的: 構文追跡のストレージ管理について、Number of Backup Versionsは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にNumber of Backup Vを指定し、OSKB020041の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Number of Backup V
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Number of Backup V
    CASE OSKB020041
    SOURCE DFSMS
    ```

    Number of Backup VとOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020041を同じ出力で読み、構文追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020041.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Number of Backup V と OSKB020041 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Primary Days Non-usage {#c06-i0213}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Primary Days Non-usageは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 展開読解のストレージ管理で Primary 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Primary 機能の出力を取らず展開読解のストレージ管理の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開読解の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して展開読解のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開読解のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では Primary 機能 は「展開読解のストレージ管理に関係する定義値と表示行を照合する展開読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では Primary 機能の属性行と IDC0001I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明だけに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では Primary 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開読解初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Primary Days Non-usage**

    - 検証目的: 警告照合のストレージ管理について、Primary Days Non-usageは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、警告照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にPrimary Days Non-uを指定し、OSKB020037の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Primary Days Non-u
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Primary Days Non-u
    CASE OSKB020037
    SOURCE DFSMS
    ```

    Primary Days Non-uとOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020037を同じ出力で読み、警告照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020037.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Primary Days Non-u と OSKB020037 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Retain Days Only Backup Version {#c06-i0214}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Retain Days Only Backup Versionは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 上書読解のストレージ管理でストレージ管理の運用確認を行います。Retain 機能の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書読解のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず上書読解のストレージ管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書読解の根拠にする。 ✅
    - D. Retain 機能の属性行を読まず上書読解のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では Retain 機能 は「DFSMS で Retain 機能の扱いを記録する上書読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では Retain 機能の表示結果と IDC0001I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明だけに寄り、判定名は上書読解不足です。上書読解資料では Retain 機能の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Retain Days Only Backup Version**

    - 検証目的: 展開追跡のストレージ管理について、Retain Days Only Backup Versionは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、展開追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRetain Days Only Bを指定し、OSKB020042の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Retain Days Only B
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Retain Days Only B
    CASE OSKB020042
    SOURCE DFSMS
    ```

    Retain Days Only BとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020042を同じ出力で読み、展開追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020042.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Retain Days Only B と OSKB020042 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Retention Limit {#c06-i0215}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Retention Limitは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 構文読解のストレージ管理に関係する Retention Limitの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文読解で再確認できる形にする。 ✅
    - B. Retention Limitの名称と担当者名だけを残して構文読解のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で構文読解のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず構文読解のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では Retention Limit は「Retention Limitの用途をストレージ管理の表示で確認する構文読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では DFSMS の Retention Limitと IDC0001I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明だけに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では Retention Limitを DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **Retention Limit**

    - 検証目的: 記録照合のストレージ管理について、Retention Limitは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030033の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRetention Limitを指定し、OSKB030033の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Retention Limit
    CASE OSKB030033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Retention Limit
    CASE OSKB030033
    SOURCE DFSMS
    ```

    Retention LimitとOSKB030033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030033を同じ出力で読み、記録照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030033.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Retention Limit と OSKB030033 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Retention Limit**

    - 検証目的: 値域照合のストレージ管理について、Retention Limitは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRetention Limitを指定し、OSKB020036の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Retention Limit
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Retention Limit
    CASE OSKB020036
    SOURCE DFSMS
    ```

    Retention LimitとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020036を同じ出力で読み、値域照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020036.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Retention Limit と OSKB020036 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Rolled-off GDS Action {#c06-i0216}
*分類: SMS_MGMTCLAS*  ・  難易度: 上級

Rolled-off GDS Actionは、DFSMS / IDCAMS / VSAMのSMS_MGMTCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 区切読解のストレージ管理で Rolled-off 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Rolled-off 機能の出力を取らず区切読解のストレージ管理の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切読解として引き継ぐ。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して区切読解のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切読解のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では Rolled-off 機能 は「区切読解のストレージ管理に関係する定義値と表示行を照合する区切読解項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では Rolled-off 機能の属性行と IDC0001I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明だけに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では Rolled-off 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切読解初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Rolled-off GDS Action**

    - 検証目的: 終端追跡のストレージ管理について、Rolled-off GDS Actionは、DFSMS / IDCAMS / VSAM の SMS_MGMTCLAS で機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、終端追跡のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にRolled-off GDS Actを指定し、OSKB020045の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Rolled-off GDS Act
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Rolled-off GDS Act
    CASE OSKB020045
    SOURCE DFSMS
    ```

    Rolled-off GDS ActとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020045を同じ出力で読み、終端追跡のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020045.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Rolled-off GDS Act と OSKB020045 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration




## DFSMS / IDCAMS / VSAM > SMS_STORCLAS

### Accessibility {#c06-i0217}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Accessibilityは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 記録分離のストレージ管理に関係する Accessibilityの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、記録分離の証跡として残す。 ✅
    - B. Accessibilityの名称と担当者名だけを残して記録分離のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で記録分離のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず記録分離のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では Accessibility は「Accessibilityの用途をストレージ管理の表示で確認する記録分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では DFSMS の Accessibilityと IDC0001I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明だけに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では Accessibilityを DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Accessibility**

    - 検証目的: 出力照合のストレージ管理について、Accessibilityは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、出力照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にAccessibilityを指定し、OSKB020028の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Accessibility
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Accessibility
    CASE OSKB020028
    SOURCE DFSMS
    ```

    AccessibilityとOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020028を同じ出力で読み、出力照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020028.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Accessibility と OSKB020028 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Availability {#c06-i0218}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Availabilityは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。STANDARD/CONTINUOUS/CONTINUOUS_PREFERRED から選択。PPRC/HyperSwap 等のミラー構成を要求する場合に上げる

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 優先分離のストレージ管理に関する Availabilityの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず優先分離のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先分離のストレージ管理の証跡として保存して根拠にする。
    - C. Availabilityの変更点を出力本文から切り離して優先分離のストレージ管理の承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を優先分離で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では Availability は「Availabilityの状態と出力メッセージを結び付ける優先分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では Availabilityの出力行と IDC0001I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明だけに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では Availabilityを DFSMS の確認記録に残し、対象名は優先分離対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Availability**

    - 検証目的: 上書照合のストレージ管理について、Availabilityは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。STANDARD/Cに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にAvailabilityを指定し、OSKB020027の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Availability
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Availability
    CASE OSKB020027
    SOURCE DFSMS
    ```

    AvailabilityとOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020027を同じ出力で読み、上書照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020027.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Availability と OSKB020027 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### CF Cache / CF Lock Set {#c06-i0219}
*分類: SMS_STORCLAS*  ・  難易度: 上級

CF Cache / CF Lock Setは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 値域分離の・に関する CF Cache 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず値域分離の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域分離の・の証跡として保存して根拠にする。
    - C. CF Cache 属性の変更点を出力本文から切り離して値域分離の・の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、値域分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では CF Cache 属性 は「CF Cache 属性の状態と出力メッセージを結び付ける値域分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では CF Cache 属性の出力行と IDC0001I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明だけに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では CF Cache 属性を DFSMS の確認記録に残し、対象名は値域分離対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **CF Cache ・ CF Lock Set**

    - 検証目的: 優先照合の・について、CF Cache / CF Lock Setは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、優先照合の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCF Cache ・ CF Lockを指定し、OSKB030032の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CF Cache ・ CF Lock
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CF Cache ・ CF Lock
    CASE OSKB030032
    SOURCE DFSMS
    ```

    CF Cache ・ CF LockとOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030032を同じ出力で読み、優先照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030032.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の CF Cache ・ CF Lock と OSKB030032 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **CF Cache ・ CF Lock Set**

    - 検証目的: 範囲照合の・について、CF Cache / CF Lock Setは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、範囲照合の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCF Cache ・ CF Lockを指定し、OSKB020031の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CF Cache ・ CF Lock
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CF Cache ・ CF Lock
    CASE OSKB020031
    SOURCE DFSMS
    ```

    CF Cache ・ CF LockとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020031を同じ出力で読み、範囲照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020031.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の CF Cache ・ CF Lock と OSKB020031 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Direct Millisecond Response {#c06-i0220}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Direct Millisecond Responseは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 条件分離のストレージ管理に関係する Direct 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件分離で再確認できる形にする。 ✅
    - B. Direct 機能の名称と担当者名だけを残して条件分離のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で条件分離のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず条件分離のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では Direct 機能 は「Direct 機能の用途をストレージ管理の表示で確認する条件分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では DFSMS の Direct 機能と IDC0001I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明だけに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では Direct 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Direct Millisecond Response**

    - 検証目的: 置換照合のストレージ管理について、Direct Millisecond Responseは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にDirect Millisecondを指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Direct Millisecond
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Direct Millisecond
    CASE OSKB020024
    SOURCE DFSMS
    ```

    Direct MillisecondとOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020024を同じ出力で読み、置換照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020024.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Direct Millisecond と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Guaranteed Space {#c06-i0221}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Guaranteed Spaceは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。プライマリ全量を割り振り時に確保することを要求 (YES)。VSAM の前領域保証に使う。「Guaranteed Space」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 比較分離のストレージ管理で Guaranteed Spaceの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Guaranteed Spaceの出力を取らず比較分離のストレージ管理の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、比較分離の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して比較分離のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較分離のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では Guaranteed Space は「比較分離のストレージ管理に関係する定義値と表示行を照合する比較分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では Guaranteed Spaceの属性行と IDC3009I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明だけに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では Guaranteed Spaceを DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較分離初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Guaranteed Space**

    - 検証目的: 条件照合のストレージ管理について、Guaranteed Spaceは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。プライマリ全に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にGuaranteed Spaceを指定し、OSKB020029の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Guaranteed Space
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Guaranteed Space
    CASE OSKB020029
    SOURCE DFSMS
    ```

    Guaranteed SpaceとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020029を同じ出力で読み、条件照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020029.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Guaranteed Space と OSKB020029 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Guaranteed Synchronous Write {#c06-i0222}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Guaranteed Synchronous Writeは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 順序分離のストレージ管理でストレージ管理の運用確認を行います。Guaranteed 機能の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で順序分離のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず順序分離のストレージ管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序分離の根拠にする。 ✅
    - D. Guaranteed 機能の属性行を読まず順序分離のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では Guaranteed 機能 は「DFSMS で Guaranteed 機能の扱いを記録する順序分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では Guaranteed 機能の表示結果と IDC0001I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明だけに寄り、判定名は順序分離不足です。順序分離資料では Guaranteed 機能の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Guaranteed Synchronous Write**

    - 検証目的: 区切照合のストレージ管理について、Guaranteed Synchronous Writeは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にGuaranteed Synchroを指定し、OSKB020030の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Guaranteed Synchro
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Guaranteed Synchro
    CASE OSKB020030
    SOURCE DFSMS
    ```

    Guaranteed SynchroとOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020030を同じ出力で読み、区切照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020030.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Guaranteed Synchro と OSKB020030 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Initial Access Response Seconds {#c06-i0223}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Initial Access Response Secondsは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。初回アクセスまでの待ち時間目標 (秒)。マイグレーション再呼び戻し許容度を表現。「Initial Access Response Seconds」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 範囲分離のストレージ管理でストレージ管理の運用確認を行います。Initial 機能の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で範囲分離のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず範囲分離のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲分離の根拠を固定する。 ✅
    - D. Initial 機能の属性行を読まず範囲分離のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では Initial 機能 は「DFSMS で Initial 機能の扱いを記録する範囲分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では Initial 機能の表示結果と IDC3009I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明だけに寄り、判定名は範囲分離不足です。範囲分離資料では Initial 機能の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **Initial Access Response Seconds**

    - 検証目的: 範囲照合のストレージ管理について、Initial Access Response Secondsは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にInitial Access Resを指定し、OSKB030031の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Initial Access Res
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Initial Access Res
    CASE OSKB030031
    SOURCE DFSMS
    ```

    Initial Access ResとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030031を同じ出力で読み、範囲照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB030031.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Initial Access Res と OSKB030031 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB030031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **Initial Access Response Seconds**

    - 検証目的: 探索照合のストレージ管理について、Initial Access Response Secondsは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にInitial Access Resを指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Initial Access Res
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Initial Access Res
    CASE OSKB020026
    SOURCE DFSMS
    ```

    Initial Access ResとOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020026を同じ出力で読み、探索照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020026.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Initial Access Res と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Sequential Millisecond Response {#c06-i0224}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Sequential Millisecond Responseは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 区切分離のストレージ管理で Sequential 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Sequential 機能の出力を取らず区切分離のストレージ管理の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切分離の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して区切分離のストレージ管理の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切分離のストレージ管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では Sequential 機能 は「区切分離のストレージ管理に関係する定義値と表示行を照合する区切分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では Sequential 機能の属性行と IDC0001I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明だけに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では Sequential 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切分離初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Sequential Millisecond Response**

    - 検証目的: 終端照合のストレージ管理について、Sequential Millisecond Responseは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、終端照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にSequential Milliseを指定し、OSKB020025の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Sequential Millise
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Sequential Millise
    CASE OSKB020025
    SOURCE DFSMS
    ```

    Sequential MilliseとOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020025を同じ出力で読み、終端照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020025.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Sequential Millise と OSKB020025 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Storage Class 概要 {#c06-i0225}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Storage Class 概要は、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。性能・可用性要件をモデル化する SMS クラス。応答時間、可用性、CF キャッシュ利用などを宣言する。「Storage Class 概要」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 出力分離の概要に関する Storage Class 概要の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず出力分離の概要の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力分離の概要の証跡として保存して根拠にする。
    - C. Storage Class 概要の変更点を出力本文から切り離して出力分離の概要の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、出力分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では Storage Class 概要 は「Storage Class 概要の状態と出力メッセージを結び付ける出力分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では Storage Class 概要の出力行と IDC3009I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明だけに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では Storage Class 概要を DFSMS の確認記録に残し、対象名は出力分離対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Storage Class 概要**

    - 検証目的: 呼出照合の概要について、Storage Class 概要は、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。性能・可用性に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出照合の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にStorage Class 概要を指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Storage Class 概要
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Storage Class 概要
    CASE OSKB020023
    SOURCE DFSMS
    ```

    Storage Class 概要とOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020023を同じ出力で読み、呼出照合の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020023.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Storage Class 概要 と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Sustained Data Rate {#c06-i0226}
*分類: SMS_STORCLAS*  ・  難易度: 上級

Sustained Data Rateは、DFSMS / IDCAMS / VSAMのSMS_STORCLASで機能名、見出し、または確認対象として参照する項目です。求められる持続スループット (MB/s)。SSD/HDD 階層の選定根拠。「Sustained Data Rate」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（1問）"
    **問題.** 警告分離のストレージ管理に関係する Sustained 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、警告分離の採否を説明欄に結び付ける。 ✅
    - B. Sustained 機能の名称と担当者名だけを残して警告分離のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で警告分離のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず警告分離のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では Sustained 機能 は「Sustained 機能の用途をストレージ管理の表示で確認する警告分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では DFSMS の Sustained 機能と IDC3009I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明だけに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では Sustained 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Sustained Data Rate**

    - 検証目的: 優先照合のストレージ管理について、Sustained Data Rateは、DFSMS / IDCAMS / VSAM の SMS_STORCLAS で機能名、見出し、または確認対象として参照する項目です。求めらに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先照合のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にSustained Data Ratを指定し、OSKB020032の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Sustained Data Rat
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Sustained Data Rat
    CASE OSKB020032
    SOURCE DFSMS
    ```

    Sustained Data RatとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020032を同じ出力で読み、優先照合のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020032.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Sustained Data Rat と OSKB020032 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration




## DFSMS / IDCAMS / VSAM > SMS_STORGRP

### Allocation/Migration System ID {#c06-i0227}
*分類: SMS_STORGRP*  ・  難易度: 上級

Allocation/Migration System IDは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。システム単位での割り振り可否・マイグレーション可否を SMSplex で制御。「Allocation/Migration System ID」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 区切検分の・で Allocation 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Allocation 属性の出力を取らず区切検分の・の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、区切検分の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切検分の・の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切検分の・へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では Allocation 属性 は「区切検分の・に関係する定義値と表示行を照合する区切検分項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では Allocation 属性の属性行と IDC3009I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明だけに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では Allocation 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切検分初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 値域照合条件の値域照合として Allocation/Migration System  を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 承認欄の記入を優先して出力メッセージを保存しない。
    - B. 値域照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 名称と担当者名を保存して表示本文を確認しない。
    - D. 別分類の結果を流用して同じ証跡として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。値域照合条件で扱う Allocation/Migration System  は DFSMS / IDCAMS / VSAM の確認対象です（値域照合条件用語）。値域照合条件の担当者は値域照合として、表示本文とメッセージを照合します（値域照合条件照合）。値域照合条件の対応を残すと、後続担当者は同じ出典に戻って確認できます（値域照合条件出典）。A: 値域照合条件で表示とメッセージを結ぶ場合に根拠になります（値域照合条件A）。B: 値域照合条件で定義と出力の関係がない場合は追跡できません（値域照合条件B）。C: 値域照合条件で出典名のみでは実際の表示を説明できません（値域照合条件C）。D: 値域照合条件で操作記録のみでは値や状態の確認が不足します（値域照合条件D）。値域照合条件の初出用語として Allocation/Migration System  を扱い、分類内の確認名として保存します（値域照合条件終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Allocation・ Migration System ID**

    - 検証目的: 終端検査の・について、Allocation/Migration System ID は、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端検査の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にAllocation・ Migratを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Allocation・ Migrat
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Allocation・ Migrat
    CASE OSKB020065
    SOURCE DFSMS
    ```

    Allocation・ MigratとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020065を同じ出力で読み、終端検査の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020065.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Allocation・ Migrat と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Auto Migrate / Auto Backup / Auto Dump {#c06-i0228}
*分類: SMS_STORGRP*  ・  難易度: 上級

Auto Migrate / Auto Backup / Auto Dumpは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 出力検分の・に関する Auto Migrate 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず出力検分の・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力検分の・の証跡として保存して根拠にする。
    - C. Auto Migrate 属性の変更点を出力本文から切り離して出力検分の・の承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を出力検分で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では Auto Migrate 属性 は「Auto Migrate 属性の状態と出力メッセージを結び付ける出力検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では Auto Migrate 属性の出力行と IDC0001I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明だけに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では Auto Migrate 属性を DFSMS の確認記録に残し、対象名は出力検分対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 記録照合識別の記録照合として Auto Migrate / Auto Backup / を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 記録照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。記録照合識別で扱う Auto Migrate / Auto Backup / は DFSMS / IDCAMS / VSAM の確認対象です（記録照合識別用語）。記録照合識別の担当者は記録照合として、表示本文とメッセージを照合します（記録照合識別照合）。記録照合識別の対応を残すと、後続担当者は同じ出典に戻って確認できます（記録照合識別出典）。A: 記録照合識別で表示とメッセージを結ぶ場合に根拠になります（記録照合識別A）。B: 記録照合識別で定義と出力の関係がない場合は追跡できません（記録照合識別B）。C: 記録照合識別で出典名のみでは実際の表示を説明できません（記録照合識別C）。D: 記録照合識別で操作記録のみでは値や状態の確認が不足します（記録照合識別D）。記録照合識別の初出用語として Auto Migrate / Auto Backup / を扱い、分類内の確認名として保存します（記録照合識別終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200



### DUMMY {#c06-i0229}
*分類: SMS_STORGRP*  ・  難易度: 上級

DUMMYは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。ACS 段階で割り振り対象外にする目印プール。意図的な拒否経路の構築に使う。「DUMMY」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 上書検分のストレージ管理でストレージ管理の運用確認を行います。DUMMY の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書検分のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず上書検分のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書検分の根拠を固定する。 ✅
    - D. DUMMY の属性行を読まず上書検分のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では DUMMY は「DFSMS で DUMMY の扱いを記録する上書検分項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では DUMMY の表示結果と IDC3009I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明だけに寄り、判定名は上書検分不足です。上書検分資料では DUMMY の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 監査確認のストレージ管理でストレージ管理の運用確認を行います。DUMMY の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査確認のストレージ管理を確認した扱いにする。
    - B. IDC3009I の有無を確認せず監査確認のストレージ管理を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査確認の記録として扱う。 ✅
    - D. DUMMY の属性行を読まず監査確認のストレージ管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認のストレージ管理において選択記号 C を採用し、識別名は監査確認です。監査確認のストレージ管理において DUMMY は説明欄の「DFSMS で DUMMY の扱いを記録する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のストレージ管理を受け取る担当者は、DUMMY の表示結果と IDC3009I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のストレージ管理は別カテゴリの確認を流用しており、DUMMY の根拠にならないため監査確認ではありません。 B: 監査確認のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため監査確認ではありません。 C: 監査確認のストレージ管理は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のストレージ管理が示す DUMMY は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **DUMMY**

    - 検証目的: 展開検査のストレージ管理について、DUMMY は、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目です。ACS 段階で割り振り対象外にする目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開検査のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にDUMMYを指定し、OSKB020062の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND DUMMY
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM DUMMY
    CASE OSKB020062
    SOURCE DFSMS
    ```

    DUMMYとOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020062を同じ出力で読み、展開検査のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020062.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の DUMMY と OSKB020062 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Migrate Threshold (Low/High) {#c06-i0230}
*分類: SMS_STORGRP*  ・  難易度: 上級

Migrate Threshold (Low/High)は、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 条件検分の・に関係する Migrate 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、条件検分の証跡として残す。 ✅
    - B. Migrate 機能の名称と担当者名だけを残して条件検分の・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で条件検分の・を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず条件検分の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では Migrate 機能 は「Migrate 機能の用途をストレージ管理の表示で確認する条件検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景では DFSMS の Migrate 機能と IDC0001I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明だけに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では Migrate 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 変更照合更新の変更照合として Migrate Threshold (Low/High) を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 変更照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正解はAです。変更照合更新で扱う Migrate Threshold (Low/High) は DFSMS / IDCAMS / VSAM の確認対象です（変更照合更新用語）。変更照合更新の担当者は変更照合として、表示本文とメッセージを照合します（変更照合更新照合）。変更照合更新の対応を残すと、後続担当者は同じ出典に戻って確認できます（変更照合更新出典）。A: 変更照合更新で表示とメッセージを結ぶ場合に根拠になります（変更照合更新A）。B: 変更照合更新で定義と出力の関係がない場合は追跡できません（変更照合更新B）。C: 変更照合更新で出典名のみでは実際の表示を説明できません（変更照合更新C）。D: 変更照合更新で操作記録のみでは値や状態の確認が不足します（変更照合更新D）。変更照合更新の初出用語として Migrate Threshold (Low/High) を扱い、分類内の確認名として保存します（変更照合更新終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Migrate Threshold (Low・ High)**

    - 検証目的: 置換検査の・について、Migrate Threshold (Low/High)は、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換検査の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にMigrate Threshold を指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Migrate Threshold 
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Migrate Threshold 
    CASE OSKB020064
    SOURCE DFSMS
    ```

    Migrate Threshold とOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020064を同じ出力で読み、置換検査の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020064.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Migrate Threshold  と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### OBJECT / OBJECT BACKUP タイプ {#c06-i0231}
*分類: SMS_STORGRP*  ・  難易度: 上級

OBJECT / OBJECT BACKUP タイプは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 探索検分の・ タで OBJECT 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. OBJECT 属性の出力を取らず探索検分の・ タの説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索検分の確認値として扱う。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して探索検分の・ タの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索検分の・ タへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では OBJECT 属性 は「探索検分の・ タに関係する定義値と表示行を照合する探索検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では OBJECT 属性の属性行と IDC0001I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明だけに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では OBJECT 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索検分初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 範囲照合入力の範囲照合として OBJECT を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 範囲照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。範囲照合入力で扱う OBJECT は DFSMS / IDCAMS / VSAM の確認対象です（範囲照合入力用語）。範囲照合入力の担当者は範囲照合として、表示本文とメッセージを照合します（範囲照合入力照合）。範囲照合入力の対応を残すと、後続担当者は同じ出典に戻って確認できます（範囲照合入力出典）。A: 範囲照合入力で表示とメッセージを結ぶ場合に根拠になります（範囲照合入力A）。B: 範囲照合入力で定義と出力の関係がない場合は追跡できません（範囲照合入力B）。C: 範囲照合入力で出典名のみでは実際の表示を説明できません（範囲照合入力C）。D: 範囲照合入力で操作記録のみでは値や状態の確認が不足します（範囲照合入力D）。範囲照合入力の初出用語として OBJECT を扱い、分類内の確認名として保存します（範囲照合入力終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **OBJECT ・ OBJECT BACKUP タイプ**

    - 検証目的: 復旧照合の・ タについて、OBJECT / OBJECT BACKUP タイプは、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030038の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、復旧照合の・ タの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にOBJECT ・ OBJECT BAを指定し、OSKB030038の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND OBJECT ・ OBJECT BA
    CASE OSKB030038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM OBJECT ・ OBJECT BA
    CASE OSKB030038
    SOURCE DFSMS
    ```

    OBJECT ・ OBJECT BAとOSKB030038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030038を同じ出力で読み、復旧照合の・ タの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB030038
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB030038.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB030038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の OBJECT ・ OBJECT BA と OSKB030038 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB030038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration

    ---

    **OBJECT ・ OBJECT BACKUP タイプ**

    - 検証目的: 構文検査の・ タについて、OBJECT / OBJECT BACKUP タイプは、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、構文検査の・ タの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にOBJECT ・ OBJECT BAを指定し、OSKB020061の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND OBJECT ・ OBJECT BA
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM OBJECT ・ OBJECT BA
    CASE OSKB020061
    SOURCE DFSMS
    ```

    OBJECT ・ OBJECT BAとOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020061を同じ出力で読み、構文検査の・ タの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020061.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の OBJECT ・ OBJECT BA と OSKB020061 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### POOL タイプ {#c06-i0232}
*分類: SMS_STORGRP*  ・  難易度: 上級

POOL タイプは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 呼出検分のタイプでストレージ管理の運用確認を行います。POOL タイプの根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出検分のタイプを確認した扱いにする。
    - B. IDC0001I の有無を確認せず呼出検分のタイプを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出検分の確認にする。 ✅
    - D. POOL タイプの属性行を読まず呼出検分のタイプの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では POOL タイプ は「DFSMS で POOL タイプの扱いを記録する呼出検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では POOL タイプの表示結果と IDC0001I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明だけに寄り、判定名は呼出検分不足です。呼出検分資料では POOL タイプの使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 順序確認のタイプでストレージ管理の運用確認を行います。POOL タイプの根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で順序確認のタイプを確認した扱いにする。
    - B. IDC0001I の有無を確認せず順序確認のタイプを正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序確認の記録として扱う。 ✅
    - D. POOL タイプの属性行を読まず順序確認のタイプの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認のタイプにおいて選択記号 C を採用し、識別名は順序確認です。順序確認のタイプにおいて POOL タイプ は説明欄の「DFSMS で POOL タイプの扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のタイプを受け取る担当者は、POOL タイプの表示結果と IDC0001I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のタイプは別カテゴリの確認を流用しており、POOL タイプの根拠にならないため順序確認ではありません。 B: 順序確認のタイプは戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため順序確認ではありません。 C: 順序確認のタイプは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のタイプは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のタイプが示す POOL タイプは出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **POOL タイプ**

    - 検証目的: 復旧追跡のタイプについて、POOL タイプは、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、復旧追跡のタイプの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にPOOL タイプを指定し、OSKB020058の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND POOL タイプ
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM POOL タイプ
    CASE OSKB020058
    SOURCE DFSMS
    ```

    POOL タイプとOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020058を同じ出力で読み、復旧追跡のタイプの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020058.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の POOL タイプ と OSKB020058 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### Storage Group 概要 {#c06-i0233}
*分類: SMS_STORGRP*  ・  難易度: 上級

Storage Group 概要は、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 展開検分の概要で Storage Group 概要の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Storage Group 概要の出力を取らず展開検分の概要の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開検分として引き継ぐ。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して展開検分の概要の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開検分の概要へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では Storage Group 概要 は「展開検分の概要に関係する定義値と表示行を照合する展開検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では Storage Group 概要の属性行と IDC0001I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明だけに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では Storage Group 概要を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開検分初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 比較確認の概要で Storage Group 概要の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Storage Group 概要の出力を取らず比較確認の概要の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 ✅
    - C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して比較確認の概要の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の概要へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認の概要において選択記号 B を採用し、識別名は比較確認です。比較確認の概要において Storage Group 概要 は説明欄の「比較確認の概要に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の概要の証跡を読む担当者は、Storage Group 概要の属性行と IDC0001I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の概要は名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の概要は対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため比較確認ではありません。 D: 比較確認の概要は別カテゴリの確認を流用しており、Storage Group 概要の根拠にならないため比較確認ではありません。比較確認の概要に出る Storage Group 概要は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は比較確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Storage Group 概要**

    - 検証目的: 警告追跡の概要について、Storage Group 概要は、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、警告追跡の概要の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にStorage Group 概要を指定し、OSKB020057の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Storage Group 概要
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Storage Group 概要
    CASE OSKB020057
    SOURCE DFSMS
    ```

    Storage Group 概要とOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020057を同じ出力で読み、警告追跡の概要の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020057.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Storage Group 概要 と OSKB020057 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### TAPE タイプ {#c06-i0234}
*分類: SMS_STORGRP*  ・  難易度: 上級

TAPE タイプは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 終端検分のタイプに関係する TAPE タイプの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検分で再確認できる形にする。 ✅
    - B. TAPE タイプの名称と担当者名だけを残して終端検分のタイプの表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端検分のタイプを確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず終端検分のタイプの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では TAPE タイプ は「TAPE タイプの用途をストレージ管理の表示で確認する終端検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景では DFSMS の TAPE タイプと IDC0001I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明だけに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では TAPE タイプを DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 警告確認のタイプに関係する TAPE タイプの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 ✅
    - B. TAPE タイプの名称と担当者名のみを残して警告確認のタイプの表示本文を確認対象に含めない。
    - C. ストレージ管理以外の画面で警告確認のタイプを確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず警告確認のタイプの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認のタイプにおいて選択記号 A を採用し、識別名は警告確認です。警告確認のタイプにおいて TAPE タイプ は説明欄の「TAPE タイプの用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のタイプに関連して、DFSMS では TAPE タイプの表示属性と IDC0001I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のタイプは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のタイプは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のタイプは別カテゴリの確認を流用しており、TAPE タイプの根拠にならないため警告確認ではありません。 D: 警告確認のタイプは戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため警告確認ではありません。警告確認のタイプで使う TAPE タイプという用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は警告確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **TAPE タイプ**

    - 検証目的: 変更追跡のタイプについて、TAPE タイプは、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、変更追跡のタイプの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にTAPE タイプを指定し、OSKB020060の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND TAPE タイプ
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM TAPE タイプ
    CASE OSKB020060
    SOURCE DFSMS
    ```

    TAPE タイプとOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020060を同じ出力で読み、変更追跡のタイプの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020060.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の TAPE タイプ と OSKB020060 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration



### VIO タイプ {#c06-i0235}
*分類: SMS_STORGRP*  ・  難易度: 上級

VIO タイプは、DFSMS / IDCAMS / VSAMのSMS_STORGRPで機能名、見出し、または確認対象として参照する項目です。Virtual I/O 用一時データセット向けプール。RAM 上に置かれ高速。「VIO タイプ」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMSdfp Storage Administration

??? question "確認問題（2問）"
    **問題.** 置換検分のタイプに関する VIO タイプの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換検分のタイプの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換検分のタイプの証跡として保存して根拠にする。
    - C. VIO タイプの変更点を出力本文から切り離して置換検分のタイプの承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、置換検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では VIO タイプ は「VIO タイプの状態と出力メッセージを結び付ける置換検分項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では VIO タイプの出力行と IDC3009I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明だけに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では VIO タイプを DFSMS の確認記録に残し、対象名は置換検分対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 値域確認のタイプに関する VIO タイプの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))の結果を残さず値域確認のタイプの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のタイプの証跡として保存して根拠にする。
    - C. VIO タイプの変更点を出力本文から切り離して値域確認のタイプの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認のタイプにおいて選択記号 D を採用し、識別名は値域確認です。値域確認のタイプにおいて VIO タイプ は説明欄の「VIO タイプの状態と出力メッセージを結び付ける項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認のタイプに関する記録は、VIO タイプの出力行と IDC3009I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認のタイプは戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため値域確認ではありません。 B: 値域確認のタイプは別カテゴリの確認を流用しており、VIO タイプの根拠にならないため値域確認ではありません。 C: 値域確認のタイプは名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認のタイプは対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認のタイプで記録する VIO タイプは DFSMS の確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **VIO タイプ**

    - 検証目的: 監査追跡のタイプについて、VIO タイプは、DFSMS / IDCAMS / VSAM の SMS_STORGRP で機能名、見出し、または確認対象として参照する項目です。Virtual I/O 用一時デに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査追跡のタイプの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVIO タイプを指定し、OSKB020059の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VIO タイプ
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VIO タイプ
    CASE OSKB020059
    SOURCE DFSMS
    ```

    VIO タイプとOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020059を同じ出力で読み、監査追跡のタイプの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020059.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の VIO タイプ と OSKB020059 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMSdfp Storage Administration




## DFSMS / IDCAMS / VSAM > VERIFY

### VERIFY DATASET(name) {#c06-i0236}
*分類: VERIFY*  ・  難易度: 上級

名前指定で VERIFY 実行。動的割り振り経由で OPEN から CLOSE する。名前指定で VERIFY 実行。動的割り振り経由で OPEN→CLOSE する

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 上書記録のストレージ管理でストレージ管理の運用確認を行います。VERIFY DATASET 属性の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で上書記録のストレージ管理を確認した扱いにする。
    - B. IDC0005I の有無を確認せず上書記録のストレージ管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書記録の根拠を固定する。 ✅
    - D. VERIFY DATASET 属性の属性行を読まず上書記録のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では VERIFY DATASET 属性 は「DFSMS で VERIFY DATASET 属性の扱いを記録する上書記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では VERIFY DATASET 属性の表示結果と IDC0005I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明だけに寄り、判定名は上書記録不足です。上書記録資料では VERIFY DATASET 属性の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **VERIFY DATASET(name)**

    - 検証目的: 展開確認のストレージ管理について、名前指定で VERIFY 実行。動的割り振り経由で OPEN から CLOSE する。名前指定で VERIFY 実行。動的割り振り経由で OPEN から CLOSE するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020002の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、展開確認のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVERIFY DATASET(namを指定し、OSKB020002の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VERIFY DATASET(nam
    CASE OSKB020002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VERIFY DATASET(nam
    CASE OSKB020002
    SOURCE DFSMS
    ```

    VERIFY DATASET(namとOSKB020002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020002を同じ出力で読み、展開確認のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB020002
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB020002.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB020002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の VERIFY DATASET(nam と OSKB020002 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB020002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### VERIFY 効果 {#c06-i0237}
*分類: VERIFY*  ・  難易度: 上級

VERIFY 効果は、DFSMS / IDCAMS / VSAMのVERIFYで確認する項目です。クラスターの High-Used RBA / レコードカウント等を実体に基づき再計算。失敗続きの OPEN を救済する

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 出力記録の効果に関する VERIFY 効果の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)の結果を残さず出力記録の効果の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力記録の効果の証跡として保存して根拠にする。
    - C. VERIFY 効果の変更点を出力本文から切り離して出力記録の効果の承認欄だけ残す。
    - D. IDC0005I を含む表示を保存し、説明欄との差分を出力記録で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では VERIFY 効果 は「VERIFY 効果の状態と出力メッセージを結び付ける出力記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では VERIFY 効果の出力行と IDC0005I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明だけに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では VERIFY 効果を DFSMS の確認記録に残し、対象名は出力記録対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **VERIFY 効果**

    - 検証目的: 呼出確認の効果について、VERIFY 効果は、DFSMS / IDCAMS / VSAM の VERIFY で確認する項目です。クラスターの High-Used RBA / レコードカウント等を実体に基に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020003の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、呼出確認の効果の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVERIFY 効果を指定し、OSKB020003の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VERIFY 効果
    CASE OSKB020003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VERIFY 効果
    CASE OSKB020003
    SOURCE DFSMS
    ```

    VERIFY 効果とOSKB020003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020003を同じ出力で読み、呼出確認の効果の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB020003
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB020003.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB020003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の VERIFY 効果 と OSKB020003 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB020003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands



### VERIFY 基本 {#c06-i0238}
*分類: VERIFY*  ・  難易度: 上級

VSAM データセットのカタログ統計と実体を突き合わせ、未クローズによる不整合を修復する。CICS や OPEN 中異常終了後の常用処置

**出典:** z / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 探索記録の基本で VERIFY 基本の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VERIFY 基本の出力を取らず探索記録の基本の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索記録の確認値として扱う。 ✅
    - C. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)を省略して探索記録の基本の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索記録の基本へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では VERIFY 基本 は「探索記録の基本に関係する定義値と表示行を照合する探索記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では VERIFY 基本の属性行と IDC0005I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明だけに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では VERIFY 基本を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索記録初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **VERIFY 基本**

    - 検証目的: 探索照合の基本について、VSAM データセットのカタログ統計と実体を突き合わせ、未クローズによる不整合を修復する。CICS や OPEN 中異常終了後の常用処置に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030026の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、探索照合の基本の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVERIFY 基本を指定し、OSKB030026の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VERIFY 基本
    CASE OSKB030026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VERIFY 基本
    CASE OSKB030026
    SOURCE DFSMS
    ```

    VERIFY 基本とOSKB030026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB030026を同じ出力で読み、探索照合の基本の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB030026
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB030026.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB030026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の VERIFY 基本 と OSKB030026 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB030026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands

    ---

    **VERIFY 基本**

    - 検証目的: 構文確認の基本について、VSAM データセットのカタログ統計と実体を突き合わせ、未クローズによる不整合を修復する。CICS や OPEN 中異常終了後の常用処置に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020001の検証用出力を記録できる。
    - セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、構文確認の基本の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にVERIFY 基本を指定し、OSKB020001の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND VERIFY 基本
    CASE OSKB020001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM VERIFY 基本
    CASE OSKB020001
    SOURCE DFSMS
    ```

    VERIFY 基本とOSKB020001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020001を同じ出力で読み、構文確認の基本の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CASE OSKB020001
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
    CLUSTER ------- OSKB020001.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0005IとOSKB020001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
    ② ステップ2 の VERIFY 基本 と OSKB020001 が画面・出力に表示されること
    ③ ステップ3 の IDC0005I と OSKB020001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Access Method Services Commands




## DFSMS / IDCAMS / VSAM > VSAM_CONCEPTS

### AMP パラメータ (JCL) {#c06-i0239}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

DD 文 AMP= で VSAM のオープン時属性 (BUFND/BUFNI/AMORG/RECFM 等) を上書き。バッチ性能チューニングの常用手段

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（2問）"
    **問題.** 出力追跡再のパラメータに関する AMP パラメータ (JCL)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず出力追跡再のパラメータの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力追跡再のパラメータの証跡として保存して根拠にする。
    - C. AMP パラメータ (JCL)の変更点を出力本文から切り離して出力追跡再のパラメータの承認欄だけ残す。
    - D. IDC0001I を含む表示を保存し、説明欄との差分を出力追跡再で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡再正解では選択記号 D を採用し、正解名は出力追跡再正解です。出力追跡再根拠では AMP パラメータ (JCL) は「AMP パラメータ (JCL)の状態と出力メッセージを結び付ける出力追跡再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は出力追跡再根拠です。出力追跡再保存では AMP パラメータ (JCL)の出力行と IDC0001I を一緒に残し、保存名は出力追跡再保存です。選択肢ごとの違いを示します。 A: 出力追跡再欠落は戻り値や記録番号に寄り、欠落名は出力追跡再欠落です。 B: 出力追跡再流用は別カテゴリの確認であり、排除名は出力追跡再流用です。 C: 出力追跡再不足は名称や説明だけに寄り、判定名は出力追跡再不足です。 D: 出力追跡再正答は対象出力と項目説明を結び、根拠名は出力追跡再正答です。出力追跡再対象では AMP パラメータ (JCL)を DFSMS の確認記録に残し、対象名は出力追跡再対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 変更検査のパラメータに関する AMP パラメータ (JCL)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず変更検査のパラメータの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のパラメータの証跡として保存して根拠にする。
    - C. AMP パラメータ (JCL)の変更点を出力本文から切り離して変更検査のパラメータの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査のパラメータにおいて選択記号 D を採用し、識別名は変更検査です。変更検査のパラメータにおいて AMP パラメータ (JCL) は説明欄の「AMP パラメータ (JCL)の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査のパラメータに関する記録は、AMP パラメータ (JCL)の出力行と IDC0001I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査のパラメータは戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため変更検査ではありません。 B: 変更検査のパラメータは別カテゴリの確認を流用しており、AMP パラメータ (JCL)の根拠にならないため変更検査ではありません。 C: 変更検査のパラメータは名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査のパラメータは対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査のパラメータで記録する AMP パラメータ (JCL)は DFSMS の確認記録に残す対象名であり、用語名は変更検査です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **AMP パラメータ (JCL)**

    - 検証目的: 呼出記録のパラメータについて、DD 文 AMP= で VSAM のオープン時属性 (BUFND/BUFNI/AMORG/RECFM 等) を上書き。バッチ性能チューニングの常用手段に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020123の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、呼出記録のパラメータの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にAMP パラメータ (JCL)を指定し、OSKB020123の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND AMP パラメータ (JCL)
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM AMP パラメータ (JCL)
    CASE OSKB020123
    SOURCE DFSMS
    ```

    AMP パラメータ (JCL)とOSKB020123が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020123を同じ出力で読み、呼出記録のパラメータの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020123.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020123が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の AMP パラメータ (JCL) と OSKB020123 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### BUFND / BUFNI {#c06-i0240}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

BUFND / BUFNIは、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで確認する項目です。データ用/インデックス用バッファ数の指定。順次は BUFND を増やし、ランダムは BUFNI を増やすのが基本

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 条件追跡再の・に関係する BUFND ・ BUFNI の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、条件追跡再の証跡として残す。 ✅
    - B. BUFND ・ BUFNI の名称と担当者名だけを残して条件追跡再の・の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で条件追跡再の・を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず条件追跡再の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡再正解では選択記号 A を採用し、正解名は条件追跡再正解です。条件追跡再根拠では BUFND ・ BUFNI は「BUFND ・ BUFNI の用途をストレージ管理の表示で確認する条件追跡再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件追跡再根拠です。条件追跡再背景では DFSMS の BUFND ・ BUFNI と IDC0001I を同じ証跡に残し、背景名は条件追跡再背景です。他の選択肢を確認します。 A: 条件追跡再正答は対象出力と項目説明を結び、根拠名は条件追跡再正答です。 B: 条件追跡再不足は名称や説明だけに寄り、判定名は条件追跡再不足です。 C: 条件追跡再流用は別カテゴリの確認であり、排除名は条件追跡再流用です。 D: 条件追跡再欠落は戻り値や記録番号に寄り、欠落名は条件追跡再欠落です。条件追跡再用語では BUFND ・ BUFNI を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件追跡再用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **BUFND ・ BUFNI**

    - 検証目的: 置換記録の・について、BUFND / BUFNI は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で確認する項目です。データ用/インデックス用バッファ数の指定。順次は Bに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020124の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換記録の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にBUFND ・ BUFNIを指定し、OSKB020124の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND BUFND ・ BUFNI
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM BUFND ・ BUFNI
    CASE OSKB020124
    SOURCE DFSMS
    ```

    BUFND ・ BUFNIとOSKB020124が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020124を同じ出力で読み、置換記録の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020124.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020124が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の BUFND ・ BUFNI と OSKB020124 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### CI スプリット / CA スプリット {#c06-i0241}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

CI スプリット / CA スプリットは、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。FREESPACE 枯渇時に発生するインプレース分割。CA スプリットは物理データ移動を伴い高コスト。「CI スプリット / CA スプリット」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 構文追跡再のスプリット ・ スプリットに関係する CI スプリット 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、構文追跡再の採否を説明欄に結び付ける。 ✅
    - B. CI スプリット 属性の名称と担当者名だけを残して構文追跡再のスプリット ・ スプリットの表示本文を対象から外す。
    - C. ストレージ管理以外の画面で構文追跡再のスプリット ・ スプリットを確認し同じ証跡として扱ったことにする。
    - D. IDC3009I の有無を見ず構文追跡再のスプリット ・ スプリットの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡再正解では選択記号 A を採用し、正解名は構文追跡再正解です。構文追跡再根拠では CI スプリット 属性 は「CI スプリット 属性の用途をストレージ管理の表示で確認する構文追跡再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文追跡再根拠です。構文追跡再背景では DFSMS の CI スプリット 属性と IDC3009I を同じ証跡に残し、背景名は構文追跡再背景です。他の選択肢を確認します。 A: 構文追跡再正答は対象出力と項目説明を結び、根拠名は構文追跡再正答です。 B: 構文追跡再不足は名称や説明だけに寄り、判定名は構文追跡再不足です。 C: 構文追跡再流用は別カテゴリの確認であり、排除名は構文追跡再流用です。 D: 構文追跡再欠落は戻り値や記録番号に寄り、欠落名は構文追跡再欠落です。構文追跡再用語では CI スプリット 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文追跡再用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（2件）"
    **CI スプリット ・ CA スプリット**

    - 検証目的: 条件追跡のスプリット ・ スプリットについて、CI スプリット / CA スプリットは、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照する項目です。FRに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030049の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件追跡のスプリット ・ スプリットの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCI スプリット ・ CA スプリッを指定し、OSKB030049の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CI スプリット ・ CA スプリッ
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CI スプリット ・ CA スプリッ
    CASE OSKB030049
    SOURCE DFSMS
    ```

    CI スプリット ・ CA スプリッとOSKB030049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030049を同じ出力で読み、条件追跡のスプリット ・ スプリットの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB030049.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB030049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の CI スプリット ・ CA スプリッ と OSKB030049 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB030049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

    ---

    **CI スプリット ・ CA スプリット**

    - 検証目的: 値域整理のスプリット ・ スプリットについて、CI スプリット / CA スプリットは、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照する項目です。FRに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域整理のスプリット ・ スプリットの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にCI スプリット ・ CA スプリッを指定し、OSKB020116の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND CI スプリット ・ CA スプリッ
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM CI スプリット ・ CA スプリッ
    CASE OSKB020116
    SOURCE DFSMS
    ```

    CI スプリット ・ CA スプリッとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020116を同じ出力で読み、値域整理のスプリット ・ スプリットの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020116.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の CI スプリット ・ CA スプリッ と OSKB020116 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### Control Area (CA) {#c06-i0242}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

Control Area (CA)は、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで確認する項目です。複数 CI を束ねた割り振り/分割単位。通常 1 シリンダーまたは複数トラック。CA スプリットは性能影響が大きい

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（2問）"
    **問題.** 変更照合再のストレージ管理に関する Control Area (CA)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず変更照合再のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更照合再のストレージ管理の証跡として保存して根拠にする。
    - C. Control Area (CA)の変更点を出力本文から切り離して変更照合再のストレージ管理の承認欄だけ残す。
    - D. 同じ画面で対象行と IDC0001I を読み、変更照合再の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合再正解では選択記号 D を採用し、正解名は変更照合再正解です。変更照合再根拠では Control Area (CA) は「Control Area (CA)の状態と出力メッセージを結び付ける変更照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は変更照合再根拠です。変更照合再保存では Control Area (CA)の出力行と IDC0001I を一緒に残し、保存名は変更照合再保存です。選択肢ごとの違いを示します。 A: 変更照合再欠落は戻り値や記録番号に寄り、欠落名は変更照合再欠落です。 B: 変更照合再流用は別カテゴリの確認であり、排除名は変更照合再流用です。 C: 変更照合再不足は名称や説明だけに寄り、判定名は変更照合再不足です。 D: 変更照合再正答は対象出力と項目説明を結び、根拠名は変更照合再正答です。変更照合再対象では Control Area (CA)を DFSMS の確認記録に残し、対象名は変更照合再対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 優先検査のストレージ管理に関する Control Area (CA)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず優先検査のストレージ管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のストレージ管理の証跡として保存して根拠にする。
    - C. Control Area (CA)の変更点を出力本文から切り離して優先検査のストレージ管理の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検査のストレージ管理において選択記号 D を採用し、識別名は優先検査です。優先検査のストレージ管理において Control Area (CA) は説明欄の「Control Area (CA)の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査のストレージ管理に関する記録は、Control Area (CA)の出力行と IDC0001I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため優先検査ではありません。 B: 優先検査のストレージ管理は別カテゴリの確認を流用しており、Control Area (CA)の根拠にならないため優先検査ではありません。 C: 優先検査のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査のストレージ管理は対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査のストレージ管理で記録する Control Area (CA)は DFSMS の確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Control Area (CA)**

    - 検証目的: 順序整理のストレージ管理について、Control Area (CA)は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で確認する項目です。複数 CI を束ねた割り振り/分割単位。通常に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にControl Area (CA)を指定し、OSKB020115の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Control Area (CA)
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Control Area (CA)
    CASE OSKB020115
    SOURCE DFSMS
    ```

    Control Area (CA)とOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020115を同じ出力で読み、順序整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020115.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Control Area (CA) と OSKB020115 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### Control Interval (CI) {#c06-i0243}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

VSAM の入出力単位。複数論理レコード + RDF + CIDF からなる物理ブロックで、CISZ で大きさを決める

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 監査照合再のストレージ管理でストレージ管理の運用確認を行います。Control 機能の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で監査照合再のストレージ管理を確認した扱いにする。
    - B. IDC0001I の有無を確認せず監査照合再のストレージ管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査照合再の根拠にする。 ✅
    - D. Control 機能の属性行を読まず監査照合再のストレージ管理の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合再正解では選択記号 C を採用し、正解名は監査照合再正解です。監査照合再根拠では Control 機能 は「DFSMS で Control 機能の扱いを記録する監査照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査照合再根拠です。監査照合再受渡では Control 機能の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査照合再受渡です。不適切な選択肢を整理します。 A: 監査照合再流用は別カテゴリの確認であり、排除名は監査照合再流用です。 B: 監査照合再欠落は戻り値や記録番号に寄り、欠落名は監査照合再欠落です。 C: 監査照合再正答は対象出力と項目説明を結び、根拠名は監査照合再正答です。 D: 監査照合再不足は名称や説明だけに寄り、判定名は監査照合再不足です。監査照合再資料では Control 機能の使い方を出典欄から追跡し、資料名は監査照合再資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Control Interval (CI)**

    - 検証目的: 比較整理のストレージ管理について、VSAM の入出力単位。複数論理レコード + RDF + CIDF からなる物理ブロックで、CISZ で大きさを決めるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にControl Interval (を指定し、OSKB020114の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Control Interval (
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Control Interval (
    CASE OSKB020114
    SOURCE DFSMS
    ```

    Control Interval (とOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020114を同じ出力で読み、比較整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020114.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Control Interval ( と OSKB020114 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### Extended Format VSAM {#c06-i0244}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

Extended Format VSAMは、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Using Data Sets / z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 終端追跡再のストレージ管理に関係する Extended 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端追跡再で再確認できる形にする。 ✅
    - B. Extended 機能の名称と担当者名だけを残して終端追跡再のストレージ管理の表示本文を対象から外す。
    - C. ストレージ管理以外の画面で終端追跡再のストレージ管理を確認し同じ証跡として扱ったことにする。
    - D. IDC0001I の有無を見ず終端追跡再のストレージ管理の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡再正解では選択記号 A を採用し、正解名は終端追跡再正解です。終端追跡再根拠では Extended 機能 は「Extended 機能の用途をストレージ管理の表示で確認する終端追跡再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は終端追跡再根拠です。終端追跡再背景では DFSMS の Extended 機能と IDC0001I を同じ証跡に残し、背景名は終端追跡再背景です。他の選択肢を確認します。 A: 終端追跡再正答は対象出力と項目説明を結び、根拠名は終端追跡再正答です。 B: 終端追跡再不足は名称や説明だけに寄り、判定名は終端追跡再不足です。 C: 終端追跡再流用は別カテゴリの確認であり、排除名は終端追跡再流用です。 D: 終端追跡再欠落は戻り値や記録番号に寄り、欠落名は終端追跡再欠落です。終端追跡再用語では Extended 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端追跡再用語です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Extended Format VSAM**

    - 検証目的: 変更整理のストレージ管理について、Extended Format VSAM は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、変更整理のストレージ管理の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にExtended Format VSを指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Extended Format VS
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Extended Format VS
    CASE OSKB020120
    SOURCE DFSMS
    ```

    Extended Format VSとOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020120を同じ出力で読み、変更整理のストレージ管理の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020120.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Extended Format VS と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### HURBA / HARBA {#c06-i0245}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

HURBA / HARBAは、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Using Data Sets / z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（1問）"
    **問題.** 展開追跡再の・で HURBA ・ HARBA の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. HURBA ・ HARBA の出力を取らず展開追跡再の・の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開追跡再として引き継ぐ。 ✅
    - C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して展開追跡再の・の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開追跡再の・へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡再正解では選択記号 B を採用し、正解名は展開追跡再正解です。展開追跡再根拠では HURBA ・ HARBA は「展開追跡再の・に関係する定義値と表示行を照合する展開追跡再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は展開追跡再根拠です。展開追跡再追跡では HURBA ・ HARBA の属性行と IDC0001I を合わせ、追跡名は展開追跡再追跡です。誤答側の問題点を分けます。 A: 展開追跡再不足は名称や説明だけに寄り、判定名は展開追跡再不足です。 B: 展開追跡再正答は対象出力と項目説明を結び、根拠名は展開追跡再正答です。 C: 展開追跡再欠落は戻り値や記録番号に寄り、欠落名は展開追跡再欠落です。 D: 展開追跡再流用は別カテゴリの確認であり、排除名は展開追跡再流用です。展開追跡再初出では HURBA ・ HARBA を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開追跡再初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **HURBA ・ HARBA**

    - 検証目的: 警告整理の・について、HURBA / HARBA は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、警告整理の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にHURBA ・ HARBAを指定し、OSKB020117の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND HURBA ・ HARBA
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM HURBA ・ HARBA
    CASE OSKB020117
    SOURCE DFSMS
    ```

    HURBA ・ HARBAとOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020117を同じ出力で読み、警告整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020117.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の HURBA ・ HARBA と OSKB020117 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### Reorganization (再編成) {#c06-i0246}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

Reorganization (再編成)は、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。REPRO アウト から 新クラスター DEFINE から REPRO イン で論理順位再構築。FREESPACE 復元、CA スプリット解消に必須。REPRO アウト→新クラスター DEFINE→REPRO イン で論理順位再構築。FREESPACE 復元、CA スプリット解消に必須

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（2問）"
    **問題.** 区切追跡再の再編成で Reorganization 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Reorganization 属性の出力を取らず区切追跡再の再編成の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、区切追跡再の確認記録にまとめる。 ✅
    - C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切追跡再の再編成の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切追跡再の再編成へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡再正解では選択記号 B を採用し、正解名は区切追跡再正解です。区切追跡再根拠では Reorganization 属性 は「区切追跡再の再編成に関係する定義値と表示行を照合する区切追跡再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切追跡再根拠です。区切追跡再追跡では Reorganization 属性の属性行と IDC3009I を合わせ、追跡名は区切追跡再追跡です。誤答側の問題点を分けます。 A: 区切追跡再不足は名称や説明だけに寄り、判定名は区切追跡再不足です。 B: 区切追跡再正答は対象出力と項目説明を結び、根拠名は区切追跡再正答です。 C: 区切追跡再欠落は戻り値や記録番号に寄り、欠落名は区切追跡再欠落です。 D: 区切追跡再流用は別カテゴリの確認であり、排除名は区切追跡再流用です。区切追跡再初出では Reorganization 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切追跡再初出です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 展開判定の再編成で Reorganization (再編成)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Reorganization (再編成)の出力を取らず展開判定の再編成の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開判定の確認結果にする。 ✅
    - C. DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を省略して展開判定の再編成の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の再編成へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開判定の再編成において選択記号 B を採用し、識別名は展開判定です。展開判定の再編成において Reorganization (再編成) は説明欄の「展開判定の再編成に関係する定義値と表示行を照合する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は展開判定です。展開判定の再編成の証跡を読む担当者は、Reorganization (再編成)の属性行と IDC3009I を合わせて追跡し、背景名は展開判定です。誤答側の問題点を分けます。 A: 展開判定の再編成は名称や説明のみに寄り、状態を示す出力本文が不足するため展開判定ではありません。 B: 展開判定の再編成は対象出力と項目説明を結び、根拠を残すので展開判定です。 C: 展開判定の再編成は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため展開判定ではありません。 D: 展開判定の再編成は別カテゴリの確認を流用しており、Reorganization (再編成)の根拠にならないため展開判定ではありません。展開判定の再編成に出る Reorganization (再編成)は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は展開判定です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Reorganization (再編成)**

    - 検証目的: 終端記録の再編成について、Reorganization (再編成)は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照する項目です。Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020125の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端記録の再編成の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にReorganization (再編を指定し、OSKB020125の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Reorganization (再編
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Reorganization (再編
    CASE OSKB020125
    SOURCE DFSMS
    ```

    Reorganization (再編とOSKB020125が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020125を同じ出力で読み、終端記録の再編成の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020125.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020125が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Reorganization (再編 と OSKB020125 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### Sequence Set / Index Set {#c06-i0247}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

Sequence Set / Index Setは、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。KSDS インデックスの 2 階層。Sequence Set は CI へのポインタ、Index Set は Sequence Set へのツリー

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（2問）"
    **問題.** 呼出追跡再の・でストレージ管理の運用確認を行います。Sequence Set 属性の根拠にできる作業はどれですか。

    - A. DFSMS と無関係な一覧で呼出追跡再の・を確認した扱いにする。
    - B. IDC0001I の有無を確認せず呼出追跡再の・を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡再の確認にする。 ✅
    - D. Sequence Set 属性の属性行を読まず呼出追跡再の・の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡再正解では選択記号 C を採用し、正解名は呼出追跡再正解です。呼出追跡再根拠では Sequence Set 属性 は「DFSMS で Sequence Set 属性の扱いを記録する呼出追跡再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は呼出追跡再根拠です。呼出追跡再受渡では Sequence Set 属性の表示結果と IDC0001I を同じ確認単位にし、受渡名は呼出追跡再受渡です。不適切な選択肢を整理します。 A: 呼出追跡再流用は別カテゴリの確認であり、排除名は呼出追跡再流用です。 B: 呼出追跡再欠落は戻り値や記録番号に寄り、欠落名は呼出追跡再欠落です。 C: 呼出追跡再正答は対象出力と項目説明を結び、根拠名は呼出追跡再正答です。 D: 呼出追跡再不足は名称や説明だけに寄り、判定名は呼出追跡再不足です。呼出追跡再資料では Sequence Set 属性の使い方を出典欄から追跡し、資料名は呼出追跡再資料です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 復旧照合権限の復旧照合として Sequence Set / Index Set を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 復旧照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解はCです。復旧照合権限で扱う Sequence Set / Index Set は DFSMS / IDCAMS / VSAM の確認対象です（復旧照合権限用語）。復旧照合権限の担当者は復旧照合として、表示本文とメッセージを照合します（復旧照合権限照合）。復旧照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（復旧照合権限出典）。A: 復旧照合権限で表示とメッセージを結ぶ場合に根拠になります（復旧照合権限A）。B: 復旧照合権限で定義と出力の関係がない場合は追跡できません（復旧照合権限B）。C: 復旧照合権限で出典名のみでは実際の表示を説明できません（復旧照合権限C）。D: 復旧照合権限で操作記録のみでは値や状態の確認が不足します（復旧照合権限D）。復旧照合権限の初出用語として Sequence Set / Index Set を扱い、分類内の確認名として保存します（復旧照合権限終点）。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Sequence Set ・ Index Set**

    - 検証目的: 復旧整理の・について、Sequence Set / Index Setは、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。
    - セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、復旧整理の・の確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にSequence Set ・ Indを指定し、OSKB020118の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Sequence Set ・ Ind
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Sequence Set ・ Ind
    CASE OSKB020118
    SOURCE DFSMS
    ```

    Sequence Set ・ IndとOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020118を同じ出力で読み、復旧整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
    CLUSTER ------- OSKB020118.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC0001IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
    ② ステップ2 の Sequence Set ・ Ind と OSKB020118 が画面・出力に表示されること
    ③ ステップ3 の IDC0001I と OSKB020118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands



### Spanned Record と SPANNED 属性 {#c06-i0248}
*分類: VSAM_CONCEPTS*  ・  難易度: 上級

Spanned Record と SPANNED 属性は、DFSMS / IDCAMS / VSAMのVSAM_CONCEPTSで機能名、見出し、または確認対象として参照する項目です。1 レコードが複数 CI に跨る形式。RECORDSIZE が CISZ を超える設計で使う。インデックスは Spanned 不可。「Spanned Record と SPANNED 属性」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい

**出典:** z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands

??? question "確認問題（2問）"
    **問題.** 置換追跡再のストレージ管理に関する Spanned 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換追跡再のストレージ管理の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換追跡再のストレージ管理の証跡として保存して根拠にする。
    - C. Spanned 機能の変更点を出力本文から切り離して置換追跡再のストレージ管理の承認欄だけ残す。
    - D. DFSMS の表示形式に沿って根拠行を採り、置換追跡再の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡再正解では選択記号 D を採用し、正解名は置換追跡再正解です。置換追跡再根拠では Spanned 機能 は「Spanned 機能の状態と出力メッセージを結び付ける置換追跡再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換追跡再根拠です。置換追跡再保存では Spanned 機能の出力行と IDC3009I を一緒に残し、保存名は置換追跡再保存です。選択肢ごとの違いを示します。 A: 置換追跡再欠落は戻り値や記録番号に寄り、欠落名は置換追跡再欠落です。 B: 置換追跡再流用は別カテゴリの確認であり、排除名は置換追跡再流用です。 C: 置換追跡再不足は名称や説明だけに寄り、判定名は置換追跡再不足です。 D: 置換追跡再正答は対象出力と項目説明を結び、根拠名は置換追跡再正答です。置換追跡再対象では Spanned 機能を DFSMS の確認記録に残し、対象名は置換追跡再対象です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200

    ---

    **問題.** 値域検査のとに関する Spanned Record と SPANNED の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))の結果を残さず値域検査のとの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のとの証跡として保存して根拠にする。
    - C. Spanned Record と SPANNED の変更点を出力本文から切り離して値域検査のとの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検査のとにおいて選択記号 D を採用し、識別名は値域検査です。値域検査のとにおいて Spanned Record と SPANNED は説明欄の「Spanned Record と SPANNED の状態と出力メッセージを結び付ける項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査のとに関する記録は、Spanned Record と SPANNED の出力行と IDC3009I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査のとは戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため値域検査ではありません。 B: 値域検査のとは別カテゴリの確認を流用しており、Spanned Record と SPANNED の根拠にならないため値域検査ではありません。 C: 値域検査のとは名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査のとは対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査のとで記録する Spanned Record と SPANNED は DFSMS の確認記録に残す対象名であり、用語名は値域検査です。

    **出典:** zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200


??? note "検証手順（1件）"
    **Spanned Record と SPANNED 属性**

    - 検証目的: 監査整理のとについて、Spanned Record と SPANNED 属性は、DFSMS / IDCAMS / VSAM の VSAM_CONCEPTS で機能名、見出し、または確認対象として参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。
    - セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===> に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査整理のとの確認表示へ進みます。
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
    現在の画面はIDCAMSの表示結果です。FIND欄にSpanned Record と Sを指定し、OSKB020119の対象行を見つけます。
    操作（入力）:
    ```text
    (IDCAMS Result)
    COMMAND INPUT ===> FIND Spanned Record と S
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IDCAMS Result)
    ITEM Spanned Record と S
    CASE OSKB020119
    SOURCE DFSMS
    ```

    Spanned Record と SとOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020119を同じ出力で読み、監査整理のとの根拠を記録します。
    操作（入力）:
    ```text
    (IDCAMS Detail)
    COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    IDCAMS  SYSTEM SERVICES
    /* IDCAMS COMMAND */
       DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
    CLUSTER ------- OSKB020119.CLUSTER
    IN-CAT --- SYS1.MASTER.CATALOG
    IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
    ```

    IDC3009IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
    ② ステップ2 の Spanned Record と S と OSKB020119 が画面・出力に表示されること
    ③ ステップ3 の IDC3009I と OSKB020119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS DFSMS Using Data Sets / OS DFSMS Access Method Services Commands


