# JCL JOB 文

<div class="kb-cov" markdown>

**技術項目 162 件**  ／  QA対応 162（100.0%・不足 0）  ／  手順対応 159（98.15%・不足 3）

</div>

このカテゴリでは技術項目 162 件を掲載し、確認問題 402 問・検証手順 197 件を項目ごとに紐づけています。対応率は技術項目に明示的に対応付けられた件数で算出しています（増補継続中）。


> 最終更新: 2026-07-16


## 収録項目


### JOB 文 ABEND

- [JCL ERROR JCL015](part-01.md#c19-i0001)
- [S322 — CPU 時間超過](part-01.md#c19-i0002)
- [S722 — 出力上限超過](part-01.md#c19-i0003)
- [S822 — 領域不足](part-01.md#c19-i0004)

### JOB 文 ADDRSPC

- [ADDRSPC=REAL](part-01.md#c19-i0005)
- [ADDRSPC=REAL と REGION 解釈](part-01.md#c19-i0006)
- [ADDRSPC=REAL の用途](part-01.md#c19-i0007)
- [ADDRSPC=VIRT](part-01.md#c19-i0008)

### JOB 文 CLASS

- [CLASS と JOBCLASS イニシエータの関係](part-01.md#c19-i0009)
- [CLASS と SCHENV の関係](part-01.md#c19-i0010)
- [CLASS と TIME 上限の関係](part-01.md#c19-i0011)
- [CLASS の値域](part-01.md#c19-i0012)
- [CLASS パラメータの目的](part-01.md#c19-i0013)
- [CLASS 省略時の既定値](part-01.md#c19-i0014)

### JOB 文 COND

- [COND と IF/THEN/ELSE/ENDIF の関係](part-01.md#c19-i0015)
- [COND の解釈方向に注意](part-01.md#c19-i0016)
- [COND を IF 構造に置き換える推奨](part-01.md#c19-i0017)
- [COND パラメータの目的](part-01.md#c19-i0018)
- [COND 演算子 EQ](part-01.md#c19-i0019)
- [COND 演算子 GE](part-01.md#c19-i0020)
- [COND 演算子 GT](part-01.md#c19-i0021)
- [COND 演算子 LE](part-01.md#c19-i0022)
- [COND 演算子 LT](part-01.md#c19-i0023)
- [COND 演算子 NE](part-01.md#c19-i0024)
- [COND 複数条件 (OR 結合)](part-01.md#c19-i0025)
- [COND=(code,operator) 構文](part-01.md#c19-i0026)
- [COND=EVEN](part-01.md#c19-i0027)
- [COND=ONLY](part-01.md#c19-i0028)
- [JOB 文 COND と EXEC 文 COND の併用](part-01.md#c19-i0029)
- [JOB 文 COND の有効範囲](part-01.md#c19-i0030)

### JOB 文 GROUP

- [GROUP パラメータの目的](part-01.md#c19-i0031)
- [GROUP 省略時の動作](part-01.md#c19-i0032)

### JOB 文 IF 構造

- [COND と IF の併用時優先順位](part-01.md#c19-i0033)
- [IF 条件と ABEND 検査](part-01.md#c19-i0034)
- [IF 条件と RC 参照](part-01.md#c19-i0035)
- [IF 構造のネスト](part-01.md#c19-i0036)
- [IF/THEN/ELSE/ENDIF の位置](part-01.md#c19-i0037)

### JOB 文 MEMLIMIT

- [MEMLIMIT と IARV64 GETSTOR の関係](part-01.md#c19-i0038)
- [MEMLIMIT パラメータの目的](part-01.md#c19-i0039)
- [MEMLIMIT 省略時の既定値](part-01.md#c19-i0040)
- [MEMLIMIT=NG](part-01.md#c19-i0041)
- [MEMLIMIT=NM](part-01.md#c19-i0042)
- [MEMLIMIT=NOLIMIT](part-01.md#c19-i0043)
- [MEMLIMIT=NP](part-01.md#c19-i0044)
- [MEMLIMIT=NT](part-01.md#c19-i0045)
- [REGION=0M と MEMLIMIT の関係](part-01.md#c19-i0046)

### JOB 文 MSGCLASS

- [MSGCLASS と SYSOUT のクラス継承](part-01.md#c19-i0047)
- [MSGCLASS の値域](part-01.md#c19-i0048)
- [MSGCLASS パラメータの目的](part-01.md#c19-i0049)
- [MSGCLASS 省略時の動作](part-01.md#c19-i0050)
- [MSGCLASS=Z のホールド運用](part-01.md#c19-i0051)

### JOB 文 MSGLEVEL

- [MSGLEVEL messages=0](part-01.md#c19-i0052)
- [MSGLEVEL messages=1](part-01.md#c19-i0053)
- [MSGLEVEL statements=0](part-01.md#c19-i0054)
- [MSGLEVEL statements=1](part-01.md#c19-i0055)
- [MSGLEVEL statements=2](part-01.md#c19-i0056)
- [MSGLEVEL パラメータ構文](part-01.md#c19-i0057)
- [MSGLEVEL 省略時](part-01.md#c19-i0058)

### JOB 文 NOTIFY

- [NOTIFY と TSO SEND の関係](part-01.md#c19-i0059)
- [NOTIFY パラメータの目的](part-01.md#c19-i0060)
- [NOTIFY=&SYSUID](part-01.md#c19-i0061)
- [NOTIFY=user.node](part-01.md#c19-i0062)

### JOB 文 PASSWORD

- [PASSWORD パラメータの目的](part-01.md#c19-i0063)
- [PASSWORD 平文記述の危険性](part-01.md#c19-i0064)
- [PASSWORD/NEWPWD 新旧切替](part-01.md#c19-i0065)

### JOB 文 PERFORM

- [PERFORM の現状](part-01.md#c19-i0066)
- [PERFORM パラメータの目的](part-01.md#c19-i0067)

### JOB 文 PRTY

- [PRTY と WLM サービスクラスの関係](part-01.md#c19-i0068)
- [PRTY の値域](part-01.md#c19-i0069)
- [PRTY パラメータの目的](part-01.md#c19-i0070)
- [PRTY 省略時のデフォルト](part-01.md#c19-i0071)

### JOB 文 REGION

- [REGION と ABEND 878/80A](part-01.md#c19-i0072)
- [REGION と IEFUSI 出口](part-01.md#c19-i0073)
- [REGION の JOB 文と EXEC 文の優先順位](part-01.md#c19-i0074)
- [REGION の値域 (KB)](part-01.md#c19-i0075)
- [REGION の値域 (MB)](part-01.md#c19-i0076)
- [REGION パラメータの目的](part-01.md#c19-i0077)
- [REGION 偶数バイト切り上げ](part-01.md#c19-i0078)
- [REGION 省略時のデフォルト](part-01.md#c19-i0079)
- [REGION=0K](part-01.md#c19-i0080)
- [REGION=0M](part-01.md#c19-i0081)
- [REGION=NK の意味](part-01.md#c19-i0082)
- [REGION=NM と 16M ラインの関係](part-01.md#c19-i0083)
- [REGION=NM の意味](part-01.md#c19-i0084)

### JOB 文 RESTART

- [RESTART と DD DISP=(NEW,...) の整合](part-01.md#c19-i0085)
- [RESTART と GDG 世代の関係](part-01.md#c19-i0086)
- [RESTART と SYSCHK DD](part-01.md#c19-i0087)
- [RESTART パラメータの目的](part-01.md#c19-i0088)
- [RESTART=(stepname,checkid)](part-01.md#c19-i0089)
- [RESTART=*](part-01.md#c19-i0090)
- [RESTART=stepname](part-01.md#c19-i0091)
- [RESTART=stepname.procstep](part-01.md#c19-i0092)

### JOB 文 SCHENV

- [SCHENV と Parallel Sysplex](part-01.md#c19-i0093)
- [SCHENV パラメータの目的](part-01.md#c19-i0094)
- [SCHENV 未充足時の挙動](part-01.md#c19-i0095)

### JOB 文 SECLABEL

- [SECLABEL と MLS 環境](part-01.md#c19-i0096)
- [SECLABEL パラメータの目的](part-01.md#c19-i0097)

### JOB 文 TIME

- [JOB 文 TIME と EXEC 文 TIME の優先順位](part-01.md#c19-i0098)
- [TIME パラメータの目的](part-01.md#c19-i0099)
- [TIME 上限超過時の動作](part-01.md#c19-i0100)
- [TIME 省略時のデフォルト](part-01.md#c19-i0101)
- [TIME=(mm,ss) の構文](part-01.md#c19-i0102)
- [TIME=1440 の歴史的意味](part-01.md#c19-i0103)
- [TIME=MAXIMUM](part-01.md#c19-i0104)
- [TIME=NOLIMIT](part-01.md#c19-i0105)
- [TIME=分のみ指定](part-01.md#c19-i0106)

### JOB 文 TYPRUN

- [TYPRUN=COPY](part-01.md#c19-i0107)
- [TYPRUN=HOLD](part-01.md#c19-i0108)
- [TYPRUN=HOLD のリリース方法](part-01.md#c19-i0109)
- [TYPRUN=JCLHOLD](part-01.md#c19-i0110)
- [TYPRUN=SCAN](part-01.md#c19-i0111)
- [TYPRUN=SCAN と JES2 構文検証](part-01.md#c19-i0112)

### JOB 文 USER

- [USER の長さと文字種](part-01.md#c19-i0113)
- [USER パラメータの目的](part-01.md#c19-i0114)
- [USER 省略時のユーザ](part-01.md#c19-i0115)

### JOB 文 jobname

- [jobname の // 直後配置](part-01.md#c19-i0116)
- [jobname の命名規約とユーザ ID 連携](part-01.md#c19-i0117)
- [jobname の文字種](part-01.md#c19-i0118)
- [jobname の長さ制限](part-01.md#c19-i0119)
- [jobname 第 1 桁の制約](part-01.md#c19-i0120)
- [jobname 重複時の動作](part-01.md#c19-i0121)

### JOB 文 その他

- [CCSID パラメータ](part-01.md#c19-i0122)
- [DSENQSHR パラメータ](part-01.md#c19-i0123)
- [EMAIL パラメータ](part-01.md#c19-i0124)
- [JESLOG パラメータ](part-01.md#c19-i0125)
- [JOBRC パラメータ](part-01.md#c19-i0126)
- [REGIONX パラメータ](part-01.md#c19-i0127)
- [SYSAFF パラメータ](part-01.md#c19-i0128)

### JOB 文 アカウンティング

- [IEFUJV アカウンティング検証出口](part-01.md#c19-i0129)
- [アカウンティング情報の位置](part-01.md#c19-i0130)
- [アカウンティング情報の最大長](part-01.md#c19-i0131)
- [アカウンティング情報の構文](part-01.md#c19-i0132)
- [アカウンティング情報の省略](part-01.md#c19-i0133)
- [アカウンティング情報内の特殊文字](part-01.md#c19-i0134)
- [アカウンティング番号](part-01.md#c19-i0135)

### JOB 文 セキュリティ

- [Surrogate ユーザ運用](part-01.md#c19-i0136)

### JOB 文 プログラマ名

- [プログラマ名にアポストロフィが必要なケース](part-01.md#c19-i0137)
- [プログラマ名の位置](part-01.md#c19-i0138)
- [プログラマ名の最大長](part-01.md#c19-i0139)
- [プログラマ名の省略](part-01.md#c19-i0140)

### JOB 文 出力上限

- [BYTES パラメータの目的](part-01.md#c19-i0141)
- [BYTES/LINES と JES2 ESTBYTE/ESTLNCT の関係](part-01.md#c19-i0142)
- [BYTES=(N,option)](part-01.md#c19-i0143)
- [CARDS パラメータの目的](part-01.md#c19-i0144)
- [CARDS=(N,option)](part-01.md#c19-i0145)
- [LINES パラメータの目的](part-01.md#c19-i0146)
- [LINES=(N,option)](part-01.md#c19-i0147)
- [PAGES パラメータの目的](part-01.md#c19-i0148)
- [PAGES=(N,option)](part-01.md#c19-i0149)

### JOB 文 基本

- [//* コメント文との違い](part-01.md#c19-i0150)
- [JOB ステートメントの位置付け](part-01.md#c19-i0151)
- [JOB ステートメント最小構文](part-01.md#c19-i0152)
- [JOB 文のフィールド構成](part-01.md#c19-i0153)
- [JOB 文の継続行ルール](part-01.md#c19-i0154)
- [JOB 文コメントの記述位置](part-01.md#c19-i0155)

### JOB 文 運用

- [JCLLIB 文との関係](part-01.md#c19-i0156)
- [JES2 JOBCLASS の RESTART= 設定](part-01.md#c19-i0157)
- [JOB 文 IEFUJI 出口](part-01.md#c19-i0158)
- [JOB 文 IEFUJV 出口検証](part-01.md#c19-i0159)
- [JOBLIB DD 文の位置](part-01.md#c19-i0160)
- [JOBPARM JES2 制御文](part-01.md#c19-i0161)
- [ROUTE XEQ JES2 制御文](part-01.md#c19-i0162)

### その他

- [その他](part-02.md#c19-other)