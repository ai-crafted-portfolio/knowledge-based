---
search:
  exclude: true
---

# JCL DD 文 — 詳細 (4/6)

[← JCL DD 文 の概要へ戻る](index.md)


## JCL DD 文 > SYSOUT-付属

### FREE=CLOSE {#c17-i0156}
*分類: SYSOUT-付属*  ・  難易度: 中級

FREE=CLOSEは、JCL DD 文のSYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。CLOSE 時点で SPOOL に出力を解放、ジョブ終了を待たずに後段 (プリンタ) が処理可能。「FREE=CLOSE」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 終端分離の付属に関係する FREE=CLOSE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD で得た表示本文を使い、終端分離の採否を説明欄に結び付ける。 ✅
    - B. FREE=CLOSE の名称と担当者名だけを残して終端分離の付属の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で終端分離の付属を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端分離の付属の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では FREE=CLOSE は「FREE=CLOSE の用途をジョブデータ定義の表示で確認する終端分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景ではz/OS JCL の FREE=CLOSE と IEF236I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明だけに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では FREE=CLOSE を JCL DD 文で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 上書照合の付属でジョブデータ定義の運用確認を行います。FREE=CLOSE の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書照合の付属を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書照合の付属を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書照合の記録として扱う。 ✅
    - D. FREE=CLOSE の属性行を読まず上書照合の付属の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合の付属において選択記号 C を採用し、識別名は上書照合です。上書照合の付属において FREE=CLOSE は説明欄の「z/OS JCL で FREE=CLOSE の扱いを記録する上書照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の付属を受け取る担当者は、FREE=CLOSE の表示結果と IEF236I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の付属は別カテゴリの確認を流用しており、FREE=CLOSE の根拠にならないため上書照合ではありません。 B: 上書照合の付属は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書照合ではありません。 C: 上書照合の付属は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の付属は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の付属が示す FREE=CLOSE は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FREE=CLOSE**

    - 検証目的: 変更確認の付属について、FREE=CLOSE は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。CLOSE 時点で SPOOL に出力を解放、ジョブ終了に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、変更確認の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にFREE=CLOSEを指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FREE=CLOSE
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FREE=CLOSE
    CASE OSKB020020
    SOURCE z/OS JCL
    ```

    FREE=CLOSEとOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020020を同じ出力で読み、変更確認の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020020
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020020.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020020 STEP1 SYSUT1
    ```

    IEF236IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FREE=CLOSE と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FREE=END {#c17-i0157}
*分類: SYSOUT-付属*  ・  難易度: 中級

FREE=ENDは、JCL DD 文のSYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 探索分離の付属で FREE=END の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FREE=END の出力を取らず探索分離の付属の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索分離として引き継ぐ。 ✅
    - C. ST OSKBDD を省略して探索分離の付属の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索分離の付属へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では FREE=END は「探索分離の付属に関係する定義値と表示行を照合する探索分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では FREE=END の属性行と IEF236I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明だけに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では FREE=END を JCL DD 文の運用手順で確認し、初出名は探索分離初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 出力照合の付属に関する FREE=END の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力照合の付属の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の付属の証跡として保存して根拠にする。
    - C. FREE=END の変更点を出力本文から切り離して出力照合の付属の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合の付属において選択記号 D を採用し、識別名は出力照合です。出力照合の付属において FREE=END は説明欄の「FREE=END の状態と出力メッセージを結び付ける出力照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の付属に関する記録は、FREE=END の出力行と IEF236I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の付属は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力照合ではありません。 B: 出力照合の付属は別カテゴリの確認を流用しており、FREE=END の根拠にならないため出力照合ではありません。 C: 出力照合の付属は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の付属は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の付属で記録する FREE=END はz/OS JCL の確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **FREE=END**

    - 検証目的: 区切照合の付属について、FREE=END は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切照合の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にFREE=ENDを指定し、OSKB030030の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FREE=END
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FREE=END
    CASE OSKB030030
    SOURCE z/OS JCL
    ```

    FREE=ENDとOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030030を同じ出力で読み、区切照合の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030030
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030030.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030030 STEP1 SYSUT1
    ```

    IEF236IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FREE=END と OSKB030030 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **FREE=END**

    - 検証目的: 構文照合の付属について、FREE=END は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、構文照合の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にFREE=ENDを指定し、OSKB020021の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FREE=END
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FREE=END
    CASE OSKB020021
    SOURCE z/OS JCL
    ```

    FREE=ENDとOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020021を同じ出力で読み、構文照合の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020021
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020021.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020021 STEP1 SYSUT1
    ```

    IEF236IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FREE=END と OSKB020021 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### HOLD=NO {#c17-i0158}
*分類: SYSOUT-付属*  ・  難易度: 中級

HOLD=NOは、JCL DD 文のSYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 条件分離の付属に関係する HOLD=NO の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件分離で再確認できる形にする。 ✅
    - B. HOLD=NO の名称と担当者名だけを残して条件分離の付属の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で条件分離の付属を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件分離の付属の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では HOLD=NO は「HOLD=NO の用途をジョブデータ定義の表示で確認する条件分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景ではz/OS JCL の HOLD=NO と IEF236I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明だけに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では HOLD=NO を JCL DD 文で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 範囲照合の付属でジョブデータ定義の運用確認を行います。HOLD=NO の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲照合の付属を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲照合の付属を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. HOLD=NO の属性行を読まず範囲照合の付属の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合の付属において選択記号 C を採用し、識別名は範囲照合です。範囲照合の付属において HOLD=NO は説明欄の「z/OS JCL で HOLD=NO の扱いを記録する範囲照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の付属を受け取る担当者は、HOLD=NO の表示結果と IEF236I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の付属は別カテゴリの確認を流用しており、HOLD=NO の根拠にならないため範囲照合ではありません。 B: 範囲照合の付属は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の付属は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の付属は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の付属が示す HOLD=NO は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **HOLD=NO**

    - 検証目的: 置換照合の付属について、HOLD=NO は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換照合の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にHOLD=NOを指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND HOLD=NO
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM HOLD=NO
    CASE OSKB020024
    SOURCE z/OS JCL
    ```

    HOLD=NOとOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020024を同じ出力で読み、置換照合の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020024
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020024.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020024 STEP1 SYSUT1
    ```

    IEF236IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の HOLD=NO と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### HOLD=YES {#c17-i0159}
*分類: SYSOUT-付属*  ・  難易度: 中級

HOLD=YESは、JCL DD 文のSYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。SPOOL に出力を保留状態で残す。オペレータ解除まで印刷されない。「HOLD=YES」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 出力分離の付属に関する HOLD=YES の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力分離の付属の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力分離の付属の証跡として保存して根拠にする。
    - C. HOLD=YES の変更点を出力本文から切り離して出力分離の付属の承認欄だけ残す。
    - D. z/OS JCL の表示形式に沿って根拠行を採り、出力分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では HOLD=YES は「HOLD=YES の状態と出力メッセージを結び付ける出力分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では HOLD=YES の出力行と IEF236I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明だけに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では HOLD=YES をz/OS JCL の確認記録に残し、対象名は出力分離対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 区切照合の付属で HOLD=YES の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. HOLD=YES の出力を取らず区切照合の付属の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して区切照合の付属の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の付属へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合の付属において選択記号 B を採用し、識別名は区切照合です。区切照合の付属において HOLD=YES は説明欄の「区切照合の付属に関係する定義値と表示行を照合する区切照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の付属の証跡を読む担当者は、HOLD=YES の属性行と IEF236I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の付属は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の付属は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の付属は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため区切照合ではありません。 D: 区切照合の付属は別カテゴリの確認を流用しており、HOLD=YES の根拠にならないため区切照合ではありません。区切照合の付属に出る HOLD=YES は JCL DD 文の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **HOLD=YES**

    - 検証目的: 呼出照合の付属について、HOLD=YES は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。SPOOL に出力を保留状態で残す。オペレータ解除まで印刷さに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出照合の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にHOLD=YESを指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND HOLD=YES
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM HOLD=YES
    CASE OSKB020023
    SOURCE z/OS JCL
    ```

    HOLD=YESとOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020023を同じ出力で読み、呼出照合の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020023
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020023.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020023 STEP1 SYSUT1
    ```

    IEF236IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の HOLD=YES と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### OUTLIM=n {#c17-i0160}
*分類: SYSOUT-付属*  ・  難易度: 中級

OUTLIM=nは、JCL DD 文のSYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。SYSOUT データセットへの最大レコード数を制限。暴走時の SPOOL 爆食防止。「OUTLIM=n」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 置換分離の付属に関する OUTLIM=nの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換分離の付属の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換分離の付属の証跡として保存して根拠にする。
    - C. OUTLIM=nの変更点を出力本文から切り離して置換分離の付属の承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、置換分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では OUTLIM=n は「OUTLIM=nの状態と出力メッセージを結び付ける置換分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では OUTLIM=nの出力行と IEF236I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明だけに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では OUTLIM=nをz/OS JCL の確認記録に残し、対象名は置換分離対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 探索照合の付属で OUTLIM=nの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. OUTLIM=nの出力を取らず探索照合の付属の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して探索照合の付属の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の付属へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合の付属において選択記号 B を採用し、識別名は探索照合です。探索照合の付属において OUTLIM=n は説明欄の「探索照合の付属に関係する定義値と表示行を照合する探索照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の付属の証跡を読む担当者は、OUTLIM=nの属性行と IEF236I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の付属は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の付属は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の付属は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため探索照合ではありません。 D: 探索照合の付属は別カテゴリの確認を流用しており、OUTLIM=nの根拠にならないため探索照合ではありません。探索照合の付属に出る OUTLIM=nは JCL DD 文の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **OUTLIM=n**

    - 検証目的: 監査確認の付属について、OUTLIM=nは、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。SYSOUT データセットへの最大レコード数を制限。暴走時のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、監査確認の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にOUTLIM=nを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND OUTLIM=n
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM OUTLIM=n
    CASE OSKB020019
    SOURCE z/OS JCL
    ```

    OUTLIM=nとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020019を同じ出力で読み、監査確認の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020019
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020019.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020019 STEP1 SYSUT1
    ```

    IEF236IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の OUTLIM=n と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### SPIN=UNALLOC {#c17-i0161}
*分類: SYSOUT-付属*  ・  難易度: 中級

DD 解放時に SPOOL に切り離す (FREE=CLOSE と類似目的)。「SPIN=UNALLOC」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 上書分離の付属でジョブデータ定義の運用確認を行います。SPIN=UNALLOC の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書分離の付属を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書分離の付属を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書分離の確認にする。 ✅
    - D. SPIN=UNALLOC の属性行を読まず上書分離の付属の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では SPIN=UNALLOC は「z/OS JCL で SPIN=UNALLOC の扱いを記録する上書分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では SPIN=UNALLOC の表示結果と IEF236I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明だけに寄り、判定名は上書分離不足です。上書分離資料では SPIN=UNALLOC の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 条件照合の付属に関係する SPIN=UNALLOC の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. SPIN=UNALLOC の名称と担当者名のみを残して条件照合の付属の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で条件照合の付属を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件照合の付属の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合の付属において選択記号 A を採用し、識別名は条件照合です。条件照合の付属において SPIN=UNALLOC は説明欄の「SPIN=UNALLOC の用途をジョブデータ定義の表示で確認する条件照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の付属に関連して、z/OS JCL では SPIN=UNALLOC の表示属性と IEF236I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の付属は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の付属は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の付属は別カテゴリの確認を流用しており、SPIN=UNALLOC の根拠にならないため条件照合ではありません。 D: 条件照合の付属は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため条件照合ではありません。条件照合の付属で使う SPIN=UNALLOC という用語は JCL DD 文で扱う確認対象であり、用語名は条件照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **SPIN=UNALLOC**

    - 検証目的: 展開照合の付属について、DD 解放時に SPOOL に切り離す (FREE=CLOSE と類似目的)。「SPIN=UNALLOC」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開照合の付属の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にSPIN=UNALLOCを指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SPIN=UNALLOC
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SPIN=UNALLOC
    CASE OSKB020022
    SOURCE z/OS JCL
    ```

    SPIN=UNALLOCとOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020022を同じ出力で読み、展開照合の付属の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020022
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020022.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020022 STEP1 SYSUT1
    ```

    IEF236IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の SPIN=UNALLOC と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UCS=印字盤 {#c17-i0162}
*分類: SYSOUT-付属*  ・  難易度: 中級

UCS=印字盤は、JCL DD 文のSYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。Universal Character Set (印字盤) の識別子。特定文字盤のチェーンプリンタ向け。「UCS=印字盤」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 構文分離の印字盤に関係する UCS= 印字盤の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、構文分離の証跡として残す。 ✅
    - B. UCS= 印字盤の名称と担当者名だけを残して構文分離の印字盤の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で構文分離の印字盤を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文分離の印字盤の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では UCS= 印字盤 は「UCS= 印字盤の用途をジョブデータ定義の表示で確認する構文分離項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景ではz/OS JCL の UCS= 印字盤と IEF236I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明だけに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では UCS= 印字盤を JCL DD 文で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 呼出照合の印字盤でジョブデータ定義の運用確認を行います。UCS= 印字盤の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出照合の印字盤を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出照合の印字盤を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 ✅
    - D. UCS= 印字盤の属性行を読まず呼出照合の印字盤の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合の印字盤において選択記号 C を採用し、識別名は呼出照合です。呼出照合の印字盤において UCS= 印字盤 は説明欄の「z/OS JCL で UCS= 印字盤の扱いを記録する呼出照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の印字盤を受け取る担当者は、UCS= 印字盤の表示結果と IEF236I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の印字盤は別カテゴリの確認を流用しており、UCS= 印字盤の根拠にならないため呼出照合ではありません。 B: 呼出照合の印字盤は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の印字盤は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の印字盤は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の印字盤が示す UCS= 印字盤は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **UCS= 印字盤**

    - 検証目的: 条件照合の印字盤について、UCS= 印字盤は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。Universal Character Set (印字盤) のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030029の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、条件照合の印字盤の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUCS= 印字盤を指定し、OSKB030029の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UCS= 印字盤
    CASE OSKB030029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UCS= 印字盤
    CASE OSKB030029
    SOURCE z/OS JCL
    ```

    UCS= 印字盤とOSKB030029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030029を同じ出力で読み、条件照合の印字盤の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030029
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030029
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030029.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030029 STEP1 SYSUT1
    ```

    IEF236IとOSKB030029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UCS= 印字盤 と OSKB030029 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **UCS= 印字盤**

    - 検証目的: 値域確認の印字盤について、UCS= 印字盤は、JCL DD 文の SYSOUT-付属で機能名、見出し、または確認対象として参照する項目です。Universal Character Set (印字盤) のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域確認の印字盤の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUCS= 印字盤を指定し、OSKB020016の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UCS= 印字盤
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UCS= 印字盤
    CASE OSKB020016
    SOURCE z/OS JCL
    ```

    UCS= 印字盤とOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020016を同じ出力で読み、値域確認の印字盤の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020016
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020016.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020016 STEP1 SYSUT1
    ```

    IEF236IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UCS= 印字盤 と OSKB020016 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > UNIT

### UNIT 省略時の解決 {#c17-i0163}
*分類: UNIT*  ・  難易度: 初級

DSN がカタログ登録済みなら UNIT/VOL はカタログから補完される。新規割振りで省略するとエラー。「UNIT 省略時の解決」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 復旧追跡の省略時の解決で UNIT 省略時の解決の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT 省略時の解決の出力を取らず復旧追跡の省略時の解決の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧追跡の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して復旧追跡の省略時の解決の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧追跡の省略時の解決へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では UNIT 省略時の解決 は「復旧追跡の省略時の解決に関係する定義値と表示行を照合する復旧追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では UNIT 省略時の解決の属性行と IEF236I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明だけに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では UNIT 省略時の解決を JCL DD 文の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 変更照合の省略時の解決に関する UNIT 省略時の解決の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず変更照合の省略時の解決の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の省略時の解決の証跡として保存して根拠にする。
    - C. UNIT 省略時の解決の変更点を出力本文から切り離して変更照合の省略時の解決の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 変更照合の省略時の解決において選択記号 D を採用し、識別名は変更照合です。変更照合の省略時の解決において UNIT 省略時の解決 は説明欄の「DSN がカタログ登録済みなら UNIT/VOL はカタログから補完される。新規割振りで省略するとエラー。「UNIT 省略時の解決」は割り当」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の省略時の解決に関する記録は、UNIT 省略時の解決の出力行と IEF236I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の省略時の解決は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため変更照合ではありません。 B: 変更照合の省略時の解決は別カテゴリの確認を流用しており、UNIT 省略時の解決の根拠にならないため変更照合ではありません。 C: 変更照合の省略時の解決は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の省略時の解決は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の省略時の解決で記録する UNIT 省略時の解決はz/OS JCL の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT 省略時の解決**

    - 検証目的: 記録追跡の省略時の解決について、DSN がカタログ登録済みなら UNIT/VOL はカタログから補完される。新規割振りで省略するとエラー。「UNIT 省略時の解決」は割り当て結果を調べるとき、DISP、Uに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、記録追跡の省略時の解決の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT 省略時の解決を指定し、OSKB010053の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT 省略時の解決
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT 省略時の解決
    CASE OSKB010053
    SOURCE z/OS JCL
    ```

    UNIT 省略時の解決とOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010053を同じ出力で読み、記録追跡の省略時の解決の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010053
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010053.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010053 STEP1 SYSUT1
    ```

    IEF236IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT 省略時の解決 と OSKB010053 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=(SYSDA,2) {#c17-i0164}
*分類: UNIT*  ・  難易度: 中級

UNIT=(SYSDA,2)は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。汎用名 SYSDA から 2 装置を割り当てる例。マルチボリューム DASD 構成。「UNIT=(SYSDA,2)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 警告追跡のジョブデータ定義に関係する UNIT=(SYSDA,2)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、警告追跡の証跡として残す。 ✅
    - B. UNIT=(SYSDA,2)の名称と担当者名だけを残して警告追跡のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で警告追跡のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告追跡のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では UNIT=(SYSDA,2) は「UNIT=(SYSDA,2)の用途をジョブデータ定義の表示で確認する警告追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景ではz/OS JCL の UNIT=(SYSDA,2)と IEF236I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明だけに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では UNIT=(SYSDA,2)を JCL DD 文で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 監査照合のジョブデータ定義でジョブデータ定義の運用確認を行います。UNIT=(SYSDA,2)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査照合のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査照合のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. UNIT=(SYSDA,2)の属性行を読まず監査照合のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合のジョブデータ定義において選択記号 C を採用し、識別名は監査照合です。監査照合のジョブデータ定義において UNIT=(SYSDA,2) は説明欄の「z/OS JCL で UNIT=(SYSDA,2)の扱いを記録する監査照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のジョブデータ定義を受け取る担当者は、UNIT=(SYSDA,2)の表示結果と IEF236I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=(SYSDA,2)の根拠にならないため監査照合ではありません。 B: 監査照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため監査照合ではありません。 C: 監査照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のジョブデータ定義が示す UNIT=(SYSDA,2)は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=(SYSDA,2)**

    - 検証目的: 優先追跡のジョブデータ定義について、UNIT=(SYSDA,2)は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。汎用名 SYSDA から 2 装置を割り当てる例。マルチボに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=(SYSDA,2)を指定し、OSKB010052の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=(SYSDA,2)
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=(SYSDA,2)
    CASE OSKB010052
    SOURCE z/OS JCL
    ```

    UNIT=(SYSDA,2)とOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010052を同じ出力で読み、優先追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010052
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010052.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010052 STEP1 SYSUT1
    ```

    IEF236IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=(SYSDA,2) と OSKB010052 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=(unit,,DEFER) {#c17-i0165}
*分類: UNIT*  ・  難易度: 中級

UNIT=(unit,,DEFER)は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。DEFER 指定でデータセットが実際に開かれるまでマウント待ち。ステップ開始時のマウント要求を遅延。「UNIT=(unit,,DEFER)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 順序追跡のジョブデータ定義でジョブデータ定義の運用確認を行います。UNIT=(unit 命令の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序追跡のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序追跡のジョブデータ定義を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序追跡の根拠を固定する。 ✅
    - D. UNIT=(unit 命令の属性行を読まず順序追跡のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では UNIT=(unit 命令 は「z/OS JCL で UNIT=(unit 命令の扱いを記録する順序追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では UNIT=(unit 命令の表示結果と IEF236I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明だけに寄り、判定名は順序追跡不足です。順序追跡資料では UNIT=(unit 命令の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 警告照合のジョブデータ定義に関係する UNIT=(unit,,DEFER)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 ✅
    - B. UNIT=(unit,,DEFER)の名称と担当者名のみを残して警告照合のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で警告照合のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告照合のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合のジョブデータ定義において選択記号 A を採用し、識別名は警告照合です。警告照合のジョブデータ定義において UNIT=(unit,,DEFER) は説明欄の「UNIT=(unit,,DEFER)の用途をジョブデータ定義の表示で確認する警告照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のジョブデータ定義に関連して、z/OS JCL では UNIT=(unit,,DEFER)の表示属性と IEF236I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=(unit,,DEFER)の根拠にならないため警告照合ではありません。 D: 警告照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため警告照合ではありません。警告照合のジョブデータ定義で使う UNIT=(unit,,DEFER)という用語は JCL DD 文で扱う確認対象であり、用語名は警告照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=(unit,,DEFER)**

    - 検証目的: 区切追跡のジョブデータ定義について、UNIT=(unit,,DEFER)は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。DEFER 指定でデータセットが実際に開かれるまでに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=(unit,,DEFER)を指定し、OSKB010050の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=(unit,,DEFER)
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=(unit,,DEFER)
    CASE OSKB010050
    SOURCE z/OS JCL
    ```

    UNIT=(unit,,DEFER)とOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010050を同じ出力で読み、区切追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010050
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010050.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010050 STEP1 SYSUT1
    ```

    IEF236IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=(unit,,DEFER) と OSKB010050 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=(unit,,P) 並列マウント {#c17-i0166}
*分類: UNIT*  ・  難易度: 中級

UNIT=(unit,,P) 並列マウントは、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 値域追跡の並列マウントに関する UNIT= 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域追跡の並列マウントの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域追跡の並列マウントの証跡として保存して根拠にする。
    - C. UNIT= 属性の変更点を出力本文から切り離して値域追跡の並列マウントの承認欄だけ残す。
    - D. IEF236I を含む表示を保存し、説明欄との差分を値域追跡で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では UNIT= 属性 は「UNIT= 属性の状態と出力メッセージを結び付ける値域追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では UNIT= 属性の出力行と IEF236I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明だけに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では UNIT= 属性をz/OS JCL の確認記録に残し、対象名は値域追跡対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 復旧照合の並列マウントで UNIT=(unit,,P) 並列マウントの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT=(unit,,P) 並列マウントの出力を取らず復旧照合の並列マウントの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して復旧照合の並列マウントの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の並列マウントへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合の並列マウントにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の並列マウントにおいて UNIT=(unit,,P) 並列マウント は説明欄の「復旧照合の並列マウントに関係する定義値と表示行を照合する復旧照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の並列マウントの証跡を読む担当者は、UNIT=(unit,,P) 並列マウントの属性行と IEF236I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の並列マウントは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の並列マウントは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の並列マウントは戻り値や記録番号に寄り、IEF236I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の並列マウントは別カテゴリの確認を流用しており、UNIT=(unit,,P) 並列マウントの根拠にならないため復旧照合ではありません。復旧照合の並列マウントに出る UNIT=(unit,,P) 並列マウントは JCL DD 文の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **UNIT=(unit,,P) 並列マウント**

    - 検証目的: 優先確認の並列マウントについて、UNIT=(unit,,P) 並列マウントは、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030012の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先確認の並列マウントの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=(unit,,P) 並列マを指定し、OSKB030012の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=(unit,,P) 並列マ
    CASE OSKB030012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=(unit,,P) 並列マ
    CASE OSKB030012
    SOURCE z/OS JCL
    ```

    UNIT=(unit,,P) 並列マとOSKB030012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030012を同じ出力で読み、優先確認の並列マウントの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030012
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030012
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030012.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030012 STEP1 SYSUT1
    ```

    IEF236IとOSKB030012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=(unit,,P) 並列マ と OSKB030012 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **UNIT=(unit,,P) 並列マウント**

    - 検証目的: 範囲追跡の並列マウントについて、UNIT=(unit,,P) 並列マウントは、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲追跡の並列マウントの確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=(unit,,P) 並列マを指定し、OSKB010051の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=(unit,,P) 並列マ
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=(unit,,P) 並列マ
    CASE OSKB010051
    SOURCE z/OS JCL
    ```

    UNIT=(unit,,P) 並列マとOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010051を同じ出力で読み、範囲追跡の並列マウントの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010051
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010051.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010051 STEP1 SYSUT1
    ```

    IEF236IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=(unit,,P) 並列マ と OSKB010051 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=(unit,count) {#c17-i0167}
*分類: UNIT*  ・  難易度: 中級

UNIT=(unit,count)は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。第 2 サブパラメータで装置台数を指定。マルチボリュームを同時に並べる時などに使用。「UNIT=(unit,count)」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 比較追跡のジョブデータ定義で UNIT=(unit 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT=(unit 命令の出力を取らず比較追跡のジョブデータ定義の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較追跡の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して比較追跡のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較追跡のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では UNIT=(unit 命令 は「比較追跡のジョブデータ定義に関係する定義値と表示行を照合する比較追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では UNIT=(unit 命令の属性行と IEF236I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明だけに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では UNIT=(unit 命令を JCL DD 文の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 値域照合のジョブデータ定義に関する UNIT=(unit,count)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域照合のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のジョブデータ定義の証跡として保存して根拠にする。
    - C. UNIT=(unit,count)の変更点を出力本文から切り離して値域照合のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合のジョブデータ定義において選択記号 D を採用し、識別名は値域照合です。値域照合のジョブデータ定義において UNIT=(unit,count) は説明欄の「UNIT=(unit,count)の状態と出力メッセージを結び付ける値域照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のジョブデータ定義に関する記録は、UNIT=(unit,count)の出力行と IEF236I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため値域照合ではありません。 B: 値域照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=(unit,count)の根拠にならないため値域照合ではありません。 C: 値域照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のジョブデータ定義で記録する UNIT=(unit,count)はz/OS JCL の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=(unit,count)**

    - 検証目的: 条件追跡のジョブデータ定義について、UNIT=(unit,count)は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。第 2 サブパラメータで装置台数を指定。マルチボリュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=(unit,count)を指定し、OSKB010049の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=(unit,count)
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=(unit,count)
    CASE OSKB010049
    SOURCE z/OS JCL
    ```

    UNIT=(unit,count)とOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010049を同じ出力で読み、条件追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010049
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010049.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010049 STEP1 SYSUT1
    ```

    IEF236IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=(unit,count) と OSKB010049 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=3390 {#c17-i0168}
*分類: UNIT*  ・  難易度: 中級

UNIT=3390は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。装置タイプ名指定 (3390 DASD)。具体装置に紐付くため可搬性は低下。「UNIT=3390」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 条件追跡のジョブデータ定義に関係する UNIT=3390 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD で得た表示本文を使い、条件追跡の採否を説明欄に結び付ける。 ✅
    - B. UNIT=3390 の名称と担当者名だけを残して条件追跡のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で条件追跡のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件追跡のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では UNIT=3390 は「UNIT=3390 の用途をジョブデータ定義の表示で確認する条件追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景ではz/OS JCL の UNIT=3390 と IEF236I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明だけに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では UNIT=3390 を JCL DD 文で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 範囲照合のジョブデータ定義でジョブデータ定義の運用確認を行います。UNIT=3390 の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲照合のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲照合のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. UNIT=3390 の属性行を読まず範囲照合のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合のジョブデータ定義において選択記号 C を採用し、識別名は範囲照合です。範囲照合のジョブデータ定義において UNIT=3390 は説明欄の「z/OS JCL で UNIT=3390 の扱いを記録する範囲照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のジョブデータ定義を受け取る担当者は、UNIT=3390 の表示結果と IEF236I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=3390 の根拠にならないため範囲照合ではありません。 B: 範囲照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のジョブデータ定義が示す UNIT=3390 は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=3390**

    - 検証目的: 置換追跡のジョブデータ定義について、UNIT=3390 は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。装置タイプ名指定 (3390 DASD)。具体装置に紐付くため可搬性に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=3390を指定し、OSKB010044の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=3390
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=3390
    CASE OSKB010044
    SOURCE z/OS JCL
    ```

    UNIT=3390とOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010044を同じ出力で読み、置換追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010044
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010044.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010044 STEP1 SYSUT1
    ```

    IEF236IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=3390 と OSKB010044 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=3480 {#c17-i0169}
*分類: UNIT*  ・  難易度: 中級

装置タイプ名指定 (3480 カートリッジテープ、3490 の前世代)。「UNIT=3480」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 範囲追跡のジョブデータ定義でジョブデータ定義の運用確認を行います。UNIT=3480 の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で範囲追跡のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず範囲追跡のジョブデータ定義を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲追跡の確認にする。 ✅
    - D. UNIT=3480 の属性行を読まず範囲追跡のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では UNIT=3480 は「z/OS JCL で UNIT=3480 の扱いを記録する範囲追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では UNIT=3480 の表示結果と IEF236I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明だけに寄り、判定名は範囲追跡不足です。範囲追跡資料では UNIT=3480 の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 記録照合のジョブデータ定義に関係する UNIT=3480 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 ✅
    - B. UNIT=3480 の名称と担当者名のみを残して記録照合のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で記録照合のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録照合のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合のジョブデータ定義において選択記号 A を採用し、識別名は記録照合です。記録照合のジョブデータ定義において UNIT=3480 は説明欄の「UNIT=3480 の用途をジョブデータ定義の表示で確認する記録照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のジョブデータ定義に関連して、z/OS JCL では UNIT=3480 の表示属性と IEF236I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=3480 の根拠にならないため記録照合ではありません。 D: 記録照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため記録照合ではありません。記録照合のジョブデータ定義で使う UNIT=3480 という用語は JCL DD 文で扱う確認対象であり、用語名は記録照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **UNIT=3480**

    - 検証目的: 範囲確認のジョブデータ定義について、装置タイプ名指定 (3480 カートリッジテープ、3490 の前世代)。「UNIT=3480」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットやに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030011の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲確認のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=3480を指定し、OSKB030011の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=3480
    CASE OSKB030011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=3480
    CASE OSKB030011
    SOURCE z/OS JCL
    ```

    UNIT=3480とOSKB030011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030011を同じ出力で読み、範囲確認のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030011
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030011
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030011.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030011 STEP1 SYSUT1
    ```

    IEF236IとOSKB030011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=3480 と OSKB030011 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **UNIT=3480**

    - 検証目的: 探索追跡のジョブデータ定義について、装置タイプ名指定 (3480 カートリッジテープ、3490 の前世代)。「UNIT=3480」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットやに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、探索追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=3480を指定し、OSKB010046の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=3480
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=3480
    CASE OSKB010046
    SOURCE z/OS JCL
    ```

    UNIT=3480とOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010046を同じ出力で読み、探索追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010046
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010046.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010046 STEP1 SYSUT1
    ```

    IEF236IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=3480 と OSKB010046 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=3490 {#c17-i0170}
*分類: UNIT*  ・  難易度: 中級

UNIT=3490は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 区切追跡のジョブデータ定義で UNIT=3490 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT=3490 の出力を取らず区切追跡のジョブデータ定義の説明文と承認印だけを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切追跡として引き継ぐ。 ✅
    - C. ST OSKBDD を省略して区切追跡のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切追跡のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では UNIT=3490 は「区切追跡のジョブデータ定義に関係する定義値と表示行を照合する区切追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では UNIT=3490 の属性行と IEF236I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明だけに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では UNIT=3490 を JCL DD 文の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 優先照合のジョブデータ定義に関する UNIT=3490 の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先照合のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のジョブデータ定義の証跡として保存して根拠にする。
    - C. UNIT=3490 の変更点を出力本文から切り離して優先照合のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合のジョブデータ定義において選択記号 D を採用し、識別名は優先照合です。優先照合のジョブデータ定義において UNIT=3490 は説明欄の「UNIT=3490 の状態と出力メッセージを結び付ける優先照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のジョブデータ定義に関する記録は、UNIT=3490 の出力行と IEF236I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため優先照合ではありません。 B: 優先照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=3490 の根拠にならないため優先照合ではありません。 C: 優先照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のジョブデータ定義で記録する UNIT=3490 はz/OS JCL の確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=3490**

    - 検証目的: 終端追跡のジョブデータ定義について、UNIT=3490 は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=3490を指定し、OSKB010045の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=3490
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=3490
    CASE OSKB010045
    SOURCE z/OS JCL
    ```

    UNIT=3490とOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010045を同じ出力で読み、終端追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010045
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010045.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010045 STEP1 SYSUT1
    ```

    IEF236IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=3490 と OSKB010045 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=AFF=ddname (装置親近性) {#c17-i0171}
*分類: UNIT*  ・  難易度: 中級

UNIT=AFF=ddname (装置親近性)は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 記録追跡の装置親近性に関係する UNIT 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録追跡で再確認できる形にする。 ✅
    - B. UNIT 属性の名称と担当者名だけを残して記録追跡の装置親近性の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で記録追跡の装置親近性を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず記録追跡の装置親近性の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では UNIT 属性 は「UNIT 属性の用途をジョブデータ定義の表示で確認する記録追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景ではz/OS JCL の UNIT 属性と IEF236I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明だけに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では UNIT 属性を JCL DD 文で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 順序照合の装置親近性でジョブデータ定義の運用確認を行います。UNIT=AFF=ddname (装置親近性)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序照合の装置親近性を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序照合の装置親近性を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序照合の記録として扱う。 ✅
    - D. UNIT=AFF=ddname (装置親近性)の属性行を読まず順序照合の装置親近性の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合の装置親近性において選択記号 C を採用し、識別名は順序照合です。順序照合の装置親近性において UNIT=AFF=ddname (装置親近性) は説明欄の「z/OS JCL で UNIT=AFF=ddname (装置親近性)の扱いを記録する順序照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の装置親近性を受け取る担当者は、UNIT=AFF=ddname (装置親近性)の表示結果と IEF236I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の装置親近性は別カテゴリの確認を流用しており、UNIT=AFF=ddname (装置親近性)の根拠にならないため順序照合ではありません。 B: 順序照合の装置親近性は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため順序照合ではありません。 C: 順序照合の装置親近性は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の装置親近性は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の装置親近性が示す UNIT=AFF=ddname (装置親近性)は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=AFF=ddname (装置親近性)**

    - 検証目的: 出力追跡の装置親近性について、UNIT=AFF=ddname (装置親近性)は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、出力追跡の装置親近性の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=AFF=ddname (装を指定し、OSKB010048の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=AFF=ddname (装
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=AFF=ddname (装
    CASE OSKB010048
    SOURCE z/OS JCL
    ```

    UNIT=AFF=ddname (装とOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010048を同じ出力で読み、出力追跡の装置親近性の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010048
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010048.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010048 STEP1 SYSUT1
    ```

    IEF236IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=AFF=ddname (装 と OSKB010048 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=CART {#c17-i0172}
*分類: UNIT*  ・  難易度: 中級

カートリッジテープ装置グループの典型名 (環境依存)。「UNIT=CART」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 出力追跡のジョブデータ定義に関する UNIT=CART の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力追跡のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力追跡のジョブデータ定義の証跡として保存して根拠にする。
    - C. UNIT=CART の変更点を出力本文から切り離して出力追跡のジョブデータ定義の承認欄だけ残す。
    - D. 同じ画面で対象行と IEF236I を読み、出力追跡の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では UNIT=CART は「UNIT=CART の状態と出力メッセージを結び付ける出力追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では UNIT=CART の出力行と IEF236I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明だけに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では UNIT=CART をz/OS JCL の確認記録に残し、対象名は出力追跡対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 区切照合のジョブデータ定義で UNIT=CART の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT=CART の出力を取らず区切照合のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して区切照合のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合のジョブデータ定義において選択記号 B を採用し、識別名は区切照合です。区切照合のジョブデータ定義において UNIT=CART は説明欄の「区切照合のジョブデータ定義に関係する定義値と表示行を照合する区切照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のジョブデータ定義の証跡を読む担当者は、UNIT=CART の属性行と IEF236I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため区切照合ではありません。 D: 区切照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=CART の根拠にならないため区切照合ではありません。区切照合のジョブデータ定義に出る UNIT=CART は JCL DD 文の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=CART**

    - 検証目的: 呼出追跡のジョブデータ定義について、カートリッジテープ装置グループの典型名 (環境依存)。「UNIT=CART」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=CARTを指定し、OSKB010043の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=CART
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=CART
    CASE OSKB010043
    SOURCE z/OS JCL
    ```

    UNIT=CARTとOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010043を同じ出力で読み、呼出追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010043
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010043.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010043 STEP1 SYSUT1
    ```

    IEF236IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=CART と OSKB010043 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=SYSALLDA {#c17-i0173}
*分類: UNIT*  ・  難易度: 中級

UNIT=SYSALLDAは、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。全 DASD 装置を対象とする IBM 標準汎用名。SYSDA 未定義環境でも使える。「UNIT=SYSALLDA」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 探索追跡のジョブデータ定義で UNIT=SYSALLDA の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT=SYSALLDA の出力を取らず探索追跡のジョブデータ定義の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、探索追跡の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して探索追跡のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索追跡のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では UNIT=SYSALLDA は「探索追跡のジョブデータ定義に関係する定義値と表示行を照合する探索追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では UNIT=SYSALLDA の属性行と IEF236I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明だけに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では UNIT=SYSALLDA を JCL DD 文の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 出力照合のジョブデータ定義に関する UNIT=SYSALLDA の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力照合のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のジョブデータ定義の証跡として保存して根拠にする。
    - C. UNIT=SYSALLDA の変更点を出力本文から切り離して出力照合のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合のジョブデータ定義において選択記号 D を採用し、識別名は出力照合です。出力照合のジョブデータ定義において UNIT=SYSALLDA は説明欄の「UNIT=SYSALLDA の状態と出力メッセージを結び付ける出力照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のジョブデータ定義に関する記録は、UNIT=SYSALLDA の出力行と IEF236I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力照合ではありません。 B: 出力照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=SYSALLDA の根拠にならないため出力照合ではありません。 C: 出力照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のジョブデータ定義で記録する UNIT=SYSALLDA はz/OS JCL の確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **UNIT=SYSALLDA**

    - 検証目的: 区切確認のジョブデータ定義について、UNIT=SYSALLDA は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。全 DASD 装置を対象とする IBM 標準汎用名。SYSDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、区切確認のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=SYSALLDAを指定し、OSKB030010の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=SYSALLDA
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=SYSALLDA
    CASE OSKB030010
    SOURCE z/OS JCL
    ```

    UNIT=SYSALLDAとOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030010を同じ出力で読み、区切確認のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030010
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030010
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030010.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030010 STEP1 SYSUT1
    ```

    IEF236IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=SYSALLDA と OSKB030010 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **UNIT=SYSALLDA**

    - 検証目的: 構文追跡のジョブデータ定義について、UNIT=SYSALLDA は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。全 DASD 装置を対象とする IBM 標準汎用名。SYSDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010041の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、構文追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=SYSALLDAを指定し、OSKB010041の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=SYSALLDA
    CASE OSKB010041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=SYSALLDA
    CASE OSKB010041
    SOURCE z/OS JCL
    ```

    UNIT=SYSALLDAとOSKB010041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010041を同じ出力で読み、構文追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010041
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010041
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010041.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010041 STEP1 SYSUT1
    ```

    IEF236IとOSKB010041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=SYSALLDA と OSKB010041 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=SYSDA {#c17-i0174}
*分類: UNIT*  ・  難易度: 中級

UNIT=SYSDAは、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。汎用 DASD グループ名。インストールが定義した DA 装置一式から空きを割り当てる。一時 DSN/中間データの定番。「UNIT=SYSDA」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 終端追跡のジョブデータ定義に関係する UNIT=SYSDA の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、終端追跡の証跡として残す。 ✅
    - B. UNIT=SYSDA の名称と担当者名だけを残して終端追跡のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で終端追跡のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端追跡のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では UNIT=SYSDA は「UNIT=SYSDA の用途をジョブデータ定義の表示で確認する終端追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景ではz/OS JCL の UNIT=SYSDA と IEF236I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明だけに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では UNIT=SYSDA を JCL DD 文で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 上書照合のジョブデータ定義でジョブデータ定義の運用確認を行います。UNIT=SYSDA の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書照合のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書照合のジョブデータ定義を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書照合の記録として扱う。 ✅
    - D. UNIT=SYSDA の属性行を読まず上書照合のジョブデータ定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合のジョブデータ定義において選択記号 C を採用し、識別名は上書照合です。上書照合のジョブデータ定義において UNIT=SYSDA は説明欄の「z/OS JCL で UNIT=SYSDA の扱いを記録する上書照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のジョブデータ定義を受け取る担当者は、UNIT=SYSDA の表示結果と IEF236I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=SYSDA の根拠にならないため上書照合ではありません。 B: 上書照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため上書照合ではありません。 C: 上書照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のジョブデータ定義が示す UNIT=SYSDA は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=SYSDA**

    - 検証目的: 変更照合のジョブデータ定義について、UNIT=SYSDA は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。汎用 DASD グループ名。インストールが定義した DA 装置一式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、変更照合のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=SYSDAを指定し、OSKB010040の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=SYSDA
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=SYSDA
    CASE OSKB010040
    SOURCE z/OS JCL
    ```

    UNIT=SYSDAとOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010040を同じ出力で読み、変更照合のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010040
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010040
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010040.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010040 STEP1 SYSUT1
    ```

    IEF236IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=SYSDA と OSKB010040 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=TAPE {#c17-i0175}
*分類: UNIT*  ・  難易度: 中級

UNIT=TAPEは、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 上書追跡のジョブデータ定義でジョブデータ定義の運用確認を行います。UNIT=TAPE の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書追跡のジョブデータ定義を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書追跡のジョブデータ定義を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書追跡の根拠にする。 ✅
    - D. UNIT=TAPE の属性行を読まず上書追跡のジョブデータ定義の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では UNIT=TAPE は「z/OS JCL で UNIT=TAPE の扱いを記録する上書追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では UNIT=TAPE の表示結果と IEF236I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明だけに寄り、判定名は上書追跡不足です。上書追跡資料では UNIT=TAPE の使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 条件照合のジョブデータ定義に関係する UNIT=TAPE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. UNIT=TAPE の名称と担当者名のみを残して条件照合のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で条件照合のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件照合のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合のジョブデータ定義において選択記号 A を採用し、識別名は条件照合です。条件照合のジョブデータ定義において UNIT=TAPE は説明欄の「UNIT=TAPE の用途をジョブデータ定義の表示で確認する条件照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のジョブデータ定義に関連して、z/OS JCL では UNIT=TAPE の表示属性と IEF236I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のジョブデータ定義は別カテゴリの確認を流用しており、UNIT=TAPE の根拠にならないため条件照合ではありません。 D: 条件照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため条件照合ではありません。条件照合のジョブデータ定義で使う UNIT=TAPE という用語は JCL DD 文で扱う確認対象であり、用語名は条件照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=TAPE**

    - 検証目的: 展開追跡のジョブデータ定義について、UNIT=TAPE は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=TAPEを指定し、OSKB010042の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=TAPE
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=TAPE
    CASE OSKB010042
    SOURCE z/OS JCL
    ```

    UNIT=TAPEとOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010042を同じ出力で読み、展開追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010042
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010042.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010042 STEP1 SYSUT1
    ```

    IEF236IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=TAPE と OSKB010042 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### UNIT=device-address (例 180) {#c17-i0176}
*分類: UNIT*  ・  難易度: 中級

UNIT=device-address (例 180)は、JCL DD 文のUNITで機能名、見出し、または確認対象として参照する項目です。装置 ID (アドレス) を 3〜4 桁で直接指定。特定物理装置をピン留めしたい場合に限る。「UNIT=device-address (例 180)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 優先追跡の例に関する UNIT 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先追跡の例の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先追跡の例の証跡として保存して根拠にする。
    - C. UNIT 属性の変更点を出力本文から切り離して優先追跡の例の承認欄だけ残す。
    - D. z/OS JCL の表示形式に沿って根拠行を採り、優先追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では UNIT 属性 は「UNIT 属性の状態と出力メッセージを結び付ける優先追跡項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では UNIT 属性の出力行と IEF236I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明だけに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では UNIT 属性をz/OS JCL の確認記録に残し、対象名は優先追跡対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 比較照合の例で UNIT=device-address (例 1の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. UNIT=device-address (例 1の出力を取らず比較照合の例の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して比較照合の例の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の例へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合の例において選択記号 B を採用し、識別名は比較照合です。比較照合の例において UNIT=device-address (例 1 は説明欄の「比較照合の例に関係する定義値と表示行を照合する比較照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の例の証跡を読む担当者は、UNIT=device-address (例 1の属性行と IEF236I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の例は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の例は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の例は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため比較照合ではありません。 D: 比較照合の例は別カテゴリの確認を流用しており、UNIT=device-address (例 1の根拠にならないため比較照合ではありません。比較照合の例に出る UNIT=device-address (例 1は JCL DD 文の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **UNIT=device-address (例 180)**

    - 検証目的: 上書追跡の例について、UNIT=device-address (例 180)は、JCL DD 文の UNIT で機能名、見出し、または確認対象として参照する項目です。装置 ID (アドレス) を 3に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、上書追跡の例の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にUNIT=device-addresを指定し、OSKB010047の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNIT=device-addres
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNIT=device-addres
    CASE OSKB010047
    SOURCE z/OS JCL
    ```

    UNIT=device-addresとOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB010047を同じ出力で読み、上書追跡の例の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB010047
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB010047.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB010047 STEP1 SYSUT1
    ```

    IEF236IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の UNIT=device-addres と OSKB010047 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB010047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide




## JCL DD 文 > USS-PATH

### FILEDATA=BINARY {#c17-i0177}
*分類: USS-PATH*  ・  難易度: 中級

バイナリ扱い (改行解釈なし)。「FILEDATA=BINARY」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 条件検分のジョブデータ定義に関係する FILEDATA=BINARY の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、条件検分の証跡として残す。 ✅
    - B. FILEDATA=BINARY の名称と担当者名だけを残して条件検分のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で条件検分のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件検分のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では FILEDATA=BINARY は「FILEDATA=BINARY の用途をジョブデータ定義の表示で確認する条件検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景ではz/OS JCL の FILEDATA=BINARY と IEF236I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明だけに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では FILEDATA=BINARY を JCL DD 文で扱う確認対象とし、用語名は条件検分用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 構文照合のジョブデータ定義に関係する FILEDATA=BINARY の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 ✅
    - B. FILEDATA=BINARY の名称と担当者名のみを残して構文照合のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で構文照合のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず構文照合のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合のジョブデータ定義において選択記号 A を採用し、識別名は構文照合です。構文照合のジョブデータ定義において FILEDATA=BINARY は説明欄の「FILEDATA=BINARY の用途をジョブデータ定義の表示で確認する構文照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のジョブデータ定義に関連して、z/OS JCL では FILEDATA=BINARY の表示属性と IEF236I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のジョブデータ定義は別カテゴリの確認を流用しており、FILEDATA=BINARY の根拠にならないため構文照合ではありません。 D: 構文照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため構文照合ではありません。構文照合のジョブデータ定義で使う FILEDATA=BINARY という用語は JCL DD 文で扱う確認対象であり、用語名は構文照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FILEDATA=BINARY**

    - 検証目的: 置換検査のジョブデータ定義について、バイナリ扱い (改行解釈なし)。「FILEDATA=BINARY」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすいに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、置換検査のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にFILEDATA=BINARYを指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FILEDATA=BINARY
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FILEDATA=BINARY
    CASE OSKB020064
    SOURCE z/OS JCL
    ```

    FILEDATA=BINARYとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020064を同じ出力で読み、置換検査のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020064
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020064.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020064 STEP1 SYSUT1
    ```

    IEF236IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FILEDATA=BINARY と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FILEDATA=RECORD {#c17-i0178}
*分類: USS-PATH*  ・  難易度: 中級

FILEDATA=RECORDは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。固定長レコード形式扱い (LRECL 必須)。「FILEDATA=RECORD」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 区切検分のジョブデータ定義で FILEDATA=RECORD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FILEDATA=RECORD の出力を取らず区切検分のジョブデータ定義の説明文と承認印だけを残す。
    - B. 出典欄の説明と運用出力を照合し、区切検分の確認記録にまとめる。 ✅
    - C. ST OSKBDD を省略して区切検分のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切検分のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では FILEDATA=RECORD は「区切検分のジョブデータ定義に関係する定義値と表示行を照合する区切検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では FILEDATA=RECORD の属性行と IEF236I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明だけに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では FILEDATA=RECORD を JCL DD 文の運用手順で確認し、初出名は区切検分初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 展開照合のジョブデータ定義で FILEDATA=RECORD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FILEDATA=RECORD の出力を取らず展開照合のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 ✅
    - C. ST OSKBDD を省略して展開照合のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合のジョブデータ定義において選択記号 B を採用し、識別名は展開照合です。展開照合のジョブデータ定義において FILEDATA=RECORD は説明欄の「展開照合のジョブデータ定義に関係する定義値と表示行を照合する展開照合項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合のジョブデータ定義の証跡を読む担当者は、FILEDATA=RECORD の属性行と IEF236I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため展開照合ではありません。 D: 展開照合のジョブデータ定義は別カテゴリの確認を流用しており、FILEDATA=RECORD の根拠にならないため展開照合ではありません。展開照合のジョブデータ定義に出る FILEDATA=RECORD は JCL DD 文の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FILEDATA=RECORD**

    - 検証目的: 終端検査のジョブデータ定義について、FILEDATA=RECORD は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。固定長レコード形式扱い (LRECL 必須)。「に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、終端検査のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にFILEDATA=RECORDを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FILEDATA=RECORD
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FILEDATA=RECORD
    CASE OSKB020065
    SOURCE z/OS JCL
    ```

    FILEDATA=RECORDとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020065を同じ出力で読み、終端検査のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020065
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020065.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020065 STEP1 SYSUT1
    ```

    IEF236IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FILEDATA=RECORD と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### FILEDATA=TEXT {#c17-i0179}
*分類: USS-PATH*  ・  難易度: 中級

FILEDATA=TEXTは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 出力検分のジョブデータ定義に関する FILEDATA=TEXT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力検分のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力検分のジョブデータ定義の証跡として保存して根拠にする。
    - C. FILEDATA=TEXT の変更点を出力本文から切り離して出力検分のジョブデータ定義の承認欄だけ残す。
    - D. IEF236I を含む表示を保存し、説明欄との差分を出力検分で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では FILEDATA=TEXT は「FILEDATA=TEXT の状態と出力メッセージを結び付ける出力検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では FILEDATA=TEXT の出力行と IEF236I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明だけに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では FILEDATA=TEXT をz/OS JCL の確認記録に残し、対象名は出力検分対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 変更確認のジョブデータ定義に関する FILEDATA=TEXT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず変更確認のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のジョブデータ定義の証跡として保存して根拠にする。
    - C. FILEDATA=TEXT の変更点を出力本文から切り離して変更確認のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認のジョブデータ定義において選択記号 D を採用し、識別名は変更確認です。変更確認のジョブデータ定義において FILEDATA=TEXT は説明欄の「FILEDATA=TEXT の状態と出力メッセージを結び付ける変更確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のジョブデータ定義に関する記録は、FILEDATA=TEXT の出力行と IEF236I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため変更確認ではありません。 B: 変更確認のジョブデータ定義は別カテゴリの確認を流用しており、FILEDATA=TEXT の根拠にならないため変更確認ではありません。 C: 変更確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のジョブデータ定義で記録する FILEDATA=TEXT はz/OS JCL の確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **FILEDATA=TEXT**

    - 検証目的: 呼出検査のジョブデータ定義について、FILEDATA=TEXT は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、呼出検査のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にFILEDATA=TEXTを指定し、OSKB020063の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND FILEDATA=TEXT
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM FILEDATA=TEXT
    CASE OSKB020063
    SOURCE z/OS JCL
    ```

    FILEDATA=TEXTとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020063を同じ出力で読み、呼出検査のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020063
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020063.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020063 STEP1 SYSUT1
    ```

    IEF236IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の FILEDATA=TEXT と OSKB020063 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATH='/path/to/file' {#c17-i0180}
*分類: USS-PATH*  ・  難易度: 中級

USS ファイルを DD として参照。バッチプログラムから USS ファイルにアクセスする基本形。「PATH='/path/to/file'」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 優先読解の・ ・ ・に関する PATH=' 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず優先読解の・ ・ ・の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先読解の・ ・ ・の証跡として保存して根拠にする。
    - C. PATH=' 属性の変更点を出力本文から切り離して優先読解の・ ・ ・の承認欄だけ残す。
    - D. z/OS JCL の表示形式に沿って根拠行を採り、優先読解の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では PATH=' 属性 は「PATH=' 属性の状態と出力メッセージを結び付ける優先読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では PATH=' 属性の出力行と IEF236I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明だけに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では PATH=' 属性をz/OS JCL の確認記録に残し、対象名は優先読解対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 構文照合保守の構文照合として PATH を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 戻り値と時刻を主な根拠にして表示行を読まない。
    - D. 構文照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正解はDです。構文照合保守で扱う PATH は JCL DD 文 の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として PATH を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATH='・path・to・file'**

    - 検証目的: 上書追跡の・ ・ ・について、USS ファイルを DD として参照。バッチプログラムから USS ファイルにアクセスする基本形。「PATH='/path/to/file'」は割り当て結果を調べるとき、Dに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、上書追跡の・ ・ ・の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATH='・path・to・filを指定し、OSKB020047の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATH='・path・to・fil
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATH='・path・to・fil
    CASE OSKB020047
    SOURCE z/OS JCL
    ```

    PATH='・path・to・filとOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020047を同じ出力で読み、上書追跡の・ ・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020047
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020047.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020047 STEP1 SYSUT1
    ```

    IEF236IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATH='・path・to・fil と OSKB020047 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHDISP 第 2 引数 (異常) {#c17-i0181}
*分類: USS-PATH*  ・  難易度: 中級

PATHDISP 第 2 引数 (異常)は、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。PATHDISP=(KEEP,DELETE) のように 2 番目で異常終了時の処理を指定。「PATHDISP 第 2 引数 (異常)」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 上書検分の第 引数 異常でジョブデータ定義の運用確認を行います。PATHDISP 第 2 引数 属性の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で上書検分の第 引数 異常を確認した扱いにする。
    - B. IEF236I の有無を確認せず上書検分の第 引数 異常を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書検分の根拠を固定する。 ✅
    - D. PATHDISP 第 2 引数 属性の属性行を読まず上書検分の第 引数 異常の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では PATHDISP 第 2 引数 属性 は「z/OS JCL で PATHDISP 第 2 引数 属性の扱いを記録する上書検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では PATHDISP 第 2 引数 属性の表示結果と IEF236I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明だけに寄り、判定名は上書検分不足です。上書検分資料では PATHDISP 第 2 引数 属性の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 監査確認の第 引数 異常でジョブデータ定義の運用確認を行います。PATHDISP 第 2 引数 (異常)の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で監査確認の第 引数 異常を確認した扱いにする。
    - B. IEF236I の有無を確認せず監査確認の第 引数 異常を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査確認の記録として扱う。 ✅
    - D. PATHDISP 第 2 引数 (異常)の属性行を読まず監査確認の第 引数 異常の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認の第 引数 異常において選択記号 C を採用し、識別名は監査確認です。監査確認の第 引数 異常において PATHDISP 第 2 引数 (異常) は説明欄の「z/OS JCL で PATHDISP 第 2 引数 (異常)の扱いを記録する監査確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の第 引数 異常を受け取る担当者は、PATHDISP 第 2 引数 (異常)の表示結果と IEF236I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の第 引数 異常は別カテゴリの確認を流用しており、PATHDISP 第 2 引数 (異常)の根拠にならないため監査確認ではありません。 B: 監査確認の第 引数 異常は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため監査確認ではありません。 C: 監査確認の第 引数 異常は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の第 引数 異常は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の第 引数 異常が示す PATHDISP 第 2 引数 (異常)は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHDISP 第 2 引数 (異常)**

    - 検証目的: 展開検査の第 引数 異常について、PATHDISP 第 2 引数 (異常)は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。PATHDISP=(KEEP,DELEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、展開検査の第 引数 異常の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHDISP 第 2 引数 (異を指定し、OSKB020062の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHDISP 第 2 引数 (異
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHDISP 第 2 引数 (異
    CASE OSKB020062
    SOURCE z/OS JCL
    ```

    PATHDISP 第 2 引数 (異とOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020062を同じ出力で読み、展開検査の第 引数 異常の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020062
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020062.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020062 STEP1 SYSUT1
    ```

    IEF236IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHDISP 第 2 引数 (異 と OSKB020062 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHDISP=DELETE {#c17-i0182}
*分類: USS-PATH*  ・  難易度: 中級

ステップ終了時にファイルを削除 (正常終了)。「PATHDISP=DELETE」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 探索検分のジョブデータ定義で PATHDISP=DELETE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHDISP=DELETE の出力を取らず探索検分のジョブデータ定義の説明文と承認印だけを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索検分の確認値として扱う。 ✅
    - C. ST OSKBDD を省略して探索検分のジョブデータ定義の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索検分のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では PATHDISP=DELETE は「探索検分のジョブデータ定義に関係する定義値と表示行を照合する探索検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では PATHDISP=DELETE の属性行と IEF236I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明だけに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では PATHDISP=DELETE を JCL DD 文の運用手順で確認し、初出名は探索検分初出です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 復旧確認のジョブデータ定義で PATHDISP=DELETE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PATHDISP=DELETE の出力を取らず復旧確認のジョブデータ定義の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 ✅
    - C. ST OSKBDD を省略して復旧確認のジョブデータ定義の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のジョブデータ定義へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認のジョブデータ定義において選択記号 B を採用し、識別名は復旧確認です。復旧確認のジョブデータ定義において PATHDISP=DELETE は説明欄の「復旧確認のジョブデータ定義に関係する定義値と表示行を照合する復旧確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認のジョブデータ定義の証跡を読む担当者は、PATHDISP=DELETE の属性行と IEF236I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHDISP=DELETE の根拠にならないため復旧確認ではありません。復旧確認のジョブデータ定義に出る PATHDISP=DELETE は JCL DD 文の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **PATHDISP=DELETE**

    - 検証目的: 復旧照合のジョブデータ定義について、ステップ終了時にファイルを削除 (正常終了)。「PATHDISP=DELETE」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030038の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧照合のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHDISP=DELETEを指定し、OSKB030038の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHDISP=DELETE
    CASE OSKB030038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHDISP=DELETE
    CASE OSKB030038
    SOURCE z/OS JCL
    ```

    PATHDISP=DELETEとOSKB030038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030038を同じ出力で読み、復旧照合のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030038
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030038
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030038.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030038 STEP1 SYSUT1
    ```

    IEF236IとOSKB030038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHDISP=DELETE と OSKB030038 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PATHDISP=DELETE**

    - 検証目的: 構文検査のジョブデータ定義について、ステップ終了時にファイルを削除 (正常終了)。「PATHDISP=DELETE」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHDISP=DELETEを指定し、OSKB020061の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHDISP=DELETE
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHDISP=DELETE
    CASE OSKB020061
    SOURCE z/OS JCL
    ```

    PATHDISP=DELETEとOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020061を同じ出力で読み、構文検査のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020061
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020061.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020061 STEP1 SYSUT1
    ```

    IEF236IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHDISP=DELETE と OSKB020061 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHDISP=KEEP {#c17-i0183}
*分類: USS-PATH*  ・  難易度: 中級

PATHDISP=KEEPは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 終端検分のジョブデータ定義に関係する PATHDISP=KEEP の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検分で再確認できる形にする。 ✅
    - B. PATHDISP=KEEP の名称と担当者名だけを残して終端検分のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で終端検分のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず終端検分のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では PATHDISP=KEEP は「PATHDISP=KEEP の用途をジョブデータ定義の表示で確認する終端検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景ではz/OS JCL の PATHDISP=KEEP と IEF236I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明だけに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では PATHDISP=KEEP を JCL DD 文で扱う確認対象とし、用語名は終端検分用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 警告確認のジョブデータ定義に関係する PATHDISP=KEEP の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 ✅
    - B. PATHDISP=KEEP の名称と担当者名のみを残して警告確認のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で警告確認のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告確認のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認のジョブデータ定義において選択記号 A を採用し、識別名は警告確認です。警告確認のジョブデータ定義において PATHDISP=KEEP は説明欄の「PATHDISP=KEEP の用途をジョブデータ定義の表示で確認する警告確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のジョブデータ定義に関連して、z/OS JCL では PATHDISP=KEEP の表示属性と IEF236I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHDISP=KEEP の根拠にならないため警告確認ではありません。 D: 警告確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため警告確認ではありません。警告確認のジョブデータ定義で使う PATHDISP=KEEP という用語は JCL DD 文で扱う確認対象であり、用語名は警告確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHDISP=KEEP**

    - 検証目的: 変更追跡のジョブデータ定義について、PATHDISP=KEEP は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHDISP=KEEPを指定し、OSKB020060の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHDISP=KEEP
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHDISP=KEEP
    CASE OSKB020060
    SOURCE z/OS JCL
    ```

    PATHDISP=KEEPとOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020060を同じ出力で読み、変更追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020060
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020060.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020060 STEP1 SYSUT1
    ```

    IEF236IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHDISP=KEEP と OSKB020060 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHMODE 8 進指定 {#c17-i0184}
*分類: USS-PATH*  ・  難易度: 中級

OCREAT 時のパーミッションを 8 進で指定 (例: 0755)。「PATHMODE 8 進指定」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 呼出検分の進指定でジョブデータ定義の運用確認を行います。PATHMODE 8 進指定の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で呼出検分の進指定を確認した扱いにする。
    - B. IEF236I の有無を確認せず呼出検分の進指定を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出検分の確認にする。 ✅
    - D. PATHMODE 8 進指定の属性行を読まず呼出検分の進指定の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では PATHMODE 8 進指定 は「z/OS JCL で PATHMODE 8 進指定の扱いを記録する呼出検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では PATHMODE 8 進指定の表示結果と IEF236I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明だけに寄り、判定名は呼出検分不足です。呼出検分資料では PATHMODE 8 進指定の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 順序確認の進指定でジョブデータ定義の運用確認を行います。PATHMODE 8 進指定の根拠にできる作業はどれですか。

    - A. z/OS JCL と無関係な一覧で順序確認の進指定を確認した扱いにする。
    - B. IEF236I の有無を確認せず順序確認の進指定を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序確認の記録として扱う。 ✅
    - D. PATHMODE 8 進指定の属性行を読まず順序確認の進指定の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認の進指定において選択記号 C を採用し、識別名は順序確認です。順序確認の進指定において PATHMODE 8 進指定 は説明欄の「z/OS JCL で PATHMODE 8 進指定の扱いを記録する順序確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の進指定を受け取る担当者は、PATHMODE 8 進指定の表示結果と IEF236I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の進指定は別カテゴリの確認を流用しており、PATHMODE 8 進指定の根拠にならないため順序確認ではありません。 B: 順序確認の進指定は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため順序確認ではありません。 C: 順序確認の進指定は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の進指定は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の進指定が示す PATHMODE 8 進指定は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHMODE 8 進指定**

    - 検証目的: 復旧追跡の進指定について、OCREAT 時のパーミッションを 8 進で指定 (例: 0755)。「PATHMODE 8 進指定」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、復旧追跡の進指定の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHMODE 8 進指定を指定し、OSKB020058の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHMODE 8 進指定
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHMODE 8 進指定
    CASE OSKB020058
    SOURCE z/OS JCL
    ```

    PATHMODE 8 進指定とOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020058を同じ出力で読み、復旧追跡の進指定の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020058
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020058.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020058 STEP1 SYSUT1
    ```

    IEF236IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHMODE 8 進指定 と OSKB020058 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHMODE 記号指定 {#c17-i0185}
*分類: USS-PATH*  ・  難易度: 中級

PATHMODE 記号指定は、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。PATHMODE=(SIRUSR,SIWUSR,...) で記号定数を列挙する形式。「PATHMODE 記号指定」は割り当て結果を調べるとき、DISP、UNIT、SPACE、DCB など周辺指定との組み合わせで確認する

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 置換検分の記号指定に関する PATHMODE 記号指定の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず置換検分の記号指定の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換検分の記号指定の証跡として保存して根拠にする。
    - C. PATHMODE 記号指定の変更点を出力本文から切り離して置換検分の記号指定の承認欄だけ残す。
    - D. z/OS JCL の表示形式に沿って根拠行を採り、置換検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では PATHMODE 記号指定 は「PATHMODE 記号指定の状態と出力メッセージを結び付ける置換検分項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では PATHMODE 記号指定の出力行と IEF236I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明だけに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では PATHMODE 記号指定をz/OS JCL の確認記録に残し、対象名は置換検分対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 値域確認の記号指定に関する PATHMODE 記号指定の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域確認の記号指定の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の記号指定の証跡として保存して根拠にする。
    - C. PATHMODE 記号指定の変更点を出力本文から切り離して値域確認の記号指定の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認の記号指定において選択記号 D を採用し、識別名は値域確認です。値域確認の記号指定において PATHMODE 記号指定 は説明欄の「PATHMODE 記号指定の状態と出力メッセージを結び付ける値域確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の記号指定に関する記録は、PATHMODE 記号指定の出力行と IEF236I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の記号指定は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため値域確認ではありません。 B: 値域確認の記号指定は別カテゴリの確認を流用しており、PATHMODE 記号指定の根拠にならないため値域確認ではありません。 C: 値域確認の記号指定は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の記号指定は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の記号指定で記録する PATHMODE 記号指定はz/OS JCL の確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHMODE 記号指定**

    - 検証目的: 監査追跡の記号指定について、PATHMODE 記号指定は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。PATHMODE=(SIRUSR,SIWUSR,などに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、監査追跡の記号指定の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHMODE 記号指定を指定し、OSKB020059の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHMODE 記号指定
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHMODE 記号指定
    CASE OSKB020059
    SOURCE z/OS JCL
    ```

    PATHMODE 記号指定とOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020059を同じ出力で読み、監査追跡の記号指定の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020059
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020059.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020059 STEP1 SYSUT1
    ```

    IEF236IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHMODE 記号指定 と OSKB020059 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=OAPPEND {#c17-i0186}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=OAPPENDは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS JCL Reference、z/OS MVS JCL User's Guide を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 値域読解のジョブデータ定義に関する PATHOPTS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず値域読解のジョブデータ定義の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域読解のジョブデータ定義の証跡として保存して根拠にする。
    - C. PATHOPTS 属性の変更点を出力本文から切り離して値域読解のジョブデータ定義の承認欄だけ残す。
    - D. IEF236I を含む表示を保存し、説明欄との差分を値域読解で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では PATHOPTS 属性 は「PATHOPTS 属性の状態と出力メッセージを結び付ける値域読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では PATHOPTS 属性の出力行と IEF236I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明だけに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では PATHOPTS 属性をz/OS JCL の確認記録に残し、対象名は値域読解対象です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 出力確認のジョブデータ定義に関する PATHOPTS=OAPPEND の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBDD の結果を残さず出力確認のジョブデータ定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のジョブデータ定義の証跡として保存して根拠にする。
    - C. PATHOPTS=OAPPEND の変更点を出力本文から切り離して出力確認のジョブデータ定義の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認のジョブデータ定義において選択記号 D を採用し、識別名は出力確認です。出力確認のジョブデータ定義において PATHOPTS=OAPPEND は説明欄の「PATHOPTS=OAPPEND の状態と出力メッセージを結び付ける出力確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認のジョブデータ定義に関する記録は、PATHOPTS=OAPPEND の出力行と IEF236I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため出力確認ではありません。 B: 出力確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=OAPPEND の根拠にならないため出力確認ではありません。 C: 出力確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認のジョブデータ定義で記録する PATHOPTS=OAPPEND はz/OS JCL の確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（2件）"
    **PATHOPTS=OAPPEND**

    - 検証目的: 値域照合のジョブデータ定義について、PATHOPTS=OAPPEND は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030036の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、値域照合のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OAPPENDを指定し、OSKB030036の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OAPPEND
    CASE OSKB030036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OAPPEND
    CASE OSKB030036
    SOURCE z/OS JCL
    ```

    PATHOPTS=OAPPENDとOSKB030036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB030036を同じ出力で読み、値域照合のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB030036
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB030036
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB030036.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB030036 STEP1 SYSUT1
    ```

    IEF236IとOSKB030036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OAPPEND と OSKB030036 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB030036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PATHOPTS=OAPPEND**

    - 検証目的: 範囲追跡のジョブデータ定義について、PATHOPTS=OAPPEND は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、範囲追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OAPPENDを指定し、OSKB020051の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OAPPEND
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OAPPEND
    CASE OSKB020051
    SOURCE z/OS JCL
    ```

    PATHOPTS=OAPPENDとOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020051を同じ出力で読み、範囲追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020051
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020051.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020051 STEP1 SYSUT1
    ```

    IEF236IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OAPPEND と OSKB020051 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



### PATHOPTS=OCREAT {#c17-i0187}
*分類: USS-PATH*  ・  難易度: 中級

PATHOPTS=OCREATは、JCL DD 文のUSS-PATHで機能名、見出し、または確認対象として参照する項目です。存在しなければ作成。PATHMODE と組み合わせる。「PATHOPTS=OCREAT」を読むと、プログラムが参照する DD 名と、実際に割り当てられるデータセットや装置の関係を追いやすい

**出典:** z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

??? question "確認問題（2問）"
    **問題.** 警告読解のジョブデータ定義に関係する PATHOPTS=OCREAT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBDD の結果から対象行を抜き出し、警告読解の証跡として残す。 ✅
    - B. PATHOPTS=OCREAT の名称と担当者名だけを残して警告読解のジョブデータ定義の表示本文を対象から外す。
    - C. ジョブデータ定義以外の画面で警告読解のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず警告読解のジョブデータ定義の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では PATHOPTS=OCREAT は「PATHOPTS=OCREAT の用途をジョブデータ定義の表示で確認する警告読解項目」と ST OSKBDD または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景ではz/OS JCL の PATHOPTS=OCREAT と IEF236I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明だけに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では PATHOPTS=OCREAT を JCL DD 文で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800

    ---

    **問題.** 条件確認のジョブデータ定義に関係する PATHOPTS=OCREAT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 ✅
    - B. PATHOPTS=OCREAT の名称と担当者名のみを残して条件確認のジョブデータ定義の表示本文を確認対象に含めない。
    - C. ジョブデータ定義以外の画面で条件確認のジョブデータ定義を確認し同じ証跡として扱ったことにする。
    - D. IEF236I の有無を見ず条件確認のジョブデータ定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認のジョブデータ定義において選択記号 A を採用し、識別名は条件確認です。条件確認のジョブデータ定義において PATHOPTS=OCREAT は説明欄の「PATHOPTS=OCREAT の用途をジョブデータ定義の表示で確認する条件確認項目」と ST OSKBDD または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のジョブデータ定義に関連して、z/OS JCL では PATHOPTS=OCREAT の表示属性と IEF236I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のジョブデータ定義は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のジョブデータ定義は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のジョブデータ定義は別カテゴリの確認を流用しており、PATHOPTS=OCREAT の根拠にならないため条件確認ではありません。 D: 条件確認のジョブデータ定義は戻り値や記録番号に寄り、IEF236I や属性表示を落とすため条件確認ではありません。条件確認のジョブデータ定義で使う PATHOPTS=OCREAT という用語は JCL DD 文で扱う確認対象であり、用語名は条件確認です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600） / zOS31_ieam800


??? note "検証手順（1件）"
    **PATHOPTS=OCREAT**

    - 検証目的: 優先追跡のジョブデータ定義について、PATHOPTS=OCREAT は、JCL DD 文の USS-PATH で機能名、見出し、または確認対象として参照する項目です。存在しなければ作成。PATHMODE と組み合わに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBDDを実行し、IEF236Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBDD を入力し、優先追跡のジョブデータ定義の確認表示へ進みます。
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
    現在の画面はSDSFの表示結果です。FIND欄にPATHOPTS=OCREATを指定し、OSKB020052の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PATHOPTS=OCREAT
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PATHOPTS=OCREAT
    CASE OSKB020052
    SOURCE z/OS JCL
    ```

    PATHOPTS=OCREATとOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEF236IとOSKB020052を同じ出力で読み、優先追跡のジョブデータ定義の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBDD
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    JESJCL FOR JOB OSKB020052
    //STEP1   EXEC PGM=IEFBR14
    //SYSUT1  DD DSN=OSKB020052.DATA,DISP=SHR
    IEF236I ALLOC. FOR OSKB020052 STEP1 SYSUT1
    ```

    IEF236IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBDD が画面・出力に表示されること
    ② ステップ2 の PATHOPTS=OCREAT と OSKB020052 が画面・出力に表示されること
    ③ ステップ3 の IEF236I と OSKB020052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide



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


