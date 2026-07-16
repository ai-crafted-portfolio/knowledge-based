---
search:
  exclude: true
---

# Db2 for z/OS — 詳細 (5/7)

[← Db2 for z/OS の概要へ戻る](index.md)


## Db2 for z/OS > ユーティリティ制御文オプション > DSNUTILBオプション

### DISCARDS {#c07-i0306}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

DISCARDSは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **DISCARDS**

    - 検証目的: 値域整理のオプションについて、DISCARDS は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、値域整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDISCARDSを指定し、OSKB020116の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DISCARDS
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DISCARDS
    CASE OSKB020116
    SOURCE Db2 for z/OS
    ```

    DISCARDSとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020116を同じ出力で読み、値域整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020116
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020116
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020116
    ```

    DSNV401IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DISCARDS と OSKB020116 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### DISP {#c07-i0307}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

DISPは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **DISP**

    - 検証目的: 区切整理のオプションについて、DISP は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、区切整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDISPを指定し、OSKB020110の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DISP
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DISP
    CASE OSKB020110
    SOURCE Db2 for z/OS
    ```

    DISPとOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020110を同じ出力で読み、区切整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020110
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020110
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020110
    ```

    DSNV401IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DISP と OSKB020110 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### DSN {#c07-i0308}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

DSNは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **DSN**

    - 検証目的: 上書整理のオプションについて、DSN は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、上書整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNを指定し、OSKB020107の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSN
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSN
    CASE OSKB020107
    SOURCE Db2 for z/OS
    ```

    DSNとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020107を同じ出力で読み、上書整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020107
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020107
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020107
    ```

    DSNV401IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSN と OSKB020107 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### ENFORCE {#c07-i0309}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

ENFORCEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **ENFORCE**

    - 検証目的: 順序整理のオプションについて、ENFORCE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、順序整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にENFORCEを指定し、OSKB020115の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND ENFORCE
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM ENFORCE
    CASE OSKB020115
    SOURCE Db2 for z/OS
    ```

    ENFORCEとOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020115を同じ出力で読み、順序整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020115
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020115
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020115
    ```

    DSNV401IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の ENFORCE と OSKB020115 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### EXCLUDE {#c07-i0310}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

EXCLUDEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **EXCLUDE**

    - 検証目的: 探索整理のオプションについて、EXCLUDE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020106の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、探索整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にEXCLUDEを指定し、OSKB020106の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND EXCLUDE
    CASE OSKB020106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM EXCLUDE
    CASE OSKB020106
    SOURCE Db2 for z/OS
    ```

    EXCLUDEとOSKB020106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020106を同じ出力で読み、探索整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020106
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020106
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020106
    ```

    DSNV401IとOSKB020106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の EXCLUDE と OSKB020106 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### FREQVAL {#c07-i0311}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

FREQVALは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **FREQVAL**

    - 検証目的: 監査整理のオプションについて、FREQVAL は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、監査整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にFREQVALを指定し、OSKB020119の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND FREQVAL
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM FREQVAL
    CASE OSKB020119
    SOURCE Db2 for z/OS
    ```

    FREQVALとOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020119を同じ出力で読み、監査整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020119
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020119
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020119
    ```

    DSNV401IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の FREQVAL と OSKB020119 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### FROMCOPY {#c07-i0312}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

FROMCOPYは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **FROMCOPY**

    - 検証目的: 置換記録のオプションについて、FROMCOPY は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020124の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、置換記録のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にFROMCOPYを指定し、OSKB020124の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND FROMCOPY
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM FROMCOPY
    CASE OSKB020124
    SOURCE Db2 for z/OS
    ```

    FROMCOPYとOSKB020124が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020124を同じ出力で読み、置換記録のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020124
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020124
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020124
    ```

    DSNV401IとOSKB020124が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の FROMCOPY と OSKB020124 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### HISTOGRAM {#c07-i0313}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

HISTOGRAMは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **HISTOGRAM**

    - 検証目的: 変更整理のオプションについて、HISTOGRAM は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、変更整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にHISTOGRAMを指定し、OSKB020120の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND HISTOGRAM
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM HISTOGRAM
    CASE OSKB020120
    SOURCE Db2 for z/OS
    ```

    HISTOGRAMとOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020120を同じ出力で読み、変更整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020120
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020120
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020120
    ```

    DSNV401IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の HISTOGRAM と OSKB020120 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### INCLUDE {#c07-i0314}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

INCLUDEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **INCLUDE**

    - 検証目的: 終端整理のオプションについて、INCLUDE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020105の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、終端整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にINCLUDEを指定し、OSKB020105の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND INCLUDE
    CASE OSKB020105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM INCLUDE
    CASE OSKB020105
    SOURCE Db2 for z/OS
    ```

    INCLUDEとOSKB020105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020105を同じ出力で読み、終端整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020105
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020105
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020105
    ```

    DSNV401IとOSKB020105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の INCLUDE と OSKB020105 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### KEYCARD {#c07-i0315}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

KEYCARDは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **KEYCARD**

    - 検証目的: 復旧整理のオプションについて、KEYCARD は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、復旧整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にKEYCARDを指定し、OSKB020118の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND KEYCARD
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM KEYCARD
    CASE OSKB020118
    SOURCE Db2 for z/OS
    ```

    KEYCARDとOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020118を同じ出力で読み、復旧整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020118
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020118
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020118
    ```

    DSNV401IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の KEYCARD と OSKB020118 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### LISTDEF {#c07-i0316}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

LISTDEFは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810


### LOG {#c07-i0317}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

LOGは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **LOG**

    - 検証目的: 比較整理のオプションについて、LOG は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、比較整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にLOGを指定し、OSKB020114の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND LOG
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM LOG
    CASE OSKB020114
    SOURCE Db2 for z/OS
    ```

    LOGとOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020114を同じ出力で読み、比較整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020114
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020114
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020114
    ```

    DSNV401IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の LOG と OSKB020114 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### LOGONLY {#c07-i0318}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

LOGONLYは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **LOGONLY**

    - 検証目的: 探索記録のオプションについて、LOGONLY は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020126の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、探索記録のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にLOGONLYを指定し、OSKB020126の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND LOGONLY
    CASE OSKB020126
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM LOGONLY
    CASE OSKB020126
    SOURCE Db2 for z/OS
    ```

    LOGONLYとOSKB020126が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020126を同じ出力で読み、探索記録のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020126
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020126
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020126
    ```

    DSNV401IとOSKB020126が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の LOGONLY と OSKB020126 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020126 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### OPTIONS TEMPLATEDD {#c07-i0319}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

OPTIONS TEMPLATEDDは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います

**出典:** Db2_zOS_Utility_Guide p.810


### RECOVERYDDN {#c07-i0320}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

RECOVERYDDNは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? question "確認問題（4問）"
    **問題.** 回復用データ定義名を保守計画で確認します。Db2の作業記録に回復データ定義名の根拠を残します。夜間保守の事前レビューで、対象と戻し方を運用記録へ残します。どのユーティリティまたは証跡を中心に確認しますか。確認時はコピー履歴カタログのDSNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。

    - A. MODIFY RECOVERY
    - B. RECOVERYDDN ✅
    - C. OPTIONS
    - D. SYSIBM.SYSINDEXPART

    正解: **B** ／ 難易度: 上級

    **解説:** 論点回復用データ定義名は、回復で使うコピー入力を指定することを目的に扱い、確認項目は回復用データ定義名保守です。背景回復用データ定義名として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は回復用データ定義名棚卸です。回復用データ定義名の仕組みは、コピー履歴カタログのDSNAME列と実行ログを照合する理由が回復用データ定義名観点です。A: 回復用データ定義名で見る回復履歴の削除は代替にならず、今回の比較対象から外す理由は回復用データ定義名判断です。B: 回復用データ定義名が正答です。カタログ登録と実データセットを確認することに合うため、採否を決める説明軸は回復用データ定義名定義です。C: 回復用データ定義名で見る実行共通指定は代替にならず、今回の比較対象から外す理由は回復用データ定義名根拠です。D: 回復用データ定義名で見る索引パート状態表は代替にならず、今回の比較対象から外す理由は回復用データ定義名列確認です。初出語回復用データ定義名とは、技術項目名 RECOVERYDDN で表すDb2ユーティリティ、指定、または記録名であり、用語定義は回復用データ定義名根拠です。

    **出典:** Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting

    ---

    **問題.** 回復用データ定義名を障害復旧で確認します。Db2の作業記録に回復データ定義名の根拠を残します。回復判断の前に、コピー履歴と制限状態を突き合わせます。どの項目を根拠にするのが適切ですか。確認時はコピー履歴カタログのDSNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。

    - A. DSNUTILB
    - B. SYSIBM.SYSTABLESPACE
    - C. RECOVERYDDN ✅
    - D. LOAD REPLACE

    正解: **C** ／ 難易度: 上級

    **解説:** 論点回復用データ定義名は、回復で使うコピー入力を指定することを目的に扱い、確認項目は回復用データ定義名判断です。背景回復用データ定義名として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は回復用データ定義名定義です。回復用データ定義名の仕組みは、コピー履歴カタログのDSNAME列と実行ログを照合する理由が回復用データ定義名根拠です。A: 回復用データ定義名で見るユーティリティ制御プログラムは代替にならず、今回の比較対象から外す理由は回復用データ定義名保守です。B: 回復用データ定義名で見る表スペース状態表は代替にならず、今回の比較対象から外す理由は回復用データ定義名棚卸です。C: 回復用データ定義名が正答です。カタログ登録と実データセットを確認することに合うため、採否を決める説明軸は回復用データ定義名観点です。D: 回復用データ定義名で見る置換ロードは代替にならず、今回の比較対象から外す理由は回復用データ定義名証跡です。初出語回復用データ定義名とは、技術項目名 RECOVERYDDN で表すDb2ユーティリティ、指定、または記録名であり、用語定義は回復用データ定義名観点です。

    **出典:** Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting

    ---

    **問題.** 回復用データ定義名を性能維持で確認します。Db2の作業記録に回復データ定義名の根拠を残します。統計と再編成の結果を見て、後続の再バインド要否を整理します。どの指定またはカタログが目的に合いますか。確認時はコピー履歴カタログのDSNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。

    - A. OPTIONS
    - B. REORG TABLESPACE
    - C. REPAIR SET
    - D. RECOVERYDDN ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 論点回復用データ定義名は、回復で使うコピー入力を指定することを目的に扱い、確認項目は回復用データ定義名保守です。背景回復用データ定義名として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は回復用データ定義名棚卸です。回復用データ定義名の仕組みは、コピー履歴カタログのDSNAME列と実行ログを照合する理由が回復用データ定義名観点です。A: 回復用データ定義名で見る実行共通指定は代替にならず、今回の比較対象から外す理由は回復用データ定義名判断です。B: 回復用データ定義名で見る表スペース再編成は代替にならず、今回の比較対象から外す理由は回復用データ定義名定義です。C: 回復用データ定義名で見る制限状態の補修は代替にならず、今回の比較対象から外す理由は回復用データ定義名根拠です。D: 回復用データ定義名が正答です。カタログ登録と実データセットを確認することに合うため、採否を決める説明軸は回復用データ定義名列確認です。初出語回復用データ定義名とは、技術項目名 RECOVERYDDN で表すDb2ユーティリティ、指定、または記録名であり、用語定義は回復用データ定義名根拠です。

    **出典:** Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting

    ---

    **問題.** 回復用データ定義名を監査証跡で確認します。Db2の作業記録に回復データ定義名の根拠を残します。作業後に、実行入力とカタログ上の結果が一致することを確認します。どの名前を証跡として残しますか。確認時はコピー履歴カタログのDSNAME列も照合対象にします。この条件で、どの選択肢が適切ですか。

    - A. RECOVERYDDN ✅
    - B. FLASHCOPY
    - C. CHECK DATA
    - D. RUNSTATS

    正解: **A** ／ 難易度: 上級

    **解説:** 論点回復用データ定義名は、回復で使うコピー入力を指定することを目的に扱い、確認項目は回復用データ定義名判断です。背景回復用データ定義名として、Db2ユーティリティの入力、出力、カタログ記録を結ぶ証跡名は回復用データ定義名定義です。回復用データ定義名の仕組みは、コピー履歴カタログのDSNAME列と実行ログを照合する理由が回復用データ定義名根拠です。A: 回復用データ定義名が正答です。カタログ登録と実データセットを確認することに合うため、採否を決める説明軸は回復用データ定義名保守です。B: 回復用データ定義名で見るストレージコピーは代替にならず、今回の比較対象から外す理由は回復用データ定義名棚卸です。C: 回復用データ定義名で見る参照整合性検査は代替にならず、今回の比較対象から外す理由は回復用データ定義名観点です。D: 回復用データ定義名で見る統計収集は代替にならず、今回の比較対象から外す理由は回復用データ定義名証跡です。初出語回復用データ定義名とは、技術項目名 RECOVERYDDN で表すDb2ユーティリティ、指定、または記録名であり、用語定義は回復用データ定義名観点です。

    **出典:** Db2_zOS_Utility_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **RECOVERYDDN**

    - 検証目的: 優先整理のオプションについて、RECOVERYDDN は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、優先整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にRECOVERYDDNを指定し、OSKB020112の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND RECOVERYDDN
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM RECOVERYDDN
    CASE OSKB020112
    SOURCE Db2 for z/OS
    ```

    RECOVERYDDNとOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020112を同じ出力で読み、優先整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020112
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020112
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020112
    ```

    DSNV401IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の RECOVERYDDN と OSKB020112 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### REPLACE {#c07-i0321}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

REPLACEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **REPLACE**

    - 検証目的: 記録整理のオプションについて、REPLACE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、記録整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にREPLACEを指定し、OSKB020113の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND REPLACE
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM REPLACE
    CASE OSKB020113
    SOURCE Db2 for z/OS
    ```

    REPLACEとOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020113を同じ出力で読み、記録整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020113
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020113
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020113
    ```

    DSNV401IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の REPLACE と OSKB020113 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### REPORT {#c07-i0322}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

REPORTは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **REPORT**

    - 検証目的: 展開記録のオプションについて、REPORT は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020122の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、展開記録のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にREPORTを指定し、OSKB020122の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND REPORT
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM REPORT
    CASE OSKB020122
    SOURCE Db2 for z/OS
    ```

    REPORTとOSKB020122が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020122を同じ出力で読み、展開記録のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020122
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020122
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020122
    ```

    DSNV401IとOSKB020122が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の REPORT と OSKB020122 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### RESTOREBEFORE {#c07-i0323}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

RESTOREBEFOREは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **RESTOREBEFORE**

    - 検証目的: 終端記録のオプションについて、RESTOREBEFORE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱いまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020125の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、終端記録のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にRESTOREBEFOREを指定し、OSKB020125の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND RESTOREBEFORE
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM RESTOREBEFORE
    CASE OSKB020125
    SOURCE Db2 for z/OS
    ```

    RESTOREBEFOREとOSKB020125が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020125を同じ出力で読み、終端記録のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020125
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020125
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020125
    ```

    DSNV401IとOSKB020125が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の RESTOREBEFORE と OSKB020125 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### RESUME {#c07-i0324}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

RESUMEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810


### SHRLEVEL {#c07-i0325}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

SHRLEVELは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810


### SORTKEYS {#c07-i0326}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

SORTKEYSは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **SORTKEYS**

    - 検証目的: 警告整理のオプションについて、SORTKEYS は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、警告整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSORTKEYSを指定し、OSKB020117の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SORTKEYS
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SORTKEYS
    CASE OSKB020117
    SOURCE Db2 for z/OS
    ```

    SORTKEYSとOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020117を同じ出力で読み、警告整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020117
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020117
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020117
    ```

    DSNV401IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SORTKEYS と OSKB020117 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### SPACE {#c07-i0327}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

SPACEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **SPACE**

    - 検証目的: 条件整理のオプションについて、SPACE は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点ではに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020109の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、条件整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSPACEを指定し、OSKB020109の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SPACE
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SPACE
    CASE OSKB020109
    SOURCE Db2 for z/OS
    ```

    SPACEとOSKB020109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020109を同じ出力で読み、条件整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020109
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020109
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020109
    ```

    DSNV401IとOSKB020109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SPACE と OSKB020109 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### STATISTICS {#c07-i0328}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

STATISTICSは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810


### TEMPLATE {#c07-i0329}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

TEMPLATEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います

**出典:** Db2_zOS_Utility_Guide p.810


### TOLOGPOINT {#c07-i0330}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

TOLOGPOINTは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **TOLOGPOINT**

    - 検証目的: 呼出記録のオプションについて、TOLOGPOINT は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020123の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、呼出記録のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にTOLOGPOINTを指定し、OSKB020123の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND TOLOGPOINT
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM TOLOGPOINT
    CASE OSKB020123
    SOURCE Db2 for z/OS
    ```

    TOLOGPOINTとOSKB020123が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020123を同じ出力で読み、呼出記録のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020123
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020123
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020123
    ```

    DSNV401IとOSKB020123が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の TOLOGPOINT と OSKB020123 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### TORBA {#c07-i0331}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

TORBAは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810


### UNIT {#c07-i0332}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

UNITは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810

??? note "検証手順（1件）"
    **UNIT**

    - 検証目的: 出力整理のオプションについて、UNIT は、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020108の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、出力整理のオプションの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にUNITを指定し、OSKB020108の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND UNIT
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM UNIT
    CASE OSKB020108
    SOURCE Db2 for z/OS
    ```

    UNITとOSKB020108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020108を同じ出力で読み、出力整理のオプションの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020108
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020108
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020108
    ```

    DSNV401IとOSKB020108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の UNIT と OSKB020108 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Utility_Guide p.810



### UPDATE {#c07-i0333}
*分類: ユーティリティ制御文オプション > DSNUTILBオプション*  ・  難易度: 中級

UPDATEは、Db2ユーティリティの制御文または制御文オプションです。対象資源、出力データセット、回復位置、統計取得など、実行結果を左右する指定として扱います。 現時点では候補行として保持し、正式採用前に検索で該当マニュアルのページを確認します

**出典:** Db2_zOS_Utility_Guide p.810



## Db2 for z/OS > ルーチン・トリガー・SQL PL > セキュリティ属性

### SECURITY DB2 {#c07-i0334}
*分類: ルーチン・トリガー・SQL PL > セキュリティ属性*  ・  難易度: 中級

SECURITY DB2は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** routine が外部資源へ触れるため、実行時の権限確認方式を定義で選びます。Db2 側の扱いに寄せる指定はどれですか。

    - A. DB2側権限 ✅
    - B. 統計profile
    - C. DDF port
    - D. copy pool

    正解: **A** ／ 難易度: 中級

    **解説:** 権限確認を Db2 側の扱いに寄せる指定であり、A を採ります。B: 統計収集条件の再利用です。C: 分散接続の口です。D: copy 管理のまとまりです。RACF と SQL 権限を分けて確認します；背景にはセキュリティ属性の指定では、SECURITY DB2 が routine 実行時の非 Db2 資源アクセスを Db2 側の扱いに寄せます、stored procedure が外部ファイルや z/OS 資源へ触れる場合は、どの ID で権限確認されるかが重要です、設計時は RACF 環境と SQL 実行権限を分けて確認しますという関係があり、この区別で確認する名称は「SECURITY」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **SECURITY DB2**

    - 検証目的: 上書追跡のセキュリティ属性について、SECURITY DB2 は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解しに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、上書追跡のセキュリティ属性の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSECURITY DB2を指定し、OSKB020047の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SECURITY DB2
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SECURITY DB2
    CASE OSKB020047
    SOURCE Db2 for z/OS
    ```

    SECURITY DB2とOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020047を同じ出力で読み、上書追跡のセキュリティ属性の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020047
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020047
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020047
    ```

    DSNV401IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SECURITY DB2 と OSKB020047 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### SECURITY USER {#c07-i0335}
*分類: ルーチン・トリガー・SQL PL > セキュリティ属性*  ・  難易度: 中級

SECURITY USERは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 同じ routine でも、呼び出した利用者の権限に応じて外部資源への到達範囲を変えます。指定する属性はどれですか。

    - A. plan hint
    - B. 利用者権限 ✅
    - C. page steal
    - D. RUNSTATS

    正解: **B** ／ 難易度: 中級

    **解説:** 呼び出し利用者の権限で外部資源アクセスを扱う指定であり、B を選びます。A: access path を誘導する情報です。C: buffer pool のページ退避です。D: 統計収集処理です。利用者 ID の z/OS 権限を確認します；背景には呼び出し者側のセキュリティ属性として、SECURITY USER は routine 実行時に利用者 ID の権限を使う考え方です、外部資源アクセスでは、呼び出した利用者が必要な z/OS 権限を持つかが問題になります、共通手続きでも、利用者ごとの到達範囲を変えたい場合に確認しますという関係があり、この区別で確認する名称は「USER」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **SECURITY USER**

    - 検証目的: 出力追跡のセキュリティ属性について、SECURITY USER は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、出力追跡のセキュリティ属性の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にSECURITY USERを指定し、OSKB020048の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND SECURITY USER
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM SECURITY USER
    CASE OSKB020048
    SOURCE Db2 for z/OS
    ```

    SECURITY USERとOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020048を同じ出力で読み、出力追跡のセキュリティ属性の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020048
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020048
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020048
    ```

    DSNV401IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の SECURITY USER と OSKB020048 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation




## Db2 for z/OS > ルーチン・トリガー・SQL PL > ルーチン種類

### UDF {#c07-i0336}
*分類: ルーチン・トリガー・SQL PL > ルーチン種類*  ・  難易度: 中級

UDFは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 業務独自の計算や変換を SQL 式の中で呼び出し、標準関数を主な根拠にしては足りない処理を共通化します。該当するものはどれですか。

    - A. 行削除DDL
    - B. 表space
    - C. bind option
    - D. 利用者関数 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** SQL 式から呼び出す利用者定義関数に当たるため、D を選びます。A: DROP などの定義操作です。B: データを格納する論理構造です。C: package 作成時の指定です。関数名の解決では schema 修飾や CURRENT PATH を確認します；背景には関数として利用するルーチン種類では、UDF を SQL 式から呼び出せる利用者定義関数として扱います、標準関数で足りない計算や変換を共通化し、scalar function や table function として使います、名前解決では schema 修飾や CURRENT PATH を確認し、意図しない関数に解決されないようにしますという関係があり、この区別で確認する名称は「UDF」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **UDF**

    - 検証目的: 構文追跡のルーチン種類について、UDF は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、構文追跡のルーチン種類の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にUDFを指定し、OSKB020041の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND UDF
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM UDF
    CASE OSKB020041
    SOURCE Db2 for z/OS
    ```

    UDFとOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020041を同じ出力で読み、構文追跡のルーチン種類の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020041
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020041
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020041
    ```

    DSNV401IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の UDF と OSKB020041 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### external SQL procedure {#c07-i0337}
*分類: ルーチン・トリガー・SQL PL > ルーチン種類*  ・  難易度: 中級

external SQL procedureは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** SQL で書いた手続きについて、作成準備に DSNTPSMP などの外部支援を使います。該当する種類はどれですか。

    - A. 監査role
    - B. load copy
    - C. 外部SQL準備 ✅
    - D. buffer固定

    正解: **C** ／ 難易度: 中級

    **解説:** 外部の SQL procedure processor で準備される形式に当たるため、C を選びます。A: 権限監査のまとまりです。B: backup 資材の取得です。D: buffer pool の固定指定です。作成支援環境と権限を先に整えます；背景にはSQL 手続きのルーチン種類では、external SQL procedure が外部 SQL procedure processor で準備される形式です、DSNTPSMP を使う場合は、外部 SQL procedure の支援環境と必要な権限を事前に整えます、native 形式へ移行する際は、作成方法と実行環境の違いを切り分けますという関係があり、この区別で確認する名称は「external」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **external SQL procedure**

    - 検証目的: 変更照合のルーチン種類について、external SQL procedureは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻りに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、変更照合のルーチン種類の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にexternal SQL proceを指定し、OSKB020040の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND external SQL proce
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM external SQL proce
    CASE OSKB020040
    SOURCE Db2 for z/OS
    ```

    external SQL proceとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020040を同じ出力で読み、変更照合のルーチン種類の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020040
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020040
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020040
    ```

    DSNV401IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の external SQL proce と OSKB020040 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### external stored procedure {#c07-i0338}
*分類: ルーチン・トリガー・SQL PL > ルーチン種類*  ・  難易度: 中級

external stored procedureは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 既存の COBOL プログラムを手続きとして呼び出し、WLM 管理のアドレス空間で動かします。該当する種類はどれですか。

    - A. 索引設計
    - B. 外部実行手続き ✅
    - C. SQL表関数
    - D. 行契機処理

    正解: **B** ／ 難易度: 中級

    **解説:** 外部プログラムを WLM 管理のアドレス空間で動かす手続きに当たるため、B を選びます。A: access path に関係する設計です。C: SQL から呼ぶ関数の一種です。D: 表の変更に反応する処理です。実行環境と外部資源権限の確認が必要です；背景には外部連携を含むルーチン種類として、external stored procedure は WLM 管理のアドレス空間で外部プログラムを実行します、処理本体は COBOL、C、Java などの言語で用意され、Db2 には手続き定義として登録されます、運用では WLM 環境、外部資源権限、ロードモジュールの配置をそろえますという関係があり、この区別で確認する名称は「stored」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **external stored procedure**

    - 検証目的: 監査照合のルーチン種類について、external stored procedureは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、監査照合のルーチン種類の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にexternal stored prを指定し、OSKB020039の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND external stored pr
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM external stored pr
    CASE OSKB020039
    SOURCE Db2 for z/OS
    ```

    external stored prとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020039を同じ出力で読み、監査照合のルーチン種類の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020039
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020039
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020039
    ```

    DSNV401IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の external stored pr と OSKB020039 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### native SQL procedure {#c07-i0339}
*分類: ルーチン・トリガー・SQL PL > ルーチン種類*  ・  難易度: 中級

native SQL procedureは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** SQL PL で書いた手続き本体を Db2 側で管理し、外部実行モジュールを別に用意しない方式を選びます。該当する種類はどれですか。

    - A. SQL内蔵処理 ✅
    - B. 外部言語呼出し
    - C. 関数拡張
    - D. 表更新契機

    正解: **A** ／ 難易度: 中級

    **解説:** Db2 内で SQL PL 手続き本体を管理する方式に当たるため、A を選びます。B: COBOL や Java など外部言語の実行に寄る手続きです。C: SQL 式から呼ぶ利用者定義関数です。D: 表操作に反応するトリガーです。移行時は依存機能と権限を先に確認します；背景にはnative SQL procedure は、ルーチン種類の中で Db2 内に管理される SQL 手続きです、手続き本体は SQL PL で書き、外部実行モジュールを用意せずに Db2 側で準備されます、外部手続きから移行する場合は、実行権限、依存する機能、デバッグ条件を確認しますという関係があり、この区別で確認する名称は「native」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **native SQL procedure**

    - 検証目的: 復旧照合のルーチン種類について、native SQL procedureは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、復旧照合のルーチン種類の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にnative SQL proceduを指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND native SQL procedu
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM native SQL procedu
    CASE OSKB020038
    SOURCE Db2 for z/OS
    ```

    native SQL proceduとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020038を同じ出力で読み、復旧照合のルーチン種類の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020038
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020038
    ```

    DSNV401IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の native SQL procedu と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation




## Db2 for z/OS > ルーチン・トリガー・SQL PL > 定義操作

### ALTER PROCEDURE {#c07-i0340}
*分類: ルーチン・トリガー・SQL PL > 定義操作*  ・  難易度: 初級

ALTER PROCEDUREは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。定義操作の作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 既存手続きのデバッグ可否や実行環境など、変更可能な属性のみを更新します。使う操作はどれですか。

    - A. 表領域作成
    - B. 手続き属性変更 ✅
    - C. 通信port表示
    - D. backup取得

    正解: **B** ／ 難易度: 中級

    **解説:** 既存手続きの変更可能な属性を更新する操作であり、B が合います。A: storage 構造を作る DDL です。C: DDF 接続口の確認です。D: image copy などの保守作業です。手続き種類ごとの変更制約を確認します；背景には既存 procedure の定義操作では、ALTER PROCEDURE によって変更可能な属性を更新します、debug mode、WLM 環境、版の扱いなどは手続き種類によって制約が異なります、obfuscation された手続きや作成時に固定された条件は、変更可否を SQL Reference で確認しますという関係があり、この区別で確認する名称は「ALTER」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **ALTER PROCEDURE**

    - 検証目的: 展開追跡の定義操作について、ALTER PROCEDURE は、Db2オブジェクトの定義を作成、変更、削除するための DDL です。定義操作の作業では、対象オブジェクト、依存関係、後続の REBIND や RUNに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、展開追跡の定義操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にALTER PROCEDUREを指定し、OSKB020042の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND ALTER PROCEDURE
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM ALTER PROCEDURE
    CASE OSKB020042
    SOURCE Db2 for z/OS
    ```

    ALTER PROCEDUREとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020042を同じ出力で読み、展開追跡の定義操作の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020042
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020042
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020042
    ```

    DSNV401IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の ALTER PROCEDURE と OSKB020042 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### CREATE FUNCTION {#c07-i0341}
*分類: ルーチン・トリガー・SQL PL > 定義操作*  ・  難易度: 初級

CREATE FUNCTIONは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。定義操作の作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 独自関数を SQL 式から呼び出せるように登録し、引数型や実装方式を定義します。使う操作はどれですか。

    - A. thread表示
    - B. view削除
    - C. 関数登録 ✅
    - D. copy複製

    正解: **C** ／ 難易度: 中級

    **解説:** 利用者定義関数を登録する定義操作に当たるため、C が該当します。A: 実行中 thread の確認です。B: 既存 view を取り除く DDL です。D: copy 資材を別 copy へ複製する処理です。名前解決と引数型を定義時にそろえます；背景には関数を追加する定義操作として、CREATE FUNCTION は Db2 に利用者定義関数を登録します、compiled SQL scalar function、inlined SQL scalar function、外部関数など、実装方式に応じて属性が変わります、SQL から呼ばれるため、名前解決、引数型、実行権限を合わせて設計しますという関係があり、この区別で確認する名称は「FUNCTION」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203



### CREATE PROCEDURE {#c07-i0342}
*分類: ルーチン・トリガー・SQL PL > 定義操作*  ・  難易度: 初級

CREATE PROCEDUREは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。定義操作の作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 新しい手続きを Db2 に登録し、引数や言語、WLM 環境などを定義します。使う操作はどれですか。

    - A. 新規手続き登録 ✅
    - B. 統計再収集
    - C. log退避
    - D. 索引再編成

    正解: **A** ／ 難易度: 中級

    **解説:** 手続きを新規登録する定義操作のため、A に当たります。B: RUNSTATS などで統計を更新する作業です。C: active log を archive 側へ退避する運用です。D: 索引の保守処理です。引数、言語、実行属性を定義時にそろえます；背景には定義操作の中心として、CREATE PROCEDURE は Db2 に stored procedure の名前、引数、言語、実行属性を登録します、SQL PL 本体を定義に含める場合は native SQL procedure として扱います、外部手続きでは外部名、WLM 環境、parameter style などを実行方式に合わせますという関係があり、この区別で確認する名称は「PROCEDURE」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203



### CREATE TRIGGER {#c07-i0343}
*分類: ルーチン・トリガー・SQL PL > 定義操作*  ・  難易度: 初級

CREATE TRIGGERは、Db2オブジェクトの定義を作成、変更、削除するためのDDLです。定義操作の作業では、対象オブジェクト、依存関係、後続のREBINDやRUNSTATSへの影響を確認してから使います

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation


### INSTEAD OF trigger {#c07-i0344}
*分類: ルーチン・トリガー・SQL PL > 定義操作*  ・  難易度: 中級

INSTEAD OF triggerは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 更新できない view に対する操作を受け、基礎表への別処理として実行させます。該当する仕組みはどれですか。

    - A. index only scan
    - B. archive log
    - C. view代替契機 ✅
    - D. thread reuse

    正解: **C** ／ 難易度: 中級

    **解説:** view への操作を代替処理へ置き換える trigger に当たるため、C にします。A: 索引を主な根拠にして読み取る access path です。B: 退避済み log 資材です。D: thread の再利用に関する考え方です。基礎表への実処理と権限を確認します；背景にはINSTEAD OF trigger は、view 更新と組み合わせる定義操作として直接更新できない view への操作を別の処理に置き換えます、アプリケーションは view に対して更新したように見えます、実際には trigger 本体が基礎表への処理を実行しますという関係があり、この区別で確認する名称は「INSTEAD」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **INSTEAD OF trigger**

    - 検証目的: 呼出追跡の定義操作について、INSTEAD OF triggerは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、呼出追跡の定義操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にINSTEAD OF triggerを指定し、OSKB020043の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND INSTEAD OF trigger
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM INSTEAD OF trigger
    CASE OSKB020043
    SOURCE Db2 for z/OS
    ```

    INSTEAD OF triggerとOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020043を同じ出力で読み、呼出追跡の定義操作の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020043
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020043
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020043
    ```

    DSNV401IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の INSTEAD OF trigger と OSKB020043 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation




## Db2 for z/OS > ルーチン・トリガー・SQL PL > 実行・移行

### CALL statement {#c07-i0345}
*分類: ルーチン・トリガー・SQL PL > 実行・移行*  ・  難易度: 中級

CALL statementは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** client program から stored procedure を実行し、必要な引数を渡します。使う SQL 文はどれですか。

    - A. CREATE INDEX
    - B. ALTER TABLE
    - C. FETCH ONLY
    - D. 手続き呼出し ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 手続きを実行する SQL 文に当たるため、D にします。A: index を作成する DDL です。B: 表定義を変更する DDL です。C: cursor 読み取りの指定です。呼び出し時は schema 修飾と引数の対応を確認します；背景には実行・移行の作業で routine を呼び出すとき、CALL statement は stored procedure を実行する SQL 文です、client program、ODBC、JDBC、Db2 command line processor などから使えます、引数の渡し方や schema 修飾を誤ると、別 schema の procedure に解決される可能性がありますという関係があり、この区別で確認する名称は「statement」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **CALL statement**

    - 検証目的: 条件追跡の実行・移行について、CALL statementは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、条件追跡の実行・移行の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にCALL statementを指定し、OSKB020049の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND CALL statement
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM CALL statement
    CASE OSKB020049
    SOURCE Db2 for z/OS
    ```

    CALL statementとOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020049を同じ出力で読み、条件追跡の実行・移行の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020049
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020049
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020049
    ```

    DSNV401IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の CALL statement と OSKB020049 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### DSNTPSMP {#c07-i0346}
*分類: ルーチン・トリガー・SQL PL > 実行・移行*  ・  難易度: 中級

DSNTPSMPは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** debugger 利用時の作成経路として、外部 SQL 手続きを作成・準備する REXX stored procedure を選びます。該当するものはどれですか。

    - A. ADMIN_INFO_SYSPARM
    - B. DSNTPSMP ✅
    - C. DSN1COPY
    - D. DSNJU003

    正解: **B** ／ 難易度: 中級

    **解説:** 作成支援用の手続きとして外部 SQL 手続きを準備するため、B が適切です。A: subsystem parameter の照会に使う管理手続きです。C: data set を複写する道具です。D: BSDS 変更系の保守道具です。WLM 環境と必要権限を事前に整えます；背景には実行・移行で使う DSNTPSMP は、external SQL procedure を作成・準備するための REXX stored procedure です、利用するには支援環境、WLM 環境、REXX language support、必要権限を整えます、debugger を使う場合は、JCL ではなく DSNTPSMP を使う指示がありますという関係があり、この区別で確認する名称は「DSNTPSMP」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203



### external to native procedure migration {#c07-i0347}
*分類: ルーチン・トリガー・SQL PL > 実行・移行*  ・  難易度: 中級

external to native procedure migrationは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 外部準備物を減らすため、外部 SQL 手続きを Db2 側で管理する SQL PL 手続きへ置き換えます。該当する作業はどれですか。

    - A. log archive
    - B. trigger drop
    - C. buffer split
    - D. native移行 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** native 形式へ外部 SQL 手続きを移す作業に当たるため、D を選びます。A: active log の退避運用です。B: trigger を削除する DDL です。C: buffer pool の分割設計です。非対応機能と呼び出し側影響を先に確認します；背景にはexternal to native procedure migration は、実行・移行の中で SQL 手続きを native SQL procedure へ置き換える作業です、外部準備物を減らし、Db2 側で手続き本体を管理しやすくする狙いがあります、移行前には非対応機能、権限、呼び出し側への影響を洗い出しますという関係があり、この区別で確認する名称は「migration」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203




## Db2 for z/OS > ルーチン・トリガー・SQL PL > 実行環境

### ASUTIME {#c07-i0348}
*分類: ルーチン・トリガー・SQL PL > 実行環境*  ・  難易度: 中級

ASUTIMEは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** routine の処理量に上限を設け、誤った長時間実行が Db2 資源を占有しないようにします。指定する属性はどれですか。

    - A. VIEW CHECK
    - B. SQL PATH
    - C. 処理量上限 ✅
    - D. LOG APPLY

    正解: **C** ／ 難易度: 中級

    **解説:** 処理量上限を指定する属性に当たるため、C を選びます。A: view 更新時の検査に関係します。B: 関数や手続きの名前解決経路です。D: log 適用の回復処理です。正常処理を止めない値に調整します；背景にはASUTIME は、実行環境で routine が消費できる処理量の上限を指定する属性です、無制限に走る処理や誤ったループが Db2 資源を占有しないようにする目的があります、設定値は業務処理の正常な所要量を見て決め、低すぎる値で正規処理を止めないようにしますという関係があり、この区別で確認する名称は「ASUTIME」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **ASUTIME**

    - 検証目的: 終端追跡の実行環境について、ASUTIME は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、終端追跡の実行環境の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にASUTIMEを指定し、OSKB020045の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND ASUTIME
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM ASUTIME
    CASE OSKB020045
    SOURCE Db2 for z/OS
    ```

    ASUTIMEとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020045を同じ出力で読み、終端追跡の実行環境の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020045
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020045
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020045
    ```

    DSNV401IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の ASUTIME と OSKB020045 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### PARAMETER STYLE {#c07-i0349}
*分類: ルーチン・トリガー・SQL PL > 実行環境*  ・  難易度: 中級

PARAMETER STYLEは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 外部プログラムが引数をどの並びや形式で受け取るかを、routine 定義で指定します。該当する属性はどれですか。

    - A. schema owner
    - B. 引数受渡形式 ✅
    - C. log mode
    - D. buffer steal

    正解: **B** ／ 難易度: 中級

    **解説:** 外部本体との引数受け渡し形式を示す属性のため、B が適切です。A: object の所有者に関係します。C: log 運用の状態です。D: buffer pool のページ退避です。SQL 定義と外部プログラムの並びを一致させます；背景にはPARAMETER STYLE は、実行環境と routine 本体の間で引数をどの形式で受け渡すかを示す属性です、外部 stored procedure や UDF では、言語や実装方式に合う style を選びます、呼び出し側の SQL 定義と外部プログラムの引数並びがずれると、実行時の障害につながりますという関係があり、この区別で確認する名称は「STYLE」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **PARAMETER STYLE**

    - 検証目的: 置換追跡の実行環境について、PARAMETER STYLE は、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、置換追跡の実行環境の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にPARAMETER STYLEを指定し、OSKB020044の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND PARAMETER STYLE
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM PARAMETER STYLE
    CASE OSKB020044
    SOURCE Db2 for z/OS
    ```

    PARAMETER STYLEとOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020044を同じ出力で読み、置換追跡の実行環境の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020044
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020044
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020044
    ```

    DSNV401IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の PARAMETER STYLE と OSKB020044 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation



### WLM ENVIRONMENT {#c07-i0350}
*分類: ルーチン・トリガー・SQL PL > 実行環境*  ・  難易度: 中級

WLM ENVIRONMENTは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 外部 routine を WLM 管理のアドレス空間へ割り当て、負荷特性に合う環境で動かします。指定するものはどれですか。

    - A. 実行WLM環境 ✅
    - B. SQLCODE
    - C. COPYDDN
    - D. APPLCOMPAT

    正解: **A** ／ 難易度: 中級

    **解説:** 外部処理を動かす WLM アプリケーション環境の指定であり、A が合います。B: SQL 実行結果のコードです。C: utility の DD 名指定です。D: SQL 互換レベルの指定です。負荷特性別に環境を分ける設計が必要です；背景にはWLM を使う実行環境では、WLM ENVIRONMENT が stored procedure や UDF を動かすアプリケーション環境を指定します、多くの外部 routine は、native SQL procedure と異なり WLM 管理のアドレス空間で実行されます、負荷特性が違う routine を同じ環境に詰め込まないよう設計しますという関係があり、この区別で確認する名称は「ENVIRONMENT」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203



### result sets {#c07-i0351}
*分類: ルーチン・トリガー・SQL PL > 実行環境*  ・  難易度: 中級

result setsは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解します

**出典:** Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** stored procedure から呼び出し元へ cursor 経由で結果を返す設計にします。定義で意識するものはどれですか。

    - A. active log
    - B. lock timeout
    - C. image copy
    - D. 戻り結果集合 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 手続きから返す結果集合を扱う指定であり、D が該当します。A: 現在書き込み中の log 資材です。B: lock 待ちの上限時間です。C: backup のための copy 資材です。DYNAMIC RESULT SETS の数と client 側の受け取りをそろえます；背景にはresult sets は、実行環境で stored procedure が呼び出し側へ返す結果集合を表します、DYNAMIC RESULT SETS の数を定義すると、呼び出し側は cursor を受け取って結果を読みます、設計時は返却件数、cursor の閉じ忘れ、client 側の受け取り方式を確認しますという関係があり、この区別で確認する名称は「result」です。

    **出典:** Db2_zOS_AppProg_SQL_Guide.pdf p.282 / Db2_zOS_AppProg_SQL_Guide.pdf p.295 / Db2_zOS_AppProg_SQL_Guide.pdf p.298 / Db2_zOS_Installation.pdf p.505 / Db2_zOS_Installation.pdf p.564 / Db2_zOS_Installation.pdf p.574 / Db2_zOS_Installation.pdf p.981 / Db2_zOS_Installation.pdf p.984 / Db2_zOS_SQL_Reference.pdf p.1289 / Db2_zOS_SQL_Reference.pdf p.1420 / Db2_zOS_SQL_Reference.pdf p.1460 / Db2_zOS_Admin_Guide.pdf p.520 / Db2_zOS_AppProg_Java.pdf p.203


??? note "検証手順（1件）"
    **result sets**

    - 検証目的: 探索追跡の実行環境について、result setsは、Db2のルーチン、関数、プロシージャ、トリガー、SQL PL 実行に関わる項目です。実行環境、権限、呼び出し形式、失敗時の戻り情報を合わせて理解しまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、探索追跡の実行環境の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にresult setsを指定し、OSKB020046の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND result sets
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM result sets
    CASE OSKB020046
    SOURCE Db2 for z/OS
    ```

    result setsとOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020046を同じ出力で読み、探索追跡の実行環境の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020046
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020046
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020046
    ```

    DSNV401IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の result sets と OSKB020046 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_AppProg_SQL_Guide / Db2_zOS_SQL_Reference / Db2_zOS_Installation




## Db2 for z/OS > ログと回復

### アクティブログ {#c07-i0352}
*分類: ログと回復*  ・  難易度: 中級

Db2 for z/OS の ログと回復で扱うアクティブログは、Db2 が現在の更新履歴を記録するログデータセットです。コミット済み更新の回復、再始動、障害後の整合性維持に必要です。運用では満杯、切替、二重化の状態を監視します

**出典:** Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security

??? question "確認問題（1問）"
    **問題.** 出力確認のアクティブログに関するアクティブログの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. -DISPLAY THREAD(*)の結果を残さず出力確認のアクティブログの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のアクティブログの証跡として保存して根拠にする。
    - C. アクティブログの変更点を出力本文から切り離して出力確認のアクティブログの承認欄のみ残す。
    - D. Db2 for z/OS の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠ではアクティブログは「アクティブログの状態と出力メッセージを結び付ける出力確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存ではアクティブログの出力行と DSNV401I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象ではアクティブログを Db2 for z/OS の確認記録に残し、対象名は出力確認対象です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（1件）"
    **アクティブログ**

    - 検証目的: 出力確認のアクティブログについて、Db2 for z/OS の ログと回復で扱うアクティブログは、Db2 が現在の更新履歴を記録するログデータセットです。コミット済み更新の回復、再始動、障害後の整合性維持にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD(*) を入力し、出力確認のアクティブログの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    ```

    COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にアクティブログを指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND アクティブログ
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM アクティブログ
    CASE OSKB010008
    SOURCE Db2 for z/OS
    ```

    アクティブログとOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010008を同じ出力で読み、出力確認のアクティブログの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010008
    -DISPLAY THREAD(*)
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010008
    ```

    DSNV401IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD(*) が画面・出力に表示されること
    ② ステップ2 の アクティブログ と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security



### アーカイブログ {#c07-i0353}
*分類: ログと回復*  ・  難易度: 中級

Db2 for z/OS の ログと回復で扱うアーカイブログは、切り替え済みのアクティブログを長期保管するためのログです。ポイントインタイム回復や災害復旧で必要になるため、保存期間と媒体の可用性が重要です。リカバリ計画ではアーカイブログの欠落がないかを確認します

**出典:** Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security

??? question "確認問題（1問）"
    **問題.** 条件確認のアーカイブログに関係するアーカイブログの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 ✅
    - B. アーカイブログの名称と担当者名のみを残して条件確認のアーカイブログの表示本文を確認対象に含めない。
    - C. データベース管理以外の画面で条件確認のアーカイブログを確認し同じ証跡として扱ったことにする。
    - D. DSNV401I の有無を見ず条件確認のアーカイブログの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠ではアーカイブログは「アーカイブログの用途をデータベース管理の表示で確認する条件確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では Db2 for z/OS のアーカイブログと DSNV401I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語ではアーカイブログを Db2 for z/OS で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（1件）"
    **アーカイブログ**

    - 検証目的: 条件確認のアーカイブログについて、Db2 for z/OS の ログと回復で扱うアーカイブログは、切り替え済みのアクティブログを長期保管するためのログです。ポイントインタイム回復や災害復旧で必要になるため、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD(*) を入力し、条件確認のアーカイブログの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    ```

    COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にアーカイブログを指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND アーカイブログ
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM アーカイブログ
    CASE OSKB010009
    SOURCE Db2 for z/OS
    ```

    アーカイブログとOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010009を同じ出力で読み、条件確認のアーカイブログの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010009
    -DISPLAY THREAD(*)
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010009
    ```

    DSNV401IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD(*) が画面・出力に表示されること
    ② ステップ2 の アーカイブログ と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security




## Db2 for z/OS > ログ・回復・再始動 > BSDS・ログ管理

### BSDS {#c07-i0354}
*分類: ログ・回復・再始動 > BSDS・ログ管理*  ・  難易度: 中級

BSDSは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation


### DSNJU003 {#c07-i0355}
*分類: ログ・回復・再始動 > BSDS・ログ管理*  ・  難易度: 上級

DSNJU003は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** ログデータセットの登録内容やDDF関連のBSDS情報を変更する必要があります。BSDSの中身を書き換える作業で使うものはどれを選びますか。

    - A. BSDS更新ユーティリティ ✅
    - B. ログマップ印刷ユーティリティ
    - C. アクセスパス説明機能
    - D. 表データ抽出ユーティリティ

    正解: **A** ／ 難易度: 上級

    **解説:** ログ目録を変更する作業なので、Aを選びます。BはBSDSの内容を印刷して確認する用途です。CはSQLのアクセスパス確認で使います。Dは表データを外部ファイルへ出す処理です。二重BSDSでは片方のみを更新しない運用が欠かせません；背景にはBSDS・ログ管理の変更作業で使うDSNJU003は、Db2 for z/OSのchange log inventoryとしてBSDS内のログ目録やDDF関連情報などを変更します、二重BSDSを扱う場合は両方のコピーを同じ実行で更新し、片側のみを変更して同期を崩さないようにします、更新後は印刷結果で内容を確認しますという関係があり、この区別で確認する名称は「DSNJU003」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting



### DSNJU004 {#c07-i0356}
*分類: ログ・回復・再始動 > BSDS・ログ管理*  ・  難易度: 上級

DSNJU004は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** BSDSに登録されたログ範囲やチェックポイントを変更せずに一覧化し、障害調査の証跡として残します。実行する確認作業として適切なものはどれでしょうか。

    - A. ログ目録の変更
    - B. 表スペースのCOPY
    - C. ログマップの印刷 ✅
    - D. パッケージの再BIND

    正解: **C** ／ 難易度: 上級

    **解説:** ログマップを一覧化するため、Cが正解です。AはBSDSを書き換える作業で、参照のみの確認ではありません。Bは回復用コピーを作るユーティリティです。Dはアプリケーションのアクセスパス再生成に関わります。印刷結果は再始動前後の比較資料になります；背景にはBSDSの内容確認で使うDSNJU004は、Db2 for z/OSのログマップを印刷する単独実行プログラムです、障害調査やBSDS変更後の確認では、アクティブログ、アーカイブログ、チェックポイント、データ共用メンバー情報などが期待どおりかを出力で確認しますという関係があり、この区別で確認する名称は「DSNJU004」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **DSNJU004**

    - 検証目的: 出力整理の・ログ管理について、DSNJU004 は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010108の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、出力整理の・ログ管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNJU004を指定し、OSKB010108の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNJU004
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNJU004
    CASE OSKB010108
    SOURCE Db2 for z/OS
    ```

    DSNJU004とOSKB010108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010108を同じ出力で読み、出力整理の・ログ管理の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010108
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010108
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010108
    ```

    DSNV401IとOSKB010108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNJU004 と OSKB010108 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation




## Db2 for z/OS > ログ・回復・再始動 > コピー・回復方式

### catalog and directory recovery {#c07-i0357}
*分類: ログ・回復・再始動 > コピー・回復方式*  ・  難易度: 中級

catalog and directory recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 定義情報を保持するシステム表群や内部制御領域に障害があり、Db2基盤資材として復旧順序を管理します。対象となる回復作業はどれですか。

    - A. ユーザー表のみのEXPORT
    - B. JDBCドライバー更新
    - C. カタログとディレクトリの回復 ✅
    - D. SQLCAの再初期化

    正解: **C** ／ 難易度: 中級

    **解説:** Db2基盤資材の復旧なので、Cが該当します。Aは業務データの取り出しで、システム資材の回復ではありません。Bはクライアント接続部品の保守です。Dはプログラム側の状態初期化です。影響範囲が広いため、回復点と再始動手順をそろえます；背景にはカタログ・ディレクトリ障害を扱う回復方式では、catalog and directory recoveryがDb2 for z/OSの定義情報や内部制御資材を戻します、通常の業務表より影響範囲が広く、コピー、ログ、停止範囲、再始動順序を慎重に確認します、復旧後はカタログを参照する関連処理も確認対象になりますという関係があり、この区別で確認する名称は「directory」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting



### image copy {#c07-i0358}
*分類: ログ・回復・再始動 > コピー・回復方式*  ・  難易度: 中級

image copyは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 表スペース障害に備え、後でRECOVERの基点にできるデータセットを定期的に取得します。この回復資材は何と呼ぶのが適切ですか。

    - A. SQL通信領域
    - B. アクセスパス表
    - C. スレッド待ち情報
    - D. 回復用イメージコピー ✅

    正解: **D** ／ 難易度: 中級

    **解説:** コピーを回復の基点にするため、Dを選びます。Aはプログラム側でSQL結果を受ける領域です。BはEXPLAIN結果の格納先です。Cは性能調査で見る待ち情報です。取得後はSYSCOPYやREPORT RECOVERYで世代を確認します；背景には回復用コピーの管理で使うimage copyは、Db2 for z/OSの表スペースや索引スペースなどの内容を回復用に取得したコピーです、回復処理ではコピーを基点にログを適用して戻すため、取得時点、対象名、コピー世代、SYSCOPYの記録をそろえて管理します、候補確認にはREPORT RECOVERYの出力を使いますという関係があり、この区別で確認する名称は「image」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting



### page recovery {#c07-i0359}
*分類: ログ・回復・再始動 > コピー・回復方式*  ・  難易度: 中級

page recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 表スペース全体を戻すのではなく、破損が確認された一部ページのみを対象にして復旧時間を抑えたい状況です。近い考え方はどれでしょうか。

    - A. 全件UNLOAD
    - B. ページ単位の回復 ✅
    - C. 列マスク作成
    - D. パッケージ解放

    正解: **B** ／ 難易度: 中級

    **解説:** 対象ページのみを戻す考え方なので、Bを選びます。Aは表データを外部へ取り出す操作です。Cは行列アクセス制御に関わる定義です。Dは実行資材を解放する管理作業です。実施前に診断資料で破損範囲を特定します；背景にはページ損傷を扱う回復方式では、page recoveryがDb2 for z/OSの表スペース全体ではなく損傷ページを対象にします、影響範囲を小さく抑えられる一方、対象ページ、必要なコピー、ログ範囲、オブジェクト状態を正確に把握してから実行します、診断資料で範囲を特定しますという関係があり、この区別で確認する名称は「page」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **page recovery**

    - 検証目的: 比較整理のコピー・回復方式について、page recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL 全体ではなく、対象指定、処理に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010114の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、比較整理のコピー・回復方式の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にpage recoveryを指定し、OSKB010114の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND page recovery
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM page recovery
    CASE OSKB010114
    SOURCE Db2 for z/OS
    ```

    page recoveryとOSKB010114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010114を同じ出力で読み、比較整理のコピー・回復方式の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010114
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010114
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010114
    ```

    DSNV401IとOSKB010114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の page recovery と OSKB010114 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation



### point-in-time recovery {#c07-i0360}
*分類: ログ・回復・再始動 > コピー・回復方式*  ・  難易度: 中級

point-in-time recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL全体ではなく、対象指定、処理目的、実行後に確認する状態を中心に扱います

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 誤更新が発生したため、最新状態ではなく、問題発生直前のログ位置まで表スペースを戻します。この回復方式として正しいものはどれですか。

    - A. 時点指定回復 ✅
    - B. 統計履歴削除
    - C. 索引のRUNSTATS
    - D. DDFポート変更

    正解: **A** ／ 難易度: 中級

    **解説:** 特定の過去時点へ戻すため、Aが正解です。Bはカタログ内の統計履歴整理です。Cは索引統計の収集作業です。Dは分散接続の設定変更です。停止点にはRBAやLRSNを使い、必要なコピーとログを事前に確認します；背景には時点指定の回復方式では、point-in-time recoveryがDb2 for z/OSのRECOVERでTOCOPY、TOLOGPOINT、TORBAなどを使って対象を特定時点へ戻します、イメージコピー完了後のRBAまたはLRSNを確認し、必要なログ範囲がそろっていることを前提に実施します、誤更新対応では停止点の選定が重要ですという関係があり、この区別で確認する名称は「point-in-time」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **point-in-time recovery**

    - 検証目的: 記録整理のコピー・回復方式について、point-in-time recoveryは、Db2ユーティリティまたはその制御文で、データ保守、統計収集、コピー、回復、再編成などの実行単位になります。JCL 全体ではなに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010113の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、記録整理のコピー・回復方式の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にpoint-in-time recoを指定し、OSKB010113の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND point-in-time reco
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM point-in-time reco
    CASE OSKB010113
    SOURCE Db2 for z/OS
    ```

    point-in-time recoとOSKB010113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010113を同じ出力で読み、記録整理のコピー・回復方式の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010113
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010113
    ```

    DSNV401IとOSKB010113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の point-in-time reco と OSKB010113 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation




## Db2 for z/OS > ログ・回復・再始動 > ログ資材

### active log {#c07-i0361}
*分類: ログ・回復・再始動 > ログ資材*  ・  難易度: 中級

active logは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? note "検証手順（1件）"
    **active log**

    - 検証目的: 探索整理のログ資材について、active logは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010106の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、探索整理のログ資材の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にactive logを指定し、OSKB010106の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND active log
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM active log
    CASE OSKB010106
    SOURCE Db2 for z/OS
    ```

    active logとOSKB010106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010106を同じ出力で読み、探索整理のログ資材の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010106
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010106
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010106
    ```

    DSNV401IとOSKB010106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の active log と OSKB010106 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation



### archive log {#c07-i0362}
*分類: ログ・回復・再始動 > ログ資材*  ・  難易度: 中級

archive logは、Db2サブシステムや対象資源の状態を表示、開始、停止、変更する運用コマンド項目です。MVSコマンド一般ではなく、Db2側で何が変わり、どの表示で確認できるかを扱います

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation


### dual logging {#c07-i0363}
*分類: ログ・回復・再始動 > ログ資材*  ・  難易度: 中級

dual loggingは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** ログを置くディスクを分け、片側障害でも再始動や回復に必要なログ範囲を失わない構成にしたい場面です。採るべき考え方はどれですか。

    - A. アーカイブログの削除
    - B. ログの二重化 ✅
    - C. 表スペースの再編成
    - D. SQLCAの初期化

    正解: **B** ／ 難易度: 中級

    **解説:** 二つのログコピーを保持する構成なので、Bが正解です。Aは保存済みログの整理で、可用性を上げる仕組みではありません。Cは表データの物理配置を直す処理です。DはSQL結果を受け取るアプリケーション領域で、ログ資材の保護とは役割が違います。二重化していてもBSDSとの範囲不一致は再始動障害になります；背景にはログ資材の保護で扱うdual loggingは、Db2 for z/OSのログを二重化して障害時の復旧可能性を高める構成です、片方のログデータセットやボリュームに問題が出ても、もう一方のコピーからログ範囲を確認して再始動や回復へ進めます、登録内容と実データセットの世代がBSDS上でそろっていることが重要ですという関係があり、この区別で確認する名称は「logging」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting




## Db2 for z/OS > ログ・回復・再始動 > 再始動ポイント

### ACCESS(MAINT) {#c07-i0364}
*分類: ログ・回復・再始動 > 再始動ポイント*  ・  難易度: 中級

ACCESS(MAINT)は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 表スペースの復旧作業中に一般利用者の参照・更新を入れず、保守担当のみが扱える状態にしたい場面です。設定するアクセス状態として合うものはどれですか。

    - A. ACCESS(RO)
    - B. 保守用アクセス ✅
    - C. WITH HOLD
    - D. KEEPDYNAMIC(YES)

    正解: **B** ／ 難易度: 中級

    **解説:** 保守作業用に利用を絞るため、Bが該当します。Aは読み取り専用の方向で、保守状態とは意図が異なります。Cはカーソル保持のSQL指定です。Dは動的SQLキャッシュ関連のBIND属性です。作業後は通常アクセスへ戻す確認を入れます；背景には再始動ポイント周辺の保守作業で使うACCESS(MAINT)は、Db2 for z/OSの対象オブジェクトを保守用アクセス状態にして通常利用を抑止する指定です、復旧作業の前に業務更新が入らない状態を作り、RECOVERや検証後のSTART DATABASEで通常アクセスへ戻します、保守状態を残さない確認も必要ですという関係があり、この区別で確認する名称は「ACCESS」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **ACCESS(MAINT)**

    - 検証目的: 優先整理の再始動ポイントについて、ACCESS(MAINT)は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010112の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、優先整理の再始動ポイントの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にACCESS(MAINT)を指定し、OSKB010112の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND ACCESS(MAINT)
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM ACCESS(MAINT)
    CASE OSKB010112
    SOURCE Db2 for z/OS
    ```

    ACCESS(MAINT)とOSKB010112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010112を同じ出力で読み、優先整理の再始動ポイントの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010112
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010112
    ```

    DSNV401IとOSKB010112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の ACCESS(MAINT) と OSKB010112 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation



### ENDRBA {#c07-i0365}
*分類: ログ・回復・再始動 > 再始動ポイント*  ・  難易度: 中級

ENDRBAは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** ログ範囲を棚卸しするとき、対象ログの終端を示す値を記録し、再始動でどこまでを含めるか確認します。この終端を表す項目はどれですか。

    - A. START DATABASE
    - B. ログ範囲の終了RBA ✅
    - C. バッファプールサイズ
    - D. パッケージ所有者

    正解: **B** ／ 難易度: 中級

    **解説:** ログ範囲の終端を示すため、Bを選びます。Aはオブジェクトを開始するDb2コマンドです。Cはメモリ割り当ての設定値です。Dはパッケージ定義に付く管理属性です。終了位置と開始位置の対応をBSDS出力で突き合わせます；背景にはログ範囲の終了確認で見るENDRBAは、Db2 for z/OSのログデータセットや回復処理で扱う範囲の終了位置を表すRBA値です、条件付き再始動やBSDS確認では、開始点を主な根拠にしてなく終了点がどこまでを対象に含めるかを決めます、誤った値はログ適用範囲のずれにつながりますという関係があり、この区別で確認する名称は「ENDRBA」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **ENDRBA**

    - 検証目的: 条件整理の再始動ポイントについて、ENDRBA は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010109の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、条件整理の再始動ポイントの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にENDRBAを指定し、OSKB010109の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND ENDRBA
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM ENDRBA
    CASE OSKB010109
    SOURCE Db2 for z/OS
    ```

    ENDRBAとOSKB010109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010109を同じ出力で読み、条件整理の再始動ポイントの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010109
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010109
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010109
    ```

    DSNV401IとOSKB010109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の ENDRBA と OSKB010109 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation



### LRSN {#c07-i0366}
*分類: ログ・回復・再始動 > 再始動ポイント*  ・  難易度: 中級

LRSNは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** Data Sharingグループで複数メンバーの更新順序をそろえて復旧点を決めます。グループ全体のログ順序を比較する値として適切なのはどれですか。

    - A. LOBロケータ
    - B. SDSFジョブID
    - C. ログレコードシーケンス番号 ✅
    - D. SQLプロシージャ名

    正解: **C** ／ 難易度: 中級

    **解説:** データ共用全体のログ順序を示すため、Cを選びます。Aは大きなオブジェクトを参照するSQL値です。BはJES上のジョブ識別子です。Dはルーチン定義の名前です。復旧停止点ではRBAとの環境差を意識します；背景にはData Sharing環境のログ順序で使うLRSNは、Db2 for z/OSのログレコードシーケンス番号です、メンバーをまたいだ更新順序やpoint-in-time recoveryの停止点を扱うとき、RBAを主な根拠にしては表せないグループ全体の順序を示します、回復点の表記を環境に合わせて選びますという関係があり、この区別で確認する名称は「LRSN」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **LRSN**

    - 検証目的: 範囲整理の再始動ポイントについて、LRSN は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010111の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、範囲整理の再始動ポイントの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にLRSNを指定し、OSKB010111の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND LRSN
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM LRSN
    CASE OSKB010111
    SOURCE Db2 for z/OS
    ```

    LRSNとOSKB010111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010111を同じ出力で読み、範囲整理の再始動ポイントの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010111
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010111
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010111
    ```

    DSNV401IとOSKB010111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の LRSN と OSKB010111 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation



### RBA {#c07-i0367}
*分類: ログ・回復・再始動 > 再始動ポイント*  ・  難易度: 中級

RBAは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 非データ共用のDb2で、ログ上の特定位置まで表スペースを戻すため、停止点をバイト位置で指定します。この位置を表す考え方はどれですか。

    - A. 相対バイトアドレス ✅
    - B. ロール名
    - C. 索引ページサイズ
    - D. JDBC接続URL

    正解: **A** ／ 難易度: 中級

    **解説:** ログ内の相対的なバイト位置を使うため、Aが正解です。Bは権限管理で使う名前です。Cは索引やページセットの物理設計です。Dは分散接続のクライアント指定です。データ共用ではLRSNとの使い分けを確認します；背景にはログ位置を扱うRBAは、Db2 for z/OSのログ内のバイト位置を表す相対バイトアドレスです、非データ共用環境の回復点やログ範囲の照合で使われ、RECOVERのTORBA指定では復旧を止めるログ位置として扱われます、印刷出力では開始値や終了値と合わせて読みますという関係があり、この区別で確認する名称は「RBA」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **RBA**

    - 検証目的: 区切整理の再始動ポイントについて、RBA は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010110の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、区切整理の再始動ポイントの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にRBAを指定し、OSKB010110の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND RBA
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM RBA
    CASE OSKB010110
    SOURCE Db2 for z/OS
    ```

    RBAとOSKB010110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010110を同じ出力で読み、区切整理の再始動ポイントの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010110
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010110
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010110
    ```

    DSNV401IとOSKB010110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の RBA と OSKB010110 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation



### conditional restart control record {#c07-i0368}
*分類: ログ・回復・再始動 > 再始動ポイント*  ・  難易度: 中級

conditional restart control recordは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** システム全体のバックアップを戻した後、ログ適用の終点を指定してDb2を特定時点で再始動させる計画です。準備する制御情報はどれが該当しますか。

    - A. SQLCA
    - B. PLAN_TABLE
    - C. RUNSTATS PROFILE
    - D. 条件付き再始動の制御レコード ✅

    正解: **D** ／ 難易度: 中級

    **解説:** ログ適用範囲を制御する情報なので、Dが該当します。AはアプリケーションがSQLの戻り状態を保持する領域です。Bはアクセスパス説明結果を格納する表です。Cは統計収集の既定内容を保存します。再始動点の設定は回復手順全体の整合性に直結します；背景にはconditional restart control recordは、Db2 for z/OSの再始動ポイント設計で、条件付き再始動時のログ適用をどこまでに制限するかを示します、システム全体のバックアップから戻す場合やクローン環境を作る場合、ログ切り詰め点を誤ると復旧範囲が想定とずれます、設定値は事前に回復計画と照合しますという関係があり、この区別で確認する名称は「conditional」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting




## Db2 for z/OS > ログ・回復・再始動 > 障害時再始動

### restart after log error {#c07-i0369}
*分類: ログ・回復・再始動 > 障害時再始動*  ・  難易度: 中級

restart after log errorは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** Db2起動時にログ範囲とBSDS登録内容の不一致が疑われます。再始動前に優先して行うべき対応として最も自然なのはどれですか。

    - A. 統計を収集してアクセスパスを変える
    - B. ビュー定義を削除して再作成する
    - C. SQLJプロファイルをBINDする
    - D. BSDSとログ目録の整合を確認する ✅

    正解: **D** ／ 難易度: 中級

    **解説:** ログとBSDSの一致確認が先なので、Dが正解です。Aは性能やアクセスパスの作業です。Bはスキーマ定義の保守で、ログ障害の再始動対応ではありません。Cはアプリケーション開発資材の準備です。必要なら印刷結果を基に目録修正やBSDS回復へ進みます；背景には障害時再始動の対応で扱うrestart after log errorは、Db2 for z/OSのログデータセットやBSDS情報の不一致後に安全な起動へ戻す作業を指します、DSNJU004でBSDSの登録内容を確認し、必要に応じてDSNJU003やRECOVER BSDSで目録やコピー状態を整えます、原因を残したまま起動を繰り返さないことが大切ですという関係があり、この区別で確認する名称は「after」です。

    **出典:** Db2_zOS_Admin_Guide / Db2_zOS_Utility_Guide / Db2_zOS_Messages / Db2_zOS_Troubleshooting


??? note "検証手順（1件）"
    **restart after log error**

    - 検証目的: 順序整理の障害時再始動について、restart after log errorは、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010115の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、順序整理の障害時再始動の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にrestart after log を指定し、OSKB010115の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND restart after log 
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM restart after log 
    CASE OSKB010115
    SOURCE Db2 for z/OS
    ```

    restart after log とOSKB010115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010115を同じ出力で読み、順序整理の障害時再始動の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010115
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010115
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010115
    ```

    DSNV401IとOSKB010115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の restart after log  と OSKB010115 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Admin_Guide / Db2_zOS_Troubleshooting / Db2_zOS_Installation




## Db2 for z/OS > 基本概念

### Db2 サブシステム {#c07-i0370}
*分類: 基本概念*  ・  難易度: 初級

Db2 for z/OS の 基本概念で扱うDb2 サブシステムは、z/OS 上で SQL 要求、ロック、ログ、バッファ管理を受け持つ Db2 の実行単位です。アプリケーションは接続先のサブシステムまたはデータ共有グループを通じて表や索引にアクセスします。運用では起動状態、カタログ整合性、ログの健全性を合わせて確認します

**出典:** Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security


### データ共有グループ {#c07-i0371}
*分類: 基本概念*  ・  難易度: 中級

Db2 for z/OS の 基本概念で扱うデータ共有グループは、複数の Db2 メンバーが同じデータを共有して処理する Parallel Sysplex 上の構成です。Coupling Facility の構造とログ管理が前提になり、単一サブシステムよりも可用性とスケールを高めます。障害時はメンバー単位の状態とグループ全体の整合性を分けて見ます

**出典:** Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security

??? question "確認問題（1問）"
    **問題.** 展開確認のデータ共有グループでデータ共有グループの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. データ共有グループの出力を取らず展開確認のデータ共有グループの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 ✅
    - C. -DISPLAY THREAD(*)を省略して展開確認のデータ共有グループの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のデータ共有グループへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠ではデータ共有グループは「展開確認のデータ共有グループに関係する定義値と表示行を照合する展開確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡ではデータ共有グループの属性行と DSNV401I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出ではデータ共有グループを Db2 for z/OS の運用手順で確認し、初出名は展開確認初出です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（1件）"
    **データ共有グループ**

    - 検証目的: 展開確認のデータ共有グループについて、Db2 for z/OS の 基本概念で扱うデータ共有グループは、複数の Db2 メンバーが同じデータを共有して処理する Parallel Sysplex 上の構成です。Cに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD(*) を入力し、展開確認のデータ共有グループの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    ```

    COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にデータ共有グループを指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND データ共有グループ
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM データ共有グループ
    CASE OSKB010002
    SOURCE Db2 for z/OS
    ```

    データ共有グループとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010002を同じ出力で読み、展開確認のデータ共有グループの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010002
    -DISPLAY THREAD(*)
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010002
    ```

    DSNV401IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD(*) が画面・出力に表示されること
    ② ステップ2 の データ共有グループ と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security




## Db2 for z/OS > 基本概念・アーキテクチャ > 全体構造

### Db2カタログ {#c07-i0372}
*分類: 基本概念・アーキテクチャ > 全体構造*  ・  難易度: 初級

Db2カタログは、データベース、表、索引、パッケージ、権限などの定義情報を保持するシステム管理表群です。障害調査や定義確認では、カタログの内容がDb2側の現在の認識を示します

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? note "検証手順（1件）"
    **Db2カタログ**

    - 検証目的: 展開確認のカタログについて、Db2カタログは、データベース、表、索引、パッケージ、権限などの定義情報を保持するシステム管理表群です。障害調査や定義確認では、カタログの内容が Db2側の現在の認識を示しまに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、展開確認のカタログの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDb2カタログを指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND Db2カタログ
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM Db2カタログ
    CASE OSKB010002
    SOURCE Db2 for z/OS
    ```

    Db2カタログとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010002を同じ出力で読み、展開確認のカタログの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010002
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010002
    ```

    DSNV401IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の Db2カタログ と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation



### Db2サブシステム {#c07-i0373}
*分類: 基本概念・アーキテクチャ > 全体構造*  ・  難易度: 初級

Db2サブシステムは、z/OS上でSQL処理、ログ管理、ロック管理、分散接続などをまとめて提供するDb2の実行単位です。運用では起動状態、接続口、ログ資材、関連アドレス空間を合わせて確認します

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 構文確認のサブシステムに関係する Db2 サブシステムの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. -DISPLAY THREAD(*)の結果から対象行を抜き出し、構文確認の証跡として残す。 ✅
    - B. Db2 サブシステムの名称と担当者名のみを残して構文確認のサブシステムの表示本文を確認対象に含めない。
    - C. データベース管理以外の画面で構文確認のサブシステムを確認し同じ証跡として扱ったことにする。
    - D. DSNV401I の有無を見ず構文確認のサブシステムの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Db2 サブシステム は「Db2 サブシステムの用途をデータベース管理の表示で確認する構文確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では Db2 for z/OS の Db2 サブシステムと DSNV401I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Db2 サブシステムを Db2 for z/OS で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（2件）"
    **Db2サブシステム**

    - 検証目的: 構文確認のサブシステムについて、Db2サブシステムは、z/OS 上で SQL 処理、ログ管理、ロック管理、分散接続などをまとめて提供する Db2の実行単位です。運用では起動状態、接続口、ログ資材、関連アドレス空間に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、構文確認のサブシステムの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDb2サブシステムを指定し、OSKB010001の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND Db2サブシステム
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM Db2サブシステム
    CASE OSKB010001
    SOURCE Db2 for z/OS
    ```

    Db2サブシステムとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010001を同じ出力で読み、構文確認のサブシステムの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010001
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010001
    ```

    DSNV401IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の Db2サブシステム と OSKB010001 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

    ---

    **Db2 サブシステム**

    - 検証目的: 構文確認のサブシステムについて、Db2 for z/OS の 基本概念で扱う Db2 サブシステムは、z/OS 上で SQL 要求、ロック、ログ、バッファ管理を受け持つ Db2 の実行単位です。アプリケーシに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD(*) を入力し、構文確認のサブシステムの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    ```

    COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDb2 サブシステムを指定し、OSKB010001の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND Db2 サブシステム
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM Db2 サブシステム
    CASE OSKB010001
    SOURCE Db2 for z/OS
    ```

    Db2 サブシステムとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010001を同じ出力で読み、構文確認のサブシステムの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010001
    -DISPLAY THREAD(*)
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010001
    ```

    DSNV401IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD(*) が画面・出力に表示されること
    ② ステップ2 の Db2 サブシステム と OSKB010001 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security



### Db2ディレクトリ {#c07-i0374}
*分類: 基本概念・アーキテクチャ > 全体構造*  ・  難易度: 初級

Db2ディレクトリは、Db2が内部制御のために使うシステム領域です。通常の業務表のように直接操作する対象ではなく、カタログやログと合わせてDb2の基盤資材として保護します

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? note "検証手順（1件）"
    **Db2ディレクトリ**

    - 検証目的: 呼出確認のディレクトリについて、Db2ディレクトリは、Db2が内部制御のために使うシステム領域です。通常の業務表のように直接操作する対象ではなく、カタログやログと合わせて Db2の基盤資材として保護しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、呼出確認のディレクトリの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDb2ディレクトリを指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND Db2ディレクトリ
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM Db2ディレクトリ
    CASE OSKB010003
    SOURCE Db2 for z/OS
    ```

    Db2ディレクトリとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010003を同じ出力で読み、呼出確認のディレクトリの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010003
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010003
    ```

    DSNV401IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の Db2ディレクトリ と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation




## Db2 for z/OS > 基本概念・アーキテクチャ > 実行・連携基盤

### DDF概要 {#c07-i0375}
*分類: 基本概念・アーキテクチャ > 実行・連携基盤*  ・  難易度: 初級

DDFは、Db2 for z/OSへ分散接続を受け付けるための機能です。ポート、ロケーション名、DBAT、暗号化設定と結び付き、リモート・アプリケーションの接続可否に直接影響します

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? note "検証手順（1件）"
    **DDF 概要**

    - 検証目的: 出力確認の概要について、DDF は、Db2 for z/OS へ分散接続を受け付けるための機能です。ポート、ロケーション名、DBAT、暗号化設定と結び付き、リモート・アプリケーションの接続可否に直接影に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、出力確認の概要の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDDF 概要を指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DDF 概要
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DDF 概要
    CASE OSKB010008
    SOURCE Db2 for z/OS
    ```

    DDF 概要とOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010008を同じ出力で読み、出力確認の概要の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010008
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010008
    ```

    DSNV401IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DDF 概要 と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation



### Data Sharing概要 {#c07-i0376}
*分類: 基本概念・アーキテクチャ > 実行・連携基盤*  ・  難易度: 初級

Data Sharingは、複数のDb2メンバーが同じデータを共有する構成です。カップリング・ファシリティ、グループ・バッファー・プール、メンバー間ロックを含めて、単独Db2とは別の運用判断が必要になります

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 複数 member が同じ data を共有し、coupling facility の GBP や lock structure を使います。該当する構成はどれですか。

    - A. 単独catalog
    - B. 外部routine
    - C. SQLSTATE
    - D. 共有group構成 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 複数 member で data を共有する構成なので、D が適切です。A: 定義情報表の単独確認です。B: WLM で動く手続きです。C: SQLSTATE などの戻り状態です。GBP と lock structure の関係を確認します；背景には複数 member で Db2 を使う実行・連携基盤として、Data Sharing概要は group、member、coupling facility の関係を扱います、group buffer pool や lock structure を使い、複数 subsystem が同じ data を共有します、設計では GBP、IRLM、log、restart の関係を確認しますという関係があり、この区別で確認する名称は「Sharing」です。

    **出典:** Db2_zOS_Introduction.pdf p.231 / Db2_zOS_Introduction.pdf p.258 / Db2_zOS_Admin_Guide.pdf p.40 / Db2_zOS_Admin_Guide.pdf p.428 / Db2_zOS_Data_Sharing.pdf p.16 / Db2_zOS_Data_Sharing.pdf p.86 / Db2_zOS_Installation.pdf p.278 / Db2_zOS_Installation.pdf p.280 / Db2_zOS_Utility_Guide.pdf p.25 / Db2_zOS_Utility_Guide.pdf p.1068 / Db2_zOS_Troubleshooting.pdf p.287 / Db2_zOS_Admin_Guide.pdf p.648


??? note "検証手順（1件）"
    **Data Sharing概要**

    - 検証目的: 区切確認の概要について、Data Sharingは、複数の Db2メンバーが同じデータを共有する構成です。カップリング・ファシリティ、グループ・バッファー・プール、メンバー間ロックを含めて、単独 Dbに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、区切確認の概要の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にData Sharing概要を指定し、OSKB010010の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND Data Sharing概要
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM Data Sharing概要
    CASE OSKB010010
    SOURCE Db2 for z/OS
    ```

    Data Sharing概要とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010010を同じ出力で読み、区切確認の概要の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010010
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010010
    ```

    DSNV401IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の Data Sharing概要 と OSKB010010 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation



### Db2ログ概要 {#c07-i0377}
*分類: 基本概念・アーキテクチャ > 実行・連携基盤*  ・  難易度: 初級

Db2ログは、更新内容を記録し、再始動や回復で整合性を戻すための基盤資材です。アクティブログ、アーカイブログ、BSDSの関係を理解しておくと、障害時の復旧判断がしやすくなります

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 更新内容を記録し、restart や media recovery で変更を再適用できるようにします。見る仕組みはどれですか。

    - A. package cache
    - B. view定義
    - C. 更新記録基盤 ✅
    - D. DDF port

    正解: **C** ／ 難易度: 中級

    **解説:** 更新内容を記録して回復に使う基盤なので、C を選びます。A: package 実行の管理領域です。B: 仮想表の定義です。D: 分散接続の接続口です。active log と archive log の状態を見ます；背景には更新を保全する実行・連携基盤として、Db2ログ概要は active log、archive log、BSDS の役割をまとめて理解します、commit 済み変更の回復、restart、roll back、media recovery に必要な情報が log に残ります、運用では書き込み先、退避状況、log map を確認しますという関係があり、この区別で確認する名称は「ログ概要」です。

    **出典:** Db2_zOS_Introduction.pdf p.231 / Db2_zOS_Introduction.pdf p.258 / Db2_zOS_Admin_Guide.pdf p.40 / Db2_zOS_Admin_Guide.pdf p.428 / Db2_zOS_Data_Sharing.pdf p.16 / Db2_zOS_Data_Sharing.pdf p.86 / Db2_zOS_Installation.pdf p.278 / Db2_zOS_Installation.pdf p.280 / Db2_zOS_Utility_Guide.pdf p.25 / Db2_zOS_Utility_Guide.pdf p.1068 / Db2_zOS_Troubleshooting.pdf p.287 / Db2_zOS_Admin_Guide.pdf p.648


??? note "検証手順（1件）"
    **Db2ログ概要**

    - 検証目的: 条件確認のログ概要について、Db2ログは、更新内容を記録し、再始動や回復で整合性を戻すための基盤資材です。アクティブログ、アーカイブログ、BSDS の関係を理解しておくと、障害時の復旧判断がしやすくなりに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、条件確認のログ概要の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDb2ログ概要を指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND Db2ログ概要
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM Db2ログ概要
    CASE OSKB010009
    SOURCE Db2 for z/OS
    ```

    Db2ログ概要とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010009を同じ出力で読み、条件確認のログ概要の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010009
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010009
    ```

    DSNV401IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の Db2ログ概要 と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation



### IRLM {#c07-i0378}
*分類: 基本概念・アーキテクチャ > 実行・連携基盤*  ・  難易度: 初級

IRLMは、Db2 for z/OSの実行・連携基盤で用いるDb2のロック要求を管理するロック・マネージャーです。デッドロック、タイムアウト、待ち時間の調査では、Db2本体だけでなくIRLM側の状態も確認します。実行・連携基盤では、指定値と対象資源、実行時の出力を突き合わせて確認する。

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? note "検証手順（1件）"
    **IRLM**

    - 検証目的: 上書確認の実行・連携基盤について、IRLM は、Db2 for z/OS の実行・連携基盤で用いる Db2のロック要求を管理するロック・マネージャーです。デッドロック、タイムアウト、待ち時間の調査では、Db2本体に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、上書確認の実行・連携基盤の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にIRLMを指定し、OSKB010007の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND IRLM
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM IRLM
    CASE OSKB010007
    SOURCE Db2 for z/OS
    ```

    IRLMとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010007を同じ出力で読み、上書確認の実行・連携基盤の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010007
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010007
    ```

    DSNV401IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の IRLM と OSKB010007 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation




## Db2 for z/OS > 基本概念・アーキテクチャ > 記憶構造

### データベース {#c07-i0379}
*分類: 基本概念・アーキテクチャ > 記憶構造*  ・  難易度: 中級

データベースは、基本概念・アーキテクチャの中で記憶構造に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2全体像の部品として扱い、JCLやMVSアドレス空間一般へ広げないとは分けて扱います

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? question "確認問題（2問）"
    **問題.** table space や index space をまとめる論理的な入れ物を定義し、配下 object の管理単位にします。該当するものはどれですか。

    - A. 論理格納枠 ✅
    - B. SQL戻り値
    - C. WLM環境
    - D. 通信通知

    正解: **A** ／ 難易度: 中級

    **解説:** table space などをまとめる論理的な入れ物なので、A が合います。B: SQL 実行結果の値です。C: 外部 routine の実行先です。D: DDF などの message です。配下 object との関係を確認します；背景には記憶構造としてのデータベースは、table space や index space をまとめる Db2 の論理的な入れ物です、業務上の表そのものではなく、storage group や管理単位と結び付いて物理資源の割り当てに関係します、作成や削除では配下 object との関係を確認しますという関係があり、この区別で確認する名称は「データベース」です。

    **出典:** Db2_zOS_Introduction.pdf p.231 / Db2_zOS_Introduction.pdf p.258 / Db2_zOS_Admin_Guide.pdf p.40 / Db2_zOS_Admin_Guide.pdf p.428 / Db2_zOS_Data_Sharing.pdf p.16 / Db2_zOS_Data_Sharing.pdf p.86 / Db2_zOS_Installation.pdf p.278 / Db2_zOS_Installation.pdf p.280 / Db2_zOS_Utility_Guide.pdf p.25 / Db2_zOS_Utility_Guide.pdf p.1068 / Db2_zOS_Troubleshooting.pdf p.287 / Db2_zOS_Admin_Guide.pdf p.648

    ---

    **問題.** 呼出確認のデータベースでデータベース管理の運用確認を行います。データベースの根拠にできる作業はどれですか。

    - A. Db2 for z/OS と無関係な一覧で呼出確認のデータベースを確認した扱いにする。
    - B. DSNT360I の有無を確認せず呼出確認のデータベースを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. データベースの属性行を読まず呼出確認のデータベースの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠ではデータベースは「Db2 for z/OS でデータベースの扱いを記録する呼出確認項目」と-DISPLAY DATABASE(*) SPACENAM(*)または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡ではデータベースの表示結果と DSNT360I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料ではデータベースの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（2件）"
    **データベース**

    - 検証目的: 置換確認のデータベースについて、データベースは、基本概念・アーキテクチャの中で記憶構造に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2全体像に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、置換確認のデータベースの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にデータベースを指定し、OSKB010004の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND データベース
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM データベース
    CASE OSKB010004
    SOURCE Db2 for z/OS
    ```

    データベースとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010004を同じ出力で読み、置換確認のデータベースの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010004
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010004
    ```

    DSNV401IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の データベース と OSKB010004 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

    ---

    **データベース**

    - 検証目的: 呼出確認のデータベースについて、Db2 for z/OS の ストレージ構造で扱うデータベースは、Db2 のデータベースは、表スペースや索引スペースをまとめる論理的な入れ物です。業務上のアプリケーション単に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY DATABASE(*) SPACENAM(*)を実行し、DSNT360Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY DATABASE(*) SPACENAM(*) を入力し、呼出確認のデータベースの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY DATABASE(*) SPACENAM(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY DATABASE(*) SPACENAM(*)
    ```

    COMMAND INPUTに-DISPLAY DATABASE(*) SPACENAM(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にデータベースを指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND データベース
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM データベース
    CASE OSKB010003
    SOURCE Db2 for z/OS
    ```

    データベースとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNT360IとOSKB010003を同じ出力で読み、呼出確認のデータベースの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY DATABASE(*) SPACENAM(*)
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010003
    -DISPLAY DATABASE(*) SPACENAM(*)
    DSNT360I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010003
    ```

    DSNT360IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY DATABASE(*) SPACENAM(*) が画面・出力に表示されること
    ② ステップ2 の データベース と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の DSNT360I と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security



### 索引スペース {#c07-i0380}
*分類: 基本概念・アーキテクチャ > 記憶構造*  ・  難易度: 中級

索引スペースは、基本概念・アーキテクチャの中で記憶構造に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2全体像の部品として扱い、JCLやMVSアドレス空間一般へ広げないとは分けて扱います

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? question "確認問題（2問）"
    **問題.** index のページを格納し、表データとは別に REBUILD や COPY の対象として扱います。該当する構造はどれですか。

    - A. DDF thread
    - B. active log
    - C. 索引格納単位 ✅
    - D. SQLSTATE

    正解: **C** ／ 難易度: 中級

    **解説:** index のページを格納する構造なので、C が該当します。A: 分散接続の thread です。B: 現在書き込み中の log 資材です。D: SQL 実行結果の状態分類です。表側の格納単位と分けて確認します；背景には索引データを置く記憶構造として、索引スペースは index のページを格納します、表データとは別に管理され、access path、REBUILD INDEX、COPY、buffer pool 選択に関係します、障害時は table space と index space のどちらが対象かを切り分けますという関係があり、この区別で確認する名称は「索引スペース」です。

    **出典:** Db2_zOS_Introduction.pdf p.231 / Db2_zOS_Introduction.pdf p.258 / Db2_zOS_Admin_Guide.pdf p.40 / Db2_zOS_Admin_Guide.pdf p.428 / Db2_zOS_Data_Sharing.pdf p.16 / Db2_zOS_Data_Sharing.pdf p.86 / Db2_zOS_Installation.pdf p.278 / Db2_zOS_Installation.pdf p.280 / Db2_zOS_Utility_Guide.pdf p.25 / Db2_zOS_Utility_Guide.pdf p.1068 / Db2_zOS_Troubleshooting.pdf p.287 / Db2_zOS_Admin_Guide.pdf p.648

    ---

    **問題.** 終端確認の索引スペースに関係する索引スペースの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. -DISPLAY THREAD(*)で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 ✅
    - B. 索引スペースの名称と担当者名のみを残して終端確認の索引スペースの表示本文を確認対象に含めない。
    - C. データベース管理以外の画面で終端確認の索引スペースを確認し同じ証跡として扱ったことにする。
    - D. DSNV401I の有無を見ず終端確認の索引スペースの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では索引スペースは「索引スペースの用途をデータベース管理の表示で確認する終端確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では Db2 for z/OS の索引スペースと DSNV401I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では索引スペースを Db2 for z/OS で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（2件）"
    **索引スペース**

    - 検証目的: 探索確認の索引スペースについて、索引スペースは、基本概念・アーキテクチャの中で記憶構造に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2全体像に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、探索確認の索引スペースの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄に索引スペースを指定し、OSKB010006の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND 索引スペース
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM 索引スペース
    CASE OSKB010006
    SOURCE Db2 for z/OS
    ```

    索引スペースとOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010006を同じ出力で読み、探索確認の索引スペースの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010006
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010006
    ```

    DSNV401IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の 索引スペース と OSKB010006 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

    ---

    **索引スペース**

    - 検証目的: 終端確認の索引スペースについて、Db2 for z/OS の ストレージ構造で扱う索引スペースは、索引データを保持する Db2 の記憶構造です。索引の状態が悪いとアクセスパス、ユニーク制約、ユーティリティに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD(*) を入力し、終端確認の索引スペースの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    ```

    COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄に索引スペースを指定し、OSKB010005の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND 索引スペース
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM 索引スペース
    CASE OSKB010005
    SOURCE Db2 for z/OS
    ```

    索引スペースとOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010005を同じ出力で読み、終端確認の索引スペースの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010005
    -DISPLAY THREAD(*)
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010005
    ```

    DSNV401IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD(*) が画面・出力に表示されること
    ② ステップ2 の 索引スペース と OSKB010005 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security



### 表スペース {#c07-i0381}
*分類: 基本概念・アーキテクチャ > 記憶構造*  ・  難易度: 中級

表スペースは、基本概念・アーキテクチャの中で記憶構造に関わるDb2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2全体像の部品として扱い、JCLやMVSアドレス空間一般へ広げないとは分けて扱います

**出典:** Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

??? question "確認問題（1問）"
    **問題.** 置換確認の表スペースに関する表スペースの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. -DISPLAY THREAD(*)の結果を残さず置換確認の表スペースの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の表スペースの証跡として保存して根拠にする。
    - C. 表スペースの変更点を出力本文から切り離して置換確認の表スペースの承認欄のみ残す。
    - D. 同じ画面で対象行と DSNV401I を読み、置換確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では表スペースは「表スペースの状態と出力メッセージを結び付ける置換確認項目」と-DISPLAY THREAD(*)または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では表スペースの出力行と DSNV401I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では表スペースを Db2 for z/OS の確認記録に残し、対象名は置換確認対象です。

    **出典:** Db2_zOS_Command_Reference / Db2_zOS_Admin_Guide


??? note "検証手順（2件）"
    **表スペース**

    - 検証目的: 終端確認の表スペースについて、表スペースは、基本概念・アーキテクチャの中で記憶構造に関わる Db2技術項目です。役割、使いどころ、注意点、隣接項目との違い。一方で、隣接カテゴリの詳細説明。 Db2全体像のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、終端確認の表スペースの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄に表スペースを指定し、OSKB010005の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND 表スペース
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM 表スペース
    CASE OSKB010005
    SOURCE Db2 for z/OS
    ```

    表スペースとOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010005を同じ出力で読み、終端確認の表スペースの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010005
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010005
    ```

    DSNV401IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の 表スペース と OSKB010005 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Introduction / Db2_zOS_Admin_Guide / Db2_zOS_Installation

    ---

    **表スペース**

    - 検証目的: 置換確認の表スペースについて、Db2 for z/OS の ストレージ構造で扱う表スペースは、Db2 表データを格納する主要な記憶構造です。分割方式、ページサイズ、ロック粒度、ユーティリティ状態が性能とに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREAD(*)を実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD(*) を入力し、置換確認の表スペースの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    ```

    COMMAND INPUTに-DISPLAY THREAD(*)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄に表スペースを指定し、OSKB010004の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND 表スペース
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM 表スペース
    CASE OSKB010004
    SOURCE Db2 for z/OS
    ```

    表スペースとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010004を同じ出力で読み、置換確認の表スペースの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD(*)
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010004
    -DISPLAY THREAD(*)
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010004
    ```

    DSNV401IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD(*) が画面・出力に表示されること
    ② ステップ2 の 表スペース と OSKB010004 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2 13 for z / OS: Introduction to Db2 for z / OS / OS: Command Reference / OS: Administration Guide / OS: Managing Security




## Db2 for z/OS > 導入・移行・サブシステムパラメータ > サブシステム資材・初期化

### BSDS二重化 {#c07-i0382}
*分類: 導入・移行・サブシステムパラメータ > サブシステム資材・初期化*  ・  難易度: 中級

BSDS二重化は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** ログ目録を保護するため、BSDS2 DD を追加し RECOVER BSDS で2本構成を確立します。この作業は何ですか。

    - A. DDF情報更新
    - B. ルーチン検証
    - C. BSDS二重化 ✅
    - D. DSNHDECP作成

    正解: **C** ／ 難易度: 中級

    **解説:** bootstrap data setを2本構成にする作業に当たるため、Cが正解です。A: 分散接続情報をBSDSへ記録します。B: Db2提供ルーチンの検証です。D: DSNHDECP の作成であり、ログ目録の冗長化ではありません；背景にはDb2 のサブシステム資材として、BSDS二重化は bootstrap data set を2本構成にしてログ管理情報を保護します、追加時は DSN6LOGP の TWOBSDS を YES にし、起動プロシージャに BSDS2 DD を追加してから RECOVER BSDS で二重化を確立します、停止要否とバックアウト手順も確認しますという関係があり、この区別で確認する名称は「二重化」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891


??? note "検証手順（1件）"
    **BSDS 二重化**

    - 検証目的: 監査確認の二重化について、BSDS 二重化は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、監査確認の二重化の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にBSDS 二重化を指定し、OSKB010019の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND BSDS 二重化
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM BSDS 二重化
    CASE OSKB010019
    SOURCE Db2 for z/OS
    ```

    BSDS 二重化とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010019を同じ出力で読み、監査確認の二重化の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010019
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010019
    ```

    DSNV401IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の BSDS 二重化 と OSKB010019 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### DDF情報のBSDS更新 {#c07-i0383}
*分類: 導入・移行・サブシステムパラメータ > サブシステム資材・初期化*  ・  難易度: 中級

DDF情報のBSDS更新は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（2問）"
    **問題.** LOCATIONやTCP/IPポートなどの分散接続情報をBSDSへ記録し、DDF開始時の表示と一致するかを確認します。該当する作業はどれですか。

    - A. DSNTIARの呼び出し
    - B. RUNSTATSの実行
    - C. パッケージFREE
    - D. DSNJU003によるDDF通信レコード更新 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 分散接続の通信情報をBSDSに記録する作業なので、Dを選択します。誤答AはSQLCAをメッセージ化するルーチン呼び出し、誤答Bは統計収集です。誤答Cはパッケージ削除であり、LOCATIONやPORTをBSDSへ反映する作業ではありません；背景には分散接続情報を BSDS へ記録する導入作業が DDF 情報の BSDS 更新です、DSNJU003 の DDF statement は、サブシステムパラメータ周辺の反映で使います、LOCATION、PORT、RESPORT、IPNAME などを bootstrap data set に保存し、開始後は DSNL08x 系メッセージで同じ値が見えるかを確認しますという関係があり、この区別で確認する名称は「BSDS」です。

    **出典:** Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages

    ---

    **問題.** LOCATIONやPORTなどの分散接続情報を、DSNJU003のDDF statementでBSDSへ反映します。この作業はどれですか。

    - A. DSNTIJICバックアップ
    - B. DDF情報のBSDS更新 ✅
    - C. DSNHDECP再作成
    - D. CTHREAD変更

    正解: **B** ／ 難易度: 中級

    **解説:** 分散接続のcommunication recordをBSDSへ反映するため、Bが正解です。A: DSNTIJICによるcatalogとdirectoryのコピーです。C: 既定値ロードモジュールを作る処理です。D: システム実行時パラメータの変更で、DDF通信レコード更新とは別です；背景には分散接続のサブシステム資材として、DDF情報のBSDS更新は communication record を bootstrap data set へ記録する作業です、DSNTIJUL または DSNJU003 の DDF statement では、LOCATION、PORT、RESPORT、IPNAME などを反映します、開始後は DDF 表示や DSNL 系メッセージで値の一致を見ますという関係があり、この区別で確認する名称は「DDF」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891



### DSNHDECP {#c07-i0384}
*分類: 導入・移行・サブシステムパラメータ > サブシステム資材・初期化*  ・  難易度: 中級

DSNHDECPは、Db2サブシステム・パラメータ、導入資材、起動時反映に関わる項目です。DSNZPARMや導入ジョブとの関係を押さえ、変更がいつ有効になるかを確認します

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（2問）"
    **問題.** アプリケーションが参照するCCSIDなどの既定値を含み、サイトに合わせて作成されるロードモジュールを確認します。該当する資材はどれですか。

    - A. BSDSコピー
    - B. DSNDB07作業DB
    - C. DSNZPxxx
    - D. DSNHDECP ✅

    正解: **D** ／ 難易度: 中級

    **解説:** CCSIDなどを含むアプリケーション既定値の資材なので、Dが正解です。誤答Aはログ管理のbootstrap data set、誤答Bは作業ファイル用DBです。誤答Cはサブシステムパラメータ側のモジュールであり、用途が分かれます；背景にはアプリケーション既定を保持するロードモジュールが DSNHDECP です、導入・初期化作業では CCSID などのサイト固有値を反映した場合に、コンパイルや実行で参照するロードライブラリ連結も合わせて確認し、標準配布版との取り違えを防ぎますという関係があり、この区別で確認する名称は「DSNHDECP」です。

    **出典:** Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages

    ---

    **問題.** 既定CCSIDやSQL既定値をアプリケーションが参照できるよう、既定値資材を確認します。該当する資材はどれですか。

    - A. DSNHDECP ✅
    - B. DSNZPxxx
    - C. DDF通信レコード
    - D. active log

    正解: **A** ／ 難易度: 中級

    **解説:** 既定CCSIDやSQL実行時既定値を保持する資材に当たるため、Aが正解です。B: 起動時パラメータを入れる別資材です。C: BSDS内の分散接続情報です。D: ログ記録用データセットで、実行時の既定CCSIDとは役割が違います；背景にはDSNHDECP は、サブシステム資材・初期化で扱う application defaults load module です、導入ジョブ DSNTIJUA により、アプリケーションが参照する既定CCSIDやSQL実行時の既定値を持つ資材を作ります、配置先ライブラリの取り違えは起動や実行時エラーにつながりますという関係があり、この区別で確認する名称は「DSNHDECP」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891


??? note "検証手順（2件）"
    **DSNHDECP**

    - 検証目的: 復旧確認のサブシステム資材・初期化について、DSNHDECP は、Db2サブシステム・パラメータ、導入資材、起動時反映に関わる項目です。DSNZPARM や導入ジョブとの関係を押さえ、変更がいつ有効になるかを確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、復旧確認のサブシステム資材・初期化の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNHDECPを指定し、OSKB010018の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNHDECP
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNHDECP
    CASE OSKB010018
    SOURCE Db2 for z/OS
    ```

    DSNHDECPとOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010018を同じ出力で読み、復旧確認のサブシステム資材・初期化の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010018
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010018
    ```

    DSNV401IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNHDECP と OSKB010018 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

    ---

    **DSNHDECP**

    - 検証目的: 終端検査の導入・初期化・起動反映について、DSNHDECP は、Db2サブシステム・パラメータ、導入資材、起動時反映に関わる項目です。DSNZPARM や導入ジョブとの関係を押さえ、変更がいつ有効になるかを確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、終端検査の導入・初期化・起動反映の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNHDECPを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNHDECP
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNHDECP
    CASE OSKB020065
    SOURCE Db2 for z/OS
    ```

    DSNHDECPとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB020065を同じ出力で読み、終端検査の導入・初期化・起動反映の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB020065
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB020065
    ```

    DSNV401IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNHDECP と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Performance p.216



### DSNZPxxx {#c07-i0385}
*分類: 導入・移行・サブシステムパラメータ > サブシステム資材・初期化*  ・  難易度: 中級

DSNZPxxxは、Db2サブシステム・パラメータ、導入資材、起動時反映に関わる項目です。DSNZPARMや導入ジョブとの関係を押さえ、変更がいつ有効になるかを確認します

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（2問）"
    **問題.** 導入CLISTで選んだ多数の実行時パラメータをロードモジュール化し、Db2起動時に読み込ませます。確認する成果物はどれですか。

    - A. ZPARMロードモジュール ✅
    - B. アプリケーション既定値モジュール
    - C. DDF通信レコード更新
    - D. ユーティリティ終了コマンド

    正解: **A** ／ 難易度: 中級

    **解説:** 導入パネル値から作られるサブシステム側の資材なので、Aを選びます。誤答Bはアプリケーション既定値の資材です。誤答CはBSDS内の分散接続情報を書き換える作業で、誤答Dは実行中ユーティリティを終える運用操作です；背景には実行時設定を格納するロードモジュールとして DSNZPxxx を使います、導入ジョブ DSNTIJUZ が DSN6ARVP や DSN6SPRM などを展開してこの資材を作成し、起動JCLの ZPARM 指定で Db2 に読み込ませますという関係があり、この区別で確認する名称は「DSNZPxxx」です。

    **出典:** Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages

    ---

    **問題.** 実行時パラメータを格納し、Db2開始時に PARM 指定で読み込まれるロードモジュールを確認します。対象資材はどれですか。

    - A. DSNHMCID
    - B. DSNHDECP
    - C. DSNZPxxx ✅
    - D. BSDSコピー

    正解: **C** ／ 難易度: 中級

    **解説:** サブシステムパラメータモジュールなので、Cを選びます。A: メッセージ変換用CCSID資材です。B: アプリケーションの既定値を持つ別資材です。D: ログ管理に関わるbootstrap data setのコピーで、起動時パラメータ本体ではありません；背景にはDb2 起動時に読み込む DSNZPxxx は、サブシステム資材・初期化で扱うパラメータ用の実行資材です、DSNTIJUZ が DSN6ARVP、DSN6FAC、DSN6GRP、DSN6LOGP、DSN6SPRM、DSN6SYSP を展開して作成します、起動JCLや START DB2 PARM の指定と一致させますという関係があり、この区別で確認する名称は「DSNZPxxx」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891


??? note "検証手順（1件）"
    **DSNZPxxx**

    - 検証目的: 警告確認のサブシステム資材・初期化について、DSNZPxxxは、Db2サブシステム・パラメータ、導入資材、起動時反映に関わる項目です。DSNZPARM や導入ジョブとの関係を押さえ、変更がいつ有効になるかを確認しますに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、警告確認のサブシステム資材・初期化の確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNZPxxxを指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNZPxxx
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNZPxxx
    CASE OSKB010017
    SOURCE Db2 for z/OS
    ```

    DSNZPxxxとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010017を同じ出力で読み、警告確認のサブシステム資材・初期化の根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010017
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010017
    ```

    DSNV401IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNZPxxx と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### active log初期化 {#c07-i0386}
*分類: 導入・移行・サブシステムパラメータ > サブシステム資材・初期化*  ・  難易度: 中級

active log初期化は、Db2のログ、BSDS、再始動、回復位置の判断に関わる項目です。障害時には、どの資材が根拠になり、どの時点まで戻せるかを説明できることが重要です

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** 新しいログデータセットをオンライン投入する前に、DSNJLOGF で事前整形して初回書き込み時の遅延を避けます。選ぶ作業名はどれですか。

    - A. catalog image copy
    - B. DDF再同期
    - C. DSNZPxxx再リンク
    - D. ログ事前フォーマット ✅

    正解: **D** ／ 難易度: 中級

    **解説:** ログデータセットを先に整える作業なので、Dが該当します。A: catalog/directoryの退避であり、ログ整形ではありません。B: 分散接続の再同期系の話です。C: ZPARMを再リンクする作業で、ログデータセット整形とは別です；背景にはサブシステム資材・初期化の作業として、active log初期化では新しい active log data set を定義し、DSNJLOGF などで事前整形します、Db2 が初回書き込み時に制御域を整形する遅延を避けるため、オンライン投入前にpreformatしておきます、DSNTIJL1からDSNTIJLxの範囲はログ番号と単一/二重ログ構成で変わりますという関係があり、この区別で確認する名称は「active」です。

    **出典:** Db2_zOS_Installation.pdf p.397 / Db2_zOS_Installation.pdf p.476 / Db2_zOS_Installation.pdf p.523 / Db2_zOS_Installation.pdf p.596 / Db2_zOS_Installation.pdf p.731 / Db2_zOS_Installation.pdf p.830 / Db2_zOS_Admin_Guide.pdf p.645 / Db2_zOS_Utility_Guide.pdf p.891




## Db2 for z/OS > 導入・移行・サブシステムパラメータ > 導入・移行ジョブ

### DSNTIJUA {#c07-i0387}
*分類: 導入・移行・サブシステムパラメータ > 導入・移行ジョブ*  ・  難易度: 中級

DSNTIJUAは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（2問）"
    **問題.** サイト固有のアプリケーション既定値を反映し、プログラムが使う既定モジュールを用意します。該当する導入ジョブはどれですか。

    - A. DSNTIJIC
    - B. DSNTIJSO
    - C. DSNTIJUA ✅
    - D. DSNTIJRV

    正解: **C** ／ 難易度: 中級

    **解説:** サイト固有の既定値を作る導入ジョブとして、Cを選択します。誤答Aは導入後検証やサンプル確認で見かけるジョブです。誤答BはSQL処理確認の系統で、誤答Dは移行検証の文脈で扱います。作成先モジュールも見ます；背景には既定値モジュールを準備する導入ジョブが DSNTIJUA です、このサブシステムパラメータ周辺の作業では、DSNHDECP に入るアプリケーション既定値や文字コード関連の値をサイトに合わせ、コンパイルや接続プログラムが参照できる形にしますという関係があり、この区別で確認する名称は「DSNTIJUA」です。

    **出典:** Db2_zOS_Installation / Db2_zOS_Command_Reference / Db2_zOS_Utility_Guide / Db2_zOS_Messages

    ---

    **問題.** アプリケーションが参照する既定値ロードモジュールを作り、DSNHDECP の内容を準備します。該当するジョブはどれですか。

    - A. DSNTIJUZ
    - B. DSNTIJUL
    - C. DSNTIJUM
    - D. DSNTIJUA ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 既定値ロードモジュールを作るため、Dが該当します。誤答Aはサブシステムパラメータモジュールです。誤答BはDDF関連のBSDS更新で、誤答Cはオフラインメッセージ用CCSIDを扱います。参照するロードライブラリも見ます；背景にはDSNTIJUA は、導入・移行ジョブ群で application defaults load module を作成します、アプリケーションが参照する既定CCSIDやSQL実行時の既定は、DSNHDECP に入ります、起動時設定用の DSNZPxxx と混同すると、確認すべきロードモジュールを取り違えますという関係があり、この区別で確認する名称は「DSNTIJUA」です。

    **出典:** Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542


??? note "検証手順（1件）"
    **DSNTIJUA**

    - 検証目的: 優先確認の導入・移行ジョブについて、DSNTIJUA は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、優先確認の導入・移行ジョブの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJUAを指定し、OSKB010012の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJUA
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJUA
    CASE OSKB010012
    SOURCE Db2 for z/OS
    ```

    DSNTIJUAとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010012を同じ出力で読み、優先確認の導入・移行ジョブの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010012
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010012
    ```

    DSNV401IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJUA と OSKB010012 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### DSNTIJUL {#c07-i0388}
*分類: 導入・移行・サブシステムパラメータ > 導入・移行ジョブ*  ・  難易度: 中級

DSNTIJULは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** DDF関連の通信情報を BSDS に反映するため、DSNJU003 を走らせる導入ジョブを選びます。該当するジョブはどれですか。

    - A. DSNTIJUA
    - B. DSNTIJUL ✅
    - C. DSNTIJUZ
    - D. DSNTIJUM

    正解: **B** ／ 難易度: 中級

    **解説:** 分散接続情報をBSDSへ更新するジョブなので、Bを選びます。A: アプリケーション既定値の資材作成になります。誤答Cはサブシステムパラメータモジュールを作り、誤答DはDSNHMCIDを定義するジョブです；背景にはDSNTIJUL は、導入・移行ジョブ群の中で DSNJU003 を実行し、DDF 関連情報を BSDS へ更新します、LOCATION、PORT、RESPORT、IPNAME などの通信情報は、DDF 開始時の表示と突き合わせます、データ共有では、必要なメンバー単位で実行対象を確認しますという関係があり、この区別で確認する名称は「DSNTIJUL」です。

    **出典:** Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542


??? note "検証手順（1件）"
    **DSNTIJUL**

    - 検証目的: 記録確認の導入・移行ジョブについて、DSNTIJUL は、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: Db2 Commandまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。
    - セッション環境: Db2 Commandで-DISPLAY THREADを実行し、DSNV401Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はDb2 Commandのコマンド入力画面です。COMMAND INPUT ===> に -DISPLAY THREAD を入力し、記録確認の導入・移行ジョブの確認表示へ進みます。
    操作（入力）:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command)
    COMMAND INPUT ===> -DISPLAY THREAD
    ```

    COMMAND INPUTに-DISPLAY THREADが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はDb2 Commandの表示結果です。FIND欄にDSNTIJULを指定し、OSKB010013の対象行を見つけます。
    操作（入力）:
    ```text
    (Db2 Command Result)
    COMMAND INPUT ===> FIND DSNTIJUL
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (Db2 Command Result)
    ITEM DSNTIJUL
    CASE OSKB010013
    SOURCE Db2 for z/OS
    ```

    DSNTIJULとOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はDb2 Commandの詳細表示です。DSNV401IとOSKB010013を同じ出力で読み、記録確認の導入・移行ジョブの根拠を記録します。
    操作（入力）:
    ```text
    (Db2 Command Detail)
    COMMAND INPUT ===> -DISPLAY THREAD
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    DSN COMMAND RESPONSE OSKB010013
    -DISPLAY THREAD
    DSNV401I - DISPLAY REPORT FOLLOWS -
    DSNV402I - ACTIVE THREADS -
    NAME     ST A REQ ID OSKB010013
    ```

    DSNV401IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> -DISPLAY THREAD が画面・出力に表示されること
    ② ステップ2 の DSNTIJUL と OSKB010013 が画面・出力に表示されること
    ③ ステップ3 の DSNV401I と OSKB010013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages



### DSNTIJUM {#c07-i0389}
*分類: 導入・移行・サブシステムパラメータ > 導入・移行ジョブ*  ・  難易度: 中級

DSNTIJUMは、Db2メッセージ、SQLCODE、SQLSTATE、理由コード、診断資料に関わる項目です。障害解析では、コードの意味だけでなく、直前の操作、対象資源、追加で採る証跡を結び付けます

**出典:** Db2_zOS_Installation / Db2_zOS_Codes / Db2_zOS_Messages

??? question "確認問題（1問）"
    **問題.** Db2アプリケーションやユーティリティのメッセージ変換に使う DSNHMCID を定義します。実行するジョブはどれですか。

    - A. DSNTIJUM ✅
    - B. DSNTIJUZ
    - C. DSNTIJUL
    - D. DSNTIJUA

    正解: **A** ／ 難易度: 中級

    **解説:** offline message generator CCSID module を作るジョブなので、Aを選びます。誤答BはDSNZPxxxの作成です。誤答CはDDF関連BSDS更新で、誤答Dはアプリケーション既定値ロードモジュールを作ります；背景にはDSNTIJUM は、導入・移行ジョブ群の中で DSNHMCID を定義します、この資材は、Db2 アプリケーションやユーティリティが行うメッセージ変換に必要な offline message generator CCSID module です、SMP/E の GENASM 連携を使う場合は、無効化された DSNTIMQ ステップの扱いも別途確認しますという関係があり、この区別で確認する名称は「DSNTIJUM」です。

    **出典:** Db2_zOS_Installation.pdf p.442 / Db2_zOS_Installation.pdf p.765 / Db2_zOS_Installation.pdf p.444 / Db2_zOS_Codes.pdf p.623 / Db2_zOS_Messages.pdf p.542


