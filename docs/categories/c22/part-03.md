---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (3/4)

[← MVS オペレータコマンド の概要へ戻る](index.md)


## MVS オペレータコマンド > JES2

### $D A 活動状況 {#c22-i0187}
*分類: JES2*  ・  難易度: 中級

$D A 活動状況は、JES2 イニシエータの活動状況、各クラスの稼動ジョブ一覧を表示する JES2 コマンド (MVS コマンドではなく JES2 サブコマンド)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切判定の$ 活動状況で$D A 活動状況の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. $D A 活動状況の出力を取らず区切判定の$ 活動状況の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切判定の確認結果にする。 ✅
    - C. D A,L を省略して区切判定の$ 活動状況の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の$ 活動状況へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定の$ 活動状況において選択記号 B を採用し、識別名は区切判定です。区切判定の$ 活動状況において$D A 活動状況 は説明欄の「区切判定の$ 活動状況に関係する定義値と表示行を照合する区切判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切判定です。区切判定の$ 活動状況の証跡を読む担当者は、$D A 活動状況の属性行と IEE115I を合わせて追跡し、背景名は区切判定です。誤答側の問題点を分けます。 A: 区切判定の$ 活動状況は名称や説明のみに寄り、状態を示す出力本文が不足するため区切判定ではありません。 B: 区切判定の$ 活動状況は対象出力と項目説明を結び、根拠を残すので区切判定です。 C: 区切判定の$ 活動状況は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切判定ではありません。 D: 区切判定の$ 活動状況は別カテゴリの確認を流用しており、$D A 活動状況の根拠にならないため区切判定ではありません。区切判定の$ 活動状況に出る$D A 活動状況は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **$D A 活動状況**

    - 検証目的: 呼出検査の$ 活動状況について、$D A 活動状況は、JES2 イニシエータの活動状況、各クラスの稼動ジョブ一覧を表示する JES2 コマンド (MVS コマンドではなく JES2 サブコマンド)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030063の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出検査の$ 活動状況の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に$D A 活動状況を指定し、OSKB030063の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND $D A 活動状況
    CASE OSKB030063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM $D A 活動状況
    CASE OSKB030063
    SOURCE z/OS MVS Operations
    ```

    $D A 活動状況とOSKB030063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030063を同じ出力で読み、呼出検査の$ 活動状況の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030063
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030063 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030063   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の $D A 活動状況 と OSKB030063 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### $D Q キュー状況 {#c22-i0188}
*分類: JES2*  ・  難易度: 中級

$D Q キュー状況は、MVS オペレータコマンドのJES2で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 範囲判定の$ キュー状況で操作コマンドの運用確認を行います。$D Q キュー状況の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲判定の$ キュー状況を確認した扱いにする。
    - B. IEE115I の有無を確認せず範囲判定の$ キュー状況を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲判定の記録として扱う。 ✅
    - D. $D Q キュー状況の属性行を読まず範囲判定の$ キュー状況の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定の$ キュー状況において選択記号 C を採用し、識別名は範囲判定です。範囲判定の$ キュー状況において$D Q キュー状況 は説明欄の「z/OS MVS Operationsで$D Q キュー状況の扱いを記録する範囲判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲判定です。範囲判定の$ キュー状況を受け取る担当者は、$D Q キュー状況の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲判定です。不適切な選択肢を整理します。 A: 範囲判定の$ キュー状況は別カテゴリの確認を流用しており、$D Q キュー状況の根拠にならないため範囲判定ではありません。 B: 範囲判定の$ キュー状況は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲判定ではありません。 C: 範囲判定の$ キュー状況は対象出力と項目説明を結び、根拠を残すので範囲判定です。 D: 範囲判定の$ キュー状況は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲判定ではありません。範囲判定の$ キュー状況が示す$D Q キュー状況は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **$D Q キュー状況**

    - 検証目的: 置換検査の$ キュー状況について、$D Q キュー状況は、MVS オペレータコマンドの JES2 で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030064の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換検査の$ キュー状況の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に$D Q キュー状況を指定し、OSKB030064の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND $D Q キュー状況
    CASE OSKB030064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM $D Q キュー状況
    CASE OSKB030064
    SOURCE z/OS MVS Operations
    ```

    $D Q キュー状況とOSKB030064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030064を同じ出力で読み、置換検査の$ キュー状況の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030064
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030064 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030064   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の $D Q キュー状況 と OSKB030064 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### $P JES2 ドレイン {#c22-i0189}
*分類: JES2*  ・  難易度: 中級

$P JES2 ドレインは、MVS オペレータコマンドのJES2で確認する項目です。JES2 の新規受付を停止しドレインさせる。Z EOD 前に投入する典型シーケンス

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先判定の$ ドレインに関する$P JES2 ドレインの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先判定の$ ドレインの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の$ ドレインの証跡として保存して根拠にする。
    - C. $P JES2 ドレインの変更点を出力本文から切り離して優先判定の$ ドレインの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定の$ ドレインにおいて選択記号 D を採用し、識別名は優先判定です。優先判定の$ ドレインにおいて$P JES2 ドレイン は説明欄の「$P JES2 ドレインの状態と出力メッセージを結び付ける優先判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先判定です。優先判定の$ ドレインに関する記録は、$P JES2 ドレインの出力行と IEE115I を一緒に保存し、背景名は優先判定です。選択肢ごとの違いを示します。 A: 優先判定の$ ドレインは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先判定ではありません。 B: 優先判定の$ ドレインは別カテゴリの確認を流用しており、$P JES2 ドレインの根拠にならないため優先判定ではありません。 C: 優先判定の$ ドレインは名称や説明のみに寄り、状態を示す出力本文が不足するため優先判定ではありません。 D: 優先判定の$ ドレインは対象出力と項目説明を結び、根拠を残すので優先判定です。優先判定の$ ドレインで記録する$P JES2 ドレインはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **$P JES2 ドレイン**

    - 検証目的: 終端検査の$ ドレインについて、$P JES2 ドレインは、MVS オペレータコマンドの JES2 で確認する項目です。JES2 の新規受付を停止しドレインさせる。Z EOD 前に投入する典型シーケンスに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030065の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端検査の$ ドレインの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に$P JES2 ドレインを指定し、OSKB030065の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND $P JES2 ドレイン
    CASE OSKB030065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM $P JES2 ドレイン
    CASE OSKB030065
    SOURCE z/OS MVS Operations
    ```

    $P JES2 ドレインとOSKB030065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030065を同じ出力で読み、終端検査の$ ドレインの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030065
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030065 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030065   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の $P JES2 ドレイン と OSKB030065 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > K

### K A,NONE ロール解除 {#c22-i0190}
*分類: K*  ・  難易度: 中級

K A,NONE ロール解除は、MVS オペレータコマンドのKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 呼出判定のロール解除で操作コマンドの運用確認を行います。K A,NONE ロール解除の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出判定のロール解除を確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出判定のロール解除を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出判定の記録として扱う。 ✅
    - D. K A,NONE ロール解除の属性行を読まず呼出判定のロール解除の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出判定のロール解除において選択記号 C を採用し、識別名は呼出判定です。呼出判定のロール解除において K A,NONE ロール解除 は説明欄の「z/OS MVS Operationsで K A,NONE ロール解除の扱いを記録する呼出判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出判定です。呼出判定のロール解除を受け取る担当者は、K A,NONE ロール解除の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出判定です。不適切な選択肢を整理します。 A: 呼出判定のロール解除は別カテゴリの確認を流用しており、K A,NONE ロール解除の根拠にならないため呼出判定ではありません。 B: 呼出判定のロール解除は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出判定ではありません。 C: 呼出判定のロール解除は対象出力と項目説明を結び、根拠を残すので呼出判定です。 D: 呼出判定のロール解除は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出判定ではありません。呼出判定のロール解除が示す K A,NONE ロール解除は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **K A,NONE ロール解除**

    - 検証目的: 値域追跡のロール解除について、K A,NONE ロール解除は、MVS オペレータコマンドの K で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030056の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域追跡のロール解除の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にK A,NONE ロール解除を指定し、OSKB030056の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND K A,NONE ロール解除
    CASE OSKB030056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM K A,NONE ロール解除
    CASE OSKB030056
    SOURCE z/OS MVS Operations
    ```

    K A,NONE ロール解除とOSKB030056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030056を同じ出力で読み、値域追跡のロール解除の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030056
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030056 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030056   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の K A,NONE ロール解除 と OSKB030056 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### K E,D 削除 {#c22-i0191}
*分類: K*  ・  難易度: 中級

K E,D 削除は、MVS オペレータコマンドのKで確認する項目です。K E,D で表示メッセージを消去 (Erase) する形式。視認性を上げるための運用補助

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文判定の削除に関係する K E,D 削除の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文判定として残す。 ✅
    - B. K E,D 削除の名称と担当者名のみを残して構文判定の削除の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で構文判定の削除を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文判定の削除の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定の削除において選択記号 A を採用し、識別名は構文判定です。構文判定の削除において K E,D 削除 は説明欄の「K E,D 削除の用途を操作コマンドの表示で確認する構文判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文判定です。構文判定の削除に関連して、z/OS MVS Operationsでは K E,D 削除の表示属性と IEE115I を同じ証跡に残し、背景名は構文判定です。他の選択肢を確認します。 A: 構文判定の削除は対象出力と項目説明を結び、根拠を残すので構文判定です。 B: 構文判定の削除は名称や説明のみに寄り、状態を示す出力本文が不足するため構文判定ではありません。 C: 構文判定の削除は別カテゴリの確認を流用しており、K E,D 削除の根拠にならないため構文判定ではありません。 D: 構文判定の削除は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文判定ではありません。構文判定の削除で使う K E,D 削除という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **K E,D 削除**

    - 検証目的: 比較追跡の削除について、K E,D 削除は、MVS オペレータコマンドの K で確認する項目です。K E,D で表示メッセージを消去 (Erase) する形式。視認性を上げるための運用補助に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030054の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較追跡の削除の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にK E,D 削除を指定し、OSKB030054の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND K E,D 削除
    CASE OSKB030054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM K E,D 削除
    CASE OSKB030054
    SOURCE z/OS MVS Operations
    ```

    K E,D 削除とOSKB030054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030054を同じ出力で読み、比較追跡の削除の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030054
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030054 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030054   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の K E,D 削除 と OSKB030054 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### K M,REF メッセージ再表示 {#c22-i0192}
*分類: K*  ・  難易度: 中級

K M,REF メッセージ再表示は、MVS オペレータコマンドのKで確認する項目です。K M,REF で未応答 WTOR / アクション・メッセージを再描画する。流れ去ったメッセージの確認に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更検査のメッセージ再表示に関する K M,REF メッセージ再表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更検査のメッセージ再表示の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査のメッセージ再表示の証跡として保存して根拠にする。
    - C. K M,REF メッセージ再表示の変更点を出力本文から切り離して変更検査のメッセージ再表示の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査のメッセージ再表示において選択記号 D を採用し、識別名は変更検査です。変更検査のメッセージ再表示において K M,REF メッセージ再表示 は説明欄の「K M,REF メッセージ再表示の状態と出力メッセージを結び付ける変更検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査のメッセージ再表示に関する記録は、K M,REF メッセージ再表示の出力行と IEE115I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査のメッセージ再表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更検査ではありません。 B: 変更検査のメッセージ再表示は別カテゴリの確認を流用しており、K M,REF メッセージ再表示の根拠にならないため変更検査ではありません。 C: 変更検査のメッセージ再表示は名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査のメッセージ再表示は対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査のメッセージ再表示で記録する K M,REF メッセージ再表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **K M,REF メッセージ再表示**

    - 検証目的: 記録追跡のメッセージ再表示について、K M,REF メッセージ再表示は、MVS オペレータコマンドの K で確認する項目です。K M,REF で未応答 WTOR / アクション・メッセージを再描画する。流れ去ったに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030053の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録追跡のメッセージ再表示の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にK M,REF メッセージ再表示を指定し、OSKB030053の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND K M,REF メッセージ再表示
    CASE OSKB030053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM K M,REF メッセージ再表示
    CASE OSKB030053
    SOURCE z/OS MVS Operations
    ```

    K M,REF メッセージ再表示とOSKB030053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030053を同じ出力で読み、記録追跡のメッセージ再表示の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030053
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030053 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030053   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の K M,REF メッセージ再表示 と OSKB030053 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### K N,PFK=(xx) PFK 切替 {#c22-i0193}
*分類: K*  ・  難易度: 中級

K N,PFK=(xx) PFK 切替は、MVS オペレータコマンドのKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 展開判定の切替で K N,PFK=(xx) PFK 切替の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. K N,PFK=(xx) PFK 切替の出力を取らず展開判定の切替の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開判定の確認結果にする。 ✅
    - C. D A,L を省略して展開判定の切替の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の切替へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定の切替において選択記号 B を採用し、識別名は展開判定です。展開判定の切替において K N,PFK=(xx) PFK 切替 は説明欄の「展開判定の切替に関係する定義値と表示行を照合する展開判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開判定です。展開判定の切替の証跡を読む担当者は、K N,PFK=(xx) PFK 切替の属性行と IEE115I を合わせて追跡し、背景名は展開判定です。誤答側の問題点を分けます。 A: 展開判定の切替は名称や説明のみに寄り、状態を示す出力本文が不足するため展開判定ではありません。 B: 展開判定の切替は対象出力と項目説明を結び、根拠を残すので展開判定です。 C: 展開判定の切替は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開判定ではありません。 D: 展開判定の切替は別カテゴリの確認を流用しており、K N,PFK=(xx) PFK 切替の根拠にならないため展開判定ではありません。展開判定の切替に出る K N,PFK=(xx) PFK 切替は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **K N,PFK=(xx) PFK 切替**

    - 検証目的: 順序追跡の切替について、K N,PFK=(xx) PFK 切替は、MVS オペレータコマンドの K で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030055の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序追跡の切替の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にK N,PFK=(xx) PFK 切を指定し、OSKB030055の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND K N,PFK=(xx) PFK 切
    CASE OSKB030055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM K N,PFK=(xx) PFK 切
    CASE OSKB030055
    SOURCE z/OS MVS Operations
    ```

    K N,PFK=(xx) PFK 切とOSKB030055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030055を同じ出力で読み、順序追跡の切替の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030055
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030055 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030055   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の K N,PFK=(xx) PFK 切 と OSKB030055 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### K S,DEL=... {#c22-i0194}
*分類: K*  ・  難易度: 中級

MVS オペレータコマンドのKでは、対象資源、指定値、実行時の出力を対応付けて確認します。Kは、MVS オペレータコマンドの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、K S,DEL=...の表記と許可される値を確認します。

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査検査のなどで操作コマンドの運用確認を行います。K S,DEL= などの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査検査のなどを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査検査のなどを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査検査の記録として扱う。 ✅
    - D. K S,DEL= などの属性行を読まず監査検査のなどの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査のなどにおいて選択記号 C を採用し、識別名は監査検査です。監査検査のなどにおいて K S,DEL= など は説明欄の「z/OS MVS Operationsで K S,DEL= などの扱いを記録する監査検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査検査です。監査検査のなどを受け取る担当者は、K S,DEL= などの表示結果と IEE115I を同じ確認単位として扱い、背景名は監査検査です。不適切な選択肢を整理します。 A: 監査検査のなどは別カテゴリの確認を流用しており、K S,DEL= などの根拠にならないため監査検査ではありません。 B: 監査検査のなどは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査検査ではありません。 C: 監査検査のなどは対象出力と項目説明を結び、根拠を残すので監査検査です。 D: 監査検査のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため監査検査ではありません。監査検査のなどが示す K S,DEL= などは出典欄の資料で使い方を追跡できる項目であり、用語名は監査検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200



### K コマンド基本 {#c22-i0195}
*分類: K*  ・  難易度: 初級

K コマンド基本は、MVS オペレータコマンドのKで確認する項目です。CONTROL コマンドの 1 字省略形。コンソール属性の動的変更 (PFK、ROLL、RNUM、M REF 等) に用いる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧検査のコマンド基本で K コマンド基本の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. K コマンド基本の出力を取らず復旧検査のコマンド基本の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧検査の確認結果にする。 ✅
    - C. D A,L を省略して復旧検査のコマンド基本の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査のコマンド基本へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧検査のコマンド基本において選択記号 B を採用し、識別名は復旧検査です。復旧検査のコマンド基本において K コマンド基本 は説明欄の「復旧検査のコマンド基本に関係する定義値と表示行を照合する復旧検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧検査です。復旧検査のコマンド基本の証跡を読む担当者は、K コマンド基本の属性行と IEE115I を合わせて追跡し、背景名は復旧検査です。誤答側の問題点を分けます。 A: 復旧検査のコマンド基本は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧検査ではありません。 B: 復旧検査のコマンド基本は対象出力と項目説明を結び、根拠を残すので復旧検査です。 C: 復旧検査のコマンド基本は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧検査ではありません。 D: 復旧検査のコマンド基本は別カテゴリの確認を流用しており、K コマンド基本の根拠にならないため復旧検査ではありません。復旧検査のコマンド基本に出る K コマンド基本は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **K コマンド基本**

    - 検証目的: 範囲追跡のコマンド基本について、K コマンド基本は、MVS オペレータコマンドの K で確認する項目です。CONTROL コマンドの 1 字省略形。コンソール属性の動的変更 (PFK、ROLL、RNUM、Mに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030051の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲追跡のコマンド基本の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にK コマンド基本を指定し、OSKB030051の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND K コマンド基本
    CASE OSKB030051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM K コマンド基本
    CASE OSKB030051
    SOURCE z/OS MVS Operations
    ```

    K コマンド基本とOSKB030051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030051を同じ出力で読み、範囲追跡のコマンド基本の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030051
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030051 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030051   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の K コマンド基本 と OSKB030051 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > LOG

### LOG OPERLOG (LOG 'text') {#c22-i0196}
*分類: LOG*  ・  難易度: 中級

LOG 'text' で SYSLOG / OPERLOG に任意コメントを記録する。運用作業ログを残す目的で使用

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 探索追跡の操作コマンドで LOG OPERLOG (LOG 'text')の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LOG OPERLOG (LOG 'text')の出力を取らず探索追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 ✅
    - C. D A,L を省略して探索追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡の操作コマンドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の操作コマンドにおいて LOG OPERLOG (LOG 'text') は説明欄の「探索追跡の操作コマンドに関係する定義値と表示行を照合する探索追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の操作コマンドの証跡を読む担当者は、LOG OPERLOG (LOG 'text')の属性行と IEE115I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の操作コマンドは別カテゴリの確認を流用しており、LOG OPERLOG (LOG 'text')の根拠にならないため探索追跡ではありません。探索追跡の操作コマンドに出る LOG OPERLOG (LOG 'text')は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **LOG OPERLOG (LOG 'text')**

    - 検証目的: 監査確認の操作コマンドについて、LOG 'text' で SYSLOG / OPERLOG に任意コメントを記録する。運用作業ログを残す目的で使用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030019の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLOG OPERLOG (LOG 'を指定し、OSKB030019の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LOG OPERLOG (LOG '
    CASE OSKB030019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LOG OPERLOG (LOG '
    CASE OSKB030019
    SOURCE z/OS MVS Operations
    ```

    LOG OPERLOG (LOG 'とOSKB030019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030019を同じ出力で読み、監査確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030019
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030019 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030019   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の LOG OPERLOG (LOG ' と OSKB030019 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### LOG コマンドの権限 {#c22-i0197}
*分類: LOG*  ・  難易度: 中級

発行コンソールの AUTH レベルに依存。LOG 自体はマスタ権限不要だが SYSLOG/OPERLOG の保護対象設定を確認すべき

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 上書追跡のコマンドの権限で操作コマンドの運用確認を行います。LOG コマンドの権限の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書追跡のコマンドの権限を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書追跡のコマンドの権限を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. LOG コマンドの権限の属性行を読まず上書追跡のコマンドの権限の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のコマンドの権限において選択記号 C を採用し、識別名は上書追跡です。上書追跡のコマンドの権限において LOG コマンドの権限 は説明欄の「z/OS MVS Operationsで LOG コマンドの権限の扱いを記録する上書追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のコマンドの権限を受け取る担当者は、LOG コマンドの権限の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のコマンドの権限は別カテゴリの確認を流用しており、LOG コマンドの権限の根拠にならないため上書追跡ではありません。 B: 上書追跡のコマンドの権限は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のコマンドの権限は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のコマンドの権限は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のコマンドの権限が示す LOG コマンドの権限は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **LOG コマンドの権限**

    - 検証目的: 終端追跡のコマンドの権限について、発行コンソールの AUTH レベルに依存。LOG 自体はマスタ権限不要だが SYSLOG/OPERLOG の保護対象設定を確認すべきに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040045の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端追跡のコマンドの権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLOG コマンドの権限を指定し、OSKB040045の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LOG コマンドの権限
    CASE OSKB040045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LOG コマンドの権限
    CASE OSKB040045
    SOURCE z/OS MVS Operations
    ```

    LOG コマンドの権限とOSKB040045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040045を同じ出力で読み、終端追跡のコマンドの権限の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040045 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040045   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の LOG コマンドの権限 と OSKB040045 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **LOG コマンドの権限**

    - 検証目的: 変更確認のコマンドの権限について、発行コンソールの AUTH レベルに依存。LOG 自体はマスタ権限不要だが SYSLOG/OPERLOG の保護対象設定を確認すべきに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030020の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更確認のコマンドの権限の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にLOG コマンドの権限を指定し、OSKB030020の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND LOG コマンドの権限
    CASE OSKB030020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM LOG コマンドの権限
    CASE OSKB030020
    SOURCE z/OS MVS Operations
    ```

    LOG コマンドの権限とOSKB030020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030020を同じ出力で読み、変更確認のコマンドの権限の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030020
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030020 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030020   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の LOG コマンドの権限 と OSKB030020 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > MN

### MN JOBNAMES {#c22-i0198}
*分類: MN*  ・  難易度: 中級

MN JOBNAMESは、MVS オペレータコマンドのMNで確認する項目です。全ジョブの開始・終了時にメッセージを生成。ジョブ流れの自動化前提として活用

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 終端判定の操作コマンドに関係する MN JOBNAMES の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端判定として残す。 ✅
    - B. MN JOBNAMES の名称と担当者名のみを残して終端判定の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で終端判定の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端判定の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定の操作コマンドにおいて選択記号 A を採用し、識別名は終端判定です。終端判定の操作コマンドにおいて MN JOBNAMES は説明欄の「MN JOBNAMES の用途を操作コマンドの表示で確認する終端判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端判定です。終端判定の操作コマンドに関連して、z/OS MVS Operationsでは MN JOBNAMES の表示属性と IEE115I を同じ証跡に残し、背景名は終端判定です。他の選択肢を確認します。 A: 終端判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端判定です。 B: 終端判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端判定ではありません。 C: 終端判定の操作コマンドは別カテゴリの確認を流用しており、MN JOBNAMES の根拠にならないため終端判定ではありません。 D: 終端判定の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端判定ではありません。終端判定の操作コマンドで使う MN JOBNAMES という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **MN JOBNAMES**

    - 検証目的: 復旧追跡の操作コマンドについて、MN JOBNAMES は、MVS オペレータコマンドの MN で確認する項目です。全ジョブの開始・終了時にメッセージを生成。ジョブ流れの自動化前提として活用に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030058の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、復旧追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMN JOBNAMESを指定し、OSKB030058の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MN JOBNAMES
    CASE OSKB030058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MN JOBNAMES
    CASE OSKB030058
    SOURCE z/OS MVS Operations
    ```

    MN JOBNAMESとOSKB030058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030058を同じ出力で読み、復旧追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030058
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030058 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030058   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の MN JOBNAMES と OSKB030058 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### MN SESS {#c22-i0199}
*分類: MN*  ・  難易度: 中級

MN SESSは、MVS オペレータコマンドのMNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 上書判定の操作コマンドで操作コマンドの運用確認を行います。MN SESS の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書判定の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず上書判定の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書判定の記録として扱う。 ✅
    - D. MN SESS の属性行を読まず上書判定の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定の操作コマンドにおいて選択記号 C を採用し、識別名は上書判定です。上書判定の操作コマンドにおいて MN SESS は説明欄の「z/OS MVS Operationsで MN SESS の扱いを記録する上書判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書判定です。上書判定の操作コマンドを受け取る担当者は、MN SESS の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書判定です。不適切な選択肢を整理します。 A: 上書判定の操作コマンドは別カテゴリの確認を流用しており、MN SESS の根拠にならないため上書判定ではありません。 B: 上書判定の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書判定ではありません。 C: 上書判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書判定です。 D: 上書判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書判定ではありません。上書判定の操作コマンドが示す MN SESS は出典欄の資料で使い方を追跡できる項目であり、用語名は上書判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **MN SESS**

    - 検証目的: 変更追跡の操作コマンドについて、MN SESS は、MVS オペレータコマンドの MN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030060の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMN SESSを指定し、OSKB030060の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MN SESS
    CASE OSKB030060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MN SESS
    CASE OSKB030060
    SOURCE z/OS MVS Operations
    ```

    MN SESSとOSKB030060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030060を同じ出力で読み、変更追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030060
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030060 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030060   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の MN SESS と OSKB030060 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### MN STATUS {#c22-i0200}
*分類: MN*  ・  難易度: 中級

MN STATUSは、MVS オペレータコマンドのMNで確認する項目です。DD 文割当のたびに DSN を SYSLOG に記録する形式。データセット流出調査などで一時的に有効化

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 探索判定の操作コマンドで MN STATUS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MN STATUS の出力を取らず探索判定の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索判定の確認結果にする。 ✅
    - C. D A,L を省略して探索判定の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定の操作コマンドにおいて選択記号 B を採用し、識別名は探索判定です。探索判定の操作コマンドにおいて MN STATUS は説明欄の「探索判定の操作コマンドに関係する定義値と表示行を照合する探索判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索判定です。探索判定の操作コマンドの証跡を読む担当者は、MN STATUS の属性行と IEE115I を合わせて追跡し、背景名は探索判定です。誤答側の問題点を分けます。 A: 探索判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索判定ではありません。 B: 探索判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索判定です。 C: 探索判定の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索判定ではありません。 D: 探索判定の操作コマンドは別カテゴリの確認を流用しており、MN STATUS の根拠にならないため探索判定ではありません。探索判定の操作コマンドに出る MN STATUS は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **MN STATUS**

    - 検証目的: 監査追跡の操作コマンドについて、MN STATUS は、MVS オペレータコマンドの MN で確認する項目です。DD 文割当のたびに DSN を SYSLOG に記録する形式。データセット流出調査などで一時的にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030059の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMN STATUSを指定し、OSKB030059の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MN STATUS
    CASE OSKB030059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MN STATUS
    CASE OSKB030059
    SOURCE z/OS MVS Operations
    ```

    MN STATUSとOSKB030059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030059を同じ出力で読み、監査追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030059
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030059 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030059   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の MN STATUS と OSKB030059 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### MONITOR コマンド (MN) {#c22-i0201}
*分類: MN*  ・  難易度: 中級

MN コマンドは TSU LOGON/LOGOFF、JOB 開始/終了、データセット名表示などの監視メッセージ生成を切替える

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 置換判定のコマンドに関する MONITOR コマンド (MN)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず置換判定のコマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定のコマンドの証跡として保存して根拠にする。
    - C. MONITOR コマンド (MN)の変更点を出力本文から切り離して置換判定のコマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定のコマンドにおいて選択記号 D を採用し、識別名は置換判定です。置換判定のコマンドにおいて MONITOR コマンド (MN) は説明欄の「MONITOR コマンド (MN)の状態と出力メッセージを結び付ける置換判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換判定です。置換判定のコマンドに関する記録は、MONITOR コマンド (MN)の出力行と IEE115I を一緒に保存し、背景名は置換判定です。選択肢ごとの違いを示します。 A: 置換判定のコマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換判定ではありません。 B: 置換判定のコマンドは別カテゴリの確認を流用しており、MONITOR コマンド (MN)の根拠にならないため置換判定ではありません。 C: 置換判定のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換判定ではありません。 D: 置換判定のコマンドは対象出力と項目説明を結び、根拠を残すので置換判定です。置換判定のコマンドで記録する MONITOR コマンド (MN)はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **MONITOR コマンド (MN)**

    - 検証目的: 警告追跡のコマンドについて、MN コマンドは TSU LOGON/LOGOFF、JOB 開始/終了、データセット名表示などの監視メッセージ生成を切替えるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030057の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、警告追跡のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMONITOR コマンド (MN)を指定し、OSKB030057の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MONITOR コマンド (MN)
    CASE OSKB030057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MONITOR コマンド (MN)
    CASE OSKB030057
    SOURCE z/OS MVS Operations
    ```

    MONITOR コマンド (MN)とOSKB030057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030057を同じ出力で読み、警告追跡のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030057
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030057 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030057   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の MONITOR コマンド (MN) と OSKB030057 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P

### P コマンド基本構文 {#c22-i0202}
*分類: P*  ・  難易度: 初級

P コマンド基本構文は、MVS オペレータコマンドのPで状態表示や操作を行うためのコマンド関連項目です。P jobname または P identifier で STC を停止する。実体はサブシステムへの STOP 要求でサブシステム側がクリーンアップを行う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 記録検分のコマンド基本構文に関係する P コマンド基本構文の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、記録検分として引き継ぐ。 ✅
    - B. P コマンド基本構文の名称と担当者名だけを残して記録検分のコマンド基本構文の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録検分のコマンド基本構文を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録検分のコマンド基本構文の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では P コマンド基本構文 は「P コマンド基本構文の用途を操作コマンドの表示で確認する記録検分項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景ではz/OS MVS Operationsの P コマンド基本構文と IEE457I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明だけに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では P コマンド基本構文を MVS オペレータコマンドで扱う確認対象とし、用語名は記録検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **P コマンド基本構文**

    - 検証目的: 記録照合のコマンド基本構文について、P コマンド基本構文は、MVS オペレータコマンドの P で状態表示や操作を行うためのコマンド関連項目です。P jobname または P identifier で STC をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040033の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、記録照合のコマンド基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP コマンド基本構文を指定し、OSKB040033の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P コマンド基本構文
    CASE OSKB040033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P コマンド基本構文
    CASE OSKB040033
    SOURCE z/OS MVS Operations
    ```

    P コマンド基本構文とOSKB040033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040033を同じ出力で読み、記録照合のコマンド基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040033 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040033   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の P コマンド基本構文 と OSKB040033 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **P コマンド基本構文**

    - 検証目的: 出力検査のコマンド基本構文について、P コマンド基本構文は、MVS オペレータコマンドの P で状態表示や操作を行うためのコマンド関連項目です。P jobname または P identifier で STC をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力検査のコマンド基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP コマンド基本構文を指定し、OSKB020068の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P コマンド基本構文
    CASE OSKB020068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P コマンド基本構文
    CASE OSKB020068
    SOURCE z/OS MVS Operations
    ```

    P コマンド基本構文とOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020068を同じ出力で読み、出力検査のコマンド基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020068
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020068 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020068   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の P コマンド基本構文 と OSKB020068 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P APPC

### P APPC APPC/MVS 停止 {#c22-i0203}
*分類: P APPC*  ・  難易度: 中級

P APPC APPC/MVS 停止は、MVS オペレータコマンドのP APPCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査検分の・ 停止で操作コマンドの運用確認を行います。P APPC APPC 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査検分の・ 停止を確認した扱いにする。
    - B. IEE115I の有無を確認せず監査検分の・ 停止を正常終了として記録する。
    - C. IEE115I を含む表示を保存し、説明欄との差分を監査検分で確認する。 ✅
    - D. P APPC APPC 属性の属性行を読まず監査検分の・ 停止の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では P APPC APPC 属性 は「z/OS MVS Operationsで P APPC APPC 属性の扱いを記録する監査検分項目」と D A,L または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では P APPC APPC 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明だけに寄り、判定名は監査検分不足です。監査検分資料では P APPC APPC 属性の使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **P APPC APPC ・ MVS 停止**

    - 検証目的: 比較照合の・ 停止について、P APPC APPC/MVS 停止は、MVS オペレータコマンドの P APPC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較照合の・ 停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP APPC APPC ・ MVS を指定し、OSKB040034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P APPC APPC ・ MVS 
    CASE OSKB040034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P APPC APPC ・ MVS 
    CASE OSKB040034
    SOURCE z/OS MVS Operations
    ```

    P APPC APPC ・ MVS とOSKB040034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040034を同じ出力で読み、比較照合の・ 停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040034 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040034   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P APPC APPC ・ MVS  と OSKB040034 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **P APPC APPC ・ MVS 停止**

    - 検証目的: 比較検査の・ 停止について、P APPC APPC/MVS 停止は、MVS オペレータコマンドの P APPC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較検査の・ 停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP APPC APPC ・ MVS を指定し、OSKB020074の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P APPC APPC ・ MVS 
    CASE OSKB020074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P APPC APPC ・ MVS 
    CASE OSKB020074
    SOURCE z/OS MVS Operations
    ```

    P APPC APPC ・ MVS とOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020074を同じ出力で読み、比較検査の・ 停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020074
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020074 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020074   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P APPC APPC ・ MVS  と OSKB020074 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P CICS

### P CICS リージョン停止 {#c22-i0204}
*分類: P CICS*  ・  難易度: 上級

P CICS リージョン停止は、MVS オペレータコマンドのP CICSで用いるCICS リージョンを停止する。実体は CEMT 経由 PERFORM SHUTDOWN を呼び出す内部処理。P CICSでは、指定値と対象資源、実行時の出力を突き合わせて確認する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 値域検分のリージョン停止に関する P CICS リージョン停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域検分のリージョン停止の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域検分のリージョン停止の証跡として保存して根拠にする。
    - C. P CICS リージョン停止の変更点を出力本文から切り離して値域検分のリージョン停止の承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では P CICS リージョン停止 は「P CICS リージョン停止の状態と出力メッセージを結び付ける値域検分項目」と D A,L または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では P CICS リージョン停止の出力行と IEE115I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明だけに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では P CICS リージョン停止をz/OS MVS Operationsの確認記録に残し、対象名は値域検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P CICS リージョン停止**

    - 検証目的: 範囲検査のリージョン停止について、P CICS リージョン停止は、MVS オペレータコマンドの P CICS で用いる CICS リージョンを停止する。実体は CEMT 経由 PERFORM SHUTDOWN をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020071の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲検査のリージョン停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP CICS リージョン停止を指定し、OSKB020071の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P CICS リージョン停止
    CASE OSKB020071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P CICS リージョン停止
    CASE OSKB020071
    SOURCE z/OS MVS Operations
    ```

    P CICS リージョン停止とOSKB020071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020071を同じ出力で読み、範囲検査のリージョン停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020071
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020071 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020071   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P CICS リージョン停止 と OSKB020071 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P JES2

### P JES2 停止 {#c22-i0205}
*分類: P JES2*  ・  難易度: 中級

P JES2 停止は、MVS オペレータコマンドのP JES2で用いるJES2 サブシステムを停止する。スプール上の活性ジョブが残ると拒否されるため $P JES2 等で先に流す。P JES2では、指定値と対象資源、実行時の出力を突き合わせて確認する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 比較検分の停止で P JES2 停止の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. P JES2 停止の出力を取らず比較検分の停止の説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較検分の確認にする。 ✅
    - C. D A,L を省略して比較検分の停止の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較検分の停止へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では P JES2 停止 は「比較検分の停止に関係する定義値と表示行を照合する比較検分項目」と D A,L または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では P JES2 停止の属性行と IEE115I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明だけに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では P JES2 停止を MVS オペレータコマンドの運用手順で確認し、初出名は比較検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P JES2 停止**

    - 検証目的: 条件検査の停止について、P JES2 停止は、MVS オペレータコマンドの P JES2 で用いる JES2 サブシステムを停止する。スプール上の活性ジョブが残ると拒否されるため $P JES2 等で先に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件検査の停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP JES2 停止を指定し、OSKB020069の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P JES2 停止
    CASE OSKB020069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P JES2 停止
    CASE OSKB020069
    SOURCE z/OS MVS Operations
    ```

    P JES2 停止とOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020069を同じ出力で読み、条件検査の停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020069
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020069 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020069   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P JES2 停止 と OSKB020069 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P LLA

### P LLA 停止 {#c22-i0206}
*分類: P LLA*  ・  難易度: 中級

LLA を停止する。LNKLST ロード時に LLA 経由のメモリ・コピーが使われなくなる影響を理解した上で実施

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更検分の停止に関する P LLA 停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更検分の停止の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更検分の停止の証跡として保存して根拠にする。
    - C. P LLA 停止の変更点を出力本文から切り離して変更検分の停止の承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、変更検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では P LLA 停止 は「P LLA 停止の状態と出力メッセージを結び付ける変更検分項目」と D A,L または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では P LLA 停止の出力行と IEE115I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明だけに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では P LLA 停止をz/OS MVS Operationsの確認記録に残し、対象名は変更検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P LLA 停止**

    - 検証目的: 順序検査の停止について、LLA を停止する。LNKLST ロード時に LLA 経由のメモリ・コピーが使われなくなる影響を理解した上で実施に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序検査の停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP LLA 停止を指定し、OSKB020075の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P LLA 停止
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P LLA 停止
    CASE OSKB020075
    SOURCE z/OS MVS Operations
    ```

    P LLA 停止とOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020075を同じ出力で読み、順序検査の停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020075 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020075   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P LLA 停止 と OSKB020075 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P NET

### P NET VTAM 停止 {#c22-i0207}
*分類: P NET*  ・  難易度: 上級

P NET VTAM 停止は、MVS オペレータコマンドのP NETで確認する項目です。VTAM を停止する。Z NET,QUICK と異なり、未完セッションのクリーンアップを待つ標準停止

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序検分の停止で操作コマンドの運用確認を行います。P NET VTAM 停止の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序検分の停止を確認した扱いにする。
    - B. IEE115I の有無を確認せず順序検分の停止を正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、順序検分の点検結果を残す。 ✅
    - D. P NET VTAM 停止の属性行を読まず順序検分の停止の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では P NET VTAM 停止 は「z/OS MVS Operationsで P NET VTAM 停止の扱いを記録する順序検分項目」と D A,L または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では P NET VTAM 停止の表示結果と IEE115I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明だけに寄り、判定名は順序検分不足です。順序検分資料では P NET VTAM 停止の使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P NET VTAM 停止**

    - 検証目的: 区切検査の停止について、P NET VTAM 停止は、MVS オペレータコマンドの P NET で確認する項目です。VTAM を停止する。Z NET,QUICK と異なり、未完セッションのクリーンアッに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切検査の停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP NET VTAM 停止を指定し、OSKB020070の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P NET VTAM 停止
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P NET VTAM 停止
    CASE OSKB020070
    SOURCE z/OS MVS Operations
    ```

    P NET VTAM 停止とOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020070を同じ出力で読み、区切検査の停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020070 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020070   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P NET VTAM 停止 と OSKB020070 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P SCH

### P ASCH スケジューラ停止 {#c22-i0208}
*分類: P SCH*  ・  難易度: 中級

P ASCH スケジューラ停止は、MVS オペレータコマンドのP SCHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文確認再のスケジューラ停止に関係する P ASCH スケジューラ停止の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文確認再の確認記録にまとめる。 ✅
    - B. P ASCH スケジューラ停止の名称と担当者名だけを残して構文確認再のスケジューラ停止の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文確認再のスケジューラ停止を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文確認再のスケジューラ停止の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文確認再正解では選択記号 A を採用し、正解名は構文確認再正解です。構文確認再根拠では P ASCH スケジューラ停止 は「P ASCH スケジューラ停止の用途を操作コマンドの表示で確認する構文確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は構文確認再根拠です。構文確認再背景ではz/OS MVS Operationsの P ASCH スケジューラ停止と IEE115I を同じ証跡に残し、背景名は構文確認再背景です。他の選択肢を確認します。 A: 構文確認再正答は対象出力と項目説明を結び、根拠名は構文確認再正答です。 B: 構文確認再不足は名称や説明だけに寄り、判定名は構文確認再不足です。 C: 構文確認再流用は別カテゴリの確認であり、排除名は構文確認再流用です。 D: 構文確認再欠落は戻り値や記録番号に寄り、欠落名は構文確認再欠落です。構文確認再用語では P ASCH スケジューラ停止を MVS オペレータコマンドで扱う確認対象とし、用語名は構文確認再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P ASCH スケジューラ停止**

    - 検証目的: 値域検査のスケジューラ停止について、P ASCH スケジューラ停止は、MVS オペレータコマンドの P SCH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020076の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域検査のスケジューラ停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP ASCH スケジューラ停止を指定し、OSKB020076の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P ASCH スケジューラ停止
    CASE OSKB020076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P ASCH スケジューラ停止
    CASE OSKB020076
    SOURCE z/OS MVS Operations
    ```

    P ASCH スケジューラ停止とOSKB020076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020076を同じ出力で読み、値域検査のスケジューラ停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020076
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020076 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020076   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P ASCH スケジューラ停止 と OSKB020076 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P TRACE

### P TRACE = TRACE CT,OFF {#c22-i0209}
*分類: P TRACE*  ・  難易度: 上級

コンポーネント・トレースを停止する場合は TRACE CT,OFF,COMP=name を使う (P TRACE は使わない)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧検分の操作コマンドで P 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. P 属性の出力を取らず復旧検分の操作コマンドの説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて復旧検分の根拠を固定する。 ✅
    - C. D A,L を省略して復旧検分の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧検分の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では P 属性 は「復旧検分の操作コマンドに関係する定義値と表示行を照合する復旧検分項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では P 属性の属性行と IEE115I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明だけに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では P 属性を MVS オペレータコマンドの運用手順で確認し、初出名は復旧検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P TRACE = TRACE CT,OFF**

    - 検証目的: 記録検査の操作コマンドについて、コンポーネント・トレースを停止する場合は TRACE CT,OFF,COMP=name を使う (P TRACE は使わない)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録検査の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP TRACE = TRACE CTを指定し、OSKB020073の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P TRACE = TRACE CT
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P TRACE = TRACE CT
    CASE OSKB020073
    SOURCE z/OS MVS Operations
    ```

    P TRACE = TRACE CTとOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020073を同じ出力で読み、記録検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020073 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020073   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P TRACE = TRACE CT と OSKB020073 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > P TSO

### P TSO サブシステム停止 {#c22-i0210}
*分類: P TSO*  ・  難易度: 中級

P TSO サブシステム停止は、MVS オペレータコマンドのP TSOで確認する項目です。TSO/E サブシステムを停止し、新規 LOGON を拒否する。既存ユーザに事前通知が必要

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告検分のサブシステム停止に関係する P TSO サブシステム停止の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、警告検分の確認値として扱う。 ✅
    - B. P TSO サブシステム停止の名称と担当者名だけを残して警告検分のサブシステム停止の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告検分のサブシステム停止を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告検分のサブシステム停止の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では P TSO サブシステム停止 は「P TSO サブシステム停止の用途を操作コマンドの表示で確認する警告検分項目」と D A,L または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景ではz/OS MVS Operationsの P TSO サブシステム停止と IEE115I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明だけに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では P TSO サブシステム停止を MVS オペレータコマンドで扱う確認対象とし、用語名は警告検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **P TSO サブシステム停止**

    - 検証目的: 優先検査のサブシステム停止について、P TSO サブシステム停止は、MVS オペレータコマンドの P TSO で確認する項目です。TSO/E サブシステムを停止し、新規 LOGON を拒否する。既存ユーザに事前通に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先検査のサブシステム停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にP TSO サブシステム停止を指定し、OSKB020072の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND P TSO サブシステム停止
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM P TSO サブシステム停止
    CASE OSKB020072
    SOURCE z/OS MVS Operations
    ```

    P TSO サブシステム停止とOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020072を同じ出力で読み、優先検査のサブシステム停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020072 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020072   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の P TSO サブシステム停止 と OSKB020072 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > R

### R nn,CANCEL (DUMP) {#c22-i0211}
*分類: R*  ・  難易度: 中級

R nn,CANCEL (DUMP)は、MVS オペレータコマンドのRで状態表示や操作を行うためのコマンド関連項目です。R nn,CANCEL (DUMP)は、WTOR を出している側のジョブの規約により CANCEL や DUMP を指示できる典型応答 (例: IEA911E ダンプ続行)

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力照合再の操作コマンドに関する R nn 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力照合再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力照合再の操作コマンドの証跡として保存して根拠にする。
    - C. R nn 命令の変更点を出力本文から切り離して出力照合再の操作コマンドの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、出力照合再の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合再正解では選択記号 D を採用し、正解名は出力照合再正解です。出力照合再根拠では R nn 命令 は「R nn 命令の状態と出力メッセージを結び付ける出力照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力照合再根拠です。出力照合再保存では R nn 命令の出力行と IEE115I を一緒に残し、保存名は出力照合再保存です。選択肢ごとの違いを示します。 A: 出力照合再欠落は戻り値や記録番号に寄り、欠落名は出力照合再欠落です。 B: 出力照合再流用は別カテゴリの確認であり、排除名は出力照合再流用です。 C: 出力照合再不足は名称や説明だけに寄り、判定名は出力照合再不足です。 D: 出力照合再正答は対象出力と項目説明を結び、根拠名は出力照合再正答です。出力照合再対象では R nn 命令をz/OS MVS Operationsの確認記録に残し、対象名は出力照合再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切確認の操作コマンドで R nn,CANCEL (DUMP)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. R nn,CANCEL (DUMP)の出力を取らず区切確認の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 ✅
    - C. D A,L を省略して区切確認の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認の操作コマンドにおいて選択記号 B を採用し、識別名は区切確認です。区切確認の操作コマンドにおいて R nn,CANCEL (DUMP) は説明欄の「区切確認の操作コマンドに関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の操作コマンドの証跡を読む担当者は、R nn,CANCEL (DUMP)の属性行と IEE115I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切確認ではありません。 D: 区切確認の操作コマンドは別カテゴリの確認を流用しており、R nn,CANCEL (DUMP)の根拠にならないため区切確認ではありません。区切確認の操作コマンドに出る R nn,CANCEL (DUMP)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **R nn,CANCEL (DUMP)**

    - 検証目的: 呼出整理の操作コマンドについて、R nn,CANCEL (DUMP)は、MVS オペレータコマンドの R で状態表示や操作を行うためのコマンド関連項目です。R nn,CANCEL (DUMP)は、WTOR をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020103の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,CANCEL (DUMP)を指定し、OSKB020103の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R nn,CANCEL (DUMP)
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R nn,CANCEL (DUMP)
    CASE OSKB020103
    SOURCE z/OS MVS Operations
    ```

    R nn,CANCEL (DUMP)とOSKB020103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020103を同じ出力で読み、呼出整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020103 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020103   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R nn,CANCEL (DUMP) と OSKB020103 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### R nn,U / R nn,'U' (Continue) {#c22-i0212}
*分類: R*  ・  難易度: 中級

R nn,U / R nn,'U' (Continue)は、MVS オペレータコマンドのRで確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メッセージの規約に従う

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 条件照合再の・に関係する R nn,U 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件照合再として引き継ぐ。 ✅
    - B. R nn,U 属性の名称と担当者名だけを残して条件照合再の・の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件照合再の・を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件照合再の・の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合再正解では選択記号 A を採用し、正解名は条件照合再正解です。条件照合再根拠では R nn,U 属性 は「R nn,U 属性の用途を操作コマンドの表示で確認する条件照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は条件照合再根拠です。条件照合再背景ではz/OS MVS Operationsの R nn,U 属性と IEE115I を同じ証跡に残し、背景名は条件照合再背景です。他の選択肢を確認します。 A: 条件照合再正答は対象出力と項目説明を結び、根拠名は条件照合再正答です。 B: 条件照合再不足は名称や説明だけに寄り、判定名は条件照合再不足です。 C: 条件照合再流用は別カテゴリの確認であり、排除名は条件照合再流用です。 D: 条件照合再欠落は戻り値や記録番号に寄り、欠落名は条件照合再欠落です。条件照合再用語では R nn,U 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 構文照合保守の構文照合として R nn,U / R nn,'U' (Continue) を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 別分類の結果を流用して同じ証跡として扱う。
    - C. 構文照合の確認結果を出典名と表示本文に結び付ける。 ✅
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解はCです。構文照合保守で扱う R nn,U / R nn,'U' (Continue) は MVS オペレータコマンド の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として R nn,U / R nn,'U' (Continue) を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **R nn,U ・ R nn,'U' (Continue)**

    - 検証目的: 監査照合の・について、R nn,U / R nn,'U' (Continue)は、MVS オペレータコマンドの R で確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040039の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査照合の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,U ・ R nn,'U' を指定し、OSKB040039の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R nn,U ・ R nn,'U' 
    CASE OSKB040039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R nn,U ・ R nn,'U' 
    CASE OSKB040039
    SOURCE z/OS MVS Operations
    ```

    R nn,U ・ R nn,'U' とOSKB040039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040039を同じ出力で読み、監査照合の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040039 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040039   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R nn,U ・ R nn,'U'  と OSKB040039 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **R nn,U ・ R nn,'U' (Continue)**

    - 検証目的: 置換整理の・について、R nn,U / R nn,'U' (Continue)は、MVS オペレータコマンドの R で確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020104の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,U ・ R nn,'U' を指定し、OSKB020104の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R nn,U ・ R nn,'U' 
    CASE OSKB020104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R nn,U ・ R nn,'U' 
    CASE OSKB020104
    SOURCE z/OS MVS Operations
    ```

    R nn,U ・ R nn,'U' とOSKB020104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020104を同じ出力で読み、置換整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020104
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020104 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020104   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R nn,U ・ R nn,'U'  と OSKB020104 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### R 基本構文 R nn,'text' {#c22-i0213}
*分類: R*  ・  難易度: 初級

R 基本構文 R nn,'text'は、MVS オペレータコマンドのRで確認する項目です。未応答 WTOR (D R,L で取れた応答番号 nn) に対しテキスト応答を返す。MVS オペレーションの基本動作

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 終端照合再の基本構文に関係する R 基本構文 R nn 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端照合再の確認記録にまとめる。 ✅
    - B. R 基本構文 R nn 命令の名称と担当者名だけを残して終端照合再の基本構文の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端照合再の基本構文を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端照合再の基本構文の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 終端照合再正解では選択記号 A を採用し、正解名は終端照合再正解です。終端照合再根拠では R 基本構文 R nn 命令 は「R 基本構文 R nn 命令の用途を操作コマンドの表示で確認する終端照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は終端照合再根拠です。終端照合再背景ではz/OS MVS Operationsの R 基本構文 R nn 命令と IEE115I を同じ証跡に残し、背景名は終端照合再背景です。他の選択肢を確認します。 A: 終端照合再正答は対象出力と項目説明を結び、根拠名は終端照合再正答です。 B: 終端照合再不足は名称や説明だけに寄り、判定名は終端照合再不足です。 C: 終端照合再流用は別カテゴリの確認であり、排除名は終端照合再流用です。 D: 終端照合再欠落は戻り値や記録番号に寄り、欠落名は終端照合再欠落です。終端照合再用語では R 基本構文 R nn 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 上書確認の基本構文で操作コマンドの運用確認を行います。R 基本構文 R nn,'text'の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書確認の基本構文を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書確認の基本構文を正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書確認の記録として扱う。 ✅
    - D. R 基本構文 R nn,'text'の属性行を読まず上書確認の基本構文の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書確認の基本構文において選択記号 C を採用し、識別名は上書確認です。上書確認の基本構文において R 基本構文 R nn,'text' は説明欄の「z/OS MVS Operationsで R 基本構文 R nn,'text'の扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の基本構文を受け取る担当者は、R 基本構文 R nn,'text'の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の基本構文は別カテゴリの確認を流用しており、R 基本構文 R nn,'text'の根拠にならないため上書確認ではありません。 B: 上書確認の基本構文は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書確認ではありません。 C: 上書確認の基本構文は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の基本構文が示す R 基本構文 R nn,'text'は出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **R 基本構文 R nn,'text'**

    - 検証目的: 変更判定の基本構文について、R 基本構文 R nn,'text'は、MVS オペレータコマンドの R で確認する項目です。未応答 WTOR (D R,L で取れた応答番号 nn) に対しテキスト応答を返すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020100の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更判定の基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にR 基本構文 R nn,'text'を指定し、OSKB020100の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND R 基本構文 R nn,'text'
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM R 基本構文 R nn,'text'
    CASE OSKB020100
    SOURCE z/OS MVS Operations
    ```

    R 基本構文 R nn,'text'とOSKB020100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020100を同じ出力で読み、変更判定の基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020100
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020100 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020100   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の R 基本構文 R nn,'text' と OSKB020100 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 応答テキストの引用符 {#c22-i0214}
*分類: R*  ・  難易度: 中級

応答テキストの引用符は、MVS オペレータコマンドのRで確認する項目です。空白・カンマ等を含む応答は単一引用符で囲む。引用符内の引用符は二重指定でエスケープ

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書照合再の応答テキストの引用符で操作コマンドの運用確認を行います。応答テキストの引用符の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書照合再の応答テキストの引用符を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書照合再の応答テキストの引用符を正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、上書照合再の結果として保存する。 ✅
    - D. 応答テキストの引用符の属性行を読まず上書照合再の応答テキストの引用符の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合再正解では選択記号 C を採用し、正解名は上書照合再正解です。上書照合再根拠では応答テキストの引用符は「z/OS MVS Operationsで応答テキストの引用符の扱いを記録する上書照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は上書照合再根拠です。上書照合再受渡では応答テキストの引用符の表示結果と IEE115I を同じ確認単位にし、受渡名は上書照合再受渡です。不適切な選択肢を整理します。 A: 上書照合再流用は別カテゴリの確認であり、排除名は上書照合再流用です。 B: 上書照合再欠落は戻り値や記録番号に寄り、欠落名は上書照合再欠落です。 C: 上書照合再正答は対象出力と項目説明を結び、根拠名は上書照合再正答です。 D: 上書照合再不足は名称や説明だけに寄り、判定名は上書照合再不足です。上書照合再資料では応答テキストの引用符の使い方を出典欄から追跡し、資料名は上書照合再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件確認の応答テキストの引用符に関係する応答テキストの引用符の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 ✅
    - B. 応答テキストの引用符の名称と担当者名のみを残して条件確認の応答テキストの引用符の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件確認の応答テキストの引用符を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件確認の応答テキストの引用符の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認の応答テキストの引用符において選択記号 A を採用し、識別名は条件確認です。条件確認の応答テキストの引用符において応答テキストの引用符は説明欄の「応答テキストの引用符の用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の応答テキストの引用符に関連して、z/OS MVS Operationsでは応答テキストの引用符の表示属性と IEE115I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の応答テキストの引用符は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の応答テキストの引用符は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の応答テキストの引用符は別カテゴリの確認を流用しており、応答テキストの引用符の根拠にならないため条件確認ではありません。 D: 条件確認の応答テキストの引用符は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件確認ではありません。条件確認の応答テキストの引用符で使う応答テキストの引用符という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **応答テキストの引用符**

    - 検証目的: 展開整理の応答テキストの引用符について、応答テキストの引用符は、MVS オペレータコマンドの R で確認する項目です。空白・カンマ等を含む応答は単一引用符で囲む。引用符内の引用符は二重指定でエスケープに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020102の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開整理の応答テキストの引用符の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に応答テキストの引用符を指定し、OSKB020102の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 応答テキストの引用符
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 応答テキストの引用符
    CASE OSKB020102
    SOURCE z/OS MVS Operations
    ```

    応答テキストの引用符とOSKB020102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020102を同じ出力で読み、展開整理の応答テキストの引用符の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020102
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020102 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020102   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の 応答テキストの引用符 と OSKB020102 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 応答番号 nn の形式 {#c22-i0215}
*分類: R*  ・  難易度: 中級

応答番号 nn の形式は、MVS オペレータコマンドのRで確認する項目です。nn は 00〜99 (1, 2 桁) を表示時の番号で指定する。番号は WTOR 単位に動的割当てされ、応答後は再利用される

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 探索照合再の応答番号 の形式で応答番号 nn の形式の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 応答番号 nn の形式の出力を取らず探索照合再の応答番号 の形式の説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索照合再の根拠にする。 ✅
    - C. D A,L を省略して探索照合再の応答番号 の形式の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索照合再の応答番号 の形式へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合再正解では選択記号 B を採用し、正解名は探索照合再正解です。探索照合再根拠では応答番号 nn の形式 は「探索照合再の応答番号 の形式に関係する定義値と表示行を照合する探索照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は探索照合再根拠です。探索照合再追跡では応答番号 nn の形式の属性行と IEE115I を合わせ、追跡名は探索照合再追跡です。誤答側の問題点を分けます。 A: 探索照合再不足は名称や説明だけに寄り、判定名は探索照合再不足です。 B: 探索照合再正答は対象出力と項目説明を結び、根拠名は探索照合再正答です。 C: 探索照合再欠落は戻り値や記録番号に寄り、欠落名は探索照合再欠落です。 D: 探索照合再流用は別カテゴリの確認であり、排除名は探索照合再流用です。探索照合再初出では応答番号 nn の形式を MVS オペレータコマンドの運用手順で確認し、初出名は探索照合再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 出力確認の応答番号 の形式に関する応答番号 nn の形式の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力確認の応答番号 の形式の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の応答番号 の形式の証跡として保存して根拠にする。
    - C. 応答番号 nn の形式の変更点を出力本文から切り離して出力確認の応答番号 の形式の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認の応答番号 の形式において選択記号 D を採用し、識別名は出力確認です。出力確認の応答番号 の形式において応答番号 nn の形式 は説明欄の「応答番号 nn の形式の状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の応答番号 の形式に関する記録は、応答番号 nn の形式の出力行と IEE115I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の応答番号 の形式は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力確認ではありません。 B: 出力確認の応答番号 の形式は別カテゴリの確認を流用しており、応答番号 nn の形式の根拠にならないため出力確認ではありません。 C: 出力確認の応答番号 の形式は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の応答番号 の形式は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の応答番号 の形式で記録する応答番号 nn の形式はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **応答番号 nn の形式**

    - 検証目的: 構文整理の応答番号 の形式について、応答番号 nn の形式は、MVS オペレータコマンドの R で確認する項目です。nn は 00〜99 (1, 2 桁) を表示時の番号で指定する。番号は WTOR 単位に動的割に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文整理の応答番号 の形式の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に応答番号 nn の形式を指定し、OSKB020101の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 応答番号 nn の形式
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 応答番号 nn の形式
    CASE OSKB020101
    SOURCE z/OS MVS Operations
    ```

    応答番号 nn の形式とOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020101を同じ出力で読み、構文整理の応答番号 の形式の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020101
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020101 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020101   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の 応答番号 nn の形式 と OSKB020101 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > ROUTE

### ROUTE (sys1,sys2),cmd {#c22-i0216}
*分類: ROUTE*  ・  難易度: 中級

ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドのROUTEで確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査追跡の操作コマンドで操作コマンドの運用確認を行います。ROUTE (sys1,sys2),cmdの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査追跡の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査追跡の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査追跡の記録として扱う。 ✅
    - D. ROUTE (sys1,sys2),cmdの属性行を読まず監査追跡の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査追跡の操作コマンドにおいて選択記号 C を採用し、識別名は監査追跡です。監査追跡の操作コマンドにおいて ROUTE (sys1,sys2),cmd は説明欄の「z/OS MVS Operationsで ROUTE (sys1,sys2),cmdの扱いを記録する監査追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査追跡です。監査追跡の操作コマンドを受け取る担当者は、ROUTE (sys1,sys2),cmdの表示結果と IEE115I を同じ確認単位として扱い、背景名は監査追跡です。不適切な選択肢を整理します。 A: 監査追跡の操作コマンドは別カテゴリの確認を流用しており、ROUTE (sys1,sys2),cmdの根拠にならないため監査追跡ではありません。 B: 監査追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査追跡ではありません。 C: 監査追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査追跡です。 D: 監査追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査追跡ではありません。監査追跡の操作コマンドが示す ROUTE (sys1,sys2),cmdは出典欄の資料で使い方を追跡できる項目であり、用語名は監査追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **ROUTE (sys1,sys2),cmd**

    - 検証目的: 上書追跡の操作コマンドについて、ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドの ROUTE で確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040047の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE (sys1,sys2),を指定し、OSKB040047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE (sys1,sys2),
    CASE OSKB040047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE (sys1,sys2),
    CASE OSKB040047
    SOURCE z/OS MVS Operations
    ```

    ROUTE (sys1,sys2),とOSKB040047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040047 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040047   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE (sys1,sys2), と OSKB040047 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **ROUTE (sys1,sys2),cmd**

    - 検証目的: 優先照合の操作コマンドについて、ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドの ROUTE で確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE (sys1,sys2),を指定し、OSKB030032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE (sys1,sys2),
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE (sys1,sys2),
    CASE OSKB030032
    SOURCE z/OS MVS Operations
    ```

    ROUTE (sys1,sys2),とOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030032を同じ出力で読み、優先照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030032 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030032   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE (sys1,sys2), と OSKB030032 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### ROUTE *ALL,cmd {#c22-i0217}
*分類: ROUTE*  ・  難易度: 中級

ROUTE *ALL,cmdは、MVS オペレータコマンドのROUTEで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告追跡の*に関係する ROUTE *ALL,cmdの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告追跡として残す。 ✅
    - B. ROUTE *ALL,cmdの名称と担当者名のみを残して警告追跡の*の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告追跡の*を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告追跡の*の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡の*において選択記号 A を採用し、識別名は警告追跡です。警告追跡の*において ROUTE *ALL,cmd は説明欄の「ROUTE *ALL,cmdの用途を操作コマンドの表示で確認する警告追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告追跡です。警告追跡の*に関連して、z/OS MVS Operationsでは ROUTE *ALL,cmdの表示属性と IEE115I を同じ証跡に残し、背景名は警告追跡です。他の選択肢を確認します。 A: 警告追跡の*は対象出力と項目説明を結び、根拠を残すので警告追跡です。 B: 警告追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため警告追跡ではありません。 C: 警告追跡の*は別カテゴリの確認を流用しており、ROUTE *ALL,cmdの根拠にならないため警告追跡ではありません。 D: 警告追跡の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告追跡ではありません。警告追跡の*で使う ROUTE *ALL,cmdという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **ROUTE *ALL,cmd**

    - 検証目的: 区切照合の*について、ROUTE *ALL,cmdは、MVS オペレータコマンドの ROUTE で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切照合の*の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE *ALL,cmdを指定し、OSKB030030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE *ALL,cmd
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE *ALL,cmd
    CASE OSKB030030
    SOURCE z/OS MVS Operations
    ```

    ROUTE *ALL,cmdとOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030030を同じ出力で読み、区切照合の*の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030030 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030030   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE *ALL,cmd と OSKB030030 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### ROUTE T=seconds,... {#c22-i0218}
*分類: ROUTE*  ・  難易度: 中級

ROUTE T=seconds,...は、MVS オペレータコマンドのROUTEで確認する項目です。応答待ちタイムアウトを指定。Sysplex 内応答が揃わない場合の待ち時間制御

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更追跡のなどに関する ROUTE T=seconds,などの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更追跡のなどの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡のなどの証跡として保存して根拠にする。
    - C. ROUTE T=seconds,などの変更点を出力本文から切り離して変更追跡のなどの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡のなどにおいて選択記号 D を採用し、識別名は変更追跡です。変更追跡のなどにおいて ROUTE T=seconds,など は説明欄の「ROUTE T=seconds,などの状態と出力メッセージを結び付ける変更追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更追跡です。変更追跡のなどに関する記録は、ROUTE T=seconds,などの出力行と IEE115I を一緒に保存し、背景名は変更追跡です。選択肢ごとの違いを示します。 A: 変更追跡のなどは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更追跡ではありません。 B: 変更追跡のなどは別カテゴリの確認を流用しており、ROUTE T=seconds,などの根拠にならないため変更追跡ではありません。 C: 変更追跡のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため変更追跡ではありません。 D: 変更追跡のなどは対象出力と項目説明を結び、根拠を残すので変更追跡です。変更追跡のなどで記録する ROUTE T=seconds,などはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200



### ROUTE sysname,cmd {#c22-i0219}
*分類: ROUTE*  ・  難易度: 中級

ROUTE sysname,cmdは、特定の Sysplex メンバ・システムにコマンドをルーティングする形式

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧追跡の操作コマンドで ROUTE sysname,cmdの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ROUTE sysname,cmdの出力を取らず復旧追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧追跡の確認結果にする。 ✅
    - C. D A,L を省略して復旧追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡の操作コマンドにおいて選択記号 B を採用し、識別名は復旧追跡です。復旧追跡の操作コマンドにおいて ROUTE sysname,cmd は説明欄の「復旧追跡の操作コマンドに関係する定義値と表示行を照合する復旧追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧追跡です。復旧追跡の操作コマンドの証跡を読む担当者は、ROUTE sysname,cmdの属性行と IEE115I を合わせて追跡し、背景名は復旧追跡です。誤答側の問題点を分けます。 A: 復旧追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧追跡ではありません。 B: 復旧追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧追跡です。 C: 復旧追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧追跡ではありません。 D: 復旧追跡の操作コマンドは別カテゴリの確認を流用しており、ROUTE sysname,cmdの根拠にならないため復旧追跡ではありません。復旧追跡の操作コマンドに出る ROUTE sysname,cmdは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **ROUTE sysname,cmd**

    - 検証目的: 範囲照合の操作コマンドについて、ROUTE sysname,cmdは、特定の Sysplex メンバ・システムにコマンドをルーティングする形式に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE sysname,cmdを指定し、OSKB030031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ROUTE sysname,cmd
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ROUTE sysname,cmd
    CASE OSKB030031
    SOURCE z/OS MVS Operations
    ```

    ROUTE sysname,cmdとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030031を同じ出力で読み、範囲照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030031 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030031   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の ROUTE sysname,cmd と OSKB030031 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S

### JOBNAME= 指定 {#c22-i0220}
*分類: S*  ・  難易度: 中級

JOBNAME= 指定は、MVS オペレータコマンドのSで確認する項目です。STC のジョブ名を明示的に指定する。同一プロシージャで複数インスタンスを区別する典型用途

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告読解の指定に関係する JOBNAME= 指定の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告読解の確認記録にまとめる。 ✅
    - B. JOBNAME= 指定の名称と担当者名だけを残して警告読解の指定の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告読解の指定を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告読解の指定の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では JOBNAME= 指定 は「JOBNAME= 指定の用途を操作コマンドの表示で確認する警告読解項目」と D A,L または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景ではz/OS MVS Operationsの JOBNAME= 指定と IEE115I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明だけに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では JOBNAME= 指定を MVS オペレータコマンドで扱う確認対象とし、用語名は警告読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **JOBNAME= 指定**

    - 検証目的: 優先追跡の指定について、JOBNAME= 指定は、MVS オペレータコマンドの S で確認する項目です。STC のジョブ名を明示的に指定する。同一プロシージャで複数インスタンスを区別する典型用途に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先追跡の指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にJOBNAME= 指定を指定し、OSKB020052の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND JOBNAME= 指定
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM JOBNAME= 指定
    CASE OSKB020052
    SOURCE z/OS MVS Operations
    ```

    JOBNAME= 指定とOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020052を同じ出力で読み、優先追跡の指定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020052
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020052 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020052   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の JOBNAME= 指定 と OSKB020052 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### REUSASID=YES 指定 {#c22-i0221}
*分類: S*  ・  難易度: 中級

REUSASID=YES 指定は、MVS オペレータコマンドのSで確認する項目です。新規 STC 起動時に再利用可能 ASID を割り当てる。ASID 枯渇対策時に使用する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 値域読解の指定に関する REUSASID=YES 指定の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域読解の指定の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域読解の指定の証跡として保存して根拠にする。
    - C. REUSASID=YES 指定の変更点を出力本文から切り離して値域読解の指定の承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、値域読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では REUSASID=YES 指定 は「REUSASID=YES 指定の状態と出力メッセージを結び付ける値域読解項目」と D A,L または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では REUSASID=YES 指定の出力行と IEE115I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明だけに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では REUSASID=YES 指定をz/OS MVS Operationsの確認記録に残し、対象名は値域読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **REUSASID=YES 指定**

    - 検証目的: 範囲追跡の指定について、REUSASID=YES 指定は、MVS オペレータコマンドの S で確認する項目です。新規 STC 起動時に再利用可能 ASID を割り当てる。ASID 枯渇対策時に使用するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲追跡の指定の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にREUSASID=YES 指定を指定し、OSKB020051の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND REUSASID=YES 指定
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM REUSASID=YES 指定
    CASE OSKB020051
    SOURCE z/OS MVS Operations
    ```

    REUSASID=YES 指定とOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020051を同じ出力で読み、範囲追跡の指定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020051
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020051 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020051   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の REUSASID=YES 指定 と OSKB020051 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### S コマンド基本構文 {#c22-i0222}
*分類: S*  ・  難易度: 初級

S コマンド基本構文は、MVS オペレータコマンドのSで状態表示や操作を行うためのコマンド関連項目です。S procname.identifier,parm=value の形でカタログ・プロシージャを起動する。短縮形 S。実行は新規アドレス・スペースで行われる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 比較読解のコマンド基本構文で S コマンド基本構文の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S コマンド基本構文の出力を取らず比較読解のコマンド基本構文の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて比較読解の根拠を固定する。 ✅
    - C. D A,L を省略して比較読解のコマンド基本構文の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較読解のコマンド基本構文へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では S コマンド基本構文 は「比較読解のコマンド基本構文に関係する定義値と表示行を照合する比較読解項目」と D A,L または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では S コマンド基本構文の属性行と IEE115I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明だけに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では S コマンド基本構文を MVS オペレータコマンドの運用手順で確認し、初出名は比較読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S コマンド基本構文**

    - 検証目的: 条件追跡のコマンド基本構文について、S コマンド基本構文は、MVS オペレータコマンドの S で状態表示や操作を行うためのコマンド関連項目です。S procname.identifier,parm=value のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件追跡のコマンド基本構文の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS コマンド基本構文を指定し、OSKB020049の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S コマンド基本構文
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S コマンド基本構文
    CASE OSKB020049
    SOURCE z/OS MVS Operations
    ```

    S コマンド基本構文とOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020049を同じ出力で読み、条件追跡のコマンド基本構文の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020049 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020049   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S コマンド基本構文 と OSKB020049 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### 識別子 (identifier) の役割 {#c22-i0223}
*分類: S*  ・  難易度: 中級

識別子 (identifier) の役割は、MVS オペレータコマンドのSで確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別する。MODIFY/STOP の対象指定にも使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序読解の識別子 の役割で操作コマンドの運用確認を行います。識別子 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序読解の識別子 の役割を確認した扱いにする。
    - B. IEE457I の有無を確認せず順序読解の識別子 の役割を正常終了として記録する。
    - C. IEE457I を含む表示を保存し、説明欄との差分を順序読解で確認する。 ✅
    - D. 識別子 属性の属性行を読まず順序読解の識別子 の役割の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では識別子 属性は「z/OS MVS Operationsで識別子 属性の扱いを記録する順序読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では識別子 属性の表示結果と IEE457I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明だけに寄り、判定名は順序読解不足です。順序読解資料では識別子 属性の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **識別子 (identifier) の役割**

    - 検証目的: 区切照合の識別子 の役割について、識別子 (identifier) の役割は、MVS オペレータコマンドの S で確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、区切照合の識別子 の役割の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に識別子 (identifier) のを指定し、OSKB040030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 識別子 (identifier) の
    CASE OSKB040030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 識別子 (identifier) の
    CASE OSKB040030
    SOURCE z/OS MVS Operations
    ```

    識別子 (identifier) のとOSKB040030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040030を同じ出力で読み、区切照合の識別子 の役割の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040030 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040030   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の 識別子 (identifier) の と OSKB040030 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **識別子 (identifier) の役割**

    - 検証目的: 区切追跡の識別子 の役割について、識別子 (identifier) の役割は、MVS オペレータコマンドの S で確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、区切追跡の識別子 の役割の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に識別子 (identifier) のを指定し、OSKB020050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 識別子 (identifier) の
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 識別子 (identifier) の
    CASE OSKB020050
    SOURCE z/OS MVS Operations
    ```

    識別子 (identifier) のとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020050を同じ出力で読み、区切追跡の識別子 の役割の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020050 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020050   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の 識別子 (identifier) の と OSKB020050 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S APPC

### S APPC APPC/MVS 起動 {#c22-i0224}
*分類: S APPC*  ・  難易度: 中級

APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 上書検分の・ 起動で操作コマンドの運用確認を行います。S APPC APPC 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書検分の・ 起動を確認した扱いにする。
    - B. IEE115I の有無を確認せず上書検分の・ 起動を正常終了として記録する。
    - C. IEE115I を含む表示を保存し、説明欄との差分を上書検分で確認する。 ✅
    - D. S APPC APPC 属性の属性行を読まず上書検分の・ 起動の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では S APPC APPC 属性 は「z/OS MVS Operationsで S APPC APPC 属性の扱いを記録する上書検分項目」と D A,L または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では S APPC APPC 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明だけに寄り、判定名は上書検分不足です。上書検分資料では S APPC APPC 属性の使い方を出典欄から追跡し、資料名は上書検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **S APPC APPC ・ MVS 起動**

    - 検証目的: 優先照合の・ 起動について、APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先照合の・ 起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS APPC APPC ・ MVS を指定し、OSKB040032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S APPC APPC ・ MVS 
    CASE OSKB040032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S APPC APPC ・ MVS 
    CASE OSKB040032
    SOURCE z/OS MVS Operations
    ```

    S APPC APPC ・ MVS とOSKB040032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040032を同じ出力で読み、優先照合の・ 起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040032 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040032   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S APPC APPC ・ MVS  と OSKB040032 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **S APPC APPC ・ MVS 起動**

    - 検証目的: 展開検査の・ 起動について、APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開検査の・ 起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS APPC APPC ・ MVS を指定し、OSKB020062の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S APPC APPC ・ MVS 
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S APPC APPC ・ MVS 
    CASE OSKB020062
    SOURCE z/OS MVS Operations
    ```

    S APPC APPC ・ MVS とOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020062を同じ出力で読み、展開検査の・ 起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020062 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020062   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S APPC APPC ・ MVS  と OSKB020062 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S CICS

### S CICS リージョン起動 {#c22-i0225}
*分類: S CICS*  ・  難易度: 上級

CICS Transaction Server のリージョンを起動。S CICSPROD.CICSPROD のように識別子で本番/開発を区別する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 変更読解のリージョン起動に関する S CICS リージョン起動の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更読解のリージョン起動の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更読解のリージョン起動の証跡として保存して根拠にする。
    - C. S CICS リージョン起動の変更点を出力本文から切り離して変更読解のリージョン起動の承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、変更読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では S CICS リージョン起動 は「S CICS リージョン起動の状態と出力メッセージを結び付ける変更読解項目」と D A,L または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では S CICS リージョン起動の出力行と IEE115I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明だけに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では S CICS リージョン起動をz/OS MVS Operationsの確認記録に残し、対象名は変更読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S CICS リージョン起動**

    - 検証目的: 順序追跡のリージョン起動について、CICS Transaction Server のリージョンを起動。S CICSPROD.CICSPROD のように識別子で本番/開発を区別するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序追跡のリージョン起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS CICS リージョン起動を指定し、OSKB020055の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S CICS リージョン起動
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S CICS リージョン起動
    CASE OSKB020055
    SOURCE z/OS MVS Operations
    ```

    S CICS リージョン起動とOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020055を同じ出力で読み、順序追跡のリージョン起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020055
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020055 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020055   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S CICS リージョン起動 と OSKB020055 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S DB2

### S DB2 サブシステム起動 {#c22-i0226}
*分類: S DB2*  ・  難易度: 中級

S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンド

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文検分のサブシステム起動に関係する S DB2 サブシステム起動の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、構文検分として引き継ぐ。 ✅
    - B. S DB2 サブシステム起動の名称と担当者名だけを残して構文検分のサブシステム起動の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文検分のサブシステム起動を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文検分のサブシステム起動の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では S DB2 サブシステム起動 は「S DB2 サブシステム起動の用途を操作コマンドの表示で確認する構文検分項目」と D A,L または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景ではz/OS MVS Operationsの S DB2 サブシステム起動と IEE115I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明だけに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では S DB2 サブシステム起動を MVS オペレータコマンドで扱う確認対象とし、用語名は構文検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **S DB2 サブシステム起動**

    - 検証目的: 範囲照合のサブシステム起動について、S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲照合のサブシステム起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DB2 サブシステム起動を指定し、OSKB040031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DB2 サブシステム起動
    CASE OSKB040031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DB2 サブシステム起動
    CASE OSKB040031
    SOURCE z/OS MVS Operations
    ```

    S DB2 サブシステム起動とOSKB040031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040031を同じ出力で読み、範囲照合のサブシステム起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040031 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040031   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DB2 サブシステム起動 と OSKB040031 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **S DB2 サブシステム起動**

    - 検証目的: 値域追跡のサブシステム起動について、S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域追跡のサブシステム起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DB2 サブシステム起動を指定し、OSKB020056の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DB2 サブシステム起動
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DB2 サブシステム起動
    CASE OSKB020056
    SOURCE z/OS MVS Operations
    ```

    S DB2 サブシステム起動とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020056を同じ出力で読み、値域追跡のサブシステム起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020056
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020056 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020056   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DB2 サブシステム起動 と OSKB020056 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S DLF

### S DLF Hiperbatch 起動 {#c22-i0227}
*分類: S DLF*  ・  難易度: 中級

S DLF Hiperbatch 起動は、MVS オペレータコマンドのS DLFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 探索検分の起動で S DLF Hiperbatch 起動の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S DLF Hiperbatch 起動の出力を取らず探索検分の起動の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索検分の根拠を固定する。 ✅
    - C. D A,L を省略して探索検分の起動の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索検分の起動へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では S DLF Hiperbatch 起動 は「探索検分の起動に関係する定義値と表示行を照合する探索検分項目」と D A,L または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では S DLF Hiperbatch 起動の属性行と IEE115I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明だけに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では S DLF Hiperbatch 起動を MVS オペレータコマンドの運用手順で確認し、初出名は探索検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S DLF Hiperbatch 起動**

    - 検証目的: 構文検査の起動について、S DLF Hiperbatch 起動は、MVS オペレータコマンドの S DLF で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文検査の起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DLF Hiperbatch 起を指定し、OSKB020061の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DLF Hiperbatch 起
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DLF Hiperbatch 起
    CASE OSKB020061
    SOURCE z/OS MVS Operations
    ```

    S DLF Hiperbatch 起とOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020061を同じ出力で読み、構文検査の起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020061 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020061   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DLF Hiperbatch 起 と OSKB020061 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S DUMPSRV

### S DUMPSRV SVC ダンプ・サービス {#c22-i0228}
*分類: S DUMPSRV*  ・  難易度: 中級

S DUMPSRV SVC ダンプ・サービスは、MVS オペレータコマンドのS DUMPSRVで確認する項目です。DUMPSRV (SVC ダンプ・サービス) を起動する。通常 IPL 時自動起動で手動の再起動用

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先検分のダンプ・サービスに関する S DUMPSRV SVC ダンプ 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先検分のダンプ・サービスの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先検分のダンプ・サービスの証跡として保存して根拠にする。
    - C. S DUMPSRV SVC ダンプ 属性の変更点を出力本文から切り離して優先検分のダンプ・サービスの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、優先検分の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では S DUMPSRV SVC ダンプ 属性 は「S DUMPSRV SVC ダンプ 属性の状態と出力メッセージを結び付ける優先検分項目」と D A,L または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では S DUMPSRV SVC ダンプ 属性の出力行と IEE115I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明だけに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では S DUMPSRV SVC ダンプ 属性をz/OS MVS Operationsの確認記録に残し、対象名は優先検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S DUMPSRV SVC ダンプ・サービス**

    - 検証目的: 上書検査のダンプ・サービスについて、S DUMPSRV SVC ダンプ・サービスは、MVS オペレータコマンドの S DUMPSRV で確認する項目です。DUMPSRV (SVC ダンプ・サービス) を起動する。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書検査のダンプ・サービスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS DUMPSRV SVC ダンプ・を指定し、OSKB020067の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S DUMPSRV SVC ダンプ・
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S DUMPSRV SVC ダンプ・
    CASE OSKB020067
    SOURCE z/OS MVS Operations
    ```

    S DUMPSRV SVC ダンプ・とOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020067を同じ出力で読み、上書検査のダンプ・サービスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020067 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020067   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S DUMPSRV SVC ダンプ・ と OSKB020067 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S JES2

### S JES2 起動 {#c22-i0229}
*分類: S JES2*  ・  難易度: 中級

S JES2 起動は、MVS オペレータコマンドのS JES2で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 置換検分の起動に関する S JES2 起動の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず置換検分の起動の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換検分の起動の証跡として保存して根拠にする。
    - C. S JES2 起動の変更点を出力本文から切り離して置換検分の起動の承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検分で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では S JES2 起動 は「S JES2 起動の状態と出力メッセージを結び付ける置換検分項目」と D A,L または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では S JES2 起動の出力行と IEE115I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明だけに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では S JES2 起動をz/OS MVS Operationsの確認記録に残し、対象名は置換検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S JES2 起動**

    - 検証目的: 監査追跡の起動について、S JES2 起動は、MVS オペレータコマンドの S JES2 で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査追跡の起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS JES2 起動を指定し、OSKB020059の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S JES2 起動
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S JES2 起動
    CASE OSKB020059
    SOURCE z/OS MVS Operations
    ```

    S JES2 起動とOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020059を同じ出力で読み、監査追跡の起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020059
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020059 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020059   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S JES2 起動 と OSKB020059 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### S JES2,PARM='WARM,NOREQ' {#c22-i0230}
*分類: S JES2*  ・  難易度: 中級

S JES2,PARM='WARM,NOREQ'は、MVS オペレータコマンドのS JES2で確認する項目です。通常起動 (WARM) で対話プロンプトなし。運用自動化での標準形

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 終端検分の操作コマンドに関係する S JES2 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端検分の確認値として扱う。 ✅
    - B. S JES2 命令の名称と担当者名だけを残して終端検分の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端検分の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず終端検分の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では S JES2 命令 は「S JES2 命令の用途を操作コマンドの表示で確認する終端検分項目」と D A,L または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景ではz/OS MVS Operationsの S JES2 命令と IEE115I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明だけに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では S JES2 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S JES2,PARM='WARM,NOREQ'**

    - 検証目的: 変更追跡の操作コマンドについて、S JES2,PARM='WARM,NOREQ'は、MVS オペレータコマンドの S JES2 で確認する項目です。通常起動 (WARM) で対話プロンプトなし。運用自動化でのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS JES2,PARM='WARM,を指定し、OSKB020060の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S JES2,PARM='WARM,
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S JES2,PARM='WARM,
    CASE OSKB020060
    SOURCE z/OS MVS Operations
    ```

    S JES2,PARM='WARM,とOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020060を同じ出力で読み、変更追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020060 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020060   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S JES2,PARM='WARM, と OSKB020060 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S LLA

### S LLA Library Lookaside {#c22-i0231}
*分類: S LLA*  ・  難易度: 中級

S LLA Library Lookasideは、MVS オペレータコマンドのS LLAで用いるLLA (Library Lookaside) を起動する。LNKLST ロード性能改善の前提コンポーネント。S LLAでは、指定値と対象資源、実行時の出力を突き合わせて確認する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力検分の操作コマンドに関する S 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力検分の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力検分の操作コマンドの証跡として保存して根拠にする。
    - C. S 機能の変更点を出力本文から切り離して出力検分の操作コマンドの承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、出力検分の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では S 機能 は「S 機能の状態と出力メッセージを結び付ける出力検分項目」と D A,L または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では S 機能の出力行と IEE115I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明だけに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では S 機能をz/OS MVS Operationsの確認記録に残し、対象名は出力検分対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S LLA Library Lookaside**

    - 検証目的: 呼出検査の操作コマンドについて、S LLA Library Lookasideは、MVS オペレータコマンドの S LLA で用いる LLA (Library Lookaside) を起動する。LNKLST ロに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出検査の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS LLA Library Lookを指定し、OSKB020063の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S LLA Library Look
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S LLA Library Look
    CASE OSKB020063
    SOURCE z/OS MVS Operations
    ```

    S LLA Library LookとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020063を同じ出力で読み、呼出検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020063 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020063   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S LLA Library Look と OSKB020063 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S NET

### S NET VTAM 起動 {#c22-i0232}
*分類: S NET*  ・  難易度: 上級

S NET VTAM 起動は、MVS オペレータコマンドのS NETで状態表示や操作を行うためのコマンド関連項目です。VTAM (Communications Server) を起動する。SNA / TCP/IP のうち SNA 側および APPL 配下の前提となる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 監査読解の起動で操作コマンドの運用確認を行います。S NET VTAM 起動の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査読解の起動を確認した扱いにする。
    - B. IEE115I の有無を確認せず監査読解の起動を正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、監査読解の結果として保存する。 ✅
    - D. S NET VTAM 起動の属性行を読まず監査読解の起動の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では S NET VTAM 起動 は「z/OS MVS Operationsで S NET VTAM 起動の扱いを記録する監査読解項目」と D A,L または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では S NET VTAM 起動の表示結果と IEE115I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明だけに寄り、判定名は監査読解不足です。監査読解資料では S NET VTAM 起動の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S NET VTAM 起動**

    - 検証目的: 比較追跡の起動について、S NET VTAM 起動は、MVS オペレータコマンドの S NET で状態表示や操作を行うためのコマンド関連項目です。VTAM (Communications Serverに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較追跡の起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS NET VTAM 起動を指定し、OSKB020054の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S NET VTAM 起動
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S NET VTAM 起動
    CASE OSKB020054
    SOURCE z/OS MVS Operations
    ```

    S NET VTAM 起動とOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020054を同じ出力で読み、比較追跡の起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020054 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020054   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S NET VTAM 起動 と OSKB020054 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S OMVS

### S OMVS=xx {#c22-i0233}
*分類: S OMVS*  ・  難易度: 中級

S OMVS=xxは、MVS オペレータコマンドのS OMVSで確認する項目です。z/OS UNIX を BPXPRMxx 指定で初期化または再初期化する。F BPXOINIT,SHUTDOWN 後の再起動でも使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 展開検分の操作コマンドで S OMVS=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S OMVS=xxの出力を取らず展開検分の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検分の確認にする。 ✅
    - C. D A,L を省略して展開検分の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開検分の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では S OMVS=xx は「展開検分の操作コマンドに関係する定義値と表示行を照合する展開検分項目」と D A,L または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では S OMVS=xxの属性行と IEE115I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明だけに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では S OMVS=xxを MVS オペレータコマンドの運用手順で確認し、初出名は展開検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S OMVS=xx**

    - 検証目的: 警告追跡の操作コマンドについて、S OMVS=xxは、MVS オペレータコマンドの S OMVS で確認する項目です。z/OS UNIX を BPXPRMxx 指定で初期化または再初期化する。F BPXOINに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、警告追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS OMVS=xxを指定し、OSKB020057の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S OMVS=xx
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S OMVS=xx
    CASE OSKB020057
    SOURCE z/OS MVS Operations
    ```

    S OMVS=xxとOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020057を同じ出力で読み、警告追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020057
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020057 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020057   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S OMVS=xx と OSKB020057 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S RACF

### S RACF/ICHRDSNT 関連 {#c22-i0234}
*分類: S RACF*  ・  難易度: 中級

RACF サブシステム・アドレス・スペース (RACF SUBSYS) を起動する。RACF コマンド・プレフィックス利用の前提

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 呼出検分の・ 関連で操作コマンドの運用確認を行います。S RACF 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出検分の・ 関連を確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出検分の・ 関連を正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出検分の点検結果を残す。 ✅
    - D. S RACF 属性の属性行を読まず呼出検分の・ 関連の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では S RACF 属性 は「z/OS MVS Operationsで S RACF 属性の扱いを記録する呼出検分項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では S RACF 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明だけに寄り、判定名は呼出検分不足です。呼出検分資料では S RACF 属性の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S RACF ・ ICHRDSNT 関連**

    - 検証目的: 復旧追跡の・ 関連について、RACF サブシステム・アドレス・スペース (RACF SUBSYS) を起動する。RACF コマンド・プレフィックス利用の前提に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、復旧追跡の・ 関連の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS RACF ・ ICHRDSNT を指定し、OSKB020058の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S RACF ・ ICHRDSNT 
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S RACF ・ ICHRDSNT 
    CASE OSKB020058
    SOURCE z/OS MVS Operations
    ```

    S RACF ・ ICHRDSNT とOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020058を同じ出力で読み、復旧追跡の・ 関連の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020058
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020058 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020058   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S RACF ・ ICHRDSNT  と OSKB020058 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S SCH

### S ASCH スケジューラ {#c22-i0235}
*分類: S SCH*  ・  難易度: 中級

S ASCH スケジューラは、MVS オペレータコマンドのS SCHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切検分のスケジューラで S ASCH スケジューラの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S ASCH スケジューラの出力を取らず区切検分のスケジューラの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切検分の根拠にする。 ✅
    - C. D A,L を省略して区切検分のスケジューラの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切検分のスケジューラへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では S ASCH スケジューラ は「区切検分のスケジューラに関係する定義値と表示行を照合する区切検分項目」と D A,L または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では S ASCH スケジューラの属性行と IEE115I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明だけに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では S ASCH スケジューラを MVS オペレータコマンドの運用手順で確認し、初出名は区切検分初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S ASCH スケジューラ**

    - 検証目的: 終端検査のスケジューラについて、S ASCH スケジューラは、MVS オペレータコマンドの S SCH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端検査のスケジューラの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS ASCH スケジューラを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S ASCH スケジューラ
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S ASCH スケジューラ
    CASE OSKB020065
    SOURCE z/OS MVS Operations
    ```

    S ASCH スケジューラとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020065を同じ出力で読み、終端検査のスケジューラの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020065 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020065   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S ASCH スケジューラ と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S TRACE

### S TRACE,...の不在 {#c22-i0236}
*分類: S TRACE*  ・  難易度: 上級

トレースは S ではなく TRACE CT,ON / SET TRACE で開始する点に注意。S は使用しない

**出典:** z / OS MVS System Commands



## MVS オペレータコマンド > S TSO

### S TSO TSO/E 起動 {#c22-i0237}
*分類: S TSO*  ・  難易度: 中級

S TSO TSO/E 起動は、MVS オペレータコマンドのS TSOで確認する項目です。TSO/E サブシステム (TSO サブシステム・アドレス・スペース) を起動する。LOGON 受付の前提

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 復旧読解の・ 起動で S TSO TSO ・ E 起動の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. S TSO TSO ・ E 起動の出力を取らず復旧読解の・ 起動の説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧読解の根拠にする。 ✅
    - C. D A,L を省略して復旧読解の・ 起動の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧読解の・ 起動へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では S TSO TSO ・ E 起動 は「復旧読解の・ 起動に関係する定義値と表示行を照合する復旧読解項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では S TSO TSO ・ E 起動の属性行と IEE115I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明だけに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では S TSO TSO ・ E 起動を MVS オペレータコマンドの運用手順で確認し、初出名は復旧読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S TSO TSO ・ E 起動**

    - 検証目的: 記録追跡の・ 起動について、S TSO TSO/E 起動は、MVS オペレータコマンドの S TSO で確認する項目です。TSO/E サブシステム (TSO サブシステム・アドレス・スペース) を起動するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録追跡の・ 起動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS TSO TSO ・ E 起動を指定し、OSKB020053の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S TSO TSO ・ E 起動
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S TSO TSO ・ E 起動
    CASE OSKB020053
    SOURCE z/OS MVS Operations
    ```

    S TSO TSO ・ E 起動とOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020053を同じ出力で読み、記録追跡の・ 起動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020053 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020053   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S TSO TSO ・ E 起動 と OSKB020053 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > S VLF

### S VLF Virtual Lookaside {#c22-i0238}
*分類: S VLF*  ・  難易度: 中級

VLF (Virtual Lookaside Facility) を起動する。CSVLLA・キャタログ・RACF の各キャッシュの前提

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件検分の操作コマンドに関係する S 機能の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件検分の確認記録にまとめる。 ✅
    - B. S 機能の名称と担当者名だけを残して条件検分の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件検分の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件検分の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では S 機能 は「S 機能の用途を操作コマンドの表示で確認する条件検分項目」と D A,L または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景ではz/OS MVS Operationsの S 機能と IEE115I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明だけに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では S 機能を MVS オペレータコマンドで扱う確認対象とし、用語名は条件検分用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **S VLF Virtual Lookaside**

    - 検証目的: 置換検査の操作コマンドについて、VLF (Virtual Lookaside Facility) を起動する。CSVLLA ・キャタログ・ RACF の各キャッシュの前提に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換検査の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にS VLF Virtual Lookを指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND S VLF Virtual Look
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM S VLF Virtual Look
    CASE OSKB020064
    SOURCE z/OS MVS Operations
    ```

    S VLF Virtual LookとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020064を同じ出力で読み、置換検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020064 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020064   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の S VLF Virtual Look と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SEND

### SEND 'text',CN=(*ALL) {#c22-i0239}
*分類: SEND*  ・  難易度: 中級

SEND 'text',CN=(*ALL)は、MVS オペレータコマンドのSENDで確認する項目です。Sysplex 全コンソールに一斉送信する形式。停止予告など全員告知に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切追跡の*で SEND 'text',CN=(*ALL)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SEND 'text',CN=(*ALL)の出力を取らず区切追跡の*の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 ✅
    - C. D A,L を省略して区切追跡の*の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の*へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡の*において選択記号 B を採用し、識別名は区切追跡です。区切追跡の*において SEND 'text',CN=(*ALL) は説明欄の「区切追跡の*に関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の*の証跡を読む担当者は、SEND 'text',CN=(*ALL)の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の*は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の*は別カテゴリの確認を流用しており、SEND 'text',CN=(*ALL)の根拠にならないため区切追跡ではありません。区切追跡の*に出る SEND 'text',CN=(*ALL)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',CN=(*ALL)**

    - 検証目的: 呼出照合の*について、SEND 'text',CN=(*ALL)は、MVS オペレータコマンドの SEND で確認する項目です。Sysplex 全コンソールに一斉送信する形式。停止予告など全員告知にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030023の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出照合の*の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',CN=(*Aを指定し、OSKB030023の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',CN=(*A
    CASE OSKB030023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',CN=(*A
    CASE OSKB030023
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',CN=(*AとOSKB030023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030023を同じ出力で読み、呼出照合の*の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030023 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030023   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',CN=(*A と OSKB030023 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SEND 'text',CN=name {#c22-i0240}
*分類: SEND*  ・  難易度: 中級

SEND 'text',CN=nameは、MVS オペレータコマンドのSENDで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件追跡の操作コマンドに関係する SEND 'text',CN=nameの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. SEND 'text',CN=nameの名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて SEND 'text',CN=name は説明欄の「SEND 'text',CN=nameの用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは SEND 'text',CN=nameの表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、SEND 'text',CN=nameの根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う SEND 'text',CN=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',CN=name**

    - 検証目的: 展開照合の操作コマンドについて、SEND 'text',CN=nameは、MVS オペレータコマンドの SEND で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030022の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',CN=namを指定し、OSKB030022の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',CN=nam
    CASE OSKB030022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',CN=nam
    CASE OSKB030022
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',CN=namとOSKB030022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030022を同じ出力で読み、展開照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030022
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030022 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030022   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',CN=nam と OSKB030022 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SEND 'text',NOW {#c22-i0241}
*分類: SEND*  ・  難易度: 中級

SEND 'text',NOWは、MVS オペレータコマンドのSENDで確認する項目です。即時表示モード。受信側で SAVE モードを設定しても無視して直ちに表示する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 範囲追跡の操作コマンドで操作コマンドの運用確認を行います。SEND 'text',NOW の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲追跡の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず範囲追跡の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲追跡の記録として扱う。 ✅
    - D. SEND 'text',NOW の属性行を読まず範囲追跡の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡の操作コマンドにおいて選択記号 C を採用し、識別名は範囲追跡です。範囲追跡の操作コマンドにおいて SEND 'text',NOW は説明欄の「z/OS MVS Operationsで SEND 'text',NOW の扱いを記録する範囲追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲追跡です。範囲追跡の操作コマンドを受け取る担当者は、SEND 'text',NOW の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲追跡です。不適切な選択肢を整理します。 A: 範囲追跡の操作コマンドは別カテゴリの確認を流用しており、SEND 'text',NOW の根拠にならないため範囲追跡ではありません。 B: 範囲追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲追跡ではありません。 C: 範囲追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲追跡です。 D: 範囲追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲追跡ではありません。範囲追跡の操作コマンドが示す SEND 'text',NOW は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',NOW**

    - 検証目的: 置換照合の操作コマンドについて、SEND 'text',NOW は、MVS オペレータコマンドの SEND で確認する項目です。即時表示モード。受信側で SAVE モードを設定しても無視して直ちに表示するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030024の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',NOWを指定し、OSKB030024の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',NOW
    CASE OSKB030024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',NOW
    CASE OSKB030024
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',NOWとOSKB030024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030024を同じ出力で読み、置換照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030024
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030024 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030024   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',NOW と OSKB030024 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SEND 'text',USER=userid {#c22-i0242}
*分類: SEND*  ・  難易度: 中級

SEND 'text',USER=useridは、MVS オペレータコマンドのSENDで確認する項目です。TSO ユーザに即時メッセージを送る形式。受信ユーザ側で M / N コマンドの設定が必要な点に注意

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力追跡の操作コマンドに関する SEND 'text',USER=useridの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。
    - C. SEND 'text',USER=useridの変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて SEND 'text',USER=userid は説明欄の「SEND 'text',USER=useridの状態と出力メッセージを結び付ける出力追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、SEND 'text',USER=useridの出力行と IEE115I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、SEND 'text',USER=useridの根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する SEND 'text',USER=useridはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SEND 'text',USER=userid**

    - 検証目的: 構文照合の操作コマンドについて、SEND 'text',USER=useridは、MVS オペレータコマンドの SEND で確認する項目です。TSO ユーザに即時メッセージを送る形式。受信ユーザ側で M /に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030021の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、構文照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSEND 'text',USER=uを指定し、OSKB030021の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SEND 'text',USER=u
    CASE OSKB030021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SEND 'text',USER=u
    CASE OSKB030021
    SOURCE z/OS MVS Operations
    ```

    SEND 'text',USER=uとOSKB030021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030021を同じ出力で読み、構文照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030021
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030021 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030021   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SEND 'text',USER=u と OSKB030021 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET DAE

### SET DAE=00 リセット {#c22-i0243}
*分類: SET DAE*  ・  難易度: 中級

SET DAE=00 リセットは、MVS オペレータコマンドのSET DAEで確認する項目です。ADYSET00 にて DAE をデフォルト状態に戻す典型的な用法。テスト中の調整から本番値に戻す際に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力分離のリセットに関する SET DAE=00 リセットの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力分離のリセットの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力分離のリセットの証跡として保存して根拠にする。
    - C. SET DAE=00 リセットの変更点を出力本文から切り離して出力分離のリセットの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では SET DAE=00 リセット は「SET DAE=00 リセットの状態と出力メッセージを結び付ける出力分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では SET DAE=00 リセットの出力行と IEE457I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明だけに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では SET DAE=00 リセットをz/OS MVS Operationsの確認記録に残し、対象名は出力分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切照合のリセットで SET DAE=00 リセットの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET DAE=00 リセットの出力を取らず区切照合のリセットの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. D OPDATA を省略して区切照合のリセットの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のリセットへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合のリセットにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のリセットにおいて SET DAE=00 リセット は説明欄の「区切照合のリセットに関係する定義値と表示行を照合する区切照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のリセットの証跡を読む担当者は、SET DAE=00 リセットの属性行と IEE457I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のリセットは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のリセットは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のリセットは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため区切照合ではありません。 D: 区切照合のリセットは別カテゴリの確認を流用しており、SET DAE=00 リセットの根拠にならないため区切照合ではありません。区切照合のリセットに出る SET DAE=00 リセットは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DAE=00 リセット**

    - 検証目的: 呼出照合のリセットについて、SET DAE=00 リセットは、MVS オペレータコマンドの SET DAE で確認する項目です。ADYSET00 にて DAE をデフォルト状態に戻す典型的な用法。テスト中に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、呼出照合のリセットの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DAE=00 リセットを指定し、OSKB020023の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DAE=00 リセット
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DAE=00 リセット
    CASE OSKB020023
    SOURCE z/OS MVS Operations
    ```

    SET DAE=00 リセットとOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020023を同じ出力で読み、呼出照合のリセットの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020023
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020023 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020023   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DAE=00 リセット と OSKB020023 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET DAE=xx 目的 {#c22-i0244}
*分類: SET DAE*  ・  難易度: 初級

ADYSETxx PARMLIB メンバを動的に再活性化し、重複ダンプ抑止 (DAE) の規則を変更する。再 IPL なしで運用変更可能

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書分離の目的で操作コマンドの運用確認を行います。SET DAE=xx 目的の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書分離の目的を確認した扱いにする。
    - B. IEE457I の有無を確認せず上書分離の目的を正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、上書分離の点検結果を残す。 ✅
    - D. SET DAE=xx 目的の属性行を読まず上書分離の目的の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では SET DAE=xx 目的 は「z/OS MVS Operationsで SET DAE=xx 目的の扱いを記録する上書分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では SET DAE=xx 目的の表示結果と IEE457I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明だけに寄り、判定名は上書分離不足です。上書分離資料では SET DAE=xx 目的の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件照合の目的に関係する SET DAE=xx 目的の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. SET DAE=xx 目的の名称と担当者名のみを残して条件照合の目的の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件照合の目的を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件照合の目的の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 条件照合の目的において選択記号 A を採用し、識別名は条件照合です。条件照合の目的において SET DAE=xx 目的 は説明欄の「SET DAE=xx 目的の用途を操作コマンドの表示で確認する条件照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の目的に関連して、z/OS MVS Operationsでは SET DAE=xx 目的の表示属性と IEE457I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の目的は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の目的は別カテゴリの確認を流用しており、SET DAE=xx 目的の根拠にならないため条件照合ではありません。 D: 条件照合の目的は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため条件照合ではありません。条件照合の目的で使う SET DAE=xx 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DAE=xx 目的**

    - 検証目的: 展開照合の目的について、ADYSETxx PARMLIB メンバを動的に再活性化し、重複ダンプ抑止 (DAE) の規則を変更する。再 IPL なしで運用変更可能に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、展開照合の目的の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DAE=xx 目的を指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DAE=xx 目的
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DAE=xx 目的
    CASE OSKB020022
    SOURCE z/OS MVS Operations
    ```

    SET DAE=xx 目的とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020022を同じ出力で読み、展開照合の目的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020022 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020022   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DAE=xx 目的 と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET DUMP

### SET DUMP=NODUMP 緊急停止 {#c22-i0245}
*分類: SET DUMP*  ・  難易度: 中級

SET DUMP=NODUMP 緊急停止は、MVS オペレータコマンドのSET DUMPで確認する項目です。ダンプ生成を一時的に止める用途。容量逼迫時に応急処置として使うが、原因分析資料を失うリスクを併記

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 区切分離の緊急停止で SET 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET 属性の出力を取らず区切分離の緊急停止の説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切分離の根拠を固定する。 ✅
    - C. D OPDATA を省略して区切分離の緊急停止の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切分離の緊急停止へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では SET 属性 は「区切分離の緊急停止に関係する定義値と表示行を照合する区切分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では SET 属性の属性行と IEE457I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明だけに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では SET 属性を MVS オペレータコマンドの運用手順で確認し、初出名は区切分離初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 優先照合の緊急停止に関する SET DUMP=NODUMP 緊急停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず優先照合の緊急停止の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の緊急停止の証跡として保存して根拠にする。
    - C. SET DUMP=NODUMP 緊急停止の変更点を出力本文から切り離して優先照合の緊急停止の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合の緊急停止において選択記号 D を採用し、識別名は優先照合です。優先照合の緊急停止において SET DUMP=NODUMP 緊急停止 は説明欄の「SET DUMP=NODUMP 緊急停止の状態と出力メッセージを結び付ける優先照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の緊急停止に関する記録は、SET DUMP=NODUMP 緊急停止の出力行と IEE457I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の緊急停止は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため優先照合ではありません。 B: 優先照合の緊急停止は別カテゴリの確認を流用しており、SET DUMP=NODUMP 緊急停止の根拠にならないため優先照合ではありません。 C: 優先照合の緊急停止は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の緊急停止は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の緊急停止で記録する SET DUMP=NODUMP 緊急停止はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DUMP=NODUMP 緊急停止**

    - 検証目的: 終端照合の緊急停止について、SET DUMP=NODUMP 緊急停止は、MVS オペレータコマンドの SET DUMP で確認する項目です。ダンプ生成を一時的に止める用途。容量逼迫時に応急処置として使うがに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、終端照合の緊急停止の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DUMP=NODUMP 緊急を指定し、OSKB020025の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DUMP=NODUMP 緊急
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DUMP=NODUMP 緊急
    CASE OSKB020025
    SOURCE z/OS MVS Operations
    ```

    SET DUMP=NODUMP 緊急とOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020025を同じ出力で読み、終端照合の緊急停止の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020025 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020025   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DUMP=NODUMP 緊急 と OSKB020025 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET DUMP=xx 目的 {#c22-i0246}
*分類: SET DUMP*  ・  難易度: 初級

SET DUMP=xx 目的は、DIAGxx などダンプ関連 PARMLIB メンバを動的活性化し、SVC ダンプの SDATA 既定や CHNGDUMP オプションを反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 条件分離の目的に関係する SET DUMP=xx 目的の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件分離の確認値として扱う。 ✅
    - B. SET DUMP=xx 目的の名称と担当者名だけを残して条件分離の目的の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件分離の目的を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件分離の目的の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では SET DUMP=xx 目的 は「SET DUMP=xx 目的の用途を操作コマンドの表示で確認する条件分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景ではz/OS MVS Operationsの SET DUMP=xx 目的と IEE457I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明だけに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では SET DUMP=xx 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は条件分離用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 範囲照合の目的で操作コマンドの運用確認を行います。SET DUMP=xx 目的の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲照合の目的を確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲照合の目的を正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. SET DUMP=xx 目的の属性行を読まず範囲照合の目的の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 範囲照合の目的において選択記号 C を採用し、識別名は範囲照合です。範囲照合の目的において SET DUMP=xx 目的 は説明欄の「z/OS MVS Operationsで SET DUMP=xx 目的の扱いを記録する範囲照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の目的を受け取る担当者は、SET DUMP=xx 目的の表示結果と IEE457I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の目的は別カテゴリの確認を流用しており、SET DUMP=xx 目的の根拠にならないため範囲照合ではありません。 B: 範囲照合の目的は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の目的は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の目的が示す SET DUMP=xx 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DUMP=xx 目的**

    - 検証目的: 置換照合の目的について、SET DUMP=xx 目的は、DIAGxx などダンプ関連 PARMLIB メンバを動的活性化し、SVC ダンプの SDATA 既定や CHNGDUMP オプションを反映に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、置換照合の目的の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DUMP=xx 目的を指定し、OSKB020024の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DUMP=xx 目的
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DUMP=xx 目的
    CASE OSKB020024
    SOURCE z/OS MVS Operations
    ```

    SET DUMP=xx 目的とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020024を同じ出力で読み、置換照合の目的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020024
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020024 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020024   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET DUMP=xx 目的 と OSKB020024 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET IEASYS

### SET IEASYS=xx {#c22-i0247}
*分類: SET IEASYS*  ・  難易度: 中級

IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多い

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 範囲分離の操作コマンドで操作コマンドの運用確認を行います。SET IEASYS=xxの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲分離の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲分離の操作コマンドを正常終了として記録する。
    - C. IEE457I を含む表示を保存し、説明欄との差分を範囲分離で確認する。 ✅
    - D. SET IEASYS=xxの属性行を読まず範囲分離の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では SET IEASYS=xx は「z/OS MVS Operationsで SET IEASYS=xxの扱いを記録する範囲分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では SET IEASYS=xxの表示結果と IEE457I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明だけに寄り、判定名は範囲分離不足です。範囲分離資料では SET IEASYS=xxの使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 記録照合の操作コマンドに関係する SET IEASYS=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 ✅
    - B. SET IEASYS=xxの名称と担当者名のみを残して記録照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録照合の操作コマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の操作コマンドにおいて SET IEASYS=xx は説明欄の「IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多い」と D OPDATA または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の操作コマンドに関連して、z/OS MVS Operationsでは SET IEASYS=xxの表示属性と IEE457I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の操作コマンドは別カテゴリの確認を流用しており、SET IEASYS=xxの根拠にならないため記録照合ではありません。 D: 記録照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため記録照合ではありません。記録照合の操作コマンドで使う SET IEASYS=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **SET IEASYS=xx**

    - 検証目的: 探索照合の操作コマンドについて、IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多いに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040026の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET IEASYS=xxを指定し、OSKB040026の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET IEASYS=xx
    CASE OSKB040026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET IEASYS=xx
    CASE OSKB040026
    SOURCE z/OS MVS Operations
    ```

    SET IEASYS=xxとOSKB040026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040026
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040026 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040026   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET IEASYS=xx と OSKB040026 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **SET IEASYS=xx**

    - 検証目的: 探索照合の操作コマンドについて、IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多いに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET IEASYS=xxを指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET IEASYS=xx
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET IEASYS=xx
    CASE OSKB020026
    SOURCE z/OS MVS Operations
    ```

    SET IEASYS=xxとOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020026 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020026   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET IEASYS=xx と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET MPF

### SET MPF=(xx,yy) 連結 {#c22-i0248}
*分類: SET MPF*  ・  難易度: 中級

SET MPF=(xx,yy) 連結は、MVS オペレータコマンドのSET MPFで確認する項目です。複数 MPF メンバを連結指定。基本規則 + サイト追加分という二重構造で運用する典型形

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 記録分離の連結に関係する SET MPF=(xx 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録分離の確認記録にまとめる。 ✅
    - B. SET MPF=(xx 命令の名称と担当者名だけを残して記録分離の連結の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録分離の連結を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録分離の連結の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では SET MPF=(xx 命令 は「SET MPF=(xx 命令の用途を操作コマンドの表示で確認する記録分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景ではz/OS MVS Operationsの SET MPF=(xx 命令と IEE457I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明だけに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では SET MPF=(xx 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録分離用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 順序照合の連結で操作コマンドの運用確認を行います。SET MPF=(xx,yy) 連結の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序照合の連結を確認した扱いにする。
    - B. IEE457I の有無を確認せず順序照合の連結を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序照合の記録として扱う。 ✅
    - D. SET MPF=(xx,yy) 連結の属性行を読まず順序照合の連結の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合の連結において選択記号 C を採用し、識別名は順序照合です。順序照合の連結において SET MPF=(xx,yy) 連結 は説明欄の「z/OS MVS Operationsで SET MPF=(xx,yy) 連結の扱いを記録する順序照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の連結を受け取る担当者は、SET MPF=(xx,yy) 連結の表示結果と IEE457I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の連結は別カテゴリの確認を流用しており、SET MPF=(xx,yy) 連結の根拠にならないため順序照合ではありません。 B: 順序照合の連結は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため順序照合ではありません。 C: 順序照合の連結は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の連結は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の連結が示す SET MPF=(xx,yy) 連結は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET MPF=(xx,yy) 連結**

    - 検証目的: 出力照合の連結について、SET MPF=(xx,yy) 連結は、MVS オペレータコマンドの SET MPF で確認する項目です。複数 MPF メンバを連結指定。基本規則 + サイト追加分という二重構に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力照合の連結の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET MPF=(xx,yy) 連結を指定し、OSKB020028の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET MPF=(xx,yy) 連結
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET MPF=(xx,yy) 連結
    CASE OSKB020028
    SOURCE z/OS MVS Operations
    ```

    SET MPF=(xx,yy) 連結とOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020028を同じ出力で読み、出力照合の連結の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020028
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020028 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020028   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET MPF=(xx,yy) 連結 と OSKB020028 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET MPF=xx {#c22-i0249}
*分類: SET MPF*  ・  難易度: 中級

SET MPF=xxは、MVS オペレータコマンドのSET MPFで用いるMPFLSTxx を動的活性化し、抑止メッセージ・自動化対象・色付け規則を更新する。最頻出 SET 系の一つ。SET MPFでは、指定値と対象資源、実行時の出力を突き合わせて確認する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 優先分離の操作コマンドに関する SET MPF=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず優先分離の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先分離の操作コマンドの証跡として保存して根拠にする。
    - C. SET MPF=xxの変更点を出力本文から切り離して優先分離の操作コマンドの承認欄だけ残す。
    - D. D OPDATA の結果から対象行を抜き出し、優先分離の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では SET MPF=xx は「SET MPF=xxの状態と出力メッセージを結び付ける優先分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では SET MPF=xxの出力行と IEE457I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明だけに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では SET MPF=xxをz/OS MVS Operationsの確認記録に残し、対象名は優先分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 比較照合の操作コマンドで SET MPF=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET MPF=xxの出力を取らず比較照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 ✅
    - C. D OPDATA を省略して比較照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合の操作コマンドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合の操作コマンドにおいて SET MPF=xx は説明欄の「比較照合の操作コマンドに関係する定義値と表示行を照合する比較照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の操作コマンドの証跡を読む担当者は、SET MPF=xxの属性行と IEE457I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため比較照合ではありません。 D: 比較照合の操作コマンドは別カテゴリの確認を流用しており、SET MPF=xxの根拠にならないため比較照合ではありません。比較照合の操作コマンドに出る SET MPF=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET MPF=xx**

    - 検証目的: 上書照合の操作コマンドについて、SET MPF=xxは、MVS オペレータコマンドの SET MPF で用いる MPFLSTxx を動的活性化し、抑止メッセージ・自動化対象・色付け規則を更新する。最頻出 SETに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、上書照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET MPF=xxを指定し、OSKB020027の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET MPF=xx
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET MPF=xx
    CASE OSKB020027
    SOURCE z/OS MVS Operations
    ```

    SET MPF=xxとOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020027
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020027 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020027   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET MPF=xx と OSKB020027 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET OMVS

### SET OMVS RESET=xx {#c22-i0250}
*分類: SET OMVS*  ・  難易度: 中級

SET OMVS RESET=xxは、MVS オペレータコマンドのSET OMVSで確認する項目です。現行設定を破棄して指定 BPXPRMxx 値で完全置換する形式。マウント情報には影響しない注意点を併記

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 順序分離の操作コマンドで操作コマンドの運用確認を行います。SET 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序分離の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず順序分離の操作コマンドを正常終了として記録する。
    - C. 同じ画面で対象行と IEE457I を読み、順序分離の結果として保存する。 ✅
    - D. SET 属性の属性行を読まず順序分離の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では SET 属性 は「z/OS MVS Operationsで SET 属性の扱いを記録する順序分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では SET 属性の表示結果と IEE457I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明だけに寄り、判定名は順序分離不足です。順序分離資料では SET 属性の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 警告照合の操作コマンドに関係する SET OMVS RESET=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 ✅
    - B. SET OMVS RESET=xxの名称と担当者名のみを残して警告照合の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告照合の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず警告照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合の操作コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合の操作コマンドにおいて SET OMVS RESET=xx は説明欄の「SET OMVS RESET=xxの用途を操作コマンドの表示で確認する警告照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の操作コマンドに関連して、z/OS MVS Operationsでは SET OMVS RESET=xxの表示属性と IEE457I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の操作コマンドは別カテゴリの確認を流用しており、SET OMVS RESET=xxの根拠にならないため警告照合ではありません。 D: 警告照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため警告照合ではありません。警告照合の操作コマンドで使う SET OMVS RESET=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET OMVS RESET=xx**

    - 検証目的: 区切照合の操作コマンドについて、SET OMVS RESET=xxは、MVS オペレータコマンドの SET OMVS で確認する項目です。現行設定を破棄して指定 BPXPRMxx 値で完全置換する形式。マウンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、区切照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET OMVS RESET=xxを指定し、OSKB020030の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET OMVS RESET=xx
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET OMVS RESET=xx
    CASE OSKB020030
    SOURCE z/OS MVS Operations
    ```

    SET OMVS RESET=xxとOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020030を同じ出力で読み、区切照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020030
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020030 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020030   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET OMVS RESET=xx と OSKB020030 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET OMVS=xx {#c22-i0251}
*分類: SET OMVS*  ・  難易度: 中級

SET OMVS=xxは、BPXPRMxx を動的活性化し、MAXPROCSYS など多くの z/OS UNIX 上限値を再 IPL なしで変更する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 比較分離の操作コマンドで SET OMVS=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET OMVS=xxの出力を取らず比較分離の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて比較分離の根拠にする。 ✅
    - C. D OPDATA を省略して比較分離の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較分離の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では SET OMVS=xx は「比較分離の操作コマンドに関係する定義値と表示行を照合する比較分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では SET OMVS=xxの属性行と IEE457I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明だけに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では SET OMVS=xxを MVS オペレータコマンドの運用手順で確認し、初出名は比較分離初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 値域照合の操作コマンドに関する SET OMVS=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず値域照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の操作コマンドの証跡として保存して根拠にする。
    - C. SET OMVS=xxの変更点を出力本文から切り離して値域照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合の操作コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の操作コマンドにおいて SET OMVS=xx は説明欄の「SET OMVS=xxの状態と出力メッセージを結び付ける値域照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の操作コマンドに関する記録は、SET OMVS=xxの出力行と IEE457I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため値域照合ではありません。 B: 値域照合の操作コマンドは別カテゴリの確認を流用しており、SET OMVS=xxの根拠にならないため値域照合ではありません。 C: 値域照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の操作コマンドで記録する SET OMVS=xxはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET OMVS=xx**

    - 検証目的: 条件照合の操作コマンドについて、SET OMVS=xxは、BPXPRMxx を動的活性化し、MAXPROCSYS など多くの z/OS UNIX 上限値を再 IPL なしで変更するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、条件照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET OMVS=xxを指定し、OSKB020029の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET OMVS=xx
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET OMVS=xx
    CASE OSKB020029
    SOURCE z/OS MVS Operations
    ```

    SET OMVS=xxとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020029を同じ出力で読み、条件照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020029
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020029 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020029   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET OMVS=xx と OSKB020029 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET PFK

### SET PFK=xx {#c22-i0252}
*分類: SET PFK*  ・  難易度: 中級

SET PFK=xxは、MVS オペレータコマンドのSET PFKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 値域分離の操作コマンドに関する SET PFK=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず値域分離の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域分離の操作コマンドの証跡として保存して根拠にする。
    - C. SET PFK=xxの変更点を出力本文から切り離して値域分離の操作コマンドの承認欄だけ残す。
    - D. D OPDATA で得た表示本文を使い、値域分離の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では SET PFK=xx は「SET PFK=xxの状態と出力メッセージを結び付ける値域分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では SET PFK=xxの出力行と IEE457I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明だけに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では SET PFK=xxをz/OS MVS Operationsの確認記録に残し、対象名は値域分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 復旧照合の操作コマンドで SET PFK=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET PFK=xxの出力を取らず復旧照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 ✅
    - C. D OPDATA を省略して復旧照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合の操作コマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の操作コマンドにおいて SET PFK=xx は説明欄の「復旧照合の操作コマンドに関係する定義値と表示行を照合する復旧照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の操作コマンドの証跡を読む担当者は、SET PFK=xxの属性行と IEE457I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の操作コマンドは別カテゴリの確認を流用しており、SET PFK=xxの根拠にならないため復旧照合ではありません。復旧照合の操作コマンドに出る SET PFK=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET PFK=xx**

    - 検証目的: 範囲照合の操作コマンドについて、SET PFK=xxは、MVS オペレータコマンドの SET PFK で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、範囲照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET PFK=xxを指定し、OSKB020031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET PFK=xx
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET PFK=xx
    CASE OSKB020031
    SOURCE z/OS MVS Operations
    ```

    SET PFK=xxとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020031を同じ出力で読み、範囲照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020031 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020031   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET PFK=xx と OSKB020031 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET PROG

### SET PROG=xx {#c22-i0253}
*分類: SET PROG*  ・  難易度: 中級

SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 警告分離の操作コマンドに関係する SET PROG=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告分離として引き継ぐ。 ✅
    - B. SET PROG=xxの名称と担当者名だけを残して警告分離の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告分離の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず警告分離の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では SET PROG=xx は「SET PROG=xxの用途を操作コマンドの表示で確認する警告分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景ではz/OS MVS Operationsの SET PROG=xxと IEE457I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明だけに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では SET PROG=xxを MVS オペレータコマンドで扱う確認対象とし、用語名は警告分離用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 監査照合の操作コマンドで操作コマンドの運用確認を行います。SET PROG=xxの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査照合の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず監査照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. SET PROG=xxの属性行を読まず監査照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合の操作コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の操作コマンドにおいて SET PROG=xx は説明欄の「z/OS MVS Operationsで SET PROG=xxの扱いを記録する監査照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の操作コマンドを受け取る担当者は、SET PROG=xxの表示結果と IEE457I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の操作コマンドは別カテゴリの確認を流用しており、SET PROG=xxの根拠にならないため監査照合ではありません。 B: 監査照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため監査照合ではありません。 C: 監査照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の操作コマンドが示す SET PROG=xxは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **SET PROG=xx**

    - 検証目的: 上書照合の操作コマンドについて、SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040027の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、上書照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET PROG=xxを指定し、OSKB040027の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET PROG=xx
    CASE OSKB040027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET PROG=xx
    CASE OSKB040027
    SOURCE z/OS MVS Operations
    ```

    SET PROG=xxとOSKB040027が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040027
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040027 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040027   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040027が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET PROG=xx と OSKB040027 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **SET PROG=xx**

    - 検証目的: 優先照合の操作コマンドについて、SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、優先照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET PROG=xxを指定し、OSKB020032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET PROG=xx
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET PROG=xx
    CASE OSKB020032
    SOURCE z/OS MVS Operations
    ```

    SET PROG=xxとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020032を同じ出力で読み、優先照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020032 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020032   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET PROG=xx と OSKB020032 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG APF,ADD {#c22-i0254}
*分類: SET PROG*  ・  難易度: 中級

SETPROG APF,ADDは、MVS オペレータコマンドのSET PROGで確認する項目です。個別データセットを動的に APF 許可リストへ追加するサブコマンド。緊急のソフトウェア導入時に多用

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 復旧分離の操作コマンドで SETPROG APF,ADD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SETPROG APF,ADD の出力を取らず復旧分離の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧分離の確認にする。 ✅
    - C. D A,L を省略して復旧分離の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧分離の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では SETPROG APF,ADD は「復旧分離の操作コマンドに関係する定義値と表示行を照合する復旧分離項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では SETPROG APF,ADD の属性行と IEE115I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明だけに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では SETPROG APF,ADD を MVS オペレータコマンドの運用手順で確認し、初出名は復旧分離初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 変更照合の操作コマンドに関する SETPROG APF,ADD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の操作コマンドの証跡として保存して根拠にする。
    - C. SETPROG APF,ADD の変更点を出力本文から切り離して変更照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合の操作コマンドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合の操作コマンドにおいて SETPROG APF,ADD は説明欄の「SETPROG APF,ADD の状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の操作コマンドに関する記録は、SETPROG APF,ADD の出力行と IEE115I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更照合ではありません。 B: 変更照合の操作コマンドは別カテゴリの確認を流用しており、SETPROG APF,ADD の根拠にならないため変更照合ではありません。 C: 変更照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の操作コマンドで記録する SETPROG APF,ADD はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG APF,ADD**

    - 検証目的: 記録照合の操作コマンドについて、SETPROG APF,ADD は、MVS オペレータコマンドの SET PROG で確認する項目です。個別データセットを動的に APF 許可リストへ追加するサブコマンド。緊急のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG APF,ADDを指定し、OSKB020033の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG APF,ADD
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG APF,ADD
    CASE OSKB020033
    SOURCE z/OS MVS Operations
    ```

    SETPROG APF,ADDとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020033を同じ出力で読み、記録照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020033 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020033   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG APF,ADD と OSKB020033 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG EXIT,ADD {#c22-i0255}
*分類: SET PROG*  ・  難易度: 上級

SETPROG EXIT,ADDは、MVS オペレータコマンドのSET PROGで確認する項目です。動的出口にルーチンを動的に登録する。OS の振る舞いを再 IPL なしで拡張・差替する手段

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 構文読解の操作コマンドに関係する SETPROG EXIT 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文読解の確認値として扱う。 ✅
    - B. SETPROG EXIT 命令の名称と担当者名だけを残して構文読解の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で構文読解の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文読解の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では SETPROG EXIT 命令 は「SETPROG EXIT 命令の用途を操作コマンドの表示で確認する構文読解項目」と D A,L または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景ではz/OS MVS Operationsの SETPROG EXIT 命令と IEE115I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明だけに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では SETPROG EXIT 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 呼出追跡の操作コマンドで操作コマンドの運用確認を行います。SETPROG EXIT,ADD の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出追跡の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず呼出追跡の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 ✅
    - D. SETPROG EXIT,ADD の属性行を読まず呼出追跡の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡の操作コマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の操作コマンドにおいて SETPROG EXIT,ADD は説明欄の「z/OS MVS Operationsで SETPROG EXIT,ADD の扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の操作コマンドを受け取る担当者は、SETPROG EXIT,ADD の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG EXIT,ADD の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の操作コマンドが示す SETPROG EXIT,ADD は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG EXIT,ADD**

    - 検証目的: 値域照合の操作コマンドについて、SETPROG EXIT,ADD は、MVS オペレータコマンドの SET PROG で確認する項目です。動的出口にルーチンを動的に登録する。OS の振る舞いを再 IPL なしでに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、値域照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG EXIT,ADDを指定し、OSKB020036の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG EXIT,ADD
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG EXIT,ADD
    CASE OSKB020036
    SOURCE z/OS MVS Operations
    ```

    SETPROG EXIT,ADDとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020036を同じ出力で読み、値域照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020036 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020036   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG EXIT,ADD と OSKB020036 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG LNKLST,DEFINE {#c22-i0256}
*分類: SET PROG*  ・  難易度: 中級

SETPROG LNKLST,DEFINEは、新しい LNKLST セットを定義 / ADD / ACTIVATE の動的入替手順を構成するサブコマンド。新しい LNKLST セットを定義 → ADD → ACTIVATE の動的入替手順を構成するサブコマンド

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 監査分離の操作コマンドで操作コマンドの運用確認を行います。SETPROG LNKLST 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査分離の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず監査分離の操作コマンドを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査分離の点検結果を残す。 ✅
    - D. SETPROG LNKLST 命令の属性行を読まず監査分離の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では SETPROG LNKLST 命令 は「z/OS MVS Operationsで SETPROG LNKLST 命令の扱いを記録する監査分離項目」と D A,L または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では SETPROG LNKLST 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明だけに寄り、判定名は監査分離不足です。監査分離資料では SETPROG LNKLST 命令の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 構文追跡の操作コマンドに関係する SETPROG LNKLST,DEFINE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 ✅
    - B. SETPROG LNKLST,DEFINE の名称と担当者名のみを残して構文追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で構文追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡の操作コマンドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡の操作コマンドにおいて SETPROG LNKLST,DEFINE は説明欄の「SETPROG LNKLST,DEFINE の用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の操作コマンドに関連して、z/OS MVS Operationsでは SETPROG LNKLST,DEFINE の表示属性と IEE115I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG LNKLST,DEFINE の根拠にならないため構文追跡ではありません。 D: 構文追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文追跡ではありません。構文追跡の操作コマンドで使う SETPROG LNKLST,DEFINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG LNKLST,DEFINE**

    - 検証目的: 比較照合の操作コマンドについて、SETPROG LNKLST,DEFINE は、新しい LNKLST セットを定義 / ADD / ACTIVATE の動的入替手順を構成するサブコマンド。新しい LNKLSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG LNKLST,DEFを指定し、OSKB020034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG LNKLST,DEF
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG LNKLST,DEF
    CASE OSKB020034
    SOURCE z/OS MVS Operations
    ```

    SETPROG LNKLST,DEFとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020034を同じ出力で読み、比較照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020034 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020034   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG LNKLST,DEF と OSKB020034 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETPROG LPA,ADD {#c22-i0257}
*分類: SET PROG*  ・  難易度: 中級

SETPROG LPA,ADDは、Dynamic LPA に個別モジュール / データセット内モジュールを動的追加する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 変更分離の操作コマンドに関する SETPROG LPA,ADD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更分離の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更分離の操作コマンドの証跡として保存して根拠にする。
    - C. SETPROG LPA,ADD の変更点を出力本文から切り離して変更分離の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更分離で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では SETPROG LPA,ADD は「SETPROG LPA,ADD の状態と出力メッセージを結び付ける変更分離項目」と D A,L または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では SETPROG LPA,ADD の出力行と IEE115I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明だけに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では SETPROG LPA,ADD をz/OS MVS Operationsの確認記録に残し、対象名は変更分離対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 展開追跡の操作コマンドで SETPROG LPA,ADD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SETPROG LPA,ADD の出力を取らず展開追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 ✅
    - C. D A,L を省略して展開追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡の操作コマンドにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡の操作コマンドにおいて SETPROG LPA,ADD は説明欄の「展開追跡の操作コマンドに関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の操作コマンドの証跡を読む担当者は、SETPROG LPA,ADD の属性行と IEE115I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG LPA,ADD の根拠にならないため展開追跡ではありません。展開追跡の操作コマンドに出る SETPROG LPA,ADD は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETPROG LPA,ADD**

    - 検証目的: 順序照合の操作コマンドについて、SETPROG LPA,ADD は、Dynamic LPA に個別モジュール / データセット内モジュールを動的追加するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、順序照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG LPA,ADDを指定し、OSKB020035の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETPROG LPA,ADD
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETPROG LPA,ADD
    CASE OSKB020035
    SOURCE z/OS MVS Operations
    ```

    SETPROG LPA,ADDとOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020035を同じ出力で読み、順序照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020035 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020035   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SETPROG LPA,ADD と OSKB020035 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SCH

### SET SCH=xx {#c22-i0258}
*分類: SET SCH*  ・  難易度: 中級

SCHEDxx を活性化し、プログラム特性テーブル (PPT) を更新する。AUTH/SYSTEM/NOSWAP 等の属性変更

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 展開読解の操作コマンドで SET SCH=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET SCH=xxの出力を取らず展開読解の操作コマンドの説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開読解の根拠を固定する。 ✅
    - C. D OPDATA を省略して展開読解の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開読解の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では SET SCH=xx は「展開読解の操作コマンドに関係する定義値と表示行を照合する展開読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では SET SCH=xxの属性行と IEE457I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明だけに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では SET SCH=xxを MVS オペレータコマンドの運用手順で確認し、初出名は展開読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 置換追跡の操作コマンドに関する SET SCH=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず置換追跡の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の操作コマンドの証跡として保存して根拠にする。
    - C. SET SCH=xxの変更点を出力本文から切り離して置換追跡の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡の操作コマンドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡の操作コマンドにおいて SET SCH=xx は説明欄の「SET SCH=xxの状態と出力メッセージを結び付ける置換追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の操作コマンドに関する記録は、SET SCH=xxの出力行と IEE457I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の操作コマンドは別カテゴリの確認を流用しており、SET SCH=xxの根拠にならないため置換追跡ではありません。 C: 置換追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の操作コマンドで記録する SET SCH=xxはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET SCH=xx**

    - 検証目的: 警告照合の操作コマンドについて、SCHEDxx を活性化し、プログラム特性テーブル (PPT) を更新する。AUTH/SYSTEM/NOSWAP 等の属性変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、警告照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SCH=xxを指定し、OSKB020037の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SCH=xx
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SCH=xx
    CASE OSKB020037
    SOURCE z/OS MVS Operations
    ```

    SET SCH=xxとOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020037を同じ出力で読み、警告照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020037 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020037   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SCH=xx と OSKB020037 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SLIP

### SLIP コマンド (SET SLIP=xx) {#c22-i0259}
*分類: SET SLIP*  ・  難易度: 中級

SLIP コマンド (SET SLIP=xx)は、IEASLPxx を動的活性化し、定義済み SLIP トラップ群を一括導入する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 終端読解のコマンドに関係する SLIP コマンド 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端読解の確認記録にまとめる。 ✅
    - B. SLIP コマンド 属性の名称と担当者名だけを残して終端読解のコマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端読解のコマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず終端読解のコマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では SLIP コマンド 属性 は「SLIP コマンド 属性の用途を操作コマンドの表示で確認する終端読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景ではz/OS MVS Operationsの SLIP コマンド 属性と IEE457I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明だけに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では SLIP コマンド 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 上書追跡のコマンドで操作コマンドの運用確認を行います。SLIP コマンド (SET SLIP=xx)の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書追跡のコマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず上書追跡のコマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. SLIP コマンド (SET SLIP=xx)の属性行を読まず上書追跡のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のコマンドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のコマンドにおいて SLIP コマンド (SET SLIP=xx) は説明欄の「z/OS MVS Operationsで SLIP コマンド (SET SLIP=xx)の扱いを記録する上書追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のコマンドを受け取る担当者は、SLIP コマンド (SET SLIP=xx)の表示結果と IEE457I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のコマンドは別カテゴリの確認を流用しており、SLIP コマンド (SET SLIP=xx)の根拠にならないため上書追跡ではありません。 B: 上書追跡のコマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のコマンドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のコマンドが示す SLIP コマンド (SET SLIP=xx)は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SLIP コマンド (SET SLIP=xx)**

    - 検証目的: 変更照合のコマンドについて、SLIP コマンド (SET SLIP=xx)は、IEASLPxx を動的活性化し、定義済み SLIP トラップ群を一括導入するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、変更照合のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSLIP コマンド (SET SLIを指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SLIP コマンド (SET SLI
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SLIP コマンド (SET SLI
    CASE OSKB020040
    SOURCE z/OS MVS Operations
    ```

    SLIP コマンド (SET SLIとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020040を同じ出力で読み、変更照合のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020040 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020040   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SLIP コマンド (SET SLI と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SMF

### SET SMF=xx {#c22-i0260}
*分類: SET SMF*  ・  難易度: 上級

SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 呼出読解の操作コマンドで操作コマンドの運用確認を行います。SET SMF=xxの根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で呼出読解の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず呼出読解の操作コマンドを正常終了として記録する。
    - C. IEE457I を含む表示を保存し、説明欄との差分を呼出読解で確認する。 ✅
    - D. SET SMF=xxの属性行を読まず呼出読解の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では SET SMF=xx は「z/OS MVS Operationsで SET SMF=xxの扱いを記録する呼出読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では SET SMF=xxの表示結果と IEE457I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明だけに寄り、判定名は呼出読解不足です。呼出読解資料では SET SMF=xxの使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 終端追跡の操作コマンドに関係する SET SMF=xxの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 ✅
    - B. SET SMF=xxの名称と担当者名のみを残して終端追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で終端追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず終端追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡の操作コマンドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡の操作コマンドにおいて SET SMF=xx は説明欄の「SET SMF=xxの用途を操作コマンドの表示で確認する終端追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の操作コマンドに関連して、z/OS MVS Operationsでは SET SMF=xxの表示属性と IEE457I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の操作コマンドは別カテゴリの確認を流用しており、SET SMF=xxの根拠にならないため終端追跡ではありません。 D: 終端追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため終端追跡ではありません。終端追跡の操作コマンドで使う SET SMF=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **SET SMF=xx**

    - 検証目的: 出力照合の操作コマンドについて、SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040028の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMF=xxを指定し、OSKB040028の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SMF=xx
    CASE OSKB040028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SMF=xx
    CASE OSKB040028
    SOURCE z/OS MVS Operations
    ```

    SET SMF=xxとOSKB040028が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040028を同じ出力で読み、出力照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040028
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040028 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040028   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040028が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SMF=xx と OSKB040028 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **SET SMF=xx**

    - 検証目的: 復旧照合の操作コマンドについて、SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、復旧照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMF=xxを指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SMF=xx
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SMF=xx
    CASE OSKB020038
    SOURCE z/OS MVS Operations
    ```

    SET SMF=xxとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020038を同じ出力で読み、復旧照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020038 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020038   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SMF=xx と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET SMS

### SET SMS=xx {#c22-i0261}
*分類: SET SMS*  ・  難易度: 中級

SET SMS=xxは、IGDSMSxx を活性化し、ACS ルーチン・トレース、ACDS 切替などを反映する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 置換読解の操作コマンドに関する SET SMS=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず置換読解の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換読解の操作コマンドの証跡として保存して根拠にする。
    - C. SET SMS=xxの変更点を出力本文から切り離して置換読解の操作コマンドの承認欄だけ残す。
    - D. D OPDATA の結果から対象行を抜き出し、置換読解の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では SET SMS=xx は「SET SMS=xxの状態と出力メッセージを結び付ける置換読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では SET SMS=xxの出力行と IEE457I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明だけに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では SET SMS=xxをz/OS MVS Operationsの確認記録に残し、対象名は置換読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 探索追跡の操作コマンドで SET SMS=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET SMS=xxの出力を取らず探索追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 ✅
    - C. D OPDATA を省略して探索追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡の操作コマンドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の操作コマンドにおいて SET SMS=xx は説明欄の「探索追跡の操作コマンドに関係する定義値と表示行を照合する探索追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の操作コマンドの証跡を読む担当者は、SET SMS=xxの属性行と IEE457I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の操作コマンドは別カテゴリの確認を流用しており、SET SMS=xxの根拠にならないため探索追跡ではありません。探索追跡の操作コマンドに出る SET SMS=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET SMS=xx**

    - 検証目的: 監査照合の操作コマンドについて、SET SMS=xxは、IGDSMSxx を活性化し、ACS ルーチン・トレース、ACDS 切替などを反映するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、監査照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMS=xxを指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET SMS=xx
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET SMS=xx
    CASE OSKB020039
    SOURCE z/OS MVS Operations
    ```

    SET SMS=xxとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020039を同じ出力で読み、監査照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020039 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020039   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET SMS=xx と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET TIME

### SET DATE=yyyy.ddd {#c22-i0262}
*分類: SET TIME*  ・  難易度: 中級

SET DATE=yyyy.dddは、MVS オペレータコマンドのSET TIMEで確認する項目です。ユリウス日形式でシステム日付を更新する。SET TIME と組み合わせて使用される

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 上書読解の操作コマンドで操作コマンドの運用確認を行います。SET 属性の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書読解の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず上書読解の操作コマンドを正常終了として記録する。
    - C. 同じ画面で対象行と IEE115I を読み、上書読解の結果として保存する。 ✅
    - D. SET 属性の属性行を読まず上書読解の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では SET 属性 は「z/OS MVS Operationsで SET 属性の扱いを記録する上書読解項目」と D A,L または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では SET 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明だけに寄り、判定名は上書読解不足です。上書読解資料では SET 属性の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 条件追跡の操作コマンドに関係する SET DATE=yyyy.dddの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. SET DATE=yyyy.dddの名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて SET DATE=yyyy.ddd は説明欄の「SET DATE=yyyy.dddの用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは SET DATE=yyyy.dddの表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、SET DATE=yyyy.dddの根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う SET DATE=yyyy.dddという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET DATE=yyyy.ddd**

    - 検証目的: 展開追跡の操作コマンドについて、SET DATE=yyyy.dddは、MVS オペレータコマンドの SET TIME で確認する項目です。ユリウス日形式でシステム日付を更新する。SET TIME と組み合わせに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、展開追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET DATE=yyyy.dddを指定し、OSKB020042の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET DATE=yyyy.ddd
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET DATE=yyyy.ddd
    CASE OSKB020042
    SOURCE z/OS MVS Operations
    ```

    SET DATE=yyyy.dddとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020042を同じ出力で読み、展開追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020042 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020042   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SET DATE=yyyy.ddd と OSKB020042 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SET TIME=hh.mm.ss {#c22-i0263}
*分類: SET TIME*  ・  難易度: 中級

SET TIME=hh.mm.ssは、MVS オペレータコマンドのSET TIMEで確認する項目です。システム時刻の手動更新。STP/Sysplex Timer 配下では通常使用せず、独立システムでの矯正に限定する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 探索読解の操作コマンドで SET 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET 属性の出力を取らず探索読解の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索読解の根拠にする。 ✅
    - C. D OPDATA を省略して探索読解の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索読解の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では SET 属性 は「探索読解の操作コマンドに関係する定義値と表示行を照合する探索読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では SET 属性の属性行と IEE457I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明だけに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では SET 属性を MVS オペレータコマンドの運用手順で確認し、初出名は探索読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 出力追跡の操作コマンドに関する SET TIME=hh.mm.ssの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。
    - C. SET TIME=hh.mm.ssの変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて SET TIME=hh.mm.ss は説明欄の「SET TIME=hh.mm.ssの状態と出力メッセージを結び付ける出力追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、SET TIME=hh.mm.ssの出力行と IEE457I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、SET TIME=hh.mm.ssの根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する SET TIME=hh.mm.ssはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET TIME=hh.mm.ss**

    - 検証目的: 構文追跡の操作コマンドについて、SET TIME=hh.mm.ssは、MVS オペレータコマンドの SET TIME で確認する項目です。システム時刻の手動更新。STP/Sysplex Timer 配下では通に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、構文追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET TIME=hh.mm.ssを指定し、OSKB020041の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET TIME=hh.mm.ss
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET TIME=hh.mm.ss
    CASE OSKB020041
    SOURCE z/OS MVS Operations
    ```

    SET TIME=hh.mm.ssとOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020041を同じ出力で読み、構文追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020041 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020041   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET TIME=hh.mm.ss と OSKB020041 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET TRACE

### SET TRACE,ON {#c22-i0264}
*分類: SET TRACE*  ・  難易度: 上級

SET TRACE,ONは、MVS オペレータコマンドのSET TRACEで確認する項目です。システム・トレースを動的に有効化する基本形。バッファサイズ・対象 ASID も同時に指定可能

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力読解の操作コマンドに関する SET TRACE,ON の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力読解の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力読解の操作コマンドの証跡として保存して根拠にする。
    - C. SET TRACE,ON の変更点を出力本文から切り離して出力読解の操作コマンドの承認欄だけ残す。
    - D. D A,L で得た表示本文を使い、出力読解の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では SET TRACE,ON は「SET TRACE,ON の状態と出力メッセージを結び付ける出力読解項目」と D A,L または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では SET TRACE,ON の出力行と IEE115I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明だけに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では SET TRACE,ON をz/OS MVS Operationsの確認記録に残し、対象名は出力読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切追跡の操作コマンドで SET TRACE,ON の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET TRACE,ON の出力を取らず区切追跡の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 ✅
    - C. D A,L を省略して区切追跡の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡の操作コマンドにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡の操作コマンドにおいて SET TRACE,ON は説明欄の「区切追跡の操作コマンドに関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の操作コマンドの証跡を読む担当者は、SET TRACE,ON の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の操作コマンドは別カテゴリの確認を流用しており、SET TRACE,ON の根拠にならないため区切追跡ではありません。区切追跡の操作コマンドに出る SET TRACE,ON は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET TRACE,ON**

    - 検証目的: 呼出追跡の操作コマンドについて、SET TRACE,ON は、MVS オペレータコマンドの SET TRACE で確認する項目です。システム・トレースを動的に有効化する基本形。バッファサイズ・対象 ASID もに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET TRACE,ONを指定し、OSKB020043の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET TRACE,ON
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET TRACE,ON
    CASE OSKB020043
    SOURCE z/OS MVS Operations
    ```

    SET TRACE,ONとOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020043を同じ出力で読み、呼出追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020043 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020043   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の SET TRACE,ON と OSKB020043 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### TRACE CT (CTRACE 動的) {#c22-i0265}
*分類: SET TRACE*  ・  難易度: 上級

TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件読解の動的に関係する TRACE CT 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件読解として引き継ぐ。 ✅
    - B. TRACE CT 属性の名称と担当者名だけを残して条件読解の動的の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件読解の動的を確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件読解の動的の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では TRACE CT 属性 は「TRACE CT 属性の用途を操作コマンドの表示で確認する条件読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景ではz/OS MVS Operationsの TRACE CT 属性と IEE457I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明だけに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では TRACE CT 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **TRACE CT (CTRACE 動的)**

    - 検証目的: 条件照合の動的について、TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040029の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、条件照合の動的の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRACE CT (CTRACE 動を指定し、OSKB040029の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRACE CT (CTRACE 動
    CASE OSKB040029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRACE CT (CTRACE 動
    CASE OSKB040029
    SOURCE z/OS MVS Operations
    ```

    TRACE CT (CTRACE 動とOSKB040029が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040029を同じ出力で読み、条件照合の動的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB040029
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB040029 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040029   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB040029が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の TRACE CT (CTRACE 動 と OSKB040029 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB040029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **TRACE CT (CTRACE 動的)**

    - 検証目的: 置換追跡の動的について、TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、置換追跡の動的の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRACE CT (CTRACE 動を指定し、OSKB020044の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRACE CT (CTRACE 動
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRACE CT (CTRACE 動
    CASE OSKB020044
    SOURCE z/OS MVS Operations
    ```

    TRACE CT (CTRACE 動とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020044を同じ出力で読み、置換追跡の動的の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020044 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020044   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の TRACE CT (CTRACE 動 と OSKB020044 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SET XCF

### SET XCF=xx {#c22-i0266}
*分類: SET XCF*  ・  難易度: 中級

SET XCF=xxは、COUPLExx を再活性化し、Sysplex の Couple DS 設定や SFM/CFRM ポリシー名の動的入替を行う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 区切読解の操作コマンドで SET XCF=xxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SET XCF=xxの出力を取らず区切読解の操作コマンドの説明文と承認印だけを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切読解の確認にする。 ✅
    - C. D OPDATA を省略して区切読解の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切読解の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では SET XCF=xx は「区切読解の操作コマンドに関係する定義値と表示行を照合する区切読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では SET XCF=xxの属性行と IEE457I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明だけに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では SET XCF=xxを MVS オペレータコマンドの運用手順で確認し、初出名は区切読解初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SET XCF=xx**

    - 検証目的: 終端追跡の操作コマンドについて、SET XCF=xxは、COUPLExx を再活性化し、Sysplex の Couple DS 設定や SFM/CFRM ポリシー名の動的入替を行うに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、終端追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSET XCF=xxを指定し、OSKB020045の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SET XCF=xx
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SET XCF=xx
    CASE OSKB020045
    SOURCE z/OS MVS Operations
    ```

    SET XCF=xxとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020045 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020045   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SET XCF=xx と OSKB020045 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETXCF COUPLE,ACOUPLE=dsn {#c22-i0267}
*分類: SET XCF*  ・  難易度: 中級

SETXCF COUPLE,ACOUPLE=dsnは、予備 Couple DS を動的に追加し、PSWITCH で本番側に昇格させる無停止切替手順を構成する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 記録読解の操作コマンドに関係する SETXCF COUPLE 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、記録読解の確認値として扱う。 ✅
    - B. SETXCF COUPLE 命令の名称と担当者名だけを残して記録読解の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で記録読解の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず記録読解の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では SETXCF COUPLE 命令 は「SETXCF COUPLE 命令の用途を操作コマンドの表示で確認する記録読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景ではz/OS MVS Operationsの SETXCF COUPLE 命令と IEE457I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明だけに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では SETXCF COUPLE 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録読解用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETXCF COUPLE,ACOUPLE=dsn**

    - 検証目的: 出力追跡の操作コマンドについて、SETXCF COUPLE,ACOUPLE=dsnは、予備 Couple DS を動的に追加し、PSWITCH で本番側に昇格させる無停止切替手順を構成するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、出力追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF COUPLE,ACOUを指定し、OSKB020048の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETXCF COUPLE,ACOU
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETXCF COUPLE,ACOU
    CASE OSKB020048
    SOURCE z/OS MVS Operations
    ```

    SETXCF COUPLE,ACOUとOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020048を同じ出力で読み、出力追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020048 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020048   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SETXCF COUPLE,ACOU と OSKB020048 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETXCF MODIFY,STRNAME=name {#c22-i0268}
*分類: SET XCF*  ・  難易度: 中級

SETXCF MODIFY,STRNAME=nameは、CF 構造のサイズ・配置を動的に変更する (リビルド要因)

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先読解の操作コマンドに関する SETXCF MODIFY 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず優先読解の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先読解の操作コマンドの証跡として保存して根拠にする。
    - C. SETXCF MODIFY 命令の変更点を出力本文から切り離して優先読解の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先読解で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では SETXCF MODIFY 命令 は「SETXCF MODIFY 命令の状態と出力メッセージを結び付ける優先読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では SETXCF MODIFY 命令の出力行と IEE457I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明だけに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では SETXCF MODIFY 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先読解対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETXCF MODIFY,STRNAME=name**

    - 検証目的: 上書追跡の操作コマンドについて、SETXCF MODIFY,STRNAME=nameは、CF 構造のサイズ・配置を動的に変更する (リビルド要因)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、上書追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF MODIFY,STRNを指定し、OSKB020047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETXCF MODIFY,STRN
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETXCF MODIFY,STRN
    CASE OSKB020047
    SOURCE z/OS MVS Operations
    ```

    SETXCF MODIFY,STRNとOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020047 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020047   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SETXCF MODIFY,STRN と OSKB020047 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### SETXCF START,POLICY,TYPE=type {#c22-i0269}
*分類: SET XCF*  ・  難易度: 上級

CFRM/SFM/LOGR/ARM の新規ポリシーを活性化する動的コマンド。SET XCF とは別系統だがセットで使われる

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 範囲読解の操作コマンドで操作コマンドの運用確認を行います。SETXCF START 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲読解の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず範囲読解の操作コマンドを正常終了として記録する。
    - C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲読解の点検結果を残す。 ✅
    - D. SETXCF START 命令の属性行を読まず範囲読解の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では SETXCF START 命令 は「z/OS MVS Operationsで SETXCF START 命令の扱いを記録する範囲読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では SETXCF START 命令の表示結果と IEE457I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明だけに寄り、判定名は範囲読解不足です。範囲読解資料では SETXCF START 命令の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **SETXCF START,POLICY,TYPE=type**

    - 検証目的: 探索追跡の操作コマンドについて、CFRM/SFM/LOGR/ARM の新規ポリシーを活性化する動的コマンド。SET XCF とは別系統だがセットで使われるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、探索追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF START,POLICを指定し、OSKB020046の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SETXCF START,POLIC
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SETXCF START,POLIC
    CASE OSKB020046
    SOURCE z/OS MVS Operations
    ```

    SETXCF START,POLICとOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020046 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020046   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の SETXCF START,POLIC と OSKB020046 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > STOPMN

### STOPMN JOBNAMES {#c22-i0270}
*分類: STOPMN*  ・  難易度: 中級

STOPMN JOBNAMESは、MVS オペレータコマンドのSTOPMNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 出力判定の操作コマンドに関する STOPMN JOBNAMES の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力判定の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力判定の操作コマンドの証跡として保存して根拠にする。
    - C. STOPMN JOBNAMES の変更点を出力本文から切り離して出力判定の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力判定の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力判定の操作コマンドにおいて選択記号 D を採用し、識別名は出力判定です。出力判定の操作コマンドにおいて STOPMN JOBNAMES は説明欄の「STOPMN JOBNAMES の状態と出力メッセージを結び付ける出力判定項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力判定です。出力判定の操作コマンドに関する記録は、STOPMN JOBNAMES の出力行と IEE457I を一緒に保存し、背景名は出力判定です。選択肢ごとの違いを示します。 A: 出力判定の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力判定ではありません。 B: 出力判定の操作コマンドは別カテゴリの確認を流用しており、STOPMN JOBNAMES の根拠にならないため出力判定ではありません。 C: 出力判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力判定ではありません。 D: 出力判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力判定です。出力判定の操作コマンドで記録する STOPMN JOBNAMES はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **STOPMN JOBNAMES**

    - 検証目的: 構文検査の操作コマンドについて、STOPMN JOBNAMES は、MVS オペレータコマンドの STOPMN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030061の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、構文検査の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSTOPMN JOBNAMESを指定し、OSKB030061の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND STOPMN JOBNAMES
    CASE OSKB030061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM STOPMN JOBNAMES
    CASE OSKB030061
    SOURCE z/OS MVS Operations
    ```

    STOPMN JOBNAMESとOSKB030061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030061を同じ出力で読み、構文検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030061
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030061 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030061   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の STOPMN JOBNAMES と OSKB030061 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### STOPMN STATUS {#c22-i0271}
*分類: STOPMN*  ・  難易度: 中級

STOPMN STATUSは、MVS オペレータコマンドのSTOPMNで確認する項目です。MN STATUS を停止する。継続使用は SYSLOG 肥大化のため必要に応じてオフにする

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 条件判定の操作コマンドに関係する STOPMN STATUS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件判定として残す。 ✅
    - B. STOPMN STATUS の名称と担当者名のみを残して条件判定の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で条件判定の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず条件判定の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定の操作コマンドにおいて選択記号 A を採用し、識別名は条件判定です。条件判定の操作コマンドにおいて STOPMN STATUS は説明欄の「STOPMN STATUS の用途を操作コマンドの表示で確認する条件判定項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は条件判定です。条件判定の操作コマンドに関連して、z/OS MVS Operationsでは STOPMN STATUS の表示属性と IEE457I を同じ証跡に残し、背景名は条件判定です。他の選択肢を確認します。 A: 条件判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件判定です。 B: 条件判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件判定ではありません。 C: 条件判定の操作コマンドは別カテゴリの確認を流用しており、STOPMN STATUS の根拠にならないため条件判定ではありません。 D: 条件判定の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため条件判定ではありません。条件判定の操作コマンドで使う STOPMN STATUS という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件判定です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **STOPMN STATUS**

    - 検証目的: 展開検査の操作コマンドについて、STOPMN STATUS は、MVS オペレータコマンドの STOPMN で確認する項目です。MN STATUS を停止する。継続使用は SYSLOG 肥大化のため必要に応じてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030062の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、展開検査の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSTOPMN STATUSを指定し、OSKB030062の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND STOPMN STATUS
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM STOPMN STATUS
    CASE OSKB030062
    SOURCE z/OS MVS Operations
    ```

    STOPMN STATUSとOSKB030062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030062を同じ出力で読み、展開検査の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030062 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030062   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の STOPMN STATUS と OSKB030062 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > SYMBOL

### &SYSCLONE {#c22-i0272}
*分類: SYMBOL*  ・  難易度: 中級

&SYSCLONEは、MVS オペレータコマンドのSYMBOLで確認する項目です。SYSNAME の 2 桁短縮 (CLONE) を返すシステム・シンボル。DSN プレフィックス分離などに使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 比較検査の操作コマンドで&SYSCLONE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. &SYSCLONE の出力を取らず比較検査の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較検査の確認結果にする。 ✅
    - C. D A,L を省略して比較検査の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査の操作コマンドにおいて選択記号 B を採用し、識別名は比較検査です。比較検査の操作コマンドにおいて&SYSCLONE は説明欄の「比較検査の操作コマンドに関係する定義値と表示行を照合する比較検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較検査です。比較検査の操作コマンドの証跡を読む担当者は、&SYSCLONE の属性行と IEE115I を合わせて追跡し、背景名は比較検査です。誤答側の問題点を分けます。 A: 比較検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較検査ではありません。 B: 比較検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較検査です。 C: 比較検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較検査ではありません。 D: 比較検査の操作コマンドは別カテゴリの確認を流用しており、&SYSCLONE の根拠にならないため比較検査ではありません。比較検査の操作コマンドに出る&SYSCLONE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSCLONE**

    - 検証目的: 上書追跡の操作コマンドについて、&SYSCLONE は、MVS オペレータコマンドの SYMBOL で確認する項目です。SYSNAME の 2 桁短縮 (CLONE) を返すシステム・シンボル。DSN プレフィに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030047の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、上書追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSCLONEを指定し、OSKB030047の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSCLONE
    CASE OSKB030047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSCLONE
    CASE OSKB030047
    SOURCE z/OS MVS Operations
    ```

    &SYSCLONEとOSKB030047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030047
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030047 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030047   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSCLONE と OSKB030047 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### &SYSNAME {#c22-i0273}
*分類: SYMBOL*  ・  難易度: 中級

&SYSNAMEは、MVS オペレータコマンドのSYMBOLで確認する項目です。Sysplex システム名を返すシステム・シンボル。PARMLIB / JCL / EXEC の汎用化に最頻出

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 優先検査の操作コマンドに関する&SYSNAME の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先検査の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の操作コマンドの証跡として保存して根拠にする。
    - C. &SYSNAME の変更点を出力本文から切り離して優先検査の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査の操作コマンドにおいて選択記号 D を採用し、識別名は優先検査です。優先検査の操作コマンドにおいて&SYSNAME は説明欄の「&SYSNAME の状態と出力メッセージを結び付ける優先検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査の操作コマンドに関する記録は、&SYSNAME の出力行と IEE115I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先検査ではありません。 B: 優先検査の操作コマンドは別カテゴリの確認を流用しており、&SYSNAME の根拠にならないため優先検査ではありません。 C: 優先検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査の操作コマンドで記録する&SYSNAME はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSNAME**

    - 検証目的: 終端追跡の操作コマンドについて、&SYSNAME は、MVS オペレータコマンドの SYMBOL で確認する項目です。Sysplex システム名を返すシステム・シンボル。PARMLIB / JCL / EXECに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030045の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSNAMEを指定し、OSKB030045の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSNAME
    CASE OSKB030045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSNAME
    CASE OSKB030045
    SOURCE z/OS MVS Operations
    ```

    &SYSNAMEとOSKB030045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030045
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030045 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030045   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSNAME と OSKB030045 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### &SYSPLEX {#c22-i0274}
*分類: SYMBOL*  ・  難易度: 中級

&SYSPLEXは、MVS オペレータコマンドのSYMBOLで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 記録検査の操作コマンドに関係する&SYSPLEX の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、記録検査として残す。 ✅
    - B. &SYSPLEX の名称と担当者名のみを残して記録検査の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で記録検査の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず記録検査の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査の操作コマンドにおいて選択記号 A を採用し、識別名は記録検査です。記録検査の操作コマンドにおいて&SYSPLEX は説明欄の「&SYSPLEX の用途を操作コマンドの表示で確認する記録検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録検査です。記録検査の操作コマンドに関連して、z/OS MVS Operationsでは&SYSPLEX の表示属性と IEE115I を同じ証跡に残し、背景名は記録検査です。他の選択肢を確認します。 A: 記録検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録検査です。 B: 記録検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録検査ではありません。 C: 記録検査の操作コマンドは別カテゴリの確認を流用しており、&SYSPLEX の根拠にならないため記録検査ではありません。 D: 記録検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録検査ではありません。記録検査の操作コマンドで使う&SYSPLEX という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSPLEX**

    - 検証目的: 探索追跡の操作コマンドについて、&SYSPLEX は、MVS オペレータコマンドの SYMBOL で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030046の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、探索追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSPLEXを指定し、OSKB030046の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSPLEX
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSPLEX
    CASE OSKB030046
    SOURCE z/OS MVS Operations
    ```

    &SYSPLEXとOSKB030046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030046
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030046 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030046   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSPLEX と OSKB030046 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### &SYSR1 {#c22-i0275}
*分類: SYMBOL*  ・  難易度: 中級

&SYSR1は、MVS オペレータコマンドのSYMBOLで確認する項目です。IPL 装置のボリュームシリアル (SYSRES) を返すシステム・シンボル。PARMLIB 直接参照時に使う

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 順序検査の操作コマンドで操作コマンドの運用確認を行います。&SYSR1 の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序検査の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず順序検査の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序検査の記録として扱う。 ✅
    - D. &SYSR1 の属性行を読まず順序検査の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序検査の操作コマンドにおいて選択記号 C を採用し、識別名は順序検査です。順序検査の操作コマンドにおいて&SYSR1 は説明欄の「z/OS MVS Operationsで&SYSR1 の扱いを記録する順序検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序検査です。順序検査の操作コマンドを受け取る担当者は、&SYSR1 の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序検査です。不適切な選択肢を整理します。 A: 順序検査の操作コマンドは別カテゴリの確認を流用しており、&SYSR1 の根拠にならないため順序検査ではありません。 B: 順序検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序検査ではありません。 C: 順序検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので順序検査です。 D: 順序検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序検査ではありません。順序検査の操作コマンドが示す&SYSR1 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **&SYSR1**

    - 検証目的: 出力追跡の操作コマンドについて、&SYSR1 は、MVS オペレータコマンドの SYMBOL で確認する項目です。IPL 装置のボリュームシリアル (SYSRES) を返すシステム・シンボル。PARMLIB 直に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030048の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、出力追跡の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に&SYSR1を指定し、OSKB030048の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND &SYSR1
    CASE OSKB030048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM &SYSR1
    CASE OSKB030048
    SOURCE z/OS MVS Operations
    ```

    &SYSR1とOSKB030048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030048を同じ出力で読み、出力追跡の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030048
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030048 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030048   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の &SYSR1 と OSKB030048 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### D SYMBOLS 表示 {#c22-i0276}
*分類: SYMBOL*  ・  難易度: 中級

D SYMBOLS 表示は、MVS オペレータコマンドのSYMBOLで確認する項目です。現在解決可能なシステム・シンボルとその値を一覧表示するコマンド。PARMLIB の汎用化チェックに必須

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 値域検査の表示に関する D SYMBOLS 表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域検査の表示の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の表示の証跡として保存して根拠にする。
    - C. D SYMBOLS 表示の変更点を出力本文から切り離して値域検査の表示の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域検査の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査の表示において選択記号 D を採用し、識別名は値域検査です。値域検査の表示において D SYMBOLS 表示 は説明欄の「D SYMBOLS 表示の状態と出力メッセージを結び付ける値域検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査の表示に関する記録は、D SYMBOLS 表示の出力行と IEE115I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査の表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域検査ではありません。 B: 値域検査の表示は別カテゴリの確認を流用しており、D SYMBOLS 表示の根拠にならないため値域検査ではありません。 C: 値域検査の表示は名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査の表示は対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査の表示で記録する D SYMBOLS 表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **D SYMBOLS 表示**

    - 検証目的: 条件追跡の表示について、D SYMBOLS 表示は、MVS オペレータコマンドの SYMBOL で確認する項目です。現在解決可能なシステム・シンボルとその値を一覧表示するコマンド。PARMLIB の汎に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030049の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、条件追跡の表示の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にD SYMBOLS 表示を指定し、OSKB030049の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND D SYMBOLS 表示
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM D SYMBOLS 表示
    CASE OSKB030049
    SOURCE z/OS MVS Operations
    ```

    D SYMBOLS 表示とOSKB030049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030049を同じ出力で読み、条件追跡の表示の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030049
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030049 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030049   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の D SYMBOLS 表示 と OSKB030049 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### IEASYMxx での定義 {#c22-i0277}
*分類: SYMBOL*  ・  難易度: 中級

IEASYMxx での定義は、MVS オペレータコマンドのSYMBOLで確認する項目です。ユーザ・シンボル (&USRSYM 等) は IEASYMxx で定義する。LOAD パラメータの 3 桁目で SUFFIX を選ぶ

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 警告検査のでの定義に関係する IEASYMxx での定義の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告検査として残す。 ✅
    - B. IEASYMxx での定義の名称と担当者名のみを残して警告検査のでの定義の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告検査のでの定義を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告検査のでの定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査のでの定義において選択記号 A を採用し、識別名は警告検査です。警告検査のでの定義において IEASYMxx での定義 は説明欄の「IEASYMxx での定義の用途を操作コマンドの表示で確認する警告検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査のでの定義に関連して、z/OS MVS Operationsでは IEASYMxx での定義の表示属性と IEE115I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査のでの定義は対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査のでの定義は名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査のでの定義は別カテゴリの確認を流用しており、IEASYMxx での定義の根拠にならないため警告検査ではありません。 D: 警告検査のでの定義は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告検査ではありません。警告検査のでの定義で使う IEASYMxx での定義という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **IEASYMxx での定義**

    - 検証目的: 区切追跡のの定義について、IEASYMxx での定義は、MVS オペレータコマンドの SYMBOL で確認する項目です。ユーザ・シンボル (&USRSYM 等) は IEASYMxx で定義する。LOAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切追跡のの定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIEASYMxx での定義を指定し、OSKB040050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IEASYMxx での定義
    CASE OSKB040050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IEASYMxx での定義
    CASE OSKB040050
    SOURCE z/OS MVS Operations
    ```

    IEASYMxx での定義とOSKB040050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040050を同じ出力で読み、区切追跡のの定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040050 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040050   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の IEASYMxx での定義 と OSKB040050 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **IEASYMxx での定義**

    - 検証目的: 区切追跡のでの定義について、IEASYMxx での定義は、MVS オペレータコマンドの SYMBOL で確認する項目です。ユーザ・シンボル (&USRSYM 等) は IEASYMxx で定義する。LOAに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030050の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切追跡のでの定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIEASYMxx での定義を指定し、OSKB030050の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IEASYMxx での定義
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IEASYMxx での定義
    CASE OSKB030050
    SOURCE z/OS MVS Operations
    ```

    IEASYMxx での定義とOSKB030050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030050を同じ出力で読み、区切追跡のでの定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030050
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030050 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030050   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の IEASYMxx での定義 と OSKB030050 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > TRACK

### TRACK 全体 {#c22-i0278}
*分類: TRACK*  ・  難易度: 中級

TRACK 全体は、TRACK コマンドで現在稼働中のアドレス・スペース活動とハードウェア利用状況を 1 行ずつ追跡表示する

**出典:** z / OS MVS System Commands

??? question "確認問題（1問）"
    **問題.** 構文検査の全体に関係する TRACK 全体の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文検査として残す。 ✅
    - B. TRACK 全体の名称と担当者名のみを残して構文検査の全体の表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で構文検査の全体を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず構文検査の全体の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査の全体において選択記号 A を採用し、識別名は構文検査です。構文検査の全体において TRACK 全体 は説明欄の「TRACK 全体の用途を操作コマンドの表示で確認する構文検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文検査です。構文検査の全体に関連して、z/OS MVS Operationsでは TRACK 全体の表示属性と IEE115I を同じ証跡に残し、背景名は構文検査です。他の選択肢を確認します。 A: 構文検査の全体は対象出力と項目説明を結び、根拠を残すので構文検査です。 B: 構文検査の全体は名称や説明のみに寄り、状態を示す出力本文が不足するため構文検査ではありません。 C: 構文検査の全体は別カテゴリの確認を流用しており、TRACK 全体の根拠にならないため構文検査ではありません。 D: 構文検査の全体は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文検査ではありません。構文検査の全体で使う TRACK 全体という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文検査です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **TRACK 全体**

    - 検証目的: 比較照合の全体について、TRACK 全体は、TRACK コマンドで現在稼働中のアドレス・スペース活動とハードウェア利用状況を 1 行ずつ追跡表示するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、比較照合の全体の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTRACK 全体を指定し、OSKB030034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND TRACK 全体
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM TRACK 全体
    CASE OSKB030034
    SOURCE z/OS MVS Operations
    ```

    TRACK 全体とOSKB030034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030034を同じ出力で読み、比較照合の全体の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030034
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030034 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030034   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の TRACK 全体 と OSKB030034 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V CN

### V CN(*),ACTIVATE {#c22-i0279}
*分類: V CN*  ・  難易度: 中級

V CN(*),ACTIVATEは、全ての該当コンソールを一括処理する形式 (発行コンソール側で扱える対象に限定)

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 警告照合再の*に関係する V CN(*) 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、警告照合再の確認記録にまとめる。 ✅
    - B. V CN(*) 命令の名称と担当者名だけを残して警告照合再の*の表示本文を対象から外す。
    - C. 操作コマンド以外の画面で警告照合再の*を確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告照合再の*の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合再正解では選択記号 A を採用し、正解名は警告照合再正解です。警告照合再根拠では V CN(*) 命令 は「V CN(*) 命令の用途を操作コマンドの表示で確認する警告照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は警告照合再根拠です。警告照合再背景ではz/OS MVS Operationsの V CN(*) 命令と IEE115I を同じ証跡に残し、背景名は警告照合再背景です。他の選択肢を確認します。 A: 警告照合再正答は対象出力と項目説明を結び、根拠名は警告照合再正答です。 B: 警告照合再不足は名称や説明だけに寄り、判定名は警告照合再不足です。 C: 警告照合再流用は別カテゴリの確認であり、排除名は警告照合再流用です。 D: 警告照合再欠落は戻り値や記録番号に寄り、欠落名は警告照合再欠落です。警告照合再用語では V CN(*) 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は警告照合再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 監査確認の*で操作コマンドの運用確認を行います。V CN(*),ACTIVATE の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で監査確認の*を確認した扱いにする。
    - B. IEE115I の有無を確認せず監査確認の*を正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査確認の記録として扱う。 ✅
    - D. V CN(*),ACTIVATE の属性行を読まず監査確認の*の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認の*において選択記号 C を採用し、識別名は監査確認です。監査確認の*において V CN(*),ACTIVATE は説明欄の「z/OS MVS Operationsで V CN(*),ACTIVATE の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の*を受け取る担当者は、V CN(*),ACTIVATE の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の*は別カテゴリの確認を流用しており、V CN(*),ACTIVATE の根拠にならないため監査確認ではありません。 B: 監査確認の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査確認ではありません。 C: 監査確認の*は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の*は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の*が示す V CN(*),ACTIVATE は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CN(*),ACTIVATE**

    - 検証目的: 優先整理の*について、V CN(*),ACTIVATE は、全ての該当コンソールを一括処理する形式 (発行コンソール側で扱える対象に限定)に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、優先整理の*の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(*),ACTIVATEを指定し、OSKB020112の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(*),ACTIVATE
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(*),ACTIVATE
    CASE OSKB020112
    SOURCE z/OS MVS Operations
    ```

    V CN(*),ACTIVATEとOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020112を同じ出力で読み、優先整理の*の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020112 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020112   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(*),ACTIVATE と OSKB020112 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V CN(name),ACTIVE {#c22-i0280}
*分類: V CN*  ・  難易度: 中級

V CN(name),ACTIVEは、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにする

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 順序照合再の操作コマンドで操作コマンドの運用確認を行います。V CN(name) 命令の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で順序照合再の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず順序照合再の操作コマンドを正常終了として記録する。
    - C. IEE115I を含む表示を保存し、説明欄との差分を順序照合再で確認する。 ✅
    - D. V CN(name) 命令の属性行を読まず順序照合再の操作コマンドの画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合再正解では選択記号 C を採用し、正解名は順序照合再正解です。順序照合再根拠では V CN(name) 命令 は「z/OS MVS Operationsで V CN(name) 命令の扱いを記録する順序照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は順序照合再根拠です。順序照合再受渡では V CN(name) 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序照合再受渡です。不適切な選択肢を整理します。 A: 順序照合再流用は別カテゴリの確認であり、排除名は順序照合再流用です。 B: 順序照合再欠落は戻り値や記録番号に寄り、欠落名は順序照合再欠落です。 C: 順序照合再正答は対象出力と項目説明を結び、根拠名は順序照合再正答です。 D: 順序照合再不足は名称や説明だけに寄り、判定名は順序照合再不足です。順序照合再資料では V CN(name) 命令の使い方を出典欄から追跡し、資料名は順序照合再資料です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 警告確認の操作コマンドに関係する V CN(name),ACTIVE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 ✅
    - B. V CN(name),ACTIVE の名称と担当者名のみを残して警告確認の操作コマンドの表示本文を確認対象に含めない。
    - C. 操作コマンド以外の画面で警告確認の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず警告確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認の操作コマンドにおいて選択記号 A を採用し、識別名は警告確認です。警告確認の操作コマンドにおいて V CN(name),ACTIVE は説明欄の「V CN(name),ACTIVE の用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の操作コマンドに関連して、z/OS MVS Operationsでは V CN(name),ACTIVE の表示属性と IEE115I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),ACTIVE の根拠にならないため警告確認ではありません。 D: 警告確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告確認ではありません。警告確認の操作コマンドで使う V CN(name),ACTIVE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（2件）"
    **V CN(name),ACTIVE**

    - 検証目的: 変更照合の操作コマンドについて、V CN(name),ACTIVE は、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにするに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040040の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、変更照合の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),ACTIVEを指定し、OSKB040040の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),ACTIVE
    CASE OSKB040040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),ACTIVE
    CASE OSKB040040
    SOURCE z/OS MVS Operations
    ```

    V CN(name),ACTIVEとOSKB040040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040040を同じ出力で読み、変更照合の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB040040
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB040040 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB040040   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB040040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),ACTIVE と OSKB040040 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB040040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands

    ---

    **V CN(name),ACTIVE**

    - 検証目的: 区切整理の操作コマンドについて、V CN(name),ACTIVE は、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにするに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、区切整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),ACTIVEを指定し、OSKB020110の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),ACTIVE
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),ACTIVE
    CASE OSKB020110
    SOURCE z/OS MVS Operations
    ```

    V CN(name),ACTIVEとOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020110を同じ出力で読み、区切整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020110 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020110   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),ACTIVE と OSKB020110 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V CN(name),AUTH=MASTER {#c22-i0281}
*分類: V CN*  ・  難易度: 中級

V CN(name),AUTH=MASTERは、MVS オペレータコマンドのV CNで確認する項目です。コンソール権限をマスタ・コンソールに昇格させる動的変更

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 値域照合再の操作コマンドに関する V CN 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず値域照合再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを値域照合再の操作コマンドの証跡として保存して根拠にする。
    - C. V CN 属性の変更点を出力本文から切り離して値域照合再の操作コマンドの承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、値域照合再の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合再正解では選択記号 D を採用し、正解名は値域照合再正解です。値域照合再根拠では V CN 属性 は「V CN 属性の状態と出力メッセージを結び付ける値域照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は値域照合再根拠です。値域照合再保存では V CN 属性の出力行と IEE115I を一緒に残し、保存名は値域照合再保存です。選択肢ごとの違いを示します。 A: 値域照合再欠落は戻り値や記録番号に寄り、欠落名は値域照合再欠落です。 B: 値域照合再流用は別カテゴリの確認であり、排除名は値域照合再流用です。 C: 値域照合再不足は名称や説明だけに寄り、判定名は値域照合再不足です。 D: 値域照合再正答は対象出力と項目説明を結び、根拠名は値域照合再正答です。値域照合再対象では V CN 属性をz/OS MVS Operationsの確認記録に残し、対象名は値域照合再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 復旧確認の操作コマンドで V CN(name),AUTH=MASTER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V CN(name),AUTH=MASTER の出力を取らず復旧確認の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 ✅
    - C. D A,L を省略して復旧確認の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認の操作コマンドにおいて選択記号 B を採用し、識別名は復旧確認です。復旧確認の操作コマンドにおいて V CN(name),AUTH=MASTER は説明欄の「復旧確認の操作コマンドに関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の操作コマンドの証跡を読む担当者は、V CN(name),AUTH=MASTER の属性行と IEE115I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),AUTH=MASTER の根拠にならないため復旧確認ではありません。復旧確認の操作コマンドに出る V CN(name),AUTH=MASTER は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CN(name),AUTH=MASTER**

    - 検証目的: 範囲整理の操作コマンドについて、V CN(name),AUTH=MASTER は、MVS オペレータコマンドの V CN で確認する項目です。コンソール権限をマスタ・コンソールに昇格させる動的変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020111の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、範囲整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),AUTH=MAを指定し、OSKB020111の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),AUTH=MA
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),AUTH=MA
    CASE OSKB020111
    SOURCE z/OS MVS Operations
    ```

    V CN(name),AUTH=MAとOSKB020111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020111を同じ出力で読み、範囲整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020111
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020111 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020111   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),AUTH=MA と OSKB020111 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V CN(name),LU=lu {#c22-i0282}
*分類: V CN*  ・  難易度: 中級

V CN(name),LU=luは、MVS オペレータコマンドのV CNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 復旧照合再の操作コマンドで V CN(name) 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V CN(name) 命令の出力を取らず復旧照合再の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて復旧照合再の根拠にする。 ✅
    - C. D A,L を省略して復旧照合再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧照合再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合再正解では選択記号 B を採用し、正解名は復旧照合再正解です。復旧照合再根拠では V CN(name) 命令 は「復旧照合再の操作コマンドに関係する定義値と表示行を照合する復旧照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧照合再根拠です。復旧照合再追跡では V CN(name) 命令の属性行と IEE115I を合わせ、追跡名は復旧照合再追跡です。誤答側の問題点を分けます。 A: 復旧照合再不足は名称や説明だけに寄り、判定名は復旧照合再不足です。 B: 復旧照合再正答は対象出力と項目説明を結び、根拠名は復旧照合再正答です。 C: 復旧照合再欠落は戻り値や記録番号に寄り、欠落名は復旧照合再欠落です。 D: 復旧照合再流用は別カテゴリの確認であり、排除名は復旧照合再流用です。復旧照合再初出では V CN(name) 命令を MVS オペレータコマンドの運用手順で確認し、初出名は復旧照合再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 変更確認の操作コマンドに関する V CN(name),LU=luの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず変更確認の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の操作コマンドの証跡として保存して根拠にする。
    - C. V CN(name),LU=luの変更点を出力本文から切り離して変更確認の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認の操作コマンドにおいて選択記号 D を採用し、識別名は変更確認です。変更確認の操作コマンドにおいて V CN(name),LU=lu は説明欄の「V CN(name),LU=luの状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の操作コマンドに関する記録は、V CN(name),LU=luの出力行と IEE115I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更確認ではありません。 B: 変更確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),LU=luの根拠にならないため変更確認ではありません。 C: 変更確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の操作コマンドで記録する V CN(name),LU=luはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CN(name),LU=lu**

    - 検証目的: 記録整理の操作コマンドについて、V CN(name),LU=luは、MVS オペレータコマンドの V CN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、記録整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),LU=luを指定し、OSKB020113の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CN(name),LU=lu
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CN(name),LU=lu
    CASE OSKB020113
    SOURCE z/OS MVS Operations
    ```

    V CN(name),LU=luとOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020113を同じ出力で読み、記録整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020113 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020113   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CN(name),LU=lu と OSKB020113 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V CONSOLE

### V CONSOLE,name,ALT=name2 {#c22-i0283}
*分類: V CONSOLE*  ・  難易度: 中級

V CONSOLE,name,ALT=name2は、コンソールの代替コンソール (障害時切替先) を動的に変更する

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 区切追跡再の操作コマンドで V CONSOLE 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V CONSOLE 命令の出力を取らず区切追跡再の操作コマンドの説明文と承認印だけを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて区切追跡再の根拠にする。 ✅
    - C. D A,L を省略して区切追跡再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を区切追跡再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡再正解では選択記号 B を採用し、正解名は区切追跡再正解です。区切追跡再根拠では V CONSOLE 命令 は「区切追跡再の操作コマンドに関係する定義値と表示行を照合する区切追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は区切追跡再根拠です。区切追跡再追跡では V CONSOLE 命令の属性行と IEE115I を合わせ、追跡名は区切追跡再追跡です。誤答側の問題点を分けます。 A: 区切追跡再不足は名称や説明だけに寄り、判定名は区切追跡再不足です。 B: 区切追跡再正答は対象出力と項目説明を結び、根拠名は区切追跡再正答です。 C: 区切追跡再欠落は戻り値や記録番号に寄り、欠落名は区切追跡再欠落です。 D: 区切追跡再流用は別カテゴリの確認であり、排除名は区切追跡再流用です。区切追跡再初出では V CONSOLE 命令を MVS オペレータコマンドの運用手順で確認し、初出名は区切追跡再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 優先照合の操作コマンドに関する V CONSOLE,name,ALT=name2の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず優先照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の操作コマンドの証跡として保存して根拠にする。
    - C. V CONSOLE,name,ALT=name2の変更点を出力本文から切り離して優先照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合の操作コマンドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合の操作コマンドにおいて V CONSOLE,name,ALT=name2 は説明欄の「V CONSOLE,name,ALT=name2の状態と出力メッセージを結び付ける優先照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の操作コマンドに関する記録は、V CONSOLE,name,ALT=name2の出力行と IEE115I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先照合ではありません。 B: 優先照合の操作コマンドは別カテゴリの確認を流用しており、V CONSOLE,name,ALT=name2の根拠にならないため優先照合ではありません。 C: 優先照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の操作コマンドで記録する V CONSOLE,name,ALT=name2はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V CONSOLE,name,ALT=name2**

    - 検証目的: 終端確認の操作コマンドについて、V CONSOLE,name,ALT=name2は、コンソールの代替コンソール (障害時切替先) を動的に変更するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030005の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、終端確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV CONSOLE,name,ALTを指定し、OSKB030005の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V CONSOLE,name,ALT
    CASE OSKB030005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V CONSOLE,name,ALT
    CASE OSKB030005
    SOURCE z/OS MVS Operations
    ```

    V CONSOLE,name,ALTとOSKB030005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030005を同じ出力で読み、終端確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030005
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030005 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030005   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V CONSOLE,name,ALT と OSKB030005 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V GRS

### V GRS(ALL),RESTART {#c22-i0284}
*分類: V GRS*  ・  難易度: 中級

V GRS(ALL),RESTARTは、MVS オペレータコマンドのV GRSで確認する項目です。Sysplex 全体の GRS を一括復帰させる。リング再構成のリカバリ手段

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 探索追跡再の操作コマンドで V GRS(ALL) 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V GRS(ALL) 命令の出力を取らず探索追跡再の操作コマンドの説明文と承認印だけを残す。
    - B. 参照資料名、表示行、メッセージをそろえて探索追跡再の根拠を固定する。 ✅
    - C. D OPDATA を省略して探索追跡再の操作コマンドの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を探索追跡再の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡再正解では選択記号 B を採用し、正解名は探索追跡再正解です。探索追跡再根拠では V GRS(ALL) 命令 は「探索追跡再の操作コマンドに関係する定義値と表示行を照合する探索追跡再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は探索追跡再根拠です。探索追跡再追跡では V GRS(ALL) 命令の属性行と IEE457I を合わせ、追跡名は探索追跡再追跡です。誤答側の問題点を分けます。 A: 探索追跡再不足は名称や説明だけに寄り、判定名は探索追跡再不足です。 B: 探索追跡再正答は対象出力と項目説明を結び、根拠名は探索追跡再正答です。 C: 探索追跡再欠落は戻り値や記録番号に寄り、欠落名は探索追跡再欠落です。 D: 探索追跡再流用は別カテゴリの確認であり、排除名は探索追跡再流用です。探索追跡再初出では V GRS(ALL) 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索追跡再初出です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 出力照合の操作コマンドに関する V GRS(ALL),RESTART の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OPDATA の結果を残さず出力照合の操作コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の操作コマンドの証跡として保存して根拠にする。
    - C. V GRS(ALL),RESTART の変更点を出力本文から切り離して出力照合の操作コマンドの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合の操作コマンドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合の操作コマンドにおいて V GRS(ALL),RESTART は説明欄の「V GRS(ALL),RESTART の状態と出力メッセージを結び付ける出力照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の操作コマンドに関する記録は、V GRS(ALL),RESTART の出力行と IEE457I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力照合ではありません。 B: 出力照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(ALL),RESTART の根拠にならないため出力照合ではありません。 C: 出力照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の操作コマンドで記録する V GRS(ALL),RESTART はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V GRS(ALL),RESTART**

    - 検証目的: 構文確認の操作コマンドについて、V GRS(ALL),RESTART は、MVS オペレータコマンドの V GRS で確認する項目です。Sysplex 全体の GRS を一括復帰させる。リング再構成のリカバリ手に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030001の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、構文確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(ALL),RESTARTを指定し、OSKB030001の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V GRS(ALL),RESTART
    CASE OSKB030001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V GRS(ALL),RESTART
    CASE OSKB030001
    SOURCE z/OS MVS Operations
    ```

    V GRS(ALL),RESTARTとOSKB030001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030001を同じ出力で読み、構文確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB030001
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB030001 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030001   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB030001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の V GRS(ALL),RESTART と OSKB030001 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB030001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V GRS(sysname),QUIESCE {#c22-i0285}
*分類: V GRS*  ・  難易度: 中級

V GRS(sysname),QUIESCEは、MVS オペレータコマンドのV GRSで確認する項目です。指定システムを GRS 複合体から切り離す前段階。ENQ 要求が拒否される状態に遷移

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 置換追跡再の操作コマンドに関する V GRS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず置換追跡再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換追跡再の操作コマンドの証跡として保存して根拠にする。
    - C. V GRS 属性の変更点を出力本文から切り離して置換追跡再の操作コマンドの承認欄だけ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換追跡再で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡再正解では選択記号 D を採用し、正解名は置換追跡再正解です。置換追跡再根拠では V GRS 属性 は「V GRS 属性の状態と出力メッセージを結び付ける置換追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は置換追跡再根拠です。置換追跡再保存では V GRS 属性の出力行と IEE115I を一緒に残し、保存名は置換追跡再保存です。選択肢ごとの違いを示します。 A: 置換追跡再欠落は戻り値や記録番号に寄り、欠落名は置換追跡再欠落です。 B: 置換追跡再流用は別カテゴリの確認であり、排除名は置換追跡再流用です。 C: 置換追跡再不足は名称や説明だけに寄り、判定名は置換追跡再不足です。 D: 置換追跡再正答は対象出力と項目説明を結び、根拠名は置換追跡再正答です。置換追跡再対象では V GRS 属性をz/OS MVS Operationsの確認記録に残し、対象名は置換追跡再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 探索照合の操作コマンドで V GRS(sysname),QUIESCE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V GRS(sysname),QUIESCE の出力を取らず探索照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 ✅
    - C. D A,L を省略して探索照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合の操作コマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の操作コマンドにおいて V GRS(sysname),QUIESCE は説明欄の「探索照合の操作コマンドに関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の操作コマンドの証跡を読む担当者は、V GRS(sysname),QUIESCE の属性行と IEE115I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索照合ではありません。 D: 探索照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(sysname),QUIESCE の根拠にならないため探索照合ではありません。探索照合の操作コマンドに出る V GRS(sysname),QUIESCE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V GRS(sysname),QUIESCE**

    - 検証目的: 監査整理の操作コマンドについて、V GRS(sysname),QUIESCE は、MVS オペレータコマンドの V GRS で確認する項目です。指定システムを GRS 複合体から切り離す前段階。ENQ 要求が拒に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、監査整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(sysname),QUIを指定し、OSKB020119の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V GRS(sysname),QUI
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V GRS(sysname),QUI
    CASE OSKB020119
    SOURCE z/OS MVS Operations
    ```

    V GRS(sysname),QUIとOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020119を同じ出力で読み、監査整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB020119 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020119   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V GRS(sysname),QUI と OSKB020119 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB020119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V GRS(sysname),RESTART {#c22-i0286}
*分類: V GRS*  ・  難易度: 中級

V GRS(sysname),RESTARTは、MVS オペレータコマンドのV GRSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 終端追跡再の操作コマンドに関係する V GRS 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、終端追跡再の確認値として扱う。 ✅
    - B. V GRS 属性の名称と担当者名だけを残して終端追跡再の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で終端追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE457I の有無を見ず終端追跡再の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡再正解では選択記号 A を採用し、正解名は終端追跡再正解です。終端追跡再根拠では V GRS 属性 は「V GRS 属性の用途を操作コマンドの表示で確認する終端追跡再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は終端追跡再根拠です。終端追跡再背景ではz/OS MVS Operationsの V GRS 属性と IEE457I を同じ証跡に残し、背景名は終端追跡再背景です。他の選択肢を確認します。 A: 終端追跡再正答は対象出力と項目説明を結び、根拠名は終端追跡再正答です。 B: 終端追跡再不足は名称や説明だけに寄り、判定名は終端追跡再不足です。 C: 終端追跡再流用は別カテゴリの確認であり、排除名は終端追跡再流用です。 D: 終端追跡再欠落は戻り値や記録番号に寄り、欠落名は終端追跡再欠落です。終端追跡再用語では V GRS 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端追跡再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 上書照合の操作コマンドで操作コマンドの運用確認を行います。V GRS(sysname),RESTART の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で上書照合の操作コマンドを確認した扱いにする。
    - B. IEE457I の有無を確認せず上書照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書照合の記録として扱う。 ✅
    - D. V GRS(sysname),RESTART の属性行を読まず上書照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合の操作コマンドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合の操作コマンドにおいて V GRS(sysname),RESTART は説明欄の「z/OS MVS Operationsで V GRS(sysname),RESTART の扱いを記録する上書照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の操作コマンドを受け取る担当者は、V GRS(sysname),RESTART の表示結果と IEE457I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(sysname),RESTART の根拠にならないため上書照合ではありません。 B: 上書照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため上書照合ではありません。 C: 上書照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の操作コマンドが示す V GRS(sysname),RESTART は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V GRS(sysname),RESTART**

    - 検証目的: 変更整理の操作コマンドについて、V GRS(sysname),RESTART は、MVS オペレータコマンドの V GRS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OPDATA を入力し、変更整理の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OPDATA
    ```

    COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(sysname),RESを指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V GRS(sysname),RES
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V GRS(sysname),RES
    CASE OSKB020120
    SOURCE z/OS MVS Operations
    ```

    V GRS(sysname),RESとOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020120を同じ出力で読み、変更整理の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OPDATA
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE457I OSKB020120 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB020120   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE457IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OPDATA が画面・出力に表示されること
    ② ステップ2 の V GRS(sysname),RES と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の IEE457I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands




## MVS オペレータコマンド > V PATH

### V PATH(devnum,chp),OFFLINE {#c22-i0287}
*分類: V PATH*  ・  難易度: 中級

V PATH(devnum,chp),OFFLINEは、MVS オペレータコマンドのV PATHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 条件追跡再の操作コマンドに関係する V PATH 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、条件追跡再の確認記録にまとめる。 ✅
    - B. V PATH 属性の名称と担当者名だけを残して条件追跡再の操作コマンドの表示本文を対象から外す。
    - C. 操作コマンド以外の画面で条件追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。
    - D. IEE115I の有無を見ず条件追跡再の操作コマンドの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡再正解では選択記号 A を採用し、正解名は条件追跡再正解です。条件追跡再根拠では V PATH 属性 は「V PATH 属性の用途を操作コマンドの表示で確認する条件追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は条件追跡再根拠です。条件追跡再背景ではz/OS MVS Operationsの V PATH 属性と IEE115I を同じ証跡に残し、背景名は条件追跡再背景です。他の選択肢を確認します。 A: 条件追跡再正答は対象出力と項目説明を結び、根拠名は条件追跡再正答です。 B: 条件追跡再不足は名称や説明だけに寄り、判定名は条件追跡再不足です。 C: 条件追跡再流用は別カテゴリの確認であり、排除名は条件追跡再流用です。 D: 条件追跡再欠落は戻り値や記録番号に寄り、欠落名は条件追跡再欠落です。条件追跡再用語では V PATH 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件追跡再用語です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 範囲照合の操作コマンドで操作コマンドの運用確認を行います。V PATH(devnum,chp),OFFLI の根拠にできる作業はどれですか。

    - A. z/OS MVS Operationsと無関係な一覧で範囲照合の操作コマンドを確認した扱いにする。
    - B. IEE115I の有無を確認せず範囲照合の操作コマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. V PATH(devnum,chp),OFFLI の属性行を読まず範囲照合の操作コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合の操作コマンドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合の操作コマンドにおいて V PATH(devnum,chp),OFFLI は説明欄の「z/OS MVS Operationsで V PATH(devnum,chp),OFFLI の扱いを記録する範囲照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の操作コマンドを受け取る担当者は、V PATH(devnum,chp),OFFLI の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の操作コマンドは別カテゴリの確認を流用しており、V PATH(devnum,chp),OFFLI の根拠にならないため範囲照合ではありません。 B: 範囲照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の操作コマンドが示す V PATH(devnum,chp),OFFLI は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V PATH(devnum,chp),OFFLINE**

    - 検証目的: 置換確認の操作コマンドについて、V PATH(devnum,chp),OFFLINE は、MVS オペレータコマンドの V PATH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示さに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、置換確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV PATH(devnum,chp)を指定し、OSKB030004の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V PATH(devnum,chp)
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V PATH(devnum,chp)
    CASE OSKB030004
    SOURCE z/OS MVS Operations
    ```

    V PATH(devnum,chp)とOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030004を同じ出力で読み、置換確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030004
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030004 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030004   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V PATH(devnum,chp) と OSKB030004 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands



### V PATH(devnum,chp),ONLINE {#c22-i0288}
*分類: V PATH*  ・  難易度: 中級

V PATH(devnum,chp),ONLINEは、MVS オペレータコマンドのV PATHで確認する項目です。指定装置の特定チャネル・パス (CHPID) をオンライン化する。装置レベルではなく経路レベルの制御

**出典:** z / OS MVS System Commands

??? question "確認問題（2問）"
    **問題.** 出力追跡再の操作コマンドに関する V PATH 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D A,L の結果を残さず出力追跡再の操作コマンドの担当者名と日時だけを記録する。
    - B. 別製品のメッセージを出力追跡再の操作コマンドの証跡として保存して根拠にする。
    - C. V PATH 属性の変更点を出力本文から切り離して出力追跡再の操作コマンドの承認欄だけ残す。
    - D. D A,L の結果から対象行を抜き出し、出力追跡再の証跡として残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡再正解では選択記号 D を採用し、正解名は出力追跡再正解です。出力追跡再根拠では V PATH 属性 は「V PATH 属性の状態と出力メッセージを結び付ける出力追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力追跡再根拠です。出力追跡再保存では V PATH 属性の出力行と IEE115I を一緒に残し、保存名は出力追跡再保存です。選択肢ごとの違いを示します。 A: 出力追跡再欠落は戻り値や記録番号に寄り、欠落名は出力追跡再欠落です。 B: 出力追跡再流用は別カテゴリの確認であり、排除名は出力追跡再流用です。 C: 出力追跡再不足は名称や説明だけに寄り、判定名は出力追跡再不足です。 D: 出力追跡再正答は対象出力と項目説明を結び、根拠名は出力追跡再正答です。出力追跡再対象では V PATH 属性をz/OS MVS Operationsの確認記録に残し、対象名は出力追跡再対象です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200

    ---

    **問題.** 区切照合の操作コマンドで V PATH(devnum,chp),ONLIN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. V PATH(devnum,chp),ONLIN の出力を取らず区切照合の操作コマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. D A,L を省略して区切照合の操作コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の操作コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合の操作コマンドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合の操作コマンドにおいて V PATH(devnum,chp),ONLIN は説明欄の「区切照合の操作コマンドに関係する定義値と表示行を照合する区切照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の操作コマンドの証跡を読む担当者は、V PATH(devnum,chp),ONLIN の属性行と IEE115I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切照合ではありません。 D: 区切照合の操作コマンドは別カテゴリの確認を流用しており、V PATH(devnum,chp),ONLIN の根拠にならないため区切照合ではありません。区切照合の操作コマンドに出る V PATH(devnum,chp),ONLIN は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200


??? note "検証手順（1件）"
    **V PATH(devnum,chp),ONLINE**

    - 検証目的: 呼出確認の操作コマンドについて、V PATH(devnum,chp),ONLINE は、MVS オペレータコマンドの V PATH で確認する項目です。指定装置の特定チャネル・パス (CHPID) をオンラインに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D A,L を入力し、呼出確認の操作コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D A,L
    ```

    COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にV PATH(devnum,chp)を指定し、OSKB030003の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND V PATH(devnum,chp)
    CASE OSKB030003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM V PATH(devnum,chp)
    CASE OSKB030003
    SOURCE z/OS MVS Operations
    ```

    V PATH(devnum,chp)とOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030003を同じ出力で読み、呼出確認の操作コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D A,L
    CASE OSKB030003
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE115I OSKB030003 DISPLAY ACTIVITY
    JOBNAME  STEPNAME PROCSTEP ASID  STATUS
    OSKB030003   STEP1            003C  ACTIVE
    IEE457I 00.00.00 UNIT STATUS DISPLAY
    ```

    IEE115IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D A,L が画面・出力に表示されること
    ② ステップ2 の V PATH(devnum,chp) と OSKB030003 が画面・出力に表示されること
    ③ ステップ3 の IEE115I と OSKB030003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands


