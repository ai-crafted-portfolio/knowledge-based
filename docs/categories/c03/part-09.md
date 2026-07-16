---
search:
  exclude: true
---

# Assembler / システム・プログラミング — 詳細 (9/10)

[← Assembler / システム・プログラミング の概要へ戻る](index.md)


## Assembler / システム・プログラミング > 命令: 10進

### ED addr1(l1),addr2 {#c03-i0484}
*分類: 命令: 10進*  ・  難易度: 上級

ED addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Edit。10 進結果をパターン文字列で書式化 (帳票編集) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（2問）"
    **問題.** 比較照合の命令: 進で ED addr1(l1) 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ED addr1(l1) 命令の出力を取らず比較照合の命令: 進の説明文と承認印だけを残す。
    - B. 対象の出力行とメッセージ接頭辞を同時に記録し、比較照合で再確認できる形にする。 ✅
    - C. ST OSKBASM を省略して比較照合の命令: 進の記録番号と時刻だけを残す。
    - D. 隣接項目の結果を比較照合の命令: 進へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では ED addr1(l1) 命令 は「比較照合の命令: 進に関係する定義値と表示行を照合する比較照合項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では ED addr1(l1) 命令の属性行と ASMA90I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明だけに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では ED addr1(l1) 命令を Assembler / システム・プログラミングの運用手順で確認し、初出名は比較照合初出です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400

    ---

    **問題.** 構文照合の命令: 進に関係する ED addr1(l1) 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文照合の確認値として扱う。 ✅
    - B. ED addr1(l1) 命令の名称と担当者名のみを残して構文照合の命令: 進の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で構文照合の命令: 進を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず構文照合の命令: 進の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合の命令: 進において選択記号 A を採用し、識別名は構文照合です。構文照合の命令: 進において ED addr1(l1) 命令 は説明欄の「ED addr1(l1) 命令の用途をアセンブラーの表示で確認する構文照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の命令: 進に関連して、HLASM and z/OS System Programmingでは ED addr1(l1) 命令の表示属性と ASMA90I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の命令: 進は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の命令: 進は別カテゴリの確認を流用しており、ED addr1(l1) 命令の根拠にならないため構文照合ではありません。 D: 構文照合の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため構文照合ではありません。構文照合の命令: 進で使う ED addr1(l1) 命令という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **ED addr1(l1),addr2**

    - 検証目的: 置換判定の命令: 進について、ED addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Edit。10 進結果をパターン文字列で書式化に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、置換判定の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にED addr1(l1),addr2を指定し、OSKB010084の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ED addr1(l1),addr2
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ED addr1(l1),addr2
    CASE OSKB010084
    SOURCE HLASM and z/OS System Programming
    ```

    ED addr1(l1),addr2とOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010084を同じ出力で読み、置換判定の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010084
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010084
    ASMA90I ED addr1(l1),addr2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の ED addr1(l1),addr2 と OSKB010084 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### EDMK addr1(l1),addr2 {#c03-i0485}
*分類: 命令: 10進*  ・  難易度: 上級

EDMK addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Edit and Mark。ED + 通貨記号位置を R1 に保存 (フローティング記号) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 展開照合の命令: 進で EDMK addr1 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. EDMK addr1 属性の出力を取らず展開照合の命令: 進の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開照合の根拠を固定する。 ✅
    - C. ST OSKBASM を省略して展開照合の命令: 進の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の命令: 進へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合の命令: 進において選択記号 B を採用し、識別名は展開照合です。展開照合の命令: 進において EDMK addr1 属性 は説明欄の「展開照合の命令: 進に関係する定義値と表示行を照合する展開照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の命令: 進の証跡を読む担当者は、EDMK addr1 属性の属性行と ASMA90I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の命令: 進は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため展開照合ではありません。 D: 展開照合の命令: 進は別カテゴリの確認を流用しており、EDMK addr1 属性の根拠にならないため展開照合ではありません。展開照合の命令: 進に出る EDMK addr1 属性は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **EDMK addr1(l1),addr2**

    - 検証目的: 終端判定の命令: 進について、EDMK addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Edit and Mark。ED + 通貨記に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、終端判定の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEDMK addr1(l1),addを指定し、OSKB010085の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EDMK addr1(l1),add
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EDMK addr1(l1),add
    CASE OSKB010085
    SOURCE HLASM and z/OS System Programming
    ```

    EDMK addr1(l1),addとOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010085を同じ出力で読み、終端判定の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010085
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010085
    ASMA90I EDMK addr1(l1),addr2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の EDMK addr1(l1),add と OSKB010085 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### MP addr1(l1),addr2(l2) {#c03-i0486}
*分類: 命令: 10進*  ・  難易度: 上級

MP addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で機能名、見出し、または確認対象として参照する項目です。Multiply Packed。L2≤8, L2<L1 制約 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 値域確認の命令: 進に関する MP addr1 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず値域確認の命令: 進の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の命令: 進の証跡として保存して根拠にする。
    - C. MP addr1 属性の変更点を出力本文から切り離して値域確認の命令: 進の承認欄のみ残す。
    - D. ST OSKBASM で得た表示本文を使い、値域確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認の命令: 進において選択記号 D を採用し、識別名は値域確認です。値域確認の命令: 進において MP addr1 属性 は説明欄の「MP addr1 属性の状態と出力メッセージを結び付ける値域確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の命令: 進に関する記録は、MP addr1 属性の出力行と ASMA90I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため値域確認ではありません。 B: 値域確認の命令: 進は別カテゴリの確認を流用しており、MP addr1 属性の根拠にならないため値域確認ではありません。 C: 値域確認の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の命令: 進は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の命令: 進で記録する MP addr1 属性は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **MP addr1(l1),addr2(l2)**

    - 検証目的: 監査検査の命令: 進について、MP addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で機能名、見出し、または確認対象として参照する項目です。Muに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、監査検査の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にMP addr1(l1),addr2を指定し、OSKB010079の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND MP addr1(l1),addr2
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM MP addr1(l1),addr2
    CASE OSKB010079
    SOURCE HLASM and z/OS System Programming
    ```

    MP addr1(l1),addr2とOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010079を同じ出力で読み、監査検査の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010079
    ASMA90I MP addr1(l1),addr2(l2) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の MP addr1(l1),addr2 と OSKB010079 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### PACK addr1(l1),addr2(l2) {#c03-i0487}
*分類: 命令: 10進*  ・  難易度: 上級

PACK addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。EBCDIC ゾーン形式 から パック形式に変換 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 区切確認の命令: 進で PACK addr1 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PACK addr1 属性の出力を取らず区切確認の命令: 進の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて区切確認の根拠を固定する。 ✅
    - C. ST OSKBASM を省略して区切確認の命令: 進の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の命令: 進へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認の命令: 進において選択記号 B を採用し、識別名は区切確認です。区切確認の命令: 進において PACK addr1 属性 は説明欄の「区切確認の命令: 進に関係する定義値と表示行を照合する区切確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の命令: 進の証跡を読む担当者は、PACK addr1 属性の属性行と ASMA90I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の命令: 進は対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため区切確認ではありません。 D: 区切確認の命令: 進は別カテゴリの確認を流用しており、PACK addr1 属性の根拠にならないため区切確認ではありません。区切確認の命令: 進に出る PACK addr1 属性は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **PACK addr1(l1),addr2(l2)**

    - 検証目的: 記録検査の命令: 進について、PACK addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。EBCDIC ゾーン形式 から パッに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010073の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、記録検査の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にPACK addr1(l1),addを指定し、OSKB010073の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND PACK addr1(l1),add
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM PACK addr1(l1),add
    CASE OSKB010073
    SOURCE HLASM and z/OS System Programming
    ```

    PACK addr1(l1),addとOSKB010073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010073を同じ出力で読み、記録検査の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010073
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010073
    ASMA90I PACK addr1(l1),addr2(l2) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の PACK addr1(l1),add と OSKB010073 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### SP addr1(l1),addr2(l2) {#c03-i0488}
*分類: 命令: 10進*  ・  難易度: 上級

SP addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で機能名、見出し、または確認対象として参照する項目です。SP addr1(l1),addr2(l2)は、Subtract Packed (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 順序確認の命令: 進でアセンブラーの運用確認を行います。SP addr1 属性の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で順序確認の命令: 進を確認した扱いにする。
    - B. ASMA90I の有無を確認せず順序確認の命令: 進を正常終了として記録する。
    - C. 同じ画面で対象行と ASMA90I を読み、順序確認の結果として保存する。 ✅
    - D. SP addr1 属性の属性行を読まず順序確認の命令: 進の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認の命令: 進において選択記号 C を採用し、識別名は順序確認です。順序確認の命令: 進において SP addr1 属性 は説明欄の「HLASM and z/OS System Programmingで SP addr1 属性の扱いを記録する順序確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の命令: 進を受け取る担当者は、SP addr1 属性の表示結果と ASMA90I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の命令: 進は別カテゴリの確認を流用しており、SP addr1 属性の根拠にならないため順序確認ではありません。 B: 順序確認の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため順序確認ではありません。 C: 順序確認の命令: 進は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の命令: 進が示す SP addr1 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **SP addr1(l1),addr2(l2)**

    - 検証目的: 復旧検査の命令: 進について、SP addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で機能名、見出し、または確認対象として参照する項目です。SPに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、復旧検査の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSP addr1(l1),addr2を指定し、OSKB010078の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SP addr1(l1),addr2
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SP addr1(l1),addr2
    CASE OSKB010078
    SOURCE HLASM and z/OS System Programming
    ```

    SP addr1(l1),addr2とOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010078を同じ出力で読み、復旧検査の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010078
    ASMA90I SP addr1(l1),addr2(l2) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の SP addr1(l1),addr2 と OSKB010078 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### SRP addr1(l1),shift,round {#c03-i0489}
*分類: 命令: 10進*  ・  難易度: 上級

SRP addr1(l1),shift,roundは、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Shift And Round Packed。10進シフト+四捨五入 (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 変更確認の命令: 進に関する SRP addr1 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず変更確認の命令: 進の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の命令: 進の証跡として保存して根拠にする。
    - C. SRP addr1 属性の変更点を出力本文から切り離して変更確認の命令: 進の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認の命令: 進において選択記号 D を採用し、識別名は変更確認です。変更確認の命令: 進において SRP addr1 属性 は説明欄の「SRP addr1 属性の状態と出力メッセージを結び付ける変更確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の命令: 進に関する記録は、SRP addr1 属性の出力行と ASMA90I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため変更確認ではありません。 B: 変更確認の命令: 進は別カテゴリの確認を流用しており、SRP addr1 属性の根拠にならないため変更確認ではありません。 C: 変更確認の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の命令: 進は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の命令: 進で記録する SRP addr1 属性は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **SRP addr1(l1),shift,round**

    - 検証目的: 呼出判定の命令: 進について、SRP addr1(l1),shift,roundは、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Shift And Round Pに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、呼出判定の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSRP addr1(l1),shifを指定し、OSKB010083の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND SRP addr1(l1),shif
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM SRP addr1(l1),shif
    CASE OSKB010083
    SOURCE HLASM and z/OS System Programming
    ```

    SRP addr1(l1),shifとOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010083を同じ出力で読み、呼出判定の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010083
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010083
    ASMA90I SRP addr1(l1),shift,roun ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の SRP addr1(l1),shif と OSKB010083 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_cbcpx01]



### UNPK addr1(l1),addr2(l2) {#c03-i0490}
*分類: 命令: 10進*  ・  難易度: 上級

UNPK addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。パック形式 から EBCDIC ゾーン形式に展開 (符号ニブル左移動) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 範囲確認の命令: 進でアセンブラーの運用確認を行います。UNPK addr1 属性の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で範囲確認の命令: 進を確認した扱いにする。
    - B. ASMA90I の有無を確認せず範囲確認の命令: 進を正常終了として記録する。
    - C. ASMA90I を含む表示を保存し、説明欄との差分を範囲確認で確認する。 ✅
    - D. UNPK addr1 属性の属性行を読まず範囲確認の命令: 進の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認の命令: 進において選択記号 C を採用し、識別名は範囲確認です。範囲確認の命令: 進において UNPK addr1 属性 は説明欄の「HLASM and z/OS System Programmingで UNPK addr1 属性の扱いを記録する範囲確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認の命令: 進を受け取る担当者は、UNPK addr1 属性の表示結果と ASMA90I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認の命令: 進は別カテゴリの確認を流用しており、UNPK addr1 属性の根拠にならないため範囲確認ではありません。 B: 範囲確認の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認の命令: 進は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認の命令: 進が示す UNPK addr1 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **UNPK addr1(l1),addr2(l2)**

    - 検証目的: 比較検査の命令: 進について、UNPK addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。パック形式 から EBCDIC ゾーに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010074の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、比較検査の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にUNPK addr1(l1),addを指定し、OSKB010074の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND UNPK addr1(l1),add
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM UNPK addr1(l1),add
    CASE OSKB010074
    SOURCE HLASM and z/OS System Programming
    ```

    UNPK addr1(l1),addとOSKB010074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010074を同じ出力で読み、比較検査の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010074
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010074
    ASMA90I UNPK addr1(l1),addr2(l2) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の UNPK addr1(l1),add と OSKB010074 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### ZAP addr1(l1),addr2(l2) {#c03-i0491}
*分類: 命令: 10進*  ・  難易度: 上級

ZAP addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Zero And Add Packed。0 クリア後の代入。10進=10進コピー (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（2問）"
    **問題.** 呼出確認の命令: 進でアセンブラーの運用確認を行います。ZAP addr1 属性の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で呼出確認の命令: 進を確認した扱いにする。
    - B. ASMA90I の有無を確認せず呼出確認の命令: 進を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出確認の確認記録にまとめる。 ✅
    - D. ZAP addr1 属性の属性行を読まず呼出確認の命令: 進の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では ZAP addr1 属性 は「HLASM and z/OS System Programmingで ZAP addr1 属性の扱いを記録する呼出確認項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では ZAP addr1 属性の表示結果と ASMA90I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明だけに寄り、判定名は呼出確認不足です。呼出確認資料では ZAP addr1 属性の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400

    ---

    **問題.** 復旧確認の命令: 進で ZAP addr1 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ZAP addr1 属性の出力を取らず復旧確認の命令: 進の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧確認の確認にする。 ✅
    - C. ST OSKBASM を省略して復旧確認の命令: 進の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の命令: 進へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認の命令: 進において選択記号 B を採用し、識別名は復旧確認です。復旧確認の命令: 進において ZAP addr1 属性 は説明欄の「復旧確認の命令: 進に関係する定義値と表示行を照合する復旧確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の命令: 進の証跡を読む担当者は、ZAP addr1 属性の属性行と ASMA90I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の命令: 進は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の命令: 進は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の命令: 進は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の命令: 進は別カテゴリの確認を流用しており、ZAP addr1 属性の根拠にならないため復旧確認ではありません。復旧確認の命令: 進に出る ZAP addr1 属性は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **ZAP addr1(l1),addr2(l2)**

    - 検証目的: 構文判定の命令: 進について、ZAP addr1(l1),addr2(l2)は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Zero And Add Packedに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、構文判定の命令: 進の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にZAP addr1(l1),addrを指定し、OSKB010081の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ZAP addr1(l1),addr
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ZAP addr1(l1),addr
    CASE OSKB010081
    SOURCE HLASM and z/OS System Programming
    ```

    ZAP addr1(l1),addrとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010081を同じ出力で読み、構文判定の命令: 進の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010081
    ASMA90I ZAP addr1(l1),addr2(l2) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の ZAP addr1(l1),addr と OSKB010081 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### 編集パターン文字 X'20' {#c03-i0492}
*分類: 命令: 10進*  ・  難易度: 上級

編集パターン文字 X'20'は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Digit Selector。1 桁取り出す指示子 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（2問）"
    **問題.** 終端検査の編集パターン文字に関係する編集パターン文字 X'20'の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 同じ画面で対象行と ASMA90I を読み、終端検査の結果として保存する。 ✅
    - B. 編集パターン文字 X'20'の名称と担当者名だけを残して終端検査の編集パターン文字の表示本文を対象から外す。
    - C. アセンブラー以外の画面で終端検査の編集パターン文字を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず終端検査の編集パターン文字の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では編集パターン文字 X'20' は「編集パターン文字 X'20'の用途をアセンブラーの表示で確認する終端検査項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では HLASM and z/OS System Programmingの編集パターン文字 X'20'と ASMA90I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明だけに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では編集パターン文字 X'20'を Assembler / システム・プログラミングで扱う確認対象とし、用語名は終端検査用語です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400

    ---

    **問題.** 置換照合の編集パターン文字に関する編集パターン文字 X'20'の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず置換照合の編集パターン文字の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の編集パターン文字の証跡として保存して根拠にする。
    - C. 編集パターン文字 X'20'の変更点を出力本文から切り離して置換照合の編集パターン文字の承認欄のみ残す。
    - D. ST OSKBASM の結果から対象行を抜き出し、置換照合の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合の編集パターン文字において選択記号 D を採用し、識別名は置換照合です。置換照合の編集パターン文字において編集パターン文字 X'20' は説明欄の「編集パターン文字 X'20'の状態と出力メッセージを結び付ける置換照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の編集パターン文字に関する記録は、編集パターン文字 X'20'の出力行と ASMA90I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の編集パターン文字は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため置換照合ではありません。 B: 置換照合の編集パターン文字は別カテゴリの確認を流用しており、編集パターン文字 X'20'の根拠にならないため置換照合ではありません。 C: 置換照合の編集パターン文字は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の編集パターン文字は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の編集パターン文字で記録する編集パターン文字 X'20'は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **編集パターン文字 X'20'**

    - 検証目的: 上書判定の編集パターン文字について、編集パターン文字 X'20'は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Digit Selector。1 桁取り出す指示子 (メに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、上書判定の編集パターン文字の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に編集パターン文字 X'20'を指定し、OSKB010087の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 編集パターン文字 X'20'
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 編集パターン文字 X'20'
    CASE OSKB010087
    SOURCE HLASM and z/OS System Programming
    ```

    編集パターン文字 X'20'とOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010087を同じ出力で読み、上書判定の編集パターン文字の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010087
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010087
    ASMA90I 編集パターン文字 X'20' ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の 編集パターン文字 X'20' と OSKB010087 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### 編集パターン文字 X'21' {#c03-i0493}
*分類: 命令: 10進*  ・  難易度: 上級

編集パターン文字 X'21'は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Significance Starter。最初の有効桁マーカ (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 終端照合の編集パターン文字に関係する編集パターン文字 X'21'の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端照合の確認記録にまとめる。 ✅
    - B. 編集パターン文字 X'21'の名称と担当者名のみを残して終端照合の編集パターン文字の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で終端照合の編集パターン文字を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず終端照合の編集パターン文字の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合の編集パターン文字において選択記号 A を採用し、識別名は終端照合です。終端照合の編集パターン文字において編集パターン文字 X'21' は説明欄の「編集パターン文字 X'21'の用途をアセンブラーの表示で確認する終端照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の編集パターン文字に関連して、HLASM and z/OS System Programmingでは編集パターン文字 X'21'の表示属性と ASMA90I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の編集パターン文字は対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の編集パターン文字は名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の編集パターン文字は別カテゴリの確認を流用しており、編集パターン文字 X'21'の根拠にならないため終端照合ではありません。 D: 終端照合の編集パターン文字は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため終端照合ではありません。終端照合の編集パターン文字で使う編集パターン文字 X'21'という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **編集パターン文字 X'21'**

    - 検証目的: 出力判定の編集パターン文字について、編集パターン文字 X'21'は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。Significance Starter。最初の有効桁マに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010088の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、出力判定の編集パターン文字の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に編集パターン文字 X'21'を指定し、OSKB010088の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 編集パターン文字 X'21'
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 編集パターン文字 X'21'
    CASE OSKB010088
    SOURCE HLASM and z/OS System Programming
    ```

    編集パターン文字 X'21'とOSKB010088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010088を同じ出力で読み、出力判定の編集パターン文字の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010088
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010088
    ASMA90I 編集パターン文字 X'21' ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の 編集パターン文字 X'21' と OSKB010088 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]



### 編集パターン文字 X'22' {#c03-i0494}
*分類: 命令: 10進*  ・  難易度: 上級

編集パターン文字 X'22'は、Assembler / システム・プログラミングの命令: 10進で機能名、見出し、または確認対象として参照する項目です。Field Separator。連続フィールド区切り (メインフレーム実践 (神居俊哉) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 探索照合の編集パターン文字で編集パターン文字 X'22'の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 編集パターン文字 X'22'の出力を取らず探索照合の編集パターン文字の説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索照合の根拠にする。 ✅
    - C. ST OSKBASM を省略して探索照合の編集パターン文字の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の編集パターン文字へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合の編集パターン文字において選択記号 B を採用し、識別名は探索照合です。探索照合の編集パターン文字において編集パターン文字 X'22' は説明欄の「探索照合の編集パターン文字に関係する定義値と表示行を照合する探索照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の編集パターン文字の証跡を読む担当者は、編集パターン文字 X'22'の属性行と ASMA90I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の編集パターン文字は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の編集パターン文字は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の編集パターン文字は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため探索照合ではありません。 D: 探索照合の編集パターン文字は別カテゴリの確認を流用しており、編集パターン文字 X'22'の根拠にならないため探索照合ではありません。探索照合の編集パターン文字に出る編集パターン文字 X'22'は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **編集パターン文字 X'22'**

    - 検証目的: 条件判定の編集パターン文字について、編集パターン文字 X'22'は、Assembler / システム・プログラミングの命令: 10進で機能名、見出し、または確認対象として参照する項目です。Field Sepaに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010089の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、条件判定の編集パターン文字の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に編集パターン文字 X'22'を指定し、OSKB010089の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 編集パターン文字 X'22'
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 編集パターン文字 X'22'
    CASE OSKB010089
    SOURCE HLASM and z/OS System Programming
    ```

    編集パターン文字 X'22'とOSKB010089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010089を同じ出力で読み、条件判定の編集パターン文字の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010089
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010089
    ASMA90I 編集パターン文字 X'22' ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の 編集パターン文字 X'22' と OSKB010089 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉) [zOS31_cbcpx01]



### 編集パターン文字 X'40' {#c03-i0495}
*分類: 命令: 10進*  ・  難易度: 上級

編集パターン文字 X'40'は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。ブランク (10 進数字に置換される位置) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]

??? question "確認問題（1問）"
    **問題.** 呼出照合の編集パターン文字でアセンブラーの運用確認を行います。編集パターン文字 X'40'の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で呼出照合の編集パターン文字を確認した扱いにする。
    - B. ASMA90I の有無を確認せず呼出照合の編集パターン文字を正常終了として記録する。
    - C. ASMA90I を含む表示を保存し、説明欄との差分を呼出照合で確認する。 ✅
    - D. 編集パターン文字 X'40'の属性行を読まず呼出照合の編集パターン文字の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合の編集パターン文字において選択記号 C を採用し、識別名は呼出照合です。呼出照合の編集パターン文字において編集パターン文字 X'40' は説明欄の「HLASM and z/OS System Programmingで編集パターン文字 X'40'の扱いを記録する呼出照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の編集パターン文字を受け取る担当者は、編集パターン文字 X'40'の表示結果と ASMA90I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の編集パターン文字は別カテゴリの確認を流用しており、編集パターン文字 X'40'の根拠にならないため呼出照合ではありません。 B: 呼出照合の編集パターン文字は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の編集パターン文字は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の編集パターン文字は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の編集パターン文字が示す編集パターン文字 X'40'は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **編集パターン文字 X'40'**

    - 検証目的: 探索判定の編集パターン文字について、編集パターン文字 X'40'は、Assembler / システム・プログラミングの命令: 10進で確認する項目です。ブランク (10 進数字に置換される位置) (メインフレに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010086の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、探索判定の編集パターン文字の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄に編集パターン文字 X'40'を指定し、OSKB010086の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND 編集パターン文字 X'40'
    CASE OSKB010086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM 編集パターン文字 X'40'
    CASE OSKB010086
    SOURCE HLASM and z/OS System Programming
    ```

    編集パターン文字 X'40'とOSKB010086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010086を同じ出力で読み、探索判定の編集パターン文字の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010086
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010086
    ASMA90I 編集パターン文字 X'40' ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の 編集パターン文字 X'40' と OSKB010086 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpx01]




## Assembler / システム・プログラミング > 命令: テスト

### CLC addr1(len),addr2 {#c03-i0496}
*分類: 命令: テスト*  ・  難易度: 上級

