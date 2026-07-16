---
search:
  exclude: true
---

# PSF for z/OS 4.7 — 詳細 (4/4)

[← PSF for z/OS 4.7 の概要へ戻る](index.md)


## PSF for z/OS 4.7 > 出力経路確認

### 出力経路確認 JES to PSF Output Route 変更後の確認 ROUTE03 {#c24-i0184}
*分類: 出力経路確認*  ・  難易度: 上級

変更後の確認では 出力経路確認 の PSF処理 を主操作として ROUTE03 を判定します。反映値と残存値への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE03 に残します。変更後の確認を補助する JES出力 では DEST を補助値として ROUTE03 へ保存します。主判定の変更後の確認では出力経路確認の PSF処理 から APS450I を読み ROUTE03 へ残します。証跡照合の変更後の確認では出力経路確認の APS450I と DEST を ROUTE03 に保存します。記録対応の変更後の確認では出力経路確認の ClassとDestination の証跡へ ROUTE03 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 出力経路確認 の PSF処理 と JES出力 を用い 変更結果を検証 します。JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路です。SYSOUTクラスだけで実プリンター到達を判断する危険があります。APS450I で対象 ROUTE03 の ClassとDestination を再現できる記録はどれですか。

    - A. SDSF O JOB03で周辺状態を押さえる。その後にSDSF browse PSFPROC SYSLOG FIND JOB03でAPS450Iを確認して変更結果を検証する。 ✅
    - B. JES to PSF Output Routeの停止または再定義を実施する。その後にSDSF browse PSFPROC SYSLOG FIND JOB03でAPS450Iを採取する。
    - C. データストリームのData StreamとPrinter Typeを確認する。その値を出力経路確認のROUTE03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. SDSF O JOB03が成功したためSDSF browse PSFPROC SYSLOG FIND JOB03のAPS450Iも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正答の根拠: AはPSF処理で APS450I を読みClassとDestinationの主値として変更結果を検証しROUTE03に残します。
    内部の仕組み: 変更後の確認ではJES出力を補助操作としJES to PSF Output Routeの反映値と残存値をDESTと対象ROUTE03で照合します。
    誤答を含む比較: PSF処理とJES出力の役割を分けるとA: 周辺状態の後にAPS450Iを確認する点でROUTE03を判定できます、B: 変更前のClassとDestinationを失う点でJES出力の範囲を越えます、C: データストリームの値ではAPS450Iを確認できないうえに追加前提も不正な点でROUTE03の値を示しません、D: 補助操作の成功ではAPS450Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の出力経路確認で判定する対象は ROUTE03 です。
    用語定義: 変更後の確認で使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE03へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 変更後の確認 ROUTE03**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて変更結果を検証し、ROUTE03のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB03を指定し、ROUTE03のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB03 DATA SET SYSOUT SELECTED BY FSA PRT03
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB03を指定し、ROUTE03のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB03 DDNAME SYSOUT CLASS A DEST PRT03 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT03を指定し、ROUTE03のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT03
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT03 UNIT=PRT03 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APS450I が画面・出力に表示されること
    ② ステップ2 の DEST が画面・出力に表示されること
    ③ ステップ3 の CLASS=A が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 出力経路確認 JES to PSF Output Route 引継ぎ記録 ROUTE09 {#c24-i0185}
*分類: 出力経路確認*  ・  難易度: 上級

引継ぎ記録では 出力経路確認 の PSF処理 を主操作として ROUTE09 を判定します。次担当者が追跡できる証跡への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE09 に残します。引継ぎ記録を補助する JES出力 では DEST を補助値として ROUTE09 へ保存します。主判定の引継ぎ記録では出力経路確認の PSF処理 から APS450I を読み ROUTE09 へ残します。証跡照合の引継ぎ記録では出力経路確認の APS450I と DEST を ROUTE09 に保存します。記録対応の引継ぎ記録では出力経路確認の ClassとDestination の証跡へ ROUTE09 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 出力経路確認 の PSF処理 と JES出力 を用い 再現可能な記録を作成 します。JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路です。SYSOUTクラスだけで実プリンター到達を判断する危険があります。APS450I で対象 ROUTE09 の ClassとDestination を再現できる記録はどれですか。

    - A. SDSF O JOB09が成功したためSDSF browse PSFPROC SYSLOG FIND JOB09のAPS450Iも正常だと推定する。主出力は保存しない。
    - B. SDSF browse PSFPROC SYSLOG FIND JOB09を対象名なしで実行する。一覧の先頭行をROUTE09の結果として記録する。
    - C. 対象名ROUTE09を指定してSDSF browse PSFPROC SYSLOG FIND JOB09を実行する。応答中のAPS450Iと時刻を保存する。SDSF O JOB09で周辺状態を補完する。 ✅
    - D. 前回保存したSDSF browse PSFPROC SYSLOG FIND JOB09の結果を使う。今回のSDSF O JOB09の結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 上級

    **解説:** 採用操作の理由: CはPSF処理で APS450I を読みClassとDestinationの主値として再現可能な記録を作成しROUTE09に残します。
    製品内の仕組み: 引継ぎ記録ではJES出力を補助操作としJES to PSF Output Routeの次担当者が追跡できる証跡をDESTと対象ROUTE09で照合します。
    選択肢別の説明: PSF処理とJES出力の役割を分けるとA: 補助操作の成功ではAPS450Iを確定できない点でROUTE09の値を示しません、B: 先頭行はROUTE09と確定できない点で引継ぎ記録に合いません、C: APS450Iと時刻を保存する点でPSF処理に合います、D: 採取時刻が異なる点で出力経路確認に使いません。結論として引継ぎ記録の出力経路確認で判定する対象は ROUTE09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE09へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 引継ぎ記録 ROUTE09**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて再現可能な記録を作成し、ROUTE09のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB09を指定し、ROUTE09のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB09 DATA SET SYSOUT SELECTED BY FSA PRT09
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB09を指定し、ROUTE09のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB09 DDNAME SYSOUT CLASS A DEST PRT09 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT09を指定し、ROUTE09のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT09
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT09 UNIT=PRT09 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APS450I が画面・出力に表示されること
    ② ステップ2 の DEST が画面・出力に表示されること
    ③ ステップ3 の CLASS=A が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 出力経路確認 JES to PSF Output Route 復旧後の確認 ROUTE06 {#c24-i0186}
*分類: 出力経路確認*  ・  難易度: 上級

復旧後の確認では 出力経路確認 の PSF処理 を主操作として ROUTE06 を判定します。再発していないことを示す値への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE06 に残します。復旧後の確認を補助する JES出力 では DEST を補助値として ROUTE06 へ保存します。主判定の復旧後の確認では出力経路確認の PSF処理 から APS450I を読み ROUTE06 へ残します。証跡照合の復旧後の確認では出力経路確認の APS450I と DEST を ROUTE06 に保存します。記録対応の復旧後の確認では出力経路確認の ClassとDestination の証跡へ ROUTE06 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 出力経路確認 の PSF処理 と JES出力 の役割を分け 再発していないことを示す値 を調べます。JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路です。SYSOUTクラスだけで実プリンター到達を判断する危険があります。対象 ROUTE06 を誤判定しない進め方はどれですか。

    - A. 診断・トレースのTrace ModeとTrace Datasetを確認する。その値を出力経路確認のROUTE06にも適用する。
    - B. SDSF O JOB06が成功したためSDSF browse PSFPROC SYSLOG FIND JOB06のAPS450Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象ROUTE06へ引き継げるものとする。
    - C. SDSF browse PSFPROC SYSLOG FIND JOB06を対象名なしで実行する。一覧の先頭行をROUTE06の結果として記録する。
    - D. SDSF browse PSFPROC SYSLOG FIND JOB06でAPS450Iを取得してから$D PRT06でCLASS=Aを照合する。ROUTE06のClassとDestinationを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正答内容: DはPSF処理で APS450I を読みClassとDestinationの主値として復旧後の安定性を確認しROUTE06に残します。
    構成上の背景: 復旧後の確認ではJES出力を補助操作としJES to PSF Output Routeの再発していないことを示す値をDESTと対象ROUTE06で照合します。
    候補ごとの理由: PSF処理とJES出力の役割を分けるとA: 診断・トレースの値ではAPS450Iを確認できない点でJES出力の範囲を越えます、B: 補助操作の成功ではAPS450Iを確定できないうえに追加前提も不正な点でROUTE06の値を示しません、C: 先頭行はROUTE06と確定できない点で復旧後の確認に合いません、D: APS450IとCLASS=Aを順に照合する点でPSF処理に合います。結論として復旧後の確認の出力経路確認で判定する対象は ROUTE06 です。
    初出用語: 復旧後の確認で使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE06へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 復旧後の確認 ROUTE06**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて復旧後の安定性を確認し、ROUTE06のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB06を指定し、ROUTE06のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB06 DATA SET SYSOUT SELECTED BY FSA PRT06
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB06を指定し、ROUTE06のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB06 DDNAME SYSOUT CLASS A DEST PRT06 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT06を指定し、ROUTE06のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT06
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT06 UNIT=PRT06 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の APS450I が画面・出力に表示されること
    ② ステップ2 の DEST が画面・出力に表示されること
    ③ ステップ3 の CLASS=A が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 出力経路確認 JES to PSF Output Route 復旧準備 ROUTE05 {#c24-i0187}
*分類: 出力経路確認*  ・  難易度: 上級

復旧準備では 出力経路確認 の プリンター経路 を主操作として ROUTE05 を判定します。再開前に必要な整合性への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE05 に残します。復旧準備を補助する PSF処理 では APS450I を補助値として ROUTE05 へ保存します。主判定の復旧準備では出力経路確認の プリンター経路 から CLASS=A を読み ROUTE05 へ残します。証跡照合の復旧準備では出力経路確認の CLASS=A と APS450I を ROUTE05 に保存します。記録対応の復旧準備では出力経路確認の ClassとDestination の証跡へ ROUTE05 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 復旧準備で 出力経路確認 の プリンター経路 と PSF処理 を組み合わせる際は JES to PSF Output Route がSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路という仕組みを前提にします。SYSOUTクラスだけで実プリンター到達を判断する危険があります。CLASS=A と ClassとDestination を対象 ROUTE05 で確認する組合せはどれですか。

    - A. 前回保存した$D PRT05の結果を使う。今回のSDSF browse PSFPROC SYSLOG FIND JOB05の結果と同一時点の証跡として比較する。
    - B. 保存済みのROUTE05の出力を再利用する。今回の$D PRT05とSDSF browse PSFPROC SYSLOG FIND JOB05は実行済みとして扱う。
    - C. 変更を加えず$D PRT05を実行する。CLASS=Aを保存する。差分はSDSF browse PSFPROC SYSLOG FIND JOB05の結果と対象名で対応させる。 ✅
    - D. SDSF browse PSFPROC SYSLOG FIND JOB05のAPS450IをClassとDestinationの主判定に採用する。$D PRT05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: Cはプリンター経路で CLASS=A を読みClassとDestinationの主値として復旧条件を確認しROUTE05に残します。
    処理の仕組み: 復旧準備ではPSF処理を補助操作としJES to PSF Output Routeの再開前に必要な整合性をAPS450Iと対象ROUTE05で照合します。
    選択結果の内訳: プリンター経路とPSF処理の役割を分けるとA: 採取時刻が異なる点でプリンター経路を代替しません、B: 過去出力では今回の復旧準備を示せない点で出力経路確認に使いません、C: 変更前のCLASS=Aを保存する点で正答です、D: APS450IはCLASS=Aを代替しないうえに追加前提も不正な点でROUTE05を採用できません。結論として復旧準備の出力経路確認で判定する対象は ROUTE05 です。
    用語の説明: 復旧準備で使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE05へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 復旧準備 ROUTE05**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて復旧条件を確認し、ROUTE05のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT05を指定し、ROUTE05のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT05
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT05 UNIT=PRT05 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB05を指定し、ROUTE05のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB05 DATA SET SYSOUT SELECTED BY FSA PRT05
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB05を指定し、ROUTE05のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB05 DDNAME SYSOUT CLASS A DEST PRT05 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CLASS=A が画面・出力に表示されること
    ② ステップ2 の APS450I が画面・出力に表示されること
    ③ ステップ3 の DEST が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 出力経路確認 JES to PSF Output Route 構成監査 ROUTE08 {#c24-i0188}
*分類: 出力経路確認*  ・  難易度: 上級

構成監査では 出力経路確認 の プリンター経路 を主操作として ROUTE08 を判定します。定義値と稼働値の一致への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE08 に残します。構成監査を補助する PSF処理 では APS450I を補助値として ROUTE08 へ保存します。主判定の構成監査では出力経路確認の プリンター経路 から CLASS=A を読み ROUTE08 へ残します。証跡照合の構成監査では出力経路確認の CLASS=A と APS450I を ROUTE08 に保存します。記録対応の構成監査では出力経路確認の ClassとDestination の証跡へ ROUTE08 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 構成監査で 出力経路確認 の プリンター経路 と PSF処理 を実施し JES to PSF Output Route の役割を確認します。SYSOUTクラスだけで実プリンター到達を判断する危険があります。対象 ROUTE08 の証跡を取る方法はどれですか。

    - A. 保存済みのROUTE08の出力を再利用する。今回の$D PRT08とSDSF browse PSFPROC SYSLOG FIND JOB08は実行済みとして扱う。
    - B. SDSF browse PSFPROC SYSLOG FIND JOB08の結果だけでは確定しない。$D PRT08のCLASS=Aを主証跡として構成差分を監査する。 ✅
    - C. SDSF browse PSFPROC SYSLOG FIND JOB08のAPS450IをClassとDestinationの主判定に採用する。$D PRT08の応答は採取対象から外す。
    - D. SDSF O JOB08のDESTをCLASS=Aと同義の成功表示として扱う。$D PRT08は実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: Bはプリンター経路で CLASS=A を読みClassとDestinationの主値として構成差分を監査しROUTE08に残します。
    実行時の背景: 構成監査ではPSF処理を補助操作としJES to PSF Output Routeの定義値と稼働値の一致をAPS450Iと対象ROUTE08で照合します。
    四つの候補の理由: プリンター経路とPSF処理の役割を分けるとA: 過去出力では今回の構成監査を示せない点で出力経路確認に使いません、B: CLASS=Aを主証跡として区別する点で正答です、C: APS450IはCLASS=Aを代替しない点でROUTE08を採用できません、D: DESTとCLASS=Aは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の出力経路確認で判定する対象は ROUTE08 です。
    初出語定義: 構成監査で使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE08へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 構成監査 ROUTE08**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて構成差分を監査し、ROUTE08のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT08を指定し、ROUTE08のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT08
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT08 UNIT=PRT08 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB08を指定し、ROUTE08のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB08 DATA SET SYSOUT SELECTED BY FSA PRT08
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB08を指定し、ROUTE08のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB08 DDNAME SYSOUT CLASS A DEST PRT08 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CLASS=A が画面・出力に表示されること
    ② ステップ2 の APS450I が画面・出力に表示されること
    ③ ステップ3 の DEST が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 出力経路確認 JES to PSF Output Route 通常状態の確認 ROUTE01 {#c24-i0189}
*分類: 出力経路確認*  ・  難易度: 上級

通常状態の確認では 出力経路確認 の JES出力 を主操作として ROUTE01 を判定します。基準値と現在値の差への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE01 に残します。通常状態の確認を補助する プリンター経路 では CLASS=A を補助値として ROUTE01 へ保存します。主判定の通常状態の確認では出力経路確認の JES出力 から DEST を読み ROUTE01 へ残します。証跡照合の通常状態の確認では出力経路確認の DEST と CLASS=A を ROUTE01 に保存します。記録対応の通常状態の確認では出力経路確認の ClassとDestination の証跡へ ROUTE01 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 出力経路確認 の JES出力 と プリンター経路 を使い 通常状態を確定 します。JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路です。SYSOUTクラスだけで実プリンター到達を判断する危険があります。DEST を読み対象 ROUTE01 を切り分ける確認方法はどれですか。

    - A. $D PRT01のCLASS=AをClassとDestinationの主判定に採用する。SDSF O JOB01の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. SDSF browse PSFPROC SYSLOG FIND JOB01のAPS450IをDESTと同義の成功表示として扱う。SDSF O JOB01は実行しない。
    - C. SDSF O JOB01を先に実行する。対象ROUTE01のDESTをClassとDestinationとして記録する。続いて$D PRT01で同一対象を照合する。 ✅
    - D. SDSF O JOB01が応答を返した時点で正常とする。応答中のDESTの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: CはJES出力で DEST を読みClassとDestinationの主値として通常状態を確定しROUTE01に残します。
    背景・仕組み: 通常状態の確認ではプリンター経路を補助操作としJES to PSF Output Routeの基準値と現在値の差をCLASS=Aと対象ROUTE01で照合します。
    選択肢の理由: JES出力とプリンター経路の役割を分けるとA: CLASS=AはDESTを代替しないうえに追加前提も不正な点でJES to PSF Output Routeに使えません、B: APS450IとDESTは確認項目が異なる点でROUTE01を採用できません、C: DESTを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではClassとDestinationを判定できない点で一次資料と一致しません。結論として通常状態の確認の出力経路確認で判定する対象は ROUTE01 です。
    用語の初出定義: 通常状態の確認で使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE01へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 通常状態の確認 ROUTE01**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて通常状態を確定し、ROUTE01のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB01を指定し、ROUTE01のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB01 DDNAME SYSOUT CLASS A DEST PRT01 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT01を指定し、ROUTE01のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT01
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT01 UNIT=PRT01 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB01を指定し、ROUTE01のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB01 DATA SET SYSOUT SELECTED BY FSA PRT01
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DEST が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の APS450I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 出力経路確認 JES to PSF Output Route 障害切り分け ROUTE04 {#c24-i0190}
*分類: 出力経路確認*  ・  難易度: 上級

障害切り分けでは 出力経路確認 の JES出力 を主操作として ROUTE04 を判定します。最初に失敗した処理への注意として「SYSOUTクラスだけで実プリンター到達を判断する危険があります」を ROUTE04 に残します。障害切り分けを補助する プリンター経路 では CLASS=A を補助値として ROUTE04 へ保存します。主判定の障害切り分けでは出力経路確認の JES出力 から DEST を読み ROUTE04 へ残します。証跡照合の障害切り分けでは出力経路確認の DEST と CLASS=A を ROUTE04 に保存します。記録対応の障害切り分けでは出力経路確認の ClassとDestination の証跡へ ROUTE04 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 出力経路確認 の JES出力 と プリンター経路 を照合し 最初に失敗した処理 を確かめます。JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路です。SYSOUTクラスだけで実プリンター到達を判断する危険があります。DEST を読む前に対象 ROUTE04 へ行う確認はどれですか。

    - A. SDSF browse PSFPROC SYSLOG FIND JOB04のAPS450IをDESTと同義の成功表示として扱う。SDSF O JOB04は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. SDSF O JOB04の出力でROUTE04とDESTが同じ応答にあることを確認する。ClassとDestinationをその応答から採取する。 ✅
    - C. SDSF O JOB04が応答を返した時点で正常とする。応答中のDESTの値は記録しない。
    - D. SDSF O JOB04のコマンド文字列だけを記録する。DESTを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: BはJES出力で DEST を読みClassとDestinationの主値として障害範囲を限定しROUTE04に残します。
    技術的背景: 障害切り分けではプリンター経路を補助操作としJES to PSF Output Routeの最初に失敗した処理をCLASS=Aと対象ROUTE04で照合します。
    四択の評価: JES出力とプリンター経路の役割を分けるとA: APS450IとDESTは確認項目が異なるうえに追加前提も不正な点でROUTE04を採用できません、B: ROUTE04とDESTを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではClassとDestinationを判定できない点で一次資料と一致しません、D: 入力記録だけではClassとDestinationを証明できない点でClassとDestinationを確認できません。結論として障害切り分けの出力経路確認で判定する対象は ROUTE04 です。
    初出語の意味: 障害切り分けで使う JES to PSF Output Route はSYSOUTクラス、OUTPUT文、FSS、FSA、プリンターを順に対応させて出力データセットを配送する経路を表しClassとDestinationを判定する際にROUTE04へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **出力経路確認 JES to PSF Output Route 障害切り分け ROUTE04**

    - 検証目的: 出力経路確認のJES to PSF Output Routeについて障害範囲を限定し、ROUTE04のClassとDestinationを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象ROUTE04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF O JOB04を指定し、ROUTE04のJES出力を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF O JOB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    JOBNAME JOB04 DDNAME SYSOUT CLASS A DEST PRT04 FORMS STD
    ```

    画面・出力にあるDESTを読み、ClassとDestinationと対象ROUTE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へ$D PRT04を指定し、ROUTE04のプリンター経路を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D PRT04
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT04 UNIT=PRT04 STATUS=IDLE FSS=PSF1 CLASS=A
    ```

    画面・出力にあるCLASS=Aを読み、ClassとDestinationと対象ROUTE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の出力経路確認を確認する入力画面です。COMMAND入力口へSDSF browse PSFPROC SYSLOG FIND JOB04を指定し、ROUTE04のPSF処理を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> SDSF browse PSFPROC SYSLOG FIND JOB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS450I JOB04 DATA SET SYSOUT SELECTED BY FSA PRT04
    ```

    画面・出力にあるAPS450Iを読み、ClassとDestinationと対象ROUTE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DEST が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の APS450I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 複数APSメッセージ照合 起動確認 診断060 {#c24-i0191}
*分類: 出力経路確認*  ・  難易度: 中級

第六十観点 出力経路確認 の運用票では 複数APSメッセージ照合 を単独名ではなく関連値と合わせます。第六十観点 切分けでは 一つの障害で複数の APS メッセージが出る場合に、全体を合わせて原因を確定する調査観点という役割を崩さず扱います。第六十観点 PSFPROC12 とPSF手順の値を比較し、JES定義とPSF手順の混同防止を再表示できる形にします。第六十観点 確認経路は JES、PSF開始手順、Printer Inventory、SDSFログ、AFPリソースの別を PSF記録080に残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **複数APSメッセージ照合 起動確認 診断060**

    - 検証目的: 出力経路確認における 複数APSメッセージ照合 の起動確認を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=PSFPROC12
    - セッション環境: AFP Download Plus / Printer Inventory / output log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信先定義確認により 複数APSメッセージ照合 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY AFP DOWNLOAD PRT080
    → Enter を押す
    ```

    画面・出力:
    ```text
    AFP DOWNLOAD PLUS DESTINATION FOR PRT080
    PRINTER PRT080 USES FORMDEF F1PSF080
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、トレースデータセット未準備を印刷装置の停止として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。リソース同梱確認により 複数APSメッセージ照合 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? JOB080
    → Enter を押す
    ```

    画面・出力:
    ```text
    OUTPUT GROUP JOB080
    MO:DCA-P DATA WITH INLINE RESOURCE O1PSF080 AND S1PSF080
    ```

    画面・出力には MO:DCA-P が含まれる。MO:DCA-P を読み取り、トレースデータセット未準備を印刷装置の停止として扱うことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信ログ確認により 複数APSメッセージ照合 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1059I AFP DOWNLOAD PLUS PROCESSING COMPLETED FOR PRT080
    DESTINATION RECORD RETAINED IN PSF LOG
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、トレースデータセット未準備を印刷装置の停止として扱うことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: AFP DOWNLOAD PLUS が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: MO:DCA-P が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: AFP DOWNLOAD PLUS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7




## PSF for z/OS 4.7 > 印刷アドレス空間

### FSA {#c24-i0192}
*分類: 印刷アドレス空間*  ・  難易度: 中級

PSF for z/OS 4.7 の 印刷アドレス空間で扱うFSAは、個々のプリンターや出力装置を扱う PSF の機能サブシステムアプリケーションです。印刷キュー、プリンター定義、接続状態と結び付きます。印刷停止時は対象 FSA の状態とメッセージを確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 探索確認の印刷アドレス空間で FSA の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. FSA の出力を取らず探索確認の印刷アドレス空間の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 ✅
    - C. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を省略して探索確認の印刷アドレス空間の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の印刷アドレス空間へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では FSA は「探索確認の印刷アドレス空間に関係する定義値と表示行を照合する探索確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では FSA の属性行と APS933I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では FSA を PSF for z/OS 4.7の運用手順で確認し、初出名は探索確認初出です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **FSA**

    - 検証目的: 探索確認の印刷アドレス空間について、PSF for z/OS 4.7 の 印刷アドレス空間で扱う FSA は、個々のプリンターや出力装置を扱う PSF の機能サブシステムアプリケーションです。印刷キュー、プリンタに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、探索確認の印刷アドレス空間の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にFSAを指定し、OSKB010006の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND FSA
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM FSA
    CASE OSKB010006
    SOURCE PSF for z/OS
    ```

    FSAとOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010006を同じ出力で読み、探索確認の印刷アドレス空間の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010006
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010006
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の FSA と OSKB010006 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes



### FSS {#c24-i0193}
*分類: 印刷アドレス空間*  ・  難易度: 中級

PSF for z/OS 4.7 の 印刷アドレス空間で扱うFSSは、JES から見た機能サブシステムとして PSF 印刷処理を支える単位です。複数の FSA を配下に持ち、印刷処理の実行環境を構成します。起動 JCL や Printer Inventory の定義と対応させて確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 終端確認の印刷アドレス空間に関係する FSS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 ✅
    - B. FSS の名称と担当者名のみを残して終端確認の印刷アドレス空間の表示本文を確認対象に含めない。
    - C. 印刷サービス以外の画面で終端確認の印刷アドレス空間を確認し同じ証跡として扱ったことにする。
    - D. APS933I の有無を見ず終端確認の印刷アドレス空間の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では FSS は「FSS の用途を印刷サービスの表示で確認する終端確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では PSF for z/OS の FSS と APS933I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では FSS を PSF for z/OS 4.7で扱う確認対象とし、用語名は終端確認用語です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **FSS**

    - 検証目的: 終端確認の印刷アドレス空間について、PSF for z/OS 4.7 の 印刷アドレス空間で扱う FSS は、JES から見た機能サブシステムとして PSF 印刷処理を支える単位です。複数の FSA を配下に持ちに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、終端確認の印刷アドレス空間の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にFSSを指定し、OSKB010005の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND FSS
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM FSS
    CASE OSKB010005
    SOURCE PSF for z/OS
    ```

    FSSとOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010005を同じ出力で読み、終端確認の印刷アドレス空間の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010005
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010005
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の FSS と OSKB010005 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes




## PSF for z/OS 4.7 > 基本概念

### AFP {#c24-i0194}
*分類: 基本概念*  ・  難易度: 初級

PSF for z/OS 4.7 の 基本概念で扱うAFPは、帳票やページを構成するための IBM の印刷アーキテクチャです。フォーム、フォント、ページ定義などのリソースと印刷データを組み合わせて高機能な印刷を実現します。PSF の問題では AFP データとリソースの対応を確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 展開確認の基本概念で AFP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AFP の出力を取らず展開確認の基本概念の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 ✅
    - C. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を省略して展開確認の基本概念の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の基本概念へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 初級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では AFP は「展開確認の基本概念に関係する定義値と表示行を照合する展開確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では AFP の属性行と APS933I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では AFP を PSF for z/OS 4.7の運用手順で確認し、初出名は展開確認初出です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **AFP**

    - 検証目的: 展開確認の基本概念について、PSF for z/OS 4.7 の 基本概念で扱う AFP は、帳票やページを構成するための IBM の印刷アーキテクチャです。フォーム、フォント、ページ定義などのリソースとに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、展開確認の基本概念の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にAFPを指定し、OSKB010002の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND AFP
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM AFP
    CASE OSKB010002
    SOURCE PSF for z/OS
    ```

    AFPとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010002を同じ出力で読み、展開確認の基本概念の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010002
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010002
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の AFP と OSKB010002 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes



### IPDS {#c24-i0195}
*分類: 基本概念*  ・  難易度: 中級

PSF for z/OS 4.7 の 基本概念で扱うIPDSは、プリンターへ送信される双方向の印刷データストリームです。PSF は AFP データを処理し、プリンターが解釈できる IPDS として送ります。印刷障害では IPDS 対応プリンターか、接続経路が正しいかを確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 呼出確認の基本概念で印刷サービスの運用確認を行います。IPDS の根拠にできる作業はどれですか。

    - A. PSF for z/OS と無関係な一覧で呼出確認の基本概念を確認した扱いにする。
    - B. APS933I の有無を確認せず呼出確認の基本概念を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. IPDS の属性行を読まず呼出確認の基本概念の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では IPDS は「PSF for z/OS で IPDS の扱いを記録する呼出確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では IPDS の表示結果と APS933I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では IPDS の使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **IPDS**

    - 検証目的: 呼出確認の基本概念について、PSF for z/OS 4.7 の 基本概念で扱う IPDS は、プリンターへ送信される双方向の印刷データストリームです。PSF は AFP データを処理し、プリンターが解釈に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、呼出確認の基本概念の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にIPDSを指定し、OSKB010003の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND IPDS
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM IPDS
    CASE OSKB010003
    SOURCE PSF for z/OS
    ```

    IPDSとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010003を同じ出力で読み、呼出確認の基本概念の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010003
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010003
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の IPDS と OSKB010003 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes



### PSF for z/OS {#c24-i0196}
*分類: 基本概念*  ・  難易度: 初級

PSF for z/OS 4.7 の 基本概念で扱うPSF for z/OSは、JES スプール上の印刷データを AFP プリンターへ送る z/OS のプリンタードライバー製品です。印刷データと必要なリソースを組み合わせ、IPDS としてプリンターへ送信します。障害時は JES、PSF、プリンターのどこで止まっているかを分けて確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 構文確認のPSF for z/OSに関係する PSF for z・ OS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO の結果から対象行を抜き出し、構文確認の証跡として残す。 ✅
    - B. PSF for z・ OS の名称と担当者名のみを残して構文確認のPSF for z/OSの表示本文を確認対象に含めない。
    - C. 印刷サービス以外の画面で構文確認のPSF for z/OSを確認し同じ証跡として扱ったことにする。
    - D. APS933I の有無を見ず構文確認のPSF for z/OSの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では PSF for z・ OS は「PSF for z・ OS の用途を印刷サービスの表示で確認する構文確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では PSF for z/OS の PSF for z・ OS と APS933I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では PSF for z・ OS を PSF for z/OS 4.7で扱う確認対象とし、用語名は構文確認用語です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **PSF for z・ OS**

    - 検証目的: 構文確認の・について、PSF for z/OS 4.7 の 基本概念で扱う PSF for z/OS は、JES スプール上の印刷データを AFP プリンターへ送る z/OS のプリンタードライバーに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、構文確認の・の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPSF for z・ OSを指定し、OSKB010001の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PSF for z・ OS
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PSF for z・ OS
    CASE OSKB010001
    SOURCE PSF for z/OS
    ```

    PSF for z・ OSとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010001を同じ出力で読み、構文確認の・の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010001
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010001
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の PSF for z・ OS と OSKB010001 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes




## PSF for z/OS 4.7 > 変換

### ACIF {#c24-i0197}
*分類: 変換*  ・  難易度: 中級

PSF for z/OS 4.7 の 変換で扱うACIFは、印刷データを AFP へ変換したり、索引情報を作成したりする機能です。アーカイブや電子配布と組み合わせて使われることがあります。変換結果では入力データ、リソース、索引の対応を確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 記録確認の変換に関係する ACIF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO の結果から対象行を抜き出し、記録確認の証跡として残す。 ✅
    - B. ACIF の名称と担当者名のみを残して記録確認の変換の表示本文を確認対象に含めない。
    - C. 印刷サービス以外の画面で記録確認の変換を確認し同じ証跡として扱ったことにする。
    - D. APS933I の有無を見ず記録確認の変換の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では ACIF は「ACIF の用途を印刷サービスの表示で確認する記録確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では PSF for z/OS の ACIF と APS933I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では ACIF を PSF for z/OS 4.7で扱う確認対象とし、用語名は記録確認用語です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **ACIF**

    - 検証目的: 記録確認の変換について、PSF for z/OS 4.7 の 変換で扱う ACIF は、印刷データを AFP へ変換したり、索引情報を作成したりする機能です。アーカイブや電子配布と組み合わせて使われるに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、記録確認の変換の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にACIFを指定し、OSKB010013の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND ACIF
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM ACIF
    CASE OSKB010013
    SOURCE PSF for z/OS
    ```

    ACIFとOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010013を同じ出力で読み、記録確認の変換の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010013
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010013
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の ACIF と OSKB010013 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes




## PSF for z/OS 4.7 > 診断

### PSF トレース {#c24-i0198}
*分類: 診断*  ・  難易度: 上級

PSF for z/OS 4.7 の 診断で扱うPSF トレースは、印刷処理や通信の詳細を記録する診断機能です。通常運用では負荷や容量に注意し、問題再現時に範囲を絞って取得します。取得したトレースはメッセージ、FSA、プリンター状態と合わせて読みます

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 復旧確認のトレースで PSF トレースの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. PSF トレースの出力を取らず復旧確認のトレースの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 ✅
    - C. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を省略して復旧確認のトレースの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認のトレースへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では PSF トレース は「復旧確認のトレースに関係する定義値と表示行を照合する復旧確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では PSF トレースの属性行と APS933I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では PSF トレースを PSF for z/OS 4.7の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **PSF トレース**

    - 検証目的: 復旧確認のトレースについて、PSF for z/OS 4.7 の 診断で扱う PSF トレースは、印刷処理や通信の詳細を記録する診断機能です。通常運用では負荷や容量に注意し、問題再現時に範囲を絞って取得に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、復旧確認のトレースの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPSF トレースを指定し、OSKB010018の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PSF トレース
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PSF トレース
    CASE OSKB010018
    SOURCE PSF for z/OS
    ```

    PSF トレースとOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010018を同じ出力で読み、復旧確認のトレースの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010018
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010018
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の PSF トレース と OSKB010018 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes



### PSF メッセージ {#c24-i0199}
*分類: 診断*  ・  難易度: 初級

PSF for z/OS 4.7 の 診断で扱うPSF メッセージは、印刷処理、リソース探索、FSS/FSA 起動、プリンター通信の状態を知らせる診断情報です。メッセージ ID と対象プリンター、ジョブ出力を対応させると原因を絞れます。対応時はシステムプログラマー向け応答も確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 警告確認のメッセージに関係する PSF メッセージの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 ✅
    - B. PSF メッセージの名称と担当者名のみを残して警告確認のメッセージの表示本文を確認対象に含めない。
    - C. 印刷サービス以外の画面で警告確認のメッセージを確認し同じ証跡として扱ったことにする。
    - D. APS933I の有無を見ず警告確認のメッセージの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では PSF メッセージ は「PSF メッセージの用途を印刷サービスの表示で確認する警告確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では PSF for z/OS の PSF メッセージと APS933I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では PSF メッセージを PSF for z/OS 4.7で扱う確認対象とし、用語名は警告確認用語です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **PSF メッセージ**

    - 検証目的: 警告確認のメッセージについて、PSF for z/OS 4.7 の 診断で扱う PSF メッセージは、印刷処理、リソース探索、FSS/FSA 起動、プリンター通信の状態を知らせる診断情報です。メッセージに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、警告確認のメッセージの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にPSF メッセージを指定し、OSKB010017の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND PSF メッセージ
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM PSF メッセージ
    CASE OSKB010017
    SOURCE PSF for z/OS
    ```

    PSF メッセージとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010017を同じ出力で読み、警告確認のメッセージの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010017
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010017
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の PSF メッセージ と OSKB010017 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes




## PSF for z/OS 4.7 > 診断・トレース

### AFPPARMS ページ提示確認 照合057 {#c24-i0200}
*分類: 診断・トレース*  ・  難易度: 中級

第五十七観点 診断・トレース で AFPPARMS は印刷処理の対象を特定するためのPSF側の確認項目です。第五十七観点 資料上の意味は PSF のプリンター関連パラメーターを与える制御情報で、Printer Inventorという範囲で読み取ります。第五十七観点 AFP Download Plus の宛先指定 と APS 行を同じ確認票に置き、APSメッセージ範囲の確認を説明可能にします。第五十七観点 後続確認では FSS、FSA、PRTnnnn、資源名の対応を PSF記録077から再現します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **AFPPARMS ページ提示確認 照合057**

    - 検証目的: 診断・トレースにおける AFPPARMS のページ提示確認を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=O1PSF077
    - セッション環境: ISPF browse / AFP resource library / SDSF

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。フォーム定義参照により AFPPARMS の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE PSF.USER.FDEFLIB(F1PSF077)
    → Enter を押す
    ```

    画面・出力:
    ```text
    FORMDEF F1PSF077
    COPYGROUP CG09 MEDIUM MAP AND DUPLEX SETTINGS LISTED
    ```

    画面・出力には FORMDEF が含まれる。FORMDEF を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。ページ定義参照により AFPPARMS の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE PSF.USER.PDEFLIB(P1PSF077)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PAGEDEF P1PSF077
    LINE DATA MAPPING USES FONT C0PSF09 AND PAGE FORMAT PF09
    ```

    画面・出力には PAGEDEF が含まれる。PAGEDEF を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。出力属性照合により AFPPARMS の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? PRT077
    → Enter を押す
    ```

    画面・出力:
    ```text
    JES OUTPUT FOR PRT077
    FORMDEF F1PSF077 PAGEDEF P1PSF077 CHARS C0PSF09
    ```

    画面・出力には CHARS が含まれる。CHARS を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: FORMDEF が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: PAGEDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: CHARS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### Download for z/OS リソース解決 照合081 {#c24-i0201}
*分類: 診断・トレース*  ・  難易度: 中級

第八十一観点 Download for z/OS は PSF for z/OS の 診断・トレース で確認する技術要素です。第八十一観点 リモート側処理へ出力を渡す連携機能で、データ変換、宛先、ログを照合する対象という前提をFSS/FSAの対応で点検します。第八十一観点 Printer Inventory の FSS/FSA パラメーター と APS 行を同じ確認票に置き、ログ時点差の確認を説明可能にします。第八十一観点 記録では JES定義、PRINTDEV、APSメッセージ、AFP資源のどこを見たかを PSF記録101へ書きます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **Download for z/OS リソース解決 照合081**

    - 検証目的: 診断・トレースにおける Download for z/OS のリソース解決を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=PRT101
    - セッション環境: SDSF / JES2 console / PSF log review

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。$D PRT 表示により Download for z/OS の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> /$D PRT101
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT101 DISPLAY
    PRINTER PRT101 ASSOCIATED WITH FSS PSF09 AND FSA FSA09
    ```

    画面・出力には $HASP603 が含まれる。$HASP603 を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。PSF手順参照により Download for z/OS の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PROCLIB(PSFPROC09)
    → Enter を押す
    ```

    画面・出力:
    ```text
    //PSFPROC09 PROC
    //PRT101 CNTL
    // PRINTDEV FONTLIB=PSF.FONTLIB,FORMDEF=F1PSF101,PAGEDEF=P1PSF101
    //PRT101 ENDCNTL
    ```

    画面・出力には PRINTDEV が含まれる。PRINTDEV を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。APSログ確認により Download for z/OS の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS000I SUBSYSTEM PSF09 ACTIVE
    APS1080I PRINTER PRT101 SELECTED BY PSF FSA FSA09
    ```

    画面・出力には APS000I が含まれる。APS000I を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: $HASP603 が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: PRINTDEV が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS000I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### Download for z/OS 起動確認 関連付け021 {#c24-i0202}
*分類: 診断・トレース*  ・  難易度: 中級

第二十一観点 Download for z/OS は PSF for z/OS の 診断・トレース で確認する技術要素です。第二十一観点 リモート側処理へ出力を渡す連携機能で、データ変換、宛先、ログを照合する対象という性質を開始手順で確認します。第二十一観点 Printer Inventory の FSS/FSA パラメーター と PRT041 を同じ証跡に残し、ログ時点差の確認を管理します。第二十一観点 記録では JES定義、PRINTDEV、APSメッセージ、AFP資源のどこを見たかを PSF記録041へ書きます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **Download for z/OS 起動確認 関連付け021**

    - 検証目的: 診断・トレースにおける Download for z/OS の起動確認を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=PRT041
    - セッション環境: SDSF / JES2 console / PSF log review

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。$D PRT 表示により Download for z/OS の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> /$D PRT041
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT041 DISPLAY
    PRINTER PRT041 ASSOCIATED WITH FSS PSF21 AND FSA FSA21
    ```

    画面・出力には $HASP603 が含まれる。$HASP603 を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。PSF手順参照により Download for z/OS の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PROCLIB(PSFPROC21)
    → Enter を押す
    ```

    画面・出力:
    ```text
    //PSFPROC21 PROC
    //PRT041 CNTL
    // PRINTDEV FONTLIB=PSF.FONTLIB,FORMDEF=F1PSF041,PAGEDEF=P1PSF041
    //PRT041 ENDCNTL
    ```

    画面・出力には PRINTDEV が含まれる。PRINTDEV を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。APSログ確認により Download for z/OS の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS000I SUBSYSTEM PSF21 ACTIVE
    APS1020I PRINTER PRT041 SELECTED BY PSF FSA FSA21
    ```

    画面・出力には APS000I が含まれる。APS000I を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: $HASP603 が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: PRINTDEV が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS000I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### JES2 FSSDEF 出力経路確認 照合033 {#c24-i0203}
*分類: 診断・トレース*  ・  難易度: 中級

第三十三観点 JES2 FSSDEF は 診断・トレース の定義、ログ、資源をつなぐ確認対象です。第三十三観点 PSF 開始手順を JES2 初期設定へ結び付け、機能サブシステム名とプロシージャ名を定という内容を手順値と照合します。第三十三観点 コード化フォントとコードページの組合せ と APS 行を同じ確認票に置き、JES定義とPSF手順の混同防止を説明可能にします。第三十三観点 調査票ではSDSFログ、ISPF参照、Printer Inventoryの入口を PSF記録053に区別して残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **JES2 FSSDEF 出力経路確認 照合033**

    - 検証目的: 診断・トレースにおける JES2 FSSDEF の出力経路確認を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=FSA09
    - セッション環境: Printer Inventory / PSF customization review / console

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。Printer Inventory 確認により JES2 FSSDEF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY PRINTER PRT053
    → Enter を押す
    ```

    画面・出力:
    ```text
    PRINTER PRT053
    FSS PSF09
    FSA FSA09
    TCP/IP ATTACHMENT PARAMETERS SHOWN
    ```

    画面・出力には PRINTER が含まれる。PRINTER を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSSDEF 照合により JES2 FSSDEF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(JES2PARM)
    Command ===> FIND PSF09
    → Enter を押す
    ```

    画面・出力:
    ```text
    FSSDEF PSF09,PROC=PSFPROC09
    PRT053 FSS=PSF09,MODE=FSS
    ```

    画面・出力には FSSDEF が含まれる。FSSDEF を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSAメッセージ確認により JES2 FSSDEF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> FIND FSA09
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1032I FSA09 INITIALIZATION MESSAGE FOR PRT053
    APS000I SUBSYSTEM PSF09 ACTIVE
    ```

    画面・出力には FSA09 が含まれる。FSA09 を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: PRINTER が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FSSDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: FSA09 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### JES2 FSSDEF 障害切り分け 関連付け093 {#c24-i0204}
*分類: 診断・トレース*  ・  難易度: 上級

第九十三観点 JES2 FSSDEF は 診断・トレース の定義、ログ、資源をつなぐ確認対象です。第九十三観点 PSF 開始手順を JES2 初期設定へ結び付け、機能サブシステム名とプロシージャ名を定という範囲をAFP資源名と合わせます。第九十三観点 コード化フォントとコードページの組合せ と FSA21 を同じ証跡に残し、JES定義とPSF手順の混同防止を管理します。第九十三観点 調査票ではSDSFログ、ISPF参照、Printer Inventoryの入口を PSF記録113に区別して残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **JES2 FSSDEF 障害切り分け 関連付け093**

    - 検証目的: 診断・トレースにおける JES2 FSSDEF の障害切り分けを机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=FSA21
    - セッション環境: Printer Inventory / PSF customization review / console

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。Printer Inventory 確認により JES2 FSSDEF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY PRINTER PRT113
    → Enter を押す
    ```

    画面・出力:
    ```text
    PRINTER PRT113
    FSS PSF21
    FSA FSA21
    TCP/IP ATTACHMENT PARAMETERS SHOWN
    ```

    画面・出力には PRINTER が含まれる。PRINTER を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSSDEF 照合により JES2 FSSDEF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(JES2PARM)
    Command ===> FIND PSF21
    → Enter を押す
    ```

    画面・出力:
    ```text
    FSSDEF PSF21,PROC=PSFPROC21
    PRT113 FSS=PSF21,MODE=FSS
    ```

    画面・出力には FSSDEF が含まれる。FSSDEF を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSAメッセージ確認により JES2 FSSDEF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> FIND FSA21
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1092I FSA21 INITIALIZATION MESSAGE FOR PRT113
    APS000I SUBSYSTEM PSF21 ACTIVE
    ```

    画面・出力には FSA21 が含まれる。FSA21 を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: PRINTER が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FSSDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: FSA21 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### MO:DCA-P フォント照合 照合009 {#c24-i0205}
*分類: 診断・トレース*  ・  難易度: 初級

第九観点 診断・トレース の中で MO:DCA-P はJES、PSF、AFP資源の対応を説明するための項目です。第九観点 ページ構成済みの文書データで、配置、提示、フォント参照などを構造化フィールドとして保持すという範囲をAFP資源名と合わせます。第九観点 JES2 FSSDEF と PRTnnnn 定義 と APS 行を同じ確認票に置き、トレース準備漏れの発見を説明可能にします。第九観点 証跡には APS メッセージの連続行 と資料名を併記し、PSF記録029として保存します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **MO:DCA-P フォント照合 照合009**

    - 検証目的: 診断・トレースにおける MO:DCA-P のフォント照合を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=APS1008I
    - セッション環境: PSF diagnosis / trace data set / SDSF log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース準備により MO:DCA-P の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF dataset list
    Command ===> DSLIST 'PSF.TRACE.029'
    → Enter を押す
    ```

    画面・出力:
    ```text
    DATA SET PSF.TRACE.029 CATALOGED
    TRACE TARGET FOR FSA09
    ```

    画面・出力には TRACE が含まれる。TRACE を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース開始指定により MO:DCA-P の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F PSF09,TRACE,FORMAT=PSF,COMP=MSGM
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1008I TRACE COMMAND ACCEPTED FOR PSF09
    FORMAT PSF COMPONENT MSGM
    ```

    画面・出力には FORMAT が含まれる。FORMAT を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。メッセージ連続確認により MO:DCA-P の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS1008I
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1008I TRACE RECORD WRITTEN FOR PRT029
    APS000I SUBSYSTEM PSF09 ACTIVE
    ```

    画面・出力には APS1008I が含まれる。APS1008I を読み取り、フォント置換をデータ不備ではなく通信障害として扱うことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: TRACE が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FORMAT が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS1008I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### MO:DCA-P 起動確認 関連付け069 {#c24-i0206}
*分類: 診断・トレース*  ・  難易度: 中級

第六十九観点 診断・トレース の中で MO:DCA-P はJES、PSF、AFP資源の対応を説明するための項目です。第六十九観点 対象は ページ構成済みの文書データで、配置、提示、フォント参照などを構造化フィールドとして保持すです。第六十九観点 JES2 FSSDEF と PRTnnnn 定義 と APS1068I を同じ証跡に残し、トレース準備漏れの発見を管理します。第六十九観点 証跡には APS メッセージの連続行 と資料名を併記し、PSF記録089として保存します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **MO:DCA-P 起動確認 関連付け069**

    - 検証目的: 診断・トレースにおける MO:DCA-P の起動確認を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=APS1068I
    - セッション環境: PSF diagnosis / trace data set / SDSF log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース準備により MO:DCA-P の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF dataset list
    Command ===> DSLIST 'PSF.TRACE.089'
    → Enter を押す
    ```

    画面・出力:
    ```text
    DATA SET PSF.TRACE.089 CATALOGED
    TRACE TARGET FOR FSA21
    ```

    画面・出力には TRACE が含まれる。TRACE を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース開始指定により MO:DCA-P の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F PSF21,TRACE,FORMAT=PSF,COMP=MSGM
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1068I TRACE COMMAND ACCEPTED FOR PSF21
    FORMAT PSF COMPONENT MSGM
    ```

    画面・出力には FORMAT が含まれる。FORMAT を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。メッセージ連続確認により MO:DCA-P の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS1068I
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1068I TRACE RECORD WRITTEN FOR PRT089
    APS000I SUBSYSTEM PSF21 ACTIVE
    ```

    画面・出力には APS1068I が含まれる。APS1068I を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: TRACE が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FORMAT が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS1068I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### オーバーレイ 障害切り分け 関連付け045 {#c24-i0207}
*分類: 診断・トレース*  ・  難易度: 中級

第四十五観点 診断・トレース で オーバーレイ は 障害切り分け を行う時の主要な確認点です。第四十五観点 確認時には 帳票罫線、固定文言、ロゴなどをページに重ねるための AFP リソースという性質を前提にします。第四十五観点 SDSF ログの APS メッセージ と P1PSF065 を同じ証跡に残し、AFP資源解決の確認を管理します。第四十五観点 確認経路は JES、PSF開始手順、Printer Inventory、SDSFログ、AFPリソースの別を PSF記録065に残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **オーバーレイ 障害切り分け 関連付け045**

    - 検証目的: 診断・トレースにおける オーバーレイ の障害切り分けを机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=P1PSF065
    - セッション環境: AFP Download Plus / Printer Inventory / output log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信先定義確認により オーバーレイ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY AFP DOWNLOAD PRT065
    → Enter を押す
    ```

    画面・出力:
    ```text
    AFP DOWNLOAD PLUS DESTINATION FOR PRT065
    PRINTER PRT065 USES FORMDEF F1PSF065
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。リソース同梱確認により オーバーレイ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? JOB065
    → Enter を押す
    ```

    画面・出力:
    ```text
    OUTPUT GROUP JOB065
    MO:DCA-P DATA WITH INLINE RESOURCE O1PSF065 AND S1PSF065
    ```

    画面・出力には MO:DCA-P が含まれる。MO:DCA-P を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信ログ確認により オーバーレイ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1044I AFP DOWNLOAD PLUS PROCESSING COMPLETED FOR PRT065
    DESTINATION RECORD RETAINED IN PSF LOG
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、Download Plus の宛先誤りを PSF FSA 障害として分ことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: AFP DOWNLOAD PLUS が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: MO:DCA-P が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: AFP DOWNLOAD PLUS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### 診断・トレース PSF Trace ログとの照合 TRACE07 {#c24-i0208}
*分類: 診断・トレース*  ・  難易度: 中級

ログとの照合では 診断・トレース の トレース設定 を主操作として TRACE07 を判定します。時刻と対象識別子への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE07 に残します。ログとの照合を補助する FSA再始動確認 では INTERNAL を補助値として TRACE07 へ保存します。主判定のログとの照合では診断・トレースの トレース設定 から Tracemode を読み TRACE07 へ残します。証跡照合のログとの照合では診断・トレースの Tracemode と INTERNAL を TRACE07 に保存します。記録対応のログとの照合では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE07 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** ログとの照合で 診断・トレース の トレース設定 と FSA再始動確認 を使い 操作とログを対応 します。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。Tracemode を読み対象 TRACE07 を切り分ける確認方法はどれですか。

    - A. Infoprint Server Printer Inventory > FSA PRT07 > Traceが応答を返した時点で正常とする。応答中のTracemodeの値は記録しない。CONNECTをTracemodeと同じ判定値とみなし対象TRACE07の主証跡にする。PSF Traceの時刻と対象識別子は確認済みとして扱う。さらにBROWSE SYS1.PSF.TRACE07のCONNECTをTracemodeと同種の値として併記する。
    - B. Infoprint Server Printer Inventory > FSA PRT07 > Traceのコマンド文字列だけを記録する。Tracemodeを含む応答行は保存しない。
    - C. Tracemodeを含むトレース設定の応答行を保存する。その応答を得るためInfoprint Server Printer Inventory > FSA PRT07 > Traceを使用する。対象TRACE07のTrace ModeとTrace Datasetとして記録する。 ✅
    - D. PSF Traceの停止または再定義を実施する。その後にInfoprint Server Printer Inventory > FSA PRT07 > TraceでTracemodeを採取する。

    正解: **C** ／ 難易度: 中級

    **解説:** 適切な判定: Cはトレース設定で Tracemode を読みTrace ModeとTrace Datasetの主値として操作とログを対応しTRACE07に残します。
    機能の仕組み: ログとの照合ではFSA再始動確認を補助操作としPSF Traceの時刻と対象識別子をINTERNALと対象TRACE07で照合します。
    各候補の評価: トレース設定とFSA再始動確認の役割を分けるとA: 応答の有無だけではTrace ModeとTrace Datasetを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではTrace ModeとTrace Datasetを証明できない点で一次資料と一致しません、C: Tracemodeの実値を対象別に残す点でTRACE07を判定できます、D: 変更前のTrace ModeとTrace Datasetを失う点でFSA再始動確認の範囲を越えます。結論としてログとの照合の診断・トレースで判定する対象は TRACE07 です。
    用語の定義: ログとの照合で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE07へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace ログとの照合 TRACE07**

    - 検証目的: 診断・トレースのPSF Traceについて操作とログを対応し、TRACE07のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT07 > Traceを指定し、TRACE07のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT07 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE07
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT07を指定し、TRACE07のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT07
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT07 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE07
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE07を指定し、TRACE07のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE07
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT07 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Trace が画面・出力に表示されること
    ② ステップ2 の INTERNAL が画面・出力に表示されること
    ③ ステップ3 の CONNECT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 代替経路の確認 TRACE10 {#c24-i0209}
*分類: 診断・トレース*  ・  難易度: 中級

代替経路の確認では 診断・トレース の トレース設定 を主操作として TRACE10 を判定します。主経路との役割差への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE10 に残します。代替経路の確認を補助する FSA再始動確認 では INTERNAL を補助値として TRACE10 へ保存します。主判定の代替経路の確認では診断・トレースの トレース設定 から Tracemode を読み TRACE10 へ残します。証跡照合の代替経路の確認では診断・トレースの Tracemode と INTERNAL を TRACE10 に保存します。記録対応の代替経路の確認では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE10 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 診断・トレース の トレース設定 と FSA再始動確認 を照合し 主経路との役割差 を確かめます。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。Tracemode を読む前に対象 TRACE10 へ行う確認はどれですか。

    - A. Infoprint Server Printer Inventory > FSA PRT10 > Traceのコマンド文字列だけを記録する。Tracemodeを含む応答行は保存しない。
    - B. Infoprint Server Printer Inventory > FSA PRT10 > TraceとF PSF1,DISPLAY,PRT10の対象名をそろえる。前者のTracemodeをTrace ModeとTrace Datasetの判定値として採用する。 ✅
    - C. PSF Traceの停止または再定義を実施する。その後にInfoprint Server Printer Inventory > FSA PRT10 > TraceでTracemodeを採取する。
    - D. フォント管理のCode PageとCharacter Setを確認する。その値を診断・トレースのTRACE10にも適用する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい判定結果: Bはトレース設定で Tracemode を読みTrace ModeとTrace Datasetの主値として代替手段の成立を確認しTRACE10に残します。
    運用上の背景: 代替経路の確認ではFSA再始動確認を補助操作としPSF Traceの主経路との役割差をINTERNALと対象TRACE10で照合します。
    候補別の検討: トレース設定とFSA再始動確認の役割を分けるとA: 入力記録だけではTrace ModeとTrace Datasetを証明できない点で一次資料と一致しません、B: 同じ対象名のTracemodeを採用する点でTRACE10を判定できます、C: 変更前のTrace ModeとTrace Datasetを失う点でFSA再始動確認の範囲を越えます、D: フォント管理の値ではTracemodeを確認できない点でTRACE10の値を示しません。結論として代替経路の確認の診断・トレースで判定する対象は TRACE10 です。
    重要用語の定義: 代替経路の確認で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE10へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 代替経路の確認 TRACE10**

    - 検証目的: 診断・トレースのPSF Traceについて代替手段の成立を確認し、TRACE10のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT10 > Traceを指定し、TRACE10のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT10 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE10
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT10を指定し、TRACE10のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT10
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT10 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE10
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE10を指定し、TRACE10のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE10
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT10 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Trace が画面・出力に表示されること
    ② ステップ2 の INTERNAL が画面・出力に表示されること
    ③ ステップ3 の CONNECT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 変更前の確認 TRACE02 {#c24-i0210}
*分類: 診断・トレース*  ・  難易度: 中級

変更前の確認では 診断・トレース の FSA再始動確認 を主操作として TRACE02 を判定します。変更対象と非対象の境界への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE02 に残します。変更前の確認を補助する トレース参照 では CONNECT を補助値として TRACE02 へ保存します。主判定の変更前の確認では診断・トレースの FSA再始動確認 から INTERNAL を読み TRACE02 へ残します。証跡照合の変更前の確認では診断・トレースの INTERNAL と CONNECT を TRACE02 に保存します。記録対応の変更前の確認では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE02 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 診断・トレース の FSA再始動確認 と トレース参照 を実施し PSF Trace の役割を確認します。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。対象 TRACE02 の証跡を取る方法はどれですか。

    - A. F PSF1,DISPLAY,PRT02を対象名なしで実行する。一覧の先頭行をTRACE02の結果として記録する。
    - B. 対象TRACE02についてF PSF1,DISPLAY,PRT02の応答からINTERNALを確認する。BROWSE SYS1.PSF.TRACE02は補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したF PSF1,DISPLAY,PRT02の結果を使う。今回のBROWSE SYS1.PSF.TRACE02の結果と同一時点の証跡として比較する。
    - D. 保存済みのTRACE02の出力を再利用する。今回のF PSF1,DISPLAY,PRT02とBROWSE SYS1.PSF.TRACE02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 中級

    **解説:** 採用理由: BはFSA再始動確認で INTERNAL を読みTrace ModeとTrace Datasetの主値として変更前の証跡を保存しTRACE02に残します。
    動作の背景: 変更前の確認ではトレース参照を補助操作としPSF Traceの変更対象と非対象の境界をCONNECTと対象TRACE02で照合します。
    各選択肢の検討: FSA再始動確認とトレース参照の役割を分けるとA: 先頭行はTRACE02と確定できない点で変更前の確認に合いません、B: INTERNALと補助証跡の時刻を合わせる点でFSA再始動確認に合います、C: 採取時刻が異なる点で診断・トレースに使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でPSF Traceに使えません。結論として変更前の確認の診断・トレースで判定する対象は TRACE02 です。
    初出用語の定義: 変更前の確認で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE02へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 変更前の確認 TRACE02**

    - 検証目的: 診断・トレースのPSF Traceについて変更前の証跡を保存し、TRACE02のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT02を指定し、TRACE02のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT02
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT02 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE02
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE02を指定し、TRACE02のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE02
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT02 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT02 > Traceを指定し、TRACE02のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT02 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE02
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の INTERNAL が画面・出力に表示されること
    ② ステップ2 の CONNECT が画面・出力に表示されること
    ③ ステップ3 の Trace が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 変更後の確認 TRACE03 {#c24-i0211}
*分類: 診断・トレース*  ・  難易度: 中級

変更後の確認では 診断・トレース の トレース参照 を主操作として TRACE03 を判定します。反映値と残存値への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE03 に残します。変更後の確認を補助する トレース設定 では Tracemode を補助値として TRACE03 へ保存します。主判定の変更後の確認では診断・トレースの トレース参照 から CONNECT を読み TRACE03 へ残します。証跡照合の変更後の確認では診断・トレースの CONNECT と Tracemode を TRACE03 に保存します。記録対応の変更後の確認では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE03 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 診断・トレース の トレース参照 と トレース設定 を用い 変更結果を検証 します。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。CONNECT で対象 TRACE03 の Trace ModeとTrace Dataset を再現できる記録はどれですか。

    - A. PSF Traceの停止または再定義を実施する。その後にBROWSE SYS1.PSF.TRACE03でCONNECTを採取する。
    - B. 出力経路確認のClassとDestinationを確認する。その値を診断・トレースのTRACE03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。PSF Traceの反映値と残存値は確認済みとして扱う。さらにF PSF1,DISPLAY,PRT03のINTERNALをCONNECTと同種の値として併記する。
    - C. Infoprint Server Printer Inventory > FSA PRT03 > Traceで周辺状態を押さえる。その後にBROWSE SYS1.PSF.TRACE03でCONNECTを確認して変更結果を検証する。 ✅
    - D. Infoprint Server Printer Inventory > FSA PRT03 > Traceが成功したためBROWSE SYS1.PSF.TRACE03のCONNECTも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正答の根拠: Cはトレース参照で CONNECT を読みTrace ModeとTrace Datasetの主値として変更結果を検証しTRACE03に残します。
    内部の仕組み: 変更後の確認ではトレース設定を補助操作としPSF Traceの反映値と残存値をTracemodeと対象TRACE03で照合します。
    誤答を含む比較: トレース参照とトレース設定の役割を分けるとA: 変更前のTrace ModeとTrace Datasetを失う点でTrace ModeとTrace Datasetを確認できません、B: 出力経路確認の値ではCONNECTを確認できないうえに追加前提も不正な点でトレース設定の範囲を越えます、C: 周辺状態の後にCONNECTを確認する点で現在値を示します、D: 補助操作の成功ではCONNECTを確定できない点で変更後の確認に合いません。結論として変更後の確認の診断・トレースで判定する対象は TRACE03 です。
    用語定義: 変更後の確認で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE03へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 変更後の確認 TRACE03**

    - 検証目的: 診断・トレースのPSF Traceについて変更結果を検証し、TRACE03のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE03を指定し、TRACE03のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE03
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT03 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT03 > Traceを指定し、TRACE03のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT03 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE03
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT03を指定し、TRACE03のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT03
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT03 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE03
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CONNECT が画面・出力に表示されること
    ② ステップ2 の Trace が画面・出力に表示されること
    ③ ステップ3 の INTERNAL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 引継ぎ記録 TRACE09 {#c24-i0212}
*分類: 診断・トレース*  ・  難易度: 中級

引継ぎ記録では 診断・トレース の トレース参照 を主操作として TRACE09 を判定します。次担当者が追跡できる証跡への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE09 に残します。引継ぎ記録を補助する トレース設定 では Tracemode を補助値として TRACE09 へ保存します。主判定の引継ぎ記録では診断・トレースの トレース参照 から CONNECT を読み TRACE09 へ残します。証跡照合の引継ぎ記録では診断・トレースの CONNECT と Tracemode を TRACE09 に保存します。記録対応の引継ぎ記録では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE09 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 診断・トレース の トレース参照 と トレース設定 を用い 再現可能な記録を作成 します。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。CONNECT で対象 TRACE09 の Trace ModeとTrace Dataset を再現できる記録はどれですか。

    - A. 対象名TRACE09を指定してBROWSE SYS1.PSF.TRACE09を実行する。応答中のCONNECTと時刻を保存する。Infoprint Server Printer Inventory > FSA PRT09 > Traceで周辺状態を補完する。 ✅
    - B. Infoprint Server Printer Inventory > FSA PRT09 > Traceが成功したためBROWSE SYS1.PSF.TRACE09のCONNECTも正常だと推定する。主出力は保存しない。
    - C. BROWSE SYS1.PSF.TRACE09を対象名なしで実行する。一覧の先頭行をTRACE09の結果として記録する。
    - D. 前回保存したBROWSE SYS1.PSF.TRACE09の結果を使う。今回のInfoprint Server Printer Inventory > FSA PRT09 > Traceの結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 中級

    **解説:** 採用操作の理由: Aはトレース参照で CONNECT を読みTrace ModeとTrace Datasetの主値として再現可能な記録を作成しTRACE09に残します。
    製品内の仕組み: 引継ぎ記録ではトレース設定を補助操作としPSF Traceの次担当者が追跡できる証跡をTracemodeと対象TRACE09で照合します。
    選択肢別の説明: トレース参照とトレース設定の役割を分けるとA: CONNECTと時刻を保存する点で現在値を示します、B: 補助操作の成功ではCONNECTを確定できない点で引継ぎ記録に合いません、C: 先頭行はTRACE09と確定できない点でトレース参照を代替しません、D: 採取時刻が異なる点で診断・トレースに使いません。結論として引継ぎ記録の診断・トレースで判定する対象は TRACE09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE09へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 引継ぎ記録 TRACE09**

    - 検証目的: 診断・トレースのPSF Traceについて再現可能な記録を作成し、TRACE09のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE09を指定し、TRACE09のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE09
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT09 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT09 > Traceを指定し、TRACE09のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT09 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE09
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT09を指定し、TRACE09のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT09
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT09 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE09
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CONNECT が画面・出力に表示されること
    ② ステップ2 の Trace が画面・出力に表示されること
    ③ ステップ3 の INTERNAL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 復旧後の確認 TRACE06 {#c24-i0213}
*分類: 診断・トレース*  ・  難易度: 中級

復旧後の確認では 診断・トレース の トレース参照 を主操作として TRACE06 を判定します。再発していないことを示す値への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE06 に残します。復旧後の確認を補助する トレース設定 では Tracemode を補助値として TRACE06 へ保存します。主判定の復旧後の確認では診断・トレースの トレース参照 から CONNECT を読み TRACE06 へ残します。証跡照合の復旧後の確認では診断・トレースの CONNECT と Tracemode を TRACE06 に保存します。記録対応の復旧後の確認では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE06 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 診断・トレース の トレース参照 と トレース設定 の役割を分け 再発していないことを示す値 を調べます。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。対象 TRACE06 を誤判定しない進め方はどれですか。

    - A. 開始手順のPROCNAMEとSTART RESULTを確認する。その値を診断・トレースのTRACE06にも適用する。
    - B. BROWSE SYS1.PSF.TRACE06でCONNECTを取得してからF PSF1,DISPLAY,PRT06でINTERNALを照合する。TRACE06のTrace ModeとTrace Datasetを両出力から確定する。 ✅
    - C. Infoprint Server Printer Inventory > FSA PRT06 > Traceが成功したためBROWSE SYS1.PSF.TRACE06のCONNECTも正常だと推定する。主出力は保存しない。別資源で得た状態を対象TRACE06へ引き継げるものとする。
    - D. BROWSE SYS1.PSF.TRACE06を対象名なしで実行する。一覧の先頭行をTRACE06の結果として記録する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正答内容: Bはトレース参照で CONNECT を読みTrace ModeとTrace Datasetの主値として復旧後の安定性を確認しTRACE06に残します。
    構成上の背景: 復旧後の確認ではトレース設定を補助操作としPSF Traceの再発していないことを示す値をTracemodeと対象TRACE06で照合します。
    候補ごとの理由: トレース参照とトレース設定の役割を分けるとA: 開始手順の値ではCONNECTを確認できない点でトレース設定の範囲を越えます、B: CONNECTとINTERNALを順に照合する点で現在値を示します、C: 補助操作の成功ではCONNECTを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はTRACE06と確定できない点でトレース参照を代替しません。結論として復旧後の確認の診断・トレースで判定する対象は TRACE06 です。
    初出用語: 復旧後の確認で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE06へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 復旧後の確認 TRACE06**

    - 検証目的: 診断・トレースのPSF Traceについて復旧後の安定性を確認し、TRACE06のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE06を指定し、TRACE06のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE06
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT06 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT06 > Traceを指定し、TRACE06のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT06 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE06
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT06を指定し、TRACE06のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT06
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT06 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE06
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CONNECT が画面・出力に表示されること
    ② ステップ2 の Trace が画面・出力に表示されること
    ③ ステップ3 の INTERNAL が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 復旧準備 TRACE05 {#c24-i0214}
*分類: 診断・トレース*  ・  難易度: 中級

復旧準備では 診断・トレース の FSA再始動確認 を主操作として TRACE05 を判定します。再開前に必要な整合性への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE05 に残します。復旧準備を補助する トレース参照 では CONNECT を補助値として TRACE05 へ保存します。主判定の復旧準備では診断・トレースの FSA再始動確認 から INTERNAL を読み TRACE05 へ残します。証跡照合の復旧準備では診断・トレースの INTERNAL と CONNECT を TRACE05 に保存します。記録対応の復旧準備では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE05 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 復旧準備で 診断・トレース の FSA再始動確認 と トレース参照 を組み合わせる際は PSF Trace がFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能という仕組みを前提にします。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。INTERNAL と Trace ModeとTrace Dataset を対象 TRACE05 で確認する組合せはどれですか。

    - A. 変更を加えずF PSF1,DISPLAY,PRT05を実行する。INTERNALを保存する。差分はBROWSE SYS1.PSF.TRACE05の結果と対象名で対応させる。 ✅
    - B. 前回保存したF PSF1,DISPLAY,PRT05の結果を使う。今回のBROWSE SYS1.PSF.TRACE05の結果と同一時点の証跡として比較する。
    - C. 保存済みのTRACE05の出力を再利用する。今回のF PSF1,DISPLAY,PRT05とBROWSE SYS1.PSF.TRACE05は実行済みとして扱う。
    - D. BROWSE SYS1.PSF.TRACE05のCONNECTをTrace ModeとTrace Datasetの主判定に採用する。F PSF1,DISPLAY,PRT05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 中級

    **解説:** 選定理由: AはFSA再始動確認で INTERNAL を読みTrace ModeとTrace Datasetの主値として復旧条件を確認しTRACE05に残します。
    処理の仕組み: 復旧準備ではトレース参照を補助操作としPSF Traceの再開前に必要な整合性をCONNECTと対象TRACE05で照合します。
    選択結果の内訳: FSA再始動確認とトレース参照の役割を分けるとA: 変更前のINTERNALを保存する点でFSA再始動確認に合います、B: 採取時刻が異なる点で診断・トレースに使いません、C: 過去出力では今回の復旧準備を示せない点でPSF Traceに使えません、D: CONNECTはINTERNALを代替しないうえに追加前提も不正な点でTRACE05を採用できません。結論として復旧準備の診断・トレースで判定する対象は TRACE05 です。
    用語の説明: 復旧準備で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE05へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 復旧準備 TRACE05**

    - 検証目的: 診断・トレースのPSF Traceについて復旧条件を確認し、TRACE05のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT05を指定し、TRACE05のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT05
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT05 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE05
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE05を指定し、TRACE05のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE05
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT05 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT05 > Traceを指定し、TRACE05のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT05 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE05
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の INTERNAL が画面・出力に表示されること
    ② ステップ2 の CONNECT が画面・出力に表示されること
    ③ ステップ3 の Trace が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 構成監査 TRACE08 {#c24-i0215}
*分類: 診断・トレース*  ・  難易度: 中級

構成監査では 診断・トレース の FSA再始動確認 を主操作として TRACE08 を判定します。定義値と稼働値の一致への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE08 に残します。構成監査を補助する トレース参照 では CONNECT を補助値として TRACE08 へ保存します。主判定の構成監査では診断・トレースの FSA再始動確認 から INTERNAL を読み TRACE08 へ残します。証跡照合の構成監査では診断・トレースの INTERNAL と CONNECT を TRACE08 に保存します。記録対応の構成監査では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE08 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 構成監査で 診断・トレース の FSA再始動確認 と トレース参照 を実施し PSF Trace の役割を確認します。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。対象 TRACE08 の証跡を取る方法はどれですか。

    - A. 保存済みのTRACE08の出力を再利用する。今回のF PSF1,DISPLAY,PRT08とBROWSE SYS1.PSF.TRACE08は実行済みとして扱う。
    - B. BROWSE SYS1.PSF.TRACE08のCONNECTをTrace ModeとTrace Datasetの主判定に採用する。F PSF1,DISPLAY,PRT08の応答は採取対象から外す。
    - C. Infoprint Server Printer Inventory > FSA PRT08 > TraceのTracemodeをINTERNALと同義の成功表示として扱う。F PSF1,DISPLAY,PRT08は実行しない。
    - D. BROWSE SYS1.PSF.TRACE08の結果だけでは確定しない。F PSF1,DISPLAY,PRT08のINTERNALを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 技術上の正答: DはFSA再始動確認で INTERNAL を読みTrace ModeとTrace Datasetの主値として構成差分を監査しTRACE08に残します。
    実行時の背景: 構成監査ではトレース参照を補助操作としPSF Traceの定義値と稼働値の一致をCONNECTと対象TRACE08で照合します。
    四つの候補の理由: FSA再始動確認とトレース参照の役割を分けるとA: 過去出力では今回の構成監査を示せない点で診断・トレースに使いません、B: CONNECTはINTERNALを代替しない点でPSF Traceに使えません、C: TracemodeとINTERNALは確認項目が異なる点でTRACE08を採用できません、D: INTERNALを主証跡として区別する点で主証跡になります。結論として構成監査の診断・トレースで判定する対象は TRACE08 です。
    初出語定義: 構成監査で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE08へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 構成監査 TRACE08**

    - 検証目的: 診断・トレースのPSF Traceについて構成差分を監査し、TRACE08のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT08を指定し、TRACE08のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT08
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT08 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE08
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE08を指定し、TRACE08のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE08
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT08 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT08 > Traceを指定し、TRACE08のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT08 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE08
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の INTERNAL が画面・出力に表示されること
    ② ステップ2 の CONNECT が画面・出力に表示されること
    ③ ステップ3 の Trace が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 通常状態の確認 TRACE01 {#c24-i0216}
*分類: 診断・トレース*  ・  難易度: 中級

通常状態の確認では 診断・トレース の トレース設定 を主操作として TRACE01 を判定します。基準値と現在値の差への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE01 に残します。通常状態の確認を補助する FSA再始動確認 では INTERNAL を補助値として TRACE01 へ保存します。主判定の通常状態の確認では診断・トレースの トレース設定 から Tracemode を読み TRACE01 へ残します。証跡照合の通常状態の確認では診断・トレースの Tracemode と INTERNAL を TRACE01 に保存します。記録対応の通常状態の確認では診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE01 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 診断・トレース の トレース設定 と FSA再始動確認 を使い 通常状態を確定 します。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。Tracemode を読み対象 TRACE01 を切り分ける確認方法はどれですか。

    - A. Infoprint Server Printer Inventory > FSA PRT01 > Traceを先に実行する。対象TRACE01のTracemodeをTrace ModeとTrace Datasetとして記録する。続いてF PSF1,DISPLAY,PRT01で同一対象を照合する。 ✅
    - B. F PSF1,DISPLAY,PRT01のINTERNALをTrace ModeとTrace Datasetの主判定に採用する。Infoprint Server Printer Inventory > FSA PRT01 > Traceの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - C. BROWSE SYS1.PSF.TRACE01のCONNECTをTracemodeと同義の成功表示として扱う。Infoprint Server Printer Inventory > FSA PRT01 > Traceは実行しない。
    - D. Infoprint Server Printer Inventory > FSA PRT01 > Traceが応答を返した時点で正常とする。応答中のTracemodeの値は記録しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正解の説明: Aはトレース設定で Tracemode を読みTrace ModeとTrace Datasetの主値として通常状態を確定しTRACE01に残します。
    背景・仕組み: 通常状態の確認ではFSA再始動確認を補助操作としPSF Traceの基準値と現在値の差をINTERNALと対象TRACE01で照合します。
    選択肢の理由: トレース設定とFSA再始動確認の役割を分けるとA: Tracemodeを主値として補助結果と照合する点で正答です、B: INTERNALはTracemodeを代替しないうえに追加前提も不正な点でTRACE01を採用できません、C: CONNECTとTracemodeは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではTrace ModeとTrace Datasetを判定できない点で一次資料と一致しません。結論として通常状態の確認の診断・トレースで判定する対象は TRACE01 です。
    用語の初出定義: 通常状態の確認で使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE01へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 通常状態の確認 TRACE01**

    - 検証目的: 診断・トレースのPSF Traceについて通常状態を確定し、TRACE01のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT01 > Traceを指定し、TRACE01のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT01 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE01
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT01を指定し、TRACE01のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT01
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT01 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE01
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE01を指定し、TRACE01のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE01
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT01 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Trace が画面・出力に表示されること
    ② ステップ2 の INTERNAL が画面・出力に表示されること
    ③ ステップ3 の CONNECT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 診断・トレース PSF Trace 障害切り分け TRACE04 {#c24-i0217}
*分類: 診断・トレース*  ・  難易度: 中級

障害切り分けでは 診断・トレース の トレース設定 を主操作として TRACE04 を判定します。最初に失敗した処理への注意として「Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります」を TRACE04 に残します。障害切り分けを補助する FSA再始動確認 では INTERNAL を補助値として TRACE04 へ保存します。主判定の障害切り分けでは診断・トレースの トレース設定 から Tracemode を読み TRACE04 へ残します。証跡照合の障害切り分けでは診断・トレースの Tracemode と INTERNAL を TRACE04 に保存します。記録対応の障害切り分けでは診断・トレースの Trace ModeとTrace Dataset の証跡へ TRACE04 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 診断・トレース の トレース設定 と FSA再始動確認 を照合し 最初に失敗した処理 を確かめます。PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能です。Fullトレースを長時間継続してスプールやデータセットを圧迫する危険があります。Tracemode を読む前に対象 TRACE04 へ行う確認はどれですか。

    - A. BROWSE SYS1.PSF.TRACE04のCONNECTをTracemodeと同義の成功表示として扱う。Infoprint Server Printer Inventory > FSA PRT04 > Traceは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. Infoprint Server Printer Inventory > FSA PRT04 > Traceが応答を返した時点で正常とする。応答中のTracemodeの値は記録しない。
    - C. Infoprint Server Printer Inventory > FSA PRT04 > Traceのコマンド文字列だけを記録する。Tracemodeを含む応答行は保存しない。
    - D. Infoprint Server Printer Inventory > FSA PRT04 > Traceの出力でTRACE04とTracemodeが同じ応答にあることを確認する。Trace ModeとTrace Datasetをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい操作の説明: Dはトレース設定で Tracemode を読みTrace ModeとTrace Datasetの主値として障害範囲を限定しTRACE04に残します。
    技術的背景: 障害切り分けではFSA再始動確認を補助操作としPSF Traceの最初に失敗した処理をINTERNALと対象TRACE04で照合します。
    四択の評価: トレース設定とFSA再始動確認の役割を分けるとA: CONNECTとTracemodeは確認項目が異なるうえに追加前提も不正な点でTRACE04を採用できません、B: 応答の有無だけではTrace ModeとTrace Datasetを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではTrace ModeとTrace Datasetを証明できない点で一次資料と一致しません、D: TRACE04とTracemodeを同じ応答で結ぶ点でTRACE04を判定できます。結論として障害切り分けの診断・トレースで判定する対象は TRACE04 です。
    初出語の意味: 障害切り分けで使う PSF Trace はFSSまたはFSAの初期化、接続、資源、データストリーム処理をトレースデータセットへ記録する診断機能を表しTrace ModeとTrace Datasetを判定する際にTRACE04へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **診断・トレース PSF Trace 障害切り分け TRACE04**

    - 検証目的: 診断・トレースのPSF Traceについて障害範囲を限定し、TRACE04のTrace ModeとTrace Datasetを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象TRACE04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へInfoprint Server Printer Inventory > FSA PRT04 > Traceを指定し、TRACE04のトレース設定を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> Infoprint Server Printer Inventory > FSA PRT04 > Trace
    → Enter を押す
    ```

    画面・出力:
    ```text
    Trace mode: internal Trace data set: SYS1.PSF.TRACE04
    ```

    画面・出力にあるTraceを読み、Trace ModeとTrace Datasetと対象TRACE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へF PSF1,DISPLAY,PRT04を指定し、TRACE04のFSA再始動確認を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSF1,DISPLAY,PRT04
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS101I FSA PRT04 STATUS IDLE TRACE INTERNAL DATASET SYS1.PSF.TRACE04
    ```

    画面・出力にあるINTERNALを読み、Trace ModeとTrace Datasetと対象TRACE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の診断・トレースを確認する入力画面です。COMMAND入力口へBROWSE SYS1.PSF.TRACE04を指定し、TRACE04のトレース参照を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> BROWSE SYS1.PSF.TRACE04
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF TRACE FSA PRT04 EVENT CONNECT RESPONSE SUCCESS TIME 14:45:00
    ```

    画面・出力にあるCONNECTを読み、Trace ModeとTrace Datasetと対象TRACE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Trace が画面・出力に表示されること
    ② ステップ2 の INTERNAL が画面・出力に表示されること
    ③ ステップ3 の CONNECT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes




## PSF for z/OS 4.7 > 起動設定

### AFPPARMS {#c24-i0218}
*分類: 起動設定*  ・  難易度: 上級

PSF for z/OS 4.7 の 起動設定で扱うAFPPARMSは、PSF の AFP 関連パラメータを指定する制御ステートメントです。リソース探索、メモリ利用、印刷機能の挙動に影響します。変更時は対象 FSA と反映タイミングを確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 比較確認の起動設定で AFPPARMS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. AFPPARMS の出力を取らず比較確認の起動設定の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較確認の確認記録にまとめる。 ✅
    - C. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を省略して比較確認の起動設定の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の起動設定へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では AFPPARMS は「比較確認の起動設定に関係する定義値と表示行を照合する比較確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では AFPPARMS の属性行と APS933I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では AFPPARMS を PSF for z/OS 4.7の運用手順で確認し、初出名は比較確認初出です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **AFPPARMS**

    - 検証目的: 比較確認の起動設定について、PSF for z/OS 4.7 の 起動設定で扱う AFPPARMS は、PSF の AFP 関連パラメータを指定する制御ステートメントです。リソース探索、メモリ利用、印刷機に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、比較確認の起動設定の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にAFPPARMSを指定し、OSKB010014の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND AFPPARMS
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM AFPPARMS
    CASE OSKB010014
    SOURCE PSF for z/OS
    ```

    AFPPARMSとOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010014を同じ出力で読み、比較確認の起動設定の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010014
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010014
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の AFPPARMS と OSKB010014 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes



### EXEC PARM パラメータ {#c24-i0219}
*分類: 起動設定*  ・  難易度: 中級

PSF for z/OS 4.7 の 起動設定で扱うEXEC PARM パラメータは、PSF 起動 JCL の EXEC 文で渡す起動時指定です。FSS や FSA の起動挙動に影響するため、プロシージャ変更時に確認が必要です。起動失敗では PARM 指定とメッセージを対応させます

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 順序確認のパラメータで印刷サービスの運用確認を行います。EXEC PARM パラメータの根拠にできる作業はどれですか。

    - A. PSF for z/OS と無関係な一覧で順序確認のパラメータを確認した扱いにする。
    - B. APS933I の有無を確認せず順序確認のパラメータを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 ✅
    - D. EXEC PARM パラメータの属性行を読まず順序確認のパラメータの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では EXEC PARM パラメータ は「PSF for z/OS で EXEC PARM パラメータの扱いを記録する順序確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では EXEC PARM パラメータの表示結果と APS933I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では EXEC PARM パラメータの使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **EXEC PARM パラメータ**

    - 検証目的: 順序確認のパラメータについて、PSF for z/OS 4.7 の 起動設定で扱う EXEC PARM パラメータは、PSF 起動 JCL の EXEC 文で渡す起動時指定です。FSS や FSA の起動に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、順序確認のパラメータの確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にEXEC PARM パラメータを指定し、OSKB010015の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND EXEC PARM パラメータ
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM EXEC PARM パラメータ
    CASE OSKB010015
    SOURCE PSF for z/OS
    ```

    EXEC PARM パラメータとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010015を同じ出力で読み、順序確認のパラメータの根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010015
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010015
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の EXEC PARM パラメータ と OSKB010015 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes




## PSF for z/OS 4.7 > 運用

### AFP Download Plus {#c24-i0220}
*分類: 運用*  ・  難易度: 上級

PSF for z/OS 4.7 の 運用で扱うAFP Download Plusは、AFP データを別システムへ配布する関連機能です。PSF と同じ Printer Inventory 定義や FSS/FSA 概念が関わる場面があります。配布障害では送信先、リソース、定義名を合わせて確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 変更確認の運用に関する AFP Download Plusの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO の結果を残さず変更確認の運用の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の運用の証跡として保存して根拠にする。
    - C. AFP Download Plusの変更点を出力本文から切り離して変更確認の運用の承認欄のみ残す。
    - D. PSF for z/OS の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では AFP Download Plus は「AFP Download Plusの状態と出力メッセージを結び付ける変更確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では AFP Download Plusの出力行と APS933I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では AFP Download Plusを PSF for z/OS の確認記録に残し、対象名は変更確認対象です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **AFP Download Plus**

    - 検証目的: 変更確認の運用について、PSF for z/OS 4.7 の 運用で扱う AFP Download Plusは、AFP データを別システムへ配布する関連機能です。PSF と同じ Printer Inに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、変更確認の運用の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にAFP Download Plusを指定し、OSKB010020の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND AFP Download Plus
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM AFP Download Plus
    CASE OSKB010020
    SOURCE PSF for z/OS
    ```

    AFP Download PlusとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010020を同じ出力で読み、変更確認の運用の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010020
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010020
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の AFP Download Plus と OSKB010020 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes



### プリンター再始動 {#c24-i0221}
*分類: 運用*  ・  難易度: 中級

PSF for z/OS 4.7 の 運用で扱うプリンター再始動は、異常終了や接続障害後に PSF の印刷処理を再開する運用です。FSA、JES 出力、プリンター本体の状態が一致していないと再開できません。再始動前に保留出力と重複印刷のリスクを確認します

**出典:** PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes

??? question "確認問題（1問）"
    **問題.** 監査確認のプリンター再始動で印刷サービスの運用確認を行います。プリンター再始動の根拠にできる作業はどれですか。

    - A. PSF for z/OS と無関係な一覧で監査確認のプリンター再始動を確認した扱いにする。
    - B. APS933I の有無を確認せず監査確認のプリンター再始動を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 ✅
    - D. プリンター再始動の属性行を読まず監査確認のプリンター再始動の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠ではプリンター再始動は「PSF for z/OS でプリンター再始動の扱いを記録する監査確認項目」と F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡ではプリンター再始動の表示結果と APS933I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料ではプリンター再始動の使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** zOS31_apsd000_v4r7 / apss000_v4r7


??? note "検証手順（1件）"
    **プリンター再始動**

    - 検証目的: 監査確認のプリンター再始動について、PSF for z/OS 4.7 の 運用で扱うプリンター再始動は、異常終了や接続障害後に PSF の印刷処理を再開する運用です。FSA、JES 出力、プリンター本体の状態に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。
    - セッション環境: MVS ConsoleでF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOを実行し、APS933Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===> に F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO を入力し、監査確認のプリンター再始動の確認表示へ進みます。
    操作（入力）:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    ```

    COMMAND INPUTにF PSFPROC,DISPLAY,FSA1,DATA=PRTINFOが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はMVS Consoleの表示結果です。FIND欄にプリンター再始動を指定し、OSKB010019の対象行を見つけます。
    操作（入力）:
    ```text
    (MVS Console Result)
    COMMAND INPUT ===> FIND プリンター再始動
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (MVS Console Result)
    ITEM プリンター再始動
    CASE OSKB010019
    SOURCE PSF for z/OS
    ```

    プリンター再始動とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はMVS Consoleの詳細表示です。APS933IとOSKB010019を同じ出力で読み、監査確認のプリンター再始動の根拠を記録します。
    操作（入力）:
    ```text
    (MVS Console Detail)
    COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    CASE OSKB010019
    → Enter を押す
    ```

    画面・出力:
    ```text
    PSF OPERATOR INTERFACE OSKB010019
    F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO
    APS933I PSF CONNECTED TO RECEIVER
    FSA FSA1 PRINTER INFORMATION DISPLAYED
    ```

    APS933IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> F PSFPROC,DISPLAY,FSA1,DATA=PRTINFO が画面・出力に表示されること
    ② ステップ2 の プリンター再始動 と OSKB010019 が画面・出力に表示されること
    ③ ステップ3 の APS933I と OSKB010019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: PSF for z / OS V4R7 Overview / OS Customization / OS Security Guide / OS Messages and Codes




## PSF for z/OS 4.7 > 開始手順

### AFPPARMS トレース準備 確認027 {#c24-i0222}
*分類: 開始手順*  ・  難易度: 中級

第二十七観点 開始手順 で AFPPARMS は印刷処理の対象を特定するためのPSF側の確認項目です。第二十七観点 対象は PSF のプリンター関連パラメーターを与える制御情報で、Printer Inventorです。第二十七観点 AFP Download Plus の宛先指定 をSDSFログと突き合わせ、ログ時点差の確認を作業票へ反映します。第二十七観点 後続確認では FSS、FSA、PRTnnnn、資源名の対応を PSF記録047から再現します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **AFPPARMS トレース準備 確認027**

    - 検証目的: 開始手順における AFPPARMS のトレース準備を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=O1PSF047
    - セッション環境: ISPF browse / AFP resource library / SDSF

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。フォーム定義参照により AFPPARMS の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE PSF.USER.FDEFLIB(F1PSF047)
    → Enter を押す
    ```

    画面・出力:
    ```text
    FORMDEF F1PSF047
    COPYGROUP CG03 MEDIUM MAP AND DUPLEX SETTINGS LISTED
    ```

    画面・出力には FORMDEF が含まれる。FORMDEF を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。ページ定義参照により AFPPARMS の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE PSF.USER.PDEFLIB(P1PSF047)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PAGEDEF P1PSF047
    LINE DATA MAPPING USES FONT C0PSF03 AND PAGE FORMAT PF03
    ```

    画面・出力には PAGEDEF が含まれる。PAGEDEF を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。出力属性照合により AFPPARMS の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? PRT047
    → Enter を押す
    ```

    画面・出力:
    ```text
    JES OUTPUT FOR PRT047
    FORMDEF F1PSF047 PAGEDEF P1PSF047 CHARS C0PSF03
    ```

    画面・出力には CHARS が含まれる。CHARS を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: FORMDEF が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: PAGEDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: CHARS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### AFPPARMS フォント照合 開始確認087 {#c24-i0223}
*分類: 開始手順*  ・  難易度: 上級

第八十七観点 開始手順 で AFPPARMS は印刷処理の対象を特定するためのPSF側の確認項目です。第八十七観点 確認時には PSF のプリンター関連パラメーターを与える制御情報で、Printer Inventorという性質を前提にします。第八十七観点 AFP Download Plus の宛先指定 の値を O1PSF107 と合わせ、ログ時点差の確認を記録します。第八十七観点 後続確認では FSS、FSA、PRTnnnn、資源名の対応を PSF記録107から再現します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **AFPPARMS フォント照合 開始確認087**

    - 検証目的: 開始手順における AFPPARMS のフォント照合を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=O1PSF107
    - セッション環境: ISPF browse / AFP resource library / SDSF

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。フォーム定義参照により AFPPARMS の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE PSF.USER.FDEFLIB(F1PSF107)
    → Enter を押す
    ```

    画面・出力:
    ```text
    FORMDEF F1PSF107
    COPYGROUP CG15 MEDIUM MAP AND DUPLEX SETTINGS LISTED
    ```

    画面・出力には FORMDEF が含まれる。FORMDEF を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。ページ定義参照により AFPPARMS の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE PSF.USER.PDEFLIB(P1PSF107)
    → Enter を押す
    ```

    画面・出力:
    ```text
    PAGEDEF P1PSF107
    LINE DATA MAPPING USES FONT C0PSF15 AND PAGE FORMAT PF15
    ```

    画面・出力には PAGEDEF が含まれる。PAGEDEF を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。出力属性照合により AFPPARMS の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? PRT107
    → Enter を押す
    ```

    画面・出力:
    ```text
    JES OUTPUT FOR PRT107
    FORMDEF F1PSF107 PAGEDEF P1PSF107 CHARS C0PSF15
    ```

    画面・出力には CHARS が含まれる。CHARS を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: FORMDEF が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: PAGEDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: CHARS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### Download for z/OS 定義照合 確認051 {#c24-i0224}
*分類: 開始手順*  ・  難易度: 中級

第五十一観点 Download for z/OS は PSF for z/OS の 開始手順 で確認する技術要素です。第五十一観点 リモート側処理へ出力を渡す連携機能で、データ変換、宛先、ログを照合する対象という範囲をAFP資源名と合わせます。第五十一観点 Printer Inventory の FSS/FSA パラメーター をSDSFログと突き合わせ、AFP資源解決の確認を作業票へ反映します。第五十一観点 記録では JES定義、PRINTDEV、APSメッセージ、AFP資源のどこを見たかを PSF記録071へ書きます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **Download for z/OS 定義照合 確認051**

    - 検証目的: 開始手順における Download for z/OS の定義照合を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=PRT071
    - セッション環境: SDSF / JES2 console / PSF log review

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。$D PRT 表示により Download for z/OS の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> /$D PRT071
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP603 PRT071 DISPLAY
    PRINTER PRT071 ASSOCIATED WITH FSS PSF03 AND FSA FSA03
    ```

    画面・出力には $HASP603 が含まれる。$HASP603 を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。PSF手順参照により Download for z/OS の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PROCLIB(PSFPROC03)
    → Enter を押す
    ```

    画面・出力:
    ```text
    //PSFPROC03 PROC
    //PRT071 CNTL
    // PRINTDEV FONTLIB=PSF.FONTLIB,FORMDEF=F1PSF071,PAGEDEF=P1PSF071
    //PRT071 ENDCNTL
    ```

    画面・出力には PRINTDEV が含まれる。PRINTDEV を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。APSログ確認により Download for z/OS の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS000I SUBSYSTEM PSF03 ACTIVE
    APS1050I PRINTER PRT071 SELECTED BY PSF FSA FSA03
    ```

    画面・出力には APS000I が含まれる。APS000I を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: $HASP603 が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: PRINTDEV が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS000I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### JES2 FSSDEF プリンター関連付け 開始確認063 {#c24-i0225}
*分類: 開始手順*  ・  難易度: 中級

第六十三観点 JES2 FSSDEF は 開始手順 の定義、ログ、資源をつなぐ確認対象です。第六十三観点 PSF 開始手順を JES2 初期設定へ結び付け、機能サブシステム名とプロシージャ名を定という性質を開始手順で確認します。第六十三観点 コード化フォントとコードページの組合せ の値を FSA15 と合わせ、APSメッセージ範囲の確認を記録します。第六十三観点 調査票ではSDSFログ、ISPF参照、Printer Inventoryの入口を PSF記録083に区別して残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **JES2 FSSDEF プリンター関連付け 開始確認063**

    - 検証目的: 開始手順における JES2 FSSDEF のプリンター関連付けを机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=FSA15
    - セッション環境: Printer Inventory / PSF customization review / console

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。Printer Inventory 確認により JES2 FSSDEF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY PRINTER PRT083
    → Enter を押す
    ```

    画面・出力:
    ```text
    PRINTER PRT083
    FSS PSF15
    FSA FSA15
    TCP/IP ATTACHMENT PARAMETERS SHOWN
    ```

    画面・出力には PRINTER が含まれる。PRINTER を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSSDEF 照合により JES2 FSSDEF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(JES2PARM)
    Command ===> FIND PSF15
    → Enter を押す
    ```

    画面・出力:
    ```text
    FSSDEF PSF15,PROC=PSFPROC15
    PRT083 FSS=PSF15,MODE=FSS
    ```

    画面・出力には FSSDEF が含まれる。FSSDEF を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSAメッセージ確認により JES2 FSSDEF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> FIND FSA15
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1062I FSA15 INITIALIZATION MESSAGE FOR PRT083
    APS000I SUBSYSTEM PSF15 ACTIVE
    ```

    画面・出力には FSA15 が含まれる。FSA15 を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: PRINTER が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FSSDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: FSA15 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### JES2 FSSDEF リソース解決 確認003 {#c24-i0226}
*分類: 開始手順*  ・  難易度: 初級

第三観点 JES2 FSSDEF は 開始手順 の定義、ログ、資源をつなぐ確認対象です。第三観点 確認時には PSF 開始手順を JES2 初期設定へ結び付け、機能サブシステム名とプロシージャ名を定という性質を前提にします。第三観点 コード化フォントとコードページの組合せ をSDSFログと突き合わせ、APSメッセージ範囲の確認を作業票へ反映します。第三観点 調査票ではSDSFログ、ISPF参照、Printer Inventoryの入口を PSF記録023に区別して残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **JES2 FSSDEF リソース解決 確認003**

    - 検証目的: 開始手順における JES2 FSSDEF のリソース解決を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=FSA03
    - セッション環境: Printer Inventory / PSF customization review / console

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。Printer Inventory 確認により JES2 FSSDEF の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY PRINTER PRT023
    → Enter を押す
    ```

    画面・出力:
    ```text
    PRINTER PRT023
    FSS PSF03
    FSA FSA03
    TCP/IP ATTACHMENT PARAMETERS SHOWN
    ```

    画面・出力には PRINTER が含まれる。PRINTER を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSSDEF 照合により JES2 FSSDEF の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(JES2PARM)
    Command ===> FIND PSF03
    → Enter を押す
    ```

    画面・出力:
    ```text
    FSSDEF PSF03,PROC=PSFPROC03
    PRT023 FSS=PSF03,MODE=FSS
    ```

    画面・出力には FSSDEF が含まれる。FSSDEF を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。FSAメッセージ確認により JES2 FSSDEF の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF LOG
    COMMAND ===> FIND FSA03
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1002I FSA03 INITIALIZATION MESSAGE FOR PRT023
    APS000I SUBSYSTEM PSF03 ACTIVE
    ```

    画面・出力には FSA03 が含まれる。FSA03 を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: PRINTER が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FSSDEF が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: FSA03 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### MO:DCA-P 定義照合 確認099 {#c24-i0227}
*分類: 開始手順*  ・  難易度: 上級

第九十九観点 開始手順 の中で MO:DCA-P はJES、PSF、AFP資源の対応を説明するための項目です。第九十九観点 資料上の意味は ページ構成済みの文書データで、配置、提示、フォント参照などを構造化フィールドとして保持すという範囲で読み取ります。第九十九観点 JES2 FSSDEF と PRTnnnn 定義 をSDSFログと突き合わせ、JES定義とPSF手順の混同防止を作業票へ反映します。第九十九観点 証跡には APS メッセージの連続行 と資料名を併記し、PSF記録119として保存します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **MO:DCA-P 定義照合 確認099**

    - 検証目的: 開始手順における MO:DCA-P の定義照合を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=APS1098I
    - セッション環境: PSF diagnosis / trace data set / SDSF log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース準備により MO:DCA-P の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF dataset list
    Command ===> DSLIST 'PSF.TRACE.119'
    → Enter を押す
    ```

    画面・出力:
    ```text
    DATA SET PSF.TRACE.119 CATALOGED
    TRACE TARGET FOR FSA03
    ```

    画面・出力には TRACE が含まれる。TRACE を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース開始指定により MO:DCA-P の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F PSF03,TRACE,FORMAT=PSF,COMP=MSGM
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1098I TRACE COMMAND ACCEPTED FOR PSF03
    FORMAT PSF COMPONENT MSGM
    ```

    画面・出力には FORMAT が含まれる。FORMAT を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。メッセージ連続確認により MO:DCA-P の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS1098I
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1098I TRACE RECORD WRITTEN FOR PRT119
    APS000I SUBSYSTEM PSF03 ACTIVE
    ```

    画面・出力には APS1098I が含まれる。APS1098I を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: TRACE が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FORMAT が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS1098I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### MO:DCA-P 送信先確認 開始確認039 {#c24-i0228}
*分類: 開始手順*  ・  難易度: 中級

第三十九観点 開始手順 の中で MO:DCA-P はJES、PSF、AFP資源の対応を説明するための項目です。第三十九観点 ページ構成済みの文書データで、配置、提示、フォント参照などを構造化フィールドとして保持すという前提をFSS/FSAの対応で点検します。第三十九観点 JES2 FSSDEF と PRTnnnn 定義 の値を APS1038I と合わせ、JES定義とPSF手順の混同防止を記録します。第三十九観点 証跡には APS メッセージの連続行 と資料名を併記し、PSF記録059として保存します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **MO:DCA-P 送信先確認 開始確認039**

    - 検証目的: 開始手順における MO:DCA-P の送信先確認を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=APS1038I
    - セッション環境: PSF diagnosis / trace data set / SDSF log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース準備により MO:DCA-P の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF dataset list
    Command ===> DSLIST 'PSF.TRACE.059'
    → Enter を押す
    ```

    画面・出力:
    ```text
    DATA SET PSF.TRACE.059 CATALOGED
    TRACE TARGET FOR FSA15
    ```

    画面・出力には TRACE が含まれる。TRACE を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。トレース開始指定により MO:DCA-P の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    z/OS console
    COMMAND ===> /F PSF15,TRACE,FORMAT=PSF,COMP=MSGM
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1038I TRACE COMMAND ACCEPTED FOR PSF15
    FORMAT PSF COMPONENT MSGM
    ```

    画面・出力には FORMAT が含まれる。FORMAT を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。メッセージ連続確認により MO:DCA-P の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS1038I
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1038I TRACE RECORD WRITTEN FOR PRT059
    APS000I SUBSYSTEM PSF15 ACTIVE
    ```

    画面・出力には APS1038I が含まれる。APS1038I を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: TRACE が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: FORMAT が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: APS1038I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### オーバーレイ トレース準備 確認075 {#c24-i0229}
*分類: 開始手順*  ・  難易度: 中級

第七十五観点 開始手順 で オーバーレイ は トレース準備 を行う時の主要な確認点です。第七十五観点 帳票罫線、固定文言、ロゴなどをページに重ねるための AFP リソースという内容を手順値と照合します。第七十五観点 SDSF ログの APS メッセージ をSDSFログと突き合わせ、トレース準備漏れの発見を作業票へ反映します。第七十五観点 確認経路は JES、PSF開始手順、Printer Inventory、SDSFログ、AFPリソースの別を PSF記録095に残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **オーバーレイ トレース準備 確認075**

    - 検証目的: 開始手順における オーバーレイ のトレース準備を机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=P1PSF095
    - セッション環境: AFP Download Plus / Printer Inventory / output log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信先定義確認により オーバーレイ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY AFP DOWNLOAD PRT095
    → Enter を押す
    ```

    画面・出力:
    ```text
    AFP DOWNLOAD PLUS DESTINATION FOR PRT095
    PRINTER PRT095 USES FORMDEF F1PSF095
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。リソース同梱確認により オーバーレイ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? JOB095
    → Enter を押す
    ```

    画面・出力:
    ```text
    OUTPUT GROUP JOB095
    MO:DCA-P DATA WITH INLINE RESOURCE O1PSF095 AND S1PSF095
    ```

    画面・出力には MO:DCA-P が含まれる。MO:DCA-P を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信ログ確認により オーバーレイ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1074I AFP DOWNLOAD PLUS PROCESSING COMPLETED FOR PRT095
    DESTINATION RECORD RETAINED IN PSF LOG
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、Printer Inventory と開始手順の値を別管理として扱うこことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: AFP DOWNLOAD PLUS が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: MO:DCA-P が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: AFP DOWNLOAD PLUS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### オーバーレイ プリンター関連付け 開始確認015 {#c24-i0230}
*分類: 開始手順*  ・  難易度: 初級

第十五観点 開始手順 で オーバーレイ は プリンター関連付け を行う時の主要な確認点です。第十五観点 資料上の意味は 帳票罫線、固定文言、ロゴなどをページに重ねるための AFP リソースという範囲で読み取ります。第十五観点 SDSF ログの APS メッセージ の値を P1PSF035 と合わせ、トレース準備漏れの発見を記録します。第十五観点 確認経路は JES、PSF開始手順、Printer Inventory、SDSFログ、AFPリソースの別を PSF記録035に残します。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7

??? note "検証手順（1件）"
    **オーバーレイ プリンター関連付け 開始確認015**

    - 検証目的: 開始手順における オーバーレイ のプリンター関連付けを机上で確認する。
    - 前提条件: PSF for z/OS の対象FSS、FSA、JES定義、Printer Inventory、SDSFログ、AFPリソースを確認済み。対象=P1PSF035
    - セッション環境: AFP Download Plus / Printer Inventory / output log

    **ステップ 1**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信先定義確認により オーバーレイ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Printer Inventory panel
    Action ===> DISPLAY AFP DOWNLOAD PRT035
    → Enter を押す
    ```

    画面・出力:
    ```text
    AFP DOWNLOAD PLUS DESTINATION FOR PRT035
    PRINTER PRT035 USES FORMDEF F1PSF035
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。リソース同梱確認により オーバーレイ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    SDSF output panel
    COMMAND ===> ? JOB035
    → Enter を押す
    ```

    画面・出力:
    ```text
    OUTPUT GROUP JOB035
    MO:DCA-P DATA WITH INLINE RESOURCE O1PSF035 AND S1PSF035
    ```

    画面・出力には MO:DCA-P が含まれる。MO:DCA-P を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は PSF for z/OS の確認画面またはログ表示である。送信ログ確認により オーバーレイ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF log browse
    COMMAND ===> FIND APS
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS1014I AFP DOWNLOAD PLUS PROCESSING COMPLETED FOR PRT035
    DESTINATION RECORD RETAINED IN PSF LOG
    ```

    画面・出力には AFP DOWNLOAD PLUS が含まれる。AFP DOWNLOAD PLUS を読み取り、FSA が別プリンターの属性で起動した原因を見落とすことを避けるため対象の現在値を記録する。

    - 合格条件: ステップ1: AFP DOWNLOAD PLUS が画面または出力に表示され、対象プリンター、FSS、FSA、資源名が取り違えられていないこと。
    ステップ2: MO:DCA-P が画面または出力に表示され、開始手順、JES定義、AFPリソースの対応が確認できること。
    ステップ3: AFP DOWNLOAD PLUS が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / psf_v4r7_messages_and_codes / apsp000_v4r7



### 開始手順 PSF started task ログとの照合 START07 {#c24-i0231}
*分類: 開始手順*  ・  難易度: 中級

ログとの照合では 開始手順 の FSS定義表示 を主操作として START07 を判定します。時刻と対象識別子への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START07 に残します。ログとの照合を補助する 開始 では IEF403I を補助値として START07 へ保存します。主判定のログとの照合では開始手順の FSS定義表示 から PROC=PSFPROC を読み START07 へ残します。証跡照合のログとの照合では開始手順の PROC=PSFPROC と IEF403I を START07 に保存します。記録対応のログとの照合では開始手順の PROCNAMEとSTART RESULT の証跡へ START07 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** ログとの照合で 開始手順 の FSS定義表示 と 開始 を使い 操作とログを対応 します。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。PROC=PSFPROC を読み対象 START07 を切り分ける確認方法はどれですか。

    - A. $D FSS(PSF1)が応答を返した時点で正常とする。応答中のPROC=PSFPROCの値は記録しない。ACTIVEをPROC=PSFPROCと同じ判定値とみなし対象START07の主証跡にする。
    - B. $D FSS(PSF1)のコマンド文字列だけを記録する。PROC=PSFPROCを含む応答行は保存しない。
    - C. PROC=PSFPROCを含むFSS定義表示の応答行を保存する。その応答を得るため$D FSS(PSF1)を使用する。対象START07のPROCNAMEとSTART RESULTとして記録する。 ✅
    - D. PSF started taskの停止または再定義を実施する。その後に$D FSS(PSF1)でPROC=PSFPROCを採取する。

    正解: **C** ／ 難易度: 中級

    **解説:** 適切な判定: CはFSS定義表示で PROC=PSFPROC を読みPROCNAMEとSTART RESULTの主値として操作とログを対応しSTART07に残します。
    機能の仕組み: ログとの照合では開始を補助操作としPSF started taskの時刻と対象識別子をIEF403Iと対象START07で照合します。
    各候補の評価: FSS定義表示と開始の役割を分けるとA: 応答の有無だけではPROCNAMEとSTART RESULTを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではPROCNAMEとSTART RESULTを証明できない点で一次資料と一致しません、C: PROC=PSFPROCの実値を対象別に残す点でSTART07を判定できます、D: 変更前のPROCNAMEとSTART RESULTを失う点で開始の範囲を越えます。結論としてログとの照合の開始手順で判定する対象は START07 です。
    用語の定義: ログとの照合で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART07へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task ログとの照合 START07**

    - 検証目的: 開始手順のPSF started taskについて操作とログを対応し、START07のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START07のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START07の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START07の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROC=PSFPROC が画面・出力に表示されること
    ② ステップ2 の IEF403I が画面・出力に表示されること
    ③ ステップ3 の ACTIVE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 代替経路の確認 START10 {#c24-i0232}
*分類: 開始手順*  ・  難易度: 中級

代替経路の確認では 開始手順 の FSS定義表示 を主操作として START10 を判定します。主経路との役割差への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START10 に残します。代替経路の確認を補助する 開始 では IEF403I を補助値として START10 へ保存します。主判定の代替経路の確認では開始手順の FSS定義表示 から PROC=PSFPROC を読み START10 へ残します。証跡照合の代替経路の確認では開始手順の PROC=PSFPROC と IEF403I を START10 に保存します。記録対応の代替経路の確認では開始手順の PROCNAMEとSTART RESULT の証跡へ START10 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で 開始手順 の FSS定義表示 と 開始 を照合し 主経路との役割差 を確かめます。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。PROC=PSFPROC を読む前に対象 START10 へ行う確認はどれですか。

    - A. $D FSS(PSF1)のコマンド文字列だけを記録する。PROC=PSFPROCを含む応答行は保存しない。
    - B. $D FSS(PSF1)とS PSFPROCの対象名をそろえる。前者のPROC=PSFPROCをPROCNAMEとSTART RESULTの判定値として採用する。 ✅
    - C. PSF started taskの停止または再定義を実施する。その後に$D FSS(PSF1)でPROC=PSFPROCを採取する。
    - D. フォント管理のCode PageとCharacter Setを確認する。その値を開始手順のSTART10にも適用する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい判定結果: BはFSS定義表示で PROC=PSFPROC を読みPROCNAMEとSTART RESULTの主値として代替手段の成立を確認しSTART10に残します。
    運用上の背景: 代替経路の確認では開始を補助操作としPSF started taskの主経路との役割差をIEF403Iと対象START10で照合します。
    候補別の検討: FSS定義表示と開始の役割を分けるとA: 入力記録だけではPROCNAMEとSTART RESULTを証明できない点で一次資料と一致しません、B: 同じ対象名のPROC=PSFPROCを採用する点でSTART10を判定できます、C: 変更前のPROCNAMEとSTART RESULTを失う点で開始の範囲を越えます、D: フォント管理の値ではPROC=PSFPROCを確認できない点でSTART10の値を示しません。結論として代替経路の確認の開始手順で判定する対象は START10 です。
    重要用語の定義: 代替経路の確認で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART10へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 代替経路の確認 START10**

    - 検証目的: 開始手順のPSF started taskについて代替手段の成立を確認し、START10のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START10のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START10の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START10の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROC=PSFPROC が画面・出力に表示されること
    ② ステップ2 の IEF403I が画面・出力に表示されること
    ③ ステップ3 の ACTIVE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 変更前の確認 START02 {#c24-i0233}
*分類: 開始手順*  ・  難易度: 初級

変更前の確認では 開始手順 の 開始 を主操作として START02 を判定します。変更対象と非対象の境界への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START02 に残します。変更前の確認を補助する 起動完了 では ACTIVE を補助値として START02 へ保存します。主判定の変更前の確認では開始手順の 開始 から IEF403I を読み START02 へ残します。証跡照合の変更前の確認では開始手順の IEF403I と ACTIVE を START02 に保存します。記録対応の変更前の確認では開始手順の PROCNAMEとSTART RESULT の証跡へ START02 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 変更前の確認で 開始手順 の 開始 と 起動完了 を実施し PSF started task の役割を確認します。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。対象 START02 の証跡を取る方法はどれですか。

    - A. S PSFPROCを対象名なしで実行する。一覧の先頭行をSTART02の結果として記録する。
    - B. 対象START02についてS PSFPROCの応答からIEF403Iを確認する。F PSFPROC,DISPLAYは補助証跡として時刻をそろえて保存する。 ✅
    - C. 前回保存したS PSFPROCの結果を使う。今回のF PSFPROC,DISPLAYの結果と同一時点の証跡として比較する。
    - D. 保存済みのSTART02の出力を再利用する。今回のS PSFPROCとF PSFPROC,DISPLAYは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。

    正解: **B** ／ 難易度: 初級

    **解説:** 採用理由: Bは開始で IEF403I を読みPROCNAMEとSTART RESULTの主値として変更前の証跡を保存しSTART02に残します。
    動作の背景: 変更前の確認では起動完了を補助操作としPSF started taskの変更対象と非対象の境界をACTIVEと対象START02で照合します。
    各選択肢の検討: 開始と起動完了の役割を分けるとA: 先頭行はSTART02と確定できない点で変更前の確認に合いません、B: IEF403Iと補助証跡の時刻を合わせる点で開始に合います、C: 採取時刻が異なる点で開始手順に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でPSF started taskに使えません。結論として変更前の確認の開始手順で判定する対象は START02 です。
    初出用語の定義: 変更前の確認で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART02へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 変更前の確認 START02**

    - 検証目的: 開始手順のPSF started taskについて変更前の証跡を保存し、START02のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START02の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START02の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START02のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEF403I が画面・出力に表示されること
    ② ステップ2 の ACTIVE が画面・出力に表示されること
    ③ ステップ3 の PROC=PSFPROC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 変更後の確認 START03 {#c24-i0234}
*分類: 開始手順*  ・  難易度: 初級

変更後の確認では 開始手順 の 起動完了 を主操作として START03 を判定します。反映値と残存値への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START03 に残します。変更後の確認を補助する FSS定義表示 では PROC=PSFPROC を補助値として START03 へ保存します。主判定の変更後の確認では開始手順の 起動完了 から ACTIVE を読み START03 へ残します。証跡照合の変更後の確認では開始手順の ACTIVE と PROC=PSFPROC を START03 に保存します。記録対応の変更後の確認では開始手順の PROCNAMEとSTART RESULT の証跡へ START03 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 変更後の確認で 開始手順 の 起動完了 と FSS定義表示 を用い 変更結果を検証 します。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。ACTIVE で対象 START03 の PROCNAMEとSTART RESULT を再現できる記録はどれですか。

    - A. PSF started taskの停止または再定義を実施する。その後にF PSFPROC,DISPLAYでACTIVEを採取する。
    - B. 出力経路確認のClassとDestinationを確認する。その値を開始手順のSTART03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - C. $D FSS(PSF1)で周辺状態を押さえる。その後にF PSFPROC,DISPLAYでACTIVEを確認して変更結果を検証する。 ✅
    - D. $D FSS(PSF1)が成功したためF PSFPROC,DISPLAYのACTIVEも正常だと推定する。主出力は保存しない。

    正解: **C** ／ 難易度: 初級

    **解説:** 正答の根拠: Cは起動完了で ACTIVE を読みPROCNAMEとSTART RESULTの主値として変更結果を検証しSTART03に残します。
    内部の仕組み: 変更後の確認ではFSS定義表示を補助操作としPSF started taskの反映値と残存値をPROC=PSFPROCと対象START03で照合します。
    誤答を含む比較: 起動完了とFSS定義表示の役割を分けるとA: 変更前のPROCNAMEとSTART RESULTを失う点でPROCNAMEとSTART RESULTを確認できません、B: 出力経路確認の値ではACTIVEを確認できないうえに追加前提も不正な点でFSS定義表示の範囲を越えます、C: 周辺状態の後にACTIVEを確認する点で現在値を示します、D: 補助操作の成功ではACTIVEを確定できない点で変更後の確認に合いません。結論として変更後の確認の開始手順で判定する対象は START03 です。
    用語定義: 変更後の確認で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART03へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 変更後の確認 START03**

    - 検証目的: 開始手順のPSF started taskについて変更結果を検証し、START03のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START03の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START03のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START03の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACTIVE が画面・出力に表示されること
    ② ステップ2 の PROC=PSFPROC が画面・出力に表示されること
    ③ ステップ3 の IEF403I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 引継ぎ記録 START09 {#c24-i0235}
*分類: 開始手順*  ・  難易度: 中級

引継ぎ記録では 開始手順 の 起動完了 を主操作として START09 を判定します。次担当者が追跡できる証跡への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START09 に残します。引継ぎ記録を補助する FSS定義表示 では PROC=PSFPROC を補助値として START09 へ保存します。主判定の引継ぎ記録では開始手順の 起動完了 から ACTIVE を読み START09 へ残します。証跡照合の引継ぎ記録では開始手順の ACTIVE と PROC=PSFPROC を START09 に保存します。記録対応の引継ぎ記録では開始手順の PROCNAMEとSTART RESULT の証跡へ START09 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で 開始手順 の 起動完了 と FSS定義表示 を用い 再現可能な記録を作成 します。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。ACTIVE で対象 START09 の PROCNAMEとSTART RESULT を再現できる記録はどれですか。

    - A. 対象名START09を指定してF PSFPROC,DISPLAYを実行する。応答中のACTIVEと時刻を保存する。$D FSS(PSF1)で周辺状態を補完する。 ✅
    - B. $D FSS(PSF1)が成功したためF PSFPROC,DISPLAYのACTIVEも正常だと推定する。主出力は保存しない。
    - C. F PSFPROC,DISPLAYを対象名なしで実行する。一覧の先頭行をSTART09の結果として記録する。
    - D. 前回保存したF PSFPROC,DISPLAYの結果を使う。今回の$D FSS(PSF1)の結果と同一時点の証跡として比較する。

    正解: **A** ／ 難易度: 中級

    **解説:** 採用操作の理由: Aは起動完了で ACTIVE を読みPROCNAMEとSTART RESULTの主値として再現可能な記録を作成しSTART09に残します。
    製品内の仕組み: 引継ぎ記録ではFSS定義表示を補助操作としPSF started taskの次担当者が追跡できる証跡をPROC=PSFPROCと対象START09で照合します。
    選択肢別の説明: 起動完了とFSS定義表示の役割を分けるとA: ACTIVEと時刻を保存する点で現在値を示します、B: 補助操作の成功ではACTIVEを確定できない点で引継ぎ記録に合いません、C: 先頭行はSTART09と確定できない点で起動完了を代替しません、D: 採取時刻が異なる点で開始手順に使いません。結論として引継ぎ記録の開始手順で判定する対象は START09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART09へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 引継ぎ記録 START09**

    - 検証目的: 開始手順のPSF started taskについて再現可能な記録を作成し、START09のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START09の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START09のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START09の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACTIVE が画面・出力に表示されること
    ② ステップ2 の PROC=PSFPROC が画面・出力に表示されること
    ③ ステップ3 の IEF403I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 復旧後の確認 START06 {#c24-i0236}
*分類: 開始手順*  ・  難易度: 中級

復旧後の確認では 開始手順 の 起動完了 を主操作として START06 を判定します。再発していないことを示す値への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START06 に残します。復旧後の確認を補助する FSS定義表示 では PROC=PSFPROC を補助値として START06 へ保存します。主判定の復旧後の確認では開始手順の 起動完了 から ACTIVE を読み START06 へ残します。証跡照合の復旧後の確認では開始手順の ACTIVE と PROC=PSFPROC を START06 に保存します。記録対応の復旧後の確認では開始手順の PROCNAMEとSTART RESULT の証跡へ START06 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で 開始手順 の 起動完了 と FSS定義表示 の役割を分け 再発していないことを示す値 を調べます。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。対象 START06 を誤判定しない進め方はどれですか。

    - A. 開始手順のPROCNAMEとSTART RESULTを確認する。その値を開始手順のSTART06にも適用する。
    - B. F PSFPROC,DISPLAYでACTIVEを取得してからS PSFPROCでIEF403Iを照合する。START06のPROCNAMEとSTART RESULTを両出力から確定する。 ✅
    - C. $D FSS(PSF1)が成功したためF PSFPROC,DISPLAYのACTIVEも正常だと推定する。主出力は保存しない。別資源で得た状態を対象START06へ引き継げるものとする。PSF started taskの再発していないことを示す値は確認済みとして扱う。さらにS PSFPROCのIEF403IをACTIVEと同種の値として併記する。
    - D. F PSFPROC,DISPLAYを対象名なしで実行する。一覧の先頭行をSTART06の結果として記録する。

    正解: **B** ／ 難易度: 中級

    **解説:** 正答内容: Bは起動完了で ACTIVE を読みPROCNAMEとSTART RESULTの主値として復旧後の安定性を確認しSTART06に残します。
    構成上の背景: 復旧後の確認ではFSS定義表示を補助操作としPSF started taskの再発していないことを示す値をPROC=PSFPROCと対象START06で照合します。
    候補ごとの理由: 起動完了とFSS定義表示の役割を分けるとA: 開始手順の値ではACTIVEを確認できない点でFSS定義表示の範囲を越えます、B: ACTIVEとIEF403Iを順に照合する点で現在値を示します、C: 補助操作の成功ではACTIVEを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はSTART06と確定できない点で起動完了を代替しません。結論として復旧後の確認の開始手順で判定する対象は START06 です。
    初出用語: 復旧後の確認で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART06へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 復旧後の確認 START06**

    - 検証目的: 開始手順のPSF started taskについて復旧後の安定性を確認し、START06のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START06の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START06のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START06の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACTIVE が画面・出力に表示されること
    ② ステップ2 の PROC=PSFPROC が画面・出力に表示されること
    ③ ステップ3 の IEF403I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 復旧準備 START05 {#c24-i0237}
*分類: 開始手順*  ・  難易度: 中級

復旧準備では 開始手順 の 開始 を主操作として START05 を判定します。再開前に必要な整合性への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START05 に残します。復旧準備を補助する 起動完了 では ACTIVE を補助値として START05 へ保存します。主判定の復旧準備では開始手順の 開始 から IEF403I を読み START05 へ残します。証跡照合の復旧準備では開始手順の IEF403I と ACTIVE を START05 に保存します。記録対応の復旧準備では開始手順の PROCNAMEとSTART RESULT の証跡へ START05 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 復旧準備で 開始手順 の 開始 と 起動完了 を組み合わせる際は PSF started task がJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用という仕組みを前提にします。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。IEF403I と PROCNAMEとSTART RESULT を対象 START05 で確認する組合せはどれですか。

    - A. 変更を加えずS PSFPROCを実行する。IEF403Iを保存する。差分はF PSFPROC,DISPLAYの結果と対象名で対応させる。 ✅
    - B. 前回保存したS PSFPROCの結果を使う。今回のF PSFPROC,DISPLAYの結果と同一時点の証跡として比較する。
    - C. 保存済みのSTART05の出力を再利用する。今回のS PSFPROCとF PSFPROC,DISPLAYは実行済みとして扱う。
    - D. F PSFPROC,DISPLAYのACTIVEをPROCNAMEとSTART RESULTの主判定に採用する。S PSFPROCの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **A** ／ 難易度: 中級

    **解説:** 選定理由: Aは開始で IEF403I を読みPROCNAMEとSTART RESULTの主値として復旧条件を確認しSTART05に残します。
    処理の仕組み: 復旧準備では起動完了を補助操作としPSF started taskの再開前に必要な整合性をACTIVEと対象START05で照合します。
    選択結果の内訳: 開始と起動完了の役割を分けるとA: 変更前のIEF403Iを保存する点で開始に合います、B: 採取時刻が異なる点で開始手順に使いません、C: 過去出力では今回の復旧準備を示せない点でPSF started taskに使えません、D: ACTIVEはIEF403Iを代替しないうえに追加前提も不正な点でSTART05を採用できません。結論として復旧準備の開始手順で判定する対象は START05 です。
    用語の説明: 復旧準備で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART05へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 復旧準備 START05**

    - 検証目的: 開始手順のPSF started taskについて復旧条件を確認し、START05のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START05の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START05の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START05のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEF403I が画面・出力に表示されること
    ② ステップ2 の ACTIVE が画面・出力に表示されること
    ③ ステップ3 の PROC=PSFPROC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 構成監査 START08 {#c24-i0238}
*分類: 開始手順*  ・  難易度: 中級

構成監査では 開始手順 の 開始 を主操作として START08 を判定します。定義値と稼働値の一致への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START08 に残します。構成監査を補助する 起動完了 では ACTIVE を補助値として START08 へ保存します。主判定の構成監査では開始手順の 開始 から IEF403I を読み START08 へ残します。証跡照合の構成監査では開始手順の IEF403I と ACTIVE を START08 に保存します。記録対応の構成監査では開始手順の PROCNAMEとSTART RESULT の証跡へ START08 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 構成監査で 開始手順 の 開始 と 起動完了 を実施し PSF started task の役割を確認します。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。対象 START08 の証跡を取る方法はどれですか。

    - A. 保存済みのSTART08の出力を再利用する。今回のS PSFPROCとF PSFPROC,DISPLAYは実行済みとして扱う。
    - B. F PSFPROC,DISPLAYのACTIVEをPROCNAMEとSTART RESULTの主判定に採用する。S PSFPROCの応答は採取対象から外す。
    - C. $D FSS(PSF1)のPROC=PSFPROCをIEF403Iと同義の成功表示として扱う。S PSFPROCは実行しない。
    - D. F PSFPROC,DISPLAYの結果だけでは確定しない。S PSFPROCのIEF403Iを主証跡として構成差分を監査する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 技術上の正答: Dは開始で IEF403I を読みPROCNAMEとSTART RESULTの主値として構成差分を監査しSTART08に残します。
    実行時の背景: 構成監査では起動完了を補助操作としPSF started taskの定義値と稼働値の一致をACTIVEと対象START08で照合します。
    四つの候補の理由: 開始と起動完了の役割を分けるとA: 過去出力では今回の構成監査を示せない点で開始手順に使いません、B: ACTIVEはIEF403Iを代替しない点でPSF started taskに使えません、C: PROC=PSFPROCとIEF403Iは確認項目が異なる点でSTART08を採用できません、D: IEF403Iを主証跡として区別する点で主証跡になります。結論として構成監査の開始手順で判定する対象は START08 です。
    初出語定義: 構成監査で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART08へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 構成監査 START08**

    - 検証目的: 開始手順のPSF started taskについて構成差分を監査し、START08のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START08の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START08の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START08のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEF403I が画面・出力に表示されること
    ② ステップ2 の ACTIVE が画面・出力に表示されること
    ③ ステップ3 の PROC=PSFPROC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 通常状態の確認 START01 {#c24-i0239}
*分類: 開始手順*  ・  難易度: 初級

通常状態の確認では 開始手順 の FSS定義表示 を主操作として START01 を判定します。基準値と現在値の差への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START01 に残します。通常状態の確認を補助する 開始 では IEF403I を補助値として START01 へ保存します。主判定の通常状態の確認では開始手順の FSS定義表示 から PROC=PSFPROC を読み START01 へ残します。証跡照合の通常状態の確認では開始手順の PROC=PSFPROC と IEF403I を START01 に保存します。記録対応の通常状態の確認では開始手順の PROCNAMEとSTART RESULT の証跡へ START01 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 開始手順 の FSS定義表示 と 開始 を使い 通常状態を確定 します。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。PROC=PSFPROC を読み対象 START01 を切り分ける確認方法はどれですか。

    - A. $D FSS(PSF1)を先に実行する。対象START01のPROC=PSFPROCをPROCNAMEとSTART RESULTとして記録する。続いてS PSFPROCで同一対象を照合する。 ✅
    - B. S PSFPROCのIEF403IをPROCNAMEとSTART RESULTの主判定に採用する。$D FSS(PSF1)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。PSF started taskの基準値と現在値の差は確認済みとして扱う。さらにF PSFPROC,DISPLAYのACTIVEをPROC=PSFPROCと同種の値として併記する。
    - C. F PSFPROC,DISPLAYのACTIVEをPROC=PSFPROCと同義の成功表示として扱う。$D FSS(PSF1)は実行しない。
    - D. $D FSS(PSF1)が応答を返した時点で正常とする。応答中のPROC=PSFPROCの値は記録しない。

    正解: **A** ／ 難易度: 初級

    **解説:** 正解の説明: AはFSS定義表示で PROC=PSFPROC を読みPROCNAMEとSTART RESULTの主値として通常状態を確定しSTART01に残します。
    背景・仕組み: 通常状態の確認では開始を補助操作としPSF started taskの基準値と現在値の差をIEF403Iと対象START01で照合します。
    選択肢の理由: FSS定義表示と開始の役割を分けるとA: PROC=PSFPROCを主値として補助結果と照合する点で正答です、B: IEF403IはPROC=PSFPROCを代替しないうえに追加前提も不正な点でSTART01を採用できません、C: ACTIVEとPROC=PSFPROCは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではPROCNAMEとSTART RESULTを判定できない点で一次資料と一致しません。結論として通常状態の確認の開始手順で判定する対象は START01 です。
    用語の初出定義: 通常状態の確認で使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART01へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 通常状態の確認 START01**

    - 検証目的: 開始手順のPSF started taskについて通常状態を確定し、START01のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START01のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START01の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START01の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROC=PSFPROC が画面・出力に表示されること
    ② ステップ2 の IEF403I が画面・出力に表示されること
    ③ ステップ3 の ACTIVE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes



### 開始手順 PSF started task 障害切り分け START04 {#c24-i0240}
*分類: 開始手順*  ・  難易度: 初級

障害切り分けでは 開始手順 の FSS定義表示 を主操作として START04 を判定します。最初に失敗した処理への注意として「FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります」を START04 に残します。障害切り分けを補助する 開始 では IEF403I を補助値として START04 へ保存します。主判定の障害切り分けでは開始手順の FSS定義表示 から PROC=PSFPROC を読み START04 へ残します。証跡照合の障害切り分けでは開始手順の PROC=PSFPROC と IEF403I を START04 に保存します。記録対応の障害切り分けでは開始手順の PROCNAMEとSTART RESULT の証跡へ START04 を結びます。

**出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 開始手順 の FSS定義表示 と 開始 を照合し 最初に失敗した処理 を確かめます。PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用です。FSSDEFのPROC名と実際の開始タスク名を取り違える危険があります。PROC=PSFPROC を読む前に対象 START04 へ行う確認はどれですか。

    - A. F PSFPROC,DISPLAYのACTIVEをPROC=PSFPROCと同義の成功表示として扱う。$D FSS(PSF1)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. $D FSS(PSF1)が応答を返した時点で正常とする。応答中のPROC=PSFPROCの値は記録しない。
    - C. $D FSS(PSF1)のコマンド文字列だけを記録する。PROC=PSFPROCを含む応答行は保存しない。
    - D. $D FSS(PSF1)の出力でSTART04とPROC=PSFPROCが同じ応答にあることを確認する。PROCNAMEとSTART RESULTをその応答から採取する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 正しい操作の説明: DはFSS定義表示で PROC=PSFPROC を読みPROCNAMEとSTART RESULTの主値として障害範囲を限定しSTART04に残します。
    技術的背景: 障害切り分けでは開始を補助操作としPSF started taskの最初に失敗した処理をIEF403Iと対象START04で照合します。
    四択の評価: FSS定義表示と開始の役割を分けるとA: ACTIVEとPROC=PSFPROCは確認項目が異なるうえに追加前提も不正な点でSTART04を採用できません、B: 応答の有無だけではPROCNAMEとSTART RESULTを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではPROCNAMEとSTART RESULTを証明できない点で一次資料と一致しません、D: START04とPROC=PSFPROCを同じ応答で結ぶ点でSTART04を判定できます。結論として障害切り分けの開始手順で判定する対象は START04 です。
    初出語の意味: 障害切り分けで使う PSF started task はJESのFSSDEFとPSF開始プロシージャーを対応させ、FSSおよびFSAを起動する運用を表しPROCNAMEとSTART RESULTを判定する際にSTART04へ適用します。

    **出典:** apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


??? note "検証手順（1件）"
    **開始手順 PSF started task 障害切り分け START04**

    - 検証目的: 開始手順のPSF started taskについて障害範囲を限定し、START04のPROCNAMEとSTART RESULTを実出力で確認する。
    - 前提条件: PSF for z/OS 4.7の参照権限を持ち、対象START04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PSF for z/OS 4.7の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へ$D FSS(PSF1)を指定し、START04のFSS定義表示を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> $D FSS(PSF1)
    → Enter を押す
    ```

    画面・出力:
    ```text
    $HASP879 FSS(PSF1) PROC=PSFPROC STATUS=INACTIVE SYSTEM=SYSA
    ```

    画面・出力にあるPROC=PSFPROCを読み、PROCNAMEとSTART RESULTと対象START04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へS PSFPROCを指定し、START04の開始を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> S PSFPROC
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I PSFPROC - STARTED - TIME=14.40.00
    ```

    画面・出力にあるIEF403Iを読み、PROCNAMEとSTART RESULTと対象START04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPSF for z/OS 4.7の開始手順を確認する入力画面です。COMMAND入力口へF PSFPROC,DISPLAYを指定し、START04の起動完了を表示します。
    操作（入力）:
    ```text
    PSF for z/OS 4.7 操作画面
    COMMAND ===> F PSFPROC,DISPLAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    APS100I PSFPROC DISPLAY FSS STATUS ACTIVE FSA COUNT 4
    ```

    画面・出力にあるACTIVEを読み、PROCNAMEとSTART RESULTと対象START04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の PROC=PSFPROC が画面・出力に表示されること
    ② ステップ2 の IEF403I が画面・出力に表示されること
    ③ ステップ3 の ACTIVE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: apss000_v4r7 / apsu000_v4r7 / apsd000_v4r7 / apsp000_v4r7 / psf_v4r7_messages_and_codes


