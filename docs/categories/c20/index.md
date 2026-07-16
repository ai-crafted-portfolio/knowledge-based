# JCL PROC / 制御

<div class="kb-cov" markdown>

**技術項目 181 件**  ／  QA対応 181（100.0%・不足 0）  ／  手順対応 178（98.34%・不足 3）

</div>

このカテゴリでは技術項目 181 件を掲載し、確認問題 313 問・検証手順 216 件を項目ごとに紐づけています。対応率は技術項目に明示的に対応付けられた件数で算出しています（増補継続中）。


> 最終更新: 2026-07-16


## 収録項目


### /*JOBPARM

- [/*JOBPARM 文 役割](part-01.md#c20-i0001)

### /*JOBPARM サブ

- [BYTES/CARDS/LINES/PAGES=n](part-01.md#c20-i0002)
- [COPIES=n](part-01.md#c20-i0003)
- [PROCLIB=ddname](part-01.md#c20-i0004)
- [SYSAFF=sysname](part-01.md#c20-i0005)
- [TIME=mm](part-01.md#c20-i0006)

### /*MESSAGE

- [/*MESSAGE 文 役割](part-01.md#c20-i0007)
- [/*MESSAGE 書式](part-01.md#c20-i0008)

### /*OUTPUT

- [/*OUTPUT と //OUTPUT JES2](part-01.md#c20-i0009)
- [/*OUTPUT 文 役割](part-01.md#c20-i0010)
- [/*OUTPUT 書式](part-01.md#c20-i0011)

### /*PRIORITY

- [/*PRIORITY と JOB PRTY](part-01.md#c20-i0012)
- [/*PRIORITY 文 役割](part-01.md#c20-i0013)

### /*ROUTE

- [/*ROUTE PRINT](part-01.md#c20-i0014)
- [/*ROUTE PRINT 書式](part-01.md#c20-i0015)
- [/*ROUTE PUNCH](part-01.md#c20-i0016)
- [/*ROUTE XEQ](part-01.md#c20-i0017)

### /*XMIT

- [/*XMIT と DLM=](part-01.md#c20-i0018)
- [/*XMIT 文 役割](part-01.md#c20-i0019)
- [/*XMIT 書式](part-01.md#c20-i0020)
- [/*XMIT 終端](part-01.md#c20-i0021)

### COND EVEN

- [COND=EVEN の意味](part-01.md#c20-i0022)
- [EVEN と JCL エラー](part-01.md#c20-i0023)
- [EVEN と RC 条件併用](part-01.md#c20-i0024)
- [EVEN とシステム ABEND](part-01.md#c20-i0025)

### COND ONLY

- [COND=ONLY の意味](part-01.md#c20-i0026)
- [ONLY と JCL エラー](part-01.md#c20-i0027)
- [ONLY と RC 条件併用](part-01.md#c20-i0028)

### COND 前ステップ参照

- [COND 複数条件 OR](part-01.md#c20-i0029)
- [COND=(code,oper,stepname)](part-01.md#c20-i0030)
- [COND=(code,oper,stepname.procstep)](part-01.md#c20-i0031)
- [JOB COND との優先](part-01.md#c20-i0032)
- [未実行ステップの参照](part-01.md#c20-i0033)

### COND 演算子

- [COND oper=EQ](part-01.md#c20-i0034)
- [COND oper=GE](part-01.md#c20-i0035)
- [COND oper=GT](part-01.md#c20-i0036)
- [COND oper=LE](part-01.md#c20-i0037)
- [COND oper=LT](part-01.md#c20-i0038)
- [COND oper=NE](part-01.md#c20-i0039)
- [COND の真偽逆ロジック](part-01.md#c20-i0040)
- [COND 値 code の範囲](part-01.md#c20-i0041)

### DD override DCB

- [DCB サブパラの個別上書き](part-01.md#c20-i0042)
- [DCB 全体置換](part-01.md#c20-i0043)
- [DISP オーバライド](part-01.md#c20-i0044)
- [SPACE オーバライド](part-01.md#c20-i0045)
- [VOL オーバライド](part-01.md#c20-i0046)

### DD override 削除

- [DD 削除の書式](part-01.md#c20-i0047)
- [完全削除の代替](part-01.md#c20-i0048)

### DD override 基本

- [DD オーバライドの書式](part-01.md#c20-i0049)
- [ddname の意味](part-01.md#c20-i0050)
- [stepname の意味](part-01.md#c20-i0051)
- [オーバライドと連結](part-01.md#c20-i0052)
- [オーバライド配置順](part-01.md#c20-i0053)
- [オーバライド順違反](part-01.md#c20-i0054)
- [未定義 DD 名指定](part-01.md#c20-i0055)

### DD override 追加

- [DD 追加の書式](part-01.md#c20-i0056)
- [追加 DD と STEPLIB](part-01.md#c20-i0057)
- [追加 DD の配置](part-01.md#c20-i0058)

### EXPORT 文

- [EXPORT と JES2 シンボル](part-01.md#c20-i0059)
- [EXPORT と PROC](part-01.md#c20-i0060)
- [EXPORT のスコープ](part-01.md#c20-i0061)
- [EXPORT 文の役割](part-01.md#c20-i0062)
- [EXPORT 書式](part-01.md#c20-i0063)
- [SYMLIST=* の意味](part-01.md#c20-i0064)

### IF ABEND

- [ABEND と JCL エラー区別](part-01.md#c20-i0065)
- [IF ABEND THEN](part-01.md#c20-i0066)
- [IF ¬ABEND THEN](part-01.md#c20-i0067)
- [stepname.ABEND 参照](part-01.md#c20-i0068)
- [stepname.procstep.ABEND](part-01.md#c20-i0069)

### IF ABENDCC

- [ABENDCC と ABEND 併用](part-01.md#c20-i0070)
- [ABENDCC 形式](part-01.md#c20-i0071)
- [IF ABENDCC=Sxxx](part-01.md#c20-i0072)
- [IF ABENDCC=Uxxxx](part-01.md#c20-i0073)
- [stepname.ABENDCC 参照](part-01.md#c20-i0074)

### IF RC 参照

- [&MAXCC / &LASTCC (互換)](part-01.md#c20-i0075)
- [&MAXRC キーワード](part-01.md#c20-i0076)
- [&RC キーワード](part-01.md#c20-i0077)
- [stepname.RC](part-01.md#c20-i0078)
- [stepname.RUN](part-01.md#c20-i0079)
- [stepname.procstep.RC](part-01.md#c20-i0080)
- [未実行ステップの RC](part-01.md#c20-i0081)

### IF 関係式

- [関係演算子 EQ/=](part-01.md#c20-i0082)
- [関係演算子 GE/>=](part-01.md#c20-i0083)
- [関係演算子 GT/>](part-01.md#c20-i0084)
- [関係演算子 LE/<=](part-01.md#c20-i0085)
- [関係演算子 LT/<](part-01.md#c20-i0086)
- [関係演算子 NE/¬=/^=](part-01.md#c20-i0087)

### IF/THEN/ELSE 基本

- [ELSE 文](part-01.md#c20-i0088)
- [ENDIF 文](part-01.md#c20-i0089)
- [IF 文の書式](part-01.md#c20-i0090)
- [ネスト深さ上限](part-01.md#c20-i0091)
- [括弧によるグループ化](part-01.md#c20-i0092)
- [論理 AND (&)](part-01.md#c20-i0093)
- [論理 NOT (¬/^)](part-01.md#c20-i0094)
- [論理 OR (|)](part-01.md#c20-i0095)

### INCLUDE 文

- [INCLUDE と PROC の違い](part-01.md#c20-i0096)
- [INCLUDE とシンボル](part-01.md#c20-i0097)
- [INCLUDE のネスト](part-01.md#c20-i0098)
- [INCLUDE 内容](part-01.md#c20-i0099)
- [INCLUDE 取込先](part-01.md#c20-i0100)
- [INCLUDE 文の役割](part-01.md#c20-i0101)
- [INCLUDE 書式](part-01.md#c20-i0102)

### JCLLIB 文

- [1 ジョブ 1 JCLLIB](part-01.md#c20-i0103)
- [JCLLIB と PRIVATE PROCLIB](part-01.md#c20-i0104)
- [JCLLIB の位置](part-01.md#c20-i0105)
- [JCLLIB ライブラリ数](part-01.md#c20-i0106)
- [JCLLIB 文の役割](part-01.md#c20-i0107)
- [JCLLIB 書式](part-01.md#c20-i0108)
- [ORDER= の意味](part-01.md#c20-i0109)

### PEND 文

- [PEND 文の位置](part-01.md#c20-i0110)
- [PEND 文の役割](part-01.md#c20-i0111)
- [PEND 文の書式](part-01.md#c20-i0112)
- [PEND 省略時のエラー](part-01.md#c20-i0113)
- [カタログ PROC と PEND](part-01.md#c20-i0114)

### PROC ネスト

- [ネスト DD オーバライドの順](part-01.md#c20-i0115)
- [ネスト プロシジャの定義](part-01.md#c20-i0116)
- [ネストとシンボル スコープ](part-01.md#c20-i0117)
- [ネスト循環参照](part-01.md#c20-i0118)
- [ネスト時の RC 参照](part-01.md#c20-i0119)
- [ネスト時のステップ名表記](part-01.md#c20-i0120)
- [ネスト深さ制限](part-01.md#c20-i0121)

### PROC 文 構文

- [PROC 文 オペランド省略](part-01.md#c20-i0122)
- [PROC 文 継続行](part-01.md#c20-i0123)
- [PROC 文の位置 (インストリーム)](part-01.md#c20-i0124)
- [PROC 文の位置 (カタログ)](part-01.md#c20-i0125)
- [PROC 文の役割](part-01.md#c20-i0126)
- [PROC 文の書式](part-01.md#c20-i0127)
- [pname (プロシジャ名)](part-01.md#c20-i0128)
- [カタログ PROC の pname](part-01.md#c20-i0129)

### PROC 種別

- [インストリーム PROC の利点](part-01.md#c20-i0130)
- [インストリーム PROC の最大数](part-01.md#c20-i0131)
- [インストリーム vs カタログ 検索順](part-01.md#c20-i0132)
- [インストリーム プロシジャ定義](part-01.md#c20-i0133)
- [カタログ PROC の利点](part-01.md#c20-i0134)
- [カタログ プロシジャ定義](part-01.md#c20-i0135)
- [標準 PROCLIB 連結](part-01.md#c20-i0136)

### SET 文

- [SET と PROC デフォルトの優先](part-01.md#c20-i0137)
- [SET と再帰参照](part-01.md#c20-i0138)
- [SET と空値](part-01.md#c20-i0139)
- [SET の位置](part-01.md#c20-i0140)
- [SET 文の役割](part-01.md#c20-i0141)
- [SET 書式](part-01.md#c20-i0142)
- [複数 SET 文](part-01.md#c20-i0143)

### シンボリック override

- [EXEC でのオーバライド](part-01.md#c20-i0144)
- [PROC ネスト時のオーバライド](part-01.md#c20-i0145)
- [PROC= 省略時の書き方](part-01.md#c20-i0146)
- [オーバライド 値の空指定](part-01.md#c20-i0147)
- [オーバライド未定義シンボル](part-01.md#c20-i0148)
- [オーバライド評価順](part-01.md#c20-i0149)

### シンボリック スコープ

- [EXPORT による昇格](part-01.md#c20-i0150)
- [JOB 文 シンボル参照不可](part-01.md#c20-i0151)
- [システム シンボル](part-01.md#c20-i0152)
- [ジョブ レベル SET 文](part-01.md#c20-i0153)
- [ネスト PROC へのスコープ](part-01.md#c20-i0154)
- [プロシジャ内ローカル](part-01.md#c20-i0155)

### シンボリック 参照

- [&& とアンパサンド本来文字](part-01.md#c20-i0156)
- [シンボリック 未定義参照](part-01.md#c20-i0157)
- [シンボリック参照位置](part-01.md#c20-i0158)
- [シンボリック評価タイミング](part-01.md#c20-i0159)
- [ピリオド付き参照 &sym.X](part-01.md#c20-i0160)
- [ピリオド自体を残す書き方](part-01.md#c20-i0161)

### シンボリック 命名

- [システム シンボル &SYSNAME](part-01.md#c20-i0162)
- [システム シンボル &SYSPLEX](part-01.md#c20-i0163)
- [システム シンボル &SYSUID](part-01.md#c20-i0164)
- [システム シンボル &YYMMDD/&LYYMMDD](part-01.md#c20-i0165)
- [入れ子参照](part-01.md#c20-i0166)
- [入れ子参照の上限](part-01.md#c20-i0167)
- [名前付きシンボリック](part-01.md#c20-i0168)

### シンボリック 定義

- [シンボリック 先頭文字](part-01.md#c20-i0169)
- [シンボリック表記法](part-01.md#c20-i0170)
- [デフォルト値 アポストロフィ](part-01.md#c20-i0171)
- [デフォルト値 最大長](part-01.md#c20-i0172)
- [デフォルト値 空指定](part-01.md#c20-i0173)
- [デフォルト値の指定](part-01.md#c20-i0174)
- [予約名の回避](part-01.md#c20-i0175)

### 区切りカード

- [/* の位置](part-01.md#c20-i0176)
- [/* 区切りカードの役割](part-01.md#c20-i0177)
- [// と コメント //*](part-01.md#c20-i0178)
- [// 単独カード](part-01.md#c20-i0179)
- [DLM= による代替](part-01.md#c20-i0180)
- [EOF と区切りカード](part-01.md#c20-i0181)

### その他

- [その他](part-02.md#c20-other)