CLC addr1(len),addr2は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（1問）"
    **問題.** 呼出確認の命令: テストでアセンブラーの運用確認を行います。CLC addr1 属性の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で呼出確認の命令: テストを確認した扱いにする。
    - B. ASMA90I の有無を確認せず呼出確認の命令: テストを正常終了として記録する。
    - C. 同じ画面で対象行と ASMA90I を読み、呼出確認の結果として保存する。 ✅
    - D. CLC addr1 属性の属性行を読まず呼出確認の命令: テストの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認の命令: テストにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認の命令: テストにおいて CLC addr1 属性 は説明欄の「HLASM and z/OS System Programmingで CLC addr1 属性の扱いを記録する呼出確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の命令: テストを受け取る担当者は、CLC addr1 属性の表示結果と ASMA90I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の命令: テストは別カテゴリの確認を流用しており、CLC addr1 属性の根拠にならないため呼出確認ではありません。 B: 呼出確認の命令: テストは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の命令: テストは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の命令: テストは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の命令: テストが示す CLC addr1 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（1件）"
    **CLC addr1(len),addr2**

    - 検証目的: 探索検査の命令: テストについて、CLC addr1(len),addr2は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、探索検査の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCLC addr1(len),addを指定し、OSKB010066の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CLC addr1(len),add
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CLC addr1(len),add
    CASE OSKB010066
    SOURCE HLASM and z/OS System Programming
    ```

    CLC addr1(len),addとOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010066を同じ出力で読み、探索検査の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010066
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010066
    ASMA90I CLC addr1(len),addr2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の CLC addr1(len),add と OSKB010066 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### CLI addr,imm {#c03-i0497}
*分類: 命令: テスト*  ・  難易度: 上級

CLI addr,immは、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（1問）"
    **問題.** 展開確認の命令: テストで CLI addr,immの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. CLI addr,immの出力を取らず展開確認の命令: テストの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて展開確認の根拠にする。 ✅
    - C. ST OSKBASM を省略して展開確認の命令: テストの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の命令: テストへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認の命令: テストにおいて選択記号 B を採用し、識別名は展開確認です。展開確認の命令: テストにおいて CLI addr,imm は説明欄の「展開確認の命令: テストに関係する定義値と表示行を照合する展開確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の命令: テストの証跡を読む担当者は、CLI addr,immの属性行と ASMA90I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の命令: テストは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の命令: テストは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の命令: テストは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため展開確認ではありません。 D: 展開確認の命令: テストは別カテゴリの確認を流用しており、CLI addr,immの根拠にならないため展開確認ではありません。展開確認の命令: テストに出る CLI addr,immは Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（2件）"
    **CLI addr,imm**

    - 検証目的: 記録照合の命令: テストについて、CLI addr,immは、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB060033の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、記録照合の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCLI addr,immを指定し、OSKB060033の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CLI addr,imm
    CASE OSKB060033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CLI addr,imm
    CASE OSKB060033
    SOURCE HLASM and z/OS System Programming
    ```

    CLI addr,immとOSKB060033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB060033を同じ出力で読み、記録照合の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB060033
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB060033
    ASMA90I CLI addr,imm ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB060033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の CLI addr,imm と OSKB060033 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB060033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

    ---

    **CLI addr,imm**

    - 検証目的: 終端検査の命令: テストについて、CLI addr,immは、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、終端検査の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にCLI addr,immを指定し、OSKB010065の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND CLI addr,imm
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM CLI addr,imm
    CASE OSKB010065
    SOURCE HLASM and z/OS System Programming
    ```

    CLI addr,immとOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010065を同じ出力で読み、終端検査の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010065
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010065
    ASMA90I CLI addr,imm ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の CLI addr,imm と OSKB010065 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### TM CC=0 {#c03-i0498}
*分類: 命令: テスト*  ・  難易度: 上級

TM CC=0は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（1問）"
    **問題.** 条件追跡の命令: テストに関係する TM CC=0 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBASM の結果から対象行を抜き出し、条件追跡の証跡として残す。 ✅
    - B. TM CC=0 の名称と担当者名のみを残して条件追跡の命令: テストの表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で条件追跡の命令: テストを確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず条件追跡の命令: テストの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡の命令: テストにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の命令: テストにおいて TM CC=0 は説明欄の「TM CC=0 の用途をアセンブラーの表示で確認する条件追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の命令: テストに関連して、HLASM and z/OS System Programmingでは TM CC=0 の表示属性と ASMA90I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の命令: テストは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の命令: テストは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の命令: テストは別カテゴリの確認を流用しており、TM CC=0 の根拠にならないため条件追跡ではありません。 D: 条件追跡の命令: テストは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため条件追跡ではありません。条件追跡の命令: テストで使う TM CC=0 という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は条件追跡です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（2件）"
    **TM CC=0**

    - 検証目的: 展開確認の命令: テストについて、TM CC=0 は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB060002の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、展開確認の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTM CC=0を指定し、OSKB060002の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TM CC=0
    CASE OSKB060002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TM CC=0
    CASE OSKB060002
    SOURCE HLASM and z/OS System Programming
    ```

    TM CC=0とOSKB060002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB060002を同じ出力で読み、展開確認の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB060002
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB060002
    ASMA90I TM CC=0 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB060002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TM CC=0 と OSKB060002 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB060002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

    ---

    **TM CC=0**

    - 検証目的: 展開検査の命令: テストについて、TM CC=0 は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、展開検査の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTM CC=0を指定し、OSKB010062の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TM CC=0
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TM CC=0
    CASE OSKB010062
    SOURCE HLASM and z/OS System Programming
    ```

    TM CC=0とOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010062を同じ出力で読み、展開検査の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010062
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010062
    ASMA90I TM CC=0 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TM CC=0 と OSKB010062 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### TM CC=1 {#c03-i0499}
*分類: 命令: テスト*  ・  難易度: 上級

TM CC=1は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（1問）"
    **問題.** 区切追跡の命令: テストで TM CC=1 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TM CC=1 の出力を取らず区切追跡の命令: テストの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切追跡の確認記録にまとめる。 ✅
    - C. ST OSKBASM を省略して区切追跡の命令: テストの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の命令: テストへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡の命令: テストにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡の命令: テストにおいて TM CC=1 は説明欄の「区切追跡の命令: テストに関係する定義値と表示行を照合する区切追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の命令: テストの証跡を読む担当者は、TM CC=1 の属性行と ASMA90I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の命令: テストは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の命令: テストは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の命令: テストは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の命令: テストは別カテゴリの確認を流用しており、TM CC=1 の根拠にならないため区切追跡ではありません。区切追跡の命令: テストに出る TM CC=1 は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（1件）"
    **TM CC=1**

    - 検証目的: 呼出検査の命令: テストについて、TM CC=1 は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、呼出検査の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTM CC=1を指定し、OSKB010063の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TM CC=1
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TM CC=1
    CASE OSKB010063
    SOURCE HLASM and z/OS System Programming
    ```

    TM CC=1とOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010063を同じ出力で読み、呼出検査の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010063
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010063
    ASMA90I TM CC=1 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TM CC=1 と OSKB010063 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### TM CC=3 {#c03-i0500}
*分類: 命令: テスト*  ・  難易度: 上級

TM CC=3は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（2問）"
    **問題.** 復旧確認の命令: テストで TM CC=3 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TM CC=3 の出力を取らず復旧確認の命令: テストの説明文と承認印だけを残す。
    - B. ST OSKBASM で得た表示本文を使い、復旧確認の採否を説明欄に結び付ける。 ✅
    - C. ST OSKBASM を省略して復旧確認の命令: テストの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を復旧確認の命令: テストへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では TM CC=3 は「復旧確認の命令: テストに関係する定義値と表示行を照合する復旧確認項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では TM CC=3 の属性行と ASMA90I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明だけに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では TM CC=3 を Assembler / システム・プログラミングの運用手順で確認し、初出名は復旧確認初出です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

    ---

    **問題.** 構文確認の命令: テストに関係する TM CC=3 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、構文確認の確認記録にまとめる。 ✅
    - B. TM CC=3 の名称と担当者名のみを残して構文確認の命令: テストの表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で構文確認の命令: テストを確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず構文確認の命令: テストの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認の命令: テストにおいて選択記号 A を採用し、識別名は構文確認です。構文確認の命令: テストにおいて TM CC=3 は説明欄の「TM CC=3 の用途をアセンブラーの表示で確認する構文確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の命令: テストに関連して、HLASM and z/OS System Programmingでは TM CC=3 の表示属性と ASMA90I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の命令: テストは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の命令: テストは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の命令: テストは別カテゴリの確認を流用しており、TM CC=3 の根拠にならないため構文確認ではありません。 D: 構文確認の命令: テストは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため構文確認ではありません。構文確認の命令: テストで使う TM CC=3 という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は構文確認です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（1件）"
    **TM CC=3**

    - 検証目的: 置換検査の命令: テストについて、TM CC=3 は、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、置換検査の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTM CC=3を指定し、OSKB010064の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TM CC=3
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TM CC=3
    CASE OSKB010064
    SOURCE HLASM and z/OS System Programming
    ```

    TM CC=3とOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010064を同じ出力で読み、置換検査の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010064
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010064
    ASMA90I TM CC=3 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TM CC=3 と OSKB010064 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### TM addr,mask {#c03-i0501}
*分類: 命令: テスト*  ・  難易度: 上級

TM addr,maskは、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（1問）"
    **問題.** 出力追跡の命令: テストに関する TM addr,maskの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず出力追跡の命令: テストの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の命令: テストの証跡として保存して根拠にする。
    - C. TM addr,maskの変更点を出力本文から切り離して出力追跡の命令: テストの承認欄のみ残す。
    - D. ASMA90I を含む表示を保存し、説明欄との差分を出力追跡で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡の命令: テストにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の命令: テストにおいて TM addr,mask は説明欄の「TM addr,maskの状態と出力メッセージを結び付ける出力追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の命令: テストに関する記録は、TM addr,maskの出力行と ASMA90I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の命令: テストは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の命令: テストは別カテゴリの確認を流用しており、TM addr,maskの根拠にならないため出力追跡ではありません。 C: 出力追跡の命令: テストは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の命令: テストは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の命令: テストで記録する TM addr,maskは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（1件）"
    **TM addr,mask**

    - 検証目的: 構文検査の命令: テストについて、TM addr,maskは、Assembler / システム・プログラミングの命令: テストで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、構文検査の命令: テストの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTM addr,maskを指定し、OSKB010061の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TM addr,mask
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TM addr,mask
    CASE OSKB010061
    SOURCE HLASM and z/OS System Programming
    ```

    TM addr,maskとOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010061を同じ出力で読み、構文検査の命令: テストの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010061
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010061
    ASMA90I TM addr,mask ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TM addr,mask と OSKB010061 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide




## Assembler / システム・プログラミング > 命令: データ移動

### L R1,disp(Rx,Rb) {#c03-i0502}
*分類: 命令: データ移動*  ・  難易度: 上級

