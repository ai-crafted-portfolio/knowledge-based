---
search:
  exclude: true
---

# IBM Workload Automation — 詳細 (6/6)

[← IBM Workload Automation の概要へ戻る](index.md)


## IBM Workload Automation > 長期計画管理

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

