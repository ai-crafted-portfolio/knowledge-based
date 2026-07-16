---
search:
  exclude: true
---

# CICS Transaction Server for z/OS 6.x — 詳細 (3/3)

[← CICS Transaction Server for z/OS 6.x の概要へ戻る](index.md)


## CICS Transaction Server for z/OS 6.x > メイン端末運用

### メイン端末運用 CEMTシステム照会 代替経路の確認 CIC10 {#c04-i0212}
*分類: メイン端末運用*  ・  難易度: 初級

代替経路の確認では メイン端末運用 の システム照会 を主操作として CIC10 を判定します。主経路との役割差への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC10 に残します。代替経路の確認を補助する 領域識別 では Applid を補助値として CIC10 へ保存します。主判定の代替経路の確認ではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC10 へ残します。証跡照合の代替経路の確認ではメイン端末運用・システム照会の STATUS と Applid を CIC10 に保存します。記録対応の代替経路の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC10 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で メイン端末運用 の システム照会 と 領域識別 を実施し CEMTシステム照会 の役割を確認します。別領域のCEMT画面で変更を実行する危険があります。対象 CIC10 の証跡を取る方法はどれですか。

    - A. CEMT INQUIRE SYSTEMのコマンド文字列だけを記録する。STATUSを含む応答行は保存しない。
    - B. CEMT INQUIRE SYSTEMとCEMT INQUIRE SYSTEM APPLIDの対象名をそろえる。前者のSTATUSをAPPLIDと領域状態の判定値として採用する。 ✅
    - C. CEMTシステム照会の停止または再定義を実施する。その後にCEMT INQUIRE SYSTEMでSTATUSを採取する。
    - D. トレースのTRACETYPEとSTATUSを確認する。その値をメイン端末運用のCIC10にも適用する。

    正解: **B** ／ 難易度: 初級

    **解説:** 正しい判定結果: Bはシステム照会で STATUS を読みAPPLIDと領域状態の主値として代替手段の成立を確認しCIC10に残します。
    運用上の背景: 代替経路の確認では領域識別を補助操作としCEMTシステム照会の主経路との役割差をApplidと対象CIC10で照合します。
    候補別の検討: システム照会と領域識別の役割を分けるとA: 入力記録だけではAPPLIDと領域状態を証明できない点で一次資料と一致しません、B: 同じ対象名のSTATUSを採用する点でCIC10を判定できます、C: 変更前のAPPLIDと領域状態を失う点で領域識別の範囲を越えます、D: トレースの値ではSTATUSを確認できない点でCIC10の値を示しません。結論として代替経路の確認のメイン端末運用・システム照会で判定する対象は CIC10 です。
    重要用語の定義: 代替経路の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC10へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 代替経路の確認 CIC10**

    - 検証目的: メイン端末運用のCEMTシステム照会について代替手段の成立を確認し、CIC10のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC10のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC10) Applid(CIC10) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC10の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC10) Cicstslevel(060200) Sysid(CIC10)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC10の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC10 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
    ② ステップ2 の Applid が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 変更前の確認 CIC02 {#c04-i0213}
*分類: メイン端末運用*  ・  難易度: 初級

変更前の確認では メイン端末運用 の 領域識別 を主操作として CIC02 を判定します。変更対象と非対象の境界への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC02 に残します。変更前の確認を補助する 統計記録 では DFHST0103I を補助値として CIC02 へ保存します。主判定の変更前の確認ではメイン端末運用・システム照会の 領域識別 から Applid を読み CIC02 へ残します。証跡照合の変更前の確認ではメイン端末運用・システム照会の Applid と DFHST0103I を CIC02 に保存します。記録対応の変更前の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC02 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更前の確認で メイン端末運用 の 領域識別 と 統計記録 の役割を分け 変更対象と非対象の境界 を調べます。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。対象 CIC02 を誤判定しない進め方はどれですか。

    - A. CEMT INQUIRE SYSTEM APPLIDを対象名なしで実行する。一覧の先頭行をCIC02の結果として記録する。
    - B. 対象CIC02についてCEMT INQUIRE SYSTEM APPLIDの応答からApplidを確認する。CEMT PERFORM STATISTICS RECORD ALLは補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したCEMT INQUIRE SYSTEM APPLIDの結果を使う。今回のCEMT PERFORM STATISTICS RECORD ALLの結果と同一時点の証跡として比較する。
    - D. 保存済みのCIC02の出力を再利用する。今回のCEMT INQUIRE SYSTEM APPLIDとCEMT PERFORM STATISTICS RECORD ALLは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 初級

    **解説:** 採用理由: Bは領域識別で Applid を読みAPPLIDと領域状態の主値として変更前の証跡を保存しCIC02に残します。
    動作の背景: 変更前の確認では統計記録を補助操作としCEMTシステム照会の変更対象と非対象の境界をDFHST0103Iと対象CIC02で照合します。
    各選択肢の検討: 領域識別と統計記録の役割を分けるとA: 先頭行はCIC02と確定できない点で変更前の確認に合いません、B: Applidと補助証跡の時刻を合わせる点で領域識別に合います、C: 採取時刻が異なる点でメイン端末運用に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でCEMTシステム照会に使えません。結論として変更前の確認のメイン端末運用・システム照会で判定する対象は CIC02 です。
    初出用語の定義: 変更前の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC02へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 変更前の確認 CIC02**

    - 検証目的: メイン端末運用のCEMTシステム照会について変更前の証跡を保存し、CIC02のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC02の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC02) Cicstslevel(060200) Sysid(CIC02)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC02の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC02 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC02のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC02) Applid(CIC02) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Applid が画面・出力に表示されること
    ② ステップ2 の DFHST0103I が画面・出力に表示されること
    ③ ステップ3 の STATUS が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 変更後の確認 CIC03 {#c04-i0214}
*分類: メイン端末運用*  ・  難易度: 初級

変更後の確認では メイン端末運用 の 統計記録 を主操作として CIC03 を判定します。反映値と残存値への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC03 に残します。変更後の確認を補助する システム照会 では STATUS を補助値として CIC03 へ保存します。主判定の変更後の確認ではメイン端末運用・システム照会の 統計記録 から DFHST0103I を読み CIC03 へ残します。証跡照合の変更後の確認ではメイン端末運用・システム照会の DFHST0103I と STATUS を CIC03 に保存します。記録対応の変更後の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC03 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更後の確認で メイン端末運用 の 統計記録 と システム照会 を使い 変更結果を検証 します。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。DFHST0103I を読み対象 CIC03 を切り分ける確認方法はどれですか。

    - A. CEMTシステム照会の停止または再定義を実施する。その後にCEMT PERFORM STATISTICS RECORD ALLでDFHST0103Iを採取する。
    - B. プログラム管理のPROGRAM名とNEWCOPY結果を確認する。その値をメイン端末運用のCIC03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。CEMTシステム照会の反映値と残存値は確認済みとして扱う。さらにCEMT INQUIRE SYSTEM APPLIDのApplidをDFHST0103Iと同種の値として併記する。
    - C. CEMT INQUIRE SYSTEMで周辺状態を押さえる。その後にCEMT PERFORM STATISTICS RECORD ALLでDFHST0103Iを確認して変更結果を検証する。 ✅
    - D. CEMT INQUIRE SYSTEMが成功したためCEMT PERFORM STATISTICS RECORD ALLのDFHST0103Iも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 初級

    **解説:** 正答の根拠: Cは統計記録で DFHST0103I を読みAPPLIDと領域状態の主値として変更結果を検証しCIC03に残します。
    内部の仕組み: 変更後の確認ではシステム照会を補助操作としCEMTシステム照会の反映値と残存値をSTATUSと対象CIC03で照合します。
    誤答を含む比較: 統計記録とシステム照会の役割を分けるとA: 変更前のAPPLIDと領域状態を失う点でAPPLIDと領域状態を確認できません、B: プログラム管理の値ではDFHST0103Iを確認できないうえに追加前提も不正な点でシステム照会の範囲を越えます、C: 周辺状態の後にDFHST0103Iを確認する点で現在値を示します、D: 補助操作の成功ではDFHST0103Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のメイン端末運用・システム照会で判定する対象は CIC03 です。
    用語定義: 変更後の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC03へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 変更後の確認 CIC03**

    - 検証目的: メイン端末運用のCEMTシステム照会について変更結果を検証し、CIC03のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC03の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC03 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC03のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC03) Applid(CIC03) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC03の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC03) Cicstslevel(060200) Sysid(CIC03)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
    ② ステップ2 の STATUS が画面・出力に表示されること
    ③ ステップ3 の Applid が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 引継ぎ記録 CIC09 {#c04-i0215}
*分類: メイン端末運用*  ・  難易度: 初級

引継ぎ記録では メイン端末運用 の 統計記録 を主操作として CIC09 を判定します。次担当者が追跡できる証跡への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC09 に残します。引継ぎ記録を補助する システム照会 では STATUS を補助値として CIC09 へ保存します。主判定の引継ぎ記録ではメイン端末運用・システム照会の 統計記録 から DFHST0103I を読み CIC09 へ残します。証跡照合の引継ぎ記録ではメイン端末運用・システム照会の DFHST0103I と STATUS を CIC09 に保存します。記録対応の引継ぎ記録ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC09 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で メイン端末運用 の 統計記録 と システム照会 を使い 再現可能な記録を作成 します。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。DFHST0103I を読み対象 CIC09 を切り分ける確認方法はどれですか。

    - A. 対象名CIC09を指定してCEMT PERFORM STATISTICS RECORD ALLを実行する。応答中のDFHST0103Iと時刻を保存する。CEMT INQUIRE SYSTEMで周辺状態を補完する。 ✅
    - B. CEMT INQUIRE SYSTEMが成功したためCEMT PERFORM STATISTICS RECORD ALLのDFHST0103Iも正常だと推定する。主出力は保存しない。
    - C. CEMT PERFORM STATISTICS RECORD ALLを対象名なしで実行する。一覧の先頭行をCIC09の結果として記録する。
    - D. 前回保存したCEMT PERFORM STATISTICS RECORD ALLの結果を使う。今回のCEMT INQUIRE SYSTEMの結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 初級

    **解説:** 採用操作の理由: Aは統計記録で DFHST0103I を読みAPPLIDと領域状態の主値として再現可能な記録を作成しCIC09に残します。
    製品内の仕組み: 引継ぎ記録ではシステム照会を補助操作としCEMTシステム照会の次担当者が追跡できる証跡をSTATUSと対象CIC09で照合します。
    選択肢別の説明: 統計記録とシステム照会の役割を分けるとA: DFHST0103Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではDFHST0103Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はCIC09と確定できない点で統計記録を代替しません、D: 採取時刻が異なる点でメイン端末運用に使いません。結論として引継ぎ記録のメイン端末運用・システム照会で判定する対象は CIC09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC09へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 引継ぎ記録 CIC09**

    - 検証目的: メイン端末運用のCEMTシステム照会について再現可能な記録を作成し、CIC09のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC09の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC09 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC09のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC09) Applid(CIC09) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC09の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC09) Cicstslevel(060200) Sysid(CIC09)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
    ② ステップ2 の STATUS が画面・出力に表示されること
    ③ ステップ3 の Applid が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 復旧後の確認 CIC06 {#c04-i0216}
*分類: メイン端末運用*  ・  難易度: 初級

復旧後の確認では メイン端末運用 の 統計記録 を主操作として CIC06 を判定します。再発していないことを示す値への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC06 に残します。復旧後の確認を補助する システム照会 では STATUS を補助値として CIC06 へ保存します。主判定の復旧後の確認ではメイン端末運用・システム照会の 統計記録 から DFHST0103I を読み CIC06 へ残します。証跡照合の復旧後の確認ではメイン端末運用・システム照会の DFHST0103I と STATUS を CIC06 に保存します。記録対応の復旧後の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC06 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で メイン端末運用 の 統計記録 と システム照会 を照合し 再発していないことを示す値 を確かめます。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。DFHST0103I を読む前に対象 CIC06 へ行う確認はどれですか。

    - A. WebサポートのUSAGEとPATHを確認する。その値をメイン端末運用のCIC06にも適用する。
    - B. CEMT PERFORM STATISTICS RECORD ALLでDFHST0103Iを取得してからCEMT INQUIRE SYSTEM APPLIDでApplidを照合する。CIC06のAPPLIDと領域状態を両出力から確定する。 ✅
    - C. CEMT INQUIRE SYSTEMが成功したためCEMT PERFORM STATISTICS RECORD ALLのDFHST0103Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象CIC06へ引き継げるものとする。CEMTシステム照会の再発していないことを示す値は確認済みとして扱う。さらにCEMT INQUIRE SYSTEM APPLIDのApplidをDFHST0103Iと同種の値として併記する。
    - D. CEMT PERFORM STATISTICS RECORD ALLを対象名なしで実行する。一覧の先頭行をCIC06の結果として記録する。

    正解: **B** ／ 難易度: 初級

    **解説:** 正答内容: Bは統計記録で DFHST0103I を読みAPPLIDと領域状態の主値として復旧後の安定性を確認しCIC06に残します。
    構成上の背景: 復旧後の確認ではシステム照会を補助操作としCEMTシステム照会の再発していないことを示す値をSTATUSと対象CIC06で照合します。
    候補ごとの理由: 統計記録とシステム照会の役割を分けるとA: Webサポートの値ではDFHST0103Iを確認できない点でシステム照会の範囲を越えます、B: DFHST0103IとApplidを順に照合する点で現在値を示します、C: 補助操作の成功ではDFHST0103Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はCIC06と確定できない点で統計記録を代替しません。結論として復旧後の確認のメイン端末運用・システム照会で判定する対象は CIC06 です。
    初出用語: 復旧後の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC06へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 復旧後の確認 CIC06**

    - 検証目的: メイン端末運用のCEMTシステム照会について復旧後の安定性を確認し、CIC06のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC06の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC06 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC06のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC06) Applid(CIC06) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC06の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC06) Cicstslevel(060200) Sysid(CIC06)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
    ② ステップ2 の STATUS が画面・出力に表示されること
    ③ ステップ3 の Applid が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 復旧準備 CIC05 {#c04-i0217}
*分類: メイン端末運用*  ・  難易度: 初級

復旧準備では メイン端末運用 の 領域識別 を主操作として CIC05 を判定します。再開前に必要な整合性への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC05 に残します。復旧準備を補助する 統計記録 では DFHST0103I を補助値として CIC05 へ保存します。主判定の復旧準備ではメイン端末運用・システム照会の 領域識別 から Applid を読み CIC05 へ残します。証跡照合の復旧準備ではメイン端末運用・システム照会の Applid と DFHST0103I を CIC05 に保存します。記録対応の復旧準備ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC05 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧準備で メイン端末運用 の 領域識別 と 統計記録 を用い 復旧条件を確認 します。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。Applid で対象 CIC05 の APPLIDと領域状態 を再現できる記録はどれですか。

    - A. 変更を加えずCEMT INQUIRE SYSTEM APPLIDを実行する。Applidを保存する。差分はCEMT PERFORM STATISTICS RECORD ALLの結果と対象名で対応させる。 ✅
    - B. 前回保存したCEMT INQUIRE SYSTEM APPLIDの結果を使う。今回のCEMT PERFORM STATISTICS RECORD ALLの結果と同一時点の証跡として比較する。
    - C. 保存済みのCIC05の出力を再利用する。今回のCEMT INQUIRE SYSTEM APPLIDとCEMT PERFORM STATISTICS RECORD ALLは実行済みとして扱う。
    - D. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをAPPLIDと領域状態の主判定に採用する。CEMT INQUIRE SYSTEM APPLIDの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 初級

    **解説:** 選定理由: Aは領域識別で Applid を読みAPPLIDと領域状態の主値として復旧条件を確認しCIC05に残します。
    処理の仕組み: 復旧準備では統計記録を補助操作としCEMTシステム照会の再開前に必要な整合性をDFHST0103Iと対象CIC05で照合します。
    選択結果の内訳: 領域識別と統計記録の役割を分けるとA: 変更前のApplidを保存する点で領域識別に合います、B: 採取時刻が異なる点でメイン端末運用に使いません、C: 過去出力では今回の復旧準備を示せない点でCEMTシステム照会に使えません、D: DFHST0103IはApplidを代替しないうえに追加前提も不正な点でCIC05を採用できません。結論として復旧準備のメイン端末運用・システム照会で判定する対象は CIC05 です。
    用語の説明: 復旧準備で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC05へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 復旧準備 CIC05**

    - 検証目的: メイン端末運用のCEMTシステム照会について復旧条件を確認し、CIC05のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC05の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC05) Cicstslevel(060200) Sysid(CIC05)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC05の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC05 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC05のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC05) Applid(CIC05) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Applid が画面・出力に表示されること
    ② ステップ2 の DFHST0103I が画面・出力に表示されること
    ③ ステップ3 の STATUS が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 構成監査 CIC08 {#c04-i0218}
*分類: メイン端末運用*  ・  難易度: 初級

構成監査では メイン端末運用 の 領域識別 を主操作として CIC08 を判定します。定義値と稼働値の一致への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC08 に残します。構成監査を補助する 統計記録 では DFHST0103I を補助値として CIC08 へ保存します。主判定の構成監査ではメイン端末運用・システム照会の 領域識別 から Applid を読み CIC08 へ残します。証跡照合の構成監査ではメイン端末運用・システム照会の Applid と DFHST0103I を CIC08 に保存します。記録対応の構成監査ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC08 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 構成監査で メイン端末運用 の 領域識別 と 統計記録 の役割を分け 定義値と稼働値の一致 を調べます。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。対象 CIC08 を誤判定しない進め方はどれですか。

    - A. 保存済みのCIC08の出力を再利用する。今回のCEMT INQUIRE SYSTEM APPLIDとCEMT PERFORM STATISTICS RECORD ALLは実行済みとして扱う。
    - B. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをAPPLIDと領域状態の主判定に採用する。CEMT INQUIRE SYSTEM APPLIDの応答は採取対象から外す。
    - C. CEMT INQUIRE SYSTEMのSTATUSをApplidと同義の成功表示として扱う。CEMT INQUIRE SYSTEM APPLIDは実行しない。
    - D. CEMT PERFORM STATISTICS RECORD ALLの結果だけでは確定しない。CEMT INQUIRE SYSTEM APPLIDのApplidを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 技術上の正答: Dは領域識別で Applid を読みAPPLIDと領域状態の主値として構成差分を監査しCIC08に残します。
    実行時の背景: 構成監査では統計記録を補助操作としCEMTシステム照会の定義値と稼働値の一致をDFHST0103Iと対象CIC08で照合します。
    四つの候補の理由: 領域識別と統計記録の役割を分けるとA: 過去出力では今回の構成監査を示せない点でメイン端末運用に使いません、B: DFHST0103IはApplidを代替しない点でCEMTシステム照会に使えません、C: STATUSとApplidは確認項目が異なる点でCIC08を採用できません、D: Applidを主証跡として区別する点で主証跡になります。結論として構成監査のメイン端末運用・システム照会で判定する対象は CIC08 です。
    初出語定義: 構成監査で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC08へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 構成監査 CIC08**

    - 検証目的: メイン端末運用のCEMTシステム照会について構成差分を監査し、CIC08のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC08の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC08) Cicstslevel(060200) Sysid(CIC08)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC08の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC08 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC08のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC08) Applid(CIC08) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Applid が画面・出力に表示されること
    ② ステップ2 の DFHST0103I が画面・出力に表示されること
    ③ ステップ3 の STATUS が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 通常状態の確認 CIC01 {#c04-i0219}
*分類: メイン端末運用*  ・  難易度: 初級

通常状態の確認では メイン端末運用 の システム照会 を主操作として CIC01 を判定します。基準値と現在値の差への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC01 に残します。通常状態の確認を補助する 領域識別 では Applid を補助値として CIC01 へ保存します。主判定の通常状態の確認ではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC01 へ残します。証跡照合の通常状態の確認ではメイン端末運用・システム照会の STATUS と Applid を CIC01 に保存します。記録対応の通常状態の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC01 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で メイン端末運用 の システム照会 と 領域識別 を組み合わせる際は CEMTシステム照会 がCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能という仕組みを前提にします。別領域のCEMT画面で変更を実行する危険があります。STATUS と APPLIDと領域状態 を対象 CIC01 で確認する組合せはどれですか。

    - A. CEMT INQUIRE SYSTEMを先に実行する。対象CIC01のSTATUSをAPPLIDと領域状態として記録する。続いてCEMT INQUIRE SYSTEM APPLIDで同一対象を照合する。 ✅
    - B. CEMT INQUIRE SYSTEM APPLIDのApplidをAPPLIDと領域状態の主判定に採用する。CEMT INQUIRE SYSTEMの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをSTATUSと同義の成功表示として扱う。CEMT INQUIRE SYSTEMは実行しない。
    - D. CEMT INQUIRE SYSTEMが応答を返した時点で正常とする。応答中のSTATUSの値は記録しない。

    正解: **A** ／ 難易度: 初級

    **解説:** 正解の説明: Aはシステム照会で STATUS を読みAPPLIDと領域状態の主値として通常状態を確定しCIC01に残します。
    背景・仕組み: 通常状態の確認では領域識別を補助操作としCEMTシステム照会の基準値と現在値の差をApplidと対象CIC01で照合します。
    選択肢の理由: システム照会と領域識別の役割を分けるとA: STATUSを主値として補助結果と照合する点で正答です、B: ApplidはSTATUSを代替しないうえに追加前提も不正な点でCIC01を採用できません、C: DFHST0103IとSTATUSは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではAPPLIDと領域状態を判定できない点で一次資料と一致しません。結論として通常状態の確認のメイン端末運用・システム照会で判定する対象は CIC01 です。
    用語の初出定義: 通常状態の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC01へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 通常状態の確認 CIC01**

    - 検証目的: メイン端末運用のCEMTシステム照会について通常状態を確定し、CIC01のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC01のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC01) Applid(CIC01) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC01の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC01) Cicstslevel(060200) Sysid(CIC01)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC01の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC01 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
    ② ステップ2 の Applid が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 障害切り分け CIC04 {#c04-i0220}
*分類: メイン端末運用*  ・  難易度: 初級

障害切り分けでは メイン端末運用 の システム照会 を主操作として CIC04 を判定します。最初に失敗した処理への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC04 に残します。障害切り分けを補助する 領域識別 では Applid を補助値として CIC04 へ保存します。主判定の障害切り分けではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC04 へ残します。証跡照合の障害切り分けではメイン端末運用・システム照会の STATUS と Applid を CIC04 に保存します。記録対応の障害切り分けではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC04 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 障害切り分けで メイン端末運用 の システム照会 と 領域識別 を実施し CEMTシステム照会 の役割を確認します。別領域のCEMT画面で変更を実行する危険があります。対象 CIC04 の証跡を取る方法はどれですか。

    - A. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをSTATUSと同義の成功表示として扱う。CEMT INQUIRE SYSTEMは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. CEMT INQUIRE SYSTEMが応答を返した時点で正常とする。応答中のSTATUSの値は記録しない。
    - C. CEMT INQUIRE SYSTEMのコマンド文字列だけを記録する。STATUSを含む応答行は保存しない。
    - D. CEMT INQUIRE SYSTEMの出力でCIC04とSTATUSが同じ応答にあることを確認する。APPLIDと領域状態をその応答から採取する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正しい操作の説明: Dはシステム照会で STATUS を読みAPPLIDと領域状態の主値として障害範囲を限定しCIC04に残します。
    技術的背景: 障害切り分けでは領域識別を補助操作としCEMTシステム照会の最初に失敗した処理をApplidと対象CIC04で照合します。
    四択の評価: システム照会と領域識別の役割を分けるとA: DFHST0103IとSTATUSは確認項目が異なるうえに追加前提も不正な点でCIC04を採用できません、B: 応答の有無だけではAPPLIDと領域状態を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではAPPLIDと領域状態を証明できない点で一次資料と一致しません、D: CIC04とSTATUSを同じ応答で結ぶ点でCIC04を判定できます。結論として障害切り分けのメイン端末運用・システム照会で判定する対象は CIC04 です。
    初出語の意味: 障害切り分けで使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC04へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 障害切り分け CIC04**

    - 検証目的: メイン端末運用のCEMTシステム照会について障害範囲を限定し、CIC04のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC04のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC04) Applid(CIC04) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC04の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC04) Cicstslevel(060200) Sysid(CIC04)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC04の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC04 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
    ② ステップ2 の Applid が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf




## CICS Transaction Server for z/OS 6.x > リソース定義

### CEDA {#c04-i0221}
*分類: リソース定義*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の リソース定義で扱うCEDAは、CICS リソース定義をオンラインで追加、変更、インストールするためのトランザクションです。プログラム、ファイル、トランザクションなどをグループ単位で扱います。変更時は定義の保存とリージョンへの反映を分けて確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 上書確認のリソース定義でトランザクション管理の運用確認を行います。CEDA の根拠にできる作業はどれですか。

    - A. CICS TS と無関係な一覧で上書確認のリソース定義を確認した扱いにする。
    - B. DFH4200A の有無を確認せず上書確認のリソース定義を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 ✅
    - D. CEDA の属性行を読まず上書確認のリソース定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 初級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では CEDA は「CICS TS で CEDA の扱いを記録する上書確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では CEDA の表示結果と DFH4200A を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では CEDA の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **CEDA**

    - 検証目的: 上書確認のリソース定義について、CICS Transaction Server for z/OS 6.x の リソース定義で扱う CEDA は、CICS リソース定義をオンラインで追加、変更、インストールするに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、上書確認のリソース定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCEDAを指定し、OSKB010007の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CEDA
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CEDA
    CASE OSKB010007
    SOURCE CICS TS
    ```

    CEDAとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010007を同じ出力で読み、上書確認のリソース定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010007
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010007
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A CEDA RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の CEDA と OSKB010007 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### CEDA DEFINE TRANSACTION 実行条件確認 完了コード {#c04-i0222}
*分類: リソース定義*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEDA DEFINE TRANSACTION 実行条件確認 完了コード」は、TRANSACTIONリソースをCSDに定義し、プログラムやプロファイルと結び付けるRDO操作を実行条件確認の観点で確認する技術項目です。URIMAP 行とJVMSRV07を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEDA DEFINE TRANSACTION 実行条件確認 完了コード**

    - 検証目的: リソース定義におけるCEDA DEFINE TRANSACTIONの実行条件確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=JVMSRV07
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CETR
    → Enter を押す
    ```

    画面・出力:
    ```text
    CETR CICS TRACE CONTROL
    MAIN SYSTEM TRACE FLAG ==> OFF
    AUXILIARY TRACE STATUS ==> STARTED
    ```

    画面・出力には CETR が含まれ、CETRを確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> VERBX DFHPD760 'TR=1'
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHPD760 CICS TRACE FORMATTER
    TRACE ENTRIES SELECTED FOR APPLID CIC27
    RETURN CODE = 0000
    ```

    画面・出力には DFHPD760 が含まれ、DFHPD760を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> SUBMIT CICS.DFHTU760.CNTL(TRACE)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHTU760 AUXILIARY TRACE PRINT UTILITY
    ABBREVIATED TRACE PRINTED
    RETURN CODE = 0000
    ```

    画面・出力には DFHTU760 が含まれ、DFHTU760を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CETR が画面・出力に表示されること
    ② ステップ2 の DFHPD760 が画面・出力に表示されること
    ③ ステップ3 の DFHTU760 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEDA INSTALL GROUP 定義確認 資料見出し {#c04-i0223}
*分類: リソース定義*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEDA INSTALL GROUP 定義確認 資料見出し」は、CSDグループ内の定義を稼働リージョンへインストールするRDO操作を定義確認の観点で確認する技術項目です。TCPIPSERVICE 行とDFH041を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、未インストール定義の採用を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEDA INSTALL GROUP 定義確認 資料見出し**

    - 検証目的: リソース定義におけるCEDA INSTALL GROUPの定義確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=DFH041
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TASK
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0000140) Tra(PAY041) Sus Tas Pri(001) Sta(U) Use(USR041)
    Uow(C9D5F2EE2DEE0040) Hty(SOCKET) Hva(RECEIVE) Bac Wai
    ```

    画面・出力には PAY041 が含まれ、PAY041を確認し、未インストール定義の採用を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TRANSACTION(PAY041)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tra(PAY041) Pri(001) Pro(DFH041) Ena Sta Pro Ena Resc(DFHPROF)
    ```

    画面・出力には PAY041 が含まれ、PAY041を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(DFH041)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Pro(DFH041) Leng(0001234) Resc(0001) Ced Ena Pri Dplsubsys(CICS)
    ```

    画面・出力には DFH041 が含まれ、DFH041を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の PAY041 が画面・出力に表示されること
    ② ステップ2 の PAY041 が画面・出力に表示されること
    ③ ステップ3 の DFH041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT {#c04-i0224}
*分類: リソース定義*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の リソース定義で扱うCEMTは、CICS の稼働中リソース状態を表示、変更するためのマスター端末トランザクションです。タスク、ファイル、プログラム、端末などの状態確認に使います。緊急対応では変更操作の影響範囲と監査記録を確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 出力確認のリソース定義に関する CEMT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず出力確認のリソース定義の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認のリソース定義の証跡として保存して根拠にする。
    - C. CEMT の変更点を出力本文から切り離して出力確認のリソース定義の承認欄のみ残す。
    - D. CICS TS の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では CEMT は「CEMT の状態と出力メッセージを結び付ける出力確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では CEMT の出力行と DFH4200A を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では CEMT を CICS TS の確認記録に残し、対象名は出力確認対象です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **CEMT**

    - 検証目的: 出力確認のリソース定義について、CICS Transaction Server for z/OS 6.x の リソース定義で扱う CEMT は、CICS の稼働中リソース状態を表示、変更するためのマスター端末に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、出力確認のリソース定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCEMTを指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CEMT
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CEMT
    CASE OSKB010008
    SOURCE CICS TS
    ```

    CEMTとOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010008を同じ出力で読み、出力確認のリソース定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010008
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A CEMT RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の CEMT と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### CEMT INQUIRE PROGRAM ダンプ確認 サンプル採取 {#c04-i0225}
*分類: リソース定義*  ・  難易度: 上級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEMT INQUIRE PROGRAM ダンプ確認 サンプル採取」は、PROGRAMリソースのロード状態、使用属性、インストール属性を確認するメイン端末コマンドをダンプ確認の観点で確認する技術項目です。MAX/CUR 欄と00192を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT INQUIRE PROGRAM ダンプ確認 サンプル採取**

    - 検証目的: リソース定義におけるCEMT INQUIRE PROGRAMのダンプ確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=00192
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TCPIPSERVICE(TCP03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcp(TCP03) Ope Por(08080) Pro(Http) Backlog(00050) Urm(DFHWBAAX)
    ```

    画面・出力には TCP03 が含まれ、TCP03を確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET TCPIPSERVICE(TCP03) OPEN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcp(TCP03) Ope Por(08080) Pro(Http) Backlog(00050)
    ```

    画面・出力には TCP03 が含まれ、TCP03を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TCPIP
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcpip Open ActSockets(000012) ActSslTcbs(000002)
    ```

    画面・出力には Tcpip が含まれ、Tcpipを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の TCP03 が画面・出力に表示されること
    ② ステップ2 の TCP03 が画面・出力に表示されること
    ③ ステップ3 の Tcpip が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT INQUIRE TRANSACTION 定義確認 詳細表示 {#c04-i0226}
*分類: リソース定義*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEMT INQUIRE TRANSACTION 定義確認 詳細表示」は、トランザクション定義、利用可否、プロファイル、実行属性を確認するメイン端末コマンドを定義確認の観点で確認する技術項目です。TCB 欄とFILE002を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT INQUIRE TRANSACTION 定義確認 詳細表示**

    - 検証目的: リソース定義におけるCEMT INQUIRE TRANSACTIONの定義確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=FILE002
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE002)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE002) Vsa Ope Ena Rea Upd Add Bro Del Sha
    ```

    画面・出力には FILE002 が含まれ、FILE002を確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET FILE(FILE002) CLOSED ENABLED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE002) Clo Ena Rea Upd Add Bro Del
    ```

    画面・出力には FILE002 が含まれ、FILE002を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE002)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE002) Clo Ena Rea Upd Add Bro Del
    ```

    画面・出力には FILE002 が含まれ、FILE002を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の FILE002 が画面・出力に表示されること
    ② ステップ2 の FILE002 が画面・出力に表示されること
    ③ ステップ3 の FILE002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CMCI resource table 戻りコード確認 ページング状態 {#c04-i0227}
*分類: リソース定義*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CMCI resource table 戻りコード確認 ページング状態」は、CICS定義や稼働リソースをAPI/WUI/Management Client Interfaceで扱う表を戻りコード確認の観点で確認する技術項目です。FILE 欄とDB2C08を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、TCP/IPサービス状態の見落としを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CMCI resource table 戻りコード確認 ページング状態**

    - 検証目的: リソース定義におけるCMCI resource tableの戻りコード確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=DB2C08
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> view server.xml
    → Enter を押す
    ```

    画面・出力:
    ```text
    <featureManager><feature>jdbc-4.2</feature></featureManager>
    <dataSource jndiName="jdbc/defaultCICSDataSource">
    ```

    画面・出力には featureManager が含まれ、featureManagerを確認し、TCP/IPサービス状態の見落としを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE JVMSERVER(JVMSRV08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Jvm(JVMSRV08) Ena Sta Ope Profile(DFHWLP)
    ```

    画面・出力には JVMSRV08 が含まれ、JVMSRV08を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE DB2CONN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Db2conn Connected Db2id(DSN0) TcbLimit(0008) Comthread(0004)
    ```

    画面・出力には Db2conn が含まれ、Db2connを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の featureManager が画面・出力に表示されること
    ② ステップ2 の JVMSRV08 が画面・出力に表示されること
    ③ ステップ3 の Db2conn が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CSD {#c04-i0228}
*分類: リソース定義*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の リソース定義で扱うCSDは、CICS System Definition データセットとしてリソース定義を保持するデータセットです。CEDA などで管理する定義の保管先になり、グループやリストの単位でリージョンへ反映されます。移行時は CSD の内容と起動時のリスト指定を確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 条件確認のリソース定義に関係する CSD の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 ✅
    - B. CSD の名称と担当者名のみを残して条件確認のリソース定義の表示本文を確認対象に含めない。
    - C. トランザクション管理以外の画面で条件確認のリソース定義を確認し同じ証跡として扱ったことにする。
    - D. DFH4200A の有無を見ず条件確認のリソース定義の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では CSD は「CSD の用途をトランザクション管理の表示で確認する条件確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では CICS TS の CSD と DFH4200A を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では CSD を CICS Transaction Server for z/OS 6.xで扱う確認対象とし、用語名は条件確認用語です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **CSD**

    - 検証目的: 条件確認のリソース定義について、CICS Transaction Server for z/OS 6.x の リソース定義で扱う CSD は、CICS System Definition データセットとしてリに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、条件確認のリソース定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCSDを指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CSD
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CSD
    CASE OSKB010009
    SOURCE CICS TS
    ```

    CSDとOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010009を同じ出力で読み、条件確認のリソース定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010009
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A CSD RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の CSD と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### DB2CONN resource トレース確認 再読込 {#c04-i0229}
*分類: リソース定義*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「DB2CONN resource トレース確認 再読込」は、CICSとDb2の接続属性を管理し、JDBC type 2接続にも使われるリソースをトレース確認の観点で確認する技術項目です。PROGRAM 欄とTCP15を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **DB2CONN resource トレース確認 再読込**

    - 検証目的: リソース定義におけるDB2CONN resourceのトレース確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=TCP15
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE TCPIPSERVICE(TCP15) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF TCPIPSERVICE(TCP15) GROUP(TEST)
    PROTOCOL ==> HTTP
    PORTNUMBER ==> 08080
    URM ==> DFHWBAAX
    ```

    画面・出力には CEDA が含まれ、CEDAを確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE URIMAP(URI15) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF URIMAP(URI15) GROUP(TEST)
    PATH ==> /pay/015
    TRANSACTION ==> CWBA
    ```

    画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA INSTALL GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    INSTALL SUCCESSFUL FOR GROUP TEST
    TCPIPSERVICE TCP15 INSTALLED
    URIMAP URI15 INSTALLED
    ```

    画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
    ② ステップ2 の CEDA が画面・出力に表示されること
    ③ ステップ3 の INSTALL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### DFHDU dump utility 定義確認 保存場所 {#c04-i0230}
*分類: リソース定義*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「DFHDU dump utility 定義確認 保存場所」は、トランザクションダンプを整形し、該当タスクのトレースも確認するCICSダンプユーティリティを定義確認の観点で確認する技術項目です。DFH メッセージとPAY080を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Db2接続前提の欠落を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **DFHDU dump utility 定義確認 保存場所**

    - 検証目的: リソース定義におけるDFHDU dump utilityの定義確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=PAY080
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> Open Tasks view for CIC40
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tasks view APPLID CIC40
    Task 0051988 Transaction CWXN Status Suspended Wait RECEIVE
    ```

    画面・出力には Tasks が含まれ、Tasksを確認し、Db2接続前提の欠落を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> GET CICSDefinitionTCPIPService TCP20
    → Enter を押す
    ```

    画面・出力:
    ```text
    <response><TCPIPSERVICE name="TCP20" status="OPEN" port="8080" protocol="HTTP" /></response>
    ```

    画面・出力には response が含まれ、responseを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> GET CICSDefinitionTransaction PAY080
    → Enter を押す
    ```

    画面・出力:
    ```text
    <response><TRANSACTION name="PAY080" program="DFH080" status="ENABLED" /></response>
    ```

    画面・出力には response が含まれ、responseを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の Tasks が画面・出力に表示されること
    ② ステップ2 の response が画面・出力に表示されること
    ③ ステップ3 の response が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### DFHTR0130 トレース確認 待機状態 {#c04-i0231}
*分類: リソース定義*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「DFHTR0130 トレース確認 待機状態」は、CICS内部トレース開始を示すDFHメッセージをトレース確認の観点で確認する技術項目です。PORTNUMBER 欄とCIC14を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、タスク待機理由の誤読を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **DFHTR0130 トレース確認 待機状態**

    - 検証目的: リソース定義におけるDFHTR0130のトレース確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC14
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE TRANSACTION(PAY054) GROUP(TEST) PROGRAM(DFH054)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF TRANSACTION(PAY054) GROUP(TEST)
    PROGRAM ==> DFH054
    PROFILE ==> DFHCICST
    ```

    画面・出力には CEDA が含まれ、CEDAを確認し、タスク待機理由の誤読を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE PROGRAM(DFH054) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF PROGRAM(DFH054) GROUP(TEST)
    LANGUAGE ==> COBOL
    STATUS ==> ENABLED
    ```

    画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA INSTALL GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    INSTALL SUCCESSFUL FOR GROUP TEST
    TRANSACTION PAY054 INSTALLED
    PROGRAM DFH054 INSTALLED
    ```

    画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
    ② ステップ2 の CEDA が画面・出力に表示されること
    ③ ステップ3 の INSTALL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 ログとの照合 GRP07 {#c04-i0232}
*分類: リソース定義*  ・  難易度: 初級

ログとの照合では リソース定義 の グループ表示 を主操作として GRP07 を判定します。時刻と対象識別子への注意として「別グループの同名資源をインストールする危険があります」を GRP07 に残します。ログとの照合を補助する 定義検査 では DFHED1101 を補助値として GRP07 へ保存します。主判定のログとの照合ではリソース定義・資源定義の グループ表示 から GROUP を読み GRP07 へ残します。証跡照合のログとの照合ではリソース定義・資源定義の GROUP と DFHED1101 を GRP07 に保存します。記録対応のログとの照合ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP07 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** ログとの照合で リソース定義 の グループ表示 と 定義検査 を用い 操作とログを対応 します。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。GROUP で対象 GRP07 の グループ名とインストール結果 を再現できる記録はどれですか。

    - A. GROUPを含むグループ表示の応答行を保存する。その応答を得るためCEDA DISPLAY GROUP(GRP07)を使用する。対象GRP07のグループ名とインストール結果として記録する。 ✅
    - B. CEDA DISPLAY GROUP(GRP07)が応答を返した時点で正常とする。応答中のGROUPの値は記録しない。DFHED1102をGROUPと同じ判定値とみなし対象GRP07の主証跡にする。
    - C. CEDA DISPLAY GROUP(GRP07)のコマンド文字列だけを記録する。GROUPを含む応答行は保存しない。
    - D. CEDA資源定義の停止または再定義を実施する。その後にCEDA DISPLAY GROUP(GRP07)でGROUPを採取する。

    正解: **A** ／ 難易度: 初級

    **解説:** 適切な判定: Aはグループ表示で GROUP を読みグループ名とインストール結果の主値として操作とログを対応しGRP07に残します。
    機能の仕組み: ログとの照合では定義検査を補助操作としCEDA資源定義の時刻と対象識別子をDFHED1101と対象GRP07で照合します。
    各候補の評価: グループ表示と定義検査の役割を分けるとA: GROUPの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではグループ名とインストール結果を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではグループ名とインストール結果を証明できない点でグループ名とインストール結果を確認できません、D: 変更前のグループ名とインストール結果を失う点で定義検査の範囲を越えます。結論としてログとの照合のリソース定義・資源定義で判定する対象は GRP07 です。
    用語の定義: ログとの照合で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP07へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 ログとの照合 GRP07**

    - 検証目的: リソース定義のCEDA資源定義について操作とログを対応し、GRP07のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP07)を指定し、GRP07のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP07)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP07)を指定し、GRP07の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP07 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP07)を指定し、GRP07のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP07 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
    ② ステップ2 の DFHED1101 が画面・出力に表示されること
    ③ ステップ3 の DFHED1102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 代替経路の確認 GRP10 {#c04-i0233}
*分類: リソース定義*  ・  難易度: 初級

代替経路の確認では リソース定義 の グループ表示 を主操作として GRP10 を判定します。主経路との役割差への注意として「別グループの同名資源をインストールする危険があります」を GRP10 に残します。代替経路の確認を補助する 定義検査 では DFHED1101 を補助値として GRP10 へ保存します。主判定の代替経路の確認ではリソース定義・資源定義の グループ表示 から GROUP を読み GRP10 へ残します。証跡照合の代替経路の確認ではリソース定義・資源定義の GROUP と DFHED1101 を GRP10 に保存します。記録対応の代替経路の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP10 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で リソース定義 の グループ表示 と 定義検査 の役割を分け 主経路との役割差 を調べます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。対象 GRP10 を誤判定しない進め方はどれですか。

    - A. CEDA DISPLAY GROUP(GRP10)のコマンド文字列だけを記録する。GROUPを含む応答行は保存しない。
    - B. CEDA資源定義の停止または再定義を実施する。その後にCEDA DISPLAY GROUP(GRP10)でGROUPを採取する。
    - C. Liberty JVMのJVMSTATUSとPROFILEを確認する。その値をリソース定義のGRP10にも適用する。
    - D. CEDA DISPLAY GROUP(GRP10)とCEDA CHECK GROUP(GRP10)の対象名をそろえる。前者のGROUPをグループ名とインストール結果の判定値として採用する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正しい判定結果: Dはグループ表示で GROUP を読みグループ名とインストール結果の主値として代替手段の成立を確認しGRP10に残します。
    運用上の背景: 代替経路の確認では定義検査を補助操作としCEDA資源定義の主経路との役割差をDFHED1101と対象GRP10で照合します。
    候補別の検討: グループ表示と定義検査の役割を分けるとA: 入力記録だけではグループ名とインストール結果を証明できない点で一次資料と一致しません、B: 変更前のグループ名とインストール結果を失う点でグループ名とインストール結果を確認できません、C: Liberty JVMの値ではGROUPを確認できない点で定義検査の範囲を越えます、D: 同じ対象名のGROUPを採用する点で現在値を示します。結論として代替経路の確認のリソース定義・資源定義で判定する対象は GRP10 です。
    重要用語の定義: 代替経路の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP10へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 代替経路の確認 GRP10**

    - 検証目的: リソース定義のCEDA資源定義について代替手段の成立を確認し、GRP10のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP10)を指定し、GRP10のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP10)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP10)を指定し、GRP10の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP10 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP10)を指定し、GRP10のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP10 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
    ② ステップ2 の DFHED1101 が画面・出力に表示されること
    ③ ステップ3 の DFHED1102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 変更前の確認 GRP02 {#c04-i0234}
*分類: リソース定義*  ・  難易度: 初級

変更前の確認では リソース定義 の 定義検査 を主操作として GRP02 を判定します。変更対象と非対象の境界への注意として「別グループの同名資源をインストールする危険があります」を GRP02 に残します。変更前の確認を補助する グループ導入 では DFHED1102 を補助値として GRP02 へ保存します。主判定の変更前の確認ではリソース定義・資源定義の 定義検査 から DFHED1101 を読み GRP02 へ残します。証跡照合の変更前の確認ではリソース定義・資源定義の DFHED1101 と DFHED1102 を GRP02 に保存します。記録対応の変更前の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP02 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更前の確認で リソース定義 の 定義検査 と グループ導入 を照合し 変更対象と非対象の境界 を確かめます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。DFHED1101 を読む前に対象 GRP02 へ行う確認はどれですか。

    - A. CEDA CHECK GROUP(GRP02)を対象名なしで実行する。一覧の先頭行をGRP02の結果として記録する。
    - B. 前回保存したCEDA CHECK GROUP(GRP02)の結果を使う。今回のCEDA INSTALL GROUP(GRP02)の結果と同一時点の証跡として比較する。
    - C. 保存済みのGRP02の出力を再利用する。今回のCEDA CHECK GROUP(GRP02)とCEDA INSTALL GROUP(GRP02)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象GRP02についてCEDA CHECK GROUP(GRP02)の応答からDFHED1101を確認する。CEDA INSTALL GROUP(GRP02)は補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 採用理由: Dは定義検査で DFHED1101 を読みグループ名とインストール結果の主値として変更前の証跡を保存しGRP02に残します。
    動作の背景: 変更前の確認ではグループ導入を補助操作としCEDA資源定義の変更対象と非対象の境界をDFHED1102と対象GRP02で照合します。
    各選択肢の検討: 定義検査とグループ導入の役割を分けるとA: 先頭行はGRP02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で定義検査を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でリソース定義に使いません、D: DFHED1101と補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のリソース定義・資源定義で判定する対象は GRP02 です。
    初出用語の定義: 変更前の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP02へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 変更前の確認 GRP02**

    - 検証目的: リソース定義のCEDA資源定義について変更前の証跡を保存し、GRP02のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP02)を指定し、GRP02の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP02 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP02)を指定し、GRP02のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP02 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP02)を指定し、GRP02のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP02)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHED1101 が画面・出力に表示されること
    ② ステップ2 の DFHED1102 が画面・出力に表示されること
    ③ ステップ3 の GROUP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 変更後の確認 GRP03 {#c04-i0235}
*分類: リソース定義*  ・  難易度: 初級

変更後の確認では リソース定義 の グループ導入 を主操作として GRP03 を判定します。反映値と残存値への注意として「別グループの同名資源をインストールする危険があります」を GRP03 に残します。変更後の確認を補助する グループ表示 では GROUP を補助値として GRP03 へ保存します。主判定の変更後の確認ではリソース定義・資源定義の グループ導入 から DFHED1102 を読み GRP03 へ残します。証跡照合の変更後の確認ではリソース定義・資源定義の DFHED1102 と GROUP を GRP03 に保存します。記録対応の変更後の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP03 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更後の確認で リソース定義 の グループ導入 と グループ表示 を組み合わせる際は CEDA資源定義 がCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能という仕組みを前提にします。別グループの同名資源をインストールする危険があります。DFHED1102 と グループ名とインストール結果 を対象 GRP03 で確認する組合せはどれですか。

    - A. CEDA DISPLAY GROUP(GRP03)で周辺状態を押さえる。その後にCEDA INSTALL GROUP(GRP03)でDFHED1102を確認して変更結果を検証する。 ✅
    - B. CEDA資源定義の停止または再定義を実施する。その後にCEDA INSTALL GROUP(GRP03)でDFHED1102を採取する。
    - C. メイン端末運用のAPPLIDと領域状態を確認する。その値をリソース定義のGRP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。CEDA資源定義の反映値と残存値は確認済みとして扱う。さらにCEDA CHECK GROUP(GRP03)のDFHED1101をDFHED1102と同種の値として併記する。
    - D. CEDA DISPLAY GROUP(GRP03)が成功したためCEDA INSTALL GROUP(GRP03)のDFHED1102も正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 初級

    **解説:** 正答の根拠: Aはグループ導入で DFHED1102 を読みグループ名とインストール結果の主値として変更結果を検証しGRP03に残します。
    内部の仕組み: 変更後の確認ではグループ表示を補助操作としCEDA資源定義の反映値と残存値をGROUPと対象GRP03で照合します。
    誤答を含む比較: グループ導入とグループ表示の役割を分けるとA: 周辺状態の後にDFHED1102を確認する点でGRP03を判定できます、B: 変更前のグループ名とインストール結果を失う点でグループ表示の範囲を越えます、C: メイン端末運用の値ではDFHED1102を確認できないうえに追加前提も不正な点でGRP03の値を示しません、D: 補助操作の成功ではDFHED1102を確定できない点で変更後の確認に合いません。結論として変更後の確認のリソース定義・資源定義で判定する対象は GRP03 です。
    用語定義: 変更後の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP03へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 変更後の確認 GRP03**

    - 検証目的: リソース定義のCEDA資源定義について変更結果を検証し、GRP03のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP03)を指定し、GRP03のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP03 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP03)を指定し、GRP03のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP03)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP03)を指定し、GRP03の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP03 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHED1102 が画面・出力に表示されること
    ② ステップ2 の GROUP が画面・出力に表示されること
    ③ ステップ3 の DFHED1101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 引継ぎ記録 GRP09 {#c04-i0236}
*分類: リソース定義*  ・  難易度: 初級

引継ぎ記録では リソース定義 の グループ導入 を主操作として GRP09 を判定します。次担当者が追跡できる証跡への注意として「別グループの同名資源をインストールする危険があります」を GRP09 に残します。引継ぎ記録を補助する グループ表示 では GROUP を補助値として GRP09 へ保存します。主判定の引継ぎ記録ではリソース定義・資源定義の グループ導入 から DFHED1102 を読み GRP09 へ残します。証跡照合の引継ぎ記録ではリソース定義・資源定義の DFHED1102 と GROUP を GRP09 に保存します。記録対応の引継ぎ記録ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP09 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で リソース定義 の グループ導入 と グループ表示 を組み合わせる際は CEDA資源定義 がCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能という仕組みを前提にします。別グループの同名資源をインストールする危険があります。DFHED1102 と グループ名とインストール結果 を対象 GRP09 で確認する組合せはどれですか。

    - A. CEDA DISPLAY GROUP(GRP09)が成功したためCEDA INSTALL GROUP(GRP09)のDFHED1102も正常だと推定する。主出力は保存しない。
    - B. CEDA INSTALL GROUP(GRP09)を対象名なしで実行する。一覧の先頭行をGRP09の結果として記録する。
    - C. 対象名GRP09を指定してCEDA INSTALL GROUP(GRP09)を実行する。応答中のDFHED1102と時刻を保存する。CEDA DISPLAY GROUP(GRP09)で周辺状態を補完する。 ✅
    - D. 前回保存したCEDA INSTALL GROUP(GRP09)の結果を使う。今回のCEDA DISPLAY GROUP(GRP09)の結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 初級

    **解説:** 採用操作の理由: Cはグループ導入で DFHED1102 を読みグループ名とインストール結果の主値として再現可能な記録を作成しGRP09に残します。
    製品内の仕組み: 引継ぎ記録ではグループ表示を補助操作としCEDA資源定義の次担当者が追跡できる証跡をGROUPと対象GRP09で照合します。
    選択肢別の説明: グループ導入とグループ表示の役割を分けるとA: 補助操作の成功ではDFHED1102を確定できない点でGRP09の値を示しません、B: 先頭行はGRP09と確定できない点で引継ぎ記録に合いません、C: DFHED1102と時刻を保存する点でグループ導入に合います、D: 採取時刻が異なる点でリソース定義に使いません。結論として引継ぎ記録のリソース定義・資源定義で判定する対象は GRP09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP09へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 引継ぎ記録 GRP09**

    - 検証目的: リソース定義のCEDA資源定義について再現可能な記録を作成し、GRP09のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP09)を指定し、GRP09のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP09 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP09)を指定し、GRP09のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP09)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP09)を指定し、GRP09の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP09 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHED1102 が画面・出力に表示されること
    ② ステップ2 の GROUP が画面・出力に表示されること
    ③ ステップ3 の DFHED1101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 復旧後の確認 GRP06 {#c04-i0237}
*分類: リソース定義*  ・  難易度: 初級

復旧後の確認では リソース定義 の グループ導入 を主操作として GRP06 を判定します。再発していないことを示す値への注意として「別グループの同名資源をインストールする危険があります」を GRP06 に残します。復旧後の確認を補助する グループ表示 では GROUP を補助値として GRP06 へ保存します。主判定の復旧後の確認ではリソース定義・資源定義の グループ導入 から DFHED1102 を読み GRP06 へ残します。証跡照合の復旧後の確認ではリソース定義・資源定義の DFHED1102 と GROUP を GRP06 に保存します。記録対応の復旧後の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP06 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で リソース定義 の グループ導入 と グループ表示 を実施し CEDA資源定義 の役割を確認します。別グループの同名資源をインストールする危険があります。対象 GRP06 の証跡を取る方法はどれですか。

    - A. プログラム管理のPROGRAM名とNEWCOPY結果を確認する。その値をリソース定義のGRP06にも適用する。
    - B. CEDA DISPLAY GROUP(GRP06)が成功したためCEDA INSTALL GROUP(GRP06)のDFHED1102も正常だと推定する。主出力は保存しない。別資源で得た状態を対象GRP06へ引き継げるものとする。
    - C. CEDA INSTALL GROUP(GRP06)を対象名なしで実行する。一覧の先頭行をGRP06の結果として記録する。
    - D. CEDA INSTALL GROUP(GRP06)でDFHED1102を取得してからCEDA CHECK GROUP(GRP06)でDFHED1101を照合する。GRP06のグループ名とインストール結果を両出力から確定する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正答内容: Dはグループ導入で DFHED1102 を読みグループ名とインストール結果の主値として復旧後の安定性を確認しGRP06に残します。
    構成上の背景: 復旧後の確認ではグループ表示を補助操作としCEDA資源定義の再発していないことを示す値をGROUPと対象GRP06で照合します。
    候補ごとの理由: グループ導入とグループ表示の役割を分けるとA: プログラム管理の値ではDFHED1102を確認できない点でグループ表示の範囲を越えます、B: 補助操作の成功ではDFHED1102を確定できないうえに追加前提も不正な点でGRP06の値を示しません、C: 先頭行はGRP06と確定できない点で復旧後の確認に合いません、D: DFHED1102とDFHED1101を順に照合する点でグループ導入に合います。結論として復旧後の確認のリソース定義・資源定義で判定する対象は GRP06 です。
    初出用語: 復旧後の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP06へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 復旧後の確認 GRP06**

    - 検証目的: リソース定義のCEDA資源定義について復旧後の安定性を確認し、GRP06のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP06)を指定し、GRP06のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP06 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP06)を指定し、GRP06のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP06)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP06)を指定し、GRP06の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP06 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHED1102 が画面・出力に表示されること
    ② ステップ2 の GROUP が画面・出力に表示されること
    ③ ステップ3 の DFHED1101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 復旧準備 GRP05 {#c04-i0238}
*分類: リソース定義*  ・  難易度: 初級

復旧準備では リソース定義 の 定義検査 を主操作として GRP05 を判定します。再開前に必要な整合性への注意として「別グループの同名資源をインストールする危険があります」を GRP05 に残します。復旧準備を補助する グループ導入 では DFHED1102 を補助値として GRP05 へ保存します。主判定の復旧準備ではリソース定義・資源定義の 定義検査 から DFHED1101 を読み GRP05 へ残します。証跡照合の復旧準備ではリソース定義・資源定義の DFHED1101 と DFHED1102 を GRP05 に保存します。記録対応の復旧準備ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP05 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧準備で リソース定義 の 定義検査 と グループ導入 を使い 復旧条件を確認 します。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。DFHED1101 を読み対象 GRP05 を切り分ける確認方法はどれですか。

    - A. 前回保存したCEDA CHECK GROUP(GRP05)の結果を使う。今回のCEDA INSTALL GROUP(GRP05)の結果と同一時点の証跡として比較する。
    - B. 保存済みのGRP05の出力を再利用する。今回のCEDA CHECK GROUP(GRP05)とCEDA INSTALL GROUP(GRP05)は実行済みとして扱う。
    - C. 変更を加えずCEDA CHECK GROUP(GRP05)を実行する。DFHED1101を保存する。差分はCEDA INSTALL GROUP(GRP05)の結果と対象名で対応させる。 ✅
    - D. CEDA INSTALL GROUP(GRP05)のDFHED1102をグループ名とインストール結果の主判定に採用する。CEDA CHECK GROUP(GRP05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 初級

    **解説:** 選定理由: Cは定義検査で DFHED1101 を読みグループ名とインストール結果の主値として復旧条件を確認しGRP05に残します。
    処理の仕組み: 復旧準備ではグループ導入を補助操作としCEDA資源定義の再開前に必要な整合性をDFHED1102と対象GRP05で照合します。
    選択結果の内訳: 定義検査とグループ導入の役割を分けるとA: 採取時刻が異なる点で定義検査を代替しません、B: 過去出力では今回の復旧準備を示せない点でリソース定義に使いません、C: 変更前のDFHED1101を保存する点で正答です、D: DFHED1102はDFHED1101を代替しないうえに追加前提も不正な点でGRP05を採用できません。結論として復旧準備のリソース定義・資源定義で判定する対象は GRP05 です。
    用語の説明: 復旧準備で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP05へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 復旧準備 GRP05**

    - 検証目的: リソース定義のCEDA資源定義について復旧条件を確認し、GRP05のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP05)を指定し、GRP05の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP05 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP05)を指定し、GRP05のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP05 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP05)を指定し、GRP05のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP05)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHED1101 が画面・出力に表示されること
    ② ステップ2 の DFHED1102 が画面・出力に表示されること
    ③ ステップ3 の GROUP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 構成監査 GRP08 {#c04-i0239}
*分類: リソース定義*  ・  難易度: 初級

構成監査では リソース定義 の 定義検査 を主操作として GRP08 を判定します。定義値と稼働値の一致への注意として「別グループの同名資源をインストールする危険があります」を GRP08 に残します。構成監査を補助する グループ導入 では DFHED1102 を補助値として GRP08 へ保存します。主判定の構成監査ではリソース定義・資源定義の 定義検査 から DFHED1101 を読み GRP08 へ残します。証跡照合の構成監査ではリソース定義・資源定義の DFHED1101 と DFHED1102 を GRP08 に保存します。記録対応の構成監査ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP08 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 構成監査で リソース定義 の 定義検査 と グループ導入 を照合し 定義値と稼働値の一致 を確かめます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。DFHED1101 を読む前に対象 GRP08 へ行う確認はどれですか。

    - A. 保存済みのGRP08の出力を再利用する。今回のCEDA CHECK GROUP(GRP08)とCEDA INSTALL GROUP(GRP08)は実行済みとして扱う。
    - B. CEDA INSTALL GROUP(GRP08)の結果だけでは確定しない。CEDA CHECK GROUP(GRP08)のDFHED1101を主証跡として構成差分を監査する。 ✅
    - C. CEDA INSTALL GROUP(GRP08)のDFHED1102をグループ名とインストール結果の主判定に採用する。CEDA CHECK GROUP(GRP08)の応答は採取対象から外す。
    - D. CEDA DISPLAY GROUP(GRP08)のGROUPをDFHED1101と同義の成功表示として扱う。CEDA CHECK GROUP(GRP08)は実行しない。

    正解: **B** ／ 難易度: 初級

    **解説:** 技術上の正答: Bは定義検査で DFHED1101 を読みグループ名とインストール結果の主値として構成差分を監査しGRP08に残します。
    実行時の背景: 構成監査ではグループ導入を補助操作としCEDA資源定義の定義値と稼働値の一致をDFHED1102と対象GRP08で照合します。
    四つの候補の理由: 定義検査とグループ導入の役割を分けるとA: 過去出力では今回の構成監査を示せない点でリソース定義に使いません、B: DFHED1101を主証跡として区別する点で正答です、C: DFHED1102はDFHED1101を代替しない点でGRP08を採用できません、D: GROUPとDFHED1101は確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のリソース定義・資源定義で判定する対象は GRP08 です。
    初出語定義: 構成監査で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP08へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 構成監査 GRP08**

    - 検証目的: リソース定義のCEDA資源定義について構成差分を監査し、GRP08のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP08)を指定し、GRP08の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP08 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP08)を指定し、GRP08のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP08 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP08)を指定し、GRP08のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP08)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHED1101 が画面・出力に表示されること
    ② ステップ2 の DFHED1102 が画面・出力に表示されること
    ③ ステップ3 の GROUP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 通常状態の確認 GRP01 {#c04-i0240}
*分類: リソース定義*  ・  難易度: 初級

通常状態の確認では リソース定義 の グループ表示 を主操作として GRP01 を判定します。基準値と現在値の差への注意として「別グループの同名資源をインストールする危険があります」を GRP01 に残します。通常状態の確認を補助する 定義検査 では DFHED1101 を補助値として GRP01 へ保存します。主判定の通常状態の確認ではリソース定義・資源定義の グループ表示 から GROUP を読み GRP01 へ残します。証跡照合の通常状態の確認ではリソース定義・資源定義の GROUP と DFHED1101 を GRP01 に保存します。記録対応の通常状態の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP01 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で リソース定義 の グループ表示 と 定義検査 を用い 通常状態を確定 します。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。GROUP で対象 GRP01 の グループ名とインストール結果 を再現できる記録はどれですか。

    - A. CEDA CHECK GROUP(GRP01)のDFHED1101をグループ名とインストール結果の主判定に採用する。CEDA DISPLAY GROUP(GRP01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. CEDA INSTALL GROUP(GRP01)のDFHED1102をGROUPと同義の成功表示として扱う。CEDA DISPLAY GROUP(GRP01)は実行しない。
    - C. CEDA DISPLAY GROUP(GRP01)を先に実行する。対象GRP01のGROUPをグループ名とインストール結果として記録する。続いてCEDA CHECK GROUP(GRP01)で同一対象を照合する。 ✅
    - D. CEDA DISPLAY GROUP(GRP01)が応答を返した時点で正常とする。応答中のGROUPの値は記録しない。

    正解: **C** ／ 難易度: 初級

    **解説:** 正解の説明: Cはグループ表示で GROUP を読みグループ名とインストール結果の主値として通常状態を確定しGRP01に残します。
    背景・仕組み: 通常状態の確認では定義検査を補助操作としCEDA資源定義の基準値と現在値の差をDFHED1101と対象GRP01で照合します。
    選択肢の理由: グループ表示と定義検査の役割を分けるとA: DFHED1101はGROUPを代替しないうえに追加前提も不正な点でCEDA資源定義に使えません、B: DFHED1102とGROUPは確認項目が異なる点でGRP01を採用できません、C: GROUPを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではグループ名とインストール結果を判定できない点で一次資料と一致しません。結論として通常状態の確認のリソース定義・資源定義で判定する対象は GRP01 です。
    用語の初出定義: 通常状態の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP01へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 通常状態の確認 GRP01**

    - 検証目的: リソース定義のCEDA資源定義について通常状態を確定し、GRP01のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP01)を指定し、GRP01のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP01)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP01)を指定し、GRP01の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP01 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP01)を指定し、GRP01のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP01 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
    ② ステップ2 の DFHED1101 が画面・出力に表示されること
    ③ ステップ3 の DFHED1102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### リソース定義 CEDA資源定義 障害切り分け GRP04 {#c04-i0241}
*分類: リソース定義*  ・  難易度: 初級

障害切り分けでは リソース定義 の グループ表示 を主操作として GRP04 を判定します。最初に失敗した処理への注意として「別グループの同名資源をインストールする危険があります」を GRP04 に残します。障害切り分けを補助する 定義検査 では DFHED1101 を補助値として GRP04 へ保存します。主判定の障害切り分けではリソース定義・資源定義の グループ表示 から GROUP を読み GRP04 へ残します。証跡照合の障害切り分けではリソース定義・資源定義の GROUP と DFHED1101 を GRP04 に保存します。記録対応の障害切り分けではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP04 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 障害切り分けで リソース定義 の グループ表示 と 定義検査 の役割を分け 最初に失敗した処理 を調べます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。対象 GRP04 を誤判定しない進め方はどれですか。

    - A. CEDA INSTALL GROUP(GRP04)のDFHED1102をGROUPと同義の成功表示として扱う。CEDA DISPLAY GROUP(GRP04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. CEDA DISPLAY GROUP(GRP04)の出力でGRP04とGROUPが同じ応答にあることを確認する。グループ名とインストール結果をその応答から採取する。 ✅
    - C. CEDA DISPLAY GROUP(GRP04)が応答を返した時点で正常とする。応答中のGROUPの値は記録しない。
    - D. CEDA DISPLAY GROUP(GRP04)のコマンド文字列だけを記録する。GROUPを含む応答行は保存しない。

    正解: **B** ／ 難易度: 初級

    **解説:** 正しい操作の説明: Bはグループ表示で GROUP を読みグループ名とインストール結果の主値として障害範囲を限定しGRP04に残します。
    技術的背景: 障害切り分けでは定義検査を補助操作としCEDA資源定義の最初に失敗した処理をDFHED1101と対象GRP04で照合します。
    四択の評価: グループ表示と定義検査の役割を分けるとA: DFHED1102とGROUPは確認項目が異なるうえに追加前提も不正な点でGRP04を採用できません、B: GRP04とGROUPを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではグループ名とインストール結果を判定できない点で一次資料と一致しません、D: 入力記録だけではグループ名とインストール結果を証明できない点でグループ名とインストール結果を確認できません。結論として障害切り分けのリソース定義・資源定義で判定する対象は GRP04 です。
    初出語の意味: 障害切り分けで使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP04へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **リソース定義 CEDA資源定義 障害切り分け GRP04**

    - 検証目的: リソース定義のCEDA資源定義について障害範囲を限定し、GRP04のグループ名とインストール結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP04)を指定し、GRP04のグループ表示を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA DISPLAY GROUP(GRP04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DISPLAY GROUP(GRP04)
    PROGRAM TRANSACTION FILE TCPIPSERVICE
    ```

    画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP04)を指定し、GRP04の定義検査を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA CHECK GROUP(GRP04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1101 GROUP GRP04 CHECKED. NO ERRORS FOUND
    ```

    画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP04)を指定し、GRP04のグループ導入を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA INSTALL GROUP(GRP04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHED1102 GROUP GRP04 INSTALL SUCCESSFUL
    ```

    画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
    ② ステップ2 の DFHED1101 が画面・出力に表示されること
    ③ ステップ3 の DFHED1102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf




## CICS Transaction Server for z/OS 6.x > 一時記憶

### Temporary Storage Queue {#c04-i0242}
*分類: 一時記憶*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の 一時記憶で扱うTemporary Storage Queueは、CICS 内で一時的なデータを保存するキューです。端末処理の中間データや複数タスク間の受け渡しに使われます。保存場所や有効期間を理解しないと、再始動後のデータ有無を誤解します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 範囲確認の一時記憶でトランザクション管理の運用確認を行います。Temporary Storage Queueの根拠にできる作業はどれですか。

    - A. CICS TS と無関係な一覧で範囲確認の一時記憶を確認した扱いにする。
    - B. DFH4200A の有無を確認せず範囲確認の一時記憶を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 ✅
    - D. Temporary Storage Queueの属性行を読まず範囲確認の一時記憶の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Temporary Storage Queue は「CICS TS で Temporary Storage Queueの扱いを記録する範囲確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Temporary Storage Queueの表示結果と DFH4200A を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Temporary Storage Queueの使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **Temporary Storage Queue**

    - 検証目的: 範囲確認の一時記憶について、CICS Transaction Server for z/OS 6.x の 一時記憶で扱う Temporary Storage Queueは、CICS 内で一時的なデータをに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、範囲確認の一時記憶の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTemporary Storage を指定し、OSKB010011の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Temporary Storage 
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Temporary Storage 
    CASE OSKB010011
    SOURCE CICS TS
    ```

    Temporary Storage とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010011を同じ出力で読み、範囲確認の一時記憶の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010011
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A Temporary Storage Queue RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の Temporary Storage  と OSKB010011 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### Transient Data Queue {#c04-i0243}
*分類: 一時記憶*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の 一時記憶で扱うTransient Data Queueは、CICS が順次データをキューとして扱う機能です。内部キューと外部キューがあり、ログ出力や他処理への引き渡しに使われます。処理漏れを調べるときはキュー定義と読み取り側の状態を確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 優先確認の一時記憶に関する Transient Data Queueの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず優先確認の一時記憶の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の一時記憶の証跡として保存して根拠にする。
    - C. Transient Data Queueの変更点を出力本文から切り離して優先確認の一時記憶の承認欄のみ残す。
    - D. DFH4200A を含む表示を保存し、説明欄との差分を優先確認で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Transient Data Queue は「Transient Data Queueの状態と出力メッセージを結び付ける優先確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Transient Data Queueの出力行と DFH4200A を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Transient Data Queueを CICS TS の確認記録に残し、対象名は優先確認対象です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **Transient Data Queue**

    - 検証目的: 優先確認の一時記憶について、CICS Transaction Server for z/OS 6.x の 一時記憶で扱う Transient Data Queueは、CICS が順次データをキューとしてに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、優先確認の一時記憶の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にTransient Data Queを指定し、OSKB010012の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND Transient Data Que
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM Transient Data Que
    CASE OSKB010012
    SOURCE CICS TS
    ```

    Transient Data QueとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010012を同じ出力で読み、優先確認の一時記憶の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010012
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010012
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A Transient Data Queue RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の Transient Data Que と OSKB010012 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS




## CICS Transaction Server for z/OS 6.x > 基本概念

### CICS リージョン {#c04-i0244}
*分類: 基本概念*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の 基本概念で扱うCICS リージョンは、トランザクション、プログラム、ファイル、通信資源を実行する z/OS 上のアドレス空間です。端末処理やオンライン業務の実行単位になるため、起動 JCL、SIT、リソース定義を合わせて確認します。障害時はリージョン単位のメッセージとダンプを確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 構文確認のリージョンに関係する CICS リージョンの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. F CICSA,CEMT I TRAN(OSKB)の結果から対象行を抜き出し、構文確認の証跡として残す。 ✅
    - B. CICS リージョンの名称と担当者名のみを残して構文確認のリージョンの表示本文を確認対象に含めない。
    - C. トランザクション管理以外の画面で構文確認のリージョンを確認し同じ証跡として扱ったことにする。
    - D. DFH4200A の有無を見ず構文確認のリージョンの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では CICS リージョン は「CICS リージョンの用途をトランザクション管理の表示で確認する構文確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では CICS TS の CICS リージョンと DFH4200A を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では CICS リージョンを CICS Transaction Server for z/OS 6.xで扱う確認対象とし、用語名は構文確認用語です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **CICS リージョン**

    - 検証目的: 構文確認のリージョンについて、CICS Transaction Server for z/OS 6.x の 基本概念で扱う CICS リージョンは、トランザクション、プログラム、ファイル、通信資源を実行すに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、構文確認のリージョンの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCICS リージョンを指定し、OSKB010001の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CICS リージョン
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CICS リージョン
    CASE OSKB010001
    SOURCE CICS TS
    ```

    CICS リージョンとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010001を同じ出力で読み、構文確認のリージョンの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010001
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A CICS リージョン RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の CICS リージョン と OSKB010001 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### トランザクション ID {#c04-i0245}
*分類: 基本概念*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の 基本概念で扱うトランザクション IDは、CICS で業務処理を起動するための短い識別子です。端末やプログラムから入力され、対応するプログラムやプロファイルへ結び付けられます。障害時は入力された ID と実行されたプログラムの対応を確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 展開確認のトランザクションでトランザクション ID の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. トランザクション ID の出力を取らず展開確認のトランザクションの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 ✅
    - C. F CICSA,CEMT I TRAN(OSKB)を省略して展開確認のトランザクションの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認のトランザクションへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠ではトランザクション ID は「展開確認のトランザクションに関係する定義値と表示行を照合する展開確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡ではトランザクション ID の属性行と DFH4200A を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出ではトランザクション ID を CICS Transaction Server for z/OS 6.xの運用手順で確認し、初出名は展開確認初出です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **トランザクション ID**

    - 検証目的: 展開確認のトランザクションについて、CICS Transaction Server for z/OS 6.x の 基本概念で扱うトランザクション ID は、CICS で業務処理を起動するための短い識別子です。端に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、展開確認のトランザクションの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にトランザクション IDを指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND トランザクション ID
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM トランザクション ID
    CASE OSKB010002
    SOURCE CICS TS
    ```

    トランザクション IDとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010002を同じ出力で読み、展開確認のトランザクションの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010002
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A トランザクション ID RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の トランザクション ID と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### プログラム定義 {#c04-i0246}
*分類: 基本概念*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の 基本概念で扱うプログラム定義は、CICS が実行するアプリケーションプログラムの属性を登録するリソース定義です。言語、実行モード、再入可能性、ロード先などが実行時の挙動に影響します。新規リリース時は定義とロードライブラリの整合を確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 呼出確認のプログラム定義でトランザクション管理の運用確認を行います。プログラム定義の根拠にできる作業はどれですか。

    - A. CICS TS と無関係な一覧で呼出確認のプログラム定義を確認した扱いにする。
    - B. DFH4200A の有無を確認せず呼出確認のプログラム定義を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. プログラム定義の属性行を読まず呼出確認のプログラム定義の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠ではプログラム定義は「CICS TS でプログラム定義の扱いを記録する呼出確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡ではプログラム定義の表示結果と DFH4200A を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料ではプログラム定義の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **プログラム定義**

    - 検証目的: 呼出確認のプログラム定義について、CICS Transaction Server for z/OS 6.x の 基本概念で扱うプログラム定義は、CICS が実行するアプリケーションプログラムの属性を登録するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、呼出確認のプログラム定義の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にプログラム定義を指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND プログラム定義
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM プログラム定義
    CASE OSKB010003
    SOURCE CICS TS
    ```

    プログラム定義とOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010003を同じ出力で読み、呼出確認のプログラム定義の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010003
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A プログラム定義 RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の プログラム定義 と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS




## CICS Transaction Server for z/OS 6.x > 監視

### CICS 統計 {#c04-i0247}
*分類: 監視*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の 監視で扱うCICS 統計は、リージョン、トランザクション、ファイル、ストレージなどの利用状況を示す運用情報です。性能傾向や容量計画、障害前後の比較に使います。統計の取得間隔とリセットタイミングを理解して読む必要があります

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 監査確認の統計でトランザクション管理の運用確認を行います。CICS 統計の根拠にできる作業はどれですか。

    - A. CICS TS と無関係な一覧で監査確認の統計を確認した扱いにする。
    - B. DFH4200A の有無を確認せず監査確認の統計を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 ✅
    - D. CICS 統計の属性行を読まず監査確認の統計の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では CICS 統計 は「CICS TS で CICS 統計の扱いを記録する監査確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では CICS 統計の表示結果と DFH4200A を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では CICS 統計の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **CICS 統計**

    - 検証目的: 監査確認の統計について、CICS Transaction Server for z/OS 6.x の 監視で扱う CICS 統計は、リージョン、トランザクション、ファイル、ストレージなどの利用状況をに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、監査確認の統計の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCICS 統計を指定し、OSKB010019の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CICS 統計
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CICS 統計
    CASE OSKB010019
    SOURCE CICS TS
    ```

    CICS 統計とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010019を同じ出力で読み、監査確認の統計の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010019
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A CICS 統計 RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の CICS 統計 と OSKB010019 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS




## CICS Transaction Server for z/OS 6.x > 相互通信

### IPIC {#c04-i0248}
*分類: 相互通信*  ・  難易度: 上級

CICS Transaction Server for z/OS 6.x の 相互通信で扱うIPICは、TCP/IP を使って CICS 領域間や外部クライアントと接続する通信方式です。サービス連携や分散構成で使われ、証明書やセキュリティ設定とも関わります。疎通障害では TCP/IP、CICS 定義、認証の順に切り分けます

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 警告確認の相互通信に関係する IPIC の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. F CICSA,CEMT I TRAN(OSKB)で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 ✅
    - B. IPIC の名称と担当者名のみを残して警告確認の相互通信の表示本文を確認対象に含めない。
    - C. トランザクション管理以外の画面で警告確認の相互通信を確認し同じ証跡として扱ったことにする。
    - D. DFH4200A の有無を見ず警告確認の相互通信の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では IPIC は「IPIC の用途をトランザクション管理の表示で確認する警告確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では CICS TS の IPIC と DFH4200A を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では IPIC を CICS Transaction Server for z/OS 6.xで扱う確認対象とし、用語名は警告確認用語です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **IPIC**

    - 検証目的: 警告確認の相互通信について、CICS Transaction Server for z/OS 6.x の 相互通信で扱う IPIC は、TCP/IP を使って CICS 領域間や外部クライアントと接続するに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、警告確認の相互通信の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIPICを指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IPIC
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IPIC
    CASE OSKB010017
    SOURCE CICS TS
    ```

    IPICとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010017を同じ出力で読み、警告確認の相互通信の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010017
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A IPIC RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の IPIC と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS



### MRO {#c04-i0249}
*分類: 相互通信*  ・  難易度: 上級

CICS Transaction Server for z/OS 6.x の 相互通信で扱うMROは、同一 z/OS イメージ内または近接する CICS リージョン間で通信するための方式です。トランザクションルーティングや機能分散に使われます。接続障害ではローカルとリモートの定義を両側で確認します

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 値域確認の相互通信に関する MRO の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず値域確認の相互通信の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の相互通信の証跡として保存して根拠にする。
    - C. MRO の変更点を出力本文から切り離して値域確認の相互通信の承認欄のみ残す。
    - D. 同じ画面で対象行と DFH4200A を読み、値域確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では MRO は「MRO の状態と出力メッセージを結び付ける値域確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では MRO の出力行と DFH4200A を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では MRO を CICS TS の確認記録に残し、対象名は値域確認対象です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **MRO**

    - 検証目的: 値域確認の相互通信について、CICS Transaction Server for z/OS 6.x の 相互通信で扱う MRO は、同一 z/OS イメージ内または近接する CICS リージョン間で通信に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、値域確認の相互通信の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にMROを指定し、OSKB010016の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND MRO
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM MRO
    CASE OSKB010016
    SOURCE CICS TS
    ```

    MROとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010016を同じ出力で読み、値域確認の相互通信の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010016
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010016
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A MRO RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の MRO と OSKB010016 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS




## CICS Transaction Server for z/OS 6.x > 診断

### CICS トランザクションダンプ {#c04-i0250}
*分類: 診断*  ・  難易度: 上級

CICS Transaction Server for z/OS 6.x の 診断で扱うCICS トランザクションダンプは、特定トランザクションの異常時状態を記録する診断資料です。プログラム、EXEC CICS 応答、作業領域の状態を調べる入口になります。ダンプコード、タスク番号、発生時刻をメッセージと対応させます

**出典:** CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS

??? question "確認問題（1問）"
    **問題.** 変更確認のトランザクションダンプに関する CICS トランザクションダンプの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず変更確認のトランザクションダンプの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認のトランザクションダンプの証跡として保存して根拠にする。
    - C. CICS トランザクションダンプの変更点を出力本文から切り離して変更確認のトランザクションダンプの承認欄のみ残す。
    - D. CICS TS の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では CICS トランザクションダンプ は「CICS トランザクションダンプの状態と出力メッセージを結び付ける変更確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では CICS トランザクションダンプの出力行と DFH4200A を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では CICS トランザクションダンプを CICS TS の確認記録に残し、対象名は変更確認対象です。

    **出典:** transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf


??? note "検証手順（1件）"
    **CICS トランザクションダンプ**

    - 検証目的: 変更確認のトランザクションダンプについて、CICS Transaction Server for z/OS 6.x の 診断で扱う CICS トランザクションダンプは、特定トランザクションの異常時状態を記録する診断資に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F CICSA,CEMT I TRAN(OSKB) を入力し、変更確認のトランザクションダンプの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    ```

    COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にCICS トランザクションダンプを指定し、OSKB010020の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND CICS トランザクションダンプ
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM CICS トランザクションダンプ
    CASE OSKB010020
    SOURCE CICS TS
    ```

    CICS トランザクションダンプとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010020を同じ出力で読み、変更確認のトランザクションダンプの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB)
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS CONSOLE RESPONSE OSKB010020
    F CICSA,CEMT I TRAN(OSKB)
    STATUS: RESULTS - OVERTYPE TO MODIFY
    DFH4200A CICS トランザクションダンプ RESPONSE DISPLAYED
    ```

    DFH4200AとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
    ② ステップ2 の CICS トランザクションダンプ と OSKB010020 が画面・出力に表示されること
    ③ ステップ3 の DFH4200A と OSKB010020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS


