---
search:
  exclude: true
---

# JES2 — 詳細 (2/2)

[← JES2 の概要へ戻る](index.md)


## その他


<section class="kb-item" id="c21-other"><h3>その他（特定項目に紐づかないQA・手順）</h3><p class="kb-meta">項目名が個別の技術項目に一致しなかったQA・手順です。</p><details class="kb-block"><summary>検証手順（318件）</summary><div class="kb-p"><p class="kb-pname"><strong>$D コマンドの位置付け 追加確認手順</strong></p><p>検証目的: コマンドの位置付け確認（表示値）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、コマンドの位置付け確認（表示値）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・実行中ジョブ表示確認（状態語）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、基本動作・実行中ジョブ表示確認（状態語）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA L 長形式 追加確認手順</strong></p><p>検証目的: 長形式・実行中ジョブ表示確認（資源名）について、ジョブ状態表示の応答に$HASP890とJOBAが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOB(JOBA),CONJOBS を入力し、JES2応答で$HASP890とJOBAを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOB(JOBA),CONJOBS を入力し、長形式・実行中ジョブ表示確認（資源名）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
入力欄に /$D JOB(JOBA),CONJOBS が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOB(JOBA),CONJOBS の応答から、$HASP890とJOBAを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
$HASP890 と JOBA が表示されていれば、ジョブ状態表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP890とJOBAを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
保存対象の出力に $HASP890 と JOBA が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D JOB(JOBA),CONJOBS を入力していること
② ステップ2で $HASP890 を確認していること
③ ステップ3で JOBA を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI n 個別表示 追加確認手順</strong></p><p>検証目的: 個別表示・イニシエータ表示確認（定義値）について、イニシエータ定義表示の応答に$HASP468とPARTNUMが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INITDEF を入力し、JES2応答で$HASP468とPARTNUMを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INITDEF を入力し、個別表示・イニシエータ表示確認（定義値）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INITDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INITDEF
入力欄に /$D INITDEF が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INITDEF の応答から、$HASP468とPARTNUMを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
$HASP468 と PARTNUM が表示されていれば、イニシエータ定義表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP468とPARTNUMを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
保存対象の出力に $HASP468 と PARTNUM が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D INITDEF を入力していること
② ステップ2で $HASP468 を確認していること
③ ステップ3で PARTNUM を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DMASDEF 追加確認手順</strong></p><p>検証目的: 共有構成・共有構成定義表示確認（応答行）について、チェックポイント表示の応答に$HASP829とCKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF,CKPT1,CKPT2 を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF,CKPT1,CKPT2 を入力し、共有構成・共有構成定義表示確認（応答行）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
入力欄に /$D CKPTDEF,CKPT1,CKPT2 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF,CKPT1,CKPT2 の応答から、$HASP829とCKPT1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 と CKPT1 が表示されていれば、チェックポイント表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP829とCKPT1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
保存対象の出力に $HASP829 と CKPT1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CKPTDEF,CKPT1,CKPT2 を入力していること
② ステップ2で $HASP829 を確認していること
③ ステップ3で CKPT1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DNODE n 追加確認手順</strong></p><p>検証目的: ノード表示・ノード確認（操作範囲）について、NJE接続表示の応答に$HASP815とREMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、ノード表示・ノード確認（操作範囲）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
入力欄に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 の応答から、$HASP815とREMOTE1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE接続表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP815とREMOTE1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
保存対象の出力に $HASP815 と REMOTE1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力していること
② ステップ2で $HASP815 を確認していること
③ ステップ3で REMOTE1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPRT 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・プリンタ・プリンタ表示確認（保存粒度）について、出力クラス表示の応答に$HASP842とOUTCLASS(A)が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS(A) を入力し、JES2応答で$HASP842とOUTCLASS(A)を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS(A) を入力し、基本動作・プリンタ・プリンタ表示確認（保存粒度）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
入力欄に /$D OUTCLASS(A) が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS(A) の応答から、$HASP842とOUTCLASS(A)を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
$HASP842 と OUTCLASS(A) が表示されていれば、出力クラス表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP842とOUTCLASS(A)を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
保存対象の出力に $HASP842 と OUTCLASS(A) が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D OUTCLASS(A) を入力していること
② ステップ2で $HASP842 を確認していること
③ ステップ3で OUTCLASS(A) を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$D コマンドの権限 追加確認手順</strong></p><p>検証目的: コマンドの権限確認（変更前確認）について、ネットワーク装置表示の応答に$HASP899とNETDEV1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D NETWORK を入力し、JES2応答で$HASP899とNETDEV1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D NETWORK を入力し、コマンドの権限確認（変更前確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D NETWORK
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D NETWORK
入力欄に /$D NETWORK が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D NETWORK の応答から、$HASP899とNETDEV1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
$HASP899 と NETDEV1 が表示されていれば、ネットワーク装置表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP899とNETDEV1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
保存対象の出力に $HASP899 と NETDEV1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D NETWORK を入力していること
② ステップ2で $HASP899 を確認していること
③ ステップ3で NETDEV1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ L 長形式 追加確認手順</strong></p><p>検証目的: 長形式・ジョブキュー表示確認（障害調査）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、長形式・ジョブキュー表示確認（障害調査）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA jobname 個別表示 追加確認手順</strong></p><p>検証目的: 個別表示・名前指定・実行中ジョブ表示確認（初期化定義）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、個別表示・名前指定・実行中ジョブ表示確認（初期化定義）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA STC のみ 追加確認手順</strong></p><p>検証目的: み・実行中ジョブ表示確認（運用証跡）について、ジョブ状態表示の応答に$HASP890とJOBAが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOB(JOBA),CONJOBS を入力し、JES2応答で$HASP890とJOBAを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOB(JOBA),CONJOBS を入力し、み・実行中ジョブ表示確認（運用証跡）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
入力欄に /$D JOB(JOBA),CONJOBS が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOB(JOBA),CONJOBS の応答から、$HASP890とJOBAを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
$HASP890 と JOBA が表示されていれば、ジョブ状態表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP890とJOBAを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
保存対象の出力に $HASP890 と JOBA が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D JOB(JOBA),CONJOBS を入力していること
② ステップ2で $HASP890 を確認していること
③ ステップ3で JOBA を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI と WLM 管理イニシエータ 追加確認手順</strong></p><p>検証目的: 管理イニシエータ・ワークロード管理・イニシエータ表示確認（メッセージ照合）について、イニシエータ定義表示の応答に$HASP468とPARTNUMが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INITDEF を入力し、JES2応答で$HASP468とPARTNUMを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INITDEF を入力し、管理イニシエータ・ワークロード管理・イニシエータ表示確認（メッセージ照合）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INITDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INITDEF
入力欄に /$D INITDEF が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INITDEF の応答から、$HASP468とPARTNUMを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
$HASP468 と PARTNUM が表示されていれば、イニシエータ定義表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP468とPARTNUMを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
保存対象の出力に $HASP468 と PARTNUM が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D INITDEF を入力していること
② ステップ2で $HASP468 を確認していること
③ ステップ3で PARTNUM を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DCKPTDEF 追加確認手順</strong></p><p>検証目的: チェックポイント定義表示確認（対象範囲）について、チェックポイント表示の応答に$HASP829とCKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF,CKPT1,CKPT2 を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF,CKPT1,CKPT2 を入力し、チェックポイント定義表示確認（対象範囲）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
入力欄に /$D CKPTDEF,CKPT1,CKPT2 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF,CKPT1,CKPT2 の応答から、$HASP829とCKPT1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 と CKPT1 が表示されていれば、チェックポイント表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP829とCKPT1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
保存対象の出力に $HASP829 と CKPT1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CKPTDEF,CKPT1,CKPT2 を入力していること
② ステップ2で $HASP829 を確認していること
③ ステップ3で CKPT1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S LINE n 追加確認手順</strong></p><p>検証目的: 回線・開始操作確認（影響確認）について、NJE接続表示の応答に$HASP815とREMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、回線・開始操作確認（影響確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
入力欄に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 の応答から、$HASP815とREMOTE1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE接続表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP815とREMOTE1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
保存対象の出力に $HASP815 と REMOTE1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力していること
② ステップ2で $HASP815 を確認していること
③ ステップ3で REMOTE1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPRT L 長形式 追加確認手順</strong></p><p>検証目的: 長形式・プリンタ・プリンタ表示確認（復旧確認）について、出力クラス表示の応答に$HASP842とOUTCLASS(A)が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS(A) を入力し、JES2応答で$HASP842とOUTCLASS(A)を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS(A) を入力し、長形式・プリンタ・プリンタ表示確認（復旧確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
入力欄に /$D OUTCLASS(A) が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS(A) の応答から、$HASP842とOUTCLASS(A)を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
$HASP842 と OUTCLASS(A) が表示されていれば、出力クラス表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP842とOUTCLASS(A)を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
保存対象の出力に $HASP842 と OUTCLASS(A) が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D OUTCLASS(A) を入力していること
② ステップ2で $HASP842 を確認していること
③ ステップ3で OUTCLASS(A) を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$D 応答の宛先 追加確認手順</strong></p><p>検証目的: 応答の宛先確認（クラス判定）について、ネットワーク装置表示の応答に$HASP899とNETDEV1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D NETWORK を入力し、JES2応答で$HASP899とNETDEV1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D NETWORK を入力し、応答の宛先確認（クラス判定）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D NETWORK
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D NETWORK
入力欄に /$D NETWORK が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D NETWORK の応答から、$HASP899とNETDEV1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
$HASP899 と NETDEV1 が表示されていれば、ネットワーク装置表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP899とNETDEV1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
保存対象の出力に $HASP899 と NETDEV1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D NETWORK を入力していること
② ステップ2で $HASP899 を確認していること
③ ステップ3で NETDEV1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DRDR 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・リーダ・リーダ表示確認（経路確認）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、基本動作・リーダ・リーダ表示確認（経路確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・ジョブキュー表示確認（スプール確認）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、基本動作・ジョブキュー表示確認（スプール確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA TSU のみ 追加確認手順</strong></p><p>検証目的: み・実行中ジョブ表示確認（メンバー確認）について、ジョブ状態表示の応答に$HASP890とJOBAが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOB(JOBA),CONJOBS を入力し、JES2応答で$HASP890とJOBAを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOB(JOBA),CONJOBS を入力し、み・実行中ジョブ表示確認（メンバー確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
入力欄に /$D JOB(JOBA),CONJOBS が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOB(JOBA),CONJOBS の応答から、$HASP890とJOBAを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
$HASP890 と JOBA が表示されていれば、ジョブ状態表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP890とJOBAを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
保存対象の出力に $HASP890 と JOBA が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D JOB(JOBA),CONJOBS を入力していること
② ステップ2で $HASP890 を確認していること
③ ステップ3で JOBA を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPUN 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・パンチ・パンチ表示確認（出力制御）について、イニシエータ定義表示の応答に$HASP468とPARTNUMが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INITDEF を入力し、JES2応答で$HASP468とPARTNUMを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INITDEF を入力し、基本動作・パンチ・パンチ表示確認（出力制御）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INITDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INITDEF
入力欄に /$D INITDEF が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INITDEF の応答から、$HASP468とPARTNUMを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
$HASP468 と PARTNUM が表示されていれば、イニシエータ定義表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP468とPARTNUMを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
保存対象の出力に $HASP468 と PARTNUM が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D INITDEF を入力していること
② ステップ2で $HASP468 を確認していること
③ ステップ3で PARTNUM を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$E CKPTLOCK 追加確認手順</strong></p><p>検証目的: 再始動操作確認（ジョブ制御）について、チェックポイント表示の応答に$HASP829とCKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF,CKPT1,CKPT2 を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF,CKPT1,CKPT2 を入力し、再始動操作確認（ジョブ制御）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
入力欄に /$D CKPTDEF,CKPT1,CKPT2 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF,CKPT1,CKPT2 の応答から、$HASP829とCKPT1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 と CKPT1 が表示されていれば、チェックポイント表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP829とCKPT1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
保存対象の出力に $HASP829 と CKPT1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CKPTDEF,CKPT1,CKPT2 を入力していること
② ステップ2で $HASP829 を確認していること
③ ステップ3で CKPT1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T PRT n ROUTECDE= 追加確認手順</strong></p><p>検証目的: プリンタ・変更操作確認（起動条件）について、NJE接続表示の応答に$HASP815とREMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、プリンタ・変更操作確認（起動条件）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
入力欄に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 の応答から、$HASP815とREMOTE1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE接続表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP815とREMOTE1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
保存対象の出力に $HASP815 と REMOTE1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力していること
② ステップ2で $HASP815 を確認していること
③ ステップ3で REMOTE1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DOUTCLASS c 追加確認手順</strong></p><p>検証目的: クラス・出力クラス表示確認（停止条件）について、出力クラス表示の応答に$HASP842とOUTCLASS(A)が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS(A) を入力し、JES2応答で$HASP842とOUTCLASS(A)を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS(A) を入力し、クラス・出力クラス表示確認（停止条件）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
入力欄に /$D OUTCLASS(A) が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS(A) の応答から、$HASP842とOUTCLASS(A)を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
$HASP842 と OUTCLASS(A) が表示されていれば、出力クラス表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP842とOUTCLASS(A)を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
保存対象の出力に $HASP842 と OUTCLASS(A) が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D OUTCLASS(A) を入力していること
② ステップ2で $HASP842 を確認していること
③ ステップ3で OUTCLASS(A) を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・イニシエータ表示確認（照会操作）について、ネットワーク装置表示の応答に$HASP899とNETDEV1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D NETWORK を入力し、JES2応答で$HASP899とNETDEV1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D NETWORK を入力し、基本動作・イニシエータ表示確認（照会操作）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D NETWORK
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D NETWORK
入力欄に /$D NETWORK が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D NETWORK の応答から、$HASP899とNETDEV1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
$HASP899 と NETDEV1 が表示されていれば、ネットワーク装置表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP899とNETDEV1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
保存対象の出力に $HASP899 と NETDEV1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D NETWORK を入力していること
② ステップ2で $HASP899 を確認していること
③ ステップ3で NETDEV1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPOOL 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・スプール・スプール表示確認（変更操作）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、基本動作・スプール・スプール表示確認（変更操作）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ jobname 追加確認手順</strong></p><p>検証目的: 名前指定・ジョブキュー表示確認（記録単位）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、名前指定・ジョブキュー表示確認（記録単位）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA 出力 $HASP100 追加確認手順</strong></p><p>検証目的: 出力・実行中ジョブ表示確認（比較観点）について、ジョブ状態表示の応答に$HASP890とJOBAが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOB(JOBA),CONJOBS を入力し、JES2応答で$HASP890とJOBAを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOB(JOBA),CONJOBS を入力し、出力・実行中ジョブ表示確認（比較観点）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
入力欄に /$D JOB(JOBA),CONJOBS が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOB(JOBA),CONJOBS の応答から、$HASP890とJOBAを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
$HASP890 と JOBA が表示されていれば、ジョブ状態表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP890とJOBAを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
保存対象の出力に $HASP890 と JOBA が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D JOB(JOBA),CONJOBS を入力していること
② ステップ2で $HASP890 を確認していること
③ ステップ3で JOBA を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・リリース操作確認（監査観点）について、イニシエータ定義表示の応答に$HASP468とPARTNUMが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INITDEF を入力し、JES2応答で$HASP468とPARTNUMを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INITDEF を入力し、基本動作・リリース操作確認（監査観点）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INITDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INITDEF
入力欄に /$D INITDEF が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INITDEF の応答から、$HASP468とPARTNUMを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
$HASP468 と PARTNUM が表示されていれば、イニシエータ定義表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP468とPARTNUMを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
保存対象の出力に $HASP468 と PARTNUM が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D INITDEF を入力していること
② ステップ2で $HASP468 を確認していること
③ ステップ3で PARTNUM を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T CKPTDEF など 追加確認手順</strong></p><p>検証目的: 変更操作確認（切戻し判断）について、チェックポイント表示の応答に$HASP829とCKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF,CKPT1,CKPT2 を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF,CKPT1,CKPT2 を入力し、変更操作確認（切戻し判断）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
入力欄に /$D CKPTDEF,CKPT1,CKPT2 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF,CKPT1,CKPT2 の応答から、$HASP829とCKPT1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 と CKPT1 が表示されていれば、チェックポイント表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP829とCKPT1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
保存対象の出力に $HASP829 と CKPT1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CKPTDEF,CKPT1,CKPT2 を入力していること
② ステップ2で $HASP829 を確認していること
③ ステップ3で CKPT1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T NODE n など 追加確認手順</strong></p><p>検証目的: ノード・変更操作確認（表示値）について、NJE接続表示の応答に$HASP815とREMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、ノード・変更操作確認（表示値）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
入力欄に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 の応答から、$HASP815とREMOTE1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE接続表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP815とREMOTE1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
保存対象の出力に $HASP815 と REMOTE1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力していること
② ステップ2で $HASP815 を確認していること
③ ステップ3で REMOTE1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$E PRT n 追加確認手順</strong></p><p>検証目的: プリンタ・再始動操作確認（状態語）について、出力クラス表示の応答に$HASP842とOUTCLASS(A)が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS(A) を入力し、JES2応答で$HASP842とOUTCLASS(A)を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS(A) を入力し、プリンタ・再始動操作確認（状態語）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
入力欄に /$D OUTCLASS(A) が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS(A) の応答から、$HASP842とOUTCLASS(A)を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
$HASP842 と OUTCLASS(A) が表示されていれば、出力クラス表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP842とOUTCLASS(A)を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
保存対象の出力に $HASP842 と OUTCLASS(A) が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D OUTCLASS(A) を入力していること
② ステップ2で $HASP842 を確認していること
③ ステップ3で OUTCLASS(A) を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI のクラス表示 追加確認手順</strong></p><p>検証目的: クラス表示・イニシエータ表示確認（資源名）について、ネットワーク装置表示の応答に$HASP899とNETDEV1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D NETWORK を入力し、JES2応答で$HASP899とNETDEV1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D NETWORK を入力し、クラス表示・イニシエータ表示確認（資源名）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D NETWORK
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D NETWORK
入力欄に /$D NETWORK が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D NETWORK の応答から、$HASP899とNETDEV1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
$HASP899 と NETDEV1 が表示されていれば、ネットワーク装置表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP899とNETDEV1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
保存対象の出力に $HASP899 と NETDEV1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D NETWORK を入力していること
② ステップ2で $HASP899 を確認していること
③ ステップ3で NETDEV1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPOOL L 長形式 追加確認手順</strong></p><p>検証目的: 長形式・スプール・スプール表示確認（定義値）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、長形式・スプール・スプール表示確認（定義値）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ Jnnn ジョブ番号指定 追加確認手順</strong></p><p>検証目的: ジョブ番号指定・ジョブキュー表示確認（応答行）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、ジョブ番号指定・ジョブキュー表示確認（応答行）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ Q 待機キューフィルタ 追加確認手順</strong></p><p>検証目的: 待機キューフィルタ・ジョブキュー表示確認（操作範囲）について、ジョブ状態表示の応答に$HASP890とJOBAが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOB(JOBA),CONJOBS を入力し、JES2応答で$HASP890とJOBAを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOB(JOBA),CONJOBS を入力し、待機キューフィルタ・ジョブキュー表示確認（操作範囲）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
入力欄に /$D JOB(JOBA),CONJOBS が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOB(JOBA),CONJOBS の応答から、$HASP890とJOBAを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
$HASP890 と JOBA が表示されていれば、ジョブ状態表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP890とJOBAを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
保存対象の出力に $HASP890 と JOBA が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D JOB(JOBA),CONJOBS を入力していること
② ステップ2で $HASP890 を確認していること
③ ステップ3で JOBA を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A &#x27;A&#x27; 全リリース 追加確認手順</strong></p><p>検証目的: 全リリース・リリース操作確認（保存粒度）について、イニシエータ定義表示の応答に$HASP468とPARTNUMが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INITDEF を入力し、JES2応答で$HASP468とPARTNUMを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INITDEF を入力し、全リリース・リリース操作確認（保存粒度）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INITDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INITDEF
入力欄に /$D INITDEF が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INITDEF の応答から、$HASP468とPARTNUMを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
$HASP468 と PARTNUM が表示されていれば、イニシエータ定義表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP468とPARTNUMを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
保存対象の出力に $HASP468 と PARTNUM が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D INITDEF を入力していること
② ステップ2で $HASP468 を確認していること
③ ステップ3で PARTNUM を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T MASDEF など 追加確認手順</strong></p><p>検証目的: 共有構成・変更操作確認（変更前確認）について、チェックポイント表示の応答に$HASP829とCKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF,CKPT1,CKPT2 を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF,CKPT1,CKPT2 を入力し、共有構成・変更操作確認（変更前確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
入力欄に /$D CKPTDEF,CKPT1,CKPT2 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF,CKPT1,CKPT2 の応答から、$HASP829とCKPT1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 と CKPT1 が表示されていれば、チェックポイント表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP829とCKPT1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
保存対象の出力に $HASP829 と CKPT1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CKPTDEF,CKPT1,CKPT2 を入力していること
② ステップ2で $HASP829 を確認していること
③ ステップ3で CKPT1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CONNECT ステートメント 追加確認手順</strong></p><p>検証目的: ネットワーク経路接続確認（障害調査）について、NJE接続表示の応答に$HASP815とREMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、ネットワーク経路接続確認（障害調査）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
入力欄に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 の応答から、$HASP815とREMOTE1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE接続表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP815とREMOTE1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
保存対象の出力に $HASP815 と REMOTE1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力していること
② ステップ2で $HASP815 を確認していること
③ ステップ3で REMOTE1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P PRT n 追加確認手順</strong></p><p>検証目的: プリンタ・停止操作確認（初期化定義）について、出力クラス表示の応答に$HASP842とOUTCLASS(A)が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS(A) を入力し、JES2応答で$HASP842とOUTCLASS(A)を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS(A) を入力し、プリンタ・停止操作確認（初期化定義）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
入力欄に /$D OUTCLASS(A) が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS(A) の応答から、$HASP842とOUTCLASS(A)を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
$HASP842 と OUTCLASS(A) が表示されていれば、出力クラス表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP842とOUTCLASS(A)を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
保存対象の出力に $HASP842 と OUTCLASS(A) が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D OUTCLASS(A) を入力していること
② ステップ2で $HASP842 を確認していること
③ ステップ3で OUTCLASS(A) を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DRDR n 個別表示 追加確認手順</strong></p><p>検証目的: 個別表示・リーダ・リーダ表示確認（運用証跡）について、ネットワーク装置表示の応答に$HASP899とNETDEV1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D NETWORK を入力し、JES2応答で$HASP899とNETDEV1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D NETWORK を入力し、個別表示・リーダ・リーダ表示確認（運用証跡）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D NETWORK
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D NETWORK
入力欄に /$D NETWORK が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D NETWORK の応答から、$HASP899とNETDEV1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
$HASP899 と NETDEV1 が表示されていれば、ネットワーク装置表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP899とNETDEV1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
保存対象の出力に $HASP899 と NETDEV1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D NETWORK を入力していること
② ステップ2で $HASP899 を確認していること
③ ステップ3で NETDEV1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPL VOL=ser 追加確認手順</strong></p><p>検証目的: スプール表示確認（メッセージ照合）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、スプール表示確認（メッセージ照合）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DQ 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・キュー集計表示確認（対象範囲）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、基本動作・キュー集計表示確認（対象範囲）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DQ クラス別カウント 追加確認手順</strong></p><p>検証目的: クラス別カウント・キュー集計表示確認（影響確認）について、ジョブ状態表示の応答に$HASP890とJOBAが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOB(JOBA),CONJOBS を入力し、JES2応答で$HASP890とJOBAを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOB(JOBA),CONJOBS を入力し、クラス別カウント・キュー集計表示確認（影響確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
入力欄に /$D JOB(JOBA),CONJOBS が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOB(JOBA),CONJOBS の応答から、$HASP890とJOBAを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
$HASP890 と JOBA が表示されていれば、ジョブ状態表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP890とJOBAを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D JOB(JOBA),CONJOBS
$HASP890 JOB(JOBA) JOB GROUP CONCURRENT JOB LIST
$HASP890 JOB NAME CONC JOB
$HASP890 JOBA JOBF
保存対象の出力に $HASP890 と JOBA が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D JOB(JOBA),CONJOBS を入力していること
② ステップ2で $HASP890 を確認していること
③ ステップ3で JOBA を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$H 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作・保留操作確認（復旧確認）について、イニシエータ定義表示の応答に$HASP468とPARTNUMが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INITDEF を入力し、JES2応答で$HASP468とPARTNUMを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INITDEF を入力し、基本動作・保留操作確認（復旧確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INITDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INITDEF
入力欄に /$D INITDEF が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INITDEF の応答から、$HASP468とPARTNUMを含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
$HASP468 と PARTNUM が表示されていれば、イニシエータ定義表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP468とPARTNUMを含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D INITDEF
$HASP468 INITDEF PARTNUM=10
保存対象の出力に $HASP468 と PARTNUM が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D INITDEF を入力していること
② ステップ2で $HASP468 を確認していること
③ ステップ3で PARTNUM を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF NEWCKPT1= 追加確認手順</strong></p><p>検証目的: 新第一チェックポイント・第一チェックポイント確認（クラス判定）について、チェックポイント表示の応答に$HASP829とCKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF,CKPT1,CKPT2 を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF,CKPT1,CKPT2 を入力し、新第一チェックポイント・第一チェックポイント確認（クラス判定）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
入力欄に /$D CKPTDEF,CKPT1,CKPT2 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF,CKPT1,CKPT2 の応答から、$HASP829とCKPT1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 と CKPT1 が表示されていれば、チェックポイント表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP829とCKPT1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CKPTDEF,CKPT1,CKPT2
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
保存対象の出力に $HASP829 と CKPT1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CKPTDEF,CKPT1,CKPT2 を入力していること
② ステップ2で $HASP829 を確認していること
③ ステップ3で CKPT1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT nnn ROUTINES= 追加確認手順</strong></p><p>検証目的: 出口確認（経路確認）について、NJE接続表示の応答に$HASP815とREMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力し、出口確認（経路確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
入力欄に /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 の応答から、$HASP815とREMOTE1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE接続表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP815とREMOTE1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1
$HASP815 CONNECT NODEA=ENDICOTT,MEMBERA=1,NODEB=REMOTE1
$HASP815 MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815 STATIC=YES,PATHMGR=YES
保存対象の出力に $HASP815 と REMOTE1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D CONNECT,NODEA=ENDICOTT,NODEB=REMOTE1 を入力していること
② ステップ2で $HASP815 を確認していること
③ ステップ3で REMOTE1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P PUN n 追加確認手順</strong></p><p>検証目的: パンチ・停止操作確認（スプール確認）について、出力クラス表示の応答に$HASP842とOUTCLASS(A)が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS(A) を入力し、JES2応答で$HASP842とOUTCLASS(A)を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS(A) を入力し、パンチ・停止操作確認（スプール確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
入力欄に /$D OUTCLASS(A) が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS(A) の応答から、$HASP842とOUTCLASS(A)を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
$HASP842 と OUTCLASS(A) が表示されていれば、出力クラス表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP842とOUTCLASS(A)を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D OUTCLASS(A)
$HASP842 OUTCLASS(A)
$HASP842 OUTCLASS(A) OUTPUT=PRINT,BLNKTRNC=YES,OUTDISP=(WRITE,WRITE)
$HASP842 TRKCELL=YES
保存対象の出力に $HASP842 と OUTCLASS(A) が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D OUTCLASS(A) を入力していること
② ステップ2で $HASP842 を確認していること
③ ステップ3で OUTCLASS(A) を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DT 基本動作 追加確認手順</strong></p><p>検証目的: 基本動作確認（メンバー確認）について、ネットワーク装置表示の応答に$HASP899とNETDEV1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D NETWORK を入力し、JES2応答で$HASP899とNETDEV1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D NETWORK を入力し、基本動作確認（メンバー確認）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D NETWORK
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D NETWORK
入力欄に /$D NETWORK が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D NETWORK の応答から、$HASP899とNETDEV1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
$HASP899 と NETDEV1 が表示されていれば、ネットワーク装置表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP899とNETDEV1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D NETWORK
$HASP899 $D NETWORK ACTIVE NETWORKING DEVICES
$HASP899 NAME STATUS
$HASP899 NETDEV1 ACTIVE
保存対象の出力に $HASP899 と NETDEV1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D NETWORK を入力していること
② ステップ2で $HASP899 を確認していること
③ ステップ3で NETDEV1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPOOLDEF 追加確認手順</strong></p><p>検証目的: スプール・スプール表示確認（出力制御）について、スプール使用量表示の応答に$HASP646とSPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOL を入力し、スプール・スプール表示確認（出力制御）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
入力欄に /$D SPOOL が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOL の応答から、$HASP646とSPOOL1を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP646 と SPOOL1 が表示されていれば、スプール使用量表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP646とSPOOL1を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D SPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
保存対象の出力に $HASP646 と SPOOL1 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D SPOOL を入力していること
② ステップ2で $HASP646 を確認していること
③ ステップ3で SPOOL1 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPRT n 個別表示 追加確認手順</strong></p><p>検証目的: 個別表示・プリンタ・プリンタ表示確認（ジョブ制御）について、重複ジョブ表示の応答に$HASP734とJOBT04が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2表示コマンドを送信でき、対象メンバー、権限、確認対象資源を変更管理上で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、JES2応答で$HASP734とJOBT04を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D DUPJOB,ACTIVE=YES,NUMBER を入力し、個別表示・プリンタ・プリンタ表示確認（ジョブ制御）の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
入力欄に /$D DUPJOB,ACTIVE=YES,NUMBER が表示されていれば、JES2へ送る表示コマンドを確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D DUPJOB,ACTIVE=YES,NUMBER の応答から、$HASP734とJOBT04を含む行を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
$HASP734 と JOBT04 が表示されていれば、重複ジョブ表示に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの出力一覧画面です。JES2応答を選択し、$HASP734とJOBT04を含む表示を保存対象として確認します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
COMMAND INPUT ===&gt; /$D DUPJOB,ACTIVE=YES,NUMBER
$HASP734 DUPJOB(JOBT04) NUMBER=5,ACTIVE=YES
保存対象の出力に $HASP734 と JOBT04 が含まれていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ1で /$D DUPJOB,ACTIVE=YES,NUMBER を入力していること
② ステップ2で $HASP734 を確認していること
③ ステップ3で JOBT04 を含む応答を保存対象として記録していること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2スプール使用率確認 手順</strong></p><p>検証目的: スプール使用率の机上応答を確認します。$D SPOOLに対して各スプールボリュームのSTATUSとPERCENT、$HASP646の合計使用率が読み取れることを確かめます。</p><p>前提条件: SDSFにログオン済みで、コマンド入力口から先頭 / を付けてJES2コマンドを机上確認できる前提です。実機ではスプール確認は変更管理の承認を得て、対象SSID、スプールボリューム名、使用率のしきい値、影響するジョブを確認してから実施します。</p><p>セッション環境: SDSFのコマンド入力口から /$D SPOOL を入力し、コマンド応答画面またはSDSF LOGで $HASP893、$HASP646、STATUS、PERCENT、ISSUER を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に先頭 / を付けて $D SPOOL を入力し、スプール使用率を確認するJES2コマンドを送信します。対象のSSIDと確認目的が合っているか見直します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL
COMMAND INPUT に /$D SPOOL が表示されていれば、机上例のスプール確認コマンドを実行する準備ができています。SPOOL の対象と目的が合っているか確認します。
――――
■ ステップ 2
現在の画面は $D SPOOL の応答を表示するSDSFのコマンド応答画面です。前ステップで送信したコマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、$HASP893 と $HASP646 の値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SDSF Command Response)
$HASP893 VOLUME(SPOOL1)  STATUS=ACTIVE,PERCENT=84
$HASP893 VOLUME(SPOOL2)  STATUS=ACTIVE,PERCENT=92
$HASP646 88.1904 PERCENT SPOOL UTILIZATION
STATUS=ACTIVE と PERCENT=84 が表示されていれば、机上例で各スプールボリュームの使用率を確認できています。$HASP646 の合計使用率も同じ画面で読み取ります。
――――
■ ステップ 3
現在の画面は SDSF LOG の一覧画面です。NP 欄に S を入力し、$D SPOOL の応答がシステムログにも記録されているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF LOG)
NP   COMMAND
S    LOG
→ Enter を押す
［画面・出力］
(SDSF LOG)
$HASP893 VOLUME(SPOOL1)  STATUS=ACTIVE,PERCENT=84
$HASP646 88.1904 PERCENT SPOOL UTILIZATION
ISSUER=OPER1
ISSUER=OPER1 と PERCENT=84 が同じログに残っていれば、誰がどのスプール確認を行ったかを机上例として追跡できます。応答画面とログの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /$D SPOOL が画面・出力に表示されること
② ステップ2 の STATUS=ACTIVE PERCENT=84 が画面・出力に表示されること
③ ステップ3 の ISSUER=OPER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2イニシエータ状態確認 手順</strong></p><p>検証目的: イニシエータ状態の机上応答を確認します。$D INITに対して各イニシエータのSTATUS、CLASS、ASIDが読み取れることを確かめます。</p><p>前提条件: SDSFにログオン済みで、コマンド入力口から先頭 / を付けてJES2コマンドを机上確認できる前提です。実機ではイニシエータの確認は変更管理の承認を得て、対象SSID、イニシエータ番号、クラス、稼働状況を確認してから実施します。</p><p>セッション環境: SDSFのコマンド入力口から /$D INIT を入力し、コマンド応答画面またはSDSF LOGで $HASP892、STATUS、CLASS、ASID、ISSUER を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に先頭 / を付けて $D INIT を入力し、イニシエータの状態を確認するJES2コマンドを送信します。対象のSSIDと確認目的が合っているか見直します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、机上例のイニシエータ確認コマンドを実行する準備ができています。INIT の対象と目的が合っているか確認します。
――――
■ ステップ 2
現在の画面は $D INIT の応答を表示するSDSFのコマンド応答画面です。前ステップで送信したコマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、$HASP892 のSTATUSやCLASSを同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SDSF Command Response)
$HASP892 INIT(1)    STATUS=INACTIVE,CLASS=A,NAME=1,ASID=012E
$HASP892 INIT(2)    STATUS=DRAINED,CLASS=AB,NAME=1
STATUS=INACTIVE と CLASS=A が表示されていれば、机上例でイニシエータの状態を確認できています。稼働中のINIT(1)にはASID=012Eも同じ画面で読み取れます。
――――
■ ステップ 3
現在の画面は SDSF LOG の一覧画面です。NP 欄に S を入力し、$D INIT の応答がシステムログにも記録されているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF LOG)
NP   COMMAND
S    LOG
→ Enter を押す
［画面・出力］
(SDSF LOG)
$HASP892 INIT(1)    STATUS=INACTIVE,CLASS=A,NAME=1,ASID=012E
ISSUER=OPER1
ASID=012E と ISSUER=OPER1 が同じログに残っていれば、誰がどのイニシエータ確認を行ったかを机上例として追跡できます。応答画面とログの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /$D INIT が画面・出力に表示されること
② ステップ2 の STATUS=INACTIVE CLASS=A が画面・出力に表示されること
③ ステップ3 の ASID=012E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2ジョブ待ち行列確認 手順</strong></p><p>検証目的: ジョブ待ち行列の机上応答を確認します。$D Nに対して待機ジョブのSTATUS、CLASS、PRIORITYが読み取れることを確かめます。</p><p>前提条件: SDSFにログオン済みで、コマンド入力口から先頭 / を付けてJES2コマンドを机上確認できる前提です。実機ではジョブ確認は変更管理の承認を得て、対象SSID、ジョブ名、ジョブ番号、クラスを確認してから実施します。</p><p>セッション環境: SDSFのコマンド入力口から /$D N を入力し、コマンド応答画面またはSDSF LOGで $HASP890、STATUS、CLASS、PRIORITY、ISSUER を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に先頭 / を付けて $D N を入力し、待機中のジョブを確認するJES2コマンドを送信します。対象のSSIDと確認目的が合っているか見直します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D N
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D N
COMMAND INPUT に /$D N が表示されていれば、机上例のジョブ確認コマンドを実行する準備ができています。COMMAND の対象と目的が合っているか確認します。
――――
■ ステップ 2
現在の画面は $D N の応答を表示するSDSFのコマンド応答画面です。前ステップで送信したコマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、$HASP890 のジョブ名やSTATUSを同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SDSF Command Response)
JOB00017  $HASP890 JOB(MYJOB)
$HASP890 JOB(MYJOB)     STATUS=(AWAITING EXECUTION),CLASS=H,
$HASP890                PRIORITY=9,SYSAFF=(ANY),HOLD=(JOB)
$HASP646 9.1346 PERCENT SPOOL UTILIZATION
JOB(MYJOB) と CLASS=H が表示されていれば、机上例で待機中ジョブの状態を確認できています。STATUS=(AWAITING EXECUTION) も同じ画面で読み取ります。
――――
■ ステップ 3
現在の画面は SDSF LOG の一覧画面です。NP 欄に S を入力し、$D N の応答がシステムログにも記録されているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF LOG)
NP   COMMAND
S    LOG
→ Enter を押す
［画面・出力］
(SDSF LOG)
$HASP890 JOB(MYJOB)     STATUS=(AWAITING EXECUTION),CLASS=H
ISSUER=OPER1
JOB(MYJOB) と ISSUER=OPER1 が同じログに残っていれば、誰がどのジョブ確認を行ったかを机上例として追跡できます。応答画面とログの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /$D N が画面・出力に表示されること
② ステップ2 の JOB(MYJOB) CLASS=H が画面・出力に表示されること
③ ステップ3 の ISSUER=OPER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2チェックポイント定義確認 手順</strong></p><p>検証目的: チェックポイント定義の机上応答を確認します。$D CKPTDEFに対してCKPT1やCKPT2、MODEが読み取れることを確かめます。</p><p>前提条件: SDSFにログオン済みで、コマンド入力口から先頭 / を付けてJES2コマンドを机上確認できる前提です。実機ではチェックポイント確認は変更管理の承認を得て、対象SSID、CKPT1やCKPT2のデータセット名、MODEを確認してから実施します。</p><p>セッション環境: SDSFのコマンド入力口から /$D CKPTDEF を入力し、コマンド応答画面またはSDSF LOGで CKPTDEF、CKPT1、MODE、ISSUER を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に先頭 / を付けて $D CKPTDEF を入力し、チェックポイント定義を確認するJES2コマンドを送信します。対象のSSIDと確認目的が合っているか見直します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、机上例のチェックポイント確認コマンドを実行する準備ができています。CKPTDEF の対象と目的が合っているか確認します。
――――
■ ステップ 2
現在の画面は $D CKPTDEF の応答を表示するSDSFのコマンド応答画面です。前ステップで送信したコマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、CKPT1やMODEの値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SDSF Command Response)
CKPTDEF CKPT1=(DSN=SYS1.JES2CKPT1,VOL=CHECK1,INUSE=YES),
        CKPT2=(DSN=SYS1.JESCKPT2,VOL=CHECK2,INUSE=YES),
        MODE=DUAL
MODE=DUAL と CKPT1=(DSN=SYS1.JES2CKPT1 が表示されていれば、机上例でチェックポイント定義を確認できています。CHECK1 のボリュームも同じ画面で読み取ります。
――――
■ ステップ 3
現在の画面は SDSF LOG の一覧画面です。NP 欄に S を入力し、$D CKPTDEF の応答がシステムログにも記録されているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF LOG)
NP   COMMAND
S    LOG
→ Enter を押す
［画面・出力］
(SDSF LOG)
CKPTDEF CKPT1=(DSN=SYS1.JES2CKPT1,VOL=CHECK1,INUSE=YES),
        MODE=DUAL
ISSUER=OPER1
MODE=DUAL と ISSUER=OPER1 が同じログに残っていれば、誰がどのチェックポイント確認を行ったかを机上例として追跡できます。応答画面とログの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /$D CKPTDEF が画面・出力に表示されること
② ステップ2 の MODE=DUAL が画面・出力に表示されること
③ ステップ3 の ISSUER=OPER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2トラックグループ内訳確認 手順</strong></p><p>検証目的: トラックグループ内訳の机上応答を確認します。$D SPOOL(SPOOL1),LONGに対してTGNUM、TGINUSE、PERCENTが読み取れることを確かめます。</p><p>前提条件: SDSFにログオン済みで、コマンド入力口から先頭 / を付けてJES2コマンドを机上確認できる前提です。実機ではトラックグループの確認は変更管理の承認を得て、対象SSID、スプールボリューム名、トラックグループ総数、使用中数を確認してから実施します。</p><p>セッション環境: SDSFのコマンド入力口から /$D SPOOL(SPOOL1),LONG を入力し、コマンド応答画面またはSDSF LOGで $HASP893、TGNUM、TGINUSE、PERCENT、ISSUER を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に先頭 / を付けて $D SPOOL(SPOOL1),LONG を入力し、トラックグループ内訳を確認するJES2コマンドを送信します。対象のSSIDと確認目的が合っているか見直します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOL(SPOOL1),LONG
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOL(SPOOL1),LONG
COMMAND INPUT に /$D SPOOL(SPOOL1),LONG が表示されていれば、机上例のトラックグループ確認コマンドを実行する準備ができています。SPOOL1 の対象と目的が合っているか確認します。
――――
■ ステップ 2
現在の画面は $D SPOOL(SPOOL1),LONG の応答を表示するSDSFのコマンド応答画面です。前ステップで送信したコマンドの応答メッセージを読み取ります。操作欄には追加入力を入れず、TGNUMやTGINUSEの値を同じ画面から確認します。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SDSF Command Response)
$HASP893 VOLUME(SPOOL1)  STATUS=ACTIVE,SYSAFF=(ANY),TGNUM=525
$HASP893 TGINUSE=141,TRKPERTGB=1,PERCENT=26,RESERVED=Yes
$HASP646 88.1904 PERCENT SPOOL UTILIZATION
TGNUM=525 と TGINUSE=141 が表示されていれば、机上例でトラックグループの内訳を確認できています。PERCENT=26 の使用率も同じ画面で読み取ります。
――――
■ ステップ 3
現在の画面は SDSF LOG の一覧画面です。NP 欄に S を入力し、$D SPOOL(SPOOL1),LONG の応答がシステムログにも記録されているか確認します。この操作で運用証跡として残すメッセージを探します。
［操作（入力）］
(SDSF LOG)
NP   COMMAND
S    LOG
→ Enter を押す
［画面・出力］
(SDSF LOG)
$HASP893 VOLUME(SPOOL1)  STATUS=ACTIVE,TGNUM=525
$HASP893 TGINUSE=141,PERCENT=26
ISSUER=OPER1
TGNUM=525 と ISSUER=OPER1 が同じログに残っていれば、誰がどのトラックグループ確認を行ったかを机上例として追跡できます。応答画面とログの値が一致することも確認します。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /$D SPOOL(SPOOL1),LONG が画面・出力に表示されること
② ステップ2 の TGNUM=525 TGINUSE=141 が画面・出力に表示されること
③ ステップ3 の ISSUER=OPER1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA jobname 個別表示 確認手順</strong></p><p>検証目的: $DA jobname 個別表示について、JES2コマンド応答に$HASP890と対象資源JES0753が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DA を入力し、JES2応答で$HASP890とJES0753を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DA を入力し、$DA jobname 個別表示の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DA
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DA
COMMAND INPUT に /$DA が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DA の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DA
$HASP890 JOB(JES0753) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0753) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0753) NUMBER=1,ACTIVE=YES
$HASP890 と JES0753 が表示されていれば、$DA jobname 個別表示の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0753
COMMAND=$DA
AUDIT=JES2A20753
$HASP890 RECORDED と AUDIT=JES2A20753 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DA が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0753 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA STC のみ 確認手順</strong></p><p>検証目的: $DA STC のみについて、JES2コマンド応答に$HASP890と対象資源JES0754が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DA を入力し、JES2応答で$HASP890とJES0754を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DA を入力し、$DA STC のみの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DA
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DA
COMMAND INPUT に /$DA が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DA の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DA
$HASP890 JOB(JES0754) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0754) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0754) NUMBER=1,ACTIVE=YES
$HASP890 と JES0754 が表示されていれば、$DA STC のみの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0754
COMMAND=$DA
AUDIT=JES2A20754
$HASP890 RECORDED と AUDIT=JES2A20754 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DA が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0754 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA TSU のみ 確認手順</strong></p><p>検証目的: $DA TSU のみについて、JES2コマンド応答に$HASP890と対象資源JES0755が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DA を入力し、JES2応答で$HASP890とJES0755を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DA を入力し、$DA TSU のみの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DA
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DA
COMMAND INPUT に /$DA が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DA の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DA
$HASP890 JOB(JES0755) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0755) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0755) NUMBER=1,ACTIVE=YES
$HASP890 と JES0755 が表示されていれば、$DA TSU のみの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0755
COMMAND=$DA
AUDIT=JES2A20755
$HASP890 RECORDED と AUDIT=JES2A20755 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DA が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0755 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DA 出力 $HASP100 確認手順</strong></p><p>検証目的: $DA 出力 $HASP100について、JES2コマンド応答に$HASP890と対象資源JES0756が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DA を入力し、JES2応答で$HASP890とJES0756を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DA を入力し、$DA 出力 $HASP100の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DA
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DA
COMMAND INPUT に /$DA が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DA の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DA
$HASP890 JOB(JES0756) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0756) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0756) NUMBER=1,ACTIVE=YES
$HASP890 と JES0756 が表示されていれば、$DA 出力 $HASP100の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0756
COMMAND=$DA
AUDIT=JES2A20756
$HASP890 RECORDED と AUDIT=JES2A20756 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DA が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0756 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ 基本動作 確認手順</strong></p><p>検証目的: $DJ 基本動作について、JES2コマンド応答に$HASP890と対象資源JES0757が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DJ を入力し、JES2応答で$HASP890とJES0757を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DJ を入力し、$DJ 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DJ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DJ
COMMAND INPUT に /$DJ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DJ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DJ
$HASP890 JOB(JES0757) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0757) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0757) NUMBER=1,ACTIVE=YES
$HASP890 と JES0757 が表示されていれば、$DJ 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0757
COMMAND=$DJ
AUDIT=JES2A20757
$HASP890 RECORDED と AUDIT=JES2A20757 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DJ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0757 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ jobname 確認手順</strong></p><p>検証目的: $DJ jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0758が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DJ を入力し、JES2応答で$HASP890とJES0758を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DJ を入力し、$DJ jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DJ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DJ
COMMAND INPUT に /$DJ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DJ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DJ
$HASP890 JOB(JES0758) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0758) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0758) NUMBER=1,ACTIVE=YES
$HASP890 と JES0758 が表示されていれば、$DJ jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0758
COMMAND=$DJ
AUDIT=JES2A20758
$HASP890 RECORDED と AUDIT=JES2A20758 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DJ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0758 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ Q 待機キューフィルタ 確認手順</strong></p><p>検証目的: $DJ Q 待機キューフィルタについて、JES2コマンド応答に$HASP890と対象資源JES0759が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DJ を入力し、JES2応答で$HASP890とJES0759を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DJ を入力し、$DJ Q 待機キューフィルタの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DJ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DJ
COMMAND INPUT に /$DJ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DJ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DJ
$HASP890 JOB(JES0759) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0759) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0759) NUMBER=1,ACTIVE=YES
$HASP890 と JES0759 が表示されていれば、$DJ Q 待機キューフィルタの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0759
COMMAND=$DJ
AUDIT=JES2A20759
$HASP890 RECORDED と AUDIT=JES2A20759 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DJ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0759 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ L 長形式 確認手順</strong></p><p>検証目的: $DJ L 長形式について、JES2コマンド応答に$HASP890と対象資源JES0760が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DJ を入力し、JES2応答で$HASP890とJES0760を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DJ を入力し、$DJ L 長形式の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DJ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DJ
COMMAND INPUT に /$DJ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DJ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DJ
$HASP890 JOB(JES0760) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0760) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0760) NUMBER=1,ACTIVE=YES
$HASP890 と JES0760 が表示されていれば、$DJ L 長形式の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0760
COMMAND=$DJ
AUDIT=JES2A20760
$HASP890 RECORDED と AUDIT=JES2A20760 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DJ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0760 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJ Jnnn ジョブ番号指定 確認手順</strong></p><p>検証目的: $DJ Jnnn ジョブ番号指定について、JES2コマンド応答に$HASP890と対象資源JES0761が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DJ を入力し、JES2応答で$HASP890とJES0761を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DJ を入力し、$DJ Jnnn ジョブ番号指定の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DJ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DJ
COMMAND INPUT に /$DJ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DJ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DJ
$HASP890 JOB(JES0761) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0761) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0761) NUMBER=1,ACTIVE=YES
$HASP890 と JES0761 が表示されていれば、$DJ Jnnn ジョブ番号指定の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0761
COMMAND=$DJ
AUDIT=JES2A20761
$HASP890 RECORDED と AUDIT=JES2A20761 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DJ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0761 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI 基本動作 確認手順</strong></p><p>検証目的: $DI 基本動作について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DI を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DI を入力し、$DI 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DI
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DI
COMMAND INPUT に /$DI が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DI の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$DI
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$DI 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$DI
AUDIT=JES2A20762
$HASP892 RECORDED と AUDIT=JES2A20762 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DI が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI n 個別表示 確認手順</strong></p><p>検証目的: $DI n 個別表示について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DI を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DI を入力し、$DI n 個別表示の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DI
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DI
COMMAND INPUT に /$DI が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DI の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$DI
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$DI n 個別表示の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$DI
AUDIT=JES2A20763
$HASP892 RECORDED と AUDIT=JES2A20763 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DI が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI のクラス表示 確認手順</strong></p><p>検証目的: $DI のクラス表示について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DI を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DI を入力し、$DI のクラス表示の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DI
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DI
COMMAND INPUT に /$DI が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DI の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$DI
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$DI のクラス表示の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$DI
AUDIT=JES2A20764
$HASP892 RECORDED と AUDIT=JES2A20764 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DI が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI と WLM 管理イニシエータ 確認手順</strong></p><p>検証目的: $DI と WLM 管理イニシエータについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DI を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DI を入力し、$DI と WLM 管理イニシエータの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DI
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DI
COMMAND INPUT に /$DI が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DI の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$DI
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$DI と WLM 管理イニシエータの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$DI
AUDIT=JES2A20765
$HASP892 RECORDED と AUDIT=JES2A20765 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DI が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DQ 基本動作 確認手順</strong></p><p>検証目的: $DQ 基本動作について、JES2コマンド応答に$HASP890と対象資源JES0766が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DQ を入力し、JES2応答で$HASP890とJES0766を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DQ を入力し、$DQ 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DQ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DQ
COMMAND INPUT に /$DQ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DQ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$DQ
$HASP890 JOB(JES0766) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0766) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0766) NUMBER=1,ACTIVE=YES
$HASP890 と JES0766 が表示されていれば、$DQ 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0766
COMMAND=$DQ
AUDIT=JES2A20766
$HASP890 RECORDED と AUDIT=JES2A20766 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DQ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0766 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DQ クラス別カウント 確認手順</strong></p><p>検証目的: $DQ クラス別カウントについて、JES2コマンド応答に$HASP890と対象資源JES0767が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DQ を入力し、JES2応答で$HASP890とJES0767を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DQ を入力し、$DQ クラス別カウントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DQ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DQ
COMMAND INPUT に /$DQ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DQ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$DQ
$HASP890 JOB(JES0767) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0767) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0767) NUMBER=1,ACTIVE=YES
$HASP890 と JES0767 が表示されていれば、$DQ クラス別カウントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0767
COMMAND=$DQ
AUDIT=JES2A20767
$HASP890 RECORDED と AUDIT=JES2A20767 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DQ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0767 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPRT 基本動作 確認手順</strong></p><p>検証目的: $DPRT 基本動作について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DPRT を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DPRT を入力し、$DPRT 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DPRT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DPRT
COMMAND INPUT に /$DPRT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DPRT の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$DPRT
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$DPRT 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$DPRT
AUDIT=JES2A20768
$HASP621 RECORDED と AUDIT=JES2A20768 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DPRT が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPRT n 個別表示 確認手順</strong></p><p>検証目的: $DPRT n 個別表示について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DPRT を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DPRT を入力し、$DPRT n 個別表示の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DPRT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DPRT
COMMAND INPUT に /$DPRT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DPRT の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$DPRT
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$DPRT n 個別表示の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$DPRT
AUDIT=JES2A20769
$HASP621 RECORDED と AUDIT=JES2A20769 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DPRT が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPRT L 長形式 確認手順</strong></p><p>検証目的: $DPRT L 長形式について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DPRT を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DPRT を入力し、$DPRT L 長形式の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DPRT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DPRT
COMMAND INPUT に /$DPRT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DPRT の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$DPRT
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$DPRT L 長形式の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$DPRT
AUDIT=JES2A20770
$HASP621 RECORDED と AUDIT=JES2A20770 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DPRT が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DPUN 基本動作 確認手順</strong></p><p>検証目的: $DPUN 基本動作について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DPUN を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DPUN を入力し、$DPUN 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DPUN
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DPUN
COMMAND INPUT に /$DPUN が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DPUN の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$DPUN
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$DPUN 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$DPUN
AUDIT=JES2A20771
$HASP621 RECORDED と AUDIT=JES2A20771 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DPUN が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DRDR 基本動作 確認手順</strong></p><p>検証目的: $DRDR 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DRDR を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DRDR を入力し、$DRDR 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DRDR
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DRDR
COMMAND INPUT に /$DRDR が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DRDR の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$DRDR
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$DRDR 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$DRDR
AUDIT=JES2A20772
$HASP000 RECORDED と AUDIT=JES2A20772 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DRDR が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DRDR n 個別表示 確認手順</strong></p><p>検証目的: $DRDR n 個別表示について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DRDR を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DRDR を入力し、$DRDR n 個別表示の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DRDR
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DRDR
COMMAND INPUT に /$DRDR が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DRDR の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$DRDR
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$DRDR n 個別表示の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$DRDR
AUDIT=JES2A20773
$HASP000 RECORDED と AUDIT=JES2A20773 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DRDR が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPOOL 基本動作 確認手順</strong></p><p>検証目的: $DSPOOL 基本動作について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DSPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DSPOOL を入力し、$DSPOOL 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DSPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DSPOOL
COMMAND INPUT に /$DSPOOL が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DSPOOL の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DSPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$DSPOOL 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$DSPOOL
AUDIT=JES2A20774
$HASP646 RECORDED と AUDIT=JES2A20774 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DSPOOL が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPOOL L 長形式 確認手順</strong></p><p>検証目的: $DSPOOL L 長形式について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DSPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DSPOOL を入力し、$DSPOOL L 長形式の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DSPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DSPOOL
COMMAND INPUT に /$DSPOOL が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DSPOOL の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DSPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$DSPOOL L 長形式の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$DSPOOL
AUDIT=JES2A20775
$HASP646 RECORDED と AUDIT=JES2A20775 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DSPOOL が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPL VOL=ser 確認手順</strong></p><p>検証目的: $DSPL VOL=serについて、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DSPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DSPOOL を入力し、$DSPL VOL=serの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DSPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DSPOOL
COMMAND INPUT に /$DSPOOL が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DSPOOL の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DSPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$DSPL VOL=serの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$DSPOOL
AUDIT=JES2A20776
$HASP646 RECORDED と AUDIT=JES2A20776 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DSPOOL が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DT 基本動作 確認手順</strong></p><p>検証目的: $DT 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DT を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DT を入力し、$DT 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DT
COMMAND INPUT に /$DT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DT の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$DT
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$DT 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$DT
AUDIT=JES2A20777
$HASP000 RECORDED と AUDIT=JES2A20777 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DT が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DMASDEF 確認手順</strong></p><p>検証目的: $DMASDEFについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DMASDEF を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DMASDEF を入力し、$DMASDEFの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DMASDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DMASDEF
COMMAND INPUT に /$DMASDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DMASDEF の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$DMASDEF
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$DMASDEFの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$DMASDEF
AUDIT=JES2A20778
$HASP000 RECORDED と AUDIT=JES2A20778 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DMASDEF が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DCKPTDEF 確認手順</strong></p><p>検証目的: $DCKPTDEFについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DCKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DCKPTDEF を入力し、$DCKPTDEFの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DCKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DCKPTDEF
COMMAND INPUT に /$DCKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DCKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$DCKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、$DCKPTDEFの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$DCKPTDEF
AUDIT=JES2A20779
$HASP829 RECORDED と AUDIT=JES2A20779 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DCKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DSPOOLDEF 確認手順</strong></p><p>検証目的: $DSPOOLDEFについて、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DSPOOL を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DSPOOL を入力し、$DSPOOLDEFの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DSPOOL
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DSPOOL
COMMAND INPUT に /$DSPOOL が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DSPOOL の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DSPOOL
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$DSPOOLDEFの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$DSPOOL
AUDIT=JES2A20780
$HASP646 RECORDED と AUDIT=JES2A20780 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DSPOOL が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DJOBCLASS c 確認手順</strong></p><p>検証目的: $DJOBCLASS cについて、JES2コマンド応答に$HASP890と対象資源JES0781が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DJ を入力し、JES2応答で$HASP890とJES0781を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DJ を入力し、$DJOBCLASS cの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DJ
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DJ
COMMAND INPUT に /$DJ が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DJ の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DJ
$HASP890 JOB(JES0781) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0781) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0781) NUMBER=1,ACTIVE=YES
$HASP890 と JES0781 が表示されていれば、$DJOBCLASS cの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0781
COMMAND=$DJ
AUDIT=JES2A20781
$HASP890 RECORDED と AUDIT=JES2A20781 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DJ が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0781 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DOUTCLASS c 確認手順</strong></p><p>検証目的: $DOUTCLASS cについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DOUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DOUTCLASS を入力し、$DOUTCLASS cの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DOUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DOUTCLASS
COMMAND INPUT に /$DOUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DOUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$DOUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$DOUTCLASS cの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$DOUTCLASS
AUDIT=JES2A20782
$HASP621 RECORDED と AUDIT=JES2A20782 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DOUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DNODE n 確認手順</strong></p><p>検証目的: $DNODE nについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、$DNODE nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、$DNODE nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20783
$HASP815 RECORDED と AUDIT=JES2A20783 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DACTIVATE 確認手順</strong></p><p>検証目的: $DACTIVATEについて、JES2コマンド応答に$HASP890と対象資源JES0784が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DA を入力し、JES2応答で$HASP890とJES0784を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DA を入力し、$DACTIVATEの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DA
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DA
COMMAND INPUT に /$DA が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DA の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$DA
$HASP890 JOB(JES0784) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0784) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0784) NUMBER=1,ACTIVE=YES
$HASP890 と JES0784 が表示されていれば、$DACTIVATEの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0784
COMMAND=$DA
AUDIT=JES2A20784
$HASP890 RECORDED と AUDIT=JES2A20784 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DA が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0784 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DMEMBER 確認手順</strong></p><p>検証目的: $DMEMBERについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$DMEMBERの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$DMEMBERの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20785
$HASP000 RECORDED と AUDIT=JES2A20785 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A 基本動作 確認手順</strong></p><p>検証目的: $A 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$A 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$A 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20786
$HASP000 RECORDED と AUDIT=JES2A20786 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A jobname 確認手順</strong></p><p>検証目的: $A jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0787が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0787を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$A jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0787) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0787) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0787) NUMBER=1,ACTIVE=YES
$HASP890 と JES0787 が表示されていれば、$A jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0787
COMMAND=$D JOBDEF
AUDIT=JES2A20787
$HASP890 RECORDED と AUDIT=JES2A20787 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0787 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A &#x27;A&#x27; 全リリース 確認手順</strong></p><p>検証目的: $A &#x27;A&#x27; 全リリースについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$A &#x27;A&#x27; 全リリースの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$A &#x27;A&#x27; 全リリースの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20788
$HASP000 RECORDED と AUDIT=JES2A20788 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A Jnnn ジョブ番号指定 確認手順</strong></p><p>検証目的: $A Jnnn ジョブ番号指定について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$A Jnnn ジョブ番号指定の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$A Jnnn ジョブ番号指定の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20789
$HASP000 RECORDED と AUDIT=JES2A20789 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$A と TYPRUN=HOLD 確認手順</strong></p><p>検証目的: $A と TYPRUN=HOLDについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$A と TYPRUN=HOLDの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$A と TYPRUN=HOLDの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20790
$HASP000 RECORDED と AUDIT=JES2A20790 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$C 基本動作 確認手順</strong></p><p>検証目的: $C 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$C 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$C 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20791
$HASP000 RECORDED と AUDIT=JES2A20791 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$C jobname 確認手順</strong></p><p>検証目的: $C jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0792が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0792を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$C jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0792) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0792) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0792) NUMBER=1,ACTIVE=YES
$HASP890 と JES0792 が表示されていれば、$C jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0792
COMMAND=$D JOBDEF
AUDIT=JES2A20792
$HASP890 RECORDED と AUDIT=JES2A20792 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0792 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$C jobname DUMP 確認手順</strong></p><p>検証目的: $C jobname DUMPについて、JES2コマンド応答に$HASP890と対象資源JES0793が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0793を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$C jobname DUMPの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0793) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0793) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0793) NUMBER=1,ACTIVE=YES
$HASP890 と JES0793 が表示されていれば、$C jobname DUMPの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0793
COMMAND=$D JOBDEF
AUDIT=JES2A20793
$HASP890 RECORDED と AUDIT=JES2A20793 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0793 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$C jobname PURGE 確認手順</strong></p><p>検証目的: $C jobname PURGEについて、JES2コマンド応答に$HASP890と対象資源JES0794が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0794を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$C jobname PURGEの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0794) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0794) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0794) NUMBER=1,ACTIVE=YES
$HASP890 と JES0794 が表示されていれば、$C jobname PURGEの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0794
COMMAND=$D JOBDEF
AUDIT=JES2A20794
$HASP890 RECORDED と AUDIT=JES2A20794 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0794 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$C jobname A 確認手順</strong></p><p>検証目的: $C jobname Aについて、JES2コマンド応答に$HASP890と対象資源JES0795が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0795を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$C jobname Aの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0795) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0795) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0795) NUMBER=1,ACTIVE=YES
$HASP890 と JES0795 が表示されていれば、$C jobname Aの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0795
COMMAND=$D JOBDEF
AUDIT=JES2A20795
$HASP890 RECORDED と AUDIT=JES2A20795 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0795 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$C PRT n 確認手順</strong></p><p>検証目的: $C PRT nについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$C PRT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$C PRT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20796
$HASP621 RECORDED と AUDIT=JES2A20796 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$H 基本動作 確認手順</strong></p><p>検証目的: $H 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$H 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$H 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20797
$HASP000 RECORDED と AUDIT=JES2A20797 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$H jobname 確認手順</strong></p><p>検証目的: $H jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0798が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0798を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$H jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0798) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0798) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0798) NUMBER=1,ACTIVE=YES
$HASP890 と JES0798 が表示されていれば、$H jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0798
COMMAND=$D JOBDEF
AUDIT=JES2A20798
$HASP890 RECORDED と AUDIT=JES2A20798 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0798 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$H A 全保留 確認手順</strong></p><p>検証目的: $H A 全保留について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$H A 全保留の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$H A 全保留の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20799
$HASP000 RECORDED と AUDIT=JES2A20799 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$H Jnnn 確認手順</strong></p><p>検証目的: $H Jnnnについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$H Jnnnの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$H Jnnnの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20800
$HASP000 RECORDED と AUDIT=JES2A20800 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$O 基本動作 確認手順</strong></p><p>検証目的: $O 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$O 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$O 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20801
$HASP000 RECORDED と AUDIT=JES2A20801 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$O jobname 確認手順</strong></p><p>検証目的: $O jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0802が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0802を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$O jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0802) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0802) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0802) NUMBER=1,ACTIVE=YES
$HASP890 と JES0802 が表示されていれば、$O jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0802
COMMAND=$D JOBDEF
AUDIT=JES2A20802
$HASP890 RECORDED と AUDIT=JES2A20802 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0802 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$O Jnnn 確認手順</strong></p><p>検証目的: $O Jnnnについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$O Jnnnの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$O Jnnnの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20803
$HASP000 RECORDED と AUDIT=JES2A20803 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$O と OUTCLASS=Z Hold 確認手順</strong></p><p>検証目的: $O と OUTCLASS=Z Holdについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$O と OUTCLASS=Z Holdの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$O と OUTCLASS=Z Holdの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20804
$HASP621 RECORDED と AUDIT=JES2A20804 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$E 基本動作 確認手順</strong></p><p>検証目的: $E 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$E 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$E 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20805
$HASP000 RECORDED と AUDIT=JES2A20805 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$E jobname 確認手順</strong></p><p>検証目的: $E jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0806が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0806を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$E jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0806) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0806) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0806) NUMBER=1,ACTIVE=YES
$HASP890 と JES0806 が表示されていれば、$E jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0806
COMMAND=$D JOBDEF
AUDIT=JES2A20806
$HASP890 RECORDED と AUDIT=JES2A20806 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0806 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$E PRT n 確認手順</strong></p><p>検証目的: $E PRT nについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$E PRT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$E PRT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20807
$HASP621 RECORDED と AUDIT=JES2A20807 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$E CKPTLOCK 確認手順</strong></p><p>検証目的: $E CKPTLOCKについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、$E CKPTLOCKの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、$E CKPTLOCKの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20808
$HASP829 RECORDED と AUDIT=JES2A20808 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P JES2 JES2 停止 確認手順</strong></p><p>検証目的: $P JES2 JES2 停止について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$P JES2 JES2 停止の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$P JES2 JES2 停止の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20809
$HASP000 RECORDED と AUDIT=JES2A20809 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$PJES2 ABEND JES2 異常停止 確認手順</strong></p><p>検証目的: $PJES2 ABEND JES2 異常停止について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$PJES2 ABEND JES2 異常停止の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$PJES2 ABEND JES2 異常停止の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20810
$HASP000 RECORDED と AUDIT=JES2A20810 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P INIT n 確認手順</strong></p><p>検証目的: $P INIT nについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、$P INIT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$P INIT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20811
$HASP892 RECORDED と AUDIT=JES2A20811 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P PRT n 確認手順</strong></p><p>検証目的: $P PRT nについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$P PRT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$P PRT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20812
$HASP621 RECORDED と AUDIT=JES2A20812 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P PUN n 確認手順</strong></p><p>検証目的: $P PUN nについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$P PUN nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$P PUN nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20813
$HASP621 RECORDED と AUDIT=JES2A20813 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P RDR n 確認手順</strong></p><p>検証目的: $P RDR nについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$P RDR nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$P RDR nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20814
$HASP000 RECORDED と AUDIT=JES2A20814 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P XEQ 実行停止 確認手順</strong></p><p>検証目的: $P XEQ 実行停止について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$P XEQ 実行停止の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$P XEQ 実行停止の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20815
$HASP000 RECORDED と AUDIT=JES2A20815 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$P NET ネットワーク停止 確認手順</strong></p><p>検証目的: $P NET ネットワーク停止について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$P NET ネットワーク停止の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$P NET ネットワーク停止の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20816
$HASP000 RECORDED と AUDIT=JES2A20816 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S JES2 JES2 開始 確認手順</strong></p><p>検証目的: $S JES2 JES2 開始について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$S JES2 JES2 開始の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$S JES2 JES2 開始の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20817
$HASP000 RECORDED と AUDIT=JES2A20817 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S INIT n 確認手順</strong></p><p>検証目的: $S INIT nについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、$S INIT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$S INIT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20818
$HASP892 RECORDED と AUDIT=JES2A20818 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S PRT n 確認手順</strong></p><p>検証目的: $S PRT nについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$S PRT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$S PRT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20819
$HASP621 RECORDED と AUDIT=JES2A20819 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S RDR n dsname 確認手順</strong></p><p>検証目的: $S RDR n dsnameについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$S RDR n dsnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$S RDR n dsnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20820
$HASP000 RECORDED と AUDIT=JES2A20820 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S SPL volser スプール追加 確認手順</strong></p><p>検証目的: $S SPL volser スプール追加について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、$S SPL volser スプール追加の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$S SPL volser スプール追加の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20821
$HASP646 RECORDED と AUDIT=JES2A20821 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S NET ネットワーク開始 確認手順</strong></p><p>検証目的: $S NET ネットワーク開始について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$S NET ネットワーク開始の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$S NET ネットワーク開始の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20822
$HASP000 RECORDED と AUDIT=JES2A20822 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S LINE n 確認手順</strong></p><p>検証目的: $S LINE nについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、$S LINE nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、$S LINE nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20823
$HASP815 RECORDED と AUDIT=JES2A20823 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T 基本動作 確認手順</strong></p><p>検証目的: $T 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$T 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$T 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20824
$HASP000 RECORDED と AUDIT=JES2A20824 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T INIT n CLASS= 確認手順</strong></p><p>検証目的: $T INIT n CLASS=について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、$T INIT n CLASS=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$T INIT n CLASS=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20825
$HASP892 RECORDED と AUDIT=JES2A20825 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T PRT n ROUTECDE= 確認手順</strong></p><p>検証目的: $T PRT n ROUTECDE=について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$T PRT n ROUTECDE=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$T PRT n ROUTECDE=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20826
$HASP621 RECORDED と AUDIT=JES2A20826 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T PRT n CLASS= 確認手順</strong></p><p>検証目的: $T PRT n CLASS=について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$T PRT n CLASS=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$T PRT n CLASS=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20827
$HASP621 RECORDED と AUDIT=JES2A20827 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T PRT n FCB= 確認手順</strong></p><p>検証目的: $T PRT n FCB=について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$T PRT n FCB=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$T PRT n FCB=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20828
$HASP621 RECORDED と AUDIT=JES2A20828 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T jobname CLASS= 確認手順</strong></p><p>検証目的: $T jobname CLASS=について、JES2コマンド応答に$HASP890と対象資源JES0829が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0829を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$T jobname CLASS=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0829) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0829) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0829) NUMBER=1,ACTIVE=YES
$HASP890 と JES0829 が表示されていれば、$T jobname CLASS=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0829
COMMAND=$D JOBDEF
AUDIT=JES2A20829
$HASP890 RECORDED と AUDIT=JES2A20829 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0829 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T jobname PRTY= 確認手順</strong></p><p>検証目的: $T jobname PRTY=について、JES2コマンド応答に$HASP890と対象資源JES0830が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0830を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$T jobname PRTY=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0830) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0830) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0830) NUMBER=1,ACTIVE=YES
$HASP890 と JES0830 が表示されていれば、$T jobname PRTY=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0830
COMMAND=$D JOBDEF
AUDIT=JES2A20830
$HASP890 RECORDED と AUDIT=JES2A20830 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0830 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T CKPTDEF など 確認手順</strong></p><p>検証目的: $T CKPTDEF などについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、$T CKPTDEF などの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、$T CKPTDEF などの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20831
$HASP829 RECORDED と AUDIT=JES2A20831 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T SPOOLDEF など 確認手順</strong></p><p>検証目的: $T SPOOLDEF などについて、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、$T SPOOLDEF などの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$T SPOOLDEF などの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20832
$HASP646 RECORDED と AUDIT=JES2A20832 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T JOBCLASS c など 確認手順</strong></p><p>検証目的: $T JOBCLASS c などについて、JES2コマンド応答に$HASP890と対象資源JES0833が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0833を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$T JOBCLASS c などの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0833) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0833) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0833) NUMBER=1,ACTIVE=YES
$HASP890 と JES0833 が表示されていれば、$T JOBCLASS c などの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0833
COMMAND=$D JOBDEF
AUDIT=JES2A20833
$HASP890 RECORDED と AUDIT=JES2A20833 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0833 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T OUTCLASS c など 確認手順</strong></p><p>検証目的: $T OUTCLASS c などについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$T OUTCLASS c などの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$T OUTCLASS c などの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20834
$HASP621 RECORDED と AUDIT=JES2A20834 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T NODE n など 確認手順</strong></p><p>検証目的: $T NODE n などについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、$T NODE n などの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、$T NODE n などの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20835
$HASP815 RECORDED と AUDIT=JES2A20835 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T MASDEF など 確認手順</strong></p><p>検証目的: $T MASDEF などについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、$T MASDEF などの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、$T MASDEF などの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20836
$HASP829 RECORDED と AUDIT=JES2A20836 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T REDIRECT cons 確認手順</strong></p><p>検証目的: $T REDIRECT consについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$T REDIRECT consの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$T REDIRECT consの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20837
$HASP000 RECORDED と AUDIT=JES2A20837 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$L jobname 確認手順</strong></p><p>検証目的: $L jobnameについて、JES2コマンド応答に$HASP890と対象資源JES0838が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0838を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$L jobnameの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0838) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0838) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0838) NUMBER=1,ACTIVE=YES
$HASP890 と JES0838 が表示されていれば、$L jobnameの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0838
COMMAND=$D JOBDEF
AUDIT=JES2A20838
$HASP890 RECORDED と AUDIT=JES2A20838 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0838 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$L SYSOUT 確認手順</strong></p><p>検証目的: $L SYSOUTについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$L SYSOUTの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$L SYSOUTの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20839
$HASP621 RECORDED と AUDIT=JES2A20839 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$N 基本動作 確認手順</strong></p><p>検証目的: $N 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$N 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$N 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20840
$HASP000 RECORDED と AUDIT=JES2A20840 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$Z PRT n 確認手順</strong></p><p>検証目的: $Z PRT nについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、$Z PRT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、$Z PRT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20841
$HASP621 RECORDED と AUDIT=JES2A20841 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$Z SPL volser 確認手順</strong></p><p>検証目的: $Z SPL volserについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$Z SPL volserの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$Z SPL volserの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20842
$HASP000 RECORDED と AUDIT=JES2A20842 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$VS 基本動作 確認手順</strong></p><p>検証目的: $VS 基本動作について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$VS 基本動作の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$VS 基本動作の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20843
$HASP000 RECORDED と AUDIT=JES2A20843 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$VS &#x27;JOB など&#x27; 構文 確認手順</strong></p><p>検証目的: $VS &#x27;JOB など&#x27; 構文について、JES2コマンド応答に$HASP890と対象資源JES0844が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0844を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、$VS &#x27;JOB など&#x27; 構文の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0844) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0844) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0844) NUMBER=1,ACTIVE=YES
$HASP890 と JES0844 が表示されていれば、$VS &#x27;JOB など&#x27; 構文の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0844
COMMAND=$D JOBDEF
AUDIT=JES2A20844
$HASP890 RECORDED と AUDIT=JES2A20844 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0844 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>PARMLIB 配置 確認手順</strong></p><p>検証目的: PARMLIB 配置について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、PARMLIB 配置の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、PARMLIB 配置の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20845
$HASP000 RECORDED と AUDIT=JES2A20845 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>APPL ステートメント 確認手順</strong></p><p>検証目的: APPL ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、APPL ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、APPL ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20846
$HASP000 RECORDED と AUDIT=JES2A20846 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>BUFDEF ステートメント 確認手順</strong></p><p>検証目的: BUFDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、BUFDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、BUFDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20847
$HASP000 RECORDED と AUDIT=JES2A20847 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF ステートメント 確認手順</strong></p><p>検証目的: CKPTDEF ステートメントについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20848
$HASP829 RECORDED と AUDIT=JES2A20848 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF CKPT1= 確認手順</strong></p><p>検証目的: CKPTDEF CKPT1=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF CKPT1=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF CKPT1=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20849
$HASP829 RECORDED と AUDIT=JES2A20849 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF CKPT2= 確認手順</strong></p><p>検証目的: CKPTDEF CKPT2=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF CKPT2=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF CKPT2=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20850
$HASP829 RECORDED と AUDIT=JES2A20850 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF DUPLEX=ON|OFF 確認手順</strong></p><p>検証目的: CKPTDEF DUPLEX=ON|OFFについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF DUPLEX=ON|OFFの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF DUPLEX=ON|OFFの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20851
$HASP829 RECORDED と AUDIT=JES2A20851 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF MODE=DUAL|DUPLEX 確認手順</strong></p><p>検証目的: CKPTDEF MODE=DUAL|DUPLEXについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF MODE=DUAL|DUPLEXの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF MODE=DUAL|DUPLEXの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20852
$HASP829 RECORDED と AUDIT=JES2A20852 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF NEWCKPT1= 確認手順</strong></p><p>検証目的: CKPTDEF NEWCKPT1=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF NEWCKPT1=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF NEWCKPT1=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20853
$HASP829 RECORDED と AUDIT=JES2A20853 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTDEF OPVERIFY=YES|NO 確認手順</strong></p><p>検証目的: CKPTDEF OPVERIFY=YES|NOについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTDEF OPVERIFY=YES|NOの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTDEF OPVERIFY=YES|NOの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20854
$HASP829 RECORDED と AUDIT=JES2A20854 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTSPACE ステートメント 確認手順</strong></p><p>検証目的: CKPTSPACE ステートメントについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTSPACE ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTSPACE ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20855
$HASP829 RECORDED と AUDIT=JES2A20855 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPTSPACE BERTNUM= 確認手順</strong></p><p>検証目的: CKPTSPACE BERTNUM=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPTSPACE BERTNUM=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPTSPACE BERTNUM=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20856
$HASP829 RECORDED と AUDIT=JES2A20856 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CONDEF ステートメント 確認手順</strong></p><p>検証目的: CONDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、CONDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、CONDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20857
$HASP000 RECORDED と AUDIT=JES2A20857 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CONDEF AUTOCMD= 確認手順</strong></p><p>検証目的: CONDEF AUTOCMD=について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、CONDEF AUTOCMD=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、CONDEF AUTOCMD=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20858
$HASP000 RECORDED と AUDIT=JES2A20858 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CONNECT ステートメント 確認手順</strong></p><p>検証目的: CONNECT ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、CONNECT ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、CONNECT ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20859
$HASP000 RECORDED と AUDIT=JES2A20859 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>DESTID ステートメント 確認手順</strong></p><p>検証目的: DESTID ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、DESTID ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、DESTID ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20860
$HASP000 RECORDED と AUDIT=JES2A20860 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ESTBYTE ステートメント 確認手順</strong></p><p>検証目的: ESTBYTE ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、ESTBYTE ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、ESTBYTE ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20861
$HASP000 RECORDED と AUDIT=JES2A20861 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ESTLNCT ステートメント 確認手順</strong></p><p>検証目的: ESTLNCT ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、ESTLNCT ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、ESTLNCT ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20862
$HASP000 RECORDED と AUDIT=JES2A20862 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ESTPAGE ステートメント 確認手順</strong></p><p>検証目的: ESTPAGE ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、ESTPAGE ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、ESTPAGE ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20863
$HASP000 RECORDED と AUDIT=JES2A20863 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ESTPUN ステートメント 確認手順</strong></p><p>検証目的: ESTPUN ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、ESTPUN ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、ESTPUN ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20864
$HASP621 RECORDED と AUDIT=JES2A20864 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ESTTIME ステートメント 確認手順</strong></p><p>検証目的: ESTTIME ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、ESTTIME ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、ESTTIME ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20865
$HASP000 RECORDED と AUDIT=JES2A20865 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT nnn ステートメント 確認手順</strong></p><p>検証目的: EXIT nnn ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT nnn ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT nnn ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20866
$HASP000 RECORDED と AUDIT=JES2A20866 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT nnn STATUS=ENABLED 確認手順</strong></p><p>検証目的: EXIT nnn STATUS=ENABLEDについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT nnn STATUS=ENABLEDの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT nnn STATUS=ENABLEDの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20867
$HASP000 RECORDED と AUDIT=JES2A20867 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT nnn ROUTINES= 確認手順</strong></p><p>検証目的: EXIT nnn ROUTINES=について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、EXIT nnn ROUTINES=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、EXIT nnn ROUTINES=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20868
$HASP621 RECORDED と AUDIT=JES2A20868 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>FSSDEF ステートメント 確認手順</strong></p><p>検証目的: FSSDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、FSSDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、FSSDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20869
$HASP000 RECORDED と AUDIT=JES2A20869 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>INITDEF ステートメント 確認手順</strong></p><p>検証目的: INITDEF ステートメントについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、INITDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、INITDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20870
$HASP892 RECORDED と AUDIT=JES2A20870 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>INIT n ステートメント 確認手順</strong></p><p>検証目的: INIT n ステートメントについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、INIT n ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、INIT n ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20871
$HASP892 RECORDED と AUDIT=JES2A20871 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>INIT n CLASS= 確認手順</strong></p><p>検証目的: INIT n CLASS=について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、INIT n CLASS=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、INIT n CLASS=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20872
$HASP892 RECORDED と AUDIT=JES2A20872 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>INIT n START=YES|NO 確認手順</strong></p><p>検証目的: INIT n START=YES|NOについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、INIT n START=YES|NOの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、INIT n START=YES|NOの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20873
$HASP892 RECORDED と AUDIT=JES2A20873 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>INTRDR ステートメント 確認手順</strong></p><p>検証目的: INTRDR ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、INTRDR ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、INTRDR ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20874
$HASP000 RECORDED と AUDIT=JES2A20874 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS ステートメント 確認手順</strong></p><p>検証目的: JOBCLASS ステートメントについて、JES2コマンド応答に$HASP890と対象資源JES0875が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0875を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0875) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0875) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0875) NUMBER=1,ACTIVE=YES
$HASP890 と JES0875 が表示されていれば、JOBCLASS ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0875
COMMAND=$D JOBDEF
AUDIT=JES2A20875
$HASP890 RECORDED と AUDIT=JES2A20875 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0875 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS TIME= 確認手順</strong></p><p>検証目的: JOBCLASS TIME=について、JES2コマンド応答に$HASP890と対象資源JES0876が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0876を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS TIME=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0876) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0876) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0876) NUMBER=1,ACTIVE=YES
$HASP890 と JES0876 が表示されていれば、JOBCLASS TIME=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0876
COMMAND=$D JOBDEF
AUDIT=JES2A20876
$HASP890 RECORDED と AUDIT=JES2A20876 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0876 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS REGION= 確認手順</strong></p><p>検証目的: JOBCLASS REGION=について、JES2コマンド応答に$HASP890と対象資源JES0877が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0877を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS REGION=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0877) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0877) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0877) NUMBER=1,ACTIVE=YES
$HASP890 と JES0877 が表示されていれば、JOBCLASS REGION=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0877
COMMAND=$D JOBDEF
AUDIT=JES2A20877
$HASP890 RECORDED と AUDIT=JES2A20877 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0877 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS MSGLEVEL= 確認手順</strong></p><p>検証目的: JOBCLASS MSGLEVEL=について、JES2コマンド応答に$HASP890と対象資源JES0878が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0878を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS MSGLEVEL=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0878) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0878) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0878) NUMBER=1,ACTIVE=YES
$HASP890 と JES0878 が表示されていれば、JOBCLASS MSGLEVEL=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0878
COMMAND=$D JOBDEF
AUDIT=JES2A20878
$HASP890 RECORDED と AUDIT=JES2A20878 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0878 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS XEQCOUNT= 確認手順</strong></p><p>検証目的: JOBCLASS XEQCOUNT=について、JES2コマンド応答に$HASP890と対象資源JES0879が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0879を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS XEQCOUNT=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0879) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0879) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0879) NUMBER=1,ACTIVE=YES
$HASP890 と JES0879 が表示されていれば、JOBCLASS XEQCOUNT=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0879
COMMAND=$D JOBDEF
AUDIT=JES2A20879
$HASP890 RECORDED と AUDIT=JES2A20879 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0879 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS MODE=JES|WLM 確認手順</strong></p><p>検証目的: JOBCLASS MODE=JES|WLMについて、JES2コマンド応答に$HASP890と対象資源JES0880が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0880を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS MODE=JES|WLMの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0880) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0880) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0880) NUMBER=1,ACTIVE=YES
$HASP890 と JES0880 が表示されていれば、JOBCLASS MODE=JES|WLMの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0880
COMMAND=$D JOBDEF
AUDIT=JES2A20880
$HASP890 RECORDED と AUDIT=JES2A20880 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0880 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS PROCLIB= 確認手順</strong></p><p>検証目的: JOBCLASS PROCLIB=について、JES2コマンド応答に$HASP890と対象資源JES0881が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0881を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS PROCLIB=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0881) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0881) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0881) NUMBER=1,ACTIVE=YES
$HASP890 と JES0881 が表示されていれば、JOBCLASS PROCLIB=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0881
COMMAND=$D JOBDEF
AUDIT=JES2A20881
$HASP890 RECORDED と AUDIT=JES2A20881 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0881 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBCLASS SCHENV= 確認手順</strong></p><p>検証目的: JOBCLASS SCHENV=について、JES2コマンド応答に$HASP890と対象資源JES0882が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0882を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBCLASS SCHENV=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0882) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0882) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0882) NUMBER=1,ACTIVE=YES
$HASP890 と JES0882 が表示されていれば、JOBCLASS SCHENV=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0882
COMMAND=$D JOBDEF
AUDIT=JES2A20882
$HASP890 RECORDED と AUDIT=JES2A20882 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0882 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBDEF ステートメント 確認手順</strong></p><p>検証目的: JOBDEF ステートメントについて、JES2コマンド応答に$HASP890と対象資源JES0883が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0883を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0883) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0883) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0883) NUMBER=1,ACTIVE=YES
$HASP890 と JES0883 が表示されていれば、JOBDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0883
COMMAND=$D JOBDEF
AUDIT=JES2A20883
$HASP890 RECORDED と AUDIT=JES2A20883 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0883 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBDEF JNUMBASE=/RANGE= 確認手順</strong></p><p>検証目的: JOBDEF JNUMBASE=/RANGE=について、JES2コマンド応答に$HASP890と対象資源JES0884が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0884を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBDEF JNUMBASE=/RANGE=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0884) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0884) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0884) NUMBER=1,ACTIVE=YES
$HASP890 と JES0884 が表示されていれば、JOBDEF JNUMBASE=/RANGE=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0884
COMMAND=$D JOBDEF
AUDIT=JES2A20884
$HASP890 RECORDED と AUDIT=JES2A20884 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0884 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBDEF DUPL_JOB=DELAY|NODELAY 確認手順</strong></p><p>検証目的: JOBDEF DUPL_JOB=DELAY|NODELAYについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、JOBDEF DUPL_JOB=DELAY|NODELAYの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、JOBDEF DUPL_JOB=DELAY|NODELAYの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20885
$HASP815 RECORDED と AUDIT=JES2A20885 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JOBPRTY ステートメント 確認手順</strong></p><p>検証目的: JOBPRTY ステートメントについて、JES2コマンド応答に$HASP890と対象資源JES0886が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0886を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、JOBPRTY ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0886) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0886) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0886) NUMBER=1,ACTIVE=YES
$HASP890 と JES0886 が表示されていれば、JOBPRTY ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0886
COMMAND=$D JOBDEF
AUDIT=JES2A20886
$HASP890 RECORDED と AUDIT=JES2A20886 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0886 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>LOADMOD ステートメント 確認手順</strong></p><p>検証目的: LOADMOD ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、LOADMOD ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、LOADMOD ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20887
$HASP000 RECORDED と AUDIT=JES2A20887 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>LOGON ステートメント 確認手順</strong></p><p>検証目的: LOGON ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、LOGON ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、LOGON ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20888
$HASP000 RECORDED と AUDIT=JES2A20888 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MASDEF ステートメント 確認手順</strong></p><p>検証目的: MASDEF ステートメントについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MASDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MASDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20889
$HASP829 RECORDED と AUDIT=JES2A20889 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MASDEF OWNMEMB= 確認手順</strong></p><p>検証目的: MASDEF OWNMEMB=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MASDEF OWNMEMB=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MASDEF OWNMEMB=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20890
$HASP829 RECORDED と AUDIT=JES2A20890 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MASDEF SHARED=CHECK|NOCHECK 確認手順</strong></p><p>検証目的: MASDEF SHARED=CHECK|NOCHECKについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MASDEF SHARED=CHECK|NOCHECKの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MASDEF SHARED=CHECK|NOCHECKの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20891
$HASP829 RECORDED と AUDIT=JES2A20891 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MASDEF DORMANCY= 確認手順</strong></p><p>検証目的: MASDEF DORMANCY=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MASDEF DORMANCY=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MASDEF DORMANCY=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20892
$HASP829 RECORDED と AUDIT=JES2A20892 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MASDEF HOLD= 確認手順</strong></p><p>検証目的: MASDEF HOLD=について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MASDEF HOLD=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MASDEF HOLD=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20893
$HASP829 RECORDED と AUDIT=JES2A20893 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MASDEF RESTART=YES|NO 確認手順</strong></p><p>検証目的: MASDEF RESTART=YES|NOについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MASDEF RESTART=YES|NOの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MASDEF RESTART=YES|NOの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20894
$HASP829 RECORDED と AUDIT=JES2A20894 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NETACCT ステートメント 確認手順</strong></p><p>検証目的: NETACCT ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、NETACCT ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、NETACCT ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20895
$HASP000 RECORDED と AUDIT=JES2A20895 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NETSRV ステートメント 確認手順</strong></p><p>検証目的: NETSRV ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、NETSRV ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、NETSRV ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20896
$HASP000 RECORDED と AUDIT=JES2A20896 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJEDEF ステートメント 確認手順</strong></p><p>検証目的: NJEDEF ステートメントについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJEDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJEDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20897
$HASP815 RECORDED と AUDIT=JES2A20897 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJEDEF NODENUM= 確認手順</strong></p><p>検証目的: NJEDEF NODENUM=について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJEDEF NODENUM=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJEDEF NODENUM=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20898
$HASP815 RECORDED と AUDIT=JES2A20898 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJEDEF OWNNODE= 確認手順</strong></p><p>検証目的: NJEDEF OWNNODE=について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJEDEF OWNNODE=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJEDEF OWNNODE=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20899
$HASP815 RECORDED と AUDIT=JES2A20899 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJEDEF LINENUM= 確認手順</strong></p><p>検証目的: NJEDEF LINENUM=について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJEDEF LINENUM=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJEDEF LINENUM=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20900
$HASP815 RECORDED と AUDIT=JES2A20900 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NODE n ステートメント 確認手順</strong></p><p>検証目的: NODE n ステートメントについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NODE n ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NODE n ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20901
$HASP815 RECORDED と AUDIT=JES2A20901 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NODE n NAME= 確認手順</strong></p><p>検証目的: NODE n NAME=について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NODE n NAME=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NODE n NAME=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20902
$HASP815 RECORDED と AUDIT=JES2A20902 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NODE n AUTH= 確認手順</strong></p><p>検証目的: NODE n AUTH=について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NODE n AUTH=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NODE n AUTH=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20903
$HASP815 RECORDED と AUDIT=JES2A20903 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OFF n .JR ステートメント 確認手順</strong></p><p>検証目的: OFF n .JR ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、OFF n .JR ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、OFF n .JR ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20904
$HASP000 RECORDED と AUDIT=JES2A20904 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OFFLOAD ステートメント 確認手順</strong></p><p>検証目的: OFFLOAD ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、OFFLOAD ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、OFFLOAD ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20905
$HASP000 RECORDED と AUDIT=JES2A20905 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OUTCLASS ステートメント 確認手順</strong></p><p>検証目的: OUTCLASS ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、OUTCLASS ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、OUTCLASS ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20906
$HASP621 RECORDED と AUDIT=JES2A20906 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OUTCLASS OUTDISP= 確認手順</strong></p><p>検証目的: OUTCLASS OUTDISP=について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、OUTCLASS OUTDISP=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、OUTCLASS OUTDISP=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20907
$HASP621 RECORDED と AUDIT=JES2A20907 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OUTDEF ステートメント 確認手順</strong></p><p>検証目的: OUTDEF ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、OUTDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、OUTDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20908
$HASP621 RECORDED と AUDIT=JES2A20908 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OUTDEF JOENUM= 確認手順</strong></p><p>検証目的: OUTDEF JOENUM=について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、OUTDEF JOENUM=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、OUTDEF JOENUM=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20909
$HASP621 RECORDED と AUDIT=JES2A20909 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>OUTPRTY ステートメント 確認手順</strong></p><p>検証目的: OUTPRTY ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、OUTPRTY ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、OUTPRTY ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20910
$HASP621 RECORDED と AUDIT=JES2A20910 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>PCEDEF ステートメント 確認手順</strong></p><p>検証目的: PCEDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、PCEDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、PCEDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20911
$HASP000 RECORDED と AUDIT=JES2A20911 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>PRINTDEF ステートメント 確認手順</strong></p><p>検証目的: PRINTDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、PRINTDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、PRINTDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20912
$HASP000 RECORDED と AUDIT=JES2A20912 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>PROCLIB ステートメント 確認手順</strong></p><p>検証目的: PROCLIB ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、PROCLIB ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、PROCLIB ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20913
$HASP000 RECORDED と AUDIT=JES2A20913 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>PROCLIB DD= 確認手順</strong></p><p>検証目的: PROCLIB DD=について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、PROCLIB DD=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、PROCLIB DD=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20914
$HASP000 RECORDED と AUDIT=JES2A20914 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>PUNCHDEF ステートメント 確認手順</strong></p><p>検証目的: PUNCHDEF ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、PUNCHDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、PUNCHDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20915
$HASP621 RECORDED と AUDIT=JES2A20915 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>RECVOPTS ステートメント 確認手順</strong></p><p>検証目的: RECVOPTS ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、RECVOPTS ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、RECVOPTS ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20916
$HASP000 RECORDED と AUDIT=JES2A20916 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>REDIRECT ステートメント 確認手順</strong></p><p>検証目的: REDIRECT ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、REDIRECT ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、REDIRECT ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20917
$HASP000 RECORDED と AUDIT=JES2A20917 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>REQJOBID ステートメント 確認手順</strong></p><p>検証目的: REQJOBID ステートメントについて、JES2コマンド応答に$HASP890と対象資源JES0918が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0918を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、REQJOBID ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0918) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0918) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0918) NUMBER=1,ACTIVE=YES
$HASP890 と JES0918 が表示されていれば、REQJOBID ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0918
COMMAND=$D JOBDEF
AUDIT=JES2A20918
$HASP890 RECORDED と AUDIT=JES2A20918 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0918 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>RMT nnnn ステートメント 確認手順</strong></p><p>検証目的: RMT nnnn ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、RMT nnnn ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、RMT nnnn ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20919
$HASP000 RECORDED と AUDIT=JES2A20919 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SMFDEF ステートメント 確認手順</strong></p><p>検証目的: SMFDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、SMFDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、SMFDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20920
$HASP000 RECORDED と AUDIT=JES2A20920 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SPOOLDEF ステートメント 確認手順</strong></p><p>検証目的: SPOOLDEF ステートメントについて、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、SPOOLDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、SPOOLDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20921
$HASP646 RECORDED と AUDIT=JES2A20921 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SPOOLDEF VOLUME= 確認手順</strong></p><p>検証目的: SPOOLDEF VOLUME=について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、SPOOLDEF VOLUME=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、SPOOLDEF VOLUME=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20922
$HASP646 RECORDED と AUDIT=JES2A20922 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SPOOLDEF DSNAME= 確認手順</strong></p><p>検証目的: SPOOLDEF DSNAME=について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、SPOOLDEF DSNAME=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、SPOOLDEF DSNAME=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20923
$HASP646 RECORDED と AUDIT=JES2A20923 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SPOOLDEF TGSIZE= 確認手順</strong></p><p>検証目的: SPOOLDEF TGSIZE=について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、SPOOLDEF TGSIZE=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、SPOOLDEF TGSIZE=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20924
$HASP646 RECORDED と AUDIT=JES2A20924 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SPOOLDEF TGSPACE= 確認手順</strong></p><p>検証目的: SPOOLDEF TGSPACE=について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、SPOOLDEF TGSPACE=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、SPOOLDEF TGSPACE=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20925
$HASP646 RECORDED と AUDIT=JES2A20925 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SPOOLDEF FENCE= 確認手順</strong></p><p>検証目的: SPOOLDEF FENCE=について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、SPOOLDEF FENCE=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、SPOOLDEF FENCE=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20926
$HASP646 RECORDED と AUDIT=JES2A20926 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SSI ステートメント 確認手順</strong></p><p>検証目的: SSI ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、SSI ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、SSI ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20927
$HASP000 RECORDED と AUDIT=JES2A20927 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>STCCLASS ステートメント 確認手順</strong></p><p>検証目的: STCCLASS ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、STCCLASS ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、STCCLASS ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20928
$HASP621 RECORDED と AUDIT=JES2A20928 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>SUBTDEF ステートメント 確認手順</strong></p><p>検証目的: SUBTDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、SUBTDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、SUBTDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20929
$HASP000 RECORDED と AUDIT=JES2A20929 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>TPDEF ステートメント 確認手順</strong></p><p>検証目的: TPDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、TPDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、TPDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20930
$HASP000 RECORDED と AUDIT=JES2A20930 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>TRACE ステートメント 確認手順</strong></p><p>検証目的: TRACE ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、TRACE ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、TRACE ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20931
$HASP000 RECORDED と AUDIT=JES2A20931 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>TRACEDEF ステートメント 確認手順</strong></p><p>検証目的: TRACEDEF ステートメントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、TRACEDEF ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、TRACEDEF ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20932
$HASP000 RECORDED と AUDIT=JES2A20932 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>TSUCLASS ステートメント 確認手順</strong></p><p>検証目的: TSUCLASS ステートメントについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、TSUCLASS ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、TSUCLASS ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20933
$HASP621 RECORDED と AUDIT=JES2A20933 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ZAPJOB ステートメント 確認手順</strong></p><p>検証目的: ZAPJOB ステートメントについて、JES2コマンド応答に$HASP890と対象資源JES0934が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0934を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、ZAPJOB ステートメントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0934) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0934) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0934) NUMBER=1,ACTIVE=YES
$HASP890 と JES0934 が表示されていれば、ZAPJOB ステートメントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0934
COMMAND=$D JOBDEF
AUDIT=JES2A20934
$HASP890 RECORDED と AUDIT=JES2A20934 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0934 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 出口の登録手順 確認手順</strong></p><p>検証目的: JES2 出口の登録手順について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、JES2 出口の登録手順の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、JES2 出口の登録手順の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20935
$HASP000 RECORDED と AUDIT=JES2A20935 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>出口の動的有効化 確認手順</strong></p><p>検証目的: 出口の動的有効化について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、出口の動的有効化の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、出口の動的有効化の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20936
$HASP000 RECORDED と AUDIT=JES2A20936 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 1 JCL Input Scan 確認手順</strong></p><p>検証目的: EXIT 1 JCL Input Scanについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 1 JCL Input Scanの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 1 JCL Input Scanの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20937
$HASP000 RECORDED と AUDIT=JES2A20937 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 2 JOB 文 Scan 確認手順</strong></p><p>検証目的: EXIT 2 JOB 文 Scanについて、JES2コマンド応答に$HASP890と対象資源JES0938が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0938を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、EXIT 2 JOB 文 Scanの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0938) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0938) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0938) NUMBER=1,ACTIVE=YES
$HASP890 と JES0938 が表示されていれば、EXIT 2 JOB 文 Scanの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0938
COMMAND=$D JOBDEF
AUDIT=JES2A20938
$HASP890 RECORDED と AUDIT=JES2A20938 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0938 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 3 JES2 初期化 確認手順</strong></p><p>検証目的: EXIT 3 JES2 初期化について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 3 JES2 初期化の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 3 JES2 初期化の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20939
$HASP000 RECORDED と AUDIT=JES2A20939 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 4 ジョブセパレータ 確認手順</strong></p><p>検証目的: EXIT 4 ジョブセパレータについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 4 ジョブセパレータの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 4 ジョブセパレータの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20940
$HASP000 RECORDED と AUDIT=JES2A20940 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 5 コマンド事前処理 確認手順</strong></p><p>検証目的: EXIT 5 コマンド事前処理について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 5 コマンド事前処理の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 5 コマンド事前処理の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20941
$HASP000 RECORDED と AUDIT=JES2A20941 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 6 SMF レコード処理 確認手順</strong></p><p>検証目的: EXIT 6 SMF レコード処理について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 6 SMF レコード処理の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 6 SMF レコード処理の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20942
$HASP000 RECORDED と AUDIT=JES2A20942 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 6 と SMF Type 26 確認手順</strong></p><p>検証目的: EXIT 6 と SMF Type 26について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 6 と SMF Type 26の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 6 と SMF Type 26の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20943
$HASP000 RECORDED と AUDIT=JES2A20943 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 7 SYSOUT 制御 確認手順</strong></p><p>検証目的: EXIT 7 SYSOUT 制御について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、EXIT 7 SYSOUT 制御の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、EXIT 7 SYSOUT 制御の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20944
$HASP621 RECORDED と AUDIT=JES2A20944 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 8 $WTO/$WTOR 確認手順</strong></p><p>検証目的: EXIT 8 $WTO/$WTORについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 8 $WTO/$WTORの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 8 $WTO/$WTORの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20945
$HASP000 RECORDED と AUDIT=JES2A20945 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 9 Job Select WLM 確認手順</strong></p><p>検証目的: EXIT 9 Job Select WLMについて、JES2コマンド応答に$HASP890と対象資源JES0946が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JOBDEF を入力し、JES2応答で$HASP890とJES0946を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JOBDEF を入力し、EXIT 9 Job Select WLMの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JOBDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JOBDEF
COMMAND INPUT に /$D JOBDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JOBDEF の応答から$HASP890と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JOB STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D JOBDEF
$HASP890 JOB(JES0946) STATUS=EXECUTING,CLASS=A,PRIORITY=9
$HASP890 JOB(JES0946) OWNER=USER1,SPOOL=(SPOOL1),NODE=LOCAL
$HASP734 DUPJOB(JES0946) NUMBER=1,ACTIVE=YES
$HASP890 と JES0946 が表示されていれば、EXIT 9 Job Select WLMの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP890を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP890 RECORDED FOR JES0946
COMMAND=$D JOBDEF
AUDIT=JES2A20946
$HASP890 RECORDED と AUDIT=JES2A20946 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JOBDEF が画面・出力に表示されること
② ステップ 2 の $HASP890 が画面・出力に表示されること
③ ステップ 3 の JES0946 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 10 EOF 検出 確認手順</strong></p><p>検証目的: EXIT 10 EOF 検出について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 10 EOF 検出の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 10 EOF 検出の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20947
$HASP000 RECORDED と AUDIT=JES2A20947 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 11 スプールパーティション 確認手順</strong></p><p>検証目的: EXIT 11 スプールパーティションについて、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、EXIT 11 スプールパーティションの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、EXIT 11 スプールパーティションの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20948
$HASP646 RECORDED と AUDIT=JES2A20948 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 14 ジョブ統計 確認手順</strong></p><p>検証目的: EXIT 14 ジョブ統計について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 14 ジョブ統計の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 14 ジョブ統計の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20949
$HASP000 RECORDED と AUDIT=JES2A20949 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 15 出力選択 確認手順</strong></p><p>検証目的: EXIT 15 出力選択について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、EXIT 15 出力選択の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、EXIT 15 出力選択の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20950
$HASP621 RECORDED と AUDIT=JES2A20950 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 16 NOTIFY 確認手順</strong></p><p>検証目的: EXIT 16 NOTIFYについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 16 NOTIFYの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 16 NOTIFYの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20951
$HASP000 RECORDED と AUDIT=JES2A20951 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 18 $WTO ルーティング 確認手順</strong></p><p>検証目的: EXIT 18 $WTO ルーティングについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、EXIT 18 $WTO ルーティングの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、EXIT 18 $WTO ルーティングの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20952
$HASP815 RECORDED と AUDIT=JES2A20952 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 20 EOJ 処理 確認手順</strong></p><p>検証目的: EXIT 20 EOJ 処理について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 20 EOJ 処理の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 20 EOJ 処理の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20953
$HASP000 RECORDED と AUDIT=JES2A20953 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 22 Cancel/Status 確認手順</strong></p><p>検証目的: EXIT 22 Cancel/Statusについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 22 Cancel/Statusの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 22 Cancel/Statusの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20954
$HASP000 RECORDED と AUDIT=JES2A20954 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 24 Post-Init/$T 確認手順</strong></p><p>検証目的: EXIT 24 Post-Init/$Tについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、EXIT 24 Post-Init/$Tの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、EXIT 24 Post-Init/$Tの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20955
$HASP892 RECORDED と AUDIT=JES2A20955 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 25 SAPI 確認手順</strong></p><p>検証目的: EXIT 25 SAPIについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 25 SAPIの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 25 SAPIの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20956
$HASP000 RECORDED と AUDIT=JES2A20956 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 30 サブシステム IF 確認手順</strong></p><p>検証目的: EXIT 30 サブシステム IFについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 30 サブシステム IFの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 30 サブシステム IFの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20957
$HASP000 RECORDED と AUDIT=JES2A20957 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 36 TSO サブミット 確認手順</strong></p><p>検証目的: EXIT 36 TSO サブミットについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 36 TSO サブミットの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 36 TSO サブミットの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20958
$HASP000 RECORDED と AUDIT=JES2A20958 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 39 NJE 受信 確認手順</strong></p><p>検証目的: EXIT 39 NJE 受信について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、EXIT 39 NJE 受信の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、EXIT 39 NJE 受信の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20959
$HASP815 RECORDED と AUDIT=JES2A20959 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 40 NJE 送信 確認手順</strong></p><p>検証目的: EXIT 40 NJE 送信について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、EXIT 40 NJE 送信の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、EXIT 40 NJE 送信の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20960
$HASP815 RECORDED と AUDIT=JES2A20960 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 44 SYSOUT 受信 確認手順</strong></p><p>検証目的: EXIT 44 SYSOUT 受信について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、EXIT 44 SYSOUT 受信の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、EXIT 44 SYSOUT 受信の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20961
$HASP621 RECORDED と AUDIT=JES2A20961 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 49 出力 PCE 選択 確認手順</strong></p><p>検証目的: EXIT 49 出力 PCE 選択について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、EXIT 49 出力 PCE 選択の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(OUTPUT CLASS DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、EXIT 49 出力 PCE 選択の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A20962
$HASP621 RECORDED と AUDIT=JES2A20962 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 51 変換イベント 確認手順</strong></p><p>検証目的: EXIT 51 変換イベントについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、EXIT 51 変換イベントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、EXIT 51 変換イベントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A20963
$HASP000 RECORDED と AUDIT=JES2A20963 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>EXIT 60 TCP/IP NJE 確認手順</strong></p><p>検証目的: EXIT 60 TCP/IP NJEについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、EXIT 60 TCP/IP NJEの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、EXIT 60 TCP/IP NJEの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20964
$HASP815 RECORDED と AUDIT=JES2A20964 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>イニシエータの役割 確認手順</strong></p><p>検証目的: イニシエータの役割について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、イニシエータの役割の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、イニシエータの役割の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20965
$HASP892 RECORDED と AUDIT=JES2A20965 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 管理イニシエータ 確認手順</strong></p><p>検証目的: JES2 管理イニシエータについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、JES2 管理イニシエータの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、JES2 管理イニシエータの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20966
$HASP892 RECORDED と AUDIT=JES2A20966 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>WLM 管理イニシエータ 確認手順</strong></p><p>検証目的: WLM 管理イニシエータについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、WLM 管理イニシエータの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、WLM 管理イニシエータの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20967
$HASP892 RECORDED と AUDIT=JES2A20967 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$S INIT n と $P INIT n 確認手順</strong></p><p>検証目的: $S INIT n と $P INIT nについて、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、$S INIT n と $P INIT nの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$S INIT n と $P INIT nの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20968
$HASP892 RECORDED と AUDIT=JES2A20968 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$T INIT n CLASS= 確認手順</strong></p><p>検証目的: $T INIT n CLASS=について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、$T INIT n CLASS=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$T INIT n CLASS=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20969
$HASP892 RECORDED と AUDIT=JES2A20969 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$DI でのドレイン状態 確認手順</strong></p><p>検証目的: $DI でのドレイン状態について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$DI を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$DI を入力し、$DI でのドレイン状態の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$DI
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$DI
COMMAND INPUT に /$DI が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$DI の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$DI
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、$DI でのドレイン状態の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$DI
AUDIT=JES2A20970
$HASP892 RECORDED と AUDIT=JES2A20970 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $DI が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>WLM 管理時の同時実行数制御 確認手順</strong></p><p>検証目的: WLM 管理時の同時実行数制御について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、WLM 管理時の同時実行数制御の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、WLM 管理時の同時実行数制御の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20971
$HASP892 RECORDED と AUDIT=JES2A20971 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>WLM SRVCLASS との対応 確認手順</strong></p><p>検証目的: WLM SRVCLASS との対応について、JES2コマンド応答に$HASP892と対象資源BATINI01が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D INIT を入力し、JES2応答で$HASP892とBATINI01を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D INIT を入力し、WLM SRVCLASS との対応の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D INIT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D INIT
COMMAND INPUT に /$D INIT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D INIT の応答から$HASP892と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(INITIATOR DISPLAY)
COMMAND INPUT ===&gt; /$D INIT
$HASP892 INIT(01) NAME=BATINI01,CLASS=A,STATUS=ACTIVE
$HASP892 INIT(02) NAME=BATINI02,CLASS=B,STATUS=DRAINED
$HASP892 INITDEF PARTNUM=9999
$HASP892 と BATINI01 が表示されていれば、WLM SRVCLASS との対応の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP892を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP892 RECORDED FOR BATINI01
COMMAND=$D INIT
AUDIT=JES2A20972
$HASP892 RECORDED と AUDIT=JES2A20972 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D INIT が画面・出力に表示されること
② ステップ 2 の $HASP892 が画面・出力に表示されること
③ ステップ 3 の BATINI01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS の概念 確認手順</strong></p><p>検証目的: MAS の概念について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS の概念の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS の概念の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20973
$HASP829 RECORDED と AUDIT=JES2A20973 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS 最大メンバー数 確認手順</strong></p><p>検証目的: MAS 最大メンバー数について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS 最大メンバー数の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS 最大メンバー数の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20974
$HASP829 RECORDED と AUDIT=JES2A20974 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS スプール共有 確認手順</strong></p><p>検証目的: MAS スプール共有について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、MAS スプール共有の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、MAS スプール共有の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20975
$HASP646 RECORDED と AUDIT=JES2A20975 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS チェックポイント 確認手順</strong></p><p>検証目的: MAS チェックポイントについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS チェックポイントの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS チェックポイントの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20976
$HASP829 RECORDED と AUDIT=JES2A20976 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS と RESERVE 確認手順</strong></p><p>検証目的: MAS と RESERVEについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS と RESERVEの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS と RESERVEの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20977
$HASP829 RECORDED と AUDIT=JES2A20977 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS と CF Structure 確認手順</strong></p><p>検証目的: MAS と CF Structureについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS と CF Structureの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS と CF Structureの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20978
$HASP829 RECORDED と AUDIT=JES2A20978 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS メンバー追加 確認手順</strong></p><p>検証目的: MAS メンバー追加について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS メンバー追加の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS メンバー追加の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20979
$HASP829 RECORDED と AUDIT=JES2A20979 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>MAS メンバー停止 確認手順</strong></p><p>検証目的: MAS メンバー停止について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、MAS メンバー停止の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、MAS メンバー停止の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20980
$HASP829 RECORDED と AUDIT=JES2A20980 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJE の目的 確認手順</strong></p><p>検証目的: NJE の目的について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJE の目的の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE の目的の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20981
$HASP815 RECORDED と AUDIT=JES2A20981 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJE トランスポート種別 確認手順</strong></p><p>検証目的: NJE トランスポート種別について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJE トランスポート種別の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE トランスポート種別の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20982
$HASP815 RECORDED と AUDIT=JES2A20982 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJE over TCP/IP の構成 確認手順</strong></p><p>検証目的: NJE over TCP/IP の構成について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJE over TCP/IP の構成の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE over TCP/IP の構成の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20983
$HASP815 RECORDED と AUDIT=JES2A20983 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NODE n NAME 必須要件 確認手順</strong></p><p>検証目的: NODE n NAME 必須要件について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NODE n NAME 必須要件の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NODE n NAME 必須要件の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20984
$HASP815 RECORDED と AUDIT=JES2A20984 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NODE n AUTH パラメータ 確認手順</strong></p><p>検証目的: NODE n AUTH パラメータについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NODE n AUTH パラメータの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NODE n AUTH パラメータの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20985
$HASP815 RECORDED と AUDIT=JES2A20985 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CONNECT による経路 確認手順</strong></p><p>検証目的: CONNECT による経路について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、CONNECT による経路の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、CONNECT による経路の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20986
$HASP815 RECORDED と AUDIT=JES2A20986 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>NJE と DEST/ROUTECDE 確認手順</strong></p><p>検証目的: NJE と DEST/ROUTECDEについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、NJE と DEST/ROUTECDEの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、NJE と DEST/ROUTECDEの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A20987
$HASP815 RECORDED と AUDIT=JES2A20987 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>スプール拡張手順 確認手順</strong></p><p>検証目的: スプール拡張手順について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、スプール拡張手順の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、スプール拡張手順の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20988
$HASP646 RECORDED と AUDIT=JES2A20988 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>スプール縮小 ドレイン 手順 確認手順</strong></p><p>検証目的: スプール縮小 ドレイン 手順について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、スプール縮小 ドレイン 手順の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、スプール縮小 ドレイン 手順の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20989
$HASP646 RECORDED と AUDIT=JES2A20989 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>スプール使用率監視 確認手順</strong></p><p>検証目的: スプール使用率監視について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、スプール使用率監視の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、スプール使用率監視の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20990
$HASP646 RECORDED と AUDIT=JES2A20990 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>TG Track Group 確認手順</strong></p><p>検証目的: TG Track Groupについて、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、TG Track Groupの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、TG Track Groupの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20991
$HASP646 RECORDED と AUDIT=JES2A20991 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>TGSPACE WARN= 確認手順</strong></p><p>検証目的: TGSPACE WARN=について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、TGSPACE WARN=の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、TGSPACE WARN=の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20992
$HASP646 RECORDED と AUDIT=JES2A20992 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$HASP050 スプール満杯 確認手順</strong></p><p>検証目的: $HASP050 スプール満杯について、JES2コマンド応答に$HASP646と対象資源SPOOL1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D SPOOLDEF を入力し、JES2応答で$HASP646とSPOOL1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D SPOOLDEF を入力し、$HASP050 スプール満杯の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D SPOOLDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D SPOOLDEF
COMMAND INPUT に /$D SPOOLDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D SPOOLDEF の応答から$HASP646と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(SPOOL STATUS DISPLAY)
COMMAND INPUT ===&gt; /$D SPOOLDEF
$HASP646 25 PERCENT SPOOL UTILIZATION
$HASP630 VOLUME SPOOL1 ACTIVE 25 PERCENT UTILIZATION
$HASP893 VOLUME(SPOOL1) STATUS=ACTIVE,AWAITING(EXTEND),PERCENT=25
$HASP646 と SPOOL1 が表示されていれば、$HASP050 スプール満杯の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP646を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP646 RECORDED FOR SPOOL1
COMMAND=$D SPOOLDEF
AUDIT=JES2A20993
$HASP646 RECORDED と AUDIT=JES2A20993 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D SPOOLDEF が画面・出力に表示されること
② ステップ 2 の $HASP646 が画面・出力に表示されること
③ ステップ 3 の SPOOL1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPT の役割 確認手順</strong></p><p>検証目的: CKPT の役割について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPT の役割の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPT の役割の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20994
$HASP829 RECORDED と AUDIT=JES2A20994 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPT1/CKPT2 の二重化 確認手順</strong></p><p>検証目的: CKPT1/CKPT2 の二重化について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPT1/CKPT2 の二重化の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPT1/CKPT2 の二重化の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20995
$HASP829 RECORDED と AUDIT=JES2A20995 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPT 切替 $T CKPTDEF 確認手順</strong></p><p>検証目的: CKPT 切替 $T CKPTDEFについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPT 切替 $T CKPTDEFの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPT 切替 $T CKPTDEFの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20996
$HASP829 RECORDED と AUDIT=JES2A20996 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>DASD vs CF CKPT 確認手順</strong></p><p>検証目的: DASD vs CF CKPTについて、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、DASD vs CF CKPTの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、DASD vs CF CKPTの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20997
$HASP829 RECORDED と AUDIT=JES2A20997 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPT ロック保持時間 確認手順</strong></p><p>検証目的: CKPT ロック保持時間について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPT ロック保持時間の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPT ロック保持時間の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20998
$HASP829 RECORDED と AUDIT=JES2A20998 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>CKPT サイズ拡張 確認手順</strong></p><p>検証目的: CKPT サイズ拡張について、JES2コマンド応答に$HASP829と対象資源CKPT1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CKPTDEF を入力し、JES2応答で$HASP829とCKPT1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CKPTDEF を入力し、CKPT サイズ拡張の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CKPTDEF
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CKPTDEF
COMMAND INPUT に /$D CKPTDEF が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CKPTDEF の応答から$HASP829と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(CHECKPOINT DISPLAY)
COMMAND INPUT ===&gt; /$D CKPTDEF
$HASP829 CKPTDEF CKPT1=(DSNAME=SYS1.JES2.CKPT1,VOLSER=J2CKP1)
$HASP829 CKPTDEF CKPT2=(DSNAME=SYS1.JES2.CKPT2,VOLSER=J2CKP2)
$HASP829 CKPTDEF MODE=DUPLEX
$HASP829 と CKPT1 が表示されていれば、CKPT サイズ拡張の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP829を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP829 RECORDED FOR CKPT1
COMMAND=$D CKPTDEF
AUDIT=JES2A20999
$HASP829 RECORDED と AUDIT=JES2A20999 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CKPTDEF が画面・出力に表示されること
② ステップ 2 の $HASP829 が画面・出力に表示されること
③ ステップ 3 の CKPT1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTECDE の役割 確認手順</strong></p><p>検証目的: ROUTECDE の役割について、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、ROUTECDE の役割の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、ROUTECDE の役割の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A21000
$HASP621 RECORDED と AUDIT=JES2A21000 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTECDE LOCAL 確認手順</strong></p><p>検証目的: ROUTECDE LOCALについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、ROUTECDE LOCALの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、ROUTECDE LOCALの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A21001
$HASP621 RECORDED と AUDIT=JES2A21001 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTECDE NODE 確認手順</strong></p><p>検証目的: ROUTECDE NODEについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、ROUTECDE NODEの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、ROUTECDE NODEの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A21002
$HASP815 RECORDED と AUDIT=JES2A21002 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTECDE Uxxxxxxx 確認手順</strong></p><p>検証目的: ROUTECDE Uxxxxxxxについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、ROUTECDE Uxxxxxxxの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、ROUTECDE Uxxxxxxxの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A21003
$HASP621 RECORDED と AUDIT=JES2A21003 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTECDE Rnnnn 確認手順</strong></p><p>検証目的: ROUTECDE Rnnnnについて、JES2コマンド応答に$HASP621と対象資源OUTCLASSが現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D OUTCLASS を入力し、JES2応答で$HASP621とOUTCLASSを確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D OUTCLASS を入力し、ROUTECDE Rnnnnの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D OUTCLASS
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D OUTCLASS
COMMAND INPUT に /$D OUTCLASS が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D OUTCLASS の応答から$HASP621と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D OUTCLASS
$HASP621 OUTCLASS(A) OUTPUT QUEUE DISPLAY
$HASP621 CLASS=A FORMS=STD HOLD=NO ROUTE=LOCAL
$HASP621 WRITER=PRT1 STATUS=ACTIVE
$HASP621 と OUTCLASS が表示されていれば、ROUTECDE Rnnnnの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP621を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP621 RECORDED FOR OUTCLASS
COMMAND=$D OUTCLASS
AUDIT=JES2A21004
$HASP621 RECORDED と AUDIT=JES2A21004 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D OUTCLASS が画面・出力に表示されること
② ステップ 2 の $HASP621 が画面・出力に表示されること
③ ステップ 3 の OUTCLASS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>DEST パラメータ 確認手順</strong></p><p>検証目的: DEST パラメータについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、DEST パラメータの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、DEST パラメータの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A21005
$HASP815 RECORDED と AUDIT=JES2A21005 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>DESTID ステートメント連携 確認手順</strong></p><p>検証目的: DESTID ステートメント連携について、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、DESTID ステートメント連携の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、DESTID ステートメント連携の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A21006
$HASP815 RECORDED と AUDIT=JES2A21006 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>ANYLOCAL 確認手順</strong></p><p>検証目的: ANYLOCALについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、ANYLOCALの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、ANYLOCALの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A21007
$HASP815 RECORDED と AUDIT=JES2A21007 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>WTR Writer ルーティング 確認手順</strong></p><p>検証目的: WTR Writer ルーティングについて、JES2コマンド応答に$HASP815と対象資源REMOTE1が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D CONNECT を入力し、JES2応答で$HASP815とREMOTE1を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D CONNECT を入力し、WTR Writer ルーティングの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D CONNECT
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D CONNECT
COMMAND INPUT に /$D CONNECT が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D CONNECT の応答から$HASP815と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(NJE CONNECTION DISPLAY)
COMMAND INPUT ===&gt; /$D CONNECT
$HASP815 CONNECT NODEA=LOCAL,MEMBERA=1,NODEB=REMOTE1
$HASP815         MEMBERB=1,REST=8000,STATUS=ACTIVE,STATE=PENDING
$HASP815         STATIC=YES,PATHMGR=YES
$HASP815 と REMOTE1 が表示されていれば、WTR Writer ルーティングの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP815を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP815 RECORDED FOR REMOTE1
COMMAND=$D CONNECT
AUDIT=JES2A21008
$HASP815 RECORDED と AUDIT=JES2A21008 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D CONNECT が画面・出力に表示されること
② ステップ 2 の $HASP815 が画面・出力に表示されること
③ ステップ 3 の REMOTE1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$HASP メッセージプレフィックス 確認手順</strong></p><p>検証目的: $HASP メッセージプレフィックスについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$HASP メッセージプレフィックスの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$HASP メッセージプレフィックスの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21009
$HASP000 RECORDED と AUDIT=JES2A21009 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 Hot Start 確認手順</strong></p><p>検証目的: JES2 Hot Startについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、JES2 Hot Startの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、JES2 Hot Startの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21010
$HASP000 RECORDED と AUDIT=JES2A21010 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 Warm Start 確認手順</strong></p><p>検証目的: JES2 Warm Startについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、JES2 Warm Startの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、JES2 Warm Startの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21011
$HASP000 RECORDED と AUDIT=JES2A21011 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 Cold Start 確認手順</strong></p><p>検証目的: JES2 Cold Startについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、JES2 Cold Startの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、JES2 Cold Startの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21012
$HASP000 RECORDED と AUDIT=JES2A21012 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 All-member Warm Start 確認手順</strong></p><p>検証目的: JES2 All-member Warm Startについて、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、JES2 All-member Warm Startの確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、JES2 All-member Warm Startの確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21013
$HASP000 RECORDED と AUDIT=JES2A21013 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>$ACTIVATE の役割 確認手順</strong></p><p>検証目的: $ACTIVATE の役割について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、$ACTIVATE の役割の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 OPERATOR COMMAND DISPLAY)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、$ACTIVATE の役割の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21014
$HASP000 RECORDED と AUDIT=JES2A21014 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div><div class="kb-p"><p class="kb-pname"><strong>JES2 と SAF/RACF 連携 確認手順</strong></p><p>検証目的: JES2 と SAF/RACF 連携について、JES2コマンド応答に$HASP000と対象資源JES2が現れることを机上で確認します。</p><p>前提条件: SDSFまたはMVSコンソールからJES2コマンドを送信できる権限があり、対象JES2メンバー、コマンド権限、影響範囲を変更管理で確認済みであること。</p><p>セッション環境: SDSFのCOMMAND INPUTから /$D JES2 を入力し、JES2応答で$HASP000とJES2を確認します。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に /$D JES2 を入力し、JES2 と SAF/RACF 連携の確認に必要なJES2応答を要求します。
［操作（入力）］
(SDSF PRIMARY OPTION MENU)
COMMAND INPUT ===&gt; /$D JES2
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; /$D JES2
COMMAND INPUT に /$D JES2 が表示されていれば、JES2へ送るコマンド文字列を確認できます。
――――
■ ステップ 2
現在の画面はJES2コマンド応答の表示画面です。前ステップで送った /$D JES2 の応答から$HASP000と対象資源を読み取ります。
［操作（入力）］
→ Enter を押す
［画面・出力］
(JES2 COMMAND RESPONSE)
COMMAND INPUT ===&gt; /$D JES2
$HASP000 OK
$HASP100 JES2 COMMAND ACCEPTED
$HASP150 JES2 RESOURCE DISPLAY COMPLETE
$HASP000 と JES2 が表示されていれば、JES2 と SAF/RACF 連携の確認に必要なJES2応答を取得できています。
――――
■ ステップ 3
現在の画面はSDSFの一覧画面です。NP欄に S を入力し、$HASP000を含む応答を保存対象として選択します。
［操作（入力）］
NP   JOBNAME  JobID    Owner    Queue
S    JES2LOG  STC00001 SYS1     PRINT
→ Enter を押す
［画面・出力］
(SDSF OUTPUT DATA SET)
$HASP000 RECORDED FOR JES2
COMMAND=$D JES2
AUDIT=JES2A21015
$HASP000 RECORDED と AUDIT=JES2A21015 が表示されていれば、机上例では確認結果を証跡として残せています。
――――</pre><p>合格条件: ① ステップ 1 の $D JES2 が画面・出力に表示されること
② ステップ 2 の $HASP000 が画面・出力に表示されること
③ ステップ 3 の JES2 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS JES2</p></div></details></section>
