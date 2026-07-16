---
search:
  exclude: true
---

# IMS 15.5 — 詳細 (3/3)

[← IMS 15.5 の概要へ戻る](index.md)


## IMS 15.5 > 定義体

### ACB {#c16-i0213}
*分類: 定義体*  ・  難易度: 中級

IMS 15.5 の 定義体で扱うACBは、DBD と PSB から生成される IMS 実行時用の制御情報です。オンライン実行時には ACBLIB やカタログ化された ACB が参照されます。定義変更後に ACB が更新されていないと、ソース定義と実行時の動きがずれます

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 上書確認の定義体でアイエムエスの運用確認を行います。ACB の根拠にできる作業はどれですか。

    - A. IMS 15.5と無関係な一覧で上書確認の定義体を確認した扱いにする。
    - B. DFS058I の有無を確認せず上書確認の定義体を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 ✅
    - D. ACB の属性行を読まず上書確認の定義体の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では ACB は「IMS 15.5で ACB の扱いを記録する上書確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では ACB の表示結果と DFS058I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では ACB の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **ACB**

    - 検証目的: 上書確認の定義体について、IMS 15.5 の 定義体で扱う ACB は、DBD と PSB から生成される IMS 実行時用の制御情報です。オンライン実行時には ACBLIB やカタログ化された ACに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、上書確認の定義体の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にACBを指定し、OSKB010007の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND ACB
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM ACB
    CASE OSKB010007
    SOURCE IMS 15.5
    ```

    ACBとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010007を同じ出力で読み、上書確認の定義体の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010007
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010007  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の ACB と OSKB010007 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### DBD {#c16-i0214}
*分類: 定義体*  ・  難易度: 初級

IMS 15.5 の 定義体で扱うDBDは、IMS データベースの構造、セグメント、アクセス方式を記述する定義体です。アプリケーションが実データを読む前提になるため、物理構造や索引の変更時には DBD の整合性が重要です。DBD ライブラリと ACB 生成の関係も確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 置換確認の定義体に関する DBD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. /DISPLAY TRANSACTION OSKB の結果を残さず置換確認の定義体の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の定義体の証跡として保存して根拠にする。
    - C. DBD の変更点を出力本文から切り離して置換確認の定義体の承認欄のみ残す。
    - D. 同じ画面で対象行と DFS058I を読み、置換確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では DBD は「DBD の状態と出力メッセージを結び付ける置換確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では DBD の出力行と DFS058I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では DBD を IMS 15.5の確認記録に残し、対象名は置換確認対象です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **DBD**

    - 検証目的: 置換確認の定義体について、IMS 15.5 の 定義体で扱う DBD は、IMS データベースの構造、セグメント、アクセス方式を記述する定義体です。アプリケーションが実データを読む前提になるため、物理構に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、置換確認の定義体の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にDBDを指定し、OSKB010004の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND DBD
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM DBD
    CASE OSKB010004
    SOURCE IMS 15.5
    ```

    DBDとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010004を同じ出力で読み、置換確認の定義体の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010004
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010004  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の DBD と OSKB010004 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### PCB {#c16-i0215}
*分類: 定義体*  ・  難易度: 中級

IMS 15.5 の 定義体で扱うPCBは、IMS アプリケーションがデータベースやメッセージキューへアクセスするための制御ブロックです。DB PCB と I/O PCB では役割が異なり、呼び出し時に使う PCB を間違えると処理対象も変わります。プログラム障害では PCB マスクとステータスコードを確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 探索確認の定義体で PCB の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PCB の出力を取らず探索確認の定義体の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 ✅
    - C. /DISPLAY TRANSACTION OSKB を省略して探索確認の定義体の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の定義体へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では PCB は「探索確認の定義体に関係する定義値と表示行を照合する探索確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では PCB の属性行と DFS058I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では PCB を IMS 15.5の運用手順で確認し、初出名は探索確認初出です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **PCB**

    - 検証目的: 探索確認の定義体について、IMS 15.5 の 定義体で扱う PCB は、IMS アプリケーションがデータベースやメッセージキューへアクセスするための制御ブロックです。DB PCB と I/O PCBに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、探索確認の定義体の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にPCBを指定し、OSKB010006の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND PCB
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM PCB
    CASE OSKB010006
    SOURCE IMS 15.5
    ```

    PCBとOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010006を同じ出力で読み、探索確認の定義体の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010006
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010006  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の PCB と OSKB010006 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### PSB {#c16-i0216}
*分類: 定義体*  ・  難易度: 初級

IMS 15.5 の 定義体で扱うPSBは、IMS アプリケーションが利用する PCB をまとめたプログラム仕様ブロックです。プログラムがどのデータベースやメッセージキューにアクセスできるかを定義します。権限やデータ構造の問題を調べるときは、PSB と PCB の対応を確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 終端確認の定義体に関係する PSB の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. /DISPLAY TRANSACTION OSKB で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 ✅
    - B. PSB の名称と担当者名のみを残して終端確認の定義体の表示本文を確認対象に含めない。
    - C. アイエムエス以外の画面で終端確認の定義体を確認し同じ証跡として扱ったことにする。
    - D. DFS058I の有無を見ず終端確認の定義体の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では PSB は「PSB の用途をアイエムエスの表示で確認する終端確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IMS 15.5の PSB と DFS058I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では PSB を IMS 15.5で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **PSB**

    - 検証目的: 終端確認の定義体について、IMS 15.5 の 定義体で扱う PSB は、IMS アプリケーションが利用する PCB をまとめたプログラム仕様ブロックです。プログラムがどのデータベースやメッセージキューに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、終端確認の定義体の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にPSBを指定し、OSKB010005の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND PSB
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM PSB
    CASE OSKB010005
    SOURCE IMS 15.5
    ```

    PSBとOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010005を同じ出力で読み、終端確認の定義体の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010005
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010005  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の PSB と OSKB010005 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands




## IMS 15.5 > 接続

