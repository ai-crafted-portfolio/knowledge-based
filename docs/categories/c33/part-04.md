---
search:
  exclude: true
---

# UNIX System Services (USS) — 詳細 (4/4)

[← UNIX System Services (USS) の概要へ戻る](index.md)


## UNIX System Services (USS) > USS 認可

### OMVS セグメント {#c33-i0186}
*分類: USS 認可*  ・  難易度: 中級

OMVS セグメントは、UNIX System Services (USS)のUSS 認可で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 区切追跡のセグメントで OMVS セグメントの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. OMVS セグメントの出力を取らず区切追跡のセグメントの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 ✅
    - C. OMVS ls -alを省略して区切追跡のセグメントの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡のセグメントへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡のセグメントの正解は B です。OMVS セグメント は説明欄の「区切追跡のセグメントに関係する定義値と表示行を照合する項目」と OMVS ls -alまたは該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡のセグメントの証跡を読む担当者は、OMVS セグメントの属性行と BPXM018I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡のセグメントは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡のセグメントは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡のセグメントは戻り値や記録番号に寄り、BPXM018I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡のセグメントは別カテゴリの確認を流用しており、OMVS セグメントの根拠にならないため区切追跡ではありません。区切追跡のセグメントに出る OMVS セグメントは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **OMVS セグメント**

    - 検証目的: 記録整理のセグメントについて、OMVS セグメントは、UNIX System Services (USS)の USS 認可で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010113の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでOMVS ls -alを実行し、BPXM018Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に OMVS ls -al を入力し、記録整理のセグメントの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> OMVS ls -al
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> OMVS ls -al
    ```

    COMMAND INPUTにOMVS ls -alが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にOMVS セグメントを指定し、OSKB010113の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND OMVS セグメント
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM OMVS セグメント
    CASE OSKB010113
    SOURCE z/OS UNIX System Services
    ```

    OMVS セグメントとOSKB010113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXM018IとOSKB010113を同じ出力で読み、記録整理のセグメントの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> OMVS ls -al
    CASE OSKB010113
    → Enter を押す
    ```

    画面・出力:
    ```text
    OMVS SHELL SESSION OSKB010113
    $ ls -al /u/oskb
    -rw-r--r-- 1 OSKB SYS1 128 OSKB010113.txt
    BPXM018I shell command completed
    ```

    BPXM018IとOSKB010113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OMVS ls -al が画面・出力に表示されること
    ② ステップ2 の OMVS セグメント と OSKB010113 が画面・出力に表示されること
    ③ ステップ3 の BPXM018I と OSKB010113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### UID 0 = superuser {#c33-i0187}
*分類: USS 認可*  ・  難易度: 中級

UID 0 = superuserは、UNIX System Services (USS)のUSS 認可で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 条件追跡の認可に関係する UID 0 = superuserの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. UID 0 = superuserの名称と担当者名のみを残して条件追跡の認可の表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で条件追跡の認可を確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず条件追跡の認可の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の認可の正解は A です。UID 0 = superuser は説明欄の「UID 0 = superuserの用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の認可に関連して、z/OS UNIX System Servicesでは UID 0 = superuserの表示属性と BPXO043I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の認可は対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の認可は名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の認可は別カテゴリの確認を流用しており、UID 0 = superuserの根拠にならないため条件追跡ではありません。 D: 条件追跡の認可は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため条件追跡ではありません。条件追跡の認可で使う UID 0 = superuserという用語は UNIX System Services (USS)で扱う確認対象であり、用語名は条件追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **UID 0 = superuser**

    - 検証目的: 優先整理の認可について、UID 0 = superuserは、UNIX System Services (USS)の USS 認可で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010112の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、優先整理の認可の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にUID 0 = superuserを指定し、OSKB010112の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND UID 0 = superuser
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM UID 0 = superuser
    CASE OSKB010112
    SOURCE z/OS UNIX System Services
    ```

    UID 0 = superuserとOSKB010112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB010112を同じ出力で読み、優先整理の認可の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB010112
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB010112 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB010112.ZFS
    PATH=/u/oskb/oskb010112
    ```

    BPXO043IとOSKB010112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の UID 0 = superuser と OSKB010112 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB010112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### UNIXPRIV クラス {#c33-i0188}
*分類: USS 認可*  ・  難易度: 中級

UNIXPRIV クラスは、UNIX System Services (USS)のUSS 認可で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出確認のクラスでユーエスエスの運用確認を行います。UNIXPRIV クラスの根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で呼出確認のクラスを確認した扱いにする。
    - B. BPXO043I の有無を確認せず呼出確認のクラスを正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 ✅
    - D. UNIXPRIV クラスの属性行を読まず呼出確認のクラスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認のクラスの正解は C です。UNIXPRIV クラス は説明欄の「z/OS UNIX System Servicesで UNIXPRIV クラスの扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認のクラスを受け取る担当者は、UNIXPRIV クラスの表示結果と BPXO043I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認のクラスは別カテゴリの確認を流用しており、UNIXPRIV クラスの根拠にならないため呼出確認ではありません。 B: 呼出確認のクラスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認のクラスは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認のクラスが示す UNIXPRIV クラスは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **UNIXPRIV クラス**

    - 検証目的: 値域整理のクラスについて、UNIXPRIV クラスは、UNIX System Services (USS)の USS 認可で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010116の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、値域整理のクラスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にUNIXPRIV クラスを指定し、OSKB010116の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND UNIXPRIV クラス
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM UNIXPRIV クラス
    CASE OSKB010116
    SOURCE z/OS UNIX System Services
    ```

    UNIXPRIV クラスとOSKB010116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB010116を同じ出力で読み、値域整理のクラスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB010116
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB010116 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB010116.ZFS
    PATH=/u/oskb/oskb010116
    ```

    BPXO043IとOSKB010116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の UNIXPRIV クラス と OSKB010116 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB010116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### extattr コマンド {#c33-i0189}
*分類: USS 認可*  ・  難易度: 中級

extattr コマンドは、UNIX System Services (USS)のUSS 認可で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 比較確認のコマンドでextattr コマンドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. extattr コマンドの出力を取らず比較確認のコマンドの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して比較確認のコマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認のコマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較確認のコマンドの正解は B です。extattr コマンド は説明欄の「比較確認のコマンドに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認のコマンドの証跡を読む担当者は、extattr コマンドの属性行と BPXO043I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認のコマンドは対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認のコマンドは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため比較確認ではありません。 D: 比較確認のコマンドは別カテゴリの確認を流用しており、extattr コマンドの根拠にならないため比較確認ではありません。比較確認のコマンドに出るextattr コマンドは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は比較確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **extattr コマンド**

    - 検証目的: 上書確認のコマンドについて、extattr コマンドは、UNIX System Services (USS)の USS 認可で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、上書確認のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にextattr コマンドを指定し、OSKB020007の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND extattr コマンド
    CASE OSKB020007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM extattr コマンド
    CASE OSKB020007
    SOURCE z/OS UNIX System Services
    ```

    extattr コマンドとOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020007を同じ出力で読み、上書確認のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020007
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020007 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020007.ZFS
    PATH=/u/oskb/oskb020007
    ```

    BPXO043IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の extattr コマンド と OSKB020007 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## UNIX System Services (USS) > automount

### FILESYSTYPE AUTOMNT {#c33-i0190}
*分類: automount*  ・  難易度: 中級

FILESYSTYPE AUTOMNTは、UNIX System Services (USS)のautomountで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 復旧照合のユーエスエスで FILESYSTYPE AUTOMNT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FILESYSTYPE AUTOMNT の出力を取らず復旧照合のユーエスエスの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して復旧照合のユーエスエスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のユーエスエスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合のユーエスエスの正解は B です。FILESYSTYPE AUTOMNT は説明欄の「復旧照合のユーエスエスに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のユーエスエスの証跡を読む担当者は、FILESYSTYPE AUTOMNT の属性行と BPXO043I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のユーエスエスは別カテゴリの確認を流用しており、FILESYSTYPE AUTOMNT の根拠にならないため復旧照合ではありません。復旧照合のユーエスエスに出る FILESYSTYPE AUTOMNT は UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **FILESYSTYPE AUTOMNT**

    - 検証目的: 範囲照合のユーエスエスについて、FILESYSTYPE AUTOMNT は、UNIX System Services (USS)のautomountで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、範囲照合のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にFILESYSTYPE AUTOMNを指定し、OSKB020031の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND FILESYSTYPE AUTOMN
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM FILESYSTYPE AUTOMN
    CASE OSKB020031
    SOURCE z/OS UNIX System Services
    ```

    FILESYSTYPE AUTOMNとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020031を同じ出力で読み、範囲照合のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020031
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020031 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020031.ZFS
    PATH=/u/oskb/oskb020031
    ```

    BPXO043IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の FILESYSTYPE AUTOMN と OSKB020031 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### auto.master / mapfile {#c33-i0191}
*分類: automount*  ・  難易度: 中級

auto.master / mapfileは、UNIX System Services (USS)のautomountで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 変更照合のユーエスエスに関するauto.master / mapfileの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず変更照合のユーエスエスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のユーエスエスの証跡として保存して根拠にする。
    - C. auto.master / mapfileの変更点を出力本文から切り離して変更照合のユーエスエスの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合のユーエスエスの正解は D です。auto.master / mapfile は説明欄の「auto.master / mapfileの状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のユーエスエスに関する記録は、auto.master / mapfileの出力行と BPXO043I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため変更照合ではありません。 B: 変更照合のユーエスエスは別カテゴリの確認を流用しており、auto.master / mapfileの根拠にならないため変更照合ではありません。 C: 変更照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のユーエスエスで記録するauto.master / mapfileはz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **auto.master / mapfile**

    - 検証目的: 記録照合のユーエスエスについて、auto.master / mapfileは、UNIX System Services (USS)のautomountで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、記録照合のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にauto.master / mapfを指定し、OSKB020033の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND auto.master / mapf
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM auto.master / mapf
    CASE OSKB020033
    SOURCE z/OS UNIX System Services
    ```

    auto.master / mapfとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020033を同じ出力で読み、記録照合のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020033
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020033 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020033.ZFS
    PATH=/u/oskb/oskb020033
    ```

    BPXO043IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の auto.master / mapf と OSKB020033 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### automount コマンド {#c33-i0192}
*分類: automount*  ・  難易度: 中級

automount コマンドは、UNIX System Services (USS)のautomountで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 監査照合のコマンドでユーエスエスの運用確認を行います。automount コマンドの根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で監査照合のコマンドを確認した扱いにする。
    - B. BPXO043I の有無を確認せず監査照合のコマンドを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査照合の記録として扱う。 ✅
    - D. automount コマンドの属性行を読まず監査照合のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合のコマンドの正解は C です。automount コマンド は説明欄の「z/OS UNIX System Servicesでautomount コマンドの扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のコマンドを受け取る担当者は、automount コマンドの表示結果と BPXO043I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のコマンドは別カテゴリの確認を流用しており、automount コマンドの根拠にならないため監査照合ではありません。 B: 監査照合のコマンドは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため監査照合ではありません。 C: 監査照合のコマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のコマンドが示すautomount コマンドは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **automount コマンド**

    - 検証目的: 優先照合のコマンドについて、automount コマンドは、UNIX System Services (USS)のautomountで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、優先照合のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にautomount コマンドを指定し、OSKB020032の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND automount コマンド
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM automount コマンド
    CASE OSKB020032
    SOURCE z/OS UNIX System Services
    ```

    automount コマンドとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020032を同じ出力で読み、優先照合のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020032
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020032 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020032.ZFS
    PATH=/u/oskb/oskb020032
    ```

    BPXO043IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の automount コマンド と OSKB020032 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### アイドル時 UNMOUNT {#c33-i0193}
*分類: automount*  ・  難易度: 中級

アイドル時 UNMOUNTは、UNIX System Services (USS)のautomountで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 構文追跡のアイドル時に関係するアイドル時 UNMOUNT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 ✅
    - B. アイドル時 UNMOUNT の名称と担当者名のみを残して構文追跡のアイドル時の表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で構文追跡のアイドル時を確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず構文追跡のアイドル時の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文追跡のアイドル時の正解は A です。アイドル時 UNMOUNT は説明欄の「アイドル時 UNMOUNT の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のアイドル時に関連して、z/OS UNIX System Servicesではアイドル時 UNMOUNT の表示属性と BPXO043I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のアイドル時は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のアイドル時は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のアイドル時は別カテゴリの確認を流用しており、アイドル時 UNMOUNT の根拠にならないため構文追跡ではありません。 D: 構文追跡のアイドル時は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため構文追跡ではありません。構文追跡のアイドル時で使うアイドル時 UNMOUNT という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は構文追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **アイドル時 UNMOUNT**

    - 検証目的: 比較照合のアイドル時について、アイドル時 UNMOUNT は、UNIX System Services (USS)のautomountで機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、比較照合のアイドル時の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にアイドル時 UNMOUNTを指定し、OSKB020034の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND アイドル時 UNMOUNT
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM アイドル時 UNMOUNT
    CASE OSKB020034
    SOURCE z/OS UNIX System Services
    ```

    アイドル時 UNMOUNTとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020034を同じ出力で読み、比較照合のアイドル時の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020034
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020034 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020034.ZFS
    PATH=/u/oskb/oskb020034
    ```

    BPXO043IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の アイドル時 UNMOUNT と OSKB020034 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## UNIX System Services (USS) > syscall

### _BPX_JOBNAME {#c33-i0194}
*分類: syscall*  ・  難易度: 中級

_BPX_JOBNAMEは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference


### _BPX_SHAREAS {#c33-i0195}
*分類: syscall*  ・  難易度: 中級

_BPX_SHAREASは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（2問）"
    **問題.** 優先照合のユーエスエスに関する_BPX_SHAREAS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず優先照合のユーエスエスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合のユーエスエスの証跡として保存して根拠にする。
    - C. _BPX_SHAREAS の変更点を出力本文から切り離して優先照合のユーエスエスの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合のユーエスエスの正解は D です。_BPX_SHAREAS は説明欄の「_BPX_SHAREAS の状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のユーエスエスに関する記録は、_BPX_SHAREAS の出力行と BPXO043I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため優先照合ではありません。 B: 優先照合のユーエスエスは別カテゴリの確認を流用しており、_BPX_SHAREAS の根拠にならないため優先照合ではありません。 C: 優先照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のユーエスエスで記録する_BPX_SHAREAS はz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices

    ---

    **問題.** 条件追跡の環境変数に関係する_BPX_SHAREAS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 ✅
    - B. _BPX_SHAREAS の名称と担当者名のみを残して条件追跡の環境変数の表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で条件追跡の環境変数を確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず条件追跡の環境変数の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡の環境変数の正解は A です。_BPX_SHAREAS は説明欄の「_BPX_SHAREAS の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の環境変数に関連して、z/OS UNIX System Servicesでは_BPX_SHAREAS の表示属性と BPXO043I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の環境変数は対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の環境変数は名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の環境変数は別カテゴリの確認を流用しており、_BPX_SHAREAS の根拠にならないため条件追跡ではありません。 D: 条件追跡の環境変数は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため条件追跡ではありません。条件追跡の環境変数で使う_BPX_SHAREAS という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は条件追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（2件）"
    **_BPX_SHAREAS**

    - 検証目的: 順序検査のユーエスエスについて、_BPX_SHAREAS は、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、順序検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に_BPX_SHAREASを指定し、OSKB020075の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND _BPX_SHAREAS
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM _BPX_SHAREAS
    CASE OSKB020075
    SOURCE z/OS UNIX System Services
    ```

    _BPX_SHAREASとOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020075を同じ出力で読み、順序検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020075
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020075 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020075.ZFS
    PATH=/u/oskb/oskb020075
    ```

    BPXO043IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の _BPX_SHAREAS と OSKB020075 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

    ---

    **_BPX_SHAREAS**

    - 検証目的: 優先判定の環境変数について、_BPX_SHAREAS は、UNIX System Services (USS)の USS 環境変数で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020092の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、優先判定の環境変数の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に_BPX_SHAREASを指定し、OSKB020092の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND _BPX_SHAREAS
    CASE OSKB020092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM _BPX_SHAREAS
    CASE OSKB020092
    SOURCE z/OS UNIX System Services
    ```

    _BPX_SHAREASとOSKB020092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020092を同じ出力で読み、優先判定の環境変数の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020092
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020092 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020092.ZFS
    PATH=/u/oskb/oskb020092
    ```

    BPXO043IとOSKB020092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の _BPX_SHAREAS と OSKB020092 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### exec {#c33-i0196}
*分類: syscall*  ・  難易度: 中級

execは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 探索照合のユーエスエスでexecの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. execの出力を取らず探索照合のユーエスエスの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して探索照合のユーエスエスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のユーエスエスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合のユーエスエスの正解は B です。exec は説明欄の「探索照合のユーエスエスに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のユーエスエスの証跡を読む担当者は、execの属性行と BPXO043I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため探索照合ではありません。 D: 探索照合のユーエスエスは別カテゴリの確認を流用しており、execの根拠にならないため探索照合ではありません。探索照合のユーエスエスに出るexecは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **exec**

    - 検証目的: 条件検査のユーエスエスについて、execは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、条件検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にexecを指定し、OSKB020069の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND exec
    CASE OSKB020069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM exec
    CASE OSKB020069
    SOURCE z/OS UNIX System Services
    ```

    execとOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020069を同じ出力で読み、条件検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020069
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020069 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020069.ZFS
    PATH=/u/oskb/oskb020069
    ```

    BPXO043IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の exec と OSKB020069 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### fork {#c33-i0197}
*分類: syscall*  ・  難易度: 中級

forkは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 置換照合のユーエスエスに関するforkの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず置換照合のユーエスエスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のユーエスエスの証跡として保存して根拠にする。
    - C. forkの変更点を出力本文から切り離して置換照合のユーエスエスの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合のユーエスエスの正解は D です。fork は説明欄の「forkの状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のユーエスエスに関する記録は、forkの出力行と BPXO043I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため置換照合ではありません。 B: 置換照合のユーエスエスは別カテゴリの確認を流用しており、forkの根拠にならないため置換照合ではありません。 C: 置換照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のユーエスエスで記録するforkはz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **fork**

    - 検証目的: 上書検査のユーエスエスについて、forkは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、上書検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にforkを指定し、OSKB020067の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND fork
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM fork
    CASE OSKB020067
    SOURCE z/OS UNIX System Services
    ```

    forkとOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020067を同じ出力で読み、上書検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020067
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020067 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020067.ZFS
    PATH=/u/oskb/oskb020067
    ```

    BPXO043IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の fork と OSKB020067 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### kill {#c33-i0198}
*分類: syscall*  ・  難易度: 中級

killは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference


### oepidproc {#c33-i0199}
*分類: syscall*  ・  難易度: 中級

oepidprocは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 範囲照合のユーエスエスでユーエスエスの運用確認を行います。oepidprocの根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で範囲照合のユーエスエスを確認した扱いにする。
    - B. BPXO043I の有無を確認せず範囲照合のユーエスエスを正常終了として記録する。
    - C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 ✅
    - D. oepidprocの属性行を読まず範囲照合のユーエスエスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合のユーエスエスの正解は C です。oepidproc は説明欄の「z/OS UNIX System Servicesでoepidprocの扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のユーエスエスを受け取る担当者は、oepidprocの表示結果と BPXO043I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のユーエスエスは別カテゴリの確認を流用しており、oepidprocの根拠にならないため範囲照合ではありません。 B: 範囲照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のユーエスエスが示すoepidprocは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **oepidproc**

    - 検証目的: 比較検査のユーエスエスについて、oepidprocは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、比較検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にoepidprocを指定し、OSKB020074の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND oepidproc
    CASE OSKB020074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM oepidproc
    CASE OSKB020074
    SOURCE z/OS UNIX System Services
    ```

    oepidprocとOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020074を同じ出力で読み、比較検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020074
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020074 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020074.ZFS
    PATH=/u/oskb/oskb020074
    ```

    BPXO043IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の oepidproc と OSKB020074 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### open/read/write/close {#c33-i0200}
*分類: syscall*  ・  難易度: 中級

open/read/write/closeは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 区切照合のユーエスエスでopen/read/write/closeの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. open/read/write/closeの出力を取らず区切照合のユーエスエスの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して区切照合のユーエスエスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合のユーエスエスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合のユーエスエスの正解は B です。open/read/write/close は説明欄の「区切照合のユーエスエスに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のユーエスエスの証跡を読む担当者は、open/read/write/closeの属性行と BPXO043I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため区切照合ではありません。 D: 区切照合のユーエスエスは別カテゴリの確認を流用しており、open/read/write/closeの根拠にならないため区切照合ではありません。区切照合のユーエスエスに出るopen/read/write/closeは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **open/read/write/close**

    - 検証目的: 記録検査のユーエスエスについて、open/read/write/closeは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、記録検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にopen/read/write/clを指定し、OSKB020073の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND open/read/write/cl
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM open/read/write/cl
    CASE OSKB020073
    SOURCE z/OS UNIX System Services
    ```

    open/read/write/clとOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020073を同じ出力で読み、記録検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020073
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020073 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020073.ZFS
    PATH=/u/oskb/oskb020073
    ```

    BPXO043IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の open/read/write/cl と OSKB020073 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### ptrace {#c33-i0201}
*分類: syscall*  ・  難易度: 上級

ptraceは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 上書照合のユーエスエスでユーエスエスの運用確認を行います。ptraceの根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で上書照合のユーエスエスを確認した扱いにする。
    - B. BPXO043I の有無を確認せず上書照合のユーエスエスを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書照合の記録として扱う。 ✅
    - D. ptraceの属性行を読まず上書照合のユーエスエスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合のユーエスエスの正解は C です。ptrace は説明欄の「z/OS UNIX System Servicesでptraceの扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のユーエスエスを受け取る担当者は、ptraceの表示結果と BPXO043I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のユーエスエスは別カテゴリの確認を流用しており、ptraceの根拠にならないため上書照合ではありません。 B: 上書照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため上書照合ではありません。 C: 上書照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のユーエスエスが示すptraceは出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **ptrace**

    - 検証目的: 区切検査のユーエスエスについて、ptraceは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、区切検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にptraceを指定し、OSKB020070の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ptrace
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ptrace
    CASE OSKB020070
    SOURCE z/OS UNIX System Services
    ```

    ptraceとOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020070を同じ出力で読み、区切検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020070
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020070 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020070.ZFS
    PATH=/u/oskb/oskb020070
    ```

    BPXO043IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の ptrace と OSKB020070 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### spawn {#c33-i0202}
*分類: syscall*  ・  難易度: 中級

spawnは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 終端照合のユーエスエスに関係するspawnの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 ✅
    - B. spawnの名称と担当者名のみを残して終端照合のユーエスエスの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で終端照合のユーエスエスを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず終端照合のユーエスエスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合のユーエスエスの正解は A です。spawn は説明欄の「spawnの用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合のユーエスエスに関連して、z/OS UNIX System Servicesではspawnの表示属性と BPXO043I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合のユーエスエスは別カテゴリの確認を流用しており、spawnの根拠にならないため終端照合ではありません。 D: 終端照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため終端照合ではありません。終端照合のユーエスエスで使うspawnという用語は UNIX System Services (USS)で扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **spawn**

    - 検証目的: 出力検査のユーエスエスについて、spawnは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、出力検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にspawnを指定し、OSKB020068の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND spawn
    CASE OSKB020068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM spawn
    CASE OSKB020068
    SOURCE z/OS UNIX System Services
    ```

    spawnとOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020068を同じ出力で読み、出力検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020068
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020068 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020068.ZFS
    PATH=/u/oskb/oskb020068
    ```

    BPXO043IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の spawn と OSKB020068 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### waitpid {#c33-i0203}
*分類: syscall*  ・  難易度: 中級

waitpidは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 条件照合のユーエスエスに関係するwaitpidの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. waitpidの名称と担当者名のみを残して条件照合のユーエスエスの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で条件照合のユーエスエスを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず条件照合のユーエスエスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合のユーエスエスの正解は A です。waitpid は説明欄の「waitpidの用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のユーエスエスに関連して、z/OS UNIX System Servicesではwaitpidの表示属性と BPXO043I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のユーエスエスは別カテゴリの確認を流用しており、waitpidの根拠にならないため条件照合ではありません。 D: 条件照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため条件照合ではありません。条件照合のユーエスエスで使うwaitpidという用語は UNIX System Services (USS)で扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **waitpid**

    - 検証目的: 優先検査のユーエスエスについて、waitpidは、UNIX System Services (USS)のsyscallで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、優先検査のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にwaitpidを指定し、OSKB020072の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND waitpid
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM waitpid
    CASE OSKB020072
    SOURCE z/OS UNIX System Services
    ```

    waitpidとOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020072を同じ出力で読み、優先検査のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020072
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020072 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020072.ZFS
    PATH=/u/oskb/oskb020072
    ```

    BPXO043IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の waitpid と OSKB020072 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## UNIX System Services (USS) > zFS / HFS

### Compatibility Mode Aggregate {#c33-i0204}
*分類: zFS / HFS*  ・  難易度: 中級

Compatibility Mode Aggregateは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 監査確認のユーエスエスでユーエスエスの運用確認を行います。Compatibility Mode Aggregateの根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で監査確認のユーエスエスを確認した扱いにする。
    - B. BPXO043I の有無を確認せず監査確認のユーエスエスを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査確認の記録として扱う。 ✅
    - D. Compatibility Mode Aggregateの属性行を読まず監査確認のユーエスエスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認のユーエスエスの正解は C です。Compatibility Mode Aggregate は説明欄の「z/OS UNIX System Servicesで Compatibility Mode Aggregateの扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のユーエスエスを受け取る担当者は、Compatibility Mode Aggregateの表示結果と BPXO043I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のユーエスエスは別カテゴリの確認を流用しており、Compatibility Mode Aggregateの根拠にならないため監査確認ではありません。 B: 監査確認のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため監査確認ではありません。 C: 監査確認のユーエスエスは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のユーエスエスが示す Compatibility Mode Aggregateは出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **Compatibility Mode Aggregate**

    - 検証目的: 優先確認のユーエスエスについて、Compatibility Mode Aggregateは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、優先確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCompatibility Modeを指定し、OSKB020012の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Compatibility Mode
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Compatibility Mode
    CASE OSKB020012
    SOURCE z/OS UNIX System Services
    ```

    Compatibility ModeとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020012を同じ出力で読み、優先確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020012
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020012 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020012.ZFS
    PATH=/u/oskb/oskb020012
    ```

    BPXO043IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の Compatibility Mode と OSKB020012 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### HFS → zFS 移行 {#c33-i0205}
*分類: zFS / HFS*  ・  難易度: 中級

HFS → zFS 移行は、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 条件照合のから 移行に関係する HFS から zFS 移行の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 ✅
    - B. HFS から zFS 移行の名称と担当者名のみを残して条件照合のから 移行の表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で条件照合のから 移行を確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず条件照合のから 移行の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合のから 移行の正解は A です。HFS から zFS 移行 は説明欄の「HFS から zFS 移行の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のから 移行に関連して、z/OS UNIX System Servicesでは HFS から zFS 移行の表示属性と BPXO043I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のから 移行は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のから 移行は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のから 移行は別カテゴリの確認を流用しており、HFS から zFS 移行の根拠にならないため条件照合ではありません。 D: 条件照合のから 移行は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため条件照合ではありません。条件照合のから 移行で使う HFS から zFS 移行という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は条件照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices



### HFS と zFS の関係 {#c33-i0206}
*分類: zFS / HFS*  ・  難易度: 中級

HFS と zFS の関係は、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 順序確認のと の関係でユーエスエスの運用確認を行います。HFS と zFS の関係の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で順序確認のと の関係を確認した扱いにする。
    - B. BPXO043I の有無を確認せず順序確認のと の関係を正常終了として記録する。
    - C. 説明欄と実出力を照合し、順序確認の記録として扱う。 ✅
    - D. HFS と zFS の関係の属性行を読まず順序確認のと の関係の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認のと の関係の正解は C です。HFS と zFS の関係 は説明欄の「z/OS UNIX System Servicesで HFS と zFS の関係の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のと の関係を受け取る担当者は、HFS と zFS の関係の表示結果と BPXO043I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のと の関係は別カテゴリの確認を流用しており、HFS と zFS の関係の根拠にならないため順序確認ではありません。 B: 順序確認のと の関係は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため順序確認ではありません。 C: 順序確認のと の関係は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のと の関係は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のと の関係が示す HFS と zFS の関係は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **HFS と zFS の関係**

    - 検証目的: 出力確認のと の関係について、HFS と zFS の関係は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、出力確認のと の関係の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にHFS と zFS の関係を指定し、OSKB020008の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND HFS と zFS の関係
    CASE OSKB020008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM HFS と zFS の関係
    CASE OSKB020008
    SOURCE z/OS UNIX System Services
    ```

    HFS と zFS の関係とOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020008を同じ出力で読み、出力確認のと の関係の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020008
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020008 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020008.ZFS
    PATH=/u/oskb/oskb020008
    ```

    BPXO043IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の HFS と zFS の関係 と OSKB020008 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### HFS データセット {#c33-i0207}
*分類: zFS / HFS*  ・  難易度: 中級

HFS データセットは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 値域確認のデータセットに関する HFS データセットの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず値域確認のデータセットの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のデータセットの証跡として保存して根拠にする。
    - C. HFS データセットの変更点を出力本文から切り離して値域確認のデータセットの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域確認のデータセットの正解は D です。HFS データセット は説明欄の「HFS データセットの状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認のデータセットに関する記録は、HFS データセットの出力行と BPXO043I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認のデータセットは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため値域確認ではありません。 B: 値域確認のデータセットは別カテゴリの確認を流用しており、HFS データセットの根拠にならないため値域確認ではありません。 C: 値域確認のデータセットは名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認のデータセットは対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認のデータセットで記録する HFS データセットはz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **HFS データセット**

    - 検証目的: 条件確認のデータセットについて、HFS データセットは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020009の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、条件確認のデータセットの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にHFS データセットを指定し、OSKB020009の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND HFS データセット
    CASE OSKB020009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM HFS データセット
    CASE OSKB020009
    SOURCE z/OS UNIX System Services
    ```

    HFS データセットとOSKB020009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020009を同じ出力で読み、条件確認のデータセットの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020009
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020009 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020009.ZFS
    PATH=/u/oskb/oskb020009
    ```

    BPXO043IとOSKB020009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の HFS データセット と OSKB020009 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### IOEAGFMT ユーティリティ {#c33-i0208}
*分類: zFS / HFS*  ・  難易度: 中級

IOEAGFMT ユーティリティは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 展開照合のユーティリティで IOEAGFMT ユーティリティの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IOEAGFMT ユーティリティの出力を取らず展開照合のユーティリティの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して展開照合のユーティリティの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のユーティリティへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合のユーティリティの正解は B です。IOEAGFMT ユーティリティ は説明欄の「展開照合のユーティリティに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合のユーティリティの証跡を読む担当者は、IOEAGFMT ユーティリティの属性行と BPXO043I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合のユーティリティは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合のユーティリティは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため展開照合ではありません。 D: 展開照合のユーティリティは別カテゴリの確認を流用しており、IOEAGFMT ユーティリティの根拠にならないため展開照合ではありません。展開照合のユーティリティに出る IOEAGFMT ユーティリティは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **IOEAGFMT ユーティリティ**

    - 検証目的: 順序確認のユーティリティについて、IOEAGFMT ユーティリティは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、順序確認のユーティリティの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIOEAGFMT ユーティリティを指定し、OSKB020015の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IOEAGFMT ユーティリティ
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IOEAGFMT ユーティリティ
    CASE OSKB020015
    SOURCE z/OS UNIX System Services
    ```

    IOEAGFMT ユーティリティとOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020015を同じ出力で読み、順序確認のユーティリティの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020015
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020015 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020015.ZFS
    PATH=/u/oskb/oskb020015
    ```

    BPXO043IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の IOEAGFMT ユーティリティ と OSKB020015 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### IOEFSPRC アドレス空間 {#c33-i0209}
*分類: zFS / HFS*  ・  難易度: 中級

IOEFSPRC アドレス空間は、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出照合のアドレス空間でユーエスエスの運用確認を行います。IOEFSPRC アドレス空間の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で呼出照合のアドレス空間を確認した扱いにする。
    - B. BPXO043I の有無を確認せず呼出照合のアドレス空間を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 ✅
    - D. IOEFSPRC アドレス空間の属性行を読まず呼出照合のアドレス空間の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合のアドレス空間の正解は C です。IOEFSPRC アドレス空間 は説明欄の「z/OS UNIX System Servicesで IOEFSPRC アドレス空間の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のアドレス空間を受け取る担当者は、IOEFSPRC アドレス空間の表示結果と BPXO043I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のアドレス空間は別カテゴリの確認を流用しており、IOEFSPRC アドレス空間の根拠にならないため呼出照合ではありません。 B: 呼出照合のアドレス空間は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のアドレス空間は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のアドレス空間は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のアドレス空間が示す IOEFSPRC アドレス空間は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **IOEFSPRC アドレス空間**

    - 検証目的: 値域確認のアドレス空間について、IOEFSPRC アドレス空間は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、値域確認のアドレス空間の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIOEFSPRC アドレス空間を指定し、OSKB020016の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IOEFSPRC アドレス空間
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IOEFSPRC アドレス空間
    CASE OSKB020016
    SOURCE z/OS UNIX System Services
    ```

    IOEFSPRC アドレス空間とOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020016を同じ出力で読み、値域確認のアドレス空間の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020016
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020016 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020016.ZFS
    PATH=/u/oskb/oskb020016
    ```

    BPXO043IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の IOEFSPRC アドレス空間 と OSKB020016 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### Multi-File System Aggregate {#c33-i0210}
*分類: zFS / HFS*  ・  難易度: 中級

Multi-File System Aggregateは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 変更確認のユーエスエスに関する Multi-File System Aggregateの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず変更確認のユーエスエスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のユーエスエスの証跡として保存して根拠にする。
    - C. Multi-File System Aggregateの変更点を出力本文から切り離して変更確認のユーエスエスの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認のユーエスエスの正解は D です。Multi-File System Aggregate は説明欄の「Multi-File System Aggregateの状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のユーエスエスに関する記録は、Multi-File System Aggregateの出力行と BPXO043I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため変更確認ではありません。 B: 変更確認のユーエスエスは別カテゴリの確認を流用しており、Multi-File System Aggregateの根拠にならないため変更確認ではありません。 C: 変更確認のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のユーエスエスは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のユーエスエスで記録する Multi-File System Aggregateはz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **Multi-File System Aggregate**

    - 検証目的: 記録確認のユーエスエスについて、Multi-File System Aggregateは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、記録確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMulti-File System を指定し、OSKB020013の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Multi-File System 
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Multi-File System 
    CASE OSKB020013
    SOURCE z/OS UNIX System Services
    ```

    Multi-File System とOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020013を同じ出力で読み、記録確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020013
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020013 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020013.ZFS
    PATH=/u/oskb/oskb020013
    ```

    BPXO043IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の Multi-File System  と OSKB020013 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS Aggregate {#c33-i0211}
*分類: zFS / HFS*  ・  難易度: 中級

zFS Aggregateは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 復旧確認のユーエスエスでzFS Aggregateの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. zFS Aggregateの出力を取らず復旧確認のユーエスエスの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して復旧確認のユーエスエスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のユーエスエスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認のユーエスエスの正解は B です。zFS Aggregate は説明欄の「復旧確認のユーエスエスに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認のユーエスエスの証跡を読む担当者は、zFS Aggregateの属性行と BPXO043I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認のユーエスエスは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認のユーエスエスは別カテゴリの確認を流用しており、zFS Aggregateの根拠にならないため復旧確認ではありません。復旧確認のユーエスエスに出るzFS Aggregateは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS Aggregate**

    - 検証目的: 範囲確認のユーエスエスについて、zFS Aggregateは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、範囲確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS Aggregateを指定し、OSKB020011の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS Aggregate
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS Aggregate
    CASE OSKB020011
    SOURCE z/OS UNIX System Services
    ```

    zFS AggregateとOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020011を同じ出力で読み、範囲確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020011
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020011 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020011.ZFS
    PATH=/u/oskb/oskb020011
    ```

    BPXO043IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS Aggregate と OSKB020011 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS CONFIG {#c33-i0212}
*分類: zFS / HFS*  ・  難易度: 中級

zFS CONFIGは、UNIX System Services (USS)のzFS / HFSで構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 出力照合のユーエスエスに関するzFS CONFIG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず出力照合のユーエスエスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合のユーエスエスの証跡として保存して根拠にする。
    - C. zFS CONFIG の変更点を出力本文から切り離して出力照合のユーエスエスの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力照合のユーエスエスの正解は D です。zFS CONFIG は説明欄の「zFS CONFIG の状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のユーエスエスに関する記録は、zFS CONFIG の出力行と BPXO043I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため出力照合ではありません。 B: 出力照合のユーエスエスは別カテゴリの確認を流用しており、zFS CONFIG の根拠にならないため出力照合ではありません。 C: 出力照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のユーエスエスで記録するzFS CONFIG はz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS CONFIG**

    - 検証目的: 構文照合のユーエスエスについて、zFS CONFIG は、UNIX System Services (USS)のzFS / HFS で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、構文照合のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS CONFIGを指定し、OSKB020021の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS CONFIG
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS CONFIG
    CASE OSKB020021
    SOURCE z/OS UNIX System Services
    ```

    zFS CONFIGとOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020021を同じ出力で読み、構文照合のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020021
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020021 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020021.ZFS
    PATH=/u/oskb/oskb020021
    ```

    BPXO043IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS CONFIG と OSKB020021 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS GROW {#c33-i0213}
*分類: zFS / HFS*  ・  難易度: 中級

zFS GROWは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 探索照合のユーエスエスでzFS GROW の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. zFS GROW の出力を取らず探索照合のユーエスエスの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して探索照合のユーエスエスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合のユーエスエスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合のユーエスエスの正解は B です。zFS GROW は説明欄の「探索照合のユーエスエスに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のユーエスエスの証跡を読む担当者は、zFS GROW の属性行と BPXO043I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため探索照合ではありません。 D: 探索照合のユーエスエスは別カテゴリの確認を流用しており、zFS GROW の根拠にならないため探索照合ではありません。探索照合のユーエスエスに出るzFS GROW は UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS GROW**

    - 検証目的: 監査確認のユーエスエスについて、zFS GROW は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、監査確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS GROWを指定し、OSKB020019の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS GROW
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS GROW
    CASE OSKB020019
    SOURCE z/OS UNIX System Services
    ```

    zFS GROWとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020019を同じ出力で読み、監査確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020019
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020019 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020019.ZFS
    PATH=/u/oskb/oskb020019
    ```

    BPXO043IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS GROW と OSKB020019 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS QUIESCE {#c33-i0214}
*分類: zFS / HFS*  ・  難易度: 中級

zFS QUIESCEは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 置換照合のユーエスエスに関するzFS QUIESCE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず置換照合のユーエスエスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合のユーエスエスの証跡として保存して根拠にする。
    - C. zFS QUIESCE の変更点を出力本文から切り離して置換照合のユーエスエスの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換照合のユーエスエスの正解は D です。zFS QUIESCE は説明欄の「zFS QUIESCE の状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のユーエスエスに関する記録は、zFS QUIESCE の出力行と BPXO043I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため置換照合ではありません。 B: 置換照合のユーエスエスは別カテゴリの確認を流用しており、zFS QUIESCE の根拠にならないため置換照合ではありません。 C: 置換照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のユーエスエスで記録するzFS QUIESCE はz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS QUIESCE**

    - 検証目的: 警告確認のユーエスエスについて、zFS QUIESCE は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、警告確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS QUIESCEを指定し、OSKB020017の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS QUIESCE
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS QUIESCE
    CASE OSKB020017
    SOURCE z/OS UNIX System Services
    ```

    zFS QUIESCEとOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020017を同じ出力で読み、警告確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020017
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020017 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020017.ZFS
    PATH=/u/oskb/oskb020017
    ```

    BPXO043IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS QUIESCE と OSKB020017 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS SHRINK {#c33-i0215}
*分類: zFS / HFS*  ・  難易度: 中級

zFS SHRINKは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 上書照合のユーエスエスでユーエスエスの運用確認を行います。zFS SHRINK の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で上書照合のユーエスエスを確認した扱いにする。
    - B. BPXO043I の有無を確認せず上書照合のユーエスエスを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書照合の記録として扱う。 ✅
    - D. zFS SHRINK の属性行を読まず上書照合のユーエスエスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合のユーエスエスの正解は C です。zFS SHRINK は説明欄の「z/OS UNIX System ServicesでzFS SHRINK の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のユーエスエスを受け取る担当者は、zFS SHRINK の表示結果と BPXO043I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のユーエスエスは別カテゴリの確認を流用しており、zFS SHRINK の根拠にならないため上書照合ではありません。 B: 上書照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため上書照合ではありません。 C: 上書照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のユーエスエスが示すzFS SHRINK は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS SHRINK**

    - 検証目的: 変更確認のユーエスエスについて、zFS SHRINK は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、変更確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS SHRINKを指定し、OSKB020020の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS SHRINK
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS SHRINK
    CASE OSKB020020
    SOURCE z/OS UNIX System Services
    ```

    zFS SHRINKとOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020020を同じ出力で読み、変更確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020020
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020020 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020020.ZFS
    PATH=/u/oskb/oskb020020
    ```

    BPXO043IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS SHRINK と OSKB020020 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS UNQUIESCE {#c33-i0216}
*分類: zFS / HFS*  ・  難易度: 中級

zFS UNQUIESCEは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 終端照合のユーエスエスに関係するzFS UNQUIESCE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 ✅
    - B. zFS UNQUIESCE の名称と担当者名のみを残して終端照合のユーエスエスの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で終端照合のユーエスエスを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず終端照合のユーエスエスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合のユーエスエスの正解は A です。zFS UNQUIESCE は説明欄の「zFS UNQUIESCE の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合のユーエスエスに関連して、z/OS UNIX System ServicesではzFS UNQUIESCE の表示属性と BPXO043I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合のユーエスエスは別カテゴリの確認を流用しており、zFS UNQUIESCE の根拠にならないため終端照合ではありません。 D: 終端照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため終端照合ではありません。終端照合のユーエスエスで使うzFS UNQUIESCE という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は終端照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS UNQUIESCE**

    - 検証目的: 復旧確認のユーエスエスについて、zFS UNQUIESCE は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、復旧確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS UNQUIESCEを指定し、OSKB020018の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS UNQUIESCE
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS UNQUIESCE
    CASE OSKB020018
    SOURCE z/OS UNIX System Services
    ```

    zFS UNQUIESCEとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020018を同じ出力で読み、復旧確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020018
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020018 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020018.ZFS
    PATH=/u/oskb/oskb020018
    ```

    BPXO043IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS UNQUIESCE と OSKB020018 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zFS バッキング {#c33-i0217}
*分類: zFS / HFS*  ・  難易度: 中級

zFS バッキングは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のバッキングに関係するzFS バッキングの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 ✅
    - B. zFS バッキングの名称と担当者名のみを残して警告確認のバッキングの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で警告確認のバッキングを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず警告確認のバッキングの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認のバッキングの正解は A です。zFS バッキング は説明欄の「zFS バッキングの用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のバッキングに関連して、z/OS UNIX System ServicesではzFS バッキングの表示属性と BPXO043I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のバッキングは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のバッキングは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のバッキングは別カテゴリの確認を流用しており、zFS バッキングの根拠にならないため警告確認ではありません。 D: 警告確認のバッキングは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため警告確認ではありません。警告確認のバッキングで使うzFS バッキングという用語は UNIX System Services (USS)で扱う確認対象であり、用語名は警告確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zFS バッキング**

    - 検証目的: 区切確認のバッキングについて、zFS バッキングは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、区切確認のバッキングの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzFS バッキングを指定し、OSKB020010の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zFS バッキング
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zFS バッキング
    CASE OSKB020010
    SOURCE z/OS UNIX System Services
    ```

    zFS バッキングとOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020010を同じ出力で読み、区切確認のバッキングの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020010
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020010 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020010.ZFS
    PATH=/u/oskb/oskb020010
    ```

    BPXO043IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zFS バッキング と OSKB020010 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zfsadm define / format {#c33-i0218}
*分類: zFS / HFS*  ・  難易度: 中級

zfsadm define / formatは、UNIX System Services (USS)のzFS / HFSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 構文照合のユーエスエスに関係するzfsadm define / formatの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 ✅
    - B. zfsadm define / formatの名称と担当者名のみを残して構文照合のユーエスエスの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で構文照合のユーエスエスを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず構文照合のユーエスエスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合のユーエスエスの正解は A です。zfsadm define / format は説明欄の「zfsadm define / formatの用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のユーエスエスに関連して、z/OS UNIX System Servicesではzfsadm define / formatの表示属性と BPXO043I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のユーエスエスは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のユーエスエスは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のユーエスエスは別カテゴリの確認を流用しており、zfsadm define / formatの根拠にならないため構文照合ではありません。 D: 構文照合のユーエスエスは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため構文照合ではありません。構文照合のユーエスエスで使うzfsadm define / formatという用語は UNIX System Services (USS)で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zfsadm define / format**

    - 検証目的: 比較確認のユーエスエスについて、zfsadm define / formatは、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、比較確認のユーエスエスの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzfsadm define / foを指定し、OSKB020014の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zfsadm define / fo
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zfsadm define / fo
    CASE OSKB020014
    SOURCE z/OS UNIX System Services
    ```

    zfsadm define / foとOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020014を同じ出力で読み、比較確認のユーエスエスの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020014
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020014 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020014.ZFS
    PATH=/u/oskb/oskb020014
    ```

    BPXO043IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zfsadm define / fo と OSKB020014 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## UNIX System Services (USS) > オープンソース on USS

### Perl on z/OS {#c33-i0219}
*分類: オープンソース on USS*  ・  難易度: 中級

Perl on z/OSは、UNIX System Services (USS)のオープンソース on USSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 置換追跡のオープンソースに関する Perl on z/OS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず置換追跡のオープンソースの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のオープンソースの証跡として保存して根拠にする。
    - C. Perl on z/OS の変更点を出力本文から切り離して置換追跡のオープンソースの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡のオープンソースの正解は D です。Perl on z/OS は説明欄の「Perl on z/OS の状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のオープンソースに関する記録は、Perl on z/OS の出力行と BPXO043I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のオープンソースは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のオープンソースは別カテゴリの確認を流用しており、Perl on z/OS の根拠にならないため置換追跡ではありません。 C: 置換追跡のオープンソースは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のオープンソースは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のオープンソースで記録する Perl on z/OS はz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **Perl on z/OS**

    - 検証目的: 上書判定のオープンソースについて、Perl on z/OS は、UNIX System Services (USS)のオープンソース on USS で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020087の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、上書判定のオープンソースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPerl on z/OSを指定し、OSKB020087の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Perl on z/OS
    CASE OSKB020087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Perl on z/OS
    CASE OSKB020087
    SOURCE z/OS UNIX System Services
    ```

    Perl on z/OSとOSKB020087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020087を同じ出力で読み、上書判定のオープンソースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020087
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020087 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020087.ZFS
    PATH=/u/oskb/oskb020087
    ```

    BPXO043IとOSKB020087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の Perl on z/OS と OSKB020087 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### Python on z/OS {#c33-i0220}
*分類: オープンソース on USS*  ・  難易度: 中級

Python on z/OSは、UNIX System Services (USS)のオープンソース on USSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出追跡のオープンソースでユーエスエスの運用確認を行います。Python on z/OS の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で呼出追跡のオープンソースを確認した扱いにする。
    - B. BPXO043I の有無を確認せず呼出追跡のオープンソースを正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 ✅
    - D. Python on z/OS の属性行を読まず呼出追跡のオープンソースの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡のオープンソースの正解は C です。Python on z/OS は説明欄の「z/OS UNIX System Servicesで Python on z/OS の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のオープンソースを受け取る担当者は、Python on z/OS の表示結果と BPXO043I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のオープンソースは別カテゴリの確認を流用しており、Python on z/OS の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のオープンソースは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のオープンソースは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のオープンソースは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のオープンソースが示す Python on z/OS は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **Python on z/OS**

    - 検証目的: 探索判定のオープンソースについて、Python on z/OS は、UNIX System Services (USS)のオープンソース on USS で機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、探索判定のオープンソースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPython on z/OSを指定し、OSKB020086の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Python on z/OS
    CASE OSKB020086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Python on z/OS
    CASE OSKB020086
    SOURCE z/OS UNIX System Services
    ```

    Python on z/OSとOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020086を同じ出力で読み、探索判定のオープンソースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020086
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020086 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020086.ZFS
    PATH=/u/oskb/oskb020086
    ```

    BPXO043IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の Python on z/OS と OSKB020086 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### bash on z/OS {#c33-i0221}
*分類: オープンソース on USS*  ・  難易度: 中級

bash on z/OSは、UNIX System Services (USS)のオープンソース on USSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 上書追跡のオープンソースでユーエスエスの運用確認を行います。bash on z/OS の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で上書追跡のオープンソースを確認した扱いにする。
    - B. BPXO043I の有無を確認せず上書追跡のオープンソースを正常終了として記録する。
    - C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 ✅
    - D. bash on z/OS の属性行を読まず上書追跡のオープンソースの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡のオープンソースの正解は C です。bash on z/OS は説明欄の「z/OS UNIX System Servicesでbash on z/OS の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のオープンソースを受け取る担当者は、bash on z/OS の表示結果と BPXO043I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のオープンソースは別カテゴリの確認を流用しており、bash on z/OS の根拠にならないため上書追跡ではありません。 B: 上書追跡のオープンソースは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のオープンソースは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のオープンソースは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のオープンソースが示すbash on z/OS は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **bash on z/OS**

    - 検証目的: 区切判定のオープンソースについて、bash on z/OS は、UNIX System Services (USS)のオープンソース on USS で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、区切判定のオープンソースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にbash on z/OSを指定し、OSKB020090の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND bash on z/OS
    CASE OSKB020090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM bash on z/OS
    CASE OSKB020090
    SOURCE z/OS UNIX System Services
    ```

    bash on z/OSとOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020090を同じ出力で読み、区切判定のオープンソースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020090
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020090 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020090.ZFS
    PATH=/u/oskb/oskb020090
    ```

    BPXO043IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の bash on z/OS と OSKB020090 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### curl on z/OS {#c33-i0222}
*分類: オープンソース on USS*  ・  難易度: 中級

curl on z/OSは、UNIX System Services (USS)のオープンソース on USSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 探索追跡のオープンソースでcurl on z/OS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. curl on z/OS の出力を取らず探索追跡のオープンソースの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して探索追跡のオープンソースの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡のオープンソースへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡のオープンソースの正解は B です。curl on z/OS は説明欄の「探索追跡のオープンソースに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のオープンソースの証跡を読む担当者は、curl on z/OS の属性行と BPXO043I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のオープンソースは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のオープンソースは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のオープンソースは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のオープンソースは別カテゴリの確認を流用しており、curl on z/OS の根拠にならないため探索追跡ではありません。探索追跡のオープンソースに出るcurl on z/OS は UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **curl on z/OS**

    - 検証目的: 条件判定のオープンソースについて、curl on z/OS は、UNIX System Services (USS)のオープンソース on USS で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020089の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、条件判定のオープンソースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にcurl on z/OSを指定し、OSKB020089の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND curl on z/OS
    CASE OSKB020089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM curl on z/OS
    CASE OSKB020089
    SOURCE z/OS UNIX System Services
    ```

    curl on z/OSとOSKB020089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020089を同じ出力で読み、条件判定のオープンソースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020089
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020089 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020089.ZFS
    PATH=/u/oskb/oskb020089
    ```

    BPXO043IとOSKB020089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の curl on z/OS と OSKB020089 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### git on z/OS {#c33-i0223}
*分類: オープンソース on USS*  ・  難易度: 中級

git on z/OSは、UNIX System Services (USS)のオープンソース on USSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 終端追跡のオープンソースに関係するgit on z/OS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 ✅
    - B. git on z/OS の名称と担当者名のみを残して終端追跡のオープンソースの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で終端追跡のオープンソースを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず終端追跡のオープンソースの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡のオープンソースの正解は A です。git on z/OS は説明欄の「git on z/OS の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のオープンソースに関連して、z/OS UNIX System Servicesではgit on z/OS の表示属性と BPXO043I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のオープンソースは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のオープンソースは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のオープンソースは別カテゴリの確認を流用しており、git on z/OS の根拠にならないため終端追跡ではありません。 D: 終端追跡のオープンソースは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため終端追跡ではありません。終端追跡のオープンソースで使うgit on z/OS という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **git on z/OS**

    - 検証目的: 出力判定のオープンソースについて、git on z/OS は、UNIX System Services (USS)のオープンソース on USS で機能名、見出し、または確認対象として参照する項目です。関連するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、出力判定のオープンソースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にgit on z/OSを指定し、OSKB020088の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND git on z/OS
    CASE OSKB020088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM git on z/OS
    CASE OSKB020088
    SOURCE z/OS UNIX System Services
    ```

    git on z/OSとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020088を同じ出力で読み、出力判定のオープンソースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020088
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020088 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020088.ZFS
    PATH=/u/oskb/oskb020088
    ```

    BPXO043IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の git on z/OS と OSKB020088 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### zopen community {#c33-i0224}
*分類: オープンソース on USS*  ・  難易度: 中級

zopen communityは、UNIX System Services (USS)のオープンソース on USSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 出力追跡のオープンソースに関するzopen communityの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず出力追跡のオープンソースの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡のオープンソースの証跡として保存して根拠にする。
    - C. zopen communityの変更点を出力本文から切り離して出力追跡のオープンソースの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡のオープンソースの正解は D です。zopen community は説明欄の「zopen communityの状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のオープンソースに関する記録は、zopen communityの出力行と BPXO043I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のオープンソースは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のオープンソースは別カテゴリの確認を流用しており、zopen communityの根拠にならないため出力追跡ではありません。 C: 出力追跡のオープンソースは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のオープンソースは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のオープンソースで記録するzopen communityはz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **zopen community**

    - 検証目的: 範囲判定のオープンソースについて、zopen communityは、UNIX System Services (USS)のオープンソース on USS で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020091の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、範囲判定のオープンソースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にzopen communityを指定し、OSKB020091の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND zopen community
    CASE OSKB020091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM zopen community
    CASE OSKB020091
    SOURCE z/OS UNIX System Services
    ```

    zopen communityとOSKB020091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020091を同じ出力で読み、範囲判定のオープンソースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020091
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020091 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020091.ZFS
    PATH=/u/oskb/oskb020091
    ```

    BPXO043IとOSKB020091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の zopen community と OSKB020091 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## UNIX System Services (USS) > シグナル

### SIGCHLD {#c33-i0225}
*分類: シグナル*  ・  難易度: 中級

SIGCHLDは、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 展開照合のシグナルで SIGCHLD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SIGCHLD の出力を取らず展開照合のシグナルの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して展開照合のシグナルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合のシグナルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開照合のシグナルの正解は B です。SIGCHLD は説明欄の「展開照合のシグナルに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合のシグナルの証跡を読む担当者は、SIGCHLD の属性行と BPXO043I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合のシグナルは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合のシグナルは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合のシグナルは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため展開照合ではありません。 D: 展開照合のシグナルは別カテゴリの確認を流用しており、SIGCHLD の根拠にならないため展開照合ではありません。展開照合のシグナルに出る SIGCHLD は UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGCHLD**

    - 検証目的: 終端検査のシグナルについて、SIGCHLD は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、終端検査のシグナルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGCHLDを指定し、OSKB020065の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGCHLD
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGCHLD
    CASE OSKB020065
    SOURCE z/OS UNIX System Services
    ```

    SIGCHLDとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020065を同じ出力で読み、終端検査のシグナルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020065
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020065 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020065.ZFS
    PATH=/u/oskb/oskb020065
    ```

    BPXO043IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGCHLD と OSKB020065 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### SIGDUMP (BPX 固有) {#c33-i0226}
*分類: シグナル*  ・  難易度: 中級

SIGDUMP (BPX 固有)は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出照合の固有でユーエスエスの運用確認を行います。SIGDUMP (BPX 固有)の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で呼出照合の固有を確認した扱いにする。
    - B. BPXO043I の有無を確認せず呼出照合の固有を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 ✅
    - D. SIGDUMP (BPX 固有)の属性行を読まず呼出照合の固有の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出照合の固有の正解は C です。SIGDUMP (BPX 固有) は説明欄の「z/OS UNIX System Servicesで SIGDUMP (BPX 固有)の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の固有を受け取る担当者は、SIGDUMP (BPX 固有)の表示結果と BPXO043I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の固有は別カテゴリの確認を流用しており、SIGDUMP (BPX 固有)の根拠にならないため呼出照合ではありません。 B: 呼出照合の固有は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の固有は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の固有は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の固有が示す SIGDUMP (BPX 固有)は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGDUMP (BPX 固有)**

    - 検証目的: 探索検査の固有について、SIGDUMP (BPX 固有)は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、探索検査の固有の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGDUMP (BPX 固有)を指定し、OSKB020066の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGDUMP (BPX 固有)
    CASE OSKB020066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGDUMP (BPX 固有)
    CASE OSKB020066
    SOURCE z/OS UNIX System Services
    ```

    SIGDUMP (BPX 固有)とOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020066を同じ出力で読み、探索検査の固有の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020066
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020066 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020066.ZFS
    PATH=/u/oskb/oskb020066
    ```

    BPXO043IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGDUMP (BPX 固有) と OSKB020066 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### SIGHUP {#c33-i0227}
*分類: シグナル*  ・  難易度: 中級

SIGHUPは、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 変更確認のシグナルに関する SIGHUP の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず変更確認のシグナルの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のシグナルの証跡として保存して根拠にする。
    - C. SIGHUP の変更点を出力本文から切り離して変更確認のシグナルの承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認のシグナルの正解は D です。SIGHUP は説明欄の「SIGHUP の状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のシグナルに関する記録は、SIGHUP の出力行と BPXO043I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のシグナルは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため変更確認ではありません。 B: 変更確認のシグナルは別カテゴリの確認を流用しており、SIGHUP の根拠にならないため変更確認ではありません。 C: 変更確認のシグナルは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のシグナルは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のシグナルで記録する SIGHUP はz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGHUP**

    - 検証目的: 呼出検査のシグナルについて、SIGHUP は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、呼出検査のシグナルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGHUPを指定し、OSKB020063の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGHUP
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGHUP
    CASE OSKB020063
    SOURCE z/OS UNIX System Services
    ```

    SIGHUPとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020063を同じ出力で読み、呼出検査のシグナルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020063
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020063 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020063.ZFS
    PATH=/u/oskb/oskb020063
    ```

    BPXO043IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGHUP と OSKB020063 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### SIGINT {#c33-i0228}
*分類: シグナル*  ・  難易度: 中級

SIGINTは、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 監査確認のシグナルでユーエスエスの運用確認を行います。SIGINT の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で監査確認のシグナルを確認した扱いにする。
    - B. BPXO043I の有無を確認せず監査確認のシグナルを正常終了として記録する。
    - C. 説明欄と実出力を照合し、監査確認の記録として扱う。 ✅
    - D. SIGINT の属性行を読まず監査確認のシグナルの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認のシグナルの正解は C です。SIGINT は説明欄の「z/OS UNIX System Servicesで SIGINT の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のシグナルを受け取る担当者は、SIGINT の表示結果と BPXO043I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のシグナルは別カテゴリの確認を流用しており、SIGINT の根拠にならないため監査確認ではありません。 B: 監査確認のシグナルは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため監査確認ではありません。 C: 監査確認のシグナルは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のシグナルは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のシグナルが示す SIGINT は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGINT**

    - 検証目的: 展開検査のシグナルについて、SIGINT は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、展開検査のシグナルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGINTを指定し、OSKB020062の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGINT
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGINT
    CASE OSKB020062
    SOURCE z/OS UNIX System Services
    ```

    SIGINTとOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020062を同じ出力で読み、展開検査のシグナルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020062
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020062 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020062.ZFS
    PATH=/u/oskb/oskb020062
    ```

    BPXO043IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGINT と OSKB020062 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### SIGKILL {#c33-i0229}
*分類: シグナル*  ・  難易度: 中級

SIGKILLは、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 復旧確認のシグナルで SIGKILL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SIGKILL の出力を取らず復旧確認のシグナルの説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して復旧確認のシグナルの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のシグナルへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧確認のシグナルの正解は B です。SIGKILL は説明欄の「復旧確認のシグナルに関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認のシグナルの証跡を読む担当者は、SIGKILL の属性行と BPXO043I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認のシグナルは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認のシグナルは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認のシグナルは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認のシグナルは別カテゴリの確認を流用しており、SIGKILL の根拠にならないため復旧確認ではありません。復旧確認のシグナルに出る SIGKILL は UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGKILL**

    - 検証目的: 構文検査のシグナルについて、SIGKILL は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、構文検査のシグナルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGKILLを指定し、OSKB020061の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGKILL
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGKILL
    CASE OSKB020061
    SOURCE z/OS UNIX System Services
    ```

    SIGKILLとOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020061を同じ出力で読み、構文検査のシグナルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020061
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020061 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020061.ZFS
    PATH=/u/oskb/oskb020061
    ```

    BPXO043IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGKILL と OSKB020061 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### SIGTERM {#c33-i0230}
*分類: シグナル*  ・  難易度: 中級

SIGTERMは、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 警告確認のシグナルに関係する SIGTERM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 ✅
    - B. SIGTERM の名称と担当者名のみを残して警告確認のシグナルの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で警告確認のシグナルを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず警告確認のシグナルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告確認のシグナルの正解は A です。SIGTERM は説明欄の「SIGTERM の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のシグナルに関連して、z/OS UNIX System Servicesでは SIGTERM の表示属性と BPXO043I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のシグナルは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のシグナルは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のシグナルは別カテゴリの確認を流用しており、SIGTERM の根拠にならないため警告確認ではありません。 D: 警告確認のシグナルは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため警告確認ではありません。警告確認のシグナルで使う SIGTERM という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は警告確認です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGTERM**

    - 検証目的: 変更追跡のシグナルについて、SIGTERM は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこにに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、変更追跡のシグナルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGTERMを指定し、OSKB020060の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGTERM
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGTERM
    CASE OSKB020060
    SOURCE z/OS UNIX System Services
    ```

    SIGTERMとOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020060を同じ出力で読み、変更追跡のシグナルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020060
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020060 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020060.ZFS
    PATH=/u/oskb/oskb020060
    ```

    BPXO043IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGTERM と OSKB020060 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### SIGUSR1 / SIGUSR2 {#c33-i0231}
*分類: シグナル*  ・  難易度: 中級

SIGUSR1 / SIGUSR2は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 構文照合のシグナルに関係する SIGUSR1 / SIGUSR2 の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 ✅
    - B. SIGUSR1 / SIGUSR2 の名称と担当者名のみを残して構文照合のシグナルの表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で構文照合のシグナルを確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず構文照合のシグナルの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文照合のシグナルの正解は A です。SIGUSR1 / SIGUSR2 は説明欄の「SIGUSR1 / SIGUSR2 の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のシグナルに関連して、z/OS UNIX System Servicesでは SIGUSR1 / SIGUSR2 の表示属性と BPXO043I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のシグナルは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のシグナルは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のシグナルは別カテゴリの確認を流用しており、SIGUSR1 / SIGUSR2 の根拠にならないため構文照合ではありません。 D: 構文照合のシグナルは戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため構文照合ではありません。構文照合のシグナルで使う SIGUSR1 / SIGUSR2 という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は構文照合です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **SIGUSR1 / SIGUSR2**

    - 検証目的: 置換検査のシグナルについて、SIGUSR1 / SIGUSR2 は、UNIX System Services (USS)のシグナルで機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、置換検査のシグナルの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にSIGUSR1 / SIGUSR2を指定し、OSKB020064の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND SIGUSR1 / SIGUSR2
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM SIGUSR1 / SIGUSR2
    CASE OSKB020064
    SOURCE z/OS UNIX System Services
    ```

    SIGUSR1 / SIGUSR2とOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020064を同じ出力で読み、置換検査のシグナルの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020064
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020064 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020064.ZFS
    PATH=/u/oskb/oskb020064
    ```

    BPXO043IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の SIGUSR1 / SIGUSR2 と OSKB020064 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## UNIX System Services (USS) > シンボリックリンク

### $SYSNAME 置換 {#c33-i0232}
*分類: シンボリックリンク*  ・  難易度: 中級

$SYSNAME 置換は、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 置換追跡の$ 置換に関する$SYSNAME 置換の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D OMVS,FILE の結果を残さず置換追跡の$ 置換の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の$ 置換の証跡として保存して根拠にする。
    - C. $SYSNAME 置換の変更点を出力本文から切り離して置換追跡の$ 置換の承認欄のみ残す。
    - D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡の$ 置換の正解は D です。$SYSNAME 置換 は説明欄の「$SYSNAME 置換の状態と出力メッセージを結び付ける項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の$ 置換に関する記録は、$SYSNAME 置換の出力行と BPXO043I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の$ 置換は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の$ 置換は別カテゴリの確認を流用しており、$SYSNAME 置換の根拠にならないため置換追跡ではありません。 C: 置換追跡の$ 置換は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の$ 置換は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の$ 置換で記録する$SYSNAME 置換はz/OS UNIX System Servicesの確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **$SYSNAME 置換**

    - 検証目的: 警告照合の$ 置換について、$SYSNAME 置換は、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、警告照合の$ 置換の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に$SYSNAME 置換を指定し、OSKB020037の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND $SYSNAME 置換
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM $SYSNAME 置換
    CASE OSKB020037
    SOURCE z/OS UNIX System Services
    ```

    $SYSNAME 置換とOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020037を同じ出力で読み、警告照合の$ 置換の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020037
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020037 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020037.ZFS
    PATH=/u/oskb/oskb020037
    ```

    BPXO043IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の $SYSNAME 置換 と OSKB020037 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### $VERSION 置換 {#c33-i0233}
*分類: シンボリックリンク*  ・  難易度: 中級

$VERSION 置換は、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 終端追跡の$ 置換に関係する$VERSION 置換の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 ✅
    - B. $VERSION 置換の名称と担当者名のみを残して終端追跡の$ 置換の表示本文を確認対象に含めない。
    - C. ユーエスエス以外の画面で終端追跡の$ 置換を確認し同じ証跡として扱ったことにする。
    - D. BPXO043I の有無を見ず終端追跡の$ 置換の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡の$ 置換の正解は A です。$VERSION 置換 は説明欄の「$VERSION 置換の用途をユーエスエスの表示で確認する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の$ 置換に関連して、z/OS UNIX System Servicesでは$VERSION 置換の表示属性と BPXO043I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の$ 置換は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の$ 置換は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の$ 置換は別カテゴリの確認を流用しており、$VERSION 置換の根拠にならないため終端追跡ではありません。 D: 終端追跡の$ 置換は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため終端追跡ではありません。終端追跡の$ 置換で使う$VERSION 置換という用語は UNIX System Services (USS)で扱う確認対象であり、用語名は終端追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **$VERSION 置換**

    - 検証目的: 復旧照合の$ 置換について、$VERSION 置換は、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、復旧照合の$ 置換の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に$VERSION 置換を指定し、OSKB020038の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND $VERSION 置換
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM $VERSION 置換
    CASE OSKB020038
    SOURCE z/OS UNIX System Services
    ```

    $VERSION 置換とOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020038を同じ出力で読み、復旧照合の$ 置換の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020038
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020038 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020038.ZFS
    PATH=/u/oskb/oskb020038
    ```

    BPXO043IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の $VERSION 置換 と OSKB020038 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### 拡張 symlink (extlink) {#c33-i0234}
*分類: シンボリックリンク*  ・  難易度: 中級

拡張 symlink (extlink)は、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 呼出追跡の拡張でユーエスエスの運用確認を行います。拡張 symlink (extlink)の根拠にできる作業はどれですか。

    - A. z/OS UNIX System Servicesと無関係な一覧で呼出追跡の拡張を確認した扱いにする。
    - B. BPXO043I の有無を確認せず呼出追跡の拡張を正常終了として記録する。
    - C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 ✅
    - D. 拡張 symlink (extlink)の属性行を読まず呼出追跡の拡張の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡の拡張の正解は C です。拡張 symlink (extlink) は説明欄の「z/OS UNIX System Servicesで拡張 symlink (extlink)の扱いを記録する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の拡張を受け取る担当者は、拡張 symlink (extlink)の表示結果と BPXO043I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の拡張は別カテゴリの確認を流用しており、拡張 symlink (extlink)の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の拡張は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の拡張は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の拡張は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の拡張が示す拡張 symlink (extlink)は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **拡張 symlink (extlink)**

    - 検証目的: 値域照合の拡張について、拡張 symlink (extlink)は、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、値域照合の拡張の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に拡張 symlink (extlinを指定し、OSKB020036の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 拡張 symlink (extlin
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 拡張 symlink (extlin
    CASE OSKB020036
    SOURCE z/OS UNIX System Services
    ```

    拡張 symlink (extlinとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020036を同じ出力で読み、値域照合の拡張の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020036
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020036 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020036.ZFS
    PATH=/u/oskb/oskb020036
    ```

    BPXO043IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の 拡張 symlink (extlin と OSKB020036 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference



### 通常 symlink {#c33-i0235}
*分類: シンボリックリンク*  ・  難易度: 中級

通常 symlinkは、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS UNIX System Services User's Guide、z/OS UNIX System Services Command Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

??? question "確認問題（1問）"
    **問題.** 展開追跡の通常で通常 symlinkの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 通常 symlinkの出力を取らず展開追跡の通常の説明文と承認印のみを残す。
    - B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 ✅
    - C. D OMVS,FILE を省略して展開追跡の通常の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の通常へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡の通常の正解は B です。通常 symlink は説明欄の「展開追跡の通常に関係する定義値と表示行を照合する項目」と D OMVS,FILE または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の通常の証跡を読む担当者は、通常 symlinkの属性行と BPXO043I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の通常は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の通常は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の通常は戻り値や記録番号に寄り、BPXO043I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の通常は別カテゴリの確認を流用しており、通常 symlinkの根拠にならないため展開追跡ではありません。展開追跡の通常に出る通常 symlinkは UNIX System Services (USS)の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** zOS31_ieam300 / OS MVS System Commands（zOS31_ieag100） / ABCs_Vol09_UNIX_SystemServices


??? note "検証手順（1件）"
    **通常 symlink**

    - 検証目的: 順序照合の通常について、通常 symlinkは、UNIX System Services (USS)のシンボリックリンクで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、順序照合の通常の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄に通常 symlinkを指定し、OSKB020035の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND 通常 symlink
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM 通常 symlink
    CASE OSKB020035
    SOURCE z/OS UNIX System Services
    ```

    通常 symlinkとOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020035を同じ出力で読み、順序照合の通常の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020035
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020035 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020035.ZFS
    PATH=/u/oskb/oskb020035
    ```

    BPXO043IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の 通常 symlink と OSKB020035 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference




## その他

### その他（特定項目に紐づかないQA・手順） {#c33-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? note "検証手順（5件）"
    **redirect 大なり 小なり**

    - 検証目的: 比較判定の大なり 小なりについて、redirect GT <は、UNIX System Services (USS)の USS シェル機能で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、比較判定の大なり 小なりの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にredirect 大なり 小なりを指定し、OSKB010094の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND redirect 大なり 小なり
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM redirect 大なり 小なり
    CASE OSKB010094
    SOURCE z/OS UNIX System Services
    ```

    redirect 大なり 小なりとOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB010094を同じ出力で読み、比較判定の大なり 小なりの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB010094
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB010094 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB010094.ZFS
    PATH=/u/oskb/oskb010094
    ```

    BPXO043IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の redirect 大なり 小なり と OSKB010094 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB010094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

    ---

    **here-doc 小なり小なり**

    - 検証目的: 順序判定の小なり小なりについて、here-doc <<は、UNIX System Services (USS)の USS シェル機能で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010095の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、順序判定の小なり小なりの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にhere-doc 小なり小なりを指定し、OSKB010095の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND here-doc 小なり小なり
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM here-doc 小なり小なり
    CASE OSKB010095
    SOURCE z/OS UNIX System Services
    ```

    here-doc 小なり小なりとOSKB010095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB010095を同じ出力で読み、順序判定の小なり小なりの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB010095
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB010095 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB010095.ZFS
    PATH=/u/oskb/oskb010095
    ```

    BPXO043IとOSKB010095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の here-doc 小なり小なり と OSKB010095 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB010095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

    ---

    **HFS から zFS 移行**

    - 検証目的: 展開照合のから 移行について、HFS から zFS 移行は、UNIX System Services (USS)のzFS / HFS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、展開照合のから 移行の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にHFS から zFS 移行を指定し、OSKB020022の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND HFS から zFS 移行
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM HFS から zFS 移行
    CASE OSKB020022
    SOURCE z/OS UNIX System Services
    ```

    HFS から zFS 移行とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020022を同じ出力で読み、展開照合のから 移行の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020022
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020022 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020022.ZFS
    PATH=/u/oskb/oskb020022
    ```

    BPXO043IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の HFS から zFS 移行 と OSKB020022 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

    ---

    **MOUNT PARM('など')**

    - 検証目的: 探索照合のなどについて、MOUNT PARM('など')は、UNIX System Services (USS)の MOUNT で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後にに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、探索照合のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMOUNT PARM('など')を指定し、OSKB020026の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MOUNT PARM('など')
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MOUNT PARM('など')
    CASE OSKB020026
    SOURCE z/OS UNIX System Services
    ```

    MOUNT PARM('など')とOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020026を同じ出力で読み、探索照合のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020026
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020026 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020026.ZFS
    PATH=/u/oskb/oskb020026
    ```

    BPXO043IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の MOUNT PARM('など') と OSKB020026 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

    ---

    **F BPXOINIT,SHUTDOWN= など**

    - 検証目的: 呼出整理のなどについて、UNIX System Services USS の USS オペコマンドでは、対象資源、指定値、実行時の出力を対応付けて確認します。USS オペコマンドは、UNIX Systに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020103の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでD OMVS,FILEを実行し、BPXO043Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に D OMVS,FILE を入力し、呼出整理のなどの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> D OMVS,FILE
    ```

    COMMAND INPUTにD OMVS,FILEが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にF BPXOINIT,SHUTDOWを指定し、OSKB020103の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND F BPXOINIT,SHUTDOW
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM F BPXOINIT,SHUTDOW
    CASE OSKB020103
    SOURCE z/OS UNIX System Services
    ```

    F BPXOINIT,SHUTDOWとOSKB020103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。BPXO043IとOSKB020103を同じ出力で読み、呼出整理のなどの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> D OMVS,FILE
    CASE OSKB020103
    → Enter を押す
    ```

    画面・出力:
    ```text
    BPXO043I OSKB020103 DISPLAY OMVS FILE
    TYPENAME   DEVICE   STATUS     MODE
    ZFS        ZFS01    ACTIVE     RDWR
    NAME=OSKB020103.ZFS
    PATH=/u/oskb/oskb020103
    ```

    BPXO043IとOSKB020103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D OMVS,FILE が画面・出力に表示されること
    ② ステップ2 の F BPXOINIT,SHUTDOW と OSKB020103 が画面・出力に表示されること
    ③ ステップ3 の BPXO043I と OSKB020103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS UNIX System Services User's Guide、z / OS UNIX System Services Command Reference

