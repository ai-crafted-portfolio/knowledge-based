---
search:
  exclude: true
---

# UNIX System Services (USS) — 詳細 (3/3)

[← UNIX System Services (USS) の概要へ戻る](index.md)


## UNIX System Services (USS) > シグナル

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