### IMS Connect {#c16-i0217}
*分類: 接続*  ・  難易度: 中級

IMS 15.5 の 接続で扱うIMS Connectは、TCP/IP 経由で外部クライアントと IMS トランザクションやデータアクセスをつなぐ機能です。分散アプリケーションから IMS を利用する入口になるため、ポート、セキュリティ、OTMA 連携を確認します。障害時は IMS Connect と IMS 本体の境界を分けて見ます

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 順序確認の接続でアイエムエスの運用確認を行います。IMS Connectの根拠にできる作業はどれですか。

    - A. IMS 15.5と無関係な一覧で順序確認の接続を確認した扱いにする。
    - B. DFS058I の有無を確認せず順序確認の接続を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 ✅
    - D. IMS Connectの属性行を読まず順序確認の接続の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では IMS Connect は「IMS 15.5で IMS Connectの扱いを記録する順序確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では IMS Connectの表示結果と DFS058I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では IMS Connectの使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **IMS Connect**

    - 検証目的: 順序確認の接続について、IMS 15.5 の 接続で扱う IMS Connectは、TCP/IP 経由で外部クライアントと IMS トランザクションやデータアクセスをつなぐ機能です。分散アプリケーシに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、順序確認の接続の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にIMS Connectを指定し、OSKB010015の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND IMS Connect
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM IMS Connect
    CASE OSKB010015
    SOURCE IMS 15.5
    ```

    IMS ConnectとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010015を同じ出力で読み、順序確認の接続の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010015
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010015  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の IMS Connect と OSKB010015 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands




## IMS 15.5 > 運用

### IMS チェックポイント {#c16-i0218}
*分類: 運用*  ・  難易度: 中級

IMS 15.5 の 運用で扱うIMS チェックポイントは、再始動や回復の基準点として処理状態を記録する仕組みです。BMP やオンライン処理では、チェックポイント間隔が回復時間と処理負荷に影響します。長時間処理ではチェックポイント設計を確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 変更確認のチェックポイントに関する IMS チェックポイントの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. /DISPLAY TRANSACTION OSKB の結果を残さず変更確認のチェックポイントの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のチェックポイントの証跡として保存して根拠にする。
    - C. IMS チェックポイントの変更点を出力本文から切り離して変更確認のチェックポイントの承認欄のみ残す。
    - D. IMS 15.5の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では IMS チェックポイント は「IMS チェックポイントの状態と出力メッセージを結び付ける変更確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では IMS チェックポイントの出力行と DFS058I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では IMS チェックポイントを IMS 15.5の確認記録に残し、対象名は変更確認対象です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **IMS チェックポイント**

    - 検証目的: 変更確認のチェックポイントについて、IMS 15.5 の 運用で扱う IMS チェックポイントは、再始動や回復の基準点として処理状態を記録する仕組みです。BMP やオンライン処理では、チェックポイント間隔が回復に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、変更確認のチェックポイントの確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にIMS チェックポイントを指定し、OSKB010020の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND IMS チェックポイント
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM IMS チェックポイント
    CASE OSKB010020
    SOURCE IMS 15.5
    ```

    IMS チェックポイントとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010020を同じ出力で読み、変更確認のチェックポイントの根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010020
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010020  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の IMS チェックポイント と OSKB010020 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands




## IMS 15.5 > 障害診断

### /CHECKPOINT PURGE 実行条件確認 ディスク状態 {#c16-i0219}
*分類: 障害診断*  ・  難易度: 上級

IMS 15.5 の 障害診断 で扱う「/CHECKPOINT PURGE 実行条件確認 ディスク状態」は、DBCTLでBMP完了を待つ停止系チェックポイント操作を実行条件確認の観点で確認する技術項目です。DFS680I 行とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **/CHECKPOINT PURGE 実行条件確認 ディスク状態**

    - 検証目的: 障害診断における/CHECKPOINT PURGEの実行条件確認を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
    DBDNAME=DBD096
    UNLOAD DATA SET WRITTEN
    RETURN CODE = 0000
    ```

    画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、再始動点の誤認を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFSURGL0 HD REORGANIZATION RELOAD UTILITY
    DBDNAME=DBD096
    DATABASE RELOADED
    RETURN CODE = 0000
    ```

    画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /DISPLAY DATABASE DBD096
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS000I DATABASE DBD096 ACCESS UPDATES ALLOWED AFTER RELOAD
    ```

    画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
    ② ステップ2 の DFSURGL0 が画面・出力に表示されること
    ③ ステップ3 の DFS000I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### /CHECKPOINT PURGE 接続確認 オンライン状態 {#c16-i0220}
*分類: 障害診断*  ・  難易度: 中級

IMS 15.5 の 障害診断 で扱う「/CHECKPOINT PURGE 接続確認 オンライン状態」は、DBCTLでBMP完了を待つ停止系チェックポイント操作を接続確認の観点で確認する技術項目です。DFS680I 行とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **/CHECKPOINT PURGE 接続確認 オンライン状態**

    - 検証目的: 障害診断における/CHECKPOINT PURGEの接続確認を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
    DBDNAME=DBD036
    UNLOAD DATA SET WRITTEN
    RETURN CODE = 0000
    ```

    画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFSURGL0 HD REORGANIZATION RELOAD UTILITY
    DBDNAME=DBD036
    DATABASE RELOADED
    RETURN CODE = 0000
    ```

    画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /DISPLAY DATABASE DBD036
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS000I DATABASE DBD036 ACCESS UPDATES ALLOWED AFTER RELOAD
    ```

    画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
    ② ステップ2 の DFSURGL0 が画面・出力に表示されること
    ③ ステップ3 の DFS000I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### DBD catalog reference ログ照合 詳細表示 {#c16-i0221}
*分類: 障害診断*  ・  難易度: 中級

IMS 15.5 の 障害診断 で扱う「DBD catalog reference ログ照合 詳細表示」は、IMS管理ACB環境でDBRCがIMSカタログ上のアクティブDBDを参照する仕組みをログ照合の観点で確認する技術項目です。DFS680I 行とAREA8を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **DBD catalog reference ログ照合 詳細表示**

    - 検証目的: 障害診断におけるDBD catalog referenceのログ照合を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA8
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /CHECKPOINT FREEZE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS994I *CHKPT 82170/085820**FREEZE*
    ```

    画面・出力には DFS994I が含まれ、DFS994Iを確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /NRESTART BUILDQ
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085236
    DFS994I *CHKPT 82170/085820**SIMPLE*
    ```

    画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /DISPLAY ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
    ```

    画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
    ② ステップ2 の DFS058I が画面・出力に表示されること
    ③ ステップ3 の DFS000I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### DBD catalog reference 再始動確認 設定値 {#c16-i0222}
*分類: 障害診断*  ・  難易度: 初級

IMS 15.5 の 障害診断 で扱う「DBD catalog reference 再始動確認 設定値」は、IMS管理ACB環境でDBRCがIMSカタログ上のアクティブDBDを参照する仕組みを再始動確認の観点で確認する技術項目です。DFS680I 行とAREA4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **DBD catalog reference 再始動確認 設定値**

    - 検証目的: 障害診断におけるDBD catalog referenceの再始動確認を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA4
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /CHECKPOINT FREEZE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS994I *CHKPT 82170/085820**FREEZE*
    ```

    画面・出力には DFS994I が含まれ、DFS994Iを確認し、再始動点の誤認を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /NRESTART BUILDQ
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085236
    DFS994I *CHKPT 82170/085820**SIMPLE*
    ```

    画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> /DISPLAY ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
    ```

    画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
    ② ステップ2 の DFS058I が画面・出力に表示されること
    ③ ステップ3 の DFS000I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### DFS680I ログ照合 メッセージ行 {#c16-i0223}
*分類: 障害診断*  ・  難易度: 中級

IMS 15.5 の 障害診断 で扱う「DFS680I ログ照合 メッセージ行」は、再始動で使用するチェックポイントを示すIMSメッセージをログ照合の観点で確認する技術項目です。DFS680I 行とRECON3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **DFS680I ログ照合 メッセージ行**

    - 検証目的: 障害診断におけるDFS680Iのログ照合を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON3
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="HWS1"><typ>IMSCON</typ><alias>IO024</alias><astt>ACTIVE</astt><odbm>ODBM4</odbm><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> UPDATE IMSCON TYPE(ODBM) NAME(ODBM4) START(COMM)
    → Enter を押す
    ```

    画面・出力:
    ```text
    The UPDATE IMSCON TYPE(ODBM) command completed successfully.
    ODBM4  X'00000000'  X'00000000'
    ```

    画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QUERY ODBM SHOW(ALL)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="ODBM4"><typ>ODBM</typ><stt>ACTIVE</stt><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の name= が画面・出力に表示されること
    ② ステップ2 の UPDATE が画面・出力に表示されること
    ③ ステップ3 の name= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### DFS680I 整合確認 停止確認 {#c16-i0224}
*分類: 障害診断*  ・  難易度: 上級

IMS 15.5 の 障害診断 で扱う「DFS680I 整合確認 停止確認」は、再始動で使用するチェックポイントを示すIMSメッセージを整合確認の観点で確認する技術項目です。DFS680I 行とRECON3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **DFS680I 整合確認 停止確認**

    - 検証目的: 障害診断におけるDFS680Iの整合確認を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON3
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="HWS1"><typ>IMSCON</typ><alias>IO084</alias><astt>ACTIVE</astt><odbm>ODBM4</odbm><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> UPDATE IMSCON TYPE(ODBM) NAME(ODBM4) START(COMM)
    → Enter を押す
    ```

    画面・出力:
    ```text
    The UPDATE IMSCON TYPE(ODBM) command completed successfully.
    ODBM4  X'00000000'  X'00000000'
    ```

    画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QUERY ODBM SHOW(ALL)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="ODBM4"><typ>ODBM</typ><stt>ACTIVE</stt><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の name= が画面・出力に表示されること
    ② ステップ2 の UPDATE が画面・出力に表示されること
    ③ ステップ3 の name= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### DFSURDB0 実行条件確認 統計値 {#c16-i0225}
*分類: 障害診断*  ・  難易度: 中級

IMS 15.5 の 障害診断 で扱う「DFSURDB0 実行条件確認 統計値」は、イメージコピーと変更累積、ログを使ってDBDSを復旧するIMSユーティリティを実行条件確認の観点で確認する技術項目です。DFS680I 行とUTIL048を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **DFSURDB0 実行条件確認 統計値**

    - 検証目的: 障害診断におけるDFSURDB0の実行条件確認を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL048
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> BROWSE IMS.BMP.CNTL(PSB048)
    → Enter を押す
    ```

    画面・出力:
    ```text
    EXEC PGM=DFSRRC00,PARM='BMP,PGM048,PSB048,CKPTID=LAST'
    ```

    画面・出力には EXEC が含まれ、EXECを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> FIND IMSLOGR
    → Enter を押す
    ```

    画面・出力:
    ```text
    //IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
    ```

    画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> FIND CHKPT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHKPT ID 82170/085236 FOUND FOR PSB048
    ```

    画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
    ② ステップ2 の IMSLOGR が画面・出力に表示されること
    ③ ステップ3 の CHKPT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### MINVERS 状態確認 整合確認 {#c16-i0226}
*分類: 障害診断*  ・  難易度: 中級

IMS 15.5 の 障害診断 で扱う「MINVERS 状態確認 整合確認」は、RECONデータセットで下位版戻し時のアクセス可否に影響する最小版数値を状態確認の観点で確認する技術項目です。DFS680I 行とPAY060を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities

??? note "検証手順（1件）"
    **MINVERS 状態確認 整合確認**

    - 検証目的: 障害診断におけるMINVERSの状態確認を机上確認する。
    - 前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY060
    - セッション環境: IMS terminal / TSO SPOC / JCL review

    **ステップ 1**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QRY TRAN NAME(PAY060) SHOW(ALL)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="IMS1"><typ>IMS</typ><styp>DBDC</styp><tran>PAY060</tran><status>STARTED</status><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QRY DB NAME(DBD060) SHOW(GLOBAL)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="IMS1"><db>DBD060</db><scope>GLOBAL</scope><status>AVAILABLE</status><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    IMS操作画面
    COMMAND ===> QRY AREA NAME(AREA4) SHOW(ALL)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name="IMS1"><area>AREA4</area><status>AVAILABLE</status><rc>00000000</rc></mbr>
    ```

    画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の name= が画面・出力に表示されること
    ② ステップ2 の name= が画面・出力に表示されること
    ③ ステップ3 の name= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities



### 障害診断 IMSメッセージ診断 ログとの照合 DIAG07 {#c16-i0227}
*分類: 障害診断*  ・  難易度: 上級

ログとの照合では 障害診断 の メンバー照会 を主操作として DIAG07 を判定します。時刻と対象識別子への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG07 に残します。ログとの照合を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG07 へ保存します。主判定のログとの照合では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG07 へ残します。証跡照合のログとの照合では障害診断・メッセージ診断の status と HWSQ2240W を DIAG07 に保存します。記録対応のログとの照合では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG07 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** ログとの照合で 障害診断 の メンバー照会 と IMS Connect警告 を使い 操作とログを対応 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読み対象 DIAG07 を切り分ける確認方法はどれですか。

    - A. statusを含むメンバー照会の応答行を保存する。その応答を得るためQUERY MEMBER TYPE(IMS) SHOW(STATUS)を使用する。対象DIAG07のメッセージIDと理由コードとして記録する。 ✅
    - B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。DFS680Iをstatusと同じ判定値とみなし対象DIAG07の主証跡にする。
    - C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。
    - D. IMSメッセージ診断の停止または再定義を実施する。その後にQUERY MEMBER TYPE(IMS) SHOW(STATUS)でstatusを採取する。

    正解: **A** ／ 難易度: 上級

    **解説:** 適切な判定: Aはメンバー照会で status を読みメッセージIDと理由コードの主値として操作とログを対応しDIAG07に残します。
    機能の仕組み: ログとの照合ではIMS Connect警告を補助操作としIMSメッセージ診断の時刻と対象識別子をHWSQ2240Wと対象DIAG07で照合します。
    各候補の評価: メンバー照会とIMS Connect警告の役割を分けるとA: statusの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではメッセージIDと理由コードを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではメッセージIDと理由コードを証明できない点でメッセージIDと理由コードを確認できません、D: 変更前のメッセージIDと理由コードを失う点でIMS Connect警告の範囲を越えます。結論としてログとの照合の障害診断・メッセージ診断で判定する対象は DIAG07 です。
    用語の定義: ログとの照合で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG07へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 ログとの照合 DIAG07**

    - 検証目的: 障害診断のIMSメッセージ診断について操作とログを対応し、DIAG07のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG07のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG07のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG07
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG07の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の status が画面・出力に表示されること
    ② ステップ2 の HWSQ2240W が画面・出力に表示されること
    ③ ステップ3 の DFS680I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 代替経路の確認 DIAG10 {#c16-i0228}
*分類: 障害診断*  ・  難易度: 上級

代替経路の確認では 障害診断 の メンバー照会 を主操作として DIAG10 を判定します。主経路との役割差への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG10 に残します。代替経路の確認を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG10 へ保存します。主判定の代替経路の確認では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG10 へ残します。証跡照合の代替経路の確認では障害診断・メッセージ診断の status と HWSQ2240W を DIAG10 に保存します。記録対応の代替経路の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG10 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 障害診断 の メンバー照会 と IMS Connect警告 を照合し 主経路との役割差 を確かめます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読む前に対象 DIAG10 へ行う確認はどれですか。

    - A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。
    - B. IMSメッセージ診断の停止または再定義を実施する。その後にQUERY MEMBER TYPE(IMS) SHOW(STATUS)でstatusを採取する。
    - C. DB/DC運用のSTATUSとQUEUEを確認する。その値を障害診断のDIAG10にも適用する。
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)とF HWS1,VIEWPORT ALLの対象名をそろえる。前者のstatusをメッセージIDと理由コードの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正しい判定結果: Dはメンバー照会で status を読みメッセージIDと理由コードの主値として代替手段の成立を確認しDIAG10に残します。
    運用上の背景: 代替経路の確認ではIMS Connect警告を補助操作としIMSメッセージ診断の主経路との役割差をHWSQ2240Wと対象DIAG10で照合します。
    候補別の検討: メンバー照会とIMS Connect警告の役割を分けるとA: 入力記録だけではメッセージIDと理由コードを証明できない点で一次資料と一致しません、B: 変更前のメッセージIDと理由コードを失う点でメッセージIDと理由コードを確認できません、C: DB/DC運用の値ではstatusを確認できない点でIMS Connect警告の範囲を越えます、D: 同じ対象名のstatusを採用する点で現在値を示します。結論として代替経路の確認の障害診断・メッセージ診断で判定する対象は DIAG10 です。
    重要用語の定義: 代替経路の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG10へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 代替経路の確認 DIAG10**

    - 検証目的: 障害診断のIMSメッセージ診断について代替手段の成立を確認し、DIAG10のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG10のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG10のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG10
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG10の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の status が画面・出力に表示されること
    ② ステップ2 の HWSQ2240W が画面・出力に表示されること
    ③ ステップ3 の DFS680I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 変更前の確認 DIAG02 {#c16-i0229}
*分類: 障害診断*  ・  難易度: 上級

変更前の確認では 障害診断 の IMS Connect警告 を主操作として DIAG02 を判定します。変更対象と非対象の境界への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG02 に残します。変更前の確認を補助する 再始動メッセージ では DFS680I を補助値として DIAG02 へ保存します。主判定の変更前の確認では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG02 へ残します。証跡照合の変更前の確認では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG02 に保存します。記録対応の変更前の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG02 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 障害診断 の IMS Connect警告 と 再始動メッセージ を実施し IMSメッセージ診断 の役割を確認します。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG02 の証跡を取る方法はどれですか。

    - A. F HWS1,VIEWPORT ALLを対象名なしで実行する。一覧の先頭行をDIAG02の結果として記録する。
    - B. 前回保存したF HWS1,VIEWPORT ALLの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。
    - C. 保存済みのDIAG02の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象DIAG02についてF HWS1,VIEWPORT ALLの応答からHWSQ2240Wを確認する。/DISPLAY OLDSは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 採用理由: DはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として変更前の証跡を保存しDIAG02に残します。
    動作の背景: 変更前の確認では再始動メッセージを補助操作としIMSメッセージ診断の変更対象と非対象の境界をDFS680Iと対象DIAG02で照合します。
    各選択肢の検討: IMS Connect警告と再始動メッセージの役割を分けるとA: 先頭行はDIAG02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でIMS Connect警告を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で障害診断に使いません、D: HWSQ2240Wと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の障害診断・メッセージ診断で判定する対象は DIAG02 です。
    初出用語の定義: 変更前の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG02へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 変更前の確認 DIAG02**

    - 検証目的: 障害診断のIMSメッセージ診断について変更前の証跡を保存し、DIAG02のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG02のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG02
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG02の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG02のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
    ② ステップ2 の DFS680I が画面・出力に表示されること
    ③ ステップ3 の status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 変更後の確認 DIAG03 {#c16-i0230}
*分類: 障害診断*  ・  難易度: 上級

変更後の確認では 障害診断 の 再始動メッセージ を主操作として DIAG03 を判定します。反映値と残存値への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG03 に残します。変更後の確認を補助する メンバー照会 では status を補助値として DIAG03 へ保存します。主判定の変更後の確認では障害診断・メッセージ診断の 再始動メッセージ から DFS680I を読み DIAG03 へ残します。証跡照合の変更後の確認では障害診断・メッセージ診断の DFS680I と status を DIAG03 に保存します。記録対応の変更後の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG03 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 障害診断 の 再始動メッセージ と メンバー照会 を用い 変更結果を検証 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。DFS680I で対象 DIAG03 の メッセージIDと理由コード を再現できる記録はどれですか。

    - A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)で周辺状態を押さえる。その後に/DISPLAY OLDSでDFS680Iを確認して変更結果を検証する。 ✅
    - B. IMSメッセージ診断の停止または再定義を実施する。その後に/DISPLAY OLDSでDFS680Iを採取する。
    - C. HALDBの区画状態とILDS整合を確認する。その値を障害診断のDIAG03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IMSメッセージ診断の反映値と残存値は確認済みとして扱う。さらにF HWS1,VIEWPORT ALLのHWSQ2240WをDFS680Iと同種の値として併記する。
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が成功したため/DISPLAY OLDSのDFS680Iも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正答の根拠: Aは再始動メッセージで DFS680I を読みメッセージIDと理由コードの主値として変更結果を検証しDIAG03に残します。
    内部の仕組み: 変更後の確認ではメンバー照会を補助操作としIMSメッセージ診断の反映値と残存値をstatusと対象DIAG03で照合します。
    誤答を含む比較: 再始動メッセージとメンバー照会の役割を分けるとA: 周辺状態の後にDFS680Iを確認する点でDIAG03を判定できます、B: 変更前のメッセージIDと理由コードを失う点でメンバー照会の範囲を越えます、C: HALDBの値ではDFS680Iを確認できないうえに追加前提も不正な点でDIAG03の値を示しません、D: 補助操作の成功ではDFS680Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の障害診断・メッセージ診断で判定する対象は DIAG03 です。
    用語定義: 変更後の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG03へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 変更後の確認 DIAG03**

    - 検証目的: 障害診断のIMSメッセージ診断について変更結果を検証し、DIAG03のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG03の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG03のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG03のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG03
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
    ② ステップ2 の status が画面・出力に表示されること
    ③ ステップ3 の HWSQ2240W が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 引継ぎ記録 DIAG09 {#c16-i0231}
*分類: 障害診断*  ・  難易度: 上級

引継ぎ記録では 障害診断 の 再始動メッセージ を主操作として DIAG09 を判定します。次担当者が追跡できる証跡への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG09 に残します。引継ぎ記録を補助する メンバー照会 では status を補助値として DIAG09 へ保存します。主判定の引継ぎ記録では障害診断・メッセージ診断の 再始動メッセージ から DFS680I を読み DIAG09 へ残します。証跡照合の引継ぎ記録では障害診断・メッセージ診断の DFS680I と status を DIAG09 に保存します。記録対応の引継ぎ記録では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG09 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 障害診断 の 再始動メッセージ と メンバー照会 を用い 再現可能な記録を作成 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。DFS680I で対象 DIAG09 の メッセージIDと理由コード を再現できる記録はどれですか。

    - A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が成功したため/DISPLAY OLDSのDFS680Iも正常だと推定する。主出力は保存しない。
    - B. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をDIAG09の結果として記録する。
    - C. 対象名DIAG09を指定して/DISPLAY OLDSを実行する。応答中のDFS680Iと時刻を保存する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)で周辺状態を補完する。 ✅
    - D. 前回保存した/DISPLAY OLDSの結果を使う。今回のQUERY MEMBER TYPE(IMS) SHOW(STATUS)の結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 上級

    **解説:** 採用操作の理由: Cは再始動メッセージで DFS680I を読みメッセージIDと理由コードの主値として再現可能な記録を作成しDIAG09に残します。
    製品内の仕組み: 引継ぎ記録ではメンバー照会を補助操作としIMSメッセージ診断の次担当者が追跡できる証跡をstatusと対象DIAG09で照合します。
    選択肢別の説明: 再始動メッセージとメンバー照会の役割を分けるとA: 補助操作の成功ではDFS680Iを確定できない点でDIAG09の値を示しません、B: 先頭行はDIAG09と確定できない点で引継ぎ記録に合いません、C: DFS680Iと時刻を保存する点で再始動メッセージに合います、D: 採取時刻が異なる点で障害診断に使いません。結論として引継ぎ記録の障害診断・メッセージ診断で判定する対象は DIAG09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG09へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 引継ぎ記録 DIAG09**

    - 検証目的: 障害診断のIMSメッセージ診断について再現可能な記録を作成し、DIAG09のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG09の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG09のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG09のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG09
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
    ② ステップ2 の status が画面・出力に表示されること
    ③ ステップ3 の HWSQ2240W が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 復旧後の確認 DIAG06 {#c16-i0232}
*分類: 障害診断*  ・  難易度: 上級

復旧後の確認では 障害診断 の 再始動メッセージ を主操作として DIAG06 を判定します。再発していないことを示す値への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG06 に残します。復旧後の確認を補助する メンバー照会 では status を補助値として DIAG06 へ保存します。主判定の復旧後の確認では障害診断・メッセージ診断の 再始動メッセージ から DFS680I を読み DIAG06 へ残します。証跡照合の復旧後の確認では障害診断・メッセージ診断の DFS680I と status を DIAG06 に保存します。記録対応の復旧後の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG06 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 障害診断 の 再始動メッセージ と メンバー照会 の役割を分け 再発していないことを示す値 を調べます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG06 を誤判定しない進め方はどれですか。

    - A. ODBM/OMのALIASと到達状態を確認する。その値を障害診断のDIAG06にも適用する。
    - B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が成功したため/DISPLAY OLDSのDFS680Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象DIAG06へ引き継げるものとする。
    - C. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をDIAG06の結果として記録する。
    - D. /DISPLAY OLDSでDFS680Iを取得してからF HWS1,VIEWPORT ALLでHWSQ2240Wを照合する。DIAG06のメッセージIDと理由コードを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正答内容: Dは再始動メッセージで DFS680I を読みメッセージIDと理由コードの主値として復旧後の安定性を確認しDIAG06に残します。
    構成上の背景: 復旧後の確認ではメンバー照会を補助操作としIMSメッセージ診断の再発していないことを示す値をstatusと対象DIAG06で照合します。
    候補ごとの理由: 再始動メッセージとメンバー照会の役割を分けるとA: ODBM/OMの値ではDFS680Iを確認できない点でメンバー照会の範囲を越えます、B: 補助操作の成功ではDFS680Iを確定できないうえに追加前提も不正な点でDIAG06の値を示しません、C: 先頭行はDIAG06と確定できない点で復旧後の確認に合いません、D: DFS680IとHWSQ2240Wを順に照合する点で再始動メッセージに合います。結論として復旧後の確認の障害診断・メッセージ診断で判定する対象は DIAG06 です。
    初出用語: 復旧後の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG06へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 復旧後の確認 DIAG06**

    - 検証目的: 障害診断のIMSメッセージ診断について復旧後の安定性を確認し、DIAG06のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG06の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG06のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG06のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG06
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
    ② ステップ2 の status が画面・出力に表示されること
    ③ ステップ3 の HWSQ2240W が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 復旧準備 DIAG05 {#c16-i0233}
*分類: 障害診断*  ・  難易度: 上級

復旧準備では 障害診断 の IMS Connect警告 を主操作として DIAG05 を判定します。再開前に必要な整合性への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG05 に残します。復旧準備を補助する 再始動メッセージ では DFS680I を補助値として DIAG05 へ保存します。主判定の復旧準備では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG05 へ残します。証跡照合の復旧準備では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG05 に保存します。記録対応の復旧準備では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG05 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 復旧準備で 障害診断 の IMS Connect警告 と 再始動メッセージ を組み合わせる際は IMSメッセージ診断 がDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用という仕組みを前提にします。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。HWSQ2240W と メッセージIDと理由コード を対象 DIAG05 で確認する組合せはどれですか。

    - A. 前回保存したF HWS1,VIEWPORT ALLの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。
    - B. 保存済みのDIAG05の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。
    - C. 変更を加えずF HWS1,VIEWPORT ALLを実行する。HWSQ2240Wを保存する。差分は/DISPLAY OLDSの結果と対象名で対応させる。 ✅
    - D. /DISPLAY OLDSのDFS680IをメッセージIDと理由コードの主判定に採用する。F HWS1,VIEWPORT ALLの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: CはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として復旧条件を確認しDIAG05に残します。
    処理の仕組み: 復旧準備では再始動メッセージを補助操作としIMSメッセージ診断の再開前に必要な整合性をDFS680Iと対象DIAG05で照合します。
    選択結果の内訳: IMS Connect警告と再始動メッセージの役割を分けるとA: 採取時刻が異なる点でIMS Connect警告を代替しません、B: 過去出力では今回の復旧準備を示せない点で障害診断に使いません、C: 変更前のHWSQ2240Wを保存する点で正答です、D: DFS680IはHWSQ2240Wを代替しないうえに追加前提も不正な点でDIAG05を採用できません。結論として復旧準備の障害診断・メッセージ診断で判定する対象は DIAG05 です。
    用語の説明: 復旧準備で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG05へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 復旧準備 DIAG05**

    - 検証目的: 障害診断のIMSメッセージ診断について復旧条件を確認し、DIAG05のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG05のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG05
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG05の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG05のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
    ② ステップ2 の DFS680I が画面・出力に表示されること
    ③ ステップ3 の status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 構成監査 DIAG08 {#c16-i0234}
*分類: 障害診断*  ・  難易度: 上級

構成監査では 障害診断 の IMS Connect警告 を主操作として DIAG08 を判定します。定義値と稼働値の一致への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG08 に残します。構成監査を補助する 再始動メッセージ では DFS680I を補助値として DIAG08 へ保存します。主判定の構成監査では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG08 へ残します。証跡照合の構成監査では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG08 に保存します。記録対応の構成監査では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG08 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 構成監査で 障害診断 の IMS Connect警告 と 再始動メッセージ を実施し IMSメッセージ診断 の役割を確認します。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG08 の証跡を取る方法はどれですか。

    - A. 保存済みのDIAG08の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。
    - B. /DISPLAY OLDSの結果だけでは確定しない。F HWS1,VIEWPORT ALLのHWSQ2240Wを主証跡として構成差分を監査する。 ✅
    - C. /DISPLAY OLDSのDFS680IをメッセージIDと理由コードの主判定に採用する。F HWS1,VIEWPORT ALLの応答は採取対象から外す。
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusをHWSQ2240Wと同義の成功表示として扱う。F HWS1,VIEWPORT ALLは実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: BはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として構成差分を監査しDIAG08に残します。
    実行時の背景: 構成監査では再始動メッセージを補助操作としIMSメッセージ診断の定義値と稼働値の一致をDFS680Iと対象DIAG08で照合します。
    四つの候補の理由: IMS Connect警告と再始動メッセージの役割を分けるとA: 過去出力では今回の構成監査を示せない点で障害診断に使いません、B: HWSQ2240Wを主証跡として区別する点で正答です、C: DFS680IはHWSQ2240Wを代替しない点でDIAG08を採用できません、D: statusとHWSQ2240Wは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の障害診断・メッセージ診断で判定する対象は DIAG08 です。
    初出語定義: 構成監査で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG08へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 構成監査 DIAG08**

    - 検証目的: 障害診断のIMSメッセージ診断について構成差分を監査し、DIAG08のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG08のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG08
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG08の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG08のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
    ② ステップ2 の DFS680I が画面・出力に表示されること
    ③ ステップ3 の status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 通常状態の確認 DIAG01 {#c16-i0235}
*分類: 障害診断*  ・  難易度: 上級

通常状態の確認では 障害診断 の メンバー照会 を主操作として DIAG01 を判定します。基準値と現在値の差への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG01 に残します。通常状態の確認を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG01 へ保存します。主判定の通常状態の確認では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG01 へ残します。証跡照合の通常状態の確認では障害診断・メッセージ診断の status と HWSQ2240W を DIAG01 に保存します。記録対応の通常状態の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG01 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 障害診断 の メンバー照会 と IMS Connect警告 を使い 通常状態を確定 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読み対象 DIAG01 を切り分ける確認方法はどれですか。

    - A. F HWS1,VIEWPORT ALLのHWSQ2240WをメッセージIDと理由コードの主判定に採用する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. /DISPLAY OLDSのDFS680Iをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。
    - C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)を先に実行する。対象DIAG01のstatusをメッセージIDと理由コードとして記録する。続いてF HWS1,VIEWPORT ALLで同一対象を照合する。 ✅
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cはメンバー照会で status を読みメッセージIDと理由コードの主値として通常状態を確定しDIAG01に残します。
    背景・仕組み: 通常状態の確認ではIMS Connect警告を補助操作としIMSメッセージ診断の基準値と現在値の差をHWSQ2240Wと対象DIAG01で照合します。
    選択肢の理由: メンバー照会とIMS Connect警告の役割を分けるとA: HWSQ2240Wはstatusを代替しないうえに追加前提も不正な点でIMSメッセージ診断に使えません、B: DFS680Iとstatusは確認項目が異なる点でDIAG01を採用できません、C: statusを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではメッセージIDと理由コードを判定できない点で一次資料と一致しません。結論として通常状態の確認の障害診断・メッセージ診断で判定する対象は DIAG01 です。
    用語の初出定義: 通常状態の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG01へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 通常状態の確認 DIAG01**

    - 検証目的: 障害診断のIMSメッセージ診断について通常状態を確定し、DIAG01のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG01のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG01のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG01
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG01の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の status が画面・出力に表示されること
    ② ステップ2 の HWSQ2240W が画面・出力に表示されること
    ③ ステップ3 の DFS680I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 障害切り分け DIAG04 {#c16-i0236}
*分類: 障害診断*  ・  難易度: 上級

障害切り分けでは 障害診断 の メンバー照会 を主操作として DIAG04 を判定します。最初に失敗した処理への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG04 に残します。障害切り分けを補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG04 へ保存します。主判定の障害切り分けでは障害診断・メッセージ診断の メンバー照会 から status を読み DIAG04 へ残します。証跡照合の障害切り分けでは障害診断・メッセージ診断の status と HWSQ2240W を DIAG04 に保存します。記録対応の障害切り分けでは障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG04 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 障害診断 の メンバー照会 と IMS Connect警告 を照合し 最初に失敗した処理 を確かめます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読む前に対象 DIAG04 へ行う確認はどれですか。

    - A. /DISPLAY OLDSのDFS680Iをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)の出力でDIAG04とstatusが同じ応答にあることを確認する。メッセージIDと理由コードをその応答から採取する。 ✅
    - C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bはメンバー照会で status を読みメッセージIDと理由コードの主値として障害範囲を限定しDIAG04に残します。
    技術的背景: 障害切り分けではIMS Connect警告を補助操作としIMSメッセージ診断の最初に失敗した処理をHWSQ2240Wと対象DIAG04で照合します。
    四択の評価: メンバー照会とIMS Connect警告の役割を分けるとA: DFS680Iとstatusは確認項目が異なるうえに追加前提も不正な点でDIAG04を採用できません、B: DIAG04とstatusを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではメッセージIDと理由コードを判定できない点で一次資料と一致しません、D: 入力記録だけではメッセージIDと理由コードを証明できない点でメッセージIDと理由コードを確認できません。結論として障害切り分けの障害診断・メッセージ診断で判定する対象は DIAG04 です。
    初出語の意味: 障害切り分けで使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG04へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 障害切り分け DIAG04**

    - 検証目的: 障害診断のIMSメッセージ診断について障害範囲を限定し、DIAG04のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG04のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG04のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG04
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG04の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の status が画面・出力に表示されること
    ② ステップ2 の HWSQ2240W が画面・出力に表示されること
    ③ ステップ3 の DFS680I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages




## IMS 15.5 > 領域

### BMP 領域 {#c16-i0237}
*分類: 領域*  ・  難易度: 中級

IMS 15.5 の 領域で扱うBMP 領域は、バッチ処理で IMS データベースやメッセージキューへアクセスする従属領域です。オンライン稼働中のデータと整合させながらバッチ処理できる点が特徴です。排他、チェックポイント、再始動の設計が重要になります

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 区切確認の領域で BMP 領域の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BMP 領域の出力を取らず区切確認の領域の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 ✅
    - C. /DISPLAY TRANSACTION OSKB を省略して区切確認の領域の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の領域へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では BMP 領域 は「区切確認の領域に関係する定義値と表示行を照合する区切確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では BMP 領域の属性行と DFS058I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では BMP 領域を IMS 15.5の運用手順で確認し、初出名は区切確認初出です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **BMP 領域**

    - 検証目的: 区切確認の領域について、IMS 15.5 の 領域で扱う BMP 領域は、バッチ処理で IMS データベースやメッセージキューへアクセスする従属領域です。オンライン稼働中のデータと整合させながらバッに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、区切確認の領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にBMP 領域を指定し、OSKB010010の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND BMP 領域
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM BMP 領域
    CASE OSKB010010
    SOURCE IMS 15.5
    ```

    BMP 領域とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010010を同じ出力で読み、区切確認の領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010010
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010010  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の BMP 領域 と OSKB010010 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### IFP 領域 {#c16-i0238}
*分類: 領域*  ・  難易度: 上級

IMS 15.5 の 領域で扱うIFP 領域は、Fast Path 処理向けの IMS 従属領域です。高頻度で短いトランザクションを効率よく処理する用途で使われます。Fast Path データベースやルーティングの設計と合わせて確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 範囲確認の領域でアイエムエスの運用確認を行います。IFP 領域の根拠にできる作業はどれですか。

    - A. IMS 15.5と無関係な一覧で範囲確認の領域を確認した扱いにする。
    - B. DFS058I の有無を確認せず範囲確認の領域を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 ✅
    - D. IFP 領域の属性行を読まず範囲確認の領域の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では IFP 領域 は「IMS 15.5で IFP 領域の扱いを記録する範囲確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では IFP 領域の表示結果と DFS058I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では IFP 領域の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **IFP 領域**

    - 検証目的: 範囲確認の領域について、IMS 15.5 の 領域で扱う IFP 領域は、Fast Path 処理向けの IMS 従属領域です。高頻度で短いトランザクションを効率よく処理する用途で使われます。Fasに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、範囲確認の領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にIFP 領域を指定し、OSKB010011の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND IFP 領域
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM IFP 領域
    CASE OSKB010011
    SOURCE IMS 15.5
    ```

    IFP 領域とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010011を同じ出力で読み、範囲確認の領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010011
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010011  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の IFP 領域 と OSKB010011 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### MPP 領域 {#c16-i0239}
*分類: 領域*  ・  難易度: 中級

IMS 15.5 の 領域で扱うMPP 領域は、メッセージ処理プログラムを実行する IMS の従属領域です。入力メッセージを受けて短時間のトランザクション処理を行う用途に向きます。処理遅延では、スケジューリング、キュー滞留、異常終了の有無を確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 条件確認の領域に関係する MPP 領域の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 ✅
    - B. MPP 領域の名称と担当者名のみを残して条件確認の領域の表示本文を確認対象に含めない。
    - C. アイエムエス以外の画面で条件確認の領域を確認し同じ証跡として扱ったことにする。
    - D. DFS058I の有無を見ず条件確認の領域の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では MPP 領域 は「MPP 領域の用途をアイエムエスの表示で確認する条件確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IMS 15.5の MPP 領域と DFS058I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では MPP 領域を IMS 15.5で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **MPP 領域**

    - 検証目的: 条件確認の領域について、IMS 15.5 の 領域で扱う MPP 領域は、メッセージ処理プログラムを実行する IMS の従属領域です。入力メッセージを受けて短時間のトランザクション処理を行う用途に向に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、条件確認の領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にMPP 領域を指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND MPP 領域
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM MPP 領域
    CASE OSKB010009
    SOURCE IMS 15.5
    ```

    MPP 領域とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010009を同じ出力で読み、条件確認の領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010009
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010009  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の MPP 領域 と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### 制御領域 {#c16-i0240}
*分類: 領域*  ・  難易度: 初級

IMS 15.5 の 領域で扱う制御領域は、IMS 全体の制御と共通機能を担う中核のアドレス空間です。従属領域や通信、DBRC などの周辺機能と連携して処理を進めます。起動失敗や停止時は、制御領域のメッセージを最初に確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 出力確認の制御領域に関する制御領域の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. /DISPLAY TRANSACTION OSKB の結果を残さず出力確認の制御領域の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の制御領域の証跡として保存して根拠にする。
    - C. 制御領域の変更点を出力本文から切り離して出力確認の制御領域の承認欄のみ残す。
    - D. IMS 15.5の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では制御領域は「制御領域の状態と出力メッセージを結び付ける出力確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では制御領域の出力行と DFS058I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では制御領域を IMS 15.5の確認記録に残し、対象名は出力確認対象です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **制御領域**

    - 検証目的: 出力確認の制御領域について、IMS 15.5 の 領域で扱う制御領域は、IMS 全体の制御と共通機能を担う中核のアドレス空間です。従属領域や通信、DBRC などの周辺機能と連携して処理を進めます。起動に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、出力確認の制御領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄に制御領域を指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND 制御領域
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM 制御領域
    CASE OSKB010008
    SOURCE IMS 15.5
    ```

    制御領域とOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010008を同じ出力で読み、出力確認の制御領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010008
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010008  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の 制御領域 と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands


