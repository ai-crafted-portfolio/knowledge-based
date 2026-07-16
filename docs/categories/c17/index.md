# JCL DD 文

<div class="kb-cov" markdown>

**技術項目 262 件**  ／  QA対応 254（96.95%・不足 8）  ／  手順対応 258（98.47%・不足 4）

</div>

このカテゴリでは技術項目 262 件を掲載し、確認問題 432 問・検証手順 307 件を項目ごとに紐づけています。対応率は技術項目に明示的に対応付けられた件数で算出しています（増補継続中）。


> 最終更新: 2026-07-16


## 収録項目


### AMP

- [AMP=('BUFND=n')](part-01.md#c17-i0001)
- [AMP=('BUFNI=n')](part-01.md#c17-i0002)
- [AMP=('BUFSP=n')](part-01.md#c17-i0003)
- [AMP=('CROPS=xxx')](part-01.md#c17-i0004)
- [AMP=('RECFM=...')](part-01.md#c17-i0005)
- [AMP=('STRNO=n')](part-01.md#c17-i0006)
- [AMP=('SYNAD=...')](part-01.md#c17-i0007)
- [AMP=('TRACE')](part-01.md#c17-i0008)
- [AMP=AMORG](part-01.md#c17-i0009)

### DCB-RECFM

- [RECFM=D](part-01.md#c17-i0010)
- [RECFM=F](part-01.md#c17-i0011)
- [RECFM=FB](part-01.md#c17-i0012)
- [RECFM=FBA](part-01.md#c17-i0013)
- [RECFM=FBM](part-01.md#c17-i0014)
- [RECFM=T (トラック上書き)](part-01.md#c17-i0015)
- [RECFM=U](part-01.md#c17-i0016)
- [RECFM=V](part-01.md#c17-i0017)
- [RECFM=VB](part-01.md#c17-i0018)
- [RECFM=VBA](part-01.md#c17-i0019)
- [RECFM=VBS](part-01.md#c17-i0020)
- [RECFM=VBSA](part-01.md#c17-i0021)

### DCB-参照

- [DCB 属性の解決順序](part-01.md#c17-i0022)
- [DCB=(*.step.dd,RECFM=FB)](part-01.md#c17-i0023)
- [DCB=(dsname)](part-01.md#c17-i0024)
- [DCB=*.stepname.ddname](part-01.md#c17-i0025)
- [LIKE=dsname](part-01.md#c17-i0026)
- [REFDD=*.step.dd](part-01.md#c17-i0027)

### DCB-属性

- [BLKSIZE 上限 32760 (非拡張)](part-01.md#c17-i0028)
- [BLKSIZE 明示指定](part-01.md#c17-i0029)
- [BLKSIZE=0 (システム決定)](part-01.md#c17-i0030)
- [BUFL=n](part-01.md#c17-i0031)
- [BUFNO=n](part-01.md#c17-i0032)
- [BUFOFF=L](part-01.md#c17-i0033)
- [DSORG=DA](part-01.md#c17-i0034)
- [DSORG=IS](part-01.md#c17-i0035)
- [DSORG=PO](part-01.md#c17-i0036)
- [DSORG=PS](part-01.md#c17-i0037)
- [DSORG=PSU/POU (Unmovable)](part-01.md#c17-i0038)
- [DSORG=VS](part-01.md#c17-i0039)
- [KEYLEN=n](part-01.md#c17-i0040)
- [LRECL=133](part-01.md#c17-i0041)
- [LRECL=137](part-01.md#c17-i0042)
- [LRECL=255 (可変長)](part-01.md#c17-i0043)
- [LRECL=32760](part-01.md#c17-i0044)
- [LRECL=80](part-01.md#c17-i0045)
- [LRECL=X (スパンド)](part-01.md#c17-i0046)
- [NCP=n](part-01.md#c17-i0047)
- [OPTCD=C (連鎖スケジューリング)](part-01.md#c17-i0048)
- [OPTCD=J (3800 印刷)](part-01.md#c17-i0049)
- [OPTCD=Q (ASCII 変換)](part-01.md#c17-i0050)
- [OPTCD=W (書込検証)](part-01.md#c17-i0051)
- [RKP=n](part-01.md#c17-i0052)

### DISP-典型

- [DISP=(MOD,CATLG,DELETE)](part-01.md#c17-i0053)
- [DISP=(NEW,CATLG,DELETE)](part-01.md#c17-i0054)
- [DISP=(NEW,CATLG,KEEP)](part-01.md#c17-i0055)
- [DISP=(NEW,PASS)](part-01.md#c17-i0056)
- [DISP=(OLD,DELETE)](part-01.md#c17-i0057)
- [DISP=(OLD,KEEP)](part-01.md#c17-i0058)
- [DISP=(OLD,PASS)](part-01.md#c17-i0059)
- [DISP=SHR (単独)](part-01.md#c17-i0060)

### DISP-正常

- [正常終了 CATLG](part-01.md#c17-i0061)
- [正常終了 DELETE](part-01.md#c17-i0062)
- [正常終了 KEEP](part-01.md#c17-i0063)
- [正常終了 PASS](part-01.md#c17-i0064)
- [正常終了 UNCATLG](part-01.md#c17-i0065)
- [正常終了 省略時の既定](part-01.md#c17-i0066)

### DISP-状態

- [DISP 省略時の既定](part-01.md#c17-i0067)
- [DISP 第 1 サブパラメータ省略](part-01.md#c17-i0068)
- [DISP=MOD](part-01.md#c17-i0069)
- [DISP=NEW](part-01.md#c17-i0070)
- [DISP=OLD](part-01.md#c17-i0071)
- [DISP=SHR](part-01.md#c17-i0072)

### DISP-異常

- [異常終了 CATLG](part-01.md#c17-i0073)
- [異常終了 DELETE](part-01.md#c17-i0074)
- [異常終了 KEEP](part-01.md#c17-i0075)
- [異常終了 UNCATLG](part-01.md#c17-i0076)
- [異常終了 省略時の既定](part-01.md#c17-i0077)

### DSN

- [&&NAME 同一ジョブ後続参照](part-01.md#c17-i0078)
- [44 文字制限](part-01.md#c17-i0079)
- [DSN 引用 ('...')](part-01.md#c17-i0080)
- [DSN 省略 (純粋な一時)](part-01.md#c17-i0081)
- [DSN= 基本構文](part-01.md#c17-i0082)
- [DSN=&&NAME (一時データセット, 二重アンパサンド)](part-01.md#c17-i0083)
- [DSN=NULLFILE](part-01.md#c17-i0084)
- [DSN=lib(*) 全メンバー](part-01.md#c17-i0085)
- [DSN=lib(member) メンバー指定](part-01.md#c17-i0086)
- [GDG 同一ジョブ内番号固定](part-01.md#c17-i0087)
- [GDG 相対指定 (+1)](part-01.md#c17-i0088)
- [GDG 相対指定 (-1)](part-01.md#c17-i0089)
- [GDG 相対指定 (0)](part-01.md#c17-i0090)
- [GDG 絶対世代名 G0001V00](part-01.md#c17-i0091)
- [システム生成一時 DSN 名](part-01.md#c17-i0092)
- [ノード命名規則](part-01.md#c17-i0093)
- [後方参照 *.procstepname.stepname.ddname](part-01.md#c17-i0094)
- [後方参照 *.stepname.ddname](part-01.md#c17-i0095)
- [絶対修飾名 (fully qualified)](part-01.md#c17-i0096)

### DUMMY

- [DSN=NULLFILE と DUMMY](part-01.md#c17-i0097)
- [DUMMY と DCB 併用](part-01.md#c17-i0098)
- [DUMMY 入力時の挙動](part-01.md#c17-i0099)
- [DUMMY 出力時の挙動](part-01.md#c17-i0100)

### LABEL

- [LABEL=(seq,AL)](part-01.md#c17-i0101)
- [LABEL=(seq,AUL)](part-01.md#c17-i0102)
- [LABEL=(seq,BLP)](part-01.md#c17-i0103)
- [LABEL=(seq,LTM)](part-01.md#c17-i0104)
- [LABEL=(seq,NL)](part-01.md#c17-i0105)
- [LABEL=(seq,NSL)](part-01.md#c17-i0106)
- [LABEL=(seq,SL)](part-01.md#c17-i0107)
- [LABEL=(seq,SUL)](part-01.md#c17-i0108)
- [LABEL=,EXPDT=日付](part-01.md#c17-i0109)
- [LABEL=,IN/OUT](part-01.md#c17-i0110)
- [LABEL=,PASSWORD](part-01.md#c17-i0111)
- [LABEL=,RETPD=日数](part-01.md#c17-i0112)
- [ファイル順序番号 (1〜9999)](part-01.md#c17-i0113)

### OUTPUT-分割

- [SEGMENT と SPIN の関係](part-01.md#c17-i0114)
- [SEGMENT=ページ数](part-01.md#c17-i0115)

### OUTPUT-参照

- [OUTPUT カード自体](part-01.md#c17-i0116)
- [OUTPUT=(*.ref1,*.ref2)](part-01.md#c17-i0117)
- [OUTPUT=*.OUTDD](part-01.md#c17-i0118)

### SMS

- [ACS ルーチンによる強制](part-01.md#c17-i0119)
- [AVGREC を SMS 文脈で](part-01.md#c17-i0120)
- [DATACLAS=データクラス](part-01.md#c17-i0121)
- [MGMTCLAS=管理クラス](part-01.md#c17-i0122)
- [SMS 環境下の DISP/UNIT/VOL](part-01.md#c17-i0123)
- [STORCLAS=ストレージクラス](part-01.md#c17-i0124)

### SPACE-例

- [SPACE=(CYL,(10,5))](part-01.md#c17-i0125)
- [SPACE=(CYL,(50,10),RLSE)](part-01.md#c17-i0126)
- [SPACE=(TRK,(100,20,5))](part-01.md#c17-i0127)

### SPACE-単位

- [SPACE=(BLK,...)](part-01.md#c17-i0128)
- [SPACE=(CYL,...)](part-01.md#c17-i0129)
- [SPACE=(TRK,...)](part-01.md#c17-i0130)
- [SPACE=(reclen,...)](part-01.md#c17-i0131)

### SPACE-属性

- [AVGREC=U/K/M](part-01.md#c17-i0132)
- [SPACE=,ALX 最大 5 領域](part-01.md#c17-i0133)
- [SPACE=,CONTIG](part-01.md#c17-i0134)
- [SPACE=,MXIG 最大空き割振り](part-01.md#c17-i0135)
- [SPACE=,RLSE](part-01.md#c17-i0136)
- [SPACE=,ROUND](part-01.md#c17-i0137)

### SPACE-量

- [Directory blocks (PDS)](part-01.md#c17-i0138)
- [Primary 一次割振り](part-01.md#c17-i0139)
- [Secondary 二次割振り](part-01.md#c17-i0140)

### SUBSYS

- [SUBSYS と DSN/UNIT 同居](part-01.md#c17-i0141)
- [SUBSYS=(name,parm1,parm2,...)](part-01.md#c17-i0142)
- [SUBSYS=サブシステム名](part-01.md#c17-i0143)

### SYSOUT

- [SYSOUT 出力経路選択](part-01.md#c17-i0144)
- [SYSOUT=(class,,code) コード指定](part-01.md#c17-i0145)
- [SYSOUT=(class,form)](part-01.md#c17-i0146)
- [SYSOUT=(class,writer)](part-01.md#c17-i0147)
- [SYSOUT=*](part-01.md#c17-i0148)
- [SYSOUT=A](part-01.md#c17-i0149)

### SYSOUT-付属

- [COPIES=(N,(g1,g2,...))](part-01.md#c17-i0150)
- [COPIES=N](part-01.md#c17-i0151)
- [DEST=ノード](part-01.md#c17-i0152)
- [DEST=ノード.ユーザ](part-01.md#c17-i0153)
- [FCB=書式制御](part-01.md#c17-i0154)
- [FORMS=帳票番号](part-01.md#c17-i0155)
- [FREE=CLOSE](part-01.md#c17-i0156)
- [FREE=END](part-02.md#c17-i0157)
- [HOLD=NO](part-02.md#c17-i0158)
- [HOLD=YES](part-02.md#c17-i0159)
- [OUTLIM=n](part-02.md#c17-i0160)
- [SPIN=UNALLOC](part-02.md#c17-i0161)
- [UCS=印字盤](part-02.md#c17-i0162)

### UNIT

- [UNIT 省略時の解決](part-02.md#c17-i0163)
- [UNIT=(SYSDA,2)](part-02.md#c17-i0164)
- [UNIT=(unit,,DEFER)](part-02.md#c17-i0165)
- [UNIT=(unit,,P) 並列マウント](part-02.md#c17-i0166)
- [UNIT=(unit,count)](part-02.md#c17-i0167)
- [UNIT=3390](part-02.md#c17-i0168)
- [UNIT=3480](part-02.md#c17-i0169)
- [UNIT=3490](part-02.md#c17-i0170)
- [UNIT=AFF=ddname (装置親近性)](part-02.md#c17-i0171)
- [UNIT=CART](part-02.md#c17-i0172)
- [UNIT=SYSALLDA](part-02.md#c17-i0173)
- [UNIT=SYSDA](part-02.md#c17-i0174)
- [UNIT=TAPE](part-02.md#c17-i0175)
- [UNIT=device-address (例 180)](part-02.md#c17-i0176)

### USS-PATH

- [FILEDATA=BINARY](part-02.md#c17-i0177)
- [FILEDATA=RECORD](part-02.md#c17-i0178)
- [FILEDATA=TEXT](part-02.md#c17-i0179)
- [PATH='/path/to/file'](part-02.md#c17-i0180)
- [PATHDISP 第 2 引数 (異常)](part-02.md#c17-i0181)
- [PATHDISP=DELETE](part-02.md#c17-i0182)
- [PATHDISP=KEEP](part-02.md#c17-i0183)
- [PATHMODE 8 進指定](part-02.md#c17-i0184)
- [PATHMODE 記号指定](part-02.md#c17-i0185)
- [PATHOPTS=OAPPEND](part-02.md#c17-i0186)
- [PATHOPTS=OCREAT](part-02.md#c17-i0187)
- [PATHOPTS=OEXCL](part-02.md#c17-i0188)
- [PATHOPTS=ONOCTTY](part-02.md#c17-i0189)
- [PATHOPTS=ONONBLOCK](part-02.md#c17-i0190)
- [PATHOPTS=ORDONLY](part-02.md#c17-i0191)
- [PATHOPTS=ORDWR](part-02.md#c17-i0192)
- [PATHOPTS=OSYNC](part-02.md#c17-i0193)
- [PATHOPTS=OTRUNC](part-02.md#c17-i0194)
- [PATHOPTS=OWRONLY](part-02.md#c17-i0195)

### VOL

- [VOL 完全位置取り例 VOL=(PRIVATE,RETAIN,1,5,SER=...)](part-02.md#c17-i0196)
- [VOL=,,,vol-count](part-02.md#c17-i0197)
- [VOL=,,seq-no](part-02.md#c17-i0198)
- [VOL=PRIVATE](part-02.md#c17-i0199)
- [VOL=REF=*.stepname.ddname](part-02.md#c17-i0200)
- [VOL=REF=dsname](part-02.md#c17-i0201)
- [VOL=RETAIN](part-02.md#c17-i0202)
- [VOL=SER=(v1,v2,v3)](part-02.md#c17-i0203)
- [VOL=SER=volser](part-02.md#c17-i0204)

### その他

- [ACCODE=テープアクセスコード](part-02.md#c17-i0205)
- [BUFOFF (DCB 系再掲)](part-02.md#c17-i0206)
- [CCSID=コード化文字セット ID](part-02.md#c17-i0207)
- [CHKPT=EOV](part-02.md#c17-i0208)
- [COMPACTION=テープ圧縮](part-02.md#c17-i0209)
- [DDNAME=参照](part-02.md#c17-i0210)
- [DSNTYPE=BASIC](part-02.md#c17-i0211)
- [DSNTYPE=EXTREQ / EXTPREF](part-02.md#c17-i0212)
- [DSNTYPE=HFS](part-02.md#c17-i0213)
- [DSNTYPE=LIBRARY (PDSE)](part-02.md#c17-i0214)
- [DSNTYPE=PDS](part-02.md#c17-i0215)
- [DSNTYPE=PIPE](part-02.md#c17-i0216)
- [FREE=CLOSE / END](part-02.md#c17-i0217)
- [FREEVOL=EOV](part-02.md#c17-i0218)
- [KEYOFF=n](part-02.md#c17-i0219)
- [LGSTREAM=名前](part-02.md#c17-i0220)
- [PROTECT=YES](part-02.md#c17-i0221)
- [QNAME=ddname](part-02.md#c17-i0222)
- [RECORG=KS/ES/RR/LS](part-02.md#c17-i0223)
- [RLS=NRI/CR/CRE](part-02.md#c17-i0224)
- [SECMODEL=(profile)](part-02.md#c17-i0225)
- [TERM=TS](part-02.md#c17-i0226)

### インライン

- [/* (デフォルトデリミタ)](part-02.md#c17-i0227)
- [DD *](part-02.md#c17-i0228)
- [DD DATA](part-02.md#c17-i0229)
- [DLM=delimiter](part-02.md#c17-i0230)
- [インライン DCB の既定値](part-02.md#c17-i0231)
- [次の // でも終了](part-02.md#c17-i0232)

### 保持期間

- [EXPDT と RETPD の関係](part-02.md#c17-i0233)
- [EXPDT=1999/365 (永久)](part-02.md#c17-i0234)
- [EXPDT=YYDDD (旧形式)](part-02.md#c17-i0235)
- [EXPDT=YYYY/DDD (4 桁年)](part-02.md#c17-i0236)
- [RETPD=日数](part-02.md#c17-i0237)

### 印刷

- [BURST=NO](part-02.md#c17-i0238)
- [BURST=YES](part-02.md#c17-i0239)
- [CHARS=(c1,c2,c3,c4)](part-02.md#c17-i0240)
- [CHARS=文字セット名](part-02.md#c17-i0241)
- [FLASH=(form,count)](part-02.md#c17-i0242)
- [FLASH=オーバーレイ](part-02.md#c17-i0243)
- [MODIFY=(module,trc)](part-02.md#c17-i0244)
- [MODIFY=コピー修整モジュール](part-02.md#c17-i0245)

### 横断ルール

- [DD の継続行](part-02.md#c17-i0246)
- [DD 文の位置パラメータ vs キーワード](part-02.md#c17-i0247)
- [DD 文最大数](part-02.md#c17-i0248)
- [DD 省略時のジョブ失敗ケース](part-02.md#c17-i0249)
- [GDG とジョブ別世代](part-02.md#c17-i0250)
- [GDG モデル DSCB](part-02.md#c17-i0251)
- [JCL 標準コーディング順序](part-02.md#c17-i0252)
- [コメント (//*)](part-02.md#c17-i0253)
- [属性解決順序まとめ](part-02.md#c17-i0254)

### 連結

- [BLKSIZE 順序 (先頭最大)](part-02.md#c17-i0255)
- [DD 連結 (DDname 省略)](part-02.md#c17-i0256)
- [DSORG 一致](part-02.md#c17-i0257)
- [PDS 連結 (Library 連結)](part-02.md#c17-i0258)
- [RECFM 一致](part-02.md#c17-i0259)
- [SYSOUT 連結](part-02.md#c17-i0260)
- [インストリーム連結](part-02.md#c17-i0261)
- [連結深さ上限](part-02.md#c17-i0262)

### その他

- [その他](part-02.md#c17-other)