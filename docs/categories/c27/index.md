# RACF USER/GROUP/DATASET

<div class="kb-cov" markdown>

**技術項目 387 件**  ／  QA対応 315（81.4%・不足 72）  ／  手順対応 382（98.71%・不足 5）

</div>

このカテゴリでは技術項目 387 件を掲載し、確認問題 172 問・検証手順 382 件を項目ごとに紐づけています。対応率は技術項目に明示的に対応付けられた件数で算出しています（増補継続中）。


> 最終更新: 2026-07-16


## 収録項目


### ADDGROUP BASE

- [DATA('text')](part-01.md#c27-i0001)
- [MODEL(dsname)](part-01.md#c27-i0002)
- [NOTERMUACC](part-01.md#c27-i0003)
- [OWNER(uid|group)](part-01.md#c27-i0004)
- [SUPGROUP(group)](part-01.md#c27-i0005)
- [TERMUACC](part-01.md#c27-i0006)
- [UNIVERSAL](part-01.md#c27-i0007)

### ADDGROUP CSDATA

- [CSDATA(field(val))](part-01.md#c27-i0008)

### ADDGROUP DFP

- [DFP(STORCLAS/MGMTCLAS/DATACLAS/DATAAPPL)](part-01.md#c27-i0009)

### ADDGROUP OMVS

- [OMVS(AUTOGID)](part-01.md#c27-i0010)
- [OMVS(GID(n))](part-01.md#c27-i0011)
- [OMVS(SHARED) GID 共有](part-01.md#c27-i0012)

### ADDGROUP OVM

- [OVM(GID(n))](part-01.md#c27-i0013)

### ADDGROUP TME

- [TME(ROLES(r))](part-01.md#c27-i0014)

### ADDGROUP 基本

- [ADDGROUP とは](part-01.md#c27-i0015)
- [ADDGROUP コマンドの用途](part-01.md#c27-i0016)
- [ADDGROUP 構文](part-01.md#c27-i0017)
- [ADDGROUP 発行権限](part-01.md#c27-i0018)
- [groupid 文字数](part-01.md#c27-i0019)

### ADDSD オペランド

- [AUDIT(READ|UPDATE|CONTROL|ALTER) 詳細](part-01.md#c27-i0020)
- [AUDIT(SUCCESS|FAILURES|ALL|NONE(...))](part-01.md#c27-i0021)
- [CATEGORY(cat)](part-01.md#c27-i0022)
- [DATA('text')](part-01.md#c27-i0023)
- [ERASE](part-01.md#c27-i0024)
- [FCLASS(class) FGENERIC](part-01.md#c27-i0025)
- [FROM(profile)](part-01.md#c27-i0026)
- [FROM/MODEL の違い](part-01.md#c27-i0027)
- [GENERIC](part-01.md#c27-i0028)
- [GLOBALAUDIT](part-01.md#c27-i0029)
- [LEVEL(n)](part-01.md#c27-i0030)
- [MODEL(profile)](part-01.md#c27-i0031)
- [NOERASE](part-01.md#c27-i0032)
- [NOTIFY(uid)](part-01.md#c27-i0033)
- [NOWARNING](part-01.md#c27-i0034)
- [OWNER(uid|grp)](part-01.md#c27-i0035)
- [SECLABEL(lbl)](part-01.md#c27-i0036)
- [SECLEVEL(n)](part-01.md#c27-i0037)
- [SET](part-01.md#c27-i0038)
- [UACC 既定値](part-01.md#c27-i0039)
- [UACC(NONE|EXECUTE|READ|UPDATE|CONTROL|ALTER)](part-01.md#c27-i0040)
- [UNIT(unit)](part-01.md#c27-i0041)
- [VOLSER(vol[,vol])](part-01.md#c27-i0042)
- [WARNING](part-01.md#c27-i0043)

### ADDSD 基本

- [ADDSD とは](part-01.md#c27-i0044)
- [ADDSD コマンドの用途](part-01.md#c27-i0045)
- [ADDSD 構文](part-01.md#c27-i0046)
- [ADDSD 発行権限](part-01.md#c27-i0047)
- [Discrete vs Generic 識別](part-01.md#c27-i0048)
- [profile-name 引用符](part-01.md#c27-i0049)

### ADDUSER BASE

- [ADSP](part-01.md#c27-i0050)
- [AUDITOR 属性](part-01.md#c27-i0051)
- [AUTHORITY(USE|CREATE|CONNECT|JOIN)](part-01.md#c27-i0052)
- [CATEGORY(cat)](part-01.md#c27-i0053)
- [CLAUTH(class)](part-01.md#c27-i0054)
- [DATA('text')](part-01.md#c27-i0055)
- [DFLTGRP(group)](part-01.md#c27-i0056)
- [GRPACC](part-01.md#c27-i0057)
- [MODEL(dsname)](part-01.md#c27-i0058)
- [NAME('user name')](part-01.md#c27-i0059)
- [NOADSP](part-01.md#c27-i0060)
- [NOAUDITOR](part-01.md#c27-i0061)
- [NOCLAUTH(class)](part-01.md#c27-i0062)
- [NOGRPACC](part-01.md#c27-i0063)
- [NOOPERATIONS](part-01.md#c27-i0064)
- [NOPASSWORD](part-01.md#c27-i0065)
- [NOPHRASE](part-01.md#c27-i0066)
- [NOSECLABEL](part-01.md#c27-i0067)
- [NOSPECIAL](part-01.md#c27-i0068)
- [NOUAUDIT](part-01.md#c27-i0069)
- [OPERATIONS 属性](part-01.md#c27-i0070)
- [OWNER(owner)](part-01.md#c27-i0071)
- [PASSWORD 省略時の挙動](part-01.md#c27-i0072)
- [PASSWORD(pw)](part-01.md#c27-i0073)
- [PHRASE('pass phrase')](part-01.md#c27-i0074)
- [RESUME(date)](part-01.md#c27-i0075)
- [REVOKE(date)](part-01.md#c27-i0076)
- [ROAUDIT 属性](part-01.md#c27-i0077)
- [SECLABEL(seclabel)](part-01.md#c27-i0078)
- [SECLEVEL(level)](part-01.md#c27-i0079)
- [SPECIAL 属性](part-01.md#c27-i0080)
- [UAUDIT](part-01.md#c27-i0081)
- [WHEN(DAYS/TIME)](part-01.md#c27-i0082)

### ADDUSER CICS

- [ADDUSER CICS セグメントとは](part-01.md#c27-i0083)
- [CICS セグメント指定](part-01.md#c27-i0084)
- [CICS(FORCE|NOFORCE)](part-01.md#c27-i0085)
- [CICS(OPCLASS(n,...))](part-01.md#c27-i0086)
- [CICS(OPIDENT(id))](part-01.md#c27-i0087)
- [CICS(OPPRTY(n))](part-01.md#c27-i0088)
- [CICS(TIMEOUT(hhmm))](part-01.md#c27-i0089)
- [CICS(XRFSOFF(FORCE|NOFORCE))](part-01.md#c27-i0090)
- [NOCICS](part-01.md#c27-i0091)

### ADDUSER DCE

- [ADDUSER DCE セグメントとは](part-01.md#c27-i0092)
- [DCE セグメント指定](part-01.md#c27-i0093)
- [DCE(AUTOLOGIN(YES|NO))](part-01.md#c27-i0094)
- [DCE(DCENAME('name'))](part-01.md#c27-i0095)
- [DCE(HOMECELL('cell'))](part-01.md#c27-i0096)
- [DCE(UUID('uuid'))](part-01.md#c27-i0097)

### ADDUSER DFP

- [ADDUSER DFP セグメントとは](part-01.md#c27-i0098)
- [DFP セグメント指定](part-01.md#c27-i0099)
- [DFP(DATAAPPL(name))](part-01.md#c27-i0100)
- [DFP(DATACLAS(name))](part-01.md#c27-i0101)
- [DFP(MGMTCLAS(name))](part-01.md#c27-i0102)
- [DFP(STORCLAS(name))](part-01.md#c27-i0103)
- [NODFP](part-01.md#c27-i0104)

### ADDUSER EIM

- [EIM(LDAPPROF(prof))](part-01.md#c27-i0105)

### ADDUSER KERB

- [ADDUSER KERB セグメントとは](part-01.md#c27-i0106)
- [KERB セグメント指定](part-01.md#c27-i0107)
- [KERB(ENCRYPT(...))](part-01.md#c27-i0108)
- [KERB(KERBNAME('name'))](part-01.md#c27-i0109)
- [KERB(MAXTKTLFE(n))](part-01.md#c27-i0110)

### ADDUSER LANG

- [LANGUAGE(PRIMARY(lang))](part-01.md#c27-i0111)
- [LANGUAGE(SECONDARY(lang))](part-01.md#c27-i0112)

### ADDUSER MFA

- [MFA(ACTIVE|NOACTIVE)](part-01.md#c27-i0113)
- [MFA(FACTOR(name))](part-01.md#c27-i0114)
- [MFA(TAGS('tag:val'))](part-01.md#c27-i0115)

### ADDUSER NDS

- [NDS(UNAME('name'))](part-01.md#c27-i0116)

### ADDUSER NETVIEW

- [ADDUSER NETVIEW セグメントとは](part-01.md#c27-i0117)
- [NETVIEW セグメント指定](part-01.md#c27-i0118)
- [NETVIEW(CONSNAME(name))](part-01.md#c27-i0119)
- [NETVIEW(CTL(GLOBAL|GENERAL|SPECIFIC))](part-01.md#c27-i0120)
- [NETVIEW(DOMAINS(d,...))](part-01.md#c27-i0121)
- [NETVIEW(IC('cmd'))](part-01.md#c27-i0122)
- [NETVIEW(MSGRECVR(YES|NO))](part-01.md#c27-i0123)
- [NETVIEW(NGMFADMN(YES|NO))](part-01.md#c27-i0124)
- [NETVIEW(OPCLASS(n,...))](part-01.md#c27-i0125)

### ADDUSER OMVS

- [NOOMVS](part-01.md#c27-i0126)
- [OMVS セグメント指定](part-01.md#c27-i0127)
- [OMVS(ASSIZEMAX(n))](part-01.md#c27-i0128)
- [OMVS(AUTOUID)](part-01.md#c27-i0129)
- [OMVS(CPUTIMEMAX(n))](part-01.md#c27-i0130)
- [OMVS(FILEPROCMAX(n))](part-01.md#c27-i0131)
- [OMVS(HOME('path'))](part-01.md#c27-i0132)
- [OMVS(MEMLIMIT(n))](part-01.md#c27-i0133)
- [OMVS(MMAPAREAMAX(n))](part-01.md#c27-i0134)
- [OMVS(PROCUSERMAX(n))](part-01.md#c27-i0135)
- [OMVS(PROGRAM('path'))](part-01.md#c27-i0136)
- [OMVS(SHARED) UID 共有](part-01.md#c27-i0137)
- [OMVS(SHMEMMAX(n))](part-01.md#c27-i0138)
- [OMVS(THREADSMAX(n))](part-01.md#c27-i0139)
- [OMVS(UID(n))](part-01.md#c27-i0140)

### ADDUSER OVM

- [OVM セグメント指定](part-01.md#c27-i0141)
- [OVM(UID(n)/HOME/PROGRAM/FSROOT)](part-01.md#c27-i0142)

### ADDUSER PROXY

- [PROXY(BINDDN('dn'))](part-01.md#c27-i0143)
- [PROXY(BINDPW('pw'))](part-01.md#c27-i0144)
- [PROXY(LDAPHOST('url'))](part-01.md#c27-i0145)

### ADDUSER TSO

- [NOTSO](part-01.md#c27-i0146)
- [TSO セグメント指定](part-01.md#c27-i0147)
- [TSO(ACCTNUM(acct))](part-01.md#c27-i0148)
- [TSO(COMMAND('cmd'))](part-01.md#c27-i0149)
- [TSO(DEST(dest))](part-01.md#c27-i0150)
- [TSO(HOLDCLASS(c))](part-01.md#c27-i0151)
- [TSO(JOBCLASS(c))](part-01.md#c27-i0152)
- [TSO(MAXSIZE(K))](part-01.md#c27-i0153)
- [TSO(MSGCLASS(c))](part-01.md#c27-i0154)
- [TSO(PROC(proc))](part-01.md#c27-i0155)
- [TSO(SECLABEL(lbl))](part-01.md#c27-i0156)
- [TSO(SIZE(K))](part-01.md#c27-i0157)
- [TSO(SYSOUTCLASS(c))](part-01.md#c27-i0158)
- [TSO(UNIT(unit))](part-01.md#c27-i0159)
- [TSO(USERDATA(hex))](part-01.md#c27-i0160)

### ADDUSER WORKATTR

- [ADDUSER WORKATTR セグメントとは](part-01.md#c27-i0161)
- [NOWORKATTR](part-01.md#c27-i0162)
- [WORKATTR セグメント指定](part-01.md#c27-i0163)
- [WORKATTR(WAACCNT('text'))](part-01.md#c27-i0164)
- [WORKATTR(WAADDR1〜4('text'))](part-01.md#c27-i0165)
- [WORKATTR(WABLDG('text'))](part-01.md#c27-i0166)
- [WORKATTR(WADEPT('text'))](part-01.md#c27-i0167)
- [WORKATTR(WAEMAIL('text'))](part-01.md#c27-i0168)
- [WORKATTR(WANAME('text'))](part-01.md#c27-i0169)
- [WORKATTR(WAROOM('text'))](part-01.md#c27-i0170)

### ADDUSER 基本

- [ADDUSER と DEFAULT 値](part-01.md#c27-i0171)
- [ADDUSER コマンドの用途](part-01.md#c27-i0172)
- [ADDUSER 必須オペランド](part-01.md#c27-i0173)
- [ADDUSER 既存ユーザ](part-01.md#c27-i0174)
- [ADDUSER 構文位置](part-01.md#c27-i0175)
- [ADDUSER 発行権限](part-01.md#c27-i0176)
- [ADDUSER 短縮形](part-01.md#c27-i0177)
- [userid 文字数制限](part-01.md#c27-i0178)
- [userid 文字種](part-01.md#c27-i0179)

### ALTDSD 全般

- [ALTDSD ADDCATEGORY/DELCATEGORY](part-01.md#c27-i0180)
- [ALTDSD ADDVOL(vol)](part-01.md#c27-i0181)
- [ALTDSD DATA('text')](part-01.md#c27-i0182)
- [ALTDSD DELVOL(vol)](part-01.md#c27-i0183)
- [ALTDSD ERASE/NOERASE](part-01.md#c27-i0184)
- [ALTDSD GENERIC](part-01.md#c27-i0185)
- [ALTDSD GLOBALAUDIT](part-01.md#c27-i0186)
- [ALTDSD LEVEL(n)](part-01.md#c27-i0187)
- [ALTDSD OWNER/UACC/NOTIFY/AUDIT](part-01.md#c27-i0188)
- [ALTDSD RESET(STATISTICS|ALL)](part-01.md#c27-i0189)
- [ALTDSD SECLABEL/SECLEVEL](part-01.md#c27-i0190)
- [ALTDSD WARNING/NOWARNING](part-01.md#c27-i0191)

### ALTDSD 基本

- [ALTDSD とは](part-01.md#c27-i0192)
- [ALTDSD コマンドの用途](part-01.md#c27-i0193)
- [ALTDSD 必須オペランド](part-01.md#c27-i0194)

### ALTGROUP セグメント

- [ALTGROUP DFP/OMVS/OVM/CSDATA](part-01.md#c27-i0195)
- [ALTGROUP OMVS(NOGID)](part-01.md#c27-i0196)

### ALTGROUP 全般

- [ALTGROUP OWNER/DATA/MODEL](part-01.md#c27-i0197)
- [ALTGROUP SUPGROUP(new)](part-01.md#c27-i0198)
- [ALTGROUP TERMUACC/NOTERMUACC](part-01.md#c27-i0199)
- [ALTGROUP UNIVERSAL は変更不可](part-01.md#c27-i0200)

### ALTGROUP 基本

- [ALTGROUP とは](part-01.md#c27-i0201)
- [ALTGROUP コマンドの用途](part-01.md#c27-i0202)
- [ALTGROUP 必須オペランド](part-01.md#c27-i0203)

### ALTUSER REVOKE

- [RESUME](part-01.md#c27-i0204)
- [RESUME(date)](part-01.md#c27-i0205)
- [REVOKE](part-01.md#c27-i0206)
- [REVOKE(date)](part-01.md#c27-i0207)

### ALTUSER セグメント

- [ALTUSER CICS/DFP/NETVIEW/KERB...](part-01.md#c27-i0208)
- [ALTUSER NOTSO/NOOMVS/NOCICS 等](part-01.md#c27-i0209)
- [ALTUSER OMVS(...)](part-01.md#c27-i0210)
- [ALTUSER OMVS(NOUID)](part-01.md#c27-i0211)
- [ALTUSER TSO(...)](part-01.md#c27-i0212)

### ALTUSER 全般

- [ALTUSER CLAUTH/NOCLAUTH](part-01.md#c27-i0213)
- [ALTUSER GRPACC/NOGRPACC](part-02.md#c27-i0214)
- [ALTUSER NAME/OWNER/DFLTGRP/DATA](part-02.md#c27-i0215)
- [ALTUSER PASSWORD(pw)](part-02.md#c27-i0216)
- [ALTUSER PASSWORD(pw) NOEXPIRED](part-02.md#c27-i0217)
- [ALTUSER PHRASE/NOPHRASE](part-02.md#c27-i0218)
- [ALTUSER SECLABEL/NOSECLABEL](part-02.md#c27-i0219)
- [ALTUSER SPECIAL/OPERATIONS/AUDITOR](part-02.md#c27-i0220)
- [ALTUSER UAUDIT/NOUAUDIT](part-02.md#c27-i0221)
- [ALTUSER WHEN(DAYS/TIME)](part-02.md#c27-i0222)

### ALTUSER 基本

- [ALTUSER で属性の OFF](part-02.md#c27-i0223)
- [ALTUSER とは](part-02.md#c27-i0224)
- [ALTUSER コマンドの用途](part-02.md#c27-i0225)
- [ALTUSER 必須オペランド](part-02.md#c27-i0226)
- [ALTUSER 発行権限](part-02.md#c27-i0227)

### CONNECT AUTHORITY

- [AUTHORITY(CONNECT)](part-02.md#c27-i0228)
- [AUTHORITY(CREATE)](part-02.md#c27-i0229)
- [AUTHORITY(JOIN)](part-02.md#c27-i0230)
- [AUTHORITY(USE)](part-02.md#c27-i0231)

### CONNECT GROUP

- [GROUP(group)](part-02.md#c27-i0232)

### CONNECT 基本

- [CONNECT とは](part-02.md#c27-i0233)
- [CONNECT コマンドの用途](part-02.md#c27-i0234)
- [CONNECT 必須オペランド](part-02.md#c27-i0235)
- [CONNECT 構文](part-02.md#c27-i0236)
- [CONNECT 発行権限](part-02.md#c27-i0237)

### CONNECT 属性

- [ADSP](part-02.md#c27-i0238)
- [AUDITOR](part-02.md#c27-i0239)
- [GRPACC](part-02.md#c27-i0240)
- [NOACC (ICHRIN03 同等)](part-02.md#c27-i0241)
- [NOADSP](part-02.md#c27-i0242)
- [NOGRPACC](part-02.md#c27-i0243)
- [OPERATIONS](part-02.md#c27-i0244)
- [OWNER(uid|grp)](part-02.md#c27-i0245)
- [RESUME(date)](part-02.md#c27-i0246)
- [REVOKE(date)](part-02.md#c27-i0247)
- [SPECIAL](part-02.md#c27-i0248)
- [UACC(level)](part-02.md#c27-i0249)

### DELDSD 基本

- [DELDSD ERASE 効果](part-02.md#c27-i0250)
- [DELDSD VOLUME(v)](part-02.md#c27-i0251)
- [DELDSD とは](part-02.md#c27-i0252)
- [DELDSD と実 DSN](part-02.md#c27-i0253)
- [DELDSD コマンドの用途](part-02.md#c27-i0254)
- [DELDSD 構文](part-02.md#c27-i0255)

### DELGROUP 基本

- [DELGROUP とは](part-02.md#c27-i0256)
- [DELGROUP コマンドの用途](part-02.md#c27-i0257)
- [DELGROUP 不可ケース](part-02.md#c27-i0258)
- [DELGROUP 子グループ](part-02.md#c27-i0259)
- [DELGROUP 構文](part-02.md#c27-i0260)

### DELUSER 基本

- [DELUSER とは](part-02.md#c27-i0261)
- [DELUSER の副作用](part-02.md#c27-i0262)
- [DELUSER コマンドの用途](part-02.md#c27-i0263)
- [DELUSER 不可ケース](part-02.md#c27-i0264)
- [DELUSER 構文](part-02.md#c27-i0265)
- [DELUSER 発行権限](part-02.md#c27-i0266)
- [IRRRID00 で残骸削除](part-02.md#c27-i0267)

### LISTDSD 基本

- [LISTDSD ALL](part-02.md#c27-i0268)
- [LISTDSD AUTHUSER](part-02.md#c27-i0269)
- [LISTDSD DATASET('p')](part-02.md#c27-i0270)
- [LISTDSD DSNS](part-02.md#c27-i0271)
- [LISTDSD GENERIC](part-02.md#c27-i0272)
- [LISTDSD HISTORY](part-02.md#c27-i0273)
- [LISTDSD ID(uid|grp)](part-02.md#c27-i0274)
- [LISTDSD NORACF](part-02.md#c27-i0275)
- [LISTDSD PREFIX('hlq')](part-02.md#c27-i0276)
- [LISTDSD STATISTICS](part-02.md#c27-i0277)
- [LISTDSD とは](part-02.md#c27-i0278)
- [LISTDSD コマンドの用途](part-02.md#c27-i0279)

### LISTGRP 基本

- [LISTGRP とは](part-02.md#c27-i0280)
- [LISTGRP コマンドの用途](part-02.md#c27-i0281)
- [LISTGRP ワイルドカード *](part-02.md#c27-i0282)
- [LISTGRP 構文](part-02.md#c27-i0283)

### LISTGRP 表示制御

- [LISTGRP DFP/OMVS/OVM/TME/CSDATA](part-02.md#c27-i0284)
- [LISTGRP NORACF](part-02.md#c27-i0285)
- [LISTGRP SUBGROUPS](part-02.md#c27-i0286)
- [LISTGRP 出力 メンバ一覧](part-02.md#c27-i0287)

### LISTUSER 基本

- [LISTUSER とは](part-02.md#c27-i0288)
- [LISTUSER コマンドの用途](part-02.md#c27-i0289)
- [LISTUSER ワイルドカード *](part-02.md#c27-i0290)
- [LISTUSER 構文](part-02.md#c27-i0291)
- [LISTUSER 自分自身](part-02.md#c27-i0292)

### LISTUSER 表示制御

- [LISTUSER CICS](part-02.md#c27-i0293)
- [LISTUSER DFP](part-02.md#c27-i0294)
- [LISTUSER KERB/EIM/PROXY/LANGUAGE/MFA](part-02.md#c27-i0295)
- [LISTUSER NETVIEW](part-02.md#c27-i0296)
- [LISTUSER NORACF](part-02.md#c27-i0297)
- [LISTUSER OMVS](part-02.md#c27-i0298)
- [LISTUSER OVM/NDS/DCE](part-02.md#c27-i0299)
- [LISTUSER PWD INTERVAL](part-02.md#c27-i0300)
- [LISTUSER TSO](part-02.md#c27-i0301)
- [LISTUSER WORKATTR](part-02.md#c27-i0302)
- [LISTUSER 出力 LAST-ACCESS](part-02.md#c27-i0303)
- [LISTUSER 表示パスワード](part-02.md#c27-i0304)

### PASSWORD コマンド

- [PASSWORD EXPIRED 動作](part-02.md#c27-i0305)
- [PASSWORD INTERVAL(n)](part-02.md#c27-i0306)
- [PASSWORD NOINTERVAL](part-02.md#c27-i0307)
- [PASSWORD USER(uid)](part-02.md#c27-i0308)
- [PASSWORD の用途](part-02.md#c27-i0309)
- [PASSWORD コマンドとは](part-02.md#c27-i0310)
- [PASSWORD 短縮形](part-02.md#c27-i0311)
- [PASSWORD(old/new)](part-02.md#c27-i0312)
- [PHRASE オペランド](part-02.md#c27-i0313)

### PERMIT ACCESS

- [ACCESS 階層性](part-02.md#c27-i0314)
- [ACCESS(ALTER)](part-02.md#c27-i0315)
- [ACCESS(CONTROL)](part-02.md#c27-i0316)
- [ACCESS(EXECUTE)](part-02.md#c27-i0317)
- [ACCESS(NONE)](part-02.md#c27-i0318)
- [ACCESS(READ)](part-02.md#c27-i0319)
- [ACCESS(UPDATE)](part-02.md#c27-i0320)

### PERMIT CLASS

- [CLASS(DATASET)](part-02.md#c27-i0321)
- [CLASS(class)](part-02.md#c27-i0322)

### PERMIT DELETE

- [DELETE オペランド](part-02.md#c27-i0323)

### PERMIT FROM

- [FCLASS(class)](part-02.md#c27-i0324)
- [FROM(profile)](part-02.md#c27-i0325)

### PERMIT GENERIC

- [GENERIC](part-02.md#c27-i0326)

### PERMIT ID

- [ID(*) 指定](part-02.md#c27-i0327)
- [ID(uid|grp,...)](part-02.md#c27-i0328)

### PERMIT RESET

- [RESET オペランド](part-02.md#c27-i0329)
- [RESET(ALL)](part-02.md#c27-i0330)
- [RESET(CONDITIONAL)](part-02.md#c27-i0331)
- [RESET(STANDARD)](part-02.md#c27-i0332)

### PERMIT WHEN

- [WHEN(APPCPORT(name))](part-02.md#c27-i0333)
- [WHEN(CONSOLE(name))](part-02.md#c27-i0334)
- [WHEN(CRITERIA(SQLROLE=...))](part-02.md#c27-i0335)
- [WHEN(DAYS(WEEKDAYS|ANYDAY|MONDAY|...))](part-02.md#c27-i0336)
- [WHEN(JESINPUT(name))](part-02.md#c27-i0337)
- [WHEN(PARTNER(LU))](part-02.md#c27-i0338)
- [WHEN(PROFILE(prof))](part-02.md#c27-i0339)
- [WHEN(PROGRAM(name))](part-02.md#c27-i0340)
- [WHEN(SERVAUTH(name))](part-02.md#c27-i0341)
- [WHEN(SQLROLE(role))](part-02.md#c27-i0342)
- [WHEN(SYSID(sysid))](part-02.md#c27-i0343)
- [WHEN(TIME(hhmm:hhmm))](part-02.md#c27-i0344)

### PERMIT 基本

- [PERMIT とは](part-02.md#c27-i0345)
- [PERMIT コマンドの用途](part-02.md#c27-i0346)
- [PERMIT 既定対象クラス](part-02.md#c27-i0347)
- [PERMIT 構文](part-02.md#c27-i0348)
- [PERMIT 発行権限](part-02.md#c27-i0349)

### REMOVE 基本

- [REMOVE DFLTGRP は不可](part-02.md#c27-i0350)
- [REMOVE GROUP 省略時](part-02.md#c27-i0351)
- [REMOVE OWNER(o)](part-02.md#c27-i0352)
- [REMOVE とは](part-02.md#c27-i0353)
- [REMOVE コマンドの用途](part-02.md#c27-i0354)
- [REMOVE 必須オペランド](part-02.md#c27-i0355)
- [REMOVE 構文](part-02.md#c27-i0356)
- [REMOVE 発行権限](part-02.md#c27-i0357)

### SEARCH CLASS

- [CLASS(DATASET)](part-02.md#c27-i0358)
- [CLASS(GROUP)](part-02.md#c27-i0359)
- [CLASS(USER)](part-02.md#c27-i0360)
- [CLASS(class)](part-02.md#c27-i0361)

### SEARCH フィルタ

- [FILTER('mask')](part-02.md#c27-i0362)
- [MASK('hlq','rest')](part-02.md#c27-i0363)
- [NOMASK](part-02.md#c27-i0364)

### SEARCH 基本

- [SEARCH とは](part-02.md#c27-i0365)
- [SEARCH コマンドの用途](part-02.md#c27-i0366)
- [SEARCH 発行権限](part-02.md#c27-i0367)
- [SEARCH 短縮形](part-02.md#c27-i0368)

### SEARCH 条件

- [AGE(n)](part-02.md#c27-i0369)
- [CATEGORY(cat)](part-02.md#c27-i0370)
- [ERASE](part-02.md#c27-i0371)
- [EXPIRES(n)](part-02.md#c27-i0372)
- [GENERIC](part-02.md#c27-i0373)
- [NOGENERIC](part-02.md#c27-i0374)
- [RESUME(n)](part-02.md#c27-i0375)
- [REVOKE(n)](part-02.md#c27-i0376)
- [SECLABEL(lbl)](part-02.md#c27-i0377)
- [SECLEVEL(n)](part-02.md#c27-i0378)
- [UACC(level)](part-02.md#c27-i0379)
- [USER(uid)](part-02.md#c27-i0380)
- [VOLUME(vol)](part-02.md#c27-i0381)
- [VTOC](part-02.md#c27-i0382)
- [WARNING](part-02.md#c27-i0383)

### SEARCH 表示制御

- [CLIST 出力ファイル](part-02.md#c27-i0384)
- [CLIST('cmd')](part-02.md#c27-i0385)
- [NOLIST](part-02.md#c27-i0386)
- [NORACF](part-02.md#c27-i0387)

### その他

- [その他](part-02.md#c27-other)