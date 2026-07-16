---
search:
  exclude: true
---

# IBM Workload Automation — 詳細 (3/3)

[← IBM Workload Automation の概要へ戻る](index.md)


## IBM Workload Automation > 定義

### ジョブ記述 {#c15-i0194}
*分類: 定義*  ・  難易度: 中級

IBM Workload Automation の 定義で扱うジョブ記述は、スケジューラが投入する z/OS ジョブや開始タスクの属性を定義する情報です。JCL、実行ワークステーション、依存関係、リカバリ動作と結び付きます。障害時は JES 上のジョブと scheduler 上の操作を対応させます

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 探索確認のジョブ記述でジョブ記述の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ジョブ記述の出力を取らず探索確認のジョブ記述の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 ✅
    - C. OPSTAT を省略して探索確認のジョブ記述の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認のジョブ記述へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠ではジョブ記述は「探索確認のジョブ記述に関係する定義値と表示行を照合する探索確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡ではジョブ記述の属性行と EQQZ045I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出ではジョブ記述を IBM Workload Automationの運用手順で確認し、初出名は探索確認初出です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **ジョブ記述**

    - 検証目的: 探索確認のジョブ記述について、IBM Workload Automation の 定義で扱うジョブ記述は、スケジューラが投入する z/OS ジョブや開始タスクの属性を定義する情報です。JCL、実行ワークに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、探索確認のジョブ記述の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にジョブ記述を指定し、OSKB010006の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND ジョブ記述
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM ジョブ記述
    CASE OSKB010006
    SOURCE IBM Workload Automation
    ```

    ジョブ記述とOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010006を同じ出力で読み、探索確認のジョブ記述の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010006
    COMMAND ===> OPSTAT
    OPERATION OSKB010006 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の ジョブ記述 と OSKB010006 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler



### ワークステーション {#c15-i0195}
*分類: 定義*  ・  難易度: 中級

IBM Workload Automation の 定義で扱うワークステーションは、ジョブや操作を実行する論理的な処理場所を表す定義です。z/OS の実行先、手作業、プリンターなどを区別できます。ジョブが投入されない場合は、ワークステーションの可用性と宛先を確認します

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 置換確認のワークステーションに関するワークステーションの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. OPSTAT の結果を残さず置換確認のワークステーションの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認のワークステーションの証跡として保存して根拠にする。
    - C. ワークステーションの変更点を出力本文から切り離して置換確認のワークステーションの承認欄のみ残す。
    - D. 同じ画面で対象行と EQQZ045I を読み、置換確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠ではワークステーションは「ワークステーションの状態と出力メッセージを結び付ける置換確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存ではワークステーションの出力行と EQQZ045I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象ではワークステーションを IBM Workload Automationの確認記録に残し、対象名は置換確認対象です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **ワークステーション**

    - 検証目的: 置換確認のワークステーションについて、IBM Workload Automation の 定義で扱うワークステーションは、ジョブや操作を実行する論理的な処理場所を表す定義です。z/OS の実行先、手作業、プリンに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、置換確認のワークステーションの確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にワークステーションを指定し、OSKB010004の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND ワークステーション
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM ワークステーション
    CASE OSKB010004
    SOURCE IBM Workload Automation
    ```

    ワークステーションとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010004を同じ出力で読み、置換確認のワークステーションの根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010004
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010004
    COMMAND ===> OPSTAT
    OPERATION OSKB010004 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の ワークステーション と OSKB010004 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler



### 特殊資源 {#c15-i0196}
*分類: 定義*  ・  難易度: 中級

IBM Workload Automation の 定義で扱う特殊資源は、データセット、テープ装置、業務上の排他対象などを scheduler 上で資源として扱う定義です。競合するジョブの同時実行を防ぐために使います。滞留時は資源を保持している操作と待っている操作を確認します

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 出力確認の特殊資源に関する特殊資源の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. OPSTAT の結果を残さず出力確認の特殊資源の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の特殊資源の証跡として保存して根拠にする。
    - C. 特殊資源の変更点を出力本文から切り離して出力確認の特殊資源の承認欄のみ残す。
    - D. IBM Workload Automationの表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では特殊資源は「特殊資源の状態と出力メッセージを結び付ける出力確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では特殊資源の出力行と EQQZ045I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では特殊資源を IBM Workload Automationの確認記録に残し、対象名は出力確認対象です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **特殊資源**

    - 検証目的: 出力確認の特殊資源について、IBM Workload Automation の 定義で扱う特殊資源は、データセット、テープ装置、業務上の排他対象などを scheduler 上で資源として扱う定義です。に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、出力確認の特殊資源の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄に特殊資源を指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND 特殊資源
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM 特殊資源
    CASE OSKB010008
    SOURCE IBM Workload Automation
    ```

    特殊資源とOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010008を同じ出力で読み、出力確認の特殊資源の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010008
    COMMAND ===> OPSTAT
    OPERATION OSKB010008 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の 特殊資源 と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler




## IBM Workload Automation > 操作

### Dynamic Workload Console {#c15-i0197}
*分類: 操作*  ・  難易度: 初級

IBM Workload Automation の 操作で扱うDynamic Workload Consoleは、計画確認、操作監視、問題調査を Web から行うためのインターフェースです。z/OS の ISPF パネルと役割が重なる部分もあります。運用手順ではどの画面で状態を確認するかを明確にします

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 順序確認の操作で作業スケジューラーの運用確認を行います。Dynamic Workload Consoleの根拠にできる作業はどれですか。

    - A. IBM Workload Automationと無関係な一覧で順序確認の操作を確認した扱いにする。
    - B. EQQZ045I の有無を確認せず順序確認の操作を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 ✅
    - D. Dynamic Workload Consoleの属性行を読まず順序確認の操作の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Dynamic Workload Console は「IBM Workload Automationで Dynamic Workload Consoleの扱いを記録する順序確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Dynamic Workload Consoleの表示結果と EQQZ045I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Dynamic Workload Consoleの使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **Dynamic Workload Console**

    - 検証目的: 順序確認の操作について、IBM Workload Automation の 操作で扱う Dynamic Workload Consoleは、計画確認、操作監視、問題調査を Web から行うためのインに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、順序確認の操作の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にDynamic Workload Cを指定し、OSKB010015の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND Dynamic Workload C
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM Dynamic Workload C
    CASE OSKB010015
    SOURCE IBM Workload Automation
    ```

    Dynamic Workload CとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010015を同じ出力で読み、順序確認の操作の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010015
    COMMAND ===> OPSTAT
    OPERATION OSKB010015 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の Dynamic Workload C と OSKB010015 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler



### ISPF パネルインターフェース {#c15-i0198}
*分類: 操作*  ・  難易度: 初級

IBM Workload Automation の 操作で扱うISPF パネルインターフェースは、z/OS 上で Z Workload Scheduler を操作するための対話画面です。計画、操作、依存関係、エラー状態をメインフレーム端末上で確認できます。障害時は画面上の操作番号と JES ジョブ名を対応させます

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 値域確認のパネルインターフェースに関する ISPF パネルインターフェースの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. OPSTAT の結果を残さず値域確認のパネルインターフェースの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認のパネルインターフェースの証跡として保存して根拠にする。
    - C. ISPF パネルインターフェースの変更点を出力本文から切り離して値域確認のパネルインターフェースの承認欄のみ残す。
    - D. 同じ画面で対象行と EQQZ045I を読み、値域確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では ISPF パネルインターフェース は「ISPF パネルインターフェースの状態と出力メッセージを結び付ける値域確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では ISPF パネルインターフェースの出力行と EQQZ045I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では ISPF パネルインターフェースを IBM Workload Automationの確認記録に残し、対象名は値域確認対象です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **ISPF パネルインターフェース**

    - 検証目的: 値域確認のパネルインターフェースについて、IBM Workload Automation の 操作で扱う ISPF パネルインターフェースは、z/OS 上で Z Workload Scheduler を操作するためのに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、値域確認のパネルインターフェースの確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にISPF パネルインターフェースを指定し、OSKB010016の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND ISPF パネルインターフェース
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM ISPF パネルインターフェース
    CASE OSKB010016
    SOURCE IBM Workload Automation
    ```

    ISPF パネルインターフェースとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010016を同じ出力で読み、値域確認のパネルインターフェースの根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010016
    COMMAND ===> OPSTAT
    OPERATION OSKB010016 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の ISPF パネルインターフェース と OSKB010016 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler




## IBM Workload Automation > 特殊資源管理

### conman submit sched 再実行判断 再計画083 {#c15-i0199}
*分類: 特殊資源管理*  ・  難易度: 上級

第八十三観点 特殊資源管理 の 再計画083 では conman submit sched を点検します。第八十三観点 対象は スケジュール済みのジョブストリームをオンデマンドで投入し、計画外作業を運用記録付きでです。第八十三観点 待ち状態がある時は ISPF パネルのワークステーション列 と IWAJOB103 の時刻差を確認します。第八十三観点 ジョブログは JES の purge 前に IWAログ103へ転記します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **conman submit sched 再実行判断 再計画083**

    - 検証目的: 特殊資源管理における conman submit sched の再実行判断を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=IWAJOB103
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、conman submit sched の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    IBM Z Workload Scheduler > Workload > Monitor > Monitor Jobs
    Filter job ===> IWAJOB103
    → Enter を押す
    ```

    画面・出力:
    ```text
    Monitor Jobs
    Engine ZWS1 Job IWAJOB103 Job Stream PAYROLL103 Status Successful Workstation CPU11
    ```

    画面・出力には Monitor が含まれる。Monitor を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、ISPF パネルのワークステーション列 と IWAJOB103 の対応を確認する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    Selected job IWAJOB103
    Action ===> Job Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Log for IWAJOB103
    JESMSGLG JOB IWAJOB103
    IEF142I IWAJOB103 STEP010 - STEP WAS EXECUTED - COND CODE 0000
    ```

    画面・出力には IWAJOB103 が含まれる。IWAJOB103 を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    Selected job IWAJOB103
    Action ===> Properties
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Properties
    Job IWAJOB103
    Internal status Successful
    Return code 0000
    Operation 110
    ```

    画面・出力には Properties が含まれる。Properties を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: Monitor が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: IWAJOB103 が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: Properties が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### conman submit sched 実行監視 資源確認053 {#c15-i0200}
*分類: 特殊資源管理*  ・  難易度: 中級

第五十三観点 conman submit sched は IBM Workload Automation の 特殊資源管理 で扱う確認点です。第五十三観点 対象は スケジュール済みのジョブストリームをオンデマンドで投入し、計画外作業を運用記録付きでです。第五十三観点 採取値 IWAJOB073 を計画表とログの両方で読み、採取時刻をそろえます。第五十三観点 採取後は DWC 表示と ISPF 表示の差を IWA比較073に分けます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **conman submit sched 実行監視 資源確認053**

    - 検証目的: 特殊資源管理における conman submit sched の実行監視を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=IWAJOB073
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、conman submit sched の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    IBM Z Workload Scheduler > Workload > Monitor > Monitor Jobs
    Filter job ===> IWAJOB073
    → Enter を押す
    ```

    画面・出力:
    ```text
    Monitor Jobs
    Engine ZWS1 Job IWAJOB073 Job Stream PAYROLL073 Status Successful Workstation CPU05
    ```

    画面・出力には Monitor が含まれる。Monitor を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、ISPF パネルのワークステーション列 と IWAJOB073 の対応を確認する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    Selected job IWAJOB073
    Action ===> Job Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Log for IWAJOB073
    JESMSGLG JOB IWAJOB073
    IEF142I IWAJOB073 STEP010 - STEP WAS EXECUTED - COND CODE 0000
    ```

    画面・出力には IWAJOB073 が含まれる。IWAJOB073 を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    Selected job IWAJOB073
    Action ===> Properties
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Properties
    Job IWAJOB073
    Internal status Successful
    Return code 0000
    Operation 050
    ```

    画面・出力には Properties が含まれる。Properties を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: Monitor が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: IWAJOB073 が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: Properties が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### conman submit sched 計画反映 導入確認023 {#c15-i0201}
*分類: 特殊資源管理*  ・  難易度: 中級

第二十三観点 特殊資源管理 の 導入確認023 では conman submit sched を点検します。第二十三観点 対象は スケジュール済みのジョブストリームをオンデマンドで投入し、計画外作業を運用記録付きでです。第二十三観点 待ち状態がある時は ISPF パネルのワークステーション列 と IWAJOB043 の時刻差を確認します。第二十三観点 ジョブログは JES の purge 前に IWAログ043へ転記します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **conman submit sched 計画反映 導入確認023**

    - 検証目的: 特殊資源管理における conman submit sched の計画反映を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=IWAJOB043
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、conman submit sched の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    IBM Z Workload Scheduler > Workload > Monitor > Monitor Jobs
    Filter job ===> IWAJOB043
    → Enter を押す
    ```

    画面・出力:
    ```text
    Monitor Jobs
    Engine ZWS1 Job IWAJOB043 Job Stream PAYROLL043 Status Successful Workstation CPU11
    ```

    画面・出力には Monitor が含まれる。Monitor を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、ISPF パネルのワークステーション列 と IWAJOB043 の対応を確認する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    Selected job IWAJOB043
    Action ===> Job Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Log for IWAJOB043
    JESMSGLG JOB IWAJOB043
    IEF142I IWAJOB043 STEP010 - STEP WAS EXECUTED - COND CODE 0000
    ```

    画面・出力には IWAJOB043 が含まれる。IWAJOB043 を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    Dynamic Workload Console
    Selected job IWAJOB043
    Action ===> Properties
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Properties
    Job IWAJOB043
    Internal status Successful
    Return code 0000
    Operation 230
    ```

    画面・出力には Properties が含まれる。Properties を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: Monitor が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: IWAJOB043 が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: Properties が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### job stream 変更反映 再実行038 {#c15-i0202}
*分類: 特殊資源管理*  ・  難易度: 中級

第三十八観点 job stream の 再実行038 は IBM Workload Automation の 特殊資源管理 に属します。第三十八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第三十八観点 IWA058 の確認では tracker の通信完了メッセージ を起点に、RCY02 と対象 engine を照合します。第三十八観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡058として整理します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **job stream 変更反映 再実行038**

    - 検証目的: 特殊資源管理における job stream の変更反映を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY02
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> S IWAJOB058
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQRCLSE RESTART AND CLEANUP
    JOB IWAJOB058 OPERATION 140 STATUS ERROR
    CLEANUP DATA SETS DISPLAYED
    ```

    画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY02 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> VERIFY
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
    JOB IWAJOB058 RESTART ACTION REQUIRES CONFIRMATION
    ```

    画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> STEP
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESTART SELECTION
    JOB IWAJOB058 STEP STEP010 SELECTED
    CLEANUP ACTION LIST AVAILABLE
    ```

    画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### job stream 状態確認 照合098 {#c15-i0203}
*分類: 特殊資源管理*  ・  難易度: 上級

第九十八観点 job stream の 照合098 は IBM Workload Automation の 特殊資源管理 に属します。第九十八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第九十八観点 IWA118 の確認では tracker の通信完了メッセージ を起点に、RCY08 と対象 engine を照合します。第九十八観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡118として整理します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **job stream 状態確認 照合098**

    - 検証目的: 特殊資源管理における job stream の状態確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY08
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> S IWAJOB118
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQRCLSE RESTART AND CLEANUP
    JOB IWAJOB118 OPERATION 020 STATUS ERROR
    CLEANUP DATA SETS DISPLAYED
    ```

    画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY08 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> VERIFY
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
    JOB IWAJOB118 RESTART ACTION REQUIRES CONFIRMATION
    ```

    画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> STEP
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESTART SELECTION
    JOB IWAJOB118 STEP STEP010 SELECTED
    CLEANUP ACTION LIST AVAILABLE
    ```

    画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### job stream 資源制御 依存確認008 {#c15-i0204}
*分類: 特殊資源管理*  ・  難易度: 初級

第八観点 依存確認008 では 特殊資源管理 にある job stream を扱います。第八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第八観点 DWC と ISPF の結果を分け、RCY08 の記録先を明確にします。第八観点 資源待ちがあれば special resource 名を IWA資源028へ記録します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **job stream 資源制御 依存確認008**

    - 検証目的: 特殊資源管理における job stream の資源制御を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY08
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> S IWAJOB028
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQRCLSE RESTART AND CLEANUP
    JOB IWAJOB028 OPERATION 080 STATUS ERROR
    CLEANUP DATA SETS DISPLAYED
    ```

    画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY08 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> VERIFY
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
    JOB IWAJOB028 RESTART ACTION REQUIRES CONFIRMATION
    ```

    画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> STEP
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESTART SELECTION
    JOB IWAJOB028 STEP STEP010 SELECTED
    CLEANUP ACTION LIST AVAILABLE
    ```

    画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### job stream 障害切分け ログ採取068 {#c15-i0205}
*分類: 特殊資源管理*  ・  難易度: 中級

第六十八観点 ログ採取068 では 特殊資源管理 にある job stream を扱います。第六十八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第六十八観点 DWC と ISPF の結果を分け、RCY05 の記録先を明確にします。第六十八観点 資源待ちがあれば special resource 名を IWA資源088へ記録します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **job stream 障害切分け ログ採取068**

    - 検証目的: 特殊資源管理における job stream の障害切分けを机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY05
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> S IWAJOB088
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQRCLSE RESTART AND CLEANUP
    JOB IWAJOB088 OPERATION 200 STATUS ERROR
    CLEANUP DATA SETS DISPLAYED
    ```

    画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY05 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> VERIFY
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
    JOB IWAJOB088 RESTART ACTION REQUIRES CONFIRMATION
    ```

    画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQRCLSE -------- RESTART AND CLEANUP --------
    Command ===> STEP
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESTART SELECTION
    JOB IWAJOB088 STEP STEP010 SELECTED
    CLEANUP ACTION LIST AVAILABLE
    ```

    画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource ログとの照合 SR07 {#c15-i0206}
*分類: 特殊資源管理*  ・  難易度: 中級

ログとの照合では 特殊資源管理 の 資源モニター を主操作として SR07 を判定します。時刻と対象識別子への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR07 に残します。ログとの照合を補助する 使用操作 では ALLOCATED を補助値として SR07 へ保存します。主判定のログとの照合では特殊資源管理の 資源モニター から QUANTITY を読み SR07 へ残します。証跡照合のログとの照合では特殊資源管理の QUANTITY と ALLOCATED を SR07 に保存します。記録対応のログとの照合では特殊資源管理の QuantityとAvailability の証跡へ SR07 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** ログとの照合で 特殊資源管理 の 資源モニター と 使用操作 を用い 操作とログを対応 します。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。QUANTITY で対象 SR07 の QuantityとAvailability を再現できる記録はどれですか。

    - A. QUANTITYを含む資源モニターの応答行を保存する。その応答を得るためISPF EQQMTOPP option 7 SPECRESを使用する。対象SR07のQuantityとAvailabilityとして記録する。 ✅
    - B. ISPF EQQMTOPP option 7 SPECRESが応答を返した時点で正常とする。応答中のQUANTITYの値は記録しない。EQQR011IをQUANTITYと同じ判定値とみなし対象SR07の主証跡にする。Special Resourceの時刻と対象識別子は確認済みとして扱う。さらにSDSF browse EQQMLOG FIND SR07のEQQR011IをQUANTITYと同種の値として併記する。
    - C. ISPF EQQMTOPP option 7 SPECRESのコマンド文字列だけを記録する。QUANTITYを含む応答行は保存しない。
    - D. Special Resourceの停止または再定義を実施する。その後にISPF EQQMTOPP option 7 SPECRESでQUANTITYを採取する。

    正解: **A** ／ 難易度: 中級

    **解説:** 適切な判定: Aは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として操作とログを対応しSR07に残します。
    機能の仕組み: ログとの照合では使用操作を補助操作としSpecial Resourceの時刻と対象識別子をALLOCATEDと対象SR07で照合します。
    各候補の評価: 資源モニターと使用操作の役割を分けるとA: QUANTITYの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではQuantityとAvailabilityを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではQuantityとAvailabilityを証明できない点でQuantityとAvailabilityを確認できません、D: 変更前のQuantityとAvailabilityを失う点で使用操作の範囲を越えます。結論としてログとの照合の特殊資源管理で判定する対象は SR07 です。
    用語の定義: ログとの照合で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR07へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource ログとの照合 SR07**

    - 検証目的: 特殊資源管理のSpecial Resourceについて操作とログを対応し、SR07のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR07の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR07 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR07を指定し、SR07の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR07
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR07 ADID APP07 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR07を指定し、SR07のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR07
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR07 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
    ② ステップ2 の ALLOCATED が画面・出力に表示されること
    ③ ステップ3 の EQQR011I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 代替経路の確認 SR10 {#c15-i0207}
*分類: 特殊資源管理*  ・  難易度: 中級

代替経路の確認では 特殊資源管理 の 資源モニター を主操作として SR10 を判定します。主経路との役割差への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR10 に残します。代替経路の確認を補助する 使用操作 では ALLOCATED を補助値として SR10 へ保存します。主判定の代替経路の確認では特殊資源管理の 資源モニター から QUANTITY を読み SR10 へ残します。証跡照合の代替経路の確認では特殊資源管理の QUANTITY と ALLOCATED を SR10 に保存します。記録対応の代替経路の確認では特殊資源管理の QuantityとAvailability の証跡へ SR10 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 特殊資源管理 の 資源モニター と 使用操作 の役割を分け 主経路との役割差 を調べます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。対象 SR10 を誤判定しない進め方はどれですか。

    - A. ISPF EQQMTOPP option 7 SPECRESのコマンド文字列だけを記録する。QUANTITYを含む応答行は保存しない。
    - B. Special Resourceの停止または再定義を実施する。その後にISPF EQQMTOPP option 7 SPECRESでQUANTITYを採取する。
    - C. ジョブストリーム運用のInput ArrivalとStatusを確認する。その値を特殊資源管理のSR10にも適用する。
    - D. ISPF EQQMTOPP option 7 SPECRESとISPF Special Resource Monitor USERS SR10の対象名をそろえる。前者のQUANTITYをQuantityとAvailabilityの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい判定結果: Dは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として代替手段の成立を確認しSR10に残します。
    運用上の背景: 代替経路の確認では使用操作を補助操作としSpecial Resourceの主経路との役割差をALLOCATEDと対象SR10で照合します。
    候補別の検討: 資源モニターと使用操作の役割を分けるとA: 入力記録だけではQuantityとAvailabilityを証明できない点で一次資料と一致しません、B: 変更前のQuantityとAvailabilityを失う点でQuantityとAvailabilityを確認できません、C: ジョブストリーム運用の値ではQUANTITYを確認できない点で使用操作の範囲を越えます、D: 同じ対象名のQUANTITYを採用する点で現在値を示します。結論として代替経路の確認の特殊資源管理で判定する対象は SR10 です。
    重要用語の定義: 代替経路の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR10へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 代替経路の確認 SR10**

    - 検証目的: 特殊資源管理のSpecial Resourceについて代替手段の成立を確認し、SR10のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR10の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR10 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR10を指定し、SR10の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR10
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR10 ADID APP10 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR10を指定し、SR10のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR10
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR10 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
    ② ステップ2 の ALLOCATED が画面・出力に表示されること
    ③ ステップ3 の EQQR011I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 変更前の確認 SR02 {#c15-i0208}
*分類: 特殊資源管理*  ・  難易度: 中級

変更前の確認では 特殊資源管理 の 使用操作 を主操作として SR02 を判定します。変更対象と非対象の境界への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR02 に残します。変更前の確認を補助する イベントログ では EQQR011I を補助値として SR02 へ保存します。主判定の変更前の確認では特殊資源管理の 使用操作 から ALLOCATED を読み SR02 へ残します。証跡照合の変更前の確認では特殊資源管理の ALLOCATED と EQQR011I を SR02 に保存します。記録対応の変更前の確認では特殊資源管理の QuantityとAvailability の証跡へ SR02 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 特殊資源管理 の 使用操作 と イベントログ を照合し 変更対象と非対象の境界 を確かめます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。ALLOCATED を読む前に対象 SR02 へ行う確認はどれですか。

    - A. ISPF Special Resource Monitor USERS SR02を対象名なしで実行する。一覧の先頭行をSR02の結果として記録する。
    - B. 前回保存したISPF Special Resource Monitor USERS SR02の結果を使う。今回のSDSF browse EQQMLOG FIND SR02の結果と同一時点の証跡として比較する。
    - C. 保存済みのSR02の出力を再利用する。今回のISPF Special Resource Monitor USERS SR02とSDSF browse EQQMLOG FIND SR02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象SR02についてISPF Special Resource Monitor USERS SR02の応答からALLOCATEDを確認する。SDSF browse EQQMLOG FIND SR02は補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 採用理由: Dは使用操作で ALLOCATED を読みQuantityとAvailabilityの主値として変更前の証跡を保存しSR02に残します。
    動作の背景: 変更前の確認ではイベントログを補助操作としSpecial Resourceの変更対象と非対象の境界をEQQR011Iと対象SR02で照合します。
    各選択肢の検討: 使用操作とイベントログの役割を分けるとA: 先頭行はSR02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で使用操作を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で特殊資源管理に使いません、D: ALLOCATEDと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の特殊資源管理で判定する対象は SR02 です。
    初出用語の定義: 変更前の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR02へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 変更前の確認 SR02**

    - 検証目的: 特殊資源管理のSpecial Resourceについて変更前の証跡を保存し、SR02のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR02を指定し、SR02の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR02
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR02 ADID APP02 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR02を指定し、SR02のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR02
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR02 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR02の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR02 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ALLOCATED が画面・出力に表示されること
    ② ステップ2 の EQQR011I が画面・出力に表示されること
    ③ ステップ3 の QUANTITY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 変更後の確認 SR03 {#c15-i0209}
*分類: 特殊資源管理*  ・  難易度: 中級

変更後の確認では 特殊資源管理 の イベントログ を主操作として SR03 を判定します。反映値と残存値への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR03 に残します。変更後の確認を補助する 資源モニター では QUANTITY を補助値として SR03 へ保存します。主判定の変更後の確認では特殊資源管理の イベントログ から EQQR011I を読み SR03 へ残します。証跡照合の変更後の確認では特殊資源管理の EQQR011I と QUANTITY を SR03 に保存します。記録対応の変更後の確認では特殊資源管理の QuantityとAvailability の証跡へ SR03 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 特殊資源管理 の イベントログ と 資源モニター を組み合わせる際は Special Resource がジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能という仕組みを前提にします。実在装置の状態と特殊資源の論理可用性を混同する危険があります。EQQR011I と QuantityとAvailability を対象 SR03 で確認する組合せはどれですか。

    - A. ISPF EQQMTOPP option 7 SPECRESで周辺状態を押さえる。その後にSDSF browse EQQMLOG FIND SR03でEQQR011Iを確認して変更結果を検証する。 ✅
    - B. Special Resourceの停止または再定義を実施する。その後にSDSF browse EQQMLOG FIND SR03でEQQR011Iを採取する。
    - C. 監査ログと EQQMLOGのMessage IDとADIDを確認する。その値を特殊資源管理のSR03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Special Resourceの反映値と残存値は確認済みとして扱う。さらにISPF Special Resource Monitor USERS SR03のALLOCATEDをEQQR011Iと同種の値として併記する。
    - D. ISPF EQQMTOPP option 7 SPECRESが成功したためSDSF browse EQQMLOG FIND SR03のEQQR011Iも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正答の根拠: Aはイベントログで EQQR011I を読みQuantityとAvailabilityの主値として変更結果を検証しSR03に残します。
    内部の仕組み: 変更後の確認では資源モニターを補助操作としSpecial Resourceの反映値と残存値をQUANTITYと対象SR03で照合します。
    誤答を含む比較: イベントログと資源モニターの役割を分けるとA: 周辺状態の後にEQQR011Iを確認する点でSR03を判定できます、B: 変更前のQuantityとAvailabilityを失う点で資源モニターの範囲を越えます、C: 監査ログと EQQMLOGの値ではEQQR011Iを確認できないうえに追加前提も不正な点でSR03の値を示しません、D: 補助操作の成功ではEQQR011Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の特殊資源管理で判定する対象は SR03 です。
    用語定義: 変更後の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR03へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 変更後の確認 SR03**

    - 検証目的: 特殊資源管理のSpecial Resourceについて変更結果を検証し、SR03のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR03を指定し、SR03のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR03
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR03 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR03の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR03 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR03を指定し、SR03の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR03
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR03 ADID APP03 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQR011I が画面・出力に表示されること
    ② ステップ2 の QUANTITY が画面・出力に表示されること
    ③ ステップ3 の ALLOCATED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 引継ぎ記録 SR09 {#c15-i0210}
*分類: 特殊資源管理*  ・  難易度: 中級

引継ぎ記録では 特殊資源管理 の イベントログ を主操作として SR09 を判定します。次担当者が追跡できる証跡への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR09 に残します。引継ぎ記録を補助する 資源モニター では QUANTITY を補助値として SR09 へ保存します。主判定の引継ぎ記録では特殊資源管理の イベントログ から EQQR011I を読み SR09 へ残します。証跡照合の引継ぎ記録では特殊資源管理の EQQR011I と QUANTITY を SR09 に保存します。記録対応の引継ぎ記録では特殊資源管理の QuantityとAvailability の証跡へ SR09 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 特殊資源管理 の イベントログ と 資源モニター を組み合わせる際は Special Resource がジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能という仕組みを前提にします。実在装置の状態と特殊資源の論理可用性を混同する危険があります。EQQR011I と QuantityとAvailability を対象 SR09 で確認する組合せはどれですか。

    - A. ISPF EQQMTOPP option 7 SPECRESが成功したためSDSF browse EQQMLOG FIND SR09のEQQR011Iも正常だと推定する。主出力は保存しない。
    - B. SDSF browse EQQMLOG FIND SR09を対象名なしで実行する。一覧の先頭行をSR09の結果として記録する。
    - C. 対象名SR09を指定してSDSF browse EQQMLOG FIND SR09を実行する。応答中のEQQR011Iと時刻を保存する。ISPF EQQMTOPP option 7 SPECRESで周辺状態を補完する。 ✅
    - D. 前回保存したSDSF browse EQQMLOG FIND SR09の結果を使う。今回のISPF EQQMTOPP option 7 SPECRESの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 中級

    **解説:** 採用操作の理由: Cはイベントログで EQQR011I を読みQuantityとAvailabilityの主値として再現可能な記録を作成しSR09に残します。
    製品内の仕組み: 引継ぎ記録では資源モニターを補助操作としSpecial Resourceの次担当者が追跡できる証跡をQUANTITYと対象SR09で照合します。
    選択肢別の説明: イベントログと資源モニターの役割を分けるとA: 補助操作の成功ではEQQR011Iを確定できない点でSR09の値を示しません、B: 先頭行はSR09と確定できない点で引継ぎ記録に合いません、C: EQQR011Iと時刻を保存する点でイベントログに合います、D: 採取時刻が異なる点で特殊資源管理に使いません。結論として引継ぎ記録の特殊資源管理で判定する対象は SR09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR09へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 引継ぎ記録 SR09**

    - 検証目的: 特殊資源管理のSpecial Resourceについて再現可能な記録を作成し、SR09のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR09を指定し、SR09のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR09
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR09 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR09の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR09 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR09を指定し、SR09の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR09
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR09 ADID APP09 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQR011I が画面・出力に表示されること
    ② ステップ2 の QUANTITY が画面・出力に表示されること
    ③ ステップ3 の ALLOCATED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 復旧後の確認 SR06 {#c15-i0211}
*分類: 特殊資源管理*  ・  難易度: 中級

復旧後の確認では 特殊資源管理 の イベントログ を主操作として SR06 を判定します。再発していないことを示す値への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR06 に残します。復旧後の確認を補助する 資源モニター では QUANTITY を補助値として SR06 へ保存します。主判定の復旧後の確認では特殊資源管理の イベントログ から EQQR011I を読み SR06 へ残します。証跡照合の復旧後の確認では特殊資源管理の EQQR011I と QUANTITY を SR06 に保存します。記録対応の復旧後の確認では特殊資源管理の QuantityとAvailability の証跡へ SR06 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 特殊資源管理 の イベントログ と 資源モニター を実施し Special Resource の役割を確認します。実在装置の状態と特殊資源の論理可用性を混同する危険があります。対象 SR06 の証跡を取る方法はどれですか。

    - A. 長期計画管理のRun DateとInput Arrivalを確認する。その値を特殊資源管理のSR06にも適用する。
    - B. ISPF EQQMTOPP option 7 SPECRESが成功したためSDSF browse EQQMLOG FIND SR06のEQQR011Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SR06へ引き継げるものとする。Special Resourceの再発していないことを示す値は確認済みとして扱う。さらにISPF Special Resource Monitor USERS SR06のALLOCATEDをEQQR011Iと同種の値として併記する。
    - C. SDSF browse EQQMLOG FIND SR06を対象名なしで実行する。一覧の先頭行をSR06の結果として記録する。
    - D. SDSF browse EQQMLOG FIND SR06でEQQR011Iを取得してからISPF Special Resource Monitor USERS SR06でALLOCATEDを照合する。SR06のQuantityとAvailabilityを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答内容: Dはイベントログで EQQR011I を読みQuantityとAvailabilityの主値として復旧後の安定性を確認しSR06に残します。
    構成上の背景: 復旧後の確認では資源モニターを補助操作としSpecial Resourceの再発していないことを示す値をQUANTITYと対象SR06で照合します。
    候補ごとの理由: イベントログと資源モニターの役割を分けるとA: 長期計画管理の値ではEQQR011Iを確認できない点で資源モニターの範囲を越えます、B: 補助操作の成功ではEQQR011Iを確定できないうえに追加前提も不正な点でSR06の値を示しません、C: 先頭行はSR06と確定できない点で復旧後の確認に合いません、D: EQQR011IとALLOCATEDを順に照合する点でイベントログに合います。結論として復旧後の確認の特殊資源管理で判定する対象は SR06 です。
    初出用語: 復旧後の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR06へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 復旧後の確認 SR06**

    - 検証目的: 特殊資源管理のSpecial Resourceについて復旧後の安定性を確認し、SR06のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR06を指定し、SR06のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR06
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR06 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR06の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR06 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR06を指定し、SR06の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR06
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR06 ADID APP06 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQR011I が画面・出力に表示されること
    ② ステップ2 の QUANTITY が画面・出力に表示されること
    ③ ステップ3 の ALLOCATED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 復旧準備 SR05 {#c15-i0212}
*分類: 特殊資源管理*  ・  難易度: 中級

復旧準備では 特殊資源管理 の 使用操作 を主操作として SR05 を判定します。再開前に必要な整合性への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR05 に残します。復旧準備を補助する イベントログ では EQQR011I を補助値として SR05 へ保存します。主判定の復旧準備では特殊資源管理の 使用操作 から ALLOCATED を読み SR05 へ残します。証跡照合の復旧準備では特殊資源管理の ALLOCATED と EQQR011I を SR05 に保存します。記録対応の復旧準備では特殊資源管理の QuantityとAvailability の証跡へ SR05 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧準備で 特殊資源管理 の 使用操作 と イベントログ を使い 復旧条件を確認 します。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。ALLOCATED を読み対象 SR05 を切り分ける確認方法はどれですか。

    - A. 前回保存したISPF Special Resource Monitor USERS SR05の結果を使う。今回のSDSF browse EQQMLOG FIND SR05の結果と同一時点の証跡として比較する。
    - B. 保存済みのSR05の出力を再利用する。今回のISPF Special Resource Monitor USERS SR05とSDSF browse EQQMLOG FIND SR05は実行済みとして扱う。
    - C. 変更を加えずISPF Special Resource Monitor USERS SR05を実行する。ALLOCATEDを保存する。差分はSDSF browse EQQMLOG FIND SR05の結果と対象名で対応させる。 ✅
    - D. SDSF browse EQQMLOG FIND SR05のEQQR011IをQuantityとAvailabilityの主判定に採用する。ISPF Special Resource Monitor USERS SR05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 中級

    **解説:** 選定理由: Cは使用操作で ALLOCATED を読みQuantityとAvailabilityの主値として復旧条件を確認しSR05に残します。
    処理の仕組み: 復旧準備ではイベントログを補助操作としSpecial Resourceの再開前に必要な整合性をEQQR011Iと対象SR05で照合します。
    選択結果の内訳: 使用操作とイベントログの役割を分けるとA: 採取時刻が異なる点で使用操作を代替しません、B: 過去出力では今回の復旧準備を示せない点で特殊資源管理に使いません、C: 変更前のALLOCATEDを保存する点で正答です、D: EQQR011IはALLOCATEDを代替しないうえに追加前提も不正な点でSR05を採用できません。結論として復旧準備の特殊資源管理で判定する対象は SR05 です。
    用語の説明: 復旧準備で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR05へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 復旧準備 SR05**

    - 検証目的: 特殊資源管理のSpecial Resourceについて復旧条件を確認し、SR05のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR05を指定し、SR05の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR05
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR05 ADID APP05 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR05を指定し、SR05のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR05
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR05 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR05の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR05 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ALLOCATED が画面・出力に表示されること
    ② ステップ2 の EQQR011I が画面・出力に表示されること
    ③ ステップ3 の QUANTITY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 構成監査 SR08 {#c15-i0213}
*分類: 特殊資源管理*  ・  難易度: 中級

構成監査では 特殊資源管理 の 使用操作 を主操作として SR08 を判定します。定義値と稼働値の一致への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR08 に残します。構成監査を補助する イベントログ では EQQR011I を補助値として SR08 へ保存します。主判定の構成監査では特殊資源管理の 使用操作 から ALLOCATED を読み SR08 へ残します。証跡照合の構成監査では特殊資源管理の ALLOCATED と EQQR011I を SR08 に保存します。記録対応の構成監査では特殊資源管理の QuantityとAvailability の証跡へ SR08 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 構成監査で 特殊資源管理 の 使用操作 と イベントログ を照合し 定義値と稼働値の一致 を確かめます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。ALLOCATED を読む前に対象 SR08 へ行う確認はどれですか。

    - A. 保存済みのSR08の出力を再利用する。今回のISPF Special Resource Monitor USERS SR08とSDSF browse EQQMLOG FIND SR08は実行済みとして扱う。
    - B. SDSF browse EQQMLOG FIND SR08の結果だけでは確定しない。ISPF Special Resource Monitor USERS SR08のALLOCATEDを主証跡として構成差分を監査する。 ✅
    - C. SDSF browse EQQMLOG FIND SR08のEQQR011IをQuantityとAvailabilityの主判定に採用する。ISPF Special Resource Monitor USERS SR08の応答は採取対象から外す。
    - D. ISPF EQQMTOPP option 7 SPECRESのQUANTITYをALLOCATEDと同義の成功表示として扱う。ISPF Special Resource Monitor USERS SR08は実行しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 技術上の正答: Bは使用操作で ALLOCATED を読みQuantityとAvailabilityの主値として構成差分を監査しSR08に残します。
    実行時の背景: 構成監査ではイベントログを補助操作としSpecial Resourceの定義値と稼働値の一致をEQQR011Iと対象SR08で照合します。
    四つの候補の理由: 使用操作とイベントログの役割を分けるとA: 過去出力では今回の構成監査を示せない点で特殊資源管理に使いません、B: ALLOCATEDを主証跡として区別する点で正答です、C: EQQR011IはALLOCATEDを代替しない点でSR08を採用できません、D: QUANTITYとALLOCATEDは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の特殊資源管理で判定する対象は SR08 です。
    初出語定義: 構成監査で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR08へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 構成監査 SR08**

    - 検証目的: 特殊資源管理のSpecial Resourceについて構成差分を監査し、SR08のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR08を指定し、SR08の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR08
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR08 ADID APP08 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR08を指定し、SR08のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR08
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR08 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR08の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR08 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ALLOCATED が画面・出力に表示されること
    ② ステップ2 の EQQR011I が画面・出力に表示されること
    ③ ステップ3 の QUANTITY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 通常状態の確認 SR01 {#c15-i0214}
*分類: 特殊資源管理*  ・  難易度: 中級

通常状態の確認では 特殊資源管理 の 資源モニター を主操作として SR01 を判定します。基準値と現在値の差への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR01 に残します。通常状態の確認を補助する 使用操作 では ALLOCATED を補助値として SR01 へ保存します。主判定の通常状態の確認では特殊資源管理の 資源モニター から QUANTITY を読み SR01 へ残します。証跡照合の通常状態の確認では特殊資源管理の QUANTITY と ALLOCATED を SR01 に保存します。記録対応の通常状態の確認では特殊資源管理の QuantityとAvailability の証跡へ SR01 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 特殊資源管理 の 資源モニター と 使用操作 を用い 通常状態を確定 します。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。QUANTITY で対象 SR01 の QuantityとAvailability を再現できる記録はどれですか。

    - A. ISPF Special Resource Monitor USERS SR01のALLOCATEDをQuantityとAvailabilityの主判定に採用する。ISPF EQQMTOPP option 7 SPECRESの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. SDSF browse EQQMLOG FIND SR01のEQQR011IをQUANTITYと同義の成功表示として扱う。ISPF EQQMTOPP option 7 SPECRESは実行しない。
    - C. ISPF EQQMTOPP option 7 SPECRESを先に実行する。対象SR01のQUANTITYをQuantityとAvailabilityとして記録する。続いてISPF Special Resource Monitor USERS SR01で同一対象を照合する。 ✅
    - D. ISPF EQQMTOPP option 7 SPECRESが応答を返した時点で正常とする。応答中のQUANTITYの値は記録しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解の説明: Cは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として通常状態を確定しSR01に残します。
    背景・仕組み: 通常状態の確認では使用操作を補助操作としSpecial Resourceの基準値と現在値の差をALLOCATEDと対象SR01で照合します。
    選択肢の理由: 資源モニターと使用操作の役割を分けるとA: ALLOCATEDはQUANTITYを代替しないうえに追加前提も不正な点でSpecial Resourceに使えません、B: EQQR011IとQUANTITYは確認項目が異なる点でSR01を採用できません、C: QUANTITYを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではQuantityとAvailabilityを判定できない点で一次資料と一致しません。結論として通常状態の確認の特殊資源管理で判定する対象は SR01 です。
    用語の初出定義: 通常状態の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR01へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 通常状態の確認 SR01**

    - 検証目的: 特殊資源管理のSpecial Resourceについて通常状態を確定し、SR01のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR01の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR01 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR01を指定し、SR01の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR01
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR01 ADID APP01 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR01を指定し、SR01のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR01
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR01 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
    ② ステップ2 の ALLOCATED が画面・出力に表示されること
    ③ ステップ3 の EQQR011I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 特殊資源管理 Special Resource 障害切り分け SR04 {#c15-i0215}
*分類: 特殊資源管理*  ・  難易度: 中級

障害切り分けでは 特殊資源管理 の 資源モニター を主操作として SR04 を判定します。最初に失敗した処理への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR04 に残します。障害切り分けを補助する 使用操作 では ALLOCATED を補助値として SR04 へ保存します。主判定の障害切り分けでは特殊資源管理の 資源モニター から QUANTITY を読み SR04 へ残します。証跡照合の障害切り分けでは特殊資源管理の QUANTITY と ALLOCATED を SR04 に保存します。記録対応の障害切り分けでは特殊資源管理の QuantityとAvailability の証跡へ SR04 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 特殊資源管理 の 資源モニター と 使用操作 の役割を分け 最初に失敗した処理 を調べます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。対象 SR04 を誤判定しない進め方はどれですか。

    - A. SDSF browse EQQMLOG FIND SR04のEQQR011IをQUANTITYと同義の成功表示として扱う。ISPF EQQMTOPP option 7 SPECRESは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. ISPF EQQMTOPP option 7 SPECRESの出力でSR04とQUANTITYが同じ応答にあることを確認する。QuantityとAvailabilityをその応答から採取する。 ✅
    - C. ISPF EQQMTOPP option 7 SPECRESが応答を返した時点で正常とする。応答中のQUANTITYの値は記録しない。
    - D. ISPF EQQMTOPP option 7 SPECRESのコマンド文字列だけを記録する。QUANTITYを含む応答行は保存しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Bは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として障害範囲を限定しSR04に残します。
    技術的背景: 障害切り分けでは使用操作を補助操作としSpecial Resourceの最初に失敗した処理をALLOCATEDと対象SR04で照合します。
    四択の評価: 資源モニターと使用操作の役割を分けるとA: EQQR011IとQUANTITYは確認項目が異なるうえに追加前提も不正な点でSR04を採用できません、B: SR04とQUANTITYを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではQuantityとAvailabilityを判定できない点で一次資料と一致しません、D: 入力記録だけではQuantityとAvailabilityを証明できない点でQuantityとAvailabilityを確認できません。結論として障害切り分けの特殊資源管理で判定する対象は SR04 です。
    初出語の意味: 障害切り分けで使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR04へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **特殊資源管理 Special Resource 障害切り分け SR04**

    - 検証目的: 特殊資源管理のSpecial Resourceについて障害範囲を限定し、SR04のQuantityとAvailabilityを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象SR04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR04の資源モニターを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 7 SPECRES
    → Enter を押す
    ```

    画面・出力:
    ```text
    SPECIAL RESOURCE SR04 AVAILABLE YES QUANTITY 2 USED 1
    ```

    画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR04を指定し、SR04の使用操作を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Special Resource Monitor USERS SR04
    → Enter を押す
    ```

    画面・出力:
    ```text
    RESOURCE SR04 ADID APP04 OPNO 020 QUANTITY 1 STATUS ALLOCATED
    ```

    画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR04を指定し、SR04のイベントログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND SR04
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQR011I SPECIAL RESOURCE SR04 AVAILABILITY CHANGED TO YES
    ```

    画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
    ② ステップ2 の ALLOCATED が画面・出力に表示されること
    ③ ステップ3 の EQQR011I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide




## IBM Workload Automation > 現在計画管理

### EQQMLOG ログ確認 依存確認016 {#c15-i0216}
*分類: 現在計画管理*  ・  難易度: 初級

第十六観点 依存確認016 では 現在計画管理 にある EQQMLOG を扱います。第十六観点 対象は controller、tracker、WAPL などのメッセージを確認するログで、Eです。第十六観点 特殊資源の使用量と待ち操作 を採る時点で CHK036 を明記し、変更反映の前提を守ります。第十六観点 後続作業では同じ engine と current plan を見たことを IWA監査036で残します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **EQQMLOG ログ確認 依存確認016**

    - 検証目的: 現在計画管理における EQQMLOG のログ確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CHK036
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQMLOG の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    WAPL batch review
    COMMAND ===> BROWSE EQQYPARM
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQYPARM INIT SUBSYSTEM ZWS1
    EQQMLIB SEQQMSG0
    EQQMLOG IWA.WAPL.036.MLOG
    ```

    画面・出力には EQQYPARM が含まれる。EQQYPARM を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、特殊資源の使用量と待ち操作 と CHK036 の対応を確認する。
    操作（入力）:
    ```text
    WAPL batch submit
    COMMAND ===> SUBMIT IWA.WAPL.CNTL(INIT036)
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQWAPL INIT COMPLETED
    SUBSYSTEM ZWS1
    MESSAGE LOG IWA.WAPL.036.MLOG
    RETURN CODE 0000
    ```

    画面・出力には EQQWAPL が含まれる。EQQWAPL を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    SDSF output browse
    COMMAND ===> FIND DYNLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    OPTIONS DYNLOG(IWA.WAPLLOG)
    DYNAMIC LOG IWA.WAPLLOG.D260715.T0915A.IWAJOB036
    ADVISORY MESSAGES WRITTEN
    ```

    画面・出力には OPTIONS が含まれる。OPTIONS を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQYPARM が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQWAPL が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: OPTIONS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### EQQMLOG 依存関係確認 再実行046 {#c15-i0217}
*分類: 現在計画管理*  ・  難易度: 中級

第四十六観点 EQQMLOG の 再実行046 は IBM Workload Automation の 現在計画管理 に属します。第四十六観点 対象は controller、tracker、WAPL などのメッセージを確認するログで、Eです。第四十六観点 conman または WAPL の結果を使う時は、CHK066 の取得経路を残します。第四十六観点 WAPL を使う場合は subsystem 名を IWA言語066に残します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **EQQMLOG 依存関係確認 再実行046**

    - 検証目的: 現在計画管理における EQQMLOG の依存関係確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CHK066
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQMLOG の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    WAPL batch review
    COMMAND ===> BROWSE EQQYPARM
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQYPARM INIT SUBSYSTEM ZWS1
    EQQMLIB SEQQMSG0
    EQQMLOG IWA.WAPL.066.MLOG
    ```

    画面・出力には EQQYPARM が含まれる。EQQYPARM を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、特殊資源の使用量と待ち操作 と CHK066 の対応を確認する。
    操作（入力）:
    ```text
    WAPL batch submit
    COMMAND ===> SUBMIT IWA.WAPL.CNTL(INIT066)
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQWAPL INIT COMPLETED
    SUBSYSTEM ZWS1
    MESSAGE LOG IWA.WAPL.066.MLOG
    RETURN CODE 0000
    ```

    画面・出力には EQQWAPL が含まれる。EQQWAPL を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    SDSF output browse
    COMMAND ===> FIND DYNLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    OPTIONS DYNLOG(IWA.WAPLLOG)
    DYNAMIC LOG IWA.WAPLLOG.D260715.T0915A.IWAJOB066
    ADVISORY MESSAGES WRITTEN
    ```

    画面・出力には OPTIONS が含まれる。OPTIONS を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQYPARM が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQWAPL が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: OPTIONS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### EQQMLOG 資源制御 ログ採取076 {#c15-i0218}
*分類: 現在計画管理*  ・  難易度: 中級

第七十六観点 ログ採取076 では 現在計画管理 にある EQQMLOG を扱います。第七十六観点 対象は controller、tracker、WAPL などのメッセージを確認するログで、Eです。第七十六観点 特殊資源の使用量と待ち操作 を採る時点で CHK096 を明記し、変更反映の前提を守ります。第七十六観点 後続作業では同じ engine と current plan を見たことを IWA監査096で残します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **EQQMLOG 資源制御 ログ採取076**

    - 検証目的: 現在計画管理における EQQMLOG の資源制御を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CHK096
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQMLOG の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    WAPL batch review
    COMMAND ===> BROWSE EQQYPARM
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQYPARM INIT SUBSYSTEM ZWS1
    EQQMLIB SEQQMSG0
    EQQMLOG IWA.WAPL.096.MLOG
    ```

    画面・出力には EQQYPARM が含まれる。EQQYPARM を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、特殊資源の使用量と待ち操作 と CHK096 の対応を確認する。
    操作（入力）:
    ```text
    WAPL batch submit
    COMMAND ===> SUBMIT IWA.WAPL.CNTL(INIT096)
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQWAPL INIT COMPLETED
    SUBSYSTEM ZWS1
    MESSAGE LOG IWA.WAPL.096.MLOG
    RETURN CODE 0000
    ```

    画面・出力には EQQWAPL が含まれる。EQQWAPL を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    SDSF output browse
    COMMAND ===> FIND DYNLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    OPTIONS DYNLOG(IWA.WAPLLOG)
    DYNAMIC LOG IWA.WAPLLOG.D260715.T0915A.IWAJOB096
    ADVISORY MESSAGES WRITTEN
    ```

    画面・出力には OPTIONS が含まれる。OPTIONS を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQYPARM が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQWAPL が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: OPTIONS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### current plan 定義照合 導入確認031 {#c15-i0219}
*分類: 現在計画管理*  ・  難易度: 中級

第三十一観点 現在計画管理 の 導入確認031 では current plan を点検します。第三十一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第三十一観点 操作番号とジョブ名を PAYROLL051 に結び付け、再表示時の照合点にします。第三十一観点 計画反映後は long-term plan との差を IWA計画051で照合します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **current plan 定義照合 導入確認031**

    - 検証目的: 現在計画管理における current plan の定義照合を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL051
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> LOCATE PAYROLL051
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN OPERATIONS
    ADID PAYROLL051 IADATE 260715 WS CPU07 OPNO 070 JOBNAME IWAJOB051 STATUS READY
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL051 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
    Command ===> S 070
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPJT JOB DETAIL
    APPLICATION PAYROLL051
    WORKSTATION CPU07
    OPERATION 070
    JOBNAME IWAJOB051
    INPUT ARRIVAL 260715 0900
    ```

    画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> REFRESH
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN REFRESHED
    ADID PAYROLL051 OPNO 070 STATUS READY LAST UPDATE 260715 0915
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### current plan 実行監視 再計画091 {#c15-i0220}
*分類: 現在計画管理*  ・  難易度: 上級

第九十一観点 現在計画管理 の 再計画091 では current plan を点検します。第九十一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第九十一観点 操作番号とジョブ名を PAYROLL111 に結び付け、再表示時の照合点にします。第九十一観点 計画反映後は long-term plan との差を IWA計画111で照合します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **current plan 実行監視 再計画091**

    - 検証目的: 現在計画管理における current plan の実行監視を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL111
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> LOCATE PAYROLL111
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN OPERATIONS
    ADID PAYROLL111 IADATE 260715 WS CPU07 OPNO 190 JOBNAME IWAJOB111 STATUS READY
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL111 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
    Command ===> S 190
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPJT JOB DETAIL
    APPLICATION PAYROLL111
    WORKSTATION CPU07
    OPERATION 190
    JOBNAME IWAJOB111
    INPUT ARRIVAL 260715 0900
    ```

    画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> REFRESH
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN REFRESHED
    ADID PAYROLL111 OPNO 190 STATUS READY LAST UPDATE 260715 0915
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### current plan 状態確認 監視001 {#c15-i0221}
*分類: 現在計画管理*  ・  難易度: 初級

第一観点 current plan は IBM Workload Automation の 現在計画管理 で扱う確認点です。第一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第一観点 EQQMLOG の EQQ メッセージ と PAYROLL021 を同じ記録に残し、再実行前の Ready 変更を記録せずに原因追跡できなくなることを管理します。第一観点 確認経路は DWC、ISPF、conman、WAPL の別を IWA記録021に残します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **current plan 状態確認 監視001**

    - 検証目的: 現在計画管理における current plan の状態確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL021
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> LOCATE PAYROLL021
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN OPERATIONS
    ADID PAYROLL021 IADATE 260715 WS CPU01 OPNO 010 JOBNAME IWAJOB021 STATUS READY
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL021 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
    Command ===> S 010
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPJT JOB DETAIL
    APPLICATION PAYROLL021
    WORKSTATION CPU01
    OPERATION 010
    JOBNAME IWAJOB021
    INPUT ARRIVAL 260715 0900
    ```

    画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> REFRESH
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN REFRESHED
    ADID PAYROLL021 OPNO 010 STATUS READY LAST UPDATE 260715 0915
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### current plan 計画反映 資源確認061 {#c15-i0222}
*分類: 現在計画管理*  ・  難易度: 中級

第六十一観点 current plan は IBM Workload Automation の 現在計画管理 で扱う確認点です。第六十一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第六十一観点 EQQMLOG の EQQ メッセージ と PAYROLL081 を同じ記録に残し、ジョブログが JES から purge された後に証跡を取り逃すことを管理します。第六十一観点 確認経路は DWC、ISPF、conman、WAPL の別を IWA記録081に残します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **current plan 計画反映 資源確認061**

    - 検証目的: 現在計画管理における current plan の計画反映を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL081
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> LOCATE PAYROLL081
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN OPERATIONS
    ADID PAYROLL081 IADATE 260715 WS CPU01 OPNO 130 JOBNAME IWAJOB081 STATUS READY
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL081 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
    Command ===> S 130
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPJT JOB DETAIL
    APPLICATION PAYROLL081
    WORKSTATION CPU01
    OPERATION 130
    JOBNAME IWAJOB081
    INPUT ARRIVAL 260715 0900
    ```

    画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
    Command ===> REFRESH
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMOPLT CURRENT PLAN REFRESHED
    ADID PAYROLL081 OPNO 130 STATUS READY LAST UPDATE 260715 0915
    ```

    画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan ログとの照合 CP07 {#c15-i0223}
*分類: 現在計画管理*  ・  難易度: 初級

ログとの照合では 現在計画管理 の 計画メニュー を主操作として CP07 を判定します。時刻と対象識別子への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP07 に残します。ログとの照合を補助する 操作一覧 では OPNO を補助値として CP07 へ保存します。主判定のログとの照合では現在計画管理の 計画メニュー から EQQMTOPP を読み CP07 へ残します。証跡照合のログとの照合では現在計画管理の EQQMTOPP と OPNO を CP07 に保存します。記録対応のログとの照合では現在計画管理の ADIDとOperation Status の証跡へ CP07 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** ログとの照合で 現在計画管理 の 計画メニュー と 操作一覧 を組み合わせる際は Current Plan が実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータという仕組みを前提にします。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMTOPP と ADIDとOperation Status を対象 CP07 で確認する組合せはどれですか。

    - A. ISPF EQQMTOPP option 2 LISTが応答を返した時点で正常とする。応答中のEQQMTOPPの値は記録しない。EQQMLOGをEQQMTOPPと同じ判定値とみなし対象CP07の主証跡にする。Current Planの時刻と対象識別子は確認済みとして扱う。さらにSDSF browse EQQMLOG FIND APP07のEQQMLOGをEQQMTOPPと同種の値として併記する。
    - B. ISPF EQQMTOPP option 2 LISTのコマンド文字列だけを記録する。EQQMTOPPを含む応答行は保存しない。
    - C. EQQMTOPPを含む計画メニューの応答行を保存する。その応答を得るためISPF EQQMTOPP option 2 LISTを使用する。対象CP07のADIDとOperation Statusとして記録する。 ✅
    - D. Current Planの停止または再定義を実施する。その後にISPF EQQMTOPP option 2 LISTでEQQMTOPPを採取する。

    正解: **C** ／ 難易度: 初級

    **解説:** 適切な判定: Cは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として操作とログを対応しCP07に残します。
    機能の仕組み: ログとの照合では操作一覧を補助操作としCurrent Planの時刻と対象識別子をOPNOと対象CP07で照合します。
    各候補の評価: 計画メニューと操作一覧の役割を分けるとA: 応答の有無だけではADIDとOperation Statusを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではADIDとOperation Statusを証明できない点で一次資料と一致しません、C: EQQMTOPPの実値を対象別に残す点でCP07を判定できます、D: 変更前のADIDとOperation Statusを失う点で操作一覧の範囲を越えます。結論としてログとの照合の現在計画管理で判定する対象は CP07 です。
    用語の定義: ログとの照合で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP07へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan ログとの照合 CP07**

    - 検証目的: 現在計画管理のCurrent Planについて操作とログを対応し、CP07のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP07の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP07 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP07の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP07 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB07 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB07 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP07を指定し、CP07の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP07
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP07 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の EQQMLOG が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 代替経路の確認 CP10 {#c15-i0224}
*分類: 現在計画管理*  ・  難易度: 初級

代替経路の確認では 現在計画管理 の 計画メニュー を主操作として CP10 を判定します。主経路との役割差への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP10 に残します。代替経路の確認を補助する 操作一覧 では OPNO を補助値として CP10 へ保存します。主判定の代替経路の確認では現在計画管理の 計画メニュー から EQQMTOPP を読み CP10 へ残します。証跡照合の代替経路の確認では現在計画管理の EQQMTOPP と OPNO を CP10 に保存します。記録対応の代替経路の確認では現在計画管理の ADIDとOperation Status の証跡へ CP10 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 現在計画管理 の 計画メニュー と 操作一覧 を実施し Current Plan の役割を確認します。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP10 の証跡を取る方法はどれですか。

    - A. ISPF EQQMTOPP option 2 LISTのコマンド文字列だけを記録する。EQQMTOPPを含む応答行は保存しない。
    - B. ISPF EQQMTOPP option 2 LISTとISPF EQQMTOPP option 3 OPERATIONSの対象名をそろえる。前者のEQQMTOPPをADIDとOperation Statusの判定値として採用する。 ✅
    - C. Current Planの停止または再定義を実施する。その後にISPF EQQMTOPP option 2 LISTでEQQMTOPPを採取する。
    - D. ISPF パネル運用のPanel IDとOptionを確認する。その値を現在計画管理のCP10にも適用する。

    正解: **B** ／ 難易度: 初級

    **解説:** 正しい判定結果: Bは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として代替手段の成立を確認しCP10に残します。
    運用上の背景: 代替経路の確認では操作一覧を補助操作としCurrent Planの主経路との役割差をOPNOと対象CP10で照合します。
    候補別の検討: 計画メニューと操作一覧の役割を分けるとA: 入力記録だけではADIDとOperation Statusを証明できない点で一次資料と一致しません、B: 同じ対象名のEQQMTOPPを採用する点でCP10を判定できます、C: 変更前のADIDとOperation Statusを失う点で操作一覧の範囲を越えます、D: ISPF パネル運用の値ではEQQMTOPPを確認できない点でCP10の値を示しません。結論として代替経路の確認の現在計画管理で判定する対象は CP10 です。
    重要用語の定義: 代替経路の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP10へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 代替経路の確認 CP10**

    - 検証目的: 現在計画管理のCurrent Planについて代替手段の成立を確認し、CP10のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP10の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP10 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP10の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP10 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB10 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB10 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP10を指定し、CP10の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP10
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP10 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の EQQMLOG が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 変更前の確認 CP02 {#c15-i0225}
*分類: 現在計画管理*  ・  難易度: 初級

変更前の確認では 現在計画管理 の 操作一覧 を主操作として CP02 を判定します。変更対象と非対象の境界への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP02 に残します。変更前の確認を補助する 計画ログ では EQQMLOG を補助値として CP02 へ保存します。主判定の変更前の確認では現在計画管理の 操作一覧 から OPNO を読み CP02 へ残します。証跡照合の変更前の確認では現在計画管理の OPNO と EQQMLOG を CP02 に保存します。記録対応の変更前の確認では現在計画管理の ADIDとOperation Status の証跡へ CP02 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 現在計画管理 の 操作一覧 と 計画ログ の役割を分け 変更対象と非対象の境界 を調べます。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP02 を誤判定しない進め方はどれですか。

    - A. ISPF EQQMTOPP option 3 OPERATIONSを対象名なしで実行する。一覧の先頭行をCP02の結果として記録する。
    - B. 対象CP02についてISPF EQQMTOPP option 3 OPERATIONSの応答からOPNOを確認する。SDSF browse EQQMLOG FIND APP02は補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したISPF EQQMTOPP option 3 OPERATIONSの結果を使う。今回のSDSF browse EQQMLOG FIND APP02の結果と同一時点の証跡として比較する。
    - D. 保存済みのCP02の出力を再利用する。今回のISPF EQQMTOPP option 3 OPERATIONSとSDSF browse EQQMLOG FIND APP02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 初級

    **解説:** 採用理由: Bは操作一覧で OPNO を読みADIDとOperation Statusの主値として変更前の証跡を保存しCP02に残します。
    動作の背景: 変更前の確認では計画ログを補助操作としCurrent Planの変更対象と非対象の境界をEQQMLOGと対象CP02で照合します。
    各選択肢の検討: 操作一覧と計画ログの役割を分けるとA: 先頭行はCP02と確定できない点で変更前の確認に合いません、B: OPNOと補助証跡の時刻を合わせる点で操作一覧に合います、C: 採取時刻が異なる点で現在計画管理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でCurrent Planに使えません。結論として変更前の確認の現在計画管理で判定する対象は CP02 です。
    初出用語の定義: 変更前の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP02へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 変更前の確認 CP02**

    - 検証目的: 現在計画管理のCurrent Planについて変更前の証跡を保存し、CP02のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP02の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP02 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB02 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB02 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP02を指定し、CP02の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP02
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP02 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP02の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP02 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
    ② ステップ2 の EQQMLOG が画面・出力に表示されること
    ③ ステップ3 の EQQMTOPP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 変更後の確認 CP03 {#c15-i0226}
*分類: 現在計画管理*  ・  難易度: 初級

変更後の確認では 現在計画管理 の 計画ログ を主操作として CP03 を判定します。反映値と残存値への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP03 に残します。変更後の確認を補助する 計画メニュー では EQQMTOPP を補助値として CP03 へ保存します。主判定の変更後の確認では現在計画管理の 計画ログ から EQQMLOG を読み CP03 へ残します。証跡照合の変更後の確認では現在計画管理の EQQMLOG と EQQMTOPP を CP03 に保存します。記録対応の変更後の確認では現在計画管理の ADIDとOperation Status の証跡へ CP03 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 現在計画管理 の 計画ログ と 計画メニュー を使い 変更結果を検証 します。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMLOG を読み対象 CP03 を切り分ける確認方法はどれですか。

    - A. Current Planの停止または再定義を実施する。その後にSDSF browse EQQMLOG FIND APP03でEQQMLOGを採取する。
    - B. ワークステーション管理のWSIDとOpen Intervalを確認する。その値を現在計画管理のCP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Current Planの反映値と残存値は確認済みとして扱う。さらにISPF EQQMTOPP option 3 OPERATIONSのOPNOをEQQMLOGと同種の値として併記する。
    - C. ISPF EQQMTOPP option 2 LISTで周辺状態を押さえる。その後にSDSF browse EQQMLOG FIND APP03でEQQMLOGを確認して変更結果を検証する。 ✅
    - D. ISPF EQQMTOPP option 2 LISTが成功したためSDSF browse EQQMLOG FIND APP03のEQQMLOGも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 初級

    **解説:** 正答の根拠: Cは計画ログで EQQMLOG を読みADIDとOperation Statusの主値として変更結果を検証しCP03に残します。
    内部の仕組み: 変更後の確認では計画メニューを補助操作としCurrent Planの反映値と残存値をEQQMTOPPと対象CP03で照合します。
    誤答を含む比較: 計画ログと計画メニューの役割を分けるとA: 変更前のADIDとOperation Statusを失う点でADIDとOperation Statusを確認できません、B: ワークステーション管理の値ではEQQMLOGを確認できないうえに追加前提も不正な点で計画メニューの範囲を越えます、C: 周辺状態の後にEQQMLOGを確認する点で現在値を示します、D: 補助操作の成功ではEQQMLOGを確定できない点で変更後の確認に合いません。結論として変更後の確認の現在計画管理で判定する対象は CP03 です。
    用語定義: 変更後の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP03へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 変更後の確認 CP03**

    - 検証目的: 現在計画管理のCurrent Planについて変更結果を検証し、CP03のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP03を指定し、CP03の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP03
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP03 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP03の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP03 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP03の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP03 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB03 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB03 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMLOG が画面・出力に表示されること
    ② ステップ2 の EQQMTOPP が画面・出力に表示されること
    ③ ステップ3 の OPNO が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 引継ぎ記録 CP09 {#c15-i0227}
*分類: 現在計画管理*  ・  難易度: 初級

引継ぎ記録では 現在計画管理 の 計画ログ を主操作として CP09 を判定します。次担当者が追跡できる証跡への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP09 に残します。引継ぎ記録を補助する 計画メニュー では EQQMTOPP を補助値として CP09 へ保存します。主判定の引継ぎ記録では現在計画管理の 計画ログ から EQQMLOG を読み CP09 へ残します。証跡照合の引継ぎ記録では現在計画管理の EQQMLOG と EQQMTOPP を CP09 に保存します。記録対応の引継ぎ記録では現在計画管理の ADIDとOperation Status の証跡へ CP09 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 現在計画管理 の 計画ログ と 計画メニュー を使い 再現可能な記録を作成 します。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMLOG を読み対象 CP09 を切り分ける確認方法はどれですか。

    - A. 対象名CP09を指定してSDSF browse EQQMLOG FIND APP09を実行する。応答中のEQQMLOGと時刻を保存する。ISPF EQQMTOPP option 2 LISTで周辺状態を補完する。 ✅
    - B. ISPF EQQMTOPP option 2 LISTが成功したためSDSF browse EQQMLOG FIND APP09のEQQMLOGも正常だと推定する。主出力は保存しない。
    - C. SDSF browse EQQMLOG FIND APP09を対象名なしで実行する。一覧の先頭行をCP09の結果として記録する。
    - D. 前回保存したSDSF browse EQQMLOG FIND APP09の結果を使う。今回のISPF EQQMTOPP option 2 LISTの結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 初級

    **解説:** 採用操作の理由: Aは計画ログで EQQMLOG を読みADIDとOperation Statusの主値として再現可能な記録を作成しCP09に残します。
    製品内の仕組み: 引継ぎ記録では計画メニューを補助操作としCurrent Planの次担当者が追跡できる証跡をEQQMTOPPと対象CP09で照合します。
    選択肢別の説明: 計画ログと計画メニューの役割を分けるとA: EQQMLOGと時刻を保存する点で現在値を示します、B: 補助操作の成功ではEQQMLOGを確定できない点で引継ぎ記録に合いません、C: 先頭行はCP09と確定できない点で計画ログを代替しません、D: 採取時刻が異なる点で現在計画管理に使いません。結論として引継ぎ記録の現在計画管理で判定する対象は CP09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP09へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 引継ぎ記録 CP09**

    - 検証目的: 現在計画管理のCurrent Planについて再現可能な記録を作成し、CP09のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP09を指定し、CP09の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP09
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP09 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP09の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP09 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP09の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP09 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB09 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB09 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMLOG が画面・出力に表示されること
    ② ステップ2 の EQQMTOPP が画面・出力に表示されること
    ③ ステップ3 の OPNO が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 復旧後の確認 CP06 {#c15-i0228}
*分類: 現在計画管理*  ・  難易度: 初級

復旧後の確認では 現在計画管理 の 計画ログ を主操作として CP06 を判定します。再発していないことを示す値への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP06 に残します。復旧後の確認を補助する 計画メニュー では EQQMTOPP を補助値として CP06 へ保存します。主判定の復旧後の確認では現在計画管理の 計画ログ から EQQMLOG を読み CP06 へ残します。証跡照合の復旧後の確認では現在計画管理の EQQMLOG と EQQMTOPP を CP06 に保存します。記録対応の復旧後の確認では現在計画管理の ADIDとOperation Status の証跡へ CP06 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 現在計画管理 の 計画ログ と 計画メニュー を照合し 再発していないことを示す値 を確かめます。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMLOG を読む前に対象 CP06 へ行う確認はどれですか。

    - A. ジョブ監視のStatusとJob IDを確認する。その値を現在計画管理のCP06にも適用する。
    - B. SDSF browse EQQMLOG FIND APP06でEQQMLOGを取得してからISPF EQQMTOPP option 3 OPERATIONSでOPNOを照合する。CP06のADIDとOperation Statusを両出力から確定する。 ✅
    - C. ISPF EQQMTOPP option 2 LISTが成功したためSDSF browse EQQMLOG FIND APP06のEQQMLOGも正常だと推定する。主出力は保存しない。別資源で得た状態を対象CP06へ引き継げるものとする。Current Planの再発していないことを示す値は確認済みとして扱う。さらにISPF EQQMTOPP option 3 OPERATIONSのOPNOをEQQMLOGと同種の値として併記する。
    - D. SDSF browse EQQMLOG FIND APP06を対象名なしで実行する。一覧の先頭行をCP06の結果として記録する。

    正解: **B** ／ 難易度: 初級

    **解説:** 正答内容: Bは計画ログで EQQMLOG を読みADIDとOperation Statusの主値として復旧後の安定性を確認しCP06に残します。
    構成上の背景: 復旧後の確認では計画メニューを補助操作としCurrent Planの再発していないことを示す値をEQQMTOPPと対象CP06で照合します。
    候補ごとの理由: 計画ログと計画メニューの役割を分けるとA: ジョブ監視の値ではEQQMLOGを確認できない点で計画メニューの範囲を越えます、B: EQQMLOGとOPNOを順に照合する点で現在値を示します、C: 補助操作の成功ではEQQMLOGを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はCP06と確定できない点で計画ログを代替しません。結論として復旧後の確認の現在計画管理で判定する対象は CP06 です。
    初出用語: 復旧後の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP06へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 復旧後の確認 CP06**

    - 検証目的: 現在計画管理のCurrent Planについて復旧後の安定性を確認し、CP06のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP06を指定し、CP06の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP06
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP06 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP06の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP06 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP06の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP06 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB06 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB06 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMLOG が画面・出力に表示されること
    ② ステップ2 の EQQMTOPP が画面・出力に表示されること
    ③ ステップ3 の OPNO が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 復旧準備 CP05 {#c15-i0229}
*分類: 現在計画管理*  ・  難易度: 初級

復旧準備では 現在計画管理 の 操作一覧 を主操作として CP05 を判定します。再開前に必要な整合性への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP05 に残します。復旧準備を補助する 計画ログ では EQQMLOG を補助値として CP05 へ保存します。主判定の復旧準備では現在計画管理の 操作一覧 から OPNO を読み CP05 へ残します。証跡照合の復旧準備では現在計画管理の OPNO と EQQMLOG を CP05 に保存します。記録対応の復旧準備では現在計画管理の ADIDとOperation Status の証跡へ CP05 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧準備で 現在計画管理 の 操作一覧 と 計画ログ を用い 復旧条件を確認 します。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。OPNO で対象 CP05 の ADIDとOperation Status を再現できる記録はどれですか。

    - A. 変更を加えずISPF EQQMTOPP option 3 OPERATIONSを実行する。OPNOを保存する。差分はSDSF browse EQQMLOG FIND APP05の結果と対象名で対応させる。 ✅
    - B. 前回保存したISPF EQQMTOPP option 3 OPERATIONSの結果を使う。今回のSDSF browse EQQMLOG FIND APP05の結果と同一時点の証跡として比較する。
    - C. 保存済みのCP05の出力を再利用する。今回のISPF EQQMTOPP option 3 OPERATIONSとSDSF browse EQQMLOG FIND APP05は実行済みとして扱う。
    - D. SDSF browse EQQMLOG FIND APP05のEQQMLOGをADIDとOperation Statusの主判定に採用する。ISPF EQQMTOPP option 3 OPERATIONSの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 初級

    **解説:** 選定理由: Aは操作一覧で OPNO を読みADIDとOperation Statusの主値として復旧条件を確認しCP05に残します。
    処理の仕組み: 復旧準備では計画ログを補助操作としCurrent Planの再開前に必要な整合性をEQQMLOGと対象CP05で照合します。
    選択結果の内訳: 操作一覧と計画ログの役割を分けるとA: 変更前のOPNOを保存する点で操作一覧に合います、B: 採取時刻が異なる点で現在計画管理に使いません、C: 過去出力では今回の復旧準備を示せない点でCurrent Planに使えません、D: EQQMLOGはOPNOを代替しないうえに追加前提も不正な点でCP05を採用できません。結論として復旧準備の現在計画管理で判定する対象は CP05 です。
    用語の説明: 復旧準備で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP05へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 復旧準備 CP05**

    - 検証目的: 現在計画管理のCurrent Planについて復旧条件を確認し、CP05のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP05の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP05 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB05 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB05 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP05を指定し、CP05の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP05
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP05 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP05の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP05 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
    ② ステップ2 の EQQMLOG が画面・出力に表示されること
    ③ ステップ3 の EQQMTOPP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 構成監査 CP08 {#c15-i0230}
*分類: 現在計画管理*  ・  難易度: 初級

構成監査では 現在計画管理 の 操作一覧 を主操作として CP08 を判定します。定義値と稼働値の一致への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP08 に残します。構成監査を補助する 計画ログ では EQQMLOG を補助値として CP08 へ保存します。主判定の構成監査では現在計画管理の 操作一覧 から OPNO を読み CP08 へ残します。証跡照合の構成監査では現在計画管理の OPNO と EQQMLOG を CP08 に保存します。記録対応の構成監査では現在計画管理の ADIDとOperation Status の証跡へ CP08 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 構成監査で 現在計画管理 の 操作一覧 と 計画ログ の役割を分け 定義値と稼働値の一致 を調べます。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP08 を誤判定しない進め方はどれですか。

    - A. 保存済みのCP08の出力を再利用する。今回のISPF EQQMTOPP option 3 OPERATIONSとSDSF browse EQQMLOG FIND APP08は実行済みとして扱う。
    - B. SDSF browse EQQMLOG FIND APP08のEQQMLOGをADIDとOperation Statusの主判定に採用する。ISPF EQQMTOPP option 3 OPERATIONSの応答は採取対象から外す。
    - C. ISPF EQQMTOPP option 2 LISTのEQQMTOPPをOPNOと同義の成功表示として扱う。ISPF EQQMTOPP option 3 OPERATIONSは実行しない。
    - D. SDSF browse EQQMLOG FIND APP08の結果だけでは確定しない。ISPF EQQMTOPP option 3 OPERATIONSのOPNOを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 技術上の正答: Dは操作一覧で OPNO を読みADIDとOperation Statusの主値として構成差分を監査しCP08に残します。
    実行時の背景: 構成監査では計画ログを補助操作としCurrent Planの定義値と稼働値の一致をEQQMLOGと対象CP08で照合します。
    四つの候補の理由: 操作一覧と計画ログの役割を分けるとA: 過去出力では今回の構成監査を示せない点で現在計画管理に使いません、B: EQQMLOGはOPNOを代替しない点でCurrent Planに使えません、C: EQQMTOPPとOPNOは確認項目が異なる点でCP08を採用できません、D: OPNOを主証跡として区別する点で主証跡になります。結論として構成監査の現在計画管理で判定する対象は CP08 です。
    初出語定義: 構成監査で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP08へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 構成監査 CP08**

    - 検証目的: 現在計画管理のCurrent Planについて構成差分を監査し、CP08のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP08の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP08 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB08 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB08 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP08を指定し、CP08の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP08
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP08 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP08の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP08 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
    ② ステップ2 の EQQMLOG が画面・出力に表示されること
    ③ ステップ3 の EQQMTOPP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 通常状態の確認 CP01 {#c15-i0231}
*分類: 現在計画管理*  ・  難易度: 初級

通常状態の確認では 現在計画管理 の 計画メニュー を主操作として CP01 を判定します。基準値と現在値の差への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP01 に残します。通常状態の確認を補助する 操作一覧 では OPNO を補助値として CP01 へ保存します。主判定の通常状態の確認では現在計画管理の 計画メニュー から EQQMTOPP を読み CP01 へ残します。証跡照合の通常状態の確認では現在計画管理の EQQMTOPP と OPNO を CP01 に保存します。記録対応の通常状態の確認では現在計画管理の ADIDとOperation Status の証跡へ CP01 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 現在計画管理 の 計画メニュー と 操作一覧 を組み合わせる際は Current Plan が実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータという仕組みを前提にします。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMTOPP と ADIDとOperation Status を対象 CP01 で確認する組合せはどれですか。

    - A. ISPF EQQMTOPP option 2 LISTを先に実行する。対象CP01のEQQMTOPPをADIDとOperation Statusとして記録する。続いてISPF EQQMTOPP option 3 OPERATIONSで同一対象を照合する。 ✅
    - B. ISPF EQQMTOPP option 3 OPERATIONSのOPNOをADIDとOperation Statusの主判定に採用する。ISPF EQQMTOPP option 2 LISTの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. SDSF browse EQQMLOG FIND APP01のEQQMLOGをEQQMTOPPと同義の成功表示として扱う。ISPF EQQMTOPP option 2 LISTは実行しない。
    - D. ISPF EQQMTOPP option 2 LISTが応答を返した時点で正常とする。応答中のEQQMTOPPの値は記録しない。

    正解: **A** ／ 難易度: 初級

    **解説:** 正解の説明: Aは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として通常状態を確定しCP01に残します。
    背景・仕組み: 通常状態の確認では操作一覧を補助操作としCurrent Planの基準値と現在値の差をOPNOと対象CP01で照合します。
    選択肢の理由: 計画メニューと操作一覧の役割を分けるとA: EQQMTOPPを主値として補助結果と照合する点で正答です、B: OPNOはEQQMTOPPを代替しないうえに追加前提も不正な点でCP01を採用できません、C: EQQMLOGとEQQMTOPPは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではADIDとOperation Statusを判定できない点で一次資料と一致しません。結論として通常状態の確認の現在計画管理で判定する対象は CP01 です。
    用語の初出定義: 通常状態の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP01へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 通常状態の確認 CP01**

    - 検証目的: 現在計画管理のCurrent Planについて通常状態を確定し、CP01のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP01の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP01 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP01の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP01 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB01 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB01 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP01を指定し、CP01の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP01
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP01 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の EQQMLOG が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 現在計画管理 Current Plan 障害切り分け CP04 {#c15-i0232}
*分類: 現在計画管理*  ・  難易度: 初級

障害切り分けでは 現在計画管理 の 計画メニュー を主操作として CP04 を判定します。最初に失敗した処理への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP04 に残します。障害切り分けを補助する 操作一覧 では OPNO を補助値として CP04 へ保存します。主判定の障害切り分けでは現在計画管理の 計画メニュー から EQQMTOPP を読み CP04 へ残します。証跡照合の障害切り分けでは現在計画管理の EQQMTOPP と OPNO を CP04 に保存します。記録対応の障害切り分けでは現在計画管理の ADIDとOperation Status の証跡へ CP04 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 現在計画管理 の 計画メニュー と 操作一覧 を実施し Current Plan の役割を確認します。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP04 の証跡を取る方法はどれですか。

    - A. SDSF browse EQQMLOG FIND APP04のEQQMLOGをEQQMTOPPと同義の成功表示として扱う。ISPF EQQMTOPP option 2 LISTは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. ISPF EQQMTOPP option 2 LISTが応答を返した時点で正常とする。応答中のEQQMTOPPの値は記録しない。
    - C. ISPF EQQMTOPP option 2 LISTのコマンド文字列だけを記録する。EQQMTOPPを含む応答行は保存しない。
    - D. ISPF EQQMTOPP option 2 LISTの出力でCP04とEQQMTOPPが同じ応答にあることを確認する。ADIDとOperation Statusをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正しい操作の説明: Dは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として障害範囲を限定しCP04に残します。
    技術的背景: 障害切り分けでは操作一覧を補助操作としCurrent Planの最初に失敗した処理をOPNOと対象CP04で照合します。
    四択の評価: 計画メニューと操作一覧の役割を分けるとA: EQQMLOGとEQQMTOPPは確認項目が異なるうえに追加前提も不正な点でCP04を採用できません、B: 応答の有無だけではADIDとOperation Statusを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではADIDとOperation Statusを証明できない点で一次資料と一致しません、D: CP04とEQQMTOPPを同じ応答で結ぶ点でCP04を判定できます。結論として障害切り分けの現在計画管理で判定する対象は CP04 です。
    初出語の意味: 障害切り分けで使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP04へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **現在計画管理 Current Plan 障害切り分け CP04**

    - 検証目的: 現在計画管理のCurrent Planについて障害範囲を限定し、CP04のADIDとOperation Statusを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象CP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP04の計画メニューを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 2 LIST
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMTOPP - MODIFYING THE CURRENT PLAN
    2 LIST - List existing occurrences for further processing
    Application ID APP04 Input Arrival 260715 1400 Status Started
    ```

    画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP04の操作一覧を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF EQQMTOPP option 3 OPERATIONS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADID APP04 IA 260715 1400
    OPNO 010 WS CPU1 JOBNAME JOB04 STATUS C
    OPNO 020 WS CPU1 JOBNAME JOBB04 STATUS R
    ```

    画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP04を指定し、CP04の計画ログを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQMLOG FIND APP04
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG CURRENT PLAN OCCURRENCE APP04 IA 260715 1400 UPDATED
    ```

    画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の EQQMLOG が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide




## IBM Workload Automation > 監査

### AUDIT 初期化ステートメント {#c15-i0233}
*分類: 監査*  ・  難易度: 中級

IBM Workload Automation の 監査で扱うAUDIT 初期化ステートメントは、Z Workload Scheduler のファイル変更を監査ログに残すための設定です。どのファイルのどのアクセスを記録するかを指定できます。JCL やスケジュール定義の変更管理では監査対象を確認します

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 監査確認の初期化ステートメントで作業スケジューラーの運用確認を行います。AUDIT 初期化ステートメントの根拠にできる作業はどれですか。

    - A. IBM Workload Automationと無関係な一覧で監査確認の初期化ステートメントを確認した扱いにする。
    - B. EQQZ045I の有無を確認せず監査確認の初期化ステートメントを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 ✅
    - D. AUDIT 初期化ステートメントの属性行を読まず監査確認の初期化ステートメントの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では AUDIT 初期化ステートメント は「IBM Workload Automationで AUDIT 初期化ステートメントの扱いを記録する監査確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では AUDIT 初期化ステートメントの表示結果と EQQZ045I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では AUDIT 初期化ステートメントの使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **AUDIT 初期化ステートメント**

    - 検証目的: 監査確認の初期化ステートメントについて、IBM Workload Automation の 監査で扱う AUDIT 初期化ステートメントは、Z Workload Scheduler のファイル変更を監査ログに残すたに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、監査確認の初期化ステートメントの確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にAUDIT 初期化ステートメントを指定し、OSKB010019の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND AUDIT 初期化ステートメント
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM AUDIT 初期化ステートメント
    CASE OSKB010019
    SOURCE IBM Workload Automation
    ```

    AUDIT 初期化ステートメントとOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010019を同じ出力で読み、監査確認の初期化ステートメントの根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010019
    COMMAND ===> OPSTAT
    OPERATION OSKB010019 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の AUDIT 初期化ステートメント と OSKB010019 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler




## IBM Workload Automation > 監査ログと EQQMLOG

### agent for z/OS system command 変更反映 資源確認029 {#c15-i0234}
*分類: 監査ログと EQQMLOG*  ・  難易度: 中級

第二十九観点 z/OS agent command は IBM Workload Automation の 監査ログと EQQMLOG で扱う確認点です。第二十九観点 対象は z/OS system command で agent for z/OS の staです。第二十九観点 採取値 EQQ038 を計画表とログの両方で読み、採取時刻をそろえます。第二十九観点 採取後は DWC 表示と ISPF 表示の差を IWA比較049に分けます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **agent for z/OS system command 変更反映 資源確認029**

    - 検証目的: 監査ログと EQQMLOGにおける agent for z/OS system command の変更反映を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ038
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、agent for z/OS system command の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /S EQQTRK
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQFSW1I WRITER TASK INITIALIZED FOR CPU05
    EQQMLOG 049 TRACKER START CHECK
    ```

    画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ038 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQFCC1I
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
    TRACKER CPU05 CONNECTED TO CONTROLLER ZWS1
    ```

    画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQTRK,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
    TRACKER CPU05 EVENT QUEUE NORMAL
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### agent for z/OS system command 状態確認 監視089 {#c15-i0235}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

第八十九観点 z/OS agent command は IBM Workload Automation の 監査ログと EQQMLOG で扱う確認点です。第八十九観点 対象は z/OS system command で agent for z/OS の staです。第八十九観点 採取値 EQQ018 を計画表とログの両方で読み、採取時刻をそろえます。第八十九観点 採取後は DWC 表示と ISPF 表示の差を IWA比較109に分けます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **agent for z/OS system command 状態確認 監視089**

    - 検証目的: 監査ログと EQQMLOGにおける agent for z/OS system command の状態確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ018
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、agent for z/OS system command の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /S EQQTRK
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQFSW1I WRITER TASK INITIALIZED FOR CPU05
    EQQMLOG 109 TRACKER START CHECK
    ```

    画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ018 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQFCC1I
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
    TRACKER CPU05 CONNECTED TO CONTROLLER ZWS1
    ```

    画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQTRK,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
    TRACKER CPU05 EVENT QUEUE NORMAL
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### agent for z/OS system command 障害切分け 再計画059 {#c15-i0236}
*分類: 監査ログと EQQMLOG*  ・  難易度: 中級

第五十九観点 監査ログと EQQMLOG の 再計画059 では z/OS agent command を点検します。第五十九観点 対象は z/OS system command で agent for z/OS の staです。第五十九観点 待ち状態がある時は current plan の ADID/IADATE/OPNO と EQQ068 の時刻差を確認します。第五十九観点 ジョブログは JES の purge 前に IWAログ079へ転記します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **agent for z/OS system command 障害切分け 再計画059**

    - 検証目的: 監査ログと EQQMLOGにおける agent for z/OS system command の障害切分けを机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ068
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、agent for z/OS system command の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /S EQQTRK
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQFSW1I WRITER TASK INITIALIZED FOR CPU11
    EQQMLOG 079 TRACKER START CHECK
    ```

    画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ068 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQFCC1I
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
    TRACKER CPU11 CONNECTED TO CONTROLLER ZWS1
    ```

    画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQTRK,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
    TRACKER CPU11 EVENT QUEUE NORMAL
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### run cycle ログ確認 照合074 {#c15-i0237}
*分類: 監査ログと EQQMLOG*  ・  難易度: 中級

第七十四観点 run cycle の 照合074 は IBM Workload Automation の 監査ログと EQQMLOG に属します。第七十四観点 対象は アプリケーションをいつ計画へ載せるかを決める周期条件で、カレンダーと入力到着時刻と合です。第七十四観点 IWA094 の確認では conman showjobs の Job Stream と Job 状態 を起点に、CPU02 と対象 engine を照合します。第七十四観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡094として整理します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **run cycle ログ確認 照合074**

    - 検証目的: 監査ログと EQQMLOGにおける run cycle のログ確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU02
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、run cycle の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman showjobs PAYROLL094.IWAJOB094
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Stream: PAYROLL094
    Job: IWAJOB094
    Workstation: CPU02
    Status: SUCC
    Return Code: 0
    ```

    画面・出力には Stream が含まれる。Stream を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU02 の対応を確認する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman submit sched PAYROLL094
    → Enter を押す
    ```

    画面・出力:
    ```text
    Schedule PAYROLL094 submitted
    Instance 2607150900 queued for workstation CPU02
    ```

    画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman showjobs PAYROLL094.IWAJOB094
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Stream: PAYROLL094
    Job: IWAJOB094
    Status: READY
    Dependencies: satisfied
    ```

    画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### run cycle 再実行判断 ログ採取044 {#c15-i0238}
*分類: 監査ログと EQQMLOG*  ・  難易度: 中級

第四十四観点 ログ採取044 では 監査ログと EQQMLOG にある run cycle を扱います。第四十四観点 対象は アプリケーションをいつ計画へ載せるかを決める周期条件で、カレンダーと入力到着時刻と合です。第四十四観点 DWC と ISPF の結果を分け、CPU08 の記録先を明確にします。第四十四観点 資源待ちがあれば special resource 名を IWA資源064へ記録します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **run cycle 再実行判断 ログ採取044**

    - 検証目的: 監査ログと EQQMLOGにおける run cycle の再実行判断を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU08
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、run cycle の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman showjobs PAYROLL064.IWAJOB064
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Stream: PAYROLL064
    Job: IWAJOB064
    Workstation: CPU08
    Status: SUCC
    Return Code: 0
    ```

    画面・出力には Stream が含まれる。Stream を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU08 の対応を確認する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman submit sched PAYROLL064
    → Enter を押す
    ```

    画面・出力:
    ```text
    Schedule PAYROLL064 submitted
    Instance 2607150900 queued for workstation CPU08
    ```

    画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman showjobs PAYROLL064.IWAJOB064
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Stream: PAYROLL064
    Job: IWAJOB064
    Status: READY
    Dependencies: satisfied
    ```

    画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### run cycle 実行監視 再実行014 {#c15-i0239}
*分類: 監査ログと EQQMLOG*  ・  難易度: 初級

第十四観点 run cycle の 再実行014 は IBM Workload Automation の 監査ログと EQQMLOG に属します。第十四観点 対象は アプリケーションをいつ計画へ載せるかを決める周期条件で、カレンダーと入力到着時刻と合です。第十四観点 IWA034 の確認では conman showjobs の Job Stream と Job 状態 を起点に、CPU02 と対象 engine を照合します。第十四観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡034として整理します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **run cycle 実行監視 再実行014**

    - 検証目的: 監査ログと EQQMLOGにおける run cycle の実行監視を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU02
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、run cycle の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman showjobs PAYROLL034.IWAJOB034
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Stream: PAYROLL034
    Job: IWAJOB034
    Workstation: CPU02
    Status: SUCC
    Return Code: 0
    ```

    画面・出力には Stream が含まれる。Stream を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU02 の対応を確認する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman submit sched PAYROLL034
    → Enter を押す
    ```

    画面・出力:
    ```text
    Schedule PAYROLL034 submitted
    Instance 2607150900 queued for workstation CPU02
    ```

    画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Workload Scheduler command line
    Command ===> conman showjobs PAYROLL034.IWAJOB034
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Stream: PAYROLL034
    Job: IWAJOB034
    Status: READY
    Dependencies: satisfied
    ```

    画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG ログとの照合 EQQ07 {#c15-i0240}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

ログとの照合では 監査ログと EQQMLOG の ログ参照 を主操作として EQQ07 を判定します。時刻と対象識別子への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ07 に残します。ログとの照合を補助する ADID検索 では OPNO を補助値として EQQ07 へ保存します。主判定のログとの照合では監査ログの ログ参照 から EQQN013I を読み EQQ07 へ残します。証跡照合のログとの照合では監査ログの EQQN013I と OPNO を EQQ07 に保存します。記録対応のログとの照合では監査ログの Message IDとADID の証跡へ EQQ07 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** ログとの照合で 監査ログと EQQMLOG の ログ参照 と ADID検索 を用い 操作とログを対応 します。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。EQQN013I で対象 EQQ07 の Message IDとADID を再現できる記録はどれですか。

    - A. EQQN013Iを含むログ参照の応答行を保存する。その応答を得るためSDSF browse EQQCONT DD EQQMLOGを使用する。対象EQQ07のMessage IDとADIDとして記録する。 ✅
    - B. SDSF browse EQQCONT DD EQQMLOGが応答を返した時点で正常とする。応答中のEQQN013Iの値は記録しない。RETURNをEQQN013Iと同じ判定値とみなし対象EQQ07の主証跡にする。
    - C. SDSF browse EQQCONT DD EQQMLOGのコマンド文字列だけを記録する。EQQN013Iを含む応答行は保存しない。
    - D. EQQMLOGの停止または再定義を実施する。その後にSDSF browse EQQCONT DD EQQMLOGでEQQN013Iを採取する。

    正解: **A** ／ 難易度: 上級

    **解説:** 適切な判定: Aはログ参照で EQQN013I を読みMessage IDとADIDの主値として操作とログを対応しEQQ07に残します。
    機能の仕組み: ログとの照合ではADID検索を補助操作としEQQMLOGの時刻と対象識別子をOPNOと対象EQQ07で照合します。
    各候補の評価: ログ参照とADID検索の役割を分けるとA: EQQN013Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではMessage IDとADIDを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではMessage IDとADIDを証明できない点でMessage IDとADIDを確認できません、D: 変更前のMessage IDとADIDを失う点でADID検索の範囲を越えます。結論としてログとの照合の監査ログで判定する対象は EQQ07 です。
    用語の定義: ログとの照合で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ07へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG ログとの照合 EQQ07**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて操作とログを対応し、EQQ07のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ07のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP07を指定し、EQQ07のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP07
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP07 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ07の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の RETURN が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 代替経路の確認 EQQ10 {#c15-i0241}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

代替経路の確認では 監査ログと EQQMLOG の ログ参照 を主操作として EQQ10 を判定します。主経路との役割差への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ10 に残します。代替経路の確認を補助する ADID検索 では OPNO を補助値として EQQ10 へ保存します。主判定の代替経路の確認では監査ログの ログ参照 から EQQN013I を読み EQQ10 へ残します。証跡照合の代替経路の確認では監査ログの EQQN013I と OPNO を EQQ10 に保存します。記録対応の代替経路の確認では監査ログの Message IDとADID の証跡へ EQQ10 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 監査ログと EQQMLOG の ログ参照 と ADID検索 の役割を分け 主経路との役割差 を調べます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。対象 EQQ10 を誤判定しない進め方はどれですか。

    - A. SDSF browse EQQCONT DD EQQMLOGのコマンド文字列だけを記録する。EQQN013Iを含む応答行は保存しない。
    - B. EQQMLOGの停止または再定義を実施する。その後にSDSF browse EQQCONT DD EQQMLOGでEQQN013Iを採取する。
    - C. ジョブストリーム運用のInput ArrivalとStatusを確認する。その値を監査ログと EQQMLOGのEQQ10にも適用する。
    - D. SDSF browse EQQCONT DD EQQMLOGとSDSF EQQMLOG FIND APP10の対象名をそろえる。前者のEQQN013IをMessage IDとADIDの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正しい判定結果: Dはログ参照で EQQN013I を読みMessage IDとADIDの主値として代替手段の成立を確認しEQQ10に残します。
    運用上の背景: 代替経路の確認ではADID検索を補助操作としEQQMLOGの主経路との役割差をOPNOと対象EQQ10で照合します。
    候補別の検討: ログ参照とADID検索の役割を分けるとA: 入力記録だけではMessage IDとADIDを証明できない点で一次資料と一致しません、B: 変更前のMessage IDとADIDを失う点でMessage IDとADIDを確認できません、C: ジョブストリーム運用の値ではEQQN013Iを確認できない点でADID検索の範囲を越えます、D: 同じ対象名のEQQN013Iを採用する点で現在値を示します。結論として代替経路の確認の監査ログで判定する対象は EQQ10 です。
    重要用語の定義: 代替経路の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ10へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 代替経路の確認 EQQ10**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて代替手段の成立を確認し、EQQ10のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ10のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP10を指定し、EQQ10のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP10
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP10 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ10の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の RETURN が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 変更前の確認 EQQ02 {#c15-i0242}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

変更前の確認では 監査ログと EQQMLOG の ADID検索 を主操作として EQQ02 を判定します。変更対象と非対象の境界への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ02 に残します。変更前の確認を補助する 日次計画結果 では RETURN を補助値として EQQ02 へ保存します。主判定の変更前の確認では監査ログの ADID検索 から OPNO を読み EQQ02 へ残します。証跡照合の変更前の確認では監査ログの OPNO と RETURN を EQQ02 に保存します。記録対応の変更前の確認では監査ログの Message IDとADID の証跡へ EQQ02 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 監査ログと EQQMLOG の ADID検索 と 日次計画結果 を照合し 変更対象と非対象の境界 を確かめます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。OPNO を読む前に対象 EQQ02 へ行う確認はどれですか。

    - A. SDSF EQQMLOG FIND APP02を対象名なしで実行する。一覧の先頭行をEQQ02の結果として記録する。
    - B. 前回保存したSDSF EQQMLOG FIND APP02の結果を使う。今回のSDSF browse SYSPRINT FIND RETURN CODEの結果と同一時点の証跡として比較する。
    - C. 保存済みのEQQ02の出力を再利用する。今回のSDSF EQQMLOG FIND APP02とSDSF browse SYSPRINT FIND RETURN CODEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象EQQ02についてSDSF EQQMLOG FIND APP02の応答からOPNOを確認する。SDSF browse SYSPRINT FIND RETURN CODEは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 採用理由: DはADID検索で OPNO を読みMessage IDとADIDの主値として変更前の証跡を保存しEQQ02に残します。
    動作の背景: 変更前の確認では日次計画結果を補助操作としEQQMLOGの変更対象と非対象の境界をRETURNと対象EQQ02で照合します。
    各選択肢の検討: ADID検索と日次計画結果の役割を分けるとA: 先頭行はEQQ02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でADID検索を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で監査ログと EQQMLOGに使いません、D: OPNOと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の監査ログで判定する対象は EQQ02 です。
    初出用語の定義: 変更前の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ02へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 変更前の確認 EQQ02**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて変更前の証跡を保存し、EQQ02のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP02を指定し、EQQ02のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP02
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP02 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ02の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ02のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
    ② ステップ2 の RETURN が画面・出力に表示されること
    ③ ステップ3 の EQQN013I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 変更後の確認 EQQ03 {#c15-i0243}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

変更後の確認では 監査ログと EQQMLOG の 日次計画結果 を主操作として EQQ03 を判定します。反映値と残存値への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ03 に残します。変更後の確認を補助する ログ参照 では EQQN013I を補助値として EQQ03 へ保存します。主判定の変更後の確認では監査ログの 日次計画結果 から RETURN を読み EQQ03 へ残します。証跡照合の変更後の確認では監査ログの RETURN と EQQN013I を EQQ03 に保存します。記録対応の変更後の確認では監査ログの Message IDとADID の証跡へ EQQ03 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 監査ログと EQQMLOG の 日次計画結果 と ログ参照 を組み合わせる際は EQQMLOG がcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログという仕組みを前提にします。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。RETURN と Message IDとADID を対象 EQQ03 で確認する組合せはどれですか。

    - A. SDSF browse EQQCONT DD EQQMLOGで周辺状態を押さえる。その後にSDSF browse SYSPRINT FIND RETURN CODEでRETURNを確認して変更結果を検証する。 ✅
    - B. EQQMLOGの停止または再定義を実施する。その後にSDSF browse SYSPRINT FIND RETURN CODEでRETURNを採取する。
    - C. 監査ログと EQQMLOGのMessage IDとADIDを確認する。その値を監査ログと EQQMLOGのEQQ03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。EQQMLOGの反映値と残存値は確認済みとして扱う。さらにSDSF EQQMLOG FIND APP03のOPNOをRETURNと同種の値として併記する。
    - D. SDSF browse EQQCONT DD EQQMLOGが成功したためSDSF browse SYSPRINT FIND RETURN CODEのRETURNも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正答の根拠: Aは日次計画結果で RETURN を読みMessage IDとADIDの主値として変更結果を検証しEQQ03に残します。
    内部の仕組み: 変更後の確認ではログ参照を補助操作としEQQMLOGの反映値と残存値をEQQN013Iと対象EQQ03で照合します。
    誤答を含む比較: 日次計画結果とログ参照の役割を分けるとA: 周辺状態の後にRETURNを確認する点でEQQ03を判定できます、B: 変更前のMessage IDとADIDを失う点でログ参照の範囲を越えます、C: 監査ログと EQQMLOGの値ではRETURNを確認できないうえに追加前提も不正な点でEQQ03の値を示しません、D: 補助操作の成功ではRETURNを確定できない点で変更後の確認に合いません。結論として変更後の確認の監査ログで判定する対象は EQQ03 です。
    用語定義: 変更後の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ03へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 変更後の確認 EQQ03**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて変更結果を検証し、EQQ03のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ03の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ03のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP03を指定し、EQQ03のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP03
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP03 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RETURN が画面・出力に表示されること
    ② ステップ2 の EQQN013I が画面・出力に表示されること
    ③ ステップ3 の OPNO が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 引継ぎ記録 EQQ09 {#c15-i0244}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

引継ぎ記録では 監査ログと EQQMLOG の 日次計画結果 を主操作として EQQ09 を判定します。次担当者が追跡できる証跡への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ09 に残します。引継ぎ記録を補助する ログ参照 では EQQN013I を補助値として EQQ09 へ保存します。主判定の引継ぎ記録では監査ログの 日次計画結果 から RETURN を読み EQQ09 へ残します。証跡照合の引継ぎ記録では監査ログの RETURN と EQQN013I を EQQ09 に保存します。記録対応の引継ぎ記録では監査ログの Message IDとADID の証跡へ EQQ09 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 監査ログと EQQMLOG の 日次計画結果 と ログ参照 を組み合わせる際は EQQMLOG がcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログという仕組みを前提にします。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。RETURN と Message IDとADID を対象 EQQ09 で確認する組合せはどれですか。

    - A. SDSF browse EQQCONT DD EQQMLOGが成功したためSDSF browse SYSPRINT FIND RETURN CODEのRETURNも正常だと推定する。主出力は保存しない。
    - B. SDSF browse SYSPRINT FIND RETURN CODEを対象名なしで実行する。一覧の先頭行をEQQ09の結果として記録する。
    - C. 対象名EQQ09を指定してSDSF browse SYSPRINT FIND RETURN CODEを実行する。応答中のRETURNと時刻を保存する。SDSF browse EQQCONT DD EQQMLOGで周辺状態を補完する。 ✅
    - D. 前回保存したSDSF browse SYSPRINT FIND RETURN CODEの結果を使う。今回のSDSF browse EQQCONT DD EQQMLOGの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 上級

    **解説:** 採用操作の理由: Cは日次計画結果で RETURN を読みMessage IDとADIDの主値として再現可能な記録を作成しEQQ09に残します。
    製品内の仕組み: 引継ぎ記録ではログ参照を補助操作としEQQMLOGの次担当者が追跡できる証跡をEQQN013Iと対象EQQ09で照合します。
    選択肢別の説明: 日次計画結果とログ参照の役割を分けるとA: 補助操作の成功ではRETURNを確定できない点でEQQ09の値を示しません、B: 先頭行はEQQ09と確定できない点で引継ぎ記録に合いません、C: RETURNと時刻を保存する点で日次計画結果に合います、D: 採取時刻が異なる点で監査ログと EQQMLOGに使いません。結論として引継ぎ記録の監査ログで判定する対象は EQQ09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ09へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 引継ぎ記録 EQQ09**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて再現可能な記録を作成し、EQQ09のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ09の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ09のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP09を指定し、EQQ09のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP09
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP09 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RETURN が画面・出力に表示されること
    ② ステップ2 の EQQN013I が画面・出力に表示されること
    ③ ステップ3 の OPNO が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 復旧後の確認 EQQ06 {#c15-i0245}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

復旧後の確認では 監査ログと EQQMLOG の 日次計画結果 を主操作として EQQ06 を判定します。再発していないことを示す値への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ06 に残します。復旧後の確認を補助する ログ参照 では EQQN013I を補助値として EQQ06 へ保存します。主判定の復旧後の確認では監査ログの 日次計画結果 から RETURN を読み EQQ06 へ残します。証跡照合の復旧後の確認では監査ログの RETURN と EQQN013I を EQQ06 に保存します。記録対応の復旧後の確認では監査ログの Message IDとADID の証跡へ EQQ06 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 監査ログと EQQMLOG の 日次計画結果 と ログ参照 を実施し EQQMLOG の役割を確認します。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。対象 EQQ06 の証跡を取る方法はどれですか。

    - A. 長期計画管理のRun DateとInput Arrivalを確認する。その値を監査ログと EQQMLOGのEQQ06にも適用する。
    - B. SDSF browse EQQCONT DD EQQMLOGが成功したためSDSF browse SYSPRINT FIND RETURN CODEのRETURNも正常だと推定する。主出力は保存しない。別資源で得た状態を対象EQQ06へ引き継げるものとする。
    - C. SDSF browse SYSPRINT FIND RETURN CODEを対象名なしで実行する。一覧の先頭行をEQQ06の結果として記録する。
    - D. SDSF browse SYSPRINT FIND RETURN CODEでRETURNを取得してからSDSF EQQMLOG FIND APP06でOPNOを照合する。EQQ06のMessage IDとADIDを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正答内容: Dは日次計画結果で RETURN を読みMessage IDとADIDの主値として復旧後の安定性を確認しEQQ06に残します。
    構成上の背景: 復旧後の確認ではログ参照を補助操作としEQQMLOGの再発していないことを示す値をEQQN013Iと対象EQQ06で照合します。
    候補ごとの理由: 日次計画結果とログ参照の役割を分けるとA: 長期計画管理の値ではRETURNを確認できない点でログ参照の範囲を越えます、B: 補助操作の成功ではRETURNを確定できないうえに追加前提も不正な点でEQQ06の値を示しません、C: 先頭行はEQQ06と確定できない点で復旧後の確認に合いません、D: RETURNとOPNOを順に照合する点で日次計画結果に合います。結論として復旧後の確認の監査ログで判定する対象は EQQ06 です。
    初出用語: 復旧後の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ06へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 復旧後の確認 EQQ06**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて復旧後の安定性を確認し、EQQ06のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ06の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ06のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP06を指定し、EQQ06のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP06
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP06 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の RETURN が画面・出力に表示されること
    ② ステップ2 の EQQN013I が画面・出力に表示されること
    ③ ステップ3 の OPNO が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 復旧準備 EQQ05 {#c15-i0246}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

復旧準備では 監査ログと EQQMLOG の ADID検索 を主操作として EQQ05 を判定します。再開前に必要な整合性への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ05 に残します。復旧準備を補助する 日次計画結果 では RETURN を補助値として EQQ05 へ保存します。主判定の復旧準備では監査ログの ADID検索 から OPNO を読み EQQ05 へ残します。証跡照合の復旧準備では監査ログの OPNO と RETURN を EQQ05 に保存します。記録対応の復旧準備では監査ログの Message IDとADID の証跡へ EQQ05 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧準備で 監査ログと EQQMLOG の ADID検索 と 日次計画結果 を使い 復旧条件を確認 します。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。OPNO を読み対象 EQQ05 を切り分ける確認方法はどれですか。

    - A. 前回保存したSDSF EQQMLOG FIND APP05の結果を使う。今回のSDSF browse SYSPRINT FIND RETURN CODEの結果と同一時点の証跡として比較する。
    - B. 保存済みのEQQ05の出力を再利用する。今回のSDSF EQQMLOG FIND APP05とSDSF browse SYSPRINT FIND RETURN CODEは実行済みとして扱う。
    - C. 変更を加えずSDSF EQQMLOG FIND APP05を実行する。OPNOを保存する。差分はSDSF browse SYSPRINT FIND RETURN CODEの結果と対象名で対応させる。 ✅
    - D. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをMessage IDとADIDの主判定に採用する。SDSF EQQMLOG FIND APP05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: CはADID検索で OPNO を読みMessage IDとADIDの主値として復旧条件を確認しEQQ05に残します。
    処理の仕組み: 復旧準備では日次計画結果を補助操作としEQQMLOGの再開前に必要な整合性をRETURNと対象EQQ05で照合します。
    選択結果の内訳: ADID検索と日次計画結果の役割を分けるとA: 採取時刻が異なる点でADID検索を代替しません、B: 過去出力では今回の復旧準備を示せない点で監査ログと EQQMLOGに使いません、C: 変更前のOPNOを保存する点で正答です、D: RETURNはOPNOを代替しないうえに追加前提も不正な点でEQQ05を採用できません。結論として復旧準備の監査ログで判定する対象は EQQ05 です。
    用語の説明: 復旧準備で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ05へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 復旧準備 EQQ05**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて復旧条件を確認し、EQQ05のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP05を指定し、EQQ05のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP05
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP05 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ05の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ05のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
    ② ステップ2 の RETURN が画面・出力に表示されること
    ③ ステップ3 の EQQN013I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 構成監査 EQQ08 {#c15-i0247}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

構成監査では 監査ログと EQQMLOG の ADID検索 を主操作として EQQ08 を判定します。定義値と稼働値の一致への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ08 に残します。構成監査を補助する 日次計画結果 では RETURN を補助値として EQQ08 へ保存します。主判定の構成監査では監査ログの ADID検索 から OPNO を読み EQQ08 へ残します。証跡照合の構成監査では監査ログの OPNO と RETURN を EQQ08 に保存します。記録対応の構成監査では監査ログの Message IDとADID の証跡へ EQQ08 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 構成監査で 監査ログと EQQMLOG の ADID検索 と 日次計画結果 を照合し 定義値と稼働値の一致 を確かめます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。OPNO を読む前に対象 EQQ08 へ行う確認はどれですか。

    - A. 保存済みのEQQ08の出力を再利用する。今回のSDSF EQQMLOG FIND APP08とSDSF browse SYSPRINT FIND RETURN CODEは実行済みとして扱う。
    - B. SDSF browse SYSPRINT FIND RETURN CODEの結果だけでは確定しない。SDSF EQQMLOG FIND APP08のOPNOを主証跡として構成差分を監査する。 ✅
    - C. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをMessage IDとADIDの主判定に採用する。SDSF EQQMLOG FIND APP08の応答は採取対象から外す。
    - D. SDSF browse EQQCONT DD EQQMLOGのEQQN013IをOPNOと同義の成功表示として扱う。SDSF EQQMLOG FIND APP08は実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: BはADID検索で OPNO を読みMessage IDとADIDの主値として構成差分を監査しEQQ08に残します。
    実行時の背景: 構成監査では日次計画結果を補助操作としEQQMLOGの定義値と稼働値の一致をRETURNと対象EQQ08で照合します。
    四つの候補の理由: ADID検索と日次計画結果の役割を分けるとA: 過去出力では今回の構成監査を示せない点で監査ログと EQQMLOGに使いません、B: OPNOを主証跡として区別する点で正答です、C: RETURNはOPNOを代替しない点でEQQ08を採用できません、D: EQQN013IとOPNOは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の監査ログで判定する対象は EQQ08 です。
    初出語定義: 構成監査で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ08へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 構成監査 EQQ08**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて構成差分を監査し、EQQ08のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP08を指定し、EQQ08のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP08
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP08 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ08の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ08のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
    ② ステップ2 の RETURN が画面・出力に表示されること
    ③ ステップ3 の EQQN013I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 通常状態の確認 EQQ01 {#c15-i0248}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

通常状態の確認では 監査ログと EQQMLOG の ログ参照 を主操作として EQQ01 を判定します。基準値と現在値の差への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ01 に残します。通常状態の確認を補助する ADID検索 では OPNO を補助値として EQQ01 へ保存します。主判定の通常状態の確認では監査ログの ログ参照 から EQQN013I を読み EQQ01 へ残します。証跡照合の通常状態の確認では監査ログの EQQN013I と OPNO を EQQ01 に保存します。記録対応の通常状態の確認では監査ログの Message IDとADID の証跡へ EQQ01 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 監査ログと EQQMLOG の ログ参照 と ADID検索 を用い 通常状態を確定 します。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。EQQN013I で対象 EQQ01 の Message IDとADID を再現できる記録はどれですか。

    - A. SDSF EQQMLOG FIND APP01のOPNOをMessage IDとADIDの主判定に採用する。SDSF browse EQQCONT DD EQQMLOGの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをEQQN013Iと同義の成功表示として扱う。SDSF browse EQQCONT DD EQQMLOGは実行しない。
    - C. SDSF browse EQQCONT DD EQQMLOGを先に実行する。対象EQQ01のEQQN013IをMessage IDとADIDとして記録する。続いてSDSF EQQMLOG FIND APP01で同一対象を照合する。 ✅
    - D. SDSF browse EQQCONT DD EQQMLOGが応答を返した時点で正常とする。応答中のEQQN013Iの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cはログ参照で EQQN013I を読みMessage IDとADIDの主値として通常状態を確定しEQQ01に残します。
    背景・仕組み: 通常状態の確認ではADID検索を補助操作としEQQMLOGの基準値と現在値の差をOPNOと対象EQQ01で照合します。
    選択肢の理由: ログ参照とADID検索の役割を分けるとA: OPNOはEQQN013Iを代替しないうえに追加前提も不正な点でEQQMLOGに使えません、B: RETURNとEQQN013Iは確認項目が異なる点でEQQ01を採用できません、C: EQQN013Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではMessage IDとADIDを判定できない点で一次資料と一致しません。結論として通常状態の確認の監査ログで判定する対象は EQQ01 です。
    用語の初出定義: 通常状態の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ01へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 通常状態の確認 EQQ01**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて通常状態を確定し、EQQ01のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ01のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP01を指定し、EQQ01のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP01
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP01 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ01の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の RETURN が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 監査ログと EQQMLOG EQQMLOG 障害切り分け EQQ04 {#c15-i0249}
*分類: 監査ログと EQQMLOG*  ・  難易度: 上級

障害切り分けでは 監査ログと EQQMLOG の ログ参照 を主操作として EQQ04 を判定します。最初に失敗した処理への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ04 に残します。障害切り分けを補助する ADID検索 では OPNO を補助値として EQQ04 へ保存します。主判定の障害切り分けでは監査ログの ログ参照 から EQQN013I を読み EQQ04 へ残します。証跡照合の障害切り分けでは監査ログの EQQN013I と OPNO を EQQ04 に保存します。記録対応の障害切り分けでは監査ログの Message IDとADID の証跡へ EQQ04 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 監査ログと EQQMLOG の ログ参照 と ADID検索 の役割を分け 最初に失敗した処理 を調べます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。対象 EQQ04 を誤判定しない進め方はどれですか。

    - A. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをEQQN013Iと同義の成功表示として扱う。SDSF browse EQQCONT DD EQQMLOGは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. SDSF browse EQQCONT DD EQQMLOGの出力でEQQ04とEQQN013Iが同じ応答にあることを確認する。Message IDとADIDをその応答から採取する。 ✅
    - C. SDSF browse EQQCONT DD EQQMLOGが応答を返した時点で正常とする。応答中のEQQN013Iの値は記録しない。
    - D. SDSF browse EQQCONT DD EQQMLOGのコマンド文字列だけを記録する。EQQN013Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bはログ参照で EQQN013I を読みMessage IDとADIDの主値として障害範囲を限定しEQQ04に残します。
    技術的背景: 障害切り分けではADID検索を補助操作としEQQMLOGの最初に失敗した処理をOPNOと対象EQQ04で照合します。
    四択の評価: ログ参照とADID検索の役割を分けるとA: RETURNとEQQN013Iは確認項目が異なるうえに追加前提も不正な点でEQQ04を採用できません、B: EQQ04とEQQN013Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではMessage IDとADIDを判定できない点で一次資料と一致しません、D: 入力記録だけではMessage IDとADIDを証明できない点でMessage IDとADIDを確認できません。結論として障害切り分けの監査ログで判定する対象は EQQ04 です。
    初出語の意味: 障害切り分けで使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ04へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **監査ログと EQQMLOG EQQMLOG 障害切り分け EQQ04**

    - 検証目的: 監査ログと EQQMLOGのEQQMLOGについて障害範囲を限定し、EQQ04のMessage IDとADIDを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ04のログ参照を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse EQQCONT DD EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
    ```

    画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP04を指定し、EQQ04のADID検索を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF EQQMLOG FIND APP04
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG APP04 IA 260715 1400 OPNO 010 STATUS COMPLETE
    ```

    画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ04の日次計画結果を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND RETURN CODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
    ```

    画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
    ② ステップ2 の OPNO が画面・出力に表示されること
    ③ ステップ3 の RETURN が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide




## IBM Workload Automation > 計画

### 現在計画 Current Plan {#c15-i0250}
*分類: 計画*  ・  難易度: 初級

IBM Workload Automation の 計画で扱う現在計画 Current Planは、現在計画は、実際に実行・追跡する対象ジョブや操作を保持する運用中の計画です。依存関係、ワークステーション、特殊資源、実行状態が含まれます。日々の運用では current plan の更新と拡張が中心になります

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 呼出確認の現在計画で作業スケジューラーの運用確認を行います。現在計画 Current Planの根拠にできる作業はどれですか。

    - A. IBM Workload Automationと無関係な一覧で呼出確認の現在計画を確認した扱いにする。
    - B. EQQZ045I の有無を確認せず呼出確認の現在計画を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. 現在計画 Current Planの属性行を読まず呼出確認の現在計画の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では現在計画 Current Plan は「IBM Workload Automationで現在計画 Current Planの扱いを記録する呼出確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では現在計画 Current Planの表示結果と EQQZ045I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では現在計画 Current Planの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **現在計画 Current Plan**

    - 検証目的: 呼出確認の現在計画について、IBM Workload Automation の 計画で扱う現在計画 Current Planは、現在計画は、実際に実行・追跡する対象ジョブや操作を保持する運用中の計画でに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、呼出確認の現在計画の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄に現在計画 Current Planを指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND 現在計画 Current Plan
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM 現在計画 Current Plan
    CASE OSKB010003
    SOURCE IBM Workload Automation
    ```

    現在計画 Current PlanとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010003を同じ出力で読み、呼出確認の現在計画の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010003
    COMMAND ===> OPSTAT
    OPERATION OSKB010003 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の 現在計画 Current Plan と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler



### 長期計画 LTP {#c15-i0251}
*分類: 計画*  ・  難易度: 初級

IBM Workload Automation の 計画で扱う長期計画 LTPは、長期計画は、将来の期間に実行するアプリケーションやジョブの高レベルな予定を作る計画です。数か月単位の予定や休日、サイクルを反映し、現在計画の元になります。計画変更では LTP の対象期間と反映先を確認します

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 展開確認の長期計画で長期計画 LTP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 長期計画 LTP の出力を取らず展開確認の長期計画の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 ✅
    - C. OPSTAT を省略して展開確認の長期計画の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の長期計画へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では長期計画 LTP は「展開確認の長期計画に関係する定義値と表示行を照合する展開確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では長期計画 LTP の属性行と EQQZ045I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では長期計画 LTP を IBM Workload Automationの運用手順で確認し、初出名は展開確認初出です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **長期計画 LTP**

    - 検証目的: 展開確認の長期計画について、IBM Workload Automation の 計画で扱う長期計画 LTP は、長期計画は、将来の期間に実行するアプリケーションやジョブの高レベルな予定を作る計画です。数に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、展開確認の長期計画の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄に長期計画 LTPを指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND 長期計画 LTP
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM 長期計画 LTP
    CASE OSKB010002
    SOURCE IBM Workload Automation
    ```

    長期計画 LTPとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010002を同じ出力で読み、展開確認の長期計画の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010002
    COMMAND ===> OPSTAT
    OPERATION OSKB010002 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の 長期計画 LTP と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler




## IBM Workload Automation > 運用

### Restart and cleanup {#c15-i0252}
*分類: 運用*  ・  難易度: 上級

IBM Workload Automation の 運用で扱うRestart and cleanupは、失敗したジョブの再実行や後片付けを支援する機能です。データセット削除、再投入条件、前回実行結果の扱いが関わります。自動化するときは安全に再実行できるジョブかどうかを確認します

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 復旧確認の運用で Restart and cleanupの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Restart and cleanupの出力を取らず復旧確認の運用の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 ✅
    - C. OPSTAT を省略して復旧確認の運用の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の運用へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Restart and cleanup は「復旧確認の運用に関係する定義値と表示行を照合する復旧確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Restart and cleanupの属性行と EQQZ045I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Restart and cleanupを IBM Workload Automationの運用手順で確認し、初出名は復旧確認初出です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **Restart and cleanup**

    - 検証目的: 復旧確認の運用について、IBM Workload Automation の 運用で扱う Restart and cleanupは、失敗したジョブの再実行や後片付けを支援する機能です。データセット削除に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、復旧確認の運用の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にRestart and cleanuを指定し、OSKB010018の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND Restart and cleanu
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM Restart and cleanu
    CASE OSKB010018
    SOURCE IBM Workload Automation
    ```

    Restart and cleanuとOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010018を同じ出力で読み、復旧確認の運用の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010018
    COMMAND ===> OPSTAT
    OPERATION OSKB010018 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の Restart and cleanu と OSKB010018 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler



### 計画の拡張 {#c15-i0253}
*分類: 運用*  ・  難易度: 初級

IBM Workload Automation の 運用で扱う計画の拡張は、現在計画または長期計画の対象期間を先へ延ばす運用作業です。拡張を忘れると将来のジョブが計画に現れず、投入対象になりません。定期運用では拡張結果とカレンダー反映を確認します

**出典:** IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

??? question "確認問題（1問）"
    **問題.** 警告確認の計画の拡張に関係する計画の拡張の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. OPSTAT で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 ✅
    - B. 計画の拡張の名称と担当者名のみを残して警告確認の計画の拡張の表示本文を確認対象に含めない。
    - C. 作業スケジューラー以外の画面で警告確認の計画の拡張を確認し同じ証跡として扱ったことにする。
    - D. EQQZ045I の有無を見ず警告確認の計画の拡張の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では計画の拡張は「計画の拡張の用途を作業スケジューラーの表示で確認する警告確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Workload Automationの計画の拡張と EQQZ045I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では計画の拡張を IBM Workload Automationで扱う確認対象とし、用語名は警告確認用語です。

    **出典:** 20_ZWS_Managing_Workload / 01_Overview


??? note "検証手順（1件）"
    **計画の拡張**

    - 検証目的: 警告確認の計画の拡張について、IBM Workload Automation の 運用で扱う計画の拡張は、現在計画または長期計画の対象期間を先へ延ばす運用作業です。拡張を忘れると将来のジョブが計画に現れに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に OPSTAT を入力し、警告確認の計画の拡張の確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> OPSTAT
    ```

    COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄に計画の拡張を指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND 計画の拡張
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM 計画の拡張
    CASE OSKB010017
    SOURCE IBM Workload Automation
    ```

    計画の拡張とOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010017を同じ出力で読み、警告確認の計画の拡張の根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> OPSTAT
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010017
    COMMAND ===> OPSTAT
    OPERATION OSKB010017 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> OPSTAT が画面・出力に表示されること
    ② ステップ2 の 計画の拡張 と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler




## IBM Workload Automation > 長期計画管理

### EQQJOBSA 依存関係確認 監視017 {#c15-i0254}
*分類: 長期計画管理*  ・  難易度: 初級

第十七観点 EQQJOBSA は IBM Workload Automation の 長期計画管理 で扱う確認点です。第十七観点 対象は IBM Z Workload Scheduler の batch-job skeleです。第十七観点 採取値 CAL01 を計画表とログの両方で読み、採取時刻をそろえます。第十七観点 採取後は DWC 表示と ISPF 表示の差を IWA比較037に分けます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **EQQJOBSA 依存関係確認 監視017**

    - 検証目的: 長期計画管理における EQQJOBSA の依存関係確認を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CAL01
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQJOBSA の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMLTP ---------------- LONG TERM PLAN ----------------
    Command ===> LOCATE CAL01
    → Enter を押す
    ```

    画面・出力:
    ```text
    LONG TERM PLAN
    CALENDAR CAL01 RUN CYCLE RCY08 APPLICATION PAYROLL037 INCLUDED
    ```

    画面・出力には LONG が含まれる。LONG を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Restart and cleanup の確認メッセージ と CAL01 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMAOCP -------- ADDING AN APPLICATION TO THE CURRENT PLAN --------
    Command ===> ADD PAYROLL037
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADDING APPLICATION TO CURRENT PLAN
    ADID PAYROLL037
    INPUT ARRIVAL 260715 0900
    OPERATIONS SELECTED
    ```

    画面・出力には ADDING が含まれる。ADDING を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMMOPL -------- MODIFYING OPERATIONS IN THE CURRENT PLAN --------
    Command ===> OPER
    → Enter を押す
    ```

    画面・出力:
    ```text
    MODIFYING OPERATIONS
    ADID PAYROLL037 OPNO 170 WORKSTATION CPU05 JOB IWAJOB037
    ```

    画面・出力には MODIFYING が含まれる。MODIFYING を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: LONG が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: ADDING が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: MODIFYING が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### EQQJOBSA 変更反映 資源確認077 {#c15-i0255}
*分類: 長期計画管理*  ・  難易度: 中級

第七十七観点 EQQJOBSA は IBM Workload Automation の 長期計画管理 で扱う確認点です。第七十七観点 対象は IBM Z Workload Scheduler の batch-job skeleです。第七十七観点 採取値 CAL05 を計画表とログの両方で読み、採取時刻をそろえます。第七十七観点 採取後は DWC 表示と ISPF 表示の差を IWA比較097に分けます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **EQQJOBSA 変更反映 資源確認077**

    - 検証目的: 長期計画管理における EQQJOBSA の変更反映を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CAL05
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQJOBSA の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMLTP ---------------- LONG TERM PLAN ----------------
    Command ===> LOCATE CAL05
    → Enter を押す
    ```

    画面・出力:
    ```text
    LONG TERM PLAN
    CALENDAR CAL05 RUN CYCLE RCY05 APPLICATION PAYROLL097 INCLUDED
    ```

    画面・出力には LONG が含まれる。LONG を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Restart and cleanup の確認メッセージ と CAL05 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMAOCP -------- ADDING AN APPLICATION TO THE CURRENT PLAN --------
    Command ===> ADD PAYROLL097
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADDING APPLICATION TO CURRENT PLAN
    ADID PAYROLL097
    INPUT ARRIVAL 260715 0900
    OPERATIONS SELECTED
    ```

    画面・出力には ADDING が含まれる。ADDING を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMMOPL -------- MODIFYING OPERATIONS IN THE CURRENT PLAN --------
    Command ===> OPER
    → Enter を押す
    ```

    画面・出力:
    ```text
    MODIFYING OPERATIONS
    ADID PAYROLL097 OPNO 050 WORKSTATION CPU05 JOB IWAJOB097
    ```

    画面・出力には MODIFYING が含まれる。MODIFYING を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: LONG が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: ADDING が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: MODIFYING が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### EQQJOBSA 資源制御 導入確認047 {#c15-i0256}
*分類: 長期計画管理*  ・  難易度: 中級

第四十七観点 長期計画管理 の 導入確認047 では EQQJOBSA を点検します。第四十七観点 対象は IBM Z Workload Scheduler の batch-job skeleです。第四十七観点 待ち状態がある時は Restart and cleanup の確認メッセージ と CAL07 の時刻差を確認します。第四十七観点 ジョブログは JES の purge 前に IWAログ067へ転記します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **EQQJOBSA 資源制御 導入確認047**

    - 検証目的: 長期計画管理における EQQJOBSA の資源制御を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CAL07
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQJOBSA の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMLTP ---------------- LONG TERM PLAN ----------------
    Command ===> LOCATE CAL07
    → Enter を押す
    ```

    画面・出力:
    ```text
    LONG TERM PLAN
    CALENDAR CAL07 RUN CYCLE RCY02 APPLICATION PAYROLL067 INCLUDED
    ```

    画面・出力には LONG が含まれる。LONG を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Restart and cleanup の確認メッセージ と CAL07 の対応を確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMAOCP -------- ADDING AN APPLICATION TO THE CURRENT PLAN --------
    Command ===> ADD PAYROLL067
    → Enter を押す
    ```

    画面・出力:
    ```text
    ADDING APPLICATION TO CURRENT PLAN
    ADID PAYROLL067
    INPUT ARRIVAL 260715 0900
    OPERATIONS SELECTED
    ```

    画面・出力には ADDING が含まれる。ADDING を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    IBM Z Workload Scheduler ISPF
    EQQMMOPL -------- MODIFYING OPERATIONS IN THE CURRENT PLAN --------
    Command ===> OPER
    → Enter を押す
    ```

    画面・出力:
    ```text
    MODIFYING OPERATIONS
    ADID PAYROLL067 OPNO 230 WORKSTATION CPU11 JOB IWAJOB067
    ```

    画面・出力には MODIFYING が含まれる。MODIFYING を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: LONG が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: ADDING が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: MODIFYING が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### long-term plan 再実行判断 ログ採取092 {#c15-i0257}
*分類: 長期計画管理*  ・  難易度: 上級

第九十二観点 ログ採取092 では 長期計画管理 にある long-term plan を扱います。第九十二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第九十二観点 DWC と ISPF の結果を分け、200 の記録先を明確にします。第九十二観点 資源待ちがあれば special resource 名を IWA資源112へ記録します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **long-term plan 再実行判断 ログ採取092**

    - 検証目的: 長期計画管理における long-term plan の再実行判断を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=200
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
    EQQMLOG 112 CONTROLLER CHECK RECORDED
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 200 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 112
    CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
    TRACKER CONNECTIONS LISTED FOR CPU08
    ```

    画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,CPQRY,ADID=PAYROLL112
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
    ADID PAYROLL112 OPNO 200 FOUND IN CURRENT PLAN
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### long-term plan 定義照合 照合002 {#c15-i0258}
*分類: 長期計画管理*  ・  難易度: 初級

第二観点 long-term plan の 照合002 は IBM Workload Automation の 長期計画管理 に属します。第二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第二観点 IWA022 の確認では Dynamic Workload Console の Monitor Jobs 表示 を起点に、020 と対象 engine を照合します。第二観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡022として整理します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **long-term plan 定義照合 照合002**

    - 検証目的: 長期計画管理における long-term plan の定義照合を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=020
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
    EQQMLOG 022 CONTROLLER CHECK RECORDED
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 020 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 022
    CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
    TRACKER CONNECTIONS LISTED FOR CPU02
    ```

    画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,CPQRY,ADID=PAYROLL022
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
    ADID PAYROLL022 OPNO 020 FOUND IN CURRENT PLAN
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### long-term plan 実行監視 再実行062 {#c15-i0259}
*分類: 長期計画管理*  ・  難易度: 中級

第六十二観点 long-term plan の 再実行062 は IBM Workload Automation の 長期計画管理 に属します。第六十二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第六十二観点 IWA082 の確認では Dynamic Workload Console の Monitor Jobs 表示 を起点に、140 と対象 engine を照合します。第六十二観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡082として整理します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **long-term plan 実行監視 再実行062**

    - 検証目的: 長期計画管理における long-term plan の実行監視を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=140
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
    EQQMLOG 082 CONTROLLER CHECK RECORDED
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 140 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 082
    CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
    TRACKER CONNECTIONS LISTED FOR CPU02
    ```

    画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,CPQRY,ADID=PAYROLL082
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
    ADID PAYROLL082 OPNO 140 FOUND IN CURRENT PLAN
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### long-term plan 計画反映 依存確認032 {#c15-i0260}
*分類: 長期計画管理*  ・  難易度: 中級

第三十二観点 依存確認032 では 長期計画管理 にある long-term plan を扱います。第三十二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第三十二観点 DWC と ISPF の結果を分け、080 の記録先を明確にします。第三十二観点 資源待ちがあれば special resource 名を IWA資源052へ記録します。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? note "検証手順（1件）"
    **long-term plan 計画反映 依存確認032**

    - 検証目的: 長期計画管理における long-term plan の計画反映を机上で確認する。
    - 前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=080
    - セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review

    **ステップ 1**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,STATUS
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
    EQQMLOG 052 CONTROLLER CHECK RECORDED
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 080 の対応を確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND EQQMLOG
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQMLOG 052
    CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
    TRACKER CONNECTIONS LISTED FOR CPU08
    ```

    画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。

    **ステップ 3**
    現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F EQQMAJOR,CPQRY,ADID=PAYROLL052
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
    ADID PAYROLL052 OPNO 080 FOUND IN CURRENT PLAN
    ```

    画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。

    - 合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
    ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
    ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan ログとの照合 LTP07 {#c15-i0261}
*分類: 長期計画管理*  ・  難易度: 初級

ログとの照合では 長期計画管理 の 長期計画表示 を主操作として LTP07 を判定します。時刻と対象識別子への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP07 に残します。ログとの照合を補助する 日次計画実行 では DAILY を補助値として LTP07 へ保存します。主判定のログとの照合では長期計画管理の 長期計画表示 から RUNDATE を読み LTP07 へ残します。証跡照合のログとの照合では長期計画管理の RUNDATE と DAILY を LTP07 に保存します。記録対応のログとの照合では長期計画管理の Run DateとInput Arrival の証跡へ LTP07 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** ログとの照合で 長期計画管理 の 長期計画表示 と 日次計画実行 を用い 操作とログを対応 します。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。RUNDATE で対象 LTP07 の Run DateとInput Arrival を再現できる記録はどれですか。

    - A. RUNDATEを含む長期計画表示の応答行を保存する。その応答を得るためISPF Long-Term Planning option DISPLAYを使用する。対象LTP07のRun DateとInput Arrivalとして記録する。 ✅
    - B. ISPF Long-Term Planning option DISPLAYが応答を返した時点で正常とする。応答中のRUNDATEの値は記録しない。EQQ0541EをRUNDATEと同じ判定値とみなし対象LTP07の主証跡にする。Long-Term Planの時刻と対象識別子は確認済みとして扱う。さらにSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRUNDATEと同種の値として併記する。
    - C. ISPF Long-Term Planning option DISPLAYのコマンド文字列だけを記録する。RUNDATEを含む応答行は保存しない。
    - D. Long-Term Planの停止または再定義を実施する。その後にISPF Long-Term Planning option DISPLAYでRUNDATEを採取する。

    正解: **A** ／ 難易度: 初級

    **解説:** 適切な判定: Aは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として操作とログを対応しLTP07に残します。
    機能の仕組み: ログとの照合では日次計画実行を補助操作としLong-Term Planの時刻と対象識別子をDAILYと対象LTP07で照合します。
    各候補の評価: 長期計画表示と日次計画実行の役割を分けるとA: RUNDATEの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではRun DateとInput Arrivalを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではRun DateとInput Arrivalを証明できない点でRun DateとInput Arrivalを確認できません、D: 変更前のRun DateとInput Arrivalを失う点で日次計画実行の範囲を越えます。結論としてログとの照合の長期計画管理で判定する対象は LTP07 です。
    用語の定義: ログとの照合で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP07へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan ログとの照合 LTP07**

    - 検証目的: 長期計画管理のLong-Term Planについて操作とログを対応し、LTP07のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP07の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP07
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP07)を指定し、LTP07の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP07の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
    ② ステップ2 の DAILY が画面・出力に表示されること
    ③ ステップ3 の EQQ0541E が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 代替経路の確認 LTP10 {#c15-i0262}
*分類: 長期計画管理*  ・  難易度: 初級

代替経路の確認では 長期計画管理 の 長期計画表示 を主操作として LTP10 を判定します。主経路との役割差への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP10 に残します。代替経路の確認を補助する 日次計画実行 では DAILY を補助値として LTP10 へ保存します。主判定の代替経路の確認では長期計画管理の 長期計画表示 から RUNDATE を読み LTP10 へ残します。証跡照合の代替経路の確認では長期計画管理の RUNDATE と DAILY を LTP10 に保存します。記録対応の代替経路の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP10 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 長期計画管理 の 長期計画表示 と 日次計画実行 の役割を分け 主経路との役割差 を調べます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。対象 LTP10 を誤判定しない進め方はどれですか。

    - A. ISPF Long-Term Planning option DISPLAYのコマンド文字列だけを記録する。RUNDATEを含む応答行は保存しない。
    - B. Long-Term Planの停止または再定義を実施する。その後にISPF Long-Term Planning option DISPLAYでRUNDATEを採取する。
    - C. ジョブストリーム運用のInput ArrivalとStatusを確認する。その値を長期計画管理のLTP10にも適用する。
    - D. ISPF Long-Term Planning option DISPLAYとSUBMIT IWA.DAILY.CNTL(DP10)の対象名をそろえる。前者のRUNDATEをRun DateとInput Arrivalの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正しい判定結果: Dは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として代替手段の成立を確認しLTP10に残します。
    運用上の背景: 代替経路の確認では日次計画実行を補助操作としLong-Term Planの主経路との役割差をDAILYと対象LTP10で照合します。
    候補別の検討: 長期計画表示と日次計画実行の役割を分けるとA: 入力記録だけではRun DateとInput Arrivalを証明できない点で一次資料と一致しません、B: 変更前のRun DateとInput Arrivalを失う点でRun DateとInput Arrivalを確認できません、C: ジョブストリーム運用の値ではRUNDATEを確認できない点で日次計画実行の範囲を越えます、D: 同じ対象名のRUNDATEを採用する点で現在値を示します。結論として代替経路の確認の長期計画管理で判定する対象は LTP10 です。
    重要用語の定義: 代替経路の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP10へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 代替経路の確認 LTP10**

    - 検証目的: 長期計画管理のLong-Term Planについて代替手段の成立を確認し、LTP10のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP10の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP10
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP10)を指定し、LTP10の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP10の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
    ② ステップ2 の DAILY が画面・出力に表示されること
    ③ ステップ3 の EQQ0541E が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 変更前の確認 LTP02 {#c15-i0263}
*分類: 長期計画管理*  ・  難易度: 初級

変更前の確認では 長期計画管理 の 日次計画実行 を主操作として LTP02 を判定します。変更対象と非対象の境界への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP02 に残します。変更前の確認を補助する 異常メッセージ では EQQ0541E を補助値として LTP02 へ保存します。主判定の変更前の確認では長期計画管理の 日次計画実行 から DAILY を読み LTP02 へ残します。証跡照合の変更前の確認では長期計画管理の DAILY と EQQ0541E を LTP02 に保存します。記録対応の変更前の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP02 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 長期計画管理 の 日次計画実行 と 異常メッセージ を照合し 変更対象と非対象の境界 を確かめます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。DAILY を読む前に対象 LTP02 へ行う確認はどれですか。

    - A. SUBMIT IWA.DAILY.CNTL(DP02)を対象名なしで実行する。一覧の先頭行をLTP02の結果として記録する。
    - B. 前回保存したSUBMIT IWA.DAILY.CNTL(DP02)の結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0541Eの結果と同一時点の証跡として比較する。
    - C. 保存済みのLTP02の出力を再利用する。今回のSUBMIT IWA.DAILY.CNTL(DP02)とSDSF browse SYSPRINT FIND EQQ0541Eは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象LTP02についてSUBMIT IWA.DAILY.CNTL(DP02)の応答からDAILYを確認する。SDSF browse SYSPRINT FIND EQQ0541Eは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 採用理由: Dは日次計画実行で DAILY を読みRun DateとInput Arrivalの主値として変更前の証跡を保存しLTP02に残します。
    動作の背景: 変更前の確認では異常メッセージを補助操作としLong-Term Planの変更対象と非対象の境界をEQQ0541Eと対象LTP02で照合します。
    各選択肢の検討: 日次計画実行と異常メッセージの役割を分けるとA: 先頭行はLTP02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で日次計画実行を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で長期計画管理に使いません、D: DAILYと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の長期計画管理で判定する対象は LTP02 です。
    初出用語の定義: 変更前の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP02へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 変更前の確認 LTP02**

    - 検証目的: 長期計画管理のLong-Term Planについて変更前の証跡を保存し、LTP02のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP02)を指定し、LTP02の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP02の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP02の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP02
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DAILY が画面・出力に表示されること
    ② ステップ2 の EQQ0541E が画面・出力に表示されること
    ③ ステップ3 の APPLICATION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 変更後の確認 LTP03 {#c15-i0264}
*分類: 長期計画管理*  ・  難易度: 初級

変更後の確認では 長期計画管理 の 異常メッセージ を主操作として LTP03 を判定します。反映値と残存値への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP03 に残します。変更後の確認を補助する 長期計画表示 では RUNDATE を補助値として LTP03 へ保存します。主判定の変更後の確認では長期計画管理の 異常メッセージ から EQQ0541E を読み LTP03 へ残します。証跡照合の変更後の確認では長期計画管理の EQQ0541E と RUNDATE を LTP03 に保存します。記録対応の変更後の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP03 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 長期計画管理 の 異常メッセージ と 長期計画表示 を組み合わせる際は Long-Term Plan が将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データという仕組みを前提にします。空または未更新の長期計画から日次計画を作成する危険があります。EQQ0541E と Run DateとInput Arrival を対象 LTP03 で確認する組合せはどれですか。

    - A. ISPF Long-Term Planning option DISPLAYで周辺状態を押さえる。その後にSDSF browse SYSPRINT FIND EQQ0541EでEQQ0541Eを確認して変更結果を検証する。 ✅
    - B. Long-Term Planの停止または再定義を実施する。その後にSDSF browse SYSPRINT FIND EQQ0541EでEQQ0541Eを採取する。
    - C. 監査ログと EQQMLOGのMessage IDとADIDを確認する。その値を長期計画管理のLTP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Long-Term Planの反映値と残存値は確認済みとして扱う。さらにSUBMIT IWA.DAILY.CNTL(DP03)のDAILYをEQQ0541Eと同種の値として併記する。
    - D. ISPF Long-Term Planning option DISPLAYが成功したためSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541Eも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 初級

    **解説:** 正答の根拠: Aは異常メッセージで EQQ0541E を読みRun DateとInput Arrivalの主値として変更結果を検証しLTP03に残します。
    内部の仕組み: 変更後の確認では長期計画表示を補助操作としLong-Term Planの反映値と残存値をRUNDATEと対象LTP03で照合します。
    誤答を含む比較: 異常メッセージと長期計画表示の役割を分けるとA: 周辺状態の後にEQQ0541Eを確認する点でLTP03を判定できます、B: 変更前のRun DateとInput Arrivalを失う点で長期計画表示の範囲を越えます、C: 監査ログと EQQMLOGの値ではEQQ0541Eを確認できないうえに追加前提も不正な点でLTP03の値を示しません、D: 補助操作の成功ではEQQ0541Eを確定できない点で変更後の確認に合いません。結論として変更後の確認の長期計画管理で判定する対象は LTP03 です。
    用語定義: 変更後の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP03へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 変更後の確認 LTP03**

    - 検証目的: 長期計画管理のLong-Term Planについて変更結果を検証し、LTP03のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP03の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP03の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP03
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP03)を指定し、LTP03の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQ0541E が画面・出力に表示されること
    ② ステップ2 の APPLICATION が画面・出力に表示されること
    ③ ステップ3 の DAILY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 引継ぎ記録 LTP09 {#c15-i0265}
*分類: 長期計画管理*  ・  難易度: 初級

引継ぎ記録では 長期計画管理 の 異常メッセージ を主操作として LTP09 を判定します。次担当者が追跡できる証跡への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP09 に残します。引継ぎ記録を補助する 長期計画表示 では RUNDATE を補助値として LTP09 へ保存します。主判定の引継ぎ記録では長期計画管理の 異常メッセージ から EQQ0541E を読み LTP09 へ残します。証跡照合の引継ぎ記録では長期計画管理の EQQ0541E と RUNDATE を LTP09 に保存します。記録対応の引継ぎ記録では長期計画管理の Run DateとInput Arrival の証跡へ LTP09 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 長期計画管理 の 異常メッセージ と 長期計画表示 を組み合わせる際は Long-Term Plan が将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データという仕組みを前提にします。空または未更新の長期計画から日次計画を作成する危険があります。EQQ0541E と Run DateとInput Arrival を対象 LTP09 で確認する組合せはどれですか。

    - A. ISPF Long-Term Planning option DISPLAYが成功したためSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541Eも正常だと推定する。主出力は保存しない。
    - B. SDSF browse SYSPRINT FIND EQQ0541Eを対象名なしで実行する。一覧の先頭行をLTP09の結果として記録する。
    - C. 対象名LTP09を指定してSDSF browse SYSPRINT FIND EQQ0541Eを実行する。応答中のEQQ0541Eと時刻を保存する。ISPF Long-Term Planning option DISPLAYで周辺状態を補完する。 ✅
    - D. 前回保存したSDSF browse SYSPRINT FIND EQQ0541Eの結果を使う。今回のISPF Long-Term Planning option DISPLAYの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 初級

    **解説:** 採用操作の理由: Cは異常メッセージで EQQ0541E を読みRun DateとInput Arrivalの主値として再現可能な記録を作成しLTP09に残します。
    製品内の仕組み: 引継ぎ記録では長期計画表示を補助操作としLong-Term Planの次担当者が追跡できる証跡をRUNDATEと対象LTP09で照合します。
    選択肢別の説明: 異常メッセージと長期計画表示の役割を分けるとA: 補助操作の成功ではEQQ0541Eを確定できない点でLTP09の値を示しません、B: 先頭行はLTP09と確定できない点で引継ぎ記録に合いません、C: EQQ0541Eと時刻を保存する点で異常メッセージに合います、D: 採取時刻が異なる点で長期計画管理に使いません。結論として引継ぎ記録の長期計画管理で判定する対象は LTP09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP09へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 引継ぎ記録 LTP09**

    - 検証目的: 長期計画管理のLong-Term Planについて再現可能な記録を作成し、LTP09のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP09の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP09の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP09
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP09)を指定し、LTP09の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQ0541E が画面・出力に表示されること
    ② ステップ2 の APPLICATION が画面・出力に表示されること
    ③ ステップ3 の DAILY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 復旧後の確認 LTP06 {#c15-i0266}
*分類: 長期計画管理*  ・  難易度: 初級

復旧後の確認では 長期計画管理 の 異常メッセージ を主操作として LTP06 を判定します。再発していないことを示す値への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP06 に残します。復旧後の確認を補助する 長期計画表示 では RUNDATE を補助値として LTP06 へ保存します。主判定の復旧後の確認では長期計画管理の 異常メッセージ から EQQ0541E を読み LTP06 へ残します。証跡照合の復旧後の確認では長期計画管理の EQQ0541E と RUNDATE を LTP06 に保存します。記録対応の復旧後の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP06 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 長期計画管理 の 異常メッセージ と 長期計画表示 を実施し Long-Term Plan の役割を確認します。空または未更新の長期計画から日次計画を作成する危険があります。対象 LTP06 の証跡を取る方法はどれですか。

    - A. 長期計画管理のRun DateとInput Arrivalを確認する。その値を長期計画管理のLTP06にも適用する。
    - B. ISPF Long-Term Planning option DISPLAYが成功したためSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541Eも正常だと推定する。主出力は保存しない。別資源で得た状態を対象LTP06へ引き継げるものとする。
    - C. SDSF browse SYSPRINT FIND EQQ0541Eを対象名なしで実行する。一覧の先頭行をLTP06の結果として記録する。
    - D. SDSF browse SYSPRINT FIND EQQ0541EでEQQ0541Eを取得してからSUBMIT IWA.DAILY.CNTL(DP06)でDAILYを照合する。LTP06のRun DateとInput Arrivalを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正答内容: Dは異常メッセージで EQQ0541E を読みRun DateとInput Arrivalの主値として復旧後の安定性を確認しLTP06に残します。
    構成上の背景: 復旧後の確認では長期計画表示を補助操作としLong-Term Planの再発していないことを示す値をRUNDATEと対象LTP06で照合します。
    候補ごとの理由: 異常メッセージと長期計画表示の役割を分けるとA: 長期計画管理の値ではEQQ0541Eを確認できない点で長期計画表示の範囲を越えます、B: 補助操作の成功ではEQQ0541Eを確定できないうえに追加前提も不正な点でLTP06の値を示しません、C: 先頭行はLTP06と確定できない点で復旧後の確認に合いません、D: EQQ0541EとDAILYを順に照合する点で異常メッセージに合います。結論として復旧後の確認の長期計画管理で判定する対象は LTP06 です。
    初出用語: 復旧後の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP06へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 復旧後の確認 LTP06**

    - 検証目的: 長期計画管理のLong-Term Planについて復旧後の安定性を確認し、LTP06のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP06の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP06の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP06
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP06)を指定し、LTP06の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の EQQ0541E が画面・出力に表示されること
    ② ステップ2 の APPLICATION が画面・出力に表示されること
    ③ ステップ3 の DAILY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 復旧準備 LTP05 {#c15-i0267}
*分類: 長期計画管理*  ・  難易度: 初級

復旧準備では 長期計画管理 の 日次計画実行 を主操作として LTP05 を判定します。再開前に必要な整合性への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP05 に残します。復旧準備を補助する 異常メッセージ では EQQ0541E を補助値として LTP05 へ保存します。主判定の復旧準備では長期計画管理の 日次計画実行 から DAILY を読み LTP05 へ残します。証跡照合の復旧準備では長期計画管理の DAILY と EQQ0541E を LTP05 に保存します。記録対応の復旧準備では長期計画管理の Run DateとInput Arrival の証跡へ LTP05 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 復旧準備で 長期計画管理 の 日次計画実行 と 異常メッセージ を使い 復旧条件を確認 します。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。DAILY を読み対象 LTP05 を切り分ける確認方法はどれですか。

    - A. 前回保存したSUBMIT IWA.DAILY.CNTL(DP05)の結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0541Eの結果と同一時点の証跡として比較する。
    - B. 保存済みのLTP05の出力を再利用する。今回のSUBMIT IWA.DAILY.CNTL(DP05)とSDSF browse SYSPRINT FIND EQQ0541Eは実行済みとして扱う。
    - C. 変更を加えずSUBMIT IWA.DAILY.CNTL(DP05)を実行する。DAILYを保存する。差分はSDSF browse SYSPRINT FIND EQQ0541Eの結果と対象名で対応させる。 ✅
    - D. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRun DateとInput Arrivalの主判定に採用する。SUBMIT IWA.DAILY.CNTL(DP05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 初級

    **解説:** 選定理由: Cは日次計画実行で DAILY を読みRun DateとInput Arrivalの主値として復旧条件を確認しLTP05に残します。
    処理の仕組み: 復旧準備では異常メッセージを補助操作としLong-Term Planの再開前に必要な整合性をEQQ0541Eと対象LTP05で照合します。
    選択結果の内訳: 日次計画実行と異常メッセージの役割を分けるとA: 採取時刻が異なる点で日次計画実行を代替しません、B: 過去出力では今回の復旧準備を示せない点で長期計画管理に使いません、C: 変更前のDAILYを保存する点で正答です、D: EQQ0541EはDAILYを代替しないうえに追加前提も不正な点でLTP05を採用できません。結論として復旧準備の長期計画管理で判定する対象は LTP05 です。
    用語の説明: 復旧準備で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP05へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 復旧準備 LTP05**

    - 検証目的: 長期計画管理のLong-Term Planについて復旧条件を確認し、LTP05のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP05)を指定し、LTP05の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP05の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP05の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP05
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DAILY が画面・出力に表示されること
    ② ステップ2 の EQQ0541E が画面・出力に表示されること
    ③ ステップ3 の APPLICATION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 構成監査 LTP08 {#c15-i0268}
*分類: 長期計画管理*  ・  難易度: 初級

構成監査では 長期計画管理 の 日次計画実行 を主操作として LTP08 を判定します。定義値と稼働値の一致への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP08 に残します。構成監査を補助する 異常メッセージ では EQQ0541E を補助値として LTP08 へ保存します。主判定の構成監査では長期計画管理の 日次計画実行 から DAILY を読み LTP08 へ残します。証跡照合の構成監査では長期計画管理の DAILY と EQQ0541E を LTP08 に保存します。記録対応の構成監査では長期計画管理の Run DateとInput Arrival の証跡へ LTP08 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 構成監査で 長期計画管理 の 日次計画実行 と 異常メッセージ を照合し 定義値と稼働値の一致 を確かめます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。DAILY を読む前に対象 LTP08 へ行う確認はどれですか。

    - A. 保存済みのLTP08の出力を再利用する。今回のSUBMIT IWA.DAILY.CNTL(DP08)とSDSF browse SYSPRINT FIND EQQ0541Eは実行済みとして扱う。
    - B. SDSF browse SYSPRINT FIND EQQ0541Eの結果だけでは確定しない。SUBMIT IWA.DAILY.CNTL(DP08)のDAILYを主証跡として構成差分を監査する。 ✅
    - C. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRun DateとInput Arrivalの主判定に採用する。SUBMIT IWA.DAILY.CNTL(DP08)の応答は採取対象から外す。
    - D. ISPF Long-Term Planning option DISPLAYのRUNDATEをDAILYと同義の成功表示として扱う。SUBMIT IWA.DAILY.CNTL(DP08)は実行しない。

    正解: **B** ／ 難易度: 初級

    **解説:** 技術上の正答: Bは日次計画実行で DAILY を読みRun DateとInput Arrivalの主値として構成差分を監査しLTP08に残します。
    実行時の背景: 構成監査では異常メッセージを補助操作としLong-Term Planの定義値と稼働値の一致をEQQ0541Eと対象LTP08で照合します。
    四つの候補の理由: 日次計画実行と異常メッセージの役割を分けるとA: 過去出力では今回の構成監査を示せない点で長期計画管理に使いません、B: DAILYを主証跡として区別する点で正答です、C: EQQ0541EはDAILYを代替しない点でLTP08を採用できません、D: RUNDATEとDAILYは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の長期計画管理で判定する対象は LTP08 です。
    初出語定義: 構成監査で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP08へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 構成監査 LTP08**

    - 検証目的: 長期計画管理のLong-Term Planについて構成差分を監査し、LTP08のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP08)を指定し、LTP08の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP08の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP08の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP08
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DAILY が画面・出力に表示されること
    ② ステップ2 の EQQ0541E が画面・出力に表示されること
    ③ ステップ3 の APPLICATION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 通常状態の確認 LTP01 {#c15-i0269}
*分類: 長期計画管理*  ・  難易度: 初級

通常状態の確認では 長期計画管理 の 長期計画表示 を主操作として LTP01 を判定します。基準値と現在値の差への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP01 に残します。通常状態の確認を補助する 日次計画実行 では DAILY を補助値として LTP01 へ保存します。主判定の通常状態の確認では長期計画管理の 長期計画表示 から RUNDATE を読み LTP01 へ残します。証跡照合の通常状態の確認では長期計画管理の RUNDATE と DAILY を LTP01 に保存します。記録対応の通常状態の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP01 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 長期計画管理 の 長期計画表示 と 日次計画実行 を用い 通常状態を確定 します。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。RUNDATE で対象 LTP01 の Run DateとInput Arrival を再現できる記録はどれですか。

    - A. SUBMIT IWA.DAILY.CNTL(DP01)のDAILYをRun DateとInput Arrivalの主判定に採用する。ISPF Long-Term Planning option DISPLAYの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRUNDATEと同義の成功表示として扱う。ISPF Long-Term Planning option DISPLAYは実行しない。
    - C. ISPF Long-Term Planning option DISPLAYを先に実行する。対象LTP01のRUNDATEをRun DateとInput Arrivalとして記録する。続いてSUBMIT IWA.DAILY.CNTL(DP01)で同一対象を照合する。 ✅
    - D. ISPF Long-Term Planning option DISPLAYが応答を返した時点で正常とする。応答中のRUNDATEの値は記録しない。

    正解: **C** ／ 難易度: 初級

    **解説:** 正解の説明: Cは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として通常状態を確定しLTP01に残します。
    背景・仕組み: 通常状態の確認では日次計画実行を補助操作としLong-Term Planの基準値と現在値の差をDAILYと対象LTP01で照合します。
    選択肢の理由: 長期計画表示と日次計画実行の役割を分けるとA: DAILYはRUNDATEを代替しないうえに追加前提も不正な点でLong-Term Planに使えません、B: EQQ0541EとRUNDATEは確認項目が異なる点でLTP01を採用できません、C: RUNDATEを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではRun DateとInput Arrivalを判定できない点で一次資料と一致しません。結論として通常状態の確認の長期計画管理で判定する対象は LTP01 です。
    用語の初出定義: 通常状態の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP01へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 通常状態の確認 LTP01**

    - 検証目的: 長期計画管理のLong-Term Planについて通常状態を確定し、LTP01のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP01の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP01
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP01)を指定し、LTP01の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP01の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
    ② ステップ2 の DAILY が画面・出力に表示されること
    ③ ステップ3 の EQQ0541E が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide



### 長期計画管理 Long-Term Plan 障害切り分け LTP04 {#c15-i0270}
*分類: 長期計画管理*  ・  難易度: 初級

障害切り分けでは 長期計画管理 の 長期計画表示 を主操作として LTP04 を判定します。最初に失敗した処理への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP04 に残します。障害切り分けを補助する 日次計画実行 では DAILY を補助値として LTP04 へ保存します。主判定の障害切り分けでは長期計画管理の 長期計画表示 から RUNDATE を読み LTP04 へ残します。証跡照合の障害切り分けでは長期計画管理の RUNDATE と DAILY を LTP04 に保存します。記録対応の障害切り分けでは長期計画管理の Run DateとInput Arrival の証跡へ LTP04 を結びます。

**出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 長期計画管理 の 長期計画表示 と 日次計画実行 の役割を分け 最初に失敗した処理 を調べます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。対象 LTP04 を誤判定しない進め方はどれですか。

    - A. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRUNDATEと同義の成功表示として扱う。ISPF Long-Term Planning option DISPLAYは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. ISPF Long-Term Planning option DISPLAYの出力でLTP04とRUNDATEが同じ応答にあることを確認する。Run DateとInput Arrivalをその応答から採取する。 ✅
    - C. ISPF Long-Term Planning option DISPLAYが応答を返した時点で正常とする。応答中のRUNDATEの値は記録しない。
    - D. ISPF Long-Term Planning option DISPLAYのコマンド文字列だけを記録する。RUNDATEを含む応答行は保存しない。

    正解: **B** ／ 難易度: 初級

    **解説:** 正しい操作の説明: Bは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として障害範囲を限定しLTP04に残します。
    技術的背景: 障害切り分けでは日次計画実行を補助操作としLong-Term Planの最初に失敗した処理をDAILYと対象LTP04で照合します。
    四択の評価: 長期計画表示と日次計画実行の役割を分けるとA: EQQ0541EとRUNDATEは確認項目が異なるうえに追加前提も不正な点でLTP04を採用できません、B: LTP04とRUNDATEを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではRun DateとInput Arrivalを判定できない点で一次資料と一致しません、D: 入力記録だけではRun DateとInput Arrivalを証明できない点でRun DateとInput Arrivalを確認できません。結論として障害切り分けの長期計画管理で判定する対象は LTP04 です。
    初出語の意味: 障害切り分けで使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP04へ適用します。

    **出典:** 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide


??? note "検証手順（1件）"
    **長期計画管理 Long-Term Plan 障害切り分け LTP04**

    - 検証目的: 長期計画管理のLong-Term Planについて障害範囲を限定し、LTP04のRun DateとInput Arrivalを実出力で確認する。
    - 前提条件: IBM Workload Automationの参照権限を持ち、対象LTP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP04の長期計画表示を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> ISPF Long-Term Planning option DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APPLICATION APP04
    RUN DATE 260716 INPUT ARRIVAL 0200
    DEADLINE 260716 0600 PRIORITY 5
    ```

    画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP04)を指定し、LTP04の日次計画実行を表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SUBMIT IWA.DAILY.CNTL(DP04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DAILY PLANNING STARTED
    CURRENT PLAN EXTENDED THROUGH 260716 2359
    RETURN CODE 0000
    ```

    画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP04の異常メッセージを表示します。
    操作（入力）:
    ```text
    IBM Workload Automation 操作画面
    COMMAND ===> SDSF browse SYSPRINT FIND EQQ0541E
    → Enter を押す
    ```

    画面・出力:
    ```text
    EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
    ```

    画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
    ② ステップ2 の DAILY が画面・出力に表示されること
    ③ ステップ3 の EQQ0541E が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide




## その他

### その他（特定項目に紐づかないQA・手順） {#c15-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? note "検証手順（1件）"
    **Current plan special resource segm**

    - 検証目的: 変更確認のレコードについて、IBM Workload Automation の レコードで扱う Current plan special resource segmentは、現在計画内で特殊資源の状態やに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。
    - セッション環境: IWA DialogでSRSTATを実行し、EQQZ045Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===> に SRSTAT を入力し、変更確認のレコードの確認表示へ進みます。
    操作（入力）:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> SRSTAT
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog)
    COMMAND INPUT ===> SRSTAT
    ```

    COMMAND INPUTにSRSTATが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIWA Dialogの表示結果です。FIND欄にCurrent plan speciを指定し、OSKB010020の対象行を見つけます。
    操作（入力）:
    ```text
    (IWA Dialog Result)
    COMMAND INPUT ===> FIND Current plan speci
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IWA Dialog Result)
    ITEM Current plan speci
    CASE OSKB010020
    SOURCE IBM Workload Automation
    ```

    Current plan speciとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010020を同じ出力で読み、変更確認のレコードの根拠を記録します。
    操作（入力）:
    ```text
    (IWA Dialog Detail)
    COMMAND INPUT ===> SRSTAT
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    IBM Z WORKLOAD SCHEDULER OSKB010020
    COMMAND ===> SRSTAT
    OPERATION OSKB010020 STATUS C
    EQQZ045I CURRENT PLAN ENTRY DISPLAYED
    ```

    EQQZ045IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SRSTAT が画面・出力に表示されること
    ② ステップ2 の Current plan speci と OSKB010020 が画面・出力に表示されること
    ③ ステップ3 の EQQZ045I と OSKB010020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler

