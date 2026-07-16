---
search:
  exclude: true
---

# IMS 15.5 — 詳細 (1/2)

[← IMS 15.5 の概要へ戻る](index.md)


## DB/DC運用


<section class="kb-item" id="c16-i0001"><h3>/DISPLAY TRANSACTION 状態確認 状態確認</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>IMS 15.5 の DB/DC運用 で扱う「/DISPLAY TRANSACTION 状態確認 状態確認」は、トランザクションの状態、キュー、処理可否を確認するIMSコマンドを状態確認の観点で確認する技術項目です。DFS994I 行とDBD001を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY TRANSACTION 状態確認 状態確認</strong></p><p>検証目的: DB/DC運用における/DISPLAY TRANSACTIONの状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD001</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY001
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY001 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD001
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD001 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA1
→ Enter を押す
［画面・出力］
DFS000I AREA AREA1 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0002"><h3>/DISPLAY TRANSACTION 登録確認 制御領域</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 中級</p><p>IMS 15.5 の DB/DC運用 で扱う「/DISPLAY TRANSACTION 登録確認 制御領域」は、トランザクションの状態、キュー、処理可否を確認するIMSコマンドを登録確認の観点で確認する技術項目です。DFS994I 行とDBD061を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY TRANSACTION 登録確認 制御領域</strong></p><p>検証目的: DB/DC運用における/DISPLAY TRANSACTIONの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD061</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY061
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY061 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD061
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD061 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA5
→ Enter を押す
［画面・出力］
DFS000I AREA AREA5 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0003"><h3>/NRESTART BUILDQ 出力項目確認 ボリューム状態</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 上級</p><p>IMS 15.5 の DB/DC運用 で扱う「/NRESTART BUILDQ 出力項目確認 ボリューム状態」は、直近の停止チェックポイントから通常再始動し、キュー構築を行うIMSコマンドを出力項目確認の観点で確認する技術項目です。DFS994I 行とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/NRESTART BUILDQ 出力項目確認 ボリューム状態</strong></p><p>検証目的: DB/DC運用における/NRESTART BUILDQの出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD097)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD097  DD=DBDS01  RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力には OLDS1 が含まれ、OLDS1を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0004"><h3>/NRESTART BUILDQ 戻りコード確認 区画表示</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 中級</p><p>IMS 15.5 の DB/DC運用 で扱う「/NRESTART BUILDQ 戻りコード確認 区画表示」は、直近の停止チェックポイントから通常再始動し、キュー構築を行うIMSコマンドを戻りコード確認の観点で確認する技術項目です。DFS994I 行とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/NRESTART BUILDQ 戻りコード確認 区画表示</strong></p><p>検証目的: DB/DC運用における/NRESTART BUILDQの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD037)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD037  DD=DBDS01  RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力には OLDS1 が含まれ、OLDS1を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0005"><h3>DB/DC運用 トランザクション表示 ログとの照合 PAY07</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>ログとの照合では DB/DC運用 の トランザクション状態 を主操作として PAY07 を判定します。時刻と対象識別子への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY07 に残します。ログとの照合を補助する 稼働メンバー確認 では ACTIVE を補助値として PAY07 へ保存します。主判定のログとの照合では運用・トランザクション表示の トランザクション状態 から DFS000I を読み PAY07 へ残します。証跡照合のログとの照合では運用・トランザクション表示の DFS000I と ACTIVE を PAY07 に保存します。記録対応のログとの照合では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で DB/DC運用 の トランザクション状態 と 稼働メンバー確認 を組み合わせる際は トランザクション表示 が入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能という仕組みを前提にします。停止中トランザクションや滞留キューを見落とす危険があります。DFS000I と STATUSとQUEUE を対象 PAY07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRAN PAY07が応答を返した時点で正常とする。応答中のDFS000Iの値は記録しない。DFS1929IをDFS000Iと同じ判定値とみなし対象PAY07の主証跡にする。</li><li>B. /DISPLAY TRAN PAY07のコマンド文字列だけを記録する。DFS000Iを含む応答行は保存しない。</li><li>C. DFS000Iを含むトランザクション状態の応答行を保存する。その応答を得るため/DISPLAY TRAN PAY07を使用する。対象PAY07のSTATUSとQUEUEとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. トランザクション表示の停止または再定義を実施する。その後に/DISPLAY TRAN PAY07でDFS000Iを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 適切な判定: Cはトランザクション状態で DFS000I を読みSTATUSとQUEUEの主値として操作とログを対応しPAY07に残します。
機能の仕組み: ログとの照合では稼働メンバー確認を補助操作としトランザクション表示の時刻と対象識別子をACTIVEと対象PAY07で照合します。
各候補の評価: トランザクション状態と稼働メンバー確認の役割を分けるとA: 応答の有無だけではSTATUSとQUEUEを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではSTATUSとQUEUEを証明できない点で一次資料と一致しません、C: DFS000Iの実値を対象別に残す点でPAY07を判定できます、D: 変更前のSTATUSとQUEUEを失う点で稼働メンバー確認の範囲を越えます。結論としてログとの照合の運用・トランザクション表示で判定する対象は PAY07 です。
用語の定義: ログとの照合で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 ログとの照合 PAY07</strong></p><p>検証目的: DB/DC運用のトランザクション表示について操作とログを対応し、PAY07のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY07を指定し、PAY07のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY07
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY07 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY07の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY07 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY07のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の ACTIVE が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0006"><h3>DB/DC運用 トランザクション表示 代替経路の確認 PAY10</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>代替経路の確認では DB/DC運用 の トランザクション状態 を主操作として PAY10 を判定します。主経路との役割差への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY10 に残します。代替経路の確認を補助する 稼働メンバー確認 では ACTIVE を補助値として PAY10 へ保存します。主判定の代替経路の確認では運用・トランザクション表示の トランザクション状態 から DFS000I を読み PAY10 へ残します。証跡照合の代替経路の確認では運用・トランザクション表示の DFS000I と ACTIVE を PAY10 に保存します。記録対応の代替経路の確認では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で DB/DC運用 の トランザクション状態 と 稼働メンバー確認 を実施し トランザクション表示 の役割を確認します。停止中トランザクションや滞留キューを見落とす危険があります。対象 PAY10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRAN PAY10のコマンド文字列だけを記録する。DFS000Iを含む応答行は保存しない。</li><li>B. /DISPLAY TRAN PAY10と/DISPLAY ACTIVEの対象名をそろえる。前者のDFS000IをSTATUSとQUEUEの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. トランザクション表示の停止または再定義を実施する。その後に/DISPLAY TRAN PAY10でDFS000Iを採取する。</li><li>D. ログ管理のアクティブログとアーカイブ先を確認する。その値をDB/DC運用のPAY10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい判定結果: Bはトランザクション状態で DFS000I を読みSTATUSとQUEUEの主値として代替手段の成立を確認しPAY10に残します。
運用上の背景: 代替経路の確認では稼働メンバー確認を補助操作としトランザクション表示の主経路との役割差をACTIVEと対象PAY10で照合します。
候補別の検討: トランザクション状態と稼働メンバー確認の役割を分けるとA: 入力記録だけではSTATUSとQUEUEを証明できない点で一次資料と一致しません、B: 同じ対象名のDFS000Iを採用する点でPAY10を判定できます、C: 変更前のSTATUSとQUEUEを失う点で稼働メンバー確認の範囲を越えます、D: ログ管理の値ではDFS000Iを確認できない点でPAY10の値を示しません。結論として代替経路の確認の運用・トランザクション表示で判定する対象は PAY10 です。
重要用語の定義: 代替経路の確認で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 代替経路の確認 PAY10</strong></p><p>検証目的: DB/DC運用のトランザクション表示について代替手段の成立を確認し、PAY10のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY10を指定し、PAY10のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY10
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY10 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY10の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY10 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY10のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の ACTIVE が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0007"><h3>DB/DC運用 トランザクション表示 変更前の確認 PAY02</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>変更前の確認では DB/DC運用 の 稼働メンバー確認 を主操作として PAY02 を判定します。変更対象と非対象の境界への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY02 に残します。変更前の確認を補助する システム状態 では DFS1929I を補助値として PAY02 へ保存します。主判定の変更前の確認では運用・トランザクション表示の 稼働メンバー確認 から ACTIVE を読み PAY02 へ残します。証跡照合の変更前の確認では運用・トランザクション表示の ACTIVE と DFS1929I を PAY02 に保存します。記録対応の変更前の確認では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で DB/DC運用 の 稼働メンバー確認 と システム状態 の役割を分け 変更対象と非対象の境界 を調べます。トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能です。停止中トランザクションや滞留キューを見落とす危険があります。対象 PAY02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY ACTIVEを対象名なしで実行する。一覧の先頭行をPAY02の結果として記録する。</li><li>B. 対象PAY02について/DISPLAY ACTIVEの応答からACTIVEを確認する。/DISPLAY SYSTEMは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存した/DISPLAY ACTIVEの結果を使う。今回の/DISPLAY SYSTEMの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのPAY02の出力を再利用する。今回の/DISPLAY ACTIVEと/DISPLAY SYSTEMは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: Bは稼働メンバー確認で ACTIVE を読みSTATUSとQUEUEの主値として変更前の証跡を保存しPAY02に残します。
動作の背景: 変更前の確認ではシステム状態を補助操作としトランザクション表示の変更対象と非対象の境界をDFS1929Iと対象PAY02で照合します。
各選択肢の検討: 稼働メンバー確認とシステム状態の役割を分けるとA: 先頭行はPAY02と確定できない点で変更前の確認に合いません、B: ACTIVEと補助証跡の時刻を合わせる点で稼働メンバー確認に合います、C: 採取時刻が異なる点でDB/DC運用に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でトランザクション表示に使えません。結論として変更前の確認の運用・トランザクション表示で判定する対象は PAY02 です。
初出用語の定義: 変更前の確認で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 変更前の確認 PAY02</strong></p><p>検証目的: DB/DC運用のトランザクション表示について変更前の証跡を保存し、PAY02のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY02の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY02 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY02のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY02を指定し、PAY02のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY02
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY02 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ACTIVE が画面・出力に表示されること
② ステップ2 の DFS1929I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0008"><h3>DB/DC運用 トランザクション表示 変更後の確認 PAY03</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>変更後の確認では DB/DC運用 の システム状態 を主操作として PAY03 を判定します。反映値と残存値への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY03 に残します。変更後の確認を補助する トランザクション状態 では DFS000I を補助値として PAY03 へ保存します。主判定の変更後の確認では運用・トランザクション表示の システム状態 から DFS1929I を読み PAY03 へ残します。証跡照合の変更後の確認では運用・トランザクション表示の DFS1929I と DFS000I を PAY03 に保存します。記録対応の変更後の確認では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で DB/DC運用 の システム状態 と トランザクション状態 を使い 変更結果を検証 します。トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能です。停止中トランザクションや滞留キューを見落とす危険があります。DFS1929I を読み対象 PAY03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. トランザクション表示の停止または再定義を実施する。その後に/DISPLAY SYSTEMでDFS1929Iを採取する。</li><li>B. DBRC/RECONのDBDS登録とRECON可用性を確認する。その値をDB/DC運用のPAY03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. /DISPLAY TRAN PAY03で周辺状態を押さえる。その後に/DISPLAY SYSTEMでDFS1929Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. /DISPLAY TRAN PAY03が成功したため/DISPLAY SYSTEMのDFS1929Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Cはシステム状態で DFS1929I を読みSTATUSとQUEUEの主値として変更結果を検証しPAY03に残します。
内部の仕組み: 変更後の確認ではトランザクション状態を補助操作としトランザクション表示の反映値と残存値をDFS000Iと対象PAY03で照合します。
誤答を含む比較: システム状態とトランザクション状態の役割を分けるとA: 変更前のSTATUSとQUEUEを失う点でSTATUSとQUEUEを確認できません、B: DBRC/RECONの値ではDFS1929Iを確認できないうえに追加前提も不正な点でトランザクション状態の範囲を越えます、C: 周辺状態の後にDFS1929Iを確認する点で現在値を示します、D: 補助操作の成功ではDFS1929Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の運用・トランザクション表示で判定する対象は PAY03 です。
用語定義: 変更後の確認で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 変更後の確認 PAY03</strong></p><p>検証目的: DB/DC運用のトランザクション表示について変更結果を検証し、PAY03のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY03のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY03を指定し、PAY03のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY03
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY03 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY03の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY03 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS1929I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の ACTIVE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0009"><h3>DB/DC運用 トランザクション表示 引継ぎ記録 PAY09</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>引継ぎ記録では DB/DC運用 の システム状態 を主操作として PAY09 を判定します。次担当者が追跡できる証跡への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY09 に残します。引継ぎ記録を補助する トランザクション状態 では DFS000I を補助値として PAY09 へ保存します。主判定の引継ぎ記録では運用・トランザクション表示の システム状態 から DFS1929I を読み PAY09 へ残します。証跡照合の引継ぎ記録では運用・トランザクション表示の DFS1929I と DFS000I を PAY09 に保存します。記録対応の引継ぎ記録では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で DB/DC運用 の システム状態 と トランザクション状態 を使い 再現可能な記録を作成 します。トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能です。停止中トランザクションや滞留キューを見落とす危険があります。DFS1929I を読み対象 PAY09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 対象名PAY09を指定して/DISPLAY SYSTEMを実行する。応答中のDFS1929Iと時刻を保存する。/DISPLAY TRAN PAY09で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. /DISPLAY TRAN PAY09が成功したため/DISPLAY SYSTEMのDFS1929Iも正常だと推定する。主出力は保存しない。</li><li>C. /DISPLAY SYSTEMを対象名なしで実行する。一覧の先頭行をPAY09の結果として記録する。</li><li>D. 前回保存した/DISPLAY SYSTEMの結果を使う。今回の/DISPLAY TRAN PAY09の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用操作の理由: Aはシステム状態で DFS1929I を読みSTATUSとQUEUEの主値として再現可能な記録を作成しPAY09に残します。
製品内の仕組み: 引継ぎ記録ではトランザクション状態を補助操作としトランザクション表示の次担当者が追跡できる証跡をDFS000Iと対象PAY09で照合します。
選択肢別の説明: システム状態とトランザクション状態の役割を分けるとA: DFS1929Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではDFS1929Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はPAY09と確定できない点でシステム状態を代替しません、D: 採取時刻が異なる点でDB/DC運用に使いません。結論として引継ぎ記録の運用・トランザクション表示で判定する対象は PAY09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 引継ぎ記録 PAY09</strong></p><p>検証目的: DB/DC運用のトランザクション表示について再現可能な記録を作成し、PAY09のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY09のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY09を指定し、PAY09のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY09
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY09 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY09の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY09 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS1929I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の ACTIVE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0010"><h3>DB/DC運用 トランザクション表示 復旧後の確認 PAY06</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>復旧後の確認では DB/DC運用 の システム状態 を主操作として PAY06 を判定します。再発していないことを示す値への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY06 に残します。復旧後の確認を補助する トランザクション状態 では DFS000I を補助値として PAY06 へ保存します。主判定の復旧後の確認では運用・トランザクション表示の システム状態 から DFS1929I を読み PAY06 へ残します。証跡照合の復旧後の確認では運用・トランザクション表示の DFS1929I と DFS000I を PAY06 に保存します。記録対応の復旧後の確認では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で DB/DC運用 の システム状態 と トランザクション状態 を照合し 再発していないことを示す値 を確かめます。トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能です。停止中トランザクションや滞留キューを見落とす危険があります。DFS1929I を読む前に対象 PAY06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. オンライン変更のIMPORT完了コードとメンバー反映を確認する。その値をDB/DC運用のPAY06にも適用する。</li><li>B. /DISPLAY SYSTEMでDFS1929Iを取得してから/DISPLAY ACTIVEでACTIVEを照合する。PAY06のSTATUSとQUEUEを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY TRAN PAY06が成功したため/DISPLAY SYSTEMのDFS1929Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象PAY06へ引き継げるものとする。</li><li>D. /DISPLAY SYSTEMを対象名なしで実行する。一覧の先頭行をPAY06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答内容: Bはシステム状態で DFS1929I を読みSTATUSとQUEUEの主値として復旧後の安定性を確認しPAY06に残します。
構成上の背景: 復旧後の確認ではトランザクション状態を補助操作としトランザクション表示の再発していないことを示す値をDFS000Iと対象PAY06で照合します。
候補ごとの理由: システム状態とトランザクション状態の役割を分けるとA: オンライン変更の値ではDFS1929Iを確認できない点でトランザクション状態の範囲を越えます、B: DFS1929IとACTIVEを順に照合する点で現在値を示します、C: 補助操作の成功ではDFS1929Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はPAY06と確定できない点でシステム状態を代替しません。結論として復旧後の確認の運用・トランザクション表示で判定する対象は PAY06 です。
初出用語: 復旧後の確認で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 復旧後の確認 PAY06</strong></p><p>検証目的: DB/DC運用のトランザクション表示について復旧後の安定性を確認し、PAY06のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY06のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY06を指定し、PAY06のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY06
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY06 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY06の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY06 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS1929I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の ACTIVE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0011"><h3>DB/DC運用 トランザクション表示 復旧準備 PAY05</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>復旧準備では DB/DC運用 の 稼働メンバー確認 を主操作として PAY05 を判定します。再開前に必要な整合性への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY05 に残します。復旧準備を補助する システム状態 では DFS1929I を補助値として PAY05 へ保存します。主判定の復旧準備では運用・トランザクション表示の 稼働メンバー確認 から ACTIVE を読み PAY05 へ残します。証跡照合の復旧準備では運用・トランザクション表示の ACTIVE と DFS1929I を PAY05 に保存します。記録対応の復旧準備では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で DB/DC運用 の 稼働メンバー確認 と システム状態 を用い 復旧条件を確認 します。トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能です。停止中トランザクションや滞留キューを見落とす危険があります。ACTIVE で対象 PAY05 の STATUSとQUEUE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えず/DISPLAY ACTIVEを実行する。ACTIVEを保存する。差分は/DISPLAY SYSTEMの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存した/DISPLAY ACTIVEの結果を使う。今回の/DISPLAY SYSTEMの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのPAY05の出力を再利用する。今回の/DISPLAY ACTIVEと/DISPLAY SYSTEMは実行済みとして扱う。</li><li>D. /DISPLAY SYSTEMのDFS1929IをSTATUSとQUEUEの主判定に採用する。/DISPLAY ACTIVEの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 選定理由: Aは稼働メンバー確認で ACTIVE を読みSTATUSとQUEUEの主値として復旧条件を確認しPAY05に残します。
処理の仕組み: 復旧準備ではシステム状態を補助操作としトランザクション表示の再開前に必要な整合性をDFS1929Iと対象PAY05で照合します。
選択結果の内訳: 稼働メンバー確認とシステム状態の役割を分けるとA: 変更前のACTIVEを保存する点で稼働メンバー確認に合います、B: 採取時刻が異なる点でDB/DC運用に使いません、C: 過去出力では今回の復旧準備を示せない点でトランザクション表示に使えません、D: DFS1929IはACTIVEを代替しないうえに追加前提も不正な点でPAY05を採用できません。結論として復旧準備の運用・トランザクション表示で判定する対象は PAY05 です。
用語の説明: 復旧準備で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 復旧準備 PAY05</strong></p><p>検証目的: DB/DC運用のトランザクション表示について復旧条件を確認し、PAY05のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY05の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY05 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY05のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY05を指定し、PAY05のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY05
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY05 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ACTIVE が画面・出力に表示されること
② ステップ2 の DFS1929I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0012"><h3>DB/DC運用 トランザクション表示 構成監査 PAY08</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>構成監査では DB/DC運用 の 稼働メンバー確認 を主操作として PAY08 を判定します。定義値と稼働値の一致への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY08 に残します。構成監査を補助する システム状態 では DFS1929I を補助値として PAY08 へ保存します。主判定の構成監査では運用・トランザクション表示の 稼働メンバー確認 から ACTIVE を読み PAY08 へ残します。証跡照合の構成監査では運用・トランザクション表示の ACTIVE と DFS1929I を PAY08 に保存します。記録対応の構成監査では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で DB/DC運用 の 稼働メンバー確認 と システム状態 の役割を分け 定義値と稼働値の一致 を調べます。トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能です。停止中トランザクションや滞留キューを見落とす危険があります。対象 PAY08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのPAY08の出力を再利用する。今回の/DISPLAY ACTIVEと/DISPLAY SYSTEMは実行済みとして扱う。</li><li>B. /DISPLAY SYSTEMのDFS1929IをSTATUSとQUEUEの主判定に採用する。/DISPLAY ACTIVEの応答は採取対象から外す。</li><li>C. /DISPLAY TRAN PAY08のDFS000IをACTIVEと同義の成功表示として扱う。/DISPLAY ACTIVEは実行しない。</li><li>D. /DISPLAY SYSTEMの結果だけでは確定しない。/DISPLAY ACTIVEのACTIVEを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 技術上の正答: Dは稼働メンバー確認で ACTIVE を読みSTATUSとQUEUEの主値として構成差分を監査しPAY08に残します。
実行時の背景: 構成監査ではシステム状態を補助操作としトランザクション表示の定義値と稼働値の一致をDFS1929Iと対象PAY08で照合します。
四つの候補の理由: 稼働メンバー確認とシステム状態の役割を分けるとA: 過去出力では今回の構成監査を示せない点でDB/DC運用に使いません、B: DFS1929IはACTIVEを代替しない点でトランザクション表示に使えません、C: DFS000IとACTIVEは確認項目が異なる点でPAY08を採用できません、D: ACTIVEを主証跡として区別する点で主証跡になります。結論として構成監査の運用・トランザクション表示で判定する対象は PAY08 です。
初出語定義: 構成監査で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 構成監査 PAY08</strong></p><p>検証目的: DB/DC運用のトランザクション表示について構成差分を監査し、PAY08のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY08の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY08 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY08のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY08を指定し、PAY08のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY08
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY08 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ACTIVE が画面・出力に表示されること
② ステップ2 の DFS1929I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0013"><h3>DB/DC運用 トランザクション表示 通常状態の確認 PAY01</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>通常状態の確認では DB/DC運用 の トランザクション状態 を主操作として PAY01 を判定します。基準値と現在値の差への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY01 に残します。通常状態の確認を補助する 稼働メンバー確認 では ACTIVE を補助値として PAY01 へ保存します。主判定の通常状態の確認では運用・トランザクション表示の トランザクション状態 から DFS000I を読み PAY01 へ残します。証跡照合の通常状態の確認では運用・トランザクション表示の DFS000I と ACTIVE を PAY01 に保存します。記録対応の通常状態の確認では運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で DB/DC運用 の トランザクション状態 と 稼働メンバー確認 を組み合わせる際は トランザクション表示 が入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能という仕組みを前提にします。停止中トランザクションや滞留キューを見落とす危険があります。DFS000I と STATUSとQUEUE を対象 PAY01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRAN PAY01を先に実行する。対象PAY01のDFS000IをSTATUSとQUEUEとして記録する。続いて/DISPLAY ACTIVEで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. /DISPLAY ACTIVEのACTIVEをSTATUSとQUEUEの主判定に採用する。/DISPLAY TRAN PAY01の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. /DISPLAY SYSTEMのDFS1929IをDFS000Iと同義の成功表示として扱う。/DISPLAY TRAN PAY01は実行しない。</li><li>D. /DISPLAY TRAN PAY01が応答を返した時点で正常とする。応答中のDFS000Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: Aはトランザクション状態で DFS000I を読みSTATUSとQUEUEの主値として通常状態を確定しPAY01に残します。
背景・仕組み: 通常状態の確認では稼働メンバー確認を補助操作としトランザクション表示の基準値と現在値の差をACTIVEと対象PAY01で照合します。
選択肢の理由: トランザクション状態と稼働メンバー確認の役割を分けるとA: DFS000Iを主値として補助結果と照合する点で正答です、B: ACTIVEはDFS000Iを代替しないうえに追加前提も不正な点でPAY01を採用できません、C: DFS1929IとDFS000Iは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではSTATUSとQUEUEを判定できない点で一次資料と一致しません。結論として通常状態の確認の運用・トランザクション表示で判定する対象は PAY01 です。
用語の初出定義: 通常状態の確認で使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 通常状態の確認 PAY01</strong></p><p>検証目的: DB/DC運用のトランザクション表示について通常状態を確定し、PAY01のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY01を指定し、PAY01のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY01
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY01 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY01の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY01 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY01のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の ACTIVE が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0014"><h3>DB/DC運用 トランザクション表示 障害切り分け PAY04</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>障害切り分けでは DB/DC運用 の トランザクション状態 を主操作として PAY04 を判定します。最初に失敗した処理への注意として「停止中トランザクションや滞留キューを見落とす危険があります」を PAY04 に残します。障害切り分けを補助する 稼働メンバー確認 では ACTIVE を補助値として PAY04 へ保存します。主判定の障害切り分けでは運用・トランザクション表示の トランザクション状態 から DFS000I を読み PAY04 へ残します。証跡照合の障害切り分けでは運用・トランザクション表示の DFS000I と ACTIVE を PAY04 に保存します。記録対応の障害切り分けでは運用・トランザクション表示の STATUSとQUEUE の証跡へ PAY04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで DB/DC運用 の トランザクション状態 と 稼働メンバー確認 を実施し トランザクション表示 の役割を確認します。停止中トランザクションや滞留キューを見落とす危険があります。対象 PAY04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY SYSTEMのDFS1929IをDFS000Iと同義の成功表示として扱う。/DISPLAY TRAN PAY04は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. /DISPLAY TRAN PAY04が応答を返した時点で正常とする。応答中のDFS000Iの値は記録しない。</li><li>C. /DISPLAY TRAN PAY04のコマンド文字列だけを記録する。DFS000Iを含む応答行は保存しない。</li><li>D. /DISPLAY TRAN PAY04の出力でPAY04とDFS000Iが同じ応答にあることを確認する。STATUSとQUEUEをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: Dはトランザクション状態で DFS000I を読みSTATUSとQUEUEの主値として障害範囲を限定しPAY04に残します。
技術的背景: 障害切り分けでは稼働メンバー確認を補助操作としトランザクション表示の最初に失敗した処理をACTIVEと対象PAY04で照合します。
四択の評価: トランザクション状態と稼働メンバー確認の役割を分けるとA: DFS1929IとDFS000Iは確認項目が異なるうえに追加前提も不正な点でPAY04を採用できません、B: 応答の有無だけではSTATUSとQUEUEを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではSTATUSとQUEUEを証明できない点で一次資料と一致しません、D: PAY04とDFS000Iを同じ応答で結ぶ点でPAY04を判定できます。結論として障害切り分けの運用・トランザクション表示で判定する対象は PAY04 です。
初出語の意味: 障害切り分けで使う トランザクション表示 は入力トランザクションの開始可否とキュー滞留をトランザクション名単位で示すIMSオンライン運用機能を表しSTATUSとQUEUEを判定する際にPAY04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB/DC運用 トランザクション表示 障害切り分け PAY04</strong></p><p>検証目的: DB/DC運用のトランザクション表示について障害範囲を限定し、PAY04のSTATUSとQUEUEを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PAY04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY TRAN PAY04を指定し、PAY04のトランザクション状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY04
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY04 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力にあるDFS000Iを読み、STATUSとQUEUEと対象PAY04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY ACTIVEを指定し、PAY04の稼働メンバー確認を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS1 ACTIVE TRANSACTION PAY04 PROGRAM PGMPAY
画面・出力にあるACTIVEを読み、STATUSとQUEUEと対象PAY04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDB/DC運用を確認する入力画面です。COMMAND入力口へ/DISPLAY SYSTEMを指定し、PAY04のシステム状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED FOR IMS1
画面・出力にあるDFS1929Iを読み、STATUSとQUEUEと対象PAY04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の ACTIVE が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0015"><h3>DFS994I リカバリ確認 表形式</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 中級</p><p>IMS 15.5 の DB/DC運用 で扱う「DFS994I リカバリ確認 表形式」は、チェックポイント番号と種別を表示するIMSメッセージをリカバリ確認の観点で確認する技術項目です。DFS994I 行とOLDS1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS994I リカバリ確認 表形式</strong></p><p>検証目的: DB/DC運用におけるDFS994Iのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD025
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD025.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0016"><h3>DFS994I 接続確認 再読込</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 上級</p><p>IMS 15.5 の DB/DC運用 で扱う「DFS994I 接続確認 再読込」は、チェックポイント番号と種別を表示するIMSメッセージを接続確認の観点で確認する技術項目です。DFS994I 行とOLDS1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS994I 接続確認 再読込</strong></p><p>検証目的: DB/DC運用におけるDFS994Iの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD085
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD085.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0017"><h3>DFSURGU0 出力項目確認 警告行</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 中級</p><p>IMS 15.5 の DB/DC運用 で扱う「DFSURGU0 出力項目確認 警告行」は、HD Reorganization UnloadでフルファンクションDBをアンロードするIMSユーティリティを出力項目確認の観点で確認する技術項目です。DFS994I 行とPSB049を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURGU0 出力項目確認 警告行</strong></p><p>検証目的: DB/DC運用におけるDFSURGU0の出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB049</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD049) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD049 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0018"><h3>PSB checkpoint restart リカバリ確認 構成照合</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 中級</p><p>IMS 15.5 の DB/DC運用 で扱う「PSB checkpoint restart リカバリ確認 構成照合」は、BMPやバッチプログラムの再始動点をPSBとチェックポイントIDで管理する仕組みをリカバリ確認の観点で確認する技術項目です。DFS994I 行と82112/081220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PSB checkpoint restart リカバリ確認 構成照合</strong></p><p>検証目的: DB/DC運用におけるPSB checkpoint restartのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82112/081220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0019"><h3>PSB checkpoint restart 登録確認 起動確認</h3><p class="kb-meta">分類: DB/DC運用 ・ 難易度: 初級</p><p>IMS 15.5 の DB/DC運用 で扱う「PSB checkpoint restart 登録確認 起動確認」は、BMPやバッチプログラムの再始動点をPSBとチェックポイントIDで管理する仕組みを登録確認の観点で確認する技術項目です。DFS994I 行と82122/081220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PSB checkpoint restart 登録確認 起動確認</strong></p><p>検証目的: DB/DC運用におけるPSB checkpoint restartの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82122/081220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


## DBD/PSB/ACB


<section class="kb-item" id="c16-i0020"><h3>/CHECKPOINT DUMPQ リカバリ確認 ログ採取</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 初級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「/CHECKPOINT DUMPQ リカバリ確認 ログ採取」は、メッセージキューを保持して停止するためのチェックポイント操作をリカバリ確認の観点で確認する技術項目です。DBD 名とOLDS5を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT DUMPQ リカバリ確認 ログ採取</strong></p><p>検証目的: DBD/PSB/ACBにおける/CHECKPOINT DUMPQのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS5</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD005
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD005.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0021"><h3>/CHECKPOINT DUMPQ 接続確認 保護値</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「/CHECKPOINT DUMPQ 接続確認 保護値」は、メッセージキューを保持して停止するためのチェックポイント操作を接続確認の観点で確認する技術項目です。DBD 名とOLDS5を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT DUMPQ 接続確認 保護値</strong></p><p>検証目的: DBD/PSB/ACBにおける/CHECKPOINT DUMPQの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS5</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD065
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD065.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0022"><h3>DBD/PSB/ACB IMS管理ACB ログとの照合 ACB07</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>ログとの照合では DBD/PSB/ACB（管理・定義名と有効版） の DB定義照会 を主操作として ACB07 を判定します。時刻と対象識別子への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB07 に残します。ログとの照合を補助する プログラム定義照会 では NOTINIT を補助値として ACB07 へ保存します。主判定のログとの照合では管理・定義名と有効版の DB定義照会 から AVAILABLE を読み ACB07 へ残します。証跡照合のログとの照合では管理・定義名と有効版の AVAILABLE と NOTINIT を ACB07 に保存します。記録対応のログとの照合では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で DBD/PSB/ACB の DB定義照会 と プログラム定義照会 を用い 操作とログを対応 します。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。AVAILABLE で対象 ACB07 の 定義名と有効版 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. QUERY DB NAME(ACB07) SHOW(ALL)が応答を返した時点で正常とする。応答中のAVAILABLEの値は記録しない。COMPLETEをAVAILABLEと同じ判定値とみなし対象ACB07の主証跡にする。</li><li>B. QUERY DB NAME(ACB07) SHOW(ALL)のコマンド文字列だけを記録する。AVAILABLEを含む応答行は保存しない。</li><li>C. AVAILABLEを含むDB定義照会の応答行を保存する。その応答を得るためQUERY DB NAME(ACB07) SHOW(ALL)を使用する。対象ACB07の定義名と有効版として記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. IMS管理ACBの停止または再定義を実施する。その後にQUERY DB NAME(ACB07) SHOW(ALL)でAVAILABLEを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: CはDB定義照会で AVAILABLE を読み定義名と有効版の主値として操作とログを対応しACB07に残します。
機能の仕組み: ログとの照合ではプログラム定義照会を補助操作としIMS管理ACBの時刻と対象識別子をNOTINITと対象ACB07で照合します。
各候補の評価: DB定義照会とプログラム定義照会の役割を分けるとA: 応答の有無だけでは定義名と有効版を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけでは定義名と有効版を証明できない点で一次資料と一致しません、C: AVAILABLEの実値を対象別に残す点でACB07を判定できます、D: 変更前の定義名と有効版を失う点でプログラム定義照会の範囲を越えます。結論としてログとの照合の管理・定義名と有効版で判定する対象は ACB07 です。
用語の定義: ログとの照合で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB ログとの照合 ACB07</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて操作とログを対応し、ACB07の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB07) SHOW(ALL)を指定し、ACB07のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB07) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB07&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM07) SHOW(ALL)を指定し、ACB07のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM07) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM07&lt;/pgm&gt;&lt;psb&gt;PSB07&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB07のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AVAILABLE が画面・出力に表示されること
② ステップ2 の NOTINIT が画面・出力に表示されること
③ ステップ3 の COMPLETE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0023"><h3>DBD/PSB/ACB IMS管理ACB 代替経路の確認 ACB10</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>代替経路の確認では DBD/PSB/ACB（管理・定義名と有効版） の DB定義照会 を主操作として ACB10 を判定します。主経路との役割差への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB10 に残します。代替経路の確認を補助する プログラム定義照会 では NOTINIT を補助値として ACB10 へ保存します。主判定の代替経路の確認では管理・定義名と有効版の DB定義照会 から AVAILABLE を読み ACB10 へ残します。証跡照合の代替経路の確認では管理・定義名と有効版の AVAILABLE と NOTINIT を ACB10 に保存します。記録対応の代替経路の確認では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で DBD/PSB/ACB の DB定義照会 と プログラム定義照会 の役割を分け 主経路との役割差 を調べます。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。対象 ACB10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. QUERY DB NAME(ACB10) SHOW(ALL)のコマンド文字列だけを記録する。AVAILABLEを含む応答行は保存しない。</li><li>B. QUERY DB NAME(ACB10) SHOW(ALL)とQUERY PGM NAME(PGM10) SHOW(ALL)の対象名をそろえる。前者のAVAILABLEを定義名と有効版の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. IMS管理ACBの停止または再定義を実施する。その後にQUERY DB NAME(ACB10) SHOW(ALL)でAVAILABLEを採取する。</li><li>D. リスタートの使用チェックポイントとBUILDQ結果を確認する。その値をDBD/PSB/ACBのACB10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: BはDB定義照会で AVAILABLE を読み定義名と有効版の主値として代替手段の成立を確認しACB10に残します。
運用上の背景: 代替経路の確認ではプログラム定義照会を補助操作としIMS管理ACBの主経路との役割差をNOTINITと対象ACB10で照合します。
候補別の検討: DB定義照会とプログラム定義照会の役割を分けるとA: 入力記録だけでは定義名と有効版を証明できない点で一次資料と一致しません、B: 同じ対象名のAVAILABLEを採用する点でACB10を判定できます、C: 変更前の定義名と有効版を失う点でプログラム定義照会の範囲を越えます、D: リスタートの値ではAVAILABLEを確認できない点でACB10の値を示しません。結論として代替経路の確認の管理・定義名と有効版で判定する対象は ACB10 です。
重要用語の定義: 代替経路の確認で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 代替経路の確認 ACB10</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて代替手段の成立を確認し、ACB10の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB10) SHOW(ALL)を指定し、ACB10のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB10) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB10&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM10) SHOW(ALL)を指定し、ACB10のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM10) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM10&lt;/pgm&gt;&lt;psb&gt;PSB10&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB10のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AVAILABLE が画面・出力に表示されること
② ステップ2 の NOTINIT が画面・出力に表示されること
③ ステップ3 の COMPLETE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0024"><h3>DBD/PSB/ACB IMS管理ACB 変更前の確認 ACB02</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>変更前の確認では DBD/PSB/ACB（管理・定義名と有効版） の プログラム定義照会 を主操作として ACB02 を判定します。変更対象と非対象の境界への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB02 に残します。変更前の確認を補助する カタログ取込結果 では COMPLETE を補助値として ACB02 へ保存します。主判定の変更前の確認では管理・定義名と有効版の プログラム定義照会 から NOTINIT を読み ACB02 へ残します。証跡照合の変更前の確認では管理・定義名と有効版の NOTINIT と COMPLETE を ACB02 に保存します。記録対応の変更前の確認では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で DBD/PSB/ACB の プログラム定義照会 と カタログ取込結果 を照合し 変更対象と非対象の境界 を確かめます。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。NOTINIT を読む前に対象 ACB02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. QUERY PGM NAME(PGM02) SHOW(ALL)を対象名なしで実行する。一覧の先頭行をACB02の結果として記録する。</li><li>B. 対象ACB02についてQUERY PGM NAME(PGM02) SHOW(ALL)の応答からNOTINITを確認する。IMPORT DEFN SOURCE(CATALOG)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したQUERY PGM NAME(PGM02) SHOW(ALL)の結果を使う。今回のIMPORT DEFN SOURCE(CATALOG)の結果と同一時点の証跡として比較する。</li><li>D. 保存済みのACB02の出力を再利用する。今回のQUERY PGM NAME(PGM02) SHOW(ALL)とIMPORT DEFN SOURCE(CATALOG)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bはプログラム定義照会で NOTINIT を読み定義名と有効版の主値として変更前の証跡を保存しACB02に残します。
動作の背景: 変更前の確認ではカタログ取込結果を補助操作としIMS管理ACBの変更対象と非対象の境界をCOMPLETEと対象ACB02で照合します。
各選択肢の検討: プログラム定義照会とカタログ取込結果の役割を分けるとA: 先頭行はACB02と確定できない点で変更前の確認に合いません、B: NOTINITと補助証跡の時刻を合わせる点でプログラム定義照会に合います、C: 採取時刻が異なる点でDBD/PSB/ACBに使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でIMS管理ACBに使えません。結論として変更前の確認の管理・定義名と有効版で判定する対象は ACB02 です。
初出用語の定義: 変更前の確認で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 変更前の確認 ACB02</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて変更前の証跡を保存し、ACB02の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM02) SHOW(ALL)を指定し、ACB02のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM02) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM02&lt;/pgm&gt;&lt;psb&gt;PSB02&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB02のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB02) SHOW(ALL)を指定し、ACB02のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB02) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB02&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の NOTINIT が画面・出力に表示されること
② ステップ2 の COMPLETE が画面・出力に表示されること
③ ステップ3 の AVAILABLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0025"><h3>DBD/PSB/ACB IMS管理ACB 変更後の確認 ACB03</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>変更後の確認では DBD/PSB/ACB（管理・定義名と有効版） の カタログ取込結果 を主操作として ACB03 を判定します。反映値と残存値への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB03 に残します。変更後の確認を補助する DB定義照会 では AVAILABLE を補助値として ACB03 へ保存します。主判定の変更後の確認では管理・定義名と有効版の カタログ取込結果 から COMPLETE を読み ACB03 へ残します。証跡照合の変更後の確認では管理・定義名と有効版の COMPLETE と AVAILABLE を ACB03 に保存します。記録対応の変更後の確認では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で DBD/PSB/ACB の カタログ取込結果 と DB定義照会 を組み合わせる際は IMS管理ACB がDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みという仕組みを前提にします。カタログ定義と稼働定義の世代差を見落とす危険があります。COMPLETE と 定義名と有効版 を対象 ACB03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. IMS管理ACBの停止または再定義を実施する。その後にIMPORT DEFN SOURCE(CATALOG)でCOMPLETEを採取する。</li><li>B. IMS Connectのポートと接続先メンバーを確認する。その値をDBD/PSB/ACBのACB03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IMS管理ACBの反映値と残存値は確認済みとして扱う。さらにQUERY PGM NAME(PGM03) SHOW(ALL)のNOTINITをCOMPLETEと同種の値として併記する。</li><li>C. QUERY DB NAME(ACB03) SHOW(ALL)で周辺状態を押さえる。その後にIMPORT DEFN SOURCE(CATALOG)でCOMPLETEを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. QUERY DB NAME(ACB03) SHOW(ALL)が成功したためIMPORT DEFN SOURCE(CATALOG)のCOMPLETEも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Cはカタログ取込結果で COMPLETE を読み定義名と有効版の主値として変更結果を検証しACB03に残します。
内部の仕組み: 変更後の確認ではDB定義照会を補助操作としIMS管理ACBの反映値と残存値をAVAILABLEと対象ACB03で照合します。
誤答を含む比較: カタログ取込結果とDB定義照会の役割を分けるとA: 変更前の定義名と有効版を失う点で定義名と有効版を確認できません、B: IMS Connectの値ではCOMPLETEを確認できないうえに追加前提も不正な点でDB定義照会の範囲を越えます、C: 周辺状態の後にCOMPLETEを確認する点で現在値を示します、D: 補助操作の成功ではCOMPLETEを確定できない点で変更後の確認に合いません。結論として変更後の確認の管理・定義名と有効版で判定する対象は ACB03 です。
用語定義: 変更後の確認で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 変更後の確認 ACB03</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて変更結果を検証し、ACB03の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB03のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB03) SHOW(ALL)を指定し、ACB03のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB03) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB03&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM03) SHOW(ALL)を指定し、ACB03のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM03) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM03&lt;/pgm&gt;&lt;psb&gt;PSB03&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の COMPLETE が画面・出力に表示されること
② ステップ2 の AVAILABLE が画面・出力に表示されること
③ ステップ3 の NOTINIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0026"><h3>DBD/PSB/ACB IMS管理ACB 引継ぎ記録 ACB09</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>引継ぎ記録では DBD/PSB/ACB（管理・定義名と有効版） の カタログ取込結果 を主操作として ACB09 を判定します。次担当者が追跡できる証跡への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB09 に残します。引継ぎ記録を補助する DB定義照会 では AVAILABLE を補助値として ACB09 へ保存します。主判定の引継ぎ記録では管理・定義名と有効版の カタログ取込結果 から COMPLETE を読み ACB09 へ残します。証跡照合の引継ぎ記録では管理・定義名と有効版の COMPLETE と AVAILABLE を ACB09 に保存します。記録対応の引継ぎ記録では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で DBD/PSB/ACB の カタログ取込結果 と DB定義照会 を組み合わせる際は IMS管理ACB がDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みという仕組みを前提にします。カタログ定義と稼働定義の世代差を見落とす危険があります。COMPLETE と 定義名と有効版 を対象 ACB09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 対象名ACB09を指定してIMPORT DEFN SOURCE(CATALOG)を実行する。応答中のCOMPLETEと時刻を保存する。QUERY DB NAME(ACB09) SHOW(ALL)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. QUERY DB NAME(ACB09) SHOW(ALL)が成功したためIMPORT DEFN SOURCE(CATALOG)のCOMPLETEも正常だと推定する。主出力は保存しない。</li><li>C. IMPORT DEFN SOURCE(CATALOG)を対象名なしで実行する。一覧の先頭行をACB09の結果として記録する。</li><li>D. 前回保存したIMPORT DEFN SOURCE(CATALOG)の結果を使う。今回のQUERY DB NAME(ACB09) SHOW(ALL)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Aはカタログ取込結果で COMPLETE を読み定義名と有効版の主値として再現可能な記録を作成しACB09に残します。
製品内の仕組み: 引継ぎ記録ではDB定義照会を補助操作としIMS管理ACBの次担当者が追跡できる証跡をAVAILABLEと対象ACB09で照合します。
選択肢別の説明: カタログ取込結果とDB定義照会の役割を分けるとA: COMPLETEと時刻を保存する点で現在値を示します、B: 補助操作の成功ではCOMPLETEを確定できない点で引継ぎ記録に合いません、C: 先頭行はACB09と確定できない点でカタログ取込結果を代替しません、D: 採取時刻が異なる点でDBD/PSB/ACBに使いません。結論として引継ぎ記録の管理・定義名と有効版で判定する対象は ACB09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 引継ぎ記録 ACB09</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて再現可能な記録を作成し、ACB09の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB09のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB09) SHOW(ALL)を指定し、ACB09のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB09) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB09&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM09) SHOW(ALL)を指定し、ACB09のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM09) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM09&lt;/pgm&gt;&lt;psb&gt;PSB09&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の COMPLETE が画面・出力に表示されること
② ステップ2 の AVAILABLE が画面・出力に表示されること
③ ステップ3 の NOTINIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0027"><h3>DBD/PSB/ACB IMS管理ACB 復旧後の確認 ACB06</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>復旧後の確認では DBD/PSB/ACB（管理・定義名と有効版） の カタログ取込結果 を主操作として ACB06 を判定します。再発していないことを示す値への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB06 に残します。復旧後の確認を補助する DB定義照会 では AVAILABLE を補助値として ACB06 へ保存します。主判定の復旧後の確認では管理・定義名と有効版の カタログ取込結果 から COMPLETE を読み ACB06 へ残します。証跡照合の復旧後の確認では管理・定義名と有効版の COMPLETE と AVAILABLE を ACB06 に保存します。記録対応の復旧後の確認では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で DBD/PSB/ACB の カタログ取込結果 と DB定義照会 を実施し IMS管理ACB の役割を確認します。カタログ定義と稼働定義の世代差を見落とす危険があります。対象 ACB06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. ログ管理のアクティブログとアーカイブ先を確認する。その値をDBD/PSB/ACBのACB06にも適用する。</li><li>B. IMPORT DEFN SOURCE(CATALOG)でCOMPLETEを取得してからQUERY PGM NAME(PGM06) SHOW(ALL)でNOTINITを照合する。ACB06の定義名と有効版を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. QUERY DB NAME(ACB06) SHOW(ALL)が成功したためIMPORT DEFN SOURCE(CATALOG)のCOMPLETEも正常だと推定する。主出力は保存しない。別資源で得た状態を対象ACB06へ引き継げるものとする。</li><li>D. IMPORT DEFN SOURCE(CATALOG)を対象名なしで実行する。一覧の先頭行をACB06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Bはカタログ取込結果で COMPLETE を読み定義名と有効版の主値として復旧後の安定性を確認しACB06に残します。
構成上の背景: 復旧後の確認ではDB定義照会を補助操作としIMS管理ACBの再発していないことを示す値をAVAILABLEと対象ACB06で照合します。
候補ごとの理由: カタログ取込結果とDB定義照会の役割を分けるとA: ログ管理の値ではCOMPLETEを確認できない点でDB定義照会の範囲を越えます、B: COMPLETEとNOTINITを順に照合する点で現在値を示します、C: 補助操作の成功ではCOMPLETEを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はACB06と確定できない点でカタログ取込結果を代替しません。結論として復旧後の確認の管理・定義名と有効版で判定する対象は ACB06 です。
初出用語: 復旧後の確認で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 復旧後の確認 ACB06</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて復旧後の安定性を確認し、ACB06の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB06のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB06) SHOW(ALL)を指定し、ACB06のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB06) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB06&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM06) SHOW(ALL)を指定し、ACB06のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM06) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM06&lt;/pgm&gt;&lt;psb&gt;PSB06&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の COMPLETE が画面・出力に表示されること
② ステップ2 の AVAILABLE が画面・出力に表示されること
③ ステップ3 の NOTINIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0028"><h3>DBD/PSB/ACB IMS管理ACB 復旧準備 ACB05</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>復旧準備では DBD/PSB/ACB（管理・定義名と有効版） の プログラム定義照会 を主操作として ACB05 を判定します。再開前に必要な整合性への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB05 に残します。復旧準備を補助する カタログ取込結果 では COMPLETE を補助値として ACB05 へ保存します。主判定の復旧準備では管理・定義名と有効版の プログラム定義照会 から NOTINIT を読み ACB05 へ残します。証跡照合の復旧準備では管理・定義名と有効版の NOTINIT と COMPLETE を ACB05 に保存します。記録対応の復旧準備では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で DBD/PSB/ACB の プログラム定義照会 と カタログ取込結果 を使い 復旧条件を確認 します。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。NOTINIT を読み対象 ACB05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずQUERY PGM NAME(PGM05) SHOW(ALL)を実行する。NOTINITを保存する。差分はIMPORT DEFN SOURCE(CATALOG)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したQUERY PGM NAME(PGM05) SHOW(ALL)の結果を使う。今回のIMPORT DEFN SOURCE(CATALOG)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのACB05の出力を再利用する。今回のQUERY PGM NAME(PGM05) SHOW(ALL)とIMPORT DEFN SOURCE(CATALOG)は実行済みとして扱う。</li><li>D. IMPORT DEFN SOURCE(CATALOG)のCOMPLETEを定義名と有効版の主判定に採用する。QUERY PGM NAME(PGM05) SHOW(ALL)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはプログラム定義照会で NOTINIT を読み定義名と有効版の主値として復旧条件を確認しACB05に残します。
処理の仕組み: 復旧準備ではカタログ取込結果を補助操作としIMS管理ACBの再開前に必要な整合性をCOMPLETEと対象ACB05で照合します。
選択結果の内訳: プログラム定義照会とカタログ取込結果の役割を分けるとA: 変更前のNOTINITを保存する点でプログラム定義照会に合います、B: 採取時刻が異なる点でDBD/PSB/ACBに使いません、C: 過去出力では今回の復旧準備を示せない点でIMS管理ACBに使えません、D: COMPLETEはNOTINITを代替しないうえに追加前提も不正な点でACB05を採用できません。結論として復旧準備の管理・定義名と有効版で判定する対象は ACB05 です。
用語の説明: 復旧準備で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 復旧準備 ACB05</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて復旧条件を確認し、ACB05の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM05) SHOW(ALL)を指定し、ACB05のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM05) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM05&lt;/pgm&gt;&lt;psb&gt;PSB05&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB05のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB05) SHOW(ALL)を指定し、ACB05のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB05) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB05&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の NOTINIT が画面・出力に表示されること
② ステップ2 の COMPLETE が画面・出力に表示されること
③ ステップ3 の AVAILABLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0029"><h3>DBD/PSB/ACB IMS管理ACB 構成監査 ACB08</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>構成監査では DBD/PSB/ACB（管理・定義名と有効版） の プログラム定義照会 を主操作として ACB08 を判定します。定義値と稼働値の一致への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB08 に残します。構成監査を補助する カタログ取込結果 では COMPLETE を補助値として ACB08 へ保存します。主判定の構成監査では管理・定義名と有効版の プログラム定義照会 から NOTINIT を読み ACB08 へ残します。証跡照合の構成監査では管理・定義名と有効版の NOTINIT と COMPLETE を ACB08 に保存します。記録対応の構成監査では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で DBD/PSB/ACB の プログラム定義照会 と カタログ取込結果 を照合し 定義値と稼働値の一致 を確かめます。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。NOTINIT を読む前に対象 ACB08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのACB08の出力を再利用する。今回のQUERY PGM NAME(PGM08) SHOW(ALL)とIMPORT DEFN SOURCE(CATALOG)は実行済みとして扱う。</li><li>B. IMPORT DEFN SOURCE(CATALOG)のCOMPLETEを定義名と有効版の主判定に採用する。QUERY PGM NAME(PGM08) SHOW(ALL)の応答は採取対象から外す。</li><li>C. QUERY DB NAME(ACB08) SHOW(ALL)のAVAILABLEをNOTINITと同義の成功表示として扱う。QUERY PGM NAME(PGM08) SHOW(ALL)は実行しない。</li><li>D. IMPORT DEFN SOURCE(CATALOG)の結果だけでは確定しない。QUERY PGM NAME(PGM08) SHOW(ALL)のNOTINITを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはプログラム定義照会で NOTINIT を読み定義名と有効版の主値として構成差分を監査しACB08に残します。
実行時の背景: 構成監査ではカタログ取込結果を補助操作としIMS管理ACBの定義値と稼働値の一致をCOMPLETEと対象ACB08で照合します。
四つの候補の理由: プログラム定義照会とカタログ取込結果の役割を分けるとA: 過去出力では今回の構成監査を示せない点でDBD/PSB/ACBに使いません、B: COMPLETEはNOTINITを代替しない点でIMS管理ACBに使えません、C: AVAILABLEとNOTINITは確認項目が異なる点でACB08を採用できません、D: NOTINITを主証跡として区別する点で主証跡になります。結論として構成監査の管理・定義名と有効版で判定する対象は ACB08 です。
初出語定義: 構成監査で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 構成監査 ACB08</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて構成差分を監査し、ACB08の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM08) SHOW(ALL)を指定し、ACB08のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM08) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM08&lt;/pgm&gt;&lt;psb&gt;PSB08&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB08のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB08) SHOW(ALL)を指定し、ACB08のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB08) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB08&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の NOTINIT が画面・出力に表示されること
② ステップ2 の COMPLETE が画面・出力に表示されること
③ ステップ3 の AVAILABLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0030"><h3>DBD/PSB/ACB IMS管理ACB 通常状態の確認 ACB01</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>通常状態の確認では DBD/PSB/ACB（管理・定義名と有効版） の DB定義照会 を主操作として ACB01 を判定します。基準値と現在値の差への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB01 に残します。通常状態の確認を補助する プログラム定義照会 では NOTINIT を補助値として ACB01 へ保存します。主判定の通常状態の確認では管理・定義名と有効版の DB定義照会 から AVAILABLE を読み ACB01 へ残します。証跡照合の通常状態の確認では管理・定義名と有効版の AVAILABLE と NOTINIT を ACB01 に保存します。記録対応の通常状態の確認では管理・定義名と有効版の 定義名と有効版 の証跡へ ACB01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で DBD/PSB/ACB の DB定義照会 と プログラム定義照会 を用い 通常状態を確定 します。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。AVAILABLE で対象 ACB01 の 定義名と有効版 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. QUERY DB NAME(ACB01) SHOW(ALL)を先に実行する。対象ACB01のAVAILABLEを定義名と有効版として記録する。続いてQUERY PGM NAME(PGM01) SHOW(ALL)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. QUERY PGM NAME(PGM01) SHOW(ALL)のNOTINITを定義名と有効版の主判定に採用する。QUERY DB NAME(ACB01) SHOW(ALL)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. IMPORT DEFN SOURCE(CATALOG)のCOMPLETEをAVAILABLEと同義の成功表示として扱う。QUERY DB NAME(ACB01) SHOW(ALL)は実行しない。</li><li>D. QUERY DB NAME(ACB01) SHOW(ALL)が応答を返した時点で正常とする。応答中のAVAILABLEの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: AはDB定義照会で AVAILABLE を読み定義名と有効版の主値として通常状態を確定しACB01に残します。
背景・仕組み: 通常状態の確認ではプログラム定義照会を補助操作としIMS管理ACBの基準値と現在値の差をNOTINITと対象ACB01で照合します。
選択肢の理由: DB定義照会とプログラム定義照会の役割を分けるとA: AVAILABLEを主値として補助結果と照合する点で正答です、B: NOTINITはAVAILABLEを代替しないうえに追加前提も不正な点でACB01を採用できません、C: COMPLETEとAVAILABLEは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけでは定義名と有効版を判定できない点で一次資料と一致しません。結論として通常状態の確認の管理・定義名と有効版で判定する対象は ACB01 です。
用語の初出定義: 通常状態の確認で使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 通常状態の確認 ACB01</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて通常状態を確定し、ACB01の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB01) SHOW(ALL)を指定し、ACB01のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB01) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB01&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM01) SHOW(ALL)を指定し、ACB01のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM01) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM01&lt;/pgm&gt;&lt;psb&gt;PSB01&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB01のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AVAILABLE が画面・出力に表示されること
② ステップ2 の NOTINIT が画面・出力に表示されること
③ ステップ3 の COMPLETE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0031"><h3>DBD/PSB/ACB IMS管理ACB 障害切り分け ACB04</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>障害切り分けでは DBD/PSB/ACB（管理・定義名と有効版） の DB定義照会 を主操作として ACB04 を判定します。最初に失敗した処理への注意として「カタログ定義と稼働定義の世代差を見落とす危険があります」を ACB04 に残します。障害切り分けを補助する プログラム定義照会 では NOTINIT を補助値として ACB04 へ保存します。主判定の障害切り分けでは管理・定義名と有効版の DB定義照会 から AVAILABLE を読み ACB04 へ残します。証跡照合の障害切り分けでは管理・定義名と有効版の AVAILABLE と NOTINIT を ACB04 に保存します。記録対応の障害切り分けでは管理・定義名と有効版の 定義名と有効版 の証跡へ ACB04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで DBD/PSB/ACB の DB定義照会 と プログラム定義照会 の役割を分け 最初に失敗した処理 を調べます。IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みです。カタログ定義と稼働定義の世代差を見落とす危険があります。対象 ACB04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. IMPORT DEFN SOURCE(CATALOG)のCOMPLETEをAVAILABLEと同義の成功表示として扱う。QUERY DB NAME(ACB04) SHOW(ALL)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. QUERY DB NAME(ACB04) SHOW(ALL)が応答を返した時点で正常とする。応答中のAVAILABLEの値は記録しない。</li><li>C. QUERY DB NAME(ACB04) SHOW(ALL)のコマンド文字列だけを記録する。AVAILABLEを含む応答行は保存しない。</li><li>D. QUERY DB NAME(ACB04) SHOW(ALL)の出力でACB04とAVAILABLEが同じ応答にあることを確認する。定義名と有効版をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: DはDB定義照会で AVAILABLE を読み定義名と有効版の主値として障害範囲を限定しACB04に残します。
技術的背景: 障害切り分けではプログラム定義照会を補助操作としIMS管理ACBの最初に失敗した処理をNOTINITと対象ACB04で照合します。
四択の評価: DB定義照会とプログラム定義照会の役割を分けるとA: COMPLETEとAVAILABLEは確認項目が異なるうえに追加前提も不正な点でACB04を採用できません、B: 応答の有無だけでは定義名と有効版を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけでは定義名と有効版を証明できない点で一次資料と一致しません、D: ACB04とAVAILABLEを同じ応答で結ぶ点でACB04を判定できます。結論として障害切り分けの管理・定義名と有効版で判定する対象は ACB04 です。
初出語の意味: 障害切り分けで使う IMS管理ACB はDBDとPSBの実行定義をIMSカタログから参照し、オンラインで有効な定義を管理する仕組みを表し定義名と有効版を判定する際にACB04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD/PSB/ACB IMS管理ACB 障害切り分け ACB04</strong></p><p>検証目的: DBD/PSB/ACBのIMS管理ACBについて障害範囲を限定し、ACB04の定義名と有効版を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ACB04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY DB NAME(ACB04) SHOW(ALL)を指定し、ACB04のDB定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(ACB04) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;ACB04&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるAVAILABLEを読み、定義名と有効版と対象ACB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へQUERY PGM NAME(PGM04) SHOW(ALL)を指定し、ACB04のプログラム定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY PGM NAME(PGM04) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;pgm&gt;PGM04&lt;/pgm&gt;&lt;psb&gt;PSB04&lt;/psb&gt;&lt;stt&gt;NOTINIT&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるNOTINITを読み、定義名と有効版と対象ACB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBD/PSB/ACBを確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、ACB04のカタログ取込結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;src&gt;CATALOG&lt;/src&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるCOMPLETEを読み、定義名と有効版と対象ACB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AVAILABLE が画面・出力に表示されること
② ステップ2 の NOTINIT が画面・出力に表示されること
③ ステップ3 の COMPLETE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0032"><h3>DBRC RECON record 再始動確認 資料見出し</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「DBRC RECON record 再始動確認 資料見出し」は、DBDS、イメージコピー、ログ、変更累積のリカバリ管理情報を保持するRECON記録を再始動確認の観点で確認する技術項目です。DBD 名とDBD041を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC RECON record 再始動確認 資料見出し</strong></p><p>検証目的: DBD/PSB/ACBにおけるDBRC RECON recordの再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD041</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY041
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY041 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD041
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD041 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA1
→ Enter を押す
［画面・出力］
DFS000I AREA AREA1 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0033"><h3>DFS058I ログ照合 更新対象</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「DFS058I ログ照合 更新対象」は、/NRESTART処理開始を示すIMSメッセージをログ照合の観点で確認する技術項目です。DBD 名と82162/085220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS058I ログ照合 更新対象</strong></p><p>検証目的: DBD/PSB/ACBにおけるDFS058Iのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82162/085220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0034"><h3>DFSUCUM0 実行条件確認 識別値</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「DFSUCUM0 実行条件確認 識別値」は、SLDS/RLDSの変更記録を変更累積データセットへまとめるIMSユーティリティを実行条件確認の観点で確認する技術項目です。DBD 名とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUCUM0 実行条件確認 識別値</strong></p><p>検証目的: DBD/PSB/ACBにおけるDFSUCUM0の実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD077)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD077  DD=DBDS01  RECON=RECON2
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS5 ARCHIVED TO SLDS5
RLDS STATUS AVAILABLE
画面・出力には OLDS5 が含まれ、OLDS5を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS5 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0035"><h3>DFSUCUM0 接続確認 一致条件</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 初級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「DFSUCUM0 接続確認 一致条件」は、SLDS/RLDSの変更記録を変更累積データセットへまとめるIMSユーティリティを接続確認の観点で確認する技術項目です。DBD 名とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUCUM0 接続確認 一致条件</strong></p><p>検証目的: DBD/PSB/ACBにおけるDFSUCUM0の接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD017)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD017  DD=DBDS01  RECON=RECON2
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS5 ARCHIVED TO SLDS5
RLDS STATUS AVAILABLE
画面・出力には OLDS5 が含まれ、OLDS5を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS5 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0036"><h3>IMS catalog 実行条件確認 性能値</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 中級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「IMS catalog 実行条件確認 性能値」は、IMS管理ACBでアクティブ定義の参照元になるカタログを実行条件確認の観点で確認する技術項目です。DBD 名とPSB029を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS catalog 実行条件確認 性能値</strong></p><p>検証目的: DBD/PSB/ACBにおけるIMS catalogの実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB029</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD029) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD029 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0037"><h3>IMS catalog 状態確認 イベント転送</h3><p class="kb-meta">分類: DBD/PSB/ACB ・ 難易度: 上級</p><p>IMS 15.5 の DBD/PSB/ACB で扱う「IMS catalog 状態確認 イベント転送」は、IMS管理ACBでアクティブ定義の参照元になるカタログを状態確認の観点で確認する技術項目です。DBD 名とPSB089を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS catalog 状態確認 イベント転送</strong></p><p>検証目的: DBD/PSB/ACBにおけるIMS catalogの状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB089</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD089) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD089 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


## DBRC/RECON


<section class="kb-item" id="c16-i0038"><h3>/CHECKPOINT FREEZE ログ照合 属性確認</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 初級</p><p>IMS 15.5 の DBRC/RECON で扱う「/CHECKPOINT FREEZE ログ照合 属性確認」は、入力を凍結し、既存処理とBMPチェックポイント到達を待つ停止系チェックポイントをログ照合の観点で確認する技術項目です。RECON 欄とRECON1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT FREEZE ログ照合 属性確認</strong></p><p>検証目的: DBRC/RECONにおける/CHECKPOINT FREEZEのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO004&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM4&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM4) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM4  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM4&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0039"><h3>/CHECKPOINT FREEZE 整合確認 管理値</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>IMS 15.5 の DBRC/RECON で扱う「/CHECKPOINT FREEZE 整合確認 管理値」は、入力を凍結し、既存処理とBMPチェックポイント到達を待つ停止系チェックポイントを整合確認の観点で確認する技術項目です。RECON 欄とRECON1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT FREEZE 整合確認 管理値</strong></p><p>検証目的: DBRC/RECONにおける/CHECKPOINT FREEZEの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO064&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM4&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM4) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM4  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM4&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0040"><h3>DBRC/RECON RECONリカバリ管理 ログとの照合 DBD07</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>ログとの照合では DBRC/RECON（リカバリ管理・登録と可用性） の RECON状態 を主操作として DBD07 を判定します。時刻と対象識別子への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD07 に残します。ログとの照合を補助する DBDS登録 では DBDS01 を補助値として DBD07 へ保存します。主判定のログとの照合ではリカバリ管理・登録と可用性の RECON状態 から RECON1 を読み DBD07 へ残します。証跡照合のログとの照合ではリカバリ管理・登録と可用性の RECON1 と DBDS01 を DBD07 に保存します。記録対応のログとの照合ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で DBRC/RECON の RECON状態 と DBDS登録 を組み合わせる際は RECONリカバリ管理 がDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能という仕組みを前提にします。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。RECON1 と DBDS登録とRECON可用性 を対象 DBD07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. RECON1を含むRECON状態の応答行を保存する。その応答を得るためLIST.RECON STATUSを使用する。対象DBD07のDBDS登録とRECON可用性として記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. LIST.RECON STATUSが応答を返した時点で正常とする。応答中のRECON1の値は記録しない。SLDS1をRECON1と同じ判定値とみなし対象DBD07の主証跡にする。RECONリカバリ管理の時刻と対象識別子は確認済みとして扱う。さらにLIST.LOG ALLのSLDS1をRECON1と同種の値として併記する。</li><li>C. LIST.RECON STATUSのコマンド文字列だけを記録する。RECON1を含む応答行は保存しない。</li><li>D. RECONリカバリ管理の停止または再定義を実施する。その後にLIST.RECON STATUSでRECON1を採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: AはRECON状態で RECON1 を読みDBDS登録とRECON可用性の主値として操作とログを対応しDBD07に残します。
機能の仕組み: ログとの照合ではDBDS登録を補助操作としRECONリカバリ管理の時刻と対象識別子をDBDS01と対象DBD07で照合します。
各候補の評価: RECON状態とDBDS登録の役割を分けるとA: RECON1の実値を対象別に残す点で主証跡になります、B: 応答の有無だけではDBDS登録とRECON可用性を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではDBDS登録とRECON可用性を証明できない点でDBDS登録とRECON可用性を確認できません、D: 変更前のDBDS登録とRECON可用性を失う点でDBDS登録の範囲を越えます。結論としてログとの照合のリカバリ管理・登録と可用性で判定する対象は DBD07 です。
用語の定義: ログとの照合で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 ログとの照合 DBD07</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について操作とログを対応し、DBD07のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD07のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD07)を指定し、DBD07のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD07)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD07 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD07のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECON1 が画面・出力に表示されること
② ステップ2 の DBDS01 が画面・出力に表示されること
③ ステップ3 の SLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0041"><h3>DBRC/RECON RECONリカバリ管理 代替経路の確認 DBD10</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>代替経路の確認では DBRC/RECON（リカバリ管理・登録と可用性） の RECON状態 を主操作として DBD10 を判定します。主経路との役割差への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD10 に残します。代替経路の確認を補助する DBDS登録 では DBDS01 を補助値として DBD10 へ保存します。主判定の代替経路の確認ではリカバリ管理・登録と可用性の RECON状態 から RECON1 を読み DBD10 へ残します。証跡照合の代替経路の確認ではリカバリ管理・登録と可用性の RECON1 と DBDS01 を DBD10 に保存します。記録対応の代替経路の確認ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で DBRC/RECON の RECON状態 と DBDS登録 を実施し RECONリカバリ管理 の役割を確認します。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。対象 DBD10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. LIST.RECON STATUSのコマンド文字列だけを記録する。RECON1を含む応答行は保存しない。</li><li>B. RECONリカバリ管理の停止または再定義を実施する。その後にLIST.RECON STATUSでRECON1を採取する。</li><li>C. DBD/PSB/ACBの定義名と有効版を確認する。その値をDBRC/RECONのDBD10にも適用する。</li><li>D. LIST.RECON STATUSとLIST.DBDS DBD(DBD10)の対象名をそろえる。前者のRECON1をDBDS登録とRECON可用性の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: DはRECON状態で RECON1 を読みDBDS登録とRECON可用性の主値として代替手段の成立を確認しDBD10に残します。
運用上の背景: 代替経路の確認ではDBDS登録を補助操作としRECONリカバリ管理の主経路との役割差をDBDS01と対象DBD10で照合します。
候補別の検討: RECON状態とDBDS登録の役割を分けるとA: 入力記録だけではDBDS登録とRECON可用性を証明できない点で一次資料と一致しません、B: 変更前のDBDS登録とRECON可用性を失う点でDBDS登録とRECON可用性を確認できません、C: DBD/PSB/ACBの値ではRECON1を確認できない点でDBDS登録の範囲を越えます、D: 同じ対象名のRECON1を採用する点で現在値を示します。結論として代替経路の確認のリカバリ管理・登録と可用性で判定する対象は DBD10 です。
重要用語の定義: 代替経路の確認で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 代替経路の確認 DBD10</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について代替手段の成立を確認し、DBD10のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD10のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD10)を指定し、DBD10のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD10)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD10 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD10のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECON1 が画面・出力に表示されること
② ステップ2 の DBDS01 が画面・出力に表示されること
③ ステップ3 の SLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0042"><h3>DBRC/RECON RECONリカバリ管理 変更前の確認 DBD02</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>変更前の確認では DBRC/RECON（リカバリ管理・登録と可用性） の DBDS登録 を主操作として DBD02 を判定します。変更対象と非対象の境界への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD02 に残します。変更前の確認を補助する ログ登録 では SLDS1 を補助値として DBD02 へ保存します。主判定の変更前の確認ではリカバリ管理・登録と可用性の DBDS登録 から DBDS01 を読み DBD02 へ残します。証跡照合の変更前の確認ではリカバリ管理・登録と可用性の DBDS01 と SLDS1 を DBD02 に保存します。記録対応の変更前の確認ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で DBRC/RECON の DBDS登録 と ログ登録 の役割を分け 変更対象と非対象の境界 を調べます。RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能です。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。対象 DBD02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. LIST.DBDS DBD(DBD02)を対象名なしで実行する。一覧の先頭行をDBD02の結果として記録する。</li><li>B. 前回保存したLIST.DBDS DBD(DBD02)の結果を使う。今回のLIST.LOG ALLの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのDBD02の出力を再利用する。今回のLIST.DBDS DBD(DBD02)とLIST.LOG ALLは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象DBD02についてLIST.DBDS DBD(DBD02)の応答からDBDS01を確認する。LIST.LOG ALLは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: DはDBDS登録で DBDS01 を読みDBDS登録とRECON可用性の主値として変更前の証跡を保存しDBD02に残します。
動作の背景: 変更前の確認ではログ登録を補助操作としRECONリカバリ管理の変更対象と非対象の境界をSLDS1と対象DBD02で照合します。
各選択肢の検討: DBDS登録とログ登録の役割を分けるとA: 先頭行はDBD02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でDBDS登録を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でDBRC/RECONに使いません、D: DBDS01と補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のリカバリ管理・登録と可用性で判定する対象は DBD02 です。
初出用語の定義: 変更前の確認で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 変更前の確認 DBD02</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について変更前の証跡を保存し、DBD02のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD02)を指定し、DBD02のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD02)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD02 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD02のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD02のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DBDS01 が画面・出力に表示されること
② ステップ2 の SLDS1 が画面・出力に表示されること
③ ステップ3 の RECON1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0043"><h3>DBRC/RECON RECONリカバリ管理 変更後の確認 DBD03</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>変更後の確認では DBRC/RECON（リカバリ管理・登録と可用性） の ログ登録 を主操作として DBD03 を判定します。反映値と残存値への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD03 に残します。変更後の確認を補助する RECON状態 では RECON1 を補助値として DBD03 へ保存します。主判定の変更後の確認ではリカバリ管理・登録と可用性の ログ登録 から SLDS1 を読み DBD03 へ残します。証跡照合の変更後の確認ではリカバリ管理・登録と可用性の SLDS1 と RECON1 を DBD03 に保存します。記録対応の変更後の確認ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で DBRC/RECON の ログ登録 と RECON状態 を使い 変更結果を検証 します。RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能です。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。SLDS1 を読み対象 DBD03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. LIST.RECON STATUSで周辺状態を押さえる。その後にLIST.LOG ALLでSLDS1を確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. RECONリカバリ管理の停止または再定義を実施する。その後にLIST.LOG ALLでSLDS1を採取する。</li><li>C. データベースユーティリティのユーティリティ名と戻りコードを確認する。その値をDBRC/RECONのDBD03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>D. LIST.RECON STATUSが成功したためLIST.LOG ALLのSLDS1も正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aはログ登録で SLDS1 を読みDBDS登録とRECON可用性の主値として変更結果を検証しDBD03に残します。
内部の仕組み: 変更後の確認ではRECON状態を補助操作としRECONリカバリ管理の反映値と残存値をRECON1と対象DBD03で照合します。
誤答を含む比較: ログ登録とRECON状態の役割を分けるとA: 周辺状態の後にSLDS1を確認する点でDBD03を判定できます、B: 変更前のDBDS登録とRECON可用性を失う点でRECON状態の範囲を越えます、C: データベースユーティリティの値ではSLDS1を確認できないうえに追加前提も不正な点でDBD03の値を示しません、D: 補助操作の成功ではSLDS1を確定できない点で変更後の確認に合いません。結論として変更後の確認のリカバリ管理・登録と可用性で判定する対象は DBD03 です。
用語定義: 変更後の確認で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 変更後の確認 DBD03</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について変更結果を検証し、DBD03のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD03のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD03のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD03)を指定し、DBD03のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD03)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD03 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SLDS1 が画面・出力に表示されること
② ステップ2 の RECON1 が画面・出力に表示されること
③ ステップ3 の DBDS01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0044"><h3>DBRC/RECON RECONリカバリ管理 引継ぎ記録 DBD09</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>引継ぎ記録では DBRC/RECON（リカバリ管理・登録と可用性） の ログ登録 を主操作として DBD09 を判定します。次担当者が追跡できる証跡への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD09 に残します。引継ぎ記録を補助する RECON状態 では RECON1 を補助値として DBD09 へ保存します。主判定の引継ぎ記録ではリカバリ管理・登録と可用性の ログ登録 から SLDS1 を読み DBD09 へ残します。証跡照合の引継ぎ記録ではリカバリ管理・登録と可用性の SLDS1 と RECON1 を DBD09 に保存します。記録対応の引継ぎ記録ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で DBRC/RECON の ログ登録 と RECON状態 を使い 再現可能な記録を作成 します。RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能です。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。SLDS1 を読み対象 DBD09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. LIST.RECON STATUSが成功したためLIST.LOG ALLのSLDS1も正常だと推定する。主出力は保存しない。</li><li>B. LIST.LOG ALLを対象名なしで実行する。一覧の先頭行をDBD09の結果として記録する。</li><li>C. 対象名DBD09を指定してLIST.LOG ALLを実行する。応答中のSLDS1と時刻を保存する。LIST.RECON STATUSで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したLIST.LOG ALLの結果を使う。今回のLIST.RECON STATUSの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cはログ登録で SLDS1 を読みDBDS登録とRECON可用性の主値として再現可能な記録を作成しDBD09に残します。
製品内の仕組み: 引継ぎ記録ではRECON状態を補助操作としRECONリカバリ管理の次担当者が追跡できる証跡をRECON1と対象DBD09で照合します。
選択肢別の説明: ログ登録とRECON状態の役割を分けるとA: 補助操作の成功ではSLDS1を確定できない点でDBD09の値を示しません、B: 先頭行はDBD09と確定できない点で引継ぎ記録に合いません、C: SLDS1と時刻を保存する点でログ登録に合います、D: 採取時刻が異なる点でDBRC/RECONに使いません。結論として引継ぎ記録のリカバリ管理・登録と可用性で判定する対象は DBD09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 引継ぎ記録 DBD09</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について再現可能な記録を作成し、DBD09のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD09のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD09のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD09)を指定し、DBD09のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD09)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD09 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SLDS1 が画面・出力に表示されること
② ステップ2 の RECON1 が画面・出力に表示されること
③ ステップ3 の DBDS01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0045"><h3>DBRC/RECON RECONリカバリ管理 復旧後の確認 DBD06</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>復旧後の確認では DBRC/RECON（リカバリ管理・登録と可用性） の ログ登録 を主操作として DBD06 を判定します。再発していないことを示す値への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD06 に残します。復旧後の確認を補助する RECON状態 では RECON1 を補助値として DBD06 へ保存します。主判定の復旧後の確認ではリカバリ管理・登録と可用性の ログ登録 から SLDS1 を読み DBD06 へ残します。証跡照合の復旧後の確認ではリカバリ管理・登録と可用性の SLDS1 と RECON1 を DBD06 に保存します。記録対応の復旧後の確認ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で DBRC/RECON の ログ登録 と RECON状態 を照合し 再発していないことを示す値 を確かめます。RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能です。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。SLDS1 を読む前に対象 DBD06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. DB/DC運用のSTATUSとQUEUEを確認する。その値をDBRC/RECONのDBD06にも適用する。</li><li>B. LIST.RECON STATUSが成功したためLIST.LOG ALLのSLDS1も正常だと推定する。主出力は保存しない。別資源で得た状態を対象DBD06へ引き継げるものとする。RECONリカバリ管理の再発していないことを示す値は確認済みとして扱う。さらにLIST.DBDS DBD(DBD06)のDBDS01をSLDS1と同種の値として併記する。</li><li>C. LIST.LOG ALLを対象名なしで実行する。一覧の先頭行をDBD06の結果として記録する。</li><li>D. LIST.LOG ALLでSLDS1を取得してからLIST.DBDS DBD(DBD06)でDBDS01を照合する。DBD06のDBDS登録とRECON可用性を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dはログ登録で SLDS1 を読みDBDS登録とRECON可用性の主値として復旧後の安定性を確認しDBD06に残します。
構成上の背景: 復旧後の確認ではRECON状態を補助操作としRECONリカバリ管理の再発していないことを示す値をRECON1と対象DBD06で照合します。
候補ごとの理由: ログ登録とRECON状態の役割を分けるとA: DB/DC運用の値ではSLDS1を確認できない点でRECON状態の範囲を越えます、B: 補助操作の成功ではSLDS1を確定できないうえに追加前提も不正な点でDBD06の値を示しません、C: 先頭行はDBD06と確定できない点で復旧後の確認に合いません、D: SLDS1とDBDS01を順に照合する点でログ登録に合います。結論として復旧後の確認のリカバリ管理・登録と可用性で判定する対象は DBD06 です。
初出用語: 復旧後の確認で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 復旧後の確認 DBD06</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について復旧後の安定性を確認し、DBD06のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD06のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD06のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD06)を指定し、DBD06のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD06)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD06 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SLDS1 が画面・出力に表示されること
② ステップ2 の RECON1 が画面・出力に表示されること
③ ステップ3 の DBDS01 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0046"><h3>DBRC/RECON RECONリカバリ管理 復旧準備 DBD05</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>復旧準備では DBRC/RECON（リカバリ管理・登録と可用性） の DBDS登録 を主操作として DBD05 を判定します。再開前に必要な整合性への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD05 に残します。復旧準備を補助する ログ登録 では SLDS1 を補助値として DBD05 へ保存します。主判定の復旧準備ではリカバリ管理・登録と可用性の DBDS登録 から DBDS01 を読み DBD05 へ残します。証跡照合の復旧準備ではリカバリ管理・登録と可用性の DBDS01 と SLDS1 を DBD05 に保存します。記録対応の復旧準備ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で DBRC/RECON の DBDS登録 と ログ登録 を用い 復旧条件を確認 します。RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能です。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。DBDS01 で対象 DBD05 の DBDS登録とRECON可用性 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したLIST.DBDS DBD(DBD05)の結果を使う。今回のLIST.LOG ALLの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのDBD05の出力を再利用する。今回のLIST.DBDS DBD(DBD05)とLIST.LOG ALLは実行済みとして扱う。</li><li>C. 変更を加えずLIST.DBDS DBD(DBD05)を実行する。DBDS01を保存する。差分はLIST.LOG ALLの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. LIST.LOG ALLのSLDS1をDBDS登録とRECON可用性の主判定に採用する。LIST.DBDS DBD(DBD05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: CはDBDS登録で DBDS01 を読みDBDS登録とRECON可用性の主値として復旧条件を確認しDBD05に残します。
処理の仕組み: 復旧準備ではログ登録を補助操作としRECONリカバリ管理の再開前に必要な整合性をSLDS1と対象DBD05で照合します。
選択結果の内訳: DBDS登録とログ登録の役割を分けるとA: 採取時刻が異なる点でDBDS登録を代替しません、B: 過去出力では今回の復旧準備を示せない点でDBRC/RECONに使いません、C: 変更前のDBDS01を保存する点で正答です、D: SLDS1はDBDS01を代替しないうえに追加前提も不正な点でDBD05を採用できません。結論として復旧準備のリカバリ管理・登録と可用性で判定する対象は DBD05 です。
用語の説明: 復旧準備で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 復旧準備 DBD05</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について復旧条件を確認し、DBD05のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD05)を指定し、DBD05のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD05)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD05 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD05のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD05のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DBDS01 が画面・出力に表示されること
② ステップ2 の SLDS1 が画面・出力に表示されること
③ ステップ3 の RECON1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0047"><h3>DBRC/RECON RECONリカバリ管理 構成監査 DBD08</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>構成監査では DBRC/RECON（リカバリ管理・登録と可用性） の DBDS登録 を主操作として DBD08 を判定します。定義値と稼働値の一致への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD08 に残します。構成監査を補助する ログ登録 では SLDS1 を補助値として DBD08 へ保存します。主判定の構成監査ではリカバリ管理・登録と可用性の DBDS登録 から DBDS01 を読み DBD08 へ残します。証跡照合の構成監査ではリカバリ管理・登録と可用性の DBDS01 と SLDS1 を DBD08 に保存します。記録対応の構成監査ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で DBRC/RECON の DBDS登録 と ログ登録 の役割を分け 定義値と稼働値の一致 を調べます。RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能です。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。対象 DBD08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのDBD08の出力を再利用する。今回のLIST.DBDS DBD(DBD08)とLIST.LOG ALLは実行済みとして扱う。</li><li>B. LIST.LOG ALLの結果だけでは確定しない。LIST.DBDS DBD(DBD08)のDBDS01を主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. LIST.LOG ALLのSLDS1をDBDS登録とRECON可用性の主判定に採用する。LIST.DBDS DBD(DBD08)の応答は採取対象から外す。</li><li>D. LIST.RECON STATUSのRECON1をDBDS01と同義の成功表示として扱う。LIST.DBDS DBD(DBD08)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: BはDBDS登録で DBDS01 を読みDBDS登録とRECON可用性の主値として構成差分を監査しDBD08に残します。
実行時の背景: 構成監査ではログ登録を補助操作としRECONリカバリ管理の定義値と稼働値の一致をSLDS1と対象DBD08で照合します。
四つの候補の理由: DBDS登録とログ登録の役割を分けるとA: 過去出力では今回の構成監査を示せない点でDBRC/RECONに使いません、B: DBDS01を主証跡として区別する点で正答です、C: SLDS1はDBDS01を代替しない点でDBD08を採用できません、D: RECON1とDBDS01は確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のリカバリ管理・登録と可用性で判定する対象は DBD08 です。
初出語定義: 構成監査で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 構成監査 DBD08</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について構成差分を監査し、DBD08のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD08)を指定し、DBD08のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD08)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD08 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD08のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD08のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DBDS01 が画面・出力に表示されること
② ステップ2 の SLDS1 が画面・出力に表示されること
③ ステップ3 の RECON1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0048"><h3>DBRC/RECON RECONリカバリ管理 通常状態の確認 DBD01</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>通常状態の確認では DBRC/RECON（リカバリ管理・登録と可用性） の RECON状態 を主操作として DBD01 を判定します。基準値と現在値の差への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD01 に残します。通常状態の確認を補助する DBDS登録 では DBDS01 を補助値として DBD01 へ保存します。主判定の通常状態の確認ではリカバリ管理・登録と可用性の RECON状態 から RECON1 を読み DBD01 へ残します。証跡照合の通常状態の確認ではリカバリ管理・登録と可用性の RECON1 と DBDS01 を DBD01 に保存します。記録対応の通常状態の確認ではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で DBRC/RECON の RECON状態 と DBDS登録 を組み合わせる際は RECONリカバリ管理 がDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能という仕組みを前提にします。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。RECON1 と DBDS登録とRECON可用性 を対象 DBD01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. LIST.DBDS DBD(DBD01)のDBDS01をDBDS登録とRECON可用性の主判定に採用する。LIST.RECON STATUSの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. LIST.LOG ALLのSLDS1をRECON1と同義の成功表示として扱う。LIST.RECON STATUSは実行しない。</li><li>C. LIST.RECON STATUSを先に実行する。対象DBD01のRECON1をDBDS登録とRECON可用性として記録する。続いてLIST.DBDS DBD(DBD01)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. LIST.RECON STATUSが応答を返した時点で正常とする。応答中のRECON1の値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: CはRECON状態で RECON1 を読みDBDS登録とRECON可用性の主値として通常状態を確定しDBD01に残します。
背景・仕組み: 通常状態の確認ではDBDS登録を補助操作としRECONリカバリ管理の基準値と現在値の差をDBDS01と対象DBD01で照合します。
選択肢の理由: RECON状態とDBDS登録の役割を分けるとA: DBDS01はRECON1を代替しないうえに追加前提も不正な点でRECONリカバリ管理に使えません、B: SLDS1とRECON1は確認項目が異なる点でDBD01を採用できません、C: RECON1を主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではDBDS登録とRECON可用性を判定できない点で一次資料と一致しません。結論として通常状態の確認のリカバリ管理・登録と可用性で判定する対象は DBD01 です。
用語の初出定義: 通常状態の確認で使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 通常状態の確認 DBD01</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について通常状態を確定し、DBD01のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD01のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD01)を指定し、DBD01のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD01)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD01 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD01のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECON1 が画面・出力に表示されること
② ステップ2 の DBDS01 が画面・出力に表示されること
③ ステップ3 の SLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0049"><h3>DBRC/RECON RECONリカバリ管理 障害切り分け DBD04</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>障害切り分けでは DBRC/RECON（リカバリ管理・登録と可用性） の RECON状態 を主操作として DBD04 を判定します。最初に失敗した処理への注意として「RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります」を DBD04 に残します。障害切り分けを補助する DBDS登録 では DBDS01 を補助値として DBD04 へ保存します。主判定の障害切り分けではリカバリ管理・登録と可用性の RECON状態 から RECON1 を読み DBD04 へ残します。証跡照合の障害切り分けではリカバリ管理・登録と可用性の RECON1 と DBDS01 を DBD04 に保存します。記録対応の障害切り分けではリカバリ管理・登録と可用性の DBDS登録とRECON可用性 の証跡へ DBD04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで DBRC/RECON の RECON状態 と DBDS登録 を実施し RECONリカバリ管理 の役割を確認します。RECON世代やDBDS登録の読み違いは復旧入力の欠落につながります。対象 DBD04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. LIST.LOG ALLのSLDS1をRECON1と同義の成功表示として扱う。LIST.RECON STATUSは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. LIST.RECON STATUSの出力でDBD04とRECON1が同じ応答にあることを確認する。DBDS登録とRECON可用性をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. LIST.RECON STATUSが応答を返した時点で正常とする。応答中のRECON1の値は記録しない。</li><li>D. LIST.RECON STATUSのコマンド文字列だけを記録する。RECON1を含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: BはRECON状態で RECON1 を読みDBDS登録とRECON可用性の主値として障害範囲を限定しDBD04に残します。
技術的背景: 障害切り分けではDBDS登録を補助操作としRECONリカバリ管理の最初に失敗した処理をDBDS01と対象DBD04で照合します。
四択の評価: RECON状態とDBDS登録の役割を分けるとA: SLDS1とRECON1は確認項目が異なるうえに追加前提も不正な点でDBD04を採用できません、B: DBD04とRECON1を同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではDBDS登録とRECON可用性を判定できない点で一次資料と一致しません、D: 入力記録だけではDBDS登録とRECON可用性を証明できない点でDBDS登録とRECON可用性を確認できません。結論として障害切り分けのリカバリ管理・登録と可用性で判定する対象は DBD04 です。
初出語の意味: 障害切り分けで使う RECONリカバリ管理 はDBDS、ログ、イメージコピー、変更累積の世代をRECONデータセットへ登録するDBRCの管理機能を表しDBDS登録とRECON可用性を判定する際にDBD04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC/RECON RECONリカバリ管理 障害切り分け DBD04</strong></p><p>検証目的: DBRC/RECONのRECONリカバリ管理について障害範囲を限定し、DBD04のDBDS登録とRECON可用性を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DBD04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.RECON STATUSを指定し、DBD04のRECON状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力にあるRECON1を読み、DBDS登録とRECON可用性と対象DBD04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(DBD04)を指定し、DBD04のDBDS登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD04)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD04 DD=DBDS01 RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力にあるDBDS01を読み、DBDS登録とRECON可用性と対象DBD04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のDBRC/RECONを確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、DBD04のログ登録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力にあるSLDS1を読み、DBDS登録とRECON可用性と対象DBD04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECON1 が画面・出力に表示されること
② ステップ2 の DBDS01 が画面・出力に表示されること
③ ステップ3 の SLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0050"><h3>DFS4452I 出力項目確認 除外条件</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 上級</p><p>IMS 15.5 の DBRC/RECON で扱う「DFS4452I 出力項目確認 除外条件」は、IMSplex資源クリーンアップの開始または完了を示すIMSメッセージを出力項目確認の観点で確認する技術項目です。RECON 欄とUTIL088を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS4452I 出力項目確認 除外条件</strong></p><p>検証目的: DBRC/RECONにおけるDFS4452Iの出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL088</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB088)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM088,PSB088,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB088
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0051"><h3>DFS4452I 戻りコード確認 ページング状態</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>IMS 15.5 の DBRC/RECON で扱う「DFS4452I 戻りコード確認 ページング状態」は、IMSplex資源クリーンアップの開始または完了を示すIMSメッセージを戻りコード確認の観点で確認する技術項目です。RECON 欄とUTIL028を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS4452I 戻りコード確認 ページング状態</strong></p><p>検証目的: DBRC/RECONにおけるDFS4452Iの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL028</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB028)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM028,PSB028,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB028
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0052"><h3>DFSPREC0 登録確認 登録状態</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>IMS 15.5 の DBRC/RECON で扱う「DFSPREC0 登録確認 登録状態」は、HALDB索引やILDSを再作成して整合性を戻すIMSユーティリティを登録確認の観点で確認する技術項目です。RECON 欄とAREA4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSPREC0 登録確認 登録状態</strong></p><p>検証目的: DBRC/RECONにおけるDFSPREC0の登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0053"><h3>DFSUICP0 戻りコード確認 実行結果</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>IMS 15.5 の DBRC/RECON で扱う「DFSUICP0 戻りコード確認 実行結果」は、オンライン環境で更新可能性を考慮しながらイメージコピーを取得するBMP型ユーティリティを戻りコード確認の観点で確認する技術項目です。RECON 欄とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUICP0 戻りコード確認 実行結果</strong></p><p>検証目的: DBRC/RECONにおけるDFSUICP0の戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD076
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD076
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD076
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD076 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0054"><h3>DFSUICP0 整合確認 対象ファイル</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 初級</p><p>IMS 15.5 の DBRC/RECON で扱う「DFSUICP0 整合確認 対象ファイル」は、オンライン環境で更新可能性を考慮しながらイメージコピーを取得するBMP型ユーティリティを整合確認の観点で確認する技術項目です。RECON 欄とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUICP0 整合確認 対象ファイル</strong></p><p>検証目的: DBRC/RECONにおけるDFSUICP0の整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD016
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD016
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD016
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD016 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0055"><h3>UPDATE IMSCON TYPE(ODBM) 状態確認 出力比較</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 中級</p><p>IMS 15.5 の DBRC/RECON で扱う「UPDATE IMSCON TYPE(ODBM) 状態確認 出力比較」は、IMS ConnectとODBMの通信開始または停止を行うタイプ2コマンドを状態確認の観点で確認する技術項目です。RECON 欄とPAY040を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPDATE IMSCON TYPE(ODBM) 状態確認 出力比較</strong></p><p>検証目的: DBRC/RECONにおけるUPDATE IMSCON TYPE(ODBM)の状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY040</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY040) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY040&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD040) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD040&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA8) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA8&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0056"><h3>UPDATE IMSCON TYPE(ODBM) 登録確認 キュー状態</h3><p class="kb-meta">分類: DBRC/RECON ・ 難易度: 上級</p><p>IMS 15.5 の DBRC/RECON で扱う「UPDATE IMSCON TYPE(ODBM) 登録確認 キュー状態」は、IMS ConnectとODBMの通信開始または停止を行うタイプ2コマンドを登録確認の観点で確認する技術項目です。RECON 欄とPAY100を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPDATE IMSCON TYPE(ODBM) 登録確認 キュー状態</strong></p><p>検証目的: DBRC/RECONにおけるUPDATE IMSCON TYPE(ODBM)の登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY100</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY100) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY100&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD100) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD100&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA4) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA4&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


## HALDB


<section class="kb-item" id="c16-i0057"><h3>/CHECKPOINT PURGE 戻りコード確認 実行順序</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>IMS 15.5 の HALDB で扱う「/CHECKPOINT PURGE 戻りコード確認 実行順序」は、DBCTLでBMP完了を待つ停止系チェックポイント操作を戻りコード確認の観点で確認する技術項目です。PSB 名とODBM2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT PURGE 戻りコード確認 実行順序</strong></p><p>検証目的: HALDBにおける/CHECKPOINT PURGEの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD066
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD066
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD066
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD066 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0058"><h3>/CHECKPOINT PURGE 整合確認 実行結果</h3><p class="kb-meta">分類: HALDB ・ 難易度: 初級</p><p>IMS 15.5 の HALDB で扱う「/CHECKPOINT PURGE 整合確認 実行結果」は、DBCTLでBMP完了を待つ停止系チェックポイント操作を整合確認の観点で確認する技術項目です。PSB 名とODBM2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT PURGE 整合確認 実行結果</strong></p><p>検証目的: HALDBにおける/CHECKPOINT PURGEの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD006
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD006
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD006
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD006 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0059"><h3>DBD catalog reference 登録確認 運用記録</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>IMS 15.5 の HALDB で扱う「DBD catalog reference 登録確認 運用記録」は、IMS管理ACB環境でDBRCがIMSカタログ上のアクティブDBDを参照する仕組みを登録確認の観点で確認する技術項目です。PSB 名とAREA2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD catalog reference 登録確認 運用記録</strong></p><p>検証目的: HALDBにおけるDBD catalog referenceの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0060"><h3>DFS680I リカバリ確認 待機状態</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>IMS 15.5 の HALDB で扱う「DFS680I リカバリ確認 待機状態」は、再始動で使用するチェックポイントを示すIMSメッセージをリカバリ確認の観点で確認する技術項目です。PSB 名とRECON3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS680I リカバリ確認 待機状態</strong></p><p>検証目的: HALDBにおけるDFS680Iのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON3</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO054&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM2&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM2) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM2  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM2&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0061"><h3>DFSURDB0 出力項目確認 障害記録</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>IMS 15.5 の HALDB で扱う「DFSURDB0 出力項目確認 障害記録」は、イメージコピーと変更累積、ログを使ってDBDSを復旧するIMSユーティリティを出力項目確認の観点で確認する技術項目です。PSB 名とUTIL078を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURDB0 出力項目確認 障害記録</strong></p><p>検証目的: HALDBにおけるDFSURDB0の出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL078</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB078)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM078,PSB078,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB078
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0062"><h3>DFSURDB0 戻りコード確認 除外条件</h3><p class="kb-meta">分類: HALDB ・ 難易度: 初級</p><p>IMS 15.5 の HALDB で扱う「DFSURDB0 戻りコード確認 除外条件」は、イメージコピーと変更累積、ログを使ってDBDSを復旧するIMSユーティリティを戻りコード確認の観点で確認する技術項目です。PSB 名とUTIL018を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURDB0 戻りコード確認 除外条件</strong></p><p>検証目的: HALDBにおけるDFSURDB0の戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL018</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB018)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM018,PSB018,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB018
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0063"><h3>HALDB HALDB区画管理 ログとの照合 PART07</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>ログとの照合では HALDB（区画管理・区画状態と整合） の 区画表示 を主操作として PART07 を判定します。時刻と対象識別子への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART07 に残します。ログとの照合を補助する 区画DBDS では PARTITION=PART を補助値として PART07 へ保存します。主判定のログとの照合では区画管理・区画状態と整合の 区画表示 から PARTITION を読み PART07 へ残します。証跡照合のログとの照合では区画管理・区画状態と整合の PARTITION と PARTITION=PART を PART07 に保存します。記録対応のログとの照合では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で HALDB の 区画表示 と 区画DBDS を使い 操作とログを対応 します。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。PARTITION を読み対象 PART07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. PARTITIONを含む区画表示の応答行を保存する。その応答を得るため/DISPLAY DB PART07を使用する。対象PART07の区画状態とILDS整合として記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. /DISPLAY DB PART07が応答を返した時点で正常とする。応答中のPARTITIONの値は記録しない。DFSPREC0をPARTITIONと同じ判定値とみなし対象PART07の主証跡にする。</li><li>C. /DISPLAY DB PART07のコマンド文字列だけを記録する。PARTITIONを含む応答行は保存しない。</li><li>D. HALDB区画管理の停止または再定義を実施する。その後に/DISPLAY DB PART07でPARTITIONを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aは区画表示で PARTITION を読み区画状態とILDS整合の主値として操作とログを対応しPART07に残します。
機能の仕組み: ログとの照合では区画DBDSを補助操作としHALDB区画管理の時刻と対象識別子をPARTITION=PARTと対象PART07で照合します。
各候補の評価: 区画表示と区画DBDSの役割を分けるとA: PARTITIONの実値を対象別に残す点で主証跡になります、B: 応答の有無だけでは区画状態とILDS整合を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけでは区画状態とILDS整合を証明できない点で区画状態とILDS整合を確認できません、D: 変更前の区画状態とILDS整合を失う点で区画DBDSの範囲を越えます。結論としてログとの照合の区画管理・区画状態と整合で判定する対象は PART07 です。
用語の定義: ログとの照合で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 ログとの照合 PART07</strong></p><p>検証目的: HALDBのHALDB区画管理について操作とログを対応し、PART07の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART07を指定し、PART07の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART07
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART07 PARTITION PART07 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART07) DDN(PART07)を指定し、PART07の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART07) DDN(PART07)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART07 PARTITION=PART07
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART07の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART07 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION が画面・出力に表示されること
② ステップ2 の PARTITION=PART が画面・出力に表示されること
③ ステップ3 の DFSPREC0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0064"><h3>HALDB HALDB区画管理 代替経路の確認 PART10</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>代替経路の確認では HALDB（区画管理・区画状態と整合） の 区画表示 を主操作として PART10 を判定します。主経路との役割差への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART10 に残します。代替経路の確認を補助する 区画DBDS では PARTITION=PART を補助値として PART10 へ保存します。主判定の代替経路の確認では区画管理・区画状態と整合の 区画表示 から PARTITION を読み PART10 へ残します。証跡照合の代替経路の確認では区画管理・区画状態と整合の PARTITION と PARTITION=PART を PART10 に保存します。記録対応の代替経路の確認では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で HALDB の 区画表示 と 区画DBDS を照合し 主経路との役割差 を確かめます。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。PARTITION を読む前に対象 PART10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY DB PART10のコマンド文字列だけを記録する。PARTITIONを含む応答行は保存しない。</li><li>B. HALDB区画管理の停止または再定義を実施する。その後に/DISPLAY DB PART10でPARTITIONを採取する。</li><li>C. DB/DC運用のSTATUSとQUEUEを確認する。その値をHALDBのPART10にも適用する。</li><li>D. /DISPLAY DB PART10とLIST.DBDS DBD(PART10) DDN(PART10)の対象名をそろえる。前者のPARTITIONを区画状態とILDS整合の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dは区画表示で PARTITION を読み区画状態とILDS整合の主値として代替手段の成立を確認しPART10に残します。
運用上の背景: 代替経路の確認では区画DBDSを補助操作としHALDB区画管理の主経路との役割差をPARTITION=PARTと対象PART10で照合します。
候補別の検討: 区画表示と区画DBDSの役割を分けるとA: 入力記録だけでは区画状態とILDS整合を証明できない点で一次資料と一致しません、B: 変更前の区画状態とILDS整合を失う点で区画状態とILDS整合を確認できません、C: DB/DC運用の値ではPARTITIONを確認できない点で区画DBDSの範囲を越えます、D: 同じ対象名のPARTITIONを採用する点で現在値を示します。結論として代替経路の確認の区画管理・区画状態と整合で判定する対象は PART10 です。
重要用語の定義: 代替経路の確認で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 代替経路の確認 PART10</strong></p><p>検証目的: HALDBのHALDB区画管理について代替手段の成立を確認し、PART10の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART10を指定し、PART10の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART10
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART10 PARTITION PART10 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART10) DDN(PART10)を指定し、PART10の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART10) DDN(PART10)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART10 PARTITION=PART10
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART10の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART10 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION が画面・出力に表示されること
② ステップ2 の PARTITION=PART が画面・出力に表示されること
③ ステップ3 の DFSPREC0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0065"><h3>HALDB HALDB区画管理 変更前の確認 PART02</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>変更前の確認では HALDB（区画管理・区画状態と整合） の 区画DBDS を主操作として PART02 を判定します。変更対象と非対象の境界への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART02 に残します。変更前の確認を補助する 索引再作成結果 では DFSPREC0 を補助値として PART02 へ保存します。主判定の変更前の確認では区画管理・区画状態と整合の 区画DBDS から PARTITION=PART を読み PART02 へ残します。証跡照合の変更前の確認では区画管理・区画状態と整合の PARTITION=PART と DFSPREC0 を PART02 に保存します。記録対応の変更前の確認では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で HALDB の 区画DBDS と 索引再作成結果 を実施し HALDB区画管理 の役割を確認します。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。対象 PART02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. LIST.DBDS DBD(PART02) DDN(PART02)を対象名なしで実行する。一覧の先頭行をPART02の結果として記録する。</li><li>B. 前回保存したLIST.DBDS DBD(PART02) DDN(PART02)の結果を使う。今回のSUBMIT IMS.DFSPREC0.CNTL(REBUILD)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのPART02の出力を再利用する。今回のLIST.DBDS DBD(PART02) DDN(PART02)とSUBMIT IMS.DFSPREC0.CNTL(REBUILD)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象PART02についてLIST.DBDS DBD(PART02) DDN(PART02)の応答からPARTITION=PARTを確認する。SUBMIT IMS.DFSPREC0.CNTL(REBUILD)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは区画DBDSで PARTITION=PART を読み区画状態とILDS整合の主値として変更前の証跡を保存しPART02に残します。
動作の背景: 変更前の確認では索引再作成結果を補助操作としHALDB区画管理の変更対象と非対象の境界をDFSPREC0と対象PART02で照合します。
各選択肢の検討: 区画DBDSと索引再作成結果の役割を分けるとA: 先頭行はPART02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で区画DBDSを代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でHALDBに使いません、D: PARTITION=PARTと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の区画管理・区画状態と整合で判定する対象は PART02 です。
初出用語の定義: 変更前の確認で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 変更前の確認 PART02</strong></p><p>検証目的: HALDBのHALDB区画管理について変更前の証跡を保存し、PART02の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART02) DDN(PART02)を指定し、PART02の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART02) DDN(PART02)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART02 PARTITION=PART02
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART02の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART02 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART02を指定し、PART02の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART02
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART02 PARTITION PART02 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION=PART が画面・出力に表示されること
② ステップ2 の DFSPREC0 が画面・出力に表示されること
③ ステップ3 の PARTITION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0066"><h3>HALDB HALDB区画管理 変更後の確認 PART03</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>変更後の確認では HALDB（区画管理・区画状態と整合） の 索引再作成結果 を主操作として PART03 を判定します。反映値と残存値への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART03 に残します。変更後の確認を補助する 区画表示 では PARTITION を補助値として PART03 へ保存します。主判定の変更後の確認では区画管理・区画状態と整合の 索引再作成結果 から DFSPREC0 を読み PART03 へ残します。証跡照合の変更後の確認では区画管理・区画状態と整合の DFSPREC0 と PARTITION を PART03 に保存します。記録対応の変更後の確認では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で HALDB の 索引再作成結果 と 区画表示 を用い 変更結果を検証 します。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。DFSPREC0 で対象 PART03 の 区画状態とILDS整合 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY DB PART03で周辺状態を押さえる。その後にSUBMIT IMS.DFSPREC0.CNTL(REBUILD)でDFSPREC0を確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. HALDB区画管理の停止または再定義を実施する。その後にSUBMIT IMS.DFSPREC0.CNTL(REBUILD)でDFSPREC0を採取する。</li><li>C. HALDBの区画状態とILDS整合を確認する。その値をHALDBのPART03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。HALDB区画管理の反映値と残存値は確認済みとして扱う。さらにLIST.DBDS DBD(PART03) DDN(PART03)のPARTITION=PARTをDFSPREC0と同種の値として併記する。</li><li>D. /DISPLAY DB PART03が成功したためSUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0も正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aは索引再作成結果で DFSPREC0 を読み区画状態とILDS整合の主値として変更結果を検証しPART03に残します。
内部の仕組み: 変更後の確認では区画表示を補助操作としHALDB区画管理の反映値と残存値をPARTITIONと対象PART03で照合します。
誤答を含む比較: 索引再作成結果と区画表示の役割を分けるとA: 周辺状態の後にDFSPREC0を確認する点でPART03を判定できます、B: 変更前の区画状態とILDS整合を失う点で区画表示の範囲を越えます、C: HALDBの値ではDFSPREC0を確認できないうえに追加前提も不正な点でPART03の値を示しません、D: 補助操作の成功ではDFSPREC0を確定できない点で変更後の確認に合いません。結論として変更後の確認の区画管理・区画状態と整合で判定する対象は PART03 です。
用語定義: 変更後の確認で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 変更後の確認 PART03</strong></p><p>検証目的: HALDBのHALDB区画管理について変更結果を検証し、PART03の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART03の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART03 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART03を指定し、PART03の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART03
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART03 PARTITION PART03 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART03) DDN(PART03)を指定し、PART03の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART03) DDN(PART03)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART03 PARTITION=PART03
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSPREC0 が画面・出力に表示されること
② ステップ2 の PARTITION が画面・出力に表示されること
③ ステップ3 の PARTITION=PART が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0067"><h3>HALDB HALDB区画管理 引継ぎ記録 PART09</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>引継ぎ記録では HALDB（区画管理・区画状態と整合） の 索引再作成結果 を主操作として PART09 を判定します。次担当者が追跡できる証跡への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART09 に残します。引継ぎ記録を補助する 区画表示 では PARTITION を補助値として PART09 へ保存します。主判定の引継ぎ記録では区画管理・区画状態と整合の 索引再作成結果 から DFSPREC0 を読み PART09 へ残します。証跡照合の引継ぎ記録では区画管理・区画状態と整合の DFSPREC0 と PARTITION を PART09 に保存します。記録対応の引継ぎ記録では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で HALDB の 索引再作成結果 と 区画表示 を用い 再現可能な記録を作成 します。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。DFSPREC0 で対象 PART09 の 区画状態とILDS整合 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY DB PART09が成功したためSUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0も正常だと推定する。主出力は保存しない。</li><li>B. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)を対象名なしで実行する。一覧の先頭行をPART09の結果として記録する。</li><li>C. 対象名PART09を指定してSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を実行する。応答中のDFSPREC0と時刻を保存する。/DISPLAY DB PART09で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSUBMIT IMS.DFSPREC0.CNTL(REBUILD)の結果を使う。今回の/DISPLAY DB PART09の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cは索引再作成結果で DFSPREC0 を読み区画状態とILDS整合の主値として再現可能な記録を作成しPART09に残します。
製品内の仕組み: 引継ぎ記録では区画表示を補助操作としHALDB区画管理の次担当者が追跡できる証跡をPARTITIONと対象PART09で照合します。
選択肢別の説明: 索引再作成結果と区画表示の役割を分けるとA: 補助操作の成功ではDFSPREC0を確定できない点でPART09の値を示しません、B: 先頭行はPART09と確定できない点で引継ぎ記録に合いません、C: DFSPREC0と時刻を保存する点で索引再作成結果に合います、D: 採取時刻が異なる点でHALDBに使いません。結論として引継ぎ記録の区画管理・区画状態と整合で判定する対象は PART09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 引継ぎ記録 PART09</strong></p><p>検証目的: HALDBのHALDB区画管理について再現可能な記録を作成し、PART09の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART09の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART09 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART09を指定し、PART09の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART09
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART09 PARTITION PART09 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART09) DDN(PART09)を指定し、PART09の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART09) DDN(PART09)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART09 PARTITION=PART09
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSPREC0 が画面・出力に表示されること
② ステップ2 の PARTITION が画面・出力に表示されること
③ ステップ3 の PARTITION=PART が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0068"><h3>HALDB HALDB区画管理 復旧後の確認 PART06</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>復旧後の確認では HALDB（区画管理・区画状態と整合） の 索引再作成結果 を主操作として PART06 を判定します。再発していないことを示す値への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART06 に残します。復旧後の確認を補助する 区画表示 では PARTITION を補助値として PART06 へ保存します。主判定の復旧後の確認では区画管理・区画状態と整合の 索引再作成結果 から DFSPREC0 を読み PART06 へ残します。証跡照合の復旧後の確認では区画管理・区画状態と整合の DFSPREC0 と PARTITION を PART06 に保存します。記録対応の復旧後の確認では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で HALDB の 索引再作成結果 と 区画表示 の役割を分け 再発していないことを示す値 を調べます。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。対象 PART06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. ODBM/OMのALIASと到達状態を確認する。その値をHALDBのPART06にも適用する。</li><li>B. /DISPLAY DB PART06が成功したためSUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0も正常だと推定する。主出力は保存しない。別資源で得た状態を対象PART06へ引き継げるものとする。HALDB区画管理の再発していないことを示す値は確認済みとして扱う。さらにLIST.DBDS DBD(PART06) DDN(PART06)のPARTITION=PARTをDFSPREC0と同種の値として併記する。</li><li>C. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)を対象名なしで実行する。一覧の先頭行をPART06の結果として記録する。</li><li>D. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)でDFSPREC0を取得してからLIST.DBDS DBD(PART06) DDN(PART06)でPARTITION=PARTを照合する。PART06の区画状態とILDS整合を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dは索引再作成結果で DFSPREC0 を読み区画状態とILDS整合の主値として復旧後の安定性を確認しPART06に残します。
構成上の背景: 復旧後の確認では区画表示を補助操作としHALDB区画管理の再発していないことを示す値をPARTITIONと対象PART06で照合します。
候補ごとの理由: 索引再作成結果と区画表示の役割を分けるとA: ODBM/OMの値ではDFSPREC0を確認できない点で区画表示の範囲を越えます、B: 補助操作の成功ではDFSPREC0を確定できないうえに追加前提も不正な点でPART06の値を示しません、C: 先頭行はPART06と確定できない点で復旧後の確認に合いません、D: DFSPREC0とPARTITION=PARTを順に照合する点で索引再作成結果に合います。結論として復旧後の確認の区画管理・区画状態と整合で判定する対象は PART06 です。
初出用語: 復旧後の確認で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 復旧後の確認 PART06</strong></p><p>検証目的: HALDBのHALDB区画管理について復旧後の安定性を確認し、PART06の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART06の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART06 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART06を指定し、PART06の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART06
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART06 PARTITION PART06 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART06) DDN(PART06)を指定し、PART06の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART06) DDN(PART06)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART06 PARTITION=PART06
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSPREC0 が画面・出力に表示されること
② ステップ2 の PARTITION が画面・出力に表示されること
③ ステップ3 の PARTITION=PART が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0069"><h3>HALDB HALDB区画管理 復旧準備 PART05</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>復旧準備では HALDB（区画管理・区画状態と整合） の 区画DBDS を主操作として PART05 を判定します。再開前に必要な整合性への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART05 に残します。復旧準備を補助する 索引再作成結果 では DFSPREC0 を補助値として PART05 へ保存します。主判定の復旧準備では区画管理・区画状態と整合の 区画DBDS から PARTITION=PART を読み PART05 へ残します。証跡照合の復旧準備では区画管理・区画状態と整合の PARTITION=PART と DFSPREC0 を PART05 に保存します。記録対応の復旧準備では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で HALDB の 区画DBDS と 索引再作成結果 を組み合わせる際は HALDB区画管理 が大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式という仕組みを前提にします。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。PARTITION=PART と 区画状態とILDS整合 を対象 PART05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 前回保存したLIST.DBDS DBD(PART05) DDN(PART05)の結果を使う。今回のSUBMIT IMS.DFSPREC0.CNTL(REBUILD)の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのPART05の出力を再利用する。今回のLIST.DBDS DBD(PART05) DDN(PART05)とSUBMIT IMS.DFSPREC0.CNTL(REBUILD)は実行済みとして扱う。</li><li>C. 変更を加えずLIST.DBDS DBD(PART05) DDN(PART05)を実行する。PARTITION=PARTを保存する。差分はSUBMIT IMS.DFSPREC0.CNTL(REBUILD)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0を区画状態とILDS整合の主判定に採用する。LIST.DBDS DBD(PART05) DDN(PART05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは区画DBDSで PARTITION=PART を読み区画状態とILDS整合の主値として復旧条件を確認しPART05に残します。
処理の仕組み: 復旧準備では索引再作成結果を補助操作としHALDB区画管理の再開前に必要な整合性をDFSPREC0と対象PART05で照合します。
選択結果の内訳: 区画DBDSと索引再作成結果の役割を分けるとA: 採取時刻が異なる点で区画DBDSを代替しません、B: 過去出力では今回の復旧準備を示せない点でHALDBに使いません、C: 変更前のPARTITION=PARTを保存する点で正答です、D: DFSPREC0はPARTITION=PARTを代替しないうえに追加前提も不正な点でPART05を採用できません。結論として復旧準備の区画管理・区画状態と整合で判定する対象は PART05 です。
用語の説明: 復旧準備で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 復旧準備 PART05</strong></p><p>検証目的: HALDBのHALDB区画管理について復旧条件を確認し、PART05の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART05) DDN(PART05)を指定し、PART05の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART05) DDN(PART05)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART05 PARTITION=PART05
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART05の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART05 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART05を指定し、PART05の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART05
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART05 PARTITION PART05 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION=PART が画面・出力に表示されること
② ステップ2 の DFSPREC0 が画面・出力に表示されること
③ ステップ3 の PARTITION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0070"><h3>HALDB HALDB区画管理 構成監査 PART08</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>構成監査では HALDB（区画管理・区画状態と整合） の 区画DBDS を主操作として PART08 を判定します。定義値と稼働値の一致への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART08 に残します。構成監査を補助する 索引再作成結果 では DFSPREC0 を補助値として PART08 へ保存します。主判定の構成監査では区画管理・区画状態と整合の 区画DBDS から PARTITION=PART を読み PART08 へ残します。証跡照合の構成監査では区画管理・区画状態と整合の PARTITION=PART と DFSPREC0 を PART08 に保存します。記録対応の構成監査では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で HALDB の 区画DBDS と 索引再作成結果 を実施し HALDB区画管理 の役割を確認します。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。対象 PART08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのPART08の出力を再利用する。今回のLIST.DBDS DBD(PART08) DDN(PART08)とSUBMIT IMS.DFSPREC0.CNTL(REBUILD)は実行済みとして扱う。</li><li>B. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)の結果だけでは確定しない。LIST.DBDS DBD(PART08) DDN(PART08)のPARTITION=PARTを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0を区画状態とILDS整合の主判定に採用する。LIST.DBDS DBD(PART08) DDN(PART08)の応答は採取対象から外す。</li><li>D. /DISPLAY DB PART08のPARTITIONをPARTITION=PARTと同義の成功表示として扱う。LIST.DBDS DBD(PART08) DDN(PART08)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bは区画DBDSで PARTITION=PART を読み区画状態とILDS整合の主値として構成差分を監査しPART08に残します。
実行時の背景: 構成監査では索引再作成結果を補助操作としHALDB区画管理の定義値と稼働値の一致をDFSPREC0と対象PART08で照合します。
四つの候補の理由: 区画DBDSと索引再作成結果の役割を分けるとA: 過去出力では今回の構成監査を示せない点でHALDBに使いません、B: PARTITION=PARTを主証跡として区別する点で正答です、C: DFSPREC0はPARTITION=PARTを代替しない点でPART08を採用できません、D: PARTITIONとPARTITION=PARTは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の区画管理・区画状態と整合で判定する対象は PART08 です。
初出語定義: 構成監査で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 構成監査 PART08</strong></p><p>検証目的: HALDBのHALDB区画管理について構成差分を監査し、PART08の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART08) DDN(PART08)を指定し、PART08の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART08) DDN(PART08)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART08 PARTITION=PART08
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART08の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART08 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART08を指定し、PART08の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART08
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART08 PARTITION PART08 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION=PART が画面・出力に表示されること
② ステップ2 の DFSPREC0 が画面・出力に表示されること
③ ステップ3 の PARTITION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0071"><h3>HALDB HALDB区画管理 通常状態の確認 PART01</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>通常状態の確認では HALDB（区画管理・区画状態と整合） の 区画表示 を主操作として PART01 を判定します。基準値と現在値の差への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART01 に残します。通常状態の確認を補助する 区画DBDS では PARTITION=PART を補助値として PART01 へ保存します。主判定の通常状態の確認では区画管理・区画状態と整合の 区画表示 から PARTITION を読み PART01 へ残します。証跡照合の通常状態の確認では区画管理・区画状態と整合の PARTITION と PARTITION=PART を PART01 に保存します。記録対応の通常状態の確認では区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で HALDB の 区画表示 と 区画DBDS を使い 通常状態を確定 します。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。PARTITION を読み対象 PART01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. LIST.DBDS DBD(PART01) DDN(PART01)のPARTITION=PARTを区画状態とILDS整合の主判定に採用する。/DISPLAY DB PART01の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0をPARTITIONと同義の成功表示として扱う。/DISPLAY DB PART01は実行しない。</li><li>C. /DISPLAY DB PART01を先に実行する。対象PART01のPARTITIONを区画状態とILDS整合として記録する。続いてLIST.DBDS DBD(PART01) DDN(PART01)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. /DISPLAY DB PART01が応答を返した時点で正常とする。応答中のPARTITIONの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cは区画表示で PARTITION を読み区画状態とILDS整合の主値として通常状態を確定しPART01に残します。
背景・仕組み: 通常状態の確認では区画DBDSを補助操作としHALDB区画管理の基準値と現在値の差をPARTITION=PARTと対象PART01で照合します。
選択肢の理由: 区画表示と区画DBDSの役割を分けるとA: PARTITION=PARTはPARTITIONを代替しないうえに追加前提も不正な点でHALDB区画管理に使えません、B: DFSPREC0とPARTITIONは確認項目が異なる点でPART01を採用できません、C: PARTITIONを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけでは区画状態とILDS整合を判定できない点で一次資料と一致しません。結論として通常状態の確認の区画管理・区画状態と整合で判定する対象は PART01 です。
用語の初出定義: 通常状態の確認で使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 通常状態の確認 PART01</strong></p><p>検証目的: HALDBのHALDB区画管理について通常状態を確定し、PART01の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART01を指定し、PART01の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART01
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART01 PARTITION PART01 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART01) DDN(PART01)を指定し、PART01の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART01) DDN(PART01)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART01 PARTITION=PART01
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART01の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART01 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION が画面・出力に表示されること
② ステップ2 の PARTITION=PART が画面・出力に表示されること
③ ステップ3 の DFSPREC0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0072"><h3>HALDB HALDB区画管理 障害切り分け PART04</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>障害切り分けでは HALDB（区画管理・区画状態と整合） の 区画表示 を主操作として PART04 を判定します。最初に失敗した処理への注意として「区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります」を PART04 に残します。障害切り分けを補助する 区画DBDS では PARTITION=PART を補助値として PART04 へ保存します。主判定の障害切り分けでは区画管理・区画状態と整合の 区画表示 から PARTITION を読み PART04 へ残します。証跡照合の障害切り分けでは区画管理・区画状態と整合の PARTITION と PARTITION=PART を PART04 に保存します。記録対応の障害切り分けでは区画管理・区画状態と整合の 区画状態とILDS整合 の証跡へ PART04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで HALDB の 区画表示 と 区画DBDS を照合し 最初に失敗した処理 を確かめます。HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式です。区画単位の停止や索引不整合をデータベース全体の状態と取り違える危険があります。PARTITION を読む前に対象 PART04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSPREC0.CNTL(REBUILD)のDFSPREC0をPARTITIONと同義の成功表示として扱う。/DISPLAY DB PART04は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. /DISPLAY DB PART04の出力でPART04とPARTITIONが同じ応答にあることを確認する。区画状態とILDS整合をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY DB PART04が応答を返した時点で正常とする。応答中のPARTITIONの値は記録しない。</li><li>D. /DISPLAY DB PART04のコマンド文字列だけを記録する。PARTITIONを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bは区画表示で PARTITION を読み区画状態とILDS整合の主値として障害範囲を限定しPART04に残します。
技術的背景: 障害切り分けでは区画DBDSを補助操作としHALDB区画管理の最初に失敗した処理をPARTITION=PARTと対象PART04で照合します。
四択の評価: 区画表示と区画DBDSの役割を分けるとA: DFSPREC0とPARTITIONは確認項目が異なるうえに追加前提も不正な点でPART04を採用できません、B: PART04とPARTITIONを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけでは区画状態とILDS整合を判定できない点で一次資料と一致しません、D: 入力記録だけでは区画状態とILDS整合を証明できない点で区画状態とILDS整合を確認できません。結論として障害切り分けの区画管理・区画状態と整合で判定する対象は PART04 です。
初出語の意味: 障害切り分けで使う HALDB区画管理 は大規模データベースを区画へ分割し、区画ごとに可用性とリカバリ入力を管理するIMSデータベース方式を表し区画状態とILDS整合を判定する際にPART04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALDB HALDB区画管理 障害切り分け PART04</strong></p><p>検証目的: HALDBのHALDB区画管理について障害範囲を限定し、PART04の区画状態とILDS整合を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象PART04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へ/DISPLAY DB PART04を指定し、PART04の区画表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY DB PART04
→ Enter を押す
［画面・出力］
DFS000I DATABASE PART04 PARTITION PART04 ACCESS UPDATES ALLOWED
画面・出力にあるPARTITIONを読み、区画状態とILDS整合と対象PART04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へLIST.DBDS DBD(PART04) DDN(PART04)を指定し、PART04の区画DBDSを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.DBDS DBD(PART04) DDN(PART04)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=PART04 PARTITION=PART04
IMAGE COPY NEEDED: NO
画面・出力にあるPARTITION=PARTを読み、区画状態とILDS整合と対象PART04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のHALDBを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSPREC0.CNTL(REBUILD)を指定し、PART04の索引再作成結果を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSPREC0.CNTL(REBUILD)
→ Enter を押す
［画面・出力］
DFSPREC0 HALDB INDEX ILDS REBUILD
PARTITION PART04 COMPLETE
RETURN CODE = 0000
画面・出力にあるDFSPREC0を読み、区画状態とILDS整合と対象PART04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARTITION が画面・出力に表示されること
② ステップ2 の PARTITION=PART が画面・出力に表示されること
③ ステップ3 の DFSPREC0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0073"><h3>MINVERS 再始動確認 受信先</h3><p class="kb-meta">分類: HALDB ・ 難易度: 上級</p><p>IMS 15.5 の HALDB で扱う「MINVERS 再始動確認 受信先」は、RECONデータセットで下位版戻し時のアクセス可否に影響する最小版数値を再始動確認の観点で確認する技術項目です。PSB 名とPAY090を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MINVERS 再始動確認 受信先</strong></p><p>検証目的: HALDBにおけるMINVERSの再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY090</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY090) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY090&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD090) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD090&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA2) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA2&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0074"><h3>MINVERS 出力項目確認 キュー状態</h3><p class="kb-meta">分類: HALDB ・ 難易度: 中級</p><p>IMS 15.5 の HALDB で扱う「MINVERS 出力項目確認 キュー状態」は、RECONデータセットで下位版戻し時のアクセス可否に影響する最小版数値を出力項目確認の観点で確認する技術項目です。PSB 名とPAY030を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MINVERS 出力項目確認 キュー状態</strong></p><p>検証目的: HALDBにおけるMINVERSの出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY030</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY030) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY030&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD030) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD030&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA6) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA6&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


## IMS Connect


<section class="kb-item" id="c16-i0075"><h3>/DISPLAY DATABASE リカバリ確認 再開位置</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 上級</p><p>IMS 15.5 の IMS Connect で扱う「/DISPLAY DATABASE リカバリ確認 再開位置」は、データベースまたはDBDの登録状態とアクセス状態を表示するIMSコマンドをリカバリ確認の観点で確認する技術項目です。RC 欄とAREA4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY DATABASE リカバリ確認 再開位置</strong></p><p>検証目的: IMS Connectにおける/DISPLAY DATABASEのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0076"><h3>/DISPLAY DATABASE 登録確認 製品レベル</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>IMS 15.5 の IMS Connect で扱う「/DISPLAY DATABASE 登録確認 製品レベル」は、データベースまたはDBDの登録状態とアクセス状態を表示するIMSコマンドを登録確認の観点で確認する技術項目です。RC 欄とAREA8を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY DATABASE 登録確認 製品レベル</strong></p><p>検証目的: IMS Connectにおける/DISPLAY DATABASEの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA8</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0077"><h3>/ERESTART CHKPT 出力項目確認 戻りコード</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>IMS 15.5 の IMS Connect で扱う「/ERESTART CHKPT 出力項目確認 戻りコード」は、異常終了後に指定チェックポイントから緊急再始動するIMSコマンドを出力項目確認の観点で確認する技術項目です。RC 欄とUTIL068を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/ERESTART CHKPT 出力項目確認 戻りコード</strong></p><p>検証目的: IMS Connectにおける/ERESTART CHKPTの出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL068</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB068)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM068,PSB068,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB068
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0078"><h3>/ERESTART CHKPT 戻りコード確認 障害記録</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 初級</p><p>IMS 15.5 の IMS Connect で扱う「/ERESTART CHKPT 戻りコード確認 障害記録」は、異常終了後に指定チェックポイントから緊急再始動するIMSコマンドを戻りコード確認の観点で確認する技術項目です。RC 欄とUTIL008を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/ERESTART CHKPT 戻りコード確認 障害記録</strong></p><p>検証目的: IMS Connectにおける/ERESTART CHKPTの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL008</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB008)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM008,PSB008,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB008
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0079"><h3>DFS3499I 接続確認 処理範囲</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>IMS 15.5 の IMS Connect で扱う「DFS3499I 接続確認 処理範囲」は、再始動関連のアクティブDD名を示すIMSメッセージを接続確認の観点で確認する技術項目です。RC 欄とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS3499I 接続確認 処理範囲</strong></p><p>検証目的: IMS ConnectにおけるDFS3499Iの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD056
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD056
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD056
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD056 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0080"><h3>DFSURGL0 再始動確認 保存場所</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>IMS 15.5 の IMS Connect で扱う「DFSURGL0 再始動確認 保存場所」は、HD Reorganization ReloadでアンロードデータからDBを再ロードするIMSユーティリティを再始動確認の観点で確認する技術項目です。RC 欄とPAY080を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURGL0 再始動確認 保存場所</strong></p><p>検証目的: IMS ConnectにおけるDFSURGL0の再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY080</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY080) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY080&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD080) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD080&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA8) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA8&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0081"><h3>DFSURGL0 出力項目確認 受信先</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>IMS 15.5 の IMS Connect で扱う「DFSURGL0 出力項目確認 受信先」は、HD Reorganization ReloadでアンロードデータからDBを再ロードするIMSユーティリティを出力項目確認の観点で確認する技術項目です。RC 欄とPAY020を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURGL0 出力項目確認 受信先</strong></p><p>検証目的: IMS ConnectにおけるDFSURGL0の出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY020</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY020) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY020&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD020) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD020&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA4) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA4&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0082"><h3>IMS Connect IMS Connect接続状態 ログとの照合 HWS07</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>ログとの照合では IMS Connect（接続状態・ポートと接続先メンバー） の 起動完了 を主操作として HWS07 を判定します。時刻と対象識別子への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS07 に残します。ログとの照合を補助する 接続先照会 では IMSCON を補助値として HWS07 へ保存します。主判定のログとの照合では接続状態・ポートと接続先メンバーの 起動完了 から HWSC0010I を読み HWS07 へ残します。証跡照合のログとの照合では接続状態・ポートと接続先メンバーの HWSC0010I と IMSCON を HWS07 に保存します。記録対応のログとの照合では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で IMS Connect の 起動完了 と 接続先照会 を用い 操作とログを対応 します。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。HWSC0010I で対象 HWS07 の ポートと接続先メンバー を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. HWSC0010Iを含む起動完了の応答行を保存する。その応答を得るためF HWS07,VIEWPORT ALLを使用する。対象HWS07のポートと接続先メンバーとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. F HWS07,VIEWPORT ALLが応答を返した時点で正常とする。応答中のHWSC0010Iの値は記録しない。asttをHWSC0010Iと同じ判定値とみなし対象HWS07の主証跡にする。</li><li>C. F HWS07,VIEWPORT ALLのコマンド文字列だけを記録する。HWSC0010Iを含む応答行は保存しない。</li><li>D. IMS Connect接続状態の停止または再定義を実施する。その後にF HWS07,VIEWPORT ALLでHWSC0010Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aは起動完了で HWSC0010I を読みポートと接続先メンバーの主値として操作とログを対応しHWS07に残します。
機能の仕組み: ログとの照合では接続先照会を補助操作としIMS Connect接続状態の時刻と対象識別子をIMSCONと対象HWS07で照合します。
各候補の評価: 起動完了と接続先照会の役割を分けるとA: HWSC0010Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではポートと接続先メンバーを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではポートと接続先メンバーを証明できない点でポートと接続先メンバーを確認できません、D: 変更前のポートと接続先メンバーを失う点で接続先照会の範囲を越えます。結論としてログとの照合の接続状態・ポートと接続先メンバーで判定する対象は HWS07 です。
用語の定義: ログとの照合で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 ログとの照合 HWS07</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について操作とログを対応し、HWS07のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS07,VIEWPORT ALLを指定し、HWS07の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS07,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS07
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS07の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS07&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS07のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS07&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSC0010I が画面・出力に表示されること
② ステップ2 の IMSCON が画面・出力に表示されること
③ ステップ3 の astt が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0083"><h3>IMS Connect IMS Connect接続状態 代替経路の確認 HWS10</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>代替経路の確認では IMS Connect（接続状態・ポートと接続先メンバー） の 起動完了 を主操作として HWS10 を判定します。主経路との役割差への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS10 に残します。代替経路の確認を補助する 接続先照会 では IMSCON を補助値として HWS10 へ保存します。主判定の代替経路の確認では接続状態・ポートと接続先メンバーの 起動完了 から HWSC0010I を読み HWS10 へ残します。証跡照合の代替経路の確認では接続状態・ポートと接続先メンバーの HWSC0010I と IMSCON を HWS10 に保存します。記録対応の代替経路の確認では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で IMS Connect の 起動完了 と 接続先照会 の役割を分け 主経路との役割差 を調べます。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。対象 HWS10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. F HWS10,VIEWPORT ALLのコマンド文字列だけを記録する。HWSC0010Iを含む応答行は保存しない。</li><li>B. IMS Connect接続状態の停止または再定義を実施する。その後にF HWS10,VIEWPORT ALLでHWSC0010Iを採取する。</li><li>C. ODBM/OMのALIASと到達状態を確認する。その値をIMS ConnectのHWS10にも適用する。</li><li>D. F HWS10,VIEWPORT ALLとQUERY IMSCON SHOW(ALL)の対象名をそろえる。前者のHWSC0010Iをポートと接続先メンバーの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dは起動完了で HWSC0010I を読みポートと接続先メンバーの主値として代替手段の成立を確認しHWS10に残します。
運用上の背景: 代替経路の確認では接続先照会を補助操作としIMS Connect接続状態の主経路との役割差をIMSCONと対象HWS10で照合します。
候補別の検討: 起動完了と接続先照会の役割を分けるとA: 入力記録だけではポートと接続先メンバーを証明できない点で一次資料と一致しません、B: 変更前のポートと接続先メンバーを失う点でポートと接続先メンバーを確認できません、C: ODBM/OMの値ではHWSC0010Iを確認できない点で接続先照会の範囲を越えます、D: 同じ対象名のHWSC0010Iを採用する点で現在値を示します。結論として代替経路の確認の接続状態・ポートと接続先メンバーで判定する対象は HWS10 です。
重要用語の定義: 代替経路の確認で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 代替経路の確認 HWS10</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について代替手段の成立を確認し、HWS10のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS10,VIEWPORT ALLを指定し、HWS10の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS10,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS10
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS10の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS10&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS10のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS10&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSC0010I が画面・出力に表示されること
② ステップ2 の IMSCON が画面・出力に表示されること
③ ステップ3 の astt が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0084"><h3>IMS Connect IMS Connect接続状態 変更前の確認 HWS02</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>変更前の確認では IMS Connect（接続状態・ポートと接続先メンバー） の 接続先照会 を主操作として HWS02 を判定します。変更対象と非対象の境界への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS02 に残します。変更前の確認を補助する ODBM到達性 では astt を補助値として HWS02 へ保存します。主判定の変更前の確認では接続状態・ポートと接続先メンバーの 接続先照会 から IMSCON を読み HWS02 へ残します。証跡照合の変更前の確認では接続状態・ポートと接続先メンバーの IMSCON と astt を HWS02 に保存します。記録対応の変更前の確認では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で IMS Connect の 接続先照会 と ODBM到達性 を照合し 変更対象と非対象の境界 を確かめます。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。IMSCON を読む前に対象 HWS02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. QUERY IMSCON SHOW(ALL)を対象名なしで実行する。一覧の先頭行をHWS02の結果として記録する。</li><li>B. 前回保存したQUERY IMSCON SHOW(ALL)の結果を使う。今回のQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのHWS02の出力を再利用する。今回のQUERY IMSCON SHOW(ALL)とQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象HWS02についてQUERY IMSCON SHOW(ALL)の応答からIMSCONを確認する。QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは接続先照会で IMSCON を読みポートと接続先メンバーの主値として変更前の証跡を保存しHWS02に残します。
動作の背景: 変更前の確認ではODBM到達性を補助操作としIMS Connect接続状態の変更対象と非対象の境界をasttと対象HWS02で照合します。
各選択肢の検討: 接続先照会とODBM到達性の役割を分けるとA: 先頭行はHWS02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で接続先照会を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でIMS Connectに使いません、D: IMSCONと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の接続状態・ポートと接続先メンバーで判定する対象は HWS02 です。
初出用語の定義: 変更前の確認で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 変更前の確認 HWS02</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について変更前の証跡を保存し、HWS02のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS02の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS02&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS02のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS02&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS02,VIEWPORT ALLを指定し、HWS02の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS02,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS02
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSCON が画面・出力に表示されること
② ステップ2 の astt が画面・出力に表示されること
③ ステップ3 の HWSC0010I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0085"><h3>IMS Connect IMS Connect接続状態 変更後の確認 HWS03</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>変更後の確認では IMS Connect（接続状態・ポートと接続先メンバー） の ODBM到達性 を主操作として HWS03 を判定します。反映値と残存値への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS03 に残します。変更後の確認を補助する 起動完了 では HWSC0010I を補助値として HWS03 へ保存します。主判定の変更後の確認では接続状態・ポートと接続先メンバーの ODBM到達性 から astt を読み HWS03 へ残します。証跡照合の変更後の確認では接続状態・ポートと接続先メンバーの astt と HWSC0010I を HWS03 に保存します。記録対応の変更後の確認では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で IMS Connect の ODBM到達性 と 起動完了 を組み合わせる際は IMS Connect接続状態 がTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイという仕組みを前提にします。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。astt と ポートと接続先メンバー を対象 HWS03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. F HWS03,VIEWPORT ALLで周辺状態を押さえる。その後にQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)でasttを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. IMS Connect接続状態の停止または再定義を実施する。その後にQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)でasttを採取する。</li><li>C. チェックポイントのチェックポイント種別と時刻を確認する。その値をIMS ConnectのHWS03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IMS Connect接続状態の反映値と残存値は確認済みとして扱う。さらにQUERY IMSCON SHOW(ALL)のIMSCONをasttと同種の値として併記する。</li><li>D. F HWS03,VIEWPORT ALLが成功したためQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: AはODBM到達性で astt を読みポートと接続先メンバーの主値として変更結果を検証しHWS03に残します。
内部の仕組み: 変更後の確認では起動完了を補助操作としIMS Connect接続状態の反映値と残存値をHWSC0010Iと対象HWS03で照合します。
誤答を含む比較: ODBM到達性と起動完了の役割を分けるとA: 周辺状態の後にasttを確認する点でHWS03を判定できます、B: 変更前のポートと接続先メンバーを失う点で起動完了の範囲を越えます、C: チェックポイントの値ではasttを確認できないうえに追加前提も不正な点でHWS03の値を示しません、D: 補助操作の成功ではasttを確定できない点で変更後の確認に合いません。結論として変更後の確認の接続状態・ポートと接続先メンバーで判定する対象は HWS03 です。
用語定義: 変更後の確認で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 変更後の確認 HWS03</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について変更結果を検証し、HWS03のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS03のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS03&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS03,VIEWPORT ALLを指定し、HWS03の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS03,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS03
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS03の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS03&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の astt が画面・出力に表示されること
② ステップ2 の HWSC0010I が画面・出力に表示されること
③ ステップ3 の IMSCON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0086"><h3>IMS Connect IMS Connect接続状態 引継ぎ記録 HWS09</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>引継ぎ記録では IMS Connect（接続状態・ポートと接続先メンバー） の ODBM到達性 を主操作として HWS09 を判定します。次担当者が追跡できる証跡への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS09 に残します。引継ぎ記録を補助する 起動完了 では HWSC0010I を補助値として HWS09 へ保存します。主判定の引継ぎ記録では接続状態・ポートと接続先メンバーの ODBM到達性 から astt を読み HWS09 へ残します。証跡照合の引継ぎ記録では接続状態・ポートと接続先メンバーの astt と HWSC0010I を HWS09 に保存します。記録対応の引継ぎ記録では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で IMS Connect の ODBM到達性 と 起動完了 を組み合わせる際は IMS Connect接続状態 がTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイという仕組みを前提にします。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。astt と ポートと接続先メンバー を対象 HWS09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. F HWS09,VIEWPORT ALLが成功したためQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttも正常だと推定する。主出力は保存しない。</li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を対象名なしで実行する。一覧の先頭行をHWS09の結果として記録する。</li><li>C. 対象名HWS09を指定してQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を実行する。応答中のasttと時刻を保存する。F HWS09,VIEWPORT ALLで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の結果を使う。今回のF HWS09,VIEWPORT ALLの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: CはODBM到達性で astt を読みポートと接続先メンバーの主値として再現可能な記録を作成しHWS09に残します。
製品内の仕組み: 引継ぎ記録では起動完了を補助操作としIMS Connect接続状態の次担当者が追跡できる証跡をHWSC0010Iと対象HWS09で照合します。
選択肢別の説明: ODBM到達性と起動完了の役割を分けるとA: 補助操作の成功ではasttを確定できない点でHWS09の値を示しません、B: 先頭行はHWS09と確定できない点で引継ぎ記録に合いません、C: asttと時刻を保存する点でODBM到達性に合います、D: 採取時刻が異なる点でIMS Connectに使いません。結論として引継ぎ記録の接続状態・ポートと接続先メンバーで判定する対象は HWS09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 引継ぎ記録 HWS09</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について再現可能な記録を作成し、HWS09のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS09のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS09&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS09,VIEWPORT ALLを指定し、HWS09の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS09,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS09
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS09の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS09&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の astt が画面・出力に表示されること
② ステップ2 の HWSC0010I が画面・出力に表示されること
③ ステップ3 の IMSCON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0087"><h3>IMS Connect IMS Connect接続状態 復旧後の確認 HWS06</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>復旧後の確認では IMS Connect（接続状態・ポートと接続先メンバー） の ODBM到達性 を主操作として HWS06 を判定します。再発していないことを示す値への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS06 に残します。復旧後の確認を補助する 起動完了 では HWSC0010I を補助値として HWS06 へ保存します。主判定の復旧後の確認では接続状態・ポートと接続先メンバーの ODBM到達性 から astt を読み HWS06 へ残します。証跡照合の復旧後の確認では接続状態・ポートと接続先メンバーの astt と HWSC0010I を HWS06 に保存します。記録対応の復旧後の確認では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で IMS Connect の ODBM到達性 と 起動完了 を実施し IMS Connect接続状態 の役割を確認します。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。対象 HWS06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. DBD/PSB/ACBの定義名と有効版を確認する。その値をIMS ConnectのHWS06にも適用する。</li><li>B. F HWS06,VIEWPORT ALLが成功したためQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttも正常だと推定する。主出力は保存しない。別資源で得た状態を対象HWS06へ引き継げるものとする。</li><li>C. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を対象名なしで実行する。一覧の先頭行をHWS06の結果として記録する。</li><li>D. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)でasttを取得してからQUERY IMSCON SHOW(ALL)でIMSCONを照合する。HWS06のポートと接続先メンバーを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: DはODBM到達性で astt を読みポートと接続先メンバーの主値として復旧後の安定性を確認しHWS06に残します。
構成上の背景: 復旧後の確認では起動完了を補助操作としIMS Connect接続状態の再発していないことを示す値をHWSC0010Iと対象HWS06で照合します。
候補ごとの理由: ODBM到達性と起動完了の役割を分けるとA: DBD/PSB/ACBの値ではasttを確認できない点で起動完了の範囲を越えます、B: 補助操作の成功ではasttを確定できないうえに追加前提も不正な点でHWS06の値を示しません、C: 先頭行はHWS06と確定できない点で復旧後の確認に合いません、D: asttとIMSCONを順に照合する点でODBM到達性に合います。結論として復旧後の確認の接続状態・ポートと接続先メンバーで判定する対象は HWS06 です。
初出用語: 復旧後の確認で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 復旧後の確認 HWS06</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について復旧後の安定性を確認し、HWS06のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS06のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS06&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS06,VIEWPORT ALLを指定し、HWS06の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS06,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS06
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS06の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS06&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の astt が画面・出力に表示されること
② ステップ2 の HWSC0010I が画面・出力に表示されること
③ ステップ3 の IMSCON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0088"><h3>IMS Connect IMS Connect接続状態 復旧準備 HWS05</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>復旧準備では IMS Connect（接続状態・ポートと接続先メンバー） の 接続先照会 を主操作として HWS05 を判定します。再開前に必要な整合性への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS05 に残します。復旧準備を補助する ODBM到達性 では astt を補助値として HWS05 へ保存します。主判定の復旧準備では接続状態・ポートと接続先メンバーの 接続先照会 から IMSCON を読み HWS05 へ残します。証跡照合の復旧準備では接続状態・ポートと接続先メンバーの IMSCON と astt を HWS05 に保存します。記録対応の復旧準備では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で IMS Connect の 接続先照会 と ODBM到達性 を使い 復旧条件を確認 します。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。IMSCON を読み対象 HWS05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したQUERY IMSCON SHOW(ALL)の結果を使う。今回のQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのHWS05の出力を再利用する。今回のQUERY IMSCON SHOW(ALL)とQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)は実行済みとして扱う。</li><li>C. 変更を加えずQUERY IMSCON SHOW(ALL)を実行する。IMSCONを保存する。差分はQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttをポートと接続先メンバーの主判定に採用する。QUERY IMSCON SHOW(ALL)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは接続先照会で IMSCON を読みポートと接続先メンバーの主値として復旧条件を確認しHWS05に残します。
処理の仕組み: 復旧準備ではODBM到達性を補助操作としIMS Connect接続状態の再開前に必要な整合性をasttと対象HWS05で照合します。
選択結果の内訳: 接続先照会とODBM到達性の役割を分けるとA: 採取時刻が異なる点で接続先照会を代替しません、B: 過去出力では今回の復旧準備を示せない点でIMS Connectに使いません、C: 変更前のIMSCONを保存する点で正答です、D: asttはIMSCONを代替しないうえに追加前提も不正な点でHWS05を採用できません。結論として復旧準備の接続状態・ポートと接続先メンバーで判定する対象は HWS05 です。
用語の説明: 復旧準備で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 復旧準備 HWS05</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について復旧条件を確認し、HWS05のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS05の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS05&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS05のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS05&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS05,VIEWPORT ALLを指定し、HWS05の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS05,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS05
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSCON が画面・出力に表示されること
② ステップ2 の astt が画面・出力に表示されること
③ ステップ3 の HWSC0010I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0089"><h3>IMS Connect IMS Connect接続状態 構成監査 HWS08</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>構成監査では IMS Connect（接続状態・ポートと接続先メンバー） の 接続先照会 を主操作として HWS08 を判定します。定義値と稼働値の一致への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS08 に残します。構成監査を補助する ODBM到達性 では astt を補助値として HWS08 へ保存します。主判定の構成監査では接続状態・ポートと接続先メンバーの 接続先照会 から IMSCON を読み HWS08 へ残します。証跡照合の構成監査では接続状態・ポートと接続先メンバーの IMSCON と astt を HWS08 に保存します。記録対応の構成監査では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で IMS Connect の 接続先照会 と ODBM到達性 を照合し 定義値と稼働値の一致 を確かめます。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。IMSCON を読む前に対象 HWS08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのHWS08の出力を再利用する。今回のQUERY IMSCON SHOW(ALL)とQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)は実行済みとして扱う。</li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の結果だけでは確定しない。QUERY IMSCON SHOW(ALL)のIMSCONを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttをポートと接続先メンバーの主判定に採用する。QUERY IMSCON SHOW(ALL)の応答は採取対象から外す。</li><li>D. F HWS08,VIEWPORT ALLのHWSC0010IをIMSCONと同義の成功表示として扱う。QUERY IMSCON SHOW(ALL)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bは接続先照会で IMSCON を読みポートと接続先メンバーの主値として構成差分を監査しHWS08に残します。
実行時の背景: 構成監査ではODBM到達性を補助操作としIMS Connect接続状態の定義値と稼働値の一致をasttと対象HWS08で照合します。
四つの候補の理由: 接続先照会とODBM到達性の役割を分けるとA: 過去出力では今回の構成監査を示せない点でIMS Connectに使いません、B: IMSCONを主証跡として区別する点で正答です、C: asttはIMSCONを代替しない点でHWS08を採用できません、D: HWSC0010IとIMSCONは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の接続状態・ポートと接続先メンバーで判定する対象は HWS08 です。
初出語定義: 構成監査で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 構成監査 HWS08</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について構成差分を監査し、HWS08のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS08の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS08&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS08のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS08&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS08,VIEWPORT ALLを指定し、HWS08の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS08,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS08
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSCON が画面・出力に表示されること
② ステップ2 の astt が画面・出力に表示されること
③ ステップ3 の HWSC0010I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0090"><h3>IMS Connect IMS Connect接続状態 通常状態の確認 HWS01</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>通常状態の確認では IMS Connect（接続状態・ポートと接続先メンバー） の 起動完了 を主操作として HWS01 を判定します。基準値と現在値の差への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS01 に残します。通常状態の確認を補助する 接続先照会 では IMSCON を補助値として HWS01 へ保存します。主判定の通常状態の確認では接続状態・ポートと接続先メンバーの 起動完了 から HWSC0010I を読み HWS01 へ残します。証跡照合の通常状態の確認では接続状態・ポートと接続先メンバーの HWSC0010I と IMSCON を HWS01 に保存します。記録対応の通常状態の確認では接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で IMS Connect の 起動完了 と 接続先照会 を用い 通常状態を確定 します。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。HWSC0010I で対象 HWS01 の ポートと接続先メンバー を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. QUERY IMSCON SHOW(ALL)のIMSCONをポートと接続先メンバーの主判定に採用する。F HWS01,VIEWPORT ALLの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttをHWSC0010Iと同義の成功表示として扱う。F HWS01,VIEWPORT ALLは実行しない。</li><li>C. F HWS01,VIEWPORT ALLを先に実行する。対象HWS01のHWSC0010Iをポートと接続先メンバーとして記録する。続いてQUERY IMSCON SHOW(ALL)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. F HWS01,VIEWPORT ALLが応答を返した時点で正常とする。応答中のHWSC0010Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cは起動完了で HWSC0010I を読みポートと接続先メンバーの主値として通常状態を確定しHWS01に残します。
背景・仕組み: 通常状態の確認では接続先照会を補助操作としIMS Connect接続状態の基準値と現在値の差をIMSCONと対象HWS01で照合します。
選択肢の理由: 起動完了と接続先照会の役割を分けるとA: IMSCONはHWSC0010Iを代替しないうえに追加前提も不正な点でIMS Connect接続状態に使えません、B: asttとHWSC0010Iは確認項目が異なる点でHWS01を採用できません、C: HWSC0010Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではポートと接続先メンバーを判定できない点で一次資料と一致しません。結論として通常状態の確認の接続状態・ポートと接続先メンバーで判定する対象は HWS01 です。
用語の初出定義: 通常状態の確認で使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 通常状態の確認 HWS01</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について通常状態を確定し、HWS01のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS01,VIEWPORT ALLを指定し、HWS01の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS01,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS01
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS01の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS01&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS01のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS01&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSC0010I が画面・出力に表示されること
② ステップ2 の IMSCON が画面・出力に表示されること
③ ステップ3 の astt が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0091"><h3>IMS Connect IMS Connect接続状態 障害切り分け HWS04</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>障害切り分けでは IMS Connect（接続状態・ポートと接続先メンバー） の 起動完了 を主操作として HWS04 を判定します。最初に失敗した処理への注意として「接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります」を HWS04 に残します。障害切り分けを補助する 接続先照会 では IMSCON を補助値として HWS04 へ保存します。主判定の障害切り分けでは接続状態・ポートと接続先メンバーの 起動完了 から HWSC0010I を読み HWS04 へ残します。証跡照合の障害切り分けでは接続状態・ポートと接続先メンバーの HWSC0010I と IMSCON を HWS04 に保存します。記録対応の障害切り分けでは接続状態・ポートと接続先メンバーの ポートと接続先メンバー の証跡へ HWS04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで IMS Connect の 起動完了 と 接続先照会 の役割を分け 最初に失敗した処理 を調べます。IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイです。接続先IMSplexまたはSCI停止をポート障害だけと誤認する危険があります。対象 HWS04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のasttをHWSC0010Iと同義の成功表示として扱う。F HWS04,VIEWPORT ALLは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. F HWS04,VIEWPORT ALLの出力でHWS04とHWSC0010Iが同じ応答にあることを確認する。ポートと接続先メンバーをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. F HWS04,VIEWPORT ALLが応答を返した時点で正常とする。応答中のHWSC0010Iの値は記録しない。</li><li>D. F HWS04,VIEWPORT ALLのコマンド文字列だけを記録する。HWSC0010Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bは起動完了で HWSC0010I を読みポートと接続先メンバーの主値として障害範囲を限定しHWS04に残します。
技術的背景: 障害切り分けでは接続先照会を補助操作としIMS Connect接続状態の最初に失敗した処理をIMSCONと対象HWS04で照合します。
四択の評価: 起動完了と接続先照会の役割を分けるとA: asttとHWSC0010Iは確認項目が異なるうえに追加前提も不正な点でHWS04を採用できません、B: HWS04とHWSC0010Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではポートと接続先メンバーを判定できない点で一次資料と一致しません、D: 入力記録だけではポートと接続先メンバーを証明できない点でポートと接続先メンバーを確認できません。結論として障害切り分けの接続状態・ポートと接続先メンバーで判定する対象は HWS04 です。
初出語の意味: 障害切り分けで使う IMS Connect接続状態 はTCP/IPクライアント要求をIMSまたはODBMへ中継し、ポートと接続先を管理するIMSゲートウェイを表しポートと接続先メンバーを判定する際にHWS04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect IMS Connect接続状態 障害切り分け HWS04</strong></p><p>検証目的: IMS ConnectのIMS Connect接続状態について障害範囲を限定し、HWS04のポートと接続先メンバーを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象HWS04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へF HWS04,VIEWPORT ALLを指定し、HWS04の起動完了を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS04,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSC0010I WELCOME TO IMS CONNECT! ID=HWS04
PORTID=09999 STATUS=ACTIVE
画面・出力にあるHWSC0010Iを読み、ポートと接続先メンバーと対象HWS04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON SHOW(ALL)を指定し、HWS04の接続先照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS04&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;port&gt;09999&lt;/port&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるIMSCONを読み、ポートと接続先メンバーと対象HWS04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のIMS Connectを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、HWS04のODBM到達性を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS04&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;odbm&gt;ODBM1&lt;/odbm&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるasttを読み、ポートと接続先メンバーと対象HWS04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSC0010I が画面・出力に表示されること
② ステップ2 の IMSCON が画面・出力に表示されること
③ ステップ3 の astt が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0092"><h3>IMSLOGR DD リカバリ確認 監査証跡</h3><p class="kb-meta">分類: IMS Connect ・ 難易度: 中級</p><p>IMS 15.5 の IMS Connect で扱う「IMSLOGR DD リカバリ確認 監査証跡」は、再始動時にチェックポイント記録を読み取るログ入力DDをリカバリ確認の観点で確認する技術項目です。RC 欄とRECON2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMSLOGR DD リカバリ確認 監査証跡</strong></p><p>検証目的: IMS ConnectにおけるIMSLOGR DDのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO044&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM4&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM4) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM4  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM4&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


## ODBM/OM


<section class="kb-item" id="c16-i0093"><h3>/DISPLAY AREA ログ照合 エラー詳細</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>IMS 15.5 の ODBM/OM で扱う「/DISPLAY AREA ログ照合 エラー詳細」は、DEDBやHALDB関連の領域状態を確認するIMSコマンドをログ照合の観点で確認する技術項目です。IMSLOGR DDと82142/083220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY AREA ログ照合 エラー詳細</strong></p><p>検証目的: ODBM/OMにおける/DISPLAY AREAのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82142/083220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0094"><h3>/DISPLAY AREA 整合確認 サンプル採取</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 上級</p><p>IMS 15.5 の ODBM/OM で扱う「/DISPLAY AREA 整合確認 サンプル採取」は、DEDBやHALDB関連の領域状態を確認するIMSコマンドを整合確認の観点で確認する技術項目です。IMSLOGR DDと82132/083220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY AREA 整合確認 サンプル採取</strong></p><p>検証目的: ODBM/OMにおける/DISPLAY AREAの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82132/083220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0095"><h3>DFS3804I 戻りコード確認 世代管理</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>IMS 15.5 の ODBM/OM で扱う「DFS3804I 戻りコード確認 世代管理」は、最新Restart/BuildQチェックポイントを示すIMSメッセージを戻りコード確認の観点で確認する技術項目です。IMSLOGR DDとPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS3804I 戻りコード確認 世代管理</strong></p><p>検証目的: ODBM/OMにおけるDFS3804Iの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD057)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD057  DD=DBDS01  RECON=RECON3
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS3 ARCHIVED TO SLDS3
RLDS STATUS AVAILABLE
画面・出力には OLDS3 が含まれ、OLDS3を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS3 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0096"><h3>DFSBBO00 状態確認 保持設定</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>IMS 15.5 の ODBM/OM で扱う「DFSBBO00 状態確認 保持設定」は、動的バックアウト後のリカバリ条件に応じてBatch Backoutを行うIMSユーティリティを状態確認の観点で確認する技術項目です。IMSLOGR DDとDBD021を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSBBO00 状態確認 保持設定</strong></p><p>検証目的: ODBM/OMにおけるDFSBBO00の状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD021</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY021
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY021 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD021
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD021 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA5
→ Enter を押す
［画面・出力］
DFS000I AREA AREA5 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0097"><h3>DFSBBO00 登録確認 照合単位</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>IMS 15.5 の ODBM/OM で扱う「DFSBBO00 登録確認 照合単位」は、動的バックアウト後のリカバリ条件に応じてBatch Backoutを行うIMSユーティリティを登録確認の観点で確認する技術項目です。IMSLOGR DDとDBD081を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSBBO00 登録確認 照合単位</strong></p><p>検証目的: ODBM/OMにおけるDFSBBO00の登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD081</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY081
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY081 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD081
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD081 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA1
→ Enter を押す
［画面・出力］
DFS000I AREA AREA1 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0098"><h3>DFSUDMP0 整合確認 確認範囲</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>IMS 15.5 の ODBM/OM で扱う「DFSUDMP0 整合確認 確認範囲」は、Database Image Copyを作成してリカバリ入力を確保するIMSユーティリティを整合確認の観点で確認する技術項目です。IMSLOGR DDとOLDS3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUDMP0 整合確認 確認範囲</strong></p><p>検証目的: ODBM/OMにおけるDFSUDMP0の整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS3</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD045
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD045.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0099"><h3>ODBM/OM ODBM通信管理 ログとの照合 ODBM07</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>ログとの照合では ODBM/OM（通信管理・到達状態） の 別名照会 を主操作として ODBM07 を判定します。時刻と対象識別子への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM07 に残します。ログとの照合を補助する 通信開始 では successfully を補助値として ODBM07 へ保存します。主判定のログとの照合では通信管理・到達状態の 別名照会 から alias を読み ODBM07 へ残します。証跡照合のログとの照合では通信管理・到達状態の alias と successfully を ODBM07 に保存します。記録対応のログとの照合では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で ODBM/OM の 別名照会 と 通信開始 を使い 操作とログを対応 します。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。alias を読み対象 ODBM07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)が応答を返した時点で正常とする。応答中のaliasの値は記録しない。ODBMをaliasと同じ判定値とみなし対象ODBM07の主証跡にする。</li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のコマンド文字列だけを記録する。aliasを含む応答行は保存しない。</li><li>C. aliasを含む別名照会の応答行を保存する。その応答を得るためQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を使用する。対象ODBM07のALIASと到達状態として記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. ODBM通信管理の停止または再定義を実施する。その後にQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)でaliasを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Cは別名照会で alias を読みALIASと到達状態の主値として操作とログを対応しODBM07に残します。
機能の仕組み: ログとの照合では通信開始を補助操作としODBM通信管理の時刻と対象識別子をsuccessfullyと対象ODBM07で照合します。
各候補の評価: 別名照会と通信開始の役割を分けるとA: 応答の有無だけではALIASと到達状態を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではALIASと到達状態を証明できない点で一次資料と一致しません、C: aliasの実値を対象別に残す点でODBM07を判定できます、D: 変更前のALIASと到達状態を失う点で通信開始の範囲を越えます。結論としてログとの照合の通信管理・到達状態で判定する対象は ODBM07 です。
用語の定義: ログとの照合で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 ログとの照合 ODBM07</strong></p><p>検証目的: ODBM/OMのODBM通信管理について操作とログを対応し、ODBM07のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM07の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO07&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM07&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM07) START(COMM)を指定し、ODBM07の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM07) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM07 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM07) SHOW(ALL)を指定し、ODBM07のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM07) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM07&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の alias が画面・出力に表示されること
② ステップ2 の successfully が画面・出力に表示されること
③ ステップ3 の ODBM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0100"><h3>ODBM/OM ODBM通信管理 代替経路の確認 ODBM10</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>代替経路の確認では ODBM/OM（通信管理・到達状態） の 別名照会 を主操作として ODBM10 を判定します。主経路との役割差への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM10 に残します。代替経路の確認を補助する 通信開始 では successfully を補助値として ODBM10 へ保存します。主判定の代替経路の確認では通信管理・到達状態の 別名照会 から alias を読み ODBM10 へ残します。証跡照合の代替経路の確認では通信管理・到達状態の alias と successfully を ODBM10 に保存します。記録対応の代替経路の確認では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で ODBM/OM の 別名照会 と 通信開始 を照合し 主経路との役割差 を確かめます。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。alias を読む前に対象 ODBM10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のコマンド文字列だけを記録する。aliasを含む応答行は保存しない。</li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)とUPDATE IMSCON TYPE(ODBM) NAME(ODBM10) START(COMM)の対象名をそろえる。前者のaliasをALIASと到達状態の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. ODBM通信管理の停止または再定義を実施する。その後にQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)でaliasを採取する。</li><li>D. オンライン変更のIMPORT完了コードとメンバー反映を確認する。その値をODBM/OMのODBM10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Bは別名照会で alias を読みALIASと到達状態の主値として代替手段の成立を確認しODBM10に残します。
運用上の背景: 代替経路の確認では通信開始を補助操作としODBM通信管理の主経路との役割差をsuccessfullyと対象ODBM10で照合します。
候補別の検討: 別名照会と通信開始の役割を分けるとA: 入力記録だけではALIASと到達状態を証明できない点で一次資料と一致しません、B: 同じ対象名のaliasを採用する点でODBM10を判定できます、C: 変更前のALIASと到達状態を失う点で通信開始の範囲を越えます、D: オンライン変更の値ではaliasを確認できない点でODBM10の値を示しません。結論として代替経路の確認の通信管理・到達状態で判定する対象は ODBM10 です。
重要用語の定義: 代替経路の確認で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 代替経路の確認 ODBM10</strong></p><p>検証目的: ODBM/OMのODBM通信管理について代替手段の成立を確認し、ODBM10のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM10の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO10&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM10&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM10) START(COMM)を指定し、ODBM10の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM10) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM10 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM10) SHOW(ALL)を指定し、ODBM10のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM10) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM10&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の alias が画面・出力に表示されること
② ステップ2 の successfully が画面・出力に表示されること
③ ステップ3 の ODBM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0101"><h3>ODBM/OM ODBM通信管理 変更前の確認 ODBM02</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>変更前の確認では ODBM/OM（通信管理・到達状態） の 通信開始 を主操作として ODBM02 を判定します。変更対象と非対象の境界への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM02 に残します。変更前の確認を補助する ODBM状態 では ODBM を補助値として ODBM02 へ保存します。主判定の変更前の確認では通信管理・到達状態の 通信開始 から successfully を読み ODBM02 へ残します。証跡照合の変更前の確認では通信管理・到達状態の successfully と ODBM を ODBM02 に保存します。記録対応の変更前の確認では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で ODBM/OM の 通信開始 と ODBM状態 を実施し ODBM通信管理 の役割を確認します。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。対象 ODBM02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. UPDATE IMSCON TYPE(ODBM) NAME(ODBM02) START(COMM)を対象名なしで実行する。一覧の先頭行をODBM02の結果として記録する。</li><li>B. 対象ODBM02についてUPDATE IMSCON TYPE(ODBM) NAME(ODBM02) START(COMM)の応答からsuccessfullyを確認する。QUERY ODBM NAME(ODBM02) SHOW(ALL)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したUPDATE IMSCON TYPE(ODBM) NAME(ODBM02) START(COMM)の結果を使う。今回のQUERY ODBM NAME(ODBM02) SHOW(ALL)の結果と同一時点の証跡として比較する。</li><li>D. 保存済みのODBM02の出力を再利用する。今回のUPDATE IMSCON TYPE(ODBM) NAME(ODBM02) START(COMM)とQUERY ODBM NAME(ODBM02) SHOW(ALL)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bは通信開始で successfully を読みALIASと到達状態の主値として変更前の証跡を保存しODBM02に残します。
動作の背景: 変更前の確認ではODBM状態を補助操作としODBM通信管理の変更対象と非対象の境界をODBMと対象ODBM02で照合します。
各選択肢の検討: 通信開始とODBM状態の役割を分けるとA: 先頭行はODBM02と確定できない点で変更前の確認に合いません、B: successfullyと補助証跡の時刻を合わせる点で通信開始に合います、C: 採取時刻が異なる点でODBM/OMに使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でODBM通信管理に使えません。結論として変更前の確認の通信管理・到達状態で判定する対象は ODBM02 です。
初出用語の定義: 変更前の確認で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 変更前の確認 ODBM02</strong></p><p>検証目的: ODBM/OMのODBM通信管理について変更前の証跡を保存し、ODBM02のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM02) START(COMM)を指定し、ODBM02の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM02) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM02 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM02) SHOW(ALL)を指定し、ODBM02のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM02) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM02&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM02の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO02&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM02&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の successfully が画面・出力に表示されること
② ステップ2 の ODBM が画面・出力に表示されること
③ ステップ3 の alias が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0102"><h3>ODBM/OM ODBM通信管理 変更後の確認 ODBM03</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>変更後の確認では ODBM/OM（通信管理・到達状態） の ODBM状態 を主操作として ODBM03 を判定します。反映値と残存値への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM03 に残します。変更後の確認を補助する 別名照会 では alias を補助値として ODBM03 へ保存します。主判定の変更後の確認では通信管理・到達状態の ODBM状態 から ODBM を読み ODBM03 へ残します。証跡照合の変更後の確認では通信管理・到達状態の ODBM と alias を ODBM03 に保存します。記録対応の変更後の確認では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で ODBM/OM の ODBM状態 と 別名照会 を用い 変更結果を検証 します。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。ODBM で対象 ODBM03 の ALIASと到達状態 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. ODBM通信管理の停止または再定義を実施する。その後にQUERY ODBM NAME(ODBM03) SHOW(ALL)でODBMを採取する。</li><li>B. 障害診断のメッセージIDと理由コードを確認する。その値をODBM/OMのODBM03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。ODBM通信管理の反映値と残存値は確認済みとして扱う。さらにUPDATE IMSCON TYPE(ODBM) NAME(ODBM03) START(COMM)のsuccessfullyをODBMと同種の値として併記する。</li><li>C. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)で周辺状態を押さえる。その後にQUERY ODBM NAME(ODBM03) SHOW(ALL)でODBMを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)が成功したためQUERY ODBM NAME(ODBM03) SHOW(ALL)のODBMも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: CはODBM状態で ODBM を読みALIASと到達状態の主値として変更結果を検証しODBM03に残します。
内部の仕組み: 変更後の確認では別名照会を補助操作としODBM通信管理の反映値と残存値をaliasと対象ODBM03で照合します。
誤答を含む比較: ODBM状態と別名照会の役割を分けるとA: 変更前のALIASと到達状態を失う点でALIASと到達状態を確認できません、B: 障害診断の値ではODBMを確認できないうえに追加前提も不正な点で別名照会の範囲を越えます、C: 周辺状態の後にODBMを確認する点で現在値を示します、D: 補助操作の成功ではODBMを確定できない点で変更後の確認に合いません。結論として変更後の確認の通信管理・到達状態で判定する対象は ODBM03 です。
用語定義: 変更後の確認で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 変更後の確認 ODBM03</strong></p><p>検証目的: ODBM/OMのODBM通信管理について変更結果を検証し、ODBM03のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM03) SHOW(ALL)を指定し、ODBM03のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM03) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM03&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM03の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO03&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM03&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM03) START(COMM)を指定し、ODBM03の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM03) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM03 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ODBM が画面・出力に表示されること
② ステップ2 の alias が画面・出力に表示されること
③ ステップ3 の successfully が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0103"><h3>ODBM/OM ODBM通信管理 引継ぎ記録 ODBM09</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>引継ぎ記録では ODBM/OM（通信管理・到達状態） の ODBM状態 を主操作として ODBM09 を判定します。次担当者が追跡できる証跡への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM09 に残します。引継ぎ記録を補助する 別名照会 では alias を補助値として ODBM09 へ保存します。主判定の引継ぎ記録では通信管理・到達状態の ODBM状態 から ODBM を読み ODBM09 へ残します。証跡照合の引継ぎ記録では通信管理・到達状態の ODBM と alias を ODBM09 に保存します。記録対応の引継ぎ記録では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で ODBM/OM の ODBM状態 と 別名照会 を用い 再現可能な記録を作成 します。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。ODBM で対象 ODBM09 の ALIASと到達状態 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 対象名ODBM09を指定してQUERY ODBM NAME(ODBM09) SHOW(ALL)を実行する。応答中のODBMと時刻を保存する。QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)が成功したためQUERY ODBM NAME(ODBM09) SHOW(ALL)のODBMも正常だと推定する。主出力は保存しない。</li><li>C. QUERY ODBM NAME(ODBM09) SHOW(ALL)を対象名なしで実行する。一覧の先頭行をODBM09の結果として記録する。</li><li>D. 前回保存したQUERY ODBM NAME(ODBM09) SHOW(ALL)の結果を使う。今回のQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: AはODBM状態で ODBM を読みALIASと到達状態の主値として再現可能な記録を作成しODBM09に残します。
製品内の仕組み: 引継ぎ記録では別名照会を補助操作としODBM通信管理の次担当者が追跡できる証跡をaliasと対象ODBM09で照合します。
選択肢別の説明: ODBM状態と別名照会の役割を分けるとA: ODBMと時刻を保存する点で現在値を示します、B: 補助操作の成功ではODBMを確定できない点で引継ぎ記録に合いません、C: 先頭行はODBM09と確定できない点でODBM状態を代替しません、D: 採取時刻が異なる点でODBM/OMに使いません。結論として引継ぎ記録の通信管理・到達状態で判定する対象は ODBM09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 引継ぎ記録 ODBM09</strong></p><p>検証目的: ODBM/OMのODBM通信管理について再現可能な記録を作成し、ODBM09のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM09) SHOW(ALL)を指定し、ODBM09のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM09) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM09&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM09の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO09&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM09&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM09) START(COMM)を指定し、ODBM09の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM09) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM09 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ODBM が画面・出力に表示されること
② ステップ2 の alias が画面・出力に表示されること
③ ステップ3 の successfully が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0104"><h3>ODBM/OM ODBM通信管理 復旧後の確認 ODBM06</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>復旧後の確認では ODBM/OM（通信管理・到達状態） の ODBM状態 を主操作として ODBM06 を判定します。再発していないことを示す値への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM06 に残します。復旧後の確認を補助する 別名照会 では alias を補助値として ODBM06 へ保存します。主判定の復旧後の確認では通信管理・到達状態の ODBM状態 から ODBM を読み ODBM06 へ残します。証跡照合の復旧後の確認では通信管理・到達状態の ODBM と alias を ODBM06 に保存します。記録対応の復旧後の確認では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で ODBM/OM の ODBM状態 と 別名照会 の役割を分け 再発していないことを示す値 を調べます。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。対象 ODBM06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. リスタートの使用チェックポイントとBUILDQ結果を確認する。その値をODBM/OMのODBM06にも適用する。</li><li>B. QUERY ODBM NAME(ODBM06) SHOW(ALL)でODBMを取得してからUPDATE IMSCON TYPE(ODBM) NAME(ODBM06) START(COMM)でsuccessfullyを照合する。ODBM06のALIASと到達状態を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)が成功したためQUERY ODBM NAME(ODBM06) SHOW(ALL)のODBMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象ODBM06へ引き継げるものとする。ODBM通信管理の再発していないことを示す値は確認済みとして扱う。さらにUPDATE IMSCON TYPE(ODBM) NAME(ODBM06) START(COMM)のsuccessfullyをODBMと同種の値として併記する。</li><li>D. QUERY ODBM NAME(ODBM06) SHOW(ALL)を対象名なしで実行する。一覧の先頭行をODBM06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: BはODBM状態で ODBM を読みALIASと到達状態の主値として復旧後の安定性を確認しODBM06に残します。
構成上の背景: 復旧後の確認では別名照会を補助操作としODBM通信管理の再発していないことを示す値をaliasと対象ODBM06で照合します。
候補ごとの理由: ODBM状態と別名照会の役割を分けるとA: リスタートの値ではODBMを確認できない点で別名照会の範囲を越えます、B: ODBMとsuccessfullyを順に照合する点で現在値を示します、C: 補助操作の成功ではODBMを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はODBM06と確定できない点でODBM状態を代替しません。結論として復旧後の確認の通信管理・到達状態で判定する対象は ODBM06 です。
初出用語: 復旧後の確認で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 復旧後の確認 ODBM06</strong></p><p>検証目的: ODBM/OMのODBM通信管理について復旧後の安定性を確認し、ODBM06のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM06) SHOW(ALL)を指定し、ODBM06のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM06) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM06&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM06の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO06&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM06&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM06) START(COMM)を指定し、ODBM06の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM06) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM06 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ODBM が画面・出力に表示されること
② ステップ2 の alias が画面・出力に表示されること
③ ステップ3 の successfully が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0105"><h3>ODBM/OM ODBM通信管理 復旧準備 ODBM05</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>復旧準備では ODBM/OM（通信管理・到達状態） の 通信開始 を主操作として ODBM05 を判定します。再開前に必要な整合性への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM05 に残します。復旧準備を補助する ODBM状態 では ODBM を補助値として ODBM05 へ保存します。主判定の復旧準備では通信管理・到達状態の 通信開始 から successfully を読み ODBM05 へ残します。証跡照合の復旧準備では通信管理・到達状態の successfully と ODBM を ODBM05 に保存します。記録対応の復旧準備では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で ODBM/OM の 通信開始 と ODBM状態 を組み合わせる際は ODBM通信管理 がOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みという仕組みを前提にします。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。successfully と ALIASと到達状態 を対象 ODBM05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずUPDATE IMSCON TYPE(ODBM) NAME(ODBM05) START(COMM)を実行する。successfullyを保存する。差分はQUERY ODBM NAME(ODBM05) SHOW(ALL)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したUPDATE IMSCON TYPE(ODBM) NAME(ODBM05) START(COMM)の結果を使う。今回のQUERY ODBM NAME(ODBM05) SHOW(ALL)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのODBM05の出力を再利用する。今回のUPDATE IMSCON TYPE(ODBM) NAME(ODBM05) START(COMM)とQUERY ODBM NAME(ODBM05) SHOW(ALL)は実行済みとして扱う。</li><li>D. QUERY ODBM NAME(ODBM05) SHOW(ALL)のODBMをALIASと到達状態の主判定に採用する。UPDATE IMSCON TYPE(ODBM) NAME(ODBM05) START(COMM)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aは通信開始で successfully を読みALIASと到達状態の主値として復旧条件を確認しODBM05に残します。
処理の仕組み: 復旧準備ではODBM状態を補助操作としODBM通信管理の再開前に必要な整合性をODBMと対象ODBM05で照合します。
選択結果の内訳: 通信開始とODBM状態の役割を分けるとA: 変更前のsuccessfullyを保存する点で通信開始に合います、B: 採取時刻が異なる点でODBM/OMに使いません、C: 過去出力では今回の復旧準備を示せない点でODBM通信管理に使えません、D: ODBMはsuccessfullyを代替しないうえに追加前提も不正な点でODBM05を採用できません。結論として復旧準備の通信管理・到達状態で判定する対象は ODBM05 です。
用語の説明: 復旧準備で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 復旧準備 ODBM05</strong></p><p>検証目的: ODBM/OMのODBM通信管理について復旧条件を確認し、ODBM05のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM05) START(COMM)を指定し、ODBM05の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM05) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM05 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM05) SHOW(ALL)を指定し、ODBM05のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM05) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM05&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM05の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO05&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM05&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の successfully が画面・出力に表示されること
② ステップ2 の ODBM が画面・出力に表示されること
③ ステップ3 の alias が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0106"><h3>ODBM/OM ODBM通信管理 構成監査 ODBM08</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>構成監査では ODBM/OM（通信管理・到達状態） の 通信開始 を主操作として ODBM08 を判定します。定義値と稼働値の一致への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM08 に残します。構成監査を補助する ODBM状態 では ODBM を補助値として ODBM08 へ保存します。主判定の構成監査では通信管理・到達状態の 通信開始 から successfully を読み ODBM08 へ残します。証跡照合の構成監査では通信管理・到達状態の successfully と ODBM を ODBM08 に保存します。記録対応の構成監査では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で ODBM/OM の 通信開始 と ODBM状態 を実施し ODBM通信管理 の役割を確認します。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。対象 ODBM08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのODBM08の出力を再利用する。今回のUPDATE IMSCON TYPE(ODBM) NAME(ODBM08) START(COMM)とQUERY ODBM NAME(ODBM08) SHOW(ALL)は実行済みとして扱う。</li><li>B. QUERY ODBM NAME(ODBM08) SHOW(ALL)のODBMをALIASと到達状態の主判定に採用する。UPDATE IMSCON TYPE(ODBM) NAME(ODBM08) START(COMM)の応答は採取対象から外す。</li><li>C. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のaliasをsuccessfullyと同義の成功表示として扱う。UPDATE IMSCON TYPE(ODBM) NAME(ODBM08) START(COMM)は実行しない。</li><li>D. QUERY ODBM NAME(ODBM08) SHOW(ALL)の結果だけでは確定しない。UPDATE IMSCON TYPE(ODBM) NAME(ODBM08) START(COMM)のsuccessfullyを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dは通信開始で successfully を読みALIASと到達状態の主値として構成差分を監査しODBM08に残します。
実行時の背景: 構成監査ではODBM状態を補助操作としODBM通信管理の定義値と稼働値の一致をODBMと対象ODBM08で照合します。
四つの候補の理由: 通信開始とODBM状態の役割を分けるとA: 過去出力では今回の構成監査を示せない点でODBM/OMに使いません、B: ODBMはsuccessfullyを代替しない点でODBM通信管理に使えません、C: aliasとsuccessfullyは確認項目が異なる点でODBM08を採用できません、D: successfullyを主証跡として区別する点で主証跡になります。結論として構成監査の通信管理・到達状態で判定する対象は ODBM08 です。
初出語定義: 構成監査で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 構成監査 ODBM08</strong></p><p>検証目的: ODBM/OMのODBM通信管理について構成差分を監査し、ODBM08のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM08) START(COMM)を指定し、ODBM08の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM08) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM08 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM08) SHOW(ALL)を指定し、ODBM08のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM08) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM08&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM08の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO08&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM08&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の successfully が画面・出力に表示されること
② ステップ2 の ODBM が画面・出力に表示されること
③ ステップ3 の alias が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0107"><h3>ODBM/OM ODBM通信管理 通常状態の確認 ODBM01</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>通常状態の確認では ODBM/OM（通信管理・到達状態） の 別名照会 を主操作として ODBM01 を判定します。基準値と現在値の差への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM01 に残します。通常状態の確認を補助する 通信開始 では successfully を補助値として ODBM01 へ保存します。主判定の通常状態の確認では通信管理・到達状態の 別名照会 から alias を読み ODBM01 へ残します。証跡照合の通常状態の確認では通信管理・到達状態の alias と successfully を ODBM01 に保存します。記録対応の通常状態の確認では通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で ODBM/OM の 別名照会 と 通信開始 を使い 通常状態を確定 します。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。alias を読み対象 ODBM01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を先に実行する。対象ODBM01のaliasをALIASと到達状態として記録する。続いてUPDATE IMSCON TYPE(ODBM) NAME(ODBM01) START(COMM)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. UPDATE IMSCON TYPE(ODBM) NAME(ODBM01) START(COMM)のsuccessfullyをALIASと到達状態の主判定に採用する。QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. QUERY ODBM NAME(ODBM01) SHOW(ALL)のODBMをaliasと同義の成功表示として扱う。QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)は実行しない。</li><li>D. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)が応答を返した時点で正常とする。応答中のaliasの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Aは別名照会で alias を読みALIASと到達状態の主値として通常状態を確定しODBM01に残します。
背景・仕組み: 通常状態の確認では通信開始を補助操作としODBM通信管理の基準値と現在値の差をsuccessfullyと対象ODBM01で照合します。
選択肢の理由: 別名照会と通信開始の役割を分けるとA: aliasを主値として補助結果と照合する点で正答です、B: successfullyはaliasを代替しないうえに追加前提も不正な点でODBM01を採用できません、C: ODBMとaliasは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではALIASと到達状態を判定できない点で一次資料と一致しません。結論として通常状態の確認の通信管理・到達状態で判定する対象は ODBM01 です。
用語の初出定義: 通常状態の確認で使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 通常状態の確認 ODBM01</strong></p><p>検証目的: ODBM/OMのODBM通信管理について通常状態を確定し、ODBM01のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM01の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO01&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM01&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM01) START(COMM)を指定し、ODBM01の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM01) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM01 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM01) SHOW(ALL)を指定し、ODBM01のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM01) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM01&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の alias が画面・出力に表示されること
② ステップ2 の successfully が画面・出力に表示されること
③ ステップ3 の ODBM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0108"><h3>ODBM/OM ODBM通信管理 障害切り分け ODBM04</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>障害切り分けでは ODBM/OM（通信管理・到達状態） の 別名照会 を主操作として ODBM04 を判定します。最初に失敗した処理への注意として「SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります」を ODBM04 に残します。障害切り分けを補助する 通信開始 では successfully を補助値として ODBM04 へ保存します。主判定の障害切り分けでは通信管理・到達状態の 別名照会 から alias を読み ODBM04 へ残します。証跡照合の障害切り分けでは通信管理・到達状態の alias と successfully を ODBM04 に保存します。記録対応の障害切り分けでは通信管理・到達状態の ALIASと到達状態 の証跡へ ODBM04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで ODBM/OM の 別名照会 と 通信開始 を照合し 最初に失敗した処理 を確かめます。ODBM通信管理 はOM API経由でIMS ConnectとODBMの到達性を照会し、データベース要求の通信開始または停止を制御する仕組みです。SCI停止によるNOTREACHABLEをODBMプロセス停止と誤読する危険があります。alias を読む前に対象 ODBM04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. QUERY ODBM NAME(ODBM04) SHOW(ALL)のODBMをaliasと同義の成功表示として扱う。QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)が応答を返した時点で正常とする。応答中のaliasの値は記録しない。</li><li>C. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)のコマンド文字列だけを記録する。aliasを含む応答行は保存しない。</li><li>D. QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)の出力でODBM04とaliasが同じ応答にあることを確認する。ALIASと到達状態をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Dは別名照会で alias を読みALIASと到達状態の主値として障害範囲を限定しODBM04に残します。
技術的背景: 障害切り分けでは通信開始を補助操作としODBM通信管理の最初に失敗した処理をsuccessfullyと対象ODBM04で照合します。
四択の評価: 別名照会と通信開始の役割を分けるとA: ODBMとaliasは確認項目が異なるうえに追加前提も不正な点でODBM04を採用できません、B: 応答の有無だけではALIASと到達状態を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではALIASと到達状態を証明できない点で一次資料と一致しません、D: ODBM04とaliasを同じ応答で結ぶ点でODBM04を判定できます。結論として障害切り分けの通信管理・到達状態で判定する対象は ODBM04 です。
初出語の意味: 障害切り分けで使う ODBM通信管理 はODBM/OMでALIASと到達状態を扱う機能を表しALIASと到達状態を判定する際にODBM04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ODBM/OM ODBM通信管理 障害切り分け ODBM04</strong></p><p>検証目的: ODBM/OMのODBM通信管理について障害範囲を限定し、ODBM04のALIASと到達状態を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象ODBM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY IMSCON TYPE(ODBM) SHOW(ALIAS)を指定し、ODBM04の別名照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;HWS1&#x27;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO04&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM04&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaliasを読み、ALIASと到達状態と対象ODBM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へUPDATE IMSCON TYPE(ODBM) NAME(ODBM04) START(COMM)を指定し、ODBM04の通信開始を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM04) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM04 X&#x27;00000000&#x27; X&#x27;00000000&#x27;
画面・出力にあるsuccessfullyを読み、ALIASと到達状態と対象ODBM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のODBM/OMを確認する入力画面です。COMMAND入力口へQUERY ODBM NAME(ODBM04) SHOW(ALL)を指定し、ODBM04のODBM状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY ODBM NAME(ODBM04) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;ODBM04&#x27;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるODBMを読み、ALIASと到達状態と対象ODBM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の alias が画面・出力に表示されること
② ステップ2 の successfully が画面・出力に表示されること
③ ステップ3 の ODBM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0109"><h3>QUERY IMSCON TYPE(ODBM) 実行条件確認 出力見出し</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 初級</p><p>IMS 15.5 の ODBM/OM で扱う「QUERY IMSCON TYPE(ODBM) 実行条件確認 出力見出し」は、IMS ConnectからODBM接続、別名、到達状態を確認するタイプ2コマンドを実行条件確認の観点で確認する技術項目です。IMSLOGR DDとPSB009を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>QUERY IMSCON TYPE(ODBM) 実行条件確認 出力見出し</strong></p><p>検証目的: ODBM/OMにおけるQUERY IMSCON TYPE(ODBM)の実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB009</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD009) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD009 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0110"><h3>QUERY IMSCON TYPE(ODBM) 状態確認 理由コード</h3><p class="kb-meta">分類: ODBM/OM ・ 難易度: 中級</p><p>IMS 15.5 の ODBM/OM で扱う「QUERY IMSCON TYPE(ODBM) 状態確認 理由コード」は、IMS ConnectからODBM接続、別名、到達状態を確認するタイプ2コマンドを状態確認の観点で確認する技術項目です。IMSLOGR DDとPSB069を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>QUERY IMSCON TYPE(ODBM) 状態確認 理由コード</strong></p><p>検証目的: ODBM/OMにおけるQUERY IMSCON TYPE(ODBM)の状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB069</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD069) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD069 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


## オンライン変更


<section class="kb-item" id="c16-i0111"><h3>/DISPLAY TRANSACTION ログ照合 保持設定</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 上級</p><p>IMS 15.5 の オンライン変更 で扱う「/DISPLAY TRANSACTION ログ照合 保持設定」は、トランザクションの状態、キュー、処理可否を確認するIMSコマンドをログ照合の観点で確認する技術項目です。ALIAS 欄とDBD091を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY TRANSACTION ログ照合 保持設定</strong></p><p>検証目的: オンライン変更における/DISPLAY TRANSACTIONのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD091</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY091
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY091 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD091
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD091 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA3
→ Enter を押す
［画面・出力］
DFS000I AREA AREA3 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0112"><h3>/DISPLAY TRANSACTION 再始動確認 装置一覧</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>IMS 15.5 の オンライン変更 で扱う「/DISPLAY TRANSACTION 再始動確認 装置一覧」は、トランザクションの状態、キュー、処理可否を確認するIMSコマンドを再始動確認の観点で確認する技術項目です。ALIAS 欄とDBD031を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY TRANSACTION 再始動確認 装置一覧</strong></p><p>検証目的: オンライン変更における/DISPLAY TRANSACTIONの再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD031</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY031
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY031 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD031
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD031 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA7
→ Enter を押す
［画面・出力］
DFS000I AREA AREA7 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0113"><h3>/NRESTART BUILDQ 実行条件確認 完了コード</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>IMS 15.5 の オンライン変更 で扱う「/NRESTART BUILDQ 実行条件確認 完了コード」は、直近の停止チェックポイントから通常再始動し、キュー構築を行うIMSコマンドを実行条件確認の観点で確認する技術項目です。ALIAS 欄とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/NRESTART BUILDQ 実行条件確認 完了コード</strong></p><p>検証目的: オンライン変更における/NRESTART BUILDQの実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD067)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD067  DD=DBDS01  RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力には OLDS1 が含まれ、OLDS1を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0114"><h3>/NRESTART BUILDQ 接続確認 識別値</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 初級</p><p>IMS 15.5 の オンライン変更 で扱う「/NRESTART BUILDQ 接続確認 識別値」は、直近の停止チェックポイントから通常再始動し、キュー構築を行うIMSコマンドを接続確認の観点で確認する技術項目です。ALIAS 欄とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/NRESTART BUILDQ 接続確認 識別値</strong></p><p>検証目的: オンライン変更における/NRESTART BUILDQの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD007)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD007  DD=DBDS01  RECON=RECON1
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS1 ARCHIVED TO SLDS1
RLDS STATUS AVAILABLE
画面・出力には OLDS1 が含まれ、OLDS1を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS1 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0115"><h3>DFS994I 整合確認 接続状態</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>IMS 15.5 の オンライン変更 で扱う「DFS994I 整合確認 接続状態」は、チェックポイント番号と種別を表示するIMSメッセージを整合確認の観点で確認する技術項目です。ALIAS 欄とOLDS1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS994I 整合確認 接続状態</strong></p><p>検証目的: オンライン変更におけるDFS994Iの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD055
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD055.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0116"><h3>DFSURGU0 実行条件確認 イベント転送</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>IMS 15.5 の オンライン変更 で扱う「DFSURGU0 実行条件確認 イベント転送」は、HD Reorganization UnloadでフルファンクションDBをアンロードするIMSユーティリティを実行条件確認の観点で確認する技術項目です。ALIAS 欄とPSB019を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURGU0 実行条件確認 イベント転送</strong></p><p>検証目的: オンライン変更におけるDFSURGU0の実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB019</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD019) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD019 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0117"><h3>DFSURGU0 状態確認 出力見出し</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>IMS 15.5 の オンライン変更 で扱う「DFSURGU0 状態確認 出力見出し」は、HD Reorganization UnloadでフルファンクションDBをアンロードするIMSユーティリティを状態確認の観点で確認する技術項目です。ALIAS 欄とPSB079を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURGU0 状態確認 出力見出し</strong></p><p>検証目的: オンライン変更におけるDFSURGU0の状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB079</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD079) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD079 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0118"><h3>PSB checkpoint restart ログ照合 復旧手掛かり</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>IMS 15.5 の オンライン変更 で扱う「PSB checkpoint restart ログ照合 復旧手掛かり」は、BMPやバッチプログラムの再始動点をPSBとチェックポイントIDで管理する仕組みをログ照合の観点で確認する技術項目です。ALIAS 欄と82152/084220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PSB checkpoint restart ログ照合 復旧手掛かり</strong></p><p>検証目的: オンライン変更におけるPSB checkpoint restartのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82152/084220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0119"><h3>オンライン変更 IMSカタログ定義取込 ログとの照合 DEF07</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>ログとの照合では オンライン変更 の 定義取込 を主操作として DEF07 を判定します。時刻と対象識別子への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF07 に残します。ログとの照合を補助する メンバー状態 では status を補助値として DEF07 へ保存します。主判定のログとの照合ではオンライン変更・カタログ定義取込の 定義取込 から resource を読み DEF07 へ残します。証跡照合のログとの照合ではオンライン変更・カタログ定義取込の resource と status を DEF07 に保存します。記録対応のログとの照合ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で オンライン変更 の 定義取込 と メンバー状態 を組み合わせる際は IMSカタログ定義取込 がIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みという仕組みを前提にします。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。resource と IMPORT完了コードとメンバー反映 を対象 DEF07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. IMPORT DEFN SOURCE(CATALOG)が応答を返した時点で正常とする。応答中のresourceの値は記録しない。accessをresourceと同じ判定値とみなし対象DEF07の主証跡にする。</li><li>B. IMPORT DEFN SOURCE(CATALOG)のコマンド文字列だけを記録する。resourceを含む応答行は保存しない。</li><li>C. resourceを含む定義取込の応答行を保存する。その応答を得るためIMPORT DEFN SOURCE(CATALOG)を使用する。対象DEF07のIMPORT完了コードとメンバー反映として記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. IMSカタログ定義取込の停止または再定義を実施する。その後にIMPORT DEFN SOURCE(CATALOG)でresourceを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Cは定義取込で resource を読みIMPORT完了コードとメンバー反映の主値として操作とログを対応しDEF07に残します。
機能の仕組み: ログとの照合ではメンバー状態を補助操作としIMSカタログ定義取込の時刻と対象識別子をstatusと対象DEF07で照合します。
各候補の評価: 定義取込とメンバー状態の役割を分けるとA: 応答の有無だけではIMPORT完了コードとメンバー反映を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではIMPORT完了コードとメンバー反映を証明できない点で一次資料と一致しません、C: resourceの実値を対象別に残す点でDEF07を判定できます、D: 変更前のIMPORT完了コードとメンバー反映を失う点でメンバー状態の範囲を越えます。結論としてログとの照合のオンライン変更・カタログ定義取込で判定する対象は DEF07 です。
用語の定義: ログとの照合で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 ログとの照合 DEF07</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について操作とログを対応し、DEF07のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF07の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF07&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF07のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF07) SHOW(ALL)を指定し、DEF07の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF07) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF07&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の resource が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の access が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0120"><h3>オンライン変更 IMSカタログ定義取込 代替経路の確認 DEF10</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>代替経路の確認では オンライン変更 の 定義取込 を主操作として DEF10 を判定します。主経路との役割差への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF10 に残します。代替経路の確認を補助する メンバー状態 では status を補助値として DEF10 へ保存します。主判定の代替経路の確認ではオンライン変更・カタログ定義取込の 定義取込 から resource を読み DEF10 へ残します。証跡照合の代替経路の確認ではオンライン変更・カタログ定義取込の resource と status を DEF10 に保存します。記録対応の代替経路の確認ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で オンライン変更 の 定義取込 と メンバー状態 を実施し IMSカタログ定義取込 の役割を確認します。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。対象 DEF10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. IMPORT DEFN SOURCE(CATALOG)のコマンド文字列だけを記録する。resourceを含む応答行は保存しない。</li><li>B. IMPORT DEFN SOURCE(CATALOG)とQUERY MEMBER TYPE(IMS) SHOW(STATUS)の対象名をそろえる。前者のresourceをIMPORT完了コードとメンバー反映の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. IMSカタログ定義取込の停止または再定義を実施する。その後にIMPORT DEFN SOURCE(CATALOG)でresourceを採取する。</li><li>D. ログ管理のアクティブログとアーカイブ先を確認する。その値をオンライン変更のDEF10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Bは定義取込で resource を読みIMPORT完了コードとメンバー反映の主値として代替手段の成立を確認しDEF10に残します。
運用上の背景: 代替経路の確認ではメンバー状態を補助操作としIMSカタログ定義取込の主経路との役割差をstatusと対象DEF10で照合します。
候補別の検討: 定義取込とメンバー状態の役割を分けるとA: 入力記録だけではIMPORT完了コードとメンバー反映を証明できない点で一次資料と一致しません、B: 同じ対象名のresourceを採用する点でDEF10を判定できます、C: 変更前のIMPORT完了コードとメンバー反映を失う点でメンバー状態の範囲を越えます、D: ログ管理の値ではresourceを確認できない点でDEF10の値を示しません。結論として代替経路の確認のオンライン変更・カタログ定義取込で判定する対象は DEF10 です。
重要用語の定義: 代替経路の確認で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 代替経路の確認 DEF10</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について代替手段の成立を確認し、DEF10のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF10の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF10&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF10のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF10) SHOW(ALL)を指定し、DEF10の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF10) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF10&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の resource が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の access が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0121"><h3>オンライン変更 IMSカタログ定義取込 変更前の確認 DEF02</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>変更前の確認では オンライン変更 の メンバー状態 を主操作として DEF02 を判定します。変更対象と非対象の境界への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF02 に残します。変更前の確認を補助する 反映定義照会 では access を補助値として DEF02 へ保存します。主判定の変更前の確認ではオンライン変更・カタログ定義取込の メンバー状態 から status を読み DEF02 へ残します。証跡照合の変更前の確認ではオンライン変更・カタログ定義取込の status と access を DEF02 に保存します。記録対応の変更前の確認ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で オンライン変更 の メンバー状態 と 反映定義照会 の役割を分け 変更対象と非対象の境界 を調べます。IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みです。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。対象 DEF02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)を対象名なしで実行する。一覧の先頭行をDEF02の結果として記録する。</li><li>B. 対象DEF02についてQUERY MEMBER TYPE(IMS) SHOW(STATUS)の応答からstatusを確認する。QUERY DB NAME(DEF02) SHOW(ALL)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したQUERY MEMBER TYPE(IMS) SHOW(STATUS)の結果を使う。今回のQUERY DB NAME(DEF02) SHOW(ALL)の結果と同一時点の証跡として比較する。</li><li>D. 保存済みのDEF02の出力を再利用する。今回のQUERY MEMBER TYPE(IMS) SHOW(STATUS)とQUERY DB NAME(DEF02) SHOW(ALL)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bはメンバー状態で status を読みIMPORT完了コードとメンバー反映の主値として変更前の証跡を保存しDEF02に残します。
動作の背景: 変更前の確認では反映定義照会を補助操作としIMSカタログ定義取込の変更対象と非対象の境界をaccessと対象DEF02で照合します。
各選択肢の検討: メンバー状態と反映定義照会の役割を分けるとA: 先頭行はDEF02と確定できない点で変更前の確認に合いません、B: statusと補助証跡の時刻を合わせる点でメンバー状態に合います、C: 採取時刻が異なる点でオンライン変更に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でIMSカタログ定義取込に使えません。結論として変更前の確認のオンライン変更・カタログ定義取込で判定する対象は DEF02 です。
初出用語の定義: 変更前の確認で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 変更前の確認 DEF02</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について変更前の証跡を保存し、DEF02のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF02のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF02) SHOW(ALL)を指定し、DEF02の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF02) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF02&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF02の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF02&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の access が画面・出力に表示されること
③ ステップ3 の resource が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0122"><h3>オンライン変更 IMSカタログ定義取込 変更後の確認 DEF03</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>変更後の確認では オンライン変更 の 反映定義照会 を主操作として DEF03 を判定します。反映値と残存値への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF03 に残します。変更後の確認を補助する 定義取込 では resource を補助値として DEF03 へ保存します。主判定の変更後の確認ではオンライン変更・カタログ定義取込の 反映定義照会 から access を読み DEF03 へ残します。証跡照合の変更後の確認ではオンライン変更・カタログ定義取込の access と resource を DEF03 に保存します。記録対応の変更後の確認ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で オンライン変更 の 反映定義照会 と 定義取込 を使い 変更結果を検証 します。IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みです。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。access を読み対象 DEF03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. IMSカタログ定義取込の停止または再定義を実施する。その後にQUERY DB NAME(DEF03) SHOW(ALL)でaccessを採取する。</li><li>B. DBRC/RECONのDBDS登録とRECON可用性を確認する。その値をオンライン変更のDEF03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IMSカタログ定義取込の反映値と残存値は確認済みとして扱う。さらにQUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusをaccessと同種の値として併記する。</li><li>C. IMPORT DEFN SOURCE(CATALOG)で周辺状態を押さえる。その後にQUERY DB NAME(DEF03) SHOW(ALL)でaccessを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. IMPORT DEFN SOURCE(CATALOG)が成功したためQUERY DB NAME(DEF03) SHOW(ALL)のaccessも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Cは反映定義照会で access を読みIMPORT完了コードとメンバー反映の主値として変更結果を検証しDEF03に残します。
内部の仕組み: 変更後の確認では定義取込を補助操作としIMSカタログ定義取込の反映値と残存値をresourceと対象DEF03で照合します。
誤答を含む比較: 反映定義照会と定義取込の役割を分けるとA: 変更前のIMPORT完了コードとメンバー反映を失う点でIMPORT完了コードとメンバー反映を確認できません、B: DBRC/RECONの値ではaccessを確認できないうえに追加前提も不正な点で定義取込の範囲を越えます、C: 周辺状態の後にaccessを確認する点で現在値を示します、D: 補助操作の成功ではaccessを確定できない点で変更後の確認に合いません。結論として変更後の確認のオンライン変更・カタログ定義取込で判定する対象は DEF03 です。
用語定義: 変更後の確認で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 変更後の確認 DEF03</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について変更結果を検証し、DEF03のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF03) SHOW(ALL)を指定し、DEF03の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF03) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF03&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF03の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF03&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF03のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の access が画面・出力に表示されること
② ステップ2 の resource が画面・出力に表示されること
③ ステップ3 の status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0123"><h3>オンライン変更 IMSカタログ定義取込 引継ぎ記録 DEF09</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>引継ぎ記録では オンライン変更 の 反映定義照会 を主操作として DEF09 を判定します。次担当者が追跡できる証跡への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF09 に残します。引継ぎ記録を補助する 定義取込 では resource を補助値として DEF09 へ保存します。主判定の引継ぎ記録ではオンライン変更・カタログ定義取込の 反映定義照会 から access を読み DEF09 へ残します。証跡照合の引継ぎ記録ではオンライン変更・カタログ定義取込の access と resource を DEF09 に保存します。記録対応の引継ぎ記録ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で オンライン変更 の 反映定義照会 と 定義取込 を使い 再現可能な記録を作成 します。IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みです。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。access を読み対象 DEF09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 対象名DEF09を指定してQUERY DB NAME(DEF09) SHOW(ALL)を実行する。応答中のaccessと時刻を保存する。IMPORT DEFN SOURCE(CATALOG)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. IMPORT DEFN SOURCE(CATALOG)が成功したためQUERY DB NAME(DEF09) SHOW(ALL)のaccessも正常だと推定する。主出力は保存しない。</li><li>C. QUERY DB NAME(DEF09) SHOW(ALL)を対象名なしで実行する。一覧の先頭行をDEF09の結果として記録する。</li><li>D. 前回保存したQUERY DB NAME(DEF09) SHOW(ALL)の結果を使う。今回のIMPORT DEFN SOURCE(CATALOG)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Aは反映定義照会で access を読みIMPORT完了コードとメンバー反映の主値として再現可能な記録を作成しDEF09に残します。
製品内の仕組み: 引継ぎ記録では定義取込を補助操作としIMSカタログ定義取込の次担当者が追跡できる証跡をresourceと対象DEF09で照合します。
選択肢別の説明: 反映定義照会と定義取込の役割を分けるとA: accessと時刻を保存する点で現在値を示します、B: 補助操作の成功ではaccessを確定できない点で引継ぎ記録に合いません、C: 先頭行はDEF09と確定できない点で反映定義照会を代替しません、D: 採取時刻が異なる点でオンライン変更に使いません。結論として引継ぎ記録のオンライン変更・カタログ定義取込で判定する対象は DEF09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 引継ぎ記録 DEF09</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について再現可能な記録を作成し、DEF09のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF09) SHOW(ALL)を指定し、DEF09の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF09) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF09&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF09の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF09&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF09のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の access が画面・出力に表示されること
② ステップ2 の resource が画面・出力に表示されること
③ ステップ3 の status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0124"><h3>オンライン変更 IMSカタログ定義取込 復旧後の確認 DEF06</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>復旧後の確認では オンライン変更 の 反映定義照会 を主操作として DEF06 を判定します。再発していないことを示す値への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF06 に残します。復旧後の確認を補助する 定義取込 では resource を補助値として DEF06 へ保存します。主判定の復旧後の確認ではオンライン変更・カタログ定義取込の 反映定義照会 から access を読み DEF06 へ残します。証跡照合の復旧後の確認ではオンライン変更・カタログ定義取込の access と resource を DEF06 に保存します。記録対応の復旧後の確認ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で オンライン変更 の 反映定義照会 と 定義取込 を照合し 再発していないことを示す値 を確かめます。IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みです。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。access を読む前に対象 DEF06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. オンライン変更のIMPORT完了コードとメンバー反映を確認する。その値をオンライン変更のDEF06にも適用する。</li><li>B. QUERY DB NAME(DEF06) SHOW(ALL)でaccessを取得してからQUERY MEMBER TYPE(IMS) SHOW(STATUS)でstatusを照合する。DEF06のIMPORT完了コードとメンバー反映を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. IMPORT DEFN SOURCE(CATALOG)が成功したためQUERY DB NAME(DEF06) SHOW(ALL)のaccessも正常だと推定する。主出力は保存しない。別資源で得た状態を対象DEF06へ引き継げるものとする。IMSカタログ定義取込の再発していないことを示す値は確認済みとして扱う。さらにQUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusをaccessと同種の値として併記する。</li><li>D. QUERY DB NAME(DEF06) SHOW(ALL)を対象名なしで実行する。一覧の先頭行をDEF06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Bは反映定義照会で access を読みIMPORT完了コードとメンバー反映の主値として復旧後の安定性を確認しDEF06に残します。
構成上の背景: 復旧後の確認では定義取込を補助操作としIMSカタログ定義取込の再発していないことを示す値をresourceと対象DEF06で照合します。
候補ごとの理由: 反映定義照会と定義取込の役割を分けるとA: オンライン変更の値ではaccessを確認できない点で定義取込の範囲を越えます、B: accessとstatusを順に照合する点で現在値を示します、C: 補助操作の成功ではaccessを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はDEF06と確定できない点で反映定義照会を代替しません。結論として復旧後の確認のオンライン変更・カタログ定義取込で判定する対象は DEF06 です。
初出用語: 復旧後の確認で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 復旧後の確認 DEF06</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について復旧後の安定性を確認し、DEF06のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF06) SHOW(ALL)を指定し、DEF06の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF06) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF06&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF06の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF06&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF06のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の access が画面・出力に表示されること
② ステップ2 の resource が画面・出力に表示されること
③ ステップ3 の status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0125"><h3>オンライン変更 IMSカタログ定義取込 復旧準備 DEF05</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>復旧準備では オンライン変更 の メンバー状態 を主操作として DEF05 を判定します。再開前に必要な整合性への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF05 に残します。復旧準備を補助する 反映定義照会 では access を補助値として DEF05 へ保存します。主判定の復旧準備ではオンライン変更・カタログ定義取込の メンバー状態 から status を読み DEF05 へ残します。証跡照合の復旧準備ではオンライン変更・カタログ定義取込の status と access を DEF05 に保存します。記録対応の復旧準備ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で オンライン変更 の メンバー状態 と 反映定義照会 を用い 復旧条件を確認 します。IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みです。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。status で対象 DEF05 の IMPORT完了コードとメンバー反映 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずQUERY MEMBER TYPE(IMS) SHOW(STATUS)を実行する。statusを保存する。差分はQUERY DB NAME(DEF05) SHOW(ALL)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したQUERY MEMBER TYPE(IMS) SHOW(STATUS)の結果を使う。今回のQUERY DB NAME(DEF05) SHOW(ALL)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのDEF05の出力を再利用する。今回のQUERY MEMBER TYPE(IMS) SHOW(STATUS)とQUERY DB NAME(DEF05) SHOW(ALL)は実行済みとして扱う。</li><li>D. QUERY DB NAME(DEF05) SHOW(ALL)のaccessをIMPORT完了コードとメンバー反映の主判定に採用する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはメンバー状態で status を読みIMPORT完了コードとメンバー反映の主値として復旧条件を確認しDEF05に残します。
処理の仕組み: 復旧準備では反映定義照会を補助操作としIMSカタログ定義取込の再開前に必要な整合性をaccessと対象DEF05で照合します。
選択結果の内訳: メンバー状態と反映定義照会の役割を分けるとA: 変更前のstatusを保存する点でメンバー状態に合います、B: 採取時刻が異なる点でオンライン変更に使いません、C: 過去出力では今回の復旧準備を示せない点でIMSカタログ定義取込に使えません、D: accessはstatusを代替しないうえに追加前提も不正な点でDEF05を採用できません。結論として復旧準備のオンライン変更・カタログ定義取込で判定する対象は DEF05 です。
用語の説明: 復旧準備で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 復旧準備 DEF05</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について復旧条件を確認し、DEF05のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF05のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF05) SHOW(ALL)を指定し、DEF05の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF05) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF05&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF05の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF05&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の access が画面・出力に表示されること
③ ステップ3 の resource が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0126"><h3>オンライン変更 IMSカタログ定義取込 構成監査 DEF08</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>構成監査では オンライン変更 の メンバー状態 を主操作として DEF08 を判定します。定義値と稼働値の一致への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF08 に残します。構成監査を補助する 反映定義照会 では access を補助値として DEF08 へ保存します。主判定の構成監査ではオンライン変更・カタログ定義取込の メンバー状態 から status を読み DEF08 へ残します。証跡照合の構成監査ではオンライン変更・カタログ定義取込の status と access を DEF08 に保存します。記録対応の構成監査ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で オンライン変更 の メンバー状態 と 反映定義照会 の役割を分け 定義値と稼働値の一致 を調べます。IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みです。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。対象 DEF08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのDEF08の出力を再利用する。今回のQUERY MEMBER TYPE(IMS) SHOW(STATUS)とQUERY DB NAME(DEF08) SHOW(ALL)は実行済みとして扱う。</li><li>B. QUERY DB NAME(DEF08) SHOW(ALL)のaccessをIMPORT完了コードとメンバー反映の主判定に採用する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)の応答は採取対象から外す。</li><li>C. IMPORT DEFN SOURCE(CATALOG)のresourceをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。</li><li>D. QUERY DB NAME(DEF08) SHOW(ALL)の結果だけでは確定しない。QUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはメンバー状態で status を読みIMPORT完了コードとメンバー反映の主値として構成差分を監査しDEF08に残します。
実行時の背景: 構成監査では反映定義照会を補助操作としIMSカタログ定義取込の定義値と稼働値の一致をaccessと対象DEF08で照合します。
四つの候補の理由: メンバー状態と反映定義照会の役割を分けるとA: 過去出力では今回の構成監査を示せない点でオンライン変更に使いません、B: accessはstatusを代替しない点でIMSカタログ定義取込に使えません、C: resourceとstatusは確認項目が異なる点でDEF08を採用できません、D: statusを主証跡として区別する点で主証跡になります。結論として構成監査のオンライン変更・カタログ定義取込で判定する対象は DEF08 です。
初出語定義: 構成監査で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 構成監査 DEF08</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について構成差分を監査し、DEF08のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF08のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF08) SHOW(ALL)を指定し、DEF08の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF08) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF08&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF08の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF08&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の access が画面・出力に表示されること
③ ステップ3 の resource が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0127"><h3>オンライン変更 IMSカタログ定義取込 通常状態の確認 DEF01</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>通常状態の確認では オンライン変更 の 定義取込 を主操作として DEF01 を判定します。基準値と現在値の差への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF01 に残します。通常状態の確認を補助する メンバー状態 では status を補助値として DEF01 へ保存します。主判定の通常状態の確認ではオンライン変更・カタログ定義取込の 定義取込 から resource を読み DEF01 へ残します。証跡照合の通常状態の確認ではオンライン変更・カタログ定義取込の resource と status を DEF01 に保存します。記録対応の通常状態の確認ではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で オンライン変更 の 定義取込 と メンバー状態 を組み合わせる際は IMSカタログ定義取込 がIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みという仕組みを前提にします。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。resource と IMPORT完了コードとメンバー反映 を対象 DEF01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. IMPORT DEFN SOURCE(CATALOG)を先に実行する。対象DEF01のresourceをIMPORT完了コードとメンバー反映として記録する。続いてQUERY MEMBER TYPE(IMS) SHOW(STATUS)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusをIMPORT完了コードとメンバー反映の主判定に採用する。IMPORT DEFN SOURCE(CATALOG)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. QUERY DB NAME(DEF01) SHOW(ALL)のaccessをresourceと同義の成功表示として扱う。IMPORT DEFN SOURCE(CATALOG)は実行しない。</li><li>D. IMPORT DEFN SOURCE(CATALOG)が応答を返した時点で正常とする。応答中のresourceの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Aは定義取込で resource を読みIMPORT完了コードとメンバー反映の主値として通常状態を確定しDEF01に残します。
背景・仕組み: 通常状態の確認ではメンバー状態を補助操作としIMSカタログ定義取込の基準値と現在値の差をstatusと対象DEF01で照合します。
選択肢の理由: 定義取込とメンバー状態の役割を分けるとA: resourceを主値として補助結果と照合する点で正答です、B: statusはresourceを代替しないうえに追加前提も不正な点でDEF01を採用できません、C: accessとresourceは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではIMPORT完了コードとメンバー反映を判定できない点で一次資料と一致しません。結論として通常状態の確認のオンライン変更・カタログ定義取込で判定する対象は DEF01 です。
用語の初出定義: 通常状態の確認で使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 通常状態の確認 DEF01</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について通常状態を確定し、DEF01のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF01の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF01&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF01のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF01) SHOW(ALL)を指定し、DEF01の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF01) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF01&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の resource が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の access が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0128"><h3>オンライン変更 IMSカタログ定義取込 障害切り分け DEF04</h3><p class="kb-meta">分類: オンライン変更 ・ 難易度: 中級</p><p>障害切り分けでは オンライン変更 の 定義取込 を主操作として DEF04 を判定します。最初に失敗した処理への注意として「一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります」を DEF04 に残します。障害切り分けを補助する メンバー状態 では status を補助値として DEF04 へ保存します。主判定の障害切り分けではオンライン変更・カタログ定義取込の 定義取込 から resource を読み DEF04 へ残します。証跡照合の障害切り分けではオンライン変更・カタログ定義取込の resource と status を DEF04 に保存します。記録対応の障害切り分けではオンライン変更・カタログ定義取込の IMPORT完了コードとメンバー反映 の証跡へ DEF04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで オンライン変更 の 定義取込 と メンバー状態 を実施し IMSカタログ定義取込 の役割を確認します。一部メンバーだけ旧定義が残ると処理結果がメンバーごとに変わります。対象 DEF04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. QUERY DB NAME(DEF04) SHOW(ALL)のaccessをresourceと同義の成功表示として扱う。IMPORT DEFN SOURCE(CATALOG)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. IMPORT DEFN SOURCE(CATALOG)が応答を返した時点で正常とする。応答中のresourceの値は記録しない。</li><li>C. IMPORT DEFN SOURCE(CATALOG)のコマンド文字列だけを記録する。resourceを含む応答行は保存しない。</li><li>D. IMPORT DEFN SOURCE(CATALOG)の出力でDEF04とresourceが同じ応答にあることを確認する。IMPORT完了コードとメンバー反映をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Dは定義取込で resource を読みIMPORT完了コードとメンバー反映の主値として障害範囲を限定しDEF04に残します。
技術的背景: 障害切り分けではメンバー状態を補助操作としIMSカタログ定義取込の最初に失敗した処理をstatusと対象DEF04で照合します。
四択の評価: 定義取込とメンバー状態の役割を分けるとA: accessとresourceは確認項目が異なるうえに追加前提も不正な点でDEF04を採用できません、B: 応答の有無だけではIMPORT完了コードとメンバー反映を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではIMPORT完了コードとメンバー反映を証明できない点で一次資料と一致しません、D: DEF04とresourceを同じ応答で結ぶ点でDEF04を判定できます。結論として障害切り分けのオンライン変更・カタログ定義取込で判定する対象は DEF04 です。
初出語の意味: 障害切り分けで使う IMSカタログ定義取込 はIMSカタログ上のDBDやPSBをオンライン環境へ取り込み、停止を抑えて定義を更新する仕組みを表しIMPORT完了コードとメンバー反映を判定する際にDEF04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>オンライン変更 IMSカタログ定義取込 障害切り分け DEF04</strong></p><p>検証目的: オンライン変更のIMSカタログ定義取込について障害範囲を限定し、DEF04のIMPORT完了コードとメンバー反映を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DEF04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へIMPORT DEFN SOURCE(CATALOG)を指定し、DEF04の定義取込を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; IMPORT DEFN SOURCE(CATALOG)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMPORT&lt;/typ&gt;&lt;resource&gt;DEF04&lt;/resource&gt;&lt;stt&gt;COMPLETE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるresourceを読み、IMPORT完了コードとメンバー反映と対象DEF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DEF04のメンバー状態を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、IMPORT完了コードとメンバー反映と対象DEF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のオンライン変更を確認する入力画面です。COMMAND入力口へQUERY DB NAME(DEF04) SHOW(ALL)を指定し、DEF04の反映定義照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY DB NAME(DEF04) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;db&gt;DEF04&lt;/db&gt;&lt;stt&gt;AVAILABLE&lt;/stt&gt;&lt;access&gt;UPD&lt;/access&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるaccessを読み、IMPORT完了コードとメンバー反映と対象DEF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の resource が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の access が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


## コマンド


<section class="kb-item" id="c16-i0129"><h3>MODIFY fdbrproc</h3><p class="kb-meta">分類: コマンド ・ 難易度: 上級</p><p>IMS 15.5 の コマンドで扱うMODIFY fdbrprocは、MODIFY fdbrproc コマンドは、稼働中の Fast Database Recovery 領域に対して制御操作を行うために使います。通常の IMS コマンドとは対象領域が異なるため、fdbrproc 名と操作内容を取り違えないようにします。運用記録では発行時刻と応答メッセージを残します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認のコマンドでアイエムエスの運用確認を行います。MODIFY fdbrprocの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IMS 15.5と無関係な一覧で監査確認のコマンドを確認した扱いにする。</li><li>B. DFS058I の有無を確認せず監査確認のコマンドを正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. MODIFY fdbrprocの属性行を読まず監査確認のコマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では MODIFY fdbrproc は「IMS 15.5で MODIFY fdbrprocの扱いを記録する監査確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では MODIFY fdbrprocの表示結果と DFS058I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では MODIFY fdbrprocの使い方を出典欄から追跡し、資料名は監査確認資料です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MODIFY fdbrproc</strong></p><p>検証目的: 監査確認のコマンドについて、IMS 15.5 の コマンドで扱う MODIFY fdbrprocは、MODIFY fdbrproc コマンドは、稼働中の Fast Database Recovery 領に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、監査確認のコマンドの確認表示へ進みます。
［操作（入力）］
(IMS Terminal)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
→ Enter を押す
［画面・出力］
(IMS Terminal)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIMS Terminalの表示結果です。FIND欄にMODIFY fdbrprocを指定し、OSKB010019の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND MODIFY fdbrproc
CASE OSKB010019
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM MODIFY fdbrproc
CASE OSKB010019
SOURCE IMS 15.5
MODIFY fdbrprocとOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010019を同じ出力で読み、監査確認のコマンドの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010019
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010019
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010019  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の MODIFY fdbrproc と OSKB010019 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0130"><h3>START fdbrproc</h3><p class="kb-meta">分類: コマンド ・ 難易度: 上級</p><p>IMS 15.5 の コマンドで扱うSTART fdbrprocは、START fdbrproc コマンドは、IMS Fast Database Recovery 領域を開始する操作です。FDBR は障害時の高速回復に関わるため、開始対象のプロシージャと関連する IMS 環境を確認します。起動後はメッセージと領域状態を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認のコマンドで START fdbrprocの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. START fdbrprocの出力を取らず復旧確認のコマンドの説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY TRANSACTION OSKB を省略して復旧確認のコマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認のコマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では START fdbrproc は「復旧確認のコマンドに関係する定義値と表示行を照合する復旧確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では START fdbrprocの属性行と DFS058I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では START fdbrprocを IMS 15.5の運用手順で確認し、初出名は復旧確認初出です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>START fdbrproc</strong></p><p>検証目的: 復旧確認のコマンドについて、IMS 15.5 の コマンドで扱う START fdbrprocは、START fdbrproc コマンドは、IMS Fast Database Recovery 領域を開に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、復旧確認のコマンドの確認表示へ進みます。
［操作（入力）］
(IMS Terminal)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
→ Enter を押す
［画面・出力］
(IMS Terminal)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIMS Terminalの表示結果です。FIND欄にSTART fdbrprocを指定し、OSKB010018の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND START fdbrproc
CASE OSKB010018
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM START fdbrproc
CASE OSKB010018
SOURCE IMS 15.5
START fdbrprocとOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010018を同じ出力で読み、復旧確認のコマンドの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010018
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010018
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010018  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の START fdbrproc と OSKB010018 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## チェックポイント


<section class="kb-item" id="c16-i0131"><h3>/DISPLAY DATABASE ログ照合 通信口</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 中級</p><p>IMS 15.5 の チェックポイント で扱う「/DISPLAY DATABASE ログ照合 通信口」は、データベースまたはDBDの登録状態とアクセス状態を表示するIMSコマンドをログ照合の観点で確認する技術項目です。DFS3499I 行とAREA6を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY DATABASE ログ照合 通信口</strong></p><p>検証目的: チェックポイントにおける/DISPLAY DATABASEのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA6</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0132"><h3>/DISPLAY DATABASE 再始動確認 詳細表示</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>IMS 15.5 の チェックポイント で扱う「/DISPLAY DATABASE 再始動確認 詳細表示」は、データベースまたはDBDの登録状態とアクセス状態を表示するIMSコマンドを再始動確認の観点で確認する技術項目です。DFS3499I 行とAREA2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY DATABASE 再始動確認 詳細表示</strong></p><p>検証目的: チェックポイントにおける/DISPLAY DATABASEの再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0133"><h3>/ERESTART CHKPT 実行条件確認 サービス状態</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 中級</p><p>IMS 15.5 の チェックポイント で扱う「/ERESTART CHKPT 実行条件確認 サービス状態」は、異常終了後に指定チェックポイントから緊急再始動するIMSコマンドを実行条件確認の観点で確認する技術項目です。DFS3499I 行とUTIL038を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/ERESTART CHKPT 実行条件確認 サービス状態</strong></p><p>検証目的: チェックポイントにおける/ERESTART CHKPTの実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL038</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB038)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM038,PSB038,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB038
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0134"><h3>/ERESTART CHKPT 状態確認 ページング状態</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 上級</p><p>IMS 15.5 の チェックポイント で扱う「/ERESTART CHKPT 状態確認 ページング状態」は、異常終了後に指定チェックポイントから緊急再始動するIMSコマンドを状態確認の観点で確認する技術項目です。DFS3499I 行とUTIL098を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/ERESTART CHKPT 状態確認 ページング状態</strong></p><p>検証目的: チェックポイントにおける/ERESTART CHKPTの状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL098</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB098)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM098,PSB098,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB098
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0135"><h3>DFS3499I 戻りコード確認 対象ファイル</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 上級</p><p>IMS 15.5 の チェックポイント で扱う「DFS3499I 戻りコード確認 対象ファイル」は、再始動関連のアクティブDD名を示すIMSメッセージを戻りコード確認の観点で確認する技術項目です。DFS3499I 行とODBM2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS3499I 戻りコード確認 対象ファイル</strong></p><p>検証目的: チェックポイントにおけるDFS3499Iの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD086
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD086
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD086
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD086 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0136"><h3>DFS3499I 整合確認 ディスク状態</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 中級</p><p>IMS 15.5 の チェックポイント で扱う「DFS3499I 整合確認 ディスク状態」は、再始動関連のアクティブDD名を示すIMSメッセージを整合確認の観点で確認する技術項目です。DFS3499I 行とODBM2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS3499I 整合確認 ディスク状態</strong></p><p>検証目的: チェックポイントにおけるDFS3499Iの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD026
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD026
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD026
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD026 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0137"><h3>DFSURGL0 状態確認 同期点</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 中級</p><p>IMS 15.5 の チェックポイント で扱う「DFSURGL0 状態確認 同期点」は、HD Reorganization ReloadでアンロードデータからDBを再ロードするIMSユーティリティを状態確認の観点で確認する技術項目です。DFS3499I 行とPAY050を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURGL0 状態確認 同期点</strong></p><p>検証目的: チェックポイントにおけるDFSURGL0の状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY050</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY050) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY050&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD050) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD050&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA2) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA2&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0138"><h3>IMSLOGR DD ログ照合 停止確認</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>IMS 15.5 の チェックポイント で扱う「IMSLOGR DD ログ照合 停止確認」は、再始動時にチェックポイント記録を読み取るログ入力DDをログ照合の観点で確認する技術項目です。DFS3499I 行とRECON2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMSLOGR DD ログ照合 停止確認</strong></p><p>検証目的: チェックポイントにおけるIMSLOGR DDのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO014&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM2&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM2) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM2  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM2&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0139"><h3>IMSLOGR DD 整合確認 属性確認</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 中級</p><p>IMS 15.5 の チェックポイント で扱う「IMSLOGR DD 整合確認 属性確認」は、再始動時にチェックポイント記録を読み取るログ入力DDを整合確認の観点で確認する技術項目です。DFS3499I 行とRECON2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMSLOGR DD 整合確認 属性確認</strong></p><p>検証目的: チェックポイントにおけるIMSLOGR DDの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO074&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM2&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM2) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM2  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM2&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0140"><h3>チェックポイント 停止チェックポイント ログとの照合 CKPT07</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>ログとの照合では チェックポイント の FREEZE応答 を主操作として CKPT07 を判定します。時刻と対象識別子への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT07 に残します。ログとの照合を補助する DUMPQ応答 では DUMPQ を補助値として CKPT07 へ保存します。主判定のログとの照合ではチェックポイント・停止チェックポイントの FREEZE応答 から DFS994I を読み CKPT07 へ残します。証跡照合のログとの照合ではチェックポイント・停止チェックポイントの DFS994I と DUMPQ を CKPT07 に保存します。記録対応のログとの照合ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で チェックポイント の FREEZE応答 と DUMPQ応答 を用い 操作とログを対応 します。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DFS994I で対象 CKPT07 の チェックポイント種別と時刻 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. DFS994Iを含むFREEZE応答の応答行を保存する。その応答を得るため/CHECKPOINT FREEZEを使用する。対象CKPT07のチェックポイント種別と時刻として記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. /CHECKPOINT FREEZEが応答を返した時点で正常とする。応答中のDFS994Iの値は記録しない。DFS3804IをDFS994Iと同じ判定値とみなし対象CKPT07の主証跡にする。</li><li>C. /CHECKPOINT FREEZEのコマンド文字列だけを記録する。DFS994Iを含む応答行は保存しない。</li><li>D. 停止チェックポイントの停止または再定義を実施する。その後に/CHECKPOINT FREEZEでDFS994Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 適切な判定: AはFREEZE応答で DFS994I を読みチェックポイント種別と時刻の主値として操作とログを対応しCKPT07に残します。
機能の仕組み: ログとの照合ではDUMPQ応答を補助操作とし停止チェックポイントの時刻と対象識別子をDUMPQと対象CKPT07で照合します。
各候補の評価: FREEZE応答とDUMPQ応答の役割を分けるとA: DFS994Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではチェックポイント種別と時刻を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではチェックポイント種別と時刻を証明できない点でチェックポイント種別と時刻を確認できません、D: 変更前のチェックポイント種別と時刻を失う点でDUMPQ応答の範囲を越えます。結論としてログとの照合のチェックポイント・停止チェックポイントで判定する対象は CKPT07 です。
用語の定義: ログとの照合で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント ログとの照合 CKPT07</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて操作とログを対応し、CKPT07のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT07のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT07のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT07の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DUMPQ が画面・出力に表示されること
③ ステップ3 の DFS3804I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0141"><h3>チェックポイント 停止チェックポイント 代替経路の確認 CKPT10</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>代替経路の確認では チェックポイント の FREEZE応答 を主操作として CKPT10 を判定します。主経路との役割差への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT10 に残します。代替経路の確認を補助する DUMPQ応答 では DUMPQ を補助値として CKPT10 へ保存します。主判定の代替経路の確認ではチェックポイント・停止チェックポイントの FREEZE応答 から DFS994I を読み CKPT10 へ残します。証跡照合の代替経路の確認ではチェックポイント・停止チェックポイントの DFS994I と DUMPQ を CKPT10 に保存します。記録対応の代替経路の確認ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で チェックポイント の FREEZE応答 と DUMPQ応答 の役割を分け 主経路との役割差 を調べます。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。対象 CKPT10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. /CHECKPOINT FREEZEのコマンド文字列だけを記録する。DFS994Iを含む応答行は保存しない。</li><li>B. 停止チェックポイントの停止または再定義を実施する。その後に/CHECKPOINT FREEZEでDFS994Iを採取する。</li><li>C. ODBM/OMのALIASと到達状態を確認する。その値をチェックポイントのCKPT10にも適用する。</li><li>D. /CHECKPOINT FREEZEと/CHECKPOINT DUMPQの対象名をそろえる。前者のDFS994Iをチェックポイント種別と時刻の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい判定結果: DはFREEZE応答で DFS994I を読みチェックポイント種別と時刻の主値として代替手段の成立を確認しCKPT10に残します。
運用上の背景: 代替経路の確認ではDUMPQ応答を補助操作とし停止チェックポイントの主経路との役割差をDUMPQと対象CKPT10で照合します。
候補別の検討: FREEZE応答とDUMPQ応答の役割を分けるとA: 入力記録だけではチェックポイント種別と時刻を証明できない点で一次資料と一致しません、B: 変更前のチェックポイント種別と時刻を失う点でチェックポイント種別と時刻を確認できません、C: ODBM/OMの値ではDFS994Iを確認できない点でDUMPQ応答の範囲を越えます、D: 同じ対象名のDFS994Iを採用する点で現在値を示します。結論として代替経路の確認のチェックポイント・停止チェックポイントで判定する対象は CKPT10 です。
重要用語の定義: 代替経路の確認で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 代替経路の確認 CKPT10</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて代替手段の成立を確認し、CKPT10のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT10のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT10のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT10の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DUMPQ が画面・出力に表示されること
③ ステップ3 の DFS3804I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0142"><h3>チェックポイント 停止チェックポイント 変更前の確認 CKPT02</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>変更前の確認では チェックポイント の DUMPQ応答 を主操作として CKPT02 を判定します。変更対象と非対象の境界への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT02 に残します。変更前の確認を補助する 最新停止点 では DFS3804I を補助値として CKPT02 へ保存します。主判定の変更前の確認ではチェックポイント・停止チェックポイントの DUMPQ応答 から DUMPQ を読み CKPT02 へ残します。証跡照合の変更前の確認ではチェックポイント・停止チェックポイントの DUMPQ と DFS3804I を CKPT02 に保存します。記録対応の変更前の確認ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で チェックポイント の DUMPQ応答 と 最新停止点 を照合し 変更対象と非対象の境界 を確かめます。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DUMPQ を読む前に対象 CKPT02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. /CHECKPOINT DUMPQを対象名なしで実行する。一覧の先頭行をCKPT02の結果として記録する。</li><li>B. 前回保存した/CHECKPOINT DUMPQの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのCKPT02の出力を再利用する。今回の/CHECKPOINT DUMPQと/DISPLAY OLDSは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象CKPT02について/CHECKPOINT DUMPQの応答からDUMPQを確認する。/DISPLAY OLDSは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: DはDUMPQ応答で DUMPQ を読みチェックポイント種別と時刻の主値として変更前の証跡を保存しCKPT02に残します。
動作の背景: 変更前の確認では最新停止点を補助操作とし停止チェックポイントの変更対象と非対象の境界をDFS3804Iと対象CKPT02で照合します。
各選択肢の検討: DUMPQ応答と最新停止点の役割を分けるとA: 先頭行はCKPT02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でDUMPQ応答を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でチェックポイントに使いません、D: DUMPQと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のチェックポイント・停止チェックポイントで判定する対象は CKPT02 です。
初出用語の定義: 変更前の確認で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 変更前の確認 CKPT02</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて変更前の証跡を保存し、CKPT02のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT02のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT02の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT02のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DUMPQ が画面・出力に表示されること
② ステップ2 の DFS3804I が画面・出力に表示されること
③ ステップ3 の DFS994I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0143"><h3>チェックポイント 停止チェックポイント 変更後の確認 CKPT03</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>変更後の確認では チェックポイント の 最新停止点 を主操作として CKPT03 を判定します。反映値と残存値への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT03 に残します。変更後の確認を補助する FREEZE応答 では DFS994I を補助値として CKPT03 へ保存します。主判定の変更後の確認ではチェックポイント・停止チェックポイントの 最新停止点 から DFS3804I を読み CKPT03 へ残します。証跡照合の変更後の確認ではチェックポイント・停止チェックポイントの DFS3804I と DFS994I を CKPT03 に保存します。記録対応の変更後の確認ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で チェックポイント の 最新停止点 と FREEZE応答 を組み合わせる際は 停止チェックポイント が入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能という仕組みを前提にします。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DFS3804I と チェックポイント種別と時刻 を対象 CKPT03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. /CHECKPOINT FREEZEで周辺状態を押さえる。その後に/DISPLAY OLDSでDFS3804Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. 停止チェックポイントの停止または再定義を実施する。その後に/DISPLAY OLDSでDFS3804Iを採取する。</li><li>C. チェックポイントのチェックポイント種別と時刻を確認する。その値をチェックポイントのCKPT03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>D. /CHECKPOINT FREEZEが成功したため/DISPLAY OLDSのDFS3804Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Aは最新停止点で DFS3804I を読みチェックポイント種別と時刻の主値として変更結果を検証しCKPT03に残します。
内部の仕組み: 変更後の確認ではFREEZE応答を補助操作とし停止チェックポイントの反映値と残存値をDFS994Iと対象CKPT03で照合します。
誤答を含む比較: 最新停止点とFREEZE応答の役割を分けるとA: 周辺状態の後にDFS3804Iを確認する点でCKPT03を判定できます、B: 変更前のチェックポイント種別と時刻を失う点でFREEZE応答の範囲を越えます、C: チェックポイントの値ではDFS3804Iを確認できないうえに追加前提も不正な点でCKPT03の値を示しません、D: 補助操作の成功ではDFS3804Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のチェックポイント・停止チェックポイントで判定する対象は CKPT03 です。
用語定義: 変更後の確認で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 変更後の確認 CKPT03</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて変更結果を検証し、CKPT03のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT03の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT03のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT03のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS3804I が画面・出力に表示されること
② ステップ2 の DFS994I が画面・出力に表示されること
③ ステップ3 の DUMPQ が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0144"><h3>チェックポイント 停止チェックポイント 引継ぎ記録 CKPT09</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>引継ぎ記録では チェックポイント の 最新停止点 を主操作として CKPT09 を判定します。次担当者が追跡できる証跡への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT09 に残します。引継ぎ記録を補助する FREEZE応答 では DFS994I を補助値として CKPT09 へ保存します。主判定の引継ぎ記録ではチェックポイント・停止チェックポイントの 最新停止点 から DFS3804I を読み CKPT09 へ残します。証跡照合の引継ぎ記録ではチェックポイント・停止チェックポイントの DFS3804I と DFS994I を CKPT09 に保存します。記録対応の引継ぎ記録ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で チェックポイント の 最新停止点 と FREEZE応答 を組み合わせる際は 停止チェックポイント が入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能という仕組みを前提にします。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DFS3804I と チェックポイント種別と時刻 を対象 CKPT09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. /CHECKPOINT FREEZEが成功したため/DISPLAY OLDSのDFS3804Iも正常だと推定する。主出力は保存しない。</li><li>B. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をCKPT09の結果として記録する。</li><li>C. 対象名CKPT09を指定して/DISPLAY OLDSを実行する。応答中のDFS3804Iと時刻を保存する。/CHECKPOINT FREEZEで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存した/DISPLAY OLDSの結果を使う。今回の/CHECKPOINT FREEZEの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用操作の理由: Cは最新停止点で DFS3804I を読みチェックポイント種別と時刻の主値として再現可能な記録を作成しCKPT09に残します。
製品内の仕組み: 引継ぎ記録ではFREEZE応答を補助操作とし停止チェックポイントの次担当者が追跡できる証跡をDFS994Iと対象CKPT09で照合します。
選択肢別の説明: 最新停止点とFREEZE応答の役割を分けるとA: 補助操作の成功ではDFS3804Iを確定できない点でCKPT09の値を示しません、B: 先頭行はCKPT09と確定できない点で引継ぎ記録に合いません、C: DFS3804Iと時刻を保存する点で最新停止点に合います、D: 採取時刻が異なる点でチェックポイントに使いません。結論として引継ぎ記録のチェックポイント・停止チェックポイントで判定する対象は CKPT09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 引継ぎ記録 CKPT09</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて再現可能な記録を作成し、CKPT09のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT09の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT09のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT09のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS3804I が画面・出力に表示されること
② ステップ2 の DFS994I が画面・出力に表示されること
③ ステップ3 の DUMPQ が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0145"><h3>チェックポイント 停止チェックポイント 復旧後の確認 CKPT06</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>復旧後の確認では チェックポイント の 最新停止点 を主操作として CKPT06 を判定します。再発していないことを示す値への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT06 に残します。復旧後の確認を補助する FREEZE応答 では DFS994I を補助値として CKPT06 へ保存します。主判定の復旧後の確認ではチェックポイント・停止チェックポイントの 最新停止点 から DFS3804I を読み CKPT06 へ残します。証跡照合の復旧後の確認ではチェックポイント・停止チェックポイントの DFS3804I と DFS994I を CKPT06 に保存します。記録対応の復旧後の確認ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で チェックポイント の 最新停止点 と FREEZE応答 を実施し 停止チェックポイント の役割を確認します。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。対象 CKPT06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. DBD/PSB/ACBの定義名と有効版を確認する。その値をチェックポイントのCKPT06にも適用する。</li><li>B. /CHECKPOINT FREEZEが成功したため/DISPLAY OLDSのDFS3804Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象CKPT06へ引き継げるものとする。</li><li>C. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をCKPT06の結果として記録する。</li><li>D. /DISPLAY OLDSでDFS3804Iを取得してから/CHECKPOINT DUMPQでDUMPQを照合する。CKPT06のチェックポイント種別と時刻を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答内容: Dは最新停止点で DFS3804I を読みチェックポイント種別と時刻の主値として復旧後の安定性を確認しCKPT06に残します。
構成上の背景: 復旧後の確認ではFREEZE応答を補助操作とし停止チェックポイントの再発していないことを示す値をDFS994Iと対象CKPT06で照合します。
候補ごとの理由: 最新停止点とFREEZE応答の役割を分けるとA: DBD/PSB/ACBの値ではDFS3804Iを確認できない点でFREEZE応答の範囲を越えます、B: 補助操作の成功ではDFS3804Iを確定できないうえに追加前提も不正な点でCKPT06の値を示しません、C: 先頭行はCKPT06と確定できない点で復旧後の確認に合いません、D: DFS3804IとDUMPQを順に照合する点で最新停止点に合います。結論として復旧後の確認のチェックポイント・停止チェックポイントで判定する対象は CKPT06 です。
初出用語: 復旧後の確認で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 復旧後の確認 CKPT06</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて復旧後の安定性を確認し、CKPT06のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT06の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT06のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT06のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS3804I が画面・出力に表示されること
② ステップ2 の DFS994I が画面・出力に表示されること
③ ステップ3 の DUMPQ が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0146"><h3>チェックポイント 停止チェックポイント 復旧準備 CKPT05</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>復旧準備では チェックポイント の DUMPQ応答 を主操作として CKPT05 を判定します。再開前に必要な整合性への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT05 に残します。復旧準備を補助する 最新停止点 では DFS3804I を補助値として CKPT05 へ保存します。主判定の復旧準備ではチェックポイント・停止チェックポイントの DUMPQ応答 から DUMPQ を読み CKPT05 へ残します。証跡照合の復旧準備ではチェックポイント・停止チェックポイントの DUMPQ と DFS3804I を CKPT05 に保存します。記録対応の復旧準備ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で チェックポイント の DUMPQ応答 と 最新停止点 を使い 復旧条件を確認 します。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DUMPQ を読み対象 CKPT05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存した/CHECKPOINT DUMPQの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのCKPT05の出力を再利用する。今回の/CHECKPOINT DUMPQと/DISPLAY OLDSは実行済みとして扱う。</li><li>C. 変更を加えず/CHECKPOINT DUMPQを実行する。DUMPQを保存する。差分は/DISPLAY OLDSの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. /DISPLAY OLDSのDFS3804Iをチェックポイント種別と時刻の主判定に採用する。/CHECKPOINT DUMPQの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 選定理由: CはDUMPQ応答で DUMPQ を読みチェックポイント種別と時刻の主値として復旧条件を確認しCKPT05に残します。
処理の仕組み: 復旧準備では最新停止点を補助操作とし停止チェックポイントの再開前に必要な整合性をDFS3804Iと対象CKPT05で照合します。
選択結果の内訳: DUMPQ応答と最新停止点の役割を分けるとA: 採取時刻が異なる点でDUMPQ応答を代替しません、B: 過去出力では今回の復旧準備を示せない点でチェックポイントに使いません、C: 変更前のDUMPQを保存する点で正答です、D: DFS3804IはDUMPQを代替しないうえに追加前提も不正な点でCKPT05を採用できません。結論として復旧準備のチェックポイント・停止チェックポイントで判定する対象は CKPT05 です。
用語の説明: 復旧準備で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 復旧準備 CKPT05</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて復旧条件を確認し、CKPT05のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT05のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT05の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT05のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DUMPQ が画面・出力に表示されること
② ステップ2 の DFS3804I が画面・出力に表示されること
③ ステップ3 の DFS994I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0147"><h3>チェックポイント 停止チェックポイント 構成監査 CKPT08</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>構成監査では チェックポイント の DUMPQ応答 を主操作として CKPT08 を判定します。定義値と稼働値の一致への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT08 に残します。構成監査を補助する 最新停止点 では DFS3804I を補助値として CKPT08 へ保存します。主判定の構成監査ではチェックポイント・停止チェックポイントの DUMPQ応答 から DUMPQ を読み CKPT08 へ残します。証跡照合の構成監査ではチェックポイント・停止チェックポイントの DUMPQ と DFS3804I を CKPT08 に保存します。記録対応の構成監査ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で チェックポイント の DUMPQ応答 と 最新停止点 を照合し 定義値と稼働値の一致 を確かめます。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DUMPQ を読む前に対象 CKPT08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのCKPT08の出力を再利用する。今回の/CHECKPOINT DUMPQと/DISPLAY OLDSは実行済みとして扱う。</li><li>B. /DISPLAY OLDSの結果だけでは確定しない。/CHECKPOINT DUMPQのDUMPQを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY OLDSのDFS3804Iをチェックポイント種別と時刻の主判定に採用する。/CHECKPOINT DUMPQの応答は採取対象から外す。</li><li>D. /CHECKPOINT FREEZEのDFS994IをDUMPQと同義の成功表示として扱う。/CHECKPOINT DUMPQは実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 技術上の正答: BはDUMPQ応答で DUMPQ を読みチェックポイント種別と時刻の主値として構成差分を監査しCKPT08に残します。
実行時の背景: 構成監査では最新停止点を補助操作とし停止チェックポイントの定義値と稼働値の一致をDFS3804Iと対象CKPT08で照合します。
四つの候補の理由: DUMPQ応答と最新停止点の役割を分けるとA: 過去出力では今回の構成監査を示せない点でチェックポイントに使いません、B: DUMPQを主証跡として区別する点で正答です、C: DFS3804IはDUMPQを代替しない点でCKPT08を採用できません、D: DFS994IとDUMPQは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のチェックポイント・停止チェックポイントで判定する対象は CKPT08 です。
初出語定義: 構成監査で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 構成監査 CKPT08</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて構成差分を監査し、CKPT08のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT08のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT08の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT08のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DUMPQ が画面・出力に表示されること
② ステップ2 の DFS3804I が画面・出力に表示されること
③ ステップ3 の DFS994I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0148"><h3>チェックポイント 停止チェックポイント 通常状態の確認 CKPT01</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>通常状態の確認では チェックポイント の FREEZE応答 を主操作として CKPT01 を判定します。基準値と現在値の差への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT01 に残します。通常状態の確認を補助する DUMPQ応答 では DUMPQ を補助値として CKPT01 へ保存します。主判定の通常状態の確認ではチェックポイント・停止チェックポイントの FREEZE応答 から DFS994I を読み CKPT01 へ残します。証跡照合の通常状態の確認ではチェックポイント・停止チェックポイントの DFS994I と DUMPQ を CKPT01 に保存します。記録対応の通常状態の確認ではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で チェックポイント の FREEZE応答 と DUMPQ応答 を用い 通常状態を確定 します。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。DFS994I で対象 CKPT01 の チェックポイント種別と時刻 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. /CHECKPOINT DUMPQのDUMPQをチェックポイント種別と時刻の主判定に採用する。/CHECKPOINT FREEZEの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. /DISPLAY OLDSのDFS3804IをDFS994Iと同義の成功表示として扱う。/CHECKPOINT FREEZEは実行しない。</li><li>C. /CHECKPOINT FREEZEを先に実行する。対象CKPT01のDFS994Iをチェックポイント種別と時刻として記録する。続いて/CHECKPOINT DUMPQで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. /CHECKPOINT FREEZEが応答を返した時点で正常とする。応答中のDFS994Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: CはFREEZE応答で DFS994I を読みチェックポイント種別と時刻の主値として通常状態を確定しCKPT01に残します。
背景・仕組み: 通常状態の確認ではDUMPQ応答を補助操作とし停止チェックポイントの基準値と現在値の差をDUMPQと対象CKPT01で照合します。
選択肢の理由: FREEZE応答とDUMPQ応答の役割を分けるとA: DUMPQはDFS994Iを代替しないうえに追加前提も不正な点で停止チェックポイントに使えません、B: DFS3804IとDFS994Iは確認項目が異なる点でCKPT01を採用できません、C: DFS994Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではチェックポイント種別と時刻を判定できない点で一次資料と一致しません。結論として通常状態の確認のチェックポイント・停止チェックポイントで判定する対象は CKPT01 です。
用語の初出定義: 通常状態の確認で使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 通常状態の確認 CKPT01</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて通常状態を確定し、CKPT01のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT01のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT01のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT01の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DUMPQ が画面・出力に表示されること
③ ステップ3 の DFS3804I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0149"><h3>チェックポイント 停止チェックポイント 障害切り分け CKPT04</h3><p class="kb-meta">分類: チェックポイント ・ 難易度: 初級</p><p>障害切り分けでは チェックポイント の FREEZE応答 を主操作として CKPT04 を判定します。最初に失敗した処理への注意として「FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります」を CKPT04 に残します。障害切り分けを補助する DUMPQ応答 では DUMPQ を補助値として CKPT04 へ保存します。主判定の障害切り分けではチェックポイント・停止チェックポイントの FREEZE応答 から DFS994I を読み CKPT04 へ残します。証跡照合の障害切り分けではチェックポイント・停止チェックポイントの DFS994I と DUMPQ を CKPT04 に保存します。記録対応の障害切り分けではチェックポイント・停止チェックポイントの チェックポイント種別と時刻 の証跡へ CKPT04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで チェックポイント の FREEZE応答 と DUMPQ応答 の役割を分け 最初に失敗した処理 を調べます。停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能です。FREEZEとDUMPQの目的を混同すると再始動時のキュー扱いを誤ります。対象 CKPT04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY OLDSのDFS3804IをDFS994Iと同義の成功表示として扱う。/CHECKPOINT FREEZEは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. /CHECKPOINT FREEZEの出力でCKPT04とDFS994Iが同じ応答にあることを確認する。チェックポイント種別と時刻をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. /CHECKPOINT FREEZEが応答を返した時点で正常とする。応答中のDFS994Iの値は記録しない。</li><li>D. /CHECKPOINT FREEZEのコマンド文字列だけを記録する。DFS994Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: BはFREEZE応答で DFS994I を読みチェックポイント種別と時刻の主値として障害範囲を限定しCKPT04に残します。
技術的背景: 障害切り分けではDUMPQ応答を補助操作とし停止チェックポイントの最初に失敗した処理をDUMPQと対象CKPT04で照合します。
四択の評価: FREEZE応答とDUMPQ応答の役割を分けるとA: DFS3804IとDFS994Iは確認項目が異なるうえに追加前提も不正な点でCKPT04を採用できません、B: CKPT04とDFS994Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではチェックポイント種別と時刻を判定できない点で一次資料と一致しません、D: 入力記録だけではチェックポイント種別と時刻を証明できない点でチェックポイント種別と時刻を確認できません。結論として障害切り分けのチェックポイント・停止チェックポイントで判定する対象は CKPT04 です。
初出語の意味: 障害切り分けで使う 停止チェックポイント は入力の凍結またはキュー保持を選び、処理中BMPの到達点を待って停止位置を確定する機能を表しチェックポイント種別と時刻を判定する際にCKPT04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>チェックポイント 停止チェックポイント 障害切り分け CKPT04</strong></p><p>検証目的: チェックポイントの停止チェックポイントについて障害範囲を限定し、CKPT04のチェックポイント種別と時刻を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象CKPT04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT FREEZEを指定し、CKPT04のFREEZE応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力にあるDFS994Iを読み、チェックポイント種別と時刻と対象CKPT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/CHECKPOINT DUMPQを指定し、CKPT04のDUMPQ応答を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT DUMPQ
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/090214**DUMPQ*
画面・出力にあるDUMPQを読み、チェックポイント種別と時刻と対象CKPT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のチェックポイントを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、CKPT04の最新停止点を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3804I LATEST RESTART CHKPT: 82170/085820, LATEST BUILDQ CHKPT: 82170/090214
画面・出力にあるDFS3804Iを読み、チェックポイント種別と時刻と対象CKPT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DUMPQ が画面・出力に表示されること
③ ステップ3 の DFS3804I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


## データベースユーティリティ


<section class="kb-item" id="c16-i0150"><h3>/CHECKPOINT FREEZE リカバリ確認 制御ブロック</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>IMS 15.5 の データベースユーティリティ で扱う「/CHECKPOINT FREEZE リカバリ確認 制御ブロック」は、入力を凍結し、既存処理とBMPチェックポイント到達を待つ停止系チェックポイントをリカバリ確認の観点で確認する技術項目です。CHKPT IDとRECON1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT FREEZE リカバリ確認 制御ブロック</strong></p><p>検証目的: データベースユーティリティにおける/CHECKPOINT FREEZEのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO034&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM2&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM2) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM2  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM2&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0151"><h3>/CHECKPOINT FREEZE 接続確認 メッセージ行</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 上級</p><p>IMS 15.5 の データベースユーティリティ で扱う「/CHECKPOINT FREEZE 接続確認 メッセージ行」は、入力を凍結し、既存処理とBMPチェックポイント到達を待つ停止系チェックポイントを接続確認の観点で確認する技術項目です。CHKPT IDとRECON1を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT FREEZE 接続確認 メッセージ行</strong></p><p>検証目的: データベースユーティリティにおける/CHECKPOINT FREEZEの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON1</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO094&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM2&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; UPDATE IMSCON TYPE(ODBM) NAME(ODBM2) START(COMM)
→ Enter を押す
［画面・出力］
The UPDATE IMSCON TYPE(ODBM) command completed successfully.
ODBM2  X&#x27;00000000&#x27;  X&#x27;00000000&#x27;
画面・出力には UPDATE が含まれ、UPDATEを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY ODBM SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;ODBM2&quot;&gt;&lt;typ&gt;ODBM&lt;/typ&gt;&lt;stt&gt;ACTIVE&lt;/stt&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の UPDATE が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0152"><h3>DFS4452I 実行条件確認 退避状態</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>IMS 15.5 の データベースユーティリティ で扱う「DFS4452I 実行条件確認 退避状態」は、IMSplex資源クリーンアップの開始または完了を示すIMSメッセージを実行条件確認の観点で確認する技術項目です。CHKPT IDとUTIL058を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS4452I 実行条件確認 退避状態</strong></p><p>検証目的: データベースユーティリティにおけるDFS4452Iの実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL058</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB058)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM058,PSB058,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND IMSLOGR
→ Enter を押す
［画面・出力］
//IMSLOGR DD DSN=IMS.OLDS.CHECKPOINT.INPUT,DISP=SHR
画面・出力には IMSLOGR が含まれ、IMSLOGRを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; FIND CHKPT
→ Enter を押す
［画面・出力］
CHKPT ID 82170/085236 FOUND FOR PSB058
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0153"><h3>DFSPREC0 ログ照合 設定値</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>IMS 15.5 の データベースユーティリティ で扱う「DFSPREC0 ログ照合 設定値」は、HALDB索引やILDSを再作成して整合性を戻すIMSユーティリティをログ照合の観点で確認する技術項目です。CHKPT IDとAREA2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSPREC0 ログ照合 設定値</strong></p><p>検証目的: データベースユーティリティにおけるDFSPREC0のログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0154"><h3>DFSPREC0 再始動確認 再開位置</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>IMS 15.5 の データベースユーティリティ で扱う「DFSPREC0 再始動確認 再開位置」は、HALDB索引やILDSを再作成して整合性を戻すIMSユーティリティを再始動確認の観点で確認する技術項目です。CHKPT IDとAREA6を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSPREC0 再始動確認 再開位置</strong></p><p>検証目的: データベースユーティリティにおけるDFSPREC0の再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA6</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /CHECKPOINT FREEZE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/085820**FREEZE*
画面・出力には DFS994I が含まれ、DFS994Iを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085236
DFS994I *CHKPT 82170/085820**SIMPLE*
画面・出力には DFS058I が含まれ、DFS058Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY ACTIVE
→ Enter を押す
［画面・出力］
DFS000I IMS ACTIVE AFTER NRESTART BUILDQ
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS994I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0155"><h3>DFSUICP0 接続確認 対象領域</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>IMS 15.5 の データベースユーティリティ で扱う「DFSUICP0 接続確認 対象領域」は、オンライン環境で更新可能性を考慮しながらイメージコピーを取得するBMP型ユーティリティを接続確認の観点で確認する技術項目です。CHKPT IDとODBM2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUICP0 接続確認 対象領域</strong></p><p>検証目的: データベースユーティリティにおけるDFSUICP0の接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD046
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD046
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD046
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD046 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0156"><h3>UPDATE IMSCON TYPE(ODBM) 再始動確認 終了表示</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>IMS 15.5 の データベースユーティリティ で扱う「UPDATE IMSCON TYPE(ODBM) 再始動確認 終了表示」は、IMS ConnectとODBMの通信開始または停止を行うタイプ2コマンドを再始動確認の観点で確認する技術項目です。CHKPT IDとPAY070を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPDATE IMSCON TYPE(ODBM) 再始動確認 終了表示</strong></p><p>検証目的: データベースユーティリティにおけるUPDATE IMSCON TYPE(ODBM)の再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY070</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY070) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY070&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD070) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD070&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA6) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA6&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0157"><h3>UPDATE IMSCON TYPE(ODBM) 出力項目確認 保存場所</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 初級</p><p>IMS 15.5 の データベースユーティリティ で扱う「UPDATE IMSCON TYPE(ODBM) 出力項目確認 保存場所」は、IMS ConnectとODBMの通信開始または停止を行うタイプ2コマンドを出力項目確認の観点で確認する技術項目です。CHKPT IDとPAY010を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPDATE IMSCON TYPE(ODBM) 出力項目確認 保存場所</strong></p><p>検証目的: データベースユーティリティにおけるUPDATE IMSCON TYPE(ODBM)の出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY010</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY010) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY010&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD010) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD010&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY AREA NAME(AREA2) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;area&gt;AREA2&lt;/area&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の name= が画面・出力に表示されること
③ ステップ3 の name= が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0158"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ ログとの照合 UTIL07</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 上級</p><p>ログとの照合では データベースユーティリティ の イメージコピー を主操作として UTIL07 を判定します。時刻と対象識別子への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL07 に残します。ログとの照合を補助する 変更累積 では DFSUCUM0 を補助値として UTIL07 へ保存します。主判定のログとの照合ではデータベースユーティリティ・データベース復旧ユーティリティの イメージコピー から DFSUDMP0 を読み UTIL07 へ残します。証跡照合のログとの照合ではデータベースユーティリティ・データベース復旧ユーティリティの DFSUDMP0 と DFSUCUM0 を UTIL07 に保存します。記録対応のログとの照合ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で データベースユーティリティ の イメージコピー と 変更累積 を組み合わせる際は IMSデータベース復旧ユーティリティ がイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群という仕組みを前提にします。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。DFSUDMP0 と ユーティリティ名と戻りコード を対象 UTIL07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. DFSUDMP0を含むイメージコピーの応答行を保存する。その応答を得るためSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を使用する。対象UTIL07のユーティリティ名と戻りコードとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)が応答を返した時点で正常とする。応答中のDFSUDMP0の値は記録しない。DFSURDB0をDFSUDMP0と同じ判定値とみなし対象UTIL07の主証跡にする。</li><li>C. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)のコマンド文字列だけを記録する。DFSUDMP0を含む応答行は保存しない。</li><li>D. IMSデータベース復旧ユーティリティの停止または再定義を実施する。その後にSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)でDFSUDMP0を採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: Aはイメージコピーで DFSUDMP0 を読みユーティリティ名と戻りコードの主値として操作とログを対応しUTIL07に残します。
機能の仕組み: ログとの照合では変更累積を補助操作としIMSデータベース復旧ユーティリティの時刻と対象識別子をDFSUCUM0と対象UTIL07で照合します。
各候補の評価: イメージコピーと変更累積の役割を分けるとA: DFSUDMP0の実値を対象別に残す点で主証跡になります、B: 応答の有無だけではユーティリティ名と戻りコードを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではユーティリティ名と戻りコードを証明できない点でユーティリティ名と戻りコードを確認できません、D: 変更前のユーティリティ名と戻りコードを失う点で変更累積の範囲を越えます。結論としてログとの照合のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL07 です。
用語の定義: ログとの照合で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ ログとの照合 UTIL07</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて操作とログを対応し、UTIL07のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL07のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL07
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL07の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL07のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL07.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0159"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 代替経路の確認 UTIL10</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 上級</p><p>代替経路の確認では データベースユーティリティ の イメージコピー を主操作として UTIL10 を判定します。主経路との役割差への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL10 に残します。代替経路の確認を補助する 変更累積 では DFSUCUM0 を補助値として UTIL10 へ保存します。主判定の代替経路の確認ではデータベースユーティリティ・データベース復旧ユーティリティの イメージコピー から DFSUDMP0 を読み UTIL10 へ残します。証跡照合の代替経路の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DFSUDMP0 と DFSUCUM0 を UTIL10 に保存します。記録対応の代替経路の確認ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で データベースユーティリティ の イメージコピー と 変更累積 を実施し IMSデータベース復旧ユーティリティ の役割を確認します。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。対象 UTIL10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)のコマンド文字列だけを記録する。DFSUDMP0を含む応答行は保存しない。</li><li>B. IMSデータベース復旧ユーティリティの停止または再定義を実施する。その後にSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)でDFSUDMP0を採取する。</li><li>C. DBD/PSB/ACBの定義名と有効版を確認する。その値をデータベースユーティリティのUTIL10にも適用する。</li><li>D. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)とSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)の対象名をそろえる。前者のDFSUDMP0をユーティリティ名と戻りコードの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: Dはイメージコピーで DFSUDMP0 を読みユーティリティ名と戻りコードの主値として代替手段の成立を確認しUTIL10に残します。
運用上の背景: 代替経路の確認では変更累積を補助操作としIMSデータベース復旧ユーティリティの主経路との役割差をDFSUCUM0と対象UTIL10で照合します。
候補別の検討: イメージコピーと変更累積の役割を分けるとA: 入力記録だけではユーティリティ名と戻りコードを証明できない点で一次資料と一致しません、B: 変更前のユーティリティ名と戻りコードを失う点でユーティリティ名と戻りコードを確認できません、C: DBD/PSB/ACBの値ではDFSUDMP0を確認できない点で変更累積の範囲を越えます、D: 同じ対象名のDFSUDMP0を採用する点で現在値を示します。結論として代替経路の確認のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL10 です。
重要用語の定義: 代替経路の確認で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 代替経路の確認 UTIL10</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて代替手段の成立を確認し、UTIL10のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL10のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL10
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL10の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL10のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL10.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0160"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 変更前の確認 UTIL02</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>変更前の確認では データベースユーティリティ の 変更累積 を主操作として UTIL02 を判定します。変更対象と非対象の境界への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL02 に残します。変更前の確認を補助する DBDS復旧 では DFSURDB0 を補助値として UTIL02 へ保存します。主判定の変更前の確認ではデータベースユーティリティ・データベース復旧ユーティリティの 変更累積 から DFSUCUM0 を読み UTIL02 へ残します。証跡照合の変更前の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DFSUCUM0 と DFSURDB0 を UTIL02 に保存します。記録対応の変更前の確認ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で データベースユーティリティ の 変更累積 と DBDS復旧 の役割を分け 変更対象と非対象の境界 を調べます。IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群です。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。対象 UTIL02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を対象名なしで実行する。一覧の先頭行をUTIL02の結果として記録する。</li><li>B. 前回保存したSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)の結果を使う。今回のSUBMIT IMS.DFSURDB0.CNTL(RECOVER)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのUTIL02の出力を再利用する。今回のSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)とSUBMIT IMS.DFSURDB0.CNTL(RECOVER)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象UTIL02についてSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)の応答からDFSUCUM0を確認する。SUBMIT IMS.DFSURDB0.CNTL(RECOVER)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは変更累積で DFSUCUM0 を読みユーティリティ名と戻りコードの主値として変更前の証跡を保存しUTIL02に残します。
動作の背景: 変更前の確認ではDBDS復旧を補助操作としIMSデータベース復旧ユーティリティの変更対象と非対象の境界をDFSURDB0と対象UTIL02で照合します。
各選択肢の検討: 変更累積とDBDS復旧の役割を分けるとA: 先頭行はUTIL02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で変更累積を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でデータベースユーティリティに使いません、D: DFSUCUM0と補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL02 です。
初出用語の定義: 変更前の確認で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 変更前の確認 UTIL02</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて変更前の証跡を保存し、UTIL02のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL02の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL02のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL02.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL02のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL02
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUCUM0 が画面・出力に表示されること
② ステップ2 の DFSURDB0 が画面・出力に表示されること
③ ステップ3 の DFSUDMP0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0161"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 変更後の確認 UTIL03</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>変更後の確認では データベースユーティリティ の DBDS復旧 を主操作として UTIL03 を判定します。反映値と残存値への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL03 に残します。変更後の確認を補助する イメージコピー では DFSUDMP0 を補助値として UTIL03 へ保存します。主判定の変更後の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DBDS復旧 から DFSURDB0 を読み UTIL03 へ残します。証跡照合の変更後の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DFSURDB0 と DFSUDMP0 を UTIL03 に保存します。記録対応の変更後の確認ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で データベースユーティリティ の DBDS復旧 と イメージコピー を使い 変更結果を検証 します。IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群です。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。DFSURDB0 を読み対象 UTIL03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)で周辺状態を押さえる。その後にSUBMIT IMS.DFSURDB0.CNTL(RECOVER)でDFSURDB0を確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. IMSデータベース復旧ユーティリティの停止または再定義を実施する。その後にSUBMIT IMS.DFSURDB0.CNTL(RECOVER)でDFSURDB0を採取する。</li><li>C. データベースユーティリティのユーティリティ名と戻りコードを確認する。その値をデータベースユーティリティのUTIL03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IMSデータベース復旧ユーティリティの反映値と残存値は確認済みとして扱う。さらにSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)のDFSUCUM0をDFSURDB0と同種の値として併記する。</li><li>D. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)が成功したためSUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0も正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: AはDBDS復旧で DFSURDB0 を読みユーティリティ名と戻りコードの主値として変更結果を検証しUTIL03に残します。
内部の仕組み: 変更後の確認ではイメージコピーを補助操作としIMSデータベース復旧ユーティリティの反映値と残存値をDFSUDMP0と対象UTIL03で照合します。
誤答を含む比較: DBDS復旧とイメージコピーの役割を分けるとA: 周辺状態の後にDFSURDB0を確認する点でUTIL03を判定できます、B: 変更前のユーティリティ名と戻りコードを失う点でイメージコピーの範囲を越えます、C: データベースユーティリティの値ではDFSURDB0を確認できないうえに追加前提も不正な点でUTIL03の値を示しません、D: 補助操作の成功ではDFSURDB0を確定できない点で変更後の確認に合いません。結論として変更後の確認のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL03 です。
用語定義: 変更後の確認で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 変更後の確認 UTIL03</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて変更結果を検証し、UTIL03のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL03のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL03.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL03のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL03
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL03の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSURDB0 が画面・出力に表示されること
② ステップ2 の DFSUDMP0 が画面・出力に表示されること
③ ステップ3 の DFSUCUM0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0162"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 引継ぎ記録 UTIL09</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 上級</p><p>引継ぎ記録では データベースユーティリティ の DBDS復旧 を主操作として UTIL09 を判定します。次担当者が追跡できる証跡への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL09 に残します。引継ぎ記録を補助する イメージコピー では DFSUDMP0 を補助値として UTIL09 へ保存します。主判定の引継ぎ記録ではデータベースユーティリティ・データベース復旧ユーティリティの DBDS復旧 から DFSURDB0 を読み UTIL09 へ残します。証跡照合の引継ぎ記録ではデータベースユーティリティ・データベース復旧ユーティリティの DFSURDB0 と DFSUDMP0 を UTIL09 に保存します。記録対応の引継ぎ記録ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で データベースユーティリティ の DBDS復旧 と イメージコピー を使い 再現可能な記録を作成 します。IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群です。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。DFSURDB0 を読み対象 UTIL09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)が成功したためSUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0も正常だと推定する。主出力は保存しない。</li><li>B. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)を対象名なしで実行する。一覧の先頭行をUTIL09の結果として記録する。</li><li>C. 対象名UTIL09を指定してSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を実行する。応答中のDFSURDB0と時刻を保存する。SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSUBMIT IMS.DFSURDB0.CNTL(RECOVER)の結果を使う。今回のSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: CはDBDS復旧で DFSURDB0 を読みユーティリティ名と戻りコードの主値として再現可能な記録を作成しUTIL09に残します。
製品内の仕組み: 引継ぎ記録ではイメージコピーを補助操作としIMSデータベース復旧ユーティリティの次担当者が追跡できる証跡をDFSUDMP0と対象UTIL09で照合します。
選択肢別の説明: DBDS復旧とイメージコピーの役割を分けるとA: 補助操作の成功ではDFSURDB0を確定できない点でUTIL09の値を示しません、B: 先頭行はUTIL09と確定できない点で引継ぎ記録に合いません、C: DFSURDB0と時刻を保存する点でDBDS復旧に合います、D: 採取時刻が異なる点でデータベースユーティリティに使いません。結論として引継ぎ記録のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 引継ぎ記録 UTIL09</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて再現可能な記録を作成し、UTIL09のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL09のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL09.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL09のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL09
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL09の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSURDB0 が画面・出力に表示されること
② ステップ2 の DFSUDMP0 が画面・出力に表示されること
③ ステップ3 の DFSUCUM0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0163"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 復旧後の確認 UTIL06</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>復旧後の確認では データベースユーティリティ の DBDS復旧 を主操作として UTIL06 を判定します。再発していないことを示す値への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL06 に残します。復旧後の確認を補助する イメージコピー では DFSUDMP0 を補助値として UTIL06 へ保存します。主判定の復旧後の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DBDS復旧 から DFSURDB0 を読み UTIL06 へ残します。証跡照合の復旧後の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DFSURDB0 と DFSUDMP0 を UTIL06 に保存します。記録対応の復旧後の確認ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で データベースユーティリティ の DBDS復旧 と イメージコピー を照合し 再発していないことを示す値 を確かめます。IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群です。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。DFSURDB0 を読む前に対象 UTIL06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. DB/DC運用のSTATUSとQUEUEを確認する。その値をデータベースユーティリティのUTIL06にも適用する。</li><li>B. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)が成功したためSUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0も正常だと推定する。主出力は保存しない。別資源で得た状態を対象UTIL06へ引き継げるものとする。</li><li>C. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)を対象名なしで実行する。一覧の先頭行をUTIL06の結果として記録する。</li><li>D. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)でDFSURDB0を取得してからSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)でDFSUCUM0を照合する。UTIL06のユーティリティ名と戻りコードを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: DはDBDS復旧で DFSURDB0 を読みユーティリティ名と戻りコードの主値として復旧後の安定性を確認しUTIL06に残します。
構成上の背景: 復旧後の確認ではイメージコピーを補助操作としIMSデータベース復旧ユーティリティの再発していないことを示す値をDFSUDMP0と対象UTIL06で照合します。
候補ごとの理由: DBDS復旧とイメージコピーの役割を分けるとA: DB/DC運用の値ではDFSURDB0を確認できない点でイメージコピーの範囲を越えます、B: 補助操作の成功ではDFSURDB0を確定できないうえに追加前提も不正な点でUTIL06の値を示しません、C: 先頭行はUTIL06と確定できない点で復旧後の確認に合いません、D: DFSURDB0とDFSUCUM0を順に照合する点でDBDS復旧に合います。結論として復旧後の確認のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL06 です。
初出用語: 復旧後の確認で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 復旧後の確認 UTIL06</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて復旧後の安定性を確認し、UTIL06のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL06のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL06.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL06のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL06
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL06の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSURDB0 が画面・出力に表示されること
② ステップ2 の DFSUDMP0 が画面・出力に表示されること
③ ステップ3 の DFSUCUM0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0164"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 復旧準備 UTIL05</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>復旧準備では データベースユーティリティ の 変更累積 を主操作として UTIL05 を判定します。再開前に必要な整合性への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL05 に残します。復旧準備を補助する DBDS復旧 では DFSURDB0 を補助値として UTIL05 へ保存します。主判定の復旧準備ではデータベースユーティリティ・データベース復旧ユーティリティの 変更累積 から DFSUCUM0 を読み UTIL05 へ残します。証跡照合の復旧準備ではデータベースユーティリティ・データベース復旧ユーティリティの DFSUCUM0 と DFSURDB0 を UTIL05 に保存します。記録対応の復旧準備ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で データベースユーティリティ の 変更累積 と DBDS復旧 を用い 復旧条件を確認 します。IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群です。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。DFSUCUM0 で対象 UTIL05 の ユーティリティ名と戻りコード を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)の結果を使う。今回のSUBMIT IMS.DFSURDB0.CNTL(RECOVER)の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのUTIL05の出力を再利用する。今回のSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)とSUBMIT IMS.DFSURDB0.CNTL(RECOVER)は実行済みとして扱う。</li><li>C. 変更を加えずSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を実行する。DFSUCUM0を保存する。差分はSUBMIT IMS.DFSURDB0.CNTL(RECOVER)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0をユーティリティ名と戻りコードの主判定に採用する。SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは変更累積で DFSUCUM0 を読みユーティリティ名と戻りコードの主値として復旧条件を確認しUTIL05に残します。
処理の仕組み: 復旧準備ではDBDS復旧を補助操作としIMSデータベース復旧ユーティリティの再開前に必要な整合性をDFSURDB0と対象UTIL05で照合します。
選択結果の内訳: 変更累積とDBDS復旧の役割を分けるとA: 採取時刻が異なる点で変更累積を代替しません、B: 過去出力では今回の復旧準備を示せない点でデータベースユーティリティに使いません、C: 変更前のDFSUCUM0を保存する点で正答です、D: DFSURDB0はDFSUCUM0を代替しないうえに追加前提も不正な点でUTIL05を採用できません。結論として復旧準備のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL05 です。
用語の説明: 復旧準備で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 復旧準備 UTIL05</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて復旧条件を確認し、UTIL05のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL05の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL05のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL05.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL05のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL05
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUCUM0 が画面・出力に表示されること
② ステップ2 の DFSURDB0 が画面・出力に表示されること
③ ステップ3 の DFSUDMP0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0165"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 構成監査 UTIL08</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 上級</p><p>構成監査では データベースユーティリティ の 変更累積 を主操作として UTIL08 を判定します。定義値と稼働値の一致への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL08 に残します。構成監査を補助する DBDS復旧 では DFSURDB0 を補助値として UTIL08 へ保存します。主判定の構成監査ではデータベースユーティリティ・データベース復旧ユーティリティの 変更累積 から DFSUCUM0 を読み UTIL08 へ残します。証跡照合の構成監査ではデータベースユーティリティ・データベース復旧ユーティリティの DFSUCUM0 と DFSURDB0 を UTIL08 に保存します。記録対応の構成監査ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で データベースユーティリティ の 変更累積 と DBDS復旧 の役割を分け 定義値と稼働値の一致 を調べます。IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群です。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。対象 UTIL08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのUTIL08の出力を再利用する。今回のSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)とSUBMIT IMS.DFSURDB0.CNTL(RECOVER)は実行済みとして扱う。</li><li>B. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)の結果だけでは確定しない。SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)のDFSUCUM0を主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0をユーティリティ名と戻りコードの主判定に採用する。SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)の応答は採取対象から外す。</li><li>D. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)のDFSUDMP0をDFSUCUM0と同義の成功表示として扱う。SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: Bは変更累積で DFSUCUM0 を読みユーティリティ名と戻りコードの主値として構成差分を監査しUTIL08に残します。
実行時の背景: 構成監査ではDBDS復旧を補助操作としIMSデータベース復旧ユーティリティの定義値と稼働値の一致をDFSURDB0と対象UTIL08で照合します。
四つの候補の理由: 変更累積とDBDS復旧の役割を分けるとA: 過去出力では今回の構成監査を示せない点でデータベースユーティリティに使いません、B: DFSUCUM0を主証跡として区別する点で正答です、C: DFSURDB0はDFSUCUM0を代替しない点でUTIL08を採用できません、D: DFSUDMP0とDFSUCUM0は確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL08 です。
初出語定義: 構成監査で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 構成監査 UTIL08</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて構成差分を監査し、UTIL08のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL08の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL08のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL08.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL08のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL08
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUCUM0 が画面・出力に表示されること
② ステップ2 の DFSURDB0 が画面・出力に表示されること
③ ステップ3 の DFSUDMP0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0166"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 通常状態の確認 UTIL01</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>通常状態の確認では データベースユーティリティ の イメージコピー を主操作として UTIL01 を判定します。基準値と現在値の差への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL01 に残します。通常状態の確認を補助する 変更累積 では DFSUCUM0 を補助値として UTIL01 へ保存します。主判定の通常状態の確認ではデータベースユーティリティ・データベース復旧ユーティリティの イメージコピー から DFSUDMP0 を読み UTIL01 へ残します。証跡照合の通常状態の確認ではデータベースユーティリティ・データベース復旧ユーティリティの DFSUDMP0 と DFSUCUM0 を UTIL01 に保存します。記録対応の通常状態の確認ではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で データベースユーティリティ の イメージコピー と 変更累積 を組み合わせる際は IMSデータベース復旧ユーティリティ がイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群という仕組みを前提にします。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。DFSUDMP0 と ユーティリティ名と戻りコード を対象 UTIL01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)のDFSUCUM0をユーティリティ名と戻りコードの主判定に採用する。SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0をDFSUDMP0と同義の成功表示として扱う。SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)は実行しない。</li><li>C. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を先に実行する。対象UTIL01のDFSUDMP0をユーティリティ名と戻りコードとして記録する。続いてSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)が応答を返した時点で正常とする。応答中のDFSUDMP0の値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cはイメージコピーで DFSUDMP0 を読みユーティリティ名と戻りコードの主値として通常状態を確定しUTIL01に残します。
背景・仕組み: 通常状態の確認では変更累積を補助操作としIMSデータベース復旧ユーティリティの基準値と現在値の差をDFSUCUM0と対象UTIL01で照合します。
選択肢の理由: イメージコピーと変更累積の役割を分けるとA: DFSUCUM0はDFSUDMP0を代替しないうえに追加前提も不正な点でIMSデータベース復旧ユーティリティに使えません、B: DFSURDB0とDFSUDMP0は確認項目が異なる点でUTIL01を採用できません、C: DFSUDMP0を主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではユーティリティ名と戻りコードを判定できない点で一次資料と一致しません。結論として通常状態の確認のデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL01 です。
用語の初出定義: 通常状態の確認で使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 通常状態の確認 UTIL01</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて通常状態を確定し、UTIL01のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL01のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL01
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL01の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL01のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL01.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0167"><h3>データベースユーティリティ IMSデータベース復旧ユーティリティ 障害切り分け UTIL04</h3><p class="kb-meta">分類: データベースユーティリティ ・ 難易度: 中級</p><p>障害切り分けでは データベースユーティリティ の イメージコピー を主操作として UTIL04 を判定します。最初に失敗した処理への注意として「世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります」を UTIL04 に残します。障害切り分けを補助する 変更累積 では DFSUCUM0 を補助値として UTIL04 へ保存します。主判定の障害切り分けではデータベースユーティリティ・データベース復旧ユーティリティの イメージコピー から DFSUDMP0 を読み UTIL04 へ残します。証跡照合の障害切り分けではデータベースユーティリティ・データベース復旧ユーティリティの DFSUDMP0 と DFSUCUM0 を UTIL04 に保存します。記録対応の障害切り分けではデータベースユーティリティ・データベース復旧ユーティリティの ユーティリティ名と戻りコード の証跡へ UTIL04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで データベースユーティリティ の イメージコピー と 変更累積 を実施し IMSデータベース復旧ユーティリティ の役割を確認します。世代の異なるコピーとログを組み合わせると整合しないDBDSを作ります。対象 UTIL04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IMS.DFSURDB0.CNTL(RECOVER)のDFSURDB0をDFSUDMP0と同義の成功表示として扱う。SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)の出力でUTIL04とDFSUDMP0が同じ応答にあることを確認する。ユーティリティ名と戻りコードをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)が応答を返した時点で正常とする。応答中のDFSUDMP0の値は記録しない。</li><li>D. SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)のコマンド文字列だけを記録する。DFSUDMP0を含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bはイメージコピーで DFSUDMP0 を読みユーティリティ名と戻りコードの主値として障害範囲を限定しUTIL04に残します。
技術的背景: 障害切り分けでは変更累積を補助操作としIMSデータベース復旧ユーティリティの最初に失敗した処理をDFSUCUM0と対象UTIL04で照合します。
四択の評価: イメージコピーと変更累積の役割を分けるとA: DFSURDB0とDFSUDMP0は確認項目が異なるうえに追加前提も不正な点でUTIL04を採用できません、B: UTIL04とDFSUDMP0を同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではユーティリティ名と戻りコードを判定できない点で一次資料と一致しません、D: 入力記録だけではユーティリティ名と戻りコードを証明できない点でユーティリティ名と戻りコードを確認できません。結論として障害切り分けのデータベースユーティリティ・データベース復旧ユーティリティで判定する対象は UTIL04 です。
初出語の意味: 障害切り分けで使う IMSデータベース復旧ユーティリティ はイメージコピー、変更累積、ログを段階的に使ってDBDSを復旧するバッチ処理群を表しユーティリティ名と戻りコードを判定する際にUTIL04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>データベースユーティリティ IMSデータベース復旧ユーティリティ 障害切り分け UTIL04</strong></p><p>検証目的: データベースユーティリティのIMSデータベース復旧ユーティリティについて障害範囲を限定し、UTIL04のユーティリティ名と戻りコードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象UTIL04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)を指定し、UTIL04のイメージコピーを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=UTIL04
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力にあるDFSUDMP0を読み、ユーティリティ名と戻りコードと対象UTIL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSUCUM0.CNTL(CHGACC)を指定し、UTIL04の変更累積を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力にあるDFSUCUM0を読み、ユーティリティ名と戻りコードと対象UTIL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のデータベースユーティリティを確認する入力画面です。COMMAND入力口へSUBMIT IMS.DFSURDB0.CNTL(RECOVER)を指定し、UTIL04のDBDS復旧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS UTIL04.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力にあるDFSURDB0を読み、ユーティリティ名と戻りコードと対象UTIL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


## リスタート


<section class="kb-item" id="c16-i0168"><h3>/DISPLAY AREA リカバリ確認 別名表示</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>IMS 15.5 の リスタート で扱う「/DISPLAY AREA リカバリ確認 別名表示」は、DEDBやHALDB関連の領域状態を確認するIMSコマンドをリカバリ確認の観点で確認する技術項目です。DFS3804I 行と82172/080220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY AREA リカバリ確認 別名表示</strong></p><p>検証目的: リスタートにおける/DISPLAY AREAのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82172/080220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0169"><h3>/DISPLAY AREA 登録確認 構成照合</h3><p class="kb-meta">分類: リスタート ・ 難易度: 初級</p><p>IMS 15.5 の リスタート で扱う「/DISPLAY AREA 登録確認 構成照合」は、DEDBやHALDB関連の領域状態を確認するIMSコマンドを登録確認の観点で確認する技術項目です。DFS3804I 行と82112/080220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/DISPLAY AREA 登録確認 構成照合</strong></p><p>検証目的: リスタートにおける/DISPLAY AREAの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82112/080220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力には DFS058I が含まれ、DFS058Iを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318, LATEST BUILDQ CHKPT: 82120/101400
画面・出力には DFS3499I が含まれ、DFS3499Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY SYSTEM
→ Enter を押す
［画面・出力］
DFS1929I IMS EXECUTION PARAMETERS DISPLAYED AFTER RESTART
画面・出力には DFS1929I が含まれ、DFS1929Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS1929I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0170"><h3>DFS3804I 実行条件確認 一致条件</h3><p class="kb-meta">分類: リスタート ・ 難易度: 上級</p><p>IMS 15.5 の リスタート で扱う「DFS3804I 実行条件確認 一致条件」は、最新Restart/BuildQチェックポイントを示すIMSメッセージを実行条件確認の観点で確認する技術項目です。DFS3804I 行とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS3804I 実行条件確認 一致条件</strong></p><p>検証目的: リスタートにおけるDFS3804Iの実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD087)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD087  DD=DBDS01  RECON=RECON3
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS3 ARCHIVED TO SLDS3
RLDS STATUS AVAILABLE
画面・出力には OLDS3 が含まれ、OLDS3を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS3 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0171"><h3>DFS3804I 接続確認 ボリューム状態</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>IMS 15.5 の リスタート で扱う「DFS3804I 接続確認 ボリューム状態」は、最新Restart/BuildQチェックポイントを示すIMSメッセージを接続確認の観点で確認する技術項目です。DFS3804I 行とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS3804I 接続確認 ボリューム状態</strong></p><p>検証目的: リスタートにおけるDFS3804Iの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD027)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD027  DD=DBDS01  RECON=RECON3
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.RECON STATUS
→ Enter を押す
［画面・出力］
RECON DATA SET STATUS
RECON1 AVAILABLE
RECON2 AVAILABLE
RECON3 SPARE
画面・出力には RECON が含まれ、RECONを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
OLDS3 ARCHIVED TO SLDS3
RLDS STATUS AVAILABLE
画面・出力には OLDS3 が含まれ、OLDS3を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DBRC が画面・出力に表示されること
② ステップ2 の RECON が画面・出力に表示されること
③ ステップ3 の OLDS3 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0172"><h3>DFSBBO00 再始動確認 再始動点</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>IMS 15.5 の リスタート で扱う「DFSBBO00 再始動確認 再始動点」は、動的バックアウト後のリカバリ条件に応じてBatch Backoutを行うIMSユーティリティを再始動確認の観点で確認する技術項目です。DFS3804I 行とDBD051を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSBBO00 再始動確認 再始動点</strong></p><p>検証目的: リスタートにおけるDFSBBO00の再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD051</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY051
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY051 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、ODBM接続状態の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD051
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD051 ACCESS UPDATES ALLOWED DBRC REGISTERED
画面・出力には DFS000I が含まれ、DFS000Iを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY AREA AREA3
→ Enter を押す
［画面・出力］
DFS000I AREA AREA3 STATUS AVAILABLE AUTHORIZED
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFS000I が画面・出力に表示されること
② ステップ2 の DFS000I が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0173"><h3>DFSUDMP0 リカバリ確認 再読込</h3><p class="kb-meta">分類: リスタート ・ 難易度: 初級</p><p>IMS 15.5 の リスタート で扱う「DFSUDMP0 リカバリ確認 再読込」は、Database Image Copyを作成してリカバリ入力を確保するIMSユーティリティをリカバリ確認の観点で確認する技術項目です。DFS3804I 行とOLDS3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUDMP0 リカバリ確認 再読込</strong></p><p>検証目的: リスタートにおけるDFSUDMP0のリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS3</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD015
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD015.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0174"><h3>DFSUDMP0 接続確認 ログ採取</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>IMS 15.5 の リスタート で扱う「DFSUDMP0 接続確認 ログ採取」は、Database Image Copyを作成してリカバリ入力を確保するIMSユーティリティを接続確認の観点で確認する技術項目です。DFS3804I 行とOLDS3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUDMP0 接続確認 ログ採取</strong></p><p>検証目的: リスタートにおけるDFSUDMP0の接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS3</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD075
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、再始動点の誤認を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUCUM0.CNTL(CHGACC)
→ Enter を押す
［画面・出力］
DFSUCUM0 DATABASE CHANGE ACCUMULATION UTILITY
INPUT LOGS ACCEPTED
CHANGE ACCUMULATION DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSUCUM0 が含まれ、DFSUCUM0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURDB0.CNTL(RECOVER)
→ Enter を押す
［画面・出力］
DFSURDB0 DATABASE RECOVERY UTILITY
DBDS DBD075.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0175"><h3>QUERY IMSCON TYPE(ODBM) 再始動確認 性能値</h3><p class="kb-meta">分類: リスタート ・ 難易度: 上級</p><p>IMS 15.5 の リスタート で扱う「QUERY IMSCON TYPE(ODBM) 再始動確認 性能値」は、IMS ConnectからODBM接続、別名、到達状態を確認するタイプ2コマンドを再始動確認の観点で確認する技術項目です。DFS3804I 行とPSB099を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>QUERY IMSCON TYPE(ODBM) 再始動確認 性能値</strong></p><p>検証目的: リスタートにおけるQUERY IMSCON TYPE(ODBM)の再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB099</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD099) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD099 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0176"><h3>QUERY IMSCON TYPE(ODBM) 出力項目確認 変更証跡</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>IMS 15.5 の リスタート で扱う「QUERY IMSCON TYPE(ODBM) 出力項目確認 変更証跡」は、IMS ConnectからODBM接続、別名、到達状態を確認するタイプ2コマンドを出力項目確認の観点で確認する技術項目です。DFS3804I 行とPSB039を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>QUERY IMSCON TYPE(ODBM) 出力項目確認 変更証跡</strong></p><p>検証目的: リスタートにおけるQUERY IMSCON TYPE(ODBM)の出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB039</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD039) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD039 READ FROM IMS CATALOG IMSCD3
RETURN CODE = 0000
画面・出力には DBRC が含まれ、DBRCを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; CHANGE.RECON MINVERS(&#x27;15.1&#x27;)
→ Enter を押す
［画面・出力］
RECON HEADER UPDATED
MINVERS=15.1
RETURN CODE = 0000
画面・出力には RECON が含まれ、RECONを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の name= が画面・出力に表示されること
② ステップ2 の DBRC が画面・出力に表示されること
③ ステップ3 の RECON が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0177"><h3>リスタート IMS再始動点 ログとの照合 RST07</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>ログとの照合では リスタート の 通常再始動 を主操作として RST07 を判定します。時刻と対象識別子への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST07 に残します。ログとの照合を補助する 緊急再始動 では DFS680I を補助値として RST07 へ保存します。主判定のログとの照合ではリスタート・再始動点の 通常再始動 から DFS058I を読み RST07 へ残します。証跡照合のログとの照合ではリスタート・再始動点の DFS058I と DFS680I を RST07 に保存します。記録対応のログとの照合ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で リスタート の 通常再始動 と 緊急再始動 を使い 操作とログを対応 します。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS058I を読み対象 RST07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. /NRESTART BUILDQが応答を返した時点で正常とする。応答中のDFS058Iの値は記録しない。DFS3499IをDFS058Iと同じ判定値とみなし対象RST07の主証跡にする。</li><li>B. /NRESTART BUILDQのコマンド文字列だけを記録する。DFS058Iを含む応答行は保存しない。</li><li>C. DFS058Iを含む通常再始動の応答行を保存する。その応答を得るため/NRESTART BUILDQを使用する。対象RST07の使用チェックポイントとBUILDQ結果として記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. IMS再始動点の停止または再定義を実施する。その後に/NRESTART BUILDQでDFS058Iを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Cは通常再始動で DFS058I を読み使用チェックポイントとBUILDQ結果の主値として操作とログを対応しRST07に残します。
機能の仕組み: ログとの照合では緊急再始動を補助操作としIMS再始動点の時刻と対象識別子をDFS680Iと対象RST07で照合します。
各候補の評価: 通常再始動と緊急再始動の役割を分けるとA: 応答の有無だけでは使用チェックポイントとBUILDQ結果を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけでは使用チェックポイントとBUILDQ結果を証明できない点で一次資料と一致しません、C: DFS058Iの実値を対象別に残す点でRST07を判定できます、D: 変更前の使用チェックポイントとBUILDQ結果を失う点で緊急再始動の範囲を越えます。結論としてログとの照合のリスタート・再始動点で判定する対象は RST07 です。
用語の定義: ログとの照合で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 ログとの照合 RST07</strong></p><p>検証目的: リスタートのIMS再始動点について操作とログを対応し、RST07の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST07の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST07の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST07の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の DFS3499I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0178"><h3>リスタート IMS再始動点 代替経路の確認 RST10</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>代替経路の確認では リスタート の 通常再始動 を主操作として RST10 を判定します。主経路との役割差への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST10 に残します。代替経路の確認を補助する 緊急再始動 では DFS680I を補助値として RST10 へ保存します。主判定の代替経路の確認ではリスタート・再始動点の 通常再始動 から DFS058I を読み RST10 へ残します。証跡照合の代替経路の確認ではリスタート・再始動点の DFS058I と DFS680I を RST10 に保存します。記録対応の代替経路の確認ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で リスタート の 通常再始動 と 緊急再始動 を照合し 主経路との役割差 を確かめます。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS058I を読む前に対象 RST10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. /NRESTART BUILDQのコマンド文字列だけを記録する。DFS058Iを含む応答行は保存しない。</li><li>B. /NRESTART BUILDQと/ERESTART CHKPT 0の対象名をそろえる。前者のDFS058Iを使用チェックポイントとBUILDQ結果の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. IMS再始動点の停止または再定義を実施する。その後に/NRESTART BUILDQでDFS058Iを採取する。</li><li>D. オンライン変更のIMPORT完了コードとメンバー反映を確認する。その値をリスタートのRST10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Bは通常再始動で DFS058I を読み使用チェックポイントとBUILDQ結果の主値として代替手段の成立を確認しRST10に残します。
運用上の背景: 代替経路の確認では緊急再始動を補助操作としIMS再始動点の主経路との役割差をDFS680Iと対象RST10で照合します。
候補別の検討: 通常再始動と緊急再始動の役割を分けるとA: 入力記録だけでは使用チェックポイントとBUILDQ結果を証明できない点で一次資料と一致しません、B: 同じ対象名のDFS058Iを採用する点でRST10を判定できます、C: 変更前の使用チェックポイントとBUILDQ結果を失う点で緊急再始動の範囲を越えます、D: オンライン変更の値ではDFS058Iを確認できない点でRST10の値を示しません。結論として代替経路の確認のリスタート・再始動点で判定する対象は RST10 です。
重要用語の定義: 代替経路の確認で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 代替経路の確認 RST10</strong></p><p>検証目的: リスタートのIMS再始動点について代替手段の成立を確認し、RST10の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST10の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST10の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST10の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の DFS3499I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0179"><h3>リスタート IMS再始動点 変更前の確認 RST02</h3><p class="kb-meta">分類: リスタート ・ 難易度: 初級</p><p>変更前の確認では リスタート の 緊急再始動 を主操作として RST02 を判定します。変更対象と非対象の境界への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST02 に残します。変更前の確認を補助する 再始動記録 では DFS3499I を補助値として RST02 へ保存します。主判定の変更前の確認ではリスタート・再始動点の 緊急再始動 から DFS680I を読み RST02 へ残します。証跡照合の変更前の確認ではリスタート・再始動点の DFS680I と DFS3499I を RST02 に保存します。記録対応の変更前の確認ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で リスタート の 緊急再始動 と 再始動記録 を実施し IMS再始動点 の役割を確認します。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。対象 RST02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. /ERESTART CHKPT 0を対象名なしで実行する。一覧の先頭行をRST02の結果として記録する。</li><li>B. 対象RST02について/ERESTART CHKPT 0の応答からDFS680Iを確認する。/DISPLAY OLDSは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存した/ERESTART CHKPT 0の結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのRST02の出力を再利用する。今回の/ERESTART CHKPT 0と/DISPLAY OLDSは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: Bは緊急再始動で DFS680I を読み使用チェックポイントとBUILDQ結果の主値として変更前の証跡を保存しRST02に残します。
動作の背景: 変更前の確認では再始動記録を補助操作としIMS再始動点の変更対象と非対象の境界をDFS3499Iと対象RST02で照合します。
各選択肢の検討: 緊急再始動と再始動記録の役割を分けるとA: 先頭行はRST02と確定できない点で変更前の確認に合いません、B: DFS680Iと補助証跡の時刻を合わせる点で緊急再始動に合います、C: 採取時刻が異なる点でリスタートに使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でIMS再始動点に使えません。結論として変更前の確認のリスタート・再始動点で判定する対象は RST02 です。
初出用語の定義: 変更前の確認で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 変更前の確認 RST02</strong></p><p>検証目的: リスタートのIMS再始動点について変更前の証跡を保存し、RST02の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST02の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST02の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST02の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS058I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>
