---
search:
  exclude: true
---

# PSF for z/OS 4.7 — 詳細 (3/3)

[← PSF for z/OS 4.7 の概要へ戻る](index.md)


## PSF for z/OS 4.7 > 開始手順

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


