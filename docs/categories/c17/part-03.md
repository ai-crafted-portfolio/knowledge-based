---
search:
  exclude: true
---

# JCL DD 文 — 詳細 (3/3)

[← JCL DD 文 の概要へ戻る](index.md)


## JCL DD 文 > USS-PATH

### PATHOPTS=OEXCL {#c17-i0188}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=OEXCLは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。OCREAT と併用して、既存なら失敗 (排他的作成)。「PATHOPTS=OEXCL」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 復旧読解のジョブデータ定義で PATHOPTS=OEXCL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHOPTS=OEXCL の出力を取らず復旧読解のジョブデータ定義の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧読解の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して復旧読解のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧読解のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では PATHOPTS=OEXCL は「復旧読解のジョブデータ定義に関係する定義値と表示行を照合する復旧読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では PATHOPTS=OEXCL の属性行と IEF236I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明だけに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では PATHOPTS=OEXCL を JCL DD 文の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 区切確認のジョブデータ定義で PATHOPTS=OEXCL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHOPTS=OEXCL の出力を取らず区切確認のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 ✅
    - C. ST OSKBDD を省略して区切確認のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認のジョブデータ定義において選択記号 B を採用し、識別名は区切確認です。区切確認のジョブデータ定義において PATHOPTS=OEXCL は説明欄の「区切確認のジョブデータ定義に関係する定義値と表示行を照合する区切確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認のジョブデータ定義の証跡を読む担当者は、PATHOPTS=OEXCL の属性行と IEF236I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため区切確認ではありません。 D: 区切確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=OEXCL の根拠にならないため区切確認ではありません。区切確認のジョブデータ定義に出る PATHOPTS=OEXCL は JCL DD 文の運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=OEXCL**

    - 検証目的: 記録追跡のジョブデータ定義について、PATHOPTS=OEXCL は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。OCREAT と併用して、既存なら失敗 (排他的作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OEXCLを指定し、OSKB020053の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OEXCL
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OEXCL
    CASE OSKB020053
    SOURCE z/OS JCL
    ```

    PATHOPTS=OEXCLとOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020053を同じ出力で読み、記録追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020053
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020053.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020053 STEP1 SYSUT1
    ```

    IEF236IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OEXCL と OSKB020053 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=ONOCTTY {#c17-i0189}
*分類: USS-PATH*  ・  難易度: 中級

端末となり得るファイルでも制御端末にしない。「PATHOPTS=ONOCTTY」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 変更読解のジョブデータ定義に関する PATHOPTS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず変更読解のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更読解のジョブデータ定義の証跡として保存して根拠にする。
    - C. PATHOPTS 属性の変更点を出力本文から切り離して変更読解のジョブデータ定義の承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、変更読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では PATHOPTS 属性 は「PATHOPTS 属性の状態と出力メッセージを結び付ける変更読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では PATHOPTS 属性の出力行と IEF236I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明だけに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では PATHOPTS 属性をz/OS JCL の確認記録に残し、対象名は変更読解対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 優先確認のジョブデータ定義に関する PATHOPTS=ONOCTTY の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先確認のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認のジョブデータ定義の証跡として保存して根拠にする。
    - C. PATHOPTS=ONOCTTY の変更点を出力本文から切り離して優先確認のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認のジョブデータ定義において選択記号 D を採用し、識別名は優先確認です。優先確認のジョブデータ定義において PATHOPTS=ONOCTTY は説明欄の「PATHOPTS=ONOCTTY の状態と出力メッセージを結び付ける優先確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認のジョブデータ定義に関する記録は、PATHOPTS=ONOCTTY の出力行と IEF236I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため優先確認ではありません。 B: 優先確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=ONOCTTY の根拠にならないため優先確認ではありません。 C: 優先確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認のジョブデータ定義で記録する PATHOPTS=ONOCTTY はz/OS JCL の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=ONOCTTY**

    - 検証目的: 順序追跡のジョブデータ定義について、端末となり得るファイルでも制御端末にしない。「PATHOPTS=ONOCTTY」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=ONOCTTYを指定し、OSKB020055の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=ONOCTTY
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=ONOCTTY
    CASE OSKB020055
    SOURCE z/OS JCL
    ```

    PATHOPTS=ONOCTTYとOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020055を同じ出力で読み、順序追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020055
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020055.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020055 STEP1 SYSUT1
    ```

    IEF236IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=ONOCTTY と OSKB020055 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=ONONBLOCK {#c17-i0190}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=ONONBLOCKは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。ノンブロッキングモードでオープン。FIFO 等で意味を持つ。「PATHOPTS=ONONBLOCK」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 構文検分のジョブデータ定義に関係する PATHOPTS 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD で得た表示本文を使い、構文検分の採否を説明欄に結び付ける。 ✅
    - B. PATHOPTS 属性の名称と担当者名だけを残して構文検分のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で構文検分のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文検分のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では PATHOPTS 属性 は「PATHOPTS 属性の用途をジョブデータ定義の表示で確認する構文検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景ではz/OS JCL の PATHOPTS 属性と IEF236I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明だけに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では PATHOPTS 属性を JCL DD 文で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 記録確認のジョブデータ定義に関係する PATHOPTS=ONONBLOCK の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録確認として残す。 ✅
    - B. PATHOPTS=ONONBLOCK の名称と担当者名のみを残して記録確認のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で記録確認のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録確認のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認のジョブデータ定義において選択記号 A を採用し、識別名は記録確認です。記録確認のジョブデータ定義において PATHOPTS=ONONBLOCK は説明欄の「PATHOPTS=ONONBLOCK の用途をジョブデータ定義の表示で確認する記録確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認のジョブデータ定義に関連して、z/OS JCL では PATHOPTS=ONONBLOCK の表示属性と IEF236I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=ONONBLOCK の根拠にならないため記録確認ではありません。 D: 記録確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため記録確認ではありません。記録確認のジョブデータ定義で使う PATHOPTS=ONONBLOCK という用語は JCL DD 文で扱う確認対象であり、用語名は記録確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **PATHOPTS=ONONBLOCK**

    - 検証目的: 警告照合のジョブデータ定義について、PATHOPTS=ONONBLOCK は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。ノンブロッキングモードでオープン。FIFOに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030037の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、警告照合のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=ONONBLOCKを指定し、OSKB030037の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=ONONBLOCK
    CASE OSKB030037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=ONONBLOCK
    CASE OSKB030037
    SOURCE z/OS JCL
    ```

    PATHOPTS=ONONBLOCKとOSKB030037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030037を同じ出力で読み、警告照合のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030037
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030037
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030037.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030037 STEP1 SYSUT1
    ```

    IEF236IとOSKB030037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=ONONBLOCK と OSKB030037 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PATHOPTS=ONONBLOCK**

    - 検証目的: 値域追跡のジョブデータ定義について、PATHOPTS=ONONBLOCK は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。ノンブロッキングモードでオープン。FIFOに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=ONONBLOCKを指定し、OSKB020056の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=ONONBLOCK
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=ONONBLOCK
    CASE OSKB020056
    SOURCE z/OS JCL
    ```

    PATHOPTS=ONONBLOCKとOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020056を同じ出力で読み、値域追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020056
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020056.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020056 STEP1 SYSUT1
    ```

    IEF236IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=ONONBLOCK と OSKB020056 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=ORDONLY {#c17-i0191}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=ORDONLYは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 記録読解のジョブデータ定義に関係する PATHOPTS 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録読解で再確認できる形にする。 ✅
    - B. PATHOPTS 属性の名称と担当者名だけを残して記録読解のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で記録読解のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録読解のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では PATHOPTS 属性 は「PATHOPTS 属性の用途をジョブデータ定義の表示で確認する記録読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景ではz/OS JCL の PATHOPTS 属性と IEF236I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明だけに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では PATHOPTS 属性を JCL DD 文で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 終端確認のジョブデータ定義に関係する PATHOPTS=ORDONLY の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端確認として残す。 ✅
    - B. PATHOPTS=ORDONLY の名称と担当者名のみを残して終端確認のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で終端確認のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端確認のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認のジョブデータ定義において選択記号 A を採用し、識別名は終端確認です。終端確認のジョブデータ定義において PATHOPTS=ORDONLY は説明欄の「PATHOPTS=ORDONLY の用途をジョブデータ定義の表示で確認する終端確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認のジョブデータ定義に関連して、z/OS JCL では PATHOPTS=ORDONLY の表示属性と IEF236I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=ORDONLY の根拠にならないため終端確認ではありません。 D: 終端確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため終端確認ではありません。終端確認のジョブデータ定義で使う PATHOPTS=ORDONLY という用語は JCL DD 文で扱う確認対象であり、用語名は終端確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=ORDONLY**

    - 検証目的: 出力追跡のジョブデータ定義について、PATHOPTS=ORDONLY は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、出力追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=ORDONLYを指定し、OSKB020048の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=ORDONLY
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=ORDONLY
    CASE OSKB020048
    SOURCE z/OS JCL
    ```

    PATHOPTS=ORDONLYとOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020048を同じ出力で読み、出力追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020048
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020048.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020048 STEP1 SYSUT1
    ```

    IEF236IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=ORDONLY と OSKB020048 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=ORDWR {#c17-i0192}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=ORDWRは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。読み書き両用でオープン。「PATHOPTS=ORDWR」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 順序読解のジョブデータ定義でジョブデータ定義の運用確認を行います。PATHOPTS=ORDWR の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序読解のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序読解のジョブデータ定義を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序読解の根拠を固定する。 ✅
    - D. PATHOPTS=ORDWR の属性行を読まず順序読解のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では PATHOPTS=ORDWR は「z/OS JCL で PATHOPTS=ORDWR の扱いを記録する順序読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では PATHOPTS=ORDWR の表示結果と IEF236I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明だけに寄り、判定名は順序読解不足です。順序読解資料では PATHOPTS=ORDWR の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 上書確認のジョブデータ定義でジョブデータ定義の運用確認を行います。PATHOPTS=ORDWR の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書確認のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書確認のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書確認の記録として扱う。 ✅
    - D. PATHOPTS=ORDWR の属性行を読まず上書確認のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認のジョブデータ定義において選択記号 C を採用し、識別名は上書確認です。上書確認のジョブデータ定義において PATHOPTS=ORDWR は説明欄の「z/OS JCL で PATHOPTS=ORDWR の扱いを記録する上書確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のジョブデータ定義を受け取る担当者は、PATHOPTS=ORDWR の表示結果と IEF236I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=ORDWR の根拠にならないため上書確認ではありません。 B: 上書確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書確認ではありません。 C: 上書確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のジョブデータ定義が示す PATHOPTS=ORDWR は出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=ORDWR**

    - 検証目的: 区切追跡のジョブデータ定義について、PATHOPTS=ORDWR は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。読み書き両用でオープン。「PATHOPTS=ORDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=ORDWRを指定し、OSKB020050の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=ORDWR
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=ORDWR
    CASE OSKB020050
    SOURCE z/OS JCL
    ```

    PATHOPTS=ORDWRとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020050を同じ出力で読み、区切追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020050
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020050.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020050 STEP1 SYSUT1
    ```

    IEF236IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=ORDWR と OSKB020050 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=OSYNC {#c17-i0193}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=OSYNCは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 展開検分のジョブデータ定義で PATHOPTS=OSYNC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHOPTS=OSYNC の出力を取らず展開検分のジョブデータ定義の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開検分として引き継ぐ。 ✅
    - C. ST OSKBDD を省略して展開検分のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開検分のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では PATHOPTS=OSYNC は「展開検分のジョブデータ定義に関係する定義値と表示行を照合する展開検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では PATHOPTS=OSYNC の属性行と IEF236I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明だけに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では PATHOPTS=OSYNC を JCL DD 文の運用手順で確認し、初出名は展開検分初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 比較確認のジョブデータ定義で PATHOPTS=OSYNC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHOPTS=OSYNC の出力を取らず比較確認のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 ✅
    - C. ST OSKBDD を省略して比較確認のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認のジョブデータ定義において選択記号 B を採用し、識別名は比較確認です。比較確認のジョブデータ定義において PATHOPTS=OSYNC は説明欄の「比較確認のジョブデータ定義に関係する定義値と表示行を照合する比較確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認のジョブデータ定義の証跡を読む担当者は、PATHOPTS=OSYNC の属性行と IEF236I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため比較確認ではありません。 D: 比較確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=OSYNC の根拠にならないため比較確認ではありません。比較確認のジョブデータ定義に出る PATHOPTS=OSYNC は JCL DD 文の運用手順で意味を確認する対象であり、用語名は比較確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=OSYNC**

    - 検証目的: 警告追跡のジョブデータ定義について、PATHOPTS=OSYNC は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、警告追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OSYNCを指定し、OSKB020057の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OSYNC
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OSYNC
    CASE OSKB020057
    SOURCE z/OS JCL
    ```

    PATHOPTS=OSYNCとOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020057を同じ出力で読み、警告追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020057
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020057.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020057 STEP1 SYSUT1
    ```

    IEF236IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OSYNC と OSKB020057 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=OTRUNC {#c17-i0194}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=OTRUNCは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 監査読解のジョブデータ定義でジョブデータ定義の運用確認を行います。PATHOPTS=OTRUNC の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査読解のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査読解のジョブデータ定義を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査読解の根拠にする。 ✅
    - D. PATHOPTS=OTRUNC の属性行を読まず監査読解のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では PATHOPTS=OTRUNC は「z/OS JCL で PATHOPTS=OTRUNC の扱いを記録する監査読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では PATHOPTS=OTRUNC の表示結果と IEF236I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明だけに寄り、判定名は監査読解不足です。監査読解資料では PATHOPTS=OTRUNC の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 範囲確認のジョブデータ定義でジョブデータ定義の運用確認を行います。PATHOPTS=OTRUNC の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲確認のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲確認のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲確認の記録として扱う。 ✅
    - D. PATHOPTS=OTRUNC の属性行を読まず範囲確認のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認のジョブデータ定義において選択記号 C を採用し、識別名は範囲確認です。範囲確認のジョブデータ定義において PATHOPTS=OTRUNC は説明欄の「z/OS JCL で PATHOPTS=OTRUNC の扱いを記録する範囲確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認のジョブデータ定義を受け取る担当者は、PATHOPTS=OTRUNC の表示結果と IEF236I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=OTRUNC の根拠にならないため範囲確認ではありません。 B: 範囲確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認のジョブデータ定義が示す PATHOPTS=OTRUNC は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=OTRUNC**

    - 検証目的: 比較追跡のジョブデータ定義について、PATHOPTS=OTRUNC は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OTRUNCを指定し、OSKB020054の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OTRUNC
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OTRUNC
    CASE OSKB020054
    SOURCE z/OS JCL
    ```

    PATHOPTS=OTRUNCとOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020054を同じ出力で読み、比較追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020054
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020054.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020054 STEP1 SYSUT1
    ```

    IEF236IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OTRUNC と OSKB020054 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=OWRONLY {#c17-i0195}
*分類: USS-PATH*  ・  難易度: 中級

書き込み専用でオープン。「PATHOPTS=OWRONLY」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 比較読解のジョブデータ定義で PATHOPTS 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHOPTS 属性の出力を取らず比較読解のジョブデータ定義の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較読解の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して比較読解のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較読解のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では PATHOPTS 属性 は「比較読解のジョブデータ定義に関係する定義値と表示行を照合する比較読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では PATHOPTS 属性の属性行と IEF236I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明だけに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では PATHOPTS 属性を JCL DD 文の運用手順で確認し、初出名は比較読解初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 探索確認のジョブデータ定義で PATHOPTS=OWRONLY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHOPTS=OWRONLY の出力を取らず探索確認のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索確認の確認結果にする。 ✅
    - C. ST OSKBDD を省略して探索確認のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認のジョブデータ定義において選択記号 B を採用し、識別名は探索確認です。探索確認のジョブデータ定義において PATHOPTS=OWRONLY は説明欄の「探索確認のジョブデータ定義に関係する定義値と表示行を照合する探索確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のジョブデータ定義の証跡を読む担当者は、PATHOPTS=OWRONLY の属性行と IEF236I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため探索確認ではありません。 D: 探索確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=OWRONLY の根拠にならないため探索確認ではありません。探索確認のジョブデータ定義に出る PATHOPTS=OWRONLY は JCL DD 文の運用手順で意味を確認する対象であり、用語名は探索確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=OWRONLY**

    - 検証目的: 条件追跡のジョブデータ定義について、書き込み専用でオープン。「PATHOPTS=OWRONLY」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすいに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、条件追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OWRONLYを指定し、OSKB020049の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OWRONLY
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OWRONLY
    CASE OSKB020049
    SOURCE z/OS JCL
    ```

    PATHOPTS=OWRONLYとOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020049を同じ出力で読み、条件追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020049
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020049.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020049 STEP1 SYSUT1
    ```

    IEF236IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OWRONLY と OSKB020049 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > VOL

### VOL 完全位置取り例 VOL=(PRIVATE,RETAIN,1,5,SER=...) {#c17-i0196}
*分類: VOL*  ・  難易度: 中級

VOL 完全位置取り例 VOL=(PRIVATE,RETAIN,1,5,SER=...)は、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。位置パラメータと SER の組み合わせ例。各位置の意味 (private, retain, vol-seq, vol-count, SER) を理解する基準ケース

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide


### VOL=,,,vol-count {#c17-i0197}
*分類: VOL*  ・  難易度: 中級

VOL=,,,vol-countは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。ボリューム数 (確保上限) を指定。マルチボリューム拡張の上限を明示。「VOL=,,,vol-count」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 探索検査のジョブデータ定義で VOL= 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VOL= 命令の出力を取らず探索検査のジョブデータ定義の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索検査の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して探索検査のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索検査のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では VOL= 命令 は「探索検査のジョブデータ定義に関係する定義値と表示行を照合する探索検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では VOL= 命令の属性行と IEF236I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明だけに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では VOL= 命令を JCL DD 文の運用手順で確認し、初出名は探索検査初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 出力追跡のジョブデータ定義に関する VOL=,,,vol-countの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力追跡のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のジョブデータ定義の証跡として保存して根拠にする。
    - C. VOL=,,,vol-countの変更点を出力本文から切り離して出力追跡のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡のジョブデータ定義において選択記号 D を採用し、識別名は出力追跡です。出力追跡のジョブデータ定義において VOL=,,,vol-count は説明欄の「VOL=,,,vol-countの状態と出力メッセージを結び付ける出力追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のジョブデータ定義に関する記録は、VOL=,,,vol-countの出力行と IEF236I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=,,,vol-countの根拠にならないため出力追跡ではありません。 C: 出力追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のジョブデータ定義で記録する VOL=,,,vol-countはz/OS JCL の確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **VOL=,,,vol-count**

    - 検証目的: 比較確認のジョブデータ定義について、VOL=,,,vol-countは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。ボリューム数 (確保上限) を指定。マルチボリューム拡張に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030014の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較確認のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=,,,vol-countを指定し、OSKB030014の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=,,,vol-count
    CASE OSKB030014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=,,,vol-count
    CASE OSKB030014
    SOURCE z/OS JCL
    ```

    VOL=,,,vol-countとOSKB030014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030014を同じ出力で読み、比較確認のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030014
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030014
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030014.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030014 STEP1 SYSUT1
    ```

    IEF236IとOSKB030014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=,,,vol-count と OSKB030014 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **VOL=,,,vol-count**

    - 検証目的: 構文検査のジョブデータ定義について、VOL=,,,vol-countは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。ボリューム数 (確保上限) を指定。マルチボリューム拡張に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、構文検査のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=,,,vol-countを指定し、OSKB010061の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=,,,vol-count
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=,,,vol-count
    CASE OSKB010061
    SOURCE z/OS JCL
    ```

    VOL=,,,vol-countとOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010061を同じ出力で読み、構文検査のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010061
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010061.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010061 STEP1 SYSUT1
    ```

    IEF236IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=,,,vol-count と OSKB010061 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=,,seq-no {#c17-i0198}
*分類: VOL*  ・  難易度: 中級

VOL=,,seq-noは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 終端検査のジョブデータ定義に関係する VOL=,,seq-noの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検査で再確認できる形にする。 ✅
    - B. VOL=,,seq-noの名称と担当者名だけを残して終端検査のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で終端検査のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端検査のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では VOL=,,seq-no は「VOL=,,seq-noの用途をジョブデータ定義の表示で確認する終端検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景ではz/OS JCL の VOL=,,seq-noと IEF236I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明だけに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では VOL=,,seq-noを JCL DD 文で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 上書追跡のジョブデータ定義でジョブデータ定義の運用確認を行います。VOL=,,seq-noの根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書追跡のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書追跡のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. VOL=,,seq-noの属性行を読まず上書追跡のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のジョブデータ定義において選択記号 C を採用し、識別名は上書追跡です。上書追跡のジョブデータ定義において VOL=,,seq-no は説明欄の「z/OS JCL で VOL=,,seq-noの扱いを記録する上書追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のジョブデータ定義を受け取る担当者は、VOL=,,seq-noの表示結果と IEF236I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=,,seq-noの根拠にならないため上書追跡ではありません。 B: 上書追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のジョブデータ定義が示す VOL=,,seq-noは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **VOL=,,seq-no**

    - 検証目的: 変更追跡のジョブデータ定義について、VOL=,,seq-noは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、変更追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=,,seq-noを指定し、OSKB010060の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=,,seq-no
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=,,seq-no
    CASE OSKB010060
    SOURCE z/OS JCL
    ```

    VOL=,,seq-noとOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010060を同じ出力で読み、変更追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010060
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010060.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010060 STEP1 SYSUT1
    ```

    IEF236IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=,,seq-no と OSKB010060 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=PRIVATE {#c17-i0199}
*分類: VOL*  ・  難易度: 中級

VOL=PRIVATEは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。ボリュームを専有モードでマウント。マウント解除まで他ジョブから使えない。「VOL=PRIVATE」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 呼出検査のジョブデータ定義でジョブデータ定義の運用確認を行います。VOL=PRIVATE の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出検査のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出検査のジョブデータ定義を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出検査の確認にする。 ✅
    - D. VOL=PRIVATE の属性行を読まず呼出検査のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では VOL=PRIVATE は「z/OS JCL で VOL=PRIVATE の扱いを記録する呼出検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では VOL=PRIVATE の表示結果と IEF236I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明だけに寄り、判定名は呼出検査不足です。呼出検査資料では VOL=PRIVATE の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 終端追跡のジョブデータ定義に関係する VOL=PRIVATE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 ✅
    - B. VOL=PRIVATE の名称と担当者名のみを残して終端追跡のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で終端追跡のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端追跡のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡のジョブデータ定義において選択記号 A を採用し、識別名は終端追跡です。終端追跡のジョブデータ定義において VOL=PRIVATE は説明欄の「VOL=PRIVATE の用途をジョブデータ定義の表示で確認する終端追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のジョブデータ定義に関連して、z/OS JCL では VOL=PRIVATE の表示属性と IEF236I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=PRIVATE の根拠にならないため終端追跡ではありません。 D: 終端追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため終端追跡ではありません。終端追跡のジョブデータ定義で使う VOL=PRIVATE という用語は JCL DD 文で扱う確認対象であり、用語名は終端追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **VOL=PRIVATE**

    - 検証目的: 復旧追跡のジョブデータ定義について、VOL=PRIVATE は、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。ボリュームを専有モードでマウント。マウント解除まで他ジョブから使えに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=PRIVATEを指定し、OSKB010058の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=PRIVATE
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=PRIVATE
    CASE OSKB010058
    SOURCE z/OS JCL
    ```

    VOL=PRIVATEとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010058を同じ出力で読み、復旧追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010058
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010058.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010058 STEP1 SYSUT1
    ```

    IEF236IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=PRIVATE と OSKB010058 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=REF=*.stepname.ddname {#c17-i0200}
*分類: VOL*  ・  難易度: 中級

VOL=REF=*.stepname.ddnameは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 展開検査の*で VOL=REF=* 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VOL=REF=* 属性の出力を取らず展開検査の*の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開検査として引き継ぐ。 ✅
    - C. ST OSKBDD を省略して展開検査の*の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開検査の*へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では VOL=REF=* 属性 は「展開検査の*に関係する定義値と表示行を照合する展開検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では VOL=REF=* 属性の属性行と IEF236I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明だけに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では VOL=REF=* 属性を JCL DD 文の運用手順で確認し、初出名は展開検査初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 置換追跡の*に関する VOL=REF=*.stepname.ddnamの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換追跡の*の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の*の証跡として保存して根拠にする。
    - C. VOL=REF=*.stepname.ddnamの変更点を出力本文から切り離して置換追跡の*の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡の*において選択記号 D を採用し、識別名は置換追跡です。置換追跡の*において VOL=REF=*.stepname.ddnam は説明欄の「VOL=REF=*.stepname.ddnamの状態と出力メッセージを結び付ける置換追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の*に関する記録は、VOL=REF=*.stepname.ddnamの出力行と IEF236I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の*は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の*は別カテゴリの確認を流用しており、VOL=REF=*.stepname.ddnamの根拠にならないため置換追跡ではありません。 C: 置換追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の*は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の*で記録する VOL=REF=*.stepname.ddnamはz/OS JCL の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **VOL=REF=*.stepname.ddname**

    - 検証目的: 警告追跡の*について、VOL=REF=*.stepname.ddnameは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、警告追跡の*の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=REF=*.stepnameを指定し、OSKB010057の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=REF=*.stepname
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=REF=*.stepname
    CASE OSKB010057
    SOURCE z/OS JCL
    ```

    VOL=REF=*.stepnameとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010057を同じ出力で読み、警告追跡の*の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010057
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010057.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010057 STEP1 SYSUT1
    ```

    IEF236IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=REF=*.stepname と OSKB010057 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=REF=dsname {#c17-i0201}
*分類: VOL*  ・  難易度: 中級

VOL=REF=dsnameは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。別データセットと同じボリュームに割り当て。可搬性のあるボリューム共有手段。「VOL=REF=dsname」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 構文検査のジョブデータ定義に関係する VOL=REF=dsnameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD で得た表示本文を使い、構文検査の採否を説明欄に結び付ける。 ✅
    - B. VOL=REF=dsnameの名称と担当者名だけを残して構文検査のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で構文検査のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文検査のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では VOL=REF=dsname は「VOL=REF=dsnameの用途をジョブデータ定義の表示で確認する構文検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景ではz/OS JCL の VOL=REF=dsnameと IEF236I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明だけに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では VOL=REF=dsnameを JCL DD 文で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 呼出追跡のジョブデータ定義でジョブデータ定義の運用確認を行います。VOL=REF=dsnameの根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出追跡のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出追跡のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 ✅
    - D. VOL=REF=dsnameの属性行を読まず呼出追跡のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡のジョブデータ定義において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のジョブデータ定義において VOL=REF=dsname は説明欄の「z/OS JCL で VOL=REF=dsnameの扱いを記録する呼出追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のジョブデータ定義を受け取る担当者は、VOL=REF=dsnameの表示結果と IEF236I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=REF=dsnameの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のジョブデータ定義が示す VOL=REF=dsnameは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **VOL=REF=dsname**

    - 検証目的: 記録確認のジョブデータ定義について、VOL=REF=dsnameは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。別データセットと同じボリュームに割り当て。可搬性のあるボリュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030013の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録確認のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=REF=dsnameを指定し、OSKB030013の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=REF=dsname
    CASE OSKB030013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=REF=dsname
    CASE OSKB030013
    SOURCE z/OS JCL
    ```

    VOL=REF=dsnameとOSKB030013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030013を同じ出力で読み、記録確認のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030013
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030013
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030013.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030013 STEP1 SYSUT1
    ```

    IEF236IとOSKB030013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=REF=dsname と OSKB030013 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **VOL=REF=dsname**

    - 検証目的: 値域追跡のジョブデータ定義について、VOL=REF=dsnameは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。別データセットと同じボリュームに割り当て。可搬性のあるボリュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=REF=dsnameを指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=REF=dsname
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=REF=dsname
    CASE OSKB010056
    SOURCE z/OS JCL
    ```

    VOL=REF=dsnameとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010056を同じ出力で読み、値域追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010056
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010056.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010056 STEP1 SYSUT1
    ```

    IEF236IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=REF=dsname と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=RETAIN {#c17-i0202}
*分類: VOL*  ・  難易度: 中級

VOL=RETAINは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。ステップ終了後もボリュームをマウントしたまま保持。後続ステップで再使用する場合。「VOL=RETAIN」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 置換検査のジョブデータ定義に関する VOL=RETAIN の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換検査のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換検査のジョブデータ定義の証跡として保存して根拠にする。
    - C. VOL=RETAIN の変更点を出力本文から切り離して置換検査のジョブデータ定義の承認欄だけ残す。
    - D. z/OS JCL の表示形式に沿って根拠行を採り、置換検査の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では VOL=RETAIN は「VOL=RETAIN の状態と出力メッセージを結び付ける置換検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では VOL=RETAIN の出力行と IEF236I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明だけに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では VOL=RETAIN をz/OS JCL の確認記録に残し、対象名は置換検査対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 探索追跡のジョブデータ定義で VOL=RETAIN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VOL=RETAIN の出力を取らず探索追跡のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 ✅
    - C. ST OSKBDD を省略して探索追跡のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡のジョブデータ定義において選択記号 B を採用し、識別名は探索追跡です。探索追跡のジョブデータ定義において VOL=RETAIN は説明欄の「探索追跡のジョブデータ定義に関係する定義値と表示行を照合する探索追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のジョブデータ定義の証跡を読む担当者は、VOL=RETAIN の属性行と IEF236I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=RETAIN の根拠にならないため探索追跡ではありません。探索追跡のジョブデータ定義に出る VOL=RETAIN は JCL DD 文の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **VOL=RETAIN**

    - 検証目的: 監査追跡のジョブデータ定義について、VOL=RETAIN は、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。ステップ終了後もボリュームをマウントしたまま保持。後続ステップで再使に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、監査追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=RETAINを指定し、OSKB010059の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=RETAIN
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=RETAIN
    CASE OSKB010059
    SOURCE z/OS JCL
    ```

    VOL=RETAINとOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010059を同じ出力で読み、監査追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010059
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010059.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010059 STEP1 SYSUT1
    ```

    IEF236IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=RETAIN と OSKB010059 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=SER=(v1,v2,v3) {#c17-i0203}
*分類: VOL*  ・  難易度: 中級

VOL=SER=(v1,v2,v3)は、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。複数 volser のリスト。マルチボリュームデータセットの順序を指定。「VOL=SER=(v1,v2,v3)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 変更追跡のジョブデータ定義に関する VOL=SER=(v1 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず変更追跡のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更追跡のジョブデータ定義の証跡として保存して根拠にする。
    - C. VOL=SER=(v1 命令の変更点を出力本文から切り離して変更追跡のジョブデータ定義の承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、変更追跡の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では VOL=SER=(v1 命令 は「VOL=SER=(v1 命令の状態と出力メッセージを結び付ける変更追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では VOL=SER=(v1 命令の出力行と IEF236I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明だけに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では VOL=SER=(v1 命令をz/OS JCL の確認記録に残し、対象名は変更追跡対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 展開追跡のジョブデータ定義で VOL=SER=(v1,v2,v3)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. VOL=SER=(v1,v2,v3)の出力を取らず展開追跡のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 ✅
    - C. ST OSKBDD を省略して展開追跡のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡のジョブデータ定義において選択記号 B を採用し、識別名は展開追跡です。展開追跡のジョブデータ定義において VOL=SER=(v1,v2,v3) は説明欄の「展開追跡のジョブデータ定義に関係する定義値と表示行を照合する展開追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のジョブデータ定義の証跡を読む担当者は、VOL=SER=(v1,v2,v3)の属性行と IEF236I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=SER=(v1,v2,v3)の根拠にならないため展開追跡ではありません。展開追跡のジョブデータ定義に出る VOL=SER=(v1,v2,v3)は JCL DD 文の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **VOL=SER=(v1,v2,v3)**

    - 検証目的: 順序追跡のジョブデータ定義について、VOL=SER=(v1,v2,v3)は、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。複数 volser のリスト。マルチボリュームデータに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=SER=(v1,v2,v3)を指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=SER=(v1,v2,v3)
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=SER=(v1,v2,v3)
    CASE OSKB010055
    SOURCE z/OS JCL
    ```

    VOL=SER=(v1,v2,v3)とOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010055を同じ出力で読み、順序追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010055
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010055.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010055 STEP1 SYSUT1
    ```

    IEF236IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=SER=(v1,v2,v3) と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### VOL=SER=volser {#c17-i0204}
*分類: VOL*  ・  難易度: 中級

VOL=SER=volserは、JCL DD 文のVOLで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 監査追跡のジョブデータ定義でジョブデータ定義の運用確認を行います。VOL=SER=volserの根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査追跡のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査追跡のジョブデータ定義を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査追跡の根拠にする。 ✅
    - D. VOL=SER=volserの属性行を読まず監査追跡のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では VOL=SER=volser は「z/OS JCL で VOL=SER=volserの扱いを記録する監査追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では VOL=SER=volserの表示結果と IEF236I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明だけに寄り、判定名は監査追跡不足です。監査追跡資料では VOL=SER=volserの使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 構文追跡のジョブデータ定義に関係する VOL=SER=volserの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 ✅
    - B. VOL=SER=volserの名称と担当者名のみを残して構文追跡のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で構文追跡のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文追跡のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡のジョブデータ定義において選択記号 A を採用し、識別名は構文追跡です。構文追跡のジョブデータ定義において VOL=SER=volser は説明欄の「VOL=SER=volserの用途をジョブデータ定義の表示で確認する構文追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のジョブデータ定義に関連して、z/OS JCL では VOL=SER=volserの表示属性と IEF236I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のジョブデータ定義は別カテゴリの確認を流用しており、VOL=SER=volserの根拠にならないため構文追跡ではありません。 D: 構文追跡のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため構文追跡ではありません。構文追跡のジョブデータ定義で使う VOL=SER=volserという用語は JCL DD 文で扱う確認対象であり、用語名は構文追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **VOL=SER=volser**

    - 検証目的: 比較追跡のジョブデータ定義について、VOL=SER=volserは、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較追跡のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL=SER=volserを指定し、OSKB010054の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL=SER=volser
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL=SER=volser
    CASE OSKB010054
    SOURCE z/OS JCL
    ```

    VOL=SER=volserとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010054を同じ出力で読み、比較追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010054
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010054.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010054 STEP1 SYSUT1
    ```

    IEF236IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL=SER=volser と OSKB010054 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > その他

### ACCODE=テープアクセスコード {#c17-i0205}
*分類: その他*  ・  難易度: 中級

ACCODE=テープアクセスコードは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 警告検査のテープアクセスコードに関係する ACCODE= テープアクセスコードの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告検査として残す。 ✅
    - B. ACCODE= テープアクセスコードの名称と担当者名のみを残して警告検査のテープアクセスコードの表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で警告検査のテープアクセスコードを確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告検査のテープアクセスコードの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査のテープアクセスコードにおいて選択記号 A を採用し、識別名は警告検査です。警告検査のテープアクセスコードにおいて ACCODE= テープアクセスコード は説明欄の「ACCODE= テープアクセスコードの用途をジョブデータ定義の表示で確認する警告検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査のテープアクセスコードに関連して、z/OS JCL では ACCODE= テープアクセスコードの表示属性と IEF236I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査のテープアクセスコードは対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査のテープアクセスコードは名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査のテープアクセスコードは別カテゴリの確認を流用しており、ACCODE= テープアクセスコードの根拠にならないため警告検査ではありません。 D: 警告検査のテープアクセスコードは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため警告検査ではありません。警告検査のテープアクセスコードで使う ACCODE= テープアクセスコードという用語は JCL DD 文で扱う確認対象であり、用語名は警告検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **ACCODE= テープアクセスコード**

    - 検証目的: 変更整理のテープアクセスコードについて、ACCODE= テープアクセスコードは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、変更整理のテープアクセスコードの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にACCODE= テープアクセスコードを指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ACCODE= テープアクセスコード
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ACCODE= テープアクセスコード
    CASE OSKB020120
    SOURCE z/OS JCL
    ```

    ACCODE= テープアクセスコードとOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020120を同じ出力で読み、変更整理のテープアクセスコードの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020120
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020120.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020120 STEP1 SYSUT1
    ```

    IEF236IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の ACCODE= テープアクセスコード と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### BUFOFF (DCB 系再掲) {#c17-i0206}
*分類: その他*  ・  難易度: 中級

BUFOFF (DCB 系再掲)は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。RECFM=D のテープ I/O で各ブロックの先頭オフセット指定。L=長さ 4 バイト込み。「BUFOFF (DCB 系再掲)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 終端判定の系再掲に関係する BUFOFF (DCB 系再掲)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端判定として残す。 ✅
    - B. BUFOFF (DCB 系再掲)の名称と担当者名のみを残して終端判定の系再掲の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で終端判定の系再掲を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端判定の系再掲の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定の系再掲において選択記号 A を採用し、識別名は終端判定です。終端判定の系再掲において BUFOFF (DCB 系再掲) は説明欄の「BUFOFF (DCB 系再掲)の用途をジョブデータ定義の表示で確認する終端判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は終端判定です。終端判定の系再掲に関連して、z/OS JCL では BUFOFF (DCB 系再掲)の表示属性と IEF236I を同じ証跡に残し、背景名は終端判定です。他の選択肢を確認します。 A: 終端判定の系再掲は対象出力と項目説明を結び、根拠を残すので終端判定です。 B: 終端判定の系再掲は名称や説明のみに寄り、状態を示す出力本文が不足するため終端判定ではありません。 C: 終端判定の系再掲は別カテゴリの確認を流用しており、BUFOFF (DCB 系再掲)の根拠にならないため終端判定ではありません。 D: 終端判定の系再掲は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため終端判定ではありません。終端判定の系再掲で使う BUFOFF (DCB 系再掲)という用語は JCL DD 文で扱う確認対象であり、用語名は終端判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **BUFOFF (DCB 系再掲)**

    - 検証目的: 出力記録の系再掲について、BUFOFF (DCB 系再掲)は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。RECFM=D のテープ I/O で各ブロックの先頭オフに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020128の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、出力記録の系再掲の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBUFOFF (DCB 系再掲)を指定し、OSKB020128の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BUFOFF (DCB 系再掲)
    CASE OSKB020128
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BUFOFF (DCB 系再掲)
    CASE OSKB020128
    SOURCE z/OS JCL
    ```

    BUFOFF (DCB 系再掲)とOSKB020128が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020128を同じ出力で読み、出力記録の系再掲の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020128
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020128
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020128.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020128 STEP1 SYSUT1
    ```

    IEF236IとOSKB020128が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の BUFOFF (DCB 系再掲) と OSKB020128 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020128 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### CCSID=コード化文字セット ID {#c17-i0207}
*分類: その他*  ・  難易度: 中級

CCSID=コード化文字セット IDは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。USS PATH や VSAM AMP と組み合わせて、テキスト変換の CCSID を指定。「CCSID=コード化文字セット ID」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 値域検査のコード化文字セットに関する CCSID= コード化文字セット ID の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域検査のコード化文字セットの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査のコード化文字セットの証跡として保存して根拠にする。
    - C. CCSID= コード化文字セット ID の変更点を出力本文から切り離して値域検査のコード化文字セットの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査のコード化文字セットにおいて選択記号 D を採用し、識別名は値域検査です。値域検査のコード化文字セットにおいて CCSID= コード化文字セット ID は説明欄の「CCSID= コード化文字セット ID の状態と出力メッセージを結び付ける値域検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査のコード化文字セットに関する記録は、CCSID= コード化文字セット ID の出力行と IEF236I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査のコード化文字セットは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため値域検査ではありません。 B: 値域検査のコード化文字セットは別カテゴリの確認を流用しており、CCSID= コード化文字セット ID の根拠にならないため値域検査ではありません。 C: 値域検査のコード化文字セットは名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査のコード化文字セットは対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査のコード化文字セットで記録する CCSID= コード化文字セット ID はz/OS JCL の確認記録に残す対象名であり、用語名は値域検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **CCSID= コード化文字セット ID**

    - 検証目的: 監査整理のコード化文字セットについて、CCSID= コード化文字セット ID は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。USS PATH や VSAM AMP と組み合わせに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、監査整理のコード化文字セットの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCCSID= コード化文字セット Iを指定し、OSKB020119の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CCSID= コード化文字セット I
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CCSID= コード化文字セット I
    CASE OSKB020119
    SOURCE z/OS JCL
    ```

    CCSID= コード化文字セット IとOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020119を同じ出力で読み、監査整理のコード化文字セットの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020119
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020119.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020119 STEP1 SYSUT1
    ```

    IEF236IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の CCSID= コード化文字セット I と OSKB020119 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### CHKPT=EOV {#c17-i0208}
*分類: その他*  ・  難易度: 中級

CHKPT=EOVは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。End-of-Volume 時にチェックポイント取得。長時間ジョブのリカバリ向け。「CHKPT=EOV」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 復旧検査のその他で CHKPT=EOV の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CHKPT=EOV の出力を取らず復旧検査のその他の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧検査の確認結果にする。 ✅
    - C. ST OSKBDD を省略して復旧検査のその他の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のその他へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査のその他において選択記号 B を採用し、識別名は復旧検査です。復旧検査のその他において CHKPT=EOV は説明欄の「復旧検査のその他に関係する定義値と表示行を照合する復旧検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は復旧検査です。復旧検査のその他の証跡を読む担当者は、CHKPT=EOV の属性行と IEF236I を合わせて追跡し、背景名は復旧検査です。誤答側の問題点を分けます。 A: 復旧検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧検査ではありません。 B: 復旧検査のその他は対象出力と項目説明を結び、根拠を残すので復旧検査です。 C: 復旧検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため復旧検査ではありません。 D: 復旧検査のその他は別カテゴリの確認を流用しており、CHKPT=EOV の根拠にならないため復旧検査ではありません。復旧検査のその他に出る CHKPT=EOV は JCL DD 文の運用手順で意味を確認する対象であり、用語名は復旧検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **CHKPT=EOV**

    - 検証目的: 区切追跡のその他について、CHKPT=EOV は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。End-of-Volume 時にチェックポイント取得。長時間ジョブのリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030050の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切追跡のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCHKPT=EOVを指定し、OSKB030050の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CHKPT=EOV
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CHKPT=EOV
    CASE OSKB030050
    SOURCE z/OS JCL
    ```

    CHKPT=EOVとOSKB030050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030050を同じ出力で読み、区切追跡のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030050
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030050.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030050 STEP1 SYSUT1
    ```

    IEF236IとOSKB030050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の CHKPT=EOV と OSKB030050 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CHKPT=EOV**

    - 検証目的: 構文記録のその他について、CHKPT=EOV は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。End-of-Volume 時にチェックポイント取得。長時間ジョブのリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020121の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、構文記録のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCHKPT=EOVを指定し、OSKB020121の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CHKPT=EOV
    CASE OSKB020121
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CHKPT=EOV
    CASE OSKB020121
    SOURCE z/OS JCL
    ```

    CHKPT=EOVとOSKB020121が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020121を同じ出力で読み、構文記録のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020121
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020121
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020121.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020121 STEP1 SYSUT1
    ```

    IEF236IとOSKB020121が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の CHKPT=EOV と OSKB020121 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### COMPACTION=テープ圧縮 {#c17-i0209}
*分類: その他*  ・  難易度: 中級

COMPACTION=テープ圧縮は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。テープ装置の圧縮機能を有効化。IDRC など。装置依存。「COMPACTION=テープ圧縮」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 置換判定のテープ圧縮に関する COMPACTION= テープ圧縮の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換判定のテープ圧縮の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のテープ圧縮の証跡として保存して根拠にする。
    - C. COMPACTION= テープ圧縮の変更点を出力本文から切り離して置換判定のテープ圧縮の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定のテープ圧縮において選択記号 D を採用し、識別名は置換判定です。置換判定のテープ圧縮において COMPACTION= テープ圧縮 は説明欄の「COMPACTION= テープ圧縮の状態と出力メッセージを結び付ける置換判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は置換判定です。置換判定のテープ圧縮に関する記録は、COMPACTION= テープ圧縮の出力行と IEF236I を一緒に保存し、背景名は置換判定です。選択肢ごとの違いを示します。 A: 置換判定のテープ圧縮は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため置換判定ではありません。 B: 置換判定のテープ圧縮は別カテゴリの確認を流用しており、COMPACTION= テープ圧縮の根拠にならないため置換判定ではありません。 C: 置換判定のテープ圧縮は名称や説明のみに寄り、状態を示す出力本文が不足するため置換判定ではありません。 D: 置換判定のテープ圧縮は対象出力と項目説明を結び、根拠を残すので置換判定です。置換判定のテープ圧縮で記録する COMPACTION= テープ圧縮はz/OS JCL の確認記録に残す対象名であり、用語名は置換判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **COMPACTION= テープ圧縮**

    - 検証目的: 上書記録のテープ圧縮について、COMPACTION= テープ圧縮は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。テープ装置の圧縮機能を有効化。IDRC など。装置依存。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020127の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、上書記録のテープ圧縮の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCOMPACTION= テープ圧縮を指定し、OSKB020127の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND COMPACTION= テープ圧縮
    CASE OSKB020127
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM COMPACTION= テープ圧縮
    CASE OSKB020127
    SOURCE z/OS JCL
    ```

    COMPACTION= テープ圧縮とOSKB020127が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020127を同じ出力で読み、上書記録のテープ圧縮の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020127
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020127
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020127.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020127 STEP1 SYSUT1
    ```

    IEF236IとOSKB020127が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の COMPACTION= テープ圧縮 と OSKB020127 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020127 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DDNAME=参照 {#c17-i0210}
*分類: その他*  ・  難易度: 中級

DDNAME=参照は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。DDNAME= で実 DD 名の解決を遅延 (他の DD カードのコピー的に振る舞う)。EXEC で渡される実 DD 名を後で結ぶ。「DDNAME=参照」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 順序検査の参照でジョブデータ定義の運用確認を行います。DDNAME= 参照の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序検査の参照を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序検査の参照を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序検査の記録として扱う。 ✅
    - D. DDNAME= 参照の属性行を読まず順序検査の参照の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査の参照において選択記号 C を採用し、識別名は順序検査です。順序検査の参照において DDNAME= 参照 は説明欄の「z/OS JCL で DDNAME= 参照の扱いを記録する順序検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は順序検査です。順序検査の参照を受け取る担当者は、DDNAME= 参照の表示結果と IEF236I を同じ確認単位として扱い、背景名は順序検査です。不適切な選択肢を整理します。 A: 順序検査の参照は別カテゴリの確認を流用しており、DDNAME= 参照の根拠にならないため順序検査ではありません。 B: 順序検査の参照は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため順序検査ではありません。 C: 順序検査の参照は対象出力と項目説明を結び、根拠を残すので順序検査です。 D: 順序検査の参照は名称や説明のみに寄り、状態を示す出力本文が不足するため順序検査ではありません。順序検査の参照が示す DDNAME= 参照は出典欄の資料で使い方を追跡できる項目であり、用語名は順序検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DDNAME= 参照**

    - 検証目的: 復旧整理の参照について、DDNAME= 参照は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。DDNAME= で実 DD 名の解決を遅延 (他の DD カードのコピに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧整理の参照の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDDNAME= 参照を指定し、OSKB020118の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DDNAME= 参照
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DDNAME= 参照
    CASE OSKB020118
    SOURCE z/OS JCL
    ```

    DDNAME= 参照とOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020118を同じ出力で読み、復旧整理の参照の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020118
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020118.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020118 STEP1 SYSUT1
    ```

    IEF236IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DDNAME= 参照 と OSKB020118 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSNTYPE=BASIC {#c17-i0211}
*分類: その他*  ・  難易度: 中級

DSNTYPE=BASICは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。従来 (拡張なし) 順次データセットとして割振り。「DSNTYPE=BASIC」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 区切検査のその他で DSNTYPE=BASIC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DSNTYPE=BASIC の出力を取らず区切検査のその他の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切検査の確認結果にする。 ✅
    - C. ST OSKBDD を省略して区切検査のその他の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査のその他へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査のその他において選択記号 B を採用し、識別名は区切検査です。区切検査のその他において DSNTYPE=BASIC は説明欄の「区切検査のその他に関係する定義値と表示行を照合する区切検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は区切検査です。区切検査のその他の証跡を読む担当者は、DSNTYPE=BASIC の属性行と IEF236I を合わせて追跡し、背景名は区切検査です。誤答側の問題点を分けます。 A: 区切検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため区切検査ではありません。 B: 区切検査のその他は対象出力と項目説明を結び、根拠を残すので区切検査です。 C: 区切検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため区切検査ではありません。 D: 区切検査のその他は別カテゴリの確認を流用しており、DSNTYPE=BASIC の根拠にならないため区切検査ではありません。区切検査のその他に出る DSNTYPE=BASIC は JCL DD 文の運用手順で意味を確認する対象であり、用語名は区切検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DSNTYPE=BASIC**

    - 検証目的: 記録整理のその他について、DSNTYPE=BASIC は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。従来 (拡張なし) 順次データセットとして割振り。「DSNTYに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=BASICを指定し、OSKB020113の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=BASIC
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=BASIC
    CASE OSKB020113
    SOURCE z/OS JCL
    ```

    DSNTYPE=BASICとOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020113を同じ出力で読み、記録整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020113
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020113.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020113 STEP1 SYSUT1
    ```

    IEF236IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=BASIC と OSKB020113 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSNTYPE=EXTREQ / EXTPREF {#c17-i0212}
*分類: その他*  ・  難易度: 中級

DSNTYPE=EXTREQ / EXTPREFは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。拡張形式 (EF) 順次の要求/優先指定。大型データセット用。「DSNTYPE=EXTREQ / EXTPREF」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として DSNTYPE を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 展開照合の表示本文とメッセージを照合して記録する。 ✅
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 承認欄の記入を優先して出力メッセージを保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正解はAです。展開照合権限で扱う DSNTYPE は JCL DD 文 の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として DSNTYPE を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DSNTYPE=EXTREQ ・ EXTPREF**

    - 検証目的: 優先整理の・について、DSNTYPE=EXTREQ / EXTPREF は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。拡張形式 (EF) 順次の要求/優先指定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=EXTREQ ・ Eを指定し、OSKB020112の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=EXTREQ ・ E
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=EXTREQ ・ E
    CASE OSKB020112
    SOURCE z/OS JCL
    ```

    DSNTYPE=EXTREQ ・ EとOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020112を同じ出力で読み、優先整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020112
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020112.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020112 STEP1 SYSUT1
    ```

    IEF236IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=EXTREQ ・ E と OSKB020112 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSNTYPE=HFS {#c17-i0213}
*分類: その他*  ・  難易度: 中級

DSNTYPE=HFSは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。HFS 階層ファイル (旧 USS ファイルシステム) として割振り。「DSNTYPE=HFS」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 上書検査のその他でジョブデータ定義の運用確認を行います。DSNTYPE=HFS の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書検査のその他を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書検査のその他を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書検査の記録として扱う。 ✅
    - D. DSNTYPE=HFS の属性行を読まず上書検査のその他の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査のその他において選択記号 C を採用し、識別名は上書検査です。上書検査のその他において DSNTYPE=HFS は説明欄の「z/OS JCL で DSNTYPE=HFS の扱いを記録する上書検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書検査です。上書検査のその他を受け取る担当者は、DSNTYPE=HFS の表示結果と IEF236I を同じ確認単位として扱い、背景名は上書検査です。不適切な選択肢を整理します。 A: 上書検査のその他は別カテゴリの確認を流用しており、DSNTYPE=HFS の根拠にならないため上書検査ではありません。 B: 上書検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書検査ではありません。 C: 上書検査のその他は対象出力と項目説明を結び、根拠を残すので上書検査です。 D: 上書検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため上書検査ではありません。上書検査のその他が示す DSNTYPE=HFS は出典欄の資料で使い方を追跡できる項目であり、用語名は上書検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DSNTYPE=HFS**

    - 検証目的: 区切整理のその他について、DSNTYPE=HFS は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。HFS 階層ファイル (旧 USS ファイルシステム) として割振に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=HFSを指定し、OSKB020110の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=HFS
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=HFS
    CASE OSKB020110
    SOURCE z/OS JCL
    ```

    DSNTYPE=HFSとOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020110を同じ出力で読み、区切整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020110
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020110.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020110 STEP1 SYSUT1
    ```

    IEF236IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=HFS と OSKB020110 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSNTYPE=LIBRARY (PDSE) {#c17-i0214}
*分類: その他*  ・  難易度: 中級

DSNTYPE=LIBRARY (PDSE)は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 終端検査のその他に関係する DSNTYPE=LIBRARY (PDSE)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端検査として残す。 ✅
    - B. DSNTYPE=LIBRARY (PDSE)の名称と担当者名のみを残して終端検査のその他の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で終端検査のその他を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端検査のその他の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査のその他において選択記号 A を採用し、識別名は終端検査です。終端検査のその他において DSNTYPE=LIBRARY (PDSE) は説明欄の「DSNTYPE=LIBRARY (PDSE)の用途をジョブデータ定義の表示で確認する終端検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は終端検査です。終端検査のその他に関連して、z/OS JCL では DSNTYPE=LIBRARY (PDSE)の表示属性と IEF236I を同じ証跡に残し、背景名は終端検査です。他の選択肢を確認します。 A: 終端検査のその他は対象出力と項目説明を結び、根拠を残すので終端検査です。 B: 終端検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため終端検査ではありません。 C: 終端検査のその他は別カテゴリの確認を流用しており、DSNTYPE=LIBRARY (PDSE)の根拠にならないため終端検査ではありません。 D: 終端検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため終端検査ではありません。終端検査のその他で使う DSNTYPE=LIBRARY (PDSE)という用語は JCL DD 文で扱う確認対象であり、用語名は終端検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DSNTYPE=LIBRARY (PDSE)**

    - 検証目的: 出力整理のその他について、DSNTYPE=LIBRARY (PDSE)は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020108の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、出力整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=LIBRARY (Pを指定し、OSKB020108の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=LIBRARY (P
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=LIBRARY (P
    CASE OSKB020108
    SOURCE z/OS JCL
    ```

    DSNTYPE=LIBRARY (PとOSKB020108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020108を同じ出力で読み、出力整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020108
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020108.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020108 STEP1 SYSUT1
    ```

    IEF236IとOSKB020108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=LIBRARY (P と OSKB020108 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSNTYPE=PDS {#c17-i0215}
*分類: その他*  ・  難易度: 中級

DSNTYPE=PDSは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。従来の PDS として割振り。ロードモジュール互換目的等で明示。「DSNTYPE=PDS」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 探索検査のその他で DSNTYPE=PDS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DSNTYPE=PDS の出力を取らず探索検査のその他の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索検査の確認結果にする。 ✅
    - C. ST OSKBDD を省略して探索検査のその他の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査のその他へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査のその他において選択記号 B を採用し、識別名は探索検査です。探索検査のその他において DSNTYPE=PDS は説明欄の「探索検査のその他に関係する定義値と表示行を照合する探索検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は探索検査です。探索検査のその他の証跡を読む担当者は、DSNTYPE=PDS の属性行と IEF236I を合わせて追跡し、背景名は探索検査です。誤答側の問題点を分けます。 A: 探索検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため探索検査ではありません。 B: 探索検査のその他は対象出力と項目説明を結び、根拠を残すので探索検査です。 C: 探索検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため探索検査ではありません。 D: 探索検査のその他は別カテゴリの確認を流用しており、DSNTYPE=PDS の根拠にならないため探索検査ではありません。探索検査のその他に出る DSNTYPE=PDS は JCL DD 文の運用手順で意味を確認する対象であり、用語名は探索検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DSNTYPE=PDS**

    - 検証目的: 条件整理のその他について、DSNTYPE=PDS は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。従来の PDS として割振り。ロードモジュール互換目的等で明示。「に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020109の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、条件整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=PDSを指定し、OSKB020109の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=PDS
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=PDS
    CASE OSKB020109
    SOURCE z/OS JCL
    ```

    DSNTYPE=PDSとOSKB020109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020109を同じ出力で読み、条件整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020109
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020109.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020109 STEP1 SYSUT1
    ```

    IEF236IとOSKB020109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=PDS と OSKB020109 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSNTYPE=PIPE {#c17-i0216}
*分類: その他*  ・  難易度: 中級

DSNTYPE=PIPEは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 出力検査のその他に関する DSNTYPE=PIPE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力検査のその他の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のその他の証跡として保存して根拠にする。
    - C. DSNTYPE=PIPE の変更点を出力本文から切り離して出力検査のその他の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査のその他において選択記号 D を採用し、識別名は出力検査です。出力検査のその他において DSNTYPE=PIPE は説明欄の「DSNTYPE=PIPE の状態と出力メッセージを結び付ける出力検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査のその他に関する記録は、DSNTYPE=PIPE の出力行と IEF236I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力検査ではありません。 B: 出力検査のその他は別カテゴリの確認を流用しており、DSNTYPE=PIPE の根拠にならないため出力検査ではありません。 C: 出力検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査のその他は対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査のその他で記録する DSNTYPE=PIPE はz/OS JCL の確認記録に残す対象名であり、用語名は出力検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **DSNTYPE=PIPE**

    - 検証目的: 出力追跡のその他について、DSNTYPE=PIPE は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030048の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、出力追跡のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=PIPEを指定し、OSKB030048の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=PIPE
    CASE OSKB030048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=PIPE
    CASE OSKB030048
    SOURCE z/OS JCL
    ```

    DSNTYPE=PIPEとOSKB030048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030048を同じ出力で読み、出力追跡のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030048
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030048
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030048.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030048 STEP1 SYSUT1
    ```

    IEF236IとOSKB030048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=PIPE と OSKB030048 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **DSNTYPE=PIPE**

    - 検証目的: 範囲整理のその他について、DSNTYPE=PIPE は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020111の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSNTYPE=PIPEを指定し、OSKB020111の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSNTYPE=PIPE
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSNTYPE=PIPE
    CASE OSKB020111
    SOURCE z/OS JCL
    ```

    DSNTYPE=PIPEとOSKB020111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020111を同じ出力で読み、範囲整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020111
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020111.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020111 STEP1 SYSUT1
    ```

    IEF236IとOSKB020111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSNTYPE=PIPE と OSKB020111 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FREE=CLOSE / END {#c17-i0217}
*分類: その他*  ・  難易度: 中級

DD の解放タイミング指定。SPOOL データセットや専有装置の早期解放に使う。「FREE=CLOSE / END」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **FREE=CLOSE ・ END**

    - 検証目的: 上書整理の・について、DD の解放タイミング指定。SPOOL データセットや専有装置の早期解放に使う。「FREE=CLOSE / END」は割り当て結果を調べるとき、DISP、UNIT、SPACに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、上書整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にFREE=CLOSE ・ ENDを指定し、OSKB020107の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FREE=CLOSE ・ END
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FREE=CLOSE ・ END
    CASE OSKB020107
    SOURCE z/OS JCL
    ```

    FREE=CLOSE ・ ENDとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020107を同じ出力で読み、上書整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020107
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020107.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020107 STEP1 SYSUT1
    ```

    IEF236IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FREE=CLOSE ・ END と OSKB020107 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FREEVOL=EOV {#c17-i0218}
*分類: その他*  ・  難易度: 中級

FREEVOL=EOVは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。End-of-Volume 時にボリュームを解放 (RETAIN 解除)。「FREEVOL=EOV」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 監査検査のその他でジョブデータ定義の運用確認を行います。FREEVOL=EOV の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査検査のその他を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査検査のその他を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査検査の記録として扱う。 ✅
    - D. FREEVOL=EOV の属性行を読まず監査検査のその他の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査のその他において選択記号 C を採用し、識別名は監査検査です。監査検査のその他において FREEVOL=EOV は説明欄の「z/OS JCL で FREEVOL=EOV の扱いを記録する監査検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は監査検査です。監査検査のその他を受け取る担当者は、FREEVOL=EOV の表示結果と IEF236I を同じ確認単位として扱い、背景名は監査検査です。不適切な選択肢を整理します。 A: 監査検査のその他は別カテゴリの確認を流用しており、FREEVOL=EOV の根拠にならないため監査検査ではありません。 B: 監査検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため監査検査ではありません。 C: 監査検査のその他は対象出力と項目説明を結び、根拠を残すので監査検査です。 D: 監査検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため監査検査ではありません。監査検査のその他が示す FREEVOL=EOV は出典欄の資料で使い方を追跡できる項目であり、用語名は監査検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FREEVOL=EOV**

    - 検証目的: 展開記録のその他について、FREEVOL=EOV は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。End-of-Volume 時にボリュームを解放 (RETAINに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020122の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開記録のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にFREEVOL=EOVを指定し、OSKB020122の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FREEVOL=EOV
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FREEVOL=EOV
    CASE OSKB020122
    SOURCE z/OS JCL
    ```

    FREEVOL=EOVとOSKB020122が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020122を同じ出力で読み、展開記録のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020122
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020122.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020122 STEP1 SYSUT1
    ```

    IEF236IとOSKB020122が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FREEVOL=EOV と OSKB020122 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### KEYOFF=n {#c17-i0219}
*分類: その他*  ・  難易度: 中級

KEYOFF=nは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。VSAM KSDS で論理レコード内のキーオフセット指定 (DATACLAS 経由が普通)。「KEYOFF=n」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 展開判定のその他で KEYOFF=nの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. KEYOFF=nの出力を取らず展開判定のその他の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開判定の確認結果にする。 ✅
    - C. ST OSKBDD を省略して展開判定のその他の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定のその他へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定のその他において選択記号 B を採用し、識別名は展開判定です。展開判定のその他において KEYOFF=n は説明欄の「展開判定のその他に関係する定義値と表示行を照合する展開判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は展開判定です。展開判定のその他の証跡を読む担当者は、KEYOFF=nの属性行と IEF236I を合わせて追跡し、背景名は展開判定です。誤答側の問題点を分けます。 A: 展開判定のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため展開判定ではありません。 B: 展開判定のその他は対象出力と項目説明を結び、根拠を残すので展開判定です。 C: 展開判定のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため展開判定ではありません。 D: 展開判定のその他は別カテゴリの確認を流用しており、KEYOFF=nの根拠にならないため展開判定ではありません。展開判定のその他に出る KEYOFF=nは JCL DD 文の運用手順で意味を確認する対象であり、用語名は展開判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **KEYOFF=n**

    - 検証目的: 終端記録のその他について、KEYOFF=nは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。VSAM KSDS で論理レコード内のキーオフセット指定 (DATACLに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020125の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端記録のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にKEYOFF=nを指定し、OSKB020125の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND KEYOFF=n
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM KEYOFF=n
    CASE OSKB020125
    SOURCE z/OS JCL
    ```

    KEYOFF=nとOSKB020125が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020125を同じ出力で読み、終端記録のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020125
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020125.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020125 STEP1 SYSUT1
    ```

    IEF236IとOSKB020125が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の KEYOFF=n と OSKB020125 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### LGSTREAM=名前 {#c17-i0220}
*分類: その他*  ・  難易度: 中級

System Logger ログストリームの DD 参照。長期ログのバッチ参照用途。「LGSTREAM=名前」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 構文判定の名前に関係する LGSTREAM= 名前の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文判定として残す。 ✅
    - B. LGSTREAM= 名前の名称と担当者名のみを残して構文判定の名前の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で構文判定の名前を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文判定の名前の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定の名前において選択記号 A を採用し、識別名は構文判定です。構文判定の名前において LGSTREAM= 名前 は説明欄の「LGSTREAM= 名前の用途をジョブデータ定義の表示で確認する構文判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は構文判定です。構文判定の名前に関連して、z/OS JCL では LGSTREAM= 名前の表示属性と IEF236I を同じ証跡に残し、背景名は構文判定です。他の選択肢を確認します。 A: 構文判定の名前は対象出力と項目説明を結び、根拠を残すので構文判定です。 B: 構文判定の名前は名称や説明のみに寄り、状態を示す出力本文が不足するため構文判定ではありません。 C: 構文判定の名前は別カテゴリの確認を流用しており、LGSTREAM= 名前の根拠にならないため構文判定ではありません。 D: 構文判定の名前は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため構文判定ではありません。構文判定の名前で使う LGSTREAM= 名前という用語は JCL DD 文で扱う確認対象であり、用語名は構文判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **LGSTREAM= 名前**

    - 検証目的: 置換記録の名前について、System Logger ログストリームの DD 参照。長期ログのバッチ参照用途。「LGSTREAM= 名前」を読むと、プログラムが参照する DD 名と、実際に割り当てられに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020124の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換記録の名前の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLGSTREAM= 名前を指定し、OSKB020124の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LGSTREAM= 名前
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LGSTREAM= 名前
    CASE OSKB020124
    SOURCE z/OS JCL
    ```

    LGSTREAM= 名前とOSKB020124が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020124を同じ出力で読み、置換記録の名前の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020124
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020124.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020124 STEP1 SYSUT1
    ```

    IEF236IとOSKB020124が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の LGSTREAM= 名前 と OSKB020124 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PROTECT=YES {#c17-i0221}
*分類: その他*  ・  難易度: 中級

PROTECT=YESは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 範囲検査のその他でジョブデータ定義の運用確認を行います。PROTECT=YES の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲検査のその他を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲検査のその他を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲検査の記録として扱う。 ✅
    - D. PROTECT=YES の属性行を読まず範囲検査のその他の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査のその他において選択記号 C を採用し、識別名は範囲検査です。範囲検査のその他において PROTECT=YES は説明欄の「z/OS JCL で PROTECT=YES の扱いを記録する範囲検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は範囲検査です。範囲検査のその他を受け取る担当者は、PROTECT=YES の表示結果と IEF236I を同じ確認単位として扱い、背景名は範囲検査です。不適切な選択肢を整理します。 A: 範囲検査のその他は別カテゴリの確認を流用しており、PROTECT=YES の根拠にならないため範囲検査ではありません。 B: 範囲検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため範囲検査ではありません。 C: 範囲検査のその他は対象出力と項目説明を結び、根拠を残すので範囲検査です。 D: 範囲検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲検査ではありません。範囲検査のその他が示す PROTECT=YES は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PROTECT=YES**

    - 検証目的: 比較整理のその他について、PROTECT=YES は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPROTECT=YESを指定し、OSKB020114の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PROTECT=YES
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PROTECT=YES
    CASE OSKB020114
    SOURCE z/OS JCL
    ```

    PROTECT=YESとOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020114を同じ出力で読み、比較整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020114
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020114.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020114 STEP1 SYSUT1
    ```

    IEF236IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PROTECT=YES と OSKB020114 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### QNAME=ddname {#c17-i0222}
*分類: その他*  ・  難易度: 中級

TCAM/VTAM メッセージキュー用 DD 指定。レガシー通信用途。「QNAME=ddname」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 記録検査のその他に関係する QNAME=ddnameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録検査として残す。 ✅
    - B. QNAME=ddnameの名称と担当者名のみを残して記録検査のその他の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で記録検査のその他を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録検査のその他の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査のその他において選択記号 A を採用し、識別名は記録検査です。記録検査のその他において QNAME=ddname は説明欄の「QNAME=ddnameの用途をジョブデータ定義の表示で確認する記録検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は記録検査です。記録検査のその他に関連して、z/OS JCL では QNAME=ddnameの表示属性と IEF236I を同じ証跡に残し、背景名は記録検査です。他の選択肢を確認します。 A: 記録検査のその他は対象出力と項目説明を結び、根拠を残すので記録検査です。 B: 記録検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため記録検査ではありません。 C: 記録検査のその他は別カテゴリの確認を流用しており、QNAME=ddnameの根拠にならないため記録検査ではありません。 D: 記録検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため記録検査ではありません。記録検査のその他で使う QNAME=ddnameという用語は JCL DD 文で扱う確認対象であり、用語名は記録検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **QNAME=ddname**

    - 検証目的: 条件追跡のその他について、TCAM/VTAM メッセージキュー用 DD 指定。レガシー通信用途。「QNAME=ddname」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030049の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、条件追跡のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にQNAME=ddnameを指定し、OSKB030049の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND QNAME=ddname
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM QNAME=ddname
    CASE OSKB030049
    SOURCE z/OS JCL
    ```

    QNAME=ddnameとOSKB030049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030049を同じ出力で読み、条件追跡のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030049
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030049.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030049 STEP1 SYSUT1
    ```

    IEF236IとOSKB030049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の QNAME=ddname と OSKB030049 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **QNAME=ddname**

    - 検証目的: 値域整理のその他について、TCAM/VTAM メッセージキュー用 DD 指定。レガシー通信用途。「QNAME=ddname」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にQNAME=ddnameを指定し、OSKB020116の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND QNAME=ddname
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM QNAME=ddname
    CASE OSKB020116
    SOURCE z/OS JCL
    ```

    QNAME=ddnameとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020116を同じ出力で読み、値域整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020116
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020116.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020116 STEP1 SYSUT1
    ```

    IEF236IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の QNAME=ddname と OSKB020116 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### RECORG=KS/ES/RR/LS {#c17-i0223}
*分類: その他*  ・  難易度: 中級

RECORG=KS/ES/RR/LSは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 出力照合照合の出力照合として RECORG を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 出力照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解はCです。出力照合照合で扱う RECORG は JCL DD 文 の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として RECORG を扱い、分類内の確認名として保存します（出力照合照合終点）。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **RECORG=KS ・ ES ・ RR ・ LS**

    - 検証目的: 探索記録の・ ・ ・について、RECORG=KS/ES/RR/LS は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020126の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索記録の・ ・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECORG=KS ・ ES ・ Rを指定し、OSKB020126の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECORG=KS ・ ES ・ R
    CASE OSKB020126
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECORG=KS ・ ES ・ R
    CASE OSKB020126
    SOURCE z/OS JCL
    ```

    RECORG=KS ・ ES ・ RとOSKB020126が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020126を同じ出力で読み、探索記録の・ ・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020126
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020126
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020126.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020126 STEP1 SYSUT1
    ```

    IEF236IとOSKB020126が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の RECORG=KS ・ ES ・ R と OSKB020126 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020126 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### RLS=NRI/CR/CRE {#c17-i0224}
*分類: その他*  ・  難易度: 中級

RLS=NRI/CR/CREは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。VSAM RLS アクセスレベル。NRI=No Read Integrity, CR=Consistent Read, CRE=CR with Existence

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **RLS=NRI ・ CR ・ CRE**

    - 検証目的: 呼出記録の・ ・について、RLS=NRI/CR/CRE は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。VSAM RLS アクセスレベル。NRI=No Read Iに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020123の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出記録の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRLS=NRI ・ CR ・ CREを指定し、OSKB020123の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RLS=NRI ・ CR ・ CRE
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RLS=NRI ・ CR ・ CRE
    CASE OSKB020123
    SOURCE z/OS JCL
    ```

    RLS=NRI ・ CR ・ CREとOSKB020123が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020123を同じ出力で読み、呼出記録の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020123
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020123.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020123 STEP1 SYSUT1
    ```

    IEF236IとOSKB020123が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の RLS=NRI ・ CR ・ CRE と OSKB020123 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### SECMODEL=(profile) {#c17-i0225}
*分類: その他*  ・  難易度: 中級

SECMODEL=(profile)は、JCL DD 文のその他でリソース定義、モデル、またはポリシーを読むための項目です。RACF プロファイルをモデルとして適用。データセット作成時のセキュリティ属性継承。「SECMODEL=(profile)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 優先検査のその他に関する SECMODEL=(profile)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先検査のその他の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査のその他の証跡として保存して根拠にする。
    - C. SECMODEL=(profile)の変更点を出力本文から切り離して優先検査のその他の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査のその他において選択記号 D を採用し、識別名は優先検査です。優先検査のその他において SECMODEL=(profile) は説明欄の「SECMODEL=(profile)の状態と出力メッセージを結び付ける優先検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査のその他に関する記録は、SECMODEL=(profile)の出力行と IEF236I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため優先検査ではありません。 B: 優先検査のその他は別カテゴリの確認を流用しており、SECMODEL=(profile)の根拠にならないため優先検査ではありません。 C: 優先検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査のその他は対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査のその他で記録する SECMODEL=(profile)はz/OS JCL の確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **SECMODEL=(profile)**

    - 検証目的: 順序整理のその他について、SECMODEL=(profile)は、JCL DD 文のその他でリソース定義、モデル、またはポリシーを読むための項目です。RACF プロファイルをモデルとして適用。データに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSECMODEL=(profile)を指定し、OSKB020115の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SECMODEL=(profile)
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SECMODEL=(profile)
    CASE OSKB020115
    SOURCE z/OS JCL
    ```

    SECMODEL=(profile)とOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020115を同じ出力で読み、順序整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020115
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020115.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020115 STEP1 SYSUT1
    ```

    IEF236IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SECMODEL=(profile) と OSKB020115 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### TERM=TS {#c17-i0226}
*分類: その他*  ・  難易度: 中級

TERM=TSは、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 比較検査のその他で TERM=TS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TERM=TS の出力を取らず比較検査のその他の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較検査の確認結果にする。 ✅
    - C. ST OSKBDD を省略して比較検査のその他の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のその他へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査のその他において選択記号 B を採用し、識別名は比較検査です。比較検査のその他において TERM=TS は説明欄の「比較検査のその他に関係する定義値と表示行を照合する比較検査項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は比較検査です。比較検査のその他の証跡を読む担当者は、TERM=TS の属性行と IEF236I を合わせて追跡し、背景名は比較検査です。誤答側の問題点を分けます。 A: 比較検査のその他は名称や説明のみに寄り、状態を示す出力本文が不足するため比較検査ではありません。 B: 比較検査のその他は対象出力と項目説明を結び、根拠を残すので比較検査です。 C: 比較検査のその他は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため比較検査ではありません。 D: 比較検査のその他は別カテゴリの確認を流用しており、TERM=TS の根拠にならないため比較検査ではありません。比較検査のその他に出る TERM=TS は JCL DD 文の運用手順で意味を確認する対象であり、用語名は比較検査です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **TERM=TS**

    - 検証目的: 警告整理のその他について、TERM=TS は、JCL DD 文のその他で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認しまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、警告整理のその他の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTERM=TSを指定し、OSKB020117の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TERM=TS
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TERM=TS
    CASE OSKB020117
    SOURCE z/OS JCL
    ```

    TERM=TSとOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020117を同じ出力で読み、警告整理のその他の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020117
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020117.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020117 STEP1 SYSUT1
    ```

    IEF236IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の TERM=TS と OSKB020117 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > インライン

### /* (デフォルトデリミタ) {#c17-i0227}
*分類: インライン*  ・  難易度: 中級

/* (デフォルトデリミタ)は、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 構文読解の・* デフォルトデリミタに関係する・* (デフォルトデリミタ)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文読解で再確認できる形にする。 ✅
    - B. ・* (デフォルトデリミタ)の名称と担当者名だけを残して構文読解の・* デフォルトデリミタの表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で構文読解の・* デフォルトデリミタを確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文読解の・* デフォルトデリミタの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では・* (デフォルトデリミタ)は「・* (デフォルトデリミタ)の用途をジョブデータ定義の表示で確認する構文読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景ではz/OS JCL の・* (デフォルトデリミタ)と IEF236I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明だけに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では・* (デフォルトデリミタ)を JCL DD 文で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **・* (デフォルトデリミタ)**

    - 検証目的: 記録照合の・* デフォルトデリミタについて、/* (デフォルトデリミタ)は、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030033の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録照合の・* デフォルトデリミタの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に・* (デフォルトデリミタ)を指定し、OSKB030033の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ・* (デフォルトデリミタ)
    CASE OSKB030033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ・* (デフォルトデリミタ)
    CASE OSKB030033
    SOURCE z/OS JCL
    ```

    ・* (デフォルトデリミタ)とOSKB030033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030033を同じ出力で読み、記録照合の・* デフォルトデリミタの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030033
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030033
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030033.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030033 STEP1 SYSUT1
    ```

    IEF236IとOSKB030033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の ・* (デフォルトデリミタ) と OSKB030033 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **・* (デフォルトデリミタ)**

    - 検証目的: 値域照合の・* デフォルトデリミタについて、/* (デフォルトデリミタ)は、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域照合の・* デフォルトデリミタの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に・* (デフォルトデリミタ)を指定し、OSKB020036の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ・* (デフォルトデリミタ)
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ・* (デフォルトデリミタ)
    CASE OSKB020036
    SOURCE z/OS JCL
    ```

    ・* (デフォルトデリミタ)とOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020036を同じ出力で読み、値域照合の・* デフォルトデリミタの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020036
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020036.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020036 STEP1 SYSUT1
    ```

    IEF236IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の ・* (デフォルトデリミタ) と OSKB020036 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DD * {#c17-i0228}
*分類: インライン*  ・  難易度: 中級

DD *は、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 復旧分離の*で DD *の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DD *の出力を取らず復旧分離の*の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧分離として引き継ぐ。 ✅
    - C. ST OSKBDD を省略して復旧分離の*の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧分離の*へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では DD * は「復旧分離の*に関係する定義値と表示行を照合する復旧分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では DD *の属性行と IEF236I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明だけに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では DD *を JCL DD 文の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 変更照合の*に関する DD *の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず変更照合の*の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の*の証跡として保存して根拠にする。
    - C. DD *の変更点を出力本文から切り離して変更照合の*の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合の*において選択記号 D を採用し、識別名は変更照合です。変更照合の*において DD * は説明欄の「DD *の状態と出力メッセージを結び付ける変更照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の*に関する記録は、DD *の出力行と IEF236I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の*は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため変更照合ではありません。 B: 変更照合の*は別カテゴリの確認を流用しており、DD *の根拠にならないため変更照合ではありません。 C: 変更照合の*は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の*は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の*で記録する DD *はz/OS JCL の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DD ***

    - 検証目的: 記録照合の*について、DD *は、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録照合の*の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD *を指定し、OSKB020033の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD *
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD *
    CASE OSKB020033
    SOURCE z/OS JCL
    ```

    DD *とOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020033を同じ出力で読み、記録照合の*の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020033
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020033.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020033 STEP1 SYSUT1
    ```

    IEF236IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD * と OSKB020033 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DD DATA {#c17-i0229}
*分類: インライン*  ・  難易度: 中級

DD DATAは、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。DD * と同様だがデータ内に // を含めても JCL として解釈されない。JCL を流し込むユーティリティに有効。「DD DATA」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 監査分離のインラインでジョブデータ定義の運用確認を行います。DD DATA の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査分離のインラインを確認した扱いにする。
    - B. IEF236I の有無を確認せず監査分離のインラインを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査分離の確認にする。 ✅
    - D. DD DATA の属性行を読まず監査分離のインラインの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では DD DATA は「z/OS JCL で DD DATA の扱いを記録する監査分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では DD DATA の表示結果と IEF236I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明だけに寄り、判定名は監査分離不足です。監査分離資料では DD DATA の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 構文追跡のインラインに関係する DD DATA の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 ✅
    - B. DD DATA の名称と担当者名のみを残して構文追跡のインラインの表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で構文追跡のインラインを確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文追跡のインラインの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡のインラインにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のインラインにおいて DD DATA は説明欄の「DD DATA の用途をジョブデータ定義の表示で確認する構文追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のインラインに関連して、z/OS JCL では DD DATA の表示属性と IEF236I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のインラインは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のインラインは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のインラインは別カテゴリの確認を流用しており、DD DATA の根拠にならないため構文追跡ではありません。 D: 構文追跡のインラインは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため構文追跡ではありません。構文追跡のインラインで使う DD DATA という用語は JCL DD 文で扱う確認対象であり、用語名は構文追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DD DATA**

    - 検証目的: 比較照合のインラインについて、DD DATA は、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。DD * と同様だがデータ内に // を含めても JCL として解釈さに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較照合のインラインの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD DATAを指定し、OSKB020034の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD DATA
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD DATA
    CASE OSKB020034
    SOURCE z/OS JCL
    ```

    DD DATAとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020034を同じ出力で読み、比較照合のインラインの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020034
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020034.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020034 STEP1 SYSUT1
    ```

    IEF236IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD DATA と OSKB020034 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DLM=delimiter {#c17-i0230}
*分類: インライン*  ・  難易度: 中級

DLM=delimiterは、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。DD DATA / DD * の終了デリミタを 2 文字で再定義。データ内に /* を含めたい場合などに使用。「DLM=delimiter」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 変更分離のインラインに関する DLM=delimiterの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず変更分離のインラインの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更分離のインラインの証跡として保存して根拠にする。
    - C. DLM=delimiterの変更点を出力本文から切り離して変更分離のインラインの承認欄だけ残す。
    - D. z/OS JCL の表示形式に沿って根拠行を採り、変更分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では DLM=delimiter は「DLM=delimiterの状態と出力メッセージを結び付ける変更分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では DLM=delimiterの出力行と IEF236I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明だけに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では DLM=delimiterをz/OS JCL の確認記録に残し、対象名は変更分離対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 展開追跡のインラインで DLM=delimiterの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DLM=delimiterの出力を取らず展開追跡のインラインの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 ✅
    - C. ST OSKBDD を省略して展開追跡のインラインの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のインラインへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡のインラインにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のインラインにおいて DLM=delimiter は説明欄の「展開追跡のインラインに関係する定義値と表示行を照合する展開追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のインラインの証跡を読む担当者は、DLM=delimiterの属性行と IEF236I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のインラインは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のインラインは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のインラインは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のインラインは別カテゴリの確認を流用しており、DLM=delimiterの根拠にならないため展開追跡ではありません。展開追跡のインラインに出る DLM=delimiterは JCL DD 文の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DLM=delimiter**

    - 検証目的: 順序照合のインラインについて、DLM=delimiterは、JCL DD 文のインラインで機能名、見出し、または確認対象として参照する項目です。DD DATA / DD * の終了デリミタを 2 文字でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序照合のインラインの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDLM=delimiterを指定し、OSKB020035の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DLM=delimiter
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DLM=delimiter
    CASE OSKB020035
    SOURCE z/OS JCL
    ```

    DLM=delimiterとOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020035を同じ出力で読み、順序照合のインラインの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020035
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020035.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020035 STEP1 SYSUT1
    ```

    IEF236IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DLM=delimiter と OSKB020035 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### インライン DCB の既定値 {#c17-i0231}
*分類: インライン*  ・  難易度: 中級

DD * の既定 LRECL=80, RECFM=FB, BLKSIZE=80。LRECL/RECFM は明示指定可。「インライン DCB の既定値」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 呼出読解のインライン の既定値でジョブデータ定義の運用確認を行います。インライン DCB の既定値の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出読解のインライン の既定値を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出読解のインライン の既定値を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出読解の根拠を固定する。 ✅
    - D. インライン DCB の既定値の属性行を読まず呼出読解のインライン の既定値の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠ではインライン DCB の既定値 は「z/OS JCL でインライン DCB の既定値の扱いを記録する呼出読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡ではインライン DCB の既定値の表示結果と IEF236I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明だけに寄り、判定名は呼出読解不足です。呼出読解資料ではインライン DCB の既定値の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 終端追跡のインライン の既定値に関係するインライン DCB の既定値の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 ✅
    - B. インライン DCB の既定値の名称と担当者名のみを残して終端追跡のインライン の既定値の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で終端追跡のインライン の既定値を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端追跡のインライン の既定値の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡のインライン の既定値において選択記号 A を採用し、識別名は終端追跡です。終端追跡のインライン の既定値においてインライン DCB の既定値 は説明欄の「インライン DCB の既定値の用途をジョブデータ定義の表示で確認する終端追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のインライン の既定値に関連して、z/OS JCL ではインライン DCB の既定値の表示属性と IEF236I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のインライン の既定値は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のインライン の既定値は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のインライン の既定値は別カテゴリの確認を流用しており、インライン DCB の既定値の根拠にならないため終端追跡ではありません。 D: 終端追跡のインライン の既定値は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため終端追跡ではありません。終端追跡のインライン の既定値で使うインライン DCB の既定値という用語は JCL DD 文で扱う確認対象であり、用語名は終端追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **インライン DCB の既定値**

    - 検証目的: 復旧照合のインライン の既定値について、DD * の既定 LRECL=80, RECFM=FB, BLKSIZE=80。LRECL/RECFM は明示指定可。「インライン DCB の既定値」は割り当て結果を調べるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧照合のインライン の既定値の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にインライン DCB の既定値を指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND インライン DCB の既定値
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM インライン DCB の既定値
    CASE OSKB020038
    SOURCE z/OS JCL
    ```

    インライン DCB の既定値とOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020038を同じ出力で読み、復旧照合のインライン の既定値の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020038
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020038.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020038 STEP1 SYSUT1
    ```

    IEF236IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の インライン DCB の既定値 と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### 次の // でも終了 {#c17-i0232}
*分類: インライン*  ・  難易度: 中級

DLM 未指定なら次の // で始まる行が出現した時点で実質終了。「次の // でも終了」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 展開読解の次の ・・ でも終了で次の ・・ でも終了の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 次の ・・ でも終了の出力を取らず展開読解の次の ・・ でも終了の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開読解の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して展開読解の次の ・・ でも終了の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開読解の次の ・・ でも終了へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では次の ・・ でも終了は「展開読解の次の ・・ でも終了に関係する定義値と表示行を照合する展開読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では次の ・・ でも終了の属性行と IEF236I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明だけに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では次の ・・ でも終了を JCL DD 文の運用手順で確認し、初出名は展開読解初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 置換追跡の次の ・・ でも終了に関する次の ・・ でも終了の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換追跡の次の ・・ でも終了の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の次の ・・ でも終了の証跡として保存して根拠にする。
    - C. 次の ・・ でも終了の変更点を出力本文から切り離して置換追跡の次の ・・ でも終了の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡の次の ・・ でも終了において選択記号 D を採用し、識別名は置換追跡です。置換追跡の次の ・・ でも終了において次の ・・ でも終了は説明欄の「次の ・・ でも終了の状態と出力メッセージを結び付ける置換追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の次の ・・ でも終了に関する記録は、次の ・・ でも終了の出力行と IEF236I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の次の ・・ でも終了は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の次の ・・ でも終了は別カテゴリの確認を流用しており、次の ・・ でも終了の根拠にならないため置換追跡ではありません。 C: 置換追跡の次の ・・ でも終了は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の次の ・・ でも終了は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の次の ・・ でも終了で記録する次の ・・ でも終了はz/OS JCL の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **次の ・・ でも終了**

    - 検証目的: 警告照合の次の ・・ でも終了について、DLM 未指定なら次の // で始まる行が出現した時点で実質終了。「次の // でも終了」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、警告照合の次の ・・ でも終了の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に次の ・・ でも終了を指定し、OSKB020037の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 次の ・・ でも終了
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 次の ・・ でも終了
    CASE OSKB020037
    SOURCE z/OS JCL
    ```

    次の ・・ でも終了とOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020037を同じ出力で読み、警告照合の次の ・・ でも終了の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020037
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020037.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020037 STEP1 SYSUT1
    ```

    IEF236IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の 次の ・・ でも終了 と OSKB020037 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > 保持期間

### EXPDT と RETPD の関係 {#c17-i0233}
*分類: 保持期間*  ・  難易度: 中級

両者を同時に指定するとエラー。DD 文では 1 つに統一して書く。「EXPDT と RETPD の関係」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 呼出追跡のと の関係でジョブデータ定義の運用確認を行います。EXPDT と RETPD の関係の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出追跡のと の関係を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出追跡のと の関係を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 ✅
    - D. EXPDT と RETPD の関係の属性行を読まず呼出追跡のと の関係の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡のと の関係において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のと の関係において EXPDT と RETPD の関係 は説明欄の「両者を同時に指定するとエラー。DD 文では 1 つに統一して書く。「EXPDT と RETPD の関係」は割り当て結果を調べるとき、DISP」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のと の関係を受け取る担当者は、EXPDT と RETPD の関係の表示結果と IEF236I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のと の関係は別カテゴリの確認を流用しており、EXPDT と RETPD の関係の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のと の関係は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のと の関係は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のと の関係は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のと の関係が示す EXPDT と RETPD の関係は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **EXPDT と RETPD の関係**

    - 検証目的: 呼出追跡のの関係について、両者を同時に指定するとエラー。DD 文では 1 つに統一して書く。「EXPDT と RETPD の関係」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCBに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030043の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出追跡のの関係の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEXPDT と RETPD の関係を指定し、OSKB030043の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EXPDT と RETPD の関係
    CASE OSKB030043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EXPDT と RETPD の関係
    CASE OSKB030043
    SOURCE z/OS JCL
    ```

    EXPDT と RETPD の関係とOSKB030043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030043を同じ出力で読み、呼出追跡のの関係の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030043
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030043
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030043.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030043 STEP1 SYSUT1
    ```

    IEF236IとOSKB030043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の EXPDT と RETPD の関係 と OSKB030043 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **EXPDT と RETPD の関係**

    - 検証目的: 探索判定のと の関係について、両者を同時に指定するとエラー。DD 文では 1 つに統一して書く。「EXPDT と RETPD の関係」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCBに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索判定のと の関係の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEXPDT と RETPD の関係を指定し、OSKB020086の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EXPDT と RETPD の関係
    CASE OSKB020086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EXPDT と RETPD の関係
    CASE OSKB020086
    SOURCE z/OS JCL
    ```

    EXPDT と RETPD の関係とOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020086を同じ出力で読み、探索判定のと の関係の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020086
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020086
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020086.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020086 STEP1 SYSUT1
    ```

    IEF236IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の EXPDT と RETPD の関係 と OSKB020086 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### EXPDT=1999/365 (永久) {#c17-i0234}
*分類: 保持期間*  ・  難易度: 中級

EXPDT=1999/365 (永久)は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **EXPDT=1999 ・365 (永久)**

    - 検証目的: 置換判定の・ 永久について、EXPDT=1999/365 (永久)は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020084の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換判定の・ 永久の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEXPDT=1999 ・365 (永を指定し、OSKB020084の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EXPDT=1999 ・365 (永
    CASE OSKB020084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EXPDT=1999 ・365 (永
    CASE OSKB020084
    SOURCE z/OS JCL
    ```

    EXPDT=1999 ・365 (永とOSKB020084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020084を同じ出力で読み、置換判定の・ 永久の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020084
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020084
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020084.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020084 STEP1 SYSUT1
    ```

    IEF236IとOSKB020084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の EXPDT=1999 ・365 (永 と OSKB020084 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### EXPDT=YYDDD (旧形式) {#c17-i0235}
*分類: 保持期間*  ・  難易度: 中級

EXPDT=YYDDD (旧形式)は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。2 桁年 + 通算日。1999 年以前運用の互換形式。Y2K 後は YYYY/DDD を推奨。「EXPDT=YYDDD (旧形式)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 監査照合の旧形式でジョブデータ定義の運用確認を行います。EXPDT=YYDDD (旧形式)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査照合の旧形式を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査照合の旧形式を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. EXPDT=YYDDD (旧形式)の属性行を読まず監査照合の旧形式の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合の旧形式において選択記号 C を採用し、識別名は監査照合です。監査照合の旧形式において EXPDT=YYDDD (旧形式) は説明欄の「z/OS JCL で EXPDT=YYDDD (旧形式)の扱いを記録する監査照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の旧形式を受け取る担当者は、EXPDT=YYDDD (旧形式)の表示結果と IEF236I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の旧形式は別カテゴリの確認を流用しており、EXPDT=YYDDD (旧形式)の根拠にならないため監査照合ではありません。 B: 監査照合の旧形式は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため監査照合ではありません。 C: 監査照合の旧形式は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の旧形式は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の旧形式が示す EXPDT=YYDDD (旧形式)は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **EXPDT=YYDDD (旧形式)**

    - 検証目的: 展開判定の旧形式について、EXPDT=YYDDD (旧形式)は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。2 桁年 + 通算日。1999 年以前運用の互換形式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020082の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開判定の旧形式の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEXPDT=YYDDD (旧形式)を指定し、OSKB020082の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EXPDT=YYDDD (旧形式)
    CASE OSKB020082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EXPDT=YYDDD (旧形式)
    CASE OSKB020082
    SOURCE z/OS JCL
    ```

    EXPDT=YYDDD (旧形式)とOSKB020082が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020082を同じ出力で読み、展開判定の旧形式の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020082
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020082
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020082.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020082 STEP1 SYSUT1
    ```

    IEF236IとOSKB020082が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の EXPDT=YYDDD (旧形式) と OSKB020082 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### EXPDT=YYYY/DDD (4 桁年) {#c17-i0236}
*分類: 保持期間*  ・  難易度: 中級

EXPDT=YYYY/DDD (4 桁年)は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。推奨される 4 桁年形式。1900〜2155 が指定可能。「EXPDT=YYYY/DDD (4 桁年)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **EXPDT=YYYY ・ DDD (4 桁年)**

    - 検証目的: 呼出判定の・ 桁年について、EXPDT=YYYY/DDD (4 桁年)は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。推奨される 4 桁年形式。1900〜2155に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020083の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出判定の・ 桁年の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEXPDT=YYYY ・ DDD (を指定し、OSKB020083の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EXPDT=YYYY ・ DDD (
    CASE OSKB020083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EXPDT=YYYY ・ DDD (
    CASE OSKB020083
    SOURCE z/OS JCL
    ```

    EXPDT=YYYY ・ DDD (とOSKB020083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020083を同じ出力で読み、呼出判定の・ 桁年の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020083
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020083
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020083.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020083 STEP1 SYSUT1
    ```

    IEF236IとOSKB020083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の EXPDT=YYYY ・ DDD ( と OSKB020083 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### RETPD=日数 {#c17-i0237}
*分類: 保持期間*  ・  難易度: 中級

RETPD=日数は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。現在日から数えた保持日数。0〜9999。「RETPD=日数」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 展開追跡の日数で RETPD= 日数の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RETPD= 日数の出力を取らず展開追跡の日数の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 ✅
    - C. ST OSKBDD を省略して展開追跡の日数の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の日数へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡の日数において選択記号 B を採用し、識別名は展開追跡です。展開追跡の日数において RETPD= 日数 は説明欄の「展開追跡の日数に関係する定義値と表示行を照合する展開追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の日数の証跡を読む担当者は、RETPD= 日数の属性行と IEF236I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の日数は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の日数は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の日数は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の日数は別カテゴリの確認を流用しており、RETPD= 日数の根拠にならないため展開追跡ではありません。展開追跡の日数に出る RETPD= 日数は JCL DD 文の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **RETPD= 日数**

    - 検証目的: 終端判定の日数について、RETPD= 日数は、JCL DD 文の保持期間で機能名、見出し、または確認対象として参照する項目です。現在日から数えた保持日数。0〜9999。「RETPD= 日数」を読むと、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020085の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端判定の日数の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRETPD= 日数を指定し、OSKB020085の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RETPD= 日数
    CASE OSKB020085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RETPD= 日数
    CASE OSKB020085
    SOURCE z/OS JCL
    ```

    RETPD= 日数とOSKB020085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020085を同じ出力で読み、終端判定の日数の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020085
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020085
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020085.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020085 STEP1 SYSUT1
    ```

    IEF236IとOSKB020085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の RETPD= 日数 と OSKB020085 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > 印刷

### BURST=NO {#c17-i0238}
*分類: 印刷*  ・  難易度: 中級

BURST=NOは、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。バースト無効 (連続紙のまま)。既定値。「BURST=NO」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 範囲分離の印刷でジョブデータ定義の運用確認を行います。BURST=NO の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲分離の印刷を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲分離の印刷を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲分離の根拠を固定する。 ✅
    - D. BURST=NO の属性行を読まず範囲分離の印刷の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では BURST=NO は「z/OS JCL で BURST=NO の扱いを記録する範囲分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では BURST=NO の表示結果と IEF236I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明だけに寄り、判定名は範囲分離不足です。範囲分離資料では BURST=NO の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 記録照合の印刷に関係する BURST=NO の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 ✅
    - B. BURST=NO の名称と担当者名のみを残して記録照合の印刷の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で記録照合の印刷を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録照合の印刷の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合の印刷において選択記号 A を採用し、識別名は記録照合です。記録照合の印刷において BURST=NO は説明欄の「BURST=NO の用途をジョブデータ定義の表示で確認する記録照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の印刷に関連して、z/OS JCL では BURST=NO の表示属性と IEF236I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の印刷は対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の印刷は名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の印刷は別カテゴリの確認を流用しており、BURST=NO の根拠にならないため記録照合ではありません。 D: 記録照合の印刷は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため記録照合ではありません。記録照合の印刷で使う BURST=NO という用語は JCL DD 文で扱う確認対象であり、用語名は記録照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **BURST=NO**

    - 検証目的: 範囲照合の印刷について、BURST=NO は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。バースト無効 (連続紙のまま)。既定値。「BURST=NO」は割り当て結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲照合の印刷の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBURST=NOを指定し、OSKB030031の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BURST=NO
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BURST=NO
    CASE OSKB030031
    SOURCE z/OS JCL
    ```

    BURST=NOとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030031を同じ出力で読み、範囲照合の印刷の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030031
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030031.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030031 STEP1 SYSUT1
    ```

    IEF236IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の BURST=NO と OSKB030031 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **BURST=NO**

    - 検証目的: 探索照合の印刷について、BURST=NO は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。バースト無効 (連続紙のまま)。既定値。「BURST=NO」は割り当て結果に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索照合の印刷の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBURST=NOを指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BURST=NO
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BURST=NO
    CASE OSKB020026
    SOURCE z/OS JCL
    ```

    BURST=NOとOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020026を同じ出力で読み、探索照合の印刷の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020026
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020026.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020026 STEP1 SYSUT1
    ```

    IEF236IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の BURST=NO と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### BURST=YES {#c17-i0239}
*分類: 印刷*  ・  難易度: 中級

3800 印刷装置の連続紙バースト機能を有効化 (用紙切離し)。「BURST=YES」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 区切分離の印刷で BURST=YES の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BURST=YES の出力を取らず区切分離の印刷の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切分離の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して区切分離の印刷の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切分離の印刷へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では BURST=YES は「区切分離の印刷に関係する定義値と表示行を照合する区切分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では BURST=YES の属性行と IEF236I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明だけに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では BURST=YES を JCL DD 文の運用手順で確認し、初出名は区切分離初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 優先照合の印刷に関する BURST=YES の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先照合の印刷の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の印刷の証跡として保存して根拠にする。
    - C. BURST=YES の変更点を出力本文から切り離して優先照合の印刷の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合の印刷において選択記号 D を採用し、識別名は優先照合です。優先照合の印刷において BURST=YES は説明欄の「BURST=YES の状態と出力メッセージを結び付ける優先照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の印刷に関する記録は、BURST=YES の出力行と IEF236I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の印刷は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため優先照合ではありません。 B: 優先照合の印刷は別カテゴリの確認を流用しており、BURST=YES の根拠にならないため優先照合ではありません。 C: 優先照合の印刷は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の印刷は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の印刷で記録する BURST=YES はz/OS JCL の確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **BURST=YES**

    - 検証目的: 終端照合の印刷について、3800 印刷装置の連続紙バースト機能を有効化 (用紙切離し)。「BURST=YES」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端照合の印刷の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBURST=YESを指定し、OSKB020025の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BURST=YES
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BURST=YES
    CASE OSKB020025
    SOURCE z/OS JCL
    ```

    BURST=YESとOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020025を同じ出力で読み、終端照合の印刷の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020025
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020025.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020025 STEP1 SYSUT1
    ```

    IEF236IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の BURST=YES と OSKB020025 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### CHARS=(c1,c2,c3,c4) {#c17-i0240}
*分類: 印刷*  ・  難易度: 中級

TRC 制御文字でフォント切替可能な複数フォント指定形式。「CHARS=(c1,c2,c3,c4)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 記録分離の印刷に関係する CHARS= 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、記録分離の証跡として残す。 ✅
    - B. CHARS= 属性の名称と担当者名だけを残して記録分離の印刷の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で記録分離の印刷を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録分離の印刷の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では CHARS= 属性 は「CHARS= 属性の用途をジョブデータ定義の表示で確認する記録分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景ではz/OS JCL の CHARS= 属性と IEF236I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明だけに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では CHARS= 属性を JCL DD 文で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 順序照合の印刷でジョブデータ定義の運用確認を行います。CHARS=(c1,c2,c3,c4)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序照合の印刷を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序照合の印刷を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序照合の記録として扱う。 ✅
    - D. CHARS=(c1,c2,c3,c4)の属性行を読まず順序照合の印刷の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合の印刷において選択記号 C を採用し、識別名は順序照合です。順序照合の印刷において CHARS=(c1,c2,c3,c4) は説明欄の「z/OS JCL で CHARS=(c1,c2,c3,c4)の扱いを記録する順序照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の印刷を受け取る担当者は、CHARS=(c1,c2,c3,c4)の表示結果と IEF236I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の印刷は別カテゴリの確認を流用しており、CHARS=(c1,c2,c3,c4)の根拠にならないため順序照合ではありません。 B: 順序照合の印刷は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため順序照合ではありません。 C: 順序照合の印刷は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の印刷は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の印刷が示す CHARS=(c1,c2,c3,c4)は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **CHARS=(c1,c2,c3,c4)**

    - 検証目的: 出力照合の印刷について、TRC 制御文字でフォント切替可能な複数フォント指定形式。「CHARS=(c1,c2,c3,c4)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、出力照合の印刷の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCHARS=(c1,c2,c3,c4を指定し、OSKB020028の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CHARS=(c1,c2,c3,c4
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CHARS=(c1,c2,c3,c4
    CASE OSKB020028
    SOURCE z/OS JCL
    ```

    CHARS=(c1,c2,c3,c4とOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020028を同じ出力で読み、出力照合の印刷の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020028
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020028.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020028 STEP1 SYSUT1
    ```

    IEF236IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の CHARS=(c1,c2,c3,c4 と OSKB020028 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### CHARS=文字セット名 {#c17-i0241}
*分類: 印刷*  ・  難易度: 中級

CHARS=文字セット名は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 優先分離の文字セット名に関する CHARS= 文字セット名の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先分離の文字セット名の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先分離の文字セット名の証跡として保存して根拠にする。
    - C. CHARS= 文字セット名の変更点を出力本文から切り離して優先分離の文字セット名の承認欄だけ残す。
    - D. IEF236I を含む表示を保存し、説明欄との差分を優先分離で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では CHARS= 文字セット名 は「CHARS= 文字セット名の状態と出力メッセージを結び付ける優先分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では CHARS= 文字セット名の出力行と IEF236I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明だけに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では CHARS= 文字セット名をz/OS JCL の確認記録に残し、対象名は優先分離対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 比較照合の文字セット名で CHARS= 文字セット名の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CHARS= 文字セット名の出力を取らず比較照合の文字セット名の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して比較照合の文字セット名の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の文字セット名へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合の文字セット名において選択記号 B を採用し、識別名は比較照合です。比較照合の文字セット名において CHARS= 文字セット名 は説明欄の「比較照合の文字セット名に関係する定義値と表示行を照合する比較照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の文字セット名の証跡を読む担当者は、CHARS= 文字セット名の属性行と IEF236I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の文字セット名は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の文字セット名は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の文字セット名は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため比較照合ではありません。 D: 比較照合の文字セット名は別カテゴリの確認を流用しており、CHARS= 文字セット名の根拠にならないため比較照合ではありません。比較照合の文字セット名に出る CHARS= 文字セット名は JCL DD 文の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **CHARS= 文字セット名**

    - 検証目的: 上書照合の文字セット名について、CHARS= 文字セット名は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、上書照合の文字セット名の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCHARS= 文字セット名を指定し、OSKB020027の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CHARS= 文字セット名
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CHARS= 文字セット名
    CASE OSKB020027
    SOURCE z/OS JCL
    ```

    CHARS= 文字セット名とOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020027を同じ出力で読み、上書照合の文字セット名の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020027
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020027.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020027 STEP1 SYSUT1
    ```

    IEF236IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の CHARS= 文字セット名 と OSKB020027 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FLASH=(form,count) {#c17-i0242}
*分類: 印刷*  ・  難易度: 中級

FLASH=(form,count)は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 順序分離の印刷でジョブデータ定義の運用確認を行います。FLASH=(form 命令の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序分離の印刷を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序分離の印刷を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序分離の根拠にする。 ✅
    - D. FLASH=(form 命令の属性行を読まず順序分離の印刷の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では FLASH=(form 命令 は「z/OS JCL で FLASH=(form 命令の扱いを記録する順序分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では FLASH=(form 命令の表示結果と IEF236I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明だけに寄り、判定名は順序分離不足です。順序分離資料では FLASH=(form 命令の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 警告照合の印刷に関係する FLASH=(form,count)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 ✅
    - B. FLASH=(form,count)の名称と担当者名のみを残して警告照合の印刷の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で警告照合の印刷を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告照合の印刷の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合の印刷において選択記号 A を採用し、識別名は警告照合です。警告照合の印刷において FLASH=(form,count) は説明欄の「FLASH=(form,count)の用途をジョブデータ定義の表示で確認する警告照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の印刷に関連して、z/OS JCL では FLASH=(form,count)の表示属性と IEF236I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の印刷は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の印刷は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の印刷は別カテゴリの確認を流用しており、FLASH=(form,count)の根拠にならないため警告照合ではありません。 D: 警告照合の印刷は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため警告照合ではありません。警告照合の印刷で使う FLASH=(form,count)という用語は JCL DD 文で扱う確認対象であり、用語名は警告照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FLASH=(form,count)**

    - 検証目的: 区切照合の印刷について、FLASH=(form,count)は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切照合の印刷の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にFLASH=(form,count)を指定し、OSKB020030の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FLASH=(form,count)
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FLASH=(form,count)
    CASE OSKB020030
    SOURCE z/OS JCL
    ```

    FLASH=(form,count)とOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020030を同じ出力で読み、区切照合の印刷の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020030
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020030.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020030 STEP1 SYSUT1
    ```

    IEF236IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FLASH=(form,count) と OSKB020030 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FLASH=オーバーレイ {#c17-i0243}
*分類: 印刷*  ・  難易度: 中級

FLASH=オーバーレイは、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。プリオーバーレイ (定型帳票枠) のフォーム名を指定。「FLASH=オーバーレイ」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 比較分離のオーバーレイで FLASH= オーバーレイの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FLASH= オーバーレイの出力を取らず比較分離のオーバーレイの説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、比較分離の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して比較分離のオーバーレイの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較分離のオーバーレイへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では FLASH= オーバーレイ は「比較分離のオーバーレイに関係する定義値と表示行を照合する比較分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では FLASH= オーバーレイの属性行と IEF236I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明だけに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では FLASH= オーバーレイを JCL DD 文の運用手順で確認し、初出名は比較分離初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 値域照合のオーバーレイに関する FLASH= オーバーレイの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域照合のオーバーレイの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のオーバーレイの証跡として保存して根拠にする。
    - C. FLASH= オーバーレイの変更点を出力本文から切り離して値域照合のオーバーレイの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合のオーバーレイにおいて選択記号 D を採用し、識別名は値域照合です。値域照合のオーバーレイにおいて FLASH= オーバーレイ は説明欄の「FLASH= オーバーレイの状態と出力メッセージを結び付ける値域照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のオーバーレイに関する記録は、FLASH= オーバーレイの出力行と IEF236I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のオーバーレイは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため値域照合ではありません。 B: 値域照合のオーバーレイは別カテゴリの確認を流用しており、FLASH= オーバーレイの根拠にならないため値域照合ではありません。 C: 値域照合のオーバーレイは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のオーバーレイは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のオーバーレイで記録する FLASH= オーバーレイはz/OS JCL の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FLASH= オーバーレイ**

    - 検証目的: 条件照合のオーバーレイについて、FLASH= オーバーレイは、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。プリオーバーレイ (定型帳票枠) のフォーム名を指定。「FLASHに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、条件照合のオーバーレイの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にFLASH= オーバーレイを指定し、OSKB020029の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FLASH= オーバーレイ
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FLASH= オーバーレイ
    CASE OSKB020029
    SOURCE z/OS JCL
    ```

    FLASH= オーバーレイとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020029を同じ出力で読み、条件照合のオーバーレイの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020029
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020029.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020029 STEP1 SYSUT1
    ```

    IEF236IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FLASH= オーバーレイ と OSKB020029 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### MODIFY=(module,trc) {#c17-i0244}
*分類: 印刷*  ・  難易度: 中級

MODIFY=(module,trc)は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。TRC (Table Reference Character) を指定して、モジュール内のフォント参照を制御。「MODIFY=(module,trc)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 警告分離の印刷に関係する MODIFY= 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD で得た表示本文を使い、警告分離の採否を説明欄に結び付ける。 ✅
    - B. MODIFY= 属性の名称と担当者名だけを残して警告分離の印刷の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で警告分離の印刷を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告分離の印刷の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では MODIFY= 属性 は「MODIFY= 属性の用途をジョブデータ定義の表示で確認する警告分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景ではz/OS JCL の MODIFY= 属性と IEF236I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明だけに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では MODIFY= 属性を JCL DD 文で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 監査照合の印刷でジョブデータ定義の運用確認を行います。MODIFY=(module,trc)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査照合の印刷を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査照合の印刷を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. MODIFY=(module,trc)の属性行を読まず監査照合の印刷の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合の印刷において選択記号 C を採用し、識別名は監査照合です。監査照合の印刷において MODIFY=(module,trc) は説明欄の「z/OS JCL で MODIFY=(module,trc)の扱いを記録する監査照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の印刷を受け取る担当者は、MODIFY=(module,trc)の表示結果と IEF236I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の印刷は別カテゴリの確認を流用しており、MODIFY=(module,trc)の根拠にならないため監査照合ではありません。 B: 監査照合の印刷は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため監査照合ではありません。 C: 監査照合の印刷は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の印刷は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の印刷が示す MODIFY=(module,trc)は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **MODIFY=(module,trc)**

    - 検証目的: 優先照合の印刷について、MODIFY=(module,trc)は、JCL DD 文の印刷で機能名、見出し、または確認対象として参照する項目です。TRC (Table Reference Charaに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先照合の印刷の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMODIFY=(module,trcを指定し、OSKB020032の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MODIFY=(module,trc
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MODIFY=(module,trc
    CASE OSKB020032
    SOURCE z/OS JCL
    ```

    MODIFY=(module,trcとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020032を同じ出力で読み、優先照合の印刷の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020032
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020032.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020032 STEP1 SYSUT1
    ```

    IEF236IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の MODIFY=(module,trc と OSKB020032 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### MODIFY=コピー修整モジュール {#c17-i0245}
*分類: 印刷*  ・  難易度: 中級

コピーグループごとに重ね合わせるテキストモジュールを指定。「MODIFY=コピー修整モジュール」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 値域分離のコピー修整モジュールに関する MODIFY 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域分離のコピー修整モジュールの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域分離のコピー修整モジュールの証跡として保存して根拠にする。
    - C. MODIFY 属性の変更点を出力本文から切り離して値域分離のコピー修整モジュールの承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、値域分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では MODIFY 属性 は「MODIFY 属性の状態と出力メッセージを結び付ける値域分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では MODIFY 属性の出力行と IEF236I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明だけに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では MODIFY 属性をz/OS JCL の確認記録に残し、対象名は値域分離対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 復旧照合のコピー修整モジュールで MODIFY= コピー修整モジュールの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MODIFY= コピー修整モジュールの出力を取らず復旧照合のコピー修整モジュールの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して復旧照合のコピー修整モジュールの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のコピー修整モジュールへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合のコピー修整モジュールにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合のコピー修整モジュールにおいて MODIFY= コピー修整モジュール は説明欄の「復旧照合のコピー修整モジュールに関係する定義値と表示行を照合する復旧照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のコピー修整モジュールの証跡を読む担当者は、MODIFY= コピー修整モジュールの属性行と IEF236I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のコピー修整モジュールは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のコピー修整モジュールは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のコピー修整モジュールは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のコピー修整モジュールは別カテゴリの確認を流用しており、MODIFY= コピー修整モジュールの根拠にならないため復旧照合ではありません。復旧照合のコピー修整モジュールに出る MODIFY= コピー修整モジュールは JCL DD 文の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **MODIFY= コピー修整モジュール**

    - 検証目的: 優先照合のコピー修整モジュールについて、コピーグループごとに重ね合わせるテキストモジュールを指定。「MODIFY= コピー修整モジュール」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先照合のコピー修整モジュールの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMODIFY= コピー修整モジュールを指定し、OSKB030032の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MODIFY= コピー修整モジュール
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MODIFY= コピー修整モジュール
    CASE OSKB030032
    SOURCE z/OS JCL
    ```

    MODIFY= コピー修整モジュールとOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030032を同じ出力で読み、優先照合のコピー修整モジュールの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030032
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030032.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030032 STEP1 SYSUT1
    ```

    IEF236IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の MODIFY= コピー修整モジュール と OSKB030032 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MODIFY= コピー修整モジュール**

    - 検証目的: 範囲照合のコピー修整モジュールについて、コピーグループごとに重ね合わせるテキストモジュールを指定。「MODIFY= コピー修整モジュール」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲照合のコピー修整モジュールの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMODIFY= コピー修整モジュールを指定し、OSKB020031の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MODIFY= コピー修整モジュール
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MODIFY= コピー修整モジュール
    CASE OSKB020031
    SOURCE z/OS JCL
    ```

    MODIFY= コピー修整モジュールとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020031を同じ出力で読み、範囲照合のコピー修整モジュールの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020031
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020031.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020031 STEP1 SYSUT1
    ```

    IEF236IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の MODIFY= コピー修整モジュール と OSKB020031 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > 横断ルール

### DD の継続行 {#c17-i0246}
*分類: 横断ルール*  ・  難易度: 中級

DD の継続行は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。桁 71 で切ってカンマで終え、次行を桁 16 までインデント開始。JCL の継続規約 (1〜71 桁) を守る。「DD の継続行」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 上書判定のの継続行でジョブデータ定義の運用確認を行います。DD の継続行の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書判定のの継続行を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書判定のの継続行を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書判定の記録として扱う。 ✅
    - D. DD の継続行の属性行を読まず上書判定のの継続行の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定のの継続行において選択記号 C を採用し、識別名は上書判定です。上書判定のの継続行において DD の継続行 は説明欄の「z/OS JCL で DD の継続行の扱いを記録する上書判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書判定です。上書判定のの継続行を受け取る担当者は、DD の継続行の表示結果と IEF236I を同じ確認単位として扱い、背景名は上書判定です。不適切な選択肢を整理します。 A: 上書判定のの継続行は別カテゴリの確認を流用しており、DD の継続行の根拠にならないため上書判定ではありません。 B: 上書判定のの継続行は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書判定ではありません。 C: 上書判定のの継続行は対象出力と項目説明を結び、根拠を残すので上書判定です。 D: 上書判定のの継続行は名称や説明のみに寄り、状態を示す出力本文が不足するため上書判定ではありません。上書判定のの継続行が示す DD の継続行は出典欄の資料で使い方を追跡できる項目であり、用語名は上書判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DD の継続行**

    - 検証目的: 区切記録のの継続行について、DD の継続行は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。桁 71 で切ってカンマで終え、次行を桁 16 までインデント開始。Jに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020130の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切記録のの継続行の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD の継続行を指定し、OSKB020130の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD の継続行
    CASE OSKB020130
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD の継続行
    CASE OSKB020130
    SOURCE z/OS JCL
    ```

    DD の継続行とOSKB020130が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020130を同じ出力で読み、区切記録のの継続行の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020130
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020130
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020130.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020130 STEP1 SYSUT1
    ```

    IEF236IとOSKB020130が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD の継続行 と OSKB020130 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020130 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DD 文の位置パラメータ vs キーワード {#c17-i0247}
*分類: 横断ルール*  ・  難易度: 中級

DD の各オペランドはキーワード形式 (DSN=, DISP=, ...) が原則。位置パラメータは内部サブ (DISP の中の状態/正常/異常など) で使われる

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **DD 文の位置パラメータ vs キーワード**

    - 検証目的: 条件記録の文の位置パラメータ キーワードについて、DD の各オペランドはキーワード形式 (DSN=, DISP=, など) が原則。位置パラメータは内部サブ (DISP の中の状態/正常/異常など) で使われるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020129の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、条件記録の文の位置パラメータ キーワードの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD 文の位置パラメータ vs キーを指定し、OSKB020129の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD 文の位置パラメータ vs キー
    CASE OSKB020129
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD 文の位置パラメータ vs キー
    CASE OSKB020129
    SOURCE z/OS JCL
    ```

    DD 文の位置パラメータ vs キーとOSKB020129が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020129を同じ出力で読み、条件記録の文の位置パラメータ キーワードの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020129
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020129
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020129.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020129 STEP1 SYSUT1
    ```

    IEF236IとOSKB020129が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD 文の位置パラメータ vs キー と OSKB020129 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020129 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DD 文最大数 {#c17-i0248}
*分類: 横断ルール*  ・  難易度: 中級

DD 文最大数は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。1 ステップあたりの DD 数には実装上限がある (古くは 1635、現行はさらに緩和)。極端な多 DD 設計は避ける。「DD 文最大数」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 比較判定の文最大数で DD 文最大数の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DD 文最大数の出力を取らず比較判定の文最大数の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較判定の確認結果にする。 ✅
    - C. ST OSKBDD を省略して比較判定の文最大数の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定の文最大数へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定の文最大数において選択記号 B を採用し、識別名は比較判定です。比較判定の文最大数において DD 文最大数 は説明欄の「比較判定の文最大数に関係する定義値と表示行を照合する比較判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は比較判定です。比較判定の文最大数の証跡を読む担当者は、DD 文最大数の属性行と IEF236I を合わせて追跡し、背景名は比較判定です。誤答側の問題点を分けます。 A: 比較判定の文最大数は名称や説明のみに寄り、状態を示す出力本文が不足するため比較判定ではありません。 B: 比較判定の文最大数は対象出力と項目説明を結び、根拠を残すので比較判定です。 C: 比較判定の文最大数は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため比較判定ではありません。 D: 比較判定の文最大数は別カテゴリの確認を流用しており、DD 文最大数の根拠にならないため比較判定ではありません。比較判定の文最大数に出る DD 文最大数は JCL DD 文の運用手順で意味を確認する対象であり、用語名は比較判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DD 文最大数**

    - 検証目的: 警告記録の文最大数について、DD 文最大数は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。1 ステップあたりの DD 数には実装上限がある (古くは 1635、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020137の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、警告記録の文最大数の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD 文最大数を指定し、OSKB020137の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD 文最大数
    CASE OSKB020137
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD 文最大数
    CASE OSKB020137
    SOURCE z/OS JCL
    ```

    DD 文最大数とOSKB020137が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020137を同じ出力で読み、警告記録の文最大数の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020137
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020137
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020137.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020137 STEP1 SYSUT1
    ```

    IEF236IとOSKB020137が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD 文最大数 と OSKB020137 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020137 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DD 省略時のジョブ失敗ケース {#c17-i0249}
*分類: 横断ルール*  ・  難易度: 初級

プログラムが OPEN を試みた DD が JCL に存在しないと S013 など特定の ABEND になる。「DD 省略時のジョブ失敗ケース」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? note "検証手順（1件）"
    **DD 省略時のジョブ失敗ケース**

    - 検証目的: 記録記録の省略時のジョブ失敗ケースについて、プログラムが OPEN を試みた DD が JCL に存在しないと S013 など特定の ABEND になる。「DD 省略時のジョブ失敗ケース」を読むと、プログラムが参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020133の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録記録の省略時のジョブ失敗ケースの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD 省略時のジョブ失敗ケースを指定し、OSKB020133の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD 省略時のジョブ失敗ケース
    CASE OSKB020133
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD 省略時のジョブ失敗ケース
    CASE OSKB020133
    SOURCE z/OS JCL
    ```

    DD 省略時のジョブ失敗ケースとOSKB020133が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020133を同じ出力で読み、記録記録の省略時のジョブ失敗ケースの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020133
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020133
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020133.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020133 STEP1 SYSUT1
    ```

    IEF236IとOSKB020133が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD 省略時のジョブ失敗ケース と OSKB020133 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020133 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### GDG とジョブ別世代 {#c17-i0250}
*分類: 横断ルール*  ・  難易度: 上級

GDG とジョブ別世代は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。1 ジョブ内 (+1) は全ステップで同じ世代を指す。複数ジョブ間で順序保証するには JES ジョブ順序や Scheduler 連携が必要。「GDG とジョブ別世代」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 記録判定のとジョブ別世代に関係する GDG とジョブ別世代の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録判定として残す。 ✅
    - B. GDG とジョブ別世代の名称と担当者名のみを残して記録判定のとジョブ別世代の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で記録判定のとジョブ別世代を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録判定のとジョブ別世代の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録判定のとジョブ別世代において選択記号 A を採用し、識別名は記録判定です。記録判定のとジョブ別世代において GDG とジョブ別世代 は説明欄の「GDG とジョブ別世代の用途をジョブデータ定義の表示で確認する記録判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は記録判定です。記録判定のとジョブ別世代に関連して、z/OS JCL では GDG とジョブ別世代の表示属性と IEF236I を同じ証跡に残し、背景名は記録判定です。他の選択肢を確認します。 A: 記録判定のとジョブ別世代は対象出力と項目説明を結び、根拠を残すので記録判定です。 B: 記録判定のとジョブ別世代は名称や説明のみに寄り、状態を示す出力本文が不足するため記録判定ではありません。 C: 記録判定のとジョブ別世代は別カテゴリの確認を流用しており、GDG とジョブ別世代の根拠にならないため記録判定ではありません。 D: 記録判定のとジョブ別世代は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため記録判定ではありません。記録判定のとジョブ別世代で使う GDG とジョブ別世代という用語は JCL DD 文で扱う確認対象であり、用語名は記録判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **GDG とジョブ別世代**

    - 検証目的: 値域記録のとジョブ別世代について、GDG とジョブ別世代は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。1 ジョブ内 (+1) は全ステップで同じ世代を指す。複数ジョに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020136の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域記録のとジョブ別世代の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にGDG とジョブ別世代を指定し、OSKB020136の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND GDG とジョブ別世代
    CASE OSKB020136
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM GDG とジョブ別世代
    CASE OSKB020136
    SOURCE z/OS JCL
    ```

    GDG とジョブ別世代とOSKB020136が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020136を同じ出力で読み、値域記録のとジョブ別世代の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020136
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020136
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020136.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020136 STEP1 SYSUT1
    ```

    IEF236IとOSKB020136が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の GDG とジョブ別世代 と OSKB020136 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020136 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### GDG モデル DSCB {#c17-i0251}
*分類: 横断ルール*  ・  難易度: 上級

GDG モデル DSCBは、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 優先判定のモデルに関する GDG モデル DSCB の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先判定のモデルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定のモデルの証跡として保存して根拠にする。
    - C. GDG モデル DSCB の変更点を出力本文から切り離して優先判定のモデルの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先判定のモデルにおいて選択記号 D を採用し、識別名は優先判定です。優先判定のモデルにおいて GDG モデル DSCB は説明欄の「GDG モデル DSCB の状態と出力メッセージを結び付ける優先判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は優先判定です。優先判定のモデルに関する記録は、GDG モデル DSCB の出力行と IEF236I を一緒に保存し、背景名は優先判定です。選択肢ごとの違いを示します。 A: 優先判定のモデルは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため優先判定ではありません。 B: 優先判定のモデルは別カテゴリの確認を流用しており、GDG モデル DSCB の根拠にならないため優先判定ではありません。 C: 優先判定のモデルは名称や説明のみに寄り、状態を示す出力本文が不足するため優先判定ではありません。 D: 優先判定のモデルは対象出力と項目説明を結び、根拠を残すので優先判定です。優先判定のモデルで記録する GDG モデル DSCB はz/OS JCL の確認記録に残す対象名であり、用語名は優先判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **GDG モデル DSCB**

    - 検証目的: 順序記録のモデルについて、GDG モデル DSCB は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020135の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序記録のモデルの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にGDG モデル DSCBを指定し、OSKB020135の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND GDG モデル DSCB
    CASE OSKB020135
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM GDG モデル DSCB
    CASE OSKB020135
    SOURCE z/OS JCL
    ```

    GDG モデル DSCBとOSKB020135が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020135を同じ出力で読み、順序記録のモデルの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020135
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020135
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020135.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020135 STEP1 SYSUT1
    ```

    IEF236IとOSKB020135が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の GDG モデル DSCB と OSKB020135 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020135 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### JCL 標準コーディング順序 {#c17-i0252}
*分類: 横断ルール*  ・  難易度: 中級

JCL 標準コーディング順序は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。推奨は DSN により DISP により UNIT により VOL により SPACE により DCB の順。可読性とレビュー効率の社内標準。推奨は DSN → DISP → UNIT → VOL → SPACE → DCB の順。可読性とレビュー効率の社内標準

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 範囲判定の標準コーディング順序でジョブデータ定義の運用確認を行います。JCL 標準コーディング順序の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲判定の標準コーディング順序を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲判定の標準コーディング順序を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲判定の記録として扱う。 ✅
    - D. JCL 標準コーディング順序の属性行を読まず範囲判定の標準コーディング順序の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定の標準コーディング順序において選択記号 C を採用し、識別名は範囲判定です。範囲判定の標準コーディング順序において JCL 標準コーディング順序 は説明欄の「z/OS JCL で JCL 標準コーディング順序の扱いを記録する範囲判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は範囲判定です。範囲判定の標準コーディング順序を受け取る担当者は、JCL 標準コーディング順序の表示結果と IEF236I を同じ確認単位として扱い、背景名は範囲判定です。不適切な選択肢を整理します。 A: 範囲判定の標準コーディング順序は別カテゴリの確認を流用しており、JCL 標準コーディング順序の根拠にならないため範囲判定ではありません。 B: 範囲判定の標準コーディング順序は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため範囲判定ではありません。 C: 範囲判定の標準コーディング順序は対象出力と項目説明を結び、根拠を残すので範囲判定です。 D: 範囲判定の標準コーディング順序は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲判定ではありません。範囲判定の標準コーディング順序が示す JCL 標準コーディング順序は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **JCL 標準コーディング順序**

    - 検証目的: 比較記録の標準コーディング順序について、JCL 標準コーディング順序は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。推奨は DSN により DISP により UNIT によに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020134の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較記録の標準コーディング順序の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にJCL 標準コーディング順序を指定し、OSKB020134の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND JCL 標準コーディング順序
    CASE OSKB020134
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM JCL 標準コーディング順序
    CASE OSKB020134
    SOURCE z/OS JCL
    ```

    JCL 標準コーディング順序とOSKB020134が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020134を同じ出力で読み、比較記録の標準コーディング順序の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020134
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020134
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020134.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020134 STEP1 SYSUT1
    ```

    IEF236IとOSKB020134が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の JCL 標準コーディング順序 と OSKB020134 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020134 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### コメント (//*) {#c17-i0253}
*分類: 横断ルール*  ・  難易度: 中級

コメント (//*)は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。DD の前後で説明コメントを // のあとに * で書く。実行に影響しない。「コメント (//*)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 出力判定のコメント ・・*に関するコメント (・・*)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力判定のコメント ・・*の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定のコメント ・・*の証跡として保存して根拠にする。
    - C. コメント (・・*)の変更点を出力本文から切り離して出力判定のコメント ・・*の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定のコメント ・・*において選択記号 D を採用し、識別名は出力判定です。出力判定のコメント ・・*においてコメント (・・*)は説明欄の「コメント (・・*)の状態と出力メッセージを結び付ける出力判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力判定です。出力判定のコメント ・・*に関する記録は、コメント (・・*)の出力行と IEF236I を一緒に保存し、背景名は出力判定です。選択肢ごとの違いを示します。 A: 出力判定のコメント ・・*は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力判定ではありません。 B: 出力判定のコメント ・・*は別カテゴリの確認を流用しており、コメント (・・*)の根拠にならないため出力判定ではありません。 C: 出力判定のコメント ・・*は名称や説明のみに寄り、状態を示す出力本文が不足するため出力判定ではありません。 D: 出力判定のコメント ・・*は対象出力と項目説明を結び、根拠を残すので出力判定です。出力判定のコメント ・・*で記録するコメント (・・*)はz/OS JCL の確認記録に残す対象名であり、用語名は出力判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **コメント (・・*)**

    - 検証目的: 範囲記録のコメント ・・*について、コメント (//*)は、JCL DD 文の横断ルールで機能名、見出し、または確認対象として参照する項目です。DD の前後で説明コメントを // のあとに * で書く。実行にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020131の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲記録のコメント ・・*の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にコメント (・・*)を指定し、OSKB020131の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND コメント (・・*)
    CASE OSKB020131
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM コメント (・・*)
    CASE OSKB020131
    SOURCE z/OS JCL
    ```

    コメント (・・*)とOSKB020131が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020131を同じ出力で読み、範囲記録のコメント ・・*の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020131
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020131
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020131.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020131 STEP1 SYSUT1
    ```

    IEF236IとOSKB020131が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の コメント (・・*) と OSKB020131 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020131 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### 属性解決順序まとめ {#c17-i0254}
*分類: 横断ルール*  ・  難易度: 中級

新規割振り時の属性は (1) プログラム指定 / VSAM カタログ により (2) DD 文 (DCB= / SPACE= 等) により (3) DATACLAS により (4) システム既定の順で解決される。新規割振り時の属性は (1) プログラム指定 / VSAM カタログ → (2) DD 文 (DCB= / SPACE= 等) → (3) DATACLAS → (4) システム既定の順で解決される

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（1問）"
    **問題.** 条件判定の属性解決順序まとめに関係する属性解決順序まとめの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件判定として残す。 ✅
    - B. 属性解決順序まとめの名称と担当者名のみを残して条件判定の属性解決順序まとめの表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で条件判定の属性解決順序まとめを確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件判定の属性解決順序まとめの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定の属性解決順序まとめにおいて選択記号 A を採用し、識別名は条件判定です。条件判定の属性解決順序まとめにおいて属性解決順序まとめは説明欄の「属性解決順序まとめの用途をジョブデータ定義の表示で確認する条件判定項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は条件判定です。条件判定の属性解決順序まとめに関連して、z/OS JCL では属性解決順序まとめの表示属性と IEF236I を同じ証跡に残し、背景名は条件判定です。他の選択肢を確認します。 A: 条件判定の属性解決順序まとめは対象出力と項目説明を結び、根拠を残すので条件判定です。 B: 条件判定の属性解決順序まとめは名称や説明のみに寄り、状態を示す出力本文が不足するため条件判定ではありません。 C: 条件判定の属性解決順序まとめは別カテゴリの確認を流用しており、属性解決順序まとめの根拠にならないため条件判定ではありません。 D: 条件判定の属性解決順序まとめは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため条件判定ではありません。条件判定の属性解決順序まとめで使う属性解決順序まとめという用語は JCL DD 文で扱う確認対象であり、用語名は条件判定です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **属性解決順序まとめ**

    - 検証目的: 優先記録の属性解決順序まとめについて、新規割振り時の属性は (1) プログラム指定 / VSAM カタログ により (2) DD 文 (DCB= / SPACE= 等) により (3) DATACLAS によりに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020132の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先記録の属性解決順序まとめの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に属性解決順序まとめを指定し、OSKB020132の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 属性解決順序まとめ
    CASE OSKB020132
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 属性解決順序まとめ
    CASE OSKB020132
    SOURCE z/OS JCL
    ```

    属性解決順序まとめとOSKB020132が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020132を同じ出力で読み、優先記録の属性解決順序まとめの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020132
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020132
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020132.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020132 STEP1 SYSUT1
    ```

    IEF236IとOSKB020132が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の 属性解決順序まとめ と OSKB020132 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020132 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > 連結

### BLKSIZE 順序 (先頭最大) {#c17-i0255}
*分類: 連結*  ・  難易度: 中級

連結時は先頭 DD の BLKSIZE が最大である必要がある (古い OS では必須)。新しい z/OS は自動拡張するが原則として守る。「BLKSIZE 順序 (先頭最大)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 終端読解の順序 先頭最大に関係する BLKSIZE 順序 (先頭最大)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、終端読解の証跡として残す。 ✅
    - B. BLKSIZE 順序 (先頭最大)の名称と担当者名だけを残して終端読解の順序 先頭最大の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で終端読解の順序 先頭最大を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端読解の順序 先頭最大の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では BLKSIZE 順序 (先頭最大) は「BLKSIZE 順序 (先頭最大)の用途をジョブデータ定義の表示で確認する終端読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景ではz/OS JCL の BLKSIZE 順序 (先頭最大)と IEF236I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明だけに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では BLKSIZE 順序 (先頭最大)を JCL DD 文で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 上書追跡の順序 先頭最大でジョブデータ定義の運用確認を行います。BLKSIZE 順序 (先頭最大)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書追跡の順序 先頭最大を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書追跡の順序 先頭最大を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. BLKSIZE 順序 (先頭最大)の属性行を読まず上書追跡の順序 先頭最大の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡の順序 先頭最大において選択記号 C を採用し、識別名は上書追跡です。上書追跡の順序 先頭最大において BLKSIZE 順序 (先頭最大) は説明欄の「連結時は先頭 DD の BLKSIZE が最大である必要がある (古い OS では必須)。新しい z/OS は自動拡張するが原則として守る。」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の順序 先頭最大を受け取る担当者は、BLKSIZE 順序 (先頭最大)の表示結果と IEF236I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の順序 先頭最大は別カテゴリの確認を流用しており、BLKSIZE 順序 (先頭最大)の根拠にならないため上書追跡ではありません。 B: 上書追跡の順序 先頭最大は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の順序 先頭最大は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の順序 先頭最大は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の順序 先頭最大が示す BLKSIZE 順序 (先頭最大)は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **BLKSIZE 順序 (先頭最大)**

    - 検証目的: 変更照合の順序 先頭最大について、連結時は先頭 DD の BLKSIZE が最大である必要がある (古い OS では必須)。新しい z/OS は自動拡張するが原則として守る。「BLKSIZE 順序 (先頭最に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、変更照合の順序 先頭最大の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBLKSIZE 順序 (先頭最大)を指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BLKSIZE 順序 (先頭最大)
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BLKSIZE 順序 (先頭最大)
    CASE OSKB020040
    SOURCE z/OS JCL
    ```

    BLKSIZE 順序 (先頭最大)とOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020040を同じ出力で読み、変更照合の順序 先頭最大の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020040
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020040.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020040 STEP1 SYSUT1
    ```

    IEF236IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の BLKSIZE 順序 (先頭最大) と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DD 連結 (DDname 省略) {#c17-i0256}
*分類: 連結*  ・  難易度: 初級

DD カードを連続して書き、2 枚目以降の DDNAME を省略すると先頭 DD に連結される。論理 1 入力ファイル扱い

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 置換読解の連結 省略に関する DD 連結 (DDname 省略)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換読解の連結 省略の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換読解の連結 省略の証跡として保存して根拠にする。
    - C. DD 連結 (DDname 省略)の変更点を出力本文から切り離して置換読解の連結 省略の承認欄だけ残す。
    - D. IEF236I を含む表示を保存し、説明欄との差分を置換読解で確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では DD 連結 (DDname 省略) は「DD 連結 (DDname 省略)の状態と出力メッセージを結び付ける置換読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では DD 連結 (DDname 省略)の出力行と IEF236I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明だけに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では DD 連結 (DDname 省略)をz/OS JCL の確認記録に残し、対象名は置換読解対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 探索追跡の連結 省略で DD 連結 (DDname 省略)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DD 連結 (DDname 省略)の出力を取らず探索追跡の連結 省略の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 ✅
    - C. ST OSKBDD を省略して探索追跡の連結 省略の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の連結 省略へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 探索追跡の連結 省略において選択記号 B を採用し、識別名は探索追跡です。探索追跡の連結 省略において DD 連結 (DDname 省略) は説明欄の「DD カードを連続して書き、2 枚目以降の DDNAME を省略すると先頭 DD に連結される。論理 1 入力ファイル扱い」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の連結 省略の証跡を読む担当者は、DD 連結 (DDname 省略)の属性行と IEF236I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の連結 省略は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の連結 省略は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の連結 省略は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の連結 省略は別カテゴリの確認を流用しており、DD 連結 (DDname 省略)の根拠にならないため探索追跡ではありません。探索追跡の連結 省略に出る DD 連結 (DDname 省略)は JCL DD 文の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DD 連結 (DDname 省略)**

    - 検証目的: 監査照合の連結 省略について、DD カードを連続して書き、2 枚目以降の DDNAME を省略すると先頭 DD に連結される。論理 1 入力ファイル扱いに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、監査照合の連結 省略の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDD 連結 (DDname 省略)を指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DD 連結 (DDname 省略)
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DD 連結 (DDname 省略)
    CASE OSKB020039
    SOURCE z/OS JCL
    ```

    DD 連結 (DDname 省略)とOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020039を同じ出力で読み、監査照合の連結 省略の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020039
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020039.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020039 STEP1 SYSUT1
    ```

    IEF236IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DD 連結 (DDname 省略) と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### DSORG 一致 {#c17-i0257}
*分類: 連結*  ・  難易度: 中級

DSORG 一致は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 上書読解の一致でジョブデータ定義の運用確認を行います。DSORG 一致の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書読解の一致を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書読解の一致を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書読解の根拠にする。 ✅
    - D. DSORG 一致の属性行を読まず上書読解の一致の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では DSORG 一致 は「z/OS JCL で DSORG 一致の扱いを記録する上書読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では DSORG 一致の表示結果と IEF236I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明だけに寄り、判定名は上書読解不足です。上書読解資料では DSORG 一致の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 条件追跡の一致に関係する DSORG 一致の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. DSORG 一致の名称と担当者名のみを残して条件追跡の一致の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で条件追跡の一致を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件追跡の一致の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の一致において選択記号 A を採用し、識別名は条件追跡です。条件追跡の一致において DSORG 一致 は説明欄の「DSORG 一致の用途をジョブデータ定義の表示で確認する条件追跡項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の一致に関連して、z/OS JCL では DSORG 一致の表示属性と IEF236I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の一致は対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の一致は名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の一致は別カテゴリの確認を流用しており、DSORG 一致の根拠にならないため条件追跡ではありません。 D: 条件追跡の一致は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため条件追跡ではありません。条件追跡の一致で使う DSORG 一致という用語は JCL DD 文で扱う確認対象であり、用語名は条件追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **DSORG 一致**

    - 検証目的: 展開追跡の一致について、DSORG 一致は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認しまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開追跡の一致の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSORG 一致を指定し、OSKB020042の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSORG 一致
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSORG 一致
    CASE OSKB020042
    SOURCE z/OS JCL
    ```

    DSORG 一致とOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020042を同じ出力で読み、展開追跡の一致の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020042
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020042.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020042 STEP1 SYSUT1
    ```

    IEF236IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSORG 一致 と OSKB020042 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PDS 連結 (Library 連結) {#c17-i0258}
*分類: 連結*  ・  難易度: 中級

PO データセット同士を連結し、論理的に 1 つのライブラリとして扱う (例: STEPLIB / SYSLIB)。メンバー検索順は連結順。「PDS 連結 (Library 連結)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 出力読解の連結 連結に関する PDS 連結 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力読解の連結 連結の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力読解の連結 連結の証跡として保存して根拠にする。
    - C. PDS 連結 属性の変更点を出力本文から切り離して出力読解の連結 連結の承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、出力読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では PDS 連結 属性 は「PDS 連結 属性の状態と出力メッセージを結び付ける出力読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では PDS 連結 属性の出力行と IEF236I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明だけに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では PDS 連結 属性をz/OS JCL の確認記録に残し、対象名は出力読解対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 区切追跡の連結 連結で PDS 連結 (Library 連結)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PDS 連結 (Library 連結)の出力を取らず区切追跡の連結 連結の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 ✅
    - C. ST OSKBDD を省略して区切追跡の連結 連結の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の連結 連結へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡の連結 連結において選択記号 B を採用し、識別名は区切追跡です。区切追跡の連結 連結において PDS 連結 (Library 連結) は説明欄の「PO データセット同士を連結し、論理的に 1 つのライブラリとして扱う (例: STEPLIB / SYSLIB)。メンバー検索順は連結順。」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の連結 連結の証跡を読む担当者は、PDS 連結 (Library 連結)の属性行と IEF236I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の連結 連結は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の連結 連結は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の連結 連結は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の連結 連結は別カテゴリの確認を流用しており、PDS 連結 (Library 連結)の根拠にならないため区切追跡ではありません。区切追跡の連結 連結に出る PDS 連結 (Library 連結)は JCL DD 文の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PDS 連結 (Library 連結)**

    - 検証目的: 呼出追跡の連結 連結について、PO データセット同士を連結し、論理的に 1 つのライブラリとして扱う (例: STEPLIB / SYSLIB)。メンバー検索順は連結順。「PDS 連結 (Libraryに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出追跡の連結 連結の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPDS 連結 (Library 連結を指定し、OSKB020043の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PDS 連結 (Library 連結
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PDS 連結 (Library 連結
    CASE OSKB020043
    SOURCE z/OS JCL
    ```

    PDS 連結 (Library 連結とOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020043を同じ出力で読み、呼出追跡の連結 連結の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020043
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020043.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020043 STEP1 SYSUT1
    ```

    IEF236IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PDS 連結 (Library 連結 と OSKB020043 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### RECFM 一致 {#c17-i0259}
*分類: 連結*  ・  難易度: 中級

連結対象は同じ RECFM (固定 or 可変) であることが原則。混在は不可。「RECFM 一致」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 探索読解の一致で RECFM 一致の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RECFM 一致の出力を取らず探索読解の一致の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、探索読解の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して探索読解の一致の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索読解の一致へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では RECFM 一致 は「探索読解の一致に関係する定義値と表示行を照合する探索読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では RECFM 一致の属性行と IEF236I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明だけに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では RECFM 一致を JCL DD 文の運用手順で確認し、初出名は探索読解初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 出力追跡の一致に関する RECFM 一致の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力追跡の一致の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の一致の証跡として保存して根拠にする。
    - C. RECFM 一致の変更点を出力本文から切り離して出力追跡の一致の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡の一致において選択記号 D を採用し、識別名は出力追跡です。出力追跡の一致において RECFM 一致 は説明欄の「連結対象は同じ RECFM (固定 or 可変) であることが原則。混在は不可。「RECFM 一致」は割り当て結果を調べるとき、DISP、U」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の一致に関する記録は、RECFM 一致の出力行と IEF236I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の一致は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の一致は別カテゴリの確認を流用しており、RECFM 一致の根拠にならないため出力追跡ではありません。 C: 出力追跡の一致は名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の一致は対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の一致で記録する RECFM 一致はz/OS JCL の確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **RECFM 一致**

    - 検証目的: 比較照合の一致について、連結対象は同じ RECFM (固定 or 可変) であることが原則。混在は不可。「RECFM 一致」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB などに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030034の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、比較照合の一致の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECFM 一致を指定し、OSKB030034の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECFM 一致
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECFM 一致
    CASE OSKB030034
    SOURCE z/OS JCL
    ```

    RECFM 一致とOSKB030034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030034を同じ出力で読み、比較照合の一致の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030034
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030034.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030034 STEP1 SYSUT1
    ```

    IEF236IとOSKB030034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の RECFM 一致 と OSKB030034 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RECFM 一致**

    - 検証目的: 構文追跡の一致について、連結対象は同じ RECFM (固定 or 可変) であることが原則。混在は不可。「RECFM 一致」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB などに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、構文追跡の一致の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にRECFM 一致を指定し、OSKB020041の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND RECFM 一致
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM RECFM 一致
    CASE OSKB020041
    SOURCE z/OS JCL
    ```

    RECFM 一致とOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020041を同じ出力で読み、構文追跡の一致の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020041
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020041.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020041 STEP1 SYSUT1
    ```

    IEF236IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の RECFM 一致 と OSKB020041 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### SYSOUT 連結 {#c17-i0260}
*分類: 連結*  ・  難易度: 中級

SYSOUT も連結可能。複数 DD を 1 つの SPOOL データセットに見せる。「SYSOUT 連結」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 条件読解の連結に関係する SYSOUT 連結の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD で得た表示本文を使い、条件読解の採否を説明欄に結び付ける。 ✅
    - B. SYSOUT 連結の名称と担当者名だけを残して条件読解の連結の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で条件読解の連結を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件読解の連結の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では SYSOUT 連結 は「SYSOUT 連結の用途をジョブデータ定義の表示で確認する条件読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景ではz/OS JCL の SYSOUT 連結と IEF236I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明だけに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では SYSOUT 連結を JCL DD 文で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 構文確認の連結に関係する SYSOUT 連結の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文確認として残す。 ✅
    - B. SYSOUT 連結の名称と担当者名のみを残して構文確認の連結の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で構文確認の連結を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文確認の連結の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認の連結において選択記号 A を採用し、識別名は構文確認です。構文確認の連結において SYSOUT 連結 は説明欄の「SYSOUT 連結の用途をジョブデータ定義の表示で確認する構文確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の連結に関連して、z/OS JCL では SYSOUT 連結の表示属性と IEF236I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の連結は対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の連結は名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の連結は別カテゴリの確認を流用しており、SYSOUT 連結の根拠にならないため構文確認ではありません。 D: 構文確認の連結は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため構文確認ではありません。構文確認の連結で使う SYSOUT 連結という用語は JCL DD 文で扱う確認対象であり、用語名は構文確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **SYSOUT 連結**

    - 検証目的: 置換追跡の連結について、SYSOUT も連結可能。複数 DD を 1 つの SPOOL データセットに見せる。「SYSOUT 連結」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換追跡の連結の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSYSOUT 連結を指定し、OSKB020044の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SYSOUT 連結
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SYSOUT 連結
    CASE OSKB020044
    SOURCE z/OS JCL
    ```

    SYSOUT 連結とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020044を同じ出力で読み、置換追跡の連結の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020044
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020044.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020044 STEP1 SYSUT1
    ```

    IEF236IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SYSOUT 連結 と OSKB020044 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### インストリーム連結 {#c17-i0261}
*分類: 連結*  ・  難易度: 中級

インストリーム連結は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 区切読解のインストリーム連結でインストリーム連結の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. インストリーム連結の出力を取らず区切読解のインストリーム連結の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切読解として引き継ぐ。 ✅
    - C. ST OSKBDD を省略して区切読解のインストリーム連結の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切読解のインストリーム連結へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠ではインストリーム連結は「区切読解のインストリーム連結に関係する定義値と表示行を照合する区切読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡ではインストリーム連結の属性行と IEF236I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明だけに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出ではインストリーム連結を JCL DD 文の運用手順で確認し、初出名は区切読解初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 展開確認のインストリーム連結でインストリーム連結の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. インストリーム連結の出力を取らず展開確認のインストリーム連結の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開確認の確認結果にする。 ✅
    - C. ST OSKBDD を省略して展開確認のインストリーム連結の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のインストリーム連結へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認のインストリーム連結において選択記号 B を採用し、識別名は展開確認です。展開確認のインストリーム連結においてインストリーム連結は説明欄の「展開確認のインストリーム連結に関係する定義値と表示行を照合する展開確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認のインストリーム連結の証跡を読む担当者は、インストリーム連結の属性行と IEF236I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認のインストリーム連結は名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認のインストリーム連結は対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認のインストリーム連結は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため展開確認ではありません。 D: 展開確認のインストリーム連結は別カテゴリの確認を流用しており、インストリーム連結の根拠にならないため展開確認ではありません。展開確認のインストリーム連結に出るインストリーム連結は JCL DD 文の運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **インストリーム連結**

    - 検証目的: 終端追跡のインストリーム連結について、インストリーム連結は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認しに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端追跡のインストリーム連結の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にインストリーム連結を指定し、OSKB020045の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND インストリーム連結
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM インストリーム連結
    CASE OSKB020045
    SOURCE z/OS JCL
    ```

    インストリーム連結とOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020045を同じ出力で読み、終端追跡のインストリーム連結の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020045
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020045.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020045 STEP1 SYSUT1
    ```

    IEF236IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の インストリーム連結 と OSKB020045 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### 連結深さ上限 {#c17-i0262}
*分類: 連結*  ・  難易度: 中級

連結深さ上限は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。通常は 16 (順次 / PS) or 255 (PDS 等)。装置 / DSORG ごとに上限がある。「連結深さ上限」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 範囲読解の連結深さ上限でジョブデータ定義の運用確認を行います。連結深さ上限の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲読解の連結深さ上限を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲読解の連結深さ上限を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲読解の確認にする。 ✅
    - D. 連結深さ上限の属性行を読まず範囲読解の連結深さ上限の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では連結深さ上限は「z/OS JCL で連結深さ上限の扱いを記録する範囲読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では連結深さ上限の表示結果と IEF236I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明だけに寄り、判定名は範囲読解不足です。範囲読解資料では連結深さ上限の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 呼出確認の連結深さ上限でジョブデータ定義の運用確認を行います。連結深さ上限の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出確認の連結深さ上限を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出確認の連結深さ上限を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 ✅
    - D. 連結深さ上限の属性行を読まず呼出確認の連結深さ上限の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認の連結深さ上限において選択記号 C を採用し、識別名は呼出確認です。呼出確認の連結深さ上限において連結深さ上限は説明欄の「z/OS JCL で連結深さ上限の扱いを記録する呼出確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の連結深さ上限を受け取る担当者は、連結深さ上限の表示結果と IEF236I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の連結深さ上限は別カテゴリの確認を流用しており、連結深さ上限の根拠にならないため呼出確認ではありません。 B: 呼出確認の連結深さ上限は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の連結深さ上限は対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の連結深さ上限は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の連結深さ上限が示す連結深さ上限は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **連結深さ上限**

    - 検証目的: 順序照合の連結深さ上限について、連結深さ上限は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。通常は 16 (順次 / PS) or 255 (PDS 等)。装置 / DSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030035の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序照合の連結深さ上限の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に連結深さ上限を指定し、OSKB030035の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 連結深さ上限
    CASE OSKB030035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 連結深さ上限
    CASE OSKB030035
    SOURCE z/OS JCL
    ```

    連結深さ上限とOSKB030035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030035を同じ出力で読み、順序照合の連結深さ上限の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030035
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030035
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030035.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030035 STEP1 SYSUT1
    ```

    IEF236IとOSKB030035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の 連結深さ上限 と OSKB030035 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **連結深さ上限**

    - 検証目的: 探索追跡の連結深さ上限について、連結深さ上限は、JCL DD 文の連結で機能名、見出し、または確認対象として参照する項目です。通常は 16 (順次 / PS) or 255 (PDS 等)。装置 / DSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索追跡の連結深さ上限の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に連結深さ上限を指定し、OSKB020046の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 連結深さ上限
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 連結深さ上限
    CASE OSKB020046
    SOURCE z/OS JCL
    ```

    連結深さ上限とOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020046を同じ出力で読み、探索追跡の連結深さ上限の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020046
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020046.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020046 STEP1 SYSUT1
    ```

    IEF236IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の 連結深さ上限 と OSKB020046 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## その他

### その他（特定項目に紐づかないQA・手順） {#c17-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（8問）"
    **問題.** 復旧確認の引用 などで DSN 引用 ('など')の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. DSN 引用 ('など')の出力を取らず復旧確認の引用 などの説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧確認の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して復旧確認の引用 などの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧確認の引用 などへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では DSN 引用 ('など') は「復旧確認の引用 などに関係する定義値と表示行を照合する復旧確認項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では DSN 引用 ('など')の属性行と IEF236I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明だけに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では DSN 引用 ('など')を JCL DD 文の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 上書検査の完全位置取り例でジョブデータ定義の運用確認を行います。VOL 属性の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書検査の完全位置取り例を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書検査の完全位置取り例を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書検査の根拠を固定する。 ✅
    - D. VOL 属性の属性行を読まず上書検査の完全位置取り例の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では VOL 属性 は「z/OS JCL で VOL 属性の扱いを記録する上書検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では VOL 属性の表示結果と IEF236I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明だけに寄り、判定名は上書検査不足です。上書検査資料では VOL 属性の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 出力検査のなどに関する SPACE=(TRK,など)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力検査のなどの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力検査のなどの証跡として保存して根拠にする。
    - C. SPACE=(TRK,など)の変更点を出力本文から切り離して出力検査のなどの承認欄だけ残す。
    - D. IEF236I を含む表示を保存し、説明欄との差分を出力検査で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では SPACE=(TRK,など) は「SPACE=(TRK,など)の状態と出力メッセージを結び付ける出力検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では SPACE=(TRK,など)の出力行と IEF236I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明だけに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では SPACE=(TRK,など)をz/OS JCL の確認記録に残し、対象名は出力検査対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 条件検査のなどに関係する SPACE=(CYL,など)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、条件検査の証跡として残す。 ✅
    - B. SPACE=(CYL,など)の名称と担当者名だけを残して条件検査のなどの表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で条件検査のなどを確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件検査のなどの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では SPACE=(CYL,など) は「SPACE=(CYL,など)の用途をジョブデータ定義の表示で確認する条件検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景ではz/OS JCL の SPACE=(CYL,など)と IEF236I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明だけに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では SPACE=(CYL,など)を JCL DD 文で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 区切検査のなどで SPACE=(BLK,など)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SPACE=(BLK,など)の出力を取らず区切検査のなどの説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、区切検査の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して区切検査のなどの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切検査のなどへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では SPACE=(BLK,など) は「区切検査のなどに関係する定義値と表示行を照合する区切検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では SPACE=(BLK,など)の属性行と IEF236I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明だけに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では SPACE=(BLK,など)を JCL DD 文の運用手順で確認し、初出名は区切検査初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 範囲検査のなどでジョブデータ定義の運用確認を行います。SPACE 属性の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲検査のなどを確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲検査のなどを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲検査の根拠にする。 ✅
    - D. SPACE 属性の属性行を読まず範囲検査のなどの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では SPACE 属性 は「z/OS JCL で SPACE 属性の扱いを記録する範囲検査項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では SPACE 属性の表示結果と IEF236I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明だけに寄り、判定名は範囲検査不足です。範囲検査資料では SPACE 属性の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 呼出分離のなどでジョブデータ定義の運用確認を行います。COPIES= 属性の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出分離のなどを確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出分離のなどを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出分離の根拠にする。 ✅
    - D. COPIES= 属性の属性行を読まず呼出分離のなどの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では COPIES= 属性 は「z/OS JCL で COPIES= 属性の扱いを記録する呼出分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では COPIES= 属性の表示結果と IEF236I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明だけに寄り、判定名は呼出分離不足です。呼出分離資料では COPIES= 属性の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 優先検分のジョブデータ定義に関する SUBSYS= 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先検分のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先検分のジョブデータ定義の証跡として保存して根拠にする。
    - C. SUBSYS= 属性の変更点を出力本文から切り離して優先検分のジョブデータ定義の承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、優先検分の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では SUBSYS= 属性 は「SUBSYS= 属性の状態と出力メッセージを結び付ける優先検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では SUBSYS= 属性の出力行と IEF236I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明だけに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では SUBSYS= 属性をz/OS JCL の確認記録に残し、対象名は優先検分対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（13件）"
    **SPACE=(reclen,など)**

    - 検証目的: 順序確認のなどについて、JCL DD 文の SPACE-単位では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。SPACE-単位は、JCL DD 文の運用で指定値、構文上のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030015の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、順序確認のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSPACE=(reclen,など)を指定し、OSKB030015の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SPACE=(reclen,など)
    CASE OSKB030015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SPACE=(reclen,など)
    CASE OSKB030015
    SOURCE z/OS JCL
    ```

    SPACE=(reclen,など)とOSKB030015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030015を同じ出力で読み、順序確認のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030015
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030015
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030015.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030015 STEP1 SYSUT1
    ```

    IEF236IとOSKB030015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SPACE=(reclen,など) と OSKB030015 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **AMP=('SYNAD= など')**

    - 検証目的: 探索追跡のなどについて、I/O エラー時のユーザ SYNAD ルーチン指定。「AMP=('SYNAD= など')」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定とのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030046の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索追跡のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にAMP=('SYNAD= など')を指定し、OSKB030046の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND AMP=('SYNAD= など')
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM AMP=('SYNAD= など')
    CASE OSKB030046
    SOURCE z/OS JCL
    ```

    AMP=('SYNAD= など')とOSKB030046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030046を同じ出力で読み、探索追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030046
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030046.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030046 STEP1 SYSUT1
    ```

    IEF236IとOSKB030046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の AMP=('SYNAD= など') と OSKB030046 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **後方参照 *.procstepname.stepname.ddnam**

    - 検証目的: 呼出確認の後方参照 *について、JCL DD 文の DSN では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。DSN は、JCL DD 文の運用で指定値、構文上の位置、反映後の出力をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出確認の後方参照 *の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に後方参照 *.procstepnamを指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 後方参照 *.procstepnam
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 後方参照 *.procstepnam
    CASE OSKB010003
    SOURCE z/OS JCL
    ```

    後方参照 *.procstepnamとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010003を同じ出力で読み、呼出確認の後方参照 *の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010003
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010003.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010003 STEP1 SYSUT1
    ```

    IEF236IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の 後方参照 *.procstepnam と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **DSN 引用 ('など')**

    - 検証目的: 記録確認の引用 などについて、アポストロフィで囲うと修飾規則の例外を含む DSN を指定可能。通常はカタログ標準命名規則に従うため使わない。「DSN 引用 ('など')」を読むと、プログラムが参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録確認の引用 などの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にDSN 引用 ('など')を指定し、OSKB010013の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND DSN 引用 ('など')
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM DSN 引用 ('など')
    CASE OSKB010013
    SOURCE z/OS JCL
    ```

    DSN 引用 ('など')とOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010013を同じ出力で読み、記録確認の引用 などの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010013
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010013.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010013 STEP1 SYSUT1
    ```

    IEF236IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の DSN 引用 ('など') と OSKB010013 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **VOL 完全位置取り例 VOL=(PRIVATE,RETAIN,1,**

    - 検証目的: 展開検査の完全位置取り例について、VOL 完全位置取り例 VOL=(PRIVATE,RETAIN,1,5,SER= など)は、JCL DD 文の VOL で機能名、見出し、または確認対象として参照する項目です。位に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開検査の完全位置取り例の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にVOL 完全位置取り例 VOL=(Pを指定し、OSKB010062の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND VOL 完全位置取り例 VOL=(P
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM VOL 完全位置取り例 VOL=(P
    CASE OSKB010062
    SOURCE z/OS JCL
    ```

    VOL 完全位置取り例 VOL=(PとOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010062を同じ出力で読み、展開検査の完全位置取り例の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010062
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010062.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010062 STEP1 SYSUT1
    ```

    IEF236IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の VOL 完全位置取り例 VOL=(P と OSKB010062 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SPACE=(TRK,など)**

    - 検証目的: 呼出検査のなどについて、JCL DD 文の SPACE-単位では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。SPACE-単位は、JCL DD 文の運用で指定値、構文上のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSPACE=(TRK,など)を指定し、OSKB010063の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SPACE=(TRK,など)
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SPACE=(TRK,など)
    CASE OSKB010063
    SOURCE z/OS JCL
    ```

    SPACE=(TRK,など)とOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010063を同じ出力で読み、呼出検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010063
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010063.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010063 STEP1 SYSUT1
    ```

    IEF236IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SPACE=(TRK,など) と OSKB010063 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SPACE=(CYL,など)**

    - 検証目的: 置換検査のなどについて、JCL DD 文の SPACE-単位では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。SPACE-単位は、JCL DD 文の運用で指定値、構文上のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSPACE=(CYL,など)を指定し、OSKB010064の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SPACE=(CYL,など)
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SPACE=(CYL,など)
    CASE OSKB010064
    SOURCE z/OS JCL
    ```

    SPACE=(CYL,など)とOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010064を同じ出力で読み、置換検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010064
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010064.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010064 STEP1 SYSUT1
    ```

    IEF236IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SPACE=(CYL,など) と OSKB010064 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SPACE=(BLK,など)**

    - 検証目的: 終端検査のなどについて、JCL DD 文の SPACE-単位では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。SPACE-単位は、JCL DD 文の運用で指定値、構文上のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSPACE=(BLK,など)を指定し、OSKB010065の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SPACE=(BLK,など)
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SPACE=(BLK,など)
    CASE OSKB010065
    SOURCE z/OS JCL
    ```

    SPACE=(BLK,など)とOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010065を同じ出力で読み、終端検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010065
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010065.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010065 STEP1 SYSUT1
    ```

    IEF236IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SPACE=(BLK,など) と OSKB010065 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SPACE=(reclen,など)**

    - 検証目的: 探索検査のなどについて、JCL DD 文の SPACE-単位では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。SPACE-単位は、JCL DD 文の運用で指定値、構文上のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSPACE=(reclen,など)を指定し、OSKB010066の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SPACE=(reclen,など)
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SPACE=(reclen,など)
    CASE OSKB010066
    SOURCE z/OS JCL
    ```

    SPACE=(reclen,など)とOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010066を同じ出力で読み、探索検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010066
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010066.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010066 STEP1 SYSUT1
    ```

    IEF236IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SPACE=(reclen,など) と OSKB010066 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COPIES=(N,(g1,g2,など))**

    - 検証目的: 復旧確認のなどについて、JCL DD 文の SYSOUT-付属では、ジョブ制御文の構文、指定値、展開後の JESJCL を対応付けて確認します。SYSOUT-付属は、JCL DD 文の運用で指定値、構文に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧確認のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCOPIES=(N,(g1,g2,なを指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND COPIES=(N,(g1,g2,な
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM COPIES=(N,(g1,g2,な
    CASE OSKB020018
    SOURCE z/OS JCL
    ```

    COPIES=(N,(g1,g2,なとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020018を同じ出力で読み、復旧確認のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020018
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020018.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020018 STEP1 SYSUT1
    ```

    IEF236IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の COPIES=(N,(g1,g2,な と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SUBSYS=(name,parm1,parm2,など)**

    - 検証目的: 上書検査のジョブデータ定義について、SUBSYS=(name,parm1,parm2,など)は、JCL DD 文の SUBSYS で構成値やオプションの意味を確認する項目です。サブシステムへ追加パラメータを渡す形に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、上書検査のジョブデータ定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSUBSYS=(name,parm1を指定し、OSKB020067の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SUBSYS=(name,parm1
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SUBSYS=(name,parm1
    CASE OSKB020067
    SOURCE z/OS JCL
    ```

    SUBSYS=(name,parm1とOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020067を同じ出力で読み、上書検査のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020067
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020067.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020067 STEP1 SYSUT1
    ```

    IEF236IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SUBSYS=(name,parm1 と OSKB020067 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **AMP=('RECFM= など')**

    - 検証目的: 復旧判定のなどについて、ESDS で他形式互換と見せかけるための RECFM オーバーライド (限定用途)。「AMP=('RECFM= など')」は割り当て結果を調べるとき、DISP、UNIT、SPに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020098の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧判定のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にAMP=('RECFM= など')を指定し、OSKB020098の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND AMP=('RECFM= など')
    CASE OSKB020098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM AMP=('RECFM= など')
    CASE OSKB020098
    SOURCE z/OS JCL
    ```

    AMP=('RECFM= など')とOSKB020098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020098を同じ出力で読み、復旧判定のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020098
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020098
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020098.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020098 STEP1 SYSUT1
    ```

    IEF236IとOSKB020098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の AMP=('RECFM= など') と OSKB020098 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **AMP=('SYNAD= など')**

    - 検証目的: 構文整理のなどについて、I/O エラー時のユーザ SYNAD ルーチン指定。「AMP=('SYNAD= など')」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定とのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、構文整理のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBDD
    ```

    COMMAND INPUTにST OSKBDDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にAMP=('SYNAD= など')を指定し、OSKB020101の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND AMP=('SYNAD= など')
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM AMP=('SYNAD= など')
    CASE OSKB020101
    SOURCE z/OS JCL
    ```

    AMP=('SYNAD= など')とOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020101を同じ出力で読み、構文整理のなどの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020101
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020101.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020101 STEP1 SYSUT1
    ```

    IEF236IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の AMP=('SYNAD= など') と OSKB020101 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