L R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load。主記憶 4 バイトを R1 にロード (アライン要件あり) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 優先照合の命令: データ移動に関する L R1 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず優先照合の命令: データ移動の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを優先照合の命令: データ移動の証跡として保存して根拠にする。
    - C. L R1 命令の変更点を出力本文から切り離して優先照合の命令: データ移動の承認欄だけ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、優先照合の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では L R1 命令 は「L R1 命令の状態と出力メッセージを結び付ける優先照合項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では L R1 命令の出力行と ASMA90I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明だけに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では L R1 命令を HLASM and z/OS System Programmingの確認記録に残し、対象名は優先照合対象です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **L R1,disp(Rx,Rb)**

    - 検証目的: 区切確認の命令: データ移動について、L R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load。主記憶 4 バイトを R1 にロードに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、区切確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にL R1,disp(Rx,Rb)を指定し、OSKB010010の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND L R1,disp(Rx,Rb)
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM L R1,disp(Rx,Rb)
    CASE OSKB010010
    SOURCE HLASM and z/OS System Programming
    ```

    L R1,disp(Rx,Rb)とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010010を同じ出力で読み、区切確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010010
    ASMA90I L R1,disp(Rx,Rb) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の L R1,disp(Rx,Rb) と OSKB010010 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### LA R1,addr {#c03-i0503}
*分類: 命令: データ移動*  ・  難易度: 上級

LA R1,addrは、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Address。実効アドレス計算結果 (24/31bit) を R1 にロード。値計算にも利用 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? note "検証手順（2件）"
    **LA R1,addr**

    - 検証目的: 値域確認の命令: データ移動について、LA R1,addrは、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Address。実効アドレス計算結果 (24/31に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB060016の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、値域確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLA R1,addrを指定し、OSKB060016の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LA R1,addr
    CASE OSKB060016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LA R1,addr
    CASE OSKB060016
    SOURCE HLASM and z/OS System Programming
    ```

    LA R1,addrとOSKB060016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB060016を同じ出力で読み、値域確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB060016
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB060016
    ASMA90I LA R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB060016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LA R1,addr と OSKB060016 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB060016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

    ---

    **LA R1,addr**

    - 検証目的: 出力確認の命令: データ移動について、LA R1,addrは、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Address。実効アドレス計算結果 (24/31に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、出力確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLA R1,addrを指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LA R1,addr
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LA R1,addr
    CASE OSKB010008
    SOURCE HLASM and z/OS System Programming
    ```

    LA R1,addrとOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010008を同じ出力で読み、出力確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010008
    ASMA90I LA R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LA R1,addr と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### LA で小値生成 {#c03-i0504}
*分類: 命令: データ移動*  ・  難易度: 上級

LA で小値生成は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。LA R1,1 のように 0-4095 の定数を即値ロードする慣用句 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? note "検証手順（1件）"
    **LA で小値生成**

    - 検証目的: 条件確認の小値生成について、LA で小値生成は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。LA R1,1 のように 0-4095 の定数を即値ロードする慣に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、条件確認の小値生成の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLA で小値生成を指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LA で小値生成
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LA で小値生成
    CASE OSKB010009
    SOURCE HLASM and z/OS System Programming
    ```

    LA で小値生成とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010009を同じ出力で読み、条件確認の小値生成の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010009
    ASMA90I LA で小値生成 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LA で小値生成 と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### LG R1,disp(Rx,Rb) {#c03-i0505}
*分類: 命令: データ移動*  ・  難易度: 上級

LG R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Grande (64bit)。8 バイトを R1 にロード (z/Arch) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 置換確認の命令: データ移動に関する LG R1 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず置換確認の命令: データ移動の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の命令: データ移動の証跡として保存して根拠にする。
    - C. LG R1 命令の変更点を出力本文から切り離して置換確認の命令: データ移動の承認欄のみ残す。
    - D. 同じ画面で対象行と ASMA90I を読み、置換確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認の命令: データ移動において選択記号 D を採用し、識別名は置換確認です。置換確認の命令: データ移動において LG R1 命令 は説明欄の「LG R1 命令の状態と出力メッセージを結び付ける置換確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の命令: データ移動に関する記録は、LG R1 命令の出力行と ASMA90I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の命令: データ移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため置換確認ではありません。 B: 置換確認の命令: データ移動は別カテゴリの確認を流用しており、LG R1 命令の根拠にならないため置換確認ではありません。 C: 置換確認の命令: データ移動は名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の命令: データ移動は対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の命令: データ移動で記録する LG R1 命令は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は置換確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **LG R1,disp(Rx,Rb)**

    - 検証目的: 警告確認の命令: データ移動について、LG R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Grande (64bit)。8 バに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、警告確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLG R1,disp(Rx,Rb)を指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LG R1,disp(Rx,Rb)
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LG R1,disp(Rx,Rb)
    CASE OSKB010017
    SOURCE HLASM and z/OS System Programming
    ```

    LG R1,disp(Rx,Rb)とOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010017を同じ出力で読み、警告確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010017
    ASMA90I LG R1,disp(Rx,Rb) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LG R1,disp(Rx,Rb) と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa500] [zOS31_bpxb500]



### LGR R1,R2 {#c03-i0506}
*分類: 命令: データ移動*  ・  難易度: 上級

LGR R1,R2は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。64bit レジスタ間コピー (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 探索確認の命令: データ移動で LGR R1,R2 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LGR R1,R2 の出力を取らず探索確認の命令: データ移動の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 ✅
    - C. ST OSKBASM を省略して探索確認の命令: データ移動の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の命令: データ移動へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認の命令: データ移動において選択記号 B を採用し、識別名は探索確認です。探索確認の命令: データ移動において LGR R1,R2 は説明欄の「探索確認の命令: データ移動に関係する定義値と表示行を照合する探索確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認の命令: データ移動の証跡を読む担当者は、LGR R1,R2 の属性行と ASMA90I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認の命令: データ移動は名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認の命令: データ移動は対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認の命令: データ移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため探索確認ではありません。 D: 探索確認の命令: データ移動は別カテゴリの確認を流用しており、LGR R1,R2 の根拠にならないため探索確認ではありません。探索確認の命令: データ移動に出る LGR R1,R2 は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は探索確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **LGR R1,R2**

    - 検証目的: 監査確認の命令: データ移動について、LGR R1,R2 は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。64bit レジスタ間コピー (メインフレーム実践 (神居俊哉に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、監査確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLGR R1,R2を指定し、OSKB010019の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LGR R1,R2
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LGR R1,R2
    CASE OSKB010019
    SOURCE HLASM and z/OS System Programming
    ```

    LGR R1,R2とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010019を同じ出力で読み、監査確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010019
    ASMA90I LGR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LGR R1,R2 と OSKB010019 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa500] [zOS31_bpxb500]



### LH R1,disp(Rx,Rb) {#c03-i0507}
*分類: 命令: データ移動*  ・  難易度: 上級

LH R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Halfword。半語 2 バイトを符号拡張で R1 にロード (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? note "検証手順（1件）"
    **LH R1,disp(Rx,Rb)**

    - 検証目的: 範囲確認の命令: データ移動について、LH R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Halfword。半語 2 バイトをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、範囲確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLH R1,disp(Rx,Rb)を指定し、OSKB010011の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LH R1,disp(Rx,Rb)
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LH R1,disp(Rx,Rb)
    CASE OSKB010011
    SOURCE HLASM and z/OS System Programming
    ```

    LH R1,disp(Rx,Rb)とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010011を同じ出力で読み、範囲確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010011
    ASMA90I LH R1,disp(Rx,Rb) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LH R1,disp(Rx,Rb) と OSKB010011 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### LM R1,R3,addr {#c03-i0508}
*分類: 命令: データ移動*  ・  難易度: 上級

LM R1,R3,addrは、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Multiple。R1〜R3 を主記憶連続 4 バイト区画から一括ロード (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? note "検証手順（1件）"
    **LM R1,R3,addr**

    - 検証目的: 優先確認の命令: データ移動について、LM R1,R3,addrは、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Multiple。R1〜R3 を主記憶連続に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、優先確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLM R1,R3,addrを指定し、OSKB010012の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LM R1,R3,addr
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LM R1,R3,addr
    CASE OSKB010012
    SOURCE HLASM and z/OS System Programming
    ```

    LM R1,R3,addrとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010012を同じ出力で読み、優先確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010012
    ASMA90I LM R1,R3,addr ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LM R1,R3,addr と OSKB010012 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### LM R14,R12,12(R13) {#c03-i0509}
*分類: 命令: データ移動*  ・  難易度: 上級

LM R14,R12,12(R13)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。標準セーブエリアからのレジスタ復元慣用句 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 呼出検査の命令: データ移動でアセンブラーの運用確認を行います。LM R14 命令の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で呼出検査の命令: データ移動を確認した扱いにする。
    - B. ASMA90I の有無を確認せず呼出検査の命令: データ移動を正常終了として記録する。
    - C. 出典欄の説明と運用出力を照合し、呼出検査の確認記録にまとめる。 ✅
    - D. LM R14 命令の属性行を読まず呼出検査の命令: データ移動の画面名と利用者名だけを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では LM R14 命令 は「HLASM and z/OS System Programmingで LM R14 命令の扱いを記録する呼出検査項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では LM R14 命令の表示結果と ASMA90I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明だけに寄り、判定名は呼出検査不足です。呼出検査資料では LM R14 命令の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **LM R14,R12,12(R13)**

    - 検証目的: 記録確認の命令: データ移動について、LM R14,R12,12(R13)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。標準セーブエリアからのレジスタ復元慣用句 (に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、記録確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLM R14,R12,12(R13)を指定し、OSKB010013の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LM R14,R12,12(R13)
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LM R14,R12,12(R13)
    CASE OSKB010013
    SOURCE HLASM and z/OS System Programming
    ```

    LM R14,R12,12(R13)とOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010013を同じ出力で読み、記録確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010013
    ASMA90I LM R14,R12,12(R13) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LM R14,R12,12(R13) と OSKB010013 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### LR R1,R2 {#c03-i0510}
*分類: 命令: データ移動*  ・  難易度: 上級

LR R1,R2は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Register。汎用レジスタ R2 の 32 ビット内容を R1 にコピー (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 構文確認の命令: データ移動に関係する LR R1,R2 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ASMA90I を含む表示を保存し、説明欄との差分を構文確認で確認する。 ✅
    - B. LR R1,R2 の名称と担当者名だけを残して構文確認の命令: データ移動の表示本文を対象から外す。
    - C. アセンブラー以外の画面で構文確認の命令: データ移動を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず構文確認の命令: データ移動の戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では LR R1,R2 は「LR R1,R2 の用途をアセンブラーの表示で確認する構文確認項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では HLASM and z/OS System Programmingの LR R1,R2 と ASMA90I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明だけに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では LR R1,R2 を Assembler / システム・プログラミングで扱う確認対象とし、用語名は構文確認用語です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **LR R1,R2**

    - 検証目的: 上書確認の命令: データ移動について、LR R1,R2 は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Load Register。汎用レジスタ R2 の 32 ビットに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、上書確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にLR R1,R2を指定し、OSKB010007の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND LR R1,R2
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM LR R1,R2
    CASE OSKB010007
    SOURCE HLASM and z/OS System Programming
    ```

    LR R1,R2とOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010007を同じ出力で読み、上書確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010007
    ASMA90I LR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の LR R1,R2 と OSKB010007 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### ST R1,disp(Rx,Rb) {#c03-i0511}
*分類: 命令: データ移動*  ・  難易度: 上級

ST R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store。R1 の 4 バイトを主記憶に格納 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 構文確認の命令: データ移動に関係する ST R1 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBASM の結果から対象行を抜き出し、構文確認の証跡として残す。 ✅
    - B. ST R1 命令の名称と担当者名のみを残して構文確認の命令: データ移動の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で構文確認の命令: データ移動を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず構文確認の命令: データ移動の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認の命令: データ移動において選択記号 A を採用し、識別名は構文確認です。構文確認の命令: データ移動において ST R1 命令 は説明欄の「ST R1 命令の用途をアセンブラーの表示で確認する構文確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の命令: データ移動に関連して、HLASM and z/OS System Programmingでは ST R1 命令の表示属性と ASMA90I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の命令: データ移動は対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の命令: データ移動は名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の命令: データ移動は別カテゴリの確認を流用しており、ST R1 命令の根拠にならないため構文確認ではありません。 D: 構文確認の命令: データ移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため構文確認ではありません。構文確認の命令: データ移動で使う ST R1 命令という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は構文確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **ST R1,disp(Rx,Rb)**

    - 検証目的: 比較確認の命令: データ移動について、ST R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store。R1 の 4 バイトを主記憶に格納に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、比較確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にST R1,disp(Rx,Rb)を指定し、OSKB010014の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND ST R1,disp(Rx,Rb)
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM ST R1,disp(Rx,Rb)
    CASE OSKB010014
    SOURCE HLASM and z/OS System Programming
    ```

    ST R1,disp(Rx,Rb)とOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010014を同じ出力で読み、比較確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010014
    ASMA90I ST R1,disp(Rx,Rb) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の ST R1,disp(Rx,Rb) と OSKB010014 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### STG R1,disp(Rx,Rb) {#c03-i0512}
*分類: 命令: データ移動*  ・  難易度: 上級

STG R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store Grande (64bit)。R1 の 64bit を主記憶に格納 (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 終端確認の命令: データ移動に関係する STG R1 命令の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBASM で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 ✅
    - B. STG R1 命令の名称と担当者名のみを残して終端確認の命令: データ移動の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で終端確認の命令: データ移動を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず終端確認の命令: データ移動の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認の命令: データ移動において選択記号 A を採用し、識別名は終端確認です。終端確認の命令: データ移動において STG R1 命令 は説明欄の「STG R1 命令の用途をアセンブラーの表示で確認する終端確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の命令: データ移動に関連して、HLASM and z/OS System Programmingでは STG R1 命令の表示属性と ASMA90I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の命令: データ移動は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の命令: データ移動は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の命令: データ移動は別カテゴリの確認を流用しており、STG R1 命令の根拠にならないため終端確認ではありません。 D: 終端確認の命令: データ移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため終端確認ではありません。終端確認の命令: データ移動で使う STG R1 命令という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は終端確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **STG R1,disp(Rx,Rb)**

    - 検証目的: 復旧確認の命令: データ移動について、STG R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store Grande (64bit)。Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、復旧確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSTG R1,disp(Rx,Rb)を指定し、OSKB010018の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND STG R1,disp(Rx,Rb)
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM STG R1,disp(Rx,Rb)
    CASE OSKB010018
    SOURCE HLASM and z/OS System Programming
    ```

    STG R1,disp(Rx,Rb)とOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010018を同じ出力で読み、復旧確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010018
    ASMA90I STG R1,disp(Rx,Rb) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の STG R1,disp(Rx,Rb) と OSKB010018 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa500] [zOS31_bpxb500]



### STH R1,disp(Rx,Rb) {#c03-i0513}
*分類: 命令: データ移動*  ・  難易度: 上級

STH R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store Halfword。R1 の下位 2 バイトを主記憶に格納 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 展開確認の命令: データ移動で STH R1 命令の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. STH R1 命令の出力を取らず展開確認の命令: データ移動の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 ✅
    - C. ST OSKBASM を省略して展開確認の命令: データ移動の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の命令: データ移動へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認の命令: データ移動において選択記号 B を採用し、識別名は展開確認です。展開確認の命令: データ移動において STH R1 命令 は説明欄の「展開確認の命令: データ移動に関係する定義値と表示行を照合する展開確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の命令: データ移動の証跡を読む担当者は、STH R1 命令の属性行と ASMA90I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の命令: データ移動は名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の命令: データ移動は対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の命令: データ移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため展開確認ではありません。 D: 展開確認の命令: データ移動は別カテゴリの確認を流用しており、STH R1 命令の根拠にならないため展開確認ではありません。展開確認の命令: データ移動に出る STH R1 命令は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **STH R1,disp(Rx,Rb)**

    - 検証目的: 順序確認の命令: データ移動について、STH R1,disp(Rx,Rb)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store Halfword。R1 の下位に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、順序確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSTH R1,disp(Rx,Rb)を指定し、OSKB010015の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND STH R1,disp(Rx,Rb)
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM STH R1,disp(Rx,Rb)
    CASE OSKB010015
    SOURCE HLASM and z/OS System Programming
    ```

    STH R1,disp(Rx,Rb)とOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010015を同じ出力で読み、順序確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010015
    ASMA90I STH R1,disp(Rx,Rb) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の STH R1,disp(Rx,Rb) と OSKB010015 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]



### STM R14,R12,12(R13) {#c03-i0514}
*分類: 命令: データ移動*  ・  難易度: 上級

STM R14,R12,12(R13)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store Multiple。R14,R15,R0〜R12 をセーブエリアに格納する慣用句 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]

??? question "確認問題（1問）"
    **問題.** 呼出確認の命令: データ移動でアセンブラーの運用確認を行います。STM R14 命令の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で呼出確認の命令: データ移動を確認した扱いにする。
    - B. ASMA90I の有無を確認せず呼出確認の命令: データ移動を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. STM R14 命令の属性行を読まず呼出確認の命令: データ移動の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認の命令: データ移動において選択記号 C を採用し、識別名は呼出確認です。呼出確認の命令: データ移動において STM R14 命令 は説明欄の「HLASM and z/OS System Programmingで STM R14 命令の扱いを記録する呼出確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の命令: データ移動を受け取る担当者は、STM R14 命令の表示結果と ASMA90I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の命令: データ移動は別カテゴリの確認を流用しており、STM R14 命令の根拠にならないため呼出確認ではありません。 B: 呼出確認の命令: データ移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の命令: データ移動は対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の命令: データ移動は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の命令: データ移動が示す STM R14 命令は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **STM R14,R12,12(R13)**

    - 検証目的: 値域確認の命令: データ移動について、STM R14,R12,12(R13)は、Assembler / システム・プログラミングの命令: データ移動で確認する項目です。Store Multiple。R14,R1に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、値域確認の命令: データ移動の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にSTM R14,R12,12(R13を指定し、OSKB010016の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND STM R14,R12,12(R13
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM STM R14,R12,12(R13
    CASE OSKB010016
    SOURCE HLASM and z/OS System Programming
    ```

    STM R14,R12,12(R13とOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010016を同じ出力で読み、値域確認の命令: データ移動の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010016
    ASMA90I STM R14,R12,12(R13) ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の STM R14,R12,12(R13 と OSKB010016 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa500] [zOS31_bpxb500]




## Assembler / システム・プログラミング > 命令: 分岐

### B label {#c03-i0515}
*分類: 命令: 分岐*  ・  難易度: 上級

B labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch (BC 15,label の拡張ニーモニック)。無条件分岐 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 条件照合の命令: 分岐に関係する B labelの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBASM で得た表示本文を使い、条件照合の採否を説明欄に結び付ける。 ✅
    - B. B labelの名称と担当者名のみを残して条件照合の命令: 分岐の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で条件照合の命令: 分岐を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず条件照合の命令: 分岐の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合の命令: 分岐において選択記号 A を採用し、識別名は条件照合です。条件照合の命令: 分岐において B label は説明欄の「B labelの用途をアセンブラーの表示で確認する条件照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の命令: 分岐に関連して、HLASM and z/OS System Programmingでは B labelの表示属性と ASMA90I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の命令: 分岐は別カテゴリの確認を流用しており、B labelの根拠にならないため条件照合ではありません。 D: 条件照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため条件照合ではありません。条件照合の命令: 分岐で使う B labelという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **B label**

    - 検証目的: 展開追跡の命令: 分岐について、B labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch (BC 15,label の拡張ニーモニック)。無条件分岐に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、展開追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にB labelを指定し、OSKB010042の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND B label
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM B label
    CASE OSKB010042
    SOURCE HLASM and z/OS System Programming
    ```

    B labelとOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010042を同じ出力で読み、展開追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010042
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010042
    ASMA90I B label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の B label と OSKB010042 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BAKR R1,R2 {#c03-i0516}
*分類: 命令: 分岐*  ・  難易度: 上級

BAKR R1,R2は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Stack。リンケージスタックに状態を積んで分岐 (Stacking PC 系) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 監査照合の命令: 分岐でアセンブラーの運用確認を行います。BAKR R1,R2 の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で監査照合の命令: 分岐を確認した扱いにする。
    - B. ASMA90I の有無を確認せず監査照合の命令: 分岐を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査照合の根拠にする。 ✅
    - D. BAKR R1,R2 の属性行を読まず監査照合の命令: 分岐の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合の命令: 分岐において選択記号 C を採用し、識別名は監査照合です。監査照合の命令: 分岐において BAKR R1,R2 は説明欄の「HLASM and z/OS System Programmingで BAKR R1,R2 の扱いを記録する監査照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の命令: 分岐を受け取る担当者は、BAKR R1,R2 の表示結果と ASMA90I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の命令: 分岐は別カテゴリの確認を流用しており、BAKR R1,R2 の根拠にならないため監査照合ではありません。 B: 監査照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため監査照合ではありません。 C: 監査照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の命令: 分岐が示す BAKR R1,R2 は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BAKR R1,R2**

    - 検証目的: 優先追跡の命令: 分岐について、BAKR R1,R2 は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Stack。リンケージスタックに状態を積んでに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、優先追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBAKR R1,R2を指定し、OSKB010052の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BAKR R1,R2
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BAKR R1,R2
    CASE OSKB010052
    SOURCE HLASM and z/OS System Programming
    ```

    BAKR R1,R2とOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010052を同じ出力で読み、優先追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010052
    ASMA90I BAKR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BAKR R1,R2 と OSKB010052 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieaa600]



### BAL R1,label {#c03-i0517}
*分類: 命令: 分岐*  ・  難易度: 上級

BAL R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Link。次命令アドレス+CCその他を R1 に保存して分岐 (旧 24bit) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 値域照合の命令: 分岐に関する BAL R1,labelの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBBIND の結果を残さず値域照合の命令: 分岐の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の命令: 分岐の証跡として保存して根拠にする。
    - C. BAL R1,labelの変更点を出力本文から切り離して値域照合の命令: 分岐の承認欄のみ残す。
    - D. IEW2456I を含む表示を保存し、説明欄との差分を値域照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合の命令: 分岐において選択記号 D を採用し、識別名は値域照合です。値域照合の命令: 分岐において BAL R1,label は説明欄の「BAL R1,labelの状態と出力メッセージを結び付ける値域照合項目」と ST OSKBBIND または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の命令: 分岐に関する記録は、BAL R1,labelの出力行と IEW2456I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の命令: 分岐は戻り値や記録番号に寄り、IEW2456I や属性表示を落とすため値域照合ではありません。 B: 値域照合の命令: 分岐は別カテゴリの確認を流用しており、BAL R1,labelの根拠にならないため値域照合ではありません。 C: 値域照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の命令: 分岐で記録する BAL R1,labelは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BAL R1,label**

    - 検証目的: 条件追跡の命令: 分岐について、BAL R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Link。次命令アドレス+CC その他をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBBINDを実行し、IEW2456Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBBIND を入力し、条件追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBBIND
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBBIND
    ```

    COMMAND INPUTにST OSKBBINDが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBAL R1,labelを指定し、OSKB010049の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BAL R1,label
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BAL R1,label
    CASE OSKB010049
    SOURCE HLASM and z/OS System Programming
    ```

    BAL R1,labelとOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。IEW2456IとOSKB010049を同じ出力で読み、条件追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBBIND
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010049
    IEW2456I BAL R1,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    IEW2456IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBBIND が画面・出力に表示されること
    ② ステップ2 の BAL R1,label と OSKB010049 が画面・出力に表示されること
    ③ ステップ3 の IEW2456I と OSKB010049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BAS R1,label {#c03-i0518}
*分類: 命令: 分岐*  ・  難易度: 上級

BAS R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Save (31bit 安全)。R1 に純粋な戻りアドレスを保存 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（2問）"
    **問題.** 置換検査の命令: 分岐に関する BAS R1,labelの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず置換検査の命令: 分岐の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを置換検査の命令: 分岐の証跡として保存して根拠にする。
    - C. BAS R1,labelの変更点を出力本文から切り離して置換検査の命令: 分岐の承認欄だけ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて置換検査の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では BAS R1,label は「BAS R1,labelの状態と出力メッセージを結び付ける置換検査項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では BAS R1,labelの出力行と ASMA90I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明だけに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では BAS R1,labelを HLASM and z/OS System Programmingの確認記録に残し、対象名は置換検査対象です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400

    ---

    **問題.** 警告照合の命令: 分岐に関係する BAS R1,labelの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBASM の結果から対象行を抜き出し、警告照合の証跡として残す。 ✅
    - B. BAS R1,labelの名称と担当者名のみを残して警告照合の命令: 分岐の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で警告照合の命令: 分岐を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず警告照合の命令: 分岐の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合の命令: 分岐において選択記号 A を採用し、識別名は警告照合です。警告照合の命令: 分岐において BAS R1,label は説明欄の「BAS R1,labelの用途をアセンブラーの表示で確認する警告照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の命令: 分岐に関連して、HLASM and z/OS System Programmingでは BAS R1,labelの表示属性と ASMA90I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の命令: 分岐は別カテゴリの確認を流用しており、BAS R1,labelの根拠にならないため警告照合ではありません。 D: 警告照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため警告照合ではありません。警告照合の命令: 分岐で使う BAS R1,labelという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は警告照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BAS R1,label**

    - 検証目的: 区切追跡の命令: 分岐について、BAS R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Save (31bit 安全)。R1 にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、区切追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBAS R1,labelを指定し、OSKB010050の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BAS R1,label
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BAS R1,label
    CASE OSKB010050
    SOURCE HLASM and z/OS System Programming
    ```

    BAS R1,labelとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010050を同じ出力で読み、区切追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010050
    ASMA90I BAS R1,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BAS R1,label と OSKB010050 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BASR R1,R2 {#c03-i0519}
*分類: 命令: 分岐*  ・  難易度: 上級

BASR R1,R2は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BAS Register。戻りアドレスを R1 に、R2 の番地に分岐 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 復旧照合の命令: 分岐で BASR R1,R2 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BASR R1,R2 の出力を取らず復旧照合の命令: 分岐の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧照合の確認記録にまとめる。 ✅
    - C. ST OSKBASM を省略して復旧照合の命令: 分岐の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の命令: 分岐へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合の命令: 分岐において選択記号 B を採用し、識別名は復旧照合です。復旧照合の命令: 分岐において BASR R1,R2 は説明欄の「復旧照合の命令: 分岐に関係する定義値と表示行を照合する復旧照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の命令: 分岐の証跡を読む担当者は、BASR R1,R2 の属性行と ASMA90I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の命令: 分岐は別カテゴリの確認を流用しており、BASR R1,R2 の根拠にならないため復旧照合ではありません。復旧照合の命令: 分岐に出る BASR R1,R2 は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BASR R1,R2**

    - 検証目的: 範囲追跡の命令: 分岐について、BASR R1,R2 は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BAS Register。戻りアドレスを R1 に、R2 の番地にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、範囲追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBASR R1,R2を指定し、OSKB010051の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BASR R1,R2
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BASR R1,R2
    CASE OSKB010051
    SOURCE HLASM and z/OS System Programming
    ```

    BASR R1,R2とOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010051を同じ出力で読み、範囲追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010051
    ASMA90I BASR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BASR R1,R2 と OSKB010051 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BC mask,addr {#c03-i0520}
*分類: 命令: 分岐*  ・  難易度: 上級

BC mask,addrは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch on Condition。マスクと CC が一致したら分岐 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 区切照合の命令: 分岐で BC mask,addrの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BC mask,addrの出力を取らず区切照合の命令: 分岐の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切照合として引き継ぐ。 ✅
    - C. ST OSKBASM を省略して区切照合の命令: 分岐の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の命令: 分岐へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合の命令: 分岐において選択記号 B を採用し、識別名は区切照合です。区切照合の命令: 分岐において BC mask,addr は説明欄の「区切照合の命令: 分岐に関係する定義値と表示行を照合する区切照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の命令: 分岐の証跡を読む担当者は、BC mask,addrの属性行と ASMA90I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため区切照合ではありません。 D: 区切照合の命令: 分岐は別カテゴリの確認を流用しており、BC mask,addrの根拠にならないため区切照合ではありません。区切照合の命令: 分岐に出る BC mask,addrは Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BC mask,addr**

    - 検証目的: 呼出追跡の命令: 分岐について、BC mask,addrは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch on Condition。マスクと CC が一致に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、呼出追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBC mask,addrを指定し、OSKB010043の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BC mask,addr
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BC mask,addr
    CASE OSKB010043
    SOURCE HLASM and z/OS System Programming
    ```

    BC mask,addrとOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010043を同じ出力で読み、呼出追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010043
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010043
    ASMA90I BC mask,addr ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BC mask,addr と OSKB010043 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BC マスクビット 1 {#c03-i0521}
*分類: 命令: 分岐*  ・  難易度: 上級

BC マスクビット 1は、CC=3 で分岐 (BO) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（2問）"
    **問題.** 記録照合のマスクビットに関係する BC マスクビット 1の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、記録照合の点検結果を残す。 ✅
    - B. BC マスクビット 1の名称と担当者名だけを残して記録照合のマスクビットの表示本文を対象から外す。
    - C. アセンブラー以外の画面で記録照合のマスクビットを確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず記録照合のマスクビットの戻り値と時刻だけで完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では BC マスクビット 1 は「BC マスクビット 1の用途をアセンブラーの表示で確認する記録照合項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では HLASM and z/OS System Programmingの BC マスクビット 1と ASMA90I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明だけに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では BC マスクビット 1を Assembler / システム・プログラミングで扱う確認対象とし、用語名は記録照合用語です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400

    ---

    **問題.** 比較照合のマスクビットで BC マスクビット 1の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BC マスクビット 1の出力を取らず比較照合のマスクビットの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較照合の確認値として扱う。 ✅
    - C. ST OSKBASM を省略して比較照合のマスクビットの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合のマスクビットへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合のマスクビットにおいて選択記号 B を採用し、識別名は比較照合です。比較照合のマスクビットにおいて BC マスクビット 1 は説明欄の「比較照合のマスクビットに関係する定義値と表示行を照合する比較照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のマスクビットの証跡を読む担当者は、BC マスクビット 1の属性行と ASMA90I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のマスクビットは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のマスクビットは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のマスクビットは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため比較照合ではありません。 D: 比較照合のマスクビットは別カテゴリの確認を流用しており、BC マスクビット 1の根拠にならないため比較照合ではありません。比較照合のマスクビットに出る BC マスクビット 1は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BC マスクビット 1**

    - 検証目的: 上書追跡のマスクビットについて、BC マスクビット 1は、CC=3 で分岐 (BO) (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASM Language Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、上書追跡のマスクビットの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBC マスクビット 1を指定し、OSKB010047の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BC マスクビット 1
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BC マスクビット 1
    CASE OSKB010047
    SOURCE HLASM and z/OS System Programming
    ```

    BC マスクビット 1とOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010047を同じ出力で読み、上書追跡のマスクビットの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010047
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010047
    ASMA90I BC マスクビット 1 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BC マスクビット 1 と OSKB010047 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BC マスクビット 2 {#c03-i0522}
*分類: 命令: 分岐*  ・  難易度: 上級

BC マスクビット 2は、CC=2 で分岐 (BH) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 記録照合のマスクビットに関係する BC マスクビット 2の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録照合で再確認できる形にする。 ✅
    - B. BC マスクビット 2の名称と担当者名のみを残して記録照合のマスクビットの表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で記録照合のマスクビットを確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず記録照合のマスクビットの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合のマスクビットにおいて選択記号 A を採用し、識別名は記録照合です。記録照合のマスクビットにおいて BC マスクビット 2 は説明欄の「BC マスクビット 2の用途をアセンブラーの表示で確認する記録照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のマスクビットに関連して、HLASM and z/OS System Programmingでは BC マスクビット 2の表示属性と ASMA90I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のマスクビットは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のマスクビットは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のマスクビットは別カテゴリの確認を流用しており、BC マスクビット 2の根拠にならないため記録照合ではありません。 D: 記録照合のマスクビットは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため記録照合ではありません。記録照合のマスクビットで使う BC マスクビット 2という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は記録照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BC マスクビット 2**

    - 検証目的: 探索追跡のマスクビットについて、BC マスクビット 2は、CC=2 で分岐 (BH) (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASM Language Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、探索追跡のマスクビットの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBC マスクビット 2を指定し、OSKB010046の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BC マスクビット 2
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BC マスクビット 2
    CASE OSKB010046
    SOURCE HLASM and z/OS System Programming
    ```

    BC マスクビット 2とOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010046を同じ出力で読み、探索追跡のマスクビットの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010046
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010046
    ASMA90I BC マスクビット 2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BC マスクビット 2 と OSKB010046 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BC マスクビット 4 {#c03-i0523}
*分類: 命令: 分岐*  ・  難易度: 上級

BC マスクビット 4は、CC=1 で分岐 (BL) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 優先照合のマスクビットに関する BC マスクビット 4の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず優先照合のマスクビットの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のマスクビットの証跡として保存して根拠にする。
    - C. BC マスクビット 4の変更点を出力本文から切り離して優先照合のマスクビットの承認欄のみ残す。
    - D. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、優先照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合のマスクビットにおいて選択記号 D を採用し、識別名は優先照合です。優先照合のマスクビットにおいて BC マスクビット 4 は説明欄の「BC マスクビット 4の状態と出力メッセージを結び付ける優先照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のマスクビットに関する記録は、BC マスクビット 4の出力行と ASMA90I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のマスクビットは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため優先照合ではありません。 B: 優先照合のマスクビットは別カテゴリの確認を流用しており、BC マスクビット 4の根拠にならないため優先照合ではありません。 C: 優先照合のマスクビットは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のマスクビットは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のマスクビットで記録する BC マスクビット 4は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（2件）"
    **BC マスクビット 4**

    - 検証目的: 警告確認のマスクビットについて、BC マスクビット 4は、CC=1 で分岐 (BL) (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASM Language Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB060017の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、警告確認のマスクビットの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBC マスクビット 4を指定し、OSKB060017の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BC マスクビット 4
    CASE OSKB060017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BC マスクビット 4
    CASE OSKB060017
    SOURCE HLASM and z/OS System Programming
    ```

    BC マスクビット 4とOSKB060017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB060017を同じ出力で読み、警告確認のマスクビットの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB060017
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB060017
    ASMA90I BC マスクビット 4 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB060017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BC マスクビット 4 と OSKB060017 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB060017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

    ---

    **BC マスクビット 4**

    - 検証目的: 終端追跡のマスクビットについて、BC マスクビット 4は、CC=1 で分岐 (BL) (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASM Language Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、終端追跡のマスクビットの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBC マスクビット 4を指定し、OSKB010045の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BC マスクビット 4
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BC マスクビット 4
    CASE OSKB010045
    SOURCE HLASM and z/OS System Programming
    ```

    BC マスクビット 4とOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010045を同じ出力で読み、終端追跡のマスクビットの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010045
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010045
    ASMA90I BC マスクビット 4 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BC マスクビット 4 と OSKB010045 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BC マスクビット 8 {#c03-i0524}
*分類: 命令: 分岐*  ・  難易度: 上級

BC マスクビット 8は、CC=0 で分岐 (BE) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（2問）"
    **問題.** 展開確認のマスクビットで BC マスクビット 8の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BC マスクビット 8の出力を取らず展開確認のマスクビットの説明文と承認印だけを残す。
    - B. ST OSKBASM の結果から対象行を抜き出し、展開確認の証跡として残す。 ✅
    - C. ST OSKBASM を省略して展開確認のマスクビットの記録番号と時刻だけを残す。
    - D. 隣接項目の結果を展開確認のマスクビットへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では BC マスクビット 8 は「展開確認のマスクビットに関係する定義値と表示行を照合する展開確認項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では BC マスクビット 8の属性行と ASMA90I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明だけに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では BC マスクビット 8を Assembler / システム・プログラミングの運用手順で確認し、初出名は展開確認初出です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400

    ---

    **問題.** 範囲照合のマスクビットでアセンブラーの運用確認を行います。BC マスクビット 8の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で範囲照合のマスクビットを確認した扱いにする。
    - B. ASMA90I の有無を確認せず範囲照合のマスクビットを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲照合の確認にする。 ✅
    - D. BC マスクビット 8の属性行を読まず範囲照合のマスクビットの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合のマスクビットにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合のマスクビットにおいて BC マスクビット 8 は説明欄の「HLASM and z/OS System Programmingで BC マスクビット 8の扱いを記録する範囲照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のマスクビットを受け取る担当者は、BC マスクビット 8の表示結果と ASMA90I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のマスクビットは別カテゴリの確認を流用しており、BC マスクビット 8の根拠にならないため範囲照合ではありません。 B: 範囲照合のマスクビットは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のマスクビットは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のマスクビットは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のマスクビットが示す BC マスクビット 8は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BC マスクビット 8**

    - 検証目的: 置換追跡のマスクビットについて、BC マスクビット 8は、CC=0 で分岐 (BE) (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASM Language Rに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、置換追跡のマスクビットの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBC マスクビット 8を指定し、OSKB010044の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BC マスクビット 8
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BC マスクビット 8
    CASE OSKB010044
    SOURCE HLASM and z/OS System Programming
    ```

    BC マスクビット 8とOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010044を同じ出力で読み、置換追跡のマスクビットの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010044
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010044
    ASMA90I BC マスクビット 8 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BC マスクビット 8 と OSKB010044 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BCT R1,addr {#c03-i0525}
*分類: 命令: 分岐*  ・  難易度: 上級

Branch on Count。R1-=1 し非 0 なら分岐 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 構文追跡の命令: 分岐に関係する BCT R1,addrの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. ST OSKBASM で得た表示本文を使い、構文追跡の採否を説明欄に結び付ける。 ✅
    - B. BCT R1,addrの名称と担当者名のみを残して構文追跡の命令: 分岐の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で構文追跡の命令: 分岐を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず構文追跡の命令: 分岐の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡の命令: 分岐において選択記号 A を採用し、識別名は構文追跡です。構文追跡の命令: 分岐において BCT R1,addr は説明欄の「BCT R1,addrの用途をアセンブラーの表示で確認する構文追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の命令: 分岐に関連して、HLASM and z/OS System Programmingでは BCT R1,addrの表示属性と ASMA90I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の命令: 分岐は別カテゴリの確認を流用しており、BCT R1,addrの根拠にならないため構文追跡ではありません。 D: 構文追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため構文追跡ではありません。構文追跡の命令: 分岐で使う BCT R1,addrという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は構文追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BCT R1,addr**

    - 検証目的: 比較追跡の命令: 分岐について、Branch on Count。R1-=1 し非 0 なら分岐 (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASM Languに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、比較追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBCT R1,addrを指定し、OSKB010054の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BCT R1,addr
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BCT R1,addr
    CASE OSKB010054
    SOURCE HLASM and z/OS System Programming
    ```

    BCT R1,addrとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010054を同じ出力で読み、比較追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010054
    ASMA90I BCT R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BCT R1,addr と OSKB010054 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BCTR R1,R2 {#c03-i0526}
*分類: 命令: 分岐*  ・  難易度: 上級

BCTR R1,R2は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch on Count Register。R2=0 なら分岐せず R1 だけ -1 (LA 限度突破に多用) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 展開追跡の命令: 分岐で BCTR R1,R2 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BCTR R1,R2 の出力を取らず展開追跡の命令: 分岐の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開追跡として引き継ぐ。 ✅
    - C. ST OSKBASM を省略して展開追跡の命令: 分岐の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の命令: 分岐へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡の命令: 分岐において選択記号 B を採用し、識別名は展開追跡です。展開追跡の命令: 分岐において BCTR R1,R2 は説明欄の「展開追跡の命令: 分岐に関係する定義値と表示行を照合する展開追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の命令: 分岐の証跡を読む担当者は、BCTR R1,R2 の属性行と ASMA90I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の命令: 分岐は別カテゴリの確認を流用しており、BCTR R1,R2 の根拠にならないため展開追跡ではありません。展開追跡の命令: 分岐に出る BCTR R1,R2 は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BCTR R1,R2**

    - 検証目的: 順序追跡の命令: 分岐について、BCTR R1,R2 は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch on Count Register。R2=0 なら分に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、順序追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBCTR R1,R2を指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BCTR R1,R2
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BCTR R1,R2
    CASE OSKB010055
    SOURCE HLASM and z/OS System Programming
    ```

    BCTR R1,R2とOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010055を同じ出力で読み、順序追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010055
    ASMA90I BCTR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BCTR R1,R2 と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BR R1 {#c03-i0527}
*分類: 命令: 分岐*  ・  難易度: 上級

BR R1は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch Register (BCR 15,R1)。R1 の番地に無条件分岐 (R14 で復帰) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 順序照合の命令: 分岐でアセンブラーの運用確認を行います。BR R1 の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で順序照合の命令: 分岐を確認した扱いにする。
    - B. ASMA90I の有無を確認せず順序照合の命令: 分岐を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序照合の根拠を固定する。 ✅
    - D. BR R1 の属性行を読まず順序照合の命令: 分岐の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合の命令: 分岐において選択記号 C を採用し、識別名は順序照合です。順序照合の命令: 分岐において BR R1 は説明欄の「HLASM and z/OS System Programmingで BR R1 の扱いを記録する順序照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の命令: 分岐を受け取る担当者は、BR R1 の表示結果と ASMA90I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の命令: 分岐は別カテゴリの確認を流用しており、BR R1 の根拠にならないため順序照合ではありません。 B: 順序照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため順序照合ではありません。 C: 順序照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の命令: 分岐が示す BR R1 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BR R1**

    - 検証目的: 出力追跡の命令: 分岐について、BR R1 は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch Register (BCR 15,R1)。R1 の番地に無条件に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、出力追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBR R1を指定し、OSKB010048の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BR R1
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BR R1
    CASE OSKB010048
    SOURCE HLASM and z/OS System Programming
    ```

    BR R1とOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010048を同じ出力で読み、出力追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010048
    ASMA90I BR R1 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BR R1 と OSKB010048 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieaa600]



### BRAS R1,label {#c03-i0528}
*分類: 命令: 分岐*  ・  難易度: 上級

BRAS R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BAS の相対版 (16bit 相対オフセット) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 探索追跡の命令: 分岐で BRAS R1,labelの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BRAS R1,labelの出力を取らず探索追跡の命令: 分岐の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索追跡の確認値として扱う。 ✅
    - C. ST OSKBASM を省略して探索追跡の命令: 分岐の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の命令: 分岐へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡の命令: 分岐において選択記号 B を採用し、識別名は探索追跡です。探索追跡の命令: 分岐において BRAS R1,label は説明欄の「探索追跡の命令: 分岐に関係する定義値と表示行を照合する探索追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の命令: 分岐の証跡を読む担当者は、BRAS R1,labelの属性行と ASMA90I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の命令: 分岐は別カテゴリの確認を流用しており、BRAS R1,labelの根拠にならないため探索追跡ではありません。探索追跡の命令: 分岐に出る BRAS R1,labelは Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BRAS R1,label**

    - 検証目的: 監査追跡の命令: 分岐について、BRAS R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BAS の相対版 (16bit 相対オフセット) (メインフに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、監査追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBRAS R1,labelを指定し、OSKB010059の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BRAS R1,label
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BRAS R1,label
    CASE OSKB010059
    SOURCE HLASM and z/OS System Programming
    ```

    BRAS R1,labelとOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010059を同じ出力で読み、監査追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010059
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010059
    ASMA90I BRAS R1,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BRAS R1,label と OSKB010059 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]



### BRASL R1,label {#c03-i0529}
*分類: 命令: 分岐*  ・  難易度: 上級

BRASL R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BAS の相対版 (32bit 相対オフセット)。リンケージで多用 (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 上書追跡の命令: 分岐でアセンブラーの運用確認を行います。BRASL R1,labelの根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で上書追跡の命令: 分岐を確認した扱いにする。
    - B. ASMA90I の有無を確認せず上書追跡の命令: 分岐を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書追跡の根拠を固定する。 ✅
    - D. BRASL R1,labelの属性行を読まず上書追跡の命令: 分岐の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡の命令: 分岐において選択記号 C を採用し、識別名は上書追跡です。上書追跡の命令: 分岐において BRASL R1,label は説明欄の「HLASM and z/OS System Programmingで BRASL R1,labelの扱いを記録する上書追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の命令: 分岐を受け取る担当者は、BRASL R1,labelの表示結果と ASMA90I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の命令: 分岐は別カテゴリの確認を流用しており、BRASL R1,labelの根拠にならないため上書追跡ではありません。 B: 上書追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の命令: 分岐が示す BRASL R1,labelは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BRASL R1,label**

    - 検証目的: 変更追跡の命令: 分岐について、BRASL R1,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BAS の相対版 (32bit 相対オフセット)。リンケーに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、変更追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBRASL R1,labelを指定し、OSKB010060の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BRASL R1,label
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BRASL R1,label
    CASE OSKB010060
    SOURCE HLASM and z/OS System Programming
    ```

    BRASL R1,labelとOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010060を同じ出力で読み、変更追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010060
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010060
    ASMA90I BRASL R1,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BRASL R1,label と OSKB010060 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]



### BRC mask,label {#c03-i0530}
*分類: 命令: 分岐*  ・  難易度: 上級

BRC mask,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BC の相対分岐版 (Relative)。リロケータブル分岐 (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 終端追跡の命令: 分岐に関係する BRC mask,labelの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端追跡で再確認できる形にする。 ✅
    - B. BRC mask,labelの名称と担当者名のみを残して終端追跡の命令: 分岐の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で終端追跡の命令: 分岐を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず終端追跡の命令: 分岐の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡の命令: 分岐において選択記号 A を採用し、識別名は終端追跡です。終端追跡の命令: 分岐において BRC mask,label は説明欄の「BRC mask,labelの用途をアセンブラーの表示で確認する終端追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の命令: 分岐に関連して、HLASM and z/OS System Programmingでは BRC mask,labelの表示属性と ASMA90I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の命令: 分岐は別カテゴリの確認を流用しており、BRC mask,labelの根拠にならないため終端追跡ではありません。 D: 終端追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため終端追跡ではありません。終端追跡の命令: 分岐で使う BRC mask,labelという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BRC mask,label**

    - 検証目的: 復旧追跡の命令: 分岐について、BRC mask,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。BC の相対分岐版 (Relative)。リロケータブル分に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、復旧追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBRC mask,labelを指定し、OSKB010058の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BRC mask,label
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BRC mask,label
    CASE OSKB010058
    SOURCE HLASM and z/OS System Programming
    ```

    BRC mask,labelとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010058を同じ出力で読み、復旧追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010058
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010058
    ASMA90I BRC mask,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BRC mask,label と OSKB010058 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]



### BSM R1,R2 {#c03-i0531}
*分類: 命令: 分岐*  ・  難易度: 上級

BSM R1,R2は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Set Mode。AMODE 変更を伴う分岐 (24/31 切替) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 変更照合の命令: 分岐に関する BSM R1,R2 の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず変更照合の命令: 分岐の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の命令: 分岐の証跡として保存して根拠にする。
    - C. BSM R1,R2 の変更点を出力本文から切り離して変更照合の命令: 分岐の承認欄のみ残す。
    - D. 同じ画面で対象行と ASMA90I を読み、変更照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合の命令: 分岐において選択記号 D を採用し、識別名は変更照合です。変更照合の命令: 分岐において BSM R1,R2 は説明欄の「BSM R1,R2 の状態と出力メッセージを結び付ける変更照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の命令: 分岐に関する記録は、BSM R1,R2 の出力行と ASMA90I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため変更照合ではありません。 B: 変更照合の命令: 分岐は別カテゴリの確認を流用しており、BSM R1,R2 の根拠にならないため変更照合ではありません。 C: 変更照合の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の命令: 分岐は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の命令: 分岐で記録する BSM R1,R2 は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BSM R1,R2**

    - 検証目的: 記録追跡の命令: 分岐について、BSM R1,R2 は、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Branch And Set Mode。AMODE 変更を伴う分岐に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、記録追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBSM R1,R2を指定し、OSKB010053の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BSM R1,R2
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BSM R1,R2
    CASE OSKB010053
    SOURCE HLASM and z/OS System Programming
    ```

    BSM R1,R2とOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010053を同じ出力で読み、記録追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010053
    ASMA90I BSM R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BSM R1,R2 と OSKB010053 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]



### BXH R1,R3,label {#c03-i0532}
*分類: 命令: 分岐*  ・  難易度: 上級

BXH R1,R3,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Index High。インクリメント+比較 (上限到達まで) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 置換追跡の命令: 分岐に関する BXH R1,R3,labelの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず置換追跡の命令: 分岐の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の命令: 分岐の証跡として保存して根拠にする。
    - C. BXH R1,R3,labelの変更点を出力本文から切り離して置換追跡の命令: 分岐の承認欄のみ残す。
    - D. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、置換追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡の命令: 分岐において選択記号 D を採用し、識別名は置換追跡です。置換追跡の命令: 分岐において BXH R1,R3,label は説明欄の「BXH R1,R3,labelの状態と出力メッセージを結び付ける置換追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の命令: 分岐に関する記録は、BXH R1,R3,labelの出力行と ASMA90I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の命令: 分岐は別カテゴリの確認を流用しており、BXH R1,R3,labelの根拠にならないため置換追跡ではありません。 C: 置換追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の命令: 分岐で記録する BXH R1,R3,labelは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BXH R1,R3,label**

    - 検証目的: 警告追跡の命令: 分岐について、BXH R1,R3,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Index High。インクリメント+比較 (上限到達まに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、警告追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBXH R1,R3,labelを指定し、OSKB010057の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BXH R1,R3,label
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BXH R1,R3,label
    CASE OSKB010057
    SOURCE HLASM and z/OS System Programming
    ```

    BXH R1,R3,labelとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010057を同じ出力で読み、警告追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010057
    ASMA90I BXH R1,R3,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BXH R1,R3,label と OSKB010057 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]



### BXLE R1,R3,label {#c03-i0533}
*分類: 命令: 分岐*  ・  難易度: 上級

BXLE R1,R3,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Index Low or Equal。インクリメント+比較で分岐するループ命令 (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]

??? question "確認問題（1問）"
    **問題.** 呼出追跡の命令: 分岐でアセンブラーの運用確認を行います。BXLE R1 命令の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で呼出追跡の命令: 分岐を確認した扱いにする。
    - B. ASMA90I の有無を確認せず呼出追跡の命令: 分岐を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 ✅
    - D. BXLE R1 命令の属性行を読まず呼出追跡の命令: 分岐の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡の命令: 分岐において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の命令: 分岐において BXLE R1 命令 は説明欄の「HLASM and z/OS System Programmingで BXLE R1 命令の扱いを記録する呼出追跡項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の命令: 分岐を受け取る担当者は、BXLE R1 命令の表示結果と ASMA90I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の命令: 分岐は別カテゴリの確認を流用しており、BXLE R1 命令の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の命令: 分岐は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の命令: 分岐は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の命令: 分岐は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の命令: 分岐が示す BXLE R1 命令は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **BXLE R1,R3,label**

    - 検証目的: 値域追跡の命令: 分岐について、BXLE R1,R3,labelは、Assembler / システム・プログラミングの命令: 分岐で確認する項目です。Index Low or Equal。インクリメント+に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、値域追跡の命令: 分岐の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にBXLE R1,R3,labelを指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND BXLE R1,R3,label
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM BXLE R1,R3,label
    CASE OSKB010056
    SOURCE HLASM and z/OS System Programming
    ```

    BXLE R1,R3,labelとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010056を同じ出力で読み、値域追跡の命令: 分岐の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010056
    ASMA90I BXLE R1,R3,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の BXLE R1,R3,label と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa600]




## Assembler / システム・プログラミング > 命令: 変換

### TR addr1(l1),addr2 {#c03-i0534}
*分類: 命令: 変換*  ・  難易度: 上級

TR addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 変換で確認する項目です。Translate。各バイトを変換表 addr2 でルックアップして置換 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieae400]

??? question "確認問題（1問）"
    **問題.** 上書照合の命令: 変換でアセンブラーの運用確認を行います。TR addr1(l1) 命令の根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で上書照合の命令: 変換を確認した扱いにする。
    - B. ASMA90I の有無を確認せず上書照合の命令: 変換を正常終了として記録する。
    - C. 同じ画面で対象行と ASMA90I を読み、上書照合の結果として保存する。 ✅
    - D. TR addr1(l1) 命令の属性行を読まず上書照合の命令: 変換の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合の命令: 変換において選択記号 C を採用し、識別名は上書照合です。上書照合の命令: 変換において TR addr1(l1) 命令 は説明欄の「HLASM and z/OS System Programmingで TR addr1(l1) 命令の扱いを記録する上書照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の命令: 変換を受け取る担当者は、TR addr1(l1) 命令の表示結果と ASMA90I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の命令: 変換は別カテゴリの確認を流用しており、TR addr1(l1) 命令の根拠にならないため上書照合ではありません。 B: 上書照合の命令: 変換は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため上書照合ではありません。 C: 上書照合の命令: 変換は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の命令: 変換は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の命令: 変換が示す TR addr1(l1) 命令は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **TR addr1(l1),addr2**

    - 検証目的: 区切判定の命令: 変換について、TR addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 変換で確認する項目です。Translate。各バイトを変換表 addr2に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010090の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、区切判定の命令: 変換の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTR addr1(l1),addr2を指定し、OSKB010090の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TR addr1(l1),addr2
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TR addr1(l1),addr2
    CASE OSKB010090
    SOURCE HLASM and z/OS System Programming
    ```

    TR addr1(l1),addr2とOSKB010090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010090を同じ出力で読み、区切判定の命令: 変換の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010090
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010090
    ASMA90I TR addr1(l1),addr2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TR addr1(l1),addr2 と OSKB010090 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieae400]



### TRT addr1(l1),addr2 {#c03-i0535}
*分類: 命令: 変換*  ・  難易度: 上級

TRT addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 変換で確認する項目です。Translate and Test。0 でないコードに当たったら停止 (R1=位置, R2=コード) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieae400]

??? question "確認問題（1問）"
    **問題.** 出力照合の命令: 変換に関する TRT addr1 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず出力照合の命令: 変換の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の命令: 変換の証跡として保存して根拠にする。
    - C. TRT addr1 属性の変更点を出力本文から切り離して出力照合の命令: 変換の承認欄のみ残す。
    - D. ST OSKBASM で得た表示本文を使い、出力照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合の命令: 変換において選択記号 D を採用し、識別名は出力照合です。出力照合の命令: 変換において TRT addr1 属性 は説明欄の「TRT addr1 属性の状態と出力メッセージを結び付ける出力照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の命令: 変換に関する記録は、TRT addr1 属性の出力行と ASMA90I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の命令: 変換は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため出力照合ではありません。 B: 出力照合の命令: 変換は別カテゴリの確認を流用しており、TRT addr1 属性の根拠にならないため出力照合ではありません。 C: 出力照合の命令: 変換は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の命令: 変換は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の命令: 変換で記録する TRT addr1 属性は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **TRT addr1(l1),addr2**

    - 検証目的: 範囲判定の命令: 変換について、TRT addr1(l1),addr2は、Assembler / システム・プログラミングの命令: 変換で確認する項目です。Translate and Test。0 でないに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010091の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、範囲判定の命令: 変換の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTRT addr1(l1),addrを指定し、OSKB010091の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TRT addr1(l1),addr
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TRT addr1(l1),addr
    CASE OSKB010091
    SOURCE HLASM and z/OS System Programming
    ```

    TRT addr1(l1),addrとOSKB010091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010091を同じ出力で読み、範囲判定の命令: 変換の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010091
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010091
    ASMA90I TRT addr1(l1),addr2 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TRT addr1(l1),addr と OSKB010091 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ieae400]



### TRT で語句分割 {#c03-i0536}
*分類: 命令: 変換*  ・  難易度: 上級

TRT で語句分割は、Assembler / システム・プログラミングの命令: 変換で確認する項目です。区切り文字テーブル+TRT で構文解析の基本テクニック (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieae400]

??? question "確認問題（1問）"
    **問題.** 区切照合の語句分割で TRT で語句分割の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. TRT で語句分割の出力を取らず区切照合の語句分割の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切照合の確認にする。 ✅
    - C. ST OSKBASM を省略して区切照合の語句分割の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の語句分割へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合の語句分割において選択記号 B を採用し、識別名は区切照合です。区切照合の語句分割において TRT で語句分割 は説明欄の「区切照合の語句分割に関係する定義値と表示行を照合する区切照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の語句分割の証跡を読む担当者は、TRT で語句分割の属性行と ASMA90I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の語句分割は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の語句分割は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の語句分割は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため区切照合ではありません。 D: 区切照合の語句分割は別カテゴリの確認を流用しており、TRT で語句分割の根拠にならないため区切照合ではありません。区切照合の語句分割に出る TRT で語句分割は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **TRT で語句分割**

    - 検証目的: 記録判定の語句分割について、TRT で語句分割は、Assembler / システム・プログラミングの命令: 変換で確認する項目です。区切り文字テーブル+TRT で構文解析の基本テクニック (メインフレに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010093の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、記録判定の語句分割の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTRT で語句分割を指定し、OSKB010093の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TRT で語句分割
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TRT で語句分割
    CASE OSKB010093
    SOURCE HLASM and z/OS System Programming
    ```

    TRT で語句分割とOSKB010093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010093を同じ出力で読み、記録判定の語句分割の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010093
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010093
    ASMA90I TRT で語句分割 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TRT で語句分割 と OSKB010093 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieae400]



### TRT 停止後のレジスタ {#c03-i0537}
*分類: 命令: 変換*  ・  難易度: 上級

TRT 停止後のレジスタは、Assembler / システム・プログラミングの命令: 変換で確認する項目です。R1=停止位置のアドレス, R2 の下位 8bit=テーブル値 (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieae400]

??? question "確認問題（1問）"
    **問題.** 条件照合の停止後のレジスタに関係する TRT 停止後のレジスタの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件照合として引き継ぐ。 ✅
    - B. TRT 停止後のレジスタの名称と担当者名のみを残して条件照合の停止後のレジスタの表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で条件照合の停止後のレジスタを確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず条件照合の停止後のレジスタの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合の停止後のレジスタにおいて選択記号 A を採用し、識別名は条件照合です。条件照合の停止後のレジスタにおいて TRT 停止後のレジスタ は説明欄の「TRT 停止後のレジスタの用途をアセンブラーの表示で確認する条件照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の停止後のレジスタに関連して、HLASM and z/OS System Programmingでは TRT 停止後のレジスタの表示属性と ASMA90I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の停止後のレジスタは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の停止後のレジスタは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の停止後のレジスタは別カテゴリの確認を流用しており、TRT 停止後のレジスタの根拠にならないため条件照合ではありません。 D: 条件照合の停止後のレジスタは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため条件照合ではありません。条件照合の停止後のレジスタで使う TRT 停止後のレジスタという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **TRT 停止後のレジスタ**

    - 検証目的: 優先判定の停止後のレジスタについて、TRT 停止後のレジスタは、Assembler / システム・プログラミングの命令: 変換で確認する項目です。R1= 停止位置のアドレス, R2 の下位 8bit=テーブル値に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、優先判定の停止後のレジスタの確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にTRT 停止後のレジスタを指定し、OSKB010092の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND TRT 停止後のレジスタ
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM TRT 停止後のレジスタ
    CASE OSKB010092
    SOURCE HLASM and z/OS System Programming
    ```

    TRT 停止後のレジスタとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010092を同じ出力で読み、優先判定の停止後のレジスタの根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010092
    ASMA90I TRT 停止後のレジスタ ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の TRT 停止後のレジスタ と OSKB010092 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieae400]




## Assembler / システム・プログラミング > 命令: 実行

### EX R1,addr {#c03-i0538}
*分類: 命令: 実行*  ・  難易度: 上級

EX R1,addrは、Assembler / システム・プログラミングの命令: 実行で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（2問）"
    **問題.** 変更検査の命令: 実行に関する EX R1,addrの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず変更検査の命令: 実行の担当者名と日時だけを記録する。
    - B. 別製品のメッセージを変更検査の命令: 実行の証跡として保存して根拠にする。
    - C. EX R1,addrの変更点を出力本文から切り離して変更検査の命令: 実行の承認欄だけ残す。
    - D. 操作結果の本文、対象行、時刻を同じ証跡に入れ、変更検査の確認にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では EX R1,addr は「EX R1,addrの状態と出力メッセージを結び付ける変更検査項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では EX R1,addrの出力行と ASMA90I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明だけに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では EX R1,addrを HLASM and z/OS System Programmingの確認記録に残し、対象名は変更検査対象です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

    ---

    **問題.** 上書確認の命令: 実行でアセンブラーの運用確認を行います。EX R1,addrの根拠にできる作業はどれですか。

    - A. HLASM and z/OS System Programmingと無関係な一覧で上書確認の命令: 実行を確認した扱いにする。
    - B. ASMA90I の有無を確認せず上書確認の命令: 実行を正常終了として記録する。
    - C. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、上書確認の点検結果を残す。 ✅
    - D. EX R1,addrの属性行を読まず上書確認の命令: 実行の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認の命令: 実行において選択記号 C を採用し、識別名は上書確認です。上書確認の命令: 実行において EX R1,addr は説明欄の「HLASM and z/OS System Programmingで EX R1,addrの扱いを記録する上書確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の命令: 実行を受け取る担当者は、EX R1,addrの表示結果と ASMA90I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の命令: 実行は別カテゴリの確認を流用しており、EX R1,addrの根拠にならないため上書確認ではありません。 B: 上書確認の命令: 実行は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため上書確認ではありません。 C: 上書確認の命令: 実行は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の命令: 実行は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の命令: 実行が示す EX R1,addrは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（1件）"
    **EX R1,addr**

    - 検証目的: 区切検査の命令: 実行について、EX R1,addrは、Assembler / システム・プログラミングの命令: 実行で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、区切検査の命令: 実行の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEX R1,addrを指定し、OSKB010070の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EX R1,addr
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EX R1,addr
    CASE OSKB010070
    SOURCE HLASM and z/OS System Programming
    ```

    EX R1,addrとOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010070を同じ出力で読み、区切検査の命令: 実行の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010070
    ASMA90I EX R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の EX R1,addr と OSKB010070 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### EX で MVC 長可変化 {#c03-i0539}
*分類: 命令: 実行*  ・  難易度: 上級

EX で MVC 長可変化は、Assembler / システム・プログラミングの命令: 実行で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide

??? question "確認問題（1問）"
    **問題.** 出力確認の長可変化に関する EX で MVC 長可変化の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. ST OSKBASM の結果を残さず出力確認の長可変化の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の長可変化の証跡として保存して根拠にする。
    - C. EX で MVC 長可変化の変更点を出力本文から切り離して出力確認の長可変化の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認の長可変化において選択記号 D を採用し、識別名は出力確認です。出力確認の長可変化において EX で MVC 長可変化 は説明欄の「EX で MVC 長可変化の状態と出力メッセージを結び付ける出力確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の長可変化に関する記録は、EX で MVC 長可変化の出力行と ASMA90I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の長可変化は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため出力確認ではありません。 B: 出力確認の長可変化は別カテゴリの確認を流用しており、EX で MVC 長可変化の根拠にならないため出力確認ではありません。 C: 出力確認の長可変化は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の長可変化は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の長可変化で記録する EX で MVC 長可変化は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide


??? note "検証手順（1件）"
    **EX で MVC 長可変化**

    - 検証目的: 範囲検査の長可変化について、EX で MVC 長可変化は、Assembler / システム・プログラミングの命令: 実行で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、範囲検査の長可変化の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEX で MVC 長可変化を指定し、OSKB010071の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EX で MVC 長可変化
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EX で MVC 長可変化
    CASE OSKB010071
    SOURCE HLASM and z/OS System Programming
    ```

    EX で MVC 長可変化とOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010071を同じ出力で読み、範囲検査の長可変化の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010071
    ASMA90I EX で MVC 長可変化 ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の EX で MVC 長可変化 と OSKB010071 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: zOS_HLASM_Language_Reference / zOS_HLASM_Programmers_Guide



### EXRL R1,label {#c03-i0540}
*分類: 命令: 実行*  ・  難易度: 上級

EXRL R1,labelは、Assembler / システム・プログラミングの命令: 実行で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉

??? question "確認問題（1問）"
    **問題.** 条件確認の命令: 実行に関係する EXRL R1,labelの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件確認の確認値として扱う。 ✅
    - B. EXRL R1,labelの名称と担当者名のみを残して条件確認の命令: 実行の表示本文を確認対象に含めない。
    - C. アセンブラー以外の画面で条件確認の命令: 実行を確認し同じ証跡として扱ったことにする。
    - D. ASMA90I の有無を見ず条件確認の命令: 実行の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認の命令: 実行において選択記号 A を採用し、識別名は条件確認です。条件確認の命令: 実行において EXRL R1,label は説明欄の「EXRL R1,labelの用途をアセンブラーの表示で確認する条件確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の命令: 実行に関連して、HLASM and z/OS System Programmingでは EXRL R1,labelの表示属性と ASMA90I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の命令: 実行は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の命令: 実行は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の命令: 実行は別カテゴリの確認を流用しており、EXRL R1,labelの根拠にならないため条件確認ではありません。 D: 条件確認の命令: 実行は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため条件確認ではありません。条件確認の命令: 実行で使う EXRL R1,labelという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は条件確認です。

    **出典:** zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400


??? note "検証手順（1件）"
    **EXRL R1,label**

    - 検証目的: 優先検査の命令: 実行について、EXRL R1,labelは、Assembler / システム・プログラミングの命令: 実行で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。
    - セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===> に ST OSKBASM を入力し、優先検査の命令: 実行の確認表示へ進みます。
    操作（入力）:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST OSKBASM
    ```

    COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSDSFの表示結果です。FIND欄にEXRL R1,labelを指定し、OSKB010072の対象行を見つけます。
    操作（入力）:
    ```text
    (SDSF Result)
    COMMAND INPUT ===> FIND EXRL R1,label
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Result)
    ITEM EXRL R1,label
    CASE OSKB010072
    SOURCE HLASM and z/OS System Programming
    ```

    EXRL R1,labelとOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010072を同じ出力で読み、優先検査の命令: 実行の根拠を記録します。
    操作（入力）:
    ```text
    (SDSF Detail)
    COMMAND INPUT ===> ST OSKBASM
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF OUTPUT FOR OSKB010072
    ASMA90I EXRL R1,label ASSEMBLY OR BINDER DIAGNOSTIC
    IEW2646I 4 ESD/XSD PROCESSING COMPLETED
    IEW2456I 0 SYMBOL RESOLUTION COMPLETED
    ```

    ASMA90IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST OSKBASM が画面・出力に表示されること
    ② ステップ2 の EXRL R1,label と OSKB010072 が画面・出力に表示されること
    ③ ステップ3 の ASMA90I と OSKB010072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉


