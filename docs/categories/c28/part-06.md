---
search:
  exclude: true
---

# SMP/E / SMF / WLM — 詳細 (6/7)

[← SMP/E / SMF / WLM の概要へ戻る](index.md)


## SMP/E / SMF / WLM > WLM Scheduling Environment

### Required Conditions {#c28-i0345}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

Required Conditionsは、SMP/E / SMF / WLMのWLM Scheduling Environmentで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 比較追跡の保守管理で Required Conditionsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Required Conditionsの出力を取らず比較追跡の保守管理の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を比較追跡で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して比較追跡の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡の保守管理において選択記号 B を採用し、識別名は比較追跡です。比較追跡の保守管理において Required Conditions は説明欄の「比較追跡の保守管理に関係する定義値と表示行を照合する比較追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は比較追跡です。比較追跡の保守管理の証跡を読む担当者は、Required Conditionsの属性行と IWM025I を合わせて追跡し、背景名は比較追跡です。誤答側の問題点を分けます。 A: 比較追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため比較追跡ではありません。 B: 比較追跡の保守管理は対象出力と項目説明を結び、根拠を残すので比較追跡です。 C: 比較追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため比較追跡ではありません。 D: 比較追跡の保守管理は別カテゴリの確認を流用しており、Required Conditionsの根拠にならないため比較追跡ではありません。比較追跡の保守管理に出る Required Conditionsは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は比較追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Required Conditions**

    - 検証目的: 上書記録の保守管理について、Required Conditionsは、SMP/E / SMF / WLM の WLM Scheduling Environmentで自動化処理や復旧動作を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030127の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、上書記録の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にRequired Conditionを指定し、OSKB030127の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Required Condition
    CASE OSKB030127
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Required Condition
    CASE OSKB030127
    SOURCE SMP/E SMF WLM
    ```

    Required ConditionとOSKB030127が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030127を同じ出力で読み、上書記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030127
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030127
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Required Conditions REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030127が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Required Condition と OSKB030127 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030127 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### Resource State {#c28-i0346}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

Resource Stateは、SMP/E / SMF / WLMのWLM Scheduling Environmentでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 記録追跡の保守管理に関係する Resource Stateの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて記録追跡の根拠を固定する。 ✅
    - B. Resource Stateの名称と担当者名のみを残して記録追跡の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で記録追跡の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず記録追跡の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録追跡の保守管理において選択記号 A を採用し、識別名は記録追跡です。記録追跡の保守管理において Resource State は説明欄の「Resource Stateの用途を保守管理の表示で確認する記録追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は記録追跡です。記録追跡の保守管理に関連して、SMP/E SMF WLM では Resource Stateの表示属性と IWM025I を同じ証跡に残し、背景名は記録追跡です。他の選択肢を確認します。 A: 記録追跡の保守管理は対象出力と項目説明を結び、根拠を残すので記録追跡です。 B: 記録追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため記録追跡ではありません。 C: 記録追跡の保守管理は別カテゴリの確認を流用しており、Resource Stateの根拠にならないため記録追跡ではありません。 D: 記録追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため記録追跡ではありません。記録追跡の保守管理で使う Resource Stateという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は記録追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Resource State**

    - 検証目的: 探索記録の保守管理について、Resource Stateは、SMP/E / SMF / WLM の WLM Scheduling Environmentでリソース定義、モデル、またはポリシーを読むための項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030126の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、探索記録の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にResource Stateを指定し、OSKB030126の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Resource State
    CASE OSKB030126
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Resource State
    CASE OSKB030126
    SOURCE SMP/E SMF WLM
    ```

    Resource StateとOSKB030126が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030126を同じ出力で読み、探索記録の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030126
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030126
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Resource State REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030126が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Resource State と OSKB030126 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030126 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### SE とは {#c28-i0347}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

SE とはは、SMP/E / SMF / WLMのWLM Scheduling Environmentで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? note "検証手順（1件）"
    **SE とは**

    - 検証目的: 終端記録のとはについて、SE とはは、SMP/E / SMF / WLM の WLM Scheduling Environmentで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030125の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、終端記録のとはの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にSE とはを指定し、OSKB030125の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND SE とは
    CASE OSKB030125
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM SE とは
    CASE OSKB030125
    SOURCE SMP/E SMF WLM
    ```

    SE とはとOSKB030125が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030125を同じ出力で読み、終端記録のとはの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030125
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030125
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I SE とは REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030125が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の SE とは と OSKB030125 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)



### ジョブカード SCHENV= {#c28-i0348}
*分類: WLM Scheduling Environment*  ・  難易度: 上級

ジョブカード SCHENV=は、SMP/E / SMF / WLMのWLM Scheduling Environmentで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)

??? question "確認問題（1問）"
    **問題.** 復旧追跡のジョブカードでジョブカード SCHENV= の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ジョブカード SCHENV= の出力を取らず復旧追跡のジョブカードの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IWM025I を読み、復旧追跡の結果として保存する。 ✅
    - C. D WLM,SYSTEMS を省略して復旧追跡のジョブカードの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡のジョブカードへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧追跡のジョブカードにおいて選択記号 B を採用し、識別名は復旧追跡です。復旧追跡のジョブカードにおいてジョブカード SCHENV= は説明欄の「復旧追跡のジョブカードに関係する定義値と表示行を照合する復旧追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧追跡です。復旧追跡のジョブカードの証跡を読む担当者は、ジョブカード SCHENV= の属性行と IWM025I を合わせて追跡し、背景名は復旧追跡です。誤答側の問題点を分けます。 A: 復旧追跡のジョブカードは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧追跡ではありません。 B: 復旧追跡のジョブカードは対象出力と項目説明を結び、根拠を残すので復旧追跡です。 C: 復旧追跡のジョブカードは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧追跡ではありません。 D: 復旧追跡のジョブカードは別カテゴリの確認を流用しており、ジョブカード SCHENV= の根拠にならないため復旧追跡ではありません。復旧追跡のジョブカードに出るジョブカード SCHENV= は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ジョブカード SCHENV=**

    - 検証目的: 範囲記録のジョブカードについて、ジョブカード SCHENV= は、SMP/E / SMF / WLM の WLM Scheduling Environmentで自動化処理や復旧動作を確認する項目です。起動条件、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030131の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲記録のジョブカードの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にジョブカード SCHENV=を指定し、OSKB030131の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ジョブカード SCHENV=
    CASE OSKB030131
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ジョブカード SCHENV=
    CASE OSKB030131
    SOURCE SMP/E SMF WLM
    ```

    ジョブカード SCHENV=とOSKB030131が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030131を同じ出力で読み、範囲記録のジョブカードの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030131
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030131
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ジョブカード SCHENV= REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030131が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ジョブカード SCHENV= と OSKB030131 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030131 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS System Messages (zOS31_ieam900)




## SMP/E / SMF / WLM > WLM Service Class

### Duration の単位 {#c28-i0349}
*分類: WLM Service Class*  ・  難易度: 上級

Duration の単位は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 探索確認のの単位で Duration の単位の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Duration の単位の出力を取らず探索確認のの単位の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を探索確認で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して探索確認のの単位の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のの単位へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認のの単位において選択記号 B を採用し、識別名は探索確認です。探索確認のの単位において Duration の単位 は説明欄の「探索確認のの単位に関係する定義値と表示行を照合する探索確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のの単位の証跡を読む担当者は、Duration の単位の属性行と IWM025I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のの単位は名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のの単位は対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のの単位は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため探索確認ではありません。 D: 探索確認のの単位は別カテゴリの確認を流用しており、Duration の単位の根拠にならないため探索確認ではありません。探索確認のの単位に出る Duration の単位は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は探索確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Duration の単位**

    - 検証目的: 監査検査のの単位について、Duration の単位は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030079の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、監査検査のの単位の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にDuration の単位を指定し、OSKB030079の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Duration の単位
    CASE OSKB030079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Duration の単位
    CASE OSKB030079
    SOURCE SMP/E SMF WLM
    ```

    Duration の単位とOSKB030079が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030079を同じ出力で読み、監査検査のの単位の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030079
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030079
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Duration の単位 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030079が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Duration の単位 と OSKB030079 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Honor Priority {#c28-i0350}
*分類: WLM Service Class*  ・  難易度: 上級

Honor Priorityは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 優先確認の保守管理に関する Honor Priorityの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず優先確認の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の保守管理の証跡として保存して根拠にする。
    - C. Honor Priorityの変更点を出力本文から切り離して優先確認の保守管理の承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先確認として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認の保守管理において選択記号 D を採用し、識別名は優先確認です。優先確認の保守管理において Honor Priority は説明欄の「Honor Priorityの状態と出力メッセージを結び付ける優先確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の保守管理に関する記録は、Honor Priorityの出力行と IWM025I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため優先確認ではありません。 B: 優先確認の保守管理は別カテゴリの確認を流用しており、Honor Priorityの根拠にならないため優先確認ではありません。 C: 優先確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の保守管理は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の保守管理で記録する Honor Priorityは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は優先確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Honor Priority**

    - 検証目的: 終端判定の保守管理について、Honor Priorityは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030085の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、終端判定の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にHonor Priorityを指定し、OSKB030085の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Honor Priority
    CASE OSKB030085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Honor Priority
    CASE OSKB030085
    SOURCE SMP/E SMF WLM
    ```

    Honor PriorityとOSKB030085が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030085を同じ出力で読み、終端判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030085
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030085
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Honor Priority REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030085が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Honor Priority と OSKB030085 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Importance 1 {#c28-i0351}
*分類: WLM Service Class*  ・  難易度: 上級

Importance 1は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 区切追跡の保守管理で Importance 1の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Importance 1の出力を取らず区切追跡の保守管理の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切追跡の確認にする。 ✅
    - C. D WLM,SYSTEMS を省略して区切追跡の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切追跡の保守管理において選択記号 B を採用し、識別名は区切追跡です。区切追跡の保守管理において Importance 1 は説明欄の「区切追跡の保守管理に関係する定義値と表示行を照合する区切追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の保守管理の証跡を読む担当者は、Importance 1の属性行と IWM025I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の保守管理は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の保守管理は別カテゴリの確認を流用しており、Importance 1の根拠にならないため区切追跡ではありません。区切追跡の保守管理に出る Importance 1は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は区切追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Importance 1**

    - 検証目的: 記録検査の保守管理について、Importance 1は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030073の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、記録検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にImportance 1を指定し、OSKB030073の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Importance 1
    CASE OSKB030073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Importance 1
    CASE OSKB030073
    SOURCE SMP/E SMF WLM
    ```

    Importance 1とOSKB030073が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030073を同じ出力で読み、記録検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030073
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030073
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Importance 1 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030073が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Importance 1 と OSKB030073 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Importance 2 {#c28-i0352}
*分類: WLM Service Class*  ・  難易度: 上級

Importance 2は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 構文確認の保守管理に関係する Importance 2の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、構文確認の確認にする。 ✅
    - B. Importance 2の名称と担当者名のみを残して構文確認の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で構文確認の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず構文確認の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認の保守管理において選択記号 A を採用し、識別名は構文確認です。構文確認の保守管理において Importance 2 は説明欄の「Importance 2の用途を保守管理の表示で確認する構文確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の保守管理に関連して、SMP/E SMF WLM では Importance 2の表示属性と IWM025I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の保守管理は対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の保守管理は別カテゴリの確認を流用しており、Importance 2の根拠にならないため構文確認ではありません。 D: 構文確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため構文確認ではありません。構文確認の保守管理で使う Importance 2という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は構文確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Importance 2**

    - 検証目的: 比較検査の保守管理について、Importance 2は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030074の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、比較検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にImportance 2を指定し、OSKB030074の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Importance 2
    CASE OSKB030074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Importance 2
    CASE OSKB030074
    SOURCE SMP/E SMF WLM
    ```

    Importance 2とOSKB030074が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030074を同じ出力で読み、比較検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030074
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030074
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Importance 2 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030074が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Importance 2 と OSKB030074 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Importance 3 {#c28-i0353}
*分類: WLM Service Class*  ・  難易度: 上級

Importance 3は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 展開確認の保守管理で Importance 3の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Importance 3の出力を取らず展開確認の保守管理の説明文と承認印のみを残す。
    - B. SMP/E SMF WLM の表示形式に沿って根拠行を採り、展開確認の点検結果を残す。 ✅
    - C. D WLM,SYSTEMS を省略して展開確認の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認の保守管理において選択記号 B を採用し、識別名は展開確認です。展開確認の保守管理において Importance 3 は説明欄の「展開確認の保守管理に関係する定義値と表示行を照合する展開確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の保守管理の証跡を読む担当者は、Importance 3の属性行と IWM025I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の保守管理は対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため展開確認ではありません。 D: 展開確認の保守管理は別カテゴリの確認を流用しており、Importance 3の根拠にならないため展開確認ではありません。展開確認の保守管理に出る Importance 3は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は展開確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Importance 3**

    - 検証目的: 順序検査の保守管理について、Importance 3は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030075の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、順序検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にImportance 3を指定し、OSKB030075の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Importance 3
    CASE OSKB030075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Importance 3
    CASE OSKB030075
    SOURCE SMP/E SMF WLM
    ```

    Importance 3とOSKB030075が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030075を同じ出力で読み、順序検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030075
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030075
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Importance 3 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030075が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Importance 3 と OSKB030075 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Importance 4 {#c28-i0354}
*分類: WLM Service Class*  ・  難易度: 上級

Importance 4は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 呼出確認の保守管理で保守管理の運用確認を行います。Importance 4の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で呼出確認の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず呼出確認の保守管理を正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出確認で再確認できる形にする。 ✅
    - D. Importance 4の属性行を読まず呼出確認の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認の保守管理において選択記号 C を採用し、識別名は呼出確認です。呼出確認の保守管理において Importance 4 は説明欄の「SMP/E SMF WLM で Importance 4の扱いを記録する呼出確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の保守管理を受け取る担当者は、Importance 4の表示結果と IWM025I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の保守管理は別カテゴリの確認を流用しており、Importance 4の根拠にならないため呼出確認ではありません。 B: 呼出確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の保守管理は対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の保守管理が示す Importance 4は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Importance 4**

    - 検証目的: 値域検査の保守管理について、Importance 4は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030076の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、値域検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にImportance 4を指定し、OSKB030076の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Importance 4
    CASE OSKB030076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Importance 4
    CASE OSKB030076
    SOURCE SMP/E SMF WLM
    ```

    Importance 4とOSKB030076が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030076を同じ出力で読み、値域検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030076
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030076
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Importance 4 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030076が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Importance 4 と OSKB030076 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Importance 5 {#c28-i0355}
*分類: WLM Service Class*  ・  難易度: 上級

Importance 5は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 置換確認の保守管理に関する Importance 5の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず置換確認の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の保守管理の証跡として保存して根拠にする。
    - C. Importance 5の変更点を出力本文から切り離して置換確認の保守管理の承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換確認の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認の保守管理において選択記号 D を採用し、識別名は置換確認です。置換確認の保守管理において Importance 5 は説明欄の「Importance 5の状態と出力メッセージを結び付ける置換確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の保守管理に関する記録は、Importance 5の出力行と IWM025I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため置換確認ではありません。 B: 置換確認の保守管理は別カテゴリの確認を流用しており、Importance 5の根拠にならないため置換確認ではありません。 C: 置換確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の保守管理は対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の保守管理で記録する Importance 5は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は置換確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Importance 5**

    - 検証目的: 警告検査の保守管理について、Importance 5は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030077の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、警告検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にImportance 5を指定し、OSKB030077の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Importance 5
    CASE OSKB030077
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Importance 5
    CASE OSKB030077
    SOURCE SMP/E SMF WLM
    ```

    Importance 5とOSKB030077が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030077を同じ出力で読み、警告検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030077
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030077
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Importance 5 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030077が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Importance 5 と OSKB030077 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Period Aged-Out {#c28-i0356}
*分類: WLM Service Class*  ・  難易度: 上級

Period Aged-Outは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 上書確認の保守管理で保守管理の運用確認を行います。Period Aged-Outの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で上書確認の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず上書確認の保守管理を正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、上書確認の証跡として残す。 ✅
    - D. Period Aged-Outの属性行を読まず上書確認の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認の保守管理において選択記号 C を採用し、識別名は上書確認です。上書確認の保守管理において Period Aged-Out は説明欄の「SMP/E SMF WLM で Period Aged-Outの扱いを記録する上書確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の保守管理を受け取る担当者は、Period Aged-Outの表示結果と IWM025I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の保守管理は別カテゴリの確認を流用しており、Period Aged-Outの根拠にならないため上書確認ではありません。 B: 上書確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため上書確認ではありません。 C: 上書確認の保守管理は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の保守管理が示す Period Aged-Outは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Period Aged-Out**

    - 検証目的: 変更検査の保守管理について、Period Aged-Outは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030080の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、変更検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にPeriod Aged-Outを指定し、OSKB030080の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Period Aged-Out
    CASE OSKB030080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Period Aged-Out
    CASE OSKB030080
    SOURCE SMP/E SMF WLM
    ```

    Period Aged-OutとOSKB030080が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030080を同じ出力で読み、変更検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030080
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030080
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Period Aged-Out REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030080が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Period Aged-Out と OSKB030080 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Period の概念 {#c28-i0357}
*分類: WLM Service Class*  ・  難易度: 上級

Period の概念は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。Period の概念は、実行時間で段階的に目標を弱める仕組み、例: 30 秒以内 速い目標。実行時間で段階的に目標を弱める仕組み、例: 30 秒以内 → 速い目標

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 終端確認のの概念に関係する Period の概念の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端確認の根拠を固定する。 ✅
    - B. Period の概念の名称と担当者名のみを残して終端確認のの概念の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で終端確認のの概念を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず終端確認のの概念の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認のの概念において選択記号 A を採用し、識別名は終端確認です。終端確認のの概念において Period の概念 は説明欄の「Period の概念の用途を保守管理の表示で確認する終端確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認のの概念に関連して、SMP/E SMF WLM では Period の概念の表示属性と IWM025I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認のの概念は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認のの概念は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認のの概念は別カテゴリの確認を流用しており、Period の概念の根拠にならないため終端確認ではありません。 D: 終端確認のの概念は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため終端確認ではありません。終端確認のの概念で使う Period の概念という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は終端確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Period の概念**

    - 検証目的: 復旧検査のの概念について、Period の概念は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。Period の概念はに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030078の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、復旧検査のの概念の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にPeriod の概念を指定し、OSKB030078の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Period の概念
    CASE OSKB030078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Period の概念
    CASE OSKB030078
    SOURCE SMP/E SMF WLM
    ```

    Period の概念とOSKB030078が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030078を同じ出力で読み、復旧検査のの概念の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030078
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030078
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Period の概念 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030078が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Period の概念 と OSKB030078 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### STC Subsystem 用 {#c28-i0358}
*分類: WLM Service Class*  ・  難易度: 上級

STC Subsystem 用は、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 出力確認の用に関する STC Subsystem 用の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず出力確認の用の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の用の証跡として保存して根拠にする。
    - C. STC Subsystem 用の変更点を出力本文から切り離して出力確認の用の承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力確認の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認の用において選択記号 D を採用し、識別名は出力確認です。出力確認の用において STC Subsystem 用 は説明欄の「STC Subsystem 用の状態と出力メッセージを結び付ける出力確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の用に関する記録は、STC Subsystem 用の出力行と IWM025I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の用は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため出力確認ではありません。 B: 出力確認の用は別カテゴリの確認を流用しており、STC Subsystem 用の根拠にならないため出力確認ではありません。 C: 出力確認の用は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の用は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の用で記録する STC Subsystem 用は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は出力確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **STC Subsystem 用**

    - 検証目的: 構文判定の用について、STC Subsystem 用は、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030081の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、構文判定の用の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にSTC Subsystem 用を指定し、OSKB030081の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND STC Subsystem 用
    CASE OSKB030081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM STC Subsystem 用
    CASE OSKB030081
    SOURCE SMP/E SMF WLM
    ```

    STC Subsystem 用とOSKB030081が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030081を同じ出力で読み、構文判定の用の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030081
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030081
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I STC Subsystem 用 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030081が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の STC Subsystem 用 と OSKB030081 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### SYSSTC / SYSTEM クラス {#c28-i0359}
*分類: WLM Service Class*  ・  難易度: 上級

SYSSTC / SYSTEM クラスは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? note "検証手順（1件）"
    **SYSSTC ・ SYSTEM クラス**

    - 検証目的: 展開判定の・ クラスについて、SYSSTC / SYSTEM クラスは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030082の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、展開判定の・ クラスの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にSYSSTC ・ SYSTEM クラを指定し、OSKB030082の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND SYSSTC ・ SYSTEM クラ
    CASE OSKB030082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM SYSSTC ・ SYSTEM クラ
    CASE OSKB030082
    SOURCE SMP/E SMF WLM
    ```

    SYSSTC ・ SYSTEM クラとOSKB030082が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030082を同じ出力で読み、展開判定の・ クラスの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030082
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030082
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I SYSSTC ・ SYSTEM クラス REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030082が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の SYSSTC ・ SYSTEM クラ と OSKB030082 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Service Class CPU Critical {#c28-i0360}
*分類: WLM Service Class*  ・  難易度: 上級

Service Class CPU Criticalは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 区切確認の保守管理で Service Class CPU Criticの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Service Class CPU Criticの出力を取らず区切確認の保守管理の説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IWM025I を読み、区切確認の結果として保存する。 ✅
    - C. D WLM,SYSTEMS を省略して区切確認の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認の保守管理において選択記号 B を採用し、識別名は区切確認です。区切確認の保守管理において Service Class CPU Critic は説明欄の「区切確認の保守管理に関係する定義値と表示行を照合する区切確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の保守管理の証跡を読む担当者は、Service Class CPU Criticの属性行と IWM025I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の保守管理は対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため区切確認ではありません。 D: 区切確認の保守管理は別カテゴリの確認を流用しており、Service Class CPU Criticの根拠にならないため区切確認ではありません。区切確認の保守管理に出る Service Class CPU Criticは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は区切確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Service Class CPU Critical**

    - 検証目的: 呼出判定の保守管理について、Service Class CPU Criticalは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030083の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、呼出判定の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にService Class CPU を指定し、OSKB030083の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Service Class CPU 
    CASE OSKB030083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Service Class CPU 
    CASE OSKB030083
    SOURCE SMP/E SMF WLM
    ```

    Service Class CPU とOSKB030083が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030083を同じ出力で読み、呼出判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030083
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030083
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Service Class CPU Critic REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030083が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Service Class CPU  と OSKB030083 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### Service Class Storage Critical {#c28-i0361}
*分類: WLM Service Class*  ・  難易度: 上級

Service Class Storage Criticalは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 範囲確認の保守管理で保守管理の運用確認を行います。Service Class Storage Crの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で範囲確認の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず範囲確認の保守管理を正常終了として記録する。
    - C. D WLM,SYSTEMS で得た表示本文を使い、範囲確認の採否を説明欄に結び付ける。 ✅
    - D. Service Class Storage Crの属性行を読まず範囲確認の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認の保守管理において選択記号 C を採用し、識別名は範囲確認です。範囲確認の保守管理において Service Class Storage Cr は説明欄の「SMP/E SMF WLM で Service Class Storage Crの扱いを記録する範囲確認項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認の保守管理を受け取る担当者は、Service Class Storage Crの表示結果と IWM025I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認の保守管理は別カテゴリの確認を流用しており、Service Class Storage Crの根拠にならないため範囲確認ではありません。 B: 範囲確認の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認の保守管理は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認の保守管理が示す Service Class Storage Crは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Service Class Storage Critical**

    - 検証目的: 置換判定の保守管理について、Service Class Storage Criticalは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030084の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、置換判定の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にService Class Storを指定し、OSKB030084の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Service Class Stor
    CASE OSKB030084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Service Class Stor
    CASE OSKB030084
    SOURCE SMP/E SMF WLM
    ```

    Service Class StorとOSKB030084が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030084を同じ出力で読み、置換判定の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030084
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030084
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Service Class Storage Cr REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030084が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Service Class Stor と OSKB030084 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 目標タイプ Discretionary {#c28-i0362}
*分類: WLM Service Class*  ・  難易度: 上級

目標タイプ Discretionaryは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 条件追跡の目標タイプに関係する目標タイプ Discretionaryの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、条件追跡として引き継ぐ。 ✅
    - B. 目標タイプ Discretionaryの名称と担当者名のみを残して条件追跡の目標タイプの表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で条件追跡の目標タイプを確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず条件追跡の目標タイプの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件追跡の目標タイプにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の目標タイプにおいて目標タイプ Discretionary は説明欄の「目標タイプ Discretionaryの用途を保守管理の表示で確認する条件追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の目標タイプに関連して、SMP/E SMF WLM では目標タイプ Discretionaryの表示属性と IWM025I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の目標タイプは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の目標タイプは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の目標タイプは別カテゴリの確認を流用しており、目標タイプ Discretionaryの根拠にならないため条件追跡ではありません。 D: 条件追跡の目標タイプは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため条件追跡ではありません。条件追跡の目標タイプで使う目標タイプ Discretionaryという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は条件追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **目標タイプ Discretionary**

    - 検証目的: 優先検査の目標タイプについて、目標タイプ Discretionaryは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030072の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先検査の目標タイプの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄に目標タイプ Discretionarを指定し、OSKB030072の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 目標タイプ Discretionar
    CASE OSKB030072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 目標タイプ Discretionar
    CASE OSKB030072
    SOURCE SMP/E SMF WLM
    ```

    目標タイプ DiscretionarとOSKB030072が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030072を同じ出力で読み、優先検査の目標タイプの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030072
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030072
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 目標タイプ Discretionary REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030072が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 目標タイプ Discretionar と OSKB030072 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 目標タイプ Response Time Average {#c28-i0363}
*分類: WLM Service Class*  ・  難易度: 上級

目標タイプ Response Time Averageは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 探索追跡の目標タイプで目標タイプ Response Time Averの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 目標タイプ Response Time Averの出力を取らず探索追跡の目標タイプの説明文と承認印のみを残す。
    - B. 属性行、戻り表示、メッセージ見出しを合わせて探索追跡の根拠にする。 ✅
    - C. D WLM,SYSTEMS を省略して探索追跡の目標タイプの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の目標タイプへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡の目標タイプにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の目標タイプにおいて目標タイプ Response Time Aver は説明欄の「探索追跡の目標タイプに関係する定義値と表示行を照合する探索追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の目標タイプの証跡を読む担当者は、目標タイプ Response Time Averの属性行と IWM025I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の目標タイプは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の目標タイプは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の目標タイプは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の目標タイプは別カテゴリの確認を流用しており、目標タイプ Response Time Averの根拠にならないため探索追跡ではありません。探索追跡の目標タイプに出る目標タイプ Response Time Averは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は探索追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **目標タイプ Response Time Average**

    - 検証目的: 条件検査の目標タイプについて、目標タイプ Response Time Averageは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030069の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、条件検査の目標タイプの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄に目標タイプ Response Timを指定し、OSKB030069の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 目標タイプ Response Tim
    CASE OSKB030069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 目標タイプ Response Tim
    CASE OSKB030069
    SOURCE SMP/E SMF WLM
    ```

    目標タイプ Response TimとOSKB030069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030069を同じ出力で読み、条件検査の目標タイプの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030069
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030069
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 目標タイプ Response Time Aver REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 目標タイプ Response Tim と OSKB030069 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 目標タイプ Response Time Percentile {#c28-i0364}
*分類: WLM Service Class*  ・  難易度: 上級

目標タイプ Response Time Percentileは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 上書追跡の目標タイプで保守管理の運用確認を行います。目標タイプ Response Time Percの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で上書追跡の目標タイプを確認した扱いにする。
    - B. IWM025I の有無を確認せず上書追跡の目標タイプを正常終了として記録する。
    - C. 同じ画面で対象行と IWM025I を読み、上書追跡の結果として保存する。 ✅
    - D. 目標タイプ Response Time Percの属性行を読まず上書追跡の目標タイプの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡の目標タイプにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡の目標タイプにおいて目標タイプ Response Time Perc は説明欄の「SMP/E SMF WLM で目標タイプ Response Time Percの扱いを記録する上書追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の目標タイプを受け取る担当者は、目標タイプ Response Time Percの表示結果と IWM025I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の目標タイプは別カテゴリの確認を流用しており、目標タイプ Response Time Percの根拠にならないため上書追跡ではありません。 B: 上書追跡の目標タイプは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の目標タイプは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の目標タイプは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の目標タイプが示す目標タイプ Response Time Percは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **目標タイプ Response Time Percentile**

    - 検証目的: 区切検査の目標タイプについて、目標タイプ Response Time Percentileは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030070の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切検査の目標タイプの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄に目標タイプ Response Timを指定し、OSKB030070の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 目標タイプ Response Tim
    CASE OSKB030070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 目標タイプ Response Tim
    CASE OSKB030070
    SOURCE SMP/E SMF WLM
    ```

    目標タイプ Response TimとOSKB030070が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030070を同じ出力で読み、区切検査の目標タイプの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030070
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030070
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 目標タイプ Response Time Perc REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030070が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 目標タイプ Response Tim と OSKB030070 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)



### 目標タイプ Velocity {#c28-i0365}
*分類: WLM Service Class*  ・  難易度: 上級

目標タイプ Velocityは、SMP/E / SMF / WLMのWLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 出力追跡の目標タイプに関する目標タイプ Velocityの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず出力追跡の目標タイプの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の目標タイプの証跡として保存して根拠にする。
    - C. 目標タイプ Velocityの変更点を出力本文から切り離して出力追跡の目標タイプの承認欄のみ残す。
    - D. D WLM,SYSTEMS で得た表示本文を使い、出力追跡の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡の目標タイプにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の目標タイプにおいて目標タイプ Velocity は説明欄の「目標タイプ Velocityの状態と出力メッセージを結び付ける出力追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の目標タイプに関する記録は、目標タイプ Velocityの出力行と IWM025I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の目標タイプは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の目標タイプは別カテゴリの確認を流用しており、目標タイプ Velocityの根拠にならないため出力追跡ではありません。 C: 出力追跡の目標タイプは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の目標タイプは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の目標タイプで記録する目標タイプ Velocityは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は出力追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **目標タイプ Velocity**

    - 検証目的: 範囲検査の目標タイプについて、目標タイプ Velocityは、SMP/E / SMF / WLM の WLM Service Classで機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030071の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲検査の目標タイプの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄に目標タイプ Velocityを指定し、OSKB030071の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND 目標タイプ Velocity
    CASE OSKB030071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM 目標タイプ Velocity
    CASE OSKB030071
    SOURCE SMP/E SMF WLM
    ```

    目標タイプ VelocityとOSKB030071が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030071を同じ出力で読み、範囲検査の目標タイプの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030071
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030071
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I 目標タイプ Velocity REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030071が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の 目標タイプ Velocity と OSKB030071 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100)




## SMP/E / SMF / WLM > WLM Service Definition

### Application Environment {#c28-i0366}
*分類: WLM Service Definition*  ・  難易度: 上級

Application Environmentは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 展開追跡の保守管理で Application Environmentの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Application Environmentの出力を取らず展開追跡の保守管理の説明文と承認印のみを残す。
    - B. 参照資料名、表示行、メッセージをそろえて展開追跡の根拠を固定する。 ✅
    - C. D WLM,SYSTEMS を省略して展開追跡の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開追跡の保守管理において選択記号 B を採用し、識別名は展開追跡です。展開追跡の保守管理において Application Environment は説明欄の「展開追跡の保守管理に関係する定義値と表示行を照合する展開追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の保守管理の証跡を読む担当者は、Application Environmentの属性行と IWM025I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の保守管理は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の保守管理は別カテゴリの確認を流用しており、Application Environmentの根拠にならないため展開追跡ではありません。展開追跡の保守管理に出る Application Environmentは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は展開追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Application Environment**

    - 検証目的: 終端検査の保守管理について、Application Environmentは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030065の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、終端検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にApplication Enviroを指定し、OSKB030065の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Application Enviro
    CASE OSKB030065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Application Enviro
    CASE OSKB030065
    SOURCE SMP/E SMF WLM
    ```

    Application EnviroとOSKB030065が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030065を同じ出力で読み、終端検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030065
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030065
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Application Environment REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030065が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Application Enviro と OSKB030065 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Classification Group {#c28-i0367}
*分類: WLM Service Definition*  ・  難易度: 上級

Classification Groupは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 終端追跡の保守管理に関係する Classification Groupの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 出典欄の説明と運用出力を照合し、終端追跡の確認記録にまとめる。 ✅
    - B. Classification Groupの名称と担当者名のみを残して終端追跡の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で終端追跡の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず終端追跡の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡の保守管理において選択記号 A を採用し、識別名は終端追跡です。終端追跡の保守管理において Classification Group は説明欄の「Classification Groupの用途を保守管理の表示で確認する終端追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の保守管理に関連して、SMP/E SMF WLM では Classification Groupの表示属性と IWM025I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の保守管理は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の保守管理は別カテゴリの確認を流用しており、Classification Groupの根拠にならないため終端追跡ではありません。 D: 終端追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため終端追跡ではありません。終端追跡の保守管理で使う Classification Groupという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は終端追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Classification Group**

    - 検証目的: 出力検査の保守管理について、Classification Groupは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030068の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、出力検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にClassification Groを指定し、OSKB030068の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Classification Gro
    CASE OSKB030068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Classification Gro
    CASE OSKB030068
    SOURCE SMP/E SMF WLM
    ```

    Classification GroとOSKB030068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030068を同じ出力で読み、出力検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030068
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030068
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Classification Group REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Classification Gro と OSKB030068 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Classification Rules {#c28-i0368}
*分類: WLM Service Definition*  ・  難易度: 上級

Classification Rulesは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 置換追跡の保守管理に関する Classification Rulesの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず置換追跡の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の保守管理の証跡として保存して根拠にする。
    - C. Classification Rulesの変更点を出力本文から切り離して置換追跡の保守管理の承認欄のみ残す。
    - D. D WLM,SYSTEMS の結果から対象行を抜き出し、置換追跡の証跡として残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡の保守管理において選択記号 D を採用し、識別名は置換追跡です。置換追跡の保守管理において Classification Rules は説明欄の「Classification Rulesの状態と出力メッセージを結び付ける置換追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の保守管理に関する記録は、Classification Rulesの出力行と IWM025I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の保守管理は別カテゴリの確認を流用しており、Classification Rulesの根拠にならないため置換追跡ではありません。 C: 置換追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の保守管理は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の保守管理で記録する Classification Rulesは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は置換追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Classification Rules**

    - 検証目的: 上書検査の保守管理について、Classification Rulesは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照する項に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030067の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、上書検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にClassification Rulを指定し、OSKB030067の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Classification Rul
    CASE OSKB030067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Classification Rul
    CASE OSKB030067
    SOURCE SMP/E SMF WLM
    ```

    Classification RulとOSKB030067が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030067を同じ出力で読み、上書検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030067
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030067
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Classification Rules REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030067が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Classification Rul と OSKB030067 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Report Class {#c28-i0369}
*分類: WLM Service Definition*  ・  難易度: 上級

Report Classは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（4問）"
    **問題.** 監査照合の保守管理で保守管理の運用確認を行います。Report Classの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で監査照合の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず監査照合の保守管理を正常終了として記録する。
    - C. SMP/E SMF WLM の表示形式に沿って根拠行を採り、監査照合の点検結果を残す。 ✅
    - D. Report Classの属性行を読まず監査照合の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査照合の保守管理において選択記号 C を採用し、識別名は監査照合です。監査照合の保守管理において Report Class は説明欄の「SMP/E SMF WLM で Report Classの扱いを記録する監査照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の保守管理を受け取る担当者は、Report Classの表示結果と IWM025I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の保守管理は別カテゴリの確認を流用しており、Report Classの根拠にならないため監査照合ではありません。 B: 監査照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため監査照合ではありません。 C: 監査照合の保守管理は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の保守管理が示す Report Classは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）

    ---

    **問題.** 運用面の報告クラスを証跡保存で確認します。実行した入力と表示された報告を同じ作業記録に残します。資料のコマンド形式、報告名、メッセージ名を使ってreport class assignmentを確認する場合、証跡として中心に置く項目はどれですか。

    - A. Report class ✅
    - B. REJECT SYSMOD
    - C. LSNAME TYPE
    - D. IFASMFDP data set dump

    正解: **A** ／ 難易度: 中級

    **解説:** 制御面観点で読む報告クラス証跡は正答位置Aで、記録する焦点は報告クラス読取です。復旧面観点の報告クラス状態は、サービスクラスとは別に報告集計単位を付与することを満たす入力、報告、状態表示を同じ証跡で確認する報告クラス状態です。方針面観点の報告クラス定義は、report class assignmentを入力記録と合わせて処理対象を見分ける報告クラス定義です。運用面観点の報告クラス根拠は、ワークロード管理方針の入力要求と戻った報告を結び、運用状態を説明する報告クラス根拠です。A: 選択面観点の報告クラス読取は、入力名と報告内のreport class assignmentを結ぶ報告クラス復旧です。B: 表示面観点の参照先は未採用保守要素除去状態で、作業記録で追跡する対象は報告クラス引継ぎです。C: 抽出面観点の比較先は種別別ログストリーム定義で、要求対象は報告クラス応答です。D: 保守面観点の照合先はMANデータセットダンプ根拠で、中心は報告クラス保守です。確認面観点の用語定義として、報告クラスとはz/OSの保守、記録、または作業負荷管理で、入力と出力を対応させて状態を読む報告クラス棚卸です。

    **出典:** zOS31_gim1000.pdf z / OS SMP / E Commands / zOS31_gim2000.pdf z / E Reference / zOS31_gim3000.pdf z / E User's Guide / zOS31_ieag200.pdf z / OS MVS System Management Facilities / zOS31_ieag100.pdf z / OS MVS System Commands / zOS31_ieam900.pdf z / OS MVS System Messages Vol 9 / WLM service definition report class

    ---

    **問題.** 復旧面の報告クラスを運用引継ぎで確認します。次の担当者が同じ状態を確認できる粒度で説明します。資料のコマンド形式、報告名、メッセージ名を使ってreport class assignmentを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. DISPLAY SMF,S
    - B. IFASMFDL SID
    - C. Report class ✅
    - D. VARY WLM,APPLENV,REFRESH

    正解: **C** ／ 難易度: 中級

    **解説:** 保守面観点の出力確認として報告クラス状態を読み、答えはCで、照合焦点は報告クラス定義です。構成面観点の報告クラス根拠は、サービスクラスとは別に報告集計単位を付与することを満たす入力、報告、状態表示を同じ証跡で確認する報告クラス根拠です。報告面観点で残す報告クラス応答は、report class assignmentをコマンド形式と照合する報告クラス応答です。復旧面観点の報告クラス保守は、ワークロード管理方針の入力要求と戻った報告を結び、運用状態を説明する報告クラス保守です。A: 照合面観点の比較先はシステム管理機能状態表示定義で、要求対象は報告クラス監査です。B: 抽出面観点の照合先はシステムID選択根拠で、中心は報告クラス引継ぎです。C: 管理面観点の報告クラス応答は、入力名と報告内のreport class assignmentを結ぶ報告クラス報告です。D: 方針面観点の参照先はアプリ環境再読込保守で、作業記録で追跡する対象は報告クラス復旧です。運用面観点の用語定義として、報告クラスとはz/OSの保守、記録、または作業負荷管理で、入力と出力を対応させて状態を読む報告クラス照合です。

    **出典:** zOS31_gim1000.pdf z / OS SMP / E Commands / zOS31_gim2000.pdf z / E Reference / zOS31_gim3000.pdf z / E User's Guide / zOS31_ieag200.pdf z / OS MVS System Management Facilities / zOS31_ieag100.pdf z / OS MVS System Commands / zOS31_ieam900.pdf z / OS MVS System Messages Vol 9 / WLM service definition report class

    ---

    **問題.** 構成面の報告クラスを定義確認で確認します。処理対象の定義を読み取り、表示項目と運用記録を合わせます。資料のコマンド形式、報告名、メッセージ名を使ってreport class assignmentを確認する場合、どの項目を選ぶべきですか。

    - A. Report class ✅
    - B. DISPLAY WLM
    - C. VARY WLM,APPLENV,RESUME
    - D. SET BDY(TARGET)

    正解: **A** ／ 難易度: 中級

    **解説:** 抽出面観点で読む報告クラス根拠は正答位置Aで、記録する焦点は報告クラス応答です。報告面観点の報告クラス保守は、サービスクラスとは別に報告集計単位を付与することを満たす入力、報告、状態表示を同じ証跡で確認する報告クラス保守です。記録面観点の報告クラス監査は、report class assignmentを入力記録と合わせて処理対象を見分ける報告クラス監査です。構成面観点の報告クラス引継ぎは、ワークロード管理方針の入力要求と戻った報告を結び、運用状態を説明する報告クラス引継ぎです。A: 反映面観点の報告クラス応答は、入力名と報告内のreport class assignmentを結ぶ報告クラス反映です。B: 保守面観点の参照先は有効サービス方針表示保守で、作業記録で追跡する対象は報告クラス報告です。C: 選択面観点の比較先はアプリ環境再開監査で、要求対象は報告クラス棚卸です。D: 分類面観点の照合先はターゲットゾーン選択引継ぎで、中心は報告クラス復旧です。復旧面観点の用語定義として、報告クラスとはz/OSの保守、記録、または作業負荷管理で、入力と出力を対応させて状態を読む報告クラス選択です。

    **出典:** zOS31_gim1000.pdf z / OS SMP / E Commands / zOS31_gim2000.pdf z / E Reference / zOS31_gim3000.pdf z / E User's Guide / zOS31_ieag200.pdf z / OS MVS System Management Facilities / zOS31_ieag100.pdf z / OS MVS System Commands / zOS31_ieam900.pdf z / OS MVS System Messages Vol 9 / WLM service definition report class


??? note "検証手順（1件）"
    **Report Class**

    - 検証目的: 展開検査の保守管理について、Report Classは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030062の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、展開検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にReport Classを指定し、OSKB030062の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Report Class
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Report Class
    CASE OSKB030062
    SOURCE SMP/E SMF WLM
    ```

    Report ClassとOSKB030062が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030062を同じ出力で読み、展開検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030062
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030062
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Report Class REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030062が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Report Class と OSKB030062 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Resource Group {#c28-i0370}
*分類: WLM Service Definition*  ・  難易度: 上級

Resource Groupは、SMP/E / SMF / WLMのWLM Service Definitionでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 構文追跡の保守管理に関係する Resource Groupの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 机上確認でも実出力の見出しに合わせ、構文追跡の確認値として扱う。 ✅
    - B. Resource Groupの名称と担当者名のみを残して構文追跡の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で構文追跡の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず構文追跡の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文追跡の保守管理において選択記号 A を採用し、識別名は構文追跡です。構文追跡の保守管理において Resource Group は説明欄の「Resource Groupの用途を保守管理の表示で確認する構文追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の保守管理に関連して、SMP/E SMF WLM では Resource Groupの表示属性と IWM025I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の保守管理は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の保守管理は別カテゴリの確認を流用しており、Resource Groupの根拠にならないため構文追跡ではありません。 D: 構文追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため構文追跡ではありません。構文追跡の保守管理で使う Resource Groupという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は構文追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Resource Group**

    - 検証目的: 置換検査の保守管理について、Resource Groupは、SMP/E / SMF / WLM の WLM Service Definitionでリソース定義、モデル、またはポリシーを読むための項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030064の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、置換検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にResource Groupを指定し、OSKB030064の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Resource Group
    CASE OSKB030064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Resource Group
    CASE OSKB030064
    SOURCE SMP/E SMF WLM
    ```

    Resource GroupとOSKB030064が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030064を同じ出力で読み、置換検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030064
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030064
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Resource Group REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030064が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Resource Group と OSKB030064 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Scheduling Environment {#c28-i0371}
*分類: WLM Service Definition*  ・  難易度: 上級

Scheduling Environmentは、SMP/E / SMF / WLMのWLM Service Definitionで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 呼出追跡の保守管理で保守管理の運用確認を行います。Scheduling Environmentの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で呼出追跡の保守管理を確認した扱いにする。
    - B. IWM025I の有無を確認せず呼出追跡の保守管理を正常終了として記録する。
    - C. IWM025I を含む表示を保存し、説明欄との差分を呼出追跡で確認する。 ✅
    - D. Scheduling Environmentの属性行を読まず呼出追跡の保守管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡の保守管理において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の保守管理において Scheduling Environment は説明欄の「SMP/E SMF WLM で Scheduling Environmentの扱いを記録する呼出追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の保守管理を受け取る担当者は、Scheduling Environmentの表示結果と IWM025I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の保守管理は別カテゴリの確認を流用しており、Scheduling Environmentの根拠にならないため呼出追跡ではありません。 B: 呼出追跡の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の保守管理は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の保守管理が示す Scheduling Environmentは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Scheduling Environment**

    - 検証目的: 探索検査の保守管理について、Scheduling Environmentは、SMP/E / SMF / WLM の WLM Service Definitionで自動化処理や復旧動作を確認する項目です。起に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030066の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、探索検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にScheduling Environを指定し、OSKB030066の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Scheduling Environ
    CASE OSKB030066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Scheduling Environ
    CASE OSKB030066
    SOURCE SMP/E SMF WLM
    ```

    Scheduling EnvironとOSKB030066が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030066を同じ出力で読み、探索検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030066
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030066
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Scheduling Environment REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030066が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Scheduling Environ と OSKB030066 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Service Class {#c28-i0372}
*分類: WLM Service Definition*  ・  難易度: 上級

Service Classは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 復旧照合の保守管理で Service Classの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Service Classの出力を取らず復旧照合の保守管理の説明文と承認印のみを残す。
    - B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧照合の確認にする。 ✅
    - C. D WLM,SYSTEMS を省略して復旧照合の保守管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の保守管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧照合の保守管理において選択記号 B を採用し、識別名は復旧照合です。復旧照合の保守管理において Service Class は説明欄の「復旧照合の保守管理に関係する定義値と表示行を照合する復旧照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の保守管理の証跡を読む担当者は、Service Classの属性行と IWM025I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の保守管理は対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の保守管理は別カテゴリの確認を流用しており、Service Classの根拠にならないため復旧照合ではありません。復旧照合の保守管理に出る Service Classは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Service Class**

    - 検証目的: 構文検査の保守管理について、Service Classは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030061の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、構文検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にService Classを指定し、OSKB030061の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Service Class
    CASE OSKB030061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Service Class
    CASE OSKB030061
    SOURCE SMP/E SMF WLM
    ```

    Service ClassとOSKB030061が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030061を同じ出力で読み、構文検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030061
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030061
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Service Class REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030061が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Service Class と OSKB030061 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Service Definition とは {#c28-i0373}
*分類: WLM Service Definition*  ・  難易度: 上級

Service Definition とはは、WLM の全構成情報、ISPF アプリケーションで作成し XML で保存

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? note "検証手順（1件）"
    **Service Definition とは**

    - 検証目的: 復旧追跡のとはについて、Service Definition とはは、WLM の全構成情報、ISPF アプリケーションで作成し XML で保存に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030058の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、復旧追跡のとはの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にService Definitionを指定し、OSKB030058の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Service Definition
    CASE OSKB030058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Service Definition
    CASE OSKB030058
    SOURCE SMP/E SMF WLM
    ```

    Service DefinitionとOSKB030058が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030058を同じ出力で読み、復旧追跡のとはの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030058
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030058
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Service Definition とは REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030058が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Service Definition と OSKB030058 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Service Policy {#c28-i0374}
*分類: WLM Service Definition*  ・  難易度: 上級

Service Policyは、SMP/E / SMF / WLMのWLM Service Definitionでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 値域照合の保守管理に関する Service Policyの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域照合の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の保守管理の証跡として保存して根拠にする。
    - C. Service Policyの変更点を出力本文から切り離して値域照合の保守管理の承認欄のみ残す。
    - D. D WLM,SYSTEMS で得た表示本文を使い、値域照合の採否を説明欄に結び付ける。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合の保守管理において選択記号 D を採用し、識別名は値域照合です。値域照合の保守管理において Service Policy は説明欄の「Service Policyの状態と出力メッセージを結び付ける値域照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の保守管理に関する記録は、Service Policyの出力行と IWM025I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域照合ではありません。 B: 値域照合の保守管理は別カテゴリの確認を流用しており、Service Policyの根拠にならないため値域照合ではありません。 C: 値域照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の保守管理は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の保守管理で記録する Service Policyは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Service Policy**

    - 検証目的: 監査追跡の保守管理について、Service Policyは、SMP/E / SMF / WLM の WLM Service Definitionでリソース定義、モデル、またはポリシーを読むための項目です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030059の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、監査追跡の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にService Policyを指定し、OSKB030059の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Service Policy
    CASE OSKB030059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Service Policy
    CASE OSKB030059
    SOURCE SMP/E SMF WLM
    ```

    Service PolicyとOSKB030059が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030059を同じ出力で読み、監査追跡の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030059
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030059
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Service Policy REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030059が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Service Policy と OSKB030059 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### WLM Couple Data Set {#c28-i0375}
*分類: WLM Service Definition*  ・  難易度: 上級

WLM Couple Data Setは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 警告照合の保守管理に関係する WLM Couple Data Setの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 資料上の説明と画面上の表示行を突き合わせ、警告照合として引き継ぐ。 ✅
    - B. WLM Couple Data Setの名称と担当者名のみを残して警告照合の保守管理の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告照合の保守管理を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告照合の保守管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告照合の保守管理において選択記号 A を採用し、識別名は警告照合です。警告照合の保守管理において WLM Couple Data Set は説明欄の「WLM Couple Data Setの用途を保守管理の表示で確認する警告照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の保守管理に関連して、SMP/E SMF WLM では WLM Couple Data Setの表示属性と IWM025I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の保守管理は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の保守管理は別カテゴリの確認を流用しており、WLM Couple Data Setの根拠にならないため警告照合ではありません。 D: 警告照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告照合ではありません。警告照合の保守管理で使う WLM Couple Data Setという用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **WLM Couple Data Set**

    - 検証目的: 変更追跡の保守管理について、WLM Couple Data Setは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030060の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、変更追跡の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にWLM Couple Data Seを指定し、OSKB030060の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND WLM Couple Data Se
    CASE OSKB030060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM WLM Couple Data Se
    CASE OSKB030060
    SOURCE SMP/E SMF WLM
    ```

    WLM Couple Data SeとOSKB030060が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030060を同じ出力で読み、変更追跡の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030060
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030060
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I WLM Couple Data Set REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030060が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の WLM Couple Data Se と OSKB030060 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)



### Workload {#c28-i0376}
*分類: WLM Service Definition*  ・  難易度: 上級

Workloadは、SMP/E / SMF / WLMのWLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS Planning Workload Management (zOS31_ieaw100); OS MVS Programming Workload Management Services (zOS31_ieaw200) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)

??? question "確認問題（1問）"
    **問題.** 変更照合の保守管理に関する Workloadの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず変更照合の保守管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の保守管理の証跡として保存して根拠にする。
    - C. Workloadの変更点を出力本文から切り離して変更照合の保守管理の承認欄のみ残す。
    - D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更照合で再確認できる形にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更照合の保守管理において選択記号 D を採用し、識別名は変更照合です。変更照合の保守管理において Workload は説明欄の「Workloadの状態と出力メッセージを結び付ける変更照合項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の保守管理に関する記録は、Workloadの出力行と IWM025I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の保守管理は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため変更照合ではありません。 B: 変更照合の保守管理は別カテゴリの確認を流用しており、Workloadの根拠にならないため変更照合ではありません。 C: 変更照合の保守管理は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の保守管理は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の保守管理で記録する Workloadは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は変更照合です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Workload**

    - 検証目的: 呼出検査の保守管理について、Workloadは、SMP/E / SMF / WLM の WLM Service Definitionで機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030063の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、呼出検査の保守管理の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にWorkloadを指定し、OSKB030063の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Workload
    CASE OSKB030063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Workload
    CASE OSKB030063
    SOURCE SMP/E SMF WLM
    ```

    WorkloadとOSKB030063が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030063を同じ出力で読み、呼出検査の保守管理の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030063
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030063
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Workload REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030063が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Workload と OSKB030063 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning Workload Management (zOS31_ieaw100) / OS MVS Programming Workload Management Services (zOS31_ieaw200)




## SMP/E / SMF / WLM > WLM 運用コマンド

### D WLM {#c28-i0377}
*分類: WLM 運用コマンド*  ・  難易度: 上級

D WLMは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 呼出検査の運用コマンドで保守管理の運用確認を行います。D WLM の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で呼出検査の運用コマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず呼出検査の運用コマンドを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、呼出検査で再確認できる形にする。 ✅
    - D. D WLM の属性行を読まず呼出検査の運用コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出検査の運用コマンドにおいて選択記号 C を採用し、識別名は呼出検査です。呼出検査の運用コマンドにおいて D WLM は説明欄の「SMP/E SMF WLM で D WLM の扱いを記録する呼出検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は呼出検査です。呼出検査の運用コマンドを受け取る担当者は、D WLM の表示結果と IWM025I を同じ確認単位として扱い、背景名は呼出検査です。不適切な選択肢を整理します。 A: 呼出検査の運用コマンドは別カテゴリの確認を流用しており、D WLM の根拠にならないため呼出検査ではありません。 B: 呼出検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため呼出検査ではありません。 C: 呼出検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので呼出検査です。 D: 呼出検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出検査ではありません。呼出検査の運用コマンドが示す D WLM は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **D WLM**

    - 検証目的: 値域記録の運用コマンドについて、D WLM は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030136の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、値域記録の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にD WLMを指定し、OSKB030136の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND D WLM
    CASE OSKB030136
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM D WLM
    CASE OSKB030136
    SOURCE SMP/E SMF WLM
    ```

    D WLMとOSKB030136が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030136を同じ出力で読み、値域記録の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030136
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030136
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I D WLM REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030136が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の D WLM と OSKB030136 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030136 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### D WLM,APPLENV=* {#c28-i0378}
*分類: WLM 運用コマンド*  ・  難易度: 上級

D WLM,APPLENV=*は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 終端検査の*に関係する D WLM,APPLENV=*の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて終端検査の根拠を固定する。 ✅
    - B. D WLM,APPLENV=*の名称と担当者名のみを残して終端検査の*の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で終端検査の*を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず終端検査の*の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端検査の*において選択記号 A を採用し、識別名は終端検査です。終端検査の*において D WLM,APPLENV=* は説明欄の「D WLM,APPLENV=*の用途を保守管理の表示で確認する終端検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は終端検査です。終端検査の*に関連して、SMP/E SMF WLM では D WLM,APPLENV=*の表示属性と IWM025I を同じ証跡に残し、背景名は終端検査です。他の選択肢を確認します。 A: 終端検査の*は対象出力と項目説明を結び、根拠を残すので終端検査です。 B: 終端検査の*は名称や説明のみに寄り、状態を示す出力本文が不足するため終端検査ではありません。 C: 終端検査の*は別カテゴリの確認を流用しており、D WLM,APPLENV=*の根拠にならないため終端検査ではありません。 D: 終端検査の*は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため終端検査ではありません。終端検査の*で使う D WLM,APPLENV=*という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は終端検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **D WLM,APPLENV=***

    - 検証目的: 復旧記録の*について、D WLM,APPLENV=*は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030138の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、復旧記録の*の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にD WLM,APPLENV=*を指定し、OSKB030138の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND D WLM,APPLENV=*
    CASE OSKB030138
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM D WLM,APPLENV=*
    CASE OSKB030138
    SOURCE SMP/E SMF WLM
    ```

    D WLM,APPLENV=*とOSKB030138が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030138を同じ出力で読み、復旧記録の*の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030138
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030138
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I D WLM,APPLENV=* REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030138が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の D WLM,APPLENV=* と OSKB030138 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030138 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### D WLM,RESOURCE=* {#c28-i0379}
*分類: WLM 運用コマンド*  ・  難易度: 上級

D WLM,RESOURCE=*は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 上書検査の*で保守管理の運用確認を行います。D WLM,RESOURCE=*の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で上書検査の*を確認した扱いにする。
    - B. IWM025I の有無を確認せず上書検査の*を正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、上書検査の証跡として残す。 ✅
    - D. D WLM,RESOURCE=*の属性行を読まず上書検査の*の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書検査の*において選択記号 C を採用し、識別名は上書検査です。上書検査の*において D WLM,RESOURCE=* は説明欄の「SMP/E SMF WLM で D WLM,RESOURCE=*の扱いを記録する上書検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は上書検査です。上書検査の*を受け取る担当者は、D WLM,RESOURCE=*の表示結果と IWM025I を同じ確認単位として扱い、背景名は上書検査です。不適切な選択肢を整理します。 A: 上書検査の*は別カテゴリの確認を流用しており、D WLM,RESOURCE=*の根拠にならないため上書検査ではありません。 B: 上書検査の*は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため上書検査ではありません。 C: 上書検査の*は対象出力と項目説明を結び、根拠を残すので上書検査です。 D: 上書検査の*は名称や説明のみに寄り、状態を示す出力本文が不足するため上書検査ではありません。上書検査の*が示す D WLM,RESOURCE=*は出典欄の資料で使い方を追跡できる項目であり、用語名は上書検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **D WLM,RESOURCE=***

    - 検証目的: 変更記録の*について、D WLM,RESOURCE=*は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030140の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、変更記録の*の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にD WLM,RESOURCE=*を指定し、OSKB030140の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND D WLM,RESOURCE=*
    CASE OSKB030140
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM D WLM,RESOURCE=*
    CASE OSKB030140
    SOURCE SMP/E SMF WLM
    ```

    D WLM,RESOURCE=*とOSKB030140が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030140を同じ出力で読み、変更記録の*の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030140
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030140
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I D WLM,RESOURCE=* REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030140が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の D WLM,RESOURCE=* と OSKB030140 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030140 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### D WLM,SCHENV=* {#c28-i0380}
*分類: WLM 運用コマンド*  ・  難易度: 上級

D WLM,SCHENV=*は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 探索検査の*で D WLM,SCHENV=*の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. D WLM,SCHENV=*の出力を取らず探索検査の*の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を探索検査で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して探索検査の*の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の*へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索検査の*において選択記号 B を採用し、識別名は探索検査です。探索検査の*において D WLM,SCHENV=* は説明欄の「探索検査の*に関係する定義値と表示行を照合する探索検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は探索検査です。探索検査の*の証跡を読む担当者は、D WLM,SCHENV=*の属性行と IWM025I を合わせて追跡し、背景名は探索検査です。誤答側の問題点を分けます。 A: 探索検査の*は名称や説明のみに寄り、状態を示す出力本文が不足するため探索検査ではありません。 B: 探索検査の*は対象出力と項目説明を結び、根拠を残すので探索検査です。 C: 探索検査の*は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため探索検査ではありません。 D: 探索検査の*は別カテゴリの確認を流用しており、D WLM,SCHENV=*の根拠にならないため探索検査ではありません。探索検査の*に出る D WLM,SCHENV=*は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は探索検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **D WLM,SCHENV=***

    - 検証目的: 監査記録の*について、D WLM,SCHENV=*は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030139の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、監査記録の*の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にD WLM,SCHENV=*を指定し、OSKB030139の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND D WLM,SCHENV=*
    CASE OSKB030139
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM D WLM,SCHENV=*
    CASE OSKB030139
    SOURCE SMP/E SMF WLM
    ```

    D WLM,SCHENV=*とOSKB030139が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030139を同じ出力で読み、監査記録の*の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030139
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030139
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I D WLM,SCHENV=* REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030139が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の D WLM,SCHENV=* と OSKB030139 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030139 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### D WLM,SYSTEMS {#c28-i0381}
*分類: WLM 運用コマンド*  ・  難易度: 上級

D WLM,SYSTEMSは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 置換検査の運用コマンドに関する D WLM,SYSTEMS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず置換検査の運用コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の運用コマンドの証跡として保存して根拠にする。
    - C. D WLM,SYSTEMS の変更点を出力本文から切り離して置換検査の運用コマンドの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、置換検査の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換検査の運用コマンドにおいて選択記号 D を採用し、識別名は置換検査です。置換検査の運用コマンドにおいて D WLM,SYSTEMS は説明欄の「D WLM,SYSTEMS の状態と出力メッセージを結び付ける置換検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は置換検査です。置換検査の運用コマンドに関する記録は、D WLM,SYSTEMS の出力行と IWM025I を一緒に保存し、背景名は置換検査です。選択肢ごとの違いを示します。 A: 置換検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため置換検査ではありません。 B: 置換検査の運用コマンドは別カテゴリの確認を流用しており、D WLM,SYSTEMS の根拠にならないため置換検査ではありません。 C: 置換検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換検査ではありません。 D: 置換検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので置換検査です。置換検査の運用コマンドで記録する D WLM,SYSTEMS は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は置換検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **D WLM,SYSTEMS**

    - 検証目的: 警告記録の運用コマンドについて、D WLM,SYSTEMS は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030137の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、警告記録の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にD WLM,SYSTEMSを指定し、OSKB030137の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND D WLM,SYSTEMS
    CASE OSKB030137
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM D WLM,SYSTEMS
    CASE OSKB030137
    SOURCE SMP/E SMF WLM
    ```

    D WLM,SYSTEMSとOSKB030137が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030137を同じ出力で読み、警告記録の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030137
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030137
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I D WLM,SYSTEMS REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030137が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の D WLM,SYSTEMS と OSKB030137 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030137 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### Discretionary 利用シーン {#c28-i0382}
*分類: WLM 運用コマンド*  ・  難易度: 上級

Discretionary 利用シーンは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 変更検査の利用シーンに関する Discretionary 利用シーンの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず変更検査の利用シーンの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の利用シーンの証跡として保存して根拠にする。
    - C. Discretionary 利用シーンの変更点を出力本文から切り離して変更検査の利用シーンの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、変更検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検査の利用シーンにおいて選択記号 D を採用し、識別名は変更検査です。変更検査の利用シーンにおいて Discretionary 利用シーン は説明欄の「Discretionary 利用シーンの状態と出力メッセージを結び付ける変更検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査の利用シーンに関する記録は、Discretionary 利用シーンの出力行と IWM025I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査の利用シーンは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため変更検査ではありません。 B: 変更検査の利用シーンは別カテゴリの確認を流用しており、Discretionary 利用シーンの根拠にならないため変更検査ではありません。 C: 変更検査の利用シーンは名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査の利用シーンは対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査の利用シーンで記録する Discretionary 利用シーンは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は変更検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Discretionary 利用シーン**

    - 検証目的: 記録分離の利用シーンについて、Discretionary 利用シーンは、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030153の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、記録分離の利用シーンの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にDiscretionary 利用シーを指定し、OSKB030153の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Discretionary 利用シー
    CASE OSKB030153
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Discretionary 利用シー
    CASE OSKB030153
    SOURCE SMP/E SMF WLM
    ```

    Discretionary 利用シーとOSKB030153が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030153を同じ出力で読み、記録分離の利用シーンの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030153
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030153
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Discretionary 利用シーン REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030153が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Discretionary 利用シー と OSKB030153 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030153 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### ENF 41 Listener {#c28-i0383}
*分類: WLM 運用コマンド*  ・  難易度: 上級

ENF 41 Listenerは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 順序検査の運用コマンドで保守管理の運用確認を行います。ENF 41 Listenerの根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で順序検査の運用コマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず順序検査の運用コマンドを正常終了として記録する。
    - C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序検査で再確認できる形にする。 ✅
    - D. ENF 41 Listenerの属性行を読まず順序検査の運用コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検査の運用コマンドにおいて選択記号 C を採用し、識別名は順序検査です。順序検査の運用コマンドにおいて ENF 41 Listener は説明欄の「SMP/E SMF WLM で ENF 41 Listenerの扱いを記録する順序検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は順序検査です。順序検査の運用コマンドを受け取る担当者は、ENF 41 Listenerの表示結果と IWM025I を同じ確認単位として扱い、背景名は順序検査です。不適切な選択肢を整理します。 A: 順序検査の運用コマンドは別カテゴリの確認を流用しており、ENF 41 Listenerの根拠にならないため順序検査ではありません。 B: 順序検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため順序検査ではありません。 C: 順序検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので順序検査です。 D: 順序検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序検査ではありません。順序検査の運用コマンドが示す ENF 41 Listenerは出典欄の資料で使い方を追跡できる項目であり、用語名は順序検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ENF 41 Listener**

    - 検証目的: 出力分離の運用コマンドについて、ENF 41 Listenerは、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030148の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、出力分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にENF 41 Listenerを指定し、OSKB030148の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ENF 41 Listener
    CASE OSKB030148
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ENF 41 Listener
    CASE OSKB030148
    SOURCE SMP/E SMF WLM
    ```

    ENF 41 ListenerとOSKB030148が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030148を同じ出力で読み、出力分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030148
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030148
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ENF 41 Listener REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030148が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ENF 41 Listener と OSKB030148 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030148 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### ENF 57 Listener {#c28-i0384}
*分類: WLM 運用コマンド*  ・  難易度: 上級

ENF 57 Listenerは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 値域検査の運用コマンドに関する ENF 57 Listenerの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず値域検査の運用コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の運用コマンドの証跡として保存して根拠にする。
    - C. ENF 57 Listenerの変更点を出力本文から切り離して値域検査の運用コマンドの承認欄のみ残す。
    - D. 机上確認でも実出力の見出しに合わせ、値域検査の確認値として扱う。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検査の運用コマンドにおいて選択記号 D を採用し、識別名は値域検査です。値域検査の運用コマンドにおいて ENF 57 Listener は説明欄の「ENF 57 Listenerの状態と出力メッセージを結び付ける値域検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査の運用コマンドに関する記録は、ENF 57 Listenerの出力行と IWM025I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため値域検査ではありません。 B: 値域検査の運用コマンドは別カテゴリの確認を流用しており、ENF 57 Listenerの根拠にならないため値域検査ではありません。 C: 値域検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査の運用コマンドで記録する ENF 57 Listenerは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は値域検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **ENF 57 Listener**

    - 検証目的: 条件分離の運用コマンドについて、ENF 57 Listenerは、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030149の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、条件分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にENF 57 Listenerを指定し、OSKB030149の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND ENF 57 Listener
    CASE OSKB030149
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM ENF 57 Listener
    CASE OSKB030149
    SOURCE SMP/E SMF WLM
    ```

    ENF 57 ListenerとOSKB030149が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030149を同じ出力で読み、条件分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030149
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030149
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I ENF 57 Listener REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030149が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の ENF 57 Listener と OSKB030149 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030149 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### F WLM,APPLENV=...,REFRESH {#c28-i0385}
*分類: WLM 運用コマンド*  ・  難易度: 上級

F WLM,APPLENV=...,REFRESHは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)


### F WLM,MODE=GOAL {#c28-i0386}
*分類: WLM 運用コマンド*  ・  難易度: 上級

F WLM,MODE=GOALは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 区切検査の運用コマンドで F WLM,MODE=GOAL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. F WLM,MODE=GOAL の出力を取らず区切検査の運用コマンドの説明文と承認印のみを残す。
    - B. 同じ画面で対象行と IWM025I を読み、区切検査の結果として保存する。 ✅
    - C. D WLM,SYSTEMS を省略して区切検査の運用コマンドの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査の運用コマンドへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切検査の運用コマンドにおいて選択記号 B を採用し、識別名は区切検査です。区切検査の運用コマンドにおいて F WLM,MODE=GOAL は説明欄の「区切検査の運用コマンドに関係する定義値と表示行を照合する区切検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は区切検査です。区切検査の運用コマンドの証跡を読む担当者は、F WLM,MODE=GOAL の属性行と IWM025I を合わせて追跡し、背景名は区切検査です。誤答側の問題点を分けます。 A: 区切検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切検査ではありません。 B: 区切検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので区切検査です。 C: 区切検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため区切検査ではありません。 D: 区切検査の運用コマンドは別カテゴリの確認を流用しており、F WLM,MODE=GOAL の根拠にならないため区切検査ではありません。区切検査の運用コマンドに出る F WLM,MODE=GOAL は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は区切検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **F WLM,MODE=GOAL**

    - 検証目的: 呼出分離の運用コマンドについて、F WLM,MODE=GOAL は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030143の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、呼出分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にF WLM,MODE=GOALを指定し、OSKB030143の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND F WLM,MODE=GOAL
    CASE OSKB030143
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM F WLM,MODE=GOAL
    CASE OSKB030143
    SOURCE SMP/E SMF WLM
    ```

    F WLM,MODE=GOALとOSKB030143が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030143を同じ出力で読み、呼出分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030143
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030143
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I F WLM,MODE=GOAL REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030143が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の F WLM,MODE=GOAL と OSKB030143 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030143 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### Goal vs Velocity 選択 {#c28-i0387}
*分類: WLM 運用コマンド*  ・  難易度: 上級

Goal vs Velocity 選択は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。Goal vs Velocity 選択は、応答時間が測定できる Response Time、長時間バッチ Velocity。応答時間が測定できる → Response Time、長時間バッチ → Velocity

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 復旧検査の選択で Goal vs Velocity 選択の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Goal vs Velocity 選択の出力を取らず復旧検査の選択の説明文と承認印のみを残す。
    - B. IWM025I を含む表示を保存し、説明欄との差分を復旧検査で確認する。 ✅
    - C. D WLM,SYSTEMS を省略して復旧検査の選択の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の選択へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検査の選択において選択記号 B を採用し、識別名は復旧検査です。復旧検査の選択において Goal vs Velocity 選択 は説明欄の「復旧検査の選択に関係する定義値と表示行を照合する復旧検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は復旧検査です。復旧検査の選択の証跡を読む担当者は、Goal vs Velocity 選択の属性行と IWM025I を合わせて追跡し、背景名は復旧検査です。誤答側の問題点を分けます。 A: 復旧検査の選択は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧検査ではありません。 B: 復旧検査の選択は対象出力と項目説明を結び、根拠を残すので復旧検査です。 C: 復旧検査の選択は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため復旧検査ではありません。 D: 復旧検査の選択は別カテゴリの確認を流用しており、Goal vs Velocity 選択の根拠にならないため復旧検査ではありません。復旧検査の選択に出る Goal vs Velocity 選択は SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は復旧検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Goal vs Velocity 選択**

    - 検証目的: 範囲分離の選択について、Goal vs Velocity 選択は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。Goal vs Veloに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030151の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、範囲分離の選択の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にGoal vs Velocity 選を指定し、OSKB030151の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Goal vs Velocity 選
    CASE OSKB030151
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Goal vs Velocity 選
    CASE OSKB030151
    SOURCE SMP/E SMF WLM
    ```

    Goal vs Velocity 選とOSKB030151が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030151を同じ出力で読み、範囲分離の選択の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030151
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030151
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Goal vs Velocity 選択 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030151が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Goal vs Velocity 選 と OSKB030151 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030151 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### PI (Performance Index) {#c28-i0388}
*分類: WLM 運用コマンド*  ・  難易度: 上級

PI (Performance Index)は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 監査追跡の運用コマンドで保守管理の運用確認を行います。PI 属性の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で監査追跡の運用コマンドを確認した扱いにする。
    - B. IWM025I の有無を確認せず監査追跡の運用コマンドを正常終了として記録する。
    - C. D WLM,SYSTEMS で得た表示本文を使い、監査追跡の採否を説明欄に結び付ける。 ✅
    - D. PI 属性の属性行を読まず監査追跡の運用コマンドの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査追跡の運用コマンドにおいて選択記号 C を採用し、識別名は監査追跡です。監査追跡の運用コマンドにおいて PI 属性 は説明欄の「SMP/E SMF WLM で PI 属性の扱いを記録する監査追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は監査追跡です。監査追跡の運用コマンドを受け取る担当者は、PI 属性の表示結果と IWM025I を同じ確認単位として扱い、背景名は監査追跡です。不適切な選択肢を整理します。 A: 監査追跡の運用コマンドは別カテゴリの確認を流用しており、PI 属性の根拠にならないため監査追跡ではありません。 B: 監査追跡の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため監査追跡ではありません。 C: 監査追跡の運用コマンドは対象出力と項目説明を結び、根拠を残すので監査追跡です。 D: 監査追跡の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査追跡ではありません。監査追跡の運用コマンドが示す PI 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は監査追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **PI (Performance Index)**

    - 検証目的: 優先記録の運用コマンドについて、PI (Performance Index)は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030132の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先記録の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にPI (Performance Inを指定し、OSKB030132の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND PI (Performance In
    CASE OSKB030132
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM PI (Performance In
    CASE OSKB030132
    SOURCE SMP/E SMF WLM
    ```

    PI (Performance InとOSKB030132が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030132を同じ出力で読み、優先記録の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030132
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030132
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I PI (Performance Index) REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030132が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の PI (Performance In と OSKB030132 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030132 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### PI < 1.0 {#c28-i0389}
*分類: WLM 運用コマンド*  ・  難易度: 上級

PI < 1.0は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)


### PI = 1.0 {#c28-i0390}
*分類: WLM 運用コマンド*  ・  難易度: 上級

PI = 1.0は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 変更追跡の運用コマンドに関する PI = 1.0の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず変更追跡の運用コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡の運用コマンドの証跡として保存して根拠にする。
    - C. PI = 1.0の変更点を出力本文から切り離して変更追跡の運用コマンドの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、変更追跡として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更追跡の運用コマンドにおいて選択記号 D を採用し、識別名は変更追跡です。変更追跡の運用コマンドにおいて PI = 1.0 は説明欄の「PI = 1.0の状態と出力メッセージを結び付ける変更追跡項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は変更追跡です。変更追跡の運用コマンドに関する記録は、PI = 1.0の出力行と IWM025I を一緒に保存し、背景名は変更追跡です。選択肢ごとの違いを示します。 A: 変更追跡の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため変更追跡ではありません。 B: 変更追跡の運用コマンドは別カテゴリの確認を流用しており、PI = 1.0の根拠にならないため変更追跡ではありません。 C: 変更追跡の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更追跡ではありません。 D: 変更追跡の運用コマンドは対象出力と項目説明を結び、根拠を残すので変更追跡です。変更追跡の運用コマンドで記録する PI = 1.0は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は変更追跡です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **PI = 1.0**

    - 検証目的: 記録記録の運用コマンドについて、PI = 1.0は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030133の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、記録記録の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にPI = 1.0を指定し、OSKB030133の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND PI = 1.0
    CASE OSKB030133
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM PI = 1.0
    CASE OSKB030133
    SOURCE SMP/E SMF WLM
    ```

    PI = 1.0とOSKB030133が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030133を同じ出力で読み、記録記録の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030133
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030133
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I PI = 1.0 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030133が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の PI = 1.0 と OSKB030133 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030133 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### PI > 1.0 {#c28-i0391}
*分類: WLM 運用コマンド*  ・  難易度: 上級

PI 1 超.0は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)


### RMF Monitor III SYSSUM {#c28-i0392}
*分類: WLM 運用コマンド*  ・  難易度: 上級

RMF Monitor III SYSSUMは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 優先検査の運用コマンドに関する RMF Monitor III SYSSUM の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず優先検査の運用コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の運用コマンドの証跡として保存して根拠にする。
    - C. RMF Monitor III SYSSUM の変更点を出力本文から切り離して優先検査の運用コマンドの承認欄のみ残す。
    - D. 資料上の説明と画面上の表示行を突き合わせ、優先検査として引き継ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検査の運用コマンドにおいて選択記号 D を採用し、識別名は優先検査です。優先検査の運用コマンドにおいて RMF Monitor III SYSSUM は説明欄の「RMF Monitor III SYSSUM の状態と出力メッセージを結び付ける優先検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査の運用コマンドに関する記録は、RMF Monitor III SYSSUM の出力行と IWM025I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため優先検査ではありません。 B: 優先検査の運用コマンドは別カテゴリの確認を流用しており、RMF Monitor III SYSSUM の根拠にならないため優先検査ではありません。 C: 優先検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査の運用コマンドで記録する RMF Monitor III SYSSUM は SMP/E SMF WLM の確認記録に残す対象名であり、用語名は優先検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **RMF Monitor III SYSSUM**

    - 検証目的: 終端分離の運用コマンドについて、RMF Monitor III SYSSUM は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030145の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、終端分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にRMF Monitor III SYを指定し、OSKB030145の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND RMF Monitor III SY
    CASE OSKB030145
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM RMF Monitor III SY
    CASE OSKB030145
    SOURCE SMP/E SMF WLM
    ```

    RMF Monitor III SYとOSKB030145が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030145を同じ出力で読み、終端分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030145
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030145
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I RMF Monitor III SYSSUM REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030145が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の RMF Monitor III SY と OSKB030145 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030145 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### RMF Monitor III WFEX {#c28-i0393}
*分類: WLM 運用コマンド*  ・  難易度: 上級

RMF Monitor III WFEXは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 記録検査の運用コマンドに関係する RMF Monitor III WFEX の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録検査の確認にする。 ✅
    - B. RMF Monitor III WFEX の名称と担当者名のみを残して記録検査の運用コマンドの表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で記録検査の運用コマンドを確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず記録検査の運用コマンドの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検査の運用コマンドにおいて選択記号 A を採用し、識別名は記録検査です。記録検査の運用コマンドにおいて RMF Monitor III WFEX は説明欄の「RMF Monitor III WFEX の用途を保守管理の表示で確認する記録検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は記録検査です。記録検査の運用コマンドに関連して、SMP/E SMF WLM では RMF Monitor III WFEX の表示属性と IWM025I を同じ証跡に残し、背景名は記録検査です。他の選択肢を確認します。 A: 記録検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので記録検査です。 B: 記録検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録検査ではありません。 C: 記録検査の運用コマンドは別カテゴリの確認を流用しており、RMF Monitor III WFEX の根拠にならないため記録検査ではありません。 D: 記録検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため記録検査ではありません。記録検査の運用コマンドで使う RMF Monitor III WFEX という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は記録検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **RMF Monitor III WFEX**

    - 検証目的: 探索分離の運用コマンドについて、RMF Monitor III WFEX は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030146の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、探索分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にRMF Monitor III WFを指定し、OSKB030146の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND RMF Monitor III WF
    CASE OSKB030146
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM RMF Monitor III WF
    CASE OSKB030146
    SOURCE SMP/E SMF WLM
    ```

    RMF Monitor III WFとOSKB030146が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030146を同じ出力で読み、探索分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030146
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030146
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I RMF Monitor III WFEX REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030146が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の RMF Monitor III WF と OSKB030146 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030146 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### SMF 99 と WLM 内部 {#c28-i0394}
*分類: WLM 運用コマンド*  ・  難易度: 上級

SMF 99 と WLM 内部は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 警告検査のと 内部に関係する SMF 99 と WLM 内部の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 参照資料名、表示行、メッセージをそろえて警告検査の根拠を固定する。 ✅
    - B. SMF 99 と WLM 内部の名称と担当者名のみを残して警告検査のと 内部の表示本文を確認対象に含めない。
    - C. 保守管理以外の画面で警告検査のと 内部を確認し同じ証跡として扱ったことにする。
    - D. IWM025I の有無を見ず警告検査のと 内部の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検査のと 内部において選択記号 A を採用し、識別名は警告検査です。警告検査のと 内部において SMF 99 と WLM 内部 は説明欄の「SMF 99 と WLM 内部の用途を保守管理の表示で確認する警告検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査のと 内部に関連して、SMP/E SMF WLM では SMF 99 と WLM 内部の表示属性と IWM025I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査のと 内部は対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査のと 内部は名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査のと 内部は別カテゴリの確認を流用しており、SMF 99 と WLM 内部の根拠にならないため警告検査ではありません。 D: 警告検査のと 内部は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため警告検査ではありません。警告検査のと 内部で使う SMF 99 と WLM 内部という用語は SMP/E / SMF / WLM で扱う確認対象であり、用語名は警告検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **SMF 99 と WLM 内部**

    - 検証目的: 区切分離のと 内部について、SMF 99 と WLM 内部は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030150の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、区切分離のと 内部の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にSMF 99 と WLM 内部を指定し、OSKB030150の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND SMF 99 と WLM 内部
    CASE OSKB030150
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM SMF 99 と WLM 内部
    CASE OSKB030150
    SOURCE SMP/E SMF WLM
    ```

    SMF 99 と WLM 内部とOSKB030150が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030150を同じ出力で読み、区切分離のと 内部の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030150
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030150
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I SMF 99 と WLM 内部 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030150が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の SMF 99 と WLM 内部 と OSKB030150 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030150 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### V WLM,POLICY=name {#c28-i0395}
*分類: WLM 運用コマンド*  ・  難易度: 上級

V WLM,POLICY=nameは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 出力検査の運用コマンドに関する V WLM,POLICY=nameの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. D WLM,SYSTEMS の結果を残さず出力検査の運用コマンドの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の運用コマンドの証跡として保存して根拠にする。
    - C. V WLM,POLICY=nameの変更点を出力本文から切り離して出力検査の運用コマンドの承認欄のみ残す。
    - D. 出典欄の説明と運用出力を照合し、出力検査の確認記録にまとめる。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力検査の運用コマンドにおいて選択記号 D を採用し、識別名は出力検査です。出力検査の運用コマンドにおいて V WLM,POLICY=name は説明欄の「V WLM,POLICY=nameの状態と出力メッセージを結び付ける出力検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査の運用コマンドに関する記録は、V WLM,POLICY=nameの出力行と IWM025I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査の運用コマンドは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため出力検査ではありません。 B: 出力検査の運用コマンドは別カテゴリの確認を流用しており、V WLM,POLICY=nameの根拠にならないため出力検査ではありません。 C: 出力検査の運用コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査の運用コマンドは対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査の運用コマンドで記録する V WLM,POLICY=nameは SMP/E SMF WLM の確認記録に残す対象名であり、用語名は出力検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **V WLM,POLICY=name**

    - 検証目的: 構文分離の運用コマンドについて、V WLM,POLICY=nameは、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030141の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、構文分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にV WLM,POLICY=nameを指定し、OSKB030141の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND V WLM,POLICY=name
    CASE OSKB030141
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM V WLM,POLICY=name
    CASE OSKB030141
    SOURCE SMP/E SMF WLM
    ```

    V WLM,POLICY=nameとOSKB030141が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030141を同じ出力で読み、構文分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030141
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030141
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I V WLM,POLICY=name REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030141が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の V WLM,POLICY=name と OSKB030141 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030141 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### V WLM,POLICY=name,REFRESH {#c28-i0396}
*分類: WLM 運用コマンド*  ・  難易度: 上級

V WLM,POLICY=name,REFRESHは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? note "検証手順（1件）"
    **V WLM,POLICY=name,REFRESH**

    - 検証目的: 展開分離の運用コマンドについて、V WLM,POLICY=name,REFRESH は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030142の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、展開分離の運用コマンドの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にV WLM,POLICY=name,を指定し、OSKB030142の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND V WLM,POLICY=name,
    CASE OSKB030142
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM V WLM,POLICY=name,
    CASE OSKB030142
    SOURCE SMP/E SMF WLM
    ```

    V WLM,POLICY=name,とOSKB030142が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030142を同じ出力で読み、展開分離の運用コマンドの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030142
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030142
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I V WLM,POLICY=name,REFRES REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030142が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の V WLM,POLICY=name, と OSKB030142 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030142 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### Velocity の典型値 {#c28-i0397}
*分類: WLM 運用コマンド*  ・  難易度: 上級

Velocity の典型値は、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 監査検査のの典型値で保守管理の運用確認を行います。Velocity の典型値の根拠にできる作業はどれですか。

    - A. SMP/E SMF WLM と無関係な一覧で監査検査のの典型値を確認した扱いにする。
    - B. IWM025I の有無を確認せず監査検査のの典型値を正常終了として記録する。
    - C. D WLM,SYSTEMS の結果から対象行を抜き出し、監査検査の証跡として残す。 ✅
    - D. Velocity の典型値の属性行を読まず監査検査のの典型値の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検査のの典型値において選択記号 C を採用し、識別名は監査検査です。監査検査のの典型値において Velocity の典型値 は説明欄の「SMP/E SMF WLM で Velocity の典型値の扱いを記録する監査検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は監査検査です。監査検査のの典型値を受け取る担当者は、Velocity の典型値の表示結果と IWM025I を同じ確認単位として扱い、背景名は監査検査です。不適切な選択肢を整理します。 A: 監査検査のの典型値は別カテゴリの確認を流用しており、Velocity の典型値の根拠にならないため監査検査ではありません。 B: 監査検査のの典型値は戻り値や記録番号に寄り、IWM025I や属性表示を落とすため監査検査ではありません。 C: 監査検査のの典型値は対象出力と項目説明を結び、根拠を残すので監査検査です。 D: 監査検査のの典型値は名称や説明のみに寄り、状態を示す出力本文が不足するため監査検査ではありません。監査検査のの典型値が示す Velocity の典型値は出典欄の資料で使い方を追跡できる項目であり、用語名は監査検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **Velocity の典型値**

    - 検証目的: 優先分離のの典型値について、Velocity の典型値は、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態のに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030152の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、優先分離のの典型値の確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にVelocity の典型値を指定し、OSKB030152の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND Velocity の典型値
    CASE OSKB030152
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM Velocity の典型値
    CASE OSKB030152
    SOURCE SMP/E SMF WLM
    ```

    Velocity の典型値とOSKB030152が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030152を同じ出力で読み、優先分離のの典型値の根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030152
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030152
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I Velocity の典型値 REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030152が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の Velocity の典型値 と OSKB030152 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030152 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)



### WLM ENF イベント {#c28-i0398}
*分類: WLM 運用コマンド*  ・  難易度: 上級

WLM ENF イベントは、SMP/E / SMF / WLMのWLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands (zOS31_ieag100) / z/OS MVS Planning Workload Management (zOS31_ieaw100) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)

??? question "確認問題（1問）"
    **問題.** 比較検査のイベントで WLM ENF イベントの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. WLM ENF イベントの出力を取らず比較検査のイベントの説明文と承認印のみを残す。
    - B. SMP/E SMF WLM の表示形式に沿って根拠行を採り、比較検査の点検結果を残す。 ✅
    - C. D WLM,SYSTEMS を省略して比較検査のイベントの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査のイベントへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検査のイベントにおいて選択記号 B を採用し、識別名は比較検査です。比較検査のイベントにおいて WLM ENF イベント は説明欄の「比較検査のイベントに関係する定義値と表示行を照合する比較検査項目」と D WLM,SYSTEMS または該当パネルの出力を照合する対象で、答え名は比較検査です。比較検査のイベントの証跡を読む担当者は、WLM ENF イベントの属性行と IWM025I を合わせて追跡し、背景名は比較検査です。誤答側の問題点を分けます。 A: 比較検査のイベントは名称や説明のみに寄り、状態を示す出力本文が不足するため比較検査ではありません。 B: 比較検査のイベントは対象出力と項目説明を結び、根拠を残すので比較検査です。 C: 比較検査のイベントは戻り値や記録番号に寄り、IWM025I や属性表示を落とすため比較検査ではありません。 D: 比較検査のイベントは別カテゴリの確認を流用しており、WLM ENF イベントの根拠にならないため比較検査ではありません。比較検査のイベントに出る WLM ENF イベントは SMP/E / SMF / WLM の運用手順で意味を確認する対象であり、用語名は比較検査です。

    **出典:** and Diagnosis（zOS31_gim0000） / OS MVS System Commands（zOS31_ieag100）


??? note "検証手順（1件）"
    **WLM ENF イベント**

    - 検証目的: 上書分離のイベントについて、WLM ENF イベントは、SMP/E / SMF / WLM の WLM 運用コマンドで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: SMP/Eまたは関連TSO/コンソールを参照でき、OSKB030147の検証用出力を記録できる。
    - セッション環境: SMP/EでD WLM,SYSTEMSを実行し、IWM025Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はSMP/Eのコマンド入力画面です。COMMAND INPUT ===> に D WLM,SYSTEMS を入力し、上書分離のイベントの確認表示へ進みます。
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
    現在の画面はSMP/Eの表示結果です。FIND欄にWLM ENF イベントを指定し、OSKB030147の対象行を見つけます。
    操作（入力）:
    ```text
    (SMP/E Result)
    COMMAND INPUT ===> FIND WLM ENF イベント
    CASE OSKB030147
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SMP/E Result)
    ITEM WLM ENF イベント
    CASE OSKB030147
    SOURCE SMP/E SMF WLM
    ```

    WLM ENF イベントとOSKB030147が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はSMP/Eの詳細表示です。IWM025IとOSKB030147を同じ出力で読み、上書分離のイベントの根拠を記録します。
    操作（入力）:
    ```text
    (SMP/E Detail)
    COMMAND INPUT ===> D WLM,SYSTEMS
    CASE OSKB030147
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMP/E REPORT OSKB030147
    COMMAND INPUT ===> D WLM,SYSTEMS
    IWM025I WLM ENF イベント REPORT FOLLOWS
    ZONE TARGET1 STATUS REVIEWED
    ```

    IWM025IとOSKB030147が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> D WLM,SYSTEMS が画面・出力に表示されること
    ② ステップ2 の WLM ENF イベント と OSKB030147 が画面・出力に表示されること
    ③ ステップ3 の IWM025I と OSKB030147 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (zOS31_ieag100) / OS MVS Planning Workload Management (zOS31_ieaw100)


