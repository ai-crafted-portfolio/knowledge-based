# JCL EXEC 文

<div class="kb-cov" markdown>

**技術項目 142 件**  ／  QA対応 96（67.61%・不足 46）  ／  手順対応 142（100.0%・不足 0）

</div>

このカテゴリでは技術項目 142 件を掲載し、確認問題 124 問・検証手順 105 件を項目ごとに紐づけています。対応率は技術項目に明示的に対応付けられた件数で算出しています（増補継続中）。


> 最終更新: 2026-07-16


## 収録項目


### ACCT

- [ACCT と JOB アカウント情報](part-01.md#c18-i0001)
- [ACCT の用途](part-01.md#c18-i0002)
- [ACCT 最大長](part-01.md#c18-i0003)
- [ACCT=(info1,info2,…)](part-01.md#c18-i0004)
- [ACCT=info](part-01.md#c18-i0005)

### ADDRSPC

- [ADDRSPC と JOB ADDRSPC](part-01.md#c18-i0006)
- [ADDRSPC=REAL](part-01.md#c18-i0007)
- [ADDRSPC=REAL と REGION](part-01.md#c18-i0008)
- [ADDRSPC=REAL の制約](part-01.md#c18-i0009)
- [ADDRSPC=VIRT](part-01.md#c18-i0010)

### COND 基本

- [COND と RC=0 既定](part-01.md#c18-i0011)
- [COND の目的](part-01.md#c18-i0012)
- [COND の複数条件](part-01.md#c18-i0013)
- [COND=(code,oper)](part-01.md#c18-i0014)
- [COND=(code,oper,stepname)](part-01.md#c18-i0015)
- [COND=(code,oper,stepname.procstep)](part-01.md#c18-i0016)

### COND 拡張

- [COND と IF/THEN の使い分け](part-01.md#c18-i0017)
- [COND=EVEN](part-01.md#c18-i0018)
- [COND=ONLY](part-01.md#c18-i0019)
- [COND=ONLY と JCL エラー](part-01.md#c18-i0020)
- [EVEN と RC 条件の併用](part-01.md#c18-i0021)
- [JOB 文 COND との関係](part-01.md#c18-i0022)
- [ONLY と RC 条件の併用](part-01.md#c18-i0023)

### COND 演算子

- [COND oper=EQ (=)](part-01.md#c18-i0024)
- [COND oper=GE (≥)](part-01.md#c18-i0025)
- [COND oper=GT (>)](part-01.md#c18-i0026)
- [COND oper=LE (≤)](part-01.md#c18-i0027)
- [COND oper=LT (<)](part-01.md#c18-i0028)
- [COND oper=NE (≠)](part-01.md#c18-i0029)
- [演算子の論理](part-01.md#c18-i0030)

### DYNAMNBR

- [DYNAMNBR と TSO/E](part-01.md#c18-i0031)
- [DYNAMNBR の用途](part-01.md#c18-i0032)
- [DYNAMNBR 既定値](part-01.md#c18-i0033)
- [DYNAMNBR 過剰指定](part-01.md#c18-i0034)
- [DYNAMNBR=n](part-01.md#c18-i0035)

### EXEC 文 基本

- [EXEC 文の必須要素](part-01.md#c18-i0036)
- [EXEC 文の構文位置](part-01.md#c18-i0037)
- [オペランド区切り](part-01.md#c18-i0038)
- [コメント記入位置](part-01.md#c18-i0039)
- [ステップ名 (省略可)](part-01.md#c18-i0040)
- [ステップ名 先頭文字](part-01.md#c18-i0041)
- [ステップ名 文字数](part-01.md#c18-i0042)
- [ステップ名 省略時の挙動](part-01.md#c18-i0043)
- [ステップ名 重複禁止](part-01.md#c18-i0044)
- [継続行](part-01.md#c18-i0045)

### IF/THEN/ELSE

- [&LASTRC キーワード](part-01.md#c18-i0046)
- [&MAXRC キーワード](part-01.md#c18-i0047)
- [&RC キーワード](part-01.md#c18-i0048)
- [ABEND の論理値](part-01.md#c18-i0049)
- [ELSE 句](part-01.md#c18-i0050)
- [ENDIF 必須](part-01.md#c18-i0051)
- [IF と COND の併用注意](part-01.md#c18-i0052)
- [IF/THEN の基本](part-01.md#c18-i0053)
- [JCL エラー時の挙動](part-01.md#c18-i0054)
- [RUN/ABEND/ABENDCC の組合せ](part-01.md#c18-i0055)
- [stepname.ABEND キーワード](part-01.md#c18-i0056)
- [stepname.ABENDCC キーワード](part-01.md#c18-i0057)
- [stepname.RC 参照](part-01.md#c18-i0058)
- [stepname.RUN キーワード](part-01.md#c18-i0059)
- [stepname.procstep.RC 参照](part-01.md#c18-i0060)
- [¬ABEND の使い方](part-01.md#c18-i0061)
- [ネスト深さ](part-01.md#c18-i0062)
- [ラベル名 制限](part-01.md#c18-i0063)
- [括弧によるグループ化](part-01.md#c18-i0064)
- [比較演算子 EQ/=](part-01.md#c18-i0065)
- [比較演算子 GE/>=](part-01.md#c18-i0066)
- [比較演算子 GT/>](part-01.md#c18-i0067)
- [比較演算子 LE/<=](part-01.md#c18-i0068)
- [比較演算子 LT/<](part-01.md#c18-i0069)
- [比較演算子 NE/¬= /^=](part-01.md#c18-i0070)
- [論理 AND (&)](part-01.md#c18-i0071)
- [論理 NOT (¬/^)](part-01.md#c18-i0072)
- [論理 OR (|)](part-01.md#c18-i0073)

### PARM=

- [PARM= の用途](part-01.md#c18-i0074)

### PARM= 内容

- [PARM= 全角/DBCS の扱い](part-01.md#c18-i0075)
- [PARM= 受取側 (ASM)](part-01.md#c18-i0076)
- [PARM= 受取側 (COBOL)](part-01.md#c18-i0077)
- [PARM= 最大長 100 バイト](part-01.md#c18-i0078)
- [PARM= 継続記述](part-01.md#c18-i0079)
- [アポストロフィのエスケープ](part-01.md#c18-i0080)
- [アンパサンドのエスケープ](part-01.md#c18-i0081)
- [プロシジャ ステップ単位上書き](part-01.md#c18-i0082)
- [プロシジャ側 PARM 上書き](part-01.md#c18-i0083)
- [空 PARM 指定](part-01.md#c18-i0084)

### PARM= 形式

- [PARM='value with spaces'](part-01.md#c18-i0085)
- [PARM=(sub1,'sub 2',sub3)](part-01.md#c18-i0086)
- [PARM=(sub1,sub2,…)](part-01.md#c18-i0087)
- [PARM=value (単純文字列)](part-01.md#c18-i0088)

### PERFORM

- [PERFORM と JOB PERFORM](part-01.md#c18-i0089)
- [PERFORM と WLM 互換モード](part-01.md#c18-i0090)
- [PERFORM の用途](part-01.md#c18-i0091)
- [PERFORM=n](part-01.md#c18-i0092)

### PGM= 形式

- [EXEC PGM=*.procstep.ddname](part-01.md#c18-i0093)
- [EXEC PGM=*.stepname.ddname](part-01.md#c18-i0094)
- [EXEC PGM=progname](part-01.md#c18-i0095)
- [PGM= と JOBLIB の優先順](part-01.md#c18-i0096)
- [PGM= と LNKLST](part-01.md#c18-i0097)
- [PGM= と STEPLIB 連結](part-01.md#c18-i0098)
- [PGM=IEBGENER 等システムユーティリティ](part-01.md#c18-i0099)
- [PGM=IEFBR14](part-01.md#c18-i0100)
- [progname 文字数](part-01.md#c18-i0101)

### PROC= 形式

- [EXEC PROC=procname](part-01.md#c18-i0102)
- [EXEC procname (PROC= 省略)](part-01.md#c18-i0103)
- [JCLLIB との併用](part-01.md#c18-i0104)
- [PGM= と PROC= の排他](part-01.md#c18-i0105)
- [procname 文字数](part-01.md#c18-i0106)
- [インストリーム プロシジャ](part-01.md#c18-i0107)
- [カタログ式プロシジャ](part-01.md#c18-i0108)
- [プロシジャ シンボルパラメータ](part-01.md#c18-i0109)

### REGION (STEP)

- [REGION と 16M 境界](part-01.md#c18-i0110)
- [REGION と MEMLIMIT の関係](part-01.md#c18-i0111)
- [REGION の目的](part-01.md#c18-i0112)
- [REGION 既定値](part-01.md#c18-i0113)
- [REGION=0K / 0M](part-01.md#c18-i0114)
- [REGION=0M とアドレス空間](part-01.md#c18-i0115)
- [REGION=nK](part-01.md#c18-i0116)
- [REGION=nM](part-01.md#c18-i0117)
- [REGIONX (上下境界指定)](part-01.md#c18-i0118)
- [ステップ REGION と JOB REGION](part-01.md#c18-i0119)

### TIME (STEP)

- [S322 ABEND](part-01.md#c18-i0120)
- [TIME と JOB TIME の優先](part-01.md#c18-i0121)
- [TIME 既定値](part-01.md#c18-i0122)
- [TIME 範囲](part-01.md#c18-i0123)
- [TIME=(,seconds)](part-01.md#c18-i0124)
- [TIME=(minutes,seconds)](part-01.md#c18-i0125)
- [TIME=0](part-01.md#c18-i0126)
- [TIME=1440](part-01.md#c18-i0127)
- [TIME=MAXIMUM](part-01.md#c18-i0128)
- [TIME=NOLIMIT](part-01.md#c18-i0129)
- [TIME=minutes](part-01.md#c18-i0130)

### その他オペランド

- [DPRTY=(value1,value2)](part-01.md#c18-i0131)
- [MEMLIMIT (DD JOBLIB ではなく)](part-01.md#c18-i0132)
- [PROCESS=](part-01.md#c18-i0133)
- [RD (再始動定義)](part-01.md#c18-i0134)

### 後方参照

- [*.stepname.ddname 形式](part-01.md#c18-i0135)
- [*.stepname.procstep.ddname 形式](part-01.md#c18-i0136)
- [COND での *.stepname 参照](part-01.md#c18-i0137)
- [EXEC PGM=*.s.d](part-01.md#c18-i0138)
- [後方参照と RESTART](part-01.md#c18-i0139)
- [後方参照とプロシジャ](part-01.md#c18-i0140)
- [後方参照と未実行ステップ](part-01.md#c18-i0141)
- [後方参照の有効範囲](part-01.md#c18-i0142)

### その他

- [その他](part-01.md#c18-other)