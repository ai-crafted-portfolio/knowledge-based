---
search:
  exclude: true
---

# SMP/E / SMF / WLM — 詳細 (5/7)

[← SMP/E / SMF / WLM の概要へ戻る](index.md)


## SMP/E / SMF / WLM > SMP/E ZONE操作

### ZONEEDIT OPTIONS {#c28-i0284}
*分類: SMP/E ZONE操作*  ・  難易度: 上級

ZONEEDIT OPTIONSは、SMP/E / SMF / WLMのSMP/E ZONE操作で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Reference (zOS31_gim2000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)

??? question "確認問題（1問）"
    **問題.** 優先確認の操作に関する ZONEEDIT OPTIONS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず優先確認の操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の操作の証跡として保存して根拠にする。
    - C. ZONEEDIT OPTIONS の変更点を出力本文から切り離して優先確認の操作の承認欄のみ残す。
    - D. D WLM,SYSTEMS の結果から対象行を抜き出し、優先確認の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認の操作において選択記号 D を採用し、識別名は優先確認です。優先確認の操作において ZONEEDIT OPTIONS は説明欄の「ZONEEDIT OPTIONS の状態と出力メッセージを結び付ける優先確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の操作に関する記録は、ZONEEDIT OPTIONS の出力行と IWM025I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の操作は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため優先確認ではありません。 B: 優先確認の操作は別カテゴリの確認を流用しており、ZONEEDIT OPTIONS の根拠にならないため優先確認ではありません。 C: 優先確認の操作は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の操作は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の操作で記録する ZONEEDIT OPTIONS は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ZONEEDIT OPTIONS**

    - 検証目的: 順序検査の操作について、ZONEEDIT OPTIONS は、SMP/E / SMF / WLM の SMP/E ZONE 操作で構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010075の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、順序検査の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にZONEEDIT OPTIONSを指定し、OSKB010075の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ZONEEDIT OPTIONS
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ZONEEDIT OPTIONS
    CASE OSKB010075
    SOURCE SMP/E SMF WLM
    ```

    ZONEEDIT OPTIONSとOSKB010075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010075を同じ出力で読み、順序検査の操作の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010075
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010075
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ZONEEDIT OPTIONS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ZONEEDIT OPTIONS と OSKB010075 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)



### ZONEEXPORT {#c28-i0285}
*分類: SMP/E ZONE操作*  ・  難易度: 上級

ZONEEXPORTは、SMP/E / SMF / WLMのSMP/E ZONE操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Reference (zOS31_gim2000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)

??? question "確認問題（1問）"
    **問題.** 値域確認の操作に関する ZONEEXPORT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域確認の操作の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の操作の証跡として保存して根拠にする。
    - C. ZONEEXPORT の変更点を出力本文から切り離して値域確認の操作の承認欄のみ残す。
    - D. D WLM,SYSTEMS で得た表示本文を使い、値域確認の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認の操作において選択記号 D を採用し、識別名は値域確認です。値域確認の操作において ZONEEXPORT は説明欄の「ZONEEXPORT の状態と出力メッセージを結び付ける値域確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の操作に関する記録は、ZONEEXPORT の出力行と IWM025I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の操作は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域確認ではありません。 B: 値域確認の操作は別カテゴリの確認を流用しており、ZONEEXPORT の根拠にならないため値域確認ではありません。 C: 値域確認の操作は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の操作は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の操作で記録する ZONEEXPORT は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ZONEEXPORT**

    - 検証目的: 監査検査の操作について、ZONEEXPORT は、SMP/E / SMF / WLM の SMP/E ZONE 操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、監査検査の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にZONEEXPORTを指定し、OSKB010079の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ZONEEXPORT
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ZONEEXPORT
    CASE OSKB010079
    SOURCE SMP/E SMF WLM
    ```

    ZONEEXPORTとOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010079を同じ出力で読み、監査検査の操作の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010079
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010079
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ZONEEXPORT REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ZONEEXPORT と OSKB010079 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)



### ZONEEXPORT vs UNLOAD {#c28-i0286}
*分類: SMP/E ZONE操作*  ・  難易度: 上級

ZONEEXPORT vs UNLOADは、SMP/E / SMF / WLMのSMP/E ZONE操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Reference (zOS31_gim2000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)

??? question "確認問題（1問）"
    **問題.** 復旧確認の操作で ZONEEXPORT vs UNLOAD の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ZONEEXPORT vs UNLOAD の出力を取らず復旧確認の操作の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧確認の確認にする。 ✅
    - C. D WLM,SYSTEMS を省略して復旧確認の操作の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の操作へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認の操作において選択記号 B を採用し、識別名は復旧確認です。復旧確認の操作において ZONEEXPORT vs UNLOAD は説明欄の「復旧確認の操作に関係する定義値と表示行を照合する復旧確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の操作の証跡を読む担当者は、ZONEEXPORT vs UNLOAD の属性行と IWM025I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の操作は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の操作は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の操作は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の操作は別カテゴリの確認を流用しており、ZONEEXPORT vs UNLOAD の根拠にならないため復旧確認ではありません。復旧確認の操作に出る ZONEEXPORT vs UNLOAD は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ZONEEXPORT vs UNLOAD**

    - 検証目的: 構文判定の操作について、ZONEEXPORT vs UNLOAD は、SMP/E / SMF / WLM の SMP/E ZONE 操作で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、構文判定の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にZONEEXPORT vs UNLOを指定し、OSKB010081の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ZONEEXPORT vs UNLO
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ZONEEXPORT vs UNLO
    CASE OSKB010081
    SOURCE SMP/E SMF WLM
    ```

    ZONEEXPORT vs UNLOとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010081を同じ出力で読み、構文判定の操作の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010081
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010081
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ZONEEXPORT vs UNLOAD REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ZONEEXPORT vs UNLO と OSKB010081 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)



### ZONEIMPORT {#c28-i0287}
*分類: SMP/E ZONE操作*  ・  難易度: 上級

ZONEIMPORTは、SMP/E / SMF / WLMのSMP/E ZONE操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Reference (zOS31_gim2000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)

??? question "確認問題（1問）"
    **問題.** 警告確認の操作に関係する ZONEIMPORT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告確認として引き継ぐ。 ✅
    - B. ZONEIMPORT の名称と担当者名のみを残して警告確認の操作の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告確認の操作を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告確認の操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認の操作において選択記号 A を採用し、識別名は警告確認です。警告確認の操作において ZONEIMPORT は説明欄の「ZONEIMPORT の用途を保守管理の表示で確認する警告確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の操作に関連して、SMP/E SMF WLM では ZONEIMPORT の表示属性と IWM025I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の操作は対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の操作は名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の操作は別カテゴリの確認を流用しており、ZONEIMPORT の根拠にならないため警告確認ではありません。 D: 警告確認の操作は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告確認ではありません。警告確認の操作で使う ZONEIMPORT という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ZONEIMPORT**

    - 検証目的: 変更検査の操作について、ZONEIMPORT は、SMP/E / SMF / WLM の SMP/E ZONE 操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010080の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、変更検査の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にZONEIMPORTを指定し、OSKB010080の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ZONEIMPORT
    CASE OSKB010080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ZONEIMPORT
    CASE OSKB010080
    SOURCE SMP/E SMF WLM
    ```

    ZONEIMPORTとOSKB010080が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010080を同じ出力で読み、変更検査の操作の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010080
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010080
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ZONEIMPORT REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010080が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ZONEIMPORT と OSKB010080 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)



### ZONEMERGE {#c28-i0288}
*分類: SMP/E ZONE操作*  ・  難易度: 上級

ZONEMERGEは、SMP/E / SMF / WLMのSMP/E ZONE操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Reference (zOS31_gim2000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)

??? question "確認問題（1問）"
    **問題.** 順序確認の操作で保守管理の運用確認を行います。ZONEMERGE の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で順序確認の操作を確認した扱いにする。
    - B. IWM025I の有無を確認せず順序確認の操作を正常終了として記録する。
    - C. 同じ画面で対象行と IWM025I を読み、順序確認の結果として保存する。 ✅
    - D. ZONEMERGE の属性行を読まず順序確認の操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認の操作において選択記号 C を採用し、識別名は順序確認です。順序確認の操作において ZONEMERGE は説明欄の「SMP/E SMF WLM で ZONEMERGE の扱いを記録する順序確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の操作を受け取る担当者は、ZONEMERGE の表示結果と IWM025I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の操作は別カテゴリの確認を流用しており、ZONEMERGE の根拠にならないため順序確認ではありません。 B: 順序確認の操作は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため順序確認ではありません。 C: 順序確認の操作は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の操作は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の操作が示す ZONEMERGE は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ZONEMERGE**

    - 検証目的: 復旧検査の操作について、ZONEMERGE は、SMP/E / SMF / WLM の SMP/E ZONE 操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、復旧検査の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にZONEMERGEを指定し、OSKB010078の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ZONEMERGE
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ZONEMERGE
    CASE OSKB010078
    SOURCE SMP/E SMF WLM
    ```

    ZONEMERGEとOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010078を同じ出力で読み、復旧検査の操作の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010078
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010078
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ZONEMERGE REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ZONEMERGE と OSKB010078 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)



### ZONERENAME {#c28-i0289}
*分類: SMP/E ZONE操作*  ・  難易度: 上級

ZONERENAMEは、SMP/E / SMF / WLMのSMP/E ZONE操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Reference (zOS31_gim2000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)

??? question "確認問題（1問）"
    **問題.** 記録確認の操作に関係する ZONERENAME の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、記録確認の確認記録にまとめる。 ✅
    - B. ZONERENAME の名称と担当者名のみを残して記録確認の操作の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で記録確認の操作を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず記録確認の操作の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認の操作において選択記号 A を採用し、識別名は記録確認です。記録確認の操作において ZONERENAME は説明欄の「ZONERENAME の用途を保守管理の表示で確認する記録確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の操作に関連して、SMP/E SMF WLM では ZONERENAME の表示属性と IWM025I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の操作は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の操作は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の操作は別カテゴリの確認を流用しており、ZONERENAME の根拠にならないため記録確認ではありません。 D: 記録確認の操作は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため記録確認ではありません。記録確認の操作で使う ZONERENAME という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は記録確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ZONERENAME**

    - 検証目的: 値域検査の操作について、ZONERENAME は、SMP/E / SMF / WLM の SMP/E ZONE 操作で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010076の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、値域検査の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にZONERENAMEを指定し、OSKB010076の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ZONERENAME
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ZONERENAME
    CASE OSKB010076
    SOURCE SMP/E SMF WLM
    ```

    ZONERENAMEとOSKB010076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010076を同じ出力で読み、値域検査の操作の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010076
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010076
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ZONERENAME REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ZONERENAME と OSKB010076 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Reference (zOS31_gim2000)




## SMP/E / SMF / WLM > SMP/E その他コマンド

### REPORT CROSSZONE {#c28-i0290}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

REPORT CROSSZONEは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 変更照合のその他コマンドに関する REPORT CROSSZONE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず変更照合のその他コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のその他コマンドの証跡として保存して根拠にする。
    - C. REPORT CROSSZONE の変更点を出力本文から切り離して変更照合のその他コマンドの承認欄のみ残す。
    - D. 同じ画面で対象行と IWM025I を読み、変更照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合のその他コマンドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合のその他コマンドにおいて REPORT CROSSZONE は説明欄の「REPORT CROSSZONE の状態と出力メッセージを結び付ける変更照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のその他コマンドに関する記録は、REPORT CROSSZONE の出力行と IWM025I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため変更照合ではありません。 B: 変更照合のその他コマンドは別カテゴリの確認を流用しており、REPORT CROSSZONE の根拠にならないため変更照合ではありません。 C: 変更照合のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のその他コマンドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のその他コマンドで記録する REPORT CROSSZONE は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **REPORT CROSSZONE**

    - 検証目的: 記録追跡のその他コマンドについて、REPORT CROSSZONE は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、記録追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にREPORT CROSSZONEを指定し、OSKB010053の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND REPORT CROSSZONE
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM REPORT CROSSZONE
    CASE OSKB010053
    SOURCE SMP/E SMF WLM
    ```

    REPORT CROSSZONEとOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010053を同じ出力で読み、記録追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010053
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010053
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I REPORT CROSSZONE REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の REPORT CROSSZONE と OSKB010053 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### REPORT ERRSYSMODS {#c28-i0291}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

REPORT ERRSYSMODSは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 構文追跡のその他コマンドに関係する REPORT ERRSYSMODS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D WLM,SYSTEMS で得た表示本文を使い、構文追跡の採否を説明欄に結び付ける。 ✅
    - B. REPORT ERRSYSMODS の名称と担当者名のみを残して構文追跡のその他コマンドの表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で構文追跡のその他コマンドを確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず構文追跡のその他コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡のその他コマンドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のその他コマンドにおいて REPORT ERRSYSMODS は説明欄の「REPORT ERRSYSMODS の用途を保守管理の表示で確認する構文追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のその他コマンドに関連して、SMP/E SMF WLM では REPORT ERRSYSMODS の表示属性と IWM025I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のその他コマンドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のその他コマンドは別カテゴリの確認を流用しており、REPORT ERRSYSMODS の根拠にならないため構文追跡ではありません。 D: 構文追跡のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため構文追跡ではありません。構文追跡のその他コマンドで使う REPORT ERRSYSMODS という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は構文追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **REPORT ERRSYSMODS**

    - 検証目的: 比較追跡のその他コマンドについて、REPORT ERRSYSMODS は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、比較追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にREPORT ERRSYSMODSを指定し、OSKB010054の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND REPORT ERRSYSMODS
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM REPORT ERRSYSMODS
    CASE OSKB010054
    SOURCE SMP/E SMF WLM
    ```

    REPORT ERRSYSMODSとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010054を同じ出力で読み、比較追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010054
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010054
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I REPORT ERRSYSMODS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の REPORT ERRSYSMODS と OSKB010054 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### REPORT INVENTORY {#c28-i0292}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

REPORT INVENTORYは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 呼出追跡のその他コマンドで保守管理の運用確認を行います。REPORT INVENTORY の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で呼出追跡のその他コマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず呼出追跡のその他コマンドを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 ✅
    - D. REPORT INVENTORY の属性行を読まず呼出追跡のその他コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡のその他コマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のその他コマンドにおいて REPORT INVENTORY は説明欄の「SMP/E SMF WLM で REPORT INVENTORY の扱いを記録する呼出追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のその他コマンドを受け取る担当者は、REPORT INVENTORY の表示結果と IWM025I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のその他コマンドは別カテゴリの確認を流用しており、REPORT INVENTORY の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のその他コマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のその他コマンドが示す REPORT INVENTORY は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **REPORT INVENTORY**

    - 検証目的: 値域追跡のその他コマンドについて、REPORT INVENTORY は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、値域追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にREPORT INVENTORYを指定し、OSKB010056の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND REPORT INVENTORY
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM REPORT INVENTORY
    CASE OSKB010056
    SOURCE SMP/E SMF WLM
    ```

    REPORT INVENTORYとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010056を同じ出力で読み、値域追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010056
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010056
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I REPORT INVENTORY REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の REPORT INVENTORY と OSKB010056 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### REPORT MISSINGFIX {#c28-i0293}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

REPORT MISSINGFIXは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 置換追跡のその他コマンドに関する REPORT MISSINGFIX の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず置換追跡のその他コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡のその他コマンドの証跡として保存して根拠にする。
    - C. REPORT MISSINGFIX の変更点を出力本文から切り離して置換追跡のその他コマンドの承認欄のみ残す。
    - D. SMP/E SMF WLM の表示形式に沿って根拠行を採り、置換追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡のその他コマンドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のその他コマンドにおいて REPORT MISSINGFIX は説明欄の「REPORT MISSINGFIX の状態と出力メッセージを結び付ける置換追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のその他コマンドに関する記録は、REPORT MISSINGFIX の出力行と IWM025I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のその他コマンドは別カテゴリの確認を流用しており、REPORT MISSINGFIX の根拠にならないため置換追跡ではありません。 C: 置換追跡のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のその他コマンドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のその他コマンドで記録する REPORT MISSINGFIX は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **REPORT MISSINGFIX**

    - 検証目的: 警告追跡のその他コマンドについて、REPORT MISSINGFIX は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、警告追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にREPORT MISSINGFIXを指定し、OSKB010057の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND REPORT MISSINGFIX
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM REPORT MISSINGFIX
    CASE OSKB010057
    SOURCE SMP/E SMF WLM
    ```

    REPORT MISSINGFIXとOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010057を同じ出力で読み、警告追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010057
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010057
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I REPORT MISSINGFIX REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の REPORT MISSINGFIX と OSKB010057 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### REPORT SOURCEID {#c28-i0294}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

REPORT SOURCEIDは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 展開追跡のその他コマンドで REPORT SOURCEID の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. REPORT SOURCEID の出力を取らず展開追跡のその他コマンドの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開追跡として引き継ぐ。 ✅
    - C. D WLM,SYSTEMS を省略して展開追跡のその他コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のその他コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡のその他コマンドにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のその他コマンドにおいて REPORT SOURCEID は説明欄の「展開追跡のその他コマンドに関係する定義値と表示行を照合する展開追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のその他コマンドの証跡を読む担当者は、REPORT SOURCEID の属性行と IWM025I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のその他コマンドは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のその他コマンドは別カテゴリの確認を流用しており、REPORT SOURCEID の根拠にならないため展開追跡ではありません。展開追跡のその他コマンドに出る REPORT SOURCEID は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **REPORT SOURCEID**

    - 検証目的: 順序追跡のその他コマンドについて、REPORT SOURCEID は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示さに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、順序追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にREPORT SOURCEIDを指定し、OSKB010055の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND REPORT SOURCEID
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM REPORT SOURCEID
    CASE OSKB010055
    SOURCE SMP/E SMF WLM
    ```

    REPORT SOURCEIDとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010055を同じ出力で読み、順序追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010055
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010055
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I REPORT SOURCEID REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の REPORT SOURCEID と OSKB010055 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### REPORT SYSMODS {#c28-i0295}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

REPORT SYSMODSは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 監査照合のその他コマンドで保守管理の運用確認を行います。REPORT SYSMODS の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で監査照合のその他コマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず監査照合のその他コマンドを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査照合の根拠にする。 ✅
    - D. REPORT SYSMODS の属性行を読まず監査照合のその他コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合のその他コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合のその他コマンドにおいて REPORT SYSMODS は説明欄の「SMP/E SMF WLM で REPORT SYSMODS の扱いを記録する監査照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のその他コマンドを受け取る担当者は、REPORT SYSMODS の表示結果と IWM025I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のその他コマンドは別カテゴリの確認を流用しており、REPORT SYSMODS の根拠にならないため監査照合ではありません。 B: 監査照合のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため監査照合ではありません。 C: 監査照合のその他コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のその他コマンドが示す REPORT SYSMODS は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **REPORT SYSMODS**

    - 検証目的: 優先追跡のその他コマンドについて、REPORT SYSMODS は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にREPORT SYSMODSを指定し、OSKB010052の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND REPORT SYSMODS
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM REPORT SYSMODS
    CASE OSKB010052
    SOURCE SMP/E SMF WLM
    ```

    REPORT SYSMODSとOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010052を同じ出力で読み、優先追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010052
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010052
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I REPORT SYSMODS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の REPORT SYSMODS と OSKB010052 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### RESETRC コマンド {#c28-i0296}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

RESETRC コマンドは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 復旧照合のコマンドで RESETRC コマンドの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. RESETRC コマンドの出力を取らず復旧照合のコマンドの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧照合の確認記録にまとめる。 ✅
    - C. D WLM,SYSTEMS を省略して復旧照合のコマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合のコマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合のコマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合のコマンドにおいて RESETRC コマンド は説明欄の「復旧照合のコマンドに関係する定義値と表示行を照合する復旧照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のコマンドの証跡を読む担当者は、RESETRC コマンドの属性行と IWM025I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のコマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のコマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のコマンドは別カテゴリの確認を流用しており、RESETRC コマンドの根拠にならないため復旧照合ではありません。復旧照合のコマンドに出る RESETRC コマンドは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **RESETRC コマンド**

    - 検証目的: 範囲追跡のコマンドについて、RESETRC コマンドは、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲追跡のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にRESETRC コマンドを指定し、OSKB010051の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND RESETRC コマンド
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM RESETRC コマンド
    CASE OSKB010051
    SOURCE SMP/E SMF WLM
    ```

    RESETRC コマンドとOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010051を同じ出力で読み、範囲追跡のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010051
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010051
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I RESETRC コマンド REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の RESETRC コマンド と OSKB010051 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### RESTORE BYPASS {#c28-i0297}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

RESTORE BYPASSは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 警告照合のその他コマンドに関係する RESTORE BYPASS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果から対象行を抜き出し、警告照合の証跡として残す。 ✅
    - B. RESTORE BYPASS の名称と担当者名のみを残して警告照合のその他コマンドの表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告照合のその他コマンドを確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告照合のその他コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合のその他コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のその他コマンドにおいて RESTORE BYPASS は説明欄の「RESTORE BYPASS の用途を保守管理の表示で確認する警告照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のその他コマンドに関連して、SMP/E SMF WLM では RESTORE BYPASS の表示属性と IWM025I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のその他コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のその他コマンドは別カテゴリの確認を流用しており、RESTORE BYPASS の根拠にならないため警告照合ではありません。 D: 警告照合のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告照合ではありません。警告照合のその他コマンドで使う RESTORE BYPASS という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **RESTORE BYPASS**

    - 検証目的: 区切追跡のその他コマンドについて、RESTORE BYPASS は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にRESTORE BYPASSを指定し、OSKB010050の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND RESTORE BYPASS
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM RESTORE BYPASS
    CASE OSKB010050
    SOURCE SMP/E SMF WLM
    ```

    RESTORE BYPASSとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010050を同じ出力で読み、区切追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010050
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010050
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I RESTORE BYPASS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の RESTORE BYPASS と OSKB010050 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### RESTORE SELECT {#c28-i0298}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

RESTORE SELECTは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 値域照合のその他コマンドに関する RESTORE SELECT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域照合のその他コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合のその他コマンドの証跡として保存して根拠にする。
    - C. RESTORE SELECT の変更点を出力本文から切り離して値域照合のその他コマンドの承認欄のみ残す。
    - D. IWM025I を含む表示を保存し、説明欄との差分を値域照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合のその他コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合のその他コマンドにおいて RESTORE SELECT は説明欄の「RESTORE SELECT の状態と出力メッセージを結び付ける値域照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のその他コマンドに関する記録は、RESTORE SELECT の出力行と IWM025I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域照合ではありません。 B: 値域照合のその他コマンドは別カテゴリの確認を流用しており、RESTORE SELECT の根拠にならないため値域照合ではありません。 C: 値域照合のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のその他コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のその他コマンドで記録する RESTORE SELECT は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **RESTORE SELECT**

    - 検証目的: 条件追跡のその他コマンドについて、RESTORE SELECT は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、条件追跡のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にRESTORE SELECTを指定し、OSKB010049の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND RESTORE SELECT
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM RESTORE SELECT
    CASE OSKB010049
    SOURCE SMP/E SMF WLM
    ```

    RESTORE SELECTとOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010049を同じ出力で読み、条件追跡のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010049
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010049
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I RESTORE SELECT REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の RESTORE SELECT と OSKB010049 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### RESTORE コマンド {#c28-i0299}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

RESTORE コマンドは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 順序照合のコマンドで保守管理の運用確認を行います。RESTORE コマンドの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で順序照合のコマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず順序照合のコマンドを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序照合の根拠を固定する。 ✅
    - D. RESTORE コマンドの属性行を読まず順序照合のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合のコマンドにおいて選択記号 C を採用し、識別名は順序照合です。順序照合のコマンドにおいて RESTORE コマンド は説明欄の「SMP/E SMF WLM で RESTORE コマンドの扱いを記録する順序照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のコマンドを受け取る担当者は、RESTORE コマンドの表示結果と IWM025I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のコマンドは別カテゴリの確認を流用しており、RESTORE コマンドの根拠にならないため順序照合ではありません。 B: 順序照合のコマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため順序照合ではありません。 C: 順序照合のコマンドは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のコマンドが示す RESTORE コマンドは出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **RESTORE コマンド**

    - 検証目的: 出力追跡のコマンドについて、RESTORE コマンドは、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、出力追跡のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にRESTORE コマンドを指定し、OSKB010048の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND RESTORE コマンド
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM RESTORE コマンド
    CASE OSKB010048
    SOURCE SMP/E SMF WLM
    ```

    RESTORE コマンドとOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010048を同じ出力で読み、出力追跡のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010048
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010048
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I RESTORE コマンド REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の RESTORE コマンド と OSKB010048 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### UNLOAD SYSMOD {#c28-i0300}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

UNLOAD SYSMODは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 条件確認のその他コマンドに関係する UNLOAD SYSMOD の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、条件確認の確認値として扱う。 ✅
    - B. UNLOAD SYSMOD の名称と担当者名のみを残して条件確認のその他コマンドの表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で条件確認のその他コマンドを確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず条件確認のその他コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認のその他コマンドにおいて選択記号 A を採用し、識別名は条件確認です。条件確認のその他コマンドにおいて UNLOAD SYSMOD は説明欄の「UNLOAD SYSMOD の用途を保守管理の表示で確認する条件確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のその他コマンドに関連して、SMP/E SMF WLM では UNLOAD SYSMOD の表示属性と IWM025I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のその他コマンドは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のその他コマンドは別カテゴリの確認を流用しており、UNLOAD SYSMOD の根拠にならないため条件確認ではありません。 D: 条件確認のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため条件確認ではありません。条件確認のその他コマンドで使う UNLOAD SYSMOD という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は条件確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **UNLOAD SYSMOD**

    - 検証目的: 優先検査のその他コマンドについて、UNLOAD SYSMOD は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先検査のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にUNLOAD SYSMODを指定し、OSKB010072の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND UNLOAD SYSMOD
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM UNLOAD SYSMOD
    CASE OSKB010072
    SOURCE SMP/E SMF WLM
    ```

    UNLOAD SYSMODとOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010072を同じ出力で読み、優先検査のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010072
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010072
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I UNLOAD SYSMOD REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の UNLOAD SYSMOD と OSKB010072 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### UNLOAD ZONE {#c28-i0301}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

UNLOAD ZONEは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 出力確認のその他コマンドに関する UNLOAD ZONE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず出力確認のその他コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のその他コマンドの証跡として保存して根拠にする。
    - C. UNLOAD ZONE の変更点を出力本文から切り離して出力確認のその他コマンドの承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力確認で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認のその他コマンドにおいて選択記号 D を採用し、識別名は出力確認です。出力確認のその他コマンドにおいて UNLOAD ZONE は説明欄の「UNLOAD ZONE の状態と出力メッセージを結び付ける出力確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認のその他コマンドに関する記録は、UNLOAD ZONE の出力行と IWM025I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認のその他コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため出力確認ではありません。 B: 出力確認のその他コマンドは別カテゴリの確認を流用しており、UNLOAD ZONE の根拠にならないため出力確認ではありません。 C: 出力確認のその他コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認のその他コマンドは対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認のその他コマンドで記録する UNLOAD ZONE は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **UNLOAD ZONE**

    - 検証目的: 範囲検査のその他コマンドについて、UNLOAD ZONE は、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲検査のその他コマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にUNLOAD ZONEを指定し、OSKB010071の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND UNLOAD ZONE
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM UNLOAD ZONE
    CASE OSKB010071
    SOURCE SMP/E SMF WLM
    ```

    UNLOAD ZONEとOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010071を同じ出力で読み、範囲検査のその他コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010071
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010071
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I UNLOAD ZONE REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の UNLOAD ZONE と OSKB010071 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)



### UNLOAD コマンド {#c28-i0302}
*分類: SMP/E その他コマンド*  ・  難易度: 上級

UNLOAD コマンドは、SMP/E / SMF / WLMのSMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS SMP/E Commands (zOS31_gim1000) / z/OS SMP/E Messages, Codes, and Diagnosis (zOS31_gim0000) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)

??? question "確認問題（1問）"
    **問題.** 上書確認のコマンドで保守管理の運用確認を行います。UNLOAD コマンドの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で上書確認のコマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず上書確認のコマンドを正常終了として記録する。
    - C. SMP/E SMF WLM の表示形式に沿って根拠行を採り、上書確認の点検結果を残す。 ✅
    - D. UNLOAD コマンドの属性行を読まず上書確認のコマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認のコマンドにおいて選択記号 C を採用し、識別名は上書確認です。上書確認のコマンドにおいて UNLOAD コマンド は説明欄の「SMP/E SMF WLM で UNLOAD コマンドの扱いを記録する上書確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のコマンドを受け取る担当者は、UNLOAD コマンドの表示結果と IWM025I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のコマンドは別カテゴリの確認を流用しており、UNLOAD コマンドの根拠にならないため上書確認ではありません。 B: 上書確認のコマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため上書確認ではありません。 C: 上書確認のコマンドは対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のコマンドが示す UNLOAD コマンドは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **UNLOAD コマンド**

    - 検証目的: 区切検査のコマンドについて、UNLOAD コマンドは、SMP/E / SMF / WLM の SMP/E その他コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切検査のコマンドの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にUNLOAD コマンドを指定し、OSKB010070の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND UNLOAD コマンド
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM UNLOAD コマンド
    CASE OSKB010070
    SOURCE SMP/E SMF WLM
    ```

    UNLOAD コマンドとOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB010070を同じ出力で読み、区切検査のコマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB010070
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB010070
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I UNLOAD コマンド REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の UNLOAD コマンド と OSKB010070 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB010070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS SMP / E Commands (zOS31_gim1000) / E Messages / Codes / and Diagnosis (zOS31_gim0000)




## SMP/E / SMF / WLM > WLM Application Environment

### AE Procedure {#c28-i0303}
*分類: WLM Application Environment*  ・  難易度: 上級

AE Procedureは、SMP/E / SMF / WLMのWLM Application Environmentで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 区切追跡の保守管理で AE Procedureの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AE Procedureの出力を取らず区切追跡の保守管理の説明文と承認印のみを残す。
    - B. SMP/E SMF WLM の表示形式に沿って根拠行を採り、区切追跡の点検結果を残す。 ✅
    - C. D WLM,SYSTEMS を省略して区切追跡の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡の保守管理において選択記号 B を採用し、識別名は区切追跡です。区切追跡の保守管理において AE Procedure は説明欄の「区切追跡の保守管理に関係する定義値と表示行を照合する区切追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の保守管理の証跡を読む担当者は、AE Procedureの属性行と IWM025I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の保守管理は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の保守管理は別カテゴリの確認を流用しており、AE Procedureの根拠にならないため区切追跡ではありません。区切追跡の保守管理に出る AE Procedureは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **AE Procedure**

    - 検証目的: 呼出記録の保守管理について、AE Procedureは、SMP/E / SMF / WLM の WLM Application Environmentで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030123の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、呼出記録の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にAE Procedureを指定し、OSKB030123の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND AE Procedure
    CASE OSKB030123
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM AE Procedure
    CASE OSKB030123
    SOURCE SMP/E SMF WLM
    ```

    AE ProcedureとOSKB030123が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030123を同じ出力で読み、呼出記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030123
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030123
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I AE Procedure REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030123が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の AE Procedure と OSKB030123 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### AE Quiesce/Resume {#c28-i0304}
*分類: WLM Application Environment*  ・  難易度: 上級

AE Quiesce/Resumeは、SMP/E / SMF / WLMのWLM Application Environmentで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? note "検証手順（1件）"
    **AE Quiesce・ Resume**

    - 検証目的: 置換記録の・について、AE Quiesce/Resumeは、SMP/E / SMF / WLM の WLM Application Environmentで機能名、見出し、または確認対象として参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030124の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、置換記録の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にAE Quiesce・ Resumeを指定し、OSKB030124の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND AE Quiesce・ Resume
    CASE OSKB030124
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM AE Quiesce・ Resume
    CASE OSKB030124
    SOURCE SMP/E SMF WLM
    ```

    AE Quiesce・ ResumeとOSKB030124が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030124を同じ出力で読み、置換記録の・の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030124
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030124
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I AE Quiesce・ Resume REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030124が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の AE Quiesce・ Resume と OSKB030124 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### AE とは {#c28-i0305}
*分類: WLM Application Environment*  ・  難易度: 上級

AE とはは、SMP/E / SMF / WLMのWLM Application Environmentで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? note "検証手順（1件）"
    **AE とは**

    - 検証目的: 構文記録のとはについて、AE とはは、SMP/E / SMF / WLM の WLM Application Environmentで機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030121の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、構文記録のとはの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にAE とはを指定し、OSKB030121の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND AE とは
    CASE OSKB030121
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM AE とは
    CASE OSKB030121
    SOURCE SMP/E SMF WLM
    ```

    AE とはとOSKB030121が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030121を同じ出力で読み、構文記録のとはの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030121
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030121
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I AE とは REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030121が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の AE とは と OSKB030121 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### Db2 Stored Procedure AE {#c28-i0306}
*分類: WLM Application Environment*  ・  難易度: 上級

Db2 Stored Procedure AEは、SMP/E / SMF / WLMのWLM Application Environmentで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 条件追跡の保守管理に関係する Db2 Stored Procedure AE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、条件追跡の確認にする。 ✅
    - B. Db2 Stored Procedure AE の名称と担当者名のみを残して条件追跡の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で条件追跡の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず条件追跡の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡の保守管理において選択記号 A を採用し、識別名は条件追跡です。条件追跡の保守管理において Db2 Stored Procedure AE は説明欄の「Db2 Stored Procedure AE の用途を保守管理の表示で確認する条件追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の保守管理に関連して、SMP/E SMF WLM では Db2 Stored Procedure AE の表示属性と IWM025I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の保守管理は対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の保守管理は別カテゴリの確認を流用しており、Db2 Stored Procedure AE の根拠にならないため条件追跡ではありません。 D: 条件追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため条件追跡ではありません。条件追跡の保守管理で使う Db2 Stored Procedure AE という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は条件追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Db2 Stored Procedure AE**

    - 検証目的: 展開記録の保守管理について、Db2 Stored Procedure AE は、SMP/E / SMF / WLM の WLM Application Environmentで機能名、見出し、または確認対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030122の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、展開記録の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にDb2 Stored Proceduを指定し、OSKB030122の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Db2 Stored Procedu
    CASE OSKB030122
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Db2 Stored Procedu
    CASE OSKB030122
    SOURCE SMP/E SMF WLM
    ```

    Db2 Stored ProceduとOSKB030122が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030122を同じ出力で読み、展開記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030122
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030122
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Db2 Stored Procedure AE REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030122が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Db2 Stored Procedu と OSKB030122 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)




## SMP/E / SMF / WLM > WLM Classification Rules

### Qualifier Group {#c28-i0307}
*分類: WLM Classification Rules*  ・  難易度: 上級

Qualifier Groupは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 構文追跡の保守管理に関係する Qualifier Groupの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて構文追跡の根拠を固定する。 ✅
    - B. Qualifier Groupの名称と担当者名のみを残して構文追跡の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で構文追跡の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず構文追跡の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡の保守管理において選択記号 A を採用し、識別名は構文追跡です。構文追跡の保守管理において Qualifier Group は説明欄の「Qualifier Groupの用途を保守管理の表示で確認する構文追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の保守管理に関連して、SMP/E SMF WLM では Qualifier Groupの表示属性と IWM025I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の保守管理は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の保守管理は別カテゴリの確認を流用しており、Qualifier Groupの根拠にならないため構文追跡ではありません。 D: 構文追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため構文追跡ではありません。構文追跡の保守管理で使う Qualifier Groupという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は構文追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Qualifier Group**

    - 検証目的: 比較整理の保守管理について、Qualifier Groupは、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030114の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、比較整理の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にQualifier Groupを指定し、OSKB030114の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Qualifier Group
    CASE OSKB030114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Qualifier Group
    CASE OSKB030114
    SOURCE SMP/E SMF WLM
    ```

    Qualifier GroupとOSKB030114が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030114を同じ出力で読み、比較整理の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030114
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030114
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Qualifier Group REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030114が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Qualifier Group と OSKB030114 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem ASCH {#c28-i0308}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem ASCHは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 警告確認の保守管理に関係する Subsystem ASCH の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告確認の根拠を固定する。 ✅
    - B. Subsystem ASCH の名称と担当者名のみを残して警告確認の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告確認の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告確認の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認の保守管理において選択記号 A を採用し、識別名は警告確認です。警告確認の保守管理において Subsystem ASCH は説明欄の「Subsystem ASCH の用途を保守管理の表示で確認する警告確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の保守管理に関連して、SMP/E SMF WLM では Subsystem ASCH の表示属性と IWM025I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の保守管理は対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の保守管理は別カテゴリの確認を流用しており、Subsystem ASCH の根拠にならないため警告確認ではありません。 D: 警告確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告確認ではありません。警告確認の保守管理で使う Subsystem ASCH という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem ASCH**

    - 検証目的: 区切判定の保守管理について、Subsystem ASCH は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030090の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem ASCHを指定し、OSKB030090の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem ASCH
    CASE OSKB030090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem ASCH
    CASE OSKB030090
    SOURCE SMP/E SMF WLM
    ```

    Subsystem ASCHとOSKB030090が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030090を同じ出力で読み、区切判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030090
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030090
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem ASCH REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030090が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem ASCH と OSKB030090 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem CICS {#c28-i0309}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem CICSは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 復旧確認の保守管理で Subsystem CICS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Subsystem CICS の出力を取らず復旧確認の保守管理の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を復旧確認で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して復旧確認の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認の保守管理において選択記号 B を採用し、識別名は復旧確認です。復旧確認の保守管理において Subsystem CICS は説明欄の「復旧確認の保守管理に関係する定義値と表示行を照合する復旧確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の保守管理の証跡を読む担当者は、Subsystem CICS の属性行と IWM025I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の保守管理は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の保守管理は別カテゴリの確認を流用しており、Subsystem CICS の根拠にならないため復旧確認ではありません。復旧確認の保守管理に出る Subsystem CICS は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem CICS**

    - 検証目的: 範囲判定の保守管理について、Subsystem CICS は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030091の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem CICSを指定し、OSKB030091の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem CICS
    CASE OSKB030091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem CICS
    CASE OSKB030091
    SOURCE SMP/E SMF WLM
    ```

    Subsystem CICSとOSKB030091が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030091を同じ出力で読み、範囲判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030091
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030091
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem CICS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030091が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem CICS と OSKB030091 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem DB2 {#c28-i0310}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem DB2は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 変更確認の保守管理に関する Subsystem DB2 の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず変更確認の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の保守管理の証跡として保存して根拠にする。
    - C. Subsystem DB2 の変更点を出力本文から切り離して変更確認の保守管理の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更確認の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認の保守管理において選択記号 D を採用し、識別名は変更確認です。変更確認の保守管理において Subsystem DB2 は説明欄の「Subsystem DB2 の状態と出力メッセージを結び付ける変更確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の保守管理に関する記録は、Subsystem DB2 の出力行と IWM025I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため変更確認ではありません。 B: 変更確認の保守管理は別カテゴリの確認を流用しており、Subsystem DB2 の根拠にならないため変更確認ではありません。 C: 変更確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の保守管理は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の保守管理で記録する Subsystem DB2 は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は変更確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem DB2**

    - 検証目的: 記録判定の保守管理について、Subsystem DB2 は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030093の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、記録判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem DB2を指定し、OSKB030093の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem DB2
    CASE OSKB030093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem DB2
    CASE OSKB030093
    SOURCE SMP/E SMF WLM
    ```

    Subsystem DB2とOSKB030093が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030093を同じ出力で読み、記録判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030093
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030093
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem DB2 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030093が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem DB2 と OSKB030093 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem DDF {#c28-i0311}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem DDFは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 構文照合の保守管理に関係する Subsystem DDF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて構文照合の根拠にする。 ✅
    - B. Subsystem DDF の名称と担当者名のみを残して構文照合の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で構文照合の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず構文照合の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合の保守管理において選択記号 A を採用し、識別名は構文照合です。構文照合の保守管理において Subsystem DDF は説明欄の「Subsystem DDF の用途を保守管理の表示で確認する構文照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の保守管理に関連して、SMP/E SMF WLM では Subsystem DDF の表示属性と IWM025I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の保守管理は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の保守管理は別カテゴリの確認を流用しており、Subsystem DDF の根拠にならないため構文照合ではありません。 D: 構文照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため構文照合ではありません。構文照合の保守管理で使う Subsystem DDF という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は構文照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem DDF**

    - 検証目的: 比較判定の保守管理について、Subsystem DDF は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030094の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、比較判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem DDFを指定し、OSKB030094の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem DDF
    CASE OSKB030094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem DDF
    CASE OSKB030094
    SOURCE SMP/E SMF WLM
    ```

    Subsystem DDFとOSKB030094が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030094を同じ出力で読み、比較判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030094
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030094
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem DDF REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030094が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem DDF と OSKB030094 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem IMS {#c28-i0312}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem IMSは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 監査確認の保守管理で保守管理の運用確認を行います。Subsystem IMS の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で監査確認の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず監査確認の保守管理を正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、監査確認の証跡として残す。 ✅
    - D. Subsystem IMS の属性行を読まず監査確認の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認の保守管理において選択記号 C を採用し、識別名は監査確認です。監査確認の保守管理において Subsystem IMS は説明欄の「SMP/E SMF WLM で Subsystem IMS の扱いを記録する監査確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の保守管理を受け取る担当者は、Subsystem IMS の表示結果と IWM025I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の保守管理は別カテゴリの確認を流用しており、Subsystem IMS の根拠にならないため監査確認ではありません。 B: 監査確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため監査確認ではありません。 C: 監査確認の保守管理は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の保守管理が示す Subsystem IMS は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem IMS**

    - 検証目的: 優先判定の保守管理について、Subsystem IMS は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030092の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem IMSを指定し、OSKB030092の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem IMS
    CASE OSKB030092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem IMS
    CASE OSKB030092
    SOURCE SMP/E SMF WLM
    ```

    Subsystem IMSとOSKB030092が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030092を同じ出力で読み、優先判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030092
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030092
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem IMS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030092が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem IMS と OSKB030092 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem JES {#c28-i0313}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem JESは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 記録確認の保守管理に関係する Subsystem JES の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録確認の確認にする。 ✅
    - B. Subsystem JES の名称と担当者名のみを残して記録確認の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で記録確認の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず記録確認の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認の保守管理において選択記号 A を採用し、識別名は記録確認です。記録確認の保守管理において Subsystem JES は説明欄の「Subsystem JES の用途を保守管理の表示で確認する記録確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の保守管理に関連して、SMP/E SMF WLM では Subsystem JES の表示属性と IWM025I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の保守管理は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の保守管理は別カテゴリの確認を流用しており、Subsystem JES の根拠にならないため記録確認ではありません。 D: 記録確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため記録確認ではありません。記録確認の保守管理で使う Subsystem JES という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は記録確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem JES**

    - 検証目的: 探索判定の保守管理について、Subsystem JES は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030086の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、探索判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem JESを指定し、OSKB030086の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem JES
    CASE OSKB030086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem JES
    CASE OSKB030086
    SOURCE SMP/E SMF WLM
    ```

    Subsystem JESとOSKB030086が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030086を同じ出力で読み、探索判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030086
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030086
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem JES REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030086が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem JES と OSKB030086 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem MQ {#c28-i0314}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem MQは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 展開照合の保守管理で Subsystem MQ の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Subsystem MQ の出力を取らず展開照合の保守管理の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IWM025I を読み、展開照合の結果として保存する。 ✅
    - C. D WLM,SYSTEMS を省略して展開照合の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合の保守管理において選択記号 B を採用し、識別名は展開照合です。展開照合の保守管理において Subsystem MQ は説明欄の「展開照合の保守管理に関係する定義値と表示行を照合する展開照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の保守管理の証跡を読む担当者は、Subsystem MQ の属性行と IWM025I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の保守管理は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため展開照合ではありません。 D: 展開照合の保守管理は別カテゴリの確認を流用しており、Subsystem MQ の根拠にならないため展開照合ではありません。展開照合の保守管理に出る Subsystem MQ は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は展開照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem MQ**

    - 検証目的: 順序判定の保守管理について、Subsystem MQ は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030095の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、順序判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem MQを指定し、OSKB030095の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem MQ
    CASE OSKB030095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem MQ
    CASE OSKB030095
    SOURCE SMP/E SMF WLM
    ```

    Subsystem MQとOSKB030095が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030095を同じ出力で読み、順序判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030095
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030095
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem MQ REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030095が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem MQ と OSKB030095 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem NETV {#c28-i0315}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem NETVは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 呼出照合の保守管理で保守管理の運用確認を行います。Subsystem NETV の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で呼出照合の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず呼出照合の保守管理を正常終了として記録する。
    - C. D WLM,SYSTEMS で得た表示本文を使い、呼出照合の採否を説明欄に結び付ける。 ✅
    - D. Subsystem NETV の属性行を読まず呼出照合の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合の保守管理において選択記号 C を採用し、識別名は呼出照合です。呼出照合の保守管理において Subsystem NETV は説明欄の「SMP/E SMF WLM で Subsystem NETV の扱いを記録する呼出照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の保守管理を受け取る担当者は、Subsystem NETV の表示結果と IWM025I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の保守管理は別カテゴリの確認を流用しており、Subsystem NETV の根拠にならないため呼出照合ではありません。 B: 呼出照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の保守管理は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の保守管理が示す Subsystem NETV は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem NETV**

    - 検証目的: 値域判定の保守管理について、Subsystem NETV は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030096の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、値域判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem NETVを指定し、OSKB030096の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem NETV
    CASE OSKB030096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem NETV
    CASE OSKB030096
    SOURCE SMP/E SMF WLM
    ```

    Subsystem NETVとOSKB030096が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030096を同じ出力で読み、値域判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030096
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030096
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem NETV REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030096が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem NETV と OSKB030096 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem OMVS {#c28-i0316}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem OMVSは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 値域確認の保守管理に関する Subsystem OMVS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域確認の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の保守管理の証跡として保存して根拠にする。
    - C. Subsystem OMVS の変更点を出力本文から切り離して値域確認の保守管理の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認の保守管理において選択記号 D を採用し、識別名は値域確認です。値域確認の保守管理において Subsystem OMVS は説明欄の「Subsystem OMVS の状態と出力メッセージを結び付ける値域確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の保守管理に関する記録は、Subsystem OMVS の出力行と IWM025I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域確認ではありません。 B: 値域確認の保守管理は別カテゴリの確認を流用しており、Subsystem OMVS の根拠にならないため値域確認ではありません。 C: 値域確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の保守管理は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の保守管理で記録する Subsystem OMVS は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem OMVS**

    - 検証目的: 条件判定の保守管理について、Subsystem OMVS は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030089の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、条件判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem OMVSを指定し、OSKB030089の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem OMVS
    CASE OSKB030089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem OMVS
    CASE OSKB030089
    SOURCE SMP/E SMF WLM
    ```

    Subsystem OMVSとOSKB030089が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030089を同じ出力で読み、条件判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030089
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030089
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem OMVS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030089が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem OMVS と OSKB030089 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem STC {#c28-i0317}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem STCは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 順序確認の保守管理で保守管理の運用確認を行います。Subsystem STC の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で順序確認の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず順序確認の保守管理を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序確認で再確認できる形にする。 ✅
    - D. Subsystem STC の属性行を読まず順序確認の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認の保守管理において選択記号 C を採用し、識別名は順序確認です。順序確認の保守管理において Subsystem STC は説明欄の「SMP/E SMF WLM で Subsystem STC の扱いを記録する順序確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の保守管理を受け取る担当者は、Subsystem STC の表示結果と IWM025I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の保守管理は別カテゴリの確認を流用しており、Subsystem STC の根拠にならないため順序確認ではありません。 B: 順序確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため順序確認ではありません。 C: 順序確認の保守管理は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の保守管理が示す Subsystem STC は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem STC**

    - 検証目的: 出力判定の保守管理について、Subsystem STC は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030088の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、出力判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem STCを指定し、OSKB030088の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem STC
    CASE OSKB030088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem STC
    CASE OSKB030088
    SOURCE SMP/E SMF WLM
    ```

    Subsystem STCとOSKB030088が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030088を同じ出力で読み、出力判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030088
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030088
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem STC REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030088が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem STC と OSKB030088 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem TCP {#c28-i0318}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem TCPは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 置換照合の保守管理に関する Subsystem TCP の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず置換照合の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の保守管理の証跡として保存して根拠にする。
    - C. Subsystem TCP の変更点を出力本文から切り離して置換照合の保守管理の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、置換照合として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合の保守管理において選択記号 D を採用し、識別名は置換照合です。置換照合の保守管理において Subsystem TCP は説明欄の「Subsystem TCP の状態と出力メッセージを結び付ける置換照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の保守管理に関する記録は、Subsystem TCP の出力行と IWM025I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため置換照合ではありません。 B: 置換照合の保守管理は別カテゴリの確認を流用しており、Subsystem TCP の根拠にならないため置換照合ではありません。 C: 置換照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の保守管理は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の保守管理で記録する Subsystem TCP は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は置換照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem TCP**

    - 検証目的: 警告判定の保守管理について、Subsystem TCP は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030097の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、警告判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem TCPを指定し、OSKB030097の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem TCP
    CASE OSKB030097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem TCP
    CASE OSKB030097
    SOURCE SMP/E SMF WLM
    ```

    Subsystem TCPとOSKB030097が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030097を同じ出力で読み、警告判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030097
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030097
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem TCP REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030097が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem TCP と OSKB030097 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Subsystem TSO {#c28-i0319}
*分類: WLM Classification Rules*  ・  難易度: 上級

Subsystem TSOは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 比較確認の保守管理で Subsystem TSO の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Subsystem TSO の出力を取らず比較確認の保守管理の説明文と承認印のみを残す。
    - B. SMP/E SMF WLM の表示形式に沿って根拠行を採り、比較確認の点検結果を残す。 ✅
    - C. D WLM,SYSTEMS を省略して比較確認の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認の保守管理において選択記号 B を採用し、識別名は比較確認です。比較確認の保守管理において Subsystem TSO は説明欄の「比較確認の保守管理に関係する定義値と表示行を照合する比較確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の保守管理の証跡を読む担当者は、Subsystem TSO の属性行と IWM025I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の保守管理は対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため比較確認ではありません。 D: 比較確認の保守管理は別カテゴリの確認を流用しており、Subsystem TSO の根拠にならないため比較確認ではありません。比較確認の保守管理に出る Subsystem TSO は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は比較確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Subsystem TSO**

    - 検証目的: 上書判定の保守管理について、Subsystem TSO は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030087の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、上書判定の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にSubsystem TSOを指定し、OSKB030087の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Subsystem TSO
    CASE OSKB030087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Subsystem TSO
    CASE OSKB030087
    SOURCE SMP/E SMF WLM
    ```

    Subsystem TSOとOSKB030087が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030087を同じ出力で読み、上書判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030087
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030087
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Subsystem TSO REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030087が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Subsystem TSO と OSKB030087 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### デフォルト Report Class {#c28-i0320}
*分類: WLM Classification Rules*  ・  難易度: 上級

デフォルト Report Classは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 変更照合のデフォルトに関するデフォルト Report Classの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず変更照合のデフォルトの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合のデフォルトの証跡として保存して根拠にする。
    - C. デフォルト Report Classの変更点を出力本文から切り離して変更照合のデフォルトの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、変更照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合のデフォルトにおいて選択記号 D を採用し、識別名は変更照合です。変更照合のデフォルトにおいてデフォルト Report Class は説明欄の「デフォルト Report Classの状態と出力メッセージを結び付ける変更照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のデフォルトに関する記録は、デフォルト Report Classの出力行と IWM025I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のデフォルトは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため変更照合ではありません。 B: 変更照合のデフォルトは別カテゴリの確認を流用しており、デフォルト Report Classの根拠にならないため変更照合ではありません。 C: 変更照合のデフォルトは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のデフォルトは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のデフォルトで記録するデフォルト Report Classは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **デフォルト Report Class**

    - 検証目的: 記録整理のデフォルトについて、デフォルト Report Classは、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030113の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、記録整理のデフォルトの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にデフォルト Report Classを指定し、OSKB030113の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND デフォルト Report Class
    CASE OSKB030113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM デフォルト Report Class
    CASE OSKB030113
    SOURCE SMP/E SMF WLM
    ```

    デフォルト Report ClassとOSKB030113が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030113を同じ出力で読み、記録整理のデフォルトの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030113
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030113
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I デフォルト Report Class REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030113が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の デフォルト Report Class と OSKB030113 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### デフォルト Service Class {#c28-i0321}
*分類: WLM Classification Rules*  ・  難易度: 上級

デフォルト Service Classは、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 監査照合のデフォルトで保守管理の運用確認を行います。デフォルト Service Classの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で監査照合のデフォルトを確認した扱いにする。
    - B. IWM025I の有無を確認せず監査照合のデフォルトを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査照合で再確認できる形にする。 ✅
    - D. デフォルト Service Classの属性行を読まず監査照合のデフォルトの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合のデフォルトにおいて選択記号 C を採用し、識別名は監査照合です。監査照合のデフォルトにおいてデフォルト Service Class は説明欄の「SMP/E SMF WLM でデフォルト Service Classの扱いを記録する監査照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のデフォルトを受け取る担当者は、デフォルト Service Classの表示結果と IWM025I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のデフォルトは別カテゴリの確認を流用しており、デフォルト Service Classの根拠にならないため監査照合ではありません。 B: 監査照合のデフォルトは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため監査照合ではありません。 C: 監査照合のデフォルトは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のデフォルトは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のデフォルトが示すデフォルト Service Classは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **デフォルト Service Class**

    - 検証目的: 優先整理のデフォルトについて、デフォルト Service Classは、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030112の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先整理のデフォルトの確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にデフォルト Service Clasを指定し、OSKB030112の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND デフォルト Service Clas
    CASE OSKB030112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM デフォルト Service Clas
    CASE OSKB030112
    SOURCE SMP/E SMF WLM
    ```

    デフォルト Service ClasとOSKB030112が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030112を同じ出力で読み、優先整理のデフォルトの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030112
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030112
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I デフォルト Service Class REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030112が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の デフォルト Service Clas と OSKB030112 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 CN (Connection Type) {#c28-i0322}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 CN (Connection Type)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 順序照合の条件で保守管理の運用確認を行います。条件 CN 属性の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で順序照合の条件を確認した扱いにする。
    - B. IWM025I の有無を確認せず順序照合の条件を正常終了として記録する。
    - C. D WLM,SYSTEMS で得た表示本文を使い、順序照合の採否を説明欄に結び付ける。 ✅
    - D. 条件 CN 属性の属性行を読まず順序照合の条件の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合の条件において選択記号 C を採用し、識別名は順序照合です。順序照合の条件において条件 CN 属性 は説明欄の「SMP/E SMF WLM で条件 CN 属性の扱いを記録する順序照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の条件を受け取る担当者は、条件 CN 属性の表示結果と IWM025I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の条件は別カテゴリの確認を流用しており、条件 CN 属性の根拠にならないため順序照合ではありません。 B: 順序照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため順序照合ではありません。 C: 順序照合の条件は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の条件が示す条件 CN 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 CN (Connection Type)**

    - 検証目的: 出力整理の条件について、条件 CN (Connection Type)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030108の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、出力整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 CN (Connection を指定し、OSKB030108の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 CN (Connection 
    CASE OSKB030108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 CN (Connection 
    CASE OSKB030108
    SOURCE SMP/E SMF WLM
    ```

    条件 CN (Connection とOSKB030108が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030108を同じ出力で読み、出力整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030108
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030108
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 CN (Connection Type) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030108が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 CN (Connection  と OSKB030108 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 PC (Procedure Name) {#c28-i0323}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 PC (Procedure Name)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 値域照合の条件に関する条件 PC 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域照合の条件の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の条件の証跡として保存して根拠にする。
    - C. 条件 PC 属性の変更点を出力本文から切り離して値域照合の条件の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、値域照合として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合の条件において選択記号 D を採用し、識別名は値域照合です。値域照合の条件において条件 PC 属性 は説明欄の「条件 PC 属性の状態と出力メッセージを結び付ける値域照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の条件に関する記録は、条件 PC 属性の出力行と IWM025I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域照合ではありません。 B: 値域照合の条件は別カテゴリの確認を流用しており、条件 PC 属性の根拠にならないため値域照合ではありません。 C: 値域照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の条件は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の条件で記録する条件 PC 属性は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 PC (Procedure Name)**

    - 検証目的: 条件整理の条件について、条件 PC (Procedure Name)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030109の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、条件整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 PC (Procedure Nを指定し、OSKB030109の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 PC (Procedure N
    CASE OSKB030109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 PC (Procedure N
    CASE OSKB030109
    SOURCE SMP/E SMF WLM
    ```

    条件 PC (Procedure NとOSKB030109が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030109を同じ出力で読み、条件整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030109
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030109
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 PC (Procedure Name) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030109が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 PC (Procedure N と OSKB030109 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 PF (Performance Group) {#c28-i0324}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 PF (Performance Group)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 記録照合の条件に関係する条件 PF 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて記録照合の根拠にする。 ✅
    - B. 条件 PF 属性の名称と担当者名のみを残して記録照合の条件の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で記録照合の条件を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず記録照合の条件の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合の条件において選択記号 A を採用し、識別名は記録照合です。記録照合の条件において条件 PF 属性 は説明欄の「条件 PF 属性の用途を保守管理の表示で確認する記録照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の条件に関連して、SMP/E SMF WLM では条件 PF 属性の表示属性と IWM025I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の条件は対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の条件は別カテゴリの確認を流用しており、条件 PF 属性の根拠にならないため記録照合ではありません。 D: 記録照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため記録照合ではありません。記録照合の条件で使う条件 PF 属性という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は記録照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 PF (Performance Group)**

    - 検証目的: 探索整理の条件について、条件 PF (Performance Group)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象とに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030106の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、探索整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 PF (Performanceを指定し、OSKB030106の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 PF (Performance
    CASE OSKB030106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 PF (Performance
    CASE OSKB030106
    SOURCE SMP/E SMF WLM
    ```

    条件 PF (PerformanceとOSKB030106が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030106を同じ出力で読み、探索整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030106
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030106
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 PF (Performance Group REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030106が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 PF (Performance と OSKB030106 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 PRGN (Performance Group No.) {#c28-i0325}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 PRGN (Performance Group No.)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 警告照合の条件に関係する条件 PRGN 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、警告照合の確認にする。 ✅
    - B. 条件 PRGN 属性の名称と担当者名のみを残して警告照合の条件の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告照合の条件を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告照合の条件の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合の条件において選択記号 A を採用し、識別名は警告照合です。警告照合の条件において条件 PRGN 属性 は説明欄の「条件 PRGN 属性の用途を保守管理の表示で確認する警告照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の条件に関連して、SMP/E SMF WLM では条件 PRGN 属性の表示属性と IWM025I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の条件は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の条件は別カテゴリの確認を流用しており、条件 PRGN 属性の根拠にならないため警告照合ではありません。 D: 警告照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告照合ではありません。警告照合の条件で使う条件 PRGN 属性という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 PRGN (Performance Group No.)**

    - 検証目的: 区切整理の条件について、条件 PRGN (Performance Group No.)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、またに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030110の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 PRGN (Performanを指定し、OSKB030110の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 PRGN (Performan
    CASE OSKB030110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 PRGN (Performan
    CASE OSKB030110
    SOURCE SMP/E SMF WLM
    ```

    条件 PRGN (PerformanとOSKB030110が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030110を同じ出力で読み、区切整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030110
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030110
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 PRGN (Performance Gro REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030110が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 PRGN (Performan と OSKB030110 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 PRI (Priority) {#c28-i0326}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 PRI (Priority)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 範囲照合の条件で保守管理の運用確認を行います。条件 PRI (Priority)の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で範囲照合の条件を確認した扱いにする。
    - B. IWM025I の有無を確認せず範囲照合の条件を正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、範囲照合の証跡として残す。 ✅
    - D. 条件 PRI (Priority)の属性行を読まず範囲照合の条件の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合の条件において選択記号 C を採用し、識別名は範囲照合です。範囲照合の条件において条件 PRI (Priority) は説明欄の「SMP/E SMF WLM で条件 PRI (Priority)の扱いを記録する範囲照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の条件を受け取る担当者は、条件 PRI (Priority)の表示結果と IWM025I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の条件は別カテゴリの確認を流用しており、条件 PRI (Priority)の根拠にならないため範囲照合ではありません。 B: 範囲照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の条件は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の条件が示す条件 PRI (Priority)は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 PRI (Priority)**

    - 検証目的: 置換整理の条件について、条件 PRI (Priority)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030104の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、置換整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 PRI (Priority)を指定し、OSKB030104の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 PRI (Priority)
    CASE OSKB030104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 PRI (Priority)
    CASE OSKB030104
    SOURCE SMP/E SMF WLM
    ```

    条件 PRI (Priority)とOSKB030104が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030104を同じ出力で読み、置換整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030104
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030104
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 PRI (Priority) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030104が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 PRI (Priority) と OSKB030104 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 PRINT (Print Class) {#c28-i0327}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 PRINT (Print Class)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 比較照合の条件で条件 PRINT 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 条件 PRINT 属性の出力を取らず比較照合の条件の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IWM025I を読み、比較照合の結果として保存する。 ✅
    - C. D WLM,SYSTEMS を省略して比較照合の条件の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の条件へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較照合の条件において選択記号 B を採用し、識別名は比較照合です。比較照合の条件において条件 PRINT 属性 は説明欄の「比較照合の条件に関係する定義値と表示行を照合する比較照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の条件の証跡を読む担当者は、条件 PRINT 属性の属性行と IWM025I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の条件は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため比較照合ではありません。 D: 比較照合の条件は別カテゴリの確認を流用しており、条件 PRINT 属性の根拠にならないため比較照合ではありません。比較照合の条件に出る条件 PRINT 属性は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は比較照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 PRINT (Print Class)**

    - 検証目的: 上書整理の条件について、条件 PRINT (Print Class)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030107の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、上書整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 PRINT (Print Clを指定し、OSKB030107の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 PRINT (Print Cl
    CASE OSKB030107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 PRINT (Print Cl
    CASE OSKB030107
    SOURCE SMP/E SMF WLM
    ```

    条件 PRINT (Print ClとOSKB030107が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030107を同じ出力で読み、上書整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030107
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030107
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 PRINT (Print Class) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030107が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 PRINT (Print Cl と OSKB030107 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 PX (Sysplex Name) {#c28-i0328}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 PX (Sysplex Name)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 優先照合の条件に関する条件 PX 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず優先照合の条件の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の条件の証跡として保存して根拠にする。
    - C. 条件 PX 属性の変更点を出力本文から切り離して優先照合の条件の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、優先照合の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合の条件において選択記号 D を採用し、識別名は優先照合です。優先照合の条件において条件 PX 属性 は説明欄の「条件 PX 属性の状態と出力メッセージを結び付ける優先照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の条件に関する記録は、条件 PX 属性の出力行と IWM025I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため優先照合ではありません。 B: 優先照合の条件は別カテゴリの確認を流用しており、条件 PX 属性の根拠にならないため優先照合ではありません。 C: 優先照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の条件は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の条件で記録する条件 PX 属性は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は優先照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 PX (Sysplex Name)**

    - 検証目的: 終端整理の条件について、条件 PX (Sysplex Name)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030105の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、終端整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 PX (Sysplex Namを指定し、OSKB030105の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 PX (Sysplex Nam
    CASE OSKB030105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 PX (Sysplex Nam
    CASE OSKB030105
    SOURCE SMP/E SMF WLM
    ```

    条件 PX (Sysplex NamとOSKB030105が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030105を同じ出力で読み、終端整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030105
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030105
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 PX (Sysplex Name) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030105が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 PX (Sysplex Nam と OSKB030105 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 SC (Service Class) {#c28-i0329}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 SC (Service Class)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 条件照合の条件に関係する条件 SC 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて条件照合の根拠を固定する。 ✅
    - B. 条件 SC 属性の名称と担当者名のみを残して条件照合の条件の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で条件照合の条件を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず条件照合の条件の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合の条件において選択記号 A を採用し、識別名は条件照合です。条件照合の条件において条件 SC 属性 は説明欄の「条件 SC 属性の用途を保守管理の表示で確認する条件照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の条件に関連して、SMP/E SMF WLM では条件 SC 属性の表示属性と IWM025I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の条件は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の条件は別カテゴリの確認を流用しており、条件 SC 属性の根拠にならないため条件照合ではありません。 D: 条件照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため条件照合ではありません。条件照合の条件で使う条件 SC 属性という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は条件照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 SC (Service Class)**

    - 検証目的: 展開整理の条件について、条件 SC (Service Class)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030102の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、展開整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 SC (Service Claを指定し、OSKB030102の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 SC (Service Cla
    CASE OSKB030102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 SC (Service Cla
    CASE OSKB030102
    SOURCE SMP/E SMF WLM
    ```

    条件 SC (Service ClaとOSKB030102が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030102を同じ出力で読み、展開整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030102
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030102
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 SC (Service Class) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030102が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 SC (Service Cla と OSKB030102 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 SE (Scheduling Env) {#c28-i0330}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 SE (Scheduling Env)は、SMP/E / SMF / WLMのWLM Classification Rulesで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 復旧照合の条件で条件 SE 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 条件 SE 属性の出力を取らず復旧照合の条件の説明文と承認印のみを残す。
    - B. SMP/E SMF WLM の表示形式に沿って根拠行を採り、復旧照合の点検結果を残す。 ✅
    - C. D WLM,SYSTEMS を省略して復旧照合の条件の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の条件へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合の条件において選択記号 B を採用し、識別名は復旧照合です。復旧照合の条件において条件 SE 属性 は説明欄の「復旧照合の条件に関係する定義値と表示行を照合する復旧照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の条件の証跡を読む担当者は、条件 SE 属性の属性行と IWM025I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の条件は対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の条件は別カテゴリの確認を流用しており、条件 SE 属性の根拠にならないため復旧照合ではありません。復旧照合の条件に出る条件 SE 属性は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 SE (Scheduling Env)**

    - 検証目的: 範囲整理の条件について、条件 SE (Scheduling Env)は、SMP/E / SMF / WLM の WLM Classification Rulesで自動化処理や復旧動作を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030111の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 SE (Scheduling を指定し、OSKB030111の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 SE (Scheduling 
    CASE OSKB030111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 SE (Scheduling 
    CASE OSKB030111
    SOURCE SMP/E SMF WLM
    ```

    条件 SE (Scheduling とOSKB030111が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030111を同じ出力で読み、範囲整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030111
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030111
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 SE (Scheduling Env) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030111が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 SE (Scheduling  と OSKB030111 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 SI (Subsystem Instance) {#c28-i0331}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 SI (Subsystem Instance)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 上書照合の条件で保守管理の運用確認を行います。条件 SI 属性の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で上書照合の条件を確認した扱いにする。
    - B. IWM025I の有無を確認せず上書照合の条件を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、上書照合で再確認できる形にする。 ✅
    - D. 条件 SI 属性の属性行を読まず上書照合の条件の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合の条件において選択記号 C を採用し、識別名は上書照合です。上書照合の条件において条件 SI 属性 は説明欄の「SMP/E SMF WLM で条件 SI 属性の扱いを記録する上書照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の条件を受け取る担当者は、条件 SI 属性の表示結果と IWM025I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の条件は別カテゴリの確認を流用しており、条件 SI 属性の根拠にならないため上書照合ではありません。 B: 上書照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため上書照合ではありません。 C: 上書照合の条件は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の条件が示す条件 SI 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 SI (Subsystem Instance)**

    - 検証目的: 変更判定の条件について、条件 SI (Subsystem Instance)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030100の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、変更判定の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 SI (Subsystem Iを指定し、OSKB030100の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 SI (Subsystem I
    CASE OSKB030100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 SI (Subsystem I
    CASE OSKB030100
    SOURCE SMP/E SMF WLM
    ```

    条件 SI (Subsystem IとOSKB030100が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030100を同じ出力で読み、変更判定の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030100
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030100
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 SI (Subsystem Instanc REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030100が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 SI (Subsystem I と OSKB030100 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 SY (System Name) {#c28-i0332}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 SY (System Name)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 出力照合の条件に関する条件 SY 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず出力照合の条件の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の条件の証跡として保存して根拠にする。
    - C. 条件 SY 属性の変更点を出力本文から切り離して出力照合の条件の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、出力照合の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合の条件において選択記号 D を採用し、識別名は出力照合です。出力照合の条件において条件 SY 属性 は説明欄の「条件 SY 属性の状態と出力メッセージを結び付ける出力照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の条件に関する記録は、条件 SY 属性の出力行と IWM025I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため出力照合ではありません。 B: 出力照合の条件は別カテゴリの確認を流用しており、条件 SY 属性の根拠にならないため出力照合ではありません。 C: 出力照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の条件は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の条件で記録する条件 SY 属性は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は出力照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 SY (System Name)**

    - 検証目的: 構文整理の条件について、条件 SY (System Name)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030101の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、構文整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 SY (System Nameを指定し、OSKB030101の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 SY (System Name
    CASE OSKB030101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 SY (System Name
    CASE OSKB030101
    SOURCE SMP/E SMF WLM
    ```

    条件 SY (System NameとOSKB030101が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030101を同じ出力で読み、構文整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030101
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030101
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 SY (System Name) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030101が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 SY (System Name と OSKB030101 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 TC (Transaction Class) {#c28-i0333}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 TC (Transaction Class)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 探索照合の条件で条件 TC 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 条件 TC 属性の出力を取らず探索照合の条件の説明文と承認印のみを残す。
    - B. SMP/E SMF WLM の表示形式に沿って根拠行を採り、探索照合の点検結果を残す。 ✅
    - C. D WLM,SYSTEMS を省略して探索照合の条件の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の条件へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合の条件において選択記号 B を採用し、識別名は探索照合です。探索照合の条件において条件 TC 属性 は説明欄の「探索照合の条件に関係する定義値と表示行を照合する探索照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の条件の証跡を読む担当者は、条件 TC 属性の属性行と IWM025I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の条件は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため探索照合ではありません。 D: 探索照合の条件は別カテゴリの確認を流用しており、条件 TC 属性の根拠にならないため探索照合ではありません。探索照合の条件に出る条件 TC 属性は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は探索照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 TC (Transaction Class)**

    - 検証目的: 監査判定の条件について、条件 TC (Transaction Class)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象とに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030099の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、監査判定の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 TC (Transactionを指定し、OSKB030099の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 TC (Transaction
    CASE OSKB030099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 TC (Transaction
    CASE OSKB030099
    SOURCE SMP/E SMF WLM
    ```

    条件 TC (TransactionとOSKB030099が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030099を同じ出力で読み、監査判定の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030099
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030099
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 TC (Transaction Class REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030099が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 TC (Transaction と OSKB030099 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 TN (Transaction Name) {#c28-i0334}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 TN (Transaction Name)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 終端照合の条件に関係する条件 TN 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、終端照合の確認にする。 ✅
    - B. 条件 TN 属性の名称と担当者名のみを残して終端照合の条件の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で終端照合の条件を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず終端照合の条件の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合の条件において選択記号 A を採用し、識別名は終端照合です。終端照合の条件において条件 TN 属性 は説明欄の「条件 TN 属性の用途を保守管理の表示で確認する終端照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の条件に関連して、SMP/E SMF WLM では条件 TN 属性の表示属性と IWM025I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の条件は対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の条件は別カテゴリの確認を流用しており、条件 TN 属性の根拠にならないため終端照合ではありません。 D: 終端照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため終端照合ではありません。終端照合の条件で使う条件 TN 属性という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は終端照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 TN (Transaction Name)**

    - 検証目的: 復旧判定の条件について、条件 TN (Transaction Name)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象としに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030098の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、復旧判定の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 TN (Transactionを指定し、OSKB030098の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 TN (Transaction
    CASE OSKB030098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 TN (Transaction
    CASE OSKB030098
    SOURCE SMP/E SMF WLM
    ```

    条件 TN (TransactionとOSKB030098が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030098を同じ出力で読み、復旧判定の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030098
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030098
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 TN (Transaction Name) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030098が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 TN (Transaction と OSKB030098 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 条件 UI (User ID) {#c28-i0335}
*分類: WLM Classification Rules*  ・  難易度: 上級

条件 UI (User ID)は、SMP/E / SMF / WLMのWLM Classification Rulesで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 区切照合の条件で条件 UI (User ID)の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 条件 UI (User ID)の出力を取らず区切照合の条件の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を区切照合で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して区切照合の条件の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の条件へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合の条件において選択記号 B を採用し、識別名は区切照合です。区切照合の条件において条件 UI (User ID) は説明欄の「区切照合の条件に関係する定義値と表示行を照合する区切照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の条件の証跡を読む担当者は、条件 UI (User ID)の属性行と IWM025I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の条件は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の条件は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の条件は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため区切照合ではありません。 D: 区切照合の条件は別カテゴリの確認を流用しており、条件 UI (User ID)の根拠にならないため区切照合ではありません。区切照合の条件に出る条件 UI (User ID)は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は区切照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **条件 UI (User ID)**

    - 検証目的: 呼出整理の条件について、条件 UI (User ID)は、SMP/E / SMF / WLM の WLM Classification Rulesで機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030103の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、呼出整理の条件の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄に条件 UI (User ID)を指定し、OSKB030103の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 条件 UI (User ID)
    CASE OSKB030103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 条件 UI (User ID)
    CASE OSKB030103
    SOURCE SMP/E SMF WLM
    ```

    条件 UI (User ID)とOSKB030103が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030103を同じ出力で読み、呼出整理の条件の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030103
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030103
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 条件 UI (User ID) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030103が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 条件 UI (User ID) と OSKB030103 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)




## SMP/E / SMF / WLM > WLM Resource Group

### Maximum capacity {#c28-i0336}
*分類: WLM Resource Group*  ・  難易度: 上級

Maximum capacityは、SMP/E / SMF / WLMのWLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 探索追跡の保守管理で Maximum capacityの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Maximum capacityの出力を取らず探索追跡の保守管理の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IWM025I を読み、探索追跡の結果として保存する。 ✅
    - C. D WLM,SYSTEMS を省略して探索追跡の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡の保守管理において選択記号 B を採用し、識別名は探索追跡です。探索追跡の保守管理において Maximum capacity は説明欄の「探索追跡の保守管理に関係する定義値と表示行を照合する探索追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の保守管理の証跡を読む担当者は、Maximum capacityの属性行と IWM025I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の保守管理は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の保守管理は別カテゴリの確認を流用しており、Maximum capacityの根拠にならないため探索追跡ではありません。探索追跡の保守管理に出る Maximum capacityは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Maximum capacity**

    - 検証目的: 監査整理の保守管理について、Maximum capacityは、SMP/E / SMF / WLM の WLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030119の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、監査整理の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にMaximum capacityを指定し、OSKB030119の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Maximum capacity
    CASE OSKB030119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Maximum capacity
    CASE OSKB030119
    SOURCE SMP/E SMF WLM
    ```

    Maximum capacityとOSKB030119が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030119を同じ出力で読み、監査整理の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030119
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030119
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Maximum capacity REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030119が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Maximum capacity と OSKB030119 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Minimum capacity {#c28-i0337}
*分類: WLM Resource Group*  ・  難易度: 上級

Minimum capacityは、SMP/E / SMF / WLMのWLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 上書追跡の保守管理で保守管理の運用確認を行います。Minimum capacityの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で上書追跡の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず上書追跡の保守管理を正常終了として記録する。
    - C. D WLM,SYSTEMS で得た表示本文を使い、上書追跡の採否を説明欄に結び付ける。 ✅
    - D. Minimum capacityの属性行を読まず上書追跡の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡の保守管理において選択記号 C を採用し、識別名は上書追跡です。上書追跡の保守管理において Minimum capacity は説明欄の「SMP/E SMF WLM で Minimum capacityの扱いを記録する上書追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の保守管理を受け取る担当者は、Minimum capacityの表示結果と IWM025I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の保守管理は別カテゴリの確認を流用しており、Minimum capacityの根拠にならないため上書追跡ではありません。 B: 上書追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の保守管理は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の保守管理が示す Minimum capacityは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Minimum capacity**

    - 検証目的: 変更整理の保守管理について、Minimum capacityは、SMP/E / SMF / WLM の WLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030120の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、変更整理の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にMinimum capacityを指定し、OSKB030120の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Minimum capacity
    CASE OSKB030120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Minimum capacity
    CASE OSKB030120
    SOURCE SMP/E SMF WLM
    ```

    Minimum capacityとOSKB030120が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030120を同じ出力で読み、変更整理の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030120
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030120
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Minimum capacity REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030120が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Minimum capacity と OSKB030120 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Resource Group の役割 {#c28-i0338}
*分類: WLM Resource Group*  ・  難易度: 上級

Resource Group の役割は、SMP/E / SMF / WLMのWLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 展開追跡のの役割で Resource Group の役割の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Resource Group の役割の出力を取らず展開追跡のの役割の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を展開追跡で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して展開追跡のの役割の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡のの役割へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡のの役割において選択記号 B を採用し、識別名は展開追跡です。展開追跡のの役割において Resource Group の役割 は説明欄の「展開追跡のの役割に関係する定義値と表示行を照合する展開追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のの役割の証跡を読む担当者は、Resource Group の役割の属性行と IWM025I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のの役割は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のの役割は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のの役割は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のの役割は別カテゴリの確認を流用しており、Resource Group の役割の根拠にならないため展開追跡ではありません。展開追跡のの役割に出る Resource Group の役割は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Resource Group の役割**

    - 検証目的: 順序整理のの役割について、Resource Group の役割は、SMP/E / SMF / WLM の WLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030115の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、順序整理のの役割の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にResource Group の役割を指定し、OSKB030115の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Resource Group の役割
    CASE OSKB030115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Resource Group の役割
    CASE OSKB030115
    SOURCE SMP/E SMF WLM
    ```

    Resource Group の役割とOSKB030115が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030115を同じ出力で読み、順序整理のの役割の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030115
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030115
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Resource Group の役割 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030115が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Resource Group の役割 と OSKB030115 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Type 1 SU/sec {#c28-i0339}
*分類: WLM Resource Group*  ・  難易度: 上級

Type 1 SU/secは、SMP/E / SMF / WLMのWLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 呼出追跡のType 1 SU/secで保守管理の運用確認を行います。Type 1 SU ・secの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で呼出追跡のType 1 SU/secを確認した扱いにする。
    - B. IWM025I の有無を確認せず呼出追跡のType 1 SU/secを正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、呼出追跡の証跡として残す。 ✅
    - D. Type 1 SU ・secの属性行を読まず呼出追跡のType 1 SU/secの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡のType 1 SU/secにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のType 1 SU/secにおいて Type 1 SU ・sec は説明欄の「SMP/E SMF WLM で Type 1 SU ・secの扱いを記録する呼出追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のType 1 SU/secを受け取る担当者は、Type 1 SU ・secの表示結果と IWM025I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のType 1 SU/secは別カテゴリの確認を流用しており、Type 1 SU ・secの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のType 1 SU/secは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のType 1 SU/secは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のType 1 SU/secは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のType 1 SU/secが示す Type 1 SU ・secは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Type 1 SU ・sec**

    - 検証目的: 値域整理の・について、Type 1 SU/secは、SMP/E / SMF / WLM の WLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソーに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030116の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、値域整理の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にType 1 SU ・secを指定し、OSKB030116の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Type 1 SU ・sec
    CASE OSKB030116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Type 1 SU ・sec
    CASE OSKB030116
    SOURCE SMP/E SMF WLM
    ```

    Type 1 SU ・secとOSKB030116が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030116を同じ出力で読み、値域整理の・の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030116
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030116
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Type 1 SU ・sec REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030116が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Type 1 SU ・sec と OSKB030116 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Type 2 % LPAR Share {#c28-i0340}
*分類: WLM Resource Group*  ・  難易度: 上級

Type 2 % LPAR Shareは、SMP/E / SMF / WLMのWLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 置換追跡の%に関する Type 2 % LPAR Shareの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず置換追跡の%の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の%の証跡として保存して根拠にする。
    - C. Type 2 % LPAR Shareの変更点を出力本文から切り離して置換追跡の%の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、置換追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡の%において選択記号 D を採用し、識別名は置換追跡です。置換追跡の%において Type 2 % LPAR Share は説明欄の「Type 2 % LPAR Shareの状態と出力メッセージを結び付ける置換追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の%に関する記録は、Type 2 % LPAR Shareの出力行と IWM025I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の%は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の%は別カテゴリの確認を流用しており、Type 2 % LPAR Shareの根拠にならないため置換追跡ではありません。 C: 置換追跡の%は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の%は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の%で記録する Type 2 % LPAR Shareは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Type 2 % LPAR Share**

    - 検証目的: 警告整理の%について、Type 2 % LPAR Shareは、SMP/E / SMF / WLM の WLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目ですに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030117の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、警告整理の%の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にType 2 % LPAR Sharを指定し、OSKB030117の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Type 2 % LPAR Shar
    CASE OSKB030117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Type 2 % LPAR Shar
    CASE OSKB030117
    SOURCE SMP/E SMF WLM
    ```

    Type 2 % LPAR SharとOSKB030117が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030117を同じ出力で読み、警告整理の%の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030117
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030117
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Type 2 % LPAR Share REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030117が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Type 2 % LPAR Shar と OSKB030117 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Type 3 % Sysplex Share {#c28-i0341}
*分類: WLM Resource Group*  ・  難易度: 上級

Type 3 % Sysplex Shareは、SMP/E / SMF / WLMのWLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 終端追跡の%に関係する Type 3 % Sysplex Shareの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて終端追跡の根拠にする。 ✅
    - B. Type 3 % Sysplex Shareの名称と担当者名のみを残して終端追跡の%の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で終端追跡の%を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず終端追跡の%の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡の%において選択記号 A を採用し、識別名は終端追跡です。終端追跡の%において Type 3 % Sysplex Share は説明欄の「Type 3 % Sysplex Shareの用途を保守管理の表示で確認する終端追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の%に関連して、SMP/E SMF WLM では Type 3 % Sysplex Shareの表示属性と IWM025I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の%は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の%は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の%は別カテゴリの確認を流用しており、Type 3 % Sysplex Shareの根拠にならないため終端追跡ではありません。 D: 終端追跡の%は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため終端追跡ではありません。終端追跡の%で使う Type 3 % Sysplex Shareという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は終端追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Type 3 % Sysplex Share**

    - 検証目的: 復旧整理の%について、Type 3 % Sysplex Shareは、SMP/E / SMF / WLM の WLM Resource Groupでリソース定義、モデル、またはポリシーを読むための項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030118の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、復旧整理の%の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にType 3 % Sysplex Sを指定し、OSKB030118の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Type 3 % Sysplex S
    CASE OSKB030118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Type 3 % Sysplex S
    CASE OSKB030118
    SOURCE SMP/E SMF WLM
    ```

    Type 3 % Sysplex SとOSKB030118が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030118を同じ出力で読み、復旧整理の%の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030118
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030118
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Type 3 % Sysplex Share REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030118が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Type 3 % Sysplex S と OSKB030118 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)




## SMP/E / SMF / WLM > WLM Scheduling Environment

### F WLM,RESOURCE=name,OFF {#c28-i0342}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

F WLM,RESOURCE=name,OFFは、SMP/E / SMF / WLMのWLM Scheduling Environmentでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 値域追跡の保守管理に関する F WLM,RESOURCE=name,OFF の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域追跡の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡の保守管理の証跡として保存して根拠にする。
    - C. F WLM,RESOURCE=name,OFF の変更点を出力本文から切り離して値域追跡の保守管理の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、値域追跡の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域追跡の保守管理において選択記号 D を採用し、識別名は値域追跡です。値域追跡の保守管理において F WLM,RESOURCE=name,OFF は説明欄の「F WLM,RESOURCE=name,OFF の状態と出力メッセージを結び付ける値域追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域追跡です。値域追跡の保守管理に関する記録は、F WLM,RESOURCE=name,OFF の出力行と IWM025I を一緒に保存し、背景名は値域追跡です。選択肢ごとの違いを示します。 A: 値域追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域追跡ではありません。 B: 値域追跡の保守管理は別カテゴリの確認を流用しており、F WLM,RESOURCE=name,OFF の根拠にならないため値域追跡ではありません。 C: 値域追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため値域追跡ではありません。 D: 値域追跡の保守管理は対象出力と項目説明を結び、根拠を残すので値域追跡です。値域追跡の保守管理で記録する F WLM,RESOURCE=name,OFF は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **F WLM,RESOURCE=name,OFF**

    - 検証目的: 条件記録の保守管理について、F WLM,RESOURCE=name,OFF は、SMP/E / SMF / WLM の WLM Scheduling Environmentでリソース定義、モデル、またはポリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030129の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、条件記録の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にF WLM,RESOURCE=namを指定し、OSKB030129の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND F WLM,RESOURCE=nam
    CASE OSKB030129
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM F WLM,RESOURCE=nam
    CASE OSKB030129
    SOURCE SMP/E SMF WLM
    ```

    F WLM,RESOURCE=namとOSKB030129が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030129を同じ出力で読み、条件記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030129
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030129
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I F WLM,RESOURCE=name,OFF REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030129が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の F WLM,RESOURCE=nam と OSKB030129 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030129 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### F WLM,RESOURCE=name,ON {#c28-i0343}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

F WLM,RESOURCE=name,ONは、SMP/E / SMF / WLMのWLM Scheduling Environmentでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 順序追跡の保守管理で保守管理の運用確認を行います。F WLM,RESOURCE=name,ON の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で順序追跡の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず順序追跡の保守管理を正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、順序追跡の証跡として残す。 ✅
    - D. F WLM,RESOURCE=name,ON の属性行を読まず順序追跡の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序追跡の保守管理において選択記号 C を採用し、識別名は順序追跡です。順序追跡の保守管理において F WLM,RESOURCE=name,ON は説明欄の「SMP/E SMF WLM で F WLM,RESOURCE=name,ON の扱いを記録する順序追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は順序追跡です。順序追跡の保守管理を受け取る担当者は、F WLM,RESOURCE=name,ON の表示結果と IWM025I を同じ確認単位として扱い、背景名は順序追跡です。不適切な選択肢を整理します。 A: 順序追跡の保守管理は別カテゴリの確認を流用しており、F WLM,RESOURCE=name,ON の根拠にならないため順序追跡ではありません。 B: 順序追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため順序追跡ではありません。 C: 順序追跡の保守管理は対象出力と項目説明を結び、根拠を残すので順序追跡です。 D: 順序追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため順序追跡ではありません。順序追跡の保守管理が示す F WLM,RESOURCE=name,ON は出典欄の資料で使い方を追跡できる項目であり、用語名は順序追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **F WLM,RESOURCE=name,ON**

    - 検証目的: 出力記録の保守管理について、F WLM,RESOURCE=name,ON は、SMP/E / SMF / WLM の WLM Scheduling Environmentでリソース定義、モデル、またはポリシに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030128の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、出力記録の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にF WLM,RESOURCE=namを指定し、OSKB030128の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND F WLM,RESOURCE=nam
    CASE OSKB030128
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM F WLM,RESOURCE=nam
    CASE OSKB030128
    SOURCE SMP/E SMF WLM
    ```

    F WLM,RESOURCE=namとOSKB030128が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030128を同じ出力で読み、出力記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030128
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030128
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I F WLM,RESOURCE=name,ON REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030128が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の F WLM,RESOURCE=nam と OSKB030128 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030128 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### F WLM,RESOURCE=name,RESET {#c28-i0344}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

F WLM,RESOURCE=name,RESETは、SMP/E / SMF / WLMのWLM Scheduling Environmentでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 警告追跡の保守管理に関係する F WLM,RESOURCE=name,RESE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 属性行、戻り表示、メッセージ見出しを合わせて警告追跡の根拠にする。 ✅
    - B. F WLM,RESOURCE=name,RESE の名称と担当者名のみを残して警告追跡の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告追跡の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告追跡の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告追跡の保守管理において選択記号 A を採用し、識別名は警告追跡です。警告追跡の保守管理において F WLM,RESOURCE=name,RESE は説明欄の「F WLM,RESOURCE=name,RESE の用途を保守管理の表示で確認する警告追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告追跡です。警告追跡の保守管理に関連して、SMP/E SMF WLM では F WLM,RESOURCE=name,RESE の表示属性と IWM025I を同じ証跡に残し、背景名は警告追跡です。他の選択肢を確認します。 A: 警告追跡の保守管理は対象出力と項目説明を結び、根拠を残すので警告追跡です。 B: 警告追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため警告追跡ではありません。 C: 警告追跡の保守管理は別カテゴリの確認を流用しており、F WLM,RESOURCE=name,RESE の根拠にならないため警告追跡ではありません。 D: 警告追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告追跡ではありません。警告追跡の保守管理で使う F WLM,RESOURCE=name,RESE という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **F WLM,RESOURCE=name,RESET**

    - 検証目的: 区切記録の保守管理について、F WLM,RESOURCE=name,RESET は、SMP/E / SMF / WLM の WLM Scheduling Environmentでリソース定義、モデル、またはに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030130の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切記録の保守管理の確認表示へ進みます。
    操作（入力）:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E)
    COMMAND INPUT ===> D WLM,SYSTEMS
    ```

    COMMAND INPUTにD WLM,SYSTEMSが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はSMP/Eの表示結果です。FIND欄にF WLM,RESOURCE=namを指定し、OSKB030130の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND F WLM,RESOURCE=nam
    CASE OSKB030130
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM F WLM,RESOURCE=nam
    CASE OSKB030130
    SOURCE SMP/E SMF WLM
    ```

    F WLM,RESOURCE=namとOSKB030130が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030130を同じ出力で読み、区切記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030130
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030130
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I F WLM,RESOURCE=name,RESE REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030130が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の F WLM,RESOURCE=nam と OSKB030130 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030130 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)


