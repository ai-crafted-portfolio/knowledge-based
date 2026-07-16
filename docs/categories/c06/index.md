# DFSMS / IDCAMS / VSAM

<div class="kb-cov" markdown>

**技術項目 250 件**  ／  QA対応 250（100.0%・不足 0）  ／  手順対応 246（98.4%・不足 4）

</div>

このカテゴリでは技術項目 250 件を掲載し、確認問題 316 問・検証手順 295 件を項目ごとに紐づけています。対応率は技術項目に明示的に対応付けられた件数で算出しています（増補継続中）。


> 最終更新: 2026-07-16


## 収録項目


### ACS_ROUTINES

- [ACS TEST 機能](part-01.md#c06-i0001)
- [ACS ルーチン概要](part-01.md#c06-i0002)
- [ACS 変数 (&DSN, &USER, &APPLIC など)](part-01.md#c06-i0003)
- [DATACLAS ACS](part-01.md#c06-i0004)
- [FILTLIST](part-01.md#c06-i0005)
- [MGMTCLAS ACS](part-01.md#c06-i0006)
- [STORCLAS ACS](part-01.md#c06-i0007)
- [STORGRP ACS](part-01.md#c06-i0008)

### ALTER

- [ADDVOLUMES / REMOVEVOLUMES](part-01.md#c06-i0009)
- [ALTER NULLIFY](part-01.md#c06-i0010)
- [ALTER 基本](part-01.md#c06-i0011)
- [BUFFERSPACE(n)](part-01.md#c06-i0012)
- [BWO (Backup-While-Open) 設定](part-01.md#c06-i0013)
- [FREESPACE(ci% ca%)](part-01.md#c06-i0014)
- [INHIBIT / UNINHIBIT](part-01.md#c06-i0015)
- [LOCK / UNLOCK](part-01.md#c06-i0016)
- [LOG / LOGSTREAMID (RLS/TVS)](part-01.md#c06-i0017)
- [MGMTCLAS / STORCLAS / DATACLAS 変更](part-01.md#c06-i0018)
- [NEWNAME(newname)](part-01.md#c06-i0019)
- [SHAREOPTIONS(cr cs)](part-01.md#c06-i0020)
- [TO(yyyyddd) / FOR(days)](part-01.md#c06-i0021)

### BLDINDEX

- [BLDINDEX 基本](part-01.md#c06-i0022)
- [EXTERNALSORT / INTERNALSORT](part-01.md#c06-i0023)
- [INDATASET / OUTDATASET (BLDINDEX)](part-01.md#c06-i0024)
- [WORKFILES(dd1 dd2)](part-01.md#c06-i0025)

### DEFINE_AIX

- [DEFINE ALTERNATEINDEX 基本](part-01.md#c06-i0026)
- [KEYS(len off) / RECORDSIZE](part-01.md#c06-i0027)
- [RELATE(basename)](part-01.md#c06-i0028)
- [UNIQUEKEY / NONUNIQUEKEY](part-01.md#c06-i0029)
- [UPGRADE / NOUPGRADE](part-01.md#c06-i0030)

### DEFINE_ALIAS

- [DEFINE ALIAS 基本](part-01.md#c06-i0031)
- [RELATE(usercatname)](part-01.md#c06-i0032)
- [SYMBOLICRELATE](part-01.md#c06-i0033)

### DEFINE_CATALOG

- [DEFINE MASTERCATALOG](part-01.md#c06-i0034)
- [DEFINE USERCATALOG](part-01.md#c06-i0035)
- [ICFCATALOG](part-01.md#c06-i0036)
- [STRNO(n) (カタログ性能)](part-01.md#c06-i0037)
- [VOLCATALOG (テープ)](part-01.md#c06-i0038)

### DEFINE_CLUSTER

- [ATTEMPTS(n)](part-01.md#c06-i0039)
- [AUTHORIZATION(modname [str])](part-01.md#c06-i0040)
- [BUFFERSPACE(n)](part-01.md#c06-i0041)
- [CATALOG(catname)](part-01.md#c06-i0042)
- [CISZ の選択指針](part-01.md#c06-i0043)
- [CODE(code)](part-01.md#c06-i0044)
- [CONTROLINTERVALSIZE / CISZ(n)](part-01.md#c06-i0045)
- [CONTROLPW / MASTERPW / UPDATEPW / READPW](part-01.md#c06-i0046)
- [CYLINDERS(p s)](part-01.md#c06-i0047)
- [DATACLAS(name)](part-01.md#c06-i0048)
- [DEFINE CLUSTER 基本構文](part-01.md#c06-i0049)
- [EXCEPTIONEXIT(modname)](part-01.md#c06-i0050)
- [FREESPACE(ci% ca%)](part-01.md#c06-i0051)
- [IMBED (廃止)](part-01.md#c06-i0052)
- [INDEXED (KSDS)](part-01.md#c06-i0053)
- [KEYS(length offset)](part-01.md#c06-i0054)
- [LINEAR (LDS)](part-01.md#c06-i0055)
- [MGMTCLAS(name)](part-01.md#c06-i0056)
- [MODEL(entryname)](part-01.md#c06-i0057)
- [NAME(entryname)](part-01.md#c06-i0058)
- [NONINDEXED (ESDS)](part-01.md#c06-i0059)
- [NUMBERED (RRDS)](part-01.md#c06-i0060)
- [OWNER(ownerid)](part-01.md#c06-i0061)
- [RECORDS(p s)](part-01.md#c06-i0062)
- [RECORDSIZE(avg max)](part-01.md#c06-i0063)
- [RECOVERY (既定)](part-01.md#c06-i0064)
- [REPLICATE (廃止)](part-01.md#c06-i0065)
- [REUSE / NOREUSE](part-01.md#c06-i0066)
- [SHAREOPTIONS(3,3) の注意](part-01.md#c06-i0067)
- [SHAREOPTIONS(4,4) と RLS](part-01.md#c06-i0068)
- [SHAREOPTIONS(cr cs)](part-01.md#c06-i0069)
- [SPANNED](part-01.md#c06-i0070)
- [SPEED](part-01.md#c06-i0071)
- [STORCLAS(name)](part-01.md#c06-i0072)
- [TO(yyyyddd) / FOR(days)](part-01.md#c06-i0073)
- [TRACKS(p s)](part-01.md#c06-i0074)
- [UNIQUE / SUBALLOCATION (廃止)](part-01.md#c06-i0075)
- [UNIT(unittype)](part-01.md#c06-i0076)
- [VOLUMES(volser ...)](part-01.md#c06-i0077)

### DEFINE_GDG

- [DEFINE GDG 基本](part-01.md#c06-i0078)
- [EMPTY / NOEMPTY](part-01.md#c06-i0079)
- [EXTENDED](part-01.md#c06-i0080)
- [LIMIT(n)](part-01.md#c06-i0081)
- [OWNER(id)](part-01.md#c06-i0082)
- [PURGE / NOPURGE](part-01.md#c06-i0083)
- [SCRATCH / NOSCRATCH](part-01.md#c06-i0084)
- [TO / FOR (GDG)](part-01.md#c06-i0085)

### DEFINE_NONVSAM

- [DEFINE NONVSAM 基本](part-01.md#c06-i0086)
- [FILESEQUENCENUMBERS (テープ)](part-01.md#c06-i0087)
- [VOLUMES(volser) と DEVICETYPES](part-01.md#c06-i0088)

### DEFINE_PAGESPACE

- [DEFINE PAGESPACE 基本](part-01.md#c06-i0089)
- [SWAP (廃止)](part-01.md#c06-i0090)

### DEFINE_PATH

- [DEFINE PATH 基本](part-01.md#c06-i0091)
- [PATHENTRY(aixname)](part-01.md#c06-i0092)
- [UPDATE / NOUPDATE (PATH)](part-01.md#c06-i0093)

### DELETE

- [AIX (ALTERNATEINDEX)](part-01.md#c06-i0094)
- [ALIAS](part-01.md#c06-i0095)
- [CLUSTER](part-01.md#c06-i0096)
- [DELETE 基本](part-01.md#c06-i0097)
- [ERASE / NOERASE](part-01.md#c06-i0098)
- [FORCE](part-01.md#c06-i0099)
- [GDG](part-01.md#c06-i0100)
- [NONVSAM](part-01.md#c06-i0101)
- [PAGESPACE](part-01.md#c06-i0102)
- [PATH](part-01.md#c06-i0103)
- [PURGE / NOPURGE](part-01.md#c06-i0104)
- [SCRATCH / NOSCRATCH (DELETE)](part-01.md#c06-i0105)
- [USERCATALOG](part-01.md#c06-i0106)

### DIAGNOSE

- [COMPAREDD](part-01.md#c06-i0107)
- [DIAGNOSE 基本](part-01.md#c06-i0108)
- [ICFCATALOG / VVDS](part-01.md#c06-i0109)
- [INCLUDE / EXCLUDE](part-01.md#c06-i0110)

### DSS

- [BUILDSA](part-01.md#c06-i0111)
- [COMPRESS](part-01.md#c06-i0112)
- [CONVERTV](part-01.md#c06-i0113)
- [COPY](part-01.md#c06-i0114)
- [DFSMSdss 概要](part-01.md#c06-i0115)
- [DUMP](part-01.md#c06-i0116)
- [PHYSINDD / LOGINDD](part-01.md#c06-i0117)
- [PRINT (DSS)](part-01.md#c06-i0118)
- [RELEASE](part-01.md#c06-i0119)
- [RESTORE](part-01.md#c06-i0120)

### EXAMINE

- [ERRORLIMIT(n)](part-01.md#c06-i0121)
- [EXAMINE 基本](part-01.md#c06-i0122)
- [INDEXTEST / DATATEST](part-01.md#c06-i0123)

### EXPORT

- [EXPORT 基本](part-01.md#c06-i0124)
- [INFILE / OUTFILE (EXPORT)](part-01.md#c06-i0125)
- [TEMPORARY / PERMANENT](part-01.md#c06-i0126)

### EXPORTRA

- [EXPORTRA (リカバリ用)](part-01.md#c06-i0127)

### HSM

- [Automatic Backup](part-01.md#c06-i0128)
- [Automatic Dump](part-01.md#c06-i0129)
- [DFSMShsm 概要](part-01.md#c06-i0130)
- [HALTERDS](part-01.md#c06-i0131)
- [HBACKDS](part-01.md#c06-i0132)
- [HDELETE](part-01.md#c06-i0133)
- [HMIGRATE](part-01.md#c06-i0134)
- [HQUERY](part-01.md#c06-i0135)
- [HRECALL](part-01.md#c06-i0136)
- [HRECOVER](part-01.md#c06-i0137)
- [HSEND コマンド](part-01.md#c06-i0138)
- [Primary Space Management (PSM)](part-01.md#c06-i0139)

### ICF

- [BCS と VVDS の整合性](part-01.md#c06-i0140)
- [BCS の役割](part-01.md#c06-i0141)
- [Catalog Address Space (CAS)](part-01.md#c06-i0142)
- [Catalog Search Order](part-01.md#c06-i0143)
- [ICF カタログ概要](part-01.md#c06-i0144)
- [MODIFY CATALOG コマンド](part-01.md#c06-i0145)
- [NVR (Non-VSAM Volume Record)](part-01.md#c06-i0146)
- [VVDS の役割](part-01.md#c06-i0147)
- [VVDS 名規則](part-01.md#c06-i0148)
- [VVR (VSAM Volume Record)](part-01.md#c06-i0149)

### IMPORT

- [IMPORT 基本](part-01.md#c06-i0150)
- [INTOEMPTY](part-01.md#c06-i0151)
- [OBJECTS (IMPORT)](part-01.md#c06-i0152)

### IMPORTRA

- [IMPORTRA (リカバリ用)](part-01.md#c06-i0153)

### LISTCAT

- [ALL](part-01.md#c06-i0154)
- [ALLOCATION](part-01.md#c06-i0155)
- [CATALOG(catname)](part-01.md#c06-i0156)
- [CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIAS](part-01.md#c06-i0157)
- [CREATION / EXPIRATION](part-02.md#c06-i0158)
- [ENTRIES(name) / LEVEL(prefix)](part-02.md#c06-i0159)
- [HISTORY](part-02.md#c06-i0160)
- [LISTCAT 基本](part-02.md#c06-i0161)
- [NAMES](part-02.md#c06-i0162)
- [OUTFILE(ddname)](part-02.md#c06-i0163)
- [SPACE](part-02.md#c06-i0164)
- [VOLUME](part-02.md#c06-i0165)

### PRINT

- [CHARACTER](part-02.md#c06-i0166)
- [DUMP (既定)](part-02.md#c06-i0167)
- [FROMKEY/TOKEY/COUNT/SKIP (PRINT)](part-02.md#c06-i0168)
- [HEX](part-02.md#c06-i0169)
- [INFILE(ddname) / INDATASET(name)](part-02.md#c06-i0170)
- [PRINT 基本](part-02.md#c06-i0171)

### REPRO

- [COUNT(n)](part-02.md#c06-i0172)
- [FROMADDRESS / TOADDRESS](part-02.md#c06-i0173)
- [FROMKEY / TOKEY](part-02.md#c06-i0174)
- [FROMNUMBER / TONUMBER](part-02.md#c06-i0175)
- [INDATASET(name) / OUTDATASET(name)](part-02.md#c06-i0176)
- [INFILE(ddname) / OUTFILE(ddname)](part-02.md#c06-i0177)
- [INFILECOPY (カタログ複写)](part-02.md#c06-i0178)
- [MERGECAT / NOMERGECAT](part-02.md#c06-i0179)
- [REPLACE](part-02.md#c06-i0180)
- [REPRO 初期ロード](part-02.md#c06-i0181)
- [REPRO 基本](part-02.md#c06-i0182)
- [REUSE (REPRO)](part-02.md#c06-i0183)
- [SKIP(n)](part-02.md#c06-i0184)

### RMM

- [DFSMSrmm 概要](part-02.md#c06-i0185)
- [RMM ADDRACK](part-02.md#c06-i0186)
- [RMM ADDVOLUME / DELETEVOLUME](part-02.md#c06-i0187)
- [RMM CHANGERACK](part-02.md#c06-i0188)
- [RMM CHANGEVOLUME](part-02.md#c06-i0189)
- [RMM LISTDATASET](part-02.md#c06-i0190)
- [RMM LISTVOLUME](part-02.md#c06-i0191)
- [Vital Record Specification (VRS)](part-02.md#c06-i0192)

### SMS_DATACLAS

- [Compaction](part-02.md#c06-i0193)
- [DSORG](part-02.md#c06-i0194)
- [Data Class 概要](part-02.md#c06-i0195)
- [Extended Addressability (EA)](part-02.md#c06-i0196)
- [Extended Format](part-02.md#c06-i0197)
- [Imbed/Replicate (廃止)](part-02.md#c06-i0198)
- [RECFM / LRECL / BLKSIZE](part-02.md#c06-i0199)
- [Reuse](part-02.md#c06-i0200)
- [Space Allocation (Avg / Primary / Secondary)](part-02.md#c06-i0201)
- [VSAM CISZ / KEYS / FREESPACE / SHAREOPTIONS](part-02.md#c06-i0202)
- [Volume Count](part-02.md#c06-i0203)

### SMS_MGMTCLAS

- [# GDG Elements on Primary](part-02.md#c06-i0204)
- [Admin or User Command Backup](part-02.md#c06-i0205)
- [Backup Frequency](part-02.md#c06-i0206)
- [Command or Auto Migrate](part-02.md#c06-i0207)
- [Expire after Date/Days](part-02.md#c06-i0208)
- [Expire after Days Non-usage](part-02.md#c06-i0209)
- [Level 1 Days Non-usage](part-02.md#c06-i0210)
- [Management Class 概要](part-02.md#c06-i0211)
- [Number of Backup Versions](part-02.md#c06-i0212)
- [Primary Days Non-usage](part-02.md#c06-i0213)
- [Retain Days Only Backup Version](part-02.md#c06-i0214)
- [Retention Limit](part-02.md#c06-i0215)
- [Rolled-off GDS Action](part-02.md#c06-i0216)

### SMS_STORCLAS

- [Accessibility](part-02.md#c06-i0217)
- [Availability](part-02.md#c06-i0218)
- [CF Cache / CF Lock Set](part-02.md#c06-i0219)
- [Direct Millisecond Response](part-02.md#c06-i0220)
- [Guaranteed Space](part-02.md#c06-i0221)
- [Guaranteed Synchronous Write](part-02.md#c06-i0222)
- [Initial Access Response Seconds](part-02.md#c06-i0223)
- [Sequential Millisecond Response](part-02.md#c06-i0224)
- [Storage Class 概要](part-02.md#c06-i0225)
- [Sustained Data Rate](part-02.md#c06-i0226)

### SMS_STORGRP

- [Allocation/Migration System ID](part-02.md#c06-i0227)
- [Auto Migrate / Auto Backup / Auto Dump](part-02.md#c06-i0228)
- [DUMMY](part-02.md#c06-i0229)
- [Migrate Threshold (Low/High)](part-02.md#c06-i0230)
- [OBJECT / OBJECT BACKUP タイプ](part-02.md#c06-i0231)
- [POOL タイプ](part-02.md#c06-i0232)
- [Storage Group 概要](part-02.md#c06-i0233)
- [TAPE タイプ](part-02.md#c06-i0234)
- [VIO タイプ](part-02.md#c06-i0235)

### VERIFY

- [VERIFY DATASET(name)](part-02.md#c06-i0236)
- [VERIFY 効果](part-02.md#c06-i0237)
- [VERIFY 基本](part-02.md#c06-i0238)

### VSAM_CONCEPTS

- [AMP パラメータ (JCL)](part-02.md#c06-i0239)
- [BUFND / BUFNI](part-02.md#c06-i0240)
- [CI スプリット / CA スプリット](part-02.md#c06-i0241)
- [Control Area (CA)](part-02.md#c06-i0242)
- [Control Interval (CI)](part-02.md#c06-i0243)
- [Extended Format VSAM](part-02.md#c06-i0244)
- [HURBA / HARBA](part-02.md#c06-i0245)
- [Reorganization (再編成)](part-02.md#c06-i0246)
- [Sequence Set / Index Set](part-02.md#c06-i0247)
- [Spanned Record と SPANNED 属性](part-02.md#c06-i0248)
- [VSAM RLS (Record Level Sharing)](part-02.md#c06-i0249)
- [VSAM TVS (Transactional VSAM)](part-02.md#c06-i0250)

### その他

- [その他](part-02.md#c06-other)