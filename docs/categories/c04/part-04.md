---
search:
  exclude: true
---

# CICS Transaction Server for z/OS 6.x — 詳細 (4/5)

[← CICS Transaction Server for z/OS 6.x の概要へ戻る](index.md)


## CICS Transaction Server for z/OS 6.x > ファイル管理

### CICS-MQ bridge トレース確認 監査証跡 {#c04-i0174}
*分類: ファイル管理*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の ファイル管理 で扱う「CICS-MQ bridge トレース確認 監査証跡」は、MQメッセージから3270トランザクションを起動し、CEMTなどを橋渡しする連携機能をトレース確認の観点で確認する技術項目です。DFH メッセージとCIC04を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CICS-MQ bridge トレース確認 監査証跡**

    - 検証目的: ファイル管理におけるCICS-MQ bridgeのトレース確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC04
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE TRANSACTION(PAY044) GROUP(TEST) PROGRAM(DFH044)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF TRANSACTION(PAY044) GROUP(TEST)
    PROGRAM ==> DFH044
    PROFILE ==> DFHCICST
    ```

    画面・出力には CEDA が含まれ、CEDAを確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE PROGRAM(DFH044) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF PROGRAM(DFH044) GROUP(TEST)
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
    TRANSACTION PAY044 INSTALLED
    PROGRAM DFH044 INSTALLED
    ```

    画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
    ② ステップ2 の CEDA が画面・出力に表示されること
    ③ ステップ3 の INSTALL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 ログとの照合 FILE07 {#c04-i0175}
*分類: ファイル管理*  ・  難易度: 中級

ログとの照合では ファイル管理 の ファイル照会 を主操作として FILE07 を判定します。時刻と対象識別子への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE07 に残します。ログとの照合を補助する データセット照会 では Dsn を補助値として FILE07 へ保存します。主判定のログとの照合ではファイル管理・資源の ファイル照会 から File を読み FILE07 へ残します。証跡照合のログとの照合ではファイル管理・資源の File と Dsn を FILE07 に保存します。記録対応のログとの照合ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE07 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** ログとの照合で ファイル管理 の ファイル照会 と データセット照会 を用い 操作とログを対応 します。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。File で対象 FILE07 の OPENSTATUSとDSNAME を再現できる記録はどれですか。

    - A. CEMT INQUIRE FILE(FILE07)が応答を返した時点で正常とする。応答中のFileの値は記録しない。DFHST0103IをFileと同じ判定値とみなし対象FILE07の主証跡にする。
    - B. CEMT INQUIRE FILE(FILE07)のコマンド文字列だけを記録する。Fileを含む応答行は保存しない。
    - C. Fileを含むファイル照会の応答行を保存する。その応答を得るためCEMT INQUIRE FILE(FILE07)を使用する。対象FILE07のOPENSTATUSとDSNAMEとして記録する。 ✅
    - D. FILE資源の停止または再定義を実施する。その後にCEMT INQUIRE FILE(FILE07)でFileを採取する。

    正解: **C** ／ 難易度: 中級

    **解説:** 適切な判定: Cはファイル照会で File を読みOPENSTATUSとDSNAMEの主値として操作とログを対応しFILE07に残します。
    機能の仕組み: ログとの照合ではデータセット照会を補助操作としFILE資源の時刻と対象識別子をDsnと対象FILE07で照合します。
    各候補の評価: ファイル照会とデータセット照会の役割を分けるとA: 応答の有無だけではOPENSTATUSとDSNAMEを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではOPENSTATUSとDSNAMEを証明できない点で一次資料と一致しません、C: Fileの実値を対象別に残す点でFILE07を判定できます、D: 変更前のOPENSTATUSとDSNAMEを失う点でデータセット照会の範囲を越えます。結論としてログとの照合のファイル管理・資源で判定する対象は FILE07 です。
    用語の定義: ログとの照合で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE07へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 ログとの照合 FILE07**

    - 検証目的: ファイル管理のFILE資源について操作とログを対応し、FILE07のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE07)を指定し、FILE07のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE07) Ope Ena Rea Upd Dsname(APP.FILE07.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE07.DATA)を指定し、FILE07のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE07.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE07.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE07.DATAを読み、OPENSTATUSとDSNAMEと対象FILE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE07)を指定し、FILE07の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE07 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の File が画面・出力に表示されること
    ② ステップ2 の APP.FILE07.DATA が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 代替経路の確認 FILE10 {#c04-i0176}
*分類: ファイル管理*  ・  難易度: 中級

代替経路の確認では ファイル管理 の ファイル照会 を主操作として FILE10 を判定します。主経路との役割差への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE10 に残します。代替経路の確認を補助する データセット照会 では Dsn を補助値として FILE10 へ保存します。主判定の代替経路の確認ではファイル管理・資源の ファイル照会 から File を読み FILE10 へ残します。証跡照合の代替経路の確認ではファイル管理・資源の File と Dsn を FILE10 に保存します。記録対応の代替経路の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE10 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で ファイル管理 の ファイル照会 と データセット照会 の役割を分け 主経路との役割差 を調べます。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。対象 FILE10 を誤判定しない進め方はどれですか。

    - A. CEMT INQUIRE FILE(FILE10)のコマンド文字列だけを記録する。Fileを含む応答行は保存しない。
    - B. CEMT INQUIRE FILE(FILE10)とCEMT INQUIRE DSNAME(APP.FILE10.DATA)の対象名をそろえる。前者のFileをOPENSTATUSとDSNAMEの判定値として採用する。 ✅
    - C. FILE資源の停止または再定義を実施する。その後にCEMT INQUIRE FILE(FILE10)でFileを採取する。
    - D. ダンプ解析のDUMPCODEとDUMPSCOPEを確認する。その値をファイル管理のFILE10にも適用する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい判定結果: Bはファイル照会で File を読みOPENSTATUSとDSNAMEの主値として代替手段の成立を確認しFILE10に残します。
    運用上の背景: 代替経路の確認ではデータセット照会を補助操作としFILE資源の主経路との役割差をDsnと対象FILE10で照合します。
    候補別の検討: ファイル照会とデータセット照会の役割を分けるとA: 入力記録だけではOPENSTATUSとDSNAMEを証明できない点で一次資料と一致しません、B: 同じ対象名のFileを採用する点でFILE10を判定できます、C: 変更前のOPENSTATUSとDSNAMEを失う点でデータセット照会の範囲を越えます、D: ダンプ解析の値ではFileを確認できない点でFILE10の値を示しません。結論として代替経路の確認のファイル管理・資源で判定する対象は FILE10 です。
    重要用語の定義: 代替経路の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE10へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 代替経路の確認 FILE10**

    - 検証目的: ファイル管理のFILE資源について代替手段の成立を確認し、FILE10のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE10)を指定し、FILE10のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE10) Ope Ena Rea Upd Dsname(APP.FILE10.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE10.DATA)を指定し、FILE10のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE10.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE10.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE10.DATAを読み、OPENSTATUSとDSNAMEと対象FILE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE10)を指定し、FILE10の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE10 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の File が画面・出力に表示されること
    ② ステップ2 の APP.FILE10.DATA が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 変更前の確認 FILE02 {#c04-i0177}
*分類: ファイル管理*  ・  難易度: 中級

変更前の確認では ファイル管理 の データセット照会 を主操作として FILE02 を判定します。変更対象と非対象の境界への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE02 に残します。変更前の確認を補助する 統計採取 では DFHST0103I を補助値として FILE02 へ保存します。主判定の変更前の確認ではファイル管理・資源の データセット照会 から Dsn を読み FILE02 へ残します。証跡照合の変更前の確認ではファイル管理・資源の Dsn と DFHST0103I を FILE02 に保存します。記録対応の変更前の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE02 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更前の確認で ファイル管理 の データセット照会 と 統計採取 を照合し 変更対象と非対象の境界 を確かめます。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。Dsn を読む前に対象 FILE02 へ行う確認はどれですか。

    - A. CEMT INQUIRE DSNAME(APP.FILE02.DATA)を対象名なしで実行する。一覧の先頭行をFILE02の結果として記録する。
    - B. 対象FILE02についてCEMT INQUIRE DSNAME(APP.FILE02.DATA)の応答からDsnを確認する。CEMT PERFORM STATISTICS RECORD FILE(FILE02)は補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したCEMT INQUIRE DSNAME(APP.FILE02.DATA)の結果を使う。今回のCEMT PERFORM STATISTICS RECORD FILE(FILE02)の結果と同一時点の証跡として比較する。
    - D. 保存済みのFILE02の出力を再利用する。今回のCEMT INQUIRE DSNAME(APP.FILE02.DATA)とCEMT PERFORM STATISTICS RECORD FILE(FILE02)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 中級

    **解説:** 採用理由: Bはデータセット照会で Dsn を読みOPENSTATUSとDSNAMEの主値として変更前の証跡を保存しFILE02に残します。
    動作の背景: 変更前の確認では統計採取を補助操作としFILE資源の変更対象と非対象の境界をDFHST0103Iと対象FILE02で照合します。
    各選択肢の検討: データセット照会と統計採取の役割を分けるとA: 先頭行はFILE02と確定できない点で変更前の確認に合いません、B: Dsnと補助証跡の時刻を合わせる点でデータセット照会に合います、C: 採取時刻が異なる点でファイル管理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でFILE資源に使えません。結論として変更前の確認のファイル管理・資源で判定する対象は FILE02 です。
    初出用語の定義: 変更前の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE02へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 変更前の確認 FILE02**

    - 検証目的: ファイル管理のFILE資源について変更前の証跡を保存し、FILE02のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE02.DATA)を指定し、FILE02のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE02.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE02.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE02.DATAを読み、OPENSTATUSとDSNAMEと対象FILE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE02)を指定し、FILE02の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE02 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE02)を指定し、FILE02のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE02) Ope Ena Rea Upd Dsname(APP.FILE02.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APP.FILE02.DATA が画面・出力に表示されること
    ② ステップ2 の DFHST0103I が画面・出力に表示されること
    ③ ステップ3 の File が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 変更後の確認 FILE03 {#c04-i0178}
*分類: ファイル管理*  ・  難易度: 中級

変更後の確認では ファイル管理 の 統計採取 を主操作として FILE03 を判定します。反映値と残存値への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE03 に残します。変更後の確認を補助する ファイル照会 では File を補助値として FILE03 へ保存します。主判定の変更後の確認ではファイル管理・資源の 統計採取 から DFHST0103I を読み FILE03 へ残します。証跡照合の変更後の確認ではファイル管理・資源の DFHST0103I と File を FILE03 に保存します。記録対応の変更後の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE03 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更後の確認で ファイル管理 の 統計採取 と ファイル照会 を組み合わせる際は FILE資源 がデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源という仕組みを前提にします。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。DFHST0103I と OPENSTATUSとDSNAME を対象 FILE03 で確認する組合せはどれですか。

    - A. FILE資源の停止または再定義を実施する。その後にCEMT PERFORM STATISTICS RECORD FILE(FILE03)でDFHST0103Iを採取する。
    - B. ファイル管理のOPENSTATUSとDSNAMEを確認する。その値をファイル管理のFILE03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。FILE資源の反映値と残存値は確認済みとして扱う。さらにCEMT INQUIRE DSNAME(APP.FILE03.DATA)のDsnをDFHST0103Iと同種の値として併記する。
    - C. CEMT INQUIRE FILE(FILE03)で周辺状態を押さえる。その後にCEMT PERFORM STATISTICS RECORD FILE(FILE03)でDFHST0103Iを確認して変更結果を検証する。 ✅
    - D. CEMT INQUIRE FILE(FILE03)が成功したためCEMT PERFORM STATISTICS RECORD FILE(FILE03)のDFHST0103Iも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正答の根拠: Cは統計採取で DFHST0103I を読みOPENSTATUSとDSNAMEの主値として変更結果を検証しFILE03に残します。
    内部の仕組み: 変更後の確認ではファイル照会を補助操作としFILE資源の反映値と残存値をFileと対象FILE03で照合します。
    誤答を含む比較: 統計採取とファイル照会の役割を分けるとA: 変更前のOPENSTATUSとDSNAMEを失う点でOPENSTATUSとDSNAMEを確認できません、B: ファイル管理の値ではDFHST0103Iを確認できないうえに追加前提も不正な点でファイル照会の範囲を越えます、C: 周辺状態の後にDFHST0103Iを確認する点で現在値を示します、D: 補助操作の成功ではDFHST0103Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のファイル管理・資源で判定する対象は FILE03 です。
    用語定義: 変更後の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE03へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 変更後の確認 FILE03**

    - 検証目的: ファイル管理のFILE資源について変更結果を検証し、FILE03のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE03)を指定し、FILE03の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE03 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE03)を指定し、FILE03のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE03) Ope Ena Rea Upd Dsname(APP.FILE03.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE03.DATA)を指定し、FILE03のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE03.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE03.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE03.DATAを読み、OPENSTATUSとDSNAMEと対象FILE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
    ② ステップ2 の File が画面・出力に表示されること
    ③ ステップ3 の APP.FILE03.DATA が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 引継ぎ記録 FILE09 {#c04-i0179}
*分類: ファイル管理*  ・  難易度: 中級

引継ぎ記録では ファイル管理 の 統計採取 を主操作として FILE09 を判定します。次担当者が追跡できる証跡への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE09 に残します。引継ぎ記録を補助する ファイル照会 では File を補助値として FILE09 へ保存します。主判定の引継ぎ記録ではファイル管理・資源の 統計採取 から DFHST0103I を読み FILE09 へ残します。証跡照合の引継ぎ記録ではファイル管理・資源の DFHST0103I と File を FILE09 に保存します。記録対応の引継ぎ記録ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE09 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で ファイル管理 の 統計採取 と ファイル照会 を組み合わせる際は FILE資源 がデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源という仕組みを前提にします。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。DFHST0103I と OPENSTATUSとDSNAME を対象 FILE09 で確認する組合せはどれですか。

    - A. 対象名FILE09を指定してCEMT PERFORM STATISTICS RECORD FILE(FILE09)を実行する。応答中のDFHST0103Iと時刻を保存する。CEMT INQUIRE FILE(FILE09)で周辺状態を補完する。 ✅
    - B. CEMT INQUIRE FILE(FILE09)が成功したためCEMT PERFORM STATISTICS RECORD FILE(FILE09)のDFHST0103Iも正常だと推定する。主出力は保存しない。
    - C. CEMT PERFORM STATISTICS RECORD FILE(FILE09)を対象名なしで実行する。一覧の先頭行をFILE09の結果として記録する。
    - D. 前回保存したCEMT PERFORM STATISTICS RECORD FILE(FILE09)の結果を使う。今回のCEMT INQUIRE FILE(FILE09)の結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 中級

    **解説:** 採用操作の理由: Aは統計採取で DFHST0103I を読みOPENSTATUSとDSNAMEの主値として再現可能な記録を作成しFILE09に残します。
    製品内の仕組み: 引継ぎ記録ではファイル照会を補助操作としFILE資源の次担当者が追跡できる証跡をFileと対象FILE09で照合します。
    選択肢別の説明: 統計採取とファイル照会の役割を分けるとA: DFHST0103Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではDFHST0103Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はFILE09と確定できない点で統計採取を代替しません、D: 採取時刻が異なる点でファイル管理に使いません。結論として引継ぎ記録のファイル管理・資源で判定する対象は FILE09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE09へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 引継ぎ記録 FILE09**

    - 検証目的: ファイル管理のFILE資源について再現可能な記録を作成し、FILE09のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE09)を指定し、FILE09の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE09 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE09)を指定し、FILE09のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE09) Ope Ena Rea Upd Dsname(APP.FILE09.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE09.DATA)を指定し、FILE09のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE09.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE09.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE09.DATAを読み、OPENSTATUSとDSNAMEと対象FILE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
    ② ステップ2 の File が画面・出力に表示されること
    ③ ステップ3 の APP.FILE09.DATA が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 復旧後の確認 FILE06 {#c04-i0180}
*分類: ファイル管理*  ・  難易度: 中級

復旧後の確認では ファイル管理 の 統計採取 を主操作として FILE06 を判定します。再発していないことを示す値への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE06 に残します。復旧後の確認を補助する ファイル照会 では File を補助値として FILE06 へ保存します。主判定の復旧後の確認ではファイル管理・資源の 統計採取 から DFHST0103I を読み FILE06 へ残します。証跡照合の復旧後の確認ではファイル管理・資源の DFHST0103I と File を FILE06 に保存します。記録対応の復旧後の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE06 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で ファイル管理 の 統計採取 と ファイル照会 を実施し FILE資源 の役割を確認します。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。対象 FILE06 の証跡を取る方法はどれですか。

    - A. Liberty JVMのJVMSTATUSとPROFILEを確認する。その値をファイル管理のFILE06にも適用する。
    - B. CEMT PERFORM STATISTICS RECORD FILE(FILE06)でDFHST0103Iを取得してからCEMT INQUIRE DSNAME(APP.FILE06.DATA)でDsnを照合する。FILE06のOPENSTATUSとDSNAMEを両出力から確定する。 ✅
    - C. CEMT INQUIRE FILE(FILE06)が成功したためCEMT PERFORM STATISTICS RECORD FILE(FILE06)のDFHST0103Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象FILE06へ引き継げるものとする。FILE資源の再発していないことを示す値は確認済みとして扱う。さらにCEMT INQUIRE DSNAME(APP.FILE06.DATA)のDsnをDFHST0103Iと同種の値として併記する。
    - D. CEMT PERFORM STATISTICS RECORD FILE(FILE06)を対象名なしで実行する。一覧の先頭行をFILE06の結果として記録する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正答内容: Bは統計採取で DFHST0103I を読みOPENSTATUSとDSNAMEの主値として復旧後の安定性を確認しFILE06に残します。
    構成上の背景: 復旧後の確認ではファイル照会を補助操作としFILE資源の再発していないことを示す値をFileと対象FILE06で照合します。
    候補ごとの理由: 統計採取とファイル照会の役割を分けるとA: Liberty JVMの値ではDFHST0103Iを確認できない点でファイル照会の範囲を越えます、B: DFHST0103IとDsnを順に照合する点で現在値を示します、C: 補助操作の成功ではDFHST0103Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はFILE06と確定できない点で統計採取を代替しません。結論として復旧後の確認のファイル管理・資源で判定する対象は FILE06 です。
    初出用語: 復旧後の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE06へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 復旧後の確認 FILE06**

    - 検証目的: ファイル管理のFILE資源について復旧後の安定性を確認し、FILE06のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE06)を指定し、FILE06の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE06 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE06)を指定し、FILE06のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE06) Ope Ena Rea Upd Dsname(APP.FILE06.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE06.DATA)を指定し、FILE06のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE06.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE06.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE06.DATAを読み、OPENSTATUSとDSNAMEと対象FILE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
    ② ステップ2 の File が画面・出力に表示されること
    ③ ステップ3 の APP.FILE06.DATA が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 復旧準備 FILE05 {#c04-i0181}
*分類: ファイル管理*  ・  難易度: 中級

復旧準備では ファイル管理 の データセット照会 を主操作として FILE05 を判定します。再開前に必要な整合性への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE05 に残します。復旧準備を補助する 統計採取 では DFHST0103I を補助値として FILE05 へ保存します。主判定の復旧準備ではファイル管理・資源の データセット照会 から Dsn を読み FILE05 へ残します。証跡照合の復旧準備ではファイル管理・資源の Dsn と DFHST0103I を FILE05 に保存します。記録対応の復旧準備ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE05 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧準備で ファイル管理 の データセット照会 と 統計採取 を使い 復旧条件を確認 します。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。Dsn を読み対象 FILE05 を切り分ける確認方法はどれですか。

    - A. 変更を加えずCEMT INQUIRE DSNAME(APP.FILE05.DATA)を実行する。Dsnを保存する。差分はCEMT PERFORM STATISTICS RECORD FILE(FILE05)の結果と対象名で対応させる。 ✅
    - B. 前回保存したCEMT INQUIRE DSNAME(APP.FILE05.DATA)の結果を使う。今回のCEMT PERFORM STATISTICS RECORD FILE(FILE05)の結果と同一時点の証跡として比較する。
    - C. 保存済みのFILE05の出力を再利用する。今回のCEMT INQUIRE DSNAME(APP.FILE05.DATA)とCEMT PERFORM STATISTICS RECORD FILE(FILE05)は実行済みとして扱う。
    - D. CEMT PERFORM STATISTICS RECORD FILE(FILE05)のDFHST0103IをOPENSTATUSとDSNAMEの主判定に採用する。CEMT INQUIRE DSNAME(APP.FILE05.DATA)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 中級

    **解説:** 選定理由: Aはデータセット照会で Dsn を読みOPENSTATUSとDSNAMEの主値として復旧条件を確認しFILE05に残します。
    処理の仕組み: 復旧準備では統計採取を補助操作としFILE資源の再開前に必要な整合性をDFHST0103Iと対象FILE05で照合します。
    選択結果の内訳: データセット照会と統計採取の役割を分けるとA: 変更前のDsnを保存する点でデータセット照会に合います、B: 採取時刻が異なる点でファイル管理に使いません、C: 過去出力では今回の復旧準備を示せない点でFILE資源に使えません、D: DFHST0103IはDsnを代替しないうえに追加前提も不正な点でFILE05を採用できません。結論として復旧準備のファイル管理・資源で判定する対象は FILE05 です。
    用語の説明: 復旧準備で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE05へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 復旧準備 FILE05**

    - 検証目的: ファイル管理のFILE資源について復旧条件を確認し、FILE05のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE05.DATA)を指定し、FILE05のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE05.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE05.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE05.DATAを読み、OPENSTATUSとDSNAMEと対象FILE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE05)を指定し、FILE05の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE05 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE05)を指定し、FILE05のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE05) Ope Ena Rea Upd Dsname(APP.FILE05.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APP.FILE05.DATA が画面・出力に表示されること
    ② ステップ2 の DFHST0103I が画面・出力に表示されること
    ③ ステップ3 の File が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 構成監査 FILE08 {#c04-i0182}
*分類: ファイル管理*  ・  難易度: 中級

構成監査では ファイル管理 の データセット照会 を主操作として FILE08 を判定します。定義値と稼働値の一致への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE08 に残します。構成監査を補助する 統計採取 では DFHST0103I を補助値として FILE08 へ保存します。主判定の構成監査ではファイル管理・資源の データセット照会 から Dsn を読み FILE08 へ残します。証跡照合の構成監査ではファイル管理・資源の Dsn と DFHST0103I を FILE08 に保存します。記録対応の構成監査ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE08 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 構成監査で ファイル管理 の データセット照会 と 統計採取 を照合し 定義値と稼働値の一致 を確かめます。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。Dsn を読む前に対象 FILE08 へ行う確認はどれですか。

    - A. 保存済みのFILE08の出力を再利用する。今回のCEMT INQUIRE DSNAME(APP.FILE08.DATA)とCEMT PERFORM STATISTICS RECORD FILE(FILE08)は実行済みとして扱う。
    - B. CEMT PERFORM STATISTICS RECORD FILE(FILE08)のDFHST0103IをOPENSTATUSとDSNAMEの主判定に採用する。CEMT INQUIRE DSNAME(APP.FILE08.DATA)の応答は採取対象から外す。
    - C. CEMT INQUIRE FILE(FILE08)のFileをDsnと同義の成功表示として扱う。CEMT INQUIRE DSNAME(APP.FILE08.DATA)は実行しない。
    - D. CEMT PERFORM STATISTICS RECORD FILE(FILE08)の結果だけでは確定しない。CEMT INQUIRE DSNAME(APP.FILE08.DATA)のDsnを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 技術上の正答: Dはデータセット照会で Dsn を読みOPENSTATUSとDSNAMEの主値として構成差分を監査しFILE08に残します。
    実行時の背景: 構成監査では統計採取を補助操作としFILE資源の定義値と稼働値の一致をDFHST0103Iと対象FILE08で照合します。
    四つの候補の理由: データセット照会と統計採取の役割を分けるとA: 過去出力では今回の構成監査を示せない点でファイル管理に使いません、B: DFHST0103IはDsnを代替しない点でFILE資源に使えません、C: FileとDsnは確認項目が異なる点でFILE08を採用できません、D: Dsnを主証跡として区別する点で主証跡になります。結論として構成監査のファイル管理・資源で判定する対象は FILE08 です。
    初出語定義: 構成監査で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE08へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 構成監査 FILE08**

    - 検証目的: ファイル管理のFILE資源について構成差分を監査し、FILE08のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE08.DATA)を指定し、FILE08のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE08.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE08.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE08.DATAを読み、OPENSTATUSとDSNAMEと対象FILE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE08)を指定し、FILE08の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE08 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE08)を指定し、FILE08のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE08) Ope Ena Rea Upd Dsname(APP.FILE08.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APP.FILE08.DATA が画面・出力に表示されること
    ② ステップ2 の DFHST0103I が画面・出力に表示されること
    ③ ステップ3 の File が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 通常状態の確認 FILE01 {#c04-i0183}
*分類: ファイル管理*  ・  難易度: 中級

通常状態の確認では ファイル管理 の ファイル照会 を主操作として FILE01 を判定します。基準値と現在値の差への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE01 に残します。通常状態の確認を補助する データセット照会 では Dsn を補助値として FILE01 へ保存します。主判定の通常状態の確認ではファイル管理・資源の ファイル照会 から File を読み FILE01 へ残します。証跡照合の通常状態の確認ではファイル管理・資源の File と Dsn を FILE01 に保存します。記録対応の通常状態の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE01 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で ファイル管理 の ファイル照会 と データセット照会 を用い 通常状態を確定 します。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。File で対象 FILE01 の OPENSTATUSとDSNAME を再現できる記録はどれですか。

    - A. CEMT INQUIRE FILE(FILE01)を先に実行する。対象FILE01のFileをOPENSTATUSとDSNAMEとして記録する。続いてCEMT INQUIRE DSNAME(APP.FILE01.DATA)で同一対象を照合する。 ✅
    - B. CEMT INQUIRE DSNAME(APP.FILE01.DATA)のDsnをOPENSTATUSとDSNAMEの主判定に採用する。CEMT INQUIRE FILE(FILE01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. CEMT PERFORM STATISTICS RECORD FILE(FILE01)のDFHST0103IをFileと同義の成功表示として扱う。CEMT INQUIRE FILE(FILE01)は実行しない。
    - D. CEMT INQUIRE FILE(FILE01)が応答を返した時点で正常とする。応答中のFileの値は記録しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正解の説明: Aはファイル照会で File を読みOPENSTATUSとDSNAMEの主値として通常状態を確定しFILE01に残します。
    背景・仕組み: 通常状態の確認ではデータセット照会を補助操作としFILE資源の基準値と現在値の差をDsnと対象FILE01で照合します。
    選択肢の理由: ファイル照会とデータセット照会の役割を分けるとA: Fileを主値として補助結果と照合する点で正答です、B: DsnはFileを代替しないうえに追加前提も不正な点でFILE01を採用できません、C: DFHST0103IとFileは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではOPENSTATUSとDSNAMEを判定できない点で一次資料と一致しません。結論として通常状態の確認のファイル管理・資源で判定する対象は FILE01 です。
    用語の初出定義: 通常状態の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE01へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 通常状態の確認 FILE01**

    - 検証目的: ファイル管理のFILE資源について通常状態を確定し、FILE01のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE01)を指定し、FILE01のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE01) Ope Ena Rea Upd Dsname(APP.FILE01.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE01.DATA)を指定し、FILE01のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE01.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE01.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE01.DATAを読み、OPENSTATUSとDSNAMEと対象FILE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE01)を指定し、FILE01の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE01 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の File が画面・出力に表示されること
    ② ステップ2 の APP.FILE01.DATA が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### ファイル管理 FILE資源 障害切り分け FILE04 {#c04-i0184}
*分類: ファイル管理*  ・  難易度: 中級

障害切り分けでは ファイル管理 の ファイル照会 を主操作として FILE04 を判定します。最初に失敗した処理への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE04 に残します。障害切り分けを補助する データセット照会 では Dsn を補助値として FILE04 へ保存します。主判定の障害切り分けではファイル管理・資源の ファイル照会 から File を読み FILE04 へ残します。証跡照合の障害切り分けではファイル管理・資源の File と Dsn を FILE04 に保存します。記録対応の障害切り分けではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE04 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 障害切り分けで ファイル管理 の ファイル照会 と データセット照会 の役割を分け 最初に失敗した処理 を調べます。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。対象 FILE04 を誤判定しない進め方はどれですか。

    - A. CEMT PERFORM STATISTICS RECORD FILE(FILE04)のDFHST0103IをFileと同義の成功表示として扱う。CEMT INQUIRE FILE(FILE04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. CEMT INQUIRE FILE(FILE04)が応答を返した時点で正常とする。応答中のFileの値は記録しない。
    - C. CEMT INQUIRE FILE(FILE04)のコマンド文字列だけを記録する。Fileを含む応答行は保存しない。
    - D. CEMT INQUIRE FILE(FILE04)の出力でFILE04とFileが同じ応答にあることを確認する。OPENSTATUSとDSNAMEをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Dはファイル照会で File を読みOPENSTATUSとDSNAMEの主値として障害範囲を限定しFILE04に残します。
    技術的背景: 障害切り分けではデータセット照会を補助操作としFILE資源の最初に失敗した処理をDsnと対象FILE04で照合します。
    四択の評価: ファイル照会とデータセット照会の役割を分けるとA: DFHST0103IとFileは確認項目が異なるうえに追加前提も不正な点でFILE04を採用できません、B: 応答の有無だけではOPENSTATUSとDSNAMEを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではOPENSTATUSとDSNAMEを証明できない点で一次資料と一致しません、D: FILE04とFileを同じ応答で結ぶ点でFILE04を判定できます。結論として障害切り分けのファイル管理・資源で判定する対象は FILE04 です。
    初出語の意味: 障害切り分けで使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE04へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **ファイル管理 FILE資源 障害切り分け FILE04**

    - 検証目的: ファイル管理のFILE資源について障害範囲を限定し、FILE04のOPENSTATUSとDSNAMEを実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE04)を指定し、FILE04のファイル照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    File(FILE04) Ope Ena Rea Upd Dsname(APP.FILE04.DATA)
    ```

    画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE04.DATA)を指定し、FILE04のデータセット照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE DSNAME(APP.FILE04.DATA)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Dsn(APP.FILE04.DATA) Quiesced(No) Retlocks(No)
    ```

    画面・出力にあるAPP.FILE04.DATAを読み、OPENSTATUSとDSNAMEと対象FILE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE04)を指定し、FILE04の統計採取を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD FILE(FILE04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I FILE FILE04 STATISTICS RECORDED
    ```

    画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の File が画面・出力に表示されること
    ② ステップ2 の APP.FILE04.DATA が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf




## CICS Transaction Server for z/OS 6.x > プログラム管理

### CEDA DEFINE FILE 状態確認 理由コード {#c04-i0185}
*分類: プログラム管理*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEDA DEFINE FILE 状態確認 理由コード」は、VSAMなどのFILEリソースをCSDに定義し、データセット名や状態を管理するRDO操作を状態確認の観点で確認する技術項目です。MAX/CUR 欄とAEI8を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、未インストール定義の採用を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEDA DEFINE FILE 状態確認 理由コード**

    - 検証目的: プログラム管理におけるCEDA DEFINE FILEの状態確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=AEI8
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> PUT CICS bridge message for CEMT INQUIRE TASK
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS-MQ BRIDGE REQUEST ACCEPTED
    TRANSACTION CEMT
    COMMAND CEMT INQUIRE TASK
    ```

    画面・出力には CICS-MQ が含まれ、CICS-MQを確認し、未インストール定義の採用を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TASK TRAN(CWXN)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0051988) Tra(CWXN) Sus Tas Pri(001) Sta(U) Use(WEBSRV)
    Uow(C9D5F2EE2DEE8499) Hty(SOCKET) Hva(RECEIVE) Hti(200841) Bac Wai
    ```

    画面・出力には CWXN が含まれ、CWXNを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TRANSACTION(CWXN)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tra(CWXN) Pri(001) Pro(DFHWBXN) Ena Sta Profile(DFHCICST)
    ```

    画面・出力には CWXN が含まれ、CWXNを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CICS-MQ が画面・出力に表示されること
    ② ステップ2 の CWXN が画面・出力に表示されること
    ③ ステップ3 の CWXN が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT INQUIRE FILE 接続確認 属性確認 {#c04-i0186}
*分類: プログラム管理*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEMT INQUIRE FILE 接続確認 属性確認」は、FILEリソースのOPEN/CLOSED、ENABLED/DISABLED、使用状態を確認するメイン端末コマンドを接続確認の観点で確認する技術項目です。FILE 欄とCIC04を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT INQUIRE FILE 接続確認 属性確認**

    - 検証目的: プログラム管理におけるCEMT INQUIRE FILEの接続確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC04
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE TRANSACTION(PAY004) GROUP(TEST) PROGRAM(DFH004)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF TRANSACTION(PAY004) GROUP(TEST)
    PROGRAM ==> DFH004
    PROFILE ==> DFHCICST
    ```

    画面・出力には CEDA が含まれ、CEDAを確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE PROGRAM(DFH004) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF PROGRAM(DFH004) GROUP(TEST)
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
    TRANSACTION PAY004 INSTALLED
    PROGRAM DFH004 INSTALLED
    ```

    画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
    ② ステップ2 の CEDA が画面・出力に表示されること
    ③ ステップ3 の INSTALL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT INQUIRE TCPIPSERVICE 戻りコード確認 表形式 {#c04-i0187}
*分類: プログラム管理*  ・  難易度: 上級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEMT INQUIRE TCPIPSERVICE 戻りコード確認 表形式」は、TCPIPSERVICEのOPEN/CLOSED、PORT、BACKLOG、URMを確認するメイン端末コマンドを戻りコード確認の観点で確認する技術項目です。Tas 行とTCP05を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT INQUIRE TCPIPSERVICE 戻りコード確認 表形式**

    - 検証目的: プログラム管理におけるCEMT INQUIRE TCPIPSERVICEの戻りコード確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=TCP05
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE TCPIPSERVICE(TCP05) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF TCPIPSERVICE(TCP05) GROUP(TEST)
    PROTOCOL ==> HTTP
    PORTNUMBER ==> 08080
    URM ==> DFHWBAAX
    ```

    画面・出力には CEDA が含まれ、CEDAを確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE URIMAP(URI05) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF URIMAP(URI05) GROUP(TEST)
    PATH ==> /pay/095
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
    TCPIPSERVICE TCP05 INSTALLED
    URIMAP URI05 INSTALLED
    ```

    画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
    ② ステップ2 の CEDA が画面・出力に表示されること
    ③ ステップ3 の INSTALL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT SET TRD 接続確認 設定値 {#c04-i0188}
*分類: プログラム管理*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEMT SET TRD 接続確認 設定値」は、トランザクション異常終了コードに対するダンプ取得条件を設定する操作を接続確認の観点で確認する技術項目です。RC 欄とFILE082を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、タスク待機理由の誤読を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT SET TRD 接続確認 設定値**

    - 検証目的: プログラム管理におけるCEMT SET TRDの接続確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=FILE082
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE082)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE082) Vsa Ope Ena Rea Upd Add Bro Del Sha
    ```

    画面・出力には FILE082 が含まれ、FILE082を確認し、タスク待機理由の誤読を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET FILE(FILE082) CLOSED ENABLED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE082) Clo Ena Rea Upd Add Bro Del
    ```

    画面・出力には FILE082 が含まれ、FILE082を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE082)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE082) Clo Ena Rea Upd Add Bro Del
    ```

    画面・出力には FILE082 が含まれ、FILE082を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の FILE082 が画面・出力に表示されること
    ② ステップ2 の FILE082 が画面・出力に表示されること
    ③ ステップ3 の FILE082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CONFDATA trace setting 出力項目確認 キュー状態 {#c04-i0189}
*分類: プログラム管理*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CONFDATA trace setting 出力項目確認 キュー状態」は、トレースに含める機密データ表示をHIDE/SHOWで制御する設定を出力項目確認の観点で確認する技術項目です。PORTNUMBER 欄とPAY030を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CONFDATA trace setting 出力項目確認 キュー状態**

    - 検証目的: プログラム管理におけるCONFDATA trace settingの出力項目確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=PAY030
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> Open Tasks view for CIC30
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tasks view APPLID CIC30
    Task 0051988 Transaction CWXN Status Suspended Wait RECEIVE
    ```

    画面・出力には Tasks が含まれ、Tasksを確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> GET CICSDefinitionTCPIPService TCP30
    → Enter を押す
    ```

    画面・出力:
    ```text
    <response><TCPIPSERVICE name="TCP30" status="OPEN" port="8080" protocol="HTTP" /></response>
    ```

    画面・出力には response が含まれ、responseを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> GET CICSDefinitionTransaction PAY030
    → Enter を押す
    ```

    画面・出力:
    ```text
    <response><TRANSACTION name="PAY030" program="DFH030" status="ENABLED" /></response>
    ```

    画面・出力には response が含まれ、responseを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の Tasks が画面・出力に表示されること
    ② ステップ2 の response が画面・出力に表示されること
    ③ ステップ3 の response が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CWXN transaction リソース照合 処理範囲 {#c04-i0190}
*分類: プログラム管理*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CWXN transaction リソース照合 処理範囲」は、CICS Web SupportのHTTP要求処理に使われるCICS supplied transactionをリソース照合の観点で確認する技術項目です。DFH メッセージとURI26を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、TCP/IPサービス状態の見落としを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CWXN transaction リソース照合 処理範囲**

    - 検証目的: プログラム管理におけるCWXN transactionのリソース照合を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=URI26
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET TRD(AEI5) SYS MAX(1) ADD
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trd(AEI5) Sys Cur(000000) Max(000001) Add
    ```

    画面・出力には AEI5 が含まれ、AEI5を確認し、TCP/IPサービス状態の見落としを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TRD(AEI5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trd(AEI5) Sys Cur(000000) Max(000001) Add
    ```

    画面・出力には AEI5 が含まれ、AEI5を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET SYD(12345) SYS MAX(1) ADD
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYDUMP Syd(12345) Sys Cur(000000) Max(000001) Add
    ```

    画面・出力には SYDUMP が含まれ、SYDUMPを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の AEI5 が画面・出力に表示されること
    ② ステップ2 の AEI5 が画面・出力に表示されること
    ③ ステップ3 の SYDUMP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### Liberty DataSource リソース照合 一致条件 {#c04-i0191}
*分類: プログラム管理*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「Liberty DataSource リソース照合 一致条件」は、server.xmlでDb2 DataSourceを構成し、CICSのDB2CONNを経由する接続設定をリソース照合の観点で確認する技術項目です。TCPIPSERVICE 行とJVMSRV17を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Db2接続前提の欠落を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **Liberty DataSource リソース照合 一致条件**

    - 検証目的: プログラム管理におけるLiberty DataSourceのリソース照合を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=JVMSRV17
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

    画面・出力には CETR が含まれ、CETRを確認し、Db2接続前提の欠落を避けるため対象の現在値を固定する。

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
    TRACE ENTRIES SELECTED FOR APPLID CIC17
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



### URIMAP resource 接続確認 復旧手掛かり {#c04-i0192}
*分類: プログラム管理*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「URIMAP resource 接続確認 復旧手掛かり」は、HTTP要求をTCPIPSERVICE、パス、alias transactionへ対応付けるWebサポート定義を接続確認の観点で確認する技術項目です。URIMAP 行と00142を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **URIMAP resource 接続確認 復旧手掛かり**

    - 検証目的: プログラム管理におけるURIMAP resourceの接続確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=00142
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TCPIPSERVICE(TCP13)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcp(TCP13) Ope Por(08080) Pro(Http) Backlog(00050) Urm(DFHWBAAX)
    ```

    画面・出力には TCP13 が含まれ、TCP13を確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET TCPIPSERVICE(TCP13) OPEN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcp(TCP13) Ope Por(08080) Pro(Http) Backlog(00050)
    ```

    画面・出力には TCP13 が含まれ、TCP13を読み、出典資料の出力項目と運用記録を対応させる。

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

    - 合格条件: ① ステップ1 の TCP13 が画面・出力に表示されること
    ② ステップ2 の TCP13 が画面・出力に表示されること
    ③ ステップ3 の Tcpip が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 ログとの照合 PGM07 {#c04-i0193}
*分類: プログラム管理*  ・  難易度: 中級

ログとの照合では プログラム管理 の プログラム照会 を主操作として PGM07 を判定します。時刻と対象識別子への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM07 に残します。ログとの照合を補助する 使用タスク確認 では Status を補助値として PGM07 へ保存します。主判定のログとの照合ではプログラム管理・資源の プログラム照会 から Prog を読み PGM07 へ残します。証跡照合のログとの照合ではプログラム管理・資源の Prog と Status を PGM07 に保存します。記録対応のログとの照合ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM07 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** ログとの照合で プログラム管理 の プログラム照会 と 使用タスク確認 を組み合わせる際は PROGRAM資源 がロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源という仕組みを前提にします。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。Prog と PROGRAM名とNEWCOPY結果 を対象 PGM07 で確認する組合せはどれですか。

    - A. Progを含むプログラム照会の応答行を保存する。その応答を得るためCEMT INQUIRE PROGRAM(PGM07)を使用する。対象PGM07のPROGRAM名とNEWCOPY結果として記録する。 ✅
    - B. CEMT INQUIRE PROGRAM(PGM07)が応答を返した時点で正常とする。応答中のProgの値は記録しない。PROGRAMをProgと同じ判定値とみなし対象PGM07の主証跡にする。PROGRAM資源の時刻と対象識別子は確認済みとして扱う。さらにCEDA VIEW PROGRAM(PGM07) GROUP(GRP07)のPROGRAMをProgと同種の値として併記する。
    - C. CEMT INQUIRE PROGRAM(PGM07)のコマンド文字列だけを記録する。Progを含む応答行は保存しない。
    - D. PROGRAM資源の停止または再定義を実施する。その後にCEMT INQUIRE PROGRAM(PGM07)でProgを採取する。

    正解: **A** ／ 難易度: 中級

    **解説:** 適切な判定: Aはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として操作とログを対応しPGM07に残します。
    機能の仕組み: ログとの照合では使用タスク確認を補助操作としPROGRAM資源の時刻と対象識別子をStatusと対象PGM07で照合します。
    各候補の評価: プログラム照会と使用タスク確認の役割を分けるとA: Progの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではPROGRAM名とNEWCOPY結果を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではPROGRAM名とNEWCOPY結果を証明できない点でPROGRAM名とNEWCOPY結果を確認できません、D: 変更前のPROGRAM名とNEWCOPY結果を失う点で使用タスク確認の範囲を越えます。結論としてログとの照合のプログラム管理・資源で判定する対象は PGM07 です。
    用語の定義: ログとの照合で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM07へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 ログとの照合 PGM07**

    - 検証目的: プログラム管理のPROGRAM資源について操作とログを対応し、PGM07のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM07)を指定し、PGM07のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM07) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM07)を指定し、PGM07の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064107) Prog(PGM07) Tra(PAY07) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM07) GROUP(GRP07)を指定し、PGM07の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM07) GROUP(GRP07)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM07) GROUP(GRP07) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Prog が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の PROGRAM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 代替経路の確認 PGM10 {#c04-i0194}
*分類: プログラム管理*  ・  難易度: 中級

代替経路の確認では プログラム管理 の プログラム照会 を主操作として PGM10 を判定します。主経路との役割差への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM10 に残します。代替経路の確認を補助する 使用タスク確認 では Status を補助値として PGM10 へ保存します。主判定の代替経路の確認ではプログラム管理・資源の プログラム照会 から Prog を読み PGM10 へ残します。証跡照合の代替経路の確認ではプログラム管理・資源の Prog と Status を PGM10 に保存します。記録対応の代替経路の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM10 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で プログラム管理 の プログラム照会 と 使用タスク確認 を実施し PROGRAM資源 の役割を確認します。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM10 の証跡を取る方法はどれですか。

    - A. CEMT INQUIRE PROGRAM(PGM10)のコマンド文字列だけを記録する。Progを含む応答行は保存しない。
    - B. PROGRAM資源の停止または再定義を実施する。その後にCEMT INQUIRE PROGRAM(PGM10)でProgを採取する。
    - C. リソース定義のグループ名とインストール結果を確認する。その値をプログラム管理のPGM10にも適用する。
    - D. CEMT INQUIRE PROGRAM(PGM10)とCEMT INQUIRE TASK PROGRAM(PGM10)の対象名をそろえる。前者のProgをPROGRAM名とNEWCOPY結果の判定値として採用する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい判定結果: Dはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として代替手段の成立を確認しPGM10に残します。
    運用上の背景: 代替経路の確認では使用タスク確認を補助操作としPROGRAM資源の主経路との役割差をStatusと対象PGM10で照合します。
    候補別の検討: プログラム照会と使用タスク確認の役割を分けるとA: 入力記録だけではPROGRAM名とNEWCOPY結果を証明できない点で一次資料と一致しません、B: 変更前のPROGRAM名とNEWCOPY結果を失う点でPROGRAM名とNEWCOPY結果を確認できません、C: リソース定義の値ではProgを確認できない点で使用タスク確認の範囲を越えます、D: 同じ対象名のProgを採用する点で現在値を示します。結論として代替経路の確認のプログラム管理・資源で判定する対象は PGM10 です。
    重要用語の定義: 代替経路の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM10へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 代替経路の確認 PGM10**

    - 検証目的: プログラム管理のPROGRAM資源について代替手段の成立を確認し、PGM10のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM10)を指定し、PGM10のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM10) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM10)を指定し、PGM10の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064110) Prog(PGM10) Tra(PAY10) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM10) GROUP(GRP10)を指定し、PGM10の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM10) GROUP(GRP10)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM10) GROUP(GRP10) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Prog が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の PROGRAM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 変更前の確認 PGM02 {#c04-i0195}
*分類: プログラム管理*  ・  難易度: 中級

変更前の確認では プログラム管理 の 使用タスク確認 を主操作として PGM02 を判定します。変更対象と非対象の境界への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM02 に残します。変更前の確認を補助する 定義参照 では PROGRAM を補助値として PGM02 へ保存します。主判定の変更前の確認ではプログラム管理・資源の 使用タスク確認 から Status を読み PGM02 へ残します。証跡照合の変更前の確認ではプログラム管理・資源の Status と PROGRAM を PGM02 に保存します。記録対応の変更前の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM02 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更前の確認で プログラム管理 の 使用タスク確認 と 定義参照 の役割を分け 変更対象と非対象の境界 を調べます。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM02 を誤判定しない進め方はどれですか。

    - A. CEMT INQUIRE TASK PROGRAM(PGM02)を対象名なしで実行する。一覧の先頭行をPGM02の結果として記録する。
    - B. 前回保存したCEMT INQUIRE TASK PROGRAM(PGM02)の結果を使う。今回のCEDA VIEW PROGRAM(PGM02) GROUP(GRP02)の結果と同一時点の証跡として比較する。
    - C. 保存済みのPGM02の出力を再利用する。今回のCEMT INQUIRE TASK PROGRAM(PGM02)とCEDA VIEW PROGRAM(PGM02) GROUP(GRP02)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象PGM02についてCEMT INQUIRE TASK PROGRAM(PGM02)の応答からStatusを確認する。CEDA VIEW PROGRAM(PGM02) GROUP(GRP02)は補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 採用理由: Dは使用タスク確認で Status を読みPROGRAM名とNEWCOPY結果の主値として変更前の証跡を保存しPGM02に残します。
    動作の背景: 変更前の確認では定義参照を補助操作としPROGRAM資源の変更対象と非対象の境界をPROGRAMと対象PGM02で照合します。
    各選択肢の検討: 使用タスク確認と定義参照の役割を分けるとA: 先頭行はPGM02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で使用タスク確認を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でプログラム管理に使いません、D: Statusと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のプログラム管理・資源で判定する対象は PGM02 です。
    初出用語の定義: 変更前の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM02へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 変更前の確認 PGM02**

    - 検証目的: プログラム管理のPROGRAM資源について変更前の証跡を保存し、PGM02のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM02)を指定し、PGM02の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064102) Prog(PGM02) Tra(PAY02) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM02) GROUP(GRP02)を指定し、PGM02の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM02) GROUP(GRP02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM02) GROUP(GRP02) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM02)を指定し、PGM02のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM02)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM02) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の PROGRAM が画面・出力に表示されること
    ③ ステップ3 の Prog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 変更後の確認 PGM03 {#c04-i0196}
*分類: プログラム管理*  ・  難易度: 中級

変更後の確認では プログラム管理 の 定義参照 を主操作として PGM03 を判定します。反映値と残存値への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM03 に残します。変更後の確認を補助する プログラム照会 では Prog を補助値として PGM03 へ保存します。主判定の変更後の確認ではプログラム管理・資源の 定義参照 から PROGRAM を読み PGM03 へ残します。証跡照合の変更後の確認ではプログラム管理・資源の PROGRAM と Prog を PGM03 に保存します。記録対応の変更後の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM03 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 変更後の確認で プログラム管理 の 定義参照 と プログラム照会 を使い 変更結果を検証 します。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。PROGRAM を読み対象 PGM03 を切り分ける確認方法はどれですか。

    - A. CEMT INQUIRE PROGRAM(PGM03)で周辺状態を押さえる。その後にCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)でPROGRAMを確認して変更結果を検証する。 ✅
    - B. PROGRAM資源の停止または再定義を実施する。その後にCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)でPROGRAMを採取する。
    - C. Liberty JVMのJVMSTATUSとPROFILEを確認する。その値をプログラム管理のPGM03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。PROGRAM資源の反映値と残存値は確認済みとして扱う。さらにCEMT INQUIRE TASK PROGRAM(PGM03)のStatusをPROGRAMと同種の値として併記する。
    - D. CEMT INQUIRE PROGRAM(PGM03)が成功したためCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)のPROGRAMも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正答の根拠: Aは定義参照で PROGRAM を読みPROGRAM名とNEWCOPY結果の主値として変更結果を検証しPGM03に残します。
    内部の仕組み: 変更後の確認ではプログラム照会を補助操作としPROGRAM資源の反映値と残存値をProgと対象PGM03で照合します。
    誤答を含む比較: 定義参照とプログラム照会の役割を分けるとA: 周辺状態の後にPROGRAMを確認する点でPGM03を判定できます、B: 変更前のPROGRAM名とNEWCOPY結果を失う点でプログラム照会の範囲を越えます、C: Liberty JVMの値ではPROGRAMを確認できないうえに追加前提も不正な点でPGM03の値を示しません、D: 補助操作の成功ではPROGRAMを確定できない点で変更後の確認に合いません。結論として変更後の確認のプログラム管理・資源で判定する対象は PGM03 です。
    用語定義: 変更後の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM03へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 変更後の確認 PGM03**

    - 検証目的: プログラム管理のPROGRAM資源について変更結果を検証し、PGM03のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)を指定し、PGM03の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM03) GROUP(GRP03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM03) GROUP(GRP03) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM03)を指定し、PGM03のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM03) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM03)を指定し、PGM03の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064103) Prog(PGM03) Tra(PAY03) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROGRAM が画面・出力に表示されること
    ② ステップ2 の Prog が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 引継ぎ記録 PGM09 {#c04-i0197}
*分類: プログラム管理*  ・  難易度: 中級

引継ぎ記録では プログラム管理 の 定義参照 を主操作として PGM09 を判定します。次担当者が追跡できる証跡への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM09 に残します。引継ぎ記録を補助する プログラム照会 では Prog を補助値として PGM09 へ保存します。主判定の引継ぎ記録ではプログラム管理・資源の 定義参照 から PROGRAM を読み PGM09 へ残します。証跡照合の引継ぎ記録ではプログラム管理・資源の PROGRAM と Prog を PGM09 に保存します。記録対応の引継ぎ記録ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM09 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で プログラム管理 の 定義参照 と プログラム照会 を使い 再現可能な記録を作成 します。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。PROGRAM を読み対象 PGM09 を切り分ける確認方法はどれですか。

    - A. CEMT INQUIRE PROGRAM(PGM09)が成功したためCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)のPROGRAMも正常だと推定する。主出力は保存しない。
    - B. CEDA VIEW PROGRAM(PGM09) GROUP(GRP09)を対象名なしで実行する。一覧の先頭行をPGM09の結果として記録する。
    - C. 対象名PGM09を指定してCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)を実行する。応答中のPROGRAMと時刻を保存する。CEMT INQUIRE PROGRAM(PGM09)で周辺状態を補完する。 ✅
    - D. 前回保存したCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)の結果を使う。今回のCEMT INQUIRE PROGRAM(PGM09)の結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 中級

    **解説:** 採用操作の理由: Cは定義参照で PROGRAM を読みPROGRAM名とNEWCOPY結果の主値として再現可能な記録を作成しPGM09に残します。
    製品内の仕組み: 引継ぎ記録ではプログラム照会を補助操作としPROGRAM資源の次担当者が追跡できる証跡をProgと対象PGM09で照合します。
    選択肢別の説明: 定義参照とプログラム照会の役割を分けるとA: 補助操作の成功ではPROGRAMを確定できない点でPGM09の値を示しません、B: 先頭行はPGM09と確定できない点で引継ぎ記録に合いません、C: PROGRAMと時刻を保存する点で定義参照に合います、D: 採取時刻が異なる点でプログラム管理に使いません。結論として引継ぎ記録のプログラム管理・資源で判定する対象は PGM09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM09へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 引継ぎ記録 PGM09**

    - 検証目的: プログラム管理のPROGRAM資源について再現可能な記録を作成し、PGM09のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)を指定し、PGM09の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM09) GROUP(GRP09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM09) GROUP(GRP09) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM09)を指定し、PGM09のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM09) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM09)を指定し、PGM09の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064109) Prog(PGM09) Tra(PAY09) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROGRAM が画面・出力に表示されること
    ② ステップ2 の Prog が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 復旧後の確認 PGM06 {#c04-i0198}
*分類: プログラム管理*  ・  難易度: 中級

復旧後の確認では プログラム管理 の 定義参照 を主操作として PGM06 を判定します。再発していないことを示す値への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM06 に残します。復旧後の確認を補助する プログラム照会 では Prog を補助値として PGM06 へ保存します。主判定の復旧後の確認ではプログラム管理・資源の 定義参照 から PROGRAM を読み PGM06 へ残します。証跡照合の復旧後の確認ではプログラム管理・資源の PROGRAM と Prog を PGM06 に保存します。記録対応の復旧後の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM06 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で プログラム管理 の 定義参照 と プログラム照会 を照合し 再発していないことを示す値 を確かめます。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。PROGRAM を読む前に対象 PGM06 へ行う確認はどれですか。

    - A. トレースのTRACETYPEとSTATUSを確認する。その値をプログラム管理のPGM06にも適用する。
    - B. CEMT INQUIRE PROGRAM(PGM06)が成功したためCEDA VIEW PROGRAM(PGM06) GROUP(GRP06)のPROGRAMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象PGM06へ引き継げるものとする。PROGRAM資源の再発していないことを示す値は確認済みとして扱う。さらにCEMT INQUIRE TASK PROGRAM(PGM06)のStatusをPROGRAMと同種の値として併記する。
    - C. CEDA VIEW PROGRAM(PGM06) GROUP(GRP06)を対象名なしで実行する。一覧の先頭行をPGM06の結果として記録する。
    - D. CEDA VIEW PROGRAM(PGM06) GROUP(GRP06)でPROGRAMを取得してからCEMT INQUIRE TASK PROGRAM(PGM06)でStatusを照合する。PGM06のPROGRAM名とNEWCOPY結果を両出力から確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答内容: Dは定義参照で PROGRAM を読みPROGRAM名とNEWCOPY結果の主値として復旧後の安定性を確認しPGM06に残します。
    構成上の背景: 復旧後の確認ではプログラム照会を補助操作としPROGRAM資源の再発していないことを示す値をProgと対象PGM06で照合します。
    候補ごとの理由: 定義参照とプログラム照会の役割を分けるとA: トレースの値ではPROGRAMを確認できない点でプログラム照会の範囲を越えます、B: 補助操作の成功ではPROGRAMを確定できないうえに追加前提も不正な点でPGM06の値を示しません、C: 先頭行はPGM06と確定できない点で復旧後の確認に合いません、D: PROGRAMとStatusを順に照合する点で定義参照に合います。結論として復旧後の確認のプログラム管理・資源で判定する対象は PGM06 です。
    初出用語: 復旧後の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM06へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 復旧後の確認 PGM06**

    - 検証目的: プログラム管理のPROGRAM資源について復旧後の安定性を確認し、PGM06のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM06) GROUP(GRP06)を指定し、PGM06の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM06) GROUP(GRP06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM06) GROUP(GRP06) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM06)を指定し、PGM06のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM06) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM06)を指定し、PGM06の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM06)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064106) Prog(PGM06) Tra(PAY06) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROGRAM が画面・出力に表示されること
    ② ステップ2 の Prog が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 復旧準備 PGM05 {#c04-i0199}
*分類: プログラム管理*  ・  難易度: 中級

復旧準備では プログラム管理 の 使用タスク確認 を主操作として PGM05 を判定します。再開前に必要な整合性への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM05 に残します。復旧準備を補助する 定義参照 では PROGRAM を補助値として PGM05 へ保存します。主判定の復旧準備ではプログラム管理・資源の 使用タスク確認 から Status を読み PGM05 へ残します。証跡照合の復旧準備ではプログラム管理・資源の Status と PROGRAM を PGM05 に保存します。記録対応の復旧準備ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM05 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 復旧準備で プログラム管理 の 使用タスク確認 と 定義参照 を用い 復旧条件を確認 します。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。Status で対象 PGM05 の PROGRAM名とNEWCOPY結果 を再現できる記録はどれですか。

    - A. 前回保存したCEMT INQUIRE TASK PROGRAM(PGM05)の結果を使う。今回のCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)の結果と同一時点の証跡として比較する。
    - B. 保存済みのPGM05の出力を再利用する。今回のCEMT INQUIRE TASK PROGRAM(PGM05)とCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)は実行済みとして扱う。
    - C. 変更を加えずCEMT INQUIRE TASK PROGRAM(PGM05)を実行する。Statusを保存する。差分はCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)の結果と対象名で対応させる。 ✅
    - D. CEDA VIEW PROGRAM(PGM05) GROUP(GRP05)のPROGRAMをPROGRAM名とNEWCOPY結果の主判定に採用する。CEMT INQUIRE TASK PROGRAM(PGM05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 中級

    **解説:** 選定理由: Cは使用タスク確認で Status を読みPROGRAM名とNEWCOPY結果の主値として復旧条件を確認しPGM05に残します。
    処理の仕組み: 復旧準備では定義参照を補助操作としPROGRAM資源の再開前に必要な整合性をPROGRAMと対象PGM05で照合します。
    選択結果の内訳: 使用タスク確認と定義参照の役割を分けるとA: 採取時刻が異なる点で使用タスク確認を代替しません、B: 過去出力では今回の復旧準備を示せない点でプログラム管理に使いません、C: 変更前のStatusを保存する点で正答です、D: PROGRAMはStatusを代替しないうえに追加前提も不正な点でPGM05を採用できません。結論として復旧準備のプログラム管理・資源で判定する対象は PGM05 です。
    用語の説明: 復旧準備で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM05へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 復旧準備 PGM05**

    - 検証目的: プログラム管理のPROGRAM資源について復旧条件を確認し、PGM05のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM05)を指定し、PGM05の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064105) Prog(PGM05) Tra(PAY05) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)を指定し、PGM05の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM05) GROUP(GRP05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM05) GROUP(GRP05) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM05)を指定し、PGM05のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM05)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM05) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の PROGRAM が画面・出力に表示されること
    ③ ステップ3 の Prog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 構成監査 PGM08 {#c04-i0200}
*分類: プログラム管理*  ・  難易度: 中級

構成監査では プログラム管理 の 使用タスク確認 を主操作として PGM08 を判定します。定義値と稼働値の一致への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM08 に残します。構成監査を補助する 定義参照 では PROGRAM を補助値として PGM08 へ保存します。主判定の構成監査ではプログラム管理・資源の 使用タスク確認 から Status を読み PGM08 へ残します。証跡照合の構成監査ではプログラム管理・資源の Status と PROGRAM を PGM08 に保存します。記録対応の構成監査ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM08 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 構成監査で プログラム管理 の 使用タスク確認 と 定義参照 の役割を分け 定義値と稼働値の一致 を調べます。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM08 を誤判定しない進め方はどれですか。

    - A. 保存済みのPGM08の出力を再利用する。今回のCEMT INQUIRE TASK PROGRAM(PGM08)とCEDA VIEW PROGRAM(PGM08) GROUP(GRP08)は実行済みとして扱う。
    - B. CEDA VIEW PROGRAM(PGM08) GROUP(GRP08)の結果だけでは確定しない。CEMT INQUIRE TASK PROGRAM(PGM08)のStatusを主証跡として構成差分を監査する。 ✅
    - C. CEDA VIEW PROGRAM(PGM08) GROUP(GRP08)のPROGRAMをPROGRAM名とNEWCOPY結果の主判定に採用する。CEMT INQUIRE TASK PROGRAM(PGM08)の応答は採取対象から外す。
    - D. CEMT INQUIRE PROGRAM(PGM08)のProgをStatusと同義の成功表示として扱う。CEMT INQUIRE TASK PROGRAM(PGM08)は実行しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 技術上の正答: Bは使用タスク確認で Status を読みPROGRAM名とNEWCOPY結果の主値として構成差分を監査しPGM08に残します。
    実行時の背景: 構成監査では定義参照を補助操作としPROGRAM資源の定義値と稼働値の一致をPROGRAMと対象PGM08で照合します。
    四つの候補の理由: 使用タスク確認と定義参照の役割を分けるとA: 過去出力では今回の構成監査を示せない点でプログラム管理に使いません、B: Statusを主証跡として区別する点で正答です、C: PROGRAMはStatusを代替しない点でPGM08を採用できません、D: ProgとStatusは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のプログラム管理・資源で判定する対象は PGM08 です。
    初出語定義: 構成監査で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM08へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 構成監査 PGM08**

    - 検証目的: プログラム管理のPROGRAM資源について構成差分を監査し、PGM08のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM08)を指定し、PGM08の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064108) Prog(PGM08) Tra(PAY08) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM08) GROUP(GRP08)を指定し、PGM08の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM08) GROUP(GRP08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM08) GROUP(GRP08) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM08)を指定し、PGM08のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM08)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM08) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の PROGRAM が画面・出力に表示されること
    ③ ステップ3 の Prog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 通常状態の確認 PGM01 {#c04-i0201}
*分類: プログラム管理*  ・  難易度: 中級

通常状態の確認では プログラム管理 の プログラム照会 を主操作として PGM01 を判定します。基準値と現在値の差への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM01 に残します。通常状態の確認を補助する 使用タスク確認 では Status を補助値として PGM01 へ保存します。主判定の通常状態の確認ではプログラム管理・資源の プログラム照会 から Prog を読み PGM01 へ残します。証跡照合の通常状態の確認ではプログラム管理・資源の Prog と Status を PGM01 に保存します。記録対応の通常状態の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM01 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で プログラム管理 の プログラム照会 と 使用タスク確認 を組み合わせる際は PROGRAM資源 がロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源という仕組みを前提にします。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。Prog と PROGRAM名とNEWCOPY結果 を対象 PGM01 で確認する組合せはどれですか。

    - A. CEMT INQUIRE TASK PROGRAM(PGM01)のStatusをPROGRAM名とNEWCOPY結果の主判定に採用する。CEMT INQUIRE PROGRAM(PGM01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. CEDA VIEW PROGRAM(PGM01) GROUP(GRP01)のPROGRAMをProgと同義の成功表示として扱う。CEMT INQUIRE PROGRAM(PGM01)は実行しない。
    - C. CEMT INQUIRE PROGRAM(PGM01)を先に実行する。対象PGM01のProgをPROGRAM名とNEWCOPY結果として記録する。続いてCEMT INQUIRE TASK PROGRAM(PGM01)で同一対象を照合する。 ✅
    - D. CEMT INQUIRE PROGRAM(PGM01)が応答を返した時点で正常とする。応答中のProgの値は記録しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解の説明: Cはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として通常状態を確定しPGM01に残します。
    背景・仕組み: 通常状態の確認では使用タスク確認を補助操作としPROGRAM資源の基準値と現在値の差をStatusと対象PGM01で照合します。
    選択肢の理由: プログラム照会と使用タスク確認の役割を分けるとA: StatusはProgを代替しないうえに追加前提も不正な点でPROGRAM資源に使えません、B: PROGRAMとProgは確認項目が異なる点でPGM01を採用できません、C: Progを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではPROGRAM名とNEWCOPY結果を判定できない点で一次資料と一致しません。結論として通常状態の確認のプログラム管理・資源で判定する対象は PGM01 です。
    用語の初出定義: 通常状態の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM01へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 通常状態の確認 PGM01**

    - 検証目的: プログラム管理のPROGRAM資源について通常状態を確定し、PGM01のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM01)を指定し、PGM01のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM01) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM01)を指定し、PGM01の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064101) Prog(PGM01) Tra(PAY01) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM01) GROUP(GRP01)を指定し、PGM01の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM01) GROUP(GRP01)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM01) GROUP(GRP01) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Prog が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の PROGRAM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### プログラム管理 PROGRAM資源 障害切り分け PGM04 {#c04-i0202}
*分類: プログラム管理*  ・  難易度: 中級

障害切り分けでは プログラム管理 の プログラム照会 を主操作として PGM04 を判定します。最初に失敗した処理への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM04 に残します。障害切り分けを補助する 使用タスク確認 では Status を補助値として PGM04 へ保存します。主判定の障害切り分けではプログラム管理・資源の プログラム照会 から Prog を読み PGM04 へ残します。証跡照合の障害切り分けではプログラム管理・資源の Prog と Status を PGM04 に保存します。記録対応の障害切り分けではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM04 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** 障害切り分けで プログラム管理 の プログラム照会 と 使用タスク確認 を実施し PROGRAM資源 の役割を確認します。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM04 の証跡を取る方法はどれですか。

    - A. CEDA VIEW PROGRAM(PGM04) GROUP(GRP04)のPROGRAMをProgと同義の成功表示として扱う。CEMT INQUIRE PROGRAM(PGM04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. CEMT INQUIRE PROGRAM(PGM04)の出力でPGM04とProgが同じ応答にあることを確認する。PROGRAM名とNEWCOPY結果をその応答から採取する。 ✅
    - C. CEMT INQUIRE PROGRAM(PGM04)が応答を返した時点で正常とする。応答中のProgの値は記録しない。
    - D. CEMT INQUIRE PROGRAM(PGM04)のコマンド文字列だけを記録する。Progを含む応答行は保存しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Bはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として障害範囲を限定しPGM04に残します。
    技術的背景: 障害切り分けでは使用タスク確認を補助操作としPROGRAM資源の最初に失敗した処理をStatusと対象PGM04で照合します。
    四択の評価: プログラム照会と使用タスク確認の役割を分けるとA: PROGRAMとProgは確認項目が異なるうえに追加前提も不正な点でPGM04を採用できません、B: PGM04とProgを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではPROGRAM名とNEWCOPY結果を判定できない点で一次資料と一致しません、D: 入力記録だけではPROGRAM名とNEWCOPY結果を証明できない点でPROGRAM名とNEWCOPY結果を確認できません。結論として障害切り分けのプログラム管理・資源で判定する対象は PGM04 です。
    初出語の意味: 障害切り分けで使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM04へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **プログラム管理 PROGRAM資源 障害切り分け PGM04**

    - 検証目的: プログラム管理のPROGRAM資源について障害範囲を限定し、PGM04のPROGRAM名とNEWCOPY結果を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM04)を指定し、PGM04のプログラム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(PGM04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS
    Prog(PGM04) Ena Resc Language(COBOL) Usecount(00000004)
    ```

    画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM04)を指定し、PGM04の使用タスク確認を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE TASK PROGRAM(PGM04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0064104) Prog(PGM04) Tra(PAY04) Status(RUNNING)
    ```

    画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM04) GROUP(GRP04)を指定し、PGM04の定義参照を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEDA VIEW PROGRAM(PGM04) GROUP(GRP04)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PROGRAM(PGM04) GROUP(GRP04) STATUS(ENABLED) DATALOCATION(ANY)
    ```

    画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Prog が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の PROGRAM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf




## CICS Transaction Server for z/OS 6.x > メイン端末運用

### CEDA DEFINE TCPIPSERVICE 状態確認 出力比較 {#c04-i0203}
*分類: メイン端末運用*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEDA DEFINE TCPIPSERVICE 状態確認 出力比較」は、CICS Web SupportやIPICの入口となるTCPIPSERVICEを定義するRDO操作を状態確認の観点で確認する技術項目です。FILE 欄とPAY040を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、タスク待機理由の誤読を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEDA DEFINE TCPIPSERVICE 状態確認 出力比較**

    - 検証目的: メイン端末運用におけるCEDA DEFINE TCPIPSERVICEの状態確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=PAY040
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

    画面・出力には Tasks が含まれ、Tasksを確認し、タスク待機理由の誤読を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> GET CICSDefinitionTCPIPService TCP10
    → Enter を押す
    ```

    画面・出力:
    ```text
    <response><TCPIPSERVICE name="TCP10" status="OPEN" port="8080" protocol="HTTP" /></response>
    ```

    画面・出力には response が含まれ、responseを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> GET CICSDefinitionTransaction PAY040
    → Enter を押す
    ```

    画面・出力:
    ```text
    <response><TRANSACTION name="PAY040" program="DFH040" status="ENABLED" /></response>
    ```

    画面・出力には response が含まれ、responseを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の Tasks が画面・出力に表示されること
    ② ステップ2 の response が画面・出力に表示されること
    ③ ステップ3 の response が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT INQUIRE TASK 状態確認 状態確認 {#c04-i0204}
*分類: メイン端末運用*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT INQUIRE TASK 状態確認 状態確認」は、ユーザータスクのTASKID、TRANID、UOW、待機理由、TCB種別を表示するメイン端末コマンドを状態確認の観点で確認する技術項目です。Uow 欄とDFH001を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT INQUIRE TASK 状態確認 状態確認**

    - 検証目的: メイン端末運用におけるCEMT INQUIRE TASKの状態確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=DFH001
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
    Tas(0000100) Tra(PAY001) Sus Tas Pri(001) Sta(U) Use(USR001)
    Uow(C9D5F2EE2DEE0000) Hty(SOCKET) Hva(RECEIVE) Bac Wai
    ```

    画面・出力には PAY001 が含まれ、PAY001を確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TRANSACTION(PAY001)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tra(PAY001) Pri(001) Pro(DFH001) Ena Sta Pro Ena Resc(DFHPROF)
    ```

    画面・出力には PAY001 が含まれ、PAY001を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE PROGRAM(DFH001)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Pro(DFH001) Leng(0001234) Resc(0001) Ced Ena Pri Dplsubsys(CICS)
    ```

    画面・出力には DFH001 が含まれ、DFH001を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の PAY001 が画面・出力に表示されること
    ② ステップ2 の PAY001 が画面・出力に表示されること
    ③ ステップ3 の DFH001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT INQUIRE TRANSACTION トレース確認 再開位置 {#c04-i0205}
*分類: メイン端末運用*  ・  難易度: 上級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT INQUIRE TRANSACTION トレース確認 再開位置」は、トランザクション定義、利用可否、プロファイル、実行属性を確認するメイン端末コマンドをトレース確認の観点で確認する技術項目です。DFH メッセージとFILE092を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT INQUIRE TRANSACTION トレース確認 再開位置**

    - 検証目的: メイン端末運用におけるCEMT INQUIRE TRANSACTIONのトレース確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=FILE092
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE092)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE092) Vsa Ope Ena Rea Upd Add Bro Del Sha
    ```

    画面・出力には FILE092 が含まれ、FILE092を確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET FILE(FILE092) CLOSED ENABLED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE092) Clo Ena Rea Upd Add Bro Del
    ```

    画面・出力には FILE092 が含まれ、FILE092を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE FILE(FILE092)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fil(FILE092) Clo Ena Rea Upd Add Bro Del
    ```

    画面・出力には FILE092 が含まれ、FILE092を残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の FILE092 が画面・出力に表示されること
    ② ステップ2 の FILE092 が画面・出力に表示されること
    ③ ステップ3 の FILE092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT SET SYD 接続確認 更新対象 {#c04-i0206}
*分類: メイン端末運用*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT SET SYD 接続確認 更新対象」は、DFHメッセージに対するシステムダンプ取得条件を設定する操作を接続確認の観点で確認する技術項目です。TCPIPSERVICE 行と00152を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT SET SYD 接続確認 更新対象**

    - 検証目的: メイン端末運用におけるCEMT SET SYDの接続確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=00152
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TCPIPSERVICE(TCP23)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcp(TCP23) Ope Por(08080) Pro(Http) Backlog(00050) Urm(DFHWBAAX)
    ```

    画面・出力には TCP23 が含まれ、TCP23を確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET TCPIPSERVICE(TCP23) OPEN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tcp(TCP23) Ope Por(08080) Pro(Http) Backlog(00050)
    ```

    画面・出力には TCP23 が含まれ、TCP23を読み、出典資料の出力項目と運用記録を対応させる。

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

    - 合格条件: ① ステップ1 の TCP23 が画面・出力に表示されること
    ② ステップ2 の TCP23 が画面・出力に表示されること
    ③ ステップ3 の Tcpip が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CEMT SET TCPIPSERVICE 戻りコード確認 実行順序 {#c04-i0207}
*分類: メイン端末運用*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT SET TCPIPSERVICE 戻りコード確認 実行順序」は、TCP/IPサービスのOPEN/CLOSEやBACKLOGなどを即時変更するメイン端末操作を戻りコード確認の観点で確認する技術項目です。PORTNUMBER 欄とURI06を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Db2接続前提の欠落を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CEMT SET TCPIPSERVICE 戻りコード確認 実行順序**

    - 検証目的: メイン端末運用におけるCEMT SET TCPIPSERVICEの戻りコード確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=URI06
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET TRD(AEI5) SYS MAX(1) ADD
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trd(AEI5) Sys Cur(000000) Max(000001) Add
    ```

    画面・出力には AEI5 が含まれ、AEI5を確認し、Db2接続前提の欠落を避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TRD(AEI5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trd(AEI5) Sys Cur(000000) Max(000001) Add
    ```

    画面・出力には AEI5 が含まれ、AEI5を読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT SET SYD(12345) SYS MAX(1) ADD
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYDUMP Syd(12345) Sys Cur(000000) Max(000001) Add
    ```

    画面・出力には SYDUMP が含まれ、SYDUMPを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の AEI5 が画面・出力に表示されること
    ② ステップ2 の AEI5 が画面・出力に表示されること
    ③ ステップ3 の SYDUMP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### CICS Explorer Tasks view リソース照合 ボリューム状態 {#c04-i0208}
*分類: メイン端末運用*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CICS Explorer Tasks view リソース照合 ボリューム状態」は、CEMT INQUIRE TASK相当のタスク情報をGUIで確認するビューをリソース照合の観点で確認する技術項目です。PROGRAM 欄とJVMSRV07を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、未インストール定義の採用を名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CICS Explorer Tasks view リソース照合 ボリューム状態**

    - 検証目的: メイン端末運用におけるCICS Explorer Tasks viewのリソース照合を机上確認する。
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

    画面・出力には CETR が含まれ、CETRを確認し、未インストール定義の採用を避けるため対象の現在値を固定する。

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



### CICS-MQ bridge 接続確認 停止確認 {#c04-i0209}
*分類: メイン端末運用*  ・  難易度: 初級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CICS-MQ bridge 接続確認 停止確認」は、MQメッセージから3270トランザクションを起動し、CEMTなどを橋渡しする連携機能を接続確認の観点で確認する技術項目です。TCB 欄とCIC14を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、TCP/IPサービス状態の見落としを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **CICS-MQ bridge 接続確認 停止確認**

    - 検証目的: メイン端末運用におけるCICS-MQ bridgeの接続確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC14
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE TRANSACTION(PAY014) GROUP(TEST) PROGRAM(DFH014)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF TRANSACTION(PAY014) GROUP(TEST)
    PROGRAM ==> DFH014
    PROFILE ==> DFHCICST
    ```

    画面・出力には CEDA が含まれ、CEDAを確認し、TCP/IPサービス状態の見落としを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEDA DEFINE PROGRAM(DFH014) GROUP(TEST)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CEDA DEF PROGRAM(DFH014) GROUP(TEST)
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
    TRANSACTION PAY014 INSTALLED
    PROGRAM DFH014 INSTALLED
    ```

    画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
    ② ステップ2 の CEDA が画面・出力に表示されること
    ③ ステップ3 の INSTALL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### DFHTU trace utility 状態確認 出力見出し {#c04-i0210}
*分類: メイン端末運用*  ・  難易度: 中級

CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「DFHTU trace utility 状態確認 出力見出し」は、補助トレースデータを整形して問題判別に使うCICSトレースユーティリティを状態確認の観点で確認する技術項目です。URIMAP 行とAEI8を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? note "検証手順（1件）"
    **DFHTU trace utility 状態確認 出力見出し**

    - 検証目的: メイン端末運用におけるDFHTU trace utilityの状態確認を机上確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=AEI8
    - セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> PUT CICS bridge message for CEMT INQUIRE TASK
    → Enter を押す
    ```

    画面・出力:
    ```text
    CICS-MQ BRIDGE REQUEST ACCEPTED
    TRANSACTION CEMT
    COMMAND CEMT INQUIRE TASK
    ```

    画面・出力には CICS-MQ が含まれ、CICS-MQを確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TASK TRAN(CWXN)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tas(0051988) Tra(CWXN) Sus Tas Pri(001) Sta(U) Use(WEBSRV)
    Uow(C9D5F2EE2DEE8499) Hty(SOCKET) Hva(RECEIVE) Hti(200841) Bac Wai
    ```

    画面・出力には CWXN が含まれ、CWXNを読み、出典資料の出力項目と運用記録を対応させる。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
    操作（入力）:
    ```text
    CICS操作画面
    COMMAND ===> CEMT INQUIRE TRANSACTION(CWXN)
    → Enter を押す
    ```

    画面・出力:
    ```text
    Tra(CWXN) Pri(001) Pro(DFHWBXN) Ena Sta Profile(DFHCICST)
    ```

    画面・出力には CWXN が含まれ、CWXNを残し、同じ手順を再実行したときの照合点にする。

    - 合格条件: ① ステップ1 の CICS-MQ が画面・出力に表示されること
    ② ステップ2 の CWXN が画面・出力に表示されること
    ③ ステップ3 の CWXN が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



### メイン端末運用 CEMTシステム照会 ログとの照合 CIC07 {#c04-i0211}
*分類: メイン端末運用*  ・  難易度: 初級

ログとの照合では メイン端末運用 の システム照会 を主操作として CIC07 を判定します。時刻と対象識別子への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC07 に残します。ログとの照合を補助する 領域識別 では Applid を補助値として CIC07 へ保存します。主判定のログとの照合ではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC07 へ残します。証跡照合のログとの照合ではメイン端末運用・システム照会の STATUS と Applid を CIC07 に保存します。記録対応のログとの照合ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC07 を結びます。

**出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf

??? question "確認問題（1問）"
    **問題.** ログとの照合で メイン端末運用 の システム照会 と 領域識別 を組み合わせる際は CEMTシステム照会 がCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能という仕組みを前提にします。別領域のCEMT画面で変更を実行する危険があります。STATUS と APPLIDと領域状態 を対象 CIC07 で確認する組合せはどれですか。

    - A. CEMT INQUIRE SYSTEMが応答を返した時点で正常とする。応答中のSTATUSの値は記録しない。DFHST0103IをSTATUSと同じ判定値とみなし対象CIC07の主証跡にする。
    - B. CEMT INQUIRE SYSTEMのコマンド文字列だけを記録する。STATUSを含む応答行は保存しない。
    - C. STATUSを含むシステム照会の応答行を保存する。その応答を得るためCEMT INQUIRE SYSTEMを使用する。対象CIC07のAPPLIDと領域状態として記録する。 ✅
    - D. CEMTシステム照会の停止または再定義を実施する。その後にCEMT INQUIRE SYSTEMでSTATUSを採取する。

    正解: **C** ／ 難易度: 初級

    **解説:** 適切な判定: Cはシステム照会で STATUS を読みAPPLIDと領域状態の主値として操作とログを対応しCIC07に残します。
    機能の仕組み: ログとの照合では領域識別を補助操作としCEMTシステム照会の時刻と対象識別子をApplidと対象CIC07で照合します。
    各候補の評価: システム照会と領域識別の役割を分けるとA: 応答の有無だけではAPPLIDと領域状態を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではAPPLIDと領域状態を証明できない点で一次資料と一致しません、C: STATUSの実値を対象別に残す点でCIC07を判定できます、D: 変更前のAPPLIDと領域状態を失う点で領域識別の範囲を越えます。結論としてログとの照合のメイン端末運用・システム照会で判定する対象は CIC07 です。
    用語の定義: ログとの照合で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC07へ適用します。

    **出典:** transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf


??? note "検証手順（1件）"
    **メイン端末運用 CEMTシステム照会 ログとの照合 CIC07**

    - 検証目的: メイン端末運用のCEMTシステム照会について操作とログを対応し、CIC07のAPPLIDと領域状態を実出力で確認する。
    - 前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC07のシステム照会を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATUS: RESULTS - OVERTYPE TO MODIFY
    Sysid(CIC07) Applid(CIC07) Aging(1000) Maxtasks(120)
    ```

    画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC07の領域識別を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT INQUIRE SYSTEM APPLID
    → Enter を押す
    ```

    画面・出力:
    ```text
    Applid(CIC07) Cicstslevel(060200) Sysid(CIC07)
    ```

    画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC07の統計記録を表示します。
    操作（入力）:
    ```text
    CICS Transaction Server for z/OS 6.x 操作画面
    COMMAND ===> CEMT PERFORM STATISTICS RECORD ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFHST0103I CIC07 STATISTICS RECORDING REQUEST COMPLETED
    ```

    画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
    ② ステップ2 の Applid が画面・出力に表示されること
    ③ ステップ3 の DFHST0103I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf



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


