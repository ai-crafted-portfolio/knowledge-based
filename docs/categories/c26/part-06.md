---
search:
  exclude: true
---

# RACF SETROPTS/RDEFINE/RACDCERT — 詳細 (6/6)

[← RACF SETROPTS/RDEFINE/RACDCERT の概要へ戻る](index.md)


## RACF SETROPTS/RDEFINE/RACDCERT > z/OS 3.1

### PASSWORD ALGORITHM デフォルト KDFAES {#c26-i0375}
*分類: z/OS 3.1*  ・  難易度: 上級

PASSWORD ALGORITHM デフォルト KDFAESは、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 出力検査のデフォルトに関する PASSWORD ALGORITHM デフォルトの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力検査のデフォルトの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査のデフォルトの証跡として保存して根拠にする。
    - C. PASSWORD ALGORITHM デフォルトの変更点を出力本文から切り離して出力検査のデフォルトの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検査のデフォルトにおいて選択記号 D を採用し、識別名は出力検査です。出力検査のデフォルトにおいて PASSWORD ALGORITHM デフォルト は説明欄の「PASSWORD ALGORITHM デフォルトの状態と出力メッセージを結び付ける出力検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査のデフォルトに関する記録は、PASSWORD ALGORITHM デフォルトの出力行と IRRD105I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査のデフォルトは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力検査ではありません。 B: 出力検査のデフォルトは別カテゴリの確認を流用しており、PASSWORD ALGORITHM デフォルトの根拠にならないため出力検査ではありません。 C: 出力検査のデフォルトは名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査のデフォルトは対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査のデフォルトで記録する PASSWORD ALGORITHM デフォルトは RACF の確認記録に残す対象名であり、用語名は出力検査です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **PASSWORD ALGORITHM デフォルト KDFAES**

    - 検証目的: 構文分離のデフォルトについて、PASSWORD ALGORITHM デフォルト KDFAES は、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030141の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、構文分離のデフォルトの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にPASSWORD ALGORITHMを指定し、OSKB030141の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND PASSWORD ALGORITHM
    CASE OSKB030141
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM PASSWORD ALGORITHM
    CASE OSKB030141
    SOURCE RACF
    ```

    PASSWORD ALGORITHMとOSKB030141が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030141を同じ出力で読み、構文分離のデフォルトの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030141
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030141 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I PASSWORD ALGORITHM デフォルト INFORMATION LISTED
    ```

    IRRD105IとOSKB030141が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の PASSWORD ALGORITHM と OSKB030141 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030141 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RACF 健全性チェック {#c26-i0376}
*分類: z/OS 3.1*  ・  難易度: 上級

RACF 健全性チェックは、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 範囲検査の健全性チェックでセキュリティ設定の運用確認を行います。RACF 健全性チェックの根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で範囲検査の健全性チェックを確認した扱いにする。
    - B. IRRD105I の有無を確認せず範囲検査の健全性チェックを正常終了として記録する。
    - C. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、範囲検査の採否を説明欄に結び付ける。 ✅
    - D. RACF 健全性チェックの属性行を読まず範囲検査の健全性チェックの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲検査の健全性チェックにおいて選択記号 C を採用し、識別名は範囲検査です。範囲検査の健全性チェックにおいて RACF 健全性チェック は説明欄の「RACF で RACF 健全性チェックの扱いを記録する範囲検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲検査です。範囲検査の健全性チェックを受け取る担当者は、RACF 健全性チェックの表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲検査です。不適切な選択肢を整理します。 A: 範囲検査の健全性チェックは別カテゴリの確認を流用しており、RACF 健全性チェックの根拠にならないため範囲検査ではありません。 B: 範囲検査の健全性チェックは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲検査ではありません。 C: 範囲検査の健全性チェックは対象出力と項目説明を結び、根拠を残すので範囲検査です。 D: 範囲検査の健全性チェックは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲検査ではありません。範囲検査の健全性チェックが示す RACF 健全性チェックは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲検査です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RACF 健全性チェック**

    - 検証目的: 置換分離の健全性チェックについて、RACF 健全性チェックは、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030144の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、置換分離の健全性チェックの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRACF 健全性チェックを指定し、OSKB030144の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RACF 健全性チェック
    CASE OSKB030144
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RACF 健全性チェック
    CASE OSKB030144
    SOURCE RACF
    ```

    RACF 健全性チェックとOSKB030144が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030144を同じ出力で読み、置換分離の健全性チェックの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030144
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030144 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RACF 健全性チェック INFORMATION LISTED
    ```

    IRRD105IとOSKB030144が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RACF 健全性チェック と OSKB030144 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030144 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RRSF 拡張 {#c26-i0377}
*分類: z/OS 3.1*  ・  難易度: 上級

RRSF 拡張は、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 優先検査の拡張に関する RRSF 拡張の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先検査の拡張の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の拡張の証跡として保存して根拠にする。
    - C. RRSF 拡張の変更点を出力本文から切り離して優先検査の拡張の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先検査として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検査の拡張において選択記号 D を採用し、識別名は優先検査です。優先検査の拡張において RRSF 拡張 は説明欄の「RRSF 拡張の状態と出力メッセージを結び付ける優先検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査の拡張に関する記録は、RRSF 拡張の出力行と IRRD105I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査の拡張は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先検査ではありません。 B: 優先検査の拡張は別カテゴリの確認を流用しており、RRSF 拡張の根拠にならないため優先検査ではありません。 C: 優先検査の拡張は名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査の拡張は対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査の拡張で記録する RRSF 拡張は RACF の確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RRSF 拡張**

    - 検証目的: 終端分離の拡張について、RRSF 拡張は、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030145の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端分離の拡張の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRRSF 拡張を指定し、OSKB030145の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RRSF 拡張
    CASE OSKB030145
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RRSF 拡張
    CASE OSKB030145
    SOURCE RACF
    ```

    RRSF 拡張とOSKB030145が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030145を同じ出力で読み、終端分離の拡張の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030145
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030145 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RRSF 拡張 INFORMATION LISTED
    ```

    IRRD105IとOSKB030145が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RRSF 拡張 と OSKB030145 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030145 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### TLS 1.3 用 RACDCERT サポート {#c26-i0378}
*分類: z/OS 3.1*  ・  難易度: 上級

TLS 1.3 用 RACDCERT サポートは、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 条件検査の用 サポートに関係する TLS 1 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて条件検査の根拠にする。 ✅
    - B. TLS 1 属性の名称と担当者名のみを残して条件検査の用 サポートの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で条件検査の用 サポートを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず条件検査の用 サポートの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件検査の用 サポートにおいて選択記号 A を採用し、識別名は条件検査です。条件検査の用 サポートにおいて TLS 1 属性 は説明欄の「TLS 1 属性の用途をセキュリティ設定の表示で確認する条件検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件検査です。条件検査の用 サポートに関連して、RACF では TLS 1 属性の表示属性と IRRD105I を同じ証跡に残し、背景名は条件検査です。他の選択肢を確認します。 A: 条件検査の用 サポートは対象出力と項目説明を結び、根拠を残すので条件検査です。 B: 条件検査の用 サポートは名称や説明のみに寄り、状態を示す出力本文が不足するため条件検査ではありません。 C: 条件検査の用 サポートは別カテゴリの確認を流用しており、TLS 1 属性の根拠にならないため条件検査ではありません。 D: 条件検査の用 サポートは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件検査ではありません。条件検査の用 サポートで使う TLS 1 属性という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件検査です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **TLS 1.3 用 RACDCERT サポート**

    - 検証目的: 展開分離の用 サポートについて、TLS 1.3 用 RACDCERT サポートは、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030142の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開分離の用 サポートの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にTLS 1.3 用 RACDCERTを指定し、OSKB030142の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND TLS 1.3 用 RACDCERT
    CASE OSKB030142
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM TLS 1.3 用 RACDCERT
    CASE OSKB030142
    SOURCE RACF
    ```

    TLS 1.3 用 RACDCERTとOSKB030142が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030142を同じ出力で読み、展開分離の用 サポートの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030142
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030142 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I TLS 1.3 用 RACDCERT サポート INFORMATION LISTED
    ```

    IRRD105IとOSKB030142が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の TLS 1.3 用 RACDCERT と OSKB030142 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030142 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## RACF SETROPTS/RDEFINE/RACDCERT > ユーティリティ

### IRRDBU00 {#c26-i0379}
*分類: ユーティリティ*  ・  難易度: 上級

IRRDBU00は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 警告確認のユーティリティに関係する IRRDBU00 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告確認の根拠を固定する。 ✅
    - B. IRRDBU00 の名称と担当者名のみを残して警告確認のユーティリティの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で警告確認のユーティリティを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず警告確認のユーティリティの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認のユーティリティにおいて選択記号 A を採用し、識別名は警告確認です。警告確認のユーティリティにおいて IRRDBU00 は説明欄の「IRRDBU00 の用途をセキュリティ設定の表示で確認する警告確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のユーティリティに関連して、RACF では IRRDBU00 の表示属性と IRRD105I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のユーティリティは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のユーティリティは別カテゴリの確認を流用しており、IRRDBU00 の根拠にならないため警告確認ではありません。 D: 警告確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため警告確認ではありません。警告確認のユーティリティで使う IRRDBU00 という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は警告確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRDBU00**

    - 検証目的: 区切判定のユーティリティについて、IRRDBU00 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030090の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切判定のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRDBU00を指定し、OSKB030090の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRDBU00
    CASE OSKB030090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRDBU00
    CASE OSKB030090
    SOURCE RACF
    ```

    IRRDBU00とOSKB030090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030090を同じ出力で読み、区切判定のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030090
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030090 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRDBU00 INFORMATION LISTED
    ```

    IRRD105IとOSKB030090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRDBU00 と OSKB030090 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRDBU00 と DB2 LOAD {#c26-i0380}
*分類: ユーティリティ*  ・  難易度: 上級

IRRDBU00 と DB2 LOADは、アンロード結果を Db2 にロードして分析。「IRRDBU00 と DB2 LOAD」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 監査確認のとでセキュリティ設定の運用確認を行います。IRRDBU00 と DB2 LOAD の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で監査確認のとを確認した扱いにする。
    - B. IRRD105I の有無を確認せず監査確認のとを正常終了として記録する。
    - C. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、監査確認の証跡として残す。 ✅
    - D. IRRDBU00 と DB2 LOAD の属性行を読まず監査確認のとの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認のとにおいて選択記号 C を採用し、識別名は監査確認です。監査確認のとにおいて IRRDBU00 と DB2 LOAD は説明欄の「RACF で IRRDBU00 と DB2 LOAD の扱いを記録する監査確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のとを受け取る担当者は、IRRDBU00 と DB2 LOAD の表示結果と IRRD105I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のとは別カテゴリの確認を流用しており、IRRDBU00 と DB2 LOAD の根拠にならないため監査確認ではありません。 B: 監査確認のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため監査確認ではありません。 C: 監査確認のとは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のとは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のとが示す IRRDBU00 と DB2 LOAD は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRDBU00 と DB2 LOAD**

    - 検証目的: 優先判定のとについて、IRRDBU00 と DB2 LOAD は、アンロード結果を Db2 にロードして分析。「IRRDBU00 と DB2 LOAD」を確認すると、SETROPTS、RDEFINに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030092の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先判定のとの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRDBU00 と DB2 LOAを指定し、OSKB030092の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRDBU00 と DB2 LOA
    CASE OSKB030092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRDBU00 と DB2 LOA
    CASE OSKB030092
    SOURCE RACF
    ```

    IRRDBU00 と DB2 LOAとOSKB030092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030092を同じ出力で読み、優先判定のとの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030092
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030092 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRDBU00 と DB2 LOAD INFORMATION LISTED
    ```

    IRRD105IとOSKB030092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRDBU00 と DB2 LOA と OSKB030092 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRDBU00 出力レコード タイプ {#c26-i0381}
*分類: ユーティリティ*  ・  難易度: 上級

IRRDBU00 出力レコード タイプは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? note "検証手順（1件）"
    **IRRDBU00 出力レコード タイプ**

    - 検証目的: 範囲判定の出力レコード タイプについて、IRRDBU00 出力レコード タイプは、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030091の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲判定の出力レコード タイプの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRDBU00 出力レコード タイを指定し、OSKB030091の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRDBU00 出力レコード タイ
    CASE OSKB030091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRDBU00 出力レコード タイ
    CASE OSKB030091
    SOURCE RACF
    ```

    IRRDBU00 出力レコード タイとOSKB030091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030091を同じ出力で読み、範囲判定の出力レコード タイプの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030091
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030091 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRDBU00 出力レコード タイプ INFORMATION LISTED
    ```

    IRRD105IとOSKB030091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRDBU00 出力レコード タイ と OSKB030091 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRRID00 {#c26-i0382}
*分類: ユーティリティ*  ・  難易度: 上級

IRRRID00は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 変更確認のユーティリティに関する IRRRID00 の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. RACDCERT ID(OSKBUSR) LIST の結果を残さず変更確認のユーティリティの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のユーティリティの証跡として保存して根拠にする。
    - C. IRRRID00 の変更点を出力本文から切り離して変更確認のユーティリティの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更確認の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認のユーティリティにおいて選択記号 D を採用し、識別名は変更確認です。変更確認のユーティリティにおいて IRRRID00 は説明欄の「IRRRID00 の状態と出力メッセージを結び付ける変更確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のユーティリティに関する記録は、IRRRID00 の出力行と IRRD105I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため変更確認ではありません。 B: 変更確認のユーティリティは別カテゴリの確認を流用しており、IRRRID00 の根拠にならないため変更確認ではありません。 C: 変更確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のユーティリティは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のユーティリティで記録する IRRRID00 は RACF の確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRRID00**

    - 検証目的: 記録判定のユーティリティについて、IRRRID00 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030093の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録判定のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRRID00を指定し、OSKB030093の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRRID00
    CASE OSKB030093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRRID00
    CASE OSKB030093
    SOURCE RACF
    ```

    IRRRID00とOSKB030093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030093を同じ出力で読み、記録判定のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030093
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030093 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRRID00 INFORMATION LISTED
    ```

    IRRD105IとOSKB030093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRRID00 と OSKB030093 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRRID00 と remove ID {#c26-i0383}
*分類: ユーティリティ*  ・  難易度: 上級

IRRRID00 と remove IDは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文照合のとに関係する IRRRID00 と remove ID の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文照合の根拠にする。 ✅
    - B. IRRRID00 と remove ID の名称と担当者名のみを残して構文照合のとの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で構文照合のとを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず構文照合のとの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合のとにおいて選択記号 A を採用し、識別名は構文照合です。構文照合のとにおいて IRRRID00 と remove ID は説明欄の「IRRRID00 と remove ID の用途をセキュリティ設定の表示で確認する構文照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のとに関連して、RACF では IRRRID00 と remove ID の表示属性と IRRD105I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のとは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のとは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のとは別カテゴリの確認を流用しており、IRRRID00 と remove ID の根拠にならないため構文照合ではありません。 D: 構文照合のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文照合ではありません。構文照合のとで使う IRRRID00 と remove ID という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRRID00 と remove ID**

    - 検証目的: 比較判定のとについて、IRRRID00 と remove ID は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030094の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較判定のとの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRRID00 と remove を指定し、OSKB030094の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRRID00 と remove 
    CASE OSKB030094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRRID00 と remove 
    CASE OSKB030094
    SOURCE RACF
    ```

    IRRRID00 と remove とOSKB030094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030094を同じ出力で読み、比較判定のとの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030094
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030094 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRRID00 と remove ID INFORMATION LISTED
    ```

    IRRD105IとOSKB030094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRRID00 と remove  と OSKB030094 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRRID00 出力 CLIST {#c26-i0384}
*分類: ユーティリティ*  ・  難易度: 上級

IRRRID00 出力 CLISTは、残存参照を削除する RACF コマンド CLIST を生成。「IRRRID00 出力 CLIST」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開照合の出力で IRRRID00 出力 CLIST の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IRRRID00 出力 CLIST の出力を取らず展開照合の出力の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IRRD105I を読み、展開照合の結果として保存する。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して展開照合の出力の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の出力へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合の出力において選択記号 B を採用し、識別名は展開照合です。展開照合の出力において IRRRID00 出力 CLIST は説明欄の「展開照合の出力に関係する定義値と表示行を照合する展開照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の出力の証跡を読む担当者は、IRRRID00 出力 CLIST の属性行と IRRD105I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の出力は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の出力は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の出力は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開照合ではありません。 D: 展開照合の出力は別カテゴリの確認を流用しており、IRRRID00 出力 CLIST の根拠にならないため展開照合ではありません。展開照合の出力に出る IRRRID00 出力 CLIST は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRRID00 出力 CLIST**

    - 検証目的: 順序判定の出力について、IRRRID00 出力 CLIST は、残存参照を削除する RACF コマンド CLIST を生成。「IRRRID00 出力 CLIST」を確認すると、SETROPTS、RDに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030095の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序判定の出力の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRRID00 出力 CLISTを指定し、OSKB030095の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRRID00 出力 CLIST
    CASE OSKB030095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRRID00 出力 CLIST
    CASE OSKB030095
    SOURCE RACF
    ```

    IRRRID00 出力 CLISTとOSKB030095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030095を同じ出力で読み、順序判定の出力の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030095
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030095 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRRID00 出力 CLIST INFORMATION LISTED
    ```

    IRRD105IとOSKB030095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRRID00 出力 CLIST と OSKB030095 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRUT100 {#c26-i0385}
*分類: ユーティリティ*  ・  難易度: 上級

IRRUT100は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 呼出照合のユーティリティでセキュリティ設定の運用確認を行います。IRRUT100 の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で呼出照合のユーティリティを確認した扱いにする。
    - B. IRRD105I の有無を確認せず呼出照合のユーティリティを正常終了として記録する。
    - C. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、呼出照合の採否を説明欄に結び付ける。 ✅
    - D. IRRUT100 の属性行を読まず呼出照合のユーティリティの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合のユーティリティにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合のユーティリティにおいて IRRUT100 は説明欄の「RACF で IRRUT100 の扱いを記録する呼出照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のユーティリティを受け取る担当者は、IRRUT100 の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のユーティリティは別カテゴリの確認を流用しており、IRRUT100 の根拠にならないため呼出照合ではありません。 B: 呼出照合のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のユーティリティは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のユーティリティが示す IRRUT100 は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRUT100**

    - 検証目的: 値域判定のユーティリティについて、IRRUT100 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030096の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域判定のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT100を指定し、OSKB030096の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRUT100
    CASE OSKB030096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRUT100
    CASE OSKB030096
    SOURCE RACF
    ```

    IRRUT100とOSKB030096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030096を同じ出力で読み、値域判定のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030096
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030096 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRUT100 INFORMATION LISTED
    ```

    IRRD105IとOSKB030096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRUT100 と OSKB030096 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRUT200 {#c26-i0386}
*分類: ユーティリティ*  ・  難易度: 上級

IRRUT200は、RACF DB のステータス・統計・索引整合性チェック。「IRRUT200」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 記録確認のユーティリティに関係する IRRUT200 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録確認の確認にする。 ✅
    - B. IRRUT200 の名称と担当者名のみを残して記録確認のユーティリティの表示本文を確認対象に含めない。
    - C. セキュリティ設定以外の画面で記録確認のユーティリティを確認し同じ証跡として扱ったことにする。
    - D. IRRD105I の有無を見ず記録確認のユーティリティの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認のユーティリティにおいて選択記号 A を採用し、識別名は記録確認です。記録確認のユーティリティにおいて IRRUT200 は説明欄の「IRRUT200 の用途をセキュリティ設定の表示で確認する記録確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認のユーティリティに関連して、RACF では IRRUT200 の表示属性と IRRD105I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認のユーティリティは対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認のユーティリティは別カテゴリの確認を流用しており、IRRUT200 の根拠にならないため記録確認ではありません。 D: 記録確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録確認ではありません。記録確認のユーティリティで使う IRRUT200 という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRUT200**

    - 検証目的: 探索判定のユーティリティについて、IRRUT200 は、RACF DB のステータス・統計・索引整合性チェック。「IRRUT200」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030086の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、探索判定のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT200を指定し、OSKB030086の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRUT200
    CASE OSKB030086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRUT200
    CASE OSKB030086
    SOURCE RACF
    ```

    IRRUT200とOSKB030086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030086を同じ出力で読み、探索判定のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030086
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030086 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRUT200 INFORMATION LISTED
    ```

    IRRD105IとOSKB030086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRUT200 と OSKB030086 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRUT200 PARM=INDEX/MAP {#c26-i0387}
*分類: ユーティリティ*  ・  難易度: 上級

IRRUT200 PARM=INDEX/MAPは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 構文照合保守の構文照合として IRRUT200 を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 名称と担当者名を保存して表示本文を確認しない。
    - B. 構文照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 別分類の結果を流用して同じ証跡として扱う。
    - D. 戻り値と時刻を主な根拠にして表示行を読まない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。構文照合保守で扱う IRRUT200 は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として IRRUT200 を扱い、分類内の確認名として保存します（構文照合保守終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRUT200 PARM=INDEX ・ MAP**

    - 検証目的: 上書判定の・について、IRRUT200 PARM=INDEX/MAP は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030087の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、上書判定の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT200 PARM=INDEを指定し、OSKB030087の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRUT200 PARM=INDE
    CASE OSKB030087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRUT200 PARM=INDE
    CASE OSKB030087
    SOURCE RACF
    ```

    IRRUT200 PARM=INDEとOSKB030087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030087を同じ出力で読み、上書判定の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030087
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030087 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRUT200 PARM=INDEX ・ MAP INFORMATION LISTED
    ```

    IRRD105IとOSKB030087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRUT200 PARM=INDE と OSKB030087 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRUT400 {#c26-i0388}
*分類: ユーティリティ*  ・  難易度: 上級

IRRUT400は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 順序確認のユーティリティでセキュリティ設定の運用確認を行います。IRRUT400 の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で順序確認のユーティリティを確認した扱いにする。
    - B. IRRD105I の有無を確認せず順序確認のユーティリティを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序確認で再確認できる形にする。 ✅
    - D. IRRUT400 の属性行を読まず順序確認のユーティリティの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認のユーティリティにおいて選択記号 C を採用し、識別名は順序確認です。順序確認のユーティリティにおいて IRRUT400 は説明欄の「RACF で IRRUT400 の扱いを記録する順序確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のユーティリティを受け取る担当者は、IRRUT400 の表示結果と IRRD105I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のユーティリティは別カテゴリの確認を流用しており、IRRUT400 の根拠にならないため順序確認ではありません。 B: 順序確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため順序確認ではありません。 C: 順序確認のユーティリティは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のユーティリティが示す IRRUT400 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRUT400**

    - 検証目的: 出力判定のユーティリティについて、IRRUT400 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030088の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、出力判定のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT400を指定し、OSKB030088の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRUT400
    CASE OSKB030088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRUT400
    CASE OSKB030088
    SOURCE RACF
    ```

    IRRUT400とOSKB030088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030088を同じ出力で読み、出力判定のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030088
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030088 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRUT400 INFORMATION LISTED
    ```

    IRRD105IとOSKB030088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRUT400 と OSKB030088 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### IRRUT400 PARM=ALLOCATE/NOLOCKINPUT {#c26-i0389}
*分類: ユーティリティ*  ・  難易度: 上級

IRRUT400 PARM=ALLOCATE/NOLOCKINPUTは、出力 DB 割振/排他制御指定。「IRRUT400 PARM=ALLOCATE/NOLOCKINPUT」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 展開照合権限の展開照合として IRRUT400 を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 別分類の結果を流用して同じ証跡として扱う。
    - B. 戻り値と時刻を主な根拠にして表示行を読まない。
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 展開照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。展開照合権限で扱う IRRUT400 は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として IRRUT400 を扱い、分類内の確認名として保存します（展開照合権限終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **IRRUT400 PARM=ALLOCATE ・ NOLOCKINPUT**

    - 検証目的: 条件判定の・について、IRRUT400 PARM=ALLOCATE/NOLOCKINPUT は、出力 DB 割振/排他制御指定。「IRRUT400 PARM=ALLOCATE/NOLOCKINPUに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030089の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、条件判定の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT400 PARM=ALLOを指定し、OSKB030089の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IRRUT400 PARM=ALLO
    CASE OSKB030089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IRRUT400 PARM=ALLO
    CASE OSKB030089
    SOURCE RACF
    ```

    IRRUT400 PARM=ALLOとOSKB030089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030089を同じ出力で読み、条件判定の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030089
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030089 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IRRUT400 PARM=ALLOCATE ・ N INFORMATION LISTED
    ```

    IRRD105IとOSKB030089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IRRUT400 PARM=ALLO と OSKB030089 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)



### RACUT200/RACUT400 JCL {#c26-i0390}
*分類: ユーティリティ*  ・  難易度: 上級

RACUT200/RACUT400 JCLは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS Security Server RACF Command Language Reference (z / OS 3.1)

??? question "確認問題（1問）"
    **問題.** 出力照合照合の出力照合として RACUT200/RACUT400 を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 承認欄の記入を優先して出力メッセージを保存しない。
    - C. 名称と担当者名を保存して表示本文を確認しない。
    - D. 出力照合の操作記録とメッセージを対応させて残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正解はDです。出力照合照合で扱う RACUT200/RACUT400 は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として RACUT200/RACUT400 を扱い、分類内の確認名として保存します（出力照合照合終点）。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（1件）"
    **RACUT200 ・ RACUT400 JCL**

    - 検証目的: 警告判定の・について、RACUT200/RACUT400 JCL は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030097の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、警告判定の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にRACUT200 ・ RACUT40を指定し、OSKB030097の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND RACUT200 ・ RACUT40
    CASE OSKB030097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM RACUT200 ・ RACUT40
    CASE OSKB030097
    SOURCE RACF
    ```

    RACUT200 ・ RACUT40とOSKB030097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030097を同じ出力で読み、警告判定の・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030097
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030097 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I RACUT200 ・ RACUT400 JCL INFORMATION LISTED
    ```

    IRRD105IとOSKB030097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の RACUT200 ・ RACUT40 と OSKB030097 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)




## その他

### その他（特定項目に紐づかないQA・手順） {#c26-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（3問）"
    **問題.** 展開追跡の:で PASSWORD 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PASSWORD 属性の出力を取らず展開追跡の:の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開追跡として引き継ぐ。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して展開追跡の:の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の:へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡の:において選択記号 B を採用し、識別名は展開追跡です。展開追跡の:において PASSWORD 属性 は説明欄の「展開追跡の:に関係する定義値と表示行を照合する展開追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の:の証跡を読む担当者は、PASSWORD 属性の属性行と IRRD105I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の:は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の:は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の:は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の:は別カテゴリの確認を流用しており、PASSWORD 属性の根拠にならないため展開追跡ではありません。展開追跡の:に出る PASSWORD 属性は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM

    ---

    **問題.** 呼出追跡のなどでセキュリティ設定の運用確認を行います。PASSWORD 属性の根拠にできる作業はどれですか。

    - A. RACF と無関係な一覧で呼出追跡のなどを確認した扱いにする。
    - B. IRRD105I の有無を確認せず呼出追跡のなどを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 ✅
    - D. PASSWORD 属性の属性行を読まず呼出追跡のなどの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡のなどにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のなどにおいて PASSWORD 属性 は説明欄の「RACF で PASSWORD 属性の扱いを記録する呼出追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のなどを受け取る担当者は、PASSWORD 属性の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のなどは別カテゴリの確認を流用しており、PASSWORD 属性の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のなどは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のなどは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のなどが示す PASSWORD 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM

    ---

    **問題.** 復旧照合のとはで SMF Type 80 とはの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SMF Type 80 とはの出力を取らず復旧照合のとはの説明文と承認印のみを残す。
    - B. RACF の表示形式に沿って根拠行を採り、復旧照合の点検結果を残す。 ✅
    - C. RACDCERT ID(OSKBUSR) LIST を省略して復旧照合のとはの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のとはへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合のとはにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合のとはにおいて SMF Type 80 とは は説明欄の「復旧照合のとはに関係する定義値と表示行を照合する復旧照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のとはの証跡を読む担当者は、SMF Type 80 とはの属性行と IRRD105I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のとはは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のとはは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のとはは別カテゴリの確認を流用しており、SMF Type 80 とはの根拠にならないため復旧照合ではありません。復旧照合のとはに出る SMF Type 80 とはは RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** zOS31_icha400 / Db2_zOS_RACF_ACM


??? note "検証手順（18件）"
    **PASSWORD(RULE1(LENGTH(m:n)など))**

    - 検証目的: 順序追跡の:について、PASSWORD(RULE1(LENGTH(m:n)など))は、RACF SETROPTS/RDEFINE/RACDCERT の PASSWORD で認証、権限、またはセキュリテに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序追跡の:の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にPASSWORD(RULE1(LENを指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND PASSWORD(RULE1(LEN
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM PASSWORD(RULE1(LEN
    CASE OSKB010055
    SOURCE RACF
    ```

    PASSWORD(RULE1(LENとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010055を同じ出力で読み、順序追跡の:の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010055 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I PASSWORD(RULE1(LENGTH(m: INFORMATION LISTED
    ```

    IRRD105IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の PASSWORD(RULE1(LEN と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **PASSWORD(RULE2)など RULE8**

    - 検証目的: 値域追跡のなどについて、PASSWORD(RULE2)など RULE8 は、最大 8 種類のパスワード書式ルールを定義可。「PASSWORD(RULE2)など RULE8」を確認すると、SETROPTSに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、値域追跡のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にPASSWORD(RULE2)など を指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND PASSWORD(RULE2)など 
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM PASSWORD(RULE2)など 
    CASE OSKB010056
    SOURCE RACF
    ```

    PASSWORD(RULE2)など とOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010056を同じ出力で読み、値域追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010056 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I PASSWORD(RULE2)など RULE8 INFORMATION LISTED
    ```

    IRRD105IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の PASSWORD(RULE2)など  と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **LOGOPTIONS(SUCCESSES|FAILURES(clas**

    - 検証目的: 優先判定の|について、LOGOPTIONS(SUCCESSES|FAILURES(class))は、成功のみ/失敗のみを記録。「LOGOPTIONS(SUCCESSES|FAILURES(claに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先判定の|の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にLOGOPTIONS(SUCCESSを指定し、OSKB010092の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND LOGOPTIONS(SUCCESS
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM LOGOPTIONS(SUCCESS
    CASE OSKB010092
    SOURCE RACF
    ```

    LOGOPTIONS(SUCCESSとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010092を同じ出力で読み、優先判定の|の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB010092
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB010092 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I LOGOPTIONS(SUCCESSES|FAI INFORMATION LISTED
    ```

    IRRD105IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の LOGOPTIONS(SUCCESS と OSKB010092 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB010092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **UACC(READ|UPDATE|CONTROL|ALTER|NON**

    - 検証目的: 優先確認の| |について、UACC(READ|UPDATE|CONTROL|ALTER|NONE)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先確認の| |の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にUACC(READ|UPDATE|Cを指定し、OSKB020012の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND UACC(READ|UPDATE|C
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM UACC(READ|UPDATE|C
    CASE OSKB020012
    SOURCE RACF
    ```

    UACC(READ|UPDATE|CとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020012を同じ出力で読み、優先確認の| |の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020012 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I UACC(READ|UPDATE|CONTROL INFORMATION LISTED
    ```

    IRRD105IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の UACC(READ|UPDATE|C と OSKB020012 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **CATEGORY(name1,name2,など)**

    - 検証目的: 終端照合のなどについて、CATEGORY(name1,name2,など)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、終端照合のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にCATEGORY(name1,namを指定し、OSKB020025の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND CATEGORY(name1,nam
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM CATEGORY(name1,nam
    CASE OSKB020025
    SOURCE RACF
    ```

    CATEGORY(name1,namとOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020025を同じ出力で読み、終端照合のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020025
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020025 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I CATEGORY(name1,name2,など) INFORMATION LISTED
    ```

    IRRD105IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の CATEGORY(name1,nam と OSKB020025 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **WHEN(DAYS(など)|TIME(など))**

    - 検証目的: 優先照合のなど | などについて、WHEN(DAYS(など)|TIME(など))は、アクセス可能な曜日/時間帯。「WHEN(DAYS(など)|TIME(など))」を確認すると、SETROPTS、RDEFINに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先照合のなど | などの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(DAYS(など)|TIMEを指定し、OSKB020032の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND WHEN(DAYS(など)|TIME
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM WHEN(DAYS(など)|TIME
    CASE OSKB020032
    SOURCE RACF
    ```

    WHEN(DAYS(など)|TIMEとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020032を同じ出力で読み、優先照合のなど | などの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020032 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I WHEN(DAYS(など)|TIME(など)) INFORMATION LISTED
    ```

    IRRD105IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の WHEN(DAYS(など)|TIME と OSKB020032 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **ADDMEM(member1,member2,など)**

    - 検証目的: 記録照合のなについて、ADDMEM(member1,member2,など)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録照合のなの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にADDMEM(member1,memを指定し、OSKB020033の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ADDMEM(member1,mem
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ADDMEM(member1,mem
    CASE OSKB020033
    SOURCE RACF
    ```

    ADDMEM(member1,memとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020033を同じ出力で読み、記録照合のなの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020033 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ADDMEM(member1,member2,な INFORMATION LISTED
    ```

    IRRD105IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ADDMEM(member1,mem と OSKB020033 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **JESJOBS SUBMIT.nodeid.jobname.owne**

    - 検証目的: 記録追跡のセキュリティ設定について、JESJOBS SUBMIT.nodeid.jobname.ownerは、ジョブ サブミット権限プロファイル。「JESJOBS SUBMIT.nodeid.jobname.に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、記録追跡のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にJESJOBS SUBMIT.nodを指定し、OSKB020053の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JESJOBS SUBMIT.nod
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JESJOBS SUBMIT.nod
    CASE OSKB020053
    SOURCE RACF
    ```

    JESJOBS SUBMIT.nodとOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020053を同じ出力で読み、記録追跡のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020053
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020053 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JESJOBS SUBMIT.nodeid.jo INFORMATION LISTED
    ```

    IRRD105IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JESJOBS SUBMIT.nod と OSKB020053 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **JESJOBS CANCEL.nodeid.userid.jobna**

    - 検証目的: 比較追跡のセキュリティ設定について、JESJOBS CANCEL.nodeid.userid.jobnameは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較追跡のセキュリティ設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にJESJOBS CANCEL.nodを指定し、OSKB020054の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND JESJOBS CANCEL.nod
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM JESJOBS CANCEL.nod
    CASE OSKB020054
    SOURCE RACF
    ```

    JESJOBS CANCEL.nodとOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020054を同じ出力で読み、比較追跡のセキュリティ設定の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB020054
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB020054 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I JESJOBS CANCEL.nodeid.us INFORMATION LISTED
    ```

    IRRD105IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の JESJOBS CANCEL.nod と OSKB020054 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB020054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **SIGNWITH(SITE LABEL(など))**

    - 検証目的: 区切照合のなどについて、SIGNWITH(SITE LABEL(など))は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT GENCERT で認証、権限、またはセキュに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、区切照合のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSIGNWITH(SITE LABEを指定し、OSKB030030の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SIGNWITH(SITE LABE
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SIGNWITH(SITE LABE
    CASE OSKB030030
    SOURCE RACF
    ```

    SIGNWITH(SITE LABEとOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030030を同じ出力で読み、区切照合のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030030
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030030 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SIGNWITH(SITE LABEL(など)) INFORMATION LISTED
    ```

    IRRD105IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SIGNWITH(SITE LABE と OSKB030030 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **KEYUSAGE(HANDSHAKE|DATAENCRYPT|CER**

    - 検証目的: 範囲照合の|について、KEYUSAGE(HANDSHAKE|DATAENCRYPT|CERTSIGN など)は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT GEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲照合の|の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にKEYUSAGE(HANDSHAKEを指定し、OSKB030031の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND KEYUSAGE(HANDSHAKE
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM KEYUSAGE(HANDSHAKE
    CASE OSKB030031
    SOURCE RACF
    ```

    KEYUSAGE(HANDSHAKEとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030031を同じ出力で読み、範囲照合の|の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030031
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030031 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I KEYUSAGE(HANDSHAKE|DATAE INFORMATION LISTED
    ```

    IRRD105IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の KEYUSAGE(HANDSHAKE と OSKB030031 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **ALTNAME(IP(など)|DOMAIN(など)|EMAIL(など**

    - 検証目的: 優先照合のなど | などについて、ALTNAME(IP(など)|DOMAIN(など)|EMAIL(など)|URI(など))は、サブジェクト代替名 (SAN)。「ALTNAME(IP(など)|DOMAIN(なに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、優先照合のなど | などの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にALTNAME(IP(など)|DOMを指定し、OSKB030032の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND ALTNAME(IP(など)|DOM
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM ALTNAME(IP(など)|DOM
    CASE OSKB030032
    SOURCE RACF
    ```

    ALTNAME(IP(など)|DOMとOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030032を同じ出力で読み、優先照合のなど | などの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030032
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030032 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I ALTNAME(IP(など)|DOMAIN(など INFORMATION LISTED
    ```

    IRRD105IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の ALTNAME(IP(など)|DOM と OSKB030032 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **LIST(LABEL('など'))**

    - 検証目的: 比較追跡のなどについて、LIST(LABEL('など'))は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT LIST で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030054の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、比較追跡のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にLIST(LABEL('など'))を指定し、OSKB030054の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND LIST(LABEL('など'))
    CASE OSKB030054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM LIST(LABEL('など'))
    CASE OSKB030054
    SOURCE RACF
    ```

    LIST(LABEL('など'))とOSKB030054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030054を同じ出力で読み、比較追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030054
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030054 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I LIST(LABEL('など')) INFORMATION LISTED
    ```

    IRRD105IとOSKB030054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の LIST(LABEL('など')) と OSKB030054 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **LIST(SERIALNUMBER(など) ISSUERSDN(など**

    - 検証目的: 順序追跡のなどについて、LIST(SERIALNUMBER(など) ISSUERSDN(など))は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT LIST で認証、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030055の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、順序追跡のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にLIST(SERIALNUMBER(を指定し、OSKB030055の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND LIST(SERIALNUMBER(
    CASE OSKB030055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM LIST(SERIALNUMBER(
    CASE OSKB030055
    SOURCE RACF
    ```

    LIST(SERIALNUMBER(とOSKB030055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030055を同じ出力で読み、順序追跡のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030055
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030055 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I LIST(SERIALNUMBER(など) IS INFORMATION LISTED
    ```

    IRRD105IとOSKB030055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の LIST(SERIALNUMBER( と OSKB030055 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **SDNFILTER('など')**

    - 検証目的: 展開検査のなどについて、SDNFILTER('など')は、Subject DN フィルタ。「SDNFILTER('など')」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030062の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、展開検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にSDNFILTER('など')を指定し、OSKB030062の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND SDNFILTER('など')
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM SDNFILTER('など')
    CASE OSKB030062
    SOURCE RACF
    ```

    SDNFILTER('など')とOSKB030062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030062を同じ出力で読み、展開検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030062 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I SDNFILTER('など') INFORMATION LISTED
    ```

    IRRD105IとOSKB030062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の SDNFILTER('など') と OSKB030062 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **IDNFILTER('など')**

    - 検証目的: 呼出検査のなどについて、IDNFILTER('など')は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT MAP で認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030063の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、呼出検査のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にIDNFILTER('など')を指定し、OSKB030063の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND IDNFILTER('など')
    CASE OSKB030063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM IDNFILTER('など')
    CASE OSKB030063
    SOURCE RACF
    ```

    IDNFILTER('など')とOSKB030063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030063を同じ出力で読み、呼出検査のなどの根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030063
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030063 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I IDNFILTER('など') INFORMATION LISTED
    ```

    IRRD105IとOSKB030063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の IDNFILTER('など') と OSKB030063 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **DEFAULT ・ PERSONAL ・ CERTAUTH ・ SITE USA**

    - 検証目的: 範囲検査の・ ・について、DEFAULT/PERSONAL/CERTAUTH/SITE USAGE は、Key Ring 内の用途指定。「DEFAULT/PERSONAL/CERTAUTH/SITEに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030071の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、範囲検査の・ ・の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にDEFAULT ・ PERSONALを指定し、OSKB030071の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND DEFAULT ・ PERSONAL
    CASE OSKB030071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM DEFAULT ・ PERSONAL
    CASE OSKB030071
    SOURCE RACF
    ```

    DEFAULT ・ PERSONALとOSKB030071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030071を同じ出力で読み、範囲検査の・ ・の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030071
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030071 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I DEFAULT ・ PERSONAL ・ CERTAUT INFORMATION LISTED
    ```

    IRRD105IとOSKB030071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の DEFAULT ・ PERSONAL と OSKB030071 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

    ---

    **LISTUSER など AUDITOR 専用**

    - 検証目的: 復旧検査のなど 専用について、LISTUSER など AUDITOR 専用は、RACF SETROPTS/RDEFINE/RACDCERT の AUDITOR コマンドで状態表示や操作を行うためのコマンド関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030078の検証用出力を記録できる。
    - セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===> に RACDCERT ID(OSKBUSR) LIST を入力し、復旧検査のなど 専用の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    ```

    COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO RACFの表示結果です。FIND欄にLISTUSER など AUDITOを指定し、OSKB030078の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO RACF Result)
    COMMAND INPUT ===> FIND LISTUSER など AUDITO
    CASE OSKB030078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO RACF Result)
    ITEM LISTUSER など AUDITO
    CASE OSKB030078
    SOURCE RACF
    ```

    LISTUSER など AUDITOとOSKB030078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030078を同じ出力で読み、復旧検査のなど 専用の根拠を記録します。
    操作（入力）:
    ```text
    (TSO RACF Detail)
    COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST
    CASE OSKB030078
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO RACF COMMAND RESPONSE
    RACDCERT ID(OSKBUSR) LIST
    USER=OSKB030078 OWNER=SYS1 DEFAULT-GROUP=SYS1
    IRRD105I LISTUSER など AUDITOR 専用 INFORMATION LISTED
    ```

    IRRD105IとOSKB030078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
    ② ステップ2 の LISTUSER など AUDITO と OSKB030078 が画面・出力に表示されること
    ③ ステップ3 の IRRD105I と OSKB030078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)

