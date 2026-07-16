---
search:
  exclude: true
---

# Sysplex / XCF / GRS / CF — 詳細 (1/1)

[← Sysplex / XCF / GRS / CF の概要へ戻る](index.md)


## ARM


<section class="kb-item" id="c29-i0001"><h3>ARM の役割</h3><p class="kb-meta">分類: ARM ・ 難易度: 上級</p><p>Sysplex 内で特定のジョブ/STC を 障害時に同一または別システムへ自動再起動する。CICS, IMS, DB2, MQ などの長期常駐サブシステムの自動回復に用いる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0002"><h3>ARM ポリシーの活性化</h3><p class="kb-meta">分類: ARM ・ 難易度: 上級</p><p>SETXCF START,POLICY,TYPE=ARM,POLNAME=xxx。複数ポリシー保持・切替が可能。IXCMIAPU で DATA TYPE(ARM) として登録する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0003"><h3>ELEMENT 定義</h3><p class="kb-meta">分類: ARM ・ 難易度: 上級</p><p>再起動対象を一意に識別するエレメント名と再起動方法 (RESTART_METHOD: PERSIST/STC/JOB/SYSTERM/SYSGONE) を指定する。コードでは IXCARM REGISTER 実行が必要</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0004"><h3>JES2/JES3 との連携</h3><p class="kb-meta">分類: ARM ・ 難易度: 上級</p><p>ARM 再起動は JES サブシステムが先に Up している必要がある。RESTART_GROUP 内に JES 自身を入れない/外部監視からの起動順序を設計する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0005"><h3>READYTIMEOUT / TERMTYPE</h3><p class="kb-meta">分類: ARM ・ 難易度: 上級</p><p>READYTIMEOUT は再起動準備完了待ち時間、TERMTYPE は終了種別と判定(ELEMTERM/SYSTERM)。失敗時は ARM が次のシステムを探す</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0006"><h3>RESTART_GROUP</h3><p class="kb-meta">分類: ARM ・ 難易度: 上級</p><p>RESTART_GROUPは、Sysplex / XCF / GRS / CFのARMで機能名、見出し、または確認対象として参照する項目です。セットで同期再起動したい要素群を 1 つのリスタートグループとして定義する。グループ内のすべての ELEMENT が再起動可能になるのを待ってから再起動される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## CDS サイズ計算


<section class="kb-item" id="c29-i0007"><h3>CFRM CDS の ITEM</h3><p class="kb-meta">分類: CDS サイズ計算 ・ 難易度: 上級</p><p>POLICY, CF, STR, CONNECT(POLICY/CF/STR/CONN/SMREBLD/MSGBASED) の各上限を ITEM NAME 指定で宣言する。STR 数を増やすと将来の構造追加に余裕ができる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0008"><h3>IXCL1DSU の役割</h3><p class="kb-meta">分類: CDS サイズ計算 ・ 難易度: 中級</p><p>IXCL1DSU の役割は、Sysplex / XCF / GRS / CFのCDS サイズ計算で機能名、見出し、または確認対象として参照する項目です。Couple Data Set フォーマット用バッチユーティリティ。DATA TYPE と ITEM パラメータでサイズを宣言し、SHAREOPTIONS(3,3) の VSAM LDS として作成する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0009"><h3>SFM / ARM / LOGR の ITEM</h3><p class="kb-meta">分類: CDS サイズ計算 ・ 難易度: 上級</p><p>SFM / ARM / LOGR の ITEMは、Sysplex / XCF / GRS / CFのCDS サイズ計算で機能名、見出し、または確認対象として参照する項目です。SFM=POLICY/SYSTEM、ARM=POLICY/RESTART_GROUP/ELEMENT、LOGR=LSR(LogStream)/DSEXTENT/SMDUPLEX 等を ITEM で指定する。下回ると追加定義が拒否される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0010"><h3>Sysplex CDS の ITEM</h3><p class="kb-meta">分類: CDS サイズ計算 ・ 難易度: 中級</p><p>MAXSYSTEM (最大システム数)、MAXGROUP (最大 XCF グループ数)、MAXMEMBER (グループあたり最大メンバ数) の 3 つを IXCL1DSU の DATA TYPE(SYSPLEX) で宣言する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0011"><h3>再フォーマットの必要性</h3><p class="kb-meta">分類: CDS サイズ計算 ・ 難易度: 中級</p><p>ITEM 上限を増やすには新しい CDS を IXCL1DSU で作成し、SETXCF COUPLE,ACOUPLE で組込 から SETXCF COUPLE,PSWITCH でプライマリ昇格させる無停止切替が標準手順</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## CFRM


<section class="kb-item" id="c29-i0012"><h3>CF DEFINE (NAME/TYPE/PARTITION/CPCID/SIDE)</h3><p class="kb-meta">分類: CFRM ・ 難易度: 上級</p><p>Coupling Facility 自体の定義。NAME(CF 論理名)、TYPE(CF モデル)、PARTITION(LPAR ID)、CPCID(CPC シリアル)、SIDE(物理位置) で個々の CF イメージを識別する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0013"><h3>CFRM の役割</h3><p class="kb-meta">分類: CFRM ・ 難易度: 上級</p><p>Coupling Facility リソース(CF と Structure)の管理ポリシーを Sysplex 全体に配布する仕組み。IXCMIAPU で管理データを CFRM CDS に登録し、SETXCF START,POLICY で活性化する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0014"><h3>CFRM ポリシーの活性化</h3><p class="kb-meta">分類: CFRM ・ 難易度: 上級</p><p>SETXCF START,POLICY,TYPE=CFRM,POLNAME=xxx で活性化。複数ポリシーを CDS に保持して切替えできる。STOP では既存接続は維持される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0015"><h3>DUPLEX 制御</h3><p class="kb-meta">分類: CFRM ・ 難易度: 上級</p><p>DUPLEX 制御は、Sysplex / XCF / GRS / CFのCFRMで機能名、見出し、または確認対象として参照する項目です。Structure 単位で DUPLEX(ENABLED/ALLOWED/DISABLED) を指定し、System-Managed Duplexing の対象を制御する。Lock/List 構造は MSGBASED Duplexing が推奨される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0016"><h3>IXCMIAPU ユーティリティ</h3><p class="kb-meta">分類: CFRM ・ 難易度: 上級</p><p>CFRM/SFM/ARM/LOGR ポリシー定義用バッチユーティリティ。DATA TYPE(CFRM) を指定し、DEFINE POLICY NAME(...) と DEFINE CF, DEFINE STRUCTURE 等のステートメントを記述する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0017"><h3>MSGBASED Protocol</h3><p class="kb-meta">分類: CFRM ・ 難易度: 上級</p><p>CFRM 制御を CDS ベースから MSGBASED(XCF メッセージベース) に切替えるとポリシー操作の応答が速くなる。z/OS 1.8 以降の推奨。SETXCF MODIFY,CFRM,MSGBASED=YES</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## CFRM Structure


<section class="kb-item" id="c29-i0018"><h3>ALLOWAUTOALT</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>実行時に構造サイズや Entry/Element 比を WLM/XES が自動調整することを許可する。CFSizer 推奨値からの逸脱を吸収するチューニング省力化機能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0019"><h3>CFLEVEL 要件</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>CFLEVEL 要件は、Sysplex / XCF / GRS / CFのCFRM Structureで確認する項目です。構造種別ごとに最低 CFLEVEL が要求される(例 List Notification Vector 拡張は CFLEVEL 以上15)。PREFLIST 上の全 CF が要件を満たすことが必要</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0020"><h3>DUPLEX(ENABLED/ALLOWED/DISABLED)</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>DUPLEX(ENABLED/ALLOWED/DISABLED)は、Sysplex / XCF / GRS / CFのCFRM Structureで機能名、見出し、または確認対象として参照する項目です。System-Managed Duplexing の許可レベル。ENABLED は自動二重化、ALLOWED はオペレータ要求で二重化、DISABLED は二重化禁止</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0021"><h3>ENFORCEORDER</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>ENFORCEORDERは、Sysplex / XCF / GRS / CFのCFRM Structureで機能名、見出し、または確認対象として参照する項目です。PREFLIST の先頭 CF にあくまで割り付ける制御。可用性より配置安定を優先したい場合に使う。AutoAlter/Rebuild との挙動差異に注意</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0022"><h3>EXCLLIST (Exclusion List)</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>同じ CF 上に置きたくない構造の共存禁止リスト。可用性向上のため Lock/List のペアを別 CF に分散する目的で使用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0023"><h3>MINSIZE</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>MINSIZEは、Sysplex / XCF / GRS / CFのCFRM Structureで機能名、見出し、または確認対象として参照する項目です。ALLOWAUTOALT 環境で AutoAlter が縮小可能な下限を指定。指定しない場合は INITSIZE がデフォルト下限となる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0024"><h3>PREFLIST (Preference List)</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>構造を割り当てる CF の優先順序リスト。先頭から順に試行され、容量・接続性を満たす最初の CF が選ばれる。Rebuild 時は先頭優先で再配置される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0025"><h3>REBUILDPERCENT</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>REBUILDPERCENTは、Sysplex / XCF / GRS / CFのCFRM Structureで機能名、見出し、または確認対象として参照する項目です。Connectivity Failure 時に Rebuild を実行する判定閾値(%)。生き残ったコネクションの比率がこの値以上なら Rebuild、未満なら接続切断とする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0026"><h3>SIZE / INITSIZE</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>INITSIZE で初期割当、SIZE で最大割当を指定する。CFSizer ツールで算出した値を反映するのが基本で、INITSIZE&lt;SIZE の場合は ALLOWAUTOALT で自動拡張可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0027"><h3>STRUCTURE NAME</h3><p class="kb-meta">分類: CFRM Structure ・ 難易度: 上級</p><p>STRUCTURE NAMEは、Sysplex / XCF / GRS / CFのCFRM Structureで機能名、見出し、または確認対象として参照する項目です。16 文字以内の構造論理名。製品が要求する名称規則(例 ISGLOCK, IRLMLOCK1, DSNDB0G_GBP1) に合わせて命名する。命名は連結アプリ側のリンクキーとなる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## COUPLExx


<section class="kb-item" id="c29-i0028"><h3>CLASSDEF (Transport Class)</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>XCF Transport Class を定義する。CLASSDEF CLASS(DEFAULT) CLASSLEN(956) MAXMSG(2000) GROUP(UNDESIG) のように、長さ・最大メッセージ数・対応グループを指定する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0029"><h3>CLEANUP(n)</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>システム除去時の XCF メンバ後処理タイムアウト(秒)。デフォルト 15。長すぎると Sysplex Wait 状態が長引く</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0030"><h3>COUPLExx の動的反映</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>COUPLExx の動的反映は、Sysplex / XCF / GRS / CFのCOUPLExxで機能名、見出し、または確認対象として参照する項目です。SETXCF COUPLE,PCOUPLE=/ACOUPLE= や SETXCF MODIFY によって一部要素は IPL 不要で反映可能だが、PLEXCFG・Sysplex 名・INTERVAL の一部は IPL マイグレーションが必要</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0031"><h3>COUPLExx の役割</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>IEASYSxx の COUPLE= 指定で参照される PARMLIB メンバ。Sysplex 名、PLEXCFG、各種 CDS 配置、CLASSDEF/PATHIN/PATHOUT/LOCALMSG、CFRM/SFM 等の起動有無を一括定義する。NIP フェーズで読み込まれる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0032"><h3>DATA TYPE(CFRM/SFM/ARM/WLM/LOGR/BPXMCDS)</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 上級</p><p>DATA TYPE(CFRM/SFM/ARM/WLM/LOGR/BPXMCDS)は、Sysplex / XCF / GRS / CFのCOUPLExxで機能名、見出し、または確認対象として参照する項目です。各機能用 CDS を同じ DATA TYPE 構文で個別に登録する。指定された機能のみ NIP/IPL 後に有効化される。CDS が無い機能はそのサービスが非活性となる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0033"><h3>DATA TYPE(SYSPLEX) ステートメント</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>Sysplex CDS のプライマリ/オルタネートを定義する。例: DATA TYPE(SYSPLEX) PCOUPLE(SYS1.PCOUPLE) ACOUPLE(SYS1.ACOUPLE)。最低限必要な CDS 指定</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0034"><h3>INTERVAL / OPNOTIFY</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>XCF の Status Monitor インターバル(秒)とオペレータ通知タイムアウト。例: INTERVAL(85) OPNOTIFY(90)。Sysplex Failure Management 未使用時のシステム障害検出時間に影響</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0035"><h3>LOCALMSG</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>同一 LPAR 内 XCF クライアントへのメッセージング用ローカルバッファ。LOCALMSG MAXMSG(n) で予約量を指定する。性能チューニング項目</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0036"><h3>MAXMSG (System Default)</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>PATHOUT/CLASSDEF 個別指定が無い場合の既定 MAXMSG 値。Sysplex 規模に応じて増量するチューニング対象</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0037"><h3>PATHIN / PATHOUT 指定</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>XCF シグナリングの入力/出力経路を CTC (DEVICE) または CF 構造 (STRNAME) で指定する。例: PATHOUT STRNAME(IXC_DEFAULT_1)、PATHIN DEVICE(0E20,0E21)。複数記述可</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0038"><h3>RETRY</h3><p class="kb-meta">分類: COUPLExx ・ 難易度: 中級</p><p>RETRYは、Sysplex / XCF / GRS / CFのCOUPLExxで機能名、見出し、または確認対象として参照する項目です。シグナリング経路エラー時のリトライ回数。RETRY(10) が一般的デフォルト。経路品質に応じ調整。複数経路を持つ構成では、単なるエラー回避ではなく、経路障害時の切替時間とオペレータ通知の遅れを合わせて見る</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## Couple Data Set


<section class="kb-item" id="c29-i0039"><h3>ARM CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 上級</p><p>ARM CDSは、Sysplex / XCF / GRS / CFのCouple Data Setで機能名、見出し、または確認対象として参照する項目です。Automatic Restart Management ポリシーを格納する。ARM が定義した要素(STC/JOB)を障害時に同一/別システムで自動再起動する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0040"><h3>BPXMCDS (OMVS) CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>z/OS UNIX Shared File System (Shared HFS/zFS) の所有権・マウント情報を Sysplex 内で共有するための CDS。BPXPRMxx の SYSPLEX(YES) と組で使用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0041"><h3>CDS とは</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>Sysplex 全体で共有する制御情報を格納する VSAM 形式の DASD データセット。プライマリと(できれば物理的に別ボリュームの)オルタネートを必ずペアで構成する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0042"><h3>CDS の暗号化対応</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>z/OS Data Set Encryption により CDS も暗号化可能。鍵を扱う ICSF が IPL 早期に活性化される必要があり、IPL 順序とキャッシュ鍵セットの要件に注意する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0043"><h3>CDS 配置のベストプラクティス</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>プライマリ/オルタネートを別 DASD サブシステム・別チャネルパスに配置し、Sysplex CDS と他 CDS をできるだけ別ボリュームに分散して I/O 集中と単一障害点を排除する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0044"><h3>CFRM CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 上級</p><p>CFRM ポリシー (CF 定義/STRUCTURE 定義) を保持。CFRM CDS 不在時は CF を利用するサービス (GRS Star, DB2 GBP 等) が起動できない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0045"><h3>DISPLAY XCF,COUPLE</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>全 CDS の現用名・スペア・I/O 状況を表示する。例: D XCF,COUPLE,TYPE=(SYSPLEX,CFRM,SFM)。日常運用での標準確認コマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0046"><h3>FORMAT TYPE 一致原則</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>プライマリ/オルタネートはバージョン・容量(ITEM)・FORMAT パラメータが完全一致している必要がある。不一致だと SETXCF COUPLE,ACOUPLE が拒否される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0047"><h3>LOGR CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 上級</p><p>System Logger ログストリーム定義および接続/オフロード状態を保持する。LOGR CDS は CFRM とほぼ常時必須で、SYSLOG/OPERLOG/CICS LSR/RRS の前提となる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0048"><h3>Primary / Alternate / Spare</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>全 CDS は PRIMARY と ALTERNATE をペアで用意し、運用中の SPARE CDS を SETXCF で切替可能とする 3 面構成が推奨される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0049"><h3>SFM CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 上級</p><p>Sysplex Failure Management ポリシー (SYSTEM/RECONFIG/PROMPT/ISOLATETIME/CONNFAIL/MEMSTALLTIME 等) を格納する。SFM 未活性時は IXC402D の手動応答に依存する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0050"><h3>Sysplex CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>システム参加状況、XCF グループ/メンバ、ハートビート情報を保持する最重要 CDS。Sysplex CDS が両系喪失すると Sysplex は停止する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0051"><h3>WLM CDS</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>WLM サービス定義 (Service Policy / Classification Rules / Service Class) を格納する。Sysplex 全 LPAR で同一 WLM ポリシーを共有する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0052"><h3>プライマリ喪失時の動作</h3><p class="kb-meta">分類: Couple Data Set ・ 難易度: 中級</p><p>プライマリ CDS I/O エラー時は自動的にオルタネートをプライマリへ昇格させ、オルタネートが空席となる。SPARE があれば SETXCF COUPLE,ACOUPLE= で補充する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## D GRS


<section class="kb-item" id="c29-i0053"><h3>D GRS</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRSは、Sysplex / XCF / GRS / CFのD GRSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS MVS Planning: Global Resource Serialization、z/OS MVS Initialization and Tuning Reference を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0054"><h3>D GRS,ANALYZE</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,ANALYZEは、Sysplex / XCF / GRS / CFのD GRSで機能名、見出し、または確認対象として参照する項目です。DEPENDENCY/WAITER/BLOCKER のグラフ解析を行い、長期競合の依存連鎖を可視化する。単純な保有者一覧では分からない待ちの連鎖を追うため、複数ジョブが絡むハング解析で使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0055"><h3>D GRS,C (Contention)</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,C (Contention)は、Sysplex / XCF / GRS / CFのD GRSで機能名、見出し、または確認対象として参照する項目です。現在競合中の ENQ をオーナ/ウェイタ別に列挙する。Hang 解析の起点。どのジョブが資源を保持し、どのジョブが待っているかを見て、停止候補や業務影響を判断する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0056"><h3>D GRS,DELAY</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>GRS リクエストの遅延を Top-N 表示。性能劣化時の起点。遅延量の大きい要求を先に見つけることで、全体遅延の原因になっている資源やジョブを絞り込む</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0057"><h3>D GRS,RES=(QNAME,RNAME)</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,RES=(QNAME,RNAME)は、Sysplex / XCF / GRS / CFのD GRSで機能名、見出し、または確認対象として参照する項目です。特定 ENQ リソースの保有者・待機者を表示する。マスク使用で部分一致検索が可能。QNAME/RNAME が分かっている場合に、広い競合一覧ではなく対象資源だけを直接確認できる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0058"><h3>D GRS,SYSTEM</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>Sysplex 内 GRS メンバの状態を一覧表示。Star 構成時は ISGLOCK 接続状況を含む。特定 LPAR だけが遅れているか、Sysplex 全体で同じ状態かを切り分けるときに使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


## ENQ/DEQ


<section class="kb-item" id="c29-i0059"><h3>Contention 監視</h3><p class="kb-meta">分類: ENQ/DEQ ・ 難易度: 中級</p><p>D GRS,C や ISGECA(Enqueue Contention Audit) で待機/保有関係を可視化する。長期 ENQ Hold は Sysplex 全体の性能阻害要因</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0060"><h3>DEQ マクロ</h3><p class="kb-meta">分類: ENQ/DEQ ・ 難易度: 中級</p><p>ENQ で取得したリソースを解放する。SYSTEMS スコープの場合は GRS への解放通知が Sysplex に伝搬される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0061"><h3>ENQ マクロの種類</h3><p class="kb-meta">分類: ENQ/DEQ ・ 難易度: 中級</p><p>ENQ は SCOPE=STEP/SYSTEM/SYSTEMS の 3 段階で取得スコープを指定する。SYSTEMS は GRS により Sysplex 全体で直列化される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0062"><h3>QNAME と RNAME</h3><p class="kb-meta">分類: ENQ/DEQ ・ 難易度: 中級</p><p>QNAME と RNAMEは、Sysplex / XCF / GRS / CFのENQ/DEQで機能名、見出し、または確認対象として参照する項目です。QNAME は最大 8 文字のリソースカテゴリ、RNAME は最大 255 文字のリソース個別名。両者で一意なロックを形成する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0063"><h3>RESERVE / HW Reserve</h3><p class="kb-meta">分類: ENQ/DEQ ・ 難易度: 中級</p><p>共有 DASD に対する物理 RESERVE で他システムからの I/O を排除する古典手法。RCRNL で ENQ 変換するのが現代の標準</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0064"><h3>排他 (EXCL) と共用 (SHR)</h3><p class="kb-meta">分類: ENQ/DEQ ・ 難易度: 中級</p><p>ENQ TYPE=EXCLUSIVE はライタロック、TYPE=SHARED はリーダロック。SHR 同士のみ並行取得が可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


## GRS


<section class="kb-item" id="c29-i0065"><h3>GRS Ring → Star 移行</h3><p class="kb-meta">分類: GRS ・ 難易度: 中級</p><p>全システム同期で SET GRS=STAR を投入する必要がある。Step 中はリソース直列化が不安定になるため計画停止枠で実施する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0066"><h3>GRS Ring 構成</h3><p class="kb-meta">分類: GRS ・ 難易度: 中級</p><p>システム間で RSA トークンを順送りし ENQ/DEQ を伝搬する旧方式。CTC ベースの XCF 経路で動作するが、システム数増加でレイテンシが線形に増大する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0067"><h3>GRS Star 構成</h3><p class="kb-meta">分類: GRS ・ 難易度: 中級</p><p>CF Lock 構造 ISGLOCK を使用する現行方式。Parallel Sysplex 必須。RSA 伝搬不要で応答が O(1) となるため大規模 Sysplex の標準</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0068"><h3>GRS の役割</h3><p class="kb-meta">分類: GRS ・ 難易度: 中級</p><p>GRS の役割は、Sysplex / XCF / GRS / CFのGRSで機能名、見出し、または確認対象として参照する項目です。Global Resource Serialization。ENQ/DEQ/RESERVE を Sysplex 全体で直列化するためのコンポーネント。Sysplex 全体のスループットに直接影響する基盤サービス</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0069"><h3>GRSCNF の MODE</h3><p class="kb-meta">分類: GRS ・ 難易度: 中級</p><p>GRSCNF=NONE/MIGRATE/RING/STAR を指定。STAR 推奨。MIGRATE は混在期に限定使用するレガシモード</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0070"><h3>ISGLOCK Structure</h3><p class="kb-meta">分類: GRS ・ 難易度: 上級</p><p>GRS Star 用 CF Lock 構造。CFRM ポリシーに DEFINE STRUCTURE NAME(ISGLOCK) で定義し、サイズは CFSizer で算出する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


## GRS PARMLIB


<section class="kb-item" id="c29-i0071"><h3>ENQMAXU / ENQMAXA</h3><p class="kb-meta">分類: GRS PARMLIB ・ 難易度: 上級</p><p>ENQMAXU / ENQMAXAは、Sysplex / XCF / GRS / CFのGRS PARMLIBで構成値やオプションの意味を確認する項目です。Address Space 当たり/Sysplex 全体の最大未処理 ENQ 数。デフォルトは 16384 程度で、Logger/RRS が多い環境では増量を検討する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0072"><h3>GRSCNFxx の役割</h3><p class="kb-meta">分類: GRS PARMLIB ・ 難易度: 上級</p><p>GRS 全体の構成 (MODE/CTC/RESMIL/GCMD/SYNCHRES/ENQMAXU/ENQMAXA) を定義する PARMLIB メンバ。IEASYSxx の GRSCNF= で指定</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0073"><h3>GRSRNL=EXCLUDE オプション</h3><p class="kb-meta">分類: GRS PARMLIB ・ 難易度: 上級</p><p>GRSRNL=EXCLUDE オプションは、Sysplex / XCF / GRS / CFのGRS PARMLIBで構成値やオプションの意味を確認する項目です。RNL の Inclusion/Exclusion を全て無視する緊急時オプション。本番では原則使用しない。RNL 設計を一時的に無効化する強い指定なので、問題切り分け後は通常の Inclusion/Exclusion 設計へ戻す</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0074"><h3>RESMIL / TOLINT</h3><p class="kb-meta">分類: GRS PARMLIB ・ 難易度: 上級</p><p>RESMIL / TOLINTは、Sysplex / XCF / GRS / CFのGRS PARMLIBで構成値やオプションの意味を確認する項目です。Ring 構成時のリング応答とトレラント間隔を制御するタイミングパラメータ。Star 構成では無視される。応答遅延を許容しすぎると障害検出が遅れ、短すぎると一時的な遅延を障害として扱う可能性がある</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0075"><h3>SYNCHRES</h3><p class="kb-meta">分類: GRS PARMLIB ・ 難易度: 上級</p><p>DASD Reserve を発行する前に GRS が同期的に解決を試みるかを指定する。性能影響に注意。競合解消を早めたい場面で検討するが、Reserve の発行順序や既存アプリケーションの待ち時間にも影響する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


## GRS RNL


<section class="kb-item" id="c29-i0076"><h3>GRSRNLxx PARMLIB</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 上級</p><p>RNL の本体を定義する PARMLIB メンバ。RNL=INCL/EXCL/CONV ステートメントで QNAME/RNAME を指定する。SET GRSRNL=xx で再ロード</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0077"><h3>RESERVE Conversion (RCRNL)</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>ハードウェア RESERVE を Sysplex-wide ENQ に変換するリスト。共有 DASD の RESERVE 競合を GRS で吸収するために使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0078"><h3>RNL の役割</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>Resource Name List。ENQ リソースを Sysplex 単位/システム単位/CONVERT の対象に振り分けるフィルター。GRSRNLxx で定義する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0079"><h3>RNL チューニング指針</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>Inclusion を過度に増やすと CF Lock 競合が増え、Exclusion を過度に増やすと整合性破壊リスクが増す。標準 IBM 推奨 RNL からの逸脱は最小に</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0080"><h3>RNL 編集時の注意</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>全システムで同一 RNL を持つことが必須。差分があると整合が崩れ、原則 Sysplex 単位の段階的展開が必要となる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0081"><h3>SYSTEM Inclusion (SIRNL)</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>SYSTEM Inclusion (SIRNL)は、Sysplex / XCF / GRS / CFのGRS RNLで機能名、見出し、または確認対象として参照する項目です。Sysplex-wide にすべきリソースのうち、デフォルトで SYSTEM スコープのものを Sysplex に格上げするリスト。例: SYSDSN.</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0082"><h3>SYSTEMS Exclusion (SERNL)</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>SYSTEMS Exclusion (SERNL)は、Sysplex / XCF / GRS / CFのGRS RNLで機能名、見出し、または確認対象として参照する項目です。Sysplex スコープから外して SYSTEM ローカルに留めたいリソースのリスト。性能向上目的で限定的に使用する。除外したリソースは他システムとの競合管理から外れるため、共有データセットや共通リソースには安易に使わない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0083"><h3>Synchronous RNL Change</h3><p class="kb-meta">分類: GRS RNL ・ 難易度: 中級</p><p>z/OS 1.8 以降、SET GRSRNL=xx,FORCE で全システム同時刷新が可能。混在期を許容する場合のみ単システム更新を選ぶ</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Planning: Global Resource Serialization、z / OS MVS Initialization and Tuning Reference</p></section>


## IXGCONN


<section class="kb-item" id="c29-i0084"><h3>IMPORTCONNECT / EXPORTCONNECT</h3><p class="kb-meta">分類: IXGCONN ・ 難易度: 中級</p><p>IMPORTCONNECT / EXPORTCONNECTは、Sysplex / XCF / GRS / CFのIXGCONNで機能名、見出し、または確認対象として参照する項目です。他システム接続済みのストリームに参照のみで接続する Import 種別。書込みアクセスは Export Connect で確立する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0085"><h3>IXGCONN マクロ</h3><p class="kb-meta">分類: IXGCONN ・ 難易度: 中級</p><p>IXGCONN マクロは、Sysplex / XCF / GRS / CFのIXGCONNで機能名、見出し、または確認対象として参照する項目です。アプリが Logger ログストリームに接続するためのマクロ。REQUEST=CONNECT で接続、DISCONNECT で切断。STREAMNAME を指定する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0086"><h3>IXGDELET / オフロード</h3><p class="kb-meta">分類: IXGCONN ・ 難易度: 中級</p><p>IXGDELET / オフロードは、Sysplex / XCF / GRS / CFのIXGCONNで機能名、見出し、または確認対象として参照する項目です。RETPD 経過ブロックの削除と DASD オフロード制御。OFFLOADRECALL/HIGHOFFLOAD/LOWOFFLOAD でしきい値を調整する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0087"><h3>IXGWRITE / IXGBRWSE</h3><p class="kb-meta">分類: IXGCONN ・ 難易度: 中級</p><p>ログストリームへの書込み(IXGWRITE)と参照(IXGBRWSE)。Sysplex 内 LPAR から同時書込が可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


## LogStream


<section class="kb-item" id="c29-i0088"><h3>CF 接続型</h3><p class="kb-meta">分類: LogStream ・ 難易度: 中級</p><p>CF List 構造をステージング領域として用い、Sysplex 全 LPAR から書込み可能。OPERLOG/RRS/CICS LSR が典型用途</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0089"><h3>DASDONLY 型</h3><p class="kb-meta">分類: LogStream ・ 難易度: 中級</p><p>CF を使わず単一 LPAR からのアクセスで完結する型。RACF SMF や監査用に使用する。CF 非依存で構成しやすい一方、複数システム共有や高可用性が必要なログには向かない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0090"><h3>HIGHOFFLOAD / LOWOFFLOAD</h3><p class="kb-meta">分類: LogStream ・ 難易度: 中級</p><p>CF / ステージング使用率がしきい値を越えた時に DASD オフロードを起動する制御。誤設定は CF Full から Logger Loss の原因</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0091"><h3>LOGR ポリシー</h3><p class="kb-meta">分類: LogStream ・ 難易度: 上級</p><p>DEFINE LOGSTREAM / DEFINE STRUCTURE で論理ログ単位を定義する。CF 接続型 (STRUCTNAME) と DASDONLY 型がある</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0092"><h3>RETPD / AUTODELETE</h3><p class="kb-meta">分類: LogStream ・ 難易度: 中級</p><p>RETPD / AUTODELETEは、Sysplex / XCF / GRS / CFのLogStreamで機能名、見出し、または確認対象として参照する項目です。ログ保持期間と削除自動化。コンプライアンス要件と DASD コストのトレードオフ。保存期間を長くすると監査証跡は残しやすいが、DASD 使用量とオフロード運用の負荷が増える</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0093"><h3>STG_DUPLEX</h3><p class="kb-meta">分類: LogStream ・ 難易度: 上級</p><p>ステージングデータセットでログを二重化する設定。CF 単一障害でログ喪失リスクを抑える。ログ可用性を高める指定だが、ステージング用 DASD の容量とオフロード設計も合わせて管理する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


## Logger


<section class="kb-item" id="c29-i0094"><h3>EMCS Console / 抑止フィルタ</h3><p class="kb-meta">分類: Logger ・ 難易度: 中級</p><p>EMCS Console / 抑止フィルタは、Sysplex / XCF / GRS / CFのLoggerで機能名、見出し、または確認対象として参照する項目です。OPERLOG は EMCS コンソール経由でも参照可能。MPF(Message Processing Facility) で抑止したメッセージは OPERLOG 出力前にフィルタされる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0095"><h3>OPERLOG (CONSOLxx)</h3><p class="kb-meta">分類: Logger ・ 難易度: 中級</p><p>System Logger 経由で Sysplex 全 LPAR のコンソールメッセージを 1 本のログストリームに集約する。CONSOLxx HARDCOPY DEVNUM(OPERLOG) で活性化</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0096"><h3>OPERLOG ログストリーム名</h3><p class="kb-meta">分類: Logger ・ 難易度: 中級</p><p>SYSPLEX.OPERLOG を CFRM 構造 (List) と LOGR ポリシーで定義し、IXGLOGR アドレス空間が管理する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0097"><h3>SDSF / IPCS による参照</h3><p class="kb-meta">分類: Logger ・ 難易度: 中級</p><p>SDSF / IPCS による参照は、Sysplex / XCF / GRS / CFのLoggerで機能名、見出し、または確認対象として参照する項目です。SDSF の OPERLOG パネル、または IPCS BLSCDDIR の OPERLOG コマンドで時系列参照する。SYSLOG と並列に運用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0098"><h3>SYSLOG</h3><p class="kb-meta">分類: Logger ・ 難易度: 中級</p><p>SYSLOGは、Sysplex / XCF / GRS / CFのLoggerで機能名、見出し、または確認対象として参照する項目です。JES SYSOUT に書き出される従来型コンソールログ。LPAR ローカルで完結。OPERLOG 移行後も併用可能。Sysplex 共通ログではないため、複数 LPAR の時系列を合わせる調査では OPERLOG との違いを意識する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


## RRS


<section class="kb-item" id="c29-i0099"><h3>RRS Indoubt 解決</h3><p class="kb-meta">分類: RRS ・ 難易度: 中級</p><p>ネットワーク障害等で In-Doubt 化したトランザクションを RRS パネル(ISPF: ATRRRS) または IXCMIAPU 相当ユーティリティから手動解決する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0100"><h3>RRS と XCF Group</h3><p class="kb-meta">分類: RRS ・ 難易度: 中級</p><p>ATRRRS という XCF グループでメンバシップを管理する。D XCF,GROUP,ATRRRS で参加 LPAR を確認できる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0101"><h3>RRS とは</h3><p class="kb-meta">分類: RRS ・ 難易度: 中級</p><p>RRS とはは、Sysplex / XCF / GRS / CFのRRSで機能名、見出し、または確認対象として参照する項目です。Resource Recovery Services。Sysplex 全体の分散トランザクションコーディネータ。CICS/DB2/IMS/MQ/WAS が参加し、Two-Phase Commit を統一管理する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0102"><h3>RRS ログストリーム</h3><p class="kb-meta">分類: RRS ・ 難易度: 中級</p><p>RRS は ATR.* 系の 5 つのログストリーム(MAIN/DELAYED/RESTART/ARCHIVE/RM.DATA)を System Logger に要求する。LOGR/CFRM の事前準備が必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


<section class="kb-item" id="c29-i0103"><h3>RRS 初期化と START</h3><p class="kb-meta">分類: RRS ・ 難易度: 中級</p><p>S RRS で起動。IXCMIAPU で LOGR ポリシー登録済みでないと初期化失敗。RRS はリカバリ単位を管理するため、ログストリーム定義と起動順序が整っていないと関連サービスも影響を受ける</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Programming: Assembler Services Guide</p></section>


## SETXCF


<section class="kb-item" id="c29-i0104"><h3>SETXCF COUPLE,ACOUPLE=</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>SETXCF COUPLE,ACOUPLE=は、Sysplex / XCF / GRS / CFのSETXCFで機能名、見出し、または確認対象として参照する項目です。オルタネート CDS を組込む。プライマリ喪失後の再オルタ補充や Spare 切替時に使用する。CDS の冗長性を戻す作業なので、追加するデータセット名と現在のプライマリ状態を取り違えないようにする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0105"><h3>SETXCF COUPLE,PSWITCH</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>SETXCF COUPLE,PSWITCHは、Sysplex / XCF / GRS / CFのSETXCFで機能名、見出し、または確認対象として参照する項目です。オルタネートをプライマリに昇格し、現プライマリを切り離す。CDS 拡張時の無停止切替で使用する。切替後は新しいプライマリとオルタネートの組み合わせを表示コマンドで確認し、片系だけのまま放置しない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0106"><h3>SETXCF FORCE</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>SETXCF FORCEは、Sysplex / XCF / GRS / CFのSETXCFで機能名、見出し、または確認対象として参照する項目です。失効した Policy/Structure/Connection を強制的に削除する。FORCE,STRUCTURE,STRNAME=... など。誤操作で Connector を破壊する危険があり慎重に使用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0107"><h3>SETXCF MODIFY,CLASSDEF</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>SETXCF MODIFY,CLASSDEFは、Sysplex / XCF / GRS / CFのSETXCFで機能名、見出し、または確認対象として参照する項目です。Transport Class の MAXMSG/CLASSLEN/GROUP をオンラインで変更する。COUPLExx と差分を整合させる運用が必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0108"><h3>SETXCF MODIFY,LOCALMSG</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>LOCALMSG MAXMSG をオンラインで変更する。XCF Stall 兆候時の応急処置として使用。一時対処として有効だが、恒久対応ではメッセージ量、Transport Class、経路設計も合わせて見直す</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0109"><h3>SETXCF START / STOP</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>PATHIN/PATHOUT/POLICY/REBUILD などのリソースを起動・停止する基本コマンド。例: SETXCF START,POLICY,TYPE=CFRM,POLNAME=PROD</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0110"><h3>SETXCF START,ALTER</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 中級</p><p>SETXCF START,ALTERは、Sysplex / XCF / GRS / CFのSETXCFで機能名、見出し、または確認対象として参照する項目です。ALLOWAUTOALT 設定下の構造をオペレータが手動でリサイズする。SIZE/ENTRYCOUNT/ELEMENTCOUNT を指定可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0111"><h3>SETXCF START,REBUILD</h3><p class="kb-meta">分類: SETXCF ・ 難易度: 上級</p><p>SETXCF START,REBUILDは、Sysplex / XCF / GRS / CFのSETXCFで機能名、見出し、または確認対象として参照する項目です。CF Structure を別 CF に再配置/再構築する。LOCATION=NORMAL/OTHER を選び、計画停止時の CF 移動に用いる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


## SFM


<section class="kb-item" id="c29-i0112"><h3>CFSTRHANGTIME(n)</h3><p class="kb-meta">分類: SFM ・ 難易度: 上級</p><p>CFSTRHANGTIME(n)は、Sysplex / XCF / GRS / CFのSFMで機能名、見出し、または確認対象として参照する項目です。CF Structure のコネクタ応答待ち上限。長時間 Hang する Structure Connector を強制的にイベント完了させる(z/OS 2.1+)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0113"><h3>ISOLATETIME(n)</h3><p class="kb-meta">分類: SFM ・ 難易度: 上級</p><p>ステータス更新が n 秒途絶えたシステムを自動的に Isolation(Partition Out) する設定。System Isolation には CF List 構造または FENCE 機構を用いる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0114"><h3>MEMSTALLTIME(n)</h3><p class="kb-meta">分類: SFM ・ 難易度: 上級</p><p>XCF メンバが n 秒応答しない場合に当該メンバを切り離す上限。Sysplex 全体の Wait/Hang を抑止する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0115"><h3>PROMPT vs ISOLATETIME</h3><p class="kb-meta">分類: SFM ・ 難易度: 上級</p><p>PROMPT vs ISOLATETIMEは、Sysplex / XCF / GRS / CFのSFMで機能名、見出し、または確認対象として参照する項目です。PROMPT は IXC402D 応答待ち(従来動作)、ISOLATETIME は自動隔離。CONNFAIL(YES) と組み合わせ、シグナリング欠損時の対処を選ぶ</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0116"><h3>RECONFIG / WEIGHT</h3><p class="kb-meta">分類: SFM ・ 難易度: 上級</p><p>PR/SM CPU・ストレージ・CHPID の再構成を SFM に委ねる場合の重み付け。WEIGHT(n) を全システムに付与し、生存側の容量を増やす</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0117"><h3>SFM の目的</h3><p class="kb-meta">分類: SFM ・ 難易度: 上級</p><p>Sysplex 障害時のオペレータ判断を自動化し、IXC402D 応答待ちで Sysplex が機能停止することを防ぐ。SFM CDS に格納したポリシーを活性化して使用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## Sysplex Distributor


<section class="kb-item" id="c29-i0118"><h3>DVIPA とは</h3><p class="kb-meta">分類: Sysplex Distributor ・ 難易度: 中級</p><p>Dynamic Virtual IP Address。Sysplex 内で移動可能な仮想 IP。アプリケーション可用性向上の TCP/IP 基盤</p><p class="kb-src"><strong>出典:</strong> z / OS Communications Server IP Configuration Reference、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0119"><h3>DVIPA タイプ</h3><p class="kb-meta">分類: Sysplex Distributor ・ 難易度: 中級</p><p>DVIPA タイプは、Sysplex / XCF / GRS / CFのSysplex Distributorで機能名、見出し、または確認対象として参照する項目です。VIPADEFINE(静的所有)、VIPABACKUP(代替所有)、VIPADYNAMIC(動的) を組み合わせ、所有移動とフェイルオーバを構成する</p><p class="kb-src"><strong>出典:</strong> z / OS Communications Server IP Configuration Reference、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0120"><h3>SD と XCF</h3><p class="kb-meta">分類: Sysplex Distributor ・ 難易度: 中級</p><p>Distributor と Target 間の制御情報は XCF メッセージで授受される。Sysplex 健全性が SD 動作の前提となる</p><p class="kb-src"><strong>出典:</strong> z / OS Communications Server IP Configuration Reference、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0121"><h3>SHAREPORT / SHAREPORTWLM</h3><p class="kb-meta">分類: Sysplex Distributor ・ 難易度: 中級</p><p>SHAREPORT / SHAREPORTWLMは、Sysplex / XCF / GRS / CFのSysplex Distributorで機能名、見出し、または確認対象として参照する項目です。同一ポートを複数アプリケーションが共有する設定。SHAREPORTWLM は WLM 推奨値で負荷分散を行う。WLM と組み合わせると、単なる接続数ではなくサーバの処理能力や応答状況を反映した配分にできる</p><p class="kb-src"><strong>出典:</strong> z / OS Communications Server IP Configuration Reference、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0122"><h3>Sysplex Autonomics</h3><p class="kb-meta">分類: Sysplex Distributor ・ 難易度: 中級</p><p>Sysplex 内 TCP/IP スタックを WLM とサーバ応答に基づき動的に切り替える機能群。EZBTCPIP の自動監視を含む</p><p class="kb-src"><strong>出典:</strong> z / OS Communications Server IP Configuration Reference、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0123"><h3>VIPADISTRIBUTE</h3><p class="kb-meta">分類: Sysplex Distributor ・ 難易度: 中級</p><p>Distributing Stack(分散ホスト)で受信した接続を Sysplex 内の Target Stack にルーティング/負荷分散する設定</p><p class="kb-src"><strong>出典:</strong> z / OS Communications Server IP Configuration Reference、z / OS MVS Setting Up a Sysplex</p></section>


## Sysplex Ops


<section class="kb-item" id="c29-i0124"><h3>ROUTE *ALL</h3><p class="kb-meta">分類: Sysplex Ops ・ 難易度: 中級</p><p>Sysplex 内全 LPAR で同一コマンドを実行する。例: ROUTE *ALL,D A,L で全 LPAR のアクティブジョブ一覧を一括取得</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0125"><h3>ROUTE sysgrp</h3><p class="kb-meta">分類: Sysplex Ops ・ 難易度: 中級</p><p>Sysplex Group 名指定で部分集合に発行する。CONSOLxx の SYSGROUP 定義と組み合わせる。同じコマンドを複数 LPAR へまとめて出したい場合に使い、全台発行と部分発行を切り分ける</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0126"><h3>ROUTE sysname</h3><p class="kb-meta">分類: Sysplex Ops ・ 難易度: 中級</p><p>ROUTE sysnameは、Sysplex / XCF / GRS / CFのSysplex Opsで機能名、見出し、または確認対象として参照する項目です。特定 LPAR にコマンドをルーティングする。サブシステム停止時の遠隔操作で多用される。対象システムを間違えると別 LPAR に操作が入るため、発行前に sysname と操作対象を確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0127"><h3>Sysplex IPL 順序</h3><p class="kb-meta">分類: Sysplex Ops ・ 難易度: 中級</p><p>GRS Star は先頭 IPL システムが ISGLOCK を初期化するため、CFRM/SFM/ARM CDS が両系利用可能であることを IPL 前に確認する運用ルール</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0128"><h3>V XCF,sysname,OFFLINE</h3><p class="kb-meta">分類: Sysplex Ops ・ 難易度: 中級</p><p>正常な計画停止用に LPAR を Sysplex から離脱させる。SFM 制御下では自動隔離経路と区別が必要。計画停止では通常の離脱手順として使い、障害隔離や強制排除とは運用上の意味を分ける</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


## Sysplex Time


<section class="kb-item" id="c29-i0129"><h3>CTN ID と Timing Network</h3><p class="kb-meta">分類: Sysplex Time ・ 難易度: 中級</p><p>STP 構成内で共通の CTN ID(英数 8 文字)を持つ CPC が CTN を形成する。複数 CTN を混在させると同期しないため、Sysplex メンバ全 CPC で同一 CTN ID が必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0130"><h3>Leap Second / Time Offset</h3><p class="kb-meta">分類: Sysplex Time ・ 難易度: 中級</p><p>STP は閏秒の事前/事後挿入や UTC オフセット指定を HMC からスケジュール可能。Sysplex 全体で同一時刻を保つため、システム別の TOD 調整は禁止</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0131"><h3>STP (Server Time Protocol) の概要</h3><p class="kb-meta">分類: Sysplex Time ・ 難易度: 中級</p><p>STP (Server Time Protocol) の概要は、Sysplex / XCF / GRS / CFのSysplex Timeで機能名、見出し、または確認対象として参照する項目です。9037 を不要とするメッセージベースのサーバ間時刻同期。CPC 間 ICA SR/Coupling リンクで Timing-Only/Timing-and-Coupling として構成し、Coordinated Timing Network (CTN) を形成する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0132"><h3>Stratum レベル (S0/S1/S2)</h3><p class="kb-meta">分類: Sysplex Time ・ 難易度: 中級</p><p>S0=タイムソース PTS/BTS、S1=直接同期、S2=多段同期。Preferred Time Server(PTS), Backup Time Server(BTS), Arbiter を割り当て、PTS 障害時に BTS が引き継ぐ</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0133"><h3>Sysplex Timer (9037) の位置づけ</h3><p class="kb-meta">分類: Sysplex Time ・ 難易度: 中級</p><p>外部時刻源として複数 LPAR の TOD クロックを同期させる旧世代ハードウェア。Parallel Sysplex 必須要件として ETR ネットワークを構成する。Z14 以降では STP に置き換えが進む</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0134"><h3>TOD クロック同期失敗の影響</h3><p class="kb-meta">分類: Sysplex Time ・ 難易度: 中級</p><p>Sysplex メンバ間で TOD 差が許容を越えると、XCF ステータス更新の時系列整合が崩れ、Wait State X&#x27;0A2&#x27; または Sysplex Partition が発生する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## Sysplex種別


<section class="kb-item" id="c29-i0135"><h3>Base Sysplex</h3><p class="kb-meta">分類: Sysplex種別 ・ 難易度: 中級</p><p>複数 z/OS イメージを XCF シグナリングで結合するが Coupling Facility を持たない構成。シグナリングは CTC または CDS を経由する。GRS Ring は使えるが GRS Star は不可</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0136"><h3>MONOPLEX</h3><p class="kb-meta">分類: Sysplex種別 ・ 難易度: 中級</p><p>単一 z/OS イメージを 1 つのスプレックスとして扱う最小構成。XCF はシグナリング相手を持たず、CDS は Sysplex CDS のみ使用される。CFRM/SFM 等の付加 CDS は不要で、PLEXCFG=MONOPLEX を COUPLExx に指定する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0137"><h3>PLEXCFG オプション一覧</h3><p class="kb-meta">分類: Sysplex種別 ・ 難易度: 中級</p><p>COUPLExx PARMLIB の PLEXCFG パラメータは MONOPLEX / XCFLOCAL / MULTISYSTEM / ANY を指定可能。MULTISYSTEM は Base/Parallel 双方を含み、ANY は IPL 時の他システムの存在で動的決定する非推奨指定</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0138"><h3>Parallel Sysplex</h3><p class="kb-meta">分類: Sysplex種別 ・ 難易度: 中級</p><p>Coupling Facility と Sysplex Timer/STP を用いて複数 z/OS イメージをデータシェアリング可能な形で結合した構成。CF Structure を介して GRS Star, RACF, DB2 Data Sharing, IMS Shared Queue 等を実現する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0139"><h3>Sysplex 名 (SYSPLEX キーワード)</h3><p class="kb-meta">分類: Sysplex種別 ・ 難易度: 中級</p><p>COUPLExx の SYSPLEX(name) で最大 8 文字の Sysplex 名を定義する。Sysplex CDS に格納され、複数 LPAR が同じ Sysplex 名を持つことで結合される。一度活性化した Sysplex 名は CDS 再作成までは変更不可</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0140"><h3>XCF-Local Mode</h3><p class="kb-meta">分類: Sysplex種別 ・ 難易度: 中級</p><p>XCF 機能を起動するが他システムとシグナリングしない単一イメージ構成。MONOPLEX に近いがアプリケーション(例 RRS, GRS Star は不可) 視点で XCF サービスを利用できる点が異なる。PLEXCFG=XCFLOCAL</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## XCF Command


<section class="kb-item" id="c29-i0141"><h3>D XCF</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>Sysplex 概要表示。Sysplex 名、メンバシステム一覧、状態、IPL 時刻、Sysplex タイミング情報を返す</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0142"><h3>D XCF,CF</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>CF の物理状態と接続済みシステム一覧を表示。CF 名・CFLEVEL・モデル・ダンプ可否を含む。CF 障害やリンク切断を疑うときは、接続済みシステムと CFLEVEL を見て、構成上の前提が満たされているか確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0143"><h3>D XCF,CLASSDEF</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>D XCF,CLASSDEFは、Sysplex / XCF / GRS / CFのXCF Commandで状態表示や操作を行うためのコマンド関連項目です。Transport Class 一覧と各クラスの CLASSLEN, MAXMSG, GROUP 割当、使用量を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0144"><h3>D XCF,COUPLE</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>全 CDS のプライマリ/オルタネートと I/O 状態を表示。TYPE=(SYSPLEX,CFRM,...) で絞り込み可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0145"><h3>D XCF,GROUP</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>XCF グループ一覧。GROUP 名指定で参加メンバとその状態 (ACTIVE/QUIESCED 等) を取得する。特定サービスの停止や片系だけの異常を調べるときは、グループ名を絞ってメンバ状態を確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0146"><h3>D XCF,PI / D XCF,PO</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>D XCF,PI / D XCF,POは、Sysplex / XCF / GRS / CFのXCF Commandで状態表示や操作を行うためのコマンド関連項目です。シグナリング経路 (PATHIN/PATHOUT) の状態表示。各経路の Transfer Time, Buffer Use, STATUS を含む</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0147"><h3>D XCF,STR</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>CFRM 構造一覧。STRNAME 指定で個別構造の Connector, Size, Disposition を確認できる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0148"><h3>D XCF,SYSPLEX</h3><p class="kb-meta">分類: XCF Command ・ 難易度: 中級</p><p>D XCF,SYSPLEXは、Sysplex / XCF / GRS / CFのXCF Commandで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands、z/OS MVS Setting Up a Sysplex を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands、z / OS MVS Setting Up a Sysplex</p></section>


## XCF Group


<section class="kb-item" id="c29-i0149"><h3>Group / Member とは</h3><p class="kb-meta">分類: XCF Group ・ 難易度: 中級</p><p>XCF ユーザは Group に Join し、Group 内 Member 間でメッセージ送受や状態同期を行う。1 グループあたり最大 1023 メンバ。IXCJOIN/IXCMSGO/IXCLEAVE で操作する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0150"><h3>Status Update Missing</h3><p class="kb-meta">分類: XCF Group ・ 難易度: 中級</p><p>Status Update Missingは、Sysplex / XCF / GRS / CFのXCF Groupで自動化処理や復旧動作を確認する項目です。メンバが INTERVAL 内に Status Update を出さない状態。SFM が活性ならポリシーに従い隔離、未活性なら IXC402D が発行される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0151"><h3>User State 領域</h3><p class="kb-meta">分類: XCF Group ・ 難易度: 中級</p><p>User State 領域は、Sysplex / XCF / GRS / CFのXCF Groupで機能名、見出し、または確認対象として参照する項目です。メンバが任意の制御情報をブロードキャスト共有できる固定長領域。State 変更通知が他メンバに自動配信される。メンバ間で状態を軽く共有したいサービスでは、個別メッセージ送信よりも状態領域の更新を使う方が設計しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0152"><h3>システムグループ (SYSXCF)</h3><p class="kb-meta">分類: XCF Group ・ 難易度: 中級</p><p>z/OS 内部用の予約グループ群。SYSXCF, SYSGRS, SYSRRS, SYSCNZMG, SYSWLM などが該当し、IBM 製品はそれぞれ独自のグループ名を持つ</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0153"><h3>メンバステータス</h3><p class="kb-meta">分類: XCF Group ・ 難易度: 中級</p><p>ACTIVE/QUIESCED/FAILED/CREATED/UNDEFINED を取り、D XCF,GROUP,...,member で確認可能。FAILED は IXCDELET 等の後処理が必要</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


## XCF Path


<section class="kb-item" id="c29-i0154"><h3>CF 構造経路 (PATHSTRUCTURE)</h3><p class="kb-meta">分類: XCF Path ・ 難易度: 上級</p><p>CF Signaling 構造を利用する経路。CFRM ポリシーに IXC_DEFAULT_1 等の List 構造を定義し、PATHIN/PATHOUT STRNAME(...) で参照する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0155"><h3>CTC 経路</h3><p class="kb-meta">分類: XCF Path ・ 難易度: 中級</p><p>CTC 経路は、Sysplex / XCF / GRS / CFのXCF Pathで機能名、見出し、または確認対象として参照する項目です。DEVICE 番号で物理 CTC を使用する。双方向で対になる側に PATHIN と PATHOUT を交差して定義する必要がある</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0156"><h3>PATHIN/PATHOUT 構文</h3><p class="kb-meta">分類: XCF Path ・ 難易度: 中級</p><p>PATHIN/PATHOUT 構文は、Sysplex / XCF / GRS / CFのXCF Pathで機能名、見出し、または確認対象として参照する項目です。PATHIN/PATHOUT を CTC DEVICE 指定または STRNAME 指定で記述する。例: PATHOUT DEVICE(0E20) または PATHOUT STRNAME(IXC_DEFAULT_1)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0157"><h3>シグナリング構造の名前ルール</h3><p class="kb-meta">分類: XCF Path ・ 難易度: 中級</p><p>IXC_ で始まる List 構造を CFRM に登録するのが推奨。経路ごとに 2 つ以上の構造を別 CF に分散して可用性を確保する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0158"><h3>経路追加/削除</h3><p class="kb-meta">分類: XCF Path ・ 難易度: 中級</p><p>SETXCF START,PATHIN/PATHOUT,DEVICE=/STRNAME= で動的追加、SETXCF STOP,PATHIN/PATHOUT,... で削除する。IPL は不要</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0159"><h3>経路選択アルゴリズム</h3><p class="kb-meta">分類: XCF Path ・ 難易度: 中級</p><p>Transport Class とメッセージサイズに基づき、利用可能で空きのある最良経路が選ばれる。経路間負荷分散は XCF が自動制御する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


## XCF Signaling


<section class="kb-item" id="c29-i0160"><h3>Buffer / MAXMSG の効果</h3><p class="kb-meta">分類: XCF Signaling ・ 難易度: 中級</p><p>MAXMSG はバッファプール上限(KB)。小さすぎるとシグナリング詰まりが発生し XCF Stall を招く。RMF Mon III の XCF レポートで使用率を監視する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0161"><h3>Signaling Connection 状態</h3><p class="kb-meta">分類: XCF Signaling ・ 難易度: 中級</p><p>WORKING/INOPERATIVE/RESTARTING/STOPPING を取り、SETXCF START/STOP で遷移する。D XCF,PI / PO で表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0162"><h3>XCF の概要</h3><p class="kb-meta">分類: XCF Signaling ・ 難易度: 中級</p><p>Cross-System Coupling Facility。Sysplex 内システム間のメンバシップ管理、グループ通信、ステータス監視を提供する z/OS コンポーネント。GRS/RRS/LOGR/Console 等の上位サービスが利用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0163"><h3>シグナリングの帯域監視</h3><p class="kb-meta">分類: XCF Signaling ・ 難易度: 中級</p><p>RMF Monitor III の XCF レポートで Transfer Time, Send/Receive Buffer Use, REQ REJECT を確認する。継続的に REQ REJECT が出る場合は MAXMSG/経路追加で対処</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0164"><h3>シグナリング多重化</h3><p class="kb-meta">分類: XCF Signaling ・ 難易度: 中級</p><p>シグナリング多重化は、Sysplex / XCF / GRS / CFのXCF Signalingで自動化処理や復旧動作を確認する項目です。PATHIN/PATHOUT を複数定義し、Transport Class 単位に経路選択される。1 経路故障時も継続するため最低 2 経路の冗長化が必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


<section class="kb-item" id="c29-i0165"><h3>シグナリング経路の種類</h3><p class="kb-meta">分類: XCF Signaling ・ 難易度: 中級</p><p>CTC (Channel-to-Channel) ベースと CF List 構造ベースの 2 種が併用可能。CF ベースは構造内 Notification List で送受する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Programming: Sysplex Services Guide、z / OS MVS Setting Up a Sysplex</p></section>


## XCF Transport


<section class="kb-item" id="c29-i0166"><h3>DEFAULT クラス</h3><p class="kb-meta">分類: XCF Transport ・ 難易度: 中級</p><p>DEFAULT クラスは、Sysplex / XCF / GRS / CFのXCF Transportで機能名、見出し、または確認対象として参照する項目です。標準クラス。CLASSLEN(956) など 1KB 程度のシグナリングメッセージを処理する。すべての XCF グループが利用可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0167"><h3>GROUP 指定</h3><p class="kb-meta">分類: XCF Transport ・ 難易度: 中級</p><p>クラスに紐づける XCF グループ。GROUP(UNDESIG) は未指定グループ全般を意味する。特定グループ専用クラスを作って干渉回避することも可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0168"><h3>LARGE クラス</h3><p class="kb-meta">分類: XCF Transport ・ 難易度: 中級</p><p>LARGE クラスは、Sysplex / XCF / GRS / CFのXCF Transportで機能名、見出し、または確認対象として参照する項目です。大型ペイロード用クラス。CLASSLEN(62464) や 65535 等の大バッファを確保し、Logger オフロードや RRS バッファ転送を分離する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0169"><h3>SMALL クラス</h3><p class="kb-meta">分類: XCF Transport ・ 難易度: 中級</p><p>SMALL クラスは、Sysplex / XCF / GRS / CFのXCF Transportで機能名、見出し、または確認対象として参照する項目です。短メッセージ専用クラス。小さな CLASSLEN により小バッファを大量に確保し、頻度の高い短メッセージを高速化する。大きなメッセージと同じクラスに混ぜないことで、バッファ浪費や短メッセージの待ちを減らせる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0170"><h3>Transport Class とは</h3><p class="kb-meta">分類: XCF Transport ・ 難易度: 中級</p><p>Transport Class とはは、Sysplex / XCF / GRS / CFのXCF Transportで機能名、見出し、または確認対象として参照する項目です。メッセージ長と利用グループを基準に経路をクラス分けする仕組み。CLASSDEF で CLASSLEN/MAXMSG/GROUP を指定する。経路は CLASSDEF と PATHOUT で結びつく</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>


<section class="kb-item" id="c29-i0171"><h3>クラスチューニング指針</h3><p class="kb-meta">分類: XCF Transport ・ 難易度: 中級</p><p>クラスチューニング指針は、Sysplex / XCF / GRS / CFのXCF Transportで機能名、見出し、または確認対象として参照する項目です。ペイロード分布に合わせ 3〜5 クラス程度に階層化し、MAXMSG をクラスごとに増やすのが性能最適化の定石。RMF で REQ REJECT を見ながら調整する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS Setting Up a Sysplex、z / OS MVS Initialization and Tuning Reference</p></section>
